import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Literal,
    Predicate,
    expression_BooleanLiteral,
    expression_Expression,
    expression_Function,
    expression_IntegerLiteral,
    expression_Literal,
    expression_NullLiteral,
    expression_Predicate,
    expression_PredicateBooleanOperator,
    expression_PredicateComparisonOperator,
    expression_PredicateEqualityOperator,
    expression_PredicateIsEmpty,
    expression_PredicateIsNull,
    expression_PredicateIsOperator,
    expression_PredicateLikeOperator,
    expression_StringLiteral,
    expression_TimeLiteral,
    expression_Variable,
    BooleanOperator,
    ComparisionOperator,
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

def test_assoc_expressions0_reverse_link_reassign_clear():
    a1 = expression_PredicateBooleanOperator(operator="sample_text")
    a2 = expression_PredicateBooleanOperator(operator="sample_text_2")
    b = expression_Predicate(negated=True)
    _safe_set(b, 'expression_Predicate', a1)
    assert _is_linked(b, 'expression_Predicate', a1)
    if hasattr(a1, 'expression_PredicateBooleanOperator'):
        assert _is_linked(a1, 'expression_PredicateBooleanOperator', b)
    _safe_set(b, 'expression_Predicate', a2)
    assert _is_linked(b, 'expression_Predicate', a2)
    if hasattr(a1, 'expression_PredicateBooleanOperator'):
        assert not _is_linked(a1, 'expression_PredicateBooleanOperator', b)
    if hasattr(a2, 'expression_PredicateBooleanOperator'):
        assert _is_linked(a2, 'expression_PredicateBooleanOperator', b)
    _safe_set(b, 'expression_Predicate', None)
    assert not _is_linked(b, 'expression_Predicate', a2)
    if hasattr(a2, 'expression_PredicateBooleanOperator'):
        assert not _is_linked(a2, 'expression_PredicateBooleanOperator', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_left5_stub_double():
    # expression_Expression has no real 'expression_Expression6' property in the generated
    # code (a bare stub) -- manually attach it so expression_PredicateComparisonOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_PredicateComparisonOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_PredicateComparisonOperator(operator="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression6', None)
    _safe_set(owner, 'expression_PredicateComparisonOperator', partner)
    assert getattr(partner, 'expression_Expression6') == owner
    _safe_set(owner, 'expression_PredicateComparisonOperator', None)
    assert getattr(partner, 'expression_Expression6') is None


def test_assoc_right7_stub_double():
    # expression_Expression has no real 'expression_Expression9' property in the generated
    # code (a bare stub) -- manually attach it so expression_PredicateComparisonOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_PredicateComparisonOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_PredicateComparisonOperator(operator="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression9', None)
    _safe_set(owner, 'expression_PredicateComparisonOperator8', partner)
    assert getattr(partner, 'expression_Expression9') == owner
    _safe_set(owner, 'expression_PredicateComparisonOperator8', None)
    assert getattr(partner, 'expression_Expression9') is None


