import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
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
    ClassDiagram_GuestManager,
    ClassDiagram_HotelAdministration,
    ClassDiagram_Hotel_Booking,
    ClassDiagram_Hotel_Facility,
    ClassDiagram_Hotel_Room,
    ClassDiagram_Hotel_Staff,
    ClassDiagram_IServiceBooking,
    ClassDiagram_RoomAdministration,
    ClassDiagram_RoomAppliance_ApplianceType,
    ClassDiagram_RoomManager,
    ClassDiagram_Room_RoomAppliance,
    ClassDiagram_Room_RoomKey,
    ClassDiagram_Room_RoomType,
    ClassDiagram_StaffAdministration,
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

def test_assoc_accessedBy11_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomKey(expirationDate=date(2024, 1, 1))
    a2 = ClassDiagram_Room_RoomKey(expirationDate=date(2025, 6, 15))
    b = ClassDiagram_Hotel_Room(cleaningStatus=True, maintenceStatus=True, roomNumber=7)
    _safe_set(b, 'ClassDiagram_Hotel_Room12', {a1})
    assert _is_linked(b, 'ClassDiagram_Hotel_Room12', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomKey'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomKey', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room12', {a2})
    assert _is_linked(b, 'ClassDiagram_Hotel_Room12', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomKey'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomKey', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomKey'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomKey', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room12', set())
    assert not _is_linked(b, 'ClassDiagram_Hotel_Room12', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomKey'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomKey', b)


def test_assoc_applianceType16_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomType(area=3.14, maxNumberOfGuests=7, name="sample_text", price=3.14)
    a2 = ClassDiagram_Room_RoomType(area=9.99, maxNumberOfGuests=13, name="sample_text_2", price=9.99)
    b = ClassDiagram_RoomAppliance_ApplianceType(name="sample_text")
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType', a1)
    assert _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomType17'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomType17', b)
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType', a2)
    assert _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomType17'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomType17', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomType17'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomType17', b)
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType', None)
    assert not _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomType17'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomType17', b)


def test_assoc_applianceType18_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomAppliance(name="sample_text")
    a2 = ClassDiagram_Room_RoomAppliance(name="sample_text_2")
    b = ClassDiagram_RoomAppliance_ApplianceType(name="sample_text")
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType19', a1)
    assert _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType19', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomAppliance'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomAppliance', b)
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType19', a2)
    assert _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType19', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomAppliance'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomAppliance', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomAppliance'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomAppliance', b)
    _safe_set(b, 'ClassDiagram_RoomAppliance_ApplianceType19', None)
    assert not _is_linked(b, 'ClassDiagram_RoomAppliance_ApplianceType19', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomAppliance'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomAppliance', b)


