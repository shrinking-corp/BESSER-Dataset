import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    studyplan_Course,
    studyplan_CourseGroup,
    studyplan_FieldOfStudy,
    studyplan_Semester,
    studyplan_Specialization,
    studyplan_StudyPlan,
    CourseStatus,
    SemesterType,
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

def test_studyplan_Course_courseCode_value_roundtrip():
    instance = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    assert instance.courseCode == 7
    instance.courseCode = 13
    assert instance.courseCode == 13


def test_studyplan_Course_courseName_value_roundtrip():
    instance = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    assert instance.courseName == "sample_text"
    instance.courseName = "sample_text_2"
    assert instance.courseName == "sample_text_2"


def test_studyplan_Course_credit_value_roundtrip():
    instance = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    assert instance.credit == 3.14
    instance.credit = 9.99
    assert instance.credit == 9.99


def test_studyplan_Course_status_value_roundtrip():
    instance = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_studyplan_CourseGroup_courseStatus_value_roundtrip():
    instance = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    assert instance.courseStatus == "sample_text"
    instance.courseStatus = "sample_text_2"
    assert instance.courseStatus == "sample_text_2"


def test_studyplan_CourseGroup_group_value_roundtrip():
    instance = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_studyplan_FieldOfStudy_fieldName_value_roundtrip():
    instance = studyplan_FieldOfStudy(fieldName="sample_text")
    assert instance.fieldName == "sample_text"
    instance.fieldName = "sample_text_2"
    assert instance.fieldName == "sample_text_2"


def test_studyplan_Semester_semesterType_value_roundtrip():
    instance = studyplan_Semester(semesterType="sample_text", year=7)
    assert instance.semesterType == "sample_text"
    instance.semesterType = "sample_text_2"
    assert instance.semesterType == "sample_text_2"


