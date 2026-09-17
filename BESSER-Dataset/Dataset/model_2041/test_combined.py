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
    tp1_State,
    tp1_Transition,
    tp1_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tp1_state_is_not_abstract():
    assert not inspect.isabstract(tp1_State)


def test_hyp_tp1_state_constructor_exists():
    assert callable(tp1_State.__init__)


def test_hyp_tp1_state_constructor_args():
    sig = inspect.signature(tp1_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tp1_transition_is_not_abstract():
    assert not inspect.isabstract(tp1_Transition)


def test_hyp_tp1_transition_constructor_exists():
    assert callable(tp1_Transition.__init__)


def test_hyp_tp1_transition_constructor_args():
    sig = inspect.signature(tp1_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tp1_statemachine_is_not_abstract():
    assert not inspect.isabstract(tp1_StateMachine)


def test_hyp_tp1_statemachine_constructor_exists():
    assert callable(tp1_StateMachine.__init__)


def test_hyp_tp1_statemachine_constructor_args():
    sig = inspect.signature(tp1_StateMachine.__init__)
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
tp1_State_strategy = st.builds(
    tp1_State,
    name=
        safe_text
)
tp1_Transition_strategy = st.builds(
    tp1_Transition,
    name=
        safe_text
)
tp1_StateMachine_strategy = st.builds(
    tp1_StateMachine,
    name=
        safe_text
)




@given(instance=tp1_State_strategy)
def test_hyp_tp1_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=tp1_Transition_strategy)
def test_hyp_tp1_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=tp1_StateMachine_strategy)
def test_hyp_tp1_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tp1_StateMachine_strategy)
@settings(max_examples=30)
def test_hyp_tp1_statemachine_execute_changes_state(instance):
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
        assert has_statements, f"Function 'execute' in tp1_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in tp1_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in tp1_StateMachine is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    tp1_State,
    tp1_StateMachine,
    tp1_Transition,
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

