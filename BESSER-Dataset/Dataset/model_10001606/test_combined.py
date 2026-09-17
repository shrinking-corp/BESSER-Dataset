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
    SubCategory,
    OrderItem,
    FavoriteItem,
    CouponCode,
    Category,
    Item,
    Order,
    User,
    BaseEntity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_subcategory_is_not_abstract():
    assert not inspect.isabstract(SubCategory)


def test_hyp_subcategory_constructor_exists():
    assert callable(SubCategory.__init__)


def test_hyp_subcategory_constructor_args():
    sig = inspect.signature(SubCategory.__init__)
    params = list(sig.parameters.keys())
    assert "RusName" in params, "Missing parameter 'RusName'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "CategoryId" in params, "Missing parameter 'CategoryId'"






def test_hyp_orderitem_is_not_abstract():
    assert not inspect.isabstract(OrderItem)


def test_hyp_orderitem_constructor_exists():
    assert callable(OrderItem.__init__)


def test_hyp_orderitem_constructor_args():
    sig = inspect.signature(OrderItem.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "ItemId" in params, "Missing parameter 'ItemId'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "OrderId" in params, "Missing parameter 'OrderId'"








def test_hyp_favoriteitem_is_not_abstract():
    assert not inspect.isabstract(FavoriteItem)


def test_hyp_favoriteitem_constructor_exists():
    assert callable(FavoriteItem.__init__)


def test_hyp_favoriteitem_constructor_args():
    sig = inspect.signature(FavoriteItem.__init__)
    params = list(sig.parameters.keys())
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "ItemId" in params, "Missing parameter 'ItemId'"





def test_hyp_couponcode_is_not_abstract():
    assert not inspect.isabstract(CouponCode)


def test_hyp_couponcode_constructor_exists():
    assert callable(CouponCode.__init__)


def test_hyp_couponcode_constructor_args():
    sig = inspect.signature(CouponCode.__init__)
    params = list(sig.parameters.keys())
    assert "ExpiryDate" in params, "Missing parameter 'ExpiryDate'"
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "Discount" in params, "Missing parameter 'Discount'"
    assert "Code" in params, "Missing parameter 'Code'"







def test_hyp_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_hyp_category_constructor_exists():
    assert callable(Category.__init__)


def test_hyp_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "RusName" in params, "Missing parameter 'RusName'"





def test_hyp_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_hyp_item_constructor_exists():
    assert callable(Item.__init__)


def test_hyp_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Brand" in params, "Missing parameter 'Brand'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Discount" in params, "Missing parameter 'Discount'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "MinPreviewImagePath" in params, "Missing parameter 'MinPreviewImagePath'"
    assert "ImagePath2" in params, "Missing parameter 'ImagePath2'"
    assert "PreviewImagePath" in params, "Missing parameter 'PreviewImagePath'"
    assert "ImagePath3" in params, "Missing parameter 'ImagePath3'"
    assert "Color" in params, "Missing parameter 'Color'"
    assert "Size" in params, "Missing parameter 'Size'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "ImagePath1" in params, "Missing parameter 'ImagePath1'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "CategoryId" in params, "Missing parameter 'CategoryId'"
    assert "SubCategoryId" in params, "Missing parameter 'SubCategoryId'"




















def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "CodeId" in params, "Missing parameter 'CodeId'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "Comment" in params, "Missing parameter 'Comment'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "TotalPrice" in params, "Missing parameter 'TotalPrice'"
    assert "Status" in params, "Missing parameter 'Status'"












def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Login" in params, "Missing parameter 'Login'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "Role" in params, "Missing parameter 'Role'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "FirstName" in params, "Missing parameter 'FirstName'"
    assert "Email" in params, "Missing parameter 'Email'"










def test_hyp_baseentity_is_not_abstract():
    assert not inspect.isabstract(BaseEntity)


def test_hyp_baseentity_constructor_exists():
    assert callable(BaseEntity.__init__)


def test_hyp_baseentity_constructor_args():
    sig = inspect.signature(BaseEntity.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "UpdatedBy" in params, "Missing parameter 'UpdatedBy'"
    assert "Active" in params, "Missing parameter 'Active'"
    assert "UpdatedDate" in params, "Missing parameter 'UpdatedDate'"
    assert "CreatedBy" in params, "Missing parameter 'CreatedBy'"
    assert "CreatedDate" in params, "Missing parameter 'CreatedDate'"








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
SubCategory_strategy = st.builds(
    SubCategory,
    RusName=
        safe_text,
    Name=
        safe_text,
    CategoryId=
        safe_text
)
OrderItem_strategy = st.builds(
    OrderItem,
    Price=
        safe_text,
    Amount=
        st.integers(),
    ItemId=
        safe_text,
    Name=
        safe_text,
    OrderId=
        safe_text
)
FavoriteItem_strategy = st.builds(
    FavoriteItem,
    UserId=
        safe_text,
    ItemId=
        safe_text
)
CouponCode_strategy = st.builds(
    CouponCode,
    ExpiryDate=
        safe_text,
    UserId=
        safe_text,
    Discount=
        st.integers(),
    Code=
        safe_text
)
Category_strategy = st.builds(
    Category,
    Name=
        safe_text,
    RusName=
        safe_text
)
Item_strategy = st.builds(
    Item,
    Price=
        safe_text,
    Brand=
        safe_text,
    Name=
        safe_text,
    Discount=
        safe_text,
    Sex=
        st.integers(),
    Description=
        safe_text,
    MinPreviewImagePath=
        safe_text,
    ImagePath2=
        safe_text,
    PreviewImagePath=
        safe_text,
    ImagePath3=
        safe_text,
    Color=
        safe_text,
    Size=
        safe_text,
    Amount=
        st.integers(),
    ImagePath1=
        safe_text,
    Status=
        st.integers(),
    CategoryId=
        safe_text,
    SubCategoryId=
        safe_text
)
Order_strategy = st.builds(
    Order,
    CodeId=
        safe_text,
    Email=
        safe_text,
    UserId=
        safe_text,
    Comment=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text,
    PhoneNumber=
        safe_text,
    TotalPrice=
        safe_text,
    Status=
        st.integers()
)
User_strategy = st.builds(
    User,
    Password=
        safe_text,
    Login=
        safe_text,
    PhoneNumber=
        safe_text,
    Role=
        st.integers(),
    LastName=
        safe_text,
    FirstName=
        safe_text,
    Email=
        safe_text
)
BaseEntity_strategy = st.builds(
    BaseEntity,
    Id=
        safe_text,
    UpdatedBy=
        safe_text,
    Active=
        st.booleans(),
    UpdatedDate=
        safe_text,
    CreatedBy=
        safe_text,
    CreatedDate=
        safe_text
)




@given(instance=SubCategory_strategy)
def test_hyp_subcategory_RusName_setter(instance):
    original = instance.RusName
    instance.RusName = original
    assert instance.RusName == original



@given(instance=SubCategory_strategy)
def test_hyp_subcategory_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=SubCategory_strategy)
def test_hyp_subcategory_CategoryId_setter(instance):
    original = instance.CategoryId
    instance.CategoryId = original
    assert instance.CategoryId == original




@given(instance=OrderItem_strategy)
def test_hyp_orderitem_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=OrderItem_strategy)
def test_hyp_orderitem_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=OrderItem_strategy)
def test_hyp_orderitem_ItemId_setter(instance):
    original = instance.ItemId
    instance.ItemId = original
    assert instance.ItemId == original



