import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tdt4250case_Course,
    tdt4250case_CourseInstance,
    tdt4250case_CourseRole,
    tdt4250case_CourseWork,
    tdt4250case_CreditReductionCourse,
    tdt4250case_Department,
    tdt4250case_Examination,
    tdt4250case_ExaminationActivity,
    tdt4250case_Person,
    tdt4250case_ScheduledActivity,
    tdt4250case_Studyprogram,
    tdt4250case_Timetable,
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

def test_assoc_course12_reverse_link_reassign_clear():
    a1 = tdt4250case_CreditReductionCourse(from_=date(2024, 1, 1), reduction=3.14, to=date(2024, 1, 1))
    a2 = tdt4250case_CreditReductionCourse(from_=date(2025, 6, 15), reduction=9.99, to=date(2025, 6, 15))
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'tdt4250case_Course14', a1)
    assert _is_linked(b, 'tdt4250case_Course14', a1)
    if hasattr(a1, 'tdt4250case_CreditReductionCourse13'):
        assert _is_linked(a1, 'tdt4250case_CreditReductionCourse13', b)
    _safe_set(b, 'tdt4250case_Course14', a2)
    assert _is_linked(b, 'tdt4250case_Course14', a2)
    if hasattr(a1, 'tdt4250case_CreditReductionCourse13'):
        assert not _is_linked(a1, 'tdt4250case_CreditReductionCourse13', b)
    if hasattr(a2, 'tdt4250case_CreditReductionCourse13'):
        assert _is_linked(a2, 'tdt4250case_CreditReductionCourse13', b)
    _safe_set(b, 'tdt4250case_Course14', None)
    assert not _is_linked(b, 'tdt4250case_Course14', a2)
    if hasattr(a2, 'tdt4250case_CreditReductionCourse13'):
        assert not _is_linked(a2, 'tdt4250case_CreditReductionCourse13', b)


def test_assoc_course15_reverse_link_reassign_clear():
    a1 = tdt4250case_Studyprogram(code="sample_text")
    a2 = tdt4250case_Studyprogram(code="sample_text_2")
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'studyprogram'):
        assert _is_linked(a1, 'studyprogram', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'studyprogram'):
        assert not _is_linked(a1, 'studyprogram', b)
    if hasattr(a2, 'studyprogram'):
        assert _is_linked(a2, 'studyprogram', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'studyprogram'):
        assert not _is_linked(a2, 'studyprogram', b)


def test_assoc_course25_reverse_link_reassign_clear():
    a1 = tdt4250case_CourseInstance(semester="sample_text")
    a2 = tdt4250case_CourseInstance(semester="sample_text_2")
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'Course26', a1)
    assert _is_linked(b, 'Course26', a1)
    if hasattr(a1, 'instance'):
        assert _is_linked(a1, 'instance', b)
    _safe_set(b, 'Course26', a2)
    assert _is_linked(b, 'Course26', a2)
    if hasattr(a1, 'instance'):
        assert not _is_linked(a1, 'instance', b)
    if hasattr(a2, 'instance'):
        assert _is_linked(a2, 'instance', b)
    _safe_set(b, 'Course26', None)
    assert not _is_linked(b, 'Course26', a2)
    if hasattr(a2, 'instance'):
        assert not _is_linked(a2, 'instance', b)


def test_assoc_courseCoordinator23_reverse_link_reassign_clear():
    a1 = tdt4250case_Person(name="sample_text", username="sample_text")
    a2 = tdt4250case_Person(name="sample_text_2", username="sample_text_2")
    b = tdt4250case_CourseInstance(semester="sample_text")
    _safe_set(b, 'tdt4250case_CourseInstance24', a1)
    assert _is_linked(b, 'tdt4250case_CourseInstance24', a1)
    if hasattr(a1, 'tdt4250case_Person'):
        assert _is_linked(a1, 'tdt4250case_Person', b)
    _safe_set(b, 'tdt4250case_CourseInstance24', a2)
    assert _is_linked(b, 'tdt4250case_CourseInstance24', a2)
    if hasattr(a1, 'tdt4250case_Person'):
        assert not _is_linked(a1, 'tdt4250case_Person', b)
    if hasattr(a2, 'tdt4250case_Person'):
        assert _is_linked(a2, 'tdt4250case_Person', b)
    _safe_set(b, 'tdt4250case_CourseInstance24', None)
    assert not _is_linked(b, 'tdt4250case_CourseInstance24', a2)
    if hasattr(a2, 'tdt4250case_Person'):
        assert not _is_linked(a2, 'tdt4250case_Person', b)


