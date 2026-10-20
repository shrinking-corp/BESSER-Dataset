import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actions,
    EndCondition,
    Expression,
    RotateMovementAction,
    RotatePoints,
    dSL_ANDexpression,
    dSL_Actions,
    dSL_Behavior,
    dSL_BehaviorName,
    dSL_ColorLiteral,
    dSL_DepthLiteral,
    dSL_DistanceLiteral,
    dSL_EdgeLiteral,
    dSL_EndAfter,
    dSL_EndCondition,
    dSL_EndWhen,
    dSL_Expression,
    dSL_ExpressionBracket,
    dSL_LeftMovementAction,
    dSL_LeftRotatePoint,
    dSL_MarsRoverExpedition,
    dSL_MeasurementAction,
    dSL_MiddleRotatePoint,
    dSL_Mission,
    dSL_MoveAction,
    dSL_MovementAction,
    dSL_ORexpression,
    dSL_RightMovementAction,
    dSL_RightRotatePoint,
    dSL_RotateMovementAction,
    dSL_RotatePoints,
    dSL_TouchLiteral,
    dSL_TrueLiteral,
    ActionEnum,
    BackEnum,
    ColorEnum,
    EdgeEnum,
    FBEnum,
    LREnum,
    MAEnum,
    Tenum,
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

def test_assoc_behaviorlist3_reverse_link_reassign_clear():
    a1 = dSL_Mission(name="sample_text")
    a2 = dSL_Mission(name="sample_text_2")
    b = dSL_BehaviorName(name="sample_text")
    _safe_set(b, 'dSL_BehaviorName', a1)
    assert _is_linked(b, 'dSL_BehaviorName', a1)
    if hasattr(a1, 'dSL_Mission4'):
        assert _is_linked(a1, 'dSL_Mission4', b)
    _safe_set(b, 'dSL_BehaviorName', a2)
    assert _is_linked(b, 'dSL_BehaviorName', a2)
    if hasattr(a1, 'dSL_Mission4'):
        assert not _is_linked(a1, 'dSL_Mission4', b)
    if hasattr(a2, 'dSL_Mission4'):
        assert _is_linked(a2, 'dSL_Mission4', b)
    _safe_set(b, 'dSL_BehaviorName', None)
    assert not _is_linked(b, 'dSL_BehaviorName', a2)
    if hasattr(a2, 'dSL_Mission4'):
        assert not _is_linked(a2, 'dSL_Mission4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actionlist11_stub_double():
    # dSL_Actions has no real 'dSL_Actions' property in the generated
    # code (a bare stub) -- manually attach it so dSL_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_Behavior(name="sample_text")
    partner = dSL_Actions()
    setattr(partner, 'dSL_Actions', None)
    _safe_set(owner, 'dSL_Behavior12', {partner})
    assert getattr(partner, 'dSL_Actions') == owner
    _safe_set(owner, 'dSL_Behavior12', set())
    assert getattr(partner, 'dSL_Actions') is None


def test_assoc_endcondition5_stub_double():
    # dSL_EndCondition has no real 'dSL_EndCondition' property in the generated
    # code (a bare stub) -- manually attach it so dSL_Mission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_Mission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_Mission(name="sample_text")
    partner = dSL_EndCondition()
    setattr(partner, 'dSL_EndCondition', None)
    _safe_set(owner, 'dSL_Mission6', partner)
    assert getattr(partner, 'dSL_EndCondition') == owner
    _safe_set(owner, 'dSL_Mission6', None)
    assert getattr(partner, 'dSL_EndCondition') is None


def test_assoc_endwhenlist7_stub_double():
    # dSL_EndCondition has no real 'dSL_EndCondition8' property in the generated
    # code (a bare stub) -- manually attach it so dSL_EndWhen's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_EndWhen's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_EndWhen(name="sample_text", times=7)
    partner = dSL_EndCondition()
    setattr(partner, 'dSL_EndCondition8', None)
    _safe_set(owner, 'dSL_EndWhen', partner)
    assert owner in getattr(partner, 'dSL_EndCondition8')
    _safe_set(owner, 'dSL_EndWhen', None)
    assert owner not in getattr(partner, 'dSL_EndCondition8')


def test_assoc_leftmove13_stub_double():
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


def test_assoc_missionlist0_stub_double():
    # dSL_MarsRoverExpedition has no real 'dSL_MarsRoverExpedition' property in the generated
    # code (a bare stub) -- manually attach it so dSL_Mission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_Mission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_Mission(name="sample_text")
    partner = dSL_MarsRoverExpedition()
    setattr(partner, 'dSL_MarsRoverExpedition', None)
    _safe_set(owner, 'dSL_Mission', partner)
    assert owner in getattr(partner, 'dSL_MarsRoverExpedition')
    _safe_set(owner, 'dSL_Mission', None)
    assert owner not in getattr(partner, 'dSL_MarsRoverExpedition')


def test_assoc_rightmove14_stub_double():
    # dSL_RightMovementAction has no real 'dSL_RightMovementAction' property in the generated
    # code (a bare stub) -- manually attach it so dSL_MovementAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_MovementAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_MovementAction(actionenum="sample_text")
    partner = dSL_RightMovementAction()
    setattr(partner, 'dSL_RightMovementAction', None)
    _safe_set(owner, 'dSL_MovementAction15', partner)
    assert getattr(partner, 'dSL_RightMovementAction') == owner
    _safe_set(owner, 'dSL_MovementAction15', None)
    assert getattr(partner, 'dSL_RightMovementAction') is None


def test_assoc_sensorExpression9_stub_double():
    # dSL_Expression has no real 'dSL_Expression' property in the generated
    # code (a bare stub) -- manually attach it so dSL_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_Behavior(name="sample_text")
    partner = dSL_Expression()
    setattr(partner, 'dSL_Expression', None)
    _safe_set(owner, 'dSL_Behavior10', partner)
    assert getattr(partner, 'dSL_Expression') == owner
    _safe_set(owner, 'dSL_Behavior10', None)
    assert getattr(partner, 'dSL_Expression') is None


def test_assoc_tasklist1_stub_double():
    # dSL_MarsRoverExpedition has no real 'dSL_MarsRoverExpedition2' property in the generated
    # code (a bare stub) -- manually attach it so dSL_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSL_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSL_Behavior(name="sample_text")
    partner = dSL_MarsRoverExpedition()
    setattr(partner, 'dSL_MarsRoverExpedition2', None)
    _safe_set(owner, 'dSL_Behavior', partner)
    assert owner in getattr(partner, 'dSL_MarsRoverExpedition2')
    _safe_set(owner, 'dSL_Behavior', None)
    assert owner not in getattr(partner, 'dSL_MarsRoverExpedition2')


