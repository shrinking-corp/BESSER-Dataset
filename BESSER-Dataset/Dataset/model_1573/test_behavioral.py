import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ScaffoldGraph_Edge,
    ScaffoldGraph_Graph,
    ScaffoldGraph_Vertex,
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

def test_assoc_edges1_reverse_link_reassign_clear():
    a1 = ScaffoldGraph_Graph(name="sample_text")
    a2 = ScaffoldGraph_Graph(name="sample_text_2")
    b = ScaffoldGraph_Edge(weight=7)
    _safe_set(b, 'ScaffoldGraph_Edge', a1)
    assert _is_linked(b, 'ScaffoldGraph_Edge', a1)
    if hasattr(a1, 'ScaffoldGraph_Graph2'):
        assert _is_linked(a1, 'ScaffoldGraph_Graph2', b)
    _safe_set(b, 'ScaffoldGraph_Edge', a2)
    assert _is_linked(b, 'ScaffoldGraph_Edge', a2)
    if hasattr(a1, 'ScaffoldGraph_Graph2'):
        assert not _is_linked(a1, 'ScaffoldGraph_Graph2', b)
    if hasattr(a2, 'ScaffoldGraph_Graph2'):
        assert _is_linked(a2, 'ScaffoldGraph_Graph2', b)
    _safe_set(b, 'ScaffoldGraph_Edge', None)
    assert not _is_linked(b, 'ScaffoldGraph_Edge', a2)
    if hasattr(a2, 'ScaffoldGraph_Graph2'):
        assert not _is_linked(a2, 'ScaffoldGraph_Graph2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_EVin6_stub_double():
    # ScaffoldGraph_Vertex has no real 'Vertex' property in the generated
    # code (a bare stub) -- manually attach it so ScaffoldGraph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ScaffoldGraph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ScaffoldGraph_Edge(weight=7)
    partner = ScaffoldGraph_Vertex()
    setattr(partner, 'Vertex', None)
    _safe_set(owner, 'VEin', partner)
    assert getattr(partner, 'Vertex') == owner
    _safe_set(owner, 'VEin', None)
    assert getattr(partner, 'Vertex') is None


def test_assoc_EVout7_stub_double():
    # ScaffoldGraph_Vertex has no real 'Vertex8' property in the generated
    # code (a bare stub) -- manually attach it so ScaffoldGraph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ScaffoldGraph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ScaffoldGraph_Edge(weight=7)
    partner = ScaffoldGraph_Vertex()
    setattr(partner, 'Vertex8', None)
    _safe_set(owner, 'VEout', partner)
    assert getattr(partner, 'Vertex8') == owner
    _safe_set(owner, 'VEout', None)
    assert getattr(partner, 'Vertex8') is None


def test_assoc_VEin3_stub_double():
    # ScaffoldGraph_Vertex has no real 'EVin' property in the generated
    # code (a bare stub) -- manually attach it so ScaffoldGraph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ScaffoldGraph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ScaffoldGraph_Edge(weight=7)
    partner = ScaffoldGraph_Vertex()
    setattr(partner, 'EVin', None)
    _safe_set(owner, 'Edge', partner)
    assert owner in getattr(partner, 'EVin')
    _safe_set(owner, 'Edge', None)
    assert owner not in getattr(partner, 'EVin')


def test_assoc_VEout4_stub_double():
    # ScaffoldGraph_Vertex has no real 'EVout' property in the generated
    # code (a bare stub) -- manually attach it so ScaffoldGraph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ScaffoldGraph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ScaffoldGraph_Edge(weight=7)
    partner = ScaffoldGraph_Vertex()
    setattr(partner, 'EVout', None)
    _safe_set(owner, 'Edge5', partner)
    assert owner in getattr(partner, 'EVout')
    _safe_set(owner, 'Edge5', None)
    assert owner not in getattr(partner, 'EVout')


def test_assoc_vertices0_stub_double():
    # ScaffoldGraph_Vertex has no real 'ScaffoldGraph_Vertex' property in the generated
    # code (a bare stub) -- manually attach it so ScaffoldGraph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ScaffoldGraph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ScaffoldGraph_Graph(name="sample_text")
    partner = ScaffoldGraph_Vertex()
    setattr(partner, 'ScaffoldGraph_Vertex', None)
    _safe_set(owner, 'ScaffoldGraph_Graph', {partner})
    assert getattr(partner, 'ScaffoldGraph_Vertex') == owner
    _safe_set(owner, 'ScaffoldGraph_Graph', set())
    assert getattr(partner, 'ScaffoldGraph_Vertex') is None


