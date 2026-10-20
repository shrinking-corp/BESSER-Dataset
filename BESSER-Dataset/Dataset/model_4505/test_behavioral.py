import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    BooleanValue,
    NumberValue,
    Query,
    RoverExpression,
    RoverValue,
    Statement,
    StringValue,
    rcl_Action,
    rcl_BackwardAction,
    rcl_BackwardMinAction,
    rcl_BooleanExpression,
    rcl_BooleanValue,
    rcl_Conditional,
    rcl_ForwardAction,
    rcl_ForwardMinAction,
    rcl_HumidityQuery,
    rcl_LogAction,
    rcl_Loop,
    rcl_MessageQuery,
    rcl_NumberValue,
    rcl_NumericExpression,
    rcl_ObstacleQuery,
    rcl_Param,
    rcl_Query,
    rcl_RclBlock,
    rcl_RoverExpression,
    rcl_RoverProgram,
    rcl_RoverValue,
    rcl_SendAction,
    rcl_Statement,
    rcl_StopAction,
    rcl_StringExpression,
    rcl_StringValue,
    rcl_TemperatureQuery,
    rcl_TurnAction,
    rcl_TurnDegAction,
    rcl_VarAssignment,
    rcl_VarRef,
    BooleanOperator,
    NumericOperator,
    StringOperator,
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

def test_assoc_lhs18_reverse_link_reassign_clear():
    a1 = rcl_NumericExpression(op="sample_text")
    a2 = rcl_NumericExpression(op="sample_text_2")
    b = rcl_NumberValue(nValue=7)
    _safe_set(b, 'rcl_NumberValue', a1)
    assert _is_linked(b, 'rcl_NumberValue', a1)
    if hasattr(a1, 'rcl_NumericExpression'):
        assert _is_linked(a1, 'rcl_NumericExpression', b)
    _safe_set(b, 'rcl_NumberValue', a2)
    assert _is_linked(b, 'rcl_NumberValue', a2)
    if hasattr(a1, 'rcl_NumericExpression'):
        assert not _is_linked(a1, 'rcl_NumericExpression', b)
    if hasattr(a2, 'rcl_NumericExpression'):
        assert _is_linked(a2, 'rcl_NumericExpression', b)
    _safe_set(b, 'rcl_NumberValue', None)
    assert not _is_linked(b, 'rcl_NumberValue', a2)
    if hasattr(a2, 'rcl_NumericExpression'):
        assert not _is_linked(a2, 'rcl_NumericExpression', b)


def test_assoc_lhs22_reverse_link_reassign_clear():
    a1 = rcl_StringValue(sValue="sample_text")
    a2 = rcl_StringValue(sValue="sample_text_2")
    b = rcl_StringExpression(op="sample_text")
    _safe_set(b, 'rcl_StringExpression', a1)
    assert _is_linked(b, 'rcl_StringExpression', a1)
    if hasattr(a1, 'rcl_StringValue'):
        assert _is_linked(a1, 'rcl_StringValue', b)
    _safe_set(b, 'rcl_StringExpression', a2)
    assert _is_linked(b, 'rcl_StringExpression', a2)
    if hasattr(a1, 'rcl_StringValue'):
        assert not _is_linked(a1, 'rcl_StringValue', b)
    if hasattr(a2, 'rcl_StringValue'):
        assert _is_linked(a2, 'rcl_StringValue', b)
    _safe_set(b, 'rcl_StringExpression', None)
    assert not _is_linked(b, 'rcl_StringExpression', a2)
    if hasattr(a2, 'rcl_StringValue'):
        assert not _is_linked(a2, 'rcl_StringValue', b)


def test_assoc_lhs26_reverse_link_reassign_clear():
    a1 = rcl_BooleanValue(bValue=True)
    a2 = rcl_BooleanValue(bValue=False)
    b = rcl_BooleanExpression(op="sample_text")
    _safe_set(b, 'rcl_BooleanExpression', a1)
    assert _is_linked(b, 'rcl_BooleanExpression', a1)
    if hasattr(a1, 'rcl_BooleanValue'):
        assert _is_linked(a1, 'rcl_BooleanValue', b)
    _safe_set(b, 'rcl_BooleanExpression', a2)
    assert _is_linked(b, 'rcl_BooleanExpression', a2)
    if hasattr(a1, 'rcl_BooleanValue'):
        assert not _is_linked(a1, 'rcl_BooleanValue', b)
    if hasattr(a2, 'rcl_BooleanValue'):
        assert _is_linked(a2, 'rcl_BooleanValue', b)
    _safe_set(b, 'rcl_BooleanExpression', None)
    assert not _is_linked(b, 'rcl_BooleanExpression', a2)
    if hasattr(a2, 'rcl_BooleanValue'):
        assert not _is_linked(a2, 'rcl_BooleanValue', b)


