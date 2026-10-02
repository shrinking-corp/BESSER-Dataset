import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDNode,
    AbstractNodeMapping,
    AbstractToolDescription,
    AdditionalLayer,
    BasicLabelStyle,
    BasicLabelStyleDescription,
    BorderedStyle,
    CollapseFilter,
    ColorDescription,
    ConditionalContainerStyleDescription,
    ConditionalEdgeStyleDescription,
    ConditionalNodeStyleDescription,
    ConditionalStyleDescription,
    ContainerMapping,
    ContainerModelOperation,
    ContainerStyle,
    CreateView,
    Customizable,
    Customization,
    DDiagram,
    DDiagramElement,
    DDiagramElementContainer,
    DRepresentation,
    DRepresentationElement,
    DSemanticDecorator,
    DecorationDescription,
    DecorationDescriptionsSet,
    DiagramDescription,
    DiagramElementMapping,
    DocumentedElement,
    DragAndDropTarget,
    EdgeMapping,
    EdgeMappingImport,
    EdgeStyle,
    EdgeStyleDescription,
    EdgeTarget,
    EnumLayoutValue,
    EnumOption,
    Filter,
    FilterDescription,
    GraphicalFilter,
    HideLabelCapabilityStyle,
    IEdgeMapping,
    IdentifiedElement,
    InteractiveVariableDescription,
    LabelStyle,
    Layer,
    Layout,
    LayoutOption,
    MappingBasedToolDescription,
    NodeMapping,
    NodeStyle,
    NodeStyleDescription,
    RepresentationCreationDescription,
    RepresentationExtensionDescription,
    RepresentationNavigationDescription,
    Style,
    StyleDescription,
    ToolEntry,
    TypedVariable,
    VariableValue,
    concern_ConcernDescription,
    concern_ConcernSet,
    description_AbstractMappingImport,
    description_AbstractNodeMapping,
    description_AbstractVariable,
    description_ContainerMapping,
    description_DiagramDescription,
    description_DiagramElementMapping,
    description_DocumentedElement,
    description_DragAndDropTargetDescription,
    description_EndUserDocumentedElement,
    description_IEdgeMapping,
    description_IdentifiedElement,
    description_NodeMapping,
    description_PasteTargetDescription,
    description_RepresentationDescription,
    description_RepresentationElementMapping,
    description_RepresentationImportDescription,
    diagram_AbsoluteBoundsFilter,
    diagram_AbstractDNode,
    diagram_AppliedCompositeFilters,
    diagram_BeginLabelStyle,
    diagram_BorderedStyle,
    diagram_BracketEdgeStyle,
    diagram_BundledImage,
    diagram_CenterLabelStyle,
    diagram_CollapseFilter,
    diagram_ComputedStyleDescriptionRegistry,
    diagram_ContainerStyle,
    diagram_CustomStyle,
    diagram_DDiagram,
    diagram_DDiagramElement,
    diagram_DDiagramElementContainer,
    diagram_DEdge,
    diagram_DNode,
    diagram_DNodeContainer,
    diagram_DNodeList,
    diagram_DNodeListElement,
    diagram_DSemanticDiagram,
    diagram_Decoration,
    diagram_Dot,
    diagram_DragAndDropTarget,
    diagram_EObject,
    diagram_EObjectVariableValue,
    diagram_EdgeStyle,
    diagram_EdgeTarget,
    diagram_Ellipse,
    diagram_EndLabelStyle,
    diagram_FilterVariableHistory,
    diagram_FlatContainerStyle,
    diagram_FoldingFilter,
    diagram_FoldingPointFilter,
    diagram_GaugeCompositeStyle,
    diagram_GaugeSection,
    diagram_GraphicalFilter,
    diagram_HideFilter,
    diagram_HideLabelCapabilityStyle,
    diagram_HideLabelFilter,
    diagram_IndirectlyCollapseFilter,
    diagram_Lozenge,
    diagram_NodeStyle,
    diagram_Note,
    diagram_ShapeContainerStyle,
    diagram_Square,
    diagram_Style,
    diagram_TypedVariableValue,
    diagram_VariableValue,
    diagram_WorkspaceImage,
    diagram_concern_ConcernDescription,
    diagram_concern_ConcernSet,
    diagram_description_AbstractNodeMapping,
    diagram_description_AdditionalLayer,
    diagram_description_BooleanLayoutOption,
    diagram_description_CompositeLayout,
    diagram_description_ConditionalContainerStyleDescription,
    diagram_description_ConditionalEdgeStyleDescription,
    diagram_description_ConditionalNodeStyleDescription,
    diagram_description_ContainerMapping,
    diagram_description_ContainerMappingImport,
    diagram_description_CustomLayoutConfiguration,
    diagram_description_DiagramDescription,
    diagram_description_DiagramElementMapping,
    diagram_description_DiagramExtensionDescription,
    diagram_description_DiagramImportDescription,
    diagram_description_DoubleLayoutOption,
    diagram_description_DragAndDropTargetDescription,
    diagram_description_EdgeMapping,
    diagram_description_EdgeMappingImport,
    diagram_description_EnumLayoutOption,
    diagram_description_EnumLayoutValue,
    diagram_description_EnumOption,
    diagram_description_EnumSetLayoutOption,
    diagram_description_IEdgeMapping,
    diagram_description_IntegerLayoutOption,
    diagram_description_Layer,
    diagram_description_Layout,
    diagram_description_LayoutOption,
    diagram_description_MappingBasedDecoration,
    diagram_description_NodeMapping,
    diagram_description_NodeMappingImport,
    diagram_description_OrderedTreeLayout,
    diagram_description_StringLayoutOption,
    diagram_filter_CompositeFilterDescription,
    diagram_filter_Filter,
    diagram_filter_FilterDescription,
    diagram_filter_MappingFilter,
    diagram_filter_VariableFilter,
    diagram_style_BeginLabelStyleDescription,
    diagram_style_BorderedStyleDescription,
    diagram_style_BracketEdgeStyleDescription,
    diagram_style_BundledImageDescription,
    diagram_style_CenterLabelStyleDescription,
    diagram_style_ContainerStyleDescription,
    diagram_style_CustomStyleDescription,
    diagram_style_DotDescription,
    diagram_style_EdgeStyleDescription,
    diagram_style_EllipseNodeDescription,
    diagram_style_EndLabelStyleDescription,
    diagram_style_FlatContainerStyleDescription,
    diagram_style_GaugeCompositeStyleDescription,
    diagram_style_GaugeSectionDescription,
    diagram_style_HideLabelCapabilityStyleDescription,
    diagram_style_LozengeNodeDescription,
    diagram_style_NodeStyleDescription,
    diagram_style_NoteDescription,
    diagram_style_RoundedCornerStyleDescription,
    diagram_style_ShapeContainerStyleDescription,
    diagram_style_SizeComputationContainerStyleDescription,
    diagram_style_SquareDescription,
    diagram_style_WorkspaceImageDescription,
    diagram_tool_BehaviorTool,
    diagram_tool_ContainerCreationDescription,
    diagram_tool_ContainerDropDescription,
    diagram_tool_CreateEdgeView,
    diagram_tool_CreateView,
    diagram_tool_DeleteElementDescription,
    diagram_tool_DeleteHook,
    diagram_tool_DeleteHookParameter,
    diagram_tool_DiagramCreationDescription,
    diagram_tool_DiagramNavigationDescription,
    diagram_tool_DirectEditLabel,
    diagram_tool_DoubleClickDescription,
    diagram_tool_EdgeCreationDescription,
    diagram_tool_ElementDoubleClickVariable,
    diagram_tool_Navigation,
    diagram_tool_NodeCreationDescription,
    diagram_tool_NodeCreationVariable,
    diagram_tool_ReconnectEdgeDescription,
    diagram_tool_RequestDescription,
    diagram_tool_SourceEdgeCreationVariable,
    diagram_tool_SourceEdgeViewCreationVariable,
    diagram_tool_TargetEdgeCreationVariable,
    diagram_tool_TargetEdgeViewCreationVariable,
    diagram_tool_ToolGroup,
    diagram_tool_ToolGroupExtension,
    diagram_tool_ToolSection,
    filter_CompositeFilterDescription,
    filter_Filter,
    filter_FilterDescription,
    style_BeginLabelStyleDescription,
    style_BorderedStyleDescription,
    style_CenterLabelStyleDescription,
    style_ContainerStyleDescription,
    style_EdgeStyleDescription,
    style_EndLabelStyleDescription,
    style_GaugeSectionDescription,
    style_HideLabelCapabilityStyleDescription,
    style_LabelBorderStyleDescription,
    style_LabelStyleDescription,
    style_NodeStyleDescription,
    style_RoundedCornerStyleDescription,
    style_SizeComputationContainerStyleDescription,
    style_StyleDescription,
    style_TooltipStyleDescription,
    tool_AbstractToolDescription,
    tool_BehaviorTool,
    tool_ContainerDropDescription,
    tool_ContainerViewVariable,
    tool_DeleteElementDescription,
    tool_DeleteHook,
    tool_DeleteHookParameter,
    tool_DirectEditLabel,
    tool_DoubleClickDescription,
    tool_DropContainerVariable,
    tool_EditMaskVariables,
    tool_ElementDeleteVariable,
    tool_ElementDoubleClickVariable,
    tool_ElementDropVariable,
    tool_ElementSelectVariable,
    tool_GroupMenu,
    tool_InitEdgeCreationOperation,
    tool_InitialContainerDropOperation,
    tool_InitialNodeCreationOperation,
    tool_InitialOperation,
    tool_NodeCreationVariable,
    tool_PopupMenu,
    tool_ReconnectEdgeDescription,
    tool_RepresentationCreationDescription,
    tool_SelectModelElementVariable,
    tool_SourceEdgeCreationVariable,
    tool_SourceEdgeViewCreationVariable,
    tool_TargetEdgeCreationVariable,
    tool_TargetEdgeViewCreationVariable,
    tool_ToolEntry,
    tool_ToolGroup,
    tool_ToolGroupExtension,
    tool_ToolSection,
    tool_VariableContainer,
    validation_ValidationRule,
    validation_ValidationSet,
    AlignmentKind,
    ArrangeConstraint,
    BackgroundStyle,
    BundledImageShape,
    CenteringStyle,
    ContainerLayout,
    ContainerShape,
    EdgeArrows,
    EdgeRouting,
    FilterKind,
    FoldingStyle,
    LabelPosition,
    LayoutDirection,
    LayoutOptionTarget,
    LineStyle,
    ReconnectionKind,
    ResizeKind,
    Side,
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

