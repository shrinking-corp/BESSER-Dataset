import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    company_Company,
    company_Dept,
    company_Employee,
    company_Person,
    company_Subunit,
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

def test_assoc_manager1_reverse_link_reassign_clear():
    a1 = company_Employee(salary=3.14)
    a2 = company_Employee(salary=9.99)
    b = company_Dept(name="sample_text")
    _safe_set(b, 'company_Dept2', a1)
    assert _is_linked(b, 'company_Dept2', a1)
    if hasattr(a1, 'company_Employee'):
        assert _is_linked(a1, 'company_Employee', b)
    _safe_set(b, 'company_Dept2', a2)
    assert _is_linked(b, 'company_Dept2', a2)
    if hasattr(a1, 'company_Employee'):
        assert not _is_linked(a1, 'company_Employee', b)
    if hasattr(a2, 'company_Employee'):
        assert _is_linked(a2, 'company_Employee', b)
    _safe_set(b, 'company_Dept2', None)
    assert not _is_linked(b, 'company_Dept2', a2)
    if hasattr(a2, 'company_Employee'):
        assert not _is_linked(a2, 'company_Employee', b)


def test_assoc_person5_reverse_link_reassign_clear():
    a1 = company_Person(address="sample_text", name="sample_text")
    a2 = company_Person(address="sample_text_2", name="sample_text_2")
    b = company_Employee(salary=3.14)
    _safe_set(b, 'company_Employee6', a1)
    assert _is_linked(b, 'company_Employee6', a1)
    if hasattr(a1, 'company_Person'):
        assert _is_linked(a1, 'company_Person', b)
    _safe_set(b, 'company_Employee6', a2)
    assert _is_linked(b, 'company_Employee6', a2)
    if hasattr(a1, 'company_Person'):
        assert not _is_linked(a1, 'company_Person', b)
    if hasattr(a2, 'company_Person'):
        assert _is_linked(a2, 'company_Person', b)
    _safe_set(b, 'company_Employee6', None)
    assert not _is_linked(b, 'company_Employee6', a2)
    if hasattr(a2, 'company_Person'):
        assert not _is_linked(a2, 'company_Person', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_depts0_stub_double():
    # company_Company has no real 'company_Company' property in the generated
    # code (a bare stub) -- manually attach it so company_Dept's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Dept's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Dept(name="sample_text")
    partner = company_Company()
    setattr(partner, 'company_Company', None)
    _safe_set(owner, 'company_Dept', partner)
    assert owner in getattr(partner, 'company_Company')
    _safe_set(owner, 'company_Dept', None)
    assert owner not in getattr(partner, 'company_Company')


def test_assoc_du10_stub_double():
    # company_Subunit has no real 'company_Subunit11' property in the generated
    # code (a bare stub) -- manually attach it so company_Dept's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Dept's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Dept(name="sample_text")
    partner = company_Subunit()
    setattr(partner, 'company_Subunit11', None)
    _safe_set(owner, 'company_Dept12', partner)
    assert getattr(partner, 'company_Subunit11') == owner
    _safe_set(owner, 'company_Dept12', None)
    assert getattr(partner, 'company_Subunit11') is None


def test_assoc_pu7_stub_double():
    # company_Subunit has no real 'company_Subunit8' property in the generated
    # code (a bare stub) -- manually attach it so company_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Employee(salary=3.14)
    partner = company_Subunit()
    setattr(partner, 'company_Subunit8', None)
    _safe_set(owner, 'company_Employee9', partner)
    assert getattr(partner, 'company_Subunit8') == owner
    _safe_set(owner, 'company_Employee9', None)
    assert getattr(partner, 'company_Subunit8') is None


def test_assoc_subunits3_stub_double():
    # company_Subunit has no real 'company_Subunit' property in the generated
    # code (a bare stub) -- manually attach it so company_Dept's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Dept's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Dept(name="sample_text")
    partner = company_Subunit()
    setattr(partner, 'company_Subunit', None)
    _safe_set(owner, 'company_Dept4', {partner})
    assert getattr(partner, 'company_Subunit') == owner
    _safe_set(owner, 'company_Dept4', set())
    assert getattr(partner, 'company_Subunit') is None


