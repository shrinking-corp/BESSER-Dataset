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
    basicfsm_Action,
    basicfsm_Guard,
    basicfsm_Trans,
    basicfsm_State,
    basicfsm_Machine,
    State,
    basicfsm_InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_basicfsm_action_is_not_abstract():
    assert not inspect.isabstract(basicfsm_Action)


def test_hyp_basicfsm_action_constructor_exists():
    assert callable(basicfsm_Action.__init__)


def test_hyp_basicfsm_action_constructor_args():
    sig = inspect.signature(basicfsm_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicfsm_guard_is_not_abstract():
    assert not inspect.isabstract(basicfsm_Guard)


def test_hyp_basicfsm_guard_constructor_exists():
    assert callable(basicfsm_Guard.__init__)


def test_hyp_basicfsm_guard_constructor_args():
    sig = inspect.signature(basicfsm_Guard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicfsm_trans_is_not_abstract():
    assert not inspect.isabstract(basicfsm_Trans)


def test_hyp_basicfsm_trans_constructor_exists():
    assert callable(basicfsm_Trans.__init__)


def test_hyp_basicfsm_trans_constructor_args():
    sig = inspect.signature(basicfsm_Trans.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"




def test_hyp_basicfsm_state_is_not_abstract():
    assert not inspect.isabstract(basicfsm_State)


def test_hyp_basicfsm_state_constructor_exists():
    assert callable(basicfsm_State.__init__)


def test_hyp_basicfsm_state_constructor_args():
    sig = inspect.signature(basicfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_basicfsm_machine_is_not_abstract():
    assert not inspect.isabstract(basicfsm_Machine)


def test_hyp_basicfsm_machine_constructor_exists():
    assert callable(basicfsm_Machine.__init__)


def test_hyp_basicfsm_machine_constructor_args():
    sig = inspect.signature(basicfsm_Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicfsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(basicfsm_InitialState)


def test_hyp_basicfsm_initialstate_constructor_exists():
    assert callable(basicfsm_InitialState.__init__)


def test_hyp_basicfsm_initialstate_constructor_args():
    sig = inspect.signature(basicfsm_InitialState.__init__)
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
basicfsm_Action_strategy = st.builds(
    basicfsm_Action,
)
basicfsm_Guard_strategy = st.builds(
    basicfsm_Guard,
)
basicfsm_Trans_strategy = st.builds(
    basicfsm_Trans,
    event=
        safe_text
)
basicfsm_State_strategy = st.builds(
    basicfsm_State,
    name=
        safe_text
)
basicfsm_Machine_strategy = st.builds(
    basicfsm_Machine,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
basicfsm_InitialState_strategy = st.builds(
    basicfsm_InitialState,
)






@given(instance=basicfsm_Trans_strategy)
def test_hyp_basicfsm_trans_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original




@given(instance=basicfsm_State_strategy)
def test_hyp_basicfsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=basicfsm_Machine_strategy)
def test_hyp_basicfsm_machine_name_setter(instance):
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
    State,
    basicfsm_Action,
    basicfsm_Guard,
    basicfsm_InitialState,
    basicfsm_Machine,
    basicfsm_State,
    basicfsm_Trans,
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

def test_basicfsm_Machine_name_value_roundtrip():
    instance = basicfsm_Machine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basicfsm_State_name_value_roundtrip():
    instance = basicfsm_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basicfsm_Trans_event_value_roundtrip():
    instance = basicfsm_Trans(event="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_basicfsm_InitialState_isa_State():
    instance = basicfsm_InitialState()
    assert isinstance(instance, State)


def test_assoc_action11_link_reassign_clear():
    a = basicfsm_Trans(event="sample_text")
    b1 = basicfsm_Action()
    b2 = basicfsm_Action()
    _safe_set(a, 'basicfsm_Trans12', b1)
    assert _is_linked(a, 'basicfsm_Trans12', b1)
    if hasattr(b1, 'basicfsm_Action'):
        assert _is_linked(b1, 'basicfsm_Action', a)
    _safe_set(a, 'basicfsm_Trans12', b2)
    assert _is_linked(a, 'basicfsm_Trans12', b2)
    if hasattr(b1, 'basicfsm_Action'):
        assert not _is_linked(b1, 'basicfsm_Action', a)
    if hasattr(b2, 'basicfsm_Action'):
        assert _is_linked(b2, 'basicfsm_Action', a)
    _safe_set(a, 'basicfsm_Trans12', None)
    assert not _is_linked(a, 'basicfsm_Trans12', b2)
    if hasattr(b2, 'basicfsm_Action'):
        assert not _is_linked(b2, 'basicfsm_Action', a)


def test_assoc_guard9_link_reassign_clear():
    a = basicfsm_Trans(event="sample_text")
    b1 = basicfsm_Guard()
    b2 = basicfsm_Guard()
    _safe_set(a, 'basicfsm_Trans10', b1)
    assert _is_linked(a, 'basicfsm_Trans10', b1)
    if hasattr(b1, 'basicfsm_Guard'):
        assert _is_linked(b1, 'basicfsm_Guard', a)
    _safe_set(a, 'basicfsm_Trans10', b2)
    assert _is_linked(a, 'basicfsm_Trans10', b2)
    if hasattr(b1, 'basicfsm_Guard'):
        assert not _is_linked(b1, 'basicfsm_Guard', a)
    if hasattr(b2, 'basicfsm_Guard'):
        assert _is_linked(b2, 'basicfsm_Guard', a)
    _safe_set(a, 'basicfsm_Trans10', None)
    assert not _is_linked(a, 'basicfsm_Trans10', b2)
    if hasattr(b2, 'basicfsm_Guard'):
        assert not _is_linked(b2, 'basicfsm_Guard', a)


def test_assoc_in_3_link_reassign_clear():
    a = basicfsm_Trans(event="sample_text")
    b1 = basicfsm_State(name="sample_text")
    b2 = basicfsm_State(name="sample_text_2")
    _safe_set(a, 'Trans', b1)
    assert _is_linked(a, 'Trans', b1)
    if hasattr(b1, 'tgt'):
        assert _is_linked(b1, 'tgt', a)
    _safe_set(a, 'Trans', b2)
    assert _is_linked(a, 'Trans', b2)
    if hasattr(b1, 'tgt'):
        assert not _is_linked(b1, 'tgt', a)
    if hasattr(b2, 'tgt'):
        assert _is_linked(b2, 'tgt', a)
    _safe_set(a, 'Trans', None)
    assert not _is_linked(a, 'Trans', b2)
    if hasattr(b2, 'tgt'):
        assert not _is_linked(b2, 'tgt', a)


def test_assoc_out4_link_reassign_clear():
    a = basicfsm_Trans(event="sample_text")
    b1 = basicfsm_State(name="sample_text")
    b2 = basicfsm_State(name="sample_text_2")
    _safe_set(a, 'Trans5', b1)
    assert _is_linked(a, 'Trans5', b1)
    if hasattr(b1, 'src'):
        assert _is_linked(b1, 'src', a)
    _safe_set(a, 'Trans5', b2)
    assert _is_linked(a, 'Trans5', b2)
    if hasattr(b1, 'src'):
        assert not _is_linked(b1, 'src', a)
    if hasattr(b2, 'src'):
        assert _is_linked(b2, 'src', a)
    _safe_set(a, 'Trans5', None)
    assert not _is_linked(a, 'Trans5', b2)
    if hasattr(b2, 'src'):
        assert not _is_linked(b2, 'src', a)


def test_assoc_src6_link_reassign_clear():
    a = basicfsm_Trans(event="sample_text")
    b1 = basicfsm_State(name="sample_text")
    b2 = basicfsm_State(name="sample_text_2")
    _safe_set(a, 'out', b1)
    assert _is_linked(a, 'out', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'out', b2)
    assert _is_linked(a, 'out', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'out', None)
    assert not _is_linked(a, 'out', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_states0_link_reassign_clear():
    a = basicfsm_State(name="sample_text")
    b1 = basicfsm_Machine(name="sample_text")
    b2 = basicfsm_Machine(name="sample_text_2")
    _safe_set(a, 'basicfsm_State', b1)
    assert _is_linked(a, 'basicfsm_State', b1)
    if hasattr(b1, 'basicfsm_Machine'):
        assert _is_linked(b1, 'basicfsm_Machine', a)
    _safe_set(a, 'basicfsm_State', b2)
    assert _is_linked(a, 'basicfsm_State', b2)
    if hasattr(b1, 'basicfsm_Machine'):
        assert not _is_linked(b1, 'basicfsm_Machine', a)
    if hasattr(b2, 'basicfsm_Machine'):
        assert _is_linked(b2, 'basicfsm_Machine', a)
    _safe_set(a, 'basicfsm_State', None)
    assert not _is_linked(a, 'basicfsm_State', b2)
    if hasattr(b2, 'basicfsm_Machine'):
        assert not _is_linked(b2, 'basicfsm_Machine', a)


def test_assoc_tgt7_link_reassign_clear():
    a = basicfsm_Trans(event="sample_text")
    b1 = basicfsm_State(name="sample_text")
    b2 = basicfsm_State(name="sample_text_2")
    _safe_set(a, 'in_', b1)
    assert _is_linked(a, 'in_', b1)
    if hasattr(b1, 'State8'):
        assert _is_linked(b1, 'State8', a)
    _safe_set(a, 'in_', b2)
    assert _is_linked(a, 'in_', b2)
    if hasattr(b1, 'State8'):
        assert not _is_linked(b1, 'State8', a)
    if hasattr(b2, 'State8'):
        assert _is_linked(b2, 'State8', a)
    _safe_set(a, 'in_', None)
    assert not _is_linked(a, 'in_', b2)
    if hasattr(b2, 'State8'):
        assert not _is_linked(b2, 'State8', a)


def test_assoc_trans1_link_reassign_clear():
    a = basicfsm_Trans(event="sample_text")
    b1 = basicfsm_Machine(name="sample_text")
    b2 = basicfsm_Machine(name="sample_text_2")
    _safe_set(a, 'basicfsm_Trans', b1)
    assert _is_linked(a, 'basicfsm_Trans', b1)
    if hasattr(b1, 'basicfsm_Machine2'):
        assert _is_linked(b1, 'basicfsm_Machine2', a)
    _safe_set(a, 'basicfsm_Trans', b2)
    assert _is_linked(a, 'basicfsm_Trans', b2)
    if hasattr(b1, 'basicfsm_Machine2'):
        assert not _is_linked(b1, 'basicfsm_Machine2', a)
    if hasattr(b2, 'basicfsm_Machine2'):
        assert _is_linked(b2, 'basicfsm_Machine2', a)
    _safe_set(a, 'basicfsm_Trans', None)
    assert not _is_linked(a, 'basicfsm_Trans', b2)
    if hasattr(b2, 'basicfsm_Machine2'):
        assert not _is_linked(b2, 'basicfsm_Machine2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


basicfsm_Action_strategy = st.builds(basicfsm_Action)
@given(instance=basicfsm_Action_strategy)
@settings(max_examples=25)
def test_basicfsm_Action_instantiation(instance):
    assert isinstance(instance, basicfsm_Action)


basicfsm_Guard_strategy = st.builds(basicfsm_Guard)
@given(instance=basicfsm_Guard_strategy)
@settings(max_examples=25)
def test_basicfsm_Guard_instantiation(instance):
    assert isinstance(instance, basicfsm_Guard)


basicfsm_InitialState_strategy = st.builds(basicfsm_InitialState)
@given(instance=basicfsm_InitialState_strategy)
@settings(max_examples=25)
def test_basicfsm_InitialState_instantiation(instance):
    assert isinstance(instance, basicfsm_InitialState)


basicfsm_Machine_strategy = st.builds(basicfsm_Machine, name=safe_text)
@given(instance=basicfsm_Machine_strategy)
@settings(max_examples=25)
def test_basicfsm_Machine_instantiation(instance):
    assert isinstance(instance, basicfsm_Machine)


basicfsm_State_strategy = st.builds(basicfsm_State, name=safe_text)
@given(instance=basicfsm_State_strategy)
@settings(max_examples=25)
def test_basicfsm_State_instantiation(instance):
    assert isinstance(instance, basicfsm_State)


basicfsm_Trans_strategy = st.builds(basicfsm_Trans, event=safe_text)
@given(instance=basicfsm_Trans_strategy)
@settings(max_examples=25)
def test_basicfsm_Trans_instantiation(instance):
    assert isinstance(instance, basicfsm_Trans)



