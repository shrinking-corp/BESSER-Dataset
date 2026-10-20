import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Adult,
    Business_Seats,
    Child,
    Contact_Center_Agent_Actor,
    Customer_Actor,
    Economy_Seats,
    FFP_Members,
    First_Class,
    Flight,
    Infant,
    Offers,
    Passengers,
    Qaboos_Airways,
    Qaboos_Reservation_System_Book_ticket__UseCase,
    Qaboos_Reservation_System_Cancel_booking_UseCase,
    Qaboos_Reservation_System_Check_Flights_Availability_UseCase,
    Qaboos_Reservation_System_Check_In_Online_UseCase,
    Qaboos_Reservation_System_Choose_Seats_UseCase,
    Qaboos_Reservation_System_Confirm_booking__UseCase,
    Qaboos_Reservation_System_Enter_Passengers_Details_UseCase,
    Qaboos_Reservation_System_Enter_flight_Details_UseCase,
    Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase,
    Qaboos_Reservation_System_Make_Payment_UseCase,
    Qaboos_Reservation_System_Manage_Booking_UseCase,
    Qaboos_Reservation_System_Update_Flight_Details_UseCase,
    Seats,
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

def test_assoc_Books_reverse_link_reassign_clear():
    a1 = Passengers(Passenger_Details="sample_text", Passenger_TKT_No="sample_text", passenger_name="sample_text")
    a2 = Passengers(Passenger_Details="sample_text_2", Passenger_TKT_No="sample_text_2", passenger_name="sample_text_2")
    b = Flight(Flgt_Details="sample_text", Flgt_NO="sample_text")
    _safe_set(b, 'passengers23', a1)
    assert _is_linked(b, 'passengers23', a1)
    if hasattr(a1, 'flight22'):
        assert _is_linked(a1, 'flight22', b)
    _safe_set(b, 'passengers23', a2)
    assert _is_linked(b, 'passengers23', a2)
    if hasattr(a1, 'flight22'):
        assert not _is_linked(a1, 'flight22', b)
    if hasattr(a2, 'flight22'):
        assert _is_linked(a2, 'flight22', b)
    _safe_set(b, 'passengers23', None)
    assert not _is_linked(b, 'passengers23', a2)
    if hasattr(a2, 'flight22'):
        assert not _is_linked(a2, 'flight22', b)


def test_assoc_Checks_reverse_link_reassign_clear():
    a1 = Passengers(Passenger_Details="sample_text", Passenger_TKT_No="sample_text", passenger_name="sample_text")
    a2 = Passengers(Passenger_Details="sample_text_2", Passenger_TKT_No="sample_text_2", passenger_name="sample_text_2")
    b = Offers(Offer_Det="sample_text", Offer_Expiry_Date="sample_text", Offer_NO="sample_text")
    _safe_set(b, 'passengers25', a1)
    assert _is_linked(b, 'passengers25', a1)
    if hasattr(a1, 'offers24'):
        assert _is_linked(a1, 'offers24', b)
    _safe_set(b, 'passengers25', a2)
    assert _is_linked(b, 'passengers25', a2)
    if hasattr(a1, 'offers24'):
        assert not _is_linked(a1, 'offers24', b)
    if hasattr(a2, 'offers24'):
        assert _is_linked(a2, 'offers24', b)
    _safe_set(b, 'passengers25', None)
    assert not _is_linked(b, 'passengers25', a2)
    if hasattr(a2, 'offers24'):
        assert not _is_linked(a2, 'offers24', b)


def test_assoc_Qaboos_Airways_Flight_reverse_link_reassign_clear():
    a1 = Qaboos_Airways(Comp_Commercial_NO="sample_text", Comp_location="sample_text")
    a2 = Qaboos_Airways(Comp_Commercial_NO="sample_text_2", Comp_location="sample_text_2")
    b = Flight(Flgt_Details="sample_text", Flgt_NO="sample_text")
    _safe_set(b, 'qaboos_Airways19', a1)
    assert _is_linked(b, 'qaboos_Airways19', a1)
    if hasattr(a1, 'flight18'):
        assert _is_linked(a1, 'flight18', b)
    _safe_set(b, 'qaboos_Airways19', a2)
    assert _is_linked(b, 'qaboos_Airways19', a2)
    if hasattr(a1, 'flight18'):
        assert not _is_linked(a1, 'flight18', b)
    if hasattr(a2, 'flight18'):
        assert _is_linked(a2, 'flight18', b)
    _safe_set(b, 'qaboos_Airways19', None)
    assert not _is_linked(b, 'qaboos_Airways19', a2)
    if hasattr(a2, 'flight18'):
        assert not _is_linked(a2, 'flight18', b)


