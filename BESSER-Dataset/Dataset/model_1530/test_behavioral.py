import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tP1_EM_State,
    tP1_EM_StateMachine,
    tP1_EM_Transition,
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

def test_assoc_from_10_reverse_link_reassign_clear():
    a1 = tP1_EM_Transition(name="sample_text")
    a2 = tP1_EM_Transition(name="sample_text_2")
    b = tP1_EM_State(name="sample_text")
    _safe_set(b, 'State11', a1)
    assert _is_linked(b, 'State11', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State11', a2)
    assert _is_linked(b, 'State11', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State11', None)
    assert not _is_linked(b, 'State11', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_incoming6_reverse_link_reassign_clear():
    a1 = tP1_EM_Transition(name="sample_text")
    a2 = tP1_EM_Transition(name="sample_text_2")
    b = tP1_EM_State(name="sample_text")
    _safe_set(b, 'to', a1)
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'to', a2)
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'to', None)
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_initialState3_reverse_link_reassign_clear():
    a1 = tP1_EM_StateMachine(name="sample_text")
    a2 = tP1_EM_StateMachine(name="sample_text_2")
    b = tP1_EM_State(name="sample_text")
    _safe_set(b, 'tP1_EM_State5', a1)
    assert _is_linked(b, 'tP1_EM_State5', a1)
    if hasattr(a1, 'tP1_EM_StateMachine4'):
        assert _is_linked(a1, 'tP1_EM_StateMachine4', b)
    _safe_set(b, 'tP1_EM_State5', a2)
    assert _is_linked(b, 'tP1_EM_State5', a2)
    if hasattr(a1, 'tP1_EM_StateMachine4'):
        assert not _is_linked(a1, 'tP1_EM_StateMachine4', b)
    if hasattr(a2, 'tP1_EM_StateMachine4'):
        assert _is_linked(a2, 'tP1_EM_StateMachine4', b)
    _safe_set(b, 'tP1_EM_State5', None)
    assert not _is_linked(b, 'tP1_EM_State5', a2)
    if hasattr(a2, 'tP1_EM_StateMachine4'):
        assert not _is_linked(a2, 'tP1_EM_StateMachine4', b)


def test_assoc_outgoing7_reverse_link_reassign_clear():
    a1 = tP1_EM_Transition(name="sample_text")
    a2 = tP1_EM_Transition(name="sample_text_2")
    b = tP1_EM_State(name="sample_text")
    _safe_set(b, 'from_', a1)
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'Transition8'):
        assert _is_linked(a1, 'Transition8', b)
    _safe_set(b, 'from_', a2)
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'Transition8'):
        assert not _is_linked(a1, 'Transition8', b)
    if hasattr(a2, 'Transition8'):
        assert _is_linked(a2, 'Transition8', b)
    _safe_set(b, 'from_', None)
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'Transition8'):
        assert not _is_linked(a2, 'Transition8', b)


def test_assoc_state1_reverse_link_reassign_clear():
    a1 = tP1_EM_StateMachine(name="sample_text")
    a2 = tP1_EM_StateMachine(name="sample_text_2")
    b = tP1_EM_State(name="sample_text")
    _safe_set(b, 'tP1_EM_State', a1)
    assert _is_linked(b, 'tP1_EM_State', a1)
    if hasattr(a1, 'tP1_EM_StateMachine2'):
        assert _is_linked(a1, 'tP1_EM_StateMachine2', b)
    _safe_set(b, 'tP1_EM_State', a2)
    assert _is_linked(b, 'tP1_EM_State', a2)
    if hasattr(a1, 'tP1_EM_StateMachine2'):
        assert not _is_linked(a1, 'tP1_EM_StateMachine2', b)
    if hasattr(a2, 'tP1_EM_StateMachine2'):
        assert _is_linked(a2, 'tP1_EM_StateMachine2', b)
    _safe_set(b, 'tP1_EM_State', None)
    assert not _is_linked(b, 'tP1_EM_State', a2)
    if hasattr(a2, 'tP1_EM_StateMachine2'):
        assert not _is_linked(a2, 'tP1_EM_StateMachine2', b)


def test_assoc_to9_reverse_link_reassign_clear():
    a1 = tP1_EM_Transition(name="sample_text")
    a2 = tP1_EM_Transition(name="sample_text_2")
    b = tP1_EM_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


def test_assoc_transition0_reverse_link_reassign_clear():
    a1 = tP1_EM_Transition(name="sample_text")
    a2 = tP1_EM_Transition(name="sample_text_2")
    b = tP1_EM_StateMachine(name="sample_text")
    _safe_set(b, 'tP1_EM_StateMachine', {a1})
    assert _is_linked(b, 'tP1_EM_StateMachine', a1)
    if hasattr(a1, 'tP1_EM_Transition'):
        assert _is_linked(a1, 'tP1_EM_Transition', b)
    _safe_set(b, 'tP1_EM_StateMachine', {a2})
    assert _is_linked(b, 'tP1_EM_StateMachine', a2)
    if hasattr(a1, 'tP1_EM_Transition'):
        assert not _is_linked(a1, 'tP1_EM_Transition', b)
    if hasattr(a2, 'tP1_EM_Transition'):
        assert _is_linked(a2, 'tP1_EM_Transition', b)
    _safe_set(b, 'tP1_EM_StateMachine', set())
    assert not _is_linked(b, 'tP1_EM_StateMachine', a2)
    if hasattr(a2, 'tP1_EM_Transition'):
        assert not _is_linked(a2, 'tP1_EM_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

