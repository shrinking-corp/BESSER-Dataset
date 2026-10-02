#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    AbstractDNode,
    AbstractNodeMapping,
    AbstractToolDescription,
    AdditionalLayer,
    AlignmentKind,
    ArrangeConstraint,
    BackgroundStyle,
    BasicLabelStyle,
    BasicLabelStyleDescription,
    BorderedStyle,
    BundledImageShape,
    CenteringStyle,
    CollapseFilter,
    ColorDescription,
    ConditionalContainerStyleDescription,
    ConditionalEdgeStyleDescription,
    ConditionalNodeStyleDescription,
    ConditionalStyleDescription,
    ContainerLayout,
    ContainerMapping,
    ContainerModelOperation,
    ContainerShape,
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
    EdgeArrows,
    EdgeMapping,
    EdgeMappingImport,
    EdgeRouting,
    EdgeStyle,
    EdgeStyleDescription,
    EdgeTarget,
    Enum,
    EnumLayoutValue,
    EnumOption,
    Filter,
    FilterDescription,
    FilterKind,
    FoldingStyle,
    GraphicalFilter,
    HideLabelCapabilityStyle,
    IEdgeMapping,
    IdentifiedElement,
    InteractiveVariableDescription,
    LabelPosition,
    LabelStyle,
    Layer,
    Layout,
    LayoutDirection,
    LayoutOption,
    LayoutOptionTarget,
    LineStyle,
    MappingBasedToolDescription,
    NodeMapping,
    NodeStyle,
    NodeStyleDescription,
    ReconnectionKind,
    RepresentationCreationDescription,
    RepresentationExtensionDescription,
    RepresentationNavigationDescription,
    ResizeKind,
    Side,
    Style,
    StyleDescription,
    ToolEntry,
    TypedVariable,
    VariableValue,
    abstractmethod,
    concern_ConcernDescription,
    concern_ConcernSet,
    date,
    datetime,
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
    time,
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
)


def test_0():
    var_0 = python_code_.MappingBasedToolDescription()
    var_1 = "''H_"
    var_2 = python_code_.diagram_BeginLabelStyle()
    var_3 = var_2.getDescription()
    var_4 = python_code_.EdgeMapping
    var_5 = python_code_.diagram_tool_ReconnectEdgeDescription(
        reconnectionKind=var_4,
        diagram_tool_ReconnectEdgeDescription404=var_1,
        diagram_tool_ReconnectEdgeDescription410=-2758.77,
    )
    assert isinstance(var_5, python_code_.diagram_tool_ReconnectEdgeDescription)
    var_6 = var_5.getMappings()
    var_7 = python_code_.diagram_DDiagramElementContainer(
        width=var_0,
        height=var_1,
        diagram_DDiagramElementContainer59=var_3,
        diagram_DDiagramElementContainer73=None,
        diagram_DDiagramElementContainer75=var_6,
    )
    assert isinstance(var_7, python_code_.diagram_DDiagramElementContainer)
    var_7.getNodesFromMapping(diagram_mapping=var_4)
    var_10 = True
    var_11 = python_code_.diagram_tool_Navigation(createIfNotExistent=var_10)
    assert isinstance(var_11, python_code_.diagram_tool_Navigation)
    var_12 = python_code_.ContainerStyle()
    var_13 = python_code_.tool_ContainerViewVariable()
    var_14 = python_code_.diagram_tool_DeleteElementDescription(
        diagram_tool_DeleteElementDescription={
            "ELG$-k\x0b,T=]kH\x0bx(\t=5": "SCkG^S[^Z_3gm3",
            '>"n\n@YI': -842,
        },
        diagram_tool_DeleteElementDescription378=var_12,
        diagram_tool_DeleteElementDescription381=var_13,
        diagram_tool_DeleteElementDescription387=var_4,
    )
    assert isinstance(var_14, python_code_.diagram_tool_DeleteElementDescription)
    var_14.getMappings()


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = python_code_.description_ContainerMapping()
    var_1 = python_code_.tool_DirectEditLabel()
    var_7 = python_code_.diagram_style_LozengeNodeDescription(
        widthComputationExpression=None, heightComputationExpression=var_0
    )
    assert isinstance(var_7, python_code_.diagram_style_LozengeNodeDescription)
    var_8 = "b\t`"
    var_9 = python_code_.diagram_tool_DeleteHook(id=var_8)
    assert isinstance(var_9, python_code_.diagram_tool_DeleteHook)
    python_code_.diagram_filter_FilterDescription()
    python_code_.diagram_description_ContainerMapping(
        childrenPresentation=var_1,
        diagram_description_ContainerMapping=complex(417.1688, 486.0085635),
    )


