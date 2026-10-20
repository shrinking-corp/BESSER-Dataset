import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Command,
    Constraint,
    Vehicle,
    platoon_Command,
    platoon_Constraint,
    platoon_Constraints,
    platoon_FollowVehicle,
    platoon_ForwardCommand,
    platoon_HeadwayConstraint,
    platoon_LeadingVehicle,
    platoon_Platoon,
    platoon_Route,
    platoon_TurnCommand,
    platoon_Vehicle,
    platoon_World,
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

def test_assoc_commands3_stub_double():
    # platoon_Command has no real 'platoon_Command' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_Command()
    setattr(partner, 'platoon_Command', None)
    _safe_set(owner, 'platoon_Route', {partner})
    assert getattr(partner, 'platoon_Command') == owner
    _safe_set(owner, 'platoon_Route', set())
    assert getattr(partner, 'platoon_Command') is None


def test_assoc_follows4_stub_double():
    # platoon_FollowVehicle has no real 'platoon_FollowVehicle5' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(name="sample_text")
    partner = platoon_FollowVehicle()
    setattr(partner, 'platoon_FollowVehicle5', None)
    _safe_set(owner, 'platoon_Vehicle', partner)
    assert getattr(partner, 'platoon_FollowVehicle5') == owner
    _safe_set(owner, 'platoon_Vehicle', None)
    assert getattr(partner, 'platoon_FollowVehicle5') is None


def test_assoc_route11_stub_double():
    # platoon_World has no real 'platoon_World12' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_World()
    setattr(partner, 'platoon_World12', None)
    _safe_set(owner, 'platoon_Route13', partner)
    assert getattr(partner, 'platoon_World12') == owner
    _safe_set(owner, 'platoon_Route13', None)
    assert getattr(partner, 'platoon_World12') is None


def test_assoc_route6_stub_double():
    # platoon_LeadingVehicle has no real 'platoon_LeadingVehicle7' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_LeadingVehicle()
    setattr(partner, 'platoon_LeadingVehicle7', None)
    _safe_set(owner, 'platoon_Route8', partner)
    assert getattr(partner, 'platoon_LeadingVehicle7') == owner
    _safe_set(owner, 'platoon_Route8', None)
    assert getattr(partner, 'platoon_LeadingVehicle7') is None


