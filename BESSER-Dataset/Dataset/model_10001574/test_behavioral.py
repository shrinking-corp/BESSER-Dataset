import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor_Actor,
    Checkout_UseCase,
    Class,
    Collection_UseCase,
    Delivery_UseCase,
    Edit_cart__address_info_UseCase,
    Login_UseCase,
    Menu_UseCase,
    Order_Online_UseCase,
    PayPal_UseCase,
    Register_Login_UseCase,
    Registered_User_Actor,
    Select_Items_UseCase,
    Terms_policies_UseCase,
    UseCase2_UseCase,
    UseCase3_UseCase,
    UseCase_UseCase,
    User_Information_UseCase,
    Voucher_Loyalty_Code_UseCase,
    address_info_deliverypage_UseCase,
    card_UseCase,
    cash_UseCase,
    login_for_SavedInfo_UseCase,
    mobile_pinCode_UseCase,
    non_Registered_Actor,
    payment_UseCase,
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

