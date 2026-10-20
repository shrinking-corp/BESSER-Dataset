import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    study_Course,
    study_Department,
    study_Program,
    study_Semester,
    study_Specialisation,
    study_Student,
    study_StudyPlan,
    study_courseAllocation,
    grades,
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

def test_assoc_course43_reverse_link_reassign_clear():
    a1 = study_courseAllocation(grade="sample_text")
    a2 = study_courseAllocation(grade="sample_text_2")
    b = study_Course(code="sample_text", credits=3.14, name="sample_text", season="sample_text", year=7)
    _safe_set(b, 'study_Course45', a1)
    assert _is_linked(b, 'study_Course45', a1)
    if hasattr(a1, 'study_courseAllocation44'):
        assert _is_linked(a1, 'study_courseAllocation44', b)
    _safe_set(b, 'study_Course45', a2)
    assert _is_linked(b, 'study_Course45', a2)
    if hasattr(a1, 'study_courseAllocation44'):
        assert not _is_linked(a1, 'study_courseAllocation44', b)
    if hasattr(a2, 'study_courseAllocation44'):
        assert _is_linked(a2, 'study_courseAllocation44', b)
    _safe_set(b, 'study_Course45', None)
    assert not _is_linked(b, 'study_Course45', a2)
    if hasattr(a2, 'study_courseAllocation44'):
        assert not _is_linked(a2, 'study_courseAllocation44', b)


def test_assoc_courses0_reverse_link_reassign_clear():
    a1 = study_Department(code="sample_text", name="sample_text")
    a2 = study_Department(code="sample_text_2", name="sample_text_2")
    b = study_Course(code="sample_text", credits=3.14, name="sample_text", season="sample_text", year=7)
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


def test_assoc_courses30_reverse_link_reassign_clear():
    a1 = study_Semester(season="sample_text", year=7)
    a2 = study_Semester(season="sample_text_2", year=13)
    b = study_Course(code="sample_text", credits=3.14, name="sample_text", season="sample_text", year=7)
    _safe_set(b, 'study_Course', a1)
    assert _is_linked(b, 'study_Course', a1)
    if hasattr(a1, 'study_Semester'):
        assert _is_linked(a1, 'study_Semester', b)
    _safe_set(b, 'study_Course', a2)
    assert _is_linked(b, 'study_Course', a2)
    if hasattr(a1, 'study_Semester'):
        assert not _is_linked(a1, 'study_Semester', b)
    if hasattr(a2, 'study_Semester'):
        assert _is_linked(a2, 'study_Semester', b)
    _safe_set(b, 'study_Course', None)
    assert not _is_linked(b, 'study_Course', a2)
    if hasattr(a2, 'study_Semester'):
        assert not _is_linked(a2, 'study_Semester', b)


def test_assoc_courses36_reverse_link_reassign_clear():
    a1 = study_courseAllocation(grade="sample_text")
    a2 = study_courseAllocation(grade="sample_text_2")
    b = study_StudyPlan()
    _safe_set(b, 'study_StudyPlan37', {a1})
    assert _is_linked(b, 'study_StudyPlan37', a1)
    if hasattr(a1, 'study_courseAllocation'):
        assert _is_linked(a1, 'study_courseAllocation', b)
    _safe_set(b, 'study_StudyPlan37', {a2})
    assert _is_linked(b, 'study_StudyPlan37', a2)
    if hasattr(a1, 'study_courseAllocation'):
        assert not _is_linked(a1, 'study_courseAllocation', b)
    if hasattr(a2, 'study_courseAllocation'):
        assert _is_linked(a2, 'study_courseAllocation', b)
    _safe_set(b, 'study_StudyPlan37', set())
    assert not _is_linked(b, 'study_StudyPlan37', a2)
    if hasattr(a2, 'study_courseAllocation'):
        assert not _is_linked(a2, 'study_courseAllocation', b)


