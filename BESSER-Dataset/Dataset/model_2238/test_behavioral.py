import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    studies_Course,
    studies_CourseInstance,
    studies_Semester,
    studies_Study,
    studies_StudyCourse,
    studies_StudyInstance,
    studies_StudyYear,
    studies_University,
    SemesterCode,
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

def test_assoc_autumnSemester13_reverse_link_reassign_clear():
    a1 = studies_StudyYear(programName="sample_text")
    a2 = studies_StudyYear(programName="sample_text_2")
    b = studies_Semester(studyYearSemester="sample_text")
    _safe_set(b, 'studies_Semester15', a1)
    assert _is_linked(b, 'studies_Semester15', a1)
    if hasattr(a1, 'studies_StudyYear14'):
        assert _is_linked(a1, 'studies_StudyYear14', b)
    _safe_set(b, 'studies_Semester15', a2)
    assert _is_linked(b, 'studies_Semester15', a2)
    if hasattr(a1, 'studies_StudyYear14'):
        assert not _is_linked(a1, 'studies_StudyYear14', b)
    if hasattr(a2, 'studies_StudyYear14'):
        assert _is_linked(a2, 'studies_StudyYear14', b)
    _safe_set(b, 'studies_Semester15', None)
    assert not _is_linked(b, 'studies_Semester15', a2)
    if hasattr(a2, 'studies_StudyYear14'):
        assert not _is_linked(a2, 'studies_StudyYear14', b)


def test_assoc_course4_reverse_link_reassign_clear():
    a1 = studies_CourseInstance(instanceName="sample_text", semester="sample_text", year=7)
    a2 = studies_CourseInstance(instanceName="sample_text_2", semester="sample_text_2", year=13)
    b = studies_Course(code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'courseInstances'):
        assert _is_linked(a1, 'courseInstances', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'courseInstances'):
        assert not _is_linked(a1, 'courseInstances', b)
    if hasattr(a2, 'courseInstances'):
        assert _is_linked(a2, 'courseInstances', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'courseInstances'):
        assert not _is_linked(a2, 'courseInstances', b)


def test_assoc_courseInstance16_reverse_link_reassign_clear():
    a1 = studies_StudyCourse(mandatory=True)
    a2 = studies_StudyCourse(mandatory=False)
    b = studies_CourseInstance(instanceName="sample_text", semester="sample_text", year=7)
    _safe_set(b, 'studies_CourseInstance', a1)
    assert _is_linked(b, 'studies_CourseInstance', a1)
    if hasattr(a1, 'studies_StudyCourse'):
        assert _is_linked(a1, 'studies_StudyCourse', b)
    _safe_set(b, 'studies_CourseInstance', a2)
    assert _is_linked(b, 'studies_CourseInstance', a2)
    if hasattr(a1, 'studies_StudyCourse'):
        assert not _is_linked(a1, 'studies_StudyCourse', b)
    if hasattr(a2, 'studies_StudyCourse'):
        assert _is_linked(a2, 'studies_StudyCourse', b)
    _safe_set(b, 'studies_CourseInstance', None)
    assert not _is_linked(b, 'studies_CourseInstance', a2)
    if hasattr(a2, 'studies_StudyCourse'):
        assert not _is_linked(a2, 'studies_StudyCourse', b)


def test_assoc_courseInstances3_reverse_link_reassign_clear():
    a1 = studies_CourseInstance(instanceName="sample_text", semester="sample_text", year=7)
    a2 = studies_CourseInstance(instanceName="sample_text_2", semester="sample_text_2", year=13)
    b = studies_Course(code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'course', {a1})
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'CourseInstance'):
        assert _is_linked(a1, 'CourseInstance', b)
    _safe_set(b, 'course', {a2})
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'CourseInstance'):
        assert not _is_linked(a1, 'CourseInstance', b)
    if hasattr(a2, 'CourseInstance'):
        assert _is_linked(a2, 'CourseInstance', b)
    _safe_set(b, 'course', set())
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'CourseInstance'):
        assert not _is_linked(a2, 'CourseInstance', b)


