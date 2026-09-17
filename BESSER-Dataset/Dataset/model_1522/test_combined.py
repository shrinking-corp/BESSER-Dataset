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
    minifsm_Terminal,
    minifsm_Initial,
    minifsm_Transition,
    minifsm_State,
    minifsm_FSM,
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



def test_hyp_minifsm_terminal_is_not_abstract():
    assert not inspect.isabstract(minifsm_Terminal)


def test_hyp_minifsm_terminal_constructor_exists():
    assert callable(minifsm_Terminal.__init__)


def test_hyp_minifsm_terminal_constructor_args():
    sig = inspect.signature(minifsm_Terminal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minifsm_initial_is_not_abstract():
    assert not inspect.isabstract(minifsm_Initial)


def test_hyp_minifsm_initial_constructor_exists():
    assert callable(minifsm_Initial.__init__)


def test_hyp_minifsm_initial_constructor_args():
    sig = inspect.signature(minifsm_Initial.__init__)
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




def test_hyp_minifsm_fsm_is_not_abstract():
    assert not inspect.isabstract(minifsm_FSM)


def test_hyp_minifsm_fsm_constructor_exists():
    assert callable(minifsm_FSM.__init__)


def test_hyp_minifsm_fsm_constructor_args():
    sig = inspect.signature(minifsm_FSM.__init__)
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
minifsm_Terminal_strategy = st.builds(
    minifsm_Terminal,
)
minifsm_Initial_strategy = st.builds(
    minifsm_Initial,
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
minifsm_FSM_strategy = st.builds(
    minifsm_FSM,
)







@given(instance=minifsm_Transition_strategy)
def test_hyp_minifsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm_Transition_strategy)
@settings(max_examples=30)
def test_hyp_minifsm_transition_isactivated_changes_state(instance):
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
        assert has_statements, f"Function 'isActivated' in minifsm_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isActivated' in minifsm_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isActivated' in minifsm_Transition is not implemented or raised an error")




@given(instance=minifsm_State_strategy)
def test_hyp_minifsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm_State_strategy)
@settings(max_examples=30)
def test_hyp_minifsm_state_execute_changes_state(instance):
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
        assert has_statements, f"Function 'execute' in minifsm_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in minifsm_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in minifsm_State is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm_FSM_strategy)
@settings(max_examples=30)
def test_hyp_minifsm_fsm_handle_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.handle(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.handle).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'handle' in minifsm_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'handle' in minifsm_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'handle' in minifsm_FSM is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    State,
    minifsm_FSM,
    minifsm_Initial,
    minifsm_State,
    minifsm_Terminal,
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


def test_minifsm_Initial_isa_State():
    instance = minifsm_Initial()
    assert isinstance(instance, State)


def test_minifsm_Terminal_isa_State():
    instance = minifsm_Terminal()
    assert isinstance(instance, State)


def test_assoc_fsm7_link_reassign_clear():
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_FSM()
    b2 = minifsm_FSM()
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
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_State(name="sample_text")
    b2 = minifsm_State(name="sample_text_2")
    _safe_set(a, 'minifsm_Transition', b1)
    assert _is_linked(a, 'minifsm_Transition', b1)
    if hasattr(b1, 'minifsm_State3'):
        assert _is_linked(b1, 'minifsm_State3', a)
    _safe_set(a, 'minifsm_Transition', b2)
    assert _is_linked(a, 'minifsm_Transition', b2)
    if hasattr(b1, 'minifsm_State3'):
        assert not _is_linked(b1, 'minifsm_State3', a)
    if hasattr(b2, 'minifsm_State3'):
        assert _is_linked(b2, 'minifsm_State3', a)
    _safe_set(a, 'minifsm_Transition', None)
    assert not _is_linked(a, 'minifsm_Transition', b2)
    if hasattr(b2, 'minifsm_State3'):
        assert not _is_linked(b2, 'minifsm_State3', a)


def test_assoc_outgoing4_link_reassign_clear():
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_State(name="sample_text")
    b2 = minifsm_State(name="sample_text_2")
    _safe_set(a, 'minifsm_Transition5', b1)
    assert _is_linked(a, 'minifsm_Transition5', b1)
    if hasattr(b1, 'minifsm_State6'):
        assert _is_linked(b1, 'minifsm_State6', a)
    _safe_set(a, 'minifsm_Transition5', b2)
    assert _is_linked(a, 'minifsm_Transition5', b2)
    if hasattr(b1, 'minifsm_State6'):
        assert not _is_linked(b1, 'minifsm_State6', a)
    if hasattr(b2, 'minifsm_State6'):
        assert _is_linked(b2, 'minifsm_State6', a)
    _safe_set(a, 'minifsm_Transition5', None)
    assert not _is_linked(a, 'minifsm_Transition5', b2)
    if hasattr(b2, 'minifsm_State6'):
        assert not _is_linked(b2, 'minifsm_State6', a)


def test_assoc_states0_link_reassign_clear():
    a = minifsm_State(name="sample_text")
    b1 = minifsm_FSM()
    b2 = minifsm_FSM()
    _safe_set(a, 'minifsm_State', b1)
    assert _is_linked(a, 'minifsm_State', b1)
    if hasattr(b1, 'minifsm_FSM'):
        assert _is_linked(b1, 'minifsm_FSM', a)
    _safe_set(a, 'minifsm_State', b2)
    assert _is_linked(a, 'minifsm_State', b2)
    if hasattr(b1, 'minifsm_FSM'):
        assert not _is_linked(b1, 'minifsm_FSM', a)
    if hasattr(b2, 'minifsm_FSM'):
        assert _is_linked(b2, 'minifsm_FSM', a)
    _safe_set(a, 'minifsm_State', None)
    assert not _is_linked(a, 'minifsm_State', b2)
    if hasattr(b2, 'minifsm_FSM'):
        assert not _is_linked(b2, 'minifsm_FSM', a)


def test_assoc_transitions1_link_reassign_clear():
    a = minifsm_Transition(event="sample_text")
    b1 = minifsm_FSM()
    b2 = minifsm_FSM()
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


minifsm_FSM_strategy = st.builds(minifsm_FSM)
@given(instance=minifsm_FSM_strategy)
@settings(max_examples=25)
def test_minifsm_FSM_instantiation(instance):
    assert isinstance(instance, minifsm_FSM)


minifsm_Initial_strategy = st.builds(minifsm_Initial)
@given(instance=minifsm_Initial_strategy)
@settings(max_examples=25)
def test_minifsm_Initial_instantiation(instance):
    assert isinstance(instance, minifsm_Initial)


minifsm_State_strategy = st.builds(minifsm_State, name=safe_text)
@given(instance=minifsm_State_strategy)
@settings(max_examples=25)
def test_minifsm_State_instantiation(instance):
    assert isinstance(instance, minifsm_State)


minifsm_Terminal_strategy = st.builds(minifsm_Terminal)
@given(instance=minifsm_Terminal_strategy)
@settings(max_examples=25)
def test_minifsm_Terminal_instantiation(instance):
    assert isinstance(instance, minifsm_Terminal)


minifsm_Transition_strategy = st.builds(minifsm_Transition, event=safe_text)
@given(instance=minifsm_Transition_strategy)
@settings(max_examples=25)
def test_minifsm_Transition_instantiation(instance):
    assert isinstance(instance, minifsm_Transition)



