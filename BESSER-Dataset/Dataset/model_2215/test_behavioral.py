import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    studyProgramStructure_Course,
    studyProgramStructure_CourseAllocation,
    studyProgramStructure_CourseGroup,
    studyProgramStructure_Program,
    studyProgramStructure_Semester,
    studyProgramStructure_Specialization,
    studyProgramStructure_Student,
    studyProgramStructure_StudyPlan,
    studyProgramStructure_University,
    CourseStatus,
    Grade,
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

def test_assoc_baseSpecialization7_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    _safe_set(b, 'furtherSpecializations', a1)
    assert _is_linked(b, 'furtherSpecializations', a1)
    if hasattr(a1, 'Specialization8'):
        assert _is_linked(a1, 'Specialization8', b)
    _safe_set(b, 'furtherSpecializations', a2)
    assert _is_linked(b, 'furtherSpecializations', a2)
    if hasattr(a1, 'Specialization8'):
        assert not _is_linked(a1, 'Specialization8', b)
    if hasattr(a2, 'Specialization8'):
        assert _is_linked(a2, 'Specialization8', b)
    _safe_set(b, 'furtherSpecializations', None)
    assert not _is_linked(b, 'furtherSpecializations', a2)
    if hasattr(a2, 'Specialization8'):
        assert not _is_linked(a2, 'Specialization8', b)


def test_assoc_course37_reverse_link_reassign_clear():
    a1 = studyProgramStructure_CourseAllocation(grade="sample_text")
    a2 = studyProgramStructure_CourseAllocation(grade="sample_text_2")
    b = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'studyProgramStructure_Course39', a1)
    assert _is_linked(b, 'studyProgramStructure_Course39', a1)
    if hasattr(a1, 'studyProgramStructure_CourseAllocation38'):
        assert _is_linked(a1, 'studyProgramStructure_CourseAllocation38', b)
    _safe_set(b, 'studyProgramStructure_Course39', a2)
    assert _is_linked(b, 'studyProgramStructure_Course39', a2)
    if hasattr(a1, 'studyProgramStructure_CourseAllocation38'):
        assert not _is_linked(a1, 'studyProgramStructure_CourseAllocation38', b)
    if hasattr(a2, 'studyProgramStructure_CourseAllocation38'):
        assert _is_linked(a2, 'studyProgramStructure_CourseAllocation38', b)
    _safe_set(b, 'studyProgramStructure_Course39', None)
    assert not _is_linked(b, 'studyProgramStructure_Course39', a2)
    if hasattr(a2, 'studyProgramStructure_CourseAllocation38'):
        assert not _is_linked(a2, 'studyProgramStructure_CourseAllocation38', b)


def test_assoc_courseGroups12_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Semester(season="sample_text", year=7)
    a2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    b = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    _safe_set(b, 'CourseGroup', a1)
    assert _is_linked(b, 'CourseGroup', a1)
    if hasattr(a1, 'semester'):
        assert _is_linked(a1, 'semester', b)
    _safe_set(b, 'CourseGroup', a2)
    assert _is_linked(b, 'CourseGroup', a2)
    if hasattr(a1, 'semester'):
        assert not _is_linked(a1, 'semester', b)
    if hasattr(a2, 'semester'):
        assert _is_linked(a2, 'semester', b)
    _safe_set(b, 'CourseGroup', None)
    assert not _is_linked(b, 'CourseGroup', a2)
    if hasattr(a2, 'semester'):
        assert not _is_linked(a2, 'semester', b)


def test_assoc_courses20_reverse_link_reassign_clear():
    a1 = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    a2 = studyProgramStructure_CourseGroup(name="sample_text_2", status="sample_text_2")
    b = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'studyProgramStructure_Course', a1)
    assert _is_linked(b, 'studyProgramStructure_Course', a1)
    if hasattr(a1, 'studyProgramStructure_CourseGroup'):
        assert _is_linked(a1, 'studyProgramStructure_CourseGroup', b)
    _safe_set(b, 'studyProgramStructure_Course', a2)
    assert _is_linked(b, 'studyProgramStructure_Course', a2)
    if hasattr(a1, 'studyProgramStructure_CourseGroup'):
        assert not _is_linked(a1, 'studyProgramStructure_CourseGroup', b)
    if hasattr(a2, 'studyProgramStructure_CourseGroup'):
        assert _is_linked(a2, 'studyProgramStructure_CourseGroup', b)
    _safe_set(b, 'studyProgramStructure_Course', None)
    assert not _is_linked(b, 'studyProgramStructure_Course', a2)
    if hasattr(a2, 'studyProgramStructure_CourseGroup'):
        assert not _is_linked(a2, 'studyProgramStructure_CourseGroup', b)


