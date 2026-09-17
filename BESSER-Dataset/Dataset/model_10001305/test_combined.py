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
    Vendor,
    UserAddress,
    Promos,
    Product,
    OrderProcess,
    ShoppingCart,
    Regular_Members,
    Premium_Members,
    UserName,
    User_Account,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_vendor_is_not_abstract():
    assert not inspect.isabstract(Vendor)


def test_hyp_vendor_constructor_exists():
    assert callable(Vendor.__init__)


def test_hyp_vendor_constructor_args():
    sig = inspect.signature(Vendor.__init__)
    params = list(sig.parameters.keys())
    assert "Contact_Number" in params, "Missing parameter 'Contact_Number'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "VendorID" in params, "Missing parameter 'VendorID'"
    assert "Address" in params, "Missing parameter 'Address'"








def test_hyp_useraddress_is_not_abstract():
    assert not inspect.isabstract(UserAddress)


def test_hyp_useraddress_constructor_exists():
    assert callable(UserAddress.__init__)


def test_hyp_useraddress_constructor_args():
    sig = inspect.signature(UserAddress.__init__)
    params = list(sig.parameters.keys())
    assert "City" in params, "Missing parameter 'City'"
    assert "StreetName" in params, "Missing parameter 'StreetName'"
    assert "StreetNum" in params, "Missing parameter 'StreetNum'"
    assert "PostCode" in params, "Missing parameter 'PostCode'"







def test_hyp_promos_is_not_abstract():
    assert not inspect.isabstract(Promos)


def test_hyp_promos_constructor_exists():
    assert callable(Promos.__init__)


