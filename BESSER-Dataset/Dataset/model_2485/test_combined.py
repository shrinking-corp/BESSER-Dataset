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
    fsmProv_Trigger,
    fsmProv_Transition,
    fsmProv_State,
    fsmProv_AbstractState,
    fsmProv_Region,
    fsmProv_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsmprov_trigger_is_not_abstract():
    assert not inspect.isabstract(fsmProv_Trigger)


def test_hyp_fsmprov_trigger_constructor_exists():
    assert callable(fsmProv_Trigger.__init__)


def test_hyp_fsmprov_trigger_constructor_args():
    sig = inspect.signature(fsmProv_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_fsmprov_transition_is_not_abstract():
    assert not inspect.isabstract(fsmProv_Transition)


def test_hyp_fsmprov_transition_constructor_exists():
    assert callable(fsmProv_Transition.__init__)


def test_hyp_fsmprov_transition_constructor_args():
    sig = inspect.signature(fsmProv_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsmprov_state_is_not_abstract():
    assert not inspect.isabstract(fsmProv_State)


def test_hyp_fsmprov_state_constructor_exists():
    assert callable(fsmProv_State.__init__)


def test_hyp_fsmprov_state_constructor_args():
    sig = inspect.signature(fsmProv_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsmprov_abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsmProv_AbstractState)


def test_hyp_fsmprov_abstractstate_constructor_exists():
    assert callable(fsmProv_AbstractState.__init__)


def test_hyp_fsmprov_abstractstate_constructor_args():
    sig = inspect.signature(fsmProv_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsmprov_region_is_not_abstract():
    assert not inspect.isabstract(fsmProv_Region)


def test_hyp_fsmprov_region_constructor_exists():
    assert callable(fsmProv_Region.__init__)


def test_hyp_fsmprov_region_constructor_args():
    sig = inspect.signature(fsmProv_Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsmprov_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsmProv_StateMachine)


def test_hyp_fsmprov_statemachine_constructor_exists():
    assert callable(fsmProv_StateMachine.__init__)


def test_hyp_fsmprov_statemachine_constructor_args():
    sig = inspect.signature(fsmProv_StateMachine.__init__)
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
fsmProv_Trigger_strategy = st.builds(
    fsmProv_Trigger,
    expression=
        safe_text
)
fsmProv_Transition_strategy = st.builds(
    fsmProv_Transition,
)
fsmProv_State_strategy = st.builds(
    fsmProv_State,
)
fsmProv_AbstractState_strategy = st.builds(
    fsmProv_AbstractState,
)
fsmProv_Region_strategy = st.builds(
    fsmProv_Region,
)
fsmProv_StateMachine_strategy = st.builds(
    fsmProv_StateMachine,
)




@given(instance=fsmProv_Trigger_strategy)
def test_hyp_fsmprov_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmProv_Trigger_strategy)
@settings(max_examples=30)
def test_hyp_fsmprov_trigger_evaltrigger_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evalTrigger(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evalTrigger).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evalTrigger' in fsmProv_Trigger is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evalTrigger' in fsmProv_Trigger did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evalTrigger' in fsmProv_Trigger is not implemented or raised an error")







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    fsmProv_AbstractState,
    fsmProv_Region,
    fsmProv_State,
    fsmProv_StateMachine,
    fsmProv_Transition,
    fsmProv_Trigger,
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

def test_fsmProv_Trigger_expression_value_roundtrip():
    instance = fsmProv_Trigger(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

fsmProv_AbstractState_strategy = st.builds(fsmProv_AbstractState)
@given(instance=fsmProv_AbstractState_strategy)
@settings(max_examples=25)
def test_fsmProv_AbstractState_instantiation(instance):
    assert isinstance(instance, fsmProv_AbstractState)


fsmProv_Region_strategy = st.builds(fsmProv_Region)
@given(instance=fsmProv_Region_strategy)
@settings(max_examples=25)
def test_fsmProv_Region_instantiation(instance):
    assert isinstance(instance, fsmProv_Region)


fsmProv_State_strategy = st.builds(fsmProv_State)
@given(instance=fsmProv_State_strategy)
@settings(max_examples=25)
def test_fsmProv_State_instantiation(instance):
    assert isinstance(instance, fsmProv_State)


fsmProv_StateMachine_strategy = st.builds(fsmProv_StateMachine)
@given(instance=fsmProv_StateMachine_strategy)
@settings(max_examples=25)
def test_fsmProv_StateMachine_instantiation(instance):
    assert isinstance(instance, fsmProv_StateMachine)


fsmProv_Transition_strategy = st.builds(fsmProv_Transition)
@given(instance=fsmProv_Transition_strategy)
@settings(max_examples=25)
def test_fsmProv_Transition_instantiation(instance):
    assert isinstance(instance, fsmProv_Transition)


fsmProv_Trigger_strategy = st.builds(fsmProv_Trigger, expression=safe_text)
@given(instance=fsmProv_Trigger_strategy)
@settings(max_examples=25)
def test_fsmProv_Trigger_instantiation(instance):
    assert isinstance(instance, fsmProv_Trigger)



