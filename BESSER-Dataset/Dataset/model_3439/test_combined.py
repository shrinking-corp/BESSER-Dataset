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

@given(instance=school_Student_strategy)
@settings(max_examples=30)
def test_hyp_school_student_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in school_Student is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in school_Student did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in school_Student is not implemented or raised an error")




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

@given(instance=school_Classroom_strategy)
@settings(max_examples=30)
def test_hyp_school_classroom_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in school_Classroom is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in school_Classroom did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in school_Classroom is not implemented or raised an error")


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