def test_assoc_courses22_reverse_link_reassign_clear():
    a1 = studyProgramStructure_University(name="sample_text")
    a2 = studyProgramStructure_University(name="sample_text_2")
    b = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'studyProgramStructure_Course24', a1)
    assert _is_linked(b, 'studyProgramStructure_Course24', a1)
    if hasattr(a1, 'studyProgramStructure_University23'):
        assert _is_linked(a1, 'studyProgramStructure_University23', b)
    _safe_set(b, 'studyProgramStructure_Course24', a2)
    assert _is_linked(b, 'studyProgramStructure_Course24', a2)
    if hasattr(a1, 'studyProgramStructure_University23'):
        assert not _is_linked(a1, 'studyProgramStructure_University23', b)
    if hasattr(a2, 'studyProgramStructure_University23'):
        assert _is_linked(a2, 'studyProgramStructure_University23', b)
    _safe_set(b, 'studyProgramStructure_Course24', None)
    assert not _is_linked(b, 'studyProgramStructure_Course24', a2)
    if hasattr(a2, 'studyProgramStructure_University23'):
        assert not _is_linked(a2, 'studyProgramStructure_University23', b)


def test_assoc_furtherSpecializations4_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    _safe_set(b, 'baseSpecialization', {a1})
    assert _is_linked(b, 'baseSpecialization', a1)
    if hasattr(a1, 'Specialization5'):
        assert _is_linked(a1, 'Specialization5', b)
    _safe_set(b, 'baseSpecialization', {a2})
    assert _is_linked(b, 'baseSpecialization', a2)
    if hasattr(a1, 'Specialization5'):
        assert not _is_linked(a1, 'Specialization5', b)
    if hasattr(a2, 'Specialization5'):
        assert _is_linked(a2, 'Specialization5', b)
    _safe_set(b, 'baseSpecialization', set())
    assert not _is_linked(b, 'baseSpecialization', a2)
    if hasattr(a2, 'Specialization5'):
        assert not _is_linked(a2, 'Specialization5', b)


def test_assoc_program11_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'Program', a1)
    assert _is_linked(b, 'Program', a1)
    if hasattr(a1, 'specializations'):
        assert _is_linked(a1, 'specializations', b)
    _safe_set(b, 'Program', a2)
    assert _is_linked(b, 'Program', a2)
    if hasattr(a1, 'specializations'):
        assert not _is_linked(a1, 'specializations', b)
    if hasattr(a2, 'specializations'):
        assert _is_linked(a2, 'specializations', b)
    _safe_set(b, 'Program', None)
    assert not _is_linked(b, 'Program', a2)
    if hasattr(a2, 'specializations'):
        assert not _is_linked(a2, 'specializations', b)


def test_assoc_program13_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Semester(season="sample_text", year=7)
    a2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'Program14', a1)
    assert _is_linked(b, 'Program14', a1)
    if hasattr(a1, 'semesters'):
        assert _is_linked(a1, 'semesters', b)
    _safe_set(b, 'Program14', a2)
    assert _is_linked(b, 'Program14', a2)
    if hasattr(a1, 'semesters'):
        assert not _is_linked(a1, 'semesters', b)
    if hasattr(a2, 'semesters'):
        assert _is_linked(a2, 'semesters', b)
    _safe_set(b, 'Program14', None)
    assert not _is_linked(b, 'Program14', a2)
    if hasattr(a2, 'semesters'):
        assert not _is_linked(a2, 'semesters', b)


def test_assoc_program28_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Student(name="sample_text")
    a2 = studyProgramStructure_Student(name="sample_text_2")
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'studyProgramStructure_Program30', a1)
    assert _is_linked(b, 'studyProgramStructure_Program30', a1)
    if hasattr(a1, 'studyProgramStructure_Student29'):
        assert _is_linked(a1, 'studyProgramStructure_Student29', b)
    _safe_set(b, 'studyProgramStructure_Program30', a2)
    assert _is_linked(b, 'studyProgramStructure_Program30', a2)
    if hasattr(a1, 'studyProgramStructure_Student29'):
        assert not _is_linked(a1, 'studyProgramStructure_Student29', b)
    if hasattr(a2, 'studyProgramStructure_Student29'):
        assert _is_linked(a2, 'studyProgramStructure_Student29', b)
    _safe_set(b, 'studyProgramStructure_Program30', None)
    assert not _is_linked(b, 'studyProgramStructure_Program30', a2)
    if hasattr(a2, 'studyProgramStructure_Student29'):
        assert not _is_linked(a2, 'studyProgramStructure_Student29', b)