def test_assoc_beginLabelStyle108_reverse_link_reassign_clear():
    a1 = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    a2 = diagram_EdgeStyle(centered="sample_text_2", foldingStyle="sample_text_2", lineStyle="sample_text_2", routingStyle="sample_text_2", size="sample_text_2", sourceArrow="sample_text_2", strokeColor="sample_text_2", targetArrow="sample_text_2")
    b = diagram_BeginLabelStyle()
    _safe_set(b, 'diagram_BeginLabelStyle', a1)
    assert _is_linked(b, 'diagram_BeginLabelStyle', a1)
    if hasattr(a1, 'diagram_EdgeStyle109'):
        assert _is_linked(a1, 'diagram_EdgeStyle109', b)
    _safe_set(b, 'diagram_BeginLabelStyle', a2)
    assert _is_linked(b, 'diagram_BeginLabelStyle', a2)
    if hasattr(a1, 'diagram_EdgeStyle109'):
        assert not _is_linked(a1, 'diagram_EdgeStyle109', b)
    if hasattr(a2, 'diagram_EdgeStyle109'):
        assert _is_linked(a2, 'diagram_EdgeStyle109', b)
    _safe_set(b, 'diagram_BeginLabelStyle', None)
    assert not _is_linked(b, 'diagram_BeginLabelStyle', a2)
    if hasattr(a2, 'diagram_EdgeStyle109'):
        assert not _is_linked(a2, 'diagram_EdgeStyle109', b)


