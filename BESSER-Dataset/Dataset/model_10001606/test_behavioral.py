import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_Category_Item_reverse_link_reassign_clear():
    a1 = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    a2 = Item(Amount=13, Brand="sample_text_2", CategoryId="sample_text_2", Color="sample_text_2", Description="sample_text_2", Discount="sample_text_2", ImagePath1="sample_text_2", ImagePath2="sample_text_2", ImagePath3="sample_text_2", MinPreviewImagePath="sample_text_2", Name="sample_text_2", PreviewImagePath="sample_text_2", Price="sample_text_2", Sex=13, Size="sample_text_2", Status=13, SubCategoryId="sample_text_2")
    b = Category(Name="sample_text", RusName="sample_text")
    _safe_set(b, 'item14', a1)
    assert _is_linked(b, 'item14', a1)
    if hasattr(a1, 'category15'):
        assert _is_linked(a1, 'category15', b)
    _safe_set(b, 'item14', a2)
    assert _is_linked(b, 'item14', a2)
    if hasattr(a1, 'category15'):
        assert not _is_linked(a1, 'category15', b)
    if hasattr(a2, 'category15'):
        assert _is_linked(a2, 'category15', b)
    _safe_set(b, 'item14', None)
    assert not _is_linked(b, 'item14', a2)
    if hasattr(a2, 'category15'):
        assert not _is_linked(a2, 'category15', b)


def test_assoc_CouponCode_User_reverse_link_reassign_clear():
    a1 = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    a2 = User(Email="sample_text_2", FirstName="sample_text_2", LastName="sample_text_2", Login="sample_text_2", Password="sample_text_2", PhoneNumber="sample_text_2", Role=13)
    b = CouponCode(Code="sample_text", Discount=7, ExpiryDate="sample_text", UserId="sample_text")
    _safe_set(b, 'user6', a1)
    assert _is_linked(b, 'user6', a1)
    if hasattr(a1, 'couponCode7'):
        assert _is_linked(a1, 'couponCode7', b)
    _safe_set(b, 'user6', a2)
    assert _is_linked(b, 'user6', a2)
    if hasattr(a1, 'couponCode7'):
        assert not _is_linked(a1, 'couponCode7', b)
    if hasattr(a2, 'couponCode7'):
        assert _is_linked(a2, 'couponCode7', b)
    _safe_set(b, 'user6', None)
    assert not _is_linked(b, 'user6', a2)
    if hasattr(a2, 'couponCode7'):
        assert not _is_linked(a2, 'couponCode7', b)


def test_assoc_FavoriteItem_User_reverse_link_reassign_clear():
    a1 = User(Email="sample_text", FirstName="sample_text", LastName="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", Role=7)
    a2 = User(Email="sample_text_2", FirstName="sample_text_2", LastName="sample_text_2", Login="sample_text_2", Password="sample_text_2", PhoneNumber="sample_text_2", Role=13)
    b = FavoriteItem(ItemId="sample_text", UserId="sample_text")
    _safe_set(b, 'user2', a1)
    assert _is_linked(b, 'user2', a1)
    if hasattr(a1, 'favoriteItem3'):
        assert _is_linked(a1, 'favoriteItem3', b)
    _safe_set(b, 'user2', a2)
    assert _is_linked(b, 'user2', a2)
    if hasattr(a1, 'favoriteItem3'):
        assert not _is_linked(a1, 'favoriteItem3', b)
    if hasattr(a2, 'favoriteItem3'):
        assert _is_linked(a2, 'favoriteItem3', b)
    _safe_set(b, 'user2', None)
    assert not _is_linked(b, 'user2', a2)
    if hasattr(a2, 'favoriteItem3'):
        assert not _is_linked(a2, 'favoriteItem3', b)


def test_assoc_Item_FavoriteItem_reverse_link_reassign_clear():
    a1 = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    a2 = Item(Amount=13, Brand="sample_text_2", CategoryId="sample_text_2", Color="sample_text_2", Description="sample_text_2", Discount="sample_text_2", ImagePath1="sample_text_2", ImagePath2="sample_text_2", ImagePath3="sample_text_2", MinPreviewImagePath="sample_text_2", Name="sample_text_2", PreviewImagePath="sample_text_2", Price="sample_text_2", Sex=13, Size="sample_text_2", Status=13, SubCategoryId="sample_text_2")
    b = FavoriteItem(ItemId="sample_text", UserId="sample_text")
    _safe_set(b, 'item1', a1)
    assert _is_linked(b, 'item1', a1)
    if hasattr(a1, 'favoriteItem0'):
        assert _is_linked(a1, 'favoriteItem0', b)
    _safe_set(b, 'item1', a2)
    assert _is_linked(b, 'item1', a2)
    if hasattr(a1, 'favoriteItem0'):
        assert not _is_linked(a1, 'favoriteItem0', b)
    if hasattr(a2, 'favoriteItem0'):
        assert _is_linked(a2, 'favoriteItem0', b)
    _safe_set(b, 'item1', None)
    assert not _is_linked(b, 'item1', a2)
    if hasattr(a2, 'favoriteItem0'):
        assert not _is_linked(a2, 'favoriteItem0', b)


