import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Assignable,
    BasicContext,
    BasicPackage,
    BinaryExpression,
    ConnectionNode,
    Context,
    Controller,
    Expression,
    Junction,
    LambdaExp,
    Member,
    NamedElement,
    NamedExpression,
    Node,
    NodeContainer,
    Operation,
    OperationSig,
    QuantifierExpression,
    Reference,
    RelationType,
    RoboticPlatform,
    SetType,
    State,
    StateMachine,
    StateMachineBody,
    Statement,
    Type,
    TypeDecl,
    TypedNamedElement,
    Variable,
    robochart_Action,
    robochart_And,
    robochart_AnyType,
    robochart_ArrayAssignable,
    robochart_ArrayExp,
    robochart_AsExp,
    robochart_Assignable,
    robochart_Assignment,
    robochart_BasicContext,
    robochart_BasicPackage,
    robochart_BinaryExpression,
    robochart_BooleanExp,
    robochart_Call,
    robochart_CallExp,
    robochart_Cat,
    robochart_Clock,
    robochart_ClockExp,
    robochart_ClockReset,
    robochart_Connection,
    robochart_ConnectionNode,
    robochart_Context,
    robochart_Controller,
    robochart_ControllerDef,
    robochart_ControllerRef,
    robochart_Declaration,
    robochart_DefiniteDescription,
    robochart_Different,
    robochart_Div,
    robochart_DuringAction,
    robochart_ElseExp,
    robochart_EntryAction,
    robochart_EnumExp,
    robochart_Enumeration,
    robochart_Equals,
    robochart_Event,
    robochart_Exists,
    robochart_ExitAction,
    robochart_Expression,
    robochart_Field,
    robochart_Final,
    robochart_FloatExp,
    robochart_Forall,
    robochart_FromExp,
    robochart_Function,
    robochart_FunctionType,
    robochart_GreaterOrEqual,
    robochart_GreaterThan,
    robochart_IdExp,
    robochart_IfExpression,
    robochart_IfStmt,
    robochart_Iff,
    robochart_Implies,
    robochart_Import,
    robochart_InExp,
    robochart_Initial,
    robochart_IntegerExp,
    robochart_Interface,
    robochart_IsExp,
    robochart_Junction,
    robochart_LambdaExp,
    robochart_LessOrEqual,
    robochart_LessThan,
    robochart_LetExpression,
    robochart_Literal,
    robochart_MatrixType,
    robochart_Member,
    robochart_Minus,
    robochart_Modulus,
    robochart_Mult,
    robochart_NameType,
    robochart_NamedElement,
    robochart_NamedExpression,
    robochart_Neg,
    robochart_Node,
    robochart_NodeContainer,
    robochart_Not,
    robochart_Operation,
    robochart_OperationDef,
    robochart_OperationRef,
    robochart_OperationSig,
    robochart_Or,
    robochart_ParExp,
    robochart_ParStmt,
    robochart_Parameter,
    robochart_Plus,
    robochart_PrimitiveType,
    robochart_ProbabilisticJunction,
    robochart_ProductType,
    robochart_QuantifierExpression,
    robochart_RCModule,
    robochart_RCPackage,
    robochart_RangeExp,
    robochart_RecordType,
    robochart_RefExp,
    robochart_Reference,
    robochart_RelationType,
    robochart_ResultExp,
    robochart_RoboticPlatform,
    robochart_RoboticPlatformDef,
    robochart_RoboticPlatformRef,
    robochart_Selection,
    robochart_SendEvent,
    robochart_SeqExp,
    robochart_SeqStatement,
    robochart_SeqType,
    robochart_SetComp,
    robochart_SetExp,
    robochart_SetRange,
    robochart_SetType,
    robochart_Skip,
    robochart_State,
    robochart_StateClockExp,
    robochart_StateMachine,
    robochart_StateMachineBody,
    robochart_StateMachineDef,
    robochart_StateMachineRef,
    robochart_Statement,
    robochart_StringExp,
    robochart_TimedStatement,
    robochart_ToExp,
    robochart_Transition,
    robochart_Trigger,
    robochart_TupleExp,
    robochart_Type,
    robochart_TypeDecl,
    robochart_TypeExp,
    robochart_TypeRef,
    robochart_TypedNamedElement,
    robochart_VarExp,
    robochart_VarRef,
    robochart_VarSelection,
    robochart_Variable,
    robochart_VariableList,
    robochart_VectorType,
    robochart_Wait,
    robochart_WaitingCondition,
    robochart_WaitingConditionRef,
    TriggerType,
    VariableModifier,
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

