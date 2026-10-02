#!/usr/bin/env python3
"""Generate `test_behavioral.py` per model: a small, targeted supplement to
`test_structural_full.py` that tests each bidirectional association from
**both ends independently**, not just one side relying on the other's side
effect. A COPY of `generate_structural_tests.py` (that file is never
modified -- `test_structural_full.py` stays exactly as it is, still correct
for what it checks); this script only emits the one new kind of test this
diagnosis found missing, not a re-emission of attributes/generalizations/
forward-direction association tests, which `test_structural_full.py`
already covers.

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

**Not every surviving mutant is fixable this way.** The same diagnosis found
a separate, genuinely unkillable class of surviving mutants: where the
association's other participant class is a bare `class X: pass` stub with
no real properties at all, the generated code's own `hasattr(item, "...")`
guard is permanently False, making the mutant inside it dead code for any
possible test. This script does nothing for that case (nothing could) --
see the DECISIONS.md entry for the full trace, and account for this floor
when judging any approach's resulting mutation score.

What this generates: for each binary association where BOTH ends have a
real, independently-settable property (checked via `_has_real_property()`,
already present in the copied generator), one additional test that:
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

Usage:
    python scripts/generate_behavioral_tests.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import concurrent.futures
import inspect
import datetime
import importlib.util
import json
import platform
import sys
import uuid
from pathlib import Path

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural import (
    AssociationClass, BinaryAssociation, Class, DomainModel, Enumeration,
)

OLD_GLOB = "*_BUML_model.py"
NEW_GLOB = "*_buml.py"
TEST_FILENAME = "test_behavioral.py"
# Cached results with one of these statuses are automatically re-attempted
# on the next run under the SAME --report-name -- same fix as
# validate_mutation.py/validate_mutation_properties.py (2026-10-01).
# "missing_file" is excluded: permanent (no BUML source/python_code.py to
# load), not a transient failure a re-run would fix.
RETRIABLE_STATUSES = {"error"}

SAMPLE_LITERAL = {
    "str": '"sample_text"',
    "int": "7",
    "float": "3.14",
    "bool": "True",
    "date": "date(2024, 1, 1)",
    "datetime": "datetime(2024, 1, 1, 12, 0, 0)",
    "time": "time(12, 0, 0)",
    "timedelta": "timedelta(days=1)",
    "any": '"sample_any_value"',
}
SAMPLE_LITERAL_ALT = {
    "str": '"sample_text_2"',
    "int": "13",
    "float": "9.99",
    "bool": "False",
    "date": "date(2025, 6, 15)",
    "datetime": "datetime(2025, 6, 15, 8, 30, 0)",
    "time": "time(8, 30, 0)",
    "timedelta": "timedelta(days=2)",
    "any": '"sample_any_value_2"',
}

def load_cache(cache_path: Path) -> dict[str, dict]:
    """Read a JSONL cache of previously-completed results, keyed by model name.

    Tolerates a truncated last line (e.g. the process was killed mid-write)
    by skipping any line that fails to parse.
    """
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


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in models_file.read_text().splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


def find_buml_file(model_dir: Path) -> Path | None:
    matches = list(model_dir.glob(OLD_GLOB)) or list(model_dir.glob(NEW_GLOB))
    return matches[0] if matches else None


def load_domain_model(file_path: Path):
    module_name = f"buml_model_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    if spec is None or spec.loader is None:
        raise ValueError(f"Could not load Python module from path: {file_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(module_name, None)

    for value in vars(module).values():
        if isinstance(value, DomainModel):
            return value
    for value in vars(module).values():
        if isinstance(value, Project) and value.models:
            return value.models[0]

    raise ValueError(f"No DomainModel found in {file_path}")


def _type_name(value) -> str:
    return value.name if hasattr(value, "name") else str(value)


def load_python_module(source_path: Path):
    module_name = f"python_code_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(module_name, str(source_path))
    if spec is None or spec.loader is None:
        raise ValueError(f"Could not load Python module from path: {source_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(module_name, None)
    return module


def _has_real_property(cls, attr_name: str) -> bool:
    """Whether `cls` (a class from the actually-generated python_code module,
    not the BUML model) implements `attr_name` as a real @property -- i.e.
    whether assigning to it actually runs setter logic, as opposed to a bare
    `class X: pass` silently accepting a plain dynamic attribute assignment
    that triggers nothing. Declaring an association in BUML does not
    guarantee the generator implemented it on either participant's class
    (confirmed: model_1's petrinet_Arc/petrinet_Token are bare stubs despite
    being association participants) -- this has to be checked against the
    real generated code, not inferred from the model.
    """
    if cls is None:
        return False
    for klass in getattr(cls, "__mro__", [cls]):
        if attr_name in klass.__dict__:
            return isinstance(klass.__dict__[attr_name], property)
    return False


def _ordered_ends(association):
    """Deterministic (end1, end2) pair -- association.ends is an unordered set,
    so picking list(ends)[0]/[1] directly varies between process runs
    (Python's hash randomization). Same fix as buml_to_puml.py's
    _ordered_ends -- needed here too, and originally missed."""
    ends = list(getattr(association, "ends", []))
    if len(ends) != 2:
        return None

    def end_key(end):
        multiplicity = getattr(end, "multiplicity", None)
        return (
            _type_name(getattr(end, "type", "")),
            str(getattr(end, "name", "")),
            str(getattr(multiplicity, "min", "")),
            str(getattr(multiplicity, "max", "")),
            bool(getattr(end, "is_navigable", False)),
            bool(getattr(end, "is_composite", False)),
            bool(getattr(end, "is_aggregation", False)),
        )

    ordered = sorted(ends, key=end_key)
    return ordered[0], ordered[1]


def _is_many(multiplicity) -> bool:
    if multiplicity is None:
        return True
    max_val = getattr(multiplicity, "max", None)
    return max_val is None or max_val == "*" or (isinstance(max_val, (int, float)) and max_val > 1)


def _sanitize(name: str) -> str:
    return "".join(c if c.isalnum() or c == "_" else "_" for c in name)


def _python_identifier(name: str) -> str:
    """Best-effort sanitization matching how this dataset's python_code.py
    generator turns a BUML `.name` into an actual Python identifier: strip
    any character that isn't valid in one. Confirmed real case:
    model_2533's `Class(name="raas_small_test_#29373817")` -- "#" is legal
    in a UML/BUML name but not in a Python identifier (and would start a
    comment if emitted raw, silently truncating the rest of the line) -- the
    generated code simply drops it: `class raas_small_test_29373817:`.
    """
    cleaned = "".join(c for c in name if c.isalnum() or c == "_")
    if not cleaned or cleaned[0].isdigit():
        cleaned = f"_{cleaned}"
    return cleaned


def resolve_code_name(code_module, raw_name: str) -> str | None:
    """The actual attribute name `raw_name` resolves to in the generated
    python_code module -- not always the same string as the BUML `.name`
    (see _python_identifier). Returns None if neither the raw nor the
    sanitized form exists there, meaning this class/enum can't be safely
    referenced in generated code at all (BUML model and generated code have
    diverged too far to bridge automatically).
    """
    if hasattr(code_module, raw_name):
        return raw_name
    sanitized = _python_identifier(raw_name)
    if sanitized != raw_name and hasattr(code_module, sanitized):
        return sanitized
    return None


def build_literal_tables(model, code_module) -> tuple[dict, dict, set]:
    """Extend the static primitive sample-value tables with this model's own
    enum literals (e.g. "UserRole" -> "UserRole.SALES_MANAGER"). Enumeration-
    typed attributes are NOT optional in the generated __init__ just because
    we don't have a static literal for them -- omitting them from
    constructor_kwargs() left them as a *missing required argument*, breaking
    construction (and therefore every test) for any class with one.
    Confirmed on Model_1000000001: 64/108 tests failed with
    "missing 1 required positional argument: 'role'" until this was added.
    Returns (sample_table, alt_table, known_type_names).
    """
    sample = dict(SAMPLE_LITERAL)
    alt = dict(SAMPLE_LITERAL_ALT)
    for enum in (t for t in model.types if isinstance(t, Enumeration)):
        literals = sorted(enum.literals, key=lambda l: l.name)
        if not literals:
            continue
        # Dict KEY stays the raw BUML name (that's what _type_name(attr.type)
        # returns for lookups elsewhere); the VALUE must use the name the
        # enum actually has in python_code.py, or the emitted literal
        # (e.g. "UserRole.SALES_MANAGER") would reference a name that
        # doesn't exist there -- see resolve_code_name().
        code_enum_name = resolve_code_name(code_module, enum.name)
        if code_enum_name is None:
            continue
        sample[enum.name] = f"{code_enum_name}.{literals[0].name}"
        alt[enum.name] = f"{code_enum_name}.{literals[1].name}" if len(literals) > 1 else f"{code_enum_name}.{literals[0].name}"
    return sample, alt, set(sample.keys())


def _required_param_names(code_class) -> set | None:
    """Names of code_class.__init__'s parameters with no default (excluding
    self). None if code_class is missing or has no introspectable __init__
    (a bare `class X: pass` stub -- always constructible with zero args)."""
    if code_class is None:
        return None
    try:
        sig = inspect.signature(code_class.__init__)
    except (TypeError, ValueError):
        return None
    return {
        name for name, param in sig.parameters.items()
        if name != "self" and param.default is inspect.Parameter.empty
        and param.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY)
    }


def is_constructible(class_type, code_class, known_types: set) -> bool:
    """Whether we can actually build a valid constructor call for this class.

    Checks the REAL __init__ signature, not just the BUML model's attribute
    list -- they can diverge. Confirmed real case: model_10000002's `Order`
    requires `status: OrderStatus`, but `OrderStatus` is a genuinely empty
    enum (`class OrderStatus(Enum): pass`, zero literals) in the generated
    code -- there is no valid Python value for it at all, so `Order` is
    unconstructable by anyone, not just by this generator. Silently omitting
    unfillable required arguments (the previous behavior) breaks
    construction instead of catching this.
    """
    required = _required_param_names(code_class)
    if required is None:
        return True
    coverable = {a.name for a in class_type.attributes if _type_name(getattr(a, "type", "")) in known_types}
    return required.issubset(coverable)


def plain_attributes(class_type, known_types: set) -> list:
    """This class's own attributes whose type has a known sample literal
    (primitives, plus this model's own enums)."""
    return [a for a in class_type.attributes if _type_name(getattr(a, "type", "")) in known_types]


def constructor_kwargs(class_type, known_types: set, sample_table: dict, alt: bool, alt_table: dict) -> str:
    table = alt_table if alt else sample_table
    parts = []
    for attr in sorted(plain_attributes(class_type, known_types), key=lambda a: a.name):
        literal = table.get(_type_name(attr.type), '"sample"')
        parts.append(f"{attr.name}={literal}")
    return ", ".join(parts)


def generate_tests(model, code_module) -> str:
    classes = sorted((t for t in model.types if isinstance(t, Class)), key=_type_name)
    enums = sorted((t for t in model.types if isinstance(t, Enumeration)), key=_type_name)
    associations = sorted(
        (a for a in model.associations if isinstance(a, BinaryAssociation)), key=_type_name
    )

    sample_table, alt_table, known_types = build_literal_tables(model, code_module)

    # A class/enum's BUML `.name` isn't always the identifier it has in the
    # generated python_code.py (see resolve_code_name/_python_identifier --
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
        ordered = _ordered_ends(assoc)
        if ordered is None:
            continue
        e1, e2 = ordered
        # attribute named e1.name (type e1.type) lives on class e2.type, and vice versa
        class_a, attr_a, type_a, many_a = e2.type, e1.name, e1.type, _is_many(e1.multiplicity)
        class_b, attr_b, type_b, many_b = e1.type, e2.name, e2.type, _is_many(e2.multiplicity)

        code_class_a = getattr(code_module, code_names[class_a.name], None) if class_a.name in code_names else None
        code_class_b = getattr(code_module, code_names[class_b.name], None) if class_b.name in code_names else None
        a_is_real = _has_real_property(code_class_a, attr_a)
        b_is_real = _has_real_property(code_class_b, attr_b)

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

        tname = _sanitize(f"assoc_{assoc.name}")
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
        output_path.write_text(test_text)
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
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += ["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--dataset-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "Dataset",
    )
    parser.add_argument(
        "--reports-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "reports",
    )
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
    retriable = {m: r for m, r in cached_results_all.items() if r["status"] in RETRIABLE_STATUSES}
    cached_results = {m: r for m, r in cached_results_all.items() if m not in retriable}

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

    results: list[dict] = list(cached_results.values())
    done = skipped
    cache_file = cache_path.open("a")
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(generate_model, model_dir): model_dir for model_dir in model_dirs}
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "model": model_dir.name, "status": "error", "error_message": str(exc),
                        "buml_source": None, "tests_written": None,
                    }
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                print(f"  {done}/{total}: {model_dir.name} -> {result['status']}", flush=True)
    finally:
        cache_file.close()

    report = build_report(results)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Generated: {report['generated_count']}/{report['total_models']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
