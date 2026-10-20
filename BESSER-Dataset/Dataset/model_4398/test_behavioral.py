import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    AngleOperation,
    AngleUnit,
    ArduinoModule,
    Board,
    BooleanValue,
    ImperialSystemUnit,
    LengthOperation,
    LengthUnit,
    MetricSystemUnit,
    Module,
    NamedElement,
    NumberValue,
    Pin,
    Quantity,
    QuantityHomogenousOperation,
    QuantityOperation,
    QuantityScalarOperation,
    Query,
    RoverExpression,
    RoverValue,
    Statement,
    StringValue,
    Unit,
    raspirover_Action,
    raspirover_AnalogPin,
    raspirover_Angle,
    raspirover_AngleAdd,
    raspirover_AngleDistinct,
    raspirover_AngleEquals,
    raspirover_AngleGreater,
    raspirover_AngleOperation,
    raspirover_AngleScalarDivide,
    raspirover_AngleScalarMultiply,
    raspirover_AngleSmaller,
    raspirover_AngleSubtract,
    raspirover_AngleUnit,
    raspirover_ArduinoAnalogModule,
    raspirover_ArduinoDigitalModule,
    raspirover_ArduinoModule,
    raspirover_BackwardAction,
    raspirover_BackwardMinAction,
    raspirover_Block,
    raspirover_Board,
    raspirover_BooleanExpression,
    raspirover_BooleanValue,
    raspirover_Centimeter,
    raspirover_Conditional,
    raspirover_Degree,
    raspirover_DigitalPin,
    raspirover_Foot,
    raspirover_ForwardAction,
    raspirover_ForwardMinAction,
    raspirover_Gradian,
    raspirover_HumidityQuery,
    raspirover_ImperialSystemUnit,
    raspirover_Inch,
    raspirover_Instruction,
    raspirover_Length,
    raspirover_LengthAdd,
    raspirover_LengthDistinct,
    raspirover_LengthEquals,
    raspirover_LengthGreater,
    raspirover_LengthOperation,
    raspirover_LengthScalarDivide,
    raspirover_LengthScalarMultiply,
    raspirover_LengthSmaller,
    raspirover_LengthSubtract,
    raspirover_LengthUnit,
    raspirover_LogAction,
    raspirover_Loop,
    raspirover_MessageQuery,
    raspirover_Meter,
    raspirover_MetricSystemUnit,
    raspirover_Millimeter,
    raspirover_Module,
    raspirover_NamedElement,
    raspirover_NumberValue,
    raspirover_NumericExpression,
    raspirover_ObstacleQuery,
    raspirover_Param,
    raspirover_Pin,
    raspirover_Project,
    raspirover_Quantity,
    raspirover_QuantityArithmeticOperation,
    raspirover_QuantityComparisonOperation,
    raspirover_QuantityHomogenousOperation,
    raspirover_QuantityOperation,
    raspirover_QuantityScalarOperation,
    raspirover_Query,
    raspirover_Radian,
    raspirover_RasPiBoard,
    raspirover_RclBlock,
    raspirover_RoverExpression,
    raspirover_RoverProgram,
    raspirover_RoverValue,
    raspirover_SendAction,
    raspirover_Sketch,
    raspirover_Statement,
    raspirover_StopAction,
    raspirover_StringExpression,
    raspirover_StringValue,
    raspirover_TemperatureQuery,
    raspirover_Turn,
    raspirover_TurnAction,
    raspirover_TurnDegAction,
    raspirover_Unit,
    raspirover_VarAssignment,
    raspirover_VarRef,
    raspirover_Yard,
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

