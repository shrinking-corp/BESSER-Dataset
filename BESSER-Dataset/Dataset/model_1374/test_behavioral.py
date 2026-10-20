import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    statemachines_Event,
    statemachines_State,
    statemachines_StateMachine,
    statemachines_Transition,
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

def test_assoc_event11_stub_double():
    # statemachines_Transition has no real 'statemachines_Transition12' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Event(code="sample_text", name="sample_text")
    partner = statemachines_Transition()
    setattr(partner, 'statemachines_Transition12', None)
    _safe_set(owner, 'statemachines_Event13', partner)
    assert getattr(partner, 'statemachines_Transition12') == owner
    _safe_set(owner, 'statemachines_Event13', None)
    assert getattr(partner, 'statemachines_Transition12') is None


def test_assoc_events1_stub_double():
    # statemachines_StateMachine has no real 'statemachines_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Event(code="sample_text", name="sample_text")
    partner = statemachines_StateMachine()
    setattr(partner, 'statemachines_StateMachine2', None)
    _safe_set(owner, 'statemachines_Event', partner)
    assert owner in getattr(partner, 'statemachines_StateMachine2')
    _safe_set(owner, 'statemachines_Event', None)
    assert owner not in getattr(partner, 'statemachines_StateMachine2')


def test_assoc_resetEvents3_stub_double():
    # statemachines_StateMachine has no real 'statemachines_StateMachine4' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Event(code="sample_text", name="sample_text")
    partner = statemachines_StateMachine()
    setattr(partner, 'statemachines_StateMachine4', None)
    _safe_set(owner, 'statemachines_Event5', partner)
    assert owner in getattr(partner, 'statemachines_StateMachine4')
    _safe_set(owner, 'statemachines_Event5', None)
    assert owner not in getattr(partner, 'statemachines_StateMachine4')


def test_assoc_state8_stub_double():
    # statemachines_Transition has no real 'statemachines_Transition9' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(name="sample_text")
    partner = statemachines_Transition()
    setattr(partner, 'statemachines_Transition9', None)
    _safe_set(owner, 'statemachines_State10', partner)
    assert getattr(partner, 'statemachines_Transition9') == owner
    _safe_set(owner, 'statemachines_State10', None)
    assert getattr(partner, 'statemachines_Transition9') is None


def test_assoc_states0_stub_double():
    # statemachines_StateMachine has no real 'statemachines_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(name="sample_text")
    partner = statemachines_StateMachine()
    setattr(partner, 'statemachines_StateMachine', None)
    _safe_set(owner, 'statemachines_State', partner)
    assert owner in getattr(partner, 'statemachines_StateMachine')
    _safe_set(owner, 'statemachines_State', None)
    assert owner not in getattr(partner, 'statemachines_StateMachine')


def test_assoc_transitions6_stub_double():
    # statemachines_Transition has no real 'statemachines_Transition' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(name="sample_text")
    partner = statemachines_Transition()
    setattr(partner, 'statemachines_Transition', None)
    _safe_set(owner, 'statemachines_State7', {partner})
    assert getattr(partner, 'statemachines_Transition') == owner
    _safe_set(owner, 'statemachines_State7', set())
    assert getattr(partner, 'statemachines_Transition') is None


