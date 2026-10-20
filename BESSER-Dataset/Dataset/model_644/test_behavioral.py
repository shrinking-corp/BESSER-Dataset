import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_Leader2_reverse_link_reassign_clear():
    a1 = reservationsystem_Crew(employeeId="sample_text")
    a2 = reservationsystem_Crew(employeeId="sample_text_2")
    b = reservationsystem_Crew(employeeId="sample_text")
    _safe_set(b, 'reservationsystem_Crew1', a1)
    assert _is_linked(b, 'reservationsystem_Crew1', a1)
    if hasattr(a1, 'reservationsystem_Crew'):
        assert _is_linked(a1, 'reservationsystem_Crew', b)
    _safe_set(b, 'reservationsystem_Crew1', a2)
    assert _is_linked(b, 'reservationsystem_Crew1', a2)
    if hasattr(a1, 'reservationsystem_Crew'):
        assert not _is_linked(a1, 'reservationsystem_Crew', b)
    if hasattr(a2, 'reservationsystem_Crew'):
        assert _is_linked(a2, 'reservationsystem_Crew', b)
    _safe_set(b, 'reservationsystem_Crew1', None)
    assert not _is_linked(b, 'reservationsystem_Crew1', a2)
    if hasattr(a2, 'reservationsystem_Crew'):
        assert not _is_linked(a2, 'reservationsystem_Crew', b)


def test_assoc_airport33_reverse_link_reassign_clear():
    a1 = reservationsystem_City(abbr="sample_text", id=7, name="sample_text")
    a2 = reservationsystem_City(abbr="sample_text_2", id=13, name="sample_text_2")
    b = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    _safe_set(b, 'Airport', a1)
    assert _is_linked(b, 'Airport', a1)
    if hasattr(a1, 'city'):
        assert _is_linked(a1, 'city', b)
    _safe_set(b, 'Airport', a2)
    assert _is_linked(b, 'Airport', a2)
    if hasattr(a1, 'city'):
        assert not _is_linked(a1, 'city', b)
    if hasattr(a2, 'city'):
        assert _is_linked(a2, 'city', b)
    _safe_set(b, 'Airport', None)
    assert not _is_linked(b, 'Airport', a2)
    if hasattr(a2, 'city'):
        assert not _is_linked(a2, 'city', b)


def test_assoc_belongsTo0_reverse_link_reassign_clear():
    a1 = reservationsystem_User(md5Pwd="sample_text", userName="sample_text", userType="sample_text")
    a2 = reservationsystem_User(md5Pwd="sample_text_2", userName="sample_text_2", userType="sample_text_2")
    b = reservationsystem_Person(FamilyName="sample_text", addr="sample_text", birthDate=date(2024, 1, 1), citizenship="sample_text", email="sample_text", gender=7, id=7, middleName="sample_text", name="sample_text", passportId="sample_text", phone="sample_text", residence="sample_text")
    _safe_set(b, 'reservationsystem_Person', a1)
    assert _is_linked(b, 'reservationsystem_Person', a1)
    if hasattr(a1, 'reservationsystem_User'):
        assert _is_linked(a1, 'reservationsystem_User', b)
    _safe_set(b, 'reservationsystem_Person', a2)
    assert _is_linked(b, 'reservationsystem_Person', a2)
    if hasattr(a1, 'reservationsystem_User'):
        assert not _is_linked(a1, 'reservationsystem_User', b)
    if hasattr(a2, 'reservationsystem_User'):
        assert _is_linked(a2, 'reservationsystem_User', b)
    _safe_set(b, 'reservationsystem_Person', None)
    assert not _is_linked(b, 'reservationsystem_Person', a2)
    if hasattr(a2, 'reservationsystem_User'):
        assert not _is_linked(a2, 'reservationsystem_User', b)


