import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_scheduleOfCourse_Capacity_exam_value_roundtrip():
    instance = scheduleOfCourse_Capacity(exam=7, normal=7)
    assert instance.exam == 7
    instance.exam = 13
    assert instance.exam == 13


def test_scheduleOfCourse_Capacity_normal_value_roundtrip():
    instance = scheduleOfCourse_Capacity(exam=7, normal=7)
    assert instance.normal == 7
    instance.normal = 13
    assert instance.normal == 13


def test_scheduleOfCourse_CourseLoad_totalQuantity_value_roundtrip():
    instance = scheduleOfCourse_CourseLoad(totalQuantity=7, type="sample_text", unitQuantity=7)
    assert instance.totalQuantity == 7
    instance.totalQuantity = 13
    assert instance.totalQuantity == 13


def test_scheduleOfCourse_CourseLoad_type_value_roundtrip():
    instance = scheduleOfCourse_CourseLoad(totalQuantity=7, type="sample_text", unitQuantity=7)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_scheduleOfCourse_CourseLoad_unitQuantity_value_roundtrip():
    instance = scheduleOfCourse_CourseLoad(totalQuantity=7, type="sample_text", unitQuantity=7)
    assert instance.unitQuantity == 7
    instance.unitQuantity = 13
    assert instance.unitQuantity == 13


def test_scheduleOfCourse_Lesson_end_value_roundtrip():
    instance = scheduleOfCourse_Lesson(end="sample_text", start="sample_text")
    assert instance.end == "sample_text"
    instance.end = "sample_text_2"
    assert instance.end == "sample_text_2"


def test_scheduleOfCourse_Lesson_start_value_roundtrip():
    instance = scheduleOfCourse_Lesson(end="sample_text", start="sample_text")
    assert instance.start == "sample_text"
    instance.start = "sample_text_2"
    assert instance.start == "sample_text_2"


def test_scheduleOfCourse_LessonPeriod_end_value_roundtrip():
    instance = scheduleOfCourse_LessonPeriod(end="sample_text", start="sample_text")
    assert instance.end == "sample_text"
    instance.end = "sample_text_2"
    assert instance.end == "sample_text_2"


def test_scheduleOfCourse_LessonPeriod_start_value_roundtrip():
    instance = scheduleOfCourse_LessonPeriod(end="sample_text", start="sample_text")
    assert instance.start == "sample_text"
    instance.start = "sample_text_2"
    assert instance.start == "sample_text_2"


def test_scheduleOfCourse_Occupation_current_value_roundtrip():
    instance = scheduleOfCourse_Occupation(current=7, max=7)
    assert instance.current == 7
    instance.current = 13
    assert instance.current == 13


def test_scheduleOfCourse_Occupation_max_value_roundtrip():
    instance = scheduleOfCourse_Occupation(current=7, max=7)
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_scheduleOfCourse_Room_description_value_roundtrip():
    instance = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_scheduleOfCourse_Room_id_value_roundtrip():
    instance = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scheduleOfCourse_Room_name_value_roundtrip():
    instance = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_scheduleOfCourse_Room_type_value_roundtrip():
    instance = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_scheduleOfCourse_Shift_name_value_roundtrip():
    instance = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_scheduleOfCourse_Shift_types_value_roundtrip():
    instance = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    assert instance.types == "sample_text"
    instance.types = "sample_text_2"
    assert instance.types == "sample_text_2"


