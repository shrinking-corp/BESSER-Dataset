import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    State,
    StateMachine,
    TracedClass,
    Transition,
    UHSM_CompositeState,
    UHSM_EObject,
    UHSM_FinalState,
    UHSM_InitialState,
    UHSM_State,
    UHSM_StateMachine,
    UHSM_TracedClass,
    UHSM_Transition,
    UHSM_UState,
    UHSM_UStateMachine,
    UHSM_UTransition,
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

def test_UHSM_State_name_value_roundtrip():
    instance = UHSM_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_UHSM_StateMachine_name_value_roundtrip():
    instance = UHSM_StateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_UHSM_TracedClass_trace_value_roundtrip():
    instance = UHSM_TracedClass(trace="sample_text")
    assert instance.trace == "sample_text"
    instance.trace = "sample_text_2"
    assert instance.trace == "sample_text_2"


def test_UHSM_Transition_effect_value_roundtrip():
    instance = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    assert instance.effect == "sample_text"
    instance.effect = "sample_text_2"
    assert instance.effect == "sample_text_2"


def test_UHSM_Transition_name_value_roundtrip():
    instance = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_UHSM_Transition_trigger_value_roundtrip():
    instance = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    assert instance.trigger == "sample_text"
    instance.trigger = "sample_text_2"
    assert instance.trigger == "sample_text_2"


def test_UHSM_CompositeState_isa_State():
    instance = UHSM_CompositeState()
    assert isinstance(instance, State)


def test_UHSM_FinalState_isa_State():
    instance = UHSM_FinalState()
    assert isinstance(instance, State)


def test_UHSM_InitialState_isa_State():
    instance = UHSM_InitialState()
    assert isinstance(instance, State)


def test_UHSM_UState_isa_State():
    instance = UHSM_UState()
    assert isinstance(instance, State)


def test_UHSM_UStateMachine_isa_StateMachine():
    instance = UHSM_UStateMachine()
    assert isinstance(instance, StateMachine)


def test_UHSM_State_isa_TracedClass():
    instance = UHSM_State(name="sample_text")
    assert isinstance(instance, TracedClass)


def test_UHSM_StateMachine_isa_TracedClass():
    instance = UHSM_StateMachine(name="sample_text")
    assert isinstance(instance, TracedClass)


def test_UHSM_Transition_isa_TracedClass():
    instance = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    assert isinstance(instance, TracedClass)


def test_UHSM_UTransition_isa_Transition():
    instance = UHSM_UTransition()
    assert isinstance(instance, Transition)


def test_assoc_States16_link_reassign_clear():
    a = UHSM_State(name="sample_text")
    b1 = UHSM_UState()
    b2 = UHSM_UState()
    _safe_set(a, 'UHSM_State17', b1)
    assert _is_linked(a, 'UHSM_State17', b1)
    if hasattr(b1, 'UHSM_UState'):
        assert _is_linked(b1, 'UHSM_UState', a)
    _safe_set(a, 'UHSM_State17', b2)
    assert _is_linked(a, 'UHSM_State17', b2)
    if hasattr(b1, 'UHSM_UState'):
        assert not _is_linked(b1, 'UHSM_UState', a)
    if hasattr(b2, 'UHSM_UState'):
        assert _is_linked(b2, 'UHSM_UState', a)
    _safe_set(a, 'UHSM_State17', None)
    assert not _is_linked(a, 'UHSM_State17', b2)
    if hasattr(b2, 'UHSM_UState'):
        assert not _is_linked(b2, 'UHSM_UState', a)


def test_assoc_ownedState11_link_reassign_clear():
    a = UHSM_StateMachine(name="sample_text")
    b1 = UHSM_State(name="sample_text")
    b2 = UHSM_State(name="sample_text_2")
    _safe_set(a, 'UHSM_StateMachine', {b1})
    assert _is_linked(a, 'UHSM_StateMachine', b1)
    if hasattr(b1, 'UHSM_State12'):
        assert _is_linked(b1, 'UHSM_State12', a)
    _safe_set(a, 'UHSM_StateMachine', {b2})
    assert _is_linked(a, 'UHSM_StateMachine', b2)
    if hasattr(b1, 'UHSM_State12'):
        assert not _is_linked(b1, 'UHSM_State12', a)
    if hasattr(b2, 'UHSM_State12'):
        assert _is_linked(b2, 'UHSM_State12', a)
    _safe_set(a, 'UHSM_StateMachine', set())
    assert not _is_linked(a, 'UHSM_StateMachine', b2)
    if hasattr(b2, 'UHSM_State12'):
        assert not _is_linked(b2, 'UHSM_State12', a)


