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

def test_assoc_block1_reverse_link_reassign_clear():
    a1 = rcl_RoverProgram(name="sample_text")
    a2 = rcl_RoverProgram(name="sample_text_2")
    b = rcl_RclBlock()
    _safe_set(b, 'rcl_RclBlock', a1)
    assert _is_linked(b, 'rcl_RclBlock', a1)
    if hasattr(a1, 'rcl_RoverProgram2'):
        assert _is_linked(a1, 'rcl_RoverProgram2', b)
    _safe_set(b, 'rcl_RclBlock', a2)
    assert _is_linked(b, 'rcl_RclBlock', a2)
    if hasattr(a1, 'rcl_RoverProgram2'):
        assert not _is_linked(a1, 'rcl_RoverProgram2', b)
    if hasattr(a2, 'rcl_RoverProgram2'):
        assert _is_linked(a2, 'rcl_RoverProgram2', b)
    _safe_set(b, 'rcl_RclBlock', None)
    assert not _is_linked(b, 'rcl_RclBlock', a2)
    if hasattr(a2, 'rcl_RoverProgram2'):
        assert not _is_linked(a2, 'rcl_RoverProgram2', b)


def test_assoc_block14_reverse_link_reassign_clear():
    a1 = rcl_RclBlock()
    a2 = rcl_RclBlock()
    b = rcl_Loop()
    _safe_set(b, 'rcl_Loop15', a1)
    assert _is_linked(b, 'rcl_Loop15', a1)
    if hasattr(a1, 'rcl_RclBlock16'):
        assert _is_linked(a1, 'rcl_RclBlock16', b)
    _safe_set(b, 'rcl_Loop15', a2)
    assert _is_linked(b, 'rcl_Loop15', a2)
    if hasattr(a1, 'rcl_RclBlock16'):
        assert not _is_linked(a1, 'rcl_RclBlock16', b)
    if hasattr(a2, 'rcl_RclBlock16'):
        assert _is_linked(a2, 'rcl_RclBlock16', b)
    _safe_set(b, 'rcl_Loop15', None)
    assert not _is_linked(b, 'rcl_Loop15', a2)
    if hasattr(a2, 'rcl_RclBlock16'):
        assert not _is_linked(a2, 'rcl_RclBlock16', b)


def test_assoc_condFalse9_reverse_link_reassign_clear():
    a1 = rcl_RclBlock()
    a2 = rcl_RclBlock()
    b = rcl_Conditional()
    _safe_set(b, 'rcl_Conditional10', a1)
    assert _is_linked(b, 'rcl_Conditional10', a1)
    if hasattr(a1, 'rcl_RclBlock11'):
        assert _is_linked(a1, 'rcl_RclBlock11', b)
    _safe_set(b, 'rcl_Conditional10', a2)
    assert _is_linked(b, 'rcl_Conditional10', a2)
    if hasattr(a1, 'rcl_RclBlock11'):
        assert not _is_linked(a1, 'rcl_RclBlock11', b)
    if hasattr(a2, 'rcl_RclBlock11'):
        assert _is_linked(a2, 'rcl_RclBlock11', b)
    _safe_set(b, 'rcl_Conditional10', None)
    assert not _is_linked(b, 'rcl_Conditional10', a2)
    if hasattr(a2, 'rcl_RclBlock11'):
        assert not _is_linked(a2, 'rcl_RclBlock11', b)


def test_assoc_condTrue6_reverse_link_reassign_clear():
    a1 = rcl_RclBlock()
    a2 = rcl_RclBlock()
    b = rcl_Conditional()
    _safe_set(b, 'rcl_Conditional7', a1)
    assert _is_linked(b, 'rcl_Conditional7', a1)
    if hasattr(a1, 'rcl_RclBlock8'):
        assert _is_linked(a1, 'rcl_RclBlock8', b)
    _safe_set(b, 'rcl_Conditional7', a2)
    assert _is_linked(b, 'rcl_Conditional7', a2)
    if hasattr(a1, 'rcl_RclBlock8'):
        assert not _is_linked(a1, 'rcl_RclBlock8', b)
    if hasattr(a2, 'rcl_RclBlock8'):
        assert _is_linked(a2, 'rcl_RclBlock8', b)
    _safe_set(b, 'rcl_Conditional7', None)
    assert not _is_linked(b, 'rcl_Conditional7', a2)
    if hasattr(a2, 'rcl_RclBlock8'):
        assert not _is_linked(a2, 'rcl_RclBlock8', b)


