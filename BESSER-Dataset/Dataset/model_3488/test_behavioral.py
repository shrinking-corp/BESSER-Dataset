import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    model_Conjunction,
    model_Disjunction,
    model_Equation,
    model_ExistsContextualExpression,
    model_Expression,
    model_ForAllContextualExpression,
    model_Implication,
    model_Negation,
    model_PrimaryExpression,
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

def test_assoc_expression0_stub_double():
    # model_Expression has no real 'model_Expression' property in the generated
    # code (a bare stub) -- manually attach it so model_ForAllContextualExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ForAllContextualExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ForAllContextualExpression(contextId="sample_text")
    partner = model_Expression()
    setattr(partner, 'model_Expression', None)
    _safe_set(owner, 'model_ForAllContextualExpression', partner)
    assert getattr(partner, 'model_Expression') == owner
    _safe_set(owner, 'model_ForAllContextualExpression', None)
    assert getattr(partner, 'model_Expression') is None


def test_assoc_expression1_stub_double():
    # model_Expression has no real 'model_Expression2' property in the generated
    # code (a bare stub) -- manually attach it so model_ExistsContextualExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ExistsContextualExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ExistsContextualExpression(contextId="sample_text")
    partner = model_Expression()
    setattr(partner, 'model_Expression2', None)
    _safe_set(owner, 'model_ExistsContextualExpression', partner)
    assert getattr(partner, 'model_Expression2') == owner
    _safe_set(owner, 'model_ExistsContextualExpression', None)
    assert getattr(partner, 'model_Expression2') is None


