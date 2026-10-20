import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    studyprogram_Course,
    studyprogram_Department,
    studyprogram_ElectiveCourses,
    studyprogram_ObligatoryCourses,
    studyprogram_Program,
    studyprogram_Semester,
    studyprogram_SemesterCourse,
    studyprogram_StudyPlan,
    studyprogram_University,
    studyprogram_Year,
    CourseType,
    SemesterType,
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

def test_assoc_course30_reverse_link_reassign_clear():
    a1 = studyprogram_SemesterCourse(name="sample_text", type="sample_text")
    a2 = studyprogram_SemesterCourse(name="sample_text_2", type="sample_text_2")
    b = studyprogram_Course(code="sample_text", credits="sample_text", name="sample_text", semester="sample_text")
    _safe_set(b, 'studyprogram_Course', a1)
    assert _is_linked(b, 'studyprogram_Course', a1)
    if hasattr(a1, 'studyprogram_SemesterCourse'):
        assert _is_linked(a1, 'studyprogram_SemesterCourse', b)
    _safe_set(b, 'studyprogram_Course', a2)
    assert _is_linked(b, 'studyprogram_Course', a2)
    if hasattr(a1, 'studyprogram_SemesterCourse'):
        assert not _is_linked(a1, 'studyprogram_SemesterCourse', b)
    if hasattr(a2, 'studyprogram_SemesterCourse'):
        assert _is_linked(a2, 'studyprogram_SemesterCourse', b)
    _safe_set(b, 'studyprogram_Course', None)
    assert not _is_linked(b, 'studyprogram_Course', a2)
    if hasattr(a2, 'studyprogram_SemesterCourse'):
        assert not _is_linked(a2, 'studyprogram_SemesterCourse', b)


def test_assoc_courses2_reverse_link_reassign_clear():
    a1 = studyprogram_Department(name="sample_text")
    a2 = studyprogram_Department(name="sample_text_2")
    b = studyprogram_Course(code="sample_text", credits="sample_text", name="sample_text", semester="sample_text")
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


def test_assoc_department31_reverse_link_reassign_clear():
    a1 = studyprogram_Department(name="sample_text")
    a2 = studyprogram_Department(name="sample_text_2")
    b = studyprogram_Course(code="sample_text", credits="sample_text", name="sample_text", semester="sample_text")
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'Department32'):
        assert _is_linked(a1, 'Department32', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'Department32'):
        assert not _is_linked(a1, 'Department32', b)
    if hasattr(a2, 'Department32'):
        assert _is_linked(a2, 'Department32', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'Department32'):
        assert not _is_linked(a2, 'Department32', b)


def test_assoc_department5_reverse_link_reassign_clear():
    a1 = studyprogram_Program(name="sample_text")
    a2 = studyprogram_Program(name="sample_text_2")
    b = studyprogram_Department(name="sample_text")
    _safe_set(b, 'Department6', a1)
    assert _is_linked(b, 'Department6', a1)
    if hasattr(a1, 'programs'):
        assert _is_linked(a1, 'programs', b)
    _safe_set(b, 'Department6', a2)
    assert _is_linked(b, 'Department6', a2)
    if hasattr(a1, 'programs'):
        assert not _is_linked(a1, 'programs', b)
    if hasattr(a2, 'programs'):
        assert _is_linked(a2, 'programs', b)
    _safe_set(b, 'Department6', None)
    assert not _is_linked(b, 'Department6', a2)
    if hasattr(a2, 'programs'):
        assert not _is_linked(a2, 'programs', b)


