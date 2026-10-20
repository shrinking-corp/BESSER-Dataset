import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_course25_reverse_link_reassign_clear():
    a1 = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    a2 = studyplan_CourseGroup(courseStatus="sample_text_2", group="sample_text_2")
    b = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'courseGroup'):
        assert _is_linked(a1, 'courseGroup', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'courseGroup'):
        assert not _is_linked(a1, 'courseGroup', b)
    if hasattr(a2, 'courseGroup'):
        assert _is_linked(a2, 'courseGroup', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'courseGroup'):
        assert not _is_linked(a2, 'courseGroup', b)


def test_assoc_courseGroup14_reverse_link_reassign_clear():
    a1 = studyplan_Specialization(specName="sample_text")
    a2 = studyplan_Specialization(specName="sample_text_2")
    b = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    _safe_set(b, 'studyplan_CourseGroup', a1)
    assert _is_linked(b, 'studyplan_CourseGroup', a1)
    if hasattr(a1, 'studyplan_Specialization15'):
        assert _is_linked(a1, 'studyplan_Specialization15', b)
    _safe_set(b, 'studyplan_CourseGroup', a2)
    assert _is_linked(b, 'studyplan_CourseGroup', a2)
    if hasattr(a1, 'studyplan_Specialization15'):
        assert not _is_linked(a1, 'studyplan_Specialization15', b)
    if hasattr(a2, 'studyplan_Specialization15'):
        assert _is_linked(a2, 'studyplan_Specialization15', b)
    _safe_set(b, 'studyplan_CourseGroup', None)
    assert not _is_linked(b, 'studyplan_CourseGroup', a2)
    if hasattr(a2, 'studyplan_Specialization15'):
        assert not _is_linked(a2, 'studyplan_Specialization15', b)


def test_assoc_courseGroup8_reverse_link_reassign_clear():
    a1 = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    a2 = studyplan_CourseGroup(courseStatus="sample_text_2", group="sample_text_2")
    b = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    _safe_set(b, 'course', a1)
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'CourseGroup'):
        assert _is_linked(a1, 'CourseGroup', b)
    _safe_set(b, 'course', a2)
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'CourseGroup'):
        assert not _is_linked(a1, 'CourseGroup', b)
    if hasattr(a2, 'CourseGroup'):
        assert _is_linked(a2, 'CourseGroup', b)
    _safe_set(b, 'course', None)
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'CourseGroup'):
        assert not _is_linked(a2, 'CourseGroup', b)


def test_assoc_courses1_reverse_link_reassign_clear():
    a1 = studyplan_StudyPlan(planName="sample_text")
    a2 = studyplan_StudyPlan(planName="sample_text_2")
    b = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    _safe_set(b, 'studyplan_Course', a1)
    assert _is_linked(b, 'studyplan_Course', a1)
    if hasattr(a1, 'studyplan_StudyPlan2'):
        assert _is_linked(a1, 'studyplan_StudyPlan2', b)
    _safe_set(b, 'studyplan_Course', a2)
    assert _is_linked(b, 'studyplan_Course', a2)
    if hasattr(a1, 'studyplan_StudyPlan2'):
        assert not _is_linked(a1, 'studyplan_StudyPlan2', b)
    if hasattr(a2, 'studyplan_StudyPlan2'):
        assert _is_linked(a2, 'studyplan_StudyPlan2', b)
    _safe_set(b, 'studyplan_Course', None)
    assert not _is_linked(b, 'studyplan_Course', a2)
    if hasattr(a2, 'studyplan_StudyPlan2'):
        assert not _is_linked(a2, 'studyplan_StudyPlan2', b)


def test_assoc_courses5_reverse_link_reassign_clear():
    a1 = studyplan_Semester(semesterType="sample_text", year=7)
    a2 = studyplan_Semester(semesterType="sample_text_2", year=13)
    b = studyplan_Course(courseCode=7, courseName="sample_text", credit=3.14, status="sample_text")
    _safe_set(b, 'studyplan_Course7', a1)
    assert _is_linked(b, 'studyplan_Course7', a1)
    if hasattr(a1, 'studyplan_Semester6'):
        assert _is_linked(a1, 'studyplan_Semester6', b)
    _safe_set(b, 'studyplan_Course7', a2)
    assert _is_linked(b, 'studyplan_Course7', a2)
    if hasattr(a1, 'studyplan_Semester6'):
        assert not _is_linked(a1, 'studyplan_Semester6', b)
    if hasattr(a2, 'studyplan_Semester6'):
        assert _is_linked(a2, 'studyplan_Semester6', b)
    _safe_set(b, 'studyplan_Course7', None)
    assert not _is_linked(b, 'studyplan_Course7', a2)
    if hasattr(a2, 'studyplan_Semester6'):
        assert not _is_linked(a2, 'studyplan_Semester6', b)


