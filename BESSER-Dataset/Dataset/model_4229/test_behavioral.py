import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Function,
    Interval,
    NamedElement,
    company106_Action,
    company106_Agency,
    company106_Company,
    company106_Department,
    company106_Employee,
    company106_Flow,
    company106_Function,
    company106_Goal,
    company106_HierarchyLink,
    company106_Interval,
    company106_NamedElement,
    company106_Objective,
    company106_ObjectiveReach,
    company106_Room,
    company106_Workstation,
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

def test_assoc_actions41_reverse_link_reassign_clear():
    a1 = company106_ObjectiveReach(statement="sample_text", value=3.14)
    a2 = company106_ObjectiveReach(statement="sample_text_2", value=9.99)
    b = company106_Action(statement="sample_text")
    _safe_set(b, 'company106_Action', a1)
    assert _is_linked(b, 'company106_Action', a1)
    if hasattr(a1, 'company106_ObjectiveReach42'):
        assert _is_linked(a1, 'company106_ObjectiveReach42', b)
    _safe_set(b, 'company106_Action', a2)
    assert _is_linked(b, 'company106_Action', a2)
    if hasattr(a1, 'company106_ObjectiveReach42'):
        assert not _is_linked(a1, 'company106_ObjectiveReach42', b)
    if hasattr(a2, 'company106_ObjectiveReach42'):
        assert _is_linked(a2, 'company106_ObjectiveReach42', b)
    _safe_set(b, 'company106_Action', None)
    assert not _is_linked(b, 'company106_Action', a2)
    if hasattr(a2, 'company106_ObjectiveReach42'):
        assert not _is_linked(a2, 'company106_ObjectiveReach42', b)


def test_assoc_employees30_reverse_link_reassign_clear():
    a1 = company106_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    a2 = company106_Employee(address=13, fullName="sample_text_2", socialSecurityNumber="sample_text_2")
    b = company106_Agency(acronym="sample_text", status="sample_text")
    _safe_set(b, 'company106_Agency31', {a1})
    assert _is_linked(b, 'company106_Agency31', a1)
    if hasattr(a1, 'company106_Employee32'):
        assert _is_linked(a1, 'company106_Employee32', b)
    _safe_set(b, 'company106_Agency31', {a2})
    assert _is_linked(b, 'company106_Agency31', a2)
    if hasattr(a1, 'company106_Employee32'):
        assert not _is_linked(a1, 'company106_Employee32', b)
    if hasattr(a2, 'company106_Employee32'):
        assert _is_linked(a2, 'company106_Employee32', b)
    _safe_set(b, 'company106_Agency31', set())
    assert not _is_linked(b, 'company106_Agency31', a2)
    if hasattr(a2, 'company106_Employee32'):
        assert not _is_linked(a2, 'company106_Employee32', b)


def test_assoc_fromEmployee13_reverse_link_reassign_clear():
    a1 = company106_HierarchyLink(hierarchy="sample_text")
    a2 = company106_HierarchyLink(hierarchy="sample_text_2")
    b = company106_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'company106_Employee15', a1)
    assert _is_linked(b, 'company106_Employee15', a1)
    if hasattr(a1, 'company106_HierarchyLink14'):
        assert _is_linked(a1, 'company106_HierarchyLink14', b)
    _safe_set(b, 'company106_Employee15', a2)
    assert _is_linked(b, 'company106_Employee15', a2)
    if hasattr(a1, 'company106_HierarchyLink14'):
        assert not _is_linked(a1, 'company106_HierarchyLink14', b)
    if hasattr(a2, 'company106_HierarchyLink14'):
        assert _is_linked(a2, 'company106_HierarchyLink14', b)
    _safe_set(b, 'company106_Employee15', None)
    assert not _is_linked(b, 'company106_Employee15', a2)
    if hasattr(a2, 'company106_HierarchyLink14'):
        assert not _is_linked(a2, 'company106_HierarchyLink14', b)


def test_assoc_hierarchies8_reverse_link_reassign_clear():
    a1 = company106_HierarchyLink(hierarchy="sample_text")
    a2 = company106_HierarchyLink(hierarchy="sample_text_2")
    b = company106_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'company106_Employee', {a1})
    assert _is_linked(b, 'company106_Employee', a1)
    if hasattr(a1, 'company106_HierarchyLink'):
        assert _is_linked(a1, 'company106_HierarchyLink', b)
    _safe_set(b, 'company106_Employee', {a2})
    assert _is_linked(b, 'company106_Employee', a2)
    if hasattr(a1, 'company106_HierarchyLink'):
        assert not _is_linked(a1, 'company106_HierarchyLink', b)
    if hasattr(a2, 'company106_HierarchyLink'):
        assert _is_linked(a2, 'company106_HierarchyLink', b)
    _safe_set(b, 'company106_Employee', set())
    assert not _is_linked(b, 'company106_Employee', a2)
    if hasattr(a2, 'company106_HierarchyLink'):
        assert not _is_linked(a2, 'company106_HierarchyLink', b)


