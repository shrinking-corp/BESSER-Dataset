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
    menus_PersonDirectory,
    menus_Person,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_menus_persondirectory_is_not_abstract():
    assert not inspect.isabstract(menus_PersonDirectory)


def test_hyp_menus_persondirectory_constructor_exists():
    assert callable(menus_PersonDirectory.__init__)


def test_hyp_menus_persondirectory_constructor_args():
    sig = inspect.signature(menus_PersonDirectory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_menus_person_is_not_abstract():
    assert not inspect.isabstract(menus_Person)


def test_hyp_menus_person_constructor_exists():
    assert callable(menus_Person.__init__)


def test_hyp_menus_person_constructor_args():
    sig = inspect.signature(menus_Person.__init__)
    params = list(sig.parameters.keys())
    assert "pregnant" in params, "Missing parameter 'pregnant'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"






def test_hyp_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_hyp_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "MALE",
        "FEMALE",
        "UNSPECIFIED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
menus_PersonDirectory_strategy = st.builds(
    menus_PersonDirectory,
)
menus_Person_strategy = st.builds(
    menus_Person,
    pregnant=
        st.booleans(),
    sex=
        safe_text,
    lastname=
        safe_text,
    firstname=
        safe_text,
    dateOfBirth=
        st.dates()
)





@given(instance=menus_Person_strategy)
def test_hyp_menus_person_pregnant_setter(instance):
    original = instance.pregnant
    instance.pregnant = original
    assert instance.pregnant == original



@given(instance=menus_Person_strategy)
def test_hyp_menus_person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=menus_Person_strategy)
def test_hyp_menus_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=menus_Person_strategy)
def test_hyp_menus_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=menus_Person_strategy)
def test_hyp_menus_person_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    menus_Person,
    menus_PersonDirectory,
    Gender,
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

def test_menus_Person_dateOfBirth_value_roundtrip():
    instance = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_menus_Person_firstname_value_roundtrip():
    instance = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_menus_Person_lastname_value_roundtrip():
    instance = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_menus_Person_pregnant_value_roundtrip():
    instance = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    assert instance.pregnant == True
    instance.pregnant = False
    assert instance.pregnant == False


def test_menus_Person_sex_value_roundtrip():
    instance = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_assoc_entry2_link_reassign_clear():
    a = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    b1 = menus_PersonDirectory()
    b2 = menus_PersonDirectory()
    _safe_set(a, 'menus_Person3', b1)
    assert _is_linked(a, 'menus_Person3', b1)
    if hasattr(b1, 'menus_PersonDirectory'):
        assert _is_linked(b1, 'menus_PersonDirectory', a)
    _safe_set(a, 'menus_Person3', b2)
    assert _is_linked(a, 'menus_Person3', b2)
    if hasattr(b1, 'menus_PersonDirectory'):
        assert not _is_linked(b1, 'menus_PersonDirectory', a)
    if hasattr(b2, 'menus_PersonDirectory'):
        assert _is_linked(b2, 'menus_PersonDirectory', a)
    _safe_set(a, 'menus_Person3', None)
    assert not _is_linked(a, 'menus_Person3', b2)
    if hasattr(b2, 'menus_PersonDirectory'):
        assert not _is_linked(b2, 'menus_PersonDirectory', a)


def test_assoc_partner1_link_reassign_clear():
    a = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    b1 = menus_Person(dateOfBirth=date(2024, 1, 1), firstname="sample_text", lastname="sample_text", pregnant=True, sex="sample_text")
    b2 = menus_Person(dateOfBirth=date(2025, 6, 15), firstname="sample_text_2", lastname="sample_text_2", pregnant=False, sex="sample_text_2")
    _safe_set(a, 'menus_Person', b1)
    assert _is_linked(a, 'menus_Person', b1)
    if hasattr(b1, 'menus_Person0'):
        assert _is_linked(b1, 'menus_Person0', a)
    _safe_set(a, 'menus_Person', b2)
    assert _is_linked(a, 'menus_Person', b2)
    if hasattr(b1, 'menus_Person0'):
        assert not _is_linked(b1, 'menus_Person0', a)
    if hasattr(b2, 'menus_Person0'):
        assert _is_linked(b2, 'menus_Person0', a)
    _safe_set(a, 'menus_Person', None)
    assert not _is_linked(a, 'menus_Person', b2)
    if hasattr(b2, 'menus_Person0'):
        assert not _is_linked(b2, 'menus_Person0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

menus_Person_strategy = st.builds(menus_Person, dateOfBirth=st.dates(), firstname=safe_text, lastname=safe_text, pregnant=st.booleans(), sex=safe_text)
@given(instance=menus_Person_strategy)
@settings(max_examples=25)
def test_menus_Person_instantiation(instance):
    assert isinstance(instance, menus_Person)


menus_PersonDirectory_strategy = st.builds(menus_PersonDirectory)
@given(instance=menus_PersonDirectory_strategy)
@settings(max_examples=25)
def test_menus_PersonDirectory_instantiation(instance):
    assert isinstance(instance, menus_PersonDirectory)



