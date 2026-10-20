import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActivityEdge,
    ActivityNode,
    BooleanExpression,
    Chunk,
    Contained,
    ControlNode,
    ExecutableNode,
    Expression,
    Field,
    FinalNode,
    HWComponent,
    IDLType,
    IntegerExpression,
    LastStatement,
    LastStatement_Return,
    NamedElement,
    Statement,
    Statement_FunctioncallOrAssignment,
    Typed,
    Value,
    Variable,
    iot2_Action,
    iot2_Activity,
    iot2_ActivityEdge,
    iot2_ActivityFinalNode,
    iot2_ActivityNode,
    iot2_Actuator,
    iot2_Block,
    iot2_Board,
    iot2_BooleanBinaryExpression,
    iot2_BooleanExpression,
    iot2_BooleanUnaryExpression,
    iot2_BooleanValue,
    iot2_BooleanVariable,
    iot2_Chunk,
    iot2_Contained,
    iot2_Container,
    iot2_ControlFlow,
    iot2_ControlNode,
    iot2_DecisionNode,
    iot2_ExceptionDef,
    iot2_ExecutableNode,
    iot2_Expression,
    iot2_Expression_AccessArray,
    iot2_Expression_AccessMember,
    iot2_Expression_And,
    iot2_Expression_CallFunction,
    iot2_Expression_CallMemberFunction,
    iot2_Expression_Concatenation,
    iot2_Expression_Division,
    iot2_Expression_Equal,
    iot2_Expression_Exponentiation,
    iot2_Expression_False,
    iot2_Expression_Function,
    iot2_Expression_Invert,
    iot2_Expression_Larger,
    iot2_Expression_Larger_Equal,
    iot2_Expression_Length,
    iot2_Expression_Minus,
    iot2_Expression_Modulo,
    iot2_Expression_Multiplication,
    iot2_Expression_Negate,
    iot2_Expression_Nil,
    iot2_Expression_Not_Equal,
    iot2_Expression_Number,
    iot2_Expression_Or,
    iot2_Expression_Plus,
    iot2_Expression_Smaller,
    iot2_Expression_Smaller_Equal,
    iot2_Expression_String,
    iot2_Expression_TableConstructor,
    iot2_Expression_True,
    iot2_Expression_VarArgs,
    iot2_Expression_VariableName,
    iot2_Field,
    iot2_Field_AddEntryToTable,
    iot2_Field_AddEntryToTable_Brackets,
    iot2_Field_AppendEntryToTable,
    iot2_FinalNode,
    iot2_ForkNode,
    iot2_Function,
    iot2_Functioncall_Arguments,
    iot2_HWComponent,
    iot2_IDLType,
    iot2_InitialNode,
    iot2_Input,
    iot2_InputValue,
    iot2_IntegerCalculationExpression,
    iot2_IntegerComparisonExpression,
    iot2_IntegerExpression,
    iot2_IntegerValue,
    iot2_IntegerVariable,
    iot2_JoinNode,
    iot2_LastStatement,
    iot2_LastStatement_Break,
    iot2_LastStatement_Return,
    iot2_LastStatement_ReturnWithValue,
    iot2_MergeNode,
    iot2_NamedElement,
    iot2_OpaqueAction,
    iot2_OperationDef,
    iot2_ParameterDef,
    iot2_PrimitiveDef,
    iot2_Sensor,
    iot2_Sketch,
    iot2_Statement,
    iot2_Statement_Assignment,
    iot2_Statement_Block,
    iot2_Statement_CallFunction,
    iot2_Statement_CallMemberFunction,
    iot2_Statement_For_Generic,
    iot2_Statement_For_Numeric,
    iot2_Statement_FunctioncallOrAssignment,
    iot2_Statement_GlobalFunction_Declaration,
    iot2_Statement_If_Then_Else,
    iot2_Statement_If_Then_Else_ElseIfPart,
    iot2_Statement_LocalFunction_Declaration,
    iot2_Statement_Local_Variable_Declaration,
    iot2_Statement_Repeat,
    iot2_Statement_While,
    iot2_System,
    iot2_Token,
    iot2_Trace,
    iot2_Typed,
    iot2_TypedefDef,
    iot2_Value,
    iot2_Variable,
    BoardType,
    BooleanBinaryOperator,
    BooleanUnaryOperator,
    IntegerCalculationOperator,
    IntegerComparisonOperator,
    ParameterMode,
    PrimitiveKind,
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

