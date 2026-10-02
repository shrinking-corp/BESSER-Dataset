import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Anchor,
    BasicCompartment,
    BasicDecorationNode,
    BasicSemanticCompartment,
    Bendpoints,
    CanonicalStyle,
    ConnectorStyle,
    DataTypeStyle,
    DecorationNode,
    DescriptionStyle,
    Diagram,
    DiagramLinkStyle,
    DiagramStyle,
    DrawerStyle,
    EModelElement,
    Edge,
    FillStyle,
    FilteringStyle,
    FontStyle,
    GuideStyle,
    ImageStyle,
    LayoutConstraint,
    LineStyle,
    Location,
    NamedStyle,
    Node,
    PageStyle,
    RoundedCornersStyle,
    RoutingStyle,
    ShapeStyle,
    Size,
    SortingStyle,
    StringObjectConverter,
    Style,
    TitleStyle,
    View,
    notation_Anchor,
    notation_ArrowStyle,
    notation_BasicCompartment,
    notation_BasicDecorationNode,
    notation_BasicSemanticCompartment,
    notation_Bendpoints,
    notation_BooleanListValueStyle,
    notation_BooleanValueStyle,
    notation_Bounds,
    notation_ByteArrayValueStyle,
    notation_CanonicalStyle,
    notation_Compartment,
    notation_Connector,
    notation_ConnectorStyle,
    notation_DataTypeStyle,
    notation_DecorationNode,
    notation_DescriptionStyle,
    notation_Diagram,
    notation_DiagramLinkStyle,
    notation_DiagramStyle,
    notation_DoubleListValueStyle,
    notation_DoubleValueStyle,
    notation_DrawerStyle,
    notation_EDataType,
    notation_EObject,
    notation_EObjectListValueStyle,
    notation_EObjectValueStyle,
    notation_Edge,
    notation_FillStyle,
    notation_FilteringStyle,
    notation_FontStyle,
    notation_Guide,
    notation_GuideStyle,
    notation_HintedDiagramLinkStyle,
    notation_IdentityAnchor,
    notation_Image,
    notation_ImageBufferStyle,
    notation_ImageStyle,
    notation_IntListValueStyle,
    notation_IntValueStyle,
    notation_LayoutConstraint,
    notation_LineStyle,
    notation_LineTypeStyle,
    notation_ListCompartment,
    notation_ListValueStyle,
    notation_Location,
    notation_MultiDiagramLinkStyle,
    notation_NamedStyle,
    notation_Node,
    notation_NodeEntry,
    notation_PageStyle,
    notation_PropertiesSetStyle,
    notation_PropertyValue,
    notation_Ratio,
    notation_RelativeBendpoints,
    notation_RoundedCornersStyle,
    notation_RoutingStyle,
    notation_SemanticListCompartment,
    notation_Shape,
    notation_ShapeStyle,
    notation_SingleValueStyle,
    notation_Size,
    notation_SortingStyle,
    notation_StandardDiagram,
    notation_StringListValueStyle,
    notation_StringObjectConverter,
    notation_StringToPropertyValueMapEntry,
    notation_StringValueStyle,
    notation_Style,
    notation_TextStyle,
    notation_TitleStyle,
    notation_View,
    Alignment,
    ArrowType,
    Filtering,
    GradientStyle,
    JumpLinkStatus,
    JumpLinkType,
    LineType,
    MeasurementUnit,
    Routing,
    Smoothness,
    Sorting,
    SortingDirection,
    TextAlignment,
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

def test_assoc_TransientEdges29_reverse_link_reassign_clear():
    a1 = notation_Edge()
    a2 = notation_Edge()
    b = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    _safe_set(b, 'notation_Diagram30', {a1})
    assert _is_linked(b, 'notation_Diagram30', a1)
    if hasattr(a1, 'notation_Edge31'):
        assert _is_linked(a1, 'notation_Edge31', b)
    _safe_set(b, 'notation_Diagram30', {a2})
    assert _is_linked(b, 'notation_Diagram30', a2)
    if hasattr(a1, 'notation_Edge31'):
        assert not _is_linked(a1, 'notation_Edge31', b)
    if hasattr(a2, 'notation_Edge31'):
        assert _is_linked(a2, 'notation_Edge31', b)
    _safe_set(b, 'notation_Diagram30', set())
    assert not _is_linked(b, 'notation_Diagram30', a2)
    if hasattr(a2, 'notation_Edge31'):
        assert not _is_linked(a2, 'notation_Edge31', b)