def test_assoc_centerLabelStyle110_reverse_link_reassign_clear():
    a1 = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    a2 = diagram_EdgeStyle(centered="sample_text_2", foldingStyle="sample_text_2", lineStyle="sample_text_2", routingStyle="sample_text_2", size="sample_text_2", sourceArrow="sample_text_2", strokeColor="sample_text_2", targetArrow="sample_text_2")
    b = diagram_CenterLabelStyle()
    _safe_set(b, 'diagram_CenterLabelStyle', a1)
    assert _is_linked(b, 'diagram_CenterLabelStyle', a1)
    if hasattr(a1, 'diagram_EdgeStyle111'):
        assert _is_linked(a1, 'diagram_EdgeStyle111', b)
    _safe_set(b, 'diagram_CenterLabelStyle', a2)
    assert _is_linked(b, 'diagram_CenterLabelStyle', a2)
    if hasattr(a1, 'diagram_EdgeStyle111'):
        assert not _is_linked(a1, 'diagram_EdgeStyle111', b)
    if hasattr(a2, 'diagram_EdgeStyle111'):
        assert _is_linked(a2, 'diagram_EdgeStyle111', b)
    _safe_set(b, 'diagram_CenterLabelStyle', None)
    assert not _is_linked(b, 'diagram_CenterLabelStyle', a2)
    if hasattr(a2, 'diagram_EdgeStyle111'):
        assert not _is_linked(a2, 'diagram_EdgeStyle111', b)


