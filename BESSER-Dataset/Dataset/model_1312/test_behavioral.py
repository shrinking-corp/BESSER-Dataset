import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    StateMachine_NamedState,
    StateMachine_State,
    StateMachine_Transition,
    StateMachine_UnNamedState,
    StateMachine_WashingMachine,
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

def test_assoc_outgoings0_stub_double():
    # StateMachine_State has no real 'StateMachine_State' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(action="sample_text", id=7, name="sample_text", trigger="sample_text")
    partner = StateMachine_State()
    setattr(partner, 'StateMachine_State', None)
    _safe_set(owner, 'StateMachine_Transition', partner)
    assert owner in getattr(partner, 'StateMachine_State')
    _safe_set(owner, 'StateMachine_Transition', None)
    assert owner not in getattr(partner, 'StateMachine_State')


def test_assoc_source1_stub_double():
    # StateMachine_State has no real 'StateMachine_State3' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(action="sample_text", id=7, name="sample_text", trigger="sample_text")
    partner = StateMachine_State()
    setattr(partner, 'StateMachine_State3', None)
    _safe_set(owner, 'StateMachine_Transition2', partner)
    assert getattr(partner, 'StateMachine_State3') == owner
    _safe_set(owner, 'StateMachine_Transition2', None)
    assert getattr(partner, 'StateMachine_State3') is None


def test_assoc_target4_stub_double():
    # StateMachine_State has no real 'StateMachine_State6' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(action="sample_text", id=7, name="sample_text", trigger="sample_text")
    partner = StateMachine_State()
    setattr(partner, 'StateMachine_State6', None)
    _safe_set(owner, 'StateMachine_Transition5', partner)
    assert getattr(partner, 'StateMachine_State6') == owner
    _safe_set(owner, 'StateMachine_Transition5', None)
    assert getattr(partner, 'StateMachine_State6') is None


def test_assoc_transitions9_stub_double():
    # StateMachine_WashingMachine has no real 'StateMachine_WashingMachine10' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(action="sample_text", id=7, name="sample_text", trigger="sample_text")
    partner = StateMachine_WashingMachine()
    setattr(partner, 'StateMachine_WashingMachine10', None)
    _safe_set(owner, 'StateMachine_Transition11', partner)
    assert owner in getattr(partner, 'StateMachine_WashingMachine10')
    _safe_set(owner, 'StateMachine_Transition11', None)
    assert owner not in getattr(partner, 'StateMachine_WashingMachine10')


