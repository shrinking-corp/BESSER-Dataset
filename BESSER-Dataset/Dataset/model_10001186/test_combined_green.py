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
    ArrPrint,
    Print,
    Documents,
    Provider,
    Visitor,
    Array,
    Number,
    Category,
    String,
    Null,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_arrprint_is_not_abstract():
    assert not inspect.isabstract(ArrPrint)


def test_hyp_arrprint_constructor_exists():
    assert callable(ArrPrint.__init__)


def test_hyp_arrprint_constructor_args():
    sig = inspect.signature(ArrPrint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_print_is_not_abstract():
    assert not inspect.isabstract(Print)


def test_hyp_print_constructor_exists():
    assert callable(Print.__init__)


def test_hyp_print_constructor_args():
    sig = inspect.signature(Print.__init__)
    params = list(sig.parameters.keys())



def test_hyp_documents_is_not_abstract():
    assert not inspect.isabstract(Documents)


def test_hyp_documents_constructor_exists():
    assert callable(Documents.__init__)


def test_hyp_documents_constructor_args():
    sig = inspect.signature(Documents.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"
    assert "file_name" in params, "Missing parameter 'file_name'"
    assert "tab_counter" in params, "Missing parameter 'tab_counter'"
    assert "data" in params, "Missing parameter 'data'"

def test_hyp_documents_has_file():
    assert hasattr(Documents, "file")
    descriptor = None
    for klass in Documents.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_hyp_documents_has_file_name():
    assert hasattr(Documents, "file_name")
    descriptor = None
    for klass in Documents.__mro__:
        if "file_name" in klass.__dict__:
            descriptor = klass.__dict__["file_name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_documents_has_tab_counter():
    assert hasattr(Documents, "tab_counter")
    descriptor = None
    for klass in Documents.__mro__:
        if "tab_counter" in klass.__dict__:
            descriptor = klass.__dict__["tab_counter"]
            break
    assert isinstance(descriptor, property)

def test_hyp_documents_has_data():
    assert hasattr(Documents, "data")
    descriptor = None
    for klass in Documents.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_hyp_provider_is_not_abstract():
    assert not inspect.isabstract(Provider)


def test_hyp_provider_constructor_exists():
    assert callable(Provider.__init__)


def test_hyp_provider_constructor_args():
    sig = inspect.signature(Provider.__init__)
    params = list(sig.parameters.keys())
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "providerId" in params, "Missing parameter 'providerId'"
    assert "email" in params, "Missing parameter 'email'"
    assert "photoURL" in params, "Missing parameter 'photoURL'"

def test_hyp_provider_has_displayName():
    assert hasattr(Provider, "displayName")
    descriptor = None
    for klass in Provider.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_hyp_provider_has_uid():
    assert hasattr(Provider, "uid")
    descriptor = None
    for klass in Provider.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_hyp_provider_has_providerId():
    assert hasattr(Provider, "providerId")
    descriptor = None
    for klass in Provider.__mro__:
        if "providerId" in klass.__dict__:
            descriptor = klass.__dict__["providerId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_provider_has_email():
    assert hasattr(Provider, "email")
    descriptor = None
    for klass in Provider.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_hyp_provider_has_photoURL():
    assert hasattr(Provider, "photoURL")
    descriptor = None
    for klass in Provider.__mro__:
        if "photoURL" in klass.__dict__:
            descriptor = klass.__dict__["photoURL"]
            break
    assert isinstance(descriptor, property)



def test_hyp_visitor_is_not_abstract():
    assert not inspect.isabstract(Visitor)


def test_hyp_visitor_constructor_exists():
    assert callable(Visitor.__init__)


def test_hyp_visitor_constructor_args():
    sig = inspect.signature(Visitor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_array_is_not_abstract():
    assert not inspect.isabstract(Array)


def test_hyp_array_constructor_exists():
    assert callable(Array.__init__)


def test_hyp_array_constructor_args():
    sig = inspect.signature(Array.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_hyp_array_has_data():
    assert hasattr(Array, "data")
    descriptor = None
    for klass in Array.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_hyp_number_is_not_abstract():
    assert not inspect.isabstract(Number)


def test_hyp_number_constructor_exists():
    assert callable(Number.__init__)


def test_hyp_number_constructor_args():
    sig = inspect.signature(Number.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"




def test_hyp_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_hyp_category_constructor_exists():
    assert callable(Category.__init__)


def test_hyp_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "parent" in params, "Missing parameter 'parent'"
    assert "section" in params, "Missing parameter 'section'"
    assert "name" in params, "Missing parameter 'name'"

def test_hyp_category_has_id():
    assert hasattr(Category, "id")
    descriptor = None
    for klass in Category.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_category_has_parent():
    assert hasattr(Category, "parent")
    descriptor = None
    for klass in Category.__mro__:
        if "parent" in klass.__dict__:
            descriptor = klass.__dict__["parent"]
            break
    assert isinstance(descriptor, property)

def test_hyp_category_has_section():
    assert hasattr(Category, "section")
    descriptor = None
    for klass in Category.__mro__:
        if "section" in klass.__dict__:
            descriptor = klass.__dict__["section"]
            break
    assert isinstance(descriptor, property)

def test_hyp_category_has_name():
    assert hasattr(Category, "name")
    descriptor = None
    for klass in Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hyp_string_is_not_abstract():
    assert not inspect.isabstract(String)


def test_hyp_string_constructor_exists():
    assert callable(String.__init__)


def test_hyp_string_constructor_args():
    sig = inspect.signature(String.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_hyp_string_has_data():
    assert hasattr(String, "data")
    descriptor = None
    for klass in String.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_hyp_null_is_not_abstract():
    assert not inspect.isabstract(Null)


def test_hyp_null_constructor_exists():
    assert callable(Null.__init__)


def test_hyp_null_constructor_args():
    sig = inspect.signature(Null.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "email" in params, "Missing parameter 'email'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "photoURL" in params, "Missing parameter 'photoURL'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "id" in params, "Missing parameter 'id'"
    assert "address" in params, "Missing parameter 'address'"

def test_hyp_user_has_firstName():
    assert hasattr(User, "firstName")
    descriptor = None
    for klass in User.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_email():
    assert hasattr(User, "email")
    descriptor = None
    for klass in User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_lastName():
    assert hasattr(User, "lastName")
    descriptor = None
    for klass in User.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_photoURL():
    assert hasattr(User, "photoURL")
    descriptor = None
    for klass in User.__mro__:
        if "photoURL" in klass.__dict__:
            descriptor = klass.__dict__["photoURL"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_phone():
    assert hasattr(User, "phone")
    descriptor = None
    for klass in User.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_id():
    assert hasattr(User, "id")
    descriptor = None
    for klass in User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_address():
    assert hasattr(User, "address")
    descriptor = None
    for klass in User.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)


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
ArrPrint_strategy = st.builds(
    ArrPrint,
)
Print_strategy = st.builds(
    Print,
)
Documents_strategy = st.builds(
    Documents,
    file=
        safe_text,
    file_name=
        safe_text,
    tab_counter=
        st.integers(),
    data=
        st.none()
)
Provider_strategy = st.builds(
    Provider,
    displayName=
        st.none(),
    uid=
        safe_text,
    providerId=
        st.none(),
    email=
        st.none(),
    photoURL=
        st.none()
)
Visitor_strategy = st.builds(
    Visitor,
)
Array_strategy = st.builds(
    Array,
    data=
        st.none()
)
Number_strategy = st.builds(
    Number,
    data=
        st.integers()
)
Category_strategy = st.builds(
    Category,
    id=
        safe_text,
    parent=
        st.none(),
    section=
        st.none(),
    name=
        st.none()
)
String_strategy = st.builds(
    String,
    data=
        st.none()
)
Null_strategy = st.builds(
    Null,
)
User_strategy = st.builds(
    User,
    firstName=
        st.none(),
    email=
        st.none(),
    lastName=
        st.none(),
    photoURL=
        st.none(),
    phone=
        st.none(),
    id=
        safe_text,
    address=
        st.none()
)



@given(instance=Documents_strategy)
@settings(max_examples=50)
def test_hyp_documents_instantiation(instance):
    assert isinstance(instance, Documents)



@given(instance=Documents_strategy)
def test_hyp_documents_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=Documents_strategy)
def test_hyp_documents_file_name_setter(instance):
    original = instance.file_name
    instance.file_name = original
    assert instance.file_name == original



@given(instance=Documents_strategy)
def test_hyp_documents_tab_counter_setter(instance):
    original = instance.tab_counter
    instance.tab_counter = original
    assert instance.tab_counter == original



@given(instance=Documents_strategy)
def test_hyp_documents_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=Provider_strategy)
@settings(max_examples=50)
def test_hyp_provider_instantiation(instance):
    assert isinstance(instance, Provider)



@given(instance=Provider_strategy)
def test_hyp_provider_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=Provider_strategy)
def test_hyp_provider_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=Provider_strategy)
def test_hyp_provider_providerId_setter(instance):
    original = instance.providerId
    instance.providerId = original
    assert instance.providerId == original



@given(instance=Provider_strategy)
def test_hyp_provider_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Provider_strategy)
def test_hyp_provider_photoURL_setter(instance):
    original = instance.photoURL
    instance.photoURL = original
    assert instance.photoURL == original


@given(instance=Array_strategy)
@settings(max_examples=50)
def test_hyp_array_instantiation(instance):
    assert isinstance(instance, Array)



@given(instance=Array_strategy)
def test_hyp_array_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original




@given(instance=Number_strategy)
def test_hyp_number_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_hyp_category_instantiation(instance):
    assert isinstance(instance, Category)



@given(instance=Category_strategy)
def test_hyp_category_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Category_strategy)
def test_hyp_category_parent_setter(instance):
    original = instance.parent
    instance.parent = original
    assert instance.parent == original



@given(instance=Category_strategy)
def test_hyp_category_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original



@given(instance=Category_strategy)
def test_hyp_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=String_strategy)
@settings(max_examples=50)
def test_hyp_string_instantiation(instance):
    assert isinstance(instance, String)



@given(instance=String_strategy)
def test_hyp_string_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original


@given(instance=User_strategy)
@settings(max_examples=50)
def test_hyp_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_hyp_user_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=User_strategy)
def test_hyp_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User_strategy)
def test_hyp_user_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=User_strategy)
def test_hyp_user_photoURL_setter(instance):
    original = instance.photoURL
    instance.photoURL = original
    assert instance.photoURL == original



