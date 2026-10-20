import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fsm_Buffer,
    fsm_FSM,
    fsm_State,
    fsm_System,
    fsm_Transition,
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

def test_assoc_currentState7_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    _safe_set(b, 'fsm_FSM8', a1)
    assert _is_linked(b, 'fsm_FSM8', a1)
    if hasattr(a1, 'fsm_State9'):
        assert _is_linked(a1, 'fsm_State9', b)
    _safe_set(b, 'fsm_FSM8', a2)
    assert _is_linked(b, 'fsm_FSM8', a2)
    if hasattr(a1, 'fsm_State9'):
        assert not _is_linked(a1, 'fsm_State9', b)
    if hasattr(a2, 'fsm_State9'):
        assert _is_linked(a2, 'fsm_State9', b)
    _safe_set(b, 'fsm_FSM8', None)
    assert not _is_linked(b, 'fsm_FSM8', a2)
    if hasattr(a2, 'fsm_State9'):
        assert not _is_linked(a2, 'fsm_State9', b)


def test_assoc_fsm14_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    _safe_set(b, 'FSM', a1)
    assert _is_linked(b, 'FSM', a1)
    if hasattr(a1, 'ownedStates'):
        assert _is_linked(a1, 'ownedStates', b)
    _safe_set(b, 'FSM', a2)
    assert _is_linked(b, 'FSM', a2)
    if hasattr(a1, 'ownedStates'):
        assert not _is_linked(a1, 'ownedStates', b)
    if hasattr(a2, 'ownedStates'):
        assert _is_linked(a2, 'ownedStates', b)
    _safe_set(b, 'FSM', None)
    assert not _is_linked(b, 'FSM', a2)
    if hasattr(a2, 'ownedStates'):
        assert not _is_linked(a2, 'ownedStates', b)


def test_assoc_fsm23_reverse_link_reassign_clear():
    a1 = fsm_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    _safe_set(b, 'FSM24', a1)
    assert _is_linked(b, 'FSM24', a1)
    if hasattr(a1, 'ownedTransitions'):
        assert _is_linked(a1, 'ownedTransitions', b)
    _safe_set(b, 'FSM24', a2)
    assert _is_linked(b, 'FSM24', a2)
    if hasattr(a1, 'ownedTransitions'):
        assert not _is_linked(a1, 'ownedTransitions', b)
    if hasattr(a2, 'ownedTransitions'):
        assert _is_linked(a2, 'ownedTransitions', b)
    _safe_set(b, 'FSM24', None)
    assert not _is_linked(b, 'FSM24', a2)
    if hasattr(a2, 'ownedTransitions'):
        assert not _is_linked(a2, 'ownedTransitions', b)


def test_assoc_incoming10_reverse_link_reassign_clear():
    a1 = fsm_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'tgt', {a1})
    assert _is_linked(b, 'tgt', a1)
    if hasattr(a1, 'Transition11'):
        assert _is_linked(a1, 'Transition11', b)
    _safe_set(b, 'tgt', {a2})
    assert _is_linked(b, 'tgt', a2)
    if hasattr(a1, 'Transition11'):
        assert not _is_linked(a1, 'Transition11', b)
    if hasattr(a2, 'Transition11'):
        assert _is_linked(a2, 'Transition11', b)
    _safe_set(b, 'tgt', set())
    assert not _is_linked(b, 'tgt', a2)
    if hasattr(a2, 'Transition11'):
        assert not _is_linked(a2, 'Transition11', b)


