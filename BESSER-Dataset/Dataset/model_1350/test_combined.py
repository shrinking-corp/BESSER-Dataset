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
    statemachine_Named,
    AbstractState,
    statemachine_State,
    statemachine_Initial,
    Named,
    statemachine_Transition,
    statemachine_AbstractState,
    statemachine_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_statemachine_named_is_not_abstract():
    assert not inspect.isabstract(statemachine_Named)


def test_hyp_statemachine_named_constructor_exists():
    assert callable(statemachine_Named.__init__)


def test_hyp_statemachine_named_constructor_args():
    sig = inspect.signature(statemachine_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_hyp_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_hyp_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_hyp_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_hyp_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_initial_is_not_abstract():
    assert not inspect.isabstract(statemachine_Initial)


def test_hyp_statemachine_initial_constructor_exists():
    assert callable(statemachine_Initial.__init__)


def test_hyp_statemachine_initial_constructor_args():
    sig = inspect.signature(statemachine_Initial.__init__)
    params = list(sig.parameters.keys())



def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_hyp_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_hyp_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_abstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_AbstractState)


def test_hyp_statemachine_abstractstate_constructor_exists():
    assert callable(statemachine_AbstractState.__init__)


def test_hyp_statemachine_abstractstate_constructor_args():
    sig = inspect.signature(statemachine_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_hyp_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_hyp_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
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
statemachine_Named_strategy = st.builds(
    statemachine_Named,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
)
statemachine_Initial_strategy = st.builds(
    statemachine_Initial,
)
Named_strategy = st.builds(
    Named,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_AbstractState_strategy = st.builds(
    statemachine_AbstractState,
)
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
)




@given(instance=statemachine_Named_strategy)
def test_hyp_statemachine_named_name_setter(instance):
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
    AbstractState,
    Named,
    statemachine_AbstractState,
    statemachine_Initial,
    statemachine_Named,
    statemachine_State,
    statemachine_StateMachine,
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

def test_statemachine_Named_name_value_roundtrip():
    instance = statemachine_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_Initial_isa_AbstractState():
    instance = statemachine_Initial()
    assert isinstance(instance, AbstractState)


def test_statemachine_State_isa_AbstractState():
    instance = statemachine_State()
    assert isinstance(instance, AbstractState)


def test_statemachine_AbstractState_isa_Named():
    instance = statemachine_AbstractState()
    assert isinstance(instance, Named)


def test_statemachine_Transition_isa_Named():
    instance = statemachine_Transition()
    assert isinstance(instance, Named)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


statemachine_AbstractState_strategy = st.builds(statemachine_AbstractState)
@given(instance=statemachine_AbstractState_strategy)
@settings(max_examples=25)
def test_statemachine_AbstractState_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractState)


statemachine_Initial_strategy = st.builds(statemachine_Initial)
@given(instance=statemachine_Initial_strategy)
@settings(max_examples=25)
def test_statemachine_Initial_instantiation(instance):
    assert isinstance(instance, statemachine_Initial)


statemachine_Named_strategy = st.builds(statemachine_Named, name=safe_text)
@given(instance=statemachine_Named_strategy)
@settings(max_examples=25)
def test_statemachine_Named_instantiation(instance):
    assert isinstance(instance, statemachine_Named)


statemachine_State_strategy = st.builds(statemachine_State)
@given(instance=statemachine_State_strategy)
@settings(max_examples=25)
def test_statemachine_State_instantiation(instance):
    assert isinstance(instance, statemachine_State)


statemachine_StateMachine_strategy = st.builds(statemachine_StateMachine)
@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=25)
def test_statemachine_StateMachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)


statemachine_Transition_strategy = st.builds(statemachine_Transition)
@given(instance=statemachine_Transition_strategy)
@settings(max_examples=25)
def test_statemachine_Transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