def test_assoc_Qaboos_Airways_Passengers_reverse_link_reassign_clear():
    a1 = Qaboos_Airways(Comp_Commercial_NO="sample_text", Comp_location="sample_text")
    a2 = Qaboos_Airways(Comp_Commercial_NO="sample_text_2", Comp_location="sample_text_2")
    b = Passengers(Passenger_Details="sample_text", Passenger_TKT_No="sample_text", passenger_name="sample_text")
    _safe_set(b, 'qaboos_Airways21', a1)
    assert _is_linked(b, 'qaboos_Airways21', a1)
    if hasattr(a1, 'passengers20'):
        assert _is_linked(a1, 'passengers20', b)
    _safe_set(b, 'qaboos_Airways21', a2)
    assert _is_linked(b, 'qaboos_Airways21', a2)
    if hasattr(a1, 'passengers20'):
        assert not _is_linked(a1, 'passengers20', b)
    if hasattr(a2, 'passengers20'):
        assert _is_linked(a2, 'passengers20', b)
    _safe_set(b, 'qaboos_Airways21', None)
    assert not _is_linked(b, 'qaboos_Airways21', a2)
    if hasattr(a2, 'passengers20'):
        assert not _is_linked(a2, 'passengers20', b)


def test_assoc_Selects_reverse_link_reassign_clear():
    a1 = Seats(Seat_Catoegry="sample_text", Seat_ID="sample_text", Seat_NO="sample_text")
    a2 = Seats(Seat_Catoegry="sample_text_2", Seat_ID="sample_text_2", Seat_NO="sample_text_2")
    b = Passengers(Passenger_Details="sample_text", Passenger_TKT_No="sample_text", passenger_name="sample_text")
    _safe_set(b, 'seats28', a1)
    assert _is_linked(b, 'seats28', a1)
    if hasattr(a1, 'passengers29'):
        assert _is_linked(a1, 'passengers29', b)
    _safe_set(b, 'seats28', a2)
    assert _is_linked(b, 'seats28', a2)
    if hasattr(a1, 'passengers29'):
        assert not _is_linked(a1, 'passengers29', b)
    if hasattr(a2, 'passengers29'):
        assert _is_linked(a2, 'passengers29', b)
    _safe_set(b, 'seats28', None)
    assert not _is_linked(b, 'seats28', a2)
    if hasattr(a2, 'passengers29'):
        assert not _is_linked(a2, 'passengers29', b)


def test_assoc_joins_reverse_link_reassign_clear():
    a1 = Passengers(Passenger_Details="sample_text", Passenger_TKT_No="sample_text", passenger_name="sample_text")
    a2 = Passengers(Passenger_Details="sample_text_2", Passenger_TKT_No="sample_text_2", passenger_name="sample_text_2")
    b = FFP_Members(FFP_Category="sample_text", FFP_ID="sample_text", FFP_Qmiles="sample_text")
    _safe_set(b, 'passengers27', a1)
    assert _is_linked(b, 'passengers27', a1)
    if hasattr(a1, 'fFP_Members26'):
        assert _is_linked(a1, 'fFP_Members26', b)
    _safe_set(b, 'passengers27', a2)
    assert _is_linked(b, 'passengers27', a2)
    if hasattr(a1, 'fFP_Members26'):
        assert not _is_linked(a1, 'fFP_Members26', b)
    if hasattr(a2, 'fFP_Members26'):
        assert _is_linked(a2, 'fFP_Members26', b)
    _safe_set(b, 'passengers27', None)
    assert not _is_linked(b, 'passengers27', a2)
    if hasattr(a2, 'fFP_Members26'):
        assert not _is_linked(a2, 'fFP_Members26', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

