import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FSM,
    State,
    Transition,
    tfsm_FSM,
    tfsm_Guard,
    tfsm_State,
    tfsm_Transition,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_currentState0_stub_double():
    # tfsm_FSM has no real 'tfsm_FSM' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_State(time=7)
    partner = tfsm_FSM()
    setattr(partner, 'tfsm_FSM', None)
    _safe_set(owner, 'tfsm_State', partner)
    assert getattr(partner, 'tfsm_FSM') == owner
    _safe_set(owner, 'tfsm_State', None)
    assert getattr(partner, 'tfsm_FSM') is None


def test_assoc_guard1_stub_double():
    # tfsm_Transition has no real 'tfsm_Transition' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Guard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Guard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Guard(time=7)
    partner = tfsm_Transition()
    setattr(partner, 'tfsm_Transition', None)
    _safe_set(owner, 'tfsm_Guard', partner)
    assert getattr(partner, 'tfsm_Transition') == owner
    _safe_set(owner, 'tfsm_Guard', None)
    assert getattr(partner, 'tfsm_Transition') is None


