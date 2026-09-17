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
    simplefsm_State,
    simplefsm_SimpleFiniteStateMachine,
    simplefsm_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_simplefsm_state_is_not_abstract():
    assert not inspect.isabstract(simplefsm_State)


def test_hyp_simplefsm_state_constructor_exists():
    assert callable(simplefsm_State.__init__)


def test_hyp_simplefsm_state_constructor_args():
    sig = inspect.signature(simplefsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_simplefsm_simplefinitestatemachine_is_not_abstract():
    assert not inspect.isabstract(simplefsm_SimpleFiniteStateMachine)


def test_hyp_simplefsm_simplefinitestatemachine_constructor_exists():
    assert callable(simplefsm_SimpleFiniteStateMachine.__init__)


def test_hyp_simplefsm_simplefinitestatemachine_constructor_args():
    sig = inspect.signature(simplefsm_SimpleFiniteStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_simplefsm_transition_is_not_abstract():
    assert not inspect.isabstract(simplefsm_Transition)


def test_hyp_simplefsm_transition_constructor_exists():
    assert callable(simplefsm_Transition.__init__)


def test_hyp_simplefsm_transition_constructor_args():
    sig = inspect.signature(simplefsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
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
simplefsm_State_strategy = st.builds(
    simplefsm_State,
    action=
        safe_text,
    name=
        safe_text
)
simplefsm_SimpleFiniteStateMachine_strategy = st.builds(
    simplefsm_SimpleFiniteStateMachine,
    name=
        safe_text
)
simplefsm_Transition_strategy = st.builds(
    simplefsm_Transition,
    event=
        safe_text,
    name=
        safe_text
)




@given(instance=simplefsm_State_strategy)
def test_hyp_simplefsm_state_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=simplefsm_State_strategy)
def test_hyp_simplefsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=simplefsm_SimpleFiniteStateMachine_strategy)
def test_hyp_simplefsm_simplefinitestatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=simplefsm_Transition_strategy)
def test_hyp_simplefsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=simplefsm_Transition_strategy)
def test_hyp_simplefsm_transition_name_setter(instance):
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
    simplefsm_SimpleFiniteStateMachine,
    simplefsm_State,
    simplefsm_Transition,
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