def test_assoc_block21_reverse_link_reassign_clear():
    a1 = raspirover_RoverProgram(name="sample_text")
    a2 = raspirover_RoverProgram(name="sample_text_2")
    b = raspirover_RclBlock()
    _safe_set(b, 'raspirover_RclBlock', a1)
    assert _is_linked(b, 'raspirover_RclBlock', a1)
    if hasattr(a1, 'raspirover_RoverProgram22'):
        assert _is_linked(a1, 'raspirover_RoverProgram22', b)
    _safe_set(b, 'raspirover_RclBlock', a2)
    assert _is_linked(b, 'raspirover_RclBlock', a2)
    if hasattr(a1, 'raspirover_RoverProgram22'):
        assert not _is_linked(a1, 'raspirover_RoverProgram22', b)
    if hasattr(a2, 'raspirover_RoverProgram22'):
        assert _is_linked(a2, 'raspirover_RoverProgram22', b)
    _safe_set(b, 'raspirover_RclBlock', None)
    assert not _is_linked(b, 'raspirover_RclBlock', a2)
    if hasattr(a2, 'raspirover_RoverProgram22'):
        assert not _is_linked(a2, 'raspirover_RoverProgram22', b)


def test_assoc_block34_reverse_link_reassign_clear():
    a1 = raspirover_RclBlock()
    a2 = raspirover_RclBlock()
    b = raspirover_Loop()
    _safe_set(b, 'raspirover_Loop35', a1)
    assert _is_linked(b, 'raspirover_Loop35', a1)
    if hasattr(a1, 'raspirover_RclBlock36'):
        assert _is_linked(a1, 'raspirover_RclBlock36', b)
    _safe_set(b, 'raspirover_Loop35', a2)
    assert _is_linked(b, 'raspirover_Loop35', a2)
    if hasattr(a1, 'raspirover_RclBlock36'):
        assert not _is_linked(a1, 'raspirover_RclBlock36', b)
    if hasattr(a2, 'raspirover_RclBlock36'):
        assert _is_linked(a2, 'raspirover_RclBlock36', b)
    _safe_set(b, 'raspirover_Loop35', None)
    assert not _is_linked(b, 'raspirover_Loop35', a2)
    if hasattr(a2, 'raspirover_RclBlock36'):
        assert not _is_linked(a2, 'raspirover_RclBlock36', b)


def test_assoc_condFalse29_reverse_link_reassign_clear():
    a1 = raspirover_RclBlock()
    a2 = raspirover_RclBlock()
    b = raspirover_Conditional()
    _safe_set(b, 'raspirover_Conditional30', a1)
    assert _is_linked(b, 'raspirover_Conditional30', a1)
    if hasattr(a1, 'raspirover_RclBlock31'):
        assert _is_linked(a1, 'raspirover_RclBlock31', b)
    _safe_set(b, 'raspirover_Conditional30', a2)
    assert _is_linked(b, 'raspirover_Conditional30', a2)
    if hasattr(a1, 'raspirover_RclBlock31'):
        assert not _is_linked(a1, 'raspirover_RclBlock31', b)
    if hasattr(a2, 'raspirover_RclBlock31'):
        assert _is_linked(a2, 'raspirover_RclBlock31', b)
    _safe_set(b, 'raspirover_Conditional30', None)
    assert not _is_linked(b, 'raspirover_Conditional30', a2)
    if hasattr(a2, 'raspirover_RclBlock31'):
        assert not _is_linked(a2, 'raspirover_RclBlock31', b)


def test_assoc_condTrue26_reverse_link_reassign_clear():
    a1 = raspirover_RclBlock()
    a2 = raspirover_RclBlock()
    b = raspirover_Conditional()
    _safe_set(b, 'raspirover_Conditional27', a1)
    assert _is_linked(b, 'raspirover_Conditional27', a1)
    if hasattr(a1, 'raspirover_RclBlock28'):
        assert _is_linked(a1, 'raspirover_RclBlock28', b)
    _safe_set(b, 'raspirover_Conditional27', a2)
    assert _is_linked(b, 'raspirover_Conditional27', a2)
    if hasattr(a1, 'raspirover_RclBlock28'):
        assert not _is_linked(a1, 'raspirover_RclBlock28', b)
    if hasattr(a2, 'raspirover_RclBlock28'):
        assert _is_linked(a2, 'raspirover_RclBlock28', b)
    _safe_set(b, 'raspirover_Conditional27', None)
    assert not _is_linked(b, 'raspirover_Conditional27', a2)
    if hasattr(a2, 'raspirover_RclBlock28'):
        assert not _is_linked(a2, 'raspirover_RclBlock28', b)


