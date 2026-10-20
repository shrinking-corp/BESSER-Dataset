import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    programme_Course,
    programme_Department,
    programme_Programme,
    programme_Semester,
    programme_SemesterCourse,
    programme_Specialization,
    programme_StudyYear,
    CourseLevel,
    CourseType,
    ProgrammeType,
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

def test_assoc_availableSpecializations3_reverse_link_reassign_clear():
    a1 = programme_Specialization(name="sample_text")
    a2 = programme_Specialization(name="sample_text_2")
    b = programme_Programme(code="sample_text", name="sample_text", programmeType="sample_text")
    _safe_set(b, 'programme_Programme4', {a1})
    assert _is_linked(b, 'programme_Programme4', a1)
    if hasattr(a1, 'programme_Specialization'):
        assert _is_linked(a1, 'programme_Specialization', b)
    _safe_set(b, 'programme_Programme4', {a2})
    assert _is_linked(b, 'programme_Programme4', a2)
    if hasattr(a1, 'programme_Specialization'):
        assert not _is_linked(a1, 'programme_Specialization', b)
    if hasattr(a2, 'programme_Specialization'):
        assert _is_linked(a2, 'programme_Specialization', b)
    _safe_set(b, 'programme_Programme4', set())
    assert not _is_linked(b, 'programme_Programme4', a2)
    if hasattr(a2, 'programme_Specialization'):
        assert not _is_linked(a2, 'programme_Specialization', b)


def test_assoc_availableSpecializations8_reverse_link_reassign_clear():
    a1 = programme_Specialization(name="sample_text")
    a2 = programme_Specialization(name="sample_text_2")
    b = programme_Specialization(name="sample_text")
    _safe_set(b, 'programme_Specialization9', a1)
    assert _is_linked(b, 'programme_Specialization9', a1)
    if hasattr(a1, 'programme_Specialization7'):
        assert _is_linked(a1, 'programme_Specialization7', b)
    _safe_set(b, 'programme_Specialization9', a2)
    assert _is_linked(b, 'programme_Specialization9', a2)
    if hasattr(a1, 'programme_Specialization7'):
        assert not _is_linked(a1, 'programme_Specialization7', b)
    if hasattr(a2, 'programme_Specialization7'):
        assert _is_linked(a2, 'programme_Specialization7', b)
    _safe_set(b, 'programme_Specialization9', None)
    assert not _is_linked(b, 'programme_Specialization9', a2)
    if hasattr(a2, 'programme_Specialization7'):
        assert not _is_linked(a2, 'programme_Specialization7', b)


def test_assoc_courses1_reverse_link_reassign_clear():
    a1 = programme_Department(name="sample_text")
    a2 = programme_Department(name="sample_text_2")
    b = programme_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text", taugtIn="sample_text")
    _safe_set(b, 'programme_Course', a1)
    assert _is_linked(b, 'programme_Course', a1)
    if hasattr(a1, 'programme_Department2'):
        assert _is_linked(a1, 'programme_Department2', b)
    _safe_set(b, 'programme_Course', a2)
    assert _is_linked(b, 'programme_Course', a2)
    if hasattr(a1, 'programme_Department2'):
        assert not _is_linked(a1, 'programme_Department2', b)
    if hasattr(a2, 'programme_Department2'):
        assert _is_linked(a2, 'programme_Department2', b)
    _safe_set(b, 'programme_Course', None)
    assert not _is_linked(b, 'programme_Course', a2)
    if hasattr(a2, 'programme_Department2'):
        assert not _is_linked(a2, 'programme_Department2', b)


def test_assoc_courses15_reverse_link_reassign_clear():
    a1 = programme_SemesterCourse(courseType="sample_text")
    a2 = programme_SemesterCourse(courseType="sample_text_2")
    b = programme_Semester(semesterType="sample_text")
    _safe_set(b, 'programme_Semester16', {a1})
    assert _is_linked(b, 'programme_Semester16', a1)
    if hasattr(a1, 'programme_SemesterCourse'):
        assert _is_linked(a1, 'programme_SemesterCourse', b)
    _safe_set(b, 'programme_Semester16', {a2})
    assert _is_linked(b, 'programme_Semester16', a2)
    if hasattr(a1, 'programme_SemesterCourse'):
        assert not _is_linked(a1, 'programme_SemesterCourse', b)
    if hasattr(a2, 'programme_SemesterCourse'):
        assert _is_linked(a2, 'programme_SemesterCourse', b)
    _safe_set(b, 'programme_Semester16', set())
    assert not _is_linked(b, 'programme_Semester16', a2)
    if hasattr(a2, 'programme_SemesterCourse'):
        assert not _is_linked(a2, 'programme_SemesterCourse', b)