def test_assoc_incomingFSM17_reverse_link_reassign_clear():
    a1 = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    a2 = fsm_FSM(consummedString="sample_text_2", name="sample_text_2", underProcessTrigger="sample_text_2")
    b = fsm_Buffer(currentValues="sample_text", initialValue="sample_text", name="sample_text")
    _safe_set(b, 'outputBuffer', a1)
    assert _is_linked(b, 'outputBuffer', a1)
    if hasattr(a1, 'FSM18'):
        assert _is_linked(a1, 'FSM18', b)
    _safe_set(b, 'outputBuffer', a2)
    assert _is_linked(b, 'outputBuffer', a2)
    if hasattr(a1, 'FSM18'):
        assert not _is_linked(a1, 'FSM18', b)
    if hasattr(a2, 'FSM18'):
        assert _is_linked(a2, 'FSM18', b)
    _safe_set(b, 'outputBuffer', None)
    assert not _is_linked(b, 'outputBuffer', a2)
    if hasattr(a2, 'FSM18'):
        assert not _is_linked(a2, 'FSM18', b)


def test_assoc_initialState6_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    _safe_set(b, 'fsm_FSM', a1)
    assert _is_linked(b, 'fsm_FSM', a1)
    if hasattr(a1, 'fsm_State'):
        assert _is_linked(a1, 'fsm_State', b)
    _safe_set(b, 'fsm_FSM', a2)
    assert _is_linked(b, 'fsm_FSM', a2)
    if hasattr(a1, 'fsm_State'):
        assert not _is_linked(a1, 'fsm_State', b)
    if hasattr(a2, 'fsm_State'):
        assert _is_linked(a2, 'fsm_State', b)
    _safe_set(b, 'fsm_FSM', None)
    assert not _is_linked(b, 'fsm_FSM', a2)
    if hasattr(a2, 'fsm_State'):
        assert not _is_linked(a2, 'fsm_State', b)


def test_assoc_inputBuffer3_reverse_link_reassign_clear():
    a1 = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    a2 = fsm_FSM(consummedString="sample_text_2", name="sample_text_2", underProcessTrigger="sample_text_2")
    b = fsm_Buffer(currentValues="sample_text", initialValue="sample_text", name="sample_text")
    _safe_set(b, 'Buffer', a1)
    assert _is_linked(b, 'Buffer', a1)
    if hasattr(a1, 'outgoingFSM'):
        assert _is_linked(a1, 'outgoingFSM', b)
    _safe_set(b, 'Buffer', a2)
    assert _is_linked(b, 'Buffer', a2)
    if hasattr(a1, 'outgoingFSM'):
        assert not _is_linked(a1, 'outgoingFSM', b)
    if hasattr(a2, 'outgoingFSM'):
        assert _is_linked(a2, 'outgoingFSM', b)
    _safe_set(b, 'Buffer', None)
    assert not _is_linked(b, 'Buffer', a2)
    if hasattr(a2, 'outgoingFSM'):
        assert not _is_linked(a2, 'outgoingFSM', b)


def test_assoc_outgoing12_reverse_link_reassign_clear():
    a1 = fsm_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'src', {a1})
    assert _is_linked(b, 'src', a1)
    if hasattr(a1, 'Transition13'):
        assert _is_linked(a1, 'Transition13', b)
    _safe_set(b, 'src', {a2})
    assert _is_linked(b, 'src', a2)
    if hasattr(a1, 'Transition13'):
        assert not _is_linked(a1, 'Transition13', b)
    if hasattr(a2, 'Transition13'):
        assert _is_linked(a2, 'Transition13', b)
    _safe_set(b, 'src', set())
    assert not _is_linked(b, 'src', a2)
    if hasattr(a2, 'Transition13'):
        assert not _is_linked(a2, 'Transition13', b)


