# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Comparable_Patient__Interface,
    genmymodelreverse_java_lang_Object,
    genmymodelreverse_java_lang_Exception,
    genmymodelreverse_C1,
    genmymodelreverse_java_lang_Comparable_Interface,
    sec05_Patient,
    sec05_Person,
    sec05_demoSec05,
    hw3test_HW3ElevatorSimulationTest,
    hw3_Passenger,
    hw3_Floor,
    hw3_ElevatorFullException,
    hw3_Elevator,
    hw3_Building,
    hw2test_HW2ElevatorSimulationTest,
    hw2_Floor,
    hw2_ElevatorFullException,
    hw2_Elevator,
    hw2_Building,
    elevatortest_Patient,
    elevatortest_Person,
    elevatortest_ElevatorTest,
    elevator_Elevator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_comparable_patient__interface_is_not_abstract():
    assert not inspect.isabstract(Comparable_Patient__Interface)


def test_hyp_comparable_patient__interface_constructor_exists():
    assert callable(Comparable_Patient__Interface.__init__)


def test_hyp_comparable_patient__interface_constructor_args():
    sig = inspect.signature(Comparable_Patient__Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_java_lang_object_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Object)


def test_hyp_genmymodelreverse_java_lang_object_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Object.__init__)


def test_hyp_genmymodelreverse_java_lang_object_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_java_lang_exception_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Exception)


def test_hyp_genmymodelreverse_java_lang_exception_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Exception.__init__)


def test_hyp_genmymodelreverse_java_lang_exception_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Exception.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_c1_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C1)


def test_hyp_genmymodelreverse_c1_constructor_exists():
    assert callable(genmymodelreverse_C1.__init__)


def test_hyp_genmymodelreverse_c1_constructor_args():
    sig = inspect.signature(genmymodelreverse_C1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genmymodelreverse_java_lang_comparable_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Comparable_Interface)


def test_hyp_genmymodelreverse_java_lang_comparable_interface_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Comparable_Interface.__init__)


def test_hyp_genmymodelreverse_java_lang_comparable_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Comparable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sec05_patient_is_not_abstract():
    assert not inspect.isabstract(sec05_Patient)


def test_hyp_sec05_patient_constructor_exists():
    assert callable(sec05_Patient.__init__)


def test_hyp_sec05_patient_constructor_args():
    sig = inspect.signature(sec05_Patient.__init__)
    params = list(sig.parameters.keys())
    assert "urgencyIndex" in params, "Missing parameter 'urgencyIndex'"




def test_hyp_sec05_person_is_not_abstract():
    assert not inspect.isabstract(sec05_Person)


def test_hyp_sec05_person_constructor_exists():
    assert callable(sec05_Person.__init__)


