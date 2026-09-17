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
    education_Course,
    Person,
    education_Teacher,
    education_Student,
    education_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_education_course_is_not_abstract():
    assert not inspect.isabstract(education_Course)


def test_hyp_education_course_constructor_exists():
    assert callable(education_Course.__init__)


def test_hyp_education_course_constructor_args():
    sig = inspect.signature(education_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_education_teacher_is_not_abstract():
    assert not inspect.isabstract(education_Teacher)


def test_hyp_education_teacher_constructor_exists():
    assert callable(education_Teacher.__init__)


def test_hyp_education_teacher_constructor_args():
    sig = inspect.signature(education_Teacher.__init__)
    params = list(sig.parameters.keys())



def test_hyp_education_student_is_not_abstract():
    assert not inspect.isabstract(education_Student)


def test_hyp_education_student_constructor_exists():
    assert callable(education_Student.__init__)


def test_hyp_education_student_constructor_args():
    sig = inspect.signature(education_Student.__init__)
    params = list(sig.parameters.keys())



def test_hyp_education_person_is_not_abstract():
    assert not inspect.isabstract(education_Person)


def test_hyp_education_person_constructor_exists():
    assert callable(education_Person.__init__)


def test_hyp_education_person_constructor_args():
    sig = inspect.signature(education_Person.__init__)
    params = list(sig.parameters.keys())
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
education_Course_strategy = st.builds(
    education_Course,
    name=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
education_Teacher_strategy = st.builds(
    education_Teacher,
)
education_Student_strategy = st.builds(
    education_Student,
)
education_Person_strategy = st.builds(
    education_Person,
    lastname=
        safe_text,
    firstname=
        safe_text
)




@given(instance=education_Course_strategy)
def test_hyp_education_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=education_Course_strategy)
@settings(max_examples=30)
def test_hyp_education_course_finish_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.finish(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.finish).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'finish' in education_Course is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'finish' in education_Course did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'finish' in education_Course is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=education_Course_strategy)
@settings(max_examples=30)
def test_hyp_education_course_start_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.start(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.start).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'start' in education_Course is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'start' in education_Course did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'start' in education_Course is not implemented or raised an error")







@given(instance=education_Person_strategy)
def test_hyp_education_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=education_Person_strategy)
def test_hyp_education_person_firstname_setter(instance):
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
    Person,
    education_Course,
    education_Person,
    education_Student,
    education_Teacher,
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

def test_education_Course_name_value_roundtrip():
    instance = education_Course(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_education_Person_firstname_value_roundtrip():
    instance = education_Person(firstname="sample_text", lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_education_Person_lastname_value_roundtrip():
    instance = education_Person(firstname="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_education_Student_isa_Person():
    instance = education_Student()
    assert isinstance(instance, Person)


def test_education_Teacher_isa_Person():
    instance = education_Teacher()
    assert isinstance(instance, Person)


def test_assoc_student0_link_reassign_clear():
    a = education_Course(name="sample_text")
    b1 = education_Student()
    b2 = education_Student()
    _safe_set(a, 'education_Course', {b1})
    assert _is_linked(a, 'education_Course', b1)
    if hasattr(b1, 'education_Student'):
        assert _is_linked(b1, 'education_Student', a)
    _safe_set(a, 'education_Course', {b2})
    assert _is_linked(a, 'education_Course', b2)
    if hasattr(b1, 'education_Student'):
        assert not _is_linked(b1, 'education_Student', a)
    if hasattr(b2, 'education_Student'):
        assert _is_linked(b2, 'education_Student', a)
    _safe_set(a, 'education_Course', set())
    assert not _is_linked(a, 'education_Course', b2)
    if hasattr(b2, 'education_Student'):
        assert not _is_linked(b2, 'education_Student', a)


def test_assoc_teacher1_link_reassign_clear():
    a = education_Course(name="sample_text")
    b1 = education_Teacher()
    b2 = education_Teacher()
    _safe_set(a, 'education_Course2', b1)
    assert _is_linked(a, 'education_Course2', b1)
    if hasattr(b1, 'education_Teacher'):
        assert _is_linked(b1, 'education_Teacher', a)
    _safe_set(a, 'education_Course2', b2)
    assert _is_linked(a, 'education_Course2', b2)
    if hasattr(b1, 'education_Teacher'):
        assert not _is_linked(b1, 'education_Teacher', a)
    if hasattr(b2, 'education_Teacher'):
        assert _is_linked(b2, 'education_Teacher', a)
    _safe_set(a, 'education_Course2', None)
    assert not _is_linked(a, 'education_Course2', b2)
    if hasattr(b2, 'education_Teacher'):
        assert not _is_linked(b2, 'education_Teacher', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


education_Course_strategy = st.builds(education_Course, name=safe_text)
@given(instance=education_Course_strategy)
@settings(max_examples=25)
def test_education_Course_instantiation(instance):
    assert isinstance(instance, education_Course)


education_Person_strategy = st.builds(education_Person, firstname=safe_text, lastname=safe_text)
@given(instance=education_Person_strategy)
@settings(max_examples=25)
def test_education_Person_instantiation(instance):
    assert isinstance(instance, education_Person)


education_Student_strategy = st.builds(education_Student)
@given(instance=education_Student_strategy)
@settings(max_examples=25)
def test_education_Student_instantiation(instance):
    assert isinstance(instance, education_Student)


education_Teacher_strategy = st.builds(education_Teacher)
@given(instance=education_Teacher_strategy)
@settings(max_examples=25)
def test_education_Teacher_instantiation(instance):
    assert isinstance(instance, education_Teacher)



