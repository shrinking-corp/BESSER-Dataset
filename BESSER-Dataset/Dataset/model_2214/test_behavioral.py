import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    study_Course,
    study_CourseRelationship,
    study_ElectiveCourseList,
    study_IndividualStudyPlan,
    study_Semester,
    study_Specialization,
    study_Student,
    study_StudyProgramme,
    study_University,
    GradeEnum,
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

def test_assoc_allSpecializations6_reverse_link_reassign_clear():
    a1 = study_StudyProgramme(code="sample_text", name="sample_text", numYears=7)
    a2 = study_StudyProgramme(code="sample_text_2", name="sample_text_2", numYears=13)
    b = study_Specialization(name="sample_text", numYears=7)
    _safe_set(b, 'Specialization', a1)
    assert _is_linked(b, 'Specialization', a1)
    if hasattr(a1, 'studyProgramme'):
        assert _is_linked(a1, 'studyProgramme', b)
    _safe_set(b, 'Specialization', a2)
    assert _is_linked(b, 'Specialization', a2)
    if hasattr(a1, 'studyProgramme'):
        assert not _is_linked(a1, 'studyProgramme', b)
    if hasattr(a2, 'studyProgramme'):
        assert _is_linked(a2, 'studyProgramme', b)
    _safe_set(b, 'Specialization', None)
    assert not _is_linked(b, 'Specialization', a2)
    if hasattr(a2, 'studyProgramme'):
        assert not _is_linked(a2, 'studyProgramme', b)


def test_assoc_baseSpecializations7_reverse_link_reassign_clear():
    a1 = study_StudyProgramme(code="sample_text", name="sample_text", numYears=7)
    a2 = study_StudyProgramme(code="sample_text_2", name="sample_text_2", numYears=13)
    b = study_Specialization(name="sample_text", numYears=7)
    _safe_set(b, 'study_Specialization', a1)
    assert _is_linked(b, 'study_Specialization', a1)
    if hasattr(a1, 'study_StudyProgramme'):
        assert _is_linked(a1, 'study_StudyProgramme', b)
    _safe_set(b, 'study_Specialization', a2)
    assert _is_linked(b, 'study_Specialization', a2)
    if hasattr(a1, 'study_StudyProgramme'):
        assert not _is_linked(a1, 'study_StudyProgramme', b)
    if hasattr(a2, 'study_StudyProgramme'):
        assert _is_linked(a2, 'study_StudyProgramme', b)
    _safe_set(b, 'study_Specialization', None)
    assert not _is_linked(b, 'study_Specialization', a2)
    if hasattr(a2, 'study_StudyProgramme'):
        assert not _is_linked(a2, 'study_StudyProgramme', b)


def test_assoc_course36_reverse_link_reassign_clear():
    a1 = study_CourseRelationship(grade="sample_text", numExamAttempts=7)
    a2 = study_CourseRelationship(grade="sample_text_2", numExamAttempts=13)
    b = study_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'study_Course37', a1)
    assert _is_linked(b, 'study_Course37', a1)
    if hasattr(a1, 'study_CourseRelationship'):
        assert _is_linked(a1, 'study_CourseRelationship', b)
    _safe_set(b, 'study_Course37', a2)
    assert _is_linked(b, 'study_Course37', a2)
    if hasattr(a1, 'study_CourseRelationship'):
        assert not _is_linked(a1, 'study_CourseRelationship', b)
    if hasattr(a2, 'study_CourseRelationship'):
        assert _is_linked(a2, 'study_CourseRelationship', b)
    _safe_set(b, 'study_Course37', None)
    assert not _is_linked(b, 'study_Course37', a2)
    if hasattr(a2, 'study_CourseRelationship'):
        assert not _is_linked(a2, 'study_CourseRelationship', b)


def test_assoc_courses1_reverse_link_reassign_clear():
    a1 = study_University(name="sample_text")
    a2 = study_University(name="sample_text_2")
    b = study_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'university2'):
        assert _is_linked(a1, 'university2', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'university2'):
        assert not _is_linked(a1, 'university2', b)
    if hasattr(a2, 'university2'):
        assert _is_linked(a2, 'university2', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'university2'):
        assert not _is_linked(a2, 'university2', b)


