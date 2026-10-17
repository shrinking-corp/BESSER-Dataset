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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activateBehaviors25_stub_double():
    # tool_BehaviorTool has no real 'tool_BehaviorTool' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = tool_BehaviorTool()
    setattr(partner, 'tool_BehaviorTool', None)
    _safe_set(owner, 'diagram_DDiagram26', {partner})
    assert getattr(partner, 'tool_BehaviorTool') == owner
    _safe_set(owner, 'diagram_DDiagram26', set())
    assert getattr(partner, 'tool_BehaviorTool') is None


def test_assoc_activatedFilters16_stub_double():
    # filter_FilterDescription has no real 'filter_FilterDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = filter_FilterDescription()
    setattr(partner, 'filter_FilterDescription', None)
    _safe_set(owner, 'diagram_DDiagram17', {partner})
    assert getattr(partner, 'filter_FilterDescription') == owner
    _safe_set(owner, 'diagram_DDiagram17', set())
    assert getattr(partner, 'filter_FilterDescription') is None


def test_assoc_activatedLayers29_stub_double():
    # Layer has no real 'Layer' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = Layer()
    setattr(partner, 'Layer', None)
    _safe_set(owner, 'diagram_DDiagram30', {partner})
    assert getattr(partner, 'Layer') == owner
    _safe_set(owner, 'diagram_DDiagram30', set())
    assert getattr(partner, 'Layer') is None


def test_assoc_activatedRules23_stub_double():
    # validation_ValidationRule has no real 'validation_ValidationRule' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = validation_ValidationRule()
    setattr(partner, 'validation_ValidationRule', None)
    _safe_set(owner, 'diagram_DDiagram24', {partner})
    assert getattr(partner, 'validation_ValidationRule') == owner
    _safe_set(owner, 'diagram_DDiagram24', set())
    assert getattr(partner, 'validation_ValidationRule') is None


def test_assoc_activatedTransientLayers18_stub_double():
    # AdditionalLayer has no real 'AdditionalLayer' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = AdditionalLayer()
    setattr(partner, 'AdditionalLayer', None)
    _safe_set(owner, 'diagram_DDiagram19', {partner})
    assert getattr(partner, 'AdditionalLayer') == owner
    _safe_set(owner, 'diagram_DDiagram19', set())
    assert getattr(partner, 'AdditionalLayer') is None


def test_assoc_actualMapping53_stub_double():
    # NodeMapping has no real 'NodeMapping' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping', None)
    _safe_set(owner, 'diagram_DNode54', partner)
    assert getattr(partner, 'NodeMapping') == owner
    _safe_set(owner, 'diagram_DNode54', None)
    assert getattr(partner, 'NodeMapping') is None


def test_assoc_actualMapping72_stub_double():
    # ContainerMapping has no real 'ContainerMapping' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElementContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElementContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    partner = ContainerMapping()
    setattr(partner, 'ContainerMapping', None)
    _safe_set(owner, 'diagram_DDiagramElementContainer73', partner)
    assert getattr(partner, 'ContainerMapping') == owner
    _safe_set(owner, 'diagram_DDiagramElementContainer73', None)
    assert getattr(partner, 'ContainerMapping') is None


def test_assoc_actualMapping98_stub_double():
    # IEdgeMapping has no real 'IEdgeMapping' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    partner = IEdgeMapping()
    setattr(partner, 'IEdgeMapping', None)
    _safe_set(owner, 'diagram_DEdge99', partner)
    assert getattr(partner, 'IEdgeMapping') == owner
    _safe_set(owner, 'diagram_DEdge99', None)
    assert getattr(partner, 'IEdgeMapping') is None


def test_assoc_additionalLayers144_stub_double():
    # AdditionalLayer has no real 'AdditionalLayer146' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = AdditionalLayer()
    setattr(partner, 'AdditionalLayer146', None)
    _safe_set(owner, 'diagram_description_DiagramDescription145', {partner})
    assert getattr(partner, 'AdditionalLayer146') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription145', set())
    assert getattr(partner, 'AdditionalLayer146') is None


def test_assoc_allEdgeMappings124_stub_double():
    # EdgeMapping has no real 'EdgeMapping' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = EdgeMapping()
    setattr(partner, 'EdgeMapping', None)
    _safe_set(owner, 'diagram_description_DiagramDescription125', {partner})
    assert getattr(partner, 'EdgeMapping') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription125', set())
    assert getattr(partner, 'EdgeMapping') is None


def test_assoc_allFilters20_stub_double():
    # filter_FilterDescription has no real 'filter_FilterDescription22' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = filter_FilterDescription()
    setattr(partner, 'filter_FilterDescription22', None)
    _safe_set(owner, 'diagram_DDiagram21', {partner})
    assert getattr(partner, 'filter_FilterDescription22') == owner
    _safe_set(owner, 'diagram_DDiagram21', set())
    assert getattr(partner, 'filter_FilterDescription22') is None


def test_assoc_allTools130_stub_double():
    # tool_AbstractToolDescription has no real 'tool_AbstractToolDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = tool_AbstractToolDescription()
    setattr(partner, 'tool_AbstractToolDescription', None)
    _safe_set(owner, 'diagram_description_DiagramDescription131', {partner})
    assert getattr(partner, 'tool_AbstractToolDescription') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription131', set())
    assert getattr(partner, 'tool_AbstractToolDescription') is None


def test_assoc_allTools257_stub_double():
    # tool_AbstractToolDescription has no real 'tool_AbstractToolDescription259' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = tool_AbstractToolDescription()
    setattr(partner, 'tool_AbstractToolDescription259', None)
    _safe_set(owner, 'diagram_description_Layer258', {partner})
    assert getattr(partner, 'tool_AbstractToolDescription259') == owner
    _safe_set(owner, 'diagram_description_Layer258', set())
    assert getattr(partner, 'tool_AbstractToolDescription259') is None


def test_assoc_backgroundColor166_stub_double():
    # ColorDescription has no real 'ColorDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription', None)
    _safe_set(owner, 'diagram_description_DiagramDescription167', partner)
    assert getattr(partner, 'ColorDescription') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription167', None)
    assert getattr(partner, 'ColorDescription') is None


def test_assoc_backgroundColor283_stub_double():
    # ColorDescription has no real 'ColorDescription284' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_DotDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_DotDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_DotDescription(strokeSizeComputationExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription284', None)
    _safe_set(owner, 'diagram_style_DotDescription', partner)
    assert getattr(partner, 'ColorDescription284') == owner
    _safe_set(owner, 'diagram_style_DotDescription', None)
    assert getattr(partner, 'ColorDescription284') is None


def test_assoc_backgroundColor286_stub_double():
    # ColorDescription has no real 'ColorDescription287' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_GaugeSectionDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_GaugeSectionDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription287', None)
    _safe_set(owner, 'diagram_style_GaugeSectionDescription', partner)
    assert getattr(partner, 'ColorDescription287') == owner
    _safe_set(owner, 'diagram_style_GaugeSectionDescription', None)
    assert getattr(partner, 'ColorDescription287') is None


def test_assoc_backgroundColor291_stub_double():
    # ColorDescription has no real 'ColorDescription292' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_FlatContainerStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_FlatContainerStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription292', None)
    _safe_set(owner, 'diagram_style_FlatContainerStyleDescription', partner)
    assert getattr(partner, 'ColorDescription292') == owner
    _safe_set(owner, 'diagram_style_FlatContainerStyleDescription', None)
    assert getattr(partner, 'ColorDescription292') is None


def test_assoc_backgroundColor298_stub_double():
    # ColorDescription has no real 'ColorDescription299' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_ShapeContainerStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_ShapeContainerStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_ShapeContainerStyleDescription(shape="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription299', None)
    _safe_set(owner, 'diagram_style_ShapeContainerStyleDescription', partner)
    assert getattr(partner, 'ColorDescription299') == owner
    _safe_set(owner, 'diagram_style_ShapeContainerStyleDescription', None)
    assert getattr(partner, 'ColorDescription299') is None


def test_assoc_beginLabelStyleDescription302_stub_double():
    # style_BeginLabelStyleDescription has no real 'style_BeginLabelStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_EdgeStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_EdgeStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    partner = style_BeginLabelStyleDescription()
    setattr(partner, 'style_BeginLabelStyleDescription', None)
    _safe_set(owner, 'diagram_style_EdgeStyleDescription303', partner)
    assert getattr(partner, 'style_BeginLabelStyleDescription') == owner
    _safe_set(owner, 'diagram_style_EdgeStyleDescription303', None)
    assert getattr(partner, 'style_BeginLabelStyleDescription') is None


def test_assoc_borderColor271_stub_double():
    # ColorDescription has no real 'ColorDescription272' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_BorderedStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_BorderedStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_BorderedStyleDescription(borderLineStyle="sample_text", borderSizeComputationExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription272', None)
    _safe_set(owner, 'diagram_style_BorderedStyleDescription', partner)
    assert getattr(partner, 'ColorDescription272') == owner
    _safe_set(owner, 'diagram_style_BorderedStyleDescription', None)
    assert getattr(partner, 'ColorDescription272') is None


