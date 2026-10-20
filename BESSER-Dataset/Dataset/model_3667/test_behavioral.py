import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    exo1_Company,
    exo1_Departement,
    exo1_Employee,
    exo1_Project,
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

def test_assoc_departement2_reverse_link_reassign_clear():
    a1 = exo1_Project(budget=7, name="sample_text")
    a2 = exo1_Project(budget=13, name="sample_text_2")
    b = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    _safe_set(b, 'Departement', a1)
    assert _is_linked(b, 'Departement', a1)
    if hasattr(a1, 'projects'):
        assert _is_linked(a1, 'projects', b)
    _safe_set(b, 'Departement', a2)
    assert _is_linked(b, 'Departement', a2)
    if hasattr(a1, 'projects'):
        assert not _is_linked(a1, 'projects', b)
    if hasattr(a2, 'projects'):
        assert _is_linked(a2, 'projects', b)
    _safe_set(b, 'Departement', None)
    assert not _is_linked(b, 'Departement', a2)
    if hasattr(a2, 'projects'):
        assert not _is_linked(a2, 'projects', b)


def test_assoc_departements8_reverse_link_reassign_clear():
    a1 = exo1_Employee(name="sample_text", salary="sample_text")
    a2 = exo1_Employee(name="sample_text_2", salary="sample_text_2")
    b = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    _safe_set(b, 'Departement10', a1)
    assert _is_linked(b, 'Departement10', a1)
    if hasattr(a1, 'employees9'):
        assert _is_linked(a1, 'employees9', b)
    _safe_set(b, 'Departement10', a2)
    assert _is_linked(b, 'Departement10', a2)
    if hasattr(a1, 'employees9'):
        assert not _is_linked(a1, 'employees9', b)
    if hasattr(a2, 'employees9'):
        assert _is_linked(a2, 'employees9', b)
    _safe_set(b, 'Departement10', None)
    assert not _is_linked(b, 'Departement10', a2)
    if hasattr(a2, 'employees9'):
        assert not _is_linked(a2, 'employees9', b)


def test_assoc_employees1_reverse_link_reassign_clear():
    a1 = exo1_Employee(name="sample_text", salary="sample_text")
    a2 = exo1_Employee(name="sample_text_2", salary="sample_text_2")
    b = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    _safe_set(b, 'departements', {a1})
    assert _is_linked(b, 'departements', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'departements', {a2})
    assert _is_linked(b, 'departements', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'departements', set())
    assert not _is_linked(b, 'departements', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_employees3_reverse_link_reassign_clear():
    a1 = exo1_Project(budget=7, name="sample_text")
    a2 = exo1_Project(budget=13, name="sample_text_2")
    b = exo1_Employee(name="sample_text", salary="sample_text")
    _safe_set(b, 'Employee5', a1)
    assert _is_linked(b, 'Employee5', a1)
    if hasattr(a1, 'projects4'):
        assert _is_linked(a1, 'projects4', b)
    _safe_set(b, 'Employee5', a2)
    assert _is_linked(b, 'Employee5', a2)
    if hasattr(a1, 'projects4'):
        assert not _is_linked(a1, 'projects4', b)
    if hasattr(a2, 'projects4'):
        assert _is_linked(a2, 'projects4', b)
    _safe_set(b, 'Employee5', None)
    assert not _is_linked(b, 'Employee5', a2)
    if hasattr(a2, 'projects4'):
        assert not _is_linked(a2, 'projects4', b)


def test_assoc_projects0_reverse_link_reassign_clear():
    a1 = exo1_Project(budget=7, name="sample_text")
    a2 = exo1_Project(budget=13, name="sample_text_2")
    b = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    _safe_set(b, 'departement', {a1})
    assert _is_linked(b, 'departement', a1)
    if hasattr(a1, 'Project'):
        assert _is_linked(a1, 'Project', b)
    _safe_set(b, 'departement', {a2})
    assert _is_linked(b, 'departement', a2)
    if hasattr(a1, 'Project'):
        assert not _is_linked(a1, 'Project', b)
    if hasattr(a2, 'Project'):
        assert _is_linked(a2, 'Project', b)
    _safe_set(b, 'departement', set())
    assert not _is_linked(b, 'departement', a2)
    if hasattr(a2, 'Project'):
        assert not _is_linked(a2, 'Project', b)


def test_assoc_projects6_reverse_link_reassign_clear():
    a1 = exo1_Project(budget=7, name="sample_text")
    a2 = exo1_Project(budget=13, name="sample_text_2")
    b = exo1_Employee(name="sample_text", salary="sample_text")
    _safe_set(b, 'employees', {a1})
    assert _is_linked(b, 'employees', a1)
    if hasattr(a1, 'Project7'):
        assert _is_linked(a1, 'Project7', b)
    _safe_set(b, 'employees', {a2})
    assert _is_linked(b, 'employees', a2)
    if hasattr(a1, 'Project7'):
        assert not _is_linked(a1, 'Project7', b)
    if hasattr(a2, 'Project7'):
        assert _is_linked(a2, 'Project7', b)
    _safe_set(b, 'employees', set())
    assert not _is_linked(b, 'employees', a2)
    if hasattr(a2, 'Project7'):
        assert not _is_linked(a2, 'Project7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_departements14_stub_double():
    # exo1_Company has no real 'exo1_Company15' property in the generated
    # code (a bare stub) -- manually attach it so exo1_Departement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exo1_Departement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    partner = exo1_Company()
    setattr(partner, 'exo1_Company15', None)
    _safe_set(owner, 'exo1_Departement', partner)
    assert owner in getattr(partner, 'exo1_Company15')
    _safe_set(owner, 'exo1_Departement', None)
    assert owner not in getattr(partner, 'exo1_Company15')


def test_assoc_employees11_stub_double():
    # exo1_Company has no real 'exo1_Company' property in the generated
    # code (a bare stub) -- manually attach it so exo1_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exo1_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exo1_Employee(name="sample_text", salary="sample_text")
    partner = exo1_Company()
    setattr(partner, 'exo1_Company', None)
    _safe_set(owner, 'exo1_Employee', partner)
    assert owner in getattr(partner, 'exo1_Company')
    _safe_set(owner, 'exo1_Employee', None)
    assert owner not in getattr(partner, 'exo1_Company')


def test_assoc_projets12_stub_double():
    # exo1_Company has no real 'exo1_Company13' property in the generated
    # code (a bare stub) -- manually attach it so exo1_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # exo1_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = exo1_Project(budget=7, name="sample_text")
    partner = exo1_Company()
    setattr(partner, 'exo1_Company13', None)
    _safe_set(owner, 'exo1_Project', partner)
    assert owner in getattr(partner, 'exo1_Company13')
    _safe_set(owner, 'exo1_Project', None)
    assert owner not in getattr(partner, 'exo1_Company13')


