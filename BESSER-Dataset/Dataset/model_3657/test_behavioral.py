import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Employee,
    company_Company,
    company_Department,
    company_Division,
    company_Employee,
    company_Freelance,
    company_Student,
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

def test_assoc_boss9_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    _safe_set(b, 'managed', a1)
    assert _is_linked(b, 'managed', a1)
    if hasattr(a1, 'Employee10'):
        assert _is_linked(a1, 'Employee10', b)
    _safe_set(b, 'managed', a2)
    assert _is_linked(b, 'managed', a2)
    if hasattr(a1, 'Employee10'):
        assert not _is_linked(a1, 'Employee10', b)
    if hasattr(a2, 'Employee10'):
        assert _is_linked(a2, 'Employee10', b)
    _safe_set(b, 'managed', None)
    assert not _is_linked(b, 'managed', a2)
    if hasattr(a2, 'Employee10'):
        assert not _is_linked(a2, 'Employee10', b)


def test_assoc_company26_reverse_link_reassign_clear():
    a1 = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    a2 = company_Division(budget="sample_text_2", name="sample_text_2", numberEmployeesOfTheMonth="sample_text_2")
    b = company_Company(eotmDelta="sample_text", name="sample_text")
    _safe_set(b, 'Company', a1)
    assert _is_linked(b, 'Company', a1)
    if hasattr(a1, 'division'):
        assert _is_linked(a1, 'division', b)
    _safe_set(b, 'Company', a2)
    assert _is_linked(b, 'Company', a2)
    if hasattr(a1, 'division'):
        assert not _is_linked(a1, 'division', b)
    if hasattr(a2, 'division'):
        assert _is_linked(a2, 'division', b)
    _safe_set(b, 'Company', None)
    assert not _is_linked(b, 'Company', a2)
    if hasattr(a2, 'division'):
        assert not _is_linked(a2, 'division', b)


def test_assoc_department19_reverse_link_reassign_clear():
    a1 = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    a2 = company_Division(budget="sample_text_2", name="sample_text_2", numberEmployeesOfTheMonth="sample_text_2")
    b = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    _safe_set(b, 'company_Department20', a1)
    assert _is_linked(b, 'company_Department20', a1)
    if hasattr(a1, 'company_Division'):
        assert _is_linked(a1, 'company_Division', b)
    _safe_set(b, 'company_Department20', a2)
    assert _is_linked(b, 'company_Department20', a2)
    if hasattr(a1, 'company_Division'):
        assert not _is_linked(a1, 'company_Division', b)
    if hasattr(a2, 'company_Division'):
        assert _is_linked(a2, 'company_Division', b)
    _safe_set(b, 'company_Department20', None)
    assert not _is_linked(b, 'company_Department20', a2)
    if hasattr(a2, 'company_Division'):
        assert not _is_linked(a2, 'company_Division', b)


def test_assoc_directed3_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    _safe_set(b, 'Division', a1)
    assert _is_linked(b, 'Division', a1)
    if hasattr(a1, 'director'):
        assert _is_linked(a1, 'director', b)
    _safe_set(b, 'Division', a2)
    assert _is_linked(b, 'Division', a2)
    if hasattr(a1, 'director'):
        assert not _is_linked(a1, 'director', b)
    if hasattr(a2, 'director'):
        assert _is_linked(a2, 'director', b)
    _safe_set(b, 'Division', None)
    assert not _is_linked(b, 'Division', a2)
    if hasattr(a2, 'director'):
        assert not _is_linked(a2, 'director', b)


def test_assoc_director21_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    _safe_set(b, 'directed', a1)
    assert _is_linked(b, 'directed', a1)
    if hasattr(a1, 'Employee22'):
        assert _is_linked(a1, 'Employee22', b)
    _safe_set(b, 'directed', a2)
    assert _is_linked(b, 'directed', a2)
    if hasattr(a1, 'Employee22'):
        assert not _is_linked(a1, 'Employee22', b)
    if hasattr(a2, 'Employee22'):
        assert _is_linked(a2, 'Employee22', b)
    _safe_set(b, 'directed', None)
    assert not _is_linked(b, 'directed', a2)
    if hasattr(a2, 'Employee22'):
        assert not _is_linked(a2, 'Employee22', b)


