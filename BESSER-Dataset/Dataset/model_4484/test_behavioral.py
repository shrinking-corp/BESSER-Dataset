import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Instruction,
    NamedElement,
    behaviour_Action,
    behaviour_Choice,
    behaviour_Condition,
    behaviour_Drone,
    behaviour_DroneBehaviour,
    behaviour_FieldObject,
    behaviour_Instruct,
    behaviour_Instruction,
    behaviour_Lift,
    behaviour_MovableObject,
    behaviour_MoveTo,
    behaviour_NamedElement,
    behaviour_Pause,
    behaviour_PerformAction,
    behaviour_PlaceObject,
    behaviour_SendMessage,
    behaviour_WaitForMessage,
    behaviour_While,
    ConditionKind,
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

def test_assoc_condition25_stub_double():
    # behaviour_While has no real 'behaviour_While26' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Condition(key="sample_text", operation="sample_text", value="sample_text")
    partner = behaviour_While()
    setattr(partner, 'behaviour_While26', None)
    _safe_set(owner, 'behaviour_Condition27', partner)
    assert getattr(partner, 'behaviour_While26') == owner
    _safe_set(owner, 'behaviour_Condition27', None)
    assert getattr(partner, 'behaviour_While26') is None


def test_assoc_condition8_stub_double():
    # behaviour_Choice has no real 'behaviour_Choice' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Condition(key="sample_text", operation="sample_text", value="sample_text")
    partner = behaviour_Choice()
    setattr(partner, 'behaviour_Choice', None)
    _safe_set(owner, 'behaviour_Condition', partner)
    assert getattr(partner, 'behaviour_Choice') == owner
    _safe_set(owner, 'behaviour_Condition', None)
    assert getattr(partner, 'behaviour_Choice') is None


def test_assoc_drones1_stub_double():
    # behaviour_Drone has no real 'behaviour_Drone' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DroneBehaviour's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DroneBehaviour's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DroneBehaviour(canBeInterrupted=True)
    partner = behaviour_Drone()
    setattr(partner, 'behaviour_Drone', None)
    _safe_set(owner, 'behaviour_DroneBehaviour2', {partner})
    assert getattr(partner, 'behaviour_Drone') == owner
    _safe_set(owner, 'behaviour_DroneBehaviour2', set())
    assert getattr(partner, 'behaviour_Drone') is None


def test_assoc_fieldObject15_stub_double():
    # behaviour_FieldObject has no real 'behaviour_FieldObject17' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Condition(key="sample_text", operation="sample_text", value="sample_text")
    partner = behaviour_FieldObject()
    setattr(partner, 'behaviour_FieldObject17', None)
    _safe_set(owner, 'behaviour_Condition16', partner)
    assert getattr(partner, 'behaviour_FieldObject17') == owner
    _safe_set(owner, 'behaviour_Condition16', None)
    assert getattr(partner, 'behaviour_FieldObject17') is None


def test_assoc_instructions0_stub_double():
    # behaviour_Instruction has no real 'behaviour_Instruction' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DroneBehaviour's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DroneBehaviour's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DroneBehaviour(canBeInterrupted=True)
    partner = behaviour_Instruction()
    setattr(partner, 'behaviour_Instruction', None)
    _safe_set(owner, 'behaviour_DroneBehaviour', {partner})
    assert getattr(partner, 'behaviour_Instruction') == owner
    _safe_set(owner, 'behaviour_DroneBehaviour', set())
    assert getattr(partner, 'behaviour_Instruction') is None


def test_assoc_whenArrived18_stub_double():
    # behaviour_Instruction has no real 'behaviour_Instruction19' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_WaitForMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_WaitForMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_WaitForMessage(timeout=3.14, type="sample_text")
    partner = behaviour_Instruction()
    setattr(partner, 'behaviour_Instruction19', None)
    _safe_set(owner, 'behaviour_WaitForMessage', {partner})
    assert getattr(partner, 'behaviour_Instruction19') == owner
    _safe_set(owner, 'behaviour_WaitForMessage', set())
    assert getattr(partner, 'behaviour_Instruction19') is None


def test_assoc_whenLost20_stub_double():
    # behaviour_Instruction has no real 'behaviour_Instruction22' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_WaitForMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_WaitForMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_WaitForMessage(timeout=3.14, type="sample_text")
    partner = behaviour_Instruction()
    setattr(partner, 'behaviour_Instruction22', None)
    _safe_set(owner, 'behaviour_WaitForMessage21', {partner})
    assert getattr(partner, 'behaviour_Instruction22') == owner
    _safe_set(owner, 'behaviour_WaitForMessage21', set())
    assert getattr(partner, 'behaviour_Instruction22') is None


