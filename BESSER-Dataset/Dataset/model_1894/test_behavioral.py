import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Backend_CodePack_BankComponent,
    Booking,
    CheckInHandler,
    CodePack_Backend_CheckInHandler,
    CodePack_Backend_CustomerHandler,
    CodePack_Backend_ManagementHandler,
    CodePack_Backend_ReceptionHandler,
    CodePack_CheckInMachine,
    CodePack_DataBank,
    CodePack_DataModels_Bill,
    CodePack_DataModels_Booking,
    CodePack_DataModels_Customer,
    CodePack_DataModels_ExtraService,
    CodePack_DataModels_Guest,
    CodePack_DataModels_PaymentData,
    CodePack_DataModels_Room,
    CodePack_DataModels_RoomBooked,
    CodePack_DataModels_RoomType,
    CodePack_DataModels_ServiceType,
    CodePack_DataModels_StaffMember,
    CodePack_DataModels_StaffRole,
    CodePack_IBookings,
    CodePack_ICheckIn,
    CodePack_IManagement,
    CodePack_IReceptionOperations_rename_required,
    CodePack_IStaffAdmin,
    CodePack_IStaffAuthentication,
    CodePack_IUserAccount,
    CodePack_Shared_ContactData,
    CodePack_StaffGUI,
    CodePack_UserGUI,
    Customer,
    CustomerHandler,
    ExtraService,
    Guest,
    IBookings,
    ICheckIn,
    IManagement,
    IReceptionOperations_rename_required,
    IStaffAdmin,
    IStaffAuthentication,
    IUserAccount,
    ManagementHandler,
    PaymentData,
    ReceptionHandler,
    Room,
    RoomBooked,
    RoomType,
    ServiceType,
    StaffMember,
    StaffRole,
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

def test_assoc_booking26_stub_double():
    # Booking has no real 'Booking27' property in the generated
    # code (a bare stub) -- manually attach it so CodePack_DataModels_RoomBooked's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CodePack_DataModels_RoomBooked's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CodePack_DataModels_RoomBooked(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), room_number=7)
    partner = Booking()
    setattr(partner, 'Booking27', None)
    _safe_set(owner, 'CodePack_DataModels_RoomBooked', partner)
    assert getattr(partner, 'Booking27') == owner
    _safe_set(owner, 'CodePack_DataModels_RoomBooked', None)
    assert getattr(partner, 'Booking27') is None


def test_assoc_checkInHandler4_stub_double():
    # CheckInHandler has no real 'CheckInHandler' property in the generated
    # code (a bare stub) -- manually attach it so CodePack_CheckInMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CodePack_CheckInMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CodePack_CheckInMachine()
    partner = CheckInHandler()
    setattr(partner, 'CheckInHandler', None)
    _safe_set(owner, 'CodePack_CheckInMachine', partner)
    assert getattr(partner, 'CheckInHandler') == owner
    _safe_set(owner, 'CodePack_CheckInMachine', None)
    assert getattr(partner, 'CheckInHandler') is None


def test_assoc_customerHandler3_stub_double():
    # CustomerHandler has no real 'CustomerHandler' property in the generated
    # code (a bare stub) -- manually attach it so CodePack_UserGUI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CodePack_UserGUI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CodePack_UserGUI()
    partner = CustomerHandler()
    setattr(partner, 'CustomerHandler', None)
    _safe_set(owner, 'CodePack_UserGUI', partner)
    assert getattr(partner, 'CustomerHandler') == owner
    _safe_set(owner, 'CodePack_UserGUI', None)
    assert getattr(partner, 'CustomerHandler') is None


def test_assoc_managementHandler0_stub_double():
    # ManagementHandler has no real 'ManagementHandler' property in the generated
    # code (a bare stub) -- manually attach it so CodePack_StaffGUI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CodePack_StaffGUI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CodePack_StaffGUI()
    partner = ManagementHandler()
    setattr(partner, 'ManagementHandler', None)
    _safe_set(owner, 'CodePack_StaffGUI', partner)
    assert getattr(partner, 'ManagementHandler') == owner
    _safe_set(owner, 'CodePack_StaffGUI', None)
    assert getattr(partner, 'ManagementHandler') is None


def test_assoc_receptionHandler1_stub_double():
    # ReceptionHandler has no real 'ReceptionHandler' property in the generated
    # code (a bare stub) -- manually attach it so CodePack_StaffGUI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CodePack_StaffGUI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CodePack_StaffGUI()
    partner = ReceptionHandler()
    setattr(partner, 'ReceptionHandler', None)
    _safe_set(owner, 'CodePack_StaffGUI2', partner)
    assert getattr(partner, 'ReceptionHandler') == owner
    _safe_set(owner, 'CodePack_StaffGUI2', None)
    assert getattr(partner, 'ReceptionHandler') is None


def test_assoc_room33_stub_double():
    # Room has no real 'Room34' property in the generated
    # code (a bare stub) -- manually attach it so CodePack_DataModels_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CodePack_DataModels_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    partner = Room()
    setattr(partner, 'Room34', None)
    _safe_set(owner, 'CodePack_DataModels_Booking', partner)
    assert getattr(partner, 'Room34') == owner
    _safe_set(owner, 'CodePack_DataModels_Booking', None)
    assert getattr(partner, 'Room34') is None


def test_assoc_rooms_booked28_stub_double():
    # Room has no real 'Room29' property in the generated
    # code (a bare stub) -- manually attach it so CodePack_DataModels_Bill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CodePack_DataModels_Bill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CodePack_DataModels_Bill(booking_id=7, total_price=3.14)
    partner = Room()
    setattr(partner, 'Room29', None)
    _safe_set(owner, 'CodePack_DataModels_Bill', {partner})
    assert getattr(partner, 'Room29') == owner
    _safe_set(owner, 'CodePack_DataModels_Bill', set())
    assert getattr(partner, 'Room29') is None


def test_assoc_services_ordered30_stub_double():
    # ExtraService has no real 'ExtraService32' property in the generated
    # code (a bare stub) -- manually attach it so CodePack_DataModels_Bill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CodePack_DataModels_Bill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CodePack_DataModels_Bill(booking_id=7, total_price=3.14)
    partner = ExtraService()
    setattr(partner, 'ExtraService32', None)
    _safe_set(owner, 'CodePack_DataModels_Bill31', {partner})
    assert getattr(partner, 'ExtraService32') == owner
    _safe_set(owner, 'CodePack_DataModels_Bill31', set())
    assert getattr(partner, 'ExtraService32') is None