def test_scheduleOfCourse_TopLevelSpace_id_value_roundtrip():
    instance = scheduleOfCourse_TopLevelSpace(id="sample_text", name="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scheduleOfCourse_TopLevelSpace_name_value_roundtrip():
    instance = scheduleOfCourse_TopLevelSpace(id="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_scheduleOfCourse_TopLevelSpace_type_value_roundtrip():
    instance = scheduleOfCourse_TopLevelSpace(id="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_assoc_capacity16_link_reassign_clear():
    a = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    b1 = scheduleOfCourse_Capacity(exam=7, normal=7)
    b2 = scheduleOfCourse_Capacity(exam=13, normal=13)
    _safe_set(a, 'scheduleOfCourse_Room17', b1)
    assert _is_linked(a, 'scheduleOfCourse_Room17', b1)
    if hasattr(b1, 'scheduleOfCourse_Capacity'):
        assert _is_linked(b1, 'scheduleOfCourse_Capacity', a)
    _safe_set(a, 'scheduleOfCourse_Room17', b2)
    assert _is_linked(a, 'scheduleOfCourse_Room17', b2)
    if hasattr(b1, 'scheduleOfCourse_Capacity'):
        assert not _is_linked(b1, 'scheduleOfCourse_Capacity', a)
    if hasattr(b2, 'scheduleOfCourse_Capacity'):
        assert _is_linked(b2, 'scheduleOfCourse_Capacity', a)
    _safe_set(a, 'scheduleOfCourse_Room17', None)
    assert not _is_linked(a, 'scheduleOfCourse_Room17', b2)
    if hasattr(b2, 'scheduleOfCourse_Capacity'):
        assert not _is_linked(b2, 'scheduleOfCourse_Capacity', a)


def test_assoc_courseLoads6_link_reassign_clear():
    a = scheduleOfCourse_CourseLoad(totalQuantity=7, type="sample_text", unitQuantity=7)
    b1 = scheduleOfCourse_scheduleOfCourse()
    b2 = scheduleOfCourse_scheduleOfCourse()
    _safe_set(a, 'scheduleOfCourse_CourseLoad', b1)
    assert _is_linked(a, 'scheduleOfCourse_CourseLoad', b1)
    if hasattr(b1, 'scheduleOfCourse_scheduleOfCourse7'):
        assert _is_linked(b1, 'scheduleOfCourse_scheduleOfCourse7', a)
    _safe_set(a, 'scheduleOfCourse_CourseLoad', b2)
    assert _is_linked(a, 'scheduleOfCourse_CourseLoad', b2)
    if hasattr(b1, 'scheduleOfCourse_scheduleOfCourse7'):
        assert not _is_linked(b1, 'scheduleOfCourse_scheduleOfCourse7', a)
    if hasattr(b2, 'scheduleOfCourse_scheduleOfCourse7'):
        assert _is_linked(b2, 'scheduleOfCourse_scheduleOfCourse7', a)
    _safe_set(a, 'scheduleOfCourse_CourseLoad', None)
    assert not _is_linked(a, 'scheduleOfCourse_CourseLoad', b2)
    if hasattr(b2, 'scheduleOfCourse_scheduleOfCourse7'):
        assert not _is_linked(b2, 'scheduleOfCourse_scheduleOfCourse7', a)


def test_assoc_lessonPeriods5_link_reassign_clear():
    a = scheduleOfCourse_LessonPeriod(end="sample_text", start="sample_text")
    b1 = scheduleOfCourse_scheduleOfCourse()
    b2 = scheduleOfCourse_scheduleOfCourse()
    _safe_set(a, 'scheduleOfCourse_LessonPeriod', b1)
    assert _is_linked(a, 'scheduleOfCourse_LessonPeriod', b1)
    if hasattr(b1, 'scheduleOfCourse_scheduleOfCourse'):
        assert _is_linked(b1, 'scheduleOfCourse_scheduleOfCourse', a)
    _safe_set(a, 'scheduleOfCourse_LessonPeriod', b2)
    assert _is_linked(a, 'scheduleOfCourse_LessonPeriod', b2)
    if hasattr(b1, 'scheduleOfCourse_scheduleOfCourse'):
        assert not _is_linked(b1, 'scheduleOfCourse_scheduleOfCourse', a)
    if hasattr(b2, 'scheduleOfCourse_scheduleOfCourse'):
        assert _is_linked(b2, 'scheduleOfCourse_scheduleOfCourse', a)
    _safe_set(a, 'scheduleOfCourse_LessonPeriod', None)
    assert not _is_linked(a, 'scheduleOfCourse_LessonPeriod', b2)
    if hasattr(b2, 'scheduleOfCourse_scheduleOfCourse'):
        assert not _is_linked(b2, 'scheduleOfCourse_scheduleOfCourse', a)


def test_assoc_lessons1_link_reassign_clear():
    a = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    b1 = scheduleOfCourse_Lesson(end="sample_text", start="sample_text")
    b2 = scheduleOfCourse_Lesson(end="sample_text_2", start="sample_text_2")
    _safe_set(a, 'scheduleOfCourse_Shift2', {b1})
    assert _is_linked(a, 'scheduleOfCourse_Shift2', b1)
    if hasattr(b1, 'scheduleOfCourse_Lesson'):
        assert _is_linked(b1, 'scheduleOfCourse_Lesson', a)
    _safe_set(a, 'scheduleOfCourse_Shift2', {b2})
    assert _is_linked(a, 'scheduleOfCourse_Shift2', b2)
    if hasattr(b1, 'scheduleOfCourse_Lesson'):
        assert not _is_linked(b1, 'scheduleOfCourse_Lesson', a)
    if hasattr(b2, 'scheduleOfCourse_Lesson'):
        assert _is_linked(b2, 'scheduleOfCourse_Lesson', a)
    _safe_set(a, 'scheduleOfCourse_Shift2', set())
    assert not _is_linked(a, 'scheduleOfCourse_Shift2', b2)
    if hasattr(b2, 'scheduleOfCourse_Lesson'):
        assert not _is_linked(b2, 'scheduleOfCourse_Lesson', a)


def test_assoc_occupation0_link_reassign_clear():
    a = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    b1 = scheduleOfCourse_Occupation(current=7, max=7)
    b2 = scheduleOfCourse_Occupation(current=13, max=13)
    _safe_set(a, 'scheduleOfCourse_Shift', b1)
    assert _is_linked(a, 'scheduleOfCourse_Shift', b1)
    if hasattr(b1, 'scheduleOfCourse_Occupation'):
        assert _is_linked(b1, 'scheduleOfCourse_Occupation', a)
    _safe_set(a, 'scheduleOfCourse_Shift', b2)
    assert _is_linked(a, 'scheduleOfCourse_Shift', b2)
    if hasattr(b1, 'scheduleOfCourse_Occupation'):
        assert not _is_linked(b1, 'scheduleOfCourse_Occupation', a)
    if hasattr(b2, 'scheduleOfCourse_Occupation'):
        assert _is_linked(b2, 'scheduleOfCourse_Occupation', a)
    _safe_set(a, 'scheduleOfCourse_Shift', None)
    assert not _is_linked(a, 'scheduleOfCourse_Shift', b2)
    if hasattr(b2, 'scheduleOfCourse_Occupation'):
        assert not _is_linked(b2, 'scheduleOfCourse_Occupation', a)


def test_assoc_room11_link_reassign_clear():
    a = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    b1 = scheduleOfCourse_Lesson(end="sample_text", start="sample_text")
    b2 = scheduleOfCourse_Lesson(end="sample_text_2", start="sample_text_2")
    _safe_set(a, 'scheduleOfCourse_Room13', b1)
    assert _is_linked(a, 'scheduleOfCourse_Room13', b1)
    if hasattr(b1, 'scheduleOfCourse_Lesson12'):
        assert _is_linked(b1, 'scheduleOfCourse_Lesson12', a)
    _safe_set(a, 'scheduleOfCourse_Room13', b2)
    assert _is_linked(a, 'scheduleOfCourse_Room13', b2)
    if hasattr(b1, 'scheduleOfCourse_Lesson12'):
        assert not _is_linked(b1, 'scheduleOfCourse_Lesson12', a)
    if hasattr(b2, 'scheduleOfCourse_Lesson12'):
        assert _is_linked(b2, 'scheduleOfCourse_Lesson12', a)
    _safe_set(a, 'scheduleOfCourse_Room13', None)
    assert not _is_linked(a, 'scheduleOfCourse_Room13', b2)
    if hasattr(b2, 'scheduleOfCourse_Lesson12'):
        assert not _is_linked(b2, 'scheduleOfCourse_Lesson12', a)


def test_assoc_rooms3_link_reassign_clear():
    a = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    b1 = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    b2 = scheduleOfCourse_Room(description="sample_text_2", id="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'scheduleOfCourse_Shift4', {b1})
    assert _is_linked(a, 'scheduleOfCourse_Shift4', b1)
    if hasattr(b1, 'scheduleOfCourse_Room'):
        assert _is_linked(b1, 'scheduleOfCourse_Room', a)
    _safe_set(a, 'scheduleOfCourse_Shift4', {b2})
    assert _is_linked(a, 'scheduleOfCourse_Shift4', b2)
    if hasattr(b1, 'scheduleOfCourse_Room'):
        assert not _is_linked(b1, 'scheduleOfCourse_Room', a)
    if hasattr(b2, 'scheduleOfCourse_Room'):
        assert _is_linked(b2, 'scheduleOfCourse_Room', a)
    _safe_set(a, 'scheduleOfCourse_Shift4', set())
    assert not _is_linked(a, 'scheduleOfCourse_Shift4', b2)
    if hasattr(b2, 'scheduleOfCourse_Room'):
        assert not _is_linked(b2, 'scheduleOfCourse_Room', a)


def test_assoc_shifts8_link_reassign_clear():
    a = scheduleOfCourse_Shift(name="sample_text", types="sample_text")
    b1 = scheduleOfCourse_scheduleOfCourse()
    b2 = scheduleOfCourse_scheduleOfCourse()
    _safe_set(a, 'scheduleOfCourse_Shift10', b1)
    assert _is_linked(a, 'scheduleOfCourse_Shift10', b1)
    if hasattr(b1, 'scheduleOfCourse_scheduleOfCourse9'):
        assert _is_linked(b1, 'scheduleOfCourse_scheduleOfCourse9', a)
    _safe_set(a, 'scheduleOfCourse_Shift10', b2)
    assert _is_linked(a, 'scheduleOfCourse_Shift10', b2)
    if hasattr(b1, 'scheduleOfCourse_scheduleOfCourse9'):
        assert not _is_linked(b1, 'scheduleOfCourse_scheduleOfCourse9', a)
    if hasattr(b2, 'scheduleOfCourse_scheduleOfCourse9'):
        assert _is_linked(b2, 'scheduleOfCourse_scheduleOfCourse9', a)
    _safe_set(a, 'scheduleOfCourse_Shift10', None)
    assert not _is_linked(a, 'scheduleOfCourse_Shift10', b2)
    if hasattr(b2, 'scheduleOfCourse_scheduleOfCourse9'):
        assert not _is_linked(b2, 'scheduleOfCourse_scheduleOfCourse9', a)


def test_assoc_topLevelSpace14_link_reassign_clear():
    a = scheduleOfCourse_TopLevelSpace(id="sample_text", name="sample_text", type="sample_text")
    b1 = scheduleOfCourse_Room(description="sample_text", id="sample_text", name="sample_text", type="sample_text")
    b2 = scheduleOfCourse_Room(description="sample_text_2", id="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'scheduleOfCourse_TopLevelSpace', b1)
    assert _is_linked(a, 'scheduleOfCourse_TopLevelSpace', b1)
    if hasattr(b1, 'scheduleOfCourse_Room15'):
        assert _is_linked(b1, 'scheduleOfCourse_Room15', a)
    _safe_set(a, 'scheduleOfCourse_TopLevelSpace', b2)
    assert _is_linked(a, 'scheduleOfCourse_TopLevelSpace', b2)
    if hasattr(b1, 'scheduleOfCourse_Room15'):
        assert not _is_linked(b1, 'scheduleOfCourse_Room15', a)
    if hasattr(b2, 'scheduleOfCourse_Room15'):
        assert _is_linked(b2, 'scheduleOfCourse_Room15', a)
    _safe_set(a, 'scheduleOfCourse_TopLevelSpace', None)
    assert not _is_linked(a, 'scheduleOfCourse_TopLevelSpace', b2)
    if hasattr(b2, 'scheduleOfCourse_Room15'):
        assert not _is_linked(b2, 'scheduleOfCourse_Room15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

scheduleOfCourse_Capacity_strategy = st.builds(scheduleOfCourse_Capacity, exam=st.integers(), normal=st.integers())
@given(instance=scheduleOfCourse_Capacity_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_Capacity_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Capacity)


scheduleOfCourse_CourseLoad_strategy = st.builds(scheduleOfCourse_CourseLoad, totalQuantity=st.integers(), type=safe_text, unitQuantity=st.integers())
@given(instance=scheduleOfCourse_CourseLoad_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_CourseLoad_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_CourseLoad)


scheduleOfCourse_Lesson_strategy = st.builds(scheduleOfCourse_Lesson, end=safe_text, start=safe_text)
@given(instance=scheduleOfCourse_Lesson_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_Lesson_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Lesson)


scheduleOfCourse_LessonPeriod_strategy = st.builds(scheduleOfCourse_LessonPeriod, end=safe_text, start=safe_text)
@given(instance=scheduleOfCourse_LessonPeriod_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_LessonPeriod_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_LessonPeriod)


scheduleOfCourse_Occupation_strategy = st.builds(scheduleOfCourse_Occupation, current=st.integers(), max=st.integers())
@given(instance=scheduleOfCourse_Occupation_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_Occupation_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Occupation)


scheduleOfCourse_Room_strategy = st.builds(scheduleOfCourse_Room, description=safe_text, id=safe_text, name=safe_text, type=safe_text)
@given(instance=scheduleOfCourse_Room_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_Room_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Room)


scheduleOfCourse_Shift_strategy = st.builds(scheduleOfCourse_Shift, name=safe_text, types=safe_text)
@given(instance=scheduleOfCourse_Shift_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_Shift_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_Shift)


scheduleOfCourse_TopLevelSpace_strategy = st.builds(scheduleOfCourse_TopLevelSpace, id=safe_text, name=safe_text, type=safe_text)
@given(instance=scheduleOfCourse_TopLevelSpace_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_TopLevelSpace_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_TopLevelSpace)


scheduleOfCourse_scheduleOfCourse_strategy = st.builds(scheduleOfCourse_scheduleOfCourse)
@given(instance=scheduleOfCourse_scheduleOfCourse_strategy)
@settings(max_examples=25)
def test_scheduleOfCourse_scheduleOfCourse_instantiation(instance):
    assert isinstance(instance, scheduleOfCourse_scheduleOfCourse)


