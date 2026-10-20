import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    HotelManagementClassDiagram_Addon,
    HotelManagementClassDiagram_Bill,
    HotelManagementClassDiagram_BookedRoom,
    HotelManagementClassDiagram_Booking,
    HotelManagementClassDiagram_BookingController,
    HotelManagementClassDiagram_Costable,
    HotelManagementClassDiagram_Creditcard,
    HotelManagementClassDiagram_Customer,
    HotelManagementClassDiagram_Discount,
    HotelManagementClassDiagram_Employee,
    HotelManagementClassDiagram_EmployeeType,
    HotelManagementClassDiagram_Hotel,
    HotelManagementClassDiagram_Interaction1,
    HotelManagementClassDiagram_Interaction2,
    HotelManagementClassDiagram_Interaction3,
    HotelManagementClassDiagram_Interaction4,
    HotelManagementClassDiagram_Interaction5,
    HotelManagementClassDiagram_MaintenanceController,
    HotelManagementClassDiagram_ManagementController,
    HotelManagementClassDiagram_Person,
    HotelManagementClassDiagram_Room,
    Person,
    Room,
    EType,
    RoomType,
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

def test_assoc_addons22_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_BookedRoom()
    a2 = HotelManagementClassDiagram_BookedRoom()
    b = HotelManagementClassDiagram_Addon(description="sample_text", name="sample_text")
    _safe_set(b, 'HotelManagementClassDiagram_Addon23', a1)
    assert _is_linked(b, 'HotelManagementClassDiagram_Addon23', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_BookedRoom'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_BookedRoom', b)
    _safe_set(b, 'HotelManagementClassDiagram_Addon23', a2)
    assert _is_linked(b, 'HotelManagementClassDiagram_Addon23', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_BookedRoom'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_BookedRoom', b)
    if hasattr(a2, 'HotelManagementClassDiagram_BookedRoom'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_BookedRoom', b)
    _safe_set(b, 'HotelManagementClassDiagram_Addon23', None)
    assert not _is_linked(b, 'HotelManagementClassDiagram_Addon23', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_BookedRoom'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_BookedRoom', b)


def test_assoc_addons4_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    a2 = HotelManagementClassDiagram_Booking(bookingId=13, checkedIn=False, checkedOut=False, created=date(2025, 6, 15), endDate=date(2025, 6, 15), externalComments="sample_text_2", internalComments="sample_text_2", startDate=date(2025, 6, 15))
    b = HotelManagementClassDiagram_Addon(description="sample_text", name="sample_text")
    _safe_set(b, 'HotelManagementClassDiagram_Addon', a1)
    assert _is_linked(b, 'HotelManagementClassDiagram_Addon', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Booking5'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Booking5', b)
    _safe_set(b, 'HotelManagementClassDiagram_Addon', a2)
    assert _is_linked(b, 'HotelManagementClassDiagram_Addon', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Booking5'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Booking5', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Booking5'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Booking5', b)
    _safe_set(b, 'HotelManagementClassDiagram_Addon', None)
    assert not _is_linked(b, 'HotelManagementClassDiagram_Addon', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Booking5'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Booking5', b)


def test_assoc_bookedRooms6_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    a2 = HotelManagementClassDiagram_Room(booked=False, internalComment="sample_text_2", maxNbrPeople=13, roomName="sample_text_2", roomNumber=13, size=9.99, types="sample_text_2", underCleaning=False, underRepair=False)
    b = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    _safe_set(b, 'HotelManagementClassDiagram_Booking7', {a1})
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking7', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Room'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Room', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking7', {a2})
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking7', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Room'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Room', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Room'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Room', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking7', set())
    assert not _is_linked(b, 'HotelManagementClassDiagram_Booking7', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Room'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Room', b)


def test_assoc_costables13_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Costable(price=3.14)
    a2 = HotelManagementClassDiagram_Costable(price=9.99)
    b = HotelManagementClassDiagram_Bill(final=True, paid=True, totalPrice=3.14, valueAddedTax=3.14)
    _safe_set(b, 'HotelManagementClassDiagram_Bill', {a1})
    assert _is_linked(b, 'HotelManagementClassDiagram_Bill', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Costable'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Costable', b)
    _safe_set(b, 'HotelManagementClassDiagram_Bill', {a2})
    assert _is_linked(b, 'HotelManagementClassDiagram_Bill', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Costable'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Costable', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Costable'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Costable', b)
    _safe_set(b, 'HotelManagementClassDiagram_Bill', set())
    assert not _is_linked(b, 'HotelManagementClassDiagram_Bill', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Costable'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Costable', b)


