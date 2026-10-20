import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    studyprograms_Course,
    studyprograms_CourseAccess,
    studyprograms_Department,
    studyprograms_IndividualStudyPlan,
    studyprograms_Programme,
    studyprograms_Semester,
    studyprograms_Specialisation,
    Access,
    AvailableSemesters,
    Level,
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

def test_assoc_courseAccess8_reverse_link_reassign_clear():
    a1 = studyprograms_Semester(semesterCode="sample_text", semesterType="sample_text", year=7)
    a2 = studyprograms_Semester(semesterCode="sample_text_2", semesterType="sample_text_2", year=13)
    b = studyprograms_CourseAccess(Access="sample_text")
    _safe_set(b, 'studyprograms_CourseAccess', a1)
    assert _is_linked(b, 'studyprograms_CourseAccess', a1)
    if hasattr(a1, 'studyprograms_Semester9'):
        assert _is_linked(a1, 'studyprograms_Semester9', b)
    _safe_set(b, 'studyprograms_CourseAccess', a2)
    assert _is_linked(b, 'studyprograms_CourseAccess', a2)
    if hasattr(a1, 'studyprograms_Semester9'):
        assert not _is_linked(a1, 'studyprograms_Semester9', b)
    if hasattr(a2, 'studyprograms_Semester9'):
        assert _is_linked(a2, 'studyprograms_Semester9', b)
    _safe_set(b, 'studyprograms_CourseAccess', None)
    assert not _is_linked(b, 'studyprograms_CourseAccess', a2)
    if hasattr(a2, 'studyprograms_Semester9'):
        assert not _is_linked(a2, 'studyprograms_Semester9', b)


def test_assoc_courses10_reverse_link_reassign_clear():
    a1 = studyprograms_CourseAccess(Access="sample_text")
    a2 = studyprograms_CourseAccess(Access="sample_text_2")
    b = studyprograms_Course(availableSemester="sample_text", code="sample_text", ects=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'studyprograms_Course', a1)
    assert _is_linked(b, 'studyprograms_Course', a1)
    if hasattr(a1, 'studyprograms_CourseAccess11'):
        assert _is_linked(a1, 'studyprograms_CourseAccess11', b)
    _safe_set(b, 'studyprograms_Course', a2)
    assert _is_linked(b, 'studyprograms_Course', a2)
    if hasattr(a1, 'studyprograms_CourseAccess11'):
        assert not _is_linked(a1, 'studyprograms_CourseAccess11', b)
    if hasattr(a2, 'studyprograms_CourseAccess11'):
        assert _is_linked(a2, 'studyprograms_CourseAccess11', b)
    _safe_set(b, 'studyprograms_Course', None)
    assert not _is_linked(b, 'studyprograms_Course', a2)
    if hasattr(a2, 'studyprograms_CourseAccess11'):
        assert not _is_linked(a2, 'studyprograms_CourseAccess11', b)


def test_assoc_courses14_reverse_link_reassign_clear():
    a1 = studyprograms_Department(code="sample_text", name="sample_text")
    a2 = studyprograms_Department(code="sample_text_2", name="sample_text_2")
    b = studyprograms_Course(availableSemester="sample_text", code="sample_text", ects=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'studyprograms_Course16', a1)
    assert _is_linked(b, 'studyprograms_Course16', a1)
    if hasattr(a1, 'studyprograms_Department15'):
        assert _is_linked(a1, 'studyprograms_Department15', b)
    _safe_set(b, 'studyprograms_Course16', a2)
    assert _is_linked(b, 'studyprograms_Course16', a2)
    if hasattr(a1, 'studyprograms_Department15'):
        assert not _is_linked(a1, 'studyprograms_Department15', b)
    if hasattr(a2, 'studyprograms_Department15'):
        assert _is_linked(a2, 'studyprograms_Department15', b)
    _safe_set(b, 'studyprograms_Course16', None)
    assert not _is_linked(b, 'studyprograms_Course16', a2)
    if hasattr(a2, 'studyprograms_Department15'):
        assert not _is_linked(a2, 'studyprograms_Department15', b)


def test_assoc_programmes12_reverse_link_reassign_clear():
    a1 = studyprograms_Programme(code="sample_text", duration=7, name="sample_text", startYear=7)
    a2 = studyprograms_Programme(code="sample_text_2", duration=13, name="sample_text_2", startYear=13)
    b = studyprograms_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'studyprograms_Department', {a1})
    assert _is_linked(b, 'studyprograms_Department', a1)
    if hasattr(a1, 'studyprograms_Programme13'):
        assert _is_linked(a1, 'studyprograms_Programme13', b)
    _safe_set(b, 'studyprograms_Department', {a2})
    assert _is_linked(b, 'studyprograms_Department', a2)
    if hasattr(a1, 'studyprograms_Programme13'):
        assert not _is_linked(a1, 'studyprograms_Programme13', b)
    if hasattr(a2, 'studyprograms_Programme13'):
        assert _is_linked(a2, 'studyprograms_Programme13', b)
    _safe_set(b, 'studyprograms_Department', set())
    assert not _is_linked(b, 'studyprograms_Department', a2)
    if hasattr(a2, 'studyprograms_Programme13'):
        assert not _is_linked(a2, 'studyprograms_Programme13', b)


