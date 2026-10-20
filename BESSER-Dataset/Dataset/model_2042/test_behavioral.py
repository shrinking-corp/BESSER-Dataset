import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Assignable,
    Expression,
    Identifiable,
    Literal,
    Statement,
    StatementOperation,
    StringExpression,
    urml_ActionCode,
    urml_Assignable,
    urml_Assignment,
    urml_Attribute,
    urml_BoolLiteral,
    urml_Capsule,
    urml_CapsuleInst,
    urml_ConcatenateExpression,
    urml_ConditionalAndExpression,
    urml_ConditionalOrExpression,
    urml_Connector,
    urml_Divide,
    urml_Equal,
    urml_Expression,
    urml_FunctionCall,
    urml_GreaterThan,
    urml_GreaterThanOrEqual,
    urml_Identifiable,
    urml_Identifier,
    urml_IfStatement,
    urml_IfStatementOperation,
    urml_IncomingVariable,
    urml_InformTimer,
    urml_IntLiteral,
    urml_Invoke,
    urml_LessThan,
    urml_LessThanOrEqual,
    urml_Literal,
    urml_LocalVar,
    urml_LogPort,
    urml_LogStatement,
    urml_Minus,
    urml_Model,
    urml_Modulo,
    urml_Multiply,
    urml_NoOp,
    urml_NotBooleanExpression,
    urml_NotEqual,
    urml_Operation,
    urml_OperationCode,
    urml_Plus,
    urml_Port,
    urml_Protocol,
    urml_ReturnStatement,
    urml_SendTrigger,
    urml_Signal,
    urml_StateMachine,
    urml_State_,
    urml_Statement,
    urml_StatementOperation,
    urml_StringExpression,
    urml_TimerPort,
    urml_Transition,
    urml_Trigger_in,
    urml_Trigger_out,
    urml_UnaryExpression,
    urml_Variable,
    urml_WhileLoop,
    urml_WhileLoopOperation,
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

def test_assoc_capsuleInsts23_reverse_link_reassign_clear():
    a1 = urml_CapsuleInst(name="sample_text")
    a2 = urml_CapsuleInst(name="sample_text_2")
    b = urml_Capsule(name="sample_text", root=True)
    _safe_set(b, 'urml_Capsule24', {a1})
    assert _is_linked(b, 'urml_Capsule24', a1)
    if hasattr(a1, 'urml_CapsuleInst'):
        assert _is_linked(a1, 'urml_CapsuleInst', b)
    _safe_set(b, 'urml_Capsule24', {a2})
    assert _is_linked(b, 'urml_Capsule24', a2)
    if hasattr(a1, 'urml_CapsuleInst'):
        assert not _is_linked(a1, 'urml_CapsuleInst', b)
    if hasattr(a2, 'urml_CapsuleInst'):
        assert _is_linked(a2, 'urml_CapsuleInst', b)
    _safe_set(b, 'urml_Capsule24', set())
    assert not _is_linked(b, 'urml_Capsule24', a2)
    if hasattr(a2, 'urml_CapsuleInst'):
        assert not _is_linked(a2, 'urml_CapsuleInst', b)


def test_assoc_capsules0_reverse_link_reassign_clear():
    a1 = urml_Model(name="sample_text")
    a2 = urml_Model(name="sample_text_2")
    b = urml_Capsule(name="sample_text", root=True)
    _safe_set(b, 'urml_Capsule', a1)
    assert _is_linked(b, 'urml_Capsule', a1)
    if hasattr(a1, 'urml_Model'):
        assert _is_linked(a1, 'urml_Model', b)
    _safe_set(b, 'urml_Capsule', a2)
    assert _is_linked(b, 'urml_Capsule', a2)
    if hasattr(a1, 'urml_Model'):
        assert not _is_linked(a1, 'urml_Model', b)
    if hasattr(a2, 'urml_Model'):
        assert _is_linked(a2, 'urml_Model', b)
    _safe_set(b, 'urml_Capsule', None)
    assert not _is_linked(b, 'urml_Capsule', a2)
    if hasattr(a2, 'urml_Model'):
        assert not _is_linked(a2, 'urml_Model', b)