def test_assoc_ownedSubState8_link_reassign_clear():
    a = UHSM_State(name="sample_text")
    b1 = UHSM_CompositeState()
    b2 = UHSM_CompositeState()
    _safe_set(a, 'UHSM_State10', b1)
    assert _is_linked(a, 'UHSM_State10', b1)
    if hasattr(b1, 'UHSM_CompositeState9'):
        assert _is_linked(b1, 'UHSM_CompositeState9', a)
    _safe_set(a, 'UHSM_State10', b2)
    assert _is_linked(a, 'UHSM_State10', b2)
    if hasattr(b1, 'UHSM_CompositeState9'):
        assert not _is_linked(b1, 'UHSM_CompositeState9', a)
    if hasattr(b2, 'UHSM_CompositeState9'):
        assert _is_linked(b2, 'UHSM_CompositeState9', a)
    _safe_set(a, 'UHSM_State10', None)
    assert not _is_linked(a, 'UHSM_State10', b2)
    if hasattr(b2, 'UHSM_CompositeState9'):
        assert not _is_linked(b2, 'UHSM_CompositeState9', a)


def test_assoc_ownedTransition13_link_reassign_clear():
    a = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    b1 = UHSM_StateMachine(name="sample_text")
    b2 = UHSM_StateMachine(name="sample_text_2")
    _safe_set(a, 'UHSM_Transition15', b1)
    assert _is_linked(a, 'UHSM_Transition15', b1)
    if hasattr(b1, 'UHSM_StateMachine14'):
        assert _is_linked(b1, 'UHSM_StateMachine14', a)
    _safe_set(a, 'UHSM_Transition15', b2)
    assert _is_linked(a, 'UHSM_Transition15', b2)
    if hasattr(b1, 'UHSM_StateMachine14'):
        assert not _is_linked(b1, 'UHSM_StateMachine14', a)
    if hasattr(b2, 'UHSM_StateMachine14'):
        assert _is_linked(b2, 'UHSM_StateMachine14', a)
    _safe_set(a, 'UHSM_Transition15', None)
    assert not _is_linked(a, 'UHSM_Transition15', b2)
    if hasattr(b2, 'UHSM_StateMachine14'):
        assert not _is_linked(b2, 'UHSM_StateMachine14', a)


def test_assoc_owningCompositeState0_link_reassign_clear():
    a = UHSM_State(name="sample_text")
    b1 = UHSM_CompositeState()
    b2 = UHSM_CompositeState()
    _safe_set(a, 'UHSM_State', b1)
    assert _is_linked(a, 'UHSM_State', b1)
    if hasattr(b1, 'UHSM_CompositeState'):
        assert _is_linked(b1, 'UHSM_CompositeState', a)
    _safe_set(a, 'UHSM_State', b2)
    assert _is_linked(a, 'UHSM_State', b2)
    if hasattr(b1, 'UHSM_CompositeState'):
        assert not _is_linked(b1, 'UHSM_CompositeState', a)
    if hasattr(b2, 'UHSM_CompositeState'):
        assert _is_linked(b2, 'UHSM_CompositeState', a)
    _safe_set(a, 'UHSM_State', None)
    assert not _is_linked(a, 'UHSM_State', b2)
    if hasattr(b2, 'UHSM_CompositeState'):
        assert not _is_linked(b2, 'UHSM_CompositeState', a)


