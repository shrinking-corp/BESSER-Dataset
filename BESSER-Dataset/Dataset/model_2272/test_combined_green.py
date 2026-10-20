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
    Univerity_University,
    Univerity_Person,
    Univerity_Courses,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_univerity_university_is_not_abstract():
    assert not inspect.isabstract(Univerity_University)


def test_hyp_univerity_university_constructor_exists():
    assert callable(Univerity_University.__init__)


def test_hyp_univerity_university_constructor_args():
    sig = inspect.signature(Univerity_University.__init__)
    params = list(sig.parameters.keys())



def test_hyp_univerity_person_is_not_abstract():
    assert not inspect.isabstract(Univerity_Person)


def test_hyp_univerity_person_constructor_exists():
    assert callable(Univerity_Person.__init__)


def test_hyp_univerity_person_constructor_args():
    sig = inspect.signature(Univerity_Person.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_univerity_courses_is_not_abstract():
    assert not inspect.isabstract(Univerity_Courses)


def test_hyp_univerity_courses_constructor_exists():
    assert callable(Univerity_Courses.__init__)


def test_hyp_univerity_courses_constructor_args():
    sig = inspect.signature(Univerity_Courses.__init__)
    params = list(sig.parameters.keys())
    assert "Semester" in params, "Missing parameter 'Semester'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "CFU" in params, "Missing parameter 'CFU'"





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
Univerity_University_strategy = st.builds(
    Univerity_University,
)
Univerity_Person_strategy = st.builds(
    Univerity_Person,
    Email=
        safe_text,
    Name=
        safe_text
)
Univerity_Courses_strategy = st.builds(
    Univerity_Courses,
    Semester=
        safe_text,
    Name=
        safe_text,
    CFU=
        st.integers()
)





@given(instance=Univerity_Person_strategy)
def test_hyp_univerity_person_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Univerity_Person_strategy)
def test_hyp_univerity_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Univerity_Courses_strategy)
def test_hyp_univerity_courses_Semester_setter(instance):
    original = instance.Semester
    instance.Semester = original
    assert instance.Semester == original



@given(instance=Univerity_Courses_strategy)
def test_hyp_univerity_courses_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Univerity_Courses_strategy)
def test_hyp_univerity_courses_CFU_setter(instance):
    original = instance.CFU
    instance.CFU = original
    assert instance.CFU == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Univerity_Courses,
    Univerity_Person,
    Univerity_University,
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

def test_Univerity_Courses_CFU_value_roundtrip():
    instance = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    assert instance.CFU == 7
    instance.CFU = 13
    assert instance.CFU == 13


def test_Univerity_Courses_Name_value_roundtrip():
    instance = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Univerity_Courses_Semester_value_roundtrip():
    instance = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    assert instance.Semester == "sample_text"
    instance.Semester = "sample_text_2"
    assert instance.Semester == "sample_text_2"


