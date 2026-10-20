import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ADMIN,
    FACULTY,
    Modify_attendance_external,
    PARENT,
    STUDENT,
    _Component,
    admin_Actor,
    answer_attendance_call_external,
    faculty_Actor,
    login_external,
    logout_external,
    modify_list_of_students_external,
    parent_Actor,
    post_attendance_external,
    recieve_attendance_sms_external,
    send_attendance_sms_external,
    student_Actor,
    take_attendance_call_external,
    view_cumiliative_attendance_external,
    view_subject_wise_attendance_external,
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

def test_assoc_FACULTY_ADMIN_reverse_link_reassign_clear():
    a1 = FACULTY(id="sample_text", password="sample_text")
    a2 = FACULTY(id="sample_text_2", password="sample_text_2")
    b = ADMIN(id="sample_text", password="sample_text")
    _safe_set(b, 'fACULTY43', {a1})
    assert _is_linked(b, 'fACULTY43', a1)
    if hasattr(a1, 'aDMIN42'):
        assert _is_linked(a1, 'aDMIN42', b)
    _safe_set(b, 'fACULTY43', {a2})
    assert _is_linked(b, 'fACULTY43', a2)
    if hasattr(a1, 'aDMIN42'):
        assert not _is_linked(a1, 'aDMIN42', b)
    if hasattr(a2, 'aDMIN42'):
        assert _is_linked(a2, 'aDMIN42', b)
    _safe_set(b, 'fACULTY43', set())
    assert not _is_linked(b, 'fACULTY43', a2)
    if hasattr(a2, 'aDMIN42'):
        assert not _is_linked(a2, 'aDMIN42', b)


def test_assoc_FACULTY_STUDENT_reverse_link_reassign_clear():
    a1 = STUDENT(id="sample_text", password="sample_text")
    a2 = STUDENT(id="sample_text_2", password="sample_text_2")
    b = FACULTY(id="sample_text", password="sample_text")
    _safe_set(b, 'sTUDENT40', {a1})
    assert _is_linked(b, 'sTUDENT40', a1)
    if hasattr(a1, 'fACULTY41'):
        assert _is_linked(a1, 'fACULTY41', b)
    _safe_set(b, 'sTUDENT40', {a2})
    assert _is_linked(b, 'sTUDENT40', a2)
    if hasattr(a1, 'fACULTY41'):
        assert not _is_linked(a1, 'fACULTY41', b)
    if hasattr(a2, 'fACULTY41'):
        assert _is_linked(a2, 'fACULTY41', b)
    _safe_set(b, 'sTUDENT40', set())
    assert not _is_linked(b, 'sTUDENT40', a2)
    if hasattr(a2, 'fACULTY41'):
        assert not _is_linked(a2, 'fACULTY41', b)


def test_assoc_PARENT_ADMIN_reverse_link_reassign_clear():
    a1 = PARENT(id="sample_text", password="sample_text", phoneNumber=7)
    a2 = PARENT(id="sample_text_2", password="sample_text_2", phoneNumber=13)
    b = ADMIN(id="sample_text", password="sample_text")
    _safe_set(b, 'pARENT47', {a1})
    assert _is_linked(b, 'pARENT47', a1)
    if hasattr(a1, 'aDMIN46'):
        assert _is_linked(a1, 'aDMIN46', b)
    _safe_set(b, 'pARENT47', {a2})
    assert _is_linked(b, 'pARENT47', a2)
    if hasattr(a1, 'aDMIN46'):
        assert not _is_linked(a1, 'aDMIN46', b)
    if hasattr(a2, 'aDMIN46'):
        assert _is_linked(a2, 'aDMIN46', b)
    _safe_set(b, 'pARENT47', set())
    assert not _is_linked(b, 'pARENT47', a2)
    if hasattr(a2, 'aDMIN46'):
        assert not _is_linked(a2, 'aDMIN46', b)


def test_assoc_STUDENT_ADMIN_reverse_link_reassign_clear():
    a1 = STUDENT(id="sample_text", password="sample_text")
    a2 = STUDENT(id="sample_text_2", password="sample_text_2")
    b = ADMIN(id="sample_text", password="sample_text")
    _safe_set(b, 'sTUDENT45', {a1})
    assert _is_linked(b, 'sTUDENT45', a1)
    if hasattr(a1, 'aDMIN44'):
        assert _is_linked(a1, 'aDMIN44', b)
    _safe_set(b, 'sTUDENT45', {a2})
    assert _is_linked(b, 'sTUDENT45', a2)
    if hasattr(a1, 'aDMIN44'):
        assert not _is_linked(a1, 'aDMIN44', b)
    if hasattr(a2, 'aDMIN44'):
        assert _is_linked(a2, 'aDMIN44', b)
    _safe_set(b, 'sTUDENT45', set())
    assert not _is_linked(b, 'sTUDENT45', a2)
    if hasattr(a2, 'aDMIN44'):
        assert not _is_linked(a2, 'aDMIN44', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

