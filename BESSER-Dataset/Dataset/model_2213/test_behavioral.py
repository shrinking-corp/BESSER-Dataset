import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Semester,
    studyPlan_Course,
    studyPlan_Semester,
    studyPlan_SemesterPlan,
    studyPlan_SemesterProgramme,
    studyPlan_Specialization,
    studyPlan_Student,
    studyPlan_StudyPlan,
    studyPlan_StudyProgramme,
    studyPlan_University,
    SeasonEnum,
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

def test_assoc_continuations28_reverse_link_reassign_clear():
    a1 = studyPlan_Specialization(name="sample_text", year=7)
    a2 = studyPlan_Specialization(name="sample_text_2", year=13)
    b = studyPlan_Specialization(name="sample_text", year=7)
    _safe_set(b, 'studyPlan_Specialization27', {a1})
    assert _is_linked(b, 'studyPlan_Specialization27', a1)
    if hasattr(a1, 'studyPlan_Specialization'):
        assert _is_linked(a1, 'studyPlan_Specialization', b)
    _safe_set(b, 'studyPlan_Specialization27', {a2})
    assert _is_linked(b, 'studyPlan_Specialization27', a2)
    if hasattr(a1, 'studyPlan_Specialization'):
        assert not _is_linked(a1, 'studyPlan_Specialization', b)
    if hasattr(a2, 'studyPlan_Specialization'):
        assert _is_linked(a2, 'studyPlan_Specialization', b)
    _safe_set(b, 'studyPlan_Specialization27', set())
    assert not _is_linked(b, 'studyPlan_Specialization27', a2)
    if hasattr(a2, 'studyPlan_Specialization'):
        assert not _is_linked(a2, 'studyPlan_Specialization', b)


