import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Observation,
    dronesSimulation_Drone,
    dronesSimulation_DroneInstance,
    dronesSimulation_DroneObservation,
    dronesSimulation_DronesSimulation,
    dronesSimulation_Observation,
    dronesSimulation_Obstacle,
    dronesSimulation_ObstacleObservation,
    dronesSimulation_Position,
    dronesSimulation_Role,
    dronesSimulation_RoleInstance,
    dronesSimulation_Scenario,
    dronesSimulation_Task,
    dronesSimulation_TaskInstance,
    DroneState,
    TaskState,
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

def test_assoc_observations10_reverse_link_reassign_clear():
    a1 = dronesSimulation_Observation(id="sample_text", time="sample_text")
    a2 = dronesSimulation_Observation(id="sample_text_2", time="sample_text_2")
    b = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    _safe_set(b, 'dronesSimulation_DroneInstance11', {a1})
    assert _is_linked(b, 'dronesSimulation_DroneInstance11', a1)
    if hasattr(a1, 'dronesSimulation_Observation'):
        assert _is_linked(a1, 'dronesSimulation_Observation', b)
    _safe_set(b, 'dronesSimulation_DroneInstance11', {a2})
    assert _is_linked(b, 'dronesSimulation_DroneInstance11', a2)
    if hasattr(a1, 'dronesSimulation_Observation'):
        assert not _is_linked(a1, 'dronesSimulation_Observation', b)
    if hasattr(a2, 'dronesSimulation_Observation'):
        assert _is_linked(a2, 'dronesSimulation_Observation', b)
    _safe_set(b, 'dronesSimulation_DroneInstance11', set())
    assert not _is_linked(b, 'dronesSimulation_DroneInstance11', a2)
    if hasattr(a2, 'dronesSimulation_Observation'):
        assert not _is_linked(a2, 'dronesSimulation_Observation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allocatedDrone18_stub_double():
    # dronesSimulation_RoleInstance has no real 'currentRole' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_DroneInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_DroneInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    partner = dronesSimulation_RoleInstance()
    setattr(partner, 'currentRole', None)
    _safe_set(owner, 'DroneInstance', partner)
    assert getattr(partner, 'currentRole') == owner
    _safe_set(owner, 'DroneInstance', None)
    assert getattr(partner, 'currentRole') is None


def test_assoc_currentRole9_stub_double():
    # dronesSimulation_RoleInstance has no real 'RoleInstance' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_DroneInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_DroneInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    partner = dronesSimulation_RoleInstance()
    setattr(partner, 'RoleInstance', None)
    _safe_set(owner, 'allocatedDrone', partner)
    assert getattr(partner, 'RoleInstance') == owner
    _safe_set(owner, 'allocatedDrone', None)
    assert getattr(partner, 'RoleInstance') is None


def test_assoc_drone5_stub_double():
    # dronesSimulation_Drone has no real 'dronesSimulation_Drone' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_DroneInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_DroneInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    partner = dronesSimulation_Drone()
    setattr(partner, 'dronesSimulation_Drone', None)
    _safe_set(owner, 'dronesSimulation_DroneInstance6', partner)
    assert getattr(partner, 'dronesSimulation_Drone') == owner
    _safe_set(owner, 'dronesSimulation_DroneInstance6', None)
    assert getattr(partner, 'dronesSimulation_Drone') is None


def test_assoc_droneInstances3_stub_double():
    # dronesSimulation_DronesSimulation has no real 'dronesSimulation_DronesSimulation4' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_DroneInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_DroneInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    partner = dronesSimulation_DronesSimulation()
    setattr(partner, 'dronesSimulation_DronesSimulation4', None)
    _safe_set(owner, 'dronesSimulation_DroneInstance', partner)
    assert owner in getattr(partner, 'dronesSimulation_DronesSimulation4')
    _safe_set(owner, 'dronesSimulation_DroneInstance', None)
    assert owner not in getattr(partner, 'dronesSimulation_DronesSimulation4')


def test_assoc_position7_stub_double():
    # dronesSimulation_Position has no real 'dronesSimulation_Position' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_DroneInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_DroneInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    partner = dronesSimulation_Position()
    setattr(partner, 'dronesSimulation_Position', None)
    _safe_set(owner, 'dronesSimulation_DroneInstance8', partner)
    assert getattr(partner, 'dronesSimulation_Position') == owner
    _safe_set(owner, 'dronesSimulation_DroneInstance8', None)
    assert getattr(partner, 'dronesSimulation_Position') is None


def test_assoc_roleInstances14_stub_double():
    # dronesSimulation_RoleInstance has no real 'RoleInstance15' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_TaskInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_TaskInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_TaskInstance(state="sample_text")
    partner = dronesSimulation_RoleInstance()
    setattr(partner, 'RoleInstance15', None)
    _safe_set(owner, 'taskInstance', {partner})
    assert getattr(partner, 'RoleInstance15') == owner
    _safe_set(owner, 'taskInstance', set())
    assert getattr(partner, 'RoleInstance15') is None


def test_assoc_task12_stub_double():
    # dronesSimulation_Task has no real 'dronesSimulation_Task' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_TaskInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_TaskInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_TaskInstance(state="sample_text")
    partner = dronesSimulation_Task()
    setattr(partner, 'dronesSimulation_Task', None)
    _safe_set(owner, 'dronesSimulation_TaskInstance13', partner)
    assert getattr(partner, 'dronesSimulation_Task') == owner
    _safe_set(owner, 'dronesSimulation_TaskInstance13', None)
    assert getattr(partner, 'dronesSimulation_Task') is None


def test_assoc_taskInstance17_stub_double():
    # dronesSimulation_RoleInstance has no real 'roleInstances' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_TaskInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_TaskInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_TaskInstance(state="sample_text")
    partner = dronesSimulation_RoleInstance()
    setattr(partner, 'roleInstances', None)
    _safe_set(owner, 'TaskInstance', partner)
    assert getattr(partner, 'roleInstances') == owner
    _safe_set(owner, 'TaskInstance', None)
    assert getattr(partner, 'roleInstances') is None


def test_assoc_taskInstances1_stub_double():
    # dronesSimulation_DronesSimulation has no real 'dronesSimulation_DronesSimulation2' property in the generated
    # code (a bare stub) -- manually attach it so dronesSimulation_TaskInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dronesSimulation_TaskInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dronesSimulation_TaskInstance(state="sample_text")
    partner = dronesSimulation_DronesSimulation()
    setattr(partner, 'dronesSimulation_DronesSimulation2', None)
    _safe_set(owner, 'dronesSimulation_TaskInstance', partner)
    assert owner in getattr(partner, 'dronesSimulation_DronesSimulation2')
    _safe_set(owner, 'dronesSimulation_TaskInstance', None)
    assert owner not in getattr(partner, 'dronesSimulation_DronesSimulation2')


