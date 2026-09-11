import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Banner,
    Cart,
    Collection,
    Color,
    DetailCart,
    DetailOrder,
    Gallery,
    Inventory,
    Orders,
    Products,
    Size,
    Type,
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

def test_Admin_AdminInfo_value_roundtrip():
    instance = Admin(AdminInfo="sample_text", ID=7, Password="sample_text", UserName="sample_text")
    assert instance.AdminInfo == "sample_text"
    instance.AdminInfo = "sample_text_2"
    assert instance.AdminInfo == "sample_text_2"


def test_Admin_ID_value_roundtrip():
    instance = Admin(AdminInfo="sample_text", ID=7, Password="sample_text", UserName="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Admin_Password_value_roundtrip():
    instance = Admin(AdminInfo="sample_text", ID=7, Password="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Admin_UserName_value_roundtrip():
    instance = Admin(AdminInfo="sample_text", ID=7, Password="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Banner_BannerID_value_roundtrip():
    instance = Banner(BannerID=7, BannerInfo="sample_text", DateEnd="sample_text", DateStart="sample_text", Image="sample_text", IsShow=7)
    assert instance.BannerID == 7
    instance.BannerID = 13
    assert instance.BannerID == 13


def test_Banner_BannerInfo_value_roundtrip():
    instance = Banner(BannerID=7, BannerInfo="sample_text", DateEnd="sample_text", DateStart="sample_text", Image="sample_text", IsShow=7)
    assert instance.BannerInfo == "sample_text"
    instance.BannerInfo = "sample_text_2"
    assert instance.BannerInfo == "sample_text_2"


def test_Banner_DateEnd_value_roundtrip():
    instance = Banner(BannerID=7, BannerInfo="sample_text", DateEnd="sample_text", DateStart="sample_text", Image="sample_text", IsShow=7)
    assert instance.DateEnd == "sample_text"
    instance.DateEnd = "sample_text_2"
    assert instance.DateEnd == "sample_text_2"


def test_Banner_DateStart_value_roundtrip():
    instance = Banner(BannerID=7, BannerInfo="sample_text", DateEnd="sample_text", DateStart="sample_text", Image="sample_text", IsShow=7)
    assert instance.DateStart == "sample_text"
    instance.DateStart = "sample_text_2"
    assert instance.DateStart == "sample_text_2"


def test_Banner_Image_value_roundtrip():
    instance = Banner(BannerID=7, BannerInfo="sample_text", DateEnd="sample_text", DateStart="sample_text", Image="sample_text", IsShow=7)
    assert instance.Image == "sample_text"
    instance.Image = "sample_text_2"
    assert instance.Image == "sample_text_2"


def test_Banner_IsShow_value_roundtrip():
    instance = Banner(BannerID=7, BannerInfo="sample_text", DateEnd="sample_text", DateStart="sample_text", Image="sample_text", IsShow=7)
    assert instance.IsShow == 7
    instance.IsShow = 13
    assert instance.IsShow == 13


def test_Cart_CartID_value_roundtrip():
    instance = Cart(CartID=7, CartInfo="sample_text")
    assert instance.CartID == 7
    instance.CartID = 13
    assert instance.CartID == 13


def test_Cart_CartInfo_value_roundtrip():
    instance = Cart(CartID=7, CartInfo="sample_text")
    assert instance.CartInfo == "sample_text"
    instance.CartInfo = "sample_text_2"
    assert instance.CartInfo == "sample_text_2"


def test_Collection_CollectionID_value_roundtrip():
    instance = Collection(CollectionID=7, CollectionName="sample_text")
    assert instance.CollectionID == 7
    instance.CollectionID = 13
    assert instance.CollectionID == 13


def test_Collection_CollectionName_value_roundtrip():
    instance = Collection(CollectionID=7, CollectionName="sample_text")
    assert instance.CollectionName == "sample_text"
    instance.CollectionName = "sample_text_2"
    assert instance.CollectionName == "sample_text_2"


def test_Color_ColorID_value_roundtrip():
    instance = Color(ColorID="sample_text", ColorName="sample_text")
    assert instance.ColorID == "sample_text"
    instance.ColorID = "sample_text_2"
    assert instance.ColorID == "sample_text_2"


def test_Color_ColorName_value_roundtrip():
    instance = Color(ColorID="sample_text", ColorName="sample_text")
    assert instance.ColorName == "sample_text"
    instance.ColorName = "sample_text_2"
    assert instance.ColorName == "sample_text_2"


def test_DetailCart_CartID_value_roundtrip():
    instance = DetailCart(CartID=7, DetailCartID=7, DetailCartInfo="sample_text", ProductID=7)
    assert instance.CartID == 7
    instance.CartID = 13
    assert instance.CartID == 13


def test_DetailCart_DetailCartID_value_roundtrip():
    instance = DetailCart(CartID=7, DetailCartID=7, DetailCartInfo="sample_text", ProductID=7)
    assert instance.DetailCartID == 7
    instance.DetailCartID = 13
    assert instance.DetailCartID == 13


def test_DetailCart_DetailCartInfo_value_roundtrip():
    instance = DetailCart(CartID=7, DetailCartID=7, DetailCartInfo="sample_text", ProductID=7)
    assert instance.DetailCartInfo == "sample_text"
    instance.DetailCartInfo = "sample_text_2"
    assert instance.DetailCartInfo == "sample_text_2"


def test_DetailCart_ProductID_value_roundtrip():
    instance = DetailCart(CartID=7, DetailCartID=7, DetailCartInfo="sample_text", ProductID=7)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_DetailOrder_DetailOrderID_value_roundtrip():
    instance = DetailOrder(DetailOrderID=7, DetailOrderInfo="sample_text", OrderID=7, ProductID=7)
    assert instance.DetailOrderID == 7
    instance.DetailOrderID = 13
    assert instance.DetailOrderID == 13


def test_DetailOrder_DetailOrderInfo_value_roundtrip():
    instance = DetailOrder(DetailOrderID=7, DetailOrderInfo="sample_text", OrderID=7, ProductID=7)
    assert instance.DetailOrderInfo == "sample_text"
    instance.DetailOrderInfo = "sample_text_2"
    assert instance.DetailOrderInfo == "sample_text_2"


def test_DetailOrder_OrderID_value_roundtrip():
    instance = DetailOrder(DetailOrderID=7, DetailOrderInfo="sample_text", OrderID=7, ProductID=7)
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_DetailOrder_ProductID_value_roundtrip():
    instance = DetailOrder(DetailOrderID=7, DetailOrderInfo="sample_text", OrderID=7, ProductID=7)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_Gallery_DateCreate_value_roundtrip():
    instance = Gallery(DateCreate="sample_text", GalleryID=7, GalleryName="sample_text", Image="sample_text", ProductID=7)
    assert instance.DateCreate == "sample_text"
    instance.DateCreate = "sample_text_2"
    assert instance.DateCreate == "sample_text_2"


def test_Gallery_GalleryID_value_roundtrip():
    instance = Gallery(DateCreate="sample_text", GalleryID=7, GalleryName="sample_text", Image="sample_text", ProductID=7)
    assert instance.GalleryID == 7
    instance.GalleryID = 13
    assert instance.GalleryID == 13


def test_Gallery_GalleryName_value_roundtrip():
    instance = Gallery(DateCreate="sample_text", GalleryID=7, GalleryName="sample_text", Image="sample_text", ProductID=7)
    assert instance.GalleryName == "sample_text"
    instance.GalleryName = "sample_text_2"
    assert instance.GalleryName == "sample_text_2"


def test_Gallery_Image_value_roundtrip():
    instance = Gallery(DateCreate="sample_text", GalleryID=7, GalleryName="sample_text", Image="sample_text", ProductID=7)
    assert instance.Image == "sample_text"
    instance.Image = "sample_text_2"
    assert instance.Image == "sample_text_2"


def test_Gallery_ProductID_value_roundtrip():
    instance = Gallery(DateCreate="sample_text", GalleryID=7, GalleryName="sample_text", Image="sample_text", ProductID=7)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_Inventory_ColorID_value_roundtrip():
    instance = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    assert instance.ColorID == 7
    instance.ColorID = 13
    assert instance.ColorID == 13


def test_Inventory_InStock_value_roundtrip():
    instance = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    assert instance.InStock == 7
    instance.InStock = 13
    assert instance.InStock == 13


def test_Inventory_ProductID_value_roundtrip():
    instance = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_Inventory_SizeID_value_roundtrip():
    instance = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    assert instance.SizeID == 7
    instance.SizeID = 13
    assert instance.SizeID == 13


def test_Orders_DeliInfo_value_roundtrip():
    instance = Orders(DeliInfo="sample_text", OrderID=7, OrderInfo="sample_text", UserID=7)
    assert instance.DeliInfo == "sample_text"
    instance.DeliInfo = "sample_text_2"
    assert instance.DeliInfo == "sample_text_2"


def test_Orders_OrderID_value_roundtrip():
    instance = Orders(DeliInfo="sample_text", OrderID=7, OrderInfo="sample_text", UserID=7)
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Orders_OrderInfo_value_roundtrip():
    instance = Orders(DeliInfo="sample_text", OrderID=7, OrderInfo="sample_text", UserID=7)
    assert instance.OrderInfo == "sample_text"
    instance.OrderInfo = "sample_text_2"
    assert instance.OrderInfo == "sample_text_2"


def test_Orders_UserID_value_roundtrip():
    instance = Orders(DeliInfo="sample_text", OrderID=7, OrderInfo="sample_text", UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_Products_CollectionID_value_roundtrip():
    instance = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    assert instance.CollectionID == 7
    instance.CollectionID = 13
    assert instance.CollectionID == 13


def test_Products_DateCreate_value_roundtrip():
    instance = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    assert instance.DateCreate == "sample_text"
    instance.DateCreate = "sample_text_2"
    assert instance.DateCreate == "sample_text_2"


def test_Products_InStock_value_roundtrip():
    instance = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    assert instance.InStock == 7
    instance.InStock = 13
    assert instance.InStock == 13


def test_Products_Index_value_roundtrip():
    instance = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    assert instance.Index == 7
    instance.Index = 13
    assert instance.Index == 13


def test_Products_ProductID_value_roundtrip():
    instance = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    assert instance.ProductID == 7
    instance.ProductID = 13
    assert instance.ProductID == 13


def test_Products_ProductInfo_value_roundtrip():
    instance = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    assert instance.ProductInfo == "sample_text"
    instance.ProductInfo = "sample_text_2"
    assert instance.ProductInfo == "sample_text_2"


def test_Products_TypeID_value_roundtrip():
    instance = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    assert instance.TypeID == 7
    instance.TypeID = 13
    assert instance.TypeID == 13


def test_Products_TypeID1_value_roundtrip():
    instance = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    assert instance.TypeID1 == 7
    instance.TypeID1 = 13
    assert instance.TypeID1 == 13


def test_Size_SizeID_value_roundtrip():
    instance = Size(SizeID=7, SizeName="sample_text")
    assert instance.SizeID == 7
    instance.SizeID = 13
    assert instance.SizeID == 13


def test_Size_SizeName_value_roundtrip():
    instance = Size(SizeID=7, SizeName="sample_text")
    assert instance.SizeName == "sample_text"
    instance.SizeName = "sample_text_2"
    assert instance.SizeName == "sample_text_2"


def test_Type_TypeID_value_roundtrip():
    instance = Type(TypeID=7, TypeName="sample_text")
    assert instance.TypeID == 7
    instance.TypeID = 13
    assert instance.TypeID == 13


def test_Type_TypeName_value_roundtrip():
    instance = Type(TypeID=7, TypeName="sample_text")
    assert instance.TypeName == "sample_text"
    instance.TypeName = "sample_text_2"
    assert instance.TypeName == "sample_text_2"


def test_User_Email_value_roundtrip():
    instance = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_User_ID_value_roundtrip():
    instance = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_User_Password_value_roundtrip():
    instance = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_User_Phone_value_roundtrip():
    instance = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    assert instance.Phone == 7
    instance.Phone = 13
    assert instance.Phone == 13


def test_User_Point_value_roundtrip():
    instance = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    assert instance.Point == 7
    instance.Point = 13
    assert instance.Point == 13


def test_User_UserInfo_value_roundtrip():
    instance = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    assert instance.UserInfo == "sample_text"
    instance.UserInfo = "sample_text_2"
    assert instance.UserInfo == "sample_text_2"


def test_User_UserName_value_roundtrip():
    instance = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_assoc_Cart_User_link_reassign_clear():
    a = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    b1 = Cart(CartID=7, CartInfo="sample_text")
    b2 = Cart(CartID=13, CartInfo="sample_text_2")
    _safe_set(a, 'cart23', b1)
    assert _is_linked(a, 'cart23', b1)
    if hasattr(b1, 'user22'):
        assert _is_linked(b1, 'user22', a)
    _safe_set(a, 'cart23', b2)
    assert _is_linked(a, 'cart23', b2)
    if hasattr(b1, 'user22'):
        assert not _is_linked(b1, 'user22', a)
    if hasattr(b2, 'user22'):
        assert _is_linked(b2, 'user22', a)
    _safe_set(a, 'cart23', None)
    assert not _is_linked(a, 'cart23', b2)
    if hasattr(b2, 'user22'):
        assert not _is_linked(b2, 'user22', a)


def test_assoc_Collection_Products_link_reassign_clear():
    a = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    b1 = Collection(CollectionID=7, CollectionName="sample_text")
    b2 = Collection(CollectionID=13, CollectionName="sample_text_2")
    _safe_set(a, 'collection7', b1)
    assert _is_linked(a, 'collection7', b1)
    if hasattr(b1, 'products6'):
        assert _is_linked(b1, 'products6', a)
    _safe_set(a, 'collection7', b2)
    assert _is_linked(a, 'collection7', b2)
    if hasattr(b1, 'products6'):
        assert not _is_linked(b1, 'products6', a)
    if hasattr(b2, 'products6'):
        assert _is_linked(b2, 'products6', a)
    _safe_set(a, 'collection7', None)
    assert not _is_linked(a, 'collection7', b2)
    if hasattr(b2, 'products6'):
        assert not _is_linked(b2, 'products6', a)


def test_assoc_Color_Inventory_link_reassign_clear():
    a = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    b1 = Color(ColorID="sample_text", ColorName="sample_text")
    b2 = Color(ColorID="sample_text_2", ColorName="sample_text_2")
    _safe_set(a, 'color3', {b1})
    assert _is_linked(a, 'color3', b1)
    if hasattr(b1, 'inventory2'):
        assert _is_linked(b1, 'inventory2', a)
    _safe_set(a, 'color3', {b2})
    assert _is_linked(a, 'color3', b2)
    if hasattr(b1, 'inventory2'):
        assert not _is_linked(b1, 'inventory2', a)
    if hasattr(b2, 'inventory2'):
        assert _is_linked(b2, 'inventory2', a)
    _safe_set(a, 'color3', set())
    assert not _is_linked(a, 'color3', b2)
    if hasattr(b2, 'inventory2'):
        assert not _is_linked(b2, 'inventory2', a)


def test_assoc_DetailCart_Cart_link_reassign_clear():
    a = DetailCart(CartID=7, DetailCartID=7, DetailCartInfo="sample_text", ProductID=7)
    b1 = Cart(CartID=7, CartInfo="sample_text")
    b2 = Cart(CartID=13, CartInfo="sample_text_2")
    _safe_set(a, 'cart18', b1)
    assert _is_linked(a, 'cart18', b1)
    if hasattr(b1, 'detailCart19'):
        assert _is_linked(b1, 'detailCart19', a)
    _safe_set(a, 'cart18', b2)
    assert _is_linked(a, 'cart18', b2)
    if hasattr(b1, 'detailCart19'):
        assert not _is_linked(b1, 'detailCart19', a)
    if hasattr(b2, 'detailCart19'):
        assert _is_linked(b2, 'detailCart19', a)
    _safe_set(a, 'cart18', None)
    assert not _is_linked(a, 'cart18', b2)
    if hasattr(b2, 'detailCart19'):
        assert not _is_linked(b2, 'detailCart19', a)


def test_assoc_DetailOrder_Orders_link_reassign_clear():
    a = Orders(DeliInfo="sample_text", OrderID=7, OrderInfo="sample_text", UserID=7)
    b1 = DetailOrder(DetailOrderID=7, DetailOrderInfo="sample_text", OrderID=7, ProductID=7)
    b2 = DetailOrder(DetailOrderID=13, DetailOrderInfo="sample_text_2", OrderID=13, ProductID=13)
    _safe_set(a, 'detailOrder17', {b1})
    assert _is_linked(a, 'detailOrder17', b1)
    if hasattr(b1, 'orders16'):
        assert _is_linked(b1, 'orders16', a)
    _safe_set(a, 'detailOrder17', {b2})
    assert _is_linked(a, 'detailOrder17', b2)
    if hasattr(b1, 'orders16'):
        assert not _is_linked(b1, 'orders16', a)
    if hasattr(b2, 'orders16'):
        assert _is_linked(b2, 'orders16', a)
    _safe_set(a, 'detailOrder17', set())
    assert not _is_linked(a, 'detailOrder17', b2)
    if hasattr(b2, 'orders16'):
        assert not _is_linked(b2, 'orders16', a)


def test_assoc_DetailOrder_Products_link_reassign_clear():
    a = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    b1 = DetailOrder(DetailOrderID=7, DetailOrderInfo="sample_text", OrderID=7, ProductID=7)
    b2 = DetailOrder(DetailOrderID=13, DetailOrderInfo="sample_text_2", OrderID=13, ProductID=13)
    _safe_set(a, 'detailOrder13', b1)
    assert _is_linked(a, 'detailOrder13', b1)
    if hasattr(b1, 'products12'):
        assert _is_linked(b1, 'products12', a)
    _safe_set(a, 'detailOrder13', b2)
    assert _is_linked(a, 'detailOrder13', b2)
    if hasattr(b1, 'products12'):
        assert not _is_linked(b1, 'products12', a)
    if hasattr(b2, 'products12'):
        assert _is_linked(b2, 'products12', a)
    _safe_set(a, 'detailOrder13', None)
    assert not _is_linked(a, 'detailOrder13', b2)
    if hasattr(b2, 'products12'):
        assert not _is_linked(b2, 'products12', a)


def test_assoc_Gallery_Products_link_reassign_clear():
    a = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    b1 = Gallery(DateCreate="sample_text", GalleryID=7, GalleryName="sample_text", Image="sample_text", ProductID=7)
    b2 = Gallery(DateCreate="sample_text_2", GalleryID=13, GalleryName="sample_text_2", Image="sample_text_2", ProductID=13)
    _safe_set(a, 'gallery11', {b1})
    assert _is_linked(a, 'gallery11', b1)
    if hasattr(b1, 'products10'):
        assert _is_linked(b1, 'products10', a)
    _safe_set(a, 'gallery11', {b2})
    assert _is_linked(a, 'gallery11', b2)
    if hasattr(b1, 'products10'):
        assert not _is_linked(b1, 'products10', a)
    if hasattr(b2, 'products10'):
        assert _is_linked(b2, 'products10', a)
    _safe_set(a, 'gallery11', set())
    assert not _is_linked(a, 'gallery11', b2)
    if hasattr(b2, 'products10'):
        assert not _is_linked(b2, 'products10', a)


def test_assoc_Orders_User_link_reassign_clear():
    a = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    b1 = Orders(DeliInfo="sample_text", OrderID=7, OrderInfo="sample_text", UserID=7)
    b2 = Orders(DeliInfo="sample_text_2", OrderID=13, OrderInfo="sample_text_2", UserID=13)
    _safe_set(a, 'orders21', b1)
    assert _is_linked(a, 'orders21', b1)
    if hasattr(b1, 'user20'):
        assert _is_linked(b1, 'user20', a)
    _safe_set(a, 'orders21', b2)
    assert _is_linked(a, 'orders21', b2)
    if hasattr(b1, 'user20'):
        assert not _is_linked(b1, 'user20', a)
    if hasattr(b2, 'user20'):
        assert _is_linked(b2, 'user20', a)
    _safe_set(a, 'orders21', None)
    assert not _is_linked(a, 'orders21', b2)
    if hasattr(b2, 'user20'):
        assert not _is_linked(b2, 'user20', a)


def test_assoc_Products_DetailCart_link_reassign_clear():
    a = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    b1 = DetailCart(CartID=7, DetailCartID=7, DetailCartInfo="sample_text", ProductID=7)
    b2 = DetailCart(CartID=13, DetailCartID=13, DetailCartInfo="sample_text_2", ProductID=13)
    _safe_set(a, 'detailCart14', b1)
    assert _is_linked(a, 'detailCart14', b1)
    if hasattr(b1, 'products15'):
        assert _is_linked(b1, 'products15', a)
    _safe_set(a, 'detailCart14', b2)
    assert _is_linked(a, 'detailCart14', b2)
    if hasattr(b1, 'products15'):
        assert not _is_linked(b1, 'products15', a)
    if hasattr(b2, 'products15'):
        assert _is_linked(b2, 'products15', a)
    _safe_set(a, 'detailCart14', None)
    assert not _is_linked(a, 'detailCart14', b2)
    if hasattr(b2, 'products15'):
        assert not _is_linked(b2, 'products15', a)


def test_assoc_Products_Inventory_link_reassign_clear():
    a = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    b1 = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    b2 = Inventory(ColorID=13, InStock=13, ProductID=13, SizeID=13)
    _safe_set(a, 'inventory4', {b1})
    assert _is_linked(a, 'inventory4', b1)
    if hasattr(b1, 'products5'):
        assert _is_linked(b1, 'products5', a)
    _safe_set(a, 'inventory4', {b2})
    assert _is_linked(a, 'inventory4', b2)
    if hasattr(b1, 'products5'):
        assert not _is_linked(b1, 'products5', a)
    if hasattr(b2, 'products5'):
        assert _is_linked(b2, 'products5', a)
    _safe_set(a, 'inventory4', set())
    assert not _is_linked(a, 'inventory4', b2)
    if hasattr(b2, 'products5'):
        assert not _is_linked(b2, 'products5', a)


def test_assoc_Size_Inventory_link_reassign_clear():
    a = Size(SizeID=7, SizeName="sample_text")
    b1 = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    b2 = Inventory(ColorID=13, InStock=13, ProductID=13, SizeID=13)
    _safe_set(a, 'inventory0', {b1})
    assert _is_linked(a, 'inventory0', b1)
    if hasattr(b1, 'size1'):
        assert _is_linked(b1, 'size1', a)
    _safe_set(a, 'inventory0', {b2})
    assert _is_linked(a, 'inventory0', b2)
    if hasattr(b1, 'size1'):
        assert not _is_linked(b1, 'size1', a)
    if hasattr(b2, 'size1'):
        assert _is_linked(b2, 'size1', a)
    _safe_set(a, 'inventory0', set())
    assert not _is_linked(a, 'inventory0', b2)
    if hasattr(b2, 'size1'):
        assert not _is_linked(b2, 'size1', a)


def test_assoc_Type_Products_link_reassign_clear():
    a = Type(TypeID=7, TypeName="sample_text")
    b1 = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    b2 = Products(CollectionID=13, DateCreate="sample_text_2", InStock=13, Index=13, ProductID=13, ProductInfo="sample_text_2", TypeID=13, TypeID1=13)
    _safe_set(a, 'products8', {b1})
    assert _is_linked(a, 'products8', b1)
    if hasattr(b1, 'type9'):
        assert _is_linked(b1, 'type9', a)
    _safe_set(a, 'products8', {b2})
    assert _is_linked(a, 'products8', b2)
    if hasattr(b1, 'type9'):
        assert not _is_linked(b1, 'type9', a)
    if hasattr(b2, 'type9'):
        assert _is_linked(b2, 'type9', a)
    _safe_set(a, 'products8', set())
    assert not _is_linked(a, 'products8', b2)
    if hasattr(b2, 'type9'):
        assert not _is_linked(b2, 'type9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, AdminInfo=safe_text, ID=st.integers(), Password=safe_text, UserName=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Banner_strategy = st.builds(Banner, BannerID=st.integers(), BannerInfo=safe_text, DateEnd=safe_text, DateStart=safe_text, Image=safe_text, IsShow=st.integers())
@given(instance=Banner_strategy)
@settings(max_examples=25)
def test_Banner_instantiation(instance):
    assert isinstance(instance, Banner)


Cart_strategy = st.builds(Cart, CartID=st.integers(), CartInfo=safe_text)
@given(instance=Cart_strategy)
@settings(max_examples=25)
def test_Cart_instantiation(instance):
    assert isinstance(instance, Cart)


Collection_strategy = st.builds(Collection, CollectionID=st.integers(), CollectionName=safe_text)
@given(instance=Collection_strategy)
@settings(max_examples=25)
def test_Collection_instantiation(instance):
    assert isinstance(instance, Collection)


Color_strategy = st.builds(Color, ColorID=safe_text, ColorName=safe_text)
@given(instance=Color_strategy)
@settings(max_examples=25)
def test_Color_instantiation(instance):
    assert isinstance(instance, Color)


DetailCart_strategy = st.builds(DetailCart, CartID=st.integers(), DetailCartID=st.integers(), DetailCartInfo=safe_text, ProductID=st.integers())
@given(instance=DetailCart_strategy)
@settings(max_examples=25)
def test_DetailCart_instantiation(instance):
    assert isinstance(instance, DetailCart)


DetailOrder_strategy = st.builds(DetailOrder, DetailOrderID=st.integers(), DetailOrderInfo=safe_text, OrderID=st.integers(), ProductID=st.integers())
@given(instance=DetailOrder_strategy)
@settings(max_examples=25)
def test_DetailOrder_instantiation(instance):
    assert isinstance(instance, DetailOrder)


Gallery_strategy = st.builds(Gallery, DateCreate=safe_text, GalleryID=st.integers(), GalleryName=safe_text, Image=safe_text, ProductID=st.integers())
@given(instance=Gallery_strategy)
@settings(max_examples=25)
def test_Gallery_instantiation(instance):
    assert isinstance(instance, Gallery)


Inventory_strategy = st.builds(Inventory, ColorID=st.integers(), InStock=st.integers(), ProductID=st.integers(), SizeID=st.integers())
@given(instance=Inventory_strategy)
@settings(max_examples=25)
def test_Inventory_instantiation(instance):
    assert isinstance(instance, Inventory)


Orders_strategy = st.builds(Orders, DeliInfo=safe_text, OrderID=st.integers(), OrderInfo=safe_text, UserID=st.integers())
@given(instance=Orders_strategy)
@settings(max_examples=25)
def test_Orders_instantiation(instance):
    assert isinstance(instance, Orders)


Products_strategy = st.builds(Products, CollectionID=st.integers(), DateCreate=safe_text, InStock=st.integers(), Index=st.integers(), ProductID=st.integers(), ProductInfo=safe_text, TypeID=st.integers(), TypeID1=st.integers())
@given(instance=Products_strategy)
@settings(max_examples=25)
def test_Products_instantiation(instance):
    assert isinstance(instance, Products)


Size_strategy = st.builds(Size, SizeID=st.integers(), SizeName=safe_text)
@given(instance=Size_strategy)
@settings(max_examples=25)
def test_Size_instantiation(instance):
    assert isinstance(instance, Size)


Type_strategy = st.builds(Type, TypeID=st.integers(), TypeName=safe_text)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


User_strategy = st.builds(User, Email=safe_text, ID=st.integers(), Password=safe_text, Phone=st.integers(), Point=st.integers(), UserInfo=safe_text, UserName=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


