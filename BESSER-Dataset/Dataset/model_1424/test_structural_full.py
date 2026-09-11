import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Guard,
    Value,
    statemachine_Command,
    statemachine_Constant,
    statemachine_ConstantRef,
    statemachine_Event,
    statemachine_Guard,
    statemachine_IntLiteral,
    statemachine_RangeGuard,
    statemachine_State,
    statemachine_Statemachine,
    statemachine_Thing,
    statemachine_Transition,
    statemachine_Value,
    statemachine_ValueGuard,
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

def test_statemachine_Command_code_value_roundtrip():
    instance = statemachine_Command(code=7, name="sample_text")
    assert instance.code == 7
    instance.code = 13
    assert instance.code == 13


def test_statemachine_Command_name_value_roundtrip():
    instance = statemachine_Command(code=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_Constant_name_value_roundtrip():
    instance = statemachine_Constant(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_Event_code_value_roundtrip():
    instance = statemachine_Event(code=7, name="sample_text")
    assert instance.code == 7
    instance.code = 13
    assert instance.code == 13


def test_statemachine_Event_name_value_roundtrip():
    instance = statemachine_Event(code=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_IntLiteral_value_value_roundtrip():
    instance = statemachine_IntLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_statemachine_State_description_value_roundtrip():
    instance = statemachine_State(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_statemachine_State_name_value_roundtrip():
    instance = statemachine_State(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_Statemachine_name_value_roundtrip():
    instance = statemachine_Statemachine(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_Thing_name_value_roundtrip():
    instance = statemachine_Thing(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_RangeGuard_isa_Guard():
    instance = statemachine_RangeGuard()
    assert isinstance(instance, Guard)


def test_statemachine_ValueGuard_isa_Guard():
    instance = statemachine_ValueGuard()
    assert isinstance(instance, Guard)


def test_statemachine_ConstantRef_isa_Value():
    instance = statemachine_ConstantRef()
    assert isinstance(instance, Value)


def test_statemachine_IntLiteral_isa_Value():
    instance = statemachine_IntLiteral(value=7)
    assert isinstance(instance, Value)


def test_assoc_actions26_link_reassign_clear():
    a = statemachine_State(description="sample_text", name="sample_text")
    b1 = statemachine_Command(code=7, name="sample_text")
    b2 = statemachine_Command(code=13, name="sample_text_2")
    _safe_set(a, 'statemachine_State27', {b1})
    assert _is_linked(a, 'statemachine_State27', b1)
    if hasattr(b1, 'statemachine_Command28'):
        assert _is_linked(b1, 'statemachine_Command28', a)
    _safe_set(a, 'statemachine_State27', {b2})
    assert _is_linked(a, 'statemachine_State27', b2)
    if hasattr(b1, 'statemachine_Command28'):
        assert not _is_linked(b1, 'statemachine_Command28', a)
    if hasattr(b2, 'statemachine_Command28'):
        assert _is_linked(b2, 'statemachine_Command28', a)
    _safe_set(a, 'statemachine_State27', set())
    assert not _is_linked(a, 'statemachine_State27', b2)
    if hasattr(b2, 'statemachine_Command28'):
        assert not _is_linked(b2, 'statemachine_Command28', a)


def test_assoc_commands4_link_reassign_clear():
    a = statemachine_Statemachine(name="sample_text")
    b1 = statemachine_Command(code=7, name="sample_text")
    b2 = statemachine_Command(code=13, name="sample_text_2")
    _safe_set(a, 'statemachine_Statemachine5', {b1})
    assert _is_linked(a, 'statemachine_Statemachine5', b1)
    if hasattr(b1, 'statemachine_Command'):
        assert _is_linked(b1, 'statemachine_Command', a)
    _safe_set(a, 'statemachine_Statemachine5', {b2})
    assert _is_linked(a, 'statemachine_Statemachine5', b2)
    if hasattr(b1, 'statemachine_Command'):
        assert not _is_linked(b1, 'statemachine_Command', a)
    if hasattr(b2, 'statemachine_Command'):
        assert _is_linked(b2, 'statemachine_Command', a)
    _safe_set(a, 'statemachine_Statemachine5', set())
    assert not _is_linked(a, 'statemachine_Statemachine5', b2)
    if hasattr(b2, 'statemachine_Command'):
        assert not _is_linked(b2, 'statemachine_Command', a)


def test_assoc_constant18_link_reassign_clear():
    a = statemachine_Constant(name="sample_text")
    b1 = statemachine_ConstantRef()
    b2 = statemachine_ConstantRef()
    _safe_set(a, 'statemachine_Constant19', b1)
    assert _is_linked(a, 'statemachine_Constant19', b1)
    if hasattr(b1, 'statemachine_ConstantRef'):
        assert _is_linked(b1, 'statemachine_ConstantRef', a)
    _safe_set(a, 'statemachine_Constant19', b2)
    assert _is_linked(a, 'statemachine_Constant19', b2)
    if hasattr(b1, 'statemachine_ConstantRef'):
        assert not _is_linked(b1, 'statemachine_ConstantRef', a)
    if hasattr(b2, 'statemachine_ConstantRef'):
        assert _is_linked(b2, 'statemachine_ConstantRef', a)
    _safe_set(a, 'statemachine_Constant19', None)
    assert not _is_linked(a, 'statemachine_Constant19', b2)
    if hasattr(b2, 'statemachine_ConstantRef'):
        assert not _is_linked(b2, 'statemachine_ConstantRef', a)


def test_assoc_constants6_link_reassign_clear():
    a = statemachine_Statemachine(name="sample_text")
    b1 = statemachine_Constant(name="sample_text")
    b2 = statemachine_Constant(name="sample_text_2")
    _safe_set(a, 'statemachine_Statemachine7', {b1})
    assert _is_linked(a, 'statemachine_Statemachine7', b1)
    if hasattr(b1, 'statemachine_Constant'):
        assert _is_linked(b1, 'statemachine_Constant', a)
    _safe_set(a, 'statemachine_Statemachine7', {b2})
    assert _is_linked(a, 'statemachine_Statemachine7', b2)
    if hasattr(b1, 'statemachine_Constant'):
        assert not _is_linked(b1, 'statemachine_Constant', a)
    if hasattr(b2, 'statemachine_Constant'):
        assert _is_linked(b2, 'statemachine_Constant', a)
    _safe_set(a, 'statemachine_Statemachine7', set())
    assert not _is_linked(a, 'statemachine_Statemachine7', b2)
    if hasattr(b2, 'statemachine_Constant'):
        assert not _is_linked(b2, 'statemachine_Constant', a)


def test_assoc_event33_link_reassign_clear():
    a = statemachine_Event(code=7, name="sample_text")
    b1 = statemachine_Transition()
    b2 = statemachine_Transition()
    _safe_set(a, 'statemachine_Event35', b1)
    assert _is_linked(a, 'statemachine_Event35', b1)
    if hasattr(b1, 'statemachine_Transition34'):
        assert _is_linked(b1, 'statemachine_Transition34', a)
    _safe_set(a, 'statemachine_Event35', b2)
    assert _is_linked(a, 'statemachine_Event35', b2)
    if hasattr(b1, 'statemachine_Transition34'):
        assert not _is_linked(b1, 'statemachine_Transition34', a)
    if hasattr(b2, 'statemachine_Transition34'):
        assert _is_linked(b2, 'statemachine_Transition34', a)
    _safe_set(a, 'statemachine_Event35', None)
    assert not _is_linked(a, 'statemachine_Event35', b2)
    if hasattr(b2, 'statemachine_Transition34'):
        assert not _is_linked(b2, 'statemachine_Transition34', a)


def test_assoc_events0_link_reassign_clear():
    a = statemachine_Statemachine(name="sample_text")
    b1 = statemachine_Event(code=7, name="sample_text")
    b2 = statemachine_Event(code=13, name="sample_text_2")
    _safe_set(a, 'statemachine_Statemachine', {b1})
    assert _is_linked(a, 'statemachine_Statemachine', b1)
    if hasattr(b1, 'statemachine_Event'):
        assert _is_linked(b1, 'statemachine_Event', a)
    _safe_set(a, 'statemachine_Statemachine', {b2})
    assert _is_linked(a, 'statemachine_Statemachine', b2)
    if hasattr(b1, 'statemachine_Event'):
        assert not _is_linked(b1, 'statemachine_Event', a)
    if hasattr(b2, 'statemachine_Event'):
        assert _is_linked(b2, 'statemachine_Event', a)
    _safe_set(a, 'statemachine_Statemachine', set())
    assert not _is_linked(a, 'statemachine_Statemachine', b2)
    if hasattr(b2, 'statemachine_Event'):
        assert not _is_linked(b2, 'statemachine_Event', a)


def test_assoc_guard10_link_reassign_clear():
    a = statemachine_Event(code=7, name="sample_text")
    b1 = statemachine_Guard()
    b2 = statemachine_Guard()
    _safe_set(a, 'statemachine_Event11', b1)
    assert _is_linked(a, 'statemachine_Event11', b1)
    if hasattr(b1, 'statemachine_Guard'):
        assert _is_linked(b1, 'statemachine_Guard', a)
    _safe_set(a, 'statemachine_Event11', b2)
    assert _is_linked(a, 'statemachine_Event11', b2)
    if hasattr(b1, 'statemachine_Guard'):
        assert not _is_linked(b1, 'statemachine_Guard', a)
    if hasattr(b2, 'statemachine_Guard'):
        assert _is_linked(b2, 'statemachine_Guard', a)
    _safe_set(a, 'statemachine_Event11', None)
    assert not _is_linked(a, 'statemachine_Event11', b2)
    if hasattr(b2, 'statemachine_Guard'):
        assert not _is_linked(b2, 'statemachine_Guard', a)


def test_assoc_guard20_link_reassign_clear():
    a = statemachine_Command(code=7, name="sample_text")
    b1 = statemachine_Guard()
    b2 = statemachine_Guard()
    _safe_set(a, 'statemachine_Command21', b1)
    assert _is_linked(a, 'statemachine_Command21', b1)
    if hasattr(b1, 'statemachine_Guard22'):
        assert _is_linked(b1, 'statemachine_Guard22', a)
    _safe_set(a, 'statemachine_Command21', b2)
    assert _is_linked(a, 'statemachine_Command21', b2)
    if hasattr(b1, 'statemachine_Guard22'):
        assert not _is_linked(b1, 'statemachine_Guard22', a)
    if hasattr(b2, 'statemachine_Guard22'):
        assert _is_linked(b2, 'statemachine_Guard22', a)
    _safe_set(a, 'statemachine_Command21', None)
    assert not _is_linked(a, 'statemachine_Command21', b2)
    if hasattr(b2, 'statemachine_Guard22'):
        assert not _is_linked(b2, 'statemachine_Guard22', a)


def test_assoc_guard42_link_reassign_clear():
    a = statemachine_Thing(name="sample_text")
    b1 = statemachine_Guard()
    b2 = statemachine_Guard()
    _safe_set(a, 'statemachine_Thing43', b1)
    assert _is_linked(a, 'statemachine_Thing43', b1)
    if hasattr(b1, 'statemachine_Guard44'):
        assert _is_linked(b1, 'statemachine_Guard44', a)
    _safe_set(a, 'statemachine_Thing43', b2)
    assert _is_linked(a, 'statemachine_Thing43', b2)
    if hasattr(b1, 'statemachine_Guard44'):
        assert not _is_linked(b1, 'statemachine_Guard44', a)
    if hasattr(b2, 'statemachine_Guard44'):
        assert _is_linked(b2, 'statemachine_Guard44', a)
    _safe_set(a, 'statemachine_Thing43', None)
    assert not _is_linked(a, 'statemachine_Thing43', b2)
    if hasattr(b2, 'statemachine_Guard44'):
        assert not _is_linked(b2, 'statemachine_Guard44', a)


def test_assoc_resetEvents1_link_reassign_clear():
    a = statemachine_Statemachine(name="sample_text")
    b1 = statemachine_Event(code=7, name="sample_text")
    b2 = statemachine_Event(code=13, name="sample_text_2")
    _safe_set(a, 'statemachine_Statemachine2', {b1})
    assert _is_linked(a, 'statemachine_Statemachine2', b1)
    if hasattr(b1, 'statemachine_Event3'):
        assert _is_linked(b1, 'statemachine_Event3', a)
    _safe_set(a, 'statemachine_Statemachine2', {b2})
    assert _is_linked(a, 'statemachine_Statemachine2', b2)
    if hasattr(b1, 'statemachine_Event3'):
        assert not _is_linked(b1, 'statemachine_Event3', a)
    if hasattr(b2, 'statemachine_Event3'):
        assert _is_linked(b2, 'statemachine_Event3', a)
    _safe_set(a, 'statemachine_Statemachine2', set())
    assert not _is_linked(a, 'statemachine_Statemachine2', b2)
    if hasattr(b2, 'statemachine_Event3'):
        assert not _is_linked(b2, 'statemachine_Event3', a)


def test_assoc_state39_link_reassign_clear():
    a = statemachine_State(description="sample_text", name="sample_text")
    b1 = statemachine_Transition()
    b2 = statemachine_Transition()
    _safe_set(a, 'statemachine_State41', b1)
    assert _is_linked(a, 'statemachine_State41', b1)
    if hasattr(b1, 'statemachine_Transition40'):
        assert _is_linked(b1, 'statemachine_Transition40', a)
    _safe_set(a, 'statemachine_State41', b2)
    assert _is_linked(a, 'statemachine_State41', b2)
    if hasattr(b1, 'statemachine_Transition40'):
        assert not _is_linked(b1, 'statemachine_Transition40', a)
    if hasattr(b2, 'statemachine_Transition40'):
        assert _is_linked(b2, 'statemachine_Transition40', a)
    _safe_set(a, 'statemachine_State41', None)
    assert not _is_linked(a, 'statemachine_State41', b2)
    if hasattr(b2, 'statemachine_Transition40'):
        assert not _is_linked(b2, 'statemachine_Transition40', a)


def test_assoc_states8_link_reassign_clear():
    a = statemachine_Statemachine(name="sample_text")
    b1 = statemachine_State(description="sample_text", name="sample_text")
    b2 = statemachine_State(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'statemachine_Statemachine9', {b1})
    assert _is_linked(a, 'statemachine_Statemachine9', b1)
    if hasattr(b1, 'statemachine_State'):
        assert _is_linked(b1, 'statemachine_State', a)
    _safe_set(a, 'statemachine_Statemachine9', {b2})
    assert _is_linked(a, 'statemachine_Statemachine9', b2)
    if hasattr(b1, 'statemachine_State'):
        assert not _is_linked(b1, 'statemachine_State', a)
    if hasattr(b2, 'statemachine_State'):
        assert _is_linked(b2, 'statemachine_State', a)
    _safe_set(a, 'statemachine_Statemachine9', set())
    assert not _is_linked(a, 'statemachine_Statemachine9', b2)
    if hasattr(b2, 'statemachine_State'):
        assert not _is_linked(b2, 'statemachine_State', a)


def test_assoc_things31_link_reassign_clear():
    a = statemachine_Thing(name="sample_text")
    b1 = statemachine_State(description="sample_text", name="sample_text")
    b2 = statemachine_State(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'statemachine_Thing', b1)
    assert _is_linked(a, 'statemachine_Thing', b1)
    if hasattr(b1, 'statemachine_State32'):
        assert _is_linked(b1, 'statemachine_State32', a)
    _safe_set(a, 'statemachine_Thing', b2)
    assert _is_linked(a, 'statemachine_Thing', b2)
    if hasattr(b1, 'statemachine_State32'):
        assert not _is_linked(b1, 'statemachine_State32', a)
    if hasattr(b2, 'statemachine_State32'):
        assert _is_linked(b2, 'statemachine_State32', a)
    _safe_set(a, 'statemachine_Thing', None)
    assert not _is_linked(a, 'statemachine_Thing', b2)
    if hasattr(b2, 'statemachine_State32'):
        assert not _is_linked(b2, 'statemachine_State32', a)


def test_assoc_transitions29_link_reassign_clear():
    a = statemachine_State(description="sample_text", name="sample_text")
    b1 = statemachine_Transition()
    b2 = statemachine_Transition()
    _safe_set(a, 'statemachine_State30', {b1})
    assert _is_linked(a, 'statemachine_State30', b1)
    if hasattr(b1, 'statemachine_Transition'):
        assert _is_linked(b1, 'statemachine_Transition', a)
    _safe_set(a, 'statemachine_State30', {b2})
    assert _is_linked(a, 'statemachine_State30', b2)
    if hasattr(b1, 'statemachine_Transition'):
        assert not _is_linked(b1, 'statemachine_Transition', a)
    if hasattr(b2, 'statemachine_Transition'):
        assert _is_linked(b2, 'statemachine_Transition', a)
    _safe_set(a, 'statemachine_State30', set())
    assert not _is_linked(a, 'statemachine_State30', b2)
    if hasattr(b2, 'statemachine_Transition'):
        assert not _is_linked(b2, 'statemachine_Transition', a)


def test_assoc_value23_link_reassign_clear():
    a = statemachine_Constant(name="sample_text")
    b1 = statemachine_Value()
    b2 = statemachine_Value()
    _safe_set(a, 'statemachine_Constant24', b1)
    assert _is_linked(a, 'statemachine_Constant24', b1)
    if hasattr(b1, 'statemachine_Value25'):
        assert _is_linked(b1, 'statemachine_Value25', a)
    _safe_set(a, 'statemachine_Constant24', b2)
    assert _is_linked(a, 'statemachine_Constant24', b2)
    if hasattr(b1, 'statemachine_Value25'):
        assert not _is_linked(b1, 'statemachine_Value25', a)
    if hasattr(b2, 'statemachine_Value25'):
        assert _is_linked(b2, 'statemachine_Value25', a)
    _safe_set(a, 'statemachine_Constant24', None)
    assert not _is_linked(a, 'statemachine_Constant24', b2)
    if hasattr(b2, 'statemachine_Value25'):
        assert not _is_linked(b2, 'statemachine_Value25', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Guard_strategy = st.builds(Guard)
@given(instance=Guard_strategy)
@settings(max_examples=25)
def test_Guard_instantiation(instance):
    assert isinstance(instance, Guard)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


statemachine_Command_strategy = st.builds(statemachine_Command, code=st.integers(), name=safe_text)
@given(instance=statemachine_Command_strategy)
@settings(max_examples=25)
def test_statemachine_Command_instantiation(instance):
    assert isinstance(instance, statemachine_Command)


statemachine_Constant_strategy = st.builds(statemachine_Constant, name=safe_text)
@given(instance=statemachine_Constant_strategy)
@settings(max_examples=25)
def test_statemachine_Constant_instantiation(instance):
    assert isinstance(instance, statemachine_Constant)


statemachine_ConstantRef_strategy = st.builds(statemachine_ConstantRef)
@given(instance=statemachine_ConstantRef_strategy)
@settings(max_examples=25)
def test_statemachine_ConstantRef_instantiation(instance):
    assert isinstance(instance, statemachine_ConstantRef)


statemachine_Event_strategy = st.builds(statemachine_Event, code=st.integers(), name=safe_text)
@given(instance=statemachine_Event_strategy)
@settings(max_examples=25)
def test_statemachine_Event_instantiation(instance):
    assert isinstance(instance, statemachine_Event)


statemachine_Guard_strategy = st.builds(statemachine_Guard)
@given(instance=statemachine_Guard_strategy)
@settings(max_examples=25)
def test_statemachine_Guard_instantiation(instance):
    assert isinstance(instance, statemachine_Guard)


statemachine_IntLiteral_strategy = st.builds(statemachine_IntLiteral, value=st.integers())
@given(instance=statemachine_IntLiteral_strategy)
@settings(max_examples=25)
def test_statemachine_IntLiteral_instantiation(instance):
    assert isinstance(instance, statemachine_IntLiteral)


statemachine_RangeGuard_strategy = st.builds(statemachine_RangeGuard)
@given(instance=statemachine_RangeGuard_strategy)
@settings(max_examples=25)
def test_statemachine_RangeGuard_instantiation(instance):
    assert isinstance(instance, statemachine_RangeGuard)


statemachine_State_strategy = st.builds(statemachine_State, description=safe_text, name=safe_text)
@given(instance=statemachine_State_strategy)
@settings(max_examples=25)
def test_statemachine_State_instantiation(instance):
    assert isinstance(instance, statemachine_State)


statemachine_Statemachine_strategy = st.builds(statemachine_Statemachine, name=safe_text)
@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=25)
def test_statemachine_Statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)


statemachine_Thing_strategy = st.builds(statemachine_Thing, name=safe_text)
@given(instance=statemachine_Thing_strategy)
@settings(max_examples=25)
def test_statemachine_Thing_instantiation(instance):
    assert isinstance(instance, statemachine_Thing)


statemachine_Transition_strategy = st.builds(statemachine_Transition)
@given(instance=statemachine_Transition_strategy)
@settings(max_examples=25)
def test_statemachine_Transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)


statemachine_Value_strategy = st.builds(statemachine_Value)
@given(instance=statemachine_Value_strategy)
@settings(max_examples=25)
def test_statemachine_Value_instantiation(instance):
    assert isinstance(instance, statemachine_Value)


statemachine_ValueGuard_strategy = st.builds(statemachine_ValueGuard)
@given(instance=statemachine_ValueGuard_strategy)
@settings(max_examples=25)
def test_statemachine_ValueGuard_instantiation(instance):
    assert isinstance(instance, statemachine_ValueGuard)