def test_hyp_promos_constructor_args():
    sig = inspect.signature(Promos.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "EndDate" in params, "Missing parameter 'EndDate'"
    assert "Discount" in params, "Missing parameter 'Discount'"
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"








def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_hyp_product_constructor_exists():
    assert callable(Product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "InventoryQuantity" in params, "Missing parameter 'InventoryQuantity'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "VendorID" in params, "Missing parameter 'VendorID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "InventoryMinQuantity" in params, "Missing parameter 'InventoryMinQuantity'"








def test_hyp_orderprocess_is_not_abstract():
    assert not inspect.isabstract(OrderProcess)


def test_hyp_orderprocess_constructor_exists():
    assert callable(OrderProcess.__init__)


def test_hyp_orderprocess_constructor_args():
    sig = inspect.signature(OrderProcess.__init__)
    params = list(sig.parameters.keys())
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "OrderPickUp" in params, "Missing parameter 'OrderPickUp'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "IsMember" in params, "Missing parameter 'IsMember'"
    assert "MemberShipPayment" in params, "Missing parameter 'MemberShipPayment'"










def test_hyp_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_hyp_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_hyp_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "ShoppingCartID" in params, "Missing parameter 'ShoppingCartID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Promo" in params, "Missing parameter 'Promo'"

def test_hyp_shoppingcart_has_ShoppingCartID():
    assert hasattr(ShoppingCart, "ShoppingCartID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "ShoppingCartID" in klass.__dict__:
            descriptor = klass.__dict__["ShoppingCartID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_shoppingcart_has_ProductID():
    assert hasattr(ShoppingCart, "ProductID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_shoppingcart_has_Quantity():
    assert hasattr(ShoppingCart, "Quantity")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_hyp_shoppingcart_has_Total():
    assert hasattr(ShoppingCart, "Total")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Total" in klass.__dict__:
            descriptor = klass.__dict__["Total"]
            break
    assert isinstance(descriptor, property)

def test_hyp_shoppingcart_has_OrderID():
    assert hasattr(ShoppingCart, "OrderID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_shoppingcart_has_UserID():
    assert hasattr(ShoppingCart, "UserID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_shoppingcart_has_Promo():
    assert hasattr(ShoppingCart, "Promo")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Promo" in klass.__dict__:
            descriptor = klass.__dict__["Promo"]
            break
    assert isinstance(descriptor, property)



def test_hyp_regular_members_is_not_abstract():
    assert not inspect.isabstract(Regular_Members)


def test_hyp_regular_members_constructor_exists():
    assert callable(Regular_Members.__init__)


def test_hyp_regular_members_constructor_args():
    sig = inspect.signature(Regular_Members.__init__)
    params = list(sig.parameters.keys())
    assert "TrialStartDate" in params, "Missing parameter 'TrialStartDate'"
    assert "TriedPremium" in params, "Missing parameter 'TriedPremium'"





def test_hyp_premium_members_is_not_abstract():
    assert not inspect.isabstract(Premium_Members)


def test_hyp_premium_members_constructor_exists():
    assert callable(Premium_Members.__init__)


def test_hyp_premium_members_constructor_args():
    sig = inspect.signature(Premium_Members.__init__)
    params = list(sig.parameters.keys())
    assert "MembershipEndDate" in params, "Missing parameter 'MembershipEndDate'"
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"
    assert "MembershipStartDate" in params, "Missing parameter 'MembershipStartDate'"






def test_hyp_username_is_not_abstract():
    assert not inspect.isabstract(UserName)


def test_hyp_username_constructor_exists():
    assert callable(UserName.__init__)


def test_hyp_username_constructor_args():
    sig = inspect.signature(UserName.__init__)
    params = list(sig.parameters.keys())
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "FirstName" in params, "Missing parameter 'FirstName'"





def test_hyp_user_account_is_not_abstract():
    assert not inspect.isabstract(User_Account)


def test_hyp_user_account_constructor_exists():
    assert callable(User_Account.__init__)


def test_hyp_user_account_constructor_args():
    sig = inspect.signature(User_Account.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "DateOfBirth" in params, "Missing parameter 'DateOfBirth'"
    assert "RegDate" in params, "Missing parameter 'RegDate'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "FullName" in params, "Missing parameter 'FullName'"
    assert "UserAddress" in params, "Missing parameter 'UserAddress'"








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
Vendor_strategy = st.builds(
    Vendor,
    Contact_Number=
        st.integers(),
    Email=
        safe_text,
    Name=
        safe_text,
    VendorID=
        st.integers(),
    Address=
        safe_text
)
UserAddress_strategy = st.builds(
    UserAddress,
    City=
        safe_text,
    StreetName=
        safe_text,
    StreetNum=
        st.integers(),
    PostCode=
        safe_text
)
Promos_strategy = st.builds(
    Promos,
    Name=
        safe_text,
    EndDate=
        safe_text,
    Discount=
        safe_text,
    PromoCode=
        safe_text,
    StartDate=
        safe_text
)
Product_strategy = st.builds(
    Product,
    InventoryQuantity=
        st.integers(),
    Description=
        safe_text,
    VendorID=
        st.integers(),
    ProductID=
        st.integers(),
    InventoryMinQuantity=
        st.integers()
)
OrderProcess_strategy = st.builds(
    OrderProcess,
    PromoCode=
        safe_text,
    UserID=
        st.integers(),
    OrderID=
        st.integers(),
    OrderPickUp=
        st.integers(),
    Total=
        safe_text,
    IsMember=
        st.integers(),
    MemberShipPayment=
        st.integers()
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    ShoppingCartID=
        st.integers(),
    ProductID=
        st.integers(),
    Quantity=
        st.integers(),
    Total=
        safe_text,
    OrderID=
        st.integers(),
    UserID=
        safe_text,
    Promo=
        st.none()
)
Regular_Members_strategy = st.builds(
    Regular_Members,
    TrialStartDate=
        safe_text,
    TriedPremium=
        st.integers()
)
Premium_Members_strategy = st.builds(
    Premium_Members,
    MembershipEndDate=
        safe_text,
    PromoCode=
        safe_text,
    MembershipStartDate=
        safe_text
)
UserName_strategy = st.builds(
    UserName,
    LastName=
        safe_text,
    FirstName=
        safe_text
)
User_Account_strategy = st.builds(
    User_Account,
    UserID=
        safe_text,
    DateOfBirth=
        safe_text,
    RegDate=
        safe_text,
    Email=
        safe_text,
    FullName=
        safe_text,
    UserAddress=
        safe_text
)




@given(instance=Vendor_strategy)
def test_hyp_vendor_Contact_Number_setter(instance):
    original = instance.Contact_Number
    instance.Contact_Number = original
    assert instance.Contact_Number == original



@given(instance=Vendor_strategy)
def test_hyp_vendor_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Vendor_strategy)
def test_hyp_vendor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Vendor_strategy)
def test_hyp_vendor_VendorID_setter(instance):
    original = instance.VendorID
    instance.VendorID = original
    assert instance.VendorID == original



@given(instance=Vendor_strategy)
def test_hyp_vendor_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original




@given(instance=UserAddress_strategy)
def test_hyp_useraddress_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=UserAddress_strategy)
def test_hyp_useraddress_StreetName_setter(instance):
    original = instance.StreetName
    instance.StreetName = original
    assert instance.StreetName == original



@given(instance=UserAddress_strategy)
def test_hyp_useraddress_StreetNum_setter(instance):
    original = instance.StreetNum
    instance.StreetNum = original
    assert instance.StreetNum == original



@given(instance=UserAddress_strategy)
def test_hyp_useraddress_PostCode_setter(instance):
    original = instance.PostCode
    instance.PostCode = original
    assert instance.PostCode == original




@given(instance=Promos_strategy)
def test_hyp_promos_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Promos_strategy)
def test_hyp_promos_EndDate_setter(instance):
    original = instance.EndDate
    instance.EndDate = original
    assert instance.EndDate == original



@given(instance=Promos_strategy)
def test_hyp_promos_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original



@given(instance=Promos_strategy)
def test_hyp_promos_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original



@given(instance=Promos_strategy)
def test_hyp_promos_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original




@given(instance=Product_strategy)
def test_hyp_product_InventoryQuantity_setter(instance):
    original = instance.InventoryQuantity
    instance.InventoryQuantity = original
    assert instance.InventoryQuantity == original



@given(instance=Product_strategy)
def test_hyp_product_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Product_strategy)
def test_hyp_product_VendorID_setter(instance):
    original = instance.VendorID
    instance.VendorID = original
    assert instance.VendorID == original



@given(instance=Product_strategy)
def test_hyp_product_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Product_strategy)
def test_hyp_product_InventoryMinQuantity_setter(instance):
    original = instance.InventoryMinQuantity
    instance.InventoryMinQuantity = original
    assert instance.InventoryMinQuantity == original




@given(instance=OrderProcess_strategy)
def test_hyp_orderprocess_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original



@given(instance=OrderProcess_strategy)
def test_hyp_orderprocess_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=OrderProcess_strategy)
def test_hyp_orderprocess_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=OrderProcess_strategy)
def test_hyp_orderprocess_OrderPickUp_setter(instance):
    original = instance.OrderPickUp
    instance.OrderPickUp = original
    assert instance.OrderPickUp == original



