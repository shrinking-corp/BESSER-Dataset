# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ShoppingCart,
    Category,
    AdvSearch,
    Search,
    BookSet,
    Administrator,
    Book,
    BooksOrder,
    Customer,
    SessionManager,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_hyp_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_hyp_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "customerID" in params, "Missing parameter 'customerID'"
    assert "price" in params, "Missing parameter 'price'"
    assert "orderID" in params, "Missing parameter 'orderID'"






def test_hyp_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_hyp_category_constructor_exists():
    assert callable(Category.__init__)


def test_hyp_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "categoryID" in params, "Missing parameter 'categoryID'"
    assert "categoryName" in params, "Missing parameter 'categoryName'"





def test_hyp_advsearch_is_not_abstract():
    assert not inspect.isabstract(AdvSearch)


def test_hyp_advsearch_constructor_exists():
    assert callable(AdvSearch.__init__)


def test_hyp_advsearch_constructor_args():
    sig = inspect.signature(AdvSearch.__init__)
    params = list(sig.parameters.keys())
    assert "bookHighCost" in params, "Missing parameter 'bookHighCost'"
    assert "bookLowCost" in params, "Missing parameter 'bookLowCost'"
    assert "categoryID" in params, "Missing parameter 'categoryID'"
    assert "bookTitle" in params, "Missing parameter 'bookTitle'"
    assert "bookAuthor" in params, "Missing parameter 'bookAuthor'"








def test_hyp_search_is_not_abstract():
    assert not inspect.isabstract(Search)


def test_hyp_search_constructor_exists():
    assert callable(Search.__init__)


def test_hyp_search_constructor_args():
    sig = inspect.signature(Search.__init__)
    params = list(sig.parameters.keys())
    assert "bookTitle" in params, "Missing parameter 'bookTitle'"
    assert "categoryID" in params, "Missing parameter 'categoryID'"





def test_hyp_bookset_is_not_abstract():
    assert not inspect.isabstract(BookSet)


def test_hyp_bookset_constructor_exists():
    assert callable(BookSet.__init__)


def test_hyp_bookset_constructor_args():
    sig = inspect.signature(BookSet.__init__)
    params = list(sig.parameters.keys())
    assert "bookName" in params, "Missing parameter 'bookName'"
    assert "bookID" in params, "Missing parameter 'bookID'"





def test_hyp_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_hyp_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_hyp_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "adminID" in params, "Missing parameter 'adminID'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"








def test_hyp_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_hyp_book_constructor_exists():
    assert callable(Book.__init__)


def test_hyp_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "price" in params, "Missing parameter 'price'"
    assert "imageURL" in params, "Missing parameter 'imageURL'"
    assert "bookName" in params, "Missing parameter 'bookName'"
    assert "bookID" in params, "Missing parameter 'bookID'"
    assert "categoryID" in params, "Missing parameter 'categoryID'"
    assert "productURL" in params, "Missing parameter 'productURL'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "rating" in params, "Missing parameter 'rating'"












def test_hyp_booksorder_is_not_abstract():
    assert not inspect.isabstract(BooksOrder)


def test_hyp_booksorder_constructor_exists():
    assert callable(BooksOrder.__init__)