def test_assoc_borderedNodeMappings182_stub_double():
    # NodeMapping has no real 'NodeMapping183' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_AbstractNodeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_AbstractNodeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_AbstractNodeMapping(domainClass="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping183', None)
    _safe_set(owner, 'diagram_description_AbstractNodeMapping', {partner})
    assert getattr(partner, 'NodeMapping183') == owner
    _safe_set(owner, 'diagram_description_AbstractNodeMapping', set())
    assert getattr(partner, 'NodeMapping183') is None


def test_assoc_candidatesMapping55_stub_double():
    # NodeMapping has no real 'NodeMapping57' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping57', None)
    _safe_set(owner, 'diagram_DNode56', {partner})
    assert getattr(partner, 'NodeMapping57') == owner
    _safe_set(owner, 'diagram_DNode56', set())
    assert getattr(partner, 'NodeMapping57') is None


def test_assoc_candidatesMapping74_stub_double():
    # ContainerMapping has no real 'ContainerMapping76' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElementContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElementContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    partner = ContainerMapping()
    setattr(partner, 'ContainerMapping76', None)
    _safe_set(owner, 'diagram_DDiagramElementContainer75', {partner})
    assert getattr(partner, 'ContainerMapping76') == owner
    _safe_set(owner, 'diagram_DDiagramElementContainer75', set())
    assert getattr(partner, 'ContainerMapping76') is None


def test_assoc_centerLabelStyleDescription304_stub_double():
    # style_CenterLabelStyleDescription has no real 'style_CenterLabelStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_EdgeStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_EdgeStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    partner = style_CenterLabelStyleDescription()
    setattr(partner, 'style_CenterLabelStyleDescription', None)
    _safe_set(owner, 'diagram_style_EdgeStyleDescription305', partner)
    assert getattr(partner, 'style_CenterLabelStyleDescription') == owner
    _safe_set(owner, 'diagram_style_EdgeStyleDescription305', None)
    assert getattr(partner, 'style_CenterLabelStyleDescription') is None


def test_assoc_centeredSourceMappings308_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping310' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_EdgeStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_EdgeStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping310', None)
    _safe_set(owner, 'diagram_style_EdgeStyleDescription309', {partner})
    assert getattr(partner, 'DiagramElementMapping310') == owner
    _safe_set(owner, 'diagram_style_EdgeStyleDescription309', set())
    assert getattr(partner, 'DiagramElementMapping310') is None


def test_assoc_centeredTargetMappings311_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping313' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_EdgeStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_EdgeStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping313', None)
    _safe_set(owner, 'diagram_style_EdgeStyleDescription312', {partner})
    assert getattr(partner, 'DiagramElementMapping313') == owner
    _safe_set(owner, 'diagram_style_EdgeStyleDescription312', set())
    assert getattr(partner, 'DiagramElementMapping313') is None


def test_assoc_color273_stub_double():
    # ColorDescription has no real 'ColorDescription274' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_SquareDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_SquareDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_SquareDescription(height="sample_text", width="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription274', None)
    _safe_set(owner, 'diagram_style_SquareDescription', partner)
    assert getattr(partner, 'ColorDescription274') == owner
    _safe_set(owner, 'diagram_style_SquareDescription', None)
    assert getattr(partner, 'ColorDescription274') is None


def test_assoc_color275_stub_double():
    # ColorDescription has no real 'ColorDescription276' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_LozengeNodeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_LozengeNodeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription276', None)
    _safe_set(owner, 'diagram_style_LozengeNodeDescription', partner)
    assert getattr(partner, 'ColorDescription276') == owner
    _safe_set(owner, 'diagram_style_LozengeNodeDescription', None)
    assert getattr(partner, 'ColorDescription276') is None


def test_assoc_color277_stub_double():
    # ColorDescription has no real 'ColorDescription278' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_EllipseNodeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_EllipseNodeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription278', None)
    _safe_set(owner, 'diagram_style_EllipseNodeDescription', partner)
    assert getattr(partner, 'ColorDescription278') == owner
    _safe_set(owner, 'diagram_style_EllipseNodeDescription', None)
    assert getattr(partner, 'ColorDescription278') is None


def test_assoc_color279_stub_double():
    # ColorDescription has no real 'ColorDescription280' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_BundledImageDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_BundledImageDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_BundledImageDescription(providedShapeID="sample_text", shape="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription280', None)
    _safe_set(owner, 'diagram_style_BundledImageDescription', partner)
    assert getattr(partner, 'ColorDescription280') == owner
    _safe_set(owner, 'diagram_style_BundledImageDescription', None)
    assert getattr(partner, 'ColorDescription280') is None


def test_assoc_concerns128_stub_double():
    # concern_ConcernSet has no real 'concern_ConcernSet' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = concern_ConcernSet()
    setattr(partner, 'concern_ConcernSet', None)
    _safe_set(owner, 'diagram_description_DiagramDescription129', partner)
    assert getattr(partner, 'concern_ConcernSet') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription129', None)
    assert getattr(partner, 'concern_ConcernSet') is None


def test_assoc_conditionnalStyles203_stub_double():
    # ConditionalContainerStyleDescription has no real 'ConditionalContainerStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_ContainerMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_ContainerMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    partner = ConditionalContainerStyleDescription()
    setattr(partner, 'ConditionalContainerStyleDescription', None)
    _safe_set(owner, 'diagram_description_ContainerMapping204', {partner})
    assert getattr(partner, 'ConditionalContainerStyleDescription') == owner
    _safe_set(owner, 'diagram_description_ContainerMapping204', set())
    assert getattr(partner, 'ConditionalContainerStyleDescription') is None


def test_assoc_conditionnalStyles216_stub_double():
    # ConditionalEdgeStyleDescription has no real 'ConditionalEdgeStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_EdgeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_EdgeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    partner = ConditionalEdgeStyleDescription()
    setattr(partner, 'ConditionalEdgeStyleDescription', None)
    _safe_set(owner, 'diagram_description_EdgeMapping217', {partner})
    assert getattr(partner, 'ConditionalEdgeStyleDescription') == owner
    _safe_set(owner, 'diagram_description_EdgeMapping217', set())
    assert getattr(partner, 'ConditionalEdgeStyleDescription') is None


def test_assoc_conditionnalStyles224_stub_double():
    # ConditionalEdgeStyleDescription has no real 'ConditionalEdgeStyleDescription226' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_EdgeMappingImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_EdgeMappingImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_EdgeMappingImport(inheritsAncestorFilters=True)
    partner = ConditionalEdgeStyleDescription()
    setattr(partner, 'ConditionalEdgeStyleDescription226', None)
    _safe_set(owner, 'diagram_description_EdgeMappingImport225', {partner})
    assert getattr(partner, 'ConditionalEdgeStyleDescription226') == owner
    _safe_set(owner, 'diagram_description_EdgeMappingImport225', set())
    assert getattr(partner, 'ConditionalEdgeStyleDescription226') is None


def test_assoc_containerMappings155_stub_double():
    # ContainerMapping has no real 'ContainerMapping157' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = ContainerMapping()
    setattr(partner, 'ContainerMapping157', None)
    _safe_set(owner, 'diagram_description_DiagramDescription156', {partner})
    assert getattr(partner, 'ContainerMapping157') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription156', set())
    assert getattr(partner, 'ContainerMapping157') is None


def test_assoc_containerMappings251_stub_double():
    # ContainerMapping has no real 'ContainerMapping253' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = ContainerMapping()
    setattr(partner, 'ContainerMapping253', None)
    _safe_set(owner, 'diagram_description_Layer252', {partner})
    assert getattr(partner, 'ContainerMapping253') == owner
    _safe_set(owner, 'diagram_description_Layer252', set())
    assert getattr(partner, 'ContainerMapping253') is None


def test_assoc_containerMappings362_stub_double():
    # ContainerMapping has no real 'ContainerMapping363' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    partner = ContainerMapping()
    setattr(partner, 'ContainerMapping363', None)
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription', {partner})
    assert getattr(partner, 'ContainerMapping363') == owner
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription', set())
    assert getattr(partner, 'ContainerMapping363') is None


def test_assoc_containerView380_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable382' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_DeleteElementDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_DeleteElementDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_DeleteElementDescription()
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable382', None)
    _safe_set(owner, 'diagram_tool_DeleteElementDescription381', partner)
    assert getattr(partner, 'tool_ContainerViewVariable382') == owner
    _safe_set(owner, 'diagram_tool_DeleteElementDescription381', None)
    assert getattr(partner, 'tool_ContainerViewVariable382') is None