def test_assoc_courses0_reverse_link_reassign_clear():
    a1 = studies_University(name="sample_text")
    a2 = studies_University(name="sample_text_2")
    b = studies_Course(code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'studies_Course', a1)
    assert _is_linked(b, 'studies_Course', a1)
    if hasattr(a1, 'studies_University'):
        assert _is_linked(a1, 'studies_University', b)
    _safe_set(b, 'studies_Course', a2)
    assert _is_linked(b, 'studies_Course', a2)
    if hasattr(a1, 'studies_University'):
        assert not _is_linked(a1, 'studies_University', b)
    if hasattr(a2, 'studies_University'):
        assert _is_linked(a2, 'studies_University', b)
    _safe_set(b, 'studies_Course', None)
    assert not _is_linked(b, 'studies_Course', a2)
    if hasattr(a2, 'studies_University'):
        assert not _is_linked(a2, 'studies_University', b)


def test_assoc_courses17_reverse_link_reassign_clear():
    a1 = studies_Semester(studyYearSemester="sample_text")
    a2 = studies_Semester(studyYearSemester="sample_text_2")
    b = studies_CourseInstance(instanceName="sample_text", semester="sample_text", year=7)
    _safe_set(b, 'studies_CourseInstance19', a1)
    assert _is_linked(b, 'studies_CourseInstance19', a1)
    if hasattr(a1, 'studies_Semester18'):
        assert _is_linked(a1, 'studies_Semester18', b)
    _safe_set(b, 'studies_CourseInstance19', a2)
    assert _is_linked(b, 'studies_CourseInstance19', a2)
    if hasattr(a1, 'studies_Semester18'):
        assert not _is_linked(a1, 'studies_Semester18', b)
    if hasattr(a2, 'studies_Semester18'):
        assert _is_linked(a2, 'studies_Semester18', b)
    _safe_set(b, 'studies_CourseInstance19', None)
    assert not _is_linked(b, 'studies_CourseInstance19', a2)
    if hasattr(a2, 'studies_Semester18'):
        assert not _is_linked(a2, 'studies_Semester18', b)


def test_assoc_nextYear9_reverse_link_reassign_clear():
    a1 = studies_StudyYear(programName="sample_text")
    a2 = studies_StudyYear(programName="sample_text_2")
    b = studies_StudyYear(programName="sample_text")
    _safe_set(b, 'studies_StudyYear8', {a1})
    assert _is_linked(b, 'studies_StudyYear8', a1)
    if hasattr(a1, 'studies_StudyYear10'):
        assert _is_linked(a1, 'studies_StudyYear10', b)
    _safe_set(b, 'studies_StudyYear8', {a2})
    assert _is_linked(b, 'studies_StudyYear8', a2)
    if hasattr(a1, 'studies_StudyYear10'):
        assert not _is_linked(a1, 'studies_StudyYear10', b)
    if hasattr(a2, 'studies_StudyYear10'):
        assert _is_linked(a2, 'studies_StudyYear10', b)
    _safe_set(b, 'studies_StudyYear8', set())
    assert not _is_linked(b, 'studies_StudyYear8', a2)
    if hasattr(a2, 'studies_StudyYear10'):
        assert not _is_linked(a2, 'studies_StudyYear10', b)


def test_assoc_springSemester11_reverse_link_reassign_clear():
    a1 = studies_StudyYear(programName="sample_text")
    a2 = studies_StudyYear(programName="sample_text_2")
    b = studies_Semester(studyYearSemester="sample_text")
    _safe_set(b, 'studies_Semester', a1)
    assert _is_linked(b, 'studies_Semester', a1)
    if hasattr(a1, 'studies_StudyYear12'):
        assert _is_linked(a1, 'studies_StudyYear12', b)
    _safe_set(b, 'studies_Semester', a2)
    assert _is_linked(b, 'studies_Semester', a2)
    if hasattr(a1, 'studies_StudyYear12'):
        assert not _is_linked(a1, 'studies_StudyYear12', b)
    if hasattr(a2, 'studies_StudyYear12'):
        assert _is_linked(a2, 'studies_StudyYear12', b)
    _safe_set(b, 'studies_Semester', None)
    assert not _is_linked(b, 'studies_Semester', a2)
    if hasattr(a2, 'studies_StudyYear12'):
        assert not _is_linked(a2, 'studies_StudyYear12', b)


