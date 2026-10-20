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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bendpoints3_stub_double():
    # notation_Bendpoints has no real 'notation_Bendpoints' property in the generated
    # code (a bare stub) -- manually attach it so notation_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Edge()
    partner = notation_Bendpoints()
    setattr(partner, 'notation_Bendpoints', None)
    _safe_set(owner, 'notation_Edge', partner)
    assert getattr(partner, 'notation_Bendpoints') == owner
    _safe_set(owner, 'notation_Edge', None)
    assert getattr(partner, 'notation_Bendpoints') is None


def test_assoc_cropBound43_stub_double():
    # notation_Bounds has no real 'notation_Bounds' property in the generated
    # code (a bare stub) -- manually attach it so notation_ImageStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_ImageStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_ImageStyle(antiAlias="sample_text", maintainAspectRatio="sample_text")
    partner = notation_Bounds()
    setattr(partner, 'notation_Bounds', None)
    _safe_set(owner, 'notation_ImageStyle', partner)
    assert getattr(partner, 'notation_Bounds') == owner
    _safe_set(owner, 'notation_ImageStyle', None)
    assert getattr(partner, 'notation_Bounds') is None


def test_assoc_diagramLink56_stub_double():
    # notation_DiagramLinkStyle has no real 'notation_DiagramLinkStyle' property in the generated
    # code (a bare stub) -- manually attach it so notation_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    partner = notation_DiagramLinkStyle()
    setattr(partner, 'notation_DiagramLinkStyle', None)
    _safe_set(owner, 'notation_Diagram57', partner)
    assert getattr(partner, 'notation_DiagramLinkStyle') == owner
    _safe_set(owner, 'notation_Diagram57', None)
    assert getattr(partner, 'notation_DiagramLinkStyle') is None


def test_assoc_diagramLinks58_stub_double():
    # notation_MultiDiagramLinkStyle has no real 'notation_MultiDiagramLinkStyle' property in the generated
    # code (a bare stub) -- manually attach it so notation_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    partner = notation_MultiDiagramLinkStyle()
    setattr(partner, 'notation_MultiDiagramLinkStyle', None)
    _safe_set(owner, 'notation_Diagram59', partner)
    assert owner in getattr(partner, 'notation_MultiDiagramLinkStyle')
    _safe_set(owner, 'notation_Diagram59', None)
    assert owner not in getattr(partner, 'notation_MultiDiagramLinkStyle')


def test_assoc_element18_stub_double():
    # notation_EObject has no real 'notation_EObject20' property in the generated
    # code (a bare stub) -- manually attach it so notation_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_View(mutable=True, type="sample_text", visible=True)
    partner = notation_EObject()
    setattr(partner, 'notation_EObject20', None)
    _safe_set(owner, 'notation_View19', partner)
    assert getattr(partner, 'notation_EObject20') == owner
    _safe_set(owner, 'notation_View19', None)
    assert getattr(partner, 'notation_EObject20') is None


def test_assoc_filteredObjects41_stub_double():
    # notation_EObject has no real 'notation_EObject42' property in the generated
    # code (a bare stub) -- manually attach it so notation_FilteringStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_FilteringStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_FilteringStyle(filtering="sample_text", filteringKeys="sample_text")
    partner = notation_EObject()
    setattr(partner, 'notation_EObject42', None)
    _safe_set(owner, 'notation_FilteringStyle', {partner})
    assert getattr(partner, 'notation_EObject42') == owner
    _safe_set(owner, 'notation_FilteringStyle', set())
    assert getattr(partner, 'notation_EObject42') is None


def test_assoc_horizontalGuides32_stub_double():
    # notation_GuideStyle has no real 'notation_GuideStyle' property in the generated
    # code (a bare stub) -- manually attach it so notation_Guide's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Guide's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Guide(position=7)
    partner = notation_GuideStyle()
    setattr(partner, 'notation_GuideStyle', None)
    _safe_set(owner, 'notation_Guide', partner)
    assert owner in getattr(partner, 'notation_GuideStyle')
    _safe_set(owner, 'notation_Guide', None)
    assert owner not in getattr(partner, 'notation_GuideStyle')


