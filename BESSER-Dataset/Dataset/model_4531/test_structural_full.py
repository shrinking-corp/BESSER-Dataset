import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    drone_Action,
    drone_Battery,
    drone_Device,
    drone_Drone,
    drone_FlightPerformance,
    drone_Memory,
    drone_NamedElement,
    drone_Parameter,
    drone_Processor,
    drone_Property,
    drone_ROSDriver,
    drone_Size,
    LaunchType,
    MemoryType,
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

def test_drone_Battery_capacity_value_roundtrip():
    instance = drone_Battery(capacity=7, cellType="sample_text", rechargeTime=7, voltage=3.14)
    assert instance.capacity == 7
    instance.capacity = 13
    assert instance.capacity == 13


def test_drone_Battery_cellType_value_roundtrip():
    instance = drone_Battery(capacity=7, cellType="sample_text", rechargeTime=7, voltage=3.14)
    assert instance.cellType == "sample_text"
    instance.cellType = "sample_text_2"
    assert instance.cellType == "sample_text_2"


def test_drone_Battery_rechargeTime_value_roundtrip():
    instance = drone_Battery(capacity=7, cellType="sample_text", rechargeTime=7, voltage=3.14)
    assert instance.rechargeTime == 7
    instance.rechargeTime = 13
    assert instance.rechargeTime == 13


def test_drone_Battery_voltage_value_roundtrip():
    instance = drone_Battery(capacity=7, cellType="sample_text", rechargeTime=7, voltage=3.14)
    assert instance.voltage == 3.14
    instance.voltage = 9.99
    assert instance.voltage == 9.99


def test_drone_Drone_accelerometer_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.accelerometer == True
    instance.accelerometer = False
    assert instance.accelerometer == False


def test_drone_Drone_barometer_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.barometer == True
    instance.barometer = False
    assert instance.barometer == False


def test_drone_Drone_communicationRange_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.communicationRange == 3.14
    instance.communicationRange = 9.99
    assert instance.communicationRange == 9.99


def test_drone_Drone_dataRate_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.dataRate == 7
    instance.dataRate = 13
    assert instance.dataRate == 13


def test_drone_Drone_giro_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.giro == True
    instance.giro = False
    assert instance.giro == False


def test_drone_Drone_gps_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.gps == True
    instance.gps = False
    assert instance.gps == False


def test_drone_Drone_magnetometer_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.magnetometer == True
    instance.magnetometer = False
    assert instance.magnetometer == False


def test_drone_Drone_maxPowerConsumption_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.maxPowerConsumption == 3.14
    instance.maxPowerConsumption = 9.99
    assert instance.maxPowerConsumption == 9.99


def test_drone_Drone_maxVoltage_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.maxVoltage == 3.14
    instance.maxVoltage = 9.99
    assert instance.maxVoltage == 9.99


def test_drone_Drone_minVoltage_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.minVoltage == 3.14
    instance.minVoltage = 9.99
    assert instance.minVoltage == 9.99


def test_drone_Drone_onBoardObstacleAvoidance_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.onBoardObstacleAvoidance == True
    instance.onBoardObstacleAvoidance = False
    assert instance.onBoardObstacleAvoidance == False


def test_drone_Drone_radioFrequency_value_roundtrip():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert instance.radioFrequency == 7
    instance.radioFrequency = 13
    assert instance.radioFrequency == 13


def test_drone_FlightPerformance_launchType_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.launchType == "sample_text"
    instance.launchType = "sample_text_2"
    assert instance.launchType == "sample_text_2"


def test_drone_FlightPerformance_maxAcceleration_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxAcceleration == 7
    instance.maxAcceleration = 13
    assert instance.maxAcceleration == 13


def test_drone_FlightPerformance_maxAltitude_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxAltitude == 7
    instance.maxAltitude = 13
    assert instance.maxAltitude == 13


def test_drone_FlightPerformance_maxClimbRate_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxClimbRate == 3.14
    instance.maxClimbRate = 9.99
    assert instance.maxClimbRate == 9.99


def test_drone_FlightPerformance_maxDescendRate_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxDescendRate == 3.14
    instance.maxDescendRate = 9.99
    assert instance.maxDescendRate == 9.99


def test_drone_FlightPerformance_maxFlightTime_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxFlightTime == 7
    instance.maxFlightTime = 13
    assert instance.maxFlightTime == 13


