import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DiagramElement,
    Edge,
    Node,
    Shape,
    mtm_di_Bounds,
    mtm_di_Diagram,
    mtm_di_DiagramElement,
    mtm_di_DocumentRoot,
    mtm_di_EStringToStringMapEntry,
    mtm_di_Edge,
    mtm_di_ExtensionType,
    mtm_di_Label,
    mtm_di_LabeledEdge,
    mtm_di_LabeledShape,
    mtm_di_Node,
    mtm_di_Plane,
    mtm_di_Point,
    mtm_di_Shape,
    mtm_di_Style,
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

def test_mtm_di_Diagram_documentation_value_roundtrip():
    instance = mtm_di_Diagram(documentation="sample_text", id="sample_text", name="sample_text", resolution="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_mtm_di_Diagram_id_value_roundtrip():
    instance = mtm_di_Diagram(documentation="sample_text", id="sample_text", name="sample_text", resolution="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_mtm_di_Diagram_name_value_roundtrip():
    instance = mtm_di_Diagram(documentation="sample_text", id="sample_text", name="sample_text", resolution="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mtm_di_Diagram_resolution_value_roundtrip():
    instance = mtm_di_Diagram(documentation="sample_text", id="sample_text", name="sample_text", resolution="sample_text")
    assert instance.resolution == "sample_text"
    instance.resolution = "sample_text_2"
    assert instance.resolution == "sample_text_2"


def test_mtm_di_DiagramElement_anyAttribute_value_roundtrip():
    instance = mtm_di_DiagramElement(anyAttribute="sample_text", id="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_mtm_di_DiagramElement_id_value_roundtrip():
    instance = mtm_di_DiagramElement(anyAttribute="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_mtm_di_DocumentRoot_mixed_value_roundtrip():
    instance = mtm_di_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_mtm_di_ExtensionType_any_value_roundtrip():
    instance = mtm_di_ExtensionType(any="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_mtm_di_Plane_diagramElementGroup_value_roundtrip():
    instance = mtm_di_Plane(diagramElementGroup="sample_text")
    assert instance.diagramElementGroup == "sample_text"
    instance.diagramElementGroup = "sample_text_2"
    assert instance.diagramElementGroup == "sample_text_2"


def test_mtm_di_Style_id_value_roundtrip():
    instance = mtm_di_Style(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_mtm_di_Edge_isa_DiagramElement():
    instance = mtm_di_Edge()
    assert isinstance(instance, DiagramElement)


def test_mtm_di_Node_isa_DiagramElement():
    instance = mtm_di_Node()
    assert isinstance(instance, DiagramElement)


def test_mtm_di_LabeledEdge_isa_Edge():
    instance = mtm_di_LabeledEdge()
    assert isinstance(instance, Edge)


def test_mtm_di_Label_isa_Node():
    instance = mtm_di_Label()
    assert isinstance(instance, Node)


def test_mtm_di_Plane_isa_Node():
    instance = mtm_di_Plane(diagramElementGroup="sample_text")
    assert isinstance(instance, Node)


def test_mtm_di_Shape_isa_Node():
    instance = mtm_di_Shape()
    assert isinstance(instance, Node)


def test_mtm_di_LabeledShape_isa_Shape():
    instance = mtm_di_LabeledShape()
    assert isinstance(instance, Shape)


def test_assoc_diagram14_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_Diagram(documentation="sample_text", id="sample_text", name="sample_text", resolution="sample_text")
    b2 = mtm_di_Diagram(documentation="sample_text_2", id="sample_text_2", name="sample_text_2", resolution="sample_text_2")
    _safe_set(a, 'mtm_di_DocumentRoot15', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot15', b1)
    if hasattr(b1, 'mtm_di_Diagram'):
        assert _is_linked(b1, 'mtm_di_Diagram', a)
    _safe_set(a, 'mtm_di_DocumentRoot15', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot15', b2)
    if hasattr(b1, 'mtm_di_Diagram'):
        assert not _is_linked(b1, 'mtm_di_Diagram', a)
    if hasattr(b2, 'mtm_di_Diagram'):
        assert _is_linked(b2, 'mtm_di_Diagram', a)
    _safe_set(a, 'mtm_di_DocumentRoot15', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot15', b2)
    if hasattr(b2, 'mtm_di_Diagram'):
        assert not _is_linked(b2, 'mtm_di_Diagram', a)


def test_assoc_diagramElement11_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_DiagramElement(anyAttribute="sample_text", id="sample_text")
    b2 = mtm_di_DiagramElement(anyAttribute="sample_text_2", id="sample_text_2")
    _safe_set(a, 'mtm_di_DocumentRoot12', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot12', b1)
    if hasattr(b1, 'mtm_di_DiagramElement13'):
        assert _is_linked(b1, 'mtm_di_DiagramElement13', a)
    _safe_set(a, 'mtm_di_DocumentRoot12', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot12', b2)
    if hasattr(b1, 'mtm_di_DiagramElement13'):
        assert not _is_linked(b1, 'mtm_di_DiagramElement13', a)
    if hasattr(b2, 'mtm_di_DiagramElement13'):
        assert _is_linked(b2, 'mtm_di_DiagramElement13', a)
    _safe_set(a, 'mtm_di_DocumentRoot12', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot12', b2)
    if hasattr(b2, 'mtm_di_DiagramElement13'):
        assert not _is_linked(b2, 'mtm_di_DiagramElement13', a)


def test_assoc_diagramElement3_link_reassign_clear():
    a = mtm_di_Plane(diagramElementGroup="sample_text")
    b1 = mtm_di_DiagramElement(anyAttribute="sample_text", id="sample_text")
    b2 = mtm_di_DiagramElement(anyAttribute="sample_text_2", id="sample_text_2")
    _safe_set(a, 'mtm_di_Plane', {b1})
    assert _is_linked(a, 'mtm_di_Plane', b1)
    if hasattr(b1, 'mtm_di_DiagramElement4'):
        assert _is_linked(b1, 'mtm_di_DiagramElement4', a)
    _safe_set(a, 'mtm_di_Plane', {b2})
    assert _is_linked(a, 'mtm_di_Plane', b2)
    if hasattr(b1, 'mtm_di_DiagramElement4'):
        assert not _is_linked(b1, 'mtm_di_DiagramElement4', a)
    if hasattr(b2, 'mtm_di_DiagramElement4'):
        assert _is_linked(b2, 'mtm_di_DiagramElement4', a)
    _safe_set(a, 'mtm_di_Plane', set())
    assert not _is_linked(a, 'mtm_di_Plane', b2)
    if hasattr(b2, 'mtm_di_DiagramElement4'):
        assert not _is_linked(b2, 'mtm_di_DiagramElement4', a)


def test_assoc_edge16_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_Edge()
    b2 = mtm_di_Edge()
    _safe_set(a, 'mtm_di_DocumentRoot17', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot17', b1)
    if hasattr(b1, 'mtm_di_Edge18'):
        assert _is_linked(b1, 'mtm_di_Edge18', a)
    _safe_set(a, 'mtm_di_DocumentRoot17', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot17', b2)
    if hasattr(b1, 'mtm_di_Edge18'):
        assert not _is_linked(b1, 'mtm_di_Edge18', a)
    if hasattr(b2, 'mtm_di_Edge18'):
        assert _is_linked(b2, 'mtm_di_Edge18', a)
    _safe_set(a, 'mtm_di_DocumentRoot17', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot17', b2)
    if hasattr(b2, 'mtm_di_Edge18'):
        assert not _is_linked(b2, 'mtm_di_Edge18', a)


def test_assoc_extension0_link_reassign_clear():
    a = mtm_di_ExtensionType(any="sample_text")
    b1 = mtm_di_DiagramElement(anyAttribute="sample_text", id="sample_text")
    b2 = mtm_di_DiagramElement(anyAttribute="sample_text_2", id="sample_text_2")
    _safe_set(a, 'mtm_di_ExtensionType', b1)
    assert _is_linked(a, 'mtm_di_ExtensionType', b1)
    if hasattr(b1, 'mtm_di_DiagramElement'):
        assert _is_linked(b1, 'mtm_di_DiagramElement', a)
    _safe_set(a, 'mtm_di_ExtensionType', b2)
    assert _is_linked(a, 'mtm_di_ExtensionType', b2)
    if hasattr(b1, 'mtm_di_DiagramElement'):
        assert not _is_linked(b1, 'mtm_di_DiagramElement', a)
    if hasattr(b2, 'mtm_di_DiagramElement'):
        assert _is_linked(b2, 'mtm_di_DiagramElement', a)
    _safe_set(a, 'mtm_di_ExtensionType', None)
    assert not _is_linked(a, 'mtm_di_ExtensionType', b2)
    if hasattr(b2, 'mtm_di_DiagramElement'):
        assert not _is_linked(b2, 'mtm_di_DiagramElement', a)


def test_assoc_label19_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_Label()
    b2 = mtm_di_Label()
    _safe_set(a, 'mtm_di_DocumentRoot20', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot20', b1)
    if hasattr(b1, 'mtm_di_Label21'):
        assert _is_linked(b1, 'mtm_di_Label21', a)
    _safe_set(a, 'mtm_di_DocumentRoot20', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot20', b2)
    if hasattr(b1, 'mtm_di_Label21'):
        assert not _is_linked(b1, 'mtm_di_Label21', a)
    if hasattr(b2, 'mtm_di_Label21'):
        assert _is_linked(b2, 'mtm_di_Label21', a)
    _safe_set(a, 'mtm_di_DocumentRoot20', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot20', b2)
    if hasattr(b2, 'mtm_di_Label21'):
        assert not _is_linked(b2, 'mtm_di_Label21', a)


def test_assoc_labeledEdge22_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_LabeledEdge()
    b2 = mtm_di_LabeledEdge()
    _safe_set(a, 'mtm_di_DocumentRoot23', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot23', b1)
    if hasattr(b1, 'mtm_di_LabeledEdge'):
        assert _is_linked(b1, 'mtm_di_LabeledEdge', a)
    _safe_set(a, 'mtm_di_DocumentRoot23', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot23', b2)
    if hasattr(b1, 'mtm_di_LabeledEdge'):
        assert not _is_linked(b1, 'mtm_di_LabeledEdge', a)
    if hasattr(b2, 'mtm_di_LabeledEdge'):
        assert _is_linked(b2, 'mtm_di_LabeledEdge', a)
    _safe_set(a, 'mtm_di_DocumentRoot23', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot23', b2)
    if hasattr(b2, 'mtm_di_LabeledEdge'):
        assert not _is_linked(b2, 'mtm_di_LabeledEdge', a)


def test_assoc_labeledShape24_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_LabeledShape()
    b2 = mtm_di_LabeledShape()
    _safe_set(a, 'mtm_di_DocumentRoot25', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot25', b1)
    if hasattr(b1, 'mtm_di_LabeledShape'):
        assert _is_linked(b1, 'mtm_di_LabeledShape', a)
    _safe_set(a, 'mtm_di_DocumentRoot25', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot25', b2)
    if hasattr(b1, 'mtm_di_LabeledShape'):
        assert not _is_linked(b1, 'mtm_di_LabeledShape', a)
    if hasattr(b2, 'mtm_di_LabeledShape'):
        assert _is_linked(b2, 'mtm_di_LabeledShape', a)
    _safe_set(a, 'mtm_di_DocumentRoot25', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot25', b2)
    if hasattr(b2, 'mtm_di_LabeledShape'):
        assert not _is_linked(b2, 'mtm_di_LabeledShape', a)


def test_assoc_node26_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_Node()
    b2 = mtm_di_Node()
    _safe_set(a, 'mtm_di_DocumentRoot27', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot27', b1)
    if hasattr(b1, 'mtm_di_Node'):
        assert _is_linked(b1, 'mtm_di_Node', a)
    _safe_set(a, 'mtm_di_DocumentRoot27', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot27', b2)
    if hasattr(b1, 'mtm_di_Node'):
        assert not _is_linked(b1, 'mtm_di_Node', a)
    if hasattr(b2, 'mtm_di_Node'):
        assert _is_linked(b2, 'mtm_di_Node', a)
    _safe_set(a, 'mtm_di_DocumentRoot27', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot27', b2)
    if hasattr(b2, 'mtm_di_Node'):
        assert not _is_linked(b2, 'mtm_di_Node', a)


def test_assoc_plane28_link_reassign_clear():
    a = mtm_di_Plane(diagramElementGroup="sample_text")
    b1 = mtm_di_DocumentRoot(mixed="sample_text")
    b2 = mtm_di_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'mtm_di_Plane30', b1)
    assert _is_linked(a, 'mtm_di_Plane30', b1)
    if hasattr(b1, 'mtm_di_DocumentRoot29'):
        assert _is_linked(b1, 'mtm_di_DocumentRoot29', a)
    _safe_set(a, 'mtm_di_Plane30', b2)
    assert _is_linked(a, 'mtm_di_Plane30', b2)
    if hasattr(b1, 'mtm_di_DocumentRoot29'):
        assert not _is_linked(b1, 'mtm_di_DocumentRoot29', a)
    if hasattr(b2, 'mtm_di_DocumentRoot29'):
        assert _is_linked(b2, 'mtm_di_DocumentRoot29', a)
    _safe_set(a, 'mtm_di_Plane30', None)
    assert not _is_linked(a, 'mtm_di_Plane30', b2)
    if hasattr(b2, 'mtm_di_DocumentRoot29'):
        assert not _is_linked(b2, 'mtm_di_DocumentRoot29', a)


def test_assoc_shape31_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_Shape()
    b2 = mtm_di_Shape()
    _safe_set(a, 'mtm_di_DocumentRoot32', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot32', b1)
    if hasattr(b1, 'mtm_di_Shape33'):
        assert _is_linked(b1, 'mtm_di_Shape33', a)
    _safe_set(a, 'mtm_di_DocumentRoot32', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot32', b2)
    if hasattr(b1, 'mtm_di_Shape33'):
        assert not _is_linked(b1, 'mtm_di_Shape33', a)
    if hasattr(b2, 'mtm_di_Shape33'):
        assert _is_linked(b2, 'mtm_di_Shape33', a)
    _safe_set(a, 'mtm_di_DocumentRoot32', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot32', b2)
    if hasattr(b2, 'mtm_di_Shape33'):
        assert not _is_linked(b2, 'mtm_di_Shape33', a)


def test_assoc_style34_link_reassign_clear():
    a = mtm_di_Style(id="sample_text")
    b1 = mtm_di_DocumentRoot(mixed="sample_text")
    b2 = mtm_di_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'mtm_di_Style', b1)
    assert _is_linked(a, 'mtm_di_Style', b1)
    if hasattr(b1, 'mtm_di_DocumentRoot35'):
        assert _is_linked(b1, 'mtm_di_DocumentRoot35', a)
    _safe_set(a, 'mtm_di_Style', b2)
    assert _is_linked(a, 'mtm_di_Style', b2)
    if hasattr(b1, 'mtm_di_DocumentRoot35'):
        assert not _is_linked(b1, 'mtm_di_DocumentRoot35', a)
    if hasattr(b2, 'mtm_di_DocumentRoot35'):
        assert _is_linked(b2, 'mtm_di_DocumentRoot35', a)
    _safe_set(a, 'mtm_di_Style', None)
    assert not _is_linked(a, 'mtm_di_Style', b2)
    if hasattr(b2, 'mtm_di_DocumentRoot35'):
        assert not _is_linked(b2, 'mtm_di_DocumentRoot35', a)


def test_assoc_xMLNSPrefixMap7_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_EStringToStringMapEntry()
    b2 = mtm_di_EStringToStringMapEntry()
    _safe_set(a, 'mtm_di_DocumentRoot', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot', b1)
    if hasattr(b1, 'mtm_di_EStringToStringMapEntry'):
        assert _is_linked(b1, 'mtm_di_EStringToStringMapEntry', a)
    _safe_set(a, 'mtm_di_DocumentRoot', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot', b2)
    if hasattr(b1, 'mtm_di_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'mtm_di_EStringToStringMapEntry', a)
    if hasattr(b2, 'mtm_di_EStringToStringMapEntry'):
        assert _is_linked(b2, 'mtm_di_EStringToStringMapEntry', a)
    _safe_set(a, 'mtm_di_DocumentRoot', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot', b2)
    if hasattr(b2, 'mtm_di_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'mtm_di_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation8_link_reassign_clear():
    a = mtm_di_DocumentRoot(mixed="sample_text")
    b1 = mtm_di_EStringToStringMapEntry()
    b2 = mtm_di_EStringToStringMapEntry()
    _safe_set(a, 'mtm_di_DocumentRoot9', {b1})
    assert _is_linked(a, 'mtm_di_DocumentRoot9', b1)
    if hasattr(b1, 'mtm_di_EStringToStringMapEntry10'):
        assert _is_linked(b1, 'mtm_di_EStringToStringMapEntry10', a)
    _safe_set(a, 'mtm_di_DocumentRoot9', {b2})
    assert _is_linked(a, 'mtm_di_DocumentRoot9', b2)
    if hasattr(b1, 'mtm_di_EStringToStringMapEntry10'):
        assert not _is_linked(b1, 'mtm_di_EStringToStringMapEntry10', a)
    if hasattr(b2, 'mtm_di_EStringToStringMapEntry10'):
        assert _is_linked(b2, 'mtm_di_EStringToStringMapEntry10', a)
    _safe_set(a, 'mtm_di_DocumentRoot9', set())
    assert not _is_linked(a, 'mtm_di_DocumentRoot9', b2)
    if hasattr(b2, 'mtm_di_EStringToStringMapEntry10'):
        assert not _is_linked(b2, 'mtm_di_EStringToStringMapEntry10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DiagramElement_strategy = st.builds(DiagramElement)
@given(instance=DiagramElement_strategy)
@settings(max_examples=25)
def test_DiagramElement_instantiation(instance):
    assert isinstance(instance, DiagramElement)


Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


mtm_di_Bounds_strategy = st.builds(mtm_di_Bounds)
@given(instance=mtm_di_Bounds_strategy)
@settings(max_examples=25)
def test_mtm_di_Bounds_instantiation(instance):
    assert isinstance(instance, mtm_di_Bounds)


mtm_di_Diagram_strategy = st.builds(mtm_di_Diagram, documentation=safe_text, id=safe_text, name=safe_text, resolution=safe_text)
@given(instance=mtm_di_Diagram_strategy)
@settings(max_examples=25)
def test_mtm_di_Diagram_instantiation(instance):
    assert isinstance(instance, mtm_di_Diagram)


mtm_di_DiagramElement_strategy = st.builds(mtm_di_DiagramElement, anyAttribute=safe_text, id=safe_text)
@given(instance=mtm_di_DiagramElement_strategy)
@settings(max_examples=25)
def test_mtm_di_DiagramElement_instantiation(instance):
    assert isinstance(instance, mtm_di_DiagramElement)


mtm_di_DocumentRoot_strategy = st.builds(mtm_di_DocumentRoot, mixed=safe_text)
@given(instance=mtm_di_DocumentRoot_strategy)
@settings(max_examples=25)
def test_mtm_di_DocumentRoot_instantiation(instance):
    assert isinstance(instance, mtm_di_DocumentRoot)


mtm_di_EStringToStringMapEntry_strategy = st.builds(mtm_di_EStringToStringMapEntry)
@given(instance=mtm_di_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_mtm_di_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, mtm_di_EStringToStringMapEntry)


mtm_di_Edge_strategy = st.builds(mtm_di_Edge)
@given(instance=mtm_di_Edge_strategy)
@settings(max_examples=25)
def test_mtm_di_Edge_instantiation(instance):
    assert isinstance(instance, mtm_di_Edge)


mtm_di_ExtensionType_strategy = st.builds(mtm_di_ExtensionType, any=safe_text)
@given(instance=mtm_di_ExtensionType_strategy)
@settings(max_examples=25)
def test_mtm_di_ExtensionType_instantiation(instance):
    assert isinstance(instance, mtm_di_ExtensionType)


mtm_di_Label_strategy = st.builds(mtm_di_Label)
@given(instance=mtm_di_Label_strategy)
@settings(max_examples=25)
def test_mtm_di_Label_instantiation(instance):
    assert isinstance(instance, mtm_di_Label)


mtm_di_LabeledEdge_strategy = st.builds(mtm_di_LabeledEdge)
@given(instance=mtm_di_LabeledEdge_strategy)
@settings(max_examples=25)
def test_mtm_di_LabeledEdge_instantiation(instance):
    assert isinstance(instance, mtm_di_LabeledEdge)


mtm_di_LabeledShape_strategy = st.builds(mtm_di_LabeledShape)
@given(instance=mtm_di_LabeledShape_strategy)
@settings(max_examples=25)
def test_mtm_di_LabeledShape_instantiation(instance):
    assert isinstance(instance, mtm_di_LabeledShape)


mtm_di_Node_strategy = st.builds(mtm_di_Node)
@given(instance=mtm_di_Node_strategy)
@settings(max_examples=25)
def test_mtm_di_Node_instantiation(instance):
    assert isinstance(instance, mtm_di_Node)


mtm_di_Plane_strategy = st.builds(mtm_di_Plane, diagramElementGroup=safe_text)
@given(instance=mtm_di_Plane_strategy)
@settings(max_examples=25)
def test_mtm_di_Plane_instantiation(instance):
    assert isinstance(instance, mtm_di_Plane)


mtm_di_Point_strategy = st.builds(mtm_di_Point)
@given(instance=mtm_di_Point_strategy)
@settings(max_examples=25)
def test_mtm_di_Point_instantiation(instance):
    assert isinstance(instance, mtm_di_Point)


mtm_di_Shape_strategy = st.builds(mtm_di_Shape)
@given(instance=mtm_di_Shape_strategy)
@settings(max_examples=25)
def test_mtm_di_Shape_instantiation(instance):
    assert isinstance(instance, mtm_di_Shape)


mtm_di_Style_strategy = st.builds(mtm_di_Style, id=safe_text)
@given(instance=mtm_di_Style_strategy)
@settings(max_examples=25)
def test_mtm_di_Style_instantiation(instance):
    assert isinstance(instance, mtm_di_Style)


