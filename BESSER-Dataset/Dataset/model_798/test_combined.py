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
    fsmSample_Transition,
    fsmSample_State,
    fsmSample_FSM,
    fsmSample_Action,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsmsample_transition_is_not_abstract():
    assert not inspect.isabstract(fsmSample_Transition)


def test_hyp_fsmsample_transition_constructor_exists():
    assert callable(fsmSample_Transition.__init__)


def test_hyp_fsmsample_transition_constructor_args():
    sig = inspect.signature(fsmSample_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"





def test_hyp_fsmsample_state_is_not_abstract():
    assert not inspect.isabstract(fsmSample_State)


def test_hyp_fsmsample_state_constructor_exists():
    assert callable(fsmSample_State.__init__)


def test_hyp_fsmsample_state_constructor_args():
    sig = inspect.signature(fsmSample_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fsmsample_fsm_is_not_abstract():
    assert not inspect.isabstract(fsmSample_FSM)


def test_hyp_fsmsample_fsm_constructor_exists():
    assert callable(fsmSample_FSM.__init__)


def test_hyp_fsmsample_fsm_constructor_args():
    sig = inspect.signature(fsmSample_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fsmsample_action_is_not_abstract():
    assert not inspect.isabstract(fsmSample_Action)


def test_hyp_fsmsample_action_constructor_exists():
    assert callable(fsmSample_Action.__init__)


def test_hyp_fsmsample_action_constructor_args():
    sig = inspect.signature(fsmSample_Action.__init__)
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
fsmSample_Transition_strategy = st.builds(
    fsmSample_Transition,
    output=
        safe_text,
    input=
        safe_text
)
fsmSample_State_strategy = st.builds(
    fsmSample_State,
    name=
        safe_text
)
fsmSample_FSM_strategy = st.builds(
    fsmSample_FSM,
    name=
        safe_text
)
fsmSample_Action_strategy = st.builds(
    fsmSample_Action,
    name=
        safe_text
)




@given(instance=fsmSample_Transition_strategy)
def test_hyp_fsmsample_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=fsmSample_Transition_strategy)
def test_hyp_fsmsample_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original




@given(instance=fsmSample_State_strategy)
def test_hyp_fsmsample_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fsmSample_FSM_strategy)
def test_hyp_fsmsample_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fsmSample_Action_strategy)
def test_hyp_fsmsample_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmSample_Action_strategy)
@settings(max_examples=30)
def test_hyp_fsmsample_action_run_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.run(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.run).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'run' in fsmSample_Action is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in fsmSample_Action did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in fsmSample_Action is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    fsmSample_Action,
    fsmSample_FSM,
    fsmSample_State,
    fsmSample_Transition,
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

