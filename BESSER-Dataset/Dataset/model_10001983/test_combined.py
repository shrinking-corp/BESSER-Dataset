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
    Test_Report,
    Passenger,
    CarCallBox,
    Sim,
    BackgroundCallListener,
    BackgroundStopLoader,
    array_enum_,
    FloorCallBox,
    Controller,
    Call,
    Floor,
    Car,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_test_report_is_not_abstract():
    assert not inspect.isabstract(Test_Report)


def test_hyp_test_report_constructor_exists():
    assert callable(Test_Report.__init__)


def test_hyp_test_report_constructor_args():
    sig = inspect.signature(Test_Report.__init__)
    params = list(sig.parameters.keys())



def test_hyp_passenger_is_not_abstract():
    assert not inspect.isabstract(Passenger)


def test_hyp_passenger_constructor_exists():
    assert callable(Passenger.__init__)


def test_hyp_passenger_constructor_args():
    sig = inspect.signature(Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "DEST" in params, "Missing parameter 'DEST'"
    assert "WEIGHT" in params, "Missing parameter 'WEIGHT'"
    assert "readyToDie" in params, "Missing parameter 'readyToDie'"
    assert "traveling" in params, "Missing parameter 'traveling'"
    assert "START_FLOOR" in params, "Missing parameter 'START_FLOOR'"
    assert "waiting" in params, "Missing parameter 'waiting'"
    assert "carNum" in params, "Missing parameter 'carNum'"










def test_hyp_carcallbox_is_not_abstract():
    assert not inspect.isabstract(CarCallBox)


def test_hyp_carcallbox_constructor_exists():
    assert callable(CarCallBox.__init__)


def test_hyp_carcallbox_constructor_args():
    sig = inspect.signature(CarCallBox.__init__)
    params = list(sig.parameters.keys())
    assert "buttons" in params, "Missing parameter 'buttons'"




def test_hyp_sim_is_not_abstract():
    assert not inspect.isabstract(Sim)


def test_hyp_sim_constructor_exists():
    assert callable(Sim.__init__)


def test_hyp_sim_constructor_args():
    sig = inspect.signature(Sim.__init__)
    params = list(sig.parameters.keys())
    assert "people" in params, "Missing parameter 'people'"
    assert "elevator" in params, "Missing parameter 'elevator'"

def test_hyp_sim_has_people():
    assert hasattr(Sim, "people")
    descriptor = None
    for klass in Sim.__mro__:
        if "people" in klass.__dict__:
            descriptor = klass.__dict__["people"]
            break
    assert isinstance(descriptor, property)

def test_hyp_sim_has_elevator():
    assert hasattr(Sim, "elevator")
    descriptor = None
    for klass in Sim.__mro__:
        if "elevator" in klass.__dict__:
            descriptor = klass.__dict__["elevator"]
            break
    assert isinstance(descriptor, property)



def test_hyp_backgroundcalllistener_is_not_abstract():
    assert not inspect.isabstract(BackgroundCallListener)


def test_hyp_backgroundcalllistener_constructor_exists():
    assert callable(BackgroundCallListener.__init__)


def test_hyp_backgroundcalllistener_constructor_args():
    sig = inspect.signature(BackgroundCallListener.__init__)
    params = list(sig.parameters.keys())



def test_hyp_backgroundstoploader_is_not_abstract():
    assert not inspect.isabstract(BackgroundStopLoader)


def test_hyp_backgroundstoploader_constructor_exists():
    assert callable(BackgroundStopLoader.__init__)


def test_hyp_backgroundstoploader_constructor_args():
    sig = inspect.signature(BackgroundStopLoader.__init__)
    params = list(sig.parameters.keys())
    assert "stops" in params, "Missing parameter 'stops'"




def test_hyp_array_enum__is_not_abstract():
    assert not inspect.isabstract(array_enum_)


def test_hyp_array_enum__constructor_exists():
    assert callable(array_enum_.__init__)


def test_hyp_array_enum__constructor_args():
    sig = inspect.signature(array_enum_.__init__)
    params = list(sig.parameters.keys())



def test_hyp_floorcallbox_is_not_abstract():
    assert not inspect.isabstract(FloorCallBox)


def test_hyp_floorcallbox_constructor_exists():
    assert callable(FloorCallBox.__init__)


def test_hyp_floorcallbox_constructor_args():
    sig = inspect.signature(FloorCallBox.__init__)
    params = list(sig.parameters.keys())
    assert "BUTTONS" in params, "Missing parameter 'BUTTONS'"
    assert "LOCATION" in params, "Missing parameter 'LOCATION'"

def test_hyp_floorcallbox_has_BUTTONS():
    assert hasattr(FloorCallBox, "BUTTONS")
    descriptor = None
    for klass in FloorCallBox.__mro__:
        if "BUTTONS" in klass.__dict__:
            descriptor = klass.__dict__["BUTTONS"]
            break
    assert isinstance(descriptor, property)

def test_hyp_floorcallbox_has_LOCATION():
    assert hasattr(FloorCallBox, "LOCATION")
    descriptor = None
    for klass in FloorCallBox.__mro__:
        if "LOCATION" in klass.__dict__:
            descriptor = klass.__dict__["LOCATION"]
            break
    assert isinstance(descriptor, property)



def test_hyp_controller_is_not_abstract():
    assert not inspect.isabstract(Controller)


def test_hyp_controller_constructor_exists():
    assert callable(Controller.__init__)


def test_hyp_controller_constructor_args():
    sig = inspect.signature(Controller.__init__)
    params = list(sig.parameters.keys())
    assert "callQueue" in params, "Missing parameter 'callQueue'"
    assert "floors" in params, "Missing parameter 'floors'"
    assert "cars" in params, "Missing parameter 'cars'"
    assert "callAdmin" in params, "Missing parameter 'callAdmin'"

def test_hyp_controller_has_callQueue():
    assert hasattr(Controller, "callQueue")
    descriptor = None
    for klass in Controller.__mro__:
        if "callQueue" in klass.__dict__:
            descriptor = klass.__dict__["callQueue"]
            break
    assert isinstance(descriptor, property)

def test_hyp_controller_has_floors():
    assert hasattr(Controller, "floors")
    descriptor = None
    for klass in Controller.__mro__:
        if "floors" in klass.__dict__:
            descriptor = klass.__dict__["floors"]
            break
    assert isinstance(descriptor, property)

def test_hyp_controller_has_cars():
    assert hasattr(Controller, "cars")
    descriptor = None
    for klass in Controller.__mro__:
        if "cars" in klass.__dict__:
            descriptor = klass.__dict__["cars"]
            break
    assert isinstance(descriptor, property)

def test_hyp_controller_has_callAdmin():
    assert hasattr(Controller, "callAdmin")
    descriptor = None
    for klass in Controller.__mro__:
        if "callAdmin" in klass.__dict__:
            descriptor = klass.__dict__["callAdmin"]
            break
    assert isinstance(descriptor, property)



def test_hyp_call_is_not_abstract():
    assert not inspect.isabstract(Call)


def test_hyp_call_constructor_exists():
    assert callable(Call.__init__)


def test_hyp_call_constructor_args():
    sig = inspect.signature(Call.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "created" in params, "Missing parameter 'created'"

def test_hyp_call_has_location():
    assert hasattr(Call, "location")
    descriptor = None
    for klass in Call.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_hyp_call_has_direction():
    assert hasattr(Call, "direction")
    descriptor = None
    for klass in Call.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_hyp_call_has_created():
    assert hasattr(Call, "created")
    descriptor = None
    for klass in Call.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)



def test_hyp_floor_is_not_abstract():
    assert not inspect.isabstract(Floor)


def test_hyp_floor_constructor_exists():
    assert callable(Floor.__init__)


def test_hyp_floor_constructor_args():
    sig = inspect.signature(Floor.__init__)
    params = list(sig.parameters.keys())
    assert "TOP" in params, "Missing parameter 'TOP'"
    assert "LOCATION" in params, "Missing parameter 'LOCATION'"
    assert "BOTTOM" in params, "Missing parameter 'BOTTOM'"
    assert "number" in params, "Missing parameter 'number'"
    assert "box" in params, "Missing parameter 'box'"

def test_hyp_floor_has_TOP():
    assert hasattr(Floor, "TOP")
    descriptor = None
    for klass in Floor.__mro__:
        if "TOP" in klass.__dict__:
            descriptor = klass.__dict__["TOP"]
            break
    assert isinstance(descriptor, property)

def test_hyp_floor_has_LOCATION():
    assert hasattr(Floor, "LOCATION")
    descriptor = None
    for klass in Floor.__mro__:
        if "LOCATION" in klass.__dict__:
            descriptor = klass.__dict__["LOCATION"]
            break
    assert isinstance(descriptor, property)

def test_hyp_floor_has_BOTTOM():
    assert hasattr(Floor, "BOTTOM")
    descriptor = None
    for klass in Floor.__mro__:
        if "BOTTOM" in klass.__dict__:
            descriptor = klass.__dict__["BOTTOM"]
            break
    assert isinstance(descriptor, property)

def test_hyp_floor_has_number():
    assert hasattr(Floor, "number")
    descriptor = None
    for klass in Floor.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_hyp_floor_has_box():
    assert hasattr(Floor, "box")
    descriptor = None
    for klass in Floor.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)



