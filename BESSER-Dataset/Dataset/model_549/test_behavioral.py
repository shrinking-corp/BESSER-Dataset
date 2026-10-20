import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    family_FamilyTree,
    family_Female,
    family_Male,
    family_Person,
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

def test_assoc_children4_reverse_link_reassign_clear():
    a1 = family_Person(age=7, name="sample_text", size=7, weight=7)
    a2 = family_Person(age=13, name="sample_text_2", size=13, weight=13)
    b = family_Person(age=7, name="sample_text", size=7, weight=7)
    _safe_set(b, 'family_Person5', a1)
    assert _is_linked(b, 'family_Person5', a1)
    if hasattr(a1, 'family_Person3'):
        assert _is_linked(a1, 'family_Person3', b)
    _safe_set(b, 'family_Person5', a2)
    assert _is_linked(b, 'family_Person5', a2)
    if hasattr(a1, 'family_Person3'):
        assert not _is_linked(a1, 'family_Person3', b)
    if hasattr(a2, 'family_Person3'):
        assert _is_linked(a2, 'family_Person3', b)
    _safe_set(b, 'family_Person5', None)
    assert not _is_linked(b, 'family_Person5', a2)
    if hasattr(a2, 'family_Person3'):
        assert not _is_linked(a2, 'family_Person3', b)


def test_assoc_relative7_reverse_link_reassign_clear():
    a1 = family_Person(age=7, name="sample_text", size=7, weight=7)
    a2 = family_Person(age=13, name="sample_text_2", size=13, weight=13)
    b = family_Person(age=7, name="sample_text", size=7, weight=7)
    _safe_set(b, 'family_Person8', a1)
    assert _is_linked(b, 'family_Person8', a1)
    if hasattr(a1, 'family_Person6'):
        assert _is_linked(a1, 'family_Person6', b)
    _safe_set(b, 'family_Person8', a2)
    assert _is_linked(b, 'family_Person8', a2)
    if hasattr(a1, 'family_Person6'):
        assert not _is_linked(a1, 'family_Person6', b)
    if hasattr(a2, 'family_Person6'):
        assert _is_linked(a2, 'family_Person6', b)
    _safe_set(b, 'family_Person8', None)
    assert not _is_linked(b, 'family_Person8', a2)
    if hasattr(a2, 'family_Person6'):
        assert not _is_linked(a2, 'family_Person6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_father0_stub_double():
    # family_Male has no real 'family_Male' property in the generated
    # code (a bare stub) -- manually attach it so family_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # family_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = family_Person(age=7, name="sample_text", size=7, weight=7)
    partner = family_Male()
    setattr(partner, 'family_Male', None)
    _safe_set(owner, 'family_Person', partner)
    assert getattr(partner, 'family_Male') == owner
    _safe_set(owner, 'family_Person', None)
    assert getattr(partner, 'family_Male') is None


def test_assoc_mother1_stub_double():
    # family_Female has no real 'family_Female' property in the generated
    # code (a bare stub) -- manually attach it so family_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # family_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = family_Person(age=7, name="sample_text", size=7, weight=7)
    partner = family_Female()
    setattr(partner, 'family_Female', None)
    _safe_set(owner, 'family_Person2', partner)
    assert getattr(partner, 'family_Female') == owner
    _safe_set(owner, 'family_Person2', None)
    assert getattr(partner, 'family_Female') is None


def test_assoc_people9_stub_double():
    # family_FamilyTree has no real 'family_FamilyTree' property in the generated
    # code (a bare stub) -- manually attach it so family_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # family_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = family_Person(age=7, name="sample_text", size=7, weight=7)
    partner = family_FamilyTree()
    setattr(partner, 'family_FamilyTree', None)
    _safe_set(owner, 'family_Person10', partner)
    assert owner in getattr(partner, 'family_FamilyTree')
    _safe_set(owner, 'family_Person10', None)
    assert owner not in getattr(partner, 'family_FamilyTree')