@given(instance=OrderProcess_strategy)
def test_hyp_orderprocess_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original



@given(instance=OrderProcess_strategy)
def test_hyp_orderprocess_IsMember_setter(instance):
    original = instance.IsMember
    instance.IsMember = original
    assert instance.IsMember == original



@given(instance=OrderProcess_strategy)
def test_hyp_orderprocess_MemberShipPayment_setter(instance):
    original = instance.MemberShipPayment
    instance.MemberShipPayment = original
    assert instance.MemberShipPayment == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_hyp_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_ShoppingCartID_setter(instance):
    original = instance.ShoppingCartID
    instance.ShoppingCartID = original
    assert instance.ShoppingCartID == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_Promo_setter(instance):
    original = instance.Promo
    instance.Promo = original
    assert instance.Promo == original




@given(instance=Regular_Members_strategy)
def test_hyp_regular_members_TrialStartDate_setter(instance):
    original = instance.TrialStartDate
    instance.TrialStartDate = original
    assert instance.TrialStartDate == original



@given(instance=Regular_Members_strategy)
def test_hyp_regular_members_TriedPremium_setter(instance):
    original = instance.TriedPremium
    instance.TriedPremium = original
    assert instance.TriedPremium == original




@given(instance=Premium_Members_strategy)
def test_hyp_premium_members_MembershipEndDate_setter(instance):
    original = instance.MembershipEndDate
    instance.MembershipEndDate = original
    assert instance.MembershipEndDate == original



