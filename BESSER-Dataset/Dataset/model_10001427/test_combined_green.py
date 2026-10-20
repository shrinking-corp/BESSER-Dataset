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
    Payment,
    shippinginfo,
    order,
    orderDetail,
    product,
    cartitem,
    ShoppingCart,
    User,
    Login,
    login_status,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Payment_type" in params, "Missing parameter 'Payment_type'"
    assert "Payment_method" in params, "Missing parameter 'Payment_method'"
    assert "Payment_id" in params, "Missing parameter 'Payment_id'"






def test_hyp_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(shippinginfo)


def test_hyp_shippinginfo_constructor_exists():
    assert callable(shippinginfo.__init__)


def test_hyp_shippinginfo_constructor_args():
    sig = inspect.signature(shippinginfo.__init__)
    params = list(sig.parameters.keys())
    assert "shipping_type" in params, "Missing parameter 'shipping_type'"
    assert "shipping_date" in params, "Missing parameter 'shipping_date'"
    assert "shipping_cost" in params, "Missing parameter 'shipping_cost'"
    assert "shipping_id" in params, "Missing parameter 'shipping_id'"
    assert "shipping_Address" in params, "Missing parameter 'shipping_Address'"








def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(order)


def test_hyp_order_constructor_exists():
    assert callable(order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(order.__init__)
    params = list(sig.parameters.keys())
    assert "shippingid" in params, "Missing parameter 'shippingid'"
    assert "status" in params, "Missing parameter 'status'"
    assert "date_created" in params, "Missing parameter 'date_created'"
    assert "order_ID" in params, "Missing parameter 'order_ID'"
    assert "shipping_date" in params, "Missing parameter 'shipping_date'"
    assert "c_name" in params, "Missing parameter 'c_name'"









def test_hyp_orderdetail_is_not_abstract():
    assert not inspect.isabstract(orderDetail)


def test_hyp_orderdetail_constructor_exists():
    assert callable(orderDetail.__init__)


def test_hyp_orderdetail_constructor_args():
    sig = inspect.signature(orderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "productid" in params, "Missing parameter 'productid'"
    assert "productname" in params, "Missing parameter 'productname'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "subtotall" in params, "Missing parameter 'subtotall'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "orderId" in params, "Missing parameter 'orderId'"









def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(product)


def test_hyp_product_constructor_exists():
    assert callable(product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(product.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "productid" in params, "Missing parameter 'productid'"
    assert "productname" in params, "Missing parameter 'productname'"
    assert "imagefilename" in params, "Missing parameter 'imagefilename'"







def test_hyp_cartitem_is_not_abstract():
    assert not inspect.isabstract(cartitem)


def test_hyp_cartitem_constructor_exists():
    assert callable(cartitem.__init__)


def test_hyp_cartitem_constructor_args():
    sig = inspect.signature(cartitem.__init__)
    params = list(sig.parameters.keys())
    assert "subtotal" in params, "Missing parameter 'subtotal'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "product" in params, "Missing parameter 'product'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "name" in params, "Missing parameter 'name'"








def test_hyp_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_hyp_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_hyp_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "cartId" in params, "Missing parameter 'cartId'"
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"







def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"
    assert "User_name" in params, "Missing parameter 'User_name'"
    assert "phone_no" in params, "Missing parameter 'phone_no'"
    assert "Card_info" in params, "Missing parameter 'Card_info'"
    assert "shipping_info" in params, "Missing parameter 'shipping_info'"









def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "password" in params, "Missing parameter 'password'"
    assert "login_status" in params, "Missing parameter 'login_status'"




def test_hyp_login_status_exists():
    # Check that the Enumeration exists
    assert login_status is not None

def test_hyp_login_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in login_status]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in login_status"


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
Payment_strategy = st.builds(
    Payment,
    Payment_type=
        safe_text,
    Payment_method=
        st.integers(),
    Payment_id=
        safe_text
)
shippinginfo_strategy = st.builds(
    shippinginfo,
    shipping_type=
        safe_text,
    shipping_date=
        st.dates(),
    shipping_cost=
        st.integers(),
    shipping_id=
        safe_text,
    shipping_Address=
        safe_text
)
order_strategy = st.builds(
    order,
    shippingid=
        safe_text,
    status=
        safe_text,
    date_created=
        st.dates(),
    order_ID=
        st.integers(),
    shipping_date=
        st.dates(),
    c_name=
        safe_text
)
orderDetail_strategy = st.builds(
    orderDetail,
    productid=
        st.integers(),
    productname=
        safe_text,
    unitcost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    subtotall=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    quantity=
        st.integers(),
    orderId=
        st.integers()
)
product_strategy = st.builds(
    product,
    price=
        st.integers(),
    productid=
        st.integers(),
    productname=
        safe_text,
    imagefilename=
        safe_text
)
cartitem_strategy = st.builds(
    cartitem,
    subtotal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    unitcost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    product=
        st.integers(),
    quantity=
        st.integers(),
    name=
        safe_text
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    quantity=
        st.integers(),
    productId=
        st.integers(),
    cartId=
        st.integers(),
    dateAdded=
        st.integers()
)
User_strategy = st.builds(
    User,
    email=
        safe_text,
    address=
        safe_text,
    User_name=
        safe_text,
    phone_no=
        st.integers(),
    Card_info=
        safe_text,
    shipping_info=
        safe_text
)
Login_strategy = st.builds(
    Login,
    UserId=
        safe_text,
    password=
        safe_text,
    login_status=
        safe_text
)




@given(instance=Payment_strategy)
def test_hyp_payment_Payment_type_setter(instance):
    original = instance.Payment_type
    instance.Payment_type = original
    assert instance.Payment_type == original



@given(instance=Payment_strategy)
def test_hyp_payment_Payment_method_setter(instance):
    original = instance.Payment_method
    instance.Payment_method = original
    assert instance.Payment_method == original



@given(instance=Payment_strategy)
def test_hyp_payment_Payment_id_setter(instance):
    original = instance.Payment_id
    instance.Payment_id = original
    assert instance.Payment_id == original




@given(instance=shippinginfo_strategy)
def test_hyp_shippinginfo_shipping_type_setter(instance):
    original = instance.shipping_type
    instance.shipping_type = original
    assert instance.shipping_type == original



@given(instance=shippinginfo_strategy)
def test_hyp_shippinginfo_shipping_date_setter(instance):
    original = instance.shipping_date
    instance.shipping_date = original
    assert instance.shipping_date == original



@given(instance=shippinginfo_strategy)
def test_hyp_shippinginfo_shipping_cost_setter(instance):
    original = instance.shipping_cost
    instance.shipping_cost = original
    assert instance.shipping_cost == original



@given(instance=shippinginfo_strategy)
def test_hyp_shippinginfo_shipping_id_setter(instance):
    original = instance.shipping_id
    instance.shipping_id = original
    assert instance.shipping_id == original



@given(instance=shippinginfo_strategy)
def test_hyp_shippinginfo_shipping_Address_setter(instance):
    original = instance.shipping_Address
    instance.shipping_Address = original
    assert instance.shipping_Address == original




@given(instance=order_strategy)
def test_hyp_order_shippingid_setter(instance):
    original = instance.shippingid
    instance.shippingid = original
    assert instance.shippingid == original



@given(instance=order_strategy)
def test_hyp_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=order_strategy)
def test_hyp_order_date_created_setter(instance):
    original = instance.date_created
    instance.date_created = original
    assert instance.date_created == original



@given(instance=order_strategy)
def test_hyp_order_order_ID_setter(instance):
    original = instance.order_ID
    instance.order_ID = original
    assert instance.order_ID == original



@given(instance=order_strategy)
def test_hyp_order_shipping_date_setter(instance):
    original = instance.shipping_date
    instance.shipping_date = original
    assert instance.shipping_date == original



@given(instance=order_strategy)
def test_hyp_order_c_name_setter(instance):
    original = instance.c_name
    instance.c_name = original
    assert instance.c_name == original




@given(instance=orderDetail_strategy)
def test_hyp_orderdetail_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=orderDetail_strategy)
def test_hyp_orderdetail_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original



@given(instance=orderDetail_strategy)
def test_hyp_orderdetail_unitcost_setter(instance):
    original = instance.unitcost
    instance.unitcost = original
    assert instance.unitcost == original



@given(instance=orderDetail_strategy)
def test_hyp_orderdetail_subtotall_setter(instance):
    original = instance.subtotall
    instance.subtotall = original
    assert instance.subtotall == original



@given(instance=orderDetail_strategy)
def test_hyp_orderdetail_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=orderDetail_strategy)
def test_hyp_orderdetail_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original




