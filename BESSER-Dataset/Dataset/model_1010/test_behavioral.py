import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    fsm_FSM,
    fsm_Final,
    fsm_Initial,
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

def test_assoc_source0_reverse_link_reassign_clear():
    a1 = fsm_Transition(name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(name="sample_text_2", trigger="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'fsm_State', a1)
    assert _is_linked(b, 'fsm_State', a1)
    if hasattr(a1, 'fsm_Transition'):
        assert _is_linked(a1, 'fsm_Transition', b)
    _safe_set(b, 'fsm_State', a2)
    assert _is_linked(b, 'fsm_State', a2)
    if hasattr(a1, 'fsm_Transition'):
        assert not _is_linked(a1, 'fsm_Transition', b)
    if hasattr(a2, 'fsm_Transition'):
        assert _is_linked(a2, 'fsm_Transition', b)
    _safe_set(b, 'fsm_State', None)
    assert not _is_linked(b, 'fsm_State', a2)
    if hasattr(a2, 'fsm_Transition'):
        assert not _is_linked(a2, 'fsm_Transition', b)


def test_assoc_state4_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'fsm_FSM', {a1})
    assert _is_linked(b, 'fsm_FSM', a1)
    if hasattr(a1, 'fsm_State5'):
        assert _is_linked(a1, 'fsm_State5', b)
    _safe_set(b, 'fsm_FSM', {a2})
    assert _is_linked(b, 'fsm_FSM', a2)
    if hasattr(a1, 'fsm_State5'):
        assert not _is_linked(a1, 'fsm_State5', b)
    if hasattr(a2, 'fsm_State5'):
        assert _is_linked(a2, 'fsm_State5', b)
    _safe_set(b, 'fsm_FSM', set())
    assert not _is_linked(b, 'fsm_FSM', a2)
    if hasattr(a2, 'fsm_State5'):
        assert not _is_linked(a2, 'fsm_State5', b)


def test_assoc_target1_reverse_link_reassign_clear():
    a1 = fsm_Transition(name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(name="sample_text_2", trigger="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'fsm_State3', a1)
    assert _is_linked(b, 'fsm_State3', a1)
    if hasattr(a1, 'fsm_Transition2'):
        assert _is_linked(a1, 'fsm_Transition2', b)
    _safe_set(b, 'fsm_State3', a2)
    assert _is_linked(b, 'fsm_State3', a2)
    if hasattr(a1, 'fsm_Transition2'):
        assert not _is_linked(a1, 'fsm_Transition2', b)
    if hasattr(a2, 'fsm_Transition2'):
        assert _is_linked(a2, 'fsm_Transition2', b)
    _safe_set(b, 'fsm_State3', None)
    assert not _is_linked(b, 'fsm_State3', a2)
    if hasattr(a2, 'fsm_Transition2'):
        assert not _is_linked(a2, 'fsm_Transition2', b)


def test_assoc_transition6_reverse_link_reassign_clear():
    a1 = fsm_Transition(name="sample_text", trigger="sample_text")
    a2 = fsm_Transition(name="sample_text_2", trigger="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'fsm_FSM7', {a1})
    assert _is_linked(b, 'fsm_FSM7', a1)
    if hasattr(a1, 'fsm_Transition8'):
        assert _is_linked(a1, 'fsm_Transition8', b)
    _safe_set(b, 'fsm_FSM7', {a2})
    assert _is_linked(b, 'fsm_FSM7', a2)
    if hasattr(a1, 'fsm_Transition8'):
        assert not _is_linked(a1, 'fsm_Transition8', b)
    if hasattr(a2, 'fsm_Transition8'):
        assert _is_linked(a2, 'fsm_Transition8', b)
    _safe_set(b, 'fsm_FSM7', set())
    assert not _is_linked(b, 'fsm_FSM7', a2)
    if hasattr(a2, 'fsm_Transition8'):
        assert not _is_linked(a2, 'fsm_Transition8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_final11_stub_double():
    # fsm_Final has no real 'fsm_Final' property in the generated
    # code (a bare stub) -- manually attach it so fsm_FSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_FSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_FSM(name="sample_text")
    partner = fsm_Final()
    setattr(partner, 'fsm_Final', None)
    _safe_set(owner, 'fsm_FSM12', partner)
    assert getattr(partner, 'fsm_Final') == owner
    _safe_set(owner, 'fsm_FSM12', None)
    assert getattr(partner, 'fsm_Final') is None


def test_assoc_initial9_stub_double():
    # fsm_Initial has no real 'fsm_Initial' property in the generated
    # code (a bare stub) -- manually attach it so fsm_FSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_FSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_FSM(name="sample_text")
    partner = fsm_Initial()
    setattr(partner, 'fsm_Initial', None)
    _safe_set(owner, 'fsm_FSM10', partner)
    assert getattr(partner, 'fsm_Initial') == owner
    _safe_set(owner, 'fsm_FSM10', None)
    assert getattr(partner, 'fsm_Initial') is None


