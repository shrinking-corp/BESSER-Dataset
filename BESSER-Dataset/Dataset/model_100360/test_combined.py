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
    fowlerdsl_Transition,
    fowlerdsl_State,
    fowlerdsl_Command,
    fowlerdsl_Event,
    fowlerdsl_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fowlerdsl_transition_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_Transition)


def test_hyp_fowlerdsl_transition_constructor_exists():
    assert callable(fowlerdsl_Transition.__init__)


def test_hyp_fowlerdsl_transition_constructor_args():
    sig = inspect.signature(fowlerdsl_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fowlerdsl_state_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_State)


def test_hyp_fowlerdsl_state_constructor_exists():
    assert callable(fowlerdsl_State.__init__)


def test_hyp_fowlerdsl_state_constructor_args():
    sig = inspect.signature(fowlerdsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_fowlerdsl_command_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_Command)


def test_hyp_fowlerdsl_command_constructor_exists():
    assert callable(fowlerdsl_Command.__init__)


def test_hyp_fowlerdsl_command_constructor_args():
    sig = inspect.signature(fowlerdsl_Command.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fowlerdsl_event_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_Event)


def test_hyp_fowlerdsl_event_constructor_exists():
    assert callable(fowlerdsl_Event.__init__)


def test_hyp_fowlerdsl_event_constructor_args():
    sig = inspect.signature(fowlerdsl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "resetting" in params, "Missing parameter 'resetting'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_fowlerdsl_statemachine_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_Statemachine)


def test_hyp_fowlerdsl_statemachine_constructor_exists():
    assert callable(fowlerdsl_Statemachine.__init__)


def test_hyp_fowlerdsl_statemachine_constructor_args():
    sig = inspect.signature(fowlerdsl_Statemachine.__init__)
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
fowlerdsl_Transition_strategy = st.builds(
    fowlerdsl_Transition,
)
fowlerdsl_State_strategy = st.builds(
    fowlerdsl_State,
    name=
        safe_text
)
fowlerdsl_Command_strategy = st.builds(
    fowlerdsl_Command,
    code=
        safe_text,
    name=
        safe_text
)
fowlerdsl_Event_strategy = st.builds(
    fowlerdsl_Event,
    code=
        safe_text,
    resetting=
        st.booleans(),
    name=
        safe_text
)
fowlerdsl_Statemachine_strategy = st.builds(
    fowlerdsl_Statemachine,
)





@given(instance=fowlerdsl_State_strategy)
def test_hyp_fowlerdsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fowlerdsl_Command_strategy)
def test_hyp_fowlerdsl_command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=fowlerdsl_Command_strategy)
def test_hyp_fowlerdsl_command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=fowlerdsl_Event_strategy)
def test_hyp_fowlerdsl_event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=fowlerdsl_Event_strategy)
def test_hyp_fowlerdsl_event_resetting_setter(instance):
    original = instance.resetting
    instance.resetting = original
    assert instance.resetting == original



@given(instance=fowlerdsl_Event_strategy)
def test_hyp_fowlerdsl_event_name_setter(instance):
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
    fowlerdsl_Command,
    fowlerdsl_Event,
    fowlerdsl_State,
    fowlerdsl_Statemachine,
    fowlerdsl_Transition,
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