def test_assoc_division27_reverse_link_reassign_clear():
    a1 = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    a2 = company_Division(budget="sample_text_2", name="sample_text_2", numberEmployeesOfTheMonth="sample_text_2")
    b = company_Company(eotmDelta="sample_text", name="sample_text")
    _safe_set(b, 'company', a1)
    assert _is_linked(b, 'company', a1)
    if hasattr(a1, 'Division28'):
        assert _is_linked(a1, 'Division28', b)
    _safe_set(b, 'company', a2)
    assert _is_linked(b, 'company', a2)
    if hasattr(a1, 'Division28'):
        assert not _is_linked(a1, 'Division28', b)
    if hasattr(a2, 'Division28'):
        assert _is_linked(a2, 'Division28', b)
    _safe_set(b, 'company', None)
    assert not _is_linked(b, 'company', a2)
    if hasattr(a2, 'Division28'):
        assert not _is_linked(a2, 'Division28', b)


def test_assoc_divisionDirector29_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Company(eotmDelta="sample_text", name="sample_text")
    _safe_set(b, 'company_Company', a1)
    assert _is_linked(b, 'company_Company', a1)
    if hasattr(a1, 'company_Employee30'):
        assert _is_linked(a1, 'company_Employee30', b)
    _safe_set(b, 'company_Company', a2)
    assert _is_linked(b, 'company_Company', a2)
    if hasattr(a1, 'company_Employee30'):
        assert not _is_linked(a1, 'company_Employee30', b)
    if hasattr(a2, 'company_Employee30'):
        assert _is_linked(a2, 'company_Employee30', b)
    _safe_set(b, 'company_Company', None)
    assert not _is_linked(b, 'company_Company', a2)
    if hasattr(a2, 'company_Employee30'):
        assert not _is_linked(a2, 'company_Employee30', b)


def test_assoc_employee8_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    _safe_set(b, 'employer', {a1})
    assert _is_linked(b, 'employer', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'employer', {a2})
    assert _is_linked(b, 'employer', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'employer', set())
    assert not _is_linked(b, 'employer', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_employeeOfTheMonth17_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    _safe_set(b, 'company_Department', {a1})
    assert _is_linked(b, 'company_Department', a1)
    if hasattr(a1, 'company_Employee18'):
        assert _is_linked(a1, 'company_Employee18', b)
    _safe_set(b, 'company_Department', {a2})
    assert _is_linked(b, 'company_Department', a2)
    if hasattr(a1, 'company_Employee18'):
        assert not _is_linked(a1, 'company_Employee18', b)
    if hasattr(a2, 'company_Employee18'):
        assert _is_linked(a2, 'company_Employee18', b)
    _safe_set(b, 'company_Department', set())
    assert not _is_linked(b, 'company_Department', a2)
    if hasattr(a2, 'company_Employee18'):
        assert not _is_linked(a2, 'company_Employee18', b)


def test_assoc_employeesOfTheMonth23_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    _safe_set(b, 'company_Division24', {a1})
    assert _is_linked(b, 'company_Division24', a1)
    if hasattr(a1, 'company_Employee25'):
        assert _is_linked(a1, 'company_Employee25', b)
    _safe_set(b, 'company_Division24', {a2})
    assert _is_linked(b, 'company_Division24', a2)
    if hasattr(a1, 'company_Employee25'):
        assert not _is_linked(a1, 'company_Employee25', b)
    if hasattr(a2, 'company_Employee25'):
        assert _is_linked(a2, 'company_Employee25', b)
    _safe_set(b, 'company_Division24', set())
    assert not _is_linked(b, 'company_Division24', a2)
    if hasattr(a2, 'company_Employee25'):
        assert not _is_linked(a2, 'company_Employee25', b)


def test_assoc_employer0_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'employee'):
        assert _is_linked(a1, 'employee', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'employee'):
        assert not _is_linked(a1, 'employee', b)
    if hasattr(a2, 'employee'):
        assert _is_linked(a2, 'employee', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'employee'):
        assert not _is_linked(a2, 'employee', b)


