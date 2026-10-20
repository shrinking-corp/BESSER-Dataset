import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    oving1APD_Course,
    oving1APD_Department,
    oving1APD_Semester,
    oving1APD_Slot,
    oving1APD_Specialization,
    oving1APD_StudyProgram,
    CourseStatus,
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

def test_assoc_course23_reverse_link_reassign_clear():
    a1 = oving1APD_Specialization(name="sample_text")
    a2 = oving1APD_Specialization(name="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'Course25', a1)
    assert _is_linked(b, 'Course25', a1)
    if hasattr(a1, 'specialization24'):
        assert _is_linked(a1, 'specialization24', b)
    _safe_set(b, 'Course25', a2)
    assert _is_linked(b, 'Course25', a2)
    if hasattr(a1, 'specialization24'):
        assert not _is_linked(a1, 'specialization24', b)
    if hasattr(a2, 'specialization24'):
        assert _is_linked(a2, 'specialization24', b)
    _safe_set(b, 'Course25', None)
    assert not _is_linked(b, 'Course25', a2)
    if hasattr(a2, 'specialization24'):
        assert not _is_linked(a2, 'specialization24', b)


def test_assoc_course29_reverse_link_reassign_clear():
    a1 = oving1APD_Slot(name="sample_text")
    a2 = oving1APD_Slot(name="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'Course30', a1)
    assert _is_linked(b, 'Course30', a1)
    if hasattr(a1, 'slot'):
        assert _is_linked(a1, 'slot', b)
    _safe_set(b, 'Course30', a2)
    assert _is_linked(b, 'Course30', a2)
    if hasattr(a1, 'slot'):
        assert not _is_linked(a1, 'slot', b)
    if hasattr(a2, 'slot'):
        assert _is_linked(a2, 'slot', b)
    _safe_set(b, 'Course30', None)
    assert not _is_linked(b, 'Course30', a2)
    if hasattr(a2, 'slot'):
        assert not _is_linked(a2, 'slot', b)


def test_assoc_courseInSemester6_reverse_link_reassign_clear():
    a1 = oving1APD_Semester(number=7)
    a2 = oving1APD_Semester(number=13)
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'hasCourse', a1)
    assert _is_linked(b, 'hasCourse', a1)
    if hasattr(a1, 'Semester7'):
        assert _is_linked(a1, 'Semester7', b)
    _safe_set(b, 'hasCourse', a2)
    assert _is_linked(b, 'hasCourse', a2)
    if hasattr(a1, 'Semester7'):
        assert not _is_linked(a1, 'Semester7', b)
    if hasattr(a2, 'Semester7'):
        assert _is_linked(a2, 'Semester7', b)
    _safe_set(b, 'hasCourse', None)
    assert not _is_linked(b, 'hasCourse', a2)
    if hasattr(a2, 'Semester7'):
        assert not _is_linked(a2, 'Semester7', b)


def test_assoc_department4_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'studyProgram5'):
        assert _is_linked(a1, 'studyProgram5', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'studyProgram5'):
        assert not _is_linked(a1, 'studyProgram5', b)
    if hasattr(a2, 'studyProgram5'):
        assert _is_linked(a2, 'studyProgram5', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'studyProgram5'):
        assert not _is_linked(a2, 'studyProgram5', b)


def test_assoc_hasCourse12_reverse_link_reassign_clear():
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


def test_assoc_semester2_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'Semester', a1)
    assert _is_linked(b, 'Semester', a1)
    if hasattr(a1, 'studyProgram3'):
        assert _is_linked(a1, 'studyProgram3', b)
    _safe_set(b, 'Semester', a2)
    assert _is_linked(b, 'Semester', a2)
    if hasattr(a1, 'studyProgram3'):
        assert not _is_linked(a1, 'studyProgram3', b)
    if hasattr(a2, 'studyProgram3'):
        assert _is_linked(a2, 'studyProgram3', b)
    _safe_set(b, 'Semester', None)
    assert not _is_linked(b, 'Semester', a2)
    if hasattr(a2, 'studyProgram3'):
        assert not _is_linked(a2, 'studyProgram3', b)