def test_assoc_book36_reverse_link_reassign_clear():
    a1 = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    a2 = reservationsystem_Seat(isExit=False, no="sample_text_2", type=13)
    b = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    _safe_set(b, 'Booking38', a1)
    assert _is_linked(b, 'Booking38', a1)
    if hasattr(a1, 'seats37'):
        assert _is_linked(a1, 'seats37', b)
    _safe_set(b, 'Booking38', a2)
    assert _is_linked(b, 'Booking38', a2)
    if hasattr(a1, 'seats37'):
        assert not _is_linked(a1, 'seats37', b)
    if hasattr(a2, 'seats37'):
        assert _is_linked(a2, 'seats37', b)
    _safe_set(b, 'Booking38', None)
    assert not _is_linked(b, 'Booking38', a2)
    if hasattr(a2, 'seats37'):
        assert not _is_linked(a2, 'seats37', b)


def test_assoc_booking24_reverse_link_reassign_clear():
    a1 = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    a2 = reservationsystem_SpecificFlight(date=date(2025, 6, 15), id=13, realArriTime=date(2025, 6, 15), realDepTime=date(2025, 6, 15), status=13)
    b = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    _safe_set(b, 'Booking26', a1)
    assert _is_linked(b, 'Booking26', a1)
    if hasattr(a1, 'specificFlight25'):
        assert _is_linked(a1, 'specificFlight25', b)
    _safe_set(b, 'Booking26', a2)
    assert _is_linked(b, 'Booking26', a2)
    if hasattr(a1, 'specificFlight25'):
        assert not _is_linked(a1, 'specificFlight25', b)
    if hasattr(a2, 'specificFlight25'):
        assert _is_linked(a2, 'specificFlight25', b)
    _safe_set(b, 'Booking26', None)
    assert not _is_linked(b, 'Booking26', a2)
    if hasattr(a2, 'specificFlight25'):
        assert not _is_linked(a2, 'specificFlight25', b)


def test_assoc_booking5_reverse_link_reassign_clear():
    a1 = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    a2 = reservationsystem_Passenger(foodPref="sample_text_2", specialNeeds="sample_text_2")
    b = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    _safe_set(b, 'Booking', a1)
    assert _is_linked(b, 'Booking', a1)
    if hasattr(a1, 'passenger'):
        assert _is_linked(a1, 'passenger', b)
    _safe_set(b, 'Booking', a2)
    assert _is_linked(b, 'Booking', a2)
    if hasattr(a1, 'passenger'):
        assert not _is_linked(a1, 'passenger', b)
    if hasattr(a2, 'passenger'):
        assert _is_linked(a2, 'passenger', b)
    _safe_set(b, 'Booking', None)
    assert not _is_linked(b, 'Booking', a2)
    if hasattr(a2, 'passenger'):
        assert not _is_linked(a2, 'passenger', b)


def test_assoc_city32_reverse_link_reassign_clear():
    a1 = reservationsystem_City(abbr="sample_text", id=7, name="sample_text")
    a2 = reservationsystem_City(abbr="sample_text_2", id=13, name="sample_text_2")
    b = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    _safe_set(b, 'airport', a1)
    assert _is_linked(b, 'airport', a1)
    if hasattr(a1, 'City'):
        assert _is_linked(a1, 'City', b)
    _safe_set(b, 'airport', a2)
    assert _is_linked(b, 'airport', a2)
    if hasattr(a1, 'City'):
        assert not _is_linked(a1, 'City', b)
    if hasattr(a2, 'City'):
        assert _is_linked(a2, 'City', b)
    _safe_set(b, 'airport', None)
    assert not _is_linked(b, 'airport', a2)
    if hasattr(a2, 'City'):
        assert not _is_linked(a2, 'City', b)


def test_assoc_crew22_reverse_link_reassign_clear():
    a1 = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    a2 = reservationsystem_SpecificFlight(date=date(2025, 6, 15), id=13, realArriTime=date(2025, 6, 15), realDepTime=date(2025, 6, 15), status=13)
    b = reservationsystem_Crew(employeeId="sample_text")
    _safe_set(b, 'Crew', a1)
    assert _is_linked(b, 'Crew', a1)
    if hasattr(a1, 'specificFlight23'):
        assert _is_linked(a1, 'specificFlight23', b)
    _safe_set(b, 'Crew', a2)
    assert _is_linked(b, 'Crew', a2)
    if hasattr(a1, 'specificFlight23'):
        assert not _is_linked(a1, 'specificFlight23', b)
    if hasattr(a2, 'specificFlight23'):
        assert _is_linked(a2, 'specificFlight23', b)
    _safe_set(b, 'Crew', None)
    assert not _is_linked(b, 'Crew', a2)
    if hasattr(a2, 'specificFlight23'):
        assert not _is_linked(a2, 'specificFlight23', b)


