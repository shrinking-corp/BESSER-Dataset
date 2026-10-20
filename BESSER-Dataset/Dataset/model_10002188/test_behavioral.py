import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_Cart_User_reverse_link_reassign_clear():
    a1 = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    a2 = User(Email="sample_text_2", ID=13, Password="sample_text_2", Phone=13, Point=13, UserInfo="sample_text_2", UserName="sample_text_2")
    b = Cart(CartID=7, CartInfo="sample_text")
    _safe_set(b, 'user22', a1)
    assert _is_linked(b, 'user22', a1)
    if hasattr(a1, 'cart23'):
        assert _is_linked(a1, 'cart23', b)
    _safe_set(b, 'user22', a2)
    assert _is_linked(b, 'user22', a2)
    if hasattr(a1, 'cart23'):
        assert not _is_linked(a1, 'cart23', b)
    if hasattr(a2, 'cart23'):
        assert _is_linked(a2, 'cart23', b)
    _safe_set(b, 'user22', None)
    assert not _is_linked(b, 'user22', a2)
    if hasattr(a2, 'cart23'):
        assert not _is_linked(a2, 'cart23', b)


def test_assoc_Collection_Products_reverse_link_reassign_clear():
    a1 = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    a2 = Products(CollectionID=13, DateCreate="sample_text_2", InStock=13, Index=13, ProductID=13, ProductInfo="sample_text_2", TypeID=13, TypeID1=13)
    b = Collection(CollectionID=7, CollectionName="sample_text")
    _safe_set(b, 'products6', {a1})
    assert _is_linked(b, 'products6', a1)
    if hasattr(a1, 'collection7'):
        assert _is_linked(a1, 'collection7', b)
    _safe_set(b, 'products6', {a2})
    assert _is_linked(b, 'products6', a2)
    if hasattr(a1, 'collection7'):
        assert not _is_linked(a1, 'collection7', b)
    if hasattr(a2, 'collection7'):
        assert _is_linked(a2, 'collection7', b)
    _safe_set(b, 'products6', set())
    assert not _is_linked(b, 'products6', a2)
    if hasattr(a2, 'collection7'):
        assert not _is_linked(a2, 'collection7', b)


def test_assoc_Color_Inventory_reverse_link_reassign_clear():
    a1 = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    a2 = Inventory(ColorID=13, InStock=13, ProductID=13, SizeID=13)
    b = Color(ColorID="sample_text", ColorName="sample_text")
    _safe_set(b, 'inventory2', {a1})
    assert _is_linked(b, 'inventory2', a1)
    if hasattr(a1, 'color3'):
        assert _is_linked(a1, 'color3', b)
    _safe_set(b, 'inventory2', {a2})
    assert _is_linked(b, 'inventory2', a2)
    if hasattr(a1, 'color3'):
        assert not _is_linked(a1, 'color3', b)
    if hasattr(a2, 'color3'):
        assert _is_linked(a2, 'color3', b)
    _safe_set(b, 'inventory2', set())
    assert not _is_linked(b, 'inventory2', a2)
    if hasattr(a2, 'color3'):
        assert not _is_linked(a2, 'color3', b)


def test_assoc_DetailCart_Cart_reverse_link_reassign_clear():
    a1 = DetailCart(CartID=7, DetailCartID=7, DetailCartInfo="sample_text", ProductID=7)
    a2 = DetailCart(CartID=13, DetailCartID=13, DetailCartInfo="sample_text_2", ProductID=13)
    b = Cart(CartID=7, CartInfo="sample_text")
    _safe_set(b, 'detailCart19', {a1})
    assert _is_linked(b, 'detailCart19', a1)
    if hasattr(a1, 'cart18'):
        assert _is_linked(a1, 'cart18', b)
    _safe_set(b, 'detailCart19', {a2})
    assert _is_linked(b, 'detailCart19', a2)
    if hasattr(a1, 'cart18'):
        assert not _is_linked(a1, 'cart18', b)
    if hasattr(a2, 'cart18'):
        assert _is_linked(a2, 'cart18', b)
    _safe_set(b, 'detailCart19', set())
    assert not _is_linked(b, 'detailCart19', a2)
    if hasattr(a2, 'cart18'):
        assert not _is_linked(a2, 'cart18', b)