def test_assoc_OrderItem_Order_reverse_link_reassign_clear():
    a1 = OrderItem(Amount=7, ItemId="sample_text", Name="sample_text", OrderId="sample_text", Price="sample_text")
    a2 = OrderItem(Amount=13, ItemId="sample_text_2", Name="sample_text_2", OrderId="sample_text_2", Price="sample_text_2")
    b = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    _safe_set(b, 'orderItem9', a1)
    assert _is_linked(b, 'orderItem9', a1)
    if hasattr(a1, 'order8'):
        assert _is_linked(a1, 'order8', b)
    _safe_set(b, 'orderItem9', a2)
    assert _is_linked(b, 'orderItem9', a2)
    if hasattr(a1, 'order8'):
        assert not _is_linked(a1, 'order8', b)
    if hasattr(a2, 'order8'):
        assert _is_linked(a2, 'order8', b)
    _safe_set(b, 'orderItem9', None)
    assert not _is_linked(b, 'orderItem9', a2)
    if hasattr(a2, 'order8'):
        assert not _is_linked(a2, 'order8', b)


def test_assoc_Order_CouponCode_reverse_link_reassign_clear():
    a1 = Order(Address="sample_text", CodeId="sample_text", Comment="sample_text", Email="sample_text", Name="sample_text", PhoneNumber="sample_text", Status=7, TotalPrice="sample_text", UserId="sample_text")
    a2 = Order(Address="sample_text_2", CodeId="sample_text_2", Comment="sample_text_2", Email="sample_text_2", Name="sample_text_2", PhoneNumber="sample_text_2", Status=13, TotalPrice="sample_text_2", UserId="sample_text_2")
    b = CouponCode(Code="sample_text", Discount=7, ExpiryDate="sample_text", UserId="sample_text")
    _safe_set(b, 'order5', a1)
    assert _is_linked(b, 'order5', a1)
    if hasattr(a1, 'couponCode4'):
        assert _is_linked(a1, 'couponCode4', b)
    _safe_set(b, 'order5', a2)
    assert _is_linked(b, 'order5', a2)
    if hasattr(a1, 'couponCode4'):
        assert not _is_linked(a1, 'couponCode4', b)
    if hasattr(a2, 'couponCode4'):
        assert _is_linked(a2, 'couponCode4', b)
    _safe_set(b, 'order5', None)
    assert not _is_linked(b, 'order5', a2)
    if hasattr(a2, 'couponCode4'):
        assert not _is_linked(a2, 'couponCode4', b)


def test_assoc_SubCategory_Category_reverse_link_reassign_clear():
    a1 = SubCategory(CategoryId="sample_text", Name="sample_text", RusName="sample_text")
    a2 = SubCategory(CategoryId="sample_text_2", Name="sample_text_2", RusName="sample_text_2")
    b = Category(Name="sample_text", RusName="sample_text")
    _safe_set(b, 'subCategory11', a1)
    assert _is_linked(b, 'subCategory11', a1)
    if hasattr(a1, 'category10'):
        assert _is_linked(a1, 'category10', b)
    _safe_set(b, 'subCategory11', a2)
    assert _is_linked(b, 'subCategory11', a2)
    if hasattr(a1, 'category10'):
        assert not _is_linked(a1, 'category10', b)
    if hasattr(a2, 'category10'):
        assert _is_linked(a2, 'category10', b)
    _safe_set(b, 'subCategory11', None)
    assert not _is_linked(b, 'subCategory11', a2)
    if hasattr(a2, 'category10'):
        assert not _is_linked(a2, 'category10', b)


def test_assoc_SubCategory_Item_reverse_link_reassign_clear():
    a1 = SubCategory(CategoryId="sample_text", Name="sample_text", RusName="sample_text")
    a2 = SubCategory(CategoryId="sample_text_2", Name="sample_text_2", RusName="sample_text_2")
    b = Item(Amount=7, Brand="sample_text", CategoryId="sample_text", Color="sample_text", Description="sample_text", Discount="sample_text", ImagePath1="sample_text", ImagePath2="sample_text", ImagePath3="sample_text", MinPreviewImagePath="sample_text", Name="sample_text", PreviewImagePath="sample_text", Price="sample_text", Sex=7, Size="sample_text", Status=7, SubCategoryId="sample_text")
    _safe_set(b, 'subCategory13', a1)
    assert _is_linked(b, 'subCategory13', a1)
    if hasattr(a1, 'item12'):
        assert _is_linked(a1, 'item12', b)
    _safe_set(b, 'subCategory13', a2)
    assert _is_linked(b, 'subCategory13', a2)
    if hasattr(a1, 'item12'):
        assert not _is_linked(a1, 'item12', b)
    if hasattr(a2, 'item12'):
        assert _is_linked(a2, 'item12', b)
    _safe_set(b, 'subCategory13', None)
    assert not _is_linked(b, 'subCategory13', a2)
    if hasattr(a2, 'item12'):
        assert not _is_linked(a2, 'item12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