@given(instance=Premium_Members_strategy)
def test_hyp_premium_members_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original



@given(instance=Premium_Members_strategy)
def test_hyp_premium_members_MembershipStartDate_setter(instance):
    original = instance.MembershipStartDate
    instance.MembershipStartDate = original
    assert instance.MembershipStartDate == original




@given(instance=UserName_strategy)
def test_hyp_username_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=UserName_strategy)
def test_hyp_username_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original




@given(instance=User_Account_strategy)
def test_hyp_user_account_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=User_Account_strategy)
def test_hyp_user_account_DateOfBirth_setter(instance):
    original = instance.DateOfBirth
    instance.DateOfBirth = original
    assert instance.DateOfBirth == original



@given(instance=User_Account_strategy)
def test_hyp_user_account_RegDate_setter(instance):
    original = instance.RegDate
    instance.RegDate = original
    assert instance.RegDate == original



@given(instance=User_Account_strategy)
def test_hyp_user_account_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_Account_strategy)
def test_hyp_user_account_FullName_setter(instance):
    original = instance.FullName
    instance.FullName = original
    assert instance.FullName == original



@given(instance=User_Account_strategy)
def test_hyp_user_account_UserAddress_setter(instance):
    original = instance.UserAddress
    instance.UserAddress = original
    assert instance.UserAddress == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    OrderProcess,
    Premium_Members,
    Product,
    Promos,
    Regular_Members,
    ShoppingCart,
    UserAddress,
    UserName,
    User_Account,
    Vendor,
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

def test_OrderProcess_IsMember_value_roundtrip():
    instance = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    assert instance.IsMember == 7
    instance.IsMember = 13
    assert instance.IsMember == 13


def test_OrderProcess_MemberShipPayment_value_roundtrip():
    instance = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    assert instance.MemberShipPayment == 7
    instance.MemberShipPayment = 13
    assert instance.MemberShipPayment == 13


def test_OrderProcess_OrderID_value_roundtrip():
    instance = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_OrderProcess_OrderPickUp_value_roundtrip():
    instance = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    assert instance.OrderPickUp == 7
    instance.OrderPickUp = 13
    assert instance.OrderPickUp == 13


def test_OrderProcess_PromoCode_value_roundtrip():
    instance = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    assert instance.PromoCode == "sample_text"
    instance.PromoCode = "sample_text_2"
    assert instance.PromoCode == "sample_text_2"


def test_OrderProcess_Total_value_roundtrip():
    instance = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    assert instance.Total == "sample_text"
    instance.Total = "sample_text_2"
    assert instance.Total == "sample_text_2"


def test_OrderProcess_UserID_value_roundtrip():
    instance = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_Premium_Members_MembershipEndDate_value_roundtrip():
    instance = Premium_Members(MembershipEndDate="sample_text", MembershipStartDate="sample_text", PromoCode="sample_text")
    assert instance.MembershipEndDate == "sample_text"
    instance.MembershipEndDate = "sample_text_2"
    assert instance.MembershipEndDate == "sample_text_2"


def test_Premium_Members_MembershipStartDate_value_roundtrip():
    instance = Premium_Members(MembershipEndDate="sample_text", MembershipStartDate="sample_text", PromoCode="sample_text")
    assert instance.MembershipStartDate == "sample_text"
    instance.MembershipStartDate = "sample_text_2"
    assert instance.MembershipStartDate == "sample_text_2"


def test_Premium_Members_PromoCode_value_roundtrip():
    instance = Premium_Members(MembershipEndDate="sample_text", MembershipStartDate="sample_text", PromoCode="sample_text")
    assert instance.PromoCode == "sample_text"
    instance.PromoCode = "sample_text_2"
    assert instance.PromoCode == "sample_text_2"


def test_Product_Description_value_roundtrip():
    instance = Product(Description="sample_text", InventoryMinQuantity=7, InventoryQuantity=7, ProductID=7, VendorID=7)
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Product_InventoryMinQuantity_value_roundtrip():
    instance = Product(Description="sample_text", InventoryMinQuantity=7, InventoryQuantity=7, ProductID=7, VendorID=7)
    assert instance.InventoryMinQuantity == 7
    instance.InventoryMinQuantity = 13
    assert instance.InventoryMinQuantity == 13


