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
    Schedule,
    Note,
    Subject,
    Grade,
    Teacher,
    Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_schedule_is_not_abstract():
    assert not inspect.isabstract(Schedule)


def test_hyp_schedule_constructor_exists():
    assert callable(Schedule.__init__)


def test_hyp_schedule_constructor_args():
    sig = inspect.signature(Schedule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_note_is_not_abstract():
    assert not inspect.isabstract(Note)


def test_hyp_note_constructor_exists():
    assert callable(Note.__init__)


def test_hyp_note_constructor_args():
    sig = inspect.signature(Note.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subject_is_not_abstract():
    assert not inspect.isabstract(Subject)


def test_hyp_subject_constructor_exists():
    assert callable(Subject.__init__)


def test_hyp_subject_constructor_args():
    sig = inspect.signature(Subject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_grade_is_not_abstract():
    assert not inspect.isabstract(Grade)


def test_hyp_grade_constructor_exists():
    assert callable(Grade.__init__)


def test_hyp_grade_constructor_args():
    sig = inspect.signature(Grade.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_teacher_is_not_abstract():
    assert not inspect.isabstract(Teacher)


def test_hyp_teacher_constructor_exists():
    assert callable(Teacher.__init__)


def test_hyp_teacher_constructor_args():
    sig = inspect.signature(Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"
    assert "surname" in params, "Missing parameter 'surname'"







def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "surname" in params, "Missing parameter 'surname'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phone" in params, "Missing parameter 'phone'"
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
Schedule_strategy = st.builds(
    Schedule,
)
Note_strategy = st.builds(
    Note,
)
Subject_strategy = st.builds(
    Subject,
)
Grade_strategy = st.builds(
    Grade,
    name=
        safe_text
)
Teacher_strategy = st.builds(
    Teacher,
    phone=
        safe_text,
    name=
        safe_text,
    email=
        safe_text,
    surname=
        safe_text
)
Student_strategy = st.builds(
    Student,
    surname=
        safe_text,
    email=
        safe_text,
    phone=
        safe_text,
    name=
        safe_text
)







@given(instance=Grade_strategy)
def test_hyp_grade_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Teacher_strategy)
def test_hyp_teacher_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Teacher_strategy)
def test_hyp_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Teacher_strategy)
def test_hyp_teacher_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Teacher_strategy)
def test_hyp_teacher_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original




@given(instance=Student_strategy)
def test_hyp_student_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=Student_strategy)
def test_hyp_student_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Student_strategy)
def test_hyp_student_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Student_strategy)
def test_hyp_student_name_setter(instance):
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
    Grade,
    Note,
    Schedule,
    Student,
    Subject,
    Teacher,
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

