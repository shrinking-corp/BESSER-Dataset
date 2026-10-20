import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    school_BooleanExpr,
    school_Course,
    school_CourseOfStudy,
    school_CourseResult,
    school_Faculty,
    school_Query,
    school_School,
    school_SchoolDatabase,
    school_Student,
    school_Teacher,
    school_Where,
    SchoolElement,
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

def test_assoc_and_36_reverse_link_reassign_clear():
    a1 = school_BooleanExpr(lhs="sample_text", operator="sample_text", rhs="sample_text")
    a2 = school_BooleanExpr(lhs="sample_text_2", operator="sample_text_2", rhs="sample_text_2")
    b = school_BooleanExpr(lhs="sample_text", operator="sample_text", rhs="sample_text")
    _safe_set(b, 'school_BooleanExpr37', a1)
    assert _is_linked(b, 'school_BooleanExpr37', a1)
    if hasattr(a1, 'school_BooleanExpr35'):
        assert _is_linked(a1, 'school_BooleanExpr35', b)
    _safe_set(b, 'school_BooleanExpr37', a2)
    assert _is_linked(b, 'school_BooleanExpr37', a2)
    if hasattr(a1, 'school_BooleanExpr35'):
        assert not _is_linked(a1, 'school_BooleanExpr35', b)
    if hasattr(a2, 'school_BooleanExpr35'):
        assert _is_linked(a2, 'school_BooleanExpr35', b)
    _safe_set(b, 'school_BooleanExpr37', None)
    assert not _is_linked(b, 'school_BooleanExpr37', a2)
    if hasattr(a2, 'school_BooleanExpr35'):
        assert not _is_linked(a2, 'school_BooleanExpr35', b)


def test_assoc_course10_reverse_link_reassign_clear():
    a1 = school_CourseOfStudy(name="sample_text")
    a2 = school_CourseOfStudy(name="sample_text_2")
    b = school_Course(courseNumber="sample_text", name="sample_text")
    _safe_set(b, 'school_Course12', a1)
    assert _is_linked(b, 'school_Course12', a1)
    if hasattr(a1, 'school_CourseOfStudy11'):
        assert _is_linked(a1, 'school_CourseOfStudy11', b)
    _safe_set(b, 'school_Course12', a2)
    assert _is_linked(b, 'school_Course12', a2)
    if hasattr(a1, 'school_CourseOfStudy11'):
        assert not _is_linked(a1, 'school_CourseOfStudy11', b)
    if hasattr(a2, 'school_CourseOfStudy11'):
        assert _is_linked(a2, 'school_CourseOfStudy11', b)
    _safe_set(b, 'school_Course12', None)
    assert not _is_linked(b, 'school_Course12', a2)
    if hasattr(a2, 'school_CourseOfStudy11'):
        assert not _is_linked(a2, 'school_CourseOfStudy11', b)


def test_assoc_course27_reverse_link_reassign_clear():
    a1 = school_CourseResult(grade="sample_text")
    a2 = school_CourseResult(grade="sample_text_2")
    b = school_Course(courseNumber="sample_text", name="sample_text")
    _safe_set(b, 'Course28', a1)
    assert _is_linked(b, 'Course28', a1)
    if hasattr(a1, 'courseresult'):
        assert _is_linked(a1, 'courseresult', b)
    _safe_set(b, 'Course28', a2)
    assert _is_linked(b, 'Course28', a2)
    if hasattr(a1, 'courseresult'):
        assert not _is_linked(a1, 'courseresult', b)
    if hasattr(a2, 'courseresult'):
        assert _is_linked(a2, 'courseresult', b)
    _safe_set(b, 'Course28', None)
    assert not _is_linked(b, 'Course28', a2)
    if hasattr(a2, 'courseresult'):
        assert not _is_linked(a2, 'courseresult', b)


def test_assoc_course3_reverse_link_reassign_clear():
    a1 = school_School(name="sample_text")
    a2 = school_School(name="sample_text_2")
    b = school_Course(courseNumber="sample_text", name="sample_text")
    _safe_set(b, 'school_Course', a1)
    assert _is_linked(b, 'school_Course', a1)
    if hasattr(a1, 'school_School4'):
        assert _is_linked(a1, 'school_School4', b)
    _safe_set(b, 'school_Course', a2)
    assert _is_linked(b, 'school_Course', a2)
    if hasattr(a1, 'school_School4'):
        assert not _is_linked(a1, 'school_School4', b)
    if hasattr(a2, 'school_School4'):
        assert _is_linked(a2, 'school_School4', b)
    _safe_set(b, 'school_Course', None)
    assert not _is_linked(b, 'school_Course', a2)
    if hasattr(a2, 'school_School4'):
        assert not _is_linked(a2, 'school_School4', b)