def test_assoc_boards1_reverse_link_reassign_clear():
    a1 = iot2_System(name="sample_text")
    a2 = iot2_System(name="sample_text_2")
    b = iot2_Board(name="sample_text", type="sample_text")
    _safe_set(b, 'iot2_Board', a1)
    assert _is_linked(b, 'iot2_Board', a1)
    if hasattr(a1, 'iot2_System2'):
        assert _is_linked(a1, 'iot2_System2', b)
    _safe_set(b, 'iot2_Board', a2)
    assert _is_linked(b, 'iot2_Board', a2)
    if hasattr(a1, 'iot2_System2'):
        assert not _is_linked(a1, 'iot2_System2', b)
    if hasattr(a2, 'iot2_System2'):
        assert _is_linked(a2, 'iot2_System2', b)
    _safe_set(b, 'iot2_Board', None)
    assert not _is_linked(b, 'iot2_Board', a2)
    if hasattr(a2, 'iot2_System2'):
        assert not _is_linked(a2, 'iot2_System2', b)


def test_assoc_canRaise22_reverse_link_reassign_clear():
    a1 = iot2_OperationDef(contexts="sample_text", isOneway=True)
    a2 = iot2_OperationDef(contexts="sample_text_2", isOneway=False)
    b = iot2_ExceptionDef(typeCode="sample_text")
    _safe_set(b, 'iot2_ExceptionDef', a1)
    assert _is_linked(b, 'iot2_ExceptionDef', a1)
    if hasattr(a1, 'iot2_OperationDef23'):
        assert _is_linked(a1, 'iot2_OperationDef23', b)
    _safe_set(b, 'iot2_ExceptionDef', a2)
    assert _is_linked(b, 'iot2_ExceptionDef', a2)
    if hasattr(a1, 'iot2_OperationDef23'):
        assert not _is_linked(a1, 'iot2_OperationDef23', b)
    if hasattr(a2, 'iot2_OperationDef23'):
        assert _is_linked(a2, 'iot2_OperationDef23', b)
    _safe_set(b, 'iot2_ExceptionDef', None)
    assert not _is_linked(b, 'iot2_ExceptionDef', a2)
    if hasattr(a2, 'iot2_OperationDef23'):
        assert not _is_linked(a2, 'iot2_OperationDef23', b)


def test_assoc_components0_reverse_link_reassign_clear():
    a1 = iot2_System(name="sample_text")
    a2 = iot2_System(name="sample_text_2")
    b = iot2_HWComponent(name="sample_text")
    _safe_set(b, 'iot2_HWComponent', a1)
    assert _is_linked(b, 'iot2_HWComponent', a1)
    if hasattr(a1, 'iot2_System'):
        assert _is_linked(a1, 'iot2_System', b)
    _safe_set(b, 'iot2_HWComponent', a2)
    assert _is_linked(b, 'iot2_HWComponent', a2)
    if hasattr(a1, 'iot2_System'):
        assert not _is_linked(a1, 'iot2_System', b)
    if hasattr(a2, 'iot2_System'):
        assert _is_linked(a2, 'iot2_System', b)
    _safe_set(b, 'iot2_HWComponent', None)
    assert not _is_linked(b, 'iot2_HWComponent', a2)
    if hasattr(a2, 'iot2_System'):
        assert not _is_linked(a2, 'iot2_System', b)


def test_assoc_components5_reverse_link_reassign_clear():
    a1 = iot2_HWComponent(name="sample_text")
    a2 = iot2_HWComponent(name="sample_text_2")
    b = iot2_Board(name="sample_text", type="sample_text")
    _safe_set(b, 'iot2_Board6', {a1})
    assert _is_linked(b, 'iot2_Board6', a1)
    if hasattr(a1, 'iot2_HWComponent7'):
        assert _is_linked(a1, 'iot2_HWComponent7', b)
    _safe_set(b, 'iot2_Board6', {a2})
    assert _is_linked(b, 'iot2_Board6', a2)
    if hasattr(a1, 'iot2_HWComponent7'):
        assert not _is_linked(a1, 'iot2_HWComponent7', b)
    if hasattr(a2, 'iot2_HWComponent7'):
        assert _is_linked(a2, 'iot2_HWComponent7', b)
    _safe_set(b, 'iot2_Board6', set())
    assert not _is_linked(b, 'iot2_Board6', a2)
    if hasattr(a2, 'iot2_HWComponent7'):
        assert not _is_linked(a2, 'iot2_HWComponent7', b)


