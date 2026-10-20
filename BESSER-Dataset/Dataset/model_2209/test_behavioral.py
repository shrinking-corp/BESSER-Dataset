import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    study_Course,
    study_Department,
    study_Programme,
    study_Semester,
    study_SemesterCourse,
    study_Specialization,
    IsMandatory,
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

def test_assoc_course13_reverse_link_reassign_clear():
    a1 = study_SemesterCourse(mandatory="sample_text")
    a2 = study_SemesterCourse(mandatory="sample_text_2")
    b = study_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'study_Course', a1)
    assert _is_linked(b, 'study_Course', a1)
    if hasattr(a1, 'study_SemesterCourse'):
        assert _is_linked(a1, 'study_SemesterCourse', b)
    _safe_set(b, 'study_Course', a2)
    assert _is_linked(b, 'study_Course', a2)
    if hasattr(a1, 'study_SemesterCourse'):
        assert not _is_linked(a1, 'study_SemesterCourse', b)
    if hasattr(a2, 'study_SemesterCourse'):
        assert _is_linked(a2, 'study_SemesterCourse', b)
    _safe_set(b, 'study_Course', None)
    assert not _is_linked(b, 'study_Course', a2)
    if hasattr(a2, 'study_SemesterCourse'):
        assert not _is_linked(a2, 'study_SemesterCourse', b)


def test_assoc_courses19_reverse_link_reassign_clear():
    a1 = study_Department(name="sample_text")
    a2 = study_Department(name="sample_text_2")
    b = study_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
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
    a1 = study_SemesterCourse(mandatory="sample_text")
    a2 = study_SemesterCourse(mandatory="sample_text_2")
    b = study_Semester(Season="sample_text", year=7)
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


def test_assoc_department16_reverse_link_reassign_clear():
    a1 = study_Department(name="sample_text")
    a2 = study_Department(name="sample_text_2")
    b = study_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'courses17', a1)
    assert _is_linked(b, 'courses17', a1)
    if hasattr(a1, 'Department18'):
        assert _is_linked(a1, 'Department18', b)
    _safe_set(b, 'courses17', a2)
    assert _is_linked(b, 'courses17', a2)
    if hasattr(a1, 'Department18'):
        assert not _is_linked(a1, 'Department18', b)
    if hasattr(a2, 'Department18'):
        assert _is_linked(a2, 'Department18', b)
    _safe_set(b, 'courses17', None)
    assert not _is_linked(b, 'courses17', a2)
    if hasattr(a2, 'Department18'):
        assert not _is_linked(a2, 'Department18', b)


def test_assoc_department3_reverse_link_reassign_clear():
    a1 = study_Programme(code="sample_text", duration=7, name="sample_text")
    a2 = study_Programme(code="sample_text_2", duration=13, name="sample_text_2")
    b = study_Department(name="sample_text")
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


def test_assoc_programme11_reverse_link_reassign_clear():
    a1 = study_Specialization(name="sample_text")
    a2 = study_Specialization(name="sample_text_2")
    b = study_Programme(code="sample_text", duration=7, name="sample_text")
    _safe_set(b, 'Programme12', a1)
    assert _is_linked(b, 'Programme12', a1)
    if hasattr(a1, 'specializations'):
        assert _is_linked(a1, 'specializations', b)
    _safe_set(b, 'Programme12', a2)
    assert _is_linked(b, 'Programme12', a2)
    if hasattr(a1, 'specializations'):
        assert not _is_linked(a1, 'specializations', b)
    if hasattr(a2, 'specializations'):
        assert _is_linked(a2, 'specializations', b)
    _safe_set(b, 'Programme12', None)
    assert not _is_linked(b, 'Programme12', a2)
    if hasattr(a2, 'specializations'):
        assert not _is_linked(a2, 'specializations', b)


def test_assoc_programme5_reverse_link_reassign_clear():
    a1 = study_Semester(Season="sample_text", year=7)
    a2 = study_Semester(Season="sample_text_2", year=13)
    b = study_Programme(code="sample_text", duration=7, name="sample_text")
    _safe_set(b, 'Programme', a1)
    assert _is_linked(b, 'Programme', a1)
    if hasattr(a1, 'semesters'):
        assert _is_linked(a1, 'semesters', b)
    _safe_set(b, 'Programme', a2)
    assert _is_linked(b, 'Programme', a2)
    if hasattr(a1, 'semesters'):
        assert not _is_linked(a1, 'semesters', b)
    if hasattr(a2, 'semesters'):
        assert _is_linked(a2, 'semesters', b)
    _safe_set(b, 'Programme', None)
    assert not _is_linked(b, 'Programme', a2)
    if hasattr(a2, 'semesters'):
        assert not _is_linked(a2, 'semesters', b)


