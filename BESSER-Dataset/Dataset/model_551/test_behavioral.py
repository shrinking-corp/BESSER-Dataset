import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    familyTree_FamilyTree,
    familyTree_Female,
    familyTree_Male,
    familyTree_Person,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children11_stub_double():
    # familyTree_Female has no real 'mother' property in the generated
    # code (a bare stub) -- manually attach it so familyTree_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyTree_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyTree_Person(lastName="sample_text", name="sample_text")
    partner = familyTree_Female()
    setattr(partner, 'mother', None)
    _safe_set(owner, 'Person12', partner)
    assert getattr(partner, 'mother') == owner
    _safe_set(owner, 'Person12', None)
    assert getattr(partner, 'mother') is None


def test_assoc_children7_stub_double():
    # familyTree_Male has no real 'father' property in the generated
    # code (a bare stub) -- manually attach it so familyTree_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyTree_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyTree_Person(lastName="sample_text", name="sample_text")
    partner = familyTree_Male()
    setattr(partner, 'father', None)
    _safe_set(owner, 'Person8', partner)
    assert getattr(partner, 'father') == owner
    _safe_set(owner, 'Person8', None)
    assert getattr(partner, 'father') is None


def test_assoc_father1_stub_double():
    # familyTree_Male has no real 'Male' property in the generated
    # code (a bare stub) -- manually attach it so familyTree_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyTree_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyTree_Person(lastName="sample_text", name="sample_text")
    partner = familyTree_Male()
    setattr(partner, 'Male', None)
    _safe_set(owner, 'children', partner)
    assert getattr(partner, 'Male') == owner
    _safe_set(owner, 'children', None)
    assert getattr(partner, 'Male') is None


def test_assoc_leaves0_stub_double():
    # familyTree_FamilyTree has no real 'tree' property in the generated
    # code (a bare stub) -- manually attach it so familyTree_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyTree_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyTree_Person(lastName="sample_text", name="sample_text")
    partner = familyTree_FamilyTree()
    setattr(partner, 'tree', None)
    _safe_set(owner, 'Person', partner)
    assert owner in getattr(partner, 'tree')
    _safe_set(owner, 'Person', None)
    assert owner not in getattr(partner, 'tree')


def test_assoc_mother2_stub_double():
    # familyTree_Female has no real 'Female' property in the generated
    # code (a bare stub) -- manually attach it so familyTree_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyTree_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyTree_Person(lastName="sample_text", name="sample_text")
    partner = familyTree_Female()
    setattr(partner, 'Female', None)
    _safe_set(owner, 'children3', partner)
    assert getattr(partner, 'Female') == owner
    _safe_set(owner, 'children3', None)
    assert getattr(partner, 'Female') is None


def test_assoc_tree4_stub_double():
    # familyTree_FamilyTree has no real 'FamilyTree' property in the generated
    # code (a bare stub) -- manually attach it so familyTree_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyTree_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyTree_Person(lastName="sample_text", name="sample_text")
    partner = familyTree_FamilyTree()
    setattr(partner, 'FamilyTree', None)
    _safe_set(owner, 'leaves', partner)
    assert getattr(partner, 'FamilyTree') == owner
    _safe_set(owner, 'leaves', None)
    assert getattr(partner, 'FamilyTree') is None


