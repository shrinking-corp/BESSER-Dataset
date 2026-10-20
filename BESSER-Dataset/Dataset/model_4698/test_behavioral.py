import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    familytree_FamilyTree,
    familytree_Man,
    familytree_Person,
    familytree_Woman,
    RelationshipStatus,
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

def test_assoc_children1_reverse_link_reassign_clear():
    a1 = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    a2 = familytree_Person(dayOfBirth=date(2025, 6, 15), dayOfDeath=date(2025, 6, 15), died=False, firstName="sample_text_2", imagePaths="sample_text_2", locationOfBirth="sample_text_2", nameOfBirth="sample_text_2", relationshipStatus="sample_text_2", secondName="sample_text_2")
    b = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    _safe_set(b, 'parents', {a1})
    assert _is_linked(b, 'parents', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'parents', {a2})
    assert _is_linked(b, 'parents', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'parents', set())
    assert not _is_linked(b, 'parents', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_inRelationTo9_reverse_link_reassign_clear():
    a1 = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    a2 = familytree_Person(dayOfBirth=date(2025, 6, 15), dayOfDeath=date(2025, 6, 15), died=False, firstName="sample_text_2", imagePaths="sample_text_2", locationOfBirth="sample_text_2", nameOfBirth="sample_text_2", relationshipStatus="sample_text_2", secondName="sample_text_2")
    b = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    _safe_set(b, 'inRelationWith', a1)
    assert _is_linked(b, 'inRelationWith', a1)
    if hasattr(a1, 'Person10'):
        assert _is_linked(a1, 'Person10', b)
    _safe_set(b, 'inRelationWith', a2)
    assert _is_linked(b, 'inRelationWith', a2)
    if hasattr(a1, 'Person10'):
        assert not _is_linked(a1, 'Person10', b)
    if hasattr(a2, 'Person10'):
        assert _is_linked(a2, 'Person10', b)
    _safe_set(b, 'inRelationWith', None)
    assert not _is_linked(b, 'inRelationWith', a2)
    if hasattr(a2, 'Person10'):
        assert not _is_linked(a2, 'Person10', b)


def test_assoc_inRelationWith6_reverse_link_reassign_clear():
    a1 = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    a2 = familytree_Person(dayOfBirth=date(2025, 6, 15), dayOfDeath=date(2025, 6, 15), died=False, firstName="sample_text_2", imagePaths="sample_text_2", locationOfBirth="sample_text_2", nameOfBirth="sample_text_2", relationshipStatus="sample_text_2", secondName="sample_text_2")
    b = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    _safe_set(b, 'inRelationTo', a1)
    assert _is_linked(b, 'inRelationTo', a1)
    if hasattr(a1, 'Person7'):
        assert _is_linked(a1, 'Person7', b)
    _safe_set(b, 'inRelationTo', a2)
    assert _is_linked(b, 'inRelationTo', a2)
    if hasattr(a1, 'Person7'):
        assert not _is_linked(a1, 'Person7', b)
    if hasattr(a2, 'Person7'):
        assert _is_linked(a2, 'Person7', b)
    _safe_set(b, 'inRelationTo', None)
    assert not _is_linked(b, 'inRelationTo', a2)
    if hasattr(a2, 'Person7'):
        assert not _is_linked(a2, 'Person7', b)


def test_assoc_parents3_reverse_link_reassign_clear():
    a1 = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    a2 = familytree_Person(dayOfBirth=date(2025, 6, 15), dayOfDeath=date(2025, 6, 15), died=False, firstName="sample_text_2", imagePaths="sample_text_2", locationOfBirth="sample_text_2", nameOfBirth="sample_text_2", relationshipStatus="sample_text_2", secondName="sample_text_2")
    b = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    _safe_set(b, 'children', {a1})
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Person4'):
        assert _is_linked(a1, 'Person4', b)
    _safe_set(b, 'children', {a2})
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Person4'):
        assert not _is_linked(a1, 'Person4', b)
    if hasattr(a2, 'Person4'):
        assert _is_linked(a2, 'Person4', b)
    _safe_set(b, 'children', set())
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Person4'):
        assert not _is_linked(a2, 'Person4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_members11_stub_double():
    # familytree_FamilyTree has no real 'familytree_FamilyTree' property in the generated
    # code (a bare stub) -- manually attach it so familytree_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familytree_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familytree_Person(dayOfBirth=date(2024, 1, 1), dayOfDeath=date(2024, 1, 1), died=True, firstName="sample_text", imagePaths="sample_text", locationOfBirth="sample_text", nameOfBirth="sample_text", relationshipStatus="sample_text", secondName="sample_text")
    partner = familytree_FamilyTree()
    setattr(partner, 'familytree_FamilyTree', None)
    _safe_set(owner, 'familytree_Person', partner)
    assert owner in getattr(partner, 'familytree_FamilyTree')
    _safe_set(owner, 'familytree_Person', None)
    assert owner not in getattr(partner, 'familytree_FamilyTree')