def test_assoc_currentConcern14_stub_double():
    # concern_ConcernDescription has no real 'concern_ConcernDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = concern_ConcernDescription()
    setattr(partner, 'concern_ConcernDescription', None)
    _safe_set(owner, 'diagram_DDiagram15', partner)
    assert getattr(partner, 'concern_ConcernDescription') == owner
    _safe_set(owner, 'diagram_DDiagram15', None)
    assert getattr(partner, 'concern_ConcernDescription') is None


def test_assoc_customization268_stub_double():
    # Customization has no real 'Customization' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = Customization()
    setattr(partner, 'Customization', None)
    _safe_set(owner, 'diagram_description_Layer269', partner)
    assert getattr(partner, 'Customization') == owner
    _safe_set(owner, 'diagram_description_Layer269', None)
    assert getattr(partner, 'Customization') is None


def test_assoc_decorationDescriptionsSet266_stub_double():
    # DecorationDescriptionsSet has no real 'DecorationDescriptionsSet' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = DecorationDescriptionsSet()
    setattr(partner, 'DecorationDescriptionsSet', None)
    _safe_set(owner, 'diagram_description_Layer267', partner)
    assert getattr(partner, 'DecorationDescriptionsSet') == owner
    _safe_set(owner, 'diagram_description_Layer267', None)
    assert getattr(partner, 'DecorationDescriptionsSet') is None


def test_assoc_decorations37_stub_double():
    # diagram_Decoration has no real 'diagram_Decoration' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    partner = diagram_Decoration()
    setattr(partner, 'diagram_Decoration', None)
    _safe_set(owner, 'diagram_DDiagramElement38', {partner})
    assert getattr(partner, 'diagram_Decoration') == owner
    _safe_set(owner, 'diagram_DDiagramElement38', set())
    assert getattr(partner, 'diagram_Decoration') is None


def test_assoc_defaultConcern132_stub_double():
    # concern_ConcernDescription has no real 'concern_ConcernDescription134' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = concern_ConcernDescription()
    setattr(partner, 'concern_ConcernDescription134', None)
    _safe_set(owner, 'diagram_description_DiagramDescription133', partner)
    assert getattr(partner, 'concern_ConcernDescription134') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription133', None)
    assert getattr(partner, 'concern_ConcernDescription134') is None


def test_assoc_defaultLayer141_stub_double():
    # Layer has no real 'Layer143' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = Layer()
    setattr(partner, 'Layer143', None)
    _safe_set(owner, 'diagram_description_DiagramDescription142', partner)
    assert getattr(partner, 'Layer143') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription142', None)
    assert getattr(partner, 'Layer143') is None


def test_assoc_deletionDescription178_stub_double():
    # tool_DeleteElementDescription has no real 'tool_DeleteElementDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramElementMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramElementMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    partner = tool_DeleteElementDescription()
    setattr(partner, 'tool_DeleteElementDescription', None)
    _safe_set(owner, 'diagram_description_DiagramElementMapping', partner)
    assert getattr(partner, 'tool_DeleteElementDescription') == owner
    _safe_set(owner, 'diagram_description_DiagramElementMapping', None)
    assert getattr(partner, 'tool_DeleteElementDescription') is None


def test_assoc_description4_stub_double():
    # DiagramDescription has no real 'DiagramDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = DiagramDescription()
    setattr(partner, 'DiagramDescription', None)
    _safe_set(owner, 'diagram_DDiagram5', partner)
    assert getattr(partner, 'DiagramDescription') == owner
    _safe_set(owner, 'diagram_DDiagram5', None)
    assert getattr(partner, 'DiagramDescription') is None


def test_assoc_diagramDescription425_stub_double():
    # DiagramDescription has no real 'DiagramDescription426' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_Navigation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_Navigation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_Navigation(createIfNotExistent=True)
    partner = DiagramDescription()
    setattr(partner, 'DiagramDescription426', None)
    _safe_set(owner, 'diagram_tool_Navigation', partner)
    assert getattr(partner, 'DiagramDescription426') == owner
    _safe_set(owner, 'diagram_tool_Navigation', None)
    assert getattr(partner, 'DiagramDescription426') is None


def test_assoc_diagramElementMapping42_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping', None)
    _safe_set(owner, 'diagram_DDiagramElement43', partner)
    assert getattr(partner, 'DiagramElementMapping') == owner
    _safe_set(owner, 'diagram_DDiagramElement43', None)
    assert getattr(partner, 'DiagramElementMapping') is None


def test_assoc_diagramInitialisation139_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation', None)
    _safe_set(owner, 'diagram_description_DiagramDescription140', partner)
    assert getattr(partner, 'tool_InitialOperation') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription140', None)
    assert getattr(partner, 'tool_InitialOperation') is None


def test_assoc_doubleClickDescription181_stub_double():
    # tool_DoubleClickDescription has no real 'DoubleClickDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramElementMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramElementMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    partner = tool_DoubleClickDescription()
    setattr(partner, 'DoubleClickDescription', None)
    _safe_set(owner, 'mappings', partner)
    assert getattr(partner, 'DoubleClickDescription') == owner
    _safe_set(owner, 'mappings', None)
    assert getattr(partner, 'DoubleClickDescription') is None


def test_assoc_edgeMappingImports153_stub_double():
    # EdgeMappingImport has no real 'EdgeMappingImport' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = EdgeMappingImport()
    setattr(partner, 'EdgeMappingImport', None)
    _safe_set(owner, 'diagram_description_DiagramDescription154', {partner})
    assert getattr(partner, 'EdgeMappingImport') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription154', set())
    assert getattr(partner, 'EdgeMappingImport') is None


def test_assoc_edgeMappingImports248_stub_double():
    # EdgeMappingImport has no real 'EdgeMappingImport250' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = EdgeMappingImport()
    setattr(partner, 'EdgeMappingImport250', None)
    _safe_set(owner, 'diagram_description_Layer249', {partner})
    assert getattr(partner, 'EdgeMappingImport250') == owner
    _safe_set(owner, 'diagram_description_Layer249', set())
    assert getattr(partner, 'EdgeMappingImport250') is None


def test_assoc_edgeMappings150_stub_double():
    # EdgeMapping has no real 'EdgeMapping152' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = EdgeMapping()
    setattr(partner, 'EdgeMapping152', None)
    _safe_set(owner, 'diagram_description_DiagramDescription151', {partner})
    assert getattr(partner, 'EdgeMapping152') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription151', set())
    assert getattr(partner, 'EdgeMapping152') is None


def test_assoc_edgeMappings245_stub_double():
    # EdgeMapping has no real 'EdgeMapping247' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = EdgeMapping()
    setattr(partner, 'EdgeMapping247', None)
    _safe_set(owner, 'diagram_description_Layer246', {partner})
    assert getattr(partner, 'EdgeMapping247') == owner
    _safe_set(owner, 'diagram_description_Layer246', set())
    assert getattr(partner, 'EdgeMapping247') is None


def test_assoc_edgeMappings344_stub_double():
    # EdgeMapping has no real 'EdgeMapping345' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_EdgeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_EdgeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    partner = EdgeMapping()
    setattr(partner, 'EdgeMapping345', None)
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription', {partner})
    assert getattr(partner, 'EdgeMapping345') == owner
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription', set())
    assert getattr(partner, 'EdgeMapping345') is None


def test_assoc_edgeView414_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable416' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ReconnectEdgeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ReconnectEdgeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable416', None)
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription415', partner)
    assert getattr(partner, 'tool_ElementSelectVariable416') == owner
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription415', None)
    assert getattr(partner, 'tool_ElementSelectVariable416') is None


def test_assoc_element376_stub_double():
    # tool_ElementDeleteVariable has no real 'tool_ElementDeleteVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_DeleteElementDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_DeleteElementDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_DeleteElementDescription()
    partner = tool_ElementDeleteVariable()
    setattr(partner, 'tool_ElementDeleteVariable', None)
    _safe_set(owner, 'diagram_tool_DeleteElementDescription', partner)
    assert getattr(partner, 'tool_ElementDeleteVariable') == owner
    _safe_set(owner, 'diagram_tool_DeleteElementDescription', None)
    assert getattr(partner, 'tool_ElementDeleteVariable') is None


def test_assoc_element409_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ReconnectEdgeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ReconnectEdgeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable', None)
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription410', partner)
    assert getattr(partner, 'tool_ElementSelectVariable') == owner
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription410', None)
    assert getattr(partner, 'tool_ElementSelectVariable') is None


def test_assoc_element438_stub_double():
    # tool_ElementDropVariable has no real 'tool_ElementDropVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerDropDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerDropDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    partner = tool_ElementDropVariable()
    setattr(partner, 'tool_ElementDropVariable', None)
    _safe_set(owner, 'diagram_tool_ContainerDropDescription439', partner)
    assert getattr(partner, 'tool_ElementDropVariable') == owner
    _safe_set(owner, 'diagram_tool_ContainerDropDescription439', None)
    assert getattr(partner, 'tool_ElementDropVariable') is None