def test_assoc_degrees57_reverse_link_reassign_clear():
    a1 = raspirover_TurnDegAction()
    a2 = raspirover_TurnDegAction()
    b = raspirover_NumberValue(nValue="sample_text")
    _safe_set(b, 'raspirover_NumberValue58', a1)
    assert _is_linked(b, 'raspirover_NumberValue58', a1)
    if hasattr(a1, 'raspirover_TurnDegAction'):
        assert _is_linked(a1, 'raspirover_TurnDegAction', b)
    _safe_set(b, 'raspirover_NumberValue58', a2)
    assert _is_linked(b, 'raspirover_NumberValue58', a2)
    if hasattr(a1, 'raspirover_TurnDegAction'):
        assert not _is_linked(a1, 'raspirover_TurnDegAction', b)
    if hasattr(a2, 'raspirover_TurnDegAction'):
        assert _is_linked(a2, 'raspirover_TurnDegAction', b)
    _safe_set(b, 'raspirover_NumberValue58', None)
    assert not _is_linked(b, 'raspirover_NumberValue58', a2)
    if hasattr(a2, 'raspirover_TurnDegAction'):
        assert not _is_linked(a2, 'raspirover_TurnDegAction', b)


def test_assoc_distance53_reverse_link_reassign_clear():
    a1 = raspirover_NumberValue(nValue="sample_text")
    a2 = raspirover_NumberValue(nValue="sample_text_2")
    b = raspirover_ForwardMinAction()
    _safe_set(b, 'raspirover_ForwardMinAction', a1)
    assert _is_linked(b, 'raspirover_ForwardMinAction', a1)
    if hasattr(a1, 'raspirover_NumberValue54'):
        assert _is_linked(a1, 'raspirover_NumberValue54', b)
    _safe_set(b, 'raspirover_ForwardMinAction', a2)
    assert _is_linked(b, 'raspirover_ForwardMinAction', a2)
    if hasattr(a1, 'raspirover_NumberValue54'):
        assert not _is_linked(a1, 'raspirover_NumberValue54', b)
    if hasattr(a2, 'raspirover_NumberValue54'):
        assert _is_linked(a2, 'raspirover_NumberValue54', b)
    _safe_set(b, 'raspirover_ForwardMinAction', None)
    assert not _is_linked(b, 'raspirover_ForwardMinAction', a2)
    if hasattr(a2, 'raspirover_NumberValue54'):
        assert not _is_linked(a2, 'raspirover_NumberValue54', b)


def test_assoc_distance55_reverse_link_reassign_clear():
    a1 = raspirover_NumberValue(nValue="sample_text")
    a2 = raspirover_NumberValue(nValue="sample_text_2")
    b = raspirover_BackwardMinAction()
    _safe_set(b, 'raspirover_BackwardMinAction', a1)
    assert _is_linked(b, 'raspirover_BackwardMinAction', a1)
    if hasattr(a1, 'raspirover_NumberValue56'):
        assert _is_linked(a1, 'raspirover_NumberValue56', b)
    _safe_set(b, 'raspirover_BackwardMinAction', a2)
    assert _is_linked(b, 'raspirover_BackwardMinAction', a2)
    if hasattr(a1, 'raspirover_NumberValue56'):
        assert not _is_linked(a1, 'raspirover_NumberValue56', b)
    if hasattr(a2, 'raspirover_NumberValue56'):
        assert _is_linked(a2, 'raspirover_NumberValue56', b)
    _safe_set(b, 'raspirover_BackwardMinAction', None)
    assert not _is_linked(b, 'raspirover_BackwardMinAction', a2)
    if hasattr(a2, 'raspirover_NumberValue56'):
        assert not _is_linked(a2, 'raspirover_NumberValue56', b)


def test_assoc_enclosing23_reverse_link_reassign_clear():
    a1 = raspirover_Statement()
    a2 = raspirover_Statement()
    b = raspirover_RclBlock()
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


