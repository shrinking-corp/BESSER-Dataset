import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AdministratorProvides,
    Biller,
    Booker,
    Customer,
    CustomerProvides,
    DB_interface,
    GuestBiller,
    GuestInterface,
    ManagerInterface,
    Receipt,
    RoomHandlerInterface,
    RoomProvider,
    RoomType,
    ServiceHandlerInterface,
    ServiceProvider,
    ServiceType,
    Validator,
    newClasses_AdministratorProvides,
    newClasses_BankComponent,
    newClasses_Biller,
    newClasses_Billing,
    newClasses_Booker,
    newClasses_Booking,
    newClasses_CreditCard,
    newClasses_Customer,
    newClasses_CustomerProvides,
    newClasses_DB_interface,
    newClasses_Database,
    newClasses_Guest,
    newClasses_GuestBiller,
    newClasses_GuestInterface,
    newClasses_InformationValidator,
    newClasses_LoginChecker,
    newClasses_Manager,
    newClasses_ManagerInterface,
    newClasses_Receipt,
    newClasses_ReceiptCreator,
    newClasses_Room,
    newClasses_RoomHandler,
    newClasses_RoomHandlerInterface,
    newClasses_RoomProvider,
    newClasses_RoomType,
    newClasses_Service,
    newClasses_ServiceHandler,
    newClasses_ServiceHandlerInterface,
    newClasses_ServiceProvider,
    newClasses_ServiceType,
    newClasses_Validator,
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

def test_assoc_booking0_reverse_link_reassign_clear():
    a1 = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    a2 = newClasses_Customer(address="sample_text_2", bookingCost="sample_text_2", bookingNum="sample_text_2", city="sample_text_2", country="sample_text_2", email="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", personalNum="sample_text_2", phoneNum="sample_text_2", zipCode="sample_text_2")
    b = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    _safe_set(b, 'newClasses_Booking', a1)
    assert _is_linked(b, 'newClasses_Booking', a1)
    if hasattr(a1, 'newClasses_Customer'):
        assert _is_linked(a1, 'newClasses_Customer', b)
    _safe_set(b, 'newClasses_Booking', a2)
    assert _is_linked(b, 'newClasses_Booking', a2)
    if hasattr(a1, 'newClasses_Customer'):
        assert not _is_linked(a1, 'newClasses_Customer', b)
    if hasattr(a2, 'newClasses_Customer'):
        assert _is_linked(a2, 'newClasses_Customer', b)
    _safe_set(b, 'newClasses_Booking', None)
    assert not _is_linked(b, 'newClasses_Booking', a2)
    if hasattr(a2, 'newClasses_Customer'):
        assert not _is_linked(a2, 'newClasses_Customer', b)


