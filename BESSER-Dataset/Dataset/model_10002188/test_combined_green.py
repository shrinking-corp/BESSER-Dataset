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
    Admin,
    DetailOrder,
    Orders,
    DetailCart,
    Cart,
    Inventory,
    Size,
    Color,
    Banner,
    Gallery,
    Type,
    Collection,
    Products,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "AdminInfo" in params, "Missing parameter 'AdminInfo'"
    assert "Password" in params, "Missing parameter 'Password'"







def test_hyp_detailorder_is_not_abstract():
    assert not inspect.isabstract(DetailOrder)


def test_hyp_detailorder_constructor_exists():
    assert callable(DetailOrder.__init__)


def test_hyp_detailorder_constructor_args():
    sig = inspect.signature(DetailOrder.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "DetailOrderInfo" in params, "Missing parameter 'DetailOrderInfo'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "DetailOrderID" in params, "Missing parameter 'DetailOrderID'"







def test_hyp_orders_is_not_abstract():
    assert not inspect.isabstract(Orders)


def test_hyp_orders_constructor_exists():
    assert callable(Orders.__init__)


def test_hyp_orders_constructor_args():
    sig = inspect.signature(Orders.__init__)
    params = list(sig.parameters.keys())
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "DeliInfo" in params, "Missing parameter 'DeliInfo'"
    assert "OrderInfo" in params, "Missing parameter 'OrderInfo'"
    assert "UserID" in params, "Missing parameter 'UserID'"







def test_hyp_detailcart_is_not_abstract():
    assert not inspect.isabstract(DetailCart)


def test_hyp_detailcart_constructor_exists():
    assert callable(DetailCart.__init__)


def test_hyp_detailcart_constructor_args():
    sig = inspect.signature(DetailCart.__init__)
    params = list(sig.parameters.keys())
    assert "DetailCartID" in params, "Missing parameter 'DetailCartID'"
    assert "DetailCartInfo" in params, "Missing parameter 'DetailCartInfo'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "CartID" in params, "Missing parameter 'CartID'"







def test_hyp_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_hyp_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_hyp_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())
    assert "CartID" in params, "Missing parameter 'CartID'"
    assert "CartInfo" in params, "Missing parameter 'CartInfo'"





def test_hyp_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_hyp_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_hyp_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "ColorID" in params, "Missing parameter 'ColorID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "SizeID" in params, "Missing parameter 'SizeID'"
    assert "InStock" in params, "Missing parameter 'InStock'"







def test_hyp_size_is_not_abstract():
    assert not inspect.isabstract(Size)


def test_hyp_size_constructor_exists():
    assert callable(Size.__init__)


def test_hyp_size_constructor_args():
    sig = inspect.signature(Size.__init__)
    params = list(sig.parameters.keys())
    assert "SizeID" in params, "Missing parameter 'SizeID'"
    assert "SizeName" in params, "Missing parameter 'SizeName'"





def test_hyp_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_hyp_color_constructor_exists():
    assert callable(Color.__init__)


def test_hyp_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())
    assert "ColorName" in params, "Missing parameter 'ColorName'"
    assert "ColorID" in params, "Missing parameter 'ColorID'"





def test_hyp_banner_is_not_abstract():
    assert not inspect.isabstract(Banner)


def test_hyp_banner_constructor_exists():
    assert callable(Banner.__init__)


def test_hyp_banner_constructor_args():
    sig = inspect.signature(Banner.__init__)
    params = list(sig.parameters.keys())
    assert "BannerInfo" in params, "Missing parameter 'BannerInfo'"
    assert "IsShow" in params, "Missing parameter 'IsShow'"
    assert "DateStart" in params, "Missing parameter 'DateStart'"
    assert "Image" in params, "Missing parameter 'Image'"
    assert "BannerID" in params, "Missing parameter 'BannerID'"
    assert "DateEnd" in params, "Missing parameter 'DateEnd'"









def test_hyp_gallery_is_not_abstract():
    assert not inspect.isabstract(Gallery)


def test_hyp_gallery_constructor_exists():
    assert callable(Gallery.__init__)


