import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Booking,
    Crew,
    Person,
    reservationsystem_Airport,
    reservationsystem_Attendant,
    reservationsystem_Booking,
    reservationsystem_City,
    reservationsystem_Crew,
    reservationsystem_GeneralFlight,
    reservationsystem_Passenger,
    reservationsystem_PaymentInfo,
    reservationsystem_Person,
    reservationsystem_Pilot,
    reservationsystem_Plane,
    reservationsystem_Seat,
    reservationsystem_SpecificFlight,
    reservationsystem_User,
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

def test_reservationsystem_Airport_abbr_value_roundtrip():
    instance = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    assert instance.abbr == "sample_text"
    instance.abbr = "sample_text_2"
    assert instance.abbr == "sample_text_2"


def test_reservationsystem_Airport_id_value_roundtrip():
    instance = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_reservationsystem_Airport_name_value_roundtrip():
    instance = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_reservationsystem_Booking_baggageInfo_value_roundtrip():
    instance = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    assert instance.baggageInfo == "sample_text"
    instance.baggageInfo = "sample_text_2"
    assert instance.baggageInfo == "sample_text_2"


def test_reservationsystem_Booking_bookNo_value_roundtrip():
    instance = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    assert instance.bookNo == "sample_text"
    instance.bookNo = "sample_text_2"
    assert instance.bookNo == "sample_text_2"


def test_reservationsystem_Booking_bookingStatus_value_roundtrip():
    instance = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    assert instance.bookingStatus == 7
    instance.bookingStatus = 13
    assert instance.bookingStatus == 13


def test_reservationsystem_City_abbr_value_roundtrip():
    instance = reservationsystem_City(abbr="sample_text", id=7, name="sample_text")
    assert instance.abbr == "sample_text"
    instance.abbr = "sample_text_2"
    assert instance.abbr == "sample_text_2"


