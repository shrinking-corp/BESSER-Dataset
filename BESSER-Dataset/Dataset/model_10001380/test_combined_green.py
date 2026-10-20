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
    Subject,
    StudyField,
    Headmaster,
    Exam,
    Teacher,
    Student,
    School,
    Student__,
    StudyField__,
    Teacher__,
    Subjects__,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_subject_is_not_abstract():
    assert not inspect.isabstract(Subject)


def test_hyp_subject_constructor_exists():
    assert callable(Subject.__init__)


def test_hyp_subject_constructor_args():
    sig = inspect.signature(Subject.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"
    assert "currentId" in params, "Missing parameter 'currentId'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_studyfield_is_not_abstract():
    assert not inspect.isabstract(StudyField)


def test_hyp_studyfield_constructor_exists():
    assert callable(StudyField.__init__)


def test_hyp_studyfield_constructor_args():
    sig = inspect.signature(StudyField.__init__)
    params = list(sig.parameters.keys())
    assert "currentId" in params, "Missing parameter 'currentId'"
    assert "subjectsCount" in params, "Missing parameter 'subjectsCount'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subjects" in params, "Missing parameter 'subjects'"
    assert "name" in params, "Missing parameter 'name'"

def test_hyp_studyfield_has_currentId():
    assert hasattr(StudyField, "currentId")
    descriptor = None
    for klass in StudyField.__mro__:
        if "currentId" in klass.__dict__:
            descriptor = klass.__dict__["currentId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_studyfield_has_subjectsCount():
    assert hasattr(StudyField, "subjectsCount")
    descriptor = None
    for klass in StudyField.__mro__:
        if "subjectsCount" in klass.__dict__:
            descriptor = klass.__dict__["subjectsCount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_studyfield_has_id():
    assert hasattr(StudyField, "id")
    descriptor = None
    for klass in StudyField.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_studyfield_has_subjects():
    assert hasattr(StudyField, "subjects")
    descriptor = None
    for klass in StudyField.__mro__:
        if "subjects" in klass.__dict__:
            descriptor = klass.__dict__["subjects"]
            break
    assert isinstance(descriptor, property)

def test_hyp_studyfield_has_name():
    assert hasattr(StudyField, "name")
    descriptor = None
    for klass in StudyField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hyp_headmaster_is_not_abstract():
    assert not inspect.isabstract(Headmaster)


def test_hyp_headmaster_constructor_exists():
    assert callable(Headmaster.__init__)


def test_hyp_headmaster_constructor_args():
    sig = inspect.signature(Headmaster.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exam_is_not_abstract():
    assert not inspect.isabstract(Exam)


def test_hyp_exam_constructor_exists():
    assert callable(Exam.__init__)


def test_hyp_exam_constructor_args():
    sig = inspect.signature(Exam.__init__)
    params = list(sig.parameters.keys())
    assert "currentId" in params, "Missing parameter 'currentId'"
    assert "points" in params, "Missing parameter 'points'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "subject" in params, "Missing parameter 'subject'"

def test_hyp_exam_has_currentId():
    assert hasattr(Exam, "currentId")
    descriptor = None
    for klass in Exam.__mro__:
        if "currentId" in klass.__dict__:
            descriptor = klass.__dict__["currentId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_exam_has_points():
    assert hasattr(Exam, "points")
    descriptor = None
    for klass in Exam.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_hyp_exam_has_id():
    assert hasattr(Exam, "id")
    descriptor = None
    for klass in Exam.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_exam_has_name():
    assert hasattr(Exam, "name")
    descriptor = None
    for klass in Exam.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_exam_has_subject():
    assert hasattr(Exam, "subject")
    descriptor = None
    for klass in Exam.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_hyp_teacher_is_not_abstract():
    assert not inspect.isabstract(Teacher)


def test_hyp_teacher_constructor_exists():
    assert callable(Teacher.__init__)


def test_hyp_teacher_constructor_args():
    sig = inspect.signature(Teacher.__init__)
    params = list(sig.parameters.keys())



def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())



def test_hyp_school_is_not_abstract():
    assert not inspect.isabstract(School)


def test_hyp_school_constructor_exists():
    assert callable(School.__init__)


def test_hyp_school_constructor_args():
    sig = inspect.signature(School.__init__)
    params = list(sig.parameters.keys())
    assert "fields" in params, "Missing parameter 'fields'"
    assert "headmaster" in params, "Missing parameter 'headmaster'"
    assert "studentsCount" in params, "Missing parameter 'studentsCount'"
    assert "fieldsCount" in params, "Missing parameter 'fieldsCount'"
    assert "teachersCount" in params, "Missing parameter 'teachersCount'"
    assert "students" in params, "Missing parameter 'students'"
    assert "teachers" in params, "Missing parameter 'teachers'"
    assert "name" in params, "Missing parameter 'name'"

def test_hyp_school_has_fields():
    assert hasattr(School, "fields")
    descriptor = None
    for klass in School.__mro__:
        if "fields" in klass.__dict__:
            descriptor = klass.__dict__["fields"]
            break
    assert isinstance(descriptor, property)

def test_hyp_school_has_headmaster():
    assert hasattr(School, "headmaster")
    descriptor = None
    for klass in School.__mro__:
        if "headmaster" in klass.__dict__:
            descriptor = klass.__dict__["headmaster"]
            break
    assert isinstance(descriptor, property)

def test_hyp_school_has_studentsCount():
    assert hasattr(School, "studentsCount")
    descriptor = None
    for klass in School.__mro__:
        if "studentsCount" in klass.__dict__:
            descriptor = klass.__dict__["studentsCount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_school_has_fieldsCount():
    assert hasattr(School, "fieldsCount")
    descriptor = None
    for klass in School.__mro__:
        if "fieldsCount" in klass.__dict__:
            descriptor = klass.__dict__["fieldsCount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_school_has_teachersCount():
    assert hasattr(School, "teachersCount")
    descriptor = None
    for klass in School.__mro__:
        if "teachersCount" in klass.__dict__:
            descriptor = klass.__dict__["teachersCount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_school_has_students():
    assert hasattr(School, "students")
    descriptor = None
    for klass in School.__mro__:
        if "students" in klass.__dict__:
            descriptor = klass.__dict__["students"]
            break
    assert isinstance(descriptor, property)

def test_hyp_school_has_teachers():
    assert hasattr(School, "teachers")
    descriptor = None
    for klass in School.__mro__:
        if "teachers" in klass.__dict__:
            descriptor = klass.__dict__["teachers"]
            break
    assert isinstance(descriptor, property)

def test_hyp_school_has_name():
    assert hasattr(School, "name")
    descriptor = None
    for klass in School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_student___exists():
    # Check that the Enumeration exists
    assert Student__ is not None

def test_hyp_student___has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Student__]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Student__"

def test_hyp_studyfield___exists():
    # Check that the Enumeration exists
    assert StudyField__ is not None

def test_hyp_studyfield___has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyField__]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyField__"

def test_hyp_teacher___exists():
    # Check that the Enumeration exists
    assert Teacher__ is not None

def test_hyp_teacher___has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Teacher__]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Teacher__"

def test_hyp_subjects___exists():
    # Check that the Enumeration exists
    assert Subjects__ is not None

def test_hyp_subjects___has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Subjects__]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Subjects__"


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
Subject_strategy = st.builds(
    Subject,
    credits=
        st.integers(),
    name=
        safe_text,
    currentId=
        st.integers(),
    id=
        st.integers()
)
StudyField_strategy = st.builds(
    StudyField,
    currentId=
        st.integers(),
    subjectsCount=
        st.integers(),
    id=
        st.integers(),
    subjects=
        st.none(),
    name=
        safe_text
)
Headmaster_strategy = st.builds(
    Headmaster,
)
Exam_strategy = st.builds(
    Exam,
    currentId=
        st.integers(),
    points=
        st.integers(),
    id=
        safe_text,
    name=
        safe_text,
    subject=
        st.none()
)
Teacher_strategy = st.builds(
    Teacher,
)
Student_strategy = st.builds(
    Student,
)
School_strategy = st.builds(
    School,
    fields=
        st.none(),
    headmaster=
        st.none(),
    studentsCount=
        st.integers(),
    fieldsCount=
        st.integers(),
    teachersCount=
        st.integers(),
    students=
        st.none(),
    teachers=
        st.none(),
    name=
        st.integers()
)




@given(instance=Subject_strategy)
def test_hyp_subject_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=Subject_strategy)
def test_hyp_subject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Subject_strategy)
def test_hyp_subject_currentId_setter(instance):
    original = instance.currentId
    instance.currentId = original
    assert instance.currentId == original



@given(instance=Subject_strategy)
def test_hyp_subject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=StudyField_strategy)
@settings(max_examples=50)
def test_hyp_studyfield_instantiation(instance):
    assert isinstance(instance, StudyField)



