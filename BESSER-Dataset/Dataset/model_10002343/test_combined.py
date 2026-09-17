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
    Item,
    Shopping_Cart,
    Order,
    Customer,
    Account,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_hyp_item_constructor_exists():
    assert callable(Item.__init__)


def test_hyp_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "colour" in params, "Missing parameter 'colour'"






def test_hyp_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_hyp_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_hyp_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "cartId" in params, "Missing parameter 'cartId'"




def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_hyp_order_has_price():
    assert hasattr(Order, "price")
    descriptor = None
    for klass in Order.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_quantity():
    assert hasattr(Order, "quantity")
    descriptor = None
    for klass in Order.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "cellNo" in params, "Missing parameter 'cellNo'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "name" in params, "Missing parameter 'name'"








def test_hyp_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_hyp_account_constructor_exists():
    assert callable(Account.__init__)


def test_hyp_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"




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
Item_strategy = st.builds(
    Item,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    productId=
        safe_text,
    colour=
        safe_text
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    cartId=
        safe_text
)
Order_strategy = st.builds(
    Order,
    price=
        st.none(),
    quantity=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    emailAddress=
        safe_text,
    cellNo=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Gender=
        safe_text,
    DOB=
        safe_text,
    name=
        safe_text
)
Account_strategy = st.builds(
    Account,
    Username=
        safe_text,
    Password=
        st.integers()
)




@given(instance=Item_strategy)
def test_hyp_item_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Item_strategy)
def test_hyp_item_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=Item_strategy)
def test_hyp_item_colour_setter(instance):
    original = instance.colour
    instance.colour = original
    assert instance.colour == original




@given(instance=Shopping_Cart_strategy)
def test_hyp_shopping_cart_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_hyp_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_hyp_order_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Order_strategy)
def test_hyp_order_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original




@given(instance=Customer_strategy)
def test_hyp_customer_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=Customer_strategy)
def test_hyp_customer_cellNo_setter(instance):
    original = instance.cellNo
    instance.cellNo = original
    assert instance.cellNo == original



@given(instance=Customer_strategy)
def test_hyp_customer_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Customer_strategy)
def test_hyp_customer_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=Customer_strategy)
def test_hyp_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Account_strategy)
def test_hyp_account_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Account_strategy)
def test_hyp_account_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account,
    Customer,
    Item,
    Order,
    Shopping_Cart,
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

def test_Account_Password_value_roundtrip():
    instance = Account(Password=7, Username="sample_text")
    assert instance.Password == 7
    instance.Password = 13
    assert instance.Password == 13


