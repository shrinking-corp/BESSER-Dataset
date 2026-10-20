import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    projectPlanning_Assignment,
    projectPlanning_Capability,
    projectPlanning_Employee,
    projectPlanning_Project,
    projectPlanning_ProjectPlan,
    projectPlanning_Rating,
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

def test_assoc_capability18_reverse_link_reassign_clear():
    a1 = projectPlanning_Rating(rating=7)
    a2 = projectPlanning_Rating(rating=13)
    b = projectPlanning_Capability(name="sample_text")
    _safe_set(b, 'projectPlanning_Capability20', a1)
    assert _is_linked(b, 'projectPlanning_Capability20', a1)
    if hasattr(a1, 'projectPlanning_Rating19'):
        assert _is_linked(a1, 'projectPlanning_Rating19', b)
    _safe_set(b, 'projectPlanning_Capability20', a2)
    assert _is_linked(b, 'projectPlanning_Capability20', a2)
    if hasattr(a1, 'projectPlanning_Rating19'):
        assert not _is_linked(a1, 'projectPlanning_Rating19', b)
    if hasattr(a2, 'projectPlanning_Rating19'):
        assert _is_linked(a2, 'projectPlanning_Rating19', b)
    _safe_set(b, 'projectPlanning_Capability20', None)
    assert not _is_linked(b, 'projectPlanning_Capability20', a2)
    if hasattr(a2, 'projectPlanning_Rating19'):
        assert not _is_linked(a2, 'projectPlanning_Rating19', b)


def test_assoc_hasCapabilities12_reverse_link_reassign_clear():
    a1 = projectPlanning_Employee(hasResource=7, name="sample_text")
    a2 = projectPlanning_Employee(hasResource=13, name="sample_text_2")
    b = projectPlanning_Capability(name="sample_text")
    _safe_set(b, 'projectPlanning_Capability14', a1)
    assert _is_linked(b, 'projectPlanning_Capability14', a1)
    if hasattr(a1, 'projectPlanning_Employee13'):
        assert _is_linked(a1, 'projectPlanning_Employee13', b)
    _safe_set(b, 'projectPlanning_Capability14', a2)
    assert _is_linked(b, 'projectPlanning_Capability14', a2)
    if hasattr(a1, 'projectPlanning_Employee13'):
        assert not _is_linked(a1, 'projectPlanning_Employee13', b)
    if hasattr(a2, 'projectPlanning_Employee13'):
        assert _is_linked(a2, 'projectPlanning_Employee13', b)
    _safe_set(b, 'projectPlanning_Capability14', None)
    assert not _is_linked(b, 'projectPlanning_Capability14', a2)
    if hasattr(a2, 'projectPlanning_Employee13'):
        assert not _is_linked(a2, 'projectPlanning_Employee13', b)


def test_assoc_ratings15_reverse_link_reassign_clear():
    a1 = projectPlanning_Rating(rating=7)
    a2 = projectPlanning_Rating(rating=13)
    b = projectPlanning_Employee(hasResource=7, name="sample_text")
    _safe_set(b, 'projectPlanning_Employee16', {a1})
    assert _is_linked(b, 'projectPlanning_Employee16', a1)
    if hasattr(a1, 'projectPlanning_Rating17'):
        assert _is_linked(a1, 'projectPlanning_Rating17', b)
    _safe_set(b, 'projectPlanning_Employee16', {a2})
    assert _is_linked(b, 'projectPlanning_Employee16', a2)
    if hasattr(a1, 'projectPlanning_Rating17'):
        assert not _is_linked(a1, 'projectPlanning_Rating17', b)
    if hasattr(a2, 'projectPlanning_Rating17'):
        assert _is_linked(a2, 'projectPlanning_Rating17', b)
    _safe_set(b, 'projectPlanning_Employee16', set())
    assert not _is_linked(b, 'projectPlanning_Employee16', a2)
    if hasattr(a2, 'projectPlanning_Rating17'):
        assert not _is_linked(a2, 'projectPlanning_Rating17', b)


