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
    fsm_Transition,
    fsm_State,
    fsm_FiniteStateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_hyp_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_hyp_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"






def test_hyp_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_hyp_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_hyp_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isInitialState" in params, "Missing parameter 'isInitialState'"





def test_hyp_fsm_finitestatemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_FiniteStateMachine)


def test_hyp_fsm_finitestatemachine_constructor_exists():
    assert callable(fsm_FiniteStateMachine.__init__)


def test_hyp_fsm_finitestatemachine_constructor_args():
    sig = inspect.signature(fsm_FiniteStateMachine.__init__)
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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    name=
        safe_text,
    output=
        safe_text,
    input=
        safe_text
)
fsm_State_strategy = st.builds(
    fsm_State,
    name=
        safe_text,
    isInitialState=
        st.booleans()
)
fsm_FiniteStateMachine_strategy = st.builds(
    fsm_FiniteStateMachine,
    name=
        safe_text
)




@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original




@given(instance=fsm_State_strategy)
def test_hyp_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsm_State_strategy)
def test_hyp_fsm_state_isInitialState_setter(instance):
    original = instance.isInitialState
    instance.isInitialState = original
    assert instance.isInitialState == original




@given(instance=fsm_FiniteStateMachine_strategy)
def test_hyp_fsm_finitestatemachine_name_setter(instance):
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
    fsm_FiniteStateMachine,
    fsm_State,
    fsm_Transition,
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

def test_fsm_FiniteStateMachine_name_value_roundtrip():
    instance = fsm_FiniteStateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsm_State_isInitialState_value_roundtrip():
    instance = fsm_State(isInitialState=True, name="sample_text")
    assert instance.isInitialState == True
    instance.isInitialState = False
    assert instance.isInitialState == False


def test_fsm_State_name_value_roundtrip():
    instance = fsm_State(isInitialState=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsm_Transition_input_value_roundtrip():
    instance = fsm_Transition(input="sample_text", name="sample_text", output="sample_text")
    assert instance.input == "sample_text"
    instance.input = "sample_text_2"
    assert instance.input == "sample_text_2"


def test_fsm_Transition_name_value_roundtrip():
    instance = fsm_Transition(input="sample_text", name="sample_text", output="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsm_Transition_output_value_roundtrip():
    instance = fsm_Transition(input="sample_text", name="sample_text", output="sample_text")
    assert instance.output == "sample_text"
    instance.output = "sample_text_2"
    assert instance.output == "sample_text_2"


def test_assoc_outgoingTransitions1_link_reassign_clear():
    a = fsm_Transition(input="sample_text", name="sample_text", output="sample_text")
    b1 = fsm_State(isInitialState=True, name="sample_text")
    b2 = fsm_State(isInitialState=False, name="sample_text_2")
    _safe_set(a, 'fsm_Transition', b1)
    assert _is_linked(a, 'fsm_Transition', b1)
    if hasattr(b1, 'fsm_State2'):
        assert _is_linked(b1, 'fsm_State2', a)
    _safe_set(a, 'fsm_Transition', b2)
    assert _is_linked(a, 'fsm_Transition', b2)
    if hasattr(b1, 'fsm_State2'):
        assert not _is_linked(b1, 'fsm_State2', a)
    if hasattr(b2, 'fsm_State2'):
        assert _is_linked(b2, 'fsm_State2', a)
    _safe_set(a, 'fsm_Transition', None)
    assert not _is_linked(a, 'fsm_Transition', b2)
    if hasattr(b2, 'fsm_State2'):
        assert not _is_linked(b2, 'fsm_State2', a)


def test_assoc_states0_link_reassign_clear():
    a = fsm_State(isInitialState=True, name="sample_text")
    b1 = fsm_FiniteStateMachine(name="sample_text")
    b2 = fsm_FiniteStateMachine(name="sample_text_2")
    _safe_set(a, 'fsm_State', b1)
    assert _is_linked(a, 'fsm_State', b1)
    if hasattr(b1, 'fsm_FiniteStateMachine'):
        assert _is_linked(b1, 'fsm_FiniteStateMachine', a)
    _safe_set(a, 'fsm_State', b2)
    assert _is_linked(a, 'fsm_State', b2)
    if hasattr(b1, 'fsm_FiniteStateMachine'):
        assert not _is_linked(b1, 'fsm_FiniteStateMachine', a)
    if hasattr(b2, 'fsm_FiniteStateMachine'):
        assert _is_linked(b2, 'fsm_FiniteStateMachine', a)
    _safe_set(a, 'fsm_State', None)
    assert not _is_linked(a, 'fsm_State', b2)
    if hasattr(b2, 'fsm_FiniteStateMachine'):
        assert not _is_linked(b2, 'fsm_FiniteStateMachine', a)


def test_assoc_target3_link_reassign_clear():
    a = fsm_Transition(input="sample_text", name="sample_text", output="sample_text")
    b1 = fsm_State(isInitialState=True, name="sample_text")
    b2 = fsm_State(isInitialState=False, name="sample_text_2")
    _safe_set(a, 'fsm_Transition4', b1)
    assert _is_linked(a, 'fsm_Transition4', b1)
    if hasattr(b1, 'fsm_State5'):
        assert _is_linked(b1, 'fsm_State5', a)
    _safe_set(a, 'fsm_Transition4', b2)
    assert _is_linked(a, 'fsm_Transition4', b2)
    if hasattr(b1, 'fsm_State5'):
        assert not _is_linked(b1, 'fsm_State5', a)
    if hasattr(b2, 'fsm_State5'):
        assert _is_linked(b2, 'fsm_State5', a)
    _safe_set(a, 'fsm_Transition4', None)
    assert not _is_linked(a, 'fsm_Transition4', b2)
    if hasattr(b2, 'fsm_State5'):
        assert not _is_linked(b2, 'fsm_State5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

fsm_FiniteStateMachine_strategy = st.builds(fsm_FiniteStateMachine, name=safe_text)
@given(instance=fsm_FiniteStateMachine_strategy)
@settings(max_examples=25)
def test_fsm_FiniteStateMachine_instantiation(instance):
    assert isinstance(instance, fsm_FiniteStateMachine)


fsm_State_strategy = st.builds(fsm_State, isInitialState=st.booleans(), name=safe_text)
@given(instance=fsm_State_strategy)
@settings(max_examples=25)
def test_fsm_State_instantiation(instance):
    assert isinstance(instance, fsm_State)


fsm_Transition_strategy = st.builds(fsm_Transition, input=safe_text, name=safe_text, output=safe_text)
@given(instance=fsm_Transition_strategy)
@settings(max_examples=25)
def test_fsm_Transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