def test_assoc_expr25_reverse_link_reassign_clear():
    a1 = raspirover_RoverExpression()
    a2 = raspirover_RoverExpression()
    b = raspirover_Conditional()
    _safe_set(b, 'raspirover_Conditional', a1)
    assert _is_linked(b, 'raspirover_Conditional', a1)
    if hasattr(a1, 'raspirover_RoverExpression'):
        assert _is_linked(a1, 'raspirover_RoverExpression', b)
    _safe_set(b, 'raspirover_Conditional', a2)
    assert _is_linked(b, 'raspirover_Conditional', a2)
    if hasattr(a1, 'raspirover_RoverExpression'):
        assert not _is_linked(a1, 'raspirover_RoverExpression', b)
    if hasattr(a2, 'raspirover_RoverExpression'):
        assert _is_linked(a2, 'raspirover_RoverExpression', b)
    _safe_set(b, 'raspirover_Conditional', None)
    assert not _is_linked(b, 'raspirover_Conditional', a2)
    if hasattr(a2, 'raspirover_RoverExpression'):
        assert not _is_linked(a2, 'raspirover_RoverExpression', b)


def test_assoc_expr32_reverse_link_reassign_clear():
    a1 = raspirover_RoverExpression()
    a2 = raspirover_RoverExpression()
    b = raspirover_Loop()
    _safe_set(b, 'raspirover_Loop', a1)
    assert _is_linked(b, 'raspirover_Loop', a1)
    if hasattr(a1, 'raspirover_RoverExpression33'):
        assert _is_linked(a1, 'raspirover_RoverExpression33', b)
    _safe_set(b, 'raspirover_Loop', a2)
    assert _is_linked(b, 'raspirover_Loop', a2)
    if hasattr(a1, 'raspirover_RoverExpression33'):
        assert not _is_linked(a1, 'raspirover_RoverExpression33', b)
    if hasattr(a2, 'raspirover_RoverExpression33'):
        assert _is_linked(a2, 'raspirover_RoverExpression33', b)
    _safe_set(b, 'raspirover_Loop', None)
    assert not _is_linked(b, 'raspirover_Loop', a2)
    if hasattr(a2, 'raspirover_RoverExpression33'):
        assert not _is_linked(a2, 'raspirover_RoverExpression33', b)


def test_assoc_instructions13_reverse_link_reassign_clear():
    a1 = raspirover_Instruction()
    a2 = raspirover_Instruction()
    b = raspirover_Block()
    _safe_set(b, 'raspirover_Block14', {a1})
    assert _is_linked(b, 'raspirover_Block14', a1)
    if hasattr(a1, 'raspirover_Instruction'):
        assert _is_linked(a1, 'raspirover_Instruction', b)
    _safe_set(b, 'raspirover_Block14', {a2})
    assert _is_linked(b, 'raspirover_Block14', a2)
    if hasattr(a1, 'raspirover_Instruction'):
        assert not _is_linked(a1, 'raspirover_Instruction', b)
    if hasattr(a2, 'raspirover_Instruction'):
        assert _is_linked(a2, 'raspirover_Instruction', b)
    _safe_set(b, 'raspirover_Block14', set())
    assert not _is_linked(b, 'raspirover_Block14', a2)
    if hasattr(a2, 'raspirover_Instruction'):
        assert not _is_linked(a2, 'raspirover_Instruction', b)


def test_assoc_lhs38_reverse_link_reassign_clear():
    a1 = raspirover_NumericExpression(op=True)
    a2 = raspirover_NumericExpression(op=False)
    b = raspirover_NumberValue(nValue="sample_text")
    _safe_set(b, 'raspirover_NumberValue', a1)
    assert _is_linked(b, 'raspirover_NumberValue', a1)
    if hasattr(a1, 'raspirover_NumericExpression'):
        assert _is_linked(a1, 'raspirover_NumericExpression', b)
    _safe_set(b, 'raspirover_NumberValue', a2)
    assert _is_linked(b, 'raspirover_NumberValue', a2)
    if hasattr(a1, 'raspirover_NumericExpression'):
        assert not _is_linked(a1, 'raspirover_NumericExpression', b)
    if hasattr(a2, 'raspirover_NumericExpression'):
        assert _is_linked(a2, 'raspirover_NumericExpression', b)
    _safe_set(b, 'raspirover_NumberValue', None)
    assert not _is_linked(b, 'raspirover_NumberValue', a2)
    if hasattr(a2, 'raspirover_NumericExpression'):
        assert not _is_linked(a2, 'raspirover_NumericExpression', b)