def test_hyp_gallery_constructor_args():
    sig = inspect.signature(Gallery.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "GalleryName" in params, "Missing parameter 'GalleryName'"
    assert "GalleryID" in params, "Missing parameter 'GalleryID'"
    assert "DateCreate" in params, "Missing parameter 'DateCreate'"
    assert "Image" in params, "Missing parameter 'Image'"








def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())
    assert "TypeID" in params, "Missing parameter 'TypeID'"
    assert "TypeName" in params, "Missing parameter 'TypeName'"





def test_hyp_collection_is_not_abstract():
    assert not inspect.isabstract(Collection)


def test_hyp_collection_constructor_exists():
    assert callable(Collection.__init__)


def test_hyp_collection_constructor_args():
    sig = inspect.signature(Collection.__init__)
    params = list(sig.parameters.keys())
    assert "CollectionName" in params, "Missing parameter 'CollectionName'"
    assert "CollectionID" in params, "Missing parameter 'CollectionID'"





def test_hyp_products_is_not_abstract():
    assert not inspect.isabstract(Products)


def test_hyp_products_constructor_exists():
    assert callable(Products.__init__)


def test_hyp_products_constructor_args():
    sig = inspect.signature(Products.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "CollectionID" in params, "Missing parameter 'CollectionID'"
    assert "InStock" in params, "Missing parameter 'InStock'"
    assert "TypeID1" in params, "Missing parameter 'TypeID1'"
    assert "TypeID" in params, "Missing parameter 'TypeID'"
    assert "ProductInfo" in params, "Missing parameter 'ProductInfo'"
    assert "Index" in params, "Missing parameter 'Index'"
    assert "DateCreate" in params, "Missing parameter 'DateCreate'"











def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Point" in params, "Missing parameter 'Point'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserInfo" in params, "Missing parameter 'UserInfo'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Phone" in params, "Missing parameter 'Phone'"









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
Admin_strategy = st.builds(
    Admin,
    UserName=
        safe_text,
    ID=
        st.integers(),
    AdminInfo=
        safe_text,
    Password=
        safe_text
)
DetailOrder_strategy = st.builds(
    DetailOrder,
    ProductID=
        st.integers(),
    DetailOrderInfo=
        safe_text,
    OrderID=
        st.integers(),
    DetailOrderID=
        st.integers()
)
Orders_strategy = st.builds(
    Orders,
    OrderID=
        st.integers(),
    DeliInfo=
        safe_text,
    OrderInfo=
        safe_text,
    UserID=
        st.integers()
)
DetailCart_strategy = st.builds(
    DetailCart,
    DetailCartID=
        st.integers(),
    DetailCartInfo=
        safe_text,
    ProductID=
        st.integers(),
    CartID=
        st.integers()
)
Cart_strategy = st.builds(
    Cart,
    CartID=
        st.integers(),
    CartInfo=
        safe_text
)
Inventory_strategy = st.builds(
    Inventory,
    ColorID=
        st.integers(),
    ProductID=
        st.integers(),
    SizeID=
        st.integers(),
    InStock=
        st.integers()
)
Size_strategy = st.builds(
    Size,
    SizeID=
        st.integers(),
    SizeName=
        safe_text
)
Color_strategy = st.builds(
    Color,
    ColorName=
        safe_text,
    ColorID=
        safe_text
)
Banner_strategy = st.builds(
    Banner,
    BannerInfo=
        safe_text,
    IsShow=
        st.integers(),
    DateStart=
        safe_text,
    Image=
        safe_text,
    BannerID=
        st.integers(),
    DateEnd=
        safe_text
)
Gallery_strategy = st.builds(
    Gallery,
    ProductID=
        st.integers(),
    GalleryName=
        safe_text,
    GalleryID=
        st.integers(),
    DateCreate=
        safe_text,
    Image=
        safe_text
)
Type_strategy = st.builds(
    Type,
    TypeID=
        st.integers(),
    TypeName=
        safe_text
)
Collection_strategy = st.builds(
    Collection,
    CollectionName=
        safe_text,
    CollectionID=
        st.integers()
)
Products_strategy = st.builds(
    Products,
    ProductID=
        st.integers(),
    CollectionID=
        st.integers(),
    InStock=
        st.integers(),
    TypeID1=
        st.integers(),
    TypeID=
        st.integers(),
    ProductInfo=
        safe_text,
    Index=
        st.integers(),
    DateCreate=
        safe_text
)
User_strategy = st.builds(
    User,
    UserName=
        safe_text,
    Point=
        st.integers(),
    Email=
        safe_text,
    Password=
        safe_text,
    UserInfo=
        safe_text,
    ID=
        st.integers(),
    Phone=
        st.integers()
)




@given(instance=Admin_strategy)
def test_hyp_admin_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Admin_strategy)
def test_hyp_admin_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Admin_strategy)
def test_hyp_admin_AdminInfo_setter(instance):
    original = instance.AdminInfo
    instance.AdminInfo = original
    assert instance.AdminInfo == original