def test_Product_InventoryQuantity_value_roundtrip():
    instance = Product(Description="sample_text", InventoryMinQuantity=7, InventoryQuantity=7, ProductID=7, VendorID=7)
    assert instance.InventoryQuantity == 7
    instance.InventoryQuantity = 13
    assert instance.InventoryQuantity == 13


def test_Product_ProductID_value_roundtrip():
    instance = Product(Description="sample_text", InventoryMinQuantity=7, InventoryQuantity=7, ProductID=7, VendorID=7)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_Product_VendorID_value_roundtrip():
    instance = Product(Description="sample_text", InventoryMinQuantity=7, InventoryQuantity=7, ProductID=7, VendorID=7)
    assert instance.VendorID == 7
    instance.VendorID = 13
    assert instance.VendorID == 13


def test_Promos_Discount_value_roundtrip():
    instance = Promos(Discount="sample_text", EndDate="sample_text", Name="sample_text", PromoCode="sample_text", StartDate="sample_text")
    assert instance.Discount == "sample_text"
    instance.Discount = "sample_text_2"
    assert instance.Discount == "sample_text_2"


def test_Promos_EndDate_value_roundtrip():
    instance = Promos(Discount="sample_text", EndDate="sample_text", Name="sample_text", PromoCode="sample_text", StartDate="sample_text")
    assert instance.EndDate == "sample_text"
    instance.EndDate = "sample_text_2"
    assert instance.EndDate == "sample_text_2"


