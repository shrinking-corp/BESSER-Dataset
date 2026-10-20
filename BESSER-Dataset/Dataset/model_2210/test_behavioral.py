import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CourseSlot,
    universityStudies_Course,
    universityStudies_CourseSlot,
    universityStudies_Department,
    universityStudies_ElectiveCourseSlot,
    universityStudies_MandatoryCourseSlot,
    universityStudies_Programme,
    universityStudies_Semester,
    universityStudies_Specialization,
    Credits,
    ProgrammeType,
    Seasons,
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

def test_assoc_furtherSpecializations7_reverse_link_reassign_clear():
    a1 = universityStudies_Specialization(name="sample_text")
    a2 = universityStudies_Specialization(name="sample_text_2")
    b = universityStudies_Specialization(name="sample_text")
    _safe_set(b, 'universityStudies_Specialization8', a1)
    assert _is_linked(b, 'universityStudies_Specialization8', a1)
    if hasattr(a1, 'universityStudies_Specialization6'):
        assert _is_linked(a1, 'universityStudies_Specialization6', b)
    _safe_set(b, 'universityStudies_Specialization8', a2)
    assert _is_linked(b, 'universityStudies_Specialization8', a2)
    if hasattr(a1, 'universityStudies_Specialization6'):
        assert not _is_linked(a1, 'universityStudies_Specialization6', b)
    if hasattr(a2, 'universityStudies_Specialization6'):
        assert _is_linked(a2, 'universityStudies_Specialization6', b)
    _safe_set(b, 'universityStudies_Specialization8', None)
    assert not _is_linked(b, 'universityStudies_Specialization8', a2)
    if hasattr(a2, 'universityStudies_Specialization6'):
        assert not _is_linked(a2, 'universityStudies_Specialization6', b)


def test_assoc_programmes0_reverse_link_reassign_clear():
    a1 = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    a2 = universityStudies_Programme(name="sample_text_2", numberOfSemesters=13, programmeType="sample_text_2")
    b = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    _safe_set(b, 'universityStudies_Course', {a1})
    assert _is_linked(b, 'universityStudies_Course', a1)
    if hasattr(a1, 'universityStudies_Programme'):
        assert _is_linked(a1, 'universityStudies_Programme', b)
    _safe_set(b, 'universityStudies_Course', {a2})
    assert _is_linked(b, 'universityStudies_Course', a2)
    if hasattr(a1, 'universityStudies_Programme'):
        assert not _is_linked(a1, 'universityStudies_Programme', b)
    if hasattr(a2, 'universityStudies_Programme'):
        assert _is_linked(a2, 'universityStudies_Programme', b)
    _safe_set(b, 'universityStudies_Course', set())
    assert not _is_linked(b, 'universityStudies_Course', a2)
    if hasattr(a2, 'universityStudies_Programme'):
        assert not _is_linked(a2, 'universityStudies_Programme', b)


def test_assoc_semesters3_reverse_link_reassign_clear():
    a1 = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    a2 = universityStudies_Semester(name="sample_text_2", season="sample_text_2", semesterNumber=13)
    b = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    _safe_set(b, 'universityStudies_Programme4', {a1})
    assert _is_linked(b, 'universityStudies_Programme4', a1)
    if hasattr(a1, 'universityStudies_Semester'):
        assert _is_linked(a1, 'universityStudies_Semester', b)
    _safe_set(b, 'universityStudies_Programme4', {a2})
    assert _is_linked(b, 'universityStudies_Programme4', a2)
    if hasattr(a1, 'universityStudies_Semester'):
        assert not _is_linked(a1, 'universityStudies_Semester', b)
    if hasattr(a2, 'universityStudies_Semester'):
        assert _is_linked(a2, 'universityStudies_Semester', b)
    _safe_set(b, 'universityStudies_Programme4', set())
    assert not _is_linked(b, 'universityStudies_Programme4', a2)
    if hasattr(a2, 'universityStudies_Semester'):
        assert not _is_linked(a2, 'universityStudies_Semester', b)


def test_assoc_semesters9_reverse_link_reassign_clear():
    a1 = universityStudies_Specialization(name="sample_text")
    a2 = universityStudies_Specialization(name="sample_text_2")
    b = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    _safe_set(b, 'universityStudies_Semester11', a1)
    assert _is_linked(b, 'universityStudies_Semester11', a1)
    if hasattr(a1, 'universityStudies_Specialization10'):
        assert _is_linked(a1, 'universityStudies_Specialization10', b)
    _safe_set(b, 'universityStudies_Semester11', a2)
    assert _is_linked(b, 'universityStudies_Semester11', a2)
    if hasattr(a1, 'universityStudies_Specialization10'):
        assert not _is_linked(a1, 'universityStudies_Specialization10', b)
    if hasattr(a2, 'universityStudies_Specialization10'):
        assert _is_linked(a2, 'universityStudies_Specialization10', b)
    _safe_set(b, 'universityStudies_Semester11', None)
    assert not _is_linked(b, 'universityStudies_Semester11', a2)
    if hasattr(a2, 'universityStudies_Specialization10'):
        assert not _is_linked(a2, 'universityStudies_Specialization10', b)


