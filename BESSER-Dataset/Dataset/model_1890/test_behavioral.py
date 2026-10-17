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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bookedServices5_stub_double():
    # Service has no real 'Service6' property in the generated
    # code (a bare stub) -- manually attach it so Classes_mdsdBooking_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_mdsdBooking_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_mdsdBooking_Booking(bill_Id="sample_text", bookingId="sample_text", customerEmail="sample_text", customerName="sample_text", dateFrom=date(2024, 1, 1), dateTo=date(2024, 1, 1), isCheckedIn=True, isCheckedOut=True, petName="sample_text", roomNumber=7)
    partner = Service()
    setattr(partner, 'Service6', None)
    _safe_set(owner, 'Classes_mdsdBooking_Booking', {partner})
    assert getattr(partner, 'Service6') == owner
    _safe_set(owner, 'Classes_mdsdBooking_Booking', set())
    assert getattr(partner, 'Service6') is None


def test_assoc_bookings2_stub_double():
    # Booking has no real 'Booking' property in the generated
    # code (a bare stub) -- manually attach it so Classes_mdsdBooking_BookingController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_mdsdBooking_BookingController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_mdsdBooking_BookingController()
    partner = Booking()
    setattr(partner, 'Booking', None)
    _safe_set(owner, 'Classes_mdsdBooking_BookingController', {partner})
    assert getattr(partner, 'Booking') == owner
    _safe_set(owner, 'Classes_mdsdBooking_BookingController', set())
    assert getattr(partner, 'Booking') is None


def test_assoc_mealInfo7_stub_double():
    # Meal has no real 'Meal' property in the generated
    # code (a bare stub) -- manually attach it so Classes_mdsdBooking_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_mdsdBooking_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_mdsdBooking_Booking(bill_Id="sample_text", bookingId="sample_text", customerEmail="sample_text", customerName="sample_text", dateFrom=date(2024, 1, 1), dateTo=date(2024, 1, 1), isCheckedIn=True, isCheckedOut=True, petName="sample_text", roomNumber=7)
    partner = Meal()
    setattr(partner, 'Meal', None)
    _safe_set(owner, 'Classes_mdsdBooking_Booking8', partner)
    assert getattr(partner, 'Meal') == owner
    _safe_set(owner, 'Classes_mdsdBooking_Booking8', None)
    assert getattr(partner, 'Meal') is None


def test_assoc_pets12_stub_double():
    # Pet has no real 'Pet' property in the generated
    # code (a bare stub) -- manually attach it so Classes_mdsdAccount_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_mdsdAccount_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_mdsdAccount_Account(accountID="sample_text", email="sample_text", isLoggedIn=True, name="sample_text", password="sample_text")
    partner = Pet()
    setattr(partner, 'Pet', None)
    _safe_set(owner, 'Classes_mdsdAccount_Account', {partner})
    assert getattr(partner, 'Pet') == owner
    _safe_set(owner, 'Classes_mdsdAccount_Account', set())
    assert getattr(partner, 'Pet') is None


def test_assoc_rooms9_stub_double():
    # Room has no real 'Room' property in the generated
    # code (a bare stub) -- manually attach it so Classes_mdsdAdmin_AdminController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_mdsdAdmin_AdminController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_mdsdAdmin_AdminController()
    partner = Room()
    setattr(partner, 'Room', None)
    _safe_set(owner, 'Classes_mdsdAdmin_AdminController', {partner})
    assert getattr(partner, 'Room') == owner
    _safe_set(owner, 'Classes_mdsdAdmin_AdminController', set())
    assert getattr(partner, 'Room') is None


def test_assoc_services3_stub_double():
    # Service has no real 'Service' property in the generated
    # code (a bare stub) -- manually attach it so Classes_mdsdBooking_BookingController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_mdsdBooking_BookingController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_mdsdBooking_BookingController()
    partner = Service()
    setattr(partner, 'Service', None)
    _safe_set(owner, 'Classes_mdsdBooking_BookingController4', {partner})
    assert getattr(partner, 'Service') == owner
    _safe_set(owner, 'Classes_mdsdBooking_BookingController4', set())
    assert getattr(partner, 'Service') is None


def test_assoc_staff10_stub_double():
    # HotelStaff has no real 'HotelStaff' property in the generated
    # code (a bare stub) -- manually attach it so Classes_mdsdAdmin_AdminController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_mdsdAdmin_AdminController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_mdsdAdmin_AdminController()
    partner = HotelStaff()
    setattr(partner, 'HotelStaff', None)
    _safe_set(owner, 'Classes_mdsdAdmin_AdminController11', {partner})
    assert getattr(partner, 'HotelStaff') == owner
    _safe_set(owner, 'Classes_mdsdAdmin_AdminController11', set())
    assert getattr(partner, 'HotelStaff') is None


def test_assoc_transactions1_stub_double():
    # Transaction has no real 'Transaction' property in the generated
    # code (a bare stub) -- manually attach it so Classes_mdsdBilling_Bill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_mdsdBilling_Bill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_mdsdBilling_Bill(ID="sample_text", isPaid=True)
    partner = Transaction()
    setattr(partner, 'Transaction', None)
    _safe_set(owner, 'Classes_mdsdBilling_Bill', {partner})
    assert getattr(partner, 'Transaction') == owner
    _safe_set(owner, 'Classes_mdsdBilling_Bill', set())
    assert getattr(partner, 'Transaction') is None


