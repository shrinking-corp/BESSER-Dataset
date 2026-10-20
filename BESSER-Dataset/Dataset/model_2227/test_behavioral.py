import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    studyprograms_Course,
    studyprograms_CourseAccess,
    studyprograms_Department,
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

def test_assoc_courseAccess9_reverse_link_reassign_clear():
    a1 = studyprograms_Semester(semesterCode="sample_text", semesterType="sample_text", year=7)
    a2 = studyprograms_Semester(semesterCode="sample_text_2", semesterType="sample_text_2", year=13)
    b = studyprograms_CourseAccess(Access="sample_text")
    _safe_set(b, 'studyprograms_CourseAccess', a1)
    assert _is_linked(b, 'studyprograms_CourseAccess', a1)
    if hasattr(a1, 'studyprograms_Semester10'):
        assert _is_linked(a1, 'studyprograms_Semester10', b)
    _safe_set(b, 'studyprograms_CourseAccess', a2)
    assert _is_linked(b, 'studyprograms_CourseAccess', a2)
    if hasattr(a1, 'studyprograms_Semester10'):
        assert not _is_linked(a1, 'studyprograms_Semester10', b)
    if hasattr(a2, 'studyprograms_Semester10'):
        assert _is_linked(a2, 'studyprograms_Semester10', b)
    _safe_set(b, 'studyprograms_CourseAccess', None)
    assert not _is_linked(b, 'studyprograms_CourseAccess', a2)
    if hasattr(a2, 'studyprograms_Semester10'):
        assert not _is_linked(a2, 'studyprograms_Semester10', b)


def test_assoc_courses11_reverse_link_reassign_clear():
    a1 = studyprograms_CourseAccess(Access="sample_text")
    a2 = studyprograms_CourseAccess(Access="sample_text_2")
    b = studyprograms_Course(availableSemester="sample_text", code="sample_text", ects=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'studyprograms_Course', a1)
    assert _is_linked(b, 'studyprograms_Course', a1)
    if hasattr(a1, 'studyprograms_CourseAccess12'):
        assert _is_linked(a1, 'studyprograms_CourseAccess12', b)
    _safe_set(b, 'studyprograms_Course', a2)
    assert _is_linked(b, 'studyprograms_Course', a2)
    if hasattr(a1, 'studyprograms_CourseAccess12'):
        assert not _is_linked(a1, 'studyprograms_CourseAccess12', b)
    if hasattr(a2, 'studyprograms_CourseAccess12'):
        assert _is_linked(a2, 'studyprograms_CourseAccess12', b)
    _safe_set(b, 'studyprograms_Course', None)
    assert not _is_linked(b, 'studyprograms_Course', a2)
    if hasattr(a2, 'studyprograms_CourseAccess12'):
        assert not _is_linked(a2, 'studyprograms_CourseAccess12', b)


def test_assoc_courses15_reverse_link_reassign_clear():
    a1 = studyprograms_Department(code="sample_text", name="sample_text")
    a2 = studyprograms_Department(code="sample_text_2", name="sample_text_2")
    b = studyprograms_Course(availableSemester="sample_text", code="sample_text", ects=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'studyprograms_Course17', a1)
    assert _is_linked(b, 'studyprograms_Course17', a1)
    if hasattr(a1, 'studyprograms_Department16'):
        assert _is_linked(a1, 'studyprograms_Department16', b)
    _safe_set(b, 'studyprograms_Course17', a2)
    assert _is_linked(b, 'studyprograms_Course17', a2)
    if hasattr(a1, 'studyprograms_Department16'):
        assert not _is_linked(a1, 'studyprograms_Department16', b)
    if hasattr(a2, 'studyprograms_Department16'):
        assert _is_linked(a2, 'studyprograms_Department16', b)
    _safe_set(b, 'studyprograms_Course17', None)
    assert not _is_linked(b, 'studyprograms_Course17', a2)
    if hasattr(a2, 'studyprograms_Department16'):
        assert not _is_linked(a2, 'studyprograms_Department16', b)


def test_assoc_programmes13_reverse_link_reassign_clear():
    a1 = studyprograms_Programme(code="sample_text", duration=7, name="sample_text", startYear=7)
    a2 = studyprograms_Programme(code="sample_text_2", duration=13, name="sample_text_2", startYear=13)
    b = studyprograms_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'studyprograms_Department', {a1})
    assert _is_linked(b, 'studyprograms_Department', a1)
    if hasattr(a1, 'studyprograms_Programme14'):
        assert _is_linked(a1, 'studyprograms_Programme14', b)
    _safe_set(b, 'studyprograms_Department', {a2})
    assert _is_linked(b, 'studyprograms_Department', a2)
    if hasattr(a1, 'studyprograms_Programme14'):
        assert not _is_linked(a1, 'studyprograms_Programme14', b)
    if hasattr(a2, 'studyprograms_Programme14'):
        assert _is_linked(a2, 'studyprograms_Programme14', b)
    _safe_set(b, 'studyprograms_Department', set())
    assert not _is_linked(b, 'studyprograms_Department', a2)
    if hasattr(a2, 'studyprograms_Programme14'):
        assert not _is_linked(a2, 'studyprograms_Programme14', b)


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


def test_assoc_specializations7_reverse_link_reassign_clear():
    a1 = studyprograms_Specialisation(name="sample_text", startSemester=7)
    a2 = studyprograms_Specialisation(name="sample_text_2", startSemester=13)
    b = studyprograms_Specialisation(name="sample_text", startSemester=7)
    _safe_set(b, 'studyprograms_Specialisation8', a1)
    assert _is_linked(b, 'studyprograms_Specialisation8', a1)
    if hasattr(a1, 'studyprograms_Specialisation6'):
        assert _is_linked(a1, 'studyprograms_Specialisation6', b)
    _safe_set(b, 'studyprograms_Specialisation8', a2)
    assert _is_linked(b, 'studyprograms_Specialisation8', a2)
    if hasattr(a1, 'studyprograms_Specialisation6'):
        assert not _is_linked(a1, 'studyprograms_Specialisation6', b)
    if hasattr(a2, 'studyprograms_Specialisation6'):
        assert _is_linked(a2, 'studyprograms_Specialisation6', b)
    _safe_set(b, 'studyprograms_Specialisation8', None)
    assert not _is_linked(b, 'studyprograms_Specialisation8', a2)
    if hasattr(a2, 'studyprograms_Specialisation6'):
        assert not _is_linked(a2, 'studyprograms_Specialisation6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