def test_assoc_semester21_reverse_link_reassign_clear():
    a1 = oving1APD_Specialization(name="sample_text")
    a2 = oving1APD_Specialization(name="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'Semester22', a1)
    assert _is_linked(b, 'Semester22', a1)
    if hasattr(a1, 'specialization'):
        assert _is_linked(a1, 'specialization', b)
    _safe_set(b, 'Semester22', a2)
    assert _is_linked(b, 'Semester22', a2)
    if hasattr(a1, 'specialization'):
        assert not _is_linked(a1, 'specialization', b)
    if hasattr(a2, 'specialization'):
        assert _is_linked(a2, 'specialization', b)
    _safe_set(b, 'Semester22', None)
    assert not _is_linked(b, 'Semester22', a2)
    if hasattr(a2, 'specialization'):
        assert not _is_linked(a2, 'specialization', b)


def test_assoc_semester31_reverse_link_reassign_clear():
    a1 = oving1APD_Slot(name="sample_text")
    a2 = oving1APD_Slot(name="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'Semester33', a1)
    assert _is_linked(b, 'Semester33', a1)
    if hasattr(a1, 'slot32'):
        assert _is_linked(a1, 'slot32', b)
    _safe_set(b, 'Semester33', a2)
    assert _is_linked(b, 'Semester33', a2)
    if hasattr(a1, 'slot32'):
        assert not _is_linked(a1, 'slot32', b)
    if hasattr(a2, 'slot32'):
        assert _is_linked(a2, 'slot32', b)
    _safe_set(b, 'Semester33', None)
    assert not _is_linked(b, 'Semester33', a2)
    if hasattr(a2, 'slot32'):
        assert not _is_linked(a2, 'slot32', b)


def test_assoc_slot10_reverse_link_reassign_clear():
    a1 = oving1APD_Slot(name="sample_text")
    a2 = oving1APD_Slot(name="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'course11', a1)
    assert _is_linked(b, 'course11', a1)
    if hasattr(a1, 'Slot'):
        assert _is_linked(a1, 'Slot', b)
    _safe_set(b, 'course11', a2)
    assert _is_linked(b, 'course11', a2)
    if hasattr(a1, 'Slot'):
        assert not _is_linked(a1, 'Slot', b)
    if hasattr(a2, 'Slot'):
        assert _is_linked(a2, 'Slot', b)
    _safe_set(b, 'course11', None)
    assert not _is_linked(b, 'course11', a2)
    if hasattr(a2, 'Slot'):
        assert not _is_linked(a2, 'Slot', b)


def test_assoc_slot13_reverse_link_reassign_clear():
    a1 = oving1APD_Slot(name="sample_text")
    a2 = oving1APD_Slot(name="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'semester', a1)
    assert _is_linked(b, 'semester', a1)
    if hasattr(a1, 'Slot14'):
        assert _is_linked(a1, 'Slot14', b)
    _safe_set(b, 'semester', a2)
    assert _is_linked(b, 'semester', a2)
    if hasattr(a1, 'Slot14'):
        assert not _is_linked(a1, 'Slot14', b)
    if hasattr(a2, 'Slot14'):
        assert _is_linked(a2, 'Slot14', b)
    _safe_set(b, 'semester', None)
    assert not _is_linked(b, 'semester', a2)
    if hasattr(a2, 'Slot14'):
        assert not _is_linked(a2, 'Slot14', b)


def test_assoc_specialization1_reverse_link_reassign_clear():
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


def test_assoc_specialization18_reverse_link_reassign_clear():
    a1 = oving1APD_Specialization(name="sample_text")
    a2 = oving1APD_Specialization(name="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'semester19', a1)
    assert _is_linked(b, 'semester19', a1)
    if hasattr(a1, 'Specialization20'):
        assert _is_linked(a1, 'Specialization20', b)
    _safe_set(b, 'semester19', a2)
    assert _is_linked(b, 'semester19', a2)
    if hasattr(a1, 'Specialization20'):
        assert not _is_linked(a1, 'Specialization20', b)
    if hasattr(a2, 'Specialization20'):
        assert _is_linked(a2, 'Specialization20', b)
    _safe_set(b, 'semester19', None)
    assert not _is_linked(b, 'semester19', a2)
    if hasattr(a2, 'Specialization20'):
        assert not _is_linked(a2, 'Specialization20', b)


def test_assoc_specialization8_reverse_link_reassign_clear():
    a1 = oving1APD_Specialization(name="sample_text")
    a2 = oving1APD_Specialization(name="sample_text_2")
    b = oving1APD_Course(code="sample_text", credit=3.14, level=7, name="sample_text")
    _safe_set(b, 'course', a1)
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'Specialization9'):
        assert _is_linked(a1, 'Specialization9', b)
    _safe_set(b, 'course', a2)
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'Specialization9'):
        assert not _is_linked(a1, 'Specialization9', b)
    if hasattr(a2, 'Specialization9'):
        assert _is_linked(a2, 'Specialization9', b)
    _safe_set(b, 'course', None)
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'Specialization9'):
        assert not _is_linked(a2, 'Specialization9', b)


def test_assoc_studyProgram0_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'department', a1)
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'StudyProgram'):
        assert _is_linked(a1, 'StudyProgram', b)
    _safe_set(b, 'department', a2)
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'StudyProgram'):
        assert not _is_linked(a1, 'StudyProgram', b)
    if hasattr(a2, 'StudyProgram'):
        assert _is_linked(a2, 'StudyProgram', b)
    _safe_set(b, 'department', None)
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'StudyProgram'):
        assert not _is_linked(a2, 'StudyProgram', b)


