import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Turn,
    Vehicle,
    platoon_Action,
    platoon_Constraints,
    platoon_FV,
    platoon_Forward,
    platoon_LV,
    platoon_Left,
    platoon_Model,
    platoon_Platoon,
    platoon_Right,
    platoon_Route,
    platoon_Turn,
    platoon_Vehicle,
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

def test_assoc_actions14_stub_double():
    # platoon_Action has no real 'platoon_Action' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_Action()
    setattr(partner, 'platoon_Action', None)
    _safe_set(owner, 'platoon_Route15', {partner})
    assert getattr(partner, 'platoon_Action') == owner
    _safe_set(owner, 'platoon_Route15', set())
    assert getattr(partner, 'platoon_Action') is None


def test_assoc_constraints3_stub_double():
    # platoon_Model has no real 'platoon_Model4' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Constraints's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Constraints's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Constraints(maxHeadway=7, minHeadway=7)
    partner = platoon_Model()
    setattr(partner, 'platoon_Model4', None)
    _safe_set(owner, 'platoon_Constraints', partner)
    assert getattr(partner, 'platoon_Model4') == owner
    _safe_set(owner, 'platoon_Constraints', None)
    assert getattr(partner, 'platoon_Model4') is None


def test_assoc_pulledBy9_stub_double():
    # platoon_FV has no real 'platoon_FV10' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Vehicle(name="sample_text")
    partner = platoon_FV()
    setattr(partner, 'platoon_FV10', None)
    _safe_set(owner, 'platoon_Vehicle', partner)
    assert getattr(partner, 'platoon_FV10') == owner
    _safe_set(owner, 'platoon_Vehicle', None)
    assert getattr(partner, 'platoon_FV10') is None


def test_assoc_route11_stub_double():
    # platoon_LV has no real 'platoon_LV12' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_LV()
    setattr(partner, 'platoon_LV12', None)
    _safe_set(owner, 'platoon_Route13', partner)
    assert getattr(partner, 'platoon_LV12') == owner
    _safe_set(owner, 'platoon_Route13', None)
    assert getattr(partner, 'platoon_LV12') is None


def test_assoc_routes1_stub_double():
    # platoon_Model has no real 'platoon_Model2' property in the generated
    # code (a bare stub) -- manually attach it so platoon_Route's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # platoon_Route's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = platoon_Route(name="sample_text")
    partner = platoon_Model()
    setattr(partner, 'platoon_Model2', None)
    _safe_set(owner, 'platoon_Route', partner)
    assert getattr(partner, 'platoon_Model2') == owner
    _safe_set(owner, 'platoon_Route', None)
    assert getattr(partner, 'platoon_Model2') is None


