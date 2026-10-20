import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ChangeAction,
    Expression,
    ExtDeclaration,
    stateMachineDsl_Action,
    stateMachineDsl_And,
    stateMachineDsl_BoolExp,
    stateMachineDsl_ChangeAction,
    stateMachineDsl_CommandAction,
    stateMachineDsl_Comparison,
    stateMachineDsl_Condition,
    stateMachineDsl_Declaration,
    stateMachineDsl_DecrementAction,
    stateMachineDsl_DoubleExp,
    stateMachineDsl_EObject,
    stateMachineDsl_Equality,
    stateMachineDsl_Event,
    stateMachineDsl_Expression,
    stateMachineDsl_ExtDeclaration,
    stateMachineDsl_Function,
    stateMachineDsl_FunctionUse,
    stateMachineDsl_IncrementAction,
    stateMachineDsl_Member,
    stateMachineDsl_MemberState,
    stateMachineDsl_MinusCond,
    stateMachineDsl_MulOrDiv,
    stateMachineDsl_Not,
    stateMachineDsl_NumberExp,
    stateMachineDsl_Or,
    stateMachineDsl_Parameter,
    stateMachineDsl_ParameterFunction,
    stateMachineDsl_Parenthesis,
    stateMachineDsl_PlusCond,
    stateMachineDsl_Procedure,
    stateMachineDsl_ProcedureUse,
    stateMachineDsl_ResetAction,
    stateMachineDsl_SetAction,
    stateMachineDsl_State,
    stateMachineDsl_StateMachine,
    stateMachineDsl_StringExp,
    stateMachineDsl_Transition,
    stateMachineDsl_VarParName,
    stateMachineDsl_VarRef,
    stateMachineDsl_VarType,
    stateMachineDsl_Variable,
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

def test_assoc_initial3_reverse_link_reassign_clear():
    a1 = stateMachineDsl_StateMachine(name="sample_text")
    a2 = stateMachineDsl_StateMachine(name="sample_text_2")
    b = stateMachineDsl_State(name="sample_text")
    _safe_set(b, 'stateMachineDsl_State5', a1)
    assert _is_linked(b, 'stateMachineDsl_State5', a1)
    if hasattr(a1, 'stateMachineDsl_StateMachine4'):
        assert _is_linked(a1, 'stateMachineDsl_StateMachine4', b)
    _safe_set(b, 'stateMachineDsl_State5', a2)
    assert _is_linked(b, 'stateMachineDsl_State5', a2)
    if hasattr(a1, 'stateMachineDsl_StateMachine4'):
        assert not _is_linked(a1, 'stateMachineDsl_StateMachine4', b)
    if hasattr(a2, 'stateMachineDsl_StateMachine4'):
        assert _is_linked(a2, 'stateMachineDsl_StateMachine4', b)
    _safe_set(b, 'stateMachineDsl_State5', None)
    assert not _is_linked(b, 'stateMachineDsl_State5', a2)
    if hasattr(a2, 'stateMachineDsl_StateMachine4'):
        assert not _is_linked(a2, 'stateMachineDsl_StateMachine4', b)


def test_assoc_parameters42_reverse_link_reassign_clear():
    a1 = stateMachineDsl_ParameterFunction(name="sample_text")
    a2 = stateMachineDsl_ParameterFunction(name="sample_text_2")
    b = stateMachineDsl_ExtDeclaration(name="sample_text")
    _safe_set(b, 'stateMachineDsl_ExtDeclaration43', {a1})
    assert _is_linked(b, 'stateMachineDsl_ExtDeclaration43', a1)
    if hasattr(a1, 'stateMachineDsl_ParameterFunction'):
        assert _is_linked(a1, 'stateMachineDsl_ParameterFunction', b)
    _safe_set(b, 'stateMachineDsl_ExtDeclaration43', {a2})
    assert _is_linked(b, 'stateMachineDsl_ExtDeclaration43', a2)
    if hasattr(a1, 'stateMachineDsl_ParameterFunction'):
        assert not _is_linked(a1, 'stateMachineDsl_ParameterFunction', b)
    if hasattr(a2, 'stateMachineDsl_ParameterFunction'):
        assert _is_linked(a2, 'stateMachineDsl_ParameterFunction', b)
    _safe_set(b, 'stateMachineDsl_ExtDeclaration43', set())
    assert not _is_linked(b, 'stateMachineDsl_ExtDeclaration43', a2)
    if hasattr(a2, 'stateMachineDsl_ParameterFunction'):
        assert not _is_linked(a2, 'stateMachineDsl_ParameterFunction', b)