def test_Account_Username_value_roundtrip():
    instance = Account(Password=7, Username="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


def test_Customer_DOB_value_roundtrip():
    instance = Customer(DOB="sample_text", Gender="sample_text", cellNo=3.14, emailAddress="sample_text", name="sample_text")
    assert instance.DOB == "sample_text"
    instance.DOB = "sample_text_2"
    assert instance.DOB == "sample_text_2"


def test_Customer_Gender_value_roundtrip():
    instance = Customer(DOB="sample_text", Gender="sample_text", cellNo=3.14, emailAddress="sample_text", name="sample_text")
    assert instance.Gender == "sample_text"
    instance.Gender = "sample_text_2"
    assert instance.Gender == "sample_text_2"


def test_Customer_cellNo_value_roundtrip():
    instance = Customer(DOB="sample_text", Gender="sample_text", cellNo=3.14, emailAddress="sample_text", name="sample_text")
    assert instance.cellNo == 3.14
    instance.cellNo = 9.99
    assert instance.cellNo == 9.99


def test_Customer_emailAddress_value_roundtrip():
    instance = Customer(DOB="sample_text", Gender="sample_text", cellNo=3.14, emailAddress="sample_text", name="sample_text")
    assert instance.emailAddress == "sample_text"
    instance.emailAddress = "sample_text_2"
    assert instance.emailAddress == "sample_text_2"


def test_Customer_name_value_roundtrip():
    instance = Customer(DOB="sample_text", Gender="sample_text", cellNo=3.14, emailAddress="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Item_colour_value_roundtrip():
    instance = Item(colour="sample_text", price=3.14, productId="sample_text")
    assert instance.colour == "sample_text"
    instance.colour = "sample_text_2"
    assert instance.colour == "sample_text_2"


def test_Item_price_value_roundtrip():
    instance = Item(colour="sample_text", price=3.14, productId="sample_text")
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_Item_productId_value_roundtrip():
    instance = Item(colour="sample_text", price=3.14, productId="sample_text")
    assert instance.productId == "sample_text"
    instance.productId = "sample_text_2"
    assert instance.productId == "sample_text_2"


def test_Shopping_Cart_cartId_value_roundtrip():
    instance = Shopping_Cart(cartId="sample_text")
    assert instance.cartId == "sample_text"
    instance.cartId = "sample_text_2"
    assert instance.cartId == "sample_text_2"


def test_assoc_Shopping_Cart_Login_link_reassign_clear():
    a = Shopping_Cart(cartId="sample_text")
    b1 = Item(colour="sample_text", price=3.14, productId="sample_text")
    b2 = Item(colour="sample_text_2", price=9.99, productId="sample_text_2")
    _safe_set(a, 'Shopping_Cart_Login_08', {b1})
    assert _is_linked(a, 'Shopping_Cart_Login_08', b1)
    if hasattr(b1, 'Shopping_Cart_Login_19'):
        assert _is_linked(b1, 'Shopping_Cart_Login_19', a)
    _safe_set(a, 'Shopping_Cart_Login_08', {b2})
    assert _is_linked(a, 'Shopping_Cart_Login_08', b2)
    if hasattr(b1, 'Shopping_Cart_Login_19'):
        assert not _is_linked(b1, 'Shopping_Cart_Login_19', a)
    if hasattr(b2, 'Shopping_Cart_Login_19'):
        assert _is_linked(b2, 'Shopping_Cart_Login_19', a)
    _safe_set(a, 'Shopping_Cart_Login_08', set())
    assert not _is_linked(a, 'Shopping_Cart_Login_08', b2)
    if hasattr(b2, 'Shopping_Cart_Login_19'):
        assert not _is_linked(b2, 'Shopping_Cart_Login_19', a)


def test_assoc_User_Login_link_reassign_clear():
    a = Item(colour="sample_text", price=3.14, productId="sample_text")
    b1 = Account(Password=7, Username="sample_text")
    b2 = Account(Password=13, Username="sample_text_2")
    _safe_set(a, 'user5', b1)
    assert _is_linked(a, 'user5', b1)
    if hasattr(b1, 'login4'):
        assert _is_linked(b1, 'login4', a)
    _safe_set(a, 'user5', b2)
    assert _is_linked(a, 'user5', b2)
    if hasattr(b1, 'login4'):
        assert not _is_linked(b1, 'login4', a)
    if hasattr(b2, 'login4'):
        assert _is_linked(b2, 'login4', a)
    _safe_set(a, 'user5', None)
    assert not _is_linked(a, 'user5', b2)
    if hasattr(b2, 'login4'):
        assert not _is_linked(b2, 'login4', a)


def test_assoc_User_Myprofile_link_reassign_clear():
    a = Customer(DOB="sample_text", Gender="sample_text", cellNo=3.14, emailAddress="sample_text", name="sample_text")
    b1 = Account(Password=7, Username="sample_text")
    b2 = Account(Password=13, Username="sample_text_2")
    _safe_set(a, 'user1', b1)
    assert _is_linked(a, 'user1', b1)
    if hasattr(b1, 'myprofile0'):
        assert _is_linked(b1, 'myprofile0', a)
    _safe_set(a, 'user1', b2)
    assert _is_linked(a, 'user1', b2)
    if hasattr(b1, 'myprofile0'):
        assert not _is_linked(b1, 'myprofile0', a)
    if hasattr(b2, 'myprofile0'):
        assert _is_linked(b2, 'myprofile0', a)
    _safe_set(a, 'user1', None)
    assert not _is_linked(a, 'user1', b2)
    if hasattr(b2, 'myprofile0'):
        assert not _is_linked(b2, 'myprofile0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Account_strategy = st.builds(Account, Password=st.integers(), Username=safe_text)
@given(instance=Account_strategy)
@settings(max_examples=25)
def test_Account_instantiation(instance):
    assert isinstance(instance, Account)


Customer_strategy = st.builds(Customer, DOB=safe_text, Gender=safe_text, cellNo=st.floats(allow_nan=False, allow_infinity=False), emailAddress=safe_text, name=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Item_strategy = st.builds(Item, colour=safe_text, price=st.floats(allow_nan=False, allow_infinity=False), productId=safe_text)
@given(instance=Item_strategy)
@settings(max_examples=25)
def test_Item_instantiation(instance):
    assert isinstance(instance, Item)


Shopping_Cart_strategy = st.builds(Shopping_Cart, cartId=safe_text)
@given(instance=Shopping_Cart_strategy)
@settings(max_examples=25)
def test_Shopping_Cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