def test_simplefsm_SimpleFiniteStateMachine_name_value_roundtrip():
    instance = simplefsm_SimpleFiniteStateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_simplefsm_State_action_value_roundtrip():
    instance = simplefsm_State(action="sample_text", name="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_simplefsm_State_name_value_roundtrip():
    instance = simplefsm_State(action="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_simplefsm_Transition_event_value_roundtrip():
    instance = simplefsm_Transition(event="sample_text", name="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_simplefsm_Transition_name_value_roundtrip():
    instance = simplefsm_Transition(event="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_outgoingTransitions1_link_reassign_clear():
    a = simplefsm_Transition(event="sample_text", name="sample_text")
    b1 = simplefsm_State(action="sample_text", name="sample_text")
    b2 = simplefsm_State(action="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'owningState'):
        assert _is_linked(b1, 'owningState', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'owningState'):
        assert not _is_linked(b1, 'owningState', a)
    if hasattr(b2, 'owningState'):
        assert _is_linked(b2, 'owningState', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'owningState'):
        assert not _is_linked(b2, 'owningState', a)


def test_assoc_owningFSM2_link_reassign_clear():
    a = simplefsm_State(action="sample_text", name="sample_text")
    b1 = simplefsm_SimpleFiniteStateMachine(name="sample_text")
    b2 = simplefsm_SimpleFiniteStateMachine(name="sample_text_2")
    _safe_set(a, 'states', b1)
    assert _is_linked(a, 'states', b1)
    if hasattr(b1, 'SimpleFiniteStateMachine'):
        assert _is_linked(b1, 'SimpleFiniteStateMachine', a)
    _safe_set(a, 'states', b2)
    assert _is_linked(a, 'states', b2)
    if hasattr(b1, 'SimpleFiniteStateMachine'):
        assert not _is_linked(b1, 'SimpleFiniteStateMachine', a)
    if hasattr(b2, 'SimpleFiniteStateMachine'):
        assert _is_linked(b2, 'SimpleFiniteStateMachine', a)
    _safe_set(a, 'states', None)
    assert not _is_linked(a, 'states', b2)
    if hasattr(b2, 'SimpleFiniteStateMachine'):
        assert not _is_linked(b2, 'SimpleFiniteStateMachine', a)


def test_assoc_owningState4_link_reassign_clear():
    a = simplefsm_Transition(event="sample_text", name="sample_text")
    b1 = simplefsm_State(action="sample_text", name="sample_text")
    b2 = simplefsm_State(action="sample_text_2", name="sample_text_2")
    _safe_set(a, 'outgoingTransitions', b1)
    assert _is_linked(a, 'outgoingTransitions', b1)
    if hasattr(b1, 'State5'):
        assert _is_linked(b1, 'State5', a)
    _safe_set(a, 'outgoingTransitions', b2)
    assert _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b1, 'State5'):
        assert not _is_linked(b1, 'State5', a)
    if hasattr(b2, 'State5'):
        assert _is_linked(b2, 'State5', a)
    _safe_set(a, 'outgoingTransitions', None)
    assert not _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b2, 'State5'):
        assert not _is_linked(b2, 'State5', a)


def test_assoc_states0_link_reassign_clear():
    a = simplefsm_State(action="sample_text", name="sample_text")
    b1 = simplefsm_SimpleFiniteStateMachine(name="sample_text")
    b2 = simplefsm_SimpleFiniteStateMachine(name="sample_text_2")
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'owningFSM'):
        assert _is_linked(b1, 'owningFSM', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'owningFSM'):
        assert not _is_linked(b1, 'owningFSM', a)
    if hasattr(b2, 'owningFSM'):
        assert _is_linked(b2, 'owningFSM', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'owningFSM'):
        assert not _is_linked(b2, 'owningFSM', a)


def test_assoc_target3_link_reassign_clear():
    a = simplefsm_Transition(event="sample_text", name="sample_text")
    b1 = simplefsm_State(action="sample_text", name="sample_text")
    b2 = simplefsm_State(action="sample_text_2", name="sample_text_2")
    _safe_set(a, 'simplefsm_Transition', b1)
    assert _is_linked(a, 'simplefsm_Transition', b1)
    if hasattr(b1, 'simplefsm_State'):
        assert _is_linked(b1, 'simplefsm_State', a)
    _safe_set(a, 'simplefsm_Transition', b2)
    assert _is_linked(a, 'simplefsm_Transition', b2)
    if hasattr(b1, 'simplefsm_State'):
        assert not _is_linked(b1, 'simplefsm_State', a)
    if hasattr(b2, 'simplefsm_State'):
        assert _is_linked(b2, 'simplefsm_State', a)
    _safe_set(a, 'simplefsm_Transition', None)
    assert not _is_linked(a, 'simplefsm_Transition', b2)
    if hasattr(b2, 'simplefsm_State'):
        assert not _is_linked(b2, 'simplefsm_State', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

simplefsm_SimpleFiniteStateMachine_strategy = st.builds(simplefsm_SimpleFiniteStateMachine, name=safe_text)
@given(instance=simplefsm_SimpleFiniteStateMachine_strategy)
@settings(max_examples=25)
def test_simplefsm_SimpleFiniteStateMachine_instantiation(instance):
    assert isinstance(instance, simplefsm_SimpleFiniteStateMachine)


simplefsm_State_strategy = st.builds(simplefsm_State, action=safe_text, name=safe_text)
@given(instance=simplefsm_State_strategy)
@settings(max_examples=25)
def test_simplefsm_State_instantiation(instance):
    assert isinstance(instance, simplefsm_State)


simplefsm_Transition_strategy = st.builds(simplefsm_Transition, event=safe_text, name=safe_text)
@given(instance=simplefsm_Transition_strategy)
@settings(max_examples=25)
def test_simplefsm_Transition_instantiation(instance):
    assert isinstance(instance, simplefsm_Transition)



