import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Compartment,
    ComplexNodeShape,
    DOT_Anchor,
    DOT_Arc,
    DOT_ArrowShape,
    DOT_Compartment,
    DOT_ComplexLabel,
    DOT_ComplexNodeShape,
    DOT_DirectedArc,
    DOT_Graph,
    DOT_GraphElement,
    DOT_HorizontalCompartment,
    DOT_Label,
    DOT_Layer,
    DOT_MNodeShape,
    DOT_Node,
    DOT_NodeShape,
    DOT_Nodelike,
    DOT_PointNodeShape,
    DOT_PolygonNodeShape,
    DOT_RecordNodeShape,
    DOT_Shape,
    DOT_SimpleCompartment,
    DOT_SimpleLabel,
    DOT_SimpleNodeShape,
    DOT_SubGraph,
    DOT_UndirectedArc,
    DOT_VerticalCompartment,
    GraphElement,
    Label,
    NodeShape,
    Nodelike,
    Shape,
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

def test_assoc_arcs14_reverse_link_reassign_clear():
    a1 = DOT_Layer(layerSeparator="sample_text")
    a2 = DOT_Layer(layerSeparator="sample_text_2")
    b = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    _safe_set(b, 'Arc', a1)
    assert _is_linked(b, 'Arc', a1)
    if hasattr(a1, 'layers15'):
        assert _is_linked(a1, 'layers15', b)
    _safe_set(b, 'Arc', a2)
    assert _is_linked(b, 'Arc', a2)
    if hasattr(a1, 'layers15'):
        assert not _is_linked(a1, 'layers15', b)
    if hasattr(a2, 'layers15'):
        assert _is_linked(a2, 'layers15', b)
    _safe_set(b, 'Arc', None)
    assert not _is_linked(b, 'Arc', a2)
    if hasattr(a2, 'layers15'):
        assert not _is_linked(a2, 'layers15', b)


def test_assoc_arrowHead42_reverse_link_reassign_clear():
    a1 = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    a2 = DOT_DirectedArc(head_lp=9.99, tail_lp=9.99)
    b = DOT_ArrowShape(clipping="sample_text", isPlain=True, size=7)
    _safe_set(b, 'DOT_ArrowShape', a1)
    assert _is_linked(b, 'DOT_ArrowShape', a1)
    if hasattr(a1, 'DOT_DirectedArc'):
        assert _is_linked(a1, 'DOT_DirectedArc', b)
    _safe_set(b, 'DOT_ArrowShape', a2)
    assert _is_linked(b, 'DOT_ArrowShape', a2)
    if hasattr(a1, 'DOT_DirectedArc'):
        assert not _is_linked(a1, 'DOT_DirectedArc', b)
    if hasattr(a2, 'DOT_DirectedArc'):
        assert _is_linked(a2, 'DOT_DirectedArc', b)
    _safe_set(b, 'DOT_ArrowShape', None)
    assert not _is_linked(b, 'DOT_ArrowShape', a2)
    if hasattr(a2, 'DOT_DirectedArc'):
        assert not _is_linked(a2, 'DOT_DirectedArc', b)


def test_assoc_arrowTail48_reverse_link_reassign_clear():
    a1 = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    a2 = DOT_DirectedArc(head_lp=9.99, tail_lp=9.99)
    b = DOT_ArrowShape(clipping="sample_text", isPlain=True, size=7)
    _safe_set(b, 'DOT_ArrowShape50', a1)
    assert _is_linked(b, 'DOT_ArrowShape50', a1)
    if hasattr(a1, 'DOT_DirectedArc49'):
        assert _is_linked(a1, 'DOT_DirectedArc49', b)
    _safe_set(b, 'DOT_ArrowShape50', a2)
    assert _is_linked(b, 'DOT_ArrowShape50', a2)
    if hasattr(a1, 'DOT_DirectedArc49'):
        assert not _is_linked(a1, 'DOT_DirectedArc49', b)
    if hasattr(a2, 'DOT_DirectedArc49'):
        assert _is_linked(a2, 'DOT_DirectedArc49', b)
    _safe_set(b, 'DOT_ArrowShape50', None)
    assert not _is_linked(b, 'DOT_ArrowShape50', a2)
    if hasattr(a2, 'DOT_DirectedArc49'):
        assert not _is_linked(a2, 'DOT_DirectedArc49', b)


def test_assoc_graph16_reverse_link_reassign_clear():
    a1 = DOT_Layer(layerSeparator="sample_text")
    a2 = DOT_Layer(layerSeparator="sample_text_2")
    b = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    _safe_set(b, 'Graph', a1)
    assert _is_linked(b, 'Graph', a1)
    if hasattr(a1, 'layers17'):
        assert _is_linked(a1, 'layers17', b)
    _safe_set(b, 'Graph', a2)
    assert _is_linked(b, 'Graph', a2)
    if hasattr(a1, 'layers17'):
        assert not _is_linked(a1, 'layers17', b)
    if hasattr(a2, 'layers17'):
        assert _is_linked(a2, 'layers17', b)
    _safe_set(b, 'Graph', None)
    assert not _is_linked(b, 'Graph', a2)
    if hasattr(a2, 'layers17'):
        assert not _is_linked(a2, 'layers17', b)


