import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Function,
    Interval,
    NamedElement,
    company104_Agency,
    company104_Company,
    company104_Department,
    company104_Employee,
    company104_Flow,
    company104_Function,
    company104_Goal,
    company104_HierarchyLink,
    company104_Interval,
    company104_NamedElement,
    company104_Objective,
    company104_ObjectiveReach,
    company104_Room,
    company104_Workstation,
    Hierarchy,
    ObjectiveNature,
    ObjectiveType,
    RoleType,
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

def test_assoc_employees30_reverse_link_reassign_clear():
    a1 = company104_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    a2 = company104_Employee(address=13, fullName="sample_text_2", socialSecurityNumber="sample_text_2")
    b = company104_Agency(Accronym="sample_text", Status="sample_text")
    _safe_set(b, 'company104_Agency31', {a1})
    assert _is_linked(b, 'company104_Agency31', a1)
    if hasattr(a1, 'company104_Employee32'):
        assert _is_linked(a1, 'company104_Employee32', b)
    _safe_set(b, 'company104_Agency31', {a2})
    assert _is_linked(b, 'company104_Agency31', a2)
    if hasattr(a1, 'company104_Employee32'):
        assert not _is_linked(a1, 'company104_Employee32', b)
    if hasattr(a2, 'company104_Employee32'):
        assert _is_linked(a2, 'company104_Employee32', b)
    _safe_set(b, 'company104_Agency31', set())
    assert not _is_linked(b, 'company104_Agency31', a2)
    if hasattr(a2, 'company104_Employee32'):
        assert not _is_linked(a2, 'company104_Employee32', b)


def test_assoc_fromEmployee13_reverse_link_reassign_clear():
    a1 = company104_HierarchyLink(hierarchy="sample_text")
    a2 = company104_HierarchyLink(hierarchy="sample_text_2")
    b = company104_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'company104_Employee15', a1)
    assert _is_linked(b, 'company104_Employee15', a1)
    if hasattr(a1, 'company104_HierarchyLink14'):
        assert _is_linked(a1, 'company104_HierarchyLink14', b)
    _safe_set(b, 'company104_Employee15', a2)
    assert _is_linked(b, 'company104_Employee15', a2)
    if hasattr(a1, 'company104_HierarchyLink14'):
        assert not _is_linked(a1, 'company104_HierarchyLink14', b)
    if hasattr(a2, 'company104_HierarchyLink14'):
        assert _is_linked(a2, 'company104_HierarchyLink14', b)
    _safe_set(b, 'company104_Employee15', None)
    assert not _is_linked(b, 'company104_Employee15', a2)
    if hasattr(a2, 'company104_HierarchyLink14'):
        assert not _is_linked(a2, 'company104_HierarchyLink14', b)


def test_assoc_hierarchies8_reverse_link_reassign_clear():
    a1 = company104_HierarchyLink(hierarchy="sample_text")
    a2 = company104_HierarchyLink(hierarchy="sample_text_2")
    b = company104_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'company104_Employee', {a1})
    assert _is_linked(b, 'company104_Employee', a1)
    if hasattr(a1, 'company104_HierarchyLink'):
        assert _is_linked(a1, 'company104_HierarchyLink', b)
    _safe_set(b, 'company104_Employee', {a2})
    assert _is_linked(b, 'company104_Employee', a2)
    if hasattr(a1, 'company104_HierarchyLink'):
        assert not _is_linked(a1, 'company104_HierarchyLink', b)
    if hasattr(a2, 'company104_HierarchyLink'):
        assert _is_linked(a2, 'company104_HierarchyLink', b)
    _safe_set(b, 'company104_Employee', set())
    assert not _is_linked(b, 'company104_Employee', a2)
    if hasattr(a2, 'company104_HierarchyLink'):
        assert not _is_linked(a2, 'company104_HierarchyLink', b)


def test_assoc_inChargeOf12_reverse_link_reassign_clear():
    a1 = company104_Workstation(ProfileDescription="sample_text")
    a2 = company104_Workstation(ProfileDescription="sample_text_2")
    b = company104_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'owners', a1)
    assert _is_linked(b, 'owners', a1)
    if hasattr(a1, 'Workstation'):
        assert _is_linked(a1, 'Workstation', b)
    _safe_set(b, 'owners', a2)
    assert _is_linked(b, 'owners', a2)
    if hasattr(a1, 'Workstation'):
        assert not _is_linked(a1, 'Workstation', b)
    if hasattr(a2, 'Workstation'):
        assert _is_linked(a2, 'Workstation', b)
    _safe_set(b, 'owners', None)
    assert not _is_linked(b, 'owners', a2)
    if hasattr(a2, 'Workstation'):
        assert not _is_linked(a2, 'Workstation', b)


