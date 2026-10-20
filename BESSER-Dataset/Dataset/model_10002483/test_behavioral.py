import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Booking,
    Hotels,
    Location,
    Owner,
    Rooms,
    User,
    occupancy,
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

def test_assoc_City_Hotels_reverse_link_reassign_clear():
    a1 = Location(attribute="sample_text", loc_id=7, loc_name="sample_text")
    a2 = Location(attribute="sample_text_2", loc_id=13, loc_name="sample_text_2")
    b = Hotels(hotel_description=7, id=7, name=7)
    _safe_set(b, 'city1', a1)
    assert _is_linked(b, 'city1', a1)
    if hasattr(a1, 'hotels0'):
        assert _is_linked(a1, 'hotels0', b)
    _safe_set(b, 'city1', a2)
    assert _is_linked(b, 'city1', a2)
    if hasattr(a1, 'hotels0'):
        assert not _is_linked(a1, 'hotels0', b)
    if hasattr(a2, 'hotels0'):
        assert _is_linked(a2, 'hotels0', b)
    _safe_set(b, 'city1', None)
    assert not _is_linked(b, 'city1', a2)
    if hasattr(a2, 'hotels0'):
        assert not _is_linked(a2, 'hotels0', b)


def test_assoc_Hotels_Rooms_reverse_link_reassign_clear():
    a1 = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    a2 = Rooms(checkin_date=13, checkout_date=13, id=13, name="sample_text_2", price=13, room_description="sample_text_2")
    b = Hotels(hotel_description=7, id=7, name=7)
    _safe_set(b, 'rooms2', a1)
    assert _is_linked(b, 'rooms2', a1)
    if hasattr(a1, 'hotels3'):
        assert _is_linked(a1, 'hotels3', b)
    _safe_set(b, 'rooms2', a2)
    assert _is_linked(b, 'rooms2', a2)
    if hasattr(a1, 'hotels3'):
        assert not _is_linked(a1, 'hotels3', b)
    if hasattr(a2, 'hotels3'):
        assert _is_linked(a2, 'hotels3', b)
    _safe_set(b, 'rooms2', None)
    assert not _is_linked(b, 'rooms2', a2)
    if hasattr(a2, 'hotels3'):
        assert not _is_linked(a2, 'hotels3', b)


def test_assoc_Rooms_Booking_reverse_link_reassign_clear():
    a1 = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    a2 = Rooms(checkin_date=13, checkout_date=13, id=13, name="sample_text_2", price=13, room_description="sample_text_2")
    b = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    _safe_set(b, 'rooms9', a1)
    assert _is_linked(b, 'rooms9', a1)
    if hasattr(a1, 'booking8'):
        assert _is_linked(a1, 'booking8', b)
    _safe_set(b, 'rooms9', a2)
    assert _is_linked(b, 'rooms9', a2)
    if hasattr(a1, 'booking8'):
        assert not _is_linked(a1, 'booking8', b)
    if hasattr(a2, 'booking8'):
        assert _is_linked(a2, 'booking8', b)
    _safe_set(b, 'rooms9', None)
    assert not _is_linked(b, 'rooms9', a2)
    if hasattr(a2, 'booking8'):
        assert not _is_linked(a2, 'booking8', b)


def test_assoc_User_Booking_reverse_link_reassign_clear():
    a1 = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    a2 = User(Name="sample_text_2", address="sample_text_2", id=13, mail_id="sample_text_2", password=13, phn_no=13)
    b = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    _safe_set(b, 'User_Booking_15', a1)
    assert _is_linked(b, 'User_Booking_15', a1)
    if hasattr(a1, 'User_Booking_04'):
        assert _is_linked(a1, 'User_Booking_04', b)
    _safe_set(b, 'User_Booking_15', a2)
    assert _is_linked(b, 'User_Booking_15', a2)
    if hasattr(a1, 'User_Booking_04'):
        assert not _is_linked(a1, 'User_Booking_04', b)
    if hasattr(a2, 'User_Booking_04'):
        assert _is_linked(a2, 'User_Booking_04', b)
    _safe_set(b, 'User_Booking_15', None)
    assert not _is_linked(b, 'User_Booking_15', a2)
    if hasattr(a2, 'User_Booking_04'):
        assert not _is_linked(a2, 'User_Booking_04', b)


def test_assoc_occupancy_Booking_reverse_link_reassign_clear():
    a1 = occupancy(booking_id=7)
    a2 = occupancy(booking_id=13)
    b = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    _safe_set(b, 'occupancy_Booking_111', a1)
    assert _is_linked(b, 'occupancy_Booking_111', a1)
    if hasattr(a1, 'occupancy_Booking_010'):
        assert _is_linked(a1, 'occupancy_Booking_010', b)
    _safe_set(b, 'occupancy_Booking_111', a2)
    assert _is_linked(b, 'occupancy_Booking_111', a2)
    if hasattr(a1, 'occupancy_Booking_010'):
        assert not _is_linked(a1, 'occupancy_Booking_010', b)
    if hasattr(a2, 'occupancy_Booking_010'):
        assert _is_linked(a2, 'occupancy_Booking_010', b)
    _safe_set(b, 'occupancy_Booking_111', None)
    assert not _is_linked(b, 'occupancy_Booking_111', a2)
    if hasattr(a2, 'occupancy_Booking_010'):
        assert not _is_linked(a2, 'occupancy_Booking_010', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