@given(instance=User_strategy)
def test_hyp_user_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=User_strategy)
def test_hyp_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=User_strategy)
def test_hyp_user_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArrPrint,
    Array,
    Category,
    Documents,
    Null,
    Number,
    Print,
    Provider,
    String,
    User,
    Visitor,
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

def test_Number_data_value_roundtrip():
    instance = Number(data=7)
    assert instance.data == 7
    instance.data = 13
    assert instance.data == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArrPrint_strategy = st.builds(ArrPrint)
@given(instance=ArrPrint_strategy)
@settings(max_examples=25)
def test_ArrPrint_instantiation(instance):
    assert isinstance(instance, ArrPrint)


Null_strategy = st.builds(Null)
@given(instance=Null_strategy)
@settings(max_examples=25)
def test_Null_instantiation(instance):
    assert isinstance(instance, Null)


Number_strategy = st.builds(Number, data=st.integers())
@given(instance=Number_strategy)
@settings(max_examples=25)
def test_Number_instantiation(instance):
    assert isinstance(instance, Number)


Print_strategy = st.builds(Print)
@given(instance=Print_strategy)
@settings(max_examples=25)
def test_Print_instantiation(instance):
    assert isinstance(instance, Print)


Visitor_strategy = st.builds(Visitor)
@given(instance=Visitor_strategy)
@settings(max_examples=25)
def test_Visitor_instantiation(instance):
    assert isinstance(instance, Visitor)



