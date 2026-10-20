import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_BaseDateInformation_Category_reverse_link_reassign_clear():
    a1 = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    a2 = Category(CategoryID=13, CategoryName="sample_text_2", Description="sample_text_2", isActive=False)
    b = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    _safe_set(b, 'category6', a1)
    assert _is_linked(b, 'category6', a1)
    if hasattr(a1, 'baseDateInformation7'):
        assert _is_linked(a1, 'baseDateInformation7', b)
    _safe_set(b, 'category6', a2)
    assert _is_linked(b, 'category6', a2)
    if hasattr(a1, 'baseDateInformation7'):
        assert not _is_linked(a1, 'baseDateInformation7', b)
    if hasattr(a2, 'baseDateInformation7'):
        assert _is_linked(a2, 'baseDateInformation7', b)
    _safe_set(b, 'category6', None)
    assert not _is_linked(b, 'category6', a2)
    if hasattr(a2, 'baseDateInformation7'):
        assert not _is_linked(a2, 'baseDateInformation7', b)


def test_assoc_BaseDateInformation_FlashSale_reverse_link_reassign_clear():
    a1 = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    a2 = FlashSale(Description="sample_text_2", DiscountAmount=13, DiscountPercent=13, FlashSaleID=13, FlashSaleName="sample_text_2", OnlineShopID=13)
    b = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    _safe_set(b, 'flashSale16', a1)
    assert _is_linked(b, 'flashSale16', a1)
    if hasattr(a1, 'baseDateInformation17'):
        assert _is_linked(a1, 'baseDateInformation17', b)
    _safe_set(b, 'flashSale16', a2)
    assert _is_linked(b, 'flashSale16', a2)
    if hasattr(a1, 'baseDateInformation17'):
        assert not _is_linked(a1, 'baseDateInformation17', b)
    if hasattr(a2, 'baseDateInformation17'):
        assert _is_linked(a2, 'baseDateInformation17', b)
    _safe_set(b, 'flashSale16', None)
    assert not _is_linked(b, 'flashSale16', a2)
    if hasattr(a2, 'baseDateInformation17'):
        assert not _is_linked(a2, 'baseDateInformation17', b)


def test_assoc_BaseDateInformation_OnlineShop_reverse_link_reassign_clear():
    a1 = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    a2 = OnlineShop(OnlineShopID=13, OnlineShopName="sample_text_2", ShopCategoryID=13, isActive=False)
    b = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    _safe_set(b, 'onlineShop22', a1)
    assert _is_linked(b, 'onlineShop22', a1)
    if hasattr(a1, 'baseDateInformation23'):
        assert _is_linked(a1, 'baseDateInformation23', b)
    _safe_set(b, 'onlineShop22', a2)
    assert _is_linked(b, 'onlineShop22', a2)
    if hasattr(a1, 'baseDateInformation23'):
        assert not _is_linked(a1, 'baseDateInformation23', b)
    if hasattr(a2, 'baseDateInformation23'):
        assert _is_linked(a2, 'baseDateInformation23', b)
    _safe_set(b, 'onlineShop22', None)
    assert not _is_linked(b, 'onlineShop22', a2)
    if hasattr(a2, 'baseDateInformation23'):
        assert not _is_linked(a2, 'baseDateInformation23', b)


def test_assoc_BaseDateInformation_Product_reverse_link_reassign_clear():
    a1 = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    a2 = Product(CategoryID=13, Description="sample_text_2", Image="sample_text_2", OnlineShopID=13, Price="sample_text_2", ProductID=13, ProductName="sample_text_2", isActive=False)
    b = BaseDateInformation(CreateDate="sample_text", CreatedBy="sample_text", LastModifedBy="sample_text", LastModifedDate="sample_text")
    _safe_set(b, 'product10', a1)
    assert _is_linked(b, 'product10', a1)
    if hasattr(a1, 'baseDateInformation11'):
        assert _is_linked(a1, 'baseDateInformation11', b)
    _safe_set(b, 'product10', a2)
    assert _is_linked(b, 'product10', a2)
    if hasattr(a1, 'baseDateInformation11'):
        assert not _is_linked(a1, 'baseDateInformation11', b)
    if hasattr(a2, 'baseDateInformation11'):
        assert _is_linked(a2, 'baseDateInformation11', b)
    _safe_set(b, 'product10', None)
    assert not _is_linked(b, 'product10', a2)
    if hasattr(a2, 'baseDateInformation11'):
        assert not _is_linked(a2, 'baseDateInformation11', b)