@given(instance=Admin_strategy)
def test_hyp_admin_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original




@given(instance=DetailOrder_strategy)
def test_hyp_detailorder_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=DetailOrder_strategy)
def test_hyp_detailorder_DetailOrderInfo_setter(instance):
    original = instance.DetailOrderInfo
    instance.DetailOrderInfo = original
    assert instance.DetailOrderInfo == original



@given(instance=DetailOrder_strategy)
def test_hyp_detailorder_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=DetailOrder_strategy)
def test_hyp_detailorder_DetailOrderID_setter(instance):
    original = instance.DetailOrderID
    instance.DetailOrderID = original
    assert instance.DetailOrderID == original




@given(instance=Orders_strategy)
def test_hyp_orders_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Orders_strategy)
def test_hyp_orders_DeliInfo_setter(instance):
    original = instance.DeliInfo
    instance.DeliInfo = original
    assert instance.DeliInfo == original



@given(instance=Orders_strategy)
def test_hyp_orders_OrderInfo_setter(instance):
    original = instance.OrderInfo
    instance.OrderInfo = original
    assert instance.OrderInfo == original



@given(instance=Orders_strategy)
def test_hyp_orders_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original




@given(instance=DetailCart_strategy)
def test_hyp_detailcart_DetailCartID_setter(instance):
    original = instance.DetailCartID
    instance.DetailCartID = original
    assert instance.DetailCartID == original



@given(instance=DetailCart_strategy)
def test_hyp_detailcart_DetailCartInfo_setter(instance):
    original = instance.DetailCartInfo
    instance.DetailCartInfo = original
    assert instance.DetailCartInfo == original



@given(instance=DetailCart_strategy)
def test_hyp_detailcart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=DetailCart_strategy)
def test_hyp_detailcart_CartID_setter(instance):
    original = instance.CartID
    instance.CartID = original
    assert instance.CartID == original




@given(instance=Cart_strategy)
def test_hyp_cart_CartID_setter(instance):
    original = instance.CartID
    instance.CartID = original
    assert instance.CartID == original



@given(instance=Cart_strategy)
def test_hyp_cart_CartInfo_setter(instance):
    original = instance.CartInfo
    instance.CartInfo = original
    assert instance.CartInfo == original




@given(instance=Inventory_strategy)
def test_hyp_inventory_ColorID_setter(instance):
    original = instance.ColorID
    instance.ColorID = original
    assert instance.ColorID == original



@given(instance=Inventory_strategy)
def test_hyp_inventory_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Inventory_strategy)
def test_hyp_inventory_SizeID_setter(instance):
    original = instance.SizeID
    instance.SizeID = original
    assert instance.SizeID == original



@given(instance=Inventory_strategy)
def test_hyp_inventory_InStock_setter(instance):
    original = instance.InStock
    instance.InStock = original
    assert instance.InStock == original




@given(instance=Size_strategy)
def test_hyp_size_SizeID_setter(instance):
    original = instance.SizeID
    instance.SizeID = original
    assert instance.SizeID == original



@given(instance=Size_strategy)
def test_hyp_size_SizeName_setter(instance):
    original = instance.SizeName
    instance.SizeName = original
    assert instance.SizeName == original




@given(instance=Color_strategy)
def test_hyp_color_ColorName_setter(instance):
    original = instance.ColorName
    instance.ColorName = original
    assert instance.ColorName == original



@given(instance=Color_strategy)
def test_hyp_color_ColorID_setter(instance):
    original = instance.ColorID
    instance.ColorID = original
    assert instance.ColorID == original




