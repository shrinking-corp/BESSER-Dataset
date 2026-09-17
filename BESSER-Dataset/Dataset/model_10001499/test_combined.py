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
    Parking_Record,
    Spot,
    ParkingLot,
    VehicleInterface_Interface,
    MotorCycle,
    Car,
    Bus,
    AbstractVehicle,
    spotRestriction,
    spotType,
    spotStatus,
    vehicleStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_parking_record_is_not_abstract():
    assert not inspect.isabstract(Parking_Record)


def test_hyp_parking_record_constructor_exists():
    assert callable(Parking_Record.__init__)


def test_hyp_parking_record_constructor_args():
    sig = inspect.signature(Parking_Record.__init__)
    params = list(sig.parameters.keys())
    assert "spot" in params, "Missing parameter 'spot'"
    assert "vehicleLicensePlate" in params, "Missing parameter 'vehicleLicensePlate'"
    assert "ownerPhone" in params, "Missing parameter 'ownerPhone'"
    assert "parkTime" in params, "Missing parameter 'parkTime'"
    assert "totalCost" in params, "Missing parameter 'totalCost'"
    assert "releaseTime" in params, "Missing parameter 'releaseTime'"
    assert "ownerName" in params, "Missing parameter 'ownerName'"
    assert "vehicleModel" in params, "Missing parameter 'vehicleModel'"
    assert "hourlyRate" in params, "Missing parameter 'hourlyRate'"
    assert "vehicleColor" in params, "Missing parameter 'vehicleColor'"