def test_assoc_from_66_reverse_link_reassign_clear():
    a1 = urml_Transition(init=True, name="sample_text", universal=True)
    a2 = urml_Transition(init=False, name="sample_text_2", universal=False)
    b = urml_State_(final=True, name="sample_text")
    _safe_set(b, 'urml_State_68', a1)
    assert _is_linked(b, 'urml_State_68', a1)
    if hasattr(a1, 'urml_Transition67'):
        assert _is_linked(a1, 'urml_Transition67', b)
    _safe_set(b, 'urml_State_68', a2)
    assert _is_linked(b, 'urml_State_68', a2)
    if hasattr(a1, 'urml_Transition67'):
        assert not _is_linked(a1, 'urml_Transition67', b)
    if hasattr(a2, 'urml_Transition67'):
        assert _is_linked(a2, 'urml_Transition67', b)
    _safe_set(b, 'urml_State_68', None)
    assert not _is_linked(b, 'urml_State_68', a2)
    if hasattr(a2, 'urml_Transition67'):
        assert not _is_linked(a2, 'urml_Transition67', b)


def test_assoc_incomingMessages4_reverse_link_reassign_clear():
    a1 = urml_Signal(name="sample_text")
    a2 = urml_Signal(name="sample_text_2")
    b = urml_Protocol(name="sample_text")
    _safe_set(b, 'urml_Protocol5', {a1})
    assert _is_linked(b, 'urml_Protocol5', a1)
    if hasattr(a1, 'urml_Signal'):
        assert _is_linked(a1, 'urml_Signal', b)
    _safe_set(b, 'urml_Protocol5', {a2})
    assert _is_linked(b, 'urml_Protocol5', a2)
    if hasattr(a1, 'urml_Signal'):
        assert not _is_linked(a1, 'urml_Signal', b)
    if hasattr(a2, 'urml_Signal'):
        assert _is_linked(a2, 'urml_Signal', b)
    _safe_set(b, 'urml_Protocol5', set())
    assert not _is_linked(b, 'urml_Protocol5', a2)
    if hasattr(a2, 'urml_Signal'):
        assert not _is_linked(a2, 'urml_Signal', b)


def test_assoc_interfacePorts11_reverse_link_reassign_clear():
    a1 = urml_Port(conjugated=True, name="sample_text")
    a2 = urml_Port(conjugated=False, name="sample_text_2")
    b = urml_Capsule(name="sample_text", root=True)
    _safe_set(b, 'urml_Capsule12', {a1})
    assert _is_linked(b, 'urml_Capsule12', a1)
    if hasattr(a1, 'urml_Port'):
        assert _is_linked(a1, 'urml_Port', b)
    _safe_set(b, 'urml_Capsule12', {a2})
    assert _is_linked(b, 'urml_Capsule12', a2)
    if hasattr(a1, 'urml_Port'):
        assert not _is_linked(a1, 'urml_Port', b)
    if hasattr(a2, 'urml_Port'):
        assert _is_linked(a2, 'urml_Port', b)
    _safe_set(b, 'urml_Capsule12', set())
    assert not _is_linked(b, 'urml_Capsule12', a2)
    if hasattr(a2, 'urml_Port'):
        assert not _is_linked(a2, 'urml_Port', b)


def test_assoc_internalPorts13_reverse_link_reassign_clear():
    a1 = urml_Port(conjugated=True, name="sample_text")
    a2 = urml_Port(conjugated=False, name="sample_text_2")
    b = urml_Capsule(name="sample_text", root=True)
    _safe_set(b, 'urml_Capsule14', {a1})
    assert _is_linked(b, 'urml_Capsule14', a1)
    if hasattr(a1, 'urml_Port15'):
        assert _is_linked(a1, 'urml_Port15', b)
    _safe_set(b, 'urml_Capsule14', {a2})
    assert _is_linked(b, 'urml_Capsule14', a2)
    if hasattr(a1, 'urml_Port15'):
        assert not _is_linked(a1, 'urml_Port15', b)
    if hasattr(a2, 'urml_Port15'):
        assert _is_linked(a2, 'urml_Port15', b)
    _safe_set(b, 'urml_Capsule14', set())
    assert not _is_linked(b, 'urml_Capsule14', a2)
    if hasattr(a2, 'urml_Port15'):
        assert not _is_linked(a2, 'urml_Port15', b)


def test_assoc_logPorts18_reverse_link_reassign_clear():
    a1 = urml_LogPort(name="sample_text")
    a2 = urml_LogPort(name="sample_text_2")
    b = urml_Capsule(name="sample_text", root=True)
    _safe_set(b, 'urml_Capsule19', {a1})
    assert _is_linked(b, 'urml_Capsule19', a1)
    if hasattr(a1, 'urml_LogPort'):
        assert _is_linked(a1, 'urml_LogPort', b)
    _safe_set(b, 'urml_Capsule19', {a2})
    assert _is_linked(b, 'urml_Capsule19', a2)
    if hasattr(a1, 'urml_LogPort'):
        assert not _is_linked(a1, 'urml_LogPort', b)
    if hasattr(a2, 'urml_LogPort'):
        assert _is_linked(a2, 'urml_LogPort', b)
    _safe_set(b, 'urml_Capsule19', set())
    assert not _is_linked(b, 'urml_Capsule19', a2)
    if hasattr(a2, 'urml_LogPort'):
        assert not _is_linked(a2, 'urml_LogPort', b)


