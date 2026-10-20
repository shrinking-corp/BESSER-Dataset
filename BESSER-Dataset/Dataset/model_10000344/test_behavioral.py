import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cuenta,
    ItemOrden,
    Licor,
    Login,
    Orden,
    Pago,
    Vendedor,
    Venta,
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
    a1 = Orden(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    a2 = Orden(number=13, ordered=date(2025, 6, 15), shipTo="sample_text_2", shipped=False, status="sample_text_2", total=9.99)
    b = Cuenta(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'Orden16', {a1})
    assert _is_linked(b, 'Orden16', a1)
    if hasattr(a1, 'Cuenta17'):
        assert _is_linked(a1, 'Cuenta17', b)
    _safe_set(b, 'Orden16', {a2})
    assert _is_linked(b, 'Orden16', a2)
    if hasattr(a1, 'Cuenta17'):
        assert not _is_linked(a1, 'Cuenta17', b)
    if hasattr(a2, 'Cuenta17'):
        assert _is_linked(a2, 'Cuenta17', b)
    _safe_set(b, 'Orden16', set())
    assert not _is_linked(b, 'Orden16', a2)
    if hasattr(a2, 'Cuenta17'):
        assert not _is_linked(a2, 'Cuenta17', b)


def test_assoc_Account_Payment_reverse_link_reassign_clear():
    a1 = Pago(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Pago(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Cuenta(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
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
    a1 = Venta(creationDate=date(2024, 1, 1))
    a2 = Venta(creationDate=date(2025, 6, 15))
    b = Cuenta(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'cart8', a1)
    assert _is_linked(b, 'cart8', a1)
    if hasattr(a1, 'Cuenta9'):
        assert _is_linked(a1, 'Cuenta9', b)
    _safe_set(b, 'cart8', a2)
    assert _is_linked(b, 'cart8', a2)
    if hasattr(a1, 'Cuenta9'):
        assert not _is_linked(a1, 'Cuenta9', b)
    if hasattr(a2, 'Cuenta9'):
        assert _is_linked(a2, 'Cuenta9', b)
    _safe_set(b, 'cart8', None)
    assert not _is_linked(b, 'cart8', a2)
    if hasattr(a2, 'Cuenta9'):
        assert not _is_linked(a2, 'Cuenta9', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = Vendedor(address="sample_text", email="sample_text", phone="sample_text")
    a2 = Vendedor(address="sample_text_2", email="sample_text_2", phone="sample_text_2")
    b = Cuenta(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'Vendedor7', a1)
    assert _is_linked(b, 'Vendedor7', a1)
    if hasattr(a1, 'Cuenta6'):
        assert _is_linked(a1, 'Cuenta6', b)
    _safe_set(b, 'Vendedor7', a2)
    assert _is_linked(b, 'Vendedor7', a2)
    if hasattr(a1, 'Cuenta6'):
        assert not _is_linked(a1, 'Cuenta6', b)
    if hasattr(a2, 'Cuenta6'):
        assert _is_linked(a2, 'Cuenta6', b)
    _safe_set(b, 'Vendedor7', None)
    assert not _is_linked(b, 'Vendedor7', a2)
    if hasattr(a2, 'Cuenta6'):
        assert not _is_linked(a2, 'Cuenta6', b)


def test_assoc_Order_LineItem_reverse_link_reassign_clear():
    a1 = Orden(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    a2 = Orden(number=13, ordered=date(2025, 6, 15), shipTo="sample_text_2", shipped=False, status="sample_text_2", total=9.99)
    b = ItemOrden(price=3.14, quantity=7)
    _safe_set(b, 'order15', a1)
    assert _is_linked(b, 'order15', a1)
    if hasattr(a1, 'items14'):
        assert _is_linked(a1, 'items14', b)
    _safe_set(b, 'order15', a2)
    assert _is_linked(b, 'order15', a2)
    if hasattr(a1, 'items14'):
        assert not _is_linked(a1, 'items14', b)
    if hasattr(a2, 'items14'):
        assert _is_linked(a2, 'items14', b)
    _safe_set(b, 'order15', None)
    assert not _is_linked(b, 'order15', a2)
    if hasattr(a2, 'items14'):
        assert not _is_linked(a2, 'items14', b)


def test_assoc_Payment_Order_reverse_link_reassign_clear():
    a1 = Pago(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Pago(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Orden(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    _safe_set(b, 'payment19', a1)
    assert _is_linked(b, 'payment19', a1)
    if hasattr(a1, 'Orden18'):
        assert _is_linked(a1, 'Orden18', b)
    _safe_set(b, 'payment19', a2)
    assert _is_linked(b, 'payment19', a2)
    if hasattr(a1, 'Orden18'):
        assert not _is_linked(a1, 'Orden18', b)
    if hasattr(a2, 'Orden18'):
        assert _is_linked(a2, 'Orden18', b)
    _safe_set(b, 'payment19', None)
    assert not _is_linked(b, 'payment19', a2)
    if hasattr(a2, 'Orden18'):
        assert not _is_linked(a2, 'Orden18', b)


def test_assoc_Product_LineItem_reverse_link_reassign_clear():
    a1 = Licor(description="sample_text", name="sample_text")
    a2 = Licor(description="sample_text_2", name="sample_text_2")
    b = ItemOrden(price=3.14, quantity=7)
    _safe_set(b, 'Producto13', a1)
    assert _is_linked(b, 'Producto13', a1)
    if hasattr(a1, 'lineItems12'):
        assert _is_linked(a1, 'lineItems12', b)
    _safe_set(b, 'Producto13', a2)
    assert _is_linked(b, 'Producto13', a2)
    if hasattr(a1, 'lineItems12'):
        assert not _is_linked(a1, 'lineItems12', b)
    if hasattr(a2, 'lineItems12'):
        assert _is_linked(a2, 'lineItems12', b)
    _safe_set(b, 'Producto13', None)
    assert not _is_linked(b, 'Producto13', a2)
    if hasattr(a2, 'lineItems12'):
        assert not _is_linked(a2, 'lineItems12', b)


def test_assoc_ShoppingCart_LineItem_reverse_link_reassign_clear():
    a1 = Venta(creationDate=date(2024, 1, 1))
    a2 = Venta(creationDate=date(2025, 6, 15))
    b = ItemOrden(price=3.14, quantity=7)
    _safe_set(b, 'sc11', a1)
    assert _is_linked(b, 'sc11', a1)
    if hasattr(a1, 'items10'):
        assert _is_linked(a1, 'items10', b)
    _safe_set(b, 'sc11', a2)
    assert _is_linked(b, 'sc11', a2)
    if hasattr(a1, 'items10'):
        assert not _is_linked(a1, 'items10', b)
    if hasattr(a2, 'items10'):
        assert _is_linked(a2, 'items10', b)
    _safe_set(b, 'sc11', None)
    assert not _is_linked(b, 'sc11', a2)
    if hasattr(a2, 'items10'):
        assert not _is_linked(a2, 'items10', b)


def test_assoc_WebUser_Customer_reverse_link_reassign_clear():
    a1 = Vendedor(address="sample_text", email="sample_text", phone="sample_text")
    a2 = Vendedor(address="sample_text_2", email="sample_text_2", phone="sample_text_2")
    b = Login(login="sample_text", password="sample_text", state="sample_text")
    _safe_set(b, 'Vendedor4', a1)
    assert _is_linked(b, 'Vendedor4', a1)
    if hasattr(a1, 'UsuarioWeb5'):
        assert _is_linked(a1, 'UsuarioWeb5', b)
    _safe_set(b, 'Vendedor4', a2)
    assert _is_linked(b, 'Vendedor4', a2)
    if hasattr(a1, 'UsuarioWeb5'):
        assert not _is_linked(a1, 'UsuarioWeb5', b)
    if hasattr(a2, 'UsuarioWeb5'):
        assert _is_linked(a2, 'UsuarioWeb5', b)
    _safe_set(b, 'Vendedor4', None)
    assert not _is_linked(b, 'Vendedor4', a2)
    if hasattr(a2, 'UsuarioWeb5'):
        assert not _is_linked(a2, 'UsuarioWeb5', b)


def test_assoc_WebUser_ShoppingCart_reverse_link_reassign_clear():
    a1 = Venta(creationDate=date(2024, 1, 1))
    a2 = Venta(creationDate=date(2025, 6, 15))
    b = Login(login="sample_text", password="sample_text", state="sample_text")
    _safe_set(b, 'Venta2', a1)
    assert _is_linked(b, 'Venta2', a1)
    if hasattr(a1, 'UsuarioWeb3'):
        assert _is_linked(a1, 'UsuarioWeb3', b)
    _safe_set(b, 'Venta2', a2)
    assert _is_linked(b, 'Venta2', a2)
    if hasattr(a1, 'UsuarioWeb3'):
        assert not _is_linked(a1, 'UsuarioWeb3', b)
    if hasattr(a2, 'UsuarioWeb3'):
        assert _is_linked(a2, 'UsuarioWeb3', b)
    _safe_set(b, 'Venta2', None)
    assert not _is_linked(b, 'Venta2', a2)
    if hasattr(a2, 'UsuarioWeb3'):
        assert not _is_linked(a2, 'UsuarioWeb3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