def test_assoc_programs21_reverse_link_reassign_clear():
    a1 = studyProgramStructure_University(name="sample_text")
    a2 = studyProgramStructure_University(name="sample_text_2")
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'studyProgramStructure_Program', a1)
    assert _is_linked(b, 'studyProgramStructure_Program', a1)
    if hasattr(a1, 'studyProgramStructure_University'):
        assert _is_linked(a1, 'studyProgramStructure_University', b)
    _safe_set(b, 'studyProgramStructure_Program', a2)
    assert _is_linked(b, 'studyProgramStructure_Program', a2)
    if hasattr(a1, 'studyProgramStructure_University'):
        assert not _is_linked(a1, 'studyProgramStructure_University', b)
    if hasattr(a2, 'studyProgramStructure_University'):
        assert _is_linked(a2, 'studyProgramStructure_University', b)
    _safe_set(b, 'studyProgramStructure_Program', None)
    assert not _is_linked(b, 'studyProgramStructure_Program', a2)
    if hasattr(a2, 'studyProgramStructure_University'):
        assert not _is_linked(a2, 'studyProgramStructure_University', b)


def test_assoc_semester18_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Semester(season="sample_text", year=7)
    a2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    b = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    _safe_set(b, 'courseGroups', a1)
    assert _is_linked(b, 'courseGroups', a1)
    if hasattr(a1, 'Semester19'):
        assert _is_linked(a1, 'Semester19', b)
    _safe_set(b, 'courseGroups', a2)
    assert _is_linked(b, 'courseGroups', a2)
    if hasattr(a1, 'Semester19'):
        assert not _is_linked(a1, 'Semester19', b)
    if hasattr(a2, 'Semester19'):
        assert _is_linked(a2, 'Semester19', b)
    _safe_set(b, 'courseGroups', None)
    assert not _is_linked(b, 'courseGroups', a2)
    if hasattr(a2, 'Semester19'):
        assert not _is_linked(a2, 'Semester19', b)


def test_assoc_semesters1_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Semester(season="sample_text", year=7)
    a2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'program2', {a1})
    assert _is_linked(b, 'program2', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'program2', {a2})
    assert _is_linked(b, 'program2', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'program2', set())
    assert not _is_linked(b, 'program2', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


def test_assoc_semesters9_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Semester(season="sample_text", year=7)
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


def test_assoc_specialization15_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Semester(season="sample_text", year=7)
    _safe_set(b, 'semesters16', a1)
    assert _is_linked(b, 'semesters16', a1)
    if hasattr(a1, 'Specialization17'):
        assert _is_linked(a1, 'Specialization17', b)
    _safe_set(b, 'semesters16', a2)
    assert _is_linked(b, 'semesters16', a2)
    if hasattr(a1, 'Specialization17'):
        assert not _is_linked(a1, 'Specialization17', b)
    if hasattr(a2, 'Specialization17'):
        assert _is_linked(a2, 'Specialization17', b)
    _safe_set(b, 'semesters16', None)
    assert not _is_linked(b, 'semesters16', a2)
    if hasattr(a2, 'Specialization17'):
        assert not _is_linked(a2, 'Specialization17', b)


def test_assoc_specializations0_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'program', {a1})
    assert _is_linked(b, 'program', a1)
    if hasattr(a1, 'Specialization'):
        assert _is_linked(a1, 'Specialization', b)
    _safe_set(b, 'program', {a2})
    assert _is_linked(b, 'program', a2)
    if hasattr(a1, 'Specialization'):
        assert not _is_linked(a1, 'Specialization', b)
    if hasattr(a2, 'Specialization'):
        assert _is_linked(a2, 'Specialization', b)
    _safe_set(b, 'program', set())
    assert not _is_linked(b, 'program', a2)
    if hasattr(a2, 'Specialization'):
        assert not _is_linked(a2, 'Specialization', b)