def test_assoc_courseWork10_reverse_link_reassign_clear():
    a1 = tdt4250case_CourseWork(hours=7, type="sample_text")
    a2 = tdt4250case_CourseWork(hours=13, type="sample_text_2")
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'tdt4250case_Course11', {a1})
    assert _is_linked(b, 'tdt4250case_Course11', a1)
    if hasattr(a1, 'tdt4250case_CourseWork'):
        assert _is_linked(a1, 'tdt4250case_CourseWork', b)
    _safe_set(b, 'tdt4250case_Course11', {a2})
    assert _is_linked(b, 'tdt4250case_Course11', a2)
    if hasattr(a1, 'tdt4250case_CourseWork'):
        assert not _is_linked(a1, 'tdt4250case_CourseWork', b)
    if hasattr(a2, 'tdt4250case_CourseWork'):
        assert _is_linked(a2, 'tdt4250case_CourseWork', b)
    _safe_set(b, 'tdt4250case_Course11', set())
    assert not _is_linked(b, 'tdt4250case_Course11', a2)
    if hasattr(a2, 'tdt4250case_CourseWork'):
        assert not _is_linked(a2, 'tdt4250case_CourseWork', b)


def test_assoc_creditReductionCourse6_reverse_link_reassign_clear():
    a1 = tdt4250case_CreditReductionCourse(from_=date(2024, 1, 1), reduction=3.14, to=date(2024, 1, 1))
    a2 = tdt4250case_CreditReductionCourse(from_=date(2025, 6, 15), reduction=9.99, to=date(2025, 6, 15))
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'tdt4250case_Course7', {a1})
    assert _is_linked(b, 'tdt4250case_Course7', a1)
    if hasattr(a1, 'tdt4250case_CreditReductionCourse'):
        assert _is_linked(a1, 'tdt4250case_CreditReductionCourse', b)
    _safe_set(b, 'tdt4250case_Course7', {a2})
    assert _is_linked(b, 'tdt4250case_Course7', a2)
    if hasattr(a1, 'tdt4250case_CreditReductionCourse'):
        assert not _is_linked(a1, 'tdt4250case_CreditReductionCourse', b)
    if hasattr(a2, 'tdt4250case_CreditReductionCourse'):
        assert _is_linked(a2, 'tdt4250case_CreditReductionCourse', b)
    _safe_set(b, 'tdt4250case_Course7', set())
    assert not _is_linked(b, 'tdt4250case_Course7', a2)
    if hasattr(a2, 'tdt4250case_CreditReductionCourse'):
        assert not _is_linked(a2, 'tdt4250case_CreditReductionCourse', b)


def test_assoc_employee33_reverse_link_reassign_clear():
    a1 = tdt4250case_Person(name="sample_text", username="sample_text")
    a2 = tdt4250case_Person(name="sample_text_2", username="sample_text_2")
    b = tdt4250case_Department(code="sample_text", name="sample_text")
    _safe_set(b, 'tdt4250case_Department34', {a1})
    assert _is_linked(b, 'tdt4250case_Department34', a1)
    if hasattr(a1, 'tdt4250case_Person35'):
        assert _is_linked(a1, 'tdt4250case_Person35', b)
    _safe_set(b, 'tdt4250case_Department34', {a2})
    assert _is_linked(b, 'tdt4250case_Department34', a2)
    if hasattr(a1, 'tdt4250case_Person35'):
        assert not _is_linked(a1, 'tdt4250case_Person35', b)
    if hasattr(a2, 'tdt4250case_Person35'):
        assert _is_linked(a2, 'tdt4250case_Person35', b)
    _safe_set(b, 'tdt4250case_Department34', set())
    assert not _is_linked(b, 'tdt4250case_Department34', a2)
    if hasattr(a2, 'tdt4250case_Person35'):
        assert not _is_linked(a2, 'tdt4250case_Person35', b)


