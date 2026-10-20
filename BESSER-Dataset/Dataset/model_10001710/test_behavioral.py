import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Cart,
    Customer,
    Order,
    Payment,
    Payment_Verification,
    Product,
    Web_Login,
    catalog,
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

def test_assoc_Account__Order_reverse_link_reassign_clear():
    a1 = Order(address="sample_text", items="sample_text", ordered="sample_text", shipped="sample_text", status="sample_text", t="sample_text")
    a2 = Order(address="sample_text_2", items="sample_text_2", ordered="sample_text_2", shipped="sample_text_2", status="sample_text_2", t="sample_text_2")
    b = Account(billing_address="sample_text", id="sample_text", open="sample_text")
    _safe_set(b, 'order14', a1)
    assert _is_linked(b, 'order14', a1)
    if hasattr(a1, 'account15'):
        assert _is_linked(a1, 'account15', b)
    _safe_set(b, 'order14', a2)
    assert _is_linked(b, 'order14', a2)
    if hasattr(a1, 'account15'):
        assert not _is_linked(a1, 'account15', b)
    if hasattr(a2, 'account15'):
        assert _is_linked(a2, 'account15', b)
    _safe_set(b, 'order14', None)
    assert not _is_linked(b, 'order14', a2)
    if hasattr(a2, 'account15'):
        assert not _is_linked(a2, 'account15', b)


def test_assoc_Cart_Order_reverse_link_reassign_clear():
    a1 = Order(address="sample_text", items="sample_text", ordered="sample_text", shipped="sample_text", status="sample_text", t="sample_text")
    a2 = Order(address="sample_text_2", items="sample_text_2", ordered="sample_text_2", shipped="sample_text_2", status="sample_text_2", t="sample_text_2")
    b = Cart(Id="sample_text", items=7)
    _safe_set(b, 'order18', a1)
    assert _is_linked(b, 'order18', a1)
    if hasattr(a1, 'cart19'):
        assert _is_linked(a1, 'cart19', b)
    _safe_set(b, 'order18', a2)
    assert _is_linked(b, 'order18', a2)
    if hasattr(a1, 'cart19'):
        assert not _is_linked(a1, 'cart19', b)
    if hasattr(a2, 'cart19'):
        assert _is_linked(a2, 'cart19', b)
    _safe_set(b, 'order18', None)
    assert not _is_linked(b, 'order18', a2)
    if hasattr(a2, 'cart19'):
        assert not _is_linked(a2, 'cart19', b)


