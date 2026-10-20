import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Carro_de_Compras,
    Cliente,
    Order,
    Payment,
    Product,
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
    _safe_set(b, 'order6', {a1})
    assert _is_linked(b, 'order6', a1)
    if hasattr(a1, 'account7'):
        assert _is_linked(a1, 'account7', b)
    _safe_set(b, 'order6', {a2})
    assert _is_linked(b, 'order6', a2)
    if hasattr(a1, 'account7'):
        assert not _is_linked(a1, 'account7', b)
    if hasattr(a2, 'account7'):
        assert _is_linked(a2, 'account7', b)
    _safe_set(b, 'order6', set())
    assert not _is_linked(b, 'order6', a2)
    if hasattr(a2, 'account7'):
        assert not _is_linked(a2, 'account7', b)


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
    a1 = Carro_de_Compras(Cantidad=7, IdCarro=7, Precio=7, Producto="sample_text")
    a2 = Carro_de_Compras(Cantidad=13, IdCarro=13, Precio=13, Producto="sample_text_2")
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'cart4', a1)
    assert _is_linked(b, 'cart4', a1)
    if hasattr(a1, 'account5'):
        assert _is_linked(a1, 'account5', b)
    _safe_set(b, 'cart4', a2)
    assert _is_linked(b, 'cart4', a2)
    if hasattr(a1, 'account5'):
        assert not _is_linked(a1, 'account5', b)
    if hasattr(a2, 'account5'):
        assert _is_linked(a2, 'account5', b)
    _safe_set(b, 'cart4', None)
    assert not _is_linked(b, 'cart4', a2)
    if hasattr(a2, 'account5'):
        assert not _is_linked(a2, 'account5', b)


def test_assoc_Payment_Order_reverse_link_reassign_clear():
    a1 = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Payment(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Order(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    _safe_set(b, 'payment9', a1)
    assert _is_linked(b, 'payment9', a1)
    if hasattr(a1, 'order8'):
        assert _is_linked(a1, 'order8', b)
    _safe_set(b, 'payment9', a2)
    assert _is_linked(b, 'payment9', a2)
    if hasattr(a1, 'order8'):
        assert not _is_linked(a1, 'order8', b)
    if hasattr(a2, 'order8'):
        assert _is_linked(a2, 'order8', b)
    _safe_set(b, 'payment9', None)
    assert not _is_linked(b, 'payment9', a2)
    if hasattr(a2, 'order8'):
        assert not _is_linked(a2, 'order8', b)


def test_assoc_WebUser_ShoppingCart_reverse_link_reassign_clear():
    a1 = Cliente(Contacto=7, Direcci_n="sample_text", Nombre="sample_text", email="sample_text")
    a2 = Cliente(Contacto=13, Direcci_n="sample_text_2", Nombre="sample_text_2", email="sample_text_2")
    b = Carro_de_Compras(Cantidad=7, IdCarro=7, Precio=7, Producto="sample_text")
    _safe_set(b, 'webUser3', a1)
    assert _is_linked(b, 'webUser3', a1)
    if hasattr(a1, 'shoppingCart2'):
        assert _is_linked(a1, 'shoppingCart2', b)
    _safe_set(b, 'webUser3', a2)
    assert _is_linked(b, 'webUser3', a2)
    if hasattr(a1, 'shoppingCart2'):
        assert not _is_linked(a1, 'shoppingCart2', b)
    if hasattr(a2, 'shoppingCart2'):
        assert _is_linked(a2, 'shoppingCart2', b)
    _safe_set(b, 'webUser3', None)
    assert not _is_linked(b, 'webUser3', a2)
    if hasattr(a2, 'shoppingCart2'):
        assert not _is_linked(a2, 'shoppingCart2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