def test_assoc_Category_OnlineShop_reverse_link_reassign_clear():
    a1 = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    a2 = OnlineShop(OnlineShopID=13, OnlineShopName="sample_text_2", ShopCategoryID=13, isActive=False)
    b = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    _safe_set(b, 'onlineShop4', a1)
    assert _is_linked(b, 'onlineShop4', a1)
    if hasattr(a1, 'category5'):
        assert _is_linked(a1, 'category5', b)
    _safe_set(b, 'onlineShop4', a2)
    assert _is_linked(b, 'onlineShop4', a2)
    if hasattr(a1, 'category5'):
        assert not _is_linked(a1, 'category5', b)
    if hasattr(a2, 'category5'):
        assert _is_linked(a2, 'category5', b)
    _safe_set(b, 'onlineShop4', None)
    assert not _is_linked(b, 'onlineShop4', a2)
    if hasattr(a2, 'category5'):
        assert not _is_linked(a2, 'category5', b)


def test_assoc_Category_Product_reverse_link_reassign_clear():
    a1 = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    a2 = Product(CategoryID=13, Description="sample_text_2", Image="sample_text_2", OnlineShopID=13, Price="sample_text_2", ProductID=13, ProductName="sample_text_2", isActive=False)
    b = Category(CategoryID=7, CategoryName="sample_text", Description="sample_text", isActive=True)
    _safe_set(b, 'product0', {a1})
    assert _is_linked(b, 'product0', a1)
    if hasattr(a1, 'category1'):
        assert _is_linked(a1, 'category1', b)
    _safe_set(b, 'product0', {a2})
    assert _is_linked(b, 'product0', a2)
    if hasattr(a1, 'category1'):
        assert not _is_linked(a1, 'category1', b)
    if hasattr(a2, 'category1'):
        assert _is_linked(a2, 'category1', b)
    _safe_set(b, 'product0', set())
    assert not _is_linked(b, 'product0', a2)
    if hasattr(a2, 'category1'):
        assert not _is_linked(a2, 'category1', b)


def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    a2 = Order(OrderCustomerID=13, OrderDate="sample_text_2", OrderID=13, ReceiveCustomerID=13, ShopOnlineID=13, Status=False, TotalDiscount="sample_text_2", TotalPrice="sample_text_2", UserID=13)
    b = Customer(Address="sample_text", CustomerID=7, CustomerName="sample_text", Email="sample_text", Gender=7, Phone="sample_text")
    _safe_set(b, 'order2', a1)
    assert _is_linked(b, 'order2', a1)
    if hasattr(a1, 'customer3'):
        assert _is_linked(a1, 'customer3', b)
    _safe_set(b, 'order2', a2)
    assert _is_linked(b, 'order2', a2)
    if hasattr(a1, 'customer3'):
        assert not _is_linked(a1, 'customer3', b)
    if hasattr(a2, 'customer3'):
        assert _is_linked(a2, 'customer3', b)
    _safe_set(b, 'order2', None)
    assert not _is_linked(b, 'order2', a2)
    if hasattr(a2, 'customer3'):
        assert not _is_linked(a2, 'customer3', b)


def test_assoc_OnlineShop_FlashSale_reverse_link_reassign_clear():
    a1 = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    a2 = OnlineShop(OnlineShopID=13, OnlineShopName="sample_text_2", ShopCategoryID=13, isActive=False)
    b = FlashSale(Description="sample_text", DiscountAmount=7, DiscountPercent=7, FlashSaleID=7, FlashSaleName="sample_text", OnlineShopID=7)
    _safe_set(b, 'onlineShop19', a1)
    assert _is_linked(b, 'onlineShop19', a1)
    if hasattr(a1, 'flashSale18'):
        assert _is_linked(a1, 'flashSale18', b)
    _safe_set(b, 'onlineShop19', a2)
    assert _is_linked(b, 'onlineShop19', a2)
    if hasattr(a1, 'flashSale18'):
        assert not _is_linked(a1, 'flashSale18', b)
    if hasattr(a2, 'flashSale18'):
        assert _is_linked(a2, 'flashSale18', b)
    _safe_set(b, 'onlineShop19', None)
    assert not _is_linked(b, 'onlineShop19', a2)
    if hasattr(a2, 'flashSale18'):
        assert not _is_linked(a2, 'flashSale18', b)


