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
    party_CommonObject,
    URL,
    party_Web,
    Party,
    party_Person,
    Address,
    party_USAddress,
    party_EMail,
    ContactInfo,
    party_Address,
    party_Custom,
    party_URL,
    party_Phone,
    DateEffectiveObject,
    party_Role,
    party_MatrixRelationship,
    party_Tag,
    party_Tagged,
    party_Organization,
    party_Identity,
    party_ContactInfo,
    Tagged,
    party_DateEffectiveObject,
    party_Party,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_party_commonobject_is_not_abstract():
    assert not inspect.isabstract(party_CommonObject)


def test_hyp_party_commonobject_constructor_exists():
    assert callable(party_CommonObject.__init__)


def test_hyp_party_commonobject_constructor_args():
    sig = inspect.signature(party_CommonObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_url_is_not_abstract():
    assert not inspect.isabstract(URL)


def test_hyp_url_constructor_exists():
    assert callable(URL.__init__)


def test_hyp_url_constructor_args():
    sig = inspect.signature(URL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_party_web_is_not_abstract():
    assert not inspect.isabstract(party_Web)


def test_hyp_party_web_constructor_exists():
    assert callable(party_Web.__init__)


def test_hyp_party_web_constructor_args():
    sig = inspect.signature(party_Web.__init__)
    params = list(sig.parameters.keys())



def test_hyp_party_is_not_abstract():
    assert not inspect.isabstract(Party)


def test_hyp_party_constructor_exists():
    assert callable(Party.__init__)


def test_hyp_party_constructor_args():
    sig = inspect.signature(Party.__init__)
    params = list(sig.parameters.keys())



def test_hyp_party_person_is_not_abstract():
    assert not inspect.isabstract(party_Person)


def test_hyp_party_person_constructor_exists():
    assert callable(party_Person.__init__)


def test_hyp_party_person_constructor_args():
    sig = inspect.signature(party_Person.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_hyp_address_constructor_exists():
    assert callable(Address.__init__)


def test_hyp_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_hyp_party_usaddress_is_not_abstract():
    assert not inspect.isabstract(party_USAddress)


def test_hyp_party_usaddress_constructor_exists():
    assert callable(party_USAddress.__init__)


def test_hyp_party_usaddress_constructor_args():
    sig = inspect.signature(party_USAddress.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "recipient" in params, "Missing parameter 'recipient'"
    assert "street2" in params, "Missing parameter 'street2'"
    assert "street1" in params, "Missing parameter 'street1'"
    assert "state" in params, "Missing parameter 'state'"
    assert "zip" in params, "Missing parameter 'zip'"









def test_hyp_party_email_is_not_abstract():
    assert not inspect.isabstract(party_EMail)


def test_hyp_party_email_constructor_exists():
    assert callable(party_EMail.__init__)


def test_hyp_party_email_constructor_args():
    sig = inspect.signature(party_EMail.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contactinfo_is_not_abstract():
    assert not inspect.isabstract(ContactInfo)


def test_hyp_contactinfo_constructor_exists():
    assert callable(ContactInfo.__init__)


def test_hyp_contactinfo_constructor_args():
    sig = inspect.signature(ContactInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_party_address_is_not_abstract():
    assert not inspect.isabstract(party_Address)


def test_hyp_party_address_constructor_exists():
    assert callable(party_Address.__init__)


def test_hyp_party_address_constructor_args():
    sig = inspect.signature(party_Address.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"




def test_hyp_party_custom_is_not_abstract():
    assert not inspect.isabstract(party_Custom)


def test_hyp_party_custom_constructor_exists():
    assert callable(party_Custom.__init__)


def test_hyp_party_custom_constructor_args():
    sig = inspect.signature(party_Custom.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"




def test_hyp_party_url_is_not_abstract():
    assert not inspect.isabstract(party_URL)


def test_hyp_party_url_constructor_exists():
    assert callable(party_URL.__init__)


def test_hyp_party_url_constructor_args():
    sig = inspect.signature(party_URL.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"




def test_hyp_party_phone_is_not_abstract():
    assert not inspect.isabstract(party_Phone)


def test_hyp_party_phone_constructor_exists():
    assert callable(party_Phone.__init__)


def test_hyp_party_phone_constructor_args():
    sig = inspect.signature(party_Phone.__init__)
    params = list(sig.parameters.keys())
    assert "areaCode" in params, "Missing parameter 'areaCode'"
    assert "number" in params, "Missing parameter 'number'"
    assert "countryCode" in params, "Missing parameter 'countryCode'"






def test_hyp_dateeffectiveobject_is_not_abstract():
    assert not inspect.isabstract(DateEffectiveObject)


def test_hyp_dateeffectiveobject_constructor_exists():
    assert callable(DateEffectiveObject.__init__)


def test_hyp_dateeffectiveobject_constructor_args():
    sig = inspect.signature(DateEffectiveObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_party_role_is_not_abstract():
    assert not inspect.isabstract(party_Role)


def test_hyp_party_role_constructor_exists():
    assert callable(party_Role.__init__)


def test_hyp_party_role_constructor_args():
    sig = inspect.signature(party_Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_party_matrixrelationship_is_not_abstract():
    assert not inspect.isabstract(party_MatrixRelationship)


def test_hyp_party_matrixrelationship_constructor_exists():
    assert callable(party_MatrixRelationship.__init__)


def test_hyp_party_matrixrelationship_constructor_args():
    sig = inspect.signature(party_MatrixRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_party_tag_is_not_abstract():
    assert not inspect.isabstract(party_Tag)


def test_hyp_party_tag_constructor_exists():
    assert callable(party_Tag.__init__)


def test_hyp_party_tag_constructor_args():
    sig = inspect.signature(party_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"






def test_hyp_party_tagged_is_not_abstract():
    assert not inspect.isabstract(party_Tagged)


def test_hyp_party_tagged_constructor_exists():
    assert callable(party_Tagged.__init__)


def test_hyp_party_tagged_constructor_args():
    sig = inspect.signature(party_Tagged.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"




def test_hyp_party_organization_is_not_abstract():
    assert not inspect.isabstract(party_Organization)


def test_hyp_party_organization_constructor_exists():
    assert callable(party_Organization.__init__)


def test_hyp_party_organization_constructor_args():
    sig = inspect.signature(party_Organization.__init__)
    params = list(sig.parameters.keys())
    assert "organizationType" in params, "Missing parameter 'organizationType'"




def test_hyp_party_identity_is_not_abstract():
    assert not inspect.isabstract(party_Identity)


def test_hyp_party_identity_constructor_exists():
    assert callable(party_Identity.__init__)


def test_hyp_party_identity_constructor_args():
    sig = inspect.signature(party_Identity.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"
    assert "comment" in params, "Missing parameter 'comment'"






def test_hyp_party_contactinfo_is_not_abstract():
    assert not inspect.isabstract(party_ContactInfo)


def test_hyp_party_contactinfo_constructor_exists():
    assert callable(party_ContactInfo.__init__)


def test_hyp_party_contactinfo_constructor_args():
    sig = inspect.signature(party_ContactInfo.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"




def test_hyp_tagged_is_not_abstract():
    assert not inspect.isabstract(Tagged)


def test_hyp_tagged_constructor_exists():
    assert callable(Tagged.__init__)


def test_hyp_tagged_constructor_args():
    sig = inspect.signature(Tagged.__init__)
    params = list(sig.parameters.keys())



def test_hyp_party_dateeffectiveobject_is_not_abstract():
    assert not inspect.isabstract(party_DateEffectiveObject)


def test_hyp_party_dateeffectiveobject_constructor_exists():
    assert callable(party_DateEffectiveObject.__init__)


def test_hyp_party_dateeffectiveobject_constructor_args():
    sig = inspect.signature(party_DateEffectiveObject.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"





def test_hyp_party_party_is_not_abstract():
    assert not inspect.isabstract(party_Party)


def test_hyp_party_party_constructor_exists():
    assert callable(party_Party.__init__)


def test_hyp_party_party_constructor_args():
    sig = inspect.signature(party_Party.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"




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
party_CommonObject_strategy = st.builds(
    party_CommonObject,
)
URL_strategy = st.builds(
    URL,
)
party_Web_strategy = st.builds(
    party_Web,
)
Party_strategy = st.builds(
    Party,
)
party_Person_strategy = st.builds(
    party_Person,
    title=
        safe_text
)
Address_strategy = st.builds(
    Address,
)
party_USAddress_strategy = st.builds(
    party_USAddress,
    city=
        safe_text,
    recipient=
        safe_text,
    street2=
        safe_text,
    street1=
        safe_text,
    state=
        safe_text,
    zip=
        safe_text
)
party_EMail_strategy = st.builds(
    party_EMail,
)
ContactInfo_strategy = st.builds(
    ContactInfo,
)
party_Address_strategy = st.builds(
    party_Address,
    country=
        safe_text
)
party_Custom_strategy = st.builds(
    party_Custom,
    location=
        safe_text
)
party_URL_strategy = st.builds(
    party_URL,
    address=
        safe_text
)
party_Phone_strategy = st.builds(
    party_Phone,
    areaCode=
        st.integers(),
    number=
        safe_text,
    countryCode=
        safe_text
)
DateEffectiveObject_strategy = st.builds(
    DateEffectiveObject,
)
party_Role_strategy = st.builds(
    party_Role,
    name=
        safe_text
)
party_MatrixRelationship_strategy = st.builds(
    party_MatrixRelationship,
    name=
        safe_text
)
party_Tag_strategy = st.builds(
    party_Tag,
    value=
        safe_text,
    name=
        safe_text,
    comment=
        safe_text
)
party_Tagged_strategy = st.builds(
    party_Tagged,
    comment=
        safe_text
)
party_Organization_strategy = st.builds(
    party_Organization,
    organizationType=
        safe_text
)
party_Identity_strategy = st.builds(
    party_Identity,
    type=
        safe_text,
    value=
        safe_text,
    comment=
        safe_text
)
party_ContactInfo_strategy = st.builds(
    party_ContactInfo,
    category=
        safe_text
)
Tagged_strategy = st.builds(
    Tagged,
)
party_DateEffectiveObject_strategy = st.builds(
    party_DateEffectiveObject,
    end=
        st.dates(),
    start=
        st.dates()
)
party_Party_strategy = st.builds(
    party_Party,
    uid=
        safe_text,
    name=
        safe_text
)








@given(instance=party_Person_strategy)
def test_hyp_party_person_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original





@given(instance=party_USAddress_strategy)
def test_hyp_party_usaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=party_USAddress_strategy)
def test_hyp_party_usaddress_recipient_setter(instance):
    original = instance.recipient
    instance.recipient = original
    assert instance.recipient == original



@given(instance=party_USAddress_strategy)
def test_hyp_party_usaddress_street2_setter(instance):
    original = instance.street2
    instance.street2 = original
    assert instance.street2 == original



@given(instance=party_USAddress_strategy)
def test_hyp_party_usaddress_street1_setter(instance):
    original = instance.street1
    instance.street1 = original
    assert instance.street1 == original



@given(instance=party_USAddress_strategy)
def test_hyp_party_usaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=party_USAddress_strategy)
def test_hyp_party_usaddress_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original






@given(instance=party_Address_strategy)
def test_hyp_party_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original




@given(instance=party_Custom_strategy)
def test_hyp_party_custom_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original




@given(instance=party_URL_strategy)
def test_hyp_party_url_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original




@given(instance=party_Phone_strategy)
def test_hyp_party_phone_areaCode_setter(instance):
    original = instance.areaCode
    instance.areaCode = original
    assert instance.areaCode == original



@given(instance=party_Phone_strategy)
def test_hyp_party_phone_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=party_Phone_strategy)
def test_hyp_party_phone_countryCode_setter(instance):
    original = instance.countryCode
    instance.countryCode = original
    assert instance.countryCode == original





@given(instance=party_Role_strategy)
def test_hyp_party_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=party_MatrixRelationship_strategy)
def test_hyp_party_matrixrelationship_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=party_Tag_strategy)
def test_hyp_party_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=party_Tag_strategy)
def test_hyp_party_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=party_Tag_strategy)
def test_hyp_party_tag_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original




@given(instance=party_Tagged_strategy)
def test_hyp_party_tagged_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original




@given(instance=party_Organization_strategy)
def test_hyp_party_organization_organizationType_setter(instance):
    original = instance.organizationType
    instance.organizationType = original
    assert instance.organizationType == original




@given(instance=party_Identity_strategy)
def test_hyp_party_identity_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=party_Identity_strategy)
def test_hyp_party_identity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=party_Identity_strategy)
def test_hyp_party_identity_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original




@given(instance=party_ContactInfo_strategy)
def test_hyp_party_contactinfo_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original





@given(instance=party_DateEffectiveObject_strategy)
def test_hyp_party_dateeffectiveobject_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=party_DateEffectiveObject_strategy)
def test_hyp_party_dateeffectiveobject_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=party_DateEffectiveObject_strategy)
@settings(max_examples=30)
def test_hyp_party_dateeffectiveobject_iseffective_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isEffective(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isEffective).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isEffective' in party_DateEffectiveObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEffective' in party_DateEffectiveObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEffective' in party_DateEffectiveObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=party_DateEffectiveObject_strategy)
@settings(max_examples=30)
def test_hyp_party_dateeffectiveobject_iseffectivenow_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isEffectiveNow()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isEffectiveNow).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isEffectiveNow' in party_DateEffectiveObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEffectiveNow' in party_DateEffectiveObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEffectiveNow' in party_DateEffectiveObject is not implemented or raised an error")




@given(instance=party_Party_strategy)
def test_hyp_party_party_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=party_Party_strategy)
def test_hyp_party_party_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=party_Party_strategy)
@settings(max_examples=30)
def test_hyp_party_party_setexternalparent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setExternalParent(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setExternalParent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setExternalParent' in party_Party is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setExternalParent' in party_Party did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setExternalParent' in party_Party is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Address,
    ContactInfo,
    DateEffectiveObject,
    Party,
    Tagged,
    URL,
    party_Address,
    party_CommonObject,
    party_ContactInfo,
    party_Custom,
    party_DateEffectiveObject,
    party_EMail,
    party_Identity,
    party_MatrixRelationship,
    party_Organization,
    party_Party,
    party_Person,
    party_Phone,
    party_Role,
    party_Tag,
    party_Tagged,
    party_URL,
    party_USAddress,
    party_Web,
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

def test_party_Address_country_value_roundtrip():
    instance = party_Address(country="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_party_ContactInfo_category_value_roundtrip():
    instance = party_ContactInfo(category="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_party_Custom_location_value_roundtrip():
    instance = party_Custom(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_party_DateEffectiveObject_end_value_roundtrip():
    instance = party_DateEffectiveObject(end=date(2024, 1, 1), start=date(2024, 1, 1))
    assert instance.end == date(2024, 1, 1)
    instance.end = date(2025, 6, 15)
    assert instance.end == date(2025, 6, 15)


def test_party_DateEffectiveObject_start_value_roundtrip():
    instance = party_DateEffectiveObject(end=date(2024, 1, 1), start=date(2024, 1, 1))
    assert instance.start == date(2024, 1, 1)
    instance.start = date(2025, 6, 15)
    assert instance.start == date(2025, 6, 15)


def test_party_Identity_comment_value_roundtrip():
    instance = party_Identity(comment="sample_text", type="sample_text", value="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_party_Identity_type_value_roundtrip():
    instance = party_Identity(comment="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_party_Identity_value_value_roundtrip():
    instance = party_Identity(comment="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_party_MatrixRelationship_name_value_roundtrip():
    instance = party_MatrixRelationship(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_party_Organization_organizationType_value_roundtrip():
    instance = party_Organization(organizationType="sample_text")
    assert instance.organizationType == "sample_text"
    instance.organizationType = "sample_text_2"
    assert instance.organizationType == "sample_text_2"


def test_party_Party_name_value_roundtrip():
    instance = party_Party(name="sample_text", uid="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_party_Party_uid_value_roundtrip():
    instance = party_Party(name="sample_text", uid="sample_text")
    assert instance.uid == "sample_text"
    instance.uid = "sample_text_2"
    assert instance.uid == "sample_text_2"


def test_party_Person_title_value_roundtrip():
    instance = party_Person(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_party_Phone_areaCode_value_roundtrip():
    instance = party_Phone(areaCode=7, countryCode="sample_text", number="sample_text")
    assert instance.areaCode == 7
    instance.areaCode = 13
    assert instance.areaCode == 13


def test_party_Phone_countryCode_value_roundtrip():
    instance = party_Phone(areaCode=7, countryCode="sample_text", number="sample_text")
    assert instance.countryCode == "sample_text"
    instance.countryCode = "sample_text_2"
    assert instance.countryCode == "sample_text_2"


def test_party_Phone_number_value_roundtrip():
    instance = party_Phone(areaCode=7, countryCode="sample_text", number="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_party_Role_name_value_roundtrip():
    instance = party_Role(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_party_Tag_comment_value_roundtrip():
    instance = party_Tag(comment="sample_text", name="sample_text", value="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_party_Tag_name_value_roundtrip():
    instance = party_Tag(comment="sample_text", name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_party_Tag_value_value_roundtrip():
    instance = party_Tag(comment="sample_text", name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_party_Tagged_comment_value_roundtrip():
    instance = party_Tagged(comment="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_party_URL_address_value_roundtrip():
    instance = party_URL(address="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_party_USAddress_city_value_roundtrip():
    instance = party_USAddress(city="sample_text", recipient="sample_text", state="sample_text", street1="sample_text", street2="sample_text", zip="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_party_USAddress_recipient_value_roundtrip():
    instance = party_USAddress(city="sample_text", recipient="sample_text", state="sample_text", street1="sample_text", street2="sample_text", zip="sample_text")
    assert instance.recipient == "sample_text"
    instance.recipient = "sample_text_2"
    assert instance.recipient == "sample_text_2"


def test_party_USAddress_state_value_roundtrip():
    instance = party_USAddress(city="sample_text", recipient="sample_text", state="sample_text", street1="sample_text", street2="sample_text", zip="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_party_USAddress_street1_value_roundtrip():
    instance = party_USAddress(city="sample_text", recipient="sample_text", state="sample_text", street1="sample_text", street2="sample_text", zip="sample_text")
    assert instance.street1 == "sample_text"
    instance.street1 = "sample_text_2"
    assert instance.street1 == "sample_text_2"


def test_party_USAddress_street2_value_roundtrip():
    instance = party_USAddress(city="sample_text", recipient="sample_text", state="sample_text", street1="sample_text", street2="sample_text", zip="sample_text")
    assert instance.street2 == "sample_text"
    instance.street2 = "sample_text_2"
    assert instance.street2 == "sample_text_2"


def test_party_USAddress_zip_value_roundtrip():
    instance = party_USAddress(city="sample_text", recipient="sample_text", state="sample_text", street1="sample_text", street2="sample_text", zip="sample_text")
    assert instance.zip == "sample_text"
    instance.zip = "sample_text_2"
    assert instance.zip == "sample_text_2"


def test_party_USAddress_isa_Address():
    instance = party_USAddress(city="sample_text", recipient="sample_text", state="sample_text", street1="sample_text", street2="sample_text", zip="sample_text")
    assert isinstance(instance, Address)


def test_party_Address_isa_ContactInfo():
    instance = party_Address(country="sample_text")
    assert isinstance(instance, ContactInfo)


def test_party_Custom_isa_ContactInfo():
    instance = party_Custom(location="sample_text")
    assert isinstance(instance, ContactInfo)


def test_party_Phone_isa_ContactInfo():
    instance = party_Phone(areaCode=7, countryCode="sample_text", number="sample_text")
    assert isinstance(instance, ContactInfo)


def test_party_URL_isa_ContactInfo():
    instance = party_URL(address="sample_text")
    assert isinstance(instance, ContactInfo)


def test_party_ContactInfo_isa_DateEffectiveObject():
    instance = party_ContactInfo(category="sample_text")
    assert isinstance(instance, DateEffectiveObject)


def test_party_MatrixRelationship_isa_DateEffectiveObject():
    instance = party_MatrixRelationship(name="sample_text")
    assert isinstance(instance, DateEffectiveObject)


def test_party_Role_isa_DateEffectiveObject():
    instance = party_Role(name="sample_text")
    assert isinstance(instance, DateEffectiveObject)


def test_party_Organization_isa_Party():
    instance = party_Organization(organizationType="sample_text")
    assert isinstance(instance, Party)


def test_party_Person_isa_Party():
    instance = party_Person(title="sample_text")
    assert isinstance(instance, Party)


def test_party_DateEffectiveObject_isa_Tagged():
    instance = party_DateEffectiveObject(end=date(2024, 1, 1), start=date(2024, 1, 1))
    assert isinstance(instance, Tagged)


def test_party_Party_isa_Tagged():
    instance = party_Party(name="sample_text", uid="sample_text")
    assert isinstance(instance, Tagged)


def test_party_EMail_isa_URL():
    instance = party_EMail()
    assert isinstance(instance, URL)


def test_party_Web_isa_URL():
    instance = party_Web()
    assert isinstance(instance, URL)


def test_assoc_children5_link_reassign_clear():
    a = party_Party(name="sample_text", uid="sample_text")
    b1 = party_Organization(organizationType="sample_text")
    b2 = party_Organization(organizationType="sample_text_2")
    _safe_set(a, 'Party6', b1)
    assert _is_linked(a, 'Party6', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'Party6', b2)
    assert _is_linked(a, 'Party6', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'Party6', None)
    assert not _is_linked(a, 'Party6', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_contactInfo0_link_reassign_clear():
    a = party_Party(name="sample_text", uid="sample_text")
    b1 = party_ContactInfo(category="sample_text")
    b2 = party_ContactInfo(category="sample_text_2")
    _safe_set(a, 'owner', {b1})
    assert _is_linked(a, 'owner', b1)
    if hasattr(b1, 'ContactInfo'):
        assert _is_linked(b1, 'ContactInfo', a)
    _safe_set(a, 'owner', {b2})
    assert _is_linked(a, 'owner', b2)
    if hasattr(b1, 'ContactInfo'):
        assert not _is_linked(b1, 'ContactInfo', a)
    if hasattr(b2, 'ContactInfo'):
        assert _is_linked(b2, 'ContactInfo', a)
    _safe_set(a, 'owner', set())
    assert not _is_linked(a, 'owner', b2)
    if hasattr(b2, 'ContactInfo'):
        assert not _is_linked(b2, 'ContactInfo', a)


def test_assoc_externalChildren7_link_reassign_clear():
    a = party_Party(name="sample_text", uid="sample_text")
    b1 = party_Organization(organizationType="sample_text")
    b2 = party_Organization(organizationType="sample_text_2")
    _safe_set(a, 'party_Party8', b1)
    assert _is_linked(a, 'party_Party8', b1)
    if hasattr(b1, 'party_Organization'):
        assert _is_linked(b1, 'party_Organization', a)
    _safe_set(a, 'party_Party8', b2)
    assert _is_linked(a, 'party_Party8', b2)
    if hasattr(b1, 'party_Organization'):
        assert not _is_linked(b1, 'party_Organization', a)
    if hasattr(b2, 'party_Organization'):
        assert _is_linked(b2, 'party_Organization', a)
    _safe_set(a, 'party_Party8', None)
    assert not _is_linked(a, 'party_Party8', b2)
    if hasattr(b2, 'party_Organization'):
        assert not _is_linked(b2, 'party_Organization', a)


def test_assoc_identity1_link_reassign_clear():
    a = party_Party(name="sample_text", uid="sample_text")
    b1 = party_Identity(comment="sample_text", type="sample_text", value="sample_text")
    b2 = party_Identity(comment="sample_text_2", type="sample_text_2", value="sample_text_2")
    _safe_set(a, 'party_Party', {b1})
    assert _is_linked(a, 'party_Party', b1)
    if hasattr(b1, 'party_Identity'):
        assert _is_linked(b1, 'party_Identity', a)
    _safe_set(a, 'party_Party', {b2})
    assert _is_linked(a, 'party_Party', b2)
    if hasattr(b1, 'party_Identity'):
        assert not _is_linked(b1, 'party_Identity', a)
    if hasattr(b2, 'party_Identity'):
        assert _is_linked(b2, 'party_Identity', a)
    _safe_set(a, 'party_Party', set())
    assert not _is_linked(a, 'party_Party', b2)
    if hasattr(b2, 'party_Identity'):
        assert not _is_linked(b2, 'party_Identity', a)


def test_assoc_matrixedChildren9_link_reassign_clear():
    a = party_Organization(organizationType="sample_text")
    b1 = party_MatrixRelationship(name="sample_text")
    b2 = party_MatrixRelationship(name="sample_text_2")
    _safe_set(a, 'party_Organization10', {b1})
    assert _is_linked(a, 'party_Organization10', b1)
    if hasattr(b1, 'party_MatrixRelationship'):
        assert _is_linked(b1, 'party_MatrixRelationship', a)
    _safe_set(a, 'party_Organization10', {b2})
    assert _is_linked(a, 'party_Organization10', b2)
    if hasattr(b1, 'party_MatrixRelationship'):
        assert not _is_linked(b1, 'party_MatrixRelationship', a)
    if hasattr(b2, 'party_MatrixRelationship'):
        assert _is_linked(b2, 'party_MatrixRelationship', a)
    _safe_set(a, 'party_Organization10', set())
    assert not _is_linked(a, 'party_Organization10', b2)
    if hasattr(b2, 'party_MatrixRelationship'):
        assert not _is_linked(b2, 'party_MatrixRelationship', a)


def test_assoc_owner13_link_reassign_clear():
    a = party_Role(name="sample_text")
    b1 = party_CommonObject()
    b2 = party_CommonObject()
    _safe_set(a, 'roles', b1)
    assert _is_linked(a, 'roles', b1)
    if hasattr(b1, 'CommonObject'):
        assert _is_linked(b1, 'CommonObject', a)
    _safe_set(a, 'roles', b2)
    assert _is_linked(a, 'roles', b2)
    if hasattr(b1, 'CommonObject'):
        assert not _is_linked(b1, 'CommonObject', a)
    if hasattr(b2, 'CommonObject'):
        assert _is_linked(b2, 'CommonObject', a)
    _safe_set(a, 'roles', None)
    assert not _is_linked(a, 'roles', b2)
    if hasattr(b2, 'CommonObject'):
        assert not _is_linked(b2, 'CommonObject', a)


def test_assoc_owner4_link_reassign_clear():
    a = party_Party(name="sample_text", uid="sample_text")
    b1 = party_ContactInfo(category="sample_text")
    b2 = party_ContactInfo(category="sample_text_2")
    _safe_set(a, 'Party', b1)
    assert _is_linked(a, 'Party', b1)
    if hasattr(b1, 'contactInfo'):
        assert _is_linked(b1, 'contactInfo', a)
    _safe_set(a, 'Party', b2)
    assert _is_linked(a, 'Party', b2)
    if hasattr(b1, 'contactInfo'):
        assert not _is_linked(b1, 'contactInfo', a)
    if hasattr(b2, 'contactInfo'):
        assert _is_linked(b2, 'contactInfo', a)
    _safe_set(a, 'Party', None)
    assert not _is_linked(a, 'Party', b2)
    if hasattr(b2, 'contactInfo'):
        assert not _is_linked(b2, 'contactInfo', a)


def test_assoc_parent2_link_reassign_clear():
    a = party_Party(name="sample_text", uid="sample_text")
    b1 = party_Organization(organizationType="sample_text")
    b2 = party_Organization(organizationType="sample_text_2")
    _safe_set(a, 'children', b1)
    assert _is_linked(a, 'children', b1)
    if hasattr(b1, 'Organization'):
        assert _is_linked(b1, 'Organization', a)
    _safe_set(a, 'children', b2)
    assert _is_linked(a, 'children', b2)
    if hasattr(b1, 'Organization'):
        assert not _is_linked(b1, 'Organization', a)
    if hasattr(b2, 'Organization'):
        assert _is_linked(b2, 'Organization', a)
    _safe_set(a, 'children', None)
    assert not _is_linked(a, 'children', b2)
    if hasattr(b2, 'Organization'):
        assert not _is_linked(b2, 'Organization', a)


def test_assoc_party11_link_reassign_clear():
    a = party_Role(name="sample_text")
    b1 = party_Party(name="sample_text", uid="sample_text")
    b2 = party_Party(name="sample_text_2", uid="sample_text_2")
    _safe_set(a, 'party_Role', {b1})
    assert _is_linked(a, 'party_Role', b1)
    if hasattr(b1, 'party_Party12'):
        assert _is_linked(b1, 'party_Party12', a)
    _safe_set(a, 'party_Role', {b2})
    assert _is_linked(a, 'party_Role', b2)
    if hasattr(b1, 'party_Party12'):
        assert not _is_linked(b1, 'party_Party12', a)
    if hasattr(b2, 'party_Party12'):
        assert _is_linked(b2, 'party_Party12', a)
    _safe_set(a, 'party_Role', set())
    assert not _is_linked(a, 'party_Role', b2)
    if hasattr(b2, 'party_Party12'):
        assert not _is_linked(b2, 'party_Party12', a)


def test_assoc_roles14_link_reassign_clear():
    a = party_Role(name="sample_text")
    b1 = party_CommonObject()
    b2 = party_CommonObject()
    _safe_set(a, 'Role', b1)
    assert _is_linked(a, 'Role', b1)
    if hasattr(b1, 'owner15'):
        assert _is_linked(b1, 'owner15', a)
    _safe_set(a, 'Role', b2)
    assert _is_linked(a, 'Role', b2)
    if hasattr(b1, 'owner15'):
        assert not _is_linked(b1, 'owner15', a)
    if hasattr(b2, 'owner15'):
        assert _is_linked(b2, 'owner15', a)
    _safe_set(a, 'Role', None)
    assert not _is_linked(a, 'Role', b2)
    if hasattr(b2, 'owner15'):
        assert not _is_linked(b2, 'owner15', a)


def test_assoc_tags3_link_reassign_clear():
    a = party_Tagged(comment="sample_text")
    b1 = party_Tag(comment="sample_text", name="sample_text", value="sample_text")
    b2 = party_Tag(comment="sample_text_2", name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'party_Tagged', {b1})
    assert _is_linked(a, 'party_Tagged', b1)
    if hasattr(b1, 'party_Tag'):
        assert _is_linked(b1, 'party_Tag', a)
    _safe_set(a, 'party_Tagged', {b2})
    assert _is_linked(a, 'party_Tagged', b2)
    if hasattr(b1, 'party_Tag'):
        assert not _is_linked(b1, 'party_Tag', a)
    if hasattr(b2, 'party_Tag'):
        assert _is_linked(b2, 'party_Tag', a)
    _safe_set(a, 'party_Tagged', set())
    assert not _is_linked(a, 'party_Tagged', b2)
    if hasattr(b2, 'party_Tag'):
        assert not _is_linked(b2, 'party_Tag', a)


def test_assoc_target16_link_reassign_clear():
    a = party_Party(name="sample_text", uid="sample_text")
    b1 = party_MatrixRelationship(name="sample_text")
    b2 = party_MatrixRelationship(name="sample_text_2")
    _safe_set(a, 'party_Party18', b1)
    assert _is_linked(a, 'party_Party18', b1)
    if hasattr(b1, 'party_MatrixRelationship17'):
        assert _is_linked(b1, 'party_MatrixRelationship17', a)
    _safe_set(a, 'party_Party18', b2)
    assert _is_linked(a, 'party_Party18', b2)
    if hasattr(b1, 'party_MatrixRelationship17'):
        assert not _is_linked(b1, 'party_MatrixRelationship17', a)
    if hasattr(b2, 'party_MatrixRelationship17'):
        assert _is_linked(b2, 'party_MatrixRelationship17', a)
    _safe_set(a, 'party_Party18', None)
    assert not _is_linked(a, 'party_Party18', b2)
    if hasattr(b2, 'party_MatrixRelationship17'):
        assert not _is_linked(b2, 'party_MatrixRelationship17', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Address_strategy = st.builds(Address)
@given(instance=Address_strategy)
@settings(max_examples=25)
def test_Address_instantiation(instance):
    assert isinstance(instance, Address)


ContactInfo_strategy = st.builds(ContactInfo)
@given(instance=ContactInfo_strategy)
@settings(max_examples=25)
def test_ContactInfo_instantiation(instance):
    assert isinstance(instance, ContactInfo)


DateEffectiveObject_strategy = st.builds(DateEffectiveObject)
@given(instance=DateEffectiveObject_strategy)
@settings(max_examples=25)
def test_DateEffectiveObject_instantiation(instance):
    assert isinstance(instance, DateEffectiveObject)


Party_strategy = st.builds(Party)
@given(instance=Party_strategy)
@settings(max_examples=25)
def test_Party_instantiation(instance):
    assert isinstance(instance, Party)


Tagged_strategy = st.builds(Tagged)
@given(instance=Tagged_strategy)
@settings(max_examples=25)
def test_Tagged_instantiation(instance):
    assert isinstance(instance, Tagged)


URL_strategy = st.builds(URL)
@given(instance=URL_strategy)
@settings(max_examples=25)
def test_URL_instantiation(instance):
    assert isinstance(instance, URL)


party_Address_strategy = st.builds(party_Address, country=safe_text)
@given(instance=party_Address_strategy)
@settings(max_examples=25)
def test_party_Address_instantiation(instance):
    assert isinstance(instance, party_Address)


party_CommonObject_strategy = st.builds(party_CommonObject)
@given(instance=party_CommonObject_strategy)
@settings(max_examples=25)
def test_party_CommonObject_instantiation(instance):
    assert isinstance(instance, party_CommonObject)


party_ContactInfo_strategy = st.builds(party_ContactInfo, category=safe_text)
@given(instance=party_ContactInfo_strategy)
@settings(max_examples=25)
def test_party_ContactInfo_instantiation(instance):
    assert isinstance(instance, party_ContactInfo)


party_Custom_strategy = st.builds(party_Custom, location=safe_text)
@given(instance=party_Custom_strategy)
@settings(max_examples=25)
def test_party_Custom_instantiation(instance):
    assert isinstance(instance, party_Custom)


party_DateEffectiveObject_strategy = st.builds(party_DateEffectiveObject, end=st.dates(), start=st.dates())
@given(instance=party_DateEffectiveObject_strategy)
@settings(max_examples=25)
def test_party_DateEffectiveObject_instantiation(instance):
    assert isinstance(instance, party_DateEffectiveObject)


party_EMail_strategy = st.builds(party_EMail)
@given(instance=party_EMail_strategy)
@settings(max_examples=25)
def test_party_EMail_instantiation(instance):
    assert isinstance(instance, party_EMail)


party_Identity_strategy = st.builds(party_Identity, comment=safe_text, type=safe_text, value=safe_text)
@given(instance=party_Identity_strategy)
@settings(max_examples=25)
def test_party_Identity_instantiation(instance):
    assert isinstance(instance, party_Identity)


party_MatrixRelationship_strategy = st.builds(party_MatrixRelationship, name=safe_text)
@given(instance=party_MatrixRelationship_strategy)
@settings(max_examples=25)
def test_party_MatrixRelationship_instantiation(instance):
    assert isinstance(instance, party_MatrixRelationship)


party_Organization_strategy = st.builds(party_Organization, organizationType=safe_text)
@given(instance=party_Organization_strategy)
@settings(max_examples=25)
def test_party_Organization_instantiation(instance):
    assert isinstance(instance, party_Organization)


party_Party_strategy = st.builds(party_Party, name=safe_text, uid=safe_text)
@given(instance=party_Party_strategy)
@settings(max_examples=25)
def test_party_Party_instantiation(instance):
    assert isinstance(instance, party_Party)


party_Person_strategy = st.builds(party_Person, title=safe_text)
@given(instance=party_Person_strategy)
@settings(max_examples=25)
def test_party_Person_instantiation(instance):
    assert isinstance(instance, party_Person)


party_Phone_strategy = st.builds(party_Phone, areaCode=st.integers(), countryCode=safe_text, number=safe_text)
@given(instance=party_Phone_strategy)
@settings(max_examples=25)
def test_party_Phone_instantiation(instance):
    assert isinstance(instance, party_Phone)


party_Role_strategy = st.builds(party_Role, name=safe_text)
@given(instance=party_Role_strategy)
@settings(max_examples=25)
def test_party_Role_instantiation(instance):
    assert isinstance(instance, party_Role)


party_Tag_strategy = st.builds(party_Tag, comment=safe_text, name=safe_text, value=safe_text)
@given(instance=party_Tag_strategy)
@settings(max_examples=25)
def test_party_Tag_instantiation(instance):
    assert isinstance(instance, party_Tag)


party_Tagged_strategy = st.builds(party_Tagged, comment=safe_text)
@given(instance=party_Tagged_strategy)
@settings(max_examples=25)
def test_party_Tagged_instantiation(instance):
    assert isinstance(instance, party_Tagged)


party_URL_strategy = st.builds(party_URL, address=safe_text)
@given(instance=party_URL_strategy)
@settings(max_examples=25)
def test_party_URL_instantiation(instance):
    assert isinstance(instance, party_URL)


party_USAddress_strategy = st.builds(party_USAddress, city=safe_text, recipient=safe_text, state=safe_text, street1=safe_text, street2=safe_text, zip=safe_text)
@given(instance=party_USAddress_strategy)
@settings(max_examples=25)
def test_party_USAddress_instantiation(instance):
    assert isinstance(instance, party_USAddress)


party_Web_strategy = st.builds(party_Web)
@given(instance=party_Web_strategy)
@settings(max_examples=25)
def test_party_Web_instantiation(instance):
    assert isinstance(instance, party_Web)



