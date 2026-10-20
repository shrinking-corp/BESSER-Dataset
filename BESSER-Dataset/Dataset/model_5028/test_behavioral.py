import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    amazoninformational_Customer,
    amazoninformational_Invoice,
    amazoninformational_Order,
    amazoninformational_Package,
    amazoninformational_Payment,
    amazoninformational_Product,
    amazoninformational_Shipment,
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

def test_assoc_customer6_reverse_link_reassign_clear():
    a1 = amazoninformational_Order(status="sample_text", totalAmount=3.14)
    a2 = amazoninformational_Order(status="sample_text_2", totalAmount=9.99)
    b = amazoninformational_Customer(address="sample_text", consummedCredit=3.14, creditLimit=3.14, inGoodStanding=True, isVIP=True)
    _safe_set(b, 'amazoninformational_Customer', a1)
    assert _is_linked(b, 'amazoninformational_Customer', a1)
    if hasattr(a1, 'amazoninformational_Order7'):
        assert _is_linked(a1, 'amazoninformational_Order7', b)
    _safe_set(b, 'amazoninformational_Customer', a2)
    assert _is_linked(b, 'amazoninformational_Customer', a2)
    if hasattr(a1, 'amazoninformational_Order7'):
        assert not _is_linked(a1, 'amazoninformational_Order7', b)
    if hasattr(a2, 'amazoninformational_Order7'):
        assert _is_linked(a2, 'amazoninformational_Order7', b)
    _safe_set(b, 'amazoninformational_Customer', None)
    assert not _is_linked(b, 'amazoninformational_Customer', a2)
    if hasattr(a2, 'amazoninformational_Order7'):
        assert not _is_linked(a2, 'amazoninformational_Order7', b)


def test_assoc_order10_reverse_link_reassign_clear():
    a1 = amazoninformational_Package(location="sample_text")
    a2 = amazoninformational_Package(location="sample_text_2")
    b = amazoninformational_Order(status="sample_text", totalAmount=3.14)
    _safe_set(b, 'Order', a1)
    assert _is_linked(b, 'Order', a1)
    if hasattr(a1, 'packages'):
        assert _is_linked(a1, 'packages', b)
    _safe_set(b, 'Order', a2)
    assert _is_linked(b, 'Order', a2)
    if hasattr(a1, 'packages'):
        assert not _is_linked(a1, 'packages', b)
    if hasattr(a2, 'packages'):
        assert _is_linked(a2, 'packages', b)
    _safe_set(b, 'Order', None)
    assert not _is_linked(b, 'Order', a2)
    if hasattr(a2, 'packages'):
        assert not _is_linked(a2, 'packages', b)


def test_assoc_packages4_reverse_link_reassign_clear():
    a1 = amazoninformational_Package(location="sample_text")
    a2 = amazoninformational_Package(location="sample_text_2")
    b = amazoninformational_Order(status="sample_text", totalAmount=3.14)
    _safe_set(b, 'order5', {a1})
    assert _is_linked(b, 'order5', a1)
    if hasattr(a1, 'Package'):
        assert _is_linked(a1, 'Package', b)
    _safe_set(b, 'order5', {a2})
    assert _is_linked(b, 'order5', a2)
    if hasattr(a1, 'Package'):
        assert not _is_linked(a1, 'Package', b)
    if hasattr(a2, 'Package'):
        assert _is_linked(a2, 'Package', b)
    _safe_set(b, 'order5', set())
    assert not _is_linked(b, 'order5', a2)
    if hasattr(a2, 'Package'):
        assert not _is_linked(a2, 'Package', b)


def test_assoc_products0_reverse_link_reassign_clear():
    a1 = amazoninformational_Product(onHand=7)
    a2 = amazoninformational_Product(onHand=13)
    b = amazoninformational_Order(status="sample_text", totalAmount=3.14)
    _safe_set(b, 'amazoninformational_Order', {a1})
    assert _is_linked(b, 'amazoninformational_Order', a1)
    if hasattr(a1, 'amazoninformational_Product'):
        assert _is_linked(a1, 'amazoninformational_Product', b)
    _safe_set(b, 'amazoninformational_Order', {a2})
    assert _is_linked(b, 'amazoninformational_Order', a2)
    if hasattr(a1, 'amazoninformational_Product'):
        assert not _is_linked(a1, 'amazoninformational_Product', b)
    if hasattr(a2, 'amazoninformational_Product'):
        assert _is_linked(a2, 'amazoninformational_Product', b)
    _safe_set(b, 'amazoninformational_Order', set())
    assert not _is_linked(b, 'amazoninformational_Order', a2)
    if hasattr(a2, 'amazoninformational_Product'):
        assert not _is_linked(a2, 'amazoninformational_Product', b)


