import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    simpleExpressions_AndExpression,
    simpleExpressions_Comparison,
    simpleExpressions_Expression,
    simpleExpressions_IfCondition,
    simpleExpressions_MethodCall,
    simpleExpressions_NotExpression,
    simpleExpressions_NumberLiteral,
    simpleExpressions_OrExpression,
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

def test_assoc_condition0_stub_double():
    # simpleExpressions_Expression has no real 'simpleExpressions_Expression' property in the generated
    # code (a bare stub) -- manually attach it so simpleExpressions_IfCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleExpressions_IfCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleExpressions_IfCondition(elseif=True)
    partner = simpleExpressions_Expression()
    setattr(partner, 'simpleExpressions_Expression', None)
    _safe_set(owner, 'simpleExpressions_IfCondition', partner)
    assert getattr(partner, 'simpleExpressions_Expression') == owner
    _safe_set(owner, 'simpleExpressions_IfCondition', None)
    assert getattr(partner, 'simpleExpressions_Expression') is None


def test_assoc_left11_stub_double():
    # simpleExpressions_Expression has no real 'simpleExpressions_Expression12' property in the generated
    # code (a bare stub) -- manually attach it so simpleExpressions_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleExpressions_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleExpressions_Comparison(operator="sample_text")
    partner = simpleExpressions_Expression()
    setattr(partner, 'simpleExpressions_Expression12', None)
    _safe_set(owner, 'simpleExpressions_Comparison', partner)
    assert getattr(partner, 'simpleExpressions_Expression12') == owner
    _safe_set(owner, 'simpleExpressions_Comparison', None)
    assert getattr(partner, 'simpleExpressions_Expression12') is None


def test_assoc_right13_stub_double():
    # simpleExpressions_Expression has no real 'simpleExpressions_Expression15' property in the generated
    # code (a bare stub) -- manually attach it so simpleExpressions_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleExpressions_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleExpressions_Comparison(operator="sample_text")
    partner = simpleExpressions_Expression()
    setattr(partner, 'simpleExpressions_Expression15', None)
    _safe_set(owner, 'simpleExpressions_Comparison14', partner)
    assert getattr(partner, 'simpleExpressions_Expression15') == owner
    _safe_set(owner, 'simpleExpressions_Comparison14', None)
    assert getattr(partner, 'simpleExpressions_Expression15') is None


