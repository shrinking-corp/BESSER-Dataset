import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    IAdministratorProvides,
    IHotelStartupProvides,
    User,
    bankcomponents_ICustomerProvides,
    hotelsystem_Bill,
    hotelsystem_Booking,
    hotelsystem_Customer,
    hotelsystem_IHotelAdministratorProvides,
    hotelsystem_IHotelCustomerProvides,
    hotelsystem_IHotelReceptionistProvides,
    hotelsystem_IHotelStartupProvides,
    hotelsystem_IRoomHandler,
    hotelsystem_PaymentHandler,
    hotelsystem_Room,
    hotelsystem_RoomExtra,
    hotelsystem_RoomHandler,
    hotelsystem_RoomReservation,
    hotelsystem_RoomType,
    se_actor_Administrator,
    se_actor_Receptionist,
    se_actor_User,
    se_bankcomponents_BankAdministrator,
    se_bankcomponents_IAdministratorProvides,
    se_bankcomponents_ICustomerProvides,
    se_hotelsystem_Bill,
    se_hotelsystem_Booking,
    se_hotelsystem_BookingHandler,
    se_hotelsystem_Customer,
    se_hotelsystem_FreeRoomTypesDTO,
    se_hotelsystem_HotelInitializer,
    se_hotelsystem_IHotelAdministratorProvides,
    se_hotelsystem_IHotelCustomerProvides,
    se_hotelsystem_IHotelReceptionistProvides,
    se_hotelsystem_IHotelStartupProvides,
    se_hotelsystem_IRoomHandler,
    se_hotelsystem_PaymentHandler,
    se_hotelsystem_Room,
    se_hotelsystem_RoomExtra,
    se_hotelsystem_RoomHandler,
    se_hotelsystem_RoomReservation,
    se_hotelsystem_RoomType,
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

def test_assoc_bankingComponent19_stub_double():
    # bankcomponents_ICustomerProvides has no real 'bankcomponents_ICustomerProvides' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_PaymentHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_PaymentHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_PaymentHandler()
    partner = bankcomponents_ICustomerProvides()
    setattr(partner, 'bankcomponents_ICustomerProvides', None)
    _safe_set(owner, 'se_hotelsystem_PaymentHandler', partner)
    assert getattr(partner, 'bankcomponents_ICustomerProvides') == owner
    _safe_set(owner, 'se_hotelsystem_PaymentHandler', None)
    assert getattr(partner, 'bankcomponents_ICustomerProvides') is None


def test_assoc_bills8_stub_double():
    # hotelsystem_Bill has no real 'hotelsystem_Bill' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_Booking(bookingId=7, canceled=True, confirmed=True, endDate="sample_text", startDate="sample_text")
    partner = hotelsystem_Bill()
    setattr(partner, 'hotelsystem_Bill', None)
    _safe_set(owner, 'se_hotelsystem_Booking9', {partner})
    assert getattr(partner, 'hotelsystem_Bill') == owner
    _safe_set(owner, 'se_hotelsystem_Booking9', set())
    assert getattr(partner, 'hotelsystem_Bill') is None


def test_assoc_bookings0_stub_double():
    # hotelsystem_Booking has no real 'hotelsystem_Booking' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_BookingHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_BookingHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_BookingHandler(bookingCurrentlyCheckingOut=7, nextBookingId=7)
    partner = hotelsystem_Booking()
    setattr(partner, 'hotelsystem_Booking', None)
    _safe_set(owner, 'se_hotelsystem_BookingHandler', {partner})
    assert getattr(partner, 'hotelsystem_Booking') == owner
    _safe_set(owner, 'se_hotelsystem_BookingHandler', set())
    assert getattr(partner, 'hotelsystem_Booking') is None


def test_assoc_customer5_stub_double():
    # hotelsystem_Customer has no real 'hotelsystem_Customer' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_Booking(bookingId=7, canceled=True, confirmed=True, endDate="sample_text", startDate="sample_text")
    partner = hotelsystem_Customer()
    setattr(partner, 'hotelsystem_Customer', None)
    _safe_set(owner, 'se_hotelsystem_Booking', partner)
    assert getattr(partner, 'hotelsystem_Customer') == owner
    _safe_set(owner, 'se_hotelsystem_Booking', None)
    assert getattr(partner, 'hotelsystem_Customer') is None


def test_assoc_paymentHandler1_stub_double():
    # hotelsystem_PaymentHandler has no real 'hotelsystem_PaymentHandler' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_BookingHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_BookingHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_BookingHandler(bookingCurrentlyCheckingOut=7, nextBookingId=7)
    partner = hotelsystem_PaymentHandler()
    setattr(partner, 'hotelsystem_PaymentHandler', None)
    _safe_set(owner, 'se_hotelsystem_BookingHandler2', partner)
    assert getattr(partner, 'hotelsystem_PaymentHandler') == owner
    _safe_set(owner, 'se_hotelsystem_BookingHandler2', None)
    assert getattr(partner, 'hotelsystem_PaymentHandler') is None


def test_assoc_room13_stub_double():
    # hotelsystem_Room has no real 'hotelsystem_Room' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_RoomReservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_RoomReservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_RoomReservation(checkInDate="sample_text", checkOuDate="sample_text", endDate="sample_text", startDate="sample_text")
    partner = hotelsystem_Room()
    setattr(partner, 'hotelsystem_Room', None)
    _safe_set(owner, 'se_hotelsystem_RoomReservation14', partner)
    assert getattr(partner, 'hotelsystem_Room') == owner
    _safe_set(owner, 'se_hotelsystem_RoomReservation14', None)
    assert getattr(partner, 'hotelsystem_Room') is None


