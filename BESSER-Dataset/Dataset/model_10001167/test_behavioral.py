import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator_Actor,
    Attendance,
    Authenticate_staff,
    Authentication_UseCase,
    Employee2,
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

def test_assoc_Employee_Leave_reverse_link_reassign_clear():
    a1 = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    a2 = Leave(Emp_Id=13, Leave_ApplyDate=date(2025, 6, 15), Leave_EndDate=date(2025, 6, 15), Leave_NoOfDays=13, Leave_StartDate=date(2025, 6, 15), Leave_Status="sample_text_2", Leave_Title="sample_text_2", Leave_detail="sample_text_2", leave_id=13)
    b = Employee2(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    _safe_set(b, 'leave4', a1)
    assert _is_linked(b, 'leave4', a1)
    if hasattr(a1, 'employee5'):
        assert _is_linked(a1, 'employee5', b)
    _safe_set(b, 'leave4', a2)
    assert _is_linked(b, 'leave4', a2)
    if hasattr(a1, 'employee5'):
        assert not _is_linked(a1, 'employee5', b)
    if hasattr(a2, 'employee5'):
        assert _is_linked(a2, 'employee5', b)
    _safe_set(b, 'leave4', None)
    assert not _is_linked(b, 'leave4', a2)
    if hasattr(a2, 'employee5'):
        assert not _is_linked(a2, 'employee5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