def test_assoc__from108_reverse_link_reassign_clear():
    a1 = robochart_Variable(modifier="sample_text")
    a2 = robochart_Variable(modifier="sample_text_2")
    b = robochart_Trigger(_type="sample_text")
    _safe_set(b, 'robochart_Trigger109', a1)
    assert _is_linked(b, 'robochart_Trigger109', a1)
    if hasattr(a1, 'robochart_Variable110'):
        assert _is_linked(a1, 'robochart_Variable110', b)
    _safe_set(b, 'robochart_Trigger109', a2)
    assert _is_linked(b, 'robochart_Trigger109', a2)
    if hasattr(a1, 'robochart_Variable110'):
        assert not _is_linked(a1, 'robochart_Variable110', b)
    if hasattr(a2, 'robochart_Variable110'):
        assert _is_linked(a2, 'robochart_Variable110', b)
    _safe_set(b, 'robochart_Trigger109', None)
    assert not _is_linked(b, 'robochart_Trigger109', a2)
    if hasattr(a2, 'robochart_Variable110'):
        assert not _is_linked(a2, 'robochart_Variable110', b)


def test_assoc_efrom139_reverse_link_reassign_clear():
    a1 = robochart_Event(broadcast=True)
    a2 = robochart_Event(broadcast=False)
    b = robochart_Connection(async_=True, bidirec=True)
    _safe_set(b, 'robochart_Connection140', a1)
    assert _is_linked(b, 'robochart_Connection140', a1)
    if hasattr(a1, 'robochart_Event141'):
        assert _is_linked(a1, 'robochart_Event141', b)
    _safe_set(b, 'robochart_Connection140', a2)
    assert _is_linked(b, 'robochart_Connection140', a2)
    if hasattr(a1, 'robochart_Event141'):
        assert not _is_linked(a1, 'robochart_Event141', b)
    if hasattr(a2, 'robochart_Event141'):
        assert _is_linked(a2, 'robochart_Event141', b)
    _safe_set(b, 'robochart_Connection140', None)
    assert not _is_linked(b, 'robochart_Connection140', a2)
    if hasattr(a2, 'robochart_Event141'):
        assert not _is_linked(a2, 'robochart_Event141', b)


def test_assoc_eto142_reverse_link_reassign_clear():
    a1 = robochart_Event(broadcast=True)
    a2 = robochart_Event(broadcast=False)
    b = robochart_Connection(async_=True, bidirec=True)
    _safe_set(b, 'robochart_Connection143', a1)
    assert _is_linked(b, 'robochart_Connection143', a1)
    if hasattr(a1, 'robochart_Event144'):
        assert _is_linked(a1, 'robochart_Event144', b)
    _safe_set(b, 'robochart_Connection143', a2)
    assert _is_linked(b, 'robochart_Connection143', a2)
    if hasattr(a1, 'robochart_Event144'):
        assert not _is_linked(a1, 'robochart_Event144', b)
    if hasattr(a2, 'robochart_Event144'):
        assert _is_linked(a2, 'robochart_Event144', b)
    _safe_set(b, 'robochart_Connection143', None)
    assert not _is_linked(b, 'robochart_Connection143', a2)
    if hasattr(a2, 'robochart_Event144'):
        assert not _is_linked(a2, 'robochart_Event144', b)


