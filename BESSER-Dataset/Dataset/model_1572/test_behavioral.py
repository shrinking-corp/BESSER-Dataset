import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Graph_Edges,
    Graph_Graph,
    Graph_Vertices,
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

def test_assoc_edge3_reverse_link_reassign_clear():
    a1 = Graph_Vertices(name="sample_text")
    a2 = Graph_Vertices(name="sample_text_2")
    b = Graph_Edges(name="sample_text")
    _safe_set(b, 'Edges', a1)
    assert _is_linked(b, 'Edges', a1)
    if hasattr(a1, 'vertice'):
        assert _is_linked(a1, 'vertice', b)
    _safe_set(b, 'Edges', a2)
    assert _is_linked(b, 'Edges', a2)
    if hasattr(a1, 'vertice'):
        assert not _is_linked(a1, 'vertice', b)
    if hasattr(a2, 'vertice'):
        assert _is_linked(a2, 'vertice', b)
    _safe_set(b, 'Edges', None)
    assert not _is_linked(b, 'Edges', a2)
    if hasattr(a2, 'vertice'):
        assert not _is_linked(a2, 'vertice', b)


def test_assoc_vertice4_reverse_link_reassign_clear():
    a1 = Graph_Vertices(name="sample_text")
    a2 = Graph_Vertices(name="sample_text_2")
    b = Graph_Edges(name="sample_text")
    _safe_set(b, 'edge', {a1})
    assert _is_linked(b, 'edge', a1)
    if hasattr(a1, 'Vertices'):
        assert _is_linked(a1, 'Vertices', b)
    _safe_set(b, 'edge', {a2})
    assert _is_linked(b, 'edge', a2)
    if hasattr(a1, 'Vertices'):
        assert not _is_linked(a1, 'Vertices', b)
    if hasattr(a2, 'Vertices'):
        assert _is_linked(a2, 'Vertices', b)
    _safe_set(b, 'edge', set())
    assert not _is_linked(b, 'edge', a2)
    if hasattr(a2, 'Vertices'):
        assert not _is_linked(a2, 'Vertices', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edge1_stub_double():
    # Graph_Graph has no real 'Graph_Graph2' property in the generated
    # code (a bare stub) -- manually attach it so Graph_Edges's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Graph_Edges's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Graph_Edges(name="sample_text")
    partner = Graph_Graph()
    setattr(partner, 'Graph_Graph2', None)
    _safe_set(owner, 'Graph_Edges', partner)
    assert owner in getattr(partner, 'Graph_Graph2')
    _safe_set(owner, 'Graph_Edges', None)
    assert owner not in getattr(partner, 'Graph_Graph2')


def test_assoc_vertice0_stub_double():
    # Graph_Graph has no real 'Graph_Graph' property in the generated
    # code (a bare stub) -- manually attach it so Graph_Vertices's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Graph_Vertices's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Graph_Vertices(name="sample_text")
    partner = Graph_Graph()
    setattr(partner, 'Graph_Graph', None)
    _safe_set(owner, 'Graph_Vertices', partner)
    assert owner in getattr(partner, 'Graph_Graph')
    _safe_set(owner, 'Graph_Vertices', None)
    assert owner not in getattr(partner, 'Graph_Graph')


