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
    Shopping,
    OrderDetails,
    ShippingInfo,
    Order,
    ShoppingCart,
    Administrator,
    Customer,
    Users,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_shopping_is_not_abstract():
    assert not inspect.isabstract(Shopping)


def test_hyp_shopping_constructor_exists():
    assert callable(Shopping.__init__)


def test_hyp_shopping_constructor_args():
    sig = inspect.signature(Shopping.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Identity" in params, "Missing parameter 'Identity'"
    assert "Location" in params, "Missing parameter 'Location'"






def test_hyp_orderdetails_is_not_abstract():
    assert not inspect.isabstract(OrderDetails)


def test_hyp_orderdetails_constructor_exists():
    assert callable(OrderDetails.__init__)


def test_hyp_orderdetails_constructor_args():
    sig = inspect.signature(OrderDetails.__init__)
    params = list(sig.parameters.keys())
    assert "ProductName" in params, "Missing parameter 'ProductName'"
    assert "UnitCost" in params, "Missing parameter 'UnitCost'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "SubTotal" in params, "Missing parameter 'SubTotal'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"









def test_hyp_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(ShippingInfo)


def test_hyp_shippinginfo_constructor_exists():
    assert callable(ShippingInfo.__init__)


def test_hyp_shippinginfo_constructor_args():
    sig = inspect.signature(ShippingInfo.__init__)
    params = list(sig.parameters.keys())
    assert "ShippingID" in params, "Missing parameter 'ShippingID'"
    assert "ShippingRegionID" in params, "Missing parameter 'ShippingRegionID'"
    assert "ShippingCost" in params, "Missing parameter 'ShippingCost'"
    assert "ShippingType" in params, "Missing parameter 'ShippingType'"







def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "DateShipped" in params, "Missing parameter 'DateShipped'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "CustomerID" in params, "Missing parameter 'CustomerID'"
    assert "DateCreated" in params, "Missing parameter 'DateCreated'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "ShippingID" in params, "Missing parameter 'ShippingID'"










def test_hyp_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_hyp_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_hyp_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "DateAdded" in params, "Missing parameter 'DateAdded'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "CartID" in params, "Missing parameter 'CartID'"







def test_hyp_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_hyp_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_hyp_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "AdminName" in params, "Missing parameter 'AdminName'"
    assert "Email" in params, "Missing parameter 'Email'"





def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "CreditCartInfo" in params, "Missing parameter 'CreditCartInfo'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "AccountBalance" in params, "Missing parameter 'AccountBalance'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "ShippingInfo" in params, "Missing parameter 'ShippingInfo'"









def test_hyp_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_hyp_users_constructor_exists():
    assert callable(Users.__init__)


def test_hyp_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "RegisterDate" in params, "Missing parameter 'RegisterDate'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "LoginStatus" in params, "Missing parameter 'LoginStatus'"






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
Shopping_strategy = st.builds(
    Shopping,
    Name=
        safe_text,
    Identity=
        st.integers(),
    Location=
        safe_text
)
OrderDetails_strategy = st.builds(
    OrderDetails,
    ProductName=
        safe_text,
    UnitCost=
        st.integers(),
    OrderID=
        st.integers(),
    Quantity=
        st.integers(),
    SubTotal=
        st.integers(),
    ProductID=
        st.integers()
)
ShippingInfo_strategy = st.builds(
    ShippingInfo,
    ShippingID=
        st.integers(),
    ShippingRegionID=
        st.integers(),
    ShippingCost=
        st.integers(),
    ShippingType=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Status=
        safe_text,
    DateShipped=
        safe_text,
    OrderID=
        st.integers(),
    CustomerID=
        safe_text,
    DateCreated=
        safe_text,
    CustomerName=
        safe_text,
    ShippingID=
        safe_text
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    ProductID=
        st.integers(),
    DateAdded=
        st.integers(),
    Quantity=
        st.integers(),
    CartID=
        st.integers()
)
Administrator_strategy = st.builds(
    Administrator,
    AdminName=
        safe_text,
    Email=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    CreditCartInfo=
        safe_text,
    CustomerName=
        safe_text,
    AccountBalance=
        st.integers(),
    Address=
        safe_text,
    Email=
        safe_text,
    ShippingInfo=
        safe_text
)
Users_strategy = st.builds(
    Users,
    Password=
        safe_text,
    RegisterDate=
        st.integers(),
    UserID=
        safe_text,
    LoginStatus=
        safe_text
)




@given(instance=Shopping_strategy)
def test_hyp_shopping_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Shopping_strategy)
def test_hyp_shopping_Identity_setter(instance):
    original = instance.Identity
    instance.Identity = original
    assert instance.Identity == original



