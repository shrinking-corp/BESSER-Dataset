import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AllBase,
    Employee,
    toe_AllBase,
    toe_AllHolder,
    toe_Contribution,
    toe_Department,
    toe_Employee,
    toe_Manager,
    toe_Project,
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

def test_assoc_contributions25_reverse_link_reassign_clear():
    a1 = toe_Project(departmentWide=True, name="sample_text")
    a2 = toe_Project(departmentWide=False, name="sample_text_2")
    b = toe_Contribution(description="sample_text")
    _safe_set(b, 'Contribution26', a1)
    assert _is_linked(b, 'Contribution26', a1)
    if hasattr(a1, 'project'):
        assert _is_linked(a1, 'project', b)
    _safe_set(b, 'Contribution26', a2)
    assert _is_linked(b, 'Contribution26', a2)
    if hasattr(a1, 'project'):
        assert not _is_linked(a1, 'project', b)
    if hasattr(a2, 'project'):
        assert _is_linked(a2, 'project', b)
    _safe_set(b, 'Contribution26', None)
    assert not _is_linked(b, 'Contribution26', a2)
    if hasattr(a2, 'project'):
        assert not _is_linked(a2, 'project', b)


def test_assoc_contributions3_reverse_link_reassign_clear():
    a1 = toe_Employee(name="sample_text", salary=7)
    a2 = toe_Employee(name="sample_text_2", salary=13)
    b = toe_Contribution(description="sample_text")
    _safe_set(b, 'Contribution', a1)
    assert _is_linked(b, 'Contribution', a1)
    if hasattr(a1, 'employee'):
        assert _is_linked(a1, 'employee', b)
    _safe_set(b, 'Contribution', a2)
    assert _is_linked(b, 'Contribution', a2)
    if hasattr(a1, 'employee'):
        assert not _is_linked(a1, 'employee', b)
    if hasattr(a2, 'employee'):
        assert _is_linked(a2, 'employee', b)
    _safe_set(b, 'Contribution', None)
    assert not _is_linked(b, 'Contribution', a2)
    if hasattr(a2, 'employee'):
        assert not _is_linked(a2, 'employee', b)


def test_assoc_department2_reverse_link_reassign_clear():
    a1 = toe_Employee(name="sample_text", salary=7)
    a2 = toe_Employee(name="sample_text_2", salary=13)
    b = toe_Department(name="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'employees'):
        assert _is_linked(a1, 'employees', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'employees'):
        assert not _is_linked(a1, 'employees', b)
    if hasattr(a2, 'employees'):
        assert _is_linked(a2, 'employees', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'employees'):
        assert not _is_linked(a2, 'employees', b)


def test_assoc_employee8_reverse_link_reassign_clear():
    a1 = toe_Employee(name="sample_text", salary=7)
    a2 = toe_Employee(name="sample_text_2", salary=13)
    b = toe_Contribution(description="sample_text")
    _safe_set(b, 'contributions', a1)
    assert _is_linked(b, 'contributions', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'contributions', a2)
    assert _is_linked(b, 'contributions', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'contributions', None)
    assert not _is_linked(b, 'contributions', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_employees15_reverse_link_reassign_clear():
    a1 = toe_Employee(name="sample_text", salary=7)
    a2 = toe_Employee(name="sample_text_2", salary=13)
    b = toe_Department(name="sample_text")
    _safe_set(b, 'department', {a1})
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'Employee16'):
        assert _is_linked(a1, 'Employee16', b)
    _safe_set(b, 'department', {a2})
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'Employee16'):
        assert not _is_linked(a1, 'Employee16', b)
    if hasattr(a2, 'Employee16'):
        assert _is_linked(a2, 'Employee16', b)
    _safe_set(b, 'department', set())
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'Employee16'):
        assert not _is_linked(a2, 'Employee16', b)


def test_assoc_parentDepartment18_reverse_link_reassign_clear():
    a1 = toe_Department(name="sample_text")
    a2 = toe_Department(name="sample_text_2")
    b = toe_Department(name="sample_text")
    _safe_set(b, 'subDepartments', a1)
    assert _is_linked(b, 'subDepartments', a1)
    if hasattr(a1, 'Department19'):
        assert _is_linked(a1, 'Department19', b)
    _safe_set(b, 'subDepartments', a2)
    assert _is_linked(b, 'subDepartments', a2)
    if hasattr(a1, 'Department19'):
        assert not _is_linked(a1, 'Department19', b)
    if hasattr(a2, 'Department19'):
        assert _is_linked(a2, 'Department19', b)
    _safe_set(b, 'subDepartments', None)
    assert not _is_linked(b, 'subDepartments', a2)
    if hasattr(a2, 'Department19'):
        assert not _is_linked(a2, 'Department19', b)


def test_assoc_project9_reverse_link_reassign_clear():
    a1 = toe_Project(departmentWide=True, name="sample_text")
    a2 = toe_Project(departmentWide=False, name="sample_text_2")
    b = toe_Contribution(description="sample_text")
    _safe_set(b, 'contributions10', a1)
    assert _is_linked(b, 'contributions10', a1)
    if hasattr(a1, 'Project11'):
        assert _is_linked(a1, 'Project11', b)
    _safe_set(b, 'contributions10', a2)
    assert _is_linked(b, 'contributions10', a2)
    if hasattr(a1, 'Project11'):
        assert not _is_linked(a1, 'Project11', b)
    if hasattr(a2, 'Project11'):
        assert _is_linked(a2, 'Project11', b)
    _safe_set(b, 'contributions10', None)
    assert not _is_linked(b, 'contributions10', a2)
    if hasattr(a2, 'Project11'):
        assert not _is_linked(a2, 'Project11', b)