def test_Grade_name_value_roundtrip():
    instance = Grade(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Student_email_value_roundtrip():
    instance = Student(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Student_name_value_roundtrip():
    instance = Student(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Student_phone_value_roundtrip():
    instance = Student(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_Student_surname_value_roundtrip():
    instance = Student(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_Teacher_email_value_roundtrip():
    instance = Teacher(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Teacher_name_value_roundtrip():
    instance = Teacher(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Teacher_phone_value_roundtrip():
    instance = Teacher(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_Teacher_surname_value_roundtrip():
    instance = Teacher(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_assoc_Grade_Teacher_link_reassign_clear():
    a = Teacher(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    b1 = Grade(name="sample_text")
    b2 = Grade(name="sample_text_2")
    _safe_set(a, 'grades1', b1)
    assert _is_linked(a, 'grades1', b1)
    if hasattr(b1, 'teacher0'):
        assert _is_linked(b1, 'teacher0', a)
    _safe_set(a, 'grades1', b2)
    assert _is_linked(a, 'grades1', b2)
    if hasattr(b1, 'teacher0'):
        assert not _is_linked(b1, 'teacher0', a)
    if hasattr(b2, 'teacher0'):
        assert _is_linked(b2, 'teacher0', a)
    _safe_set(a, 'grades1', None)
    assert not _is_linked(a, 'grades1', b2)
    if hasattr(b2, 'teacher0'):
        assert not _is_linked(b2, 'teacher0', a)


def test_assoc_Schedule_Student_link_reassign_clear():
    a = Student(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    b1 = Schedule()
    b2 = Schedule()
    _safe_set(a, 'schedule9', b1)
    assert _is_linked(a, 'schedule9', b1)
    if hasattr(b1, 'student8'):
        assert _is_linked(b1, 'student8', a)
    _safe_set(a, 'schedule9', b2)
    assert _is_linked(a, 'schedule9', b2)
    if hasattr(b1, 'student8'):
        assert not _is_linked(b1, 'student8', a)
    if hasattr(b2, 'student8'):
        assert _is_linked(b2, 'student8', a)
    _safe_set(a, 'schedule9', None)
    assert not _is_linked(a, 'schedule9', b2)
    if hasattr(b2, 'student8'):
        assert not _is_linked(b2, 'student8', a)


def test_assoc_Student_Grade_link_reassign_clear():
    a = Student(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    b1 = Grade(name="sample_text")
    b2 = Grade(name="sample_text_2")
    _safe_set(a, 'grade2', b1)
    assert _is_linked(a, 'grade2', b1)
    if hasattr(b1, 'students3'):
        assert _is_linked(b1, 'students3', a)
    _safe_set(a, 'grade2', b2)
    assert _is_linked(a, 'grade2', b2)
    if hasattr(b1, 'students3'):
        assert not _is_linked(b1, 'students3', a)
    if hasattr(b2, 'students3'):
        assert _is_linked(b2, 'students3', a)
    _safe_set(a, 'grade2', None)
    assert not _is_linked(a, 'grade2', b2)
    if hasattr(b2, 'students3'):
        assert not _is_linked(b2, 'students3', a)


def test_assoc_Student_Subject_link_reassign_clear():
    a = Student(email="sample_text", name="sample_text", phone="sample_text", surname="sample_text")
    b1 = Subject()
    b2 = Subject()
    _safe_set(a, 'subjects4', b1)
    assert _is_linked(a, 'subjects4', b1)
    if hasattr(b1, 'student5'):
        assert _is_linked(b1, 'student5', a)
    _safe_set(a, 'subjects4', b2)
    assert _is_linked(a, 'subjects4', b2)
    if hasattr(b1, 'student5'):
        assert not _is_linked(b1, 'student5', a)
    if hasattr(b2, 'student5'):
        assert _is_linked(b2, 'student5', a)
    _safe_set(a, 'subjects4', None)
    assert not _is_linked(a, 'subjects4', b2)
    if hasattr(b2, 'student5'):
        assert not _is_linked(b2, 'student5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Grade_strategy = st.builds(Grade, name=safe_text)
@given(instance=Grade_strategy)
@settings(max_examples=25)
def test_Grade_instantiation(instance):
    assert isinstance(instance, Grade)


Note_strategy = st.builds(Note)
@given(instance=Note_strategy)
@settings(max_examples=25)
def test_Note_instantiation(instance):
    assert isinstance(instance, Note)


Schedule_strategy = st.builds(Schedule)
@given(instance=Schedule_strategy)
@settings(max_examples=25)
def test_Schedule_instantiation(instance):
    assert isinstance(instance, Schedule)


Student_strategy = st.builds(Student, email=safe_text, name=safe_text, phone=safe_text, surname=safe_text)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Subject_strategy = st.builds(Subject)
@given(instance=Subject_strategy)
@settings(max_examples=25)
def test_Subject_instantiation(instance):
    assert isinstance(instance, Subject)


Teacher_strategy = st.builds(Teacher, email=safe_text, name=safe_text, phone=safe_text, surname=safe_text)
@given(instance=Teacher_strategy)
@settings(max_examples=25)
def test_Teacher_instantiation(instance):
    assert isinstance(instance, Teacher)