def test_2():
    var_0 = python_code_.DecorationDescriptionsSet()
    var_1 = python_code_.diagram_GaugeCompositeStyle(alignment=var_0)
    assert isinstance(var_1, python_code_.diagram_GaugeCompositeStyle)
    var_2 = python_code_.DRepresentationElement()
    var_4 = "tool_DeleteHookParameter"
    var_5 = " x/o|!;sZC9"
    var_6 = python_code_.diagram_style_EllipseNodeDescription(
        horizontalDiameterComputationExpression=var_4,
        verticalDiameterComputationExpression=var_5,
    )
    assert isinstance(var_6, python_code_.diagram_style_EllipseNodeDescription)
    var_7 = python_code_.diagram_tool_ReconnectEdgeDescription(
        reconnectionKind=[465.13, "D}OuJ}i<X3UuYE<1]", "EB2!d_Oa<9"]
    )
    assert isinstance(var_7, python_code_.diagram_tool_ReconnectEdgeDescription)
    var_8 = var_7.getMappings()
    var_13 = python_code_.diagram_ShapeContainerStyle(
        shape=var_4, backgroundColor=var_2
    )
    assert isinstance(var_13, python_code_.diagram_ShapeContainerStyle)
    var_14 = python_code_.IEdgeMapping()
    var_15 = python_code_.diagram_style_CustomStyleDescription
    var_16 = "diagram_GraphicalFilter,_diagram_style_GaugeSectionDescription__diagram_style_GaugeSectionDescription289,diagram_DDiagram"
    var_17 = python_code_.diagram_GaugeSection(
        min=var_14,
        max=var_5,
        value=var_4,
        label=var_15,
        backgroundColor=var_16,
        foregroundColor=var_8,
    )
    assert isinstance(var_17, python_code_.diagram_GaugeSection)


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = "square.filter_FilterDescription.NORTH_SOUTH._diagram_DDiagramElement__diagram_DDiagramElement45"
    var_1 = python_code_.tool_SourceEdgeCreationVariable()
    var_2 = python_code_.diagram_tool_ReconnectEdgeDescription(
        reconnectionKind=var_0,
        diagram_tool_ReconnectEdgeDescription=var_1,
        diagram_tool_ReconnectEdgeDescription407=var_1,
        diagram_tool_ReconnectEdgeDescription415={False, -1140.52, True},
    )
    assert isinstance(var_2, python_code_.diagram_tool_ReconnectEdgeDescription)
    var_3 = var_2.getMappings()
    var_4 = python_code_.diagram_CenterLabelStyle()
    var_5 = var_4.getDescription()
    var_6 = python_code_.concern_ConcernSet()
    var_7 = var_2.getMappings()
    var_8 = python_code_.tool_InitialOperation()
    var_9 = python_code_.BorderedStyle
    python_code_.diagram_description_DiagramDescription(
        domainClass=var_2,
        preconditionExpression=var_3,
        enablePopupBars=var_0,
        rootExpression=None,
        diagram_description_DiagramDescription133=(),
        diagram_description_DiagramDescription=var_5,
        diagram_description_DiagramDescription129=var_6,
        diagram_description_DiagramDescription164=var_7,
        diagram_description_DiagramDescription140=var_8,
        diagram_description_DiagramDescription154=var_9,
        diagram_description_DiagramDescription156=None,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_1 = "_diagram_AbstractDNode__diagram_AbstractDNode_diagram_description_DiagramDescription__diagram_description_DiagramDescription129"
    var_2 = "e]J'n2,$y%4a;:E~mT("
    var_3 = python_code_.diagram_ContainerStyle()
    var_4 = python_code_.diagram_DDiagramElementContainer(
        width=var_1,
        height=var_2,
        diagram_DDiagramElementContainer=var_1,
        diagram_DDiagramElementContainer68=var_3,
    )
    assert isinstance(var_4, python_code_.diagram_DDiagramElementContainer)
    var_5 = python_code_.diagram_BeginLabelStyle()
    var_6 = python_code_.tool_AbstractToolDescription
    var_5.setDescription(diagram_description=var_6)
    var_9 = python_code_.EdgeTarget()
    python_code_.diagram_tool_ContainerDropDescription(
        dragSource=var_9,
        moveEdges=1953.13,
        diagram_tool_ContainerDropDescription=var_6,
        diagram_tool_ContainerDropDescription444=var_5,
    )


def test_5():
    var_0 = "Hu=lFsd7y"
    var_1 = python_code_.diagram_NodeStyle(
        labelPosition=var_0, diagram_NodeStyle={False, 942}
    )
    assert isinstance(var_1, python_code_.diagram_NodeStyle)
    var_5 = python_code_.tool_ContainerViewVariable()
    var_6 = python_code_.diagram_tool_DeleteElementDescription(
        diagram_tool_DeleteElementDescription381=var_5
    )
    assert isinstance(var_6, python_code_.diagram_tool_DeleteElementDescription)
    var_7 = python_code_.description_DocumentedElement()
    var_9 = python_code_.diagram_description_DiagramDescription
    var_10 = python_code_.diagram_style_ShapeContainerStyleDescription(
        shape=var_0, style_ContainerStyleDescription=var_9
    )
    assert isinstance(var_10, python_code_.diagram_style_ShapeContainerStyleDescription)
    var_14 = python_code_.diagram_Dot(
        backgroundColor=var_7, strokeSizeComputationExpression=-2541.98
    )
    assert isinstance(var_14, python_code_.diagram_Dot)
    var_17 = python_code_.diagram_tool_ToolSection(icon=var_0)
    assert isinstance(var_17, python_code_.diagram_tool_ToolSection)
    var_19 = python_code_.diagram_filter_FilterDescription()
    var_19.isVisible(diagram_element=var_19)


def test_6():
    var_1 = python_code_.DiagramDescription()
    var_2 = python_code_.diagram_style_CustomStyleDescription(id=var_1)
    assert isinstance(var_2, python_code_.diagram_style_CustomStyleDescription)
    var_3 = python_code_.StyleDescription()
    var_5 = python_code_.ConditionalNodeStyleDescription()
    var_7 = python_code_.description_EndUserDocumentedElement
    var_8 = python_code_.diagram_style_WorkspaceImageDescription(
        workspacePath=var_7, style_NodeStyleDescription228=True
    )
    assert isinstance(var_8, python_code_.diagram_style_WorkspaceImageDescription)
    var_11 = '#^r1WX"[0>;o'
    var_12 = python_code_.diagram_style_BorderedStyleDescription(
        borderSizeComputationExpression=[],
        borderLineStyle=var_11,
        diagram_style_BorderedStyleDescription=var_7,
    )
    assert isinstance(var_12, python_code_.diagram_style_BorderedStyleDescription)
    var_13 = python_code_.diagram_Lozenge(width=var_3, height=[], color=var_7)
    assert isinstance(var_13, python_code_.diagram_Lozenge)
    var_14 = python_code_.DDiagram()
    var_16 = python_code_.diagram_tool_CreateEdgeView(
        sourceExpression=var_5, targetExpression=var_11
    )
    assert isinstance(var_16, python_code_.diagram_tool_CreateEdgeView)
    var_18 = python_code_.diagram_tool_RequestDescription(type=var_11)
    assert isinstance(var_18, python_code_.diagram_tool_RequestDescription)
    var_21 = python_code_.diagram_BeginLabelStyle()
    var_21.setDescription(diagram_description=var_14)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = "4"
    var_1 = python_code_.diagram_EndLabelStyle()
    python_code_.diagram_EdgeStyle(
        sourceArrow={408.12, True},
        targetArrow=var_0,
        foldingStyle=var_0,
        size=-3666,
        lineStyle=var_0,
        routingStyle=var_0,
        centered=('">|JOY', True, 1),
        strokeColor=var_0,
        diagram_EdgeStyle113=var_1,
    )


def test_8():
    var_0 = "<ob\n$|_`:l"
    var_1 = python_code_.diagram_BundledImage(
        shape=var_0, color=var_0, providedShapeID=var_0
    )
    assert isinstance(var_1, python_code_.diagram_BundledImage)


def test_9():
    var_1 = (
        "_diagram_style_LozengeNodeDescription__diagram_style_LozengeNodeDescription"
    )
    var_2 = python_code_.diagram_BundledImage(
        shape=None, color=var_1, providedShapeID=var_1
    )
    assert isinstance(var_2, python_code_.diagram_BundledImage)
    var_11 = python_code_.diagram_description_CompositeLayout
    var_12 = python_code_.diagram_Lozenge(width=var_11, height=False, color=var_1)
    assert isinstance(var_12, python_code_.diagram_Lozenge)
    var_14 = True
    var_15 = python_code_.diagram_HideLabelCapabilityStyle(hideLabelByDefault=var_14)
    assert isinstance(var_15, python_code_.diagram_HideLabelCapabilityStyle)
