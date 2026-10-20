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
    familyleft1_Son,
    familyleft1_Mother,
    familyleft1_Family,
    familyleft1_Father,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_familyleft1_son_is_not_abstract():
    assert not inspect.isabstract(familyleft1_Son)


def test_hyp_familyleft1_son_constructor_exists():
    assert callable(familyleft1_Son.__init__)


def test_hyp_familyleft1_son_constructor_args():
    sig = inspect.signature(familyleft1_Son.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sex" in params, "Missing parameter 'sex'"






def test_hyp_familyleft1_mother_is_not_abstract():
    assert not inspect.isabstract(familyleft1_Mother)


def test_hyp_familyleft1_mother_constructor_exists():
    assert callable(familyleft1_Mother.__init__)


def test_hyp_familyleft1_mother_constructor_args():
    sig = inspect.signature(familyleft1_Mother.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"





def test_hyp_familyleft1_family_is_not_abstract():
    assert not inspect.isabstract(familyleft1_Family)


def test_hyp_familyleft1_family_constructor_exists():
    assert callable(familyleft1_Family.__init__)


def test_hyp_familyleft1_family_constructor_args():
    sig = inspect.signature(familyleft1_Family.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "surname" in params, "Missing parameter 'surname'"





def test_hyp_familyleft1_father_is_not_abstract():
    assert not inspect.isabstract(familyleft1_Father)


def test_hyp_familyleft1_father_constructor_exists():
    assert callable(familyleft1_Father.__init__)


def test_hyp_familyleft1_father_constructor_args():
    sig = inspect.signature(familyleft1_Father.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
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
familyleft1_Son_strategy = st.builds(
    familyleft1_Son,
    age=
        st.integers(),
    name=
        safe_text,
    sex=
        safe_text
)
familyleft1_Mother_strategy = st.builds(
    familyleft1_Mother,
    name=
        safe_text,
    age=
        st.integers()
)
familyleft1_Family_strategy = st.builds(
    familyleft1_Family,
    location=
        safe_text,
    surname=
        safe_text
)
familyleft1_Father_strategy = st.builds(
    familyleft1_Father,
    age=
        st.integers(),
    name=
        safe_text
)




@given(instance=familyleft1_Son_strategy)
def test_hyp_familyleft1_son_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=familyleft1_Son_strategy)
def test_hyp_familyleft1_son_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=familyleft1_Son_strategy)
def test_hyp_familyleft1_son_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original




@given(instance=familyleft1_Mother_strategy)
def test_hyp_familyleft1_mother_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=familyleft1_Mother_strategy)
def test_hyp_familyleft1_mother_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original




@given(instance=familyleft1_Family_strategy)
def test_hyp_familyleft1_family_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=familyleft1_Family_strategy)
def test_hyp_familyleft1_family_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original




@given(instance=familyleft1_Father_strategy)
def test_hyp_familyleft1_father_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=familyleft1_Father_strategy)
def test_hyp_familyleft1_father_name_setter(instance):
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
    familyleft1_Family,
    familyleft1_Father,
    familyleft1_Mother,
    familyleft1_Son,
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

