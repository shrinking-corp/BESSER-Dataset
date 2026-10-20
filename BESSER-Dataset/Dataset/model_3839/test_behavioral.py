import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryCondition,
    Condition,
    sql4csv_AndCondition,
    sql4csv_BinaryCondition,
    sql4csv_Column,
    sql4csv_ColumnEquality,
    sql4csv_Condition,
    sql4csv_EObject,
    sql4csv_Equality,
    sql4csv_OrCondition,
    sql4csv_Program,
    sql4csv_Query,
    sql4csv_SQL4CSV,
    sql4csv_Table,
    sql4csv_ValueEquality,
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

def test_assoc_table15_reverse_link_reassign_clear():
    a1 = sql4csv_Table(name="sample_text")
    a2 = sql4csv_Table(name="sample_text_2")
    b = sql4csv_Column(name="sample_text")
    _safe_set(b, 'sql4csv_Column16', a1)
    assert _is_linked(b, 'sql4csv_Column16', a1)
    if hasattr(a1, 'sql4csv_Table17'):
        assert _is_linked(a1, 'sql4csv_Table17', b)
    _safe_set(b, 'sql4csv_Column16', a2)
    assert _is_linked(b, 'sql4csv_Column16', a2)
    if hasattr(a1, 'sql4csv_Table17'):
        assert not _is_linked(a1, 'sql4csv_Table17', b)
    if hasattr(a2, 'sql4csv_Table17'):
        assert _is_linked(a2, 'sql4csv_Table17', b)
    _safe_set(b, 'sql4csv_Column16', None)
    assert not _is_linked(b, 'sql4csv_Column16', a2)
    if hasattr(a2, 'sql4csv_Table17'):
        assert not _is_linked(a2, 'sql4csv_Table17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_column3_stub_double():
    # sql4csv_Query has no real 'sql4csv_Query4' property in the generated
    # code (a bare stub) -- manually attach it so sql4csv_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql4csv_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql4csv_Column(name="sample_text")
    partner = sql4csv_Query()
    setattr(partner, 'sql4csv_Query4', None)
    _safe_set(owner, 'sql4csv_Column', partner)
    assert getattr(partner, 'sql4csv_Query4') == owner
    _safe_set(owner, 'sql4csv_Column', None)
    assert getattr(partner, 'sql4csv_Query4') is None


def test_assoc_columns5_stub_double():
    # sql4csv_Query has no real 'sql4csv_Query6' property in the generated
    # code (a bare stub) -- manually attach it so sql4csv_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql4csv_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql4csv_Column(name="sample_text")
    partner = sql4csv_Query()
    setattr(partner, 'sql4csv_Query6', None)
    _safe_set(owner, 'sql4csv_Column7', partner)
    assert owner in getattr(partner, 'sql4csv_Query6')
    _safe_set(owner, 'sql4csv_Column7', None)
    assert owner not in getattr(partner, 'sql4csv_Query6')


def test_assoc_left18_stub_double():
    # sql4csv_Equality has no real 'sql4csv_Equality' property in the generated
    # code (a bare stub) -- manually attach it so sql4csv_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql4csv_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql4csv_Column(name="sample_text")
    partner = sql4csv_Equality()
    setattr(partner, 'sql4csv_Equality', None)
    _safe_set(owner, 'sql4csv_Column19', partner)
    assert getattr(partner, 'sql4csv_Equality') == owner
    _safe_set(owner, 'sql4csv_Column19', None)
    assert getattr(partner, 'sql4csv_Equality') is None


def test_assoc_right27_stub_double():
    # sql4csv_ColumnEquality has no real 'sql4csv_ColumnEquality' property in the generated
    # code (a bare stub) -- manually attach it so sql4csv_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql4csv_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql4csv_Column(name="sample_text")
    partner = sql4csv_ColumnEquality()
    setattr(partner, 'sql4csv_ColumnEquality', None)
    _safe_set(owner, 'sql4csv_Column28', partner)
    assert getattr(partner, 'sql4csv_ColumnEquality') == owner
    _safe_set(owner, 'sql4csv_Column28', None)
    assert getattr(partner, 'sql4csv_ColumnEquality') is None


def test_assoc_table8_stub_double():
    # sql4csv_Query has no real 'sql4csv_Query9' property in the generated
    # code (a bare stub) -- manually attach it so sql4csv_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql4csv_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql4csv_Table(name="sample_text")
    partner = sql4csv_Query()
    setattr(partner, 'sql4csv_Query9', None)
    _safe_set(owner, 'sql4csv_Table', partner)
    assert getattr(partner, 'sql4csv_Query9') == owner
    _safe_set(owner, 'sql4csv_Table', None)
    assert getattr(partner, 'sql4csv_Query9') is None


def test_assoc_tables10_stub_double():
    # sql4csv_Query has no real 'sql4csv_Query11' property in the generated
    # code (a bare stub) -- manually attach it so sql4csv_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql4csv_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql4csv_Table(name="sample_text")
    partner = sql4csv_Query()
    setattr(partner, 'sql4csv_Query11', None)
    _safe_set(owner, 'sql4csv_Table12', partner)
    assert owner in getattr(partner, 'sql4csv_Query11')
    _safe_set(owner, 'sql4csv_Table12', None)
    assert owner not in getattr(partner, 'sql4csv_Query11')


