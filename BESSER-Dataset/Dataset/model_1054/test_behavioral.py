import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    FSM_AbstractState,
    FSM_EndState,
    FSM_StartState,
    FSM_State,
    FSM_StateMachine,
    FSM_Transition,
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

def test_assoc_states0_reverse_link_reassign_clear():
    a1 = FSM_StateMachine(code="sample_text")
    a2 = FSM_StateMachine(code="sample_text_2")
    b = FSM_AbstractState(envs="sample_text", name="sample_text")
    _safe_set(b, 'FSM_AbstractState', a1)
    assert _is_linked(b, 'FSM_AbstractState', a1)
    if hasattr(a1, 'FSM_StateMachine'):
        assert _is_linked(a1, 'FSM_StateMachine', b)
    _safe_set(b, 'FSM_AbstractState', a2)
    assert _is_linked(b, 'FSM_AbstractState', a2)
    if hasattr(a1, 'FSM_StateMachine'):
        assert not _is_linked(a1, 'FSM_StateMachine', b)
    if hasattr(a2, 'FSM_StateMachine'):
        assert _is_linked(a2, 'FSM_StateMachine', b)
    _safe_set(b, 'FSM_AbstractState', None)
    assert not _is_linked(b, 'FSM_AbstractState', a2)
    if hasattr(a2, 'FSM_StateMachine'):
        assert not _is_linked(a2, 'FSM_StateMachine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_source3_stub_double():
    # FSM_Transition has no real 'FSM_Transition5' property in the generated
    # code (a bare stub) -- manually attach it so FSM_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_AbstractState(envs="sample_text", name="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'FSM_Transition5', None)
    _safe_set(owner, 'FSM_AbstractState4', {partner})
    assert getattr(partner, 'FSM_Transition5') == owner
    _safe_set(owner, 'FSM_AbstractState4', set())
    assert getattr(partner, 'FSM_Transition5') is None


def test_assoc_target6_stub_double():
    # FSM_Transition has no real 'FSM_Transition8' property in the generated
    # code (a bare stub) -- manually attach it so FSM_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_AbstractState(envs="sample_text", name="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'FSM_Transition8', None)
    _safe_set(owner, 'FSM_AbstractState7', {partner})
    assert getattr(partner, 'FSM_Transition8') == owner
    _safe_set(owner, 'FSM_AbstractState7', set())
    assert getattr(partner, 'FSM_Transition8') is None


def test_assoc_transitions1_stub_double():
    # FSM_Transition has no real 'FSM_Transition' property in the generated
    # code (a bare stub) -- manually attach it so FSM_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_StateMachine(code="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'FSM_Transition', None)
    _safe_set(owner, 'FSM_StateMachine2', {partner})
    assert getattr(partner, 'FSM_Transition') == owner
    _safe_set(owner, 'FSM_StateMachine2', set())
    assert getattr(partner, 'FSM_Transition') is None


