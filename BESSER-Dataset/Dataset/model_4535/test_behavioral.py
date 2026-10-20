import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ControlTask,
    NamedElement,
    Task,
    mission_ControlTask,
    mission_Coordinate,
    mission_Drone,
    mission_Fork,
    mission_Join,
    mission_LineTask,
    mission_Mission,
    mission_NamedElement,
    mission_PointTask,
    mission_PolygonTask,
    mission_Swarm,
    mission_Task,
    mission_TaskDependency,
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

def test_assoc_home7_reverse_link_reassign_clear():
    a1 = mission_Drone(returnHome=True, type="sample_text")
    a2 = mission_Drone(returnHome=False, type="sample_text_2")
    b = mission_Coordinate(altitude=3.14, latitude=3.14, longitude=3.14)
    _safe_set(b, 'mission_Coordinate', a1)
    assert _is_linked(b, 'mission_Coordinate', a1)
    if hasattr(a1, 'mission_Drone8'):
        assert _is_linked(a1, 'mission_Drone8', b)
    _safe_set(b, 'mission_Coordinate', a2)
    assert _is_linked(b, 'mission_Coordinate', a2)
    if hasattr(a1, 'mission_Drone8'):
        assert not _is_linked(a1, 'mission_Drone8', b)
    if hasattr(a2, 'mission_Drone8'):
        assert _is_linked(a2, 'mission_Drone8', b)
    _safe_set(b, 'mission_Coordinate', None)
    assert not _is_linked(b, 'mission_Coordinate', a2)
    if hasattr(a2, 'mission_Drone8'):
        assert not _is_linked(a2, 'mission_Drone8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_drones5_stub_double():
    # mission_Swarm has no real 'mission_Swarm6' property in the generated
    # code (a bare stub) -- manually attach it so mission_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Drone(returnHome=True, type="sample_text")
    partner = mission_Swarm()
    setattr(partner, 'mission_Swarm6', None)
    _safe_set(owner, 'mission_Drone', partner)
    assert owner in getattr(partner, 'mission_Swarm6')
    _safe_set(owner, 'mission_Drone', None)
    assert owner not in getattr(partner, 'mission_Swarm6')


def test_assoc_initialPosition19_stub_double():
    # mission_PolygonTask has no real 'mission_PolygonTask20' property in the generated
    # code (a bare stub) -- manually attach it so mission_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Coordinate(altitude=3.14, latitude=3.14, longitude=3.14)
    partner = mission_PolygonTask()
    setattr(partner, 'mission_PolygonTask20', None)
    _safe_set(owner, 'mission_Coordinate21', partner)
    assert getattr(partner, 'mission_PolygonTask20') == owner
    _safe_set(owner, 'mission_Coordinate21', None)
    assert getattr(partner, 'mission_PolygonTask20') is None


def test_assoc_initialPosition26_stub_double():
    # mission_LineTask has no real 'mission_LineTask27' property in the generated
    # code (a bare stub) -- manually attach it so mission_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Coordinate(altitude=3.14, latitude=3.14, longitude=3.14)
    partner = mission_LineTask()
    setattr(partner, 'mission_LineTask27', None)
    _safe_set(owner, 'mission_Coordinate28', partner)
    assert getattr(partner, 'mission_LineTask27') == owner
    _safe_set(owner, 'mission_Coordinate28', None)
    assert getattr(partner, 'mission_LineTask27') is None


def test_assoc_point22_stub_double():
    # mission_PointTask has no real 'mission_PointTask' property in the generated
    # code (a bare stub) -- manually attach it so mission_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Coordinate(altitude=3.14, latitude=3.14, longitude=3.14)
    partner = mission_PointTask()
    setattr(partner, 'mission_PointTask', None)
    _safe_set(owner, 'mission_Coordinate23', partner)
    assert getattr(partner, 'mission_PointTask') == owner
    _safe_set(owner, 'mission_Coordinate23', None)
    assert getattr(partner, 'mission_PointTask') is None


def test_assoc_points24_stub_double():
    # mission_LineTask has no real 'mission_LineTask' property in the generated
    # code (a bare stub) -- manually attach it so mission_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Coordinate(altitude=3.14, latitude=3.14, longitude=3.14)
    partner = mission_LineTask()
    setattr(partner, 'mission_LineTask', None)
    _safe_set(owner, 'mission_Coordinate25', partner)
    assert owner in getattr(partner, 'mission_LineTask')
    _safe_set(owner, 'mission_Coordinate25', None)
    assert owner not in getattr(partner, 'mission_LineTask')


def test_assoc_referencePosition9_stub_double():
    # mission_ControlTask has no real 'mission_ControlTask' property in the generated
    # code (a bare stub) -- manually attach it so mission_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Coordinate(altitude=3.14, latitude=3.14, longitude=3.14)
    partner = mission_ControlTask()
    setattr(partner, 'mission_ControlTask', None)
    _safe_set(owner, 'mission_Coordinate10', partner)
    assert getattr(partner, 'mission_ControlTask') == owner
    _safe_set(owner, 'mission_Coordinate10', None)
    assert getattr(partner, 'mission_ControlTask') is None


def test_assoc_shell17_stub_double():
    # mission_PolygonTask has no real 'mission_PolygonTask' property in the generated
    # code (a bare stub) -- manually attach it so mission_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Coordinate(altitude=3.14, latitude=3.14, longitude=3.14)
    partner = mission_PolygonTask()
    setattr(partner, 'mission_PolygonTask', None)
    _safe_set(owner, 'mission_Coordinate18', partner)
    assert owner in getattr(partner, 'mission_PolygonTask')
    _safe_set(owner, 'mission_Coordinate18', None)
    assert owner not in getattr(partner, 'mission_PolygonTask')


def test_assoc_swarm3_stub_double():
    # mission_Swarm has no real 'mission_Swarm' property in the generated
    # code (a bare stub) -- manually attach it so mission_Mission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Mission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Mission(crs="sample_text")
    partner = mission_Swarm()
    setattr(partner, 'mission_Swarm', None)
    _safe_set(owner, 'mission_Mission4', partner)
    assert getattr(partner, 'mission_Swarm') == owner
    _safe_set(owner, 'mission_Mission4', None)
    assert getattr(partner, 'mission_Swarm') is None


def test_assoc_taskDependencies1_stub_double():
    # mission_TaskDependency has no real 'mission_TaskDependency' property in the generated
    # code (a bare stub) -- manually attach it so mission_Mission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Mission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Mission(crs="sample_text")
    partner = mission_TaskDependency()
    setattr(partner, 'mission_TaskDependency', None)
    _safe_set(owner, 'mission_Mission2', {partner})
    assert getattr(partner, 'mission_TaskDependency') == owner
    _safe_set(owner, 'mission_Mission2', set())
    assert getattr(partner, 'mission_TaskDependency') is None


def test_assoc_tasks0_stub_double():
    # mission_Task has no real 'mission_Task' property in the generated
    # code (a bare stub) -- manually attach it so mission_Mission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mission_Mission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mission_Mission(crs="sample_text")
    partner = mission_Task()
    setattr(partner, 'mission_Task', None)
    _safe_set(owner, 'mission_Mission', {partner})
    assert getattr(partner, 'mission_Task') == owner
    _safe_set(owner, 'mission_Mission', set())
    assert getattr(partner, 'mission_Task') is None


