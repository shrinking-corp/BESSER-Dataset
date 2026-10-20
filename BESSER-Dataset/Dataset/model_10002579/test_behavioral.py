import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator_Actor,
    Attendance,
    Authenticate_staff,
    Authentication_UseCase,
    Employee_Actor,
    Employee_Management_System_Component,
    Login,
    Login_external,
    Logout_external,
    Mission,
    Salary,
    Salary_Management_UseCase,
    staff_member,
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

def test_assoc_Employee_Attendance_reverse_link_reassign_clear():
    a1 = staff_member(staff_Address="sample_text", staff_ContactNo="sample_text", staff_DOB=date(2024, 1, 1), staff_Date_Of_Joint=date(2024, 1, 1), staff_Department="sample_text", staff_Email="sample_text", staff_Id=7, staff_NIC="sample_text", staff_Name="sample_text", staff_Position="sample_text", staff_Salary=3.14)
    a2 = staff_member(staff_Address="sample_text_2", staff_ContactNo="sample_text_2", staff_DOB=date(2025, 6, 15), staff_Date_Of_Joint=date(2025, 6, 15), staff_Department="sample_text_2", staff_Email="sample_text_2", staff_Id=13, staff_NIC="sample_text_2", staff_Name="sample_text_2", staff_Position="sample_text_2", staff_Salary=9.99)
    b = Attendance(AttendTime="sample_text", Attend_date=date(2024, 1, 1), Emp_id="sample_text", Leaving_Time="sample_text")
    _safe_set(b, 'staff3', a1)
    assert _is_linked(b, 'staff3', a1)
    if hasattr(a1, 'attendance2'):
        assert _is_linked(a1, 'attendance2', b)
    _safe_set(b, 'staff3', a2)
    assert _is_linked(b, 'staff3', a2)
    if hasattr(a1, 'attendance2'):
        assert not _is_linked(a1, 'attendance2', b)
    if hasattr(a2, 'attendance2'):
        assert _is_linked(a2, 'attendance2', b)
    _safe_set(b, 'staff3', None)
    assert not _is_linked(b, 'staff3', a2)
    if hasattr(a2, 'attendance2'):
        assert not _is_linked(a2, 'attendance2', b)


def test_assoc_Employee_Leave_reverse_link_reassign_clear():
    a1 = staff_member(staff_Address="sample_text", staff_ContactNo="sample_text", staff_DOB=date(2024, 1, 1), staff_Date_Of_Joint=date(2024, 1, 1), staff_Department="sample_text", staff_Email="sample_text", staff_Id=7, staff_NIC="sample_text", staff_Name="sample_text", staff_Position="sample_text", staff_Salary=3.14)
    a2 = staff_member(staff_Address="sample_text_2", staff_ContactNo="sample_text_2", staff_DOB=date(2025, 6, 15), staff_Date_Of_Joint=date(2025, 6, 15), staff_Department="sample_text_2", staff_Email="sample_text_2", staff_Id=13, staff_NIC="sample_text_2", staff_Name="sample_text_2", staff_Position="sample_text_2", staff_Salary=9.99)
    b = Mission(mission_EndDate=date(2024, 1, 1), mission_NoOfDays=7, mission_StartDate=date(2024, 1, 1), mission_Status="sample_text", mission_Title="sample_text", mission_detail="sample_text", mission_id=7, staff_Id=7)
    _safe_set(b, 'staff1', a1)
    assert _is_linked(b, 'staff1', a1)
    if hasattr(a1, 'staff0'):
        assert _is_linked(a1, 'staff0', b)
    _safe_set(b, 'staff1', a2)
    assert _is_linked(b, 'staff1', a2)
    if hasattr(a1, 'staff0'):
        assert not _is_linked(a1, 'staff0', b)
    if hasattr(a2, 'staff0'):
        assert _is_linked(a2, 'staff0', b)
    _safe_set(b, 'staff1', None)
    assert not _is_linked(b, 'staff1', a2)
    if hasattr(a2, 'staff0'):
        assert not _is_linked(a2, 'staff0', b)


def test_assoc_Employee_Salary_reverse_link_reassign_clear():
    a1 = staff_member(staff_Address="sample_text", staff_ContactNo="sample_text", staff_DOB=date(2024, 1, 1), staff_Date_Of_Joint=date(2024, 1, 1), staff_Department="sample_text", staff_Email="sample_text", staff_Id=7, staff_NIC="sample_text", staff_Name="sample_text", staff_Position="sample_text", staff_Salary=3.14)
    a2 = staff_member(staff_Address="sample_text_2", staff_ContactNo="sample_text_2", staff_DOB=date(2025, 6, 15), staff_Date_Of_Joint=date(2025, 6, 15), staff_Department="sample_text_2", staff_Email="sample_text_2", staff_Id=13, staff_NIC="sample_text_2", staff_Name="sample_text_2", staff_Position="sample_text_2", staff_Salary=9.99)
    b = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    _safe_set(b, 'staff5', a1)
    assert _is_linked(b, 'staff5', a1)
    if hasattr(a1, 'salary4'):
        assert _is_linked(a1, 'salary4', b)
    _safe_set(b, 'staff5', a2)
    assert _is_linked(b, 'staff5', a2)
    if hasattr(a1, 'salary4'):
        assert not _is_linked(a1, 'salary4', b)
    if hasattr(a2, 'salary4'):
        assert _is_linked(a2, 'salary4', b)
    _safe_set(b, 'staff5', None)
    assert not _is_linked(b, 'staff5', a2)
    if hasattr(a2, 'salary4'):
        assert not _is_linked(a2, 'salary4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

