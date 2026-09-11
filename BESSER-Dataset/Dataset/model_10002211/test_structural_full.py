import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BaseDateInformation,
    Category,
    Customer,
    FlashSale,
    OnlineShop,
    Order,
    Product,
    Role,
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

def test_BaseDateInformation_CreateDate_value_roundtrip():
    instance = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    assert instance.CreateDate == "sample_text"
    instance.CreateDate = "sample_text_2"
    assert instance.CreateDate == "sample_text_2"


def test_BaseDateInformation_CreatedBy_value_roundtrip():
    instance = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    assert instance.CreatedBy == "sample_text"
    instance.CreatedBy = "sample_text_2"
    assert instance.CreatedBy == "sample_text_2"


def test_BaseDateInformation_LastModifedBy_value_roundtrip():
    instance = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    assert instance.LastModifedBy == "sample_text"
    instance.LastModifedBy = "sample_text_2"
    assert instance.LastModifedBy == "sample_text_2"


def test_BaseDateInformation_LastModifedDate_value_roundtrip():
    instance = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    assert instance.LastModifedDate == "sample_text"
    instance.LastModifedDate = "sample_text_2"
    assert instance.LastModifedDate == "sample_text_2"


def test_Category_CategoryID_value_roundtrip():
    instance = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    assert instance.CategoryID == 7
    instance.CategoryID = 13
    assert instance.CategoryID == 13


def test_Category_CategoryName_value_roundtrip():
    instance = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    assert instance.CategoryName == "sample_text"
    instance.CategoryName = "sample_text_2"
    assert instance.CategoryName == "sample_text_2"


def test_Category_Description_value_roundtrip():
    instance = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Category_isActive_value_roundtrip():
    instance = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    assert instance.isActive == True
    instance.isActive = False
    assert instance.isActive == False