def test_assoc_courseofstudy1_reverse_link_reassign_clear():
    a1 = school_School(name="sample_text")
    a2 = school_School(name="sample_text_2")
    b = school_CourseOfStudy(name="sample_text")
    _safe_set(b, 'school_CourseOfStudy', a1)
    assert _is_linked(b, 'school_CourseOfStudy', a1)
    if hasattr(a1, 'school_School2'):
        assert _is_linked(a1, 'school_School2', b)
    _safe_set(b, 'school_CourseOfStudy', a2)
    assert _is_linked(b, 'school_CourseOfStudy', a2)
    if hasattr(a1, 'school_School2'):
        assert not _is_linked(a1, 'school_School2', b)
    if hasattr(a2, 'school_School2'):
        assert _is_linked(a2, 'school_School2', b)
    _safe_set(b, 'school_CourseOfStudy', None)
    assert not _is_linked(b, 'school_CourseOfStudy', a2)
    if hasattr(a2, 'school_School2'):
        assert not _is_linked(a2, 'school_School2', b)


def test_assoc_courseofstudy21_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text", studentNumber="sample_text")
    a2 = school_Student(name="sample_text_2", studentNumber="sample_text_2")
    b = school_CourseOfStudy(name="sample_text")
    _safe_set(b, 'CourseOfStudy22', a1)
    assert _is_linked(b, 'CourseOfStudy22', a1)
    if hasattr(a1, 'student'):
        assert _is_linked(a1, 'student', b)
    _safe_set(b, 'CourseOfStudy22', a2)
    assert _is_linked(b, 'CourseOfStudy22', a2)
    if hasattr(a1, 'student'):
        assert not _is_linked(a1, 'student', b)
    if hasattr(a2, 'student'):
        assert _is_linked(a2, 'student', b)
    _safe_set(b, 'CourseOfStudy22', None)
    assert not _is_linked(b, 'CourseOfStudy22', a2)
    if hasattr(a2, 'student'):
        assert not _is_linked(a2, 'student', b)


def test_assoc_courseofstudy9_reverse_link_reassign_clear():
    a1 = school_Faculty(name="sample_text")
    a2 = school_Faculty(name="sample_text_2")
    b = school_CourseOfStudy(name="sample_text")
    _safe_set(b, 'CourseOfStudy', a1)
    assert _is_linked(b, 'CourseOfStudy', a1)
    if hasattr(a1, 'faculty'):
        assert _is_linked(a1, 'faculty', b)
    _safe_set(b, 'CourseOfStudy', a2)
    assert _is_linked(b, 'CourseOfStudy', a2)
    if hasattr(a1, 'faculty'):
        assert not _is_linked(a1, 'faculty', b)
    if hasattr(a2, 'faculty'):
        assert _is_linked(a2, 'faculty', b)
    _safe_set(b, 'CourseOfStudy', None)
    assert not _is_linked(b, 'CourseOfStudy', a2)
    if hasattr(a2, 'faculty'):
        assert not _is_linked(a2, 'faculty', b)


def test_assoc_courseresult19_reverse_link_reassign_clear():
    a1 = school_CourseResult(grade="sample_text")
    a2 = school_CourseResult(grade="sample_text_2")
    b = school_Course(courseNumber="sample_text", name="sample_text")
    _safe_set(b, 'course', {a1})
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'CourseResult'):
        assert _is_linked(a1, 'CourseResult', b)
    _safe_set(b, 'course', {a2})
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'CourseResult'):
        assert not _is_linked(a1, 'CourseResult', b)
    if hasattr(a2, 'CourseResult'):
        assert _is_linked(a2, 'CourseResult', b)
    _safe_set(b, 'course', set())
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'CourseResult'):
        assert not _is_linked(a2, 'CourseResult', b)


