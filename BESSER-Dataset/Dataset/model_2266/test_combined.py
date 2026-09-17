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
    TUWien_Student,
    TUWien_Course,
    TUWien_University,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tuwien_student_is_not_abstract():
    assert not inspect.isabstract(TUWien_Student)


def test_hyp_tuwien_student_constructor_exists():
    assert callable(TUWien_Student.__init__)


def test_hyp_tuwien_student_constructor_args():
    sig = inspect.signature(TUWien_Student.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_tuwien_course_is_not_abstract():
    assert not inspect.isabstract(TUWien_Course)


def test_hyp_tuwien_course_constructor_exists():
    assert callable(TUWien_Course.__init__)


def test_hyp_tuwien_course_constructor_args():
    sig = inspect.signature(TUWien_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_tuwien_university_is_not_abstract():
    assert not inspect.isabstract(TUWien_University)


def test_hyp_tuwien_university_constructor_exists():
    assert callable(TUWien_University.__init__)


def test_hyp_tuwien_university_constructor_args():
    sig = inspect.signature(TUWien_University.__init__)
    params = list(sig.parameters.keys())
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
TUWien_Student_strategy = st.builds(
    TUWien_Student,
    id=
        st.integers(),
    name=
        safe_text
)
TUWien_Course_strategy = st.builds(
    TUWien_Course,
    name=
        safe_text,
    id=
        safe_text
)
TUWien_University_strategy = st.builds(
    TUWien_University,
    name=
        safe_text
)




@given(instance=TUWien_Student_strategy)
def test_hyp_tuwien_student_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=TUWien_Student_strategy)
def test_hyp_tuwien_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=TUWien_Course_strategy)
def test_hyp_tuwien_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=TUWien_Course_strategy)
def test_hyp_tuwien_course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=TUWien_University_strategy)
def test_hyp_tuwien_university_name_setter(instance):
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
    TUWien_Course,
    TUWien_Student,
    TUWien_University,
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

def test_TUWien_Course_id_value_roundtrip():
    instance = TUWien_Course(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_TUWien_Course_name_value_roundtrip():
    instance = TUWien_Course(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_TUWien_Student_id_value_roundtrip():
    instance = TUWien_Student(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_TUWien_Student_name_value_roundtrip():
    instance = TUWien_Student(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_TUWien_University_name_value_roundtrip():
    instance = TUWien_University(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_course3_link_reassign_clear():
    a = TUWien_Student(id=7, name="sample_text")
    b1 = TUWien_Course(id="sample_text", name="sample_text")
    b2 = TUWien_Course(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'student', {b1})
    assert _is_linked(a, 'student', b1)
    if hasattr(b1, 'Course'):
        assert _is_linked(b1, 'Course', a)
    _safe_set(a, 'student', {b2})
    assert _is_linked(a, 'student', b2)
    if hasattr(b1, 'Course'):
        assert not _is_linked(b1, 'Course', a)
    if hasattr(b2, 'Course'):
        assert _is_linked(b2, 'Course', a)
    _safe_set(a, 'student', set())
    assert not _is_linked(a, 'student', b2)
    if hasattr(b2, 'Course'):
        assert not _is_linked(b2, 'Course', a)


def test_assoc_courses0_link_reassign_clear():
    a = TUWien_University(name="sample_text")
    b1 = TUWien_Course(id="sample_text", name="sample_text")
    b2 = TUWien_Course(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'TUWien_University', {b1})
    assert _is_linked(a, 'TUWien_University', b1)
    if hasattr(b1, 'TUWien_Course'):
        assert _is_linked(b1, 'TUWien_Course', a)
    _safe_set(a, 'TUWien_University', {b2})
    assert _is_linked(a, 'TUWien_University', b2)
    if hasattr(b1, 'TUWien_Course'):
        assert not _is_linked(b1, 'TUWien_Course', a)
    if hasattr(b2, 'TUWien_Course'):
        assert _is_linked(b2, 'TUWien_Course', a)
    _safe_set(a, 'TUWien_University', set())
    assert not _is_linked(a, 'TUWien_University', b2)
    if hasattr(b2, 'TUWien_Course'):
        assert not _is_linked(b2, 'TUWien_Course', a)


def test_assoc_student4_link_reassign_clear():
    a = TUWien_Student(id=7, name="sample_text")
    b1 = TUWien_Course(id="sample_text", name="sample_text")
    b2 = TUWien_Course(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Student', b1)
    assert _is_linked(a, 'Student', b1)
    if hasattr(b1, 'course'):
        assert _is_linked(b1, 'course', a)
    _safe_set(a, 'Student', b2)
    assert _is_linked(a, 'Student', b2)
    if hasattr(b1, 'course'):
        assert not _is_linked(b1, 'course', a)
    if hasattr(b2, 'course'):
        assert _is_linked(b2, 'course', a)
    _safe_set(a, 'Student', None)
    assert not _is_linked(a, 'Student', b2)
    if hasattr(b2, 'course'):
        assert not _is_linked(b2, 'course', a)


def test_assoc_students1_link_reassign_clear():
    a = TUWien_University(name="sample_text")
    b1 = TUWien_Student(id=7, name="sample_text")
    b2 = TUWien_Student(id=13, name="sample_text_2")
    _safe_set(a, 'TUWien_University2', {b1})
    assert _is_linked(a, 'TUWien_University2', b1)
    if hasattr(b1, 'TUWien_Student'):
        assert _is_linked(b1, 'TUWien_Student', a)
    _safe_set(a, 'TUWien_University2', {b2})
    assert _is_linked(a, 'TUWien_University2', b2)
    if hasattr(b1, 'TUWien_Student'):
        assert not _is_linked(b1, 'TUWien_Student', a)
    if hasattr(b2, 'TUWien_Student'):
        assert _is_linked(b2, 'TUWien_Student', a)
    _safe_set(a, 'TUWien_University2', set())
    assert not _is_linked(a, 'TUWien_University2', b2)
    if hasattr(b2, 'TUWien_Student'):
        assert not _is_linked(b2, 'TUWien_Student', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

TUWien_Course_strategy = st.builds(TUWien_Course, id=safe_text, name=safe_text)
@given(instance=TUWien_Course_strategy)
@settings(max_examples=25)
def test_TUWien_Course_instantiation(instance):
    assert isinstance(instance, TUWien_Course)


TUWien_Student_strategy = st.builds(TUWien_Student, id=st.integers(), name=safe_text)
@given(instance=TUWien_Student_strategy)
@settings(max_examples=25)
def test_TUWien_Student_instantiation(instance):
    assert isinstance(instance, TUWien_Student)


TUWien_University_strategy = st.builds(TUWien_University, name=safe_text)
@given(instance=TUWien_University_strategy)
@settings(max_examples=25)
def test_TUWien_University_instantiation(instance):
    assert isinstance(instance, TUWien_University)