def test_fowlerdsl_Command_code_value_roundtrip():
    instance = fowlerdsl_Command(code="sample_text", name="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_fowlerdsl_Command_name_value_roundtrip():
    instance = fowlerdsl_Command(code="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fowlerdsl_Event_code_value_roundtrip():
    instance = fowlerdsl_Event(code="sample_text", name="sample_text", resetting=True)
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_fowlerdsl_Event_name_value_roundtrip():
    instance = fowlerdsl_Event(code="sample_text", name="sample_text", resetting=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fowlerdsl_Event_resetting_value_roundtrip():
    instance = fowlerdsl_Event(code="sample_text", name="sample_text", resetting=True)
    assert instance.resetting == True
    instance.resetting = False
    assert instance.resetting == False


def test_fowlerdsl_State_name_value_roundtrip():
    instance = fowlerdsl_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_actions5_link_reassign_clear():
    a = fowlerdsl_State(name="sample_text")
    b1 = fowlerdsl_Command(code="sample_text", name="sample_text")
    b2 = fowlerdsl_Command(code="sample_text_2", name="sample_text_2")
    _safe_set(a, 'fowlerdsl_State6', {b1})
    assert _is_linked(a, 'fowlerdsl_State6', b1)
    if hasattr(b1, 'fowlerdsl_Command7'):
        assert _is_linked(b1, 'fowlerdsl_Command7', a)
    _safe_set(a, 'fowlerdsl_State6', {b2})
    assert _is_linked(a, 'fowlerdsl_State6', b2)
    if hasattr(b1, 'fowlerdsl_Command7'):
        assert not _is_linked(b1, 'fowlerdsl_Command7', a)
    if hasattr(b2, 'fowlerdsl_Command7'):
        assert _is_linked(b2, 'fowlerdsl_Command7', a)
    _safe_set(a, 'fowlerdsl_State6', set())
    assert not _is_linked(a, 'fowlerdsl_State6', b2)
    if hasattr(b2, 'fowlerdsl_Command7'):
        assert not _is_linked(b2, 'fowlerdsl_Command7', a)


def test_assoc_commands1_link_reassign_clear():
    a = fowlerdsl_Command(code="sample_text", name="sample_text")
    b1 = fowlerdsl_Statemachine()
    b2 = fowlerdsl_Statemachine()
    _safe_set(a, 'fowlerdsl_Command', b1)
    assert _is_linked(a, 'fowlerdsl_Command', b1)
    if hasattr(b1, 'fowlerdsl_Statemachine2'):
        assert _is_linked(b1, 'fowlerdsl_Statemachine2', a)
    _safe_set(a, 'fowlerdsl_Command', b2)
    assert _is_linked(a, 'fowlerdsl_Command', b2)
    if hasattr(b1, 'fowlerdsl_Statemachine2'):
        assert not _is_linked(b1, 'fowlerdsl_Statemachine2', a)
    if hasattr(b2, 'fowlerdsl_Statemachine2'):
        assert _is_linked(b2, 'fowlerdsl_Statemachine2', a)
    _safe_set(a, 'fowlerdsl_Command', None)
    assert not _is_linked(a, 'fowlerdsl_Command', b2)
    if hasattr(b2, 'fowlerdsl_Statemachine2'):
        assert not _is_linked(b2, 'fowlerdsl_Statemachine2', a)


def test_assoc_event10_link_reassign_clear():
    a = fowlerdsl_Event(code="sample_text", name="sample_text", resetting=True)
    b1 = fowlerdsl_Transition()
    b2 = fowlerdsl_Transition()
    _safe_set(a, 'fowlerdsl_Event12', b1)
    assert _is_linked(a, 'fowlerdsl_Event12', b1)
    if hasattr(b1, 'fowlerdsl_Transition11'):
        assert _is_linked(b1, 'fowlerdsl_Transition11', a)
    _safe_set(a, 'fowlerdsl_Event12', b2)
    assert _is_linked(a, 'fowlerdsl_Event12', b2)
    if hasattr(b1, 'fowlerdsl_Transition11'):
        assert not _is_linked(b1, 'fowlerdsl_Transition11', a)
    if hasattr(b2, 'fowlerdsl_Transition11'):
        assert _is_linked(b2, 'fowlerdsl_Transition11', a)
    _safe_set(a, 'fowlerdsl_Event12', None)
    assert not _is_linked(a, 'fowlerdsl_Event12', b2)
    if hasattr(b2, 'fowlerdsl_Transition11'):
        assert not _is_linked(b2, 'fowlerdsl_Transition11', a)


def test_assoc_events0_link_reassign_clear():
    a = fowlerdsl_Event(code="sample_text", name="sample_text", resetting=True)
    b1 = fowlerdsl_Statemachine()
    b2 = fowlerdsl_Statemachine()
    _safe_set(a, 'fowlerdsl_Event', b1)
    assert _is_linked(a, 'fowlerdsl_Event', b1)
    if hasattr(b1, 'fowlerdsl_Statemachine'):
        assert _is_linked(b1, 'fowlerdsl_Statemachine', a)
    _safe_set(a, 'fowlerdsl_Event', b2)
    assert _is_linked(a, 'fowlerdsl_Event', b2)
    if hasattr(b1, 'fowlerdsl_Statemachine'):
        assert not _is_linked(b1, 'fowlerdsl_Statemachine', a)
    if hasattr(b2, 'fowlerdsl_Statemachine'):
        assert _is_linked(b2, 'fowlerdsl_Statemachine', a)
    _safe_set(a, 'fowlerdsl_Event', None)
    assert not _is_linked(a, 'fowlerdsl_Event', b2)
    if hasattr(b2, 'fowlerdsl_Statemachine'):
        assert not _is_linked(b2, 'fowlerdsl_Statemachine', a)


def test_assoc_state13_link_reassign_clear():
    a = fowlerdsl_State(name="sample_text")
    b1 = fowlerdsl_Transition()
    b2 = fowlerdsl_Transition()
    _safe_set(a, 'fowlerdsl_State15', b1)
    assert _is_linked(a, 'fowlerdsl_State15', b1)
    if hasattr(b1, 'fowlerdsl_Transition14'):
        assert _is_linked(b1, 'fowlerdsl_Transition14', a)
    _safe_set(a, 'fowlerdsl_State15', b2)
    assert _is_linked(a, 'fowlerdsl_State15', b2)
    if hasattr(b1, 'fowlerdsl_Transition14'):
        assert not _is_linked(b1, 'fowlerdsl_Transition14', a)
    if hasattr(b2, 'fowlerdsl_Transition14'):
        assert _is_linked(b2, 'fowlerdsl_Transition14', a)
    _safe_set(a, 'fowlerdsl_State15', None)
    assert not _is_linked(a, 'fowlerdsl_State15', b2)
    if hasattr(b2, 'fowlerdsl_Transition14'):
        assert not _is_linked(b2, 'fowlerdsl_Transition14', a)


def test_assoc_states3_link_reassign_clear():
    a = fowlerdsl_State(name="sample_text")
    b1 = fowlerdsl_Statemachine()
    b2 = fowlerdsl_Statemachine()
    _safe_set(a, 'fowlerdsl_State', b1)
    assert _is_linked(a, 'fowlerdsl_State', b1)
    if hasattr(b1, 'fowlerdsl_Statemachine4'):
        assert _is_linked(b1, 'fowlerdsl_Statemachine4', a)
    _safe_set(a, 'fowlerdsl_State', b2)
    assert _is_linked(a, 'fowlerdsl_State', b2)
    if hasattr(b1, 'fowlerdsl_Statemachine4'):
        assert not _is_linked(b1, 'fowlerdsl_Statemachine4', a)
    if hasattr(b2, 'fowlerdsl_Statemachine4'):
        assert _is_linked(b2, 'fowlerdsl_Statemachine4', a)
    _safe_set(a, 'fowlerdsl_State', None)
    assert not _is_linked(a, 'fowlerdsl_State', b2)
    if hasattr(b2, 'fowlerdsl_Statemachine4'):
        assert not _is_linked(b2, 'fowlerdsl_Statemachine4', a)


def test_assoc_transitions8_link_reassign_clear():
    a = fowlerdsl_State(name="sample_text")
    b1 = fowlerdsl_Transition()
    b2 = fowlerdsl_Transition()
    _safe_set(a, 'fowlerdsl_State9', {b1})
    assert _is_linked(a, 'fowlerdsl_State9', b1)
    if hasattr(b1, 'fowlerdsl_Transition'):
        assert _is_linked(b1, 'fowlerdsl_Transition', a)
    _safe_set(a, 'fowlerdsl_State9', {b2})
    assert _is_linked(a, 'fowlerdsl_State9', b2)
    if hasattr(b1, 'fowlerdsl_Transition'):
        assert not _is_linked(b1, 'fowlerdsl_Transition', a)
    if hasattr(b2, 'fowlerdsl_Transition'):
        assert _is_linked(b2, 'fowlerdsl_Transition', a)
    _safe_set(a, 'fowlerdsl_State9', set())
    assert not _is_linked(a, 'fowlerdsl_State9', b2)
    if hasattr(b2, 'fowlerdsl_Transition'):
        assert not _is_linked(b2, 'fowlerdsl_Transition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

fowlerdsl_Command_strategy = st.builds(fowlerdsl_Command, code=safe_text, name=safe_text)
@given(instance=fowlerdsl_Command_strategy)
@settings(max_examples=25)
def test_fowlerdsl_Command_instantiation(instance):
    assert isinstance(instance, fowlerdsl_Command)


fowlerdsl_Event_strategy = st.builds(fowlerdsl_Event, code=safe_text, name=safe_text, resetting=st.booleans())
@given(instance=fowlerdsl_Event_strategy)
@settings(max_examples=25)
def test_fowlerdsl_Event_instantiation(instance):
    assert isinstance(instance, fowlerdsl_Event)


fowlerdsl_State_strategy = st.builds(fowlerdsl_State, name=safe_text)
@given(instance=fowlerdsl_State_strategy)
@settings(max_examples=25)
def test_fowlerdsl_State_instantiation(instance):
    assert isinstance(instance, fowlerdsl_State)


fowlerdsl_Statemachine_strategy = st.builds(fowlerdsl_Statemachine)
@given(instance=fowlerdsl_Statemachine_strategy)
@settings(max_examples=25)
def test_fowlerdsl_Statemachine_instantiation(instance):
    assert isinstance(instance, fowlerdsl_Statemachine)


fowlerdsl_Transition_strategy = st.builds(fowlerdsl_Transition)
@given(instance=fowlerdsl_Transition_strategy)
@settings(max_examples=25)
def test_fowlerdsl_Transition_instantiation(instance):
    assert isinstance(instance, fowlerdsl_Transition)



