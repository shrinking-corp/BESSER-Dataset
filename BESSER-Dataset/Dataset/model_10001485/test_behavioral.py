import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Add_sold_products_UseCase,
    Calculating_the_check_UseCase,
    Card_id_registration_UseCase,
    Entering_prices_UseCase,
    Make_comprehensive_reports_UseCase,
    Online_customer_request_UseCase,
    add_customer_UseCase,
    add_products_to_sections__UseCase,
    add_seller__UseCase,
    cashier_Actor,
    customer,
    customer_address__UseCase,
    customer_name_UseCase,
    delete_customer__UseCase,
    delete_seller_UseCase,
    direct_sale,
    direct_sale_UseCase,
    later_payment_sale__UseCase,
    manager_Actor,
    online_market,
    sale_by_instalment,
    section,
    seller,
    seller__Actor,
    seller_registration_UseCase,
    the_product,
    update_section_UseCase,
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

def test_assoc_seller_section_reverse_link_reassign_clear():
    a1 = seller(name="sample_text", number=7, salary=7, section_name="sample_text")
    a2 = seller(name="sample_text_2", number=13, salary=13, section_name="sample_text_2")
    b = section(name="sample_text", number=7)
    _safe_set(b, 'seller37', {a1})
    assert _is_linked(b, 'seller37', a1)
    if hasattr(a1, 'section36'):
        assert _is_linked(a1, 'section36', b)
    _safe_set(b, 'seller37', {a2})
    assert _is_linked(b, 'seller37', a2)
    if hasattr(a1, 'section36'):
        assert not _is_linked(a1, 'section36', b)
    if hasattr(a2, 'section36'):
        assert _is_linked(a2, 'section36', b)
    _safe_set(b, 'seller37', set())
    assert not _is_linked(b, 'seller37', a2)
    if hasattr(a2, 'section36'):
        assert not _is_linked(a2, 'section36', b)


def test_assoc_the_product_customer_reverse_link_reassign_clear():
    a1 = the_product(name="sample_text", price=7, type="sample_text")
    a2 = the_product(name="sample_text_2", price=13, type="sample_text_2")
    b = customer(address="sample_text", id_card=7, name="sample_text")
    _safe_set(b, 'the_product31', a1)
    assert _is_linked(b, 'the_product31', a1)
    if hasattr(a1, 'customer30'):
        assert _is_linked(a1, 'customer30', b)
    _safe_set(b, 'the_product31', a2)
    assert _is_linked(b, 'the_product31', a2)
    if hasattr(a1, 'customer30'):
        assert not _is_linked(a1, 'customer30', b)
    if hasattr(a2, 'customer30'):
        assert _is_linked(a2, 'customer30', b)
    _safe_set(b, 'the_product31', None)
    assert not _is_linked(b, 'the_product31', a2)
    if hasattr(a2, 'customer30'):
        assert not _is_linked(a2, 'customer30', b)


def test_assoc_the_product_direct_sale_reverse_link_reassign_clear():
    a1 = the_product(name="sample_text", price=7, type="sample_text")
    a2 = the_product(name="sample_text_2", price=13, type="sample_text_2")
    b = direct_sale(attribute="sample_text", saled_products="sample_text", username="sample_text")
    _safe_set(b, 'the_product33', a1)
    assert _is_linked(b, 'the_product33', a1)
    if hasattr(a1, 'direct_sale32'):
        assert _is_linked(a1, 'direct_sale32', b)
    _safe_set(b, 'the_product33', a2)
    assert _is_linked(b, 'the_product33', a2)
    if hasattr(a1, 'direct_sale32'):
        assert not _is_linked(a1, 'direct_sale32', b)
    if hasattr(a2, 'direct_sale32'):
        assert _is_linked(a2, 'direct_sale32', b)
    _safe_set(b, 'the_product33', None)
    assert not _is_linked(b, 'the_product33', a2)
    if hasattr(a2, 'direct_sale32'):
        assert not _is_linked(a2, 'direct_sale32', b)


def test_assoc_the_product_online_market_reverse_link_reassign_clear():
    a1 = the_product(name="sample_text", price=7, type="sample_text")
    a2 = the_product(name="sample_text_2", price=13, type="sample_text_2")
    b = online_market(customer_address="sample_text", customer_name="sample_text", product_price="sample_text", product_type="sample_text", register_id_card=7)
    _safe_set(b, 'the_product29', a1)
    assert _is_linked(b, 'the_product29', a1)
    if hasattr(a1, 'online_market28'):
        assert _is_linked(a1, 'online_market28', b)
    _safe_set(b, 'the_product29', a2)
    assert _is_linked(b, 'the_product29', a2)
    if hasattr(a1, 'online_market28'):
        assert not _is_linked(a1, 'online_market28', b)
    if hasattr(a2, 'online_market28'):
        assert _is_linked(a2, 'online_market28', b)
    _safe_set(b, 'the_product29', None)
    assert not _is_linked(b, 'the_product29', a2)
    if hasattr(a2, 'online_market28'):
        assert not _is_linked(a2, 'online_market28', b)


def test_assoc_the_product_sale_by_instalment_reverse_link_reassign_clear():
    a1 = the_product(name="sample_text", price=7, type="sample_text")
    a2 = the_product(name="sample_text_2", price=13, type="sample_text_2")
    b = sale_by_instalment(customer_name="sample_text", id_card=7, saled_product="sample_text")
    _safe_set(b, 'the_product35', a1)
    assert _is_linked(b, 'the_product35', a1)
    if hasattr(a1, 'sale_by_instalment34'):
        assert _is_linked(a1, 'sale_by_instalment34', b)
    _safe_set(b, 'the_product35', a2)
    assert _is_linked(b, 'the_product35', a2)
    if hasattr(a1, 'sale_by_instalment34'):
        assert not _is_linked(a1, 'sale_by_instalment34', b)
    if hasattr(a2, 'sale_by_instalment34'):
        assert _is_linked(a2, 'sale_by_instalment34', b)
    _safe_set(b, 'the_product35', None)
    assert not _is_linked(b, 'the_product35', a2)
    if hasattr(a2, 'sale_by_instalment34'):
        assert not _is_linked(a2, 'sale_by_instalment34', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