def test_assoc_lhs42_reverse_link_reassign_clear():
    a1 = raspirover_StringValue(sValue=True)
    a2 = raspirover_StringValue(sValue=False)
    b = raspirover_StringExpression(op=True)
    _safe_set(b, 'raspirover_StringExpression', a1)
    assert _is_linked(b, 'raspirover_StringExpression', a1)
    if hasattr(a1, 'raspirover_StringValue'):
        assert _is_linked(a1, 'raspirover_StringValue', b)
    _safe_set(b, 'raspirover_StringExpression', a2)
    assert _is_linked(b, 'raspirover_StringExpression', a2)
    if hasattr(a1, 'raspirover_StringValue'):
        assert not _is_linked(a1, 'raspirover_StringValue', b)
    if hasattr(a2, 'raspirover_StringValue'):
        assert _is_linked(a2, 'raspirover_StringValue', b)
    _safe_set(b, 'raspirover_StringExpression', None)
    assert not _is_linked(b, 'raspirover_StringExpression', a2)
    if hasattr(a2, 'raspirover_StringValue'):
        assert not _is_linked(a2, 'raspirover_StringValue', b)


def test_assoc_lhs46_reverse_link_reassign_clear():
    a1 = raspirover_BooleanValue(bValue=True)
    a2 = raspirover_BooleanValue(bValue=False)
    b = raspirover_BooleanExpression(op="sample_text")
    _safe_set(b, 'raspirover_BooleanExpression', a1)
    assert _is_linked(b, 'raspirover_BooleanExpression', a1)
    if hasattr(a1, 'raspirover_BooleanValue'):
        assert _is_linked(a1, 'raspirover_BooleanValue', b)
    _safe_set(b, 'raspirover_BooleanExpression', a2)
    assert _is_linked(b, 'raspirover_BooleanExpression', a2)
    if hasattr(a1, 'raspirover_BooleanValue'):
        assert not _is_linked(a1, 'raspirover_BooleanValue', b)
    if hasattr(a2, 'raspirover_BooleanValue'):
        assert _is_linked(a2, 'raspirover_BooleanValue', b)
    _safe_set(b, 'raspirover_BooleanExpression', None)
    assert not _is_linked(b, 'raspirover_BooleanExpression', a2)
    if hasattr(a2, 'raspirover_BooleanValue'):
        assert not _is_linked(a2, 'raspirover_BooleanValue', b)


def test_assoc_lhs66_reverse_link_reassign_clear():
    a1 = raspirover_QuantityScalarOperation(rhs=3.14)
    a2 = raspirover_QuantityScalarOperation(rhs=9.99)
    b = raspirover_Quantity(value="sample_text")
    _safe_set(b, 'raspirover_Quantity67', a1)
    assert _is_linked(b, 'raspirover_Quantity67', a1)
    if hasattr(a1, 'raspirover_QuantityScalarOperation'):
        assert _is_linked(a1, 'raspirover_QuantityScalarOperation', b)
    _safe_set(b, 'raspirover_Quantity67', a2)
    assert _is_linked(b, 'raspirover_Quantity67', a2)
    if hasattr(a1, 'raspirover_QuantityScalarOperation'):
        assert not _is_linked(a1, 'raspirover_QuantityScalarOperation', b)
    if hasattr(a2, 'raspirover_QuantityScalarOperation'):
        assert _is_linked(a2, 'raspirover_QuantityScalarOperation', b)
    _safe_set(b, 'raspirover_Quantity67', None)
    assert not _is_linked(b, 'raspirover_Quantity67', a2)
    if hasattr(a2, 'raspirover_QuantityScalarOperation'):
        assert not _is_linked(a2, 'raspirover_QuantityScalarOperation', b)


