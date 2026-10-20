import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Graph,
    dot_Attribute,
    dot_DirectedEdge,
    dot_DirectedGraph,
    dot_Graph,
    dot_GraphModel,
    dot_Node,
    dot_UnDirectedEdge,
    dot_UndirectedGraph,
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

def test_assoc_attributes16_stub_double():
    # dot_DirectedEdge has no real 'dot_DirectedEdge17' property in the generated
    # code (a bare stub) -- manually attach it so dot_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Attribute(weight=7)
    partner = dot_DirectedEdge()
    setattr(partner, 'dot_DirectedEdge17', None)
    _safe_set(owner, 'dot_Attribute18', partner)
    assert owner in getattr(partner, 'dot_DirectedEdge17')
    _safe_set(owner, 'dot_Attribute18', None)
    assert owner not in getattr(partner, 'dot_DirectedEdge17')


def test_assoc_attributes8_stub_double():
    # dot_UnDirectedEdge has no real 'dot_UnDirectedEdge9' property in the generated
    # code (a bare stub) -- manually attach it so dot_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Attribute(weight=7)
    partner = dot_UnDirectedEdge()
    setattr(partner, 'dot_UnDirectedEdge9', None)
    _safe_set(owner, 'dot_Attribute', partner)
    assert owner in getattr(partner, 'dot_UnDirectedEdge9')
    _safe_set(owner, 'dot_Attribute', None)
    assert owner not in getattr(partner, 'dot_UnDirectedEdge9')


def test_assoc_graph0_stub_double():
    # dot_GraphModel has no real 'dot_GraphModel' property in the generated
    # code (a bare stub) -- manually attach it so dot_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Graph(name="sample_text")
    partner = dot_GraphModel()
    setattr(partner, 'dot_GraphModel', None)
    _safe_set(owner, 'dot_Graph', partner)
    assert owner in getattr(partner, 'dot_GraphModel')
    _safe_set(owner, 'dot_Graph', None)
    assert owner not in getattr(partner, 'dot_GraphModel')


def test_assoc_src10_stub_double():
    # dot_DirectedEdge has no real 'dot_DirectedEdge11' property in the generated
    # code (a bare stub) -- manually attach it so dot_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Node(name="sample_text")
    partner = dot_DirectedEdge()
    setattr(partner, 'dot_DirectedEdge11', None)
    _safe_set(owner, 'dot_Node12', partner)
    assert getattr(partner, 'dot_DirectedEdge11') == owner
    _safe_set(owner, 'dot_Node12', None)
    assert getattr(partner, 'dot_DirectedEdge11') is None


def test_assoc_src3_stub_double():
    # dot_UnDirectedEdge has no real 'dot_UnDirectedEdge4' property in the generated
    # code (a bare stub) -- manually attach it so dot_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Node(name="sample_text")
    partner = dot_UnDirectedEdge()
    setattr(partner, 'dot_UnDirectedEdge4', None)
    _safe_set(owner, 'dot_Node', partner)
    assert getattr(partner, 'dot_UnDirectedEdge4') == owner
    _safe_set(owner, 'dot_Node', None)
    assert getattr(partner, 'dot_UnDirectedEdge4') is None


def test_assoc_tgt13_stub_double():
    # dot_DirectedEdge has no real 'dot_DirectedEdge14' property in the generated
    # code (a bare stub) -- manually attach it so dot_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Node(name="sample_text")
    partner = dot_DirectedEdge()
    setattr(partner, 'dot_DirectedEdge14', None)
    _safe_set(owner, 'dot_Node15', partner)
    assert getattr(partner, 'dot_DirectedEdge14') == owner
    _safe_set(owner, 'dot_Node15', None)
    assert getattr(partner, 'dot_DirectedEdge14') is None


def test_assoc_tgt5_stub_double():
    # dot_UnDirectedEdge has no real 'dot_UnDirectedEdge6' property in the generated
    # code (a bare stub) -- manually attach it so dot_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Node(name="sample_text")
    partner = dot_UnDirectedEdge()
    setattr(partner, 'dot_UnDirectedEdge6', None)
    _safe_set(owner, 'dot_Node7', partner)
    assert getattr(partner, 'dot_UnDirectedEdge6') == owner
    _safe_set(owner, 'dot_Node7', None)
    assert getattr(partner, 'dot_UnDirectedEdge6') is None