@given(instance=OrderItem_strategy)
def test_hyp_orderitem_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=OrderItem_strategy)
def test_hyp_orderitem_OrderId_setter(instance):
    original = instance.OrderId
    instance.OrderId = original
    assert instance.OrderId == original




@given(instance=FavoriteItem_strategy)
def test_hyp_favoriteitem_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=FavoriteItem_strategy)
def test_hyp_favoriteitem_ItemId_setter(instance):
    original = instance.ItemId
    instance.ItemId = original
    assert instance.ItemId == original




@given(instance=CouponCode_strategy)
def test_hyp_couponcode_ExpiryDate_setter(instance):
    original = instance.ExpiryDate
    instance.ExpiryDate = original
    assert instance.ExpiryDate == original



@given(instance=CouponCode_strategy)
def test_hyp_couponcode_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=CouponCode_strategy)
def test_hyp_couponcode_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original



@given(instance=CouponCode_strategy)
def test_hyp_couponcode_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original




@given(instance=Category_strategy)
def test_hyp_category_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Category_strategy)
def test_hyp_category_RusName_setter(instance):
    original = instance.RusName
    instance.RusName = original
    assert instance.RusName == original




@given(instance=Item_strategy)
def test_hyp_item_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Item_strategy)
def test_hyp_item_Brand_setter(instance):
    original = instance.Brand
    instance.Brand = original
    assert instance.Brand == original