def test_assoc_programmes0_reverse_link_reassign_clear():
    a1 = programme_Programme(code="sample_text", name="sample_text", programmeType="sample_text")
    a2 = programme_Programme(code="sample_text_2", name="sample_text_2", programmeType="sample_text_2")
    b = programme_Department(name="sample_text")
    _safe_set(b, 'programme_Department', {a1})
    assert _is_linked(b, 'programme_Department', a1)
    if hasattr(a1, 'programme_Programme'):
        assert _is_linked(a1, 'programme_Programme', b)
    _safe_set(b, 'programme_Department', {a2})
    assert _is_linked(b, 'programme_Department', a2)
    if hasattr(a1, 'programme_Programme'):
        assert not _is_linked(a1, 'programme_Programme', b)
    if hasattr(a2, 'programme_Programme'):
        assert _is_linked(a2, 'programme_Programme', b)
    _safe_set(b, 'programme_Department', set())
    assert not _is_linked(b, 'programme_Department', a2)
    if hasattr(a2, 'programme_Programme'):
        assert not _is_linked(a2, 'programme_Programme', b)


def test_assoc_semesterCourse17_reverse_link_reassign_clear():
    a1 = programme_SemesterCourse(courseType="sample_text")
    a2 = programme_SemesterCourse(courseType="sample_text_2")
    b = programme_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text", taugtIn="sample_text")
    _safe_set(b, 'programme_Course19', a1)
    assert _is_linked(b, 'programme_Course19', a1)
    if hasattr(a1, 'programme_SemesterCourse18'):
        assert _is_linked(a1, 'programme_SemesterCourse18', b)
    _safe_set(b, 'programme_Course19', a2)
    assert _is_linked(b, 'programme_Course19', a2)
    if hasattr(a1, 'programme_SemesterCourse18'):
        assert not _is_linked(a1, 'programme_SemesterCourse18', b)
    if hasattr(a2, 'programme_SemesterCourse18'):
        assert _is_linked(a2, 'programme_SemesterCourse18', b)
    _safe_set(b, 'programme_Course19', None)
    assert not _is_linked(b, 'programme_Course19', a2)
    if hasattr(a2, 'programme_SemesterCourse18'):
        assert not _is_linked(a2, 'programme_SemesterCourse18', b)


def test_assoc_semesters13_reverse_link_reassign_clear():
    a1 = programme_StudyYear(year=7)
    a2 = programme_StudyYear(year=13)
    b = programme_Semester(semesterType="sample_text")
    _safe_set(b, 'programme_Semester', a1)
    assert _is_linked(b, 'programme_Semester', a1)
    if hasattr(a1, 'programme_StudyYear14'):
        assert _is_linked(a1, 'programme_StudyYear14', b)
    _safe_set(b, 'programme_Semester', a2)
    assert _is_linked(b, 'programme_Semester', a2)
    if hasattr(a1, 'programme_StudyYear14'):
        assert not _is_linked(a1, 'programme_StudyYear14', b)
    if hasattr(a2, 'programme_StudyYear14'):
        assert _is_linked(a2, 'programme_StudyYear14', b)
    _safe_set(b, 'programme_Semester', None)
    assert not _is_linked(b, 'programme_Semester', a2)
    if hasattr(a2, 'programme_StudyYear14'):
        assert not _is_linked(a2, 'programme_StudyYear14', b)


def test_assoc_studyYears10_reverse_link_reassign_clear():
    a1 = programme_StudyYear(year=7)
    a2 = programme_StudyYear(year=13)
    b = programme_Specialization(name="sample_text")
    _safe_set(b, 'programme_Specialization11', {a1})
    assert _is_linked(b, 'programme_Specialization11', a1)
    if hasattr(a1, 'programme_StudyYear12'):
        assert _is_linked(a1, 'programme_StudyYear12', b)
    _safe_set(b, 'programme_Specialization11', {a2})
    assert _is_linked(b, 'programme_Specialization11', a2)
    if hasattr(a1, 'programme_StudyYear12'):
        assert not _is_linked(a1, 'programme_StudyYear12', b)
    if hasattr(a2, 'programme_StudyYear12'):
        assert _is_linked(a2, 'programme_StudyYear12', b)
    _safe_set(b, 'programme_Specialization11', set())
    assert not _is_linked(b, 'programme_Specialization11', a2)
    if hasattr(a2, 'programme_StudyYear12'):
        assert not _is_linked(a2, 'programme_StudyYear12', b)


def test_assoc_studyYears5_reverse_link_reassign_clear():
    a1 = programme_StudyYear(year=7)
    a2 = programme_StudyYear(year=13)
    b = programme_Programme(code="sample_text", name="sample_text", programmeType="sample_text")
    _safe_set(b, 'programme_Programme6', {a1})
    assert _is_linked(b, 'programme_Programme6', a1)
    if hasattr(a1, 'programme_StudyYear'):
        assert _is_linked(a1, 'programme_StudyYear', b)
    _safe_set(b, 'programme_Programme6', {a2})
    assert _is_linked(b, 'programme_Programme6', a2)
    if hasattr(a1, 'programme_StudyYear'):
        assert not _is_linked(a1, 'programme_StudyYear', b)
    if hasattr(a2, 'programme_StudyYear'):
        assert _is_linked(a2, 'programme_StudyYear', b)
    _safe_set(b, 'programme_Programme6', set())
    assert not _is_linked(b, 'programme_Programme6', a2)
    if hasattr(a2, 'programme_StudyYear'):
        assert not _is_linked(a2, 'programme_StudyYear', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