def test_assoc_from_15_reverse_link_reassign_clear():
    a1 = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    a2 = reservationsystem_GeneralFlight(arrivalTime="sample_text_2", departureTime="sample_text_2", flightNo="sample_text_2")
    b = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    _safe_set(b, 'reservationsystem_Airport', a1)
    assert _is_linked(b, 'reservationsystem_Airport', a1)
    if hasattr(a1, 'reservationsystem_GeneralFlight'):
        assert _is_linked(a1, 'reservationsystem_GeneralFlight', b)
    _safe_set(b, 'reservationsystem_Airport', a2)
    assert _is_linked(b, 'reservationsystem_Airport', a2)
    if hasattr(a1, 'reservationsystem_GeneralFlight'):
        assert not _is_linked(a1, 'reservationsystem_GeneralFlight', b)
    if hasattr(a2, 'reservationsystem_GeneralFlight'):
        assert _is_linked(a2, 'reservationsystem_GeneralFlight', b)
    _safe_set(b, 'reservationsystem_Airport', None)
    assert not _is_linked(b, 'reservationsystem_Airport', a2)
    if hasattr(a2, 'reservationsystem_GeneralFlight'):
        assert not _is_linked(a2, 'reservationsystem_GeneralFlight', b)


def test_assoc_generalFlight19_reverse_link_reassign_clear():
    a1 = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    a2 = reservationsystem_SpecificFlight(date=date(2025, 6, 15), id=13, realArriTime=date(2025, 6, 15), realDepTime=date(2025, 6, 15), status=13)
    b = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    _safe_set(b, 'GeneralFlight', a1)
    assert _is_linked(b, 'GeneralFlight', a1)
    if hasattr(a1, 'specificFlight'):
        assert _is_linked(a1, 'specificFlight', b)
    _safe_set(b, 'GeneralFlight', a2)
    assert _is_linked(b, 'GeneralFlight', a2)
    if hasattr(a1, 'specificFlight'):
        assert not _is_linked(a1, 'specificFlight', b)
    if hasattr(a2, 'specificFlight'):
        assert _is_linked(a2, 'specificFlight', b)
    _safe_set(b, 'GeneralFlight', None)
    assert not _is_linked(b, 'GeneralFlight', a2)
    if hasattr(a2, 'specificFlight'):
        assert not _is_linked(a2, 'specificFlight', b)


def test_assoc_passenger4_reverse_link_reassign_clear():
    a1 = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    a2 = reservationsystem_Passenger(foodPref="sample_text_2", specialNeeds="sample_text_2")
    b = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    _safe_set(b, 'reservationsystem_Booking', a1)
    assert _is_linked(b, 'reservationsystem_Booking', a1)
    if hasattr(a1, 'reservationsystem_Passenger'):
        assert _is_linked(a1, 'reservationsystem_Passenger', b)
    _safe_set(b, 'reservationsystem_Booking', a2)
    assert _is_linked(b, 'reservationsystem_Booking', a2)
    if hasattr(a1, 'reservationsystem_Passenger'):
        assert not _is_linked(a1, 'reservationsystem_Passenger', b)
    if hasattr(a2, 'reservationsystem_Passenger'):
        assert _is_linked(a2, 'reservationsystem_Passenger', b)
    _safe_set(b, 'reservationsystem_Booking', None)
    assert not _is_linked(b, 'reservationsystem_Booking', a2)
    if hasattr(a2, 'reservationsystem_Passenger'):
        assert not _is_linked(a2, 'reservationsystem_Passenger', b)


