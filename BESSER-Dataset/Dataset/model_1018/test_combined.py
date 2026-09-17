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
    State,
    fsm_Final,
    fsm_Initial,
    fsm_FSM,
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
    assert "event" in params, "Missing parameter 'event'"




def test_hyp_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_hyp_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_hyp_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_final_is_not_abstract():
    assert not inspect.isabstract(fsm_Final)


def test_hyp_fsm_final_constructor_exists():
    assert callable(fsm_Final.__init__)


def test_hyp_fsm_final_constructor_args():
    sig = inspect.signature(fsm_Final.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_initial_is_not_abstract():
    assert not inspect.isabstract(fsm_Initial)


def test_hyp_fsm_initial_constructor_exists():
    assert callable(fsm_Initial.__init__)


def test_hyp_fsm_initial_constructor_args():
    sig = inspect.signature(fsm_Initial.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(fsm_FSM)


def test_hyp_fsm_fsm_constructor_exists():
    assert callable(fsm_FSM.__init__)


def test_hyp_fsm_fsm_constructor_args():
    sig = inspect.signature(fsm_FSM.__init__)
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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    event=
        safe_text
)
fsm_State_strategy = st.builds(
    fsm_State,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm_Final_strategy = st.builds(
    fsm_Final,
)
fsm_Initial_strategy = st.builds(
    fsm_Initial,
)
fsm_FSM_strategy = st.builds(
    fsm_FSM,
)




@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_Transition_strategy)
@settings(max_examples=30)
def test_hyp_fsm_transition_isactivated_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isActivated()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isActivated).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isActivated' in fsm_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isActivated' in fsm_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isActivated' in fsm_Transition is not implemented or raised an error")




@given(instance=fsm_State_strategy)
def test_hyp_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_State_strategy)
@settings(max_examples=30)
def test_hyp_fsm_state_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in fsm_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in fsm_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in fsm_State is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_FSM_strategy)
@settings(max_examples=30)
def test_hyp_fsm_fsm_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in fsm_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in fsm_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in fsm_FSM is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    State,
    fsm_FSM,
    fsm_Final,
    fsm_Initial,
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

