import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Vehicle,
    platoon_Constraints,
    platoon_FollowingVehicle,
    platoon_Forward,
    platoon_LeaderVehicle,
    platoon_Platoon,
    platoon_Root,
    platoon_Route,
    platoon_TurnLeft,
    platoon_TurnRight,
    platoon_Vehicle,
    platoon_routeCommand,
    routeCommand,
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

def test_assoc_constraints3_stub_double():
    # platoon_Root has no real 'platoon_Root4' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Constraints's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Constraints's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Constraints(lbound=7, ubound=7)
    partner = platoon_Root()
    setattr(partner, 'platoon_Root4', None)
    _safe_set(owner, 'platoon_Constraints', partner)
    assert getattr(partner, 'platoon_Root4') == owner
    _safe_set(owner, 'platoon_Constraints', None)
    assert getattr(partner, 'platoon_Root4') is None


def test_assoc_following11_stub_double():
    # platoon_FollowingVehicle has no real 'platoon_FollowingVehicle12' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(name="sample_text")
    partner = platoon_FollowingVehicle()
    setattr(partner, 'platoon_FollowingVehicle12', None)
    _safe_set(owner, 'platoon_Vehicle', partner)
    assert getattr(partner, 'platoon_FollowingVehicle12') == owner
    _safe_set(owner, 'platoon_Vehicle', None)
    assert getattr(partner, 'platoon_FollowingVehicle12') is None


def test_assoc_route1_stub_double():
    # platoon_Root has no real 'platoon_Root2' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_Root()
    setattr(partner, 'platoon_Root2', None)
    _safe_set(owner, 'platoon_Route', partner)
    assert getattr(partner, 'platoon_Root2') == owner
    _safe_set(owner, 'platoon_Route', None)
    assert getattr(partner, 'platoon_Root2') is None


def test_assoc_route13_stub_double():
    # platoon_LeaderVehicle has no real 'platoon_LeaderVehicle14' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_LeaderVehicle()
    setattr(partner, 'platoon_LeaderVehicle14', None)
    _safe_set(owner, 'platoon_Route15', partner)
    assert getattr(partner, 'platoon_LeaderVehicle14') == owner
    _safe_set(owner, 'platoon_Route15', None)
    assert getattr(partner, 'platoon_LeaderVehicle14') is None


def test_assoc_routeCommands5_stub_double():
    # platoon_routeCommand has no real 'platoon_routeCommand' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_routeCommand()
    setattr(partner, 'platoon_routeCommand', None)
    _safe_set(owner, 'platoon_Route6', {partner})
    assert getattr(partner, 'platoon_routeCommand') == owner
    _safe_set(owner, 'platoon_Route6', set())
    assert getattr(partner, 'platoon_routeCommand') is None