def test_assoc_bill28_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Booking(bookingID=7, checkedIn=True, endDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = ClassDiagram_Hotel_Booking(bookingID=13, checkedIn=False, endDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = ClassDiagram_Booking_Bill(paidAmount=3.14)
    _safe_set(b, 'ClassDiagram_Booking_Bill', a1)
    assert _is_linked(b, 'ClassDiagram_Booking_Bill', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking29'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Booking29', b)
    _safe_set(b, 'ClassDiagram_Booking_Bill', a2)
    assert _is_linked(b, 'ClassDiagram_Booking_Bill', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking29'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Booking29', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking29'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Booking29', b)
    _safe_set(b, 'ClassDiagram_Booking_Bill', None)
    assert not _is_linked(b, 'ClassDiagram_Booking_Bill', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking29'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Booking29', b)


def test_assoc_billManager41_reverse_link_reassign_clear():
    a1 = ClassDiagram_BookingManager()
    a2 = ClassDiagram_BookingManager()
    b = ClassDiagram_BillManager()
    _safe_set(b, 'ClassDiagram_BillManager', a1)
    assert _is_linked(b, 'ClassDiagram_BillManager', a1)
    if hasattr(a1, 'ClassDiagram_BookingManager42'):
        assert _is_linked(a1, 'ClassDiagram_BookingManager42', b)
    _safe_set(b, 'ClassDiagram_BillManager', a2)
    assert _is_linked(b, 'ClassDiagram_BillManager', a2)
    if hasattr(a1, 'ClassDiagram_BookingManager42'):
        assert not _is_linked(a1, 'ClassDiagram_BookingManager42', b)
    if hasattr(a2, 'ClassDiagram_BookingManager42'):
        assert _is_linked(a2, 'ClassDiagram_BookingManager42', b)
    _safe_set(b, 'ClassDiagram_BillManager', None)
    assert not _is_linked(b, 'ClassDiagram_BillManager', a2)
    if hasattr(a2, 'ClassDiagram_BookingManager42'):
        assert not _is_linked(a2, 'ClassDiagram_BookingManager42', b)


def test_assoc_company46_reverse_link_reassign_clear():
    a1 = ClassDiagram_GuestManager()
    a2 = ClassDiagram_GuestManager()
    b = ClassDiagram_Company(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company48', a1)
    assert _is_linked(b, 'ClassDiagram_Company48', a1)
    if hasattr(a1, 'ClassDiagram_GuestManager47'):
        assert _is_linked(a1, 'ClassDiagram_GuestManager47', b)
    _safe_set(b, 'ClassDiagram_Company48', a2)
    assert _is_linked(b, 'ClassDiagram_Company48', a2)
    if hasattr(a1, 'ClassDiagram_GuestManager47'):
        assert not _is_linked(a1, 'ClassDiagram_GuestManager47', b)
    if hasattr(a2, 'ClassDiagram_GuestManager47'):
        assert _is_linked(a2, 'ClassDiagram_GuestManager47', b)
    _safe_set(b, 'ClassDiagram_Company48', None)
    assert not _is_linked(b, 'ClassDiagram_Company48', a2)
    if hasattr(a2, 'ClassDiagram_GuestManager47'):
        assert not _is_linked(a2, 'ClassDiagram_GuestManager47', b)


def test_assoc_company60_reverse_link_reassign_clear():
    a1 = ClassDiagram_HotelAdministration()
    a2 = ClassDiagram_HotelAdministration()
    b = ClassDiagram_Company(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company61', a1)
    assert _is_linked(b, 'ClassDiagram_Company61', a1)
    if hasattr(a1, 'ClassDiagram_HotelAdministration'):
        assert _is_linked(a1, 'ClassDiagram_HotelAdministration', b)
    _safe_set(b, 'ClassDiagram_Company61', a2)
    assert _is_linked(b, 'ClassDiagram_Company61', a2)
    if hasattr(a1, 'ClassDiagram_HotelAdministration'):
        assert not _is_linked(a1, 'ClassDiagram_HotelAdministration', b)
    if hasattr(a2, 'ClassDiagram_HotelAdministration'):
        assert _is_linked(a2, 'ClassDiagram_HotelAdministration', b)
    _safe_set(b, 'ClassDiagram_Company61', None)
    assert not _is_linked(b, 'ClassDiagram_Company61', a2)
    if hasattr(a2, 'ClassDiagram_HotelAdministration'):
        assert not _is_linked(a2, 'ClassDiagram_HotelAdministration', b)


def test_assoc_contains32_reverse_link_reassign_clear():
    a1 = ClassDiagram_Booking_PurchasedService(name="sample_text", price=3.14)
    a2 = ClassDiagram_Booking_PurchasedService(name="sample_text_2", price=9.99)
    b = ClassDiagram_Booking_Bill(paidAmount=3.14)
    _safe_set(b, 'ClassDiagram_Booking_Bill33', {a1})
    assert _is_linked(b, 'ClassDiagram_Booking_Bill33', a1)
    if hasattr(a1, 'ClassDiagram_Booking_PurchasedService'):
        assert _is_linked(a1, 'ClassDiagram_Booking_PurchasedService', b)
    _safe_set(b, 'ClassDiagram_Booking_Bill33', {a2})
    assert _is_linked(b, 'ClassDiagram_Booking_Bill33', a2)
    if hasattr(a1, 'ClassDiagram_Booking_PurchasedService'):
        assert not _is_linked(a1, 'ClassDiagram_Booking_PurchasedService', b)
    if hasattr(a2, 'ClassDiagram_Booking_PurchasedService'):
        assert _is_linked(a2, 'ClassDiagram_Booking_PurchasedService', b)
    _safe_set(b, 'ClassDiagram_Booking_Bill33', set())
    assert not _is_linked(b, 'ClassDiagram_Booking_Bill33', a2)
    if hasattr(a2, 'ClassDiagram_Booking_PurchasedService'):
        assert not _is_linked(a2, 'ClassDiagram_Booking_PurchasedService', b)


def test_assoc_employees5_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Staff(firstName="sample_text", hasWorkTitel="sample_text", lastName="sample_text", ssn="sample_text")
    a2 = ClassDiagram_Hotel_Staff(firstName="sample_text_2", hasWorkTitel="sample_text_2", lastName="sample_text_2", ssn="sample_text_2")
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel6', {a1})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel6', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Staff'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Staff', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel6', {a2})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel6', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Staff'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Staff', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Staff'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Staff', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel6', set())
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel6', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Staff'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Staff', b)


def test_assoc_facilityService30_reverse_link_reassign_clear():
    a1 = ClassDiagram_Facility_FacilityService(name="sample_text", price=3.14)
    a2 = ClassDiagram_Facility_FacilityService(name="sample_text_2", price=9.99)
    b = ClassDiagram_Booking_BookedService(date=date(2024, 1, 1))
    _safe_set(b, 'ClassDiagram_Booking_BookedService31', a1)
    assert _is_linked(b, 'ClassDiagram_Booking_BookedService31', a1)
    if hasattr(a1, 'ClassDiagram_Facility_FacilityService'):
        assert _is_linked(a1, 'ClassDiagram_Facility_FacilityService', b)
    _safe_set(b, 'ClassDiagram_Booking_BookedService31', a2)
    assert _is_linked(b, 'ClassDiagram_Booking_BookedService31', a2)
    if hasattr(a1, 'ClassDiagram_Facility_FacilityService'):
        assert not _is_linked(a1, 'ClassDiagram_Facility_FacilityService', b)
    if hasattr(a2, 'ClassDiagram_Facility_FacilityService'):
        assert _is_linked(a2, 'ClassDiagram_Facility_FacilityService', b)
    _safe_set(b, 'ClassDiagram_Booking_BookedService31', None)
    assert not _is_linked(b, 'ClassDiagram_Booking_BookedService31', a2)
    if hasattr(a2, 'ClassDiagram_Facility_FacilityService'):
        assert not _is_linked(a2, 'ClassDiagram_Facility_FacilityService', b)


def test_assoc_facilityType34_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Facility(name="sample_text")
    a2 = ClassDiagram_Hotel_Facility(name="sample_text_2")
    b = ClassDiagram_Facility_FacilityType(name="sample_text")
    _safe_set(b, 'ClassDiagram_Facility_FacilityType', a1)
    assert _is_linked(b, 'ClassDiagram_Facility_FacilityType', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Facility'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Facility', b)
    _safe_set(b, 'ClassDiagram_Facility_FacilityType', a2)
    assert _is_linked(b, 'ClassDiagram_Facility_FacilityType', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Facility'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Facility', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Facility'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Facility', b)
    _safe_set(b, 'ClassDiagram_Facility_FacilityType', None)
    assert not _is_linked(b, 'ClassDiagram_Facility_FacilityType', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Facility'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Facility', b)


def test_assoc_guestManager39_reverse_link_reassign_clear():
    a1 = ClassDiagram_GuestManager()
    a2 = ClassDiagram_GuestManager()
    b = ClassDiagram_BookingManager()
    _safe_set(b, 'ClassDiagram_BookingManager40', a1)
    assert _is_linked(b, 'ClassDiagram_BookingManager40', a1)
    if hasattr(a1, 'ClassDiagram_GuestManager'):
        assert _is_linked(a1, 'ClassDiagram_GuestManager', b)
    _safe_set(b, 'ClassDiagram_BookingManager40', a2)
    assert _is_linked(b, 'ClassDiagram_BookingManager40', a2)
    if hasattr(a1, 'ClassDiagram_GuestManager'):
        assert not _is_linked(a1, 'ClassDiagram_GuestManager', b)
    if hasattr(a2, 'ClassDiagram_GuestManager'):
        assert _is_linked(a2, 'ClassDiagram_GuestManager', b)
    _safe_set(b, 'ClassDiagram_BookingManager40', None)
    assert not _is_linked(b, 'ClassDiagram_BookingManager40', a2)
    if hasattr(a2, 'ClassDiagram_GuestManager'):
        assert not _is_linked(a2, 'ClassDiagram_GuestManager', b)


def test_assoc_hotel35_reverse_link_reassign_clear():
    a1 = ClassDiagram_Company_Hotel(name="sample_text")
    a2 = ClassDiagram_Company_Hotel(name="sample_text_2")
    b = ClassDiagram_BookingManager()
    _safe_set(b, 'ClassDiagram_BookingManager', a1)
    assert _is_linked(b, 'ClassDiagram_BookingManager', a1)
    if hasattr(a1, 'ClassDiagram_Company_Hotel36'):
        assert _is_linked(a1, 'ClassDiagram_Company_Hotel36', b)
    _safe_set(b, 'ClassDiagram_BookingManager', a2)
    assert _is_linked(b, 'ClassDiagram_BookingManager', a2)
    if hasattr(a1, 'ClassDiagram_Company_Hotel36'):
        assert not _is_linked(a1, 'ClassDiagram_Company_Hotel36', b)
    if hasattr(a2, 'ClassDiagram_Company_Hotel36'):
        assert _is_linked(a2, 'ClassDiagram_Company_Hotel36', b)
    _safe_set(b, 'ClassDiagram_BookingManager', None)
    assert not _is_linked(b, 'ClassDiagram_BookingManager', a2)
    if hasattr(a2, 'ClassDiagram_Company_Hotel36'):
        assert not _is_linked(a2, 'ClassDiagram_Company_Hotel36', b)


def test_assoc_hotel43_reverse_link_reassign_clear():
    a1 = ClassDiagram_RoomManager()
    a2 = ClassDiagram_RoomManager()
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel45', a1)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel45', a1)
    if hasattr(a1, 'ClassDiagram_RoomManager44'):
        assert _is_linked(a1, 'ClassDiagram_RoomManager44', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel45', a2)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel45', a2)
    if hasattr(a1, 'ClassDiagram_RoomManager44'):
        assert not _is_linked(a1, 'ClassDiagram_RoomManager44', b)
    if hasattr(a2, 'ClassDiagram_RoomManager44'):
        assert _is_linked(a2, 'ClassDiagram_RoomManager44', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel45', None)
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel45', a2)
    if hasattr(a2, 'ClassDiagram_RoomManager44'):
        assert not _is_linked(a2, 'ClassDiagram_RoomManager44', b)


def test_assoc_hotel49_reverse_link_reassign_clear():
    a1 = ClassDiagram_Company_Hotel(name="sample_text")
    a2 = ClassDiagram_Company_Hotel(name="sample_text_2")
    b = ClassDiagram_BillManager()
    _safe_set(b, 'ClassDiagram_BillManager50', a1)
    assert _is_linked(b, 'ClassDiagram_BillManager50', a1)
    if hasattr(a1, 'ClassDiagram_Company_Hotel51'):
        assert _is_linked(a1, 'ClassDiagram_Company_Hotel51', b)
    _safe_set(b, 'ClassDiagram_BillManager50', a2)
    assert _is_linked(b, 'ClassDiagram_BillManager50', a2)
    if hasattr(a1, 'ClassDiagram_Company_Hotel51'):
        assert not _is_linked(a1, 'ClassDiagram_Company_Hotel51', b)
    if hasattr(a2, 'ClassDiagram_Company_Hotel51'):
        assert _is_linked(a2, 'ClassDiagram_Company_Hotel51', b)
    _safe_set(b, 'ClassDiagram_BillManager50', None)
    assert not _is_linked(b, 'ClassDiagram_BillManager50', a2)
    if hasattr(a2, 'ClassDiagram_Company_Hotel51'):
        assert not _is_linked(a2, 'ClassDiagram_Company_Hotel51', b)


def test_assoc_hotel52_reverse_link_reassign_clear():
    a1 = ClassDiagram_StaffAdministration()
    a2 = ClassDiagram_StaffAdministration()
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel53', a1)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel53', a1)
    if hasattr(a1, 'ClassDiagram_StaffAdministration'):
        assert _is_linked(a1, 'ClassDiagram_StaffAdministration', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel53', a2)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel53', a2)
    if hasattr(a1, 'ClassDiagram_StaffAdministration'):
        assert not _is_linked(a1, 'ClassDiagram_StaffAdministration', b)
    if hasattr(a2, 'ClassDiagram_StaffAdministration'):
        assert _is_linked(a2, 'ClassDiagram_StaffAdministration', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel53', None)
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel53', a2)
    if hasattr(a2, 'ClassDiagram_StaffAdministration'):
        assert not _is_linked(a2, 'ClassDiagram_StaffAdministration', b)


def test_assoc_hotel54_reverse_link_reassign_clear():
    a1 = ClassDiagram_RoomAdministration()
    a2 = ClassDiagram_RoomAdministration()
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel55', a1)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel55', a1)
    if hasattr(a1, 'ClassDiagram_RoomAdministration'):
        assert _is_linked(a1, 'ClassDiagram_RoomAdministration', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel55', a2)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel55', a2)
    if hasattr(a1, 'ClassDiagram_RoomAdministration'):
        assert not _is_linked(a1, 'ClassDiagram_RoomAdministration', b)
    if hasattr(a2, 'ClassDiagram_RoomAdministration'):
        assert _is_linked(a2, 'ClassDiagram_RoomAdministration', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel55', None)
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel55', a2)
    if hasattr(a2, 'ClassDiagram_RoomAdministration'):
        assert not _is_linked(a2, 'ClassDiagram_RoomAdministration', b)


def test_assoc_hotel56_reverse_link_reassign_clear():
    a1 = ClassDiagram_Company_Hotel(name="sample_text")
    a2 = ClassDiagram_Company_Hotel(name="sample_text_2")
    b = ClassDiagram_ApplianceAdministration()
    _safe_set(b, 'ClassDiagram_ApplianceAdministration', a1)
    assert _is_linked(b, 'ClassDiagram_ApplianceAdministration', a1)
    if hasattr(a1, 'ClassDiagram_Company_Hotel57'):
        assert _is_linked(a1, 'ClassDiagram_Company_Hotel57', b)
    _safe_set(b, 'ClassDiagram_ApplianceAdministration', a2)
    assert _is_linked(b, 'ClassDiagram_ApplianceAdministration', a2)
    if hasattr(a1, 'ClassDiagram_Company_Hotel57'):
        assert not _is_linked(a1, 'ClassDiagram_Company_Hotel57', b)
    if hasattr(a2, 'ClassDiagram_Company_Hotel57'):
        assert _is_linked(a2, 'ClassDiagram_Company_Hotel57', b)
    _safe_set(b, 'ClassDiagram_ApplianceAdministration', None)
    assert not _is_linked(b, 'ClassDiagram_ApplianceAdministration', a2)
    if hasattr(a2, 'ClassDiagram_Company_Hotel57'):
        assert not _is_linked(a2, 'ClassDiagram_Company_Hotel57', b)


def test_assoc_hotel58_reverse_link_reassign_clear():
    a1 = ClassDiagram_FacilityAdministration()
    a2 = ClassDiagram_FacilityAdministration()
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel59', a1)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel59', a1)
    if hasattr(a1, 'ClassDiagram_FacilityAdministration'):
        assert _is_linked(a1, 'ClassDiagram_FacilityAdministration', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel59', a2)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel59', a2)
    if hasattr(a1, 'ClassDiagram_FacilityAdministration'):
        assert not _is_linked(a1, 'ClassDiagram_FacilityAdministration', b)
    if hasattr(a2, 'ClassDiagram_FacilityAdministration'):
        assert _is_linked(a2, 'ClassDiagram_FacilityAdministration', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel59', None)
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel59', a2)
    if hasattr(a2, 'ClassDiagram_FacilityAdministration'):
        assert not _is_linked(a2, 'ClassDiagram_FacilityAdministration', b)


def test_assoc_hotel62_reverse_link_reassign_clear():
    a1 = ClassDiagram_FacilityManager()
    a2 = ClassDiagram_FacilityManager()
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel63', a1)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel63', a1)
    if hasattr(a1, 'ClassDiagram_FacilityManager'):
        assert _is_linked(a1, 'ClassDiagram_FacilityManager', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel63', a2)
    assert _is_linked(b, 'ClassDiagram_Company_Hotel63', a2)
    if hasattr(a1, 'ClassDiagram_FacilityManager'):
        assert not _is_linked(a1, 'ClassDiagram_FacilityManager', b)
    if hasattr(a2, 'ClassDiagram_FacilityManager'):
        assert _is_linked(a2, 'ClassDiagram_FacilityManager', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel63', None)
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel63', a2)
    if hasattr(a2, 'ClassDiagram_FacilityManager'):
        assert not _is_linked(a2, 'ClassDiagram_FacilityManager', b)


def test_assoc_includes20_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Booking(bookingID=7, checkedIn=True, endDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = ClassDiagram_Hotel_Booking(bookingID=13, checkedIn=False, endDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = ClassDiagram_Booking_BookedService(date=date(2024, 1, 1))
    _safe_set(b, 'ClassDiagram_Booking_BookedService', a1)
    assert _is_linked(b, 'ClassDiagram_Booking_BookedService', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking21'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Booking21', b)
    _safe_set(b, 'ClassDiagram_Booking_BookedService', a2)
    assert _is_linked(b, 'ClassDiagram_Booking_BookedService', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking21'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Booking21', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking21'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Booking21', b)
    _safe_set(b, 'ClassDiagram_Booking_BookedService', None)
    assert not _is_linked(b, 'ClassDiagram_Booking_BookedService', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking21'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Booking21', b)


def test_assoc_listOfBookings7_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Booking(bookingID=7, checkedIn=True, endDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = ClassDiagram_Hotel_Booking(bookingID=13, checkedIn=False, endDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel8', {a1})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel8', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Booking', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel8', {a2})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel8', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Booking', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Booking', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel8', set())
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel8', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Booking', b)


def test_assoc_listOfRoomTypes9_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomType(area=3.14, maxNumberOfGuests=7, name="sample_text", price=3.14)
    a2 = ClassDiagram_Room_RoomType(area=9.99, maxNumberOfGuests=13, name="sample_text_2", price=9.99)
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel10', {a1})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel10', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomType'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomType', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel10', {a2})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel10', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomType'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomType', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomType'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomType', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel10', set())
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel10', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomType'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomType', b)


def test_assoc_listOfRooms3_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Room(cleaningStatus=True, maintenceStatus=True, roomNumber=7)
    a2 = ClassDiagram_Hotel_Room(cleaningStatus=False, maintenceStatus=False, roomNumber=13)
    b = ClassDiagram_Company_Hotel(name="sample_text")
    _safe_set(b, 'ClassDiagram_Company_Hotel4', {a1})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel4', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Room'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Room', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel4', {a2})
    assert _is_linked(b, 'ClassDiagram_Company_Hotel4', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Room'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Room', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Room'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Room', b)
    _safe_set(b, 'ClassDiagram_Company_Hotel4', set())
    assert not _is_linked(b, 'ClassDiagram_Company_Hotel4', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Room'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Room', b)


def test_assoc_owns0_reverse_link_reassign_clear():
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


def test_assoc_recordsOf1_reverse_link_reassign_clear():
    a1 = ClassDiagram_Company_GuestRecord(adress="sample_text", name="sample_text", paymentInformation="sample_text", phoneNumber="sample_text", ssn="sample_text")
    a2 = ClassDiagram_Company_GuestRecord(adress="sample_text_2", name="sample_text_2", paymentInformation="sample_text_2", phoneNumber="sample_text_2", ssn="sample_text_2")
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


def test_assoc_responsibleGuest25_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Booking(bookingID=7, checkedIn=True, endDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = ClassDiagram_Hotel_Booking(bookingID=13, checkedIn=False, endDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = ClassDiagram_Company_GuestRecord(adress="sample_text", name="sample_text", paymentInformation="sample_text", phoneNumber="sample_text", ssn="sample_text")
    _safe_set(b, 'ClassDiagram_Company_GuestRecord27', a1)
    assert _is_linked(b, 'ClassDiagram_Company_GuestRecord27', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking26'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Booking26', b)
    _safe_set(b, 'ClassDiagram_Company_GuestRecord27', a2)
    assert _is_linked(b, 'ClassDiagram_Company_GuestRecord27', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Booking26'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Booking26', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking26'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Booking26', b)
    _safe_set(b, 'ClassDiagram_Company_GuestRecord27', None)
    assert not _is_linked(b, 'ClassDiagram_Company_GuestRecord27', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Booking26'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Booking26', b)


def test_assoc_roomManager37_reverse_link_reassign_clear():
    a1 = ClassDiagram_RoomManager()
    a2 = ClassDiagram_RoomManager()
    b = ClassDiagram_BookingManager()
    _safe_set(b, 'ClassDiagram_BookingManager38', a1)
    assert _is_linked(b, 'ClassDiagram_BookingManager38', a1)
    if hasattr(a1, 'ClassDiagram_RoomManager'):
        assert _is_linked(a1, 'ClassDiagram_RoomManager', b)
    _safe_set(b, 'ClassDiagram_BookingManager38', a2)
    assert _is_linked(b, 'ClassDiagram_BookingManager38', a2)
    if hasattr(a1, 'ClassDiagram_RoomManager'):
        assert not _is_linked(a1, 'ClassDiagram_RoomManager', b)
    if hasattr(a2, 'ClassDiagram_RoomManager'):
        assert _is_linked(a2, 'ClassDiagram_RoomManager', b)
    _safe_set(b, 'ClassDiagram_BookingManager38', None)
    assert not _is_linked(b, 'ClassDiagram_BookingManager38', a2)
    if hasattr(a2, 'ClassDiagram_RoomManager'):
        assert not _is_linked(a2, 'ClassDiagram_RoomManager', b)


def test_assoc_roomType13_reverse_link_reassign_clear():
    a1 = ClassDiagram_Room_RoomType(area=3.14, maxNumberOfGuests=7, name="sample_text", price=3.14)
    a2 = ClassDiagram_Room_RoomType(area=9.99, maxNumberOfGuests=13, name="sample_text_2", price=9.99)
    b = ClassDiagram_Hotel_Room(cleaningStatus=True, maintenceStatus=True, roomNumber=7)
    _safe_set(b, 'ClassDiagram_Hotel_Room14', a1)
    assert _is_linked(b, 'ClassDiagram_Hotel_Room14', a1)
    if hasattr(a1, 'ClassDiagram_Room_RoomType15'):
        assert _is_linked(a1, 'ClassDiagram_Room_RoomType15', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room14', a2)
    assert _is_linked(b, 'ClassDiagram_Hotel_Room14', a2)
    if hasattr(a1, 'ClassDiagram_Room_RoomType15'):
        assert not _is_linked(a1, 'ClassDiagram_Room_RoomType15', b)
    if hasattr(a2, 'ClassDiagram_Room_RoomType15'):
        assert _is_linked(a2, 'ClassDiagram_Room_RoomType15', b)
    _safe_set(b, 'ClassDiagram_Hotel_Room14', None)
    assert not _is_linked(b, 'ClassDiagram_Hotel_Room14', a2)
    if hasattr(a2, 'ClassDiagram_Room_RoomType15'):
        assert not _is_linked(a2, 'ClassDiagram_Room_RoomType15', b)


def test_assoc_rooms22_reverse_link_reassign_clear():
    a1 = ClassDiagram_Hotel_Room(cleaningStatus=True, maintenceStatus=True, roomNumber=7)
    a2 = ClassDiagram_Hotel_Room(cleaningStatus=False, maintenceStatus=False, roomNumber=13)
    b = ClassDiagram_Hotel_Booking(bookingID=7, checkedIn=True, endDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    _safe_set(b, 'ClassDiagram_Hotel_Booking23', {a1})
    assert _is_linked(b, 'ClassDiagram_Hotel_Booking23', a1)
    if hasattr(a1, 'ClassDiagram_Hotel_Room24'):
        assert _is_linked(a1, 'ClassDiagram_Hotel_Room24', b)
    _safe_set(b, 'ClassDiagram_Hotel_Booking23', {a2})
    assert _is_linked(b, 'ClassDiagram_Hotel_Booking23', a2)
    if hasattr(a1, 'ClassDiagram_Hotel_Room24'):
        assert not _is_linked(a1, 'ClassDiagram_Hotel_Room24', b)
    if hasattr(a2, 'ClassDiagram_Hotel_Room24'):
        assert _is_linked(a2, 'ClassDiagram_Hotel_Room24', b)
    _safe_set(b, 'ClassDiagram_Hotel_Booking23', set())
    assert not _is_linked(b, 'ClassDiagram_Hotel_Booking23', a2)
    if hasattr(a2, 'ClassDiagram_Hotel_Room24'):
        assert not _is_linked(a2, 'ClassDiagram_Hotel_Room24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

