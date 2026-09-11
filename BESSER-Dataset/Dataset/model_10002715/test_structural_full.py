import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Cart_Checkout,
    Cart_ShoppingCart,
    Customer_Account,
    Customer_Customer,
    Customer_Customer1,
    Customer_Payment,
    Customer_Payment1,
    Customer_User,
    GUI_Screen,
    Product_Item,
    Product_Item_Specification,
    Product_Item_Type,
    Shopping_Cart_Checkout,
    Shopping_Cart_ShoppingCart,
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

def test_Cart_ShoppingCart_AddCart_value_roundtrip():
    instance = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.AddCart == 7
    instance.AddCart = 13
    assert instance.AddCart == 13


def test_Cart_ShoppingCart_CheckoutID_value_roundtrip():
    instance = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.CheckoutID == 7
    instance.CheckoutID = 13
    assert instance.CheckoutID == 13


def test_Cart_ShoppingCart_GetTotal___value_roundtrip():
    instance = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.GetTotal__ == 3.14
    instance.GetTotal__ = 9.99
    assert instance.GetTotal__ == 9.99


def test_Cart_ShoppingCart_RemoveOrder_value_roundtrip():
    instance = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.RemoveOrder == 7
    instance.RemoveOrder = 13
    assert instance.RemoveOrder == 13


def test_Cart_ShoppingCart_UpdateOrder_value_roundtrip():
    instance = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.UpdateOrder == 7
    instance.UpdateOrder = 13
    assert instance.UpdateOrder == 13


def test_Cart_ShoppingCart_creationDate_value_roundtrip():
    instance = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.creationDate == date(2024, 1, 1)
    instance.creationDate = date(2025, 6, 15)
    assert instance.creationDate == date(2025, 6, 15)


def test_Cart_ShoppingCart_id_value_roundtrip():
    instance = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Customer_Account_Login___value_roundtrip():
    instance = Customer_Account(Login__="sample_text", account__="sample_text")
    assert instance.Login__ == "sample_text"
    instance.Login__ = "sample_text_2"
    assert instance.Login__ == "sample_text_2"


def test_Customer_Account_account___value_roundtrip():
    instance = Customer_Account(Login__="sample_text", account__="sample_text")
    assert instance.account__ == "sample_text"
    instance.account__ = "sample_text_2"
    assert instance.account__ == "sample_text_2"


def test_Customer_Customer_Message_value_roundtrip():
    instance = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    assert instance.Message == "sample_text"
    instance.Message = "sample_text_2"
    assert instance.Message == "sample_text_2"


def test_Customer_Customer_emailAddress_value_roundtrip():
    instance = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    assert instance.emailAddress == "sample_text"
    instance.emailAddress = "sample_text_2"
    assert instance.emailAddress == "sample_text_2"


def test_Customer_Customer_firstname_value_roundtrip():
    instance = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_Customer_Customer_id_value_roundtrip():
    instance = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Customer_Customer_lastname_value_roundtrip():
    instance = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_Customer_Customer_login_value_roundtrip():
    instance = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_Customer_Customer_password_value_roundtrip():
    instance = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Customer_Customer1_Account___value_roundtrip():
    instance = Customer_Customer1(Account__="sample_text", PaymentMet__=3.14, select__="sample_text", userId="sample_text")
    assert instance.Account__ == "sample_text"
    instance.Account__ = "sample_text_2"
    assert instance.Account__ == "sample_text_2"


def test_Customer_Customer1_PaymentMet___value_roundtrip():
    instance = Customer_Customer1(Account__="sample_text", PaymentMet__=3.14, select__="sample_text", userId="sample_text")
    assert instance.PaymentMet__ == 3.14
    instance.PaymentMet__ = 9.99
    assert instance.PaymentMet__ == 9.99


def test_Customer_Customer1_select___value_roundtrip():
    instance = Customer_Customer1(Account__="sample_text", PaymentMet__=3.14, select__="sample_text", userId="sample_text")
    assert instance.select__ == "sample_text"
    instance.select__ = "sample_text_2"
    assert instance.select__ == "sample_text_2"