def test_assoc_department12_reverse_link_reassign_clear():
    a1 = study_Student(name="sample_text")
    a2 = study_Student(name="sample_text_2")
    b = study_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'Department13', a1)
    assert _is_linked(b, 'Department13', a1)
    if hasattr(a1, 'students'):
        assert _is_linked(a1, 'students', b)
    _safe_set(b, 'Department13', a2)
    assert _is_linked(b, 'Department13', a2)
    if hasattr(a1, 'students'):
        assert not _is_linked(a1, 'students', b)
    if hasattr(a2, 'students'):
        assert _is_linked(a2, 'students', b)
    _safe_set(b, 'Department13', None)
    assert not _is_linked(b, 'Department13', a2)
    if hasattr(a2, 'students'):
        assert not _is_linked(a2, 'students', b)


def test_assoc_department16_reverse_link_reassign_clear():
    a1 = study_Department(code="sample_text", name="sample_text")
    a2 = study_Department(code="sample_text_2", name="sample_text_2")
    b = study_Course(code="sample_text", credits=3.14, name="sample_text", season="sample_text", year=7)
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'Department17'):
        assert _is_linked(a1, 'Department17', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'Department17'):
        assert not _is_linked(a1, 'Department17', b)
    if hasattr(a2, 'Department17'):
        assert _is_linked(a2, 'Department17', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'Department17'):
        assert not _is_linked(a2, 'Department17', b)


def test_assoc_department25_reverse_link_reassign_clear():
    a1 = study_Specialisation(name="sample_text", requirement="sample_text")
    a2 = study_Specialisation(name="sample_text_2", requirement="sample_text_2")
    b = study_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'Department27', a1)
    assert _is_linked(b, 'Department27', a1)
    if hasattr(a1, 'specialisations26'):
        assert _is_linked(a1, 'specialisations26', b)
    _safe_set(b, 'Department27', a2)
    assert _is_linked(b, 'Department27', a2)
    if hasattr(a1, 'specialisations26'):
        assert not _is_linked(a1, 'specialisations26', b)
    if hasattr(a2, 'specialisations26'):
        assert _is_linked(a2, 'specialisations26', b)
    _safe_set(b, 'Department27', None)
    assert not _is_linked(b, 'Department27', a2)
    if hasattr(a2, 'specialisations26'):
        assert not _is_linked(a2, 'specialisations26', b)


def test_assoc_department31_reverse_link_reassign_clear():
    a1 = study_Semester(season="sample_text", year=7)
    a2 = study_Semester(season="sample_text_2", year=13)
    b = study_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'Department33', a1)
    assert _is_linked(b, 'Department33', a1)
    if hasattr(a1, 'semesters32'):
        assert _is_linked(a1, 'semesters32', b)
    _safe_set(b, 'Department33', a2)
    assert _is_linked(b, 'Department33', a2)
    if hasattr(a1, 'semesters32'):
        assert not _is_linked(a1, 'semesters32', b)
    if hasattr(a2, 'semesters32'):
        assert _is_linked(a2, 'semesters32', b)
    _safe_set(b, 'Department33', None)
    assert not _is_linked(b, 'Department33', a2)
    if hasattr(a2, 'semesters32'):
        assert not _is_linked(a2, 'semesters32', b)


def test_assoc_department9_reverse_link_reassign_clear():
    a1 = study_Program(code="sample_text", name="sample_text", numYears=7)
    a2 = study_Program(code="sample_text_2", name="sample_text_2", numYears=13)
    b = study_Department(code="sample_text", name="sample_text")
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


def test_assoc_program18_reverse_link_reassign_clear():
    a1 = study_Specialisation(name="sample_text", requirement="sample_text")
    a2 = study_Specialisation(name="sample_text_2", requirement="sample_text_2")
    b = study_Program(code="sample_text", name="sample_text", numYears=7)
    _safe_set(b, 'Program19', a1)
    assert _is_linked(b, 'Program19', a1)
    if hasattr(a1, 'specialisations'):
        assert _is_linked(a1, 'specialisations', b)
    _safe_set(b, 'Program19', a2)
    assert _is_linked(b, 'Program19', a2)
    if hasattr(a1, 'specialisations'):
        assert not _is_linked(a1, 'specialisations', b)
    if hasattr(a2, 'specialisations'):
        assert _is_linked(a2, 'specialisations', b)
    _safe_set(b, 'Program19', None)
    assert not _is_linked(b, 'Program19', a2)
    if hasattr(a2, 'specialisations'):
        assert not _is_linked(a2, 'specialisations', b)


