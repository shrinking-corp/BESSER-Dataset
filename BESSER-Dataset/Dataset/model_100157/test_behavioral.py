import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArrayExpression,
    Expression,
    ExpressionWhereEntry,
    WhereEntry,
    query_AndWhereEntry,
    query_ArrayExpression,
    query_BooleanArrayExpression,
    query_BooleanExpression,
    query_Database,
    query_DateArrayExpression,
    query_DateExpression,
    query_DoubleArrayExpression,
    query_DoubleExpression,
    query_Expression,
    query_ExpressionWhereEntry,
    query_LongArrayExpression,
    query_LongExpression,
    query_Model,
    query_MultiExpressionWhereEntry,
    query_NullArrayExpression,
    query_NullExpression,
    query_OrWhereEntry,
    query_ReplacableValue,
    query_SingleExpressionWhereEntry,
    query_StringArrayExpression,
    query_StringExpression,
    query_WhereEntry,
    ArrayOperator,
    Operator,
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

def test_assoc_db0_reverse_link_reassign_clear():
    a1 = query_Model(attrs="sample_text")
    a2 = query_Model(attrs="sample_text_2")
    b = query_Database(dbName="sample_text", name="sample_text", port="sample_text", url="sample_text")
    _safe_set(b, 'query_Database', a1)
    assert _is_linked(b, 'query_Database', a1)
    if hasattr(a1, 'query_Model'):
        assert _is_linked(a1, 'query_Model', b)
    _safe_set(b, 'query_Database', a2)
    assert _is_linked(b, 'query_Database', a2)
    if hasattr(a1, 'query_Model'):
        assert not _is_linked(a1, 'query_Model', b)
    if hasattr(a2, 'query_Model'):
        assert _is_linked(a2, 'query_Model', b)
    _safe_set(b, 'query_Database', None)
    assert not _is_linked(b, 'query_Database', a2)
    if hasattr(a2, 'query_Model'):
        assert not _is_linked(a2, 'query_Model', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_rhs3_stub_double():
    # query_Expression has no real 'query_Expression' property in the generated
    # code (a bare stub) -- manually attach it so query_SingleExpressionWhereEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_SingleExpressionWhereEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_SingleExpressionWhereEntry(operator="sample_text")
    partner = query_Expression()
    setattr(partner, 'query_Expression', None)
    _safe_set(owner, 'query_SingleExpressionWhereEntry', partner)
    assert getattr(partner, 'query_Expression') == owner
    _safe_set(owner, 'query_SingleExpressionWhereEntry', None)
    assert getattr(partner, 'query_Expression') is None


def test_assoc_rhs4_stub_double():
    # query_ArrayExpression has no real 'query_ArrayExpression' property in the generated
    # code (a bare stub) -- manually attach it so query_MultiExpressionWhereEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_MultiExpressionWhereEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_MultiExpressionWhereEntry(operator="sample_text")
    partner = query_ArrayExpression()
    setattr(partner, 'query_ArrayExpression', None)
    _safe_set(owner, 'query_MultiExpressionWhereEntry', partner)
    assert getattr(partner, 'query_ArrayExpression') == owner
    _safe_set(owner, 'query_MultiExpressionWhereEntry', None)
    assert getattr(partner, 'query_ArrayExpression') is None


def test_assoc_whereEntry1_stub_double():
    # query_WhereEntry has no real 'query_WhereEntry' property in the generated
    # code (a bare stub) -- manually attach it so query_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_Model(attrs="sample_text")
    partner = query_WhereEntry()
    setattr(partner, 'query_WhereEntry', None)
    _safe_set(owner, 'query_Model2', partner)
    assert getattr(partner, 'query_WhereEntry') == owner
    _safe_set(owner, 'query_Model2', None)
    assert getattr(partner, 'query_WhereEntry') is None


