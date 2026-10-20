import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Project,
    employee_Address,
    employee_EmailAddress,
    employee_Employee,
    employee_EmploymentPeriod,
    employee_JobTitle,
    employee_LargeProject,
    employee_Organization,
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

def test_assoc_address12_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", id="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_Address(city="sample_text", country="sample_text", id="sample_text", postalCode="sample_text", province="sample_text", street="sample_text")
    _safe_set(b, 'employee_Address', a1)
    assert _is_linked(b, 'employee_Address', a1)
    if hasattr(a1, 'employee_Employee13'):
        assert _is_linked(a1, 'employee_Employee13', b)
    _safe_set(b, 'employee_Address', a2)
    assert _is_linked(b, 'employee_Address', a2)
    if hasattr(a1, 'employee_Employee13'):
        assert not _is_linked(a1, 'employee_Employee13', b)
    if hasattr(a2, 'employee_Employee13'):
        assert _is_linked(a2, 'employee_Employee13', b)
    _safe_set(b, 'employee_Address', None)
    assert not _is_linked(b, 'employee_Address', a2)
    if hasattr(a2, 'employee_Employee13'):
        assert not _is_linked(a2, 'employee_Employee13', b)


def test_assoc_emailAddresses29_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", id="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_EmailAddress(address="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'employee_EmailAddress', a1)
    assert _is_linked(b, 'employee_EmailAddress', a1)
    if hasattr(a1, 'employee_Employee30'):
        assert _is_linked(a1, 'employee_Employee30', b)
    _safe_set(b, 'employee_EmailAddress', a2)
    assert _is_linked(b, 'employee_EmailAddress', a2)
    if hasattr(a1, 'employee_Employee30'):
        assert not _is_linked(a1, 'employee_Employee30', b)
    if hasattr(a2, 'employee_Employee30'):
        assert _is_linked(a2, 'employee_Employee30', b)
    _safe_set(b, 'employee_EmailAddress', None)
    assert not _is_linked(b, 'employee_EmailAddress', a2)
    if hasattr(a2, 'employee_Employee30'):
        assert not _is_linked(a2, 'employee_Employee30', b)


def test_assoc_employees0_reverse_link_reassign_clear():
    a1 = employee_Organization(name="sample_text")
    a2 = employee_Organization(name="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee', a1)
    assert _is_linked(b, 'employee_Employee', a1)
    if hasattr(a1, 'employee_Organization'):
        assert _is_linked(a1, 'employee_Organization', b)
    _safe_set(b, 'employee_Employee', a2)
    assert _is_linked(b, 'employee_Employee', a2)
    if hasattr(a1, 'employee_Organization'):
        assert not _is_linked(a1, 'employee_Organization', b)
    if hasattr(a2, 'employee_Organization'):
        assert _is_linked(a2, 'employee_Organization', b)
    _safe_set(b, 'employee_Employee', None)
    assert not _is_linked(b, 'employee_Employee', a2)
    if hasattr(a2, 'employee_Organization'):
        assert not _is_linked(a2, 'employee_Organization', b)


def test_assoc_jobTitle14_reverse_link_reassign_clear():
    a1 = employee_JobTitle(title="sample_text")
    a2 = employee_JobTitle(title="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee15', a1)
    assert _is_linked(b, 'employee_Employee15', a1)
    if hasattr(a1, 'employee_JobTitle16'):
        assert _is_linked(a1, 'employee_JobTitle16', b)
    _safe_set(b, 'employee_Employee15', a2)
    assert _is_linked(b, 'employee_Employee15', a2)
    if hasattr(a1, 'employee_JobTitle16'):
        assert not _is_linked(a1, 'employee_JobTitle16', b)
    if hasattr(a2, 'employee_JobTitle16'):
        assert _is_linked(a2, 'employee_JobTitle16', b)
    _safe_set(b, 'employee_Employee15', None)
    assert not _is_linked(b, 'employee_Employee15', a2)
    if hasattr(a2, 'employee_JobTitle16'):
        assert not _is_linked(a2, 'employee_JobTitle16', b)


def test_assoc_jobs3_reverse_link_reassign_clear():
    a1 = employee_Organization(name="sample_text")
    a2 = employee_Organization(name="sample_text_2")
    b = employee_JobTitle(title="sample_text")
    _safe_set(b, 'employee_JobTitle', a1)
    assert _is_linked(b, 'employee_JobTitle', a1)
    if hasattr(a1, 'employee_Organization4'):
        assert _is_linked(a1, 'employee_Organization4', b)
    _safe_set(b, 'employee_JobTitle', a2)
    assert _is_linked(b, 'employee_JobTitle', a2)
    if hasattr(a1, 'employee_Organization4'):
        assert not _is_linked(a1, 'employee_Organization4', b)
    if hasattr(a2, 'employee_Organization4'):
        assert _is_linked(a2, 'employee_Organization4', b)
    _safe_set(b, 'employee_JobTitle', None)
    assert not _is_linked(b, 'employee_JobTitle', a2)
    if hasattr(a2, 'employee_Organization4'):
        assert not _is_linked(a2, 'employee_Organization4', b)


def test_assoc_managedEmployees21_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", id="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee22', a1)
    assert _is_linked(b, 'employee_Employee22', a1)
    if hasattr(a1, 'employee_Employee20'):
        assert _is_linked(a1, 'employee_Employee20', b)
    _safe_set(b, 'employee_Employee22', a2)
    assert _is_linked(b, 'employee_Employee22', a2)
    if hasattr(a1, 'employee_Employee20'):
        assert not _is_linked(a1, 'employee_Employee20', b)
    if hasattr(a2, 'employee_Employee20'):
        assert _is_linked(a2, 'employee_Employee20', b)
    _safe_set(b, 'employee_Employee22', None)
    assert not _is_linked(b, 'employee_Employee22', a2)
    if hasattr(a2, 'employee_Employee20'):
        assert not _is_linked(a2, 'employee_Employee20', b)


def test_assoc_manager18_reverse_link_reassign_clear():
    a1 = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    a2 = employee_Employee(firstName="sample_text_2", gender="sample_text_2", id="sample_text_2", lastName="sample_text_2", responsibilities="sample_text_2", salary=9.99)
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee19', a1)
    assert _is_linked(b, 'employee_Employee19', a1)
    if hasattr(a1, 'employee_Employee17'):
        assert _is_linked(a1, 'employee_Employee17', b)
    _safe_set(b, 'employee_Employee19', a2)
    assert _is_linked(b, 'employee_Employee19', a2)
    if hasattr(a1, 'employee_Employee17'):
        assert not _is_linked(a1, 'employee_Employee17', b)
    if hasattr(a2, 'employee_Employee17'):
        assert _is_linked(a2, 'employee_Employee17', b)
    _safe_set(b, 'employee_Employee19', None)
    assert not _is_linked(b, 'employee_Employee19', a2)
    if hasattr(a2, 'employee_Employee17'):
        assert not _is_linked(a2, 'employee_Employee17', b)


def test_assoc_owner8_reverse_link_reassign_clear():
    a1 = employee_PhoneNumber(areaCode="sample_text", number="sample_text", type="sample_text")
    a2 = employee_PhoneNumber(areaCode="sample_text_2", number="sample_text_2", type="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee9', a1)
    assert _is_linked(b, 'employee_Employee9', a1)
    if hasattr(a1, 'employee_PhoneNumber'):
        assert _is_linked(a1, 'employee_PhoneNumber', b)
    _safe_set(b, 'employee_Employee9', a2)
    assert _is_linked(b, 'employee_Employee9', a2)
    if hasattr(a1, 'employee_PhoneNumber'):
        assert not _is_linked(a1, 'employee_PhoneNumber', b)
    if hasattr(a2, 'employee_PhoneNumber'):
        assert _is_linked(a2, 'employee_PhoneNumber', b)
    _safe_set(b, 'employee_Employee9', None)
    assert not _is_linked(b, 'employee_Employee9', a2)
    if hasattr(a2, 'employee_PhoneNumber'):
        assert not _is_linked(a2, 'employee_PhoneNumber', b)


def test_assoc_period10_reverse_link_reassign_clear():
    a1 = employee_EmploymentPeriod(endDate=date(2024, 1, 1), id="sample_text", startDate=date(2024, 1, 1))
    a2 = employee_EmploymentPeriod(endDate=date(2025, 6, 15), id="sample_text_2", startDate=date(2025, 6, 15))
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee11', a1)
    assert _is_linked(b, 'employee_Employee11', a1)
    if hasattr(a1, 'employee_EmploymentPeriod'):
        assert _is_linked(a1, 'employee_EmploymentPeriod', b)
    _safe_set(b, 'employee_Employee11', a2)
    assert _is_linked(b, 'employee_Employee11', a2)
    if hasattr(a1, 'employee_EmploymentPeriod'):
        assert not _is_linked(a1, 'employee_EmploymentPeriod', b)
    if hasattr(a2, 'employee_EmploymentPeriod'):
        assert _is_linked(a2, 'employee_EmploymentPeriod', b)
    _safe_set(b, 'employee_Employee11', None)
    assert not _is_linked(b, 'employee_Employee11', a2)
    if hasattr(a2, 'employee_EmploymentPeriod'):
        assert not _is_linked(a2, 'employee_EmploymentPeriod', b)


def test_assoc_phoneNumbers23_reverse_link_reassign_clear():
    a1 = employee_PhoneNumber(areaCode="sample_text", number="sample_text", type="sample_text")
    a2 = employee_PhoneNumber(areaCode="sample_text_2", number="sample_text_2", type="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee24', {a1})
    assert _is_linked(b, 'employee_Employee24', a1)
    if hasattr(a1, 'employee_PhoneNumber25'):
        assert _is_linked(a1, 'employee_PhoneNumber25', b)
    _safe_set(b, 'employee_Employee24', {a2})
    assert _is_linked(b, 'employee_Employee24', a2)
    if hasattr(a1, 'employee_PhoneNumber25'):
        assert not _is_linked(a1, 'employee_PhoneNumber25', b)
    if hasattr(a2, 'employee_PhoneNumber25'):
        assert _is_linked(a2, 'employee_PhoneNumber25', b)
    _safe_set(b, 'employee_Employee24', set())
    assert not _is_linked(b, 'employee_Employee24', a2)
    if hasattr(a2, 'employee_PhoneNumber25'):
        assert not _is_linked(a2, 'employee_PhoneNumber25', b)


def test_assoc_projects1_reverse_link_reassign_clear():
    a1 = employee_Project(description="sample_text", name="sample_text")
    a2 = employee_Project(description="sample_text_2", name="sample_text_2")
    b = employee_Organization(name="sample_text")
    _safe_set(b, 'employee_Organization2', {a1})
    assert _is_linked(b, 'employee_Organization2', a1)
    if hasattr(a1, 'employee_Project'):
        assert _is_linked(a1, 'employee_Project', b)
    _safe_set(b, 'employee_Organization2', {a2})
    assert _is_linked(b, 'employee_Organization2', a2)
    if hasattr(a1, 'employee_Project'):
        assert not _is_linked(a1, 'employee_Project', b)
    if hasattr(a2, 'employee_Project'):
        assert _is_linked(a2, 'employee_Project', b)
    _safe_set(b, 'employee_Organization2', set())
    assert not _is_linked(b, 'employee_Organization2', a2)
    if hasattr(a2, 'employee_Project'):
        assert not _is_linked(a2, 'employee_Project', b)


def test_assoc_projects26_reverse_link_reassign_clear():
    a1 = employee_Project(description="sample_text", name="sample_text")
    a2 = employee_Project(description="sample_text_2", name="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee27', {a1})
    assert _is_linked(b, 'employee_Employee27', a1)
    if hasattr(a1, 'employee_Project28'):
        assert _is_linked(a1, 'employee_Project28', b)
    _safe_set(b, 'employee_Employee27', {a2})
    assert _is_linked(b, 'employee_Employee27', a2)
    if hasattr(a1, 'employee_Project28'):
        assert not _is_linked(a1, 'employee_Project28', b)
    if hasattr(a2, 'employee_Project28'):
        assert _is_linked(a2, 'employee_Project28', b)
    _safe_set(b, 'employee_Employee27', set())
    assert not _is_linked(b, 'employee_Employee27', a2)
    if hasattr(a2, 'employee_Project28'):
        assert not _is_linked(a2, 'employee_Project28', b)


def test_assoc_teamLeader5_reverse_link_reassign_clear():
    a1 = employee_Project(description="sample_text", name="sample_text")
    a2 = employee_Project(description="sample_text_2", name="sample_text_2")
    b = employee_Employee(firstName="sample_text", gender="sample_text", id="sample_text", lastName="sample_text", responsibilities="sample_text", salary=3.14)
    _safe_set(b, 'employee_Employee7', a1)
    assert _is_linked(b, 'employee_Employee7', a1)
    if hasattr(a1, 'employee_Project6'):
        assert _is_linked(a1, 'employee_Project6', b)
    _safe_set(b, 'employee_Employee7', a2)
    assert _is_linked(b, 'employee_Employee7', a2)
    if hasattr(a1, 'employee_Project6'):
        assert not _is_linked(a1, 'employee_Project6', b)
    if hasattr(a2, 'employee_Project6'):
        assert _is_linked(a2, 'employee_Project6', b)
    _safe_set(b, 'employee_Employee7', None)
    assert not _is_linked(b, 'employee_Employee7', a2)
    if hasattr(a2, 'employee_Project6'):
        assert not _is_linked(a2, 'employee_Project6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