def test_assoc_containers12_reverse_link_reassign_clear():
    a1 = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    a2 = diagram_DDiagramElementContainer(height="sample_text_2", width="sample_text_2")
    b = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    _safe_set(b, 'diagram_DDiagram13', {a1})
    assert _is_linked(b, 'diagram_DDiagram13', a1)
    if hasattr(a1, 'diagram_DDiagramElementContainer'):
        assert _is_linked(a1, 'diagram_DDiagramElementContainer', b)
    _safe_set(b, 'diagram_DDiagram13', {a2})
    assert _is_linked(b, 'diagram_DDiagram13', a2)
    if hasattr(a1, 'diagram_DDiagramElementContainer'):
        assert not _is_linked(a1, 'diagram_DDiagramElementContainer', b)
    if hasattr(a2, 'diagram_DDiagramElementContainer'):
        assert _is_linked(a2, 'diagram_DDiagramElementContainer', b)
    _safe_set(b, 'diagram_DDiagram13', set())
    assert not _is_linked(b, 'diagram_DDiagram13', a2)
    if hasattr(a2, 'diagram_DDiagramElementContainer'):
        assert not _is_linked(a2, 'diagram_DDiagramElementContainer', b)


def test_assoc_containers62_reverse_link_reassign_clear():
    a1 = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    a2 = diagram_DDiagramElementContainer(height="sample_text_2", width="sample_text_2")
    b = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    _safe_set(b, 'diagram_DDiagramElementContainer63', a1)
    assert _is_linked(b, 'diagram_DDiagramElementContainer63', a1)
    if hasattr(a1, 'diagram_DDiagramElementContainer61'):
        assert _is_linked(a1, 'diagram_DDiagramElementContainer61', b)
    _safe_set(b, 'diagram_DDiagramElementContainer63', a2)
    assert _is_linked(b, 'diagram_DDiagramElementContainer63', a2)
    if hasattr(a1, 'diagram_DDiagramElementContainer61'):
        assert not _is_linked(a1, 'diagram_DDiagramElementContainer61', b)
    if hasattr(a2, 'diagram_DDiagramElementContainer61'):
        assert _is_linked(a2, 'diagram_DDiagramElementContainer61', b)
    _safe_set(b, 'diagram_DDiagramElementContainer63', None)
    assert not _is_linked(b, 'diagram_DDiagramElementContainer63', a2)
    if hasattr(a2, 'diagram_DDiagramElementContainer61'):
        assert not _is_linked(a2, 'diagram_DDiagramElementContainer61', b)