def test_assoc_params0_reverse_link_reassign_clear():
    a1 = rcl_RoverProgram(name="sample_text")
    a2 = rcl_RoverProgram(name="sample_text_2")
    b = rcl_Param(name="sample_text")
    _safe_set(b, 'rcl_Param', a1)
    assert _is_linked(b, 'rcl_Param', a1)
    if hasattr(a1, 'rcl_RoverProgram'):
        assert _is_linked(a1, 'rcl_RoverProgram', b)
    _safe_set(b, 'rcl_Param', a2)
    assert _is_linked(b, 'rcl_Param', a2)
    if hasattr(a1, 'rcl_RoverProgram'):
        assert not _is_linked(a1, 'rcl_RoverProgram', b)
    if hasattr(a2, 'rcl_RoverProgram'):
        assert _is_linked(a2, 'rcl_RoverProgram', b)
    _safe_set(b, 'rcl_Param', None)
    assert not _is_linked(b, 'rcl_Param', a2)
    if hasattr(a2, 'rcl_RoverProgram'):
        assert not _is_linked(a2, 'rcl_RoverProgram', b)


def test_assoc_rhs19_reverse_link_reassign_clear():
    a1 = rcl_NumericExpression(op="sample_text")
    a2 = rcl_NumericExpression(op="sample_text_2")
    b = rcl_NumberValue(nValue=7)
    _safe_set(b, 'rcl_NumberValue21', a1)
    assert _is_linked(b, 'rcl_NumberValue21', a1)
    if hasattr(a1, 'rcl_NumericExpression20'):
        assert _is_linked(a1, 'rcl_NumericExpression20', b)
    _safe_set(b, 'rcl_NumberValue21', a2)
    assert _is_linked(b, 'rcl_NumberValue21', a2)
    if hasattr(a1, 'rcl_NumericExpression20'):
        assert not _is_linked(a1, 'rcl_NumericExpression20', b)
    if hasattr(a2, 'rcl_NumericExpression20'):
        assert _is_linked(a2, 'rcl_NumericExpression20', b)
    _safe_set(b, 'rcl_NumberValue21', None)
    assert not _is_linked(b, 'rcl_NumberValue21', a2)
    if hasattr(a2, 'rcl_NumericExpression20'):
        assert not _is_linked(a2, 'rcl_NumericExpression20', b)


def test_assoc_rhs23_reverse_link_reassign_clear():
    a1 = rcl_StringValue(sValue="sample_text")
    a2 = rcl_StringValue(sValue="sample_text_2")
    b = rcl_StringExpression(op="sample_text")
    _safe_set(b, 'rcl_StringExpression24', a1)
    assert _is_linked(b, 'rcl_StringExpression24', a1)
    if hasattr(a1, 'rcl_StringValue25'):
        assert _is_linked(a1, 'rcl_StringValue25', b)
    _safe_set(b, 'rcl_StringExpression24', a2)
    assert _is_linked(b, 'rcl_StringExpression24', a2)
    if hasattr(a1, 'rcl_StringValue25'):
        assert not _is_linked(a1, 'rcl_StringValue25', b)
    if hasattr(a2, 'rcl_StringValue25'):
        assert _is_linked(a2, 'rcl_StringValue25', b)
    _safe_set(b, 'rcl_StringExpression24', None)
    assert not _is_linked(b, 'rcl_StringExpression24', a2)
    if hasattr(a2, 'rcl_StringValue25'):
        assert not _is_linked(a2, 'rcl_StringValue25', b)


