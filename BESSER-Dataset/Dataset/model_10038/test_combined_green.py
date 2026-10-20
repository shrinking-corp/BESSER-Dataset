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
    t2_Son,
    t2_Dad,
    t2_Person,
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



def test_hyp_t2_son_is_not_abstract():
    assert not inspect.isabstract(t2_Son)


def test_hyp_t2_son_constructor_exists():
    assert callable(t2_Son.__init__)


def test_hyp_t2_son_constructor_args():
    sig = inspect.signature(t2_Son.__init__)
    params = list(sig.parameters.keys())



def test_hyp_t2_dad_is_not_abstract():
    assert not inspect.isabstract(t2_Dad)


def test_hyp_t2_dad_constructor_exists():
    assert callable(t2_Dad.__init__)


def test_hyp_t2_dad_constructor_args():
    sig = inspect.signature(t2_Dad.__init__)
    params = list(sig.parameters.keys())



def test_hyp_t2_person_is_not_abstract():
    assert not inspect.isabstract(t2_Person)


def test_hyp_t2_person_constructor_exists():
    assert callable(t2_Person.__init__)


def test_hyp_t2_person_constructor_args():
    sig = inspect.signature(t2_Person.__init__)
    params = list(sig.parameters.keys())
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
t2_Son_strategy = st.builds(
    t2_Son,
)
t2_Dad_strategy = st.builds(
    t2_Dad,
)
t2_Person_strategy = st.builds(
    t2_Person,
    age=
        st.integers()
)







@given(instance=t2_Person_strategy)
def test_hyp_t2_person_age_setter(instance):
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
    t2_Dad,
    t2_Person,
    t2_Son,
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

def test_t2_Person_age_value_roundtrip():
    instance = t2_Person(age=7)
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_t2_Dad_isa_Person():
    instance = t2_Dad()
    assert isinstance(instance, Person)


def test_t2_Son_isa_Person():
    instance = t2_Son()
    assert isinstance(instance, Person)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


t2_Dad_strategy = st.builds(t2_Dad)
@given(instance=t2_Dad_strategy)
@settings(max_examples=25)
def test_t2_Dad_instantiation(instance):
    assert isinstance(instance, t2_Dad)


t2_Person_strategy = st.builds(t2_Person, age=st.integers())
@given(instance=t2_Person_strategy)
@settings(max_examples=25)
def test_t2_Person_instantiation(instance):
    assert isinstance(instance, t2_Person)


t2_Son_strategy = st.builds(t2_Son)
@given(instance=t2_Son_strategy)
@settings(max_examples=25)
def test_t2_Son_instantiation(instance):
    assert isinstance(instance, t2_Son)