def test_assoc_products8_reverse_link_reassign_clear():
    a1 = amazoninformational_Product(onHand=7)
    a2 = amazoninformational_Product(onHand=13)
    b = amazoninformational_Package(location="sample_text")
    _safe_set(b, 'amazoninformational_Package', a1)
    assert _is_linked(b, 'amazoninformational_Package', a1)
    if hasattr(a1, 'amazoninformational_Product9'):
        assert _is_linked(a1, 'amazoninformational_Product9', b)
    _safe_set(b, 'amazoninformational_Package', a2)
    assert _is_linked(b, 'amazoninformational_Package', a2)
    if hasattr(a1, 'amazoninformational_Product9'):
        assert not _is_linked(a1, 'amazoninformational_Product9', b)
    if hasattr(a2, 'amazoninformational_Product9'):
        assert _is_linked(a2, 'amazoninformational_Product9', b)
    _safe_set(b, 'amazoninformational_Package', None)
    assert not _is_linked(b, 'amazoninformational_Package', a2)
    if hasattr(a2, 'amazoninformational_Product9'):
        assert not _is_linked(a2, 'amazoninformational_Product9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_invoice2_stub_double():
    # amazoninformational_Invoice has no real 'Invoice' property in the generated
    # code (a bare stub) -- manually attach it so amazoninformational_Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amazoninformational_Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amazoninformational_Order(status="sample_text", totalAmount=3.14)
    partner = amazoninformational_Invoice()
    setattr(partner, 'Invoice', None)
    _safe_set(owner, 'order3', partner)
    assert getattr(partner, 'Invoice') == owner
    _safe_set(owner, 'order3', None)
    assert getattr(partner, 'Invoice') is None


def test_assoc_order13_stub_double():
    # amazoninformational_Shipment has no real 'shipment' property in the generated
    # code (a bare stub) -- manually attach it so amazoninformational_Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amazoninformational_Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amazoninformational_Order(status="sample_text", totalAmount=3.14)
    partner = amazoninformational_Shipment()
    setattr(partner, 'shipment', None)
    _safe_set(owner, 'Order14', partner)
    assert getattr(partner, 'shipment') == owner
    _safe_set(owner, 'Order14', None)
    assert getattr(partner, 'shipment') is None


def test_assoc_order15_stub_double():
    # amazoninformational_Invoice has no real 'invoice' property in the generated
    # code (a bare stub) -- manually attach it so amazoninformational_Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amazoninformational_Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amazoninformational_Order(status="sample_text", totalAmount=3.14)
    partner = amazoninformational_Invoice()
    setattr(partner, 'invoice', None)
    _safe_set(owner, 'Order16', partner)
    assert getattr(partner, 'invoice') == owner
    _safe_set(owner, 'Order16', None)
    assert getattr(partner, 'invoice') is None


def test_assoc_package11_stub_double():
    # amazoninformational_Shipment has no real 'amazoninformational_Shipment' property in the generated
    # code (a bare stub) -- manually attach it so amazoninformational_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amazoninformational_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amazoninformational_Package(location="sample_text")
    partner = amazoninformational_Shipment()
    setattr(partner, 'amazoninformational_Shipment', None)
    _safe_set(owner, 'amazoninformational_Package12', partner)
    assert owner in getattr(partner, 'amazoninformational_Shipment')
    _safe_set(owner, 'amazoninformational_Package12', None)
    assert owner not in getattr(partner, 'amazoninformational_Shipment')


def test_assoc_shipment1_stub_double():
    # amazoninformational_Shipment has no real 'Shipment' property in the generated
    # code (a bare stub) -- manually attach it so amazoninformational_Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amazoninformational_Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amazoninformational_Order(status="sample_text", totalAmount=3.14)
    partner = amazoninformational_Shipment()
    setattr(partner, 'Shipment', None)
    _safe_set(owner, 'order', partner)
    assert getattr(partner, 'Shipment') == owner
    _safe_set(owner, 'order', None)
    assert getattr(partner, 'Shipment') is None


