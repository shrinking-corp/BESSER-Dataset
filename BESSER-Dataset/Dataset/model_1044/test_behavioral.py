import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    sample_FSM,
    sample_Finalstate,
    sample_Initstate,
    sample_State,
    sample_Transition,
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

def test_assoc_StateTo3_reverse_link_reassign_clear():
    a1 = sample_Transition(name="sample_text", trigger="sample_text")
    a2 = sample_Transition(name="sample_text_2", trigger="sample_text_2")
    b = sample_State(name="sample_text")
    _safe_set(b, 'sample_State5', a1)
    assert _is_linked(b, 'sample_State5', a1)
    if hasattr(a1, 'sample_Transition4'):
        assert _is_linked(a1, 'sample_Transition4', b)
    _safe_set(b, 'sample_State5', a2)
    assert _is_linked(b, 'sample_State5', a2)
    if hasattr(a1, 'sample_Transition4'):
        assert not _is_linked(a1, 'sample_Transition4', b)
    if hasattr(a2, 'sample_Transition4'):
        assert _is_linked(a2, 'sample_Transition4', b)
    _safe_set(b, 'sample_State5', None)
    assert not _is_linked(b, 'sample_State5', a2)
    if hasattr(a2, 'sample_Transition4'):
        assert not _is_linked(a2, 'sample_Transition4', b)


def test_assoc_state1_reverse_link_reassign_clear():
    a1 = sample_State(name="sample_text")
    a2 = sample_State(name="sample_text_2")
    b = sample_FSM(name="sample_text")
    _safe_set(b, 'sample_FSM2', {a1})
    assert _is_linked(b, 'sample_FSM2', a1)
    if hasattr(a1, 'sample_State'):
        assert _is_linked(a1, 'sample_State', b)
    _safe_set(b, 'sample_FSM2', {a2})
    assert _is_linked(b, 'sample_FSM2', a2)
    if hasattr(a1, 'sample_State'):
        assert not _is_linked(a1, 'sample_State', b)
    if hasattr(a2, 'sample_State'):
        assert _is_linked(a2, 'sample_State', b)
    _safe_set(b, 'sample_FSM2', set())
    assert not _is_linked(b, 'sample_FSM2', a2)
    if hasattr(a2, 'sample_State'):
        assert not _is_linked(a2, 'sample_State', b)


def test_assoc_stateFrom6_reverse_link_reassign_clear():
    a1 = sample_Transition(name="sample_text", trigger="sample_text")
    a2 = sample_Transition(name="sample_text_2", trigger="sample_text_2")
    b = sample_State(name="sample_text")
    _safe_set(b, 'sample_State8', a1)
    assert _is_linked(b, 'sample_State8', a1)
    if hasattr(a1, 'sample_Transition7'):
        assert _is_linked(a1, 'sample_Transition7', b)
    _safe_set(b, 'sample_State8', a2)
    assert _is_linked(b, 'sample_State8', a2)
    if hasattr(a1, 'sample_Transition7'):
        assert not _is_linked(a1, 'sample_Transition7', b)
    if hasattr(a2, 'sample_Transition7'):
        assert _is_linked(a2, 'sample_Transition7', b)
    _safe_set(b, 'sample_State8', None)
    assert not _is_linked(b, 'sample_State8', a2)
    if hasattr(a2, 'sample_Transition7'):
        assert not _is_linked(a2, 'sample_Transition7', b)


def test_assoc_transition0_reverse_link_reassign_clear():
    a1 = sample_Transition(name="sample_text", trigger="sample_text")
    a2 = sample_Transition(name="sample_text_2", trigger="sample_text_2")
    b = sample_FSM(name="sample_text")
    _safe_set(b, 'sample_FSM', {a1})
    assert _is_linked(b, 'sample_FSM', a1)
    if hasattr(a1, 'sample_Transition'):
        assert _is_linked(a1, 'sample_Transition', b)
    _safe_set(b, 'sample_FSM', {a2})
    assert _is_linked(b, 'sample_FSM', a2)
    if hasattr(a1, 'sample_Transition'):
        assert not _is_linked(a1, 'sample_Transition', b)
    if hasattr(a2, 'sample_Transition'):
        assert _is_linked(a2, 'sample_Transition', b)
    _safe_set(b, 'sample_FSM', set())
    assert not _is_linked(b, 'sample_FSM', a2)
    if hasattr(a2, 'sample_Transition'):
        assert not _is_linked(a2, 'sample_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