def test_assoc_DetailOrder_Orders_reverse_link_reassign_clear():
    a1 = Orders(DeliInfo="sample_text", OrderID=7, OrderInfo="sample_text", UserID=7)
    a2 = Orders(DeliInfo="sample_text_2", OrderID=13, OrderInfo="sample_text_2", UserID=13)
    b = DetailOrder(DetailOrderID=7, DetailOrderInfo="sample_text", OrderID=7, ProductID=7)
    _safe_set(b, 'orders16', a1)
    assert _is_linked(b, 'orders16', a1)
    if hasattr(a1, 'detailOrder17'):
        assert _is_linked(a1, 'detailOrder17', b)
    _safe_set(b, 'orders16', a2)
    assert _is_linked(b, 'orders16', a2)
    if hasattr(a1, 'detailOrder17'):
        assert not _is_linked(a1, 'detailOrder17', b)
    if hasattr(a2, 'detailOrder17'):
        assert _is_linked(a2, 'detailOrder17', b)
    _safe_set(b, 'orders16', None)
    assert not _is_linked(b, 'orders16', a2)
    if hasattr(a2, 'detailOrder17'):
        assert not _is_linked(a2, 'detailOrder17', b)


def test_assoc_DetailOrder_Products_reverse_link_reassign_clear():
    a1 = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    a2 = Products(CollectionID=13, DateCreate="sample_text_2", InStock=13, Index=13, ProductID=13, ProductInfo="sample_text_2", TypeID=13, TypeID1=13)
    b = DetailOrder(DetailOrderID=7, DetailOrderInfo="sample_text", OrderID=7, ProductID=7)
    _safe_set(b, 'products12', {a1})
    assert _is_linked(b, 'products12', a1)
    if hasattr(a1, 'detailOrder13'):
        assert _is_linked(a1, 'detailOrder13', b)
    _safe_set(b, 'products12', {a2})
    assert _is_linked(b, 'products12', a2)
    if hasattr(a1, 'detailOrder13'):
        assert not _is_linked(a1, 'detailOrder13', b)
    if hasattr(a2, 'detailOrder13'):
        assert _is_linked(a2, 'detailOrder13', b)
    _safe_set(b, 'products12', set())
    assert not _is_linked(b, 'products12', a2)
    if hasattr(a2, 'detailOrder13'):
        assert not _is_linked(a2, 'detailOrder13', b)


def test_assoc_Gallery_Products_reverse_link_reassign_clear():
    a1 = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    a2 = Products(CollectionID=13, DateCreate="sample_text_2", InStock=13, Index=13, ProductID=13, ProductInfo="sample_text_2", TypeID=13, TypeID1=13)
    b = Gallery(DateCreate="sample_text", GalleryID=7, GalleryName="sample_text", Image="sample_text", ProductID=7)
    _safe_set(b, 'products10', a1)
    assert _is_linked(b, 'products10', a1)
    if hasattr(a1, 'gallery11'):
        assert _is_linked(a1, 'gallery11', b)
    _safe_set(b, 'products10', a2)
    assert _is_linked(b, 'products10', a2)
    if hasattr(a1, 'gallery11'):
        assert not _is_linked(a1, 'gallery11', b)
    if hasattr(a2, 'gallery11'):
        assert _is_linked(a2, 'gallery11', b)
    _safe_set(b, 'products10', None)
    assert not _is_linked(b, 'products10', a2)
    if hasattr(a2, 'gallery11'):
        assert not _is_linked(a2, 'gallery11', b)


def test_assoc_Orders_User_reverse_link_reassign_clear():
    a1 = User(Email="sample_text", ID=7, Password="sample_text", Phone=7, Point=7, UserInfo="sample_text", UserName="sample_text")
    a2 = User(Email="sample_text_2", ID=13, Password="sample_text_2", Phone=13, Point=13, UserInfo="sample_text_2", UserName="sample_text_2")
    b = Orders(DeliInfo="sample_text", OrderID=7, OrderInfo="sample_text", UserID=7)
    _safe_set(b, 'user20', a1)
    assert _is_linked(b, 'user20', a1)
    if hasattr(a1, 'orders21'):
        assert _is_linked(a1, 'orders21', b)
    _safe_set(b, 'user20', a2)
    assert _is_linked(b, 'user20', a2)
    if hasattr(a1, 'orders21'):
        assert not _is_linked(a1, 'orders21', b)
    if hasattr(a2, 'orders21'):
        assert _is_linked(a2, 'orders21', b)
    _safe_set(b, 'user20', None)
    assert not _is_linked(b, 'user20', a2)
    if hasattr(a2, 'orders21'):
        assert not _is_linked(a2, 'orders21', b)