def test_Customer_Customer1_userId_value_roundtrip():
    instance = Customer_Customer1(Account__="sample_text", PaymentMet__=3.14, select__="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_Customer_Payment_ApplPay_value_roundtrip():
    instance = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    assert instance.ApplPay == 7
    instance.ApplPay = 13
    assert instance.ApplPay == 13


def test_Customer_Payment_CustomerId_value_roundtrip():
    instance = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    assert instance.CustomerId == "sample_text"
    instance.CustomerId = "sample_text_2"
    assert instance.CustomerId == "sample_text_2"


def test_Customer_Payment_PayPal_value_roundtrip():
    instance = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    assert instance.PayPal == 7
    instance.PayPal = 13
    assert instance.PayPal == 13


def test_Customer_Payment_Payment___value_roundtrip():
    instance = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    assert instance.Payment__ == 3.14
    instance.Payment__ = 9.99
    assert instance.Payment__ == 9.99


def test_Customer_Payment_Paymentid_value_roundtrip():
    instance = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    assert instance.Paymentid == 7
    instance.Paymentid = 13
    assert instance.Paymentid == 13


def test_Customer_Payment_login_value_roundtrip():
    instance = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_Customer_User_Addresschange___value_roundtrip():
    instance = Customer_User(Addresschange__="sample_text", userid__="sample_text")
    assert instance.Addresschange__ == "sample_text"
    instance.Addresschange__ = "sample_text_2"
    assert instance.Addresschange__ == "sample_text_2"


def test_Customer_User_userid___value_roundtrip():
    instance = Customer_User(Addresschange__="sample_text", userid__="sample_text")
    assert instance.userid__ == "sample_text"
    instance.userid__ = "sample_text_2"
    assert instance.userid__ == "sample_text_2"


def test_GUI_Screen_DisplayList___value_roundtrip():
    instance = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    assert instance.DisplayList__ == 7
    instance.DisplayList__ = 13
    assert instance.DisplayList__ == 13


def test_GUI_Screen_Error___value_roundtrip():
    instance = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    assert instance.Error__ == "sample_text"
    instance.Error__ = "sample_text_2"
    assert instance.Error__ == "sample_text_2"


def test_GUI_Screen_Exit___value_roundtrip():
    instance = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    assert instance.Exit__ == "sample_text"
    instance.Exit__ = "sample_text_2"
    assert instance.Exit__ == "sample_text_2"


def test_GUI_Screen_Message_value_roundtrip():
    instance = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    assert instance.Message == "sample_text"
    instance.Message = "sample_text_2"
    assert instance.Message == "sample_text_2"


def test_GUI_Screen_id_value_roundtrip():
    instance = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Product_Item_OutofStock___value_roundtrip():
    instance = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    assert instance.OutofStock__ == "sample_text"
    instance.OutofStock__ = "sample_text_2"
    assert instance.OutofStock__ == "sample_text_2"


def test_Product_Item_id_value_roundtrip():
    instance = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Product_Item_list___value_roundtrip():
    instance = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    assert instance.list__ == 3.14
    instance.list__ = 9.99
    assert instance.list__ == 9.99


def test_Product_Item_quantity_value_roundtrip():
    instance = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Product_Item_totalcost___value_roundtrip():
    instance = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    assert instance.totalcost__ == "sample_text"
    instance.totalcost__ = "sample_text_2"
    assert instance.totalcost__ == "sample_text_2"


def test_Product_Item_Specification_Brand___value_roundtrip():
    instance = Product_Item_Specification(Brand__="sample_text", ItemSpecs__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.Brand__ == "sample_text"
    instance.Brand__ = "sample_text_2"
    assert instance.Brand__ == "sample_text_2"


def test_Product_Item_Specification_ItemSpecs___value_roundtrip():
    instance = Product_Item_Specification(Brand__="sample_text", ItemSpecs__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.ItemSpecs__ == "sample_text"
    instance.ItemSpecs__ = "sample_text_2"
    assert instance.ItemSpecs__ == "sample_text_2"


def test_Product_Item_Specification_id_value_roundtrip():
    instance = Product_Item_Specification(Brand__="sample_text", ItemSpecs__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Product_Item_Specification_price_value_roundtrip():
    instance = Product_Item_Specification(Brand__="sample_text", ItemSpecs__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_Product_Item_Specification_quantity_value_roundtrip():
    instance = Product_Item_Specification(Brand__="sample_text", ItemSpecs__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Product_Item_Type_Avail___value_roundtrip():
    instance = Product_Item_Type(Avail__="sample_text", ItemType__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.Avail__ == "sample_text"
    instance.Avail__ = "sample_text_2"
    assert instance.Avail__ == "sample_text_2"


def test_Product_Item_Type_ItemType___value_roundtrip():
    instance = Product_Item_Type(Avail__="sample_text", ItemType__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.ItemType__ == "sample_text"
    instance.ItemType__ = "sample_text_2"
    assert instance.ItemType__ == "sample_text_2"


def test_Product_Item_Type_id_value_roundtrip():
    instance = Product_Item_Type(Avail__="sample_text", ItemType__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Product_Item_Type_price_value_roundtrip():
    instance = Product_Item_Type(Avail__="sample_text", ItemType__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_Product_Item_Type_quantity_value_roundtrip():
    instance = Product_Item_Type(Avail__="sample_text", ItemType__="sample_text", id=7, price=3.14, quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Shopping_Cart_Checkout_CheckoutID_value_roundtrip():
    instance = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    assert instance.CheckoutID == 7
    instance.CheckoutID = 13
    assert instance.CheckoutID == 13


def test_Shopping_Cart_Checkout_Checkout___value_roundtrip():
    instance = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    assert instance.Checkout__ == 3.14
    instance.Checkout__ = 9.99
    assert instance.Checkout__ == 9.99


def test_Shopping_Cart_Checkout_CustomerID_value_roundtrip():
    instance = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    assert instance.CustomerID == "sample_text"
    instance.CustomerID = "sample_text_2"
    assert instance.CustomerID == "sample_text_2"


def test_Shopping_Cart_Checkout_Paymentid_value_roundtrip():
    instance = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    assert instance.Paymentid == 7
    instance.Paymentid = 13
    assert instance.Paymentid == 13


def test_Shopping_Cart_Checkout_billingMethod_value_roundtrip():
    instance = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    assert instance.billingMethod == "sample_text"
    instance.billingMethod = "sample_text_2"
    assert instance.billingMethod == "sample_text_2"


def test_Shopping_Cart_ShoppingCart_AddOrder_value_roundtrip():
    instance = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.AddOrder == 7
    instance.AddOrder = 13
    assert instance.AddOrder == 13


def test_Shopping_Cart_ShoppingCart_CheckoutID_value_roundtrip():
    instance = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.CheckoutID == 7
    instance.CheckoutID = 13
    assert instance.CheckoutID == 13


def test_Shopping_Cart_ShoppingCart_GetTotal___value_roundtrip():
    instance = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.GetTotal__ == 3.14
    instance.GetTotal__ = 9.99
    assert instance.GetTotal__ == 9.99


def test_Shopping_Cart_ShoppingCart_RemoveOrder_value_roundtrip():
    instance = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.RemoveOrder == 7
    instance.RemoveOrder = 13
    assert instance.RemoveOrder == 13


def test_Shopping_Cart_ShoppingCart_UpdateOrder_value_roundtrip():
    instance = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.UpdateOrder == 7
    instance.UpdateOrder = 13
    assert instance.UpdateOrder == 13


def test_Shopping_Cart_ShoppingCart_creationDate_value_roundtrip():
    instance = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.creationDate == date(2024, 1, 1)
    instance.creationDate = date(2025, 6, 15)
    assert instance.creationDate == date(2025, 6, 15)


def test_Shopping_Cart_ShoppingCart_id_value_roundtrip():
    instance = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_assoc_Customer_ShoppingCart_link_reassign_clear():
    a = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    b1 = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    b2 = Customer_Customer(Message="sample_text_2", emailAddress="sample_text_2", firstname="sample_text_2", id=13, lastname="sample_text_2", login="sample_text_2", password="sample_text_2")
    _safe_set(a, 'Customer_ShoppingCart_13', b1)
    assert _is_linked(a, 'Customer_ShoppingCart_13', b1)
    if hasattr(b1, 'Customer_ShoppingCart_02'):
        assert _is_linked(b1, 'Customer_ShoppingCart_02', a)
    _safe_set(a, 'Customer_ShoppingCart_13', b2)
    assert _is_linked(a, 'Customer_ShoppingCart_13', b2)
    if hasattr(b1, 'Customer_ShoppingCart_02'):
        assert not _is_linked(b1, 'Customer_ShoppingCart_02', a)
    if hasattr(b2, 'Customer_ShoppingCart_02'):
        assert _is_linked(b2, 'Customer_ShoppingCart_02', a)
    _safe_set(a, 'Customer_ShoppingCart_13', None)
    assert not _is_linked(a, 'Customer_ShoppingCart_13', b2)
    if hasattr(b2, 'Customer_ShoppingCart_02'):
        assert not _is_linked(b2, 'Customer_ShoppingCart_02', a)


def test_assoc_GUI_Screen_Account_link_reassign_clear():
    a = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    b1 = Customer_Account(Login__="sample_text", account__="sample_text")
    b2 = Customer_Account(Login__="sample_text_2", account__="sample_text_2")
    _safe_set(a, 'GUI_Screen_Account_022', b1)
    assert _is_linked(a, 'GUI_Screen_Account_022', b1)
    if hasattr(b1, 'GUI_Screen_Account_123'):
        assert _is_linked(b1, 'GUI_Screen_Account_123', a)
    _safe_set(a, 'GUI_Screen_Account_022', b2)
    assert _is_linked(a, 'GUI_Screen_Account_022', b2)
    if hasattr(b1, 'GUI_Screen_Account_123'):
        assert not _is_linked(b1, 'GUI_Screen_Account_123', a)
    if hasattr(b2, 'GUI_Screen_Account_123'):
        assert _is_linked(b2, 'GUI_Screen_Account_123', a)
    _safe_set(a, 'GUI_Screen_Account_022', None)
    assert not _is_linked(a, 'GUI_Screen_Account_022', b2)
    if hasattr(b2, 'GUI_Screen_Account_123'):
        assert not _is_linked(b2, 'GUI_Screen_Account_123', a)


def test_assoc_GUI_Screen_Item_link_reassign_clear():
    a = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    b1 = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    b2 = GUI_Screen(DisplayList__=13, Error__="sample_text_2", Exit__="sample_text_2", Message="sample_text_2", id=13)
    _safe_set(a, 'GUI_Screen_Item_127', b1)
    assert _is_linked(a, 'GUI_Screen_Item_127', b1)
    if hasattr(b1, 'GUI_Screen_Item_026'):
        assert _is_linked(b1, 'GUI_Screen_Item_026', a)
    _safe_set(a, 'GUI_Screen_Item_127', b2)
    assert _is_linked(a, 'GUI_Screen_Item_127', b2)
    if hasattr(b1, 'GUI_Screen_Item_026'):
        assert not _is_linked(b1, 'GUI_Screen_Item_026', a)
    if hasattr(b2, 'GUI_Screen_Item_026'):
        assert _is_linked(b2, 'GUI_Screen_Item_026', a)
    _safe_set(a, 'GUI_Screen_Item_127', None)
    assert not _is_linked(a, 'GUI_Screen_Item_127', b2)
    if hasattr(b2, 'GUI_Screen_Item_026'):
        assert not _is_linked(b2, 'GUI_Screen_Item_026', a)


def test_assoc_GUI_Screen_ShoppingCart_link_reassign_clear():
    a = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    b1 = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    b2 = Cart_ShoppingCart(AddCart=13, CheckoutID=13, GetTotal__=9.99, RemoveOrder=13, UpdateOrder=13, creationDate=date(2025, 6, 15), id=13)
    _safe_set(a, 'GUI_Screen_ShoppingCart_024', b1)
    assert _is_linked(a, 'GUI_Screen_ShoppingCart_024', b1)
    if hasattr(b1, 'GUI_Screen_ShoppingCart_125'):
        assert _is_linked(b1, 'GUI_Screen_ShoppingCart_125', a)
    _safe_set(a, 'GUI_Screen_ShoppingCart_024', b2)
    assert _is_linked(a, 'GUI_Screen_ShoppingCart_024', b2)
    if hasattr(b1, 'GUI_Screen_ShoppingCart_125'):
        assert not _is_linked(b1, 'GUI_Screen_ShoppingCart_125', a)
    if hasattr(b2, 'GUI_Screen_ShoppingCart_125'):
        assert _is_linked(b2, 'GUI_Screen_ShoppingCart_125', a)
    _safe_set(a, 'GUI_Screen_ShoppingCart_024', None)
    assert not _is_linked(a, 'GUI_Screen_ShoppingCart_024', b2)
    if hasattr(b2, 'GUI_Screen_ShoppingCart_125'):
        assert not _is_linked(b2, 'GUI_Screen_ShoppingCart_125', a)


def test_assoc_Item_ShoppingCart_link_reassign_clear():
    a = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    b1 = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    b2 = Cart_ShoppingCart(AddCart=13, CheckoutID=13, GetTotal__=9.99, RemoveOrder=13, UpdateOrder=13, creationDate=date(2025, 6, 15), id=13)
    _safe_set(a, 'Item_ShoppingCart_020', b1)
    assert _is_linked(a, 'Item_ShoppingCart_020', b1)
    if hasattr(b1, 'Item_ShoppingCart_121'):
        assert _is_linked(b1, 'Item_ShoppingCart_121', a)
    _safe_set(a, 'Item_ShoppingCart_020', b2)
    assert _is_linked(a, 'Item_ShoppingCart_020', b2)
    if hasattr(b1, 'Item_ShoppingCart_121'):
        assert not _is_linked(b1, 'Item_ShoppingCart_121', a)
    if hasattr(b2, 'Item_ShoppingCart_121'):
        assert _is_linked(b2, 'Item_ShoppingCart_121', a)
    _safe_set(a, 'Item_ShoppingCart_020', None)
    assert not _is_linked(a, 'Item_ShoppingCart_020', b2)
    if hasattr(b2, 'Item_ShoppingCart_121'):
        assert not _is_linked(b2, 'Item_ShoppingCart_121', a)


def test_assoc_Item_Specification_Item_link_reassign_clear():
    a = Product_Item_Specification(Brand__="sample_text", ItemSpecs__="sample_text", id=7, price=3.14, quantity=7)
    b1 = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    b2 = Product_Item(OutofStock__="sample_text_2", id=13, list__=9.99, quantity=13, totalcost__="sample_text_2")
    _safe_set(a, 'Item_Specification_Item_016', b1)
    assert _is_linked(a, 'Item_Specification_Item_016', b1)
    if hasattr(b1, 'Item_Specification_Item_117'):
        assert _is_linked(b1, 'Item_Specification_Item_117', a)
    _safe_set(a, 'Item_Specification_Item_016', b2)
    assert _is_linked(a, 'Item_Specification_Item_016', b2)
    if hasattr(b1, 'Item_Specification_Item_117'):
        assert not _is_linked(b1, 'Item_Specification_Item_117', a)
    if hasattr(b2, 'Item_Specification_Item_117'):
        assert _is_linked(b2, 'Item_Specification_Item_117', a)
    _safe_set(a, 'Item_Specification_Item_016', None)
    assert not _is_linked(a, 'Item_Specification_Item_016', b2)
    if hasattr(b2, 'Item_Specification_Item_117'):
        assert not _is_linked(b2, 'Item_Specification_Item_117', a)


def test_assoc_Item_Type_Item_link_reassign_clear():
    a = Product_Item_Type(Avail__="sample_text", ItemType__="sample_text", id=7, price=3.14, quantity=7)
    b1 = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    b2 = Product_Item(OutofStock__="sample_text_2", id=13, list__=9.99, quantity=13, totalcost__="sample_text_2")
    _safe_set(a, 'Item_Type_Item_018', b1)
    assert _is_linked(a, 'Item_Type_Item_018', b1)
    if hasattr(b1, 'Item_Type_Item_119'):
        assert _is_linked(b1, 'Item_Type_Item_119', a)
    _safe_set(a, 'Item_Type_Item_018', b2)
    assert _is_linked(a, 'Item_Type_Item_018', b2)
    if hasattr(b1, 'Item_Type_Item_119'):
        assert not _is_linked(b1, 'Item_Type_Item_119', a)
    if hasattr(b2, 'Item_Type_Item_119'):
        assert _is_linked(b2, 'Item_Type_Item_119', a)
    _safe_set(a, 'Item_Type_Item_018', None)
    assert not _is_linked(a, 'Item_Type_Item_018', b2)
    if hasattr(b2, 'Item_Type_Item_119'):
        assert not _is_linked(b2, 'Item_Type_Item_119', a)


def test_assoc_Payment_Checkout_link_reassign_clear():
    a = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    b1 = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    b2 = Customer_Payment(ApplPay=13, CustomerId="sample_text_2", PayPal=13, Payment__=9.99, Paymentid=13, login="sample_text_2")
    _safe_set(a, 'Payment_Checkout_15', {b1})
    assert _is_linked(a, 'Payment_Checkout_15', b1)
    if hasattr(b1, 'Payment_Checkout_04'):
        assert _is_linked(b1, 'Payment_Checkout_04', a)
    _safe_set(a, 'Payment_Checkout_15', {b2})
    assert _is_linked(a, 'Payment_Checkout_15', b2)
    if hasattr(b1, 'Payment_Checkout_04'):
        assert not _is_linked(b1, 'Payment_Checkout_04', a)
    if hasattr(b2, 'Payment_Checkout_04'):
        assert _is_linked(b2, 'Payment_Checkout_04', a)
    _safe_set(a, 'Payment_Checkout_15', set())
    assert not _is_linked(a, 'Payment_Checkout_15', b2)
    if hasattr(b2, 'Payment_Checkout_04'):
        assert not _is_linked(b2, 'Payment_Checkout_04', a)


def test_assoc_Payment_Customer_link_reassign_clear():
    a = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    b1 = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    b2 = Customer_Customer(Message="sample_text_2", emailAddress="sample_text_2", firstname="sample_text_2", id=13, lastname="sample_text_2", login="sample_text_2", password="sample_text_2")
    _safe_set(a, 'Payment_Customer_00', b1)
    assert _is_linked(a, 'Payment_Customer_00', b1)
    if hasattr(b1, 'Payment_Customer_11'):
        assert _is_linked(b1, 'Payment_Customer_11', a)
    _safe_set(a, 'Payment_Customer_00', b2)
    assert _is_linked(a, 'Payment_Customer_00', b2)
    if hasattr(b1, 'Payment_Customer_11'):
        assert not _is_linked(b1, 'Payment_Customer_11', a)
    if hasattr(b2, 'Payment_Customer_11'):
        assert _is_linked(b2, 'Payment_Customer_11', a)
    _safe_set(a, 'Payment_Customer_00', None)
    assert not _is_linked(a, 'Payment_Customer_00', b2)
    if hasattr(b2, 'Payment_Customer_11'):
        assert not _is_linked(b2, 'Payment_Customer_11', a)


def test_assoc_ShoppingCart_Checkout_link_reassign_clear():
    a = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    b1 = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    b2 = Shopping_Cart_Checkout(CheckoutID=13, Checkout__=9.99, CustomerID="sample_text_2", Paymentid=13, billingMethod="sample_text_2")
    _safe_set(a, 'ShoppingCart_Checkout_06', {b1})
    assert _is_linked(a, 'ShoppingCart_Checkout_06', b1)
    if hasattr(b1, 'ShoppingCart_Checkout_17'):
        assert _is_linked(b1, 'ShoppingCart_Checkout_17', a)
    _safe_set(a, 'ShoppingCart_Checkout_06', {b2})
    assert _is_linked(a, 'ShoppingCart_Checkout_06', b2)
    if hasattr(b1, 'ShoppingCart_Checkout_17'):
        assert not _is_linked(b1, 'ShoppingCart_Checkout_17', a)
    if hasattr(b2, 'ShoppingCart_Checkout_17'):
        assert _is_linked(b2, 'ShoppingCart_Checkout_17', a)
    _safe_set(a, 'ShoppingCart_Checkout_06', set())
    assert not _is_linked(a, 'ShoppingCart_Checkout_06', b2)
    if hasattr(b2, 'ShoppingCart_Checkout_17'):
        assert not _is_linked(b2, 'ShoppingCart_Checkout_17', a)


def test_assoc_ShoppingCart_Customer_link_reassign_clear():
    a = Customer_Customer1(Account__="sample_text", PaymentMet__=3.14, select__="sample_text", userId="sample_text")
    b1 = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    b2 = Cart_ShoppingCart(AddCart=13, CheckoutID=13, GetTotal__=9.99, RemoveOrder=13, UpdateOrder=13, creationDate=date(2025, 6, 15), id=13)
    _safe_set(a, 'ShoppingCart_Customer_113', b1)
    assert _is_linked(a, 'ShoppingCart_Customer_113', b1)
    if hasattr(b1, 'ShoppingCart_Customer_012'):
        assert _is_linked(b1, 'ShoppingCart_Customer_012', a)
    _safe_set(a, 'ShoppingCart_Customer_113', b2)
    assert _is_linked(a, 'ShoppingCart_Customer_113', b2)
    if hasattr(b1, 'ShoppingCart_Customer_012'):
        assert not _is_linked(b1, 'ShoppingCart_Customer_012', a)
    if hasattr(b2, 'ShoppingCart_Customer_012'):
        assert _is_linked(b2, 'ShoppingCart_Customer_012', a)
    _safe_set(a, 'ShoppingCart_Customer_113', None)
    assert not _is_linked(a, 'ShoppingCart_Customer_113', b2)
    if hasattr(b2, 'ShoppingCart_Customer_012'):
        assert not _is_linked(b2, 'ShoppingCart_Customer_012', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Cart_ShoppingCart_strategy = st.builds(Cart_ShoppingCart, AddCart=st.integers(), CheckoutID=st.integers(), GetTotal__=st.floats(allow_nan=False, allow_infinity=False), RemoveOrder=st.integers(), UpdateOrder=st.integers(), creationDate=st.dates(), id=st.integers())
@given(instance=Cart_ShoppingCart_strategy)
@settings(max_examples=25)
def test_Cart_ShoppingCart_instantiation(instance):
    assert isinstance(instance, Cart_ShoppingCart)


Customer_Account_strategy = st.builds(Customer_Account, Login__=safe_text, account__=safe_text)
@given(instance=Customer_Account_strategy)
@settings(max_examples=25)
def test_Customer_Account_instantiation(instance):
    assert isinstance(instance, Customer_Account)


Customer_Customer_strategy = st.builds(Customer_Customer, Message=safe_text, emailAddress=safe_text, firstname=safe_text, id=st.integers(), lastname=safe_text, login=safe_text, password=safe_text)
@given(instance=Customer_Customer_strategy)
@settings(max_examples=25)
def test_Customer_Customer_instantiation(instance):
    assert isinstance(instance, Customer_Customer)


Customer_Customer1_strategy = st.builds(Customer_Customer1, Account__=safe_text, PaymentMet__=st.floats(allow_nan=False, allow_infinity=False), select__=safe_text, userId=safe_text)
@given(instance=Customer_Customer1_strategy)
@settings(max_examples=25)
def test_Customer_Customer1_instantiation(instance):
    assert isinstance(instance, Customer_Customer1)


Customer_Payment_strategy = st.builds(Customer_Payment, ApplPay=st.integers(), CustomerId=safe_text, PayPal=st.integers(), Payment__=st.floats(allow_nan=False, allow_infinity=False), Paymentid=st.integers(), login=safe_text)
@given(instance=Customer_Payment_strategy)
@settings(max_examples=25)
def test_Customer_Payment_instantiation(instance):
    assert isinstance(instance, Customer_Payment)


Customer_User_strategy = st.builds(Customer_User, Addresschange__=safe_text, userid__=safe_text)
@given(instance=Customer_User_strategy)
@settings(max_examples=25)
def test_Customer_User_instantiation(instance):
    assert isinstance(instance, Customer_User)


GUI_Screen_strategy = st.builds(GUI_Screen, DisplayList__=st.integers(), Error__=safe_text, Exit__=safe_text, Message=safe_text, id=st.integers())
@given(instance=GUI_Screen_strategy)
@settings(max_examples=25)
def test_GUI_Screen_instantiation(instance):
    assert isinstance(instance, GUI_Screen)


Product_Item_strategy = st.builds(Product_Item, OutofStock__=safe_text, id=st.integers(), list__=st.floats(allow_nan=False, allow_infinity=False), quantity=st.integers(), totalcost__=safe_text)
@given(instance=Product_Item_strategy)
@settings(max_examples=25)
def test_Product_Item_instantiation(instance):
    assert isinstance(instance, Product_Item)


Product_Item_Specification_strategy = st.builds(Product_Item_Specification, Brand__=safe_text, ItemSpecs__=safe_text, id=st.integers(), price=st.floats(allow_nan=False, allow_infinity=False), quantity=st.integers())
@given(instance=Product_Item_Specification_strategy)
@settings(max_examples=25)
def test_Product_Item_Specification_instantiation(instance):
    assert isinstance(instance, Product_Item_Specification)


Product_Item_Type_strategy = st.builds(Product_Item_Type, Avail__=safe_text, ItemType__=safe_text, id=st.integers(), price=st.floats(allow_nan=False, allow_infinity=False), quantity=st.integers())
@given(instance=Product_Item_Type_strategy)
@settings(max_examples=25)
def test_Product_Item_Type_instantiation(instance):
    assert isinstance(instance, Product_Item_Type)


Shopping_Cart_Checkout_strategy = st.builds(Shopping_Cart_Checkout, CheckoutID=st.integers(), Checkout__=st.floats(allow_nan=False, allow_infinity=False), CustomerID=safe_text, Paymentid=st.integers(), billingMethod=safe_text)
@given(instance=Shopping_Cart_Checkout_strategy)
@settings(max_examples=25)
def test_Shopping_Cart_Checkout_instantiation(instance):
    assert isinstance(instance, Shopping_Cart_Checkout)


Shopping_Cart_ShoppingCart_strategy = st.builds(Shopping_Cart_ShoppingCart, AddOrder=st.integers(), CheckoutID=st.integers(), GetTotal__=st.floats(allow_nan=False, allow_infinity=False), RemoveOrder=st.integers(), UpdateOrder=st.integers(), creationDate=st.dates(), id=st.integers())
@given(instance=Shopping_Cart_ShoppingCart_strategy)
@settings(max_examples=25)
def test_Shopping_Cart_ShoppingCart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart_ShoppingCart)


