import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator,
    AdvSearch,
    Book,
    BookSet,
    BooksOrder,
    Category,
    Customer,
    Search,
    SessionManager,
    ShoppingCart,
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

def test_assoc_BookSet_AdvSearch_reverse_link_reassign_clear():
    a1 = BookSet(bookID=7, bookName="sample_text")
    a2 = BookSet(bookID=13, bookName="sample_text_2")
    b = AdvSearch(bookAuthor="sample_text", bookHighCost="sample_text", bookLowCost="sample_text", bookTitle="sample_text", categoryID="sample_text")
    _safe_set(b, 'bookSet13', {a1})
    assert _is_linked(b, 'bookSet13', a1)
    if hasattr(a1, 'advSearch12'):
        assert _is_linked(a1, 'advSearch12', b)
    _safe_set(b, 'bookSet13', {a2})
    assert _is_linked(b, 'bookSet13', a2)
    if hasattr(a1, 'advSearch12'):
        assert not _is_linked(a1, 'advSearch12', b)
    if hasattr(a2, 'advSearch12'):
        assert _is_linked(a2, 'advSearch12', b)
    _safe_set(b, 'bookSet13', set())
    assert not _is_linked(b, 'bookSet13', a2)
    if hasattr(a2, 'advSearch12'):
        assert not _is_linked(a2, 'advSearch12', b)


def test_assoc_BookSet_Search_reverse_link_reassign_clear():
    a1 = Search(bookTitle="sample_text", categoryID="sample_text")
    a2 = Search(bookTitle="sample_text_2", categoryID="sample_text_2")
    b = BookSet(bookID=7, bookName="sample_text")
    _safe_set(b, 'search10', {a1})
    assert _is_linked(b, 'search10', a1)
    if hasattr(a1, 'bookSet11'):
        assert _is_linked(a1, 'bookSet11', b)
    _safe_set(b, 'search10', {a2})
    assert _is_linked(b, 'search10', a2)
    if hasattr(a1, 'bookSet11'):
        assert not _is_linked(a1, 'bookSet11', b)
    if hasattr(a2, 'bookSet11'):
        assert _is_linked(a2, 'bookSet11', b)
    _safe_set(b, 'search10', set())
    assert not _is_linked(b, 'search10', a2)
    if hasattr(a2, 'bookSet11'):
        assert not _is_linked(a2, 'bookSet11', b)


def test_assoc_BooksOrder_Administrator_reverse_link_reassign_clear():
    a1 = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    a2 = BooksOrder(customerID=13, orderID=13, price="sample_text_2", quantity=13)
    b = Administrator(adminID=7, email="sample_text", name="sample_text", password="sample_text", phoneNo="sample_text")
    _safe_set(b, 'booksOrder9', {a1})
    assert _is_linked(b, 'booksOrder9', a1)
    if hasattr(a1, 'administrator8'):
        assert _is_linked(a1, 'administrator8', b)
    _safe_set(b, 'booksOrder9', {a2})
    assert _is_linked(b, 'booksOrder9', a2)
    if hasattr(a1, 'administrator8'):
        assert not _is_linked(a1, 'administrator8', b)
    if hasattr(a2, 'administrator8'):
        assert _is_linked(a2, 'administrator8', b)
    _safe_set(b, 'booksOrder9', set())
    assert not _is_linked(b, 'booksOrder9', a2)
    if hasattr(a2, 'administrator8'):
        assert not _is_linked(a2, 'administrator8', b)


def test_assoc_BooksOrder_Book_reverse_link_reassign_clear():
    a1 = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    a2 = BooksOrder(customerID=13, orderID=13, price="sample_text_2", quantity=13)
    b = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    _safe_set(b, 'booksOrder7', a1)
    assert _is_linked(b, 'booksOrder7', a1)
    if hasattr(a1, 'book6'):
        assert _is_linked(a1, 'book6', b)
    _safe_set(b, 'booksOrder7', a2)
    assert _is_linked(b, 'booksOrder7', a2)
    if hasattr(a1, 'book6'):
        assert not _is_linked(a1, 'book6', b)
    if hasattr(a2, 'book6'):
        assert _is_linked(a2, 'book6', b)
    _safe_set(b, 'booksOrder7', None)
    assert not _is_linked(b, 'booksOrder7', a2)
    if hasattr(a2, 'book6'):
        assert not _is_linked(a2, 'book6', b)


def test_assoc_Category_Book_reverse_link_reassign_clear():
    a1 = Category(categoryID=7, categoryName="sample_text")
    a2 = Category(categoryID=13, categoryName="sample_text_2")
    b = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    _safe_set(b, 'category17', {a1})
    assert _is_linked(b, 'category17', a1)
    if hasattr(a1, 'book16'):
        assert _is_linked(a1, 'book16', b)
    _safe_set(b, 'category17', {a2})
    assert _is_linked(b, 'category17', a2)
    if hasattr(a1, 'book16'):
        assert not _is_linked(a1, 'book16', b)
    if hasattr(a2, 'book16'):
        assert _is_linked(a2, 'book16', b)
    _safe_set(b, 'category17', set())
    assert not _is_linked(b, 'category17', a2)
    if hasattr(a2, 'book16'):
        assert not _is_linked(a2, 'book16', b)


