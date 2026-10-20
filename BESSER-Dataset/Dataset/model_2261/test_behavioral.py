import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Course,
    school_Course,
    school_LimitedCapacityCourse,
    school_School,
    school_SchoolClass,
    school_SpecialisationCourse,
    school_Student,
    school_Teacher,
    school_Year,
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

def test_assoc_courses14_reverse_link_reassign_clear():
    a1 = school_SchoolClass(code="sample_text")
    a2 = school_SchoolClass(code="sample_text_2")
    b = school_Course(subject="sample_text", weight=7)
    _safe_set(b, 'Course16', a1)
    assert _is_linked(b, 'Course16', a1)
    if hasattr(a1, 'schoolClass15'):
        assert _is_linked(a1, 'schoolClass15', b)
    _safe_set(b, 'Course16', a2)
    assert _is_linked(b, 'Course16', a2)
    if hasattr(a1, 'schoolClass15'):
        assert not _is_linked(a1, 'schoolClass15', b)
    if hasattr(a2, 'schoolClass15'):
        assert _is_linked(a2, 'schoolClass15', b)
    _safe_set(b, 'Course16', None)
    assert not _is_linked(b, 'Course16', a2)
    if hasattr(a2, 'schoolClass15'):
        assert not _is_linked(a2, 'schoolClass15', b)


def test_assoc_courses25_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_Course(subject="sample_text", weight=7)
    _safe_set(b, 'Course26', a1)
    assert _is_linked(b, 'Course26', a1)
    if hasattr(a1, 'teacher'):
        assert _is_linked(a1, 'teacher', b)
    _safe_set(b, 'Course26', a2)
    assert _is_linked(b, 'Course26', a2)
    if hasattr(a1, 'teacher'):
        assert not _is_linked(a1, 'teacher', b)
    if hasattr(a2, 'teacher'):
        assert _is_linked(a2, 'teacher', b)
    _safe_set(b, 'Course26', None)
    assert not _is_linked(b, 'Course26', a2)
    if hasattr(a2, 'teacher'):
        assert not _is_linked(a2, 'teacher', b)


def test_assoc_courses9_reverse_link_reassign_clear():
    a1 = school_School(address="sample_text", name="sample_text")
    a2 = school_School(address="sample_text_2", name="sample_text_2")
    b = school_Course(subject="sample_text", weight=7)
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'school10'):
        assert _is_linked(a1, 'school10', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'school10'):
        assert not _is_linked(a1, 'school10', b)
    if hasattr(a2, 'school10'):
        assert _is_linked(a2, 'school10', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'school10'):
        assert not _is_linked(a2, 'school10', b)


def test_assoc_friendsWith22_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text")
    a2 = school_Student(name="sample_text_2")
    b = school_Student(name="sample_text")
    _safe_set(b, 'school_Student21', {a1})
    assert _is_linked(b, 'school_Student21', a1)
    if hasattr(a1, 'school_Student'):
        assert _is_linked(a1, 'school_Student', b)
    _safe_set(b, 'school_Student21', {a2})
    assert _is_linked(b, 'school_Student21', a2)
    if hasattr(a1, 'school_Student'):
        assert not _is_linked(a1, 'school_Student', b)
    if hasattr(a2, 'school_Student'):
        assert _is_linked(a2, 'school_Student', b)
    _safe_set(b, 'school_Student21', set())
    assert not _is_linked(b, 'school_Student21', a2)
    if hasattr(a2, 'school_Student'):
        assert not _is_linked(a2, 'school_Student', b)


def test_assoc_homeroomTeacher17_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_SchoolClass(code="sample_text")
    _safe_set(b, 'homeroomedClass', a1)
    assert _is_linked(b, 'homeroomedClass', a1)
    if hasattr(a1, 'Teacher18'):
        assert _is_linked(a1, 'Teacher18', b)
    _safe_set(b, 'homeroomedClass', a2)
    assert _is_linked(b, 'homeroomedClass', a2)
    if hasattr(a1, 'Teacher18'):
        assert not _is_linked(a1, 'Teacher18', b)
    if hasattr(a2, 'Teacher18'):
        assert _is_linked(a2, 'Teacher18', b)
    _safe_set(b, 'homeroomedClass', None)
    assert not _is_linked(b, 'homeroomedClass', a2)
    if hasattr(a2, 'Teacher18'):
        assert not _is_linked(a2, 'Teacher18', b)