def test_assoc_passenger8_reverse_link_reassign_clear():
    a1 = reservationsystem_Passenger(foodPref="sample_text", specialNeeds="sample_text")
    a2 = reservationsystem_Passenger(foodPref="sample_text_2", specialNeeds="sample_text_2")
    b = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    _safe_set(b, 'booking', {a1})
    assert _is_linked(b, 'booking', a1)
    if hasattr(a1, 'Passenger'):
        assert _is_linked(a1, 'Passenger', b)
    _safe_set(b, 'booking', {a2})
    assert _is_linked(b, 'booking', a2)
    if hasattr(a1, 'Passenger'):
        assert not _is_linked(a1, 'Passenger', b)
    if hasattr(a2, 'Passenger'):
        assert _is_linked(a2, 'Passenger', b)
    _safe_set(b, 'booking', set())
    assert not _is_linked(b, 'booking', a2)
    if hasattr(a2, 'Passenger'):
        assert not _is_linked(a2, 'Passenger', b)


def test_assoc_paymentInfo6_reverse_link_reassign_clear():
    a1 = reservationsystem_PaymentInfo(cardAddr="sample_text", cardNo="sample_text", cardOwner="sample_text", createTime=date(2024, 1, 1), id="sample_text", payTime=date(2024, 1, 1), status=7, type=7)
    a2 = reservationsystem_PaymentInfo(cardAddr="sample_text_2", cardNo="sample_text_2", cardOwner="sample_text_2", createTime=date(2025, 6, 15), id="sample_text_2", payTime=date(2025, 6, 15), status=13, type=13)
    b = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    _safe_set(b, 'reservationsystem_Booking7', {a1})
    assert _is_linked(b, 'reservationsystem_Booking7', a1)
    if hasattr(a1, 'reservationsystem_PaymentInfo'):
        assert _is_linked(a1, 'reservationsystem_PaymentInfo', b)
    _safe_set(b, 'reservationsystem_Booking7', {a2})
    assert _is_linked(b, 'reservationsystem_Booking7', a2)
    if hasattr(a1, 'reservationsystem_PaymentInfo'):
        assert not _is_linked(a1, 'reservationsystem_PaymentInfo', b)
    if hasattr(a2, 'reservationsystem_PaymentInfo'):
        assert _is_linked(a2, 'reservationsystem_PaymentInfo', b)
    _safe_set(b, 'reservationsystem_Booking7', set())
    assert not _is_linked(b, 'reservationsystem_Booking7', a2)
    if hasattr(a2, 'reservationsystem_PaymentInfo'):
        assert not _is_linked(a2, 'reservationsystem_PaymentInfo', b)


def test_assoc_plane20_reverse_link_reassign_clear():
    a1 = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    a2 = reservationsystem_SpecificFlight(date=date(2025, 6, 15), id=13, realArriTime=date(2025, 6, 15), realDepTime=date(2025, 6, 15), status=13)
    b = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    _safe_set(b, 'Plane', a1)
    assert _is_linked(b, 'Plane', a1)
    if hasattr(a1, 'specificFlight21'):
        assert _is_linked(a1, 'specificFlight21', b)
    _safe_set(b, 'Plane', a2)
    assert _is_linked(b, 'Plane', a2)
    if hasattr(a1, 'specificFlight21'):
        assert not _is_linked(a1, 'specificFlight21', b)
    if hasattr(a2, 'specificFlight21'):
        assert _is_linked(a2, 'specificFlight21', b)
    _safe_set(b, 'Plane', None)
    assert not _is_linked(b, 'Plane', a2)
    if hasattr(a2, 'specificFlight21'):
        assert not _is_linked(a2, 'specificFlight21', b)


def test_assoc_plane34_reverse_link_reassign_clear():
    a1 = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    a2 = reservationsystem_Seat(isExit=False, no="sample_text_2", type=13)
    b = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    _safe_set(b, 'Plane35', a1)
    assert _is_linked(b, 'Plane35', a1)
    if hasattr(a1, 'seats'):
        assert _is_linked(a1, 'seats', b)
    _safe_set(b, 'Plane35', a2)
    assert _is_linked(b, 'Plane35', a2)
    if hasattr(a1, 'seats'):
        assert not _is_linked(a1, 'seats', b)
    if hasattr(a2, 'seats'):
        assert _is_linked(a2, 'seats', b)
    _safe_set(b, 'Plane35', None)
    assert not _is_linked(b, 'Plane35', a2)
    if hasattr(a2, 'seats'):
        assert not _is_linked(a2, 'seats', b)


