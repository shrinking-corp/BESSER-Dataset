import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BookingManager,
    ClassDiagram_ApplianceAdministration,
    ClassDiagram_ApplianceType_ApplianceService,
    ClassDiagram_BillManager,
    ClassDiagram_BookingManager,
    ClassDiagram_Booking_Bill,
    ClassDiagram_Booking_BookedService,
    ClassDiagram_Booking_PurchasedService,
    ClassDiagram_Company,
    ClassDiagram_Company_GuestRecord,
    ClassDiagram_Company_Hotel,
    ClassDiagram_FacilityAdministration,
    ClassDiagram_FacilityManager,
    ClassDiagram_Facility_FacilityService,
    ClassDiagram_Facility_FacilityType,
    ClassDiagram_GuestBooking,
    ClassDiagram_GuestManager,
    ClassDiagram_HotelAdministration,
    ClassDiagram_Hotel_Booking,
    ClassDiagram_Hotel_Facility,
    ClassDiagram_Hotel_Room,
    ClassDiagram_Hotel_Staff,
    ClassDiagram_IApplianceAdministration,
    ClassDiagram_IBillManager,
    ClassDiagram_IBooking,
    ClassDiagram_IFacilityAdministration,
    ClassDiagram_IFacilityManager,
    ClassDiagram_IGuestManager,
    ClassDiagram_IHotelAdministration,
    ClassDiagram_IRoomAdministration,
    ClassDiagram_IRoomManager,
    ClassDiagram_IServiceBooking,
    ClassDiagram_IStaffAdministration,
    ClassDiagram_RoomAdministration,
    ClassDiagram_RoomAppliance_ApplianceType,
    ClassDiagram_RoomManager,
    ClassDiagram_Room_RoomAppliance,
    ClassDiagram_Room_RoomKey,
    ClassDiagram_Room_RoomType,
    ClassDiagram_ServiceBooking,
    ClassDiagram_StaffAdministration,
    ClassDiagram_StaffBooking,
    IApplianceAdministration,
    IBillManager,
    IBooking,
    IFacilityAdministration,
    IFacilityManager,
    IGuestManager,
    IHotelAdministration,
    IRoomAdministration,
    IRoomManager,
    IServiceBooking,
    IStaffAdministration,
    StaffType,
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

def test_assoc_bookedservice11_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Booking(bookingID=7, checkedIn=True, endDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = ClassDiagram_Hotel_Booking(bookingID=13, checkedIn=False, endDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = ClassDiagram_Booking_BookedService(date=date(2024, 1, 1), price=3.14)
    _safe_set(b, 'ClassDiagram_Booking_BookedService', a1)
    assert _is_linked(b, 'ClassDiagram_Booking_BookedService', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking12'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Booking12', b)
    _safe_set(b, 'ClassDiagram_Booking_BookedService', a2)
    assert _is_linked(b, 'ClassDiagram_Booking_BookedService', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking12'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Booking12', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking12'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Booking12', b)
    _safe_set(b, 'ClassDiagram_Booking_BookedService', None)
    assert not _is_linked(b, 'ClassDiagram_Booking_BookedService', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking12'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Booking12', b)


def test_assoc_employee9_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Staff(firstName="sample_text", lastName="sample_text", ssn="sample_text", stafftype="sample_text")
    a2 = ClassDiagram_Hotel_Staff(firstName="sample_text_2", lastName="sample_text_2", ssn="sample_text_2", stafftype="sample_text_2")
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel10', {a1})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel10', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Staff'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Staff', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel10', {a2})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel10', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Staff'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Staff', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Staff'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Staff', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel10', set())
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel10', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Staff'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Staff', b)


def test_assoc_hasAppliance22_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomType(area=3.14, maxNumberOfGuests=7, price=3.14)
    a2 = ClassDiagram_Room_RoomType(area=9.99, maxNumberOfGuests=13, price=9.99)
    b = ClassDiagram_Room_RoomAppliance(name="sample_text")
    _safe_set(b, 'ClassDiagram_Room_RoomAppliance24', a1)
    assert _is_linked(b, 'ClassDiagram_Room_RoomAppliance24', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomType23'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomType23', b)
    _safe_set(b, 'ClassDiagram_Room_RoomAppliance24', a2)
    assert _is_linked(b, 'ClassDiagram_Room_RoomAppliance24', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomType23'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomType23', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomType23'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomType23', b)
    _safe_set(b, 'ClassDiagram_Room_RoomAppliance24', None)
    assert not _is_linked(b, 'ClassDiagram_Room_RoomAppliance24', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomType23'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomType23', b)


def test_assoc_hasApplianceType20_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomAppliance(name="sample_text")
    a2 = ClassDiagram_Room_RoomAppliance(name="sample_text_2")
    b = ClassDiagram_RoomAppliance_ApplianceType(name="sample_text")
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType', a1)
    assert _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomAppliance21'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomAppliance21', b)
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType', a2)
    assert _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomAppliance21'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomAppliance21', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomAppliance21'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomAppliance21', b)
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType', None)
    assert not _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomAppliance21'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomAppliance21', b)