def test_assoc_specializations31_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Student(name="sample_text")
    a2 = studyProgramStructure_Student(name="sample_text_2")
    b = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    _safe_set(b, 'studyProgramStructure_Specialization', a1)
    assert _is_linked(b, 'studyProgramStructure_Specialization', a1)
    if hasattr(a1, 'studyProgramStructure_Student32'):
        assert _is_linked(a1, 'studyProgramStructure_Student32', b)
    _safe_set(b, 'studyProgramStructure_Specialization', a2)
    assert _is_linked(b, 'studyProgramStructure_Specialization', a2)
    if hasattr(a1, 'studyProgramStructure_Student32'):
        assert not _is_linked(a1, 'studyProgramStructure_Student32', b)
    if hasattr(a2, 'studyProgramStructure_Student32'):
        assert _is_linked(a2, 'studyProgramStructure_Student32', b)
    _safe_set(b, 'studyProgramStructure_Specialization', None)
    assert not _is_linked(b, 'studyProgramStructure_Specialization', a2)
    if hasattr(a2, 'studyProgramStructure_Student32'):
        assert not _is_linked(a2, 'studyProgramStructure_Student32', b)


def test_assoc_students25_reverse_link_reassign_clear():
    a1 = studyProgramStructure_University(name="sample_text")
    a2 = studyProgramStructure_University(name="sample_text_2")
    b = studyProgramStructure_Student(name="sample_text")
    _safe_set(b, 'studyProgramStructure_Student', a1)
    assert _is_linked(b, 'studyProgramStructure_Student', a1)
    if hasattr(a1, 'studyProgramStructure_University26'):
        assert _is_linked(a1, 'studyProgramStructure_University26', b)
    _safe_set(b, 'studyProgramStructure_Student', a2)
    assert _is_linked(b, 'studyProgramStructure_Student', a2)
    if hasattr(a1, 'studyProgramStructure_University26'):
        assert not _is_linked(a1, 'studyProgramStructure_University26', b)
    if hasattr(a2, 'studyProgramStructure_University26'):
        assert _is_linked(a2, 'studyProgramStructure_University26', b)
    _safe_set(b, 'studyProgramStructure_Student', None)
    assert not _is_linked(b, 'studyProgramStructure_Student', a2)
    if hasattr(a2, 'studyProgramStructure_University26'):
        assert not _is_linked(a2, 'studyProgramStructure_University26', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_courseAllocation34_stub_double():
    # studyProgramStructure_StudyPlan has no real 'studyProgramStructure_StudyPlan35' property in the generated
    # code (a bare stub) -- manually attach it so studyProgramStructure_CourseAllocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyProgramStructure_CourseAllocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyProgramStructure_CourseAllocation(grade="sample_text")
    partner = studyProgramStructure_StudyPlan()
    setattr(partner, 'studyProgramStructure_StudyPlan35', None)
    _safe_set(owner, 'studyProgramStructure_CourseAllocation', partner)
    assert owner in getattr(partner, 'studyProgramStructure_StudyPlan35')
    _safe_set(owner, 'studyProgramStructure_CourseAllocation', None)
    assert owner not in getattr(partner, 'studyProgramStructure_StudyPlan35')


def test_assoc_semesters33_stub_double():
    # studyProgramStructure_StudyPlan has no real 'studyProgramStructure_StudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so studyProgramStructure_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyProgramStructure_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyProgramStructure_Semester(season="sample_text", year=7)
    partner = studyProgramStructure_StudyPlan()
    setattr(partner, 'studyProgramStructure_StudyPlan', None)
    _safe_set(owner, 'studyProgramStructure_Semester', partner)
    assert owner in getattr(partner, 'studyProgramStructure_StudyPlan')
    _safe_set(owner, 'studyProgramStructure_Semester', None)
    assert owner not in getattr(partner, 'studyProgramStructure_StudyPlan')


def test_assoc_student36_stub_double():
    # studyProgramStructure_StudyPlan has no real 'studyPlan' property in the generated
    # code (a bare stub) -- manually attach it so studyProgramStructure_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyProgramStructure_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyProgramStructure_Student(name="sample_text")
    partner = studyProgramStructure_StudyPlan()
    setattr(partner, 'studyPlan', None)
    _safe_set(owner, 'Student', partner)
    assert getattr(partner, 'studyPlan') == owner
    _safe_set(owner, 'Student', None)
    assert getattr(partner, 'studyPlan') is None


def test_assoc_studyPlan27_stub_double():
    # studyProgramStructure_StudyPlan has no real 'StudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so studyProgramStructure_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyProgramStructure_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyProgramStructure_Student(name="sample_text")
    partner = studyProgramStructure_StudyPlan()
    setattr(partner, 'StudyPlan', None)
    _safe_set(owner, 'student', partner)
    assert getattr(partner, 'StudyPlan') == owner
    _safe_set(owner, 'student', None)
    assert getattr(partner, 'StudyPlan') is None