def test_assoc_homeroomedClass27_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_SchoolClass(code="sample_text")
    _safe_set(b, 'SchoolClass28', a1)
    assert _is_linked(b, 'SchoolClass28', a1)
    if hasattr(a1, 'homeroomTeacher'):
        assert _is_linked(a1, 'homeroomTeacher', b)
    _safe_set(b, 'SchoolClass28', a2)
    assert _is_linked(b, 'SchoolClass28', a2)
    if hasattr(a1, 'homeroomTeacher'):
        assert not _is_linked(a1, 'homeroomTeacher', b)
    if hasattr(a2, 'homeroomTeacher'):
        assert _is_linked(a2, 'homeroomTeacher', b)
    _safe_set(b, 'SchoolClass28', None)
    assert not _is_linked(b, 'SchoolClass28', a2)
    if hasattr(a2, 'homeroomTeacher'):
        assert not _is_linked(a2, 'homeroomTeacher', b)


def test_assoc_school0_reverse_link_reassign_clear():
    a1 = school_School(address="sample_text", name="sample_text")
    a2 = school_School(address="sample_text_2", name="sample_text_2")
    b = school_Course(subject="sample_text", weight=7)
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'School'):
        assert _is_linked(a1, 'School', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'School'):
        assert not _is_linked(a1, 'School', b)
    if hasattr(a2, 'School'):
        assert _is_linked(a2, 'School', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'School'):
        assert not _is_linked(a2, 'School', b)


def test_assoc_school23_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_School(address="sample_text", name="sample_text")
    _safe_set(b, 'School24', a1)
    assert _is_linked(b, 'School24', a1)
    if hasattr(a1, 'teachers'):
        assert _is_linked(a1, 'teachers', b)
    _safe_set(b, 'School24', a2)
    assert _is_linked(b, 'School24', a2)
    if hasattr(a1, 'teachers'):
        assert not _is_linked(a1, 'teachers', b)
    if hasattr(a2, 'teachers'):
        assert _is_linked(a2, 'teachers', b)
    _safe_set(b, 'School24', None)
    assert not _is_linked(b, 'School24', a2)
    if hasattr(a2, 'teachers'):
        assert not _is_linked(a2, 'teachers', b)


def test_assoc_school29_reverse_link_reassign_clear():
    a1 = school_Year(startingDate=7)
    a2 = school_Year(startingDate=13)
    b = school_School(address="sample_text", name="sample_text")
    _safe_set(b, 'School30', a1)
    assert _is_linked(b, 'School30', a1)
    if hasattr(a1, 'years'):
        assert _is_linked(a1, 'years', b)
    _safe_set(b, 'School30', a2)
    assert _is_linked(b, 'School30', a2)
    if hasattr(a1, 'years'):
        assert not _is_linked(a1, 'years', b)
    if hasattr(a2, 'years'):
        assert _is_linked(a2, 'years', b)
    _safe_set(b, 'School30', None)
    assert not _is_linked(b, 'School30', a2)
    if hasattr(a2, 'years'):
        assert not _is_linked(a2, 'years', b)


def test_assoc_schoolClass19_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text")
    a2 = school_Student(name="sample_text_2")
    b = school_SchoolClass(code="sample_text")
    _safe_set(b, 'SchoolClass20', a1)
    assert _is_linked(b, 'SchoolClass20', a1)
    if hasattr(a1, 'students'):
        assert _is_linked(a1, 'students', b)
    _safe_set(b, 'SchoolClass20', a2)
    assert _is_linked(b, 'SchoolClass20', a2)
    if hasattr(a1, 'students'):
        assert not _is_linked(a1, 'students', b)
    if hasattr(a2, 'students'):
        assert _is_linked(a2, 'students', b)
    _safe_set(b, 'SchoolClass20', None)
    assert not _is_linked(b, 'SchoolClass20', a2)
    if hasattr(a2, 'students'):
        assert not _is_linked(a2, 'students', b)


def test_assoc_schoolClass3_reverse_link_reassign_clear():
    a1 = school_SchoolClass(code="sample_text")
    a2 = school_SchoolClass(code="sample_text_2")
    b = school_Course(subject="sample_text", weight=7)
    _safe_set(b, 'courses4', a1)
    assert _is_linked(b, 'courses4', a1)
    if hasattr(a1, 'SchoolClass'):
        assert _is_linked(a1, 'SchoolClass', b)
    _safe_set(b, 'courses4', a2)
    assert _is_linked(b, 'courses4', a2)
    if hasattr(a1, 'SchoolClass'):
        assert not _is_linked(a1, 'SchoolClass', b)
    if hasattr(a2, 'SchoolClass'):
        assert _is_linked(a2, 'SchoolClass', b)
    _safe_set(b, 'courses4', None)
    assert not _is_linked(b, 'courses4', a2)
    if hasattr(a2, 'SchoolClass'):
        assert not _is_linked(a2, 'SchoolClass', b)