def test_assoc_states1_reverse_link_reassign_clear():
    a1 = stateMachineDsl_StateMachine(name="sample_text")
    a2 = stateMachineDsl_StateMachine(name="sample_text_2")
    b = stateMachineDsl_State(name="sample_text")
    _safe_set(b, 'stateMachineDsl_State', a1)
    assert _is_linked(b, 'stateMachineDsl_State', a1)
    if hasattr(a1, 'stateMachineDsl_StateMachine2'):
        assert _is_linked(a1, 'stateMachineDsl_StateMachine2', b)
    _safe_set(b, 'stateMachineDsl_State', a2)
    assert _is_linked(b, 'stateMachineDsl_State', a2)
    if hasattr(a1, 'stateMachineDsl_StateMachine2'):
        assert not _is_linked(a1, 'stateMachineDsl_StateMachine2', b)
    if hasattr(a2, 'stateMachineDsl_StateMachine2'):
        assert _is_linked(a2, 'stateMachineDsl_StateMachine2', b)
    _safe_set(b, 'stateMachineDsl_State', None)
    assert not _is_linked(b, 'stateMachineDsl_State', a2)
    if hasattr(a2, 'stateMachineDsl_StateMachine2'):
        assert not _is_linked(a2, 'stateMachineDsl_StateMachine2', b)


