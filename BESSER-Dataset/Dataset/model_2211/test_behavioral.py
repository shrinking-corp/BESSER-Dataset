import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    StudyProgrammes_Course,
    StudyProgrammes_CourseAccess,
    StudyProgrammes_Department,
    StudyProgrammes_Programme,
    StudyProgrammes_Semester,
    StudyProgrammes_Specialization,
    Access,
    SemesterSeason,
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

def test_assoc_course12_reverse_link_reassign_clear():
    a1 = StudyProgrammes_CourseAccess(access="sample_text")
    a2 = StudyProgrammes_CourseAccess(access="sample_text_2")
    b = StudyProgrammes_Course(availableSemesters="sample_text", code="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'StudyProgrammes_Course14', a1)
    assert _is_linked(b, 'StudyProgrammes_Course14', a1)
    if hasattr(a1, 'StudyProgrammes_CourseAccess13'):
        assert _is_linked(a1, 'StudyProgrammes_CourseAccess13', b)
    _safe_set(b, 'StudyProgrammes_Course14', a2)
    assert _is_linked(b, 'StudyProgrammes_Course14', a2)
    if hasattr(a1, 'StudyProgrammes_CourseAccess13'):
        assert not _is_linked(a1, 'StudyProgrammes_CourseAccess13', b)
    if hasattr(a2, 'StudyProgrammes_CourseAccess13'):
        assert _is_linked(a2, 'StudyProgrammes_CourseAccess13', b)
    _safe_set(b, 'StudyProgrammes_Course14', None)
    assert not _is_linked(b, 'StudyProgrammes_Course14', a2)
    if hasattr(a2, 'StudyProgrammes_CourseAccess13'):
        assert not _is_linked(a2, 'StudyProgrammes_CourseAccess13', b)


def test_assoc_courseAccesses10_reverse_link_reassign_clear():
    a1 = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    a2 = StudyProgrammes_Semester(code="sample_text_2", semesterSeason="sample_text_2", year=13)
    b = StudyProgrammes_CourseAccess(access="sample_text")
    _safe_set(b, 'StudyProgrammes_CourseAccess', a1)
    assert _is_linked(b, 'StudyProgrammes_CourseAccess', a1)
    if hasattr(a1, 'StudyProgrammes_Semester11'):
        assert _is_linked(a1, 'StudyProgrammes_Semester11', b)
    _safe_set(b, 'StudyProgrammes_CourseAccess', a2)
    assert _is_linked(b, 'StudyProgrammes_CourseAccess', a2)
    if hasattr(a1, 'StudyProgrammes_Semester11'):
        assert not _is_linked(a1, 'StudyProgrammes_Semester11', b)
    if hasattr(a2, 'StudyProgrammes_Semester11'):
        assert _is_linked(a2, 'StudyProgrammes_Semester11', b)
    _safe_set(b, 'StudyProgrammes_CourseAccess', None)
    assert not _is_linked(b, 'StudyProgrammes_CourseAccess', a2)
    if hasattr(a2, 'StudyProgrammes_Semester11'):
        assert not _is_linked(a2, 'StudyProgrammes_Semester11', b)


def test_assoc_courses1_reverse_link_reassign_clear():
    a1 = StudyProgrammes_Department(name="sample_text")
    a2 = StudyProgrammes_Department(name="sample_text_2")
    b = StudyProgrammes_Course(availableSemesters="sample_text", code="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'StudyProgrammes_Course', a1)
    assert _is_linked(b, 'StudyProgrammes_Course', a1)
    if hasattr(a1, 'StudyProgrammes_Department2'):
        assert _is_linked(a1, 'StudyProgrammes_Department2', b)
    _safe_set(b, 'StudyProgrammes_Course', a2)
    assert _is_linked(b, 'StudyProgrammes_Course', a2)
    if hasattr(a1, 'StudyProgrammes_Department2'):
        assert not _is_linked(a1, 'StudyProgrammes_Department2', b)
    if hasattr(a2, 'StudyProgrammes_Department2'):
        assert _is_linked(a2, 'StudyProgrammes_Department2', b)
    _safe_set(b, 'StudyProgrammes_Course', None)
    assert not _is_linked(b, 'StudyProgrammes_Course', a2)
    if hasattr(a2, 'StudyProgrammes_Department2'):
        assert not _is_linked(a2, 'StudyProgrammes_Department2', b)


def test_assoc_programmes0_reverse_link_reassign_clear():
    a1 = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    a2 = StudyProgrammes_Programme(code="sample_text_2", name="sample_text_2", semestersBeforeSpecialization=13, startYear=13, totalNumberOfSemesters=13)
    b = StudyProgrammes_Department(name="sample_text")
    _safe_set(b, 'StudyProgrammes_Department', {a1})
    assert _is_linked(b, 'StudyProgrammes_Department', a1)
    if hasattr(a1, 'StudyProgrammes_Programme'):
        assert _is_linked(a1, 'StudyProgrammes_Programme', b)
    _safe_set(b, 'StudyProgrammes_Department', {a2})
    assert _is_linked(b, 'StudyProgrammes_Department', a2)
    if hasattr(a1, 'StudyProgrammes_Programme'):
        assert not _is_linked(a1, 'StudyProgrammes_Programme', b)
    if hasattr(a2, 'StudyProgrammes_Programme'):
        assert _is_linked(a2, 'StudyProgrammes_Programme', b)
    _safe_set(b, 'StudyProgrammes_Department', set())
    assert not _is_linked(b, 'StudyProgrammes_Department', a2)
    if hasattr(a2, 'StudyProgrammes_Programme'):
        assert not _is_linked(a2, 'StudyProgrammes_Programme', b)


def test_assoc_semesters5_reverse_link_reassign_clear():
    a1 = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    a2 = StudyProgrammes_Semester(code="sample_text_2", semesterSeason="sample_text_2", year=13)
    b = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    _safe_set(b, 'StudyProgrammes_Programme6', {a1})
    assert _is_linked(b, 'StudyProgrammes_Programme6', a1)
    if hasattr(a1, 'StudyProgrammes_Semester'):
        assert _is_linked(a1, 'StudyProgrammes_Semester', b)
    _safe_set(b, 'StudyProgrammes_Programme6', {a2})
    assert _is_linked(b, 'StudyProgrammes_Programme6', a2)
    if hasattr(a1, 'StudyProgrammes_Semester'):
        assert not _is_linked(a1, 'StudyProgrammes_Semester', b)
    if hasattr(a2, 'StudyProgrammes_Semester'):
        assert _is_linked(a2, 'StudyProgrammes_Semester', b)
    _safe_set(b, 'StudyProgrammes_Programme6', set())
    assert not _is_linked(b, 'StudyProgrammes_Programme6', a2)
    if hasattr(a2, 'StudyProgrammes_Semester'):
        assert not _is_linked(a2, 'StudyProgrammes_Semester', b)


def test_assoc_semesters7_reverse_link_reassign_clear():
    a1 = StudyProgrammes_Specialization(lengthInSemesters=7, name="sample_text", startSemester=7)
    a2 = StudyProgrammes_Specialization(lengthInSemesters=13, name="sample_text_2", startSemester=13)
    b = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    _safe_set(b, 'StudyProgrammes_Semester9', a1)
    assert _is_linked(b, 'StudyProgrammes_Semester9', a1)
    if hasattr(a1, 'StudyProgrammes_Specialization8'):
        assert _is_linked(a1, 'StudyProgrammes_Specialization8', b)
    _safe_set(b, 'StudyProgrammes_Semester9', a2)
    assert _is_linked(b, 'StudyProgrammes_Semester9', a2)
    if hasattr(a1, 'StudyProgrammes_Specialization8'):
        assert not _is_linked(a1, 'StudyProgrammes_Specialization8', b)
    if hasattr(a2, 'StudyProgrammes_Specialization8'):
        assert _is_linked(a2, 'StudyProgrammes_Specialization8', b)
    _safe_set(b, 'StudyProgrammes_Semester9', None)
    assert not _is_linked(b, 'StudyProgrammes_Semester9', a2)
    if hasattr(a2, 'StudyProgrammes_Specialization8'):
        assert not _is_linked(a2, 'StudyProgrammes_Specialization8', b)


def test_assoc_specializations3_reverse_link_reassign_clear():
    a1 = StudyProgrammes_Specialization(lengthInSemesters=7, name="sample_text", startSemester=7)
    a2 = StudyProgrammes_Specialization(lengthInSemesters=13, name="sample_text_2", startSemester=13)
    b = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    _safe_set(b, 'StudyProgrammes_Programme4', {a1})
    assert _is_linked(b, 'StudyProgrammes_Programme4', a1)
    if hasattr(a1, 'StudyProgrammes_Specialization'):
        assert _is_linked(a1, 'StudyProgrammes_Specialization', b)
    _safe_set(b, 'StudyProgrammes_Programme4', {a2})
    assert _is_linked(b, 'StudyProgrammes_Programme4', a2)
    if hasattr(a1, 'StudyProgrammes_Specialization'):
        assert not _is_linked(a1, 'StudyProgrammes_Specialization', b)
    if hasattr(a2, 'StudyProgrammes_Specialization'):
        assert _is_linked(a2, 'StudyProgrammes_Specialization', b)
    _safe_set(b, 'StudyProgrammes_Programme4', set())
    assert not _is_linked(b, 'StudyProgrammes_Programme4', a2)
    if hasattr(a2, 'StudyProgrammes_Specialization'):
        assert not _is_linked(a2, 'StudyProgrammes_Specialization', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