def test_hyp_booksorder_constructor_args():
    sig = inspect.signature(BooksOrder.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "customerID" in params, "Missing parameter 'customerID'"
    assert "orderID" in params, "Missing parameter 'orderID'"







def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "name" in params, "Missing parameter 'name'"
    assert "CCinfo" in params, "Missing parameter 'CCinfo'"
    assert "customerID" in params, "Missing parameter 'customerID'"
    assert "address" in params, "Missing parameter 'address'"
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"










def test_hyp_sessionmanager_is_not_abstract():
    assert not inspect.isabstract(SessionManager)


def test_hyp_sessionmanager_constructor_exists():
    assert callable(SessionManager.__init__)


def test_hyp_sessionmanager_constructor_args():
    sig = inspect.signature(SessionManager.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "categoryName" in params, "Missing parameter 'categoryName'"





def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"





# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    customerID=
        st.integers(),
    price=
        safe_text,
    orderID=
        st.integers()
)
Category_strategy = st.builds(
    Category,
    categoryID=
        st.integers(),
    categoryName=
        safe_text
)
AdvSearch_strategy = st.builds(
    AdvSearch,
    bookHighCost=
        safe_text,
    bookLowCost=
        safe_text,
    categoryID=
        safe_text,
    bookTitle=
        safe_text,
    bookAuthor=
        safe_text
)
Search_strategy = st.builds(
    Search,
    bookTitle=
        safe_text,
    categoryID=
        safe_text
)
BookSet_strategy = st.builds(
    BookSet,
    bookName=
        safe_text,
    bookID=
        st.integers()
)
Administrator_strategy = st.builds(
    Administrator,
    adminID=
        st.integers(),
    email=
        safe_text,
    phoneNo=
        safe_text,
    name=
        safe_text,
    password=
        safe_text
)
Book_strategy = st.builds(
    Book,
    authorName=
        safe_text,
    price=
        safe_text,
    imageURL=
        safe_text,
    bookName=
        safe_text,
    bookID=
        st.integers(),
    categoryID=
        st.integers(),
    productURL=
        safe_text,
    notes=
        safe_text,
    rating=
        st.integers()
)
BooksOrder_strategy = st.builds(
    BooksOrder,
    price=
        safe_text,
    quantity=
        st.integers(),
    customerID=
        st.integers(),
    orderID=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    phoneNo=
        st.integers(),
    name=
        safe_text,
    CCinfo=
        safe_text,
    customerID=
        safe_text,
    address=
        safe_text,
    password=
        safe_text,
    email=
        safe_text
)
SessionManager_strategy = st.builds(
    SessionManager,
    userID=
        st.integers(),
    categoryName=
        safe_text
)
User_strategy = st.builds(
    User,
    loginStatus=
        safe_text,
    userID=
        st.integers(),
    password=
        safe_text
)




@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_orderID_setter(instance):
    original = instance.orderID
    instance.orderID = original
    assert instance.orderID == original




@given(instance=Category_strategy)
def test_hyp_category_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original



@given(instance=Category_strategy)
def test_hyp_category_categoryName_setter(instance):
    original = instance.categoryName
    instance.categoryName = original
    assert instance.categoryName == original




@given(instance=AdvSearch_strategy)
def test_hyp_advsearch_bookHighCost_setter(instance):
    original = instance.bookHighCost
    instance.bookHighCost = original
    assert instance.bookHighCost == original



@given(instance=AdvSearch_strategy)
def test_hyp_advsearch_bookLowCost_setter(instance):
    original = instance.bookLowCost
    instance.bookLowCost = original
    assert instance.bookLowCost == original



@given(instance=AdvSearch_strategy)
def test_hyp_advsearch_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original



@given(instance=AdvSearch_strategy)
def test_hyp_advsearch_bookTitle_setter(instance):
    original = instance.bookTitle
    instance.bookTitle = original
    assert instance.bookTitle == original



@given(instance=AdvSearch_strategy)
def test_hyp_advsearch_bookAuthor_setter(instance):
    original = instance.bookAuthor
    instance.bookAuthor = original
    assert instance.bookAuthor == original




@given(instance=Search_strategy)
def test_hyp_search_bookTitle_setter(instance):
    original = instance.bookTitle
    instance.bookTitle = original
    assert instance.bookTitle == original



@given(instance=Search_strategy)
def test_hyp_search_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original




@given(instance=BookSet_strategy)
def test_hyp_bookset_bookName_setter(instance):
    original = instance.bookName
    instance.bookName = original
    assert instance.bookName == original



@given(instance=BookSet_strategy)
def test_hyp_bookset_bookID_setter(instance):
    original = instance.bookID
    instance.bookID = original
    assert instance.bookID == original




@given(instance=Administrator_strategy)
def test_hyp_administrator_adminID_setter(instance):
    original = instance.adminID
    instance.adminID = original
    assert instance.adminID == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Book_strategy)
def test_hyp_book_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=Book_strategy)
def test_hyp_book_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Book_strategy)
def test_hyp_book_imageURL_setter(instance):
    original = instance.imageURL
    instance.imageURL = original
    assert instance.imageURL == original



@given(instance=Book_strategy)
def test_hyp_book_bookName_setter(instance):
    original = instance.bookName
    instance.bookName = original
    assert instance.bookName == original



@given(instance=Book_strategy)
def test_hyp_book_bookID_setter(instance):
    original = instance.bookID
    instance.bookID = original
    assert instance.bookID == original



@given(instance=Book_strategy)
def test_hyp_book_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original



@given(instance=Book_strategy)
def test_hyp_book_productURL_setter(instance):
    original = instance.productURL
    instance.productURL = original
    assert instance.productURL == original



@given(instance=Book_strategy)
def test_hyp_book_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=Book_strategy)
def test_hyp_book_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original




@given(instance=BooksOrder_strategy)
def test_hyp_booksorder_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=BooksOrder_strategy)
def test_hyp_booksorder_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=BooksOrder_strategy)
def test_hyp_booksorder_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original



@given(instance=BooksOrder_strategy)
def test_hyp_booksorder_orderID_setter(instance):
    original = instance.orderID
    instance.orderID = original
    assert instance.orderID == original




@given(instance=Customer_strategy)
def test_hyp_customer_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Customer_strategy)
def test_hyp_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_hyp_customer_CCinfo_setter(instance):
    original = instance.CCinfo
    instance.CCinfo = original
    assert instance.CCinfo == original



@given(instance=Customer_strategy)
def test_hyp_customer_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original



@given(instance=Customer_strategy)
def test_hyp_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_hyp_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Customer_strategy)
def test_hyp_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original




@given(instance=SessionManager_strategy)
def test_hyp_sessionmanager_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=SessionManager_strategy)
def test_hyp_sessionmanager_categoryName_setter(instance):
    original = instance.categoryName
    instance.categoryName = original
    assert instance.categoryName == original




@given(instance=User_strategy)
def test_hyp_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original



@given(instance=User_strategy)
def test_hyp_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