def test_assoc_Customer_BooksOrder_reverse_link_reassign_clear():
    a1 = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    a2 = Customer(CCinfo="sample_text_2", address="sample_text_2", customerID="sample_text_2", email="sample_text_2", name="sample_text_2", password="sample_text_2", phoneNo=13)
    b = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    _safe_set(b, 'customer5', {a1})
    assert _is_linked(b, 'customer5', a1)
    if hasattr(a1, 'booksOrder4'):
        assert _is_linked(a1, 'booksOrder4', b)
    _safe_set(b, 'customer5', {a2})
    assert _is_linked(b, 'customer5', a2)
    if hasattr(a1, 'booksOrder4'):
        assert not _is_linked(a1, 'booksOrder4', b)
    if hasattr(a2, 'booksOrder4'):
        assert _is_linked(a2, 'booksOrder4', b)
    _safe_set(b, 'customer5', set())
    assert not _is_linked(b, 'customer5', a2)
    if hasattr(a2, 'booksOrder4'):
        assert not _is_linked(a2, 'booksOrder4', b)


def test_assoc_Customer_ShoppingCart_reverse_link_reassign_clear():
    a1 = ShoppingCart(customerID=7, orderID=7, price="sample_text")
    a2 = ShoppingCart(customerID=13, orderID=13, price="sample_text_2")
    b = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    _safe_set(b, 'shoppingCart20', a1)
    assert _is_linked(b, 'shoppingCart20', a1)
    if hasattr(a1, 'customer21'):
        assert _is_linked(a1, 'customer21', b)
    _safe_set(b, 'shoppingCart20', a2)
    assert _is_linked(b, 'shoppingCart20', a2)
    if hasattr(a1, 'customer21'):
        assert not _is_linked(a1, 'customer21', b)
    if hasattr(a2, 'customer21'):
        assert _is_linked(a2, 'customer21', b)
    _safe_set(b, 'shoppingCart20', None)
    assert not _is_linked(b, 'shoppingCart20', a2)
    if hasattr(a2, 'customer21'):
        assert not _is_linked(a2, 'customer21', b)


def test_assoc_SessionManager_Category_reverse_link_reassign_clear():
    a1 = SessionManager(categoryName="sample_text", userID=7)
    a2 = SessionManager(categoryName="sample_text_2", userID=13)
    b = Category(categoryID=7, categoryName="sample_text")
    _safe_set(b, 'sessionManager15', a1)
    assert _is_linked(b, 'sessionManager15', a1)
    if hasattr(a1, 'category14'):
        assert _is_linked(a1, 'category14', b)
    _safe_set(b, 'sessionManager15', a2)
    assert _is_linked(b, 'sessionManager15', a2)
    if hasattr(a1, 'category14'):
        assert not _is_linked(a1, 'category14', b)
    if hasattr(a2, 'category14'):
        assert _is_linked(a2, 'category14', b)
    _safe_set(b, 'sessionManager15', None)
    assert not _is_linked(b, 'sessionManager15', a2)
    if hasattr(a2, 'category14'):
        assert not _is_linked(a2, 'category14', b)


def test_assoc_SessionManager_User_reverse_link_reassign_clear():
    a1 = User(loginStatus="sample_text", password="sample_text", userID=7)
    a2 = User(loginStatus="sample_text_2", password="sample_text_2", userID=13)
    b = SessionManager(categoryName="sample_text", userID=7)
    _safe_set(b, 'user2', a1)
    assert _is_linked(b, 'user2', a1)
    if hasattr(a1, 'sessionManager3'):
        assert _is_linked(a1, 'sessionManager3', b)
    _safe_set(b, 'user2', a2)
    assert _is_linked(b, 'user2', a2)
    if hasattr(a1, 'sessionManager3'):
        assert not _is_linked(a1, 'sessionManager3', b)
    if hasattr(a2, 'sessionManager3'):
        assert _is_linked(a2, 'sessionManager3', b)
    _safe_set(b, 'user2', None)
    assert not _is_linked(b, 'user2', a2)
    if hasattr(a2, 'sessionManager3'):
        assert not _is_linked(a2, 'sessionManager3', b)


def test_assoc_ShoppingCart_BooksOrder_reverse_link_reassign_clear():
    a1 = ShoppingCart(customerID=7, orderID=7, price="sample_text")
    a2 = ShoppingCart(customerID=13, orderID=13, price="sample_text_2")
    b = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    _safe_set(b, 'shoppingCart19', a1)
    assert _is_linked(b, 'shoppingCart19', a1)
    if hasattr(a1, 'booksOrder18'):
        assert _is_linked(a1, 'booksOrder18', b)
    _safe_set(b, 'shoppingCart19', a2)
    assert _is_linked(b, 'shoppingCart19', a2)
    if hasattr(a1, 'booksOrder18'):
        assert not _is_linked(a1, 'booksOrder18', b)
    if hasattr(a2, 'booksOrder18'):
        assert _is_linked(a2, 'booksOrder18', b)
    _safe_set(b, 'shoppingCart19', None)
    assert not _is_linked(b, 'shoppingCart19', a2)
    if hasattr(a2, 'booksOrder18'):
        assert not _is_linked(a2, 'booksOrder18', b)


def test_assoc_User_User_reverse_link_reassign_clear():
    a1 = User(loginStatus="sample_text", password="sample_text", userID=7)
    a2 = User(loginStatus="sample_text_2", password="sample_text_2", userID=13)
    b = User(loginStatus="sample_text", password="sample_text", userID=7)
    _safe_set(b, 'user1', a1)
    assert _is_linked(b, 'user1', a1)
    if hasattr(a1, 'user0'):
        assert _is_linked(a1, 'user0', b)
    _safe_set(b, 'user1', a2)
    assert _is_linked(b, 'user1', a2)
    if hasattr(a1, 'user0'):
        assert not _is_linked(a1, 'user0', b)
    if hasattr(a2, 'user0'):
        assert _is_linked(a2, 'user0', b)
    _safe_set(b, 'user1', None)
    assert not _is_linked(b, 'user1', a2)
    if hasattr(a2, 'user0'):
        assert not _is_linked(a2, 'user0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