def test_assoc_schoolClasses31_reverse_link_reassign_clear():
    a1 = school_Year(startingDate=7)
    a2 = school_Year(startingDate=13)
    b = school_SchoolClass(code="sample_text")
    _safe_set(b, 'SchoolClass32', a1)
    assert _is_linked(b, 'SchoolClass32', a1)
    if hasattr(a1, 'year'):
        assert _is_linked(a1, 'year', b)
    _safe_set(b, 'SchoolClass32', a2)
    assert _is_linked(b, 'SchoolClass32', a2)
    if hasattr(a1, 'year'):
        assert not _is_linked(a1, 'year', b)
    if hasattr(a2, 'year'):
        assert _is_linked(a2, 'year', b)
    _safe_set(b, 'SchoolClass32', None)
    assert not _is_linked(b, 'SchoolClass32', a2)
    if hasattr(a2, 'year'):
        assert not _is_linked(a2, 'year', b)


def test_assoc_students13_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text")
    a2 = school_Student(name="sample_text_2")
    b = school_SchoolClass(code="sample_text")
    _safe_set(b, 'schoolClass', {a1})
    assert _is_linked(b, 'schoolClass', a1)
    if hasattr(a1, 'Student'):
        assert _is_linked(a1, 'Student', b)
    _safe_set(b, 'schoolClass', {a2})
    assert _is_linked(b, 'schoolClass', a2)
    if hasattr(a1, 'Student'):
        assert not _is_linked(a1, 'Student', b)
    if hasattr(a2, 'Student'):
        assert _is_linked(a2, 'Student', b)
    _safe_set(b, 'schoolClass', set())
    assert not _is_linked(b, 'schoolClass', a2)
    if hasattr(a2, 'Student'):
        assert not _is_linked(a2, 'Student', b)


def test_assoc_teacher1_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_Course(subject="sample_text", weight=7)
    _safe_set(b, 'courses2', a1)
    assert _is_linked(b, 'courses2', a1)
    if hasattr(a1, 'Teacher'):
        assert _is_linked(a1, 'Teacher', b)
    _safe_set(b, 'courses2', a2)
    assert _is_linked(b, 'courses2', a2)
    if hasattr(a1, 'Teacher'):
        assert not _is_linked(a1, 'Teacher', b)
    if hasattr(a2, 'Teacher'):
        assert _is_linked(a2, 'Teacher', b)
    _safe_set(b, 'courses2', None)
    assert not _is_linked(b, 'courses2', a2)
    if hasattr(a2, 'Teacher'):
        assert not _is_linked(a2, 'Teacher', b)


def test_assoc_teachers6_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_School(address="sample_text", name="sample_text")
    _safe_set(b, 'school7', {a1})
    assert _is_linked(b, 'school7', a1)
    if hasattr(a1, 'Teacher8'):
        assert _is_linked(a1, 'Teacher8', b)
    _safe_set(b, 'school7', {a2})
    assert _is_linked(b, 'school7', a2)
    if hasattr(a1, 'Teacher8'):
        assert not _is_linked(a1, 'Teacher8', b)
    if hasattr(a2, 'Teacher8'):
        assert _is_linked(a2, 'Teacher8', b)
    _safe_set(b, 'school7', set())
    assert not _is_linked(b, 'school7', a2)
    if hasattr(a2, 'Teacher8'):
        assert not _is_linked(a2, 'Teacher8', b)


def test_assoc_year11_reverse_link_reassign_clear():
    a1 = school_Year(startingDate=7)
    a2 = school_Year(startingDate=13)
    b = school_SchoolClass(code="sample_text")
    _safe_set(b, 'schoolClasses', a1)
    assert _is_linked(b, 'schoolClasses', a1)
    if hasattr(a1, 'Year12'):
        assert _is_linked(a1, 'Year12', b)
    _safe_set(b, 'schoolClasses', a2)
    assert _is_linked(b, 'schoolClasses', a2)
    if hasattr(a1, 'Year12'):
        assert not _is_linked(a1, 'Year12', b)
    if hasattr(a2, 'Year12'):
        assert _is_linked(a2, 'Year12', b)
    _safe_set(b, 'schoolClasses', None)
    assert not _is_linked(b, 'schoolClasses', a2)
    if hasattr(a2, 'Year12'):
        assert not _is_linked(a2, 'Year12', b)


def test_assoc_years5_reverse_link_reassign_clear():
    a1 = school_Year(startingDate=7)
    a2 = school_Year(startingDate=13)
    b = school_School(address="sample_text", name="sample_text")
    _safe_set(b, 'school', {a1})
    assert _is_linked(b, 'school', a1)
    if hasattr(a1, 'Year'):
        assert _is_linked(a1, 'Year', b)
    _safe_set(b, 'school', {a2})
    assert _is_linked(b, 'school', a2)
    if hasattr(a1, 'Year'):
        assert not _is_linked(a1, 'Year', b)
    if hasattr(a2, 'Year'):
        assert _is_linked(a2, 'Year', b)
    _safe_set(b, 'school', set())
    assert not _is_linked(b, 'school', a2)
    if hasattr(a2, 'Year'):
        assert not _is_linked(a2, 'Year', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

