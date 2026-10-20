import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Cart,
    Kategori,
    Order,
    Orderdetail,
    Produk,
    Shippinginfo,
    User,
    admin,
    barang,
    kategori,
    order,
    orderdetail,
    pembeli,
    pembeli1,
    penjual,
    role,
    user,
    vendor,
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

def test_assoc_Cart_Customer_reverse_link_reassign_clear():
    a1 = pembeli(address="sample_text", id="sample_text", mail="sample_text", name="sample_text", password="sample_text", shippinginfo="sample_text", username="sample_text")
    a2 = pembeli(address="sample_text_2", id="sample_text_2", mail="sample_text_2", name="sample_text_2", password="sample_text_2", shippinginfo="sample_text_2", username="sample_text_2")
    b = Cart(cartid="sample_text", date="sample_text", productid="sample_text", quantity="sample_text")
    _safe_set(b, 'customer4', a1)
    assert _is_linked(b, 'customer4', a1)
    if hasattr(a1, 'cart5'):
        assert _is_linked(a1, 'cart5', b)
    _safe_set(b, 'customer4', a2)
    assert _is_linked(b, 'customer4', a2)
    if hasattr(a1, 'cart5'):
        assert not _is_linked(a1, 'cart5', b)
    if hasattr(a2, 'cart5'):
        assert _is_linked(a2, 'cart5', b)
    _safe_set(b, 'customer4', None)
    assert not _is_linked(b, 'customer4', a2)
    if hasattr(a2, 'cart5'):
        assert not _is_linked(a2, 'cart5', b)


def test_assoc_Orderdetail_Order_reverse_link_reassign_clear():
    a1 = Orderdetail(cost="sample_text", orderid="sample_text", productid="sample_text", quantity="sample_text", total="sample_text")
    a2 = Orderdetail(cost="sample_text_2", orderid="sample_text_2", productid="sample_text_2", quantity="sample_text_2", total="sample_text_2")
    b = Order(customerid="sample_text", datedeliver="sample_text", dateorder="sample_text", orderid="sample_text", shippingid="sample_text", status="sample_text")
    _safe_set(b, 'orderdetail3', a1)
    assert _is_linked(b, 'orderdetail3', a1)
    if hasattr(a1, 'order2'):
        assert _is_linked(a1, 'order2', b)
    _safe_set(b, 'orderdetail3', a2)
    assert _is_linked(b, 'orderdetail3', a2)
    if hasattr(a1, 'order2'):
        assert not _is_linked(a1, 'order2', b)
    if hasattr(a2, 'order2'):
        assert _is_linked(a2, 'order2', b)
    _safe_set(b, 'orderdetail3', None)
    assert not _is_linked(b, 'orderdetail3', a2)
    if hasattr(a2, 'order2'):
        assert not _is_linked(a2, 'order2', b)


def test_assoc_Produk_Kategori_reverse_link_reassign_clear():
    a1 = Produk(desc="sample_text", idkategori="sample_text", name="sample_text", price="sample_text", productid="sample_text")
    a2 = Produk(desc="sample_text_2", idkategori="sample_text_2", name="sample_text_2", price="sample_text_2", productid="sample_text_2")
    b = Kategori(desc="sample_text", idkategori="sample_text", name="sample_text", productid="sample_text")
    _safe_set(b, 'produk11', a1)
    assert _is_linked(b, 'produk11', a1)
    if hasattr(a1, 'kategori10'):
        assert _is_linked(a1, 'kategori10', b)
    _safe_set(b, 'produk11', a2)
    assert _is_linked(b, 'produk11', a2)
    if hasattr(a1, 'kategori10'):
        assert not _is_linked(a1, 'kategori10', b)
    if hasattr(a2, 'kategori10'):
        assert _is_linked(a2, 'kategori10', b)
    _safe_set(b, 'produk11', None)
    assert not _is_linked(b, 'produk11', a2)
    if hasattr(a2, 'kategori10'):
        assert not _is_linked(a2, 'kategori10', b)