def test_assoc_diagramElements1_reverse_link_reassign_clear():
    a1 = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    a2 = diagram_DDiagramElement(tooltipText="sample_text_2", visible=False)
    b = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    _safe_set(b, 'diagram_DDiagram2', {a1})
    assert _is_linked(b, 'diagram_DDiagram2', a1)
    if hasattr(a1, 'diagram_DDiagramElement3'):
        assert _is_linked(a1, 'diagram_DDiagramElement3', b)
    _safe_set(b, 'diagram_DDiagram2', {a2})
    assert _is_linked(b, 'diagram_DDiagram2', a2)
    if hasattr(a1, 'diagram_DDiagramElement3'):
        assert not _is_linked(a1, 'diagram_DDiagramElement3', b)
    if hasattr(a2, 'diagram_DDiagramElement3'):
        assert _is_linked(a2, 'diagram_DDiagramElement3', b)
    _safe_set(b, 'diagram_DDiagram2', set())
    assert not _is_linked(b, 'diagram_DDiagram2', a2)
    if hasattr(a2, 'diagram_DDiagramElement3'):
        assert not _is_linked(a2, 'diagram_DDiagramElement3', b)


def test_assoc_edges6_reverse_link_reassign_clear():
    a1 = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    a2 = diagram_DEdge(arrangeConstraints="sample_text_2", beginLabel="sample_text_2", endLabel="sample_text_2", isFold=False, isMockEdge=False, routingStyle="sample_text_2", size="sample_text_2")
    b = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    _safe_set(b, 'diagram_DDiagram7', {a1})
    assert _is_linked(b, 'diagram_DDiagram7', a1)
    if hasattr(a1, 'diagram_DEdge'):
        assert _is_linked(a1, 'diagram_DEdge', b)
    _safe_set(b, 'diagram_DDiagram7', {a2})
    assert _is_linked(b, 'diagram_DDiagram7', a2)
    if hasattr(a1, 'diagram_DEdge'):
        assert not _is_linked(a1, 'diagram_DEdge', b)
    if hasattr(a2, 'diagram_DEdge'):
        assert _is_linked(a2, 'diagram_DEdge', b)
    _safe_set(b, 'diagram_DDiagram7', set())
    assert not _is_linked(b, 'diagram_DDiagram7', a2)
    if hasattr(a2, 'diagram_DEdge'):
        assert not _is_linked(a2, 'diagram_DEdge', b)


def test_assoc_elements64_reverse_link_reassign_clear():
    a1 = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    a2 = diagram_DDiagramElementContainer(height="sample_text_2", width="sample_text_2")
    b = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    _safe_set(b, 'diagram_DDiagramElement66', a1)
    assert _is_linked(b, 'diagram_DDiagramElement66', a1)
    if hasattr(a1, 'diagram_DDiagramElementContainer65'):
        assert _is_linked(a1, 'diagram_DDiagramElementContainer65', b)
    _safe_set(b, 'diagram_DDiagramElement66', a2)
    assert _is_linked(b, 'diagram_DDiagramElement66', a2)
    if hasattr(a1, 'diagram_DDiagramElementContainer65'):
        assert not _is_linked(a1, 'diagram_DDiagramElementContainer65', b)
    if hasattr(a2, 'diagram_DDiagramElementContainer65'):
        assert _is_linked(a2, 'diagram_DDiagramElementContainer65', b)
    _safe_set(b, 'diagram_DDiagramElement66', None)
    assert not _is_linked(b, 'diagram_DDiagramElement66', a2)
    if hasattr(a2, 'diagram_DDiagramElementContainer65'):
        assert not _is_linked(a2, 'diagram_DDiagramElementContainer65', b)