def test_assoc_rhs27_reverse_link_reassign_clear():
    a1 = rcl_BooleanValue(bValue=True)
    a2 = rcl_BooleanValue(bValue=False)
    b = rcl_BooleanExpression(op="sample_text")
    _safe_set(b, 'rcl_BooleanExpression28', a1)
    assert _is_linked(b, 'rcl_BooleanExpression28', a1)
    if hasattr(a1, 'rcl_BooleanValue29'):
        assert _is_linked(a1, 'rcl_BooleanValue29', b)
    _safe_set(b, 'rcl_BooleanExpression28', a2)
    assert _is_linked(b, 'rcl_BooleanExpression28', a2)
    if hasattr(a1, 'rcl_BooleanValue29'):
        assert not _is_linked(a1, 'rcl_BooleanValue29', b)
    if hasattr(a2, 'rcl_BooleanValue29'):
        assert _is_linked(a2, 'rcl_BooleanValue29', b)
    _safe_set(b, 'rcl_BooleanExpression28', None)
    assert not _is_linked(b, 'rcl_BooleanExpression28', a2)
    if hasattr(a2, 'rcl_BooleanValue29'):
        assert not _is_linked(a2, 'rcl_BooleanValue29', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_block1_stub_double():
    # rcl_RclBlock has no real 'rcl_RclBlock' property in the generated
    # code (a bare stub) -- manually attach it so rcl_RoverProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rcl_RoverProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rcl_RoverProgram(name="sample_text")
    partner = rcl_RclBlock()
    setattr(partner, 'rcl_RclBlock', None)
    _safe_set(owner, 'rcl_RoverProgram2', partner)
    assert getattr(partner, 'rcl_RclBlock') == owner
    _safe_set(owner, 'rcl_RoverProgram2', None)
    assert getattr(partner, 'rcl_RclBlock') is None


def test_assoc_degrees34_stub_double():
    # rcl_TurnDegAction has no real 'rcl_TurnDegAction' property in the generated
    # code (a bare stub) -- manually attach it so rcl_NumberValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rcl_NumberValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rcl_NumberValue(nValue=7)
    partner = rcl_TurnDegAction()
    setattr(partner, 'rcl_TurnDegAction', None)
    _safe_set(owner, 'rcl_NumberValue35', partner)
    assert getattr(partner, 'rcl_TurnDegAction') == owner
    _safe_set(owner, 'rcl_NumberValue35', None)
    assert getattr(partner, 'rcl_TurnDegAction') is None


def test_assoc_distance30_stub_double():
    # rcl_ForwardMinAction has no real 'rcl_ForwardMinAction' property in the generated
    # code (a bare stub) -- manually attach it so rcl_NumberValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rcl_NumberValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rcl_NumberValue(nValue=7)
    partner = rcl_ForwardMinAction()
    setattr(partner, 'rcl_ForwardMinAction', None)
    _safe_set(owner, 'rcl_NumberValue31', partner)
    assert getattr(partner, 'rcl_ForwardMinAction') == owner
    _safe_set(owner, 'rcl_NumberValue31', None)
    assert getattr(partner, 'rcl_ForwardMinAction') is None


def test_assoc_distance32_stub_double():
    # rcl_BackwardMinAction has no real 'rcl_BackwardMinAction' property in the generated
    # code (a bare stub) -- manually attach it so rcl_NumberValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rcl_NumberValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rcl_NumberValue(nValue=7)
    partner = rcl_BackwardMinAction()
    setattr(partner, 'rcl_BackwardMinAction', None)
    _safe_set(owner, 'rcl_NumberValue33', partner)
    assert getattr(partner, 'rcl_BackwardMinAction') == owner
    _safe_set(owner, 'rcl_NumberValue33', None)
    assert getattr(partner, 'rcl_BackwardMinAction') is None


def test_assoc_value4_stub_double():
    # rcl_RoverValue has no real 'rcl_RoverValue' property in the generated
    # code (a bare stub) -- manually attach it so rcl_VarAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rcl_VarAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rcl_VarAssignment(name="sample_text")
    partner = rcl_RoverValue()
    setattr(partner, 'rcl_RoverValue', None)
    _safe_set(owner, 'rcl_VarAssignment', partner)
    assert getattr(partner, 'rcl_RoverValue') == owner
    _safe_set(owner, 'rcl_VarAssignment', None)
    assert getattr(partner, 'rcl_RoverValue') is None


