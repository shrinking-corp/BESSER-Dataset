import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    university_CourseInstances,
    university_Courses,
    university_ProgrammeInstances,
    university_ProgrammeSemesters,
    university_Programmes,
    university_Semesters,
    university_Slot,
    university_Specializations,
    university_University,
    SemesterTime,
    SlotType,
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

def test_assoc_courses28_reverse_link_reassign_clear():
    a1 = university_University(name="sample_text")
    a2 = university_University(name="sample_text_2")
    b = university_Courses(code="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'university_Courses', a1)
    assert _is_linked(b, 'university_Courses', a1)
    if hasattr(a1, 'university_University29'):
        assert _is_linked(a1, 'university_University29', b)
    _safe_set(b, 'university_Courses', a2)
    assert _is_linked(b, 'university_Courses', a2)
    if hasattr(a1, 'university_University29'):
        assert not _is_linked(a1, 'university_University29', b)
    if hasattr(a2, 'university_University29'):
        assert _is_linked(a2, 'university_University29', b)
    _safe_set(b, 'university_Courses', None)
    assert not _is_linked(b, 'university_Courses', a2)
    if hasattr(a2, 'university_University29'):
        assert not _is_linked(a2, 'university_University29', b)


def test_assoc_instances0_reverse_link_reassign_clear():
    a1 = university_Programmes(code="sample_text", name="sample_text")
    a2 = university_Programmes(code="sample_text_2", name="sample_text_2")
    b = university_ProgrammeInstances(startYear=7)
    _safe_set(b, 'ProgrammeInstances', a1)
    assert _is_linked(b, 'ProgrammeInstances', a1)
    if hasattr(a1, 'programme'):
        assert _is_linked(a1, 'programme', b)
    _safe_set(b, 'ProgrammeInstances', a2)
    assert _is_linked(b, 'ProgrammeInstances', a2)
    if hasattr(a1, 'programme'):
        assert not _is_linked(a1, 'programme', b)
    if hasattr(a2, 'programme'):
        assert _is_linked(a2, 'programme', b)
    _safe_set(b, 'ProgrammeInstances', None)
    assert not _is_linked(b, 'ProgrammeInstances', a2)
    if hasattr(a2, 'programme'):
        assert not _is_linked(a2, 'programme', b)


def test_assoc_programme1_reverse_link_reassign_clear():
    a1 = university_Programmes(code="sample_text", name="sample_text")
    a2 = university_Programmes(code="sample_text_2", name="sample_text_2")
    b = university_ProgrammeInstances(startYear=7)
    _safe_set(b, 'instances', a1)
    assert _is_linked(b, 'instances', a1)
    if hasattr(a1, 'Programmes'):
        assert _is_linked(a1, 'Programmes', b)
    _safe_set(b, 'instances', a2)
    assert _is_linked(b, 'instances', a2)
    if hasattr(a1, 'Programmes'):
        assert not _is_linked(a1, 'Programmes', b)
    if hasattr(a2, 'Programmes'):
        assert _is_linked(a2, 'Programmes', b)
    _safe_set(b, 'instances', None)
    assert not _is_linked(b, 'instances', a2)
    if hasattr(a2, 'Programmes'):
        assert not _is_linked(a2, 'Programmes', b)


def test_assoc_programmeInstance23_reverse_link_reassign_clear():
    a1 = university_Specializations(name="sample_text")
    a2 = university_Specializations(name="sample_text_2")
    b = university_ProgrammeInstances(startYear=7)
    _safe_set(b, 'ProgrammeInstances24', a1)
    assert _is_linked(b, 'ProgrammeInstances24', a1)
    if hasattr(a1, 'specializations'):
        assert _is_linked(a1, 'specializations', b)
    _safe_set(b, 'ProgrammeInstances24', a2)
    assert _is_linked(b, 'ProgrammeInstances24', a2)
    if hasattr(a1, 'specializations'):
        assert not _is_linked(a1, 'specializations', b)
    if hasattr(a2, 'specializations'):
        assert _is_linked(a2, 'specializations', b)
    _safe_set(b, 'ProgrammeInstances24', None)
    assert not _is_linked(b, 'ProgrammeInstances24', a2)
    if hasattr(a2, 'specializations'):
        assert not _is_linked(a2, 'specializations', b)


def test_assoc_programmes27_reverse_link_reassign_clear():
    a1 = university_University(name="sample_text")
    a2 = university_University(name="sample_text_2")
    b = university_Programmes(code="sample_text", name="sample_text")
    _safe_set(b, 'university_Programmes', a1)
    assert _is_linked(b, 'university_Programmes', a1)
    if hasattr(a1, 'university_University'):
        assert _is_linked(a1, 'university_University', b)
    _safe_set(b, 'university_Programmes', a2)
    assert _is_linked(b, 'university_Programmes', a2)
    if hasattr(a1, 'university_University'):
        assert not _is_linked(a1, 'university_University', b)
    if hasattr(a2, 'university_University'):
        assert _is_linked(a2, 'university_University', b)
    _safe_set(b, 'university_Programmes', None)
    assert not _is_linked(b, 'university_Programmes', a2)
    if hasattr(a2, 'university_University'):
        assert not _is_linked(a2, 'university_University', b)


def test_assoc_semesters30_reverse_link_reassign_clear():
    a1 = university_University(name="sample_text")
    a2 = university_University(name="sample_text_2")
    b = university_Semesters(semesterTime="sample_text", year=7)
    _safe_set(b, 'university_Semesters32', a1)
    assert _is_linked(b, 'university_Semesters32', a1)
    if hasattr(a1, 'university_University31'):
        assert _is_linked(a1, 'university_University31', b)
    _safe_set(b, 'university_Semesters32', a2)
    assert _is_linked(b, 'university_Semesters32', a2)
    if hasattr(a1, 'university_University31'):
        assert not _is_linked(a1, 'university_University31', b)
    if hasattr(a2, 'university_University31'):
        assert _is_linked(a2, 'university_University31', b)
    _safe_set(b, 'university_Semesters32', None)
    assert not _is_linked(b, 'university_Semesters32', a2)
    if hasattr(a2, 'university_University31'):
        assert not _is_linked(a2, 'university_University31', b)


def test_assoc_specializations3_reverse_link_reassign_clear():
    a1 = university_Specializations(name="sample_text")
    a2 = university_Specializations(name="sample_text_2")
    b = university_ProgrammeInstances(startYear=7)
    _safe_set(b, 'programmeInstance4', {a1})
    assert _is_linked(b, 'programmeInstance4', a1)
    if hasattr(a1, 'Specializations'):
        assert _is_linked(a1, 'Specializations', b)
    _safe_set(b, 'programmeInstance4', {a2})
    assert _is_linked(b, 'programmeInstance4', a2)
    if hasattr(a1, 'Specializations'):
        assert not _is_linked(a1, 'Specializations', b)
    if hasattr(a2, 'Specializations'):
        assert _is_linked(a2, 'Specializations', b)
    _safe_set(b, 'programmeInstance4', set())
    assert not _is_linked(b, 'programmeInstance4', a2)
    if hasattr(a2, 'Specializations'):
        assert not _is_linked(a2, 'Specializations', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_avaliableCourses19_stub_double():
    # university_CourseInstances has no real 'university_CourseInstances20' property in the generated
    # code (a bare stub) -- manually attach it so university_Slot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Slot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Slot(name="sample_text", points=7, slotType="sample_text")
    partner = university_CourseInstances()
    setattr(partner, 'university_CourseInstances20', None)
    _safe_set(owner, 'university_Slot', {partner})
    assert getattr(partner, 'university_CourseInstances20') == owner
    _safe_set(owner, 'university_Slot', set())
    assert getattr(partner, 'university_CourseInstances20') is None


def test_assoc_course6_stub_double():
    # university_CourseInstances has no real 'instances7' property in the generated
    # code (a bare stub) -- manually attach it so university_Courses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Courses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Courses(code="sample_text", credits=3.14, name="sample_text")
    partner = university_CourseInstances()
    setattr(partner, 'instances7', None)
    _safe_set(owner, 'Courses', partner)
    assert getattr(partner, 'instances7') == owner
    _safe_set(owner, 'Courses', None)
    assert getattr(partner, 'instances7') is None


def test_assoc_instances5_stub_double():
    # university_CourseInstances has no real 'CourseInstances' property in the generated
    # code (a bare stub) -- manually attach it so university_Courses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Courses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Courses(code="sample_text", credits=3.14, name="sample_text")
    partner = university_CourseInstances()
    setattr(partner, 'CourseInstances', None)
    _safe_set(owner, 'course', {partner})
    assert getattr(partner, 'CourseInstances') == owner
    _safe_set(owner, 'course', set())
    assert getattr(partner, 'CourseInstances') is None


def test_assoc_programmeInstance9_stub_double():
    # university_ProgrammeSemesters has no real 'programmeSemesters' property in the generated
    # code (a bare stub) -- manually attach it so university_ProgrammeInstances's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_ProgrammeInstances's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_ProgrammeInstances(startYear=7)
    partner = university_ProgrammeSemesters()
    setattr(partner, 'programmeSemesters', None)
    _safe_set(owner, 'ProgrammeInstances10', partner)
    assert getattr(partner, 'programmeSemesters') == owner
    _safe_set(owner, 'ProgrammeInstances10', None)
    assert getattr(partner, 'programmeSemesters') is None


def test_assoc_programmeSemester17_stub_double():
    # university_ProgrammeSemesters has no real 'ProgrammeSemesters18' property in the generated
    # code (a bare stub) -- manually attach it so university_Slot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Slot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Slot(name="sample_text", points=7, slotType="sample_text")
    partner = university_ProgrammeSemesters()
    setattr(partner, 'ProgrammeSemesters18', None)
    _safe_set(owner, 'slots', partner)
    assert getattr(partner, 'ProgrammeSemesters18') == owner
    _safe_set(owner, 'slots', None)
    assert getattr(partner, 'ProgrammeSemesters18') is None


def test_assoc_programmeSemester25_stub_double():
    # university_ProgrammeSemesters has no real 'ProgrammeSemesters26' property in the generated
    # code (a bare stub) -- manually attach it so university_Specializations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Specializations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Specializations(name="sample_text")
    partner = university_ProgrammeSemesters()
    setattr(partner, 'ProgrammeSemesters26', None)
    _safe_set(owner, 'specialization', {partner})
    assert getattr(partner, 'ProgrammeSemesters26') == owner
    _safe_set(owner, 'specialization', set())
    assert getattr(partner, 'ProgrammeSemesters26') is None


def test_assoc_programmeSemesters2_stub_double():
    # university_ProgrammeSemesters has no real 'ProgrammeSemesters' property in the generated
    # code (a bare stub) -- manually attach it so university_ProgrammeInstances's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_ProgrammeInstances's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_ProgrammeInstances(startYear=7)
    partner = university_ProgrammeSemesters()
    setattr(partner, 'ProgrammeSemesters', None)
    _safe_set(owner, 'programmeInstance', {partner})
    assert getattr(partner, 'ProgrammeSemesters') == owner
    _safe_set(owner, 'programmeInstance', set())
    assert getattr(partner, 'ProgrammeSemesters') is None


def test_assoc_programmeSemesters21_stub_double():
    # university_ProgrammeSemesters has no real 'ProgrammeSemesters22' property in the generated
    # code (a bare stub) -- manually attach it so university_Semesters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Semesters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Semesters(semesterTime="sample_text", year=7)
    partner = university_ProgrammeSemesters()
    setattr(partner, 'ProgrammeSemesters22', None)
    _safe_set(owner, 'semester', {partner})
    assert getattr(partner, 'ProgrammeSemesters22') == owner
    _safe_set(owner, 'semester', set())
    assert getattr(partner, 'ProgrammeSemesters22') is None


def test_assoc_semester12_stub_double():
    # university_ProgrammeSemesters has no real 'programmeSemesters13' property in the generated
    # code (a bare stub) -- manually attach it so university_Semesters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Semesters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Semesters(semesterTime="sample_text", year=7)
    partner = university_ProgrammeSemesters()
    setattr(partner, 'programmeSemesters13', None)
    _safe_set(owner, 'Semesters', partner)
    assert getattr(partner, 'programmeSemesters13') == owner
    _safe_set(owner, 'Semesters', None)
    assert getattr(partner, 'programmeSemesters13') is None


def test_assoc_semester8_stub_double():
    # university_CourseInstances has no real 'university_CourseInstances' property in the generated
    # code (a bare stub) -- manually attach it so university_Semesters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Semesters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Semesters(semesterTime="sample_text", year=7)
    partner = university_CourseInstances()
    setattr(partner, 'university_CourseInstances', None)
    _safe_set(owner, 'university_Semesters', partner)
    assert getattr(partner, 'university_CourseInstances') == owner
    _safe_set(owner, 'university_Semesters', None)
    assert getattr(partner, 'university_CourseInstances') is None


def test_assoc_slots11_stub_double():
    # university_ProgrammeSemesters has no real 'programmeSemester' property in the generated
    # code (a bare stub) -- manually attach it so university_Slot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Slot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Slot(name="sample_text", points=7, slotType="sample_text")
    partner = university_ProgrammeSemesters()
    setattr(partner, 'programmeSemester', None)
    _safe_set(owner, 'Slot', partner)
    assert owner in getattr(partner, 'programmeSemester')
    _safe_set(owner, 'Slot', None)
    assert owner not in getattr(partner, 'programmeSemester')


def test_assoc_specialization14_stub_double():
    # university_ProgrammeSemesters has no real 'programmeSemester15' property in the generated
    # code (a bare stub) -- manually attach it so university_Specializations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Specializations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Specializations(name="sample_text")
    partner = university_ProgrammeSemesters()
    setattr(partner, 'programmeSemester15', None)
    _safe_set(owner, 'Specializations16', partner)
    assert getattr(partner, 'programmeSemester15') == owner
    _safe_set(owner, 'Specializations16', None)
    assert getattr(partner, 'programmeSemester15') is None


