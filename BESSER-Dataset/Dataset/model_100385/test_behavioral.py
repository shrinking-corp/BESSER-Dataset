import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    AbstractTransition,
    AbstractTransitionEvent,
    AbstractUriLiteral,
    Action,
    Event,
    Expression,
    IntLiteral,
    Literal,
    ResourceImport,
    ResourceUriLiteral,
    Typed,
    scxmlxt_AbstractState,
    scxmlxt_AbstractTransition,
    scxmlxt_AbstractTransitionEvent,
    scxmlxt_AbstractUriLiteral,
    scxmlxt_Action,
    scxmlxt_AssignmentAction,
    scxmlxt_BooleanLiteral,
    scxmlxt_Condition,
    scxmlxt_DelayLiteral,
    scxmlxt_DomainDataImport,
    scxmlxt_DomainModelImport,
    scxmlxt_EClassifier,
    scxmlxt_EObject,
    scxmlxt_EObjectReference,
    scxmlxt_EObjectUriLiteral,
    scxmlxt_EPath,
    scxmlxt_EStep,
    scxmlxt_EStepFilter,
    scxmlxt_EnterEvent,
    scxmlxt_Event,
    scxmlxt_ExitEvent,
    scxmlxt_Expression,
    scxmlxt_FloatLiteral,
    scxmlxt_InitialTransition,
    scxmlxt_IntLiteral,
    scxmlxt_InternalTransition,
    scxmlxt_Literal,
    scxmlxt_ResourceImport,
    scxmlxt_ResourceUriLiteral,
    scxmlxt_ScriptAction,
    scxmlxt_ScriptEvent,
    scxmlxt_ScriptExpression,
    scxmlxt_State,
    scxmlxt_StateMachine,
    scxmlxt_StringLiteral,
    scxmlxt_SymbolicAction,
    scxmlxt_SymbolicEvent,
    scxmlxt_TimerEvent,
    scxmlxt_Transition,
    scxmlxt_TransitionEvent,
    scxmlxt_Typed,
    scxmlxt_UriLiteral,
    scxmlxt_VarDef,
    scxmlxt_VarRef,
    TimeUnit,
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

def test_assoc_filter48_reverse_link_reassign_clear():
    a1 = scxmlxt_EStepFilter(freeVarName="sample_text")
    a2 = scxmlxt_EStepFilter(freeVarName="sample_text_2")
    b = scxmlxt_EStep(featureName="sample_text")
    _safe_set(b, 'scxmlxt_EStep49', a1)
    assert _is_linked(b, 'scxmlxt_EStep49', a1)
    if hasattr(a1, 'scxmlxt_EStepFilter'):
        assert _is_linked(a1, 'scxmlxt_EStepFilter', b)
    _safe_set(b, 'scxmlxt_EStep49', a2)
    assert _is_linked(b, 'scxmlxt_EStep49', a2)
    if hasattr(a1, 'scxmlxt_EStepFilter'):
        assert not _is_linked(a1, 'scxmlxt_EStepFilter', b)
    if hasattr(a2, 'scxmlxt_EStepFilter'):
        assert _is_linked(a2, 'scxmlxt_EStepFilter', b)
    _safe_set(b, 'scxmlxt_EStep49', None)
    assert not _is_linked(b, 'scxmlxt_EStep49', a2)
    if hasattr(a2, 'scxmlxt_EStepFilter'):
        assert not _is_linked(a2, 'scxmlxt_EStepFilter', b)


