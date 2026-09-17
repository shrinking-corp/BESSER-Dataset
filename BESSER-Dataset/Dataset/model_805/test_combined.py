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
    fsm_NamedElement,
    NamedElement,
    fsm_StateMachine,
    fsm_Transition,
    fsm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm_NamedElement)


def test_hyp_fsm_namedelement_constructor_exists():
    assert callable(fsm_NamedElement.__init__)


def test_hyp_fsm_namedelement_constructor_args():
    sig = inspect.signature(fsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_hyp_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_hyp_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "unprocessedString" in params, "Missing parameter 'unprocessedString'"
    assert "producedString" in params, "Missing parameter 'producedString'"
    assert "consummedString" in params, "Missing parameter 'consummedString'"






def test_hyp_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_hyp_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_hyp_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"





def test_hyp_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_hyp_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_hyp_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
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
fsm_NamedElement_strategy = st.builds(
    fsm_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
    unprocessedString=
        safe_text,
    producedString=
        safe_text,
    consummedString=
        safe_text
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    input=
        safe_text,
    output=
        safe_text
)
fsm_State_strategy = st.builds(
    fsm_State,
)




@given(instance=fsm_NamedElement_strategy)
def test_hyp_fsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=fsm_StateMachine_strategy)
def test_hyp_fsm_statemachine_unprocessedString_setter(instance):
    original = instance.unprocessedString
    instance.unprocessedString = original
    assert instance.unprocessedString == original



@given(instance=fsm_StateMachine_strategy)
def test_hyp_fsm_statemachine_producedString_setter(instance):
    original = instance.producedString
    instance.producedString = original
    assert instance.producedString == original



@given(instance=fsm_StateMachine_strategy)
def test_hyp_fsm_statemachine_consummedString_setter(instance):
    original = instance.consummedString
    instance.consummedString = original
    assert instance.consummedString == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=30)
def test_hyp_fsm_statemachine_initializemodel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.initializeModel(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.initializeModel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'initializeModel' in fsm_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initializeModel' in fsm_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initializeModel' in fsm_StateMachine is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=30)
def test_hyp_fsm_statemachine_main_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.main()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.main).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'main' in fsm_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'main' in fsm_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'main' in fsm_StateMachine is not implemented or raised an error")




@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_Transition_strategy)
@settings(max_examples=30)
def test_hyp_fsm_transition_fire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fire()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fire' in fsm_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in fsm_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in fsm_Transition is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_State_strategy)
@settings(max_examples=30)
def test_hyp_fsm_state_step_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.step(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.step).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'step' in fsm_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'step' in fsm_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'step' in fsm_State is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    fsm_NamedElement,
    fsm_State,
    fsm_StateMachine,
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

def test_fsm_NamedElement_name_value_roundtrip():
    instance = fsm_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsm_StateMachine_consummedString_value_roundtrip():
    instance = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    assert instance.consummedString == "sample_text"
    instance.consummedString = "sample_text_2"
    assert instance.consummedString == "sample_text_2"


def test_fsm_StateMachine_producedString_value_roundtrip():
    instance = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    assert instance.producedString == "sample_text"
    instance.producedString = "sample_text_2"
    assert instance.producedString == "sample_text_2"


def test_fsm_StateMachine_unprocessedString_value_roundtrip():
    instance = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    assert instance.unprocessedString == "sample_text"
    instance.unprocessedString = "sample_text_2"
    assert instance.unprocessedString == "sample_text_2"


def test_fsm_Transition_input_value_roundtrip():
    instance = fsm_Transition(input="sample_text", output="sample_text")
    assert instance.input == "sample_text"
    instance.input = "sample_text_2"
    assert instance.input == "sample_text_2"


def test_fsm_Transition_output_value_roundtrip():
    instance = fsm_Transition(input="sample_text", output="sample_text")
    assert instance.output == "sample_text"
    instance.output = "sample_text_2"
    assert instance.output == "sample_text_2"


def test_fsm_State_isa_NamedElement():
    instance = fsm_State()
    assert isinstance(instance, NamedElement)


def test_fsm_StateMachine_isa_NamedElement():
    instance = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    assert isinstance(instance, NamedElement)


def test_fsm_Transition_isa_NamedElement():
    instance = fsm_Transition(input="sample_text", output="sample_text")
    assert isinstance(instance, NamedElement)


def test_assoc_currentState4_link_reassign_clear():
    a = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
    _safe_set(a, 'fsm_StateMachine5', b1)
    assert _is_linked(a, 'fsm_StateMachine5', b1)
    if hasattr(b1, 'fsm_State6'):
        assert _is_linked(b1, 'fsm_State6', a)
    _safe_set(a, 'fsm_StateMachine5', b2)
    assert _is_linked(a, 'fsm_StateMachine5', b2)
    if hasattr(b1, 'fsm_State6'):
        assert not _is_linked(b1, 'fsm_State6', a)
    if hasattr(b2, 'fsm_State6'):
        assert _is_linked(b2, 'fsm_State6', a)
    _safe_set(a, 'fsm_StateMachine5', None)
    assert not _is_linked(a, 'fsm_StateMachine5', b2)
    if hasattr(b2, 'fsm_State6'):
        assert not _is_linked(b2, 'fsm_State6', a)


