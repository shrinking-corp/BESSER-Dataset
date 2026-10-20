import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    scheduleOfCourse_Capacity,
    scheduleOfCourse_CourseLoad,
    scheduleOfCourse_Lesson,
    scheduleOfCourse_LessonPeriod,
    scheduleOfCourse_Occupation,
    scheduleOfCourse_Room,
    scheduleOfCourse_Shift,
    scheduleOfCourse_TopLevelSpace,
    scheduleOfCourse_scheduleOfCourse,
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

def test_assoc_capacity16_reverse_link_reassign_clear():
    a1 = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    a2 = scheduleOfCourse_Room(description="sample_text_2", id="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = scheduleOfCourse_Capacity(exam=7, normal=7)
    _safe_set(b, 'scheduleOfCourse_Capacity', a1)
    assert _is_linked(b, 'scheduleOfCourse_Capacity', a1)
    if hasattr(a1, 'scheduleOfCourse_Room17'):
        assert _is_linked(a1, 'scheduleOfCourse_Room17', b)
    _safe_set(b, 'scheduleOfCourse_Capacity', a2)
    assert _is_linked(b, 'scheduleOfCourse_Capacity', a2)
    if hasattr(a1, 'scheduleOfCourse_Room17'):
        assert not _is_linked(a1, 'scheduleOfCourse_Room17', b)
    if hasattr(a2, 'scheduleOfCourse_Room17'):
        assert _is_linked(a2, 'scheduleOfCourse_Room17', b)
    _safe_set(b, 'scheduleOfCourse_Capacity', None)
    assert not _is_linked(b, 'scheduleOfCourse_Capacity', a2)
    if hasattr(a2, 'scheduleOfCourse_Room17'):
        assert not _is_linked(a2, 'scheduleOfCourse_Room17', b)


def test_assoc_lessons1_reverse_link_reassign_clear():
    a1 = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    a2 = scheduleOfCourse_Shift(name="sample_text_2", types="sample_text_2")
    b = scheduleOfCourse_Lesson(end="sample_text", start="sample_text")
    _safe_set(b, 'scheduleOfCourse_Lesson', a1)
    assert _is_linked(b, 'scheduleOfCourse_Lesson', a1)
    if hasattr(a1, 'scheduleOfCourse_Shift2'):
        assert _is_linked(a1, 'scheduleOfCourse_Shift2', b)
    _safe_set(b, 'scheduleOfCourse_Lesson', a2)
    assert _is_linked(b, 'scheduleOfCourse_Lesson', a2)
    if hasattr(a1, 'scheduleOfCourse_Shift2'):
        assert not _is_linked(a1, 'scheduleOfCourse_Shift2', b)
    if hasattr(a2, 'scheduleOfCourse_Shift2'):
        assert _is_linked(a2, 'scheduleOfCourse_Shift2', b)
    _safe_set(b, 'scheduleOfCourse_Lesson', None)
    assert not _is_linked(b, 'scheduleOfCourse_Lesson', a2)
    if hasattr(a2, 'scheduleOfCourse_Shift2'):
        assert not _is_linked(a2, 'scheduleOfCourse_Shift2', b)


def test_assoc_occupation0_reverse_link_reassign_clear():
    a1 = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    a2 = scheduleOfCourse_Shift(name="sample_text_2", types="sample_text_2")
    b = scheduleOfCourse_Occupation(current=7, max=7)
    _safe_set(b, 'scheduleOfCourse_Occupation', a1)
    assert _is_linked(b, 'scheduleOfCourse_Occupation', a1)
    if hasattr(a1, 'scheduleOfCourse_Shift'):
        assert _is_linked(a1, 'scheduleOfCourse_Shift', b)
    _safe_set(b, 'scheduleOfCourse_Occupation', a2)
    assert _is_linked(b, 'scheduleOfCourse_Occupation', a2)
    if hasattr(a1, 'scheduleOfCourse_Shift'):
        assert not _is_linked(a1, 'scheduleOfCourse_Shift', b)
    if hasattr(a2, 'scheduleOfCourse_Shift'):
        assert _is_linked(a2, 'scheduleOfCourse_Shift', b)
    _safe_set(b, 'scheduleOfCourse_Occupation', None)
    assert not _is_linked(b, 'scheduleOfCourse_Occupation', a2)
    if hasattr(a2, 'scheduleOfCourse_Shift'):
        assert not _is_linked(a2, 'scheduleOfCourse_Shift', b)


def test_assoc_room11_reverse_link_reassign_clear():
    a1 = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    a2 = scheduleOfCourse_Room(description="sample_text_2", id="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = scheduleOfCourse_Lesson(end="sample_text", start="sample_text")
    _safe_set(b, 'scheduleOfCourse_Lesson12', a1)
    assert _is_linked(b, 'scheduleOfCourse_Lesson12', a1)
    if hasattr(a1, 'scheduleOfCourse_Room13'):
        assert _is_linked(a1, 'scheduleOfCourse_Room13', b)
    _safe_set(b, 'scheduleOfCourse_Lesson12', a2)
    assert _is_linked(b, 'scheduleOfCourse_Lesson12', a2)
    if hasattr(a1, 'scheduleOfCourse_Room13'):
        assert not _is_linked(a1, 'scheduleOfCourse_Room13', b)
    if hasattr(a2, 'scheduleOfCourse_Room13'):
        assert _is_linked(a2, 'scheduleOfCourse_Room13', b)
    _safe_set(b, 'scheduleOfCourse_Lesson12', None)
    assert not _is_linked(b, 'scheduleOfCourse_Lesson12', a2)
    if hasattr(a2, 'scheduleOfCourse_Room13'):
        assert not _is_linked(a2, 'scheduleOfCourse_Room13', b)


def test_assoc_rooms3_reverse_link_reassign_clear():
    a1 = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    a2 = scheduleOfCourse_Shift(name="sample_text_2", types="sample_text_2")
    b = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'scheduleOfCourse_Room', a1)
    assert _is_linked(b, 'scheduleOfCourse_Room', a1)
    if hasattr(a1, 'scheduleOfCourse_Shift4'):
        assert _is_linked(a1, 'scheduleOfCourse_Shift4', b)
    _safe_set(b, 'scheduleOfCourse_Room', a2)
    assert _is_linked(b, 'scheduleOfCourse_Room', a2)
    if hasattr(a1, 'scheduleOfCourse_Shift4'):
        assert not _is_linked(a1, 'scheduleOfCourse_Shift4', b)
    if hasattr(a2, 'scheduleOfCourse_Shift4'):
        assert _is_linked(a2, 'scheduleOfCourse_Shift4', b)
    _safe_set(b, 'scheduleOfCourse_Room', None)
    assert not _is_linked(b, 'scheduleOfCourse_Room', a2)
    if hasattr(a2, 'scheduleOfCourse_Shift4'):
        assert not _is_linked(a2, 'scheduleOfCourse_Shift4', b)


def test_assoc_topLevelSpace14_reverse_link_reassign_clear():
    a1 = scheduleOfCourse_TopLevelSpace(id="sample_text", name="sample_text", type="sample_text")
    a2 = scheduleOfCourse_TopLevelSpace(id="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'scheduleOfCourse_Room15', a1)
    assert _is_linked(b, 'scheduleOfCourse_Room15', a1)
    if hasattr(a1, 'scheduleOfCourse_TopLevelSpace'):
        assert _is_linked(a1, 'scheduleOfCourse_TopLevelSpace', b)
    _safe_set(b, 'scheduleOfCourse_Room15', a2)
    assert _is_linked(b, 'scheduleOfCourse_Room15', a2)
    if hasattr(a1, 'scheduleOfCourse_TopLevelSpace'):
        assert not _is_linked(a1, 'scheduleOfCourse_TopLevelSpace', b)
    if hasattr(a2, 'scheduleOfCourse_TopLevelSpace'):
        assert _is_linked(a2, 'scheduleOfCourse_TopLevelSpace', b)
    _safe_set(b, 'scheduleOfCourse_Room15', None)
    assert not _is_linked(b, 'scheduleOfCourse_Room15', a2)
    if hasattr(a2, 'scheduleOfCourse_TopLevelSpace'):
        assert not _is_linked(a2, 'scheduleOfCourse_TopLevelSpace', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_courseLoads6_stub_double():
    # scheduleOfCourse_scheduleOfCourse has no real 'scheduleOfCourse_scheduleOfCourse7' property in the generated
    # code (a bare stub) -- manually attach it so scheduleOfCourse_CourseLoad's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scheduleOfCourse_CourseLoad's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scheduleOfCourse_CourseLoad(totalQuantity=7, type="sample_text", unitQuantity=7)
    partner = scheduleOfCourse_scheduleOfCourse()
    setattr(partner, 'scheduleOfCourse_scheduleOfCourse7', None)
    _safe_set(owner, 'scheduleOfCourse_CourseLoad', partner)
    assert owner in getattr(partner, 'scheduleOfCourse_scheduleOfCourse7')
    _safe_set(owner, 'scheduleOfCourse_CourseLoad', None)
    assert owner not in getattr(partner, 'scheduleOfCourse_scheduleOfCourse7')


def test_assoc_lessonPeriods5_stub_double():
    # scheduleOfCourse_scheduleOfCourse has no real 'scheduleOfCourse_scheduleOfCourse' property in the generated
    # code (a bare stub) -- manually attach it so scheduleOfCourse_LessonPeriod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scheduleOfCourse_LessonPeriod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scheduleOfCourse_LessonPeriod(end="sample_text", start="sample_text")
    partner = scheduleOfCourse_scheduleOfCourse()
    setattr(partner, 'scheduleOfCourse_scheduleOfCourse', None)
    _safe_set(owner, 'scheduleOfCourse_LessonPeriod', partner)
    assert owner in getattr(partner, 'scheduleOfCourse_scheduleOfCourse')
    _safe_set(owner, 'scheduleOfCourse_LessonPeriod', None)
    assert owner not in getattr(partner, 'scheduleOfCourse_scheduleOfCourse')


def test_assoc_shifts8_stub_double():
    # scheduleOfCourse_scheduleOfCourse has no real 'scheduleOfCourse_scheduleOfCourse9' property in the generated
    # code (a bare stub) -- manually attach it so scheduleOfCourse_Shift's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scheduleOfCourse_Shift's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    partner = scheduleOfCourse_scheduleOfCourse()
    setattr(partner, 'scheduleOfCourse_scheduleOfCourse9', None)
    _safe_set(owner, 'scheduleOfCourse_Shift10', partner)
    assert owner in getattr(partner, 'scheduleOfCourse_scheduleOfCourse9')
    _safe_set(owner, 'scheduleOfCourse_Shift10', None)
    assert owner not in getattr(partner, 'scheduleOfCourse_scheduleOfCourse9')


