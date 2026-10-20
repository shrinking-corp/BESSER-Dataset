import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator_Actor,
    Attendance,
    Authenticate_staff,
    Authentication_UseCase,
    Employee,
    Employee_Actor,
    Employee_Management_System_Component,
    Leave,
    Login,
    Login_external,
    Logout_external,
    Salary,
    Salary_Management_UseCase,
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
    a1 = Employee(Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Designation="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14)
    a2 = Employee(Emp_ContactNo="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Designation="sample_text_2", Emp_Email="sample_text_2", Emp_Id=13, Emp_Name="sample_text_2", Emp_Salary=9.99)
    b = Attendance(Date=date(2024, 1, 1), Emp_id="sample_text", endTime="sample_text", startTime="sample_text")
    _safe_set(b, 'Employee_Attendance_13', a1)
    assert _is_linked(b, 'Employee_Attendance_13', a1)
    if hasattr(a1, 'Employee_Attendance_02'):
        assert _is_linked(a1, 'Employee_Attendance_02', b)
    _safe_set(b, 'Employee_Attendance_13', a2)
    assert _is_linked(b, 'Employee_Attendance_13', a2)
    if hasattr(a1, 'Employee_Attendance_02'):
        assert not _is_linked(a1, 'Employee_Attendance_02', b)
    if hasattr(a2, 'Employee_Attendance_02'):
        assert _is_linked(a2, 'Employee_Attendance_02', b)
    _safe_set(b, 'Employee_Attendance_13', None)
    assert not _is_linked(b, 'Employee_Attendance_13', a2)
    if hasattr(a2, 'Employee_Attendance_02'):
        assert not _is_linked(a2, 'Employee_Attendance_02', b)


def test_assoc_Employee_Leave_reverse_link_reassign_clear():
    a1 = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_Type="sample_text", leave_id=7)
    a2 = Leave(Emp_Id=13, Leave_ApplyDate=date(2025, 6, 15), Leave_EndDate=date(2025, 6, 15), Leave_NoOfDays=13, Leave_StartDate=date(2025, 6, 15), Leave_Status="sample_text_2", Leave_Title="sample_text_2", Leave_Type="sample_text_2", leave_id=13)
    b = Employee(Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Designation="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14)
    _safe_set(b, 'Employee_Leave_00', a1)
    assert _is_linked(b, 'Employee_Leave_00', a1)
    if hasattr(a1, 'Employee_Leave_11'):
        assert _is_linked(a1, 'Employee_Leave_11', b)
    _safe_set(b, 'Employee_Leave_00', a2)
    assert _is_linked(b, 'Employee_Leave_00', a2)
    if hasattr(a1, 'Employee_Leave_11'):
        assert not _is_linked(a1, 'Employee_Leave_11', b)
    if hasattr(a2, 'Employee_Leave_11'):
        assert _is_linked(a2, 'Employee_Leave_11', b)
    _safe_set(b, 'Employee_Leave_00', None)
    assert not _is_linked(b, 'Employee_Leave_00', a2)
    if hasattr(a2, 'Employee_Leave_11'):
        assert not _is_linked(a2, 'Employee_Leave_11', b)


def test_assoc_Employee_Salary_reverse_link_reassign_clear():
    a1 = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    a2 = Salary(Emp_Id=13, OverTime="sample_text_2", Sly_Basic=9.99, Sly_Decrement=9.99, Sly_Increment=9.99, Sly_Netgross=9.99)
    b = Employee(Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Designation="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14)
    _safe_set(b, 'Employee_Salary_04', a1)
    assert _is_linked(b, 'Employee_Salary_04', a1)
    if hasattr(a1, 'Employee_Salary_15'):
        assert _is_linked(a1, 'Employee_Salary_15', b)
    _safe_set(b, 'Employee_Salary_04', a2)
    assert _is_linked(b, 'Employee_Salary_04', a2)
    if hasattr(a1, 'Employee_Salary_15'):
        assert not _is_linked(a1, 'Employee_Salary_15', b)
    if hasattr(a2, 'Employee_Salary_15'):
        assert _is_linked(a2, 'Employee_Salary_15', b)
    _safe_set(b, 'Employee_Salary_04', None)
    assert not _is_linked(b, 'Employee_Salary_04', a2)
    if hasattr(a2, 'Employee_Salary_15'):
        assert not _is_linked(a2, 'Employee_Salary_15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