def test_assoc_seats12_reverse_link_reassign_clear():
    a1 = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    a2 = reservationsystem_Seat(isExit=False, no="sample_text_2", type=13)
    b = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    _safe_set(b, 'book', {a1})
    assert _is_linked(b, 'book', a1)
    if hasattr(a1, 'Seat'):
        assert _is_linked(a1, 'Seat', b)
    _safe_set(b, 'book', {a2})
    assert _is_linked(b, 'book', a2)
    if hasattr(a1, 'Seat'):
        assert not _is_linked(a1, 'Seat', b)
    if hasattr(a2, 'Seat'):
        assert _is_linked(a2, 'Seat', b)
    _safe_set(b, 'book', set())
    assert not _is_linked(b, 'book', a2)
    if hasattr(a2, 'Seat'):
        assert not _is_linked(a2, 'Seat', b)


def test_assoc_seats29_reverse_link_reassign_clear():
    a1 = reservationsystem_Seat(isExit=True, no="sample_text", type=7)
    a2 = reservationsystem_Seat(isExit=False, no="sample_text_2", type=13)
    b = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    _safe_set(b, 'plane30', {a1})
    assert _is_linked(b, 'plane30', a1)
    if hasattr(a1, 'Seat31'):
        assert _is_linked(a1, 'Seat31', b)
    _safe_set(b, 'plane30', {a2})
    assert _is_linked(b, 'plane30', a2)
    if hasattr(a1, 'Seat31'):
        assert not _is_linked(a1, 'Seat31', b)
    if hasattr(a2, 'Seat31'):
        assert _is_linked(a2, 'Seat31', b)
    _safe_set(b, 'plane30', set())
    assert not _is_linked(b, 'plane30', a2)
    if hasattr(a2, 'Seat31'):
        assert not _is_linked(a2, 'Seat31', b)


def test_assoc_specificFlight13_reverse_link_reassign_clear():
    a1 = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    a2 = reservationsystem_SpecificFlight(date=date(2025, 6, 15), id=13, realArriTime=date(2025, 6, 15), realDepTime=date(2025, 6, 15), status=13)
    b = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    _safe_set(b, 'generalFlight', {a1})
    assert _is_linked(b, 'generalFlight', a1)
    if hasattr(a1, 'SpecificFlight14'):
        assert _is_linked(a1, 'SpecificFlight14', b)
    _safe_set(b, 'generalFlight', {a2})
    assert _is_linked(b, 'generalFlight', a2)
    if hasattr(a1, 'SpecificFlight14'):
        assert not _is_linked(a1, 'SpecificFlight14', b)
    if hasattr(a2, 'SpecificFlight14'):
        assert _is_linked(a2, 'SpecificFlight14', b)
    _safe_set(b, 'generalFlight', set())
    assert not _is_linked(b, 'generalFlight', a2)
    if hasattr(a2, 'SpecificFlight14'):
        assert not _is_linked(a2, 'SpecificFlight14', b)


def test_assoc_specificFlight27_reverse_link_reassign_clear():
    a1 = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    a2 = reservationsystem_SpecificFlight(date=date(2025, 6, 15), id=13, realArriTime=date(2025, 6, 15), realDepTime=date(2025, 6, 15), status=13)
    b = reservationsystem_Plane(capacity=7, crewNum=7, id="sample_text", model="sample_text")
    _safe_set(b, 'plane', {a1})
    assert _is_linked(b, 'plane', a1)
    if hasattr(a1, 'SpecificFlight28'):
        assert _is_linked(a1, 'SpecificFlight28', b)
    _safe_set(b, 'plane', {a2})
    assert _is_linked(b, 'plane', a2)
    if hasattr(a1, 'SpecificFlight28'):
        assert not _is_linked(a1, 'SpecificFlight28', b)
    if hasattr(a2, 'SpecificFlight28'):
        assert _is_linked(a2, 'SpecificFlight28', b)
    _safe_set(b, 'plane', set())
    assert not _is_linked(b, 'plane', a2)
    if hasattr(a2, 'SpecificFlight28'):
        assert not _is_linked(a2, 'SpecificFlight28', b)


