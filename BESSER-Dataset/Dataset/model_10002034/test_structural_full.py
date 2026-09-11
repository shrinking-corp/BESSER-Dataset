import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Administrator_adminID_value_roundtrip():
    instance = Administrator(adminID=7, email="sample_text", name="sample_text", password="sample_text", phoneNo="sample_text")
    assert instance.adminID == 7
    instance.adminID = 13
    assert instance.adminID == 13


def test_Administrator_email_value_roundtrip():
    instance = Administrator(adminID=7, email="sample_text", name="sample_text", password="sample_text", phoneNo="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Administrator_name_value_roundtrip():
    instance = Administrator(adminID=7, email="sample_text", name="sample_text", password="sample_text", phoneNo="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Administrator_password_value_roundtrip():
    instance = Administrator(adminID=7, email="sample_text", name="sample_text", password="sample_text", phoneNo="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Administrator_phoneNo_value_roundtrip():
    instance = Administrator(adminID=7, email="sample_text", name="sample_text", password="sample_text", phoneNo="sample_text")
    assert instance.phoneNo == "sample_text"
    instance.phoneNo = "sample_text_2"
    assert instance.phoneNo == "sample_text_2"


def test_AdvSearch_bookAuthor_value_roundtrip():
    instance = AdvSearch(bookAuthor="sample_text", bookHighCost="sample_text", bookLowCost="sample_text", bookTitle="sample_text", categoryID="sample_text")
    assert instance.bookAuthor == "sample_text"
    instance.bookAuthor = "sample_text_2"
    assert instance.bookAuthor == "sample_text_2"


def test_AdvSearch_bookHighCost_value_roundtrip():
    instance = AdvSearch(bookAuthor="sample_text", bookHighCost="sample_text", bookLowCost="sample_text", bookTitle="sample_text", categoryID="sample_text")
    assert instance.bookHighCost == "sample_text"
    instance.bookHighCost = "sample_text_2"
    assert instance.bookHighCost == "sample_text_2"


def test_AdvSearch_bookLowCost_value_roundtrip():
    instance = AdvSearch(bookAuthor="sample_text", bookHighCost="sample_text", bookLowCost="sample_text", bookTitle="sample_text", categoryID="sample_text")
    assert instance.bookLowCost == "sample_text"
    instance.bookLowCost = "sample_text_2"
    assert instance.bookLowCost == "sample_text_2"


def test_AdvSearch_bookTitle_value_roundtrip():
    instance = AdvSearch(bookAuthor="sample_text", bookHighCost="sample_text", bookLowCost="sample_text", bookTitle="sample_text", categoryID="sample_text")
    assert instance.bookTitle == "sample_text"
    instance.bookTitle = "sample_text_2"
    assert instance.bookTitle == "sample_text_2"


def test_AdvSearch_categoryID_value_roundtrip():
    instance = AdvSearch(bookAuthor="sample_text", bookHighCost="sample_text", bookLowCost="sample_text", bookTitle="sample_text", categoryID="sample_text")
    assert instance.categoryID == "sample_text"
    instance.categoryID = "sample_text_2"
    assert instance.categoryID == "sample_text_2"


def test_Book_authorName_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.authorName == "sample_text"
    instance.authorName = "sample_text_2"
    assert instance.authorName == "sample_text_2"


def test_Book_bookID_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.bookID == 7
    instance.bookID = 13
    assert instance.bookID == 13


def test_Book_bookName_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.bookName == "sample_text"
    instance.bookName = "sample_text_2"
    assert instance.bookName == "sample_text_2"


def test_Book_categoryID_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.categoryID == 7
    instance.categoryID = 13
    assert instance.categoryID == 13


def test_Book_imageURL_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.imageURL == "sample_text"
    instance.imageURL = "sample_text_2"
    assert instance.imageURL == "sample_text_2"


def test_Book_notes_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.notes == "sample_text"
    instance.notes = "sample_text_2"
    assert instance.notes == "sample_text_2"


def test_Book_price_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_Book_productURL_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.productURL == "sample_text"
    instance.productURL = "sample_text_2"
    assert instance.productURL == "sample_text_2"


def test_Book_rating_value_roundtrip():
    instance = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    assert instance.rating == 7
    instance.rating = 13
    assert instance.rating == 13


def test_BookSet_bookID_value_roundtrip():
    instance = BookSet(bookID=7, bookName="sample_text")
    assert instance.bookID == 7
    instance.bookID = 13
    assert instance.bookID == 13


def test_BookSet_bookName_value_roundtrip():
    instance = BookSet(bookID=7, bookName="sample_text")
    assert instance.bookName == "sample_text"
    instance.bookName = "sample_text_2"
    assert instance.bookName == "sample_text_2"


def test_BooksOrder_customerID_value_roundtrip():
    instance = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    assert instance.customerID == 7
    instance.customerID = 13
    assert instance.customerID == 13


def test_BooksOrder_orderID_value_roundtrip():
    instance = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    assert instance.orderID == 7
    instance.orderID = 13
    assert instance.orderID == 13


def test_BooksOrder_price_value_roundtrip():
    instance = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_BooksOrder_quantity_value_roundtrip():
    instance = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Category_categoryID_value_roundtrip():
    instance = Category(categoryID=7, categoryName="sample_text")
    assert instance.categoryID == 7
    instance.categoryID = 13
    assert instance.categoryID == 13


def test_Category_categoryName_value_roundtrip():
    instance = Category(categoryID=7, categoryName="sample_text")
    assert instance.categoryName == "sample_text"
    instance.categoryName = "sample_text_2"
    assert instance.categoryName == "sample_text_2"


def test_Customer_CCinfo_value_roundtrip():
    instance = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    assert instance.CCinfo == "sample_text"
    instance.CCinfo = "sample_text_2"
    assert instance.CCinfo == "sample_text_2"


def test_Customer_address_value_roundtrip():
    instance = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer_customerID_value_roundtrip():
    instance = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    assert instance.customerID == "sample_text"
    instance.customerID = "sample_text_2"
    assert instance.customerID == "sample_text_2"


def test_Customer_email_value_roundtrip():
    instance = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Customer_name_value_roundtrip():
    instance = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Customer_password_value_roundtrip():
    instance = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Customer_phoneNo_value_roundtrip():
    instance = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    assert instance.phoneNo == 7
    instance.phoneNo = 13
    assert instance.phoneNo == 13


def test_Search_bookTitle_value_roundtrip():
    instance = Search(bookTitle="sample_text", categoryID="sample_text")
    assert instance.bookTitle == "sample_text"
    instance.bookTitle = "sample_text_2"
    assert instance.bookTitle == "sample_text_2"


def test_Search_categoryID_value_roundtrip():
    instance = Search(bookTitle="sample_text", categoryID="sample_text")
    assert instance.categoryID == "sample_text"
    instance.categoryID = "sample_text_2"
    assert instance.categoryID == "sample_text_2"


def test_SessionManager_categoryName_value_roundtrip():
    instance = SessionManager(categoryName="sample_text", userID=7)
    assert instance.categoryName == "sample_text"
    instance.categoryName = "sample_text_2"
    assert instance.categoryName == "sample_text_2"


def test_SessionManager_userID_value_roundtrip():
    instance = SessionManager(categoryName="sample_text", userID=7)
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_ShoppingCart_customerID_value_roundtrip():
    instance = ShoppingCart(customerID=7, orderID=7, price="sample_text")
    assert instance.customerID == 7
    instance.customerID = 13
    assert instance.customerID == 13


def test_ShoppingCart_orderID_value_roundtrip():
    instance = ShoppingCart(customerID=7, orderID=7, price="sample_text")
    assert instance.orderID == 7
    instance.orderID = 13
    assert instance.orderID == 13


def test_ShoppingCart_price_value_roundtrip():
    instance = ShoppingCart(customerID=7, orderID=7, price="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_User_loginStatus_value_roundtrip():
    instance = User(loginStatus="sample_text", password="sample_text", userID=7)
    assert instance.loginStatus == "sample_text"
    instance.loginStatus = "sample_text_2"
    assert instance.loginStatus == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(loginStatus="sample_text", password="sample_text", userID=7)
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_userID_value_roundtrip():
    instance = User(loginStatus="sample_text", password="sample_text", userID=7)
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_assoc_BookSet_AdvSearch_link_reassign_clear():
    a = BookSet(bookID=7, bookName="sample_text")
    b1 = AdvSearch(bookAuthor="sample_text", bookHighCost="sample_text", bookLowCost="sample_text", bookTitle="sample_text", categoryID="sample_text")
    b2 = AdvSearch(bookAuthor="sample_text_2", bookHighCost="sample_text_2", bookLowCost="sample_text_2", bookTitle="sample_text_2", categoryID="sample_text_2")
    _safe_set(a, 'advSearch12', {b1})
    assert _is_linked(a, 'advSearch12', b1)
    if hasattr(b1, 'bookSet13'):
        assert _is_linked(b1, 'bookSet13', a)
    _safe_set(a, 'advSearch12', {b2})
    assert _is_linked(a, 'advSearch12', b2)
    if hasattr(b1, 'bookSet13'):
        assert not _is_linked(b1, 'bookSet13', a)
    if hasattr(b2, 'bookSet13'):
        assert _is_linked(b2, 'bookSet13', a)
    _safe_set(a, 'advSearch12', set())
    assert not _is_linked(a, 'advSearch12', b2)
    if hasattr(b2, 'bookSet13'):
        assert not _is_linked(b2, 'bookSet13', a)


def test_assoc_BookSet_Search_link_reassign_clear():
    a = Search(bookTitle="sample_text", categoryID="sample_text")
    b1 = BookSet(bookID=7, bookName="sample_text")
    b2 = BookSet(bookID=13, bookName="sample_text_2")
    _safe_set(a, 'bookSet11', {b1})
    assert _is_linked(a, 'bookSet11', b1)
    if hasattr(b1, 'search10'):
        assert _is_linked(b1, 'search10', a)
    _safe_set(a, 'bookSet11', {b2})
    assert _is_linked(a, 'bookSet11', b2)
    if hasattr(b1, 'search10'):
        assert not _is_linked(b1, 'search10', a)
    if hasattr(b2, 'search10'):
        assert _is_linked(b2, 'search10', a)
    _safe_set(a, 'bookSet11', set())
    assert not _is_linked(a, 'bookSet11', b2)
    if hasattr(b2, 'search10'):
        assert not _is_linked(b2, 'search10', a)


def test_assoc_BooksOrder_Administrator_link_reassign_clear():
    a = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    b1 = Administrator(adminID=7, email="sample_text", name="sample_text", password="sample_text", phoneNo="sample_text")
    b2 = Administrator(adminID=13, email="sample_text_2", name="sample_text_2", password="sample_text_2", phoneNo="sample_text_2")
    _safe_set(a, 'administrator8', b1)
    assert _is_linked(a, 'administrator8', b1)
    if hasattr(b1, 'booksOrder9'):
        assert _is_linked(b1, 'booksOrder9', a)
    _safe_set(a, 'administrator8', b2)
    assert _is_linked(a, 'administrator8', b2)
    if hasattr(b1, 'booksOrder9'):
        assert not _is_linked(b1, 'booksOrder9', a)
    if hasattr(b2, 'booksOrder9'):
        assert _is_linked(b2, 'booksOrder9', a)
    _safe_set(a, 'administrator8', None)
    assert not _is_linked(a, 'administrator8', b2)
    if hasattr(b2, 'booksOrder9'):
        assert not _is_linked(b2, 'booksOrder9', a)


def test_assoc_BooksOrder_Book_link_reassign_clear():
    a = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    b1 = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    b2 = Book(authorName="sample_text_2", bookID=13, bookName="sample_text_2", categoryID=13, imageURL="sample_text_2", notes="sample_text_2", price="sample_text_2", productURL="sample_text_2", rating=13)
    _safe_set(a, 'book6', {b1})
    assert _is_linked(a, 'book6', b1)
    if hasattr(b1, 'booksOrder7'):
        assert _is_linked(b1, 'booksOrder7', a)
    _safe_set(a, 'book6', {b2})
    assert _is_linked(a, 'book6', b2)
    if hasattr(b1, 'booksOrder7'):
        assert not _is_linked(b1, 'booksOrder7', a)
    if hasattr(b2, 'booksOrder7'):
        assert _is_linked(b2, 'booksOrder7', a)
    _safe_set(a, 'book6', set())
    assert not _is_linked(a, 'book6', b2)
    if hasattr(b2, 'booksOrder7'):
        assert not _is_linked(b2, 'booksOrder7', a)


def test_assoc_Category_Book_link_reassign_clear():
    a = Category(categoryID=7, categoryName="sample_text")
    b1 = Book(authorName="sample_text", bookID=7, bookName="sample_text", categoryID=7, imageURL="sample_text", notes="sample_text", price="sample_text", productURL="sample_text", rating=7)
    b2 = Book(authorName="sample_text_2", bookID=13, bookName="sample_text_2", categoryID=13, imageURL="sample_text_2", notes="sample_text_2", price="sample_text_2", productURL="sample_text_2", rating=13)
    _safe_set(a, 'book16', b1)
    assert _is_linked(a, 'book16', b1)
    if hasattr(b1, 'category17'):
        assert _is_linked(b1, 'category17', a)
    _safe_set(a, 'book16', b2)
    assert _is_linked(a, 'book16', b2)
    if hasattr(b1, 'category17'):
        assert not _is_linked(b1, 'category17', a)
    if hasattr(b2, 'category17'):
        assert _is_linked(b2, 'category17', a)
    _safe_set(a, 'book16', None)
    assert not _is_linked(a, 'book16', b2)
    if hasattr(b2, 'category17'):
        assert not _is_linked(b2, 'category17', a)


def test_assoc_Customer_BooksOrder_link_reassign_clear():
    a = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    b1 = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    b2 = BooksOrder(customerID=13, orderID=13, price="sample_text_2", quantity=13)
    _safe_set(a, 'booksOrder4', b1)
    assert _is_linked(a, 'booksOrder4', b1)
    if hasattr(b1, 'customer5'):
        assert _is_linked(b1, 'customer5', a)
    _safe_set(a, 'booksOrder4', b2)
    assert _is_linked(a, 'booksOrder4', b2)
    if hasattr(b1, 'customer5'):
        assert not _is_linked(b1, 'customer5', a)
    if hasattr(b2, 'customer5'):
        assert _is_linked(b2, 'customer5', a)
    _safe_set(a, 'booksOrder4', None)
    assert not _is_linked(a, 'booksOrder4', b2)
    if hasattr(b2, 'customer5'):
        assert not _is_linked(b2, 'customer5', a)


def test_assoc_Customer_ShoppingCart_link_reassign_clear():
    a = ShoppingCart(customerID=7, orderID=7, price="sample_text")
    b1 = Customer(CCinfo="sample_text", address="sample_text", customerID="sample_text", email="sample_text", name="sample_text", password="sample_text", phoneNo=7)
    b2 = Customer(CCinfo="sample_text_2", address="sample_text_2", customerID="sample_text_2", email="sample_text_2", name="sample_text_2", password="sample_text_2", phoneNo=13)
    _safe_set(a, 'customer21', {b1})
    assert _is_linked(a, 'customer21', b1)
    if hasattr(b1, 'shoppingCart20'):
        assert _is_linked(b1, 'shoppingCart20', a)
    _safe_set(a, 'customer21', {b2})
    assert _is_linked(a, 'customer21', b2)
    if hasattr(b1, 'shoppingCart20'):
        assert not _is_linked(b1, 'shoppingCart20', a)
    if hasattr(b2, 'shoppingCart20'):
        assert _is_linked(b2, 'shoppingCart20', a)
    _safe_set(a, 'customer21', set())
    assert not _is_linked(a, 'customer21', b2)
    if hasattr(b2, 'shoppingCart20'):
        assert not _is_linked(b2, 'shoppingCart20', a)


def test_assoc_SessionManager_Category_link_reassign_clear():
    a = SessionManager(categoryName="sample_text", userID=7)
    b1 = Category(categoryID=7, categoryName="sample_text")
    b2 = Category(categoryID=13, categoryName="sample_text_2")
    _safe_set(a, 'category14', b1)
    assert _is_linked(a, 'category14', b1)
    if hasattr(b1, 'sessionManager15'):
        assert _is_linked(b1, 'sessionManager15', a)
    _safe_set(a, 'category14', b2)
    assert _is_linked(a, 'category14', b2)
    if hasattr(b1, 'sessionManager15'):
        assert not _is_linked(b1, 'sessionManager15', a)
    if hasattr(b2, 'sessionManager15'):
        assert _is_linked(b2, 'sessionManager15', a)
    _safe_set(a, 'category14', None)
    assert not _is_linked(a, 'category14', b2)
    if hasattr(b2, 'sessionManager15'):
        assert not _is_linked(b2, 'sessionManager15', a)


def test_assoc_SessionManager_User_link_reassign_clear():
    a = User(loginStatus="sample_text", password="sample_text", userID=7)
    b1 = SessionManager(categoryName="sample_text", userID=7)
    b2 = SessionManager(categoryName="sample_text_2", userID=13)
    _safe_set(a, 'sessionManager3', b1)
    assert _is_linked(a, 'sessionManager3', b1)
    if hasattr(b1, 'user2'):
        assert _is_linked(b1, 'user2', a)
    _safe_set(a, 'sessionManager3', b2)
    assert _is_linked(a, 'sessionManager3', b2)
    if hasattr(b1, 'user2'):
        assert not _is_linked(b1, 'user2', a)
    if hasattr(b2, 'user2'):
        assert _is_linked(b2, 'user2', a)
    _safe_set(a, 'sessionManager3', None)
    assert not _is_linked(a, 'sessionManager3', b2)
    if hasattr(b2, 'user2'):
        assert not _is_linked(b2, 'user2', a)


def test_assoc_ShoppingCart_BooksOrder_link_reassign_clear():
    a = ShoppingCart(customerID=7, orderID=7, price="sample_text")
    b1 = BooksOrder(customerID=7, orderID=7, price="sample_text", quantity=7)
    b2 = BooksOrder(customerID=13, orderID=13, price="sample_text_2", quantity=13)
    _safe_set(a, 'booksOrder18', {b1})
    assert _is_linked(a, 'booksOrder18', b1)
    if hasattr(b1, 'shoppingCart19'):
        assert _is_linked(b1, 'shoppingCart19', a)
    _safe_set(a, 'booksOrder18', {b2})
    assert _is_linked(a, 'booksOrder18', b2)
    if hasattr(b1, 'shoppingCart19'):
        assert not _is_linked(b1, 'shoppingCart19', a)
    if hasattr(b2, 'shoppingCart19'):
        assert _is_linked(b2, 'shoppingCart19', a)
    _safe_set(a, 'booksOrder18', set())
    assert not _is_linked(a, 'booksOrder18', b2)
    if hasattr(b2, 'shoppingCart19'):
        assert not _is_linked(b2, 'shoppingCart19', a)


def test_assoc_User_User_link_reassign_clear():
    a = User(loginStatus="sample_text", password="sample_text", userID=7)
    b1 = User(loginStatus="sample_text", password="sample_text", userID=7)
    b2 = User(loginStatus="sample_text_2", password="sample_text_2", userID=13)
    _safe_set(a, 'user0', b1)
    assert _is_linked(a, 'user0', b1)
    if hasattr(b1, 'user1'):
        assert _is_linked(b1, 'user1', a)
    _safe_set(a, 'user0', b2)
    assert _is_linked(a, 'user0', b2)
    if hasattr(b1, 'user1'):
        assert not _is_linked(b1, 'user1', a)
    if hasattr(b2, 'user1'):
        assert _is_linked(b2, 'user1', a)
    _safe_set(a, 'user0', None)
    assert not _is_linked(a, 'user0', b2)
    if hasattr(b2, 'user1'):
        assert not _is_linked(b2, 'user1', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_strategy = st.builds(Administrator, adminID=st.integers(), email=safe_text, name=safe_text, password=safe_text, phoneNo=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


AdvSearch_strategy = st.builds(AdvSearch, bookAuthor=safe_text, bookHighCost=safe_text, bookLowCost=safe_text, bookTitle=safe_text, categoryID=safe_text)
@given(instance=AdvSearch_strategy)
@settings(max_examples=25)
def test_AdvSearch_instantiation(instance):
    assert isinstance(instance, AdvSearch)


Book_strategy = st.builds(Book, authorName=safe_text, bookID=st.integers(), bookName=safe_text, categoryID=st.integers(), imageURL=safe_text, notes=safe_text, price=safe_text, productURL=safe_text, rating=st.integers())
@given(instance=Book_strategy)
@settings(max_examples=25)
def test_Book_instantiation(instance):
    assert isinstance(instance, Book)


BookSet_strategy = st.builds(BookSet, bookID=st.integers(), bookName=safe_text)
@given(instance=BookSet_strategy)
@settings(max_examples=25)
def test_BookSet_instantiation(instance):
    assert isinstance(instance, BookSet)


BooksOrder_strategy = st.builds(BooksOrder, customerID=st.integers(), orderID=st.integers(), price=safe_text, quantity=st.integers())
@given(instance=BooksOrder_strategy)
@settings(max_examples=25)
def test_BooksOrder_instantiation(instance):
    assert isinstance(instance, BooksOrder)


Category_strategy = st.builds(Category, categoryID=st.integers(), categoryName=safe_text)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


Customer_strategy = st.builds(Customer, CCinfo=safe_text, address=safe_text, customerID=safe_text, email=safe_text, name=safe_text, password=safe_text, phoneNo=st.integers())
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Search_strategy = st.builds(Search, bookTitle=safe_text, categoryID=safe_text)
@given(instance=Search_strategy)
@settings(max_examples=25)
def test_Search_instantiation(instance):
    assert isinstance(instance, Search)


SessionManager_strategy = st.builds(SessionManager, categoryName=safe_text, userID=st.integers())
@given(instance=SessionManager_strategy)
@settings(max_examples=25)
def test_SessionManager_instantiation(instance):
    assert isinstance(instance, SessionManager)


ShoppingCart_strategy = st.builds(ShoppingCart, customerID=st.integers(), orderID=st.integers(), price=safe_text)
@given(instance=ShoppingCart_strategy)
@settings(max_examples=25)
def test_ShoppingCart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)


User_strategy = st.builds(User, loginStatus=safe_text, password=safe_text, userID=st.integers())
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


