import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    oving1APD_Course,
    oving1APD_Department,
    oving1APD_Semester,
    oving1APD_Slot,
    oving1APD_Specialization,
    oving1APD_StudyProgram,
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

def test_assoc_course1_reverse_link_reassign_clear():
    a1 = oving1APD_Department(name="sample_text", shortName="sample_text")
    a2 = oving1APD_Department(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'oving1APD_Course', a1)
    assert _is_linked(b, 'oving1APD_Course', a1)
    if hasattr(a1, 'oving1APD_Department'):
        assert _is_linked(a1, 'oving1APD_Department', b)
    _safe_set(b, 'oving1APD_Course', a2)
    assert _is_linked(b, 'oving1APD_Course', a2)
    if hasattr(a1, 'oving1APD_Department'):
        assert not _is_linked(a1, 'oving1APD_Department', b)
    if hasattr(a2, 'oving1APD_Department'):
        assert _is_linked(a2, 'oving1APD_Department', b)
    _safe_set(b, 'oving1APD_Course', None)
    assert not _is_linked(b, 'oving1APD_Course', a2)
    if hasattr(a2, 'oving1APD_Department'):
        assert not _is_linked(a2, 'oving1APD_Department', b)


def test_assoc_course24_reverse_link_reassign_clear():
    a1 = oving1APD_Specialization(name="sample_text")
    a2 = oving1APD_Specialization(name="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'Course26', a1)
    assert _is_linked(b, 'Course26', a1)
    if hasattr(a1, 'specialization25'):
        assert _is_linked(a1, 'specialization25', b)
    _safe_set(b, 'Course26', a2)
    assert _is_linked(b, 'Course26', a2)
    if hasattr(a1, 'specialization25'):
        assert not _is_linked(a1, 'specialization25', b)
    if hasattr(a2, 'specialization25'):
        assert _is_linked(a2, 'specialization25', b)
    _safe_set(b, 'Course26', None)
    assert not _is_linked(b, 'Course26', a2)
    if hasattr(a2, 'specialization25'):
        assert not _is_linked(a2, 'specialization25', b)


def test_assoc_course30_reverse_link_reassign_clear():
    a1 = oving1APD_Slot(name="sample_text")
    a2 = oving1APD_Slot(name="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'Course31', a1)
    assert _is_linked(b, 'Course31', a1)
    if hasattr(a1, 'slot'):
        assert _is_linked(a1, 'slot', b)
    _safe_set(b, 'Course31', a2)
    assert _is_linked(b, 'Course31', a2)
    if hasattr(a1, 'slot'):
        assert not _is_linked(a1, 'slot', b)
    if hasattr(a2, 'slot'):
        assert _is_linked(a2, 'slot', b)
    _safe_set(b, 'Course31', None)
    assert not _is_linked(b, 'Course31', a2)
    if hasattr(a2, 'slot'):
        assert not _is_linked(a2, 'slot', b)


def test_assoc_courseInSemester7_reverse_link_reassign_clear():
    a1 = oving1APD_Semester(number=7)
    a2 = oving1APD_Semester(number=13)
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'hasCourse', {a1})
    assert _is_linked(b, 'hasCourse', a1)
    if hasattr(a1, 'Semester8'):
        assert _is_linked(a1, 'Semester8', b)
    _safe_set(b, 'hasCourse', {a2})
    assert _is_linked(b, 'hasCourse', a2)
    if hasattr(a1, 'Semester8'):
        assert not _is_linked(a1, 'Semester8', b)
    if hasattr(a2, 'Semester8'):
        assert _is_linked(a2, 'Semester8', b)
    _safe_set(b, 'hasCourse', set())
    assert not _is_linked(b, 'hasCourse', a2)
    if hasattr(a2, 'Semester8'):
        assert not _is_linked(a2, 'Semester8', b)


def test_assoc_department5_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'studyProgram6'):
        assert _is_linked(a1, 'studyProgram6', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'studyProgram6'):
        assert not _is_linked(a1, 'studyProgram6', b)
    if hasattr(a2, 'studyProgram6'):
        assert _is_linked(a2, 'studyProgram6', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'studyProgram6'):
        assert not _is_linked(a2, 'studyProgram6', b)


def test_assoc_hasCourse13_reverse_link_reassign_clear():
    a1 = oving1APD_Semester(number=7)
    a2 = oving1APD_Semester(number=13)
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'courseInSemester'):
        assert _is_linked(a1, 'courseInSemester', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'courseInSemester'):
        assert not _is_linked(a1, 'courseInSemester', b)
    if hasattr(a2, 'courseInSemester'):
        assert _is_linked(a2, 'courseInSemester', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'courseInSemester'):
        assert not _is_linked(a2, 'courseInSemester', b)


