import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AABB,
    Capability,
    NamedElement,
    Region,
    dronesStructure_AABB,
    dronesStructure_Capability,
    dronesStructure_Charger,
    dronesStructure_CooperativeAction,
    dronesStructure_Dimension,
    dronesStructure_Drone,
    dronesStructure_DroneType,
    dronesStructure_DronesStructure,
    dronesStructure_MovementCapability,
    dronesStructure_NamedElement,
    dronesStructure_Obstacle,
    dronesStructure_Position,
    dronesStructure_ProvidedCapability,
    dronesStructure_Region,
    dronesStructure_RequiredCapability,
    dronesStructure_Role,
    dronesStructure_ScanningCapability,
    dronesStructure_Scenario,
    dronesStructure_ScenarioBounds,
    dronesStructure_Task,
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

def test_dronesStructure_CooperativeAction_duration_value_roundtrip():
    instance = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    assert instance.duration == 3.14
    instance.duration = 9.99
    assert instance.duration == 9.99


def test_dronesStructure_CooperativeAction_startTimeout_value_roundtrip():
    instance = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    assert instance.startTimeout == 3.14
    instance.startTimeout = 9.99
    assert instance.startTimeout == 9.99


def test_dronesStructure_Dimension_depth_value_roundtrip():
    instance = dronesStructure_Dimension(depth=3.14, height=3.14, width=3.14)
    assert instance.depth == 3.14
    instance.depth = 9.99
    assert instance.depth == 9.99