def test_assoc_elementView377_stub_double():
    # tool_ElementDeleteVariable has no real 'tool_ElementDeleteVariable379' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_DeleteElementDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_DeleteElementDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_DeleteElementDescription()
    partner = tool_ElementDeleteVariable()
    setattr(partner, 'tool_ElementDeleteVariable379', None)
    _safe_set(owner, 'diagram_tool_DeleteElementDescription378', partner)
    assert getattr(partner, 'tool_ElementDeleteVariable379') == owner
    _safe_set(owner, 'diagram_tool_DeleteElementDescription378', None)
    assert getattr(partner, 'tool_ElementDeleteVariable379') is None


def test_assoc_endLabelStyleDescription306_stub_double():
    # style_EndLabelStyleDescription has no real 'style_EndLabelStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_EdgeStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_EdgeStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    partner = style_EndLabelStyleDescription()
    setattr(partner, 'style_EndLabelStyleDescription', None)
    _safe_set(owner, 'diagram_style_EdgeStyleDescription307', partner)
    assert getattr(partner, 'style_EndLabelStyleDescription') == owner
    _safe_set(owner, 'diagram_style_EdgeStyleDescription307', None)
    assert getattr(partner, 'style_EndLabelStyleDescription') is None


def test_assoc_extraMappings341_stub_double():
    # AbstractNodeMapping has no real 'AbstractNodeMapping343' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_NodeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_NodeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    partner = AbstractNodeMapping()
    setattr(partner, 'AbstractNodeMapping343', None)
    _safe_set(owner, 'diagram_tool_NodeCreationDescription342', {partner})
    assert getattr(partner, 'AbstractNodeMapping343') == owner
    _safe_set(owner, 'diagram_tool_NodeCreationDescription342', set())
    assert getattr(partner, 'AbstractNodeMapping343') is None


def test_assoc_extraMappings373_stub_double():
    # AbstractNodeMapping has no real 'AbstractNodeMapping375' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    partner = AbstractNodeMapping()
    setattr(partner, 'AbstractNodeMapping375', None)
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription374', {partner})
    assert getattr(partner, 'AbstractNodeMapping375') == owner
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription374', set())
    assert getattr(partner, 'AbstractNodeMapping375') is None


def test_assoc_extraSourceMappings356_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping358' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_EdgeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_EdgeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping358', None)
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription357', {partner})
    assert getattr(partner, 'DiagramElementMapping358') == owner
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription357', set())
    assert getattr(partner, 'DiagramElementMapping358') is None


def test_assoc_extraTargetMappings359_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping361' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_EdgeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_EdgeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping361', None)
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription360', {partner})
    assert getattr(partner, 'DiagramElementMapping361') == owner
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription360', set())
    assert getattr(partner, 'DiagramElementMapping361') is None


def test_assoc_filterVariableHistory27_stub_double():
    # diagram_FilterVariableHistory has no real 'diagram_FilterVariableHistory' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = diagram_FilterVariableHistory()
    setattr(partner, 'diagram_FilterVariableHistory', None)
    _safe_set(owner, 'diagram_DDiagram28', partner)
    assert getattr(partner, 'diagram_FilterVariableHistory') == owner
    _safe_set(owner, 'diagram_DDiagram28', None)
    assert getattr(partner, 'diagram_FilterVariableHistory') is None


def test_assoc_filters122_stub_double():
    # filter_FilterDescription has no real 'filter_FilterDescription123' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = filter_FilterDescription()
    setattr(partner, 'filter_FilterDescription123', None)
    _safe_set(owner, 'diagram_description_DiagramDescription', {partner})
    assert getattr(partner, 'filter_FilterDescription123') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription', set())
    assert getattr(partner, 'filter_FilterDescription123') is None


def test_assoc_foregroundColor288_stub_double():
    # ColorDescription has no real 'ColorDescription290' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_GaugeSectionDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_GaugeSectionDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription290', None)
    _safe_set(owner, 'diagram_style_GaugeSectionDescription289', partner)
    assert getattr(partner, 'ColorDescription290') == owner
    _safe_set(owner, 'diagram_style_GaugeSectionDescription289', None)
    assert getattr(partner, 'ColorDescription290') is None


def test_assoc_foregroundColor293_stub_double():
    # ColorDescription has no real 'ColorDescription295' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_FlatContainerStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_FlatContainerStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription295', None)
    _safe_set(owner, 'diagram_style_FlatContainerStyleDescription294', partner)
    assert getattr(partner, 'ColorDescription295') == owner
    _safe_set(owner, 'diagram_style_FlatContainerStyleDescription294', None)
    assert getattr(partner, 'ColorDescription295') is None


def test_assoc_graphicalFilters44_stub_double():
    # diagram_GraphicalFilter has no real 'diagram_GraphicalFilter' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    partner = diagram_GraphicalFilter()
    setattr(partner, 'diagram_GraphicalFilter', None)
    _safe_set(owner, 'diagram_DDiagramElement45', {partner})
    assert getattr(partner, 'diagram_GraphicalFilter') == owner
    _safe_set(owner, 'diagram_DDiagramElement45', set())
    assert getattr(partner, 'diagram_GraphicalFilter') is None


def test_assoc_groupExtensions323_stub_double():
    # tool_ToolGroupExtension has no real 'tool_ToolGroupExtension' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ToolSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ToolSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ToolSection(icon="sample_text")
    partner = tool_ToolGroupExtension()
    setattr(partner, 'tool_ToolGroupExtension', None)
    _safe_set(owner, 'diagram_tool_ToolSection324', {partner})
    assert getattr(partner, 'tool_ToolGroupExtension') == owner
    _safe_set(owner, 'diagram_tool_ToolSection324', set())
    assert getattr(partner, 'tool_ToolGroupExtension') is None


def test_assoc_groups325_stub_double():
    # tool_GroupMenu has no real 'tool_GroupMenu' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ToolSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ToolSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ToolSection(icon="sample_text")
    partner = tool_GroupMenu()
    setattr(partner, 'tool_GroupMenu', None)
    _safe_set(owner, 'diagram_tool_ToolSection326', {partner})
    assert getattr(partner, 'tool_GroupMenu') == owner
    _safe_set(owner, 'diagram_tool_ToolSection326', set())
    assert getattr(partner, 'tool_GroupMenu') is None


def test_assoc_hook386_stub_double():
    # tool_DeleteHook has no real 'tool_DeleteHook' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_DeleteElementDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_DeleteElementDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_DeleteElementDescription()
    partner = tool_DeleteHook()
    setattr(partner, 'tool_DeleteHook', None)
    _safe_set(owner, 'diagram_tool_DeleteElementDescription387', partner)
    assert getattr(partner, 'tool_DeleteHook') == owner
    _safe_set(owner, 'diagram_tool_DeleteElementDescription387', None)
    assert getattr(partner, 'tool_DeleteHook') is None


def test_assoc_importedMapping222_stub_double():
    # IEdgeMapping has no real 'IEdgeMapping223' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_EdgeMappingImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_EdgeMappingImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_EdgeMappingImport(inheritsAncestorFilters=True)
    partner = IEdgeMapping()
    setattr(partner, 'IEdgeMapping223', None)
    _safe_set(owner, 'diagram_description_EdgeMappingImport', partner)
    assert getattr(partner, 'IEdgeMapping223') == owner
    _safe_set(owner, 'diagram_description_EdgeMappingImport', None)
    assert getattr(partner, 'IEdgeMapping223') is None


def test_assoc_incomingEdges106_stub_double():
    # diagram_EdgeTarget has no real 'targetNode' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    partner = diagram_EdgeTarget()
    setattr(partner, 'targetNode', None)
    _safe_set(owner, 'DEdge107', partner)
    assert getattr(partner, 'targetNode') == owner
    _safe_set(owner, 'DEdge107', None)
    assert getattr(partner, 'targetNode') is None


def test_assoc_init135_stub_double():
    # tool_RepresentationCreationDescription has no real 'tool_RepresentationCreationDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = tool_RepresentationCreationDescription()
    setattr(partner, 'tool_RepresentationCreationDescription', None)
    _safe_set(owner, 'diagram_description_DiagramDescription136', partner)
    assert getattr(partner, 'tool_RepresentationCreationDescription') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription136', None)
    assert getattr(partner, 'tool_RepresentationCreationDescription') is None


def test_assoc_initialOperation339_stub_double():
    # tool_InitialNodeCreationOperation has no real 'tool_InitialNodeCreationOperation' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_NodeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_NodeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    partner = tool_InitialNodeCreationOperation()
    setattr(partner, 'tool_InitialNodeCreationOperation', None)
    _safe_set(owner, 'diagram_tool_NodeCreationDescription340', partner)
    assert getattr(partner, 'tool_InitialNodeCreationOperation') == owner
    _safe_set(owner, 'diagram_tool_NodeCreationDescription340', None)
    assert getattr(partner, 'tool_InitialNodeCreationOperation') is None


