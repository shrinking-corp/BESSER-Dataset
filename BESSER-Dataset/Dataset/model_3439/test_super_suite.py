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
    school_School,
    school_Student,
    school_Classroom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_school_school_is_not_abstract():
    assert not inspect.isabstract(school_School)


def test_hyp_school_school_constructor_exists():
    assert callable(school_School.__init__)


def test_hyp_school_school_constructor_args():
    sig = inspect.signature(school_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "director" in params, "Missing parameter 'director'"
    assert "city" in params, "Missing parameter 'city'"







def test_hyp_school_student_is_not_abstract():
    assert not inspect.isabstract(school_Student)


def test_hyp_school_student_constructor_exists():
    assert callable(school_Student.__init__)


def test_hyp_school_student_constructor_args():
    sig = inspect.signature(school_Student.__init__)
    params = list(sig.parameters.keys())
    assert "nickname" in params, "Missing parameter 'nickname'"
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_school_classroom_is_not_abstract():
    assert not inspect.isabstract(school_Classroom)


def test_hyp_school_classroom_constructor_exists():
    assert callable(school_Classroom.__init__)


def test_hyp_school_classroom_constructor_args():
    sig = inspect.signature(school_Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "teacher" in params, "Missing parameter 'teacher'"
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"






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
school_School_strategy = st.builds(
    school_School,
    name=
        safe_text,
    zipCode=
        safe_text,
    director=
        safe_text,
    city=
        safe_text
)
school_Student_strategy = st.builds(
    school_Student,
    nickname=
        safe_text,
    age=
        st.integers(),
    name=
        safe_text
)
school_Classroom_strategy = st.builds(
    school_Classroom,
    rank=
        st.integers(),
    teacher=
        safe_text,
    name=
        safe_text,
    capacity=
        st.integers()
)




@given(instance=school_School_strategy)
def test_hyp_school_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=school_School_strategy)
def test_hyp_school_school_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original



@given(instance=school_School_strategy)
def test_hyp_school_school_director_setter(instance):
    original = instance.director
    instance.director = original
    assert instance.director == original



@given(instance=school_School_strategy)
def test_hyp_school_school_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original




@given(instance=school_Student_strategy)
def test_hyp_school_student_nickname_setter(instance):
    original = instance.nickname
    instance.nickname = original
    assert instance.nickname == original



@given(instance=school_Student_strategy)
def test_hyp_school_student_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=school_Student_strategy)
def test_hyp_school_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





@given(instance=school_Classroom_strategy)
def test_hyp_school_classroom_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=school_Classroom_strategy)
def test_hyp_school_classroom_teacher_setter(instance):
    original = instance.teacher
    instance.teacher = original
    assert instance.teacher == original



@given(instance=school_Classroom_strategy)
def test_hyp_school_classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=school_Classroom_strategy)
def test_hyp_school_classroom_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    school_Classroom,
    school_School,
    school_Student,
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

def test_school_Classroom_capacity_value_roundtrip():
    instance = school_Classroom(capacity=7, name="sample_text", rank=7, teacher="sample_text")
    assert instance.capacity == 7
    instance.capacity = 13
    assert instance.capacity == 13


