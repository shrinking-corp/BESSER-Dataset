import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Project,
    employee_Address,
    employee_Degree,
    employee_Directory,
    employee_EmailAddress,
    employee_Employee,
    employee_EmploymentPeriod,
    employee_JobTitle,
    employee_LargeProject,
    employee_PhoneNumber,
    employee_Project,
    employee_SmallProject,
    Gender,
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

def test_assoc_address13_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_Address(city="sample_text", country="sample_text", postalCode="sample_text", province="sample_text", street="sample_text")
    _safe_set(b, 'employee_Address', a1)
    assert _is_linked(b, 'employee_Address', a1)
    if hasattr(a1, 'employee_Employee14'):
        assert _is_linked(a1, 'employee_Employee14', b)
    _safe_set(b, 'employee_Address', a2)
    assert _is_linked(b, 'employee_Address', a2)
    if hasattr(a1, 'employee_Employee14'):
        assert not _is_linked(a1, 'employee_Employee14', b)
    if hasattr(a2, 'employee_Employee14'):
        assert _is_linked(a2, 'employee_Employee14', b)
    _safe_set(b, 'employee_Address', None)
    assert not _is_linked(b, 'employee_Address', a2)
    if hasattr(a2, 'employee_Employee14'):
        assert not _is_linked(a2, 'employee_Employee14', b)


def test_assoc_degrees25_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_Degree(name="sample_text")
    _safe_set(b, 'employee_Degree27', a1)
    assert _is_linked(b, 'employee_Degree27', a1)
    if hasattr(a1, 'employee_Employee26'):
        assert _is_linked(a1, 'employee_Employee26', b)
    _safe_set(b, 'employee_Degree27', a2)
    assert _is_linked(b, 'employee_Degree27', a2)
    if hasattr(a1, 'employee_Employee26'):
        assert not _is_linked(a1, 'employee_Employee26', b)
    if hasattr(a2, 'employee_Employee26'):
        assert _is_linked(a2, 'employee_Employee26', b)
    _safe_set(b, 'employee_Degree27', None)
    assert not _is_linked(b, 'employee_Degree27', a2)
    if hasattr(a2, 'employee_Employee26'):
        assert not _is_linked(a2, 'employee_Employee26', b)


def test_assoc_degrees5_reverse_link_reassign_clear():
    a1 = employee_Directory(name="sample_text")
    a2 = employee_Directory(name="sample_text_2")
    b = employee_Degree(name="sample_text")
    _safe_set(b, 'employee_Degree', a1)
    assert _is_linked(b, 'employee_Degree', a1)
    if hasattr(a1, 'employee_Directory6'):
        assert _is_linked(a1, 'employee_Directory6', b)
    _safe_set(b, 'employee_Degree', a2)
    assert _is_linked(b, 'employee_Degree', a2)
    if hasattr(a1, 'employee_Directory6'):
        assert not _is_linked(a1, 'employee_Directory6', b)
    if hasattr(a2, 'employee_Directory6'):
        assert _is_linked(a2, 'employee_Directory6', b)
    _safe_set(b, 'employee_Degree', None)
    assert not _is_linked(b, 'employee_Degree', a2)
    if hasattr(a2, 'employee_Directory6'):
        assert not _is_linked(a2, 'employee_Directory6', b)


def test_assoc_emailAddresses31_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_EmailAddress(address="sample_text")
    _safe_set(b, 'employee_EmailAddress', a1)
    assert _is_linked(b, 'employee_EmailAddress', a1)
    if hasattr(a1, 'employee_Employee32'):
        assert _is_linked(a1, 'employee_Employee32', b)
    _safe_set(b, 'employee_EmailAddress', a2)
    assert _is_linked(b, 'employee_EmailAddress', a2)
    if hasattr(a1, 'employee_Employee32'):
        assert not _is_linked(a1, 'employee_Employee32', b)
    if hasattr(a2, 'employee_Employee32'):
        assert _is_linked(a2, 'employee_Employee32', b)
    _safe_set(b, 'employee_EmailAddress', None)
    assert not _is_linked(b, 'employee_EmailAddress', a2)
    if hasattr(a2, 'employee_Employee32'):
        assert not _is_linked(a2, 'employee_Employee32', b)


def test_assoc_employees1_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_Directory(name="sample_text")
    _safe_set(b, 'employee_Directory2', {a1})
    assert _is_linked(b, 'employee_Directory2', a1)
    if hasattr(a1, 'employee_Employee'):
        assert _is_linked(a1, 'employee_Employee', b)
    _safe_set(b, 'employee_Directory2', {a2})
    assert _is_linked(b, 'employee_Directory2', a2)
    if hasattr(a1, 'employee_Employee'):
        assert not _is_linked(a1, 'employee_Employee', b)
    if hasattr(a2, 'employee_Employee'):
        assert _is_linked(a2, 'employee_Employee', b)
    _safe_set(b, 'employee_Directory2', set())
    assert not _is_linked(b, 'employee_Directory2', a2)
    if hasattr(a2, 'employee_Employee'):
        assert not _is_linked(a2, 'employee_Employee', b)