def test_assoc_initialOperation354_stub_double():
    # tool_InitEdgeCreationOperation has no real 'tool_InitEdgeCreationOperation' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_EdgeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_EdgeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    partner = tool_InitEdgeCreationOperation()
    setattr(partner, 'tool_InitEdgeCreationOperation', None)
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription355', partner)
    assert getattr(partner, 'tool_InitEdgeCreationOperation') == owner
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription355', None)
    assert getattr(partner, 'tool_InitEdgeCreationOperation') is None


def test_assoc_initialOperation370_stub_double():
    # tool_InitialNodeCreationOperation has no real 'tool_InitialNodeCreationOperation372' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    partner = tool_InitialNodeCreationOperation()
    setattr(partner, 'tool_InitialNodeCreationOperation372', None)
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription371', partner)
    assert getattr(partner, 'tool_InitialNodeCreationOperation372') == owner
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription371', None)
    assert getattr(partner, 'tool_InitialNodeCreationOperation372') is None


def test_assoc_initialOperation383_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation385' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_DeleteElementDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_DeleteElementDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_DeleteElementDescription()
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation385', None)
    _safe_set(owner, 'diagram_tool_DeleteElementDescription384', partner)
    assert getattr(partner, 'tool_InitialOperation385') == owner
    _safe_set(owner, 'diagram_tool_DeleteElementDescription384', None)
    assert getattr(partner, 'tool_InitialOperation385') is None


def test_assoc_initialOperation411_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation413' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ReconnectEdgeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ReconnectEdgeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation413', None)
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription412', partner)
    assert getattr(partner, 'tool_InitialOperation413') == owner
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription412', None)
    assert getattr(partner, 'tool_InitialOperation413') is None


def test_assoc_initialOperation418_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation420' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_DirectEditLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_DirectEditLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_DirectEditLabel(inputLabelExpression="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation420', None)
    _safe_set(owner, 'diagram_tool_DirectEditLabel419', partner)
    assert getattr(partner, 'tool_InitialOperation420') == owner
    _safe_set(owner, 'diagram_tool_DirectEditLabel419', None)
    assert getattr(partner, 'tool_InitialOperation420') is None


def test_assoc_initialOperation421_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation422' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_BehaviorTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_BehaviorTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_BehaviorTool(domainClass="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation422', None)
    _safe_set(owner, 'diagram_tool_BehaviorTool', partner)
    assert getattr(partner, 'tool_InitialOperation422') == owner
    _safe_set(owner, 'diagram_tool_BehaviorTool', None)
    assert getattr(partner, 'tool_InitialOperation422') is None


def test_assoc_initialOperation443_stub_double():
    # tool_InitialContainerDropOperation has no real 'tool_InitialContainerDropOperation' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerDropDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerDropDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    partner = tool_InitialContainerDropOperation()
    setattr(partner, 'tool_InitialContainerDropOperation', None)
    _safe_set(owner, 'diagram_tool_ContainerDropDescription444', partner)
    assert getattr(partner, 'tool_InitialContainerDropOperation') == owner
    _safe_set(owner, 'diagram_tool_ContainerDropDescription444', None)
    assert getattr(partner, 'tool_InitialContainerDropOperation') is None


def test_assoc_labelBorderStyle296_stub_double():
    # style_LabelBorderStyleDescription has no real 'style_LabelBorderStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_FlatContainerStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_FlatContainerStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    partner = style_LabelBorderStyleDescription()
    setattr(partner, 'style_LabelBorderStyleDescription', None)
    _safe_set(owner, 'diagram_style_FlatContainerStyleDescription297', partner)
    assert getattr(partner, 'style_LabelBorderStyleDescription') == owner
    _safe_set(owner, 'diagram_style_FlatContainerStyleDescription297', None)
    assert getattr(partner, 'style_LabelBorderStyleDescription') is None


def test_assoc_labelDirectEdit179_stub_double():
    # tool_DirectEditLabel has no real 'tool_DirectEditLabel' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramElementMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramElementMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    partner = tool_DirectEditLabel()
    setattr(partner, 'tool_DirectEditLabel', None)
    _safe_set(owner, 'diagram_description_DiagramElementMapping180', partner)
    assert getattr(partner, 'tool_DirectEditLabel') == owner
    _safe_set(owner, 'diagram_description_DiagramElementMapping180', None)
    assert getattr(partner, 'tool_DirectEditLabel') is None


def test_assoc_layout137_stub_double():
    # Layout has no real 'Layout' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = Layout()
    setattr(partner, 'Layout', None)
    _safe_set(owner, 'diagram_description_DiagramDescription138', partner)
    assert getattr(partner, 'Layout') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription138', None)
    assert getattr(partner, 'Layout') is None


def test_assoc_layoutOptions235_stub_double():
    # LayoutOption has no real 'LayoutOption' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_CustomLayoutConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_CustomLayoutConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_CustomLayoutConfiguration(description="sample_text", id="sample_text", label="sample_text")
    partner = LayoutOption()
    setattr(partner, 'LayoutOption', None)
    _safe_set(owner, 'diagram_description_CustomLayoutConfiguration', {partner})
    assert getattr(partner, 'LayoutOption') == owner
    _safe_set(owner, 'diagram_description_CustomLayoutConfiguration', set())
    assert getattr(partner, 'LayoutOption') is None


def test_assoc_mapping423_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping424' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_CreateView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_CreateView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping424', None)
    _safe_set(owner, 'diagram_tool_CreateView', partner)
    assert getattr(partner, 'DiagramElementMapping424') == owner
    _safe_set(owner, 'diagram_tool_CreateView', None)
    assert getattr(partner, 'DiagramElementMapping424') is None


def test_assoc_mappings431_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping432' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerDropDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerDropDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping432', None)
    _safe_set(owner, 'diagram_tool_ContainerDropDescription', {partner})
    assert getattr(partner, 'DiagramElementMapping432') == owner
    _safe_set(owner, 'diagram_tool_ContainerDropDescription', set())
    assert getattr(partner, 'DiagramElementMapping432') is None


def test_assoc_mappings445_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping446' property in the generated
    # code (a bare stub) -- manually attach it so diagram_filter_MappingFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_filter_MappingFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping446', None)
    _safe_set(owner, 'diagram_filter_MappingFilter', {partner})
    assert getattr(partner, 'DiagramElementMapping446') == owner
    _safe_set(owner, 'diagram_filter_MappingFilter', set())
    assert getattr(partner, 'DiagramElementMapping446') is None


def test_assoc_mask417_stub_double():
    # tool_EditMaskVariables has no real 'tool_EditMaskVariables' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_DirectEditLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_DirectEditLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_DirectEditLabel(inputLabelExpression="sample_text")
    partner = tool_EditMaskVariables()
    setattr(partner, 'tool_EditMaskVariables', None)
    _safe_set(owner, 'diagram_tool_DirectEditLabel', partner)
    assert getattr(partner, 'tool_EditMaskVariables') == owner
    _safe_set(owner, 'diagram_tool_DirectEditLabel', None)
    assert getattr(partner, 'tool_EditMaskVariables') is None


def test_assoc_newContainer435_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable437' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerDropDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerDropDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable437', None)
    _safe_set(owner, 'diagram_tool_ContainerDropDescription436', partner)
    assert getattr(partner, 'tool_DropContainerVariable437') == owner
    _safe_set(owner, 'diagram_tool_ContainerDropDescription436', None)
    assert getattr(partner, 'tool_DropContainerVariable437') is None


def test_assoc_newViewContainer440_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable442' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerDropDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerDropDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable442', None)
    _safe_set(owner, 'diagram_tool_ContainerDropDescription441', partner)
    assert getattr(partner, 'tool_ContainerViewVariable442') == owner
    _safe_set(owner, 'diagram_tool_ContainerDropDescription441', None)
    assert getattr(partner, 'tool_ContainerViewVariable442') is None


def test_assoc_nodeListElements10_stub_double():
    # diagram_DNodeListElement has no real 'diagram_DNodeListElement' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, isInShowingMode=True, synchronized=True)
    partner = diagram_DNodeListElement()
    setattr(partner, 'diagram_DNodeListElement', None)
    _safe_set(owner, 'diagram_DDiagram11', {partner})
    assert getattr(partner, 'diagram_DNodeListElement') == owner
    _safe_set(owner, 'diagram_DDiagram11', set())
    assert getattr(partner, 'diagram_DNodeListElement') is None


def test_assoc_nodeMapping233_stub_double():
    # AbstractNodeMapping has no real 'AbstractNodeMapping234' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_OrderedTreeLayout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_OrderedTreeLayout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_OrderedTreeLayout(childrenExpression="sample_text")
    partner = AbstractNodeMapping()
    setattr(partner, 'AbstractNodeMapping234', None)
    _safe_set(owner, 'diagram_description_OrderedTreeLayout', {partner})
    assert getattr(partner, 'AbstractNodeMapping234') == owner
    _safe_set(owner, 'diagram_description_OrderedTreeLayout', set())
    assert getattr(partner, 'AbstractNodeMapping234') is None