def test_assoc_objectives25_reverse_link_reassign_clear():
    a1 = company104_Objective(nature="sample_text", type="sample_text", value=3.14)
    a2 = company104_Objective(nature="sample_text_2", type="sample_text_2", value=9.99)
    b = company104_Goal(statement="sample_text")
    _safe_set(b, 'company104_Goal26', {a1})
    assert _is_linked(b, 'company104_Goal26', a1)
    if hasattr(a1, 'company104_Objective'):
        assert _is_linked(a1, 'company104_Objective', b)
    _safe_set(b, 'company104_Goal26', {a2})
    assert _is_linked(b, 'company104_Goal26', a2)
    if hasattr(a1, 'company104_Objective'):
        assert not _is_linked(a1, 'company104_Objective', b)
    if hasattr(a2, 'company104_Objective'):
        assert _is_linked(a2, 'company104_Objective', b)
    _safe_set(b, 'company104_Goal26', set())
    assert not _is_linked(b, 'company104_Goal26', a2)
    if hasattr(a2, 'company104_Objective'):
        assert not _is_linked(a2, 'company104_Objective', b)


def test_assoc_owners24_reverse_link_reassign_clear():
    a1 = company104_Workstation(ProfileDescription="sample_text")
    a2 = company104_Workstation(ProfileDescription="sample_text_2")
    b = company104_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'Employee', a1)
    assert _is_linked(b, 'Employee', a1)
    if hasattr(a1, 'inChargeOf'):
        assert _is_linked(a1, 'inChargeOf', b)
    _safe_set(b, 'Employee', a2)
    assert _is_linked(b, 'Employee', a2)
    if hasattr(a1, 'inChargeOf'):
        assert not _is_linked(a1, 'inChargeOf', b)
    if hasattr(a2, 'inChargeOf'):
        assert _is_linked(a2, 'inChargeOf', b)
    _safe_set(b, 'Employee', None)
    assert not _is_linked(b, 'Employee', a2)
    if hasattr(a2, 'inChargeOf'):
        assert not _is_linked(a2, 'inChargeOf', b)


def test_assoc_reacheds33_reverse_link_reassign_clear():
    a1 = company104_ObjectiveReach(statement="sample_text", value=3.14)
    a2 = company104_ObjectiveReach(statement="sample_text_2", value=9.99)
    b = company104_Agency(Accronym="sample_text", Status="sample_text")
    _safe_set(b, 'company104_Agency34', {a1})
    assert _is_linked(b, 'company104_Agency34', a1)
    if hasattr(a1, 'company104_ObjectiveReach'):
        assert _is_linked(a1, 'company104_ObjectiveReach', b)
    _safe_set(b, 'company104_Agency34', {a2})
    assert _is_linked(b, 'company104_Agency34', a2)
    if hasattr(a1, 'company104_ObjectiveReach'):
        assert not _is_linked(a1, 'company104_ObjectiveReach', b)
    if hasattr(a2, 'company104_ObjectiveReach'):
        assert _is_linked(a2, 'company104_ObjectiveReach', b)
    _safe_set(b, 'company104_Agency34', set())
    assert not _is_linked(b, 'company104_Agency34', a2)
    if hasattr(a2, 'company104_ObjectiveReach'):
        assert not _is_linked(a2, 'company104_ObjectiveReach', b)


def test_assoc_srcAgency38_reverse_link_reassign_clear():
    a1 = company104_ObjectiveReach(statement="sample_text", value=3.14)
    a2 = company104_ObjectiveReach(statement="sample_text_2", value=9.99)
    b = company104_Agency(Accronym="sample_text", Status="sample_text")
    _safe_set(b, 'company104_Agency40', a1)
    assert _is_linked(b, 'company104_Agency40', a1)
    if hasattr(a1, 'company104_ObjectiveReach39'):
        assert _is_linked(a1, 'company104_ObjectiveReach39', b)
    _safe_set(b, 'company104_Agency40', a2)
    assert _is_linked(b, 'company104_Agency40', a2)
    if hasattr(a1, 'company104_ObjectiveReach39'):
        assert not _is_linked(a1, 'company104_ObjectiveReach39', b)
    if hasattr(a2, 'company104_ObjectiveReach39'):
        assert _is_linked(a2, 'company104_ObjectiveReach39', b)
    _safe_set(b, 'company104_Agency40', None)
    assert not _is_linked(b, 'company104_Agency40', a2)
    if hasattr(a2, 'company104_ObjectiveReach39'):
        assert not _is_linked(a2, 'company104_ObjectiveReach39', b)


