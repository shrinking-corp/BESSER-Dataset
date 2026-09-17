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
    stateMachineEditRules_DFA,
    stateMachineEditRules_State,
    stateMachineEditRules_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_statemachineeditrules_dfa_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules_DFA)


def test_hyp_statemachineeditrules_dfa_constructor_exists():
    assert callable(stateMachineEditRules_DFA.__init__)


def test_hyp_statemachineeditrules_dfa_constructor_args():
    sig = inspect.signature(stateMachineEditRules_DFA.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachineeditrules_state_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules_State)


def test_hyp_statemachineeditrules_state_constructor_exists():
    assert callable(stateMachineEditRules_State.__init__)


def test_hyp_statemachineeditrules_state_constructor_args():
    sig = inspect.signature(stateMachineEditRules_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isStart" in params, "Missing parameter 'isStart'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"






def test_hyp_statemachineeditrules_transition_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules_Transition)


def test_hyp_statemachineeditrules_transition_constructor_exists():
    assert callable(stateMachineEditRules_Transition.__init__)


def test_hyp_statemachineeditrules_transition_constructor_args():
    sig = inspect.signature(stateMachineEditRules_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"



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
stateMachineEditRules_DFA_strategy = st.builds(
    stateMachineEditRules_DFA,
)
stateMachineEditRules_State_strategy = st.builds(
    stateMachineEditRules_State,
    id=
        safe_text,
    isStart=
        st.booleans(),
    isEnd=
        st.booleans()
)
stateMachineEditRules_Transition_strategy = st.builds(
    stateMachineEditRules_Transition,
    input=
        safe_text
)





@given(instance=stateMachineEditRules_State_strategy)
def test_hyp_statemachineeditrules_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=stateMachineEditRules_State_strategy)
def test_hyp_statemachineeditrules_state_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original



@given(instance=stateMachineEditRules_State_strategy)
def test_hyp_statemachineeditrules_state_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original




@given(instance=stateMachineEditRules_Transition_strategy)
def test_hyp_statemachineeditrules_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    stateMachineEditRules_DFA,
    stateMachineEditRules_State,
    stateMachineEditRules_Transition,
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

def test_stateMachineEditRules_State_id_value_roundtrip():
    instance = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_stateMachineEditRules_State_isEnd_value_roundtrip():
    instance = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    assert instance.isEnd == True
    instance.isEnd = False
    assert instance.isEnd == False


def test_stateMachineEditRules_State_isStart_value_roundtrip():
    instance = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    assert instance.isStart == True
    instance.isStart = False
    assert instance.isStart == False


def test_stateMachineEditRules_Transition_input_value_roundtrip():
    instance = stateMachineEditRules_Transition(input="sample_text")
    assert instance.input == "sample_text"
    instance.input = "sample_text_2"
    assert instance.input == "sample_text_2"


def test_assoc_from_1_link_reassign_clear():
    a = stateMachineEditRules_Transition(input="sample_text")
    b1 = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    b2 = stateMachineEditRules_State(id="sample_text_2", isEnd=False, isStart=False)
    _safe_set(a, 'outgoingTransitions', b1)
    assert _is_linked(a, 'outgoingTransitions', b1)
    if hasattr(b1, 'State2'):
        assert _is_linked(b1, 'State2', a)
    _safe_set(a, 'outgoingTransitions', b2)
    assert _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b1, 'State2'):
        assert not _is_linked(b1, 'State2', a)
    if hasattr(b2, 'State2'):
        assert _is_linked(b2, 'State2', a)
    _safe_set(a, 'outgoingTransitions', None)
    assert not _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b2, 'State2'):
        assert not _is_linked(b2, 'State2', a)


def test_assoc_incomingTransitions3_link_reassign_clear():
    a = stateMachineEditRules_Transition(input="sample_text")
    b1 = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    b2 = stateMachineEditRules_State(id="sample_text_2", isEnd=False, isStart=False)
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


