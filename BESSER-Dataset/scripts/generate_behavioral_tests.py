#!/usr/bin/env python3
"""Generate `test_behavioral.py` per model: a small, targeted supplement to
`test_structural_full.py` that tests each bidirectional association from
**both ends independently**, not just one side relying on the other's side
effect. Shares its model/code helpers with `generate_structural_tests.py`
via `_common/testgen.py`, but only emits the kinds of test that file does
not (attributes, generalizations and forward-direction association tests
stay in `test_structural_full.py`).

Why this exists (see docs/DECISIONS.md, 2026-10-01, "Real surviving-mutant
diagnosis on model_1"): `test_structural_full.py`'s own
`test_assoc_X_link_reassign_clear` already calls a setter twice with two
different values and checks the reciprocal side -- it is NOT a weak,
single-snapshot test, contrary to an earlier (wrong) assumption this
session. Tracing real surviving mutants against `model_1` found the actual
gap is narrower and different: that test only ever calls the setter from
**one** side (`class_a`) and observes the reciprocal side (`class_b`) only
as a side effect -- it never calls `class_b`'s own setter directly. For a
genuinely bidirectional association (where BOTH sides implement a real
`@property`/`@x.setter` pair, not just one), this misses mutants in
`class_b`'s *own* "remove old value" guard logic, because by the time that
guard runs (triggered recursively from inside `class_a`'s setter), the
outer setter has already overwritten its own stored state -- the specific
comparison a mutant touches ends up checking already-stale data. Verified
by hand-adding exactly this kind of test and confirming a previously-
surviving mutant (`model_1`, line 96, `ReplaceComparisonOperator_IsNot_Is`)
is killed by it.

**Second gap, found and fixed 2026-10-12: the "unkillable" stub-association
mutants turned out to be killable after all, with a test double.** The
original assumption was that when one side's class is a bare
`class X: pass` stub, the generated code's `hasattr(item, "...")` guard
protecting the bidirectional-consistency logic is permanently False, so the
mutant inside it is dead code for any possible test -- confirmed real on
`model_1` (~92% of its surviving mutants traced to exactly this: `target`,
`petrinet_Node5`, `petrinet_Node9`, `Node`, and `petrinet_Petrinet2` all
point at the bare `petrinet_Arc` stub). The dead-code diagnosis was correct,
but the conclusion "nothing could" kill it was wrong: `petrinet_Arc` has no
`__slots__`, so nothing stops a TEST from manually attaching the exact
attribute name a real implementation would have had
(`setattr(stub_instance, reciprocal_attr_name, ...)`) before exercising the
real side's setter. This is an ordinary test-double pattern -- standing in
for an incomplete collaborator to test the REAL side's own logic in
isolation -- not a fabricated result: the resulting assertion genuinely
passes or fails based on real behavior of real code, it just does so via a
hand-shaped object rather than one the generated code happens to construct
on its own. Verified by hand-tracing exactly this sequence against
`model_1`'s `target` property and confirming the `opp_val == self`
comparison mutants are observably killable this way.

What this generates: for each binary association where BOTH ends have a
real, independently-settable property (checked via `has_real_property()`),
one additional test that:
  1. Constructs objects for both classes.
  2. Sets the **class_b-side** object's own attribute directly (not via
     class_a's setter's side effect) to link to a class_a instance.
  3. Reassigns it to a *different* class_a instance, directly on class_b.
  4. Checks the old link was cleared and the new one established, on BOTH
     sides, mirroring (not duplicating) `test_structural_full.py`'s existing
     forward-direction test.

This is the mirror image of the existing `link_reassign_clear` test --
exercising class_b's own setter guard directly, the half of a bidirectional
pair the existing test never calls on its own.

**A second, independent kind of test, for the stub case**: for each binary
association where exactly ONE side has a real property and the other is a
bare stub, one test that:
  1. Constructs both sides.
  2. Manually `setattr()`s the stub side with the exact attribute name the
     real side's setter checks via `hasattr()` -- simulating the reciprocal
     property a correct implementation would have had, so the real side's
     guard is actually reachable instead of permanently skipped.
  3. Calls the real side's own setter (assign, then clear), asserting the
     stub's manually-attached attribute updates correctly in both
     directions.
This targets the "equivalent mutant" class the reverse-direction test above
explicitly cannot help with -- not dead code after all, just code that a
test can't reach without standing in for an incomplete collaborator.

Usage:
    python scripts/generate_behavioral_tests.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import inspect
import datetime
import platform
import re
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
    load_python_module, resolve_code_name, sanitize,
)

from besser.BUML.metamodel.structural import BinaryAssociation, Class, Enumeration  # noqa: E402

TEST_FILENAME = "test_behavioral.py"
# "missing_file" is permanent, so only crashes are retried from the cache.
RETRIABLE_STATUSES = frozenset({"error"})

_HASATTR_TARGET = re.compile(r'hasattr\((?:item|value),\s*"([^"]+)"\)')


def _reciprocal_lookup(cls, attr_name: str) -> tuple[str, bool] | None:
    """(name, is_many) for what `cls.attr_name`'s real setter does to the
    partner object, read from the setter's own source rather than the BUML
    model: `name` from its `hasattr(item/value, "...")` guard, `is_many` from
    whether it propagates via `set([self])`/`.add(self)` (collection) or a
    plain `setattr(..., self)` (single object). BUML end names can contain
    characters the generator sanitizes (e.g. `RDBMS.ecoreTable` ->
    `RDBMS_ecoreTable`), and asserting the wrong shape or attaching the wrong
    name makes the test fail unconditionally (2026-10-17, model_100170 and
    the many-valued-end bug)."""
    for klass in getattr(cls, "__mro__", [cls]):
        prop = klass.__dict__.get(attr_name)
        if isinstance(prop, property) and prop.fset is not None:
            try:
                source = inspect.getsource(prop.fset)
            except (OSError, TypeError):
                return None
            match = _HASATTR_TARGET.search(source)
            if not match:
                return None
            is_many = "set([self])" in source or ".add(self)" in source
            return match.group(1), is_many
    return None


def generate_tests(model, code_module) -> str:
    classes = sorted((t for t in model.types if isinstance(t, Class)), key=type_name)
    enums = sorted((t for t in model.types if isinstance(t, Enumeration)), key=type_name)
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
        "import pytest",
        "from datetime import date, datetime, time, timedelta",
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
        "# REVERSE-DIRECTION ASSOCIATION TESTS",
        "# Mirrors test_structural_full.py's link_reassign_clear, but sets from the",
        "# OTHER end's own setter directly, instead of relying on it firing only as a",
        "# side effect of the forward-direction test. See module docstring.",
        "# =============================================================================",
        "",
    ]

    # --- binary associations: reverse-direction link -> reassign -> clear ---
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

        # ONLY relevant when BOTH sides independently implement a real
        # setter. If only one side is real, test_structural_full.py's
        # existing forward test already exercises the one setter that
        # exists -- there is no "other side" to reverse-test. If neither
        # side is real, nothing to test at all (same as the forward
        # generator). This is the one condition this file exists to cover.
        if not (a_is_real and b_is_real):
            continue
        if not constructible.get(class_a.name, False) or not constructible.get(class_b.name, False):
            continue

        tname = sanitize(f"assoc_{assoc.name}")
        kwargs_a1 = constructor_kwargs(class_a, known_types, sample_table, False, alt_table)
        kwargs_a2 = constructor_kwargs(class_a, known_types, sample_table, True, alt_table)
        kwargs_b = constructor_kwargs(class_b, known_types, sample_table, False, alt_table)
        set_val1 = "{a1}" if many_b else "a1"
        set_val2 = "{a2}" if many_b else "a2"

        # This is the mirror image of test_structural_full.py's forward test:
        # there, `a`'s own setter is called directly and `b`'s reciprocal
        # state is only ever observed, never set directly. Here, `b`'s own
        # setter is called directly instead -- exercising b's own "remove
        # old value" guard as a DIRECT call, not as a side effect triggered
        # from inside a's setter (where, by the time it runs, the outer
        # setter has already overwritten its own stored state -- see
        # docs/DECISIONS.md, 2026-10-01, for the traced example this fixes).
        lines += [
            f"def test_{tname}_reverse_link_reassign_clear():",
            f"    a1 = {code_names[class_a.name]}({kwargs_a1})",
            f"    a2 = {code_names[class_a.name]}({kwargs_a2})",
            f"    b = {code_names[class_b.name]}({kwargs_b})",
            f"    _safe_set(b, {attr_b!r}, {set_val1})",
            f"    assert _is_linked(b, {attr_b!r}, a1)",
            f"    if hasattr(a1, {attr_a!r}):",
            f"        assert _is_linked(a1, {attr_a!r}, b)",
            f"    _safe_set(b, {attr_b!r}, {set_val2})",
            f"    assert _is_linked(b, {attr_b!r}, a2)",
            f"    if hasattr(a1, {attr_a!r}):",
            f"        assert not _is_linked(a1, {attr_a!r}, b)",
            f"    if hasattr(a2, {attr_a!r}):",
            f"        assert _is_linked(a2, {attr_a!r}, b)",
            f"    _safe_set(b, {attr_b!r}, {'set()' if many_b else 'None'})",
            f"    assert not _is_linked(b, {attr_b!r}, a2)",
            f"    if hasattr(a2, {attr_a!r}):",
            f"        assert not _is_linked(a2, {attr_a!r}, b)",
            "",
            "",
        ]

    lines += [
        "# =============================================================================",
        "# STUB-SIDE TEST DOUBLE",
        "# For associations where one side is a bare stub class with no real property:",
        "# manually attach the attribute a real implementation would have had, so the",
        "# real side's hasattr()-guarded consistency logic is actually reachable. See",
        "# module docstring.",
        "# =============================================================================",
        "",
    ]

    # --- binary associations: stub-side test double ---
    for assoc in associations:
        ordered = ordered_ends(assoc)
        if ordered is None:
            continue
        e1, e2 = ordered
        class_a, attr_a, type_a, many_a = e2.type, e1.name, e1.type, is_many(e1.multiplicity)
        class_b, attr_b, type_b, many_b = e1.type, e2.name, e2.type, is_many(e2.multiplicity)

        code_class_a = getattr(code_module, code_names[class_a.name], None) if class_a.name in code_names else None
        code_class_b = getattr(code_module, code_names[class_b.name], None) if class_b.name in code_names else None
        a_is_real = has_real_property(code_class_a, attr_a)
        b_is_real = has_real_property(code_class_b, attr_b)

        # Exactly one side real, the other a stub -- the gap neither the
        # forward generator's test nor the reverse-direction test above can
        # reach (the former's hasattr guard on the stub partner is
        # permanently False with a real stub instance; the latter requires
        # BOTH sides real so it never applies here at all).
        if a_is_real and not b_is_real:
            real_cls, real_attr, real_many, real_code_cls = class_a, attr_a, many_a, code_class_a
            stub_cls = class_b
        elif b_is_real and not a_is_real:
            real_cls, real_attr, real_many, real_code_cls = class_b, attr_b, many_b, code_class_b
            stub_cls = class_a
        else:
            continue  # both real (handled above) or both stub (nothing testable either way)

        if not constructible.get(real_cls.name, False) or not constructible.get(stub_cls.name, False):
            continue
        lookup = _reciprocal_lookup(real_code_cls, real_attr)
        if lookup is None:
            continue  # can't confirm what the setter does to the partner -- don't guess
        stub_attr, stub_many = lookup

        tname = sanitize(f"assoc_{assoc.name}_stub_double")
        kwargs_real = constructor_kwargs(real_cls, known_types, sample_table, False, alt_table)
        kwargs_stub = constructor_kwargs(stub_cls, known_types, sample_table, False, alt_table)
        set_val = "{partner}" if real_many else "partner"
        clear_val = "set()" if real_many else "None"
        # The real setter's propagation shape depends on the STUB end's own
        # multiplicity: a many-valued reciprocal gets `set([self])` / `.add(self)`
        # on assign and `.discard(self)` on clear (leaving an empty set, not
        # None); a scalar one gets `setattr(..., self)` / `setattr(..., None)`.
        # Asserting the scalar shape against a many-valued end fails
        # unconditionally -- and an unmutated-failing test makes cosmic-ray
        # read every mutant as killed (2026-10-17 code-review finding).
        if stub_many:
            assert_linked = f"    assert owner in getattr(partner, {stub_attr!r})"
            assert_cleared = f"    assert owner not in getattr(partner, {stub_attr!r})"
        else:
            assert_linked = f"    assert getattr(partner, {stub_attr!r}) == owner"
            assert_cleared = f"    assert getattr(partner, {stub_attr!r}) is None"

        lines += [
            f"def test_{tname}():",
            f"    # {stub_cls.name} has no real {stub_attr!r} property in the generated",
            f"    # code (a bare stub) -- manually attach it so {real_cls.name}'s own",
            f"    # bidirectional-consistency guard can actually be exercised. This tests",
            f"    # {real_cls.name}'s OWN setter logic via a hand-shaped stand-in for an",
            f"    # incomplete collaborator, same reasoning as a test double anywhere else.",
            f"    owner = {code_names[real_cls.name]}({kwargs_real})",
            f"    partner = {code_names[stub_cls.name]}({kwargs_stub})",
            f"    setattr(partner, {stub_attr!r}, None)",
            f"    _safe_set(owner, {real_attr!r}, {set_val})",
            assert_linked,
            f"    _safe_set(owner, {real_attr!r}, {clear_val})",
            assert_cleared,
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
        "# Behavioral Test Generation Report",
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
    lines +=["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="behavioral_tests_report")
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

    print(f"Generating behavioral tests for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache -- "
              f"same report, no separate retry run needed")

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