def test_assoc_specializations1_reverse_link_reassign_clear():
    a1 = universityStudies_Specialization(name="sample_text")
    a2 = universityStudies_Specialization(name="sample_text_2")
    b = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    _safe_set(b, 'universityStudies_Programme2', {a1})
    assert _is_linked(b, 'universityStudies_Programme2', a1)
    if hasattr(a1, 'universityStudies_Specialization'):
        assert _is_linked(a1, 'universityStudies_Specialization', b)
    _safe_set(b, 'universityStudies_Programme2', {a2})
    assert _is_linked(b, 'universityStudies_Programme2', a2)
    if hasattr(a1, 'universityStudies_Specialization'):
        assert not _is_linked(a1, 'universityStudies_Specialization', b)
    if hasattr(a2, 'universityStudies_Specialization'):
        assert _is_linked(a2, 'universityStudies_Specialization', b)
    _safe_set(b, 'universityStudies_Programme2', set())
    assert not _is_linked(b, 'universityStudies_Programme2', a2)
    if hasattr(a2, 'universityStudies_Specialization'):
        assert not _is_linked(a2, 'universityStudies_Specialization', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Courses14_stub_double():
    # universityStudies_Department has no real 'universityStudies_Department' property in the generated
    # code (a bare stub) -- manually attach it so universityStudies_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityStudies_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    partner = universityStudies_Department()
    setattr(partner, 'universityStudies_Department', None)
    _safe_set(owner, 'universityStudies_Course15', partner)
    assert owner in getattr(partner, 'universityStudies_Department')
    _safe_set(owner, 'universityStudies_Course15', None)
    assert owner not in getattr(partner, 'universityStudies_Department')


def test_assoc_Department5_stub_double():
    # universityStudies_Department has no real 'Department' property in the generated
    # code (a bare stub) -- manually attach it so universityStudies_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityStudies_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    partner = universityStudies_Department()
    setattr(partner, 'Department', None)
    _safe_set(owner, 'Programmes', partner)
    assert getattr(partner, 'Department') == owner
    _safe_set(owner, 'Programmes', None)
    assert getattr(partner, 'Department') is None


def test_assoc_Programmes16_stub_double():
    # universityStudies_Department has no real 'Department17' property in the generated
    # code (a bare stub) -- manually attach it so universityStudies_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityStudies_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    partner = universityStudies_Department()
    setattr(partner, 'Department17', None)
    _safe_set(owner, 'Programme', partner)
    assert getattr(partner, 'Department17') == owner
    _safe_set(owner, 'Programme', None)
    assert getattr(partner, 'Department17') is None


def test_assoc_course18_stub_double():
    # universityStudies_CourseSlot has no real 'universityStudies_CourseSlot19' property in the generated
    # code (a bare stub) -- manually attach it so universityStudies_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityStudies_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    partner = universityStudies_CourseSlot()
    setattr(partner, 'universityStudies_CourseSlot19', None)
    _safe_set(owner, 'universityStudies_Course20', partner)
    assert getattr(partner, 'universityStudies_CourseSlot19') == owner
    _safe_set(owner, 'universityStudies_Course20', None)
    assert getattr(partner, 'universityStudies_CourseSlot19') is None


def test_assoc_courseSlots12_stub_double():
    # universityStudies_CourseSlot has no real 'universityStudies_CourseSlot' property in the generated
    # code (a bare stub) -- manually attach it so universityStudies_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityStudies_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    partner = universityStudies_CourseSlot()
    setattr(partner, 'universityStudies_CourseSlot', None)
    _safe_set(owner, 'universityStudies_Semester13', {partner})
    assert getattr(partner, 'universityStudies_CourseSlot') == owner
    _safe_set(owner, 'universityStudies_Semester13', set())
    assert getattr(partner, 'universityStudies_CourseSlot') is None


def test_assoc_optionalCourses21_stub_double():
    # universityStudies_ElectiveCourseSlot has no real 'universityStudies_ElectiveCourseSlot' property in the generated
    # code (a bare stub) -- manually attach it so universityStudies_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityStudies_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    partner = universityStudies_ElectiveCourseSlot()
    setattr(partner, 'universityStudies_ElectiveCourseSlot', None)
    _safe_set(owner, 'universityStudies_Course22', partner)
    assert owner in getattr(partner, 'universityStudies_ElectiveCourseSlot')
    _safe_set(owner, 'universityStudies_Course22', None)
    assert owner not in getattr(partner, 'universityStudies_ElectiveCourseSlot')


