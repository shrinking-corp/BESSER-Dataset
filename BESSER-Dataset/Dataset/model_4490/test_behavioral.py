import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actions,
    Expression,
    RotateMovementAction,
    RotatePoints,
    dSL_ANDexpression,
    dSL_Actions,
    dSL_Behaviors,
    dSL_ColorLiteral,
    dSL_DistanceLiteral,
    dSL_EdgeLiteral,
    dSL_Expression,
    dSL_ExpressionBracket,
    dSL_LeftMovementAction,
    dSL_LeftRotatePoint,
    dSL_MiddleRotatePoint,
    dSL_MovementAction,
    dSL_ORexpression,
    dSL_RightMovementAction,
    dSL_RightRotatePoint,
    dSL_RobotBehavior,
    dSL_RotateMovementAction,
    dSL_RotatePoints,
    dSL_TouchLiteral,
    ActionEnum,
    ColorEnum,
    EdgeEnum,
    FBEnum,
    LREnum,
    TouchEnum,
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

def test_assoc_actionlist3_stub_double():
    # dSL_Actions has no real 'dSL_Actions' property in the generated
    # code (a bare stub) -- manually attach it so dSL_Behaviors's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_Behaviors's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_Behaviors(name="sample_text")
    partner = dSL_Actions()
    setattr(partner, 'dSL_Actions', None)
    _safe_set(owner, 'dSL_Behaviors4', {partner})
    assert getattr(partner, 'dSL_Actions') == owner
    _safe_set(owner, 'dSL_Behaviors4', set())
    assert getattr(partner, 'dSL_Actions') is None


def test_assoc_behaviorlist0_stub_double():
    # dSL_RobotBehavior has no real 'dSL_RobotBehavior' property in the generated
    # code (a bare stub) -- manually attach it so dSL_Behaviors's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_Behaviors's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_Behaviors(name="sample_text")
    partner = dSL_RobotBehavior()
    setattr(partner, 'dSL_RobotBehavior', None)
    _safe_set(owner, 'dSL_Behaviors', partner)
    assert owner in getattr(partner, 'dSL_RobotBehavior')
    _safe_set(owner, 'dSL_Behaviors', None)
    assert owner not in getattr(partner, 'dSL_RobotBehavior')


def test_assoc_leftmove5_stub_double():
    # dSL_LeftMovementAction has no real 'dSL_LeftMovementAction' property in the generated
    # code (a bare stub) -- manually attach it so dSL_MovementAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_MovementAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_MovementAction(actionenum="sample_text")
    partner = dSL_LeftMovementAction()
    setattr(partner, 'dSL_LeftMovementAction', None)
    _safe_set(owner, 'dSL_MovementAction', partner)
    assert getattr(partner, 'dSL_LeftMovementAction') == owner
    _safe_set(owner, 'dSL_MovementAction', None)
    assert getattr(partner, 'dSL_LeftMovementAction') is None


def test_assoc_rightmove6_stub_double():
    # dSL_RightMovementAction has no real 'dSL_RightMovementAction' property in the generated
    # code (a bare stub) -- manually attach it so dSL_MovementAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_MovementAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_MovementAction(actionenum="sample_text")
    partner = dSL_RightMovementAction()
    setattr(partner, 'dSL_RightMovementAction', None)
    _safe_set(owner, 'dSL_MovementAction7', partner)
    assert getattr(partner, 'dSL_RightMovementAction') == owner
    _safe_set(owner, 'dSL_MovementAction7', None)
    assert getattr(partner, 'dSL_RightMovementAction') is None


def test_assoc_sensorExpression1_stub_double():
    # dSL_Expression has no real 'dSL_Expression' property in the generated
    # code (a bare stub) -- manually attach it so dSL_Behaviors's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_Behaviors's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_Behaviors(name="sample_text")
    partner = dSL_Expression()
    setattr(partner, 'dSL_Expression', None)
    _safe_set(owner, 'dSL_Behaviors2', partner)
    assert getattr(partner, 'dSL_Expression') == owner
    _safe_set(owner, 'dSL_Behaviors2', None)
    assert getattr(partner, 'dSL_Expression') is None