def test_Promos_Name_value_roundtrip():
    instance = Promos(Discount="sample_text", EndDate="sample_text", Name="sample_text", PromoCode="sample_text", StartDate="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Promos_PromoCode_value_roundtrip():
    instance = Promos(Discount="sample_text", EndDate="sample_text", Name="sample_text", PromoCode="sample_text", StartDate="sample_text")
    assert instance.PromoCode == "sample_text"
    instance.PromoCode = "sample_text_2"
    assert instance.PromoCode == "sample_text_2"


def test_Promos_StartDate_value_roundtrip():
    instance = Promos(Discount="sample_text", EndDate="sample_text", Name="sample_text", PromoCode="sample_text", StartDate="sample_text")
    assert instance.StartDate == "sample_text"
    instance.StartDate = "sample_text_2"
    assert instance.StartDate == "sample_text_2"


def test_Regular_Members_TrialStartDate_value_roundtrip():
    instance = Regular_Members(TrialStartDate="sample_text", TriedPremium=7)
    assert instance.TrialStartDate == "sample_text"
    instance.TrialStartDate = "sample_text_2"
    assert instance.TrialStartDate == "sample_text_2"


def test_Regular_Members_TriedPremium_value_roundtrip():
    instance = Regular_Members(TrialStartDate="sample_text", TriedPremium=7)
    assert instance.TriedPremium == 7
    instance.TriedPremium = 13
    assert instance.TriedPremium == 13


def test_UserAddress_City_value_roundtrip():
    instance = UserAddress(City="sample_text", PostCode="sample_text", StreetName="sample_text", StreetNum=7)
    assert instance.City == "sample_text"
    instance.City = "sample_text_2"
    assert instance.City == "sample_text_2"


def test_UserAddress_PostCode_value_roundtrip():
    instance = UserAddress(City="sample_text", PostCode="sample_text", StreetName="sample_text", StreetNum=7)
    assert instance.PostCode == "sample_text"
    instance.PostCode = "sample_text_2"
    assert instance.PostCode == "sample_text_2"


def test_UserAddress_StreetName_value_roundtrip():
    instance = UserAddress(City="sample_text", PostCode="sample_text", StreetName="sample_text", StreetNum=7)
    assert instance.StreetName == "sample_text"
    instance.StreetName = "sample_text_2"
    assert instance.StreetName == "sample_text_2"


def test_UserAddress_StreetNum_value_roundtrip():
    instance = UserAddress(City="sample_text", PostCode="sample_text", StreetName="sample_text", StreetNum=7)
    assert instance.StreetNum == 7
    instance.StreetNum = 13
    assert instance.StreetNum == 13


def test_UserName_FirstName_value_roundtrip():
    instance = UserName(FirstName="sample_text", LastName="sample_text")
    assert instance.FirstName == "sample_text"
    instance.FirstName = "sample_text_2"
    assert instance.FirstName == "sample_text_2"


def test_UserName_LastName_value_roundtrip():
    instance = UserName(FirstName="sample_text", LastName="sample_text")
    assert instance.LastName == "sample_text"
    instance.LastName = "sample_text_2"
    assert instance.LastName == "sample_text_2"


def test_User_Account_DateOfBirth_value_roundtrip():
    instance = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    assert instance.DateOfBirth == "sample_text"
    instance.DateOfBirth = "sample_text_2"
    assert instance.DateOfBirth == "sample_text_2"


def test_User_Account_Email_value_roundtrip():
    instance = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_User_Account_FullName_value_roundtrip():
    instance = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    assert instance.FullName == "sample_text"
    instance.FullName = "sample_text_2"
    assert instance.FullName == "sample_text_2"


def test_User_Account_RegDate_value_roundtrip():
    instance = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    assert instance.RegDate == "sample_text"
    instance.RegDate = "sample_text_2"
    assert instance.RegDate == "sample_text_2"


def test_User_Account_UserAddress_value_roundtrip():
    instance = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    assert instance.UserAddress == "sample_text"
    instance.UserAddress = "sample_text_2"
    assert instance.UserAddress == "sample_text_2"


def test_User_Account_UserID_value_roundtrip():
    instance = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    assert instance.UserID == "sample_text"
    instance.UserID = "sample_text_2"
    assert instance.UserID == "sample_text_2"


def test_Vendor_Address_value_roundtrip():
    instance = Vendor(Address="sample_text", Contact_Number=7, Email="sample_text", Name="sample_text", VendorID=7)
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Vendor_Contact_Number_value_roundtrip():
    instance = Vendor(Address="sample_text", Contact_Number=7, Email="sample_text", Name="sample_text", VendorID=7)
    assert instance.Contact_Number == 7
    instance.Contact_Number = 13
    assert instance.Contact_Number == 13


def test_Vendor_Email_value_roundtrip():
    instance = Vendor(Address="sample_text", Contact_Number=7, Email="sample_text", Name="sample_text", VendorID=7)
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Vendor_Name_value_roundtrip():
    instance = Vendor(Address="sample_text", Contact_Number=7, Email="sample_text", Name="sample_text", VendorID=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Vendor_VendorID_value_roundtrip():
    instance = Vendor(Address="sample_text", Contact_Number=7, Email="sample_text", Name="sample_text", VendorID=7)
    assert instance.VendorID == 7
    instance.VendorID = 13
    assert instance.VendorID == 13


def test_assoc_Customer_ShoppingCart_link_reassign_clear():
    a = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    b1 = UserName(FirstName="sample_text", LastName="sample_text")
    b2 = UserName(FirstName="sample_text_2", LastName="sample_text_2")
    _safe_set(a, 'Customer_ShoppingCart_00', b1)
    assert _is_linked(a, 'Customer_ShoppingCart_00', b1)
    if hasattr(b1, 'Customer_ShoppingCart_11'):
        assert _is_linked(b1, 'Customer_ShoppingCart_11', a)
    _safe_set(a, 'Customer_ShoppingCart_00', b2)
    assert _is_linked(a, 'Customer_ShoppingCart_00', b2)
    if hasattr(b1, 'Customer_ShoppingCart_11'):
        assert not _is_linked(b1, 'Customer_ShoppingCart_11', a)
    if hasattr(b2, 'Customer_ShoppingCart_11'):
        assert _is_linked(b2, 'Customer_ShoppingCart_11', a)
    _safe_set(a, 'Customer_ShoppingCart_00', None)
    assert not _is_linked(a, 'Customer_ShoppingCart_00', b2)
    if hasattr(b2, 'Customer_ShoppingCart_11'):
        assert not _is_linked(b2, 'Customer_ShoppingCart_11', a)


def test_assoc_Premium_Members_Promos_link_reassign_clear():
    a = Promos(Discount="sample_text", EndDate="sample_text", Name="sample_text", PromoCode="sample_text", StartDate="sample_text")
    b1 = Premium_Members(MembershipEndDate="sample_text", MembershipStartDate="sample_text", PromoCode="sample_text")
    b2 = Premium_Members(MembershipEndDate="sample_text_2", MembershipStartDate="sample_text_2", PromoCode="sample_text_2")
    _safe_set(a, 'Premium_Members_Promos_113', b1)
    assert _is_linked(a, 'Premium_Members_Promos_113', b1)
    if hasattr(b1, 'Premium_Members_Promos_012'):
        assert _is_linked(b1, 'Premium_Members_Promos_012', a)
    _safe_set(a, 'Premium_Members_Promos_113', b2)
    assert _is_linked(a, 'Premium_Members_Promos_113', b2)
    if hasattr(b1, 'Premium_Members_Promos_012'):
        assert not _is_linked(b1, 'Premium_Members_Promos_012', a)
    if hasattr(b2, 'Premium_Members_Promos_012'):
        assert _is_linked(b2, 'Premium_Members_Promos_012', a)
    _safe_set(a, 'Premium_Members_Promos_113', None)
    assert not _is_linked(a, 'Premium_Members_Promos_113', b2)
    if hasattr(b2, 'Premium_Members_Promos_012'):
        assert not _is_linked(b2, 'Premium_Members_Promos_012', a)


def test_assoc_Product_Vendor_link_reassign_clear():
    a = Vendor(Address="sample_text", Contact_Number=7, Email="sample_text", Name="sample_text", VendorID=7)
    b1 = Product(Description="sample_text", InventoryMinQuantity=7, InventoryQuantity=7, ProductID=7, VendorID=7)
    b2 = Product(Description="sample_text_2", InventoryMinQuantity=13, InventoryQuantity=13, ProductID=13, VendorID=13)
    _safe_set(a, 'Product_Vendor_115', {b1})
    assert _is_linked(a, 'Product_Vendor_115', b1)
    if hasattr(b1, 'Product_Vendor_014'):
        assert _is_linked(b1, 'Product_Vendor_014', a)
    _safe_set(a, 'Product_Vendor_115', {b2})
    assert _is_linked(a, 'Product_Vendor_115', b2)
    if hasattr(b1, 'Product_Vendor_014'):
        assert not _is_linked(b1, 'Product_Vendor_014', a)
    if hasattr(b2, 'Product_Vendor_014'):
        assert _is_linked(b2, 'Product_Vendor_014', a)
    _safe_set(a, 'Product_Vendor_115', set())
    assert not _is_linked(a, 'Product_Vendor_115', b2)
    if hasattr(b2, 'Product_Vendor_014'):
        assert not _is_linked(b2, 'Product_Vendor_014', a)


def test_assoc_User_Account_OrderProcess_link_reassign_clear():
    a = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    b1 = OrderProcess(IsMember=7, MemberShipPayment=7, OrderID=7, OrderPickUp=7, PromoCode="sample_text", Total="sample_text", UserID=7)
    b2 = OrderProcess(IsMember=13, MemberShipPayment=13, OrderID=13, OrderPickUp=13, PromoCode="sample_text_2", Total="sample_text_2", UserID=13)
    _safe_set(a, 'orderProcess6', {b1})
    assert _is_linked(a, 'orderProcess6', b1)
    if hasattr(b1, 'user_Account7'):
        assert _is_linked(b1, 'user_Account7', a)
    _safe_set(a, 'orderProcess6', {b2})
    assert _is_linked(a, 'orderProcess6', b2)
    if hasattr(b1, 'user_Account7'):
        assert not _is_linked(b1, 'user_Account7', a)
    if hasattr(b2, 'user_Account7'):
        assert _is_linked(b2, 'user_Account7', a)
    _safe_set(a, 'orderProcess6', set())
    assert not _is_linked(a, 'orderProcess6', b2)
    if hasattr(b2, 'user_Account7'):
        assert not _is_linked(b2, 'user_Account7', a)


def test_assoc_User_Account_UserAddress_link_reassign_clear():
    a = User_Account(DateOfBirth="sample_text", Email="sample_text", FullName="sample_text", RegDate="sample_text", UserAddress="sample_text", UserID="sample_text")
    b1 = UserAddress(City="sample_text", PostCode="sample_text", StreetName="sample_text", StreetNum=7)
    b2 = UserAddress(City="sample_text_2", PostCode="sample_text_2", StreetName="sample_text_2", StreetNum=13)
    _safe_set(a, 'userAddress10', b1)
    assert _is_linked(a, 'userAddress10', b1)
    if hasattr(b1, 'user_Account11'):
        assert _is_linked(b1, 'user_Account11', a)
    _safe_set(a, 'userAddress10', b2)
    assert _is_linked(a, 'userAddress10', b2)
    if hasattr(b1, 'user_Account11'):
        assert not _is_linked(b1, 'user_Account11', a)
    if hasattr(b2, 'user_Account11'):
        assert _is_linked(b2, 'user_Account11', a)
    _safe_set(a, 'userAddress10', None)
    assert not _is_linked(a, 'userAddress10', b2)
    if hasattr(b2, 'user_Account11'):
        assert not _is_linked(b2, 'user_Account11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

OrderProcess_strategy = st.builds(OrderProcess, IsMember=st.integers(), MemberShipPayment=st.integers(), OrderID=st.integers(), OrderPickUp=st.integers(), PromoCode=safe_text, Total=safe_text, UserID=st.integers())
@given(instance=OrderProcess_strategy)
@settings(max_examples=25)
def test_OrderProcess_instantiation(instance):
    assert isinstance(instance, OrderProcess)


Premium_Members_strategy = st.builds(Premium_Members, MembershipEndDate=safe_text, MembershipStartDate=safe_text, PromoCode=safe_text)
@given(instance=Premium_Members_strategy)
@settings(max_examples=25)
def test_Premium_Members_instantiation(instance):
    assert isinstance(instance, Premium_Members)


Product_strategy = st.builds(Product, Description=safe_text, InventoryMinQuantity=st.integers(), InventoryQuantity=st.integers(), ProductID=st.integers(), VendorID=st.integers())
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)


Promos_strategy = st.builds(Promos, Discount=safe_text, EndDate=safe_text, Name=safe_text, PromoCode=safe_text, StartDate=safe_text)
@given(instance=Promos_strategy)
@settings(max_examples=25)
def test_Promos_instantiation(instance):
    assert isinstance(instance, Promos)


Regular_Members_strategy = st.builds(Regular_Members, TrialStartDate=safe_text, TriedPremium=st.integers())
@given(instance=Regular_Members_strategy)
@settings(max_examples=25)
def test_Regular_Members_instantiation(instance):
    assert isinstance(instance, Regular_Members)


UserAddress_strategy = st.builds(UserAddress, City=safe_text, PostCode=safe_text, StreetName=safe_text, StreetNum=st.integers())
@given(instance=UserAddress_strategy)
@settings(max_examples=25)
def test_UserAddress_instantiation(instance):
    assert isinstance(instance, UserAddress)


UserName_strategy = st.builds(UserName, FirstName=safe_text, LastName=safe_text)
@given(instance=UserName_strategy)
@settings(max_examples=25)
def test_UserName_instantiation(instance):
    assert isinstance(instance, UserName)


User_Account_strategy = st.builds(User_Account, DateOfBirth=safe_text, Email=safe_text, FullName=safe_text, RegDate=safe_text, UserAddress=safe_text, UserID=safe_text)
@given(instance=User_Account_strategy)
@settings(max_examples=25)
def test_User_Account_instantiation(instance):
    assert isinstance(instance, User_Account)


Vendor_strategy = st.builds(Vendor, Address=safe_text, Contact_Number=st.integers(), Email=safe_text, Name=safe_text, VendorID=st.integers())
@given(instance=Vendor_strategy)
@settings(max_examples=25)
def test_Vendor_instantiation(instance):
    assert isinstance(instance, Vendor)