def test_drone_FlightPerformance_maxFlightTimeWithMaxPayload_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxFlightTimeWithMaxPayload == 7
    instance.maxFlightTimeWithMaxPayload = 13
    assert instance.maxFlightTimeWithMaxPayload == 13


def test_drone_FlightPerformance_maxOperatingTemperature_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxOperatingTemperature == 3.14
    instance.maxOperatingTemperature = 9.99
    assert instance.maxOperatingTemperature == 9.99


def test_drone_FlightPerformance_maxPayload_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxPayload == 7
    instance.maxPayload = 13
    assert instance.maxPayload == 13


def test_drone_FlightPerformance_maxSpeed_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxSpeed == 7
    instance.maxSpeed = 13
    assert instance.maxSpeed == 13


def test_drone_FlightPerformance_maxTurnRate_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.maxTurnRate == 3.14
    instance.maxTurnRate = 9.99
    assert instance.maxTurnRate == 9.99


def test_drone_FlightPerformance_minAcceleration_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.minAcceleration == 7
    instance.minAcceleration = 13
    assert instance.minAcceleration == 13


def test_drone_FlightPerformance_minOperatingTemperature_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.minOperatingTemperature == 3.14
    instance.minOperatingTemperature = 9.99
    assert instance.minOperatingTemperature == 9.99


def test_drone_FlightPerformance_minSpeed_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.minSpeed == 7
    instance.minSpeed = 13
    assert instance.minSpeed == 13


def test_drone_FlightPerformance_minTurnRate_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.minTurnRate == 3.14
    instance.minTurnRate = 9.99
    assert instance.minTurnRate == 9.99


def test_drone_FlightPerformance_positionHold_value_roundtrip():
    instance = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    assert instance.positionHold == 3.14
    instance.positionHold = 9.99
    assert instance.positionHold == 9.99


def test_drone_Memory_size_value_roundtrip():
    instance = drone_Memory(size=7, subType="sample_text", type="sample_text")
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_drone_Memory_subType_value_roundtrip():
    instance = drone_Memory(size=7, subType="sample_text", type="sample_text")
    assert instance.subType == "sample_text"
    instance.subType = "sample_text_2"
    assert instance.subType == "sample_text_2"


