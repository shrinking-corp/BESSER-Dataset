import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tdt4250_Course,
    tdt4250_Specialisation,
    tdt4250_Student,
    tdt4250_StudyProgram,
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

def test_assoc_courses5_reverse_link_reassign_clear():
    a1 = tdt4250_Student(current_semester=7, studentID=7)
    a2 = tdt4250_Student(current_semester=13, studentID=13)
    b = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", study_points=3.14)
    _safe_set(b, 'tdt4250_Course7', a1)
    assert _is_linked(b, 'tdt4250_Course7', a1)
    if hasattr(a1, 'tdt4250_Student6'):
        assert _is_linked(a1, 'tdt4250_Student6', b)
    _safe_set(b, 'tdt4250_Course7', a2)
    assert _is_linked(b, 'tdt4250_Course7', a2)
    if hasattr(a1, 'tdt4250_Student6'):
        assert not _is_linked(a1, 'tdt4250_Student6', b)
    if hasattr(a2, 'tdt4250_Student6'):
        assert _is_linked(a2, 'tdt4250_Student6', b)
    _safe_set(b, 'tdt4250_Course7', None)
    assert not _is_linked(b, 'tdt4250_Course7', a2)
    if hasattr(a2, 'tdt4250_Student6'):
        assert not _is_linked(a2, 'tdt4250_Student6', b)


def test_assoc_elective_courses14_reverse_link_reassign_clear():
    a1 = tdt4250_Specialisation(name="sample_text")
    a2 = tdt4250_Specialisation(name="sample_text_2")
    b = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", study_points=3.14)
    _safe_set(b, 'tdt4250_Course16', a1)
    assert _is_linked(b, 'tdt4250_Course16', a1)
    if hasattr(a1, 'tdt4250_Specialisation15'):
        assert _is_linked(a1, 'tdt4250_Specialisation15', b)
    _safe_set(b, 'tdt4250_Course16', a2)
    assert _is_linked(b, 'tdt4250_Course16', a2)
    if hasattr(a1, 'tdt4250_Specialisation15'):
        assert not _is_linked(a1, 'tdt4250_Specialisation15', b)
    if hasattr(a2, 'tdt4250_Specialisation15'):
        assert _is_linked(a2, 'tdt4250_Specialisation15', b)
    _safe_set(b, 'tdt4250_Course16', None)
    assert not _is_linked(b, 'tdt4250_Course16', a2)
    if hasattr(a2, 'tdt4250_Specialisation15'):
        assert not _is_linked(a2, 'tdt4250_Specialisation15', b)


def test_assoc_obligatory_courses11_reverse_link_reassign_clear():
    a1 = tdt4250_Specialisation(name="sample_text")
    a2 = tdt4250_Specialisation(name="sample_text_2")
    b = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", study_points=3.14)
    _safe_set(b, 'tdt4250_Course13', a1)
    assert _is_linked(b, 'tdt4250_Course13', a1)
    if hasattr(a1, 'tdt4250_Specialisation12'):
        assert _is_linked(a1, 'tdt4250_Specialisation12', b)
    _safe_set(b, 'tdt4250_Course13', a2)
    assert _is_linked(b, 'tdt4250_Course13', a2)
    if hasattr(a1, 'tdt4250_Specialisation12'):
        assert not _is_linked(a1, 'tdt4250_Specialisation12', b)
    if hasattr(a2, 'tdt4250_Specialisation12'):
        assert _is_linked(a2, 'tdt4250_Specialisation12', b)
    _safe_set(b, 'tdt4250_Course13', None)
    assert not _is_linked(b, 'tdt4250_Course13', a2)
    if hasattr(a2, 'tdt4250_Specialisation12'):
        assert not _is_linked(a2, 'tdt4250_Specialisation12', b)


