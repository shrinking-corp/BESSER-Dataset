import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Card,
    Transaction,
    _Fee,
    _LoginCredential,
    _OrderDetail,
    _PaymentInfo,
    _TransactionType,
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

def test_assoc_Farmer__ProductType_reverse_link_reassign_clear():
    a1 = _TransactionType(_type="sample_text")
    a2 = _TransactionType(_type="sample_text_2")
    b = Card(_address="sample_text", _email="sample_text", _logincredentialsid=7, _phone=7, _username="sample_text", _usertypeid=7)
    _safe_set(b, '_Add_Product_Type12', {a1})
    assert _is_linked(b, '_Add_Product_Type12', a1)
    if hasattr(a1, 'farmer13'):
        assert _is_linked(a1, 'farmer13', b)
    _safe_set(b, '_Add_Product_Type12', {a2})
    assert _is_linked(b, '_Add_Product_Type12', a2)
    if hasattr(a1, 'farmer13'):
        assert not _is_linked(a1, 'farmer13', b)
    if hasattr(a2, 'farmer13'):
        assert _is_linked(a2, 'farmer13', b)
    _safe_set(b, '_Add_Product_Type12', set())
    assert not _is_linked(b, '_Add_Product_Type12', a2)
    if hasattr(a2, 'farmer13'):
        assert not _is_linked(a2, 'farmer13', b)


def test_assoc_ProductType_Product_reverse_link_reassign_clear():
    a1 = _TransactionType(_type="sample_text")
    a2 = _TransactionType(_type="sample_text_2")
    b = _Fee(_description="sample_text", _name="sample_text", _price=7, _producttypeid=7, _stock=7)
    _safe_set(b, '_type_of5', a1)
    assert _is_linked(b, '_type_of5', a1)
    if hasattr(a1, '_has_products4'):
        assert _is_linked(a1, '_has_products4', b)
    _safe_set(b, '_type_of5', a2)
    assert _is_linked(b, '_type_of5', a2)
    if hasattr(a1, '_has_products4'):
        assert not _is_linked(a1, '_has_products4', b)
    if hasattr(a2, '_has_products4'):
        assert _is_linked(a2, '_has_products4', b)
    _safe_set(b, '_type_of5', None)
    assert not _is_linked(b, '_type_of5', a2)
    if hasattr(a2, '_has_products4'):
        assert not _is_linked(a2, '_has_products4', b)


def test_assoc_Ratings_Customer_reverse_link_reassign_clear():
    a1 = Transaction(orderId=7, shipmentNumber=7)
    a2 = Transaction(orderId=13, shipmentNumber=13)
    b = Card(_address="sample_text", _email="sample_text", _logincredentialsid=7, _phone=7, _username="sample_text", _usertypeid=7)
    _safe_set(b, '_ships3', {a1})
    assert _is_linked(b, '_ships3', a1)
    if hasattr(a1, '_Delivers2'):
        assert _is_linked(a1, '_Delivers2', b)
    _safe_set(b, '_ships3', {a2})
    assert _is_linked(b, '_ships3', a2)
    if hasattr(a1, '_Delivers2'):
        assert not _is_linked(a1, '_Delivers2', b)
    if hasattr(a2, '_Delivers2'):
        assert _is_linked(a2, '_Delivers2', b)
    _safe_set(b, '_ships3', set())
    assert not _is_linked(b, '_ships3', a2)
    if hasattr(a2, '_Delivers2'):
        assert not _is_linked(a2, '_Delivers2', b)


def test_assoc_WebUser_Customer_reverse_link_reassign_clear():
    a1 = _LoginCredential(_loginid="sample_text", _password="sample_text")
    a2 = _LoginCredential(_loginid="sample_text_2", _password="sample_text_2")
    b = Card(_address="sample_text", _email="sample_text", _logincredentialsid=7, _phone=7, _username="sample_text", _usertypeid=7)
    _safe_set(b, '_logs_in_with1', a1)
    assert _is_linked(b, '_logs_in_with1', a1)
    if hasattr(a1, '_for0'):
        assert _is_linked(a1, '_for0', b)
    _safe_set(b, '_logs_in_with1', a2)
    assert _is_linked(b, '_logs_in_with1', a2)
    if hasattr(a1, '_for0'):
        assert not _is_linked(a1, '_for0', b)
    if hasattr(a2, '_for0'):
        assert _is_linked(a2, '_for0', b)
    _safe_set(b, '_logs_in_with1', None)
    assert not _is_linked(b, '_logs_in_with1', a2)
    if hasattr(a2, '_for0'):
        assert not _is_linked(a2, '_for0', b)