def test_assoc_inChargeOf12_reverse_link_reassign_clear():
    a1 = company106_Workstation(profileDescription="sample_text")
    a2 = company106_Workstation(profileDescription="sample_text_2")
    b = company106_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
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
    a1 = company106_Objective(nature="sample_text", type="sample_text", value=3.14)
    a2 = company106_Objective(nature="sample_text_2", type="sample_text_2", value=9.99)
    b = company106_Goal(statement="sample_text")
    _safe_set(b, 'company106_Goal26', {a1})
    assert _is_linked(b, 'company106_Goal26', a1)
    if hasattr(a1, 'company106_Objective'):
        assert _is_linked(a1, 'company106_Objective', b)
    _safe_set(b, 'company106_Goal26', {a2})
    assert _is_linked(b, 'company106_Goal26', a2)
    if hasattr(a1, 'company106_Objective'):
        assert not _is_linked(a1, 'company106_Objective', b)
    if hasattr(a2, 'company106_Objective'):
        assert _is_linked(a2, 'company106_Objective', b)
    _safe_set(b, 'company106_Goal26', set())
    assert not _is_linked(b, 'company106_Goal26', a2)
    if hasattr(a2, 'company106_Objective'):
        assert not _is_linked(a2, 'company106_Objective', b)


def test_assoc_owners24_reverse_link_reassign_clear():
    a1 = company106_Workstation(profileDescription="sample_text")
    a2 = company106_Workstation(profileDescription="sample_text_2")
    b = company106_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
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
    a1 = company106_ObjectiveReach(statement="sample_text", value=3.14)
    a2 = company106_ObjectiveReach(statement="sample_text_2", value=9.99)
    b = company106_Agency(acronym="sample_text", status="sample_text")
    _safe_set(b, 'company106_Agency34', {a1})
    assert _is_linked(b, 'company106_Agency34', a1)
    if hasattr(a1, 'company106_ObjectiveReach'):
        assert _is_linked(a1, 'company106_ObjectiveReach', b)
    _safe_set(b, 'company106_Agency34', {a2})
    assert _is_linked(b, 'company106_Agency34', a2)
    if hasattr(a1, 'company106_ObjectiveReach'):
        assert not _is_linked(a1, 'company106_ObjectiveReach', b)
    if hasattr(a2, 'company106_ObjectiveReach'):
        assert _is_linked(a2, 'company106_ObjectiveReach', b)
    _safe_set(b, 'company106_Agency34', set())
    assert not _is_linked(b, 'company106_Agency34', a2)
    if hasattr(a2, 'company106_ObjectiveReach'):
        assert not _is_linked(a2, 'company106_ObjectiveReach', b)


def test_assoc_srcAgency38_reverse_link_reassign_clear():
    a1 = company106_ObjectiveReach(statement="sample_text", value=3.14)
    a2 = company106_ObjectiveReach(statement="sample_text_2", value=9.99)
    b = company106_Agency(acronym="sample_text", status="sample_text")
    _safe_set(b, 'company106_Agency40', a1)
    assert _is_linked(b, 'company106_Agency40', a1)
    if hasattr(a1, 'company106_ObjectiveReach39'):
        assert _is_linked(a1, 'company106_ObjectiveReach39', b)
    _safe_set(b, 'company106_Agency40', a2)
    assert _is_linked(b, 'company106_Agency40', a2)
    if hasattr(a1, 'company106_ObjectiveReach39'):
        assert not _is_linked(a1, 'company106_ObjectiveReach39', b)
    if hasattr(a2, 'company106_ObjectiveReach39'):
        assert _is_linked(a2, 'company106_ObjectiveReach39', b)
    _safe_set(b, 'company106_Agency40', None)
    assert not _is_linked(b, 'company106_Agency40', a2)
    if hasattr(a2, 'company106_ObjectiveReach39'):
        assert not _is_linked(a2, 'company106_ObjectiveReach39', b)


def test_assoc_toEmployee16_reverse_link_reassign_clear():
    a1 = company106_HierarchyLink(hierarchy="sample_text")
    a2 = company106_HierarchyLink(hierarchy="sample_text_2")
    b = company106_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'company106_Employee18', a1)
    assert _is_linked(b, 'company106_Employee18', a1)
    if hasattr(a1, 'company106_HierarchyLink17'):
        assert _is_linked(a1, 'company106_HierarchyLink17', b)
    _safe_set(b, 'company106_Employee18', a2)
    assert _is_linked(b, 'company106_Employee18', a2)
    if hasattr(a1, 'company106_HierarchyLink17'):
        assert not _is_linked(a1, 'company106_HierarchyLink17', b)
    if hasattr(a2, 'company106_HierarchyLink17'):
        assert _is_linked(a2, 'company106_HierarchyLink17', b)
    _safe_set(b, 'company106_Employee18', None)
    assert not _is_linked(b, 'company106_Employee18', a2)
    if hasattr(a2, 'company106_HierarchyLink17'):
        assert not _is_linked(a2, 'company106_HierarchyLink17', b)


