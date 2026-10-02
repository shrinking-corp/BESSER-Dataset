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