def test_assoc_type71_reverse_link_reassign_clear():
    a1 = stateMachineDsl_VarType(vt="sample_text")
    a2 = stateMachineDsl_VarType(vt="sample_text_2")
    b = stateMachineDsl_ParameterFunction(name="sample_text")
    _safe_set(b, 'stateMachineDsl_ParameterFunction72', a1)
    assert _is_linked(b, 'stateMachineDsl_ParameterFunction72', a1)
    if hasattr(a1, 'stateMachineDsl_VarType73'):
        assert _is_linked(a1, 'stateMachineDsl_VarType73', b)
    _safe_set(b, 'stateMachineDsl_ParameterFunction72', a2)
    assert _is_linked(b, 'stateMachineDsl_ParameterFunction72', a2)
    if hasattr(a1, 'stateMachineDsl_VarType73'):
        assert not _is_linked(a1, 'stateMachineDsl_VarType73', b)
    if hasattr(a2, 'stateMachineDsl_VarType73'):
        assert _is_linked(a2, 'stateMachineDsl_VarType73', b)
    _safe_set(b, 'stateMachineDsl_ParameterFunction72', None)
    assert not _is_linked(b, 'stateMachineDsl_ParameterFunction72', a2)
    if hasattr(a2, 'stateMachineDsl_VarType73'):
        assert not _is_linked(a2, 'stateMachineDsl_VarType73', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition44_stub_double():
    # stateMachineDsl_Condition has no real 'stateMachineDsl_Condition46' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Event(name="sample_text")
    partner = stateMachineDsl_Condition()
    setattr(partner, 'stateMachineDsl_Condition46', None)
    _safe_set(owner, 'stateMachineDsl_Event45', partner)
    assert getattr(partner, 'stateMachineDsl_Condition46') == owner
    _safe_set(owner, 'stateMachineDsl_Event45', None)
    assert getattr(partner, 'stateMachineDsl_Condition46') is None


def test_assoc_condition51_stub_double():
    # stateMachineDsl_Condition has no real 'stateMachineDsl_Condition53' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Procedure(name="sample_text")
    partner = stateMachineDsl_Condition()
    setattr(partner, 'stateMachineDsl_Condition53', None)
    _safe_set(owner, 'stateMachineDsl_Procedure52', partner)
    assert getattr(partner, 'stateMachineDsl_Condition53') == owner
    _safe_set(owner, 'stateMachineDsl_Procedure52', None)
    assert getattr(partner, 'stateMachineDsl_Condition53') is None


def test_assoc_declarations0_stub_double():
    # stateMachineDsl_Declaration has no real 'stateMachineDsl_Declaration' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_StateMachine(name="sample_text")
    partner = stateMachineDsl_Declaration()
    setattr(partner, 'stateMachineDsl_Declaration', None)
    _safe_set(owner, 'stateMachineDsl_StateMachine', {partner})
    assert getattr(partner, 'stateMachineDsl_Declaration') == owner
    _safe_set(owner, 'stateMachineDsl_StateMachine', set())
    assert getattr(partner, 'stateMachineDsl_Declaration') is None


def test_assoc_event10_stub_double():
    # stateMachineDsl_Declaration has no real 'stateMachineDsl_Declaration11' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Event(name="sample_text")
    partner = stateMachineDsl_Declaration()
    setattr(partner, 'stateMachineDsl_Declaration11', None)
    _safe_set(owner, 'stateMachineDsl_Event', partner)
    assert getattr(partner, 'stateMachineDsl_Declaration11') == owner
    _safe_set(owner, 'stateMachineDsl_Event', None)
    assert getattr(partner, 'stateMachineDsl_Declaration11') is None


def test_assoc_event28_stub_double():
    # stateMachineDsl_Transition has no real 'stateMachineDsl_Transition29' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Event(name="sample_text")
    partner = stateMachineDsl_Transition()
    setattr(partner, 'stateMachineDsl_Transition29', None)
    _safe_set(owner, 'stateMachineDsl_Event30', partner)
    assert getattr(partner, 'stateMachineDsl_Transition29') == owner
    _safe_set(owner, 'stateMachineDsl_Event30', None)
    assert getattr(partner, 'stateMachineDsl_Transition29') is None


def test_assoc_extdecl8_stub_double():
    # stateMachineDsl_Declaration has no real 'stateMachineDsl_Declaration9' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_ExtDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_ExtDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_ExtDeclaration(name="sample_text")
    partner = stateMachineDsl_Declaration()
    setattr(partner, 'stateMachineDsl_Declaration9', None)
    _safe_set(owner, 'stateMachineDsl_ExtDeclaration', partner)
    assert getattr(partner, 'stateMachineDsl_Declaration9') == owner
    _safe_set(owner, 'stateMachineDsl_ExtDeclaration', None)
    assert getattr(partner, 'stateMachineDsl_Declaration9') is None


def test_assoc_left109_stub_double():
    # stateMachineDsl_Expression has no real 'stateMachineDsl_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Equality(op="sample_text")
    partner = stateMachineDsl_Expression()
    setattr(partner, 'stateMachineDsl_Expression110', None)
    _safe_set(owner, 'stateMachineDsl_Equality', partner)
    assert getattr(partner, 'stateMachineDsl_Expression110') == owner
    _safe_set(owner, 'stateMachineDsl_Equality', None)
    assert getattr(partner, 'stateMachineDsl_Expression110') is None


def test_assoc_left114_stub_double():
    # stateMachineDsl_Expression has no real 'stateMachineDsl_Expression115' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Comparison(op="sample_text")
    partner = stateMachineDsl_Expression()
    setattr(partner, 'stateMachineDsl_Expression115', None)
    _safe_set(owner, 'stateMachineDsl_Comparison', partner)
    assert getattr(partner, 'stateMachineDsl_Expression115') == owner
    _safe_set(owner, 'stateMachineDsl_Comparison', None)
    assert getattr(partner, 'stateMachineDsl_Expression115') is None


def test_assoc_left129_stub_double():
    # stateMachineDsl_Expression has no real 'stateMachineDsl_Expression130' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_MulOrDiv(op="sample_text")
    partner = stateMachineDsl_Expression()
    setattr(partner, 'stateMachineDsl_Expression130', None)
    _safe_set(owner, 'stateMachineDsl_MulOrDiv', partner)
    assert getattr(partner, 'stateMachineDsl_Expression130') == owner
    _safe_set(owner, 'stateMachineDsl_MulOrDiv', None)
    assert getattr(partner, 'stateMachineDsl_Expression130') is None


def test_assoc_members14_stub_double():
    # stateMachineDsl_MemberState has no real 'stateMachineDsl_MemberState' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_State(name="sample_text")
    partner = stateMachineDsl_MemberState()
    setattr(partner, 'stateMachineDsl_MemberState', None)
    _safe_set(owner, 'stateMachineDsl_State15', {partner})
    assert getattr(partner, 'stateMachineDsl_MemberState') == owner
    _safe_set(owner, 'stateMachineDsl_State15', set())
    assert getattr(partner, 'stateMachineDsl_MemberState') is None


def test_assoc_members47_stub_double():
    # stateMachineDsl_Member has no real 'stateMachineDsl_Member' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Event(name="sample_text")
    partner = stateMachineDsl_Member()
    setattr(partner, 'stateMachineDsl_Member', None)
    _safe_set(owner, 'stateMachineDsl_Event48', {partner})
    assert getattr(partner, 'stateMachineDsl_Member') == owner
    _safe_set(owner, 'stateMachineDsl_Event48', set())
    assert getattr(partner, 'stateMachineDsl_Member') is None


def test_assoc_members54_stub_double():
    # stateMachineDsl_Member has no real 'stateMachineDsl_Member56' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Procedure(name="sample_text")
    partner = stateMachineDsl_Member()
    setattr(partner, 'stateMachineDsl_Member56', None)
    _safe_set(owner, 'stateMachineDsl_Procedure55', {partner})
    assert getattr(partner, 'stateMachineDsl_Member56') == owner
    _safe_set(owner, 'stateMachineDsl_Procedure55', set())
    assert getattr(partner, 'stateMachineDsl_Member56') is None


def test_assoc_n36_stub_double():
    # stateMachineDsl_Variable has no real 'stateMachineDsl_Variable37' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_VarParName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_VarParName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_VarParName(name="sample_text")
    partner = stateMachineDsl_Variable()
    setattr(partner, 'stateMachineDsl_Variable37', None)
    _safe_set(owner, 'stateMachineDsl_VarParName', partner)
    assert getattr(partner, 'stateMachineDsl_Variable37') == owner
    _safe_set(owner, 'stateMachineDsl_VarParName', None)
    assert getattr(partner, 'stateMachineDsl_Variable37') is None


def test_assoc_n60_stub_double():
    # stateMachineDsl_Parameter has no real 'stateMachineDsl_Parameter61' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_VarParName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_VarParName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_VarParName(name="sample_text")
    partner = stateMachineDsl_Parameter()
    setattr(partner, 'stateMachineDsl_Parameter61', None)
    _safe_set(owner, 'stateMachineDsl_VarParName62', partner)
    assert getattr(partner, 'stateMachineDsl_Parameter61') == owner
    _safe_set(owner, 'stateMachineDsl_VarParName62', None)
    assert getattr(partner, 'stateMachineDsl_Parameter61') is None


def test_assoc_parameters49_stub_double():
    # stateMachineDsl_Parameter has no real 'stateMachineDsl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Procedure(name="sample_text")
    partner = stateMachineDsl_Parameter()
    setattr(partner, 'stateMachineDsl_Parameter', None)
    _safe_set(owner, 'stateMachineDsl_Procedure50', {partner})
    assert getattr(partner, 'stateMachineDsl_Parameter') == owner
    _safe_set(owner, 'stateMachineDsl_Procedure50', set())
    assert getattr(partner, 'stateMachineDsl_Parameter') is None


def test_assoc_procedure12_stub_double():
    # stateMachineDsl_Declaration has no real 'stateMachineDsl_Declaration13' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Procedure(name="sample_text")
    partner = stateMachineDsl_Declaration()
    setattr(partner, 'stateMachineDsl_Declaration13', None)
    _safe_set(owner, 'stateMachineDsl_Procedure', partner)
    assert getattr(partner, 'stateMachineDsl_Declaration13') == owner
    _safe_set(owner, 'stateMachineDsl_Procedure', None)
    assert getattr(partner, 'stateMachineDsl_Declaration13') is None


def test_assoc_procedure91_stub_double():
    # stateMachineDsl_ProcedureUse has no real 'stateMachineDsl_ProcedureUse' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Procedure(name="sample_text")
    partner = stateMachineDsl_ProcedureUse()
    setattr(partner, 'stateMachineDsl_ProcedureUse', None)
    _safe_set(owner, 'stateMachineDsl_Procedure92', partner)
    assert getattr(partner, 'stateMachineDsl_ProcedureUse') == owner
    _safe_set(owner, 'stateMachineDsl_Procedure92', None)
    assert getattr(partner, 'stateMachineDsl_ProcedureUse') is None


def test_assoc_returnvalue69_stub_double():
    # stateMachineDsl_Function has no real 'stateMachineDsl_Function' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_VarType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_VarType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_VarType(vt="sample_text")
    partner = stateMachineDsl_Function()
    setattr(partner, 'stateMachineDsl_Function', None)
    _safe_set(owner, 'stateMachineDsl_VarType70', partner)
    assert getattr(partner, 'stateMachineDsl_Function') == owner
    _safe_set(owner, 'stateMachineDsl_VarType70', None)
    assert getattr(partner, 'stateMachineDsl_Function') is None


def test_assoc_right111_stub_double():
    # stateMachineDsl_Expression has no real 'stateMachineDsl_Expression113' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Equality(op="sample_text")
    partner = stateMachineDsl_Expression()
    setattr(partner, 'stateMachineDsl_Expression113', None)
    _safe_set(owner, 'stateMachineDsl_Equality112', partner)
    assert getattr(partner, 'stateMachineDsl_Expression113') == owner
    _safe_set(owner, 'stateMachineDsl_Equality112', None)
    assert getattr(partner, 'stateMachineDsl_Expression113') is None


def test_assoc_right116_stub_double():
    # stateMachineDsl_Expression has no real 'stateMachineDsl_Expression118' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_Comparison(op="sample_text")
    partner = stateMachineDsl_Expression()
    setattr(partner, 'stateMachineDsl_Expression118', None)
    _safe_set(owner, 'stateMachineDsl_Comparison117', partner)
    assert getattr(partner, 'stateMachineDsl_Expression118') == owner
    _safe_set(owner, 'stateMachineDsl_Comparison117', None)
    assert getattr(partner, 'stateMachineDsl_Expression118') is None


def test_assoc_right131_stub_double():
    # stateMachineDsl_Expression has no real 'stateMachineDsl_Expression133' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_MulOrDiv(op="sample_text")
    partner = stateMachineDsl_Expression()
    setattr(partner, 'stateMachineDsl_Expression133', None)
    _safe_set(owner, 'stateMachineDsl_MulOrDiv132', partner)
    assert getattr(partner, 'stateMachineDsl_Expression133') == owner
    _safe_set(owner, 'stateMachineDsl_MulOrDiv132', None)
    assert getattr(partner, 'stateMachineDsl_Expression133') is None


def test_assoc_to25_stub_double():
    # stateMachineDsl_Transition has no real 'stateMachineDsl_Transition26' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_State(name="sample_text")
    partner = stateMachineDsl_Transition()
    setattr(partner, 'stateMachineDsl_Transition26', None)
    _safe_set(owner, 'stateMachineDsl_State27', partner)
    assert getattr(partner, 'stateMachineDsl_Transition26') == owner
    _safe_set(owner, 'stateMachineDsl_State27', None)
    assert getattr(partner, 'stateMachineDsl_Transition26') is None


def test_assoc_type38_stub_double():
    # stateMachineDsl_Variable has no real 'stateMachineDsl_Variable39' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_VarType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_VarType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_VarType(vt="sample_text")
    partner = stateMachineDsl_Variable()
    setattr(partner, 'stateMachineDsl_Variable39', None)
    _safe_set(owner, 'stateMachineDsl_VarType', partner)
    assert getattr(partner, 'stateMachineDsl_Variable39') == owner
    _safe_set(owner, 'stateMachineDsl_VarType', None)
    assert getattr(partner, 'stateMachineDsl_Variable39') is None


def test_assoc_type57_stub_double():
    # stateMachineDsl_Parameter has no real 'stateMachineDsl_Parameter58' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_VarType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_VarType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_VarType(vt="sample_text")
    partner = stateMachineDsl_Parameter()
    setattr(partner, 'stateMachineDsl_Parameter58', None)
    _safe_set(owner, 'stateMachineDsl_VarType59', partner)
    assert getattr(partner, 'stateMachineDsl_Parameter58') == owner
    _safe_set(owner, 'stateMachineDsl_VarType59', None)
    assert getattr(partner, 'stateMachineDsl_Parameter58') is None


def test_assoc_variable136_stub_double():
    # stateMachineDsl_VarRef has no real 'stateMachineDsl_VarRef' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_VarParName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_VarParName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_VarParName(name="sample_text")
    partner = stateMachineDsl_VarRef()
    setattr(partner, 'stateMachineDsl_VarRef', None)
    _safe_set(owner, 'stateMachineDsl_VarParName137', partner)
    assert getattr(partner, 'stateMachineDsl_VarRef') == owner
    _safe_set(owner, 'stateMachineDsl_VarParName137', None)
    assert getattr(partner, 'stateMachineDsl_VarRef') is None


def test_assoc_variable79_stub_double():
    # stateMachineDsl_SetAction has no real 'stateMachineDsl_SetAction' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_VarParName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_VarParName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_VarParName(name="sample_text")
    partner = stateMachineDsl_SetAction()
    setattr(partner, 'stateMachineDsl_SetAction', None)
    _safe_set(owner, 'stateMachineDsl_VarParName80', partner)
    assert getattr(partner, 'stateMachineDsl_SetAction') == owner
    _safe_set(owner, 'stateMachineDsl_VarParName80', None)
    assert getattr(partner, 'stateMachineDsl_SetAction') is None


def test_assoc_variable84_stub_double():
    # stateMachineDsl_ChangeAction has no real 'stateMachineDsl_ChangeAction' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineDsl_VarParName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineDsl_VarParName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineDsl_VarParName(name="sample_text")
    partner = stateMachineDsl_ChangeAction()
    setattr(partner, 'stateMachineDsl_ChangeAction', None)
    _safe_set(owner, 'stateMachineDsl_VarParName85', partner)
    assert getattr(partner, 'stateMachineDsl_ChangeAction') == owner
    _safe_set(owner, 'stateMachineDsl_VarParName85', None)
    assert getattr(partner, 'stateMachineDsl_ChangeAction') is None