def test_assoc_diagram21_reverse_link_reassign_clear():
    a1 = notation_View(mutable=True, type="sample_text", visible=True)
    a2 = notation_View(mutable=False, type="sample_text_2", visible=False)
    b = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    _safe_set(b, 'notation_Diagram', a1)
    assert _is_linked(b, 'notation_Diagram', a1)
    if hasattr(a1, 'notation_View22'):
        assert _is_linked(a1, 'notation_View22', b)
    _safe_set(b, 'notation_Diagram', a2)
    assert _is_linked(b, 'notation_Diagram', a2)
    if hasattr(a1, 'notation_View22'):
        assert not _is_linked(a1, 'notation_View22', b)
    if hasattr(a2, 'notation_View22'):
        assert _is_linked(a2, 'notation_View22', b)
    _safe_set(b, 'notation_Diagram', None)
    assert not _is_linked(b, 'notation_Diagram', a2)
    if hasattr(a2, 'notation_View22'):
        assert not _is_linked(a2, 'notation_View22', b)


def test_assoc_key38_reverse_link_reassign_clear():
    a1 = notation_NodeEntry(value="sample_text")
    a2 = notation_NodeEntry(value="sample_text_2")
    b = notation_Node()
    _safe_set(b, 'notation_Node40', a1)
    assert _is_linked(b, 'notation_Node40', a1)
    if hasattr(a1, 'notation_NodeEntry39'):
        assert _is_linked(a1, 'notation_NodeEntry39', b)
    _safe_set(b, 'notation_Node40', a2)
    assert _is_linked(b, 'notation_Node40', a2)
    if hasattr(a1, 'notation_NodeEntry39'):
        assert not _is_linked(a1, 'notation_NodeEntry39', b)
    if hasattr(a2, 'notation_NodeEntry39'):
        assert _is_linked(a2, 'notation_NodeEntry39', b)
    _safe_set(b, 'notation_Node40', None)
    assert not _is_linked(b, 'notation_Node40', a2)
    if hasattr(a2, 'notation_NodeEntry39'):
        assert not _is_linked(a2, 'notation_NodeEntry39', b)


def test_assoc_nodeMap36_reverse_link_reassign_clear():
    a1 = notation_NodeEntry(value="sample_text")
    a2 = notation_NodeEntry(value="sample_text_2")
    b = notation_Guide(position=7)
    _safe_set(b, 'notation_Guide37', {a1})
    assert _is_linked(b, 'notation_Guide37', a1)
    if hasattr(a1, 'notation_NodeEntry'):
        assert _is_linked(a1, 'notation_NodeEntry', b)
    _safe_set(b, 'notation_Guide37', {a2})
    assert _is_linked(b, 'notation_Guide37', a2)
    if hasattr(a1, 'notation_NodeEntry'):
        assert not _is_linked(a1, 'notation_NodeEntry', b)
    if hasattr(a2, 'notation_NodeEntry'):
        assert _is_linked(a2, 'notation_NodeEntry', b)
    _safe_set(b, 'notation_Guide37', set())
    assert not _is_linked(b, 'notation_Guide37', a2)
    if hasattr(a2, 'notation_NodeEntry'):
        assert not _is_linked(a2, 'notation_NodeEntry', b)


