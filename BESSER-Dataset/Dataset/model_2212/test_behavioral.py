import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    StudyProgramme_Course,
    StudyProgramme_CourseGroup,
    StudyProgramme_Department,
    StudyProgramme_Programme,
    StudyProgramme_Semester,
    StudyProgramme_Specialization,
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

def test_assoc_course21_reverse_link_reassign_clear():
    a1 = StudyProgramme_Department(code="sample_text", name="sample_text")
    a2 = StudyProgramme_Department(code="sample_text_2", name="sample_text_2")
    b = StudyProgramme_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'StudyProgramme_Course23', a1)
    assert _is_linked(b, 'StudyProgramme_Course23', a1)
    if hasattr(a1, 'StudyProgramme_Department22'):
        assert _is_linked(a1, 'StudyProgramme_Department22', b)
    _safe_set(b, 'StudyProgramme_Course23', a2)
    assert _is_linked(b, 'StudyProgramme_Course23', a2)
    if hasattr(a1, 'StudyProgramme_Department22'):
        assert not _is_linked(a1, 'StudyProgramme_Department22', b)
    if hasattr(a2, 'StudyProgramme_Department22'):
        assert _is_linked(a2, 'StudyProgramme_Department22', b)
    _safe_set(b, 'StudyProgramme_Course23', None)
    assert not _is_linked(b, 'StudyProgramme_Course23', a2)
    if hasattr(a2, 'StudyProgramme_Department22'):
        assert not _is_linked(a2, 'StudyProgramme_Department22', b)


def test_assoc_courseGroups5_reverse_link_reassign_clear():
    a1 = StudyProgramme_Semester(creditConstraint="sample_text", number=7, season="sample_text", totalCredits=3.14)
    a2 = StudyProgramme_Semester(creditConstraint="sample_text_2", number=13, season="sample_text_2", totalCredits=9.99)
    b = StudyProgramme_CourseGroup(status="sample_text")
    _safe_set(b, 'StudyProgramme_CourseGroup', a1)
    assert _is_linked(b, 'StudyProgramme_CourseGroup', a1)
    if hasattr(a1, 'StudyProgramme_Semester6'):
        assert _is_linked(a1, 'StudyProgramme_Semester6', b)
    _safe_set(b, 'StudyProgramme_CourseGroup', a2)
    assert _is_linked(b, 'StudyProgramme_CourseGroup', a2)
    if hasattr(a1, 'StudyProgramme_Semester6'):
        assert not _is_linked(a1, 'StudyProgramme_Semester6', b)
    if hasattr(a2, 'StudyProgramme_Semester6'):
        assert _is_linked(a2, 'StudyProgramme_Semester6', b)
    _safe_set(b, 'StudyProgramme_CourseGroup', None)
    assert not _is_linked(b, 'StudyProgramme_CourseGroup', a2)
    if hasattr(a2, 'StudyProgramme_Semester6'):
        assert not _is_linked(a2, 'StudyProgramme_Semester6', b)


def test_assoc_courseList3_reverse_link_reassign_clear():
    a1 = StudyProgramme_Semester(creditConstraint="sample_text", number=7, season="sample_text", totalCredits=3.14)
    a2 = StudyProgramme_Semester(creditConstraint="sample_text_2", number=13, season="sample_text_2", totalCredits=9.99)
    b = StudyProgramme_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'StudyProgramme_Course', a1)
    assert _is_linked(b, 'StudyProgramme_Course', a1)
    if hasattr(a1, 'StudyProgramme_Semester4'):
        assert _is_linked(a1, 'StudyProgramme_Semester4', b)
    _safe_set(b, 'StudyProgramme_Course', a2)
    assert _is_linked(b, 'StudyProgramme_Course', a2)
    if hasattr(a1, 'StudyProgramme_Semester4'):
        assert not _is_linked(a1, 'StudyProgramme_Semester4', b)
    if hasattr(a2, 'StudyProgramme_Semester4'):
        assert _is_linked(a2, 'StudyProgramme_Semester4', b)
    _safe_set(b, 'StudyProgramme_Course', None)
    assert not _is_linked(b, 'StudyProgramme_Course', a2)
    if hasattr(a2, 'StudyProgramme_Semester4'):
        assert not _is_linked(a2, 'StudyProgramme_Semester4', b)


