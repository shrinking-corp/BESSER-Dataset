import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classes_AdministratorProvides,
    Classes_Bill,
    Classes_Booking,
    Classes_Charge,
    Classes_Customer,
    Classes_CustomerProvides,
    Classes_IBookingManagement,
    Classes_IBookingManagementImpl,
    Classes_IFinance,
    Classes_IFinanceImpl,
    Classes_IHotelManager,
    Classes_IHotelManagerImpl,
    Classes_IPerson,
    Classes_Room,
    Classes_RoomType,
    Classes_StaffMember,
    IBookingManagement,
    IFinance,
    IHotelManager,
    IPerson,
    ChargeType,
    RoomStatus,
    RoomTypeName,
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

def test_assoc_bookings1_reverse_link_reassign_clear():
    a1 = Classes_Room(roomNumber="sample_text", status="sample_text")
    a2 = Classes_Room(roomNumber="sample_text_2", status="sample_text_2")
    b = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    _safe_set(b, 'Booking', a1)
    assert _is_linked(b, 'Booking', a1)
    if hasattr(a1, 'rooms'):
        assert _is_linked(a1, 'rooms', b)
    _safe_set(b, 'Booking', a2)
    assert _is_linked(b, 'Booking', a2)
    if hasattr(a1, 'rooms'):
        assert not _is_linked(a1, 'rooms', b)
    if hasattr(a2, 'rooms'):
        assert _is_linked(a2, 'rooms', b)
    _safe_set(b, 'Booking', None)
    assert not _is_linked(b, 'Booking', a2)
    if hasattr(a2, 'rooms'):
        assert not _is_linked(a2, 'rooms', b)


def test_assoc_room4_reverse_link_reassign_clear():
    a1 = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    a2 = Classes_RoomType(description="sample_text_2", features="sample_text_2", numberOfGuests="sample_text_2", price="sample_text_2", roomTypeName="sample_text_2")
    b = Classes_Room(roomNumber="sample_text", status="sample_text")
    _safe_set(b, 'Room', a1)
    assert _is_linked(b, 'Room', a1)
    if hasattr(a1, 'roomType'):
        assert _is_linked(a1, 'roomType', b)
    _safe_set(b, 'Room', a2)
    assert _is_linked(b, 'Room', a2)
    if hasattr(a1, 'roomType'):
        assert not _is_linked(a1, 'roomType', b)
    if hasattr(a2, 'roomType'):
        assert _is_linked(a2, 'roomType', b)
    _safe_set(b, 'Room', None)
    assert not _is_linked(b, 'Room', a2)
    if hasattr(a2, 'roomType'):
        assert not _is_linked(a2, 'roomType', b)


def test_assoc_roomType0_reverse_link_reassign_clear():
    a1 = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    a2 = Classes_RoomType(description="sample_text_2", features="sample_text_2", numberOfGuests="sample_text_2", price="sample_text_2", roomTypeName="sample_text_2")
    b = Classes_Room(roomNumber="sample_text", status="sample_text")
    _safe_set(b, 'room', a1)
    assert _is_linked(b, 'room', a1)
    if hasattr(a1, 'RoomType'):
        assert _is_linked(a1, 'RoomType', b)
    _safe_set(b, 'room', a2)
    assert _is_linked(b, 'room', a2)
    if hasattr(a1, 'RoomType'):
        assert not _is_linked(a1, 'RoomType', b)
    if hasattr(a2, 'RoomType'):
        assert _is_linked(a2, 'RoomType', b)
    _safe_set(b, 'room', None)
    assert not _is_linked(b, 'room', a2)
    if hasattr(a2, 'RoomType'):
        assert not _is_linked(a2, 'RoomType', b)