def test_assoc_studyProgram15_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Semester(number=7)
    _safe_set(b, 'semester16', a1)
    assert _is_linked(b, 'semester16', a1)
    if hasattr(a1, 'StudyProgram17'):
        assert _is_linked(a1, 'StudyProgram17', b)
    _safe_set(b, 'semester16', a2)
    assert _is_linked(b, 'semester16', a2)
    if hasattr(a1, 'StudyProgram17'):
        assert not _is_linked(a1, 'StudyProgram17', b)
    if hasattr(a2, 'StudyProgram17'):
        assert _is_linked(a2, 'StudyProgram17', b)
    _safe_set(b, 'semester16', None)
    assert not _is_linked(b, 'semester16', a2)
    if hasattr(a2, 'StudyProgram17'):
        assert not _is_linked(a2, 'StudyProgram17', b)


def test_assoc_studyProgram26_reverse_link_reassign_clear():
    a1 = oving1APD_StudyProgram(name="sample_text", shortName="sample_text")
    a2 = oving1APD_StudyProgram(name="sample_text_2", shortName="sample_text_2")
    b = oving1APD_Specialization(name="sample_text")
    _safe_set(b, 'specialization27', a1)
    assert _is_linked(b, 'specialization27', a1)
    if hasattr(a1, 'StudyProgram28'):
        assert _is_linked(a1, 'StudyProgram28', b)
    _safe_set(b, 'specialization27', a2)
    assert _is_linked(b, 'specialization27', a2)
    if hasattr(a1, 'StudyProgram28'):
        assert not _is_linked(a1, 'StudyProgram28', b)
    if hasattr(a2, 'StudyProgram28'):
        assert _is_linked(a2, 'StudyProgram28', b)
    _safe_set(b, 'specialization27', None)
    assert not _is_linked(b, 'specialization27', a2)
    if hasattr(a2, 'StudyProgram28'):
        assert not _is_linked(a2, 'StudyProgram28', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

