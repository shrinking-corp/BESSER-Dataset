#!/usr/bin/env python3
"""Cross-reference the BUML model's declared structure against the generated
code's actual structure **by name**, not by count.

Complements (does not replace or modify) `validate_generator_fidelity.py`,
which only ever compares totals (e.g. "model says 5 classes, code has 6").
Flagged 2026-10-01: a count match is close to meaningless on its own -- two
totals can agree while referring to entirely different, unrelated names. The
real question ("did the generator actually produce *this specific* class/
attribute/operation the model declares?") requires checking name sets, not
totals. This matters beyond today's dataset too: it's the right-shaped check
for validating whether an LLM (or any other generator) produced code with
*all the necessary* classes/methods/attributes, not just the right number of
each -- a count match tells you nothing about that.

Two genuinely independent artifacts, same pair `validate_generator_fidelity.py`
uses, read differently here:
  - The live BUML model itself (via `besser` -- requires `.venv-puml`, NOT
    `model_metadata.json`, which only stores aggregate counts, no names at
    all). Reuses `generate_structural_tests.py`'s own BUML-loading and
    identifier-sanitization helpers (`find_buml_file`, `load_domain_model`,
    `python_identifier`) rather than reimplementing them -- that logic
    already handles real, confirmed edge cases (e.g. a BUML name containing
    "#", invalid in a Python identifier, which the actual code generator
    silently strips; model_2533 is the known example).
  - `code_structure.json` -- tree-sitter's view of `python_code.py`'s actual
    classes/attributes/methods, by name.

What counts as a real mismatch vs. expected, reported-only noise (same
philosophy as the count-based script, applied at name granularity):
  - **Classes**: a BUML class whose name (raw, sanitized, or pluralized --
    see below) has no matching class in the code at all is a real miss --
    nothing to argue about.
  - **Attributes**: a BUML-declared attribute whose name doesn't resolve
    (raw, sanitized, or disambiguated -- see below) against its matched
    class's code-side `attributes` **or** `methods` names is a real miss.
    The reverse (code attributes not in the model) is NOT flagged --
    expected, since association ends also contribute accessor attributes
    the BUML `Class.attributes` list never includes (same reason
    `validate_generator_fidelity.py`'s attribute counts never match).
  - **Operations**: a BUML-declared Operation whose name doesn't appear
    anywhere in its matched class's code-side `methods` list is a real
    miss. The reverse (code methods not matching any operation -- `__init__`,
    property getters/setters) is NOT flagged, for the same reason.

**Found and fixed 2026-10-11, root-caused by actually reading the generated
code for several of the 22 models the original version of this script
flagged as mismatched** (not by guessing): all 22 were false positives in
*this script's* resolution logic, not real generator or tree-sitter defects.
Two concrete, confirmed patterns, both now handled:

1. **Attribute name collides with a Python keyword/builtin
   (`property`, `self`) -- 20/22 models.** The generator disambiguates,
   but inconsistently across the dataset (confirmed on real examples, not
   assumed to be uniform): sometimes only the *internal* backing
   field/constructor-parameter gets a suffix while the *public* `@property`
   accessor keeps the original name (`model_116`: attribute `self` ->
   backing field `self_`, but `def self(self): ...` is still the public
   getter -- confirmed directly in `code_structure.json`: tree-sitter put
   `"self"` in that class's `methods` list, not `attributes`, which the old
   version of this script never checked). Other times both the backing
   field AND the public accessor get the SAME numeric suffix instead
   (`model_100505`: attribute `self` -> `self1` end-to-end;
   `model_10001303`: attribute `property` -> `property1` end-to-end --
   confirmed `"property1"` appears in `code_structure.json`, never
   `"property"` alone). Fixed by resolving an attribute's name against the
   UNION of the matched class's `attributes` and `methods` names, trying
   raw name, `python_identifier`-sanitized name, AND a `+ "1"`-suffixed
   form of each.
2. **`Factura` -> `Facturas` pluralization -- 2/22 models.** Already known
   and already handled in `generate_structural_tests.py`'s own
   `resolve_code_name()` (a different script, used when actually writing
   tests against the generated code) -- this script just never carried the
   same rule. Fixed by also trying a `+ "s"`-suffixed form when resolving a
   class name.

Both fixes are deliberately narrow (one extra fallback name-set, two extra
suffix forms) rather than a general fuzzy-match, to avoid trading false
"missing" reports for false "found" ones. A third, even narrower fallback
(case-insensitive match, tried only after every exact-form candidate above)
was added for one more confirmed real case: `model_10001897`'s `Codigo`
BUML attribute resolves to the generated code's `codigo`.

**Re-verified against exactly these 22 models (never a full/sampled
dataset run): 20/22 now resolve cleanly.** The remaining 2 are genuinely
different from each other, not a leftover resolution gap: `model_10001897`
has exactly one real, unresolvable miss (`Fecha`, absent from the generated
code under any name or case this script tries); `model_10001985` -- despite
being lumped together with `model_10001897` as "the Factura pair" in
earlier project notes -- turns out to have an entirely different, more
complex structure: its BUML `Factura` class has no single matching class in
the code at all, splitting instead into two package/layer-qualified classes
(`LogicaPresentacion___Factura_Component`, `Persistencia___Factura_Component`)
-- not a simple pluralization, and not chased further here.

Usage:
    python scripts/validate_generator_fidelity_names.py --models-file PATH
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--workers N] [--limit N] [--fresh]

Requires `.venv-puml` (where `besser` is installed), not the main `.venv`.
"""
from __future__ import annotations