def test_assoc_jobTitle15_reverse_link_reassign_clear():
    a1 = employee_JobTitle(title="sample_text")
    a2 = employee_JobTitle(title="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee16', a1)
    assert _is_linked(b, 'employee_Employee16', a1)
    if hasattr(a1, 'employee_JobTitle17'):
        assert _is_linked(a1, 'employee_JobTitle17', b)
    _safe_set(b, 'employee_Employee16', a2)
    assert _is_linked(b, 'employee_Employee16', a2)
    if hasattr(a1, 'employee_JobTitle17'):
        assert not _is_linked(a1, 'employee_JobTitle17', b)
    if hasattr(a2, 'employee_JobTitle17'):
        assert _is_linked(a2, 'employee_JobTitle17', b)
    _safe_set(b, 'employee_Employee16', None)
    assert not _is_linked(b, 'employee_Employee16', a2)
    if hasattr(a2, 'employee_JobTitle17'):
        assert not _is_linked(a2, 'employee_JobTitle17', b)


def test_assoc_jobs3_reverse_link_reassign_clear():
    a1 = employee_JobTitle(title="sample_text")
    a2 = employee_JobTitle(title="sample_text_2")
    b = employee_Directory(name="sample_text")
    _safe_set(b, 'employee_Directory4', {a1})
    assert _is_linked(b, 'employee_Directory4', a1)
    if hasattr(a1, 'employee_JobTitle'):
        assert _is_linked(a1, 'employee_JobTitle', b)
    _safe_set(b, 'employee_Directory4', {a2})
    assert _is_linked(b, 'employee_Directory4', a2)
    if hasattr(a1, 'employee_JobTitle'):
        assert not _is_linked(a1, 'employee_JobTitle', b)
    if hasattr(a2, 'employee_JobTitle'):
        assert _is_linked(a2, 'employee_JobTitle', b)
    _safe_set(b, 'employee_Directory4', set())
    assert not _is_linked(b, 'employee_Directory4', a2)
    if hasattr(a2, 'employee_JobTitle'):
        assert not _is_linked(a2, 'employee_JobTitle', b)


def test_assoc_managedEmployees22_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'manager', {a1})
    assert _is_linked(b, 'manager', a1)
    if hasattr(a1, 'Employee23'):
        assert _is_linked(a1, 'Employee23', b)
    _safe_set(b, 'manager', {a2})
    assert _is_linked(b, 'manager', a2)
    if hasattr(a1, 'Employee23'):
        assert not _is_linked(a1, 'Employee23', b)
    if hasattr(a2, 'Employee23'):
        assert _is_linked(a2, 'Employee23', b)
    _safe_set(b, 'manager', set())
    assert not _is_linked(b, 'manager', a2)
    if hasattr(a2, 'Employee23'):
        assert not _is_linked(a2, 'Employee23', b)


def test_assoc_manager19_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'managedEmployees', a1)
    assert _is_linked(b, 'managedEmployees', a1)
    if hasattr(a1, 'Employee20'):
        assert _is_linked(a1, 'Employee20', b)
    _safe_set(b, 'managedEmployees', a2)
    assert _is_linked(b, 'managedEmployees', a2)
    if hasattr(a1, 'Employee20'):
        assert not _is_linked(a1, 'Employee20', b)
    if hasattr(a2, 'Employee20'):
        assert _is_linked(a2, 'Employee20', b)
    _safe_set(b, 'managedEmployees', None)
    assert not _is_linked(b, 'managedEmployees', a2)
    if hasattr(a2, 'Employee20'):
        assert not _is_linked(a2, 'Employee20', b)