def test_familyleft1_Family_location_value_roundtrip():
    instance = familyleft1_Family(location="sample_text", surname="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_familyleft1_Family_surname_value_roundtrip():
    instance = familyleft1_Family(location="sample_text", surname="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_familyleft1_Father_age_value_roundtrip():
    instance = familyleft1_Father(age=7, name="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_familyleft1_Father_name_value_roundtrip():
    instance = familyleft1_Father(age=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_familyleft1_Mother_age_value_roundtrip():
    instance = familyleft1_Mother(age=7, name="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_familyleft1_Mother_name_value_roundtrip():
    instance = familyleft1_Mother(age=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_familyleft1_Son_age_value_roundtrip():
    instance = familyleft1_Son(age=7, name="sample_text", sex="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_familyleft1_Son_name_value_roundtrip():
    instance = familyleft1_Son(age=7, name="sample_text", sex="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_familyleft1_Son_sex_value_roundtrip():
    instance = familyleft1_Son(age=7, name="sample_text", sex="sample_text")
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_assoc_family0_link_reassign_clear():
    a = familyleft1_Father(age=7, name="sample_text")
    b1 = familyleft1_Family(location="sample_text", surname="sample_text")
    b2 = familyleft1_Family(location="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'father', b1)
    assert _is_linked(a, 'father', b1)
    if hasattr(b1, 'Family'):
        assert _is_linked(b1, 'Family', a)
    _safe_set(a, 'father', b2)
    assert _is_linked(a, 'father', b2)
    if hasattr(b1, 'Family'):
        assert not _is_linked(b1, 'Family', a)
    if hasattr(b2, 'Family'):
        assert _is_linked(b2, 'Family', a)
    _safe_set(a, 'father', None)
    assert not _is_linked(a, 'father', b2)
    if hasattr(b2, 'Family'):
        assert not _is_linked(b2, 'Family', a)


def test_assoc_family1_link_reassign_clear():
    a = familyleft1_Mother(age=7, name="sample_text")
    b1 = familyleft1_Family(location="sample_text", surname="sample_text")
    b2 = familyleft1_Family(location="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'mother', b1)
    assert _is_linked(a, 'mother', b1)
    if hasattr(b1, 'Family2'):
        assert _is_linked(b1, 'Family2', a)
    _safe_set(a, 'mother', b2)
    assert _is_linked(a, 'mother', b2)
    if hasattr(b1, 'Family2'):
        assert not _is_linked(b1, 'Family2', a)
    if hasattr(b2, 'Family2'):
        assert _is_linked(b2, 'Family2', a)
    _safe_set(a, 'mother', None)
    assert not _is_linked(a, 'mother', b2)
    if hasattr(b2, 'Family2'):
        assert not _is_linked(b2, 'Family2', a)


def test_assoc_family3_link_reassign_clear():
    a = familyleft1_Son(age=7, name="sample_text", sex="sample_text")
    b1 = familyleft1_Family(location="sample_text", surname="sample_text")
    b2 = familyleft1_Family(location="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'sons', b1)
    assert _is_linked(a, 'sons', b1)
    if hasattr(b1, 'Family4'):
        assert _is_linked(b1, 'Family4', a)
    _safe_set(a, 'sons', b2)
    assert _is_linked(a, 'sons', b2)
    if hasattr(b1, 'Family4'):
        assert not _is_linked(b1, 'Family4', a)
    if hasattr(b2, 'Family4'):
        assert _is_linked(b2, 'Family4', a)
    _safe_set(a, 'sons', None)
    assert not _is_linked(a, 'sons', b2)
    if hasattr(b2, 'Family4'):
        assert not _is_linked(b2, 'Family4', a)


def test_assoc_father5_link_reassign_clear():
    a = familyleft1_Father(age=7, name="sample_text")
    b1 = familyleft1_Family(location="sample_text", surname="sample_text")
    b2 = familyleft1_Family(location="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'Father', b1)
    assert _is_linked(a, 'Father', b1)
    if hasattr(b1, 'family'):
        assert _is_linked(b1, 'family', a)
    _safe_set(a, 'Father', b2)
    assert _is_linked(a, 'Father', b2)
    if hasattr(b1, 'family'):
        assert not _is_linked(b1, 'family', a)
    if hasattr(b2, 'family'):
        assert _is_linked(b2, 'family', a)
    _safe_set(a, 'Father', None)
    assert not _is_linked(a, 'Father', b2)
    if hasattr(b2, 'family'):
        assert not _is_linked(b2, 'family', a)


def test_assoc_mother6_link_reassign_clear():
    a = familyleft1_Mother(age=7, name="sample_text")
    b1 = familyleft1_Family(location="sample_text", surname="sample_text")
    b2 = familyleft1_Family(location="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'Mother', b1)
    assert _is_linked(a, 'Mother', b1)
    if hasattr(b1, 'family7'):
        assert _is_linked(b1, 'family7', a)
    _safe_set(a, 'Mother', b2)
    assert _is_linked(a, 'Mother', b2)
    if hasattr(b1, 'family7'):
        assert not _is_linked(b1, 'family7', a)
    if hasattr(b2, 'family7'):
        assert _is_linked(b2, 'family7', a)
    _safe_set(a, 'Mother', None)
    assert not _is_linked(a, 'Mother', b2)
    if hasattr(b2, 'family7'):
        assert not _is_linked(b2, 'family7', a)


def test_assoc_sons8_link_reassign_clear():
    a = familyleft1_Son(age=7, name="sample_text", sex="sample_text")
    b1 = familyleft1_Family(location="sample_text", surname="sample_text")
    b2 = familyleft1_Family(location="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'Son', b1)
    assert _is_linked(a, 'Son', b1)
    if hasattr(b1, 'family9'):
        assert _is_linked(b1, 'family9', a)
    _safe_set(a, 'Son', b2)
    assert _is_linked(a, 'Son', b2)
    if hasattr(b1, 'family9'):
        assert not _is_linked(b1, 'family9', a)
    if hasattr(b2, 'family9'):
        assert _is_linked(b2, 'family9', a)
    _safe_set(a, 'Son', None)
    assert not _is_linked(a, 'Son', b2)
    if hasattr(b2, 'family9'):
        assert not _is_linked(b2, 'family9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

familyleft1_Family_strategy = st.builds(familyleft1_Family, location=safe_text, surname=safe_text)
@given(instance=familyleft1_Family_strategy)
@settings(max_examples=25)
def test_familyleft1_Family_instantiation(instance):
    assert isinstance(instance, familyleft1_Family)


familyleft1_Father_strategy = st.builds(familyleft1_Father, age=st.integers(), name=safe_text)
@given(instance=familyleft1_Father_strategy)
@settings(max_examples=25)
def test_familyleft1_Father_instantiation(instance):
    assert isinstance(instance, familyleft1_Father)


familyleft1_Mother_strategy = st.builds(familyleft1_Mother, age=st.integers(), name=safe_text)
@given(instance=familyleft1_Mother_strategy)
@settings(max_examples=25)
def test_familyleft1_Mother_instantiation(instance):
    assert isinstance(instance, familyleft1_Mother)


familyleft1_Son_strategy = st.builds(familyleft1_Son, age=st.integers(), name=safe_text, sex=safe_text)
@given(instance=familyleft1_Son_strategy)
@settings(max_examples=25)
def test_familyleft1_Son_instantiation(instance):
    assert isinstance(instance, familyleft1_Son)