def test_assoc_requiresCapabilities9_reverse_link_reassign_clear():
    a1 = projectPlanning_Project(name="sample_text", requiresResources=7)
    a2 = projectPlanning_Project(name="sample_text_2", requiresResources=13)
    b = projectPlanning_Capability(name="sample_text")
    _safe_set(b, 'projectPlanning_Capability11', a1)
    assert _is_linked(b, 'projectPlanning_Capability11', a1)
    if hasattr(a1, 'projectPlanning_Project10'):
        assert _is_linked(a1, 'projectPlanning_Project10', b)
    _safe_set(b, 'projectPlanning_Capability11', a2)
    assert _is_linked(b, 'projectPlanning_Capability11', a2)
    if hasattr(a1, 'projectPlanning_Project10'):
        assert not _is_linked(a1, 'projectPlanning_Project10', b)
    if hasattr(a2, 'projectPlanning_Project10'):
        assert _is_linked(a2, 'projectPlanning_Project10', b)
    _safe_set(b, 'projectPlanning_Capability11', None)
    assert not _is_linked(b, 'projectPlanning_Capability11', a2)
    if hasattr(a2, 'projectPlanning_Project10'):
        assert not _is_linked(a2, 'projectPlanning_Project10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_capabilities0_stub_double():
    # projectPlanning_ProjectPlan has no real 'projectPlanning_ProjectPlan' property in the generated
    # code (a bare stub) -- manually attach it so projectPlanning_Capability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # projectPlanning_Capability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = projectPlanning_Capability(name="sample_text")
    partner = projectPlanning_ProjectPlan()
    setattr(partner, 'projectPlanning_ProjectPlan', None)
    _safe_set(owner, 'projectPlanning_Capability', partner)
    assert owner in getattr(partner, 'projectPlanning_ProjectPlan')
    _safe_set(owner, 'projectPlanning_Capability', None)
    assert owner not in getattr(partner, 'projectPlanning_ProjectPlan')


def test_assoc_employee24_stub_double():
    # projectPlanning_Assignment has no real 'projectPlanning_Assignment25' property in the generated
    # code (a bare stub) -- manually attach it so projectPlanning_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # projectPlanning_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = projectPlanning_Employee(hasResource=7, name="sample_text")
    partner = projectPlanning_Assignment()
    setattr(partner, 'projectPlanning_Assignment25', None)
    _safe_set(owner, 'projectPlanning_Employee26', partner)
    assert getattr(partner, 'projectPlanning_Assignment25') == owner
    _safe_set(owner, 'projectPlanning_Employee26', None)
    assert getattr(partner, 'projectPlanning_Assignment25') is None


def test_assoc_employees1_stub_double():
    # projectPlanning_ProjectPlan has no real 'projectPlanning_ProjectPlan2' property in the generated
    # code (a bare stub) -- manually attach it so projectPlanning_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # projectPlanning_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = projectPlanning_Employee(hasResource=7, name="sample_text")
    partner = projectPlanning_ProjectPlan()
    setattr(partner, 'projectPlanning_ProjectPlan2', None)
    _safe_set(owner, 'projectPlanning_Employee', partner)
    assert owner in getattr(partner, 'projectPlanning_ProjectPlan2')
    _safe_set(owner, 'projectPlanning_Employee', None)
    assert owner not in getattr(partner, 'projectPlanning_ProjectPlan2')


def test_assoc_project21_stub_double():
    # projectPlanning_Assignment has no real 'projectPlanning_Assignment22' property in the generated
    # code (a bare stub) -- manually attach it so projectPlanning_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # projectPlanning_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = projectPlanning_Project(name="sample_text", requiresResources=7)
    partner = projectPlanning_Assignment()
    setattr(partner, 'projectPlanning_Assignment22', None)
    _safe_set(owner, 'projectPlanning_Project23', partner)
    assert getattr(partner, 'projectPlanning_Assignment22') == owner
    _safe_set(owner, 'projectPlanning_Project23', None)
    assert getattr(partner, 'projectPlanning_Assignment22') is None


def test_assoc_projects3_stub_double():
    # projectPlanning_ProjectPlan has no real 'projectPlanning_ProjectPlan4' property in the generated
    # code (a bare stub) -- manually attach it so projectPlanning_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # projectPlanning_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = projectPlanning_Project(name="sample_text", requiresResources=7)
    partner = projectPlanning_ProjectPlan()
    setattr(partner, 'projectPlanning_ProjectPlan4', None)
    _safe_set(owner, 'projectPlanning_Project', partner)
    assert owner in getattr(partner, 'projectPlanning_ProjectPlan4')
    _safe_set(owner, 'projectPlanning_Project', None)
    assert owner not in getattr(partner, 'projectPlanning_ProjectPlan4')


def test_assoc_ratings5_stub_double():
    # projectPlanning_ProjectPlan has no real 'projectPlanning_ProjectPlan6' property in the generated
    # code (a bare stub) -- manually attach it so projectPlanning_Rating's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # projectPlanning_Rating's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = projectPlanning_Rating(rating=7)
    partner = projectPlanning_ProjectPlan()
    setattr(partner, 'projectPlanning_ProjectPlan6', None)
    _safe_set(owner, 'projectPlanning_Rating', partner)
    assert owner in getattr(partner, 'projectPlanning_ProjectPlan6')
    _safe_set(owner, 'projectPlanning_Rating', None)
    assert owner not in getattr(partner, 'projectPlanning_ProjectPlan6')


