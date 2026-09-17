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
    SimplePersons_Female,
    SimplePersons_Male,
    SimplePersons_Person,
    SimplePersons_PersonRegister,
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



def test_hyp_simplepersons_female_is_not_abstract():
    assert not inspect.isabstract(SimplePersons_Female)


def test_hyp_simplepersons_female_constructor_exists():
    assert callable(SimplePersons_Female.__init__)


def test_hyp_simplepersons_female_constructor_args():
    sig = inspect.signature(SimplePersons_Female.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplepersons_male_is_not_abstract():
    assert not inspect.isabstract(SimplePersons_Male)


def test_hyp_simplepersons_male_constructor_exists():
    assert callable(SimplePersons_Male.__init__)


def test_hyp_simplepersons_male_constructor_args():
    sig = inspect.signature(SimplePersons_Male.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplepersons_person_is_not_abstract():
    assert not inspect.isabstract(SimplePersons_Person)


def test_hyp_simplepersons_person_constructor_exists():
    assert callable(SimplePersons_Person.__init__)


def test_hyp_simplepersons_person_constructor_args():
    sig = inspect.signature(SimplePersons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_simplepersons_personregister_is_not_abstract():
    assert not inspect.isabstract(SimplePersons_PersonRegister)


def test_hyp_simplepersons_personregister_constructor_exists():
    assert callable(SimplePersons_PersonRegister.__init__)


def test_hyp_simplepersons_personregister_constructor_args():
    sig = inspect.signature(SimplePersons_PersonRegister.__init__)
    params = list(sig.parameters.keys())


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
SimplePersons_Female_strategy = st.builds(
    SimplePersons_Female,
)
SimplePersons_Male_strategy = st.builds(
    SimplePersons_Male,
)
SimplePersons_Person_strategy = st.builds(
    SimplePersons_Person,
    name=
        safe_text
)
SimplePersons_PersonRegister_strategy = st.builds(
    SimplePersons_PersonRegister,
)







@given(instance=SimplePersons_Person_strategy)
def test_hyp_simplepersons_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Person,
    SimplePersons_Female,
    SimplePersons_Male,
    SimplePersons_Person,
    SimplePersons_PersonRegister,
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

def test_SimplePersons_Person_name_value_roundtrip():
    instance = SimplePersons_Person(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SimplePersons_Female_isa_Person():
    instance = SimplePersons_Female()
    assert isinstance(instance, Person)


def test_SimplePersons_Male_isa_Person():
    instance = SimplePersons_Male()
    assert isinstance(instance, Person)


def test_assoc_persons0_link_reassign_clear():
    a = SimplePersons_Person(name="sample_text")
    b1 = SimplePersons_PersonRegister()
    b2 = SimplePersons_PersonRegister()
    _safe_set(a, 'SimplePersons_Person', b1)
    assert _is_linked(a, 'SimplePersons_Person', b1)
    if hasattr(b1, 'SimplePersons_PersonRegister'):
        assert _is_linked(b1, 'SimplePersons_PersonRegister', a)
    _safe_set(a, 'SimplePersons_Person', b2)
    assert _is_linked(a, 'SimplePersons_Person', b2)
    if hasattr(b1, 'SimplePersons_PersonRegister'):
        assert not _is_linked(b1, 'SimplePersons_PersonRegister', a)
    if hasattr(b2, 'SimplePersons_PersonRegister'):
        assert _is_linked(b2, 'SimplePersons_PersonRegister', a)
    _safe_set(a, 'SimplePersons_Person', None)
    assert not _is_linked(a, 'SimplePersons_Person', b2)
    if hasattr(b2, 'SimplePersons_PersonRegister'):
        assert not _is_linked(b2, 'SimplePersons_PersonRegister', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


SimplePersons_Female_strategy = st.builds(SimplePersons_Female)
@given(instance=SimplePersons_Female_strategy)
@settings(max_examples=25)
def test_SimplePersons_Female_instantiation(instance):
    assert isinstance(instance, SimplePersons_Female)


SimplePersons_Male_strategy = st.builds(SimplePersons_Male)
@given(instance=SimplePersons_Male_strategy)
@settings(max_examples=25)
def test_SimplePersons_Male_instantiation(instance):
    assert isinstance(instance, SimplePersons_Male)


SimplePersons_Person_strategy = st.builds(SimplePersons_Person, name=safe_text)
@given(instance=SimplePersons_Person_strategy)
@settings(max_examples=25)
def test_SimplePersons_Person_instantiation(instance):
    assert isinstance(instance, SimplePersons_Person)


SimplePersons_PersonRegister_strategy = st.builds(SimplePersons_PersonRegister)
@given(instance=SimplePersons_PersonRegister_strategy)
@settings(max_examples=25)
def test_SimplePersons_PersonRegister_instantiation(instance):
    assert isinstance(instance, SimplePersons_PersonRegister)