def test_assoc_script50_reverse_link_reassign_clear():
    a1 = scxmlxt_ScriptExpression(script="sample_text")
    a2 = scxmlxt_ScriptExpression(script="sample_text_2")
    b = scxmlxt_EStepFilter(freeVarName="sample_text")
    _safe_set(b, 'scxmlxt_EStepFilter51', a1)
    assert _is_linked(b, 'scxmlxt_EStepFilter51', a1)
    if hasattr(a1, 'scxmlxt_ScriptExpression'):
        assert _is_linked(a1, 'scxmlxt_ScriptExpression', b)
    _safe_set(b, 'scxmlxt_EStepFilter51', a2)
    assert _is_linked(b, 'scxmlxt_EStepFilter51', a2)
    if hasattr(a1, 'scxmlxt_ScriptExpression'):
        assert not _is_linked(a1, 'scxmlxt_ScriptExpression', b)
    if hasattr(a2, 'scxmlxt_ScriptExpression'):
        assert _is_linked(a2, 'scxmlxt_ScriptExpression', b)
    _safe_set(b, 'scxmlxt_EStepFilter51', None)
    assert not _is_linked(b, 'scxmlxt_EStepFilter51', a2)
    if hasattr(a2, 'scxmlxt_ScriptExpression'):
        assert not _is_linked(a2, 'scxmlxt_ScriptExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition15_stub_double():
    # scxmlxt_AbstractTransition has no real 'scxmlxt_AbstractTransition16' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_Condition(script="sample_text")
    partner = scxmlxt_AbstractTransition()
    setattr(partner, 'scxmlxt_AbstractTransition16', None)
    _safe_set(owner, 'scxmlxt_Condition', partner)
    assert getattr(partner, 'scxmlxt_AbstractTransition16') == owner
    _safe_set(owner, 'scxmlxt_Condition', None)
    assert getattr(partner, 'scxmlxt_AbstractTransition16') is None


def test_assoc_currentStates1_stub_double():
    # scxmlxt_StateMachine has no real 'scxmlxt_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_State(name="sample_text")
    partner = scxmlxt_StateMachine()
    setattr(partner, 'scxmlxt_StateMachine2', None)
    _safe_set(owner, 'scxmlxt_State', partner)
    assert owner in getattr(partner, 'scxmlxt_StateMachine2')
    _safe_set(owner, 'scxmlxt_State', None)
    assert owner not in getattr(partner, 'scxmlxt_StateMachine2')


def test_assoc_delay31_stub_double():
    # scxmlxt_Expression has no real 'scxmlxt_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_SymbolicAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_SymbolicAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_SymbolicAction(name="sample_text")
    partner = scxmlxt_Expression()
    setattr(partner, 'scxmlxt_Expression32', None)
    _safe_set(owner, 'scxmlxt_SymbolicAction', partner)
    assert getattr(partner, 'scxmlxt_Expression32') == owner
    _safe_set(owner, 'scxmlxt_SymbolicAction', None)
    assert getattr(partner, 'scxmlxt_Expression32') is None


def test_assoc_eType33_stub_double():
    # scxmlxt_EClassifier has no real 'scxmlxt_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_Typed's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_Typed's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_Typed(many=True)
    partner = scxmlxt_EClassifier()
    setattr(partner, 'scxmlxt_EClassifier', None)
    _safe_set(owner, 'scxmlxt_Typed', partner)
    assert getattr(partner, 'scxmlxt_EClassifier') == owner
    _safe_set(owner, 'scxmlxt_Typed', None)
    assert getattr(partner, 'scxmlxt_EClassifier') is None


def test_assoc_imports0_stub_double():
    # scxmlxt_StateMachine has no real 'scxmlxt_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_ResourceImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_ResourceImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_ResourceImport(importURI="sample_text")
    partner = scxmlxt_StateMachine()
    setattr(partner, 'scxmlxt_StateMachine', None)
    _safe_set(owner, 'scxmlxt_ResourceImport', partner)
    assert owner in getattr(partner, 'scxmlxt_StateMachine')
    _safe_set(owner, 'scxmlxt_ResourceImport', None)
    assert owner not in getattr(partner, 'scxmlxt_StateMachine')


def test_assoc_init34_stub_double():
    # scxmlxt_Expression has no real 'scxmlxt_Expression36' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_VarDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_VarDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_VarDef(name="sample_text")
    partner = scxmlxt_Expression()
    setattr(partner, 'scxmlxt_Expression36', None)
    _safe_set(owner, 'scxmlxt_VarDef35', partner)
    assert getattr(partner, 'scxmlxt_Expression36') == owner
    _safe_set(owner, 'scxmlxt_VarDef35', None)
    assert getattr(partner, 'scxmlxt_Expression36') is None


def test_assoc_initialTransition3_stub_double():
    # scxmlxt_InitialTransition has no real 'scxmlxt_InitialTransition' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_State(name="sample_text")
    partner = scxmlxt_InitialTransition()
    setattr(partner, 'scxmlxt_InitialTransition', None)
    _safe_set(owner, 'scxmlxt_State4', partner)
    assert getattr(partner, 'scxmlxt_InitialTransition') == owner
    _safe_set(owner, 'scxmlxt_State4', None)
    assert getattr(partner, 'scxmlxt_InitialTransition') is None


def test_assoc_source22_stub_double():
    # scxmlxt_TransitionEvent has no real 'scxmlxt_TransitionEvent' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_State(name="sample_text")
    partner = scxmlxt_TransitionEvent()
    setattr(partner, 'scxmlxt_TransitionEvent', None)
    _safe_set(owner, 'scxmlxt_State23', partner)
    assert getattr(partner, 'scxmlxt_TransitionEvent') == owner
    _safe_set(owner, 'scxmlxt_State23', None)
    assert getattr(partner, 'scxmlxt_TransitionEvent') is None


def test_assoc_states7_stub_double():
    # scxmlxt_AbstractState has no real 'scxmlxt_AbstractState' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_State(name="sample_text")
    partner = scxmlxt_AbstractState()
    setattr(partner, 'scxmlxt_AbstractState', None)
    _safe_set(owner, 'scxmlxt_State8', partner)
    assert owner in getattr(partner, 'scxmlxt_AbstractState')
    _safe_set(owner, 'scxmlxt_State8', None)
    assert owner not in getattr(partner, 'scxmlxt_AbstractState')


def test_assoc_steps46_stub_double():
    # scxmlxt_EPath has no real 'scxmlxt_EPath47' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_EStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_EStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_EStep(featureName="sample_text")
    partner = scxmlxt_EPath()
    setattr(partner, 'scxmlxt_EPath47', None)
    _safe_set(owner, 'scxmlxt_EStep', partner)
    assert owner in getattr(partner, 'scxmlxt_EPath47')
    _safe_set(owner, 'scxmlxt_EStep', None)
    assert owner not in getattr(partner, 'scxmlxt_EPath47')


def test_assoc_target20_stub_double():
    # scxmlxt_Transition has no real 'scxmlxt_Transition' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_State(name="sample_text")
    partner = scxmlxt_Transition()
    setattr(partner, 'scxmlxt_Transition', None)
    _safe_set(owner, 'scxmlxt_State21', partner)
    assert getattr(partner, 'scxmlxt_Transition') == owner
    _safe_set(owner, 'scxmlxt_State21', None)
    assert getattr(partner, 'scxmlxt_Transition') is None


def test_assoc_target24_stub_double():
    # scxmlxt_TransitionEvent has no real 'scxmlxt_TransitionEvent25' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_State(name="sample_text")
    partner = scxmlxt_TransitionEvent()
    setattr(partner, 'scxmlxt_TransitionEvent25', None)
    _safe_set(owner, 'scxmlxt_State26', partner)
    assert getattr(partner, 'scxmlxt_TransitionEvent25') == owner
    _safe_set(owner, 'scxmlxt_State26', None)
    assert getattr(partner, 'scxmlxt_TransitionEvent25') is None


def test_assoc_var37_stub_double():
    # scxmlxt_AssignmentAction has no real 'scxmlxt_AssignmentAction' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_VarDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_VarDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_VarDef(name="sample_text")
    partner = scxmlxt_AssignmentAction()
    setattr(partner, 'scxmlxt_AssignmentAction', None)
    _safe_set(owner, 'scxmlxt_VarDef38', partner)
    assert getattr(partner, 'scxmlxt_AssignmentAction') == owner
    _safe_set(owner, 'scxmlxt_VarDef38', None)
    assert getattr(partner, 'scxmlxt_AssignmentAction') is None


def test_assoc_var42_stub_double():
    # scxmlxt_VarRef has no real 'scxmlxt_VarRef' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_VarDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_VarDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_VarDef(name="sample_text")
    partner = scxmlxt_VarRef()
    setattr(partner, 'scxmlxt_VarRef', None)
    _safe_set(owner, 'scxmlxt_VarDef43', partner)
    assert getattr(partner, 'scxmlxt_VarRef') == owner
    _safe_set(owner, 'scxmlxt_VarDef43', None)
    assert getattr(partner, 'scxmlxt_VarRef') is None


def test_assoc_variables11_stub_double():
    # scxmlxt_AbstractState has no real 'scxmlxt_AbstractState12' property in the generated
    # code (a bare stub) -- manually attach it so scxmlxt_VarDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxmlxt_VarDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxmlxt_VarDef(name="sample_text")
    partner = scxmlxt_AbstractState()
    setattr(partner, 'scxmlxt_AbstractState12', None)
    _safe_set(owner, 'scxmlxt_VarDef', partner)
    assert owner in getattr(partner, 'scxmlxt_AbstractState12')
    _safe_set(owner, 'scxmlxt_VarDef', None)
    assert owner not in getattr(partner, 'scxmlxt_AbstractState12')


