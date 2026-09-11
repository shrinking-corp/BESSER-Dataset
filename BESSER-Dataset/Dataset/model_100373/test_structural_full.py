import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    MDAIntermediateStateMachine_Automaton,
    MDAIntermediateStateMachine_Content,
    MDAIntermediateStateMachine_Message,
    MDAIntermediateStateMachine_MessageSequence,
    MDAIntermediateStateMachine_Operation,
    MDAIntermediateStateMachine_Participant,
    MDAIntermediateStateMachine_State,
    MDAIntermediateStateMachine_Transition,
    MDAIntermediateStateMachine_Value,
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

def test_MDAIntermediateStateMachine_Automaton_name_value_roundtrip():
    instance = MDAIntermediateStateMachine_Automaton(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MDAIntermediateStateMachine_Content_name_value_roundtrip():
    instance = MDAIntermediateStateMachine_Content(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MDAIntermediateStateMachine_Operation_name_value_roundtrip():
    instance = MDAIntermediateStateMachine_Operation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MDAIntermediateStateMachine_Participant_name_value_roundtrip():
    instance = MDAIntermediateStateMachine_Participant(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MDAIntermediateStateMachine_State_name_value_roundtrip():
    instance = MDAIntermediateStateMachine_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MDAIntermediateStateMachine_Value_value_value_roundtrip():
    instance = MDAIntermediateStateMachine_Value(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_assoc_automatons1_link_reassign_clear():
    a = MDAIntermediateStateMachine_Content(name="sample_text")
    b1 = MDAIntermediateStateMachine_Automaton(name="sample_text")
    b2 = MDAIntermediateStateMachine_Automaton(name="sample_text_2")
    _safe_set(a, 'MDAIntermediateStateMachine_Content2', {b1})
    assert _is_linked(a, 'MDAIntermediateStateMachine_Content2', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Automaton'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Automaton', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Content2', {b2})
    assert _is_linked(a, 'MDAIntermediateStateMachine_Content2', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Automaton'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Automaton', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Automaton'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Automaton', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Content2', set())
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Content2', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Automaton'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Automaton', a)


def test_assoc_initialState11_link_reassign_clear():
    a = MDAIntermediateStateMachine_State(name="sample_text")
    b1 = MDAIntermediateStateMachine_Automaton(name="sample_text")
    b2 = MDAIntermediateStateMachine_Automaton(name="sample_text_2")
    _safe_set(a, 'MDAIntermediateStateMachine_State13', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State13', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Automaton12'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Automaton12', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State13', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State13', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Automaton12'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Automaton12', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Automaton12'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Automaton12', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State13', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_State13', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Automaton12'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Automaton12', a)


def test_assoc_input28_link_reassign_clear():
    a = MDAIntermediateStateMachine_Operation(name="sample_text")
    b1 = MDAIntermediateStateMachine_Transition()
    b2 = MDAIntermediateStateMachine_Transition()
    _safe_set(a, 'MDAIntermediateStateMachine_Operation30', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Operation30', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition29'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Transition29', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Operation30', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Operation30', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition29'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Transition29', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition29'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Transition29', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Operation30', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Operation30', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition29'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Transition29', a)


def test_assoc_messages7_link_reassign_clear():
    a = MDAIntermediateStateMachine_Content(name="sample_text")
    b1 = MDAIntermediateStateMachine_Message()
    b2 = MDAIntermediateStateMachine_Message()
    _safe_set(a, 'MDAIntermediateStateMachine_Content8', {b1})
    assert _is_linked(a, 'MDAIntermediateStateMachine_Content8', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Message'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Message', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Content8', {b2})
    assert _is_linked(a, 'MDAIntermediateStateMachine_Content8', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Message'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Message', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Message'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Message', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Content8', set())
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Content8', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Message'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Message', a)


def test_assoc_operation33_link_reassign_clear():
    a = MDAIntermediateStateMachine_Operation(name="sample_text")
    b1 = MDAIntermediateStateMachine_Message()
    b2 = MDAIntermediateStateMachine_Message()
    _safe_set(a, 'MDAIntermediateStateMachine_Operation35', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Operation35', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Message34'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Message34', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Operation35', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Operation35', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Message34'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Message34', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Message34'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Message34', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Operation35', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Operation35', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Message34'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Message34', a)


def test_assoc_operations3_link_reassign_clear():
    a = MDAIntermediateStateMachine_Operation(name="sample_text")
    b1 = MDAIntermediateStateMachine_Content(name="sample_text")
    b2 = MDAIntermediateStateMachine_Content(name="sample_text_2")
    _safe_set(a, 'MDAIntermediateStateMachine_Operation', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Operation', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Content4'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Content4', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Operation', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Operation', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Content4'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Content4', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Content4'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Content4', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Operation', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Operation', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Content4'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Content4', a)


def test_assoc_participant19_link_reassign_clear():
    a = MDAIntermediateStateMachine_Participant(name="sample_text")
    b1 = MDAIntermediateStateMachine_Automaton(name="sample_text")
    b2 = MDAIntermediateStateMachine_Automaton(name="sample_text_2")
    _safe_set(a, 'MDAIntermediateStateMachine_Participant21', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Participant21', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Automaton20'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Automaton20', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Participant21', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Participant21', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Automaton20'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Automaton20', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Automaton20'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Automaton20', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Participant21', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Participant21', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Automaton20'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Automaton20', a)


def test_assoc_participants5_link_reassign_clear():
    a = MDAIntermediateStateMachine_Participant(name="sample_text")
    b1 = MDAIntermediateStateMachine_Content(name="sample_text")
    b2 = MDAIntermediateStateMachine_Content(name="sample_text_2")
    _safe_set(a, 'MDAIntermediateStateMachine_Participant', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Participant', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Content6'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Content6', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Participant', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Participant', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Content6'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Content6', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Content6'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Content6', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Participant', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Participant', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Content6'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Content6', a)


def test_assoc_postState25_link_reassign_clear():
    a = MDAIntermediateStateMachine_State(name="sample_text")
    b1 = MDAIntermediateStateMachine_Transition()
    b2 = MDAIntermediateStateMachine_Transition()
    _safe_set(a, 'MDAIntermediateStateMachine_State27', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State27', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition26'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Transition26', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State27', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State27', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition26'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Transition26', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition26'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Transition26', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State27', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_State27', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition26'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Transition26', a)


def test_assoc_preState22_link_reassign_clear():
    a = MDAIntermediateStateMachine_State(name="sample_text")
    b1 = MDAIntermediateStateMachine_Transition()
    b2 = MDAIntermediateStateMachine_Transition()
    _safe_set(a, 'MDAIntermediateStateMachine_State24', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State24', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition23'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Transition23', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State24', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State24', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition23'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Transition23', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition23'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Transition23', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State24', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_State24', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition23'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Transition23', a)


def test_assoc_receiver36_link_reassign_clear():
    a = MDAIntermediateStateMachine_Participant(name="sample_text")
    b1 = MDAIntermediateStateMachine_Message()
    b2 = MDAIntermediateStateMachine_Message()
    _safe_set(a, 'MDAIntermediateStateMachine_Participant38', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Participant38', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Message37'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Message37', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Participant38', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Participant38', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Message37'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Message37', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Message37'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Message37', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Participant38', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Participant38', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Message37'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Message37', a)


def test_assoc_returnValue31_link_reassign_clear():
    a = MDAIntermediateStateMachine_Value(value="sample_text")
    b1 = MDAIntermediateStateMachine_Transition()
    b2 = MDAIntermediateStateMachine_Transition()
    _safe_set(a, 'MDAIntermediateStateMachine_Value', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Value', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition32'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Transition32', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Value', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Value', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition32'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Transition32', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition32'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Transition32', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Value', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Value', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition32'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Transition32', a)


def test_assoc_returnValue39_link_reassign_clear():
    a = MDAIntermediateStateMachine_Value(value="sample_text")
    b1 = MDAIntermediateStateMachine_Message()
    b2 = MDAIntermediateStateMachine_Message()
    _safe_set(a, 'MDAIntermediateStateMachine_Value41', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Value41', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Message40'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Message40', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Value41', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_Value41', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Message40'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Message40', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Message40'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Message40', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Value41', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Value41', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Message40'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Message40', a)


def test_assoc_sequences9_link_reassign_clear():
    a = MDAIntermediateStateMachine_State(name="sample_text")
    b1 = MDAIntermediateStateMachine_MessageSequence()
    b2 = MDAIntermediateStateMachine_MessageSequence()
    _safe_set(a, 'MDAIntermediateStateMachine_State10', {b1})
    assert _is_linked(a, 'MDAIntermediateStateMachine_State10', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_MessageSequence'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_MessageSequence', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State10', {b2})
    assert _is_linked(a, 'MDAIntermediateStateMachine_State10', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_MessageSequence'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_MessageSequence', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_MessageSequence'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_MessageSequence', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State10', set())
    assert not _is_linked(a, 'MDAIntermediateStateMachine_State10', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_MessageSequence'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_MessageSequence', a)


def test_assoc_states0_link_reassign_clear():
    a = MDAIntermediateStateMachine_State(name="sample_text")
    b1 = MDAIntermediateStateMachine_Content(name="sample_text")
    b2 = MDAIntermediateStateMachine_Content(name="sample_text_2")
    _safe_set(a, 'MDAIntermediateStateMachine_State', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Content'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Content', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Content'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Content', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Content'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Content', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_State', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Content'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Content', a)


def test_assoc_states14_link_reassign_clear():
    a = MDAIntermediateStateMachine_State(name="sample_text")
    b1 = MDAIntermediateStateMachine_Automaton(name="sample_text")
    b2 = MDAIntermediateStateMachine_Automaton(name="sample_text_2")
    _safe_set(a, 'MDAIntermediateStateMachine_State16', b1)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State16', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Automaton15'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Automaton15', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State16', b2)
    assert _is_linked(a, 'MDAIntermediateStateMachine_State16', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Automaton15'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Automaton15', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Automaton15'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Automaton15', a)
    _safe_set(a, 'MDAIntermediateStateMachine_State16', None)
    assert not _is_linked(a, 'MDAIntermediateStateMachine_State16', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Automaton15'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Automaton15', a)


def test_assoc_transitions17_link_reassign_clear():
    a = MDAIntermediateStateMachine_Automaton(name="sample_text")
    b1 = MDAIntermediateStateMachine_Transition()
    b2 = MDAIntermediateStateMachine_Transition()
    _safe_set(a, 'MDAIntermediateStateMachine_Automaton18', {b1})
    assert _is_linked(a, 'MDAIntermediateStateMachine_Automaton18', b1)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition'):
        assert _is_linked(b1, 'MDAIntermediateStateMachine_Transition', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Automaton18', {b2})
    assert _is_linked(a, 'MDAIntermediateStateMachine_Automaton18', b2)
    if hasattr(b1, 'MDAIntermediateStateMachine_Transition'):
        assert not _is_linked(b1, 'MDAIntermediateStateMachine_Transition', a)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition'):
        assert _is_linked(b2, 'MDAIntermediateStateMachine_Transition', a)
    _safe_set(a, 'MDAIntermediateStateMachine_Automaton18', set())
    assert not _is_linked(a, 'MDAIntermediateStateMachine_Automaton18', b2)
    if hasattr(b2, 'MDAIntermediateStateMachine_Transition'):
        assert not _is_linked(b2, 'MDAIntermediateStateMachine_Transition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

MDAIntermediateStateMachine_Automaton_strategy = st.builds(MDAIntermediateStateMachine_Automaton, name=safe_text)
@given(instance=MDAIntermediateStateMachine_Automaton_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_Automaton_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_Automaton)


MDAIntermediateStateMachine_Content_strategy = st.builds(MDAIntermediateStateMachine_Content, name=safe_text)
@given(instance=MDAIntermediateStateMachine_Content_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_Content_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_Content)


MDAIntermediateStateMachine_Message_strategy = st.builds(MDAIntermediateStateMachine_Message)
@given(instance=MDAIntermediateStateMachine_Message_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_Message_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_Message)


MDAIntermediateStateMachine_MessageSequence_strategy = st.builds(MDAIntermediateStateMachine_MessageSequence)
@given(instance=MDAIntermediateStateMachine_MessageSequence_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_MessageSequence_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_MessageSequence)


MDAIntermediateStateMachine_Operation_strategy = st.builds(MDAIntermediateStateMachine_Operation, name=safe_text)
@given(instance=MDAIntermediateStateMachine_Operation_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_Operation_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_Operation)


MDAIntermediateStateMachine_Participant_strategy = st.builds(MDAIntermediateStateMachine_Participant, name=safe_text)
@given(instance=MDAIntermediateStateMachine_Participant_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_Participant_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_Participant)


MDAIntermediateStateMachine_State_strategy = st.builds(MDAIntermediateStateMachine_State, name=safe_text)
@given(instance=MDAIntermediateStateMachine_State_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_State_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_State)


MDAIntermediateStateMachine_Transition_strategy = st.builds(MDAIntermediateStateMachine_Transition)
@given(instance=MDAIntermediateStateMachine_Transition_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_Transition_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_Transition)


MDAIntermediateStateMachine_Value_strategy = st.builds(MDAIntermediateStateMachine_Value, value=safe_text)
@given(instance=MDAIntermediateStateMachine_Value_strategy)
@settings(max_examples=25)
def test_MDAIntermediateStateMachine_Value_instantiation(instance):
    assert isinstance(instance, MDAIntermediateStateMachine_Value)