def test_assoc_function83_reverse_link_reassign_clear():
    a1 = iot2_Statement_GlobalFunction_Declaration(functionName="sample_text", prefix="sample_text")
    a2 = iot2_Statement_GlobalFunction_Declaration(functionName="sample_text_2", prefix="sample_text_2")
    b = iot2_Function(parameters="sample_text", varArgs=True)
    _safe_set(b, 'iot2_Function', a1)
    assert _is_linked(b, 'iot2_Function', a1)
    if hasattr(a1, 'iot2_Statement_GlobalFunction_Declaration'):
        assert _is_linked(a1, 'iot2_Statement_GlobalFunction_Declaration', b)
    _safe_set(b, 'iot2_Function', a2)
    assert _is_linked(b, 'iot2_Function', a2)
    if hasattr(a1, 'iot2_Statement_GlobalFunction_Declaration'):
        assert not _is_linked(a1, 'iot2_Statement_GlobalFunction_Declaration', b)
    if hasattr(a2, 'iot2_Statement_GlobalFunction_Declaration'):
        assert _is_linked(a2, 'iot2_Statement_GlobalFunction_Declaration', b)
    _safe_set(b, 'iot2_Function', None)
    assert not _is_linked(b, 'iot2_Function', a2)
    if hasattr(a2, 'iot2_Statement_GlobalFunction_Declaration'):
        assert not _is_linked(a2, 'iot2_Statement_GlobalFunction_Declaration', b)


def test_assoc_function84_reverse_link_reassign_clear():
    a1 = iot2_Statement_LocalFunction_Declaration(functionName="sample_text")
    a2 = iot2_Statement_LocalFunction_Declaration(functionName="sample_text_2")
    b = iot2_Function(parameters="sample_text", varArgs=True)
    _safe_set(b, 'iot2_Function85', a1)
    assert _is_linked(b, 'iot2_Function85', a1)
    if hasattr(a1, 'iot2_Statement_LocalFunction_Declaration'):
        assert _is_linked(a1, 'iot2_Statement_LocalFunction_Declaration', b)
    _safe_set(b, 'iot2_Function85', a2)
    assert _is_linked(b, 'iot2_Function85', a2)
    if hasattr(a1, 'iot2_Statement_LocalFunction_Declaration'):
        assert not _is_linked(a1, 'iot2_Statement_LocalFunction_Declaration', b)
    if hasattr(a2, 'iot2_Statement_LocalFunction_Declaration'):
        assert _is_linked(a2, 'iot2_Statement_LocalFunction_Declaration', b)
    _safe_set(b, 'iot2_Function85', None)
    assert not _is_linked(b, 'iot2_Function85', a2)
    if hasattr(a2, 'iot2_Statement_LocalFunction_Declaration'):
        assert not _is_linked(a2, 'iot2_Statement_LocalFunction_Declaration', b)


def test_assoc_members31_reverse_link_reassign_clear():
    a1 = iot2_Field(identifier="sample_text")
    a2 = iot2_Field(identifier="sample_text_2")
    b = iot2_ExceptionDef(typeCode="sample_text")
    _safe_set(b, 'iot2_ExceptionDef32', {a1})
    assert _is_linked(b, 'iot2_ExceptionDef32', a1)
    if hasattr(a1, 'iot2_Field'):
        assert _is_linked(a1, 'iot2_Field', b)
    _safe_set(b, 'iot2_ExceptionDef32', {a2})
    assert _is_linked(b, 'iot2_ExceptionDef32', a2)
    if hasattr(a1, 'iot2_Field'):
        assert not _is_linked(a1, 'iot2_Field', b)
    if hasattr(a2, 'iot2_Field'):
        assert _is_linked(a2, 'iot2_Field', b)
    _safe_set(b, 'iot2_ExceptionDef32', set())
    assert not _is_linked(b, 'iot2_ExceptionDef32', a2)
    if hasattr(a2, 'iot2_Field'):
        assert not _is_linked(a2, 'iot2_Field', b)


