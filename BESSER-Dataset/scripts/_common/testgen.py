"""Helpers shared by generate_structural_tests.py and generate_behavioral_tests.py:
loading the generated python_code module, mapping BUML names onto it, and
building constructor calls from sample literals. Requires besser.
"""
from __future__ import annotations

import importlib.util
import inspect
import sys
import uuid
from pathlib import Path

from besser.BUML.metamodel.structural import Enumeration

from .buml import type_name

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


def has_real_property(cls, attr_name: str) -> bool:
    """Whether the generated class implements `attr_name` as a real @property
    (so assignment runs setter logic). Declaring an association in BUML does
    not guarantee the generator implemented it: model_1's petrinet_Arc and
    petrinet_Token are bare `class X: pass` stubs despite being participants.
    """
    if cls is None:
        return False
    for klass in getattr(cls, "__mro__", [cls]):
        if attr_name in klass.__dict__:
            return isinstance(klass.__dict__[attr_name], property)
    return False


def is_many(multiplicity) -> bool:
    if multiplicity is None:
        return True
    max_val = getattr(multiplicity, "max", None)
    return max_val is None or max_val == "*" or (isinstance(max_val, (int, float)) and max_val > 1)


def sanitize(name: str) -> str:
    """Make `name` safe inside a generated test function name."""
    return "".join(c if c.isalnum() or c == "_" else "_" for c in name)


def python_identifier(name: str) -> str:
    """How the dataset's code generator turns a BUML name into a Python
    identifier: invalid characters are dropped (model_2533's
    `raas_small_test_#29373817` becomes `class raas_small_test_29373817:`)."""
    cleaned = "".join(c for c in name if c.isalnum() or c == "_")
    if not cleaned or cleaned[0].isdigit():
        cleaned = f"_{cleaned}"
    return cleaned


def resolve_code_name(code_module, raw_name: str) -> str | None:
    """The name `raw_name` actually has in the generated module (raw or
    sanitized), or None if neither exists there."""
    if hasattr(code_module, raw_name):
        return raw_name
    sanitized = python_identifier(raw_name)
    if sanitized != raw_name and hasattr(code_module, sanitized):
        return sanitized
    return None


def build_literal_tables(model, code_module) -> tuple[dict, dict, set]:
    """Extend the primitive sample tables with this model's enum literals
    (e.g. "UserRole" -> "UserRole.SALES_MANAGER"). Enum-typed constructor
    arguments are required, so without these every test of such a class fails
    (Model_1000000001: 64/108 tests, "missing 1 required positional argument").
    Keys are raw BUML names; values use the enum's name in python_code.py.
    Returns (sample_table, alt_table, known_type_names).
    """
    sample = dict(SAMPLE_LITERAL)
    alt = dict(SAMPLE_LITERAL_ALT)
    for enum in (t for t in model.types if isinstance(t, Enumeration)):
        literals = sorted(enum.literals, key=lambda l: l.name)
        if not literals:
            continue
        code_enum_name = resolve_code_name(code_module, enum.name)
        if code_enum_name is None:
            continue
        sample[enum.name] = f"{code_enum_name}.{literals[0].name}"
        alt[enum.name] = f"{code_enum_name}.{literals[1].name}" if len(literals) > 1 else f"{code_enum_name}.{literals[0].name}"
    return sample, alt, set(sample.keys())


def required_param_names(code_class) -> set | None:
    """__init__ parameters without a default (excluding self), or None for a
    missing class or one with no introspectable __init__."""
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
    """Whether every required __init__ argument of the REAL generated class
    can be filled from the sample tables. The BUML model and the code can
    diverge: model_10000002's `Order` requires an `OrderStatus` that is an
    empty enum in the code, so no valid value exists."""
    required = required_param_names(code_class)
    if required is None:
        return True
    coverable = {a.name for a in class_type.attributes if type_name(getattr(a, "type", "")) in known_types}
    return required.issubset(coverable)


def plain_attributes(class_type, known_types: set) -> list:
    """The class's own attributes whose type has a sample literal."""
    return [a for a in class_type.attributes if type_name(getattr(a, "type", "")) in known_types]


def constructor_kwargs(class_type, known_types: set, sample_table: dict, alt: bool, alt_table: dict) -> str:
    table = alt_table if alt else sample_table
    parts = []
    for attr in sorted(plain_attributes(class_type, known_types), key=lambda a: a.name):
        literal = table.get(type_name(attr.type), '"sample"')
        parts.append(f"{attr.name}={literal}")
    return ", ".join(parts)