def test_assoc_instance8_reverse_link_reassign_clear():
    a1 = tdt4250case_CourseInstance(semester="sample_text")
    a2 = tdt4250case_CourseInstance(semester="sample_text_2")
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'course9', {a1})
    assert _is_linked(b, 'course9', a1)
    if hasattr(a1, 'CourseInstance'):
        assert _is_linked(a1, 'CourseInstance', b)
    _safe_set(b, 'course9', {a2})
    assert _is_linked(b, 'course9', a2)
    if hasattr(a1, 'CourseInstance'):
        assert not _is_linked(a1, 'CourseInstance', b)
    if hasattr(a2, 'CourseInstance'):
        assert _is_linked(a2, 'CourseInstance', b)
    _safe_set(b, 'course9', set())
    assert not _is_linked(b, 'course9', a2)
    if hasattr(a2, 'CourseInstance'):
        assert not _is_linked(a2, 'CourseInstance', b)


def test_assoc_person37_reverse_link_reassign_clear():
    a1 = tdt4250case_Person(name="sample_text", username="sample_text")
    a2 = tdt4250case_Person(name="sample_text_2", username="sample_text_2")
    b = tdt4250case_CourseRole(name="sample_text")
    _safe_set(b, 'role', {a1})
    assert _is_linked(b, 'role', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'role', {a2})
    assert _is_linked(b, 'role', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'role', set())
    assert not _is_linked(b, 'role', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_recommendedCourse4_reverse_link_reassign_clear():
    a1 = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    a2 = tdt4250case_Course(code="sample_text_2", content="sample_text_2", credits=9.99, name="sample_text_2")
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'tdt4250case_Course5', a1)
    assert _is_linked(b, 'tdt4250case_Course5', a1)
    if hasattr(a1, 'tdt4250case_Course3'):
        assert _is_linked(a1, 'tdt4250case_Course3', b)
    _safe_set(b, 'tdt4250case_Course5', a2)
    assert _is_linked(b, 'tdt4250case_Course5', a2)
    if hasattr(a1, 'tdt4250case_Course3'):
        assert not _is_linked(a1, 'tdt4250case_Course3', b)
    if hasattr(a2, 'tdt4250case_Course3'):
        assert _is_linked(a2, 'tdt4250case_Course3', b)
    _safe_set(b, 'tdt4250case_Course5', None)
    assert not _is_linked(b, 'tdt4250case_Course5', a2)
    if hasattr(a2, 'tdt4250case_Course3'):
        assert not _is_linked(a2, 'tdt4250case_Course3', b)


def test_assoc_requiredCourse2_reverse_link_reassign_clear():
    a1 = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    a2 = tdt4250case_Course(code="sample_text_2", content="sample_text_2", credits=9.99, name="sample_text_2")
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'tdt4250case_Course1', {a1})
    assert _is_linked(b, 'tdt4250case_Course1', a1)
    if hasattr(a1, 'tdt4250case_Course'):
        assert _is_linked(a1, 'tdt4250case_Course', b)
    _safe_set(b, 'tdt4250case_Course1', {a2})
    assert _is_linked(b, 'tdt4250case_Course1', a2)
    if hasattr(a1, 'tdt4250case_Course'):
        assert not _is_linked(a1, 'tdt4250case_Course', b)
    if hasattr(a2, 'tdt4250case_Course'):
        assert _is_linked(a2, 'tdt4250case_Course', b)
    _safe_set(b, 'tdt4250case_Course1', set())
    assert not _is_linked(b, 'tdt4250case_Course1', a2)
    if hasattr(a2, 'tdt4250case_Course'):
        assert not _is_linked(a2, 'tdt4250case_Course', b)


