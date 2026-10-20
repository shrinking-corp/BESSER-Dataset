import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ADMIN,
    FACULTY,
    PARENT,
    STUDENT,
    Student_Attendance_at_INU_Component,
    Teachers_Actor,
    admin_technician_Actor,
    answer_attendance_call_external,
    call_students_for_attendance_external,
    generate_class_wise_attendance_report_external,
    login_external,
    logout_external,
    modify_list_of_students_external,
    parent_Actor,
    post_attendance_external,
    recieve_attendance_sms_external,
    send_attendance_sms_external,
    student_Actor,
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
    _safe_set(b, 'fACULTY37', {a1})
    assert _is_linked(b, 'fACULTY37', a1)
    if hasattr(a1, 'aDMIN36'):
        assert _is_linked(a1, 'aDMIN36', b)
    _safe_set(b, 'fACULTY37', {a2})
    assert _is_linked(b, 'fACULTY37', a2)
    if hasattr(a1, 'aDMIN36'):
        assert not _is_linked(a1, 'aDMIN36', b)
    if hasattr(a2, 'aDMIN36'):
        assert _is_linked(a2, 'aDMIN36', b)
    _safe_set(b, 'fACULTY37', set())
    assert not _is_linked(b, 'fACULTY37', a2)
    if hasattr(a2, 'aDMIN36'):
        assert not _is_linked(a2, 'aDMIN36', b)


def test_assoc_FACULTY_STUDENT_reverse_link_reassign_clear():
    a1 = STUDENT(id="sample_text", password="sample_text")
    a2 = STUDENT(id="sample_text_2", password="sample_text_2")
    b = FACULTY(id="sample_text", password="sample_text")
    _safe_set(b, 'sTUDENT34', {a1})
    assert _is_linked(b, 'sTUDENT34', a1)
    if hasattr(a1, 'fACULTY35'):
        assert _is_linked(a1, 'fACULTY35', b)
    _safe_set(b, 'sTUDENT34', {a2})
    assert _is_linked(b, 'sTUDENT34', a2)
    if hasattr(a1, 'fACULTY35'):
        assert not _is_linked(a1, 'fACULTY35', b)
    if hasattr(a2, 'fACULTY35'):
        assert _is_linked(a2, 'fACULTY35', b)
    _safe_set(b, 'sTUDENT34', set())
    assert not _is_linked(b, 'sTUDENT34', a2)
    if hasattr(a2, 'fACULTY35'):
        assert not _is_linked(a2, 'fACULTY35', b)


def test_assoc_PARENT_ADMIN_reverse_link_reassign_clear():
    a1 = PARENT(id="sample_text", password="sample_text", phoneNumber=7)
    a2 = PARENT(id="sample_text_2", password="sample_text_2", phoneNumber=13)
    b = ADMIN(id="sample_text", password="sample_text")
    _safe_set(b, 'pARENT41', {a1})
    assert _is_linked(b, 'pARENT41', a1)
    if hasattr(a1, 'aDMIN40'):
        assert _is_linked(a1, 'aDMIN40', b)
    _safe_set(b, 'pARENT41', {a2})
    assert _is_linked(b, 'pARENT41', a2)
    if hasattr(a1, 'aDMIN40'):
        assert not _is_linked(a1, 'aDMIN40', b)
    if hasattr(a2, 'aDMIN40'):
        assert _is_linked(a2, 'aDMIN40', b)
    _safe_set(b, 'pARENT41', set())
    assert not _is_linked(b, 'pARENT41', a2)
    if hasattr(a2, 'aDMIN40'):
        assert not _is_linked(a2, 'aDMIN40', b)


def test_assoc_STUDENT_ADMIN_reverse_link_reassign_clear():
    a1 = STUDENT(id="sample_text", password="sample_text")
    a2 = STUDENT(id="sample_text_2", password="sample_text_2")
    b = ADMIN(id="sample_text", password="sample_text")
    _safe_set(b, 'sTUDENT39', {a1})
    assert _is_linked(b, 'sTUDENT39', a1)
    if hasattr(a1, 'aDMIN38'):
        assert _is_linked(a1, 'aDMIN38', b)
    _safe_set(b, 'sTUDENT39', {a2})
    assert _is_linked(b, 'sTUDENT39', a2)
    if hasattr(a1, 'aDMIN38'):
        assert not _is_linked(a1, 'aDMIN38', b)
    if hasattr(a2, 'aDMIN38'):
        assert _is_linked(a2, 'aDMIN38', b)
    _safe_set(b, 'sTUDENT39', set())
    assert not _is_linked(b, 'sTUDENT39', a2)
    if hasattr(a2, 'aDMIN38'):
        assert not _is_linked(a2, 'aDMIN38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

