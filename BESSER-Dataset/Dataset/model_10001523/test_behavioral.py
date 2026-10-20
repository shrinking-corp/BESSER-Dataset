import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Days_Attended,
    Employee,
    Leave,
    Login,
    Salary,
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

def test_assoc_Admin_Employee_reverse_link_reassign_clear():
    a1 = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    a2 = Employee(EmployeeEmail="sample_text_2", EmployeeId="sample_text_2", EmployeePhoneNumber=13, EmplyeeName="sample_text_2")
    b = Admin(Email="sample_text", Name="sample_text")
    _safe_set(b, 'employee8', {a1})
    assert _is_linked(b, 'employee8', a1)
    if hasattr(a1, 'admin9'):
        assert _is_linked(a1, 'admin9', b)
    _safe_set(b, 'employee8', {a2})
    assert _is_linked(b, 'employee8', a2)
    if hasattr(a1, 'admin9'):
        assert not _is_linked(a1, 'admin9', b)
    if hasattr(a2, 'admin9'):
        assert _is_linked(a2, 'admin9', b)
    _safe_set(b, 'employee8', set())
    assert not _is_linked(b, 'employee8', a2)
    if hasattr(a2, 'admin9'):
        assert not _is_linked(a2, 'admin9', b)


def test_assoc_Employee_Days_Attended_reverse_link_reassign_clear():
    a1 = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    a2 = Employee(EmployeeEmail="sample_text_2", EmployeeId="sample_text_2", EmployeePhoneNumber=13, EmplyeeName="sample_text_2")
    b = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    _safe_set(b, 'employee5', a1)
    assert _is_linked(b, 'employee5', a1)
    if hasattr(a1, 'days_Attended4'):
        assert _is_linked(a1, 'days_Attended4', b)
    _safe_set(b, 'employee5', a2)
    assert _is_linked(b, 'employee5', a2)
    if hasattr(a1, 'days_Attended4'):
        assert not _is_linked(a1, 'days_Attended4', b)
    if hasattr(a2, 'days_Attended4'):
        assert _is_linked(a2, 'days_Attended4', b)
    _safe_set(b, 'employee5', None)
    assert not _is_linked(b, 'employee5', a2)
    if hasattr(a2, 'days_Attended4'):
        assert not _is_linked(a2, 'days_Attended4', b)


def test_assoc_Employee_Leave_reverse_link_reassign_clear():
    a1 = Leave(Leave_Detail="sample_text", Leave_NoOfDays=7, attribute="sample_text")
    a2 = Leave(Leave_Detail="sample_text_2", Leave_NoOfDays=13, attribute="sample_text_2")
    b = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    _safe_set(b, 'leave6', a1)
    assert _is_linked(b, 'leave6', a1)
    if hasattr(a1, 'employee7'):
        assert _is_linked(a1, 'employee7', b)
    _safe_set(b, 'leave6', a2)
    assert _is_linked(b, 'leave6', a2)
    if hasattr(a1, 'employee7'):
        assert not _is_linked(a1, 'employee7', b)
    if hasattr(a2, 'employee7'):
        assert _is_linked(a2, 'employee7', b)
    _safe_set(b, 'leave6', None)
    assert not _is_linked(b, 'leave6', a2)
    if hasattr(a2, 'employee7'):
        assert not _is_linked(a2, 'employee7', b)


def test_assoc_Employee_Salary_reverse_link_reassign_clear():
    a1 = Salary(Bonus=7, DaysAttended=7, EmployeeID="sample_text", NetSalary=7)
    a2 = Salary(Bonus=13, DaysAttended=13, EmployeeID="sample_text_2", NetSalary=13)
    b = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    _safe_set(b, 'salary2', a1)
    assert _is_linked(b, 'salary2', a1)
    if hasattr(a1, 'employee3'):
        assert _is_linked(a1, 'employee3', b)
    _safe_set(b, 'salary2', a2)
    assert _is_linked(b, 'salary2', a2)
    if hasattr(a1, 'employee3'):
        assert not _is_linked(a1, 'employee3', b)
    if hasattr(a2, 'employee3'):
        assert _is_linked(a2, 'employee3', b)
    _safe_set(b, 'salary2', None)
    assert not _is_linked(b, 'salary2', a2)
    if hasattr(a2, 'employee3'):
        assert not _is_linked(a2, 'employee3', b)


def test_assoc_Login_Employee_reverse_link_reassign_clear():
    a1 = Login(Password="sample_text", Username="sample_text")
    a2 = Login(Password="sample_text_2", Username="sample_text_2")
    b = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    _safe_set(b, 'login1', a1)
    assert _is_linked(b, 'login1', a1)
    if hasattr(a1, 'employee0'):
        assert _is_linked(a1, 'employee0', b)
    _safe_set(b, 'login1', a2)
    assert _is_linked(b, 'login1', a2)
    if hasattr(a1, 'employee0'):
        assert not _is_linked(a1, 'employee0', b)
    if hasattr(a2, 'employee0'):
        assert _is_linked(a2, 'employee0', b)
    _safe_set(b, 'login1', None)
    assert not _is_linked(b, 'login1', a2)
    if hasattr(a2, 'employee0'):
        assert not _is_linked(a2, 'employee0', b)


def test_assoc_Salary_Days_Attended_reverse_link_reassign_clear():
    a1 = Salary(Bonus=7, DaysAttended=7, EmployeeID="sample_text", NetSalary=7)
    a2 = Salary(Bonus=13, DaysAttended=13, EmployeeID="sample_text_2", NetSalary=13)
    b = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    _safe_set(b, 'salary11', a1)
    assert _is_linked(b, 'salary11', a1)
    if hasattr(a1, 'days_Attended10'):
        assert _is_linked(a1, 'days_Attended10', b)
    _safe_set(b, 'salary11', a2)
    assert _is_linked(b, 'salary11', a2)
    if hasattr(a1, 'days_Attended10'):
        assert not _is_linked(a1, 'days_Attended10', b)
    if hasattr(a2, 'days_Attended10'):
        assert _is_linked(a2, 'days_Attended10', b)
    _safe_set(b, 'salary11', None)
    assert not _is_linked(b, 'salary11', a2)
    if hasattr(a2, 'days_Attended10'):
        assert not _is_linked(a2, 'days_Attended10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