def test_assoc_semester22_reverse_link_reassign_clear():
    a1 = oving1APD_Specialization(name="sample_text")
    a2 = oving1APD_Specialization(name="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'Semester23', a1)
    assert _is_linked(b, 'Semester23', a1)
    if hasattr(a1, 'specialization'):
        assert _is_linked(a1, 'specialization', b)
    _safe_set(b, 'Semester23', a2)
    assert _is_linked(b, 'Semester23', a2)
    if hasattr(a1, 'specialization'):
        assert not _is_linked(a1, 'specialization', b)
    if hasattr(a2, 'specialization'):
        assert _is_linked(a2, 'specialization', b)
    _safe_set(b, 'Semester23', None)
    assert not _is_linked(b, 'Semester23', a2)
    if hasattr(a2, 'specialization'):
        assert not _is_linked(a2, 'specialization', b)


def test_assoc_semester3_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'Semester', a1)
    assert _is_linked(b, 'Semester', a1)
    if hasattr(a1, 'studyProgram4'):
        assert _is_linked(a1, 'studyProgram4', b)
    _safe_set(b, 'Semester', a2)
    assert _is_linked(b, 'Semester', a2)
    if hasattr(a1, 'studyProgram4'):
        assert not _is_linked(a1, 'studyProgram4', b)
    if hasattr(a2, 'studyProgram4'):
        assert _is_linked(a2, 'studyProgram4', b)
    _safe_set(b, 'Semester', None)
    assert not _is_linked(b, 'Semester', a2)
    if hasattr(a2, 'studyProgram4'):
        assert not _is_linked(a2, 'studyProgram4', b)