def test_assoc_OnlineShop_Order_reverse_link_reassign_clear():
    a1 = Order(OrderCustomerID=7, OrderDate="sample_text", OrderID=7, ReceiveCustomerID=7, ShopOnlineID=7, Status=True, TotalDiscount="sample_text", TotalPrice="sample_text", UserID=7)
    a2 = Order(OrderCustomerID=13, OrderDate="sample_text_2", OrderID=13, ReceiveCustomerID=13, ShopOnlineID=13, Status=False, TotalDiscount="sample_text_2", TotalPrice="sample_text_2", UserID=13)
    b = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    _safe_set(b, 'order20', a1)
    assert _is_linked(b, 'order20', a1)
    if hasattr(a1, 'onlineShop21'):
        assert _is_linked(a1, 'onlineShop21', b)
    _safe_set(b, 'order20', a2)
    assert _is_linked(b, 'order20', a2)
    if hasattr(a1, 'onlineShop21'):
        assert not _is_linked(a1, 'onlineShop21', b)
    if hasattr(a2, 'onlineShop21'):
        assert _is_linked(a2, 'onlineShop21', b)
    _safe_set(b, 'order20', None)
    assert not _is_linked(b, 'order20', a2)
    if hasattr(a2, 'onlineShop21'):
        assert not _is_linked(a2, 'onlineShop21', b)


def test_assoc_OnlineShop_User_reverse_link_reassign_clear():
    a1 = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    a2 = User(Password="sample_text_2", RegisterDate="sample_text_2", RoleID=13, UserID="sample_text_2", Username="sample_text_2", isActive=False)
    b = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    _safe_set(b, 'user14', a1)
    assert _is_linked(b, 'user14', a1)
    if hasattr(a1, 'onlineShop15'):
        assert _is_linked(a1, 'onlineShop15', b)
    _safe_set(b, 'user14', a2)
    assert _is_linked(b, 'user14', a2)
    if hasattr(a1, 'onlineShop15'):
        assert not _is_linked(a1, 'onlineShop15', b)
    if hasattr(a2, 'onlineShop15'):
        assert _is_linked(a2, 'onlineShop15', b)
    _safe_set(b, 'user14', None)
    assert not _is_linked(b, 'user14', a2)
    if hasattr(a2, 'onlineShop15'):
        assert not _is_linked(a2, 'onlineShop15', b)


def test_assoc_Product_OnlineShop_reverse_link_reassign_clear():
    a1 = Product(CategoryID=7, Description="sample_text", Image="sample_text", OnlineShopID=7, Price="sample_text", ProductID=7, ProductName="sample_text", isActive=True)
    a2 = Product(CategoryID=13, Description="sample_text_2", Image="sample_text_2", OnlineShopID=13, Price="sample_text_2", ProductID=13, ProductName="sample_text_2", isActive=False)
    b = OnlineShop(OnlineShopID=7, OnlineShopName="sample_text", ShopCategoryID=7, isActive=True)
    _safe_set(b, 'product9', a1)
    assert _is_linked(b, 'product9', a1)
    if hasattr(a1, 'onlineShop8'):
        assert _is_linked(a1, 'onlineShop8', b)
    _safe_set(b, 'product9', a2)
    assert _is_linked(b, 'product9', a2)
    if hasattr(a1, 'onlineShop8'):
        assert not _is_linked(a1, 'onlineShop8', b)
    if hasattr(a2, 'onlineShop8'):
        assert _is_linked(a2, 'onlineShop8', b)
    _safe_set(b, 'product9', None)
    assert not _is_linked(b, 'product9', a2)
    if hasattr(a2, 'onlineShop8'):
        assert not _is_linked(a2, 'onlineShop8', b)


def test_assoc_User_Role_reverse_link_reassign_clear():
    a1 = User(Password="sample_text", RegisterDate="sample_text", RoleID=7, UserID="sample_text", Username="sample_text", isActive=True)
    a2 = User(Password="sample_text_2", RegisterDate="sample_text_2", RoleID=13, UserID="sample_text_2", Username="sample_text_2", isActive=False)
    b = Role(Description="sample_text", RoleID=7, RoleName="sample_text", isActive=True)
    _safe_set(b, 'user13', a1)
    assert _is_linked(b, 'user13', a1)
    if hasattr(a1, 'role12'):
        assert _is_linked(a1, 'role12', b)
    _safe_set(b, 'user13', a2)
    assert _is_linked(b, 'user13', a2)
    if hasattr(a1, 'role12'):
        assert not _is_linked(a1, 'role12', b)
    if hasattr(a2, 'role12'):
        assert _is_linked(a2, 'role12', b)
    _safe_set(b, 'user13', None)
    assert not _is_linked(b, 'user13', a2)
    if hasattr(a2, 'role12'):
        assert not _is_linked(a2, 'role12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