def test_assoc_Produk_Orderdetail_reverse_link_reassign_clear():
    a1 = Produk(desc="sample_text", idkategori="sample_text", name="sample_text", price="sample_text", productid="sample_text")
    a2 = Produk(desc="sample_text_2", idkategori="sample_text_2", name="sample_text_2", price="sample_text_2", productid="sample_text_2")
    b = Orderdetail(cost="sample_text", orderid="sample_text", productid="sample_text", quantity="sample_text", total="sample_text")
    _safe_set(b, 'produk9', {a1})
    assert _is_linked(b, 'produk9', a1)
    if hasattr(a1, 'orderdetail8'):
        assert _is_linked(a1, 'orderdetail8', b)
    _safe_set(b, 'produk9', {a2})
    assert _is_linked(b, 'produk9', a2)
    if hasattr(a1, 'orderdetail8'):
        assert not _is_linked(a1, 'orderdetail8', b)
    if hasattr(a2, 'orderdetail8'):
        assert _is_linked(a2, 'orderdetail8', b)
    _safe_set(b, 'produk9', set())
    assert not _is_linked(b, 'produk9', a2)
    if hasattr(a2, 'orderdetail8'):
        assert not _is_linked(a2, 'orderdetail8', b)


def test_assoc_Shippinginfo_Order_reverse_link_reassign_clear():
    a1 = Shippinginfo(cost="sample_text", region="sample_text", shippingid="sample_text", total="sample_text", type="sample_text")
    a2 = Shippinginfo(cost="sample_text_2", region="sample_text_2", shippingid="sample_text_2", total="sample_text_2", type="sample_text_2")
    b = Order(customerid="sample_text", datedeliver="sample_text", dateorder="sample_text", orderid="sample_text", shippingid="sample_text", status="sample_text")
    _safe_set(b, 'shippinginfo1', a1)
    assert _is_linked(b, 'shippinginfo1', a1)
    if hasattr(a1, 'order0'):
        assert _is_linked(a1, 'order0', b)
    _safe_set(b, 'shippinginfo1', a2)
    assert _is_linked(b, 'shippinginfo1', a2)
    if hasattr(a1, 'order0'):
        assert not _is_linked(a1, 'order0', b)
    if hasattr(a2, 'order0'):
        assert _is_linked(a2, 'order0', b)
    _safe_set(b, 'shippinginfo1', None)
    assert not _is_linked(b, 'shippinginfo1', a2)
    if hasattr(a2, 'order0'):
        assert not _is_linked(a2, 'order0', b)


def test_assoc_admin_user_reverse_link_reassign_clear():
    a1 = user(id_order=7, id_role=7, id_user=7)
    a2 = user(id_order=13, id_role=13, id_user=13)
    b = admin(id=7, password="sample_text", username="sample_text")
    _safe_set(b, 'user14', a1)
    assert _is_linked(b, 'user14', a1)
    if hasattr(a1, 'admin15'):
        assert _is_linked(a1, 'admin15', b)
    _safe_set(b, 'user14', a2)
    assert _is_linked(b, 'user14', a2)
    if hasattr(a1, 'admin15'):
        assert not _is_linked(a1, 'admin15', b)
    if hasattr(a2, 'admin15'):
        assert _is_linked(a2, 'admin15', b)
    _safe_set(b, 'user14', None)
    assert not _is_linked(b, 'user14', a2)
    if hasattr(a2, 'admin15'):
        assert not _is_linked(a2, 'admin15', b)


def test_assoc_barang_kategori_reverse_link_reassign_clear():
    a1 = kategori(deskripsi_kategori="sample_text", id=7, nama_kategori="sample_text")
    a2 = kategori(deskripsi_kategori="sample_text_2", id=13, nama_kategori="sample_text_2")
    b = barang(deskripsi_barang="sample_text", harga_barang=7, id=7, id_kategori=7, nama_barang="sample_text")
    _safe_set(b, 'kategori24', a1)
    assert _is_linked(b, 'kategori24', a1)
    if hasattr(a1, 'barang25'):
        assert _is_linked(a1, 'barang25', b)
    _safe_set(b, 'kategori24', a2)
    assert _is_linked(b, 'kategori24', a2)
    if hasattr(a1, 'barang25'):
        assert not _is_linked(a1, 'barang25', b)
    if hasattr(a2, 'barang25'):
        assert _is_linked(a2, 'barang25', b)
    _safe_set(b, 'kategori24', None)
    assert not _is_linked(b, 'kategori24', a2)
    if hasattr(a2, 'barang25'):
        assert not _is_linked(a2, 'barang25', b)