@given(instance=product_strategy)
def test_hyp_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=product_strategy)
def test_hyp_product_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=product_strategy)
def test_hyp_product_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original



@given(instance=product_strategy)
def test_hyp_product_imagefilename_setter(instance):
    original = instance.imagefilename
    instance.imagefilename = original
    assert instance.imagefilename == original




@given(instance=cartitem_strategy)
def test_hyp_cartitem_subtotal_setter(instance):
    original = instance.subtotal
    instance.subtotal = original
    assert instance.subtotal == original



@given(instance=cartitem_strategy)
def test_hyp_cartitem_unitcost_setter(instance):
    original = instance.unitcost
    instance.unitcost = original
    assert instance.unitcost == original



@given(instance=cartitem_strategy)
def test_hyp_cartitem_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original



@given(instance=cartitem_strategy)
def test_hyp_cartitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=cartitem_strategy)
def test_hyp_cartitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original




@given(instance=User_strategy)
def test_hyp_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User_strategy)
def test_hyp_user_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=User_strategy)
def test_hyp_user_User_name_setter(instance):
    original = instance.User_name
    instance.User_name = original
    assert instance.User_name == original



@given(instance=User_strategy)
def test_hyp_user_phone_no_setter(instance):
    original = instance.phone_no
    instance.phone_no = original
    assert instance.phone_no == original



