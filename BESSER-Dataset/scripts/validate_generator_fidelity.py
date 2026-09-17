#!/usr/bin/env python3
"""Cross-reference the BUML model's declared structure against the generated
code's actual structure, to check whether the code generator faithfully
reproduced what the diagram declares.

Two genuinely independent artifacts, never compared against each other before:
  - `model_metadata.json` -- structural counts read from the BUML *model*
    itself via `besser` (generate_model_metadata.py). What the diagram says.
  - `code_structure.json` -- structural counts read from `python_code.py`'s
    actual syntax tree via tree-sitter (generate_code_structure.py). What the
    generated code actually has.

Both must already exist per model (this script creates neither) -- run
`generate_model_metadata.py` / `generate_code_structure.py` first if either
is missing for a model.

Which fields are actually comparable, and why some deltas are EXPECTED:
  - `classes` vs `classes` -- directly comparable, should match closely.
    Known systematic exception: a class whose BUML name contains characters
    invalid in a Python identifier (e.g. "#") is still one real class on
    both sides, so this alone shouldn't cause a mismatch; a genuine
    generation failure (a class silently dropped) would.
  - `abstract_classes` vs `abstract_classes` -- comparable, but tree-sitter's
    notion (an `ABC` base or an `@abstractmethod`-decorated method) doesn't
    necessarily match the BUML model's own `is_abstract` flag on a Class --
    confirmed dataset-wide (300-model sample) that 0/732 methods are
    actually `@abstractmethod` here, so any nonzero code-side abstract
    count while the model-side is high suggests the flag isn't propagated
    into the generated base classes as `ABC`.
  - `enumerations` vs `enum_classes` -- comparable, should match closely.
  - `attributes` vs `attributes` -- NOT directly comparable, by design, and
    a mismatch here is EXPECTED, not a bug: model_metadata.json counts only
    attributes the BUML model directly declares on a Class; code_structure.json
    counts every `self.x = ...` assignment in `__init__` plus every
    class-body assignment, which ALSO includes association-derived
    accessors (each BinaryAssociation contributes an attribute-like accessor
    to a class -- see generate_structural_tests.py's association-end
    mapping). So code-side attributes >= model-side attributes is the
    normal case; reported for visibility, not flagged as a defect.
  - `methods` vs `methods` -- similarly not directly comparable: BUML
    "methods" are declared Operations only; tree-sitter "methods" counts
    every function in a class body, including `__init__` and every
    `@property`/`@x.setter` accessor generated for each attribute/
    association end. Code-side will always be much larger; reported for
    visibility, not flagged.
  - No comparison attempted for `generalizations`/`associations`/
    `aggregation`/`composition` (model-only -- tree-sitter deliberately
    doesn't extract relationships, see extract_structure.py) or
    `module_functions`/`dataclasses` (code-only -- no BUML equivalent).

Usage:
    python scripts/validate_generator_fidelity.py [--models-file PATH]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--workers N] [--limit N] [--fresh] [--write-metadata]
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import platform
from pathlib import Path

MODEL_METADATA_FILENAME = "model_metadata.json"
CODE_STRUCTURE_FILENAME = "code_structure.json"
METADATA_FILENAME = "code_metadata.json"
METADATA_KEY = "generator_fidelity_validation"

# (model_metadata.json field, code_structure counts field) -- directly
# comparable pairs only; see module docstring for why attributes/methods
# are reported without being flagged as mismatches.
DIRECTLY_COMPARABLE = [
    ("classes", "classes"),
    ("abstract_classes", "abstract_classes"),
    ("enumerations", "enum_classes"),
]
REPORTED_ONLY = [
    ("attributes", "attributes"),
    ("methods", "methods"),
]


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in models_file.read_text().splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


def load_cache(cache_path: Path) -> dict[str, dict]:
    cached: dict[str, dict] = {}
    if not cache_path.is_file():
        return cached
    with cache_path.open("r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                result = json.loads(line)
            except json.JSONDecodeError:
                continue
            cached[result["model"]] = result
    return cached


def compare_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "error_message": None,
        "model_counts": None,
        "code_counts": None,
        "comparable_deltas": None,
        "reported_deltas": None,
        "has_mismatch": None,
        "code_has_parse_error": None,
    }

    mm_path = model_dir / MODEL_METADATA_FILENAME
    cs_path = model_dir / CODE_STRUCTURE_FILENAME
    if not mm_path.is_file():
        result["error_message"] = f"{MODEL_METADATA_FILENAME} not found"
        return result
    if not cs_path.is_file():
        result["error_message"] = f"{CODE_STRUCTURE_FILENAME} not found"
        return result

    try:
        model_meta = json.loads(mm_path.read_text(encoding="utf-8"))
        code_struct = json.loads(cs_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        result["status"] = "parse_error"
        result["error_message"] = str(exc)
        return result

    if model_meta.get("status") != "measured":
        result["status"] = "model_metadata_unusable"
        result["error_message"] = f"model_metadata.json status is {model_meta.get('status')!r}, not 'measured'"
        return result

    classes = code_struct.get("classes", [])
    code_counts = {
        "classes": len(classes),
        "attributes": sum(len(c["attributes"]) for c in classes),
        "methods": sum(len(c["methods"]) for c in classes),
        "abstract_classes": sum(1 for c in classes if c["is_abstract"]),
        "enum_classes": sum(1 for c in classes if c["is_enum"]),
    }
    result["code_counts"] = code_counts
    result["code_has_parse_error"] = code_struct.get("has_error")
    result["model_counts"] = {k: model_meta.get(k) for k, _ in DIRECTLY_COMPARABLE + REPORTED_ONLY}

    comparable_deltas = {}
    has_mismatch = False
    for model_field, code_field in DIRECTLY_COMPARABLE:
        model_val = model_meta.get(model_field)
        code_val = code_counts.get(code_field)
        delta = code_val - model_val if model_val is not None and code_val is not None else None
        comparable_deltas[model_field] = {"model": model_val, "code": code_val, "delta": delta}
        if delta is not None and delta != 0:
            has_mismatch = True
    result["comparable_deltas"] = comparable_deltas
    result["has_mismatch"] = has_mismatch

    reported_deltas = {}
    for model_field, code_field in REPORTED_ONLY:
        model_val = model_meta.get(model_field)
        code_val = code_counts.get(code_field)
        delta = code_val - model_val if model_val is not None and code_val is not None else None
        reported_deltas[model_field] = {"model": model_val, "code": code_val, "delta": delta}
    result["reported_deltas"] = reported_deltas

    result["status"] = "compared"
    return result


def write_metadata(model_dir: Path, result: dict) -> bool:
    metadata_path = model_dir / METADATA_FILENAME
    if not metadata_path.is_file():
        return False
    try:
        metadata = json.loads(metadata_path.read_text())
    except json.JSONDecodeError:
        return False
    metadata[METADATA_KEY] = {
        "checked_at": result["checked_at"],
        "python_version": result["python_version"],
        "status": result["status"],
        "comparable_deltas": result["comparable_deltas"],
        "reported_deltas": result["reported_deltas"],
        "has_mismatch": result["has_mismatch"],
        "code_has_parse_error": result["code_has_parse_error"],
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
    return True


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    compared = [r for r in results if r["status"] == "compared"]
    mismatched = [r for r in compared if r["has_mismatch"]]

    per_field = {}
    for field, _ in DIRECTLY_COMPARABLE:
        vals = [r["comparable_deltas"][field]["delta"] for r in compared if r["comparable_deltas"][field]["delta"] is not None]
        nonzero = [v for v in vals if v != 0]
        per_field[field] = {
            "models_compared": len(vals),
            "models_with_nonzero_delta": len(nonzero),
            "avg_delta": round(sum(vals) / len(vals), 4) if vals else None,
        }
    for field, _ in REPORTED_ONLY:
        vals = [r["reported_deltas"][field]["delta"] for r in compared if r["reported_deltas"][field]["delta"] is not None]
        per_field[field] = {
            "models_compared": len(vals),
            "avg_delta": round(sum(vals) / len(vals), 4) if vals else None,
        }

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "compared_count": len(compared),
        "mismatched_count": len(mismatched),
        "mismatch_rate": round(len(mismatched) / len(compared), 4) if compared else None,
        "per_field": per_field,
        "mismatched_models": sorted(r["model"] for r in mismatched),
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Generator Fidelity Report (BUML model vs. generated code)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "Cross-references `model_metadata.json` (what the BUML model declares) "
        "against `code_structure.json` (what python_code.py's syntax tree actually "
        "has, via tree-sitter). See the script's docstring for which fields are "
        "directly comparable vs. reported-only.",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Compared:** {report['compared_count']}",
        f"- **Models with a mismatch (classes/abstract_classes/enumerations delta != 0):** "
        f"{report['mismatched_count']} ({(report['mismatch_rate'] or 0) * 100:.2f}%)",
        "",
        "## Directly-comparable fields",
        "",
        "| Field | Compared | Nonzero delta | Avg delta (code - model) |",
        "|---|---|---|---|",
    ]
    for field, _ in DIRECTLY_COMPARABLE:
        p = report["per_field"][field]
        lines.append(f"| {field} | {p['models_compared']} | {p['models_with_nonzero_delta']} | {p['avg_delta']} |")
    lines += [
        "",
        "## Reported-only fields (mismatch EXPECTED, not flagged -- see docstring)",
        "",
        "| Field | Compared | Avg delta (code - model) |",
        "|---|---|---|",
    ]
    for field, _ in REPORTED_ONLY:
        p = report["per_field"][field]
        lines.append(f"| {field} | {p['models_compared']} | {p['avg_delta']} |")
    lines += [
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += ["", "Mismatched models listed in the accompanying `.json` report's `mismatched_models`."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="generator_fidelity_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute every model")
    parser.add_argument("--write-metadata", action="store_true",
                         help="Also write results into each model's code_metadata.json "
                              "under the 'generator_fidelity_validation' key")
    args = parser.parse_args()

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"

    cached_results: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    print(f"Comparing model vs. code structure for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")

    results: list[dict] = list(cached_results.values())
    done = skipped
    cache_file = cache_path.open("a")
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(compare_model, model_dir): model_dir for model_dir in model_dirs}
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "model": model_dir.name, "status": "error", "error_message": str(exc),
                        "model_counts": None, "code_counts": None, "comparable_deltas": None,
                        "reported_deltas": None, "has_mismatch": None, "code_has_parse_error": None,
                    }
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                if done % 500 == 0 or done == total:
                    print(f"  {done}/{total} compared", flush=True)
    finally:
        cache_file.close()

    if args.write_metadata:
        written = 0
        for result in results:
            if result["status"] == "compared":
                model_dir = args.dataset_dir / result["model"]
                if write_metadata(model_dir, result):
                    written += 1
        print(f"Wrote {METADATA_KEY} into {written}/{len(results)} models' code_metadata.json")

    report = build_report(results)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Compared: {report['compared_count']}/{report['total_models']}")
    print(f"Mismatched: {report['mismatched_count']} ({(report['mismatch_rate'] or 0) * 100:.2f}%)")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
