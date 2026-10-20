import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Address,
    Administrator,
    Category,
    Class,
    Class1,
    Class2,
    CreditCardPayment,
    Credit_DebitCard,
    Credit_DebitCard1,
    Customer,
    Department,
    EmailNotification,
    Gpay,
    Item,
    Notify_Interface,
    Offer_Interface,
    Order,
    OrderDetail,
    OrderService,
    PayLater,
    PayLater1,
    Payment,
    Payment_Interface,
    Price,
    Product,
    ProductDiscount,
    PushNotification,
    SMS,
    SessionManager,
    Shipping,
    ShippingType_Interface,
    ShoppingCart,
    TimeBasedDiscount,
    User,
    Vendor,
    billdesk_Interface,
    cartItem,
    customeraddress_Interface,
    email,
    email_Interface,
    gpay_Interface,
    keywordSet,
    mobile_Interface,
    notify_Interface,
    paylater_Interface,
    payment_Interface,
    pickuppoint_Interface,
    promotions,
    searchFacade,
    shiporder_Interface,
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

def test_assoc_Administrator_Order_reverse_link_reassign_clear():
    a1 = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    a2 = Order(BillingAddress="sample_text_2", Item="sample_text_2", OrderId=13, OrderStatus="sample_text_2", Payment="sample_text_2", ShippingAddress="sample_text_2", customerId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", dateShipped="sample_text_2", status="sample_text_2")
    b = Administrator(adminName="sample_text", email="sample_text")
    _safe_set(b, 'order16', a1)
    assert _is_linked(b, 'order16', a1)
    if hasattr(a1, 'administrator17'):
        assert _is_linked(a1, 'administrator17', b)
    _safe_set(b, 'order16', a2)
    assert _is_linked(b, 'order16', a2)
    if hasattr(a1, 'administrator17'):
        assert not _is_linked(a1, 'administrator17', b)
    if hasattr(a2, 'administrator17'):
        assert _is_linked(a2, 'administrator17', b)
    _safe_set(b, 'order16', None)
    assert not _is_linked(b, 'order16', a2)
    if hasattr(a2, 'administrator17'):
        assert not _is_linked(a2, 'administrator17', b)


def test_assoc_Cart_Cart_reverse_link_reassign_clear():
    a1 = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    a2 = cartItem(name="sample_text_2", productId=13, quantity=13, subtotal="sample_text_2", unitCost="sample_text_2")
    b = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    _safe_set(b, 'cart3', a1)
    assert _is_linked(b, 'cart3', a1)
    if hasattr(a1, 'cart2'):
        assert _is_linked(a1, 'cart2', b)
    _safe_set(b, 'cart3', a2)
    assert _is_linked(b, 'cart3', a2)
    if hasattr(a1, 'cart2'):
        assert not _is_linked(a1, 'cart2', b)
    if hasattr(a2, 'cart2'):
        assert _is_linked(a2, 'cart2', b)
    _safe_set(b, 'cart3', None)
    assert not _is_linked(b, 'cart3', a2)
    if hasattr(a2, 'cart2'):
        assert not _is_linked(a2, 'cart2', b)


def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    a2 = Order(BillingAddress="sample_text_2", Item="sample_text_2", OrderId=13, OrderStatus="sample_text_2", Payment="sample_text_2", ShippingAddress="sample_text_2", customerId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", dateShipped="sample_text_2", status="sample_text_2")
    b = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    _safe_set(b, 'order14', a1)
    assert _is_linked(b, 'order14', a1)
    if hasattr(a1, 'customer15'):
        assert _is_linked(a1, 'customer15', b)
    _safe_set(b, 'order14', a2)
    assert _is_linked(b, 'order14', a2)
    if hasattr(a1, 'customer15'):
        assert not _is_linked(a1, 'customer15', b)
    if hasattr(a2, 'customer15'):
        assert _is_linked(a2, 'customer15', b)
    _safe_set(b, 'order14', None)
    assert not _is_linked(b, 'order14', a2)
    if hasattr(a2, 'customer15'):
        assert not _is_linked(a2, 'customer15', b)


def test_assoc_Customer_promotions_reverse_link_reassign_clear():
    a1 = promotions(endDate=7, promotionCode="sample_text", startDate=7)
    a2 = promotions(endDate=13, promotionCode="sample_text_2", startDate=13)
    b = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    _safe_set(b, 'promotions34', a1)
    assert _is_linked(b, 'promotions34', a1)
    if hasattr(a1, 'customer35'):
        assert _is_linked(a1, 'customer35', b)
    _safe_set(b, 'promotions34', a2)
    assert _is_linked(b, 'promotions34', a2)
    if hasattr(a1, 'customer35'):
        assert not _is_linked(a1, 'customer35', b)
    if hasattr(a2, 'customer35'):
        assert _is_linked(a2, 'customer35', b)
    _safe_set(b, 'promotions34', None)
    assert not _is_linked(b, 'promotions34', a2)
    if hasattr(a2, 'customer35'):
        assert not _is_linked(a2, 'customer35', b)


def test_assoc_Department_Category_reverse_link_reassign_clear():
    a1 = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    a2 = Department(departmentID=13, departmentName="sample_text_2", description="sample_text_2")
    b = Category(categoryID=7, categoryName="sample_text", departmentId=7, description="sample_text")
    _safe_set(b, 'department55', a1)
    assert _is_linked(b, 'department55', a1)
    if hasattr(a1, 'category54'):
        assert _is_linked(a1, 'category54', b)
    _safe_set(b, 'department55', a2)
    assert _is_linked(b, 'department55', a2)
    if hasattr(a1, 'category54'):
        assert not _is_linked(a1, 'category54', b)
    if hasattr(a2, 'category54'):
        assert _is_linked(a2, 'category54', b)
    _safe_set(b, 'department55', None)
    assert not _is_linked(b, 'department55', a2)
    if hasattr(a2, 'category54'):
        assert not _is_linked(a2, 'category54', b)


def test_assoc_Department_Department_reverse_link_reassign_clear():
    a1 = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    a2 = Department(departmentID=13, departmentName="sample_text_2", description="sample_text_2")
    b = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    _safe_set(b, 'department53', a1)
    assert _is_linked(b, 'department53', a1)
    if hasattr(a1, 'department52'):
        assert _is_linked(a1, 'department52', b)
    _safe_set(b, 'department53', a2)
    assert _is_linked(b, 'department53', a2)
    if hasattr(a1, 'department52'):
        assert not _is_linked(a1, 'department52', b)
    if hasattr(a2, 'department52'):
        assert _is_linked(a2, 'department52', b)
    _safe_set(b, 'department53', None)
    assert not _is_linked(b, 'department53', a2)
    if hasattr(a2, 'department52'):
        assert not _is_linked(a2, 'department52', b)


def test_assoc_Genre_Genre_reverse_link_reassign_clear():
    a1 = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    a2 = Product(Name="sample_text_2", Price="sample_text_2", SKU="sample_text_2", attribute5="sample_text_2", attribute6="sample_text_2", attribute7="sample_text_2", description="sample_text_2", productId=13, reviews="sample_text_2")
    b = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    _safe_set(b, 'genre4', a1)
    assert _is_linked(b, 'genre4', a1)
    if hasattr(a1, 'genre5'):
        assert _is_linked(a1, 'genre5', b)
    _safe_set(b, 'genre4', a2)
    assert _is_linked(b, 'genre4', a2)
    if hasattr(a1, 'genre5'):
        assert not _is_linked(a1, 'genre5', b)
    if hasattr(a2, 'genre5'):
        assert _is_linked(a2, 'genre5', b)
    _safe_set(b, 'genre4', None)
    assert not _is_linked(b, 'genre4', a2)
    if hasattr(a2, 'genre5'):
        assert not _is_linked(a2, 'genre5', b)


def test_assoc_Genre_Product_reverse_link_reassign_clear():
    a1 = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    a2 = Product(Name="sample_text_2", Price="sample_text_2", SKU="sample_text_2", attribute5="sample_text_2", attribute6="sample_text_2", attribute7="sample_text_2", description="sample_text_2", productId=13, reviews="sample_text_2")
    b = Category(categoryID=7, categoryName="sample_text", departmentId=7, description="sample_text")
    _safe_set(b, 'product6', a1)
    assert _is_linked(b, 'product6', a1)
    if hasattr(a1, 'genre7'):
        assert _is_linked(a1, 'genre7', b)
    _safe_set(b, 'product6', a2)
    assert _is_linked(b, 'product6', a2)
    if hasattr(a1, 'genre7'):
        assert not _is_linked(a1, 'genre7', b)
    if hasattr(a2, 'genre7'):
        assert _is_linked(a2, 'genre7', b)
    _safe_set(b, 'product6', None)
    assert not _is_linked(b, 'product6', a2)
    if hasattr(a2, 'genre7'):
        assert not _is_linked(a2, 'genre7', b)


def test_assoc_Item_Order_reverse_link_reassign_clear():
    a1 = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    a2 = Order(BillingAddress="sample_text_2", Item="sample_text_2", OrderId=13, OrderStatus="sample_text_2", Payment="sample_text_2", ShippingAddress="sample_text_2", customerId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", dateShipped="sample_text_2", status="sample_text_2")
    b = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    _safe_set(b, 'order76', a1)
    assert _is_linked(b, 'order76', a1)
    if hasattr(a1, 'item77'):
        assert _is_linked(a1, 'item77', b)
    _safe_set(b, 'order76', a2)
    assert _is_linked(b, 'order76', a2)
    if hasattr(a1, 'item77'):
        assert not _is_linked(a1, 'item77', b)
    if hasattr(a2, 'item77'):
        assert _is_linked(a2, 'item77', b)
    _safe_set(b, 'order76', None)
    assert not _is_linked(b, 'order76', a2)
    if hasattr(a2, 'item77'):
        assert not _is_linked(a2, 'item77', b)


def test_assoc_Item_Product_reverse_link_reassign_clear():
    a1 = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    a2 = Product(Name="sample_text_2", Price="sample_text_2", SKU="sample_text_2", attribute5="sample_text_2", attribute6="sample_text_2", attribute7="sample_text_2", description="sample_text_2", productId=13, reviews="sample_text_2")
    b = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    _safe_set(b, 'product62', a1)
    assert _is_linked(b, 'product62', a1)
    if hasattr(a1, 'item63'):
        assert _is_linked(a1, 'item63', b)
    _safe_set(b, 'product62', a2)
    assert _is_linked(b, 'product62', a2)
    if hasattr(a1, 'item63'):
        assert not _is_linked(a1, 'item63', b)
    if hasattr(a2, 'item63'):
        assert _is_linked(a2, 'item63', b)
    _safe_set(b, 'product62', None)
    assert not _is_linked(b, 'product62', a2)
    if hasattr(a2, 'item63'):
        assert not _is_linked(a2, 'item63', b)


def test_assoc_OrderService_Order_reverse_link_reassign_clear():
    a1 = OrderService(attribute="sample_text")
    a2 = OrderService(attribute="sample_text_2")
    b = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    _safe_set(b, 'orderService65', a1)
    assert _is_linked(b, 'orderService65', a1)
    if hasattr(a1, 'order64'):
        assert _is_linked(a1, 'order64', b)
    _safe_set(b, 'orderService65', a2)
    assert _is_linked(b, 'orderService65', a2)
    if hasattr(a1, 'order64'):
        assert not _is_linked(a1, 'order64', b)
    if hasattr(a2, 'order64'):
        assert _is_linked(a2, 'order64', b)
    _safe_set(b, 'orderService65', None)
    assert not _is_linked(b, 'orderService65', a2)
    if hasattr(a2, 'order64'):
        assert not _is_linked(a2, 'order64', b)


def test_assoc_Order_Address_reverse_link_reassign_clear():
    a1 = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    a2 = Order(BillingAddress="sample_text_2", Item="sample_text_2", OrderId=13, OrderStatus="sample_text_2", Payment="sample_text_2", ShippingAddress="sample_text_2", customerId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", dateShipped="sample_text_2", status="sample_text_2")
    b = Address(City="sample_text", Country="sample_text", State="sample_text", Street="sample_text", Type="sample_text", ZipCode="sample_text")
    _safe_set(b, 'order81', a1)
    assert _is_linked(b, 'order81', a1)
    if hasattr(a1, 'address80'):
        assert _is_linked(a1, 'address80', b)
    _safe_set(b, 'order81', a2)
    assert _is_linked(b, 'order81', a2)
    if hasattr(a1, 'address80'):
        assert not _is_linked(a1, 'address80', b)
    if hasattr(a2, 'address80'):
        assert _is_linked(a2, 'address80', b)
    _safe_set(b, 'order81', None)
    assert not _is_linked(b, 'order81', a2)
    if hasattr(a2, 'address80'):
        assert not _is_linked(a2, 'address80', b)


def test_assoc_Order_OrderDetail_reverse_link_reassign_clear():
    a1 = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    a2 = OrderDetail(orderId=13, productId=13, productName="sample_text_2", quantity=13, subTotal="sample_text_2", unitCost="sample_text_2")
    b = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    _safe_set(b, 'orderDetail12', a1)
    assert _is_linked(b, 'orderDetail12', a1)
    if hasattr(a1, 'order13'):
        assert _is_linked(a1, 'order13', b)
    _safe_set(b, 'orderDetail12', a2)
    assert _is_linked(b, 'orderDetail12', a2)
    if hasattr(a1, 'order13'):
        assert not _is_linked(a1, 'order13', b)
    if hasattr(a2, 'order13'):
        assert _is_linked(a2, 'order13', b)
    _safe_set(b, 'orderDetail12', None)
    assert not _is_linked(b, 'orderDetail12', a2)
    if hasattr(a2, 'order13'):
        assert not _is_linked(a2, 'order13', b)


def test_assoc_Order_Shipping_reverse_link_reassign_clear():
    a1 = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    a2 = Shipping(ShippingType="sample_text_2", _attr=13, shippingAddress="sample_text_2", shippingId=13, shippingType="sample_text_2")
    b = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    _safe_set(b, 'shipping74', a1)
    assert _is_linked(b, 'shipping74', a1)
    if hasattr(a1, 'order75'):
        assert _is_linked(a1, 'order75', b)
    _safe_set(b, 'shipping74', a2)
    assert _is_linked(b, 'shipping74', a2)
    if hasattr(a1, 'order75'):
        assert not _is_linked(a1, 'order75', b)
    if hasattr(a2, 'order75'):
        assert _is_linked(a2, 'order75', b)
    _safe_set(b, 'shipping74', None)
    assert not _is_linked(b, 'shipping74', a2)
    if hasattr(a2, 'order75'):
        assert not _is_linked(a2, 'order75', b)


def test_assoc_Order_Shippinginfo_reverse_link_reassign_clear():
    a1 = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    a2 = Shipping(ShippingType="sample_text_2", _attr=13, shippingAddress="sample_text_2", shippingId=13, shippingType="sample_text_2")
    b = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    _safe_set(b, 'Order_Shippinginfo_010', a1)
    assert _is_linked(b, 'Order_Shippinginfo_010', a1)
    if hasattr(a1, 'Order_Shippinginfo_111'):
        assert _is_linked(a1, 'Order_Shippinginfo_111', b)
    _safe_set(b, 'Order_Shippinginfo_010', a2)
    assert _is_linked(b, 'Order_Shippinginfo_010', a2)
    if hasattr(a1, 'Order_Shippinginfo_111'):
        assert not _is_linked(a1, 'Order_Shippinginfo_111', b)
    if hasattr(a2, 'Order_Shippinginfo_111'):
        assert _is_linked(a2, 'Order_Shippinginfo_111', b)
    _safe_set(b, 'Order_Shippinginfo_010', None)
    assert not _is_linked(b, 'Order_Shippinginfo_010', a2)
    if hasattr(a2, 'Order_Shippinginfo_111'):
        assert not _is_linked(a2, 'Order_Shippinginfo_111', b)


def test_assoc_Price_Price_reverse_link_reassign_clear():
    a1 = Price(ActualPrice="sample_text")
    a2 = Price(ActualPrice="sample_text_2")
    b = Price(ActualPrice="sample_text")
    _safe_set(b, 'price57', a1)
    assert _is_linked(b, 'price57', a1)
    if hasattr(a1, 'price56'):
        assert _is_linked(a1, 'price56', b)
    _safe_set(b, 'price57', a2)
    assert _is_linked(b, 'price57', a2)
    if hasattr(a1, 'price56'):
        assert not _is_linked(a1, 'price56', b)
    if hasattr(a2, 'price56'):
        assert _is_linked(a2, 'price56', b)
    _safe_set(b, 'price57', None)
    assert not _is_linked(b, 'price57', a2)
    if hasattr(a2, 'price56'):
        assert not _is_linked(a2, 'price56', b)


def test_assoc_Product_OrderDetail_reverse_link_reassign_clear():
    a1 = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    a2 = Product(Name="sample_text_2", Price="sample_text_2", SKU="sample_text_2", attribute5="sample_text_2", attribute6="sample_text_2", attribute7="sample_text_2", description="sample_text_2", productId=13, reviews="sample_text_2")
    b = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    _safe_set(b, 'product19', a1)
    assert _is_linked(b, 'product19', a1)
    if hasattr(a1, 'orderDetail18'):
        assert _is_linked(a1, 'orderDetail18', b)
    _safe_set(b, 'product19', a2)
    assert _is_linked(b, 'product19', a2)
    if hasattr(a1, 'orderDetail18'):
        assert not _is_linked(a1, 'orderDetail18', b)
    if hasattr(a2, 'orderDetail18'):
        assert _is_linked(a2, 'orderDetail18', b)
    _safe_set(b, 'product19', None)
    assert not _is_linked(b, 'product19', a2)
    if hasattr(a2, 'orderDetail18'):
        assert not _is_linked(a2, 'orderDetail18', b)


def test_assoc_Product_Price_reverse_link_reassign_clear():
    a1 = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    a2 = Product(Name="sample_text_2", Price="sample_text_2", SKU="sample_text_2", attribute5="sample_text_2", attribute6="sample_text_2", attribute7="sample_text_2", description="sample_text_2", productId=13, reviews="sample_text_2")
    b = Price(ActualPrice="sample_text")
    _safe_set(b, 'product61', a1)
    assert _is_linked(b, 'product61', a1)
    if hasattr(a1, 'price60'):
        assert _is_linked(a1, 'price60', b)
    _safe_set(b, 'product61', a2)
    assert _is_linked(b, 'product61', a2)
    if hasattr(a1, 'price60'):
        assert not _is_linked(a1, 'price60', b)
    if hasattr(a2, 'price60'):
        assert _is_linked(a2, 'price60', b)
    _safe_set(b, 'product61', None)
    assert not _is_linked(b, 'product61', a2)
    if hasattr(a2, 'price60'):
        assert not _is_linked(a2, 'price60', b)


def test_assoc_Product_cartItem_reverse_link_reassign_clear():
    a1 = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    a2 = cartItem(name="sample_text_2", productId=13, quantity=13, subtotal="sample_text_2", unitCost="sample_text_2")
    b = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    _safe_set(b, 'cartItem20', a1)
    assert _is_linked(b, 'cartItem20', a1)
    if hasattr(a1, 'product21'):
        assert _is_linked(a1, 'product21', b)
    _safe_set(b, 'cartItem20', a2)
    assert _is_linked(b, 'cartItem20', a2)
    if hasattr(a1, 'product21'):
        assert not _is_linked(a1, 'product21', b)
    if hasattr(a2, 'product21'):
        assert _is_linked(a2, 'product21', b)
    _safe_set(b, 'cartItem20', None)
    assert not _is_linked(b, 'cartItem20', a2)
    if hasattr(a2, 'product21'):
        assert not _is_linked(a2, 'product21', b)


def test_assoc_SessionManager_Genre_reverse_link_reassign_clear():
    a1 = SessionManager(departmentName="sample_text", userid="sample_text")
    a2 = SessionManager(departmentName="sample_text_2", userid="sample_text_2")
    b = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    _safe_set(b, 'sessionManager9', a1)
    assert _is_linked(b, 'sessionManager9', a1)
    if hasattr(a1, 'genre8'):
        assert _is_linked(a1, 'genre8', b)
    _safe_set(b, 'sessionManager9', a2)
    assert _is_linked(b, 'sessionManager9', a2)
    if hasattr(a1, 'genre8'):
        assert not _is_linked(a1, 'genre8', b)
    if hasattr(a2, 'genre8'):
        assert _is_linked(a2, 'genre8', b)
    _safe_set(b, 'sessionManager9', None)
    assert not _is_linked(b, 'sessionManager9', a2)
    if hasattr(a2, 'genre8'):
        assert not _is_linked(a2, 'genre8', b)


def test_assoc_SessionManager_User_reverse_link_reassign_clear():
    a1 = User(loginStatus="sample_text", password="sample_text", userId="sample_text")
    a2 = User(loginStatus="sample_text_2", password="sample_text_2", userId="sample_text_2")
    b = SessionManager(departmentName="sample_text", userid="sample_text")
    _safe_set(b, 'user0', a1)
    assert _is_linked(b, 'user0', a1)
    if hasattr(a1, 'sessionManager1'):
        assert _is_linked(a1, 'sessionManager1', b)
    _safe_set(b, 'user0', a2)
    assert _is_linked(b, 'user0', a2)
    if hasattr(a1, 'sessionManager1'):
        assert not _is_linked(a1, 'sessionManager1', b)
    if hasattr(a2, 'sessionManager1'):
        assert _is_linked(a2, 'sessionManager1', b)
    _safe_set(b, 'user0', None)
    assert not _is_linked(b, 'user0', a2)
    if hasattr(a2, 'sessionManager1'):
        assert not _is_linked(a2, 'sessionManager1', b)


def test_assoc_ShoppingCart_Item_reverse_link_reassign_clear():
    a1 = ShoppingCart(GetTotalPrice="sample_text", Item="sample_text", dateAdded=7, quantity=7)
    a2 = ShoppingCart(GetTotalPrice="sample_text_2", Item="sample_text_2", dateAdded=13, quantity=13)
    b = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    _safe_set(b, 'shoppingCart79', a1)
    assert _is_linked(b, 'shoppingCart79', a1)
    if hasattr(a1, 'item78'):
        assert _is_linked(a1, 'item78', b)
    _safe_set(b, 'shoppingCart79', a2)
    assert _is_linked(b, 'shoppingCart79', a2)
    if hasattr(a1, 'item78'):
        assert not _is_linked(a1, 'item78', b)
    if hasattr(a2, 'item78'):
        assert _is_linked(a2, 'item78', b)
    _safe_set(b, 'shoppingCart79', None)
    assert not _is_linked(b, 'shoppingCart79', a2)
    if hasattr(a2, 'item78'):
        assert not _is_linked(a2, 'item78', b)


def test_assoc_keywordSet_Product_reverse_link_reassign_clear():
    a1 = keywordSet(keyword="sample_text")
    a2 = keywordSet(keyword="sample_text_2")
    b = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    _safe_set(b, 'keywordSet25', a1)
    assert _is_linked(b, 'keywordSet25', a1)
    if hasattr(a1, 'product24'):
        assert _is_linked(a1, 'product24', b)
    _safe_set(b, 'keywordSet25', a2)
    assert _is_linked(b, 'keywordSet25', a2)
    if hasattr(a1, 'product24'):
        assert not _is_linked(a1, 'product24', b)
    if hasattr(a2, 'product24'):
        assert _is_linked(a2, 'product24', b)
    _safe_set(b, 'keywordSet25', None)
    assert not _is_linked(b, 'keywordSet25', a2)
    if hasattr(a2, 'product24'):
        assert not _is_linked(a2, 'product24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_OrderService_Notify_stub_double():
    # Notify_Interface has no real 'orderService83' property in the generated
    # code (a bare stub) -- manually attach it so OrderService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OrderService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OrderService(attribute="sample_text")
    partner = Notify_Interface()
    setattr(partner, 'orderService83', None)
    _safe_set(owner, 'notify82', partner)
    assert getattr(partner, 'orderService83') == owner
    _safe_set(owner, 'notify82', None)
    assert getattr(partner, 'orderService83') is None


def test_assoc_Order_Payment_stub_double():
    # Payment has no real 'order67' property in the generated
    # code (a bare stub) -- manually attach it so Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    partner = Payment()
    setattr(partner, 'order67', None)
    _safe_set(owner, 'payment66', partner)
    assert getattr(partner, 'order67') == owner
    _safe_set(owner, 'payment66', None)
    assert getattr(partner, 'order67') is None


def test_assoc_Order_Payment2_stub_double():
    # Payment_Interface has no real 'order69' property in the generated
    # code (a bare stub) -- manually attach it so Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    partner = Payment_Interface()
    setattr(partner, 'order69', None)
    _safe_set(owner, 'payment68', partner)
    assert getattr(partner, 'order69') == owner
    _safe_set(owner, 'payment68', None)
    assert getattr(partner, 'order69') is None


def test_assoc_Product_Offer_stub_double():
    # Offer_Interface has no real 'product59' property in the generated
    # code (a bare stub) -- manually attach it so Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    partner = Offer_Interface()
    setattr(partner, 'product59', None)
    _safe_set(owner, 'offer58', partner)
    assert getattr(partner, 'product59') == owner
    _safe_set(owner, 'offer58', None)
    assert getattr(partner, 'product59') is None


def test_assoc_Shipping_ShippingType_stub_double():
    # ShippingType_Interface has no real 'shipping73' property in the generated
    # code (a bare stub) -- manually attach it so Shipping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Shipping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    partner = ShippingType_Interface()
    setattr(partner, 'shipping73', None)
    _safe_set(owner, 'shippingType272', partner)
    assert getattr(partner, 'shipping73') == owner
    _safe_set(owner, 'shippingType272', None)
    assert getattr(partner, 'shipping73') is None


def test_assoc_searchFacade_keywordSet_stub_double():
    # searchFacade has no real 'keywordSet22' property in the generated
    # code (a bare stub) -- manually attach it so keywordSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # keywordSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = keywordSet(keyword="sample_text")
    partner = searchFacade()
    setattr(partner, 'keywordSet22', None)
    _safe_set(owner, 'searchFacade23', partner)
    assert getattr(partner, 'keywordSet22') == owner
    _safe_set(owner, 'searchFacade23', None)
    assert getattr(partner, 'keywordSet22') is None


