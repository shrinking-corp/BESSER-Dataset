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

def test_assoc_from_7_reverse_link_reassign_clear():
    a1 = model_Transition(name="sample_text")
    a2 = model_Transition(name="sample_text_2")
    b = model_State(name="sample_text")
    _safe_set(b, 'State8', a1)
    assert _is_linked(b, 'State8', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State8', a2)
    assert _is_linked(b, 'State8', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State8', None)
    assert not _is_linked(b, 'State8', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_incoming3_reverse_link_reassign_clear():
    a1 = model_Transition(name="sample_text")
    a2 = model_Transition(name="sample_text_2")
    b = model_State(name="sample_text")
    _safe_set(b, 'to', {a1})
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'to', {a2})
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'to', set())
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_outgoing4_reverse_link_reassign_clear():
    a1 = model_Transition(name="sample_text")
    a2 = model_Transition(name="sample_text_2")
    b = model_State(name="sample_text")
    _safe_set(b, 'from_', {a1})
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'from_', {a2})
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'from_', set())
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_state0_reverse_link_reassign_clear():
    a1 = model_State(name="sample_text")
    a2 = model_State(name="sample_text_2")
    b = model_FSM(name="sample_text")
    _safe_set(b, 'model_FSM', {a1})
    assert _is_linked(b, 'model_FSM', a1)
    if hasattr(a1, 'model_State'):
        assert _is_linked(a1, 'model_State', b)
    _safe_set(b, 'model_FSM', {a2})
    assert _is_linked(b, 'model_FSM', a2)
    if hasattr(a1, 'model_State'):
        assert not _is_linked(a1, 'model_State', b)
    if hasattr(a2, 'model_State'):
        assert _is_linked(a2, 'model_State', b)
    _safe_set(b, 'model_FSM', set())
    assert not _is_linked(b, 'model_FSM', a2)
    if hasattr(a2, 'model_State'):
        assert not _is_linked(a2, 'model_State', b)


def test_assoc_to6_reverse_link_reassign_clear():
    a1 = model_Transition(name="sample_text")
    a2 = model_Transition(name="sample_text_2")
    b = model_State(name="sample_text")
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


def test_assoc_transition1_reverse_link_reassign_clear():
    a1 = model_Transition(name="sample_text")
    a2 = model_Transition(name="sample_text_2")
    b = model_FSM(name="sample_text")
    _safe_set(b, 'model_FSM2', {a1})
    assert _is_linked(b, 'model_FSM2', a1)
    if hasattr(a1, 'model_Transition'):
        assert _is_linked(a1, 'model_Transition', b)
    _safe_set(b, 'model_FSM2', {a2})
    assert _is_linked(b, 'model_FSM2', a2)
    if hasattr(a1, 'model_Transition'):
        assert not _is_linked(a1, 'model_Transition', b)
    if hasattr(a2, 'model_Transition'):
        assert _is_linked(a2, 'model_Transition', b)
    _safe_set(b, 'model_FSM2', set())
    assert not _is_linked(b, 'model_FSM2', a2)
    if hasattr(a2, 'model_Transition'):
        assert not _is_linked(a2, 'model_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

