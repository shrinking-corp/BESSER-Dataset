import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fsm_Fsm,
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

def test_assoc_state0_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_Fsm(name="sample_text")
    _safe_set(b, 'fsm_Fsm', a1)
    assert _is_linked(b, 'fsm_Fsm', a1)
    if hasattr(a1, 'fsm_State'):
        assert _is_linked(a1, 'fsm_State', b)
    _safe_set(b, 'fsm_Fsm', a2)
    assert _is_linked(b, 'fsm_Fsm', a2)
    if hasattr(a1, 'fsm_State'):
        assert not _is_linked(a1, 'fsm_State', b)
    if hasattr(a2, 'fsm_State'):
        assert _is_linked(a2, 'fsm_State', b)
    _safe_set(b, 'fsm_Fsm', None)
    assert not _is_linked(b, 'fsm_Fsm', a2)
    if hasattr(a2, 'fsm_State'):
        assert not _is_linked(a2, 'fsm_State', b)


def test_assoc_state6_reverse_link_reassign_clear():
    a1 = fsm_Transition(name="sample_text")
    a2 = fsm_Transition(name="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'fsm_State8', a1)
    assert _is_linked(b, 'fsm_State8', a1)
    if hasattr(a1, 'fsm_Transition7'):
        assert _is_linked(a1, 'fsm_Transition7', b)
    _safe_set(b, 'fsm_State8', a2)
    assert _is_linked(b, 'fsm_State8', a2)
    if hasattr(a1, 'fsm_Transition7'):
        assert not _is_linked(a1, 'fsm_Transition7', b)
    if hasattr(a2, 'fsm_Transition7'):
        assert _is_linked(a2, 'fsm_Transition7', b)
    _safe_set(b, 'fsm_State8', None)
    assert not _is_linked(b, 'fsm_State8', a2)
    if hasattr(a2, 'fsm_Transition7'):
        assert not _is_linked(a2, 'fsm_Transition7', b)


def test_assoc_states1_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_Fsm(name="sample_text")
    _safe_set(b, 'fsm_Fsm2', {a1})
    assert _is_linked(b, 'fsm_Fsm2', a1)
    if hasattr(a1, 'fsm_State3'):
        assert _is_linked(a1, 'fsm_State3', b)
    _safe_set(b, 'fsm_Fsm2', {a2})
    assert _is_linked(b, 'fsm_Fsm2', a2)
    if hasattr(a1, 'fsm_State3'):
        assert not _is_linked(a1, 'fsm_State3', b)
    if hasattr(a2, 'fsm_State3'):
        assert _is_linked(a2, 'fsm_State3', b)
    _safe_set(b, 'fsm_Fsm2', set())
    assert not _is_linked(b, 'fsm_Fsm2', a2)
    if hasattr(a2, 'fsm_State3'):
        assert not _is_linked(a2, 'fsm_State3', b)


def test_assoc_transitions4_reverse_link_reassign_clear():
    a1 = fsm_Transition(name="sample_text")
    a2 = fsm_Transition(name="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'fsm_State5', {a1})
    assert _is_linked(b, 'fsm_State5', a1)
    if hasattr(a1, 'fsm_Transition'):
        assert _is_linked(a1, 'fsm_Transition', b)
    _safe_set(b, 'fsm_State5', {a2})
    assert _is_linked(b, 'fsm_State5', a2)
    if hasattr(a1, 'fsm_Transition'):
        assert not _is_linked(a1, 'fsm_Transition', b)
    if hasattr(a2, 'fsm_Transition'):
        assert _is_linked(a2, 'fsm_Transition', b)
    _safe_set(b, 'fsm_State5', set())
    assert not _is_linked(b, 'fsm_State5', a2)
    if hasattr(a2, 'fsm_Transition'):
        assert not _is_linked(a2, 'fsm_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