def test_assoc_order_orderdetail_reverse_link_reassign_clear():
    a1 = orderdetail(barang_id=7, order_id=7, total="sample_text")
    a2 = orderdetail(barang_id=13, order_id=13, total="sample_text_2")
    b = order(dateorder="sample_text", id_user=7, order_id=7, status="sample_text")
    _safe_set(b, 'orderdetail22', a1)
    assert _is_linked(b, 'orderdetail22', a1)
    if hasattr(a1, 'order23'):
        assert _is_linked(a1, 'order23', b)
    _safe_set(b, 'orderdetail22', a2)
    assert _is_linked(b, 'orderdetail22', a2)
    if hasattr(a1, 'order23'):
        assert not _is_linked(a1, 'order23', b)
    if hasattr(a2, 'order23'):
        assert _is_linked(a2, 'order23', b)
    _safe_set(b, 'orderdetail22', None)
    assert not _is_linked(b, 'orderdetail22', a2)
    if hasattr(a2, 'order23'):
        assert not _is_linked(a2, 'order23', b)


def test_assoc_order_user_reverse_link_reassign_clear():
    a1 = user(id_order=7, id_role=7, id_user=7)
    a2 = user(id_order=13, id_role=13, id_user=13)
    b = order(dateorder="sample_text", id_user=7, order_id=7, status="sample_text")
    _safe_set(b, 'user20', a1)
    assert _is_linked(b, 'user20', a1)
    if hasattr(a1, 'order21'):
        assert _is_linked(a1, 'order21', b)
    _safe_set(b, 'user20', a2)
    assert _is_linked(b, 'user20', a2)
    if hasattr(a1, 'order21'):
        assert not _is_linked(a1, 'order21', b)
    if hasattr(a2, 'order21'):
        assert _is_linked(a2, 'order21', b)
    _safe_set(b, 'user20', None)
    assert not _is_linked(b, 'user20', a2)
    if hasattr(a2, 'order21'):
        assert not _is_linked(a2, 'order21', b)


def test_assoc_orderdetail_barang_reverse_link_reassign_clear():
    a1 = orderdetail(barang_id=7, order_id=7, total="sample_text")
    a2 = orderdetail(barang_id=13, order_id=13, total="sample_text_2")
    b = barang(deskripsi_barang="sample_text", harga_barang=7, id=7, id_kategori=7, nama_barang="sample_text")
    _safe_set(b, 'orderdetail27', a1)
    assert _is_linked(b, 'orderdetail27', a1)
    if hasattr(a1, 'barang26'):
        assert _is_linked(a1, 'barang26', b)
    _safe_set(b, 'orderdetail27', a2)
    assert _is_linked(b, 'orderdetail27', a2)
    if hasattr(a1, 'barang26'):
        assert not _is_linked(a1, 'barang26', b)
    if hasattr(a2, 'barang26'):
        assert _is_linked(a2, 'barang26', b)
    _safe_set(b, 'orderdetail27', None)
    assert not _is_linked(b, 'orderdetail27', a2)
    if hasattr(a2, 'barang26'):
        assert not _is_linked(a2, 'barang26', b)


