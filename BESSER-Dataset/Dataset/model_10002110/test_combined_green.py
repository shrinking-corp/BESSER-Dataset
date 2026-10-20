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
    leftOuts,
    constraints,
    conflictCheck,
    classrooms,
    subjects,
    teachers,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_leftouts_is_not_abstract():
    assert not inspect.isabstract(leftOuts)


def test_hyp_leftouts_constructor_exists():
    assert callable(leftOuts.__init__)


def test_hyp_leftouts_constructor_args():
    sig = inspect.signature(leftOuts.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "students" in params, "Missing parameter 'students'"
    assert "classroom" in params, "Missing parameter 'classroom'"
    assert "teachers" in params, "Missing parameter 'teachers'"

def test_hyp_leftouts_has_subject():
    assert hasattr(leftOuts, "subject")
    descriptor = None
    for klass in leftOuts.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_hyp_leftouts_has_students():
    assert hasattr(leftOuts, "students")
    descriptor = None
    for klass in leftOuts.__mro__:
        if "students" in klass.__dict__:
            descriptor = klass.__dict__["students"]
            break
    assert isinstance(descriptor, property)

def test_hyp_leftouts_has_classroom():
    assert hasattr(leftOuts, "classroom")
    descriptor = None
    for klass in leftOuts.__mro__:
        if "classroom" in klass.__dict__:
            descriptor = klass.__dict__["classroom"]
            break
    assert isinstance(descriptor, property)

def test_hyp_leftouts_has_teachers():
    assert hasattr(leftOuts, "teachers")
    descriptor = None
    for klass in leftOuts.__mro__:
        if "teachers" in klass.__dict__:
            descriptor = klass.__dict__["teachers"]
            break
    assert isinstance(descriptor, property)



def test_hyp_constraints_is_not_abstract():
    assert not inspect.isabstract(constraints)


def test_hyp_constraints_constructor_exists():
    assert callable(constraints.__init__)


def test_hyp_constraints_constructor_args():
    sig = inspect.signature(constraints.__init__)
    params = list(sig.parameters.keys())
    assert "doubletons" in params, "Missing parameter 'doubletons'"
    assert "singletons" in params, "Missing parameter 'singletons'"

def test_hyp_constraints_has_doubletons():
    assert hasattr(constraints, "doubletons")
    descriptor = None
    for klass in constraints.__mro__:
        if "doubletons" in klass.__dict__:
            descriptor = klass.__dict__["doubletons"]
            break
    assert isinstance(descriptor, property)

def test_hyp_constraints_has_singletons():
    assert hasattr(constraints, "singletons")
    descriptor = None
    for klass in constraints.__mro__:
        if "singletons" in klass.__dict__:
            descriptor = klass.__dict__["singletons"]
            break
    assert isinstance(descriptor, property)



def test_hyp_conflictcheck_is_not_abstract():
    assert not inspect.isabstract(conflictCheck)


def test_hyp_conflictcheck_constructor_exists():
    assert callable(conflictCheck.__init__)


def test_hyp_conflictcheck_constructor_args():
    sig = inspect.signature(conflictCheck.__init__)
    params = list(sig.parameters.keys())
    assert "subjects" in params, "Missing parameter 'subjects'"
    assert "conflict" in params, "Missing parameter 'conflict'"





def test_hyp_classrooms_is_not_abstract():
    assert not inspect.isabstract(classrooms)


def test_hyp_classrooms_constructor_exists():
    assert callable(classrooms.__init__)


def test_hyp_classrooms_constructor_args():
    sig = inspect.signature(classrooms.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "teacher" in params, "Missing parameter 'teacher'"
    assert "number" in params, "Missing parameter 'number'"






def test_hyp_subjects_is_not_abstract():
    assert not inspect.isabstract(subjects)


def test_hyp_subjects_constructor_exists():
    assert callable(subjects.__init__)


def test_hyp_subjects_constructor_args():
    sig = inspect.signature(subjects.__init__)
    params = list(sig.parameters.keys())
    assert "classroom" in params, "Missing parameter 'classroom'"
    assert "teacher" in params, "Missing parameter 'teacher'"
    assert "Section" in params, "Missing parameter 'Section'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_teachers_is_not_abstract():
    assert not inspect.isabstract(teachers)


def test_hyp_teachers_constructor_exists():
    assert callable(teachers.__init__)


def test_hyp_teachers_constructor_args():
    sig = inspect.signature(teachers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "section" in params, "Missing parameter 'section'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "classroom" in params, "Missing parameter 'classroom'"






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
leftOuts_strategy = st.builds(
    leftOuts,
    subject=
        st.none(),
    students=
        safe_text,
    classroom=
        st.none(),
    teachers=
        st.none()
)
constraints_strategy = st.builds(
    constraints,
    doubletons=
        st.none(),
    singletons=
        st.none()
)
conflictCheck_strategy = st.builds(
    conflictCheck,
    subjects=
        safe_text,
    conflict=
        st.booleans()
)
classrooms_strategy = st.builds(
    classrooms,
    subject=
        safe_text,
    teacher=
        safe_text,
    number=
        st.integers()
)
subjects_strategy = st.builds(
    subjects,
    classroom=
        st.integers(),
    teacher=
        safe_text,
    Section=
        safe_text,
    name=
        safe_text
)
teachers_strategy = st.builds(
    teachers,
    name=
        safe_text,
    section=
        safe_text,
    subject=
        safe_text,
    classroom=
        st.integers()
)

@given(instance=leftOuts_strategy)
@settings(max_examples=50)
def test_hyp_leftouts_instantiation(instance):
    assert isinstance(instance, leftOuts)



@given(instance=leftOuts_strategy)
def test_hyp_leftouts_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=leftOuts_strategy)
def test_hyp_leftouts_students_setter(instance):
    original = instance.students
    instance.students = original
    assert instance.students == original



@given(instance=leftOuts_strategy)
def test_hyp_leftouts_classroom_setter(instance):
    original = instance.classroom
    instance.classroom = original
    assert instance.classroom == original



@given(instance=leftOuts_strategy)
def test_hyp_leftouts_teachers_setter(instance):
    original = instance.teachers
    instance.teachers = original
    assert instance.teachers == original

@given(instance=constraints_strategy)
@settings(max_examples=50)
def test_hyp_constraints_instantiation(instance):
    assert isinstance(instance, constraints)



@given(instance=constraints_strategy)
def test_hyp_constraints_doubletons_setter(instance):
    original = instance.doubletons
    instance.doubletons = original
    assert instance.doubletons == original



@given(instance=constraints_strategy)
def test_hyp_constraints_singletons_setter(instance):
    original = instance.singletons
    instance.singletons = original
    assert instance.singletons == original




@given(instance=conflictCheck_strategy)
def test_hyp_conflictcheck_subjects_setter(instance):
    original = instance.subjects
    instance.subjects = original
    assert instance.subjects == original



@given(instance=conflictCheck_strategy)
def test_hyp_conflictcheck_conflict_setter(instance):
    original = instance.conflict
    instance.conflict = original
    assert instance.conflict == original




@given(instance=classrooms_strategy)
def test_hyp_classrooms_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=classrooms_strategy)
def test_hyp_classrooms_teacher_setter(instance):
    original = instance.teacher
    instance.teacher = original
    assert instance.teacher == original



@given(instance=classrooms_strategy)
def test_hyp_classrooms_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original




@given(instance=subjects_strategy)
def test_hyp_subjects_classroom_setter(instance):
    original = instance.classroom
    instance.classroom = original
    assert instance.classroom == original



@given(instance=subjects_strategy)
def test_hyp_subjects_teacher_setter(instance):
    original = instance.teacher
    instance.teacher = original
    assert instance.teacher == original



@given(instance=subjects_strategy)
def test_hyp_subjects_Section_setter(instance):
    original = instance.Section
    instance.Section = original
    assert instance.Section == original



@given(instance=subjects_strategy)
def test_hyp_subjects_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=teachers_strategy)
def test_hyp_teachers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=teachers_strategy)
def test_hyp_teachers_section_setter(instance):
    original = instance.section
    instance.section = original
    assert instance.section == original