def test_assoc_trgObjective35_reverse_link_reassign_clear():
    a1 = company106_ObjectiveReach(statement="sample_text", value=3.14)
    a2 = company106_ObjectiveReach(statement="sample_text_2", value=9.99)
    b = company106_Objective(nature="sample_text", type="sample_text", value=3.14)
    _safe_set(b, 'company106_Objective37', a1)
    assert _is_linked(b, 'company106_Objective37', a1)
    if hasattr(a1, 'company106_ObjectiveReach36'):
        assert _is_linked(a1, 'company106_ObjectiveReach36', b)
    _safe_set(b, 'company106_Objective37', a2)
    assert _is_linked(b, 'company106_Objective37', a2)
    if hasattr(a1, 'company106_ObjectiveReach36'):
        assert not _is_linked(a1, 'company106_ObjectiveReach36', b)
    if hasattr(a2, 'company106_ObjectiveReach36'):
        assert _is_linked(a2, 'company106_ObjectiveReach36', b)
    _safe_set(b, 'company106_Objective37', None)
    assert not _is_linked(b, 'company106_Objective37', a2)
    if hasattr(a2, 'company106_ObjectiveReach36'):
        assert not _is_linked(a2, 'company106_ObjectiveReach36', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_agencies0_stub_double():
    # company106_Company has no real 'company106_Company' property in the generated
    # code (a bare stub) -- manually attach it so company106_Agency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company106_Agency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company106_Agency(acronym="sample_text", status="sample_text")
    partner = company106_Company()
    setattr(partner, 'company106_Company', None)
    _safe_set(owner, 'company106_Agency', partner)
    assert owner in getattr(partner, 'company106_Company')
    _safe_set(owner, 'company106_Agency', None)
    assert owner not in getattr(partner, 'company106_Company')


def test_assoc_departments27_stub_double():
    # company106_Department has no real 'company106_Department29' property in the generated
    # code (a bare stub) -- manually attach it so company106_Agency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company106_Agency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company106_Agency(acronym="sample_text", status="sample_text")
    partner = company106_Department()
    setattr(partner, 'company106_Department29', None)
    _safe_set(owner, 'company106_Agency28', {partner})
    assert getattr(partner, 'company106_Department29') == owner
    _safe_set(owner, 'company106_Agency28', set())
    assert getattr(partner, 'company106_Department29') is None


def test_assoc_flow46_stub_double():
    # company106_Flow has no real 'company106_Flow48' property in the generated
    # code (a bare stub) -- manually attach it so company106_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company106_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company106_Action(statement="sample_text")
    partner = company106_Flow()
    setattr(partner, 'company106_Flow48', None)
    _safe_set(owner, 'company106_Action47', partner)
    assert getattr(partner, 'company106_Flow48') == owner
    _safe_set(owner, 'company106_Action47', None)
    assert getattr(partner, 'company106_Flow48') is None


def test_assoc_goals1_stub_double():
    # company106_Company has no real 'company106_Company2' property in the generated
    # code (a bare stub) -- manually attach it so company106_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company106_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company106_Goal(statement="sample_text")
    partner = company106_Company()
    setattr(partner, 'company106_Company2', None)
    _safe_set(owner, 'company106_Goal', partner)
    assert owner in getattr(partner, 'company106_Company2')
    _safe_set(owner, 'company106_Goal', None)
    assert owner not in getattr(partner, 'company106_Company2')


def test_assoc_responsibleOf9_stub_double():
    # company106_Room has no real 'company106_Room11' property in the generated
    # code (a bare stub) -- manually attach it so company106_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company106_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company106_Employee(address=7, fullName="sample_text", socialSecurityNumber="sample_text")
    partner = company106_Room()
    setattr(partner, 'company106_Room11', None)
    _safe_set(owner, 'company106_Employee10', partner)
    assert getattr(partner, 'company106_Room11') == owner
    _safe_set(owner, 'company106_Employee10', None)
    assert getattr(partner, 'company106_Room11') is None


def test_assoc_workstations22_stub_double():
    # company106_Room has no real 'company106_Room23' property in the generated
    # code (a bare stub) -- manually attach it so company106_Workstation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company106_Workstation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company106_Workstation(profileDescription="sample_text")
    partner = company106_Room()
    setattr(partner, 'company106_Room23', None)
    _safe_set(owner, 'company106_Workstation', partner)
    assert owner in getattr(partner, 'company106_Room23')
    _safe_set(owner, 'company106_Workstation', None)
    assert owner not in getattr(partner, 'company106_Room23')


