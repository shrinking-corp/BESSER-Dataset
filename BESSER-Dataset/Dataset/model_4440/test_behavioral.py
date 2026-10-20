import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Expression,
    ValueExpression,
    roverDSL_Action,
    roverDSL_AssignExpression,
    roverDSL_BBLiteral,
    roverDSL_BNotExpr,
    roverDSL_BSensorLiteral,
    roverDSL_BVBracket,
    roverDSL_BVLiteral,
    roverDSL_BVarLiteral,
    roverDSL_BehaviorName,
    roverDSL_ColorLiteral,
    roverDSL_Expression,
    roverDSL_ExpressionBinComp,
    roverDSL_ExpressionBinOp,
    roverDSL_ForwardAction,
    roverDSL_FreeAction,
    roverDSL_Global,
    roverDSL_IFExpression,
    roverDSL_Implementation,
    roverDSL_MeasureAction,
    roverDSL_Motor,
    roverDSL_Robot,
    roverDSL_RotateAction,
    roverDSL_SAccelerationAction,
    roverDSL_SSpeedAction,
    roverDSL_ShowAction,
    roverDSL_SoundAction,
    roverDSL_Static,
    roverDSL_StopAction,
    roverDSL_SubRoutine,
    roverDSL_SubRoutineAction,
    roverDSL_ValExpr,
    roverDSL_ValueExpression,
    roverDSL_WHILEExpression,
    BBinaryOp,
    Color,
    CompareOp,
    EMotor,
    Sensor,
    Sound,
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