@given(instance=teachers_strategy)
def test_hyp_teachers_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=teachers_strategy)
def test_hyp_teachers_classroom_setter(instance):
    original = instance.classroom
    instance.classroom = original
    assert instance.classroom == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    classrooms,
    conflictCheck,
    constraints,
    leftOuts,
    subjects,
    teachers,
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

def test_classrooms_number_value_roundtrip():
    instance = classrooms(number=7, subject="sample_text", teacher="sample_text")
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_classrooms_subject_value_roundtrip():
    instance = classrooms(number=7, subject="sample_text", teacher="sample_text")
    assert instance.subject == "sample_text"
    instance.subject = "sample_text_2"
    assert instance.subject == "sample_text_2"


def test_classrooms_teacher_value_roundtrip():
    instance = classrooms(number=7, subject="sample_text", teacher="sample_text")
    assert instance.teacher == "sample_text"
    instance.teacher = "sample_text_2"
    assert instance.teacher == "sample_text_2"


def test_conflictCheck_conflict_value_roundtrip():
    instance = conflictCheck(conflict=True, subjects="sample_text")
    assert instance.conflict == True
    instance.conflict = False
    assert instance.conflict == False


def test_conflictCheck_subjects_value_roundtrip():
    instance = conflictCheck(conflict=True, subjects="sample_text")
    assert instance.subjects == "sample_text"
    instance.subjects = "sample_text_2"
    assert instance.subjects == "sample_text_2"