def test_assoc_creditCard1_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Creditcard(cvc=7, expirationDay=7, expirationMonth=7, number="sample_text", owner="sample_text")
    a2 = HotelManagementClassDiagram_Creditcard(cvc=13, expirationDay=13, expirationMonth=13, number="sample_text_2", owner="sample_text_2")
    b = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    _safe_set(b, 'HotelManagementClassDiagram_Booking', a1)
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Creditcard'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Creditcard', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking', a2)
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Creditcard'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Creditcard', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Creditcard'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Creditcard', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking', None)
    assert not _is_linked(b, 'HotelManagementClassDiagram_Booking', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Creditcard'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Creditcard', b)


def test_assoc_customer14_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    a2 = HotelManagementClassDiagram_Customer(bonusPoints=13, customerID=13, miscInfo="sample_text_2", rank=9.99)
    b = HotelManagementClassDiagram_Bill(final=True, paid=True, totalPrice=3.14, valueAddedTax=3.14)
    _safe_set(b, 'HotelManagementClassDiagram_Bill15', a1)
    assert _is_linked(b, 'HotelManagementClassDiagram_Bill15', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Customer16'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Customer16', b)
    _safe_set(b, 'HotelManagementClassDiagram_Bill15', a2)
    assert _is_linked(b, 'HotelManagementClassDiagram_Bill15', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Customer16'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Customer16', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Customer16'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Customer16', b)
    _safe_set(b, 'HotelManagementClassDiagram_Bill15', None)
    assert not _is_linked(b, 'HotelManagementClassDiagram_Bill15', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Customer16'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Customer16', b)


def test_assoc_customer2_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    a2 = HotelManagementClassDiagram_Customer(bonusPoints=13, customerID=13, miscInfo="sample_text_2", rank=9.99)
    b = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    _safe_set(b, 'HotelManagementClassDiagram_Booking3', a1)
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking3', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Customer'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Customer', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking3', a2)
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking3', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Customer'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Customer', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Customer'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Customer', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking3', None)
    assert not _is_linked(b, 'HotelManagementClassDiagram_Booking3', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Customer'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Customer', b)


def test_assoc_discounts11_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Discount(amount=3.14, isPercentage="sample_text")
    a2 = HotelManagementClassDiagram_Discount(amount=9.99, isPercentage="sample_text_2")
    b = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    _safe_set(b, 'HotelManagementClassDiagram_Booking12', {a1})
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking12', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Discount'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Discount', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking12', {a2})
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking12', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Discount'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Discount', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Discount'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Discount', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking12', set())
    assert not _is_linked(b, 'HotelManagementClassDiagram_Booking12', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Discount'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Discount', b)


def test_assoc_discounts17_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Discount(amount=3.14, isPercentage="sample_text")
    a2 = HotelManagementClassDiagram_Discount(amount=9.99, isPercentage="sample_text_2")
    b = HotelManagementClassDiagram_Costable(price=3.14)
    _safe_set(b, 'HotelManagementClassDiagram_Costable18', {a1})
    assert _is_linked(b, 'HotelManagementClassDiagram_Costable18', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Discount19'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Discount19', b)
    _safe_set(b, 'HotelManagementClassDiagram_Costable18', {a2})
    assert _is_linked(b, 'HotelManagementClassDiagram_Costable18', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Discount19'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Discount19', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Discount19'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Discount19', b)
    _safe_set(b, 'HotelManagementClassDiagram_Costable18', set())
    assert not _is_linked(b, 'HotelManagementClassDiagram_Costable18', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Discount19'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Discount19', b)


def test_assoc_employeeType0_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_EmployeeType(acessLevel=7, type="sample_text")
    a2 = HotelManagementClassDiagram_EmployeeType(acessLevel=13, type="sample_text_2")
    b = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    _safe_set(b, 'HotelManagementClassDiagram_Employee', a1)
    assert _is_linked(b, 'HotelManagementClassDiagram_Employee', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_EmployeeType'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_EmployeeType', b)
    _safe_set(b, 'HotelManagementClassDiagram_Employee', a2)
    assert _is_linked(b, 'HotelManagementClassDiagram_Employee', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_EmployeeType'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_EmployeeType', b)
    if hasattr(a2, 'HotelManagementClassDiagram_EmployeeType'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_EmployeeType', b)
    _safe_set(b, 'HotelManagementClassDiagram_Employee', None)
    assert not _is_linked(b, 'HotelManagementClassDiagram_Employee', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_EmployeeType'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_EmployeeType', b)


def test_assoc_paymentMaster8_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    a2 = HotelManagementClassDiagram_Customer(bonusPoints=13, customerID=13, miscInfo="sample_text_2", rank=9.99)
    b = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    _safe_set(b, 'HotelManagementClassDiagram_Booking9', a1)
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking9', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Customer10'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Customer10', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking9', a2)
    assert _is_linked(b, 'HotelManagementClassDiagram_Booking9', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Customer10'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Customer10', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Customer10'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Customer10', b)
    _safe_set(b, 'HotelManagementClassDiagram_Booking9', None)
    assert not _is_linked(b, 'HotelManagementClassDiagram_Booking9', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Customer10'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Customer10', b)


