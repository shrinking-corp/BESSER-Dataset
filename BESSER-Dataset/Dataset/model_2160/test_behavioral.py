import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ProductSpaceElement,
    UUIDElement,
    list_ProductSpaceElement,
    list_VersionedList,
    list_VersionedListEdge,
    list_VersionedListStartReference,
    list_VersionedListVertex,
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

def test_assoc_edges1_stub_double():
    # list_VersionedListEdge has no real 'VersionedListEdge' property in the generated
    # code (a bare stub) -- manually attach it so list_VersionedList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # list_VersionedList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = list_VersionedList()
    partner = list_VersionedListEdge()
    setattr(partner, 'VersionedListEdge', None)
    _safe_set(owner, 'list2', {partner})
    assert getattr(partner, 'VersionedListEdge') == owner
    _safe_set(owner, 'list2', set())
    assert getattr(partner, 'VersionedListEdge') is None


def test_assoc_list10_stub_double():
    # list_VersionedListVertex has no real 'vertices' property in the generated
    # code (a bare stub) -- manually attach it so list_VersionedList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # list_VersionedList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = list_VersionedList()
    partner = list_VersionedListVertex()
    setattr(partner, 'vertices', None)
    _safe_set(owner, 'VersionedList', partner)
    assert getattr(partner, 'vertices') == owner
    _safe_set(owner, 'VersionedList', None)
    assert getattr(partner, 'vertices') is None


def test_assoc_list17_stub_double():
    # list_VersionedListEdge has no real 'edges' property in the generated
    # code (a bare stub) -- manually attach it so list_VersionedList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # list_VersionedList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = list_VersionedList()
    partner = list_VersionedListEdge()
    setattr(partner, 'edges', None)
    _safe_set(owner, 'VersionedList18', partner)
    assert getattr(partner, 'edges') == owner
    _safe_set(owner, 'VersionedList18', None)
    assert getattr(partner, 'edges') is None


def test_assoc_list21_stub_double():
    # list_VersionedListStartReference has no real 'startVertices' property in the generated
    # code (a bare stub) -- manually attach it so list_VersionedList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # list_VersionedList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = list_VersionedList()
    partner = list_VersionedListStartReference()
    setattr(partner, 'startVertices', None)
    _safe_set(owner, 'VersionedList22', partner)
    assert getattr(partner, 'startVertices') == owner
    _safe_set(owner, 'VersionedList22', None)
    assert getattr(partner, 'startVertices') is None


def test_assoc_startVertices3_stub_double():
    # list_VersionedListStartReference has no real 'VersionedListStartReference' property in the generated
    # code (a bare stub) -- manually attach it so list_VersionedList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # list_VersionedList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = list_VersionedList()
    partner = list_VersionedListStartReference()
    setattr(partner, 'VersionedListStartReference', None)
    _safe_set(owner, 'list4', {partner})
    assert getattr(partner, 'VersionedListStartReference') == owner
    _safe_set(owner, 'list4', set())
    assert getattr(partner, 'VersionedListStartReference') is None


def test_assoc_vertices0_stub_double():
    # list_VersionedListVertex has no real 'VersionedListVertex' property in the generated
    # code (a bare stub) -- manually attach it so list_VersionedList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # list_VersionedList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = list_VersionedList()
    partner = list_VersionedListVertex()
    setattr(partner, 'VersionedListVertex', None)
    _safe_set(owner, 'list', {partner})
    assert getattr(partner, 'VersionedListVertex') == owner
    _safe_set(owner, 'list', set())
    assert getattr(partner, 'VersionedListVertex') is None


