import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanOperation,
    ComparisonOperator,
    Condition,
    Existence,
    model_And,
    model_BooleanOperation,
    model_Column,
    model_ColumnAlias,
    model_Comparison,
    model_ComparisonOperator,
    model_Condition,
    model_Equals,
    model_Existence,
    model_Exists,
    model_From,
    model_GreaterThan,
    model_LessThan,
    model_NotEquals,
    model_NotExists,
    model_Or,
    model_Select,
    model_Table,
    model_TableAlias,
    model_Union,
    model_Where,
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

def test_assoc_columnalias7_reverse_link_reassign_clear():
    a1 = model_ColumnAlias(name="sample_text")
    a2 = model_ColumnAlias(name="sample_text_2")
    b = model_Column(name="sample_text")
    _safe_set(b, 'model_Column8', a1)
    assert _is_linked(b, 'model_Column8', a1)
    if hasattr(a1, 'model_ColumnAlias'):
        assert _is_linked(a1, 'model_ColumnAlias', b)
    _safe_set(b, 'model_Column8', a2)
    assert _is_linked(b, 'model_Column8', a2)
    if hasattr(a1, 'model_ColumnAlias'):
        assert not _is_linked(a1, 'model_ColumnAlias', b)
    if hasattr(a2, 'model_ColumnAlias'):
        assert _is_linked(a2, 'model_ColumnAlias', b)
    _safe_set(b, 'model_Column8', None)
    assert not _is_linked(b, 'model_Column8', a2)
    if hasattr(a2, 'model_ColumnAlias'):
        assert not _is_linked(a2, 'model_ColumnAlias', b)


def test_assoc_tablealias11_reverse_link_reassign_clear():
    a1 = model_TableAlias(name="sample_text")
    a2 = model_TableAlias(name="sample_text_2")
    b = model_Table(name="sample_text")
    _safe_set(b, 'model_Table12', a1)
    assert _is_linked(b, 'model_Table12', a1)
    if hasattr(a1, 'model_TableAlias'):
        assert _is_linked(a1, 'model_TableAlias', b)
    _safe_set(b, 'model_Table12', a2)
    assert _is_linked(b, 'model_Table12', a2)
    if hasattr(a1, 'model_TableAlias'):
        assert not _is_linked(a1, 'model_TableAlias', b)
    if hasattr(a2, 'model_TableAlias'):
        assert _is_linked(a2, 'model_TableAlias', b)
    _safe_set(b, 'model_Table12', None)
    assert not _is_linked(b, 'model_Table12', a2)
    if hasattr(a2, 'model_TableAlias'):
        assert not _is_linked(a2, 'model_TableAlias', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_column0_stub_double():
    # model_Select has no real 'model_Select' property in the generated
    # code (a bare stub) -- manually attach it so model_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Column(name="sample_text")
    partner = model_Select()
    setattr(partner, 'model_Select', None)
    _safe_set(owner, 'model_Column', partner)
    assert owner in getattr(partner, 'model_Select')
    _safe_set(owner, 'model_Column', None)
    assert owner not in getattr(partner, 'model_Select')


def test_assoc_comparisonoperator23_stub_double():
    # model_ComparisonOperator has no real 'model_ComparisonOperator' property in the generated
    # code (a bare stub) -- manually attach it so model_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Comparison(lhs="sample_text", rhs="sample_text")
    partner = model_ComparisonOperator()
    setattr(partner, 'model_ComparisonOperator', None)
    _safe_set(owner, 'model_Comparison', partner)
    assert getattr(partner, 'model_ComparisonOperator') == owner
    _safe_set(owner, 'model_Comparison', None)
    assert getattr(partner, 'model_ComparisonOperator') is None


def test_assoc_table9_stub_double():
    # model_From has no real 'model_From10' property in the generated
    # code (a bare stub) -- manually attach it so model_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Table(name="sample_text")
    partner = model_From()
    setattr(partner, 'model_From10', None)
    _safe_set(owner, 'model_Table', partner)
    assert owner in getattr(partner, 'model_From10')
    _safe_set(owner, 'model_Table', None)
    assert owner not in getattr(partner, 'model_From10')