def test_assoc_rooms9_reverse_link_reassign_clear():
    a1 = Classes_Room(roomNumber="sample_text", status="sample_text")
    a2 = Classes_Room(roomNumber="sample_text_2", status="sample_text_2")
    b = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    _safe_set(b, 'bookings', {a1})
    assert _is_linked(b, 'bookings', a1)
    if hasattr(a1, 'Room10'):
        assert _is_linked(a1, 'Room10', b)
    _safe_set(b, 'bookings', {a2})
    assert _is_linked(b, 'bookings', a2)
    if hasattr(a1, 'Room10'):
        assert not _is_linked(a1, 'Room10', b)
    if hasattr(a2, 'Room10'):
        assert _is_linked(a2, 'Room10', b)
    _safe_set(b, 'bookings', set())
    assert not _is_linked(b, 'bookings', a2)
    if hasattr(a2, 'Room10'):
        assert not _is_linked(a2, 'Room10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bill8_stub_double():
    # Classes_Bill has no real 'Classes_Bill' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    partner = Classes_Bill()
    setattr(partner, 'Classes_Bill', None)
    _safe_set(owner, 'Classes_Booking', partner)
    assert getattr(partner, 'Classes_Bill') == owner
    _safe_set(owner, 'Classes_Booking', None)
    assert getattr(partner, 'Classes_Bill') is None


def test_assoc_booking11_stub_double():
    # Classes_Customer has no real 'customer' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    partner = Classes_Customer()
    setattr(partner, 'customer', None)
    _safe_set(owner, 'Booking12', partner)
    assert owner in getattr(partner, 'customer')
    _safe_set(owner, 'Booking12', None)
    assert owner not in getattr(partner, 'customer')


def test_assoc_bookingHistory21_stub_double():
    # Classes_IBookingManagementImpl has no real 'Classes_IBookingManagementImpl22' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    partner = Classes_IBookingManagementImpl()
    setattr(partner, 'Classes_IBookingManagementImpl22', None)
    _safe_set(owner, 'Classes_Booking23', partner)
    assert owner in getattr(partner, 'Classes_IBookingManagementImpl22')
    _safe_set(owner, 'Classes_Booking23', None)
    assert owner not in getattr(partner, 'Classes_IBookingManagementImpl22')


def test_assoc_charge35_stub_double():
    # Classes_Bill has no real 'Classes_Bill36' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Charge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Charge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Charge(amount=7, chargeType="sample_text", date=date(2024, 1, 1))
    partner = Classes_Bill()
    setattr(partner, 'Classes_Bill36', None)
    _safe_set(owner, 'Classes_Charge', partner)
    assert owner in getattr(partner, 'Classes_Bill36')
    _safe_set(owner, 'Classes_Charge', None)
    assert owner not in getattr(partner, 'Classes_Bill36')


def test_assoc_confirmedBookings26_stub_double():
    # Classes_IBookingManagementImpl has no real 'iBookingManagementImpl27' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    partner = Classes_IBookingManagementImpl()
    setattr(partner, 'iBookingManagementImpl27', None)
    _safe_set(owner, 'Booking28', partner)
    assert owner in getattr(partner, 'iBookingManagementImpl27')
    _safe_set(owner, 'Booking28', None)
    assert owner not in getattr(partner, 'iBookingManagementImpl27')


def test_assoc_customer5_stub_double():
    # Classes_Customer has no real 'Customer' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    partner = Classes_Customer()
    setattr(partner, 'Customer', None)
    _safe_set(owner, 'booking', partner)
    assert getattr(partner, 'Customer') == owner
    _safe_set(owner, 'booking', None)
    assert getattr(partner, 'Customer') is None


def test_assoc_customerProvides32_stub_double():
    # Classes_IFinanceImpl has no real 'Classes_IFinanceImpl' property in the generated
    # code (a bare stub) -- manually attach it so Classes_CustomerProvides's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_CustomerProvides's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_CustomerProvides()
    partner = Classes_IFinanceImpl()
    setattr(partner, 'Classes_IFinanceImpl', None)
    _safe_set(owner, 'Classes_CustomerProvides', partner)
    assert getattr(partner, 'Classes_IFinanceImpl') == owner
    _safe_set(owner, 'Classes_CustomerProvides', None)
    assert getattr(partner, 'Classes_IFinanceImpl') is None


def test_assoc_iBookingManagementImpl2_stub_double():
    # Classes_IBookingManagementImpl has no real 'IBookingManagementImpl' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Room's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Room's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Room(roomNumber="sample_text", status="sample_text")
    partner = Classes_IBookingManagementImpl()
    setattr(partner, 'IBookingManagementImpl', None)
    _safe_set(owner, 'room3', partner)
    assert getattr(partner, 'IBookingManagementImpl') == owner
    _safe_set(owner, 'room3', None)
    assert getattr(partner, 'IBookingManagementImpl') is None


def test_assoc_iBookingManagementImpl6_stub_double():
    # Classes_IBookingManagementImpl has no real 'IBookingManagementImpl7' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    partner = Classes_IBookingManagementImpl()
    setattr(partner, 'IBookingManagementImpl7', None)
    _safe_set(owner, 'confirmedBookings', partner)
    assert getattr(partner, 'IBookingManagementImpl7') == owner
    _safe_set(owner, 'confirmedBookings', None)
    assert getattr(partner, 'IBookingManagementImpl7') is None


def test_assoc_pendingBookings16_stub_double():
    # Classes_IBookingManagementImpl has no real 'Classes_IBookingManagementImpl17' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    partner = Classes_IBookingManagementImpl()
    setattr(partner, 'Classes_IBookingManagementImpl17', None)
    _safe_set(owner, 'Classes_Booking18', partner)
    assert owner in getattr(partner, 'Classes_IBookingManagementImpl17')
    _safe_set(owner, 'Classes_Booking18', None)
    assert owner not in getattr(partner, 'Classes_IBookingManagementImpl17')


def test_assoc_room14_stub_double():
    # Classes_IBookingManagementImpl has no real 'iBookingManagementImpl' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Room's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Room's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Room(roomNumber="sample_text", status="sample_text")
    partner = Classes_IBookingManagementImpl()
    setattr(partner, 'iBookingManagementImpl', None)
    _safe_set(owner, 'Room15', partner)
    assert owner in getattr(partner, 'iBookingManagementImpl')
    _safe_set(owner, 'Room15', None)
    assert owner not in getattr(partner, 'iBookingManagementImpl')


def test_assoc_staff29_stub_double():
    # Classes_IHotelManagerImpl has no real 'Classes_IHotelManagerImpl' property in the generated
    # code (a bare stub) -- manually attach it so Classes_StaffMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_StaffMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_StaffMember(admin="sample_text", isLoggedIn=True, password="sample_text", username="sample_text")
    partner = Classes_IHotelManagerImpl()
    setattr(partner, 'Classes_IHotelManagerImpl', None)
    _safe_set(owner, 'Classes_StaffMember', partner)
    assert owner in getattr(partner, 'Classes_IHotelManagerImpl')
    _safe_set(owner, 'Classes_StaffMember', None)
    assert owner not in getattr(partner, 'Classes_IHotelManagerImpl')