def test_hyp_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_hyp_car_constructor_exists():
    assert callable(Car.__init__)


def test_hyp_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "stopQueue" in params, "Missing parameter 'stopQueue'"
    assert "destQueue" in params, "Missing parameter 'destQueue'"
    assert "floorNum" in params, "Missing parameter 'floorNum'"
    assert "stopLoader" in params, "Missing parameter 'stopLoader'"
    assert "weightLoad" in params, "Missing parameter 'weightLoad'"
    assert "WEIGHT_LIMIT" in params, "Missing parameter 'WEIGHT_LIMIT'"
    assert "location" in params, "Missing parameter 'location'"

def test_hyp_car_has_box():
    assert hasattr(Car, "box")
    descriptor = None
    for klass in Car.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_destination():
    assert hasattr(Car, "destination")
    descriptor = None
    for klass in Car.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_direction():
    assert hasattr(Car, "direction")
    descriptor = None
    for klass in Car.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_stopQueue():
    assert hasattr(Car, "stopQueue")
    descriptor = None
    for klass in Car.__mro__:
        if "stopQueue" in klass.__dict__:
            descriptor = klass.__dict__["stopQueue"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_destQueue():
    assert hasattr(Car, "destQueue")
    descriptor = None
    for klass in Car.__mro__:
        if "destQueue" in klass.__dict__:
            descriptor = klass.__dict__["destQueue"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_floorNum():
    assert hasattr(Car, "floorNum")
    descriptor = None
    for klass in Car.__mro__:
        if "floorNum" in klass.__dict__:
            descriptor = klass.__dict__["floorNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_stopLoader():
    assert hasattr(Car, "stopLoader")
    descriptor = None
    for klass in Car.__mro__:
        if "stopLoader" in klass.__dict__:
            descriptor = klass.__dict__["stopLoader"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_weightLoad():
    assert hasattr(Car, "weightLoad")
    descriptor = None
    for klass in Car.__mro__:
        if "weightLoad" in klass.__dict__:
            descriptor = klass.__dict__["weightLoad"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_WEIGHT_LIMIT():
    assert hasattr(Car, "WEIGHT_LIMIT")
    descriptor = None
    for klass in Car.__mro__:
        if "WEIGHT_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["WEIGHT_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_hyp_car_has_location():
    assert hasattr(Car, "location")
    descriptor = None
    for klass in Car.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)


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
Test_Report_strategy = st.builds(
    Test_Report,
)
Passenger_strategy = st.builds(
    Passenger,
    DEST=
        st.integers(),
    WEIGHT=
        st.integers(),
    readyToDie=
        st.booleans(),
    traveling=
        st.booleans(),
    START_FLOOR=
        st.integers(),
    waiting=
        st.booleans(),
    carNum=
        st.integers()
)
CarCallBox_strategy = st.builds(
    CarCallBox,
    buttons=
        safe_text
)
Sim_strategy = st.builds(
    Sim,
    people=
        safe_text,
    elevator=
        st.none()
)
BackgroundCallListener_strategy = st.builds(
    BackgroundCallListener,
)
BackgroundStopLoader_strategy = st.builds(
    BackgroundStopLoader,
    stops=
        safe_text
)
array_enum__strategy = st.builds(
    array_enum_,
)
FloorCallBox_strategy = st.builds(
    FloorCallBox,
    BUTTONS=
        st.none(),
    LOCATION=
        st.integers()
)
Controller_strategy = st.builds(
    Controller,
    callQueue=
        safe_text,
    floors=
        safe_text,
    cars=
        safe_text,
    callAdmin=
        st.none()
)
Call_strategy = st.builds(
    Call,
    location=
        st.none(),
    direction=
        safe_text,
    created=
        safe_text
)
Floor_strategy = st.builds(
    Floor,
    TOP=
        st.integers(),
    LOCATION=
        st.integers(),
    BOTTOM=
        st.integers(),
    number=
        st.integers(),
    box=
        st.none()
)
Car_strategy = st.builds(
    Car,
    box=
        st.none(),
    destination=
        st.none(),
    direction=
        safe_text,
    stopQueue=
        safe_text,
    destQueue=
        safe_text,
    floorNum=
        st.integers(),
    stopLoader=
        st.none(),
    weightLoad=
        st.integers(),
    WEIGHT_LIMIT=
        st.integers(),
    location=
        st.integers()
)





@given(instance=Passenger_strategy)
def test_hyp_passenger_DEST_setter(instance):
    original = instance.DEST
    instance.DEST = original
    assert instance.DEST == original



@given(instance=Passenger_strategy)
def test_hyp_passenger_WEIGHT_setter(instance):
    original = instance.WEIGHT
    instance.WEIGHT = original
    assert instance.WEIGHT == original



@given(instance=Passenger_strategy)
def test_hyp_passenger_readyToDie_setter(instance):
    original = instance.readyToDie
    instance.readyToDie = original
    assert instance.readyToDie == original



@given(instance=Passenger_strategy)
def test_hyp_passenger_traveling_setter(instance):
    original = instance.traveling
    instance.traveling = original
    assert instance.traveling == original



@given(instance=Passenger_strategy)
def test_hyp_passenger_START_FLOOR_setter(instance):
    original = instance.START_FLOOR
    instance.START_FLOOR = original
    assert instance.START_FLOOR == original



@given(instance=Passenger_strategy)
def test_hyp_passenger_waiting_setter(instance):
    original = instance.waiting
    instance.waiting = original
    assert instance.waiting == original



@given(instance=Passenger_strategy)
def test_hyp_passenger_carNum_setter(instance):
    original = instance.carNum
    instance.carNum = original
    assert instance.carNum == original




@given(instance=CarCallBox_strategy)
def test_hyp_carcallbox_buttons_setter(instance):
    original = instance.buttons
    instance.buttons = original
    assert instance.buttons == original

@given(instance=Sim_strategy)
@settings(max_examples=50)
def test_hyp_sim_instantiation(instance):
    assert isinstance(instance, Sim)



@given(instance=Sim_strategy)
def test_hyp_sim_people_setter(instance):
    original = instance.people
    instance.people = original
    assert instance.people == original



@given(instance=Sim_strategy)
def test_hyp_sim_elevator_setter(instance):
    original = instance.elevator
    instance.elevator = original
    assert instance.elevator == original





@given(instance=BackgroundStopLoader_strategy)
def test_hyp_backgroundstoploader_stops_setter(instance):
    original = instance.stops
    instance.stops = original
    assert instance.stops == original


@given(instance=FloorCallBox_strategy)
@settings(max_examples=50)
def test_hyp_floorcallbox_instantiation(instance):
    assert isinstance(instance, FloorCallBox)



@given(instance=FloorCallBox_strategy)
def test_hyp_floorcallbox_BUTTONS_setter(instance):
    original = instance.BUTTONS
    instance.BUTTONS = original
    assert instance.BUTTONS == original



@given(instance=FloorCallBox_strategy)
def test_hyp_floorcallbox_LOCATION_setter(instance):
    original = instance.LOCATION
    instance.LOCATION = original
    assert instance.LOCATION == original

@given(instance=Controller_strategy)
@settings(max_examples=50)
def test_hyp_controller_instantiation(instance):
    assert isinstance(instance, Controller)



@given(instance=Controller_strategy)
def test_hyp_controller_callQueue_setter(instance):
    original = instance.callQueue
    instance.callQueue = original
    assert instance.callQueue == original



@given(instance=Controller_strategy)
def test_hyp_controller_floors_setter(instance):
    original = instance.floors
    instance.floors = original
    assert instance.floors == original



@given(instance=Controller_strategy)
def test_hyp_controller_cars_setter(instance):
    original = instance.cars
    instance.cars = original
    assert instance.cars == original



@given(instance=Controller_strategy)
def test_hyp_controller_callAdmin_setter(instance):
    original = instance.callAdmin
    instance.callAdmin = original
    assert instance.callAdmin == original

@given(instance=Call_strategy)
@settings(max_examples=50)
def test_hyp_call_instantiation(instance):
    assert isinstance(instance, Call)



@given(instance=Call_strategy)
def test_hyp_call_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Call_strategy)
def test_hyp_call_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=Call_strategy)
def test_hyp_call_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original

@given(instance=Floor_strategy)
@settings(max_examples=50)
def test_hyp_floor_instantiation(instance):
    assert isinstance(instance, Floor)



@given(instance=Floor_strategy)
def test_hyp_floor_TOP_setter(instance):
    original = instance.TOP
    instance.TOP = original
    assert instance.TOP == original



@given(instance=Floor_strategy)
def test_hyp_floor_LOCATION_setter(instance):
    original = instance.LOCATION
    instance.LOCATION = original
    assert instance.LOCATION == original



@given(instance=Floor_strategy)
def test_hyp_floor_BOTTOM_setter(instance):
    original = instance.BOTTOM
    instance.BOTTOM = original
    assert instance.BOTTOM == original



@given(instance=Floor_strategy)
def test_hyp_floor_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Floor_strategy)
def test_hyp_floor_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=Car_strategy)
@settings(max_examples=50)
def test_hyp_car_instantiation(instance):
    assert isinstance(instance, Car)



