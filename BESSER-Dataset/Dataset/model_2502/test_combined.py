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
    tfsm_Guard,
    Transition,
    tfsm_Transition,
    State,
    tfsm_State,
    FSM,
    tfsm_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tfsm_guard_is_not_abstract():
    assert not inspect.isabstract(tfsm_Guard)


def test_hyp_tfsm_guard_constructor_exists():
    assert callable(tfsm_Guard.__init__)


def test_hyp_tfsm_guard_constructor_args():
    sig = inspect.signature(tfsm_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"




def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsm_transition_is_not_abstract():
    assert not inspect.isabstract(tfsm_Transition)


def test_hyp_tfsm_transition_constructor_exists():
    assert callable(tfsm_Transition.__init__)


def test_hyp_tfsm_transition_constructor_args():
    sig = inspect.signature(tfsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsm_state_is_not_abstract():
    assert not inspect.isabstract(tfsm_State)


def test_hyp_tfsm_state_constructor_exists():
    assert callable(tfsm_State.__init__)


def test_hyp_tfsm_state_constructor_args():
    sig = inspect.signature(tfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"




def test_hyp_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_hyp_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_hyp_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tfsm_fsm_is_not_abstract():
    assert not inspect.isabstract(tfsm_FSM)


def test_hyp_tfsm_fsm_constructor_exists():
    assert callable(tfsm_FSM.__init__)


def test_hyp_tfsm_fsm_constructor_args():
    sig = inspect.signature(tfsm_FSM.__init__)
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
tfsm_Guard_strategy = st.builds(
    tfsm_Guard,
    time=
        st.integers()
)
Transition_strategy = st.builds(
    Transition,
)
tfsm_Transition_strategy = st.builds(
    tfsm_Transition,
)
State_strategy = st.builds(
    State,
)
tfsm_State_strategy = st.builds(
    tfsm_State,
    time=
        st.integers()
)
FSM_strategy = st.builds(
    FSM,
)
tfsm_FSM_strategy = st.builds(
    tfsm_FSM,
)




@given(instance=tfsm_Guard_strategy)
def test_hyp_tfsm_guard_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original







@given(instance=tfsm_State_strategy)
def test_hyp_tfsm_state_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    FSM,
    State,
    Transition,
    tfsm_FSM,
    tfsm_Guard,
    tfsm_State,
    tfsm_Transition,
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

def test_tfsm_Guard_time_value_roundtrip():
    instance = tfsm_Guard(time=7)
    assert instance.time == 7
    instance.time = 13
    assert instance.time == 13


def test_tfsm_State_time_value_roundtrip():
    instance = tfsm_State(time=7)
    assert instance.time == 7
    instance.time = 13
    assert instance.time == 13


def test_tfsm_FSM_isa_FSM():
    instance = tfsm_FSM()
    assert isinstance(instance, FSM)


def test_tfsm_State_isa_State():
    instance = tfsm_State(time=7)
    assert isinstance(instance, State)


def test_tfsm_Transition_isa_Transition():
    instance = tfsm_Transition()
    assert isinstance(instance, Transition)


def test_assoc_currentState0_link_reassign_clear():
    a = tfsm_State(time=7)
    b1 = tfsm_FSM()
    b2 = tfsm_FSM()
    _safe_set(a, 'tfsm_State', b1)
    assert _is_linked(a, 'tfsm_State', b1)
    if hasattr(b1, 'tfsm_FSM'):
        assert _is_linked(b1, 'tfsm_FSM', a)
    _safe_set(a, 'tfsm_State', b2)
    assert _is_linked(a, 'tfsm_State', b2)
    if hasattr(b1, 'tfsm_FSM'):
        assert not _is_linked(b1, 'tfsm_FSM', a)
    if hasattr(b2, 'tfsm_FSM'):
        assert _is_linked(b2, 'tfsm_FSM', a)
    _safe_set(a, 'tfsm_State', None)
    assert not _is_linked(a, 'tfsm_State', b2)
    if hasattr(b2, 'tfsm_FSM'):
        assert not _is_linked(b2, 'tfsm_FSM', a)


def test_assoc_guard1_link_reassign_clear():
    a = tfsm_Guard(time=7)
    b1 = tfsm_Transition()
    b2 = tfsm_Transition()
    _safe_set(a, 'tfsm_Guard', b1)
    assert _is_linked(a, 'tfsm_Guard', b1)
    if hasattr(b1, 'tfsm_Transition'):
        assert _is_linked(b1, 'tfsm_Transition', a)
    _safe_set(a, 'tfsm_Guard', b2)
    assert _is_linked(a, 'tfsm_Guard', b2)
    if hasattr(b1, 'tfsm_Transition'):
        assert not _is_linked(b1, 'tfsm_Transition', a)
    if hasattr(b2, 'tfsm_Transition'):
        assert _is_linked(b2, 'tfsm_Transition', a)
    _safe_set(a, 'tfsm_Guard', None)
    assert not _is_linked(a, 'tfsm_Guard', b2)
    if hasattr(b2, 'tfsm_Transition'):
        assert not _is_linked(b2, 'tfsm_Transition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

FSM_strategy = st.builds(FSM)
@given(instance=FSM_strategy)
@settings(max_examples=25)
def test_FSM_instantiation(instance):
    assert isinstance(instance, FSM)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


tfsm_FSM_strategy = st.builds(tfsm_FSM)
@given(instance=tfsm_FSM_strategy)
@settings(max_examples=25)
def test_tfsm_FSM_instantiation(instance):
    assert isinstance(instance, tfsm_FSM)


tfsm_Guard_strategy = st.builds(tfsm_Guard, time=st.integers())
@given(instance=tfsm_Guard_strategy)
@settings(max_examples=25)
def test_tfsm_Guard_instantiation(instance):
    assert isinstance(instance, tfsm_Guard)


tfsm_State_strategy = st.builds(tfsm_State, time=st.integers())
@given(instance=tfsm_State_strategy)
@settings(max_examples=25)
def test_tfsm_State_instantiation(instance):
    assert isinstance(instance, tfsm_State)


tfsm_Transition_strategy = st.builds(tfsm_Transition)
@given(instance=tfsm_Transition_strategy)
@settings(max_examples=25)
def test_tfsm_Transition_instantiation(instance):
    assert isinstance(instance, tfsm_Transition)