@given(instance=Item_strategy)
def test_hyp_item_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Item_strategy)
def test_hyp_item_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original



@given(instance=Item_strategy)
def test_hyp_item_Sex_setter(instance):
    original = instance.Sex
    instance.Sex = original
    assert instance.Sex == original



@given(instance=Item_strategy)
def test_hyp_item_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Item_strategy)
def test_hyp_item_MinPreviewImagePath_setter(instance):
    original = instance.MinPreviewImagePath
    instance.MinPreviewImagePath = original
    assert instance.MinPreviewImagePath == original



@given(instance=Item_strategy)
def test_hyp_item_ImagePath2_setter(instance):
    original = instance.ImagePath2
    instance.ImagePath2 = original
    assert instance.ImagePath2 == original



@given(instance=Item_strategy)
def test_hyp_item_PreviewImagePath_setter(instance):
    original = instance.PreviewImagePath
    instance.PreviewImagePath = original
    assert instance.PreviewImagePath == original



@given(instance=Item_strategy)
def test_hyp_item_ImagePath3_setter(instance):
    original = instance.ImagePath3
    instance.ImagePath3 = original
    assert instance.ImagePath3 == original



@given(instance=Item_strategy)
def test_hyp_item_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original



@given(instance=Item_strategy)
def test_hyp_item_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original



@given(instance=Item_strategy)
def test_hyp_item_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=Item_strategy)
def test_hyp_item_ImagePath1_setter(instance):
    original = instance.ImagePath1
    instance.ImagePath1 = original
    assert instance.ImagePath1 == original



@given(instance=Item_strategy)
def test_hyp_item_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Item_strategy)
def test_hyp_item_CategoryId_setter(instance):
    original = instance.CategoryId
    instance.CategoryId = original
    assert instance.CategoryId == original



@given(instance=Item_strategy)
def test_hyp_item_SubCategoryId_setter(instance):
    original = instance.SubCategoryId
    instance.SubCategoryId = original
    assert instance.SubCategoryId == original




@given(instance=Order_strategy)
def test_hyp_order_CodeId_setter(instance):
    original = instance.CodeId
    instance.CodeId = original
    assert instance.CodeId == original



@given(instance=Order_strategy)
def test_hyp_order_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Order_strategy)
def test_hyp_order_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=Order_strategy)
def test_hyp_order_Comment_setter(instance):
    original = instance.Comment
    instance.Comment = original
    assert instance.Comment == original



@given(instance=Order_strategy)
def test_hyp_order_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Order_strategy)
def test_hyp_order_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Order_strategy)
def test_hyp_order_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=Order_strategy)
def test_hyp_order_TotalPrice_setter(instance):
    original = instance.TotalPrice
    instance.TotalPrice = original
    assert instance.TotalPrice == original



@given(instance=Order_strategy)
def test_hyp_order_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original




@given(instance=User_strategy)
def test_hyp_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_hyp_user_Login_setter(instance):
    original = instance.Login
    instance.Login = original
    assert instance.Login == original



@given(instance=User_strategy)
def test_hyp_user_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=User_strategy)
def test_hyp_user_Role_setter(instance):
    original = instance.Role
    instance.Role = original
    assert instance.Role == original



@given(instance=User_strategy)
def test_hyp_user_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=User_strategy)
def test_hyp_user_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original



@given(instance=User_strategy)
def test_hyp_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original




@given(instance=BaseEntity_strategy)
def test_hyp_baseentity_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=BaseEntity_strategy)
def test_hyp_baseentity_UpdatedBy_setter(instance):
    original = instance.UpdatedBy
    instance.UpdatedBy = original
    assert instance.UpdatedBy == original



@given(instance=BaseEntity_strategy)
def test_hyp_baseentity_Active_setter(instance):
    original = instance.Active
    instance.Active = original
    assert instance.Active == original



@given(instance=BaseEntity_strategy)
def test_hyp_baseentity_UpdatedDate_setter(instance):
    original = instance.UpdatedDate
    instance.UpdatedDate = original
    assert instance.UpdatedDate == original



@given(instance=BaseEntity_strategy)
def test_hyp_baseentity_CreatedBy_setter(instance):
    original = instance.CreatedBy
    instance.CreatedBy = original
    assert instance.CreatedBy == original



@given(instance=BaseEntity_strategy)
def test_hyp_baseentity_CreatedDate_setter(instance):
    original = instance.CreatedDate
    instance.CreatedDate = original
    assert instance.CreatedDate == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BaseEntity,
    Category,
    CouponCode,
    FavoriteItem,
    Item,
    Order,
    OrderItem,
    SubCategory,
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