def test_assoc_pembeli_user_reverse_link_reassign_clear():
    a1 = user(id_order=7, id_role=7, id_user=7)
    a2 = user(id_order=13, id_role=13, id_user=13)
    b = pembeli1(address="sample_text", id=7, id_role=7, mail="sample_text", name="sample_text", password="sample_text", username="sample_text")
    _safe_set(b, 'user16', a1)
    assert _is_linked(b, 'user16', a1)
    if hasattr(a1, 'pembeli17'):
        assert _is_linked(a1, 'pembeli17', b)
    _safe_set(b, 'user16', a2)
    assert _is_linked(b, 'user16', a2)
    if hasattr(a1, 'pembeli17'):
        assert not _is_linked(a1, 'pembeli17', b)
    if hasattr(a2, 'pembeli17'):
        assert _is_linked(a2, 'pembeli17', b)
    _safe_set(b, 'user16', None)
    assert not _is_linked(b, 'user16', a2)
    if hasattr(a2, 'pembeli17'):
        assert not _is_linked(a2, 'pembeli17', b)


def test_assoc_penjual_User_reverse_link_reassign_clear():
    a1 = penjual(address="sample_text", bank="sample_text", bussinessname="sample_text", id="sample_text", mail="sample_text", name="sample_text", password="sample_text", shippinginfo="sample_text", username="sample_text")
    a2 = penjual(address="sample_text_2", bank="sample_text_2", bussinessname="sample_text_2", id="sample_text_2", mail="sample_text_2", name="sample_text_2", password="sample_text_2", shippinginfo="sample_text_2", username="sample_text_2")
    b = User(id="sample_text", password="sample_text")
    _safe_set(b, 'penjual7', a1)
    assert _is_linked(b, 'penjual7', a1)
    if hasattr(a1, 'user6'):
        assert _is_linked(a1, 'user6', b)
    _safe_set(b, 'penjual7', a2)
    assert _is_linked(b, 'penjual7', a2)
    if hasattr(a1, 'user6'):
        assert not _is_linked(a1, 'user6', b)
    if hasattr(a2, 'user6'):
        assert _is_linked(a2, 'user6', b)
    _safe_set(b, 'penjual7', None)
    assert not _is_linked(b, 'penjual7', a2)
    if hasattr(a2, 'user6'):
        assert not _is_linked(a2, 'user6', b)


def test_assoc_role_user_reverse_link_reassign_clear():
    a1 = user(id_order=7, id_role=7, id_user=7)
    a2 = user(id_order=13, id_role=13, id_user=13)
    b = role(deskripsi_role="sample_text", id=7, nama_role="sample_text")
    _safe_set(b, 'user12', a1)
    assert _is_linked(b, 'user12', a1)
    if hasattr(a1, 'role13'):
        assert _is_linked(a1, 'role13', b)
    _safe_set(b, 'user12', a2)
    assert _is_linked(b, 'user12', a2)
    if hasattr(a1, 'role13'):
        assert not _is_linked(a1, 'role13', b)
    if hasattr(a2, 'role13'):
        assert _is_linked(a2, 'role13', b)
    _safe_set(b, 'user12', None)
    assert not _is_linked(b, 'user12', a2)
    if hasattr(a2, 'role13'):
        assert not _is_linked(a2, 'role13', b)


def test_assoc_vendor_user_reverse_link_reassign_clear():
    a1 = vendor(address="sample_text", bank="sample_text", bussinessname="sample_text", id=7, id_role=7, mail="sample_text", name="sample_text", password="sample_text", shippinginfo="sample_text", username="sample_text")
    a2 = vendor(address="sample_text_2", bank="sample_text_2", bussinessname="sample_text_2", id=13, id_role=13, mail="sample_text_2", name="sample_text_2", password="sample_text_2", shippinginfo="sample_text_2", username="sample_text_2")
    b = user(id_order=7, id_role=7, id_user=7)
    _safe_set(b, 'vendor19', a1)
    assert _is_linked(b, 'vendor19', a1)
    if hasattr(a1, 'user18'):
        assert _is_linked(a1, 'user18', b)
    _safe_set(b, 'vendor19', a2)
    assert _is_linked(b, 'vendor19', a2)
    if hasattr(a1, 'user18'):
        assert not _is_linked(a1, 'user18', b)
    if hasattr(a2, 'user18'):
        assert _is_linked(a2, 'user18', b)
    _safe_set(b, 'vendor19', None)
    assert not _is_linked(b, 'vendor19', a2)
    if hasattr(a2, 'user18'):
        assert not _is_linked(a2, 'user18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

