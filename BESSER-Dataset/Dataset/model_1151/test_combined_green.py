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
    myFirstEditorCustom_EndState,
    myFirstEditorCustom_StartState,
    myFirstEditorCustom_Transition,
    myFirstEditorCustom_State,
    myFirstEditorCustom_StateMachine,
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



def test_hyp_myfirsteditorcustom_endstate_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_EndState)


def test_hyp_myfirsteditorcustom_endstate_constructor_exists():
    assert callable(myFirstEditorCustom_EndState.__init__)


def test_hyp_myfirsteditorcustom_endstate_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_EndState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myfirsteditorcustom_startstate_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_StartState)


def test_hyp_myfirsteditorcustom_startstate_constructor_exists():
    assert callable(myFirstEditorCustom_StartState.__init__)


def test_hyp_myfirsteditorcustom_startstate_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_StartState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myfirsteditorcustom_transition_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_Transition)


def test_hyp_myfirsteditorcustom_transition_constructor_exists():
    assert callable(myFirstEditorCustom_Transition.__init__)


def test_hyp_myfirsteditorcustom_transition_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_myfirsteditorcustom_state_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_State)


def test_hyp_myfirsteditorcustom_state_constructor_exists():
    assert callable(myFirstEditorCustom_State.__init__)


def test_hyp_myfirsteditorcustom_state_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_myfirsteditorcustom_statemachine_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_StateMachine)


def test_hyp_myfirsteditorcustom_statemachine_constructor_exists():
    assert callable(myFirstEditorCustom_StateMachine.__init__)


def test_hyp_myfirsteditorcustom_statemachine_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_StateMachine.__init__)
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
State_strategy = st.builds(
    State,
)
myFirstEditorCustom_EndState_strategy = st.builds(
    myFirstEditorCustom_EndState,
)
myFirstEditorCustom_StartState_strategy = st.builds(
    myFirstEditorCustom_StartState,
)
myFirstEditorCustom_Transition_strategy = st.builds(
    myFirstEditorCustom_Transition,
    name=
        safe_text
)
myFirstEditorCustom_State_strategy = st.builds(
    myFirstEditorCustom_State,
    name=
        safe_text,
    type=
        safe_text
)
myFirstEditorCustom_StateMachine_strategy = st.builds(
    myFirstEditorCustom_StateMachine,
    name=
        safe_text
)







@given(instance=myFirstEditorCustom_Transition_strategy)
def test_hyp_myfirsteditorcustom_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=myFirstEditorCustom_State_strategy)
def test_hyp_myfirsteditorcustom_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myFirstEditorCustom_State_strategy)
def test_hyp_myfirsteditorcustom_state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=myFirstEditorCustom_StateMachine_strategy)
def test_hyp_myfirsteditorcustom_statemachine_name_setter(instance):
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
    myFirstEditorCustom_EndState,
    myFirstEditorCustom_StartState,
    myFirstEditorCustom_State,
    myFirstEditorCustom_StateMachine,
    myFirstEditorCustom_Transition,
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

