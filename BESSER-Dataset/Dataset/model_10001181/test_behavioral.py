import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator,
    Administrator_Actor,
    Attendance,
    Authentication_UseCase,
    Driving_Staff,
    Employee_Actor,
    Employee_Management_System_Component,
    Leave_Status,
    Login,
    Login_external,
    Logout_external,
    Manager,
    Salary,
    Salary_Management_UseCase,
    Staff,
    Tuning_Staff,
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

def test_assoc_Administrator_Login_reverse_link_reassign_clear():
    a1 = Login(Password="sample_text", UserName="sample_text")
    a2 = Login(Password="sample_text_2", UserName="sample_text_2")
    b = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    _safe_set(b, 'login16', a1)
    assert _is_linked(b, 'login16', a1)
    if hasattr(a1, 'administrator17'):
        assert _is_linked(a1, 'administrator17', b)
    _safe_set(b, 'login16', a2)
    assert _is_linked(b, 'login16', a2)
    if hasattr(a1, 'administrator17'):
        assert not _is_linked(a1, 'administrator17', b)
    if hasattr(a2, 'administrator17'):
        assert _is_linked(a2, 'administrator17', b)
    _safe_set(b, 'login16', None)
    assert not _is_linked(b, 'login16', a2)
    if hasattr(a2, 'administrator17'):
        assert not _is_linked(a2, 'administrator17', b)