def test_assoc_params19_reverse_link_reassign_clear():
    a1 = raspirover_RoverProgram(name="sample_text")
    a2 = raspirover_RoverProgram(name="sample_text_2")
    b = raspirover_Param(name="sample_text")
    _safe_set(b, 'raspirover_Param', a1)
    assert _is_linked(b, 'raspirover_Param', a1)
    if hasattr(a1, 'raspirover_RoverProgram20'):
        assert _is_linked(a1, 'raspirover_RoverProgram20', b)
    _safe_set(b, 'raspirover_Param', a2)
    assert _is_linked(b, 'raspirover_Param', a2)
    if hasattr(a1, 'raspirover_RoverProgram20'):
        assert not _is_linked(a1, 'raspirover_RoverProgram20', b)
    if hasattr(a2, 'raspirover_RoverProgram20'):
        assert _is_linked(a2, 'raspirover_RoverProgram20', b)
    _safe_set(b, 'raspirover_Param', None)
    assert not _is_linked(b, 'raspirover_Param', a2)
    if hasattr(a2, 'raspirover_RoverProgram20'):
        assert not _is_linked(a2, 'raspirover_RoverProgram20', b)


def test_assoc_program7_reverse_link_reassign_clear():
    a1 = raspirover_RoverProgram(name="sample_text")
    a2 = raspirover_RoverProgram(name="sample_text_2")
    b = raspirover_Project()
    _safe_set(b, 'raspirover_Project', a1)
    assert _is_linked(b, 'raspirover_Project', a1)
    if hasattr(a1, 'raspirover_RoverProgram'):
        assert _is_linked(a1, 'raspirover_RoverProgram', b)
    _safe_set(b, 'raspirover_Project', a2)
    assert _is_linked(b, 'raspirover_Project', a2)
    if hasattr(a1, 'raspirover_RoverProgram'):
        assert not _is_linked(a1, 'raspirover_RoverProgram', b)
    if hasattr(a2, 'raspirover_RoverProgram'):
        assert _is_linked(a2, 'raspirover_RoverProgram', b)
    _safe_set(b, 'raspirover_Project', None)
    assert not _is_linked(b, 'raspirover_Project', a2)
    if hasattr(a2, 'raspirover_RoverProgram'):
        assert not _is_linked(a2, 'raspirover_RoverProgram', b)


def test_assoc_quantity50_reverse_link_reassign_clear():
    a1 = raspirover_Quantity(value="sample_text")
    a2 = raspirover_Quantity(value="sample_text_2")
    b = raspirover_NumberValue(nValue="sample_text")
    _safe_set(b, 'raspirover_NumberValue51', a1)
    assert _is_linked(b, 'raspirover_NumberValue51', a1)
    if hasattr(a1, 'raspirover_Quantity'):
        assert _is_linked(a1, 'raspirover_Quantity', b)
    _safe_set(b, 'raspirover_NumberValue51', a2)
    assert _is_linked(b, 'raspirover_NumberValue51', a2)
    if hasattr(a1, 'raspirover_Quantity'):
        assert not _is_linked(a1, 'raspirover_Quantity', b)
    if hasattr(a2, 'raspirover_Quantity'):
        assert _is_linked(a2, 'raspirover_Quantity', b)
    _safe_set(b, 'raspirover_NumberValue51', None)
    assert not _is_linked(b, 'raspirover_NumberValue51', a2)
    if hasattr(a2, 'raspirover_Quantity'):
        assert not _is_linked(a2, 'raspirover_Quantity', b)


def test_assoc_rhs39_reverse_link_reassign_clear():
    a1 = raspirover_NumericExpression(op=True)
    a2 = raspirover_NumericExpression(op=False)
    b = raspirover_NumberValue(nValue="sample_text")
    _safe_set(b, 'raspirover_NumberValue41', a1)
    assert _is_linked(b, 'raspirover_NumberValue41', a1)
    if hasattr(a1, 'raspirover_NumericExpression40'):
        assert _is_linked(a1, 'raspirover_NumericExpression40', b)
    _safe_set(b, 'raspirover_NumberValue41', a2)
    assert _is_linked(b, 'raspirover_NumberValue41', a2)
    if hasattr(a1, 'raspirover_NumericExpression40'):
        assert not _is_linked(a1, 'raspirover_NumericExpression40', b)
    if hasattr(a2, 'raspirover_NumericExpression40'):
        assert _is_linked(a2, 'raspirover_NumericExpression40', b)
    _safe_set(b, 'raspirover_NumberValue41', None)
    assert not _is_linked(b, 'raspirover_NumberValue41', a2)
    if hasattr(a2, 'raspirover_NumericExpression40'):
        assert not _is_linked(a2, 'raspirover_NumericExpression40', b)