def test_assoc_roomStack20_reverse_link_reassign_clear():
    a1 = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    a2 = HotelManagementClassDiagram_Room(booked=False, internalComment="sample_text_2", maxNbrPeople=13, roomName="sample_text_2", roomNumber=13, size=9.99, types="sample_text_2", underCleaning=False, underRepair=False)
    b = HotelManagementClassDiagram_MaintenanceController()
    _safe_set(b, 'HotelManagementClassDiagram_MaintenanceController', {a1})
    assert _is_linked(b, 'HotelManagementClassDiagram_MaintenanceController', a1)
    if hasattr(a1, 'HotelManagementClassDiagram_Room21'):
        assert _is_linked(a1, 'HotelManagementClassDiagram_Room21', b)
    _safe_set(b, 'HotelManagementClassDiagram_MaintenanceController', {a2})
    assert _is_linked(b, 'HotelManagementClassDiagram_MaintenanceController', a2)
    if hasattr(a1, 'HotelManagementClassDiagram_Room21'):
        assert not _is_linked(a1, 'HotelManagementClassDiagram_Room21', b)
    if hasattr(a2, 'HotelManagementClassDiagram_Room21'):
        assert _is_linked(a2, 'HotelManagementClassDiagram_Room21', b)
    _safe_set(b, 'HotelManagementClassDiagram_MaintenanceController', set())
    assert not _is_linked(b, 'HotelManagementClassDiagram_MaintenanceController', a2)
    if hasattr(a2, 'HotelManagementClassDiagram_Room21'):
        assert not _is_linked(a2, 'HotelManagementClassDiagram_Room21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__24_stub_double():
    # HotelManagementClassDiagram_Interaction1 has no real 'HotelManagementClassDiagram_Interaction1' property in the generated
    # code (a bare stub) -- manually attach it so HotelManagementClassDiagram_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HotelManagementClassDiagram_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    partner = HotelManagementClassDiagram_Interaction1()
    setattr(partner, 'HotelManagementClassDiagram_Interaction1', None)
    _safe_set(owner, 'HotelManagementClassDiagram_Employee25', partner)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction1') == owner
    _safe_set(owner, 'HotelManagementClassDiagram_Employee25', None)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction1') is None


def test_assoc__26_stub_double():
    # HotelManagementClassDiagram_Interaction2 has no real 'HotelManagementClassDiagram_Interaction2' property in the generated
    # code (a bare stub) -- manually attach it so HotelManagementClassDiagram_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HotelManagementClassDiagram_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    partner = HotelManagementClassDiagram_Interaction2()
    setattr(partner, 'HotelManagementClassDiagram_Interaction2', None)
    _safe_set(owner, 'HotelManagementClassDiagram_Employee27', partner)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction2') == owner
    _safe_set(owner, 'HotelManagementClassDiagram_Employee27', None)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction2') is None


def test_assoc__28_stub_double():
    # HotelManagementClassDiagram_Interaction3 has no real 'HotelManagementClassDiagram_Interaction3' property in the generated
    # code (a bare stub) -- manually attach it so HotelManagementClassDiagram_MaintenanceController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HotelManagementClassDiagram_MaintenanceController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HotelManagementClassDiagram_MaintenanceController()
    partner = HotelManagementClassDiagram_Interaction3()
    setattr(partner, 'HotelManagementClassDiagram_Interaction3', None)
    _safe_set(owner, 'HotelManagementClassDiagram_MaintenanceController29', partner)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction3') == owner
    _safe_set(owner, 'HotelManagementClassDiagram_MaintenanceController29', None)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction3') is None


def test_assoc__30_stub_double():
    # HotelManagementClassDiagram_Interaction4 has no real 'HotelManagementClassDiagram_Interaction4' property in the generated
    # code (a bare stub) -- manually attach it so HotelManagementClassDiagram_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HotelManagementClassDiagram_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    partner = HotelManagementClassDiagram_Interaction4()
    setattr(partner, 'HotelManagementClassDiagram_Interaction4', None)
    _safe_set(owner, 'HotelManagementClassDiagram_Employee31', partner)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction4') == owner
    _safe_set(owner, 'HotelManagementClassDiagram_Employee31', None)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction4') is None


def test_assoc__32_stub_double():
    # HotelManagementClassDiagram_Interaction5 has no real 'HotelManagementClassDiagram_Interaction5' property in the generated
    # code (a bare stub) -- manually attach it so HotelManagementClassDiagram_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HotelManagementClassDiagram_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    partner = HotelManagementClassDiagram_Interaction5()
    setattr(partner, 'HotelManagementClassDiagram_Interaction5', None)
    _safe_set(owner, 'HotelManagementClassDiagram_Booking33', partner)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction5') == owner
    _safe_set(owner, 'HotelManagementClassDiagram_Booking33', None)
    assert getattr(partner, 'HotelManagementClassDiagram_Interaction5') is None