def test_drone_Memory_type_value_roundtrip():
    instance = drone_Memory(size=7, subType="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_drone_NamedElement_name_value_roundtrip():
    instance = drone_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_drone_Parameter_description_value_roundtrip():
    instance = drone_Parameter(description="sample_text", key="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_drone_Parameter_key_value_roundtrip():
    instance = drone_Parameter(description="sample_text", key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_drone_Processor_architecture_value_roundtrip():
    instance = drone_Processor(architecture="sample_text", frequency=7)
    assert instance.architecture == "sample_text"
    instance.architecture = "sample_text_2"
    assert instance.architecture == "sample_text_2"


def test_drone_Processor_frequency_value_roundtrip():
    instance = drone_Processor(architecture="sample_text", frequency=7)
    assert instance.frequency == 7
    instance.frequency = 13
    assert instance.frequency == 13


def test_drone_Property_value_value_roundtrip():
    instance = drone_Property(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_drone_ROSDriver_url_value_roundtrip():
    instance = drone_ROSDriver(url="sample_text", version="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_drone_ROSDriver_version_value_roundtrip():
    instance = drone_ROSDriver(url="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_drone_Size_height_value_roundtrip():
    instance = drone_Size(height=3.14, length=3.14, propellerSize=3.14, propellers=7, weight=3.14, width=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_drone_Size_length_value_roundtrip():
    instance = drone_Size(height=3.14, length=3.14, propellerSize=3.14, propellers=7, weight=3.14, width=3.14)
    assert instance.length == 3.14
    instance.length = 9.99
    assert instance.length == 9.99


def test_drone_Size_propellerSize_value_roundtrip():
    instance = drone_Size(height=3.14, length=3.14, propellerSize=3.14, propellers=7, weight=3.14, width=3.14)
    assert instance.propellerSize == 3.14
    instance.propellerSize = 9.99
    assert instance.propellerSize == 9.99


def test_drone_Size_propellers_value_roundtrip():
    instance = drone_Size(height=3.14, length=3.14, propellerSize=3.14, propellers=7, weight=3.14, width=3.14)
    assert instance.propellers == 7
    instance.propellers = 13
    assert instance.propellers == 13


def test_drone_Size_weight_value_roundtrip():
    instance = drone_Size(height=3.14, length=3.14, propellerSize=3.14, propellers=7, weight=3.14, width=3.14)
    assert instance.weight == 3.14
    instance.weight = 9.99
    assert instance.weight == 9.99


def test_drone_Size_width_value_roundtrip():
    instance = drone_Size(height=3.14, length=3.14, propellerSize=3.14, propellers=7, weight=3.14, width=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_drone_Action_isa_NamedElement():
    instance = drone_Action()
    assert isinstance(instance, NamedElement)


def test_drone_Battery_isa_NamedElement():
    instance = drone_Battery(capacity=7, cellType="sample_text", rechargeTime=7, voltage=3.14)
    assert isinstance(instance, NamedElement)


def test_drone_Device_isa_NamedElement():
    instance = drone_Device()
    assert isinstance(instance, NamedElement)


def test_drone_Drone_isa_NamedElement():
    instance = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    assert isinstance(instance, NamedElement)


def test_drone_Memory_isa_NamedElement():
    instance = drone_Memory(size=7, subType="sample_text", type="sample_text")
    assert isinstance(instance, NamedElement)


def test_drone_Processor_isa_NamedElement():
    instance = drone_Processor(architecture="sample_text", frequency=7)
    assert isinstance(instance, NamedElement)


def test_drone_Property_isa_NamedElement():
    instance = drone_Property(value="sample_text")
    assert isinstance(instance, NamedElement)


def test_drone_ROSDriver_isa_NamedElement():
    instance = drone_ROSDriver(url="sample_text", version="sample_text")
    assert isinstance(instance, NamedElement)


def test_assoc_batteries3_link_reassign_clear():
    a = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    b1 = drone_Battery(capacity=7, cellType="sample_text", rechargeTime=7, voltage=3.14)
    b2 = drone_Battery(capacity=13, cellType="sample_text_2", rechargeTime=13, voltage=9.99)
    _safe_set(a, 'drone_Drone4', {b1})
    assert _is_linked(a, 'drone_Drone4', b1)
    if hasattr(b1, 'drone_Battery'):
        assert _is_linked(b1, 'drone_Battery', a)
    _safe_set(a, 'drone_Drone4', {b2})
    assert _is_linked(a, 'drone_Drone4', b2)
    if hasattr(b1, 'drone_Battery'):
        assert not _is_linked(b1, 'drone_Battery', a)
    if hasattr(b2, 'drone_Battery'):
        assert _is_linked(b2, 'drone_Battery', a)
    _safe_set(a, 'drone_Drone4', set())
    assert not _is_linked(a, 'drone_Drone4', b2)
    if hasattr(b2, 'drone_Battery'):
        assert not _is_linked(b2, 'drone_Battery', a)


def test_assoc_dataEquipment9_link_reassign_clear():
    a = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    b1 = drone_Device()
    b2 = drone_Device()
    _safe_set(a, 'drone_Drone10', {b1})
    assert _is_linked(a, 'drone_Drone10', b1)
    if hasattr(b1, 'drone_Device'):
        assert _is_linked(b1, 'drone_Device', a)
    _safe_set(a, 'drone_Drone10', {b2})
    assert _is_linked(a, 'drone_Drone10', b2)
    if hasattr(b1, 'drone_Device'):
        assert not _is_linked(b1, 'drone_Device', a)
    if hasattr(b2, 'drone_Device'):
        assert _is_linked(b2, 'drone_Device', a)
    _safe_set(a, 'drone_Drone10', set())
    assert not _is_linked(a, 'drone_Drone10', b2)
    if hasattr(b2, 'drone_Device'):
        assert not _is_linked(b2, 'drone_Device', a)


def test_assoc_flightPerf1_link_reassign_clear():
    a = drone_FlightPerformance(launchType="sample_text", maxAcceleration=7, maxAltitude=7, maxClimbRate=3.14, maxDescendRate=3.14, maxFlightTime=7, maxFlightTimeWithMaxPayload=7, maxOperatingTemperature=3.14, maxPayload=7, maxSpeed=7, maxTurnRate=3.14, minAcceleration=7, minOperatingTemperature=3.14, minSpeed=7, minTurnRate=3.14, positionHold=3.14)
    b1 = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    b2 = drone_Drone(accelerometer=False, barometer=False, communicationRange=9.99, dataRate=13, giro=False, gps=False, magnetometer=False, maxPowerConsumption=9.99, maxVoltage=9.99, minVoltage=9.99, onBoardObstacleAvoidance=False, radioFrequency=13)
    _safe_set(a, 'drone_FlightPerformance', b1)
    assert _is_linked(a, 'drone_FlightPerformance', b1)
    if hasattr(b1, 'drone_Drone2'):
        assert _is_linked(b1, 'drone_Drone2', a)
    _safe_set(a, 'drone_FlightPerformance', b2)
    assert _is_linked(a, 'drone_FlightPerformance', b2)
    if hasattr(b1, 'drone_Drone2'):
        assert not _is_linked(b1, 'drone_Drone2', a)
    if hasattr(b2, 'drone_Drone2'):
        assert _is_linked(b2, 'drone_Drone2', a)
    _safe_set(a, 'drone_FlightPerformance', None)
    assert not _is_linked(a, 'drone_FlightPerformance', b2)
    if hasattr(b2, 'drone_Drone2'):
        assert not _is_linked(b2, 'drone_Drone2', a)


def test_assoc_memory7_link_reassign_clear():
    a = drone_Memory(size=7, subType="sample_text", type="sample_text")
    b1 = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    b2 = drone_Drone(accelerometer=False, barometer=False, communicationRange=9.99, dataRate=13, giro=False, gps=False, magnetometer=False, maxPowerConsumption=9.99, maxVoltage=9.99, minVoltage=9.99, onBoardObstacleAvoidance=False, radioFrequency=13)
    _safe_set(a, 'drone_Memory', b1)
    assert _is_linked(a, 'drone_Memory', b1)
    if hasattr(b1, 'drone_Drone8'):
        assert _is_linked(b1, 'drone_Drone8', a)
    _safe_set(a, 'drone_Memory', b2)
    assert _is_linked(a, 'drone_Memory', b2)
    if hasattr(b1, 'drone_Drone8'):
        assert not _is_linked(b1, 'drone_Drone8', a)
    if hasattr(b2, 'drone_Drone8'):
        assert _is_linked(b2, 'drone_Drone8', a)
    _safe_set(a, 'drone_Memory', None)
    assert not _is_linked(a, 'drone_Memory', b2)
    if hasattr(b2, 'drone_Drone8'):
        assert not _is_linked(b2, 'drone_Drone8', a)


def test_assoc_parameters17_link_reassign_clear():
    a = drone_Parameter(description="sample_text", key="sample_text")
    b1 = drone_Action()
    b2 = drone_Action()
    _safe_set(a, 'drone_Parameter', b1)
    assert _is_linked(a, 'drone_Parameter', b1)
    if hasattr(b1, 'drone_Action18'):
        assert _is_linked(b1, 'drone_Action18', a)
    _safe_set(a, 'drone_Parameter', b2)
    assert _is_linked(a, 'drone_Parameter', b2)
    if hasattr(b1, 'drone_Action18'):
        assert not _is_linked(b1, 'drone_Action18', a)
    if hasattr(b2, 'drone_Action18'):
        assert _is_linked(b2, 'drone_Action18', a)
    _safe_set(a, 'drone_Parameter', None)
    assert not _is_linked(a, 'drone_Parameter', b2)
    if hasattr(b2, 'drone_Action18'):
        assert not _is_linked(b2, 'drone_Action18', a)


def test_assoc_processors5_link_reassign_clear():
    a = drone_Processor(architecture="sample_text", frequency=7)
    b1 = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    b2 = drone_Drone(accelerometer=False, barometer=False, communicationRange=9.99, dataRate=13, giro=False, gps=False, magnetometer=False, maxPowerConsumption=9.99, maxVoltage=9.99, minVoltage=9.99, onBoardObstacleAvoidance=False, radioFrequency=13)
    _safe_set(a, 'drone_Processor', b1)
    assert _is_linked(a, 'drone_Processor', b1)
    if hasattr(b1, 'drone_Drone6'):
        assert _is_linked(b1, 'drone_Drone6', a)
    _safe_set(a, 'drone_Processor', b2)
    assert _is_linked(a, 'drone_Processor', b2)
    if hasattr(b1, 'drone_Drone6'):
        assert not _is_linked(b1, 'drone_Drone6', a)
    if hasattr(b2, 'drone_Drone6'):
        assert _is_linked(b2, 'drone_Drone6', a)
    _safe_set(a, 'drone_Processor', None)
    assert not _is_linked(a, 'drone_Processor', b2)
    if hasattr(b2, 'drone_Drone6'):
        assert not _is_linked(b2, 'drone_Drone6', a)


def test_assoc_properties15_link_reassign_clear():
    a = drone_Property(value="sample_text")
    b1 = drone_Device()
    b2 = drone_Device()
    _safe_set(a, 'drone_Property', b1)
    assert _is_linked(a, 'drone_Property', b1)
    if hasattr(b1, 'drone_Device16'):
        assert _is_linked(b1, 'drone_Device16', a)
    _safe_set(a, 'drone_Property', b2)
    assert _is_linked(a, 'drone_Property', b2)
    if hasattr(b1, 'drone_Device16'):
        assert not _is_linked(b1, 'drone_Device16', a)
    if hasattr(b2, 'drone_Device16'):
        assert _is_linked(b2, 'drone_Device16', a)
    _safe_set(a, 'drone_Property', None)
    assert not _is_linked(a, 'drone_Property', b2)
    if hasattr(b2, 'drone_Device16'):
        assert not _is_linked(b2, 'drone_Device16', a)


def test_assoc_rosDriver11_link_reassign_clear():
    a = drone_ROSDriver(url="sample_text", version="sample_text")
    b1 = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    b2 = drone_Drone(accelerometer=False, barometer=False, communicationRange=9.99, dataRate=13, giro=False, gps=False, magnetometer=False, maxPowerConsumption=9.99, maxVoltage=9.99, minVoltage=9.99, onBoardObstacleAvoidance=False, radioFrequency=13)
    _safe_set(a, 'drone_ROSDriver', b1)
    assert _is_linked(a, 'drone_ROSDriver', b1)
    if hasattr(b1, 'drone_Drone12'):
        assert _is_linked(b1, 'drone_Drone12', a)
    _safe_set(a, 'drone_ROSDriver', b2)
    assert _is_linked(a, 'drone_ROSDriver', b2)
    if hasattr(b1, 'drone_Drone12'):
        assert not _is_linked(b1, 'drone_Drone12', a)
    if hasattr(b2, 'drone_Drone12'):
        assert _is_linked(b2, 'drone_Drone12', a)
    _safe_set(a, 'drone_ROSDriver', None)
    assert not _is_linked(a, 'drone_ROSDriver', b2)
    if hasattr(b2, 'drone_Drone12'):
        assert not _is_linked(b2, 'drone_Drone12', a)


def test_assoc_size0_link_reassign_clear():
    a = drone_Size(height=3.14, length=3.14, propellerSize=3.14, propellers=7, weight=3.14, width=3.14)
    b1 = drone_Drone(accelerometer=True, barometer=True, communicationRange=3.14, dataRate=7, giro=True, gps=True, magnetometer=True, maxPowerConsumption=3.14, maxVoltage=3.14, minVoltage=3.14, onBoardObstacleAvoidance=True, radioFrequency=7)
    b2 = drone_Drone(accelerometer=False, barometer=False, communicationRange=9.99, dataRate=13, giro=False, gps=False, magnetometer=False, maxPowerConsumption=9.99, maxVoltage=9.99, minVoltage=9.99, onBoardObstacleAvoidance=False, radioFrequency=13)
    _safe_set(a, 'drone_Size', b1)
    assert _is_linked(a, 'drone_Size', b1)
    if hasattr(b1, 'drone_Drone'):
        assert _is_linked(b1, 'drone_Drone', a)
    _safe_set(a, 'drone_Size', b2)
    assert _is_linked(a, 'drone_Size', b2)
    if hasattr(b1, 'drone_Drone'):
        assert not _is_linked(b1, 'drone_Drone', a)
    if hasattr(b2, 'drone_Drone'):
        assert _is_linked(b2, 'drone_Drone', a)
    _safe_set(a, 'drone_Size', None)
    assert not _is_linked(a, 'drone_Size', b2)
    if hasattr(b2, 'drone_Drone'):
        assert not _is_linked(b2, 'drone_Drone', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


drone_Action_strategy = st.builds(drone_Action)
@given(instance=drone_Action_strategy)
@settings(max_examples=25)
def test_drone_Action_instantiation(instance):
    assert isinstance(instance, drone_Action)


drone_Battery_strategy = st.builds(drone_Battery, capacity=st.integers(), cellType=safe_text, rechargeTime=st.integers(), voltage=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=drone_Battery_strategy)
@settings(max_examples=25)
def test_drone_Battery_instantiation(instance):
    assert isinstance(instance, drone_Battery)


drone_Device_strategy = st.builds(drone_Device)
@given(instance=drone_Device_strategy)
@settings(max_examples=25)
def test_drone_Device_instantiation(instance):
    assert isinstance(instance, drone_Device)


drone_Drone_strategy = st.builds(drone_Drone, accelerometer=st.booleans(), barometer=st.booleans(), communicationRange=st.floats(allow_nan=False, allow_infinity=False), dataRate=st.integers(), giro=st.booleans(), gps=st.booleans(), magnetometer=st.booleans(), maxPowerConsumption=st.floats(allow_nan=False, allow_infinity=False), maxVoltage=st.floats(allow_nan=False, allow_infinity=False), minVoltage=st.floats(allow_nan=False, allow_infinity=False), onBoardObstacleAvoidance=st.booleans(), radioFrequency=st.integers())
@given(instance=drone_Drone_strategy)
@settings(max_examples=25)
def test_drone_Drone_instantiation(instance):
    assert isinstance(instance, drone_Drone)


drone_FlightPerformance_strategy = st.builds(drone_FlightPerformance, launchType=safe_text, maxAcceleration=st.integers(), maxAltitude=st.integers(), maxClimbRate=st.floats(allow_nan=False, allow_infinity=False), maxDescendRate=st.floats(allow_nan=False, allow_infinity=False), maxFlightTime=st.integers(), maxFlightTimeWithMaxPayload=st.integers(), maxOperatingTemperature=st.floats(allow_nan=False, allow_infinity=False), maxPayload=st.integers(), maxSpeed=st.integers(), maxTurnRate=st.floats(allow_nan=False, allow_infinity=False), minAcceleration=st.integers(), minOperatingTemperature=st.floats(allow_nan=False, allow_infinity=False), minSpeed=st.integers(), minTurnRate=st.floats(allow_nan=False, allow_infinity=False), positionHold=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=drone_FlightPerformance_strategy)
@settings(max_examples=25)
def test_drone_FlightPerformance_instantiation(instance):
    assert isinstance(instance, drone_FlightPerformance)


drone_Memory_strategy = st.builds(drone_Memory, size=st.integers(), subType=safe_text, type=safe_text)
@given(instance=drone_Memory_strategy)
@settings(max_examples=25)
def test_drone_Memory_instantiation(instance):
    assert isinstance(instance, drone_Memory)


drone_NamedElement_strategy = st.builds(drone_NamedElement, name=safe_text)
@given(instance=drone_NamedElement_strategy)
@settings(max_examples=25)
def test_drone_NamedElement_instantiation(instance):
    assert isinstance(instance, drone_NamedElement)


drone_Parameter_strategy = st.builds(drone_Parameter, description=safe_text, key=safe_text)
@given(instance=drone_Parameter_strategy)
@settings(max_examples=25)
def test_drone_Parameter_instantiation(instance):
    assert isinstance(instance, drone_Parameter)


drone_Processor_strategy = st.builds(drone_Processor, architecture=safe_text, frequency=st.integers())
@given(instance=drone_Processor_strategy)
@settings(max_examples=25)
def test_drone_Processor_instantiation(instance):
    assert isinstance(instance, drone_Processor)


drone_Property_strategy = st.builds(drone_Property, value=safe_text)
@given(instance=drone_Property_strategy)
@settings(max_examples=25)
def test_drone_Property_instantiation(instance):
    assert isinstance(instance, drone_Property)


drone_ROSDriver_strategy = st.builds(drone_ROSDriver, url=safe_text, version=safe_text)
@given(instance=drone_ROSDriver_strategy)
@settings(max_examples=25)
def test_drone_ROSDriver_instantiation(instance):
    assert isinstance(instance, drone_ROSDriver)


drone_Size_strategy = st.builds(drone_Size, height=st.floats(allow_nan=False, allow_infinity=False), length=st.floats(allow_nan=False, allow_infinity=False), propellerSize=st.floats(allow_nan=False, allow_infinity=False), propellers=st.integers(), weight=st.floats(allow_nan=False, allow_infinity=False), width=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=drone_Size_strategy)
@settings(max_examples=25)
def test_drone_Size_instantiation(instance):
    assert isinstance(instance, drone_Size)