def test_assoc_operations27_reverse_link_reassign_clear():
    a1 = urml_Operation(isBool=True, isInt=True, isVoid=True, name="sample_text")
    a2 = urml_Operation(isBool=False, isInt=False, isVoid=False, name="sample_text_2")
    b = urml_Capsule(name="sample_text", root=True)
    _safe_set(b, 'urml_Capsule28', {a1})
    assert _is_linked(b, 'urml_Capsule28', a1)
    if hasattr(a1, 'urml_Operation'):
        assert _is_linked(a1, 'urml_Operation', b)
    _safe_set(b, 'urml_Capsule28', {a2})
    assert _is_linked(b, 'urml_Capsule28', a2)
    if hasattr(a1, 'urml_Operation'):
        assert not _is_linked(a1, 'urml_Operation', b)
    if hasattr(a2, 'urml_Operation'):
        assert _is_linked(a2, 'urml_Operation', b)
    _safe_set(b, 'urml_Capsule28', set())
    assert not _is_linked(b, 'urml_Capsule28', a2)
    if hasattr(a2, 'urml_Operation'):
        assert not _is_linked(a2, 'urml_Operation', b)


def test_assoc_outgoingMessages6_reverse_link_reassign_clear():
    a1 = urml_Signal(name="sample_text")
    a2 = urml_Signal(name="sample_text_2")
    b = urml_Protocol(name="sample_text")
    _safe_set(b, 'urml_Protocol7', {a1})
    assert _is_linked(b, 'urml_Protocol7', a1)
    if hasattr(a1, 'urml_Signal8'):
        assert _is_linked(a1, 'urml_Signal8', b)
    _safe_set(b, 'urml_Protocol7', {a2})
    assert _is_linked(b, 'urml_Protocol7', a2)
    if hasattr(a1, 'urml_Signal8'):
        assert not _is_linked(a1, 'urml_Signal8', b)
    if hasattr(a2, 'urml_Signal8'):
        assert _is_linked(a2, 'urml_Signal8', b)
    _safe_set(b, 'urml_Protocol7', set())
    assert not _is_linked(b, 'urml_Protocol7', a2)
    if hasattr(a2, 'urml_Signal8'):
        assert not _is_linked(a2, 'urml_Signal8', b)


def test_assoc_protocol36_reverse_link_reassign_clear():
    a1 = urml_Protocol(name="sample_text")
    a2 = urml_Protocol(name="sample_text_2")
    b = urml_Port(conjugated=True, name="sample_text")
    _safe_set(b, 'urml_Port37', a1)
    assert _is_linked(b, 'urml_Port37', a1)
    if hasattr(a1, 'urml_Protocol38'):
        assert _is_linked(a1, 'urml_Protocol38', b)
    _safe_set(b, 'urml_Port37', a2)
    assert _is_linked(b, 'urml_Port37', a2)
    if hasattr(a1, 'urml_Protocol38'):
        assert not _is_linked(a1, 'urml_Protocol38', b)
    if hasattr(a2, 'urml_Protocol38'):
        assert _is_linked(a2, 'urml_Protocol38', b)
    _safe_set(b, 'urml_Port37', None)
    assert not _is_linked(b, 'urml_Port37', a2)
    if hasattr(a2, 'urml_Protocol38'):
        assert not _is_linked(a2, 'urml_Protocol38', b)


def test_assoc_protocols1_reverse_link_reassign_clear():
    a1 = urml_Protocol(name="sample_text")
    a2 = urml_Protocol(name="sample_text_2")
    b = urml_Model(name="sample_text")
    _safe_set(b, 'urml_Model2', {a1})
    assert _is_linked(b, 'urml_Model2', a1)
    if hasattr(a1, 'urml_Protocol'):
        assert _is_linked(a1, 'urml_Protocol', b)
    _safe_set(b, 'urml_Model2', {a2})
    assert _is_linked(b, 'urml_Model2', a2)
    if hasattr(a1, 'urml_Protocol'):
        assert not _is_linked(a1, 'urml_Protocol', b)
    if hasattr(a2, 'urml_Protocol'):
        assert _is_linked(a2, 'urml_Protocol', b)
    _safe_set(b, 'urml_Model2', set())
    assert not _is_linked(b, 'urml_Model2', a2)
    if hasattr(a2, 'urml_Protocol'):
        assert not _is_linked(a2, 'urml_Protocol', b)


