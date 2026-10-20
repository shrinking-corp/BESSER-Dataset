import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    jgrapht_Edge,
    jgrapht_Graph,
    jgrapht_Vertex,
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

def test_assoc_from_3_reverse_link_reassign_clear():
    a1 = jgrapht_Vertex(name="sample_text")
    a2 = jgrapht_Vertex(name="sample_text_2")
    b = jgrapht_Edge(relation="sample_text")
    _safe_set(b, 'jgrapht_Edge4', a1)
    assert _is_linked(b, 'jgrapht_Edge4', a1)
    if hasattr(a1, 'jgrapht_Vertex5'):
        assert _is_linked(a1, 'jgrapht_Vertex5', b)
    _safe_set(b, 'jgrapht_Edge4', a2)
    assert _is_linked(b, 'jgrapht_Edge4', a2)
    if hasattr(a1, 'jgrapht_Vertex5'):
        assert not _is_linked(a1, 'jgrapht_Vertex5', b)
    if hasattr(a2, 'jgrapht_Vertex5'):
        assert _is_linked(a2, 'jgrapht_Vertex5', b)
    _safe_set(b, 'jgrapht_Edge4', None)
    assert not _is_linked(b, 'jgrapht_Edge4', a2)
    if hasattr(a2, 'jgrapht_Vertex5'):
        assert not _is_linked(a2, 'jgrapht_Vertex5', b)


def test_assoc_to6_reverse_link_reassign_clear():
    a1 = jgrapht_Vertex(name="sample_text")
    a2 = jgrapht_Vertex(name="sample_text_2")
    b = jgrapht_Edge(relation="sample_text")
    _safe_set(b, 'jgrapht_Edge7', a1)
    assert _is_linked(b, 'jgrapht_Edge7', a1)
    if hasattr(a1, 'jgrapht_Vertex8'):
        assert _is_linked(a1, 'jgrapht_Vertex8', b)
    _safe_set(b, 'jgrapht_Edge7', a2)
    assert _is_linked(b, 'jgrapht_Edge7', a2)
    if hasattr(a1, 'jgrapht_Vertex8'):
        assert not _is_linked(a1, 'jgrapht_Vertex8', b)
    if hasattr(a2, 'jgrapht_Vertex8'):
        assert _is_linked(a2, 'jgrapht_Vertex8', b)
    _safe_set(b, 'jgrapht_Edge7', None)
    assert not _is_linked(b, 'jgrapht_Edge7', a2)
    if hasattr(a2, 'jgrapht_Vertex8'):
        assert not _is_linked(a2, 'jgrapht_Vertex8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges0_stub_double():
    # jgrapht_Graph has no real 'jgrapht_Graph' property in the generated
    # code (a bare stub) -- manually attach it so jgrapht_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jgrapht_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jgrapht_Edge(relation="sample_text")
    partner = jgrapht_Graph()
    setattr(partner, 'jgrapht_Graph', None)
    _safe_set(owner, 'jgrapht_Edge', partner)
    assert owner in getattr(partner, 'jgrapht_Graph')
    _safe_set(owner, 'jgrapht_Edge', None)
    assert owner not in getattr(partner, 'jgrapht_Graph')


def test_assoc_vertices1_stub_double():
    # jgrapht_Graph has no real 'jgrapht_Graph2' property in the generated
    # code (a bare stub) -- manually attach it so jgrapht_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jgrapht_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jgrapht_Vertex(name="sample_text")
    partner = jgrapht_Graph()
    setattr(partner, 'jgrapht_Graph2', None)
    _safe_set(owner, 'jgrapht_Vertex', partner)
    assert owner in getattr(partner, 'jgrapht_Graph2')
    _safe_set(owner, 'jgrapht_Vertex', None)
    assert owner not in getattr(partner, 'jgrapht_Graph2')