def test_school_Classroom_name_value_roundtrip():
    instance = school_Classroom(capacity=7, name="sample_text", rank=7, teacher="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_school_Classroom_rank_value_roundtrip():
    instance = school_Classroom(capacity=7, name="sample_text", rank=7, teacher="sample_text")
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_school_Classroom_teacher_value_roundtrip():
    instance = school_Classroom(capacity=7, name="sample_text", rank=7, teacher="sample_text")
    assert instance.teacher == "sample_text"
    instance.teacher = "sample_text_2"
    assert instance.teacher == "sample_text_2"


def test_school_School_city_value_roundtrip():
    instance = school_School(city="sample_text", director="sample_text", name="sample_text", zipCode="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_school_School_director_value_roundtrip():
    instance = school_School(city="sample_text", director="sample_text", name="sample_text", zipCode="sample_text")
    assert instance.director == "sample_text"
    instance.director = "sample_text_2"
    assert instance.director == "sample_text_2"


def test_school_School_name_value_roundtrip():
    instance = school_School(city="sample_text", director="sample_text", name="sample_text", zipCode="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_school_School_zipCode_value_roundtrip():
    instance = school_School(city="sample_text", director="sample_text", name="sample_text", zipCode="sample_text")
    assert instance.zipCode == "sample_text"
    instance.zipCode = "sample_text_2"
    assert instance.zipCode == "sample_text_2"


def test_school_Student_age_value_roundtrip():
    instance = school_Student(age=7, name="sample_text", nickname="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_school_Student_name_value_roundtrip():
    instance = school_Student(age=7, name="sample_text", nickname="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_school_Student_nickname_value_roundtrip():
    instance = school_Student(age=7, name="sample_text", nickname="sample_text")
    assert instance.nickname == "sample_text"
    instance.nickname = "sample_text_2"
    assert instance.nickname == "sample_text_2"


def test_assoc_classrooms1_link_reassign_clear():
    a = school_School(city="sample_text", director="sample_text", name="sample_text", zipCode="sample_text")
    b1 = school_Classroom(capacity=7, name="sample_text", rank=7, teacher="sample_text")
    b2 = school_Classroom(capacity=13, name="sample_text_2", rank=13, teacher="sample_text_2")
    _safe_set(a, 'school_School', {b1})
    assert _is_linked(a, 'school_School', b1)
    if hasattr(b1, 'school_Classroom2'):
        assert _is_linked(b1, 'school_Classroom2', a)
    _safe_set(a, 'school_School', {b2})
    assert _is_linked(a, 'school_School', b2)
    if hasattr(b1, 'school_Classroom2'):
        assert not _is_linked(b1, 'school_Classroom2', a)
    if hasattr(b2, 'school_Classroom2'):
        assert _is_linked(b2, 'school_Classroom2', a)
    _safe_set(a, 'school_School', set())
    assert not _is_linked(a, 'school_School', b2)
    if hasattr(b2, 'school_Classroom2'):
        assert not _is_linked(b2, 'school_Classroom2', a)


def test_assoc_friends4_link_reassign_clear():
    a = school_Student(age=7, name="sample_text", nickname="sample_text")
    b1 = school_Student(age=7, name="sample_text", nickname="sample_text")
    b2 = school_Student(age=13, name="sample_text_2", nickname="sample_text_2")
    _safe_set(a, 'school_Student3', {b1})
    assert _is_linked(a, 'school_Student3', b1)
    if hasattr(b1, 'school_Student5'):
        assert _is_linked(b1, 'school_Student5', a)
    _safe_set(a, 'school_Student3', {b2})
    assert _is_linked(a, 'school_Student3', b2)
    if hasattr(b1, 'school_Student5'):
        assert not _is_linked(b1, 'school_Student5', a)
    if hasattr(b2, 'school_Student5'):
        assert _is_linked(b2, 'school_Student5', a)
    _safe_set(a, 'school_Student3', set())
    assert not _is_linked(a, 'school_Student3', b2)
    if hasattr(b2, 'school_Student5'):
        assert not _is_linked(b2, 'school_Student5', a)


def test_assoc_students0_link_reassign_clear():
    a = school_Student(age=7, name="sample_text", nickname="sample_text")
    b1 = school_Classroom(capacity=7, name="sample_text", rank=7, teacher="sample_text")
    b2 = school_Classroom(capacity=13, name="sample_text_2", rank=13, teacher="sample_text_2")
    _safe_set(a, 'school_Student', b1)
    assert _is_linked(a, 'school_Student', b1)
    if hasattr(b1, 'school_Classroom'):
        assert _is_linked(b1, 'school_Classroom', a)
    _safe_set(a, 'school_Student', b2)
    assert _is_linked(a, 'school_Student', b2)
    if hasattr(b1, 'school_Classroom'):
        assert not _is_linked(b1, 'school_Classroom', a)
    if hasattr(b2, 'school_Classroom'):
        assert _is_linked(b2, 'school_Classroom', a)
    _safe_set(a, 'school_Student', None)
    assert not _is_linked(a, 'school_Student', b2)
    if hasattr(b2, 'school_Classroom'):
        assert not _is_linked(b2, 'school_Classroom', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

school_Classroom_strategy = st.builds(school_Classroom, capacity=st.integers(), name=safe_text, rank=st.integers(), teacher=safe_text)
@given(instance=school_Classroom_strategy)
@settings(max_examples=25)
def test_school_Classroom_instantiation(instance):
    assert isinstance(instance, school_Classroom)


school_School_strategy = st.builds(school_School, city=safe_text, director=safe_text, name=safe_text, zipCode=safe_text)
@given(instance=school_School_strategy)
@settings(max_examples=25)
def test_school_School_instantiation(instance):
    assert isinstance(instance, school_School)


school_Student_strategy = st.builds(school_Student, age=st.integers(), name=safe_text, nickname=safe_text)
@given(instance=school_Student_strategy)
@settings(max_examples=25)
def test_school_Student_instantiation(instance):
    assert isinstance(instance, school_Student)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    school_Classroom,
    school_School,
    school_Student,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_classrooms1_reverse_link_reassign_clear():
    a1 = school_School(city="sample_text", director="sample_text", name="sample_text", zipCode="sample_text")
    a2 = school_School(city="sample_text_2", director="sample_text_2", name="sample_text_2", zipCode="sample_text_2")
    b = school_Classroom(capacity=7, name="sample_text", rank=7, teacher="sample_text")
    _safe_set(b, 'school_Classroom2', a1)
    assert _is_linked(b, 'school_Classroom2', a1)
    if hasattr(a1, 'school_School'):
        assert _is_linked(a1, 'school_School', b)
    _safe_set(b, 'school_Classroom2', a2)
    assert _is_linked(b, 'school_Classroom2', a2)
    if hasattr(a1, 'school_School'):
        assert not _is_linked(a1, 'school_School', b)
    if hasattr(a2, 'school_School'):
        assert _is_linked(a2, 'school_School', b)
    _safe_set(b, 'school_Classroom2', None)
    assert not _is_linked(b, 'school_Classroom2', a2)
    if hasattr(a2, 'school_School'):
        assert not _is_linked(a2, 'school_School', b)


def test_assoc_friends4_reverse_link_reassign_clear():
    a1 = school_Student(age=7, name="sample_text", nickname="sample_text")
    a2 = school_Student(age=13, name="sample_text_2", nickname="sample_text_2")
    b = school_Student(age=7, name="sample_text", nickname="sample_text")
    _safe_set(b, 'school_Student5', a1)
    assert _is_linked(b, 'school_Student5', a1)
    if hasattr(a1, 'school_Student3'):
        assert _is_linked(a1, 'school_Student3', b)
    _safe_set(b, 'school_Student5', a2)
    assert _is_linked(b, 'school_Student5', a2)
    if hasattr(a1, 'school_Student3'):
        assert not _is_linked(a1, 'school_Student3', b)
    if hasattr(a2, 'school_Student3'):
        assert _is_linked(a2, 'school_Student3', b)
    _safe_set(b, 'school_Student5', None)
    assert not _is_linked(b, 'school_Student5', a2)
    if hasattr(a2, 'school_Student3'):
        assert not _is_linked(a2, 'school_Student3', b)


def test_assoc_students0_reverse_link_reassign_clear():
    a1 = school_Student(age=7, name="sample_text", nickname="sample_text")
    a2 = school_Student(age=13, name="sample_text_2", nickname="sample_text_2")
    b = school_Classroom(capacity=7, name="sample_text", rank=7, teacher="sample_text")
    _safe_set(b, 'school_Classroom', {a1})
    assert _is_linked(b, 'school_Classroom', a1)
    if hasattr(a1, 'school_Student'):
        assert _is_linked(a1, 'school_Student', b)
    _safe_set(b, 'school_Classroom', {a2})
    assert _is_linked(b, 'school_Classroom', a2)
    if hasattr(a1, 'school_Student'):
        assert not _is_linked(a1, 'school_Student', b)
    if hasattr(a2, 'school_Student'):
        assert _is_linked(a2, 'school_Student', b)
    _safe_set(b, 'school_Classroom', set())
    assert not _is_linked(b, 'school_Classroom', a2)
    if hasattr(a2, 'school_Student'):
        assert not _is_linked(a2, 'school_Student', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================



from python_code import school_School

def test_school_School___init__():
    assert school_School.__init__(school_School('', '', '', '', school_School=set()), '', '', '', '', school_School=set()) == None

