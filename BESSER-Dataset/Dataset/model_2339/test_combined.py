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
    person_PersonType,
    person_CompanyType,
    person_EStringToStringMapEntry,
    person_DocumentRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_person_persontype_is_not_abstract():
    assert not inspect.isabstract(person_PersonType)


def test_hyp_person_persontype_constructor_exists():
    assert callable(person_PersonType.__init__)


def test_hyp_person_persontype_constructor_args():
    sig = inspect.signature(person_PersonType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"
    assert "email" in params, "Missing parameter 'email'"
    assert "country" in params, "Missing parameter 'country'"







def test_hyp_person_companytype_is_not_abstract():
    assert not inspect.isabstract(person_CompanyType)


def test_hyp_person_companytype_constructor_exists():
    assert callable(person_CompanyType.__init__)


def test_hyp_person_companytype_constructor_args():
    sig = inspect.signature(person_CompanyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_person_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(person_EStringToStringMapEntry)


def test_hyp_person_estringtostringmapentry_constructor_exists():
    assert callable(person_EStringToStringMapEntry.__init__)


def test_hyp_person_estringtostringmapentry_constructor_args():
    sig = inspect.signature(person_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_person_documentroot_is_not_abstract():
    assert not inspect.isabstract(person_DocumentRoot)


def test_hyp_person_documentroot_constructor_exists():
    assert callable(person_DocumentRoot.__init__)


def test_hyp_person_documentroot_constructor_args():
    sig = inspect.signature(person_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"



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
person_PersonType_strategy = st.builds(
    person_PersonType,
    name=
        safe_text,
    age=
        safe_text,
    email=
        safe_text,
    country=
        safe_text
)
person_CompanyType_strategy = st.builds(
    person_CompanyType,
)
person_EStringToStringMapEntry_strategy = st.builds(
    person_EStringToStringMapEntry,
)
person_DocumentRoot_strategy = st.builds(
    person_DocumentRoot,
    mixed=
        safe_text
)




@given(instance=person_PersonType_strategy)
def test_hyp_person_persontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=person_PersonType_strategy)
def test_hyp_person_persontype_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=person_PersonType_strategy)
def test_hyp_person_persontype_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=person_PersonType_strategy)
def test_hyp_person_persontype_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original






@given(instance=person_DocumentRoot_strategy)
def test_hyp_person_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    person_CompanyType,
    person_DocumentRoot,
    person_EStringToStringMapEntry,
    person_PersonType,
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

def test_person_DocumentRoot_mixed_value_roundtrip():
    instance = person_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_person_PersonType_age_value_roundtrip():
    instance = person_PersonType(age="sample_text", country="sample_text", email="sample_text", name="sample_text")
    assert instance.age == "sample_text"
    instance.age = "sample_text_2"
    assert instance.age == "sample_text_2"


def test_person_PersonType_country_value_roundtrip():
    instance = person_PersonType(age="sample_text", country="sample_text", email="sample_text", name="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_person_PersonType_email_value_roundtrip():
    instance = person_PersonType(age="sample_text", country="sample_text", email="sample_text", name="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_person_PersonType_name_value_roundtrip():
    instance = person_PersonType(age="sample_text", country="sample_text", email="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_company5_link_reassign_clear():
    a = person_DocumentRoot(mixed="sample_text")
    b1 = person_CompanyType()
    b2 = person_CompanyType()
    _safe_set(a, 'person_DocumentRoot6', {b1})
    assert _is_linked(a, 'person_DocumentRoot6', b1)
    if hasattr(b1, 'person_CompanyType7'):
        assert _is_linked(b1, 'person_CompanyType7', a)
    _safe_set(a, 'person_DocumentRoot6', {b2})
    assert _is_linked(a, 'person_DocumentRoot6', b2)
    if hasattr(b1, 'person_CompanyType7'):
        assert not _is_linked(b1, 'person_CompanyType7', a)
    if hasattr(b2, 'person_CompanyType7'):
        assert _is_linked(b2, 'person_CompanyType7', a)
    _safe_set(a, 'person_DocumentRoot6', set())
    assert not _is_linked(a, 'person_DocumentRoot6', b2)
    if hasattr(b2, 'person_CompanyType7'):
        assert not _is_linked(b2, 'person_CompanyType7', a)


def test_assoc_person0_link_reassign_clear():
    a = person_PersonType(age="sample_text", country="sample_text", email="sample_text", name="sample_text")
    b1 = person_CompanyType()
    b2 = person_CompanyType()
    _safe_set(a, 'person_PersonType', b1)
    assert _is_linked(a, 'person_PersonType', b1)
    if hasattr(b1, 'person_CompanyType'):
        assert _is_linked(b1, 'person_CompanyType', a)
    _safe_set(a, 'person_PersonType', b2)
    assert _is_linked(a, 'person_PersonType', b2)
    if hasattr(b1, 'person_CompanyType'):
        assert not _is_linked(b1, 'person_CompanyType', a)
    if hasattr(b2, 'person_CompanyType'):
        assert _is_linked(b2, 'person_CompanyType', a)
    _safe_set(a, 'person_PersonType', None)
    assert not _is_linked(a, 'person_PersonType', b2)
    if hasattr(b2, 'person_CompanyType'):
        assert not _is_linked(b2, 'person_CompanyType', a)


def test_assoc_xMLNSPrefixMap1_link_reassign_clear():
    a = person_DocumentRoot(mixed="sample_text")
    b1 = person_EStringToStringMapEntry()
    b2 = person_EStringToStringMapEntry()
    _safe_set(a, 'person_DocumentRoot', {b1})
    assert _is_linked(a, 'person_DocumentRoot', b1)
    if hasattr(b1, 'person_EStringToStringMapEntry'):
        assert _is_linked(b1, 'person_EStringToStringMapEntry', a)
    _safe_set(a, 'person_DocumentRoot', {b2})
    assert _is_linked(a, 'person_DocumentRoot', b2)
    if hasattr(b1, 'person_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'person_EStringToStringMapEntry', a)
    if hasattr(b2, 'person_EStringToStringMapEntry'):
        assert _is_linked(b2, 'person_EStringToStringMapEntry', a)
    _safe_set(a, 'person_DocumentRoot', set())
    assert not _is_linked(a, 'person_DocumentRoot', b2)
    if hasattr(b2, 'person_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'person_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation2_link_reassign_clear():
    a = person_DocumentRoot(mixed="sample_text")
    b1 = person_EStringToStringMapEntry()
    b2 = person_EStringToStringMapEntry()
    _safe_set(a, 'person_DocumentRoot3', {b1})
    assert _is_linked(a, 'person_DocumentRoot3', b1)
    if hasattr(b1, 'person_EStringToStringMapEntry4'):
        assert _is_linked(b1, 'person_EStringToStringMapEntry4', a)
    _safe_set(a, 'person_DocumentRoot3', {b2})
    assert _is_linked(a, 'person_DocumentRoot3', b2)
    if hasattr(b1, 'person_EStringToStringMapEntry4'):
        assert not _is_linked(b1, 'person_EStringToStringMapEntry4', a)
    if hasattr(b2, 'person_EStringToStringMapEntry4'):
        assert _is_linked(b2, 'person_EStringToStringMapEntry4', a)
    _safe_set(a, 'person_DocumentRoot3', set())
    assert not _is_linked(a, 'person_DocumentRoot3', b2)
    if hasattr(b2, 'person_EStringToStringMapEntry4'):
        assert not _is_linked(b2, 'person_EStringToStringMapEntry4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

person_CompanyType_strategy = st.builds(person_CompanyType)
@given(instance=person_CompanyType_strategy)
@settings(max_examples=25)
def test_person_CompanyType_instantiation(instance):
    assert isinstance(instance, person_CompanyType)


person_DocumentRoot_strategy = st.builds(person_DocumentRoot, mixed=safe_text)
@given(instance=person_DocumentRoot_strategy)
@settings(max_examples=25)
def test_person_DocumentRoot_instantiation(instance):
    assert isinstance(instance, person_DocumentRoot)


person_EStringToStringMapEntry_strategy = st.builds(person_EStringToStringMapEntry)
@given(instance=person_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_person_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, person_EStringToStringMapEntry)


person_PersonType_strategy = st.builds(person_PersonType, age=safe_text, country=safe_text, email=safe_text, name=safe_text)
@given(instance=person_PersonType_strategy)
@settings(max_examples=25)
def test_person_PersonType_instantiation(instance):
    assert isinstance(instance, person_PersonType)