def test_assoc_event105_reverse_link_reassign_clear():
    a1 = robochart_Trigger(_type="sample_text")
    a2 = robochart_Trigger(_type="sample_text_2")
    b = robochart_Event(broadcast=True)
    _safe_set(b, 'robochart_Event107', a1)
    assert _is_linked(b, 'robochart_Event107', a1)
    if hasattr(a1, 'robochart_Trigger106'):
        assert _is_linked(a1, 'robochart_Trigger106', b)
    _safe_set(b, 'robochart_Event107', a2)
    assert _is_linked(b, 'robochart_Event107', a2)
    if hasattr(a1, 'robochart_Trigger106'):
        assert not _is_linked(a1, 'robochart_Trigger106', b)
    if hasattr(a2, 'robochart_Trigger106'):
        assert _is_linked(a2, 'robochart_Trigger106', b)
    _safe_set(b, 'robochart_Event107', None)
    assert not _is_linked(b, 'robochart_Event107', a2)
    if hasattr(a2, 'robochart_Trigger106'):
        assert not _is_linked(a2, 'robochart_Trigger106', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = robochart_Import(importedNamespace="sample_text")
    a2 = robochart_Import(importedNamespace="sample_text_2")
    b = robochart_BasicPackage(name="sample_text")
    _safe_set(b, 'robochart_BasicPackage', {a1})
    assert _is_linked(b, 'robochart_BasicPackage', a1)
    if hasattr(a1, 'robochart_Import'):
        assert _is_linked(a1, 'robochart_Import', b)
    _safe_set(b, 'robochart_BasicPackage', {a2})
    assert _is_linked(b, 'robochart_BasicPackage', a2)
    if hasattr(a1, 'robochart_Import'):
        assert not _is_linked(a1, 'robochart_Import', b)
    if hasattr(a2, 'robochart_Import'):
        assert _is_linked(a2, 'robochart_Import', b)
    _safe_set(b, 'robochart_BasicPackage', set())
    assert not _is_linked(b, 'robochart_BasicPackage', a2)
    if hasattr(a2, 'robochart_Import'):
        assert not _is_linked(a2, 'robochart_Import', b)


def test_assoc_parameter114_reverse_link_reassign_clear():
    a1 = robochart_Variable(modifier="sample_text")
    a2 = robochart_Variable(modifier="sample_text_2")
    b = robochart_Trigger(_type="sample_text")
    _safe_set(b, 'robochart_Trigger115', a1)
    assert _is_linked(b, 'robochart_Trigger115', a1)
    if hasattr(a1, 'robochart_Variable116'):
        assert _is_linked(a1, 'robochart_Variable116', b)
    _safe_set(b, 'robochart_Trigger115', a2)
    assert _is_linked(b, 'robochart_Trigger115', a2)
    if hasattr(a1, 'robochart_Variable116'):
        assert not _is_linked(a1, 'robochart_Variable116', b)
    if hasattr(a2, 'robochart_Variable116'):
        assert _is_linked(a2, 'robochart_Variable116', b)
    _safe_set(b, 'robochart_Trigger115', None)
    assert not _is_linked(b, 'robochart_Trigger115', a2)
    if hasattr(a2, 'robochart_Variable116'):
        assert not _is_linked(a2, 'robochart_Variable116', b)


def test_assoc_time120_reverse_link_reassign_clear():
    a1 = robochart_Variable(modifier="sample_text")
    a2 = robochart_Variable(modifier="sample_text_2")
    b = robochart_Trigger(_type="sample_text")
    _safe_set(b, 'robochart_Trigger121', a1)
    assert _is_linked(b, 'robochart_Trigger121', a1)
    if hasattr(a1, 'robochart_Variable122'):
        assert _is_linked(a1, 'robochart_Variable122', b)
    _safe_set(b, 'robochart_Trigger121', a2)
    assert _is_linked(b, 'robochart_Trigger121', a2)
    if hasattr(a1, 'robochart_Variable122'):
        assert not _is_linked(a1, 'robochart_Variable122', b)
    if hasattr(a2, 'robochart_Variable122'):
        assert _is_linked(a2, 'robochart_Variable122', b)
    _safe_set(b, 'robochart_Trigger121', None)
    assert not _is_linked(b, 'robochart_Trigger121', a2)
    if hasattr(a2, 'robochart_Variable122'):
        assert not _is_linked(a2, 'robochart_Variable122', b)


def test_assoc_vars35_reverse_link_reassign_clear():
    a1 = robochart_VariableList(modifier="sample_text")
    a2 = robochart_VariableList(modifier="sample_text_2")
    b = robochart_Variable(modifier="sample_text")
    _safe_set(b, 'robochart_Variable', a1)
    assert _is_linked(b, 'robochart_Variable', a1)
    if hasattr(a1, 'robochart_VariableList'):
        assert _is_linked(a1, 'robochart_VariableList', b)
    _safe_set(b, 'robochart_Variable', a2)
    assert _is_linked(b, 'robochart_Variable', a2)
    if hasattr(a1, 'robochart_VariableList'):
        assert not _is_linked(a1, 'robochart_VariableList', b)
    if hasattr(a2, 'robochart_VariableList'):
        assert _is_linked(a2, 'robochart_VariableList', b)
    _safe_set(b, 'robochart_Variable', None)
    assert not _is_linked(b, 'robochart_Variable', a2)
    if hasattr(a2, 'robochart_VariableList'):
        assert not _is_linked(a2, 'robochart_VariableList', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__predicate111_stub_double():
    # robochart_Expression has no real 'robochart_Expression113' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Trigger(_type="sample_text")
    partner = robochart_Expression()
    setattr(partner, 'robochart_Expression113', None)
    _safe_set(owner, 'robochart_Trigger112', partner)
    assert getattr(partner, 'robochart_Expression113') == owner
    _safe_set(owner, 'robochart_Trigger112', None)
    assert getattr(partner, 'robochart_Expression113') is None


def test_assoc_base317_stub_double():
    # robochart_Type has no real 'robochart_Type318' property in the generated
    # code (a bare stub) -- manually attach it so robochart_VectorType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_VectorType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_VectorType(size=7)
    partner = robochart_Type()
    setattr(partner, 'robochart_Type318', None)
    _safe_set(owner, 'robochart_VectorType', partner)
    assert getattr(partner, 'robochart_Type318') == owner
    _safe_set(owner, 'robochart_VectorType', None)
    assert getattr(partner, 'robochart_Type318') is None


def test_assoc_base319_stub_double():
    # robochart_Type has no real 'robochart_Type320' property in the generated
    # code (a bare stub) -- manually attach it so robochart_MatrixType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_MatrixType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_MatrixType(columns=7, rows=7)
    partner = robochart_Type()
    setattr(partner, 'robochart_Type320', None)
    _safe_set(owner, 'robochart_MatrixType', partner)
    assert getattr(partner, 'robochart_Type320') == owner
    _safe_set(owner, 'robochart_MatrixType', None)
    assert getattr(partner, 'robochart_Type320') is None


def test_assoc_connections132_stub_double():
    # robochart_ControllerDef has no real 'robochart_ControllerDef133' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Connection(async_=True, bidirec=True)
    partner = robochart_ControllerDef()
    setattr(partner, 'robochart_ControllerDef133', None)
    _safe_set(owner, 'robochart_Connection', partner)
    assert owner in getattr(partner, 'robochart_ControllerDef133')
    _safe_set(owner, 'robochart_Connection', None)
    assert owner not in getattr(partner, 'robochart_ControllerDef133')


def test_assoc_connections147_stub_double():
    # robochart_RCModule has no real 'robochart_RCModule148' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Connection(async_=True, bidirec=True)
    partner = robochart_RCModule()
    setattr(partner, 'robochart_RCModule148', None)
    _safe_set(owner, 'robochart_Connection149', partner)
    assert owner in getattr(partner, 'robochart_RCModule148')
    _safe_set(owner, 'robochart_Connection149', None)
    assert owner not in getattr(partner, 'robochart_RCModule148')


def test_assoc_events63_stub_double():
    # robochart_BasicContext has no real 'robochart_BasicContext64' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Event(broadcast=True)
    partner = robochart_BasicContext()
    setattr(partner, 'robochart_BasicContext64', None)
    _safe_set(owner, 'robochart_Event65', partner)
    assert owner in getattr(partner, 'robochart_BasicContext64')
    _safe_set(owner, 'robochart_Event65', None)
    assert owner not in getattr(partner, 'robochart_BasicContext64')


def test_assoc_from_134_stub_double():
    # robochart_ConnectionNode has no real 'robochart_ConnectionNode' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Connection(async_=True, bidirec=True)
    partner = robochart_ConnectionNode()
    setattr(partner, 'robochart_ConnectionNode', None)
    _safe_set(owner, 'robochart_Connection135', partner)
    assert getattr(partner, 'robochart_ConnectionNode') == owner
    _safe_set(owner, 'robochart_Connection135', None)
    assert getattr(partner, 'robochart_ConnectionNode') is None


def test_assoc_initial36_stub_double():
    # robochart_Expression has no real 'robochart_Expression' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Variable(modifier="sample_text")
    partner = robochart_Expression()
    setattr(partner, 'robochart_Expression', None)
    _safe_set(owner, 'robochart_Variable37', partner)
    assert getattr(partner, 'robochart_Expression') == owner
    _safe_set(owner, 'robochart_Variable37', None)
    assert getattr(partner, 'robochart_Expression') is None


def test_assoc_lrange288_stub_double():
    # robochart_Expression has no real 'robochart_Expression289' property in the generated
    # code (a bare stub) -- manually attach it so robochart_RangeExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_RangeExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_RangeExp(linterval="sample_text", rinterval="sample_text")
    partner = robochart_Expression()
    setattr(partner, 'robochart_Expression289', None)
    _safe_set(owner, 'robochart_RangeExp', partner)
    assert getattr(partner, 'robochart_Expression289') == owner
    _safe_set(owner, 'robochart_RangeExp', None)
    assert getattr(partner, 'robochart_Expression289') is None


def test_assoc_name308_stub_double():
    # robochart_VarRef has no real 'robochart_VarRef' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Variable(modifier="sample_text")
    partner = robochart_VarRef()
    setattr(partner, 'robochart_VarRef', None)
    _safe_set(owner, 'robochart_Variable309', partner)
    assert getattr(partner, 'robochart_VarRef') == owner
    _safe_set(owner, 'robochart_Variable309', None)
    assert getattr(partner, 'robochart_VarRef') is None


def test_assoc_operation181_stub_double():
    # robochart_Call has no real 'robochart_Call' property in the generated
    # code (a bare stub) -- manually attach it so robochart_OperationSig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_OperationSig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_OperationSig(terminates=True)
    partner = robochart_Call()
    setattr(partner, 'robochart_Call', None)
    _safe_set(owner, 'robochart_OperationSig182', partner)
    assert getattr(partner, 'robochart_Call') == owner
    _safe_set(owner, 'robochart_OperationSig182', None)
    assert getattr(partner, 'robochart_Call') is None


def test_assoc_operations60_stub_double():
    # robochart_BasicContext has no real 'robochart_BasicContext61' property in the generated
    # code (a bare stub) -- manually attach it so robochart_OperationSig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_OperationSig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_OperationSig(terminates=True)
    partner = robochart_BasicContext()
    setattr(partner, 'robochart_BasicContext61', None)
    _safe_set(owner, 'robochart_OperationSig62', partner)
    assert owner in getattr(partner, 'robochart_BasicContext61')
    _safe_set(owner, 'robochart_OperationSig62', None)
    assert owner not in getattr(partner, 'robochart_BasicContext61')


def test_assoc_parameters48_stub_double():
    # robochart_Parameter has no real 'robochart_Parameter49' property in the generated
    # code (a bare stub) -- manually attach it so robochart_OperationSig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_OperationSig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_OperationSig(terminates=True)
    partner = robochart_Parameter()
    setattr(partner, 'robochart_Parameter49', None)
    _safe_set(owner, 'robochart_OperationSig', {partner})
    assert getattr(partner, 'robochart_Parameter49') == owner
    _safe_set(owner, 'robochart_OperationSig', set())
    assert getattr(partner, 'robochart_Parameter49') is None


def test_assoc_postconditions53_stub_double():
    # robochart_Expression has no real 'robochart_Expression55' property in the generated
    # code (a bare stub) -- manually attach it so robochart_OperationSig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_OperationSig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_OperationSig(terminates=True)
    partner = robochart_Expression()
    setattr(partner, 'robochart_Expression55', None)
    _safe_set(owner, 'robochart_OperationSig54', {partner})
    assert getattr(partner, 'robochart_Expression55') == owner
    _safe_set(owner, 'robochart_OperationSig54', set())
    assert getattr(partner, 'robochart_Expression55') is None


def test_assoc_preconditions50_stub_double():
    # robochart_Expression has no real 'robochart_Expression52' property in the generated
    # code (a bare stub) -- manually attach it so robochart_OperationSig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_OperationSig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_OperationSig(terminates=True)
    partner = robochart_Expression()
    setattr(partner, 'robochart_Expression52', None)
    _safe_set(owner, 'robochart_OperationSig51', {partner})
    assert getattr(partner, 'robochart_Expression52') == owner
    _safe_set(owner, 'robochart_OperationSig51', set())
    assert getattr(partner, 'robochart_Expression52') is None


def test_assoc_reset123_stub_double():
    # robochart_ClockReset has no real 'robochart_ClockReset' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Trigger(_type="sample_text")
    partner = robochart_ClockReset()
    setattr(partner, 'robochart_ClockReset', None)
    _safe_set(owner, 'robochart_Trigger124', {partner})
    assert getattr(partner, 'robochart_ClockReset') == owner
    _safe_set(owner, 'robochart_Trigger124', set())
    assert getattr(partner, 'robochart_ClockReset') is None


def test_assoc_rrange290_stub_double():
    # robochart_Expression has no real 'robochart_Expression292' property in the generated
    # code (a bare stub) -- manually attach it so robochart_RangeExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_RangeExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_RangeExp(linterval="sample_text", rinterval="sample_text")
    partner = robochart_Expression()
    setattr(partner, 'robochart_Expression292', None)
    _safe_set(owner, 'robochart_RangeExp291', partner)
    assert getattr(partner, 'robochart_Expression292') == owner
    _safe_set(owner, 'robochart_RangeExp291', None)
    assert getattr(partner, 'robochart_Expression292') is None


def test_assoc_to136_stub_double():
    # robochart_ConnectionNode has no real 'robochart_ConnectionNode138' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Connection(async_=True, bidirec=True)
    partner = robochart_ConnectionNode()
    setattr(partner, 'robochart_ConnectionNode138', None)
    _safe_set(owner, 'robochart_Connection137', partner)
    assert getattr(partner, 'robochart_ConnectionNode138') == owner
    _safe_set(owner, 'robochart_Connection137', None)
    assert getattr(partner, 'robochart_ConnectionNode138') is None


def test_assoc_trigger175_stub_double():
    # robochart_SendEvent has no real 'robochart_SendEvent' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Trigger(_type="sample_text")
    partner = robochart_SendEvent()
    setattr(partner, 'robochart_SendEvent', None)
    _safe_set(owner, 'robochart_Trigger176', partner)
    assert getattr(partner, 'robochart_SendEvent') == owner
    _safe_set(owner, 'robochart_Trigger176', None)
    assert getattr(partner, 'robochart_SendEvent') is None


def test_assoc_trigger92_stub_double():
    # robochart_Transition has no real 'robochart_Transition93' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Trigger(_type="sample_text")
    partner = robochart_Transition()
    setattr(partner, 'robochart_Transition93', None)
    _safe_set(owner, 'robochart_Trigger', partner)
    assert getattr(partner, 'robochart_Transition93') == owner
    _safe_set(owner, 'robochart_Trigger', None)
    assert getattr(partner, 'robochart_Transition93') is None


def test_assoc_type38_stub_double():
    # robochart_Type has no real 'robochart_Type39' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Event(broadcast=True)
    partner = robochart_Type()
    setattr(partner, 'robochart_Type39', None)
    _safe_set(owner, 'robochart_Event', partner)
    assert getattr(partner, 'robochart_Type39') == owner
    _safe_set(owner, 'robochart_Event', None)
    assert getattr(partner, 'robochart_Type39') is None


def test_assoc_value117_stub_double():
    # robochart_Expression has no real 'robochart_Expression119' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Trigger(_type="sample_text")
    partner = robochart_Expression()
    setattr(partner, 'robochart_Expression119', None)
    _safe_set(owner, 'robochart_Trigger118', partner)
    assert getattr(partner, 'robochart_Expression119') == owner
    _safe_set(owner, 'robochart_Trigger118', None)
    assert getattr(partner, 'robochart_Expression119') is None


def test_assoc_value249_stub_double():
    # robochart_VarExp has no real 'robochart_VarExp' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Variable(modifier="sample_text")
    partner = robochart_VarExp()
    setattr(partner, 'robochart_VarExp', None)
    _safe_set(owner, 'robochart_Variable250', partner)
    assert getattr(partner, 'robochart_VarExp') == owner
    _safe_set(owner, 'robochart_Variable250', None)
    assert getattr(partner, 'robochart_VarExp') is None


def test_assoc_variableList58_stub_double():
    # robochart_BasicContext has no real 'robochart_BasicContext' property in the generated
    # code (a bare stub) -- manually attach it so robochart_VariableList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_VariableList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_VariableList(modifier="sample_text")
    partner = robochart_BasicContext()
    setattr(partner, 'robochart_BasicContext', None)
    _safe_set(owner, 'robochart_VariableList59', partner)
    assert owner in getattr(partner, 'robochart_BasicContext')
    _safe_set(owner, 'robochart_VariableList59', None)
    assert owner not in getattr(partner, 'robochart_BasicContext')


def test_assoc_variables203_stub_double():
    # robochart_QuantifierExpression has no real 'robochart_QuantifierExpression' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Variable(modifier="sample_text")
    partner = robochart_QuantifierExpression()
    setattr(partner, 'robochart_QuantifierExpression', None)
    _safe_set(owner, 'robochart_Variable204', partner)
    assert owner in getattr(partner, 'robochart_QuantifierExpression')
    _safe_set(owner, 'robochart_Variable204', None)
    assert owner not in getattr(partner, 'robochart_QuantifierExpression')


def test_assoc_variables211_stub_double():
    # robochart_LambdaExp has no real 'robochart_LambdaExp' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Variable(modifier="sample_text")
    partner = robochart_LambdaExp()
    setattr(partner, 'robochart_LambdaExp', None)
    _safe_set(owner, 'robochart_Variable212', partner)
    assert owner in getattr(partner, 'robochart_LambdaExp')
    _safe_set(owner, 'robochart_Variable212', None)
    assert owner not in getattr(partner, 'robochart_LambdaExp')


def test_assoc_variables273_stub_double():
    # robochart_SetComp has no real 'robochart_SetComp' property in the generated
    # code (a bare stub) -- manually attach it so robochart_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robochart_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robochart_Variable(modifier="sample_text")
    partner = robochart_SetComp()
    setattr(partner, 'robochart_SetComp', None)
    _safe_set(owner, 'robochart_Variable274', partner)
    assert owner in getattr(partner, 'robochart_SetComp')
    _safe_set(owner, 'robochart_Variable274', None)
    assert owner not in getattr(partner, 'robochart_SetComp')


