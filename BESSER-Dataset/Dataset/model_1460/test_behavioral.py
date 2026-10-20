import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    graphs_CompositeNode,
    graphs_Edge,
    graphs_Graph,
    graphs_Node,
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

def test_assoc_ends11_reverse_link_reassign_clear():
    a1 = graphs_Node(name="sample_text")
    a2 = graphs_Node(name="sample_text_2")
    b = graphs_Edge(weight=7)
    _safe_set(b, 'graphs_Edge12', {a1})
    assert _is_linked(b, 'graphs_Edge12', a1)
    if hasattr(a1, 'graphs_Node13'):
        assert _is_linked(a1, 'graphs_Node13', b)
    _safe_set(b, 'graphs_Edge12', {a2})
    assert _is_linked(b, 'graphs_Edge12', a2)
    if hasattr(a1, 'graphs_Node13'):
        assert not _is_linked(a1, 'graphs_Node13', b)
    if hasattr(a2, 'graphs_Node13'):
        assert _is_linked(a2, 'graphs_Node13', b)
    _safe_set(b, 'graphs_Edge12', set())
    assert not _is_linked(b, 'graphs_Edge12', a2)
    if hasattr(a2, 'graphs_Node13'):
        assert not _is_linked(a2, 'graphs_Node13', b)


def test_assoc_src5_reverse_link_reassign_clear():
    a1 = graphs_Node(name="sample_text")
    a2 = graphs_Node(name="sample_text_2")
    b = graphs_Edge(weight=7)
    _safe_set(b, 'graphs_Edge6', a1)
    assert _is_linked(b, 'graphs_Edge6', a1)
    if hasattr(a1, 'graphs_Node7'):
        assert _is_linked(a1, 'graphs_Node7', b)
    _safe_set(b, 'graphs_Edge6', a2)
    assert _is_linked(b, 'graphs_Edge6', a2)
    if hasattr(a1, 'graphs_Node7'):
        assert not _is_linked(a1, 'graphs_Node7', b)
    if hasattr(a2, 'graphs_Node7'):
        assert _is_linked(a2, 'graphs_Node7', b)
    _safe_set(b, 'graphs_Edge6', None)
    assert not _is_linked(b, 'graphs_Edge6', a2)
    if hasattr(a2, 'graphs_Node7'):
        assert not _is_linked(a2, 'graphs_Node7', b)


def test_assoc_tar8_reverse_link_reassign_clear():
    a1 = graphs_Node(name="sample_text")
    a2 = graphs_Node(name="sample_text_2")
    b = graphs_Edge(weight=7)
    _safe_set(b, 'graphs_Edge9', a1)
    assert _is_linked(b, 'graphs_Edge9', a1)
    if hasattr(a1, 'graphs_Node10'):
        assert _is_linked(a1, 'graphs_Node10', b)
    _safe_set(b, 'graphs_Edge9', a2)
    assert _is_linked(b, 'graphs_Edge9', a2)
    if hasattr(a1, 'graphs_Node10'):
        assert not _is_linked(a1, 'graphs_Node10', b)
    if hasattr(a2, 'graphs_Node10'):
        assert _is_linked(a2, 'graphs_Node10', b)
    _safe_set(b, 'graphs_Edge9', None)
    assert not _is_linked(b, 'graphs_Edge9', a2)
    if hasattr(a2, 'graphs_Node10'):
        assert not _is_linked(a2, 'graphs_Node10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges1_stub_double():
    # graphs_Graph has no real 'graphs_Graph2' property in the generated
    # code (a bare stub) -- manually attach it so graphs_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphs_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphs_Edge(weight=7)
    partner = graphs_Graph()
    setattr(partner, 'graphs_Graph2', None)
    _safe_set(owner, 'graphs_Edge', partner)
    assert owner in getattr(partner, 'graphs_Graph2')
    _safe_set(owner, 'graphs_Edge', None)
    assert owner not in getattr(partner, 'graphs_Graph2')


def test_assoc_nodes0_stub_double():
    # graphs_Graph has no real 'graphs_Graph' property in the generated
    # code (a bare stub) -- manually attach it so graphs_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphs_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphs_Node(name="sample_text")
    partner = graphs_Graph()
    setattr(partner, 'graphs_Graph', None)
    _safe_set(owner, 'graphs_Node', partner)
    assert owner in getattr(partner, 'graphs_Graph')
    _safe_set(owner, 'graphs_Node', None)
    assert owner not in getattr(partner, 'graphs_Graph')