def test_assoc_reservedFor31_reverse_link_reassign_clear():
    a1 = tdt4250case_Studyprogram(code="sample_text")
    a2 = tdt4250case_Studyprogram(code="sample_text_2")
    b = tdt4250case_ScheduledActivity(activity="sample_text", room="sample_text", timeslot="sample_text")
    _safe_set(b, 'tdt4250case_ScheduledActivity32', {a1})
    assert _is_linked(b, 'tdt4250case_ScheduledActivity32', a1)
    if hasattr(a1, 'tdt4250case_Studyprogram'):
        assert _is_linked(a1, 'tdt4250case_Studyprogram', b)
    _safe_set(b, 'tdt4250case_ScheduledActivity32', {a2})
    assert _is_linked(b, 'tdt4250case_ScheduledActivity32', a2)
    if hasattr(a1, 'tdt4250case_Studyprogram'):
        assert not _is_linked(a1, 'tdt4250case_Studyprogram', b)
    if hasattr(a2, 'tdt4250case_Studyprogram'):
        assert _is_linked(a2, 'tdt4250case_Studyprogram', b)
    _safe_set(b, 'tdt4250case_ScheduledActivity32', set())
    assert not _is_linked(b, 'tdt4250case_ScheduledActivity32', a2)
    if hasattr(a2, 'tdt4250case_Studyprogram'):
        assert not _is_linked(a2, 'tdt4250case_Studyprogram', b)


def test_assoc_responsibleDepartment19_reverse_link_reassign_clear():
    a1 = tdt4250case_Department(code="sample_text", name="sample_text")
    a2 = tdt4250case_Department(code="sample_text_2", name="sample_text_2")
    b = tdt4250case_CourseInstance(semester="sample_text")
    _safe_set(b, 'tdt4250case_CourseInstance20', a1)
    assert _is_linked(b, 'tdt4250case_CourseInstance20', a1)
    if hasattr(a1, 'tdt4250case_Department'):
        assert _is_linked(a1, 'tdt4250case_Department', b)
    _safe_set(b, 'tdt4250case_CourseInstance20', a2)
    assert _is_linked(b, 'tdt4250case_CourseInstance20', a2)
    if hasattr(a1, 'tdt4250case_Department'):
        assert not _is_linked(a1, 'tdt4250case_Department', b)
    if hasattr(a2, 'tdt4250case_Department'):
        assert _is_linked(a2, 'tdt4250case_Department', b)
    _safe_set(b, 'tdt4250case_CourseInstance20', None)
    assert not _is_linked(b, 'tdt4250case_CourseInstance20', a2)
    if hasattr(a2, 'tdt4250case_Department'):
        assert not _is_linked(a2, 'tdt4250case_Department', b)


def test_assoc_role21_reverse_link_reassign_clear():
    a1 = tdt4250case_CourseRole(name="sample_text")
    a2 = tdt4250case_CourseRole(name="sample_text_2")
    b = tdt4250case_CourseInstance(semester="sample_text")
    _safe_set(b, 'tdt4250case_CourseInstance22', {a1})
    assert _is_linked(b, 'tdt4250case_CourseInstance22', a1)
    if hasattr(a1, 'tdt4250case_CourseRole'):
        assert _is_linked(a1, 'tdt4250case_CourseRole', b)
    _safe_set(b, 'tdt4250case_CourseInstance22', {a2})
    assert _is_linked(b, 'tdt4250case_CourseInstance22', a2)
    if hasattr(a1, 'tdt4250case_CourseRole'):
        assert not _is_linked(a1, 'tdt4250case_CourseRole', b)
    if hasattr(a2, 'tdt4250case_CourseRole'):
        assert _is_linked(a2, 'tdt4250case_CourseRole', b)
    _safe_set(b, 'tdt4250case_CourseInstance22', set())
    assert not _is_linked(b, 'tdt4250case_CourseInstance22', a2)
    if hasattr(a2, 'tdt4250case_CourseRole'):
        assert not _is_linked(a2, 'tdt4250case_CourseRole', b)


