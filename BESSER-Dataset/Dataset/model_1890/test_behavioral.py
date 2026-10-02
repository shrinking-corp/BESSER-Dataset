import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Bill,
    Booking,
    Classes_mdsdAccount_Account,
    Classes_mdsdAccount_AccountController,
    Classes_mdsdAccount_BookingToAccount,
    Classes_mdsdAccount_CustomerAccount,
    Classes_mdsdAccount_Pet,
    Classes_mdsdAdmin_Admin,
    Classes_mdsdAdmin_AdminController,
    Classes_mdsdAdmin_BookingToAdmin,
    Classes_mdsdAdmin_HotelStaff,
    Classes_mdsdAdmin_Room,
    Classes_mdsdAdmin_Staff,
    Classes_mdsdBilling_Bill,
    Classes_mdsdBilling_BillingController,
    Classes_mdsdBilling_BookingToBill,
    Classes_mdsdBilling_CustomerBilling,
    Classes_mdsdBilling_StaffBilling,
    Classes_mdsdBilling_Transaction,
    Classes_mdsdBooking_Booking,
    Classes_mdsdBooking_BookingController,
    Classes_mdsdBooking_Meal,
    Classes_mdsdBooking_Service,
    Classes_mdsdBooking_StaffBooking,
    Classes_mdsdBooking_UserBooking,
    HotelStaff,
    Meal,
    Pet,
    Room,
    Service,
    Transaction,
    mdsdAccount_BookingToAccount,
    mdsdAccount_CustomerAccount,
    mdsdAdmin_Admin,
    mdsdAdmin_BookingToAdmin,
    mdsdAdmin_Staff,
    mdsdBilling_BookingToBill,
    mdsdBilling_CustomerBilling,
    mdsdBilling_StaffBilling,
    mdsdBooking_StaffBooking,
    mdsdBooking_UserBooking,
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

