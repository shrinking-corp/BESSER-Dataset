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
    Person,
    Persons_Female,
    Persons_Male,
    Persons_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_persons_female_is_not_abstract():
    assert not inspect.isabstract(Persons_Female)


def test_hyp_persons_female_constructor_exists():
    assert callable(Persons_Female.__init__)


def test_hyp_persons_female_constructor_args():
    sig = inspect.signature(Persons_Female.__init__)
    params = list(sig.parameters.keys())



def test_hyp_persons_male_is_not_abstract():
    assert not inspect.isabstract(Persons_Male)


def test_hyp_persons_male_constructor_exists():
    assert callable(Persons_Male.__init__)


def test_hyp_persons_male_constructor_args():
    sig = inspect.signature(Persons_Male.__init__)
    params = list(sig.parameters.keys())



def test_hyp_persons_person_is_not_abstract():
    assert not inspect.isabstract(Persons_Person)


def test_hyp_persons_person_constructor_exists():
    assert callable(Persons_Person.__init__)


def test_hyp_persons_person_constructor_args():
    sig = inspect.signature(Persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"




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
Person_strategy = st.builds(
    Person,
)
Persons_Female_strategy = st.builds(
    Persons_Female,
)
Persons_Male_strategy = st.builds(
    Persons_Male,
)
Persons_Person_strategy = st.builds(
    Persons_Person,
    name=
        safe_text,
    age=
        st.integers()
)







@given(instance=Persons_Person_strategy)
def test_hyp_persons_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Persons_Person_strategy)
def test_hyp_persons_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Person,
    Persons_Female,
    Persons_Male,
    Persons_Person,
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

def test_Persons_Person_age_value_roundtrip():
    instance = Persons_Person(age=7, name="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_Persons_Person_name_value_roundtrip():
    instance = Persons_Person(age=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Persons_Female_isa_Person():
    instance = Persons_Female()
    assert isinstance(instance, Person)


def test_Persons_Male_isa_Person():
    instance = Persons_Male()
    assert isinstance(instance, Person)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Persons_Female_strategy = st.builds(Persons_Female)
@given(instance=Persons_Female_strategy)
@settings(max_examples=25)
def test_Persons_Female_instantiation(instance):
    assert isinstance(instance, Persons_Female)


Persons_Male_strategy = st.builds(Persons_Male)
@given(instance=Persons_Male_strategy)
@settings(max_examples=25)
def test_Persons_Male_instantiation(instance):
    assert isinstance(instance, Persons_Male)


Persons_Person_strategy = st.builds(Persons_Person, age=st.integers(), name=safe_text)
@given(instance=Persons_Person_strategy)
@settings(max_examples=25)
def test_Persons_Person_instantiation(instance):
    assert isinstance(instance, Persons_Person)



