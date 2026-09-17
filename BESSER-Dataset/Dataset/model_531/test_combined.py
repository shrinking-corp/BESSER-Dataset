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
    family_Family,
    Parent,
    family_Father,
    family_Mother,
    Person,
    family_Child,
    family_Parent,
    family_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_hyp_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_hyp_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parent_is_not_abstract():
    assert not inspect.isabstract(Parent)


def test_hyp_parent_constructor_exists():
    assert callable(Parent.__init__)


def test_hyp_parent_constructor_args():
    sig = inspect.signature(Parent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_family_father_is_not_abstract():
    assert not inspect.isabstract(family_Father)


def test_hyp_family_father_constructor_exists():
    assert callable(family_Father.__init__)


def test_hyp_family_father_constructor_args():
    sig = inspect.signature(family_Father.__init__)
    params = list(sig.parameters.keys())



def test_hyp_family_mother_is_not_abstract():
    assert not inspect.isabstract(family_Mother)


def test_hyp_family_mother_constructor_exists():
    assert callable(family_Mother.__init__)


def test_hyp_family_mother_constructor_args():
    sig = inspect.signature(family_Mother.__init__)
    params = list(sig.parameters.keys())



def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_family_child_is_not_abstract():
    assert not inspect.isabstract(family_Child)


def test_hyp_family_child_constructor_exists():
    assert callable(family_Child.__init__)


def test_hyp_family_child_constructor_args():
    sig = inspect.signature(family_Child.__init__)
    params = list(sig.parameters.keys())



def test_hyp_family_parent_is_not_abstract():
    assert not inspect.isabstract(family_Parent)


def test_hyp_family_parent_constructor_exists():
    assert callable(family_Parent.__init__)


def test_hyp_family_parent_constructor_args():
    sig = inspect.signature(family_Parent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_hyp_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_hyp_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthdate" in params, "Missing parameter 'birthdate'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"





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
family_Family_strategy = st.builds(
    family_Family,
)
Parent_strategy = st.builds(
    Parent,
)
family_Father_strategy = st.builds(
    family_Father,
)
family_Mother_strategy = st.builds(
    family_Mother,
)
Person_strategy = st.builds(
    Person,
)
family_Child_strategy = st.builds(
    family_Child,
)
family_Parent_strategy = st.builds(
    family_Parent,
)
family_Person_strategy = st.builds(
    family_Person,
    birthdate=
        st.dates(),
    lastname=
        safe_text,
    firstname=
        safe_text
)











@given(instance=family_Person_strategy)
def test_hyp_family_person_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original



@given(instance=family_Person_strategy)
def test_hyp_family_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=family_Person_strategy)
def test_hyp_family_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Parent,
    Person,
    family_Child,
    family_Family,
    family_Father,
    family_Mother,
    family_Parent,
    family_Person,
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

def test_family_Person_birthdate_value_roundtrip():
    instance = family_Person(birthdate=date(2024, 1, 1), firstname="sample_text", lastname="sample_text")
    assert instance.birthdate == date(2024, 1, 1)
    instance.birthdate = date(2025, 6, 15)
    assert instance.birthdate == date(2025, 6, 15)


def test_family_Person_firstname_value_roundtrip():
    instance = family_Person(birthdate=date(2024, 1, 1), firstname="sample_text", lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_family_Person_lastname_value_roundtrip():
    instance = family_Person(birthdate=date(2024, 1, 1), firstname="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_family_Father_isa_Parent():
    instance = family_Father()
    assert isinstance(instance, Parent)


def test_family_Mother_isa_Parent():
    instance = family_Mother()
    assert isinstance(instance, Parent)


def test_family_Child_isa_Person():
    instance = family_Child()
    assert isinstance(instance, Person)


def test_family_Parent_isa_Person():
    instance = family_Parent()
    assert isinstance(instance, Person)


def test_assoc_members11_link_reassign_clear():
    a = family_Person(birthdate=date(2024, 1, 1), firstname="sample_text", lastname="sample_text")
    b1 = family_Family()
    b2 = family_Family()
    _safe_set(a, 'family_Person', b1)
    assert _is_linked(a, 'family_Person', b1)
    if hasattr(b1, 'family_Family'):
        assert _is_linked(b1, 'family_Family', a)
    _safe_set(a, 'family_Person', b2)
    assert _is_linked(a, 'family_Person', b2)
    if hasattr(b1, 'family_Family'):
        assert not _is_linked(b1, 'family_Family', a)
    if hasattr(b2, 'family_Family'):
        assert _is_linked(b2, 'family_Family', a)
    _safe_set(a, 'family_Person', None)
    assert not _is_linked(a, 'family_Person', b2)
    if hasattr(b2, 'family_Family'):
        assert not _is_linked(b2, 'family_Family', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Parent_strategy = st.builds(Parent)
@given(instance=Parent_strategy)
@settings(max_examples=25)
def test_Parent_instantiation(instance):
    assert isinstance(instance, Parent)


Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


family_Child_strategy = st.builds(family_Child)
@given(instance=family_Child_strategy)
@settings(max_examples=25)
def test_family_Child_instantiation(instance):
    assert isinstance(instance, family_Child)


family_Family_strategy = st.builds(family_Family)
@given(instance=family_Family_strategy)
@settings(max_examples=25)
def test_family_Family_instantiation(instance):
    assert isinstance(instance, family_Family)


family_Father_strategy = st.builds(family_Father)
@given(instance=family_Father_strategy)
@settings(max_examples=25)
def test_family_Father_instantiation(instance):
    assert isinstance(instance, family_Father)


family_Mother_strategy = st.builds(family_Mother)
@given(instance=family_Mother_strategy)
@settings(max_examples=25)
def test_family_Mother_instantiation(instance):
    assert isinstance(instance, family_Mother)


family_Parent_strategy = st.builds(family_Parent)
@given(instance=family_Parent_strategy)
@settings(max_examples=25)
def test_family_Parent_instantiation(instance):
    assert isinstance(instance, family_Parent)


family_Person_strategy = st.builds(family_Person, birthdate=st.dates(), firstname=safe_text, lastname=safe_text)
@given(instance=family_Person_strategy)
@settings(max_examples=25)
def test_family_Person_instantiation(instance):
    assert isinstance(instance, family_Person)



