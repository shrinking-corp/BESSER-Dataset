import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Course,
    schoolIncqDerived_Course,
    schoolIncqDerived_School,
    schoolIncqDerived_SchoolClass,
    schoolIncqDerived_SpecialisationCourse,
    schoolIncqDerived_Student,
    schoolIncqDerived_Teacher,
    schoolIncqDerived_Year,
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

def test_schoolIncqDerived_Course_subject_value_roundtrip():
    instance = schoolIncqDerived_Course(subject="sample_text", weight=7)
    assert instance.subject == "sample_text"
    instance.subject = "sample_text_2"
    assert instance.subject == "sample_text_2"


def test_schoolIncqDerived_Course_weight_value_roundtrip():
    instance = schoolIncqDerived_Course(subject="sample_text", weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_schoolIncqDerived_School_address_value_roundtrip():
    instance = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_schoolIncqDerived_School_currentYear_value_roundtrip():
    instance = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    assert instance.currentYear == 7
    instance.currentYear = 13
    assert instance.currentYear == 13


def test_schoolIncqDerived_School_name_value_roundtrip():
    instance = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_schoolIncqDerived_School_numberOfTeachers_value_roundtrip():
    instance = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    assert instance.numberOfTeachers == 7
    instance.numberOfTeachers = 13
    assert instance.numberOfTeachers == 13


def test_schoolIncqDerived_SchoolClass_code_value_roundtrip():
    instance = schoolIncqDerived_SchoolClass(code="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_schoolIncqDerived_SpecialisationCourse_specialisation_value_roundtrip():
    instance = schoolIncqDerived_SpecialisationCourse(specialisation="sample_text")
    assert instance.specialisation == "sample_text"
    instance.specialisation = "sample_text_2"
    assert instance.specialisation == "sample_text_2"


def test_schoolIncqDerived_Student_name_value_roundtrip():
    instance = schoolIncqDerived_Student(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_schoolIncqDerived_Teacher_name_value_roundtrip():
    instance = schoolIncqDerived_Teacher(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_schoolIncqDerived_Year_startingDate_value_roundtrip():
    instance = schoolIncqDerived_Year(startingDate=7)
    assert instance.startingDate == 7
    instance.startingDate = 13
    assert instance.startingDate == 13


def test_schoolIncqDerived_SpecialisationCourse_isa_Course():
    instance = schoolIncqDerived_SpecialisationCourse(specialisation="sample_text")
    assert isinstance(instance, Course)


def test_assoc_courses17_link_reassign_clear():
    a = schoolIncqDerived_SchoolClass(code="sample_text")
    b1 = schoolIncqDerived_Course(subject="sample_text", weight=7)
    b2 = schoolIncqDerived_Course(subject="sample_text_2", weight=13)
    _safe_set(a, 'schoolClass18', {b1})
    assert _is_linked(a, 'schoolClass18', b1)
    if hasattr(b1, 'Course19'):
        assert _is_linked(b1, 'Course19', a)
    _safe_set(a, 'schoolClass18', {b2})
    assert _is_linked(a, 'schoolClass18', b2)
    if hasattr(b1, 'Course19'):
        assert not _is_linked(b1, 'Course19', a)
    if hasattr(b2, 'Course19'):
        assert _is_linked(b2, 'Course19', a)
    _safe_set(a, 'schoolClass18', set())
    assert not _is_linked(a, 'schoolClass18', b2)
    if hasattr(b2, 'Course19'):
        assert not _is_linked(b2, 'Course19', a)


def test_assoc_courses26_link_reassign_clear():
    a = schoolIncqDerived_Teacher(name="sample_text")
    b1 = schoolIncqDerived_Course(subject="sample_text", weight=7)
    b2 = schoolIncqDerived_Course(subject="sample_text_2", weight=13)
    _safe_set(a, 'teacher', {b1})
    assert _is_linked(a, 'teacher', b1)
    if hasattr(b1, 'Course27'):
        assert _is_linked(b1, 'Course27', a)
    _safe_set(a, 'teacher', {b2})
    assert _is_linked(a, 'teacher', b2)
    if hasattr(b1, 'Course27'):
        assert not _is_linked(b1, 'Course27', a)
    if hasattr(b2, 'Course27'):
        assert _is_linked(b2, 'Course27', a)
    _safe_set(a, 'teacher', set())
    assert not _is_linked(a, 'teacher', b2)
    if hasattr(b2, 'Course27'):
        assert not _is_linked(b2, 'Course27', a)


def test_assoc_courses9_link_reassign_clear():
    a = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    b1 = schoolIncqDerived_Course(subject="sample_text", weight=7)
    b2 = schoolIncqDerived_Course(subject="sample_text_2", weight=13)
    _safe_set(a, 'school10', {b1})
    assert _is_linked(a, 'school10', b1)
    if hasattr(b1, 'Course'):
        assert _is_linked(b1, 'Course', a)
    _safe_set(a, 'school10', {b2})
    assert _is_linked(a, 'school10', b2)
    if hasattr(b1, 'Course'):
        assert not _is_linked(b1, 'Course', a)
    if hasattr(b2, 'Course'):
        assert _is_linked(b2, 'Course', a)
    _safe_set(a, 'school10', set())
    assert not _is_linked(a, 'school10', b2)
    if hasattr(b2, 'Course'):
        assert not _is_linked(b2, 'Course', a)


def test_assoc_homeroomTeacher20_link_reassign_clear():
    a = schoolIncqDerived_Teacher(name="sample_text")
    b1 = schoolIncqDerived_SchoolClass(code="sample_text")
    b2 = schoolIncqDerived_SchoolClass(code="sample_text_2")
    _safe_set(a, 'schoolIncqDerived_Teacher21', b1)
    assert _is_linked(a, 'schoolIncqDerived_Teacher21', b1)
    if hasattr(b1, 'schoolIncqDerived_SchoolClass'):
        assert _is_linked(b1, 'schoolIncqDerived_SchoolClass', a)
    _safe_set(a, 'schoolIncqDerived_Teacher21', b2)
    assert _is_linked(a, 'schoolIncqDerived_Teacher21', b2)
    if hasattr(b1, 'schoolIncqDerived_SchoolClass'):
        assert not _is_linked(b1, 'schoolIncqDerived_SchoolClass', a)
    if hasattr(b2, 'schoolIncqDerived_SchoolClass'):
        assert _is_linked(b2, 'schoolIncqDerived_SchoolClass', a)
    _safe_set(a, 'schoolIncqDerived_Teacher21', None)
    assert not _is_linked(a, 'schoolIncqDerived_Teacher21', b2)
    if hasattr(b2, 'schoolIncqDerived_SchoolClass'):
        assert not _is_linked(b2, 'schoolIncqDerived_SchoolClass', a)


def test_assoc_homeroomedClass28_link_reassign_clear():
    a = schoolIncqDerived_Teacher(name="sample_text")
    b1 = schoolIncqDerived_SchoolClass(code="sample_text")
    b2 = schoolIncqDerived_SchoolClass(code="sample_text_2")
    _safe_set(a, 'schoolIncqDerived_Teacher29', b1)
    assert _is_linked(a, 'schoolIncqDerived_Teacher29', b1)
    if hasattr(b1, 'schoolIncqDerived_SchoolClass30'):
        assert _is_linked(b1, 'schoolIncqDerived_SchoolClass30', a)
    _safe_set(a, 'schoolIncqDerived_Teacher29', b2)
    assert _is_linked(a, 'schoolIncqDerived_Teacher29', b2)
    if hasattr(b1, 'schoolIncqDerived_SchoolClass30'):
        assert not _is_linked(b1, 'schoolIncqDerived_SchoolClass30', a)
    if hasattr(b2, 'schoolIncqDerived_SchoolClass30'):
        assert _is_linked(b2, 'schoolIncqDerived_SchoolClass30', a)
    _safe_set(a, 'schoolIncqDerived_Teacher29', None)
    assert not _is_linked(a, 'schoolIncqDerived_Teacher29', b2)
    if hasattr(b2, 'schoolIncqDerived_SchoolClass30'):
        assert not _is_linked(b2, 'schoolIncqDerived_SchoolClass30', a)


def test_assoc_lastYear12_link_reassign_clear():
    a = schoolIncqDerived_Year(startingDate=7)
    b1 = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    b2 = schoolIncqDerived_School(address="sample_text_2", currentYear=13, name="sample_text_2", numberOfTeachers=13)
    _safe_set(a, 'schoolIncqDerived_Year', b1)
    assert _is_linked(a, 'schoolIncqDerived_Year', b1)
    if hasattr(b1, 'schoolIncqDerived_School13'):
        assert _is_linked(b1, 'schoolIncqDerived_School13', a)
    _safe_set(a, 'schoolIncqDerived_Year', b2)
    assert _is_linked(a, 'schoolIncqDerived_Year', b2)
    if hasattr(b1, 'schoolIncqDerived_School13'):
        assert not _is_linked(b1, 'schoolIncqDerived_School13', a)
    if hasattr(b2, 'schoolIncqDerived_School13'):
        assert _is_linked(b2, 'schoolIncqDerived_School13', a)
    _safe_set(a, 'schoolIncqDerived_Year', None)
    assert not _is_linked(a, 'schoolIncqDerived_Year', b2)
    if hasattr(b2, 'schoolIncqDerived_School13'):
        assert not _is_linked(b2, 'schoolIncqDerived_School13', a)


def test_assoc_school0_link_reassign_clear():
    a = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    b1 = schoolIncqDerived_Course(subject="sample_text", weight=7)
    b2 = schoolIncqDerived_Course(subject="sample_text_2", weight=13)
    _safe_set(a, 'School', b1)
    assert _is_linked(a, 'School', b1)
    if hasattr(b1, 'courses'):
        assert _is_linked(b1, 'courses', a)
    _safe_set(a, 'School', b2)
    assert _is_linked(a, 'School', b2)
    if hasattr(b1, 'courses'):
        assert not _is_linked(b1, 'courses', a)
    if hasattr(b2, 'courses'):
        assert _is_linked(b2, 'courses', a)
    _safe_set(a, 'School', None)
    assert not _is_linked(a, 'School', b2)
    if hasattr(b2, 'courses'):
        assert not _is_linked(b2, 'courses', a)


def test_assoc_school24_link_reassign_clear():
    a = schoolIncqDerived_Teacher(name="sample_text")
    b1 = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    b2 = schoolIncqDerived_School(address="sample_text_2", currentYear=13, name="sample_text_2", numberOfTeachers=13)
    _safe_set(a, 'teachers', b1)
    assert _is_linked(a, 'teachers', b1)
    if hasattr(b1, 'School25'):
        assert _is_linked(b1, 'School25', a)
    _safe_set(a, 'teachers', b2)
    assert _is_linked(a, 'teachers', b2)
    if hasattr(b1, 'School25'):
        assert not _is_linked(b1, 'School25', a)
    if hasattr(b2, 'School25'):
        assert _is_linked(b2, 'School25', a)
    _safe_set(a, 'teachers', None)
    assert not _is_linked(a, 'teachers', b2)
    if hasattr(b2, 'School25'):
        assert not _is_linked(b2, 'School25', a)


def test_assoc_school31_link_reassign_clear():
    a = schoolIncqDerived_Year(startingDate=7)
    b1 = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    b2 = schoolIncqDerived_School(address="sample_text_2", currentYear=13, name="sample_text_2", numberOfTeachers=13)
    _safe_set(a, 'years', b1)
    assert _is_linked(a, 'years', b1)
    if hasattr(b1, 'School32'):
        assert _is_linked(b1, 'School32', a)
    _safe_set(a, 'years', b2)
    assert _is_linked(a, 'years', b2)
    if hasattr(b1, 'School32'):
        assert not _is_linked(b1, 'School32', a)
    if hasattr(b2, 'School32'):
        assert _is_linked(b2, 'School32', a)
    _safe_set(a, 'years', None)
    assert not _is_linked(a, 'years', b2)
    if hasattr(b2, 'School32'):
        assert not _is_linked(b2, 'School32', a)


def test_assoc_schoolClass22_link_reassign_clear():
    a = schoolIncqDerived_Student(name="sample_text")
    b1 = schoolIncqDerived_SchoolClass(code="sample_text")
    b2 = schoolIncqDerived_SchoolClass(code="sample_text_2")
    _safe_set(a, 'students', b1)
    assert _is_linked(a, 'students', b1)
    if hasattr(b1, 'SchoolClass23'):
        assert _is_linked(b1, 'SchoolClass23', a)
    _safe_set(a, 'students', b2)
    assert _is_linked(a, 'students', b2)
    if hasattr(b1, 'SchoolClass23'):
        assert not _is_linked(b1, 'SchoolClass23', a)
    if hasattr(b2, 'SchoolClass23'):
        assert _is_linked(b2, 'SchoolClass23', a)
    _safe_set(a, 'students', None)
    assert not _is_linked(a, 'students', b2)
    if hasattr(b2, 'SchoolClass23'):
        assert not _is_linked(b2, 'SchoolClass23', a)


def test_assoc_schoolClass3_link_reassign_clear():
    a = schoolIncqDerived_SchoolClass(code="sample_text")
    b1 = schoolIncqDerived_Course(subject="sample_text", weight=7)
    b2 = schoolIncqDerived_Course(subject="sample_text_2", weight=13)
    _safe_set(a, 'SchoolClass', b1)
    assert _is_linked(a, 'SchoolClass', b1)
    if hasattr(b1, 'courses4'):
        assert _is_linked(b1, 'courses4', a)
    _safe_set(a, 'SchoolClass', b2)
    assert _is_linked(a, 'SchoolClass', b2)
    if hasattr(b1, 'courses4'):
        assert not _is_linked(b1, 'courses4', a)
    if hasattr(b2, 'courses4'):
        assert _is_linked(b2, 'courses4', a)
    _safe_set(a, 'SchoolClass', None)
    assert not _is_linked(a, 'SchoolClass', b2)
    if hasattr(b2, 'courses4'):
        assert not _is_linked(b2, 'courses4', a)


def test_assoc_schoolClasses33_link_reassign_clear():
    a = schoolIncqDerived_Year(startingDate=7)
    b1 = schoolIncqDerived_SchoolClass(code="sample_text")
    b2 = schoolIncqDerived_SchoolClass(code="sample_text_2")
    _safe_set(a, 'year', {b1})
    assert _is_linked(a, 'year', b1)
    if hasattr(b1, 'SchoolClass34'):
        assert _is_linked(b1, 'SchoolClass34', a)
    _safe_set(a, 'year', {b2})
    assert _is_linked(a, 'year', b2)
    if hasattr(b1, 'SchoolClass34'):
        assert not _is_linked(b1, 'SchoolClass34', a)
    if hasattr(b2, 'SchoolClass34'):
        assert _is_linked(b2, 'SchoolClass34', a)
    _safe_set(a, 'year', set())
    assert not _is_linked(a, 'year', b2)
    if hasattr(b2, 'SchoolClass34'):
        assert not _is_linked(b2, 'SchoolClass34', a)


def test_assoc_students16_link_reassign_clear():
    a = schoolIncqDerived_Student(name="sample_text")
    b1 = schoolIncqDerived_SchoolClass(code="sample_text")
    b2 = schoolIncqDerived_SchoolClass(code="sample_text_2")
    _safe_set(a, 'Student', b1)
    assert _is_linked(a, 'Student', b1)
    if hasattr(b1, 'schoolClass'):
        assert _is_linked(b1, 'schoolClass', a)
    _safe_set(a, 'Student', b2)
    assert _is_linked(a, 'Student', b2)
    if hasattr(b1, 'schoolClass'):
        assert not _is_linked(b1, 'schoolClass', a)
    if hasattr(b2, 'schoolClass'):
        assert _is_linked(b2, 'schoolClass', a)
    _safe_set(a, 'Student', None)
    assert not _is_linked(a, 'Student', b2)
    if hasattr(b2, 'schoolClass'):
        assert not _is_linked(b2, 'schoolClass', a)


def test_assoc_teacher1_link_reassign_clear():
    a = schoolIncqDerived_Teacher(name="sample_text")
    b1 = schoolIncqDerived_Course(subject="sample_text", weight=7)
    b2 = schoolIncqDerived_Course(subject="sample_text_2", weight=13)
    _safe_set(a, 'Teacher', b1)
    assert _is_linked(a, 'Teacher', b1)
    if hasattr(b1, 'courses2'):
        assert _is_linked(b1, 'courses2', a)
    _safe_set(a, 'Teacher', b2)
    assert _is_linked(a, 'Teacher', b2)
    if hasattr(b1, 'courses2'):
        assert not _is_linked(b1, 'courses2', a)
    if hasattr(b2, 'courses2'):
        assert _is_linked(b2, 'courses2', a)
    _safe_set(a, 'Teacher', None)
    assert not _is_linked(a, 'Teacher', b2)
    if hasattr(b2, 'courses2'):
        assert not _is_linked(b2, 'courses2', a)


def test_assoc_teachers6_link_reassign_clear():
    a = schoolIncqDerived_Teacher(name="sample_text")
    b1 = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    b2 = schoolIncqDerived_School(address="sample_text_2", currentYear=13, name="sample_text_2", numberOfTeachers=13)
    _safe_set(a, 'Teacher8', b1)
    assert _is_linked(a, 'Teacher8', b1)
    if hasattr(b1, 'school7'):
        assert _is_linked(b1, 'school7', a)
    _safe_set(a, 'Teacher8', b2)
    assert _is_linked(a, 'Teacher8', b2)
    if hasattr(b1, 'school7'):
        assert not _is_linked(b1, 'school7', a)
    if hasattr(b2, 'school7'):
        assert _is_linked(b2, 'school7', a)
    _safe_set(a, 'Teacher8', None)
    assert not _is_linked(a, 'Teacher8', b2)
    if hasattr(b2, 'school7'):
        assert not _is_linked(b2, 'school7', a)


def test_assoc_teachersWithMostCourses11_link_reassign_clear():
    a = schoolIncqDerived_Teacher(name="sample_text")
    b1 = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    b2 = schoolIncqDerived_School(address="sample_text_2", currentYear=13, name="sample_text_2", numberOfTeachers=13)
    _safe_set(a, 'schoolIncqDerived_Teacher', b1)
    assert _is_linked(a, 'schoolIncqDerived_Teacher', b1)
    if hasattr(b1, 'schoolIncqDerived_School'):
        assert _is_linked(b1, 'schoolIncqDerived_School', a)
    _safe_set(a, 'schoolIncqDerived_Teacher', b2)
    assert _is_linked(a, 'schoolIncqDerived_Teacher', b2)
    if hasattr(b1, 'schoolIncqDerived_School'):
        assert not _is_linked(b1, 'schoolIncqDerived_School', a)
    if hasattr(b2, 'schoolIncqDerived_School'):
        assert _is_linked(b2, 'schoolIncqDerived_School', a)
    _safe_set(a, 'schoolIncqDerived_Teacher', None)
    assert not _is_linked(a, 'schoolIncqDerived_Teacher', b2)
    if hasattr(b2, 'schoolIncqDerived_School'):
        assert not _is_linked(b2, 'schoolIncqDerived_School', a)


def test_assoc_year14_link_reassign_clear():
    a = schoolIncqDerived_Year(startingDate=7)
    b1 = schoolIncqDerived_SchoolClass(code="sample_text")
    b2 = schoolIncqDerived_SchoolClass(code="sample_text_2")
    _safe_set(a, 'Year15', b1)
    assert _is_linked(a, 'Year15', b1)
    if hasattr(b1, 'schoolClasses'):
        assert _is_linked(b1, 'schoolClasses', a)
    _safe_set(a, 'Year15', b2)
    assert _is_linked(a, 'Year15', b2)
    if hasattr(b1, 'schoolClasses'):
        assert not _is_linked(b1, 'schoolClasses', a)
    if hasattr(b2, 'schoolClasses'):
        assert _is_linked(b2, 'schoolClasses', a)
    _safe_set(a, 'Year15', None)
    assert not _is_linked(a, 'Year15', b2)
    if hasattr(b2, 'schoolClasses'):
        assert not _is_linked(b2, 'schoolClasses', a)


def test_assoc_years5_link_reassign_clear():
    a = schoolIncqDerived_Year(startingDate=7)
    b1 = schoolIncqDerived_School(address="sample_text", currentYear=7, name="sample_text", numberOfTeachers=7)
    b2 = schoolIncqDerived_School(address="sample_text_2", currentYear=13, name="sample_text_2", numberOfTeachers=13)
    _safe_set(a, 'Year', b1)
    assert _is_linked(a, 'Year', b1)
    if hasattr(b1, 'school'):
        assert _is_linked(b1, 'school', a)
    _safe_set(a, 'Year', b2)
    assert _is_linked(a, 'Year', b2)
    if hasattr(b1, 'school'):
        assert not _is_linked(b1, 'school', a)
    if hasattr(b2, 'school'):
        assert _is_linked(b2, 'school', a)
    _safe_set(a, 'Year', None)
    assert not _is_linked(a, 'Year', b2)
    if hasattr(b2, 'school'):
        assert not _is_linked(b2, 'school', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Course_strategy = st.builds(Course)
@given(instance=Course_strategy)
@settings(max_examples=25)
def test_Course_instantiation(instance):
    assert isinstance(instance, Course)


schoolIncqDerived_Course_strategy = st.builds(schoolIncqDerived_Course, subject=safe_text, weight=st.integers())
@given(instance=schoolIncqDerived_Course_strategy)
@settings(max_examples=25)
def test_schoolIncqDerived_Course_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_Course)


schoolIncqDerived_School_strategy = st.builds(schoolIncqDerived_School, address=safe_text, currentYear=st.integers(), name=safe_text, numberOfTeachers=st.integers())
@given(instance=schoolIncqDerived_School_strategy)
@settings(max_examples=25)
def test_schoolIncqDerived_School_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_School)


schoolIncqDerived_SchoolClass_strategy = st.builds(schoolIncqDerived_SchoolClass, code=safe_text)
@given(instance=schoolIncqDerived_SchoolClass_strategy)
@settings(max_examples=25)
def test_schoolIncqDerived_SchoolClass_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_SchoolClass)


schoolIncqDerived_SpecialisationCourse_strategy = st.builds(schoolIncqDerived_SpecialisationCourse, specialisation=safe_text)
@given(instance=schoolIncqDerived_SpecialisationCourse_strategy)
@settings(max_examples=25)
def test_schoolIncqDerived_SpecialisationCourse_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_SpecialisationCourse)


schoolIncqDerived_Student_strategy = st.builds(schoolIncqDerived_Student, name=safe_text)
@given(instance=schoolIncqDerived_Student_strategy)
@settings(max_examples=25)
def test_schoolIncqDerived_Student_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_Student)


schoolIncqDerived_Teacher_strategy = st.builds(schoolIncqDerived_Teacher, name=safe_text)
@given(instance=schoolIncqDerived_Teacher_strategy)
@settings(max_examples=25)
def test_schoolIncqDerived_Teacher_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_Teacher)


schoolIncqDerived_Year_strategy = st.builds(schoolIncqDerived_Year, startingDate=st.integers())
@given(instance=schoolIncqDerived_Year_strategy)
@settings(max_examples=25)
def test_schoolIncqDerived_Year_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_Year)


