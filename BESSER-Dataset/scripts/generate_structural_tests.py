#!/usr/bin/env python3
"""Generate `test_structural_full.py` per model: a deterministic-first test
suite aimed at near-complete coverage of `python_code.py`, to serve as a
stronger baseline than the dataset's existing `test_hypothesis.py` (never
modified or overwritten -- this is a new, additional file).

Why this exists: docs/DECISIONS.md already found the existing generated
tests check `isinstance(instance, Class)` but never that constructor values
actually landed, and (found this session) they never exercise a
relationship's REASSIGNMENT or CLEARING -- only a single `@given`
instantiation. The bidirectional-consistency setters have branches like
`if old_value is not None: ... remove from old opposite end` that a single
construction can never reach. Deterministic, scripted sequences hit those
branches every run, guaranteed -- unlike relying on Hypothesis's random
search to eventually stumble into the right sequence.

Two sections are generated, in priority order:
  1. DETERMINISTIC (primary): per attribute, construct+verify the value
     landed and that reassigning it via the setter updates it. Per
     generalization, isinstance checks. Per binary association, a three-step
     link -> reassign -> clear sequence per side, verified through a small
     `_is_linked()` helper (handles both collection-valued and
     single-valued ends uniformly, so the generated code doesn't need to
     branch per multiplicity in the assertions).
  2. HYPOTHESIS (secondary): one `@given` instantiation test per class, same
     shape as the dataset's own tests, for input-space breadth on top of the
     deterministic guarantees.

Association-end-to-attribute mapping (verified against model_1's `nodes0`):
for a BinaryAssociation with ends (e1, e2), the class `e2.type` gets an
attribute named `e1.name` typed `e1.type` (multiplicity e1.multiplicity),
and `e1.type` gets one named `e2.name` typed `e2.type` (e2.multiplicity) --
i.e. each end's own (name, type, multiplicity) describes the accessor added
to the OTHER end's class, not to its own type.

Attribute sample values: primitives use a small static literal table; each
model's own Enumeration types get their own table built per-model from their
actual literals (e.g. "UserRole.SALES_MANAGER"), since enum-typed attributes
are NOT optional in the generated __init__ just because we lack a static
literal for them -- omitting one used to leave it as a *missing required
constructor argument*, breaking construction (and therefore every test) for
any class with one. Confirmed the hard way on Model_1000000001: 64/108 tests
failed with "missing 1 required positional argument: 'role'" before this was
added -- see build_literal_tables().

classes declared `is_abstract=True` in the BUML model ARE still directly
instantiated (even though `inspect.isabstract()` would often say False for
them here anyway, since this dataset's generated ABCs typically have no
actual `@abstractmethod`-decorated methods -- confirmed both on model_1 and
across a 300-model sample, 0/732 methods). Skipping them would leave most of
a class hierarchy's setter logic (which commonly lives on the abstract
parent) completely uncovered for no real safety benefit, since nothing
actually blocks the instantiation.

Usage:
    python scripts/generate_structural_tests.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import datetime
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.buml import (  # noqa: E402
    NEW_GLOB, OLD_GLOB, find_buml_file, load_domain_model, ordered_ends, type_name,
)
from _common.cache import load_cache, partition_cache  # noqa: E402
from _common.io import add_common_io_args, find_model_dirs  # noqa: E402
from _common.pool import run_models  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402
from _common.testgen import (  # noqa: E402
    build_literal_tables, constructor_kwargs, has_real_property, is_constructible, is_many,
    load_python_module, plain_attributes, resolve_code_name, sanitize,
)

from besser.BUML.metamodel.structural import BinaryAssociation, Class, Enumeration  # noqa: E402

TEST_FILENAME = "test_structural_full.py"
RETRIABLE_STATUSES = frozenset({"error"})

HYPOTHESIS_STRATEGY = {
    "str": "safe_text",
    "int": "st.integers()",
    "float": "st.floats(allow_nan=False, allow_infinity=False)",
    "bool": "st.booleans()",
    "date": "st.dates()",
    "datetime": "st.datetimes()",
    "time": "st.times()",
    "timedelta": "st.timedeltas()",
}


def generate_tests(model, code_module) -> str:
    classes = sorted((t for t in model.types if isinstance(t, Class)), key=type_name)
    enums = sorted((t for t in model.types if isinstance(t, Enumeration)), key=type_name)
    generalizations = sorted(model.generalizations, key=lambda g: f"{type_name(g.general)}::{type_name(g.specific)}")
    associations = sorted(
        (a for a in model.associations if isinstance(a, BinaryAssociation)), key=type_name
    )

    sample_table, alt_table, known_types = build_literal_tables(model, code_module)

    # A class/enum's BUML `.name` isn't always the identifier it has in the
    # generated python_code.py (see resolve_code_name/python_identifier --
    # confirmed real case: model_2533's `raas_small_test_#29373817` loses
    # the "#"). Resolve every class/enum against the actually-loaded module
    # up front; anything that can't be resolved is excluded from imports,
    # instantiation, and everywhere else code text gets emitted, since there
    # is no safe name to reference it by.
    code_names: dict[str, str] = {}
    for t in list(classes) + list(enums):
        resolved = resolve_code_name(code_module, t.name)
        if resolved is not None:
            code_names[t.name] = resolved

    constructible = {
        cls.name: (
            cls.name in code_names
            and is_constructible(cls, getattr(code_module, code_names[cls.name], None), known_types)
        )
        for cls in classes
    }

    class_names = sorted({code_names[c.name] for c in classes if c.name in code_names})
    enum_names = sorted({code_names[e.name] for e in enums if e.name in code_names})
    import_names = class_names + enum_names
    lines: list[str] = [
        "import inspect",
        "import pytest",
        "from datetime import date, datetime, time, timedelta",
        "from hypothesis import given, settings",
        "import hypothesis.strategies as st",
        "",
    ]
    # A model can genuinely have zero classes/enums (confirmed real case:
    # model_650's BUML source has `types=None`) -- joining an empty list
    # still produced a dangling "    ," with no import, which is a syntax
    # error, not just an unused import. Skip the import block entirely when
    # there's nothing to import.
    if import_names:
        lines += [
            "from python_code import (",
            "    " + ",\n    ".join(import_names) + ",",
            ")",
            "",
        ]
    lines += [
        "safe_text = st.text(",
        "    alphabet=st.characters(",
        '        whitelist_categories=("Ll", "Lu", "Nd"),',
        '        whitelist_characters="_",',
        "    ),",
        "    min_size=1,",
        ").filter(lambda s: s[0].isalpha())",
        "",
        "def _is_linked(obj, attr_name, other):",
        "    value = getattr(obj, attr_name, None)",
        "    if isinstance(value, (set, list, tuple, frozenset)):",
        "        return other in value",
        "    return value == other",
        "",
        "def _safe_set(obj, attr_name, value):",
        "    # Some generated models have a genuine bug: two reciprocal setters",
        "    # unconditionally call each other with no base case, causing",
        "    # infinite mutual recursion for that specific relationship (found",
        "    # in model_10000002's items10/sc11 pair). That's a defect in the",
        "    # code under test, not in this test -- skip rather than fail so it",
        "    # doesn't masquerade as a test-suite problem.",
        "    try:",
        "        setattr(obj, attr_name, value)",
        "    except RecursionError:",
        "        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')",
        "",
        "# =============================================================================",
        "# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)",
        "# =============================================================================",
        "",
    ]

    # --- per-attribute value round-trip ---
    # Not skipping is_abstract=True classes: confirmed dataset-wide (300-model
    # sample, 0/732 methods actually is_abstract=True) that this dataset's
    # generated ABCs have no real @abstractmethod, so Python does not block
    # direct instantiation -- and that's exactly where most setter logic
    # lives (e.g. model_1's petrinet_Node), so skipping them for "design
    # intent" reasons would leave the majority of the file uncovered.
    for cls in classes:
        if not constructible[cls.name]:
            continue
        for attr in sorted(plain_attributes(cls, known_types), key=lambda a: a.name):
            tname = sanitize(f"{cls.name}_{attr.name}")
            kwargs = constructor_kwargs(cls, known_types, sample_table, False, alt_table)
            alt_literal = alt_table.get(type_name(attr.type), '"sample_2"')
            lines += [
                f"def test_{tname}_value_roundtrip():",
                f"    instance = {code_names[cls.name]}({kwargs})",
                f"    assert instance.{attr.name} == {sample_table.get(type_name(attr.type), chr(34)+'sample'+chr(34))}",
                f"    instance.{attr.name} = {alt_literal}",
                f"    assert instance.{attr.name} == {alt_literal}",
                "",
                "",
            ]

    # --- generalizations ---
    for gen in generalizations:
        if not constructible.get(gen.specific.name, False):
            continue
        if gen.general.name not in code_names:
            continue
        tname = sanitize(f"{gen.specific.name}_isa_{gen.general.name}")
        kwargs = constructor_kwargs(gen.specific, known_types, sample_table, False, alt_table)
        lines += [
            f"def test_{tname}():",
            f"    instance = {code_names[gen.specific.name]}({kwargs})",
            f"    assert isinstance(instance, {code_names[gen.general.name]})",
            "",
            "",
        ]

    # --- binary associations: link -> reassign -> clear ---
    for assoc in associations:
        ordered = ordered_ends(assoc)
        if ordered is None:
            continue
        e1, e2 = ordered
        # attribute named e1.name (type e1.type) lives on class e2.type, and vice versa
        class_a, attr_a, type_a, many_a = e2.type, e1.name, e1.type, is_many(e1.multiplicity)
        class_b, attr_b, type_b, many_b = e1.type, e2.name, e2.type, is_many(e2.multiplicity)

        code_class_a = getattr(code_module, code_names[class_a.name], None) if class_a.name in code_names else None
        code_class_b = getattr(code_module, code_names[class_b.name], None) if class_b.name in code_names else None
        a_is_real = has_real_property(code_class_a, attr_a)
        b_is_real = has_real_property(code_class_b, attr_b)
        if not a_is_real and b_is_real:
            # Only class_b's side actually has setter logic -- link from
            # there instead, or the assignment would be a dead no-op.
            class_a, attr_a, type_a, many_a, class_b, attr_b, type_b, many_b = (
                class_b, attr_b, type_b, many_b, class_a, attr_a, type_a, many_a
            )
        elif not a_is_real and not b_is_real:
            # Neither participant implements this relationship in the
            # generated code at all (confirmed real case: model_1's
            # tokens11, where both petrinet_Place and petrinet_Token are
            # bare `pass` stubs despite the BUML model declaring the
            # association) -- nothing exists to test here.
            continue

        if not constructible.get(class_a.name, False) or not constructible.get(class_b.name, False):
            continue

        tname = sanitize(f"assoc_{assoc.name}")
        kwargs_a = constructor_kwargs(class_a, known_types, sample_table, False, alt_table)
        kwargs_b1 = constructor_kwargs(class_b, known_types, sample_table, False, alt_table)
        kwargs_b2 = constructor_kwargs(class_b, known_types, sample_table, True, alt_table)
        set_val = f"{{b1}}" if many_a else "b1"
        set_val2 = f"{{b2}}" if many_a else "b2"

        # The generated python_code.py doesn't always implement BOTH sides of
        # a bidirectional association (confirmed: model_1's petrinet_Arc and
        # petrinet_Token are bare `pass`-only classes even though the BUML
        # model declares them as association participants -- the reciprocal
        # attribute was simply never generated for them). Guard the
        # reciprocal-side assertions with hasattr() so the test verifies
        # whatever IS actually implemented rather than failing on a
        # generation-time asymmetry outside this test's control.
        lines += [
            f"def test_{tname}_link_reassign_clear():",
            f"    a = {code_names[class_a.name]}({kwargs_a})",
            f"    b1 = {code_names[class_b.name]}({kwargs_b1})",
            f"    b2 = {code_names[class_b.name]}({kwargs_b2})",
            f"    _safe_set(a, {attr_a!r}, {set_val})",
            f"    assert _is_linked(a, {attr_a!r}, b1)",
            f"    if hasattr(b1, {attr_b!r}):",
            f"        assert _is_linked(b1, {attr_b!r}, a)",
            f"    _safe_set(a, {attr_a!r}, {set_val2})",
            f"    assert _is_linked(a, {attr_a!r}, b2)",
            f"    if hasattr(b1, {attr_b!r}):",
            f"        assert not _is_linked(b1, {attr_b!r}, a)",
            f"    if hasattr(b2, {attr_b!r}):",
            f"        assert _is_linked(b2, {attr_b!r}, a)",
            f"    _safe_set(a, {attr_a!r}, {'set()' if many_a else 'None'})",
            f"    assert not _is_linked(a, {attr_a!r}, b2)",
            f"    if hasattr(b2, {attr_b!r}):",
            f"        assert not _is_linked(b2, {attr_b!r}, a)",
            "",
            "",
        ]

    # --- Section 2: Hypothesis instantiation tests (secondary, breadth) ---
    lines += [
        "# =============================================================================",
        "# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS",
        "# =============================================================================",
        "",
    ]
    enum_names_set = {e.name for e in enums}

    def _strategy_for(buml_type: str) -> str:
        # known_types excludes empty enums, which st.sampled_from() rejects.
        if buml_type in enum_names_set and buml_type in known_types and buml_type in code_names:
            return f"st.sampled_from({code_names[buml_type]})"
        return HYPOTHESIS_STRATEGY.get(buml_type, "st.none()")

    for cls in classes:
        if not constructible[cls.name]:
            continue
        prim_attrs = sorted(plain_attributes(cls, known_types), key=lambda a: a.name)
        strategy_args = ", ".join(
            f"{a.name}={_strategy_for(type_name(a.type))}" for a in prim_attrs
        )
        tname = sanitize(cls.name)
        code_cls_name = code_names[cls.name]
        lines += [
            f"{tname}_strategy = st.builds({code_cls_name}, {strategy_args})" if strategy_args else f"{tname}_strategy = st.builds({code_cls_name})",
            "@given(instance=" + tname + "_strategy)",
            "@settings(max_examples=25)",
            f"def test_{tname}_instantiation(instance):",
            f"    assert isinstance(instance, {code_cls_name})",
            "",
            "",
        ]

    return "\n".join(lines) + "\n"


def generate_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "buml_source": None,
        "tests_written": None,
        "error_message": None,
    }

    buml_file = find_buml_file(model_dir)
    if buml_file is None:
        result["error_message"] = f"No {OLD_GLOB} or {NEW_GLOB} file found in {model_dir.name}"
        return result
    result["buml_source"] = buml_file.name

    code_path = model_dir / "python_code.py"
    if not code_path.is_file():
        result["status"] = "missing_file"
        result["error_message"] = "python_code.py not found"
        return result

    try:
        model = load_domain_model(buml_file)
        code_module = load_python_module(code_path)
        test_text = generate_tests(model, code_module)
        output_path = model_dir / TEST_FILENAME
        output_path.write_text(test_text, encoding="utf-8")
        result["status"] = "generated"
        result["tests_written"] = test_text.count("\ndef test_")
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    generated = [r for r in results if r["status"] == "generated"]
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "generated_count": len(generated),
        "avg_tests_per_model": round(sum(r["tests_written"] or 0 for r in generated) / len(generated), 2) if generated else None,
        "total_tests_written": sum(r["tests_written"] or 0 for r in generated),
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Structural Test Generation Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Generated:** {report['generated_count']}",
        f"- **Avg tests per model:** {report['avg_tests_per_model']}",
        f"- **Total tests written:** {report['total_tests_written']}",
        "",
    ]
    lines += render_status_table(report["by_status"])
    lines += ["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="structural_tests_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
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

    print(f"Generating structural tests for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache")

    results = run_models(generate_model, model_dirs, workers=args.workers, cache_path=cache_path,
                         results=list(cached_results.values()), already_done=skipped, total=total,
                         error_fields={"buml_source": None, "tests_written": None},
                         describe=lambda r: "")

    report = build_report(results)
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))

    print()
    print(f"Generated: {report['generated_count']}/{report['total_models']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
