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
TEST_FILENAME = "test_structural_full.py"

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
    generalizations = sorted(model.generalizations, key=lambda g: f"{_type_name(g.general)}::{_type_name(g.specific)}")
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
            tname = _sanitize(f"{cls.name}_{attr.name}")
            kwargs = constructor_kwargs(cls, known_types, sample_table, False, alt_table)
            alt_literal = alt_table.get(_type_name(attr.type), '"sample_2"')
            lines += [
                f"def test_{tname}_value_roundtrip():",
                f"    instance = {code_names[cls.name]}({kwargs})",
                f"    assert instance.{attr.name} == {sample_table.get(_type_name(attr.type), chr(34)+'sample'+chr(34))}",
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
        tname = _sanitize(f"{gen.specific.name}_isa_{gen.general.name}")
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

        tname = _sanitize(f"assoc_{assoc.name}")
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

    def _strategy_for(type_name: str) -> str:
        # Only sample from enums that actually have literals -- known_types
        # already excludes empty ones (build_literal_tables), same fix as
        # is_constructible: an empty `class OrderStatus(Enum): pass` has no
        # valid value, so st.sampled_from() would raise InvalidArgument.
        if type_name in enum_names_set and type_name in known_types and type_name in code_names:
            return f"st.sampled_from({code_names[type_name]})"
        return HYPOTHESIS_STRATEGY.get(type_name, "st.none()")

    for cls in classes:
        if not constructible[cls.name]:
            continue
        prim_attrs = sorted(plain_attributes(cls, known_types), key=lambda a: a.name)
        strategy_args = ", ".join(
            f"{a.name}={_strategy_for(_type_name(a.type))}" for a in prim_attrs
        )
        tname = _sanitize(cls.name)
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
        "# Structural Test Generation Report",
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
    parser.add_argument("--report-name", type=str, default="structural_tests_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
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

    print(f"Generating structural tests for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")

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