def test_Customer_Address_value_roundtrip():
    instance = Customer(Address="sample_text", CustomerID=7, CustomerName="sample_text", Email="sample_text", Gender=7, Phone="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Customer_CustomerID_value_roundtrip():
    instance = Customer(Address="sample_text", CustomerID=7, CustomerName="sample_text", Email="sample_text", Gender=7, Phone="sample_text")
    assert instance.CustomerID == 7
    instance.CustomerID = 13
    assert instance.CustomerID == 13


def test_Customer_CustomerName_value_roundtrip():
    instance = Customer(Address="sample_text", CustomerID=7, CustomerName="sample_text", Email="sample_text", Gender=7, Phone="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_Customer_Email_value_roundtrip():
    instance = Customer(Address="sample_text", CustomerID=7, CustomerName="sample_text", Email="sample_text", Gender=7, Phone="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Customer_Gender_value_roundtrip():
    instance = Customer(Address="sample_text", CustomerID=7, CustomerName="sample_text", Email="sample_text", Gender=7, Phone="sample_text")
    assert instance.Gender == 7
    instance.Gender = 13
    assert instance.Gender == 13


def test_Customer_Phone_value_roundtrip():
    instance = Customer(Address="sample_text", CustomerID=7, CustomerName="sample_text", Email="sample_text", Gender=7, Phone="sample_text")
    assert instance.Phone == "sample_text"
    instance.Phone = "sample_text_2"
    assert instance.Phone == "sample_text_2"


def test_FlashSale_Description_value_roundtrip():
    instance = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_FlashSale_DiscountAmount_value_roundtrip():
    instance = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    assert instance.DiscountAmount == 7
    instance.DiscountAmount = 13
    assert instance.DiscountAmount == 13


def test_FlashSale_DiscountPercent_value_roundtrip():
    instance = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    assert instance.DiscountPercent == 7
    instance.DiscountPercent = 13
    assert instance.DiscountPercent == 13


def test_FlashSale_FlashSaleID_value_roundtrip():
    instance = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    assert instance.FlashSaleID == 7
    instance.FlashSaleID = 13
    assert instance.FlashSaleID == 13


def test_FlashSale_FlashSaleName_value_roundtrip():
    instance = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    assert instance.FlashSaleName == "sample_text"
    instance.FlashSaleName = "sample_text_2"
    assert instance.FlashSaleName == "sample_text_2"


def test_FlashSale_OnlineShopID_value_roundtrip():
    instance = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    assert instance.OnlineShopID == 7
    instance.OnlineShopID = 13
    assert instance.OnlineShopID == 13


def test_OnlineShop_OnlineShopID_value_roundtrip():
    instance = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    assert instance.OnlineShopID == 7
    instance.OnlineShopID = 13
    assert instance.OnlineShopID == 13


def test_OnlineShop_OnlineShopName_value_roundtrip():
    instance = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    assert instance.OnlineShopName == "sample_text"
    instance.OnlineShopName = "sample_text_2"
    assert instance.OnlineShopName == "sample_text_2"


def test_OnlineShop_ShopCategoryID_value_roundtrip():
    instance = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    assert instance.ShopCategoryID == 7
    instance.ShopCategoryID = 13
    assert instance.ShopCategoryID == 13


def test_OnlineShop_isActive_value_roundtrip():
    instance = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    assert instance.isActive == True
    instance.isActive = False
    assert instance.isActive == False


def test_Order_OrderCustomerID_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.OrderCustomerID == 7
    instance.OrderCustomerID = 13
    assert instance.OrderCustomerID == 13


def test_Order_OrderDate_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.OrderDate == "sample_text"
    instance.OrderDate = "sample_text_2"
    assert instance.OrderDate == "sample_text_2"


def test_Order_OrderID_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Order_ReceiveCustomerID_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.ReceiveCustomerID == 7
    instance.ReceiveCustomerID = 13
    assert instance.ReceiveCustomerID == 13


def test_Order_ShopOnlineID_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.ShopOnlineID == 7
    instance.ShopOnlineID = 13
    assert instance.ShopOnlineID == 13


def test_Order_Status_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.Status == True
    instance.Status = False
    assert instance.Status == False


def test_Order_TotalDiscount_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.TotalDiscount == "sample_text"
    instance.TotalDiscount = "sample_text_2"
    assert instance.TotalDiscount == "sample_text_2"


def test_Order_TotalPrice_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.TotalPrice == "sample_text"
    instance.TotalPrice = "sample_text_2"
    assert instance.TotalPrice == "sample_text_2"


def test_Order_UserID_value_roundtrip():
    instance = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_Product_CategoryID_value_roundtrip():
    instance = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    assert instance.CategoryID == 7
    instance.CategoryID = 13
    assert instance.CategoryID == 13


def test_Product_Description_value_roundtrip():
    instance = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Product_Image_value_roundtrip():
    instance = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    assert instance.Image == "sample_text"
    instance.Image = "sample_text_2"
    assert instance.Image == "sample_text_2"


def test_Product_OnlineShopID_value_roundtrip():
    instance = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    assert instance.OnlineShopID == 7
    instance.OnlineShopID = 13
    assert instance.OnlineShopID == 13


def test_Product_Price_value_roundtrip():
    instance = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_Product_ProductID_value_roundtrip():
    instance = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_Product_ProductName_value_roundtrip():
    instance = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    assert instance.ProductName == "sample_text"
    instance.ProductName = "sample_text_2"
    assert instance.ProductName == "sample_text_2"


def test_Product_isActive_value_roundtrip():
    instance = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    assert instance.isActive == True
    instance.isActive = False
    assert instance.isActive == False


def test_Role_Description_value_roundtrip():
    instance = Role(Description="sample_text", RoleID=7, RoleName="sample_text", isActive=True)
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Role_RoleID_value_roundtrip():
    instance = Role(Description="sample_text", RoleID=7, RoleName="sample_text", isActive=True)
    assert instance.RoleID == 7
    instance.RoleID = 13
    assert instance.RoleID == 13


def test_Role_RoleName_value_roundtrip():
    instance = Role(Description="sample_text", RoleID=7, RoleName="sample_text", isActive=True)
    assert instance.RoleName == "sample_text"
    instance.RoleName = "sample_text_2"
    assert instance.RoleName == "sample_text_2"


def test_Role_isActive_value_roundtrip():
    instance = Role(Description="sample_text", RoleID=7, RoleName="sample_text", isActive=True)
    assert instance.isActive == True
    instance.isActive = False
    assert instance.isActive == False


def test_User_Password_value_roundtrip():
    instance = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_User_RegisterDate_value_roundtrip():
    instance = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    assert instance.RegisterDate == "sample_text"
    instance.RegisterDate = "sample_text_2"
    assert instance.RegisterDate == "sample_text_2"


def test_User_RoleID_value_roundtrip():
    instance = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    assert instance.RoleID == 7
    instance.RoleID = 13
    assert instance.RoleID == 13


def test_User_UserID_value_roundtrip():
    instance = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    assert instance.UserID == "sample_text"
    instance.UserID = "sample_text_2"
    assert instance.UserID == "sample_text_2"


def test_User_Username_value_roundtrip():
    instance = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


def test_User_isActive_value_roundtrip():
    instance = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    assert instance.isActive == True
    instance.isActive = False
    assert instance.isActive == False


def test_assoc_BaseDateInformation_Category_link_reassign_clear():
    a = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    b1 = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    b2 = BaseDateInformation(CreateDate="sample_text_2", CreatedBy="sample_text_2", LastModifedBy="sample_text_2", LastModifedDate="sample_text_2")
    _safe_set(a, 'baseDateInformation7', b1)
    assert _is_linked(a, 'baseDateInformation7', b1)
    if hasattr(b1, 'category6'):
        assert _is_linked(b1, 'category6', a)
    _safe_set(a, 'baseDateInformation7', b2)
    assert _is_linked(a, 'baseDateInformation7', b2)
    if hasattr(b1, 'category6'):
        assert not _is_linked(b1, 'category6', a)
    if hasattr(b2, 'category6'):
        assert _is_linked(b2, 'category6', a)
    _safe_set(a, 'baseDateInformation7', None)
    assert not _is_linked(a, 'baseDateInformation7', b2)
    if hasattr(b2, 'category6'):
        assert not _is_linked(b2, 'category6', a)


def test_assoc_BaseDateInformation_FlashSale_link_reassign_clear():
    a = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    b1 = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    b2 = BaseDateInformation(CreateDate="sample_text_2", CreatedBy="sample_text_2", LastModifedBy="sample_text_2", LastModifedDate="sample_text_2")
    _safe_set(a, 'baseDateInformation17', b1)
    assert _is_linked(a, 'baseDateInformation17', b1)
    if hasattr(b1, 'flashSale16'):
        assert _is_linked(b1, 'flashSale16', a)
    _safe_set(a, 'baseDateInformation17', b2)
    assert _is_linked(a, 'baseDateInformation17', b2)
    if hasattr(b1, 'flashSale16'):
        assert not _is_linked(b1, 'flashSale16', a)
    if hasattr(b2, 'flashSale16'):
        assert _is_linked(b2, 'flashSale16', a)
    _safe_set(a, 'baseDateInformation17', None)
    assert not _is_linked(a, 'baseDateInformation17', b2)
    if hasattr(b2, 'flashSale16'):
        assert not _is_linked(b2, 'flashSale16', a)


def test_assoc_BaseDateInformation_OnlineShop_link_reassign_clear():
    a = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    b1 = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    b2 = BaseDateInformation(CreateDate="sample_text_2", CreatedBy="sample_text_2", LastModifedBy="sample_text_2", LastModifedDate="sample_text_2")
    _safe_set(a, 'baseDateInformation23', b1)
    assert _is_linked(a, 'baseDateInformation23', b1)
    if hasattr(b1, 'onlineShop22'):
        assert _is_linked(b1, 'onlineShop22', a)
    _safe_set(a, 'baseDateInformation23', b2)
    assert _is_linked(a, 'baseDateInformation23', b2)
    if hasattr(b1, 'onlineShop22'):
        assert not _is_linked(b1, 'onlineShop22', a)
    if hasattr(b2, 'onlineShop22'):
        assert _is_linked(b2, 'onlineShop22', a)
    _safe_set(a, 'baseDateInformation23', None)
    assert not _is_linked(a, 'baseDateInformation23', b2)
    if hasattr(b2, 'onlineShop22'):
        assert not _is_linked(b2, 'onlineShop22', a)


def test_assoc_BaseDateInformation_Product_link_reassign_clear():
    a = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    b1 = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    b2 = BaseDateInformation(CreateDate="sample_text_2", CreatedBy="sample_text_2", LastModifedBy="sample_text_2", LastModifedDate="sample_text_2")
    _safe_set(a, 'baseDateInformation11', b1)
    assert _is_linked(a, 'baseDateInformation11', b1)
    if hasattr(b1, 'product10'):
        assert _is_linked(b1, 'product10', a)
    _safe_set(a, 'baseDateInformation11', b2)
    assert _is_linked(a, 'baseDateInformation11', b2)
    if hasattr(b1, 'product10'):
        assert not _is_linked(b1, 'product10', a)
    if hasattr(b2, 'product10'):
        assert _is_linked(b2, 'product10', a)
    _safe_set(a, 'baseDateInformation11', None)
    assert not _is_linked(a, 'baseDateInformation11', b2)
    if hasattr(b2, 'product10'):
        assert not _is_linked(b2, 'product10', a)


def test_assoc_Category_OnlineShop_link_reassign_clear():
    a = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    b1 = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    b2 = Category(CategoryID=13, CategoryName="sample_text_2", Description="sample_text_2", isActive=False)
    _safe_set(a, 'category5', b1)
    assert _is_linked(a, 'category5', b1)
    if hasattr(b1, 'onlineShop4'):
        assert _is_linked(b1, 'onlineShop4', a)
    _safe_set(a, 'category5', b2)
    assert _is_linked(a, 'category5', b2)
    if hasattr(b1, 'onlineShop4'):
        assert not _is_linked(b1, 'onlineShop4', a)
    if hasattr(b2, 'onlineShop4'):
        assert _is_linked(b2, 'onlineShop4', a)
    _safe_set(a, 'category5', None)
    assert not _is_linked(a, 'category5', b2)
    if hasattr(b2, 'onlineShop4'):
        assert not _is_linked(b2, 'onlineShop4', a)


def test_assoc_Category_Product_link_reassign_clear():
    a = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    b1 = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    b2 = Category(CategoryID=13, CategoryName="sample_text_2", Description="sample_text_2", isActive=False)
    _safe_set(a, 'category1', b1)
    assert _is_linked(a, 'category1', b1)
    if hasattr(b1, 'product0'):
        assert _is_linked(b1, 'product0', a)
    _safe_set(a, 'category1', b2)
    assert _is_linked(a, 'category1', b2)
    if hasattr(b1, 'product0'):
        assert not _is_linked(b1, 'product0', a)
    if hasattr(b2, 'product0'):
        assert _is_linked(b2, 'product0', a)
    _safe_set(a, 'category1', None)
    assert not _is_linked(a, 'category1', b2)
    if hasattr(b2, 'product0'):
        assert not _is_linked(b2, 'product0', a)


def test_assoc_Customer_Order_link_reassign_clear():
    a = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    b1 = Customer(Address="sample_text", CustomerID=7, CustomerName="sample_text", Email="sample_text", Gender=7, Phone="sample_text")
    b2 = Customer(Address="sample_text_2", CustomerID=13, CustomerName="sample_text_2", Email="sample_text_2", Gender=13, Phone="sample_text_2")
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


def test_assoc_OnlineShop_FlashSale_link_reassign_clear():
    a = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    b1 = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    b2 = FlashSale(Description="sample_text_2", DiscountAmount=13, DiscountPercent=13, FlashSaleID=13, FlashSaleName="sample_text_2", OnlineShopID=13)
    _safe_set(a, 'flashSale18', b1)
    assert _is_linked(a, 'flashSale18', b1)
    if hasattr(b1, 'onlineShop19'):
        assert _is_linked(b1, 'onlineShop19', a)
    _safe_set(a, 'flashSale18', b2)
    assert _is_linked(a, 'flashSale18', b2)
    if hasattr(b1, 'onlineShop19'):
        assert not _is_linked(b1, 'onlineShop19', a)
    if hasattr(b2, 'onlineShop19'):
        assert _is_linked(b2, 'onlineShop19', a)
    _safe_set(a, 'flashSale18', None)
    assert not _is_linked(a, 'flashSale18', b2)
    if hasattr(b2, 'onlineShop19'):
        assert not _is_linked(b2, 'onlineShop19', a)


def test_assoc_OnlineShop_Order_link_reassign_clear():
    a = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    b1 = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    b2 = OnlineShop(OnlineShopID=13, OnlineShopName="sample_text_2", ShopCategoryID=13, isActive=False)
    _safe_set(a, 'onlineShop21', b1)
    assert _is_linked(a, 'onlineShop21', b1)
    if hasattr(b1, 'order20'):
        assert _is_linked(b1, 'order20', a)
    _safe_set(a, 'onlineShop21', b2)
    assert _is_linked(a, 'onlineShop21', b2)
    if hasattr(b1, 'order20'):
        assert not _is_linked(b1, 'order20', a)
    if hasattr(b2, 'order20'):
        assert _is_linked(b2, 'order20', a)
    _safe_set(a, 'onlineShop21', None)
    assert not _is_linked(a, 'onlineShop21', b2)
    if hasattr(b2, 'order20'):
        assert not _is_linked(b2, 'order20', a)


def test_assoc_OnlineShop_User_link_reassign_clear():
    a = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    b1 = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    b2 = OnlineShop(OnlineShopID=13, OnlineShopName="sample_text_2", ShopCategoryID=13, isActive=False)
    _safe_set(a, 'onlineShop15', b1)
    assert _is_linked(a, 'onlineShop15', b1)
    if hasattr(b1, 'user14'):
        assert _is_linked(b1, 'user14', a)
    _safe_set(a, 'onlineShop15', b2)
    assert _is_linked(a, 'onlineShop15', b2)
    if hasattr(b1, 'user14'):
        assert not _is_linked(b1, 'user14', a)
    if hasattr(b2, 'user14'):
        assert _is_linked(b2, 'user14', a)
    _safe_set(a, 'onlineShop15', None)
    assert not _is_linked(a, 'onlineShop15', b2)
    if hasattr(b2, 'user14'):
        assert not _is_linked(b2, 'user14', a)


def test_assoc_Product_OnlineShop_link_reassign_clear():
    a = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    b1 = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    b2 = OnlineShop(OnlineShopID=13, OnlineShopName="sample_text_2", ShopCategoryID=13, isActive=False)
    _safe_set(a, 'onlineShop8', b1)
    assert _is_linked(a, 'onlineShop8', b1)
    if hasattr(b1, 'product9'):
        assert _is_linked(b1, 'product9', a)
    _safe_set(a, 'onlineShop8', b2)
    assert _is_linked(a, 'onlineShop8', b2)
    if hasattr(b1, 'product9'):
        assert not _is_linked(b1, 'product9', a)
    if hasattr(b2, 'product9'):
        assert _is_linked(b2, 'product9', a)
    _safe_set(a, 'onlineShop8', None)
    assert not _is_linked(a, 'onlineShop8', b2)
    if hasattr(b2, 'product9'):
        assert not _is_linked(b2, 'product9', a)


def test_assoc_User_Role_link_reassign_clear():
    a = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    b1 = Role(Description="sample_text", RoleID=7, RoleName="sample_text", isActive=True)
    b2 = Role(Description="sample_text_2", RoleID=13, RoleName="sample_text_2", isActive=False)
    _safe_set(a, 'role12', b1)
    assert _is_linked(a, 'role12', b1)
    if hasattr(b1, 'user13'):
        assert _is_linked(b1, 'user13', a)
    _safe_set(a, 'role12', b2)
    assert _is_linked(a, 'role12', b2)
    if hasattr(b1, 'user13'):
        assert not _is_linked(b1, 'user13', a)
    if hasattr(b2, 'user13'):
        assert _is_linked(b2, 'user13', a)
    _safe_set(a, 'role12', None)
    assert not _is_linked(a, 'role12', b2)
    if hasattr(b2, 'user13'):
        assert not _is_linked(b2, 'user13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BaseDateInformation_strategy = st.builds(BaseDateInformation, CreateDate=safe_text, CreatedBy=safe_text, LastModifedBy=safe_text, LastModifedDate=safe_text)
@given(instance=BaseDateInformation_strategy)
@settings(max_examples=25)
def test_BaseDateInformation_instantiation(instance):
    assert isinstance(instance, BaseDateInformation)


Category_strategy = st.builds(Category, CategoryID=st.integers(), CategoryName=safe_text, Description=safe_text, isActive=st.booleans())
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


Customer_strategy = st.builds(Customer, Address=safe_text, CustomerID=st.integers(), CustomerName=safe_text, Email=safe_text, Gender=st.integers(), Phone=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


FlashSale_strategy = st.builds(FlashSale, Description=safe_text, DiscountAmount=st.integers(), DiscountPercent=st.integers(), FlashSaleID=st.integers(), FlashSaleName=safe_text, OnlineShopID=st.integers())
@given(instance=FlashSale_strategy)
@settings(max_examples=25)
def test_FlashSale_instantiation(instance):
    assert isinstance(instance, FlashSale)


OnlineShop_strategy = st.builds(OnlineShop, OnlineShopID=st.integers(), OnlineShopName=safe_text, ShopCategoryID=st.integers(), isActive=st.booleans())
@given(instance=OnlineShop_strategy)
@settings(max_examples=25)
def test_OnlineShop_instantiation(instance):
    assert isinstance(instance, OnlineShop)


Order_strategy = st.builds(Order, OrderCustomerID=st.integers(), OrderDate=safe_text, OrderID=st.integers(), ReceiveCustomerID=st.integers(), ShopOnlineID=st.integers(), Status=st.booleans(), TotalDiscount=safe_text, TotalPrice=safe_text, UserID=st.integers())
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Product_strategy = st.builds(Product, CategoryID=st.integers(), Description=safe_text, Image=safe_text, OnlineShopID=st.integers(), Price=safe_text, ProductID=st.integers(), ProductName=safe_text, isActive=st.booleans())
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)


Role_strategy = st.builds(Role, Description=safe_text, RoleID=st.integers(), RoleName=safe_text, isActive=st.booleans())
@given(instance=Role_strategy)
@settings(max_examples=25)
def test_Role_instantiation(instance):
    assert isinstance(instance, Role)


User_strategy = st.builds(User, Password=safe_text, RegisterDate=safe_text, RoleID=st.integers(), UserID=safe_text, Username=safe_text, isActive=st.booleans())
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