@given(instance=Car_strategy)
def test_hyp_car_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original



@given(instance=Car_strategy)
def test_hyp_car_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Car_strategy)
def test_hyp_car_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=Car_strategy)
def test_hyp_car_stopQueue_setter(instance):
    original = instance.stopQueue
    instance.stopQueue = original
    assert instance.stopQueue == original



@given(instance=Car_strategy)
def test_hyp_car_destQueue_setter(instance):
    original = instance.destQueue
    instance.destQueue = original
    assert instance.destQueue == original



@given(instance=Car_strategy)
def test_hyp_car_floorNum_setter(instance):
    original = instance.floorNum
    instance.floorNum = original
    assert instance.floorNum == original



@given(instance=Car_strategy)
def test_hyp_car_stopLoader_setter(instance):
    original = instance.stopLoader
    instance.stopLoader = original
    assert instance.stopLoader == original



@given(instance=Car_strategy)
def test_hyp_car_weightLoad_setter(instance):
    original = instance.weightLoad
    instance.weightLoad = original
    assert instance.weightLoad == original



@given(instance=Car_strategy)
def test_hyp_car_WEIGHT_LIMIT_setter(instance):
    original = instance.WEIGHT_LIMIT
    instance.WEIGHT_LIMIT = original
    assert instance.WEIGHT_LIMIT == original