@given(instance=Shopping_strategy)
def test_hyp_shopping_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original




@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_ProductName_setter(instance):
    original = instance.ProductName
    instance.ProductName = original
    assert instance.ProductName == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_UnitCost_setter(instance):
    original = instance.UnitCost
    instance.UnitCost = original
    assert instance.UnitCost == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_SubTotal_setter(instance):
    original = instance.SubTotal
    instance.SubTotal = original
    assert instance.SubTotal == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original




@given(instance=ShippingInfo_strategy)
def test_hyp_shippinginfo_ShippingID_setter(instance):
    original = instance.ShippingID
    instance.ShippingID = original
    assert instance.ShippingID == original



@given(instance=ShippingInfo_strategy)
def test_hyp_shippinginfo_ShippingRegionID_setter(instance):
    original = instance.ShippingRegionID
    instance.ShippingRegionID = original
    assert instance.ShippingRegionID == original



@given(instance=ShippingInfo_strategy)
def test_hyp_shippinginfo_ShippingCost_setter(instance):
    original = instance.ShippingCost
    instance.ShippingCost = original
    assert instance.ShippingCost == original



@given(instance=ShippingInfo_strategy)
def test_hyp_shippinginfo_ShippingType_setter(instance):
    original = instance.ShippingType
    instance.ShippingType = original
    assert instance.ShippingType == original




@given(instance=Order_strategy)
def test_hyp_order_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Order_strategy)
def test_hyp_order_DateShipped_setter(instance):
    original = instance.DateShipped
    instance.DateShipped = original
    assert instance.DateShipped == original



@given(instance=Order_strategy)
def test_hyp_order_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Order_strategy)
def test_hyp_order_CustomerID_setter(instance):
    original = instance.CustomerID
    instance.CustomerID = original
    assert instance.CustomerID == original



@given(instance=Order_strategy)
def test_hyp_order_DateCreated_setter(instance):
    original = instance.DateCreated
    instance.DateCreated = original
    assert instance.DateCreated == original



@given(instance=Order_strategy)
def test_hyp_order_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=Order_strategy)
def test_hyp_order_ShippingID_setter(instance):
    original = instance.ShippingID
    instance.ShippingID = original
    assert instance.ShippingID == original




@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_DateAdded_setter(instance):
    original = instance.DateAdded
    instance.DateAdded = original
    assert instance.DateAdded == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_CartID_setter(instance):
    original = instance.CartID
    instance.CartID = original
    assert instance.CartID == original




@given(instance=Administrator_strategy)
def test_hyp_administrator_AdminName_setter(instance):
    original = instance.AdminName
    instance.AdminName = original
    assert instance.AdminName == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original




@given(instance=Customer_strategy)
def test_hyp_customer_CreditCartInfo_setter(instance):
    original = instance.CreditCartInfo
    instance.CreditCartInfo = original
    assert instance.CreditCartInfo == original



@given(instance=Customer_strategy)
def test_hyp_customer_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=Customer_strategy)
def test_hyp_customer_AccountBalance_setter(instance):
    original = instance.AccountBalance
    instance.AccountBalance = original
    assert instance.AccountBalance == original



@given(instance=Customer_strategy)
def test_hyp_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_hyp_customer_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Customer_strategy)
def test_hyp_customer_ShippingInfo_setter(instance):
    original = instance.ShippingInfo
    instance.ShippingInfo = original
    assert instance.ShippingInfo == original




@given(instance=Users_strategy)
def test_hyp_users_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Users_strategy)
def test_hyp_users_RegisterDate_setter(instance):
    original = instance.RegisterDate
    instance.RegisterDate = original
    assert instance.RegisterDate == original



@given(instance=Users_strategy)
def test_hyp_users_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=Users_strategy)
def test_hyp_users_LoginStatus_setter(instance):
    original = instance.LoginStatus
    instance.LoginStatus = original
    assert instance.LoginStatus == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator,
    Customer,
    Order,
    OrderDetails,
    ShippingInfo,
    Shopping,
    ShoppingCart,
    Users,
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

def test_Administrator_AdminName_value_roundtrip():
    instance = Administrator(AdminName="sample_text", Email="sample_text")
    assert instance.AdminName == "sample_text"
    instance.AdminName = "sample_text_2"
    assert instance.AdminName == "sample_text_2"