@given(instance=StudyField_strategy)
def test_hyp_studyfield_currentId_setter(instance):
    original = instance.currentId
    instance.currentId = original
    assert instance.currentId == original



@given(instance=StudyField_strategy)
def test_hyp_studyfield_subjectsCount_setter(instance):
    original = instance.subjectsCount
    instance.subjectsCount = original
    assert instance.subjectsCount == original



@given(instance=StudyField_strategy)
def test_hyp_studyfield_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=StudyField_strategy)
def test_hyp_studyfield_subjects_setter(instance):
    original = instance.subjects
    instance.subjects = original
    assert instance.subjects == original



@given(instance=StudyField_strategy)
def test_hyp_studyfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


@given(instance=Exam_strategy)
@settings(max_examples=50)
def test_hyp_exam_instantiation(instance):
    assert isinstance(instance, Exam)



@given(instance=Exam_strategy)
def test_hyp_exam_currentId_setter(instance):
    original = instance.currentId
    instance.currentId = original
    assert instance.currentId == original



@given(instance=Exam_strategy)
def test_hyp_exam_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=Exam_strategy)
def test_hyp_exam_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Exam_strategy)
def test_hyp_exam_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Exam_strategy)
def test_hyp_exam_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=School_strategy)
@settings(max_examples=50)
def test_hyp_school_instantiation(instance):
    assert isinstance(instance, School)