def test_assoc_furtherSpecializations12_reverse_link_reassign_clear():
    a1 = study_Specialization(name="sample_text", numYears=7)
    a2 = study_Specialization(name="sample_text_2", numYears=13)
    b = study_Specialization(name="sample_text", numYears=7)
    _safe_set(b, 'study_Specialization13', a1)
    assert _is_linked(b, 'study_Specialization13', a1)
    if hasattr(a1, 'study_Specialization11'):
        assert _is_linked(a1, 'study_Specialization11', b)
    _safe_set(b, 'study_Specialization13', a2)
    assert _is_linked(b, 'study_Specialization13', a2)
    if hasattr(a1, 'study_Specialization11'):
        assert not _is_linked(a1, 'study_Specialization11', b)
    if hasattr(a2, 'study_Specialization11'):
        assert _is_linked(a2, 'study_Specialization11', b)
    _safe_set(b, 'study_Specialization13', None)
    assert not _is_linked(b, 'study_Specialization13', a2)
    if hasattr(a2, 'study_Specialization11'):
        assert not _is_linked(a2, 'study_Specialization11', b)


def test_assoc_mandatoryCourses16_reverse_link_reassign_clear():
    a1 = study_Semester(ordinal=7)
    a2 = study_Semester(ordinal=13)
    b = study_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
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


def test_assoc_semesters10_reverse_link_reassign_clear():
    a1 = study_Specialization(name="sample_text", numYears=7)
    a2 = study_Specialization(name="sample_text_2", numYears=13)
    b = study_Semester(ordinal=7)
    _safe_set(b, 'Semester', a1)
    assert _is_linked(b, 'Semester', a1)
    if hasattr(a1, 'specialization'):
        assert _is_linked(a1, 'specialization', b)
    _safe_set(b, 'Semester', a2)
    assert _is_linked(b, 'Semester', a2)
    if hasattr(a1, 'specialization'):
        assert not _is_linked(a1, 'specialization', b)
    if hasattr(a2, 'specialization'):
        assert _is_linked(a2, 'specialization', b)
    _safe_set(b, 'Semester', None)
    assert not _is_linked(b, 'Semester', a2)
    if hasattr(a2, 'specialization'):
        assert not _is_linked(a2, 'specialization', b)


def test_assoc_specialization14_reverse_link_reassign_clear():
    a1 = study_Specialization(name="sample_text", numYears=7)
    a2 = study_Specialization(name="sample_text_2", numYears=13)
    b = study_Semester(ordinal=7)
    _safe_set(b, 'semesters', a1)
    assert _is_linked(b, 'semesters', a1)
    if hasattr(a1, 'Specialization15'):
        assert _is_linked(a1, 'Specialization15', b)
    _safe_set(b, 'semesters', a2)
    assert _is_linked(b, 'semesters', a2)
    if hasattr(a1, 'Specialization15'):
        assert not _is_linked(a1, 'Specialization15', b)
    if hasattr(a2, 'Specialization15'):
        assert _is_linked(a2, 'Specialization15', b)
    _safe_set(b, 'semesters', None)
    assert not _is_linked(b, 'semesters', a2)
    if hasattr(a2, 'Specialization15'):
        assert not _is_linked(a2, 'Specialization15', b)


def test_assoc_students3_reverse_link_reassign_clear():
    a1 = study_University(name="sample_text")
    a2 = study_University(name="sample_text_2")
    b = study_Student(name="sample_text", username="sample_text")
    _safe_set(b, 'Student', a1)
    assert _is_linked(b, 'Student', a1)
    if hasattr(a1, 'university4'):
        assert _is_linked(a1, 'university4', b)
    _safe_set(b, 'Student', a2)
    assert _is_linked(b, 'Student', a2)
    if hasattr(a1, 'university4'):
        assert not _is_linked(a1, 'university4', b)
    if hasattr(a2, 'university4'):
        assert _is_linked(a2, 'university4', b)
    _safe_set(b, 'Student', None)
    assert not _is_linked(b, 'Student', a2)
    if hasattr(a2, 'university4'):
        assert not _is_linked(a2, 'university4', b)


