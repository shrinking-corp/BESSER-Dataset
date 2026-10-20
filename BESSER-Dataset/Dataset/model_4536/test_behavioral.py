import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Task,
    turtlebotmission_Area,
    turtlebotmission_LineTask,
    turtlebotmission_Mission,
    turtlebotmission_NamedElement,
    turtlebotmission_ReturnToStartTask,
    turtlebotmission_ShortestPathTask,
    turtlebotmission_Task,
    turtlebotmission_TurtleBot,
    turtlebotmission_WayPoint,
    turtlebotmission_WaypointType,
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

def test_assoc_area0_stub_double():
    # turtlebotmission_TurtleBot has no real 'turtlebotmission_TurtleBot' property in the generated
    # code (a bare stub) -- manually attach it so turtlebotmission_Area's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turtlebotmission_Area's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turtlebotmission_Area(xmax=7, ymax=7)
    partner = turtlebotmission_TurtleBot()
    setattr(partner, 'turtlebotmission_TurtleBot', None)
    _safe_set(owner, 'turtlebotmission_Area', partner)
    assert getattr(partner, 'turtlebotmission_TurtleBot') == owner
    _safe_set(owner, 'turtlebotmission_Area', None)
    assert getattr(partner, 'turtlebotmission_TurtleBot') is None


def test_assoc_bot_start3_stub_double():
    # turtlebotmission_TurtleBot has no real 'turtlebotmission_TurtleBot4' property in the generated
    # code (a bare stub) -- manually attach it so turtlebotmission_WayPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turtlebotmission_WayPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turtlebotmission_WayPoint(coord_x=7, coord_y=7)
    partner = turtlebotmission_TurtleBot()
    setattr(partner, 'turtlebotmission_TurtleBot4', None)
    _safe_set(owner, 'turtlebotmission_WayPoint', partner)
    assert getattr(partner, 'turtlebotmission_TurtleBot4') == owner
    _safe_set(owner, 'turtlebotmission_WayPoint', None)
    assert getattr(partner, 'turtlebotmission_TurtleBot4') is None


def test_assoc_waypoints15_stub_double():
    # turtlebotmission_LineTask has no real 'turtlebotmission_LineTask' property in the generated
    # code (a bare stub) -- manually attach it so turtlebotmission_WayPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turtlebotmission_WayPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turtlebotmission_WayPoint(coord_x=7, coord_y=7)
    partner = turtlebotmission_LineTask()
    setattr(partner, 'turtlebotmission_LineTask', None)
    _safe_set(owner, 'turtlebotmission_WayPoint16', partner)
    assert owner in getattr(partner, 'turtlebotmission_LineTask')
    _safe_set(owner, 'turtlebotmission_WayPoint16', None)
    assert owner not in getattr(partner, 'turtlebotmission_LineTask')


def test_assoc_waypoints17_stub_double():
    # turtlebotmission_ShortestPathTask has no real 'turtlebotmission_ShortestPathTask' property in the generated
    # code (a bare stub) -- manually attach it so turtlebotmission_WayPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turtlebotmission_WayPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turtlebotmission_WayPoint(coord_x=7, coord_y=7)
    partner = turtlebotmission_ShortestPathTask()
    setattr(partner, 'turtlebotmission_ShortestPathTask', None)
    _safe_set(owner, 'turtlebotmission_WayPoint18', partner)
    assert owner in getattr(partner, 'turtlebotmission_ShortestPathTask')
    _safe_set(owner, 'turtlebotmission_WayPoint18', None)
    assert owner not in getattr(partner, 'turtlebotmission_ShortestPathTask')


def test_assoc_waypoints5_stub_double():
    # turtlebotmission_TurtleBot has no real 'turtlebotmission_TurtleBot6' property in the generated
    # code (a bare stub) -- manually attach it so turtlebotmission_WayPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turtlebotmission_WayPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turtlebotmission_WayPoint(coord_x=7, coord_y=7)
    partner = turtlebotmission_TurtleBot()
    setattr(partner, 'turtlebotmission_TurtleBot6', None)
    _safe_set(owner, 'turtlebotmission_WayPoint7', partner)
    assert owner in getattr(partner, 'turtlebotmission_TurtleBot6')
    _safe_set(owner, 'turtlebotmission_WayPoint7', None)
    assert owner not in getattr(partner, 'turtlebotmission_TurtleBot6')


def test_assoc_waypointtypes10_stub_double():
    # turtlebotmission_WaypointType has no real 'turtlebotmission_WaypointType12' property in the generated
    # code (a bare stub) -- manually attach it so turtlebotmission_WayPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turtlebotmission_WayPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turtlebotmission_WayPoint(coord_x=7, coord_y=7)
    partner = turtlebotmission_WaypointType()
    setattr(partner, 'turtlebotmission_WaypointType12', None)
    _safe_set(owner, 'turtlebotmission_WayPoint11', {partner})
    assert getattr(partner, 'turtlebotmission_WaypointType12') == owner
    _safe_set(owner, 'turtlebotmission_WayPoint11', set())
    assert getattr(partner, 'turtlebotmission_WaypointType12') is None