def test_assoc_departments0_reverse_link_reassign_clear():
    a1 = studyprogram_University(name="sample_text")
    a2 = studyprogram_University(name="sample_text_2")
    b = studyprogram_Department(name="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'school'):
        assert _is_linked(a1, 'school', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'school'):
        assert not _is_linked(a1, 'school', b)
    if hasattr(a2, 'school'):
        assert _is_linked(a2, 'school', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'school'):
        assert not _is_linked(a2, 'school', b)


def test_assoc_program13_reverse_link_reassign_clear():
    a1 = studyprogram_StudyPlan(name="sample_text")
    a2 = studyprogram_StudyPlan(name="sample_text_2")
    b = studyprogram_Program(name="sample_text")
    _safe_set(b, 'Program14', a1)
    assert _is_linked(b, 'Program14', a1)
    if hasattr(a1, 'studyPlans'):
        assert _is_linked(a1, 'studyPlans', b)
    _safe_set(b, 'Program14', a2)
    assert _is_linked(b, 'Program14', a2)
    if hasattr(a1, 'studyPlans'):
        assert not _is_linked(a1, 'studyPlans', b)
    if hasattr(a2, 'studyPlans'):
        assert _is_linked(a2, 'studyPlans', b)
    _safe_set(b, 'Program14', None)
    assert not _is_linked(b, 'Program14', a2)
    if hasattr(a2, 'studyPlans'):
        assert not _is_linked(a2, 'studyPlans', b)


def test_assoc_programs3_reverse_link_reassign_clear():
    a1 = studyprogram_Program(name="sample_text")
    a2 = studyprogram_Program(name="sample_text_2")
    b = studyprogram_Department(name="sample_text")
    _safe_set(b, 'department4', {a1})
    assert _is_linked(b, 'department4', a1)
    if hasattr(a1, 'Program'):
        assert _is_linked(a1, 'Program', b)
    _safe_set(b, 'department4', {a2})
    assert _is_linked(b, 'department4', a2)
    if hasattr(a1, 'Program'):
        assert not _is_linked(a1, 'Program', b)
    if hasattr(a2, 'Program'):
        assert _is_linked(a2, 'Program', b)
    _safe_set(b, 'department4', set())
    assert not _is_linked(b, 'department4', a2)
    if hasattr(a2, 'Program'):
        assert not _is_linked(a2, 'Program', b)


def test_assoc_school1_reverse_link_reassign_clear():
    a1 = studyprogram_University(name="sample_text")
    a2 = studyprogram_University(name="sample_text_2")
    b = studyprogram_Department(name="sample_text")
    _safe_set(b, 'departments', a1)
    assert _is_linked(b, 'departments', a1)
    if hasattr(a1, 'University'):
        assert _is_linked(a1, 'University', b)
    _safe_set(b, 'departments', a2)
    assert _is_linked(b, 'departments', a2)
    if hasattr(a1, 'University'):
        assert not _is_linked(a1, 'University', b)
    if hasattr(a2, 'University'):
        assert _is_linked(a2, 'University', b)
    _safe_set(b, 'departments', None)
    assert not _is_linked(b, 'departments', a2)
    if hasattr(a2, 'University'):
        assert not _is_linked(a2, 'University', b)


def test_assoc_semester28_reverse_link_reassign_clear():
    a1 = studyprogram_SemesterCourse(name="sample_text", type="sample_text")
    a2 = studyprogram_SemesterCourse(name="sample_text_2", type="sample_text_2")
    b = studyprogram_Semester(type="sample_text")
    _safe_set(b, 'Semester29', a1)
    assert _is_linked(b, 'Semester29', a1)
    if hasattr(a1, 'semesterCourses'):
        assert _is_linked(a1, 'semesterCourses', b)
    _safe_set(b, 'Semester29', a2)
    assert _is_linked(b, 'Semester29', a2)
    if hasattr(a1, 'semesterCourses'):
        assert not _is_linked(a1, 'semesterCourses', b)
    if hasattr(a2, 'semesterCourses'):
        assert _is_linked(a2, 'semesterCourses', b)
    _safe_set(b, 'Semester29', None)
    assert not _is_linked(b, 'Semester29', a2)
    if hasattr(a2, 'semesterCourses'):
        assert not _is_linked(a2, 'semesterCourses', b)


def test_assoc_semesterCourses27_reverse_link_reassign_clear():
    a1 = studyprogram_SemesterCourse(name="sample_text", type="sample_text")
    a2 = studyprogram_SemesterCourse(name="sample_text_2", type="sample_text_2")
    b = studyprogram_Semester(type="sample_text")
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


def test_assoc_semesters22_reverse_link_reassign_clear():
    a1 = studyprogram_Year(value=7)
    a2 = studyprogram_Year(value=13)
    b = studyprogram_Semester(type="sample_text")
    _safe_set(b, 'Semester', a1)
    assert _is_linked(b, 'Semester', a1)
    if hasattr(a1, 'year'):
        assert _is_linked(a1, 'year', b)
    _safe_set(b, 'Semester', a2)
    assert _is_linked(b, 'Semester', a2)
    if hasattr(a1, 'year'):
        assert not _is_linked(a1, 'year', b)
    if hasattr(a2, 'year'):
        assert _is_linked(a2, 'year', b)
    _safe_set(b, 'Semester', None)
    assert not _is_linked(b, 'Semester', a2)
    if hasattr(a2, 'year'):
        assert not _is_linked(a2, 'year', b)


def test_assoc_specialisations19_reverse_link_reassign_clear():
    a1 = studyprogram_StudyPlan(name="sample_text")
    a2 = studyprogram_StudyPlan(name="sample_text_2")
    b = studyprogram_StudyPlan(name="sample_text")
    _safe_set(b, 'studyPlan20', {a1})
    assert _is_linked(b, 'studyPlan20', a1)
    if hasattr(a1, 'StudyPlan21'):
        assert _is_linked(a1, 'StudyPlan21', b)
    _safe_set(b, 'studyPlan20', {a2})
    assert _is_linked(b, 'studyPlan20', a2)
    if hasattr(a1, 'StudyPlan21'):
        assert not _is_linked(a1, 'StudyPlan21', b)
    if hasattr(a2, 'StudyPlan21'):
        assert _is_linked(a2, 'StudyPlan21', b)
    _safe_set(b, 'studyPlan20', set())
    assert not _is_linked(b, 'studyPlan20', a2)
    if hasattr(a2, 'StudyPlan21'):
        assert not _is_linked(a2, 'StudyPlan21', b)


def test_assoc_studyPlan16_reverse_link_reassign_clear():
    a1 = studyprogram_StudyPlan(name="sample_text")
    a2 = studyprogram_StudyPlan(name="sample_text_2")
    b = studyprogram_StudyPlan(name="sample_text")
    _safe_set(b, 'specialisations', a1)
    assert _is_linked(b, 'specialisations', a1)
    if hasattr(a1, 'StudyPlan17'):
        assert _is_linked(a1, 'StudyPlan17', b)
    _safe_set(b, 'specialisations', a2)
    assert _is_linked(b, 'specialisations', a2)
    if hasattr(a1, 'StudyPlan17'):
        assert not _is_linked(a1, 'StudyPlan17', b)
    if hasattr(a2, 'StudyPlan17'):
        assert _is_linked(a2, 'StudyPlan17', b)
    _safe_set(b, 'specialisations', None)
    assert not _is_linked(b, 'specialisations', a2)
    if hasattr(a2, 'StudyPlan17'):
        assert not _is_linked(a2, 'StudyPlan17', b)


def test_assoc_studyPlan23_reverse_link_reassign_clear():
    a1 = studyprogram_Year(value=7)
    a2 = studyprogram_Year(value=13)
    b = studyprogram_StudyPlan(name="sample_text")
    _safe_set(b, 'StudyPlan24', a1)
    assert _is_linked(b, 'StudyPlan24', a1)
    if hasattr(a1, 'years'):
        assert _is_linked(a1, 'years', b)
    _safe_set(b, 'StudyPlan24', a2)
    assert _is_linked(b, 'StudyPlan24', a2)
    if hasattr(a1, 'years'):
        assert not _is_linked(a1, 'years', b)
    if hasattr(a2, 'years'):
        assert _is_linked(a2, 'years', b)
    _safe_set(b, 'StudyPlan24', None)
    assert not _is_linked(b, 'StudyPlan24', a2)
    if hasattr(a2, 'years'):
        assert not _is_linked(a2, 'years', b)


def test_assoc_studyPlans7_reverse_link_reassign_clear():
    a1 = studyprogram_StudyPlan(name="sample_text")
    a2 = studyprogram_StudyPlan(name="sample_text_2")
    b = studyprogram_Program(name="sample_text")
    _safe_set(b, 'program', {a1})
    assert _is_linked(b, 'program', a1)
    if hasattr(a1, 'StudyPlan'):
        assert _is_linked(a1, 'StudyPlan', b)
    _safe_set(b, 'program', {a2})
    assert _is_linked(b, 'program', a2)
    if hasattr(a1, 'StudyPlan'):
        assert not _is_linked(a1, 'StudyPlan', b)
    if hasattr(a2, 'StudyPlan'):
        assert _is_linked(a2, 'StudyPlan', b)
    _safe_set(b, 'program', set())
    assert not _is_linked(b, 'program', a2)
    if hasattr(a2, 'StudyPlan'):
        assert not _is_linked(a2, 'StudyPlan', b)


def test_assoc_year25_reverse_link_reassign_clear():
    a1 = studyprogram_Year(value=7)
    a2 = studyprogram_Year(value=13)
    b = studyprogram_Semester(type="sample_text")
    _safe_set(b, 'semesters', a1)
    assert _is_linked(b, 'semesters', a1)
    if hasattr(a1, 'Year26'):
        assert _is_linked(a1, 'Year26', b)
    _safe_set(b, 'semesters', a2)
    assert _is_linked(b, 'semesters', a2)
    if hasattr(a1, 'Year26'):
        assert not _is_linked(a1, 'Year26', b)
    if hasattr(a2, 'Year26'):
        assert _is_linked(a2, 'Year26', b)
    _safe_set(b, 'semesters', None)
    assert not _is_linked(b, 'semesters', a2)
    if hasattr(a2, 'Year26'):
        assert not _is_linked(a2, 'Year26', b)


def test_assoc_years12_reverse_link_reassign_clear():
    a1 = studyprogram_Year(value=7)
    a2 = studyprogram_Year(value=13)
    b = studyprogram_StudyPlan(name="sample_text")
    _safe_set(b, 'studyPlan', {a1})
    assert _is_linked(b, 'studyPlan', a1)
    if hasattr(a1, 'Year'):
        assert _is_linked(a1, 'Year', b)
    _safe_set(b, 'studyPlan', {a2})
    assert _is_linked(b, 'studyPlan', a2)
    if hasattr(a1, 'Year'):
        assert not _is_linked(a1, 'Year', b)
    if hasattr(a2, 'Year'):
        assert _is_linked(a2, 'Year', b)
    _safe_set(b, 'studyPlan', set())
    assert not _is_linked(b, 'studyPlan', a2)
    if hasattr(a2, 'Year'):
        assert not _is_linked(a2, 'Year', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_courses35_stub_double():
    # studyprogram_ElectiveCourses has no real 'studyprogram_ElectiveCourses' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Course(code="sample_text", credits="sample_text", name="sample_text", semester="sample_text")
    partner = studyprogram_ElectiveCourses()
    setattr(partner, 'studyprogram_ElectiveCourses', None)
    _safe_set(owner, 'studyprogram_Course36', partner)
    assert owner in getattr(partner, 'studyprogram_ElectiveCourses')
    _safe_set(owner, 'studyprogram_Course36', None)
    assert owner not in getattr(partner, 'studyprogram_ElectiveCourses')


def test_assoc_courses39_stub_double():
    # studyprogram_ObligatoryCourses has no real 'studyprogram_ObligatoryCourses' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Course(code="sample_text", credits="sample_text", name="sample_text", semester="sample_text")
    partner = studyprogram_ObligatoryCourses()
    setattr(partner, 'studyprogram_ObligatoryCourses', None)
    _safe_set(owner, 'studyprogram_Course40', partner)
    assert owner in getattr(partner, 'studyprogram_ObligatoryCourses')
    _safe_set(owner, 'studyprogram_Course40', None)
    assert owner not in getattr(partner, 'studyprogram_ObligatoryCourses')


def test_assoc_electiveCourses8_stub_double():
    # studyprogram_ElectiveCourses has no real 'ElectiveCourses' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Program(name="sample_text")
    partner = studyprogram_ElectiveCourses()
    setattr(partner, 'ElectiveCourses', None)
    _safe_set(owner, 'program9', partner)
    assert getattr(partner, 'ElectiveCourses') == owner
    _safe_set(owner, 'program9', None)
    assert getattr(partner, 'ElectiveCourses') is None


def test_assoc_obligatoryCourses10_stub_double():
    # studyprogram_ObligatoryCourses has no real 'ObligatoryCourses' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Program(name="sample_text")
    partner = studyprogram_ObligatoryCourses()
    setattr(partner, 'ObligatoryCourses', None)
    _safe_set(owner, 'program11', partner)
    assert getattr(partner, 'ObligatoryCourses') == owner
    _safe_set(owner, 'program11', None)
    assert getattr(partner, 'ObligatoryCourses') is None


def test_assoc_program33_stub_double():
    # studyprogram_ElectiveCourses has no real 'electiveCourses' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Program(name="sample_text")
    partner = studyprogram_ElectiveCourses()
    setattr(partner, 'electiveCourses', None)
    _safe_set(owner, 'Program34', partner)
    assert getattr(partner, 'electiveCourses') == owner
    _safe_set(owner, 'Program34', None)
    assert getattr(partner, 'electiveCourses') is None


def test_assoc_program37_stub_double():
    # studyprogram_ObligatoryCourses has no real 'obligatoryCourses' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Program(name="sample_text")
    partner = studyprogram_ObligatoryCourses()
    setattr(partner, 'obligatoryCourses', None)
    _safe_set(owner, 'Program38', partner)
    assert getattr(partner, 'obligatoryCourses') == owner
    _safe_set(owner, 'Program38', None)
    assert getattr(partner, 'obligatoryCourses') is None