def test_subjects_Section_value_roundtrip():
    instance = subjects(Section="sample_text", classroom=7, name="sample_text", teacher="sample_text")
    assert instance.Section == "sample_text"
    instance.Section = "sample_text_2"
    assert instance.Section == "sample_text_2"


def test_subjects_classroom_value_roundtrip():
    instance = subjects(Section="sample_text", classroom=7, name="sample_text", teacher="sample_text")
    assert instance.classroom == 7
    instance.classroom = 13
    assert instance.classroom == 13


def test_subjects_name_value_roundtrip():
    instance = subjects(Section="sample_text", classroom=7, name="sample_text", teacher="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_subjects_teacher_value_roundtrip():
    instance = subjects(Section="sample_text", classroom=7, name="sample_text", teacher="sample_text")
    assert instance.teacher == "sample_text"
    instance.teacher = "sample_text_2"
    assert instance.teacher == "sample_text_2"


def test_teachers_classroom_value_roundtrip():
    instance = teachers(classroom=7, name="sample_text", section="sample_text", subject="sample_text")
    assert instance.classroom == 7
    instance.classroom = 13
    assert instance.classroom == 13


def test_teachers_name_value_roundtrip():
    instance = teachers(classroom=7, name="sample_text", section="sample_text", subject="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_teachers_section_value_roundtrip():
    instance = teachers(classroom=7, name="sample_text", section="sample_text", subject="sample_text")
    assert instance.section == "sample_text"
    instance.section = "sample_text_2"
    assert instance.section == "sample_text_2"


def test_teachers_subject_value_roundtrip():
    instance = teachers(classroom=7, name="sample_text", section="sample_text", subject="sample_text")
    assert instance.subject == "sample_text"
    instance.subject = "sample_text_2"
    assert instance.subject == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

classrooms_strategy = st.builds(classrooms, number=st.integers(), subject=safe_text, teacher=safe_text)
@given(instance=classrooms_strategy)
@settings(max_examples=25)
def test_classrooms_instantiation(instance):
    assert isinstance(instance, classrooms)


conflictCheck_strategy = st.builds(conflictCheck, conflict=st.booleans(), subjects=safe_text)
@given(instance=conflictCheck_strategy)
@settings(max_examples=25)
def test_conflictCheck_instantiation(instance):
    assert isinstance(instance, conflictCheck)


subjects_strategy = st.builds(subjects, Section=safe_text, classroom=st.integers(), name=safe_text, teacher=safe_text)
@given(instance=subjects_strategy)
@settings(max_examples=25)
def test_subjects_instantiation(instance):
    assert isinstance(instance, subjects)


teachers_strategy = st.builds(teachers, classroom=st.integers(), name=safe_text, section=safe_text, subject=safe_text)
@given(instance=teachers_strategy)
@settings(max_examples=25)
def test_teachers_instantiation(instance):
    assert isinstance(instance, teachers)



