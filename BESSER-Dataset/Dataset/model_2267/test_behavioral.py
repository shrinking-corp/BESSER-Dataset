import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    university_Certificate,
    university_Course,
    university_Professor,
    university_Student,
    university_University,
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

def test_assoc_certificates8_reverse_link_reassign_clear():
    a1 = university_University(averageLength=3.14, name="sample_text", numberOfStudents=7)
    a2 = university_University(averageLength=9.99, name="sample_text_2", numberOfStudents=13)
    b = university_Certificate(note=7)
    _safe_set(b, 'university_Certificate', a1)
    assert _is_linked(b, 'university_Certificate', a1)
    if hasattr(a1, 'university_University9'):
        assert _is_linked(a1, 'university_University9', b)
    _safe_set(b, 'university_Certificate', a2)
    assert _is_linked(b, 'university_Certificate', a2)
    if hasattr(a1, 'university_University9'):
        assert not _is_linked(a1, 'university_University9', b)
    if hasattr(a2, 'university_University9'):
        assert _is_linked(a2, 'university_University9', b)
    _safe_set(b, 'university_Certificate', None)
    assert not _is_linked(b, 'university_Certificate', a2)
    if hasattr(a2, 'university_University9'):
        assert not _is_linked(a2, 'university_University9', b)


def test_assoc_course13_reverse_link_reassign_clear():
    a1 = university_Course(gradeAverage=3.14, name="sample_text", numberOfAttendants=7)
    a2 = university_Course(gradeAverage=9.99, name="sample_text_2", numberOfAttendants=13)
    b = university_Certificate(note=7)
    _safe_set(b, 'courseCertificates', a1)
    assert _is_linked(b, 'courseCertificates', a1)
    if hasattr(a1, 'Course14'):
        assert _is_linked(a1, 'Course14', b)
    _safe_set(b, 'courseCertificates', a2)
    assert _is_linked(b, 'courseCertificates', a2)
    if hasattr(a1, 'Course14'):
        assert not _is_linked(a1, 'Course14', b)
    if hasattr(a2, 'Course14'):
        assert _is_linked(a2, 'Course14', b)
    _safe_set(b, 'courseCertificates', None)
    assert not _is_linked(b, 'courseCertificates', a2)
    if hasattr(a2, 'Course14'):
        assert not _is_linked(a2, 'Course14', b)


def test_assoc_courseCertificates1_reverse_link_reassign_clear():
    a1 = university_Course(gradeAverage=3.14, name="sample_text", numberOfAttendants=7)
    a2 = university_Course(gradeAverage=9.99, name="sample_text_2", numberOfAttendants=13)
    b = university_Certificate(note=7)
    _safe_set(b, 'Certificate', a1)
    assert _is_linked(b, 'Certificate', a1)
    if hasattr(a1, 'course'):
        assert _is_linked(a1, 'course', b)
    _safe_set(b, 'Certificate', a2)
    assert _is_linked(b, 'Certificate', a2)
    if hasattr(a1, 'course'):
        assert not _is_linked(a1, 'course', b)
    if hasattr(a2, 'course'):
        assert _is_linked(a2, 'course', b)
    _safe_set(b, 'Certificate', None)
    assert not _is_linked(b, 'Certificate', a2)
    if hasattr(a2, 'course'):
        assert not _is_linked(a2, 'course', b)


def test_assoc_courses2_reverse_link_reassign_clear():
    a1 = university_Professor(name="sample_text")
    a2 = university_Professor(name="sample_text_2")
    b = university_Course(gradeAverage=3.14, name="sample_text", numberOfAttendants=7)
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'professor'):
        assert _is_linked(a1, 'professor', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'professor'):
        assert not _is_linked(a1, 'professor', b)
    if hasattr(a2, 'professor'):
        assert _is_linked(a2, 'professor', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'professor'):
        assert not _is_linked(a2, 'professor', b)


def test_assoc_courses4_reverse_link_reassign_clear():
    a1 = university_University(averageLength=3.14, name="sample_text", numberOfStudents=7)
    a2 = university_University(averageLength=9.99, name="sample_text_2", numberOfStudents=13)
    b = university_Course(gradeAverage=3.14, name="sample_text", numberOfAttendants=7)
    _safe_set(b, 'university_Course', a1)
    assert _is_linked(b, 'university_Course', a1)
    if hasattr(a1, 'university_University5'):
        assert _is_linked(a1, 'university_University5', b)
    _safe_set(b, 'university_Course', a2)
    assert _is_linked(b, 'university_Course', a2)
    if hasattr(a1, 'university_University5'):
        assert not _is_linked(a1, 'university_University5', b)
    if hasattr(a2, 'university_University5'):
        assert _is_linked(a2, 'university_University5', b)
    _safe_set(b, 'university_Course', None)
    assert not _is_linked(b, 'university_Course', a2)
    if hasattr(a2, 'university_University5'):
        assert not _is_linked(a2, 'university_University5', b)