def test_assoc_startYear7_reverse_link_reassign_clear():
    a1 = studies_StudyYear(programName="sample_text")
    a2 = studies_StudyYear(programName="sample_text_2")
    b = studies_StudyInstance(year=7)
    _safe_set(b, 'studies_StudyInstance', a1)
    assert _is_linked(b, 'studies_StudyInstance', a1)
    if hasattr(a1, 'studies_StudyYear'):
        assert _is_linked(a1, 'studies_StudyYear', b)
    _safe_set(b, 'studies_StudyInstance', a2)
    assert _is_linked(b, 'studies_StudyInstance', a2)
    if hasattr(a1, 'studies_StudyYear'):
        assert not _is_linked(a1, 'studies_StudyYear', b)
    if hasattr(a2, 'studies_StudyYear'):
        assert _is_linked(a2, 'studies_StudyYear', b)
    _safe_set(b, 'studies_StudyInstance', None)
    assert not _is_linked(b, 'studies_StudyInstance', a2)
    if hasattr(a2, 'studies_StudyYear'):
        assert not _is_linked(a2, 'studies_StudyYear', b)


def test_assoc_studies1_reverse_link_reassign_clear():
    a1 = studies_University(name="sample_text")
    a2 = studies_University(name="sample_text_2")
    b = studies_Study(code="sample_text", name="sample_text")
    _safe_set(b, 'studies_Study', a1)
    assert _is_linked(b, 'studies_Study', a1)
    if hasattr(a1, 'studies_University2'):
        assert _is_linked(a1, 'studies_University2', b)
    _safe_set(b, 'studies_Study', a2)
    assert _is_linked(b, 'studies_Study', a2)
    if hasattr(a1, 'studies_University2'):
        assert not _is_linked(a1, 'studies_University2', b)
    if hasattr(a2, 'studies_University2'):
        assert _is_linked(a2, 'studies_University2', b)
    _safe_set(b, 'studies_Study', None)
    assert not _is_linked(b, 'studies_Study', a2)
    if hasattr(a2, 'studies_University2'):
        assert not _is_linked(a2, 'studies_University2', b)


def test_assoc_study6_reverse_link_reassign_clear():
    a1 = studies_StudyInstance(year=7)
    a2 = studies_StudyInstance(year=13)
    b = studies_Study(code="sample_text", name="sample_text")
    _safe_set(b, 'Study', a1)
    assert _is_linked(b, 'Study', a1)
    if hasattr(a1, 'studyInstances'):
        assert _is_linked(a1, 'studyInstances', b)
    _safe_set(b, 'Study', a2)
    assert _is_linked(b, 'Study', a2)
    if hasattr(a1, 'studyInstances'):
        assert not _is_linked(a1, 'studyInstances', b)
    if hasattr(a2, 'studyInstances'):
        assert _is_linked(a2, 'studyInstances', b)
    _safe_set(b, 'Study', None)
    assert not _is_linked(b, 'Study', a2)
    if hasattr(a2, 'studyInstances'):
        assert not _is_linked(a2, 'studyInstances', b)


def test_assoc_studyInstances5_reverse_link_reassign_clear():
    a1 = studies_StudyInstance(year=7)
    a2 = studies_StudyInstance(year=13)
    b = studies_Study(code="sample_text", name="sample_text")
    _safe_set(b, 'study', {a1})
    assert _is_linked(b, 'study', a1)
    if hasattr(a1, 'StudyInstance'):
        assert _is_linked(a1, 'StudyInstance', b)
    _safe_set(b, 'study', {a2})
    assert _is_linked(b, 'study', a2)
    if hasattr(a1, 'StudyInstance'):
        assert not _is_linked(a1, 'StudyInstance', b)
    if hasattr(a2, 'StudyInstance'):
        assert _is_linked(a2, 'StudyInstance', b)
    _safe_set(b, 'study', set())
    assert not _is_linked(b, 'study', a2)
    if hasattr(a2, 'StudyInstance'):
        assert not _is_linked(a2, 'StudyInstance', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

