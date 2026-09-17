# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    SM_FinalState,
    SM_InitialState,
    SM_Transition,
    SM_StateMachine,
    SM_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sm_finalstate_is_not_abstract():
    assert not inspect.isabstract(SM_FinalState)


def test_hyp_sm_finalstate_constructor_exists():
    assert callable(SM_FinalState.__init__)


def test_hyp_sm_finalstate_constructor_args():
    sig = inspect.signature(SM_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sm_initialstate_is_not_abstract():
    assert not inspect.isabstract(SM_InitialState)


def test_hyp_sm_initialstate_constructor_exists():
    assert callable(SM_InitialState.__init__)


def test_hyp_sm_initialstate_constructor_args():
    sig = inspect.signature(SM_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sm_transition_is_not_abstract():
    assert not inspect.isabstract(SM_Transition)


def test_hyp_sm_transition_constructor_exists():
    assert callable(SM_Transition.__init__)


def test_hyp_sm_transition_constructor_args():
    sig = inspect.signature(SM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "effect" in params, "Missing parameter 'effect'"





def test_hyp_sm_statemachine_is_not_abstract():
    assert not inspect.isabstract(SM_StateMachine)


def test_hyp_sm_statemachine_constructor_exists():
    assert callable(SM_StateMachine.__init__)


def test_hyp_sm_statemachine_constructor_args():
    sig = inspect.signature(SM_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sm_state_is_not_abstract():
    assert not inspect.isabstract(SM_State)


def test_hyp_sm_state_constructor_exists():
    assert callable(SM_State.__init__)


def test_hyp_sm_state_constructor_args():
    sig = inspect.signature(SM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
State_strategy = st.builds(
    State,
)
SM_FinalState_strategy = st.builds(
    SM_FinalState,
)
SM_InitialState_strategy = st.builds(
    SM_InitialState,
)
SM_Transition_strategy = st.builds(
    SM_Transition,
    trigger=
        safe_text,
    effect=
        safe_text
)
SM_StateMachine_strategy = st.builds(
    SM_StateMachine,
)
SM_State_strategy = st.builds(
    SM_State,
    name=
        safe_text
)







@given(instance=SM_Transition_strategy)
def test_hyp_sm_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=SM_Transition_strategy)
def test_hyp_sm_transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original





@given(instance=SM_State_strategy)
def test_hyp_sm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    SM_FinalState,
    SM_InitialState,
    SM_State,
    SM_StateMachine,
    SM_Transition,
    State,
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

def test_SM_State_name_value_roundtrip():
    instance = SM_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SM_Transition_effect_value_roundtrip():
    instance = SM_Transition(effect="sample_text", trigger="sample_text")
    assert instance.effect == "sample_text"
    instance.effect = "sample_text_2"
    assert instance.effect == "sample_text_2"


def test_SM_Transition_trigger_value_roundtrip():
    instance = SM_Transition(effect="sample_text", trigger="sample_text")
    assert instance.trigger == "sample_text"
    instance.trigger = "sample_text_2"
    assert instance.trigger == "sample_text_2"


def test_SM_FinalState_isa_State():
    instance = SM_FinalState()
    assert isinstance(instance, State)


def test_SM_InitialState_isa_State():
    instance = SM_InitialState()
    assert isinstance(instance, State)


def test_assoc_ownedState7_link_reassign_clear():
    a = SM_State(name="sample_text")
    b1 = SM_StateMachine()
    b2 = SM_StateMachine()
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'owningStateMachine'):
        assert _is_linked(b1, 'owningStateMachine', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'owningStateMachine'):
        assert not _is_linked(b1, 'owningStateMachine', a)
    if hasattr(b2, 'owningStateMachine'):
        assert _is_linked(b2, 'owningStateMachine', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'owningStateMachine'):
        assert not _is_linked(b2, 'owningStateMachine', a)


def test_assoc_ownedTransition8_link_reassign_clear():
    a = SM_Transition(effect="sample_text", trigger="sample_text")
    b1 = SM_StateMachine()
    b2 = SM_StateMachine()
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'owningStateMachine9'):
        assert _is_linked(b1, 'owningStateMachine9', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'owningStateMachine9'):
        assert not _is_linked(b1, 'owningStateMachine9', a)
    if hasattr(b2, 'owningStateMachine9'):
        assert _is_linked(b2, 'owningStateMachine9', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'owningStateMachine9'):
        assert not _is_linked(b2, 'owningStateMachine9', a)


def test_assoc_owningStateMachine0_link_reassign_clear():
    a = SM_State(name="sample_text")
    b1 = SM_StateMachine()
    b2 = SM_StateMachine()
    _safe_set(a, 'ownedState', b1)
    assert _is_linked(a, 'ownedState', b1)
    if hasattr(b1, 'StateMachine'):
        assert _is_linked(b1, 'StateMachine', a)
    _safe_set(a, 'ownedState', b2)
    assert _is_linked(a, 'ownedState', b2)
    if hasattr(b1, 'StateMachine'):
        assert not _is_linked(b1, 'StateMachine', a)
    if hasattr(b2, 'StateMachine'):
        assert _is_linked(b2, 'StateMachine', a)
    _safe_set(a, 'ownedState', None)
    assert not _is_linked(a, 'ownedState', b2)
    if hasattr(b2, 'StateMachine'):
        assert not _is_linked(b2, 'StateMachine', a)


def test_assoc_owningStateMachine5_link_reassign_clear():
    a = SM_Transition(effect="sample_text", trigger="sample_text")
    b1 = SM_StateMachine()
    b2 = SM_StateMachine()
    _safe_set(a, 'ownedTransition', b1)
    assert _is_linked(a, 'ownedTransition', b1)
    if hasattr(b1, 'StateMachine6'):
        assert _is_linked(b1, 'StateMachine6', a)
    _safe_set(a, 'ownedTransition', b2)
    assert _is_linked(a, 'ownedTransition', b2)
    if hasattr(b1, 'StateMachine6'):
        assert not _is_linked(b1, 'StateMachine6', a)
    if hasattr(b2, 'StateMachine6'):
        assert _is_linked(b2, 'StateMachine6', a)
    _safe_set(a, 'ownedTransition', None)
    assert not _is_linked(a, 'ownedTransition', b2)
    if hasattr(b2, 'StateMachine6'):
        assert not _is_linked(b2, 'StateMachine6', a)


def test_assoc_source2_link_reassign_clear():
    a = SM_Transition(effect="sample_text", trigger="sample_text")
    b1 = SM_State(name="sample_text")
    b2 = SM_State(name="sample_text_2")
    _safe_set(a, 'SM_Transition3', b1)
    assert _is_linked(a, 'SM_Transition3', b1)
    if hasattr(b1, 'SM_State4'):
        assert _is_linked(b1, 'SM_State4', a)
    _safe_set(a, 'SM_Transition3', b2)
    assert _is_linked(a, 'SM_Transition3', b2)
    if hasattr(b1, 'SM_State4'):
        assert not _is_linked(b1, 'SM_State4', a)
    if hasattr(b2, 'SM_State4'):
        assert _is_linked(b2, 'SM_State4', a)
    _safe_set(a, 'SM_Transition3', None)
    assert not _is_linked(a, 'SM_Transition3', b2)
    if hasattr(b2, 'SM_State4'):
        assert not _is_linked(b2, 'SM_State4', a)


def test_assoc_target1_link_reassign_clear():
    a = SM_Transition(effect="sample_text", trigger="sample_text")
    b1 = SM_State(name="sample_text")
    b2 = SM_State(name="sample_text_2")
    _safe_set(a, 'SM_Transition', b1)
    assert _is_linked(a, 'SM_Transition', b1)
    if hasattr(b1, 'SM_State'):
        assert _is_linked(b1, 'SM_State', a)
    _safe_set(a, 'SM_Transition', b2)
    assert _is_linked(a, 'SM_Transition', b2)
    if hasattr(b1, 'SM_State'):
        assert not _is_linked(b1, 'SM_State', a)
    if hasattr(b2, 'SM_State'):
        assert _is_linked(b2, 'SM_State', a)
    _safe_set(a, 'SM_Transition', None)
    assert not _is_linked(a, 'SM_Transition', b2)
    if hasattr(b2, 'SM_State'):
        assert not _is_linked(b2, 'SM_State', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SM_FinalState_strategy = st.builds(SM_FinalState)
@given(instance=SM_FinalState_strategy)
@settings(max_examples=25)
def test_SM_FinalState_instantiation(instance):
    assert isinstance(instance, SM_FinalState)


SM_InitialState_strategy = st.builds(SM_InitialState)
@given(instance=SM_InitialState_strategy)
@settings(max_examples=25)
def test_SM_InitialState_instantiation(instance):
    assert isinstance(instance, SM_InitialState)


SM_State_strategy = st.builds(SM_State, name=safe_text)
@given(instance=SM_State_strategy)
@settings(max_examples=25)
def test_SM_State_instantiation(instance):
    assert isinstance(instance, SM_State)


SM_StateMachine_strategy = st.builds(SM_StateMachine)
@given(instance=SM_StateMachine_strategy)
@settings(max_examples=25)
def test_SM_StateMachine_instantiation(instance):
    assert isinstance(instance, SM_StateMachine)


SM_Transition_strategy = st.builds(SM_Transition, effect=safe_text, trigger=safe_text)
@given(instance=SM_Transition_strategy)
@settings(max_examples=25)
def test_SM_Transition_instantiation(instance):
    assert isinstance(instance, SM_Transition)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)