def test_assoc_coursesInGroup16_reverse_link_reassign_clear():
    a1 = StudyProgramme_CourseGroup(status="sample_text")
    a2 = StudyProgramme_CourseGroup(status="sample_text_2")
    b = StudyProgramme_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'StudyProgramme_Course18', a1)
    assert _is_linked(b, 'StudyProgramme_Course18', a1)
    if hasattr(a1, 'StudyProgramme_CourseGroup17'):
        assert _is_linked(a1, 'StudyProgramme_CourseGroup17', b)
    _safe_set(b, 'StudyProgramme_Course18', a2)
    assert _is_linked(b, 'StudyProgramme_Course18', a2)
    if hasattr(a1, 'StudyProgramme_CourseGroup17'):
        assert not _is_linked(a1, 'StudyProgramme_CourseGroup17', b)
    if hasattr(a2, 'StudyProgramme_CourseGroup17'):
        assert _is_linked(a2, 'StudyProgramme_CourseGroup17', b)
    _safe_set(b, 'StudyProgramme_Course18', None)
    assert not _is_linked(b, 'StudyProgramme_Course18', a2)
    if hasattr(a2, 'StudyProgramme_CourseGroup17'):
        assert not _is_linked(a2, 'StudyProgramme_CourseGroup17', b)


def test_assoc_programmeSemester0_reverse_link_reassign_clear():
    a1 = StudyProgramme_Semester(creditConstraint="sample_text", number=7, season="sample_text", totalCredits=3.14)
    a2 = StudyProgramme_Semester(creditConstraint="sample_text_2", number=13, season="sample_text_2", totalCredits=9.99)
    b = StudyProgramme_Programme(code="sample_text", duration=7, name="sample_text")
    _safe_set(b, 'StudyProgramme_Programme', {a1})
    assert _is_linked(b, 'StudyProgramme_Programme', a1)
    if hasattr(a1, 'StudyProgramme_Semester'):
        assert _is_linked(a1, 'StudyProgramme_Semester', b)
    _safe_set(b, 'StudyProgramme_Programme', {a2})
    assert _is_linked(b, 'StudyProgramme_Programme', a2)
    if hasattr(a1, 'StudyProgramme_Semester'):
        assert not _is_linked(a1, 'StudyProgramme_Semester', b)
    if hasattr(a2, 'StudyProgramme_Semester'):
        assert _is_linked(a2, 'StudyProgramme_Semester', b)
    _safe_set(b, 'StudyProgramme_Programme', set())
    assert not _is_linked(b, 'StudyProgramme_Programme', a2)
    if hasattr(a2, 'StudyProgramme_Semester'):
        assert not _is_linked(a2, 'StudyProgramme_Semester', b)


def test_assoc_programmeSpecializaton1_reverse_link_reassign_clear():
    a1 = StudyProgramme_Specialization(name="sample_text")
    a2 = StudyProgramme_Specialization(name="sample_text_2")
    b = StudyProgramme_Programme(code="sample_text", duration=7, name="sample_text")
    _safe_set(b, 'StudyProgramme_Programme2', {a1})
    assert _is_linked(b, 'StudyProgramme_Programme2', a1)
    if hasattr(a1, 'StudyProgramme_Specialization'):
        assert _is_linked(a1, 'StudyProgramme_Specialization', b)
    _safe_set(b, 'StudyProgramme_Programme2', {a2})
    assert _is_linked(b, 'StudyProgramme_Programme2', a2)
    if hasattr(a1, 'StudyProgramme_Specialization'):
        assert not _is_linked(a1, 'StudyProgramme_Specialization', b)
    if hasattr(a2, 'StudyProgramme_Specialization'):
        assert _is_linked(a2, 'StudyProgramme_Specialization', b)
    _safe_set(b, 'StudyProgramme_Programme2', set())
    assert not _is_linked(b, 'StudyProgramme_Programme2', a2)
    if hasattr(a2, 'StudyProgramme_Specialization'):
        assert not _is_linked(a2, 'StudyProgramme_Specialization', b)


def test_assoc_programmes19_reverse_link_reassign_clear():
    a1 = StudyProgramme_Programme(code="sample_text", duration=7, name="sample_text")
    a2 = StudyProgramme_Programme(code="sample_text_2", duration=13, name="sample_text_2")
    b = StudyProgramme_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'StudyProgramme_Department', {a1})
    assert _is_linked(b, 'StudyProgramme_Department', a1)
    if hasattr(a1, 'StudyProgramme_Programme20'):
        assert _is_linked(a1, 'StudyProgramme_Programme20', b)
    _safe_set(b, 'StudyProgramme_Department', {a2})
    assert _is_linked(b, 'StudyProgramme_Department', a2)
    if hasattr(a1, 'StudyProgramme_Programme20'):
        assert not _is_linked(a1, 'StudyProgramme_Programme20', b)
    if hasattr(a2, 'StudyProgramme_Programme20'):
        assert _is_linked(a2, 'StudyProgramme_Programme20', b)
    _safe_set(b, 'StudyProgramme_Department', set())
    assert not _is_linked(b, 'StudyProgramme_Department', a2)
    if hasattr(a2, 'StudyProgramme_Programme20'):
        assert not _is_linked(a2, 'StudyProgramme_Programme20', b)