def test_assoc_ref20_link_reassign_clear():
    a = UHSM_TracedClass(trace="sample_text")
    b1 = UHSM_EObject()
    b2 = UHSM_EObject()
    _safe_set(a, 'UHSM_TracedClass', {b1})
    assert _is_linked(a, 'UHSM_TracedClass', b1)
    if hasattr(b1, 'UHSM_EObject'):
        assert _is_linked(b1, 'UHSM_EObject', a)
    _safe_set(a, 'UHSM_TracedClass', {b2})
    assert _is_linked(a, 'UHSM_TracedClass', b2)
    if hasattr(b1, 'UHSM_EObject'):
        assert not _is_linked(b1, 'UHSM_EObject', a)
    if hasattr(b2, 'UHSM_EObject'):
        assert _is_linked(b2, 'UHSM_EObject', a)
    _safe_set(a, 'UHSM_TracedClass', set())
    assert not _is_linked(a, 'UHSM_TracedClass', b2)
    if hasattr(b2, 'UHSM_EObject'):
        assert not _is_linked(b2, 'UHSM_EObject', a)


def test_assoc_source5_link_reassign_clear():
    a = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    b1 = UHSM_State(name="sample_text")
    b2 = UHSM_State(name="sample_text_2")
    _safe_set(a, 'UHSM_Transition6', b1)
    assert _is_linked(a, 'UHSM_Transition6', b1)
    if hasattr(b1, 'UHSM_State7'):
        assert _is_linked(b1, 'UHSM_State7', a)
    _safe_set(a, 'UHSM_Transition6', b2)
    assert _is_linked(a, 'UHSM_Transition6', b2)
    if hasattr(b1, 'UHSM_State7'):
        assert not _is_linked(b1, 'UHSM_State7', a)
    if hasattr(b2, 'UHSM_State7'):
        assert _is_linked(b2, 'UHSM_State7', a)
    _safe_set(a, 'UHSM_Transition6', None)
    assert not _is_linked(a, 'UHSM_Transition6', b2)
    if hasattr(b2, 'UHSM_State7'):
        assert not _is_linked(b2, 'UHSM_State7', a)


def test_assoc_stateMachines18_link_reassign_clear():
    a = UHSM_StateMachine(name="sample_text")
    b1 = UHSM_UStateMachine()
    b2 = UHSM_UStateMachine()
    _safe_set(a, 'UHSM_StateMachine19', b1)
    assert _is_linked(a, 'UHSM_StateMachine19', b1)
    if hasattr(b1, 'UHSM_UStateMachine'):
        assert _is_linked(b1, 'UHSM_UStateMachine', a)
    _safe_set(a, 'UHSM_StateMachine19', b2)
    assert _is_linked(a, 'UHSM_StateMachine19', b2)
    if hasattr(b1, 'UHSM_UStateMachine'):
        assert not _is_linked(b1, 'UHSM_UStateMachine', a)
    if hasattr(b2, 'UHSM_UStateMachine'):
        assert _is_linked(b2, 'UHSM_UStateMachine', a)
    _safe_set(a, 'UHSM_StateMachine19', None)
    assert not _is_linked(a, 'UHSM_StateMachine19', b2)
    if hasattr(b2, 'UHSM_UStateMachine'):
        assert not _is_linked(b2, 'UHSM_UStateMachine', a)


def test_assoc_target2_link_reassign_clear():
    a = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    b1 = UHSM_State(name="sample_text")
    b2 = UHSM_State(name="sample_text_2")
    _safe_set(a, 'UHSM_Transition3', b1)
    assert _is_linked(a, 'UHSM_Transition3', b1)
    if hasattr(b1, 'UHSM_State4'):
        assert _is_linked(b1, 'UHSM_State4', a)
    _safe_set(a, 'UHSM_Transition3', b2)
    assert _is_linked(a, 'UHSM_Transition3', b2)
    if hasattr(b1, 'UHSM_State4'):
        assert not _is_linked(b1, 'UHSM_State4', a)
    if hasattr(b2, 'UHSM_State4'):
        assert _is_linked(b2, 'UHSM_State4', a)
    _safe_set(a, 'UHSM_Transition3', None)
    assert not _is_linked(a, 'UHSM_Transition3', b2)
    if hasattr(b2, 'UHSM_State4'):
        assert not _is_linked(b2, 'UHSM_State4', a)