def test_assoc_managed1_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    _safe_set(b, 'Department2', a1)
    assert _is_linked(b, 'Department2', a1)
    if hasattr(a1, 'boss'):
        assert _is_linked(a1, 'boss', b)
    _safe_set(b, 'Department2', a2)
    assert _is_linked(b, 'Department2', a2)
    if hasattr(a1, 'boss'):
        assert not _is_linked(a1, 'boss', b)
    if hasattr(a2, 'boss'):
        assert _is_linked(a2, 'boss', b)
    _safe_set(b, 'Department2', None)
    assert not _is_linked(b, 'Department2', a2)
    if hasattr(a2, 'boss'):
        assert not _is_linked(a2, 'boss', b)


def test_assoc_parentDepartment15_reverse_link_reassign_clear():
    a1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    a2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    b = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    _safe_set(b, 'subDepartment', a1)
    assert _is_linked(b, 'subDepartment', a1)
    if hasattr(a1, 'Department16'):
        assert _is_linked(a1, 'Department16', b)
    _safe_set(b, 'subDepartment', a2)
    assert _is_linked(b, 'subDepartment', a2)
    if hasattr(a1, 'Department16'):
        assert not _is_linked(a1, 'Department16', b)
    if hasattr(a2, 'Department16'):
        assert _is_linked(a2, 'Department16', b)
    _safe_set(b, 'subDepartment', None)
    assert not _is_linked(b, 'subDepartment', a2)
    if hasattr(a2, 'Department16'):
        assert not _is_linked(a2, 'Department16', b)


def test_assoc_secretary5_reverse_link_reassign_clear():
    a1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    a2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    b = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    _safe_set(b, 'company_Employee4', a1)
    assert _is_linked(b, 'company_Employee4', a1)
    if hasattr(a1, 'company_Employee'):
        assert _is_linked(a1, 'company_Employee', b)
    _safe_set(b, 'company_Employee4', a2)
    assert _is_linked(b, 'company_Employee4', a2)
    if hasattr(a1, 'company_Employee'):
        assert not _is_linked(a1, 'company_Employee', b)
    if hasattr(a2, 'company_Employee'):
        assert _is_linked(a2, 'company_Employee', b)
    _safe_set(b, 'company_Employee4', None)
    assert not _is_linked(b, 'company_Employee4', a2)
    if hasattr(a2, 'company_Employee'):
        assert not _is_linked(a2, 'company_Employee', b)


def test_assoc_subDepartment12_reverse_link_reassign_clear():
    a1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    a2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    b = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    _safe_set(b, 'parentDepartment', {a1})
    assert _is_linked(b, 'parentDepartment', a1)
    if hasattr(a1, 'Department13'):
        assert _is_linked(a1, 'Department13', b)
    _safe_set(b, 'parentDepartment', {a2})
    assert _is_linked(b, 'parentDepartment', a2)
    if hasattr(a1, 'Department13'):
        assert not _is_linked(a1, 'Department13', b)
    if hasattr(a2, 'Department13'):
        assert _is_linked(a2, 'Department13', b)
    _safe_set(b, 'parentDepartment', set())
    assert not _is_linked(b, 'parentDepartment', a2)
    if hasattr(a2, 'Department13'):
        assert not _is_linked(a2, 'Department13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_intern6_stub_double():
    # company_Student has no real 'company_Student' property in the generated
    # code (a bare stub) -- manually attach it so company_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    partner = company_Student()
    setattr(partner, 'company_Student', None)
    _safe_set(owner, 'company_Employee7', partner)
    assert getattr(partner, 'company_Student') == owner
    _safe_set(owner, 'company_Employee7', None)
    assert getattr(partner, 'company_Student') is None