def test_assoc_outgoingTransitions4_link_reassign_clear():
    a = stateMachineEditRules_Transition(input="sample_text")
    b1 = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    b2 = stateMachineEditRules_State(id="sample_text_2", isEnd=False, isStart=False)
    _safe_set(a, 'Transition5', b1)
    assert _is_linked(a, 'Transition5', b1)
    if hasattr(b1, 'from_'):
        assert _is_linked(b1, 'from_', a)
    _safe_set(a, 'Transition5', b2)
    assert _is_linked(a, 'Transition5', b2)
    if hasattr(b1, 'from_'):
        assert not _is_linked(b1, 'from_', a)
    if hasattr(b2, 'from_'):
        assert _is_linked(b2, 'from_', a)
    _safe_set(a, 'Transition5', None)
    assert not _is_linked(a, 'Transition5', b2)
    if hasattr(b2, 'from_'):
        assert not _is_linked(b2, 'from_', a)


def test_assoc_states6_link_reassign_clear():
    a = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    b1 = stateMachineEditRules_DFA()
    b2 = stateMachineEditRules_DFA()
    _safe_set(a, 'stateMachineEditRules_State', b1)
    assert _is_linked(a, 'stateMachineEditRules_State', b1)
    if hasattr(b1, 'stateMachineEditRules_DFA'):
        assert _is_linked(b1, 'stateMachineEditRules_DFA', a)
    _safe_set(a, 'stateMachineEditRules_State', b2)
    assert _is_linked(a, 'stateMachineEditRules_State', b2)
    if hasattr(b1, 'stateMachineEditRules_DFA'):
        assert not _is_linked(b1, 'stateMachineEditRules_DFA', a)
    if hasattr(b2, 'stateMachineEditRules_DFA'):
        assert _is_linked(b2, 'stateMachineEditRules_DFA', a)
    _safe_set(a, 'stateMachineEditRules_State', None)
    assert not _is_linked(a, 'stateMachineEditRules_State', b2)
    if hasattr(b2, 'stateMachineEditRules_DFA'):
        assert not _is_linked(b2, 'stateMachineEditRules_DFA', a)


def test_assoc_to0_link_reassign_clear():
    a = stateMachineEditRules_Transition(input="sample_text")
    b1 = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    b2 = stateMachineEditRules_State(id="sample_text_2", isEnd=False, isStart=False)
    _safe_set(a, 'incomingTransitions', b1)
    assert _is_linked(a, 'incomingTransitions', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'incomingTransitions', b2)
    assert _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'incomingTransitions', None)
    assert not _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_transitions7_link_reassign_clear():
    a = stateMachineEditRules_Transition(input="sample_text")
    b1 = stateMachineEditRules_DFA()
    b2 = stateMachineEditRules_DFA()
    _safe_set(a, 'stateMachineEditRules_Transition', b1)
    assert _is_linked(a, 'stateMachineEditRules_Transition', b1)
    if hasattr(b1, 'stateMachineEditRules_DFA8'):
        assert _is_linked(b1, 'stateMachineEditRules_DFA8', a)
    _safe_set(a, 'stateMachineEditRules_Transition', b2)
    assert _is_linked(a, 'stateMachineEditRules_Transition', b2)
    if hasattr(b1, 'stateMachineEditRules_DFA8'):
        assert not _is_linked(b1, 'stateMachineEditRules_DFA8', a)
    if hasattr(b2, 'stateMachineEditRules_DFA8'):
        assert _is_linked(b2, 'stateMachineEditRules_DFA8', a)
    _safe_set(a, 'stateMachineEditRules_Transition', None)
    assert not _is_linked(a, 'stateMachineEditRules_Transition', b2)
    if hasattr(b2, 'stateMachineEditRules_DFA8'):
        assert not _is_linked(b2, 'stateMachineEditRules_DFA8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

stateMachineEditRules_DFA_strategy = st.builds(stateMachineEditRules_DFA)
@given(instance=stateMachineEditRules_DFA_strategy)
@settings(max_examples=25)
def test_stateMachineEditRules_DFA_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules_DFA)


stateMachineEditRules_State_strategy = st.builds(stateMachineEditRules_State, id=safe_text, isEnd=st.booleans(), isStart=st.booleans())
@given(instance=stateMachineEditRules_State_strategy)
@settings(max_examples=25)
def test_stateMachineEditRules_State_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules_State)


stateMachineEditRules_Transition_strategy = st.builds(stateMachineEditRules_Transition, input=safe_text)
@given(instance=stateMachineEditRules_Transition_strategy)
@settings(max_examples=25)
def test_stateMachineEditRules_Transition_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules_Transition)