import argparse
import datetime
import json
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.buml import find_buml_file, load_domain_model, type_name  # noqa: E402
from _common.cache import load_cache, partition_cache  # noqa: E402
from _common.io import add_common_io_args, find_model_dirs  # noqa: E402
from _common.pool import run_models  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402
from _common.testgen import python_identifier  # noqa: E402
from besser.BUML.metamodel.structural import Class  # noqa: E402

CODE_STRUCTURE_FILENAME = "code_structure.json"
# "missing_file"/"missing_code_structure" are permanent facts about a model's
# input data, not transient failures, so only "error" is auto-retried.
RETRIABLE_STATUSES = frozenset({"error"})


def resolve_name_in_set(raw_name: str, known_names: set[str], extra_suffixes: tuple[str, ...] = ()) -> str | None:
    """Same base resolution rule as generate_structural_tests.py's
    resolve_code_name() (raw name, then python_identifier-sanitized name),
    against a plain name set (from code_structure.json) instead of a live
    module's hasattr() -- there is no running python_code.py here, only
    tree-sitter's static extraction.

    `extra_suffixes` adds further candidate forms on top of raw/sanitized --
    e.g. ("1",) to also try `{raw_name}1` -- for the generator's own
    keyword/builtin-collision-avoidance renaming (confirmed real, see module
    docstring's 2026-10-11 entry). Tried in addition to, not instead of, the
    base forms, since most names need no disambiguation at all.
    """
    candidates = [raw_name]
    sanitized = python_identifier(raw_name)
    if sanitized != raw_name:
        candidates.append(sanitized)
    for suffix in extra_suffixes:
        candidates.append(f"{raw_name}{suffix}")
        if sanitized != raw_name:
            candidates.append(f"{sanitized}{suffix}")
    for candidate in candidates:
        if candidate in known_names:
            return candidate
    # Last resort: case-insensitive match. Confirmed real and needed
    # (2026-10-11, model_10001897): BUML's `Codigo` attribute, capitalized,
    # resolves to the generated code's `codigo`, lowercase -- while that
    # same class's other attributes (nif, nombre, direccionPostal) are
    # already lowercase on BOTH sides, suggesting this specific case
    # mismatch is a quirk of the source BUML model's own data entry, not a
    # systematic generator rule worth a dedicated suffix form. Tried only
    # after every exact-form candidate above, to prefer an exact match
    # whenever one exists.
    lowered = {n.lower(): n for n in known_names}
    for candidate in candidates:
        if candidate.lower() in lowered:
            return lowered[candidate.lower()]
    return None


