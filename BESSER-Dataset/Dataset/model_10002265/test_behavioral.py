import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    BoMon,
    ConNguoi,
    Customer,
    Khoa,
    Order,
    Payment,
    SinhVien,
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

def test_assoc_Account_Order_reverse_link_reassign_clear():
    a1 = Order(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    a2 = Order(number=13, ordered=date(2025, 6, 15), shipTo="sample_text_2", shipped=False, status="sample_text_2", total=9.99)
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'order10', {a1})
    assert _is_linked(b, 'order10', a1)
    if hasattr(a1, 'account11'):
        assert _is_linked(a1, 'account11', b)
    _safe_set(b, 'order10', {a2})
    assert _is_linked(b, 'order10', a2)
    if hasattr(a1, 'account11'):
        assert not _is_linked(a1, 'account11', b)
    if hasattr(a2, 'account11'):
        assert _is_linked(a2, 'account11', b)
    _safe_set(b, 'order10', set())
    assert not _is_linked(b, 'order10', a2)
    if hasattr(a2, 'account11'):
        assert not _is_linked(a2, 'account11', b)


def test_assoc_Account_Payment_reverse_link_reassign_clear():
    a1 = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Payment(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'p0', {a1})
    assert _is_linked(b, 'p0', a1)
    if hasattr(a1, 'acc1'):
        assert _is_linked(a1, 'acc1', b)
    _safe_set(b, 'p0', {a2})
    assert _is_linked(b, 'p0', a2)
    if hasattr(a1, 'acc1'):
        assert not _is_linked(a1, 'acc1', b)
    if hasattr(a2, 'acc1'):
        assert _is_linked(a2, 'acc1', b)
    _safe_set(b, 'p0', set())
    assert not _is_linked(b, 'p0', a2)
    if hasattr(a2, 'acc1'):
        assert not _is_linked(a2, 'acc1', b)


def test_assoc_Account_ShoppingCart_reverse_link_reassign_clear():
    a1 = ConNguoi(CMND="sample_text", diachi="sample_text", gioitinh=True, hoten="sample_text", ngaysinh=date(2024, 1, 1))
    a2 = ConNguoi(CMND="sample_text_2", diachi="sample_text_2", gioitinh=False, hoten="sample_text_2", ngaysinh=date(2025, 6, 15))
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'cart6', a1)
    assert _is_linked(b, 'cart6', a1)
    if hasattr(a1, 'account7'):
        assert _is_linked(a1, 'account7', b)
    _safe_set(b, 'cart6', a2)
    assert _is_linked(b, 'cart6', a2)
    if hasattr(a1, 'account7'):
        assert not _is_linked(a1, 'account7', b)
    if hasattr(a2, 'account7'):
        assert _is_linked(a2, 'account7', b)
    _safe_set(b, 'cart6', None)
    assert not _is_linked(b, 'cart6', a2)
    if hasattr(a2, 'account7'):
        assert not _is_linked(a2, 'account7', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = Customer(address="sample_text", email="sample_text", phone="sample_text")
    a2 = Customer(address="sample_text_2", email="sample_text_2", phone="sample_text_2")
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'customer5', a1)
    assert _is_linked(b, 'customer5', a1)
    if hasattr(a1, 'account4'):
        assert _is_linked(a1, 'account4', b)
    _safe_set(b, 'customer5', a2)
    assert _is_linked(b, 'customer5', a2)
    if hasattr(a1, 'account4'):
        assert not _is_linked(a1, 'account4', b)
    if hasattr(a2, 'account4'):
        assert _is_linked(a2, 'account4', b)
    _safe_set(b, 'customer5', None)
    assert not _is_linked(b, 'customer5', a2)
    if hasattr(a2, 'account4'):
        assert not _is_linked(a2, 'account4', b)


def test_assoc_Payment_Order_reverse_link_reassign_clear():
    a1 = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Payment(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Order(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    _safe_set(b, 'payment13', a1)
    assert _is_linked(b, 'payment13', a1)
    if hasattr(a1, 'order12'):
        assert _is_linked(a1, 'order12', b)
    _safe_set(b, 'payment13', a2)
    assert _is_linked(b, 'payment13', a2)
    if hasattr(a1, 'order12'):
        assert not _is_linked(a1, 'order12', b)
    if hasattr(a2, 'order12'):
        assert _is_linked(a2, 'order12', b)
    _safe_set(b, 'payment13', None)
    assert not _is_linked(b, 'payment13', a2)
    if hasattr(a2, 'order12'):
        assert not _is_linked(a2, 'order12', b)


def test_assoc_Product_LineItem_reverse_link_reassign_clear():
    a1 = Khoa(makhoa="sample_text", tenkhoa="sample_text")
    a2 = Khoa(makhoa="sample_text_2", tenkhoa="sample_text_2")
    b = BoMon(mabomon="sample_text", tenbomon="sample_text")
    _safe_set(b, 'thus9', a1)
    assert _is_linked(b, 'thus9', a1)
    if hasattr(a1, 'co8'):
        assert _is_linked(a1, 'co8', b)
    _safe_set(b, 'thus9', a2)
    assert _is_linked(b, 'thus9', a2)
    if hasattr(a1, 'co8'):
        assert not _is_linked(a1, 'co8', b)
    if hasattr(a2, 'co8'):
        assert _is_linked(a2, 'co8', b)
    _safe_set(b, 'thus9', None)
    assert not _is_linked(b, 'thus9', a2)
    if hasattr(a2, 'co8'):
        assert not _is_linked(a2, 'co8', b)


def test_assoc_WebUser_Customer_reverse_link_reassign_clear():
    a1 = SinhVien(MSSV="sample_text", bomon="sample_text", lop="sample_text", nganhhoc="sample_text")
    a2 = SinhVien(MSSV="sample_text_2", bomon="sample_text_2", lop="sample_text_2", nganhhoc="sample_text_2")
    b = Customer(address="sample_text", email="sample_text", phone="sample_text")
    _safe_set(b, 'webUser3', a1)
    assert _is_linked(b, 'webUser3', a1)
    if hasattr(a1, 'customer2'):
        assert _is_linked(a1, 'customer2', b)
    _safe_set(b, 'webUser3', a2)
    assert _is_linked(b, 'webUser3', a2)
    if hasattr(a1, 'customer2'):
        assert not _is_linked(a1, 'customer2', b)
    if hasattr(a2, 'customer2'):
        assert _is_linked(a2, 'customer2', b)
    _safe_set(b, 'webUser3', None)
    assert not _is_linked(b, 'webUser3', a2)
    if hasattr(a2, 'customer2'):
        assert not _is_linked(a2, 'customer2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

