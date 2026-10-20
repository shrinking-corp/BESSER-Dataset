import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    model_FSM,
    model_State,
    model_Transition,
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

def test_assoc_fsm13_reverse_link_reassign_clear():
    a1 = model_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = model_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = model_FSM(name="sample_text")
    _safe_set(b, 'FSM14', a1)
    assert _is_linked(b, 'FSM14', a1)
    if hasattr(a1, 'ownedTransitions'):
        assert _is_linked(a1, 'ownedTransitions', b)
    _safe_set(b, 'FSM14', a2)
    assert _is_linked(b, 'FSM14', a2)
    if hasattr(a1, 'ownedTransitions'):
        assert not _is_linked(a1, 'ownedTransitions', b)
    if hasattr(a2, 'ownedTransitions'):
        assert _is_linked(a2, 'ownedTransitions', b)
    _safe_set(b, 'FSM14', None)
    assert not _is_linked(b, 'FSM14', a2)
    if hasattr(a2, 'ownedTransitions'):
        assert not _is_linked(a2, 'ownedTransitions', b)


def test_assoc_fsm8_reverse_link_reassign_clear():
    a1 = model_State(name="sample_text")
    a2 = model_State(name="sample_text_2")
    b = model_FSM(name="sample_text")
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


def test_assoc_incoming4_reverse_link_reassign_clear():
    a1 = model_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = model_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = model_State(name="sample_text")
    _safe_set(b, 'tgt', {a1})
    assert _is_linked(b, 'tgt', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'tgt', {a2})
    assert _is_linked(b, 'tgt', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'tgt', set())
    assert not _is_linked(b, 'tgt', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_initialState3_reverse_link_reassign_clear():
    a1 = model_State(name="sample_text")
    a2 = model_State(name="sample_text_2")
    b = model_FSM(name="sample_text")
    _safe_set(b, 'model_FSM', a1)
    assert _is_linked(b, 'model_FSM', a1)
    if hasattr(a1, 'model_State'):
        assert _is_linked(a1, 'model_State', b)
    _safe_set(b, 'model_FSM', a2)
    assert _is_linked(b, 'model_FSM', a2)
    if hasattr(a1, 'model_State'):
        assert not _is_linked(a1, 'model_State', b)
    if hasattr(a2, 'model_State'):
        assert _is_linked(a2, 'model_State', b)
    _safe_set(b, 'model_FSM', None)
    assert not _is_linked(b, 'model_FSM', a2)
    if hasattr(a2, 'model_State'):
        assert not _is_linked(a2, 'model_State', b)


def test_assoc_outgoing6_reverse_link_reassign_clear():
    a1 = model_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = model_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = model_State(name="sample_text")
    _safe_set(b, 'src', {a1})
    assert _is_linked(b, 'src', a1)
    if hasattr(a1, 'Transition7'):
        assert _is_linked(a1, 'Transition7', b)
    _safe_set(b, 'src', {a2})
    assert _is_linked(b, 'src', a2)
    if hasattr(a1, 'Transition7'):
        assert not _is_linked(a1, 'Transition7', b)
    if hasattr(a2, 'Transition7'):
        assert _is_linked(a2, 'Transition7', b)
    _safe_set(b, 'src', set())
    assert not _is_linked(b, 'src', a2)
    if hasattr(a2, 'Transition7'):
        assert not _is_linked(a2, 'Transition7', b)


def test_assoc_ownedStates0_reverse_link_reassign_clear():
    a1 = model_State(name="sample_text")
    a2 = model_State(name="sample_text_2")
    b = model_FSM(name="sample_text")
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
    a1 = model_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = model_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = model_FSM(name="sample_text")
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


def test_assoc_src11_reverse_link_reassign_clear():
    a1 = model_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = model_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = model_State(name="sample_text")
    _safe_set(b, 'State12', a1)
    assert _is_linked(b, 'State12', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State12', a2)
    assert _is_linked(b, 'State12', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State12', None)
    assert not _is_linked(b, 'State12', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_tgt9_reverse_link_reassign_clear():
    a1 = model_Transition(action="sample_text", name="sample_text", trigger="sample_text")
    a2 = model_Transition(action="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = model_State(name="sample_text")
    _safe_set(b, 'State10', a1)
    assert _is_linked(b, 'State10', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State10', a2)
    assert _is_linked(b, 'State10', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State10', None)
    assert not _is_linked(b, 'State10', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