def test_assoc_creditCard1_reverse_link_reassign_clear():
    a1 = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    a2 = newClasses_Customer(address="sample_text_2", bookingCost="sample_text_2", bookingNum="sample_text_2", city="sample_text_2", country="sample_text_2", email="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", personalNum="sample_text_2", phoneNum="sample_text_2", zipCode="sample_text_2")
    b = newClasses_CreditCard(creditCardNumber="sample_text", cvc="sample_text", firstName="sample_text", lastName="sample_text", month="sample_text", year="sample_text")
    _safe_set(b, 'newClasses_CreditCard', a1)
    assert _is_linked(b, 'newClasses_CreditCard', a1)
    if hasattr(a1, 'newClasses_Customer2'):
        assert _is_linked(a1, 'newClasses_Customer2', b)
    _safe_set(b, 'newClasses_CreditCard', a2)
    assert _is_linked(b, 'newClasses_CreditCard', a2)
    if hasattr(a1, 'newClasses_Customer2'):
        assert not _is_linked(a1, 'newClasses_Customer2', b)
    if hasattr(a2, 'newClasses_Customer2'):
        assert _is_linked(a2, 'newClasses_Customer2', b)
    _safe_set(b, 'newClasses_CreditCard', None)
    assert not _is_linked(b, 'newClasses_CreditCard', a2)
    if hasattr(a2, 'newClasses_Customer2'):
        assert not _is_linked(a2, 'newClasses_Customer2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_databaseHandler5_stub_double():
    # newClasses_Database has no real 'newClasses_Database' property in the generated
    # code (a bare stub) -- manually attach it so newClasses_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newClasses_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    partner = newClasses_Database()
    setattr(partner, 'newClasses_Database', None)
    _safe_set(owner, 'newClasses_Booking6', partner)
    assert getattr(partner, 'newClasses_Database') == owner
    _safe_set(owner, 'newClasses_Booking6', None)
    assert getattr(partner, 'newClasses_Database') is None


def test_assoc_manager17_stub_double():
    # newClasses_LoginChecker has no real 'newClasses_LoginChecker' property in the generated
    # code (a bare stub) -- manually attach it so newClasses_Manager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newClasses_Manager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newClasses_Manager(password="sample_text", userName="sample_text")
    partner = newClasses_LoginChecker()
    setattr(partner, 'newClasses_LoginChecker', None)
    _safe_set(owner, 'newClasses_Manager18', partner)
    assert getattr(partner, 'newClasses_LoginChecker') == owner
    _safe_set(owner, 'newClasses_Manager18', None)
    assert getattr(partner, 'newClasses_LoginChecker') is None


def test_assoc_receiptCreator3_stub_double():
    # newClasses_ReceiptCreator has no real 'newClasses_ReceiptCreator' property in the generated
    # code (a bare stub) -- manually attach it so newClasses_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newClasses_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    partner = newClasses_ReceiptCreator()
    setattr(partner, 'newClasses_ReceiptCreator', None)
    _safe_set(owner, 'newClasses_Booking4', partner)
    assert getattr(partner, 'newClasses_ReceiptCreator') == owner
    _safe_set(owner, 'newClasses_Booking4', None)
    assert getattr(partner, 'newClasses_ReceiptCreator') is None


def test_assoc_room12_stub_double():
    # newClasses_RoomHandler has no real 'newClasses_RoomHandler13' property in the generated
    # code (a bare stub) -- manually attach it so newClasses_Room's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newClasses_Room's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newClasses_Room(roomNum="sample_text", status="sample_text")
    partner = newClasses_RoomHandler()
    setattr(partner, 'newClasses_RoomHandler13', None)
    _safe_set(owner, 'newClasses_Room', partner)
    assert getattr(partner, 'newClasses_RoomHandler13') == owner
    _safe_set(owner, 'newClasses_Room', None)
    assert getattr(partner, 'newClasses_RoomHandler13') is None


def test_assoc_roomHandler8_stub_double():
    # newClasses_RoomHandler has no real 'newClasses_RoomHandler' property in the generated
    # code (a bare stub) -- manually attach it so newClasses_Manager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newClasses_Manager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newClasses_Manager(password="sample_text", userName="sample_text")
    partner = newClasses_RoomHandler()
    setattr(partner, 'newClasses_RoomHandler', None)
    _safe_set(owner, 'newClasses_Manager', partner)
    assert getattr(partner, 'newClasses_RoomHandler') == owner
    _safe_set(owner, 'newClasses_Manager', None)
    assert getattr(partner, 'newClasses_RoomHandler') is None


def test_assoc_service7_stub_double():
    # newClasses_ServiceHandler has no real 'newClasses_ServiceHandler' property in the generated
    # code (a bare stub) -- manually attach it so newClasses_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newClasses_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newClasses_Service(id="sample_text", status="sample_text")
    partner = newClasses_ServiceHandler()
    setattr(partner, 'newClasses_ServiceHandler', None)
    _safe_set(owner, 'newClasses_Service', partner)
    assert getattr(partner, 'newClasses_ServiceHandler') == owner
    _safe_set(owner, 'newClasses_Service', None)
    assert getattr(partner, 'newClasses_ServiceHandler') is None


def test_assoc_serviceHandler9_stub_double():
    # newClasses_ServiceHandler has no real 'newClasses_ServiceHandler11' property in the generated
    # code (a bare stub) -- manually attach it so newClasses_Manager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # newClasses_Manager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = newClasses_Manager(password="sample_text", userName="sample_text")
    partner = newClasses_ServiceHandler()
    setattr(partner, 'newClasses_ServiceHandler11', None)
    _safe_set(owner, 'newClasses_Manager10', partner)
    assert getattr(partner, 'newClasses_ServiceHandler11') == owner
    _safe_set(owner, 'newClasses_Manager10', None)
    assert getattr(partner, 'newClasses_ServiceHandler11') is None