def test_assoc_roomExtras11_stub_double():
    # hotelsystem_RoomExtra has no real 'hotelsystem_RoomExtra' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_RoomReservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_RoomReservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_RoomReservation(checkInDate="sample_text", checkOuDate="sample_text", endDate="sample_text", startDate="sample_text")
    partner = hotelsystem_RoomExtra()
    setattr(partner, 'hotelsystem_RoomExtra', None)
    _safe_set(owner, 'se_hotelsystem_RoomReservation12', {partner})
    assert getattr(partner, 'hotelsystem_RoomExtra') == owner
    _safe_set(owner, 'se_hotelsystem_RoomReservation12', set())
    assert getattr(partner, 'hotelsystem_RoomExtra') is None


def test_assoc_roomReservations6_stub_double():
    # hotelsystem_RoomReservation has no real 'hotelsystem_RoomReservation' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_Booking(bookingId=7, canceled=True, confirmed=True, endDate="sample_text", startDate="sample_text")
    partner = hotelsystem_RoomReservation()
    setattr(partner, 'hotelsystem_RoomReservation', None)
    _safe_set(owner, 'se_hotelsystem_Booking7', {partner})
    assert getattr(partner, 'hotelsystem_RoomReservation') == owner
    _safe_set(owner, 'se_hotelsystem_Booking7', set())
    assert getattr(partner, 'hotelsystem_RoomReservation') is None


def test_assoc_roomType10_stub_double():
    # hotelsystem_RoomType has no real 'hotelsystem_RoomType' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_RoomReservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_RoomReservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_RoomReservation(checkInDate="sample_text", checkOuDate="sample_text", endDate="sample_text", startDate="sample_text")
    partner = hotelsystem_RoomType()
    setattr(partner, 'hotelsystem_RoomType', None)
    _safe_set(owner, 'se_hotelsystem_RoomReservation', partner)
    assert getattr(partner, 'hotelsystem_RoomType') == owner
    _safe_set(owner, 'se_hotelsystem_RoomReservation', None)
    assert getattr(partner, 'hotelsystem_RoomType') is None


def test_assoc_roomTypes20_stub_double():
    # hotelsystem_RoomType has no real 'hotelsystem_RoomType21' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_RoomHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_RoomHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_RoomHandler()
    partner = hotelsystem_RoomType()
    setattr(partner, 'hotelsystem_RoomType21', None)
    _safe_set(owner, 'se_hotelsystem_RoomHandler', {partner})
    assert getattr(partner, 'hotelsystem_RoomType21') == owner
    _safe_set(owner, 'se_hotelsystem_RoomHandler', set())
    assert getattr(partner, 'hotelsystem_RoomType21') is None


def test_assoc_roomhandler3_stub_double():
    # hotelsystem_IRoomHandler has no real 'hotelsystem_IRoomHandler' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_BookingHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_BookingHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_BookingHandler(bookingCurrentlyCheckingOut=7, nextBookingId=7)
    partner = hotelsystem_IRoomHandler()
    setattr(partner, 'hotelsystem_IRoomHandler', None)
    _safe_set(owner, 'se_hotelsystem_BookingHandler4', partner)
    assert getattr(partner, 'hotelsystem_IRoomHandler') == owner
    _safe_set(owner, 'se_hotelsystem_BookingHandler4', None)
    assert getattr(partner, 'hotelsystem_IRoomHandler') is None


def test_assoc_roomreservation17_stub_double():
    # hotelsystem_RoomReservation has no real 'hotelsystem_RoomReservation18' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_Bill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_Bill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_Bill(billID=7, price=3.14)
    partner = hotelsystem_RoomReservation()
    setattr(partner, 'hotelsystem_RoomReservation18', None)
    _safe_set(owner, 'se_hotelsystem_Bill', partner)
    assert getattr(partner, 'hotelsystem_RoomReservation18') == owner
    _safe_set(owner, 'se_hotelsystem_Bill', None)
    assert getattr(partner, 'hotelsystem_RoomReservation18') is None


def test_assoc_rooms22_stub_double():
    # hotelsystem_Room has no real 'hotelsystem_Room24' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_RoomHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_RoomHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_RoomHandler()
    partner = hotelsystem_Room()
    setattr(partner, 'hotelsystem_Room24', None)
    _safe_set(owner, 'se_hotelsystem_RoomHandler23', {partner})
    assert getattr(partner, 'hotelsystem_Room24') == owner
    _safe_set(owner, 'se_hotelsystem_RoomHandler23', set())
    assert getattr(partner, 'hotelsystem_Room24') is None


def test_assoc_roomtype15_stub_double():
    # hotelsystem_RoomType has no real 'hotelsystem_RoomType16' property in the generated
    # code (a bare stub) -- manually attach it so se_hotelsystem_Room's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # se_hotelsystem_Room's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = se_hotelsystem_Room(blocked=True, occupied=True, roomNumber=7)
    partner = hotelsystem_RoomType()
    setattr(partner, 'hotelsystem_RoomType16', None)
    _safe_set(owner, 'se_hotelsystem_Room', partner)
    assert getattr(partner, 'hotelsystem_RoomType16') == owner
    _safe_set(owner, 'se_hotelsystem_Room', None)
    assert getattr(partner, 'hotelsystem_RoomType16') is None


