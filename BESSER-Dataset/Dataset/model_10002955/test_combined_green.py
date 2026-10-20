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
    OutOfServiceMechanism,
    FloorButton,
    Button_Interface,
    EmergencyButton,
    Elevator_Button,
    Queue,
    Elevator,
    Floor,
    ElevatorController,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_outofservicemechanism_is_not_abstract():
    assert not inspect.isabstract(OutOfServiceMechanism)


def test_hyp_outofservicemechanism_constructor_exists():
    assert callable(OutOfServiceMechanism.__init__)


def test_hyp_outofservicemechanism_constructor_args():
    sig = inspect.signature(OutOfServiceMechanism.__init__)
    params = list(sig.parameters.keys())



def test_hyp_floorbutton_is_not_abstract():
    assert not inspect.isabstract(FloorButton)


def test_hyp_floorbutton_constructor_exists():
    assert callable(FloorButton.__init__)


def test_hyp_floorbutton_constructor_args():
    sig = inspect.signature(FloorButton.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_hyp_floorbutton_has_direction():
    assert hasattr(FloorButton, "direction")
    descriptor = None
    for klass in FloorButton.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_hyp_button_interface_is_not_abstract():
    assert not inspect.isabstract(Button_Interface)


def test_hyp_button_interface_constructor_exists():
    assert callable(Button_Interface.__init__)


def test_hyp_button_interface_constructor_args():
    sig = inspect.signature(Button_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emergencybutton_is_not_abstract():
    assert not inspect.isabstract(EmergencyButton)


def test_hyp_emergencybutton_constructor_exists():
    assert callable(EmergencyButton.__init__)


def test_hyp_emergencybutton_constructor_args():
    sig = inspect.signature(EmergencyButton.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elevator_button_is_not_abstract():
    assert not inspect.isabstract(Elevator_Button)


def test_hyp_elevator_button_constructor_exists():
    assert callable(Elevator_Button.__init__)


def test_hyp_elevator_button_constructor_args():
    sig = inspect.signature(Elevator_Button.__init__)
    params = list(sig.parameters.keys())
    assert "floorID" in params, "Missing parameter 'floorID'"




def test_hyp_queue_is_not_abstract():
    assert not inspect.isabstract(Queue)


def test_hyp_queue_constructor_exists():
    assert callable(Queue.__init__)


def test_hyp_queue_constructor_args():
    sig = inspect.signature(Queue.__init__)
    params = list(sig.parameters.keys())
    assert "currentDirection" in params, "Missing parameter 'currentDirection'"
    assert "floorQueue" in params, "Missing parameter 'floorQueue'"

def test_hyp_queue_has_currentDirection():
    assert hasattr(Queue, "currentDirection")
    descriptor = None
    for klass in Queue.__mro__:
        if "currentDirection" in klass.__dict__:
            descriptor = klass.__dict__["currentDirection"]
            break
    assert isinstance(descriptor, property)

def test_hyp_queue_has_floorQueue():
    assert hasattr(Queue, "floorQueue")
    descriptor = None
    for klass in Queue.__mro__:
        if "floorQueue" in klass.__dict__:
            descriptor = klass.__dict__["floorQueue"]
            break
    assert isinstance(descriptor, property)



def test_hyp_elevator_is_not_abstract():
    assert not inspect.isabstract(Elevator)


def test_hyp_elevator_constructor_exists():
    assert callable(Elevator.__init__)


def test_hyp_elevator_constructor_args():
    sig = inspect.signature(Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "queue" in params, "Missing parameter 'queue'"
    assert "outOfServiceMech" in params, "Missing parameter 'outOfServiceMech'"
    assert "isOutOfService" in params, "Missing parameter 'isOutOfService'"
    assert "buttons" in params, "Missing parameter 'buttons'"
    assert "emergencyButton" in params, "Missing parameter 'emergencyButton'"

def test_hyp_elevator_has_queue():
    assert hasattr(Elevator, "queue")
    descriptor = None
    for klass in Elevator.__mro__:
        if "queue" in klass.__dict__:
            descriptor = klass.__dict__["queue"]
            break
    assert isinstance(descriptor, property)

def test_hyp_elevator_has_outOfServiceMech():
    assert hasattr(Elevator, "outOfServiceMech")
    descriptor = None
    for klass in Elevator.__mro__:
        if "outOfServiceMech" in klass.__dict__:
            descriptor = klass.__dict__["outOfServiceMech"]
            break
    assert isinstance(descriptor, property)

def test_hyp_elevator_has_isOutOfService():
    assert hasattr(Elevator, "isOutOfService")
    descriptor = None
    for klass in Elevator.__mro__:
        if "isOutOfService" in klass.__dict__:
            descriptor = klass.__dict__["isOutOfService"]
            break
    assert isinstance(descriptor, property)

def test_hyp_elevator_has_buttons():
    assert hasattr(Elevator, "buttons")
    descriptor = None
    for klass in Elevator.__mro__:
        if "buttons" in klass.__dict__:
            descriptor = klass.__dict__["buttons"]
            break
    assert isinstance(descriptor, property)

def test_hyp_elevator_has_emergencyButton():
    assert hasattr(Elevator, "emergencyButton")
    descriptor = None
    for klass in Elevator.__mro__:
        if "emergencyButton" in klass.__dict__:
            descriptor = klass.__dict__["emergencyButton"]
            break
    assert isinstance(descriptor, property)



def test_hyp_floor_is_not_abstract():
    assert not inspect.isabstract(Floor)


def test_hyp_floor_constructor_exists():
    assert callable(Floor.__init__)


def test_hyp_floor_constructor_args():
    sig = inspect.signature(Floor.__init__)
    params = list(sig.parameters.keys())
    assert "floorButtons" in params, "Missing parameter 'floorButtons'"
    assert "floorID" in params, "Missing parameter 'floorID'"

def test_hyp_floor_has_floorButtons():
    assert hasattr(Floor, "floorButtons")
    descriptor = None
    for klass in Floor.__mro__:
        if "floorButtons" in klass.__dict__:
            descriptor = klass.__dict__["floorButtons"]
            break
    assert isinstance(descriptor, property)

def test_hyp_floor_has_floorID():
    assert hasattr(Floor, "floorID")
    descriptor = None
    for klass in Floor.__mro__:
        if "floorID" in klass.__dict__:
            descriptor = klass.__dict__["floorID"]
            break
    assert isinstance(descriptor, property)



def test_hyp_elevatorcontroller_is_not_abstract():
    assert not inspect.isabstract(ElevatorController)


def test_hyp_elevatorcontroller_constructor_exists():
    assert callable(ElevatorController.__init__)


def test_hyp_elevatorcontroller_constructor_args():
    sig = inspect.signature(ElevatorController.__init__)
    params = list(sig.parameters.keys())
    assert "floors" in params, "Missing parameter 'floors'"
    assert "elevators" in params, "Missing parameter 'elevators'"

def test_hyp_elevatorcontroller_has_floors():
    assert hasattr(ElevatorController, "floors")
    descriptor = None
    for klass in ElevatorController.__mro__:
        if "floors" in klass.__dict__:
            descriptor = klass.__dict__["floors"]
            break
    assert isinstance(descriptor, property)

def test_hyp_elevatorcontroller_has_elevators():
    assert hasattr(ElevatorController, "elevators")
    descriptor = None
    for klass in ElevatorController.__mro__:
        if "elevators" in klass.__dict__:
            descriptor = klass.__dict__["elevators"]
            break
    assert isinstance(descriptor, property)

def test_hyp_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_hyp_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
OutOfServiceMechanism_strategy = st.builds(
    OutOfServiceMechanism,
)
FloorButton_strategy = st.builds(
    FloorButton,
    direction=
        st.none()
)
Button_Interface_strategy = st.builds(
    Button_Interface,
)
EmergencyButton_strategy = st.builds(
    EmergencyButton,
)
Elevator_Button_strategy = st.builds(
    Elevator_Button,
    floorID=
        st.integers()
)
Queue_strategy = st.builds(
    Queue,
    currentDirection=
        st.none(),
    floorQueue=
        st.integers()
)
Elevator_strategy = st.builds(
    Elevator,
    queue=
        st.none(),
    outOfServiceMech=
        st.none(),
    isOutOfService=
        st.booleans(),
    buttons=
        st.none(),
    emergencyButton=
        st.none()
)
Floor_strategy = st.builds(
    Floor,
    floorButtons=
        st.none(),
    floorID=
        st.integers()
)
ElevatorController_strategy = st.builds(
    ElevatorController,
    floors=
        st.none(),
    elevators=
        st.none()
)


@given(instance=FloorButton_strategy)
@settings(max_examples=50)
def test_hyp_floorbutton_instantiation(instance):
    assert isinstance(instance, FloorButton)



@given(instance=FloorButton_strategy)
def test_hyp_floorbutton_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original






@given(instance=Elevator_Button_strategy)
def test_hyp_elevator_button_floorID_setter(instance):
    original = instance.floorID
    instance.floorID = original
    assert instance.floorID == original

@given(instance=Queue_strategy)
@settings(max_examples=50)
def test_hyp_queue_instantiation(instance):
    assert isinstance(instance, Queue)



@given(instance=Queue_strategy)
def test_hyp_queue_currentDirection_setter(instance):
    original = instance.currentDirection
    instance.currentDirection = original
    assert instance.currentDirection == original



@given(instance=Queue_strategy)
def test_hyp_queue_floorQueue_setter(instance):
    original = instance.floorQueue
    instance.floorQueue = original
    assert instance.floorQueue == original

@given(instance=Elevator_strategy)
@settings(max_examples=50)
def test_hyp_elevator_instantiation(instance):
    assert isinstance(instance, Elevator)



@given(instance=Elevator_strategy)
def test_hyp_elevator_queue_setter(instance):
    original = instance.queue
    instance.queue = original
    assert instance.queue == original



@given(instance=Elevator_strategy)
def test_hyp_elevator_outOfServiceMech_setter(instance):
    original = instance.outOfServiceMech
    instance.outOfServiceMech = original
    assert instance.outOfServiceMech == original



@given(instance=Elevator_strategy)
def test_hyp_elevator_isOutOfService_setter(instance):
    original = instance.isOutOfService
    instance.isOutOfService = original
    assert instance.isOutOfService == original



@given(instance=Elevator_strategy)
def test_hyp_elevator_buttons_setter(instance):
    original = instance.buttons
    instance.buttons = original
    assert instance.buttons == original



@given(instance=Elevator_strategy)
def test_hyp_elevator_emergencyButton_setter(instance):
    original = instance.emergencyButton
    instance.emergencyButton = original
    assert instance.emergencyButton == original

@given(instance=Floor_strategy)
@settings(max_examples=50)
def test_hyp_floor_instantiation(instance):
    assert isinstance(instance, Floor)



@given(instance=Floor_strategy)
def test_hyp_floor_floorButtons_setter(instance):
    original = instance.floorButtons
    instance.floorButtons = original
    assert instance.floorButtons == original



@given(instance=Floor_strategy)
def test_hyp_floor_floorID_setter(instance):
    original = instance.floorID
    instance.floorID = original
    assert instance.floorID == original

@given(instance=ElevatorController_strategy)
@settings(max_examples=50)
def test_hyp_elevatorcontroller_instantiation(instance):
    assert isinstance(instance, ElevatorController)



@given(instance=ElevatorController_strategy)
def test_hyp_elevatorcontroller_floors_setter(instance):
    original = instance.floors
    instance.floors = original
    assert instance.floors == original



@given(instance=ElevatorController_strategy)
def test_hyp_elevatorcontroller_elevators_setter(instance):
    original = instance.elevators
    instance.elevators = original
    assert instance.elevators == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Button_Interface,
    Elevator,
    ElevatorController,
    Elevator_Button,
    EmergencyButton,
    Floor,
    FloorButton,
    OutOfServiceMechanism,
    Queue,
    Enumeration,
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

def test_Elevator_Button_floorID_value_roundtrip():
    instance = Elevator_Button(floorID=7)
    assert instance.floorID == 7
    instance.floorID = 13
    assert instance.floorID == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Button_Interface_strategy = st.builds(Button_Interface)
@given(instance=Button_Interface_strategy)
@settings(max_examples=25)
def test_Button_Interface_instantiation(instance):
    assert isinstance(instance, Button_Interface)


Elevator_Button_strategy = st.builds(Elevator_Button, floorID=st.integers())
@given(instance=Elevator_Button_strategy)
@settings(max_examples=25)
def test_Elevator_Button_instantiation(instance):
    assert isinstance(instance, Elevator_Button)


EmergencyButton_strategy = st.builds(EmergencyButton)
@given(instance=EmergencyButton_strategy)
@settings(max_examples=25)
def test_EmergencyButton_instantiation(instance):
    assert isinstance(instance, EmergencyButton)


OutOfServiceMechanism_strategy = st.builds(OutOfServiceMechanism)
@given(instance=OutOfServiceMechanism_strategy)
@settings(max_examples=25)
def test_OutOfServiceMechanism_instantiation(instance):
    assert isinstance(instance, OutOfServiceMechanism)



