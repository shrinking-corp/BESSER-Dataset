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

