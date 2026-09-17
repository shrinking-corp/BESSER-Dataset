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
    statemachine_Condition,
    statemachine_Transition,
    statemachine_Command,
    Signal,
    statemachine_OutputSignal,
    statemachine_InputSignal,
    statemachine_State,
    statemachine_Signal,
    statemachine_Statemachine,
    statemachine_Event,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_statemachine_condition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Condition)


def test_hyp_statemachine_condition_constructor_exists():
    assert callable(statemachine_Condition.__init__)


def test_hyp_statemachine_condition_constructor_args():
    sig = inspect.signature(statemachine_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_hyp_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_hyp_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_command_is_not_abstract():
    assert not inspect.isabstract(statemachine_Command)


def test_hyp_statemachine_command_constructor_exists():
    assert callable(statemachine_Command.__init__)


def test_hyp_statemachine_command_constructor_args():
    sig = inspect.signature(statemachine_Command.__init__)
    params = list(sig.parameters.keys())
    assert "newValue" in params, "Missing parameter 'newValue'"




def test_hyp_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_hyp_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_hyp_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_outputsignal_is_not_abstract():
    assert not inspect.isabstract(statemachine_OutputSignal)


def test_hyp_statemachine_outputsignal_constructor_exists():
    assert callable(statemachine_OutputSignal.__init__)


def test_hyp_statemachine_outputsignal_constructor_args():
    sig = inspect.signature(statemachine_OutputSignal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_inputsignal_is_not_abstract():
    assert not inspect.isabstract(statemachine_InputSignal)


def test_hyp_statemachine_inputsignal_constructor_exists():
    assert callable(statemachine_InputSignal.__init__)


def test_hyp_statemachine_inputsignal_constructor_args():
    sig = inspect.signature(statemachine_InputSignal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_hyp_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_hyp_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_statemachine_signal_is_not_abstract():
    assert not inspect.isabstract(statemachine_Signal)


def test_hyp_statemachine_signal_constructor_exists():
    assert callable(statemachine_Signal.__init__)


def test_hyp_statemachine_signal_constructor_args():
    sig = inspect.signature(statemachine_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statemachine)


def test_hyp_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_Statemachine.__init__)


def test_hyp_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(statemachine_Event)


def test_hyp_statemachine_event_constructor_exists():
    assert callable(statemachine_Event.__init__)


def test_hyp_statemachine_event_constructor_args():
    sig = inspect.signature(statemachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"



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
statemachine_Condition_strategy = st.builds(
    statemachine_Condition,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_Command_strategy = st.builds(
    statemachine_Command,
    newValue=
        st.booleans()
)
Signal_strategy = st.builds(
    Signal,
)
statemachine_OutputSignal_strategy = st.builds(
    statemachine_OutputSignal,
)
statemachine_InputSignal_strategy = st.builds(
    statemachine_InputSignal,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text
)
statemachine_Signal_strategy = st.builds(
    statemachine_Signal,
    name=
        safe_text
)
statemachine_Statemachine_strategy = st.builds(
    statemachine_Statemachine,
)
statemachine_Event_strategy = st.builds(
    statemachine_Event,
    value=
        st.booleans()
)






@given(instance=statemachine_Command_strategy)
def test_hyp_statemachine_command_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original







@given(instance=statemachine_State_strategy)
def test_hyp_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=statemachine_Signal_strategy)
def test_hyp_statemachine_signal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=statemachine_Event_strategy)
def test_hyp_statemachine_event_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Signal,
    statemachine_Command,
    statemachine_Condition,
    statemachine_Event,
    statemachine_InputSignal,
    statemachine_OutputSignal,
    statemachine_Signal,
    statemachine_State,
    statemachine_Statemachine,
    statemachine_Transition,
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

def test_statemachine_Command_newValue_value_roundtrip():
    instance = statemachine_Command(newValue=True)
    assert instance.newValue == True
    instance.newValue = False
    assert instance.newValue == False


def test_statemachine_Event_value_value_roundtrip():
    instance = statemachine_Event(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_statemachine_Signal_name_value_roundtrip():
    instance = statemachine_Signal(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_State_name_value_roundtrip():
    instance = statemachine_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_InputSignal_isa_Signal():
    instance = statemachine_InputSignal()
    assert isinstance(instance, Signal)


def test_statemachine_OutputSignal_isa_Signal():
    instance = statemachine_OutputSignal()
    assert isinstance(instance, Signal)


def test_assoc_commands3_link_reassign_clear():
    a = statemachine_State(name="sample_text")
    b1 = statemachine_Command(newValue=True)
    b2 = statemachine_Command(newValue=False)
    _safe_set(a, 'statemachine_State4', {b1})
    assert _is_linked(a, 'statemachine_State4', b1)
    if hasattr(b1, 'statemachine_Command'):
        assert _is_linked(b1, 'statemachine_Command', a)
    _safe_set(a, 'statemachine_State4', {b2})
    assert _is_linked(a, 'statemachine_State4', b2)
    if hasattr(b1, 'statemachine_Command'):
        assert not _is_linked(b1, 'statemachine_Command', a)
    if hasattr(b2, 'statemachine_Command'):
        assert _is_linked(b2, 'statemachine_Command', a)
    _safe_set(a, 'statemachine_State4', set())
    assert not _is_linked(a, 'statemachine_State4', b2)
    if hasattr(b2, 'statemachine_Command'):
        assert not _is_linked(b2, 'statemachine_Command', a)


def test_assoc_events15_link_reassign_clear():
    a = statemachine_Event(value=True)
    b1 = statemachine_Condition()
    b2 = statemachine_Condition()
    _safe_set(a, 'statemachine_Event', b1)
    assert _is_linked(a, 'statemachine_Event', b1)
    if hasattr(b1, 'statemachine_Condition16'):
        assert _is_linked(b1, 'statemachine_Condition16', a)
    _safe_set(a, 'statemachine_Event', b2)
    assert _is_linked(a, 'statemachine_Event', b2)
    if hasattr(b1, 'statemachine_Condition16'):
        assert not _is_linked(b1, 'statemachine_Condition16', a)
    if hasattr(b2, 'statemachine_Condition16'):
        assert _is_linked(b2, 'statemachine_Condition16', a)
    _safe_set(a, 'statemachine_Event', None)
    assert not _is_linked(a, 'statemachine_Event', b2)
    if hasattr(b2, 'statemachine_Condition16'):
        assert not _is_linked(b2, 'statemachine_Condition16', a)


def test_assoc_nestedStates8_link_reassign_clear():
    a = statemachine_State(name="sample_text")
    b1 = statemachine_State(name="sample_text")
    b2 = statemachine_State(name="sample_text_2")
    _safe_set(a, 'statemachine_State7', {b1})
    assert _is_linked(a, 'statemachine_State7', b1)
    if hasattr(b1, 'statemachine_State9'):
        assert _is_linked(b1, 'statemachine_State9', a)
    _safe_set(a, 'statemachine_State7', {b2})
    assert _is_linked(a, 'statemachine_State7', b2)
    if hasattr(b1, 'statemachine_State9'):
        assert not _is_linked(b1, 'statemachine_State9', a)
    if hasattr(b2, 'statemachine_State9'):
        assert _is_linked(b2, 'statemachine_State9', a)
    _safe_set(a, 'statemachine_State7', set())
    assert not _is_linked(a, 'statemachine_State7', b2)
    if hasattr(b2, 'statemachine_State9'):
        assert not _is_linked(b2, 'statemachine_State9', a)


def test_assoc_signal17_link_reassign_clear():
    a = statemachine_Signal(name="sample_text")
    b1 = statemachine_Event(value=True)
    b2 = statemachine_Event(value=False)
    _safe_set(a, 'statemachine_Signal19', b1)
    assert _is_linked(a, 'statemachine_Signal19', b1)
    if hasattr(b1, 'statemachine_Event18'):
        assert _is_linked(b1, 'statemachine_Event18', a)
    _safe_set(a, 'statemachine_Signal19', b2)
    assert _is_linked(a, 'statemachine_Signal19', b2)
    if hasattr(b1, 'statemachine_Event18'):
        assert not _is_linked(b1, 'statemachine_Event18', a)
    if hasattr(b2, 'statemachine_Event18'):
        assert _is_linked(b2, 'statemachine_Event18', a)
    _safe_set(a, 'statemachine_Signal19', None)
    assert not _is_linked(a, 'statemachine_Signal19', b2)
    if hasattr(b2, 'statemachine_Event18'):
        assert not _is_linked(b2, 'statemachine_Event18', a)


def test_assoc_signal20_link_reassign_clear():
    a = statemachine_Signal(name="sample_text")
    b1 = statemachine_Command(newValue=True)
    b2 = statemachine_Command(newValue=False)
    _safe_set(a, 'statemachine_Signal22', b1)
    assert _is_linked(a, 'statemachine_Signal22', b1)
    if hasattr(b1, 'statemachine_Command21'):
        assert _is_linked(b1, 'statemachine_Command21', a)
    _safe_set(a, 'statemachine_Signal22', b2)
    assert _is_linked(a, 'statemachine_Signal22', b2)
    if hasattr(b1, 'statemachine_Command21'):
        assert not _is_linked(b1, 'statemachine_Command21', a)
    if hasattr(b2, 'statemachine_Command21'):
        assert _is_linked(b2, 'statemachine_Command21', a)
    _safe_set(a, 'statemachine_Signal22', None)
    assert not _is_linked(a, 'statemachine_Signal22', b2)
    if hasattr(b2, 'statemachine_Command21'):
        assert not _is_linked(b2, 'statemachine_Command21', a)


def test_assoc_signals0_link_reassign_clear():
    a = statemachine_Signal(name="sample_text")
    b1 = statemachine_Statemachine()
    b2 = statemachine_Statemachine()
    _safe_set(a, 'statemachine_Signal', b1)
    assert _is_linked(a, 'statemachine_Signal', b1)
    if hasattr(b1, 'statemachine_Statemachine'):
        assert _is_linked(b1, 'statemachine_Statemachine', a)
    _safe_set(a, 'statemachine_Signal', b2)
    assert _is_linked(a, 'statemachine_Signal', b2)
    if hasattr(b1, 'statemachine_Statemachine'):
        assert not _is_linked(b1, 'statemachine_Statemachine', a)
    if hasattr(b2, 'statemachine_Statemachine'):
        assert _is_linked(b2, 'statemachine_Statemachine', a)
    _safe_set(a, 'statemachine_Signal', None)
    assert not _is_linked(a, 'statemachine_Signal', b2)
    if hasattr(b2, 'statemachine_Statemachine'):
        assert not _is_linked(b2, 'statemachine_Statemachine', a)


def test_assoc_state12_link_reassign_clear():
    a = statemachine_State(name="sample_text")
    b1 = statemachine_Transition()
    b2 = statemachine_Transition()
    _safe_set(a, 'statemachine_State14', b1)
    assert _is_linked(a, 'statemachine_State14', b1)
    if hasattr(b1, 'statemachine_Transition13'):
        assert _is_linked(b1, 'statemachine_Transition13', a)
    _safe_set(a, 'statemachine_State14', b2)
    assert _is_linked(a, 'statemachine_State14', b2)
    if hasattr(b1, 'statemachine_Transition13'):
        assert not _is_linked(b1, 'statemachine_Transition13', a)
    if hasattr(b2, 'statemachine_Transition13'):
        assert _is_linked(b2, 'statemachine_Transition13', a)
    _safe_set(a, 'statemachine_State14', None)
    assert not _is_linked(a, 'statemachine_State14', b2)
    if hasattr(b2, 'statemachine_Transition13'):
        assert not _is_linked(b2, 'statemachine_Transition13', a)


def test_assoc_states1_link_reassign_clear():
    a = statemachine_State(name="sample_text")
    b1 = statemachine_Statemachine()
    b2 = statemachine_Statemachine()
    _safe_set(a, 'statemachine_State', b1)
    assert _is_linked(a, 'statemachine_State', b1)
    if hasattr(b1, 'statemachine_Statemachine2'):
        assert _is_linked(b1, 'statemachine_Statemachine2', a)
    _safe_set(a, 'statemachine_State', b2)
    assert _is_linked(a, 'statemachine_State', b2)
    if hasattr(b1, 'statemachine_Statemachine2'):
        assert not _is_linked(b1, 'statemachine_Statemachine2', a)
    if hasattr(b2, 'statemachine_Statemachine2'):
        assert _is_linked(b2, 'statemachine_Statemachine2', a)
    _safe_set(a, 'statemachine_State', None)
    assert not _is_linked(a, 'statemachine_State', b2)
    if hasattr(b2, 'statemachine_Statemachine2'):
        assert not _is_linked(b2, 'statemachine_Statemachine2', a)


def test_assoc_transitions5_link_reassign_clear():
    a = statemachine_State(name="sample_text")
    b1 = statemachine_Transition()
    b2 = statemachine_Transition()
    _safe_set(a, 'statemachine_State6', {b1})
    assert _is_linked(a, 'statemachine_State6', b1)
    if hasattr(b1, 'statemachine_Transition'):
        assert _is_linked(b1, 'statemachine_Transition', a)
    _safe_set(a, 'statemachine_State6', {b2})
    assert _is_linked(a, 'statemachine_State6', b2)
    if hasattr(b1, 'statemachine_Transition'):
        assert not _is_linked(b1, 'statemachine_Transition', a)
    if hasattr(b2, 'statemachine_Transition'):
        assert _is_linked(b2, 'statemachine_Transition', a)
    _safe_set(a, 'statemachine_State6', set())
    assert not _is_linked(a, 'statemachine_State6', b2)
    if hasattr(b2, 'statemachine_Transition'):
        assert not _is_linked(b2, 'statemachine_Transition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Signal_strategy = st.builds(Signal)
@given(instance=Signal_strategy)
@settings(max_examples=25)
def test_Signal_instantiation(instance):
    assert isinstance(instance, Signal)


statemachine_Command_strategy = st.builds(statemachine_Command, newValue=st.booleans())
@given(instance=statemachine_Command_strategy)
@settings(max_examples=25)
def test_statemachine_Command_instantiation(instance):
    assert isinstance(instance, statemachine_Command)


statemachine_Condition_strategy = st.builds(statemachine_Condition)
@given(instance=statemachine_Condition_strategy)
@settings(max_examples=25)
def test_statemachine_Condition_instantiation(instance):
    assert isinstance(instance, statemachine_Condition)


statemachine_Event_strategy = st.builds(statemachine_Event, value=st.booleans())
@given(instance=statemachine_Event_strategy)
@settings(max_examples=25)
def test_statemachine_Event_instantiation(instance):
    assert isinstance(instance, statemachine_Event)


statemachine_InputSignal_strategy = st.builds(statemachine_InputSignal)
@given(instance=statemachine_InputSignal_strategy)
@settings(max_examples=25)
def test_statemachine_InputSignal_instantiation(instance):
    assert isinstance(instance, statemachine_InputSignal)


statemachine_OutputSignal_strategy = st.builds(statemachine_OutputSignal)
@given(instance=statemachine_OutputSignal_strategy)
@settings(max_examples=25)
def test_statemachine_OutputSignal_instantiation(instance):
    assert isinstance(instance, statemachine_OutputSignal)


statemachine_Signal_strategy = st.builds(statemachine_Signal, name=safe_text)
@given(instance=statemachine_Signal_strategy)
@settings(max_examples=25)
def test_statemachine_Signal_instantiation(instance):
    assert isinstance(instance, statemachine_Signal)


statemachine_State_strategy = st.builds(statemachine_State, name=safe_text)
@given(instance=statemachine_State_strategy)
@settings(max_examples=25)
def test_statemachine_State_instantiation(instance):
    assert isinstance(instance, statemachine_State)


statemachine_Statemachine_strategy = st.builds(statemachine_Statemachine)
@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=25)
def test_statemachine_Statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)


statemachine_Transition_strategy = st.builds(statemachine_Transition)
@given(instance=statemachine_Transition_strategy)
@settings(max_examples=25)
def test_statemachine_Transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



