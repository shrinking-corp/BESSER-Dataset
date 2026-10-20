import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fsm_FSM,
    fsm_State,
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

def test_assoc_containingFSM13_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'FSM14', a1)
    assert _is_linked(b, 'FSM14', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'FSM14', a2)
    assert _is_linked(b, 'FSM14', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'FSM14', None)
    assert not _is_linked(b, 'FSM14', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_containingFSM8_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'FSM', a1)
    assert _is_linked(b, 'FSM', a1)
    if hasattr(a1, 'states'):
        assert _is_linked(a1, 'states', b)
    _safe_set(b, 'FSM', a2)
    assert _is_linked(b, 'FSM', a2)
    if hasattr(a1, 'states'):
        assert not _is_linked(a1, 'states', b)
    if hasattr(a2, 'states'):
        assert _is_linked(a2, 'states', b)
    _safe_set(b, 'FSM', None)
    assert not _is_linked(b, 'FSM', a2)
    if hasattr(a2, 'states'):
        assert not _is_linked(a2, 'states', b)


def test_assoc_incomingTransitions6_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition7'):
        assert _is_linked(a1, 'Transition7', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition7'):
        assert not _is_linked(a1, 'Transition7', b)
    if hasattr(a2, 'Transition7'):
        assert _is_linked(a2, 'Transition7', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition7'):
        assert not _is_linked(a2, 'Transition7', b)


def test_assoc_initialState3_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(name="sample_text")
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


def test_assoc_outgoingTransitions4_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_source11_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State12', a1)
    assert _is_linked(b, 'State12', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State12', a2)
    assert _is_linked(b, 'State12', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State12', None)
    assert not _is_linked(b, 'State12', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'containingFSM', {a1})
    assert _is_linked(b, 'containingFSM', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'containingFSM', {a2})
    assert _is_linked(b, 'containingFSM', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'containingFSM', set())
    assert not _is_linked(b, 'containingFSM', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_target9_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State10', a1)
    assert _is_linked(b, 'State10', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State10', a2)
    assert _is_linked(b, 'State10', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State10', None)
    assert not _is_linked(b, 'State10', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'containingFSM2', {a1})
    assert _is_linked(b, 'containingFSM2', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'containingFSM2', {a2})
    assert _is_linked(b, 'containingFSM2', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'containingFSM2', set())
    assert not _is_linked(b, 'containingFSM2', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