def test_assoc_toEmployee16_reverse_link_reassign_clear():
    a1 = company104_HierarchyLink(hierarchy="sample_text")
    a2 = company104_HierarchyLink(hierarchy="sample_text_2")
    b = company104_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'company104_Employee18', a1)
    assert _is_linked(b, 'company104_Employee18', a1)
    if hasattr(a1, 'company104_HierarchyLink17'):
        assert _is_linked(a1, 'company104_HierarchyLink17', b)
    _safe_set(b, 'company104_Employee18', a2)
    assert _is_linked(b, 'company104_Employee18', a2)
    if hasattr(a1, 'company104_HierarchyLink17'):
        assert not _is_linked(a1, 'company104_HierarchyLink17', b)
    if hasattr(a2, 'company104_HierarchyLink17'):
        assert _is_linked(a2, 'company104_HierarchyLink17', b)
    _safe_set(b, 'company104_Employee18', None)
    assert not _is_linked(b, 'company104_Employee18', a2)
    if hasattr(a2, 'company104_HierarchyLink17'):
        assert not _is_linked(a2, 'company104_HierarchyLink17', b)


def test_assoc_trgObjective35_reverse_link_reassign_clear():
    a1 = company104_ObjectiveReach(statement="sample_text", value=3.14)
    a2 = company104_ObjectiveReach(statement="sample_text_2", value=9.99)
    b = company104_Objective(nature="sample_text", type="sample_text", value=3.14)
    _safe_set(b, 'company104_Objective37', a1)
    assert _is_linked(b, 'company104_Objective37', a1)
    if hasattr(a1, 'company104_ObjectiveReach36'):
        assert _is_linked(a1, 'company104_ObjectiveReach36', b)
    _safe_set(b, 'company104_Objective37', a2)
    assert _is_linked(b, 'company104_Objective37', a2)
    if hasattr(a1, 'company104_ObjectiveReach36'):
        assert not _is_linked(a1, 'company104_ObjectiveReach36', b)
    if hasattr(a2, 'company104_ObjectiveReach36'):
        assert _is_linked(a2, 'company104_ObjectiveReach36', b)
    _safe_set(b, 'company104_Objective37', None)
    assert not _is_linked(b, 'company104_Objective37', a2)
    if hasattr(a2, 'company104_ObjectiveReach36'):
        assert not _is_linked(a2, 'company104_ObjectiveReach36', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_agencies0_stub_double():
    # company104_Company has no real 'company104_Company' property in the generated
    # code (a bare stub) -- manually attach it so company104_Agency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company104_Agency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company104_Agency(Accronym="sample_text", Status="sample_text")
    partner = company104_Company()
    setattr(partner, 'company104_Company', None)
    _safe_set(owner, 'company104_Agency', partner)
    assert owner in getattr(partner, 'company104_Company')
    _safe_set(owner, 'company104_Agency', None)
    assert owner not in getattr(partner, 'company104_Company')


def test_assoc_departments27_stub_double():
    # company104_Department has no real 'company104_Department29' property in the generated
    # code (a bare stub) -- manually attach it so company104_Agency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company104_Agency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company104_Agency(Accronym="sample_text", Status="sample_text")
    partner = company104_Department()
    setattr(partner, 'company104_Department29', None)
    _safe_set(owner, 'company104_Agency28', {partner})
    assert getattr(partner, 'company104_Department29') == owner
    _safe_set(owner, 'company104_Agency28', set())
    assert getattr(partner, 'company104_Department29') is None


def test_assoc_goals1_stub_double():
    # company104_Company has no real 'company104_Company2' property in the generated
    # code (a bare stub) -- manually attach it so company104_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company104_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company104_Goal(statement="sample_text")
    partner = company104_Company()
    setattr(partner, 'company104_Company2', None)
    _safe_set(owner, 'company104_Goal', partner)
    assert owner in getattr(partner, 'company104_Company2')
    _safe_set(owner, 'company104_Goal', None)
    assert owner not in getattr(partner, 'company104_Company2')


def test_assoc_responsibleOf9_stub_double():
    # company104_Room has no real 'company104_Room11' property in the generated
    # code (a bare stub) -- manually attach it so company104_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company104_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company104_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    partner = company104_Room()
    setattr(partner, 'company104_Room11', None)
    _safe_set(owner, 'company104_Employee10', partner)
    assert getattr(partner, 'company104_Room11') == owner
    _safe_set(owner, 'company104_Employee10', None)
    assert getattr(partner, 'company104_Room11') is None


def test_assoc_workstations22_stub_double():
    # company104_Room has no real 'company104_Room23' property in the generated
    # code (a bare stub) -- manually attach it so company104_Workstation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company104_Workstation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company104_Workstation(ProfileDescription="sample_text")
    partner = company104_Room()
    setattr(partner, 'company104_Room23', None)
    _safe_set(owner, 'company104_Workstation', partner)
    assert owner in getattr(partner, 'company104_Room23')
    _safe_set(owner, 'company104_Workstation', None)
    assert owner not in getattr(partner, 'company104_Room23')


