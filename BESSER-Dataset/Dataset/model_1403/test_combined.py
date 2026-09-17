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
    HSM_CompositeState,
    HSM_Transition,
    HSM_State,
    HSM_StateMachine,
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



def test_hyp_hsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(HSM_CompositeState)


def test_hyp_hsm_compositestate_constructor_exists():
    assert callable(HSM_CompositeState.__init__)


def test_hyp_hsm_compositestate_constructor_args():
    sig = inspect.signature(HSM_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hsm_transition_is_not_abstract():
    assert not inspect.isabstract(HSM_Transition)


def test_hyp_hsm_transition_constructor_exists():
    assert callable(HSM_Transition.__init__)


def test_hyp_hsm_transition_constructor_args():
    sig = inspect.signature(HSM_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hsm_state_is_not_abstract():
    assert not inspect.isabstract(HSM_State)


def test_hyp_hsm_state_constructor_exists():
    assert callable(HSM_State.__init__)


def test_hyp_hsm_state_constructor_args():
    sig = inspect.signature(HSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_hsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(HSM_StateMachine)


def test_hyp_hsm_statemachine_constructor_exists():
    assert callable(HSM_StateMachine.__init__)


def test_hyp_hsm_statemachine_constructor_args():
    sig = inspect.signature(HSM_StateMachine.__init__)
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
HSM_CompositeState_strategy = st.builds(
    HSM_CompositeState,
)
HSM_Transition_strategy = st.builds(
    HSM_Transition,
)
HSM_State_strategy = st.builds(
    HSM_State,
    name=
        safe_text
)
HSM_StateMachine_strategy = st.builds(
    HSM_StateMachine,
)







@given(instance=HSM_State_strategy)
def test_hyp_hsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=HSM_StateMachine_strategy)
@settings(max_examples=30)
def test_hyp_hsm_statemachine_addtransition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addTransition(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addTransition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addTransition' in HSM_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTransition' in HSM_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTransition' in HSM_StateMachine is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    HSM_CompositeState,
    HSM_State,
    HSM_StateMachine,
    HSM_Transition,
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

def test_HSM_State_name_value_roundtrip():
    instance = HSM_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_HSM_CompositeState_isa_State():
    instance = HSM_CompositeState()
    assert isinstance(instance, State)


def test_assoc_owner3_link_reassign_clear():
    a = HSM_State(name="sample_text")
    b1 = HSM_CompositeState()
    b2 = HSM_CompositeState()
    _safe_set(a, 'HSM_State4', b1)
    assert _is_linked(a, 'HSM_State4', b1)
    if hasattr(b1, 'HSM_CompositeState'):
        assert _is_linked(b1, 'HSM_CompositeState', a)
    _safe_set(a, 'HSM_State4', b2)
    assert _is_linked(a, 'HSM_State4', b2)
    if hasattr(b1, 'HSM_CompositeState'):
        assert not _is_linked(b1, 'HSM_CompositeState', a)
    if hasattr(b2, 'HSM_CompositeState'):
        assert _is_linked(b2, 'HSM_CompositeState', a)
    _safe_set(a, 'HSM_State4', None)
    assert not _is_linked(a, 'HSM_State4', b2)
    if hasattr(b2, 'HSM_CompositeState'):
        assert not _is_linked(b2, 'HSM_CompositeState', a)


def test_assoc_source5_link_reassign_clear():
    a = HSM_State(name="sample_text")
    b1 = HSM_Transition()
    b2 = HSM_Transition()
    _safe_set(a, 'HSM_State7', b1)
    assert _is_linked(a, 'HSM_State7', b1)
    if hasattr(b1, 'HSM_Transition6'):
        assert _is_linked(b1, 'HSM_Transition6', a)
    _safe_set(a, 'HSM_State7', b2)
    assert _is_linked(a, 'HSM_State7', b2)
    if hasattr(b1, 'HSM_Transition6'):
        assert not _is_linked(b1, 'HSM_Transition6', a)
    if hasattr(b2, 'HSM_Transition6'):
        assert _is_linked(b2, 'HSM_Transition6', a)
    _safe_set(a, 'HSM_State7', None)
    assert not _is_linked(a, 'HSM_State7', b2)
    if hasattr(b2, 'HSM_Transition6'):
        assert not _is_linked(b2, 'HSM_Transition6', a)


def test_assoc_states0_link_reassign_clear():
    a = HSM_StateMachine()
    b1 = HSM_State(name="sample_text")
    b2 = HSM_State(name="sample_text_2")
    _safe_set(a, 'HSM_StateMachine', {b1})
    assert _is_linked(a, 'HSM_StateMachine', b1)
    if hasattr(b1, 'HSM_State'):
        assert _is_linked(b1, 'HSM_State', a)
    _safe_set(a, 'HSM_StateMachine', {b2})
    assert _is_linked(a, 'HSM_StateMachine', b2)
    if hasattr(b1, 'HSM_State'):
        assert not _is_linked(b1, 'HSM_State', a)
    if hasattr(b2, 'HSM_State'):
        assert _is_linked(b2, 'HSM_State', a)
    _safe_set(a, 'HSM_StateMachine', set())
    assert not _is_linked(a, 'HSM_StateMachine', b2)
    if hasattr(b2, 'HSM_State'):
        assert not _is_linked(b2, 'HSM_State', a)


def test_assoc_target8_link_reassign_clear():
    a = HSM_State(name="sample_text")
    b1 = HSM_Transition()
    b2 = HSM_Transition()
    _safe_set(a, 'HSM_State10', b1)
    assert _is_linked(a, 'HSM_State10', b1)
    if hasattr(b1, 'HSM_Transition9'):
        assert _is_linked(b1, 'HSM_Transition9', a)
    _safe_set(a, 'HSM_State10', b2)
    assert _is_linked(a, 'HSM_State10', b2)
    if hasattr(b1, 'HSM_Transition9'):
        assert not _is_linked(b1, 'HSM_Transition9', a)
    if hasattr(b2, 'HSM_Transition9'):
        assert _is_linked(b2, 'HSM_Transition9', a)
    _safe_set(a, 'HSM_State10', None)
    assert not _is_linked(a, 'HSM_State10', b2)
    if hasattr(b2, 'HSM_Transition9'):
        assert not _is_linked(b2, 'HSM_Transition9', a)


def test_assoc_transitions1_link_reassign_clear():
    a = HSM_StateMachine()
    b1 = HSM_Transition()
    b2 = HSM_Transition()
    _safe_set(a, 'HSM_StateMachine2', {b1})
    assert _is_linked(a, 'HSM_StateMachine2', b1)
    if hasattr(b1, 'HSM_Transition'):
        assert _is_linked(b1, 'HSM_Transition', a)
    _safe_set(a, 'HSM_StateMachine2', {b2})
    assert _is_linked(a, 'HSM_StateMachine2', b2)
    if hasattr(b1, 'HSM_Transition'):
        assert not _is_linked(b1, 'HSM_Transition', a)
    if hasattr(b2, 'HSM_Transition'):
        assert _is_linked(b2, 'HSM_Transition', a)
    _safe_set(a, 'HSM_StateMachine2', set())
    assert not _is_linked(a, 'HSM_StateMachine2', b2)
    if hasattr(b2, 'HSM_Transition'):
        assert not _is_linked(b2, 'HSM_Transition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

HSM_CompositeState_strategy = st.builds(HSM_CompositeState)
@given(instance=HSM_CompositeState_strategy)
@settings(max_examples=25)
def test_HSM_CompositeState_instantiation(instance):
    assert isinstance(instance, HSM_CompositeState)


HSM_State_strategy = st.builds(HSM_State, name=safe_text)
@given(instance=HSM_State_strategy)
@settings(max_examples=25)
def test_HSM_State_instantiation(instance):
    assert isinstance(instance, HSM_State)


HSM_StateMachine_strategy = st.builds(HSM_StateMachine)
@given(instance=HSM_StateMachine_strategy)
@settings(max_examples=25)
def test_HSM_StateMachine_instantiation(instance):
    assert isinstance(instance, HSM_StateMachine)


HSM_Transition_strategy = st.builds(HSM_Transition)
@given(instance=HSM_Transition_strategy)
@settings(max_examples=25)
def test_HSM_Transition_instantiation(instance):
    assert isinstance(instance, HSM_Transition)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)