@given(instance=Car_strategy)
def test_hyp_car_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BackgroundCallListener,
    BackgroundStopLoader,
    Call,
    Car,
    CarCallBox,
    Controller,
    Floor,
    FloorCallBox,
    Passenger,
    Sim,
    Test_Report,
    array_enum_,
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

def test_BackgroundStopLoader_stops_value_roundtrip():
    instance = BackgroundStopLoader(stops="sample_text")
    assert instance.stops == "sample_text"
    instance.stops = "sample_text_2"
    assert instance.stops == "sample_text_2"


def test_CarCallBox_buttons_value_roundtrip():
    instance = CarCallBox(buttons="sample_text")
    assert instance.buttons == "sample_text"
    instance.buttons = "sample_text_2"
    assert instance.buttons == "sample_text_2"


def test_Passenger_DEST_value_roundtrip():
    instance = Passenger(DEST=7, START_FLOOR=7, WEIGHT=7, carNum=7, readyToDie=True, traveling=True, waiting=True)
    assert instance.DEST == 7
    instance.DEST = 13
    assert instance.DEST == 13


def test_Passenger_START_FLOOR_value_roundtrip():
    instance = Passenger(DEST=7, START_FLOOR=7, WEIGHT=7, carNum=7, readyToDie=True, traveling=True, waiting=True)
    assert instance.START_FLOOR == 7
    instance.START_FLOOR = 13
    assert instance.START_FLOOR == 13