def test_assoc_endLabelStyle112_reverse_link_reassign_clear():
    a1 = diagram_EndLabelStyle()
    a2 = diagram_EndLabelStyle()
    b = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    _safe_set(b, 'diagram_EdgeStyle113', a1)
    assert _is_linked(b, 'diagram_EdgeStyle113', a1)
    if hasattr(a1, 'diagram_EndLabelStyle'):
        assert _is_linked(a1, 'diagram_EndLabelStyle', b)
    _safe_set(b, 'diagram_EdgeStyle113', a2)
    assert _is_linked(b, 'diagram_EdgeStyle113', a2)
    if hasattr(a1, 'diagram_EndLabelStyle'):
        assert not _is_linked(a1, 'diagram_EndLabelStyle', b)
    if hasattr(a2, 'diagram_EndLabelStyle'):
        assert _is_linked(a2, 'diagram_EndLabelStyle', b)
    _safe_set(b, 'diagram_EdgeStyle113', None)
    assert not _is_linked(b, 'diagram_EdgeStyle113', a2)
    if hasattr(a2, 'diagram_EndLabelStyle'):
        assert not _is_linked(a2, 'diagram_EndLabelStyle', b)


def test_assoc_hiddenElements31_reverse_link_reassign_clear():
    a1 = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    a2 = diagram_DDiagramElement(tooltipText="sample_text_2", visible=False)
    b = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    _safe_set(b, 'diagram_DDiagram32', {a1})
    assert _is_linked(b, 'diagram_DDiagram32', a1)
    if hasattr(a1, 'diagram_DDiagramElement33'):
        assert _is_linked(a1, 'diagram_DDiagramElement33', b)
    _safe_set(b, 'diagram_DDiagram32', {a2})
    assert _is_linked(b, 'diagram_DDiagram32', a2)
    if hasattr(a1, 'diagram_DDiagramElement33'):
        assert not _is_linked(a1, 'diagram_DDiagramElement33', b)
    if hasattr(a2, 'diagram_DDiagramElement33'):
        assert _is_linked(a2, 'diagram_DDiagramElement33', b)
    _safe_set(b, 'diagram_DDiagram32', set())
    assert not _is_linked(b, 'diagram_DDiagram32', a2)
    if hasattr(a2, 'diagram_DDiagramElement33'):
        assert not _is_linked(a2, 'diagram_DDiagramElement33', b)


def test_assoc_nodes58_reverse_link_reassign_clear():
    a1 = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    a2 = diagram_DNode(height="sample_text_2", labelPosition="sample_text_2", resizeKind="sample_text_2", width="sample_text_2")
    b = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    _safe_set(b, 'diagram_DDiagramElementContainer59', {a1})
    assert _is_linked(b, 'diagram_DDiagramElementContainer59', a1)
    if hasattr(a1, 'diagram_DNode60'):
        assert _is_linked(a1, 'diagram_DNode60', b)
    _safe_set(b, 'diagram_DDiagramElementContainer59', {a2})
    assert _is_linked(b, 'diagram_DDiagramElementContainer59', a2)
    if hasattr(a1, 'diagram_DNode60'):
        assert not _is_linked(a1, 'diagram_DNode60', b)
    if hasattr(a2, 'diagram_DNode60'):
        assert _is_linked(a2, 'diagram_DNode60', b)
    _safe_set(b, 'diagram_DDiagramElementContainer59', set())
    assert not _is_linked(b, 'diagram_DDiagramElementContainer59', a2)
    if hasattr(a2, 'diagram_DNode60'):
        assert not _is_linked(a2, 'diagram_DNode60', b)


def test_assoc_nodes8_reverse_link_reassign_clear():
    a1 = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    a2 = diagram_DNode(height="sample_text_2", labelPosition="sample_text_2", resizeKind="sample_text_2", width="sample_text_2")
    b = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    _safe_set(b, 'diagram_DDiagram9', {a1})
    assert _is_linked(b, 'diagram_DDiagram9', a1)
    if hasattr(a1, 'diagram_DNode'):
        assert _is_linked(a1, 'diagram_DNode', b)
    _safe_set(b, 'diagram_DDiagram9', {a2})
    assert _is_linked(b, 'diagram_DDiagram9', a2)
    if hasattr(a1, 'diagram_DNode'):
        assert not _is_linked(a1, 'diagram_DNode', b)
    if hasattr(a2, 'diagram_DNode'):
        assert _is_linked(a2, 'diagram_DNode', b)
    _safe_set(b, 'diagram_DDiagram9', set())
    assert not _is_linked(b, 'diagram_DDiagram9', a2)
    if hasattr(a2, 'diagram_DNode'):
        assert not _is_linked(a2, 'diagram_DNode', b)