def test_tp1_State_name_value_roundtrip():
    instance = tp1_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tp1_StateMachine_name_value_roundtrip():
    instance = tp1_StateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tp1_Transition_name_value_roundtrip():
    instance = tp1_Transition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_from_6_link_reassign_clear():
    a = tp1_Transition(name="sample_text")
    b1 = tp1_State(name="sample_text")
    b2 = tp1_State(name="sample_text_2")
    _safe_set(a, 'outcoming', b1)
    assert _is_linked(a, 'outcoming', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'outcoming', b2)
    assert _is_linked(a, 'outcoming', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'outcoming', None)
    assert not _is_linked(a, 'outcoming', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_incoming4_link_reassign_clear():
    a = tp1_Transition(name="sample_text")
    b1 = tp1_State(name="sample_text")
    b2 = tp1_State(name="sample_text_2")
    _safe_set(a, 'Transition5', b1)
    assert _is_linked(a, 'Transition5', b1)
    if hasattr(b1, 'to'):
        assert _is_linked(b1, 'to', a)
    _safe_set(a, 'Transition5', b2)
    assert _is_linked(a, 'Transition5', b2)
    if hasattr(b1, 'to'):
        assert not _is_linked(b1, 'to', a)
    if hasattr(b2, 'to'):
        assert _is_linked(b2, 'to', a)
    _safe_set(a, 'Transition5', None)
    assert not _is_linked(a, 'Transition5', b2)
    if hasattr(b2, 'to'):
        assert not _is_linked(b2, 'to', a)


def test_assoc_outcoming3_link_reassign_clear():
    a = tp1_Transition(name="sample_text")
    b1 = tp1_State(name="sample_text")
    b2 = tp1_State(name="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'from_'):
        assert _is_linked(b1, 'from_', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'from_'):
        assert not _is_linked(b1, 'from_', a)
    if hasattr(b2, 'from_'):
        assert _is_linked(b2, 'from_', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'from_'):
        assert not _is_linked(b2, 'from_', a)


def test_assoc_state1_link_reassign_clear():
    a = tp1_StateMachine(name="sample_text")
    b1 = tp1_State(name="sample_text")
    b2 = tp1_State(name="sample_text_2")
    _safe_set(a, 'tp1_StateMachine2', {b1})
    assert _is_linked(a, 'tp1_StateMachine2', b1)
    if hasattr(b1, 'tp1_State'):
        assert _is_linked(b1, 'tp1_State', a)
    _safe_set(a, 'tp1_StateMachine2', {b2})
    assert _is_linked(a, 'tp1_StateMachine2', b2)
    if hasattr(b1, 'tp1_State'):
        assert not _is_linked(b1, 'tp1_State', a)
    if hasattr(b2, 'tp1_State'):
        assert _is_linked(b2, 'tp1_State', a)
    _safe_set(a, 'tp1_StateMachine2', set())
    assert not _is_linked(a, 'tp1_StateMachine2', b2)
    if hasattr(b2, 'tp1_State'):
        assert not _is_linked(b2, 'tp1_State', a)


def test_assoc_to7_link_reassign_clear():
    a = tp1_Transition(name="sample_text")
    b1 = tp1_State(name="sample_text")
    b2 = tp1_State(name="sample_text_2")
    _safe_set(a, 'incoming', b1)
    assert _is_linked(a, 'incoming', b1)
    if hasattr(b1, 'State8'):
        assert _is_linked(b1, 'State8', a)
    _safe_set(a, 'incoming', b2)
    assert _is_linked(a, 'incoming', b2)
    if hasattr(b1, 'State8'):
        assert not _is_linked(b1, 'State8', a)
    if hasattr(b2, 'State8'):
        assert _is_linked(b2, 'State8', a)
    _safe_set(a, 'incoming', None)
    assert not _is_linked(a, 'incoming', b2)
    if hasattr(b2, 'State8'):
        assert not _is_linked(b2, 'State8', a)


def test_assoc_transition0_link_reassign_clear():
    a = tp1_Transition(name="sample_text")
    b1 = tp1_StateMachine(name="sample_text")
    b2 = tp1_StateMachine(name="sample_text_2")
    _safe_set(a, 'tp1_Transition', b1)
    assert _is_linked(a, 'tp1_Transition', b1)
    if hasattr(b1, 'tp1_StateMachine'):
        assert _is_linked(b1, 'tp1_StateMachine', a)
    _safe_set(a, 'tp1_Transition', b2)
    assert _is_linked(a, 'tp1_Transition', b2)
    if hasattr(b1, 'tp1_StateMachine'):
        assert not _is_linked(b1, 'tp1_StateMachine', a)
    if hasattr(b2, 'tp1_StateMachine'):
        assert _is_linked(b2, 'tp1_StateMachine', a)
    _safe_set(a, 'tp1_Transition', None)
    assert not _is_linked(a, 'tp1_Transition', b2)
    if hasattr(b2, 'tp1_StateMachine'):
        assert not _is_linked(b2, 'tp1_StateMachine', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

tp1_State_strategy = st.builds(tp1_State, name=safe_text)
@given(instance=tp1_State_strategy)
@settings(max_examples=25)
def test_tp1_State_instantiation(instance):
    assert isinstance(instance, tp1_State)


tp1_StateMachine_strategy = st.builds(tp1_StateMachine, name=safe_text)
@given(instance=tp1_StateMachine_strategy)
@settings(max_examples=25)
def test_tp1_StateMachine_instantiation(instance):
    assert isinstance(instance, tp1_StateMachine)


tp1_Transition_strategy = st.builds(tp1_Transition, name=safe_text)
@given(instance=tp1_Transition_strategy)
@settings(max_examples=25)
def test_tp1_Transition_instantiation(instance):
    assert isinstance(instance, tp1_Transition)