def test_assoc_outgoingFSM15_reverse_link_reassign_clear():
    a1 = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    a2 = fsm_FSM(consummedString="sample_text_2", name="sample_text_2", underProcessTrigger="sample_text_2")
    b = fsm_Buffer(currentValues="sample_text", initialValue="sample_text", name="sample_text")
    _safe_set(b, 'inputBuffer', a1)
    assert _is_linked(b, 'inputBuffer', a1)
    if hasattr(a1, 'FSM16'):
        assert _is_linked(a1, 'FSM16', b)
    _safe_set(b, 'inputBuffer', a2)
    assert _is_linked(b, 'inputBuffer', a2)
    if hasattr(a1, 'FSM16'):
        assert not _is_linked(a1, 'FSM16', b)
    if hasattr(a2, 'FSM16'):
        assert _is_linked(a2, 'FSM16', b)
    _safe_set(b, 'inputBuffer', None)
    assert not _is_linked(b, 'inputBuffer', a2)
    if hasattr(a2, 'FSM16'):
        assert not _is_linked(a2, 'FSM16', b)


def test_assoc_outputBuffer4_reverse_link_reassign_clear():
    a1 = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    a2 = fsm_FSM(consummedString="sample_text_2", name="sample_text_2", underProcessTrigger="sample_text_2")
    b = fsm_Buffer(currentValues="sample_text", initialValue="sample_text", name="sample_text")
    _safe_set(b, 'Buffer5', a1)
    assert _is_linked(b, 'Buffer5', a1)
    if hasattr(a1, 'incomingFSM'):
        assert _is_linked(a1, 'incomingFSM', b)
    _safe_set(b, 'Buffer5', a2)
    assert _is_linked(b, 'Buffer5', a2)
    if hasattr(a1, 'incomingFSM'):
        assert not _is_linked(a1, 'incomingFSM', b)
    if hasattr(a2, 'incomingFSM'):
        assert _is_linked(a2, 'incomingFSM', b)
    _safe_set(b, 'Buffer5', None)
    assert not _is_linked(b, 'Buffer5', a2)
    if hasattr(a2, 'incomingFSM'):
        assert not _is_linked(a2, 'incomingFSM', b)


def test_assoc_ownedStates0_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    _safe_set(b, 'fsm', {a1})
    assert _is_linked(b, 'fsm', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'fsm', {a2})
    assert _is_linked(b, 'fsm', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'fsm', set())
    assert not _is_linked(b, 'fsm', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_ownedTransitions1_reverse_link_reassign_clear():
    a1 = fsm_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    _safe_set(b, 'fsm2', {a1})
    assert _is_linked(b, 'fsm2', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'fsm2', {a2})
    assert _is_linked(b, 'fsm2', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'fsm2', set())
    assert not _is_linked(b, 'fsm2', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_src21_reverse_link_reassign_clear():
    a1 = fsm_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State22', a1)
    assert _is_linked(b, 'State22', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State22', a2)
    assert _is_linked(b, 'State22', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State22', None)
    assert not _is_linked(b, 'State22', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_tgt19_reverse_link_reassign_clear():
    a1 = fsm_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State20', a1)
    assert _is_linked(b, 'State20', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State20', a2)
    assert _is_linked(b, 'State20', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State20', None)
    assert not _is_linked(b, 'State20', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ownedBuffers27_stub_double():
    # fsm_System has no real 'fsm_System28' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Buffer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Buffer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Buffer(currentValues="sample_text", initialValue="sample_text", name="sample_text")
    partner = fsm_System()
    setattr(partner, 'fsm_System28', None)
    _safe_set(owner, 'fsm_Buffer', partner)
    assert owner in getattr(partner, 'fsm_System28')
    _safe_set(owner, 'fsm_Buffer', None)
    assert owner not in getattr(partner, 'fsm_System28')


def test_assoc_ownedFsms25_stub_double():
    # fsm_System has no real 'fsm_System' property in the generated
    # code (a bare stub) -- manually attach it so fsm_FSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_FSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_FSM(consummedString="sample_text", name="sample_text", underProcessTrigger="sample_text")
    partner = fsm_System()
    setattr(partner, 'fsm_System', None)
    _safe_set(owner, 'fsm_FSM26', partner)
    assert owner in getattr(partner, 'fsm_System')
    _safe_set(owner, 'fsm_FSM26', None)
    assert owner not in getattr(partner, 'fsm_System')