def compare_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "error_message": None,
        "classes_missing_from_code": None,
        "classes_extra_in_code": None,
        "per_class_detail": None,
        "total_classes_missing": None,
        "total_attributes_missing": None,
        "total_operations_missing": None,
        "has_mismatch": None,
    }

    buml_file = find_buml_file(model_dir)
    cs_path = model_dir / CODE_STRUCTURE_FILENAME
    if buml_file is None:
        result["error_message"] = "no BUML source file found"
        return result
    if not cs_path.is_file():
        result["status"] = "missing_code_structure"
        result["error_message"] = f"{CODE_STRUCTURE_FILENAME} not found"
        return result

    try:
        model = load_domain_model(buml_file)
        code_struct = json.loads(cs_path.read_text(encoding="utf-8"))
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
        return result

    code_classes = code_struct.get("classes", [])
    code_classes_by_name = {c["name"]: c for c in code_classes}
    code_class_names = set(code_classes_by_name.keys())

    buml_classes = [t for t in model.types if isinstance(t, Class)]
    resolved_buml_names: set[str] = set()

    classes_missing: list[str] = []
    per_class_detail: dict[str, dict] = {}
    total_attrs_missing = 0
    total_ops_missing = 0

    for cls in sorted(buml_classes, key=type_name):
        # "s" fallback: the generator pluralizes some class names
        # (Factura -> Facturas, confirmed, see module docstring) --
        # independent of the raw/sanitized forms tried by default.
        resolved = resolve_name_in_set(cls.name, code_class_names, extra_suffixes=("s",))
        if resolved is None:
            classes_missing.append(cls.name)
            continue
        resolved_buml_names.add(resolved)

        code_class = code_classes_by_name[resolved]
        code_attr_names = {a["name"] for a in code_class.get("attributes", [])}
        code_method_names = {m["name"] for m in code_class.get("methods", [])}
        # Attributes resolve against attrs UNION methods, plus a "1" suffix
        # fallback -- the generator's keyword/builtin-collision-avoidance
        # renaming sometimes keeps the original name on the public @property
        # accessor (which tree-sitter files under `methods`, not
        # `attributes`) and sometimes suffixes both the backing field and
        # the public accessor with "1" instead. Both confirmed real, see
        # module docstring's 2026-10-11 entry.
        code_attr_or_method_names = code_attr_names | code_method_names

        attrs_missing = sorted(
            a.name for a in cls.attributes
            if resolve_name_in_set(a.name, code_attr_or_method_names, extra_suffixes=("1",)) is None
        )
        ops_missing = sorted(
            op.name for op in cls.methods
            if resolve_name_in_set(getattr(op, "name", str(op)), code_method_names) is None
        )

        if attrs_missing or ops_missing:
            per_class_detail[cls.name] = {
                "resolved_code_name": resolved,
                "attributes_missing_from_code": attrs_missing,
                "operations_missing_from_code": ops_missing,
            }
        total_attrs_missing += len(attrs_missing)
        total_ops_missing += len(ops_missing)

    classes_extra = sorted(code_class_names - resolved_buml_names)

    result["classes_missing_from_code"] = sorted(classes_missing)
    result["classes_extra_in_code"] = classes_extra
    result["per_class_detail"] = per_class_detail
    result["total_classes_missing"] = len(classes_missing)
    result["total_attributes_missing"] = total_attrs_missing
    result["total_operations_missing"] = total_ops_missing
    result["has_mismatch"] = bool(classes_missing or total_attrs_missing or total_ops_missing)
    result["status"] = "compared"
    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    compared = [r for r in results if r["status"] == "compared"]
    mismatched = [r for r in compared if r["has_mismatch"]]
    with_missing_classes = [r for r in compared if r["total_classes_missing"]]
    with_missing_attrs = [r for r in compared if r["total_attributes_missing"]]
    with_missing_ops = [r for r in compared if r["total_operations_missing"]]

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": dict(sorted(by_status.items(), key=lambda kv: -kv[1])),
        "compared_count": len(compared),
        "mismatched_count": len(mismatched),
        "mismatch_rate": round(len(mismatched) / len(compared), 4) if compared else None,
        "models_with_missing_classes": len(with_missing_classes),
        "models_with_missing_attributes": len(with_missing_attrs),
        "models_with_missing_operations": len(with_missing_ops),
        "total_classes_missing_sum": sum(r["total_classes_missing"] for r in compared),
        "total_attributes_missing_sum": sum(r["total_attributes_missing"] for r in compared),
        "total_operations_missing_sum": sum(r["total_operations_missing"] for r in compared),
        "worst_models_by_total_missing": sorted(
            (
                {
                    "model": r["model"],
                    "classes_missing": r["total_classes_missing"],
                    "attributes_missing": r["total_attributes_missing"],
                    "operations_missing": r["total_operations_missing"],
                    "total": r["total_classes_missing"] + r["total_attributes_missing"] + r["total_operations_missing"],
                }
                for r in compared if r["has_mismatch"]
            ),
            key=lambda x: -x["total"],
        )[:50],
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Generator Fidelity Report, by NAME (BUML model vs. generated code)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "Unlike `generator_fidelity_report` (counts only), this checks whether "
        "each specific class/attribute/operation the model declares actually "
        "exists in the generated code, by name -- a count match does not imply "
        "a name match. See the script's docstring for what counts as a real "
        "miss vs. expected, unflagged asymmetry (code-side association "
        "accessors / `__init__` / property getters-setters, same reasoning as "
        "the count-based report).",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Compared:** {report['compared_count']}",
        f"- **Models with >=1 real mismatch:** {report['mismatched_count']} "
        f"({(report['mismatch_rate'] or 0) * 100:.2f}%)",
        f"- **Models with >=1 missing class:** {report['models_with_missing_classes']}",
        f"- **Models with >=1 missing attribute:** {report['models_with_missing_attributes']}",
        f"- **Models with >=1 missing operation:** {report['models_with_missing_operations']}",
        f"- **Total missing classes across dataset:** {report['total_classes_missing_sum']}",
        f"- **Total missing attributes across dataset:** {report['total_attributes_missing_sum']}",
        f"- **Total missing operations across dataset:** {report['total_operations_missing_sum']}",
        "",
    ]
    lines += render_status_table(report["by_status"])
    lines += [
        "",
        "## Top 50 worst models (by total missing classes+attributes+operations)",
        "",
        "| Model | Classes missing | Attributes missing | Operations missing | Total |",
        "|---|---|---|---|---|",
    ]
    for m in report["worst_models_by_total_missing"]:
        lines.append(f"| {m['model']} | {m['classes_missing']} | {m['attributes_missing']} | "
                      f"{m['operations_missing']} | {m['total']} |")
    lines += ["", "Full per-model, per-class detail (exact missing names): see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="generator_fidelity_names_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute every model")
    args = parser.parse_args()

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"

    cached_results_all: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()
    cached_results, retriable = partition_cache(cached_results_all, RETRIABLE_STATUSES)

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    print(f"Comparing model vs. code structure BY NAME for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache -- "
              f"same report, no separate retry run needed")

    results = run_models(
        compare_model, model_dirs, workers=args.workers, cache_path=cache_path,
        results=list(cached_results.values()), already_done=skipped, total=total,
        error_fields={"classes_missing_from_code": None, "classes_extra_in_code": None,
                      "per_class_detail": None, "total_classes_missing": None,
                      "total_attributes_missing": None, "total_operations_missing": None,
                      "has_mismatch": None},
    )

    report = build_report(results)
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))

    print()
    print(f"Compared: {report['compared_count']}/{report['total_models']}")
    print(f"Mismatched (by name): {report['mismatched_count']} ({(report['mismatch_rate'] or 0) * 100:.2f}%)")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