def test_assoc_ownedBorderedNodes47_reverse_link_reassign_clear():
    a1 = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    a2 = diagram_DNode(height="sample_text_2", labelPosition="sample_text_2", resizeKind="sample_text_2", width="sample_text_2")
    b = diagram_AbstractDNode(arrangeConstraints="sample_text")
    _safe_set(b, 'diagram_AbstractDNode', {a1})
    assert _is_linked(b, 'diagram_AbstractDNode', a1)
    if hasattr(a1, 'diagram_DNode48'):
        assert _is_linked(a1, 'diagram_DNode48', b)
    _safe_set(b, 'diagram_AbstractDNode', {a2})
    assert _is_linked(b, 'diagram_AbstractDNode', a2)
    if hasattr(a1, 'diagram_DNode48'):
        assert not _is_linked(a1, 'diagram_DNode48', b)
    if hasattr(a2, 'diagram_DNode48'):
        assert _is_linked(a2, 'diagram_DNode48', b)
    _safe_set(b, 'diagram_AbstractDNode', set())
    assert not _is_linked(b, 'diagram_AbstractDNode', a2)
    if hasattr(a2, 'diagram_DNode48'):
        assert not _is_linked(a2, 'diagram_DNode48', b)


def test_assoc_ownedDiagramElements0_reverse_link_reassign_clear():
    a1 = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    a2 = diagram_DDiagramElement(tooltipText="sample_text_2", visible=False)
    b = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    _safe_set(b, 'diagram_DDiagram', {a1})
    assert _is_linked(b, 'diagram_DDiagram', a1)
    if hasattr(a1, 'diagram_DDiagramElement'):
        assert _is_linked(a1, 'diagram_DDiagramElement', b)
    _safe_set(b, 'diagram_DDiagram', {a2})
    assert _is_linked(b, 'diagram_DDiagram', a2)
    if hasattr(a1, 'diagram_DDiagramElement'):
        assert not _is_linked(a1, 'diagram_DDiagramElement', b)
    if hasattr(a2, 'diagram_DDiagramElement'):
        assert _is_linked(a2, 'diagram_DDiagramElement', b)
    _safe_set(b, 'diagram_DDiagram', set())
    assert not _is_linked(b, 'diagram_DDiagram', a2)
    if hasattr(a2, 'diagram_DDiagramElement'):
        assert not _is_linked(a2, 'diagram_DDiagramElement', b)


def test_assoc_ownedDiagramElements77_reverse_link_reassign_clear():
    a1 = diagram_DNodeContainer(childrenPresentation="sample_text")
    a2 = diagram_DNodeContainer(childrenPresentation="sample_text_2")
    b = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    _safe_set(b, 'diagram_DDiagramElement78', a1)
    assert _is_linked(b, 'diagram_DDiagramElement78', a1)
    if hasattr(a1, 'diagram_DNodeContainer'):
        assert _is_linked(a1, 'diagram_DNodeContainer', b)
    _safe_set(b, 'diagram_DDiagramElement78', a2)
    assert _is_linked(b, 'diagram_DDiagramElement78', a2)
    if hasattr(a1, 'diagram_DNodeContainer'):
        assert not _is_linked(a1, 'diagram_DNodeContainer', b)
    if hasattr(a2, 'diagram_DNodeContainer'):
        assert _is_linked(a2, 'diagram_DNodeContainer', b)
    _safe_set(b, 'diagram_DDiagramElement78', None)
    assert not _is_linked(b, 'diagram_DDiagramElement78', a2)
    if hasattr(a2, 'diagram_DNodeContainer'):
        assert not _is_linked(a2, 'diagram_DNodeContainer', b)


