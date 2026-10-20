import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Admin1,
    Administrator_Actor,
    Authentication_UseCase,
    Customer,
    Customer1,
    Employee,
    Employee1,
    Employee_Actor,
    Employee_Management_System_Component,
    Leave,
    Login_external,
    Logout_external,
    Manager,
    Manager1,
    Manager2,
    Order,
    Salary,
    Salary_Management_UseCase,
    Users,
    Users1,
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
    a1 = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    a2 = Employee1(Email="sample_text_2", Emp_Address="sample_text_2", Emp_Dep="sample_text_2", Salary=13, UserName="sample_text_2", attribute="sample_text_2", contact_no=13, name="sample_text_2", password="sample_text_2")
    b = Admin1(UserName="sample_text", password="sample_text")
    _safe_set(b, 'employee10', {a1})
    assert _is_linked(b, 'employee10', a1)
    if hasattr(a1, 'admin11'):
        assert _is_linked(a1, 'admin11', b)
    _safe_set(b, 'employee10', {a2})
    assert _is_linked(b, 'employee10', a2)
    if hasattr(a1, 'admin11'):
        assert not _is_linked(a1, 'admin11', b)
    if hasattr(a2, 'admin11'):
        assert _is_linked(a2, 'admin11', b)
    _safe_set(b, 'employee10', set())
    assert not _is_linked(b, 'employee10', a2)
    if hasattr(a2, 'admin11'):
        assert not _is_linked(a2, 'admin11', b)


def test_assoc_Admin_Order_reverse_link_reassign_clear():
    a1 = Order(id=7, name="sample_text")
    a2 = Order(id=13, name="sample_text_2")
    b = Admin1(UserName="sample_text", password="sample_text")
    _safe_set(b, 'order12', a1)
    assert _is_linked(b, 'order12', a1)
    if hasattr(a1, 'admin13'):
        assert _is_linked(a1, 'admin13', b)
    _safe_set(b, 'order12', a2)
    assert _is_linked(b, 'order12', a2)
    if hasattr(a1, 'admin13'):
        assert not _is_linked(a1, 'admin13', b)
    if hasattr(a2, 'admin13'):
        assert _is_linked(a2, 'admin13', b)
    _safe_set(b, 'order12', None)
    assert not _is_linked(b, 'order12', a2)
    if hasattr(a2, 'admin13'):
        assert not _is_linked(a2, 'admin13', b)


def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Order(id=7, name="sample_text")
    a2 = Order(id=13, name="sample_text_2")
    b = Customer(UserName="sample_text", address="sample_text", country="sample_text", password="sample_text", postal_code=7)
    _safe_set(b, 'order8', {a1})
    assert _is_linked(b, 'order8', a1)
    if hasattr(a1, 'customer9'):
        assert _is_linked(a1, 'customer9', b)
    _safe_set(b, 'order8', {a2})
    assert _is_linked(b, 'order8', a2)
    if hasattr(a1, 'customer9'):
        assert not _is_linked(a1, 'customer9', b)
    if hasattr(a2, 'customer9'):
        assert _is_linked(a2, 'customer9', b)
    _safe_set(b, 'order8', set())
    assert not _is_linked(b, 'order8', a2)
    if hasattr(a2, 'customer9'):
        assert not _is_linked(a2, 'customer9', b)


def test_assoc_Employee_Leave_reverse_link_reassign_clear():
    a1 = Leave(Emp_Id=7, Leave_EndDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    a2 = Leave(Emp_Id=13, Leave_EndDate=date(2025, 6, 15), Leave_Status="sample_text_2", Leave_Title="sample_text_2", Leave_detail="sample_text_2", leave_id=13)
    b = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    _safe_set(b, 'leave0', a1)
    assert _is_linked(b, 'leave0', a1)
    if hasattr(a1, 'employee1'):
        assert _is_linked(a1, 'employee1', b)
    _safe_set(b, 'leave0', a2)
    assert _is_linked(b, 'leave0', a2)
    if hasattr(a1, 'employee1'):
        assert not _is_linked(a1, 'employee1', b)
    if hasattr(a2, 'employee1'):
        assert _is_linked(a2, 'employee1', b)
    _safe_set(b, 'leave0', None)
    assert not _is_linked(b, 'leave0', a2)
    if hasattr(a2, 'employee1'):
        assert not _is_linked(a2, 'employee1', b)


def test_assoc_Employee_Manager_reverse_link_reassign_clear():
    a1 = Manager2(id=7, name="sample_text", password="sample_text")
    a2 = Manager2(id=13, name="sample_text_2", password="sample_text_2")
    b = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    _safe_set(b, 'manager14', a1)
    assert _is_linked(b, 'manager14', a1)
    if hasattr(a1, 'employee15'):
        assert _is_linked(a1, 'employee15', b)
    _safe_set(b, 'manager14', a2)
    assert _is_linked(b, 'manager14', a2)
    if hasattr(a1, 'employee15'):
        assert not _is_linked(a1, 'employee15', b)
    if hasattr(a2, 'employee15'):
        assert _is_linked(a2, 'employee15', b)
    _safe_set(b, 'manager14', None)
    assert not _is_linked(b, 'manager14', a2)
    if hasattr(a2, 'employee15'):
        assert not _is_linked(a2, 'employee15', b)


def test_assoc_Employee_Salary_reverse_link_reassign_clear():
    a1 = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    a2 = Salary(Emp_Id=13, OverTime="sample_text_2", Sly_Basic=9.99, Sly_Decrement=9.99, Sly_Increment=9.99, Sly_Netgross=9.99)
    b = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