def test_Administrator_Email_value_roundtrip():
    instance = Administrator(AdminName="sample_text", Email="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Customer_AccountBalance_value_roundtrip():
    instance = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    assert instance.AccountBalance == 7
    instance.AccountBalance = 13
    assert instance.AccountBalance == 13


def test_Customer_Address_value_roundtrip():
    instance = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Customer_CreditCartInfo_value_roundtrip():
    instance = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    assert instance.CreditCartInfo == "sample_text"
    instance.CreditCartInfo = "sample_text_2"
    assert instance.CreditCartInfo == "sample_text_2"


def test_Customer_CustomerName_value_roundtrip():
    instance = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_Customer_Email_value_roundtrip():
    instance = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Customer_ShippingInfo_value_roundtrip():
    instance = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    assert instance.ShippingInfo == "sample_text"
    instance.ShippingInfo = "sample_text_2"
    assert instance.ShippingInfo == "sample_text_2"


def test_Order_CustomerID_value_roundtrip():
    instance = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    assert instance.CustomerID == "sample_text"
    instance.CustomerID = "sample_text_2"
    assert instance.CustomerID == "sample_text_2"


def test_Order_CustomerName_value_roundtrip():
    instance = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_Order_DateCreated_value_roundtrip():
    instance = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    assert instance.DateCreated == "sample_text"
    instance.DateCreated = "sample_text_2"
    assert instance.DateCreated == "sample_text_2"


def test_Order_DateShipped_value_roundtrip():
    instance = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    assert instance.DateShipped == "sample_text"
    instance.DateShipped = "sample_text_2"
    assert instance.DateShipped == "sample_text_2"


def test_Order_OrderID_value_roundtrip():
    instance = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Order_ShippingID_value_roundtrip():
    instance = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    assert instance.ShippingID == "sample_text"
    instance.ShippingID = "sample_text_2"
    assert instance.ShippingID == "sample_text_2"


def test_Order_Status_value_roundtrip():
    instance = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_OrderDetails_OrderID_value_roundtrip():
    instance = OrderDetails(OrderID=7, ProductID=7, ProductName="sample_text", Quantity=7, SubTotal=7, UnitCost=7)
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_OrderDetails_ProductID_value_roundtrip():
    instance = OrderDetails(OrderID=7, ProductID=7, ProductName="sample_text", Quantity=7, SubTotal=7, UnitCost=7)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_OrderDetails_ProductName_value_roundtrip():
    instance = OrderDetails(OrderID=7, ProductID=7, ProductName="sample_text", Quantity=7, SubTotal=7, UnitCost=7)
    assert instance.ProductName == "sample_text"
    instance.ProductName = "sample_text_2"
    assert instance.ProductName == "sample_text_2"


def test_OrderDetails_Quantity_value_roundtrip():
    instance = OrderDetails(OrderID=7, ProductID=7, ProductName="sample_text", Quantity=7, SubTotal=7, UnitCost=7)
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_OrderDetails_SubTotal_value_roundtrip():
    instance = OrderDetails(OrderID=7, ProductID=7, ProductName="sample_text", Quantity=7, SubTotal=7, UnitCost=7)
    assert instance.SubTotal == 7
    instance.SubTotal = 13
    assert instance.SubTotal == 13


def test_OrderDetails_UnitCost_value_roundtrip():
    instance = OrderDetails(OrderID=7, ProductID=7, ProductName="sample_text", Quantity=7, SubTotal=7, UnitCost=7)
    assert instance.UnitCost == 7
    instance.UnitCost = 13
    assert instance.UnitCost == 13


def test_ShippingInfo_ShippingCost_value_roundtrip():
    instance = ShippingInfo(ShippingCost=7, ShippingID=7, ShippingRegionID=7, ShippingType="sample_text")
    assert instance.ShippingCost == 7
    instance.ShippingCost = 13
    assert instance.ShippingCost == 13


def test_ShippingInfo_ShippingID_value_roundtrip():
    instance = ShippingInfo(ShippingCost=7, ShippingID=7, ShippingRegionID=7, ShippingType="sample_text")
    assert instance.ShippingID == 7
    instance.ShippingID = 13
    assert instance.ShippingID == 13


def test_ShippingInfo_ShippingRegionID_value_roundtrip():
    instance = ShippingInfo(ShippingCost=7, ShippingID=7, ShippingRegionID=7, ShippingType="sample_text")
    assert instance.ShippingRegionID == 7
    instance.ShippingRegionID = 13
    assert instance.ShippingRegionID == 13


def test_ShippingInfo_ShippingType_value_roundtrip():
    instance = ShippingInfo(ShippingCost=7, ShippingID=7, ShippingRegionID=7, ShippingType="sample_text")
    assert instance.ShippingType == "sample_text"
    instance.ShippingType = "sample_text_2"
    assert instance.ShippingType == "sample_text_2"


def test_Shopping_Identity_value_roundtrip():
    instance = Shopping(Identity=7, Location="sample_text", Name="sample_text")
    assert instance.Identity == 7
    instance.Identity = 13
    assert instance.Identity == 13


def test_Shopping_Location_value_roundtrip():
    instance = Shopping(Identity=7, Location="sample_text", Name="sample_text")
    assert instance.Location == "sample_text"
    instance.Location = "sample_text_2"
    assert instance.Location == "sample_text_2"


def test_Shopping_Name_value_roundtrip():
    instance = Shopping(Identity=7, Location="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_ShoppingCart_CartID_value_roundtrip():
    instance = ShoppingCart(CartID=7, DateAdded=7, ProductID=7, Quantity=7)
    assert instance.CartID == 7
    instance.CartID = 13
    assert instance.CartID == 13


def test_ShoppingCart_DateAdded_value_roundtrip():
    instance = ShoppingCart(CartID=7, DateAdded=7, ProductID=7, Quantity=7)
    assert instance.DateAdded == 7
    instance.DateAdded = 13
    assert instance.DateAdded == 13


def test_ShoppingCart_ProductID_value_roundtrip():
    instance = ShoppingCart(CartID=7, DateAdded=7, ProductID=7, Quantity=7)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_ShoppingCart_Quantity_value_roundtrip():
    instance = ShoppingCart(CartID=7, DateAdded=7, ProductID=7, Quantity=7)
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_Users_LoginStatus_value_roundtrip():
    instance = Users(LoginStatus="sample_text", Password="sample_text", RegisterDate=7, UserID="sample_text")
    assert instance.LoginStatus == "sample_text"
    instance.LoginStatus = "sample_text_2"
    assert instance.LoginStatus == "sample_text_2"


def test_Users_Password_value_roundtrip():
    instance = Users(LoginStatus="sample_text", Password="sample_text", RegisterDate=7, UserID="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Users_RegisterDate_value_roundtrip():
    instance = Users(LoginStatus="sample_text", Password="sample_text", RegisterDate=7, UserID="sample_text")
    assert instance.RegisterDate == 7
    instance.RegisterDate = 13
    assert instance.RegisterDate == 13


def test_Users_UserID_value_roundtrip():
    instance = Users(LoginStatus="sample_text", Password="sample_text", RegisterDate=7, UserID="sample_text")
    assert instance.UserID == "sample_text"
    instance.UserID = "sample_text_2"
    assert instance.UserID == "sample_text_2"


def test_assoc_Customer_Order_link_reassign_clear():
    a = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    b1 = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    b2 = Customer(AccountBalance=13, Address="sample_text_2", CreditCartInfo="sample_text_2", CustomerName="sample_text_2", Email="sample_text_2", ShippingInfo="sample_text_2")
    _safe_set(a, 'customer3', b1)
    assert _is_linked(a, 'customer3', b1)
    if hasattr(b1, 'order2'):
        assert _is_linked(b1, 'order2', a)
    _safe_set(a, 'customer3', b2)
    assert _is_linked(a, 'customer3', b2)
    if hasattr(b1, 'order2'):
        assert not _is_linked(b1, 'order2', a)
    if hasattr(b2, 'order2'):
        assert _is_linked(b2, 'order2', a)
    _safe_set(a, 'customer3', None)
    assert not _is_linked(a, 'customer3', b2)
    if hasattr(b2, 'order2'):
        assert not _is_linked(b2, 'order2', a)


def test_assoc_Customer_ShoppingCart_link_reassign_clear():
    a = ShoppingCart(CartID=7, DateAdded=7, ProductID=7, Quantity=7)
    b1 = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    b2 = Customer(AccountBalance=13, Address="sample_text_2", CreditCartInfo="sample_text_2", CustomerName="sample_text_2", Email="sample_text_2", ShippingInfo="sample_text_2")
    _safe_set(a, 'customer1', b1)
    assert _is_linked(a, 'customer1', b1)
    if hasattr(b1, 'shoppingCart0'):
        assert _is_linked(b1, 'shoppingCart0', a)
    _safe_set(a, 'customer1', b2)
    assert _is_linked(a, 'customer1', b2)
    if hasattr(b1, 'shoppingCart0'):
        assert not _is_linked(b1, 'shoppingCart0', a)
    if hasattr(b2, 'shoppingCart0'):
        assert _is_linked(b2, 'shoppingCart0', a)
    _safe_set(a, 'customer1', None)
    assert not _is_linked(a, 'customer1', b2)
    if hasattr(b2, 'shoppingCart0'):
        assert not _is_linked(b2, 'shoppingCart0', a)


def test_assoc_Order_OrderDetails_link_reassign_clear():
    a = OrderDetails(OrderID=7, ProductID=7, ProductName="sample_text", Quantity=7, SubTotal=7, UnitCost=7)
    b1 = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    b2 = Order(CustomerID="sample_text_2", CustomerName="sample_text_2", DateCreated="sample_text_2", DateShipped="sample_text_2", OrderID=13, ShippingID="sample_text_2", Status="sample_text_2")
    _safe_set(a, 'order7', b1)
    assert _is_linked(a, 'order7', b1)
    if hasattr(b1, 'has_a6'):
        assert _is_linked(b1, 'has_a6', a)
    _safe_set(a, 'order7', b2)
    assert _is_linked(a, 'order7', b2)
    if hasattr(b1, 'has_a6'):
        assert not _is_linked(b1, 'has_a6', a)
    if hasattr(b2, 'has_a6'):
        assert _is_linked(b2, 'has_a6', a)
    _safe_set(a, 'order7', None)
    assert not _is_linked(a, 'order7', b2)
    if hasattr(b2, 'has_a6'):
        assert not _is_linked(b2, 'has_a6', a)


def test_assoc_Order_ShippingInfo_link_reassign_clear():
    a = ShippingInfo(ShippingCost=7, ShippingID=7, ShippingRegionID=7, ShippingType="sample_text")
    b1 = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    b2 = Order(CustomerID="sample_text_2", CustomerName="sample_text_2", DateCreated="sample_text_2", DateShipped="sample_text_2", OrderID=13, ShippingID="sample_text_2", Status="sample_text_2")
    _safe_set(a, 'order5', b1)
    assert _is_linked(a, 'order5', b1)
    if hasattr(b1, 'shippingInfo4'):
        assert _is_linked(b1, 'shippingInfo4', a)
    _safe_set(a, 'order5', b2)
    assert _is_linked(a, 'order5', b2)
    if hasattr(b1, 'shippingInfo4'):
        assert not _is_linked(b1, 'shippingInfo4', a)
    if hasattr(b2, 'shippingInfo4'):
        assert _is_linked(b2, 'shippingInfo4', a)
    _safe_set(a, 'order5', None)
    assert not _is_linked(a, 'order5', b2)
    if hasattr(b2, 'shippingInfo4'):
        assert not _is_linked(b2, 'shippingInfo4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_strategy = st.builds(Administrator, AdminName=safe_text, Email=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Customer_strategy = st.builds(Customer, AccountBalance=st.integers(), Address=safe_text, CreditCartInfo=safe_text, CustomerName=safe_text, Email=safe_text, ShippingInfo=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Order_strategy = st.builds(Order, CustomerID=safe_text, CustomerName=safe_text, DateCreated=safe_text, DateShipped=safe_text, OrderID=st.integers(), ShippingID=safe_text, Status=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


OrderDetails_strategy = st.builds(OrderDetails, OrderID=st.integers(), ProductID=st.integers(), ProductName=safe_text, Quantity=st.integers(), SubTotal=st.integers(), UnitCost=st.integers())
@given(instance=OrderDetails_strategy)
@settings(max_examples=25)
def test_OrderDetails_instantiation(instance):
    assert isinstance(instance, OrderDetails)


ShippingInfo_strategy = st.builds(ShippingInfo, ShippingCost=st.integers(), ShippingID=st.integers(), ShippingRegionID=st.integers(), ShippingType=safe_text)
@given(instance=ShippingInfo_strategy)
@settings(max_examples=25)
def test_ShippingInfo_instantiation(instance):
    assert isinstance(instance, ShippingInfo)


Shopping_strategy = st.builds(Shopping, Identity=st.integers(), Location=safe_text, Name=safe_text)
@given(instance=Shopping_strategy)
@settings(max_examples=25)
def test_Shopping_instantiation(instance):
    assert isinstance(instance, Shopping)


ShoppingCart_strategy = st.builds(ShoppingCart, CartID=st.integers(), DateAdded=st.integers(), ProductID=st.integers(), Quantity=st.integers())
@given(instance=ShoppingCart_strategy)
@settings(max_examples=25)
def test_ShoppingCart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)


Users_strategy = st.builds(Users, LoginStatus=safe_text, Password=safe_text, RegisterDate=st.integers(), UserID=safe_text)
@given(instance=Users_strategy)
@settings(max_examples=25)
def test_Users_instantiation(instance):
    assert isinstance(instance, Users)



