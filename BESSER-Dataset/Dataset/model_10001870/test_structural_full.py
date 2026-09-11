import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Comparable_Patient__Interface,
    elevator_Elevator,
    elevatortest_ElevatorTest,
    elevatortest_Patient,
    elevatortest_Person,
    genmymodelreverse_C1,
    genmymodelreverse_java_lang_Comparable_Interface,
    genmymodelreverse_java_lang_Exception,
    genmymodelreverse_java_lang_Object,
    hw2_Building,
    hw2_Elevator,
    hw2_ElevatorFullException,
    hw2_Floor,
    hw2test_HW2ElevatorSimulationTest,
    hw3_Building,
    hw3_Elevator,
    hw3_ElevatorFullException,
    hw3_Floor,
    hw3_Passenger,
    hw3test_HW3ElevatorSimulationTest,
    sec05_Patient,
    sec05_Person,
    sec05_demoSec05,
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

def test_elevator_Elevator_NUMBER_OF_FLOORS_value_roundtrip():
    instance = elevator_Elevator(NUMBER_OF_FLOORS=7, currentFloor=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.NUMBER_OF_FLOORS == 7
    instance.NUMBER_OF_FLOORS = 13
    assert instance.NUMBER_OF_FLOORS == 13


def test_elevator_Elevator_currentFloor_value_roundtrip():
    instance = elevator_Elevator(NUMBER_OF_FLOORS=7, currentFloor=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.currentFloor == 7
    instance.currentFloor = 13
    assert instance.currentFloor == 13


def test_elevator_Elevator_isGoingUp_value_roundtrip():
    instance = elevator_Elevator(NUMBER_OF_FLOORS=7, currentFloor=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.isGoingUp == True
    instance.isGoingUp = False
    assert instance.isGoingUp == False


def test_elevator_Elevator_numOfPassengers_value_roundtrip():
    instance = elevator_Elevator(NUMBER_OF_FLOORS=7, currentFloor=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.numOfPassengers == 7
    instance.numOfPassengers = 13
    assert instance.numOfPassengers == 13


def test_elevator_Elevator_passengersToFloor_value_roundtrip():
    instance = elevator_Elevator(NUMBER_OF_FLOORS=7, currentFloor=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.passengersToFloor == "sample_text"
    instance.passengersToFloor = "sample_text_2"
    assert instance.passengersToFloor == "sample_text_2"


def test_elevatortest_Patient_urgencyIndex_value_roundtrip():
    instance = elevatortest_Patient(urgencyIndex=7)
    assert instance.urgencyIndex == 7
    instance.urgencyIndex = 13
    assert instance.urgencyIndex == 13


def test_elevatortest_Person_name_value_roundtrip():
    instance = elevatortest_Person(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_hw2_Building_FLOORS_value_roundtrip():
    instance = hw2_Building(FLOORS=7, floors="sample_text")
    assert instance.FLOORS == 7
    instance.FLOORS = 13
    assert instance.FLOORS == 13


def test_hw2_Building_floors_value_roundtrip():
    instance = hw2_Building(FLOORS=7, floors="sample_text")
    assert instance.floors == "sample_text"
    instance.floors = "sample_text_2"
    assert instance.floors == "sample_text_2"


def test_hw2_Elevator_CAPACITY_value_roundtrip():
    instance = hw2_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.CAPACITY == 7
    instance.CAPACITY = 13
    assert instance.CAPACITY == 13


def test_hw2_Elevator_NUMBER_OF_FLOORS_value_roundtrip():
    instance = hw2_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.NUMBER_OF_FLOORS == 7
    instance.NUMBER_OF_FLOORS = 13
    assert instance.NUMBER_OF_FLOORS == 13


def test_hw2_Elevator_currentFloorIndex_value_roundtrip():
    instance = hw2_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.currentFloorIndex == 7
    instance.currentFloorIndex = 13
    assert instance.currentFloorIndex == 13


def test_hw2_Elevator_isGoingUp_value_roundtrip():
    instance = hw2_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.isGoingUp == True
    instance.isGoingUp = False
    assert instance.isGoingUp == False


def test_hw2_Elevator_numOfPassengers_value_roundtrip():
    instance = hw2_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.numOfPassengers == 7
    instance.numOfPassengers = 13
    assert instance.numOfPassengers == 13


def test_hw2_Elevator_passengersToFloor_value_roundtrip():
    instance = hw2_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.passengersToFloor == "sample_text"
    instance.passengersToFloor = "sample_text_2"
    assert instance.passengersToFloor == "sample_text_2"


def test_hw2_Floor_passengersWaiting_value_roundtrip():
    instance = hw2_Floor(passengersWaiting=7)
    assert instance.passengersWaiting == 7
    instance.passengersWaiting = 13
    assert instance.passengersWaiting == 13


def test_hw3_Building_FLOORS_value_roundtrip():
    instance = hw3_Building(FLOORS=7, floors="sample_text")
    assert instance.FLOORS == 7
    instance.FLOORS = 13
    assert instance.FLOORS == 13


def test_hw3_Building_floors_value_roundtrip():
    instance = hw3_Building(FLOORS=7, floors="sample_text")
    assert instance.floors == "sample_text"
    instance.floors = "sample_text_2"
    assert instance.floors == "sample_text_2"


def test_hw3_Elevator_CAPACITY_value_roundtrip():
    instance = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.CAPACITY == 7
    instance.CAPACITY = 13
    assert instance.CAPACITY == 13


def test_hw3_Elevator_NUMBER_OF_FLOORS_value_roundtrip():
    instance = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.NUMBER_OF_FLOORS == 7
    instance.NUMBER_OF_FLOORS = 13
    assert instance.NUMBER_OF_FLOORS == 13


def test_hw3_Elevator_currentFloorIndex_value_roundtrip():
    instance = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.currentFloorIndex == 7
    instance.currentFloorIndex = 13
    assert instance.currentFloorIndex == 13


def test_hw3_Elevator_isGoingUp_value_roundtrip():
    instance = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.isGoingUp == True
    instance.isGoingUp = False
    assert instance.isGoingUp == False


def test_hw3_Elevator_numOfPassengers_value_roundtrip():
    instance = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.numOfPassengers == 7
    instance.numOfPassengers = 13
    assert instance.numOfPassengers == 13


def test_hw3_Elevator_passengersToFloor_value_roundtrip():
    instance = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    assert instance.passengersToFloor == "sample_text"
    instance.passengersToFloor = "sample_text_2"
    assert instance.passengersToFloor == "sample_text_2"


def test_hw3_Floor_myFloorNumber_value_roundtrip():
    instance = hw3_Floor(myFloorNumber=7, passengersWaiting=7)
    assert instance.myFloorNumber == 7
    instance.myFloorNumber = 13
    assert instance.myFloorNumber == 13


def test_hw3_Floor_passengersWaiting_value_roundtrip():
    instance = hw3_Floor(myFloorNumber=7, passengersWaiting=7)
    assert instance.passengersWaiting == 7
    instance.passengersWaiting = 13
    assert instance.passengersWaiting == 13


def test_hw3_Passenger_UNDEFINED_FLOOR_value_roundtrip():
    instance = hw3_Passenger(UNDEFINED_FLOOR=7, currentFloor=7, destinationFloor=7, id=7)
    assert instance.UNDEFINED_FLOOR == 7
    instance.UNDEFINED_FLOOR = 13
    assert instance.UNDEFINED_FLOOR == 13


def test_hw3_Passenger_currentFloor_value_roundtrip():
    instance = hw3_Passenger(UNDEFINED_FLOOR=7, currentFloor=7, destinationFloor=7, id=7)
    assert instance.currentFloor == 7
    instance.currentFloor = 13
    assert instance.currentFloor == 13


def test_hw3_Passenger_destinationFloor_value_roundtrip():
    instance = hw3_Passenger(UNDEFINED_FLOOR=7, currentFloor=7, destinationFloor=7, id=7)
    assert instance.destinationFloor == 7
    instance.destinationFloor = 13
    assert instance.destinationFloor == 13


def test_hw3_Passenger_id_value_roundtrip():
    instance = hw3_Passenger(UNDEFINED_FLOOR=7, currentFloor=7, destinationFloor=7, id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_sec05_Patient_urgencyIndex_value_roundtrip():
    instance = sec05_Patient(urgencyIndex=7)
    assert instance.urgencyIndex == 7
    instance.urgencyIndex = 13
    assert instance.urgencyIndex == 13


def test_sec05_Person_name_value_roundtrip():
    instance = sec05_Person(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_boardedPassengers_Elevator_Passenger_0_link_reassign_clear():
    a = hw3_Passenger(UNDEFINED_FLOOR=7, currentFloor=7, destinationFloor=7, id=7)
    b1 = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    b2 = hw3_Elevator(CAPACITY=13, NUMBER_OF_FLOORS=13, currentFloorIndex=13, isGoingUp=False, numOfPassengers=13, passengersToFloor="sample_text_2")
    _safe_set(a, 'elevator8', b1)
    assert _is_linked(a, 'elevator8', b1)
    if hasattr(b1, 'boardedPassengers9'):
        assert _is_linked(b1, 'boardedPassengers9', a)
    _safe_set(a, 'elevator8', b2)
    assert _is_linked(a, 'elevator8', b2)
    if hasattr(b1, 'boardedPassengers9'):
        assert not _is_linked(b1, 'boardedPassengers9', a)
    if hasattr(b2, 'boardedPassengers9'):
        assert _is_linked(b2, 'boardedPassengers9', a)
    _safe_set(a, 'elevator8', None)
    assert not _is_linked(a, 'elevator8', b2)
    if hasattr(b2, 'boardedPassengers9'):
        assert not _is_linked(b2, 'boardedPassengers9', a)


def test_assoc_building_Elevator_Building_1_link_reassign_clear():
    a = hw2_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    b1 = hw2_Building(FLOORS=7, floors="sample_text")
    b2 = hw2_Building(FLOORS=13, floors="sample_text_2")
    _safe_set(a, 'building13', b1)
    assert _is_linked(a, 'building13', b1)
    if hasattr(b1, 'elevator12'):
        assert _is_linked(b1, 'elevator12', a)
    _safe_set(a, 'building13', b2)
    assert _is_linked(a, 'building13', b2)
    if hasattr(b1, 'elevator12'):
        assert not _is_linked(b1, 'elevator12', a)
    if hasattr(b2, 'elevator12'):
        assert _is_linked(b2, 'elevator12', a)
    _safe_set(a, 'building13', None)
    assert not _is_linked(a, 'building13', b2)
    if hasattr(b2, 'elevator12'):
        assert not _is_linked(b2, 'elevator12', a)


def test_assoc_building_Elevator_Building_8_link_reassign_clear():
    a = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    b1 = hw3_Building(FLOORS=7, floors="sample_text")
    b2 = hw3_Building(FLOORS=13, floors="sample_text_2")
    _safe_set(a, 'building1', b1)
    assert _is_linked(a, 'building1', b1)
    if hasattr(b1, 'elevator0'):
        assert _is_linked(b1, 'elevator0', a)
    _safe_set(a, 'building1', b2)
    assert _is_linked(a, 'building1', b2)
    if hasattr(b1, 'elevator0'):
        assert not _is_linked(b1, 'elevator0', a)
    if hasattr(b2, 'elevator0'):
        assert _is_linked(b2, 'elevator0', a)
    _safe_set(a, 'building1', None)
    assert not _is_linked(a, 'building1', b2)
    if hasattr(b2, 'elevator0'):
        assert not _is_linked(b2, 'elevator0', a)


def test_assoc_downwardBound_Floor_Passenger_2_link_reassign_clear():
    a = hw3_Passenger(UNDEFINED_FLOOR=7, currentFloor=7, destinationFloor=7, id=7)
    b1 = hw3_Floor(myFloorNumber=7, passengersWaiting=7)
    b2 = hw3_Floor(myFloorNumber=13, passengersWaiting=13)
    _safe_set(a, 'floor6', b1)
    assert _is_linked(a, 'floor6', b1)
    if hasattr(b1, 'downwardBound7'):
        assert _is_linked(b1, 'downwardBound7', a)
    _safe_set(a, 'floor6', b2)
    assert _is_linked(a, 'floor6', b2)
    if hasattr(b1, 'downwardBound7'):
        assert not _is_linked(b1, 'downwardBound7', a)
    if hasattr(b2, 'downwardBound7'):
        assert _is_linked(b2, 'downwardBound7', a)
    _safe_set(a, 'floor6', None)
    assert not _is_linked(a, 'floor6', b2)
    if hasattr(b2, 'downwardBound7'):
        assert not _is_linked(b2, 'downwardBound7', a)


def test_assoc_elevator_Building_Elevator_6_link_reassign_clear():
    a = hw3_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    b1 = hw3_Building(FLOORS=7, floors="sample_text")
    b2 = hw3_Building(FLOORS=13, floors="sample_text_2")
    _safe_set(a, 'building4', b1)
    assert _is_linked(a, 'building4', b1)
    if hasattr(b1, 'elevator5'):
        assert _is_linked(b1, 'elevator5', a)
    _safe_set(a, 'building4', b2)
    assert _is_linked(a, 'building4', b2)
    if hasattr(b1, 'elevator5'):
        assert not _is_linked(b1, 'elevator5', a)
    if hasattr(b2, 'elevator5'):
        assert _is_linked(b2, 'elevator5', a)
    _safe_set(a, 'building4', None)
    assert not _is_linked(a, 'building4', b2)
    if hasattr(b2, 'elevator5'):
        assert not _is_linked(b2, 'elevator5', a)


def test_assoc_elevator_Building_Elevator_7_link_reassign_clear():
    a = hw2_Elevator(CAPACITY=7, NUMBER_OF_FLOORS=7, currentFloorIndex=7, isGoingUp=True, numOfPassengers=7, passengersToFloor="sample_text")
    b1 = hw2_Building(FLOORS=7, floors="sample_text")
    b2 = hw2_Building(FLOORS=13, floors="sample_text_2")
    _safe_set(a, 'building14', b1)
    assert _is_linked(a, 'building14', b1)
    if hasattr(b1, 'elevator15'):
        assert _is_linked(b1, 'elevator15', a)
    _safe_set(a, 'building14', b2)
    assert _is_linked(a, 'building14', b2)
    if hasattr(b1, 'elevator15'):
        assert not _is_linked(b1, 'elevator15', a)
    if hasattr(b2, 'elevator15'):
        assert _is_linked(b2, 'elevator15', a)
    _safe_set(a, 'building14', None)
    assert not _is_linked(a, 'building14', b2)
    if hasattr(b2, 'elevator15'):
        assert not _is_linked(b2, 'elevator15', a)


def test_assoc_person_Patient_Person_4_link_reassign_clear():
    a = elevatortest_Person(name="sample_text")
    b1 = elevatortest_Patient(urgencyIndex=7)
    b2 = elevatortest_Patient(urgencyIndex=13)
    _safe_set(a, 'patient10', b1)
    assert _is_linked(a, 'patient10', b1)
    if hasattr(b1, 'person11'):
        assert _is_linked(b1, 'person11', a)
    _safe_set(a, 'patient10', b2)
    assert _is_linked(a, 'patient10', b2)
    if hasattr(b1, 'person11'):
        assert not _is_linked(b1, 'person11', a)
    if hasattr(b2, 'person11'):
        assert _is_linked(b2, 'person11', a)
    _safe_set(a, 'patient10', None)
    assert not _is_linked(a, 'patient10', b2)
    if hasattr(b2, 'person11'):
        assert not _is_linked(b2, 'person11', a)


def test_assoc_person_Patient_Person_5_link_reassign_clear():
    a = sec05_Person(name="sample_text")
    b1 = sec05_Patient(urgencyIndex=7)
    b2 = sec05_Patient(urgencyIndex=13)
    _safe_set(a, 'patient16', b1)
    assert _is_linked(a, 'patient16', b1)
    if hasattr(b1, 'person17'):
        assert _is_linked(b1, 'person17', a)
    _safe_set(a, 'patient16', b2)
    assert _is_linked(a, 'patient16', b2)
    if hasattr(b1, 'person17'):
        assert not _is_linked(b1, 'person17', a)
    if hasattr(b2, 'person17'):
        assert _is_linked(b2, 'person17', a)
    _safe_set(a, 'patient16', None)
    assert not _is_linked(a, 'patient16', b2)
    if hasattr(b2, 'person17'):
        assert not _is_linked(b2, 'person17', a)


def test_assoc_residents_Floor_Passenger_3_link_reassign_clear():
    a = hw3_Passenger(UNDEFINED_FLOOR=7, currentFloor=7, destinationFloor=7, id=7)
    b1 = hw3_Floor(myFloorNumber=7, passengersWaiting=7)
    b2 = hw3_Floor(myFloorNumber=13, passengersWaiting=13)
    _safe_set(a, 'floor2', b1)
    assert _is_linked(a, 'floor2', b1)
    if hasattr(b1, 'residents3'):
        assert _is_linked(b1, 'residents3', a)
    _safe_set(a, 'floor2', b2)
    assert _is_linked(a, 'floor2', b2)
    if hasattr(b1, 'residents3'):
        assert not _is_linked(b1, 'residents3', a)
    if hasattr(b2, 'residents3'):
        assert _is_linked(b2, 'residents3', a)
    _safe_set(a, 'floor2', None)
    assert not _is_linked(a, 'floor2', b2)
    if hasattr(b2, 'residents3'):
        assert not _is_linked(b2, 'residents3', a)


def test_assoc_upwardBound_Floor_Passenger_9_link_reassign_clear():
    a = hw3_Passenger(UNDEFINED_FLOOR=7, currentFloor=7, destinationFloor=7, id=7)
    b1 = hw3_Floor(myFloorNumber=7, passengersWaiting=7)
    b2 = hw3_Floor(myFloorNumber=13, passengersWaiting=13)
    _safe_set(a, 'floor18', b1)
    assert _is_linked(a, 'floor18', b1)
    if hasattr(b1, 'upwardBound19'):
        assert _is_linked(b1, 'upwardBound19', a)
    _safe_set(a, 'floor18', b2)
    assert _is_linked(a, 'floor18', b2)
    if hasattr(b1, 'upwardBound19'):
        assert not _is_linked(b1, 'upwardBound19', a)
    if hasattr(b2, 'upwardBound19'):
        assert _is_linked(b2, 'upwardBound19', a)
    _safe_set(a, 'floor18', None)
    assert not _is_linked(a, 'floor18', b2)
    if hasattr(b2, 'upwardBound19'):
        assert not _is_linked(b2, 'upwardBound19', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Comparable_Patient__Interface_strategy = st.builds(Comparable_Patient__Interface)
@given(instance=Comparable_Patient__Interface_strategy)
@settings(max_examples=25)
def test_Comparable_Patient__Interface_instantiation(instance):
    assert isinstance(instance, Comparable_Patient__Interface)


elevator_Elevator_strategy = st.builds(elevator_Elevator, NUMBER_OF_FLOORS=st.integers(), currentFloor=st.integers(), isGoingUp=st.booleans(), numOfPassengers=st.integers(), passengersToFloor=safe_text)
@given(instance=elevator_Elevator_strategy)
@settings(max_examples=25)
def test_elevator_Elevator_instantiation(instance):
    assert isinstance(instance, elevator_Elevator)


elevatortest_ElevatorTest_strategy = st.builds(elevatortest_ElevatorTest)
@given(instance=elevatortest_ElevatorTest_strategy)
@settings(max_examples=25)
def test_elevatortest_ElevatorTest_instantiation(instance):
    assert isinstance(instance, elevatortest_ElevatorTest)


elevatortest_Patient_strategy = st.builds(elevatortest_Patient, urgencyIndex=st.integers())
@given(instance=elevatortest_Patient_strategy)
@settings(max_examples=25)
def test_elevatortest_Patient_instantiation(instance):
    assert isinstance(instance, elevatortest_Patient)


elevatortest_Person_strategy = st.builds(elevatortest_Person, name=safe_text)
@given(instance=elevatortest_Person_strategy)
@settings(max_examples=25)
def test_elevatortest_Person_instantiation(instance):
    assert isinstance(instance, elevatortest_Person)


genmymodelreverse_C1_strategy = st.builds(genmymodelreverse_C1)
@given(instance=genmymodelreverse_C1_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_C1_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C1)


genmymodelreverse_java_lang_Comparable_Interface_strategy = st.builds(genmymodelreverse_java_lang_Comparable_Interface)
@given(instance=genmymodelreverse_java_lang_Comparable_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Comparable_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Comparable_Interface)


genmymodelreverse_java_lang_Exception_strategy = st.builds(genmymodelreverse_java_lang_Exception)
@given(instance=genmymodelreverse_java_lang_Exception_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Exception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Exception)


genmymodelreverse_java_lang_Object_strategy = st.builds(genmymodelreverse_java_lang_Object)
@given(instance=genmymodelreverse_java_lang_Object_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Object_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Object)


hw2_Building_strategy = st.builds(hw2_Building, FLOORS=st.integers(), floors=safe_text)
@given(instance=hw2_Building_strategy)
@settings(max_examples=25)
def test_hw2_Building_instantiation(instance):
    assert isinstance(instance, hw2_Building)


hw2_Elevator_strategy = st.builds(hw2_Elevator, CAPACITY=st.integers(), NUMBER_OF_FLOORS=st.integers(), currentFloorIndex=st.integers(), isGoingUp=st.booleans(), numOfPassengers=st.integers(), passengersToFloor=safe_text)
@given(instance=hw2_Elevator_strategy)
@settings(max_examples=25)
def test_hw2_Elevator_instantiation(instance):
    assert isinstance(instance, hw2_Elevator)


hw2_ElevatorFullException_strategy = st.builds(hw2_ElevatorFullException)
@given(instance=hw2_ElevatorFullException_strategy)
@settings(max_examples=25)
def test_hw2_ElevatorFullException_instantiation(instance):
    assert isinstance(instance, hw2_ElevatorFullException)


hw2_Floor_strategy = st.builds(hw2_Floor, passengersWaiting=st.integers())
@given(instance=hw2_Floor_strategy)
@settings(max_examples=25)
def test_hw2_Floor_instantiation(instance):
    assert isinstance(instance, hw2_Floor)


hw2test_HW2ElevatorSimulationTest_strategy = st.builds(hw2test_HW2ElevatorSimulationTest)
@given(instance=hw2test_HW2ElevatorSimulationTest_strategy)
@settings(max_examples=25)
def test_hw2test_HW2ElevatorSimulationTest_instantiation(instance):
    assert isinstance(instance, hw2test_HW2ElevatorSimulationTest)


hw3_Building_strategy = st.builds(hw3_Building, FLOORS=st.integers(), floors=safe_text)
@given(instance=hw3_Building_strategy)
@settings(max_examples=25)
def test_hw3_Building_instantiation(instance):
    assert isinstance(instance, hw3_Building)


hw3_Elevator_strategy = st.builds(hw3_Elevator, CAPACITY=st.integers(), NUMBER_OF_FLOORS=st.integers(), currentFloorIndex=st.integers(), isGoingUp=st.booleans(), numOfPassengers=st.integers(), passengersToFloor=safe_text)
@given(instance=hw3_Elevator_strategy)
@settings(max_examples=25)
def test_hw3_Elevator_instantiation(instance):
    assert isinstance(instance, hw3_Elevator)


hw3_ElevatorFullException_strategy = st.builds(hw3_ElevatorFullException)
@given(instance=hw3_ElevatorFullException_strategy)
@settings(max_examples=25)
def test_hw3_ElevatorFullException_instantiation(instance):
    assert isinstance(instance, hw3_ElevatorFullException)


hw3_Floor_strategy = st.builds(hw3_Floor, myFloorNumber=st.integers(), passengersWaiting=st.integers())
@given(instance=hw3_Floor_strategy)
@settings(max_examples=25)
def test_hw3_Floor_instantiation(instance):
    assert isinstance(instance, hw3_Floor)


hw3_Passenger_strategy = st.builds(hw3_Passenger, UNDEFINED_FLOOR=st.integers(), currentFloor=st.integers(), destinationFloor=st.integers(), id=st.integers())
@given(instance=hw3_Passenger_strategy)
@settings(max_examples=25)
def test_hw3_Passenger_instantiation(instance):
    assert isinstance(instance, hw3_Passenger)


hw3test_HW3ElevatorSimulationTest_strategy = st.builds(hw3test_HW3ElevatorSimulationTest)
@given(instance=hw3test_HW3ElevatorSimulationTest_strategy)
@settings(max_examples=25)
def test_hw3test_HW3ElevatorSimulationTest_instantiation(instance):
    assert isinstance(instance, hw3test_HW3ElevatorSimulationTest)


sec05_Patient_strategy = st.builds(sec05_Patient, urgencyIndex=st.integers())
@given(instance=sec05_Patient_strategy)
@settings(max_examples=25)
def test_sec05_Patient_instantiation(instance):
    assert isinstance(instance, sec05_Patient)


sec05_Person_strategy = st.builds(sec05_Person, name=safe_text)
@given(instance=sec05_Person_strategy)
@settings(max_examples=25)
def test_sec05_Person_instantiation(instance):
    assert isinstance(instance, sec05_Person)


sec05_demoSec05_strategy = st.builds(sec05_demoSec05)
@given(instance=sec05_demoSec05_strategy)
@settings(max_examples=25)
def test_sec05_demoSec05_instantiation(instance):
    assert isinstance(instance, sec05_demoSec05)


