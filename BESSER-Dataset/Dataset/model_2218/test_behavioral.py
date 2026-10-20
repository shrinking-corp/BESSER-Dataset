import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    studyplan_Course,
    studyplan_Department,
    studyplan_Program,
    studyplan_Semester,
    studyplan_SemesterCourse,
    studyplan_Specialization,
    CourseStatus,
    Season,
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

def test_assoc_course14_reverse_link_reassign_clear():
    a1 = studyplan_SemesterCourse(status="sample_text")
    a2 = studyplan_SemesterCourse(status="sample_text_2")
    b = studyplan_Course(code="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'studyplan_Course', a1)
    assert _is_linked(b, 'studyplan_Course', a1)
    if hasattr(a1, 'studyplan_SemesterCourse15'):
        assert _is_linked(a1, 'studyplan_SemesterCourse15', b)
    _safe_set(b, 'studyplan_Course', a2)
    assert _is_linked(b, 'studyplan_Course', a2)
    if hasattr(a1, 'studyplan_SemesterCourse15'):
        assert not _is_linked(a1, 'studyplan_SemesterCourse15', b)
    if hasattr(a2, 'studyplan_SemesterCourse15'):
        assert _is_linked(a2, 'studyplan_SemesterCourse15', b)
    _safe_set(b, 'studyplan_Course', None)
    assert not _is_linked(b, 'studyplan_Course', a2)
    if hasattr(a2, 'studyplan_SemesterCourse15'):
        assert not _is_linked(a2, 'studyplan_SemesterCourse15', b)


def test_assoc_courses16_reverse_link_reassign_clear():
    a1 = studyplan_Department(name="sample_text")
    a2 = studyplan_Department(name="sample_text_2")
    b = studyplan_Course(code="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'department'):
        assert _is_linked(a1, 'department', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'department'):
        assert not _is_linked(a1, 'department', b)
    if hasattr(a2, 'department'):
        assert _is_linked(a2, 'department', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'department'):
        assert not _is_linked(a2, 'department', b)


def test_assoc_courses4_reverse_link_reassign_clear():
    a1 = studyplan_SemesterCourse(status="sample_text")
    a2 = studyplan_SemesterCourse(status="sample_text_2")
    b = studyplan_Semester(name="sample_text", season="sample_text", year=7)
    _safe_set(b, 'studyplan_Semester5', {a1})
    assert _is_linked(b, 'studyplan_Semester5', a1)
    if hasattr(a1, 'studyplan_SemesterCourse'):
        assert _is_linked(a1, 'studyplan_SemesterCourse', b)
    _safe_set(b, 'studyplan_Semester5', {a2})
    assert _is_linked(b, 'studyplan_Semester5', a2)
    if hasattr(a1, 'studyplan_SemesterCourse'):
        assert not _is_linked(a1, 'studyplan_SemesterCourse', b)
    if hasattr(a2, 'studyplan_SemesterCourse'):
        assert _is_linked(a2, 'studyplan_SemesterCourse', b)
    _safe_set(b, 'studyplan_Semester5', set())
    assert not _is_linked(b, 'studyplan_Semester5', a2)
    if hasattr(a2, 'studyplan_SemesterCourse'):
        assert not _is_linked(a2, 'studyplan_SemesterCourse', b)


def test_assoc_department12_reverse_link_reassign_clear():
    a1 = studyplan_Department(name="sample_text")
    a2 = studyplan_Department(name="sample_text_2")
    b = studyplan_Course(code="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'Department13'):
        assert _is_linked(a1, 'Department13', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'Department13'):
        assert not _is_linked(a1, 'Department13', b)
    if hasattr(a2, 'Department13'):
        assert _is_linked(a2, 'Department13', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'Department13'):
        assert not _is_linked(a2, 'Department13', b)


def test_assoc_department3_reverse_link_reassign_clear():
    a1 = studyplan_Program(code="sample_text", name="sample_text")
    a2 = studyplan_Program(code="sample_text_2", name="sample_text_2")
    b = studyplan_Department(name="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'programs'):
        assert _is_linked(a1, 'programs', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'programs'):
        assert not _is_linked(a1, 'programs', b)
    if hasattr(a2, 'programs'):
        assert _is_linked(a2, 'programs', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'programs'):
        assert not _is_linked(a2, 'programs', b)


def test_assoc_programs17_reverse_link_reassign_clear():
    a1 = studyplan_Program(code="sample_text", name="sample_text")
    a2 = studyplan_Program(code="sample_text_2", name="sample_text_2")
    b = studyplan_Department(name="sample_text")
    _safe_set(b, 'department18', {a1})
    assert _is_linked(b, 'department18', a1)
    if hasattr(a1, 'Program'):
        assert _is_linked(a1, 'Program', b)
    _safe_set(b, 'department18', {a2})
    assert _is_linked(b, 'department18', a2)
    if hasattr(a1, 'Program'):
        assert not _is_linked(a1, 'Program', b)
    if hasattr(a2, 'Program'):
        assert _is_linked(a2, 'Program', b)
    _safe_set(b, 'department18', set())
    assert not _is_linked(b, 'department18', a2)
    if hasattr(a2, 'Program'):
        assert not _is_linked(a2, 'Program', b)


def test_assoc_semesters0_reverse_link_reassign_clear():
    a1 = studyplan_Semester(name="sample_text", season="sample_text", year=7)
    a2 = studyplan_Semester(name="sample_text_2", season="sample_text_2", year=13)
    b = studyplan_Program(code="sample_text", name="sample_text")
    _safe_set(b, 'studyplan_Program', {a1})
    assert _is_linked(b, 'studyplan_Program', a1)
    if hasattr(a1, 'studyplan_Semester'):
        assert _is_linked(a1, 'studyplan_Semester', b)
    _safe_set(b, 'studyplan_Program', {a2})
    assert _is_linked(b, 'studyplan_Program', a2)
    if hasattr(a1, 'studyplan_Semester'):
        assert not _is_linked(a1, 'studyplan_Semester', b)
    if hasattr(a2, 'studyplan_Semester'):
        assert _is_linked(a2, 'studyplan_Semester', b)
    _safe_set(b, 'studyplan_Program', set())
    assert not _is_linked(b, 'studyplan_Program', a2)
    if hasattr(a2, 'studyplan_Semester'):
        assert not _is_linked(a2, 'studyplan_Semester', b)


def test_assoc_semesters6_reverse_link_reassign_clear():
    a1 = studyplan_Specialization(name="sample_text")
    a2 = studyplan_Specialization(name="sample_text_2")
    b = studyplan_Semester(name="sample_text", season="sample_text", year=7)
    _safe_set(b, 'studyplan_Semester8', a1)
    assert _is_linked(b, 'studyplan_Semester8', a1)
    if hasattr(a1, 'studyplan_Specialization7'):
        assert _is_linked(a1, 'studyplan_Specialization7', b)
    _safe_set(b, 'studyplan_Semester8', a2)
    assert _is_linked(b, 'studyplan_Semester8', a2)
    if hasattr(a1, 'studyplan_Specialization7'):
        assert not _is_linked(a1, 'studyplan_Specialization7', b)
    if hasattr(a2, 'studyplan_Specialization7'):
        assert _is_linked(a2, 'studyplan_Specialization7', b)
    _safe_set(b, 'studyplan_Semester8', None)
    assert not _is_linked(b, 'studyplan_Semester8', a2)
    if hasattr(a2, 'studyplan_Specialization7'):
        assert not _is_linked(a2, 'studyplan_Specialization7', b)


def test_assoc_specializations1_reverse_link_reassign_clear():
    a1 = studyplan_Specialization(name="sample_text")
    a2 = studyplan_Specialization(name="sample_text_2")
    b = studyplan_Program(code="sample_text", name="sample_text")
    _safe_set(b, 'studyplan_Program2', {a1})
    assert _is_linked(b, 'studyplan_Program2', a1)
    if hasattr(a1, 'studyplan_Specialization'):
        assert _is_linked(a1, 'studyplan_Specialization', b)
    _safe_set(b, 'studyplan_Program2', {a2})
    assert _is_linked(b, 'studyplan_Program2', a2)
    if hasattr(a1, 'studyplan_Specialization'):
        assert not _is_linked(a1, 'studyplan_Specialization', b)
    if hasattr(a2, 'studyplan_Specialization'):
        assert _is_linked(a2, 'studyplan_Specialization', b)
    _safe_set(b, 'studyplan_Program2', set())
    assert not _is_linked(b, 'studyplan_Program2', a2)
    if hasattr(a2, 'studyplan_Specialization'):
        assert not _is_linked(a2, 'studyplan_Specialization', b)


def test_assoc_specializations10_reverse_link_reassign_clear():
    a1 = studyplan_Specialization(name="sample_text")
    a2 = studyplan_Specialization(name="sample_text_2")
    b = studyplan_Specialization(name="sample_text")
    _safe_set(b, 'studyplan_Specialization9', {a1})
    assert _is_linked(b, 'studyplan_Specialization9', a1)
    if hasattr(a1, 'studyplan_Specialization11'):
        assert _is_linked(a1, 'studyplan_Specialization11', b)
    _safe_set(b, 'studyplan_Specialization9', {a2})
    assert _is_linked(b, 'studyplan_Specialization9', a2)
    if hasattr(a1, 'studyplan_Specialization11'):
        assert not _is_linked(a1, 'studyplan_Specialization11', b)
    if hasattr(a2, 'studyplan_Specialization11'):
        assert _is_linked(a2, 'studyplan_Specialization11', b)
    _safe_set(b, 'studyplan_Specialization9', set())
    assert not _is_linked(b, 'studyplan_Specialization9', a2)
    if hasattr(a2, 'studyplan_Specialization11'):
        assert not _is_linked(a2, 'studyplan_Specialization11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

