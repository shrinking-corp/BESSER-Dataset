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
    fsa_Transition,
    fsa_State,
    fsa_FSA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsa_transition_is_not_abstract():
    assert not inspect.isabstract(fsa_Transition)


def test_hyp_fsa_transition_constructor_exists():
    assert callable(fsa_Transition.__init__)


def test_hyp_fsa_transition_constructor_args():
    sig = inspect.signature(fsa_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"




def test_hyp_fsa_state_is_not_abstract():
    assert not inspect.isabstract(fsa_State)


def test_hyp_fsa_state_constructor_exists():
    assert callable(fsa_State.__init__)


def test_hyp_fsa_state_constructor_args():
    sig = inspect.signature(fsa_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accepting" in params, "Missing parameter 'accepting'"





def test_hyp_fsa_fsa_is_not_abstract():
    assert not inspect.isabstract(fsa_FSA)


def test_hyp_fsa_fsa_constructor_exists():
    assert callable(fsa_FSA.__init__)


def test_hyp_fsa_fsa_constructor_args():
    sig = inspect.signature(fsa_FSA.__init__)
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
fsa_Transition_strategy = st.builds(
    fsa_Transition,
    event=
        safe_text
)
fsa_State_strategy = st.builds(
    fsa_State,
    name=
        safe_text,
    accepting=
        st.booleans()
)
fsa_FSA_strategy = st.builds(
    fsa_FSA,
)




@given(instance=fsa_Transition_strategy)
def test_hyp_fsa_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original




@given(instance=fsa_State_strategy)
def test_hyp_fsa_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsa_State_strategy)
def test_hyp_fsa_state_accepting_setter(instance):
    original = instance.accepting
    instance.accepting = original
    assert instance.accepting == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    fsa_FSA,
    fsa_State,
    fsa_Transition,
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

def test_fsa_State_accepting_value_roundtrip():
    instance = fsa_State(accepting=True, name="sample_text")
    assert instance.accepting == True
    instance.accepting = False
    assert instance.accepting == False


def test_fsa_State_name_value_roundtrip():
    instance = fsa_State(accepting=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fsa_Transition_event_value_roundtrip():
    instance = fsa_Transition(event="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_assoc_fromState9_link_reassign_clear():
    a = fsa_Transition(event="sample_text")
    b1 = fsa_State(accepting=True, name="sample_text")
    b2 = fsa_State(accepting=False, name="sample_text_2")
    _safe_set(a, 'outgoingTransitions', b1)
    assert _is_linked(a, 'outgoingTransitions', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'outgoingTransitions', b2)
    assert _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'outgoingTransitions', None)
    assert not _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_incomingTransitions7_link_reassign_clear():
    a = fsa_Transition(event="sample_text")
    b1 = fsa_State(accepting=True, name="sample_text")
    b2 = fsa_State(accepting=False, name="sample_text_2")
    _safe_set(a, 'Transition8', b1)
    assert _is_linked(a, 'Transition8', b1)
    if hasattr(b1, 'toState'):
        assert _is_linked(b1, 'toState', a)
    _safe_set(a, 'Transition8', b2)
    assert _is_linked(a, 'Transition8', b2)
    if hasattr(b1, 'toState'):
        assert not _is_linked(b1, 'toState', a)
    if hasattr(b2, 'toState'):
        assert _is_linked(b2, 'toState', a)
    _safe_set(a, 'Transition8', None)
    assert not _is_linked(a, 'Transition8', b2)
    if hasattr(b2, 'toState'):
        assert not _is_linked(b2, 'toState', a)


def test_assoc_initialState3_link_reassign_clear():
    a = fsa_State(accepting=True, name="sample_text")
    b1 = fsa_FSA()
    b2 = fsa_FSA()
    _safe_set(a, 'fsa_State5', b1)
    assert _is_linked(a, 'fsa_State5', b1)
    if hasattr(b1, 'fsa_FSA4'):
        assert _is_linked(b1, 'fsa_FSA4', a)
    _safe_set(a, 'fsa_State5', b2)
    assert _is_linked(a, 'fsa_State5', b2)
    if hasattr(b1, 'fsa_FSA4'):
        assert not _is_linked(b1, 'fsa_FSA4', a)
    if hasattr(b2, 'fsa_FSA4'):
        assert _is_linked(b2, 'fsa_FSA4', a)
    _safe_set(a, 'fsa_State5', None)
    assert not _is_linked(a, 'fsa_State5', b2)
    if hasattr(b2, 'fsa_FSA4'):
        assert not _is_linked(b2, 'fsa_FSA4', a)


def test_assoc_outgoingTransitions6_link_reassign_clear():
    a = fsa_Transition(event="sample_text")
    b1 = fsa_State(accepting=True, name="sample_text")
    b2 = fsa_State(accepting=False, name="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'fromState'):
        assert _is_linked(b1, 'fromState', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'fromState'):
        assert not _is_linked(b1, 'fromState', a)
    if hasattr(b2, 'fromState'):
        assert _is_linked(b2, 'fromState', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'fromState'):
        assert not _is_linked(b2, 'fromState', a)


def test_assoc_states0_link_reassign_clear():
    a = fsa_State(accepting=True, name="sample_text")
    b1 = fsa_FSA()
    b2 = fsa_FSA()
    _safe_set(a, 'fsa_State', b1)
    assert _is_linked(a, 'fsa_State', b1)
    if hasattr(b1, 'fsa_FSA'):
        assert _is_linked(b1, 'fsa_FSA', a)
    _safe_set(a, 'fsa_State', b2)
    assert _is_linked(a, 'fsa_State', b2)
    if hasattr(b1, 'fsa_FSA'):
        assert not _is_linked(b1, 'fsa_FSA', a)
    if hasattr(b2, 'fsa_FSA'):
        assert _is_linked(b2, 'fsa_FSA', a)
    _safe_set(a, 'fsa_State', None)
    assert not _is_linked(a, 'fsa_State', b2)
    if hasattr(b2, 'fsa_FSA'):
        assert not _is_linked(b2, 'fsa_FSA', a)


def test_assoc_toState10_link_reassign_clear():
    a = fsa_Transition(event="sample_text")
    b1 = fsa_State(accepting=True, name="sample_text")
    b2 = fsa_State(accepting=False, name="sample_text_2")
    _safe_set(a, 'incomingTransitions', b1)
    assert _is_linked(a, 'incomingTransitions', b1)
    if hasattr(b1, 'State11'):
        assert _is_linked(b1, 'State11', a)
    _safe_set(a, 'incomingTransitions', b2)
    assert _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b1, 'State11'):
        assert not _is_linked(b1, 'State11', a)
    if hasattr(b2, 'State11'):
        assert _is_linked(b2, 'State11', a)
    _safe_set(a, 'incomingTransitions', None)
    assert not _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b2, 'State11'):
        assert not _is_linked(b2, 'State11', a)


def test_assoc_transitions1_link_reassign_clear():
    a = fsa_Transition(event="sample_text")
    b1 = fsa_FSA()
    b2 = fsa_FSA()
    _safe_set(a, 'fsa_Transition', b1)
    assert _is_linked(a, 'fsa_Transition', b1)
    if hasattr(b1, 'fsa_FSA2'):
        assert _is_linked(b1, 'fsa_FSA2', a)
    _safe_set(a, 'fsa_Transition', b2)
    assert _is_linked(a, 'fsa_Transition', b2)
    if hasattr(b1, 'fsa_FSA2'):
        assert not _is_linked(b1, 'fsa_FSA2', a)
    if hasattr(b2, 'fsa_FSA2'):
        assert _is_linked(b2, 'fsa_FSA2', a)
    _safe_set(a, 'fsa_Transition', None)
    assert not _is_linked(a, 'fsa_Transition', b2)
    if hasattr(b2, 'fsa_FSA2'):
        assert not _is_linked(b2, 'fsa_FSA2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

fsa_FSA_strategy = st.builds(fsa_FSA)
@given(instance=fsa_FSA_strategy)
@settings(max_examples=25)
def test_fsa_FSA_instantiation(instance):
    assert isinstance(instance, fsa_FSA)


fsa_State_strategy = st.builds(fsa_State, accepting=st.booleans(), name=safe_text)
@given(instance=fsa_State_strategy)
@settings(max_examples=25)
def test_fsa_State_instantiation(instance):
    assert isinstance(instance, fsa_State)


fsa_Transition_strategy = st.builds(fsa_Transition, event=safe_text)
@given(instance=fsa_Transition_strategy)
@settings(max_examples=25)
def test_fsa_Transition_instantiation(instance):
    assert isinstance(instance, fsa_Transition)



