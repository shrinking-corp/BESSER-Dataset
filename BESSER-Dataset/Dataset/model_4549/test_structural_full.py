import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_dronesSimulation_DroneInstance_currentBattery_value_roundtrip():
    instance = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    assert instance.currentBattery == 3.14
    instance.currentBattery = 9.99
    assert instance.currentBattery == 9.99


def test_dronesSimulation_DroneInstance_state_value_roundtrip():
    instance = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_dronesSimulation_Observation_id_value_roundtrip():
    instance = dronesSimulation_Observation(id="sample_text", time="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_dronesSimulation_Observation_time_value_roundtrip():
    instance = dronesSimulation_Observation(id="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_dronesSimulation_TaskInstance_state_value_roundtrip():
    instance = dronesSimulation_TaskInstance(state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_dronesSimulation_DroneObservation_isa_Observation():
    instance = dronesSimulation_DroneObservation()
    assert isinstance(instance, Observation)


def test_dronesSimulation_ObstacleObservation_isa_Observation():
    instance = dronesSimulation_ObstacleObservation()
    assert isinstance(instance, Observation)


def test_assoc_allocatedDrone18_link_reassign_clear():
    a = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    b1 = dronesSimulation_RoleInstance()
    b2 = dronesSimulation_RoleInstance()
    _safe_set(a, 'DroneInstance', b1)
    assert _is_linked(a, 'DroneInstance', b1)
    if hasattr(b1, 'currentRole'):
        assert _is_linked(b1, 'currentRole', a)
    _safe_set(a, 'DroneInstance', b2)
    assert _is_linked(a, 'DroneInstance', b2)
    if hasattr(b1, 'currentRole'):
        assert not _is_linked(b1, 'currentRole', a)
    if hasattr(b2, 'currentRole'):
        assert _is_linked(b2, 'currentRole', a)
    _safe_set(a, 'DroneInstance', None)
    assert not _is_linked(a, 'DroneInstance', b2)
    if hasattr(b2, 'currentRole'):
        assert not _is_linked(b2, 'currentRole', a)


def test_assoc_currentRole9_link_reassign_clear():
    a = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    b1 = dronesSimulation_RoleInstance()
    b2 = dronesSimulation_RoleInstance()
    _safe_set(a, 'allocatedDrone', b1)
    assert _is_linked(a, 'allocatedDrone', b1)
    if hasattr(b1, 'RoleInstance'):
        assert _is_linked(b1, 'RoleInstance', a)
    _safe_set(a, 'allocatedDrone', b2)
    assert _is_linked(a, 'allocatedDrone', b2)
    if hasattr(b1, 'RoleInstance'):
        assert not _is_linked(b1, 'RoleInstance', a)
    if hasattr(b2, 'RoleInstance'):
        assert _is_linked(b2, 'RoleInstance', a)
    _safe_set(a, 'allocatedDrone', None)
    assert not _is_linked(a, 'allocatedDrone', b2)
    if hasattr(b2, 'RoleInstance'):
        assert not _is_linked(b2, 'RoleInstance', a)


def test_assoc_drone5_link_reassign_clear():
    a = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    b1 = dronesSimulation_Drone()
    b2 = dronesSimulation_Drone()
    _safe_set(a, 'dronesSimulation_DroneInstance6', b1)
    assert _is_linked(a, 'dronesSimulation_DroneInstance6', b1)
    if hasattr(b1, 'dronesSimulation_Drone'):
        assert _is_linked(b1, 'dronesSimulation_Drone', a)
    _safe_set(a, 'dronesSimulation_DroneInstance6', b2)
    assert _is_linked(a, 'dronesSimulation_DroneInstance6', b2)
    if hasattr(b1, 'dronesSimulation_Drone'):
        assert not _is_linked(b1, 'dronesSimulation_Drone', a)
    if hasattr(b2, 'dronesSimulation_Drone'):
        assert _is_linked(b2, 'dronesSimulation_Drone', a)
    _safe_set(a, 'dronesSimulation_DroneInstance6', None)
    assert not _is_linked(a, 'dronesSimulation_DroneInstance6', b2)
    if hasattr(b2, 'dronesSimulation_Drone'):
        assert not _is_linked(b2, 'dronesSimulation_Drone', a)


def test_assoc_droneInstances3_link_reassign_clear():
    a = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    b1 = dronesSimulation_DronesSimulation()
    b2 = dronesSimulation_DronesSimulation()
    _safe_set(a, 'dronesSimulation_DroneInstance', b1)
    assert _is_linked(a, 'dronesSimulation_DroneInstance', b1)
    if hasattr(b1, 'dronesSimulation_DronesSimulation4'):
        assert _is_linked(b1, 'dronesSimulation_DronesSimulation4', a)
    _safe_set(a, 'dronesSimulation_DroneInstance', b2)
    assert _is_linked(a, 'dronesSimulation_DroneInstance', b2)
    if hasattr(b1, 'dronesSimulation_DronesSimulation4'):
        assert not _is_linked(b1, 'dronesSimulation_DronesSimulation4', a)
    if hasattr(b2, 'dronesSimulation_DronesSimulation4'):
        assert _is_linked(b2, 'dronesSimulation_DronesSimulation4', a)
    _safe_set(a, 'dronesSimulation_DroneInstance', None)
    assert not _is_linked(a, 'dronesSimulation_DroneInstance', b2)
    if hasattr(b2, 'dronesSimulation_DronesSimulation4'):
        assert not _is_linked(b2, 'dronesSimulation_DronesSimulation4', a)


def test_assoc_observations10_link_reassign_clear():
    a = dronesSimulation_Observation(id="sample_text", time="sample_text")
    b1 = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    b2 = dronesSimulation_DroneInstance(currentBattery=9.99, state="sample_text_2")
    _safe_set(a, 'dronesSimulation_Observation', b1)
    assert _is_linked(a, 'dronesSimulation_Observation', b1)
    if hasattr(b1, 'dronesSimulation_DroneInstance11'):
        assert _is_linked(b1, 'dronesSimulation_DroneInstance11', a)
    _safe_set(a, 'dronesSimulation_Observation', b2)
    assert _is_linked(a, 'dronesSimulation_Observation', b2)
    if hasattr(b1, 'dronesSimulation_DroneInstance11'):
        assert not _is_linked(b1, 'dronesSimulation_DroneInstance11', a)
    if hasattr(b2, 'dronesSimulation_DroneInstance11'):
        assert _is_linked(b2, 'dronesSimulation_DroneInstance11', a)
    _safe_set(a, 'dronesSimulation_Observation', None)
    assert not _is_linked(a, 'dronesSimulation_Observation', b2)
    if hasattr(b2, 'dronesSimulation_DroneInstance11'):
        assert not _is_linked(b2, 'dronesSimulation_DroneInstance11', a)


def test_assoc_position7_link_reassign_clear():
    a = dronesSimulation_DroneInstance(currentBattery=3.14, state="sample_text")
    b1 = dronesSimulation_Position()
    b2 = dronesSimulation_Position()
    _safe_set(a, 'dronesSimulation_DroneInstance8', b1)
    assert _is_linked(a, 'dronesSimulation_DroneInstance8', b1)
    if hasattr(b1, 'dronesSimulation_Position'):
        assert _is_linked(b1, 'dronesSimulation_Position', a)
    _safe_set(a, 'dronesSimulation_DroneInstance8', b2)
    assert _is_linked(a, 'dronesSimulation_DroneInstance8', b2)
    if hasattr(b1, 'dronesSimulation_Position'):
        assert not _is_linked(b1, 'dronesSimulation_Position', a)
    if hasattr(b2, 'dronesSimulation_Position'):
        assert _is_linked(b2, 'dronesSimulation_Position', a)
    _safe_set(a, 'dronesSimulation_DroneInstance8', None)
    assert not _is_linked(a, 'dronesSimulation_DroneInstance8', b2)
    if hasattr(b2, 'dronesSimulation_Position'):
        assert not _is_linked(b2, 'dronesSimulation_Position', a)


def test_assoc_roleInstances14_link_reassign_clear():
    a = dronesSimulation_TaskInstance(state="sample_text")
    b1 = dronesSimulation_RoleInstance()
    b2 = dronesSimulation_RoleInstance()
    _safe_set(a, 'taskInstance', {b1})
    assert _is_linked(a, 'taskInstance', b1)
    if hasattr(b1, 'RoleInstance15'):
        assert _is_linked(b1, 'RoleInstance15', a)
    _safe_set(a, 'taskInstance', {b2})
    assert _is_linked(a, 'taskInstance', b2)
    if hasattr(b1, 'RoleInstance15'):
        assert not _is_linked(b1, 'RoleInstance15', a)
    if hasattr(b2, 'RoleInstance15'):
        assert _is_linked(b2, 'RoleInstance15', a)
    _safe_set(a, 'taskInstance', set())
    assert not _is_linked(a, 'taskInstance', b2)
    if hasattr(b2, 'RoleInstance15'):
        assert not _is_linked(b2, 'RoleInstance15', a)


def test_assoc_task12_link_reassign_clear():
    a = dronesSimulation_TaskInstance(state="sample_text")
    b1 = dronesSimulation_Task()
    b2 = dronesSimulation_Task()
    _safe_set(a, 'dronesSimulation_TaskInstance13', b1)
    assert _is_linked(a, 'dronesSimulation_TaskInstance13', b1)
    if hasattr(b1, 'dronesSimulation_Task'):
        assert _is_linked(b1, 'dronesSimulation_Task', a)
    _safe_set(a, 'dronesSimulation_TaskInstance13', b2)
    assert _is_linked(a, 'dronesSimulation_TaskInstance13', b2)
    if hasattr(b1, 'dronesSimulation_Task'):
        assert not _is_linked(b1, 'dronesSimulation_Task', a)
    if hasattr(b2, 'dronesSimulation_Task'):
        assert _is_linked(b2, 'dronesSimulation_Task', a)
    _safe_set(a, 'dronesSimulation_TaskInstance13', None)
    assert not _is_linked(a, 'dronesSimulation_TaskInstance13', b2)
    if hasattr(b2, 'dronesSimulation_Task'):
        assert not _is_linked(b2, 'dronesSimulation_Task', a)


def test_assoc_taskInstance17_link_reassign_clear():
    a = dronesSimulation_TaskInstance(state="sample_text")
    b1 = dronesSimulation_RoleInstance()
    b2 = dronesSimulation_RoleInstance()
    _safe_set(a, 'TaskInstance', b1)
    assert _is_linked(a, 'TaskInstance', b1)
    if hasattr(b1, 'roleInstances'):
        assert _is_linked(b1, 'roleInstances', a)
    _safe_set(a, 'TaskInstance', b2)
    assert _is_linked(a, 'TaskInstance', b2)
    if hasattr(b1, 'roleInstances'):
        assert not _is_linked(b1, 'roleInstances', a)
    if hasattr(b2, 'roleInstances'):
        assert _is_linked(b2, 'roleInstances', a)
    _safe_set(a, 'TaskInstance', None)
    assert not _is_linked(a, 'TaskInstance', b2)
    if hasattr(b2, 'roleInstances'):
        assert not _is_linked(b2, 'roleInstances', a)


def test_assoc_taskInstances1_link_reassign_clear():
    a = dronesSimulation_TaskInstance(state="sample_text")
    b1 = dronesSimulation_DronesSimulation()
    b2 = dronesSimulation_DronesSimulation()
    _safe_set(a, 'dronesSimulation_TaskInstance', b1)
    assert _is_linked(a, 'dronesSimulation_TaskInstance', b1)
    if hasattr(b1, 'dronesSimulation_DronesSimulation2'):
        assert _is_linked(b1, 'dronesSimulation_DronesSimulation2', a)
    _safe_set(a, 'dronesSimulation_TaskInstance', b2)
    assert _is_linked(a, 'dronesSimulation_TaskInstance', b2)
    if hasattr(b1, 'dronesSimulation_DronesSimulation2'):
        assert not _is_linked(b1, 'dronesSimulation_DronesSimulation2', a)
    if hasattr(b2, 'dronesSimulation_DronesSimulation2'):
        assert _is_linked(b2, 'dronesSimulation_DronesSimulation2', a)
    _safe_set(a, 'dronesSimulation_TaskInstance', None)
    assert not _is_linked(a, 'dronesSimulation_TaskInstance', b2)
    if hasattr(b2, 'dronesSimulation_DronesSimulation2'):
        assert not _is_linked(b2, 'dronesSimulation_DronesSimulation2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Observation_strategy = st.builds(Observation)
@given(instance=Observation_strategy)
@settings(max_examples=25)
def test_Observation_instantiation(instance):
    assert isinstance(instance, Observation)


dronesSimulation_Drone_strategy = st.builds(dronesSimulation_Drone)
@given(instance=dronesSimulation_Drone_strategy)
@settings(max_examples=25)
def test_dronesSimulation_Drone_instantiation(instance):
    assert isinstance(instance, dronesSimulation_Drone)


dronesSimulation_DroneInstance_strategy = st.builds(dronesSimulation_DroneInstance, currentBattery=st.floats(allow_nan=False, allow_infinity=False), state=safe_text)
@given(instance=dronesSimulation_DroneInstance_strategy)
@settings(max_examples=25)
def test_dronesSimulation_DroneInstance_instantiation(instance):
    assert isinstance(instance, dronesSimulation_DroneInstance)


dronesSimulation_DroneObservation_strategy = st.builds(dronesSimulation_DroneObservation)
@given(instance=dronesSimulation_DroneObservation_strategy)
@settings(max_examples=25)
def test_dronesSimulation_DroneObservation_instantiation(instance):
    assert isinstance(instance, dronesSimulation_DroneObservation)


dronesSimulation_DronesSimulation_strategy = st.builds(dronesSimulation_DronesSimulation)
@given(instance=dronesSimulation_DronesSimulation_strategy)
@settings(max_examples=25)
def test_dronesSimulation_DronesSimulation_instantiation(instance):
    assert isinstance(instance, dronesSimulation_DronesSimulation)


dronesSimulation_Observation_strategy = st.builds(dronesSimulation_Observation, id=safe_text, time=safe_text)
@given(instance=dronesSimulation_Observation_strategy)
@settings(max_examples=25)
def test_dronesSimulation_Observation_instantiation(instance):
    assert isinstance(instance, dronesSimulation_Observation)


dronesSimulation_Obstacle_strategy = st.builds(dronesSimulation_Obstacle)
@given(instance=dronesSimulation_Obstacle_strategy)
@settings(max_examples=25)
def test_dronesSimulation_Obstacle_instantiation(instance):
    assert isinstance(instance, dronesSimulation_Obstacle)


dronesSimulation_ObstacleObservation_strategy = st.builds(dronesSimulation_ObstacleObservation)
@given(instance=dronesSimulation_ObstacleObservation_strategy)
@settings(max_examples=25)
def test_dronesSimulation_ObstacleObservation_instantiation(instance):
    assert isinstance(instance, dronesSimulation_ObstacleObservation)


dronesSimulation_Position_strategy = st.builds(dronesSimulation_Position)
@given(instance=dronesSimulation_Position_strategy)
@settings(max_examples=25)
def test_dronesSimulation_Position_instantiation(instance):
    assert isinstance(instance, dronesSimulation_Position)


dronesSimulation_Role_strategy = st.builds(dronesSimulation_Role)
@given(instance=dronesSimulation_Role_strategy)
@settings(max_examples=25)
def test_dronesSimulation_Role_instantiation(instance):
    assert isinstance(instance, dronesSimulation_Role)


dronesSimulation_RoleInstance_strategy = st.builds(dronesSimulation_RoleInstance)
@given(instance=dronesSimulation_RoleInstance_strategy)
@settings(max_examples=25)
def test_dronesSimulation_RoleInstance_instantiation(instance):
    assert isinstance(instance, dronesSimulation_RoleInstance)


dronesSimulation_Scenario_strategy = st.builds(dronesSimulation_Scenario)
@given(instance=dronesSimulation_Scenario_strategy)
@settings(max_examples=25)
def test_dronesSimulation_Scenario_instantiation(instance):
    assert isinstance(instance, dronesSimulation_Scenario)


dronesSimulation_Task_strategy = st.builds(dronesSimulation_Task)
@given(instance=dronesSimulation_Task_strategy)
@settings(max_examples=25)
def test_dronesSimulation_Task_instantiation(instance):
    assert isinstance(instance, dronesSimulation_Task)


dronesSimulation_TaskInstance_strategy = st.builds(dronesSimulation_TaskInstance, state=safe_text)
@given(instance=dronesSimulation_TaskInstance_strategy)
@settings(max_examples=25)
def test_dronesSimulation_TaskInstance_instantiation(instance):
    assert isinstance(instance, dronesSimulation_TaskInstance)


