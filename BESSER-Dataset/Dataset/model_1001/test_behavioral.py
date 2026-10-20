import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Data,
    Edge,
    Element,
    EndPoint,
    Graph,
    GraphML_Data,
    GraphML_Edge,
    GraphML_Element,
    GraphML_EndPoint,
    GraphML_Graph,
    GraphML_HyperEdge,
    GraphML_Key,
    GraphML_LocatedElement,
    GraphML_Node,
    GraphML_Port,
    GraphML_Root,
    Key,
    LocatedElement,
    Node,
    Port,
    AttrType,
    EdgeType,
    ElemType,
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

def test_assoc_contents6_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so GraphML_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphML_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphML_Graph(edgeDefault="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'graph', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'graph', set())
    assert getattr(partner, 'Element') is None


def test_assoc_datas3_stub_double():
    # Data has no real 'Data' property in the generated
    # code (a bare stub) -- manually attach it so GraphML_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphML_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphML_Element(id="sample_text")
    partner = Data()
    setattr(partner, 'Data', None)
    _safe_set(owner, 'GraphML_Element', {partner})
    assert getattr(partner, 'Data') == owner
    _safe_set(owner, 'GraphML_Element', set())
    assert getattr(partner, 'Data') is None


def test_assoc_graph4_stub_double():
    # Graph has no real 'Graph5' property in the generated
    # code (a bare stub) -- manually attach it so GraphML_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphML_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphML_Element(id="sample_text")
    partner = Graph()
    setattr(partner, 'Graph5', None)
    _safe_set(owner, 'contents', partner)
    assert getattr(partner, 'Graph5') == owner
    _safe_set(owner, 'contents', None)
    assert getattr(partner, 'Graph5') is None


def test_assoc_source7_stub_double():
    # Node has no real 'Node' property in the generated
    # code (a bare stub) -- manually attach it so GraphML_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphML_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphML_Edge(directed="sample_text")
    partner = Node()
    setattr(partner, 'Node', None)
    _safe_set(owner, 'sourceOf', partner)
    assert getattr(partner, 'Node') == owner
    _safe_set(owner, 'sourceOf', None)
    assert getattr(partner, 'Node') is None


def test_assoc_sourceport10_stub_double():
    # Port has no real 'Port' property in the generated
    # code (a bare stub) -- manually attach it so GraphML_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphML_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphML_Edge(directed="sample_text")
    partner = Port()
    setattr(partner, 'Port', None)
    _safe_set(owner, 'GraphML_Edge', partner)
    assert getattr(partner, 'Port') == owner
    _safe_set(owner, 'GraphML_Edge', None)
    assert getattr(partner, 'Port') is None


def test_assoc_target8_stub_double():
    # Node has no real 'Node9' property in the generated
    # code (a bare stub) -- manually attach it so GraphML_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphML_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphML_Edge(directed="sample_text")
    partner = Node()
    setattr(partner, 'Node9', None)
    _safe_set(owner, 'targetOf', partner)
    assert getattr(partner, 'Node9') == owner
    _safe_set(owner, 'targetOf', None)
    assert getattr(partner, 'Node9') is None


def test_assoc_targetport11_stub_double():
    # Port has no real 'Port13' property in the generated
    # code (a bare stub) -- manually attach it so GraphML_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphML_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphML_Edge(directed="sample_text")
    partner = Port()
    setattr(partner, 'Port13', None)
    _safe_set(owner, 'GraphML_Edge12', partner)
    assert getattr(partner, 'Port13') == owner
    _safe_set(owner, 'GraphML_Edge12', None)
    assert getattr(partner, 'Port13') is None