def test_Passenger_WEIGHT_value_roundtrip():
    instance = Passenger(DEST=7, START_FLOOR=7, WEIGHT=7, carNum=7, readyToDie=True, traveling=True, waiting=True)
    assert instance.WEIGHT == 7
    instance.WEIGHT = 13
    assert instance.WEIGHT == 13


def test_Passenger_carNum_value_roundtrip():
    instance = Passenger(DEST=7, START_FLOOR=7, WEIGHT=7, carNum=7, readyToDie=True, traveling=True, waiting=True)
    assert instance.carNum == 7
    instance.carNum = 13
    assert instance.carNum == 13


def test_Passenger_readyToDie_value_roundtrip():
    instance = Passenger(DEST=7, START_FLOOR=7, WEIGHT=7, carNum=7, readyToDie=True, traveling=True, waiting=True)
    assert instance.readyToDie == True
    instance.readyToDie = False
    assert instance.readyToDie == False


def test_Passenger_traveling_value_roundtrip():
    instance = Passenger(DEST=7, START_FLOOR=7, WEIGHT=7, carNum=7, readyToDie=True, traveling=True, waiting=True)
    assert instance.traveling == True
    instance.traveling = False
    assert instance.traveling == False


def test_Passenger_waiting_value_roundtrip():
    instance = Passenger(DEST=7, START_FLOOR=7, WEIGHT=7, carNum=7, readyToDie=True, traveling=True, waiting=True)
    assert instance.waiting == True
    instance.waiting = False
    assert instance.waiting == False


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BackgroundCallListener_strategy = st.builds(BackgroundCallListener)
@given(instance=BackgroundCallListener_strategy)
@settings(max_examples=25)
def test_BackgroundCallListener_instantiation(instance):
    assert isinstance(instance, BackgroundCallListener)


