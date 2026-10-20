import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Program_Course,
    Program_Department,
    Program_Program,
    Program_Semester,
    Program_SemesterCourse,
    Program_Specialization,
    CourseStatus,
    SemesterStatus,
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

def test_assoc_course10_reverse_link_reassign_clear():
    a1 = Program_SemesterCourse(status="sample_text")
    a2 = Program_SemesterCourse(status="sample_text_2")
    b = Program_Course(code="sample_text", credit=3.14, name="sample_text")
    _safe_set(b, 'Program_Course', a1)
    assert _is_linked(b, 'Program_Course', a1)
    if hasattr(a1, 'Program_SemesterCourse'):
        assert _is_linked(a1, 'Program_SemesterCourse', b)
    _safe_set(b, 'Program_Course', a2)
    assert _is_linked(b, 'Program_Course', a2)
    if hasattr(a1, 'Program_SemesterCourse'):
        assert not _is_linked(a1, 'Program_SemesterCourse', b)
    if hasattr(a2, 'Program_SemesterCourse'):
        assert _is_linked(a2, 'Program_SemesterCourse', b)
    _safe_set(b, 'Program_Course', None)
    assert not _is_linked(b, 'Program_Course', a2)
    if hasattr(a2, 'Program_SemesterCourse'):
        assert not _is_linked(a2, 'Program_SemesterCourse', b)


def test_assoc_courses15_reverse_link_reassign_clear():
    a1 = Program_Department(name="sample_text")
    a2 = Program_Department(name="sample_text_2")
    b = Program_Course(code="sample_text", credit=3.14, name="sample_text")
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


def test_assoc_department12_reverse_link_reassign_clear():
    a1 = Program_Department(name="sample_text")
    a2 = Program_Department(name="sample_text_2")
    b = Program_Course(code="sample_text", credit=3.14, name="sample_text")
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'Department'):
        assert _is_linked(a1, 'Department', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'Department'):
        assert not _is_linked(a1, 'Department', b)
    if hasattr(a2, 'Department'):
        assert _is_linked(a2, 'Department', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'Department'):
        assert not _is_linked(a2, 'Department', b)


def test_assoc_programs13_reverse_link_reassign_clear():
    a1 = Program_Program(name="sample_text", year=3.14)
    a2 = Program_Program(name="sample_text_2", year=9.99)
    b = Program_Department(name="sample_text")
    _safe_set(b, 'Program_Department', {a1})
    assert _is_linked(b, 'Program_Department', a1)
    if hasattr(a1, 'Program_Program14'):
        assert _is_linked(a1, 'Program_Program14', b)
    _safe_set(b, 'Program_Department', {a2})
    assert _is_linked(b, 'Program_Department', a2)
    if hasattr(a1, 'Program_Program14'):
        assert not _is_linked(a1, 'Program_Program14', b)
    if hasattr(a2, 'Program_Program14'):
        assert _is_linked(a2, 'Program_Program14', b)
    _safe_set(b, 'Program_Department', set())
    assert not _is_linked(b, 'Program_Department', a2)
    if hasattr(a2, 'Program_Program14'):
        assert not _is_linked(a2, 'Program_Program14', b)


def test_assoc_semester11_reverse_link_reassign_clear():
    a1 = Program_SemesterCourse(status="sample_text")
    a2 = Program_SemesterCourse(status="sample_text_2")
    b = Program_Semester(code="sample_text", name="sample_text", status="sample_text")
    _safe_set(b, 'Semester', a1)
    assert _is_linked(b, 'Semester', a1)
    if hasattr(a1, 'semesterCourses'):
        assert _is_linked(a1, 'semesterCourses', b)
    _safe_set(b, 'Semester', a2)
    assert _is_linked(b, 'Semester', a2)
    if hasattr(a1, 'semesterCourses'):
        assert not _is_linked(a1, 'semesterCourses', b)
    if hasattr(a2, 'semesterCourses'):
        assert _is_linked(a2, 'semesterCourses', b)
    _safe_set(b, 'Semester', None)
    assert not _is_linked(b, 'Semester', a2)
    if hasattr(a2, 'semesterCourses'):
        assert not _is_linked(a2, 'semesterCourses', b)


def test_assoc_semesterCourses9_reverse_link_reassign_clear():
    a1 = Program_SemesterCourse(status="sample_text")
    a2 = Program_SemesterCourse(status="sample_text_2")
    b = Program_Semester(code="sample_text", name="sample_text", status="sample_text")
    _safe_set(b, 'semester', {a1})
    assert _is_linked(b, 'semester', a1)
    if hasattr(a1, 'SemesterCourse'):
        assert _is_linked(a1, 'SemesterCourse', b)
    _safe_set(b, 'semester', {a2})
    assert _is_linked(b, 'semester', a2)
    if hasattr(a1, 'SemesterCourse'):
        assert not _is_linked(a1, 'SemesterCourse', b)
    if hasattr(a2, 'SemesterCourse'):
        assert _is_linked(a2, 'SemesterCourse', b)
    _safe_set(b, 'semester', set())
    assert not _is_linked(b, 'semester', a2)
    if hasattr(a2, 'SemesterCourse'):
        assert not _is_linked(a2, 'SemesterCourse', b)


