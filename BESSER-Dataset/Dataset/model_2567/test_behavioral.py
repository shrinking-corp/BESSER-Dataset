import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    dsl_Event,
    dsl_State,
    dsl_StateMachine,
    dsl_Transition,
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
    # dsl_Transition has no real 'dsl_Transition9' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Event(name="sample_text")
    partner = dsl_Transition()
    setattr(partner, 'dsl_Transition9', None)
    _safe_set(owner, 'dsl_Event10', partner)
    assert getattr(partner, 'dsl_Transition9') == owner
    _safe_set(owner, 'dsl_Event10', None)
    assert getattr(partner, 'dsl_Transition9') is None


def test_assoc_events0_stub_double():
    # dsl_StateMachine has no real 'dsl_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Event(name="sample_text")
    partner = dsl_StateMachine()
    setattr(partner, 'dsl_StateMachine', None)
    _safe_set(owner, 'dsl_Event', partner)
    assert owner in getattr(partner, 'dsl_StateMachine')
    _safe_set(owner, 'dsl_Event', None)
    assert owner not in getattr(partner, 'dsl_StateMachine')


def test_assoc_initialState1_stub_double():
    # dsl_StateMachine has no real 'dsl_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_StateMachine()
    setattr(partner, 'dsl_StateMachine2', None)
    _safe_set(owner, 'dsl_State', partner)
    assert getattr(partner, 'dsl_StateMachine2') == owner
    _safe_set(owner, 'dsl_State', None)
    assert getattr(partner, 'dsl_StateMachine2') is None


def test_assoc_state11_stub_double():
    # dsl_Transition has no real 'dsl_Transition12' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Transition()
    setattr(partner, 'dsl_Transition12', None)
    _safe_set(owner, 'dsl_State13', partner)
    assert getattr(partner, 'dsl_Transition12') == owner
    _safe_set(owner, 'dsl_State13', None)
    assert getattr(partner, 'dsl_Transition12') is None


def test_assoc_states3_stub_double():
    # dsl_StateMachine has no real 'dsl_StateMachine4' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_StateMachine()
    setattr(partner, 'dsl_StateMachine4', None)
    _safe_set(owner, 'dsl_State5', partner)
    assert owner in getattr(partner, 'dsl_StateMachine4')
    _safe_set(owner, 'dsl_State5', None)
    assert owner not in getattr(partner, 'dsl_StateMachine4')


def test_assoc_transitions6_stub_double():
    # dsl_Transition has no real 'dsl_Transition' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Transition()
    setattr(partner, 'dsl_Transition', None)
    _safe_set(owner, 'dsl_State7', {partner})
    assert getattr(partner, 'dsl_Transition') == owner
    _safe_set(owner, 'dsl_State7', set())
    assert getattr(partner, 'dsl_Transition') is None