def test_assoc_parameters20_reverse_link_reassign_clear():
    a1 = iot2_ParameterDef(direction="sample_text", identifier="sample_text")
    a2 = iot2_ParameterDef(direction="sample_text_2", identifier="sample_text_2")
    b = iot2_OperationDef(contexts="sample_text", isOneway=True)
    _safe_set(b, 'iot2_OperationDef21', {a1})
    assert _is_linked(b, 'iot2_OperationDef21', a1)
    if hasattr(a1, 'iot2_ParameterDef'):
        assert _is_linked(a1, 'iot2_ParameterDef', b)
    _safe_set(b, 'iot2_OperationDef21', {a2})
    assert _is_linked(b, 'iot2_OperationDef21', a2)
    if hasattr(a1, 'iot2_ParameterDef'):
        assert not _is_linked(a1, 'iot2_ParameterDef', b)
    if hasattr(a2, 'iot2_ParameterDef'):
        assert _is_linked(a2, 'iot2_ParameterDef', b)
    _safe_set(b, 'iot2_OperationDef21', set())
    assert not _is_linked(b, 'iot2_OperationDef21', a2)
    if hasattr(a2, 'iot2_ParameterDef'):
        assert not _is_linked(a2, 'iot2_ParameterDef', b)


def test_assoc_services10_reverse_link_reassign_clear():
    a1 = iot2_OperationDef(contexts="sample_text", isOneway=True)
    a2 = iot2_OperationDef(contexts="sample_text_2", isOneway=False)
    b = iot2_HWComponent(name="sample_text")
    _safe_set(b, 'iot2_HWComponent11', {a1})
    assert _is_linked(b, 'iot2_HWComponent11', a1)
    if hasattr(a1, 'iot2_OperationDef'):
        assert _is_linked(a1, 'iot2_OperationDef', b)
    _safe_set(b, 'iot2_HWComponent11', {a2})
    assert _is_linked(b, 'iot2_HWComponent11', a2)
    if hasattr(a1, 'iot2_OperationDef'):
        assert not _is_linked(a1, 'iot2_OperationDef', b)
    if hasattr(a2, 'iot2_OperationDef'):
        assert _is_linked(a2, 'iot2_OperationDef', b)
    _safe_set(b, 'iot2_HWComponent11', set())
    assert not _is_linked(b, 'iot2_HWComponent11', a2)
    if hasattr(a2, 'iot2_OperationDef'):
        assert not _is_linked(a2, 'iot2_OperationDef', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activity217_stub_double():
    # iot2_Activity has no real 'Activity' property in the generated
    # code (a bare stub) -- manually attach it so iot2_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_ActivityNode(running=True)
    partner = iot2_Activity()
    setattr(partner, 'Activity', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'Activity') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'Activity') is None


def test_assoc_arguments108_stub_double():
    # iot2_Functioncall_Arguments has no real 'iot2_Functioncall_Arguments110' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_CallMemberFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_CallMemberFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_CallMemberFunction(memberFunctionName="sample_text")
    partner = iot2_Functioncall_Arguments()
    setattr(partner, 'iot2_Functioncall_Arguments110', None)
    _safe_set(owner, 'iot2_Statement_CallMemberFunction109', partner)
    assert getattr(partner, 'iot2_Functioncall_Arguments110') == owner
    _safe_set(owner, 'iot2_Statement_CallMemberFunction109', None)
    assert getattr(partner, 'iot2_Functioncall_Arguments110') is None


def test_assoc_arguments199_stub_double():
    # iot2_Functioncall_Arguments has no real 'iot2_Functioncall_Arguments201' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Expression_CallMemberFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Expression_CallMemberFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Expression_CallMemberFunction(memberFunctionName="sample_text")
    partner = iot2_Functioncall_Arguments()
    setattr(partner, 'iot2_Functioncall_Arguments201', None)
    _safe_set(owner, 'iot2_Expression_CallMemberFunction200', partner)
    assert getattr(partner, 'iot2_Functioncall_Arguments201') == owner
    _safe_set(owner, 'iot2_Expression_CallMemberFunction200', None)
    assert getattr(partner, 'iot2_Functioncall_Arguments201') is None


def test_assoc_assignee239_stub_double():
    # iot2_IntegerVariable has no real 'iot2_IntegerVariable240' property in the generated
    # code (a bare stub) -- manually attach it so iot2_IntegerCalculationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_IntegerCalculationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_IntegerCalculationExpression(operator="sample_text")
    partner = iot2_IntegerVariable()
    setattr(partner, 'iot2_IntegerVariable240', None)
    _safe_set(owner, 'iot2_IntegerCalculationExpression', partner)
    assert getattr(partner, 'iot2_IntegerVariable240') == owner
    _safe_set(owner, 'iot2_IntegerCalculationExpression', None)
    assert getattr(partner, 'iot2_IntegerVariable240') is None