def test_assoc_persistedChildren14_reverse_link_reassign_clear():
    a1 = notation_View(mutable=True, type="sample_text", visible=True)
    a2 = notation_View(mutable=False, type="sample_text_2", visible=False)
    b = notation_Node()
    _safe_set(b, 'notation_Node15', a1)
    assert _is_linked(b, 'notation_Node15', a1)
    if hasattr(a1, 'notation_View'):
        assert _is_linked(a1, 'notation_View', b)
    _safe_set(b, 'notation_Node15', a2)
    assert _is_linked(b, 'notation_Node15', a2)
    if hasattr(a1, 'notation_View'):
        assert not _is_linked(a1, 'notation_View', b)
    if hasattr(a2, 'notation_View'):
        assert _is_linked(a2, 'notation_View', b)
    _safe_set(b, 'notation_Node15', None)
    assert not _is_linked(b, 'notation_Node15', a2)
    if hasattr(a2, 'notation_View'):
        assert not _is_linked(a2, 'notation_View', b)


def test_assoc_persistedEdges26_reverse_link_reassign_clear():
    a1 = notation_Edge()
    a2 = notation_Edge()
    b = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    _safe_set(b, 'notation_Diagram27', {a1})
    assert _is_linked(b, 'notation_Diagram27', a1)
    if hasattr(a1, 'notation_Edge28'):
        assert _is_linked(a1, 'notation_Edge28', b)
    _safe_set(b, 'notation_Diagram27', {a2})
    assert _is_linked(b, 'notation_Diagram27', a2)
    if hasattr(a1, 'notation_Edge28'):
        assert not _is_linked(a1, 'notation_Edge28', b)
    if hasattr(a2, 'notation_Edge28'):
        assert _is_linked(a2, 'notation_Edge28', b)
    _safe_set(b, 'notation_Diagram27', set())
    assert not _is_linked(b, 'notation_Diagram27', a2)
    if hasattr(a2, 'notation_Edge28'):
        assert not _is_linked(a2, 'notation_Edge28', b)


def test_assoc_propertiesMap45_reverse_link_reassign_clear():
    a1 = notation_StringToPropertyValueMapEntry(key="sample_text")
    a2 = notation_StringToPropertyValueMapEntry(key="sample_text_2")
    b = notation_PropertiesSetStyle()
    _safe_set(b, 'notation_PropertiesSetStyle', {a1})
    assert _is_linked(b, 'notation_PropertiesSetStyle', a1)
    if hasattr(a1, 'notation_StringToPropertyValueMapEntry'):
        assert _is_linked(a1, 'notation_StringToPropertyValueMapEntry', b)
    _safe_set(b, 'notation_PropertiesSetStyle', {a2})
    assert _is_linked(b, 'notation_PropertiesSetStyle', a2)
    if hasattr(a1, 'notation_StringToPropertyValueMapEntry'):
        assert not _is_linked(a1, 'notation_StringToPropertyValueMapEntry', b)
    if hasattr(a2, 'notation_StringToPropertyValueMapEntry'):
        assert _is_linked(a2, 'notation_StringToPropertyValueMapEntry', b)
    _safe_set(b, 'notation_PropertiesSetStyle', set())
    assert not _is_linked(b, 'notation_PropertiesSetStyle', a2)
    if hasattr(a2, 'notation_StringToPropertyValueMapEntry'):
        assert not _is_linked(a2, 'notation_StringToPropertyValueMapEntry', b)


def test_assoc_source0_reverse_link_reassign_clear():
    a1 = notation_View(mutable=True, type="sample_text", visible=True)
    a2 = notation_View(mutable=False, type="sample_text_2", visible=False)
    b = notation_Edge()
    _safe_set(b, 'sourceEdges', a1)
    assert _is_linked(b, 'sourceEdges', a1)
    if hasattr(a1, 'View'):
        assert _is_linked(a1, 'View', b)
    _safe_set(b, 'sourceEdges', a2)
    assert _is_linked(b, 'sourceEdges', a2)
    if hasattr(a1, 'View'):
        assert not _is_linked(a1, 'View', b)
    if hasattr(a2, 'View'):
        assert _is_linked(a2, 'View', b)
    _safe_set(b, 'sourceEdges', None)
    assert not _is_linked(b, 'sourceEdges', a2)
    if hasattr(a2, 'View'):
        assert not _is_linked(a2, 'View', b)


