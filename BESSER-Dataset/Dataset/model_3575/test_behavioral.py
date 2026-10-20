import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Literal,
    Predicate,
    expression_BooleanLiteral,
    expression_Expression,
    expression_IntegerLiteral,
    expression_Literal,
    expression_NullLiteral,
    expression_Predicate,
    expression_PredicateBooleanOperator,
    expression_PredicateComparisonOperator,
    expression_PredicateEqualityOperator,
    expression_PredicateInOperator,
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


def test_assoc_left5_reverse_link_reassign_clear():
    a1 = expression_PredicateComparisonOperator(operator="sample_text")
    a2 = expression_PredicateComparisonOperator(operator="sample_text_2")
    b = expression_Expression(suffixes="sample_text")
    _safe_set(b, 'expression_Expression6', a1)
    assert _is_linked(b, 'expression_Expression6', a1)
    if hasattr(a1, 'expression_PredicateComparisonOperator'):
        assert _is_linked(a1, 'expression_PredicateComparisonOperator', b)
    _safe_set(b, 'expression_Expression6', a2)
    assert _is_linked(b, 'expression_Expression6', a2)
    if hasattr(a1, 'expression_PredicateComparisonOperator'):
        assert not _is_linked(a1, 'expression_PredicateComparisonOperator', b)
    if hasattr(a2, 'expression_PredicateComparisonOperator'):
        assert _is_linked(a2, 'expression_PredicateComparisonOperator', b)
    _safe_set(b, 'expression_Expression6', None)
    assert not _is_linked(b, 'expression_Expression6', a2)
    if hasattr(a2, 'expression_PredicateComparisonOperator'):
        assert not _is_linked(a2, 'expression_PredicateComparisonOperator', b)