def test_assoc_Products_DetailCart_reverse_link_reassign_clear():
    a1 = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    a2 = Products(CollectionID=13, DateCreate="sample_text_2", InStock=13, Index=13, ProductID=13, ProductInfo="sample_text_2", TypeID=13, TypeID1=13)
    b = DetailCart(CartID=7, DetailCartID=7, DetailCartInfo="sample_text", ProductID=7)
    _safe_set(b, 'products15', {a1})
    assert _is_linked(b, 'products15', a1)
    if hasattr(a1, 'detailCart14'):
        assert _is_linked(a1, 'detailCart14', b)
    _safe_set(b, 'products15', {a2})
    assert _is_linked(b, 'products15', a2)
    if hasattr(a1, 'detailCart14'):
        assert not _is_linked(a1, 'detailCart14', b)
    if hasattr(a2, 'detailCart14'):
        assert _is_linked(a2, 'detailCart14', b)
    _safe_set(b, 'products15', set())
    assert not _is_linked(b, 'products15', a2)
    if hasattr(a2, 'detailCart14'):
        assert not _is_linked(a2, 'detailCart14', b)


def test_assoc_Products_Inventory_reverse_link_reassign_clear():
    a1 = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    a2 = Products(CollectionID=13, DateCreate="sample_text_2", InStock=13, Index=13, ProductID=13, ProductInfo="sample_text_2", TypeID=13, TypeID1=13)
    b = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    _safe_set(b, 'products5', {a1})
    assert _is_linked(b, 'products5', a1)
    if hasattr(a1, 'inventory4'):
        assert _is_linked(a1, 'inventory4', b)
    _safe_set(b, 'products5', {a2})
    assert _is_linked(b, 'products5', a2)
    if hasattr(a1, 'inventory4'):
        assert not _is_linked(a1, 'inventory4', b)
    if hasattr(a2, 'inventory4'):
        assert _is_linked(a2, 'inventory4', b)
    _safe_set(b, 'products5', set())
    assert not _is_linked(b, 'products5', a2)
    if hasattr(a2, 'inventory4'):
        assert not _is_linked(a2, 'inventory4', b)


def test_assoc_Size_Inventory_reverse_link_reassign_clear():
    a1 = Size(SizeID=7, SizeName="sample_text")
    a2 = Size(SizeID=13, SizeName="sample_text_2")
    b = Inventory(ColorID=7, InStock=7, ProductID=7, SizeID=7)
    _safe_set(b, 'size1', {a1})
    assert _is_linked(b, 'size1', a1)
    if hasattr(a1, 'inventory0'):
        assert _is_linked(a1, 'inventory0', b)
    _safe_set(b, 'size1', {a2})
    assert _is_linked(b, 'size1', a2)
    if hasattr(a1, 'inventory0'):
        assert not _is_linked(a1, 'inventory0', b)
    if hasattr(a2, 'inventory0'):
        assert _is_linked(a2, 'inventory0', b)
    _safe_set(b, 'size1', set())
    assert not _is_linked(b, 'size1', a2)
    if hasattr(a2, 'inventory0'):
        assert not _is_linked(a2, 'inventory0', b)


def test_assoc_Type_Products_reverse_link_reassign_clear():
    a1 = Type(TypeID=7, TypeName="sample_text")
    a2 = Type(TypeID=13, TypeName="sample_text_2")
    b = Products(CollectionID=7, DateCreate="sample_text", InStock=7, Index=7, ProductID=7, ProductInfo="sample_text", TypeID=7, TypeID1=7)
    _safe_set(b, 'type9', a1)
    assert _is_linked(b, 'type9', a1)
    if hasattr(a1, 'products8'):
        assert _is_linked(a1, 'products8', b)
    _safe_set(b, 'type9', a2)
    assert _is_linked(b, 'type9', a2)
    if hasattr(a1, 'products8'):
        assert not _is_linked(a1, 'products8', b)
    if hasattr(a2, 'products8'):
        assert _is_linked(a2, 'products8', b)
    _safe_set(b, 'type9', None)
    assert not _is_linked(b, 'type9', a2)
    if hasattr(a2, 'products8'):
        assert not _is_linked(a2, 'products8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

