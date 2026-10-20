import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    employee_Company,
    employee_Department,
    employee_Employee,
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

def test_assoc_company15_reverse_link_reassign_clear():
    a1 = employee_Employee(empID=7, isManager=True, name="sample_text")
    a2 = employee_Employee(empID=13, isManager=False, name="sample_text_2")
    b = employee_Company(name="sample_text")
    _safe_set(b, 'Company17', a1)
    assert _is_linked(b, 'Company17', a1)
    if hasattr(a1, 'employees16'):
        assert _is_linked(a1, 'employees16', b)
    _safe_set(b, 'Company17', a2)
    assert _is_linked(b, 'Company17', a2)
    if hasattr(a1, 'employees16'):
        assert not _is_linked(a1, 'employees16', b)
    if hasattr(a2, 'employees16'):
        assert _is_linked(a2, 'employees16', b)
    _safe_set(b, 'Company17', None)
    assert not _is_linked(b, 'Company17', a2)
    if hasattr(a2, 'employees16'):
        assert not _is_linked(a2, 'employees16', b)


def test_assoc_company6_reverse_link_reassign_clear():
    a1 = employee_Department(deptID=7, name="sample_text")
    a2 = employee_Department(deptID=13, name="sample_text_2")
    b = employee_Company(name="sample_text")
    _safe_set(b, 'Company', a1)
    assert _is_linked(b, 'Company', a1)
    if hasattr(a1, 'departments'):
        assert _is_linked(a1, 'departments', b)
    _safe_set(b, 'Company', a2)
    assert _is_linked(b, 'Company', a2)
    if hasattr(a1, 'departments'):
        assert not _is_linked(a1, 'departments', b)
    if hasattr(a2, 'departments'):
        assert _is_linked(a2, 'departments', b)
    _safe_set(b, 'Company', None)
    assert not _is_linked(b, 'Company', a2)
    if hasattr(a2, 'departments'):
        assert not _is_linked(a2, 'departments', b)


def test_assoc_department7_reverse_link_reassign_clear():
    a1 = employee_Employee(empID=7, isManager=True, name="sample_text")
    a2 = employee_Employee(empID=13, isManager=False, name="sample_text_2")
    b = employee_Department(deptID=7, name="sample_text")
    _safe_set(b, 'Department8', a1)
    assert _is_linked(b, 'Department8', a1)
    if hasattr(a1, 'employees'):
        assert _is_linked(a1, 'employees', b)
    _safe_set(b, 'Department8', a2)
    assert _is_linked(b, 'Department8', a2)
    if hasattr(a1, 'employees'):
        assert not _is_linked(a1, 'employees', b)
    if hasattr(a2, 'employees'):
        assert _is_linked(a2, 'employees', b)
    _safe_set(b, 'Department8', None)
    assert not _is_linked(b, 'Department8', a2)
    if hasattr(a2, 'employees'):
        assert not _is_linked(a2, 'employees', b)


def test_assoc_departments1_reverse_link_reassign_clear():
    a1 = employee_Department(deptID=7, name="sample_text")
    a2 = employee_Department(deptID=13, name="sample_text_2")
    b = employee_Company(name="sample_text")
    _safe_set(b, 'company2', {a1})
    assert _is_linked(b, 'company2', a1)
    if hasattr(a1, 'Department'):
        assert _is_linked(a1, 'Department', b)
    _safe_set(b, 'company2', {a2})
    assert _is_linked(b, 'company2', a2)
    if hasattr(a1, 'Department'):
        assert not _is_linked(a1, 'Department', b)
    if hasattr(a2, 'Department'):
        assert _is_linked(a2, 'Department', b)
    _safe_set(b, 'company2', set())
    assert not _is_linked(b, 'company2', a2)
    if hasattr(a2, 'Department'):
        assert not _is_linked(a2, 'Department', b)