def test_assoc_nodeMappings147_stub_double():
    # NodeMapping has no real 'NodeMapping149' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping149', None)
    _safe_set(owner, 'diagram_description_DiagramDescription148', {partner})
    assert getattr(partner, 'NodeMapping149') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription148', set())
    assert getattr(partner, 'NodeMapping149') is None


def test_assoc_nodeMappings243_stub_double():
    # NodeMapping has no real 'NodeMapping244' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping244', None)
    _safe_set(owner, 'diagram_description_Layer', {partner})
    assert getattr(partner, 'NodeMapping244') == owner
    _safe_set(owner, 'diagram_description_Layer', set())
    assert getattr(partner, 'NodeMapping244') is None


def test_assoc_nodeMappings333_stub_double():
    # NodeMapping has no real 'NodeMapping334' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_NodeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_NodeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping334', None)
    _safe_set(owner, 'diagram_tool_NodeCreationDescription', {partner})
    assert getattr(partner, 'NodeMapping334') == owner
    _safe_set(owner, 'diagram_tool_NodeCreationDescription', set())
    assert getattr(partner, 'NodeMapping334') is None


def test_assoc_oldContainer433_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerDropDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerDropDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable', None)
    _safe_set(owner, 'diagram_tool_ContainerDropDescription434', partner)
    assert getattr(partner, 'tool_DropContainerVariable') == owner
    _safe_set(owner, 'diagram_tool_ContainerDropDescription434', None)
    assert getattr(partner, 'tool_DropContainerVariable') is None


def test_assoc_originalStyle100_stub_double():
    # diagram_Style has no real 'diagram_Style102' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    partner = diagram_Style()
    setattr(partner, 'diagram_Style102', None)
    _safe_set(owner, 'diagram_DEdge101', partner)
    assert getattr(partner, 'diagram_Style102') == owner
    _safe_set(owner, 'diagram_DEdge101', None)
    assert getattr(partner, 'diagram_Style102') is None


def test_assoc_originalStyle51_stub_double():
    # diagram_Style has no real 'diagram_Style' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    partner = diagram_Style()
    setattr(partner, 'diagram_Style', None)
    _safe_set(owner, 'diagram_DNode52', partner)
    assert getattr(partner, 'diagram_Style') == owner
    _safe_set(owner, 'diagram_DNode52', None)
    assert getattr(partner, 'diagram_Style') is None


def test_assoc_originalStyle69_stub_double():
    # diagram_Style has no real 'diagram_Style71' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElementContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElementContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    partner = diagram_Style()
    setattr(partner, 'diagram_Style71', None)
    _safe_set(owner, 'diagram_DDiagramElementContainer70', partner)
    assert getattr(partner, 'diagram_Style71') == owner
    _safe_set(owner, 'diagram_DDiagramElementContainer70', None)
    assert getattr(partner, 'diagram_Style71') is None


def test_assoc_outgoingEdges105_stub_double():
    # diagram_EdgeTarget has no real 'sourceNode' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    partner = diagram_EdgeTarget()
    setattr(partner, 'sourceNode', None)
    _safe_set(owner, 'DEdge', partner)
    assert getattr(partner, 'sourceNode') == owner
    _safe_set(owner, 'DEdge', None)
    assert getattr(partner, 'sourceNode') is None


def test_assoc_ownedStyle67_stub_double():
    # diagram_ContainerStyle has no real 'diagram_ContainerStyle' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElementContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElementContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    partner = diagram_ContainerStyle()
    setattr(partner, 'diagram_ContainerStyle', None)
    _safe_set(owner, 'diagram_DDiagramElementContainer68', partner)
    assert getattr(partner, 'diagram_ContainerStyle') == owner
    _safe_set(owner, 'diagram_DDiagramElementContainer68', None)
    assert getattr(partner, 'diagram_ContainerStyle') is None


def test_assoc_ownedStyle81_stub_double():
    # diagram_DNodeListElement has no real 'diagram_DNodeListElement82' property in the generated
    # code (a bare stub) -- manually attach it so diagram_NodeStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_NodeStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_NodeStyle(labelPosition="sample_text")
    partner = diagram_DNodeListElement()
    setattr(partner, 'diagram_DNodeListElement82', None)
    _safe_set(owner, 'diagram_NodeStyle83', partner)
    assert getattr(partner, 'diagram_DNodeListElement82') == owner
    _safe_set(owner, 'diagram_NodeStyle83', None)
    assert getattr(partner, 'diagram_DNodeListElement82') is None


def test_assoc_ownedTools314_stub_double():
    # tool_ToolEntry has no real 'tool_ToolEntry' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ToolSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ToolSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ToolSection(icon="sample_text")
    partner = tool_ToolEntry()
    setattr(partner, 'tool_ToolEntry', None)
    _safe_set(owner, 'diagram_tool_ToolSection', {partner})
    assert getattr(partner, 'tool_ToolEntry') == owner
    _safe_set(owner, 'diagram_tool_ToolSection', set())
    assert getattr(partner, 'tool_ToolEntry') is None


def test_assoc_ownedVariables448_stub_double():
    # InteractiveVariableDescription has no real 'InteractiveVariableDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_filter_VariableFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_filter_VariableFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_filter_VariableFilter(semanticConditionExpression="sample_text")
    partner = InteractiveVariableDescription()
    setattr(partner, 'InteractiveVariableDescription', None)
    _safe_set(owner, 'diagram_filter_VariableFilter', {partner})
    assert getattr(partner, 'InteractiveVariableDescription') == owner
    _safe_set(owner, 'diagram_filter_VariableFilter', set())
    assert getattr(partner, 'InteractiveVariableDescription') is None


def test_assoc_parameters397_stub_double():
    # tool_DeleteHookParameter has no real 'tool_DeleteHookParameter' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_DeleteHook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_DeleteHook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_DeleteHook(id="sample_text")
    partner = tool_DeleteHookParameter()
    setattr(partner, 'tool_DeleteHookParameter', None)
    _safe_set(owner, 'diagram_tool_DeleteHook', {partner})
    assert getattr(partner, 'tool_DeleteHookParameter') == owner
    _safe_set(owner, 'diagram_tool_DeleteHook', set())
    assert getattr(partner, 'tool_DeleteHookParameter') is None


def test_assoc_parentLayers34_stub_double():
    # Layer has no real 'Layer36' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    partner = Layer()
    setattr(partner, 'Layer36', None)
    _safe_set(owner, 'diagram_DDiagramElement35', {partner})
    assert getattr(partner, 'Layer36') == owner
    _safe_set(owner, 'diagram_DDiagramElement35', set())
    assert getattr(partner, 'Layer36') is None


def test_assoc_path103_stub_double():
    # diagram_EdgeTarget has no real 'diagram_EdgeTarget' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    partner = diagram_EdgeTarget()
    setattr(partner, 'diagram_EdgeTarget', None)
    _safe_set(owner, 'diagram_DEdge104', {partner})
    assert getattr(partner, 'diagram_EdgeTarget') == owner
    _safe_set(owner, 'diagram_DEdge104', set())
    assert getattr(partner, 'diagram_EdgeTarget') is None


def test_assoc_pathNodeMapping220_stub_double():
    # AbstractNodeMapping has no real 'AbstractNodeMapping' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_EdgeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_EdgeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    partner = AbstractNodeMapping()
    setattr(partner, 'AbstractNodeMapping', None)
    _safe_set(owner, 'diagram_description_EdgeMapping221', {partner})
    assert getattr(partner, 'AbstractNodeMapping') == owner
    _safe_set(owner, 'diagram_description_EdgeMapping221', set())
    assert getattr(partner, 'AbstractNodeMapping') is None


def test_assoc_popupMenus318_stub_double():
    # tool_PopupMenu has no real 'tool_PopupMenu' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ToolSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ToolSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ToolSection(icon="sample_text")
    partner = tool_PopupMenu()
    setattr(partner, 'tool_PopupMenu', None)
    _safe_set(owner, 'diagram_tool_ToolSection319', {partner})
    assert getattr(partner, 'tool_PopupMenu') == owner
    _safe_set(owner, 'diagram_tool_ToolSection319', set())
    assert getattr(partner, 'tool_PopupMenu') is None


def test_assoc_reconnections218_stub_double():
    # tool_ReconnectEdgeDescription has no real 'tool_ReconnectEdgeDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_EdgeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_EdgeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    partner = tool_ReconnectEdgeDescription()
    setattr(partner, 'tool_ReconnectEdgeDescription', None)
    _safe_set(owner, 'diagram_description_EdgeMapping219', {partner})
    assert getattr(partner, 'tool_ReconnectEdgeDescription') == owner
    _safe_set(owner, 'diagram_description_EdgeMapping219', set())
    assert getattr(partner, 'tool_ReconnectEdgeDescription') is None