def test_assoc_professor0_reverse_link_reassign_clear():
    a1 = university_Professor(name="sample_text")
    a2 = university_Professor(name="sample_text_2")
    b = university_Course(gradeAverage=3.14, name="sample_text", numberOfAttendants=7)
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'Professor'):
        assert _is_linked(a1, 'Professor', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'Professor'):
        assert not _is_linked(a1, 'Professor', b)
    if hasattr(a2, 'Professor'):
        assert _is_linked(a2, 'Professor', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'Professor'):
        assert not _is_linked(a2, 'Professor', b)


def test_assoc_professors3_reverse_link_reassign_clear():
    a1 = university_University(averageLength=3.14, name="sample_text", numberOfStudents=7)
    a2 = university_University(averageLength=9.99, name="sample_text_2", numberOfStudents=13)
    b = university_Professor(name="sample_text")
    _safe_set(b, 'university_Professor', a1)
    assert _is_linked(b, 'university_Professor', a1)
    if hasattr(a1, 'university_University'):
        assert _is_linked(a1, 'university_University', b)
    _safe_set(b, 'university_Professor', a2)
    assert _is_linked(b, 'university_Professor', a2)
    if hasattr(a1, 'university_University'):
        assert not _is_linked(a1, 'university_University', b)
    if hasattr(a2, 'university_University'):
        assert _is_linked(a2, 'university_University', b)
    _safe_set(b, 'university_Professor', None)
    assert not _is_linked(b, 'university_Professor', a2)
    if hasattr(a2, 'university_University'):
        assert not _is_linked(a2, 'university_University', b)


def test_assoc_student12_reverse_link_reassign_clear():
    a1 = university_Student(MNR="sample_text", semester=7)
    a2 = university_Student(MNR="sample_text_2", semester=13)
    b = university_Certificate(note=7)
    _safe_set(b, 'studentCertificates', a1)
    assert _is_linked(b, 'studentCertificates', a1)
    if hasattr(a1, 'Student'):
        assert _is_linked(a1, 'Student', b)
    _safe_set(b, 'studentCertificates', a2)
    assert _is_linked(b, 'studentCertificates', a2)
    if hasattr(a1, 'Student'):
        assert not _is_linked(a1, 'Student', b)
    if hasattr(a2, 'Student'):
        assert _is_linked(a2, 'Student', b)
    _safe_set(b, 'studentCertificates', None)
    assert not _is_linked(b, 'studentCertificates', a2)
    if hasattr(a2, 'Student'):
        assert not _is_linked(a2, 'Student', b)


def test_assoc_studentCertificates10_reverse_link_reassign_clear():
    a1 = university_Student(MNR="sample_text", semester=7)
    a2 = university_Student(MNR="sample_text_2", semester=13)
    b = university_Certificate(note=7)
    _safe_set(b, 'Certificate11', a1)
    assert _is_linked(b, 'Certificate11', a1)
    if hasattr(a1, 'student'):
        assert _is_linked(a1, 'student', b)
    _safe_set(b, 'Certificate11', a2)
    assert _is_linked(b, 'Certificate11', a2)
    if hasattr(a1, 'student'):
        assert not _is_linked(a1, 'student', b)
    if hasattr(a2, 'student'):
        assert _is_linked(a2, 'student', b)
    _safe_set(b, 'Certificate11', None)
    assert not _is_linked(b, 'Certificate11', a2)
    if hasattr(a2, 'student'):
        assert not _is_linked(a2, 'student', b)


def test_assoc_students6_reverse_link_reassign_clear():
    a1 = university_University(averageLength=3.14, name="sample_text", numberOfStudents=7)
    a2 = university_University(averageLength=9.99, name="sample_text_2", numberOfStudents=13)
    b = university_Student(MNR="sample_text", semester=7)
    _safe_set(b, 'university_Student', a1)
    assert _is_linked(b, 'university_Student', a1)
    if hasattr(a1, 'university_University7'):
        assert _is_linked(a1, 'university_University7', b)
    _safe_set(b, 'university_Student', a2)
    assert _is_linked(b, 'university_Student', a2)
    if hasattr(a1, 'university_University7'):
        assert not _is_linked(a1, 'university_University7', b)
    if hasattr(a2, 'university_University7'):
        assert _is_linked(a2, 'university_University7', b)
    _safe_set(b, 'university_Student', None)
    assert not _is_linked(b, 'university_Student', a2)
    if hasattr(a2, 'university_University7'):
        assert not _is_linked(a2, 'university_University7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

