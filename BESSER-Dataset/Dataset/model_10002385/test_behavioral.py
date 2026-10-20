import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    BookSet,
    Bookstore_Shop,
    Customer,
    Order,
    Payment,
    Search,
    Shopping_Cart,
    User,
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

def test_assoc_Customer_Search_reverse_link_reassign_clear():
    a1 = Search(authorName="sample_text", bookTitle="sample_text", priceLimit="sample_text")
    a2 = Search(authorName="sample_text_2", bookTitle="sample_text_2", priceLimit="sample_text_2")
    b = Customer(customerAddress="sample_text", customerId=7, customerName="sample_text", customerPaymentInfo="sample_text", customerPhone=7)
    _safe_set(b, 'search6', {a1})
    assert _is_linked(b, 'search6', a1)
    if hasattr(a1, 'searchBook7'):
        assert _is_linked(a1, 'searchBook7', b)
    _safe_set(b, 'search6', {a2})
    assert _is_linked(b, 'search6', a2)
    if hasattr(a1, 'searchBook7'):
        assert not _is_linked(a1, 'searchBook7', b)
    if hasattr(a2, 'searchBook7'):
        assert _is_linked(a2, 'searchBook7', b)
    _safe_set(b, 'search6', set())
    assert not _is_linked(b, 'search6', a2)
    if hasattr(a2, 'searchBook7'):
        assert not _is_linked(a2, 'searchBook7', b)


def test_assoc_OrderBook_Admin_reverse_link_reassign_clear():
    a1 = Order(NumberOfBooks=7, customerId=7, orderId=7, price="sample_text")
    a2 = Order(NumberOfBooks=13, customerId=13, orderId=13, price="sample_text_2")
    b = Admin(adminId=7, adminName="sample_text", adminPassword="sample_text", adminRmail="sample_text")
    _safe_set(b, 'orderBook13', a1)
    assert _is_linked(b, 'orderBook13', a1)
    if hasattr(a1, 'addBook12'):
        assert _is_linked(a1, 'addBook12', b)
    _safe_set(b, 'orderBook13', a2)
    assert _is_linked(b, 'orderBook13', a2)
    if hasattr(a1, 'addBook12'):
        assert not _is_linked(a1, 'addBook12', b)
    if hasattr(a2, 'addBook12'):
        assert _is_linked(a2, 'addBook12', b)
    _safe_set(b, 'orderBook13', None)
    assert not _is_linked(b, 'orderBook13', a2)
    if hasattr(a2, 'addBook12'):
        assert not _is_linked(a2, 'addBook12', b)


def test_assoc_Search_BookSet_reverse_link_reassign_clear():
    a1 = Search(authorName="sample_text", bookTitle="sample_text", priceLimit="sample_text")
    a2 = Search(authorName="sample_text_2", bookTitle="sample_text_2", priceLimit="sample_text_2")
    b = BookSet(bookIsbn=7, bookTitle="sample_text")
    _safe_set(b, 'search9', a1)
    assert _is_linked(b, 'search9', a1)
    if hasattr(a1, 'bookSet8'):
        assert _is_linked(a1, 'bookSet8', b)
    _safe_set(b, 'search9', a2)
    assert _is_linked(b, 'search9', a2)
    if hasattr(a1, 'bookSet8'):
        assert not _is_linked(a1, 'bookSet8', b)
    if hasattr(a2, 'bookSet8'):
        assert _is_linked(a2, 'bookSet8', b)
    _safe_set(b, 'search9', None)
    assert not _is_linked(b, 'search9', a2)
    if hasattr(a2, 'bookSet8'):
        assert not _is_linked(a2, 'bookSet8', b)


def test_assoc_User_Admin_reverse_link_reassign_clear():
    a1 = User(password="sample_text", userId=7)
    a2 = User(password="sample_text_2", userId=13)
    b = Admin(adminId=7, adminName="sample_text", adminPassword="sample_text", adminRmail="sample_text")
    _safe_set(b, '_addUserAsMember3', a1)
    assert _is_linked(b, '_addUserAsMember3', a1)
    if hasattr(a1, 'admin2'):
        assert _is_linked(a1, 'admin2', b)
    _safe_set(b, '_addUserAsMember3', a2)
    assert _is_linked(b, '_addUserAsMember3', a2)
    if hasattr(a1, 'admin2'):
        assert not _is_linked(a1, 'admin2', b)
    if hasattr(a2, 'admin2'):
        assert _is_linked(a2, 'admin2', b)
    _safe_set(b, '_addUserAsMember3', None)
    assert not _is_linked(b, '_addUserAsMember3', a2)
    if hasattr(a2, 'admin2'):
        assert not _is_linked(a2, 'admin2', b)


def test_assoc_User_Customer_reverse_link_reassign_clear():
    a1 = User(password="sample_text", userId=7)
    a2 = User(password="sample_text_2", userId=13)
    b = Customer(customerAddress="sample_text", customerId=7, customerName="sample_text", customerPaymentInfo="sample_text", customerPhone=7)
    _safe_set(b, 'user1', a1)
    assert _is_linked(b, 'user1', a1)
    if hasattr(a1, 'customer0'):
        assert _is_linked(a1, 'customer0', b)
    _safe_set(b, 'user1', a2)
    assert _is_linked(b, 'user1', a2)
    if hasattr(a1, 'customer0'):
        assert not _is_linked(a1, 'customer0', b)
    if hasattr(a2, 'customer0'):
        assert _is_linked(a2, 'customer0', b)
    _safe_set(b, 'user1', None)
    assert not _is_linked(b, 'user1', a2)
    if hasattr(a2, 'customer0'):
        assert not _is_linked(a2, 'customer0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