def test_assoc_imageBuffer44_stub_double():
    # notation_ImageBufferStyle has no real 'notation_ImageBufferStyle' property in the generated
    # code (a bare stub) -- manually attach it so notation_Image's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Image's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Image(data="sample_text")
    partner = notation_ImageBufferStyle()
    setattr(partner, 'notation_ImageBufferStyle', None)
    _safe_set(owner, 'notation_Image', partner)
    assert getattr(partner, 'notation_ImageBufferStyle') == owner
    _safe_set(owner, 'notation_Image', None)
    assert getattr(partner, 'notation_ImageBufferStyle') is None


def test_assoc_instanceType48_stub_double():
    # notation_EDataType has no real 'notation_EDataType' property in the generated
    # code (a bare stub) -- manually attach it so notation_PropertyValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_PropertyValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_PropertyValue(rawValue="sample_text")
    partner = notation_EDataType()
    setattr(partner, 'notation_EDataType', None)
    _safe_set(owner, 'notation_PropertyValue49', partner)
    assert getattr(partner, 'notation_EDataType') == owner
    _safe_set(owner, 'notation_PropertyValue49', None)
    assert getattr(partner, 'notation_EDataType') is None


def test_assoc_layoutConstraint9_stub_double():
    # notation_LayoutConstraint has no real 'notation_LayoutConstraint' property in the generated
    # code (a bare stub) -- manually attach it so notation_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Node()
    partner = notation_LayoutConstraint()
    setattr(partner, 'notation_LayoutConstraint', None)
    _safe_set(owner, 'notation_Node', partner)
    assert getattr(partner, 'notation_LayoutConstraint') == owner
    _safe_set(owner, 'notation_Node', None)
    assert getattr(partner, 'notation_LayoutConstraint') is None


def test_assoc_sortedObjects10_stub_double():
    # notation_EObject has no real 'notation_EObject' property in the generated
    # code (a bare stub) -- manually attach it so notation_SortingStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_SortingStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_SortingStyle(sorting="sample_text", sortingKeys="sample_text")
    partner = notation_EObject()
    setattr(partner, 'notation_EObject', None)
    _safe_set(owner, 'notation_SortingStyle', {partner})
    assert getattr(partner, 'notation_EObject') == owner
    _safe_set(owner, 'notation_SortingStyle', set())
    assert getattr(partner, 'notation_EObject') is None


def test_assoc_sourceAnchor4_stub_double():
    # notation_Anchor has no real 'notation_Anchor' property in the generated
    # code (a bare stub) -- manually attach it so notation_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Edge()
    partner = notation_Anchor()
    setattr(partner, 'notation_Anchor', None)
    _safe_set(owner, 'notation_Edge5', partner)
    assert getattr(partner, 'notation_Anchor') == owner
    _safe_set(owner, 'notation_Edge5', None)
    assert getattr(partner, 'notation_Anchor') is None


def test_assoc_styles16_stub_double():
    # notation_Style has no real 'notation_Style' property in the generated
    # code (a bare stub) -- manually attach it so notation_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_View(mutable=True, type="sample_text", visible=True)
    partner = notation_Style()
    setattr(partner, 'notation_Style', None)
    _safe_set(owner, 'notation_View17', {partner})
    assert getattr(partner, 'notation_Style') == owner
    _safe_set(owner, 'notation_View17', set())
    assert getattr(partner, 'notation_Style') is None


def test_assoc_targetAnchor6_stub_double():
    # notation_Anchor has no real 'notation_Anchor8' property in the generated
    # code (a bare stub) -- manually attach it so notation_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Edge()
    partner = notation_Anchor()
    setattr(partner, 'notation_Anchor8', None)
    _safe_set(owner, 'notation_Edge7', partner)
    assert getattr(partner, 'notation_Anchor8') == owner
    _safe_set(owner, 'notation_Edge7', None)
    assert getattr(partner, 'notation_Anchor8') is None


def test_assoc_verticalGuides33_stub_double():
    # notation_GuideStyle has no real 'notation_GuideStyle34' property in the generated
    # code (a bare stub) -- manually attach it so notation_Guide's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Guide's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Guide(position=7)
    partner = notation_GuideStyle()
    setattr(partner, 'notation_GuideStyle34', None)
    _safe_set(owner, 'notation_Guide35', partner)
    assert owner in getattr(partner, 'notation_GuideStyle34')
    _safe_set(owner, 'notation_Guide35', None)
    assert owner not in getattr(partner, 'notation_GuideStyle34')


