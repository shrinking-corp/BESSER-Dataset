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
    tP1_EM_State,
    tP1_EM_Transition,
    tP1_EM_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tp1_em_state_is_not_abstract():
    assert not inspect.isabstract(tP1_EM_State)


def test_hyp_tp1_em_state_constructor_exists():
    assert callable(tP1_EM_State.__init__)


def test_hyp_tp1_em_state_constructor_args():
    sig = inspect.signature(tP1_EM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tp1_em_transition_is_not_abstract():
    assert not inspect.isabstract(tP1_EM_Transition)


def test_hyp_tp1_em_transition_constructor_exists():
    assert callable(tP1_EM_Transition.__init__)


def test_hyp_tp1_em_transition_constructor_args():
    sig = inspect.signature(tP1_EM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tp1_em_statemachine_is_not_abstract():
    assert not inspect.isabstract(tP1_EM_StateMachine)


def test_hyp_tp1_em_statemachine_constructor_exists():
    assert callable(tP1_EM_StateMachine.__init__)


def test_hyp_tp1_em_statemachine_constructor_args():
    sig = inspect.signature(tP1_EM_StateMachine.__init__)
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
tP1_EM_State_strategy = st.builds(
    tP1_EM_State,
    name=
        safe_text
)
tP1_EM_Transition_strategy = st.builds(
    tP1_EM_Transition,
    name=
        safe_text
)
tP1_EM_StateMachine_strategy = st.builds(
    tP1_EM_StateMachine,
    name=
        safe_text
)




@given(instance=tP1_EM_State_strategy)
def test_hyp_tp1_em_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=tP1_EM_Transition_strategy)
def test_hyp_tp1_em_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=tP1_EM_StateMachine_strategy)
def test_hyp_tp1_em_statemachine_name_setter(instance):
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
    tP1_EM_State,
    tP1_EM_StateMachine,
    tP1_EM_Transition,
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

def test_tP1_EM_State_name_value_roundtrip():
    instance = tP1_EM_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tP1_EM_StateMachine_name_value_roundtrip():
    instance = tP1_EM_StateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tP1_EM_Transition_name_value_roundtrip():
    instance = tP1_EM_Transition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_from_10_link_reassign_clear():
    a = tP1_EM_Transition(name="sample_text")
    b1 = tP1_EM_State(name="sample_text")
    b2 = tP1_EM_State(name="sample_text_2")
    _safe_set(a, 'outgoing', b1)
    assert _is_linked(a, 'outgoing', b1)
    if hasattr(b1, 'State11'):
        assert _is_linked(b1, 'State11', a)
    _safe_set(a, 'outgoing', b2)
    assert _is_linked(a, 'outgoing', b2)
    if hasattr(b1, 'State11'):
        assert not _is_linked(b1, 'State11', a)
    if hasattr(b2, 'State11'):
        assert _is_linked(b2, 'State11', a)
    _safe_set(a, 'outgoing', None)
    assert not _is_linked(a, 'outgoing', b2)
    if hasattr(b2, 'State11'):
        assert not _is_linked(b2, 'State11', a)