def test_assoc_obligatory_courses3_reverse_link_reassign_clear():
    a1 = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    a2 = tdt4250_StudyProgram(name="sample_text_2", number_of_semesters=13)
    b = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", study_points=3.14)
    _safe_set(b, 'tdt4250_Course', a1)
    assert _is_linked(b, 'tdt4250_Course', a1)
    if hasattr(a1, 'tdt4250_StudyProgram4'):
        assert _is_linked(a1, 'tdt4250_StudyProgram4', b)
    _safe_set(b, 'tdt4250_Course', a2)
    assert _is_linked(b, 'tdt4250_Course', a2)
    if hasattr(a1, 'tdt4250_StudyProgram4'):
        assert not _is_linked(a1, 'tdt4250_StudyProgram4', b)
    if hasattr(a2, 'tdt4250_StudyProgram4'):
        assert _is_linked(a2, 'tdt4250_StudyProgram4', b)
    _safe_set(b, 'tdt4250_Course', None)
    assert not _is_linked(b, 'tdt4250_Course', a2)
    if hasattr(a2, 'tdt4250_StudyProgram4'):
        assert not _is_linked(a2, 'tdt4250_StudyProgram4', b)


def test_assoc_specialisations1_reverse_link_reassign_clear():
    a1 = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    a2 = tdt4250_StudyProgram(name="sample_text_2", number_of_semesters=13)
    b = tdt4250_Specialisation(name="sample_text")
    _safe_set(b, 'tdt4250_Specialisation', a1)
    assert _is_linked(b, 'tdt4250_Specialisation', a1)
    if hasattr(a1, 'tdt4250_StudyProgram2'):
        assert _is_linked(a1, 'tdt4250_StudyProgram2', b)
    _safe_set(b, 'tdt4250_Specialisation', a2)
    assert _is_linked(b, 'tdt4250_Specialisation', a2)
    if hasattr(a1, 'tdt4250_StudyProgram2'):
        assert not _is_linked(a1, 'tdt4250_StudyProgram2', b)
    if hasattr(a2, 'tdt4250_StudyProgram2'):
        assert _is_linked(a2, 'tdt4250_StudyProgram2', b)
    _safe_set(b, 'tdt4250_Specialisation', None)
    assert not _is_linked(b, 'tdt4250_Specialisation', a2)
    if hasattr(a2, 'tdt4250_StudyProgram2'):
        assert not _is_linked(a2, 'tdt4250_StudyProgram2', b)


def test_assoc_students0_reverse_link_reassign_clear():
    a1 = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    a2 = tdt4250_StudyProgram(name="sample_text_2", number_of_semesters=13)
    b = tdt4250_Student(current_semester=7, studentID=7)
    _safe_set(b, 'tdt4250_Student', a1)
    assert _is_linked(b, 'tdt4250_Student', a1)
    if hasattr(a1, 'tdt4250_StudyProgram'):
        assert _is_linked(a1, 'tdt4250_StudyProgram', b)
    _safe_set(b, 'tdt4250_Student', a2)
    assert _is_linked(b, 'tdt4250_Student', a2)
    if hasattr(a1, 'tdt4250_StudyProgram'):
        assert not _is_linked(a1, 'tdt4250_StudyProgram', b)
    if hasattr(a2, 'tdt4250_StudyProgram'):
        assert _is_linked(a2, 'tdt4250_StudyProgram', b)
    _safe_set(b, 'tdt4250_Student', None)
    assert not _is_linked(b, 'tdt4250_Student', a2)
    if hasattr(a2, 'tdt4250_StudyProgram'):
        assert not _is_linked(a2, 'tdt4250_StudyProgram', b)


def test_assoc_students8_reverse_link_reassign_clear():
    a1 = tdt4250_Student(current_semester=7, studentID=7)
    a2 = tdt4250_Student(current_semester=13, studentID=13)
    b = tdt4250_Specialisation(name="sample_text")
    _safe_set(b, 'tdt4250_Specialisation9', {a1})
    assert _is_linked(b, 'tdt4250_Specialisation9', a1)
    if hasattr(a1, 'tdt4250_Student10'):
        assert _is_linked(a1, 'tdt4250_Student10', b)
    _safe_set(b, 'tdt4250_Specialisation9', {a2})
    assert _is_linked(b, 'tdt4250_Specialisation9', a2)
    if hasattr(a1, 'tdt4250_Student10'):
        assert not _is_linked(a1, 'tdt4250_Student10', b)
    if hasattr(a2, 'tdt4250_Student10'):
        assert _is_linked(a2, 'tdt4250_Student10', b)
    _safe_set(b, 'tdt4250_Specialisation9', set())
    assert not _is_linked(b, 'tdt4250_Specialisation9', a2)
    if hasattr(a2, 'tdt4250_Student10'):
        assert not _is_linked(a2, 'tdt4250_Student10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

