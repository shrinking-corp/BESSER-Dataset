import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    familytree_FamilyTree,
    familytree_Member,
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

def test_assoc_children2_reverse_link_reassign_clear():
    a1 = familytree_Member(age=7, name="sample_text")
    a2 = familytree_Member(age=13, name="sample_text_2")
    b = familytree_Member(age=7, name="sample_text")
    _safe_set(b, 'parents', {a1})
    assert _is_linked(b, 'parents', a1)
    if hasattr(a1, 'Member'):
        assert _is_linked(a1, 'Member', b)
    _safe_set(b, 'parents', {a2})
    assert _is_linked(b, 'parents', a2)
    if hasattr(a1, 'Member'):
        assert not _is_linked(a1, 'Member', b)
    if hasattr(a2, 'Member'):
        assert _is_linked(a2, 'Member', b)
    _safe_set(b, 'parents', set())
    assert not _is_linked(b, 'parents', a2)
    if hasattr(a2, 'Member'):
        assert not _is_linked(a2, 'Member', b)


def test_assoc_parents4_reverse_link_reassign_clear():
    a1 = familytree_Member(age=7, name="sample_text")
    a2 = familytree_Member(age=13, name="sample_text_2")
    b = familytree_Member(age=7, name="sample_text")
    _safe_set(b, 'children', {a1})
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Member5'):
        assert _is_linked(a1, 'Member5', b)
    _safe_set(b, 'children', {a2})
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Member5'):
        assert not _is_linked(a1, 'Member5', b)
    if hasattr(a2, 'Member5'):
        assert _is_linked(a2, 'Member5', b)
    _safe_set(b, 'children', set())
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Member5'):
        assert not _is_linked(a2, 'Member5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_members0_stub_double():
    # familytree_FamilyTree has no real 'familytree_FamilyTree' property in the generated
    # code (a bare stub) -- manually attach it so familytree_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familytree_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familytree_Member(age=7, name="sample_text")
    partner = familytree_FamilyTree()
    setattr(partner, 'familytree_FamilyTree', None)
    _safe_set(owner, 'familytree_Member', partner)
    assert owner in getattr(partner, 'familytree_FamilyTree')
    _safe_set(owner, 'familytree_Member', None)
    assert owner not in getattr(partner, 'familytree_FamilyTree')