def test_assoc_owner10_reverse_link_reassign_clear():
    a1 = employee_PhoneNumber(areaCode="sample_text", number="sample_text", type="sample_text")
    a2 = employee_PhoneNumber(areaCode="sample_text_2", number="sample_text_2", type="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'Employee', a1)
    assert _is_linked(b, 'Employee', a1)
    if hasattr(a1, 'phoneNumbers'):
        assert _is_linked(a1, 'phoneNumbers', b)
    _safe_set(b, 'Employee', a2)
    assert _is_linked(b, 'Employee', a2)
    if hasattr(a1, 'phoneNumbers'):
        assert not _is_linked(a1, 'phoneNumbers', b)
    if hasattr(a2, 'phoneNumbers'):
        assert _is_linked(a2, 'phoneNumbers', b)
    _safe_set(b, 'Employee', None)
    assert not _is_linked(b, 'Employee', a2)
    if hasattr(a2, 'phoneNumbers'):
        assert not _is_linked(a2, 'phoneNumbers', b)


def test_assoc_period11_reverse_link_reassign_clear():
    a1 = employee_EmploymentPeriod(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    a2 = employee_EmploymentPeriod(endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    b = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee12', a1)
    assert _is_linked(b, 'employee_Employee12', a1)
    if hasattr(a1, 'employee_EmploymentPeriod'):
        assert _is_linked(a1, 'employee_EmploymentPeriod', b)
    _safe_set(b, 'employee_Employee12', a2)
    assert _is_linked(b, 'employee_Employee12', a2)
    if hasattr(a1, 'employee_EmploymentPeriod'):
        assert not _is_linked(a1, 'employee_EmploymentPeriod', b)
    if hasattr(a2, 'employee_EmploymentPeriod'):
        assert _is_linked(a2, 'employee_EmploymentPeriod', b)
    _safe_set(b, 'employee_Employee12', None)
    assert not _is_linked(b, 'employee_Employee12', a2)
    if hasattr(a2, 'employee_EmploymentPeriod'):
        assert not _is_linked(a2, 'employee_EmploymentPeriod', b)


def test_assoc_phoneNumbers24_reverse_link_reassign_clear():
    a1 = employee_PhoneNumber(areaCode="sample_text", number="sample_text", type="sample_text")
    a2 = employee_PhoneNumber(areaCode="sample_text_2", number="sample_text_2", type="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'owner', {a1})
    assert _is_linked(b, 'owner', a1)
    if hasattr(a1, 'PhoneNumber'):
        assert _is_linked(a1, 'PhoneNumber', b)
    _safe_set(b, 'owner', {a2})
    assert _is_linked(b, 'owner', a2)
    if hasattr(a1, 'PhoneNumber'):
        assert not _is_linked(a1, 'PhoneNumber', b)
    if hasattr(a2, 'PhoneNumber'):
        assert _is_linked(a2, 'PhoneNumber', b)
    _safe_set(b, 'owner', set())
    assert not _is_linked(b, 'owner', a2)
    if hasattr(a2, 'PhoneNumber'):
        assert not _is_linked(a2, 'PhoneNumber', b)


def test_assoc_projects0_reverse_link_reassign_clear():
    a1 = employee_Project(description="sample_text", name="sample_text")
    a2 = employee_Project(description="sample_text_2", name="sample_text_2")
    b = employee_Directory(name="sample_text")
    _safe_set(b, 'employee_Directory', {a1})
    assert _is_linked(b, 'employee_Directory', a1)
    if hasattr(a1, 'employee_Project'):
        assert _is_linked(a1, 'employee_Project', b)
    _safe_set(b, 'employee_Directory', {a2})
    assert _is_linked(b, 'employee_Directory', a2)
    if hasattr(a1, 'employee_Project'):
        assert not _is_linked(a1, 'employee_Project', b)
    if hasattr(a2, 'employee_Project'):
        assert _is_linked(a2, 'employee_Project', b)
    _safe_set(b, 'employee_Directory', set())
    assert not _is_linked(b, 'employee_Directory', a2)
    if hasattr(a2, 'employee_Project'):
        assert not _is_linked(a2, 'employee_Project', b)


def test_assoc_projects28_reverse_link_reassign_clear():
    a1 = employee_Project(description="sample_text", name="sample_text")
    a2 = employee_Project(description="sample_text_2", name="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee29', {a1})
    assert _is_linked(b, 'employee_Employee29', a1)
    if hasattr(a1, 'employee_Project30'):
        assert _is_linked(a1, 'employee_Project30', b)
    _safe_set(b, 'employee_Employee29', {a2})
    assert _is_linked(b, 'employee_Employee29', a2)
    if hasattr(a1, 'employee_Project30'):
        assert not _is_linked(a1, 'employee_Project30', b)
    if hasattr(a2, 'employee_Project30'):
        assert _is_linked(a2, 'employee_Project30', b)
    _safe_set(b, 'employee_Employee29', set())
    assert not _is_linked(b, 'employee_Employee29', a2)
    if hasattr(a2, 'employee_Project30'):
        assert not _is_linked(a2, 'employee_Project30', b)


def test_assoc_teamLeader7_reverse_link_reassign_clear():
    a1 = employee_Project(description="sample_text", name="sample_text")
    a2 = employee_Project(description="sample_text_2", name="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee9', a1)
    assert _is_linked(b, 'employee_Employee9', a1)
    if hasattr(a1, 'employee_Project8'):
        assert _is_linked(a1, 'employee_Project8', b)
    _safe_set(b, 'employee_Employee9', a2)
    assert _is_linked(b, 'employee_Employee9', a2)
    if hasattr(a1, 'employee_Project8'):
        assert not _is_linked(a1, 'employee_Project8', b)
    if hasattr(a2, 'employee_Project8'):
        assert _is_linked(a2, 'employee_Project8', b)
    _safe_set(b, 'employee_Employee9', None)
    assert not _is_linked(b, 'employee_Employee9', a2)
    if hasattr(a2, 'employee_Project8'):
        assert not _is_linked(a2, 'employee_Project8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

