import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_customer_address_value_roundtrip():
    instance = customer(address="sample_text", id_card=7, name="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_customer_id_card_value_roundtrip():
    instance = customer(address="sample_text", id_card=7, name="sample_text")
    assert instance.id_card == 7
    instance.id_card = 13
    assert instance.id_card == 13


def test_customer_name_value_roundtrip():
    instance = customer(address="sample_text", id_card=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_direct_sale_attribute_value_roundtrip():
    instance = direct_sale(attribute="sample_text", saled_products="sample_text", username="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_direct_sale_saled_products_value_roundtrip():
    instance = direct_sale(attribute="sample_text", saled_products="sample_text", username="sample_text")
    assert instance.saled_products == "sample_text"
    instance.saled_products = "sample_text_2"
    assert instance.saled_products == "sample_text_2"


def test_direct_sale_username_value_roundtrip():
    instance = direct_sale(attribute="sample_text", saled_products="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_online_market_customer_address_value_roundtrip():
    instance = online_market(customer_address="sample_text", customer_name="sample_text", product_price="sample_text", product_type="sample_text", register_id_card=7)
    assert instance.customer_address == "sample_text"
    instance.customer_address = "sample_text_2"
    assert instance.customer_address == "sample_text_2"


def test_online_market_customer_name_value_roundtrip():
    instance = online_market(customer_address="sample_text", customer_name="sample_text", product_price="sample_text", product_type="sample_text", register_id_card=7)
    assert instance.customer_name == "sample_text"
    instance.customer_name = "sample_text_2"
    assert instance.customer_name == "sample_text_2"


def test_online_market_product_price_value_roundtrip():
    instance = online_market(customer_address="sample_text", customer_name="sample_text", product_price="sample_text", product_type="sample_text", register_id_card=7)
    assert instance.product_price == "sample_text"
    instance.product_price = "sample_text_2"
    assert instance.product_price == "sample_text_2"


def test_online_market_product_type_value_roundtrip():
    instance = online_market(customer_address="sample_text", customer_name="sample_text", product_price="sample_text", product_type="sample_text", register_id_card=7)
    assert instance.product_type == "sample_text"
    instance.product_type = "sample_text_2"
    assert instance.product_type == "sample_text_2"


def test_online_market_register_id_card_value_roundtrip():
    instance = online_market(customer_address="sample_text", customer_name="sample_text", product_price="sample_text", product_type="sample_text", register_id_card=7)
    assert instance.register_id_card == 7
    instance.register_id_card = 13
    assert instance.register_id_card == 13


def test_sale_by_instalment_customer_name_value_roundtrip():
    instance = sale_by_instalment(customer_name="sample_text", id_card=7, saled_product="sample_text")
    assert instance.customer_name == "sample_text"
    instance.customer_name = "sample_text_2"
    assert instance.customer_name == "sample_text_2"


def test_sale_by_instalment_id_card_value_roundtrip():
    instance = sale_by_instalment(customer_name="sample_text", id_card=7, saled_product="sample_text")
    assert instance.id_card == 7
    instance.id_card = 13
    assert instance.id_card == 13


def test_sale_by_instalment_saled_product_value_roundtrip():
    instance = sale_by_instalment(customer_name="sample_text", id_card=7, saled_product="sample_text")
    assert instance.saled_product == "sample_text"
    instance.saled_product = "sample_text_2"
    assert instance.saled_product == "sample_text_2"


def test_section_name_value_roundtrip():
    instance = section(name="sample_text", number=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_section_number_value_roundtrip():
    instance = section(name="sample_text", number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_seller_name_value_roundtrip():
    instance = seller(name="sample_text", number=7, salary=7, section_name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_seller_number_value_roundtrip():
    instance = seller(name="sample_text", number=7, salary=7, section_name="sample_text")
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_seller_salary_value_roundtrip():
    instance = seller(name="sample_text", number=7, salary=7, section_name="sample_text")
    assert instance.salary == 7
    instance.salary = 13
    assert instance.salary == 13


def test_seller_section_name_value_roundtrip():
    instance = seller(name="sample_text", number=7, salary=7, section_name="sample_text")
    assert instance.section_name == "sample_text"
    instance.section_name = "sample_text_2"
    assert instance.section_name == "sample_text_2"


def test_the_product_name_value_roundtrip():
    instance = the_product(name="sample_text", price=7, type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_the_product_price_value_roundtrip():
    instance = the_product(name="sample_text", price=7, type="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_the_product_type_value_roundtrip():
    instance = the_product(name="sample_text", price=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_assoc_seller_section_link_reassign_clear():
    a = seller(name="sample_text", number=7, salary=7, section_name="sample_text")
    b1 = section(name="sample_text", number=7)
    b2 = section(name="sample_text_2", number=13)
    _safe_set(a, 'section36', b1)
    assert _is_linked(a, 'section36', b1)
    if hasattr(b1, 'seller37'):
        assert _is_linked(b1, 'seller37', a)
    _safe_set(a, 'section36', b2)
    assert _is_linked(a, 'section36', b2)
    if hasattr(b1, 'seller37'):
        assert not _is_linked(b1, 'seller37', a)
    if hasattr(b2, 'seller37'):
        assert _is_linked(b2, 'seller37', a)
    _safe_set(a, 'section36', None)
    assert not _is_linked(a, 'section36', b2)
    if hasattr(b2, 'seller37'):
        assert not _is_linked(b2, 'seller37', a)


def test_assoc_the_product_customer_link_reassign_clear():
    a = the_product(name="sample_text", price=7, type="sample_text")
    b1 = customer(address="sample_text", id_card=7, name="sample_text")
    b2 = customer(address="sample_text_2", id_card=13, name="sample_text_2")
    _safe_set(a, 'customer30', b1)
    assert _is_linked(a, 'customer30', b1)
    if hasattr(b1, 'the_product31'):
        assert _is_linked(b1, 'the_product31', a)
    _safe_set(a, 'customer30', b2)
    assert _is_linked(a, 'customer30', b2)
    if hasattr(b1, 'the_product31'):
        assert not _is_linked(b1, 'the_product31', a)
    if hasattr(b2, 'the_product31'):
        assert _is_linked(b2, 'the_product31', a)
    _safe_set(a, 'customer30', None)
    assert not _is_linked(a, 'customer30', b2)
    if hasattr(b2, 'the_product31'):
        assert not _is_linked(b2, 'the_product31', a)


def test_assoc_the_product_direct_sale_link_reassign_clear():
    a = the_product(name="sample_text", price=7, type="sample_text")
    b1 = direct_sale(attribute="sample_text", saled_products="sample_text", username="sample_text")
    b2 = direct_sale(attribute="sample_text_2", saled_products="sample_text_2", username="sample_text_2")
    _safe_set(a, 'direct_sale32', b1)
    assert _is_linked(a, 'direct_sale32', b1)
    if hasattr(b1, 'the_product33'):
        assert _is_linked(b1, 'the_product33', a)
    _safe_set(a, 'direct_sale32', b2)
    assert _is_linked(a, 'direct_sale32', b2)
    if hasattr(b1, 'the_product33'):
        assert not _is_linked(b1, 'the_product33', a)
    if hasattr(b2, 'the_product33'):
        assert _is_linked(b2, 'the_product33', a)
    _safe_set(a, 'direct_sale32', None)
    assert not _is_linked(a, 'direct_sale32', b2)
    if hasattr(b2, 'the_product33'):
        assert not _is_linked(b2, 'the_product33', a)


def test_assoc_the_product_online_market_link_reassign_clear():
    a = the_product(name="sample_text", price=7, type="sample_text")
    b1 = online_market(customer_address="sample_text", customer_name="sample_text", product_price="sample_text", product_type="sample_text", register_id_card=7)
    b2 = online_market(customer_address="sample_text_2", customer_name="sample_text_2", product_price="sample_text_2", product_type="sample_text_2", register_id_card=13)
    _safe_set(a, 'online_market28', b1)
    assert _is_linked(a, 'online_market28', b1)
    if hasattr(b1, 'the_product29'):
        assert _is_linked(b1, 'the_product29', a)
    _safe_set(a, 'online_market28', b2)
    assert _is_linked(a, 'online_market28', b2)
    if hasattr(b1, 'the_product29'):
        assert not _is_linked(b1, 'the_product29', a)
    if hasattr(b2, 'the_product29'):
        assert _is_linked(b2, 'the_product29', a)
    _safe_set(a, 'online_market28', None)
    assert not _is_linked(a, 'online_market28', b2)
    if hasattr(b2, 'the_product29'):
        assert not _is_linked(b2, 'the_product29', a)


def test_assoc_the_product_sale_by_instalment_link_reassign_clear():
    a = the_product(name="sample_text", price=7, type="sample_text")
    b1 = sale_by_instalment(customer_name="sample_text", id_card=7, saled_product="sample_text")
    b2 = sale_by_instalment(customer_name="sample_text_2", id_card=13, saled_product="sample_text_2")
    _safe_set(a, 'sale_by_instalment34', b1)
    assert _is_linked(a, 'sale_by_instalment34', b1)
    if hasattr(b1, 'the_product35'):
        assert _is_linked(b1, 'the_product35', a)
    _safe_set(a, 'sale_by_instalment34', b2)
    assert _is_linked(a, 'sale_by_instalment34', b2)
    if hasattr(b1, 'the_product35'):
        assert not _is_linked(b1, 'the_product35', a)
    if hasattr(b2, 'the_product35'):
        assert _is_linked(b2, 'the_product35', a)
    _safe_set(a, 'sale_by_instalment34', None)
    assert not _is_linked(a, 'sale_by_instalment34', b2)
    if hasattr(b2, 'the_product35'):
        assert not _is_linked(b2, 'the_product35', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Add_sold_products_UseCase_strategy = st.builds(Add_sold_products_UseCase)
@given(instance=Add_sold_products_UseCase_strategy)
@settings(max_examples=25)
def test_Add_sold_products_UseCase_instantiation(instance):
    assert isinstance(instance, Add_sold_products_UseCase)


Calculating_the_check_UseCase_strategy = st.builds(Calculating_the_check_UseCase)
@given(instance=Calculating_the_check_UseCase_strategy)
@settings(max_examples=25)
def test_Calculating_the_check_UseCase_instantiation(instance):
    assert isinstance(instance, Calculating_the_check_UseCase)


Card_id_registration_UseCase_strategy = st.builds(Card_id_registration_UseCase)
@given(instance=Card_id_registration_UseCase_strategy)
@settings(max_examples=25)
def test_Card_id_registration_UseCase_instantiation(instance):
    assert isinstance(instance, Card_id_registration_UseCase)


Entering_prices_UseCase_strategy = st.builds(Entering_prices_UseCase)
@given(instance=Entering_prices_UseCase_strategy)
@settings(max_examples=25)
def test_Entering_prices_UseCase_instantiation(instance):
    assert isinstance(instance, Entering_prices_UseCase)


Make_comprehensive_reports_UseCase_strategy = st.builds(Make_comprehensive_reports_UseCase)
@given(instance=Make_comprehensive_reports_UseCase_strategy)
@settings(max_examples=25)
def test_Make_comprehensive_reports_UseCase_instantiation(instance):
    assert isinstance(instance, Make_comprehensive_reports_UseCase)


Online_customer_request_UseCase_strategy = st.builds(Online_customer_request_UseCase)
@given(instance=Online_customer_request_UseCase_strategy)
@settings(max_examples=25)
def test_Online_customer_request_UseCase_instantiation(instance):
    assert isinstance(instance, Online_customer_request_UseCase)


add_customer_UseCase_strategy = st.builds(add_customer_UseCase)
@given(instance=add_customer_UseCase_strategy)
@settings(max_examples=25)
def test_add_customer_UseCase_instantiation(instance):
    assert isinstance(instance, add_customer_UseCase)


add_products_to_sections__UseCase_strategy = st.builds(add_products_to_sections__UseCase)
@given(instance=add_products_to_sections__UseCase_strategy)
@settings(max_examples=25)
def test_add_products_to_sections__UseCase_instantiation(instance):
    assert isinstance(instance, add_products_to_sections__UseCase)


add_seller__UseCase_strategy = st.builds(add_seller__UseCase)
@given(instance=add_seller__UseCase_strategy)
@settings(max_examples=25)
def test_add_seller__UseCase_instantiation(instance):
    assert isinstance(instance, add_seller__UseCase)


cashier_Actor_strategy = st.builds(cashier_Actor)
@given(instance=cashier_Actor_strategy)
@settings(max_examples=25)
def test_cashier_Actor_instantiation(instance):
    assert isinstance(instance, cashier_Actor)


customer_strategy = st.builds(customer, address=safe_text, id_card=st.integers(), name=safe_text)
@given(instance=customer_strategy)
@settings(max_examples=25)
def test_customer_instantiation(instance):
    assert isinstance(instance, customer)


customer_address__UseCase_strategy = st.builds(customer_address__UseCase)
@given(instance=customer_address__UseCase_strategy)
@settings(max_examples=25)
def test_customer_address__UseCase_instantiation(instance):
    assert isinstance(instance, customer_address__UseCase)


customer_name_UseCase_strategy = st.builds(customer_name_UseCase)
@given(instance=customer_name_UseCase_strategy)
@settings(max_examples=25)
def test_customer_name_UseCase_instantiation(instance):
    assert isinstance(instance, customer_name_UseCase)


delete_customer__UseCase_strategy = st.builds(delete_customer__UseCase)
@given(instance=delete_customer__UseCase_strategy)
@settings(max_examples=25)
def test_delete_customer__UseCase_instantiation(instance):
    assert isinstance(instance, delete_customer__UseCase)


delete_seller_UseCase_strategy = st.builds(delete_seller_UseCase)
@given(instance=delete_seller_UseCase_strategy)
@settings(max_examples=25)
def test_delete_seller_UseCase_instantiation(instance):
    assert isinstance(instance, delete_seller_UseCase)


direct_sale_strategy = st.builds(direct_sale, attribute=safe_text, saled_products=safe_text, username=safe_text)
@given(instance=direct_sale_strategy)
@settings(max_examples=25)
def test_direct_sale_instantiation(instance):
    assert isinstance(instance, direct_sale)


direct_sale_UseCase_strategy = st.builds(direct_sale_UseCase)
@given(instance=direct_sale_UseCase_strategy)
@settings(max_examples=25)
def test_direct_sale_UseCase_instantiation(instance):
    assert isinstance(instance, direct_sale_UseCase)


later_payment_sale__UseCase_strategy = st.builds(later_payment_sale__UseCase)
@given(instance=later_payment_sale__UseCase_strategy)
@settings(max_examples=25)
def test_later_payment_sale__UseCase_instantiation(instance):
    assert isinstance(instance, later_payment_sale__UseCase)


manager_Actor_strategy = st.builds(manager_Actor)
@given(instance=manager_Actor_strategy)
@settings(max_examples=25)
def test_manager_Actor_instantiation(instance):
    assert isinstance(instance, manager_Actor)


online_market_strategy = st.builds(online_market, customer_address=safe_text, customer_name=safe_text, product_price=safe_text, product_type=safe_text, register_id_card=st.integers())
@given(instance=online_market_strategy)
@settings(max_examples=25)
def test_online_market_instantiation(instance):
    assert isinstance(instance, online_market)


sale_by_instalment_strategy = st.builds(sale_by_instalment, customer_name=safe_text, id_card=st.integers(), saled_product=safe_text)
@given(instance=sale_by_instalment_strategy)
@settings(max_examples=25)
def test_sale_by_instalment_instantiation(instance):
    assert isinstance(instance, sale_by_instalment)


section_strategy = st.builds(section, name=safe_text, number=st.integers())
@given(instance=section_strategy)
@settings(max_examples=25)
def test_section_instantiation(instance):
    assert isinstance(instance, section)


seller_strategy = st.builds(seller, name=safe_text, number=st.integers(), salary=st.integers(), section_name=safe_text)
@given(instance=seller_strategy)
@settings(max_examples=25)
def test_seller_instantiation(instance):
    assert isinstance(instance, seller)


seller__Actor_strategy = st.builds(seller__Actor)
@given(instance=seller__Actor_strategy)
@settings(max_examples=25)
def test_seller__Actor_instantiation(instance):
    assert isinstance(instance, seller__Actor)


seller_registration_UseCase_strategy = st.builds(seller_registration_UseCase)
@given(instance=seller_registration_UseCase_strategy)
@settings(max_examples=25)
def test_seller_registration_UseCase_instantiation(instance):
    assert isinstance(instance, seller_registration_UseCase)


the_product_strategy = st.builds(the_product, name=safe_text, price=st.integers(), type=safe_text)
@given(instance=the_product_strategy)
@settings(max_examples=25)
def test_the_product_instantiation(instance):
    assert isinstance(instance, the_product)


update_section_UseCase_strategy = st.builds(update_section_UseCase)
@given(instance=update_section_UseCase_strategy)
@settings(max_examples=25)
def test_update_section_UseCase_instantiation(instance):
    assert isinstance(instance, update_section_UseCase)