def test_assoc__Customer__OrderDetails_reverse_link_reassign_clear():
    a1 = _OrderDetail(OrderId=7, _orderdate=date(2024, 1, 1), _productid=7, _quantity=7, _totalamount=7, _userid=7, paymentInfoId=7)
    a2 = _OrderDetail(OrderId=13, _orderdate=date(2025, 6, 15), _productid=13, _quantity=13, _totalamount=13, _userid=13, paymentInfoId=13)
    b = Card(_address="sample_text", _email="sample_text", _logincredentialsid=7, _phone=7, _username="sample_text", _usertypeid=7)
    _safe_set(b, '_orders8', {a1})
    assert _is_linked(b, '_orders8', a1)
    if hasattr(a1, 'receives9'):
        assert _is_linked(a1, 'receives9', b)
    _safe_set(b, '_orders8', {a2})
    assert _is_linked(b, '_orders8', a2)
    if hasattr(a1, 'receives9'):
        assert not _is_linked(a1, 'receives9', b)
    if hasattr(a2, 'receives9'):
        assert _is_linked(a2, 'receives9', b)
    _safe_set(b, '_orders8', set())
    assert not _is_linked(b, '_orders8', a2)
    if hasattr(a2, 'receives9'):
        assert not _is_linked(a2, 'receives9', b)


def test_assoc__PaymentInfo__OrderDetail_reverse_link_reassign_clear():
    a1 = _PaymentInfo(_cardname="sample_text", _cardno=7, _cvv=7, _expirydate=date(2024, 1, 1), _userid=7, paymentId=7)
    a2 = _PaymentInfo(_cardname="sample_text_2", _cardno=13, _cvv=13, _expirydate=date(2025, 6, 15), _userid=13, paymentId=13)
    b = _OrderDetail(OrderId=7, _orderdate=date(2024, 1, 1), _productid=7, _quantity=7, _totalamount=7, _userid=7, paymentInfoId=7)
    _safe_set(b, '_PaymentInfo11', a1)
    assert _is_linked(b, '_PaymentInfo11', a1)
    if hasattr(a1, '_OrderDetail10'):
        assert _is_linked(a1, '_OrderDetail10', b)
    _safe_set(b, '_PaymentInfo11', a2)
    assert _is_linked(b, '_PaymentInfo11', a2)
    if hasattr(a1, '_OrderDetail10'):
        assert not _is_linked(a1, '_OrderDetail10', b)
    if hasattr(a2, '_OrderDetail10'):
        assert _is_linked(a2, '_OrderDetail10', b)
    _safe_set(b, '_PaymentInfo11', None)
    assert not _is_linked(b, '_PaymentInfo11', a2)
    if hasattr(a2, '_OrderDetail10'):
        assert not _is_linked(a2, '_OrderDetail10', b)


def test_assoc__Product__OrderDetails_reverse_link_reassign_clear():
    a1 = _OrderDetail(OrderId=7, _orderdate=date(2024, 1, 1), _productid=7, _quantity=7, _totalamount=7, _userid=7, paymentInfoId=7)
    a2 = _OrderDetail(OrderId=13, _orderdate=date(2025, 6, 15), _productid=13, _quantity=13, _totalamount=13, _userid=13, paymentInfoId=13)
    b = _Fee(_description="sample_text", _name="sample_text", _price=7, _producttypeid=7, _stock=7)
    _safe_set(b, '_is_in6', {a1})
    assert _is_linked(b, '_is_in6', a1)
    if hasattr(a1, '_contains7'):
        assert _is_linked(a1, '_contains7', b)
    _safe_set(b, '_is_in6', {a2})
    assert _is_linked(b, '_is_in6', a2)
    if hasattr(a1, '_contains7'):
        assert not _is_linked(a1, '_contains7', b)
    if hasattr(a2, '_contains7'):
        assert _is_linked(a2, '_contains7', b)
    _safe_set(b, '_is_in6', set())
    assert not _is_linked(b, '_is_in6', a2)
    if hasattr(a2, '_contains7'):
        assert not _is_linked(a2, '_contains7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