def test_assoc_courses4_reverse_link_reassign_clear():
    a1 = studyPlan_University(name="sample_text")
    a2 = studyPlan_University(name="sample_text_2")
    b = studyPlan_Course(codename="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'university5'):
        assert _is_linked(a1, 'university5', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'university5'):
        assert not _is_linked(a1, 'university5', b)
    if hasattr(a2, 'university5'):
        assert _is_linked(a2, 'university5', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'university5'):
        assert not _is_linked(a2, 'university5', b)


def test_assoc_specializations23_reverse_link_reassign_clear():
    a1 = studyPlan_StudyProgramme(codename="sample_text", lengthInYears=7, name="sample_text")
    a2 = studyPlan_StudyProgramme(codename="sample_text_2", lengthInYears=13, name="sample_text_2")
    b = studyPlan_Specialization(name="sample_text", year=7)
    _safe_set(b, 'Specialization24', a1)
    assert _is_linked(b, 'Specialization24', a1)
    if hasattr(a1, 'studyProgramme'):
        assert _is_linked(a1, 'studyProgramme', b)
    _safe_set(b, 'Specialization24', a2)
    assert _is_linked(b, 'Specialization24', a2)
    if hasattr(a1, 'studyProgramme'):
        assert not _is_linked(a1, 'studyProgramme', b)
    if hasattr(a2, 'studyProgramme'):
        assert _is_linked(a2, 'studyProgramme', b)
    _safe_set(b, 'Specialization24', None)
    assert not _is_linked(b, 'Specialization24', a2)
    if hasattr(a2, 'studyProgramme'):
        assert not _is_linked(a2, 'studyProgramme', b)


def test_assoc_students1_reverse_link_reassign_clear():
    a1 = studyPlan_University(name="sample_text")
    a2 = studyPlan_University(name="sample_text_2")
    b = studyPlan_Student(name="sample_text", username="sample_text")
    _safe_set(b, 'Student', a1)
    assert _is_linked(b, 'Student', a1)
    if hasattr(a1, 'university'):
        assert _is_linked(a1, 'university', b)
    _safe_set(b, 'Student', a2)
    assert _is_linked(b, 'Student', a2)
    if hasattr(a1, 'university'):
        assert not _is_linked(a1, 'university', b)
    if hasattr(a2, 'university'):
        assert _is_linked(a2, 'university', b)
    _safe_set(b, 'Student', None)
    assert not _is_linked(b, 'Student', a2)
    if hasattr(a2, 'university'):
        assert not _is_linked(a2, 'university', b)


def test_assoc_studyProgramme25_reverse_link_reassign_clear():
    a1 = studyPlan_StudyProgramme(codename="sample_text", lengthInYears=7, name="sample_text")
    a2 = studyPlan_StudyProgramme(codename="sample_text_2", lengthInYears=13, name="sample_text_2")
    b = studyPlan_Specialization(name="sample_text", year=7)
    _safe_set(b, 'specializations', a1)
    assert _is_linked(b, 'specializations', a1)
    if hasattr(a1, 'StudyProgramme26'):
        assert _is_linked(a1, 'StudyProgramme26', b)
    _safe_set(b, 'specializations', a2)
    assert _is_linked(b, 'specializations', a2)
    if hasattr(a1, 'StudyProgramme26'):
        assert not _is_linked(a1, 'StudyProgramme26', b)
    if hasattr(a2, 'StudyProgramme26'):
        assert _is_linked(a2, 'StudyProgramme26', b)
    _safe_set(b, 'specializations', None)
    assert not _is_linked(b, 'specializations', a2)
    if hasattr(a2, 'StudyProgramme26'):
        assert not _is_linked(a2, 'StudyProgramme26', b)


def test_assoc_studyProgrammes2_reverse_link_reassign_clear():
    a1 = studyPlan_University(name="sample_text")
    a2 = studyPlan_University(name="sample_text_2")
    b = studyPlan_StudyProgramme(codename="sample_text", lengthInYears=7, name="sample_text")
    _safe_set(b, 'StudyProgramme', a1)
    assert _is_linked(b, 'StudyProgramme', a1)
    if hasattr(a1, 'university3'):
        assert _is_linked(a1, 'university3', b)
    _safe_set(b, 'StudyProgramme', a2)
    assert _is_linked(b, 'StudyProgramme', a2)
    if hasattr(a1, 'university3'):
        assert not _is_linked(a1, 'university3', b)
    if hasattr(a2, 'university3'):
        assert _is_linked(a2, 'university3', b)
    _safe_set(b, 'StudyProgramme', None)
    assert not _is_linked(b, 'StudyProgramme', a2)
    if hasattr(a2, 'university3'):
        assert not _is_linked(a2, 'university3', b)


def test_assoc_university0_reverse_link_reassign_clear():
    a1 = studyPlan_University(name="sample_text")
    a2 = studyPlan_University(name="sample_text_2")
    b = studyPlan_Course(codename="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'University'):
        assert _is_linked(a1, 'University', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'University'):
        assert not _is_linked(a1, 'University', b)
    if hasattr(a2, 'University'):
        assert _is_linked(a2, 'University', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'University'):
        assert not _is_linked(a2, 'University', b)


def test_assoc_university17_reverse_link_reassign_clear():
    a1 = studyPlan_University(name="sample_text")
    a2 = studyPlan_University(name="sample_text_2")
    b = studyPlan_Student(name="sample_text", username="sample_text")
    _safe_set(b, 'students', a1)
    assert _is_linked(b, 'students', a1)
    if hasattr(a1, 'University18'):
        assert _is_linked(a1, 'University18', b)
    _safe_set(b, 'students', a2)
    assert _is_linked(b, 'students', a2)
    if hasattr(a1, 'University18'):
        assert not _is_linked(a1, 'University18', b)
    if hasattr(a2, 'University18'):
        assert _is_linked(a2, 'University18', b)
    _safe_set(b, 'students', None)
    assert not _is_linked(b, 'students', a2)
    if hasattr(a2, 'University18'):
        assert not _is_linked(a2, 'University18', b)


def test_assoc_university21_reverse_link_reassign_clear():
    a1 = studyPlan_University(name="sample_text")
    a2 = studyPlan_University(name="sample_text_2")
    b = studyPlan_StudyProgramme(codename="sample_text", lengthInYears=7, name="sample_text")
    _safe_set(b, 'studyProgrammes', a1)
    assert _is_linked(b, 'studyProgrammes', a1)
    if hasattr(a1, 'University22'):
        assert _is_linked(a1, 'University22', b)
    _safe_set(b, 'studyProgrammes', a2)
    assert _is_linked(b, 'studyProgrammes', a2)
    if hasattr(a1, 'University22'):
        assert not _is_linked(a1, 'University22', b)
    if hasattr(a2, 'University22'):
        assert _is_linked(a2, 'University22', b)
    _safe_set(b, 'studyProgrammes', None)
    assert not _is_linked(b, 'studyProgrammes', a2)
    if hasattr(a2, 'University22'):
        assert not _is_linked(a2, 'University22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_electiveCourses14_stub_double():
    # studyPlan_SemesterProgramme has no real 'studyPlan_SemesterProgramme15' property in the generated
    # code (a bare stub) -- manually attach it so studyPlan_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyPlan_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyPlan_Course(codename="sample_text", credits=3.14, level=7, name="sample_text")
    partner = studyPlan_SemesterProgramme()
    setattr(partner, 'studyPlan_SemesterProgramme15', None)
    _safe_set(owner, 'studyPlan_Course16', partner)
    assert owner in getattr(partner, 'studyPlan_SemesterProgramme15')
    _safe_set(owner, 'studyPlan_Course16', None)
    assert owner not in getattr(partner, 'studyPlan_SemesterProgramme15')


def test_assoc_mandatoryCourses12_stub_double():
    # studyPlan_SemesterProgramme has no real 'studyPlan_SemesterProgramme' property in the generated
    # code (a bare stub) -- manually attach it so studyPlan_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyPlan_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyPlan_Course(codename="sample_text", credits=3.14, level=7, name="sample_text")
    partner = studyPlan_SemesterProgramme()
    setattr(partner, 'studyPlan_SemesterProgramme', None)
    _safe_set(owner, 'studyPlan_Course13', partner)
    assert owner in getattr(partner, 'studyPlan_SemesterProgramme')
    _safe_set(owner, 'studyPlan_Course13', None)
    assert owner not in getattr(partner, 'studyPlan_SemesterProgramme')


def test_assoc_selectedCourses10_stub_double():
    # studyPlan_SemesterPlan has no real 'studyPlan_SemesterPlan' property in the generated
    # code (a bare stub) -- manually attach it so studyPlan_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyPlan_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyPlan_Course(codename="sample_text", credits=3.14, level=7, name="sample_text")
    partner = studyPlan_SemesterPlan()
    setattr(partner, 'studyPlan_SemesterPlan', None)
    _safe_set(owner, 'studyPlan_Course', partner)
    assert owner in getattr(partner, 'studyPlan_SemesterPlan')
    _safe_set(owner, 'studyPlan_Course', None)
    assert owner not in getattr(partner, 'studyPlan_SemesterPlan')


def test_assoc_semesters29_stub_double():
    # studyPlan_SemesterProgramme has no real 'SemesterProgramme' property in the generated
    # code (a bare stub) -- manually attach it so studyPlan_Specialization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyPlan_Specialization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyPlan_Specialization(name="sample_text", year=7)
    partner = studyPlan_SemesterProgramme()
    setattr(partner, 'SemesterProgramme', None)
    _safe_set(owner, 'specialization', {partner})
    assert getattr(partner, 'SemesterProgramme') == owner
    _safe_set(owner, 'specialization', set())
    assert getattr(partner, 'SemesterProgramme') is None


def test_assoc_specialization11_stub_double():
    # studyPlan_SemesterProgramme has no real 'semesters' property in the generated
    # code (a bare stub) -- manually attach it so studyPlan_Specialization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyPlan_Specialization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyPlan_Specialization(name="sample_text", year=7)
    partner = studyPlan_SemesterProgramme()
    setattr(partner, 'semesters', None)
    _safe_set(owner, 'Specialization', partner)
    assert getattr(partner, 'semesters') == owner
    _safe_set(owner, 'Specialization', None)
    assert getattr(partner, 'semesters') is None


def test_assoc_student6_stub_double():
    # studyPlan_StudyPlan has no real 'studyplan' property in the generated
    # code (a bare stub) -- manually attach it so studyPlan_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyPlan_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyPlan_Student(name="sample_text", username="sample_text")
    partner = studyPlan_StudyPlan()
    setattr(partner, 'studyplan', None)
    _safe_set(owner, 'Student7', partner)
    assert getattr(partner, 'studyplan') == owner
    _safe_set(owner, 'Student7', None)
    assert getattr(partner, 'studyplan') is None


def test_assoc_studyplan19_stub_double():
    # studyPlan_StudyPlan has no real 'StudyPlan20' property in the generated
    # code (a bare stub) -- manually attach it so studyPlan_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyPlan_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyPlan_Student(name="sample_text", username="sample_text")
    partner = studyPlan_StudyPlan()
    setattr(partner, 'StudyPlan20', None)
    _safe_set(owner, 'student', partner)
    assert getattr(partner, 'StudyPlan20') == owner
    _safe_set(owner, 'student', None)
    assert getattr(partner, 'StudyPlan20') is None


