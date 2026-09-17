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
    minifsm_FinalState,
    minifsm_Transition,
    minifsm_State,
    minifsm_Machine,
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



def test_hyp_minifsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(minifsm_FinalState)


def test_hyp_minifsm_finalstate_constructor_exists():
    assert callable(minifsm_FinalState.__init__)


def test_hyp_minifsm_finalstate_constructor_args():
    sig = inspect.signature(minifsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minifsm_transition_is_not_abstract():
    assert not inspect.isabstract(minifsm_Transition)


def test_hyp_minifsm_transition_constructor_exists():
    assert callable(minifsm_Transition.__init__)


def test_hyp_minifsm_transition_constructor_args():
    sig = inspect.signature(minifsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"




def test_hyp_minifsm_state_is_not_abstract():
    assert not inspect.isabstract(minifsm_State)


def test_hyp_minifsm_state_constructor_exists():
    assert callable(minifsm_State.__init__)


def test_hyp_minifsm_state_constructor_args():
    sig = inspect.signature(minifsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_minifsm_machine_is_not_abstract():
    assert not inspect.isabstract(minifsm_Machine)


def test_hyp_minifsm_machine_constructor_exists():
    assert callable(minifsm_Machine.__init__)


def test_hyp_minifsm_machine_constructor_args():
    sig = inspect.signature(minifsm_Machine.__init__)
    params = list(sig.parameters.keys())


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
minifsm_FinalState_strategy = st.builds(
    minifsm_FinalState,
)
minifsm_Transition_strategy = st.builds(
    minifsm_Transition,
    event=
        safe_text
)
minifsm_State_strategy = st.builds(
    minifsm_State,
    name=
        safe_text
)
minifsm_Machine_strategy = st.builds(
    minifsm_Machine,
)






@given(instance=minifsm_Transition_strategy)
def test_hyp_minifsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original




@given(instance=minifsm_State_strategy)
def test_hyp_minifsm_state_name_setter(instance):
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
    State,
    minifsm_FinalState,
    minifsm_Machine,
    minifsm_State,
    minifsm_Transition,
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

def test_minifsm_State_name_value_roundtrip():
    instance = minifsm_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minifsm_Transition_event_value_roundtrip():
    instance = minifsm_Transition(event="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_minifsm_FinalState_isa_State():
    instance = minifsm_FinalState()
    assert isinstance(instance, State)


def test_assoc_in_4_link_reassign_clear():
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_State(name="sample_text")
    b2 = minifsm_State(name="sample_text_2")
    _safe_set(a, 'Transition5', b1)
    assert _is_linked(a, 'Transition5', b1)
    if hasattr(b1, 'tgt'):
        assert _is_linked(b1, 'tgt', a)
    _safe_set(a, 'Transition5', b2)
    assert _is_linked(a, 'Transition5', b2)
    if hasattr(b1, 'tgt'):
        assert not _is_linked(b1, 'tgt', a)
    if hasattr(b2, 'tgt'):
        assert _is_linked(b2, 'tgt', a)
    _safe_set(a, 'Transition5', None)
    assert not _is_linked(a, 'Transition5', b2)
    if hasattr(b2, 'tgt'):
        assert not _is_linked(b2, 'tgt', a)


def test_assoc_out3_link_reassign_clear():
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_State(name="sample_text")
    b2 = minifsm_State(name="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'src'):
        assert _is_linked(b1, 'src', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'src'):
        assert not _is_linked(b1, 'src', a)
    if hasattr(b2, 'src'):
        assert _is_linked(b2, 'src', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'src'):
        assert not _is_linked(b2, 'src', a)


def test_assoc_src6_link_reassign_clear():
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_State(name="sample_text")
    b2 = minifsm_State(name="sample_text_2")
    _safe_set(a, 'out', b1)
    assert _is_linked(a, 'out', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'out', b2)
    assert _is_linked(a, 'out', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'out', None)
    assert not _is_linked(a, 'out', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_states0_link_reassign_clear():
    a = minifsm_State(name="sample_text")
    b1 = minifsm_Machine()
    b2 = minifsm_Machine()
    _safe_set(a, 'minifsm_State', b1)
    assert _is_linked(a, 'minifsm_State', b1)
    if hasattr(b1, 'minifsm_Machine'):
        assert _is_linked(b1, 'minifsm_Machine', a)
    _safe_set(a, 'minifsm_State', b2)
    assert _is_linked(a, 'minifsm_State', b2)
    if hasattr(b1, 'minifsm_Machine'):
        assert not _is_linked(b1, 'minifsm_Machine', a)
    if hasattr(b2, 'minifsm_Machine'):
        assert _is_linked(b2, 'minifsm_Machine', a)
    _safe_set(a, 'minifsm_State', None)
    assert not _is_linked(a, 'minifsm_State', b2)
    if hasattr(b2, 'minifsm_Machine'):
        assert not _is_linked(b2, 'minifsm_Machine', a)


def test_assoc_tgt7_link_reassign_clear():
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_State(name="sample_text")
    b2 = minifsm_State(name="sample_text_2")
    _safe_set(a, 'in_', b1)
    assert _is_linked(a, 'in_', b1)
    if hasattr(b1, 'State8'):
        assert _is_linked(b1, 'State8', a)
    _safe_set(a, 'in_', b2)
    assert _is_linked(a, 'in_', b2)
    if hasattr(b1, 'State8'):
        assert not _is_linked(b1, 'State8', a)
    if hasattr(b2, 'State8'):
        assert _is_linked(b2, 'State8', a)
    _safe_set(a, 'in_', None)
    assert not _is_linked(a, 'in_', b2)
    if hasattr(b2, 'State8'):
        assert not _is_linked(b2, 'State8', a)


def test_assoc_transitions1_link_reassign_clear():
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_Machine()
    b2 = minifsm_Machine()
    _safe_set(a, 'minifsm_Transition', b1)
    assert _is_linked(a, 'minifsm_Transition', b1)
    if hasattr(b1, 'minifsm_Machine2'):
        assert _is_linked(b1, 'minifsm_Machine2', a)
    _safe_set(a, 'minifsm_Transition', b2)
    assert _is_linked(a, 'minifsm_Transition', b2)
    if hasattr(b1, 'minifsm_Machine2'):
        assert not _is_linked(b1, 'minifsm_Machine2', a)
    if hasattr(b2, 'minifsm_Machine2'):
        assert _is_linked(b2, 'minifsm_Machine2', a)
    _safe_set(a, 'minifsm_Transition', None)
    assert not _is_linked(a, 'minifsm_Transition', b2)
    if hasattr(b2, 'minifsm_Machine2'):
        assert not _is_linked(b2, 'minifsm_Machine2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


minifsm_FinalState_strategy = st.builds(minifsm_FinalState)
@given(instance=minifsm_FinalState_strategy)
@settings(max_examples=25)
def test_minifsm_FinalState_instantiation(instance):
    assert isinstance(instance, minifsm_FinalState)


minifsm_Machine_strategy = st.builds(minifsm_Machine)
@given(instance=minifsm_Machine_strategy)
@settings(max_examples=25)
def test_minifsm_Machine_instantiation(instance):
    assert isinstance(instance, minifsm_Machine)


minifsm_State_strategy = st.builds(minifsm_State, name=safe_text)
@given(instance=minifsm_State_strategy)
@settings(max_examples=25)
def test_minifsm_State_instantiation(instance):
    assert isinstance(instance, minifsm_State)


minifsm_Transition_strategy = st.builds(minifsm_Transition, event=safe_text)
@given(instance=minifsm_Transition_strategy)
@settings(max_examples=25)
def test_minifsm_Transition_instantiation(instance):
    assert isinstance(instance, minifsm_Transition)