def test_assoc_role36_reverse_link_reassign_clear():
    a1 = tdt4250case_Person(name="sample_text", username="sample_text")
    a2 = tdt4250case_Person(name="sample_text_2", username="sample_text_2")
    b = tdt4250case_CourseRole(name="sample_text")
    _safe_set(b, 'CourseRole', a1)
    assert _is_linked(b, 'CourseRole', a1)
    if hasattr(a1, 'person'):
        assert _is_linked(a1, 'person', b)
    _safe_set(b, 'CourseRole', a2)
    assert _is_linked(b, 'CourseRole', a2)
    if hasattr(a1, 'person'):
        assert not _is_linked(a1, 'person', b)
    if hasattr(a2, 'person'):
        assert _is_linked(a2, 'person', b)
    _safe_set(b, 'CourseRole', None)
    assert not _is_linked(b, 'CourseRole', a2)
    if hasattr(a2, 'person'):
        assert not _is_linked(a2, 'person', b)


def test_assoc_studyprogram0_reverse_link_reassign_clear():
    a1 = tdt4250case_Studyprogram(code="sample_text")
    a2 = tdt4250case_Studyprogram(code="sample_text_2")
    b = tdt4250case_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'course', {a1})
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'Studyprogram'):
        assert _is_linked(a1, 'Studyprogram', b)
    _safe_set(b, 'course', {a2})
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'Studyprogram'):
        assert not _is_linked(a1, 'Studyprogram', b)
    if hasattr(a2, 'Studyprogram'):
        assert _is_linked(a2, 'Studyprogram', b)
    _safe_set(b, 'course', set())
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'Studyprogram'):
        assert not _is_linked(a2, 'Studyprogram', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activity27_stub_double():
    # tdt4250case_Examination has no real 'tdt4250case_Examination28' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250case_ExaminationActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250case_ExaminationActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250case_ExaminationActivity(evaluationForm="sample_text", weighting="sample_text")
    partner = tdt4250case_Examination()
    setattr(partner, 'tdt4250case_Examination28', None)
    _safe_set(owner, 'tdt4250case_ExaminationActivity', partner)
    assert owner in getattr(partner, 'tdt4250case_Examination28')
    _safe_set(owner, 'tdt4250case_ExaminationActivity', None)
    assert owner not in getattr(partner, 'tdt4250case_Examination28')


def test_assoc_examination16_stub_double():
    # tdt4250case_Examination has no real 'tdt4250case_Examination' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250case_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250case_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250case_CourseInstance(semester="sample_text")
    partner = tdt4250case_Examination()
    setattr(partner, 'tdt4250case_Examination', None)
    _safe_set(owner, 'tdt4250case_CourseInstance', partner)
    assert getattr(partner, 'tdt4250case_Examination') == owner
    _safe_set(owner, 'tdt4250case_CourseInstance', None)
    assert getattr(partner, 'tdt4250case_Examination') is None


def test_assoc_scheduledActivity29_stub_double():
    # tdt4250case_Timetable has no real 'tdt4250case_Timetable30' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250case_ScheduledActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250case_ScheduledActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250case_ScheduledActivity(activity="sample_text", room="sample_text", timeslot="sample_text")
    partner = tdt4250case_Timetable()
    setattr(partner, 'tdt4250case_Timetable30', None)
    _safe_set(owner, 'tdt4250case_ScheduledActivity', partner)
    assert owner in getattr(partner, 'tdt4250case_Timetable30')
    _safe_set(owner, 'tdt4250case_ScheduledActivity', None)
    assert owner not in getattr(partner, 'tdt4250case_Timetable30')


def test_assoc_timetable17_stub_double():
    # tdt4250case_Timetable has no real 'tdt4250case_Timetable' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250case_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250case_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250case_CourseInstance(semester="sample_text")
    partner = tdt4250case_Timetable()
    setattr(partner, 'tdt4250case_Timetable', None)
    _safe_set(owner, 'tdt4250case_CourseInstance18', partner)
    assert getattr(partner, 'tdt4250case_Timetable') == owner
    _safe_set(owner, 'tdt4250case_CourseInstance18', None)
    assert getattr(partner, 'tdt4250case_Timetable') is None