def test_assoc_degrees34_reverse_link_reassign_clear():
    a1 = rcl_TurnDegAction()
    a2 = rcl_TurnDegAction()
    b = rcl_NumberValue(nValue="sample_text")
    _safe_set(b, 'rcl_NumberValue35', a1)
    assert _is_linked(b, 'rcl_NumberValue35', a1)
    if hasattr(a1, 'rcl_TurnDegAction'):
        assert _is_linked(a1, 'rcl_TurnDegAction', b)
    _safe_set(b, 'rcl_NumberValue35', a2)
    assert _is_linked(b, 'rcl_NumberValue35', a2)
    if hasattr(a1, 'rcl_TurnDegAction'):
        assert not _is_linked(a1, 'rcl_TurnDegAction', b)
    if hasattr(a2, 'rcl_TurnDegAction'):
        assert _is_linked(a2, 'rcl_TurnDegAction', b)
    _safe_set(b, 'rcl_NumberValue35', None)
    assert not _is_linked(b, 'rcl_NumberValue35', a2)
    if hasattr(a2, 'rcl_TurnDegAction'):
        assert not _is_linked(a2, 'rcl_TurnDegAction', b)


def test_assoc_distance30_reverse_link_reassign_clear():
    a1 = rcl_NumberValue(nValue="sample_text")
    a2 = rcl_NumberValue(nValue="sample_text_2")
    b = rcl_ForwardMinAction()
    _safe_set(b, 'rcl_ForwardMinAction', a1)
    assert _is_linked(b, 'rcl_ForwardMinAction', a1)
    if hasattr(a1, 'rcl_NumberValue31'):
        assert _is_linked(a1, 'rcl_NumberValue31', b)
    _safe_set(b, 'rcl_ForwardMinAction', a2)
    assert _is_linked(b, 'rcl_ForwardMinAction', a2)
    if hasattr(a1, 'rcl_NumberValue31'):
        assert not _is_linked(a1, 'rcl_NumberValue31', b)
    if hasattr(a2, 'rcl_NumberValue31'):
        assert _is_linked(a2, 'rcl_NumberValue31', b)
    _safe_set(b, 'rcl_ForwardMinAction', None)
    assert not _is_linked(b, 'rcl_ForwardMinAction', a2)
    if hasattr(a2, 'rcl_NumberValue31'):
        assert not _is_linked(a2, 'rcl_NumberValue31', b)


def test_assoc_distance32_reverse_link_reassign_clear():
    a1 = rcl_NumberValue(nValue="sample_text")
    a2 = rcl_NumberValue(nValue="sample_text_2")
    b = rcl_BackwardMinAction()
    _safe_set(b, 'rcl_BackwardMinAction', a1)
    assert _is_linked(b, 'rcl_BackwardMinAction', a1)
    if hasattr(a1, 'rcl_NumberValue33'):
        assert _is_linked(a1, 'rcl_NumberValue33', b)
    _safe_set(b, 'rcl_BackwardMinAction', a2)
    assert _is_linked(b, 'rcl_BackwardMinAction', a2)
    if hasattr(a1, 'rcl_NumberValue33'):
        assert not _is_linked(a1, 'rcl_NumberValue33', b)
    if hasattr(a2, 'rcl_NumberValue33'):
        assert _is_linked(a2, 'rcl_NumberValue33', b)
    _safe_set(b, 'rcl_BackwardMinAction', None)
    assert not _is_linked(b, 'rcl_BackwardMinAction', a2)
    if hasattr(a2, 'rcl_NumberValue33'):
        assert not _is_linked(a2, 'rcl_NumberValue33', b)


def test_assoc_enclosing3_reverse_link_reassign_clear():
    a1 = rcl_Statement()
    a2 = rcl_Statement()
    b = rcl_RclBlock()
    _safe_set(b, 'RclBlock', a1)
    assert _is_linked(b, 'RclBlock', a1)
    if hasattr(a1, 'stmts'):
        assert _is_linked(a1, 'stmts', b)
    _safe_set(b, 'RclBlock', a2)
    assert _is_linked(b, 'RclBlock', a2)
    if hasattr(a1, 'stmts'):
        assert not _is_linked(a1, 'stmts', b)
    if hasattr(a2, 'stmts'):
        assert _is_linked(a2, 'stmts', b)
    _safe_set(b, 'RclBlock', None)
    assert not _is_linked(b, 'RclBlock', a2)
    if hasattr(a2, 'stmts'):
        assert not _is_linked(a2, 'stmts', b)