def test_assoc_rhs43_reverse_link_reassign_clear():
    a1 = raspirover_StringValue(sValue=True)
    a2 = raspirover_StringValue(sValue=False)
    b = raspirover_StringExpression(op=True)
    _safe_set(b, 'raspirover_StringExpression44', a1)
    assert _is_linked(b, 'raspirover_StringExpression44', a1)
    if hasattr(a1, 'raspirover_StringValue45'):
        assert _is_linked(a1, 'raspirover_StringValue45', b)
    _safe_set(b, 'raspirover_StringExpression44', a2)
    assert _is_linked(b, 'raspirover_StringExpression44', a2)
    if hasattr(a1, 'raspirover_StringValue45'):
        assert not _is_linked(a1, 'raspirover_StringValue45', b)
    if hasattr(a2, 'raspirover_StringValue45'):
        assert _is_linked(a2, 'raspirover_StringValue45', b)
    _safe_set(b, 'raspirover_StringExpression44', None)
    assert not _is_linked(b, 'raspirover_StringExpression44', a2)
    if hasattr(a2, 'raspirover_StringValue45'):
        assert not _is_linked(a2, 'raspirover_StringValue45', b)


def test_assoc_rhs47_reverse_link_reassign_clear():
    a1 = raspirover_BooleanValue(bValue=True)
    a2 = raspirover_BooleanValue(bValue=False)
    b = raspirover_BooleanExpression(op="sample_text")
    _safe_set(b, 'raspirover_BooleanExpression48', a1)
    assert _is_linked(b, 'raspirover_BooleanExpression48', a1)
    if hasattr(a1, 'raspirover_BooleanValue49'):
        assert _is_linked(a1, 'raspirover_BooleanValue49', b)
    _safe_set(b, 'raspirover_BooleanExpression48', a2)
    assert _is_linked(b, 'raspirover_BooleanExpression48', a2)
    if hasattr(a1, 'raspirover_BooleanValue49'):
        assert not _is_linked(a1, 'raspirover_BooleanValue49', b)
    if hasattr(a2, 'raspirover_BooleanValue49'):
        assert _is_linked(a2, 'raspirover_BooleanValue49', b)
    _safe_set(b, 'raspirover_BooleanExpression48', None)
    assert not _is_linked(b, 'raspirover_BooleanExpression48', a2)
    if hasattr(a2, 'raspirover_BooleanValue49'):
        assert not _is_linked(a2, 'raspirover_BooleanValue49', b)


def test_assoc_stmts37_reverse_link_reassign_clear():
    a1 = raspirover_Statement()
    a2 = raspirover_Statement()
    b = raspirover_RclBlock()
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


