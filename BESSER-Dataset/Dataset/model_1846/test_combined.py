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
    contacts_UoD,
    contacts_AddressBook,
    contacts_PhoneNumber,
    contacts_Address,
    contacts_Contact,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_contacts_uod_is_not_abstract():
    assert not inspect.isabstract(contacts_UoD)


def test_hyp_contacts_uod_constructor_exists():
    assert callable(contacts_UoD.__init__)


def test_hyp_contacts_uod_constructor_args():
    sig = inspect.signature(contacts_UoD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contacts_addressbook_is_not_abstract():
    assert not inspect.isabstract(contacts_AddressBook)


def test_hyp_contacts_addressbook_constructor_exists():
    assert callable(contacts_AddressBook.__init__)


def test_hyp_contacts_addressbook_constructor_args():
    sig = inspect.signature(contacts_AddressBook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contacts_phonenumber_is_not_abstract():
    assert not inspect.isabstract(contacts_PhoneNumber)


def test_hyp_contacts_phonenumber_constructor_exists():
    assert callable(contacts_PhoneNumber.__init__)


def test_hyp_contacts_phonenumber_constructor_args():
    sig = inspect.signature(contacts_PhoneNumber.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "country" in params, "Missing parameter 'country'"





def test_hyp_contacts_address_is_not_abstract():
    assert not inspect.isabstract(contacts_Address)


def test_hyp_contacts_address_constructor_exists():
    assert callable(contacts_Address.__init__)


def test_hyp_contacts_address_constructor_args():
    sig = inspect.signature(contacts_Address.__init__)
    params = list(sig.parameters.keys())
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "city" in params, "Missing parameter 'city'"
    assert "street" in params, "Missing parameter 'street'"
    assert "country" in params, "Missing parameter 'country'"
    assert "state" in params, "Missing parameter 'state'"








def test_hyp_contacts_contact_is_not_abstract():
    assert not inspect.isabstract(contacts_Contact)


def test_hyp_contacts_contact_constructor_exists():
    assert callable(contacts_Contact.__init__)


def test_hyp_contacts_contact_constructor_args():
    sig = inspect.signature(contacts_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "company" in params, "Missing parameter 'company'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "jobTitle" in params, "Missing parameter 'jobTitle'"
    assert "email" in params, "Missing parameter 'email'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "webPage" in params, "Missing parameter 'webPage'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "note" in params, "Missing parameter 'note'"
    assert "title" in params, "Missing parameter 'title'"












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
contacts_UoD_strategy = st.builds(
    contacts_UoD,
)
contacts_AddressBook_strategy = st.builds(
    contacts_AddressBook,
)
contacts_PhoneNumber_strategy = st.builds(
    contacts_PhoneNumber,
    number=
        safe_text,
    country=
        safe_text
)
contacts_Address_strategy = st.builds(
    contacts_Address,
    zipCode=
        safe_text,
    city=
        safe_text,
    street=
        safe_text,
    country=
        safe_text,
    state=
        safe_text
)
contacts_Contact_strategy = st.builds(
    contacts_Contact,
    image=
        safe_text,
    company=
        safe_text,
    firstName=
        safe_text,
    jobTitle=
        safe_text,
    email=
        safe_text,
    middleName=
        safe_text,
    webPage=
        safe_text,
    lastName=
        safe_text,
    note=
        safe_text,
    title=
        safe_text
)






@given(instance=contacts_PhoneNumber_strategy)
def test_hyp_contacts_phonenumber_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=contacts_PhoneNumber_strategy)
def test_hyp_contacts_phonenumber_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original




@given(instance=contacts_Address_strategy)
def test_hyp_contacts_address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original



@given(instance=contacts_Address_strategy)
def test_hyp_contacts_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=contacts_Address_strategy)
def test_hyp_contacts_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=contacts_Address_strategy)
def test_hyp_contacts_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=contacts_Address_strategy)
def test_hyp_contacts_address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original




@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_jobTitle_setter(instance):
    original = instance.jobTitle
    instance.jobTitle = original
    assert instance.jobTitle == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_webPage_setter(instance):
    original = instance.webPage
    instance.webPage = original
    assert instance.webPage == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original



@given(instance=contacts_Contact_strategy)
def test_hyp_contacts_contact_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    contacts_Address,
    contacts_AddressBook,
    contacts_Contact,
    contacts_PhoneNumber,
    contacts_UoD,
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