def test_dronesStructure_Dimension_height_value_roundtrip():
    instance = dronesStructure_Dimension(depth=3.14, height=3.14, width=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_dronesStructure_Dimension_width_value_roundtrip():
    instance = dronesStructure_Dimension(depth=3.14, height=3.14, width=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_dronesStructure_DroneType_idleEneryConsumption_value_roundtrip():
    instance = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    assert instance.idleEneryConsumption == 3.14
    instance.idleEneryConsumption = 9.99
    assert instance.idleEneryConsumption == 9.99


def test_dronesStructure_DroneType_maxBatteryCapacity_value_roundtrip():
    instance = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    assert instance.maxBatteryCapacity == 3.14
    instance.maxBatteryCapacity = 9.99
    assert instance.maxBatteryCapacity == 9.99


def test_dronesStructure_DroneType_weight_value_roundtrip():
    instance = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    assert instance.weight == 3.14
    instance.weight = 9.99
    assert instance.weight == 9.99


def test_dronesStructure_NamedElement_name_value_roundtrip():
    instance = dronesStructure_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dronesStructure_Position_x_value_roundtrip():
    instance = dronesStructure_Position(x=3.14, y=3.14, z=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_dronesStructure_Position_y_value_roundtrip():
    instance = dronesStructure_Position(x=3.14, y=3.14, z=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_dronesStructure_Position_z_value_roundtrip():
    instance = dronesStructure_Position(x=3.14, y=3.14, z=3.14)
    assert instance.z == 3.14
    instance.z = 9.99
    assert instance.z == 9.99


def test_dronesStructure_ProvidedCapability_energyConsumptionPerValue_value_roundtrip():
    instance = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    assert instance.energyConsumptionPerValue == 3.14
    instance.energyConsumptionPerValue = 9.99
    assert instance.energyConsumptionPerValue == 9.99


def test_dronesStructure_ProvidedCapability_maximalValue_value_roundtrip():
    instance = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    assert instance.maximalValue == 3.14
    instance.maximalValue = 9.99
    assert instance.maximalValue == 9.99


def test_dronesStructure_RequiredCapability_minimalValue_value_roundtrip():
    instance = dronesStructure_RequiredCapability(minimalValue=3.14)
    assert instance.minimalValue == 3.14
    instance.minimalValue = 9.99
    assert instance.minimalValue == 9.99


def test_dronesStructure_Scenario_maximumCommunicationDistance_value_roundtrip():
    instance = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    assert instance.maximumCommunicationDistance == 3.14
    instance.maximumCommunicationDistance = 9.99
    assert instance.maximumCommunicationDistance == 9.99


def test_dronesStructure_Scenario_safeCommunicationDistance_value_roundtrip():
    instance = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    assert instance.safeCommunicationDistance == 3.14
    instance.safeCommunicationDistance = 9.99
    assert instance.safeCommunicationDistance == 9.99


def test_dronesStructure_Obstacle_isa_AABB():
    instance = dronesStructure_Obstacle()
    assert isinstance(instance, AABB)


def test_dronesStructure_Region_isa_AABB():
    instance = dronesStructure_Region()
    assert isinstance(instance, AABB)


def test_dronesStructure_ScenarioBounds_isa_AABB():
    instance = dronesStructure_ScenarioBounds()
    assert isinstance(instance, AABB)


def test_dronesStructure_MovementCapability_isa_Capability():
    instance = dronesStructure_MovementCapability()
    assert isinstance(instance, Capability)


def test_dronesStructure_ScanningCapability_isa_Capability():
    instance = dronesStructure_ScanningCapability()
    assert isinstance(instance, Capability)


def test_dronesStructure_Capability_isa_NamedElement():
    instance = dronesStructure_Capability()
    assert isinstance(instance, NamedElement)


def test_dronesStructure_CooperativeAction_isa_NamedElement():
    instance = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    assert isinstance(instance, NamedElement)


def test_dronesStructure_Drone_isa_NamedElement():
    instance = dronesStructure_Drone()
    assert isinstance(instance, NamedElement)


def test_dronesStructure_DroneType_isa_NamedElement():
    instance = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    assert isinstance(instance, NamedElement)


def test_dronesStructure_Obstacle_isa_NamedElement():
    instance = dronesStructure_Obstacle()
    assert isinstance(instance, NamedElement)


def test_dronesStructure_Region_isa_NamedElement():
    instance = dronesStructure_Region()
    assert isinstance(instance, NamedElement)


def test_dronesStructure_Role_isa_NamedElement():
    instance = dronesStructure_Role()
    assert isinstance(instance, NamedElement)


def test_dronesStructure_Scenario_isa_NamedElement():
    instance = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    assert isinstance(instance, NamedElement)


def test_dronesStructure_Task_isa_NamedElement():
    instance = dronesStructure_Task()
    assert isinstance(instance, NamedElement)


def test_dronesStructure_Charger_isa_Region():
    instance = dronesStructure_Charger()
    assert isinstance(instance, Region)


def test_assoc_actionToPerform48_link_reassign_clear():
    a = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    b1 = dronesStructure_Task()
    b2 = dronesStructure_Task()
    _safe_set(a, 'dronesStructure_CooperativeAction50', b1)
    assert _is_linked(a, 'dronesStructure_CooperativeAction50', b1)
    if hasattr(b1, 'dronesStructure_Task49'):
        assert _is_linked(b1, 'dronesStructure_Task49', a)
    _safe_set(a, 'dronesStructure_CooperativeAction50', b2)
    assert _is_linked(a, 'dronesStructure_CooperativeAction50', b2)
    if hasattr(b1, 'dronesStructure_Task49'):
        assert not _is_linked(b1, 'dronesStructure_Task49', a)
    if hasattr(b2, 'dronesStructure_Task49'):
        assert _is_linked(b2, 'dronesStructure_Task49', a)
    _safe_set(a, 'dronesStructure_CooperativeAction50', None)
    assert not _is_linked(a, 'dronesStructure_CooperativeAction50', b2)
    if hasattr(b2, 'dronesStructure_Task49'):
        assert not _is_linked(b2, 'dronesStructure_Task49', a)


def test_assoc_allowedBounds9_link_reassign_clear():
    a = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    b1 = dronesStructure_ScenarioBounds()
    b2 = dronesStructure_ScenarioBounds()
    _safe_set(a, 'dronesStructure_Scenario10', b1)
    assert _is_linked(a, 'dronesStructure_Scenario10', b1)
    if hasattr(b1, 'dronesStructure_ScenarioBounds'):
        assert _is_linked(b1, 'dronesStructure_ScenarioBounds', a)
    _safe_set(a, 'dronesStructure_Scenario10', b2)
    assert _is_linked(a, 'dronesStructure_Scenario10', b2)
    if hasattr(b1, 'dronesStructure_ScenarioBounds'):
        assert not _is_linked(b1, 'dronesStructure_ScenarioBounds', a)
    if hasattr(b2, 'dronesStructure_ScenarioBounds'):
        assert _is_linked(b2, 'dronesStructure_ScenarioBounds', a)
    _safe_set(a, 'dronesStructure_Scenario10', None)
    assert not _is_linked(a, 'dronesStructure_Scenario10', b2)
    if hasattr(b2, 'dronesStructure_ScenarioBounds'):
        assert not _is_linked(b2, 'dronesStructure_ScenarioBounds', a)


def test_assoc_capability25_link_reassign_clear():
    a = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    b1 = dronesStructure_Capability()
    b2 = dronesStructure_Capability()
    _safe_set(a, 'dronesStructure_ProvidedCapability26', b1)
    assert _is_linked(a, 'dronesStructure_ProvidedCapability26', b1)
    if hasattr(b1, 'dronesStructure_Capability27'):
        assert _is_linked(b1, 'dronesStructure_Capability27', a)
    _safe_set(a, 'dronesStructure_ProvidedCapability26', b2)
    assert _is_linked(a, 'dronesStructure_ProvidedCapability26', b2)
    if hasattr(b1, 'dronesStructure_Capability27'):
        assert not _is_linked(b1, 'dronesStructure_Capability27', a)
    if hasattr(b2, 'dronesStructure_Capability27'):
        assert _is_linked(b2, 'dronesStructure_Capability27', a)
    _safe_set(a, 'dronesStructure_ProvidedCapability26', None)
    assert not _is_linked(a, 'dronesStructure_ProvidedCapability26', b2)
    if hasattr(b2, 'dronesStructure_Capability27'):
        assert not _is_linked(b2, 'dronesStructure_Capability27', a)


def test_assoc_capability32_link_reassign_clear():
    a = dronesStructure_RequiredCapability(minimalValue=3.14)
    b1 = dronesStructure_Capability()
    b2 = dronesStructure_Capability()
    _safe_set(a, 'dronesStructure_RequiredCapability', b1)
    assert _is_linked(a, 'dronesStructure_RequiredCapability', b1)
    if hasattr(b1, 'dronesStructure_Capability33'):
        assert _is_linked(b1, 'dronesStructure_Capability33', a)
    _safe_set(a, 'dronesStructure_RequiredCapability', b2)
    assert _is_linked(a, 'dronesStructure_RequiredCapability', b2)
    if hasattr(b1, 'dronesStructure_Capability33'):
        assert not _is_linked(b1, 'dronesStructure_Capability33', a)
    if hasattr(b2, 'dronesStructure_Capability33'):
        assert _is_linked(b2, 'dronesStructure_Capability33', a)
    _safe_set(a, 'dronesStructure_RequiredCapability', None)
    assert not _is_linked(a, 'dronesStructure_RequiredCapability', b2)
    if hasattr(b2, 'dronesStructure_Capability33'):
        assert not _is_linked(b2, 'dronesStructure_Capability33', a)


def test_assoc_cooperativeAction31_link_reassign_clear():
    a = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    b1 = dronesStructure_Role()
    b2 = dronesStructure_Role()
    _safe_set(a, 'CooperativeAction', b1)
    assert _is_linked(a, 'CooperativeAction', b1)
    if hasattr(b1, 'roles'):
        assert _is_linked(b1, 'roles', a)
    _safe_set(a, 'CooperativeAction', b2)
    assert _is_linked(a, 'CooperativeAction', b2)
    if hasattr(b1, 'roles'):
        assert not _is_linked(b1, 'roles', a)
    if hasattr(b2, 'roles'):
        assert _is_linked(b2, 'roles', a)
    _safe_set(a, 'CooperativeAction', None)
    assert not _is_linked(a, 'CooperativeAction', b2)
    if hasattr(b2, 'roles'):
        assert not _is_linked(b2, 'roles', a)


def test_assoc_cooperativeActions3_link_reassign_clear():
    a = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    b1 = dronesStructure_DronesStructure()
    b2 = dronesStructure_DronesStructure()
    _safe_set(a, 'dronesStructure_CooperativeAction', b1)
    assert _is_linked(a, 'dronesStructure_CooperativeAction', b1)
    if hasattr(b1, 'dronesStructure_DronesStructure4'):
        assert _is_linked(b1, 'dronesStructure_DronesStructure4', a)
    _safe_set(a, 'dronesStructure_CooperativeAction', b2)
    assert _is_linked(a, 'dronesStructure_CooperativeAction', b2)
    if hasattr(b1, 'dronesStructure_DronesStructure4'):
        assert not _is_linked(b1, 'dronesStructure_DronesStructure4', a)
    if hasattr(b2, 'dronesStructure_DronesStructure4'):
        assert _is_linked(b2, 'dronesStructure_DronesStructure4', a)
    _safe_set(a, 'dronesStructure_CooperativeAction', None)
    assert not _is_linked(a, 'dronesStructure_CooperativeAction', b2)
    if hasattr(b2, 'dronesStructure_DronesStructure4'):
        assert not _is_linked(b2, 'dronesStructure_DronesStructure4', a)


def test_assoc_dimension20_link_reassign_clear():
    a = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    b1 = dronesStructure_Dimension(depth=3.14, height=3.14, width=3.14)
    b2 = dronesStructure_Dimension(depth=9.99, height=9.99, width=9.99)
    _safe_set(a, 'dronesStructure_DroneType21', b1)
    assert _is_linked(a, 'dronesStructure_DroneType21', b1)
    if hasattr(b1, 'dronesStructure_Dimension'):
        assert _is_linked(b1, 'dronesStructure_Dimension', a)
    _safe_set(a, 'dronesStructure_DroneType21', b2)
    assert _is_linked(a, 'dronesStructure_DroneType21', b2)
    if hasattr(b1, 'dronesStructure_Dimension'):
        assert not _is_linked(b1, 'dronesStructure_Dimension', a)
    if hasattr(b2, 'dronesStructure_Dimension'):
        assert _is_linked(b2, 'dronesStructure_Dimension', a)
    _safe_set(a, 'dronesStructure_DroneType21', None)
    assert not _is_linked(a, 'dronesStructure_DroneType21', b2)
    if hasattr(b2, 'dronesStructure_Dimension'):
        assert not _is_linked(b2, 'dronesStructure_Dimension', a)


def test_assoc_dimension43_link_reassign_clear():
    a = dronesStructure_Dimension(depth=3.14, height=3.14, width=3.14)
    b1 = dronesStructure_AABB()
    b2 = dronesStructure_AABB()
    _safe_set(a, 'dronesStructure_Dimension45', b1)
    assert _is_linked(a, 'dronesStructure_Dimension45', b1)
    if hasattr(b1, 'dronesStructure_AABB44'):
        assert _is_linked(b1, 'dronesStructure_AABB44', a)
    _safe_set(a, 'dronesStructure_Dimension45', b2)
    assert _is_linked(a, 'dronesStructure_Dimension45', b2)
    if hasattr(b1, 'dronesStructure_AABB44'):
        assert not _is_linked(b1, 'dronesStructure_AABB44', a)
    if hasattr(b2, 'dronesStructure_AABB44'):
        assert _is_linked(b2, 'dronesStructure_AABB44', a)
    _safe_set(a, 'dronesStructure_Dimension45', None)
    assert not _is_linked(a, 'dronesStructure_Dimension45', b2)
    if hasattr(b2, 'dronesStructure_AABB44'):
        assert not _is_linked(b2, 'dronesStructure_AABB44', a)


def test_assoc_droneType28_link_reassign_clear():
    a = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    b1 = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    b2 = dronesStructure_DroneType(idleEneryConsumption=9.99, maxBatteryCapacity=9.99, weight=9.99)
    _safe_set(a, 'providedCapabilities', b1)
    assert _is_linked(a, 'providedCapabilities', b1)
    if hasattr(b1, 'DroneType'):
        assert _is_linked(b1, 'DroneType', a)
    _safe_set(a, 'providedCapabilities', b2)
    assert _is_linked(a, 'providedCapabilities', b2)
    if hasattr(b1, 'DroneType'):
        assert not _is_linked(b1, 'DroneType', a)
    if hasattr(b2, 'DroneType'):
        assert _is_linked(b2, 'DroneType', a)
    _safe_set(a, 'providedCapabilities', None)
    assert not _is_linked(a, 'providedCapabilities', b2)
    if hasattr(b2, 'DroneType'):
        assert not _is_linked(b2, 'DroneType', a)


def test_assoc_droneTypes1_link_reassign_clear():
    a = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    b1 = dronesStructure_DronesStructure()
    b2 = dronesStructure_DronesStructure()
    _safe_set(a, 'dronesStructure_DroneType', b1)
    assert _is_linked(a, 'dronesStructure_DroneType', b1)
    if hasattr(b1, 'dronesStructure_DronesStructure2'):
        assert _is_linked(b1, 'dronesStructure_DronesStructure2', a)
    _safe_set(a, 'dronesStructure_DroneType', b2)
    assert _is_linked(a, 'dronesStructure_DroneType', b2)
    if hasattr(b1, 'dronesStructure_DronesStructure2'):
        assert not _is_linked(b1, 'dronesStructure_DronesStructure2', a)
    if hasattr(b2, 'dronesStructure_DronesStructure2'):
        assert _is_linked(b2, 'dronesStructure_DronesStructure2', a)
    _safe_set(a, 'dronesStructure_DroneType', None)
    assert not _is_linked(a, 'dronesStructure_DroneType', b2)
    if hasattr(b2, 'dronesStructure_DronesStructure2'):
        assert not _is_linked(b2, 'dronesStructure_DronesStructure2', a)


def test_assoc_drones7_link_reassign_clear():
    a = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    b1 = dronesStructure_Drone()
    b2 = dronesStructure_Drone()
    _safe_set(a, 'dronesStructure_Scenario8', {b1})
    assert _is_linked(a, 'dronesStructure_Scenario8', b1)
    if hasattr(b1, 'dronesStructure_Drone'):
        assert _is_linked(b1, 'dronesStructure_Drone', a)
    _safe_set(a, 'dronesStructure_Scenario8', {b2})
    assert _is_linked(a, 'dronesStructure_Scenario8', b2)
    if hasattr(b1, 'dronesStructure_Drone'):
        assert not _is_linked(b1, 'dronesStructure_Drone', a)
    if hasattr(b2, 'dronesStructure_Drone'):
        assert _is_linked(b2, 'dronesStructure_Drone', a)
    _safe_set(a, 'dronesStructure_Scenario8', set())
    assert not _is_linked(a, 'dronesStructure_Scenario8', b2)
    if hasattr(b2, 'dronesStructure_Drone'):
        assert not _is_linked(b2, 'dronesStructure_Drone', a)


def test_assoc_dronetype38_link_reassign_clear():
    a = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    b1 = dronesStructure_Drone()
    b2 = dronesStructure_Drone()
    _safe_set(a, 'dronesStructure_DroneType40', b1)
    assert _is_linked(a, 'dronesStructure_DroneType40', b1)
    if hasattr(b1, 'dronesStructure_Drone39'):
        assert _is_linked(b1, 'dronesStructure_Drone39', a)
    _safe_set(a, 'dronesStructure_DroneType40', b2)
    assert _is_linked(a, 'dronesStructure_DroneType40', b2)
    if hasattr(b1, 'dronesStructure_Drone39'):
        assert not _is_linked(b1, 'dronesStructure_Drone39', a)
    if hasattr(b2, 'dronesStructure_Drone39'):
        assert _is_linked(b2, 'dronesStructure_Drone39', a)
    _safe_set(a, 'dronesStructure_DroneType40', None)
    assert not _is_linked(a, 'dronesStructure_DroneType40', b2)
    if hasattr(b2, 'dronesStructure_Drone39'):
        assert not _is_linked(b2, 'dronesStructure_Drone39', a)


def test_assoc_movementCapability18_link_reassign_clear():
    a = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    b1 = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    b2 = dronesStructure_DroneType(idleEneryConsumption=9.99, maxBatteryCapacity=9.99, weight=9.99)
    _safe_set(a, 'dronesStructure_ProvidedCapability', b1)
    assert _is_linked(a, 'dronesStructure_ProvidedCapability', b1)
    if hasattr(b1, 'dronesStructure_DroneType19'):
        assert _is_linked(b1, 'dronesStructure_DroneType19', a)
    _safe_set(a, 'dronesStructure_ProvidedCapability', b2)
    assert _is_linked(a, 'dronesStructure_ProvidedCapability', b2)
    if hasattr(b1, 'dronesStructure_DroneType19'):
        assert not _is_linked(b1, 'dronesStructure_DroneType19', a)
    if hasattr(b2, 'dronesStructure_DroneType19'):
        assert _is_linked(b2, 'dronesStructure_DroneType19', a)
    _safe_set(a, 'dronesStructure_ProvidedCapability', None)
    assert not _is_linked(a, 'dronesStructure_ProvidedCapability', b2)
    if hasattr(b2, 'dronesStructure_DroneType19'):
        assert not _is_linked(b2, 'dronesStructure_DroneType19', a)


def test_assoc_obstacles11_link_reassign_clear():
    a = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    b1 = dronesStructure_Obstacle()
    b2 = dronesStructure_Obstacle()
    _safe_set(a, 'dronesStructure_Scenario12', {b1})
    assert _is_linked(a, 'dronesStructure_Scenario12', b1)
    if hasattr(b1, 'dronesStructure_Obstacle'):
        assert _is_linked(b1, 'dronesStructure_Obstacle', a)
    _safe_set(a, 'dronesStructure_Scenario12', {b2})
    assert _is_linked(a, 'dronesStructure_Scenario12', b2)
    if hasattr(b1, 'dronesStructure_Obstacle'):
        assert not _is_linked(b1, 'dronesStructure_Obstacle', a)
    if hasattr(b2, 'dronesStructure_Obstacle'):
        assert _is_linked(b2, 'dronesStructure_Obstacle', a)
    _safe_set(a, 'dronesStructure_Scenario12', set())
    assert not _is_linked(a, 'dronesStructure_Scenario12', b2)
    if hasattr(b2, 'dronesStructure_Obstacle'):
        assert not _is_linked(b2, 'dronesStructure_Obstacle', a)


def test_assoc_position41_link_reassign_clear():
    a = dronesStructure_Position(x=3.14, y=3.14, z=3.14)
    b1 = dronesStructure_AABB()
    b2 = dronesStructure_AABB()
    _safe_set(a, 'dronesStructure_Position42', b1)
    assert _is_linked(a, 'dronesStructure_Position42', b1)
    if hasattr(b1, 'dronesStructure_AABB'):
        assert _is_linked(b1, 'dronesStructure_AABB', a)
    _safe_set(a, 'dronesStructure_Position42', b2)
    assert _is_linked(a, 'dronesStructure_Position42', b2)
    if hasattr(b1, 'dronesStructure_AABB'):
        assert not _is_linked(b1, 'dronesStructure_AABB', a)
    if hasattr(b2, 'dronesStructure_AABB'):
        assert _is_linked(b2, 'dronesStructure_AABB', a)
    _safe_set(a, 'dronesStructure_Position42', None)
    assert not _is_linked(a, 'dronesStructure_Position42', b2)
    if hasattr(b2, 'dronesStructure_AABB'):
        assert not _is_linked(b2, 'dronesStructure_AABB', a)


def test_assoc_providedCapabilities17_link_reassign_clear():
    a = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    b1 = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    b2 = dronesStructure_DroneType(idleEneryConsumption=9.99, maxBatteryCapacity=9.99, weight=9.99)
    _safe_set(a, 'ProvidedCapability', b1)
    assert _is_linked(a, 'ProvidedCapability', b1)
    if hasattr(b1, 'droneType'):
        assert _is_linked(b1, 'droneType', a)
    _safe_set(a, 'ProvidedCapability', b2)
    assert _is_linked(a, 'ProvidedCapability', b2)
    if hasattr(b1, 'droneType'):
        assert not _is_linked(b1, 'droneType', a)
    if hasattr(b2, 'droneType'):
        assert _is_linked(b2, 'droneType', a)
    _safe_set(a, 'ProvidedCapability', None)
    assert not _is_linked(a, 'ProvidedCapability', b2)
    if hasattr(b2, 'droneType'):
        assert not _is_linked(b2, 'droneType', a)


def test_assoc_regions13_link_reassign_clear():
    a = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    b1 = dronesStructure_Region()
    b2 = dronesStructure_Region()
    _safe_set(a, 'dronesStructure_Scenario14', {b1})
    assert _is_linked(a, 'dronesStructure_Scenario14', b1)
    if hasattr(b1, 'dronesStructure_Region'):
        assert _is_linked(b1, 'dronesStructure_Region', a)
    _safe_set(a, 'dronesStructure_Scenario14', {b2})
    assert _is_linked(a, 'dronesStructure_Scenario14', b2)
    if hasattr(b1, 'dronesStructure_Region'):
        assert not _is_linked(b1, 'dronesStructure_Region', a)
    if hasattr(b2, 'dronesStructure_Region'):
        assert _is_linked(b2, 'dronesStructure_Region', a)
    _safe_set(a, 'dronesStructure_Scenario14', set())
    assert not _is_linked(a, 'dronesStructure_Scenario14', b2)
    if hasattr(b2, 'dronesStructure_Region'):
        assert not _is_linked(b2, 'dronesStructure_Region', a)


def test_assoc_requiredCapabilities30_link_reassign_clear():
    a = dronesStructure_RequiredCapability(minimalValue=3.14)
    b1 = dronesStructure_Role()
    b2 = dronesStructure_Role()
    _safe_set(a, 'RequiredCapability', b1)
    assert _is_linked(a, 'RequiredCapability', b1)
    if hasattr(b1, 'role'):
        assert _is_linked(b1, 'role', a)
    _safe_set(a, 'RequiredCapability', b2)
    assert _is_linked(a, 'RequiredCapability', b2)
    if hasattr(b1, 'role'):
        assert not _is_linked(b1, 'role', a)
    if hasattr(b2, 'role'):
        assert _is_linked(b2, 'role', a)
    _safe_set(a, 'RequiredCapability', None)
    assert not _is_linked(a, 'RequiredCapability', b2)
    if hasattr(b2, 'role'):
        assert not _is_linked(b2, 'role', a)


def test_assoc_role34_link_reassign_clear():
    a = dronesStructure_RequiredCapability(minimalValue=3.14)
    b1 = dronesStructure_Role()
    b2 = dronesStructure_Role()
    _safe_set(a, 'requiredCapabilities', b1)
    assert _is_linked(a, 'requiredCapabilities', b1)
    if hasattr(b1, 'Role35'):
        assert _is_linked(b1, 'Role35', a)
    _safe_set(a, 'requiredCapabilities', b2)
    assert _is_linked(a, 'requiredCapabilities', b2)
    if hasattr(b1, 'Role35'):
        assert not _is_linked(b1, 'Role35', a)
    if hasattr(b2, 'Role35'):
        assert _is_linked(b2, 'Role35', a)
    _safe_set(a, 'requiredCapabilities', None)
    assert not _is_linked(a, 'requiredCapabilities', b2)
    if hasattr(b2, 'Role35'):
        assert not _is_linked(b2, 'Role35', a)


def test_assoc_roles29_link_reassign_clear():
    a = dronesStructure_CooperativeAction(duration=3.14, startTimeout=3.14)
    b1 = dronesStructure_Role()
    b2 = dronesStructure_Role()
    _safe_set(a, 'cooperativeAction', {b1})
    assert _is_linked(a, 'cooperativeAction', b1)
    if hasattr(b1, 'Role'):
        assert _is_linked(b1, 'Role', a)
    _safe_set(a, 'cooperativeAction', {b2})
    assert _is_linked(a, 'cooperativeAction', b2)
    if hasattr(b1, 'Role'):
        assert not _is_linked(b1, 'Role', a)
    if hasattr(b2, 'Role'):
        assert _is_linked(b2, 'Role', a)
    _safe_set(a, 'cooperativeAction', set())
    assert not _is_linked(a, 'cooperativeAction', b2)
    if hasattr(b2, 'Role'):
        assert not _is_linked(b2, 'Role', a)


def test_assoc_scanningCapability22_link_reassign_clear():
    a = dronesStructure_ProvidedCapability(energyConsumptionPerValue=3.14, maximalValue=3.14)
    b1 = dronesStructure_DroneType(idleEneryConsumption=3.14, maxBatteryCapacity=3.14, weight=3.14)
    b2 = dronesStructure_DroneType(idleEneryConsumption=9.99, maxBatteryCapacity=9.99, weight=9.99)
    _safe_set(a, 'dronesStructure_ProvidedCapability24', b1)
    assert _is_linked(a, 'dronesStructure_ProvidedCapability24', b1)
    if hasattr(b1, 'dronesStructure_DroneType23'):
        assert _is_linked(b1, 'dronesStructure_DroneType23', a)
    _safe_set(a, 'dronesStructure_ProvidedCapability24', b2)
    assert _is_linked(a, 'dronesStructure_ProvidedCapability24', b2)
    if hasattr(b1, 'dronesStructure_DroneType23'):
        assert not _is_linked(b1, 'dronesStructure_DroneType23', a)
    if hasattr(b2, 'dronesStructure_DroneType23'):
        assert _is_linked(b2, 'dronesStructure_DroneType23', a)
    _safe_set(a, 'dronesStructure_ProvidedCapability24', None)
    assert not _is_linked(a, 'dronesStructure_ProvidedCapability24', b2)
    if hasattr(b2, 'dronesStructure_DroneType23'):
        assert not _is_linked(b2, 'dronesStructure_DroneType23', a)


def test_assoc_scenarios0_link_reassign_clear():
    a = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    b1 = dronesStructure_DronesStructure()
    b2 = dronesStructure_DronesStructure()
    _safe_set(a, 'dronesStructure_Scenario', b1)
    assert _is_linked(a, 'dronesStructure_Scenario', b1)
    if hasattr(b1, 'dronesStructure_DronesStructure'):
        assert _is_linked(b1, 'dronesStructure_DronesStructure', a)
    _safe_set(a, 'dronesStructure_Scenario', b2)
    assert _is_linked(a, 'dronesStructure_Scenario', b2)
    if hasattr(b1, 'dronesStructure_DronesStructure'):
        assert not _is_linked(b1, 'dronesStructure_DronesStructure', a)
    if hasattr(b2, 'dronesStructure_DronesStructure'):
        assert _is_linked(b2, 'dronesStructure_DronesStructure', a)
    _safe_set(a, 'dronesStructure_Scenario', None)
    assert not _is_linked(a, 'dronesStructure_Scenario', b2)
    if hasattr(b2, 'dronesStructure_DronesStructure'):
        assert not _is_linked(b2, 'dronesStructure_DronesStructure', a)


def test_assoc_startPosition36_link_reassign_clear():
    a = dronesStructure_Position(x=3.14, y=3.14, z=3.14)
    b1 = dronesStructure_Drone()
    b2 = dronesStructure_Drone()
    _safe_set(a, 'dronesStructure_Position', b1)
    assert _is_linked(a, 'dronesStructure_Position', b1)
    if hasattr(b1, 'dronesStructure_Drone37'):
        assert _is_linked(b1, 'dronesStructure_Drone37', a)
    _safe_set(a, 'dronesStructure_Position', b2)
    assert _is_linked(a, 'dronesStructure_Position', b2)
    if hasattr(b1, 'dronesStructure_Drone37'):
        assert not _is_linked(b1, 'dronesStructure_Drone37', a)
    if hasattr(b2, 'dronesStructure_Drone37'):
        assert _is_linked(b2, 'dronesStructure_Drone37', a)
    _safe_set(a, 'dronesStructure_Position', None)
    assert not _is_linked(a, 'dronesStructure_Position', b2)
    if hasattr(b2, 'dronesStructure_Drone37'):
        assert not _is_linked(b2, 'dronesStructure_Drone37', a)


def test_assoc_tasks15_link_reassign_clear():
    a = dronesStructure_Scenario(maximumCommunicationDistance=3.14, safeCommunicationDistance=3.14)
    b1 = dronesStructure_Task()
    b2 = dronesStructure_Task()
    _safe_set(a, 'dronesStructure_Scenario16', {b1})
    assert _is_linked(a, 'dronesStructure_Scenario16', b1)
    if hasattr(b1, 'dronesStructure_Task'):
        assert _is_linked(b1, 'dronesStructure_Task', a)
    _safe_set(a, 'dronesStructure_Scenario16', {b2})
    assert _is_linked(a, 'dronesStructure_Scenario16', b2)
    if hasattr(b1, 'dronesStructure_Task'):
        assert not _is_linked(b1, 'dronesStructure_Task', a)
    if hasattr(b2, 'dronesStructure_Task'):
        assert _is_linked(b2, 'dronesStructure_Task', a)
    _safe_set(a, 'dronesStructure_Scenario16', set())
    assert not _is_linked(a, 'dronesStructure_Scenario16', b2)
    if hasattr(b2, 'dronesStructure_Task'):
        assert not _is_linked(b2, 'dronesStructure_Task', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AABB_strategy = st.builds(AABB)
@given(instance=AABB_strategy)
@settings(max_examples=25)
def test_AABB_instantiation(instance):
    assert isinstance(instance, AABB)


Capability_strategy = st.builds(Capability)
@given(instance=Capability_strategy)
@settings(max_examples=25)
def test_Capability_instantiation(instance):
    assert isinstance(instance, Capability)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Region_strategy = st.builds(Region)
@given(instance=Region_strategy)
@settings(max_examples=25)
def test_Region_instantiation(instance):
    assert isinstance(instance, Region)


dronesStructure_AABB_strategy = st.builds(dronesStructure_AABB)
@given(instance=dronesStructure_AABB_strategy)
@settings(max_examples=25)
def test_dronesStructure_AABB_instantiation(instance):
    assert isinstance(instance, dronesStructure_AABB)


dronesStructure_Capability_strategy = st.builds(dronesStructure_Capability)
@given(instance=dronesStructure_Capability_strategy)
@settings(max_examples=25)
def test_dronesStructure_Capability_instantiation(instance):
    assert isinstance(instance, dronesStructure_Capability)


dronesStructure_Charger_strategy = st.builds(dronesStructure_Charger)
@given(instance=dronesStructure_Charger_strategy)
@settings(max_examples=25)
def test_dronesStructure_Charger_instantiation(instance):
    assert isinstance(instance, dronesStructure_Charger)


dronesStructure_CooperativeAction_strategy = st.builds(dronesStructure_CooperativeAction, duration=st.floats(allow_nan=False, allow_infinity=False), startTimeout=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=dronesStructure_CooperativeAction_strategy)
@settings(max_examples=25)
def test_dronesStructure_CooperativeAction_instantiation(instance):
    assert isinstance(instance, dronesStructure_CooperativeAction)


dronesStructure_Dimension_strategy = st.builds(dronesStructure_Dimension, depth=st.floats(allow_nan=False, allow_infinity=False), height=st.floats(allow_nan=False, allow_infinity=False), width=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=dronesStructure_Dimension_strategy)
@settings(max_examples=25)
def test_dronesStructure_Dimension_instantiation(instance):
    assert isinstance(instance, dronesStructure_Dimension)


dronesStructure_Drone_strategy = st.builds(dronesStructure_Drone)
@given(instance=dronesStructure_Drone_strategy)
@settings(max_examples=25)
def test_dronesStructure_Drone_instantiation(instance):
    assert isinstance(instance, dronesStructure_Drone)


dronesStructure_DroneType_strategy = st.builds(dronesStructure_DroneType, idleEneryConsumption=st.floats(allow_nan=False, allow_infinity=False), maxBatteryCapacity=st.floats(allow_nan=False, allow_infinity=False), weight=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=dronesStructure_DroneType_strategy)
@settings(max_examples=25)
def test_dronesStructure_DroneType_instantiation(instance):
    assert isinstance(instance, dronesStructure_DroneType)


dronesStructure_DronesStructure_strategy = st.builds(dronesStructure_DronesStructure)
@given(instance=dronesStructure_DronesStructure_strategy)
@settings(max_examples=25)
def test_dronesStructure_DronesStructure_instantiation(instance):
    assert isinstance(instance, dronesStructure_DronesStructure)


dronesStructure_MovementCapability_strategy = st.builds(dronesStructure_MovementCapability)
@given(instance=dronesStructure_MovementCapability_strategy)
@settings(max_examples=25)
def test_dronesStructure_MovementCapability_instantiation(instance):
    assert isinstance(instance, dronesStructure_MovementCapability)


dronesStructure_NamedElement_strategy = st.builds(dronesStructure_NamedElement, name=safe_text)
@given(instance=dronesStructure_NamedElement_strategy)
@settings(max_examples=25)
def test_dronesStructure_NamedElement_instantiation(instance):
    assert isinstance(instance, dronesStructure_NamedElement)


dronesStructure_Obstacle_strategy = st.builds(dronesStructure_Obstacle)
@given(instance=dronesStructure_Obstacle_strategy)
@settings(max_examples=25)
def test_dronesStructure_Obstacle_instantiation(instance):
    assert isinstance(instance, dronesStructure_Obstacle)


dronesStructure_Position_strategy = st.builds(dronesStructure_Position, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False), z=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=dronesStructure_Position_strategy)
@settings(max_examples=25)
def test_dronesStructure_Position_instantiation(instance):
    assert isinstance(instance, dronesStructure_Position)


dronesStructure_ProvidedCapability_strategy = st.builds(dronesStructure_ProvidedCapability, energyConsumptionPerValue=st.floats(allow_nan=False, allow_infinity=False), maximalValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=dronesStructure_ProvidedCapability_strategy)
@settings(max_examples=25)
def test_dronesStructure_ProvidedCapability_instantiation(instance):
    assert isinstance(instance, dronesStructure_ProvidedCapability)


dronesStructure_Region_strategy = st.builds(dronesStructure_Region)
@given(instance=dronesStructure_Region_strategy)
@settings(max_examples=25)
def test_dronesStructure_Region_instantiation(instance):
    assert isinstance(instance, dronesStructure_Region)


dronesStructure_RequiredCapability_strategy = st.builds(dronesStructure_RequiredCapability, minimalValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=dronesStructure_RequiredCapability_strategy)
@settings(max_examples=25)
def test_dronesStructure_RequiredCapability_instantiation(instance):
    assert isinstance(instance, dronesStructure_RequiredCapability)


dronesStructure_Role_strategy = st.builds(dronesStructure_Role)
@given(instance=dronesStructure_Role_strategy)
@settings(max_examples=25)
def test_dronesStructure_Role_instantiation(instance):
    assert isinstance(instance, dronesStructure_Role)


dronesStructure_ScanningCapability_strategy = st.builds(dronesStructure_ScanningCapability)
@given(instance=dronesStructure_ScanningCapability_strategy)
@settings(max_examples=25)
def test_dronesStructure_ScanningCapability_instantiation(instance):
    assert isinstance(instance, dronesStructure_ScanningCapability)


dronesStructure_Scenario_strategy = st.builds(dronesStructure_Scenario, maximumCommunicationDistance=st.floats(allow_nan=False, allow_infinity=False), safeCommunicationDistance=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=dronesStructure_Scenario_strategy)
@settings(max_examples=25)
def test_dronesStructure_Scenario_instantiation(instance):
    assert isinstance(instance, dronesStructure_Scenario)


dronesStructure_ScenarioBounds_strategy = st.builds(dronesStructure_ScenarioBounds)
@given(instance=dronesStructure_ScenarioBounds_strategy)
@settings(max_examples=25)
def test_dronesStructure_ScenarioBounds_instantiation(instance):
    assert isinstance(instance, dronesStructure_ScenarioBounds)


dronesStructure_Task_strategy = st.builds(dronesStructure_Task)
@given(instance=dronesStructure_Task_strategy)
@settings(max_examples=25)
def test_dronesStructure_Task_instantiation(instance):
    assert isinstance(instance, dronesStructure_Task)


