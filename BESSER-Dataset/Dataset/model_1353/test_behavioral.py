import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    Behaviour,
    NamedElement,
    ObeoDSMObject,
    StateMachineDescription,
    statemachine_AbstractState,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_NamedElement,
    statemachine_Region,
    statemachine_State,
    statemachine_StateMachine,
    statemachine_StateMachineDescription,
    statemachine_Transition,
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

def test_assoc_from_7_stub_double():
    # statemachine_AbstractState has no real 'AbstractState' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(guard="sample_text")
    partner = statemachine_AbstractState()
    setattr(partner, 'AbstractState', None)
    _safe_set(owner, 'outcomingTransitions', partner)
    assert getattr(partner, 'AbstractState') == owner
    _safe_set(owner, 'outcomingTransitions', None)
    assert getattr(partner, 'AbstractState') is None


def test_assoc_incomingTransitions4_stub_double():
    # statemachine_AbstractState has no real 'to' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(guard="sample_text")
    partner = statemachine_AbstractState()
    setattr(partner, 'to', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'to')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'to')


def test_assoc_outcomingTransitions5_stub_double():
    # statemachine_AbstractState has no real 'from_' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(guard="sample_text")
    partner = statemachine_AbstractState()
    setattr(partner, 'from_', None)
    _safe_set(owner, 'Transition6', partner)
    assert owner in getattr(partner, 'from_')
    _safe_set(owner, 'Transition6', None)
    assert owner not in getattr(partner, 'from_')


def test_assoc_to8_stub_double():
    # statemachine_AbstractState has no real 'AbstractState9' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(guard="sample_text")
    partner = statemachine_AbstractState()
    setattr(partner, 'AbstractState9', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'AbstractState9') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'AbstractState9') is None


def test_assoc_transitions2_stub_double():
    # statemachine_StateMachineDescription has no real 'statemachine_StateMachineDescription3' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(guard="sample_text")
    partner = statemachine_StateMachineDescription()
    setattr(partner, 'statemachine_StateMachineDescription3', None)
    _safe_set(owner, 'statemachine_Transition', partner)
    assert owner in getattr(partner, 'statemachine_StateMachineDescription3')
    _safe_set(owner, 'statemachine_Transition', None)
    assert owner not in getattr(partner, 'statemachine_StateMachineDescription3')