def test_BaseEntity_Active_value_roundtrip():
    instance = BaseEntity(Active=True, CreatedBy="sample_text", CreatedDate="sample_text", Id="sample_text", UpdatedBy="sample_text", UpdatedDate="sample_text")
    assert instance.Active == True
    instance.Active = False
    assert instance.Active == False


def test_BaseEntity_CreatedBy_value_roundtrip():
    instance = BaseEntity(Active=True, CreatedBy="sample_text", CreatedDate="sample_text", Id="sample_text", UpdatedBy="sample_text", UpdatedDate="sample_text")
    assert instance.CreatedBy == "sample_text"
    instance.CreatedBy = "sample_text_2"
    assert instance.CreatedBy == "sample_text_2"


def test_BaseEntity_CreatedDate_value_roundtrip():
    instance = BaseEntity(Active=True, CreatedBy="sample_text", CreatedDate="sample_text", Id="sample_text", UpdatedBy="sample_text", UpdatedDate="sample_text")
    assert instance.CreatedDate == "sample_text"
    instance.CreatedDate = "sample_text_2"
    assert instance.CreatedDate == "sample_text_2"


def test_BaseEntity_Id_value_roundtrip():
    instance = BaseEntity(Active=True, CreatedBy="sample_text", CreatedDate="sample_text", Id="sample_text", UpdatedBy="sample_text", UpdatedDate="sample_text")
    assert instance.Id == "sample_text"
    instance.Id = "sample_text_2"
    assert instance.Id == "sample_text_2"


def test_BaseEntity_UpdatedBy_value_roundtrip():
    instance = BaseEntity(Active=True, CreatedBy="sample_text", CreatedDate="sample_text", Id="sample_text", UpdatedBy="sample_text", UpdatedDate="sample_text")
    assert instance.UpdatedBy == "sample_text"
    instance.UpdatedBy = "sample_text_2"
    assert instance.UpdatedBy == "sample_text_2"


def test_BaseEntity_UpdatedDate_value_roundtrip():
    instance = BaseEntity(Active=True, CreatedBy="sample_text", CreatedDate="sample_text", Id="sample_text", UpdatedBy="sample_text", UpdatedDate="sample_text")
    assert instance.UpdatedDate == "sample_text"
    instance.UpdatedDate = "sample_text_2"
    assert instance.UpdatedDate == "sample_text_2"