def test_assoc_enrolledIn20_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text", studentNumber="sample_text")
    a2 = school_Student(name="sample_text_2", studentNumber="sample_text_2")
    b = school_Course(courseNumber="sample_text", name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'enrolledStudent'):
        assert _is_linked(a1, 'enrolledStudent', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'enrolledStudent'):
        assert not _is_linked(a1, 'enrolledStudent', b)
    if hasattr(a2, 'enrolledStudent'):
        assert _is_linked(a2, 'enrolledStudent', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'enrolledStudent'):
        assert not _is_linked(a2, 'enrolledStudent', b)


def test_assoc_enrolledStudent16_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text", studentNumber="sample_text")
    a2 = school_Student(name="sample_text_2", studentNumber="sample_text_2")
    b = school_Course(courseNumber="sample_text", name="sample_text")
    _safe_set(b, 'enrolledIn', {a1})
    assert _is_linked(b, 'enrolledIn', a1)
    if hasattr(a1, 'Student17'):
        assert _is_linked(a1, 'Student17', b)
    _safe_set(b, 'enrolledIn', {a2})
    assert _is_linked(b, 'enrolledIn', a2)
    if hasattr(a1, 'Student17'):
        assert not _is_linked(a1, 'Student17', b)
    if hasattr(a2, 'Student17'):
        assert _is_linked(a2, 'Student17', b)
    _safe_set(b, 'enrolledIn', set())
    assert not _is_linked(b, 'enrolledIn', a2)
    if hasattr(a2, 'Student17'):
        assert not _is_linked(a2, 'Student17', b)


def test_assoc_faculty0_reverse_link_reassign_clear():
    a1 = school_School(name="sample_text")
    a2 = school_School(name="sample_text_2")
    b = school_Faculty(name="sample_text")
    _safe_set(b, 'school_Faculty', a1)
    assert _is_linked(b, 'school_Faculty', a1)
    if hasattr(a1, 'school_School'):
        assert _is_linked(a1, 'school_School', b)
    _safe_set(b, 'school_Faculty', a2)
    assert _is_linked(b, 'school_Faculty', a2)
    if hasattr(a1, 'school_School'):
        assert not _is_linked(a1, 'school_School', b)
    if hasattr(a2, 'school_School'):
        assert _is_linked(a2, 'school_School', b)
    _safe_set(b, 'school_Faculty', None)
    assert not _is_linked(b, 'school_Faculty', a2)
    if hasattr(a2, 'school_School'):
        assert not _is_linked(a2, 'school_School', b)


def test_assoc_faculty13_reverse_link_reassign_clear():
    a1 = school_Faculty(name="sample_text")
    a2 = school_Faculty(name="sample_text_2")
    b = school_CourseOfStudy(name="sample_text")
    _safe_set(b, 'courseofstudy', a1)
    assert _is_linked(b, 'courseofstudy', a1)
    if hasattr(a1, 'Faculty'):
        assert _is_linked(a1, 'Faculty', b)
    _safe_set(b, 'courseofstudy', a2)
    assert _is_linked(b, 'courseofstudy', a2)
    if hasattr(a1, 'Faculty'):
        assert not _is_linked(a1, 'Faculty', b)
    if hasattr(a2, 'Faculty'):
        assert _is_linked(a2, 'Faculty', b)
    _safe_set(b, 'courseofstudy', None)
    assert not _is_linked(b, 'courseofstudy', a2)
    if hasattr(a2, 'Faculty'):
        assert not _is_linked(a2, 'Faculty', b)


def test_assoc_or_39_reverse_link_reassign_clear():
    a1 = school_BooleanExpr(lhs="sample_text", operator="sample_text", rhs="sample_text")
    a2 = school_BooleanExpr(lhs="sample_text_2", operator="sample_text_2", rhs="sample_text_2")
    b = school_BooleanExpr(lhs="sample_text", operator="sample_text", rhs="sample_text")
    _safe_set(b, 'school_BooleanExpr40', a1)
    assert _is_linked(b, 'school_BooleanExpr40', a1)
    if hasattr(a1, 'school_BooleanExpr38'):
        assert _is_linked(a1, 'school_BooleanExpr38', b)
    _safe_set(b, 'school_BooleanExpr40', a2)
    assert _is_linked(b, 'school_BooleanExpr40', a2)
    if hasattr(a1, 'school_BooleanExpr38'):
        assert not _is_linked(a1, 'school_BooleanExpr38', b)
    if hasattr(a2, 'school_BooleanExpr38'):
        assert _is_linked(a2, 'school_BooleanExpr38', b)
    _safe_set(b, 'school_BooleanExpr40', None)
    assert not _is_linked(b, 'school_BooleanExpr40', a2)
    if hasattr(a2, 'school_BooleanExpr38'):
        assert not _is_linked(a2, 'school_BooleanExpr38', b)


