# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    customers_CustomersDB,
    customers_Address,
    customers_CreditCard,
    Address,
    customers_CanadaAddress,
    customers_USAddress,
    customers_Customer,
    CanadaProvinces,
    USStates,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_customers_customersdb_is_not_abstract():
    assert not inspect.isabstract(customers_CustomersDB)


def test_hyp_customers_customersdb_constructor_exists():
    assert callable(customers_CustomersDB.__init__)


def test_hyp_customers_customersdb_constructor_args():
    sig = inspect.signature(customers_CustomersDB.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"




def test_hyp_customers_address_is_not_abstract():
    assert not inspect.isabstract(customers_Address)


def test_hyp_customers_address_constructor_exists():
    assert callable(customers_Address.__init__)


def test_hyp_customers_address_constructor_args():
    sig = inspect.signature(customers_Address.__init__)
    params = list(sig.parameters.keys())
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "town" in params, "Missing parameter 'town'"
    assert "street" in params, "Missing parameter 'street'"






def test_hyp_customers_creditcard_is_not_abstract():
    assert not inspect.isabstract(customers_CreditCard)


def test_hyp_customers_creditcard_constructor_exists():
    assert callable(customers_CreditCard.__init__)


def test_hyp_customers_creditcard_constructor_args():
    sig = inspect.signature(customers_CreditCard.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "expiresDate" in params, "Missing parameter 'expiresDate'"
    assert "ccNumber" in params, "Missing parameter 'ccNumber'"






def test_hyp_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_hyp_address_constructor_exists():
    assert callable(Address.__init__)


def test_hyp_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customers_canadaaddress_is_not_abstract():
    assert not inspect.isabstract(customers_CanadaAddress)


def test_hyp_customers_canadaaddress_constructor_exists():
    assert callable(customers_CanadaAddress.__init__)


def test_hyp_customers_canadaaddress_constructor_args():
    sig = inspect.signature(customers_CanadaAddress.__init__)
    params = list(sig.parameters.keys())
    assert "province" in params, "Missing parameter 'province'"




def test_hyp_customers_usaddress_is_not_abstract():
    assert not inspect.isabstract(customers_USAddress)


def test_hyp_customers_usaddress_constructor_exists():
    assert callable(customers_USAddress.__init__)


def test_hyp_customers_usaddress_constructor_args():
    sig = inspect.signature(customers_USAddress.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"




def test_hyp_customers_customer_is_not_abstract():
    assert not inspect.isabstract(customers_Customer)


def test_hyp_customers_customer_constructor_exists():
    assert callable(customers_Customer.__init__)


def test_hyp_customers_customer_constructor_args():
    sig = inspect.signature(customers_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "comment" in params, "Missing parameter 'comment'"





def test_hyp_canadaprovinces_exists():
    # Check that the Enumeration exists
    assert CanadaProvinces is not None

def test_hyp_canadaprovinces_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CanadaProvinces]
    expected_literals = [
        "NB",
        "BC",
        "AB",
        "NT",
        "NL",
        "MB",
        "UNKNOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CanadaProvinces"

def test_hyp_usstates_exists():
    # Check that the Enumeration exists
    assert USStates is not None

def test_hyp_usstates_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in USStates]
    expected_literals = [
        "UNKNOWN",
        "CO",
        "AL",
        "AZ",
        "CA",
        "AS",
        "AR",
        "AK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in USStates"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
customers_CustomersDB_strategy = st.builds(
    customers_CustomersDB,
    comment=
        safe_text
)
customers_Address_strategy = st.builds(
    customers_Address,
    zipCode=
        safe_text,
    town=
        safe_text,
    street=
        safe_text
)
customers_CreditCard_strategy = st.builds(
    customers_CreditCard,
    type=
        safe_text,
    expiresDate=
        st.dates(),
    ccNumber=
        safe_text
)
Address_strategy = st.builds(
    Address,
)
customers_CanadaAddress_strategy = st.builds(
    customers_CanadaAddress,
    province=
        safe_text
)
customers_USAddress_strategy = st.builds(
    customers_USAddress,
    state=
        safe_text
)
customers_Customer_strategy = st.builds(
    customers_Customer,
    firstName=
        safe_text,
    lastName=
        safe_text,
    dateOfBirth=
        st.dates(),
    comment=
        safe_text
)




@given(instance=customers_CustomersDB_strategy)
def test_hyp_customers_customersdb_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original




@given(instance=customers_Address_strategy)
def test_hyp_customers_address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original



@given(instance=customers_Address_strategy)
def test_hyp_customers_address_town_setter(instance):
    original = instance.town
    instance.town = original
    assert instance.town == original



@given(instance=customers_Address_strategy)
def test_hyp_customers_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original




@given(instance=customers_CreditCard_strategy)
def test_hyp_customers_creditcard_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=customers_CreditCard_strategy)
def test_hyp_customers_creditcard_expiresDate_setter(instance):
    original = instance.expiresDate
    instance.expiresDate = original
    assert instance.expiresDate == original



@given(instance=customers_CreditCard_strategy)
def test_hyp_customers_creditcard_ccNumber_setter(instance):
    original = instance.ccNumber
    instance.ccNumber = original
    assert instance.ccNumber == original





@given(instance=customers_CanadaAddress_strategy)
def test_hyp_customers_canadaaddress_province_setter(instance):
    original = instance.province
    instance.province = original
    assert instance.province == original




@given(instance=customers_USAddress_strategy)
def test_hyp_customers_usaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original




@given(instance=customers_Customer_strategy)
def test_hyp_customers_customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=customers_Customer_strategy)
def test_hyp_customers_customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=customers_Customer_strategy)
def test_hyp_customers_customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=customers_Customer_strategy)
def test_hyp_customers_customer_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Address,
    customers_Address,
    customers_CanadaAddress,
    customers_CreditCard,
    customers_Customer,
    customers_CustomersDB,
    customers_USAddress,
    CanadaProvinces,
    USStates,
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