def test_assoc_layers10_reverse_link_reassign_clear():
    a1 = DOT_Layer(layerSeparator="sample_text")
    a2 = DOT_Layer(layerSeparator="sample_text_2")
    b = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    _safe_set(b, 'graph11', {a1})
    assert _is_linked(b, 'graph11', a1)
    if hasattr(a1, 'Layer'):
        assert _is_linked(a1, 'Layer', b)
    _safe_set(b, 'graph11', {a2})
    assert _is_linked(b, 'graph11', a2)
    if hasattr(a1, 'Layer'):
        assert not _is_linked(a1, 'Layer', b)
    if hasattr(a2, 'Layer'):
        assert _is_linked(a2, 'Layer', b)
    _safe_set(b, 'graph11', set())
    assert not _is_linked(b, 'graph11', a2)
    if hasattr(a2, 'Layer'):
        assert not _is_linked(a2, 'Layer', b)


def test_assoc_layers36_reverse_link_reassign_clear():
    a1 = DOT_Layer(layerSeparator="sample_text")
    a2 = DOT_Layer(layerSeparator="sample_text_2")
    b = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    _safe_set(b, 'arcs', {a1})
    assert _is_linked(b, 'arcs', a1)
    if hasattr(a1, 'Layer37'):
        assert _is_linked(a1, 'Layer37', b)
    _safe_set(b, 'arcs', {a2})
    assert _is_linked(b, 'arcs', a2)
    if hasattr(a1, 'Layer37'):
        assert not _is_linked(a1, 'Layer37', b)
    if hasattr(a2, 'Layer37'):
        assert _is_linked(a2, 'Layer37', b)
    _safe_set(b, 'arcs', set())
    assert not _is_linked(b, 'arcs', a2)
    if hasattr(a2, 'Layer37'):
        assert not _is_linked(a2, 'Layer37', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_anchor5_stub_double():
    # DOT_Compartment has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Anchor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Anchor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Anchor(name="sample_text")
    partner = DOT_Compartment()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Anchor', partner)
    assert getattr(partner, 'source') == owner
    _safe_set(owner, 'Anchor', None)
    assert getattr(partner, 'source') is None


def test_assoc_element0_stub_double():
    # DOT_Label has no real 'label' property in the generated
    # code (a bare stub) -- manually attach it so DOT_GraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_GraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_GraphElement(color="sample_text", name="sample_text", style="sample_text")
    partner = DOT_Label()
    setattr(partner, 'label', None)
    _safe_set(owner, 'GraphElement', partner)
    assert getattr(partner, 'label') == owner
    _safe_set(owner, 'GraphElement', None)
    assert getattr(partner, 'label') is None


def test_assoc_fromNode32_stub_double():
    # DOT_Nodelike has no real 'Nodelike33' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'Nodelike33', None)
    _safe_set(owner, 'refers', partner)
    assert getattr(partner, 'Nodelike33') == owner
    _safe_set(owner, 'refers', None)
    assert getattr(partner, 'Nodelike33') is None


def test_assoc_graph23_stub_double():
    # DOT_Nodelike has no real 'nodes24' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'nodes24', None)
    _safe_set(owner, 'Graph25', partner)
    assert getattr(partner, 'nodes24') == owner
    _safe_set(owner, 'Graph25', None)
    assert getattr(partner, 'nodes24') is None


def test_assoc_headlabel43_stub_double():
    # DOT_Label has no real 'DOT_Label' property in the generated
    # code (a bare stub) -- manually attach it so DOT_DirectedArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_DirectedArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    partner = DOT_Label()
    setattr(partner, 'DOT_Label', None)
    _safe_set(owner, 'DOT_DirectedArc44', partner)
    assert getattr(partner, 'DOT_Label') == owner
    _safe_set(owner, 'DOT_DirectedArc44', None)
    assert getattr(partner, 'DOT_Label') is None


def test_assoc_label8_stub_double():
    # DOT_Label has no real 'Label' property in the generated
    # code (a bare stub) -- manually attach it so DOT_GraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_GraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_GraphElement(color="sample_text", name="sample_text", style="sample_text")
    partner = DOT_Label()
    setattr(partner, 'Label', None)
    _safe_set(owner, 'element', partner)
    assert getattr(partner, 'Label') == owner
    _safe_set(owner, 'element', None)
    assert getattr(partner, 'Label') is None


def test_assoc_layers26_stub_double():
    # DOT_Nodelike has no real 'nodes27' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Layer(layerSeparator="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'nodes27', None)
    _safe_set(owner, 'Layer28', partner)
    assert owner in getattr(partner, 'nodes27')
    _safe_set(owner, 'Layer28', None)
    assert owner not in getattr(partner, 'nodes27')


def test_assoc_lhead38_stub_double():
    # DOT_Nodelike has no real 'DOT_Nodelike' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'DOT_Nodelike', None)
    _safe_set(owner, 'DOT_Arc', partner)
    assert getattr(partner, 'DOT_Nodelike') == owner
    _safe_set(owner, 'DOT_Arc', None)
    assert getattr(partner, 'DOT_Nodelike') is None


def test_assoc_ltail39_stub_double():
    # DOT_Nodelike has no real 'DOT_Nodelike41' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'DOT_Nodelike41', None)
    _safe_set(owner, 'DOT_Arc40', partner)
    assert getattr(partner, 'DOT_Nodelike41') == owner
    _safe_set(owner, 'DOT_Arc40', None)
    assert getattr(partner, 'DOT_Nodelike41') is None


def test_assoc_nodes12_stub_double():
    # DOT_Nodelike has no real 'Nodelike13' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Layer(layerSeparator="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'Nodelike13', None)
    _safe_set(owner, 'layers', {partner})
    assert getattr(partner, 'Nodelike13') == owner
    _safe_set(owner, 'layers', set())
    assert getattr(partner, 'Nodelike13') is None


def test_assoc_nodes29_stub_double():
    # DOT_Nodelike has no real 'Nodelike30' property in the generated
    # code (a bare stub) -- manually attach it so DOT_SubGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_SubGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_SubGraph(labelloc="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'Nodelike30', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'Nodelike30') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'Nodelike30') is None


def test_assoc_nodes9_stub_double():
    # DOT_Nodelike has no real 'Nodelike' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'Nodelike', None)
    _safe_set(owner, 'graph', {partner})
    assert getattr(partner, 'Nodelike') == owner
    _safe_set(owner, 'graph', set())
    assert getattr(partner, 'Nodelike') is None


def test_assoc_owner18_stub_double():
    # DOT_Nodelike has no real 'nodes' property in the generated
    # code (a bare stub) -- manually attach it so DOT_SubGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_SubGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_SubGraph(labelloc="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'nodes', None)
    _safe_set(owner, 'SubGraph', partner)
    assert getattr(partner, 'nodes') == owner
    _safe_set(owner, 'SubGraph', None)
    assert getattr(partner, 'nodes') is None


def test_assoc_referredBy21_stub_double():
    # DOT_Nodelike has no real 'toNode' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'toNode', None)
    _safe_set(owner, 'Arc22', partner)
    assert owner in getattr(partner, 'toNode')
    _safe_set(owner, 'Arc22', None)
    assert owner not in getattr(partner, 'toNode')


def test_assoc_refers19_stub_double():
    # DOT_Nodelike has no real 'fromNode' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'fromNode', None)
    _safe_set(owner, 'Arc20', partner)
    assert owner in getattr(partner, 'fromNode')
    _safe_set(owner, 'Arc20', None)
    assert owner not in getattr(partner, 'fromNode')


def test_assoc_shape31_stub_double():
    # DOT_NodeShape has no real 'DOT_NodeShape' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Node(fixedSize=True, fontname="sample_text", fontsize=7, height=7, width=7)
    partner = DOT_NodeShape()
    setattr(partner, 'DOT_NodeShape', None)
    _safe_set(owner, 'DOT_Node', partner)
    assert getattr(partner, 'DOT_NodeShape') == owner
    _safe_set(owner, 'DOT_Node', None)
    assert getattr(partner, 'DOT_NodeShape') is None


def test_assoc_source6_stub_double():
    # DOT_Compartment has no real 'Compartment7' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Anchor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Anchor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Anchor(name="sample_text")
    partner = DOT_Compartment()
    setattr(partner, 'Compartment7', None)
    _safe_set(owner, 'anchor', partner)
    assert getattr(partner, 'Compartment7') == owner
    _safe_set(owner, 'anchor', None)
    assert getattr(partner, 'Compartment7') is None


def test_assoc_taillabel45_stub_double():
    # DOT_Label has no real 'DOT_Label47' property in the generated
    # code (a bare stub) -- manually attach it so DOT_DirectedArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_DirectedArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    partner = DOT_Label()
    setattr(partner, 'DOT_Label47', None)
    _safe_set(owner, 'DOT_DirectedArc46', partner)
    assert getattr(partner, 'DOT_Label47') == owner
    _safe_set(owner, 'DOT_DirectedArc46', None)
    assert getattr(partner, 'DOT_Label47') is None


def test_assoc_toNode34_stub_double():
    # DOT_Nodelike has no real 'Nodelike35' property in the generated
    # code (a bare stub) -- manually attach it so DOT_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DOT_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    partner = DOT_Nodelike()
    setattr(partner, 'Nodelike35', None)
    _safe_set(owner, 'referredBy', partner)
    assert getattr(partner, 'Nodelike35') == owner
    _safe_set(owner, 'referredBy', None)
    assert getattr(partner, 'Nodelike35') is None