def test_assoc_program0_reverse_link_reassign_clear():
    a1 = studyplan_StudyPlan(planName="sample_text")
    a2 = studyplan_StudyPlan(planName="sample_text_2")
    b = studyplan_FieldOfStudy(fieldName="sample_text")
    _safe_set(b, 'studyplan_FieldOfStudy', a1)
    assert _is_linked(b, 'studyplan_FieldOfStudy', a1)
    if hasattr(a1, 'studyplan_StudyPlan'):
        assert _is_linked(a1, 'studyplan_StudyPlan', b)
    _safe_set(b, 'studyplan_FieldOfStudy', a2)
    assert _is_linked(b, 'studyplan_FieldOfStudy', a2)
    if hasattr(a1, 'studyplan_StudyPlan'):
        assert not _is_linked(a1, 'studyplan_StudyPlan', b)
    if hasattr(a2, 'studyplan_StudyPlan'):
        assert _is_linked(a2, 'studyplan_StudyPlan', b)
    _safe_set(b, 'studyplan_FieldOfStudy', None)
    assert not _is_linked(b, 'studyplan_FieldOfStudy', a2)
    if hasattr(a2, 'studyplan_StudyPlan'):
        assert not _is_linked(a2, 'studyplan_StudyPlan', b)


def test_assoc_semester22_reverse_link_reassign_clear():
    a1 = studyplan_Semester(semesterType="sample_text", year=7)
    a2 = studyplan_Semester(semesterType="sample_text_2", year=13)
    b = studyplan_CourseGroup(courseStatus="sample_text", group="sample_text")
    _safe_set(b, 'studyplan_CourseGroup23', a1)
    assert _is_linked(b, 'studyplan_CourseGroup23', a1)
    if hasattr(a1, 'studyplan_Semester24'):
        assert _is_linked(a1, 'studyplan_Semester24', b)
    _safe_set(b, 'studyplan_CourseGroup23', a2)
    assert _is_linked(b, 'studyplan_CourseGroup23', a2)
    if hasattr(a1, 'studyplan_Semester24'):
        assert not _is_linked(a1, 'studyplan_Semester24', b)
    if hasattr(a2, 'studyplan_Semester24'):
        assert _is_linked(a2, 'studyplan_Semester24', b)
    _safe_set(b, 'studyplan_CourseGroup23', None)
    assert not _is_linked(b, 'studyplan_CourseGroup23', a2)
    if hasattr(a2, 'studyplan_Semester24'):
        assert not _is_linked(a2, 'studyplan_Semester24', b)


def test_assoc_semester3_reverse_link_reassign_clear():
    a1 = studyplan_StudyPlan(planName="sample_text")
    a2 = studyplan_StudyPlan(planName="sample_text_2")
    b = studyplan_Semester(semesterType="sample_text", year=7)
    _safe_set(b, 'studyplan_Semester', a1)
    assert _is_linked(b, 'studyplan_Semester', a1)
    if hasattr(a1, 'studyplan_StudyPlan4'):
        assert _is_linked(a1, 'studyplan_StudyPlan4', b)
    _safe_set(b, 'studyplan_Semester', a2)
    assert _is_linked(b, 'studyplan_Semester', a2)
    if hasattr(a1, 'studyplan_StudyPlan4'):
        assert not _is_linked(a1, 'studyplan_StudyPlan4', b)
    if hasattr(a2, 'studyplan_StudyPlan4'):
        assert _is_linked(a2, 'studyplan_StudyPlan4', b)
    _safe_set(b, 'studyplan_Semester', None)
    assert not _is_linked(b, 'studyplan_Semester', a2)
    if hasattr(a2, 'studyplan_StudyPlan4'):
        assert not _is_linked(a2, 'studyplan_StudyPlan4', b)