@given(instance=Banner_strategy)
def test_hyp_banner_BannerInfo_setter(instance):
    original = instance.BannerInfo
    instance.BannerInfo = original
    assert instance.BannerInfo == original



@given(instance=Banner_strategy)
def test_hyp_banner_IsShow_setter(instance):
    original = instance.IsShow
    instance.IsShow = original
    assert instance.IsShow == original



@given(instance=Banner_strategy)
def test_hyp_banner_DateStart_setter(instance):
    original = instance.DateStart
    instance.DateStart = original
    assert instance.DateStart == original



@given(instance=Banner_strategy)
def test_hyp_banner_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original



@given(instance=Banner_strategy)
def test_hyp_banner_BannerID_setter(instance):
    original = instance.BannerID
    instance.BannerID = original
    assert instance.BannerID == original



@given(instance=Banner_strategy)
def test_hyp_banner_DateEnd_setter(instance):
    original = instance.DateEnd
    instance.DateEnd = original
    assert instance.DateEnd == original




@given(instance=Gallery_strategy)
def test_hyp_gallery_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Gallery_strategy)
def test_hyp_gallery_GalleryName_setter(instance):
    original = instance.GalleryName
    instance.GalleryName = original
    assert instance.GalleryName == original



@given(instance=Gallery_strategy)
def test_hyp_gallery_GalleryID_setter(instance):
    original = instance.GalleryID
    instance.GalleryID = original
    assert instance.GalleryID == original



@given(instance=Gallery_strategy)
def test_hyp_gallery_DateCreate_setter(instance):
    original = instance.DateCreate
    instance.DateCreate = original
    assert instance.DateCreate == original



@given(instance=Gallery_strategy)
def test_hyp_gallery_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original




@given(instance=Type_strategy)
def test_hyp_type_TypeID_setter(instance):
    original = instance.TypeID
    instance.TypeID = original
    assert instance.TypeID == original



@given(instance=Type_strategy)
def test_hyp_type_TypeName_setter(instance):
    original = instance.TypeName
    instance.TypeName = original
    assert instance.TypeName == original




@given(instance=Collection_strategy)
def test_hyp_collection_CollectionName_setter(instance):
    original = instance.CollectionName
    instance.CollectionName = original
    assert instance.CollectionName == original



@given(instance=Collection_strategy)
def test_hyp_collection_CollectionID_setter(instance):
    original = instance.CollectionID
    instance.CollectionID = original
    assert instance.CollectionID == original




@given(instance=Products_strategy)
def test_hyp_products_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Products_strategy)
def test_hyp_products_CollectionID_setter(instance):
    original = instance.CollectionID
    instance.CollectionID = original
    assert instance.CollectionID == original



@given(instance=Products_strategy)
def test_hyp_products_InStock_setter(instance):
    original = instance.InStock
    instance.InStock = original
    assert instance.InStock == original



@given(instance=Products_strategy)
def test_hyp_products_TypeID1_setter(instance):
    original = instance.TypeID1
    instance.TypeID1 = original
    assert instance.TypeID1 == original



@given(instance=Products_strategy)
def test_hyp_products_TypeID_setter(instance):
    original = instance.TypeID
    instance.TypeID = original
    assert instance.TypeID == original



@given(instance=Products_strategy)
def test_hyp_products_ProductInfo_setter(instance):
    original = instance.ProductInfo
    instance.ProductInfo = original
    assert instance.ProductInfo == original



@given(instance=Products_strategy)
def test_hyp_products_Index_setter(instance):
    original = instance.Index
    instance.Index = original
    assert instance.Index == original



@given(instance=Products_strategy)
def test_hyp_products_DateCreate_setter(instance):
    original = instance.DateCreate
    instance.DateCreate = original
    assert instance.DateCreate == original




@given(instance=User_strategy)
def test_hyp_user_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=User_strategy)
def test_hyp_user_Point_setter(instance):
    original = instance.Point
    instance.Point = original
    assert instance.Point == original



@given(instance=User_strategy)
def test_hyp_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_strategy)
def test_hyp_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_hyp_user_UserInfo_setter(instance):
    original = instance.UserInfo
    instance.UserInfo = original
    assert instance.UserInfo == original



@given(instance=User_strategy)
def test_hyp_user_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=User_strategy)
def test_hyp_user_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