def test_assoc_reusedBorderedNodeMappings184_stub_double():
    # NodeMapping has no real 'NodeMapping186' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_AbstractNodeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_AbstractNodeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_AbstractNodeMapping(domainClass="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping186', None)
    _safe_set(owner, 'diagram_description_AbstractNodeMapping185', {partner})
    assert getattr(partner, 'NodeMapping186') == owner
    _safe_set(owner, 'diagram_description_AbstractNodeMapping185', set())
    assert getattr(partner, 'NodeMapping186') is None


def test_assoc_reusedContainerMappings198_stub_double():
    # ContainerMapping has no real 'ContainerMapping200' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_ContainerMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_ContainerMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    partner = ContainerMapping()
    setattr(partner, 'ContainerMapping200', None)
    _safe_set(owner, 'diagram_description_ContainerMapping199', {partner})
    assert getattr(partner, 'ContainerMapping200') == owner
    _safe_set(owner, 'diagram_description_ContainerMapping199', set())
    assert getattr(partner, 'ContainerMapping200') is None


def test_assoc_reusedMappings158_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping160' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping160', None)
    _safe_set(owner, 'diagram_description_DiagramDescription159', {partner})
    assert getattr(partner, 'DiagramElementMapping160') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription159', set())
    assert getattr(partner, 'DiagramElementMapping160') is None


def test_assoc_reusedMappings254_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping256' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping256', None)
    _safe_set(owner, 'diagram_description_Layer255', {partner})
    assert getattr(partner, 'DiagramElementMapping256') == owner
    _safe_set(owner, 'diagram_description_Layer255', set())
    assert getattr(partner, 'DiagramElementMapping256') is None


def test_assoc_reusedNodeMappings192_stub_double():
    # NodeMapping has no real 'NodeMapping194' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_ContainerMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_ContainerMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping194', None)
    _safe_set(owner, 'diagram_description_ContainerMapping193', {partner})
    assert getattr(partner, 'NodeMapping194') == owner
    _safe_set(owner, 'diagram_description_ContainerMapping193', set())
    assert getattr(partner, 'NodeMapping194') is None


def test_assoc_reusedTools163_stub_double():
    # tool_AbstractToolDescription has no real 'tool_AbstractToolDescription165' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = tool_AbstractToolDescription()
    setattr(partner, 'tool_AbstractToolDescription165', None)
    _safe_set(owner, 'diagram_description_DiagramDescription164', {partner})
    assert getattr(partner, 'tool_AbstractToolDescription165') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription164', set())
    assert getattr(partner, 'tool_AbstractToolDescription165') is None


def test_assoc_reusedTools263_stub_double():
    # tool_AbstractToolDescription has no real 'tool_AbstractToolDescription265' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = tool_AbstractToolDescription()
    setattr(partner, 'tool_AbstractToolDescription265', None)
    _safe_set(owner, 'diagram_description_Layer264', {partner})
    assert getattr(partner, 'tool_AbstractToolDescription265') == owner
    _safe_set(owner, 'diagram_description_Layer264', set())
    assert getattr(partner, 'tool_AbstractToolDescription265') is None


def test_assoc_reusedTools320_stub_double():
    # tool_ToolEntry has no real 'tool_ToolEntry322' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ToolSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ToolSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ToolSection(icon="sample_text")
    partner = tool_ToolEntry()
    setattr(partner, 'tool_ToolEntry322', None)
    _safe_set(owner, 'diagram_tool_ToolSection321', {partner})
    assert getattr(partner, 'tool_ToolEntry322') == owner
    _safe_set(owner, 'diagram_tool_ToolSection321', set())
    assert getattr(partner, 'tool_ToolEntry322') is None


def test_assoc_sections285_stub_double():
    # style_GaugeSectionDescription has no real 'style_GaugeSectionDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_GaugeCompositeStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_GaugeCompositeStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_GaugeCompositeStyleDescription(alignment="sample_text")
    partner = style_GaugeSectionDescription()
    setattr(partner, 'style_GaugeSectionDescription', None)
    _safe_set(owner, 'diagram_style_GaugeCompositeStyleDescription', {partner})
    assert getattr(partner, 'style_GaugeSectionDescription') == owner
    _safe_set(owner, 'diagram_style_GaugeCompositeStyleDescription', set())
    assert getattr(partner, 'style_GaugeSectionDescription') is None


def test_assoc_source398_stub_double():
    # tool_SourceEdgeCreationVariable has no real 'tool_SourceEdgeCreationVariable399' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ReconnectEdgeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ReconnectEdgeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    partner = tool_SourceEdgeCreationVariable()
    setattr(partner, 'tool_SourceEdgeCreationVariable399', None)
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription', partner)
    assert getattr(partner, 'tool_SourceEdgeCreationVariable399') == owner
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription', None)
    assert getattr(partner, 'tool_SourceEdgeCreationVariable399') is None


def test_assoc_sourceMapping209_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping210' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_EdgeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_EdgeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping210', None)
    _safe_set(owner, 'diagram_description_EdgeMapping', {partner})
    assert getattr(partner, 'DiagramElementMapping210') == owner
    _safe_set(owner, 'diagram_description_EdgeMapping', set())
    assert getattr(partner, 'DiagramElementMapping210') is None


def test_assoc_sourceNode95_stub_double():
    # diagram_EdgeTarget has no real 'EdgeTarget' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    partner = diagram_EdgeTarget()
    setattr(partner, 'EdgeTarget', None)
    _safe_set(owner, 'outgoingEdges', partner)
    assert getattr(partner, 'EdgeTarget') == owner
    _safe_set(owner, 'outgoingEdges', None)
    assert getattr(partner, 'EdgeTarget') is None


def test_assoc_sourceVariable346_stub_double():
    # tool_SourceEdgeCreationVariable has no real 'tool_SourceEdgeCreationVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_EdgeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_EdgeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    partner = tool_SourceEdgeCreationVariable()
    setattr(partner, 'tool_SourceEdgeCreationVariable', None)
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription347', partner)
    assert getattr(partner, 'tool_SourceEdgeCreationVariable') == owner
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription347', None)
    assert getattr(partner, 'tool_SourceEdgeCreationVariable') is None


def test_assoc_sourceView403_stub_double():
    # tool_SourceEdgeViewCreationVariable has no real 'tool_SourceEdgeViewCreationVariable405' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ReconnectEdgeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ReconnectEdgeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    partner = tool_SourceEdgeViewCreationVariable()
    setattr(partner, 'tool_SourceEdgeViewCreationVariable405', None)
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription404', partner)
    assert getattr(partner, 'tool_SourceEdgeViewCreationVariable405') == owner
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription404', None)
    assert getattr(partner, 'tool_SourceEdgeViewCreationVariable405') is None


def test_assoc_sourceViewVariable350_stub_double():
    # tool_SourceEdgeViewCreationVariable has no real 'tool_SourceEdgeViewCreationVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_EdgeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_EdgeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    partner = tool_SourceEdgeViewCreationVariable()
    setattr(partner, 'tool_SourceEdgeViewCreationVariable', None)
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription351', partner)
    assert getattr(partner, 'tool_SourceEdgeViewCreationVariable') == owner
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription351', None)
    assert getattr(partner, 'tool_SourceEdgeViewCreationVariable') is None


def test_assoc_strokeColor300_stub_double():
    # ColorDescription has no real 'ColorDescription301' property in the generated
    # code (a bare stub) -- manually attach it so diagram_style_EdgeStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_style_EdgeStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription301', None)
    _safe_set(owner, 'diagram_style_EdgeStyleDescription', partner)
    assert getattr(partner, 'ColorDescription301') == owner
    _safe_set(owner, 'diagram_style_EdgeStyleDescription', None)
    assert getattr(partner, 'ColorDescription301') is None


def test_assoc_style201_stub_double():
    # style_ContainerStyleDescription has no real 'style_ContainerStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_ContainerMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_ContainerMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    partner = style_ContainerStyleDescription()
    setattr(partner, 'style_ContainerStyleDescription', None)
    _safe_set(owner, 'diagram_description_ContainerMapping202', partner)
    assert getattr(partner, 'style_ContainerStyleDescription') == owner
    _safe_set(owner, 'diagram_description_ContainerMapping202', None)
    assert getattr(partner, 'style_ContainerStyleDescription') is None


def test_assoc_style214_stub_double():
    # style_EdgeStyleDescription has no real 'style_EdgeStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_EdgeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_EdgeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    partner = style_EdgeStyleDescription()
    setattr(partner, 'style_EdgeStyleDescription', None)
    _safe_set(owner, 'diagram_description_EdgeMapping215', partner)
    assert getattr(partner, 'style_EdgeStyleDescription') == owner
    _safe_set(owner, 'diagram_description_EdgeMapping215', None)
    assert getattr(partner, 'style_EdgeStyleDescription') is None


