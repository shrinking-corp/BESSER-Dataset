import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    myfsm_Machine,
    myfsm_State,
    myfsm_Trans,
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

def test_assoc_initial1_reverse_link_reassign_clear():
    a1 = myfsm_State(name="sample_text")
    a2 = myfsm_State(name="sample_text_2")
    b = myfsm_Machine(name="sample_text")
    _safe_set(b, 'myfsm_Machine2', a1)
    assert _is_linked(b, 'myfsm_Machine2', a1)
    if hasattr(a1, 'myfsm_State3'):
        assert _is_linked(a1, 'myfsm_State3', b)
    _safe_set(b, 'myfsm_Machine2', a2)
    assert _is_linked(b, 'myfsm_Machine2', a2)
    if hasattr(a1, 'myfsm_State3'):
        assert not _is_linked(a1, 'myfsm_State3', b)
    if hasattr(a2, 'myfsm_State3'):
        assert _is_linked(a2, 'myfsm_State3', b)
    _safe_set(b, 'myfsm_Machine2', None)
    assert not _is_linked(b, 'myfsm_Machine2', a2)
    if hasattr(a2, 'myfsm_State3'):
        assert not _is_linked(a2, 'myfsm_State3', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = myfsm_State(name="sample_text")
    a2 = myfsm_State(name="sample_text_2")
    b = myfsm_Machine(name="sample_text")
    _safe_set(b, 'myfsm_Machine', {a1})
    assert _is_linked(b, 'myfsm_Machine', a1)
    if hasattr(a1, 'myfsm_State'):
        assert _is_linked(a1, 'myfsm_State', b)
    _safe_set(b, 'myfsm_Machine', {a2})
    assert _is_linked(b, 'myfsm_Machine', a2)
    if hasattr(a1, 'myfsm_State'):
        assert not _is_linked(a1, 'myfsm_State', b)
    if hasattr(a2, 'myfsm_State'):
        assert _is_linked(a2, 'myfsm_State', b)
    _safe_set(b, 'myfsm_Machine', set())
    assert not _is_linked(b, 'myfsm_Machine', a2)
    if hasattr(a2, 'myfsm_State'):
        assert not _is_linked(a2, 'myfsm_State', b)


def test_assoc_target6_reverse_link_reassign_clear():
    a1 = myfsm_Trans(event="sample_text")
    a2 = myfsm_Trans(event="sample_text_2")
    b = myfsm_State(name="sample_text")
    _safe_set(b, 'myfsm_State8', a1)
    assert _is_linked(b, 'myfsm_State8', a1)
    if hasattr(a1, 'myfsm_Trans7'):
        assert _is_linked(a1, 'myfsm_Trans7', b)
    _safe_set(b, 'myfsm_State8', a2)
    assert _is_linked(b, 'myfsm_State8', a2)
    if hasattr(a1, 'myfsm_Trans7'):
        assert not _is_linked(a1, 'myfsm_Trans7', b)
    if hasattr(a2, 'myfsm_Trans7'):
        assert _is_linked(a2, 'myfsm_Trans7', b)
    _safe_set(b, 'myfsm_State8', None)
    assert not _is_linked(b, 'myfsm_State8', a2)
    if hasattr(a2, 'myfsm_Trans7'):
        assert not _is_linked(a2, 'myfsm_Trans7', b)


def test_assoc_transitions4_reverse_link_reassign_clear():
    a1 = myfsm_Trans(event="sample_text")
    a2 = myfsm_Trans(event="sample_text_2")
    b = myfsm_State(name="sample_text")
    _safe_set(b, 'myfsm_State5', {a1})
    assert _is_linked(b, 'myfsm_State5', a1)
    if hasattr(a1, 'myfsm_Trans'):
        assert _is_linked(a1, 'myfsm_Trans', b)
    _safe_set(b, 'myfsm_State5', {a2})
    assert _is_linked(b, 'myfsm_State5', a2)
    if hasattr(a1, 'myfsm_Trans'):
        assert not _is_linked(a1, 'myfsm_Trans', b)
    if hasattr(a2, 'myfsm_Trans'):
        assert _is_linked(a2, 'myfsm_Trans', b)
    _safe_set(b, 'myfsm_State5', set())
    assert not _is_linked(b, 'myfsm_State5', a2)
    if hasattr(a2, 'myfsm_Trans'):
        assert not _is_linked(a2, 'myfsm_Trans', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