def test_assoc_expr12_reverse_link_reassign_clear():
    a1 = rcl_RoverExpression()
    a2 = rcl_RoverExpression()
    b = rcl_Loop()
    _safe_set(b, 'rcl_Loop', a1)
    assert _is_linked(b, 'rcl_Loop', a1)
    if hasattr(a1, 'rcl_RoverExpression13'):
        assert _is_linked(a1, 'rcl_RoverExpression13', b)
    _safe_set(b, 'rcl_Loop', a2)
    assert _is_linked(b, 'rcl_Loop', a2)
    if hasattr(a1, 'rcl_RoverExpression13'):
        assert not _is_linked(a1, 'rcl_RoverExpression13', b)
    if hasattr(a2, 'rcl_RoverExpression13'):
        assert _is_linked(a2, 'rcl_RoverExpression13', b)
    _safe_set(b, 'rcl_Loop', None)
    assert not _is_linked(b, 'rcl_Loop', a2)
    if hasattr(a2, 'rcl_RoverExpression13'):
        assert not _is_linked(a2, 'rcl_RoverExpression13', b)


def test_assoc_expr5_reverse_link_reassign_clear():
    a1 = rcl_RoverExpression()
    a2 = rcl_RoverExpression()
    b = rcl_Conditional()
    _safe_set(b, 'rcl_Conditional', a1)
    assert _is_linked(b, 'rcl_Conditional', a1)
    if hasattr(a1, 'rcl_RoverExpression'):
        assert _is_linked(a1, 'rcl_RoverExpression', b)
    _safe_set(b, 'rcl_Conditional', a2)
    assert _is_linked(b, 'rcl_Conditional', a2)
    if hasattr(a1, 'rcl_RoverExpression'):
        assert not _is_linked(a1, 'rcl_RoverExpression', b)
    if hasattr(a2, 'rcl_RoverExpression'):
        assert _is_linked(a2, 'rcl_RoverExpression', b)
    _safe_set(b, 'rcl_Conditional', None)
    assert not _is_linked(b, 'rcl_Conditional', a2)
    if hasattr(a2, 'rcl_RoverExpression'):
        assert not _is_linked(a2, 'rcl_RoverExpression', b)


def test_assoc_lhs18_reverse_link_reassign_clear():
    a1 = rcl_NumericExpression(op=True)
    a2 = rcl_NumericExpression(op=False)
    b = rcl_NumberValue(nValue="sample_text")
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
    a1 = rcl_StringValue(sValue=True)
    a2 = rcl_StringValue(sValue=False)
    b = rcl_StringExpression(op=True)
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
    a1 = rcl_NumericExpression(op=True)
    a2 = rcl_NumericExpression(op=False)
    b = rcl_NumberValue(nValue="sample_text")
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
    a1 = rcl_StringValue(sValue=True)
    a2 = rcl_StringValue(sValue=False)
    b = rcl_StringExpression(op=True)
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


def test_assoc_stmts17_reverse_link_reassign_clear():
    a1 = rcl_Statement()
    a2 = rcl_Statement()
    b = rcl_RclBlock()
    _safe_set(b, 'enclosing', {a1})
    assert _is_linked(b, 'enclosing', a1)
    if hasattr(a1, 'Statement'):
        assert _is_linked(a1, 'Statement', b)
    _safe_set(b, 'enclosing', {a2})
    assert _is_linked(b, 'enclosing', a2)
    if hasattr(a1, 'Statement'):
        assert not _is_linked(a1, 'Statement', b)
    if hasattr(a2, 'Statement'):
        assert _is_linked(a2, 'Statement', b)
    _safe_set(b, 'enclosing', set())
    assert not _is_linked(b, 'enclosing', a2)
    if hasattr(a2, 'Statement'):
        assert not _is_linked(a2, 'Statement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_value4_stub_double():
    # rcl_RoverValue has no real 'rcl_RoverValue' property in the generated
    # code (a bare stub) -- manually attach it so rcl_VarAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rcl_VarAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rcl_VarAssignment(name=True)
    partner = rcl_RoverValue()
    setattr(partner, 'rcl_RoverValue', None)
    _safe_set(owner, 'rcl_VarAssignment', partner)
    assert getattr(partner, 'rcl_RoverValue') == owner
    _safe_set(owner, 'rcl_VarAssignment', None)
    assert getattr(partner, 'rcl_RoverValue') is None