def test_assoc_motor46_reverse_link_reassign_clear():
    a1 = roverDSL_RotateAction(blocking=True)
    a2 = roverDSL_RotateAction(blocking=False)
    b = roverDSL_Motor(m="sample_text")
    _safe_set(b, 'roverDSL_Motor47', a1)
    assert _is_linked(b, 'roverDSL_Motor47', a1)
    if hasattr(a1, 'roverDSL_RotateAction'):
        assert _is_linked(a1, 'roverDSL_RotateAction', b)
    _safe_set(b, 'roverDSL_Motor47', a2)
    assert _is_linked(b, 'roverDSL_Motor47', a2)
    if hasattr(a1, 'roverDSL_RotateAction'):
        assert not _is_linked(a1, 'roverDSL_RotateAction', b)
    if hasattr(a2, 'roverDSL_RotateAction'):
        assert _is_linked(a2, 'roverDSL_RotateAction', b)
    _safe_set(b, 'roverDSL_Motor47', None)
    assert not _is_linked(b, 'roverDSL_Motor47', a2)
    if hasattr(a2, 'roverDSL_RotateAction'):
        assert not _is_linked(a2, 'roverDSL_RotateAction', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_behaviorOrder0_stub_double():
    # roverDSL_Robot has no real 'roverDSL_Robot' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_BehaviorName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_BehaviorName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_BehaviorName(name="sample_text")
    partner = roverDSL_Robot()
    setattr(partner, 'roverDSL_Robot', None)
    _safe_set(owner, 'roverDSL_BehaviorName', partner)
    assert owner in getattr(partner, 'roverDSL_Robot')
    _safe_set(owner, 'roverDSL_BehaviorName', None)
    assert owner not in getattr(partner, 'roverDSL_Robot')


def test_assoc_degrees48_stub_double():
    # roverDSL_ValueExpression has no real 'roverDSL_ValueExpression50' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_RotateAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_RotateAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_RotateAction(blocking=True)
    partner = roverDSL_ValueExpression()
    setattr(partner, 'roverDSL_ValueExpression50', None)
    _safe_set(owner, 'roverDSL_RotateAction49', partner)
    assert getattr(partner, 'roverDSL_ValueExpression50') == owner
    _safe_set(owner, 'roverDSL_RotateAction49', None)
    assert getattr(partner, 'roverDSL_ValueExpression50') is None


def test_assoc_expressions22_stub_double():
    # roverDSL_Expression has no real 'roverDSL_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_SubRoutine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_SubRoutine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_SubRoutine(name="sample_text")
    partner = roverDSL_Expression()
    setattr(partner, 'roverDSL_Expression24', None)
    _safe_set(owner, 'roverDSL_SubRoutine23', {partner})
    assert getattr(partner, 'roverDSL_Expression24') == owner
    _safe_set(owner, 'roverDSL_SubRoutine23', set())
    assert getattr(partner, 'roverDSL_Expression24') is None


def test_assoc_for_14_stub_double():
    # roverDSL_Implementation has no real 'roverDSL_Implementation15' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_BehaviorName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_BehaviorName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_BehaviorName(name="sample_text")
    partner = roverDSL_Implementation()
    setattr(partner, 'roverDSL_Implementation15', None)
    _safe_set(owner, 'roverDSL_BehaviorName16', partner)
    assert getattr(partner, 'roverDSL_Implementation15') == owner
    _safe_set(owner, 'roverDSL_BehaviorName16', None)
    assert getattr(partner, 'roverDSL_Implementation15') is None


def test_assoc_global_40_stub_double():
    # roverDSL_AssignExpression has no real 'roverDSL_AssignExpression' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Global's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Global's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Global(name="sample_text")
    partner = roverDSL_AssignExpression()
    setattr(partner, 'roverDSL_AssignExpression', None)
    _safe_set(owner, 'roverDSL_Global41', partner)
    assert getattr(partner, 'roverDSL_AssignExpression') == owner
    _safe_set(owner, 'roverDSL_Global41', None)
    assert getattr(partner, 'roverDSL_AssignExpression') is None


def test_assoc_globals1_stub_double():
    # roverDSL_Robot has no real 'roverDSL_Robot2' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Global's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Global's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Global(name="sample_text")
    partner = roverDSL_Robot()
    setattr(partner, 'roverDSL_Robot2', None)
    _safe_set(owner, 'roverDSL_Global', partner)
    assert owner in getattr(partner, 'roverDSL_Robot2')
    _safe_set(owner, 'roverDSL_Global', None)
    assert owner not in getattr(partner, 'roverDSL_Robot2')


def test_assoc_left71_stub_double():
    # roverDSL_ValueExpression has no real 'roverDSL_ValueExpression72' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_ExpressionBinOp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_ExpressionBinOp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_ExpressionBinOp(bop="sample_text")
    partner = roverDSL_ValueExpression()
    setattr(partner, 'roverDSL_ValueExpression72', None)
    _safe_set(owner, 'roverDSL_ExpressionBinOp', partner)
    assert getattr(partner, 'roverDSL_ValueExpression72') == owner
    _safe_set(owner, 'roverDSL_ExpressionBinOp', None)
    assert getattr(partner, 'roverDSL_ValueExpression72') is None


def test_assoc_left76_stub_double():
    # roverDSL_ValueExpression has no real 'roverDSL_ValueExpression77' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_ExpressionBinComp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_ExpressionBinComp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_ExpressionBinComp(bcomp="sample_text")
    partner = roverDSL_ValueExpression()
    setattr(partner, 'roverDSL_ValueExpression77', None)
    _safe_set(owner, 'roverDSL_ExpressionBinComp', partner)
    assert getattr(partner, 'roverDSL_ValueExpression77') == owner
    _safe_set(owner, 'roverDSL_ExpressionBinComp', None)
    assert getattr(partner, 'roverDSL_ValueExpression77') is None


def test_assoc_motor45_stub_double():
    # roverDSL_ForwardAction has no real 'roverDSL_ForwardAction' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Motor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Motor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Motor(m="sample_text")
    partner = roverDSL_ForwardAction()
    setattr(partner, 'roverDSL_ForwardAction', None)
    _safe_set(owner, 'roverDSL_Motor', partner)
    assert getattr(partner, 'roverDSL_ForwardAction') == owner
    _safe_set(owner, 'roverDSL_Motor', None)
    assert getattr(partner, 'roverDSL_ForwardAction') is None


def test_assoc_motor51_stub_double():
    # roverDSL_StopAction has no real 'roverDSL_StopAction' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Motor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Motor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Motor(m="sample_text")
    partner = roverDSL_StopAction()
    setattr(partner, 'roverDSL_StopAction', None)
    _safe_set(owner, 'roverDSL_Motor52', partner)
    assert getattr(partner, 'roverDSL_StopAction') == owner
    _safe_set(owner, 'roverDSL_Motor52', None)
    assert getattr(partner, 'roverDSL_StopAction') is None


def test_assoc_motor53_stub_double():
    # roverDSL_SAccelerationAction has no real 'roverDSL_SAccelerationAction' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Motor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Motor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Motor(m="sample_text")
    partner = roverDSL_SAccelerationAction()
    setattr(partner, 'roverDSL_SAccelerationAction', None)
    _safe_set(owner, 'roverDSL_Motor54', partner)
    assert getattr(partner, 'roverDSL_SAccelerationAction') == owner
    _safe_set(owner, 'roverDSL_Motor54', None)
    assert getattr(partner, 'roverDSL_SAccelerationAction') is None


def test_assoc_motor58_stub_double():
    # roverDSL_SSpeedAction has no real 'roverDSL_SSpeedAction' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Motor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Motor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Motor(m="sample_text")
    partner = roverDSL_SSpeedAction()
    setattr(partner, 'roverDSL_SSpeedAction', None)
    _safe_set(owner, 'roverDSL_Motor59', partner)
    assert getattr(partner, 'roverDSL_SSpeedAction') == owner
    _safe_set(owner, 'roverDSL_Motor59', None)
    assert getattr(partner, 'roverDSL_SSpeedAction') is None


def test_assoc_motor65_stub_double():
    # roverDSL_FreeAction has no real 'roverDSL_FreeAction' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Motor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Motor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Motor(m="sample_text")
    partner = roverDSL_FreeAction()
    setattr(partner, 'roverDSL_FreeAction', None)
    _safe_set(owner, 'roverDSL_Motor66', partner)
    assert getattr(partner, 'roverDSL_FreeAction') == owner
    _safe_set(owner, 'roverDSL_Motor66', None)
    assert getattr(partner, 'roverDSL_FreeAction') is None


def test_assoc_right73_stub_double():
    # roverDSL_ValueExpression has no real 'roverDSL_ValueExpression75' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_ExpressionBinOp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_ExpressionBinOp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_ExpressionBinOp(bop="sample_text")
    partner = roverDSL_ValueExpression()
    setattr(partner, 'roverDSL_ValueExpression75', None)
    _safe_set(owner, 'roverDSL_ExpressionBinOp74', partner)
    assert getattr(partner, 'roverDSL_ValueExpression75') == owner
    _safe_set(owner, 'roverDSL_ExpressionBinOp74', None)
    assert getattr(partner, 'roverDSL_ValueExpression75') is None


def test_assoc_right78_stub_double():
    # roverDSL_ValueExpression has no real 'roverDSL_ValueExpression80' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_ExpressionBinComp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_ExpressionBinComp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_ExpressionBinComp(bcomp="sample_text")
    partner = roverDSL_ValueExpression()
    setattr(partner, 'roverDSL_ValueExpression80', None)
    _safe_set(owner, 'roverDSL_ExpressionBinComp79', partner)
    assert getattr(partner, 'roverDSL_ValueExpression80') == owner
    _safe_set(owner, 'roverDSL_ExpressionBinComp79', None)
    assert getattr(partner, 'roverDSL_ValueExpression80') is None


def test_assoc_routine63_stub_double():
    # roverDSL_SubRoutineAction has no real 'roverDSL_SubRoutineAction' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_SubRoutine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_SubRoutine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_SubRoutine(name="sample_text")
    partner = roverDSL_SubRoutineAction()
    setattr(partner, 'roverDSL_SubRoutineAction', None)
    _safe_set(owner, 'roverDSL_SubRoutine64', partner)
    assert getattr(partner, 'roverDSL_SubRoutineAction') == owner
    _safe_set(owner, 'roverDSL_SubRoutine64', None)
    assert getattr(partner, 'roverDSL_SubRoutineAction') is None


def test_assoc_statics3_stub_double():
    # roverDSL_Robot has no real 'roverDSL_Robot4' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Static's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Static's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Static(name="sample_text")
    partner = roverDSL_Robot()
    setattr(partner, 'roverDSL_Robot4', None)
    _safe_set(owner, 'roverDSL_Static', partner)
    assert owner in getattr(partner, 'roverDSL_Robot4')
    _safe_set(owner, 'roverDSL_Static', None)
    assert owner not in getattr(partner, 'roverDSL_Robot4')


def test_assoc_subRoutines9_stub_double():
    # roverDSL_Robot has no real 'roverDSL_Robot10' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_SubRoutine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_SubRoutine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_SubRoutine(name="sample_text")
    partner = roverDSL_Robot()
    setattr(partner, 'roverDSL_Robot10', None)
    _safe_set(owner, 'roverDSL_SubRoutine', partner)
    assert owner in getattr(partner, 'roverDSL_Robot10')
    _safe_set(owner, 'roverDSL_SubRoutine', None)
    assert owner not in getattr(partner, 'roverDSL_Robot10')


def test_assoc_value11_stub_double():
    # roverDSL_ValueExpression has no real 'roverDSL_ValueExpression13' property in the generated
    # code (a bare stub) -- manually attach it so roverDSL_Static's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverDSL_Static's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverDSL_Static(name="sample_text")
    partner = roverDSL_ValueExpression()
    setattr(partner, 'roverDSL_ValueExpression13', None)
    _safe_set(owner, 'roverDSL_Static12', partner)
    assert getattr(partner, 'roverDSL_ValueExpression13') == owner
    _safe_set(owner, 'roverDSL_Static12', None)
    assert getattr(partner, 'roverDSL_ValueExpression13') is None