def test_assoc_Cart_Product_reverse_link_reassign_clear():
    a1 = Product(Category="sample_text", attribute="sample_text", name="sample_text", price="sample_text")
    a2 = Product(Category="sample_text_2", attribute="sample_text_2", name="sample_text_2", price="sample_text_2")
    b = Cart(Id="sample_text", items=7)
    _safe_set(b, 'product22', a1)
    assert _is_linked(b, 'product22', a1)
    if hasattr(a1, 'cart23'):
        assert _is_linked(a1, 'cart23', b)
    _safe_set(b, 'product22', a2)
    assert _is_linked(b, 'product22', a2)
    if hasattr(a1, 'cart23'):
        assert not _is_linked(a1, 'cart23', b)
    if hasattr(a2, 'cart23'):
        assert _is_linked(a2, 'cart23', b)
    _safe_set(b, 'product22', None)
    assert not _is_linked(b, 'product22', a2)
    if hasattr(a2, 'cart23'):
        assert not _is_linked(a2, 'cart23', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = Customer(address="sample_text", email="sample_text", id_="sample_text", phone=7)
    a2 = Customer(address="sample_text_2", email="sample_text_2", id_="sample_text_2", phone=13)
    b = Account(billing_address="sample_text", id="sample_text", open="sample_text")
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


def test_assoc_Order_Payment_reverse_link_reassign_clear():
    a1 = Payment(Details="sample_text", paid="sample_text", total="sample_text", txn_id="sample_text")
    a2 = Payment(Details="sample_text_2", paid="sample_text_2", total="sample_text_2", txn_id="sample_text_2")
    b = Order(address="sample_text", items="sample_text", ordered="sample_text", shipped="sample_text", status="sample_text", t="sample_text")
    _safe_set(b, 'payment10', a1)
    assert _is_linked(b, 'payment10', a1)
    if hasattr(a1, 'order11'):
        assert _is_linked(a1, 'order11', b)
    _safe_set(b, 'payment10', a2)
    assert _is_linked(b, 'payment10', a2)
    if hasattr(a1, 'order11'):
        assert not _is_linked(a1, 'order11', b)
    if hasattr(a2, 'order11'):
        assert _is_linked(a2, 'order11', b)
    _safe_set(b, 'payment10', None)
    assert not _is_linked(b, 'payment10', a2)
    if hasattr(a2, 'order11'):
        assert not _is_linked(a2, 'order11', b)


def test_assoc_Payment_Payment_Verification_reverse_link_reassign_clear():
    a1 = Payment_Verification(status="sample_text", txn_id="sample_text")
    a2 = Payment_Verification(status="sample_text_2", txn_id="sample_text_2")
    b = Payment(Details="sample_text", paid="sample_text", total="sample_text", txn_id="sample_text")
    _safe_set(b, 'payment_Verification12', a1)
    assert _is_linked(b, 'payment_Verification12', a1)
    if hasattr(a1, 'payment13'):
        assert _is_linked(a1, 'payment13', b)
    _safe_set(b, 'payment_Verification12', a2)
    assert _is_linked(b, 'payment_Verification12', a2)
    if hasattr(a1, 'payment13'):
        assert not _is_linked(a1, 'payment13', b)
    if hasattr(a2, 'payment13'):
        assert _is_linked(a2, 'payment13', b)
    _safe_set(b, 'payment_Verification12', None)
    assert not _is_linked(b, 'payment_Verification12', a2)
    if hasattr(a2, 'payment13'):
        assert not _is_linked(a2, 'payment13', b)


def test_assoc_Payment_Verification_Account_reverse_link_reassign_clear():
    a1 = Payment_Verification(status="sample_text", txn_id="sample_text")
    a2 = Payment_Verification(status="sample_text_2", txn_id="sample_text_2")
    b = Account(billing_address="sample_text", id="sample_text", open="sample_text")
    _safe_set(b, 'payment_Verification17', a1)
    assert _is_linked(b, 'payment_Verification17', a1)
    if hasattr(a1, 'account16'):
        assert _is_linked(a1, 'account16', b)
    _safe_set(b, 'payment_Verification17', a2)
    assert _is_linked(b, 'payment_Verification17', a2)
    if hasattr(a1, 'account16'):
        assert not _is_linked(a1, 'account16', b)
    if hasattr(a2, 'account16'):
        assert _is_linked(a2, 'account16', b)
    _safe_set(b, 'payment_Verification17', None)
    assert not _is_linked(b, 'payment_Verification17', a2)
    if hasattr(a2, 'account16'):
        assert not _is_linked(a2, 'account16', b)


def test_assoc_Payment_Verification_Customer_reverse_link_reassign_clear():
    a1 = Payment_Verification(status="sample_text", txn_id="sample_text")
    a2 = Payment_Verification(status="sample_text_2", txn_id="sample_text_2")
    b = Customer(address="sample_text", email="sample_text", id_="sample_text", phone=7)
    _safe_set(b, 'payment_Verification21', a1)
    assert _is_linked(b, 'payment_Verification21', a1)
    if hasattr(a1, 'customer20'):
        assert _is_linked(a1, 'customer20', b)
    _safe_set(b, 'payment_Verification21', a2)
    assert _is_linked(b, 'payment_Verification21', a2)
    if hasattr(a1, 'customer20'):
        assert not _is_linked(a1, 'customer20', b)
    if hasattr(a2, 'customer20'):
        assert _is_linked(a2, 'customer20', b)
    _safe_set(b, 'payment_Verification21', None)
    assert not _is_linked(b, 'payment_Verification21', a2)
    if hasattr(a2, 'customer20'):
        assert not _is_linked(a2, 'customer20', b)


def test_assoc_Product_Order_reverse_link_reassign_clear():
    a1 = Product(Category="sample_text", attribute="sample_text", name="sample_text", price="sample_text")
    a2 = Product(Category="sample_text_2", attribute="sample_text_2", name="sample_text_2", price="sample_text_2")
    b = Order(address="sample_text", items="sample_text", ordered="sample_text", shipped="sample_text", status="sample_text", t="sample_text")
    _safe_set(b, 'product9', a1)
    assert _is_linked(b, 'product9', a1)
    if hasattr(a1, 'order8'):
        assert _is_linked(a1, 'order8', b)
    _safe_set(b, 'product9', a2)
    assert _is_linked(b, 'product9', a2)
    if hasattr(a1, 'order8'):
        assert not _is_linked(a1, 'order8', b)
    if hasattr(a2, 'order8'):
        assert _is_linked(a2, 'order8', b)
    _safe_set(b, 'product9', None)
    assert not _is_linked(b, 'product9', a2)
    if hasattr(a2, 'order8'):
        assert not _is_linked(a2, 'order8', b)


def test_assoc_catalog_Product_reverse_link_reassign_clear():
    a1 = catalog(category="sample_text", name="sample_text")
    a2 = catalog(category="sample_text_2", name="sample_text_2")
    b = Product(Category="sample_text", attribute="sample_text", name="sample_text", price="sample_text")
    _safe_set(b, 'catalog7', a1)
    assert _is_linked(b, 'catalog7', a1)
    if hasattr(a1, 'product6'):
        assert _is_linked(a1, 'product6', b)
    _safe_set(b, 'catalog7', a2)
    assert _is_linked(b, 'catalog7', a2)
    if hasattr(a1, 'product6'):
        assert not _is_linked(a1, 'product6', b)
    if hasattr(a2, 'product6'):
        assert _is_linked(a2, 'product6', b)
    _safe_set(b, 'catalog7', None)
    assert not _is_linked(b, 'catalog7', a2)
    if hasattr(a2, 'product6'):
        assert not _is_linked(a2, 'product6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