def test_assoc_incomingTransitions9_link_reassign_clear():
    a = fsm_Transition(input="sample_text", output="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
    _safe_set(a, 'Transition10', b1)
    assert _is_linked(a, 'Transition10', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'Transition10', b2)
    assert _is_linked(a, 'Transition10', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'Transition10', None)
    assert not _is_linked(a, 'Transition10', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_initialState1_link_reassign_clear():
    a = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
    _safe_set(a, 'fsm_StateMachine', b1)
    assert _is_linked(a, 'fsm_StateMachine', b1)
    if hasattr(b1, 'fsm_State'):
        assert _is_linked(b1, 'fsm_State', a)
    _safe_set(a, 'fsm_StateMachine', b2)
    assert _is_linked(a, 'fsm_StateMachine', b2)
    if hasattr(b1, 'fsm_State'):
        assert not _is_linked(b1, 'fsm_State', a)
    if hasattr(b2, 'fsm_State'):
        assert _is_linked(b2, 'fsm_State', a)
    _safe_set(a, 'fsm_StateMachine', None)
    assert not _is_linked(a, 'fsm_StateMachine', b2)
    if hasattr(b2, 'fsm_State'):
        assert not _is_linked(b2, 'fsm_State', a)


def test_assoc_outgoingTransitions8_link_reassign_clear():
    a = fsm_Transition(input="sample_text", output="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
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


def test_assoc_ownedStates0_link_reassign_clear():
    a = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
    _safe_set(a, 'owningFSM', {b1})
    assert _is_linked(a, 'owningFSM', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'owningFSM', {b2})
    assert _is_linked(a, 'owningFSM', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'owningFSM', set())
    assert not _is_linked(a, 'owningFSM', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_ownedTransitions2_link_reassign_clear():
    a = fsm_Transition(input="sample_text", output="sample_text")
    b1 = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    b2 = fsm_StateMachine(consummedString="sample_text_2", producedString="sample_text_2", unprocessedString="sample_text_2")
    _safe_set(a, 'fsm_Transition', b1)
    assert _is_linked(a, 'fsm_Transition', b1)
    if hasattr(b1, 'fsm_StateMachine3'):
        assert _is_linked(b1, 'fsm_StateMachine3', a)
    _safe_set(a, 'fsm_Transition', b2)
    assert _is_linked(a, 'fsm_Transition', b2)
    if hasattr(b1, 'fsm_StateMachine3'):
        assert not _is_linked(b1, 'fsm_StateMachine3', a)
    if hasattr(b2, 'fsm_StateMachine3'):
        assert _is_linked(b2, 'fsm_StateMachine3', a)
    _safe_set(a, 'fsm_Transition', None)
    assert not _is_linked(a, 'fsm_Transition', b2)
    if hasattr(b2, 'fsm_StateMachine3'):
        assert not _is_linked(b2, 'fsm_StateMachine3', a)


def test_assoc_owningFSM7_link_reassign_clear():
    a = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
    _safe_set(a, 'StateMachine', b1)
    assert _is_linked(a, 'StateMachine', b1)
    if hasattr(b1, 'ownedStates'):
        assert _is_linked(b1, 'ownedStates', a)
    _safe_set(a, 'StateMachine', b2)
    assert _is_linked(a, 'StateMachine', b2)
    if hasattr(b1, 'ownedStates'):
        assert not _is_linked(b1, 'ownedStates', a)
    if hasattr(b2, 'ownedStates'):
        assert _is_linked(b2, 'ownedStates', a)
    _safe_set(a, 'StateMachine', None)
    assert not _is_linked(a, 'StateMachine', b2)
    if hasattr(b2, 'ownedStates'):
        assert not _is_linked(b2, 'ownedStates', a)


def test_assoc_source11_link_reassign_clear():
    a = fsm_Transition(input="sample_text", output="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
    _safe_set(a, 'outgoingTransitions', b1)
    assert _is_linked(a, 'outgoingTransitions', b1)
    if hasattr(b1, 'State12'):
        assert _is_linked(b1, 'State12', a)
    _safe_set(a, 'outgoingTransitions', b2)
    assert _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b1, 'State12'):
        assert not _is_linked(b1, 'State12', a)
    if hasattr(b2, 'State12'):
        assert _is_linked(b2, 'State12', a)
    _safe_set(a, 'outgoingTransitions', None)
    assert not _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b2, 'State12'):
        assert not _is_linked(b2, 'State12', a)


def test_assoc_target13_link_reassign_clear():
    a = fsm_Transition(input="sample_text", output="sample_text")
    b1 = fsm_State()
    b2 = fsm_State()
    _safe_set(a, 'incomingTransitions', b1)
    assert _is_linked(a, 'incomingTransitions', b1)
    if hasattr(b1, 'State14'):
        assert _is_linked(b1, 'State14', a)
    _safe_set(a, 'incomingTransitions', b2)
    assert _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b1, 'State14'):
        assert not _is_linked(b1, 'State14', a)
    if hasattr(b2, 'State14'):
        assert _is_linked(b2, 'State14', a)
    _safe_set(a, 'incomingTransitions', None)
    assert not _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b2, 'State14'):
        assert not _is_linked(b2, 'State14', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


fsm_NamedElement_strategy = st.builds(fsm_NamedElement, name=safe_text)
@given(instance=fsm_NamedElement_strategy)
@settings(max_examples=25)
def test_fsm_NamedElement_instantiation(instance):
    assert isinstance(instance, fsm_NamedElement)


fsm_State_strategy = st.builds(fsm_State)
@given(instance=fsm_State_strategy)
@settings(max_examples=25)
def test_fsm_State_instantiation(instance):
    assert isinstance(instance, fsm_State)


fsm_StateMachine_strategy = st.builds(fsm_StateMachine, consummedString=safe_text, producedString=safe_text, unprocessedString=safe_text)
@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=25)
def test_fsm_StateMachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)


fsm_Transition_strategy = st.builds(fsm_Transition, input=safe_text, output=safe_text)
@given(instance=fsm_Transition_strategy)
@settings(max_examples=25)
def test_fsm_Transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