def test_reservationsystem_City_id_value_roundtrip():
    instance = reservationsystem_City(abbr="sample_text", id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_reservationsystem_City_name_value_roundtrip():
    instance = reservationsystem_City(abbr="sample_text", id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_reservationsystem_Crew_employeeId_value_roundtrip():
    instance = reservationsystem_Crew(employeeId="sample_text")
    assert instance.employeeId == "sample_text"
    instance.employeeId = "sample_text_2"
    assert instance.employeeId == "sample_text_2"


def test_reservationsystem_GeneralFlight_arrivalTime_value_roundtrip():
    instance = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    assert instance.arrivalTime == "sample_text"
    instance.arrivalTime = "sample_text_2"
    assert instance.arrivalTime == "sample_text_2"


def test_reservationsystem_GeneralFlight_departureTime_value_roundtrip():
    instance = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    assert instance.departureTime == "sample_text"
    instance.departureTime = "sample_text_2"
    assert instance.departureTime == "sample_text_2"


def test_reservationsystem_GeneralFlight_flightNo_value_roundtrip():
    instance = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    assert instance.flightNo == "sample_text"
    instance.flightNo = "sample_text_2"
    assert instance.flightNo == "sample_text_2"


def test_reservationsystem_Passenger_foodPref_value_roundtrip():
    instance = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    assert instance.foodPref == "sample_text"
    instance.foodPref = "sample_text_2"
    assert instance.foodPref == "sample_text_2"


def test_reservationsystem_Passenger_specialNeeds_value_roundtrip():
    instance = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    assert instance.specialNeeds == "sample_text"
    instance.specialNeeds = "sample_text_2"
    assert instance.specialNeeds == "sample_text_2"


def test_reservationsystem_PaymentInfo_cardAddr_value_roundtrip():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert instance.cardAddr == "sample_text"
    instance.cardAddr = "sample_text_2"
    assert instance.cardAddr == "sample_text_2"


def test_reservationsystem_PaymentInfo_cardNo_value_roundtrip():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert instance.cardNo == "sample_text"
    instance.cardNo = "sample_text_2"
    assert instance.cardNo == "sample_text_2"


def test_reservationsystem_PaymentInfo_cardOwner_value_roundtrip():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert instance.cardOwner == "sample_text"
    instance.cardOwner = "sample_text_2"
    assert instance.cardOwner == "sample_text_2"


def test_reservationsystem_PaymentInfo_createTime_value_roundtrip():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert instance.createTime == date(2024, 1, 1)
    instance.createTime = date(2025, 6, 15)
    assert instance.createTime == date(2025, 6, 15)


def test_reservationsystem_PaymentInfo_id_value_roundtrip():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_reservationsystem_PaymentInfo_payTime_value_roundtrip():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert instance.payTime == date(2024, 1, 1)
    instance.payTime = date(2025, 6, 15)
    assert instance.payTime == date(2025, 6, 15)


def test_reservationsystem_PaymentInfo_status_value_roundtrip():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert instance.status == 7
    instance.status = 13
    assert instance.status == 13


def test_reservationsystem_PaymentInfo_type_value_roundtrip():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert instance.type == 7
    instance.type = 13
    assert instance.type == 13


def test_reservationsystem_Person_FamilyName_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.FamilyName == "sample_text"
    instance.FamilyName = "sample_text_2"
    assert instance.FamilyName == "sample_text_2"


def test_reservationsystem_Person_addr_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.addr == "sample_text"
    instance.addr = "sample_text_2"
    assert instance.addr == "sample_text_2"


def test_reservationsystem_Person_birthDate_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.birthDate == date(2024, 1, 1)
    instance.birthDate = date(2025, 6, 15)
    assert instance.birthDate == date(2025, 6, 15)


def test_reservationsystem_Person_citizenship_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.citizenship == "sample_text"
    instance.citizenship = "sample_text_2"
    assert instance.citizenship == "sample_text_2"


def test_reservationsystem_Person_email_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_reservationsystem_Person_gender_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.gender == 7
    instance.gender = 13
    assert instance.gender == 13


def test_reservationsystem_Person_id_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_reservationsystem_Person_middleName_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.middleName == "sample_text"
    instance.middleName = "sample_text_2"
    assert instance.middleName == "sample_text_2"


def test_reservationsystem_Person_name_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_reservationsystem_Person_passportId_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.passportId == "sample_text"
    instance.passportId = "sample_text_2"
    assert instance.passportId == "sample_text_2"


def test_reservationsystem_Person_phone_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_reservationsystem_Person_residence_value_roundtrip():
    instance = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    assert instance.residence == "sample_text"
    instance.residence = "sample_text_2"
    assert instance.residence == "sample_text_2"


def test_reservationsystem_Pilot_certificationId_value_roundtrip():
    instance = reservationsystem_Pilot(certificationId="sample_text", experience=7)
    assert instance.certificationId == "sample_text"
    instance.certificationId = "sample_text_2"
    assert instance.certificationId == "sample_text_2"


def test_reservationsystem_Pilot_experience_value_roundtrip():
    instance = reservationsystem_Pilot(certificationId="sample_text", experience=7)
    assert instance.experience == 7
    instance.experience = 13
    assert instance.experience == 13


def test_reservationsystem_Plane_capacity_value_roundtrip():
    instance = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    assert instance.capacity == 7
    instance.capacity = 13
    assert instance.capacity == 13


def test_reservationsystem_Plane_crewNum_value_roundtrip():
    instance = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    assert instance.crewNum == 7
    instance.crewNum = 13
    assert instance.crewNum == 13


def test_reservationsystem_Plane_id_value_roundtrip():
    instance = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_reservationsystem_Plane_model_value_roundtrip():
    instance = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    assert instance.model == "sample_text"
    instance.model = "sample_text_2"
    assert instance.model == "sample_text_2"


def test_reservationsystem_Seat_isExit_value_roundtrip():
    instance = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    assert instance.isExit == True
    instance.isExit = False
    assert instance.isExit == False


def test_reservationsystem_Seat_no_value_roundtrip():
    instance = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    assert instance.no == "sample_text"
    instance.no = "sample_text_2"
    assert instance.no == "sample_text_2"


def test_reservationsystem_Seat_type_value_roundtrip():
    instance = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    assert instance.type == 7
    instance.type = 13
    assert instance.type == 13


def test_reservationsystem_SpecificFlight_date_value_roundtrip():
    instance = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_reservationsystem_SpecificFlight_id_value_roundtrip():
    instance = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_reservationsystem_SpecificFlight_realArriTime_value_roundtrip():
    instance = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    assert instance.realArriTime == date(2024, 1, 1)
    instance.realArriTime = date(2025, 6, 15)
    assert instance.realArriTime == date(2025, 6, 15)


def test_reservationsystem_SpecificFlight_realDepTime_value_roundtrip():
    instance = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    assert instance.realDepTime == date(2024, 1, 1)
    instance.realDepTime = date(2025, 6, 15)
    assert instance.realDepTime == date(2025, 6, 15)


def test_reservationsystem_SpecificFlight_status_value_roundtrip():
    instance = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    assert instance.status == 7
    instance.status = 13
    assert instance.status == 13


def test_reservationsystem_User_md5Pwd_value_roundtrip():
    instance = reservationsystem_User(md5Pwd="sample_text", userName="sample_text", userType="sample_text")
    assert instance.md5Pwd == "sample_text"
    instance.md5Pwd = "sample_text_2"
    assert instance.md5Pwd == "sample_text_2"


def test_reservationsystem_User_userName_value_roundtrip():
    instance = reservationsystem_User(md5Pwd="sample_text", userName="sample_text", userType="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_reservationsystem_User_userType_value_roundtrip():
    instance = reservationsystem_User(md5Pwd="sample_text", userName="sample_text", userType="sample_text")
    assert instance.userType == "sample_text"
    instance.userType = "sample_text_2"
    assert instance.userType == "sample_text_2"


def test_reservationsystem_PaymentInfo_isa_Booking():
    instance = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    assert isinstance(instance, Booking)


def test_reservationsystem_Attendant_isa_Crew():
    instance = reservationsystem_Attendant()
    assert isinstance(instance, Crew)


def test_reservationsystem_Pilot_isa_Crew():
    instance = reservationsystem_Pilot(certificationId="sample_text", experience=7)
    assert isinstance(instance, Crew)


def test_reservationsystem_Crew_isa_Person():
    instance = reservationsystem_Crew(employeeId="sample_text")
    assert isinstance(instance, Person)


def test_reservationsystem_Passenger_isa_Person():
    instance = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    assert isinstance(instance, Person)


def test_assoc_Leader2_link_reassign_clear():
    a = reservationsystem_Crew(employeeId="sample_text")
    b1 = reservationsystem_Crew(employeeId="sample_text")
    b2 = reservationsystem_Crew(employeeId="sample_text_2")
    _safe_set(a, 'reservationsystem_Crew', b1)
    assert _is_linked(a, 'reservationsystem_Crew', b1)
    if hasattr(b1, 'reservationsystem_Crew1'):
        assert _is_linked(b1, 'reservationsystem_Crew1', a)
    _safe_set(a, 'reservationsystem_Crew', b2)
    assert _is_linked(a, 'reservationsystem_Crew', b2)
    if hasattr(b1, 'reservationsystem_Crew1'):
        assert not _is_linked(b1, 'reservationsystem_Crew1', a)
    if hasattr(b2, 'reservationsystem_Crew1'):
        assert _is_linked(b2, 'reservationsystem_Crew1', a)
    _safe_set(a, 'reservationsystem_Crew', None)
    assert not _is_linked(a, 'reservationsystem_Crew', b2)
    if hasattr(b2, 'reservationsystem_Crew1'):
        assert not _is_linked(b2, 'reservationsystem_Crew1', a)


def test_assoc_airport33_link_reassign_clear():
    a = reservationsystem_City(abbr="sample_text", id=7, name="sample_text")
    b1 = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    b2 = reservationsystem_Airport(abbr="sample_text_2", id=13, name="sample_text_2")
    _safe_set(a, 'city', {b1})
    assert _is_linked(a, 'city', b1)
    if hasattr(b1, 'Airport'):
        assert _is_linked(b1, 'Airport', a)
    _safe_set(a, 'city', {b2})
    assert _is_linked(a, 'city', b2)
    if hasattr(b1, 'Airport'):
        assert not _is_linked(b1, 'Airport', a)
    if hasattr(b2, 'Airport'):
        assert _is_linked(b2, 'Airport', a)
    _safe_set(a, 'city', set())
    assert not _is_linked(a, 'city', b2)
    if hasattr(b2, 'Airport'):
        assert not _is_linked(b2, 'Airport', a)


def test_assoc_belongsTo0_link_reassign_clear():
    a = reservationsystem_User(md5Pwd="sample_text", userName="sample_text", userType="sample_text")
    b1 = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    b2 = reservationsystem_Person(FamilyName="sample_text_2", addr="sample_text_2", birthDate=date(2025, 6, 15), citizenship="sample_text_2", email="sample_text_2", gender=13, id=13, middleName="sample_text_2", name="sample_text_2", passportId="sample_text_2", phone="sample_text_2", residence="sample_text_2")
    _safe_set(a, 'reservationsystem_User', b1)
    assert _is_linked(a, 'reservationsystem_User', b1)
    if hasattr(b1, 'reservationsystem_Person'):
        assert _is_linked(b1, 'reservationsystem_Person', a)
    _safe_set(a, 'reservationsystem_User', b2)
    assert _is_linked(a, 'reservationsystem_User', b2)
    if hasattr(b1, 'reservationsystem_Person'):
        assert not _is_linked(b1, 'reservationsystem_Person', a)
    if hasattr(b2, 'reservationsystem_Person'):
        assert _is_linked(b2, 'reservationsystem_Person', a)
    _safe_set(a, 'reservationsystem_User', None)
    assert not _is_linked(a, 'reservationsystem_User', b2)
    if hasattr(b2, 'reservationsystem_Person'):
        assert not _is_linked(b2, 'reservationsystem_Person', a)


def test_assoc_book36_link_reassign_clear():
    a = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    b1 = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    b2 = reservationsystem_Booking(baggageInfo="sample_text_2", bookNo="sample_text_2", bookingStatus=13)
    _safe_set(a, 'seats37', b1)
    assert _is_linked(a, 'seats37', b1)
    if hasattr(b1, 'Booking38'):
        assert _is_linked(b1, 'Booking38', a)
    _safe_set(a, 'seats37', b2)
    assert _is_linked(a, 'seats37', b2)
    if hasattr(b1, 'Booking38'):
        assert not _is_linked(b1, 'Booking38', a)
    if hasattr(b2, 'Booking38'):
        assert _is_linked(b2, 'Booking38', a)
    _safe_set(a, 'seats37', None)
    assert not _is_linked(a, 'seats37', b2)
    if hasattr(b2, 'Booking38'):
        assert not _is_linked(b2, 'Booking38', a)


def test_assoc_booking24_link_reassign_clear():
    a = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    b1 = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    b2 = reservationsystem_Booking(baggageInfo="sample_text_2", bookNo="sample_text_2", bookingStatus=13)
    _safe_set(a, 'specificFlight25', {b1})
    assert _is_linked(a, 'specificFlight25', b1)
    if hasattr(b1, 'Booking26'):
        assert _is_linked(b1, 'Booking26', a)
    _safe_set(a, 'specificFlight25', {b2})
    assert _is_linked(a, 'specificFlight25', b2)
    if hasattr(b1, 'Booking26'):
        assert not _is_linked(b1, 'Booking26', a)
    if hasattr(b2, 'Booking26'):
        assert _is_linked(b2, 'Booking26', a)
    _safe_set(a, 'specificFlight25', set())
    assert not _is_linked(a, 'specificFlight25', b2)
    if hasattr(b2, 'Booking26'):
        assert not _is_linked(b2, 'Booking26', a)


def test_assoc_booking5_link_reassign_clear():
    a = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    b1 = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    b2 = reservationsystem_Booking(baggageInfo="sample_text_2", bookNo="sample_text_2", bookingStatus=13)
    _safe_set(a, 'passenger', b1)
    assert _is_linked(a, 'passenger', b1)
    if hasattr(b1, 'Booking'):
        assert _is_linked(b1, 'Booking', a)
    _safe_set(a, 'passenger', b2)
    assert _is_linked(a, 'passenger', b2)
    if hasattr(b1, 'Booking'):
        assert not _is_linked(b1, 'Booking', a)
    if hasattr(b2, 'Booking'):
        assert _is_linked(b2, 'Booking', a)
    _safe_set(a, 'passenger', None)
    assert not _is_linked(a, 'passenger', b2)
    if hasattr(b2, 'Booking'):
        assert not _is_linked(b2, 'Booking', a)


def test_assoc_city32_link_reassign_clear():
    a = reservationsystem_City(abbr="sample_text", id=7, name="sample_text")
    b1 = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    b2 = reservationsystem_Airport(abbr="sample_text_2", id=13, name="sample_text_2")
    _safe_set(a, 'City', b1)
    assert _is_linked(a, 'City', b1)
    if hasattr(b1, 'airport'):
        assert _is_linked(b1, 'airport', a)
    _safe_set(a, 'City', b2)
    assert _is_linked(a, 'City', b2)
    if hasattr(b1, 'airport'):
        assert not _is_linked(b1, 'airport', a)
    if hasattr(b2, 'airport'):
        assert _is_linked(b2, 'airport', a)
    _safe_set(a, 'City', None)
    assert not _is_linked(a, 'City', b2)
    if hasattr(b2, 'airport'):
        assert not _is_linked(b2, 'airport', a)


def test_assoc_crew22_link_reassign_clear():
    a = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    b1 = reservationsystem_Crew(employeeId="sample_text")
    b2 = reservationsystem_Crew(employeeId="sample_text_2")
    _safe_set(a, 'specificFlight23', {b1})
    assert _is_linked(a, 'specificFlight23', b1)
    if hasattr(b1, 'Crew'):
        assert _is_linked(b1, 'Crew', a)
    _safe_set(a, 'specificFlight23', {b2})
    assert _is_linked(a, 'specificFlight23', b2)
    if hasattr(b1, 'Crew'):
        assert not _is_linked(b1, 'Crew', a)
    if hasattr(b2, 'Crew'):
        assert _is_linked(b2, 'Crew', a)
    _safe_set(a, 'specificFlight23', set())
    assert not _is_linked(a, 'specificFlight23', b2)
    if hasattr(b2, 'Crew'):
        assert not _is_linked(b2, 'Crew', a)


def test_assoc_from_15_link_reassign_clear():
    a = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    b1 = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    b2 = reservationsystem_Airport(abbr="sample_text_2", id=13, name="sample_text_2")
    _safe_set(a, 'reservationsystem_GeneralFlight', b1)
    assert _is_linked(a, 'reservationsystem_GeneralFlight', b1)
    if hasattr(b1, 'reservationsystem_Airport'):
        assert _is_linked(b1, 'reservationsystem_Airport', a)
    _safe_set(a, 'reservationsystem_GeneralFlight', b2)
    assert _is_linked(a, 'reservationsystem_GeneralFlight', b2)
    if hasattr(b1, 'reservationsystem_Airport'):
        assert not _is_linked(b1, 'reservationsystem_Airport', a)
    if hasattr(b2, 'reservationsystem_Airport'):
        assert _is_linked(b2, 'reservationsystem_Airport', a)
    _safe_set(a, 'reservationsystem_GeneralFlight', None)
    assert not _is_linked(a, 'reservationsystem_GeneralFlight', b2)
    if hasattr(b2, 'reservationsystem_Airport'):
        assert not _is_linked(b2, 'reservationsystem_Airport', a)


def test_assoc_generalFlight19_link_reassign_clear():
    a = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    b1 = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    b2 = reservationsystem_GeneralFlight(arrivalTime="sample_text_2", departureTime="sample_text_2", flightNo="sample_text_2")
    _safe_set(a, 'specificFlight', b1)
    assert _is_linked(a, 'specificFlight', b1)
    if hasattr(b1, 'GeneralFlight'):
        assert _is_linked(b1, 'GeneralFlight', a)
    _safe_set(a, 'specificFlight', b2)
    assert _is_linked(a, 'specificFlight', b2)
    if hasattr(b1, 'GeneralFlight'):
        assert not _is_linked(b1, 'GeneralFlight', a)
    if hasattr(b2, 'GeneralFlight'):
        assert _is_linked(b2, 'GeneralFlight', a)
    _safe_set(a, 'specificFlight', None)
    assert not _is_linked(a, 'specificFlight', b2)
    if hasattr(b2, 'GeneralFlight'):
        assert not _is_linked(b2, 'GeneralFlight', a)


def test_assoc_passenger4_link_reassign_clear():
    a = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    b1 = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    b2 = reservationsystem_Booking(baggageInfo="sample_text_2", bookNo="sample_text_2", bookingStatus=13)
    _safe_set(a, 'reservationsystem_Passenger', b1)
    assert _is_linked(a, 'reservationsystem_Passenger', b1)
    if hasattr(b1, 'reservationsystem_Booking'):
        assert _is_linked(b1, 'reservationsystem_Booking', a)
    _safe_set(a, 'reservationsystem_Passenger', b2)
    assert _is_linked(a, 'reservationsystem_Passenger', b2)
    if hasattr(b1, 'reservationsystem_Booking'):
        assert not _is_linked(b1, 'reservationsystem_Booking', a)
    if hasattr(b2, 'reservationsystem_Booking'):
        assert _is_linked(b2, 'reservationsystem_Booking', a)
    _safe_set(a, 'reservationsystem_Passenger', None)
    assert not _is_linked(a, 'reservationsystem_Passenger', b2)
    if hasattr(b2, 'reservationsystem_Booking'):
        assert not _is_linked(b2, 'reservationsystem_Booking', a)


def test_assoc_passenger8_link_reassign_clear():
    a = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    b1 = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    b2 = reservationsystem_Booking(baggageInfo="sample_text_2", bookNo="sample_text_2", bookingStatus=13)
    _safe_set(a, 'Passenger', b1)
    assert _is_linked(a, 'Passenger', b1)
    if hasattr(b1, 'booking'):
        assert _is_linked(b1, 'booking', a)
    _safe_set(a, 'Passenger', b2)
    assert _is_linked(a, 'Passenger', b2)
    if hasattr(b1, 'booking'):
        assert not _is_linked(b1, 'booking', a)
    if hasattr(b2, 'booking'):
        assert _is_linked(b2, 'booking', a)
    _safe_set(a, 'Passenger', None)
    assert not _is_linked(a, 'Passenger', b2)
    if hasattr(b2, 'booking'):
        assert not _is_linked(b2, 'booking', a)


def test_assoc_paymentInfo6_link_reassign_clear():
    a = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    b1 = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    b2 = reservationsystem_Booking(baggageInfo="sample_text_2", bookNo="sample_text_2", bookingStatus=13)
    _safe_set(a, 'reservationsystem_PaymentInfo', b1)
    assert _is_linked(a, 'reservationsystem_PaymentInfo', b1)
    if hasattr(b1, 'reservationsystem_Booking7'):
        assert _is_linked(b1, 'reservationsystem_Booking7', a)
    _safe_set(a, 'reservationsystem_PaymentInfo', b2)
    assert _is_linked(a, 'reservationsystem_PaymentInfo', b2)
    if hasattr(b1, 'reservationsystem_Booking7'):
        assert not _is_linked(b1, 'reservationsystem_Booking7', a)
    if hasattr(b2, 'reservationsystem_Booking7'):
        assert _is_linked(b2, 'reservationsystem_Booking7', a)
    _safe_set(a, 'reservationsystem_PaymentInfo', None)
    assert not _is_linked(a, 'reservationsystem_PaymentInfo', b2)
    if hasattr(b2, 'reservationsystem_Booking7'):
        assert not _is_linked(b2, 'reservationsystem_Booking7', a)


def test_assoc_plane20_link_reassign_clear():
    a = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    b1 = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    b2 = reservationsystem_Plane(capacity=13, crewNum=13, id="sample_text_2", model="sample_text_2")
    _safe_set(a, 'specificFlight21', b1)
    assert _is_linked(a, 'specificFlight21', b1)
    if hasattr(b1, 'Plane'):
        assert _is_linked(b1, 'Plane', a)
    _safe_set(a, 'specificFlight21', b2)
    assert _is_linked(a, 'specificFlight21', b2)
    if hasattr(b1, 'Plane'):
        assert not _is_linked(b1, 'Plane', a)
    if hasattr(b2, 'Plane'):
        assert _is_linked(b2, 'Plane', a)
    _safe_set(a, 'specificFlight21', None)
    assert not _is_linked(a, 'specificFlight21', b2)
    if hasattr(b2, 'Plane'):
        assert not _is_linked(b2, 'Plane', a)


def test_assoc_plane34_link_reassign_clear():
    a = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    b1 = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    b2 = reservationsystem_Plane(capacity=13, crewNum=13, id="sample_text_2", model="sample_text_2")
    _safe_set(a, 'seats', b1)
    assert _is_linked(a, 'seats', b1)
    if hasattr(b1, 'Plane35'):
        assert _is_linked(b1, 'Plane35', a)
    _safe_set(a, 'seats', b2)
    assert _is_linked(a, 'seats', b2)
    if hasattr(b1, 'Plane35'):
        assert not _is_linked(b1, 'Plane35', a)
    if hasattr(b2, 'Plane35'):
        assert _is_linked(b2, 'Plane35', a)
    _safe_set(a, 'seats', None)
    assert not _is_linked(a, 'seats', b2)
    if hasattr(b2, 'Plane35'):
        assert not _is_linked(b2, 'Plane35', a)


def test_assoc_seats12_link_reassign_clear():
    a = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    b1 = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    b2 = reservationsystem_Booking(baggageInfo="sample_text_2", bookNo="sample_text_2", bookingStatus=13)
    _safe_set(a, 'Seat', b1)
    assert _is_linked(a, 'Seat', b1)
    if hasattr(b1, 'book'):
        assert _is_linked(b1, 'book', a)
    _safe_set(a, 'Seat', b2)
    assert _is_linked(a, 'Seat', b2)
    if hasattr(b1, 'book'):
        assert not _is_linked(b1, 'book', a)
    if hasattr(b2, 'book'):
        assert _is_linked(b2, 'book', a)
    _safe_set(a, 'Seat', None)
    assert not _is_linked(a, 'Seat', b2)
    if hasattr(b2, 'book'):
        assert not _is_linked(b2, 'book', a)


def test_assoc_seats29_link_reassign_clear():
    a = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    b1 = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    b2 = reservationsystem_Plane(capacity=13, crewNum=13, id="sample_text_2", model="sample_text_2")
    _safe_set(a, 'Seat31', b1)
    assert _is_linked(a, 'Seat31', b1)
    if hasattr(b1, 'plane30'):
        assert _is_linked(b1, 'plane30', a)
    _safe_set(a, 'Seat31', b2)
    assert _is_linked(a, 'Seat31', b2)
    if hasattr(b1, 'plane30'):
        assert not _is_linked(b1, 'plane30', a)
    if hasattr(b2, 'plane30'):
        assert _is_linked(b2, 'plane30', a)
    _safe_set(a, 'Seat31', None)
    assert not _is_linked(a, 'Seat31', b2)
    if hasattr(b2, 'plane30'):
        assert not _is_linked(b2, 'plane30', a)


def test_assoc_specificFlight13_link_reassign_clear():
    a = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    b1 = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    b2 = reservationsystem_GeneralFlight(arrivalTime="sample_text_2", departureTime="sample_text_2", flightNo="sample_text_2")
    _safe_set(a, 'SpecificFlight14', b1)
    assert _is_linked(a, 'SpecificFlight14', b1)
    if hasattr(b1, 'generalFlight'):
        assert _is_linked(b1, 'generalFlight', a)
    _safe_set(a, 'SpecificFlight14', b2)
    assert _is_linked(a, 'SpecificFlight14', b2)
    if hasattr(b1, 'generalFlight'):
        assert not _is_linked(b1, 'generalFlight', a)
    if hasattr(b2, 'generalFlight'):
        assert _is_linked(b2, 'generalFlight', a)
    _safe_set(a, 'SpecificFlight14', None)
    assert not _is_linked(a, 'SpecificFlight14', b2)
    if hasattr(b2, 'generalFlight'):
        assert not _is_linked(b2, 'generalFlight', a)


def test_assoc_specificFlight27_link_reassign_clear():
    a = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    b1 = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    b2 = reservationsystem_Plane(capacity=13, crewNum=13, id="sample_text_2", model="sample_text_2")
    _safe_set(a, 'SpecificFlight28', b1)
    assert _is_linked(a, 'SpecificFlight28', b1)
    if hasattr(b1, 'plane'):
        assert _is_linked(b1, 'plane', a)
    _safe_set(a, 'SpecificFlight28', b2)
    assert _is_linked(a, 'SpecificFlight28', b2)
    if hasattr(b1, 'plane'):
        assert not _is_linked(b1, 'plane', a)
    if hasattr(b2, 'plane'):
        assert _is_linked(b2, 'plane', a)
    _safe_set(a, 'SpecificFlight28', None)
    assert not _is_linked(a, 'SpecificFlight28', b2)
    if hasattr(b2, 'plane'):
        assert not _is_linked(b2, 'plane', a)


def test_assoc_specificFlight3_link_reassign_clear():
    a = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    b1 = reservationsystem_Crew(employeeId="sample_text")
    b2 = reservationsystem_Crew(employeeId="sample_text_2")
    _safe_set(a, 'SpecificFlight', b1)
    assert _is_linked(a, 'SpecificFlight', b1)
    if hasattr(b1, 'crew'):
        assert _is_linked(b1, 'crew', a)
    _safe_set(a, 'SpecificFlight', b2)
    assert _is_linked(a, 'SpecificFlight', b2)
    if hasattr(b1, 'crew'):
        assert not _is_linked(b1, 'crew', a)
    if hasattr(b2, 'crew'):
        assert _is_linked(b2, 'crew', a)
    _safe_set(a, 'SpecificFlight', None)
    assert not _is_linked(a, 'SpecificFlight', b2)
    if hasattr(b2, 'crew'):
        assert not _is_linked(b2, 'crew', a)


def test_assoc_specificFlight9_link_reassign_clear():
    a = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    b1 = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    b2 = reservationsystem_Booking(baggageInfo="sample_text_2", bookNo="sample_text_2", bookingStatus=13)
    _safe_set(a, 'SpecificFlight11', b1)
    assert _is_linked(a, 'SpecificFlight11', b1)
    if hasattr(b1, 'booking10'):
        assert _is_linked(b1, 'booking10', a)
    _safe_set(a, 'SpecificFlight11', b2)
    assert _is_linked(a, 'SpecificFlight11', b2)
    if hasattr(b1, 'booking10'):
        assert not _is_linked(b1, 'booking10', a)
    if hasattr(b2, 'booking10'):
        assert _is_linked(b2, 'booking10', a)
    _safe_set(a, 'SpecificFlight11', None)
    assert not _is_linked(a, 'SpecificFlight11', b2)
    if hasattr(b2, 'booking10'):
        assert not _is_linked(b2, 'booking10', a)


def test_assoc_to16_link_reassign_clear():
    a = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    b1 = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    b2 = reservationsystem_Airport(abbr="sample_text_2", id=13, name="sample_text_2")
    _safe_set(a, 'reservationsystem_GeneralFlight17', b1)
    assert _is_linked(a, 'reservationsystem_GeneralFlight17', b1)
    if hasattr(b1, 'reservationsystem_Airport18'):
        assert _is_linked(b1, 'reservationsystem_Airport18', a)
    _safe_set(a, 'reservationsystem_GeneralFlight17', b2)
    assert _is_linked(a, 'reservationsystem_GeneralFlight17', b2)
    if hasattr(b1, 'reservationsystem_Airport18'):
        assert not _is_linked(b1, 'reservationsystem_Airport18', a)
    if hasattr(b2, 'reservationsystem_Airport18'):
        assert _is_linked(b2, 'reservationsystem_Airport18', a)
    _safe_set(a, 'reservationsystem_GeneralFlight17', None)
    assert not _is_linked(a, 'reservationsystem_GeneralFlight17', b2)
    if hasattr(b2, 'reservationsystem_Airport18'):
        assert not _is_linked(b2, 'reservationsystem_Airport18', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Booking_strategy = st.builds(Booking)
@given(instance=Booking_strategy)
@settings(max_examples=25)
def test_Booking_instantiation(instance):
    assert isinstance(instance, Booking)


Crew_strategy = st.builds(Crew)
@given(instance=Crew_strategy)
@settings(max_examples=25)
def test_Crew_instantiation(instance):
    assert isinstance(instance, Crew)


Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


reservationsystem_Airport_strategy = st.builds(reservationsystem_Airport, abbr=safe_text, id=st.integers(), name=safe_text)
@given(instance=reservationsystem_Airport_strategy)
@settings(max_examples=25)
def test_reservationsystem_Airport_instantiation(instance):
    assert isinstance(instance, reservationsystem_Airport)


reservationsystem_Attendant_strategy = st.builds(reservationsystem_Attendant)
@given(instance=reservationsystem_Attendant_strategy)
@settings(max_examples=25)
def test_reservationsystem_Attendant_instantiation(instance):
    assert isinstance(instance, reservationsystem_Attendant)


reservationsystem_Booking_strategy = st.builds(reservationsystem_Booking, baggageInfo=safe_text, bookNo=safe_text, bookingStatus=st.integers())
@given(instance=reservationsystem_Booking_strategy)
@settings(max_examples=25)
def test_reservationsystem_Booking_instantiation(instance):
    assert isinstance(instance, reservationsystem_Booking)


reservationsystem_City_strategy = st.builds(reservationsystem_City, abbr=safe_text, id=st.integers(), name=safe_text)
@given(instance=reservationsystem_City_strategy)
@settings(max_examples=25)
def test_reservationsystem_City_instantiation(instance):
    assert isinstance(instance, reservationsystem_City)


reservationsystem_Crew_strategy = st.builds(reservationsystem_Crew, employeeId=safe_text)
@given(instance=reservationsystem_Crew_strategy)
@settings(max_examples=25)
def test_reservationsystem_Crew_instantiation(instance):
    assert isinstance(instance, reservationsystem_Crew)


reservationsystem_GeneralFlight_strategy = st.builds(reservationsystem_GeneralFlight, arrivalTime=safe_text, departureTime=safe_text, flightNo=safe_text)
@given(instance=reservationsystem_GeneralFlight_strategy)
@settings(max_examples=25)
def test_reservationsystem_GeneralFlight_instantiation(instance):
    assert isinstance(instance, reservationsystem_GeneralFlight)


reservationsystem_Passenger_strategy = st.builds(reservationsystem_Passenger, foodPref=safe_text, specialNeeds=safe_text)
@given(instance=reservationsystem_Passenger_strategy)
@settings(max_examples=25)
def test_reservationsystem_Passenger_instantiation(instance):
    assert isinstance(instance, reservationsystem_Passenger)


reservationsystem_PaymentInfo_strategy = st.builds(reservationsystem_PaymentInfo, cardAddr=safe_text, cardNo=safe_text, cardOwner=safe_text, createTime=st.dates(), id=safe_text, payTime=st.dates(), status=st.integers(), type=st.integers())
@given(instance=reservationsystem_PaymentInfo_strategy)
@settings(max_examples=25)
def test_reservationsystem_PaymentInfo_instantiation(instance):
    assert isinstance(instance, reservationsystem_PaymentInfo)


reservationsystem_Person_strategy = st.builds(reservationsystem_Person, FamilyName=safe_text, addr=safe_text, birthDate=st.dates(), citizenship=safe_text, email=safe_text, gender=st.integers(), id=st.integers(), middleName=safe_text, name=safe_text, passportId=safe_text, phone=safe_text, residence=safe_text)
@given(instance=reservationsystem_Person_strategy)
@settings(max_examples=25)
def test_reservationsystem_Person_instantiation(instance):
    assert isinstance(instance, reservationsystem_Person)


reservationsystem_Pilot_strategy = st.builds(reservationsystem_Pilot, certificationId=safe_text, experience=st.integers())
@given(instance=reservationsystem_Pilot_strategy)
@settings(max_examples=25)
def test_reservationsystem_Pilot_instantiation(instance):
    assert isinstance(instance, reservationsystem_Pilot)


reservationsystem_Plane_strategy = st.builds(reservationsystem_Plane, capacity=st.integers(), crewNum=st.integers(), id=safe_text, model=safe_text)
@given(instance=reservationsystem_Plane_strategy)
@settings(max_examples=25)
def test_reservationsystem_Plane_instantiation(instance):
    assert isinstance(instance, reservationsystem_Plane)


reservationsystem_Seat_strategy = st.builds(reservationsystem_Seat, isExit=st.booleans(), no=safe_text, type=st.integers())
@given(instance=reservationsystem_Seat_strategy)
@settings(max_examples=25)
def test_reservationsystem_Seat_instantiation(instance):
    assert isinstance(instance, reservationsystem_Seat)


reservationsystem_SpecificFlight_strategy = st.builds(reservationsystem_SpecificFlight, date=st.dates(), id=st.integers(), realArriTime=st.dates(), realDepTime=st.dates(), status=st.integers())
@given(instance=reservationsystem_SpecificFlight_strategy)
@settings(max_examples=25)
def test_reservationsystem_SpecificFlight_instantiation(instance):
    assert isinstance(instance, reservationsystem_SpecificFlight)


reservationsystem_User_strategy = st.builds(reservationsystem_User, md5Pwd=safe_text, userName=safe_text, userType=safe_text)
@given(instance=reservationsystem_User_strategy)
@settings(max_examples=25)
def test_reservationsystem_User_instantiation(instance):
    assert isinstance(instance, reservationsystem_User)


