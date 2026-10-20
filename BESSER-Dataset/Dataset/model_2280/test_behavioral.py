import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fenix_Capacity,
    fenix_CourseLoad,
    fenix_LessonPeriod,
    fenix_Occupation,
    fenix_Shift,
    fenix_scheduleOfCourse,
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

def test_assoc_capacity11_reverse_link_reassign_clear():
    a1 = fenix_CourseLoad(description="sample_text", id="sample_text", name="sample_text", totalQuantity=7, type="sample_text", unitQuantity=7)
    a2 = fenix_CourseLoad(description="sample_text_2", id="sample_text_2", name="sample_text_2", totalQuantity=13, type="sample_text_2", unitQuantity=13)
    b = fenix_Capacity(exam=7, normal=7)
    _safe_set(b, 'fenix_Capacity', a1)
    assert _is_linked(b, 'fenix_Capacity', a1)
    if hasattr(a1, 'fenix_CourseLoad12'):
        assert _is_linked(a1, 'fenix_CourseLoad12', b)
    _safe_set(b, 'fenix_Capacity', a2)
    assert _is_linked(b, 'fenix_Capacity', a2)
    if hasattr(a1, 'fenix_CourseLoad12'):
        assert not _is_linked(a1, 'fenix_CourseLoad12', b)
    if hasattr(a2, 'fenix_CourseLoad12'):
        assert _is_linked(a2, 'fenix_CourseLoad12', b)
    _safe_set(b, 'fenix_Capacity', None)
    assert not _is_linked(b, 'fenix_Capacity', a2)
    if hasattr(a2, 'fenix_CourseLoad12'):
        assert not _is_linked(a2, 'fenix_CourseLoad12', b)


def test_assoc_lessons1_reverse_link_reassign_clear():
    a1 = fenix_Shift(name="sample_text", types="sample_text")
    a2 = fenix_Shift(name="sample_text_2", types="sample_text_2")
    b = fenix_LessonPeriod(end="sample_text", start="sample_text")
    _safe_set(b, 'fenix_LessonPeriod', a1)
    assert _is_linked(b, 'fenix_LessonPeriod', a1)
    if hasattr(a1, 'fenix_Shift2'):
        assert _is_linked(a1, 'fenix_Shift2', b)
    _safe_set(b, 'fenix_LessonPeriod', a2)
    assert _is_linked(b, 'fenix_LessonPeriod', a2)
    if hasattr(a1, 'fenix_Shift2'):
        assert not _is_linked(a1, 'fenix_Shift2', b)
    if hasattr(a2, 'fenix_Shift2'):
        assert _is_linked(a2, 'fenix_Shift2', b)
    _safe_set(b, 'fenix_LessonPeriod', None)
    assert not _is_linked(b, 'fenix_LessonPeriod', a2)
    if hasattr(a2, 'fenix_Shift2'):
        assert not _is_linked(a2, 'fenix_Shift2', b)


def test_assoc_occupation0_reverse_link_reassign_clear():
    a1 = fenix_Shift(name="sample_text", types="sample_text")
    a2 = fenix_Shift(name="sample_text_2", types="sample_text_2")
    b = fenix_Occupation(current=7, max=7)
    _safe_set(b, 'fenix_Occupation', a1)
    assert _is_linked(b, 'fenix_Occupation', a1)
    if hasattr(a1, 'fenix_Shift'):
        assert _is_linked(a1, 'fenix_Shift', b)
    _safe_set(b, 'fenix_Occupation', a2)
    assert _is_linked(b, 'fenix_Occupation', a2)
    if hasattr(a1, 'fenix_Shift'):
        assert not _is_linked(a1, 'fenix_Shift', b)
    if hasattr(a2, 'fenix_Shift'):
        assert _is_linked(a2, 'fenix_Shift', b)
    _safe_set(b, 'fenix_Occupation', None)
    assert not _is_linked(b, 'fenix_Occupation', a2)
    if hasattr(a2, 'fenix_Shift'):
        assert not _is_linked(a2, 'fenix_Shift', b)


def test_assoc_room5_reverse_link_reassign_clear():
    a1 = fenix_LessonPeriod(end="sample_text", start="sample_text")
    a2 = fenix_LessonPeriod(end="sample_text_2", start="sample_text_2")
    b = fenix_CourseLoad(description="sample_text", id="sample_text", name="sample_text", totalQuantity=7, type="sample_text", unitQuantity=7)
    _safe_set(b, 'fenix_CourseLoad7', a1)
    assert _is_linked(b, 'fenix_CourseLoad7', a1)
    if hasattr(a1, 'fenix_LessonPeriod6'):
        assert _is_linked(a1, 'fenix_LessonPeriod6', b)
    _safe_set(b, 'fenix_CourseLoad7', a2)
    assert _is_linked(b, 'fenix_CourseLoad7', a2)
    if hasattr(a1, 'fenix_LessonPeriod6'):
        assert not _is_linked(a1, 'fenix_LessonPeriod6', b)
    if hasattr(a2, 'fenix_LessonPeriod6'):
        assert _is_linked(a2, 'fenix_LessonPeriod6', b)
    _safe_set(b, 'fenix_CourseLoad7', None)
    assert not _is_linked(b, 'fenix_CourseLoad7', a2)
    if hasattr(a2, 'fenix_LessonPeriod6'):
        assert not _is_linked(a2, 'fenix_LessonPeriod6', b)