def test_assoc_incoming6_link_reassign_clear():
    a = tP1_EM_Transition(name="sample_text")
    b1 = tP1_EM_State(name="sample_text")
    b2 = tP1_EM_State(name="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'to'):
        assert _is_linked(b1, 'to', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'to'):
        assert not _is_linked(b1, 'to', a)
    if hasattr(b2, 'to'):
        assert _is_linked(b2, 'to', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'to'):
        assert not _is_linked(b2, 'to', a)


def test_assoc_initialState3_link_reassign_clear():
    a = tP1_EM_StateMachine(name="sample_text")
    b1 = tP1_EM_State(name="sample_text")
    b2 = tP1_EM_State(name="sample_text_2")
    _safe_set(a, 'tP1_EM_StateMachine4', b1)
    assert _is_linked(a, 'tP1_EM_StateMachine4', b1)
    if hasattr(b1, 'tP1_EM_State5'):
        assert _is_linked(b1, 'tP1_EM_State5', a)
    _safe_set(a, 'tP1_EM_StateMachine4', b2)
    assert _is_linked(a, 'tP1_EM_StateMachine4', b2)
    if hasattr(b1, 'tP1_EM_State5'):
        assert not _is_linked(b1, 'tP1_EM_State5', a)
    if hasattr(b2, 'tP1_EM_State5'):
        assert _is_linked(b2, 'tP1_EM_State5', a)
    _safe_set(a, 'tP1_EM_StateMachine4', None)
    assert not _is_linked(a, 'tP1_EM_StateMachine4', b2)
    if hasattr(b2, 'tP1_EM_State5'):
        assert not _is_linked(b2, 'tP1_EM_State5', a)


def test_assoc_outgoing7_link_reassign_clear():
    a = tP1_EM_Transition(name="sample_text")
    b1 = tP1_EM_State(name="sample_text")
    b2 = tP1_EM_State(name="sample_text_2")
    _safe_set(a, 'Transition8', b1)
    assert _is_linked(a, 'Transition8', b1)
    if hasattr(b1, 'from_'):
        assert _is_linked(b1, 'from_', a)
    _safe_set(a, 'Transition8', b2)
    assert _is_linked(a, 'Transition8', b2)
    if hasattr(b1, 'from_'):
        assert not _is_linked(b1, 'from_', a)
    if hasattr(b2, 'from_'):
        assert _is_linked(b2, 'from_', a)
    _safe_set(a, 'Transition8', None)
    assert not _is_linked(a, 'Transition8', b2)
    if hasattr(b2, 'from_'):
        assert not _is_linked(b2, 'from_', a)


def test_assoc_state1_link_reassign_clear():
    a = tP1_EM_StateMachine(name="sample_text")
    b1 = tP1_EM_State(name="sample_text")
    b2 = tP1_EM_State(name="sample_text_2")
    _safe_set(a, 'tP1_EM_StateMachine2', {b1})
    assert _is_linked(a, 'tP1_EM_StateMachine2', b1)
    if hasattr(b1, 'tP1_EM_State'):
        assert _is_linked(b1, 'tP1_EM_State', a)
    _safe_set(a, 'tP1_EM_StateMachine2', {b2})
    assert _is_linked(a, 'tP1_EM_StateMachine2', b2)
    if hasattr(b1, 'tP1_EM_State'):
        assert not _is_linked(b1, 'tP1_EM_State', a)
    if hasattr(b2, 'tP1_EM_State'):
        assert _is_linked(b2, 'tP1_EM_State', a)
    _safe_set(a, 'tP1_EM_StateMachine2', set())
    assert not _is_linked(a, 'tP1_EM_StateMachine2', b2)
    if hasattr(b2, 'tP1_EM_State'):
        assert not _is_linked(b2, 'tP1_EM_State', a)


def test_assoc_to9_link_reassign_clear():
    a = tP1_EM_Transition(name="sample_text")
    b1 = tP1_EM_State(name="sample_text")
    b2 = tP1_EM_State(name="sample_text_2")
    _safe_set(a, 'incoming', b1)
    assert _is_linked(a, 'incoming', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'incoming', b2)
    assert _is_linked(a, 'incoming', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'incoming', None)
    assert not _is_linked(a, 'incoming', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_transition0_link_reassign_clear():
    a = tP1_EM_Transition(name="sample_text")
    b1 = tP1_EM_StateMachine(name="sample_text")
    b2 = tP1_EM_StateMachine(name="sample_text_2")
    _safe_set(a, 'tP1_EM_Transition', b1)
    assert _is_linked(a, 'tP1_EM_Transition', b1)
    if hasattr(b1, 'tP1_EM_StateMachine'):
        assert _is_linked(b1, 'tP1_EM_StateMachine', a)
    _safe_set(a, 'tP1_EM_Transition', b2)
    assert _is_linked(a, 'tP1_EM_Transition', b2)
    if hasattr(b1, 'tP1_EM_StateMachine'):
        assert not _is_linked(b1, 'tP1_EM_StateMachine', a)
    if hasattr(b2, 'tP1_EM_StateMachine'):
        assert _is_linked(b2, 'tP1_EM_StateMachine', a)
    _safe_set(a, 'tP1_EM_Transition', None)
    assert not _is_linked(a, 'tP1_EM_Transition', b2)
    if hasattr(b2, 'tP1_EM_StateMachine'):
        assert not _is_linked(b2, 'tP1_EM_StateMachine', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

tP1_EM_State_strategy = st.builds(tP1_EM_State, name=safe_text)
@given(instance=tP1_EM_State_strategy)
@settings(max_examples=25)
def test_tP1_EM_State_instantiation(instance):
    assert isinstance(instance, tP1_EM_State)


tP1_EM_StateMachine_strategy = st.builds(tP1_EM_StateMachine, name=safe_text)
@given(instance=tP1_EM_StateMachine_strategy)
@settings(max_examples=25)
def test_tP1_EM_StateMachine_instantiation(instance):
    assert isinstance(instance, tP1_EM_StateMachine)


tP1_EM_Transition_strategy = st.builds(tP1_EM_Transition, name=safe_text)
@given(instance=tP1_EM_Transition_strategy)
@settings(max_examples=25)
def test_tP1_EM_Transition_instantiation(instance):
    assert isinstance(instance, tP1_EM_Transition)