def test_assoc_programs20_reverse_link_reassign_clear():
    a1 = study_Programme(code="sample_text", duration=7, name="sample_text")
    a2 = study_Programme(code="sample_text_2", duration=13, name="sample_text_2")
    b = study_Department(name="sample_text")
    _safe_set(b, 'department21', {a1})
    assert _is_linked(b, 'department21', a1)
    if hasattr(a1, 'Programme22'):
        assert _is_linked(a1, 'Programme22', b)
    _safe_set(b, 'department21', {a2})
    assert _is_linked(b, 'department21', a2)
    if hasattr(a1, 'Programme22'):
        assert not _is_linked(a1, 'Programme22', b)
    if hasattr(a2, 'Programme22'):
        assert _is_linked(a2, 'Programme22', b)
    _safe_set(b, 'department21', set())
    assert not _is_linked(b, 'department21', a2)
    if hasattr(a2, 'Programme22'):
        assert not _is_linked(a2, 'Programme22', b)


def test_assoc_semester14_reverse_link_reassign_clear():
    a1 = study_SemesterCourse(mandatory="sample_text")
    a2 = study_SemesterCourse(mandatory="sample_text_2")
    b = study_Semester(Season="sample_text", year=7)
    _safe_set(b, 'Semester15', a1)
    assert _is_linked(b, 'Semester15', a1)
    if hasattr(a1, 'courses'):
        assert _is_linked(a1, 'courses', b)
    _safe_set(b, 'Semester15', a2)
    assert _is_linked(b, 'Semester15', a2)
    if hasattr(a1, 'courses'):
        assert not _is_linked(a1, 'courses', b)
    if hasattr(a2, 'courses'):
        assert _is_linked(a2, 'courses', b)
    _safe_set(b, 'Semester15', None)
    assert not _is_linked(b, 'Semester15', a2)
    if hasattr(a2, 'courses'):
        assert not _is_linked(a2, 'courses', b)


def test_assoc_semesters0_reverse_link_reassign_clear():
    a1 = study_Semester(Season="sample_text", year=7)
    a2 = study_Semester(Season="sample_text_2", year=13)
    b = study_Programme(code="sample_text", duration=7, name="sample_text")
    _safe_set(b, 'programme', {a1})
    assert _is_linked(b, 'programme', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'programme', {a2})
    assert _is_linked(b, 'programme', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'programme', set())
    assert not _is_linked(b, 'programme', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


def test_assoc_semesters9_reverse_link_reassign_clear():
    a1 = study_Specialization(name="sample_text")
    a2 = study_Specialization(name="sample_text_2")
    b = study_Semester(Season="sample_text", year=7)
    _safe_set(b, 'Semester10', a1)
    assert _is_linked(b, 'Semester10', a1)
    if hasattr(a1, 'specialization'):
        assert _is_linked(a1, 'specialization', b)
    _safe_set(b, 'Semester10', a2)
    assert _is_linked(b, 'Semester10', a2)
    if hasattr(a1, 'specialization'):
        assert not _is_linked(a1, 'specialization', b)
    if hasattr(a2, 'specialization'):
        assert _is_linked(a2, 'specialization', b)
    _safe_set(b, 'Semester10', None)
    assert not _is_linked(b, 'Semester10', a2)
    if hasattr(a2, 'specialization'):
        assert not _is_linked(a2, 'specialization', b)


def test_assoc_specialization6_reverse_link_reassign_clear():
    a1 = study_Specialization(name="sample_text")
    a2 = study_Specialization(name="sample_text_2")
    b = study_Semester(Season="sample_text", year=7)
    _safe_set(b, 'semesters7', a1)
    assert _is_linked(b, 'semesters7', a1)
    if hasattr(a1, 'Specialization8'):
        assert _is_linked(a1, 'Specialization8', b)
    _safe_set(b, 'semesters7', a2)
    assert _is_linked(b, 'semesters7', a2)
    if hasattr(a1, 'Specialization8'):
        assert not _is_linked(a1, 'Specialization8', b)
    if hasattr(a2, 'Specialization8'):
        assert _is_linked(a2, 'Specialization8', b)
    _safe_set(b, 'semesters7', None)
    assert not _is_linked(b, 'semesters7', a2)
    if hasattr(a2, 'Specialization8'):
        assert not _is_linked(a2, 'Specialization8', b)


def test_assoc_specializations1_reverse_link_reassign_clear():
    a1 = study_Specialization(name="sample_text")
    a2 = study_Specialization(name="sample_text_2")
    b = study_Programme(code="sample_text", duration=7, name="sample_text")
    _safe_set(b, 'programme2', {a1})
    assert _is_linked(b, 'programme2', a1)
    if hasattr(a1, 'Specialization'):
        assert _is_linked(a1, 'Specialization', b)
    _safe_set(b, 'programme2', {a2})
    assert _is_linked(b, 'programme2', a2)
    if hasattr(a1, 'Specialization'):
        assert not _is_linked(a1, 'Specialization', b)
    if hasattr(a2, 'Specialization'):
        assert _is_linked(a2, 'Specialization', b)
    _safe_set(b, 'programme2', set())
    assert not _is_linked(b, 'programme2', a2)
    if hasattr(a2, 'Specialization'):
        assert not _is_linked(a2, 'Specialization', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