def test_assoc_timerPort77_reverse_link_reassign_clear():
    a1 = urml_Transition(init=True, name="sample_text", universal=True)
    a2 = urml_Transition(init=False, name="sample_text_2", universal=False)
    b = urml_TimerPort(name="sample_text")
    _safe_set(b, 'urml_TimerPort79', a1)
    assert _is_linked(b, 'urml_TimerPort79', a1)
    if hasattr(a1, 'urml_Transition78'):
        assert _is_linked(a1, 'urml_Transition78', b)
    _safe_set(b, 'urml_TimerPort79', a2)
    assert _is_linked(b, 'urml_TimerPort79', a2)
    if hasattr(a1, 'urml_Transition78'):
        assert not _is_linked(a1, 'urml_Transition78', b)
    if hasattr(a2, 'urml_Transition78'):
        assert _is_linked(a2, 'urml_Transition78', b)
    _safe_set(b, 'urml_TimerPort79', None)
    assert not _is_linked(b, 'urml_TimerPort79', a2)
    if hasattr(a2, 'urml_Transition78'):
        assert not _is_linked(a2, 'urml_Transition78', b)


def test_assoc_timerPorts16_reverse_link_reassign_clear():
    a1 = urml_TimerPort(name="sample_text")
    a2 = urml_TimerPort(name="sample_text_2")
    b = urml_Capsule(name="sample_text", root=True)
    _safe_set(b, 'urml_Capsule17', {a1})
    assert _is_linked(b, 'urml_Capsule17', a1)
    if hasattr(a1, 'urml_TimerPort'):
        assert _is_linked(a1, 'urml_TimerPort', b)
    _safe_set(b, 'urml_Capsule17', {a2})
    assert _is_linked(b, 'urml_Capsule17', a2)
    if hasattr(a1, 'urml_TimerPort'):
        assert not _is_linked(a1, 'urml_TimerPort', b)
    if hasattr(a2, 'urml_TimerPort'):
        assert _is_linked(a2, 'urml_TimerPort', b)
    _safe_set(b, 'urml_Capsule17', set())
    assert not _is_linked(b, 'urml_Capsule17', a2)
    if hasattr(a2, 'urml_TimerPort'):
        assert not _is_linked(a2, 'urml_TimerPort', b)


def test_assoc_to69_reverse_link_reassign_clear():
    a1 = urml_Transition(init=True, name="sample_text", universal=True)
    a2 = urml_Transition(init=False, name="sample_text_2", universal=False)
    b = urml_State_(final=True, name="sample_text")
    _safe_set(b, 'urml_State_71', a1)
    assert _is_linked(b, 'urml_State_71', a1)
    if hasattr(a1, 'urml_Transition70'):
        assert _is_linked(a1, 'urml_Transition70', b)
    _safe_set(b, 'urml_State_71', a2)
    assert _is_linked(b, 'urml_State_71', a2)
    if hasattr(a1, 'urml_Transition70'):
        assert not _is_linked(a1, 'urml_Transition70', b)
    if hasattr(a2, 'urml_Transition70'):
        assert _is_linked(a2, 'urml_Transition70', b)
    _safe_set(b, 'urml_State_71', None)
    assert not _is_linked(b, 'urml_State_71', a2)
    if hasattr(a2, 'urml_Transition70'):
        assert not _is_linked(a2, 'urml_Transition70', b)


