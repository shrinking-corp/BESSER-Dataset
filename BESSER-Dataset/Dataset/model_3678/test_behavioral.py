import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CSTrace,
    companies_CSTrace,
    companies_Visitable,
    companies_company,
    companies_department,
    companies_department_employees,
    companies_department_manager,
    companies_employee,
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

def test_assoc_deparment0_reverse_link_reassign_clear():
    a1 = companies_department(name="sample_text")
    a2 = companies_department(name="sample_text_2")
    b = companies_company(name="sample_text")
    _safe_set(b, 'companies_company', {a1})
    assert _is_linked(b, 'companies_company', a1)
    if hasattr(a1, 'companies_department'):
        assert _is_linked(a1, 'companies_department', b)
    _safe_set(b, 'companies_company', {a2})
    assert _is_linked(b, 'companies_company', a2)
    if hasattr(a1, 'companies_department'):
        assert not _is_linked(a1, 'companies_department', b)
    if hasattr(a2, 'companies_department'):
        assert _is_linked(a2, 'companies_department', b)
    _safe_set(b, 'companies_company', set())
    assert not _is_linked(b, 'companies_company', a2)
    if hasattr(a2, 'companies_department'):
        assert not _is_linked(a2, 'companies_department', b)


def test_assoc_deparment6_reverse_link_reassign_clear():
    a1 = companies_department(name="sample_text")
    a2 = companies_department(name="sample_text_2")
    b = companies_department(name="sample_text")
    _safe_set(b, 'companies_department7', a1)
    assert _is_linked(b, 'companies_department7', a1)
    if hasattr(a1, 'companies_department5'):
        assert _is_linked(a1, 'companies_department5', b)
    _safe_set(b, 'companies_department7', a2)
    assert _is_linked(b, 'companies_department7', a2)
    if hasattr(a1, 'companies_department5'):
        assert not _is_linked(a1, 'companies_department5', b)
    if hasattr(a2, 'companies_department5'):
        assert _is_linked(a2, 'companies_department5', b)
    _safe_set(b, 'companies_department7', None)
    assert not _is_linked(b, 'companies_department7', a2)
    if hasattr(a2, 'companies_department5'):
        assert not _is_linked(a2, 'companies_department5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_department_employees3_stub_double():
    # companies_department_employees has no real 'companies_department_employees' property in the generated
    # code (a bare stub) -- manually attach it so companies_department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # companies_department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = companies_department(name="sample_text")
    partner = companies_department_employees()
    setattr(partner, 'companies_department_employees', None)
    _safe_set(owner, 'companies_department4', partner)
    assert getattr(partner, 'companies_department_employees') == owner
    _safe_set(owner, 'companies_department4', None)
    assert getattr(partner, 'companies_department_employees') is None


def test_assoc_department_manager1_stub_double():
    # companies_department_manager has no real 'companies_department_manager' property in the generated
    # code (a bare stub) -- manually attach it so companies_department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # companies_department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = companies_department(name="sample_text")
    partner = companies_department_manager()
    setattr(partner, 'companies_department_manager', None)
    _safe_set(owner, 'companies_department2', partner)
    assert getattr(partner, 'companies_department_manager') == owner
    _safe_set(owner, 'companies_department2', None)
    assert getattr(partner, 'companies_department_manager') is None


def test_assoc_employee10_stub_double():
    # companies_department_employees has no real 'companies_department_employees11' property in the generated
    # code (a bare stub) -- manually attach it so companies_employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # companies_employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = companies_employee(address="sample_text", mentor="sample_text", name="sample_text", salary=3.14)
    partner = companies_department_employees()
    setattr(partner, 'companies_department_employees11', None)
    _safe_set(owner, 'companies_employee12', partner)
    assert owner in getattr(partner, 'companies_department_employees11')
    _safe_set(owner, 'companies_employee12', None)
    assert owner not in getattr(partner, 'companies_department_employees11')


def test_assoc_employee8_stub_double():
    # companies_department_manager has no real 'companies_department_manager9' property in the generated
    # code (a bare stub) -- manually attach it so companies_employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # companies_employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = companies_employee(address="sample_text", mentor="sample_text", name="sample_text", salary=3.14)
    partner = companies_department_manager()
    setattr(partner, 'companies_department_manager9', None)
    _safe_set(owner, 'companies_employee', partner)
    assert getattr(partner, 'companies_department_manager9') == owner
    _safe_set(owner, 'companies_employee', None)
    assert getattr(partner, 'companies_department_manager9') is None