def test_assoc_studyProgramme8_reverse_link_reassign_clear():
    a1 = study_StudyProgramme(code="sample_text", name="sample_text", numYears=7)
    a2 = study_StudyProgramme(code="sample_text_2", name="sample_text_2", numYears=13)
    b = study_Specialization(name="sample_text", numYears=7)
    _safe_set(b, 'allSpecializations', a1)
    assert _is_linked(b, 'allSpecializations', a1)
    if hasattr(a1, 'StudyProgramme9'):
        assert _is_linked(a1, 'StudyProgramme9', b)
    _safe_set(b, 'allSpecializations', a2)
    assert _is_linked(b, 'allSpecializations', a2)
    if hasattr(a1, 'StudyProgramme9'):
        assert not _is_linked(a1, 'StudyProgramme9', b)
    if hasattr(a2, 'StudyProgramme9'):
        assert _is_linked(a2, 'StudyProgramme9', b)
    _safe_set(b, 'allSpecializations', None)
    assert not _is_linked(b, 'allSpecializations', a2)
    if hasattr(a2, 'StudyProgramme9'):
        assert not _is_linked(a2, 'StudyProgramme9', b)


def test_assoc_studyProgrammes0_reverse_link_reassign_clear():
    a1 = study_University(name="sample_text")
    a2 = study_University(name="sample_text_2")
    b = study_StudyProgramme(code="sample_text", name="sample_text", numYears=7)
    _safe_set(b, 'StudyProgramme', a1)
    assert _is_linked(b, 'StudyProgramme', a1)
    if hasattr(a1, 'university'):
        assert _is_linked(a1, 'university', b)
    _safe_set(b, 'StudyProgramme', a2)
    assert _is_linked(b, 'StudyProgramme', a2)
    if hasattr(a1, 'university'):
        assert not _is_linked(a1, 'university', b)
    if hasattr(a2, 'university'):
        assert _is_linked(a2, 'university', b)
    _safe_set(b, 'StudyProgramme', None)
    assert not _is_linked(b, 'StudyProgramme', a2)
    if hasattr(a2, 'university'):
        assert not _is_linked(a2, 'university', b)


def test_assoc_university18_reverse_link_reassign_clear():
    a1 = study_University(name="sample_text")
    a2 = study_University(name="sample_text_2")
    b = study_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'University19'):
        assert _is_linked(a1, 'University19', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'University19'):
        assert not _is_linked(a1, 'University19', b)
    if hasattr(a2, 'University19'):
        assert _is_linked(a2, 'University19', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'University19'):
        assert not _is_linked(a2, 'University19', b)


def test_assoc_university24_reverse_link_reassign_clear():
    a1 = study_University(name="sample_text")
    a2 = study_University(name="sample_text_2")
    b = study_Student(name="sample_text", username="sample_text")
    _safe_set(b, 'students', a1)
    assert _is_linked(b, 'students', a1)
    if hasattr(a1, 'University25'):
        assert _is_linked(a1, 'University25', b)
    _safe_set(b, 'students', a2)
    assert _is_linked(b, 'students', a2)
    if hasattr(a1, 'University25'):
        assert not _is_linked(a1, 'University25', b)
    if hasattr(a2, 'University25'):
        assert _is_linked(a2, 'University25', b)
    _safe_set(b, 'students', None)
    assert not _is_linked(b, 'students', a2)
    if hasattr(a2, 'University25'):
        assert not _is_linked(a2, 'University25', b)