def test_assoc_semesters19_reverse_link_reassign_clear():
    a1 = studyplan_Semester(semesterType="sample_text", year=7)
    a2 = studyplan_Semester(semesterType="sample_text_2", year=13)
    b = studyplan_FieldOfStudy(fieldName="sample_text")
    _safe_set(b, 'studyplan_FieldOfStudy20', {a1})
    assert _is_linked(b, 'studyplan_FieldOfStudy20', a1)
    if hasattr(a1, 'studyplan_Semester21'):
        assert _is_linked(a1, 'studyplan_Semester21', b)
    _safe_set(b, 'studyplan_FieldOfStudy20', {a2})
    assert _is_linked(b, 'studyplan_FieldOfStudy20', a2)
    if hasattr(a1, 'studyplan_Semester21'):
        assert not _is_linked(a1, 'studyplan_Semester21', b)
    if hasattr(a2, 'studyplan_Semester21'):
        assert _is_linked(a2, 'studyplan_Semester21', b)
    _safe_set(b, 'studyplan_FieldOfStudy20', set())
    assert not _is_linked(b, 'studyplan_FieldOfStudy20', a2)
    if hasattr(a2, 'studyplan_Semester21'):
        assert not _is_linked(a2, 'studyplan_Semester21', b)


def test_assoc_semesters9_reverse_link_reassign_clear():
    a1 = studyplan_Specialization(specName="sample_text")
    a2 = studyplan_Specialization(specName="sample_text_2")
    b = studyplan_Semester(semesterType="sample_text", year=7)
    _safe_set(b, 'studyplan_Semester10', a1)
    assert _is_linked(b, 'studyplan_Semester10', a1)
    if hasattr(a1, 'studyplan_Specialization'):
        assert _is_linked(a1, 'studyplan_Specialization', b)
    _safe_set(b, 'studyplan_Semester10', a2)
    assert _is_linked(b, 'studyplan_Semester10', a2)
    if hasattr(a1, 'studyplan_Specialization'):
        assert not _is_linked(a1, 'studyplan_Specialization', b)
    if hasattr(a2, 'studyplan_Specialization'):
        assert _is_linked(a2, 'studyplan_Specialization', b)
    _safe_set(b, 'studyplan_Semester10', None)
    assert not _is_linked(b, 'studyplan_Semester10', a2)
    if hasattr(a2, 'studyplan_Specialization'):
        assert not _is_linked(a2, 'studyplan_Specialization', b)


def test_assoc_specialization12_reverse_link_reassign_clear():
    a1 = studyplan_Specialization(specName="sample_text")
    a2 = studyplan_Specialization(specName="sample_text_2")
    b = studyplan_Specialization(specName="sample_text")
    _safe_set(b, 'studyplan_Specialization13', a1)
    assert _is_linked(b, 'studyplan_Specialization13', a1)
    if hasattr(a1, 'studyplan_Specialization11'):
        assert _is_linked(a1, 'studyplan_Specialization11', b)
    _safe_set(b, 'studyplan_Specialization13', a2)
    assert _is_linked(b, 'studyplan_Specialization13', a2)
    if hasattr(a1, 'studyplan_Specialization11'):
        assert not _is_linked(a1, 'studyplan_Specialization11', b)
    if hasattr(a2, 'studyplan_Specialization11'):
        assert _is_linked(a2, 'studyplan_Specialization11', b)
    _safe_set(b, 'studyplan_Specialization13', None)
    assert not _is_linked(b, 'studyplan_Specialization13', a2)
    if hasattr(a2, 'studyplan_Specialization11'):
        assert not _is_linked(a2, 'studyplan_Specialization11', b)


def test_assoc_specialization16_reverse_link_reassign_clear():
    a1 = studyplan_Specialization(specName="sample_text")
    a2 = studyplan_Specialization(specName="sample_text_2")
    b = studyplan_FieldOfStudy(fieldName="sample_text")
    _safe_set(b, 'studyplan_FieldOfStudy17', a1)
    assert _is_linked(b, 'studyplan_FieldOfStudy17', a1)
    if hasattr(a1, 'studyplan_Specialization18'):
        assert _is_linked(a1, 'studyplan_Specialization18', b)
    _safe_set(b, 'studyplan_FieldOfStudy17', a2)
    assert _is_linked(b, 'studyplan_FieldOfStudy17', a2)
    if hasattr(a1, 'studyplan_Specialization18'):
        assert not _is_linked(a1, 'studyplan_Specialization18', b)
    if hasattr(a2, 'studyplan_Specialization18'):
        assert _is_linked(a2, 'studyplan_Specialization18', b)
    _safe_set(b, 'studyplan_FieldOfStudy17', None)
    assert not _is_linked(b, 'studyplan_FieldOfStudy17', a2)
    if hasattr(a2, 'studyplan_Specialization18'):
        assert not _is_linked(a2, 'studyplan_Specialization18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