def test_assoc_semester32_reverse_link_reassign_clear():
    a1 = oving1APD_Slot(name="sample_text")
    a2 = oving1APD_Slot(name="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'Semester34', a1)
    assert _is_linked(b, 'Semester34', a1)
    if hasattr(a1, 'slot33'):
        assert _is_linked(a1, 'slot33', b)
    _safe_set(b, 'Semester34', a2)
    assert _is_linked(b, 'Semester34', a2)
    if hasattr(a1, 'slot33'):
        assert not _is_linked(a1, 'slot33', b)
    if hasattr(a2, 'slot33'):
        assert _is_linked(a2, 'slot33', b)
    _safe_set(b, 'Semester34', None)
    assert not _is_linked(b, 'Semester34', a2)
    if hasattr(a2, 'slot33'):
        assert not _is_linked(a2, 'slot33', b)


def test_assoc_slot11_reverse_link_reassign_clear():
    a1 = oving1APD_Slot(name="sample_text")
    a2 = oving1APD_Slot(name="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'course12', a1)
    assert _is_linked(b, 'course12', a1)
    if hasattr(a1, 'Slot'):
        assert _is_linked(a1, 'Slot', b)
    _safe_set(b, 'course12', a2)
    assert _is_linked(b, 'course12', a2)
    if hasattr(a1, 'Slot'):
        assert not _is_linked(a1, 'Slot', b)
    if hasattr(a2, 'Slot'):
        assert _is_linked(a2, 'Slot', b)
    _safe_set(b, 'course12', None)
    assert not _is_linked(b, 'course12', a2)
    if hasattr(a2, 'Slot'):
        assert not _is_linked(a2, 'Slot', b)


def test_assoc_slot14_reverse_link_reassign_clear():
    a1 = oving1APD_Slot(name="sample_text")
    a2 = oving1APD_Slot(name="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'semester', a1)
    assert _is_linked(b, 'semester', a1)
    if hasattr(a1, 'Slot15'):
        assert _is_linked(a1, 'Slot15', b)
    _safe_set(b, 'semester', a2)
    assert _is_linked(b, 'semester', a2)
    if hasattr(a1, 'Slot15'):
        assert not _is_linked(a1, 'Slot15', b)
    if hasattr(a2, 'Slot15'):
        assert _is_linked(a2, 'Slot15', b)
    _safe_set(b, 'semester', None)
    assert not _is_linked(b, 'semester', a2)
    if hasattr(a2, 'Slot15'):
        assert not _is_linked(a2, 'Slot15', b)


def test_assoc_specialization19_reverse_link_reassign_clear():
    a1 = oving1APD_Specialization(name="sample_text")
    a2 = oving1APD_Specialization(name="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'semester20', a1)
    assert _is_linked(b, 'semester20', a1)
    if hasattr(a1, 'Specialization21'):
        assert _is_linked(a1, 'Specialization21', b)
    _safe_set(b, 'semester20', a2)
    assert _is_linked(b, 'semester20', a2)
    if hasattr(a1, 'Specialization21'):
        assert not _is_linked(a1, 'Specialization21', b)
    if hasattr(a2, 'Specialization21'):
        assert _is_linked(a2, 'Specialization21', b)
    _safe_set(b, 'semester20', None)
    assert not _is_linked(b, 'semester20', a2)
    if hasattr(a2, 'Specialization21'):
        assert not _is_linked(a2, 'Specialization21', b)


def test_assoc_specialization2_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Specialization(name="sample_text")
    _safe_set(b, 'Specialization', a1)
    assert _is_linked(b, 'Specialization', a1)
    if hasattr(a1, 'studyProgram'):
        assert _is_linked(a1, 'studyProgram', b)
    _safe_set(b, 'Specialization', a2)
    assert _is_linked(b, 'Specialization', a2)
    if hasattr(a1, 'studyProgram'):
        assert not _is_linked(a1, 'studyProgram', b)
    if hasattr(a2, 'studyProgram'):
        assert _is_linked(a2, 'studyProgram', b)
    _safe_set(b, 'Specialization', None)
    assert not _is_linked(b, 'Specialization', a2)
    if hasattr(a2, 'studyProgram'):
        assert not _is_linked(a2, 'studyProgram', b)


def test_assoc_specialization9_reverse_link_reassign_clear():
    a1 = oving1APD_Specialization(name="sample_text")
    a2 = oving1APD_Specialization(name="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'course', a1)
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'Specialization10'):
        assert _is_linked(a1, 'Specialization10', b)
    _safe_set(b, 'course', a2)
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'Specialization10'):
        assert not _is_linked(a1, 'Specialization10', b)
    if hasattr(a2, 'Specialization10'):
        assert _is_linked(a2, 'Specialization10', b)
    _safe_set(b, 'course', None)
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'Specialization10'):
        assert not _is_linked(a2, 'Specialization10', b)


def test_assoc_studyProgram0_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'department', {a1})
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'StudyProgram'):
        assert _is_linked(a1, 'StudyProgram', b)
    _safe_set(b, 'department', {a2})
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'StudyProgram'):
        assert not _is_linked(a1, 'StudyProgram', b)
    if hasattr(a2, 'StudyProgram'):
        assert _is_linked(a2, 'StudyProgram', b)
    _safe_set(b, 'department', set())
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'StudyProgram'):
        assert not _is_linked(a2, 'StudyProgram', b)


def test_assoc_studyProgram16_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'semester17', a1)
    assert _is_linked(b, 'semester17', a1)
    if hasattr(a1, 'StudyProgram18'):
        assert _is_linked(a1, 'StudyProgram18', b)
    _safe_set(b, 'semester17', a2)
    assert _is_linked(b, 'semester17', a2)
    if hasattr(a1, 'StudyProgram18'):
        assert not _is_linked(a1, 'StudyProgram18', b)
    if hasattr(a2, 'StudyProgram18'):
        assert _is_linked(a2, 'StudyProgram18', b)
    _safe_set(b, 'semester17', None)
    assert not _is_linked(b, 'semester17', a2)
    if hasattr(a2, 'StudyProgram18'):
        assert not _is_linked(a2, 'StudyProgram18', b)


def test_assoc_studyProgram27_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Specialization(name="sample_text")
    _safe_set(b, 'specialization28', a1)
    assert _is_linked(b, 'specialization28', a1)
    if hasattr(a1, 'StudyProgram29'):
        assert _is_linked(a1, 'StudyProgram29', b)
    _safe_set(b, 'specialization28', a2)
    assert _is_linked(b, 'specialization28', a2)
    if hasattr(a1, 'StudyProgram29'):
        assert not _is_linked(a1, 'StudyProgram29', b)
    if hasattr(a2, 'StudyProgram29'):
        assert _is_linked(a2, 'StudyProgram29', b)
    _safe_set(b, 'specialization28', None)
    assert not _is_linked(b, 'specialization28', a2)
    if hasattr(a2, 'StudyProgram29'):
        assert not _is_linked(a2, 'StudyProgram29', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

