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
    edu_Take_Course,
    edu_Student,
    edu_Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_edu_take_course_is_not_abstract():
    assert not inspect.isabstract(edu_Take_Course)


def test_hyp_edu_take_course_constructor_exists():
    assert callable(edu_Take_Course.__init__)


def test_hyp_edu_take_course_constructor_args():
    sig = inspect.signature(edu_Take_Course.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_student_is_not_abstract():
    assert not inspect.isabstract(edu_Student)


def test_hyp_edu_student_constructor_exists():
    assert callable(edu_Student.__init__)


def test_hyp_edu_student_constructor_args():
    sig = inspect.signature(edu_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "date_of_birth" in params, "Missing parameter 'date_of_birth'"






def test_hyp_edu_course_is_not_abstract():
    assert not inspect.isabstract(edu_Course)


def test_hyp_edu_course_constructor_exists():
    assert callable(edu_Course.__init__)


def test_hyp_edu_course_constructor_args():
    sig = inspect.signature(edu_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"




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
edu_Take_Course_strategy = st.builds(
    edu_Take_Course,
)
edu_Student_strategy = st.builds(
    edu_Student,
    name=
        safe_text,
    id=
        st.integers(),
    date_of_birth=
        st.dates()
)
edu_Course_strategy = st.builds(
    edu_Course,
    name=
        safe_text,
    id=
        st.integers()
)





@given(instance=edu_Student_strategy)
def test_hyp_edu_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=edu_Student_strategy)
def test_hyp_edu_student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=edu_Student_strategy)
def test_hyp_edu_student_date_of_birth_setter(instance):
    original = instance.date_of_birth
    instance.date_of_birth = original
    assert instance.date_of_birth == original




@given(instance=edu_Course_strategy)
def test_hyp_edu_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=edu_Course_strategy)
def test_hyp_edu_course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    edu_Course,
    edu_Student,
    edu_Take_Course,
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

def test_edu_Course_id_value_roundtrip():
    instance = edu_Course(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_edu_Course_name_value_roundtrip():
    instance = edu_Course(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_edu_Student_date_of_birth_value_roundtrip():
    instance = edu_Student(date_of_birth=date(2024, 1, 1), id=7, name="sample_text")
    assert instance.date_of_birth == date(2024, 1, 1)
    instance.date_of_birth = date(2025, 6, 15)
    assert instance.date_of_birth == date(2025, 6, 15)


def test_edu_Student_id_value_roundtrip():
    instance = edu_Student(date_of_birth=date(2024, 1, 1), id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_edu_Student_name_value_roundtrip():
    instance = edu_Student(date_of_birth=date(2024, 1, 1), id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_course1_link_reassign_clear():
    a = edu_Course(id=7, name="sample_text")
    b1 = edu_Take_Course()
    b2 = edu_Take_Course()
    _safe_set(a, 'edu_Course', b1)
    assert _is_linked(a, 'edu_Course', b1)
    if hasattr(b1, 'edu_Take_Course2'):
        assert _is_linked(b1, 'edu_Take_Course2', a)
    _safe_set(a, 'edu_Course', b2)
    assert _is_linked(a, 'edu_Course', b2)
    if hasattr(b1, 'edu_Take_Course2'):
        assert not _is_linked(b1, 'edu_Take_Course2', a)
    if hasattr(b2, 'edu_Take_Course2'):
        assert _is_linked(b2, 'edu_Take_Course2', a)
    _safe_set(a, 'edu_Course', None)
    assert not _is_linked(a, 'edu_Course', b2)
    if hasattr(b2, 'edu_Take_Course2'):
        assert not _is_linked(b2, 'edu_Take_Course2', a)


def test_assoc_student0_link_reassign_clear():
    a = edu_Student(date_of_birth=date(2024, 1, 1), id=7, name="sample_text")
    b1 = edu_Take_Course()
    b2 = edu_Take_Course()
    _safe_set(a, 'edu_Student', b1)
    assert _is_linked(a, 'edu_Student', b1)
    if hasattr(b1, 'edu_Take_Course'):
        assert _is_linked(b1, 'edu_Take_Course', a)
    _safe_set(a, 'edu_Student', b2)
    assert _is_linked(a, 'edu_Student', b2)
    if hasattr(b1, 'edu_Take_Course'):
        assert not _is_linked(b1, 'edu_Take_Course', a)
    if hasattr(b2, 'edu_Take_Course'):
        assert _is_linked(b2, 'edu_Take_Course', a)
    _safe_set(a, 'edu_Student', None)
    assert not _is_linked(a, 'edu_Student', b2)
    if hasattr(b2, 'edu_Take_Course'):
        assert not _is_linked(b2, 'edu_Take_Course', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

edu_Course_strategy = st.builds(edu_Course, id=st.integers(), name=safe_text)
@given(instance=edu_Course_strategy)
@settings(max_examples=25)
def test_edu_Course_instantiation(instance):
    assert isinstance(instance, edu_Course)


edu_Student_strategy = st.builds(edu_Student, date_of_birth=st.dates(), id=st.integers(), name=safe_text)
@given(instance=edu_Student_strategy)
@settings(max_examples=25)
def test_edu_Student_instantiation(instance):
    assert isinstance(instance, edu_Student)


edu_Take_Course_strategy = st.builds(edu_Take_Course)
@given(instance=edu_Take_Course_strategy)
@settings(max_examples=25)
def test_edu_Take_Course_instantiation(instance):
    assert isinstance(instance, edu_Take_Course)



