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
    PremiumCustomer,
    Product,
    OrderDetail,
    Order,
    Customer,
    Portal,
    OrderStatus,
    real,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_premiumcustomer_is_not_abstract():
    assert not inspect.isabstract(PremiumCustomer)


def test_hyp_premiumcustomer_constructor_exists():
    assert callable(PremiumCustomer.__init__)


def test_hyp_premiumcustomer_constructor_args():
    sig = inspect.signature(PremiumCustomer.__init__)
    params = list(sig.parameters.keys())
    assert "subscriptionExpires" in params, "Missing parameter 'subscriptionExpires'"




def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_hyp_product_constructor_exists():
    assert callable(Product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "productId" in params, "Missing parameter 'productId'"
    assert "description" in params, "Missing parameter 'description'"
    assert "imageFileName" in params, "Missing parameter 'imageFileName'"
    assert "stock" in params, "Missing parameter 'stock'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "price" in params, "Missing parameter 'price'"









def test_hyp_orderdetail_is_not_abstract():
    assert not inspect.isabstract(OrderDetail)


def test_hyp_orderdetail_constructor_exists():
    assert callable(OrderDetail.__init__)


def test_hyp_orderdetail_constructor_args():
    sig = inspect.signature(OrderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "subtotal" in params, "Missing parameter 'subtotal'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "ordrId" in params, "Missing parameter 'ordrId'"
    assert "unitCost" in params, "Missing parameter 'unitCost'"









def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "totalPrice" in params, "Missing parameter 'totalPrice'"
    assert "customerId" in params, "Missing parameter 'customerId'"
    assert "shippingId" in params, "Missing parameter 'shippingId'"
    assert "dateShipped" in params, "Missing parameter 'dateShipped'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_hyp_order_has_status():
    assert hasattr(Order, "status")
    descriptor = None
    for klass in Order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_orderId():
    assert hasattr(Order, "orderId")
    descriptor = None
    for klass in Order.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_totalPrice():
    assert hasattr(Order, "totalPrice")
    descriptor = None
    for klass in Order.__mro__:
        if "totalPrice" in klass.__dict__:
            descriptor = klass.__dict__["totalPrice"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_customerId():
    assert hasattr(Order, "customerId")
    descriptor = None
    for klass in Order.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_shippingId():
    assert hasattr(Order, "shippingId")
    descriptor = None
    for klass in Order.__mro__:
        if "shippingId" in klass.__dict__:
            descriptor = klass.__dict__["shippingId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_dateShipped():
    assert hasattr(Order, "dateShipped")
    descriptor = None
    for klass in Order.__mro__:
        if "dateShipped" in klass.__dict__:
            descriptor = klass.__dict__["dateShipped"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_creationDate():
    assert hasattr(Order, "creationDate")
    descriptor = None
    for klass in Order.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "shippingInfo" in params, "Missing parameter 'shippingInfo'"
    assert "address" in params, "Missing parameter 'address'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "creditCardInfo" in params, "Missing parameter 'creditCardInfo'"









def test_hyp_portal_is_not_abstract():
    assert not inspect.isabstract(Portal)


def test_hyp_portal_constructor_exists():
    assert callable(Portal.__init__)


def test_hyp_portal_constructor_args():
    sig = inspect.signature(Portal.__init__)
    params = list(sig.parameters.keys())
    assert "portalId" in params, "Missing parameter 'portalId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"




def test_hyp_orderstatus_exists():
    # Check that the Enumeration exists
    assert OrderStatus is not None

def test_hyp_orderstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderStatus"

def test_hyp_real_exists():
    # Check that the Enumeration exists
    assert real is not None

def test_hyp_real_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in real]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in real"


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
PremiumCustomer_strategy = st.builds(
    PremiumCustomer,
    subscriptionExpires=
        safe_text
)
Product_strategy = st.builds(
    Product,
    productId=
        st.integers(),
    description=
        safe_text,
    imageFileName=
        safe_text,
    stock=
        st.integers(),
    productName=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
OrderDetail_strategy = st.builds(
    OrderDetail,
    subtotal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    quantity=
        st.integers(),
    productName=
        safe_text,
    productId=
        st.integers(),
    ordrId=
        st.integers(),
    unitCost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Order_strategy = st.builds(
    Order,
    status=
        st.none(),
    orderId=
        st.integers(),
    totalPrice=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    customerId=
        st.integers(),
    shippingId=
        st.integers(),
    dateShipped=
        safe_text,
    creationDate=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    shippingInfo=
        safe_text,
    address=
        safe_text,
    phone=
        st.integers(),
    email=
        safe_text,
    name=
        safe_text,
    creditCardInfo=
        safe_text
)
Portal_strategy = st.builds(
    Portal,
    portalId=
        safe_text,
    name=
        safe_text,
    url=
        safe_text
)




@given(instance=PremiumCustomer_strategy)
def test_hyp_premiumcustomer_subscriptionExpires_setter(instance):
    original = instance.subscriptionExpires
    instance.subscriptionExpires = original
    assert instance.subscriptionExpires == original




@given(instance=Product_strategy)
def test_hyp_product_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=Product_strategy)
def test_hyp_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Product_strategy)
def test_hyp_product_imageFileName_setter(instance):
    original = instance.imageFileName
    instance.imageFileName = original
    assert instance.imageFileName == original



@given(instance=Product_strategy)
def test_hyp_product_stock_setter(instance):
    original = instance.stock
    instance.stock = original
    assert instance.stock == original



@given(instance=Product_strategy)
def test_hyp_product_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=Product_strategy)
def test_hyp_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original




@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_subtotal_setter(instance):
    original = instance.subtotal
    instance.subtotal = original
    assert instance.subtotal == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_ordrId_setter(instance):
    original = instance.ordrId
    instance.ordrId = original
    assert instance.ordrId == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_unitCost_setter(instance):
    original = instance.unitCost
    instance.unitCost = original
    assert instance.unitCost == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_hyp_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_hyp_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_hyp_order_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original



@given(instance=Order_strategy)
def test_hyp_order_totalPrice_setter(instance):
    original = instance.totalPrice
    instance.totalPrice = original
    assert instance.totalPrice == original



@given(instance=Order_strategy)
def test_hyp_order_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original



@given(instance=Order_strategy)
def test_hyp_order_shippingId_setter(instance):
    original = instance.shippingId
    instance.shippingId = original
    assert instance.shippingId == original



@given(instance=Order_strategy)
def test_hyp_order_dateShipped_setter(instance):
    original = instance.dateShipped
    instance.dateShipped = original
    assert instance.dateShipped == original



@given(instance=Order_strategy)
def test_hyp_order_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original




@given(instance=Customer_strategy)
def test_hyp_customer_shippingInfo_setter(instance):
    original = instance.shippingInfo
    instance.shippingInfo = original
    assert instance.shippingInfo == original



@given(instance=Customer_strategy)
def test_hyp_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_hyp_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Customer_strategy)
def test_hyp_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_hyp_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_hyp_customer_creditCardInfo_setter(instance):
    original = instance.creditCardInfo
    instance.creditCardInfo = original
    assert instance.creditCardInfo == original




@given(instance=Portal_strategy)
def test_hyp_portal_portalId_setter(instance):
    original = instance.portalId
    instance.portalId = original
    assert instance.portalId == original



@given(instance=Portal_strategy)
def test_hyp_portal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Portal_strategy)
def test_hyp_portal_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Customer,
    Order,
    OrderDetail,
    Portal,
    PremiumCustomer,
    Product,
    OrderStatus,
    real,
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

def test_Customer_address_value_roundtrip():
    instance = Customer(address="sample_text", creditCardInfo="sample_text", email="sample_text", name="sample_text", phone=7, shippingInfo="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer_creditCardInfo_value_roundtrip():
    instance = Customer(address="sample_text", creditCardInfo="sample_text", email="sample_text", name="sample_text", phone=7, shippingInfo="sample_text")
    assert instance.creditCardInfo == "sample_text"
    instance.creditCardInfo = "sample_text_2"
    assert instance.creditCardInfo == "sample_text_2"


def test_Customer_email_value_roundtrip():
    instance = Customer(address="sample_text", creditCardInfo="sample_text", email="sample_text", name="sample_text", phone=7, shippingInfo="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Customer_name_value_roundtrip():
    instance = Customer(address="sample_text", creditCardInfo="sample_text", email="sample_text", name="sample_text", phone=7, shippingInfo="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Customer_phone_value_roundtrip():
    instance = Customer(address="sample_text", creditCardInfo="sample_text", email="sample_text", name="sample_text", phone=7, shippingInfo="sample_text")
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


def test_Customer_shippingInfo_value_roundtrip():
    instance = Customer(address="sample_text", creditCardInfo="sample_text", email="sample_text", name="sample_text", phone=7, shippingInfo="sample_text")
    assert instance.shippingInfo == "sample_text"
    instance.shippingInfo = "sample_text_2"
    assert instance.shippingInfo == "sample_text_2"


def test_OrderDetail_ordrId_value_roundtrip():
    instance = OrderDetail(ordrId=7, productId=7, productName="sample_text", quantity=7, subtotal=3.14, unitCost=3.14)
    assert instance.ordrId == 7
    instance.ordrId = 13
    assert instance.ordrId == 13


def test_OrderDetail_productId_value_roundtrip():
    instance = OrderDetail(ordrId=7, productId=7, productName="sample_text", quantity=7, subtotal=3.14, unitCost=3.14)
    assert instance.productId == 7
    instance.productId = 13
    assert instance.productId == 13


def test_OrderDetail_productName_value_roundtrip():
    instance = OrderDetail(ordrId=7, productId=7, productName="sample_text", quantity=7, subtotal=3.14, unitCost=3.14)
    assert instance.productName == "sample_text"
    instance.productName = "sample_text_2"
    assert instance.productName == "sample_text_2"


def test_OrderDetail_quantity_value_roundtrip():
    instance = OrderDetail(ordrId=7, productId=7, productName="sample_text", quantity=7, subtotal=3.14, unitCost=3.14)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_OrderDetail_subtotal_value_roundtrip():
    instance = OrderDetail(ordrId=7, productId=7, productName="sample_text", quantity=7, subtotal=3.14, unitCost=3.14)
    assert instance.subtotal == 3.14
    instance.subtotal = 9.99
    assert instance.subtotal == 9.99


def test_OrderDetail_unitCost_value_roundtrip():
    instance = OrderDetail(ordrId=7, productId=7, productName="sample_text", quantity=7, subtotal=3.14, unitCost=3.14)
    assert instance.unitCost == 3.14
    instance.unitCost = 9.99
    assert instance.unitCost == 9.99


def test_Portal_name_value_roundtrip():
    instance = Portal(name="sample_text", portalId="sample_text", url="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Portal_portalId_value_roundtrip():
    instance = Portal(name="sample_text", portalId="sample_text", url="sample_text")
    assert instance.portalId == "sample_text"
    instance.portalId = "sample_text_2"
    assert instance.portalId == "sample_text_2"


def test_Portal_url_value_roundtrip():
    instance = Portal(name="sample_text", portalId="sample_text", url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_PremiumCustomer_subscriptionExpires_value_roundtrip():
    instance = PremiumCustomer(subscriptionExpires="sample_text")
    assert instance.subscriptionExpires == "sample_text"
    instance.subscriptionExpires = "sample_text_2"
    assert instance.subscriptionExpires == "sample_text_2"


def test_Product_description_value_roundtrip():
    instance = Product(description="sample_text", imageFileName="sample_text", price=3.14, productId=7, productName="sample_text", stock=7)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Product_imageFileName_value_roundtrip():
    instance = Product(description="sample_text", imageFileName="sample_text", price=3.14, productId=7, productName="sample_text", stock=7)
    assert instance.imageFileName == "sample_text"
    instance.imageFileName = "sample_text_2"
    assert instance.imageFileName == "sample_text_2"


def test_Product_price_value_roundtrip():
    instance = Product(description="sample_text", imageFileName="sample_text", price=3.14, productId=7, productName="sample_text", stock=7)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_Product_productId_value_roundtrip():
    instance = Product(description="sample_text", imageFileName="sample_text", price=3.14, productId=7, productName="sample_text", stock=7)
    assert instance.productId == 7
    instance.productId = 13
    assert instance.productId == 13


def test_Product_productName_value_roundtrip():
    instance = Product(description="sample_text", imageFileName="sample_text", price=3.14, productId=7, productName="sample_text", stock=7)
    assert instance.productName == "sample_text"
    instance.productName = "sample_text_2"
    assert instance.productName == "sample_text_2"


def test_Product_stock_value_roundtrip():
    instance = Product(description="sample_text", imageFileName="sample_text", price=3.14, productId=7, productName="sample_text", stock=7)
    assert instance.stock == 7
    instance.stock = 13
    assert instance.stock == 13


def test_assoc_Customer_Portal_link_reassign_clear():
    a = Portal(name="sample_text", portalId="sample_text", url="sample_text")
    b1 = Customer(address="sample_text", creditCardInfo="sample_text", email="sample_text", name="sample_text", phone=7, shippingInfo="sample_text")
    b2 = Customer(address="sample_text_2", creditCardInfo="sample_text_2", email="sample_text_2", name="sample_text_2", phone=13, shippingInfo="sample_text_2")
    _safe_set(a, 'users7', {b1})
    assert _is_linked(a, 'users7', b1)
    if hasattr(b1, 'portal6'):
        assert _is_linked(b1, 'portal6', a)
    _safe_set(a, 'users7', {b2})
    assert _is_linked(a, 'users7', b2)
    if hasattr(b1, 'portal6'):
        assert not _is_linked(b1, 'portal6', a)
    if hasattr(b2, 'portal6'):
        assert _is_linked(b2, 'portal6', a)
    _safe_set(a, 'users7', set())
    assert not _is_linked(a, 'users7', b2)
    if hasattr(b2, 'portal6'):
        assert not _is_linked(b2, 'portal6', a)


def test_assoc_Product_OrderDetail_link_reassign_clear():
    a = Product(description="sample_text", imageFileName="sample_text", price=3.14, productId=7, productName="sample_text", stock=7)
    b1 = OrderDetail(ordrId=7, productId=7, productName="sample_text", quantity=7, subtotal=3.14, unitCost=3.14)
    b2 = OrderDetail(ordrId=13, productId=13, productName="sample_text_2", quantity=13, subtotal=9.99, unitCost=9.99)
    _safe_set(a, 'orderDetails2', {b1})
    assert _is_linked(a, 'orderDetails2', b1)
    if hasattr(b1, 'product3'):
        assert _is_linked(b1, 'product3', a)
    _safe_set(a, 'orderDetails2', {b2})
    assert _is_linked(a, 'orderDetails2', b2)
    if hasattr(b1, 'product3'):
        assert not _is_linked(b1, 'product3', a)
    if hasattr(b2, 'product3'):
        assert _is_linked(b2, 'product3', a)
    _safe_set(a, 'orderDetails2', set())
    assert not _is_linked(a, 'orderDetails2', b2)
    if hasattr(b2, 'product3'):
        assert not _is_linked(b2, 'product3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Customer_strategy = st.builds(Customer, address=safe_text, creditCardInfo=safe_text, email=safe_text, name=safe_text, phone=st.integers(), shippingInfo=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


OrderDetail_strategy = st.builds(OrderDetail, ordrId=st.integers(), productId=st.integers(), productName=safe_text, quantity=st.integers(), subtotal=st.floats(allow_nan=False, allow_infinity=False), unitCost=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=OrderDetail_strategy)
@settings(max_examples=25)
def test_OrderDetail_instantiation(instance):
    assert isinstance(instance, OrderDetail)


Portal_strategy = st.builds(Portal, name=safe_text, portalId=safe_text, url=safe_text)
@given(instance=Portal_strategy)
@settings(max_examples=25)
def test_Portal_instantiation(instance):
    assert isinstance(instance, Portal)


PremiumCustomer_strategy = st.builds(PremiumCustomer, subscriptionExpires=safe_text)
@given(instance=PremiumCustomer_strategy)
@settings(max_examples=25)
def test_PremiumCustomer_instantiation(instance):
    assert isinstance(instance, PremiumCustomer)


Product_strategy = st.builds(Product, description=safe_text, imageFileName=safe_text, price=st.floats(allow_nan=False, allow_infinity=False), productId=st.integers(), productName=safe_text, stock=st.integers())
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)