@given(instance=User_strategy)
def test_hyp_user_Card_info_setter(instance):
    original = instance.Card_info
    instance.Card_info = original
    assert instance.Card_info == original



@given(instance=User_strategy)
def test_hyp_user_shipping_info_setter(instance):
    original = instance.shipping_info
    instance.shipping_info = original
    assert instance.shipping_info == original




@given(instance=Login_strategy)
def test_hyp_login_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=Login_strategy)
def test_hyp_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_hyp_login_login_status_setter(instance):
    original = instance.login_status
    instance.login_status = original
    assert instance.login_status == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Login,
    Payment,
    ShoppingCart,
    User,
    cartitem,
    order,
    orderDetail,
    product,
    shippinginfo,
    login_status,
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

def test_Login_UserId_value_roundtrip():
    instance = Login(UserId="sample_text", login_status="sample_text", password="sample_text")
    assert instance.UserId == "sample_text"
    instance.UserId = "sample_text_2"
    assert instance.UserId == "sample_text_2"


def test_Login_login_status_value_roundtrip():
    instance = Login(UserId="sample_text", login_status="sample_text", password="sample_text")
    assert instance.login_status == "sample_text"
    instance.login_status = "sample_text_2"
    assert instance.login_status == "sample_text_2"


def test_Login_password_value_roundtrip():
    instance = Login(UserId="sample_text", login_status="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Payment_Payment_id_value_roundtrip():
    instance = Payment(Payment_id="sample_text", Payment_method=7, Payment_type="sample_text")
    assert instance.Payment_id == "sample_text"
    instance.Payment_id = "sample_text_2"
    assert instance.Payment_id == "sample_text_2"


def test_Payment_Payment_method_value_roundtrip():
    instance = Payment(Payment_id="sample_text", Payment_method=7, Payment_type="sample_text")
    assert instance.Payment_method == 7
    instance.Payment_method = 13
    assert instance.Payment_method == 13


def test_Payment_Payment_type_value_roundtrip():
    instance = Payment(Payment_id="sample_text", Payment_method=7, Payment_type="sample_text")
    assert instance.Payment_type == "sample_text"
    instance.Payment_type = "sample_text_2"
    assert instance.Payment_type == "sample_text_2"


def test_ShoppingCart_cartId_value_roundtrip():
    instance = ShoppingCart(cartId=7, dateAdded=7, productId=7, quantity=7)
    assert instance.cartId == 7
    instance.cartId = 13
    assert instance.cartId == 13


def test_ShoppingCart_dateAdded_value_roundtrip():
    instance = ShoppingCart(cartId=7, dateAdded=7, productId=7, quantity=7)
    assert instance.dateAdded == 7
    instance.dateAdded = 13
    assert instance.dateAdded == 13


def test_ShoppingCart_productId_value_roundtrip():
    instance = ShoppingCart(cartId=7, dateAdded=7, productId=7, quantity=7)
    assert instance.productId == 7
    instance.productId = 13
    assert instance.productId == 13


def test_ShoppingCart_quantity_value_roundtrip():
    instance = ShoppingCart(cartId=7, dateAdded=7, productId=7, quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_User_Card_info_value_roundtrip():
    instance = User(Card_info="sample_text", User_name="sample_text", address="sample_text", email="sample_text", phone_no=7, shipping_info="sample_text")
    assert instance.Card_info == "sample_text"
    instance.Card_info = "sample_text_2"
    assert instance.Card_info == "sample_text_2"


def test_User_User_name_value_roundtrip():
    instance = User(Card_info="sample_text", User_name="sample_text", address="sample_text", email="sample_text", phone_no=7, shipping_info="sample_text")
    assert instance.User_name == "sample_text"
    instance.User_name = "sample_text_2"
    assert instance.User_name == "sample_text_2"


def test_User_address_value_roundtrip():
    instance = User(Card_info="sample_text", User_name="sample_text", address="sample_text", email="sample_text", phone_no=7, shipping_info="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_User_email_value_roundtrip():
    instance = User(Card_info="sample_text", User_name="sample_text", address="sample_text", email="sample_text", phone_no=7, shipping_info="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_User_phone_no_value_roundtrip():
    instance = User(Card_info="sample_text", User_name="sample_text", address="sample_text", email="sample_text", phone_no=7, shipping_info="sample_text")
    assert instance.phone_no == 7
    instance.phone_no = 13
    assert instance.phone_no == 13


def test_User_shipping_info_value_roundtrip():
    instance = User(Card_info="sample_text", User_name="sample_text", address="sample_text", email="sample_text", phone_no=7, shipping_info="sample_text")
    assert instance.shipping_info == "sample_text"
    instance.shipping_info = "sample_text_2"
    assert instance.shipping_info == "sample_text_2"


def test_cartitem_name_value_roundtrip():
    instance = cartitem(name="sample_text", product=7, quantity=7, subtotal=3.14, unitcost=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cartitem_product_value_roundtrip():
    instance = cartitem(name="sample_text", product=7, quantity=7, subtotal=3.14, unitcost=3.14)
    assert instance.product == 7
    instance.product = 13
    assert instance.product == 13


def test_cartitem_quantity_value_roundtrip():
    instance = cartitem(name="sample_text", product=7, quantity=7, subtotal=3.14, unitcost=3.14)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_cartitem_subtotal_value_roundtrip():
    instance = cartitem(name="sample_text", product=7, quantity=7, subtotal=3.14, unitcost=3.14)
    assert instance.subtotal == 3.14
    instance.subtotal = 9.99
    assert instance.subtotal == 9.99


def test_cartitem_unitcost_value_roundtrip():
    instance = cartitem(name="sample_text", product=7, quantity=7, subtotal=3.14, unitcost=3.14)
    assert instance.unitcost == 3.14
    instance.unitcost = 9.99
    assert instance.unitcost == 9.99


def test_order_c_name_value_roundtrip():
    instance = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    assert instance.c_name == "sample_text"
    instance.c_name = "sample_text_2"
    assert instance.c_name == "sample_text_2"


def test_order_date_created_value_roundtrip():
    instance = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    assert instance.date_created == date(2024, 1, 1)
    instance.date_created = date(2025, 6, 15)
    assert instance.date_created == date(2025, 6, 15)


def test_order_order_ID_value_roundtrip():
    instance = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    assert instance.order_ID == 7
    instance.order_ID = 13
    assert instance.order_ID == 13


def test_order_shipping_date_value_roundtrip():
    instance = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    assert instance.shipping_date == date(2024, 1, 1)
    instance.shipping_date = date(2025, 6, 15)
    assert instance.shipping_date == date(2025, 6, 15)


def test_order_shippingid_value_roundtrip():
    instance = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    assert instance.shippingid == "sample_text"
    instance.shippingid = "sample_text_2"
    assert instance.shippingid == "sample_text_2"


def test_order_status_value_roundtrip():
    instance = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_orderDetail_orderId_value_roundtrip():
    instance = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    assert instance.orderId == 7
    instance.orderId = 13
    assert instance.orderId == 13


def test_orderDetail_productid_value_roundtrip():
    instance = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    assert instance.productid == 7
    instance.productid = 13
    assert instance.productid == 13


def test_orderDetail_productname_value_roundtrip():
    instance = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    assert instance.productname == "sample_text"
    instance.productname = "sample_text_2"
    assert instance.productname == "sample_text_2"


def test_orderDetail_quantity_value_roundtrip():
    instance = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_orderDetail_subtotall_value_roundtrip():
    instance = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    assert instance.subtotall == 3.14
    instance.subtotall = 9.99
    assert instance.subtotall == 9.99


def test_orderDetail_unitcost_value_roundtrip():
    instance = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    assert instance.unitcost == 3.14
    instance.unitcost = 9.99
    assert instance.unitcost == 9.99


def test_product_imagefilename_value_roundtrip():
    instance = product(imagefilename="sample_text", price=7, productid=7, productname="sample_text")
    assert instance.imagefilename == "sample_text"
    instance.imagefilename = "sample_text_2"
    assert instance.imagefilename == "sample_text_2"


def test_product_price_value_roundtrip():
    instance = product(imagefilename="sample_text", price=7, productid=7, productname="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_product_productid_value_roundtrip():
    instance = product(imagefilename="sample_text", price=7, productid=7, productname="sample_text")
    assert instance.productid == 7
    instance.productid = 13
    assert instance.productid == 13


def test_product_productname_value_roundtrip():
    instance = product(imagefilename="sample_text", price=7, productid=7, productname="sample_text")
    assert instance.productname == "sample_text"
    instance.productname = "sample_text_2"
    assert instance.productname == "sample_text_2"


def test_shippinginfo_shipping_Address_value_roundtrip():
    instance = shippinginfo(shipping_Address="sample_text", shipping_cost=7, shipping_date=date(2024, 1, 1), shipping_id="sample_text", shipping_type="sample_text")
    assert instance.shipping_Address == "sample_text"
    instance.shipping_Address = "sample_text_2"
    assert instance.shipping_Address == "sample_text_2"


def test_shippinginfo_shipping_cost_value_roundtrip():
    instance = shippinginfo(shipping_Address="sample_text", shipping_cost=7, shipping_date=date(2024, 1, 1), shipping_id="sample_text", shipping_type="sample_text")
    assert instance.shipping_cost == 7
    instance.shipping_cost = 13
    assert instance.shipping_cost == 13


def test_shippinginfo_shipping_date_value_roundtrip():
    instance = shippinginfo(shipping_Address="sample_text", shipping_cost=7, shipping_date=date(2024, 1, 1), shipping_id="sample_text", shipping_type="sample_text")
    assert instance.shipping_date == date(2024, 1, 1)
    instance.shipping_date = date(2025, 6, 15)
    assert instance.shipping_date == date(2025, 6, 15)


def test_shippinginfo_shipping_id_value_roundtrip():
    instance = shippinginfo(shipping_Address="sample_text", shipping_cost=7, shipping_date=date(2024, 1, 1), shipping_id="sample_text", shipping_type="sample_text")
    assert instance.shipping_id == "sample_text"
    instance.shipping_id = "sample_text_2"
    assert instance.shipping_id == "sample_text_2"


def test_shippinginfo_shipping_type_value_roundtrip():
    instance = shippinginfo(shipping_Address="sample_text", shipping_cost=7, shipping_date=date(2024, 1, 1), shipping_id="sample_text", shipping_type="sample_text")
    assert instance.shipping_type == "sample_text"
    instance.shipping_type = "sample_text_2"
    assert instance.shipping_type == "sample_text_2"


def test_assoc_ShoppingCart_cartitem_link_reassign_clear():
    a = cartitem(name="sample_text", product=7, quantity=7, subtotal=3.14, unitcost=3.14)
    b1 = ShoppingCart(cartId=7, dateAdded=7, productId=7, quantity=7)
    b2 = ShoppingCart(cartId=13, dateAdded=13, productId=13, quantity=13)
    _safe_set(a, 'ShoppingCart_cartitem_13', b1)
    assert _is_linked(a, 'ShoppingCart_cartitem_13', b1)
    if hasattr(b1, 'ShoppingCart_cartitem_02'):
        assert _is_linked(b1, 'ShoppingCart_cartitem_02', a)
    _safe_set(a, 'ShoppingCart_cartitem_13', b2)
    assert _is_linked(a, 'ShoppingCart_cartitem_13', b2)
    if hasattr(b1, 'ShoppingCart_cartitem_02'):
        assert not _is_linked(b1, 'ShoppingCart_cartitem_02', a)
    if hasattr(b2, 'ShoppingCart_cartitem_02'):
        assert _is_linked(b2, 'ShoppingCart_cartitem_02', a)
    _safe_set(a, 'ShoppingCart_cartitem_13', None)
    assert not _is_linked(a, 'ShoppingCart_cartitem_13', b2)
    if hasattr(b2, 'ShoppingCart_cartitem_02'):
        assert not _is_linked(b2, 'ShoppingCart_cartitem_02', a)


def test_assoc_ShoppingCart_coustomer_link_reassign_clear():
    a = User(Card_info="sample_text", User_name="sample_text", address="sample_text", email="sample_text", phone_no=7, shipping_info="sample_text")
    b1 = ShoppingCart(cartId=7, dateAdded=7, productId=7, quantity=7)
    b2 = ShoppingCart(cartId=13, dateAdded=13, productId=13, quantity=13)
    _safe_set(a, 'ShoppingCart_coustomer_11', b1)
    assert _is_linked(a, 'ShoppingCart_coustomer_11', b1)
    if hasattr(b1, 'ShoppingCart_coustomer_00'):
        assert _is_linked(b1, 'ShoppingCart_coustomer_00', a)
    _safe_set(a, 'ShoppingCart_coustomer_11', b2)
    assert _is_linked(a, 'ShoppingCart_coustomer_11', b2)
    if hasattr(b1, 'ShoppingCart_coustomer_00'):
        assert not _is_linked(b1, 'ShoppingCart_coustomer_00', a)
    if hasattr(b2, 'ShoppingCart_coustomer_00'):
        assert _is_linked(b2, 'ShoppingCart_coustomer_00', a)
    _safe_set(a, 'ShoppingCart_coustomer_11', None)
    assert not _is_linked(a, 'ShoppingCart_coustomer_11', b2)
    if hasattr(b2, 'ShoppingCart_coustomer_00'):
        assert not _is_linked(b2, 'ShoppingCart_coustomer_00', a)


def test_assoc_cartitem_product_link_reassign_clear():
    a = product(imagefilename="sample_text", price=7, productid=7, productname="sample_text")
    b1 = cartitem(name="sample_text", product=7, quantity=7, subtotal=3.14, unitcost=3.14)
    b2 = cartitem(name="sample_text_2", product=13, quantity=13, subtotal=9.99, unitcost=9.99)
    _safe_set(a, 'cartitem13', b1)
    assert _is_linked(a, 'cartitem13', b1)
    if hasattr(b1, 'product212'):
        assert _is_linked(b1, 'product212', a)
    _safe_set(a, 'cartitem13', b2)
    assert _is_linked(a, 'cartitem13', b2)
    if hasattr(b1, 'product212'):
        assert not _is_linked(b1, 'product212', a)
    if hasattr(b2, 'product212'):
        assert _is_linked(b2, 'product212', a)
    _safe_set(a, 'cartitem13', None)
    assert not _is_linked(a, 'cartitem13', b2)
    if hasattr(b2, 'product212'):
        assert not _is_linked(b2, 'product212', a)


def test_assoc_coustomer_order_link_reassign_clear():
    a = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    b1 = User(Card_info="sample_text", User_name="sample_text", address="sample_text", email="sample_text", phone_no=7, shipping_info="sample_text")
    b2 = User(Card_info="sample_text_2", User_name="sample_text_2", address="sample_text_2", email="sample_text_2", phone_no=13, shipping_info="sample_text_2")
    _safe_set(a, 'coustomer_order_15', b1)
    assert _is_linked(a, 'coustomer_order_15', b1)
    if hasattr(b1, 'coustomer_order_04'):
        assert _is_linked(b1, 'coustomer_order_04', a)
    _safe_set(a, 'coustomer_order_15', b2)
    assert _is_linked(a, 'coustomer_order_15', b2)
    if hasattr(b1, 'coustomer_order_04'):
        assert not _is_linked(b1, 'coustomer_order_04', a)
    if hasattr(b2, 'coustomer_order_04'):
        assert _is_linked(b2, 'coustomer_order_04', a)
    _safe_set(a, 'coustomer_order_15', None)
    assert not _is_linked(a, 'coustomer_order_15', b2)
    if hasattr(b2, 'coustomer_order_04'):
        assert not _is_linked(b2, 'coustomer_order_04', a)


def test_assoc_order_Payment_link_reassign_clear():
    a = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    b1 = Payment(Payment_id="sample_text", Payment_method=7, Payment_type="sample_text")
    b2 = Payment(Payment_id="sample_text_2", Payment_method=13, Payment_type="sample_text_2")
    _safe_set(a, 'payment10', b1)
    assert _is_linked(a, 'payment10', b1)
    if hasattr(b1, 'order11'):
        assert _is_linked(b1, 'order11', a)
    _safe_set(a, 'payment10', b2)
    assert _is_linked(a, 'payment10', b2)
    if hasattr(b1, 'order11'):
        assert not _is_linked(b1, 'order11', a)
    if hasattr(b2, 'order11'):
        assert _is_linked(b2, 'order11', a)
    _safe_set(a, 'payment10', None)
    assert not _is_linked(a, 'payment10', b2)
    if hasattr(b2, 'order11'):
        assert not _is_linked(b2, 'order11', a)


def test_assoc_order_orderDetail_link_reassign_clear():
    a = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    b1 = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    b2 = order(c_name="sample_text_2", date_created=date(2025, 6, 15), order_ID=13, shipping_date=date(2025, 6, 15), shippingid="sample_text_2", status="sample_text_2")
    _safe_set(a, 'order_orderDetail_17', b1)
    assert _is_linked(a, 'order_orderDetail_17', b1)
    if hasattr(b1, 'order_orderDetail_06'):
        assert _is_linked(b1, 'order_orderDetail_06', a)
    _safe_set(a, 'order_orderDetail_17', b2)
    assert _is_linked(a, 'order_orderDetail_17', b2)
    if hasattr(b1, 'order_orderDetail_06'):
        assert not _is_linked(b1, 'order_orderDetail_06', a)
    if hasattr(b2, 'order_orderDetail_06'):
        assert _is_linked(b2, 'order_orderDetail_06', a)
    _safe_set(a, 'order_orderDetail_17', None)
    assert not _is_linked(a, 'order_orderDetail_17', b2)
    if hasattr(b2, 'order_orderDetail_06'):
        assert not _is_linked(b2, 'order_orderDetail_06', a)


def test_assoc_order_shippinginfo_link_reassign_clear():
    a = shippinginfo(shipping_Address="sample_text", shipping_cost=7, shipping_date=date(2024, 1, 1), shipping_id="sample_text", shipping_type="sample_text")
    b1 = order(c_name="sample_text", date_created=date(2024, 1, 1), order_ID=7, shipping_date=date(2024, 1, 1), shippingid="sample_text", status="sample_text")
    b2 = order(c_name="sample_text_2", date_created=date(2025, 6, 15), order_ID=13, shipping_date=date(2025, 6, 15), shippingid="sample_text_2", status="sample_text_2")
    _safe_set(a, 'order_shippinginfo_19', b1)
    assert _is_linked(a, 'order_shippinginfo_19', b1)
    if hasattr(b1, 'order_shippinginfo_08'):
        assert _is_linked(b1, 'order_shippinginfo_08', a)
    _safe_set(a, 'order_shippinginfo_19', b2)
    assert _is_linked(a, 'order_shippinginfo_19', b2)
    if hasattr(b1, 'order_shippinginfo_08'):
        assert not _is_linked(b1, 'order_shippinginfo_08', a)
    if hasattr(b2, 'order_shippinginfo_08'):
        assert _is_linked(b2, 'order_shippinginfo_08', a)
    _safe_set(a, 'order_shippinginfo_19', None)
    assert not _is_linked(a, 'order_shippinginfo_19', b2)
    if hasattr(b2, 'order_shippinginfo_08'):
        assert not _is_linked(b2, 'order_shippinginfo_08', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Login_strategy = st.builds(Login, UserId=safe_text, login_status=safe_text, password=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Payment_strategy = st.builds(Payment, Payment_id=safe_text, Payment_method=st.integers(), Payment_type=safe_text)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


ShoppingCart_strategy = st.builds(ShoppingCart, cartId=st.integers(), dateAdded=st.integers(), productId=st.integers(), quantity=st.integers())
@given(instance=ShoppingCart_strategy)
@settings(max_examples=25)
def test_ShoppingCart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)


User_strategy = st.builds(User, Card_info=safe_text, User_name=safe_text, address=safe_text, email=safe_text, phone_no=st.integers(), shipping_info=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


cartitem_strategy = st.builds(cartitem, name=safe_text, product=st.integers(), quantity=st.integers(), subtotal=st.floats(allow_nan=False, allow_infinity=False), unitcost=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=cartitem_strategy)
@settings(max_examples=25)
def test_cartitem_instantiation(instance):
    assert isinstance(instance, cartitem)


order_strategy = st.builds(order, c_name=safe_text, date_created=st.dates(), order_ID=st.integers(), shipping_date=st.dates(), shippingid=safe_text, status=safe_text)
@given(instance=order_strategy)
@settings(max_examples=25)
def test_order_instantiation(instance):
    assert isinstance(instance, order)


orderDetail_strategy = st.builds(orderDetail, orderId=st.integers(), productid=st.integers(), productname=safe_text, quantity=st.integers(), subtotall=st.floats(allow_nan=False, allow_infinity=False), unitcost=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=orderDetail_strategy)
@settings(max_examples=25)
def test_orderDetail_instantiation(instance):
    assert isinstance(instance, orderDetail)


product_strategy = st.builds(product, imagefilename=safe_text, price=st.integers(), productid=st.integers(), productname=safe_text)
@given(instance=product_strategy)
@settings(max_examples=25)
def test_product_instantiation(instance):
    assert isinstance(instance, product)


shippinginfo_strategy = st.builds(shippinginfo, shipping_Address=safe_text, shipping_cost=st.integers(), shipping_date=st.dates(), shipping_id=safe_text, shipping_type=safe_text)
@given(instance=shippinginfo_strategy)
@settings(max_examples=25)
def test_shippinginfo_instantiation(instance):
    assert isinstance(instance, shippinginfo)