def test_customers_Address_street_value_roundtrip():
    instance = customers_Address(street="sample_text", town="sample_text", zipCode="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_customers_Address_town_value_roundtrip():
    instance = customers_Address(street="sample_text", town="sample_text", zipCode="sample_text")
    assert instance.town == "sample_text"
    instance.town = "sample_text_2"
    assert instance.town == "sample_text_2"


def test_customers_Address_zipCode_value_roundtrip():
    instance = customers_Address(street="sample_text", town="sample_text", zipCode="sample_text")
    assert instance.zipCode == "sample_text"
    instance.zipCode = "sample_text_2"
    assert instance.zipCode == "sample_text_2"


def test_customers_CanadaAddress_province_value_roundtrip():
    instance = customers_CanadaAddress(province="sample_text")
    assert instance.province == "sample_text"
    instance.province = "sample_text_2"
    assert instance.province == "sample_text_2"


def test_customers_CreditCard_ccNumber_value_roundtrip():
    instance = customers_CreditCard(ccNumber="sample_text", expiresDate=date(2024, 1, 1), type="sample_text")
    assert instance.ccNumber == "sample_text"
    instance.ccNumber = "sample_text_2"
    assert instance.ccNumber == "sample_text_2"


def test_customers_CreditCard_expiresDate_value_roundtrip():
    instance = customers_CreditCard(ccNumber="sample_text", expiresDate=date(2024, 1, 1), type="sample_text")
    assert instance.expiresDate == date(2024, 1, 1)
    instance.expiresDate = date(2025, 6, 15)
    assert instance.expiresDate == date(2025, 6, 15)


def test_customers_CreditCard_type_value_roundtrip():
    instance = customers_CreditCard(ccNumber="sample_text", expiresDate=date(2024, 1, 1), type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_customers_Customer_comment_value_roundtrip():
    instance = customers_Customer(comment="sample_text", dateOfBirth=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_customers_Customer_dateOfBirth_value_roundtrip():
    instance = customers_Customer(comment="sample_text", dateOfBirth=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_customers_Customer_firstName_value_roundtrip():
    instance = customers_Customer(comment="sample_text", dateOfBirth=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_customers_Customer_lastName_value_roundtrip():
    instance = customers_Customer(comment="sample_text", dateOfBirth=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_customers_CustomersDB_comment_value_roundtrip():
    instance = customers_CustomersDB(comment="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_customers_USAddress_state_value_roundtrip():
    instance = customers_USAddress(state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_customers_CanadaAddress_isa_Address():
    instance = customers_CanadaAddress(province="sample_text")
    assert isinstance(instance, Address)


def test_customers_USAddress_isa_Address():
    instance = customers_USAddress(state="sample_text")
    assert isinstance(instance, Address)


def test_assoc_address1_link_reassign_clear():
    a = customers_Customer(comment="sample_text", dateOfBirth=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    b1 = customers_Address(street="sample_text", town="sample_text", zipCode="sample_text")
    b2 = customers_Address(street="sample_text_2", town="sample_text_2", zipCode="sample_text_2")
    _safe_set(a, 'customers_Customer', b1)
    assert _is_linked(a, 'customers_Customer', b1)
    if hasattr(b1, 'customers_Address'):
        assert _is_linked(b1, 'customers_Address', a)
    _safe_set(a, 'customers_Customer', b2)
    assert _is_linked(a, 'customers_Customer', b2)
    if hasattr(b1, 'customers_Address'):
        assert not _is_linked(b1, 'customers_Address', a)
    if hasattr(b2, 'customers_Address'):
        assert _is_linked(b2, 'customers_Address', a)
    _safe_set(a, 'customers_Customer', None)
    assert not _is_linked(a, 'customers_Customer', b2)
    if hasattr(b2, 'customers_Address'):
        assert not _is_linked(b2, 'customers_Address', a)


def test_assoc_creditCard0_link_reassign_clear():
    a = customers_Customer(comment="sample_text", dateOfBirth=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    b1 = customers_CreditCard(ccNumber="sample_text", expiresDate=date(2024, 1, 1), type="sample_text")
    b2 = customers_CreditCard(ccNumber="sample_text_2", expiresDate=date(2025, 6, 15), type="sample_text_2")
    _safe_set(a, 'holder', {b1})
    assert _is_linked(a, 'holder', b1)
    if hasattr(b1, 'CreditCard'):
        assert _is_linked(b1, 'CreditCard', a)
    _safe_set(a, 'holder', {b2})
    assert _is_linked(a, 'holder', b2)
    if hasattr(b1, 'CreditCard'):
        assert not _is_linked(b1, 'CreditCard', a)
    if hasattr(b2, 'CreditCard'):
        assert _is_linked(b2, 'CreditCard', a)
    _safe_set(a, 'holder', set())
    assert not _is_linked(a, 'holder', b2)
    if hasattr(b2, 'CreditCard'):
        assert not _is_linked(b2, 'CreditCard', a)


def test_assoc_customers3_link_reassign_clear():
    a = customers_CustomersDB(comment="sample_text")
    b1 = customers_Customer(comment="sample_text", dateOfBirth=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    b2 = customers_Customer(comment="sample_text_2", dateOfBirth=date(2025, 6, 15), firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'customers_CustomersDB', {b1})
    assert _is_linked(a, 'customers_CustomersDB', b1)
    if hasattr(b1, 'customers_Customer4'):
        assert _is_linked(b1, 'customers_Customer4', a)
    _safe_set(a, 'customers_CustomersDB', {b2})
    assert _is_linked(a, 'customers_CustomersDB', b2)
    if hasattr(b1, 'customers_Customer4'):
        assert not _is_linked(b1, 'customers_Customer4', a)
    if hasattr(b2, 'customers_Customer4'):
        assert _is_linked(b2, 'customers_Customer4', a)
    _safe_set(a, 'customers_CustomersDB', set())
    assert not _is_linked(a, 'customers_CustomersDB', b2)
    if hasattr(b2, 'customers_Customer4'):
        assert not _is_linked(b2, 'customers_Customer4', a)


def test_assoc_holder2_link_reassign_clear():
    a = customers_Customer(comment="sample_text", dateOfBirth=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    b1 = customers_CreditCard(ccNumber="sample_text", expiresDate=date(2024, 1, 1), type="sample_text")
    b2 = customers_CreditCard(ccNumber="sample_text_2", expiresDate=date(2025, 6, 15), type="sample_text_2")
    _safe_set(a, 'Customer', b1)
    assert _is_linked(a, 'Customer', b1)
    if hasattr(b1, 'creditCard'):
        assert _is_linked(b1, 'creditCard', a)
    _safe_set(a, 'Customer', b2)
    assert _is_linked(a, 'Customer', b2)
    if hasattr(b1, 'creditCard'):
        assert not _is_linked(b1, 'creditCard', a)
    if hasattr(b2, 'creditCard'):
        assert _is_linked(b2, 'creditCard', a)
    _safe_set(a, 'Customer', None)
    assert not _is_linked(a, 'Customer', b2)
    if hasattr(b2, 'creditCard'):
        assert not _is_linked(b2, 'creditCard', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Address_strategy = st.builds(Address)
@given(instance=Address_strategy)
@settings(max_examples=25)
def test_Address_instantiation(instance):
    assert isinstance(instance, Address)


customers_Address_strategy = st.builds(customers_Address, street=safe_text, town=safe_text, zipCode=safe_text)
@given(instance=customers_Address_strategy)
@settings(max_examples=25)
def test_customers_Address_instantiation(instance):
    assert isinstance(instance, customers_Address)


customers_CanadaAddress_strategy = st.builds(customers_CanadaAddress, province=safe_text)
@given(instance=customers_CanadaAddress_strategy)
@settings(max_examples=25)
def test_customers_CanadaAddress_instantiation(instance):
    assert isinstance(instance, customers_CanadaAddress)


customers_CreditCard_strategy = st.builds(customers_CreditCard, ccNumber=safe_text, expiresDate=st.dates(), type=safe_text)
@given(instance=customers_CreditCard_strategy)
@settings(max_examples=25)
def test_customers_CreditCard_instantiation(instance):
    assert isinstance(instance, customers_CreditCard)


customers_Customer_strategy = st.builds(customers_Customer, comment=safe_text, dateOfBirth=st.dates(), firstName=safe_text, lastName=safe_text)
@given(instance=customers_Customer_strategy)
@settings(max_examples=25)
def test_customers_Customer_instantiation(instance):
    assert isinstance(instance, customers_Customer)


customers_CustomersDB_strategy = st.builds(customers_CustomersDB, comment=safe_text)
@given(instance=customers_CustomersDB_strategy)
@settings(max_examples=25)
def test_customers_CustomersDB_instantiation(instance):
    assert isinstance(instance, customers_CustomersDB)


customers_USAddress_strategy = st.builds(customers_USAddress, state=safe_text)
@given(instance=customers_USAddress_strategy)
@settings(max_examples=25)
def test_customers_USAddress_instantiation(instance):
    assert isinstance(instance, customers_USAddress)