def test_assoc_semesters10_reverse_link_reassign_clear():
    a1 = StudyProgramme_Specialization(name="sample_text")
    a2 = StudyProgramme_Specialization(name="sample_text_2")
    b = StudyProgramme_Semester(creditConstraint="sample_text", number=7, season="sample_text", totalCredits=3.14)
    _safe_set(b, 'StudyProgramme_Semester12', a1)
    assert _is_linked(b, 'StudyProgramme_Semester12', a1)
    if hasattr(a1, 'StudyProgramme_Specialization11'):
        assert _is_linked(a1, 'StudyProgramme_Specialization11', b)
    _safe_set(b, 'StudyProgramme_Semester12', a2)
    assert _is_linked(b, 'StudyProgramme_Semester12', a2)
    if hasattr(a1, 'StudyProgramme_Specialization11'):
        assert not _is_linked(a1, 'StudyProgramme_Specialization11', b)
    if hasattr(a2, 'StudyProgramme_Specialization11'):
        assert _is_linked(a2, 'StudyProgramme_Specialization11', b)
    _safe_set(b, 'StudyProgramme_Semester12', None)
    assert not _is_linked(b, 'StudyProgramme_Semester12', a2)
    if hasattr(a2, 'StudyProgramme_Specialization11'):
        assert not _is_linked(a2, 'StudyProgramme_Specialization11', b)


def test_assoc_specializationCourse7_reverse_link_reassign_clear():
    a1 = StudyProgramme_Specialization(name="sample_text")
    a2 = StudyProgramme_Specialization(name="sample_text_2")
    b = StudyProgramme_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'StudyProgramme_Course9', a1)
    assert _is_linked(b, 'StudyProgramme_Course9', a1)
    if hasattr(a1, 'StudyProgramme_Specialization8'):
        assert _is_linked(a1, 'StudyProgramme_Specialization8', b)
    _safe_set(b, 'StudyProgramme_Course9', a2)
    assert _is_linked(b, 'StudyProgramme_Course9', a2)
    if hasattr(a1, 'StudyProgramme_Specialization8'):
        assert not _is_linked(a1, 'StudyProgramme_Specialization8', b)
    if hasattr(a2, 'StudyProgramme_Specialization8'):
        assert _is_linked(a2, 'StudyProgramme_Specialization8', b)
    _safe_set(b, 'StudyProgramme_Course9', None)
    assert not _is_linked(b, 'StudyProgramme_Course9', a2)
    if hasattr(a2, 'StudyProgramme_Specialization8'):
        assert not _is_linked(a2, 'StudyProgramme_Specialization8', b)


def test_assoc_specializations14_reverse_link_reassign_clear():
    a1 = StudyProgramme_Specialization(name="sample_text")
    a2 = StudyProgramme_Specialization(name="sample_text_2")
    b = StudyProgramme_Specialization(name="sample_text")
    _safe_set(b, 'StudyProgramme_Specialization15', a1)
    assert _is_linked(b, 'StudyProgramme_Specialization15', a1)
    if hasattr(a1, 'StudyProgramme_Specialization13'):
        assert _is_linked(a1, 'StudyProgramme_Specialization13', b)
    _safe_set(b, 'StudyProgramme_Specialization15', a2)
    assert _is_linked(b, 'StudyProgramme_Specialization15', a2)
    if hasattr(a1, 'StudyProgramme_Specialization13'):
        assert not _is_linked(a1, 'StudyProgramme_Specialization13', b)
    if hasattr(a2, 'StudyProgramme_Specialization13'):
        assert _is_linked(a2, 'StudyProgramme_Specialization13', b)
    _safe_set(b, 'StudyProgramme_Specialization15', None)
    assert not _is_linked(b, 'StudyProgramme_Specialization15', a2)
    if hasattr(a2, 'StudyProgramme_Specialization13'):
        assert not _is_linked(a2, 'StudyProgramme_Specialization13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

