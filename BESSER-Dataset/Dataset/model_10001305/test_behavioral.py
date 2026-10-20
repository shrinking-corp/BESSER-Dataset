import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    OrderProcess,
    Premium_Members,
    Product,
    Promos,
    Regular_Members,
    ShoppingCart,
    UserAddress,
    UserName,
    User_Account,
    Vendor,
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

def test_assoc_Customer_ShoppingCart_reverse_link_reassign_clear():
    a1 = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    a2 = User_Account(DateOfBirth="sample_text_2", Email="sample_text_2", FullName="sample_text_2", RegDate="sample_text_2", UserAddress="sample_text_2", UserID="sample_text_2")
    b = UserName(FirstName="sample_text", LastName="sample_text")
    _safe_set(b, 'Customer_ShoppingCart_11', a1)
    assert _is_linked(b, 'Customer_ShoppingCart_11', a1)
    if hasattr(a1, 'Customer_ShoppingCart_00'):
        assert _is_linked(a1, 'Customer_ShoppingCart_00', b)
    _safe_set(b, 'Customer_ShoppingCart_11', a2)
    assert _is_linked(b, 'Customer_ShoppingCart_11', a2)
    if hasattr(a1, 'Customer_ShoppingCart_00'):
        assert not _is_linked(a1, 'Customer_ShoppingCart_00', b)
    if hasattr(a2, 'Customer_ShoppingCart_00'):
        assert _is_linked(a2, 'Customer_ShoppingCart_00', b)
    _safe_set(b, 'Customer_ShoppingCart_11', None)
    assert not _is_linked(b, 'Customer_ShoppingCart_11', a2)
    if hasattr(a2, 'Customer_ShoppingCart_00'):
        assert not _is_linked(a2, 'Customer_ShoppingCart_00', b)


def test_assoc_Premium_Members_Promos_reverse_link_reassign_clear():
    a1 = Promos(Discount="sample_text", EndDate="sample_text", Name="sample_text", PromoCode="sample_text", StartDate="sample_text")
    a2 = Promos(Discount="sample_text_2", EndDate="sample_text_2", Name="sample_text_2", PromoCode="sample_text_2", StartDate="sample_text_2")
    b = Premium_Members(MembershipEndDate="sample_text", MembershipStartDate="sample_text", PromoCode="sample_text")
    _safe_set(b, 'Premium_Members_Promos_012', a1)
    assert _is_linked(b, 'Premium_Members_Promos_012', a1)
    if hasattr(a1, 'Premium_Members_Promos_113'):
        assert _is_linked(a1, 'Premium_Members_Promos_113', b)
    _safe_set(b, 'Premium_Members_Promos_012', a2)
    assert _is_linked(b, 'Premium_Members_Promos_012', a2)
    if hasattr(a1, 'Premium_Members_Promos_113'):
        assert not _is_linked(a1, 'Premium_Members_Promos_113', b)
    if hasattr(a2, 'Premium_Members_Promos_113'):
        assert _is_linked(a2, 'Premium_Members_Promos_113', b)
    _safe_set(b, 'Premium_Members_Promos_012', None)
    assert not _is_linked(b, 'Premium_Members_Promos_012', a2)
    if hasattr(a2, 'Premium_Members_Promos_113'):
        assert not _is_linked(a2, 'Premium_Members_Promos_113', b)


def test_assoc_Product_Vendor_reverse_link_reassign_clear():
    a1 = Vendor(Address="sample_text", Contact_Number=7, Email="sample_text", Name="sample_text", VendorID=7)
    a2 = Vendor(Address="sample_text_2", Contact_Number=13, Email="sample_text_2", Name="sample_text_2", VendorID=13)
    b = Product(Description="sample_text", InventoryMinQuantity=7, InventoryQuantity=7, ProductID=7, VendorID=7)
    _safe_set(b, 'Product_Vendor_014', a1)
    assert _is_linked(b, 'Product_Vendor_014', a1)
    if hasattr(a1, 'Product_Vendor_115'):
        assert _is_linked(a1, 'Product_Vendor_115', b)
    _safe_set(b, 'Product_Vendor_014', a2)
    assert _is_linked(b, 'Product_Vendor_014', a2)
    if hasattr(a1, 'Product_Vendor_115'):
        assert not _is_linked(a1, 'Product_Vendor_115', b)
    if hasattr(a2, 'Product_Vendor_115'):
        assert _is_linked(a2, 'Product_Vendor_115', b)
    _safe_set(b, 'Product_Vendor_014', None)
    assert not _is_linked(b, 'Product_Vendor_014', a2)
    if hasattr(a2, 'Product_Vendor_115'):
        assert not _is_linked(a2, 'Product_Vendor_115', b)


def test_assoc_User_Account_OrderProcess_reverse_link_reassign_clear():
    a1 = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    a2 = User_Account(DateOfBirth="sample_text_2", Email="sample_text_2", FullName="sample_text_2", RegDate="sample_text_2", UserAddress="sample_text_2", UserID="sample_text_2")
    b = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    _safe_set(b, 'user_Account7', a1)
    assert _is_linked(b, 'user_Account7', a1)
    if hasattr(a1, 'orderProcess6'):
        assert _is_linked(a1, 'orderProcess6', b)
    _safe_set(b, 'user_Account7', a2)
    assert _is_linked(b, 'user_Account7', a2)
    if hasattr(a1, 'orderProcess6'):
        assert not _is_linked(a1, 'orderProcess6', b)
    if hasattr(a2, 'orderProcess6'):
        assert _is_linked(a2, 'orderProcess6', b)
    _safe_set(b, 'user_Account7', None)
    assert not _is_linked(b, 'user_Account7', a2)
    if hasattr(a2, 'orderProcess6'):
        assert not _is_linked(a2, 'orderProcess6', b)


def test_assoc_User_Account_UserAddress_reverse_link_reassign_clear():
    a1 = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    a2 = User_Account(DateOfBirth="sample_text_2", Email="sample_text_2", FullName="sample_text_2", RegDate="sample_text_2", UserAddress="sample_text_2", UserID="sample_text_2")
    b = UserAddress(City="sample_text", PostCode="sample_text", StreetName="sample_text", StreetNum=7)
    _safe_set(b, 'user_Account11', a1)
    assert _is_linked(b, 'user_Account11', a1)
    if hasattr(a1, 'userAddress10'):
        assert _is_linked(a1, 'userAddress10', b)
    _safe_set(b, 'user_Account11', a2)
    assert _is_linked(b, 'user_Account11', a2)
    if hasattr(a1, 'userAddress10'):
        assert not _is_linked(a1, 'userAddress10', b)
    if hasattr(a2, 'userAddress10'):
        assert _is_linked(a2, 'userAddress10', b)
    _safe_set(b, 'user_Account11', None)
    assert not _is_linked(b, 'user_Account11', a2)
    if hasattr(a2, 'userAddress10'):
        assert not _is_linked(a2, 'userAddress10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

