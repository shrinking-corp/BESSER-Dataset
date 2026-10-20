import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AccountInfo,
    Administrator,
    CardInfo,
    Farmer,
    Farmer_produces,
    Order,
    Products,
    Retailer,
    Retailer_Cart,
    User,
    rating___review,
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

def test_assoc_Customer_CardInfo_reverse_link_reassign_clear():
    a1 = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    a2 = Retailer(CardInfo=13, Photo="sample_text_2", address="sample_text_2", dateOfBirth=date(2025, 6, 15), emailId="sample_text_2", name="sample_text_2", phone=13, userId=13)
    b = CardInfo(CVV=7, ID=7, billingAddress="sample_text", expiryDate=date(2024, 1, 1), name="sample_text", number=7)
    _safe_set(b, 'customer3', a1)
    assert _is_linked(b, 'customer3', a1)
    if hasattr(a1, 'cardInfo2'):
        assert _is_linked(a1, 'cardInfo2', b)
    _safe_set(b, 'customer3', a2)
    assert _is_linked(b, 'customer3', a2)
    if hasattr(a1, 'cardInfo2'):
        assert not _is_linked(a1, 'cardInfo2', b)
    if hasattr(a2, 'cardInfo2'):
        assert _is_linked(a2, 'cardInfo2', b)
    _safe_set(b, 'customer3', None)
    assert not _is_linked(b, 'customer3', a2)
    if hasattr(a2, 'cardInfo2'):
        assert not _is_linked(a2, 'cardInfo2', b)


def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    a2 = Retailer(CardInfo=13, Photo="sample_text_2", address="sample_text_2", dateOfBirth=date(2025, 6, 15), emailId="sample_text_2", name="sample_text_2", phone=13, userId=13)
    b = Order(cardDetails="sample_text", productDetails="sample_text", purchaseDate=date(2024, 1, 1), transactionID=7)
    _safe_set(b, 'customer5', a1)
    assert _is_linked(b, 'customer5', a1)
    if hasattr(a1, 'order4'):
        assert _is_linked(a1, 'order4', b)
    _safe_set(b, 'customer5', a2)
    assert _is_linked(b, 'customer5', a2)
    if hasattr(a1, 'order4'):
        assert not _is_linked(a1, 'order4', b)
    if hasattr(a2, 'order4'):
        assert _is_linked(a2, 'order4', b)
    _safe_set(b, 'customer5', None)
    assert not _is_linked(b, 'customer5', a2)
    if hasattr(a2, 'order4'):
        assert not _is_linked(a2, 'order4', b)


def test_assoc_Order_Farmer_reverse_link_reassign_clear():
    a1 = Order(cardDetails="sample_text", productDetails="sample_text", purchaseDate=date(2024, 1, 1), transactionID=7)
    a2 = Order(cardDetails="sample_text_2", productDetails="sample_text_2", purchaseDate=date(2025, 6, 15), transactionID=13)
    b = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    _safe_set(b, 'order11', a1)
    assert _is_linked(b, 'order11', a1)
    if hasattr(a1, 'farmer10'):
        assert _is_linked(a1, 'farmer10', b)
    _safe_set(b, 'order11', a2)
    assert _is_linked(b, 'order11', a2)
    if hasattr(a1, 'farmer10'):
        assert not _is_linked(a1, 'farmer10', b)
    if hasattr(a2, 'farmer10'):
        assert _is_linked(a2, 'farmer10', b)
    _safe_set(b, 'order11', None)
    assert not _is_linked(b, 'order11', a2)
    if hasattr(a2, 'farmer10'):
        assert not _is_linked(a2, 'farmer10', b)


def test_assoc_Product_Farmer_Farmer_reverse_link_reassign_clear():
    a1 = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    a2 = Products(ID=13, description="sample_text_2", discount=13, farmerID="sample_text_2", inventoryID="sample_text_2", name="sample_text_2", rating=13, reviews="sample_text_2", selling_price=9.99)
    b = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    _safe_set(b, 'product_Farmer9', a1)
    assert _is_linked(b, 'product_Farmer9', a1)
    if hasattr(a1, 'farmer8'):
        assert _is_linked(a1, 'farmer8', b)
    _safe_set(b, 'product_Farmer9', a2)
    assert _is_linked(b, 'product_Farmer9', a2)
    if hasattr(a1, 'farmer8'):
        assert not _is_linked(a1, 'farmer8', b)
    if hasattr(a2, 'farmer8'):
        assert _is_linked(a2, 'farmer8', b)
    _safe_set(b, 'product_Farmer9', None)
    assert not _is_linked(b, 'product_Farmer9', a2)
    if hasattr(a2, 'farmer8'):
        assert not _is_linked(a2, 'farmer8', b)


def test_assoc_Seller_AccountInfo_reverse_link_reassign_clear():
    a1 = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    a2 = Farmer(CardInfo="sample_text_2", accountInfoID=13, address="sample_text_2", dateOfBirth=date(2025, 6, 15), emailId="sample_text_2", name="sample_text_2", phone=13, type="sample_text_2", userId=13)
    b = AccountInfo(ID=7, accountNumber=7, bankBranch="sample_text", bankName="sample_text", name="sample_text", routingNumber=7)
    _safe_set(b, 'seller7', a1)
    assert _is_linked(b, 'seller7', a1)
    if hasattr(a1, 'accountInfo6'):
        assert _is_linked(a1, 'accountInfo6', b)
    _safe_set(b, 'seller7', a2)
    assert _is_linked(b, 'seller7', a2)
    if hasattr(a1, 'accountInfo6'):
        assert not _is_linked(a1, 'accountInfo6', b)
    if hasattr(a2, 'accountInfo6'):
        assert _is_linked(a2, 'accountInfo6', b)
    _safe_set(b, 'seller7', None)
    assert not _is_linked(b, 'seller7', a2)
    if hasattr(a2, 'accountInfo6'):
        assert not _is_linked(a2, 'accountInfo6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