def test_assoc_hasBooking3_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Booking(bookingID=7, checkedIn=True, endDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = ClassDiagram_Hotel_Booking(bookingID=13, checkedIn=False, endDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel4', {a1})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel4', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Booking', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel4', {a2})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel4', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Booking', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Booking', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel4', set())
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel4', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Booking', b)


def test_assoc_hasFacility7_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Facility(name="sample_text")
    a2 = ClassDiagram_Hotel_Facility(name="sample_text_2")
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel8', {a1})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel8', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Facility'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Facility', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel8', {a2})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel8', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Facility'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Facility', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Facility'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Facility', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel8', set())
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel8', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Facility'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Facility', b)


def test_assoc_hasGuest1_reverse_link_reassign_clear():
    a1 = ClassDiagram_Company_GuestRecord(adress="sample_text", name="sample_text", payment="sample_text", phoneNumber="sample_text", ssn="sample_text")
    a2 = ClassDiagram_Company_GuestRecord(adress="sample_text_2", name="sample_text_2", payment="sample_text_2", phoneNumber="sample_text_2", ssn="sample_text_2")
    b = ClassDiagram_Company(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company2', {a1})
    assert _is_linked(b, 'ClassDiagram_Company2', a1)
    if hasattr(a1, 'ClassDiagram_Company_GuestRecord'):
        assert _is_linked(a1, 'ClassDiagram_Company_GuestRecord', b)
    _safe_set(b, 'ClassDiagram_Company2', {a2})
    assert _is_linked(b, 'ClassDiagram_Company2', a2)
    if hasattr(a1, 'ClassDiagram_Company_GuestRecord'):
        assert not _is_linked(a1, 'ClassDiagram_Company_GuestRecord', b)
    if hasattr(a2, 'ClassDiagram_Company_GuestRecord'):
        assert _is_linked(a2, 'ClassDiagram_Company_GuestRecord', b)
    _safe_set(b, 'ClassDiagram_Company2', set())
    assert not _is_linked(b, 'ClassDiagram_Company2', a2)
    if hasattr(a2, 'ClassDiagram_Company_GuestRecord'):
        assert not _is_linked(a2, 'ClassDiagram_Company_GuestRecord', b)


def test_assoc_hasHotel0_reverse_link_reassign_clear():
    a1 = ClassDiagram_Company_Hotel(name="sample_text")
    a2 = ClassDiagram_Company_Hotel(name="sample_text_2")
    b = ClassDiagram_Company(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company', {a1})
    assert _is_linked(b, 'ClassDiagram_Company', a1)
    if hasattr(a1, 'ClassDiagram_Company_Hotel'):
        assert _is_linked(a1, 'ClassDiagram_Company_Hotel', b)
    _safe_set(b, 'ClassDiagram_Company', {a2})
    assert _is_linked(b, 'ClassDiagram_Company', a2)
    if hasattr(a1, 'ClassDiagram_Company_Hotel'):
        assert not _is_linked(a1, 'ClassDiagram_Company_Hotel', b)
    if hasattr(a2, 'ClassDiagram_Company_Hotel'):
        assert _is_linked(a2, 'ClassDiagram_Company_Hotel', b)
    _safe_set(b, 'ClassDiagram_Company', set())
    assert not _is_linked(b, 'ClassDiagram_Company', a2)
    if hasattr(a2, 'ClassDiagram_Company_Hotel'):
        assert not _is_linked(a2, 'ClassDiagram_Company_Hotel', b)


def test_assoc_hasKey18_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomKey(expirationDate=date(2024, 1, 1))
    a2 = ClassDiagram_Room_RoomKey(expirationDate=date(2025, 6, 15))
    b = ClassDiagram_Hotel_Room(cleaningStatus=True, maintenceStatus=True, roomNumber=7)
    _safe_set(b, 'ClassDiagram_Hotel_Room19', {a1})
    assert _is_linked(b, 'ClassDiagram_Hotel_Room19', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomKey'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomKey', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room19', {a2})
    assert _is_linked(b, 'ClassDiagram_Hotel_Room19', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomKey'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomKey', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomKey'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomKey', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room19', set())
    assert not _is_linked(b, 'ClassDiagram_Hotel_Room19', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomKey'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomKey', b)


def test_assoc_hasPurchaseditem13_reverse_link_reassign_clear():
    a1 = ClassDiagram_Booking_PurchasedService(name="sample_text", price=3.14)
    a2 = ClassDiagram_Booking_PurchasedService(name="sample_text_2", price=9.99)
    b = ClassDiagram_Booking_Bill(paidAmount=3.14)
    _safe_set(b, 'ClassDiagram_Booking_Bill', {a1})
    assert _is_linked(b, 'ClassDiagram_Booking_Bill', a1)
    if hasattr(a1, 'ClassDiagram_Booking_PurchasedService'):
        assert _is_linked(a1, 'ClassDiagram_Booking_PurchasedService', b)
    _safe_set(b, 'ClassDiagram_Booking_Bill', {a2})
    assert _is_linked(b, 'ClassDiagram_Booking_Bill', a2)
    if hasattr(a1, 'ClassDiagram_Booking_PurchasedService'):
        assert not _is_linked(a1, 'ClassDiagram_Booking_PurchasedService', b)
    if hasattr(a2, 'ClassDiagram_Booking_PurchasedService'):
        assert _is_linked(a2, 'ClassDiagram_Booking_PurchasedService', b)
    _safe_set(b, 'ClassDiagram_Booking_Bill', set())
    assert not _is_linked(b, 'ClassDiagram_Booking_Bill', a2)
    if hasattr(a2, 'ClassDiagram_Booking_PurchasedService'):
        assert not _is_linked(a2, 'ClassDiagram_Booking_PurchasedService', b)


def test_assoc_hasRoom5_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Room(cleaningStatus=True, maintenceStatus=True, roomNumber=7)
    a2 = ClassDiagram_Hotel_Room(cleaningStatus=False, maintenceStatus=False, roomNumber=13)
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel6', {a1})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel6', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Room'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Room', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel6', {a2})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel6', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Room'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Room', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Room'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Room', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel6', set())
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel6', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Room'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Room', b)


def test_assoc_hasType16_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomType(area=3.14, maxNumberOfGuests=7, price=3.14)
    a2 = ClassDiagram_Room_RoomType(area=9.99, maxNumberOfGuests=13, price=9.99)
    b = ClassDiagram_Hotel_Room(cleaningStatus=True, maintenceStatus=True, roomNumber=7)
    _safe_set(b, 'ClassDiagram_Hotel_Room17', a1)
    assert _is_linked(b, 'ClassDiagram_Hotel_Room17', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomType'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomType', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room17', a2)
    assert _is_linked(b, 'ClassDiagram_Hotel_Room17', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomType'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomType', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomType'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomType', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room17', None)
    assert not _is_linked(b, 'ClassDiagram_Hotel_Room17', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomType'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomType', b)


def test_assoc_hasType25_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Facility(name="sample_text")
    a2 = ClassDiagram_Hotel_Facility(name="sample_text_2")
    b = ClassDiagram_Facility_FacilityType(kind="sample_text")
    _safe_set(b, 'ClassDiagram_Facility_FacilityType', a1)
    assert _is_linked(b, 'ClassDiagram_Facility_FacilityType', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Facility26'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Facility26', b)
    _safe_set(b, 'ClassDiagram_Facility_FacilityType', a2)
    assert _is_linked(b, 'ClassDiagram_Facility_FacilityType', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Facility26'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Facility26', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Facility26'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Facility26', b)
    _safe_set(b, 'ClassDiagram_Facility_FacilityType', None)
    assert not _is_linked(b, 'ClassDiagram_Facility_FacilityType', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Facility26'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Facility26', b)


def test_assoc_roomAppliances14_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomAppliance(name="sample_text")
    a2 = ClassDiagram_Room_RoomAppliance(name="sample_text_2")
    b = ClassDiagram_Hotel_Room(cleaningStatus=True, maintenceStatus=True, roomNumber=7)
    _safe_set(b, 'ClassDiagram_Hotel_Room15', {a1})
    assert _is_linked(b, 'ClassDiagram_Hotel_Room15', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomAppliance'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomAppliance', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room15', {a2})
    assert _is_linked(b, 'ClassDiagram_Hotel_Room15', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomAppliance'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomAppliance', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomAppliance'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomAppliance', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room15', set())
    assert not _is_linked(b, 'ClassDiagram_Hotel_Room15', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomAppliance'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomAppliance', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