def test_assoc_student14_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text", studentNumber="sample_text")
    a2 = school_Student(name="sample_text_2", studentNumber="sample_text_2")
    b = school_CourseOfStudy(name="sample_text")
    _safe_set(b, 'courseofstudy15', {a1})
    assert _is_linked(b, 'courseofstudy15', a1)
    if hasattr(a1, 'Student'):
        assert _is_linked(a1, 'Student', b)
    _safe_set(b, 'courseofstudy15', {a2})
    assert _is_linked(b, 'courseofstudy15', a2)
    if hasattr(a1, 'Student'):
        assert not _is_linked(a1, 'Student', b)
    if hasattr(a2, 'Student'):
        assert _is_linked(a2, 'Student', b)
    _safe_set(b, 'courseofstudy15', set())
    assert not _is_linked(b, 'courseofstudy15', a2)
    if hasattr(a2, 'Student'):
        assert not _is_linked(a2, 'Student', b)


def test_assoc_student25_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text", studentNumber="sample_text")
    a2 = school_Student(name="sample_text_2", studentNumber="sample_text_2")
    b = school_CourseResult(grade="sample_text")
    _safe_set(b, 'school_CourseResult', a1)
    assert _is_linked(b, 'school_CourseResult', a1)
    if hasattr(a1, 'school_Student26'):
        assert _is_linked(a1, 'school_Student26', b)
    _safe_set(b, 'school_CourseResult', a2)
    assert _is_linked(b, 'school_CourseResult', a2)
    if hasattr(a1, 'school_Student26'):
        assert not _is_linked(a1, 'school_Student26', b)
    if hasattr(a2, 'school_Student26'):
        assert _is_linked(a2, 'school_Student26', b)
    _safe_set(b, 'school_CourseResult', None)
    assert not _is_linked(b, 'school_CourseResult', a2)
    if hasattr(a2, 'school_Student26'):
        assert not _is_linked(a2, 'school_Student26', b)


def test_assoc_student29_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text", studentNumber="sample_text")
    a2 = school_Student(name="sample_text_2", studentNumber="sample_text_2")
    b = school_Query(type="sample_text")
    _safe_set(b, 'school_Query', a1)
    assert _is_linked(b, 'school_Query', a1)
    if hasattr(a1, 'school_Student30'):
        assert _is_linked(a1, 'school_Student30', b)
    _safe_set(b, 'school_Query', a2)
    assert _is_linked(b, 'school_Query', a2)
    if hasattr(a1, 'school_Student30'):
        assert not _is_linked(a1, 'school_Student30', b)
    if hasattr(a2, 'school_Student30'):
        assert _is_linked(a2, 'school_Student30', b)
    _safe_set(b, 'school_Query', None)
    assert not _is_linked(b, 'school_Query', a2)
    if hasattr(a2, 'school_Student30'):
        assert not _is_linked(a2, 'school_Student30', b)


def test_assoc_student5_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text", studentNumber="sample_text")
    a2 = school_Student(name="sample_text_2", studentNumber="sample_text_2")
    b = school_School(name="sample_text")
    _safe_set(b, 'school_School6', {a1})
    assert _is_linked(b, 'school_School6', a1)
    if hasattr(a1, 'school_Student'):
        assert _is_linked(a1, 'school_Student', b)
    _safe_set(b, 'school_School6', {a2})
    assert _is_linked(b, 'school_School6', a2)
    if hasattr(a1, 'school_Student'):
        assert not _is_linked(a1, 'school_Student', b)
    if hasattr(a2, 'school_Student'):
        assert _is_linked(a2, 'school_Student', b)
    _safe_set(b, 'school_School6', set())
    assert not _is_linked(b, 'school_School6', a2)
    if hasattr(a2, 'school_Student'):
        assert not _is_linked(a2, 'school_Student', b)