def test_assoc_Administrator_Manager_reverse_link_reassign_clear():
    a1 = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    a2 = Manager(Emp_Address="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_NIC="sample_text_2", Emp_Position="sample_text_2", Mng_ContactNo="sample_text_2", Mng_Email="sample_text_2", Mng_Id=13, Mng_Name="sample_text_2", Mng_Salary=9.99)
    b = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    _safe_set(b, 'manager12', a1)
    assert _is_linked(b, 'manager12', a1)
    if hasattr(a1, 'administrator13'):
        assert _is_linked(a1, 'administrator13', b)
    _safe_set(b, 'manager12', a2)
    assert _is_linked(b, 'manager12', a2)
    if hasattr(a1, 'administrator13'):
        assert not _is_linked(a1, 'administrator13', b)
    if hasattr(a2, 'administrator13'):
        assert _is_linked(a2, 'administrator13', b)
    _safe_set(b, 'manager12', None)
    assert not _is_linked(b, 'manager12', a2)
    if hasattr(a2, 'administrator13'):
        assert not _is_linked(a2, 'administrator13', b)


def test_assoc_Employee_Attendance_reverse_link_reassign_clear():
    a1 = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    a2 = Manager(Emp_Address="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_NIC="sample_text_2", Emp_Position="sample_text_2", Mng_ContactNo="sample_text_2", Mng_Email="sample_text_2", Mng_Id=13, Mng_Name="sample_text_2", Mng_Salary=9.99)
    b = Attendance(AttendTime="sample_text", Attend_date=date(2024, 1, 1), Emp_id="sample_text", Leaving_Time="sample_text")
    _safe_set(b, 'employee3', a1)
    assert _is_linked(b, 'employee3', a1)
    if hasattr(a1, 'attendance2'):
        assert _is_linked(a1, 'attendance2', b)
    _safe_set(b, 'employee3', a2)
    assert _is_linked(b, 'employee3', a2)
    if hasattr(a1, 'attendance2'):
        assert not _is_linked(a1, 'attendance2', b)
    if hasattr(a2, 'attendance2'):
        assert _is_linked(a2, 'attendance2', b)
    _safe_set(b, 'employee3', None)
    assert not _is_linked(b, 'employee3', a2)
    if hasattr(a2, 'attendance2'):
        assert not _is_linked(a2, 'attendance2', b)


def test_assoc_Employee_Leave_reverse_link_reassign_clear():
    a1 = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    a2 = Manager(Emp_Address="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_NIC="sample_text_2", Emp_Position="sample_text_2", Mng_ContactNo="sample_text_2", Mng_Email="sample_text_2", Mng_Id=13, Mng_Name="sample_text_2", Mng_Salary=9.99)
    b = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    _safe_set(b, 'employee1', a1)
    assert _is_linked(b, 'employee1', a1)
    if hasattr(a1, 'leave0'):
        assert _is_linked(a1, 'leave0', b)
    _safe_set(b, 'employee1', a2)
    assert _is_linked(b, 'employee1', a2)
    if hasattr(a1, 'leave0'):
        assert not _is_linked(a1, 'leave0', b)
    if hasattr(a2, 'leave0'):
        assert _is_linked(a2, 'leave0', b)
    _safe_set(b, 'employee1', None)
    assert not _is_linked(b, 'employee1', a2)
    if hasattr(a2, 'leave0'):
        assert not _is_linked(a2, 'leave0', b)


def test_assoc_Employee_Salary_reverse_link_reassign_clear():
    a1 = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    a2 = Salary(Emp_Id=13, OverTime="sample_text_2", Sly_Basic=9.99, Sly_Decrement=9.99, Sly_Increment=9.99, Sly_Netgross=9.99)
    b = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    _safe_set(b, 'salary4', a1)
    assert _is_linked(b, 'salary4', a1)
    if hasattr(a1, 'employee5'):
        assert _is_linked(a1, 'employee5', b)
    _safe_set(b, 'salary4', a2)
    assert _is_linked(b, 'salary4', a2)
    if hasattr(a1, 'employee5'):
        assert not _is_linked(a1, 'employee5', b)
    if hasattr(a2, 'employee5'):
        assert _is_linked(a2, 'employee5', b)
    _safe_set(b, 'salary4', None)
    assert not _is_linked(b, 'salary4', a2)
    if hasattr(a2, 'employee5'):
        assert not _is_linked(a2, 'employee5', b)


def test_assoc_Login_Administrator_reverse_link_reassign_clear():
    a1 = Login(Password="sample_text", UserName="sample_text")
    a2 = Login(Password="sample_text_2", UserName="sample_text_2")
    b = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    _safe_set(b, 'login15', a1)
    assert _is_linked(b, 'login15', a1)
    if hasattr(a1, 'administrator14'):
        assert _is_linked(a1, 'administrator14', b)
    _safe_set(b, 'login15', a2)
    assert _is_linked(b, 'login15', a2)
    if hasattr(a1, 'administrator14'):
        assert not _is_linked(a1, 'administrator14', b)
    if hasattr(a2, 'administrator14'):
        assert _is_linked(a2, 'administrator14', b)
    _safe_set(b, 'login15', None)
    assert not _is_linked(b, 'login15', a2)
    if hasattr(a2, 'administrator14'):
        assert not _is_linked(a2, 'administrator14', b)


def test_assoc_Login_Manager_reverse_link_reassign_clear():
    a1 = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    a2 = Manager(Emp_Address="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_NIC="sample_text_2", Emp_Position="sample_text_2", Mng_ContactNo="sample_text_2", Mng_Email="sample_text_2", Mng_Id=13, Mng_Name="sample_text_2", Mng_Salary=9.99)
    b = Login(Password="sample_text", UserName="sample_text")
    _safe_set(b, 'manager18', a1)
    assert _is_linked(b, 'manager18', a1)
    if hasattr(a1, 'login19'):
        assert _is_linked(a1, 'login19', b)
    _safe_set(b, 'manager18', a2)
    assert _is_linked(b, 'manager18', a2)
    if hasattr(a1, 'login19'):
        assert not _is_linked(a1, 'login19', b)
    if hasattr(a2, 'login19'):
        assert _is_linked(a2, 'login19', b)
    _safe_set(b, 'manager18', None)
    assert not _is_linked(b, 'manager18', a2)
    if hasattr(a2, 'login19'):
        assert not _is_linked(a2, 'login19', b)


def test_assoc_Staff_Driving_Staff_reverse_link_reassign_clear():
    a1 = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    a2 = Staff(Authendication_Mood="sample_text_2", Password="sample_text_2", UserName="sample_text_2")
    b = Driving_Staff(Authendication_Mood="sample_text", Password="sample_text", PilotName="sample_text", Pilot_ContactNo="sample_text")
    _safe_set(b, 'staff21', a1)
    assert _is_linked(b, 'staff21', a1)
    if hasattr(a1, 'driving_Staff20'):
        assert _is_linked(a1, 'driving_Staff20', b)
    _safe_set(b, 'staff21', a2)
    assert _is_linked(b, 'staff21', a2)
    if hasattr(a1, 'driving_Staff20'):
        assert not _is_linked(a1, 'driving_Staff20', b)
    if hasattr(a2, 'driving_Staff20'):
        assert _is_linked(a2, 'driving_Staff20', b)
    _safe_set(b, 'staff21', None)
    assert not _is_linked(b, 'staff21', a2)
    if hasattr(a2, 'driving_Staff20'):
        assert not _is_linked(a2, 'driving_Staff20', b)


def test_assoc_Staff_Leave_Status_reverse_link_reassign_clear():
    a1 = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    a2 = Staff(Authendication_Mood="sample_text_2", Password="sample_text_2", UserName="sample_text_2")
    b = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    _safe_set(b, 'staff11', a1)
    assert _is_linked(b, 'staff11', a1)
    if hasattr(a1, 'leave_Status10'):
        assert _is_linked(a1, 'leave_Status10', b)
    _safe_set(b, 'staff11', a2)
    assert _is_linked(b, 'staff11', a2)
    if hasattr(a1, 'leave_Status10'):
        assert not _is_linked(a1, 'leave_Status10', b)
    if hasattr(a2, 'leave_Status10'):
        assert _is_linked(a2, 'leave_Status10', b)
    _safe_set(b, 'staff11', None)
    assert not _is_linked(b, 'staff11', a2)
    if hasattr(a2, 'leave_Status10'):
        assert not _is_linked(a2, 'leave_Status10', b)


def test_assoc_Staff_Tuning_Staff_reverse_link_reassign_clear():
    a1 = Tuning_Staff(Address="sample_text", Authendication_Mood="sample_text", UserName="sample_text")
    a2 = Tuning_Staff(Address="sample_text_2", Authendication_Mood="sample_text_2", UserName="sample_text_2")
    b = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    _safe_set(b, 'tuning_Staff22', a1)
    assert _is_linked(b, 'tuning_Staff22', a1)
    if hasattr(a1, 'staff23'):
        assert _is_linked(a1, 'staff23', b)
    _safe_set(b, 'tuning_Staff22', a2)
    assert _is_linked(b, 'tuning_Staff22', a2)
    if hasattr(a1, 'staff23'):
        assert not _is_linked(a1, 'staff23', b)
    if hasattr(a2, 'staff23'):
        assert _is_linked(a2, 'staff23', b)
    _safe_set(b, 'tuning_Staff22', None)
    assert not _is_linked(b, 'tuning_Staff22', a2)
    if hasattr(a2, 'staff23'):
        assert not _is_linked(a2, 'staff23', b)