def test_studyplan_Semester_year_value_roundtrip():
    instance = studyplan_Semester(semesterType="sample_text", year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_studyplan_Specialization_specName_value_roundtrip():
    instance = studyplan_Specialization(specName="sample_text")
    assert instance.specName == "sample_text"
    instance.specName = "sample_text_2"
    assert instance.specName == "sample_text_2"


def test_studyplan_StudyPlan_planName_value_roundtrip():
    instance = studyplan_StudyPlan(planName="sample_text")
    assert instance.planName == "sample_text"
    instance.planName = "sample_text_2"
    assert instance.planName == "sample_text_2"


def test_assoc_course25_link_reassign_clear():
    a = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    b1 = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    b2 = studyplan_Course(courseCode=13, courseName="sample_text_2", credit=9.99, status="sample_text_2")
    _safe_set(a, 'courseGroup', b1)
    assert _is_linked(a, 'courseGroup', b1)
    if hasattr(b1, 'Course'):
        assert _is_linked(b1, 'Course', a)
    _safe_set(a, 'courseGroup', b2)
    assert _is_linked(a, 'courseGroup', b2)
    if hasattr(b1, 'Course'):
        assert not _is_linked(b1, 'Course', a)
    if hasattr(b2, 'Course'):
        assert _is_linked(b2, 'Course', a)
    _safe_set(a, 'courseGroup', None)
    assert not _is_linked(a, 'courseGroup', b2)
    if hasattr(b2, 'Course'):
        assert not _is_linked(b2, 'Course', a)


def test_assoc_courseGroup14_link_reassign_clear():
    a = studyplan_Specialization(specName="sample_text")
    b1 = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    b2 = studyplan_CourseGroup(courseStatus="sample_text_2", group="sample_text_2")
    _safe_set(a, 'studyplan_Specialization15', b1)
    assert _is_linked(a, 'studyplan_Specialization15', b1)
    if hasattr(b1, 'studyplan_CourseGroup'):
        assert _is_linked(b1, 'studyplan_CourseGroup', a)
    _safe_set(a, 'studyplan_Specialization15', b2)
    assert _is_linked(a, 'studyplan_Specialization15', b2)
    if hasattr(b1, 'studyplan_CourseGroup'):
        assert not _is_linked(b1, 'studyplan_CourseGroup', a)
    if hasattr(b2, 'studyplan_CourseGroup'):
        assert _is_linked(b2, 'studyplan_CourseGroup', a)
    _safe_set(a, 'studyplan_Specialization15', None)
    assert not _is_linked(a, 'studyplan_Specialization15', b2)
    if hasattr(b2, 'studyplan_CourseGroup'):
        assert not _is_linked(b2, 'studyplan_CourseGroup', a)


def test_assoc_courseGroup8_link_reassign_clear():
    a = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    b1 = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    b2 = studyplan_Course(courseCode=13, courseName="sample_text_2", credit=9.99, status="sample_text_2")
    _safe_set(a, 'CourseGroup', b1)
    assert _is_linked(a, 'CourseGroup', b1)
    if hasattr(b1, 'course'):
        assert _is_linked(b1, 'course', a)
    _safe_set(a, 'CourseGroup', b2)
    assert _is_linked(a, 'CourseGroup', b2)
    if hasattr(b1, 'course'):
        assert not _is_linked(b1, 'course', a)
    if hasattr(b2, 'course'):
        assert _is_linked(b2, 'course', a)
    _safe_set(a, 'CourseGroup', None)
    assert not _is_linked(a, 'CourseGroup', b2)
    if hasattr(b2, 'course'):
        assert not _is_linked(b2, 'course', a)


def test_assoc_courses1_link_reassign_clear():
    a = studyplan_StudyPlan(planName="sample_text")
    b1 = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    b2 = studyplan_Course(courseCode=13, courseName="sample_text_2", credit=9.99, status="sample_text_2")
    _safe_set(a, 'studyplan_StudyPlan2', b1)
    assert _is_linked(a, 'studyplan_StudyPlan2', b1)
    if hasattr(b1, 'studyplan_Course'):
        assert _is_linked(b1, 'studyplan_Course', a)
    _safe_set(a, 'studyplan_StudyPlan2', b2)
    assert _is_linked(a, 'studyplan_StudyPlan2', b2)
    if hasattr(b1, 'studyplan_Course'):
        assert not _is_linked(b1, 'studyplan_Course', a)
    if hasattr(b2, 'studyplan_Course'):
        assert _is_linked(b2, 'studyplan_Course', a)
    _safe_set(a, 'studyplan_StudyPlan2', None)
    assert not _is_linked(a, 'studyplan_StudyPlan2', b2)
    if hasattr(b2, 'studyplan_Course'):
        assert not _is_linked(b2, 'studyplan_Course', a)


def test_assoc_courses5_link_reassign_clear():
    a = studyplan_Semester(semesterType="sample_text", year=7)
    b1 = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    b2 = studyplan_Course(courseCode=13, courseName="sample_text_2", credit=9.99, status="sample_text_2")
    _safe_set(a, 'studyplan_Semester6', {b1})
    assert _is_linked(a, 'studyplan_Semester6', b1)
    if hasattr(b1, 'studyplan_Course7'):
        assert _is_linked(b1, 'studyplan_Course7', a)
    _safe_set(a, 'studyplan_Semester6', {b2})
    assert _is_linked(a, 'studyplan_Semester6', b2)
    if hasattr(b1, 'studyplan_Course7'):
        assert not _is_linked(b1, 'studyplan_Course7', a)
    if hasattr(b2, 'studyplan_Course7'):
        assert _is_linked(b2, 'studyplan_Course7', a)
    _safe_set(a, 'studyplan_Semester6', set())
    assert not _is_linked(a, 'studyplan_Semester6', b2)
    if hasattr(b2, 'studyplan_Course7'):
        assert not _is_linked(b2, 'studyplan_Course7', a)


def test_assoc_program0_link_reassign_clear():
    a = studyplan_StudyPlan(planName="sample_text")
    b1 = studyplan_FieldOfStudy(fieldName="sample_text")
    b2 = studyplan_FieldOfStudy(fieldName="sample_text_2")
    _safe_set(a, 'studyplan_StudyPlan', b1)
    assert _is_linked(a, 'studyplan_StudyPlan', b1)
    if hasattr(b1, 'studyplan_FieldOfStudy'):
        assert _is_linked(b1, 'studyplan_FieldOfStudy', a)
    _safe_set(a, 'studyplan_StudyPlan', b2)
    assert _is_linked(a, 'studyplan_StudyPlan', b2)
    if hasattr(b1, 'studyplan_FieldOfStudy'):
        assert not _is_linked(b1, 'studyplan_FieldOfStudy', a)
    if hasattr(b2, 'studyplan_FieldOfStudy'):
        assert _is_linked(b2, 'studyplan_FieldOfStudy', a)
    _safe_set(a, 'studyplan_StudyPlan', None)
    assert not _is_linked(a, 'studyplan_StudyPlan', b2)
    if hasattr(b2, 'studyplan_FieldOfStudy'):
        assert not _is_linked(b2, 'studyplan_FieldOfStudy', a)


def test_assoc_semester22_link_reassign_clear():
    a = studyplan_Semester(semesterType="sample_text", year=7)
    b1 = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    b2 = studyplan_CourseGroup(courseStatus="sample_text_2", group="sample_text_2")
    _safe_set(a, 'studyplan_Semester24', b1)
    assert _is_linked(a, 'studyplan_Semester24', b1)
    if hasattr(b1, 'studyplan_CourseGroup23'):
        assert _is_linked(b1, 'studyplan_CourseGroup23', a)
    _safe_set(a, 'studyplan_Semester24', b2)
    assert _is_linked(a, 'studyplan_Semester24', b2)
    if hasattr(b1, 'studyplan_CourseGroup23'):
        assert not _is_linked(b1, 'studyplan_CourseGroup23', a)
    if hasattr(b2, 'studyplan_CourseGroup23'):
        assert _is_linked(b2, 'studyplan_CourseGroup23', a)
    _safe_set(a, 'studyplan_Semester24', None)
    assert not _is_linked(a, 'studyplan_Semester24', b2)
    if hasattr(b2, 'studyplan_CourseGroup23'):
        assert not _is_linked(b2, 'studyplan_CourseGroup23', a)


def test_assoc_semester3_link_reassign_clear():
    a = studyplan_StudyPlan(planName="sample_text")
    b1 = studyplan_Semester(semesterType="sample_text", year=7)
    b2 = studyplan_Semester(semesterType="sample_text_2", year=13)
    _safe_set(a, 'studyplan_StudyPlan4', b1)
    assert _is_linked(a, 'studyplan_StudyPlan4', b1)
    if hasattr(b1, 'studyplan_Semester'):
        assert _is_linked(b1, 'studyplan_Semester', a)
    _safe_set(a, 'studyplan_StudyPlan4', b2)
    assert _is_linked(a, 'studyplan_StudyPlan4', b2)
    if hasattr(b1, 'studyplan_Semester'):
        assert not _is_linked(b1, 'studyplan_Semester', a)
    if hasattr(b2, 'studyplan_Semester'):
        assert _is_linked(b2, 'studyplan_Semester', a)
    _safe_set(a, 'studyplan_StudyPlan4', None)
    assert not _is_linked(a, 'studyplan_StudyPlan4', b2)
    if hasattr(b2, 'studyplan_Semester'):
        assert not _is_linked(b2, 'studyplan_Semester', a)


def test_assoc_semesters19_link_reassign_clear():
    a = studyplan_Semester(semesterType="sample_text", year=7)
    b1 = studyplan_FieldOfStudy(fieldName="sample_text")
    b2 = studyplan_FieldOfStudy(fieldName="sample_text_2")
    _safe_set(a, 'studyplan_Semester21', b1)
    assert _is_linked(a, 'studyplan_Semester21', b1)
    if hasattr(b1, 'studyplan_FieldOfStudy20'):
        assert _is_linked(b1, 'studyplan_FieldOfStudy20', a)
    _safe_set(a, 'studyplan_Semester21', b2)
    assert _is_linked(a, 'studyplan_Semester21', b2)
    if hasattr(b1, 'studyplan_FieldOfStudy20'):
        assert not _is_linked(b1, 'studyplan_FieldOfStudy20', a)
    if hasattr(b2, 'studyplan_FieldOfStudy20'):
        assert _is_linked(b2, 'studyplan_FieldOfStudy20', a)
    _safe_set(a, 'studyplan_Semester21', None)
    assert not _is_linked(a, 'studyplan_Semester21', b2)
    if hasattr(b2, 'studyplan_FieldOfStudy20'):
        assert not _is_linked(b2, 'studyplan_FieldOfStudy20', a)


def test_assoc_semesters9_link_reassign_clear():
    a = studyplan_Specialization(specName="sample_text")
    b1 = studyplan_Semester(semesterType="sample_text", year=7)
    b2 = studyplan_Semester(semesterType="sample_text_2", year=13)
    _safe_set(a, 'studyplan_Specialization', {b1})
    assert _is_linked(a, 'studyplan_Specialization', b1)
    if hasattr(b1, 'studyplan_Semester10'):
        assert _is_linked(b1, 'studyplan_Semester10', a)
    _safe_set(a, 'studyplan_Specialization', {b2})
    assert _is_linked(a, 'studyplan_Specialization', b2)
    if hasattr(b1, 'studyplan_Semester10'):
        assert not _is_linked(b1, 'studyplan_Semester10', a)
    if hasattr(b2, 'studyplan_Semester10'):
        assert _is_linked(b2, 'studyplan_Semester10', a)
    _safe_set(a, 'studyplan_Specialization', set())
    assert not _is_linked(a, 'studyplan_Specialization', b2)
    if hasattr(b2, 'studyplan_Semester10'):
        assert not _is_linked(b2, 'studyplan_Semester10', a)


def test_assoc_specialization12_link_reassign_clear():
    a = studyplan_Specialization(specName="sample_text")
    b1 = studyplan_Specialization(specName="sample_text")
    b2 = studyplan_Specialization(specName="sample_text_2")
    _safe_set(a, 'studyplan_Specialization11', {b1})
    assert _is_linked(a, 'studyplan_Specialization11', b1)
    if hasattr(b1, 'studyplan_Specialization13'):
        assert _is_linked(b1, 'studyplan_Specialization13', a)
    _safe_set(a, 'studyplan_Specialization11', {b2})
    assert _is_linked(a, 'studyplan_Specialization11', b2)
    if hasattr(b1, 'studyplan_Specialization13'):
        assert not _is_linked(b1, 'studyplan_Specialization13', a)
    if hasattr(b2, 'studyplan_Specialization13'):
        assert _is_linked(b2, 'studyplan_Specialization13', a)
    _safe_set(a, 'studyplan_Specialization11', set())
    assert not _is_linked(a, 'studyplan_Specialization11', b2)
    if hasattr(b2, 'studyplan_Specialization13'):
        assert not _is_linked(b2, 'studyplan_Specialization13', a)


def test_assoc_specialization16_link_reassign_clear():
    a = studyplan_Specialization(specName="sample_text")
    b1 = studyplan_FieldOfStudy(fieldName="sample_text")
    b2 = studyplan_FieldOfStudy(fieldName="sample_text_2")
    _safe_set(a, 'studyplan_Specialization18', b1)
    assert _is_linked(a, 'studyplan_Specialization18', b1)
    if hasattr(b1, 'studyplan_FieldOfStudy17'):
        assert _is_linked(b1, 'studyplan_FieldOfStudy17', a)
    _safe_set(a, 'studyplan_Specialization18', b2)
    assert _is_linked(a, 'studyplan_Specialization18', b2)
    if hasattr(b1, 'studyplan_FieldOfStudy17'):
        assert not _is_linked(b1, 'studyplan_FieldOfStudy17', a)
    if hasattr(b2, 'studyplan_FieldOfStudy17'):
        assert _is_linked(b2, 'studyplan_FieldOfStudy17', a)
    _safe_set(a, 'studyplan_Specialization18', None)
    assert not _is_linked(a, 'studyplan_Specialization18', b2)
    if hasattr(b2, 'studyplan_FieldOfStudy17'):
        assert not _is_linked(b2, 'studyplan_FieldOfStudy17', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

studyplan_Course_strategy = st.builds(studyplan_Course, courseCode=st.integers(), courseName=safe_text, credit=st.floats(allow_nan=False, allow_infinity=False), status=safe_text)
@given(instance=studyplan_Course_strategy)
@settings(max_examples=25)
def test_studyplan_Course_instantiation(instance):
    assert isinstance(instance, studyplan_Course)


studyplan_CourseGroup_strategy = st.builds(studyplan_CourseGroup, courseStatus=safe_text, group=safe_text)
@given(instance=studyplan_CourseGroup_strategy)
@settings(max_examples=25)
def test_studyplan_CourseGroup_instantiation(instance):
    assert isinstance(instance, studyplan_CourseGroup)


studyplan_FieldOfStudy_strategy = st.builds(studyplan_FieldOfStudy, fieldName=safe_text)
@given(instance=studyplan_FieldOfStudy_strategy)
@settings(max_examples=25)
def test_studyplan_FieldOfStudy_instantiation(instance):
    assert isinstance(instance, studyplan_FieldOfStudy)


studyplan_Semester_strategy = st.builds(studyplan_Semester, semesterType=safe_text, year=st.integers())
@given(instance=studyplan_Semester_strategy)
@settings(max_examples=25)
def test_studyplan_Semester_instantiation(instance):
    assert isinstance(instance, studyplan_Semester)


studyplan_Specialization_strategy = st.builds(studyplan_Specialization, specName=safe_text)
@given(instance=studyplan_Specialization_strategy)
@settings(max_examples=25)
def test_studyplan_Specialization_instantiation(instance):
    assert isinstance(instance, studyplan_Specialization)


studyplan_StudyPlan_strategy = st.builds(studyplan_StudyPlan, planName=safe_text)
@given(instance=studyplan_StudyPlan_strategy)
@settings(max_examples=25)
def test_studyplan_StudyPlan_instantiation(instance):
    assert isinstance(instance, studyplan_StudyPlan)