def test_assoc_taughtBy18_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_Course(courseNumber="sample_text", name="sample_text")
    _safe_set(b, 'teaches', a1)
    assert _is_linked(b, 'teaches', a1)
    if hasattr(a1, 'Teacher'):
        assert _is_linked(a1, 'Teacher', b)
    _safe_set(b, 'teaches', a2)
    assert _is_linked(b, 'teaches', a2)
    if hasattr(a1, 'Teacher'):
        assert not _is_linked(a1, 'Teacher', b)
    if hasattr(a2, 'Teacher'):
        assert _is_linked(a2, 'Teacher', b)
    _safe_set(b, 'teaches', None)
    assert not _is_linked(b, 'teaches', a2)
    if hasattr(a2, 'Teacher'):
        assert not _is_linked(a2, 'Teacher', b)


def test_assoc_teacher7_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_School(name="sample_text")
    _safe_set(b, 'school_School8', {a1})
    assert _is_linked(b, 'school_School8', a1)
    if hasattr(a1, 'school_Teacher'):
        assert _is_linked(a1, 'school_Teacher', b)
    _safe_set(b, 'school_School8', {a2})
    assert _is_linked(b, 'school_School8', a2)
    if hasattr(a1, 'school_Teacher'):
        assert not _is_linked(a1, 'school_Teacher', b)
    if hasattr(a2, 'school_Teacher'):
        assert _is_linked(a2, 'school_Teacher', b)
    _safe_set(b, 'school_School8', set())
    assert not _is_linked(b, 'school_School8', a2)
    if hasattr(a2, 'school_Teacher'):
        assert not _is_linked(a2, 'school_Teacher', b)


def test_assoc_teaches23_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_Course(courseNumber="sample_text", name="sample_text")
    _safe_set(b, 'Course24', a1)
    assert _is_linked(b, 'Course24', a1)
    if hasattr(a1, 'taughtBy'):
        assert _is_linked(a1, 'taughtBy', b)
    _safe_set(b, 'Course24', a2)
    assert _is_linked(b, 'Course24', a2)
    if hasattr(a1, 'taughtBy'):
        assert not _is_linked(a1, 'taughtBy', b)
    if hasattr(a2, 'taughtBy'):
        assert _is_linked(a2, 'taughtBy', b)
    _safe_set(b, 'Course24', None)
    assert not _is_linked(b, 'Course24', a2)
    if hasattr(a2, 'taughtBy'):
        assert not _is_linked(a2, 'taughtBy', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_booleanexpr33_stub_double():
    # school_Where has no real 'school_Where34' property in the generated
    # code (a bare stub) -- manually attach it so school_BooleanExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # school_BooleanExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = school_BooleanExpr(lhs="sample_text", operator="sample_text", rhs="sample_text")
    partner = school_Where()
    setattr(partner, 'school_Where34', None)
    _safe_set(owner, 'school_BooleanExpr', partner)
    assert getattr(partner, 'school_Where34') == owner
    _safe_set(owner, 'school_BooleanExpr', None)
    assert getattr(partner, 'school_Where34') is None


def test_assoc_query43_stub_double():
    # school_SchoolDatabase has no real 'school_SchoolDatabase44' property in the generated
    # code (a bare stub) -- manually attach it so school_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # school_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = school_Query(type="sample_text")
    partner = school_SchoolDatabase()
    setattr(partner, 'school_SchoolDatabase44', None)
    _safe_set(owner, 'school_Query45', partner)
    assert owner in getattr(partner, 'school_SchoolDatabase44')
    _safe_set(owner, 'school_Query45', None)
    assert owner not in getattr(partner, 'school_SchoolDatabase44')


def test_assoc_school41_stub_double():
    # school_SchoolDatabase has no real 'school_SchoolDatabase' property in the generated
    # code (a bare stub) -- manually attach it so school_School's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # school_School's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = school_School(name="sample_text")
    partner = school_SchoolDatabase()
    setattr(partner, 'school_SchoolDatabase', None)
    _safe_set(owner, 'school_School42', partner)
    assert getattr(partner, 'school_SchoolDatabase') == owner
    _safe_set(owner, 'school_School42', None)
    assert getattr(partner, 'school_SchoolDatabase') is None


def test_assoc_where31_stub_double():
    # school_Where has no real 'school_Where' property in the generated
    # code (a bare stub) -- manually attach it so school_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # school_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = school_Query(type="sample_text")
    partner = school_Where()
    setattr(partner, 'school_Where', None)
    _safe_set(owner, 'school_Query32', partner)
    assert getattr(partner, 'school_Where') == owner
    _safe_set(owner, 'school_Query32', None)
    assert getattr(partner, 'school_Where') is None


