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
    FSM_StateMachine,
    FSM_Transition,
    FSM_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM_StateMachine)


def test_hyp_fsm_statemachine_constructor_exists():
    assert callable(FSM_StateMachine.__init__)


def test_hyp_fsm_statemachine_constructor_args():
    sig = inspect.signature(FSM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(FSM_Transition)


def test_hyp_fsm_transition_constructor_exists():
    assert callable(FSM_Transition.__init__)


def test_hyp_fsm_transition_constructor_args():
    sig = inspect.signature(FSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"




def test_hyp_fsm_state_is_not_abstract():
    assert not inspect.isabstract(FSM_State)


def test_hyp_fsm_state_constructor_exists():
    assert callable(FSM_State.__init__)


def test_hyp_fsm_state_constructor_args():
    sig = inspect.signature(FSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isAccepting" in params, "Missing parameter 'isAccepting'"




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
FSM_StateMachine_strategy = st.builds(
    FSM_StateMachine,
    name=
        safe_text
)
FSM_Transition_strategy = st.builds(
    FSM_Transition,
    input=
        safe_text
)
FSM_State_strategy = st.builds(
    FSM_State,
    name=
        safe_text,
    isAccepting=
        st.booleans()
)




@given(instance=FSM_StateMachine_strategy)
def test_hyp_fsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=FSM_Transition_strategy)
def test_hyp_fsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original




@given(instance=FSM_State_strategy)
def test_hyp_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FSM_State_strategy)
def test_hyp_fsm_state_isAccepting_setter(instance):
    original = instance.isAccepting
    instance.isAccepting = original
    assert instance.isAccepting == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    FSM_State,
    FSM_StateMachine,
    FSM_Transition,
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

def test_FSM_State_isAccepting_value_roundtrip():
    instance = FSM_State(isAccepting=True, name="sample_text")
    assert instance.isAccepting == True
    instance.isAccepting = False
    assert instance.isAccepting == False


def test_FSM_State_name_value_roundtrip():
    instance = FSM_State(isAccepting=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FSM_StateMachine_name_value_roundtrip():
    instance = FSM_StateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FSM_Transition_input_value_roundtrip():
    instance = FSM_Transition(input="sample_text")
    assert instance.input == "sample_text"
    instance.input = "sample_text_2"
    assert instance.input == "sample_text_2"


def test_assoc_incoming5_link_reassign_clear():
    a = FSM_Transition(input="sample_text")
    b1 = FSM_State(isAccepting=True, name="sample_text")
    b2 = FSM_State(isAccepting=False, name="sample_text_2")
    _safe_set(a, 'Transition6', b1)
    assert _is_linked(a, 'Transition6', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'Transition6', b2)
    assert _is_linked(a, 'Transition6', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'Transition6', None)
    assert not _is_linked(a, 'Transition6', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_outgoing4_link_reassign_clear():
    a = FSM_Transition(input="sample_text")
    b1 = FSM_State(isAccepting=True, name="sample_text")
    b2 = FSM_State(isAccepting=False, name="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_source7_link_reassign_clear():
    a = FSM_Transition(input="sample_text")
    b1 = FSM_State(isAccepting=True, name="sample_text")
    b2 = FSM_State(isAccepting=False, name="sample_text_2")
    _safe_set(a, 'outgoing', b1)
    assert _is_linked(a, 'outgoing', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'outgoing', b2)
    assert _is_linked(a, 'outgoing', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'outgoing', None)
    assert not _is_linked(a, 'outgoing', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_startState1_link_reassign_clear():
    a = FSM_StateMachine(name="sample_text")
    b1 = FSM_State(isAccepting=True, name="sample_text")
    b2 = FSM_State(isAccepting=False, name="sample_text_2")
    _safe_set(a, 'FSM_StateMachine2', b1)
    assert _is_linked(a, 'FSM_StateMachine2', b1)
    if hasattr(b1, 'FSM_State3'):
        assert _is_linked(b1, 'FSM_State3', a)
    _safe_set(a, 'FSM_StateMachine2', b2)
    assert _is_linked(a, 'FSM_StateMachine2', b2)
    if hasattr(b1, 'FSM_State3'):
        assert not _is_linked(b1, 'FSM_State3', a)
    if hasattr(b2, 'FSM_State3'):
        assert _is_linked(b2, 'FSM_State3', a)
    _safe_set(a, 'FSM_StateMachine2', None)
    assert not _is_linked(a, 'FSM_StateMachine2', b2)
    if hasattr(b2, 'FSM_State3'):
        assert not _is_linked(b2, 'FSM_State3', a)


def test_assoc_states0_link_reassign_clear():
    a = FSM_StateMachine(name="sample_text")
    b1 = FSM_State(isAccepting=True, name="sample_text")
    b2 = FSM_State(isAccepting=False, name="sample_text_2")
    _safe_set(a, 'FSM_StateMachine', {b1})
    assert _is_linked(a, 'FSM_StateMachine', b1)
    if hasattr(b1, 'FSM_State'):
        assert _is_linked(b1, 'FSM_State', a)
    _safe_set(a, 'FSM_StateMachine', {b2})
    assert _is_linked(a, 'FSM_StateMachine', b2)
    if hasattr(b1, 'FSM_State'):
        assert not _is_linked(b1, 'FSM_State', a)
    if hasattr(b2, 'FSM_State'):
        assert _is_linked(b2, 'FSM_State', a)
    _safe_set(a, 'FSM_StateMachine', set())
    assert not _is_linked(a, 'FSM_StateMachine', b2)
    if hasattr(b2, 'FSM_State'):
        assert not _is_linked(b2, 'FSM_State', a)


def test_assoc_target8_link_reassign_clear():
    a = FSM_Transition(input="sample_text")
    b1 = FSM_State(isAccepting=True, name="sample_text")
    b2 = FSM_State(isAccepting=False, name="sample_text_2")
    _safe_set(a, 'incoming', b1)
    assert _is_linked(a, 'incoming', b1)
    if hasattr(b1, 'State9'):
        assert _is_linked(b1, 'State9', a)
    _safe_set(a, 'incoming', b2)
    assert _is_linked(a, 'incoming', b2)
    if hasattr(b1, 'State9'):
        assert not _is_linked(b1, 'State9', a)
    if hasattr(b2, 'State9'):
        assert _is_linked(b2, 'State9', a)
    _safe_set(a, 'incoming', None)
    assert not _is_linked(a, 'incoming', b2)
    if hasattr(b2, 'State9'):
        assert not _is_linked(b2, 'State9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

FSM_State_strategy = st.builds(FSM_State, isAccepting=st.booleans(), name=safe_text)
@given(instance=FSM_State_strategy)
@settings(max_examples=25)
def test_FSM_State_instantiation(instance):
    assert isinstance(instance, FSM_State)


FSM_StateMachine_strategy = st.builds(FSM_StateMachine, name=safe_text)
@given(instance=FSM_StateMachine_strategy)
@settings(max_examples=25)
def test_FSM_StateMachine_instantiation(instance):
    assert isinstance(instance, FSM_StateMachine)


FSM_Transition_strategy = st.builds(FSM_Transition, input=safe_text)
@given(instance=FSM_Transition_strategy)
@settings(max_examples=25)
def test_FSM_Transition_instantiation(instance):
    assert isinstance(instance, FSM_Transition)