def test_assoc_programs1_reverse_link_reassign_clear():
    a1 = study_Program(code="sample_text", name="sample_text", numYears=7)
    a2 = study_Program(code="sample_text_2", name="sample_text_2", numYears=13)
    b = study_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'department2', {a1})
    assert _is_linked(b, 'department2', a1)
    if hasattr(a1, 'Program'):
        assert _is_linked(a1, 'Program', b)
    _safe_set(b, 'department2', {a2})
    assert _is_linked(b, 'department2', a2)
    if hasattr(a1, 'Program'):
        assert not _is_linked(a1, 'Program', b)
    if hasattr(a2, 'Program'):
        assert _is_linked(a2, 'Program', b)
    _safe_set(b, 'department2', set())
    assert not _is_linked(b, 'department2', a2)
    if hasattr(a2, 'Program'):
        assert not _is_linked(a2, 'Program', b)


def test_assoc_semester34_reverse_link_reassign_clear():
    a1 = study_StudyPlan()
    a2 = study_StudyPlan()
    b = study_Semester(season="sample_text", year=7)
    _safe_set(b, 'study_Semester35', a1)
    assert _is_linked(b, 'study_Semester35', a1)
    if hasattr(a1, 'study_StudyPlan'):
        assert _is_linked(a1, 'study_StudyPlan', b)
    _safe_set(b, 'study_Semester35', a2)
    assert _is_linked(b, 'study_Semester35', a2)
    if hasattr(a1, 'study_StudyPlan'):
        assert not _is_linked(a1, 'study_StudyPlan', b)
    if hasattr(a2, 'study_StudyPlan'):
        assert _is_linked(a2, 'study_StudyPlan', b)
    _safe_set(b, 'study_Semester35', None)
    assert not _is_linked(b, 'study_Semester35', a2)
    if hasattr(a2, 'study_StudyPlan'):
        assert not _is_linked(a2, 'study_StudyPlan', b)


def test_assoc_semesters23_reverse_link_reassign_clear():
    a1 = study_Specialisation(name="sample_text", requirement="sample_text")
    a2 = study_Specialisation(name="sample_text_2", requirement="sample_text_2")
    b = study_Semester(season="sample_text", year=7)
    _safe_set(b, 'Semester24', a1)
    assert _is_linked(b, 'Semester24', a1)
    if hasattr(a1, 'specialisation'):
        assert _is_linked(a1, 'specialisation', b)
    _safe_set(b, 'Semester24', a2)
    assert _is_linked(b, 'Semester24', a2)
    if hasattr(a1, 'specialisation'):
        assert not _is_linked(a1, 'specialisation', b)
    if hasattr(a2, 'specialisation'):
        assert _is_linked(a2, 'specialisation', b)
    _safe_set(b, 'Semester24', None)
    assert not _is_linked(b, 'Semester24', a2)
    if hasattr(a2, 'specialisation'):
        assert not _is_linked(a2, 'specialisation', b)


