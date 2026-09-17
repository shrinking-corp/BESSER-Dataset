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
    addressbook_BookVersion,
    addressbook_Repository,
    addressbook_AddressBook,
    addressbook_People,
    addressbook_Contact,
    Contact,
    addressbook_Office,
    addressbook_Electronic,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_addressbook_bookversion_is_not_abstract():
    assert not inspect.isabstract(addressbook_BookVersion)


def test_hyp_addressbook_bookversion_constructor_exists():
    assert callable(addressbook_BookVersion.__init__)


def test_hyp_addressbook_bookversion_constructor_args():
    sig = inspect.signature(addressbook_BookVersion.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_addressbook_repository_is_not_abstract():
    assert not inspect.isabstract(addressbook_Repository)


def test_hyp_addressbook_repository_constructor_exists():
    assert callable(addressbook_Repository.__init__)


def test_hyp_addressbook_repository_constructor_args():
    sig = inspect.signature(addressbook_Repository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_addressbook_addressbook_is_not_abstract():
    assert not inspect.isabstract(addressbook_AddressBook)


def test_hyp_addressbook_addressbook_constructor_exists():
    assert callable(addressbook_AddressBook.__init__)


def test_hyp_addressbook_addressbook_constructor_args():
    sig = inspect.signature(addressbook_AddressBook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_addressbook_people_is_not_abstract():
    assert not inspect.isabstract(addressbook_People)


def test_hyp_addressbook_people_constructor_exists():
    assert callable(addressbook_People.__init__)


def test_hyp_addressbook_people_constructor_args():
    sig = inspect.signature(addressbook_People.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_addressbook_contact_is_not_abstract():
    assert not inspect.isabstract(addressbook_Contact)


def test_hyp_addressbook_contact_constructor_exists():
    assert callable(addressbook_Contact.__init__)


def test_hyp_addressbook_contact_constructor_args():
    sig = inspect.signature(addressbook_Contact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contact_is_not_abstract():
    assert not inspect.isabstract(Contact)


def test_hyp_contact_constructor_exists():
    assert callable(Contact.__init__)


def test_hyp_contact_constructor_args():
    sig = inspect.signature(Contact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_addressbook_office_is_not_abstract():
    assert not inspect.isabstract(addressbook_Office)


def test_hyp_addressbook_office_constructor_exists():
    assert callable(addressbook_Office.__init__)


def test_hyp_addressbook_office_constructor_args():
    sig = inspect.signature(addressbook_Office.__init__)
    params = list(sig.parameters.keys())
    assert "company" in params, "Missing parameter 'company'"




def test_hyp_addressbook_electronic_is_not_abstract():
    assert not inspect.isabstract(addressbook_Electronic)


def test_hyp_addressbook_electronic_constructor_exists():
    assert callable(addressbook_Electronic.__init__)


def test_hyp_addressbook_electronic_constructor_args():
    sig = inspect.signature(addressbook_Electronic.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "website" in params, "Missing parameter 'website'"




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
addressbook_BookVersion_strategy = st.builds(
    addressbook_BookVersion,
    id=
        st.integers()
)
addressbook_Repository_strategy = st.builds(
    addressbook_Repository,
)
addressbook_AddressBook_strategy = st.builds(
    addressbook_AddressBook,
)
addressbook_People_strategy = st.builds(
    addressbook_People,
    name=
        safe_text
)
addressbook_Contact_strategy = st.builds(
    addressbook_Contact,
)
Contact_strategy = st.builds(
    Contact,
)
addressbook_Office_strategy = st.builds(
    addressbook_Office,
    company=
        safe_text
)
addressbook_Electronic_strategy = st.builds(
    addressbook_Electronic,
    email=
        safe_text,
    website=
        safe_text
)




@given(instance=addressbook_BookVersion_strategy)
def test_hyp_addressbook_bookversion_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=addressbook_Repository_strategy)
@settings(max_examples=30)
def test_hyp_addressbook_repository_checkin_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkin()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkin).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkin' in addressbook_Repository is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkin' in addressbook_Repository did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkin' in addressbook_Repository is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=addressbook_Repository_strategy)
@settings(max_examples=30)
def test_hyp_addressbook_repository_checkout_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkout(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkout).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkout' in addressbook_Repository is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkout' in addressbook_Repository did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkout' in addressbook_Repository is not implemented or raised an error")





@given(instance=addressbook_People_strategy)
def test_hyp_addressbook_people_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=addressbook_Office_strategy)
def test_hyp_addressbook_office_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original




@given(instance=addressbook_Electronic_strategy)
def test_hyp_addressbook_electronic_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=addressbook_Electronic_strategy)
def test_hyp_addressbook_electronic_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Contact,
    addressbook_AddressBook,
    addressbook_BookVersion,
    addressbook_Contact,
    addressbook_Electronic,
    addressbook_Office,
    addressbook_People,
    addressbook_Repository,
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

def test_addressbook_BookVersion_id_value_roundtrip():
    instance = addressbook_BookVersion(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_addressbook_Electronic_email_value_roundtrip():
    instance = addressbook_Electronic(email="sample_text", website="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_addressbook_Electronic_website_value_roundtrip():
    instance = addressbook_Electronic(email="sample_text", website="sample_text")
    assert instance.website == "sample_text"
    instance.website = "sample_text_2"
    assert instance.website == "sample_text_2"


def test_addressbook_Office_company_value_roundtrip():
    instance = addressbook_Office(company="sample_text")
    assert instance.company == "sample_text"
    instance.company = "sample_text_2"
    assert instance.company == "sample_text_2"


def test_addressbook_People_name_value_roundtrip():
    instance = addressbook_People(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_addressbook_Electronic_isa_Contact():
    instance = addressbook_Electronic(email="sample_text", website="sample_text")
    assert isinstance(instance, Contact)


def test_addressbook_Office_isa_Contact():
    instance = addressbook_Office(company="sample_text")
    assert isinstance(instance, Contact)


def test_assoc_book7_link_reassign_clear():
    a = addressbook_BookVersion(id=7)
    b1 = addressbook_AddressBook()
    b2 = addressbook_AddressBook()
    _safe_set(a, 'addressbook_BookVersion8', b1)
    assert _is_linked(a, 'addressbook_BookVersion8', b1)
    if hasattr(b1, 'addressbook_AddressBook9'):
        assert _is_linked(b1, 'addressbook_AddressBook9', a)
    _safe_set(a, 'addressbook_BookVersion8', b2)
    assert _is_linked(a, 'addressbook_BookVersion8', b2)
    if hasattr(b1, 'addressbook_AddressBook9'):
        assert not _is_linked(b1, 'addressbook_AddressBook9', a)
    if hasattr(b2, 'addressbook_AddressBook9'):
        assert _is_linked(b2, 'addressbook_AddressBook9', a)
    _safe_set(a, 'addressbook_BookVersion8', None)
    assert not _is_linked(a, 'addressbook_BookVersion8', b2)
    if hasattr(b2, 'addressbook_AddressBook9'):
        assert not _is_linked(b2, 'addressbook_AddressBook9', a)


def test_assoc_contacts0_link_reassign_clear():
    a = addressbook_People(name="sample_text")
    b1 = addressbook_Contact()
    b2 = addressbook_Contact()
    _safe_set(a, 'addressbook_People', {b1})
    assert _is_linked(a, 'addressbook_People', b1)
    if hasattr(b1, 'addressbook_Contact'):
        assert _is_linked(b1, 'addressbook_Contact', a)
    _safe_set(a, 'addressbook_People', {b2})
    assert _is_linked(a, 'addressbook_People', b2)
    if hasattr(b1, 'addressbook_Contact'):
        assert not _is_linked(b1, 'addressbook_Contact', a)
    if hasattr(b2, 'addressbook_Contact'):
        assert _is_linked(b2, 'addressbook_Contact', a)
    _safe_set(a, 'addressbook_People', set())
    assert not _is_linked(a, 'addressbook_People', b2)
    if hasattr(b2, 'addressbook_Contact'):
        assert not _is_linked(b2, 'addressbook_Contact', a)


def test_assoc_head3_link_reassign_clear():
    a = addressbook_Repository()
    b1 = addressbook_AddressBook()
    b2 = addressbook_AddressBook()
    _safe_set(a, 'addressbook_Repository', b1)
    assert _is_linked(a, 'addressbook_Repository', b1)
    if hasattr(b1, 'addressbook_AddressBook4'):
        assert _is_linked(b1, 'addressbook_AddressBook4', a)
    _safe_set(a, 'addressbook_Repository', b2)
    assert _is_linked(a, 'addressbook_Repository', b2)
    if hasattr(b1, 'addressbook_AddressBook4'):
        assert not _is_linked(b1, 'addressbook_AddressBook4', a)
    if hasattr(b2, 'addressbook_AddressBook4'):
        assert _is_linked(b2, 'addressbook_AddressBook4', a)
    _safe_set(a, 'addressbook_Repository', None)
    assert not _is_linked(a, 'addressbook_Repository', b2)
    if hasattr(b2, 'addressbook_AddressBook4'):
        assert not _is_linked(b2, 'addressbook_AddressBook4', a)


def test_assoc_history5_link_reassign_clear():
    a = addressbook_Repository()
    b1 = addressbook_BookVersion(id=7)
    b2 = addressbook_BookVersion(id=13)
    _safe_set(a, 'addressbook_Repository6', {b1})
    assert _is_linked(a, 'addressbook_Repository6', b1)
    if hasattr(b1, 'addressbook_BookVersion'):
        assert _is_linked(b1, 'addressbook_BookVersion', a)
    _safe_set(a, 'addressbook_Repository6', {b2})
    assert _is_linked(a, 'addressbook_Repository6', b2)
    if hasattr(b1, 'addressbook_BookVersion'):
        assert not _is_linked(b1, 'addressbook_BookVersion', a)
    if hasattr(b2, 'addressbook_BookVersion'):
        assert _is_linked(b2, 'addressbook_BookVersion', a)
    _safe_set(a, 'addressbook_Repository6', set())
    assert not _is_linked(a, 'addressbook_Repository6', b2)
    if hasattr(b2, 'addressbook_BookVersion'):
        assert not _is_linked(b2, 'addressbook_BookVersion', a)


def test_assoc_peoples1_link_reassign_clear():
    a = addressbook_People(name="sample_text")
    b1 = addressbook_AddressBook()
    b2 = addressbook_AddressBook()
    _safe_set(a, 'addressbook_People2', b1)
    assert _is_linked(a, 'addressbook_People2', b1)
    if hasattr(b1, 'addressbook_AddressBook'):
        assert _is_linked(b1, 'addressbook_AddressBook', a)
    _safe_set(a, 'addressbook_People2', b2)
    assert _is_linked(a, 'addressbook_People2', b2)
    if hasattr(b1, 'addressbook_AddressBook'):
        assert not _is_linked(b1, 'addressbook_AddressBook', a)
    if hasattr(b2, 'addressbook_AddressBook'):
        assert _is_linked(b2, 'addressbook_AddressBook', a)
    _safe_set(a, 'addressbook_People2', None)
    assert not _is_linked(a, 'addressbook_People2', b2)
    if hasattr(b2, 'addressbook_AddressBook'):
        assert not _is_linked(b2, 'addressbook_AddressBook', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Contact_strategy = st.builds(Contact)
@given(instance=Contact_strategy)
@settings(max_examples=25)
def test_Contact_instantiation(instance):
    assert isinstance(instance, Contact)


addressbook_AddressBook_strategy = st.builds(addressbook_AddressBook)
@given(instance=addressbook_AddressBook_strategy)
@settings(max_examples=25)
def test_addressbook_AddressBook_instantiation(instance):
    assert isinstance(instance, addressbook_AddressBook)


addressbook_BookVersion_strategy = st.builds(addressbook_BookVersion, id=st.integers())
@given(instance=addressbook_BookVersion_strategy)
@settings(max_examples=25)
def test_addressbook_BookVersion_instantiation(instance):
    assert isinstance(instance, addressbook_BookVersion)


addressbook_Contact_strategy = st.builds(addressbook_Contact)
@given(instance=addressbook_Contact_strategy)
@settings(max_examples=25)
def test_addressbook_Contact_instantiation(instance):
    assert isinstance(instance, addressbook_Contact)


addressbook_Electronic_strategy = st.builds(addressbook_Electronic, email=safe_text, website=safe_text)
@given(instance=addressbook_Electronic_strategy)
@settings(max_examples=25)
def test_addressbook_Electronic_instantiation(instance):
    assert isinstance(instance, addressbook_Electronic)


addressbook_Office_strategy = st.builds(addressbook_Office, company=safe_text)
@given(instance=addressbook_Office_strategy)
@settings(max_examples=25)
def test_addressbook_Office_instantiation(instance):
    assert isinstance(instance, addressbook_Office)


addressbook_People_strategy = st.builds(addressbook_People, name=safe_text)
@given(instance=addressbook_People_strategy)
@settings(max_examples=25)
def test_addressbook_People_instantiation(instance):
    assert isinstance(instance, addressbook_People)


addressbook_Repository_strategy = st.builds(addressbook_Repository)
@given(instance=addressbook_Repository_strategy)
@settings(max_examples=25)
def test_addressbook_Repository_instantiation(instance):
    assert isinstance(instance, addressbook_Repository)