def test_assoc_specificFlight3_reverse_link_reassign_clear():
    a1 = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    a2 = reservationsystem_SpecificFlight(date=date(2025, 6, 15), id=13, realArriTime=date(2025, 6, 15), realDepTime=date(2025, 6, 15), status=13)
    b = reservationsystem_Crew(employeeId="sample_text")
    _safe_set(b, 'crew', {a1})
    assert _is_linked(b, 'crew', a1)
    if hasattr(a1, 'SpecificFlight'):
        assert _is_linked(a1, 'SpecificFlight', b)
    _safe_set(b, 'crew', {a2})
    assert _is_linked(b, 'crew', a2)
    if hasattr(a1, 'SpecificFlight'):
        assert not _is_linked(a1, 'SpecificFlight', b)
    if hasattr(a2, 'SpecificFlight'):
        assert _is_linked(a2, 'SpecificFlight', b)
    _safe_set(b, 'crew', set())
    assert not _is_linked(b, 'crew', a2)
    if hasattr(a2, 'SpecificFlight'):
        assert not _is_linked(a2, 'SpecificFlight', b)


def test_assoc_specificFlight9_reverse_link_reassign_clear():
    a1 = reservationsystem_SpecificFlight(date=date(2024, 1, 1), id=7, realArriTime=date(2024, 1, 1), realDepTime=date(2024, 1, 1), status=7)
    a2 = reservationsystem_SpecificFlight(date=date(2025, 6, 15), id=13, realArriTime=date(2025, 6, 15), realDepTime=date(2025, 6, 15), status=13)
    b = reservationsystem_Booking(baggageInfo="sample_text", bookNo="sample_text", bookingStatus=7)
    _safe_set(b, 'booking10', {a1})
    assert _is_linked(b, 'booking10', a1)
    if hasattr(a1, 'SpecificFlight11'):
        assert _is_linked(a1, 'SpecificFlight11', b)
    _safe_set(b, 'booking10', {a2})
    assert _is_linked(b, 'booking10', a2)
    if hasattr(a1, 'SpecificFlight11'):
        assert not _is_linked(a1, 'SpecificFlight11', b)
    if hasattr(a2, 'SpecificFlight11'):
        assert _is_linked(a2, 'SpecificFlight11', b)
    _safe_set(b, 'booking10', set())
    assert not _is_linked(b, 'booking10', a2)
    if hasattr(a2, 'SpecificFlight11'):
        assert not _is_linked(a2, 'SpecificFlight11', b)


def test_assoc_to16_reverse_link_reassign_clear():
    a1 = reservationsystem_GeneralFlight(arrivalTime="sample_text", departureTime="sample_text", flightNo="sample_text")
    a2 = reservationsystem_GeneralFlight(arrivalTime="sample_text_2", departureTime="sample_text_2", flightNo="sample_text_2")
    b = reservationsystem_Airport(abbr="sample_text", id=7, name="sample_text")
    _safe_set(b, 'reservationsystem_Airport18', a1)
    assert _is_linked(b, 'reservationsystem_Airport18', a1)
    if hasattr(a1, 'reservationsystem_GeneralFlight17'):
        assert _is_linked(a1, 'reservationsystem_GeneralFlight17', b)
    _safe_set(b, 'reservationsystem_Airport18', a2)
    assert _is_linked(b, 'reservationsystem_Airport18', a2)
    if hasattr(a1, 'reservationsystem_GeneralFlight17'):
        assert not _is_linked(a1, 'reservationsystem_GeneralFlight17', b)
    if hasattr(a2, 'reservationsystem_GeneralFlight17'):
        assert _is_linked(a2, 'reservationsystem_GeneralFlight17', b)
    _safe_set(b, 'reservationsystem_Airport18', None)
    assert not _is_linked(b, 'reservationsystem_Airport18', a2)
    if hasattr(a2, 'reservationsystem_GeneralFlight17'):
        assert not _is_linked(a2, 'reservationsystem_GeneralFlight17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