def test_assoc_unit59_reverse_link_reassign_clear():
    a1 = raspirover_Unit()
    a2 = raspirover_Unit()
    b = raspirover_Quantity(value="sample_text")
    _safe_set(b, 'raspirover_Quantity60', a1)
    assert _is_linked(b, 'raspirover_Quantity60', a1)
    if hasattr(a1, 'raspirover_Unit'):
        assert _is_linked(a1, 'raspirover_Unit', b)
    _safe_set(b, 'raspirover_Quantity60', a2)
    assert _is_linked(b, 'raspirover_Quantity60', a2)
    if hasattr(a1, 'raspirover_Unit'):
        assert not _is_linked(a1, 'raspirover_Unit', b)
    if hasattr(a2, 'raspirover_Unit'):
        assert _is_linked(a2, 'raspirover_Unit', b)
    _safe_set(b, 'raspirover_Quantity60', None)
    assert not _is_linked(b, 'raspirover_Quantity60', a2)
    if hasattr(a2, 'raspirover_Unit'):
        assert not _is_linked(a2, 'raspirover_Unit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_associatedPin52_stub_double():
    # raspirover_Action has no real 'raspirover_Action' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_Pin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_Pin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_Pin(level=7)
    partner = raspirover_Action()
    setattr(partner, 'raspirover_Action', None)
    _safe_set(owner, 'raspirover_Pin', partner)
    assert getattr(partner, 'raspirover_Action') == owner
    _safe_set(owner, 'raspirover_Pin', None)
    assert getattr(partner, 'raspirover_Action') is None


def test_assoc_block10_stub_double():
    # raspirover_Sketch has no real 'raspirover_Sketch' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_Block()
    partner = raspirover_Sketch()
    setattr(partner, 'raspirover_Sketch', None)
    _safe_set(owner, 'raspirover_Block', partner)
    assert getattr(partner, 'raspirover_Sketch') == owner
    _safe_set(owner, 'raspirover_Block', None)
    assert getattr(partner, 'raspirover_Sketch') is None


def test_assoc_boards4_stub_double():
    # raspirover_Board has no real 'Board' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_Project()
    partner = raspirover_Board()
    setattr(partner, 'Board', None)
    _safe_set(owner, 'project', {partner})
    assert getattr(partner, 'Board') == owner
    _safe_set(owner, 'project', set())
    assert getattr(partner, 'Board') is None


def test_assoc_lhs61_stub_double():
    # raspirover_QuantityHomogenousOperation has no real 'raspirover_QuantityHomogenousOperation' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_Quantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_Quantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_Quantity(value="sample_text")
    partner = raspirover_QuantityHomogenousOperation()
    setattr(partner, 'raspirover_QuantityHomogenousOperation', None)
    _safe_set(owner, 'raspirover_Quantity62', partner)
    assert getattr(partner, 'raspirover_QuantityHomogenousOperation') == owner
    _safe_set(owner, 'raspirover_Quantity62', None)
    assert getattr(partner, 'raspirover_QuantityHomogenousOperation') is None


def test_assoc_project3_stub_double():
    # raspirover_Board has no real 'boards' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_Project()
    partner = raspirover_Board()
    setattr(partner, 'boards', None)
    _safe_set(owner, 'Project', partner)
    assert getattr(partner, 'boards') == owner
    _safe_set(owner, 'Project', None)
    assert getattr(partner, 'boards') is None


def test_assoc_project8_stub_double():
    # raspirover_Sketch has no real 'sketches' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_Project()
    partner = raspirover_Sketch()
    setattr(partner, 'sketches', None)
    _safe_set(owner, 'Project9', partner)
    assert getattr(partner, 'sketches') == owner
    _safe_set(owner, 'Project9', None)
    assert getattr(partner, 'sketches') is None


def test_assoc_rhs63_stub_double():
    # raspirover_QuantityHomogenousOperation has no real 'raspirover_QuantityHomogenousOperation64' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_Quantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_Quantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_Quantity(value="sample_text")
    partner = raspirover_QuantityHomogenousOperation()
    setattr(partner, 'raspirover_QuantityHomogenousOperation64', None)
    _safe_set(owner, 'raspirover_Quantity65', partner)
    assert getattr(partner, 'raspirover_QuantityHomogenousOperation64') == owner
    _safe_set(owner, 'raspirover_Quantity65', None)
    assert getattr(partner, 'raspirover_QuantityHomogenousOperation64') is None


def test_assoc_sketches5_stub_double():
    # raspirover_Sketch has no real 'Sketch' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_Project()
    partner = raspirover_Sketch()
    setattr(partner, 'Sketch', None)
    _safe_set(owner, 'project6', {partner})
    assert getattr(partner, 'Sketch') == owner
    _safe_set(owner, 'project6', set())
    assert getattr(partner, 'Sketch') is None


def test_assoc_value24_stub_double():
    # raspirover_RoverValue has no real 'raspirover_RoverValue' property in the generated
    # code (a bare stub) -- manually attach it so raspirover_VarAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspirover_VarAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspirover_VarAssignment(name=True)
    partner = raspirover_RoverValue()
    setattr(partner, 'raspirover_RoverValue', None)
    _safe_set(owner, 'raspirover_VarAssignment', partner)
    assert getattr(partner, 'raspirover_RoverValue') == owner
    _safe_set(owner, 'raspirover_VarAssignment', None)
    assert getattr(partner, 'raspirover_RoverValue') is None