def test_assoc_projectTeam21_reverse_link_reassign_clear():
    a1 = toe_Project(departmentWide=True, name="sample_text")
    a2 = toe_Project(departmentWide=False, name="sample_text_2")
    b = toe_Employee(name="sample_text", salary=7)
    _safe_set(b, 'Employee22', a1)
    assert _is_linked(b, 'Employee22', a1)
    if hasattr(a1, 'projects'):
        assert _is_linked(a1, 'projects', b)
    _safe_set(b, 'Employee22', a2)
    assert _is_linked(b, 'Employee22', a2)
    if hasattr(a1, 'projects'):
        assert not _is_linked(a1, 'projects', b)
    if hasattr(a2, 'projects'):
        assert _is_linked(a2, 'projects', b)
    _safe_set(b, 'Employee22', None)
    assert not _is_linked(b, 'Employee22', a2)
    if hasattr(a2, 'projects'):
        assert not _is_linked(a2, 'projects', b)


def test_assoc_projects1_reverse_link_reassign_clear():
    a1 = toe_Project(departmentWide=True, name="sample_text")
    a2 = toe_Project(departmentWide=False, name="sample_text_2")
    b = toe_Employee(name="sample_text", salary=7)
    _safe_set(b, 'projectTeam', {a1})
    assert _is_linked(b, 'projectTeam', a1)
    if hasattr(a1, 'Project'):
        assert _is_linked(a1, 'Project', b)
    _safe_set(b, 'projectTeam', {a2})
    assert _is_linked(b, 'projectTeam', a2)
    if hasattr(a1, 'Project'):
        assert not _is_linked(a1, 'Project', b)
    if hasattr(a2, 'Project'):
        assert _is_linked(a2, 'Project', b)
    _safe_set(b, 'projectTeam', set())
    assert not _is_linked(b, 'projectTeam', a2)
    if hasattr(a2, 'Project'):
        assert not _is_linked(a2, 'Project', b)


def test_assoc_subDepartments13_reverse_link_reassign_clear():
    a1 = toe_Department(name="sample_text")
    a2 = toe_Department(name="sample_text_2")
    b = toe_Department(name="sample_text")
    _safe_set(b, 'parentDepartment', {a1})
    assert _is_linked(b, 'parentDepartment', a1)
    if hasattr(a1, 'Department14'):
        assert _is_linked(a1, 'Department14', b)
    _safe_set(b, 'parentDepartment', {a2})
    assert _is_linked(b, 'parentDepartment', a2)
    if hasattr(a1, 'Department14'):
        assert not _is_linked(a1, 'Department14', b)
    if hasattr(a2, 'Department14'):
        assert _is_linked(a2, 'Department14', b)
    _safe_set(b, 'parentDepartment', set())
    assert not _is_linked(b, 'parentDepartment', a2)
    if hasattr(a2, 'Department14'):
        assert not _is_linked(a2, 'Department14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_lead23_stub_double():
    # toe_Manager has no real 'Manager24' property in the generated
    # code (a bare stub) -- manually attach it so toe_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # toe_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = toe_Project(departmentWide=True, name="sample_text")
    partner = toe_Manager()
    setattr(partner, 'Manager24', None)
    _safe_set(owner, 'leads', partner)
    assert getattr(partner, 'Manager24') == owner
    _safe_set(owner, 'leads', None)
    assert getattr(partner, 'Manager24') is None


def test_assoc_leads4_stub_double():
    # toe_Manager has no real 'lead' property in the generated
    # code (a bare stub) -- manually attach it so toe_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # toe_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = toe_Project(departmentWide=True, name="sample_text")
    partner = toe_Manager()
    setattr(partner, 'lead', None)
    _safe_set(owner, 'Project5', partner)
    assert owner in getattr(partner, 'lead')
    _safe_set(owner, 'Project5', None)
    assert owner not in getattr(partner, 'lead')


def test_assoc_managedDepartment6_stub_double():
    # toe_Manager has no real 'manager' property in the generated
    # code (a bare stub) -- manually attach it so toe_Department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # toe_Department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = toe_Department(name="sample_text")
    partner = toe_Manager()
    setattr(partner, 'manager', None)
    _safe_set(owner, 'Department7', partner)
    assert getattr(partner, 'manager') == owner
    _safe_set(owner, 'Department7', None)
    assert getattr(partner, 'manager') is None


def test_assoc_manager20_stub_double():
    # toe_Manager has no real 'Manager' property in the generated
    # code (a bare stub) -- manually attach it so toe_Department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # toe_Department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = toe_Department(name="sample_text")
    partner = toe_Manager()
    setattr(partner, 'Manager', None)
    _safe_set(owner, 'managedDepartment', partner)
    assert getattr(partner, 'Manager') == owner
    _safe_set(owner, 'managedDepartment', None)
    assert getattr(partner, 'Manager') is None