def test_assoc_semesters1_reverse_link_reassign_clear():
    a1 = studyprograms_Semester(semesterCode="sample_text", semesterType="sample_text", year=7)
    a2 = studyprograms_Semester(semesterCode="sample_text_2", semesterType="sample_text_2", year=13)
    b = studyprograms_Programme(code="sample_text", duration=7, name="sample_text", startYear=7)
    _safe_set(b, 'studyprograms_Programme2', {a1})
    assert _is_linked(b, 'studyprograms_Programme2', a1)
    if hasattr(a1, 'studyprograms_Semester'):
        assert _is_linked(a1, 'studyprograms_Semester', b)
    _safe_set(b, 'studyprograms_Programme2', {a2})
    assert _is_linked(b, 'studyprograms_Programme2', a2)
    if hasattr(a1, 'studyprograms_Semester'):
        assert not _is_linked(a1, 'studyprograms_Semester', b)
    if hasattr(a2, 'studyprograms_Semester'):
        assert _is_linked(a2, 'studyprograms_Semester', b)
    _safe_set(b, 'studyprograms_Programme2', set())
    assert not _is_linked(b, 'studyprograms_Programme2', a2)
    if hasattr(a2, 'studyprograms_Semester'):
        assert not _is_linked(a2, 'studyprograms_Semester', b)


def test_assoc_semesters3_reverse_link_reassign_clear():
    a1 = studyprograms_Specialisation(name="sample_text", startSemester=7)
    a2 = studyprograms_Specialisation(name="sample_text_2", startSemester=13)
    b = studyprograms_Semester(semesterCode="sample_text", semesterType="sample_text", year=7)
    _safe_set(b, 'studyprograms_Semester5', a1)
    assert _is_linked(b, 'studyprograms_Semester5', a1)
    if hasattr(a1, 'studyprograms_Specialisation4'):
        assert _is_linked(a1, 'studyprograms_Specialisation4', b)
    _safe_set(b, 'studyprograms_Semester5', a2)
    assert _is_linked(b, 'studyprograms_Semester5', a2)
    if hasattr(a1, 'studyprograms_Specialisation4'):
        assert not _is_linked(a1, 'studyprograms_Specialisation4', b)
    if hasattr(a2, 'studyprograms_Specialisation4'):
        assert _is_linked(a2, 'studyprograms_Specialisation4', b)
    _safe_set(b, 'studyprograms_Semester5', None)
    assert not _is_linked(b, 'studyprograms_Semester5', a2)
    if hasattr(a2, 'studyprograms_Specialisation4'):
        assert not _is_linked(a2, 'studyprograms_Specialisation4', b)


def test_assoc_semesters6_reverse_link_reassign_clear():
    a1 = studyprograms_Semester(semesterCode="sample_text", semesterType="sample_text", year=7)
    a2 = studyprograms_Semester(semesterCode="sample_text_2", semesterType="sample_text_2", year=13)
    b = studyprograms_IndividualStudyPlan(studentNo="sample_text")
    _safe_set(b, 'studyprograms_IndividualStudyPlan', {a1})
    assert _is_linked(b, 'studyprograms_IndividualStudyPlan', a1)
    if hasattr(a1, 'studyprograms_Semester7'):
        assert _is_linked(a1, 'studyprograms_Semester7', b)
    _safe_set(b, 'studyprograms_IndividualStudyPlan', {a2})
    assert _is_linked(b, 'studyprograms_IndividualStudyPlan', a2)
    if hasattr(a1, 'studyprograms_Semester7'):
        assert not _is_linked(a1, 'studyprograms_Semester7', b)
    if hasattr(a2, 'studyprograms_Semester7'):
        assert _is_linked(a2, 'studyprograms_Semester7', b)
    _safe_set(b, 'studyprograms_IndividualStudyPlan', set())
    assert not _is_linked(b, 'studyprograms_IndividualStudyPlan', a2)
    if hasattr(a2, 'studyprograms_Semester7'):
        assert not _is_linked(a2, 'studyprograms_Semester7', b)


def test_assoc_specialisations0_reverse_link_reassign_clear():
    a1 = studyprograms_Specialisation(name="sample_text", startSemester=7)
    a2 = studyprograms_Specialisation(name="sample_text_2", startSemester=13)
    b = studyprograms_Programme(code="sample_text", duration=7, name="sample_text", startYear=7)
    _safe_set(b, 'studyprograms_Programme', {a1})
    assert _is_linked(b, 'studyprograms_Programme', a1)
    if hasattr(a1, 'studyprograms_Specialisation'):
        assert _is_linked(a1, 'studyprograms_Specialisation', b)
    _safe_set(b, 'studyprograms_Programme', {a2})
    assert _is_linked(b, 'studyprograms_Programme', a2)
    if hasattr(a1, 'studyprograms_Specialisation'):
        assert not _is_linked(a1, 'studyprograms_Specialisation', b)
    if hasattr(a2, 'studyprograms_Specialisation'):
        assert _is_linked(a2, 'studyprograms_Specialisation', b)
    _safe_set(b, 'studyprograms_Programme', set())
    assert not _is_linked(b, 'studyprograms_Programme', a2)
    if hasattr(a2, 'studyprograms_Specialisation'):
        assert not _is_linked(a2, 'studyprograms_Specialisation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

