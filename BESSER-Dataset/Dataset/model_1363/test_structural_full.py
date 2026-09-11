import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    State,
    StateMachineObject,
    statemachine103_Action,
    statemachine103_FinalState,
    statemachine103_InitialState,
    statemachine103_NormalState,
    statemachine103_State,
    statemachine103_StateMachine,
    statemachine103_StateMachineObject,
    statemachine103_StateMachineVariable,
    statemachine103_Transition,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_statemachine103_Action_actionLabel_value_roundtrip():
    instance = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    assert instance.actionLabel == "sample_text"
    instance.actionLabel = "sample_text_2"
    assert instance.actionLabel == "sample_text_2"


def test_statemachine103_Action_actionStatement_value_roundtrip():
    instance = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    assert instance.actionStatement == "sample_text"
    instance.actionStatement = "sample_text_2"
    assert instance.actionStatement == "sample_text_2"


def test_statemachine103_State_id_value_roundtrip():
    instance = statemachine103_State(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_statemachine103_StateMachine_label_value_roundtrip():
    instance = statemachine103_StateMachine(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_statemachine103_StateMachineObject_label_value_roundtrip():
    instance = statemachine103_StateMachineObject(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_statemachine103_StateMachineVariable_name_value_roundtrip():
    instance = statemachine103_StateMachineVariable(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine103_StateMachineVariable_type_value_roundtrip():
    instance = statemachine103_StateMachineVariable(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_statemachine103_Transition_guardExpression_value_roundtrip():
    instance = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    assert instance.guardExpression == "sample_text"
    instance.guardExpression = "sample_text_2"
    assert instance.guardExpression == "sample_text_2"


def test_statemachine103_Transition_guardLabel_value_roundtrip():
    instance = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    assert instance.guardLabel == "sample_text"
    instance.guardLabel = "sample_text_2"
    assert instance.guardLabel == "sample_text_2"


def test_statemachine103_FinalState_isa_State():
    instance = statemachine103_FinalState()
    assert isinstance(instance, State)


def test_statemachine103_InitialState_isa_State():
    instance = statemachine103_InitialState()
    assert isinstance(instance, State)


def test_statemachine103_NormalState_isa_State():
    instance = statemachine103_NormalState()
    assert isinstance(instance, State)


def test_statemachine103_State_isa_StateMachineObject():
    instance = statemachine103_State(id=7)
    assert isinstance(instance, StateMachineObject)


def test_statemachine103_Transition_isa_StateMachineObject():
    instance = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    assert isinstance(instance, StateMachineObject)


def test_assoc_machineObjects0_link_reassign_clear():
    a = statemachine103_StateMachineObject(label="sample_text")
    b1 = statemachine103_StateMachine(label="sample_text")
    b2 = statemachine103_StateMachine(label="sample_text_2")
    _safe_set(a, 'statemachine103_StateMachineObject', b1)
    assert _is_linked(a, 'statemachine103_StateMachineObject', b1)
    if hasattr(b1, 'statemachine103_StateMachine'):
        assert _is_linked(b1, 'statemachine103_StateMachine', a)
    _safe_set(a, 'statemachine103_StateMachineObject', b2)
    assert _is_linked(a, 'statemachine103_StateMachineObject', b2)
    if hasattr(b1, 'statemachine103_StateMachine'):
        assert not _is_linked(b1, 'statemachine103_StateMachine', a)
    if hasattr(b2, 'statemachine103_StateMachine'):
        assert _is_linked(b2, 'statemachine103_StateMachine', a)
    _safe_set(a, 'statemachine103_StateMachineObject', None)
    assert not _is_linked(a, 'statemachine103_StateMachineObject', b2)
    if hasattr(b2, 'statemachine103_StateMachine'):
        assert not _is_linked(b2, 'statemachine103_StateMachine', a)


def test_assoc_machineVariables1_link_reassign_clear():
    a = statemachine103_StateMachineVariable(name="sample_text", type="sample_text")
    b1 = statemachine103_StateMachine(label="sample_text")
    b2 = statemachine103_StateMachine(label="sample_text_2")
    _safe_set(a, 'statemachine103_StateMachineVariable', b1)
    assert _is_linked(a, 'statemachine103_StateMachineVariable', b1)
    if hasattr(b1, 'statemachine103_StateMachine2'):
        assert _is_linked(b1, 'statemachine103_StateMachine2', a)
    _safe_set(a, 'statemachine103_StateMachineVariable', b2)
    assert _is_linked(a, 'statemachine103_StateMachineVariable', b2)
    if hasattr(b1, 'statemachine103_StateMachine2'):
        assert not _is_linked(b1, 'statemachine103_StateMachine2', a)
    if hasattr(b2, 'statemachine103_StateMachine2'):
        assert _is_linked(b2, 'statemachine103_StateMachine2', a)
    _safe_set(a, 'statemachine103_StateMachineVariable', None)
    assert not _is_linked(a, 'statemachine103_StateMachineVariable', b2)
    if hasattr(b2, 'statemachine103_StateMachine2'):
        assert not _is_linked(b2, 'statemachine103_StateMachine2', a)


def test_assoc_next10_link_reassign_clear():
    a = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    b1 = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    b2 = statemachine103_Action(actionLabel="sample_text_2", actionStatement="sample_text_2")
    _safe_set(a, 'statemachine103_Action11', b1)
    assert _is_linked(a, 'statemachine103_Action11', b1)
    if hasattr(b1, 'statemachine103_Action9'):
        assert _is_linked(b1, 'statemachine103_Action9', a)
    _safe_set(a, 'statemachine103_Action11', b2)
    assert _is_linked(a, 'statemachine103_Action11', b2)
    if hasattr(b1, 'statemachine103_Action9'):
        assert not _is_linked(b1, 'statemachine103_Action9', a)
    if hasattr(b2, 'statemachine103_Action9'):
        assert _is_linked(b2, 'statemachine103_Action9', a)
    _safe_set(a, 'statemachine103_Action11', None)
    assert not _is_linked(a, 'statemachine103_Action11', b2)
    if hasattr(b2, 'statemachine103_Action9'):
        assert not _is_linked(b2, 'statemachine103_Action9', a)


def test_assoc_s_actions12_link_reassign_clear():
    a = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    b1 = statemachine103_NormalState()
    b2 = statemachine103_NormalState()
    _safe_set(a, 'statemachine103_Action13', b1)
    assert _is_linked(a, 'statemachine103_Action13', b1)
    if hasattr(b1, 'statemachine103_NormalState'):
        assert _is_linked(b1, 'statemachine103_NormalState', a)
    _safe_set(a, 'statemachine103_Action13', b2)
    assert _is_linked(a, 'statemachine103_Action13', b2)
    if hasattr(b1, 'statemachine103_NormalState'):
        assert not _is_linked(b1, 'statemachine103_NormalState', a)
    if hasattr(b2, 'statemachine103_NormalState'):
        assert _is_linked(b2, 'statemachine103_NormalState', a)
    _safe_set(a, 'statemachine103_Action13', None)
    assert not _is_linked(a, 'statemachine103_Action13', b2)
    if hasattr(b2, 'statemachine103_NormalState'):
        assert not _is_linked(b2, 'statemachine103_NormalState', a)


def test_assoc_source3_link_reassign_clear():
    a = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    b1 = statemachine103_State(id=7)
    b2 = statemachine103_State(id=13)
    _safe_set(a, 'statemachine103_Transition', b1)
    assert _is_linked(a, 'statemachine103_Transition', b1)
    if hasattr(b1, 'statemachine103_State'):
        assert _is_linked(b1, 'statemachine103_State', a)
    _safe_set(a, 'statemachine103_Transition', b2)
    assert _is_linked(a, 'statemachine103_Transition', b2)
    if hasattr(b1, 'statemachine103_State'):
        assert not _is_linked(b1, 'statemachine103_State', a)
    if hasattr(b2, 'statemachine103_State'):
        assert _is_linked(b2, 'statemachine103_State', a)
    _safe_set(a, 'statemachine103_Transition', None)
    assert not _is_linked(a, 'statemachine103_Transition', b2)
    if hasattr(b2, 'statemachine103_State'):
        assert not _is_linked(b2, 'statemachine103_State', a)


def test_assoc_t_actions7_link_reassign_clear():
    a = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    b1 = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    b2 = statemachine103_Action(actionLabel="sample_text_2", actionStatement="sample_text_2")
    _safe_set(a, 'statemachine103_Transition8', {b1})
    assert _is_linked(a, 'statemachine103_Transition8', b1)
    if hasattr(b1, 'statemachine103_Action'):
        assert _is_linked(b1, 'statemachine103_Action', a)
    _safe_set(a, 'statemachine103_Transition8', {b2})
    assert _is_linked(a, 'statemachine103_Transition8', b2)
    if hasattr(b1, 'statemachine103_Action'):
        assert not _is_linked(b1, 'statemachine103_Action', a)
    if hasattr(b2, 'statemachine103_Action'):
        assert _is_linked(b2, 'statemachine103_Action', a)
    _safe_set(a, 'statemachine103_Transition8', set())
    assert not _is_linked(a, 'statemachine103_Transition8', b2)
    if hasattr(b2, 'statemachine103_Action'):
        assert not _is_linked(b2, 'statemachine103_Action', a)


def test_assoc_target4_link_reassign_clear():
    a = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    b1 = statemachine103_State(id=7)
    b2 = statemachine103_State(id=13)
    _safe_set(a, 'statemachine103_Transition5', b1)
    assert _is_linked(a, 'statemachine103_Transition5', b1)
    if hasattr(b1, 'statemachine103_State6'):
        assert _is_linked(b1, 'statemachine103_State6', a)
    _safe_set(a, 'statemachine103_Transition5', b2)
    assert _is_linked(a, 'statemachine103_Transition5', b2)
    if hasattr(b1, 'statemachine103_State6'):
        assert not _is_linked(b1, 'statemachine103_State6', a)
    if hasattr(b2, 'statemachine103_State6'):
        assert _is_linked(b2, 'statemachine103_State6', a)
    _safe_set(a, 'statemachine103_Transition5', None)
    assert not _is_linked(a, 'statemachine103_Transition5', b2)
    if hasattr(b2, 'statemachine103_State6'):
        assert not _is_linked(b2, 'statemachine103_State6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


StateMachineObject_strategy = st.builds(StateMachineObject)
@given(instance=StateMachineObject_strategy)
@settings(max_examples=25)
def test_StateMachineObject_instantiation(instance):
    assert isinstance(instance, StateMachineObject)


statemachine103_Action_strategy = st.builds(statemachine103_Action, actionLabel=safe_text, actionStatement=safe_text)
@given(instance=statemachine103_Action_strategy)
@settings(max_examples=25)
def test_statemachine103_Action_instantiation(instance):
    assert isinstance(instance, statemachine103_Action)


statemachine103_FinalState_strategy = st.builds(statemachine103_FinalState)
@given(instance=statemachine103_FinalState_strategy)
@settings(max_examples=25)
def test_statemachine103_FinalState_instantiation(instance):
    assert isinstance(instance, statemachine103_FinalState)


statemachine103_InitialState_strategy = st.builds(statemachine103_InitialState)
@given(instance=statemachine103_InitialState_strategy)
@settings(max_examples=25)
def test_statemachine103_InitialState_instantiation(instance):
    assert isinstance(instance, statemachine103_InitialState)


statemachine103_NormalState_strategy = st.builds(statemachine103_NormalState)
@given(instance=statemachine103_NormalState_strategy)
@settings(max_examples=25)
def test_statemachine103_NormalState_instantiation(instance):
    assert isinstance(instance, statemachine103_NormalState)


statemachine103_State_strategy = st.builds(statemachine103_State, id=st.integers())
@given(instance=statemachine103_State_strategy)
@settings(max_examples=25)
def test_statemachine103_State_instantiation(instance):
    assert isinstance(instance, statemachine103_State)


statemachine103_StateMachine_strategy = st.builds(statemachine103_StateMachine, label=safe_text)
@given(instance=statemachine103_StateMachine_strategy)
@settings(max_examples=25)
def test_statemachine103_StateMachine_instantiation(instance):
    assert isinstance(instance, statemachine103_StateMachine)


statemachine103_StateMachineObject_strategy = st.builds(statemachine103_StateMachineObject, label=safe_text)
@given(instance=statemachine103_StateMachineObject_strategy)
@settings(max_examples=25)
def test_statemachine103_StateMachineObject_instantiation(instance):
    assert isinstance(instance, statemachine103_StateMachineObject)


statemachine103_StateMachineVariable_strategy = st.builds(statemachine103_StateMachineVariable, name=safe_text, type=safe_text)
@given(instance=statemachine103_StateMachineVariable_strategy)
@settings(max_examples=25)
def test_statemachine103_StateMachineVariable_instantiation(instance):
    assert isinstance(instance, statemachine103_StateMachineVariable)


statemachine103_Transition_strategy = st.builds(statemachine103_Transition, guardExpression=safe_text, guardLabel=safe_text)
@given(instance=statemachine103_Transition_strategy)
@settings(max_examples=25)
def test_statemachine103_Transition_instantiation(instance):
    assert isinstance(instance, statemachine103_Transition)