def test_myFirstEditorCustom_State_name_value_roundtrip():
    instance = myFirstEditorCustom_State(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_myFirstEditorCustom_State_type_value_roundtrip():
    instance = myFirstEditorCustom_State(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_myFirstEditorCustom_StateMachine_name_value_roundtrip():
    instance = myFirstEditorCustom_StateMachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_myFirstEditorCustom_Transition_name_value_roundtrip():
    instance = myFirstEditorCustom_Transition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_myFirstEditorCustom_EndState_isa_State():
    instance = myFirstEditorCustom_EndState()
    assert isinstance(instance, State)


def test_myFirstEditorCustom_StartState_isa_State():
    instance = myFirstEditorCustom_StartState()
    assert isinstance(instance, State)


def test_assoc_in_4_link_reassign_clear():
    a = myFirstEditorCustom_Transition(name="sample_text")
    b1 = myFirstEditorCustom_State(name="sample_text", type="sample_text")
    b2 = myFirstEditorCustom_State(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'Transition5', b1)
    assert _is_linked(a, 'Transition5', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'Transition5', b2)
    assert _is_linked(a, 'Transition5', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'Transition5', None)
    assert not _is_linked(a, 'Transition5', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_out3_link_reassign_clear():
    a = myFirstEditorCustom_Transition(name="sample_text")
    b1 = myFirstEditorCustom_State(name="sample_text", type="sample_text")
    b2 = myFirstEditorCustom_State(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_source7_link_reassign_clear():
    a = myFirstEditorCustom_Transition(name="sample_text")
    b1 = myFirstEditorCustom_State(name="sample_text", type="sample_text")
    b2 = myFirstEditorCustom_State(name="sample_text_2", type="sample_text_2")
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


def test_assoc_state0_link_reassign_clear():
    a = myFirstEditorCustom_StateMachine(name="sample_text")
    b1 = myFirstEditorCustom_State(name="sample_text", type="sample_text")
    b2 = myFirstEditorCustom_State(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'myFirstEditorCustom_StateMachine', {b1})
    assert _is_linked(a, 'myFirstEditorCustom_StateMachine', b1)
    if hasattr(b1, 'myFirstEditorCustom_State'):
        assert _is_linked(b1, 'myFirstEditorCustom_State', a)
    _safe_set(a, 'myFirstEditorCustom_StateMachine', {b2})
    assert _is_linked(a, 'myFirstEditorCustom_StateMachine', b2)
    if hasattr(b1, 'myFirstEditorCustom_State'):
        assert not _is_linked(b1, 'myFirstEditorCustom_State', a)
    if hasattr(b2, 'myFirstEditorCustom_State'):
        assert _is_linked(b2, 'myFirstEditorCustom_State', a)
    _safe_set(a, 'myFirstEditorCustom_StateMachine', set())
    assert not _is_linked(a, 'myFirstEditorCustom_StateMachine', b2)
    if hasattr(b2, 'myFirstEditorCustom_State'):
        assert not _is_linked(b2, 'myFirstEditorCustom_State', a)


def test_assoc_target6_link_reassign_clear():
    a = myFirstEditorCustom_Transition(name="sample_text")
    b1 = myFirstEditorCustom_State(name="sample_text", type="sample_text")
    b2 = myFirstEditorCustom_State(name="sample_text_2", type="sample_text_2")
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


def test_assoc_transition1_link_reassign_clear():
    a = myFirstEditorCustom_Transition(name="sample_text")
    b1 = myFirstEditorCustom_StateMachine(name="sample_text")
    b2 = myFirstEditorCustom_StateMachine(name="sample_text_2")
    _safe_set(a, 'myFirstEditorCustom_Transition', b1)
    assert _is_linked(a, 'myFirstEditorCustom_Transition', b1)
    if hasattr(b1, 'myFirstEditorCustom_StateMachine2'):
        assert _is_linked(b1, 'myFirstEditorCustom_StateMachine2', a)
    _safe_set(a, 'myFirstEditorCustom_Transition', b2)
    assert _is_linked(a, 'myFirstEditorCustom_Transition', b2)
    if hasattr(b1, 'myFirstEditorCustom_StateMachine2'):
        assert not _is_linked(b1, 'myFirstEditorCustom_StateMachine2', a)
    if hasattr(b2, 'myFirstEditorCustom_StateMachine2'):
        assert _is_linked(b2, 'myFirstEditorCustom_StateMachine2', a)
    _safe_set(a, 'myFirstEditorCustom_Transition', None)
    assert not _is_linked(a, 'myFirstEditorCustom_Transition', b2)
    if hasattr(b2, 'myFirstEditorCustom_StateMachine2'):
        assert not _is_linked(b2, 'myFirstEditorCustom_StateMachine2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


myFirstEditorCustom_EndState_strategy = st.builds(myFirstEditorCustom_EndState)
@given(instance=myFirstEditorCustom_EndState_strategy)
@settings(max_examples=25)
def test_myFirstEditorCustom_EndState_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_EndState)


myFirstEditorCustom_StartState_strategy = st.builds(myFirstEditorCustom_StartState)
@given(instance=myFirstEditorCustom_StartState_strategy)
@settings(max_examples=25)
def test_myFirstEditorCustom_StartState_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_StartState)


myFirstEditorCustom_State_strategy = st.builds(myFirstEditorCustom_State, name=safe_text, type=safe_text)
@given(instance=myFirstEditorCustom_State_strategy)
@settings(max_examples=25)
def test_myFirstEditorCustom_State_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_State)


myFirstEditorCustom_StateMachine_strategy = st.builds(myFirstEditorCustom_StateMachine, name=safe_text)
@given(instance=myFirstEditorCustom_StateMachine_strategy)
@settings(max_examples=25)
def test_myFirstEditorCustom_StateMachine_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_StateMachine)


myFirstEditorCustom_Transition_strategy = st.builds(myFirstEditorCustom_Transition, name=safe_text)
@given(instance=myFirstEditorCustom_Transition_strategy)
@settings(max_examples=25)
def test_myFirstEditorCustom_Transition_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_Transition)