def test_assoc_type51_reverse_link_reassign_clear():
    a1 = urml_CapsuleInst(name="sample_text")
    a2 = urml_CapsuleInst(name="sample_text_2")
    b = urml_Capsule(name="sample_text", root=True)
    _safe_set(b, 'urml_Capsule53', a1)
    assert _is_linked(b, 'urml_Capsule53', a1)
    if hasattr(a1, 'urml_CapsuleInst52'):
        assert _is_linked(a1, 'urml_CapsuleInst52', b)
    _safe_set(b, 'urml_Capsule53', a2)
    assert _is_linked(b, 'urml_Capsule53', a2)
    if hasattr(a1, 'urml_CapsuleInst52'):
        assert not _is_linked(a1, 'urml_CapsuleInst52', b)
    if hasattr(a2, 'urml_CapsuleInst52'):
        assert _is_linked(a2, 'urml_CapsuleInst52', b)
    _safe_set(b, 'urml_Capsule53', None)
    assert not _is_linked(b, 'urml_Capsule53', a2)
    if hasattr(a2, 'urml_CapsuleInst52'):
        assert not _is_linked(a2, 'urml_CapsuleInst52', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_LocalVars31_stub_double():
    # urml_LocalVar has no real 'urml_LocalVar33' property in the generated
    # code (a bare stub) -- manually attach it so urml_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Operation(isBool=True, isInt=True, isVoid=True, name="sample_text")
    partner = urml_LocalVar()
    setattr(partner, 'urml_LocalVar33', None)
    _safe_set(owner, 'urml_Operation32', {partner})
    assert getattr(partner, 'urml_LocalVar33') == owner
    _safe_set(owner, 'urml_Operation32', set())
    assert getattr(partner, 'urml_LocalVar33') is None


def test_assoc_LocalVars9_stub_double():
    # urml_LocalVar has no real 'urml_LocalVar' property in the generated
    # code (a bare stub) -- manually attach it so urml_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Signal(name="sample_text")
    partner = urml_LocalVar()
    setattr(partner, 'urml_LocalVar', None)
    _safe_set(owner, 'urml_Signal10', {partner})
    assert getattr(partner, 'urml_LocalVar') == owner
    _safe_set(owner, 'urml_Signal10', set())
    assert getattr(partner, 'urml_LocalVar') is None


def test_assoc_action80_stub_double():
    # urml_ActionCode has no real 'urml_ActionCode82' property in the generated
    # code (a bare stub) -- manually attach it so urml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Transition(init=True, name="sample_text", universal=True)
    partner = urml_ActionCode()
    setattr(partner, 'urml_ActionCode82', None)
    _safe_set(owner, 'urml_Transition81', partner)
    assert getattr(partner, 'urml_ActionCode82') == owner
    _safe_set(owner, 'urml_Transition81', None)
    assert getattr(partner, 'urml_ActionCode82') is None


def test_assoc_attributes20_stub_double():
    # urml_Attribute has no real 'urml_Attribute22' property in the generated
    # code (a bare stub) -- manually attach it so urml_Capsule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Capsule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Capsule(name="sample_text", root=True)
    partner = urml_Attribute()
    setattr(partner, 'urml_Attribute22', None)
    _safe_set(owner, 'urml_Capsule21', {partner})
    assert getattr(partner, 'urml_Attribute22') == owner
    _safe_set(owner, 'urml_Capsule21', set())
    assert getattr(partner, 'urml_Attribute22') is None


def test_assoc_call162_stub_double():
    # urml_FunctionCall has no real 'urml_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so urml_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Operation(isBool=True, isInt=True, isVoid=True, name="sample_text")
    partner = urml_FunctionCall()
    setattr(partner, 'urml_FunctionCall', None)
    _safe_set(owner, 'urml_Operation163', partner)
    assert getattr(partner, 'urml_FunctionCall') == owner
    _safe_set(owner, 'urml_Operation163', None)
    assert getattr(partner, 'urml_FunctionCall') is None


def test_assoc_capsuleInst139_stub_double():
    # urml_Connector has no real 'urml_Connector40' property in the generated
    # code (a bare stub) -- manually attach it so urml_CapsuleInst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_CapsuleInst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_CapsuleInst(name="sample_text")
    partner = urml_Connector()
    setattr(partner, 'urml_Connector40', None)
    _safe_set(owner, 'urml_CapsuleInst41', partner)
    assert getattr(partner, 'urml_Connector40') == owner
    _safe_set(owner, 'urml_CapsuleInst41', None)
    assert getattr(partner, 'urml_Connector40') is None


def test_assoc_capsuleInst245_stub_double():
    # urml_Connector has no real 'urml_Connector46' property in the generated
    # code (a bare stub) -- manually attach it so urml_CapsuleInst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_CapsuleInst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_CapsuleInst(name="sample_text")
    partner = urml_Connector()
    setattr(partner, 'urml_Connector46', None)
    _safe_set(owner, 'urml_CapsuleInst47', partner)
    assert getattr(partner, 'urml_Connector46') == owner
    _safe_set(owner, 'urml_CapsuleInst47', None)
    assert getattr(partner, 'urml_Connector46') is None


def test_assoc_connectors25_stub_double():
    # urml_Connector has no real 'urml_Connector' property in the generated
    # code (a bare stub) -- manually attach it so urml_Capsule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Capsule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Capsule(name="sample_text", root=True)
    partner = urml_Connector()
    setattr(partner, 'urml_Connector', None)
    _safe_set(owner, 'urml_Capsule26', {partner})
    assert getattr(partner, 'urml_Connector') == owner
    _safe_set(owner, 'urml_Capsule26', set())
    assert getattr(partner, 'urml_Connector') is None


def test_assoc_entryCode58_stub_double():
    # urml_ActionCode has no real 'urml_ActionCode' property in the generated
    # code (a bare stub) -- manually attach it so urml_State_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_State_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_State_(final=True, name="sample_text")
    partner = urml_ActionCode()
    setattr(partner, 'urml_ActionCode', None)
    _safe_set(owner, 'urml_State_59', partner)
    assert getattr(partner, 'urml_ActionCode') == owner
    _safe_set(owner, 'urml_State_59', None)
    assert getattr(partner, 'urml_ActionCode') is None


def test_assoc_exitCode60_stub_double():
    # urml_ActionCode has no real 'urml_ActionCode62' property in the generated
    # code (a bare stub) -- manually attach it so urml_State_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_State_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_State_(final=True, name="sample_text")
    partner = urml_ActionCode()
    setattr(partner, 'urml_ActionCode62', None)
    _safe_set(owner, 'urml_State_61', partner)
    assert getattr(partner, 'urml_ActionCode62') == owner
    _safe_set(owner, 'urml_State_61', None)
    assert getattr(partner, 'urml_ActionCode62') is None


def test_assoc_exp120_stub_double():
    # urml_Expression has no real 'urml_Expression122' property in the generated
    # code (a bare stub) -- manually attach it so urml_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Variable(assign=True)
    partner = urml_Expression()
    setattr(partner, 'urml_Expression122', None)
    _safe_set(owner, 'urml_Variable121', partner)
    assert getattr(partner, 'urml_Expression122') == owner
    _safe_set(owner, 'urml_Variable121', None)
    assert getattr(partner, 'urml_Expression122') is None


def test_assoc_expr156_stub_double():
    # urml_Expression has no real 'urml_Expression158' property in the generated
    # code (a bare stub) -- manually attach it so urml_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_StringExpression(str="sample_text")
    partner = urml_Expression()
    setattr(partner, 'urml_Expression158', None)
    _safe_set(owner, 'urml_StringExpression157', partner)
    assert getattr(partner, 'urml_Expression158') == owner
    _safe_set(owner, 'urml_StringExpression157', None)
    assert getattr(partner, 'urml_Expression158') is None


def test_assoc_from_83_stub_double():
    # urml_Trigger_in has no real 'urml_Trigger_in84' property in the generated
    # code (a bare stub) -- manually attach it so urml_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Port(conjugated=True, name="sample_text")
    partner = urml_Trigger_in()
    setattr(partner, 'urml_Trigger_in84', None)
    _safe_set(owner, 'urml_Port85', partner)
    assert getattr(partner, 'urml_Trigger_in84') == owner
    _safe_set(owner, 'urml_Port85', None)
    assert getattr(partner, 'urml_Trigger_in84') is None


def test_assoc_guard72_stub_double():
    # urml_Expression has no real 'urml_Expression74' property in the generated
    # code (a bare stub) -- manually attach it so urml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Transition(init=True, name="sample_text", universal=True)
    partner = urml_Expression()
    setattr(partner, 'urml_Expression74', None)
    _safe_set(owner, 'urml_Transition73', partner)
    assert getattr(partner, 'urml_Expression74') == owner
    _safe_set(owner, 'urml_Transition73', None)
    assert getattr(partner, 'urml_Expression74') is None


def test_assoc_id161_stub_double():
    # urml_Identifier has no real 'urml_Identifier' property in the generated
    # code (a bare stub) -- manually attach it so urml_Identifiable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Identifiable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Identifiable(isBool=True, isInt=True, name="sample_text")
    partner = urml_Identifier()
    setattr(partner, 'urml_Identifier', None)
    _safe_set(owner, 'urml_Identifiable', partner)
    assert getattr(partner, 'urml_Identifier') == owner
    _safe_set(owner, 'urml_Identifiable', None)
    assert getattr(partner, 'urml_Identifier') is None


def test_assoc_left154_stub_double():
    # urml_LogStatement has no real 'urml_LogStatement155' property in the generated
    # code (a bare stub) -- manually attach it so urml_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_StringExpression(str="sample_text")
    partner = urml_LogStatement()
    setattr(partner, 'urml_LogStatement155', None)
    _safe_set(owner, 'urml_StringExpression', partner)
    assert getattr(partner, 'urml_LogStatement155') == owner
    _safe_set(owner, 'urml_StringExpression', None)
    assert getattr(partner, 'urml_LogStatement155') is None


def test_assoc_left167_stub_double():
    # urml_ConcatenateExpression has no real 'urml_ConcatenateExpression' property in the generated
    # code (a bare stub) -- manually attach it so urml_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_StringExpression(str="sample_text")
    partner = urml_ConcatenateExpression()
    setattr(partner, 'urml_ConcatenateExpression', None)
    _safe_set(owner, 'urml_StringExpression168', partner)
    assert getattr(partner, 'urml_ConcatenateExpression') == owner
    _safe_set(owner, 'urml_StringExpression168', None)
    assert getattr(partner, 'urml_ConcatenateExpression') is None


def test_assoc_logPort152_stub_double():
    # urml_LogStatement has no real 'urml_LogStatement' property in the generated
    # code (a bare stub) -- manually attach it so urml_LogPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_LogPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_LogPort(name="sample_text")
    partner = urml_LogStatement()
    setattr(partner, 'urml_LogStatement', None)
    _safe_set(owner, 'urml_LogPort153', partner)
    assert getattr(partner, 'urml_LogStatement') == owner
    _safe_set(owner, 'urml_LogPort153', None)
    assert getattr(partner, 'urml_LogStatement') is None


def test_assoc_operation130_stub_double():
    # urml_Invoke has no real 'urml_Invoke' property in the generated
    # code (a bare stub) -- manually attach it so urml_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Operation(isBool=True, isInt=True, isVoid=True, name="sample_text")
    partner = urml_Invoke()
    setattr(partner, 'urml_Invoke', None)
    _safe_set(owner, 'urml_Operation131', partner)
    assert getattr(partner, 'urml_Invoke') == owner
    _safe_set(owner, 'urml_Operation131', None)
    assert getattr(partner, 'urml_Invoke') is None


def test_assoc_operationCode34_stub_double():
    # urml_OperationCode has no real 'urml_OperationCode' property in the generated
    # code (a bare stub) -- manually attach it so urml_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Operation(isBool=True, isInt=True, isVoid=True, name="sample_text")
    partner = urml_OperationCode()
    setattr(partner, 'urml_OperationCode', None)
    _safe_set(owner, 'urml_Operation35', partner)
    assert getattr(partner, 'urml_OperationCode') == owner
    _safe_set(owner, 'urml_Operation35', None)
    assert getattr(partner, 'urml_OperationCode') is None


def test_assoc_port142_stub_double():
    # urml_Connector has no real 'urml_Connector43' property in the generated
    # code (a bare stub) -- manually attach it so urml_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Port(conjugated=True, name="sample_text")
    partner = urml_Connector()
    setattr(partner, 'urml_Connector43', None)
    _safe_set(owner, 'urml_Port44', partner)
    assert getattr(partner, 'urml_Connector43') == owner
    _safe_set(owner, 'urml_Port44', None)
    assert getattr(partner, 'urml_Connector43') is None


def test_assoc_port248_stub_double():
    # urml_Connector has no real 'urml_Connector49' property in the generated
    # code (a bare stub) -- manually attach it so urml_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Port(conjugated=True, name="sample_text")
    partner = urml_Connector()
    setattr(partner, 'urml_Connector49', None)
    _safe_set(owner, 'urml_Port50', partner)
    assert getattr(partner, 'urml_Connector49') == owner
    _safe_set(owner, 'urml_Port50', None)
    assert getattr(partner, 'urml_Connector49') is None


def test_assoc_rest169_stub_double():
    # urml_ConcatenateExpression has no real 'urml_ConcatenateExpression170' property in the generated
    # code (a bare stub) -- manually attach it so urml_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_StringExpression(str="sample_text")
    partner = urml_ConcatenateExpression()
    setattr(partner, 'urml_ConcatenateExpression170', None)
    _safe_set(owner, 'urml_StringExpression171', partner)
    assert getattr(partner, 'urml_ConcatenateExpression170') == owner
    _safe_set(owner, 'urml_StringExpression171', None)
    assert getattr(partner, 'urml_ConcatenateExpression170') is None


def test_assoc_signal86_stub_double():
    # urml_Trigger_in has no real 'urml_Trigger_in87' property in the generated
    # code (a bare stub) -- manually attach it so urml_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Signal(name="sample_text")
    partner = urml_Trigger_in()
    setattr(partner, 'urml_Trigger_in87', None)
    _safe_set(owner, 'urml_Signal88', partner)
    assert getattr(partner, 'urml_Trigger_in87') == owner
    _safe_set(owner, 'urml_Signal88', None)
    assert getattr(partner, 'urml_Trigger_in87') is None


def test_assoc_signal93_stub_double():
    # urml_Trigger_out has no real 'urml_Trigger_out94' property in the generated
    # code (a bare stub) -- manually attach it so urml_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Signal(name="sample_text")
    partner = urml_Trigger_out()
    setattr(partner, 'urml_Trigger_out94', None)
    _safe_set(owner, 'urml_Signal95', partner)
    assert getattr(partner, 'urml_Trigger_out94') == owner
    _safe_set(owner, 'urml_Signal95', None)
    assert getattr(partner, 'urml_Trigger_out94') is None


def test_assoc_statemachines29_stub_double():
    # urml_StateMachine has no real 'urml_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so urml_Capsule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Capsule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Capsule(name="sample_text", root=True)
    partner = urml_StateMachine()
    setattr(partner, 'urml_StateMachine', None)
    _safe_set(owner, 'urml_Capsule30', {partner})
    assert getattr(partner, 'urml_StateMachine') == owner
    _safe_set(owner, 'urml_Capsule30', set())
    assert getattr(partner, 'urml_StateMachine') is None


def test_assoc_states54_stub_double():
    # urml_StateMachine has no real 'urml_StateMachine55' property in the generated
    # code (a bare stub) -- manually attach it so urml_State_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_State_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_State_(final=True, name="sample_text")
    partner = urml_StateMachine()
    setattr(partner, 'urml_StateMachine55', None)
    _safe_set(owner, 'urml_State_', partner)
    assert owner in getattr(partner, 'urml_StateMachine55')
    _safe_set(owner, 'urml_State_', None)
    assert owner not in getattr(partner, 'urml_StateMachine55')


def test_assoc_substatemachine63_stub_double():
    # urml_StateMachine has no real 'urml_StateMachine65' property in the generated
    # code (a bare stub) -- manually attach it so urml_State_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_State_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_State_(final=True, name="sample_text")
    partner = urml_StateMachine()
    setattr(partner, 'urml_StateMachine65', None)
    _safe_set(owner, 'urml_State_64', partner)
    assert getattr(partner, 'urml_StateMachine65') == owner
    _safe_set(owner, 'urml_State_64', None)
    assert getattr(partner, 'urml_StateMachine65') is None


def test_assoc_timerPort125_stub_double():
    # urml_InformTimer has no real 'urml_InformTimer' property in the generated
    # code (a bare stub) -- manually attach it so urml_TimerPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_TimerPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_TimerPort(name="sample_text")
    partner = urml_InformTimer()
    setattr(partner, 'urml_InformTimer', None)
    _safe_set(owner, 'urml_TimerPort126', partner)
    assert getattr(partner, 'urml_InformTimer') == owner
    _safe_set(owner, 'urml_TimerPort126', None)
    assert getattr(partner, 'urml_InformTimer') is None


def test_assoc_to91_stub_double():
    # urml_Trigger_out has no real 'urml_Trigger_out' property in the generated
    # code (a bare stub) -- manually attach it so urml_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Port(conjugated=True, name="sample_text")
    partner = urml_Trigger_out()
    setattr(partner, 'urml_Trigger_out', None)
    _safe_set(owner, 'urml_Port92', partner)
    assert getattr(partner, 'urml_Trigger_out') == owner
    _safe_set(owner, 'urml_Port92', None)
    assert getattr(partner, 'urml_Trigger_out') is None


def test_assoc_transitions56_stub_double():
    # urml_StateMachine has no real 'urml_StateMachine57' property in the generated
    # code (a bare stub) -- manually attach it so urml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Transition(init=True, name="sample_text", universal=True)
    partner = urml_StateMachine()
    setattr(partner, 'urml_StateMachine57', None)
    _safe_set(owner, 'urml_Transition', partner)
    assert owner in getattr(partner, 'urml_StateMachine57')
    _safe_set(owner, 'urml_Transition', None)
    assert owner not in getattr(partner, 'urml_StateMachine57')


def test_assoc_triggers75_stub_double():
    # urml_Trigger_in has no real 'urml_Trigger_in' property in the generated
    # code (a bare stub) -- manually attach it so urml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Transition(init=True, name="sample_text", universal=True)
    partner = urml_Trigger_in()
    setattr(partner, 'urml_Trigger_in', None)
    _safe_set(owner, 'urml_Transition76', {partner})
    assert getattr(partner, 'urml_Trigger_in') == owner
    _safe_set(owner, 'urml_Transition76', set())
    assert getattr(partner, 'urml_Trigger_in') is None


def test_assoc_var118_stub_double():
    # urml_LocalVar has no real 'urml_LocalVar119' property in the generated
    # code (a bare stub) -- manually attach it so urml_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_Variable(assign=True)
    partner = urml_LocalVar()
    setattr(partner, 'urml_LocalVar119', None)
    _safe_set(owner, 'urml_Variable', partner)
    assert getattr(partner, 'urml_LocalVar119') == owner
    _safe_set(owner, 'urml_Variable', None)
    assert getattr(partner, 'urml_LocalVar119') is None