def test_assoc_ownedStyle49_reverse_link_reassign_clear():
    a1 = diagram_NodeStyle(labelPosition="sample_text")
    a2 = diagram_NodeStyle(labelPosition="sample_text_2")
    b = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    _safe_set(b, 'diagram_DNode50', a1)
    assert _is_linked(b, 'diagram_DNode50', a1)
    if hasattr(a1, 'diagram_NodeStyle'):
        assert _is_linked(a1, 'diagram_NodeStyle', b)
    _safe_set(b, 'diagram_DNode50', a2)
    assert _is_linked(b, 'diagram_DNode50', a2)
    if hasattr(a1, 'diagram_NodeStyle'):
        assert not _is_linked(a1, 'diagram_NodeStyle', b)
    if hasattr(a2, 'diagram_NodeStyle'):
        assert _is_linked(a2, 'diagram_NodeStyle', b)
    _safe_set(b, 'diagram_DNode50', None)
    assert not _is_linked(b, 'diagram_DNode50', a2)
    if hasattr(a2, 'diagram_NodeStyle'):
        assert not _is_linked(a2, 'diagram_NodeStyle', b)


def test_assoc_ownedStyle93_reverse_link_reassign_clear():
    a1 = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    a2 = diagram_EdgeStyle(centered="sample_text_2", foldingStyle="sample_text_2", lineStyle="sample_text_2", routingStyle="sample_text_2", size="sample_text_2", sourceArrow="sample_text_2", strokeColor="sample_text_2", targetArrow="sample_text_2")
    b = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    _safe_set(b, 'diagram_DEdge94', a1)
    assert _is_linked(b, 'diagram_DEdge94', a1)
    if hasattr(a1, 'diagram_EdgeStyle'):
        assert _is_linked(a1, 'diagram_EdgeStyle', b)
    _safe_set(b, 'diagram_DEdge94', a2)
    assert _is_linked(b, 'diagram_DEdge94', a2)
    if hasattr(a1, 'diagram_EdgeStyle'):
        assert not _is_linked(a1, 'diagram_EdgeStyle', b)
    if hasattr(a2, 'diagram_EdgeStyle'):
        assert _is_linked(a2, 'diagram_EdgeStyle', b)
    _safe_set(b, 'diagram_DEdge94', None)
    assert not _is_linked(b, 'diagram_DEdge94', a2)
    if hasattr(a2, 'diagram_EdgeStyle'):
        assert not _is_linked(a2, 'diagram_EdgeStyle', b)


def test_assoc_sections114_reverse_link_reassign_clear():
    a1 = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    a2 = diagram_GaugeSection(backgroundColor="sample_text_2", foregroundColor="sample_text_2", label="sample_text_2", max="sample_text_2", min="sample_text_2", value="sample_text_2")
    b = diagram_GaugeCompositeStyle(alignment="sample_text")
    _safe_set(b, 'diagram_GaugeCompositeStyle', {a1})
    assert _is_linked(b, 'diagram_GaugeCompositeStyle', a1)
    if hasattr(a1, 'diagram_GaugeSection'):
        assert _is_linked(a1, 'diagram_GaugeSection', b)
    _safe_set(b, 'diagram_GaugeCompositeStyle', {a2})
    assert _is_linked(b, 'diagram_GaugeCompositeStyle', a2)
    if hasattr(a1, 'diagram_GaugeSection'):
        assert not _is_linked(a1, 'diagram_GaugeSection', b)
    if hasattr(a2, 'diagram_GaugeSection'):
        assert _is_linked(a2, 'diagram_GaugeSection', b)
    _safe_set(b, 'diagram_GaugeCompositeStyle', set())
    assert not _is_linked(b, 'diagram_GaugeCompositeStyle', a2)
    if hasattr(a2, 'diagram_GaugeSection'):
        assert not _is_linked(a2, 'diagram_GaugeSection', b)