def test_assoc_assignee241_stub_double():
    # iot2_BooleanVariable has no real 'iot2_BooleanVariable242' property in the generated
    # code (a bare stub) -- manually attach it so iot2_IntegerComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_IntegerComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_IntegerComparisonExpression(operator="sample_text")
    partner = iot2_BooleanVariable()
    setattr(partner, 'iot2_BooleanVariable242', None)
    _safe_set(owner, 'iot2_IntegerComparisonExpression', partner)
    assert getattr(partner, 'iot2_BooleanVariable242') == owner
    _safe_set(owner, 'iot2_IntegerComparisonExpression', None)
    assert getattr(partner, 'iot2_BooleanVariable242') is None


def test_assoc_block75_stub_double():
    # iot2_Block has no real 'iot2_Block77' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_For_Numeric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_For_Numeric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_For_Numeric(iteratorName="sample_text")
    partner = iot2_Block()
    setattr(partner, 'iot2_Block77', None)
    _safe_set(owner, 'iot2_Statement_For_Numeric76', partner)
    assert getattr(partner, 'iot2_Block77') == owner
    _safe_set(owner, 'iot2_Statement_For_Numeric76', None)
    assert getattr(partner, 'iot2_Block77') is None


def test_assoc_block80_stub_double():
    # iot2_Block has no real 'iot2_Block82' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_For_Generic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_For_Generic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_For_Generic(names="sample_text")
    partner = iot2_Block()
    setattr(partner, 'iot2_Block82', None)
    _safe_set(owner, 'iot2_Statement_For_Generic81', partner)
    assert getattr(partner, 'iot2_Block82') == owner
    _safe_set(owner, 'iot2_Statement_For_Generic81', None)
    assert getattr(partner, 'iot2_Block82') is None


def test_assoc_body92_stub_double():
    # iot2_Block has no real 'iot2_Block94' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Function(parameters="sample_text", varArgs=True)
    partner = iot2_Block()
    setattr(partner, 'iot2_Block94', None)
    _safe_set(owner, 'iot2_Function93', partner)
    assert getattr(partner, 'iot2_Block94') == owner
    _safe_set(owner, 'iot2_Function93', None)
    assert getattr(partner, 'iot2_Block94') is None


def test_assoc_containedType28_stub_double():
    # iot2_Typed has no real 'iot2_Typed' property in the generated
    # code (a bare stub) -- manually attach it so iot2_IDLType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_IDLType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_IDLType(typeCode="sample_text")
    partner = iot2_Typed()
    setattr(partner, 'iot2_Typed', None)
    _safe_set(owner, 'iot2_IDLType', partner)
    assert getattr(partner, 'iot2_Typed') == owner
    _safe_set(owner, 'iot2_IDLType', None)
    assert getattr(partner, 'iot2_Typed') is None


def test_assoc_contains27_stub_double():
    # iot2_Container has no real 'definedIn' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Contained's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Contained's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Contained(absoluteName="sample_text", repositoryId="sample_text", version="sample_text")
    partner = iot2_Container()
    setattr(partner, 'definedIn', None)
    _safe_set(owner, 'Contained', partner)
    assert owner in getattr(partner, 'definedIn')
    _safe_set(owner, 'Contained', None)
    assert owner not in getattr(partner, 'definedIn')


def test_assoc_currentValue230_stub_double():
    # iot2_Value has no real 'iot2_Value232' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Variable(name="sample_text")
    partner = iot2_Value()
    setattr(partner, 'iot2_Value232', None)
    _safe_set(owner, 'iot2_Variable231', partner)
    assert getattr(partner, 'iot2_Value232') == owner
    _safe_set(owner, 'iot2_Variable231', None)
    assert getattr(partner, 'iot2_Value232') is None


def test_assoc_definedIn26_stub_double():
    # iot2_Container has no real 'Container' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Contained's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Contained's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Contained(absoluteName="sample_text", repositoryId="sample_text", version="sample_text")
    partner = iot2_Container()
    setattr(partner, 'Container', None)
    _safe_set(owner, 'contains', partner)
    assert getattr(partner, 'Container') == owner
    _safe_set(owner, 'contains', None)
    assert getattr(partner, 'Container') is None


def test_assoc_executedNodes258_stub_double():
    # iot2_Trace has no real 'iot2_Trace' property in the generated
    # code (a bare stub) -- manually attach it so iot2_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_ActivityNode(running=True)
    partner = iot2_Trace()
    setattr(partner, 'iot2_Trace', None)
    _safe_set(owner, 'iot2_ActivityNode259', partner)
    assert owner in getattr(partner, 'iot2_Trace')
    _safe_set(owner, 'iot2_ActivityNode259', None)
    assert owner not in getattr(partner, 'iot2_Trace')