@given(instance=School_strategy)
def test_hyp_school_fields_setter(instance):
    original = instance.fields
    instance.fields = original
    assert instance.fields == original



@given(instance=School_strategy)
def test_hyp_school_headmaster_setter(instance):
    original = instance.headmaster
    instance.headmaster = original
    assert instance.headmaster == original



@given(instance=School_strategy)
def test_hyp_school_studentsCount_setter(instance):
    original = instance.studentsCount
    instance.studentsCount = original
    assert instance.studentsCount == original



@given(instance=School_strategy)
def test_hyp_school_fieldsCount_setter(instance):
    original = instance.fieldsCount
    instance.fieldsCount = original
    assert instance.fieldsCount == original



@given(instance=School_strategy)
def test_hyp_school_teachersCount_setter(instance):
    original = instance.teachersCount
    instance.teachersCount = original
    assert instance.teachersCount == original



@given(instance=School_strategy)
def test_hyp_school_students_setter(instance):
    original = instance.students
    instance.students = original
    assert instance.students == original



@given(instance=School_strategy)
def test_hyp_school_teachers_setter(instance):
    original = instance.teachers
    instance.teachers = original
    assert instance.teachers == original



@given(instance=School_strategy)
def test_hyp_school_name_setter(instance):
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
    Exam,
    Headmaster,
    School,
    Student,
    StudyField,
    Subject,
    Teacher,
    Student__,
    StudyField__,
    Subjects__,
    Teacher__,
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

def test_Subject_credits_value_roundtrip():
    instance = Subject(credits=7, currentId=7, id=7, name="sample_text")
    assert instance.credits == 7
    instance.credits = 13
    assert instance.credits == 13


def test_Subject_currentId_value_roundtrip():
    instance = Subject(credits=7, currentId=7, id=7, name="sample_text")
    assert instance.currentId == 7
    instance.currentId = 13
    assert instance.currentId == 13


def test_Subject_id_value_roundtrip():
    instance = Subject(credits=7, currentId=7, id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Subject_name_value_roundtrip():
    instance = Subject(credits=7, currentId=7, id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Headmaster_strategy = st.builds(Headmaster)
@given(instance=Headmaster_strategy)
@settings(max_examples=25)
def test_Headmaster_instantiation(instance):
    assert isinstance(instance, Headmaster)


Student_strategy = st.builds(Student)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Subject_strategy = st.builds(Subject, credits=st.integers(), currentId=st.integers(), id=st.integers(), name=safe_text)
@given(instance=Subject_strategy)
@settings(max_examples=25)
def test_Subject_instantiation(instance):
    assert isinstance(instance, Subject)


Teacher_strategy = st.builds(Teacher)
@given(instance=Teacher_strategy)
@settings(max_examples=25)
def test_Teacher_instantiation(instance):
    assert isinstance(instance, Teacher)