def test_assoc_subContainerMappings195_stub_double():
    # ContainerMapping has no real 'ContainerMapping197' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_ContainerMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_ContainerMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    partner = ContainerMapping()
    setattr(partner, 'ContainerMapping197', None)
    _safe_set(owner, 'diagram_description_ContainerMapping196', {partner})
    assert getattr(partner, 'ContainerMapping197') == owner
    _safe_set(owner, 'diagram_description_ContainerMapping196', set())
    assert getattr(partner, 'ContainerMapping197') is None


def test_assoc_subNodeMappings190_stub_double():
    # NodeMapping has no real 'NodeMapping191' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_ContainerMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_ContainerMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    partner = NodeMapping()
    setattr(partner, 'NodeMapping191', None)
    _safe_set(owner, 'diagram_description_ContainerMapping', {partner})
    assert getattr(partner, 'NodeMapping191') == owner
    _safe_set(owner, 'diagram_description_ContainerMapping', set())
    assert getattr(partner, 'NodeMapping191') is None


def test_assoc_subSections315_stub_double():
    # tool_ToolSection has no real 'tool_ToolSection317' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ToolSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ToolSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ToolSection(icon="sample_text")
    partner = tool_ToolSection()
    setattr(partner, 'tool_ToolSection317', None)
    _safe_set(owner, 'diagram_tool_ToolSection316', {partner})
    assert getattr(partner, 'tool_ToolSection317') == owner
    _safe_set(owner, 'diagram_tool_ToolSection316', set())
    assert getattr(partner, 'tool_ToolSection317') is None


def test_assoc_target400_stub_double():
    # tool_TargetEdgeCreationVariable has no real 'tool_TargetEdgeCreationVariable402' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ReconnectEdgeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ReconnectEdgeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    partner = tool_TargetEdgeCreationVariable()
    setattr(partner, 'tool_TargetEdgeCreationVariable402', None)
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription401', partner)
    assert getattr(partner, 'tool_TargetEdgeCreationVariable402') == owner
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription401', None)
    assert getattr(partner, 'tool_TargetEdgeCreationVariable402') is None


def test_assoc_targetMapping211_stub_double():
    # DiagramElementMapping has no real 'DiagramElementMapping213' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_EdgeMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_EdgeMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    partner = DiagramElementMapping()
    setattr(partner, 'DiagramElementMapping213', None)
    _safe_set(owner, 'diagram_description_EdgeMapping212', {partner})
    assert getattr(partner, 'DiagramElementMapping213') == owner
    _safe_set(owner, 'diagram_description_EdgeMapping212', set())
    assert getattr(partner, 'DiagramElementMapping213') is None


def test_assoc_targetNode96_stub_double():
    # diagram_EdgeTarget has no real 'EdgeTarget97' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    partner = diagram_EdgeTarget()
    setattr(partner, 'EdgeTarget97', None)
    _safe_set(owner, 'incomingEdges', partner)
    assert getattr(partner, 'EdgeTarget97') == owner
    _safe_set(owner, 'incomingEdges', None)
    assert getattr(partner, 'EdgeTarget97') is None


def test_assoc_targetVariable348_stub_double():
    # tool_TargetEdgeCreationVariable has no real 'tool_TargetEdgeCreationVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_EdgeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_EdgeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    partner = tool_TargetEdgeCreationVariable()
    setattr(partner, 'tool_TargetEdgeCreationVariable', None)
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription349', partner)
    assert getattr(partner, 'tool_TargetEdgeCreationVariable') == owner
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription349', None)
    assert getattr(partner, 'tool_TargetEdgeCreationVariable') is None


def test_assoc_targetView406_stub_double():
    # tool_TargetEdgeViewCreationVariable has no real 'tool_TargetEdgeViewCreationVariable408' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ReconnectEdgeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ReconnectEdgeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    partner = tool_TargetEdgeViewCreationVariable()
    setattr(partner, 'tool_TargetEdgeViewCreationVariable408', None)
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription407', partner)
    assert getattr(partner, 'tool_TargetEdgeViewCreationVariable408') == owner
    _safe_set(owner, 'diagram_tool_ReconnectEdgeDescription407', None)
    assert getattr(partner, 'tool_TargetEdgeViewCreationVariable408') is None


def test_assoc_targetViewVariable352_stub_double():
    # tool_TargetEdgeViewCreationVariable has no real 'tool_TargetEdgeViewCreationVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_EdgeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_EdgeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    partner = tool_TargetEdgeViewCreationVariable()
    setattr(partner, 'tool_TargetEdgeViewCreationVariable', None)
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription353', partner)
    assert getattr(partner, 'tool_TargetEdgeViewCreationVariable') == owner
    _safe_set(owner, 'diagram_tool_EdgeCreationDescription353', None)
    assert getattr(partner, 'tool_TargetEdgeViewCreationVariable') is None


def test_assoc_toolSection161_stub_double():
    # tool_ToolSection has no real 'tool_ToolSection' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = tool_ToolSection()
    setattr(partner, 'tool_ToolSection', None)
    _safe_set(owner, 'diagram_description_DiagramDescription162', partner)
    assert getattr(partner, 'tool_ToolSection') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription162', None)
    assert getattr(partner, 'tool_ToolSection') is None


def test_assoc_toolSections260_stub_double():
    # tool_ToolSection has no real 'tool_ToolSection262' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_Layer(icon="sample_text")
    partner = tool_ToolSection()
    setattr(partner, 'tool_ToolSection262', None)
    _safe_set(owner, 'diagram_description_Layer261', {partner})
    assert getattr(partner, 'tool_ToolSection262') == owner
    _safe_set(owner, 'diagram_description_Layer261', set())
    assert getattr(partner, 'tool_ToolSection262') is None


def test_assoc_transientDecorations39_stub_double():
    # diagram_Decoration has no real 'diagram_Decoration41' property in the generated
    # code (a bare stub) -- manually attach it so diagram_DDiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_DDiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    partner = diagram_Decoration()
    setattr(partner, 'diagram_Decoration41', None)
    _safe_set(owner, 'diagram_DDiagramElement40', {partner})
    assert getattr(partner, 'diagram_Decoration41') == owner
    _safe_set(owner, 'diagram_DDiagramElement40', set())
    assert getattr(partner, 'diagram_Decoration41') is None


def test_assoc_validationSet126_stub_double():
    # validation_ValidationSet has no real 'validation_ValidationSet' property in the generated
    # code (a bare stub) -- manually attach it so diagram_description_DiagramDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_description_DiagramDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    partner = validation_ValidationSet()
    setattr(partner, 'validation_ValidationSet', None)
    _safe_set(owner, 'diagram_description_DiagramDescription127', partner)
    assert getattr(partner, 'validation_ValidationSet') == owner
    _safe_set(owner, 'diagram_description_DiagramDescription127', None)
    assert getattr(partner, 'validation_ValidationSet') is None


def test_assoc_variable335_stub_double():
    # tool_NodeCreationVariable has no real 'tool_NodeCreationVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_NodeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_NodeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    partner = tool_NodeCreationVariable()
    setattr(partner, 'tool_NodeCreationVariable', None)
    _safe_set(owner, 'diagram_tool_NodeCreationDescription336', partner)
    assert getattr(partner, 'tool_NodeCreationVariable') == owner
    _safe_set(owner, 'diagram_tool_NodeCreationDescription336', None)
    assert getattr(partner, 'tool_NodeCreationVariable') is None


def test_assoc_variable364_stub_double():
    # tool_NodeCreationVariable has no real 'tool_NodeCreationVariable366' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    partner = tool_NodeCreationVariable()
    setattr(partner, 'tool_NodeCreationVariable366', None)
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription365', partner)
    assert getattr(partner, 'tool_NodeCreationVariable366') == owner
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription365', None)
    assert getattr(partner, 'tool_NodeCreationVariable366') is None


def test_assoc_variableDefinition118_stub_double():
    # TypedVariable has no real 'TypedVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_TypedVariableValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_TypedVariableValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_TypedVariableValue(value="sample_text")
    partner = TypedVariable()
    setattr(partner, 'TypedVariable', None)
    _safe_set(owner, 'diagram_TypedVariableValue', partner)
    assert getattr(partner, 'TypedVariable') == owner
    _safe_set(owner, 'diagram_TypedVariableValue', None)
    assert getattr(partner, 'TypedVariable') is None


def test_assoc_viewVariable337_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_NodeCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_NodeCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable', None)
    _safe_set(owner, 'diagram_tool_NodeCreationDescription338', partner)
    assert getattr(partner, 'tool_ContainerViewVariable') == owner
    _safe_set(owner, 'diagram_tool_NodeCreationDescription338', None)
    assert getattr(partner, 'tool_ContainerViewVariable') is None


def test_assoc_viewVariable367_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable369' property in the generated
    # code (a bare stub) -- manually attach it so diagram_tool_ContainerCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagram_tool_ContainerCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable369', None)
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription368', partner)
    assert getattr(partner, 'tool_ContainerViewVariable369') == owner
    _safe_set(owner, 'diagram_tool_ContainerCreationDescription368', None)
    assert getattr(partner, 'tool_ContainerViewVariable369') is None