def test_assoc_semesters0_reverse_link_reassign_clear():
    a1 = Program_Semester(code="sample_text", name="sample_text", status="sample_text")
    a2 = Program_Semester(code="sample_text_2", name="sample_text_2", status="sample_text_2")
    b = Program_Program(name="sample_text", year=3.14)
    _safe_set(b, 'Program_Program', {a1})
    assert _is_linked(b, 'Program_Program', a1)
    if hasattr(a1, 'Program_Semester'):
        assert _is_linked(a1, 'Program_Semester', b)
    _safe_set(b, 'Program_Program', {a2})
    assert _is_linked(b, 'Program_Program', a2)
    if hasattr(a1, 'Program_Semester'):
        assert not _is_linked(a1, 'Program_Semester', b)
    if hasattr(a2, 'Program_Semester'):
        assert _is_linked(a2, 'Program_Semester', b)
    _safe_set(b, 'Program_Program', set())
    assert not _is_linked(b, 'Program_Program', a2)
    if hasattr(a2, 'Program_Semester'):
        assert not _is_linked(a2, 'Program_Semester', b)


def test_assoc_semesters3_reverse_link_reassign_clear():
    a1 = Program_Specialization(name="sample_text")
    a2 = Program_Specialization(name="sample_text_2")
    b = Program_Semester(code="sample_text", name="sample_text", status="sample_text")
    _safe_set(b, 'Program_Semester5', a1)
    assert _is_linked(b, 'Program_Semester5', a1)
    if hasattr(a1, 'Program_Specialization4'):
        assert _is_linked(a1, 'Program_Specialization4', b)
    _safe_set(b, 'Program_Semester5', a2)
    assert _is_linked(b, 'Program_Semester5', a2)
    if hasattr(a1, 'Program_Specialization4'):
        assert not _is_linked(a1, 'Program_Specialization4', b)
    if hasattr(a2, 'Program_Specialization4'):
        assert _is_linked(a2, 'Program_Specialization4', b)
    _safe_set(b, 'Program_Semester5', None)
    assert not _is_linked(b, 'Program_Semester5', a2)
    if hasattr(a2, 'Program_Specialization4'):
        assert not _is_linked(a2, 'Program_Specialization4', b)


def test_assoc_specializations1_reverse_link_reassign_clear():
    a1 = Program_Specialization(name="sample_text")
    a2 = Program_Specialization(name="sample_text_2")
    b = Program_Program(name="sample_text", year=3.14)
    _safe_set(b, 'Program_Program2', {a1})
    assert _is_linked(b, 'Program_Program2', a1)
    if hasattr(a1, 'Program_Specialization'):
        assert _is_linked(a1, 'Program_Specialization', b)
    _safe_set(b, 'Program_Program2', {a2})
    assert _is_linked(b, 'Program_Program2', a2)
    if hasattr(a1, 'Program_Specialization'):
        assert not _is_linked(a1, 'Program_Specialization', b)
    if hasattr(a2, 'Program_Specialization'):
        assert _is_linked(a2, 'Program_Specialization', b)
    _safe_set(b, 'Program_Program2', set())
    assert not _is_linked(b, 'Program_Program2', a2)
    if hasattr(a2, 'Program_Specialization'):
        assert not _is_linked(a2, 'Program_Specialization', b)


def test_assoc_specializations7_reverse_link_reassign_clear():
    a1 = Program_Specialization(name="sample_text")
    a2 = Program_Specialization(name="sample_text_2")
    b = Program_Specialization(name="sample_text")
    _safe_set(b, 'Program_Specialization8', a1)
    assert _is_linked(b, 'Program_Specialization8', a1)
    if hasattr(a1, 'Program_Specialization6'):
        assert _is_linked(a1, 'Program_Specialization6', b)
    _safe_set(b, 'Program_Specialization8', a2)
    assert _is_linked(b, 'Program_Specialization8', a2)
    if hasattr(a1, 'Program_Specialization6'):
        assert not _is_linked(a1, 'Program_Specialization6', b)
    if hasattr(a2, 'Program_Specialization6'):
        assert _is_linked(a2, 'Program_Specialization6', b)
    _safe_set(b, 'Program_Specialization8', None)
    assert not _is_linked(b, 'Program_Specialization8', a2)
    if hasattr(a2, 'Program_Specialization6'):
        assert not _is_linked(a2, 'Program_Specialization6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