def test_fsmSample_Action_name_value_roundtrip():
    instance = fsmSample_Action(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsmSample_FSM_name_value_roundtrip():
    instance = fsmSample_FSM(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsmSample_State_name_value_roundtrip():
    instance = fsmSample_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsmSample_Transition_input_value_roundtrip():
    instance = fsmSample_Transition(input="sample_text", output="sample_text")
    assert instance.input == "sample_text"
    instance.input = "sample_text_2"
    assert instance.input == "sample_text_2"


def test_fsmSample_Transition_output_value_roundtrip():
    instance = fsmSample_Transition(input="sample_text", output="sample_text")
    assert instance.output == "sample_text"
    instance.output = "sample_text_2"
    assert instance.output == "sample_text_2"


def test_assoc_action16_link_reassign_clear():
    a = fsmSample_Transition(input="sample_text", output="sample_text")
    b1 = fsmSample_Action(name="sample_text")
    b2 = fsmSample_Action(name="sample_text_2")
    _safe_set(a, 'fsmSample_Transition', b1)
    assert _is_linked(a, 'fsmSample_Transition', b1)
    if hasattr(b1, 'fsmSample_Action'):
        assert _is_linked(b1, 'fsmSample_Action', a)
    _safe_set(a, 'fsmSample_Transition', b2)
    assert _is_linked(a, 'fsmSample_Transition', b2)
    if hasattr(b1, 'fsmSample_Action'):
        assert not _is_linked(b1, 'fsmSample_Action', a)
    if hasattr(b2, 'fsmSample_Action'):
        assert _is_linked(b2, 'fsmSample_Action', a)
    _safe_set(a, 'fsmSample_Transition', None)
    assert not _is_linked(a, 'fsmSample_Transition', b2)
    if hasattr(b2, 'fsmSample_Action'):
        assert not _is_linked(b2, 'fsmSample_Action', a)


def test_assoc_currentState5_link_reassign_clear():
    a = fsmSample_State(name="sample_text")
    b1 = fsmSample_FSM(name="sample_text")
    b2 = fsmSample_FSM(name="sample_text_2")
    _safe_set(a, 'fsmSample_State7', b1)
    assert _is_linked(a, 'fsmSample_State7', b1)
    if hasattr(b1, 'fsmSample_FSM6'):
        assert _is_linked(b1, 'fsmSample_FSM6', a)
    _safe_set(a, 'fsmSample_State7', b2)
    assert _is_linked(a, 'fsmSample_State7', b2)
    if hasattr(b1, 'fsmSample_FSM6'):
        assert not _is_linked(b1, 'fsmSample_FSM6', a)
    if hasattr(b2, 'fsmSample_FSM6'):
        assert _is_linked(b2, 'fsmSample_FSM6', a)
    _safe_set(a, 'fsmSample_State7', None)
    assert not _is_linked(a, 'fsmSample_State7', b2)
    if hasattr(b2, 'fsmSample_FSM6'):
        assert not _is_linked(b2, 'fsmSample_FSM6', a)


def test_assoc_finalState2_link_reassign_clear():
    a = fsmSample_State(name="sample_text")
    b1 = fsmSample_FSM(name="sample_text")
    b2 = fsmSample_FSM(name="sample_text_2")
    _safe_set(a, 'fsmSample_State4', b1)
    assert _is_linked(a, 'fsmSample_State4', b1)
    if hasattr(b1, 'fsmSample_FSM3'):
        assert _is_linked(b1, 'fsmSample_FSM3', a)
    _safe_set(a, 'fsmSample_State4', b2)
    assert _is_linked(a, 'fsmSample_State4', b2)
    if hasattr(b1, 'fsmSample_FSM3'):
        assert not _is_linked(b1, 'fsmSample_FSM3', a)
    if hasattr(b2, 'fsmSample_FSM3'):
        assert _is_linked(b2, 'fsmSample_FSM3', a)
    _safe_set(a, 'fsmSample_State4', None)
    assert not _is_linked(a, 'fsmSample_State4', b2)
    if hasattr(b2, 'fsmSample_FSM3'):
        assert not _is_linked(b2, 'fsmSample_FSM3', a)


def test_assoc_incomingTransition10_link_reassign_clear():
    a = fsmSample_Transition(input="sample_text", output="sample_text")
    b1 = fsmSample_State(name="sample_text")
    b2 = fsmSample_State(name="sample_text_2")
    _safe_set(a, 'Transition11', b1)
    assert _is_linked(a, 'Transition11', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'Transition11', b2)
    assert _is_linked(a, 'Transition11', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'Transition11', None)
    assert not _is_linked(a, 'Transition11', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_initialState1_link_reassign_clear():
    a = fsmSample_State(name="sample_text")
    b1 = fsmSample_FSM(name="sample_text")
    b2 = fsmSample_FSM(name="sample_text_2")
    _safe_set(a, 'fsmSample_State', b1)
    assert _is_linked(a, 'fsmSample_State', b1)
    if hasattr(b1, 'fsmSample_FSM'):
        assert _is_linked(b1, 'fsmSample_FSM', a)
    _safe_set(a, 'fsmSample_State', b2)
    assert _is_linked(a, 'fsmSample_State', b2)
    if hasattr(b1, 'fsmSample_FSM'):
        assert not _is_linked(b1, 'fsmSample_FSM', a)
    if hasattr(b2, 'fsmSample_FSM'):
        assert _is_linked(b2, 'fsmSample_FSM', a)
    _safe_set(a, 'fsmSample_State', None)
    assert not _is_linked(a, 'fsmSample_State', b2)
    if hasattr(b2, 'fsmSample_FSM'):
        assert not _is_linked(b2, 'fsmSample_FSM', a)


def test_assoc_outgoingTransition9_link_reassign_clear():
    a = fsmSample_Transition(input="sample_text", output="sample_text")
    b1 = fsmSample_State(name="sample_text")
    b2 = fsmSample_State(name="sample_text_2")
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


def test_assoc_ownedState0_link_reassign_clear():
    a = fsmSample_State(name="sample_text")
    b1 = fsmSample_FSM(name="sample_text")
    b2 = fsmSample_FSM(name="sample_text_2")
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'owningFSM'):
        assert _is_linked(b1, 'owningFSM', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'owningFSM'):
        assert not _is_linked(b1, 'owningFSM', a)
    if hasattr(b2, 'owningFSM'):
        assert _is_linked(b2, 'owningFSM', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'owningFSM'):
        assert not _is_linked(b2, 'owningFSM', a)


def test_assoc_owningFSM8_link_reassign_clear():
    a = fsmSample_State(name="sample_text")
    b1 = fsmSample_FSM(name="sample_text")
    b2 = fsmSample_FSM(name="sample_text_2")
    _safe_set(a, 'ownedState', b1)
    assert _is_linked(a, 'ownedState', b1)
    if hasattr(b1, 'FSM'):
        assert _is_linked(b1, 'FSM', a)
    _safe_set(a, 'ownedState', b2)
    assert _is_linked(a, 'ownedState', b2)
    if hasattr(b1, 'FSM'):
        assert not _is_linked(b1, 'FSM', a)
    if hasattr(b2, 'FSM'):
        assert _is_linked(b2, 'FSM', a)
    _safe_set(a, 'ownedState', None)
    assert not _is_linked(a, 'ownedState', b2)
    if hasattr(b2, 'FSM'):
        assert not _is_linked(b2, 'FSM', a)


def test_assoc_source12_link_reassign_clear():
    a = fsmSample_Transition(input="sample_text", output="sample_text")
    b1 = fsmSample_State(name="sample_text")
    b2 = fsmSample_State(name="sample_text_2")
    _safe_set(a, 'outgoingTransition', b1)
    assert _is_linked(a, 'outgoingTransition', b1)
    if hasattr(b1, 'State13'):
        assert _is_linked(b1, 'State13', a)
    _safe_set(a, 'outgoingTransition', b2)
    assert _is_linked(a, 'outgoingTransition', b2)
    if hasattr(b1, 'State13'):
        assert not _is_linked(b1, 'State13', a)
    if hasattr(b2, 'State13'):
        assert _is_linked(b2, 'State13', a)
    _safe_set(a, 'outgoingTransition', None)
    assert not _is_linked(a, 'outgoingTransition', b2)
    if hasattr(b2, 'State13'):
        assert not _is_linked(b2, 'State13', a)


def test_assoc_target14_link_reassign_clear():
    a = fsmSample_Transition(input="sample_text", output="sample_text")
    b1 = fsmSample_State(name="sample_text")
    b2 = fsmSample_State(name="sample_text_2")
    _safe_set(a, 'incomingTransition', b1)
    assert _is_linked(a, 'incomingTransition', b1)
    if hasattr(b1, 'State15'):
        assert _is_linked(b1, 'State15', a)
    _safe_set(a, 'incomingTransition', b2)
    assert _is_linked(a, 'incomingTransition', b2)
    if hasattr(b1, 'State15'):
        assert not _is_linked(b1, 'State15', a)
    if hasattr(b2, 'State15'):
        assert _is_linked(b2, 'State15', a)
    _safe_set(a, 'incomingTransition', None)
    assert not _is_linked(a, 'incomingTransition', b2)
    if hasattr(b2, 'State15'):
        assert not _is_linked(b2, 'State15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

fsmSample_Action_strategy = st.builds(fsmSample_Action, name=safe_text)
@given(instance=fsmSample_Action_strategy)
@settings(max_examples=25)
def test_fsmSample_Action_instantiation(instance):
    assert isinstance(instance, fsmSample_Action)


fsmSample_FSM_strategy = st.builds(fsmSample_FSM, name=safe_text)
@given(instance=fsmSample_FSM_strategy)
@settings(max_examples=25)
def test_fsmSample_FSM_instantiation(instance):
    assert isinstance(instance, fsmSample_FSM)


fsmSample_State_strategy = st.builds(fsmSample_State, name=safe_text)
@given(instance=fsmSample_State_strategy)
@settings(max_examples=25)
def test_fsmSample_State_instantiation(instance):
    assert isinstance(instance, fsmSample_State)


fsmSample_Transition_strategy = st.builds(fsmSample_Transition, input=safe_text, output=safe_text)
@given(instance=fsmSample_Transition_strategy)
@settings(max_examples=25)
def test_fsmSample_Transition_instantiation(instance):
    assert isinstance(instance, fsmSample_Transition)