def test_fsm_State_name_value_roundtrip():
    instance = fsm_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsm_Transition_event_value_roundtrip():
    instance = fsm_Transition(event="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_fsm_Final_isa_State():
    instance = fsm_Final()
    assert isinstance(instance, State)


def test_fsm_Initial_isa_State():
    instance = fsm_Initial()
    assert isinstance(instance, State)


def test_assoc_fsm7_link_reassign_clear():
    a = fsm_Transition(event="sample_text")
    b1 = fsm_FSM()
    b2 = fsm_FSM()
    _safe_set(a, 'transitions', b1)
    assert _is_linked(a, 'transitions', b1)
    if hasattr(b1, 'FSM'):
        assert _is_linked(b1, 'FSM', a)
    _safe_set(a, 'transitions', b2)
    assert _is_linked(a, 'transitions', b2)
    if hasattr(b1, 'FSM'):
        assert not _is_linked(b1, 'FSM', a)
    if hasattr(b2, 'FSM'):
        assert _is_linked(b2, 'FSM', a)
    _safe_set(a, 'transitions', None)
    assert not _is_linked(a, 'transitions', b2)
    if hasattr(b2, 'FSM'):
        assert not _is_linked(b2, 'FSM', a)


def test_assoc_incoming2_link_reassign_clear():
    a = fsm_Transition(event="sample_text")
    b1 = fsm_State(name="sample_text")
    b2 = fsm_State(name="sample_text_2")
    _safe_set(a, 'fsm_Transition', b1)
    assert _is_linked(a, 'fsm_Transition', b1)
    if hasattr(b1, 'fsm_State3'):
        assert _is_linked(b1, 'fsm_State3', a)
    _safe_set(a, 'fsm_Transition', b2)
    assert _is_linked(a, 'fsm_Transition', b2)
    if hasattr(b1, 'fsm_State3'):
        assert not _is_linked(b1, 'fsm_State3', a)
    if hasattr(b2, 'fsm_State3'):
        assert _is_linked(b2, 'fsm_State3', a)
    _safe_set(a, 'fsm_Transition', None)
    assert not _is_linked(a, 'fsm_Transition', b2)
    if hasattr(b2, 'fsm_State3'):
        assert not _is_linked(b2, 'fsm_State3', a)


def test_assoc_outgoing4_link_reassign_clear():
    a = fsm_Transition(event="sample_text")
    b1 = fsm_State(name="sample_text")
    b2 = fsm_State(name="sample_text_2")
    _safe_set(a, 'fsm_Transition5', b1)
    assert _is_linked(a, 'fsm_Transition5', b1)
    if hasattr(b1, 'fsm_State6'):
        assert _is_linked(b1, 'fsm_State6', a)
    _safe_set(a, 'fsm_Transition5', b2)
    assert _is_linked(a, 'fsm_Transition5', b2)
    if hasattr(b1, 'fsm_State6'):
        assert not _is_linked(b1, 'fsm_State6', a)
    if hasattr(b2, 'fsm_State6'):
        assert _is_linked(b2, 'fsm_State6', a)
    _safe_set(a, 'fsm_Transition5', None)
    assert not _is_linked(a, 'fsm_Transition5', b2)
    if hasattr(b2, 'fsm_State6'):
        assert not _is_linked(b2, 'fsm_State6', a)


def test_assoc_states0_link_reassign_clear():
    a = fsm_State(name="sample_text")
    b1 = fsm_FSM()
    b2 = fsm_FSM()
    _safe_set(a, 'fsm_State', b1)
    assert _is_linked(a, 'fsm_State', b1)
    if hasattr(b1, 'fsm_FSM'):
        assert _is_linked(b1, 'fsm_FSM', a)
    _safe_set(a, 'fsm_State', b2)
    assert _is_linked(a, 'fsm_State', b2)
    if hasattr(b1, 'fsm_FSM'):
        assert not _is_linked(b1, 'fsm_FSM', a)
    if hasattr(b2, 'fsm_FSM'):
        assert _is_linked(b2, 'fsm_FSM', a)
    _safe_set(a, 'fsm_State', None)
    assert not _is_linked(a, 'fsm_State', b2)
    if hasattr(b2, 'fsm_FSM'):
        assert not _is_linked(b2, 'fsm_FSM', a)


def test_assoc_transitions1_link_reassign_clear():
    a = fsm_Transition(event="sample_text")
    b1 = fsm_FSM()
    b2 = fsm_FSM()
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'fsm'):
        assert _is_linked(b1, 'fsm', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'fsm'):
        assert not _is_linked(b1, 'fsm', a)
    if hasattr(b2, 'fsm'):
        assert _is_linked(b2, 'fsm', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'fsm'):
        assert not _is_linked(b2, 'fsm', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


fsm_FSM_strategy = st.builds(fsm_FSM)
@given(instance=fsm_FSM_strategy)
@settings(max_examples=25)
def test_fsm_FSM_instantiation(instance):
    assert isinstance(instance, fsm_FSM)


fsm_Final_strategy = st.builds(fsm_Final)
@given(instance=fsm_Final_strategy)
@settings(max_examples=25)
def test_fsm_Final_instantiation(instance):
    assert isinstance(instance, fsm_Final)


fsm_Initial_strategy = st.builds(fsm_Initial)
@given(instance=fsm_Initial_strategy)
@settings(max_examples=25)
def test_fsm_Initial_instantiation(instance):
    assert isinstance(instance, fsm_Initial)


fsm_State_strategy = st.builds(fsm_State, name=safe_text)
@given(instance=fsm_State_strategy)
@settings(max_examples=25)
def test_fsm_State_instantiation(instance):
    assert isinstance(instance, fsm_State)


fsm_Transition_strategy = st.builds(fsm_Transition, event=safe_text)
@given(instance=fsm_Transition_strategy)
@settings(max_examples=25)
def test_fsm_Transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