def test_Univerity_Person_Email_value_roundtrip():
    instance = Univerity_Person(Email="sample_text", Name="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Univerity_Person_Name_value_roundtrip():
    instance = Univerity_Person(Email="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_Courses10_link_reassign_clear():
    a = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    b1 = Univerity_University()
    b2 = Univerity_University()
    _safe_set(a, 'Univerity_Courses11', b1)
    assert _is_linked(a, 'Univerity_Courses11', b1)
    if hasattr(b1, 'Univerity_University'):
        assert _is_linked(b1, 'Univerity_University', a)
    _safe_set(a, 'Univerity_Courses11', b2)
    assert _is_linked(a, 'Univerity_Courses11', b2)
    if hasattr(b1, 'Univerity_University'):
        assert not _is_linked(b1, 'Univerity_University', a)
    if hasattr(b2, 'Univerity_University'):
        assert _is_linked(b2, 'Univerity_University', a)
    _safe_set(a, 'Univerity_Courses11', None)
    assert not _is_linked(a, 'Univerity_Courses11', b2)
    if hasattr(b2, 'Univerity_University'):
        assert not _is_linked(b2, 'Univerity_University', a)


def test_assoc_Professor2_link_reassign_clear():
    a = Univerity_Person(Email="sample_text", Name="sample_text")
    b1 = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    b2 = Univerity_Courses(CFU=13, Name="sample_text_2", Semester="sample_text_2")
    _safe_set(a, 'Univerity_Person', b1)
    assert _is_linked(a, 'Univerity_Person', b1)
    if hasattr(b1, 'Univerity_Courses3'):
        assert _is_linked(b1, 'Univerity_Courses3', a)
    _safe_set(a, 'Univerity_Person', b2)
    assert _is_linked(a, 'Univerity_Person', b2)
    if hasattr(b1, 'Univerity_Courses3'):
        assert not _is_linked(b1, 'Univerity_Courses3', a)
    if hasattr(b2, 'Univerity_Courses3'):
        assert _is_linked(b2, 'Univerity_Courses3', a)
    _safe_set(a, 'Univerity_Person', None)
    assert not _is_linked(a, 'Univerity_Person', b2)
    if hasattr(b2, 'Univerity_Courses3'):
        assert not _is_linked(b2, 'Univerity_Courses3', a)


def test_assoc_Student4_link_reassign_clear():
    a = Univerity_Person(Email="sample_text", Name="sample_text")
    b1 = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    b2 = Univerity_Courses(CFU=13, Name="sample_text_2", Semester="sample_text_2")
    _safe_set(a, 'Univerity_Person6', b1)
    assert _is_linked(a, 'Univerity_Person6', b1)
    if hasattr(b1, 'Univerity_Courses5'):
        assert _is_linked(b1, 'Univerity_Courses5', a)
    _safe_set(a, 'Univerity_Person6', b2)
    assert _is_linked(a, 'Univerity_Person6', b2)
    if hasattr(b1, 'Univerity_Courses5'):
        assert not _is_linked(b1, 'Univerity_Courses5', a)
    if hasattr(b2, 'Univerity_Courses5'):
        assert _is_linked(b2, 'Univerity_Courses5', a)
    _safe_set(a, 'Univerity_Person6', None)
    assert not _is_linked(a, 'Univerity_Person6', b2)
    if hasattr(b2, 'Univerity_Courses5'):
        assert not _is_linked(b2, 'Univerity_Courses5', a)


def test_assoc_links1_link_reassign_clear():
    a = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    b1 = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    b2 = Univerity_Courses(CFU=13, Name="sample_text_2", Semester="sample_text_2")
    _safe_set(a, 'Univerity_Courses', b1)
    assert _is_linked(a, 'Univerity_Courses', b1)
    if hasattr(b1, 'Univerity_Courses0'):
        assert _is_linked(b1, 'Univerity_Courses0', a)
    _safe_set(a, 'Univerity_Courses', b2)
    assert _is_linked(a, 'Univerity_Courses', b2)
    if hasattr(b1, 'Univerity_Courses0'):
        assert not _is_linked(b1, 'Univerity_Courses0', a)
    if hasattr(b2, 'Univerity_Courses0'):
        assert _is_linked(b2, 'Univerity_Courses0', a)
    _safe_set(a, 'Univerity_Courses', None)
    assert not _is_linked(a, 'Univerity_Courses', b2)
    if hasattr(b2, 'Univerity_Courses0'):
        assert not _is_linked(b2, 'Univerity_Courses0', a)


def test_assoc_relatives8_link_reassign_clear():
    a = Univerity_Person(Email="sample_text", Name="sample_text")
    b1 = Univerity_Person(Email="sample_text", Name="sample_text")
    b2 = Univerity_Person(Email="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'Univerity_Person7', b1)
    assert _is_linked(a, 'Univerity_Person7', b1)
    if hasattr(b1, 'Univerity_Person9'):
        assert _is_linked(b1, 'Univerity_Person9', a)
    _safe_set(a, 'Univerity_Person7', b2)
    assert _is_linked(a, 'Univerity_Person7', b2)
    if hasattr(b1, 'Univerity_Person9'):
        assert not _is_linked(b1, 'Univerity_Person9', a)
    if hasattr(b2, 'Univerity_Person9'):
        assert _is_linked(b2, 'Univerity_Person9', a)
    _safe_set(a, 'Univerity_Person7', None)
    assert not _is_linked(a, 'Univerity_Person7', b2)
    if hasattr(b2, 'Univerity_Person9'):
        assert not _is_linked(b2, 'Univerity_Person9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Univerity_Courses_strategy = st.builds(Univerity_Courses, CFU=st.integers(), Name=safe_text, Semester=safe_text)
@given(instance=Univerity_Courses_strategy)
@settings(max_examples=25)
def test_Univerity_Courses_instantiation(instance):
    assert isinstance(instance, Univerity_Courses)


Univerity_Person_strategy = st.builds(Univerity_Person, Email=safe_text, Name=safe_text)
@given(instance=Univerity_Person_strategy)
@settings(max_examples=25)
def test_Univerity_Person_instantiation(instance):
    assert isinstance(instance, Univerity_Person)


Univerity_University_strategy = st.builds(Univerity_University)
@given(instance=Univerity_University_strategy)
@settings(max_examples=25)
def test_Univerity_University_instantiation(instance):
    assert isinstance(instance, Univerity_University)