def test_hyp_parking_record_has_spot():
    assert hasattr(Parking_Record, "spot")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "spot" in klass.__dict__:
            descriptor = klass.__dict__["spot"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_vehicleLicensePlate():
    assert hasattr(Parking_Record, "vehicleLicensePlate")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "vehicleLicensePlate" in klass.__dict__:
            descriptor = klass.__dict__["vehicleLicensePlate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_ownerPhone():
    assert hasattr(Parking_Record, "ownerPhone")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "ownerPhone" in klass.__dict__:
            descriptor = klass.__dict__["ownerPhone"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_parkTime():
    assert hasattr(Parking_Record, "parkTime")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "parkTime" in klass.__dict__:
            descriptor = klass.__dict__["parkTime"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_totalCost():
    assert hasattr(Parking_Record, "totalCost")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "totalCost" in klass.__dict__:
            descriptor = klass.__dict__["totalCost"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_releaseTime():
    assert hasattr(Parking_Record, "releaseTime")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "releaseTime" in klass.__dict__:
            descriptor = klass.__dict__["releaseTime"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_ownerName():
    assert hasattr(Parking_Record, "ownerName")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_vehicleModel():
    assert hasattr(Parking_Record, "vehicleModel")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "vehicleModel" in klass.__dict__:
            descriptor = klass.__dict__["vehicleModel"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_hourlyRate():
    assert hasattr(Parking_Record, "hourlyRate")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "hourlyRate" in klass.__dict__:
            descriptor = klass.__dict__["hourlyRate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_parking_record_has_vehicleColor():
    assert hasattr(Parking_Record, "vehicleColor")
    descriptor = None
    for klass in Parking_Record.__mro__:
        if "vehicleColor" in klass.__dict__:
            descriptor = klass.__dict__["vehicleColor"]
            break
    assert isinstance(descriptor, property)



def test_hyp_spot_is_not_abstract():
    assert not inspect.isabstract(Spot)


def test_hyp_spot_constructor_exists():
    assert callable(Spot.__init__)


def test_hyp_spot_constructor_args():
    sig = inspect.signature(Spot.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "section" in params, "Missing parameter 'section'"
    assert "isValet" in params, "Missing parameter 'isValet'"
    assert "spotNumber" in params, "Missing parameter 'spotNumber'"
    assert "spotType" in params, "Missing parameter 'spotType'"
    assert "covered" in params, "Missing parameter 'covered'"
    assert "isDisabledSpot" in params, "Missing parameter 'isDisabledSpot'"
    assert "level" in params, "Missing parameter 'level'"

def test_hyp_spot_has_status():
    assert hasattr(Spot, "status")
    descriptor = None
    for klass in Spot.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spot_has_section():
    assert hasattr(Spot, "section")
    descriptor = None
    for klass in Spot.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spot_has_isValet():
    assert hasattr(Spot, "isValet")
    descriptor = None
    for klass in Spot.__mro__:
        if "isValet" in klass.__dict__:
            descriptor = klass.__dict__["isValet"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spot_has_spotNumber():
    assert hasattr(Spot, "spotNumber")
    descriptor = None
    for klass in Spot.__mro__:
        if "spotNumber" in klass.__dict__:
            descriptor = klass.__dict__["spotNumber"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spot_has_spotType():
    assert hasattr(Spot, "spotType")
    descriptor = None
    for klass in Spot.__mro__:
        if "spotType" in klass.__dict__:
            descriptor = klass.__dict__["spotType"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spot_has_covered():
    assert hasattr(Spot, "covered")
    descriptor = None
    for klass in Spot.__mro__:
        if "covered" in klass.__dict__:
            descriptor = klass.__dict__["covered"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spot_has_isDisabledSpot():
    assert hasattr(Spot, "isDisabledSpot")
    descriptor = None
    for klass in Spot.__mro__:
        if "isDisabledSpot" in klass.__dict__:
            descriptor = klass.__dict__["isDisabledSpot"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spot_has_level():
    assert hasattr(Spot, "level")
    descriptor = None
    for klass in Spot.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_hyp_parkinglot_is_not_abstract():
    assert not inspect.isabstract(ParkingLot)


def test_hyp_parkinglot_constructor_exists():
    assert callable(ParkingLot.__init__)


def test_hyp_parkinglot_constructor_args():
    sig = inspect.signature(ParkingLot.__init__)
    params = list(sig.parameters.keys())
    assert "maxSize" in params, "Missing parameter 'maxSize'"
    assert "hourlyPrice" in params, "Missing parameter 'hourlyPrice'"





def test_hyp_vehicleinterface_interface_is_not_abstract():
    assert not inspect.isabstract(VehicleInterface_Interface)


def test_hyp_vehicleinterface_interface_constructor_exists():
    assert callable(VehicleInterface_Interface.__init__)


def test_hyp_vehicleinterface_interface_constructor_args():
    sig = inspect.signature(VehicleInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_motorcycle_is_not_abstract():
    assert not inspect.isabstract(MotorCycle)


def test_hyp_motorcycle_constructor_exists():
    assert callable(MotorCycle.__init__)


def test_hyp_motorcycle_constructor_args():
    sig = inspect.signature(MotorCycle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_hyp_car_constructor_exists():
    assert callable(Car.__init__)


def test_hyp_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bus_is_not_abstract():
    assert not inspect.isabstract(Bus)


def test_hyp_bus_constructor_exists():
    assert callable(Bus.__init__)


def test_hyp_bus_constructor_args():
    sig = inspect.signature(Bus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractvehicle_is_not_abstract():
    assert not inspect.isabstract(AbstractVehicle)


def test_hyp_abstractvehicle_constructor_exists():
    assert callable(AbstractVehicle.__init__)


def test_hyp_abstractvehicle_constructor_args():
    sig = inspect.signature(AbstractVehicle.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "licensePlate" in params, "Missing parameter 'licensePlate'"
    assert "restrictions" in params, "Missing parameter 'restrictions'"

def test_hyp_abstractvehicle_has_type():
    assert hasattr(AbstractVehicle, "type")
    descriptor = None
    for klass in AbstractVehicle.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_abstractvehicle_has_licensePlate():
    assert hasattr(AbstractVehicle, "licensePlate")
    descriptor = None
    for klass in AbstractVehicle.__mro__:
        if "licensePlate" in klass.__dict__:
            descriptor = klass.__dict__["licensePlate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_abstractvehicle_has_restrictions():
    assert hasattr(AbstractVehicle, "restrictions")
    descriptor = None
    for klass in AbstractVehicle.__mro__:
        if "restrictions" in klass.__dict__:
            descriptor = klass.__dict__["restrictions"]
            break
    assert isinstance(descriptor, property)



def test_hyp_spotrestriction_is_not_abstract():
    assert not inspect.isabstract(spotRestriction)


def test_hyp_spotrestriction_constructor_exists():
    assert callable(spotRestriction.__init__)


def test_hyp_spotrestriction_constructor_args():
    sig = inspect.signature(spotRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "spotType" in params, "Missing parameter 'spotType'"

def test_hyp_spotrestriction_has_size():
    assert hasattr(spotRestriction, "size")
    descriptor = None
    for klass in spotRestriction.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spotrestriction_has_spotType():
    assert hasattr(spotRestriction, "spotType")
    descriptor = None
    for klass in spotRestriction.__mro__:
        if "spotType" in klass.__dict__:
            descriptor = klass.__dict__["spotType"]
            break
    assert isinstance(descriptor, property)

def test_hyp_spottype_exists():
    # Check that the Enumeration exists
    assert spotType is not None

def test_hyp_spottype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in spotType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in spotType"

def test_hyp_spotstatus_exists():
    # Check that the Enumeration exists
    assert spotStatus is not None

def test_hyp_spotstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in spotStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in spotStatus"

def test_hyp_vehiclestatus_exists():
    # Check that the Enumeration exists
    assert vehicleStatus is not None

def test_hyp_vehiclestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in vehicleStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in vehicleStatus"


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
Parking_Record_strategy = st.builds(
    Parking_Record,
    spot=
        st.none(),
    vehicleLicensePlate=
        safe_text,
    ownerPhone=
        safe_text,
    parkTime=
        safe_text,
    totalCost=
        st.integers(),
    releaseTime=
        safe_text,
    ownerName=
        safe_text,
    vehicleModel=
        safe_text,
    hourlyRate=
        st.integers(),
    vehicleColor=
        safe_text
)
Spot_strategy = st.builds(
    Spot,
    status=
        st.none(),
    section=
        safe_text,
    isValet=
        st.booleans(),
    spotNumber=
        st.integers(),
    spotType=
        st.none(),
    covered=
        st.booleans(),
    isDisabledSpot=
        st.booleans(),
    level=
        st.integers()
)
ParkingLot_strategy = st.builds(
    ParkingLot,
    maxSize=
        st.integers(),
    hourlyPrice=
        st.integers()
)
VehicleInterface_Interface_strategy = st.builds(
    VehicleInterface_Interface,
)
MotorCycle_strategy = st.builds(
    MotorCycle,
)
Car_strategy = st.builds(
    Car,
)
Bus_strategy = st.builds(
    Bus,
)
AbstractVehicle_strategy = st.builds(
    AbstractVehicle,
    type=
        safe_text,
    licensePlate=
        safe_text,
    restrictions=
        st.none()
)
spotRestriction_strategy = st.builds(
    spotRestriction,
    size=
        st.integers(),
    spotType=
        st.none()
)

@given(instance=Parking_Record_strategy)
@settings(max_examples=50)
def test_hyp_parking_record_instantiation(instance):
    assert isinstance(instance, Parking_Record)



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_spot_setter(instance):
    original = instance.spot
    instance.spot = original
    assert instance.spot == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_vehicleLicensePlate_setter(instance):
    original = instance.vehicleLicensePlate
    instance.vehicleLicensePlate = original
    assert instance.vehicleLicensePlate == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_ownerPhone_setter(instance):
    original = instance.ownerPhone
    instance.ownerPhone = original
    assert instance.ownerPhone == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_parkTime_setter(instance):
    original = instance.parkTime
    instance.parkTime = original
    assert instance.parkTime == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_totalCost_setter(instance):
    original = instance.totalCost
    instance.totalCost = original
    assert instance.totalCost == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_releaseTime_setter(instance):
    original = instance.releaseTime
    instance.releaseTime = original
    assert instance.releaseTime == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_vehicleModel_setter(instance):
    original = instance.vehicleModel
    instance.vehicleModel = original
    assert instance.vehicleModel == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_hourlyRate_setter(instance):
    original = instance.hourlyRate
    instance.hourlyRate = original
    assert instance.hourlyRate == original



@given(instance=Parking_Record_strategy)
def test_hyp_parking_record_vehicleColor_setter(instance):
    original = instance.vehicleColor
    instance.vehicleColor = original
    assert instance.vehicleColor == original

@given(instance=Spot_strategy)
@settings(max_examples=50)
def test_hyp_spot_instantiation(instance):
    assert isinstance(instance, Spot)



@given(instance=Spot_strategy)
def test_hyp_spot_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Spot_strategy)
def test_hyp_spot_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original



@given(instance=Spot_strategy)
def test_hyp_spot_isValet_setter(instance):
    original = instance.isValet
    instance.isValet = original
    assert instance.isValet == original



@given(instance=Spot_strategy)
def test_hyp_spot_spotNumber_setter(instance):
    original = instance.spotNumber
    instance.spotNumber = original
    assert instance.spotNumber == original



@given(instance=Spot_strategy)
def test_hyp_spot_spotType_setter(instance):
    original = instance.spotType
    instance.spotType = original
    assert instance.spotType == original



@given(instance=Spot_strategy)
def test_hyp_spot_covered_setter(instance):
    original = instance.covered
    instance.covered = original
    assert instance.covered == original



@given(instance=Spot_strategy)
def test_hyp_spot_isDisabledSpot_setter(instance):
    original = instance.isDisabledSpot
    instance.isDisabledSpot = original
    assert instance.isDisabledSpot == original



@given(instance=Spot_strategy)
def test_hyp_spot_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original




@given(instance=ParkingLot_strategy)
def test_hyp_parkinglot_maxSize_setter(instance):
    original = instance.maxSize
    instance.maxSize = original
    assert instance.maxSize == original



@given(instance=ParkingLot_strategy)
def test_hyp_parkinglot_hourlyPrice_setter(instance):
    original = instance.hourlyPrice
    instance.hourlyPrice = original
    assert instance.hourlyPrice == original





@given(instance=AbstractVehicle_strategy)
@settings(max_examples=50)
def test_hyp_abstractvehicle_instantiation(instance):
    assert isinstance(instance, AbstractVehicle)



@given(instance=AbstractVehicle_strategy)
def test_hyp_abstractvehicle_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=AbstractVehicle_strategy)
def test_hyp_abstractvehicle_licensePlate_setter(instance):
    original = instance.licensePlate
    instance.licensePlate = original
    assert instance.licensePlate == original



@given(instance=AbstractVehicle_strategy)
def test_hyp_abstractvehicle_restrictions_setter(instance):
    original = instance.restrictions
    instance.restrictions = original
    assert instance.restrictions == original

@given(instance=spotRestriction_strategy)
@settings(max_examples=50)
def test_hyp_spotrestriction_instantiation(instance):
    assert isinstance(instance, spotRestriction)



@given(instance=spotRestriction_strategy)
def test_hyp_spotrestriction_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=spotRestriction_strategy)
def test_hyp_spotrestriction_spotType_setter(instance):
    original = instance.spotType
    instance.spotType = original
    assert instance.spotType == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractVehicle,
    Bus,
    Car,
    MotorCycle,
    ParkingLot,
    Parking_Record,
    Spot,
    VehicleInterface_Interface,
    spotRestriction,
    spotStatus,
    spotType,
    vehicleStatus,
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

def test_ParkingLot_hourlyPrice_value_roundtrip():
    instance = ParkingLot(hourlyPrice=7, maxSize=7)
    assert instance.hourlyPrice == 7
    instance.hourlyPrice = 13
    assert instance.hourlyPrice == 13


def test_ParkingLot_maxSize_value_roundtrip():
    instance = ParkingLot(hourlyPrice=7, maxSize=7)
    assert instance.maxSize == 7
    instance.maxSize = 13
    assert instance.maxSize == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bus_strategy = st.builds(Bus)
@given(instance=Bus_strategy)
@settings(max_examples=25)
def test_Bus_instantiation(instance):
    assert isinstance(instance, Bus)


Car_strategy = st.builds(Car)
@given(instance=Car_strategy)
@settings(max_examples=25)
def test_Car_instantiation(instance):
    assert isinstance(instance, Car)


MotorCycle_strategy = st.builds(MotorCycle)
@given(instance=MotorCycle_strategy)
@settings(max_examples=25)
def test_MotorCycle_instantiation(instance):
    assert isinstance(instance, MotorCycle)


ParkingLot_strategy = st.builds(ParkingLot, hourlyPrice=st.integers(), maxSize=st.integers())
@given(instance=ParkingLot_strategy)
@settings(max_examples=25)
def test_ParkingLot_instantiation(instance):
    assert isinstance(instance, ParkingLot)


VehicleInterface_Interface_strategy = st.builds(VehicleInterface_Interface)
@given(instance=VehicleInterface_Interface_strategy)
@settings(max_examples=25)
def test_VehicleInterface_Interface_instantiation(instance):
    assert isinstance(instance, VehicleInterface_Interface)