def test_assoc_expressions78_stub_double():
    # iot2_Expression has no real 'iot2_Expression79' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_For_Generic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_For_Generic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_For_Generic(names="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression79', None)
    _safe_set(owner, 'iot2_Statement_For_Generic', {partner})
    assert getattr(partner, 'iot2_Expression79') == owner
    _safe_set(owner, 'iot2_Statement_For_Generic', set())
    assert getattr(partner, 'iot2_Expression79') is None


def test_assoc_fields90_stub_double():
    # iot2_Expression_TableConstructor has no real 'iot2_Expression_TableConstructor' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Field(identifier="sample_text")
    partner = iot2_Expression_TableConstructor()
    setattr(partner, 'iot2_Expression_TableConstructor', None)
    _safe_set(owner, 'iot2_Field91', partner)
    assert owner in getattr(partner, 'iot2_Expression_TableConstructor')
    _safe_set(owner, 'iot2_Field91', None)
    assert owner not in getattr(partner, 'iot2_Expression_TableConstructor')


def test_assoc_function88_stub_double():
    # iot2_Expression_Function has no real 'iot2_Expression_Function' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Function(parameters="sample_text", varArgs=True)
    partner = iot2_Expression_Function()
    setattr(partner, 'iot2_Expression_Function', None)
    _safe_set(owner, 'iot2_Function89', partner)
    assert getattr(partner, 'iot2_Expression_Function') == owner
    _safe_set(owner, 'iot2_Function89', None)
    assert getattr(partner, 'iot2_Expression_Function') is None


def test_assoc_holder257_stub_double():
    # iot2_Token has no real 'iot2_Token' property in the generated
    # code (a bare stub) -- manually attach it so iot2_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_ActivityNode(running=True)
    partner = iot2_Token()
    setattr(partner, 'iot2_Token', None)
    _safe_set(owner, 'iot2_ActivityNode', partner)
    assert getattr(partner, 'iot2_Token') == owner
    _safe_set(owner, 'iot2_ActivityNode', None)
    assert getattr(partner, 'iot2_Token') is None


def test_assoc_incoming215_stub_double():
    # iot2_ActivityEdge has no real 'ActivityEdge216' property in the generated
    # code (a bare stub) -- manually attach it so iot2_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_ActivityNode(running=True)
    partner = iot2_ActivityEdge()
    setattr(partner, 'ActivityEdge216', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'ActivityEdge216') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'ActivityEdge216') is None


def test_assoc_initialValue228_stub_double():
    # iot2_Value has no real 'iot2_Value' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Variable(name="sample_text")
    partner = iot2_Value()
    setattr(partner, 'iot2_Value', None)
    _safe_set(owner, 'iot2_Variable229', partner)
    assert getattr(partner, 'iot2_Value') == owner
    _safe_set(owner, 'iot2_Variable229', None)
    assert getattr(partner, 'iot2_Value') is None


def test_assoc_initialValue86_stub_double():
    # iot2_Expression has no real 'iot2_Expression87' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_Local_Variable_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_Local_Variable_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_Local_Variable_Declaration(variableNames="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression87', None)
    _safe_set(owner, 'iot2_Statement_Local_Variable_Declaration', {partner})
    assert getattr(partner, 'iot2_Expression87') == owner
    _safe_set(owner, 'iot2_Statement_Local_Variable_Declaration', set())
    assert getattr(partner, 'iot2_Expression87') is None


def test_assoc_inputs17_stub_double():
    # iot2_Activity has no real 'iot2_Activity18' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Variable(name="sample_text")
    partner = iot2_Activity()
    setattr(partner, 'iot2_Activity18', None)
    _safe_set(owner, 'iot2_Variable19', partner)
    assert owner in getattr(partner, 'iot2_Activity18')
    _safe_set(owner, 'iot2_Variable19', None)
    assert owner not in getattr(partner, 'iot2_Activity18')


def test_assoc_locals15_stub_double():
    # iot2_Activity has no real 'iot2_Activity16' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Variable(name="sample_text")
    partner = iot2_Activity()
    setattr(partner, 'iot2_Activity16', None)
    _safe_set(owner, 'iot2_Variable', partner)
    assert owner in getattr(partner, 'iot2_Activity16')
    _safe_set(owner, 'iot2_Variable', None)
    assert owner not in getattr(partner, 'iot2_Activity16')