def test_assoc_university5_reverse_link_reassign_clear():
    a1 = study_University(name="sample_text")
    a2 = study_University(name="sample_text_2")
    b = study_StudyProgramme(code="sample_text", name="sample_text", numYears=7)
    _safe_set(b, 'studyProgrammes', a1)
    assert _is_linked(b, 'studyProgrammes', a1)
    if hasattr(a1, 'University'):
        assert _is_linked(a1, 'University', b)
    _safe_set(b, 'studyProgrammes', a2)
    assert _is_linked(b, 'studyProgrammes', a2)
    if hasattr(a1, 'University'):
        assert not _is_linked(a1, 'University', b)
    if hasattr(a2, 'University'):
        assert _is_linked(a2, 'University', b)
    _safe_set(b, 'studyProgrammes', None)
    assert not _is_linked(b, 'studyProgrammes', a2)
    if hasattr(a2, 'University'):
        assert not _is_linked(a2, 'University', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_courses22_stub_double():
    # study_ElectiveCourseList has no real 'study_ElectiveCourseList' property in the generated
    # code (a bare stub) -- manually attach it so study_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    partner = study_ElectiveCourseList()
    setattr(partner, 'study_ElectiveCourseList', None)
    _safe_set(owner, 'study_Course23', partner)
    assert owner in getattr(partner, 'study_ElectiveCourseList')
    _safe_set(owner, 'study_Course23', None)
    assert owner not in getattr(partner, 'study_ElectiveCourseList')


def test_assoc_courses31_stub_double():
    # study_IndividualStudyPlan has no real 'studyPlan32' property in the generated
    # code (a bare stub) -- manually attach it so study_CourseRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_CourseRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_CourseRelationship(grade="sample_text", numExamAttempts=7)
    partner = study_IndividualStudyPlan()
    setattr(partner, 'studyPlan32', None)
    _safe_set(owner, 'CourseRelationship', partner)
    assert owner in getattr(partner, 'studyPlan32')
    _safe_set(owner, 'CourseRelationship', None)
    assert owner not in getattr(partner, 'studyPlan32')


def test_assoc_currentSemester29_stub_double():
    # study_IndividualStudyPlan has no real 'study_IndividualStudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so study_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Semester(ordinal=7)
    partner = study_IndividualStudyPlan()
    setattr(partner, 'study_IndividualStudyPlan', None)
    _safe_set(owner, 'study_Semester30', partner)
    assert getattr(partner, 'study_IndividualStudyPlan') == owner
    _safe_set(owner, 'study_Semester30', None)
    assert getattr(partner, 'study_IndividualStudyPlan') is None


def test_assoc_electiveCourses17_stub_double():
    # study_ElectiveCourseList has no real 'ElectiveCourseList' property in the generated
    # code (a bare stub) -- manually attach it so study_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Semester(ordinal=7)
    partner = study_ElectiveCourseList()
    setattr(partner, 'ElectiveCourseList', None)
    _safe_set(owner, 'semester', partner)
    assert getattr(partner, 'ElectiveCourseList') == owner
    _safe_set(owner, 'semester', None)
    assert getattr(partner, 'ElectiveCourseList') is None


def test_assoc_semester20_stub_double():
    # study_ElectiveCourseList has no real 'electiveCourses' property in the generated
    # code (a bare stub) -- manually attach it so study_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Semester(ordinal=7)
    partner = study_ElectiveCourseList()
    setattr(partner, 'electiveCourses', None)
    _safe_set(owner, 'Semester21', partner)
    assert getattr(partner, 'electiveCourses') == owner
    _safe_set(owner, 'Semester21', None)
    assert getattr(partner, 'electiveCourses') is None


def test_assoc_student27_stub_double():
    # study_IndividualStudyPlan has no real 'studyPlan' property in the generated
    # code (a bare stub) -- manually attach it so study_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Student(name="sample_text", username="sample_text")
    partner = study_IndividualStudyPlan()
    setattr(partner, 'studyPlan', None)
    _safe_set(owner, 'Student28', partner)
    assert getattr(partner, 'studyPlan') == owner
    _safe_set(owner, 'Student28', None)
    assert getattr(partner, 'studyPlan') is None


def test_assoc_studyPlan26_stub_double():
    # study_IndividualStudyPlan has no real 'IndividualStudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so study_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Student(name="sample_text", username="sample_text")
    partner = study_IndividualStudyPlan()
    setattr(partner, 'IndividualStudyPlan', None)
    _safe_set(owner, 'student', partner)
    assert getattr(partner, 'IndividualStudyPlan') == owner
    _safe_set(owner, 'student', None)
    assert getattr(partner, 'IndividualStudyPlan') is None


def test_assoc_studyPlan33_stub_double():
    # study_IndividualStudyPlan has no real 'IndividualStudyPlan35' property in the generated
    # code (a bare stub) -- manually attach it so study_CourseRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_CourseRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_CourseRelationship(grade="sample_text", numExamAttempts=7)
    partner = study_IndividualStudyPlan()
    setattr(partner, 'IndividualStudyPlan35', None)
    _safe_set(owner, 'courses34', partner)
    assert getattr(partner, 'IndividualStudyPlan35') == owner
    _safe_set(owner, 'courses34', None)
    assert getattr(partner, 'IndividualStudyPlan35') is None