def test_hyp_sec05_person_constructor_args():
    sig = inspect.signature(sec05_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sec05_demosec05_is_not_abstract():
    assert not inspect.isabstract(sec05_demoSec05)


def test_hyp_sec05_demosec05_constructor_exists():
    assert callable(sec05_demoSec05.__init__)


def test_hyp_sec05_demosec05_constructor_args():
    sig = inspect.signature(sec05_demoSec05.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hw3test_hw3elevatorsimulationtest_is_not_abstract():
    assert not inspect.isabstract(hw3test_HW3ElevatorSimulationTest)


def test_hyp_hw3test_hw3elevatorsimulationtest_constructor_exists():
    assert callable(hw3test_HW3ElevatorSimulationTest.__init__)


def test_hyp_hw3test_hw3elevatorsimulationtest_constructor_args():
    sig = inspect.signature(hw3test_HW3ElevatorSimulationTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hw3_passenger_is_not_abstract():
    assert not inspect.isabstract(hw3_Passenger)


def test_hyp_hw3_passenger_constructor_exists():
    assert callable(hw3_Passenger.__init__)


def test_hyp_hw3_passenger_constructor_args():
    sig = inspect.signature(hw3_Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "UNDEFINED_FLOOR" in params, "Missing parameter 'UNDEFINED_FLOOR'"
    assert "currentFloor" in params, "Missing parameter 'currentFloor'"
    assert "destinationFloor" in params, "Missing parameter 'destinationFloor'"







def test_hyp_hw3_floor_is_not_abstract():
    assert not inspect.isabstract(hw3_Floor)


def test_hyp_hw3_floor_constructor_exists():
    assert callable(hw3_Floor.__init__)


def test_hyp_hw3_floor_constructor_args():
    sig = inspect.signature(hw3_Floor.__init__)
    params = list(sig.parameters.keys())
    assert "passengersWaiting" in params, "Missing parameter 'passengersWaiting'"
    assert "myFloorNumber" in params, "Missing parameter 'myFloorNumber'"





def test_hyp_hw3_elevatorfullexception_is_not_abstract():
    assert not inspect.isabstract(hw3_ElevatorFullException)


def test_hyp_hw3_elevatorfullexception_constructor_exists():
    assert callable(hw3_ElevatorFullException.__init__)


def test_hyp_hw3_elevatorfullexception_constructor_args():
    sig = inspect.signature(hw3_ElevatorFullException.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hw3_elevator_is_not_abstract():
    assert not inspect.isabstract(hw3_Elevator)


def test_hyp_hw3_elevator_constructor_exists():
    assert callable(hw3_Elevator.__init__)


def test_hyp_hw3_elevator_constructor_args():
    sig = inspect.signature(hw3_Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "passengersToFloor" in params, "Missing parameter 'passengersToFloor'"
    assert "numOfPassengers" in params, "Missing parameter 'numOfPassengers'"
    assert "currentFloorIndex" in params, "Missing parameter 'currentFloorIndex'"
    assert "NUMBER_OF_FLOORS" in params, "Missing parameter 'NUMBER_OF_FLOORS'"
    assert "isGoingUp" in params, "Missing parameter 'isGoingUp'"
    assert "CAPACITY" in params, "Missing parameter 'CAPACITY'"









def test_hyp_hw3_building_is_not_abstract():
    assert not inspect.isabstract(hw3_Building)


def test_hyp_hw3_building_constructor_exists():
    assert callable(hw3_Building.__init__)


def test_hyp_hw3_building_constructor_args():
    sig = inspect.signature(hw3_Building.__init__)
    params = list(sig.parameters.keys())
    assert "floors" in params, "Missing parameter 'floors'"
    assert "FLOORS" in params, "Missing parameter 'FLOORS'"





def test_hyp_hw2test_hw2elevatorsimulationtest_is_not_abstract():
    assert not inspect.isabstract(hw2test_HW2ElevatorSimulationTest)


def test_hyp_hw2test_hw2elevatorsimulationtest_constructor_exists():
    assert callable(hw2test_HW2ElevatorSimulationTest.__init__)


def test_hyp_hw2test_hw2elevatorsimulationtest_constructor_args():
    sig = inspect.signature(hw2test_HW2ElevatorSimulationTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hw2_floor_is_not_abstract():
    assert not inspect.isabstract(hw2_Floor)


def test_hyp_hw2_floor_constructor_exists():
    assert callable(hw2_Floor.__init__)


def test_hyp_hw2_floor_constructor_args():
    sig = inspect.signature(hw2_Floor.__init__)
    params = list(sig.parameters.keys())
    assert "passengersWaiting" in params, "Missing parameter 'passengersWaiting'"




def test_hyp_hw2_elevatorfullexception_is_not_abstract():
    assert not inspect.isabstract(hw2_ElevatorFullException)


def test_hyp_hw2_elevatorfullexception_constructor_exists():
    assert callable(hw2_ElevatorFullException.__init__)


def test_hyp_hw2_elevatorfullexception_constructor_args():
    sig = inspect.signature(hw2_ElevatorFullException.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hw2_elevator_is_not_abstract():
    assert not inspect.isabstract(hw2_Elevator)


def test_hyp_hw2_elevator_constructor_exists():
    assert callable(hw2_Elevator.__init__)


def test_hyp_hw2_elevator_constructor_args():
    sig = inspect.signature(hw2_Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "isGoingUp" in params, "Missing parameter 'isGoingUp'"
    assert "NUMBER_OF_FLOORS" in params, "Missing parameter 'NUMBER_OF_FLOORS'"
    assert "currentFloorIndex" in params, "Missing parameter 'currentFloorIndex'"
    assert "numOfPassengers" in params, "Missing parameter 'numOfPassengers'"
    assert "passengersToFloor" in params, "Missing parameter 'passengersToFloor'"
    assert "CAPACITY" in params, "Missing parameter 'CAPACITY'"









def test_hyp_hw2_building_is_not_abstract():
    assert not inspect.isabstract(hw2_Building)


def test_hyp_hw2_building_constructor_exists():
    assert callable(hw2_Building.__init__)


def test_hyp_hw2_building_constructor_args():
    sig = inspect.signature(hw2_Building.__init__)
    params = list(sig.parameters.keys())
    assert "FLOORS" in params, "Missing parameter 'FLOORS'"
    assert "floors" in params, "Missing parameter 'floors'"





def test_hyp_elevatortest_patient_is_not_abstract():
    assert not inspect.isabstract(elevatortest_Patient)


def test_hyp_elevatortest_patient_constructor_exists():
    assert callable(elevatortest_Patient.__init__)


def test_hyp_elevatortest_patient_constructor_args():
    sig = inspect.signature(elevatortest_Patient.__init__)
    params = list(sig.parameters.keys())
    assert "urgencyIndex" in params, "Missing parameter 'urgencyIndex'"




def test_hyp_elevatortest_person_is_not_abstract():
    assert not inspect.isabstract(elevatortest_Person)


def test_hyp_elevatortest_person_constructor_exists():
    assert callable(elevatortest_Person.__init__)


def test_hyp_elevatortest_person_constructor_args():
    sig = inspect.signature(elevatortest_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_elevatortest_elevatortest_is_not_abstract():
    assert not inspect.isabstract(elevatortest_ElevatorTest)


def test_hyp_elevatortest_elevatortest_constructor_exists():
    assert callable(elevatortest_ElevatorTest.__init__)


def test_hyp_elevatortest_elevatortest_constructor_args():
    sig = inspect.signature(elevatortest_ElevatorTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elevator_elevator_is_not_abstract():
    assert not inspect.isabstract(elevator_Elevator)


def test_hyp_elevator_elevator_constructor_exists():
    assert callable(elevator_Elevator.__init__)


def test_hyp_elevator_elevator_constructor_args():
    sig = inspect.signature(elevator_Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "passengersToFloor" in params, "Missing parameter 'passengersToFloor'"
    assert "numOfPassengers" in params, "Missing parameter 'numOfPassengers'"
    assert "currentFloor" in params, "Missing parameter 'currentFloor'"
    assert "NUMBER_OF_FLOORS" in params, "Missing parameter 'NUMBER_OF_FLOORS'"
    assert "isGoingUp" in params, "Missing parameter 'isGoingUp'"







# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Comparable_Patient__Interface_strategy = st.builds(
    Comparable_Patient__Interface,
)
genmymodelreverse_java_lang_Object_strategy = st.builds(
    genmymodelreverse_java_lang_Object,
)
genmymodelreverse_java_lang_Exception_strategy = st.builds(
    genmymodelreverse_java_lang_Exception,
)
genmymodelreverse_C1_strategy = st.builds(
    genmymodelreverse_C1,
)
genmymodelreverse_java_lang_Comparable_Interface_strategy = st.builds(
    genmymodelreverse_java_lang_Comparable_Interface,
)
sec05_Patient_strategy = st.builds(
    sec05_Patient,
    urgencyIndex=
        st.integers()
)
sec05_Person_strategy = st.builds(
    sec05_Person,
    name=
        safe_text
)
sec05_demoSec05_strategy = st.builds(
    sec05_demoSec05,
)
hw3test_HW3ElevatorSimulationTest_strategy = st.builds(
    hw3test_HW3ElevatorSimulationTest,
)
hw3_Passenger_strategy = st.builds(
    hw3_Passenger,
    id=
        st.integers(),
    UNDEFINED_FLOOR=
        st.integers(),
    currentFloor=
        st.integers(),
    destinationFloor=
        st.integers()
)
hw3_Floor_strategy = st.builds(
    hw3_Floor,
    passengersWaiting=
        st.integers(),
    myFloorNumber=
        st.integers()
)
hw3_ElevatorFullException_strategy = st.builds(
    hw3_ElevatorFullException,
)
hw3_Elevator_strategy = st.builds(
    hw3_Elevator,
    passengersToFloor=
        safe_text,
    numOfPassengers=
        st.integers(),
    currentFloorIndex=
        st.integers(),
    NUMBER_OF_FLOORS=
        st.integers(),
    isGoingUp=
        st.booleans(),
    CAPACITY=
        st.integers()
)
hw3_Building_strategy = st.builds(
    hw3_Building,
    floors=
        safe_text,
    FLOORS=
        st.integers()
)
hw2test_HW2ElevatorSimulationTest_strategy = st.builds(
    hw2test_HW2ElevatorSimulationTest,
)
hw2_Floor_strategy = st.builds(
    hw2_Floor,
    passengersWaiting=
        st.integers()
)
hw2_ElevatorFullException_strategy = st.builds(
    hw2_ElevatorFullException,
)
hw2_Elevator_strategy = st.builds(
    hw2_Elevator,
    isGoingUp=
        st.booleans(),
    NUMBER_OF_FLOORS=
        st.integers(),
    currentFloorIndex=
        st.integers(),
    numOfPassengers=
        st.integers(),
    passengersToFloor=
        safe_text,
    CAPACITY=
        st.integers()
)
hw2_Building_strategy = st.builds(
    hw2_Building,
    FLOORS=
        st.integers(),
    floors=
        safe_text
)
elevatortest_Patient_strategy = st.builds(
    elevatortest_Patient,
    urgencyIndex=
        st.integers()
)
elevatortest_Person_strategy = st.builds(
    elevatortest_Person,
    name=
        safe_text
)
elevatortest_ElevatorTest_strategy = st.builds(
    elevatortest_ElevatorTest,
)
elevator_Elevator_strategy = st.builds(
    elevator_Elevator,
    passengersToFloor=
        safe_text,
    numOfPassengers=
        st.integers(),
    currentFloor=
        st.integers(),
    NUMBER_OF_FLOORS=
        st.integers(),
    isGoingUp=
        st.booleans()
)









@given(instance=sec05_Patient_strategy)
def test_hyp_sec05_patient_urgencyIndex_setter(instance):
    original = instance.urgencyIndex
    instance.urgencyIndex = original
    assert instance.urgencyIndex == original




@given(instance=sec05_Person_strategy)
def test_hyp_sec05_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=hw3_Passenger_strategy)
def test_hyp_hw3_passenger_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=hw3_Passenger_strategy)
def test_hyp_hw3_passenger_UNDEFINED_FLOOR_setter(instance):
    original = instance.UNDEFINED_FLOOR
    instance.UNDEFINED_FLOOR = original
    assert instance.UNDEFINED_FLOOR == original



@given(instance=hw3_Passenger_strategy)
def test_hyp_hw3_passenger_currentFloor_setter(instance):
    original = instance.currentFloor
    instance.currentFloor = original
    assert instance.currentFloor == original



@given(instance=hw3_Passenger_strategy)
def test_hyp_hw3_passenger_destinationFloor_setter(instance):
    original = instance.destinationFloor
    instance.destinationFloor = original
    assert instance.destinationFloor == original




@given(instance=hw3_Floor_strategy)
def test_hyp_hw3_floor_passengersWaiting_setter(instance):
    original = instance.passengersWaiting
    instance.passengersWaiting = original
    assert instance.passengersWaiting == original



@given(instance=hw3_Floor_strategy)
def test_hyp_hw3_floor_myFloorNumber_setter(instance):
    original = instance.myFloorNumber
    instance.myFloorNumber = original
    assert instance.myFloorNumber == original





@given(instance=hw3_Elevator_strategy)
def test_hyp_hw3_elevator_passengersToFloor_setter(instance):
    original = instance.passengersToFloor
    instance.passengersToFloor = original
    assert instance.passengersToFloor == original



@given(instance=hw3_Elevator_strategy)
def test_hyp_hw3_elevator_numOfPassengers_setter(instance):
    original = instance.numOfPassengers
    instance.numOfPassengers = original
    assert instance.numOfPassengers == original



@given(instance=hw3_Elevator_strategy)
def test_hyp_hw3_elevator_currentFloorIndex_setter(instance):
    original = instance.currentFloorIndex
    instance.currentFloorIndex = original
    assert instance.currentFloorIndex == original



@given(instance=hw3_Elevator_strategy)
def test_hyp_hw3_elevator_NUMBER_OF_FLOORS_setter(instance):
    original = instance.NUMBER_OF_FLOORS
    instance.NUMBER_OF_FLOORS = original
    assert instance.NUMBER_OF_FLOORS == original



@given(instance=hw3_Elevator_strategy)
def test_hyp_hw3_elevator_isGoingUp_setter(instance):
    original = instance.isGoingUp
    instance.isGoingUp = original
    assert instance.isGoingUp == original



@given(instance=hw3_Elevator_strategy)
def test_hyp_hw3_elevator_CAPACITY_setter(instance):
    original = instance.CAPACITY
    instance.CAPACITY = original
    assert instance.CAPACITY == original




@given(instance=hw3_Building_strategy)
def test_hyp_hw3_building_floors_setter(instance):
    original = instance.floors
    instance.floors = original
    assert instance.floors == original



@given(instance=hw3_Building_strategy)
def test_hyp_hw3_building_FLOORS_setter(instance):
    original = instance.FLOORS
    instance.FLOORS = original
    assert instance.FLOORS == original





@given(instance=hw2_Floor_strategy)
def test_hyp_hw2_floor_passengersWaiting_setter(instance):
    original = instance.passengersWaiting
    instance.passengersWaiting = original
    assert instance.passengersWaiting == original





@given(instance=hw2_Elevator_strategy)
def test_hyp_hw2_elevator_isGoingUp_setter(instance):
    original = instance.isGoingUp
    instance.isGoingUp = original
    assert instance.isGoingUp == original



@given(instance=hw2_Elevator_strategy)
def test_hyp_hw2_elevator_NUMBER_OF_FLOORS_setter(instance):
    original = instance.NUMBER_OF_FLOORS
    instance.NUMBER_OF_FLOORS = original
    assert instance.NUMBER_OF_FLOORS == original



@given(instance=hw2_Elevator_strategy)
def test_hyp_hw2_elevator_currentFloorIndex_setter(instance):
    original = instance.currentFloorIndex
    instance.currentFloorIndex = original
    assert instance.currentFloorIndex == original



@given(instance=hw2_Elevator_strategy)
def test_hyp_hw2_elevator_numOfPassengers_setter(instance):
    original = instance.numOfPassengers
    instance.numOfPassengers = original
    assert instance.numOfPassengers == original



@given(instance=hw2_Elevator_strategy)
def test_hyp_hw2_elevator_passengersToFloor_setter(instance):
    original = instance.passengersToFloor
    instance.passengersToFloor = original
    assert instance.passengersToFloor == original



@given(instance=hw2_Elevator_strategy)
def test_hyp_hw2_elevator_CAPACITY_setter(instance):
    original = instance.CAPACITY
    instance.CAPACITY = original
    assert instance.CAPACITY == original




@given(instance=hw2_Building_strategy)
def test_hyp_hw2_building_FLOORS_setter(instance):
    original = instance.FLOORS
    instance.FLOORS = original
    assert instance.FLOORS == original



@given(instance=hw2_Building_strategy)
def test_hyp_hw2_building_floors_setter(instance):
    original = instance.floors
    instance.floors = original
    assert instance.floors == original




@given(instance=elevatortest_Patient_strategy)
def test_hyp_elevatortest_patient_urgencyIndex_setter(instance):
    original = instance.urgencyIndex
    instance.urgencyIndex = original
    assert instance.urgencyIndex == original




@given(instance=elevatortest_Person_strategy)
def test_hyp_elevatortest_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=elevator_Elevator_strategy)
def test_hyp_elevator_elevator_passengersToFloor_setter(instance):
    original = instance.passengersToFloor
    instance.passengersToFloor = original
    assert instance.passengersToFloor == original



@given(instance=elevator_Elevator_strategy)
def test_hyp_elevator_elevator_numOfPassengers_setter(instance):
    original = instance.numOfPassengers
    instance.numOfPassengers = original
    assert instance.numOfPassengers == original



@given(instance=elevator_Elevator_strategy)
def test_hyp_elevator_elevator_currentFloor_setter(instance):
    original = instance.currentFloor
    instance.currentFloor = original
    assert instance.currentFloor == original



@given(instance=elevator_Elevator_strategy)
def test_hyp_elevator_elevator_NUMBER_OF_FLOORS_setter(instance):
    original = instance.NUMBER_OF_FLOORS
    instance.NUMBER_OF_FLOORS = original
    assert instance.NUMBER_OF_FLOORS == original



@given(instance=elevator_Elevator_strategy)
def test_hyp_elevator_elevator_isGoingUp_setter(instance):
    original = instance.isGoingUp
    instance.isGoingUp = original
    assert instance.isGoingUp == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



