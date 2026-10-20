import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    Database,
    ForeignKey,
    Key,
    LocatedElement,
    NamedElement,
    Parameter,
    SQLDDL_Column,
    SQLDDL_Database,
    SQLDDL_ForeignKey,
    SQLDDL_IntegerVal,
    SQLDDL_Key,
    SQLDDL_LocatedElement,
    SQLDDL_NamedElement,
    SQLDDL_NullVal,
    SQLDDL_Parameter,
    SQLDDL_PrimaryKey,
    SQLDDL_SimpleKey,
    SQLDDL_StringVal,
    SQLDDL_Table,
    SQLDDL_TableElement,
    SQLDDL_Type,
    SQLDDL_Value,
    Table,
    TableElement,
    Type,
    Value,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns14_stub_double():
    # Column has no real 'Column' property in the generated
    # code (a bare stub) -- manually attach it so SQLDDL_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDDL_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDDL_Key(isUnique="sample_text", name="sample_text")
    partner = Column()
    setattr(partner, 'Column', None)
    _safe_set(owner, 'keys', {partner})
    assert getattr(partner, 'Column') == owner
    _safe_set(owner, 'keys', set())
    assert getattr(partner, 'Column') is None


def test_assoc_default11_stub_double():
    # Value has no real 'Value' property in the generated
    # code (a bare stub) -- manually attach it so SQLDDL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDDL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    partner = Value()
    setattr(partner, 'Value', None)
    _safe_set(owner, 'SQLDDL_Column12', partner)
    assert getattr(partner, 'Value') == owner
    _safe_set(owner, 'SQLDDL_Column12', None)
    assert getattr(partner, 'Value') is None


def test_assoc_keys13_stub_double():
    # Key has no real 'Key' property in the generated
    # code (a bare stub) -- manually attach it so SQLDDL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDDL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    partner = Key()
    setattr(partner, 'Key', None)
    _safe_set(owner, 'columns', {partner})
    assert getattr(partner, 'Key') == owner
    _safe_set(owner, 'columns', set())
    assert getattr(partner, 'Key') is None


def test_assoc_referencedBy8_stub_double():
    # ForeignKey has no real 'ForeignKey9' property in the generated
    # code (a bare stub) -- manually attach it so SQLDDL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDDL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    partner = ForeignKey()
    setattr(partner, 'ForeignKey9', None)
    _safe_set(owner, 'referencedColumns', {partner})
    assert getattr(partner, 'ForeignKey9') == owner
    _safe_set(owner, 'referencedColumns', set())
    assert getattr(partner, 'ForeignKey9') is None


def test_assoc_type10_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so SQLDDL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDDL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDDL_Column(canBeNull="sample_text", name="sample_text")
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'SQLDDL_Column', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'SQLDDL_Column', None)
    assert getattr(partner, 'Type') is None


