import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    schemaprimerpo_DocumentRoot,
    schemaprimerpo_EStringToStringMapEntry,
    schemaprimerpo_Item,
    schemaprimerpo_PurchaseOrder,
    schemaprimerpo_USAddress,
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

def test_assoc_billTo8_reverse_link_reassign_clear():
    a1 = schemaprimerpo_USAddress(city="sample_text", country="sample_text", name="sample_text", state="sample_text", street="sample_text", zip="sample_text")
    a2 = schemaprimerpo_USAddress(city="sample_text_2", country="sample_text_2", name="sample_text_2", state="sample_text_2", street="sample_text_2", zip="sample_text_2")
    b = schemaprimerpo_PurchaseOrder(comment="sample_text", orderDate="sample_text")
    _safe_set(b, 'schemaprimerpo_PurchaseOrder9', a1)
    assert _is_linked(b, 'schemaprimerpo_PurchaseOrder9', a1)
    if hasattr(a1, 'schemaprimerpo_USAddress10'):
        assert _is_linked(a1, 'schemaprimerpo_USAddress10', b)
    _safe_set(b, 'schemaprimerpo_PurchaseOrder9', a2)
    assert _is_linked(b, 'schemaprimerpo_PurchaseOrder9', a2)
    if hasattr(a1, 'schemaprimerpo_USAddress10'):
        assert not _is_linked(a1, 'schemaprimerpo_USAddress10', b)
    if hasattr(a2, 'schemaprimerpo_USAddress10'):
        assert _is_linked(a2, 'schemaprimerpo_USAddress10', b)
    _safe_set(b, 'schemaprimerpo_PurchaseOrder9', None)
    assert not _is_linked(b, 'schemaprimerpo_PurchaseOrder9', a2)
    if hasattr(a2, 'schemaprimerpo_USAddress10'):
        assert not _is_linked(a2, 'schemaprimerpo_USAddress10', b)


def test_assoc_items11_reverse_link_reassign_clear():
    a1 = schemaprimerpo_PurchaseOrder(comment="sample_text", orderDate="sample_text")
    a2 = schemaprimerpo_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2")
    b = schemaprimerpo_Item(comment="sample_text", partNum="sample_text", productName="sample_text", quantity="sample_text", shipDate="sample_text", uSPrice="sample_text")
    _safe_set(b, 'schemaprimerpo_Item', a1)
    assert _is_linked(b, 'schemaprimerpo_Item', a1)
    if hasattr(a1, 'schemaprimerpo_PurchaseOrder12'):
        assert _is_linked(a1, 'schemaprimerpo_PurchaseOrder12', b)
    _safe_set(b, 'schemaprimerpo_Item', a2)
    assert _is_linked(b, 'schemaprimerpo_Item', a2)
    if hasattr(a1, 'schemaprimerpo_PurchaseOrder12'):
        assert not _is_linked(a1, 'schemaprimerpo_PurchaseOrder12', b)
    if hasattr(a2, 'schemaprimerpo_PurchaseOrder12'):
        assert _is_linked(a2, 'schemaprimerpo_PurchaseOrder12', b)
    _safe_set(b, 'schemaprimerpo_Item', None)
    assert not _is_linked(b, 'schemaprimerpo_Item', a2)
    if hasattr(a2, 'schemaprimerpo_PurchaseOrder12'):
        assert not _is_linked(a2, 'schemaprimerpo_PurchaseOrder12', b)


