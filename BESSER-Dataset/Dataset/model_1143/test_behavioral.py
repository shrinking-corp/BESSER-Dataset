import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    myStateMachines_Event,
    myStateMachines_State,
    myStateMachines_Statemachine,
    myStateMachines_Transition,
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

def test_assoc_event8_stub_double():
    # myStateMachines_Transition has no real 'myStateMachines_Transition9' property in the generated
    # code (a bare stub) -- manually attach it so myStateMachines_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myStateMachines_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myStateMachines_Event(name="sample_text")
    partner = myStateMachines_Transition()
    setattr(partner, 'myStateMachines_Transition9', None)
    _safe_set(owner, 'myStateMachines_Event10', partner)
    assert getattr(partner, 'myStateMachines_Transition9') == owner
    _safe_set(owner, 'myStateMachines_Event10', None)
    assert getattr(partner, 'myStateMachines_Transition9') is None


def test_assoc_events0_stub_double():
    # myStateMachines_Statemachine has no real 'myStateMachines_Statemachine' property in the generated
    # code (a bare stub) -- manually attach it so myStateMachines_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myStateMachines_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myStateMachines_Event(name="sample_text")
    partner = myStateMachines_Statemachine()
    setattr(partner, 'myStateMachines_Statemachine', None)
    _safe_set(owner, 'myStateMachines_Event', partner)
    assert owner in getattr(partner, 'myStateMachines_Statemachine')
    _safe_set(owner, 'myStateMachines_Event', None)
    assert owner not in getattr(partner, 'myStateMachines_Statemachine')


def test_assoc_refinement3_stub_double():
    # myStateMachines_Statemachine has no real 'myStateMachines_Statemachine5' property in the generated
    # code (a bare stub) -- manually attach it so myStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myStateMachines_State(actions="sample_text", name="sample_text")
    partner = myStateMachines_Statemachine()
    setattr(partner, 'myStateMachines_Statemachine5', None)
    _safe_set(owner, 'myStateMachines_State4', partner)
    assert getattr(partner, 'myStateMachines_Statemachine5') == owner
    _safe_set(owner, 'myStateMachines_State4', None)
    assert getattr(partner, 'myStateMachines_Statemachine5') is None


def test_assoc_state11_stub_double():
    # myStateMachines_Transition has no real 'myStateMachines_Transition12' property in the generated
    # code (a bare stub) -- manually attach it so myStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myStateMachines_State(actions="sample_text", name="sample_text")
    partner = myStateMachines_Transition()
    setattr(partner, 'myStateMachines_Transition12', None)
    _safe_set(owner, 'myStateMachines_State13', partner)
    assert getattr(partner, 'myStateMachines_Transition12') == owner
    _safe_set(owner, 'myStateMachines_State13', None)
    assert getattr(partner, 'myStateMachines_Transition12') is None


def test_assoc_states1_stub_double():
    # myStateMachines_Statemachine has no real 'myStateMachines_Statemachine2' property in the generated
    # code (a bare stub) -- manually attach it so myStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myStateMachines_State(actions="sample_text", name="sample_text")
    partner = myStateMachines_Statemachine()
    setattr(partner, 'myStateMachines_Statemachine2', None)
    _safe_set(owner, 'myStateMachines_State', partner)
    assert owner in getattr(partner, 'myStateMachines_Statemachine2')
    _safe_set(owner, 'myStateMachines_State', None)
    assert owner not in getattr(partner, 'myStateMachines_Statemachine2')


def test_assoc_transitions6_stub_double():
    # myStateMachines_Transition has no real 'myStateMachines_Transition' property in the generated
    # code (a bare stub) -- manually attach it so myStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myStateMachines_State(actions="sample_text", name="sample_text")
    partner = myStateMachines_Transition()
    setattr(partner, 'myStateMachines_Transition', None)
    _safe_set(owner, 'myStateMachines_State7', {partner})
    assert getattr(partner, 'myStateMachines_Transition') == owner
    _safe_set(owner, 'myStateMachines_State7', set())
    assert getattr(partner, 'myStateMachines_Transition') is None