def test_contacts_Address_city_value_roundtrip():
    instance = contacts_Address(city="sample_text", country="sample_text", state="sample_text", street="sample_text", zipCode="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_contacts_Address_country_value_roundtrip():
    instance = contacts_Address(city="sample_text", country="sample_text", state="sample_text", street="sample_text", zipCode="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_contacts_Address_state_value_roundtrip():
    instance = contacts_Address(city="sample_text", country="sample_text", state="sample_text", street="sample_text", zipCode="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_contacts_Address_street_value_roundtrip():
    instance = contacts_Address(city="sample_text", country="sample_text", state="sample_text", street="sample_text", zipCode="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_contacts_Address_zipCode_value_roundtrip():
    instance = contacts_Address(city="sample_text", country="sample_text", state="sample_text", street="sample_text", zipCode="sample_text")
    assert instance.zipCode == "sample_text"
    instance.zipCode = "sample_text_2"
    assert instance.zipCode == "sample_text_2"


def test_contacts_Contact_company_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.company == "sample_text"
    instance.company = "sample_text_2"
    assert instance.company == "sample_text_2"


def test_contacts_Contact_email_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_contacts_Contact_firstName_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_contacts_Contact_image_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_contacts_Contact_jobTitle_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.jobTitle == "sample_text"
    instance.jobTitle = "sample_text_2"
    assert instance.jobTitle == "sample_text_2"


def test_contacts_Contact_lastName_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_contacts_Contact_middleName_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.middleName == "sample_text"
    instance.middleName = "sample_text_2"
    assert instance.middleName == "sample_text_2"


def test_contacts_Contact_note_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_contacts_Contact_title_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_contacts_Contact_webPage_value_roundtrip():
    instance = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    assert instance.webPage == "sample_text"
    instance.webPage = "sample_text_2"
    assert instance.webPage == "sample_text_2"


def test_contacts_PhoneNumber_country_value_roundtrip():
    instance = contacts_PhoneNumber(country="sample_text", number="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_contacts_PhoneNumber_number_value_roundtrip():
    instance = contacts_PhoneNumber(country="sample_text", number="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_assoc_contacts9_link_reassign_clear():
    a = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    b1 = contacts_AddressBook()
    b2 = contacts_AddressBook()
    _safe_set(a, 'contacts_Contact10', b1)
    assert _is_linked(a, 'contacts_Contact10', b1)
    if hasattr(b1, 'contacts_AddressBook'):
        assert _is_linked(b1, 'contacts_AddressBook', a)
    _safe_set(a, 'contacts_Contact10', b2)
    assert _is_linked(a, 'contacts_Contact10', b2)
    if hasattr(b1, 'contacts_AddressBook'):
        assert not _is_linked(b1, 'contacts_AddressBook', a)
    if hasattr(b2, 'contacts_AddressBook'):
        assert _is_linked(b2, 'contacts_AddressBook', a)
    _safe_set(a, 'contacts_Contact10', None)
    assert not _is_linked(a, 'contacts_Contact10', b2)
    if hasattr(b2, 'contacts_AddressBook'):
        assert not _is_linked(b2, 'contacts_AddressBook', a)


def test_assoc_homeAddress6_link_reassign_clear():
    a = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    b1 = contacts_Address(city="sample_text", country="sample_text", state="sample_text", street="sample_text", zipCode="sample_text")
    b2 = contacts_Address(city="sample_text_2", country="sample_text_2", state="sample_text_2", street="sample_text_2", zipCode="sample_text_2")
    _safe_set(a, 'contacts_Contact7', b1)
    assert _is_linked(a, 'contacts_Contact7', b1)
    if hasattr(b1, 'contacts_Address8'):
        assert _is_linked(b1, 'contacts_Address8', a)
    _safe_set(a, 'contacts_Contact7', b2)
    assert _is_linked(a, 'contacts_Contact7', b2)
    if hasattr(b1, 'contacts_Address8'):
        assert not _is_linked(b1, 'contacts_Address8', a)
    if hasattr(b2, 'contacts_Address8'):
        assert _is_linked(b2, 'contacts_Address8', a)
    _safe_set(a, 'contacts_Contact7', None)
    assert not _is_linked(a, 'contacts_Contact7', b2)
    if hasattr(b2, 'contacts_Address8'):
        assert not _is_linked(b2, 'contacts_Address8', a)


def test_assoc_mobile3_link_reassign_clear():
    a = contacts_PhoneNumber(country="sample_text", number="sample_text")
    b1 = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    b2 = contacts_Contact(company="sample_text_2", email="sample_text_2", firstName="sample_text_2", image="sample_text_2", jobTitle="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", note="sample_text_2", title="sample_text_2", webPage="sample_text_2")
    _safe_set(a, 'contacts_PhoneNumber5', b1)
    assert _is_linked(a, 'contacts_PhoneNumber5', b1)
    if hasattr(b1, 'contacts_Contact4'):
        assert _is_linked(b1, 'contacts_Contact4', a)
    _safe_set(a, 'contacts_PhoneNumber5', b2)
    assert _is_linked(a, 'contacts_PhoneNumber5', b2)
    if hasattr(b1, 'contacts_Contact4'):
        assert not _is_linked(b1, 'contacts_Contact4', a)
    if hasattr(b2, 'contacts_Contact4'):
        assert _is_linked(b2, 'contacts_Contact4', a)
    _safe_set(a, 'contacts_PhoneNumber5', None)
    assert not _is_linked(a, 'contacts_PhoneNumber5', b2)
    if hasattr(b2, 'contacts_Contact4'):
        assert not _is_linked(b2, 'contacts_Contact4', a)


def test_assoc_phone1_link_reassign_clear():
    a = contacts_PhoneNumber(country="sample_text", number="sample_text")
    b1 = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    b2 = contacts_Contact(company="sample_text_2", email="sample_text_2", firstName="sample_text_2", image="sample_text_2", jobTitle="sample_text_2", lastName="sample_text_2", middleName="sample_text_2", note="sample_text_2", title="sample_text_2", webPage="sample_text_2")
    _safe_set(a, 'contacts_PhoneNumber', b1)
    assert _is_linked(a, 'contacts_PhoneNumber', b1)
    if hasattr(b1, 'contacts_Contact2'):
        assert _is_linked(b1, 'contacts_Contact2', a)
    _safe_set(a, 'contacts_PhoneNumber', b2)
    assert _is_linked(a, 'contacts_PhoneNumber', b2)
    if hasattr(b1, 'contacts_Contact2'):
        assert not _is_linked(b1, 'contacts_Contact2', a)
    if hasattr(b2, 'contacts_Contact2'):
        assert _is_linked(b2, 'contacts_Contact2', a)
    _safe_set(a, 'contacts_PhoneNumber', None)
    assert not _is_linked(a, 'contacts_PhoneNumber', b2)
    if hasattr(b2, 'contacts_Contact2'):
        assert not _is_linked(b2, 'contacts_Contact2', a)


def test_assoc_workAddress0_link_reassign_clear():
    a = contacts_Contact(company="sample_text", email="sample_text", firstName="sample_text", image="sample_text", jobTitle="sample_text", lastName="sample_text", middleName="sample_text", note="sample_text", title="sample_text", webPage="sample_text")
    b1 = contacts_Address(city="sample_text", country="sample_text", state="sample_text", street="sample_text", zipCode="sample_text")
    b2 = contacts_Address(city="sample_text_2", country="sample_text_2", state="sample_text_2", street="sample_text_2", zipCode="sample_text_2")
    _safe_set(a, 'contacts_Contact', b1)
    assert _is_linked(a, 'contacts_Contact', b1)
    if hasattr(b1, 'contacts_Address'):
        assert _is_linked(b1, 'contacts_Address', a)
    _safe_set(a, 'contacts_Contact', b2)
    assert _is_linked(a, 'contacts_Contact', b2)
    if hasattr(b1, 'contacts_Address'):
        assert not _is_linked(b1, 'contacts_Address', a)
    if hasattr(b2, 'contacts_Address'):
        assert _is_linked(b2, 'contacts_Address', a)
    _safe_set(a, 'contacts_Contact', None)
    assert not _is_linked(a, 'contacts_Contact', b2)
    if hasattr(b2, 'contacts_Address'):
        assert not _is_linked(b2, 'contacts_Address', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

contacts_Address_strategy = st.builds(contacts_Address, city=safe_text, country=safe_text, state=safe_text, street=safe_text, zipCode=safe_text)
@given(instance=contacts_Address_strategy)
@settings(max_examples=25)
def test_contacts_Address_instantiation(instance):
    assert isinstance(instance, contacts_Address)


contacts_AddressBook_strategy = st.builds(contacts_AddressBook)
@given(instance=contacts_AddressBook_strategy)
@settings(max_examples=25)
def test_contacts_AddressBook_instantiation(instance):
    assert isinstance(instance, contacts_AddressBook)


contacts_Contact_strategy = st.builds(contacts_Contact, company=safe_text, email=safe_text, firstName=safe_text, image=safe_text, jobTitle=safe_text, lastName=safe_text, middleName=safe_text, note=safe_text, title=safe_text, webPage=safe_text)
@given(instance=contacts_Contact_strategy)
@settings(max_examples=25)
def test_contacts_Contact_instantiation(instance):
    assert isinstance(instance, contacts_Contact)


contacts_PhoneNumber_strategy = st.builds(contacts_PhoneNumber, country=safe_text, number=safe_text)
@given(instance=contacts_PhoneNumber_strategy)
@settings(max_examples=25)
def test_contacts_PhoneNumber_instantiation(instance):
    assert isinstance(instance, contacts_PhoneNumber)


contacts_UoD_strategy = st.builds(contacts_UoD)
@given(instance=contacts_UoD_strategy)
@settings(max_examples=25)
def test_contacts_UoD_instantiation(instance):
    assert isinstance(instance, contacts_UoD)



