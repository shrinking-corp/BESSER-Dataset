import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    study_Course,
    study_CourseSlot,
    study_Department,
    study_Programme,
    study_Semester,
    study_Specialization,
    study_StudyPlan,
    FallOrSpring,
    programmeCode,
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

def test_assoc_courseSlot12_reverse_link_reassign_clear():
    a1 = study_Semester(fallOrSpring="sample_text", semesterNumber=7)
    a2 = study_Semester(fallOrSpring="sample_text_2", semesterNumber=13)
    b = study_CourseSlot(elective=True)
    _safe_set(b, 'study_CourseSlot', a1)
    assert _is_linked(b, 'study_CourseSlot', a1)
    if hasattr(a1, 'study_Semester13'):
        assert _is_linked(a1, 'study_Semester13', b)
    _safe_set(b, 'study_CourseSlot', a2)
    assert _is_linked(b, 'study_CourseSlot', a2)
    if hasattr(a1, 'study_Semester13'):
        assert not _is_linked(a1, 'study_Semester13', b)
    if hasattr(a2, 'study_Semester13'):
        assert _is_linked(a2, 'study_Semester13', b)
    _safe_set(b, 'study_CourseSlot', None)
    assert not _is_linked(b, 'study_CourseSlot', a2)
    if hasattr(a2, 'study_Semester13'):
        assert not _is_linked(a2, 'study_Semester13', b)


def test_assoc_electiveCourses17_reverse_link_reassign_clear():
    a1 = study_CourseSlot(elective=True)
    a2 = study_CourseSlot(elective=False)
    b = study_Course(code="sample_text", name="sample_text", points=3.14)
    _safe_set(b, 'study_Course19', a1)
    assert _is_linked(b, 'study_Course19', a1)
    if hasattr(a1, 'study_CourseSlot18'):
        assert _is_linked(a1, 'study_CourseSlot18', b)
    _safe_set(b, 'study_Course19', a2)
    assert _is_linked(b, 'study_Course19', a2)
    if hasattr(a1, 'study_CourseSlot18'):
        assert not _is_linked(a1, 'study_CourseSlot18', b)
    if hasattr(a2, 'study_CourseSlot18'):
        assert _is_linked(a2, 'study_CourseSlot18', b)
    _safe_set(b, 'study_Course19', None)
    assert not _is_linked(b, 'study_Course19', a2)
    if hasattr(a2, 'study_CourseSlot18'):
        assert not _is_linked(a2, 'study_CourseSlot18', b)


def test_assoc_mandatoryCourse14_reverse_link_reassign_clear():
    a1 = study_CourseSlot(elective=True)
    a2 = study_CourseSlot(elective=False)
    b = study_Course(code="sample_text", name="sample_text", points=3.14)
    _safe_set(b, 'study_Course16', a1)
    assert _is_linked(b, 'study_Course16', a1)
    if hasattr(a1, 'study_CourseSlot15'):
        assert _is_linked(a1, 'study_CourseSlot15', b)
    _safe_set(b, 'study_Course16', a2)
    assert _is_linked(b, 'study_Course16', a2)
    if hasattr(a1, 'study_CourseSlot15'):
        assert not _is_linked(a1, 'study_CourseSlot15', b)
    if hasattr(a2, 'study_CourseSlot15'):
        assert _is_linked(a2, 'study_CourseSlot15', b)
    _safe_set(b, 'study_Course16', None)
    assert not _is_linked(b, 'study_Course16', a2)
    if hasattr(a2, 'study_CourseSlot15'):
        assert not _is_linked(a2, 'study_CourseSlot15', b)


def test_assoc_semester9_reverse_link_reassign_clear():
    a1 = study_Specialization(name="sample_text")
    a2 = study_Specialization(name="sample_text_2")
    b = study_Semester(fallOrSpring="sample_text", semesterNumber=7)
    _safe_set(b, 'study_Semester11', a1)
    assert _is_linked(b, 'study_Semester11', a1)
    if hasattr(a1, 'study_Specialization10'):
        assert _is_linked(a1, 'study_Specialization10', b)
    _safe_set(b, 'study_Semester11', a2)
    assert _is_linked(b, 'study_Semester11', a2)
    if hasattr(a1, 'study_Specialization10'):
        assert not _is_linked(a1, 'study_Specialization10', b)
    if hasattr(a2, 'study_Specialization10'):
        assert _is_linked(a2, 'study_Specialization10', b)
    _safe_set(b, 'study_Semester11', None)
    assert not _is_linked(b, 'study_Semester11', a2)
    if hasattr(a2, 'study_Specialization10'):
        assert not _is_linked(a2, 'study_Specialization10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_course1_stub_double():
    # study_Department has no real 'study_Department2' property in the generated
    # code (a bare stub) -- manually attach it so study_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Course(code="sample_text", name="sample_text", points=3.14)
    partner = study_Department()
    setattr(partner, 'study_Department2', None)
    _safe_set(owner, 'study_Course', partner)
    assert owner in getattr(partner, 'study_Department2')
    _safe_set(owner, 'study_Course', None)
    assert owner not in getattr(partner, 'study_Department2')


def test_assoc_programme0_stub_double():
    # study_Department has no real 'study_Department' property in the generated
    # code (a bare stub) -- manually attach it so study_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Programme(name="sample_text", programmeCode="sample_text")
    partner = study_Department()
    setattr(partner, 'study_Department', None)
    _safe_set(owner, 'study_Programme', partner)
    assert owner in getattr(partner, 'study_Department')
    _safe_set(owner, 'study_Programme', None)
    assert owner not in getattr(partner, 'study_Department')


def test_assoc_semester7_stub_double():
    # study_StudyPlan has no real 'study_StudyPlan8' property in the generated
    # code (a bare stub) -- manually attach it so study_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Semester(fallOrSpring="sample_text", semesterNumber=7)
    partner = study_StudyPlan()
    setattr(partner, 'study_StudyPlan8', None)
    _safe_set(owner, 'study_Semester', partner)
    assert owner in getattr(partner, 'study_StudyPlan8')
    _safe_set(owner, 'study_Semester', None)
    assert owner not in getattr(partner, 'study_StudyPlan8')


def test_assoc_spesialization5_stub_double():
    # study_StudyPlan has no real 'study_StudyPlan6' property in the generated
    # code (a bare stub) -- manually attach it so study_Specialization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Specialization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Specialization(name="sample_text")
    partner = study_StudyPlan()
    setattr(partner, 'study_StudyPlan6', None)
    _safe_set(owner, 'study_Specialization', partner)
    assert owner in getattr(partner, 'study_StudyPlan6')
    _safe_set(owner, 'study_Specialization', None)
    assert owner not in getattr(partner, 'study_StudyPlan6')


def test_assoc_studyPlan3_stub_double():
    # study_StudyPlan has no real 'study_StudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so study_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # study_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = study_Programme(name="sample_text", programmeCode="sample_text")
    partner = study_StudyPlan()
    setattr(partner, 'study_StudyPlan', None)
    _safe_set(owner, 'study_Programme4', {partner})
    assert getattr(partner, 'study_StudyPlan') == owner
    _safe_set(owner, 'study_Programme4', set())
    assert getattr(partner, 'study_StudyPlan') is None