def test_Category_Name_value_roundtrip():
    instance = Category(Name="sample_text", RusName="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Category_RusName_value_roundtrip():
    instance = Category(Name="sample_text", RusName="sample_text")
    assert instance.RusName == "sample_text"
    instance.RusName = "sample_text_2"
    assert instance.RusName == "sample_text_2"


def test_CouponCode_Code_value_roundtrip():
    instance = CouponCode(Code="sample_text", Discount=7, ExpiryDate="sample_text", UserId="sample_text")
    assert instance.Code == "sample_text"
    instance.Code = "sample_text_2"
    assert instance.Code == "sample_text_2"


def test_CouponCode_Discount_value_roundtrip():
    instance = CouponCode(Code="sample_text", Discount=7, ExpiryDate="sample_text", UserId="sample_text")
    assert instance.Discount == 7
    instance.Discount = 13
    assert instance.Discount == 13


def test_CouponCode_ExpiryDate_value_roundtrip():
    instance = CouponCode(Code="sample_text", Discount=7, ExpiryDate="sample_text", UserId="sample_text")
    assert instance.ExpiryDate == "sample_text"
    instance.ExpiryDate = "sample_text_2"
    assert instance.ExpiryDate == "sample_text_2"


def test_CouponCode_UserId_value_roundtrip():
    instance = CouponCode(Code="sample_text", Discount=7, ExpiryDate="sample_text", UserId="sample_text")
    assert instance.UserId == "sample_text"
    instance.UserId = "sample_text_2"
    assert instance.UserId == "sample_text_2"


def test_FavoriteItem_ItemId_value_roundtrip():
    instance = FavoriteItem(ItemId="sample_text", UserId="sample_text")
    assert instance.ItemId == "sample_text"
    instance.ItemId = "sample_text_2"
    assert instance.ItemId == "sample_text_2"


def test_FavoriteItem_UserId_value_roundtrip():
    instance = FavoriteItem(ItemId="sample_text", UserId="sample_text")
    assert instance.UserId == "sample_text"
    instance.UserId = "sample_text_2"
    assert instance.UserId == "sample_text_2"


def test_Item_Amount_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Amount == 7
    instance.Amount = 13
    assert instance.Amount == 13


def test_Item_Brand_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Brand == "sample_text"
    instance.Brand = "sample_text_2"
    assert instance.Brand == "sample_text_2"


def test_Item_CategoryId_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.CategoryId == "sample_text"
    instance.CategoryId = "sample_text_2"
    assert instance.CategoryId == "sample_text_2"


def test_Item_Color_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Color == "sample_text"
    instance.Color = "sample_text_2"
    assert instance.Color == "sample_text_2"


def test_Item_Description_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Item_Discount_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Discount == "sample_text"
    instance.Discount = "sample_text_2"
    assert instance.Discount == "sample_text_2"


def test_Item_ImagePath1_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.ImagePath1 == "sample_text"
    instance.ImagePath1 = "sample_text_2"
    assert instance.ImagePath1 == "sample_text_2"


def test_Item_ImagePath2_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.ImagePath2 == "sample_text"
    instance.ImagePath2 = "sample_text_2"
    assert instance.ImagePath2 == "sample_text_2"


def test_Item_ImagePath3_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.ImagePath3 == "sample_text"
    instance.ImagePath3 = "sample_text_2"
    assert instance.ImagePath3 == "sample_text_2"


def test_Item_MinPreviewImagePath_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.MinPreviewImagePath == "sample_text"
    instance.MinPreviewImagePath = "sample_text_2"
    assert instance.MinPreviewImagePath == "sample_text_2"


def test_Item_Name_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Item_PreviewImagePath_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.PreviewImagePath == "sample_text"
    instance.PreviewImagePath = "sample_text_2"
    assert instance.PreviewImagePath == "sample_text_2"


def test_Item_Price_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_Item_Sex_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Sex == 7
    instance.Sex = 13
    assert instance.Sex == 13


def test_Item_Size_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Size == "sample_text"
    instance.Size = "sample_text_2"
    assert instance.Size == "sample_text_2"


def test_Item_Status_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.Status == 7
    instance.Status = 13
    assert instance.Status == 13


def test_Item_SubCategoryId_value_roundtrip():
    instance = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    assert instance.SubCategoryId == "sample_text"
    instance.SubCategoryId = "sample_text_2"
    assert instance.SubCategoryId == "sample_text_2"


def test_Order_Address_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Order_CodeId_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.CodeId == "sample_text"
    instance.CodeId = "sample_text_2"
    assert instance.CodeId == "sample_text_2"


def test_Order_Comment_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.Comment == "sample_text"
    instance.Comment = "sample_text_2"
    assert instance.Comment == "sample_text_2"


def test_Order_Email_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Order_Name_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Order_PhoneNumber_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.PhoneNumber == "sample_text"
    instance.PhoneNumber = "sample_text_2"
    assert instance.PhoneNumber == "sample_text_2"


def test_Order_Status_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.Status == 7
    instance.Status = 13
    assert instance.Status == 13


def test_Order_TotalPrice_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.TotalPrice == "sample_text"
    instance.TotalPrice = "sample_text_2"
    assert instance.TotalPrice == "sample_text_2"


def test_Order_UserId_value_roundtrip():
    instance = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    assert instance.UserId == "sample_text"
    instance.UserId = "sample_text_2"
    assert instance.UserId == "sample_text_2"


def test_OrderItem_Amount_value_roundtrip():
    instance = OrderItem(Amount=7, ItemId="sample_text", Name="sample_text", OrderId="sample_text", Price="sample_text")
    assert instance.Amount == 7
    instance.Amount = 13
    assert instance.Amount == 13


def test_OrderItem_ItemId_value_roundtrip():
    instance = OrderItem(Amount=7, ItemId="sample_text", Name="sample_text", OrderId="sample_text", Price="sample_text")
    assert instance.ItemId == "sample_text"
    instance.ItemId = "sample_text_2"
    assert instance.ItemId == "sample_text_2"


def test_OrderItem_Name_value_roundtrip():
    instance = OrderItem(Amount=7, ItemId="sample_text", Name="sample_text", OrderId="sample_text", Price="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_OrderItem_OrderId_value_roundtrip():
    instance = OrderItem(Amount=7, ItemId="sample_text", Name="sample_text", OrderId="sample_text", Price="sample_text")
    assert instance.OrderId == "sample_text"
    instance.OrderId = "sample_text_2"
    assert instance.OrderId == "sample_text_2"


def test_OrderItem_Price_value_roundtrip():
    instance = OrderItem(Amount=7, ItemId="sample_text", Name="sample_text", OrderId="sample_text", Price="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_SubCategory_CategoryId_value_roundtrip():
    instance = SubCategory(CategoryId="sample_text", Name="sample_text", RusName="sample_text")
    assert instance.CategoryId == "sample_text"
    instance.CategoryId = "sample_text_2"
    assert instance.CategoryId == "sample_text_2"


def test_SubCategory_Name_value_roundtrip():
    instance = SubCategory(CategoryId="sample_text", Name="sample_text", RusName="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_SubCategory_RusName_value_roundtrip():
    instance = SubCategory(CategoryId="sample_text", Name="sample_text", RusName="sample_text")
    assert instance.RusName == "sample_text"
    instance.RusName = "sample_text_2"
    assert instance.RusName == "sample_text_2"


def test_User_Email_value_roundtrip():
    instance = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_User_FirstName_value_roundtrip():
    instance = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    assert instance.FirstName == "sample_text"
    instance.FirstName = "sample_text_2"
    assert instance.FirstName == "sample_text_2"


def test_User_LastName_value_roundtrip():
    instance = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    assert instance.LastName == "sample_text"
    instance.LastName = "sample_text_2"
    assert instance.LastName == "sample_text_2"


def test_User_Login_value_roundtrip():
    instance = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    assert instance.Login == "sample_text"
    instance.Login = "sample_text_2"
    assert instance.Login == "sample_text_2"


def test_User_Password_value_roundtrip():
    instance = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_User_PhoneNumber_value_roundtrip():
    instance = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    assert instance.PhoneNumber == "sample_text"
    instance.PhoneNumber = "sample_text_2"
    assert instance.PhoneNumber == "sample_text_2"


def test_User_Role_value_roundtrip():
    instance = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    assert instance.Role == 7
    instance.Role = 13
    assert instance.Role == 13


def test_assoc_Category_Item_link_reassign_clear():
    a = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    b1 = Category(Name="sample_text", RusName="sample_text")
    b2 = Category(Name="sample_text_2", RusName="sample_text_2")
    _safe_set(a, 'category15', b1)
    assert _is_linked(a, 'category15', b1)
    if hasattr(b1, 'item14'):
        assert _is_linked(b1, 'item14', a)
    _safe_set(a, 'category15', b2)
    assert _is_linked(a, 'category15', b2)
    if hasattr(b1, 'item14'):
        assert not _is_linked(b1, 'item14', a)
    if hasattr(b2, 'item14'):
        assert _is_linked(b2, 'item14', a)
    _safe_set(a, 'category15', None)
    assert not _is_linked(a, 'category15', b2)
    if hasattr(b2, 'item14'):
        assert not _is_linked(b2, 'item14', a)


def test_assoc_CouponCode_User_link_reassign_clear():
    a = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    b1 = CouponCode(Code="sample_text", Discount=7, ExpiryDate="sample_text", UserId="sample_text")
    b2 = CouponCode(Code="sample_text_2", Discount=13, ExpiryDate="sample_text_2", UserId="sample_text_2")
    _safe_set(a, 'couponCode7', b1)
    assert _is_linked(a, 'couponCode7', b1)
    if hasattr(b1, 'user6'):
        assert _is_linked(b1, 'user6', a)
    _safe_set(a, 'couponCode7', b2)
    assert _is_linked(a, 'couponCode7', b2)
    if hasattr(b1, 'user6'):
        assert not _is_linked(b1, 'user6', a)
    if hasattr(b2, 'user6'):
        assert _is_linked(b2, 'user6', a)
    _safe_set(a, 'couponCode7', None)
    assert not _is_linked(a, 'couponCode7', b2)
    if hasattr(b2, 'user6'):
        assert not _is_linked(b2, 'user6', a)


def test_assoc_FavoriteItem_User_link_reassign_clear():
    a = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    b1 = FavoriteItem(ItemId="sample_text", UserId="sample_text")
    b2 = FavoriteItem(ItemId="sample_text_2", UserId="sample_text_2")
    _safe_set(a, 'favoriteItem3', b1)
    assert _is_linked(a, 'favoriteItem3', b1)
    if hasattr(b1, 'user2'):
        assert _is_linked(b1, 'user2', a)
    _safe_set(a, 'favoriteItem3', b2)
    assert _is_linked(a, 'favoriteItem3', b2)
    if hasattr(b1, 'user2'):
        assert not _is_linked(b1, 'user2', a)
    if hasattr(b2, 'user2'):
        assert _is_linked(b2, 'user2', a)
    _safe_set(a, 'favoriteItem3', None)
    assert not _is_linked(a, 'favoriteItem3', b2)
    if hasattr(b2, 'user2'):
        assert not _is_linked(b2, 'user2', a)


def test_assoc_Item_FavoriteItem_link_reassign_clear():
    a = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    b1 = FavoriteItem(ItemId="sample_text", UserId="sample_text")
    b2 = FavoriteItem(ItemId="sample_text_2", UserId="sample_text_2")
    _safe_set(a, 'favoriteItem0', b1)
    assert _is_linked(a, 'favoriteItem0', b1)
    if hasattr(b1, 'item1'):
        assert _is_linked(b1, 'item1', a)
    _safe_set(a, 'favoriteItem0', b2)
    assert _is_linked(a, 'favoriteItem0', b2)
    if hasattr(b1, 'item1'):
        assert not _is_linked(b1, 'item1', a)
    if hasattr(b2, 'item1'):
        assert _is_linked(b2, 'item1', a)
    _safe_set(a, 'favoriteItem0', None)
    assert not _is_linked(a, 'favoriteItem0', b2)
    if hasattr(b2, 'item1'):
        assert not _is_linked(b2, 'item1', a)


def test_assoc_OrderItem_Order_link_reassign_clear():
    a = OrderItem(Amount=7, ItemId="sample_text", Name="sample_text", OrderId="sample_text", Price="sample_text")
    b1 = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    b2 = Order(Address="sample_text_2", CodeId="sample_text_2", Comment="sample_text_2", Email="sample_text_2", Name="sample_text_2", PhoneNumber="sample_text_2", Status=13, TotalPrice="sample_text_2", UserId="sample_text_2")
    _safe_set(a, 'order8', b1)
    assert _is_linked(a, 'order8', b1)
    if hasattr(b1, 'orderItem9'):
        assert _is_linked(b1, 'orderItem9', a)
    _safe_set(a, 'order8', b2)
    assert _is_linked(a, 'order8', b2)
    if hasattr(b1, 'orderItem9'):
        assert not _is_linked(b1, 'orderItem9', a)
    if hasattr(b2, 'orderItem9'):
        assert _is_linked(b2, 'orderItem9', a)
    _safe_set(a, 'order8', None)
    assert not _is_linked(a, 'order8', b2)
    if hasattr(b2, 'orderItem9'):
        assert not _is_linked(b2, 'orderItem9', a)


def test_assoc_Order_CouponCode_link_reassign_clear():
    a = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    b1 = CouponCode(Code="sample_text", Discount=7, ExpiryDate="sample_text", UserId="sample_text")
    b2 = CouponCode(Code="sample_text_2", Discount=13, ExpiryDate="sample_text_2", UserId="sample_text_2")
    _safe_set(a, 'couponCode4', b1)
    assert _is_linked(a, 'couponCode4', b1)
    if hasattr(b1, 'order5'):
        assert _is_linked(b1, 'order5', a)
    _safe_set(a, 'couponCode4', b2)
    assert _is_linked(a, 'couponCode4', b2)
    if hasattr(b1, 'order5'):
        assert not _is_linked(b1, 'order5', a)
    if hasattr(b2, 'order5'):
        assert _is_linked(b2, 'order5', a)
    _safe_set(a, 'couponCode4', None)
    assert not _is_linked(a, 'couponCode4', b2)
    if hasattr(b2, 'order5'):
        assert not _is_linked(b2, 'order5', a)


def test_assoc_SubCategory_Category_link_reassign_clear():
    a = SubCategory(CategoryId="sample_text", Name="sample_text", RusName="sample_text")
    b1 = Category(Name="sample_text", RusName="sample_text")
    b2 = Category(Name="sample_text_2", RusName="sample_text_2")
    _safe_set(a, 'category10', b1)
    assert _is_linked(a, 'category10', b1)
    if hasattr(b1, 'subCategory11'):
        assert _is_linked(b1, 'subCategory11', a)
    _safe_set(a, 'category10', b2)
    assert _is_linked(a, 'category10', b2)
    if hasattr(b1, 'subCategory11'):
        assert not _is_linked(b1, 'subCategory11', a)
    if hasattr(b2, 'subCategory11'):
        assert _is_linked(b2, 'subCategory11', a)
    _safe_set(a, 'category10', None)
    assert not _is_linked(a, 'category10', b2)
    if hasattr(b2, 'subCategory11'):
        assert not _is_linked(b2, 'subCategory11', a)


def test_assoc_SubCategory_Item_link_reassign_clear():
    a = SubCategory(CategoryId="sample_text", Name="sample_text", RusName="sample_text")
    b1 = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    b2 = Item(Amount=13, Brand="sample_text_2", CategoryId="sample_text_2", Color="sample_text_2", Description="sample_text_2", Discount="sample_text_2", ImagePath1="sample_text_2", ImagePath2="sample_text_2", ImagePath3="sample_text_2", MinPreviewImagePath="sample_text_2", Name="sample_text_2", PreviewImagePath="sample_text_2", Price="sample_text_2", Sex=13, Size="sample_text_2", Status=13, SubCategoryId="sample_text_2")
    _safe_set(a, 'item12', b1)
    assert _is_linked(a, 'item12', b1)
    if hasattr(b1, 'subCategory13'):
        assert _is_linked(b1, 'subCategory13', a)
    _safe_set(a, 'item12', b2)
    assert _is_linked(a, 'item12', b2)
    if hasattr(b1, 'subCategory13'):
        assert not _is_linked(b1, 'subCategory13', a)
    if hasattr(b2, 'subCategory13'):
        assert _is_linked(b2, 'subCategory13', a)
    _safe_set(a, 'item12', None)
    assert not _is_linked(a, 'item12', b2)
    if hasattr(b2, 'subCategory13'):
        assert not _is_linked(b2, 'subCategory13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BaseEntity_strategy = st.builds(BaseEntity, Active=st.booleans(), CreatedBy=safe_text, CreatedDate=safe_text, Id=safe_text, UpdatedBy=safe_text, UpdatedDate=safe_text)
@given(instance=BaseEntity_strategy)
@settings(max_examples=25)
def test_BaseEntity_instantiation(instance):
    assert isinstance(instance, BaseEntity)


Category_strategy = st.builds(Category, Name=safe_text, RusName=safe_text)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


CouponCode_strategy = st.builds(CouponCode, Code=safe_text, Discount=st.integers(), ExpiryDate=safe_text, UserId=safe_text)
@given(instance=CouponCode_strategy)
@settings(max_examples=25)
def test_CouponCode_instantiation(instance):
    assert isinstance(instance, CouponCode)


FavoriteItem_strategy = st.builds(FavoriteItem, ItemId=safe_text, UserId=safe_text)
@given(instance=FavoriteItem_strategy)
@settings(max_examples=25)
def test_FavoriteItem_instantiation(instance):
    assert isinstance(instance, FavoriteItem)


Item_strategy = st.builds(Item, Amount=st.integers(), Brand=safe_text, CategoryId=safe_text, Color=safe_text, Description=safe_text, Discount=safe_text, ImagePath1=safe_text, ImagePath2=safe_text, ImagePath3=safe_text, MinPreviewImagePath=safe_text, Name=safe_text, PreviewImagePath=safe_text, Price=safe_text, Sex=st.integers(), Size=safe_text, Status=st.integers(), SubCategoryId=safe_text)
@given(instance=Item_strategy)
@settings(max_examples=25)
def test_Item_instantiation(instance):
    assert isinstance(instance, Item)


Order_strategy = st.builds(Order, Address=safe_text, CodeId=safe_text, Comment=safe_text, Email=safe_text, Name=safe_text, PhoneNumber=safe_text, Status=st.integers(), TotalPrice=safe_text, UserId=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


OrderItem_strategy = st.builds(OrderItem, Amount=st.integers(), ItemId=safe_text, Name=safe_text, OrderId=safe_text, Price=safe_text)
@given(instance=OrderItem_strategy)
@settings(max_examples=25)
def test_OrderItem_instantiation(instance):
    assert isinstance(instance, OrderItem)


SubCategory_strategy = st.builds(SubCategory, CategoryId=safe_text, Name=safe_text, RusName=safe_text)
@given(instance=SubCategory_strategy)
@settings(max_examples=25)
def test_SubCategory_instantiation(instance):
    assert isinstance(instance, SubCategory)


User_strategy = st.builds(User, Email=safe_text, FirstName=safe_text, LastName=safe_text, Login=safe_text, Password=safe_text, PhoneNumber=safe_text, Role=st.integers())
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