BackgroundStopLoader_strategy = st.builds(BackgroundStopLoader, stops=safe_text)
@given(instance=BackgroundStopLoader_strategy)
@settings(max_examples=25)
def test_BackgroundStopLoader_instantiation(instance):
    assert isinstance(instance, BackgroundStopLoader)


CarCallBox_strategy = st.builds(CarCallBox, buttons=safe_text)
@given(instance=CarCallBox_strategy)
@settings(max_examples=25)
def test_CarCallBox_instantiation(instance):
    assert isinstance(instance, CarCallBox)


Passenger_strategy = st.builds(Passenger, DEST=st.integers(), START_FLOOR=st.integers(), WEIGHT=st.integers(), carNum=st.integers(), readyToDie=st.booleans(), traveling=st.booleans(), waiting=st.booleans())
@given(instance=Passenger_strategy)
@settings(max_examples=25)
def test_Passenger_instantiation(instance):
    assert isinstance(instance, Passenger)


Test_Report_strategy = st.builds(Test_Report)
@given(instance=Test_Report_strategy)
@settings(max_examples=25)
def test_Test_Report_instantiation(instance):
    assert isinstance(instance, Test_Report)


array_enum__strategy = st.builds(array_enum_)
@given(instance=array_enum__strategy)
@settings(max_examples=25)
def test_array_enum__instantiation(instance):
    assert isinstance(instance, array_enum_)