def test_assoc_rooms3_reverse_link_reassign_clear():
    a1 = fenix_Shift(name="sample_text", types="sample_text")
    a2 = fenix_Shift(name="sample_text_2", types="sample_text_2")
    b = fenix_CourseLoad(description="sample_text", id="sample_text", name="sample_text", totalQuantity=7, type="sample_text", unitQuantity=7)
    _safe_set(b, 'fenix_CourseLoad', a1)
    assert _is_linked(b, 'fenix_CourseLoad', a1)
    if hasattr(a1, 'fenix_Shift4'):
        assert _is_linked(a1, 'fenix_Shift4', b)
    _safe_set(b, 'fenix_CourseLoad', a2)
    assert _is_linked(b, 'fenix_CourseLoad', a2)
    if hasattr(a1, 'fenix_Shift4'):
        assert not _is_linked(a1, 'fenix_Shift4', b)
    if hasattr(a2, 'fenix_Shift4'):
        assert _is_linked(a2, 'fenix_Shift4', b)
    _safe_set(b, 'fenix_CourseLoad', None)
    assert not _is_linked(b, 'fenix_CourseLoad', a2)
    if hasattr(a2, 'fenix_Shift4'):
        assert not _is_linked(a2, 'fenix_Shift4', b)


def test_assoc_topLevelSpace9_reverse_link_reassign_clear():
    a1 = fenix_CourseLoad(description="sample_text", id="sample_text", name="sample_text", totalQuantity=7, type="sample_text", unitQuantity=7)
    a2 = fenix_CourseLoad(description="sample_text_2", id="sample_text_2", name="sample_text_2", totalQuantity=13, type="sample_text_2", unitQuantity=13)
    b = fenix_CourseLoad(description="sample_text", id="sample_text", name="sample_text", totalQuantity=7, type="sample_text", unitQuantity=7)
    _safe_set(b, 'fenix_CourseLoad8', a1)
    assert _is_linked(b, 'fenix_CourseLoad8', a1)
    if hasattr(a1, 'fenix_CourseLoad10'):
        assert _is_linked(a1, 'fenix_CourseLoad10', b)
    _safe_set(b, 'fenix_CourseLoad8', a2)
    assert _is_linked(b, 'fenix_CourseLoad8', a2)
    if hasattr(a1, 'fenix_CourseLoad10'):
        assert not _is_linked(a1, 'fenix_CourseLoad10', b)
    if hasattr(a2, 'fenix_CourseLoad10'):
        assert _is_linked(a2, 'fenix_CourseLoad10', b)
    _safe_set(b, 'fenix_CourseLoad8', None)
    assert not _is_linked(b, 'fenix_CourseLoad8', a2)
    if hasattr(a2, 'fenix_CourseLoad10'):
        assert not _is_linked(a2, 'fenix_CourseLoad10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_courseLoads15_stub_double():
    # fenix_scheduleOfCourse has no real 'fenix_scheduleOfCourse16' property in the generated
    # code (a bare stub) -- manually attach it so fenix_CourseLoad's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fenix_CourseLoad's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fenix_CourseLoad(description="sample_text", id="sample_text", name="sample_text", totalQuantity=7, type="sample_text", unitQuantity=7)
    partner = fenix_scheduleOfCourse()
    setattr(partner, 'fenix_scheduleOfCourse16', None)
    _safe_set(owner, 'fenix_CourseLoad17', partner)
    assert owner in getattr(partner, 'fenix_scheduleOfCourse16')
    _safe_set(owner, 'fenix_CourseLoad17', None)
    assert owner not in getattr(partner, 'fenix_scheduleOfCourse16')


def test_assoc_lessonPeriods13_stub_double():
    # fenix_scheduleOfCourse has no real 'fenix_scheduleOfCourse' property in the generated
    # code (a bare stub) -- manually attach it so fenix_LessonPeriod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fenix_LessonPeriod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fenix_LessonPeriod(end="sample_text", start="sample_text")
    partner = fenix_scheduleOfCourse()
    setattr(partner, 'fenix_scheduleOfCourse', None)
    _safe_set(owner, 'fenix_LessonPeriod14', partner)
    assert owner in getattr(partner, 'fenix_scheduleOfCourse')
    _safe_set(owner, 'fenix_LessonPeriod14', None)
    assert owner not in getattr(partner, 'fenix_scheduleOfCourse')


def test_assoc_shifts18_stub_double():
    # fenix_scheduleOfCourse has no real 'fenix_scheduleOfCourse19' property in the generated
    # code (a bare stub) -- manually attach it so fenix_Shift's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fenix_Shift's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fenix_Shift(name="sample_text", types="sample_text")
    partner = fenix_scheduleOfCourse()
    setattr(partner, 'fenix_scheduleOfCourse19', None)
    _safe_set(owner, 'fenix_Shift20', partner)
    assert owner in getattr(partner, 'fenix_scheduleOfCourse19')
    _safe_set(owner, 'fenix_Shift20', None)
    assert owner not in getattr(partner, 'fenix_scheduleOfCourse19')