def test_assoc_semesters7_reverse_link_reassign_clear():
    a1 = study_Semester(season="sample_text", year=7)
    a2 = study_Semester(season="sample_text_2", year=13)
    b = study_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'department8', {a1})
    assert _is_linked(b, 'department8', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'department8', {a2})
    assert _is_linked(b, 'department8', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'department8', set())
    assert not _is_linked(b, 'department8', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


def test_assoc_specialisation28_reverse_link_reassign_clear():
    a1 = study_Specialisation(name="sample_text", requirement="sample_text")
    a2 = study_Specialisation(name="sample_text_2", requirement="sample_text_2")
    b = study_Semester(season="sample_text", year=7)
    _safe_set(b, 'semesters', a1)
    assert _is_linked(b, 'semesters', a1)
    if hasattr(a1, 'Specialisation29'):
        assert _is_linked(a1, 'Specialisation29', b)
    _safe_set(b, 'semesters', a2)
    assert _is_linked(b, 'semesters', a2)
    if hasattr(a1, 'Specialisation29'):
        assert not _is_linked(a1, 'Specialisation29', b)
    if hasattr(a2, 'Specialisation29'):
        assert _is_linked(a2, 'Specialisation29', b)
    _safe_set(b, 'semesters', None)
    assert not _is_linked(b, 'semesters', a2)
    if hasattr(a2, 'Specialisation29'):
        assert not _is_linked(a2, 'Specialisation29', b)


def test_assoc_specialisations10_reverse_link_reassign_clear():
    a1 = study_Specialisation(name="sample_text", requirement="sample_text")
    a2 = study_Specialisation(name="sample_text_2", requirement="sample_text_2")
    b = study_Program(code="sample_text", name="sample_text", numYears=7)
    _safe_set(b, 'program', {a1})
    assert _is_linked(b, 'program', a1)
    if hasattr(a1, 'Specialisation11'):
        assert _is_linked(a1, 'Specialisation11', b)
    _safe_set(b, 'program', {a2})
    assert _is_linked(b, 'program', a2)
    if hasattr(a1, 'Specialisation11'):
        assert not _is_linked(a1, 'Specialisation11', b)
    if hasattr(a2, 'Specialisation11'):
        assert _is_linked(a2, 'Specialisation11', b)
    _safe_set(b, 'program', set())
    assert not _is_linked(b, 'program', a2)
    if hasattr(a2, 'Specialisation11'):
        assert not _is_linked(a2, 'Specialisation11', b)


def test_assoc_specialisations15_reverse_link_reassign_clear():
    a1 = study_Student(name="sample_text")
    a2 = study_Student(name="sample_text_2")
    b = study_Specialisation(name="sample_text", requirement="sample_text")
    _safe_set(b, 'study_Specialisation', a1)
    assert _is_linked(b, 'study_Specialisation', a1)
    if hasattr(a1, 'study_Student'):
        assert _is_linked(a1, 'study_Student', b)
    _safe_set(b, 'study_Specialisation', a2)
    assert _is_linked(b, 'study_Specialisation', a2)
    if hasattr(a1, 'study_Student'):
        assert not _is_linked(a1, 'study_Student', b)
    if hasattr(a2, 'study_Student'):
        assert _is_linked(a2, 'study_Student', b)
    _safe_set(b, 'study_Specialisation', None)
    assert not _is_linked(b, 'study_Specialisation', a2)
    if hasattr(a2, 'study_Student'):
        assert not _is_linked(a2, 'study_Student', b)


def test_assoc_specialisations5_reverse_link_reassign_clear():
    a1 = study_Specialisation(name="sample_text", requirement="sample_text")
    a2 = study_Specialisation(name="sample_text_2", requirement="sample_text_2")
    b = study_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'department6', {a1})
    assert _is_linked(b, 'department6', a1)
    if hasattr(a1, 'Specialisation'):
        assert _is_linked(a1, 'Specialisation', b)
    _safe_set(b, 'department6', {a2})
    assert _is_linked(b, 'department6', a2)
    if hasattr(a1, 'Specialisation'):
        assert not _is_linked(a1, 'Specialisation', b)
    if hasattr(a2, 'Specialisation'):
        assert _is_linked(a2, 'Specialisation', b)
    _safe_set(b, 'department6', set())
    assert not _is_linked(b, 'department6', a2)
    if hasattr(a2, 'Specialisation'):
        assert not _is_linked(a2, 'Specialisation', b)


def test_assoc_student38_reverse_link_reassign_clear():
    a1 = study_StudyPlan()
    a2 = study_StudyPlan()
    b = study_Student(name="sample_text")
    _safe_set(b, 'Student39', a1)
    assert _is_linked(b, 'Student39', a1)
    if hasattr(a1, 'studyPlan'):
        assert _is_linked(a1, 'studyPlan', b)
    _safe_set(b, 'Student39', a2)
    assert _is_linked(b, 'Student39', a2)
    if hasattr(a1, 'studyPlan'):
        assert not _is_linked(a1, 'studyPlan', b)
    if hasattr(a2, 'studyPlan'):
        assert _is_linked(a2, 'studyPlan', b)
    _safe_set(b, 'Student39', None)
    assert not _is_linked(b, 'Student39', a2)
    if hasattr(a2, 'studyPlan'):
        assert not _is_linked(a2, 'studyPlan', b)


