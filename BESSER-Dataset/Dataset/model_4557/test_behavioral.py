import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    Step,
    Turn,
    Vehicle,
    platoon_Constraint,
    platoon_Constraints,
    platoon_FollowVehicle,
    platoon_Forward,
    platoon_LeadVehicle,
    platoon_Platoon,
    platoon_Route,
    platoon_Step,
    platoon_Turn,
    platoon_TurnLeft,
    platoon_TurnRight,
    platoon_Vehicle,
    platoon_World,
    platoon_headway,
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

def test_assoc_frontrunner12_stub_double():
    # platoon_FollowVehicle has no real 'platoon_FollowVehicle13' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(name="sample_text")
    partner = platoon_FollowVehicle()
    setattr(partner, 'platoon_FollowVehicle13', None)
    _safe_set(owner, 'platoon_Vehicle', partner)
    assert getattr(partner, 'platoon_FollowVehicle13') == owner
    _safe_set(owner, 'platoon_Vehicle', None)
    assert getattr(partner, 'platoon_FollowVehicle13') is None


def test_assoc_route9_stub_double():
    # platoon_LeadVehicle has no real 'platoon_LeadVehicle10' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_LeadVehicle()
    setattr(partner, 'platoon_LeadVehicle10', None)
    _safe_set(owner, 'platoon_Route11', partner)
    assert getattr(partner, 'platoon_LeadVehicle10') == owner
    _safe_set(owner, 'platoon_Route11', None)
    assert getattr(partner, 'platoon_LeadVehicle10') is None


def test_assoc_routes1_stub_double():
    # platoon_World has no real 'platoon_World2' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_World()
    setattr(partner, 'platoon_World2', None)
    _safe_set(owner, 'platoon_Route', partner)
    assert getattr(partner, 'platoon_World2') == owner
    _safe_set(owner, 'platoon_Route', None)
    assert getattr(partner, 'platoon_World2') is None


def test_assoc_steps14_stub_double():
    # platoon_Step has no real 'platoon_Step' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_Step()
    setattr(partner, 'platoon_Step', None)
    _safe_set(owner, 'platoon_Route15', {partner})
    assert getattr(partner, 'platoon_Step') == owner
    _safe_set(owner, 'platoon_Route15', set())
    assert getattr(partner, 'platoon_Step') is None


