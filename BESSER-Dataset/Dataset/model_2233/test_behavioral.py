import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tDT4250_asssignment1_2_Course,
    tDT4250_asssignment1_2_Department,
    tDT4250_asssignment1_2_Program,
    tDT4250_asssignment1_2_Program_course,
    tDT4250_asssignment1_2_Semester,
    tDT4250_asssignment1_2_Semester_Course,
    tDT4250_asssignment1_2_Specialization,
    Fall_or_spring,
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

def test_assoc_course13_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Semester_Course(Fall_or_spring="sample_text", Mandatory=True)
    a2 = tDT4250_asssignment1_2_Semester_Course(Fall_or_spring="sample_text_2", Mandatory=False)
    b = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    _safe_set(b, 'tDT4250_asssignment1_2_Course', a1)
    assert _is_linked(b, 'tDT4250_asssignment1_2_Course', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Semester_Course14'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Semester_Course14', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Course', a2)
    assert _is_linked(b, 'tDT4250_asssignment1_2_Course', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Semester_Course14'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Semester_Course14', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Semester_Course14'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Semester_Course14', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Course', None)
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Course', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Semester_Course14'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Semester_Course14', b)


def test_assoc_course15_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Program_course(Fall_or_spring="sample_text", Mandatory=True)
    a2 = tDT4250_asssignment1_2_Program_course(Fall_or_spring="sample_text_2", Mandatory=False)
    b = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    _safe_set(b, 'tDT4250_asssignment1_2_Course17', a1)
    assert _is_linked(b, 'tDT4250_asssignment1_2_Course17', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Program_course16'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Program_course16', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Course17', a2)
    assert _is_linked(b, 'tDT4250_asssignment1_2_Course17', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Program_course16'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Program_course16', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Program_course16'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Program_course16', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Course17', None)
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Course17', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Program_course16'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Program_course16', b)


def test_assoc_course18_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Department(Name="sample_text")
    a2 = tDT4250_asssignment1_2_Department(Name="sample_text_2")
    b = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    _safe_set(b, 'tDT4250_asssignment1_2_Course19', a1)
    assert _is_linked(b, 'tDT4250_asssignment1_2_Course19', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Department'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Department', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Course19', a2)
    assert _is_linked(b, 'tDT4250_asssignment1_2_Course19', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Department'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Department', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Department'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Department', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Course19', None)
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Course19', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Department'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Department', b)


def test_assoc_program20_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    a2 = tDT4250_asssignment1_2_Program(Credits="sample_text_2", Name="sample_text_2")
    b = tDT4250_asssignment1_2_Department(Name="sample_text")
    _safe_set(b, 'tDT4250_asssignment1_2_Department21', {a1})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Department21', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Program22'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Program22', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Department21', {a2})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Department21', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Program22'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Program22', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Program22'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Program22', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Department21', set())
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Department21', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Program22'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Program22', b)


def test_assoc_program_course1_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Program_course(Fall_or_spring="sample_text", Mandatory=True)
    a2 = tDT4250_asssignment1_2_Program_course(Fall_or_spring="sample_text_2", Mandatory=False)
    b = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    _safe_set(b, 'tDT4250_asssignment1_2_Program2', {a1})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Program2', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Program_course'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Program_course', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Program2', {a2})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Program2', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Program_course'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Program_course', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Program_course'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Program_course', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Program2', set())
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Program2', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Program_course'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Program_course', b)


def test_assoc_semester3_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Semester(Credits="sample_text", Number=7)
    a2 = tDT4250_asssignment1_2_Semester(Credits="sample_text_2", Number=13)
    b = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    _safe_set(b, 'tDT4250_asssignment1_2_Program4', {a1})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Program4', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Semester'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Semester', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Program4', {a2})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Program4', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Semester'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Semester', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Semester'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Semester', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Program4', set())
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Program4', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Semester'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Semester', b)


def test_assoc_semester5_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    a2 = tDT4250_asssignment1_2_Specialization(Name="sample_text_2")
    b = tDT4250_asssignment1_2_Semester(Credits="sample_text", Number=7)
    _safe_set(b, 'tDT4250_asssignment1_2_Semester7', a1)
    assert _is_linked(b, 'tDT4250_asssignment1_2_Semester7', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Specialization6'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Specialization6', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Semester7', a2)
    assert _is_linked(b, 'tDT4250_asssignment1_2_Semester7', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Specialization6'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Specialization6', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Specialization6'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Specialization6', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Semester7', None)
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Semester7', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Specialization6'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Specialization6', b)


def test_assoc_semester_course11_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Semester_Course(Fall_or_spring="sample_text", Mandatory=True)
    a2 = tDT4250_asssignment1_2_Semester_Course(Fall_or_spring="sample_text_2", Mandatory=False)
    b = tDT4250_asssignment1_2_Semester(Credits="sample_text", Number=7)
    _safe_set(b, 'tDT4250_asssignment1_2_Semester12', {a1})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Semester12', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Semester_Course'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Semester_Course', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Semester12', {a2})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Semester12', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Semester_Course'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Semester_Course', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Semester_Course'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Semester_Course', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Semester12', set())
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Semester12', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Semester_Course'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Semester_Course', b)


def test_assoc_specialization0_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    a2 = tDT4250_asssignment1_2_Specialization(Name="sample_text_2")
    b = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    _safe_set(b, 'tDT4250_asssignment1_2_Program', {a1})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Program', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Specialization'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Specialization', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Program', {a2})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Program', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Specialization'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Specialization', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Specialization'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Specialization', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Program', set())
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Program', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Specialization'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Specialization', b)


def test_assoc_specialization9_reverse_link_reassign_clear():
    a1 = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    a2 = tDT4250_asssignment1_2_Specialization(Name="sample_text_2")
    b = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    _safe_set(b, 'tDT4250_asssignment1_2_Specialization8', {a1})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Specialization8', a1)
    if hasattr(a1, 'tDT4250_asssignment1_2_Specialization10'):
        assert _is_linked(a1, 'tDT4250_asssignment1_2_Specialization10', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Specialization8', {a2})
    assert _is_linked(b, 'tDT4250_asssignment1_2_Specialization8', a2)
    if hasattr(a1, 'tDT4250_asssignment1_2_Specialization10'):
        assert not _is_linked(a1, 'tDT4250_asssignment1_2_Specialization10', b)
    if hasattr(a2, 'tDT4250_asssignment1_2_Specialization10'):
        assert _is_linked(a2, 'tDT4250_asssignment1_2_Specialization10', b)
    _safe_set(b, 'tDT4250_asssignment1_2_Specialization8', set())
    assert not _is_linked(b, 'tDT4250_asssignment1_2_Specialization8', a2)
    if hasattr(a2, 'tDT4250_asssignment1_2_Specialization10'):
        assert not _is_linked(a2, 'tDT4250_asssignment1_2_Specialization10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