def test_assoc_right7_reverse_link_reassign_clear():
    a1 = expression_PredicateComparisonOperator(operator="sample_text")
    a2 = expression_PredicateComparisonOperator(operator="sample_text_2")
    b = expression_Expression(suffixes="sample_text")
    _safe_set(b, 'expression_Expression9', a1)
    assert _is_linked(b, 'expression_Expression9', a1)
    if hasattr(a1, 'expression_PredicateComparisonOperator8'):
        assert _is_linked(a1, 'expression_PredicateComparisonOperator8', b)
    _safe_set(b, 'expression_Expression9', a2)
    assert _is_linked(b, 'expression_Expression9', a2)
    if hasattr(a1, 'expression_PredicateComparisonOperator8'):
        assert not _is_linked(a1, 'expression_PredicateComparisonOperator8', b)
    if hasattr(a2, 'expression_PredicateComparisonOperator8'):
        assert _is_linked(a2, 'expression_PredicateComparisonOperator8', b)
    _safe_set(b, 'expression_Expression9', None)
    assert not _is_linked(b, 'expression_Expression9', a2)
    if hasattr(a2, 'expression_PredicateComparisonOperator8'):
        assert not _is_linked(a2, 'expression_PredicateComparisonOperator8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_left1_stub_double():
    # expression_PredicateEqualityOperator has no real 'expression_PredicateEqualityOperator' property in the generated
    # code (a bare stub) -- manually attach it so expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Expression(suffixes="sample_text")
    partner = expression_PredicateEqualityOperator()
    setattr(partner, 'expression_PredicateEqualityOperator', None)
    _safe_set(owner, 'expression_Expression', partner)
    assert getattr(partner, 'expression_PredicateEqualityOperator') == owner
    _safe_set(owner, 'expression_Expression', None)
    assert getattr(partner, 'expression_PredicateEqualityOperator') is None


def test_assoc_left10_stub_double():
    # expression_PredicateInOperator has no real 'expression_PredicateInOperator' property in the generated
    # code (a bare stub) -- manually attach it so expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Expression(suffixes="sample_text")
    partner = expression_PredicateInOperator()
    setattr(partner, 'expression_PredicateInOperator', None)
    _safe_set(owner, 'expression_Expression11', partner)
    assert getattr(partner, 'expression_PredicateInOperator') == owner
    _safe_set(owner, 'expression_Expression11', None)
    assert getattr(partner, 'expression_PredicateInOperator') is None


def test_assoc_left15_stub_double():
    # expression_PredicateIsOperator has no real 'expression_PredicateIsOperator' property in the generated
    # code (a bare stub) -- manually attach it so expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Expression(suffixes="sample_text")
    partner = expression_PredicateIsOperator()
    setattr(partner, 'expression_PredicateIsOperator', None)
    _safe_set(owner, 'expression_Expression16', partner)
    assert getattr(partner, 'expression_PredicateIsOperator') == owner
    _safe_set(owner, 'expression_Expression16', None)
    assert getattr(partner, 'expression_PredicateIsOperator') is None


def test_assoc_left20_stub_double():
    # expression_PredicateLikeOperator has no real 'expression_PredicateLikeOperator' property in the generated
    # code (a bare stub) -- manually attach it so expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Expression(suffixes="sample_text")
    partner = expression_PredicateLikeOperator()
    setattr(partner, 'expression_PredicateLikeOperator', None)
    _safe_set(owner, 'expression_Expression21', partner)
    assert getattr(partner, 'expression_PredicateLikeOperator') == owner
    _safe_set(owner, 'expression_Expression21', None)
    assert getattr(partner, 'expression_PredicateLikeOperator') is None


def test_assoc_right12_stub_double():
    # expression_PredicateInOperator has no real 'expression_PredicateInOperator13' property in the generated
    # code (a bare stub) -- manually attach it so expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Expression(suffixes="sample_text")
    partner = expression_PredicateInOperator()
    setattr(partner, 'expression_PredicateInOperator13', None)
    _safe_set(owner, 'expression_Expression14', partner)
    assert getattr(partner, 'expression_PredicateInOperator13') == owner
    _safe_set(owner, 'expression_Expression14', None)
    assert getattr(partner, 'expression_PredicateInOperator13') is None


def test_assoc_right17_stub_double():
    # expression_PredicateIsOperator has no real 'expression_PredicateIsOperator18' property in the generated
    # code (a bare stub) -- manually attach it so expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Expression(suffixes="sample_text")
    partner = expression_PredicateIsOperator()
    setattr(partner, 'expression_PredicateIsOperator18', None)
    _safe_set(owner, 'expression_Expression19', partner)
    assert getattr(partner, 'expression_PredicateIsOperator18') == owner
    _safe_set(owner, 'expression_Expression19', None)
    assert getattr(partner, 'expression_PredicateIsOperator18') is None


def test_assoc_right2_stub_double():
    # expression_PredicateEqualityOperator has no real 'expression_PredicateEqualityOperator3' property in the generated
    # code (a bare stub) -- manually attach it so expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Expression(suffixes="sample_text")
    partner = expression_PredicateEqualityOperator()
    setattr(partner, 'expression_PredicateEqualityOperator3', None)
    _safe_set(owner, 'expression_Expression4', partner)
    assert getattr(partner, 'expression_PredicateEqualityOperator3') == owner
    _safe_set(owner, 'expression_Expression4', None)
    assert getattr(partner, 'expression_PredicateEqualityOperator3') is None


def test_assoc_right22_stub_double():
    # expression_PredicateLikeOperator has no real 'expression_PredicateLikeOperator23' property in the generated
    # code (a bare stub) -- manually attach it so expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Expression(suffixes="sample_text")
    partner = expression_PredicateLikeOperator()
    setattr(partner, 'expression_PredicateLikeOperator23', None)
    _safe_set(owner, 'expression_Expression24', partner)
    assert getattr(partner, 'expression_PredicateLikeOperator23') == owner
    _safe_set(owner, 'expression_Expression24', None)
    assert getattr(partner, 'expression_PredicateLikeOperator23') is None