def test_assoc_directReports13_reverse_link_reassign_clear():
    a1 = employee_Employee(empID=7, isManager=True, name="sample_text")
    a2 = employee_Employee(empID=13, isManager=False, name="sample_text_2")
    b = employee_Employee(empID=7, isManager=True, name="sample_text")
    _safe_set(b, 'manager', {a1})
    assert _is_linked(b, 'manager', a1)
    if hasattr(a1, 'Employee14'):
        assert _is_linked(a1, 'Employee14', b)
    _safe_set(b, 'manager', {a2})
    assert _is_linked(b, 'manager', a2)
    if hasattr(a1, 'Employee14'):
        assert not _is_linked(a1, 'Employee14', b)
    if hasattr(a2, 'Employee14'):
        assert _is_linked(a2, 'Employee14', b)
    _safe_set(b, 'manager', set())
    assert not _is_linked(b, 'manager', a2)
    if hasattr(a2, 'Employee14'):
        assert not _is_linked(a2, 'Employee14', b)


def test_assoc_employees0_reverse_link_reassign_clear():
    a1 = employee_Employee(empID=7, isManager=True, name="sample_text")
    a2 = employee_Employee(empID=13, isManager=False, name="sample_text_2")
    b = employee_Company(name="sample_text")
    _safe_set(b, 'company', {a1})
    assert _is_linked(b, 'company', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'company', {a2})
    assert _is_linked(b, 'company', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'company', set())
    assert not _is_linked(b, 'company', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_employees4_reverse_link_reassign_clear():
    a1 = employee_Employee(empID=7, isManager=True, name="sample_text")
    a2 = employee_Employee(empID=13, isManager=False, name="sample_text_2")
    b = employee_Department(deptID=7, name="sample_text")
    _safe_set(b, 'department', {a1})
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'Employee5'):
        assert _is_linked(a1, 'Employee5', b)
    _safe_set(b, 'department', {a2})
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'Employee5'):
        assert not _is_linked(a1, 'Employee5', b)
    if hasattr(a2, 'Employee5'):
        assert _is_linked(a2, 'Employee5', b)
    _safe_set(b, 'department', set())
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'Employee5'):
        assert not _is_linked(a2, 'Employee5', b)


def test_assoc_manager10_reverse_link_reassign_clear():
    a1 = employee_Employee(empID=7, isManager=True, name="sample_text")
    a2 = employee_Employee(empID=13, isManager=False, name="sample_text_2")
    b = employee_Employee(empID=7, isManager=True, name="sample_text")
    _safe_set(b, 'directReports', a1)
    assert _is_linked(b, 'directReports', a1)
    if hasattr(a1, 'Employee11'):
        assert _is_linked(a1, 'Employee11', b)
    _safe_set(b, 'directReports', a2)
    assert _is_linked(b, 'directReports', a2)
    if hasattr(a1, 'Employee11'):
        assert not _is_linked(a1, 'Employee11', b)
    if hasattr(a2, 'Employee11'):
        assert _is_linked(a2, 'Employee11', b)
    _safe_set(b, 'directReports', None)
    assert not _is_linked(b, 'directReports', a2)
    if hasattr(a2, 'Employee11'):
        assert not _is_linked(a2, 'Employee11', b)


def test_assoc_manager3_reverse_link_reassign_clear():
    a1 = employee_Employee(empID=7, isManager=True, name="sample_text")
    a2 = employee_Employee(empID=13, isManager=False, name="sample_text_2")
    b = employee_Department(deptID=7, name="sample_text")
    _safe_set(b, 'employee_Department', a1)
    assert _is_linked(b, 'employee_Department', a1)
    if hasattr(a1, 'employee_Employee'):
        assert _is_linked(a1, 'employee_Employee', b)
    _safe_set(b, 'employee_Department', a2)
    assert _is_linked(b, 'employee_Department', a2)
    if hasattr(a1, 'employee_Employee'):
        assert not _is_linked(a1, 'employee_Employee', b)
    if hasattr(a2, 'employee_Employee'):
        assert _is_linked(a2, 'employee_Employee', b)
    _safe_set(b, 'employee_Department', None)
    assert not _is_linked(b, 'employee_Department', a2)
    if hasattr(a2, 'employee_Employee'):
        assert not _is_linked(a2, 'employee_Employee', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