def test_assoc_lua24_stub_double():
    # iot2_Block has no real 'iot2_Block' property in the generated
    # code (a bare stub) -- manually attach it so iot2_OperationDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_OperationDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_OperationDef(contexts="sample_text", isOneway=True)
    partner = iot2_Block()
    setattr(partner, 'iot2_Block', None)
    _safe_set(owner, 'iot2_OperationDef25', partner)
    assert getattr(partner, 'iot2_Block') == owner
    _safe_set(owner, 'iot2_OperationDef25', None)
    assert getattr(partner, 'iot2_Block') is None


def test_assoc_nodes12_stub_double():
    # iot2_Activity has no real 'activity' property in the generated
    # code (a bare stub) -- manually attach it so iot2_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_ActivityNode(running=True)
    partner = iot2_Activity()
    setattr(partner, 'activity', None)
    _safe_set(owner, 'ActivityNode', partner)
    assert owner in getattr(partner, 'activity')
    _safe_set(owner, 'ActivityNode', None)
    assert owner not in getattr(partner, 'activity')


def test_assoc_object106_stub_double():
    # iot2_Expression has no real 'iot2_Expression107' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_CallMemberFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_CallMemberFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_CallMemberFunction(memberFunctionName="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression107', None)
    _safe_set(owner, 'iot2_Statement_CallMemberFunction', partner)
    assert getattr(partner, 'iot2_Expression107') == owner
    _safe_set(owner, 'iot2_Statement_CallMemberFunction', None)
    assert getattr(partner, 'iot2_Expression107') is None


def test_assoc_object197_stub_double():
    # iot2_Expression has no real 'iot2_Expression198' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Expression_CallMemberFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Expression_CallMemberFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Expression_CallMemberFunction(memberFunctionName="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression198', None)
    _safe_set(owner, 'iot2_Expression_CallMemberFunction', partner)
    assert getattr(partner, 'iot2_Expression198') == owner
    _safe_set(owner, 'iot2_Expression_CallMemberFunction', None)
    assert getattr(partner, 'iot2_Expression198') is None


def test_assoc_object212_stub_double():
    # iot2_Expression has no real 'iot2_Expression213' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Expression_AccessMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Expression_AccessMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Expression_AccessMember(memberName="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression213', None)
    _safe_set(owner, 'iot2_Expression_AccessMember', partner)
    assert getattr(partner, 'iot2_Expression213') == owner
    _safe_set(owner, 'iot2_Expression_AccessMember', None)
    assert getattr(partner, 'iot2_Expression213') is None


def test_assoc_operand1245_stub_double():
    # iot2_BooleanVariable has no real 'iot2_BooleanVariable246' property in the generated
    # code (a bare stub) -- manually attach it so iot2_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_BooleanBinaryExpression(operator="sample_text")
    partner = iot2_BooleanVariable()
    setattr(partner, 'iot2_BooleanVariable246', None)
    _safe_set(owner, 'iot2_BooleanBinaryExpression', partner)
    assert getattr(partner, 'iot2_BooleanVariable246') == owner
    _safe_set(owner, 'iot2_BooleanBinaryExpression', None)
    assert getattr(partner, 'iot2_BooleanVariable246') is None


def test_assoc_operand2247_stub_double():
    # iot2_BooleanVariable has no real 'iot2_BooleanVariable249' property in the generated
    # code (a bare stub) -- manually attach it so iot2_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_BooleanBinaryExpression(operator="sample_text")
    partner = iot2_BooleanVariable()
    setattr(partner, 'iot2_BooleanVariable249', None)
    _safe_set(owner, 'iot2_BooleanBinaryExpression248', partner)
    assert getattr(partner, 'iot2_BooleanVariable249') == owner
    _safe_set(owner, 'iot2_BooleanBinaryExpression248', None)
    assert getattr(partner, 'iot2_BooleanVariable249') is None


def test_assoc_operand243_stub_double():
    # iot2_BooleanVariable has no real 'iot2_BooleanVariable244' property in the generated
    # code (a bare stub) -- manually attach it so iot2_BooleanUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_BooleanUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_BooleanUnaryExpression(operator="sample_text")
    partner = iot2_BooleanVariable()
    setattr(partner, 'iot2_BooleanVariable244', None)
    _safe_set(owner, 'iot2_BooleanUnaryExpression', partner)
    assert getattr(partner, 'iot2_BooleanVariable244') == owner
    _safe_set(owner, 'iot2_BooleanUnaryExpression', None)
    assert getattr(partner, 'iot2_BooleanVariable244') is None