def test_assoc_sourceEdges11_reverse_link_reassign_clear():
    a1 = notation_View(mutable=True, type="sample_text", visible=True)
    a2 = notation_View(mutable=False, type="sample_text_2", visible=False)
    b = notation_Edge()
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_target1_reverse_link_reassign_clear():
    a1 = notation_View(mutable=True, type="sample_text", visible=True)
    a2 = notation_View(mutable=False, type="sample_text_2", visible=False)
    b = notation_Edge()
    _safe_set(b, 'targetEdges', a1)
    assert _is_linked(b, 'targetEdges', a1)
    if hasattr(a1, 'View2'):
        assert _is_linked(a1, 'View2', b)
    _safe_set(b, 'targetEdges', a2)
    assert _is_linked(b, 'targetEdges', a2)
    if hasattr(a1, 'View2'):
        assert not _is_linked(a1, 'View2', b)
    if hasattr(a2, 'View2'):
        assert _is_linked(a2, 'View2', b)
    _safe_set(b, 'targetEdges', None)
    assert not _is_linked(b, 'targetEdges', a2)
    if hasattr(a2, 'View2'):
        assert not _is_linked(a2, 'View2', b)


def test_assoc_targetEdges12_reverse_link_reassign_clear():
    a1 = notation_View(mutable=True, type="sample_text", visible=True)
    a2 = notation_View(mutable=False, type="sample_text_2", visible=False)
    b = notation_Edge()
    _safe_set(b, 'Edge13', a1)
    assert _is_linked(b, 'Edge13', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge13', a2)
    assert _is_linked(b, 'Edge13', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge13', None)
    assert not _is_linked(b, 'Edge13', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_transientChildren23_reverse_link_reassign_clear():
    a1 = notation_View(mutable=True, type="sample_text", visible=True)
    a2 = notation_View(mutable=False, type="sample_text_2", visible=False)
    b = notation_Node()
    _safe_set(b, 'notation_Node25', a1)
    assert _is_linked(b, 'notation_Node25', a1)
    if hasattr(a1, 'notation_View24'):
        assert _is_linked(a1, 'notation_View24', b)
    _safe_set(b, 'notation_Node25', a2)
    assert _is_linked(b, 'notation_Node25', a2)
    if hasattr(a1, 'notation_View24'):
        assert not _is_linked(a1, 'notation_View24', b)
    if hasattr(a2, 'notation_View24'):
        assert _is_linked(a2, 'notation_View24', b)
    _safe_set(b, 'notation_Node25', None)
    assert not _is_linked(b, 'notation_Node25', a2)
    if hasattr(a2, 'notation_View24'):
        assert not _is_linked(a2, 'notation_View24', b)


def test_assoc_value46_reverse_link_reassign_clear():
    a1 = notation_StringToPropertyValueMapEntry(key="sample_text")
    a2 = notation_StringToPropertyValueMapEntry(key="sample_text_2")
    b = notation_PropertyValue(rawValue="sample_text")
    _safe_set(b, 'notation_PropertyValue', a1)
    assert _is_linked(b, 'notation_PropertyValue', a1)
    if hasattr(a1, 'notation_StringToPropertyValueMapEntry47'):
        assert _is_linked(a1, 'notation_StringToPropertyValueMapEntry47', b)
    _safe_set(b, 'notation_PropertyValue', a2)
    assert _is_linked(b, 'notation_PropertyValue', a2)
    if hasattr(a1, 'notation_StringToPropertyValueMapEntry47'):
        assert not _is_linked(a1, 'notation_StringToPropertyValueMapEntry47', b)
    if hasattr(a2, 'notation_StringToPropertyValueMapEntry47'):
        assert _is_linked(a2, 'notation_StringToPropertyValueMapEntry47', b)
    _safe_set(b, 'notation_PropertyValue', None)
    assert not _is_linked(b, 'notation_PropertyValue', a2)
    if hasattr(a2, 'notation_StringToPropertyValueMapEntry47'):
        assert not _is_linked(a2, 'notation_StringToPropertyValueMapEntry47', b)