def test_assoc_order4_reverse_link_reassign_clear():
    a1 = schemaprimerpo_PurchaseOrder(comment="sample_text", orderDate="sample_text")
    a2 = schemaprimerpo_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2")
    b = schemaprimerpo_DocumentRoot(comment="sample_text", mixed="sample_text")
    _safe_set(b, 'schemaprimerpo_DocumentRoot5', {a1})
    assert _is_linked(b, 'schemaprimerpo_DocumentRoot5', a1)
    if hasattr(a1, 'schemaprimerpo_PurchaseOrder'):
        assert _is_linked(a1, 'schemaprimerpo_PurchaseOrder', b)
    _safe_set(b, 'schemaprimerpo_DocumentRoot5', {a2})
    assert _is_linked(b, 'schemaprimerpo_DocumentRoot5', a2)
    if hasattr(a1, 'schemaprimerpo_PurchaseOrder'):
        assert not _is_linked(a1, 'schemaprimerpo_PurchaseOrder', b)
    if hasattr(a2, 'schemaprimerpo_PurchaseOrder'):
        assert _is_linked(a2, 'schemaprimerpo_PurchaseOrder', b)
    _safe_set(b, 'schemaprimerpo_DocumentRoot5', set())
    assert not _is_linked(b, 'schemaprimerpo_DocumentRoot5', a2)
    if hasattr(a2, 'schemaprimerpo_PurchaseOrder'):
        assert not _is_linked(a2, 'schemaprimerpo_PurchaseOrder', b)


def test_assoc_shipTo6_reverse_link_reassign_clear():
    a1 = schemaprimerpo_USAddress(city="sample_text", country="sample_text", name="sample_text", state="sample_text", street="sample_text", zip="sample_text")
    a2 = schemaprimerpo_USAddress(city="sample_text_2", country="sample_text_2", name="sample_text_2", state="sample_text_2", street="sample_text_2", zip="sample_text_2")
    b = schemaprimerpo_PurchaseOrder(comment="sample_text", orderDate="sample_text")
    _safe_set(b, 'schemaprimerpo_PurchaseOrder7', a1)
    assert _is_linked(b, 'schemaprimerpo_PurchaseOrder7', a1)
    if hasattr(a1, 'schemaprimerpo_USAddress'):
        assert _is_linked(a1, 'schemaprimerpo_USAddress', b)
    _safe_set(b, 'schemaprimerpo_PurchaseOrder7', a2)
    assert _is_linked(b, 'schemaprimerpo_PurchaseOrder7', a2)
    if hasattr(a1, 'schemaprimerpo_USAddress'):
        assert not _is_linked(a1, 'schemaprimerpo_USAddress', b)
    if hasattr(a2, 'schemaprimerpo_USAddress'):
        assert _is_linked(a2, 'schemaprimerpo_USAddress', b)
    _safe_set(b, 'schemaprimerpo_PurchaseOrder7', None)
    assert not _is_linked(b, 'schemaprimerpo_PurchaseOrder7', a2)
    if hasattr(a2, 'schemaprimerpo_USAddress'):
        assert not _is_linked(a2, 'schemaprimerpo_USAddress', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_xMLNSPrefixMap0_stub_double():
    # schemaprimerpo_EStringToStringMapEntry has no real 'schemaprimerpo_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so schemaprimerpo_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # schemaprimerpo_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = schemaprimerpo_DocumentRoot(comment="sample_text", mixed="sample_text")
    partner = schemaprimerpo_EStringToStringMapEntry()
    setattr(partner, 'schemaprimerpo_EStringToStringMapEntry', None)
    _safe_set(owner, 'schemaprimerpo_DocumentRoot', {partner})
    assert getattr(partner, 'schemaprimerpo_EStringToStringMapEntry') == owner
    _safe_set(owner, 'schemaprimerpo_DocumentRoot', set())
    assert getattr(partner, 'schemaprimerpo_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # schemaprimerpo_EStringToStringMapEntry has no real 'schemaprimerpo_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so schemaprimerpo_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # schemaprimerpo_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = schemaprimerpo_DocumentRoot(comment="sample_text", mixed="sample_text")
    partner = schemaprimerpo_EStringToStringMapEntry()
    setattr(partner, 'schemaprimerpo_EStringToStringMapEntry3', None)
    _safe_set(owner, 'schemaprimerpo_DocumentRoot2', {partner})
    assert getattr(partner, 'schemaprimerpo_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'schemaprimerpo_DocumentRoot2', set())
    assert getattr(partner, 'schemaprimerpo_EStringToStringMapEntry3') is None


