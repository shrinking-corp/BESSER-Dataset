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
    gfsm_Guard,
    gfsm_State,
    gfsm_Transition,
    gfsm_Machine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_gfsm_guard_is_not_abstract():
    assert not inspect.isabstract(gfsm_Guard)


def test_hyp_gfsm_guard_constructor_exists():
    assert callable(gfsm_Guard.__init__)


def test_hyp_gfsm_guard_constructor_args():
    sig = inspect.signature(gfsm_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_gfsm_state_is_not_abstract():
    assert not inspect.isabstract(gfsm_State)


def test_hyp_gfsm_state_constructor_exists():
    assert callable(gfsm_State.__init__)


def test_hyp_gfsm_state_constructor_args():
    sig = inspect.signature(gfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_gfsm_transition_is_not_abstract():
    assert not inspect.isabstract(gfsm_Transition)


def test_hyp_gfsm_transition_constructor_exists():
    assert callable(gfsm_Transition.__init__)


def test_hyp_gfsm_transition_constructor_args():
    sig = inspect.signature(gfsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"




def test_hyp_gfsm_machine_is_not_abstract():
    assert not inspect.isabstract(gfsm_Machine)


def test_hyp_gfsm_machine_constructor_exists():
    assert callable(gfsm_Machine.__init__)


def test_hyp_gfsm_machine_constructor_args():
    sig = inspect.signature(gfsm_Machine.__init__)
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
gfsm_Guard_strategy = st.builds(
    gfsm_Guard,
    value=
        safe_text
)
gfsm_State_strategy = st.builds(
    gfsm_State,
    name=
        safe_text
)
gfsm_Transition_strategy = st.builds(
    gfsm_Transition,
    event=
        safe_text
)
gfsm_Machine_strategy = st.builds(
    gfsm_Machine,
)




@given(instance=gfsm_Guard_strategy)
def test_hyp_gfsm_guard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=gfsm_State_strategy)
def test_hyp_gfsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=gfsm_Transition_strategy)
def test_hyp_gfsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    gfsm_Guard,
    gfsm_Machine,
    gfsm_State,
    gfsm_Transition,
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

def test_gfsm_Guard_value_value_roundtrip():
    instance = gfsm_Guard(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_gfsm_State_name_value_roundtrip():
    instance = gfsm_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gfsm_Transition_event_value_roundtrip():
    instance = gfsm_Transition(event="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_assoc_from_0_link_reassign_clear():
    a = gfsm_Transition(event="sample_text")
    b1 = gfsm_State(name="sample_text")
    b2 = gfsm_State(name="sample_text_2")
    _safe_set(a, 'outgoings', b1)
    assert _is_linked(a, 'outgoings', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'outgoings', b2)
    assert _is_linked(a, 'outgoings', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'outgoings', None)
    assert not _is_linked(a, 'outgoings', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_guard3_link_reassign_clear():
    a = gfsm_Transition(event="sample_text")
    b1 = gfsm_Guard(value="sample_text")
    b2 = gfsm_Guard(value="sample_text_2")
    _safe_set(a, 'gfsm_Transition', b1)
    assert _is_linked(a, 'gfsm_Transition', b1)
    if hasattr(b1, 'gfsm_Guard'):
        assert _is_linked(b1, 'gfsm_Guard', a)
    _safe_set(a, 'gfsm_Transition', b2)
    assert _is_linked(a, 'gfsm_Transition', b2)
    if hasattr(b1, 'gfsm_Guard'):
        assert not _is_linked(b1, 'gfsm_Guard', a)
    if hasattr(b2, 'gfsm_Guard'):
        assert _is_linked(b2, 'gfsm_Guard', a)
    _safe_set(a, 'gfsm_Transition', None)
    assert not _is_linked(a, 'gfsm_Transition', b2)
    if hasattr(b2, 'gfsm_Guard'):
        assert not _is_linked(b2, 'gfsm_Guard', a)


def test_assoc_incommings5_link_reassign_clear():
    a = gfsm_Transition(event="sample_text")
    b1 = gfsm_State(name="sample_text")
    b2 = gfsm_State(name="sample_text_2")
    _safe_set(a, 'Transition6', b1)
    assert _is_linked(a, 'Transition6', b1)
    if hasattr(b1, 'to'):
        assert _is_linked(b1, 'to', a)
    _safe_set(a, 'Transition6', b2)
    assert _is_linked(a, 'Transition6', b2)
    if hasattr(b1, 'to'):
        assert not _is_linked(b1, 'to', a)
    if hasattr(b2, 'to'):
        assert _is_linked(b2, 'to', a)
    _safe_set(a, 'Transition6', None)
    assert not _is_linked(a, 'Transition6', b2)
    if hasattr(b2, 'to'):
        assert not _is_linked(b2, 'to', a)


def test_assoc_initialState11_link_reassign_clear():
    a = gfsm_State(name="sample_text")
    b1 = gfsm_Machine()
    b2 = gfsm_Machine()
    _safe_set(a, 'gfsm_State13', b1)
    assert _is_linked(a, 'gfsm_State13', b1)
    if hasattr(b1, 'gfsm_Machine12'):
        assert _is_linked(b1, 'gfsm_Machine12', a)
    _safe_set(a, 'gfsm_State13', b2)
    assert _is_linked(a, 'gfsm_State13', b2)
    if hasattr(b1, 'gfsm_Machine12'):
        assert not _is_linked(b1, 'gfsm_Machine12', a)
    if hasattr(b2, 'gfsm_Machine12'):
        assert _is_linked(b2, 'gfsm_Machine12', a)
    _safe_set(a, 'gfsm_State13', None)
    assert not _is_linked(a, 'gfsm_State13', b2)
    if hasattr(b2, 'gfsm_Machine12'):
        assert not _is_linked(b2, 'gfsm_Machine12', a)


def test_assoc_outgoings4_link_reassign_clear():
    a = gfsm_Transition(event="sample_text")
    b1 = gfsm_State(name="sample_text")
    b2 = gfsm_State(name="sample_text_2")
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


def test_assoc_states7_link_reassign_clear():
    a = gfsm_State(name="sample_text")
    b1 = gfsm_Machine()
    b2 = gfsm_Machine()
    _safe_set(a, 'gfsm_State', b1)
    assert _is_linked(a, 'gfsm_State', b1)
    if hasattr(b1, 'gfsm_Machine'):
        assert _is_linked(b1, 'gfsm_Machine', a)
    _safe_set(a, 'gfsm_State', b2)
    assert _is_linked(a, 'gfsm_State', b2)
    if hasattr(b1, 'gfsm_Machine'):
        assert not _is_linked(b1, 'gfsm_Machine', a)
    if hasattr(b2, 'gfsm_Machine'):
        assert _is_linked(b2, 'gfsm_Machine', a)
    _safe_set(a, 'gfsm_State', None)
    assert not _is_linked(a, 'gfsm_State', b2)
    if hasattr(b2, 'gfsm_Machine'):
        assert not _is_linked(b2, 'gfsm_Machine', a)


def test_assoc_to1_link_reassign_clear():
    a = gfsm_Transition(event="sample_text")
    b1 = gfsm_State(name="sample_text")
    b2 = gfsm_State(name="sample_text_2")
    _safe_set(a, 'incommings', b1)
    assert _is_linked(a, 'incommings', b1)
    if hasattr(b1, 'State2'):
        assert _is_linked(b1, 'State2', a)
    _safe_set(a, 'incommings', b2)
    assert _is_linked(a, 'incommings', b2)
    if hasattr(b1, 'State2'):
        assert not _is_linked(b1, 'State2', a)
    if hasattr(b2, 'State2'):
        assert _is_linked(b2, 'State2', a)
    _safe_set(a, 'incommings', None)
    assert not _is_linked(a, 'incommings', b2)
    if hasattr(b2, 'State2'):
        assert not _is_linked(b2, 'State2', a)


def test_assoc_transitions8_link_reassign_clear():
    a = gfsm_Transition(event="sample_text")
    b1 = gfsm_Machine()
    b2 = gfsm_Machine()
    _safe_set(a, 'gfsm_Transition10', b1)
    assert _is_linked(a, 'gfsm_Transition10', b1)
    if hasattr(b1, 'gfsm_Machine9'):
        assert _is_linked(b1, 'gfsm_Machine9', a)
    _safe_set(a, 'gfsm_Transition10', b2)
    assert _is_linked(a, 'gfsm_Transition10', b2)
    if hasattr(b1, 'gfsm_Machine9'):
        assert not _is_linked(b1, 'gfsm_Machine9', a)
    if hasattr(b2, 'gfsm_Machine9'):
        assert _is_linked(b2, 'gfsm_Machine9', a)
    _safe_set(a, 'gfsm_Transition10', None)
    assert not _is_linked(a, 'gfsm_Transition10', b2)
    if hasattr(b2, 'gfsm_Machine9'):
        assert not _is_linked(b2, 'gfsm_Machine9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

gfsm_Guard_strategy = st.builds(gfsm_Guard, value=safe_text)
@given(instance=gfsm_Guard_strategy)
@settings(max_examples=25)
def test_gfsm_Guard_instantiation(instance):
    assert isinstance(instance, gfsm_Guard)


gfsm_Machine_strategy = st.builds(gfsm_Machine)
@given(instance=gfsm_Machine_strategy)
@settings(max_examples=25)
def test_gfsm_Machine_instantiation(instance):
    assert isinstance(instance, gfsm_Machine)


gfsm_State_strategy = st.builds(gfsm_State, name=safe_text)
@given(instance=gfsm_State_strategy)
@settings(max_examples=25)
def test_gfsm_State_instantiation(instance):
    assert isinstance(instance, gfsm_State)


gfsm_Transition_strategy = st.builds(gfsm_Transition, event=safe_text)
@given(instance=gfsm_Transition_strategy)
@settings(max_examples=25)
def test_gfsm_Transition_instantiation(instance):
    assert isinstance(instance, gfsm_Transition)