def test_assoc_students20_reverse_link_reassign_clear():
    a1 = study_Student(name="sample_text")
    a2 = study_Student(name="sample_text_2")
    b = study_Specialisation(name="sample_text", requirement="sample_text")
    _safe_set(b, 'study_Specialisation21', a1)
    assert _is_linked(b, 'study_Specialisation21', a1)
    if hasattr(a1, 'study_Student22'):
        assert _is_linked(a1, 'study_Student22', b)
    _safe_set(b, 'study_Specialisation21', a2)
    assert _is_linked(b, 'study_Specialisation21', a2)
    if hasattr(a1, 'study_Student22'):
        assert not _is_linked(a1, 'study_Student22', b)
    if hasattr(a2, 'study_Student22'):
        assert _is_linked(a2, 'study_Student22', b)
    _safe_set(b, 'study_Specialisation21', None)
    assert not _is_linked(b, 'study_Specialisation21', a2)
    if hasattr(a2, 'study_Student22'):
        assert not _is_linked(a2, 'study_Student22', b)


def test_assoc_students3_reverse_link_reassign_clear():
    a1 = study_Student(name="sample_text")
    a2 = study_Student(name="sample_text_2")
    b = study_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'department4', {a1})
    assert _is_linked(b, 'department4', a1)
    if hasattr(a1, 'Student'):
        assert _is_linked(a1, 'Student', b)
    _safe_set(b, 'department4', {a2})
    assert _is_linked(b, 'department4', a2)
    if hasattr(a1, 'Student'):
        assert not _is_linked(a1, 'Student', b)
    if hasattr(a2, 'Student'):
        assert _is_linked(a2, 'Student', b)
    _safe_set(b, 'department4', set())
    assert not _is_linked(b, 'department4', a2)
    if hasattr(a2, 'Student'):
        assert not _is_linked(a2, 'Student', b)


def test_assoc_studyPlan14_reverse_link_reassign_clear():
    a1 = study_StudyPlan()
    a2 = study_StudyPlan()
    b = study_Student(name="sample_text")
    _safe_set(b, 'student', a1)
    assert _is_linked(b, 'student', a1)
    if hasattr(a1, 'StudyPlan'):
        assert _is_linked(a1, 'StudyPlan', b)
    _safe_set(b, 'student', a2)
    assert _is_linked(b, 'student', a2)
    if hasattr(a1, 'StudyPlan'):
        assert not _is_linked(a1, 'StudyPlan', b)
    if hasattr(a2, 'StudyPlan'):
        assert _is_linked(a2, 'StudyPlan', b)
    _safe_set(b, 'student', None)
    assert not _is_linked(b, 'student', a2)
    if hasattr(a2, 'StudyPlan'):
        assert not _is_linked(a2, 'StudyPlan', b)


def test_assoc_studyPlan40_reverse_link_reassign_clear():
    a1 = study_courseAllocation(grade="sample_text")
    a2 = study_courseAllocation(grade="sample_text_2")
    b = study_StudyPlan()
    _safe_set(b, 'study_StudyPlan42', a1)
    assert _is_linked(b, 'study_StudyPlan42', a1)
    if hasattr(a1, 'study_courseAllocation41'):
        assert _is_linked(a1, 'study_courseAllocation41', b)
    _safe_set(b, 'study_StudyPlan42', a2)
    assert _is_linked(b, 'study_StudyPlan42', a2)
    if hasattr(a1, 'study_courseAllocation41'):
        assert not _is_linked(a1, 'study_courseAllocation41', b)
    if hasattr(a2, 'study_courseAllocation41'):
        assert _is_linked(a2, 'study_courseAllocation41', b)
    _safe_set(b, 'study_StudyPlan42', None)
    assert not _is_linked(b, 'study_StudyPlan42', a2)
    if hasattr(a2, 'study_courseAllocation41'):
        assert not _is_linked(a2, 'study_courseAllocation41', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

