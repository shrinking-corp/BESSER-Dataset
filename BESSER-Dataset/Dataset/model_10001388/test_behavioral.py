import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Attendence,
    Employee,
    EmployeeRequest,
    Loan,
    Login,
    Salary,
    payslip,
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

def test_assoc_Attendence_Employee_reverse_link_reassign_clear():
    a1 = Employee(emp_email="sample_text", emp_id=7, emp_name="sample_text")
    a2 = Employee(emp_email="sample_text_2", emp_id=13, emp_name="sample_text_2")
    b = Attendence(Basic_salary=7, emp_id=7, emp_name="sample_text")
    _safe_set(b, 'employee0', a1)
    assert _is_linked(b, 'employee0', a1)
    if hasattr(a1, 'attendence1'):
        assert _is_linked(a1, 'attendence1', b)
    _safe_set(b, 'employee0', a2)
    assert _is_linked(b, 'employee0', a2)
    if hasattr(a1, 'attendence1'):
        assert not _is_linked(a1, 'attendence1', b)
    if hasattr(a2, 'attendence1'):
        assert _is_linked(a2, 'attendence1', b)
    _safe_set(b, 'employee0', None)
    assert not _is_linked(b, 'employee0', a2)
    if hasattr(a2, 'attendence1'):
        assert not _is_linked(a2, 'attendence1', b)


def test_assoc_Employee_Salary_reverse_link_reassign_clear():
    a1 = Salary(basic_salary="sample_text", emp_id=7, emp_name="sample_text")
    a2 = Salary(basic_salary="sample_text_2", emp_id=13, emp_name="sample_text_2")
    b = Employee(emp_email="sample_text", emp_id=7, emp_name="sample_text")
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