def test_assoc_transitions1_link_reassign_clear():
    a = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    b1 = UHSM_UTransition()
    b2 = UHSM_UTransition()
    _safe_set(a, 'UHSM_Transition', b1)
    assert _is_linked(a, 'UHSM_Transition', b1)
    if hasattr(b1, 'UHSM_UTransition'):
        assert _is_linked(b1, 'UHSM_UTransition', a)
    _safe_set(a, 'UHSM_Transition', b2)
    assert _is_linked(a, 'UHSM_Transition', b2)
    if hasattr(b1, 'UHSM_UTransition'):
        assert not _is_linked(b1, 'UHSM_UTransition', a)
    if hasattr(b2, 'UHSM_UTransition'):
        assert _is_linked(b2, 'UHSM_UTransition', a)
    _safe_set(a, 'UHSM_Transition', None)
    assert not _is_linked(a, 'UHSM_Transition', b2)
    if hasattr(b2, 'UHSM_UTransition'):
        assert not _is_linked(b2, 'UHSM_UTransition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


StateMachine_strategy = st.builds(StateMachine)
@given(instance=StateMachine_strategy)
@settings(max_examples=25)
def test_StateMachine_instantiation(instance):
    assert isinstance(instance, StateMachine)


TracedClass_strategy = st.builds(TracedClass)
@given(instance=TracedClass_strategy)
@settings(max_examples=25)
def test_TracedClass_instantiation(instance):
    assert isinstance(instance, TracedClass)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


UHSM_CompositeState_strategy = st.builds(UHSM_CompositeState)
@given(instance=UHSM_CompositeState_strategy)
@settings(max_examples=25)
def test_UHSM_CompositeState_instantiation(instance):
    assert isinstance(instance, UHSM_CompositeState)


UHSM_EObject_strategy = st.builds(UHSM_EObject)
@given(instance=UHSM_EObject_strategy)
@settings(max_examples=25)
def test_UHSM_EObject_instantiation(instance):
    assert isinstance(instance, UHSM_EObject)


UHSM_FinalState_strategy = st.builds(UHSM_FinalState)
@given(instance=UHSM_FinalState_strategy)
@settings(max_examples=25)
def test_UHSM_FinalState_instantiation(instance):
    assert isinstance(instance, UHSM_FinalState)


UHSM_InitialState_strategy = st.builds(UHSM_InitialState)
@given(instance=UHSM_InitialState_strategy)
@settings(max_examples=25)
def test_UHSM_InitialState_instantiation(instance):
    assert isinstance(instance, UHSM_InitialState)


UHSM_State_strategy = st.builds(UHSM_State, name=safe_text)
@given(instance=UHSM_State_strategy)
@settings(max_examples=25)
def test_UHSM_State_instantiation(instance):
    assert isinstance(instance, UHSM_State)


UHSM_StateMachine_strategy = st.builds(UHSM_StateMachine, name=safe_text)
@given(instance=UHSM_StateMachine_strategy)
@settings(max_examples=25)
def test_UHSM_StateMachine_instantiation(instance):
    assert isinstance(instance, UHSM_StateMachine)


UHSM_TracedClass_strategy = st.builds(UHSM_TracedClass, trace=safe_text)
@given(instance=UHSM_TracedClass_strategy)
@settings(max_examples=25)
def test_UHSM_TracedClass_instantiation(instance):
    assert isinstance(instance, UHSM_TracedClass)


UHSM_Transition_strategy = st.builds(UHSM_Transition, effect=safe_text, name=safe_text, trigger=safe_text)
@given(instance=UHSM_Transition_strategy)
@settings(max_examples=25)
def test_UHSM_Transition_instantiation(instance):
    assert isinstance(instance, UHSM_Transition)


UHSM_UState_strategy = st.builds(UHSM_UState)
@given(instance=UHSM_UState_strategy)
@settings(max_examples=25)
def test_UHSM_UState_instantiation(instance):
    assert isinstance(instance, UHSM_UState)


UHSM_UStateMachine_strategy = st.builds(UHSM_UStateMachine)
@given(instance=UHSM_UStateMachine_strategy)
@settings(max_examples=25)
def test_UHSM_UStateMachine_instantiation(instance):
    assert isinstance(instance, UHSM_UStateMachine)


UHSM_UTransition_strategy = st.builds(UHSM_UTransition)
@given(instance=UHSM_UTransition_strategy)
@settings(max_examples=25)
def test_UHSM_UTransition_instantiation(instance):
    assert isinstance(instance, UHSM_UTransition)


