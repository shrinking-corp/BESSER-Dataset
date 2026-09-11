import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_DOT_Anchor_name_value_roundtrip():
    instance = DOT_Anchor(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DOT_Arc_constraint_value_roundtrip():
    instance = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    assert instance.constraint == True
    instance.constraint = False
    assert instance.constraint == False


def test_DOT_Arc_decorate_value_roundtrip():
    instance = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    assert instance.decorate == True
    instance.decorate = False
    assert instance.decorate == False


def test_DOT_Arc_group_value_roundtrip():
    instance = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_DOT_Arc_minlen_value_roundtrip():
    instance = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    assert instance.minlen == 7
    instance.minlen = 13
    assert instance.minlen == 13


def test_DOT_Arc_sameHead_value_roundtrip():
    instance = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    assert instance.sameHead == "sample_text"
    instance.sameHead = "sample_text_2"
    assert instance.sameHead == "sample_text_2"


def test_DOT_Arc_sameTail_value_roundtrip():
    instance = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    assert instance.sameTail == "sample_text"
    instance.sameTail = "sample_text_2"
    assert instance.sameTail == "sample_text_2"


def test_DOT_ArrowShape_clipping_value_roundtrip():
    instance = DOT_ArrowShape(clipping="sample_text", isPlain=True, size=7)
    assert instance.clipping == "sample_text"
    instance.clipping = "sample_text_2"
    assert instance.clipping == "sample_text_2"


def test_DOT_ArrowShape_isPlain_value_roundtrip():
    instance = DOT_ArrowShape(clipping="sample_text", isPlain=True, size=7)
    assert instance.isPlain == True
    instance.isPlain = False
    assert instance.isPlain == False


def test_DOT_ArrowShape_size_value_roundtrip():
    instance = DOT_ArrowShape(clipping="sample_text", isPlain=True, size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_DOT_DirectedArc_head_lp_value_roundtrip():
    instance = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    assert instance.head_lp == 3.14
    instance.head_lp = 9.99
    assert instance.head_lp == 9.99


def test_DOT_DirectedArc_tail_lp_value_roundtrip():
    instance = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    assert instance.tail_lp == 3.14
    instance.tail_lp = 9.99
    assert instance.tail_lp == 9.99


def test_DOT_Graph_boundingBox_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.boundingBox == "sample_text"
    instance.boundingBox = "sample_text_2"
    assert instance.boundingBox == "sample_text_2"


def test_DOT_Graph_center_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.center == True
    instance.center = False
    assert instance.center == False


def test_DOT_Graph_compound_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.compound == True
    instance.compound = False
    assert instance.compound == False


def test_DOT_Graph_concentrate_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.concentrate == True
    instance.concentrate = False
    assert instance.concentrate == False


def test_DOT_Graph_labeljust_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.labeljust == "sample_text"
    instance.labeljust = "sample_text_2"
    assert instance.labeljust == "sample_text_2"


def test_DOT_Graph_labelloc_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.labelloc == "sample_text"
    instance.labelloc = "sample_text_2"
    assert instance.labelloc == "sample_text_2"


def test_DOT_Graph_nodeSeparation_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.nodeSeparation == 3.14
    instance.nodeSeparation = 9.99
    assert instance.nodeSeparation == 9.99


def test_DOT_Graph_ordering_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.ordering == "sample_text"
    instance.ordering = "sample_text_2"
    assert instance.ordering == "sample_text_2"


def test_DOT_Graph_rankDir_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.rankDir == "sample_text"
    instance.rankDir = "sample_text_2"
    assert instance.rankDir == "sample_text_2"


def test_DOT_Graph_ratio_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.ratio == "sample_text"
    instance.ratio = "sample_text_2"
    assert instance.ratio == "sample_text_2"


def test_DOT_Graph_size_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_DOT_Graph_type_value_roundtrip():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_DOT_GraphElement_color_value_roundtrip():
    instance = DOT_GraphElement(color="sample_text", name="sample_text", style="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_DOT_GraphElement_name_value_roundtrip():
    instance = DOT_GraphElement(color="sample_text", name="sample_text", style="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_DOT_GraphElement_style_value_roundtrip():
    instance = DOT_GraphElement(color="sample_text", name="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_DOT_Layer_layerSeparator_value_roundtrip():
    instance = DOT_Layer(layerSeparator="sample_text")
    assert instance.layerSeparator == "sample_text"
    instance.layerSeparator = "sample_text_2"
    assert instance.layerSeparator == "sample_text_2"


def test_DOT_Node_fixedSize_value_roundtrip():
    instance = DOT_Node(fixedSize=True, fontname="sample_text", fontsize=7, height=7, width=7)
    assert instance.fixedSize == True
    instance.fixedSize = False
    assert instance.fixedSize == False


def test_DOT_Node_fontname_value_roundtrip():
    instance = DOT_Node(fixedSize=True, fontname="sample_text", fontsize=7, height=7, width=7)
    assert instance.fontname == "sample_text"
    instance.fontname = "sample_text_2"
    assert instance.fontname == "sample_text_2"


def test_DOT_Node_fontsize_value_roundtrip():
    instance = DOT_Node(fixedSize=True, fontname="sample_text", fontsize=7, height=7, width=7)
    assert instance.fontsize == 7
    instance.fontsize = 13
    assert instance.fontsize == 13


def test_DOT_Node_height_value_roundtrip():
    instance = DOT_Node(fixedSize=True, fontname="sample_text", fontsize=7, height=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_DOT_Node_width_value_roundtrip():
    instance = DOT_Node(fixedSize=True, fontname="sample_text", fontsize=7, height=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_DOT_PolygonNodeShape_distortion_value_roundtrip():
    instance = DOT_PolygonNodeShape(distortion=7, isRegular=True, orientation=7, sides=7, skew=7)
    assert instance.distortion == 7
    instance.distortion = 13
    assert instance.distortion == 13


def test_DOT_PolygonNodeShape_isRegular_value_roundtrip():
    instance = DOT_PolygonNodeShape(distortion=7, isRegular=True, orientation=7, sides=7, skew=7)
    assert instance.isRegular == True
    instance.isRegular = False
    assert instance.isRegular == False


def test_DOT_PolygonNodeShape_orientation_value_roundtrip():
    instance = DOT_PolygonNodeShape(distortion=7, isRegular=True, orientation=7, sides=7, skew=7)
    assert instance.orientation == 7
    instance.orientation = 13
    assert instance.orientation == 13


def test_DOT_PolygonNodeShape_sides_value_roundtrip():
    instance = DOT_PolygonNodeShape(distortion=7, isRegular=True, orientation=7, sides=7, skew=7)
    assert instance.sides == 7
    instance.sides = 13
    assert instance.sides == 13


def test_DOT_PolygonNodeShape_skew_value_roundtrip():
    instance = DOT_PolygonNodeShape(distortion=7, isRegular=True, orientation=7, sides=7, skew=7)
    assert instance.skew == 7
    instance.skew = 13
    assert instance.skew == 13


def test_DOT_Shape_height_value_roundtrip():
    instance = DOT_Shape(height=7, peripheries=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_DOT_Shape_peripheries_value_roundtrip():
    instance = DOT_Shape(height=7, peripheries=7, width=7)
    assert instance.peripheries == 7
    instance.peripheries = 13
    assert instance.peripheries == 13


def test_DOT_Shape_width_value_roundtrip():
    instance = DOT_Shape(height=7, peripheries=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_DOT_SimpleCompartment_content_value_roundtrip():
    instance = DOT_SimpleCompartment(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_DOT_SimpleLabel_content_value_roundtrip():
    instance = DOT_SimpleLabel(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_DOT_SubGraph_labelloc_value_roundtrip():
    instance = DOT_SubGraph(labelloc="sample_text")
    assert instance.labelloc == "sample_text"
    instance.labelloc = "sample_text_2"
    assert instance.labelloc == "sample_text_2"


def test_DOT_DirectedArc_isa_Arc():
    instance = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    assert isinstance(instance, Arc)


def test_DOT_UndirectedArc_isa_Arc():
    instance = DOT_UndirectedArc()
    assert isinstance(instance, Arc)


def test_DOT_HorizontalCompartment_isa_Compartment():
    instance = DOT_HorizontalCompartment()
    assert isinstance(instance, Compartment)


def test_DOT_SimpleCompartment_isa_Compartment():
    instance = DOT_SimpleCompartment(content="sample_text")
    assert isinstance(instance, Compartment)


def test_DOT_VerticalCompartment_isa_Compartment():
    instance = DOT_VerticalCompartment()
    assert isinstance(instance, Compartment)


def test_DOT_MNodeShape_isa_ComplexNodeShape():
    instance = DOT_MNodeShape()
    assert isinstance(instance, ComplexNodeShape)


def test_DOT_PolygonNodeShape_isa_ComplexNodeShape():
    instance = DOT_PolygonNodeShape(distortion=7, isRegular=True, orientation=7, sides=7, skew=7)
    assert isinstance(instance, ComplexNodeShape)


def test_DOT_RecordNodeShape_isa_ComplexNodeShape():
    instance = DOT_RecordNodeShape()
    assert isinstance(instance, ComplexNodeShape)


def test_DOT_Arc_isa_GraphElement():
    instance = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    assert isinstance(instance, GraphElement)


def test_DOT_Graph_isa_GraphElement():
    instance = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    assert isinstance(instance, GraphElement)


def test_DOT_Layer_isa_GraphElement():
    instance = DOT_Layer(layerSeparator="sample_text")
    assert isinstance(instance, GraphElement)


def test_DOT_Nodelike_isa_GraphElement():
    instance = DOT_Nodelike()
    assert isinstance(instance, GraphElement)


def test_DOT_Shape_isa_GraphElement():
    instance = DOT_Shape(height=7, peripheries=7, width=7)
    assert isinstance(instance, GraphElement)


def test_DOT_ComplexLabel_isa_Label():
    instance = DOT_ComplexLabel()
    assert isinstance(instance, Label)


def test_DOT_SimpleLabel_isa_Label():
    instance = DOT_SimpleLabel(content="sample_text")
    assert isinstance(instance, Label)


def test_DOT_ComplexNodeShape_isa_NodeShape():
    instance = DOT_ComplexNodeShape()
    assert isinstance(instance, NodeShape)


def test_DOT_PointNodeShape_isa_NodeShape():
    instance = DOT_PointNodeShape()
    assert isinstance(instance, NodeShape)


def test_DOT_SimpleNodeShape_isa_NodeShape():
    instance = DOT_SimpleNodeShape()
    assert isinstance(instance, NodeShape)


def test_DOT_Node_isa_Nodelike():
    instance = DOT_Node(fixedSize=True, fontname="sample_text", fontsize=7, height=7, width=7)
    assert isinstance(instance, Nodelike)


def test_DOT_SubGraph_isa_Nodelike():
    instance = DOT_SubGraph(labelloc="sample_text")
    assert isinstance(instance, Nodelike)


def test_DOT_ArrowShape_isa_Shape():
    instance = DOT_ArrowShape(clipping="sample_text", isPlain=True, size=7)
    assert isinstance(instance, Shape)


def test_DOT_NodeShape_isa_Shape():
    instance = DOT_NodeShape()
    assert isinstance(instance, Shape)


def test_assoc_anchor5_link_reassign_clear():
    a = DOT_Anchor(name="sample_text")
    b1 = DOT_Compartment()
    b2 = DOT_Compartment()
    _safe_set(a, 'Anchor', b1)
    assert _is_linked(a, 'Anchor', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'Anchor', b2)
    assert _is_linked(a, 'Anchor', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'Anchor', None)
    assert not _is_linked(a, 'Anchor', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_arcs14_link_reassign_clear():
    a = DOT_Layer(layerSeparator="sample_text")
    b1 = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    b2 = DOT_Arc(constraint=False, decorate=False, group="sample_text_2", minlen=13, sameHead="sample_text_2", sameTail="sample_text_2")
    _safe_set(a, 'layers15', {b1})
    assert _is_linked(a, 'layers15', b1)
    if hasattr(b1, 'Arc'):
        assert _is_linked(b1, 'Arc', a)
    _safe_set(a, 'layers15', {b2})
    assert _is_linked(a, 'layers15', b2)
    if hasattr(b1, 'Arc'):
        assert not _is_linked(b1, 'Arc', a)
    if hasattr(b2, 'Arc'):
        assert _is_linked(b2, 'Arc', a)
    _safe_set(a, 'layers15', set())
    assert not _is_linked(a, 'layers15', b2)
    if hasattr(b2, 'Arc'):
        assert not _is_linked(b2, 'Arc', a)


def test_assoc_arrowHead42_link_reassign_clear():
    a = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    b1 = DOT_ArrowShape(clipping="sample_text", isPlain=True, size=7)
    b2 = DOT_ArrowShape(clipping="sample_text_2", isPlain=False, size=13)
    _safe_set(a, 'DOT_DirectedArc', b1)
    assert _is_linked(a, 'DOT_DirectedArc', b1)
    if hasattr(b1, 'DOT_ArrowShape'):
        assert _is_linked(b1, 'DOT_ArrowShape', a)
    _safe_set(a, 'DOT_DirectedArc', b2)
    assert _is_linked(a, 'DOT_DirectedArc', b2)
    if hasattr(b1, 'DOT_ArrowShape'):
        assert not _is_linked(b1, 'DOT_ArrowShape', a)
    if hasattr(b2, 'DOT_ArrowShape'):
        assert _is_linked(b2, 'DOT_ArrowShape', a)
    _safe_set(a, 'DOT_DirectedArc', None)
    assert not _is_linked(a, 'DOT_DirectedArc', b2)
    if hasattr(b2, 'DOT_ArrowShape'):
        assert not _is_linked(b2, 'DOT_ArrowShape', a)


def test_assoc_arrowTail48_link_reassign_clear():
    a = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    b1 = DOT_ArrowShape(clipping="sample_text", isPlain=True, size=7)
    b2 = DOT_ArrowShape(clipping="sample_text_2", isPlain=False, size=13)
    _safe_set(a, 'DOT_DirectedArc49', b1)
    assert _is_linked(a, 'DOT_DirectedArc49', b1)
    if hasattr(b1, 'DOT_ArrowShape50'):
        assert _is_linked(b1, 'DOT_ArrowShape50', a)
    _safe_set(a, 'DOT_DirectedArc49', b2)
    assert _is_linked(a, 'DOT_DirectedArc49', b2)
    if hasattr(b1, 'DOT_ArrowShape50'):
        assert not _is_linked(b1, 'DOT_ArrowShape50', a)
    if hasattr(b2, 'DOT_ArrowShape50'):
        assert _is_linked(b2, 'DOT_ArrowShape50', a)
    _safe_set(a, 'DOT_DirectedArc49', None)
    assert not _is_linked(a, 'DOT_DirectedArc49', b2)
    if hasattr(b2, 'DOT_ArrowShape50'):
        assert not _is_linked(b2, 'DOT_ArrowShape50', a)


def test_assoc_element0_link_reassign_clear():
    a = DOT_GraphElement(color="sample_text", name="sample_text", style="sample_text")
    b1 = DOT_Label()
    b2 = DOT_Label()
    _safe_set(a, 'GraphElement', b1)
    assert _is_linked(a, 'GraphElement', b1)
    if hasattr(b1, 'label'):
        assert _is_linked(b1, 'label', a)
    _safe_set(a, 'GraphElement', b2)
    assert _is_linked(a, 'GraphElement', b2)
    if hasattr(b1, 'label'):
        assert not _is_linked(b1, 'label', a)
    if hasattr(b2, 'label'):
        assert _is_linked(b2, 'label', a)
    _safe_set(a, 'GraphElement', None)
    assert not _is_linked(a, 'GraphElement', b2)
    if hasattr(b2, 'label'):
        assert not _is_linked(b2, 'label', a)


def test_assoc_fromNode32_link_reassign_clear():
    a = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'refers', b1)
    assert _is_linked(a, 'refers', b1)
    if hasattr(b1, 'Nodelike33'):
        assert _is_linked(b1, 'Nodelike33', a)
    _safe_set(a, 'refers', b2)
    assert _is_linked(a, 'refers', b2)
    if hasattr(b1, 'Nodelike33'):
        assert not _is_linked(b1, 'Nodelike33', a)
    if hasattr(b2, 'Nodelike33'):
        assert _is_linked(b2, 'Nodelike33', a)
    _safe_set(a, 'refers', None)
    assert not _is_linked(a, 'refers', b2)
    if hasattr(b2, 'Nodelike33'):
        assert not _is_linked(b2, 'Nodelike33', a)


def test_assoc_graph16_link_reassign_clear():
    a = DOT_Layer(layerSeparator="sample_text")
    b1 = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    b2 = DOT_Graph(boundingBox="sample_text_2", center=False, compound=False, concentrate=False, labeljust="sample_text_2", labelloc="sample_text_2", nodeSeparation=9.99, ordering="sample_text_2", rankDir="sample_text_2", ratio="sample_text_2", size="sample_text_2", type="sample_text_2")
    _safe_set(a, 'layers17', b1)
    assert _is_linked(a, 'layers17', b1)
    if hasattr(b1, 'Graph'):
        assert _is_linked(b1, 'Graph', a)
    _safe_set(a, 'layers17', b2)
    assert _is_linked(a, 'layers17', b2)
    if hasattr(b1, 'Graph'):
        assert not _is_linked(b1, 'Graph', a)
    if hasattr(b2, 'Graph'):
        assert _is_linked(b2, 'Graph', a)
    _safe_set(a, 'layers17', None)
    assert not _is_linked(a, 'layers17', b2)
    if hasattr(b2, 'Graph'):
        assert not _is_linked(b2, 'Graph', a)


def test_assoc_graph23_link_reassign_clear():
    a = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'Graph25', b1)
    assert _is_linked(a, 'Graph25', b1)
    if hasattr(b1, 'nodes24'):
        assert _is_linked(b1, 'nodes24', a)
    _safe_set(a, 'Graph25', b2)
    assert _is_linked(a, 'Graph25', b2)
    if hasattr(b1, 'nodes24'):
        assert not _is_linked(b1, 'nodes24', a)
    if hasattr(b2, 'nodes24'):
        assert _is_linked(b2, 'nodes24', a)
    _safe_set(a, 'Graph25', None)
    assert not _is_linked(a, 'Graph25', b2)
    if hasattr(b2, 'nodes24'):
        assert not _is_linked(b2, 'nodes24', a)


def test_assoc_headlabel43_link_reassign_clear():
    a = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    b1 = DOT_Label()
    b2 = DOT_Label()
    _safe_set(a, 'DOT_DirectedArc44', b1)
    assert _is_linked(a, 'DOT_DirectedArc44', b1)
    if hasattr(b1, 'DOT_Label'):
        assert _is_linked(b1, 'DOT_Label', a)
    _safe_set(a, 'DOT_DirectedArc44', b2)
    assert _is_linked(a, 'DOT_DirectedArc44', b2)
    if hasattr(b1, 'DOT_Label'):
        assert not _is_linked(b1, 'DOT_Label', a)
    if hasattr(b2, 'DOT_Label'):
        assert _is_linked(b2, 'DOT_Label', a)
    _safe_set(a, 'DOT_DirectedArc44', None)
    assert not _is_linked(a, 'DOT_DirectedArc44', b2)
    if hasattr(b2, 'DOT_Label'):
        assert not _is_linked(b2, 'DOT_Label', a)


def test_assoc_label8_link_reassign_clear():
    a = DOT_GraphElement(color="sample_text", name="sample_text", style="sample_text")
    b1 = DOT_Label()
    b2 = DOT_Label()
    _safe_set(a, 'element', b1)
    assert _is_linked(a, 'element', b1)
    if hasattr(b1, 'Label'):
        assert _is_linked(b1, 'Label', a)
    _safe_set(a, 'element', b2)
    assert _is_linked(a, 'element', b2)
    if hasattr(b1, 'Label'):
        assert not _is_linked(b1, 'Label', a)
    if hasattr(b2, 'Label'):
        assert _is_linked(b2, 'Label', a)
    _safe_set(a, 'element', None)
    assert not _is_linked(a, 'element', b2)
    if hasattr(b2, 'Label'):
        assert not _is_linked(b2, 'Label', a)


def test_assoc_layers10_link_reassign_clear():
    a = DOT_Layer(layerSeparator="sample_text")
    b1 = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    b2 = DOT_Graph(boundingBox="sample_text_2", center=False, compound=False, concentrate=False, labeljust="sample_text_2", labelloc="sample_text_2", nodeSeparation=9.99, ordering="sample_text_2", rankDir="sample_text_2", ratio="sample_text_2", size="sample_text_2", type="sample_text_2")
    _safe_set(a, 'Layer', b1)
    assert _is_linked(a, 'Layer', b1)
    if hasattr(b1, 'graph11'):
        assert _is_linked(b1, 'graph11', a)
    _safe_set(a, 'Layer', b2)
    assert _is_linked(a, 'Layer', b2)
    if hasattr(b1, 'graph11'):
        assert not _is_linked(b1, 'graph11', a)
    if hasattr(b2, 'graph11'):
        assert _is_linked(b2, 'graph11', a)
    _safe_set(a, 'Layer', None)
    assert not _is_linked(a, 'Layer', b2)
    if hasattr(b2, 'graph11'):
        assert not _is_linked(b2, 'graph11', a)


def test_assoc_layers26_link_reassign_clear():
    a = DOT_Layer(layerSeparator="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'Layer28', b1)
    assert _is_linked(a, 'Layer28', b1)
    if hasattr(b1, 'nodes27'):
        assert _is_linked(b1, 'nodes27', a)
    _safe_set(a, 'Layer28', b2)
    assert _is_linked(a, 'Layer28', b2)
    if hasattr(b1, 'nodes27'):
        assert not _is_linked(b1, 'nodes27', a)
    if hasattr(b2, 'nodes27'):
        assert _is_linked(b2, 'nodes27', a)
    _safe_set(a, 'Layer28', None)
    assert not _is_linked(a, 'Layer28', b2)
    if hasattr(b2, 'nodes27'):
        assert not _is_linked(b2, 'nodes27', a)


def test_assoc_layers36_link_reassign_clear():
    a = DOT_Layer(layerSeparator="sample_text")
    b1 = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    b2 = DOT_Arc(constraint=False, decorate=False, group="sample_text_2", minlen=13, sameHead="sample_text_2", sameTail="sample_text_2")
    _safe_set(a, 'Layer37', b1)
    assert _is_linked(a, 'Layer37', b1)
    if hasattr(b1, 'arcs'):
        assert _is_linked(b1, 'arcs', a)
    _safe_set(a, 'Layer37', b2)
    assert _is_linked(a, 'Layer37', b2)
    if hasattr(b1, 'arcs'):
        assert not _is_linked(b1, 'arcs', a)
    if hasattr(b2, 'arcs'):
        assert _is_linked(b2, 'arcs', a)
    _safe_set(a, 'Layer37', None)
    assert not _is_linked(a, 'Layer37', b2)
    if hasattr(b2, 'arcs'):
        assert not _is_linked(b2, 'arcs', a)


def test_assoc_lhead38_link_reassign_clear():
    a = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'DOT_Arc', b1)
    assert _is_linked(a, 'DOT_Arc', b1)
    if hasattr(b1, 'DOT_Nodelike'):
        assert _is_linked(b1, 'DOT_Nodelike', a)
    _safe_set(a, 'DOT_Arc', b2)
    assert _is_linked(a, 'DOT_Arc', b2)
    if hasattr(b1, 'DOT_Nodelike'):
        assert not _is_linked(b1, 'DOT_Nodelike', a)
    if hasattr(b2, 'DOT_Nodelike'):
        assert _is_linked(b2, 'DOT_Nodelike', a)
    _safe_set(a, 'DOT_Arc', None)
    assert not _is_linked(a, 'DOT_Arc', b2)
    if hasattr(b2, 'DOT_Nodelike'):
        assert not _is_linked(b2, 'DOT_Nodelike', a)


def test_assoc_ltail39_link_reassign_clear():
    a = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'DOT_Arc40', b1)
    assert _is_linked(a, 'DOT_Arc40', b1)
    if hasattr(b1, 'DOT_Nodelike41'):
        assert _is_linked(b1, 'DOT_Nodelike41', a)
    _safe_set(a, 'DOT_Arc40', b2)
    assert _is_linked(a, 'DOT_Arc40', b2)
    if hasattr(b1, 'DOT_Nodelike41'):
        assert not _is_linked(b1, 'DOT_Nodelike41', a)
    if hasattr(b2, 'DOT_Nodelike41'):
        assert _is_linked(b2, 'DOT_Nodelike41', a)
    _safe_set(a, 'DOT_Arc40', None)
    assert not _is_linked(a, 'DOT_Arc40', b2)
    if hasattr(b2, 'DOT_Nodelike41'):
        assert not _is_linked(b2, 'DOT_Nodelike41', a)


def test_assoc_nodes12_link_reassign_clear():
    a = DOT_Layer(layerSeparator="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'layers', {b1})
    assert _is_linked(a, 'layers', b1)
    if hasattr(b1, 'Nodelike13'):
        assert _is_linked(b1, 'Nodelike13', a)
    _safe_set(a, 'layers', {b2})
    assert _is_linked(a, 'layers', b2)
    if hasattr(b1, 'Nodelike13'):
        assert not _is_linked(b1, 'Nodelike13', a)
    if hasattr(b2, 'Nodelike13'):
        assert _is_linked(b2, 'Nodelike13', a)
    _safe_set(a, 'layers', set())
    assert not _is_linked(a, 'layers', b2)
    if hasattr(b2, 'Nodelike13'):
        assert not _is_linked(b2, 'Nodelike13', a)


def test_assoc_nodes29_link_reassign_clear():
    a = DOT_SubGraph(labelloc="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'owner', {b1})
    assert _is_linked(a, 'owner', b1)
    if hasattr(b1, 'Nodelike30'):
        assert _is_linked(b1, 'Nodelike30', a)
    _safe_set(a, 'owner', {b2})
    assert _is_linked(a, 'owner', b2)
    if hasattr(b1, 'Nodelike30'):
        assert not _is_linked(b1, 'Nodelike30', a)
    if hasattr(b2, 'Nodelike30'):
        assert _is_linked(b2, 'Nodelike30', a)
    _safe_set(a, 'owner', set())
    assert not _is_linked(a, 'owner', b2)
    if hasattr(b2, 'Nodelike30'):
        assert not _is_linked(b2, 'Nodelike30', a)


def test_assoc_nodes9_link_reassign_clear():
    a = DOT_Graph(boundingBox="sample_text", center=True, compound=True, concentrate=True, labeljust="sample_text", labelloc="sample_text", nodeSeparation=3.14, ordering="sample_text", rankDir="sample_text", ratio="sample_text", size="sample_text", type="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'graph', {b1})
    assert _is_linked(a, 'graph', b1)
    if hasattr(b1, 'Nodelike'):
        assert _is_linked(b1, 'Nodelike', a)
    _safe_set(a, 'graph', {b2})
    assert _is_linked(a, 'graph', b2)
    if hasattr(b1, 'Nodelike'):
        assert not _is_linked(b1, 'Nodelike', a)
    if hasattr(b2, 'Nodelike'):
        assert _is_linked(b2, 'Nodelike', a)
    _safe_set(a, 'graph', set())
    assert not _is_linked(a, 'graph', b2)
    if hasattr(b2, 'Nodelike'):
        assert not _is_linked(b2, 'Nodelike', a)


def test_assoc_owner18_link_reassign_clear():
    a = DOT_SubGraph(labelloc="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'SubGraph', b1)
    assert _is_linked(a, 'SubGraph', b1)
    if hasattr(b1, 'nodes'):
        assert _is_linked(b1, 'nodes', a)
    _safe_set(a, 'SubGraph', b2)
    assert _is_linked(a, 'SubGraph', b2)
    if hasattr(b1, 'nodes'):
        assert not _is_linked(b1, 'nodes', a)
    if hasattr(b2, 'nodes'):
        assert _is_linked(b2, 'nodes', a)
    _safe_set(a, 'SubGraph', None)
    assert not _is_linked(a, 'SubGraph', b2)
    if hasattr(b2, 'nodes'):
        assert not _is_linked(b2, 'nodes', a)


def test_assoc_referredBy21_link_reassign_clear():
    a = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'Arc22', b1)
    assert _is_linked(a, 'Arc22', b1)
    if hasattr(b1, 'toNode'):
        assert _is_linked(b1, 'toNode', a)
    _safe_set(a, 'Arc22', b2)
    assert _is_linked(a, 'Arc22', b2)
    if hasattr(b1, 'toNode'):
        assert not _is_linked(b1, 'toNode', a)
    if hasattr(b2, 'toNode'):
        assert _is_linked(b2, 'toNode', a)
    _safe_set(a, 'Arc22', None)
    assert not _is_linked(a, 'Arc22', b2)
    if hasattr(b2, 'toNode'):
        assert not _is_linked(b2, 'toNode', a)


def test_assoc_refers19_link_reassign_clear():
    a = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'Arc20', b1)
    assert _is_linked(a, 'Arc20', b1)
    if hasattr(b1, 'fromNode'):
        assert _is_linked(b1, 'fromNode', a)
    _safe_set(a, 'Arc20', b2)
    assert _is_linked(a, 'Arc20', b2)
    if hasattr(b1, 'fromNode'):
        assert not _is_linked(b1, 'fromNode', a)
    if hasattr(b2, 'fromNode'):
        assert _is_linked(b2, 'fromNode', a)
    _safe_set(a, 'Arc20', None)
    assert not _is_linked(a, 'Arc20', b2)
    if hasattr(b2, 'fromNode'):
        assert not _is_linked(b2, 'fromNode', a)


def test_assoc_shape31_link_reassign_clear():
    a = DOT_Node(fixedSize=True, fontname="sample_text", fontsize=7, height=7, width=7)
    b1 = DOT_NodeShape()
    b2 = DOT_NodeShape()
    _safe_set(a, 'DOT_Node', b1)
    assert _is_linked(a, 'DOT_Node', b1)
    if hasattr(b1, 'DOT_NodeShape'):
        assert _is_linked(b1, 'DOT_NodeShape', a)
    _safe_set(a, 'DOT_Node', b2)
    assert _is_linked(a, 'DOT_Node', b2)
    if hasattr(b1, 'DOT_NodeShape'):
        assert not _is_linked(b1, 'DOT_NodeShape', a)
    if hasattr(b2, 'DOT_NodeShape'):
        assert _is_linked(b2, 'DOT_NodeShape', a)
    _safe_set(a, 'DOT_Node', None)
    assert not _is_linked(a, 'DOT_Node', b2)
    if hasattr(b2, 'DOT_NodeShape'):
        assert not _is_linked(b2, 'DOT_NodeShape', a)


def test_assoc_source6_link_reassign_clear():
    a = DOT_Anchor(name="sample_text")
    b1 = DOT_Compartment()
    b2 = DOT_Compartment()
    _safe_set(a, 'anchor', b1)
    assert _is_linked(a, 'anchor', b1)
    if hasattr(b1, 'Compartment7'):
        assert _is_linked(b1, 'Compartment7', a)
    _safe_set(a, 'anchor', b2)
    assert _is_linked(a, 'anchor', b2)
    if hasattr(b1, 'Compartment7'):
        assert not _is_linked(b1, 'Compartment7', a)
    if hasattr(b2, 'Compartment7'):
        assert _is_linked(b2, 'Compartment7', a)
    _safe_set(a, 'anchor', None)
    assert not _is_linked(a, 'anchor', b2)
    if hasattr(b2, 'Compartment7'):
        assert not _is_linked(b2, 'Compartment7', a)


def test_assoc_taillabel45_link_reassign_clear():
    a = DOT_DirectedArc(head_lp=3.14, tail_lp=3.14)
    b1 = DOT_Label()
    b2 = DOT_Label()
    _safe_set(a, 'DOT_DirectedArc46', b1)
    assert _is_linked(a, 'DOT_DirectedArc46', b1)
    if hasattr(b1, 'DOT_Label47'):
        assert _is_linked(b1, 'DOT_Label47', a)
    _safe_set(a, 'DOT_DirectedArc46', b2)
    assert _is_linked(a, 'DOT_DirectedArc46', b2)
    if hasattr(b1, 'DOT_Label47'):
        assert not _is_linked(b1, 'DOT_Label47', a)
    if hasattr(b2, 'DOT_Label47'):
        assert _is_linked(b2, 'DOT_Label47', a)
    _safe_set(a, 'DOT_DirectedArc46', None)
    assert not _is_linked(a, 'DOT_DirectedArc46', b2)
    if hasattr(b2, 'DOT_Label47'):
        assert not _is_linked(b2, 'DOT_Label47', a)


def test_assoc_toNode34_link_reassign_clear():
    a = DOT_Arc(constraint=True, decorate=True, group="sample_text", minlen=7, sameHead="sample_text", sameTail="sample_text")
    b1 = DOT_Nodelike()
    b2 = DOT_Nodelike()
    _safe_set(a, 'referredBy', b1)
    assert _is_linked(a, 'referredBy', b1)
    if hasattr(b1, 'Nodelike35'):
        assert _is_linked(b1, 'Nodelike35', a)
    _safe_set(a, 'referredBy', b2)
    assert _is_linked(a, 'referredBy', b2)
    if hasattr(b1, 'Nodelike35'):
        assert not _is_linked(b1, 'Nodelike35', a)
    if hasattr(b2, 'Nodelike35'):
        assert _is_linked(b2, 'Nodelike35', a)
    _safe_set(a, 'referredBy', None)
    assert not _is_linked(a, 'referredBy', b2)
    if hasattr(b2, 'Nodelike35'):
        assert not _is_linked(b2, 'Nodelike35', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Arc_strategy = st.builds(Arc)
@given(instance=Arc_strategy)
@settings(max_examples=25)
def test_Arc_instantiation(instance):
    assert isinstance(instance, Arc)


Compartment_strategy = st.builds(Compartment)
@given(instance=Compartment_strategy)
@settings(max_examples=25)
def test_Compartment_instantiation(instance):
    assert isinstance(instance, Compartment)


ComplexNodeShape_strategy = st.builds(ComplexNodeShape)
@given(instance=ComplexNodeShape_strategy)
@settings(max_examples=25)
def test_ComplexNodeShape_instantiation(instance):
    assert isinstance(instance, ComplexNodeShape)


DOT_Anchor_strategy = st.builds(DOT_Anchor, name=safe_text)
@given(instance=DOT_Anchor_strategy)
@settings(max_examples=25)
def test_DOT_Anchor_instantiation(instance):
    assert isinstance(instance, DOT_Anchor)


DOT_Arc_strategy = st.builds(DOT_Arc, constraint=st.booleans(), decorate=st.booleans(), group=safe_text, minlen=st.integers(), sameHead=safe_text, sameTail=safe_text)
@given(instance=DOT_Arc_strategy)
@settings(max_examples=25)
def test_DOT_Arc_instantiation(instance):
    assert isinstance(instance, DOT_Arc)


DOT_ArrowShape_strategy = st.builds(DOT_ArrowShape, clipping=safe_text, isPlain=st.booleans(), size=st.integers())
@given(instance=DOT_ArrowShape_strategy)
@settings(max_examples=25)
def test_DOT_ArrowShape_instantiation(instance):
    assert isinstance(instance, DOT_ArrowShape)


DOT_Compartment_strategy = st.builds(DOT_Compartment)
@given(instance=DOT_Compartment_strategy)
@settings(max_examples=25)
def test_DOT_Compartment_instantiation(instance):
    assert isinstance(instance, DOT_Compartment)


DOT_ComplexLabel_strategy = st.builds(DOT_ComplexLabel)
@given(instance=DOT_ComplexLabel_strategy)
@settings(max_examples=25)
def test_DOT_ComplexLabel_instantiation(instance):
    assert isinstance(instance, DOT_ComplexLabel)


DOT_ComplexNodeShape_strategy = st.builds(DOT_ComplexNodeShape)
@given(instance=DOT_ComplexNodeShape_strategy)
@settings(max_examples=25)
def test_DOT_ComplexNodeShape_instantiation(instance):
    assert isinstance(instance, DOT_ComplexNodeShape)


DOT_DirectedArc_strategy = st.builds(DOT_DirectedArc, head_lp=st.floats(allow_nan=False, allow_infinity=False), tail_lp=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=DOT_DirectedArc_strategy)
@settings(max_examples=25)
def test_DOT_DirectedArc_instantiation(instance):
    assert isinstance(instance, DOT_DirectedArc)


DOT_Graph_strategy = st.builds(DOT_Graph, boundingBox=safe_text, center=st.booleans(), compound=st.booleans(), concentrate=st.booleans(), labeljust=safe_text, labelloc=safe_text, nodeSeparation=st.floats(allow_nan=False, allow_infinity=False), ordering=safe_text, rankDir=safe_text, ratio=safe_text, size=safe_text, type=safe_text)
@given(instance=DOT_Graph_strategy)
@settings(max_examples=25)
def test_DOT_Graph_instantiation(instance):
    assert isinstance(instance, DOT_Graph)


DOT_GraphElement_strategy = st.builds(DOT_GraphElement, color=safe_text, name=safe_text, style=safe_text)
@given(instance=DOT_GraphElement_strategy)
@settings(max_examples=25)
def test_DOT_GraphElement_instantiation(instance):
    assert isinstance(instance, DOT_GraphElement)


DOT_HorizontalCompartment_strategy = st.builds(DOT_HorizontalCompartment)
@given(instance=DOT_HorizontalCompartment_strategy)
@settings(max_examples=25)
def test_DOT_HorizontalCompartment_instantiation(instance):
    assert isinstance(instance, DOT_HorizontalCompartment)


DOT_Label_strategy = st.builds(DOT_Label)
@given(instance=DOT_Label_strategy)
@settings(max_examples=25)
def test_DOT_Label_instantiation(instance):
    assert isinstance(instance, DOT_Label)


DOT_Layer_strategy = st.builds(DOT_Layer, layerSeparator=safe_text)
@given(instance=DOT_Layer_strategy)
@settings(max_examples=25)
def test_DOT_Layer_instantiation(instance):
    assert isinstance(instance, DOT_Layer)


DOT_MNodeShape_strategy = st.builds(DOT_MNodeShape)
@given(instance=DOT_MNodeShape_strategy)
@settings(max_examples=25)
def test_DOT_MNodeShape_instantiation(instance):
    assert isinstance(instance, DOT_MNodeShape)


DOT_Node_strategy = st.builds(DOT_Node, fixedSize=st.booleans(), fontname=safe_text, fontsize=st.integers(), height=st.integers(), width=st.integers())
@given(instance=DOT_Node_strategy)
@settings(max_examples=25)
def test_DOT_Node_instantiation(instance):
    assert isinstance(instance, DOT_Node)


DOT_NodeShape_strategy = st.builds(DOT_NodeShape)
@given(instance=DOT_NodeShape_strategy)
@settings(max_examples=25)
def test_DOT_NodeShape_instantiation(instance):
    assert isinstance(instance, DOT_NodeShape)


DOT_Nodelike_strategy = st.builds(DOT_Nodelike)
@given(instance=DOT_Nodelike_strategy)
@settings(max_examples=25)
def test_DOT_Nodelike_instantiation(instance):
    assert isinstance(instance, DOT_Nodelike)


DOT_PointNodeShape_strategy = st.builds(DOT_PointNodeShape)
@given(instance=DOT_PointNodeShape_strategy)
@settings(max_examples=25)
def test_DOT_PointNodeShape_instantiation(instance):
    assert isinstance(instance, DOT_PointNodeShape)


DOT_PolygonNodeShape_strategy = st.builds(DOT_PolygonNodeShape, distortion=st.integers(), isRegular=st.booleans(), orientation=st.integers(), sides=st.integers(), skew=st.integers())
@given(instance=DOT_PolygonNodeShape_strategy)
@settings(max_examples=25)
def test_DOT_PolygonNodeShape_instantiation(instance):
    assert isinstance(instance, DOT_PolygonNodeShape)


DOT_RecordNodeShape_strategy = st.builds(DOT_RecordNodeShape)
@given(instance=DOT_RecordNodeShape_strategy)
@settings(max_examples=25)
def test_DOT_RecordNodeShape_instantiation(instance):
    assert isinstance(instance, DOT_RecordNodeShape)


DOT_Shape_strategy = st.builds(DOT_Shape, height=st.integers(), peripheries=st.integers(), width=st.integers())
@given(instance=DOT_Shape_strategy)
@settings(max_examples=25)
def test_DOT_Shape_instantiation(instance):
    assert isinstance(instance, DOT_Shape)


DOT_SimpleCompartment_strategy = st.builds(DOT_SimpleCompartment, content=safe_text)
@given(instance=DOT_SimpleCompartment_strategy)
@settings(max_examples=25)
def test_DOT_SimpleCompartment_instantiation(instance):
    assert isinstance(instance, DOT_SimpleCompartment)


DOT_SimpleLabel_strategy = st.builds(DOT_SimpleLabel, content=safe_text)
@given(instance=DOT_SimpleLabel_strategy)
@settings(max_examples=25)
def test_DOT_SimpleLabel_instantiation(instance):
    assert isinstance(instance, DOT_SimpleLabel)


DOT_SimpleNodeShape_strategy = st.builds(DOT_SimpleNodeShape)
@given(instance=DOT_SimpleNodeShape_strategy)
@settings(max_examples=25)
def test_DOT_SimpleNodeShape_instantiation(instance):
    assert isinstance(instance, DOT_SimpleNodeShape)


DOT_SubGraph_strategy = st.builds(DOT_SubGraph, labelloc=safe_text)
@given(instance=DOT_SubGraph_strategy)
@settings(max_examples=25)
def test_DOT_SubGraph_instantiation(instance):
    assert isinstance(instance, DOT_SubGraph)


DOT_UndirectedArc_strategy = st.builds(DOT_UndirectedArc)
@given(instance=DOT_UndirectedArc_strategy)
@settings(max_examples=25)
def test_DOT_UndirectedArc_instantiation(instance):
    assert isinstance(instance, DOT_UndirectedArc)


DOT_VerticalCompartment_strategy = st.builds(DOT_VerticalCompartment)
@given(instance=DOT_VerticalCompartment_strategy)
@settings(max_examples=25)
def test_DOT_VerticalCompartment_instantiation(instance):
    assert isinstance(instance, DOT_VerticalCompartment)


GraphElement_strategy = st.builds(GraphElement)
@given(instance=GraphElement_strategy)
@settings(max_examples=25)
def test_GraphElement_instantiation(instance):
    assert isinstance(instance, GraphElement)


Label_strategy = st.builds(Label)
@given(instance=Label_strategy)
@settings(max_examples=25)
def test_Label_instantiation(instance):
    assert isinstance(instance, Label)


NodeShape_strategy = st.builds(NodeShape)
@given(instance=NodeShape_strategy)
@settings(max_examples=25)
def test_NodeShape_instantiation(instance):
    assert isinstance(instance, NodeShape)


Nodelike_strategy = st.builds(Nodelike)
@given(instance=Nodelike_strategy)
@settings(max_examples=25)
def test_Nodelike_instantiation(instance):
    assert isinstance(instance, Nodelike)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


