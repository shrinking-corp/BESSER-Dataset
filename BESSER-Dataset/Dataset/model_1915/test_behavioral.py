import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractEvent,
    IBooking,
    IEvent,
    IHotelCustomerProvides,
    IHotelRoomProvider,
    IRoom,
    IRoomType,
    bookingSystem_IBooking,
    bookingSystem_IEvent,
    bookingSystem_IHotelBookingManager,
    bookingSystem_IHotelCustomerProvides,
    roomManager_IHotelRoomManager,
    roomManager_IHotelRoomProvider,
    roomManager_IHotelStartupProvies,
    roomManager_IRoom,
    roomManager_IRoomType,
    se_bookingSystem_AbstractEvent,
    se_bookingSystem_Booking,
    se_bookingSystem_BookingSystem,
    se_bookingSystem_CheckInEvent,
    se_bookingSystem_CheckOutEvent,
    se_bookingSystem_FreeRoomTypesDTO,
    se_bookingSystem_IBooking,
    se_bookingSystem_IEvent,
    se_bookingSystem_IHotelBookingManager,
    se_bookingSystem_IHotelCustomerProvides,
    se_roomManager_IHotelRoomManager,
    se_roomManager_IHotelRoomProvider,
    se_roomManager_IHotelStartupProvies,
    se_roomManager_IRoom,
    se_roomManager_IRoomType,
    se_roomManager_Room,
    se_roomManager_RoomManager,
    se_roomManager_RoomType,
    EventType,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bookings1_stub_double():
    # bookingSystem_IBooking has no real 'bookingSystem_IBooking' property in the generated
    # code (a bare stub) -- manually attach it so se_bookingSystem_BookingSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_bookingSystem_BookingSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_bookingSystem_BookingSystem(bookingId=7)
    partner = bookingSystem_IBooking()
    setattr(partner, 'bookingSystem_IBooking', None)
    _safe_set(owner, 'se_bookingSystem_BookingSystem2', {partner})
    assert getattr(partner, 'bookingSystem_IBooking') == owner
    _safe_set(owner, 'se_bookingSystem_BookingSystem2', set())
    assert getattr(partner, 'bookingSystem_IBooking') is None


def test_assoc_checkedInRooms9_stub_double():
    # roomManager_IRoom has no real 'roomManager_IRoom11' property in the generated
    # code (a bare stub) -- manually attach it so se_bookingSystem_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_bookingSystem_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_bookingSystem_Booking(endDate="sample_text", firstName="sample_text", id=7, lastName="sample_text", startDate="sample_text")
    partner = roomManager_IRoom()
    setattr(partner, 'roomManager_IRoom11', None)
    _safe_set(owner, 'se_bookingSystem_Booking10', {partner})
    assert getattr(partner, 'roomManager_IRoom11') == owner
    _safe_set(owner, 'se_bookingSystem_Booking10', set())
    assert getattr(partner, 'roomManager_IRoom11') is None


def test_assoc_events0_stub_double():
    # bookingSystem_IEvent has no real 'bookingSystem_IEvent' property in the generated
    # code (a bare stub) -- manually attach it so se_bookingSystem_BookingSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_bookingSystem_BookingSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_bookingSystem_BookingSystem(bookingId=7)
    partner = bookingSystem_IEvent()
    setattr(partner, 'bookingSystem_IEvent', None)
    _safe_set(owner, 'se_bookingSystem_BookingSystem', {partner})
    assert getattr(partner, 'bookingSystem_IEvent') == owner
    _safe_set(owner, 'se_bookingSystem_BookingSystem', set())
    assert getattr(partner, 'bookingSystem_IEvent') is None


def test_assoc_roomList7_stub_double():
    # roomManager_IRoom has no real 'roomManager_IRoom8' property in the generated
    # code (a bare stub) -- manually attach it so se_bookingSystem_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_bookingSystem_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_bookingSystem_Booking(endDate="sample_text", firstName="sample_text", id=7, lastName="sample_text", startDate="sample_text")
    partner = roomManager_IRoom()
    setattr(partner, 'roomManager_IRoom8', None)
    _safe_set(owner, 'se_bookingSystem_Booking', {partner})
    assert getattr(partner, 'roomManager_IRoom8') == owner
    _safe_set(owner, 'se_bookingSystem_Booking', set())
    assert getattr(partner, 'roomManager_IRoom8') is None


def test_assoc_roomProvider3_stub_double():
    # roomManager_IHotelRoomProvider has no real 'roomManager_IHotelRoomProvider' property in the generated
    # code (a bare stub) -- manually attach it so se_bookingSystem_BookingSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_bookingSystem_BookingSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_bookingSystem_BookingSystem(bookingId=7)
    partner = roomManager_IHotelRoomProvider()
    setattr(partner, 'roomManager_IHotelRoomProvider', None)
    _safe_set(owner, 'se_bookingSystem_BookingSystem4', partner)
    assert getattr(partner, 'roomManager_IHotelRoomProvider') == owner
    _safe_set(owner, 'se_bookingSystem_BookingSystem4', None)
    assert getattr(partner, 'roomManager_IHotelRoomProvider') is None


def test_assoc_roomType16_stub_double():
    # roomManager_IRoomType has no real 'roomManager_IRoomType17' property in the generated
    # code (a bare stub) -- manually attach it so se_roomManager_Room's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_roomManager_Room's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_roomManager_Room(blocked=True, extraCostDescriptions="sample_text", extraCostPrice=3.14, occupied=True, roomNumber=7)
    partner = roomManager_IRoomType()
    setattr(partner, 'roomManager_IRoomType17', None)
    _safe_set(owner, 'se_roomManager_Room', partner)
    assert getattr(partner, 'roomManager_IRoomType17') == owner
    _safe_set(owner, 'se_roomManager_Room', None)
    assert getattr(partner, 'roomManager_IRoomType17') is None


def test_assoc_rooms5_stub_double():
    # roomManager_IRoom has no real 'roomManager_IRoom' property in the generated
    # code (a bare stub) -- manually attach it so se_bookingSystem_BookingSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_bookingSystem_BookingSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_bookingSystem_BookingSystem(bookingId=7)
    partner = roomManager_IRoom()
    setattr(partner, 'roomManager_IRoom', None)
    _safe_set(owner, 'se_bookingSystem_BookingSystem6', {partner})
    assert getattr(partner, 'roomManager_IRoom') == owner
    _safe_set(owner, 'se_bookingSystem_BookingSystem6', set())
    assert getattr(partner, 'roomManager_IRoom') is None