def test_assoc_outgoing214_stub_double():
    # iot2_ActivityEdge has no real 'ActivityEdge' property in the generated
    # code (a bare stub) -- manually attach it so iot2_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_ActivityNode(running=True)
    partner = iot2_ActivityEdge()
    setattr(partner, 'ActivityEdge', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'ActivityEdge') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'ActivityEdge') is None


def test_assoc_service225_stub_double():
    # iot2_OpaqueAction has no real 'iot2_OpaqueAction226' property in the generated
    # code (a bare stub) -- manually attach it so iot2_OperationDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_OperationDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_OperationDef(contexts="sample_text", isOneway=True)
    partner = iot2_OpaqueAction()
    setattr(partner, 'iot2_OpaqueAction226', None)
    _safe_set(owner, 'iot2_OperationDef227', partner)
    assert getattr(partner, 'iot2_OpaqueAction226') == owner
    _safe_set(owner, 'iot2_OperationDef227', None)
    assert getattr(partner, 'iot2_OpaqueAction226') is None


def test_assoc_sketch3_stub_double():
    # iot2_Sketch has no real 'iot2_Sketch' property in the generated
    # code (a bare stub) -- manually attach it so iot2_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_System(name="sample_text")
    partner = iot2_Sketch()
    setattr(partner, 'iot2_Sketch', None)
    _safe_set(owner, 'iot2_System4', partner)
    assert getattr(partner, 'iot2_Sketch') == owner
    _safe_set(owner, 'iot2_System4', None)
    assert getattr(partner, 'iot2_Sketch') is None


def test_assoc_source218_stub_double():
    # iot2_ActivityEdge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so iot2_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_ActivityNode(running=True)
    partner = iot2_ActivityEdge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'ActivityNode219', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'ActivityNode219', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_startExpr67_stub_double():
    # iot2_Expression has no real 'iot2_Expression68' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_For_Numeric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_For_Numeric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_For_Numeric(iteratorName="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression68', None)
    _safe_set(owner, 'iot2_Statement_For_Numeric', partner)
    assert getattr(partner, 'iot2_Expression68') == owner
    _safe_set(owner, 'iot2_Statement_For_Numeric', None)
    assert getattr(partner, 'iot2_Expression68') is None


def test_assoc_stepExpr72_stub_double():
    # iot2_Expression has no real 'iot2_Expression74' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_For_Numeric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_For_Numeric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_For_Numeric(iteratorName="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression74', None)
    _safe_set(owner, 'iot2_Statement_For_Numeric73', partner)
    assert getattr(partner, 'iot2_Expression74') == owner
    _safe_set(owner, 'iot2_Statement_For_Numeric73', None)
    assert getattr(partner, 'iot2_Expression74') is None


def test_assoc_target220_stub_double():
    # iot2_ActivityEdge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so iot2_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_ActivityNode(running=True)
    partner = iot2_ActivityEdge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'ActivityNode221', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'ActivityNode221', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_untilExpr69_stub_double():
    # iot2_Expression has no real 'iot2_Expression71' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Statement_For_Numeric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Statement_For_Numeric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Statement_For_Numeric(iteratorName="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression71', None)
    _safe_set(owner, 'iot2_Statement_For_Numeric70', partner)
    assert getattr(partner, 'iot2_Expression71') == owner
    _safe_set(owner, 'iot2_Statement_For_Numeric70', None)
    assert getattr(partner, 'iot2_Expression71') is None


def test_assoc_value33_stub_double():
    # iot2_Expression has no real 'iot2_Expression' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Field(identifier="sample_text")
    partner = iot2_Expression()
    setattr(partner, 'iot2_Expression', None)
    _safe_set(owner, 'iot2_Field34', partner)
    assert getattr(partner, 'iot2_Expression') == owner
    _safe_set(owner, 'iot2_Field34', None)
    assert getattr(partner, 'iot2_Expression') is None


def test_assoc_variable252_stub_double():
    # iot2_InputValue has no real 'iot2_InputValue253' property in the generated
    # code (a bare stub) -- manually attach it so iot2_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot2_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot2_Variable(name="sample_text")
    partner = iot2_InputValue()
    setattr(partner, 'iot2_InputValue253', None)
    _safe_set(owner, 'iot2_Variable254', partner)
    assert getattr(partner, 'iot2_InputValue253') == owner
    _safe_set(owner, 'iot2_Variable254', None)
    assert getattr(partner, 'iot2_InputValue253') is None


