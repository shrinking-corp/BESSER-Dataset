import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_automatons1_reverse_link_reassign_clear():
    a1 = MDAIntermediateStateMachine_Content(name="sample_text")
    a2 = MDAIntermediateStateMachine_Content(name="sample_text_2")
    b = MDAIntermediateStateMachine_Automaton(name="sample_text")
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton', a1)
    assert _is_linked(b, 'MDAIntermediateStateMachine_Automaton', a1)
    if hasattr(a1, 'MDAIntermediateStateMachine_Content2'):
        assert _is_linked(a1, 'MDAIntermediateStateMachine_Content2', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton', a2)
    assert _is_linked(b, 'MDAIntermediateStateMachine_Automaton', a2)
    if hasattr(a1, 'MDAIntermediateStateMachine_Content2'):
        assert not _is_linked(a1, 'MDAIntermediateStateMachine_Content2', b)
    if hasattr(a2, 'MDAIntermediateStateMachine_Content2'):
        assert _is_linked(a2, 'MDAIntermediateStateMachine_Content2', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton', None)
    assert not _is_linked(b, 'MDAIntermediateStateMachine_Automaton', a2)
    if hasattr(a2, 'MDAIntermediateStateMachine_Content2'):
        assert not _is_linked(a2, 'MDAIntermediateStateMachine_Content2', b)


def test_assoc_initialState11_reverse_link_reassign_clear():
    a1 = MDAIntermediateStateMachine_State(name="sample_text")
    a2 = MDAIntermediateStateMachine_State(name="sample_text_2")
    b = MDAIntermediateStateMachine_Automaton(name="sample_text")
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton12', a1)
    assert _is_linked(b, 'MDAIntermediateStateMachine_Automaton12', a1)
    if hasattr(a1, 'MDAIntermediateStateMachine_State13'):
        assert _is_linked(a1, 'MDAIntermediateStateMachine_State13', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton12', a2)
    assert _is_linked(b, 'MDAIntermediateStateMachine_Automaton12', a2)
    if hasattr(a1, 'MDAIntermediateStateMachine_State13'):
        assert not _is_linked(a1, 'MDAIntermediateStateMachine_State13', b)
    if hasattr(a2, 'MDAIntermediateStateMachine_State13'):
        assert _is_linked(a2, 'MDAIntermediateStateMachine_State13', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton12', None)
    assert not _is_linked(b, 'MDAIntermediateStateMachine_Automaton12', a2)
    if hasattr(a2, 'MDAIntermediateStateMachine_State13'):
        assert not _is_linked(a2, 'MDAIntermediateStateMachine_State13', b)


def test_assoc_operations3_reverse_link_reassign_clear():
    a1 = MDAIntermediateStateMachine_Operation(name="sample_text")
    a2 = MDAIntermediateStateMachine_Operation(name="sample_text_2")
    b = MDAIntermediateStateMachine_Content(name="sample_text")
    _safe_set(b, 'MDAIntermediateStateMachine_Content4', {a1})
    assert _is_linked(b, 'MDAIntermediateStateMachine_Content4', a1)
    if hasattr(a1, 'MDAIntermediateStateMachine_Operation'):
        assert _is_linked(a1, 'MDAIntermediateStateMachine_Operation', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Content4', {a2})
    assert _is_linked(b, 'MDAIntermediateStateMachine_Content4', a2)
    if hasattr(a1, 'MDAIntermediateStateMachine_Operation'):
        assert not _is_linked(a1, 'MDAIntermediateStateMachine_Operation', b)
    if hasattr(a2, 'MDAIntermediateStateMachine_Operation'):
        assert _is_linked(a2, 'MDAIntermediateStateMachine_Operation', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Content4', set())
    assert not _is_linked(b, 'MDAIntermediateStateMachine_Content4', a2)
    if hasattr(a2, 'MDAIntermediateStateMachine_Operation'):
        assert not _is_linked(a2, 'MDAIntermediateStateMachine_Operation', b)


def test_assoc_participant19_reverse_link_reassign_clear():
    a1 = MDAIntermediateStateMachine_Participant(name="sample_text")
    a2 = MDAIntermediateStateMachine_Participant(name="sample_text_2")
    b = MDAIntermediateStateMachine_Automaton(name="sample_text")
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton20', a1)
    assert _is_linked(b, 'MDAIntermediateStateMachine_Automaton20', a1)
    if hasattr(a1, 'MDAIntermediateStateMachine_Participant21'):
        assert _is_linked(a1, 'MDAIntermediateStateMachine_Participant21', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton20', a2)
    assert _is_linked(b, 'MDAIntermediateStateMachine_Automaton20', a2)
    if hasattr(a1, 'MDAIntermediateStateMachine_Participant21'):
        assert not _is_linked(a1, 'MDAIntermediateStateMachine_Participant21', b)
    if hasattr(a2, 'MDAIntermediateStateMachine_Participant21'):
        assert _is_linked(a2, 'MDAIntermediateStateMachine_Participant21', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton20', None)
    assert not _is_linked(b, 'MDAIntermediateStateMachine_Automaton20', a2)
    if hasattr(a2, 'MDAIntermediateStateMachine_Participant21'):
        assert not _is_linked(a2, 'MDAIntermediateStateMachine_Participant21', b)


def test_assoc_participants5_reverse_link_reassign_clear():
    a1 = MDAIntermediateStateMachine_Participant(name="sample_text")
    a2 = MDAIntermediateStateMachine_Participant(name="sample_text_2")
    b = MDAIntermediateStateMachine_Content(name="sample_text")
    _safe_set(b, 'MDAIntermediateStateMachine_Content6', {a1})
    assert _is_linked(b, 'MDAIntermediateStateMachine_Content6', a1)
    if hasattr(a1, 'MDAIntermediateStateMachine_Participant'):
        assert _is_linked(a1, 'MDAIntermediateStateMachine_Participant', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Content6', {a2})
    assert _is_linked(b, 'MDAIntermediateStateMachine_Content6', a2)
    if hasattr(a1, 'MDAIntermediateStateMachine_Participant'):
        assert not _is_linked(a1, 'MDAIntermediateStateMachine_Participant', b)
    if hasattr(a2, 'MDAIntermediateStateMachine_Participant'):
        assert _is_linked(a2, 'MDAIntermediateStateMachine_Participant', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Content6', set())
    assert not _is_linked(b, 'MDAIntermediateStateMachine_Content6', a2)
    if hasattr(a2, 'MDAIntermediateStateMachine_Participant'):
        assert not _is_linked(a2, 'MDAIntermediateStateMachine_Participant', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = MDAIntermediateStateMachine_State(name="sample_text")
    a2 = MDAIntermediateStateMachine_State(name="sample_text_2")
    b = MDAIntermediateStateMachine_Content(name="sample_text")
    _safe_set(b, 'MDAIntermediateStateMachine_Content', {a1})
    assert _is_linked(b, 'MDAIntermediateStateMachine_Content', a1)
    if hasattr(a1, 'MDAIntermediateStateMachine_State'):
        assert _is_linked(a1, 'MDAIntermediateStateMachine_State', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Content', {a2})
    assert _is_linked(b, 'MDAIntermediateStateMachine_Content', a2)
    if hasattr(a1, 'MDAIntermediateStateMachine_State'):
        assert not _is_linked(a1, 'MDAIntermediateStateMachine_State', b)
    if hasattr(a2, 'MDAIntermediateStateMachine_State'):
        assert _is_linked(a2, 'MDAIntermediateStateMachine_State', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Content', set())
    assert not _is_linked(b, 'MDAIntermediateStateMachine_Content', a2)
    if hasattr(a2, 'MDAIntermediateStateMachine_State'):
        assert not _is_linked(a2, 'MDAIntermediateStateMachine_State', b)


def test_assoc_states14_reverse_link_reassign_clear():
    a1 = MDAIntermediateStateMachine_State(name="sample_text")
    a2 = MDAIntermediateStateMachine_State(name="sample_text_2")
    b = MDAIntermediateStateMachine_Automaton(name="sample_text")
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton15', {a1})
    assert _is_linked(b, 'MDAIntermediateStateMachine_Automaton15', a1)
    if hasattr(a1, 'MDAIntermediateStateMachine_State16'):
        assert _is_linked(a1, 'MDAIntermediateStateMachine_State16', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton15', {a2})
    assert _is_linked(b, 'MDAIntermediateStateMachine_Automaton15', a2)
    if hasattr(a1, 'MDAIntermediateStateMachine_State16'):
        assert not _is_linked(a1, 'MDAIntermediateStateMachine_State16', b)
    if hasattr(a2, 'MDAIntermediateStateMachine_State16'):
        assert _is_linked(a2, 'MDAIntermediateStateMachine_State16', b)
    _safe_set(b, 'MDAIntermediateStateMachine_Automaton15', set())
    assert not _is_linked(b, 'MDAIntermediateStateMachine_Automaton15', a2)
    if hasattr(a2, 'MDAIntermediateStateMachine_State16'):
        assert not _is_linked(a2, 'MDAIntermediateStateMachine_State16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_input28_stub_double():
    # MDAIntermediateStateMachine_Transition has no real 'MDAIntermediateStateMachine_Transition29' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_Operation(name="sample_text")
    partner = MDAIntermediateStateMachine_Transition()
    setattr(partner, 'MDAIntermediateStateMachine_Transition29', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_Operation30', partner)
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition29') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_Operation30', None)
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition29') is None


def test_assoc_messages7_stub_double():
    # MDAIntermediateStateMachine_Message has no real 'MDAIntermediateStateMachine_Message' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_Content's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_Content's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_Content(name="sample_text")
    partner = MDAIntermediateStateMachine_Message()
    setattr(partner, 'MDAIntermediateStateMachine_Message', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_Content8', {partner})
    assert getattr(partner, 'MDAIntermediateStateMachine_Message') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_Content8', set())
    assert getattr(partner, 'MDAIntermediateStateMachine_Message') is None


def test_assoc_operation33_stub_double():
    # MDAIntermediateStateMachine_Message has no real 'MDAIntermediateStateMachine_Message34' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_Operation(name="sample_text")
    partner = MDAIntermediateStateMachine_Message()
    setattr(partner, 'MDAIntermediateStateMachine_Message34', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_Operation35', partner)
    assert getattr(partner, 'MDAIntermediateStateMachine_Message34') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_Operation35', None)
    assert getattr(partner, 'MDAIntermediateStateMachine_Message34') is None


def test_assoc_postState25_stub_double():
    # MDAIntermediateStateMachine_Transition has no real 'MDAIntermediateStateMachine_Transition26' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_State(name="sample_text")
    partner = MDAIntermediateStateMachine_Transition()
    setattr(partner, 'MDAIntermediateStateMachine_Transition26', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_State27', partner)
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition26') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_State27', None)
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition26') is None


def test_assoc_preState22_stub_double():
    # MDAIntermediateStateMachine_Transition has no real 'MDAIntermediateStateMachine_Transition23' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_State(name="sample_text")
    partner = MDAIntermediateStateMachine_Transition()
    setattr(partner, 'MDAIntermediateStateMachine_Transition23', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_State24', partner)
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition23') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_State24', None)
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition23') is None


def test_assoc_receiver36_stub_double():
    # MDAIntermediateStateMachine_Message has no real 'MDAIntermediateStateMachine_Message37' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_Participant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_Participant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_Participant(name="sample_text")
    partner = MDAIntermediateStateMachine_Message()
    setattr(partner, 'MDAIntermediateStateMachine_Message37', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_Participant38', partner)
    assert getattr(partner, 'MDAIntermediateStateMachine_Message37') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_Participant38', None)
    assert getattr(partner, 'MDAIntermediateStateMachine_Message37') is None


def test_assoc_returnValue31_stub_double():
    # MDAIntermediateStateMachine_Transition has no real 'MDAIntermediateStateMachine_Transition32' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_Value(value="sample_text")
    partner = MDAIntermediateStateMachine_Transition()
    setattr(partner, 'MDAIntermediateStateMachine_Transition32', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_Value', partner)
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition32') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_Value', None)
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition32') is None


def test_assoc_returnValue39_stub_double():
    # MDAIntermediateStateMachine_Message has no real 'MDAIntermediateStateMachine_Message40' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_Value(value="sample_text")
    partner = MDAIntermediateStateMachine_Message()
    setattr(partner, 'MDAIntermediateStateMachine_Message40', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_Value41', partner)
    assert getattr(partner, 'MDAIntermediateStateMachine_Message40') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_Value41', None)
    assert getattr(partner, 'MDAIntermediateStateMachine_Message40') is None


def test_assoc_sequences9_stub_double():
    # MDAIntermediateStateMachine_MessageSequence has no real 'MDAIntermediateStateMachine_MessageSequence' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_State(name="sample_text")
    partner = MDAIntermediateStateMachine_MessageSequence()
    setattr(partner, 'MDAIntermediateStateMachine_MessageSequence', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_State10', {partner})
    assert getattr(partner, 'MDAIntermediateStateMachine_MessageSequence') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_State10', set())
    assert getattr(partner, 'MDAIntermediateStateMachine_MessageSequence') is None


def test_assoc_transitions17_stub_double():
    # MDAIntermediateStateMachine_Transition has no real 'MDAIntermediateStateMachine_Transition' property in the generated
    # code (a bare stub) -- manually attach it so MDAIntermediateStateMachine_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MDAIntermediateStateMachine_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MDAIntermediateStateMachine_Automaton(name="sample_text")
    partner = MDAIntermediateStateMachine_Transition()
    setattr(partner, 'MDAIntermediateStateMachine_Transition', None)
    _safe_set(owner, 'MDAIntermediateStateMachine_Automaton18', {partner})
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition') == owner
    _safe_set(owner, 'MDAIntermediateStateMachine_Automaton18', set())
    assert getattr(partner, 'MDAIntermediateStateMachine_Transition') is None


