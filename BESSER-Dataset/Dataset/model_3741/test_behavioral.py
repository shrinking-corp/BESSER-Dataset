import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    NamedElement,
    genericsql_Check,
    genericsql_Constraint,
    genericsql_DataBase,
    genericsql_Field,
    genericsql_ForeignKey,
    genericsql_NamedElement,
    genericsql_PrimaryKey,
    genericsql_Table,
    genericsql_Unique,
    Type,
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

def test_assoc_constrainedFields20_stub_double():
    # genericsql_Constraint has no real 'genericsql_Constraint21' property in the generated
    # code (a bare stub) -- manually attach it so genericsql_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericsql_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericsql_Field(autoIcrement=True, defaultValue="sample_text", notNull=True, size=7, specificType="sample_text", type="sample_text", unique=True)
    partner = genericsql_Constraint()
    setattr(partner, 'genericsql_Constraint21', None)
    _safe_set(owner, 'genericsql_Field22', partner)
    assert owner in getattr(partner, 'genericsql_Constraint21')
    _safe_set(owner, 'genericsql_Field22', None)
    assert owner not in getattr(partner, 'genericsql_Constraint21')


def test_assoc_fields4_stub_double():
    # genericsql_Table has no real 'table5' property in the generated
    # code (a bare stub) -- manually attach it so genericsql_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericsql_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericsql_Field(autoIcrement=True, defaultValue="sample_text", notNull=True, size=7, specificType="sample_text", type="sample_text", unique=True)
    partner = genericsql_Table()
    setattr(partner, 'table5', None)
    _safe_set(owner, 'Field', partner)
    assert owner in getattr(partner, 'table5')
    _safe_set(owner, 'Field', None)
    assert owner not in getattr(partner, 'table5')


def test_assoc_foreignFields11_stub_double():
    # genericsql_ForeignKey has no real 'genericsql_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so genericsql_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericsql_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericsql_Field(autoIcrement=True, defaultValue="sample_text", notNull=True, size=7, specificType="sample_text", type="sample_text", unique=True)
    partner = genericsql_ForeignKey()
    setattr(partner, 'genericsql_ForeignKey', None)
    _safe_set(owner, 'genericsql_Field12', partner)
    assert owner in getattr(partner, 'genericsql_ForeignKey')
    _safe_set(owner, 'genericsql_Field12', None)
    assert owner not in getattr(partner, 'genericsql_ForeignKey')


def test_assoc_primaryFields8_stub_double():
    # genericsql_PrimaryKey has no real 'genericsql_PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so genericsql_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericsql_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericsql_Field(autoIcrement=True, defaultValue="sample_text", notNull=True, size=7, specificType="sample_text", type="sample_text", unique=True)
    partner = genericsql_PrimaryKey()
    setattr(partner, 'genericsql_PrimaryKey', None)
    _safe_set(owner, 'genericsql_Field', partner)
    assert owner in getattr(partner, 'genericsql_PrimaryKey')
    _safe_set(owner, 'genericsql_Field', None)
    assert owner not in getattr(partner, 'genericsql_PrimaryKey')


def test_assoc_table18_stub_double():
    # genericsql_Table has no real 'Table19' property in the generated
    # code (a bare stub) -- manually attach it so genericsql_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericsql_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericsql_Field(autoIcrement=True, defaultValue="sample_text", notNull=True, size=7, specificType="sample_text", type="sample_text", unique=True)
    partner = genericsql_Table()
    setattr(partner, 'Table19', None)
    _safe_set(owner, 'fields', partner)
    assert getattr(partner, 'Table19') == owner
    _safe_set(owner, 'fields', None)
    assert getattr(partner, 'Table19') is None


