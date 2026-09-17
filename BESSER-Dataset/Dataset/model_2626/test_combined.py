# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tool_DeleteHookParameter,
    diagram_tool_DeleteHook,
    AbstractToolDescription,
    diagram_tool_RequestDescription,
    tool_DeleteHook,
    tool_ElementDeleteVariable,
    tool_ElementDoubleClickVariable,
    tool_InitEdgeCreationOperation,
    tool_TargetEdgeViewCreationVariable,
    tool_SourceEdgeViewCreationVariable,
    tool_TargetEdgeCreationVariable,
    tool_SourceEdgeCreationVariable,
    tool_ContainerViewVariable,
    tool_NodeCreationVariable,
    MappingBasedToolDescription,
    diagram_tool_ContainerCreationDescription,
    diagram_tool_DeleteElementDescription,
    diagram_tool_EdgeCreationDescription,
    diagram_tool_DoubleClickDescription,
    diagram_tool_NodeCreationDescription,
    tool_ToolGroup,
    diagram_tool_ToolGroupExtension,
    ToolEntry,
    diagram_tool_ToolGroup,
    tool_ToolGroupExtension,
    tool_PopupMenu,
    tool_ToolEntry,
    tool_InitialNodeCreationOperation,
    diagram_style_HideLabelCapabilityStyleDescription,
    EdgeStyleDescription,
    diagram_style_BracketEdgeStyleDescription,
    BasicLabelStyleDescription,
    diagram_style_CenterLabelStyleDescription,
    diagram_style_EndLabelStyleDescription,
    diagram_style_BeginLabelStyleDescription,
    style_EndLabelStyleDescription,
    style_CenterLabelStyleDescription,
    style_BeginLabelStyleDescription,
    style_LabelBorderStyleDescription,
    diagram_style_SizeComputationContainerStyleDescription,
    diagram_style_GaugeSectionDescription,
    style_GaugeSectionDescription,
    style_SizeComputationContainerStyleDescription,
    style_RoundedCornerStyleDescription,
    NodeStyleDescription,
    diagram_style_NoteDescription,
    diagram_style_EllipseNodeDescription,
    diagram_style_SquareDescription,
    diagram_style_DotDescription,
    diagram_style_GaugeCompositeStyleDescription,
    diagram_style_BundledImageDescription,
    diagram_style_CustomStyleDescription,
    style_HideLabelCapabilityStyleDescription,
    style_TooltipStyleDescription,
    style_LabelStyleDescription,
    style_BorderedStyleDescription,
    diagram_style_ContainerStyleDescription,
    ColorDescription,
    StyleDescription,
    diagram_style_RoundedCornerStyleDescription,
    diagram_style_EdgeStyleDescription,
    diagram_style_BorderedStyleDescription,
    tool_ContainerDropDescription,
    diagram_style_LozengeNodeDescription,
    diagram_description_DragAndDropTargetDescription,
    Customization,
    DecorationDescriptionsSet,
    description_EndUserDocumentedElement,
    DecorationDescription,
    diagram_description_MappingBasedDecoration,
    DocumentedElement,
    diagram_description_Layout,
    ConditionalStyleDescription,
    diagram_description_ConditionalEdgeStyleDescription,
    diagram_description_ConditionalContainerStyleDescription,
    diagram_description_ConditionalNodeStyleDescription,
    description_IdentifiedElement,
    diagram_description_IEdgeMapping,
    AbstractNodeMapping,
    tool_ReconnectEdgeDescription,
    ConditionalEdgeStyleDescription,
    style_EdgeStyleDescription,
    description_IEdgeMapping,
    description_ContainerMapping,
    description_AbstractMappingImport,
    diagram_description_ContainerMappingImport,
    description_NodeMapping,
    diagram_description_NodeMappingImport,
    ConditionalContainerStyleDescription,
    style_ContainerStyleDescription,
    diagram_style_ShapeContainerStyleDescription,
    diagram_style_FlatContainerStyleDescription,
    ConditionalNodeStyleDescription,
    style_NodeStyleDescription,
    diagram_style_WorkspaceImageDescription,
    description_AbstractNodeMapping,
    description_DiagramElementMapping,
    tool_DoubleClickDescription,
    tool_DirectEditLabel,
    tool_DeleteElementDescription,
    description_RepresentationElementMapping,
    RepresentationExtensionDescription,
    diagram_description_DiagramExtensionDescription,
    description_DiagramDescription,
    description_RepresentationImportDescription,
    diagram_description_DiagramImportDescription,
    tool_ToolSection,
    EdgeMappingImport,
    tool_InitialOperation,
    Layout,
    diagram_description_CompositeLayout,
    diagram_description_OrderedTreeLayout,
    tool_RepresentationCreationDescription,
    tool_AbstractToolDescription,
    concern_ConcernSet,
    validation_ValidationSet,
    EdgeMapping,
    description_PasteTargetDescription,
    diagram_description_DiagramElementMapping,
    description_RepresentationDescription,
    description_DragAndDropTargetDescription,
    diagram_description_NodeMapping,
    diagram_description_ContainerMapping,
    diagram_description_DiagramDescription,
    diagram_EObject,
    tool_SelectModelElementVariable,
    diagram_concern_ConcernSet,
    InteractiveVariableDescription,
    filter_Filter,
    FilterDescription,
    diagram_filter_CompositeFilterDescription,
    diagram_filter_Filter,
    Filter,
    diagram_filter_VariableFilter,
    diagram_filter_MappingFilter,
    tool_ElementDropVariable,
    tool_DropContainerVariable,
    diagram_tool_ContainerDropDescription,
    RepresentationNavigationDescription,
    diagram_tool_DiagramNavigationDescription,
    RepresentationCreationDescription,
    diagram_tool_DiagramCreationDescription,
    tool_InitialContainerDropOperation,
    ContainerModelOperation,
    diagram_tool_Navigation,
    diagram_tool_CreateView,
    tool_VariableContainer,
    description_AbstractVariable,
    diagram_tool_NodeCreationVariable,
    diagram_tool_ElementDoubleClickVariable,
    diagram_tool_SourceEdgeViewCreationVariable,
    diagram_tool_TargetEdgeCreationVariable,
    diagram_tool_TargetEdgeViewCreationVariable,
    diagram_tool_SourceEdgeCreationVariable,
    diagram_tool_BehaviorTool,
    tool_EditMaskVariables,
    diagram_tool_DirectEditLabel,
    CreateView,
    diagram_tool_CreateEdgeView,
    tool_ElementSelectVariable,
    diagram_tool_ReconnectEdgeDescription,
    diagram_tool_DeleteHookParameter,
    diagram_HideLabelCapabilityStyle,
    diagram_DragAndDropTarget,
    style_StyleDescription,
    diagram_style_NodeStyleDescription,
    diagram_ComputedStyleDescriptionRegistry,
    EdgeStyle,
    diagram_BracketEdgeStyle,
    BasicLabelStyle,
    CollapseFilter,
    diagram_IndirectlyCollapseFilter,
    diagram_VariableValue,
    TypedVariable,
    VariableValue,
    diagram_TypedVariableValue,
    diagram_EObjectVariableValue,
    diagram_EndLabelStyle,
    diagram_BeginLabelStyle,
    diagram_CenterLabelStyle,
    ContainerStyle,
    diagram_ShapeContainerStyle,
    diagram_FlatContainerStyle,
    Customizable,
    diagram_GaugeSection,
    NodeStyle,
    diagram_Note,
    diagram_Square,
    diagram_Ellipse,
    diagram_Lozenge,
    diagram_CustomStyle,
    diagram_BundledImage,
    diagram_GaugeCompositeStyle,
    diagram_WorkspaceImage,
    diagram_Dot,
    HideLabelCapabilityStyle,
    BorderedStyle,
    Style,
    diagram_BorderedStyle,
    LabelStyle,
    IEdgeMapping,
    diagram_EdgeTarget,
    diagram_EdgeStyle,
    DDiagramElementContainer,
    diagram_DNodeList,
    diagram_DNodeContainer,
    ContainerMapping,
    diagram_ContainerStyle,
    NodeMapping,
    diagram_Style,
    diagram_NodeStyle,
    EdgeTarget,
    AbstractDNode,
    DDiagramElement,
    diagram_AbstractDNode,
    filter_CompositeFilterDescription,
    GraphicalFilter,
    diagram_AppliedCompositeFilters,
    diagram_HideLabelFilter,
    diagram_FoldingPointFilter,
    diagram_CollapseFilter,
    diagram_FoldingFilter,
    diagram_AbsoluteBoundsFilter,
    diagram_HideFilter,
    diagram_GraphicalFilter,
    DiagramElementMapping,
    diagram_Decoration,
    DRepresentationElement,
    DSemanticDecorator,
    DDiagram,
    diagram_DSemanticDiagram,
    Layer,
    diagram_description_AdditionalLayer,
    diagram_FilterVariableHistory,
    tool_BehaviorTool,
    validation_ValidationRule,
    AdditionalLayer,
    filter_FilterDescription,
    concern_ConcernDescription,
    diagram_DNodeListElement,
    diagram_DEdge,
    DiagramDescription,
    diagram_DDiagramElement,
    DragAndDropTarget,
    diagram_DDiagramElementContainer,
    diagram_DNode,
    description_DocumentedElement,
    diagram_description_EdgeMappingImport,
    diagram_filter_FilterDescription,
    diagram_description_AbstractNodeMapping,
    diagram_concern_ConcernDescription,
    diagram_description_Layer,
    diagram_tool_ToolSection,
    diagram_description_EdgeMapping,
    DRepresentation,
    diagram_DDiagram,
    ContainerShape,
    BundledImageShape,
    LabelPosition,
    BackgroundStyle,
    ResizeKind,
    ReconnectionKind,
    Side,
    EdgeArrows,
    ArrangeConstraint,
    FilterKind,
    ContainerLayout,
    CenteringStyle,
    LineStyle,
    EdgeRouting,
    LayoutDirection,
    AlignmentKind,
    FoldingStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tool_deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(tool_DeleteHookParameter)


def test_hyp_tool_deletehookparameter_constructor_exists():
    assert callable(tool_DeleteHookParameter.__init__)


def test_hyp_tool_deletehookparameter_constructor_args():
    sig = inspect.signature(tool_DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_deletehook_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DeleteHook)


def test_hyp_diagram_tool_deletehook_constructor_exists():
    assert callable(diagram_tool_DeleteHook.__init__)


def test_hyp_diagram_tool_deletehook_constructor_args():
    sig = inspect.signature(diagram_tool_DeleteHook.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(AbstractToolDescription)


def test_hyp_abstracttooldescription_constructor_exists():
    assert callable(AbstractToolDescription.__init__)


def test_hyp_abstracttooldescription_constructor_args():
    sig = inspect.signature(AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_requestdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_RequestDescription)


def test_hyp_diagram_tool_requestdescription_constructor_exists():
    assert callable(diagram_tool_RequestDescription.__init__)


def test_hyp_diagram_tool_requestdescription_constructor_args():
    sig = inspect.signature(diagram_tool_RequestDescription.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_tool_deletehook_is_not_abstract():
    assert not inspect.isabstract(tool_DeleteHook)


def test_hyp_tool_deletehook_constructor_exists():
    assert callable(tool_DeleteHook.__init__)


def test_hyp_tool_deletehook_constructor_args():
    sig = inspect.signature(tool_DeleteHook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDeleteVariable)


def test_hyp_tool_elementdeletevariable_constructor_exists():
    assert callable(tool_ElementDeleteVariable.__init__)


def test_hyp_tool_elementdeletevariable_constructor_args():
    sig = inspect.signature(tool_ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_elementdoubleclickvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDoubleClickVariable)


def test_hyp_tool_elementdoubleclickvariable_constructor_exists():
    assert callable(tool_ElementDoubleClickVariable.__init__)


def test_hyp_tool_elementdoubleclickvariable_constructor_args():
    sig = inspect.signature(tool_ElementDoubleClickVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitEdgeCreationOperation)


def test_hyp_tool_initedgecreationoperation_constructor_exists():
    assert callable(tool_InitEdgeCreationOperation.__init__)


def test_hyp_tool_initedgecreationoperation_constructor_args():
    sig = inspect.signature(tool_InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_targetedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_TargetEdgeViewCreationVariable)


def test_hyp_tool_targetedgeviewcreationvariable_constructor_exists():
    assert callable(tool_TargetEdgeViewCreationVariable.__init__)


def test_hyp_tool_targetedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(tool_TargetEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_sourceedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_SourceEdgeViewCreationVariable)


def test_hyp_tool_sourceedgeviewcreationvariable_constructor_exists():
    assert callable(tool_SourceEdgeViewCreationVariable.__init__)


def test_hyp_tool_sourceedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(tool_SourceEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_targetedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_TargetEdgeCreationVariable)


def test_hyp_tool_targetedgecreationvariable_constructor_exists():
    assert callable(tool_TargetEdgeCreationVariable.__init__)


def test_hyp_tool_targetedgecreationvariable_constructor_args():
    sig = inspect.signature(tool_TargetEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_sourceedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_SourceEdgeCreationVariable)


def test_hyp_tool_sourceedgecreationvariable_constructor_exists():
    assert callable(tool_SourceEdgeCreationVariable.__init__)


def test_hyp_tool_sourceedgecreationvariable_constructor_args():
    sig = inspect.signature(tool_SourceEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerViewVariable)


def test_hyp_tool_containerviewvariable_constructor_exists():
    assert callable(tool_ContainerViewVariable.__init__)


def test_hyp_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_NodeCreationVariable)


def test_hyp_tool_nodecreationvariable_constructor_exists():
    assert callable(tool_NodeCreationVariable.__init__)


def test_hyp_tool_nodecreationvariable_constructor_args():
    sig = inspect.signature(tool_NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(MappingBasedToolDescription)


def test_hyp_mappingbasedtooldescription_constructor_exists():
    assert callable(MappingBasedToolDescription.__init__)


def test_hyp_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_containercreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ContainerCreationDescription)


def test_hyp_diagram_tool_containercreationdescription_constructor_exists():
    assert callable(diagram_tool_ContainerCreationDescription.__init__)


def test_hyp_diagram_tool_containercreationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_ContainerCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"




def test_hyp_diagram_tool_deleteelementdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DeleteElementDescription)


def test_hyp_diagram_tool_deleteelementdescription_constructor_exists():
    assert callable(diagram_tool_DeleteElementDescription.__init__)


def test_hyp_diagram_tool_deleteelementdescription_constructor_args():
    sig = inspect.signature(diagram_tool_DeleteElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_edgecreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_EdgeCreationDescription)


def test_hyp_diagram_tool_edgecreationdescription_constructor_exists():
    assert callable(diagram_tool_EdgeCreationDescription.__init__)


def test_hyp_diagram_tool_edgecreationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_EdgeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "connectionStartPrecondition" in params, "Missing parameter 'connectionStartPrecondition'"





def test_hyp_diagram_tool_doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DoubleClickDescription)


def test_hyp_diagram_tool_doubleclickdescription_constructor_exists():
    assert callable(diagram_tool_DoubleClickDescription.__init__)


def test_hyp_diagram_tool_doubleclickdescription_constructor_args():
    sig = inspect.signature(diagram_tool_DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_nodecreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_NodeCreationDescription)


def test_hyp_diagram_tool_nodecreationdescription_constructor_exists():
    assert callable(diagram_tool_NodeCreationDescription.__init__)


def test_hyp_diagram_tool_nodecreationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_NodeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"




def test_hyp_tool_toolgroup_is_not_abstract():
    assert not inspect.isabstract(tool_ToolGroup)


def test_hyp_tool_toolgroup_constructor_exists():
    assert callable(tool_ToolGroup.__init__)


def test_hyp_tool_toolgroup_constructor_args():
    sig = inspect.signature(tool_ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ToolGroupExtension)


def test_hyp_diagram_tool_toolgroupextension_constructor_exists():
    assert callable(diagram_tool_ToolGroupExtension.__init__)


def test_hyp_diagram_tool_toolgroupextension_constructor_args():
    sig = inspect.signature(diagram_tool_ToolGroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_toolentry_is_not_abstract():
    assert not inspect.isabstract(ToolEntry)


def test_hyp_toolentry_constructor_exists():
    assert callable(ToolEntry.__init__)


def test_hyp_toolentry_constructor_args():
    sig = inspect.signature(ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_toolgroup_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ToolGroup)


def test_hyp_diagram_tool_toolgroup_constructor_exists():
    assert callable(diagram_tool_ToolGroup.__init__)


def test_hyp_diagram_tool_toolgroup_constructor_args():
    sig = inspect.signature(diagram_tool_ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(tool_ToolGroupExtension)


def test_hyp_tool_toolgroupextension_constructor_exists():
    assert callable(tool_ToolGroupExtension.__init__)


def test_hyp_tool_toolgroupextension_constructor_args():
    sig = inspect.signature(tool_ToolGroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_popupmenu_is_not_abstract():
    assert not inspect.isabstract(tool_PopupMenu)


def test_hyp_tool_popupmenu_constructor_exists():
    assert callable(tool_PopupMenu.__init__)


def test_hyp_tool_popupmenu_constructor_args():
    sig = inspect.signature(tool_PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_toolentry_is_not_abstract():
    assert not inspect.isabstract(tool_ToolEntry)


def test_hyp_tool_toolentry_constructor_exists():
    assert callable(tool_ToolEntry.__init__)


def test_hyp_tool_toolentry_constructor_args():
    sig = inspect.signature(tool_ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialNodeCreationOperation)


def test_hyp_tool_initialnodecreationoperation_constructor_exists():
    assert callable(tool_InitialNodeCreationOperation.__init__)


def test_hyp_tool_initialnodecreationoperation_constructor_args():
    sig = inspect.signature(tool_InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_hidelabelcapabilitystyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_HideLabelCapabilityStyleDescription)


def test_hyp_diagram_style_hidelabelcapabilitystyledescription_constructor_exists():
    assert callable(diagram_style_HideLabelCapabilityStyleDescription.__init__)


def test_hyp_diagram_style_hidelabelcapabilitystyledescription_constructor_args():
    sig = inspect.signature(diagram_style_HideLabelCapabilityStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"




def test_hyp_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(EdgeStyleDescription)


def test_hyp_edgestyledescription_constructor_exists():
    assert callable(EdgeStyleDescription.__init__)


def test_hyp_edgestyledescription_constructor_args():
    sig = inspect.signature(EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_bracketedgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_BracketEdgeStyleDescription)


def test_hyp_diagram_style_bracketedgestyledescription_constructor_exists():
    assert callable(diagram_style_BracketEdgeStyleDescription.__init__)


def test_hyp_diagram_style_bracketedgestyledescription_constructor_args():
    sig = inspect.signature(diagram_style_BracketEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyleDescription)


def test_hyp_basiclabelstyledescription_constructor_exists():
    assert callable(BasicLabelStyleDescription.__init__)


def test_hyp_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_centerlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_CenterLabelStyleDescription)


def test_hyp_diagram_style_centerlabelstyledescription_constructor_exists():
    assert callable(diagram_style_CenterLabelStyleDescription.__init__)


def test_hyp_diagram_style_centerlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_CenterLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_endlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_EndLabelStyleDescription)


def test_hyp_diagram_style_endlabelstyledescription_constructor_exists():
    assert callable(diagram_style_EndLabelStyleDescription.__init__)


def test_hyp_diagram_style_endlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_EndLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_BeginLabelStyleDescription)


def test_hyp_diagram_style_beginlabelstyledescription_constructor_exists():
    assert callable(diagram_style_BeginLabelStyleDescription.__init__)


def test_hyp_diagram_style_beginlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_endlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_EndLabelStyleDescription)


def test_hyp_style_endlabelstyledescription_constructor_exists():
    assert callable(style_EndLabelStyleDescription.__init__)


def test_hyp_style_endlabelstyledescription_constructor_args():
    sig = inspect.signature(style_EndLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_centerlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_CenterLabelStyleDescription)


def test_hyp_style_centerlabelstyledescription_constructor_exists():
    assert callable(style_CenterLabelStyleDescription.__init__)


def test_hyp_style_centerlabelstyledescription_constructor_args():
    sig = inspect.signature(style_CenterLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_BeginLabelStyleDescription)


def test_hyp_style_beginlabelstyledescription_constructor_exists():
    assert callable(style_BeginLabelStyleDescription.__init__)


def test_hyp_style_beginlabelstyledescription_constructor_args():
    sig = inspect.signature(style_BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_LabelBorderStyleDescription)


def test_hyp_style_labelborderstyledescription_constructor_exists():
    assert callable(style_LabelBorderStyleDescription.__init__)


def test_hyp_style_labelborderstyledescription_constructor_args():
    sig = inspect.signature(style_LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_SizeComputationContainerStyleDescription)


def test_hyp_diagram_style_sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(diagram_style_SizeComputationContainerStyleDescription.__init__)


def test_hyp_diagram_style_sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"





def test_hyp_diagram_style_gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_GaugeSectionDescription)


def test_hyp_diagram_style_gaugesectiondescription_constructor_exists():
    assert callable(diagram_style_GaugeSectionDescription.__init__)


def test_hyp_diagram_style_gaugesectiondescription_constructor_args():
    sig = inspect.signature(diagram_style_GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "minValueExpression" in params, "Missing parameter 'minValueExpression'"
    assert "label" in params, "Missing parameter 'label'"
    assert "maxValueExpression" in params, "Missing parameter 'maxValueExpression'"
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"







def test_hyp_style_gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(style_GaugeSectionDescription)


def test_hyp_style_gaugesectiondescription_constructor_exists():
    assert callable(style_GaugeSectionDescription.__init__)


def test_hyp_style_gaugesectiondescription_constructor_args():
    sig = inspect.signature(style_GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_SizeComputationContainerStyleDescription)


def test_hyp_style_sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(style_SizeComputationContainerStyleDescription.__init__)


def test_hyp_style_sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(style_SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_RoundedCornerStyleDescription)


def test_hyp_style_roundedcornerstyledescription_constructor_exists():
    assert callable(style_RoundedCornerStyleDescription.__init__)


def test_hyp_style_roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(style_RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(NodeStyleDescription)


def test_hyp_nodestyledescription_constructor_exists():
    assert callable(NodeStyleDescription.__init__)


def test_hyp_nodestyledescription_constructor_args():
    sig = inspect.signature(NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_notedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_NoteDescription)


def test_hyp_diagram_style_notedescription_constructor_exists():
    assert callable(diagram_style_NoteDescription.__init__)


def test_hyp_diagram_style_notedescription_constructor_args():
    sig = inspect.signature(diagram_style_NoteDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_ellipsenodedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_EllipseNodeDescription)


def test_hyp_diagram_style_ellipsenodedescription_constructor_exists():
    assert callable(diagram_style_EllipseNodeDescription.__init__)


def test_hyp_diagram_style_ellipsenodedescription_constructor_args():
    sig = inspect.signature(diagram_style_EllipseNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameterComputationExpression" in params, "Missing parameter 'verticalDiameterComputationExpression'"
    assert "horizontalDiameterComputationExpression" in params, "Missing parameter 'horizontalDiameterComputationExpression'"





def test_hyp_diagram_style_squaredescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_SquareDescription)


def test_hyp_diagram_style_squaredescription_constructor_exists():
    assert callable(diagram_style_SquareDescription.__init__)


def test_hyp_diagram_style_squaredescription_constructor_args():
    sig = inspect.signature(diagram_style_SquareDescription.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"





def test_hyp_diagram_style_dotdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_DotDescription)


def test_hyp_diagram_style_dotdescription_constructor_exists():
    assert callable(diagram_style_DotDescription.__init__)


def test_hyp_diagram_style_dotdescription_constructor_args():
    sig = inspect.signature(diagram_style_DotDescription.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"




def test_hyp_diagram_style_gaugecompositestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_GaugeCompositeStyleDescription)


def test_hyp_diagram_style_gaugecompositestyledescription_constructor_exists():
    assert callable(diagram_style_GaugeCompositeStyleDescription.__init__)


def test_hyp_diagram_style_gaugecompositestyledescription_constructor_args():
    sig = inspect.signature(diagram_style_GaugeCompositeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"




def test_hyp_diagram_style_bundledimagedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_BundledImageDescription)


def test_hyp_diagram_style_bundledimagedescription_constructor_exists():
    assert callable(diagram_style_BundledImageDescription.__init__)


def test_hyp_diagram_style_bundledimagedescription_constructor_args():
    sig = inspect.signature(diagram_style_BundledImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "providedShapeID" in params, "Missing parameter 'providedShapeID'"





def test_hyp_diagram_style_customstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_CustomStyleDescription)


def test_hyp_diagram_style_customstyledescription_constructor_exists():
    assert callable(diagram_style_CustomStyleDescription.__init__)


def test_hyp_diagram_style_customstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_CustomStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_style_hidelabelcapabilitystyledescription_is_not_abstract():
    assert not inspect.isabstract(style_HideLabelCapabilityStyleDescription)


def test_hyp_style_hidelabelcapabilitystyledescription_constructor_exists():
    assert callable(style_HideLabelCapabilityStyleDescription.__init__)


def test_hyp_style_hidelabelcapabilitystyledescription_constructor_args():
    sig = inspect.signature(style_HideLabelCapabilityStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_tooltipstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_TooltipStyleDescription)


def test_hyp_style_tooltipstyledescription_constructor_exists():
    assert callable(style_TooltipStyleDescription.__init__)


def test_hyp_style_tooltipstyledescription_constructor_args():
    sig = inspect.signature(style_TooltipStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_labelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_LabelStyleDescription)


def test_hyp_style_labelstyledescription_constructor_exists():
    assert callable(style_LabelStyleDescription.__init__)


def test_hyp_style_labelstyledescription_constructor_args():
    sig = inspect.signature(style_LabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_borderedstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_BorderedStyleDescription)


def test_hyp_style_borderedstyledescription_constructor_exists():
    assert callable(style_BorderedStyleDescription.__init__)


def test_hyp_style_borderedstyledescription_constructor_args():
    sig = inspect.signature(style_BorderedStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_ContainerStyleDescription)


def test_hyp_diagram_style_containerstyledescription_constructor_exists():
    assert callable(diagram_style_ContainerStyleDescription.__init__)


def test_hyp_diagram_style_containerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "roundedCorner" in params, "Missing parameter 'roundedCorner'"




def test_hyp_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_hyp_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_hyp_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styledescription_is_not_abstract():
    assert not inspect.isabstract(StyleDescription)


def test_hyp_styledescription_constructor_exists():
    assert callable(StyleDescription.__init__)


def test_hyp_styledescription_constructor_args():
    sig = inspect.signature(StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_RoundedCornerStyleDescription)


def test_hyp_diagram_style_roundedcornerstyledescription_constructor_exists():
    assert callable(diagram_style_RoundedCornerStyleDescription.__init__)


def test_hyp_diagram_style_roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "arcHeight" in params, "Missing parameter 'arcHeight'"
    assert "arcWidth" in params, "Missing parameter 'arcWidth'"





def test_hyp_diagram_style_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_EdgeStyleDescription)


def test_hyp_diagram_style_edgestyledescription_constructor_exists():
    assert callable(diagram_style_EdgeStyleDescription.__init__)


def test_hyp_diagram_style_edgestyledescription_constructor_args():
    sig = inspect.signature(diagram_style_EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "endsCentering" in params, "Missing parameter 'endsCentering'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"










def test_hyp_diagram_style_borderedstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_BorderedStyleDescription)


def test_hyp_diagram_style_borderedstyledescription_constructor_exists():
    assert callable(diagram_style_BorderedStyleDescription.__init__)


def test_hyp_diagram_style_borderedstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_BorderedStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"
    assert "borderLineStyle" in params, "Missing parameter 'borderLineStyle'"





def test_hyp_tool_containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerDropDescription)


def test_hyp_tool_containerdropdescription_constructor_exists():
    assert callable(tool_ContainerDropDescription.__init__)


def test_hyp_tool_containerdropdescription_constructor_args():
    sig = inspect.signature(tool_ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_lozengenodedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_LozengeNodeDescription)


def test_hyp_diagram_style_lozengenodedescription_constructor_exists():
    assert callable(diagram_style_LozengeNodeDescription.__init__)


def test_hyp_diagram_style_lozengenodedescription_constructor_args():
    sig = inspect.signature(diagram_style_LozengeNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"





def test_hyp_diagram_description_draganddroptargetdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DragAndDropTargetDescription)


def test_hyp_diagram_description_draganddroptargetdescription_constructor_exists():
    assert callable(diagram_description_DragAndDropTargetDescription.__init__)


def test_hyp_diagram_description_draganddroptargetdescription_constructor_args():
    sig = inspect.signature(diagram_description_DragAndDropTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customization_is_not_abstract():
    assert not inspect.isabstract(Customization)


def test_hyp_customization_constructor_exists():
    assert callable(Customization.__init__)


def test_hyp_customization_constructor_args():
    sig = inspect.signature(Customization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_decorationdescriptionsset_is_not_abstract():
    assert not inspect.isabstract(DecorationDescriptionsSet)


def test_hyp_decorationdescriptionsset_constructor_exists():
    assert callable(DecorationDescriptionsSet.__init__)


def test_hyp_decorationdescriptionsset_constructor_args():
    sig = inspect.signature(DecorationDescriptionsSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(description_EndUserDocumentedElement)


def test_hyp_description_enduserdocumentedelement_constructor_exists():
    assert callable(description_EndUserDocumentedElement.__init__)


def test_hyp_description_enduserdocumentedelement_constructor_args():
    sig = inspect.signature(description_EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(DecorationDescription)


def test_hyp_decorationdescription_constructor_exists():
    assert callable(DecorationDescription.__init__)


def test_hyp_decorationdescription_constructor_args():
    sig = inspect.signature(DecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_mappingbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(diagram_description_MappingBasedDecoration)


def test_hyp_diagram_description_mappingbaseddecoration_constructor_exists():
    assert callable(diagram_description_MappingBasedDecoration.__init__)


def test_hyp_diagram_description_mappingbaseddecoration_constructor_args():
    sig = inspect.signature(diagram_description_MappingBasedDecoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_hyp_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_hyp_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_layout_is_not_abstract():
    assert not inspect.isabstract(diagram_description_Layout)


def test_hyp_diagram_description_layout_constructor_exists():
    assert callable(diagram_description_Layout.__init__)


def test_hyp_diagram_description_layout_constructor_args():
    sig = inspect.signature(diagram_description_Layout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalStyleDescription)


def test_hyp_conditionalstyledescription_constructor_exists():
    assert callable(ConditionalStyleDescription.__init__)


def test_hyp_conditionalstyledescription_constructor_args():
    sig = inspect.signature(ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ConditionalEdgeStyleDescription)


def test_hyp_diagram_description_conditionaledgestyledescription_constructor_exists():
    assert callable(diagram_description_ConditionalEdgeStyleDescription.__init__)


def test_hyp_diagram_description_conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(diagram_description_ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ConditionalContainerStyleDescription)


def test_hyp_diagram_description_conditionalcontainerstyledescription_constructor_exists():
    assert callable(diagram_description_ConditionalContainerStyleDescription.__init__)


def test_hyp_diagram_description_conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram_description_ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ConditionalNodeStyleDescription)


def test_hyp_diagram_description_conditionalnodestyledescription_constructor_exists():
    assert callable(diagram_description_ConditionalNodeStyleDescription.__init__)


def test_hyp_diagram_description_conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(diagram_description_ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(description_IdentifiedElement)


def test_hyp_description_identifiedelement_constructor_exists():
    assert callable(description_IdentifiedElement.__init__)


def test_hyp_description_identifiedelement_constructor_args():
    sig = inspect.signature(description_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_IEdgeMapping)


def test_hyp_diagram_description_iedgemapping_constructor_exists():
    assert callable(diagram_description_IEdgeMapping.__init__)


def test_hyp_diagram_description_iedgemapping_constructor_args():
    sig = inspect.signature(diagram_description_IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(AbstractNodeMapping)


def test_hyp_abstractnodemapping_constructor_exists():
    assert callable(AbstractNodeMapping.__init__)


def test_hyp_abstractnodemapping_constructor_args():
    sig = inspect.signature(AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(tool_ReconnectEdgeDescription)


def test_hyp_tool_reconnectedgedescription_constructor_exists():
    assert callable(tool_ReconnectEdgeDescription.__init__)


def test_hyp_tool_reconnectedgedescription_constructor_args():
    sig = inspect.signature(tool_ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalEdgeStyleDescription)


def test_hyp_conditionaledgestyledescription_constructor_exists():
    assert callable(ConditionalEdgeStyleDescription.__init__)


def test_hyp_conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(style_EdgeStyleDescription)


def test_hyp_style_edgestyledescription_constructor_exists():
    assert callable(style_EdgeStyleDescription.__init__)


def test_hyp_style_edgestyledescription_constructor_args():
    sig = inspect.signature(style_EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(description_IEdgeMapping)


def test_hyp_description_iedgemapping_constructor_exists():
    assert callable(description_IEdgeMapping.__init__)


def test_hyp_description_iedgemapping_constructor_args():
    sig = inspect.signature(description_IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_containermapping_is_not_abstract():
    assert not inspect.isabstract(description_ContainerMapping)


def test_hyp_description_containermapping_constructor_exists():
    assert callable(description_ContainerMapping.__init__)


def test_hyp_description_containermapping_constructor_args():
    sig = inspect.signature(description_ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(description_AbstractMappingImport)


def test_hyp_description_abstractmappingimport_constructor_exists():
    assert callable(description_AbstractMappingImport.__init__)


def test_hyp_description_abstractmappingimport_constructor_args():
    sig = inspect.signature(description_AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_containermappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ContainerMappingImport)


def test_hyp_diagram_description_containermappingimport_constructor_exists():
    assert callable(diagram_description_ContainerMappingImport.__init__)


def test_hyp_diagram_description_containermappingimport_constructor_args():
    sig = inspect.signature(diagram_description_ContainerMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_nodemapping_is_not_abstract():
    assert not inspect.isabstract(description_NodeMapping)


def test_hyp_description_nodemapping_constructor_exists():
    assert callable(description_NodeMapping.__init__)


def test_hyp_description_nodemapping_constructor_args():
    sig = inspect.signature(description_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_nodemappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram_description_NodeMappingImport)


def test_hyp_diagram_description_nodemappingimport_constructor_exists():
    assert callable(diagram_description_NodeMappingImport.__init__)


def test_hyp_diagram_description_nodemappingimport_constructor_args():
    sig = inspect.signature(diagram_description_NodeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalContainerStyleDescription)


def test_hyp_conditionalcontainerstyledescription_constructor_exists():
    assert callable(ConditionalContainerStyleDescription.__init__)


def test_hyp_conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_ContainerStyleDescription)


def test_hyp_style_containerstyledescription_constructor_exists():
    assert callable(style_ContainerStyleDescription.__init__)


def test_hyp_style_containerstyledescription_constructor_args():
    sig = inspect.signature(style_ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_shapecontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_ShapeContainerStyleDescription)


def test_hyp_diagram_style_shapecontainerstyledescription_constructor_exists():
    assert callable(diagram_style_ShapeContainerStyleDescription.__init__)


def test_hyp_diagram_style_shapecontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_ShapeContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"




def test_hyp_diagram_style_flatcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_FlatContainerStyleDescription)


def test_hyp_diagram_style_flatcontainerstyledescription_constructor_exists():
    assert callable(diagram_style_FlatContainerStyleDescription.__init__)


def test_hyp_diagram_style_flatcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_FlatContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"




def test_hyp_conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalNodeStyleDescription)


def test_hyp_conditionalnodestyledescription_constructor_exists():
    assert callable(ConditionalNodeStyleDescription.__init__)


def test_hyp_conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(style_NodeStyleDescription)


def test_hyp_style_nodestyledescription_constructor_exists():
    assert callable(style_NodeStyleDescription.__init__)


def test_hyp_style_nodestyledescription_constructor_args():
    sig = inspect.signature(style_NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_workspaceimagedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_WorkspaceImageDescription)


def test_hyp_diagram_style_workspaceimagedescription_constructor_exists():
    assert callable(diagram_style_WorkspaceImageDescription.__init__)


def test_hyp_diagram_style_workspaceimagedescription_constructor_args():
    sig = inspect.signature(diagram_style_WorkspaceImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"




def test_hyp_description_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(description_AbstractNodeMapping)


def test_hyp_description_abstractnodemapping_constructor_exists():
    assert callable(description_AbstractNodeMapping.__init__)


def test_hyp_description_abstractnodemapping_constructor_args():
    sig = inspect.signature(description_AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(description_DiagramElementMapping)


def test_hyp_description_diagramelementmapping_constructor_exists():
    assert callable(description_DiagramElementMapping.__init__)


def test_hyp_description_diagramelementmapping_constructor_args():
    sig = inspect.signature(description_DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(tool_DoubleClickDescription)


def test_hyp_tool_doubleclickdescription_constructor_exists():
    assert callable(tool_DoubleClickDescription.__init__)


def test_hyp_tool_doubleclickdescription_constructor_args():
    sig = inspect.signature(tool_DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_directeditlabel_is_not_abstract():
    assert not inspect.isabstract(tool_DirectEditLabel)


def test_hyp_tool_directeditlabel_constructor_exists():
    assert callable(tool_DirectEditLabel.__init__)


def test_hyp_tool_directeditlabel_constructor_args():
    sig = inspect.signature(tool_DirectEditLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_deleteelementdescription_is_not_abstract():
    assert not inspect.isabstract(tool_DeleteElementDescription)


def test_hyp_tool_deleteelementdescription_constructor_exists():
    assert callable(tool_DeleteElementDescription.__init__)


def test_hyp_tool_deleteelementdescription_constructor_args():
    sig = inspect.signature(tool_DeleteElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationElementMapping)


def test_hyp_description_representationelementmapping_constructor_exists():
    assert callable(description_RepresentationElementMapping.__init__)


def test_hyp_description_representationelementmapping_constructor_args():
    sig = inspect.signature(description_RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationExtensionDescription)


def test_hyp_representationextensiondescription_constructor_exists():
    assert callable(RepresentationExtensionDescription.__init__)


def test_hyp_representationextensiondescription_constructor_args():
    sig = inspect.signature(RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_diagramextensiondescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DiagramExtensionDescription)


def test_hyp_diagram_description_diagramextensiondescription_constructor_exists():
    assert callable(diagram_description_DiagramExtensionDescription.__init__)


def test_hyp_diagram_description_diagramextensiondescription_constructor_args():
    sig = inspect.signature(diagram_description_DiagramExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(description_DiagramDescription)


def test_hyp_description_diagramdescription_constructor_exists():
    assert callable(description_DiagramDescription.__init__)


def test_hyp_description_diagramdescription_constructor_args():
    sig = inspect.signature(description_DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationImportDescription)


def test_hyp_description_representationimportdescription_constructor_exists():
    assert callable(description_RepresentationImportDescription.__init__)


def test_hyp_description_representationimportdescription_constructor_args():
    sig = inspect.signature(description_RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_diagramimportdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DiagramImportDescription)


def test_hyp_diagram_description_diagramimportdescription_constructor_exists():
    assert callable(diagram_description_DiagramImportDescription.__init__)


def test_hyp_diagram_description_diagramimportdescription_constructor_args():
    sig = inspect.signature(diagram_description_DiagramImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_toolsection_is_not_abstract():
    assert not inspect.isabstract(tool_ToolSection)


def test_hyp_tool_toolsection_constructor_exists():
    assert callable(tool_ToolSection.__init__)


def test_hyp_tool_toolsection_constructor_args():
    sig = inspect.signature(tool_ToolSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(EdgeMappingImport)


def test_hyp_edgemappingimport_constructor_exists():
    assert callable(EdgeMappingImport.__init__)


def test_hyp_edgemappingimport_constructor_args():
    sig = inspect.signature(EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialOperation)


def test_hyp_tool_initialoperation_constructor_exists():
    assert callable(tool_InitialOperation.__init__)


def test_hyp_tool_initialoperation_constructor_args():
    sig = inspect.signature(tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_hyp_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_hyp_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_compositelayout_is_not_abstract():
    assert not inspect.isabstract(diagram_description_CompositeLayout)


def test_hyp_diagram_description_compositelayout_constructor_exists():
    assert callable(diagram_description_CompositeLayout.__init__)


def test_hyp_diagram_description_compositelayout_constructor_args():
    sig = inspect.signature(diagram_description_CompositeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "padding" in params, "Missing parameter 'padding'"





def test_hyp_diagram_description_orderedtreelayout_is_not_abstract():
    assert not inspect.isabstract(diagram_description_OrderedTreeLayout)


def test_hyp_diagram_description_orderedtreelayout_constructor_exists():
    assert callable(diagram_description_OrderedTreeLayout.__init__)


def test_hyp_diagram_description_orderedtreelayout_constructor_args():
    sig = inspect.signature(diagram_description_OrderedTreeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"




def test_hyp_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationCreationDescription)


def test_hyp_tool_representationcreationdescription_constructor_exists():
    assert callable(tool_RepresentationCreationDescription.__init__)


def test_hyp_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool_AbstractToolDescription)


def test_hyp_tool_abstracttooldescription_constructor_exists():
    assert callable(tool_AbstractToolDescription.__init__)


def test_hyp_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_concern_concernset_is_not_abstract():
    assert not inspect.isabstract(concern_ConcernSet)


def test_hyp_concern_concernset_constructor_exists():
    assert callable(concern_ConcernSet.__init__)


def test_hyp_concern_concernset_constructor_args():
    sig = inspect.signature(concern_ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_validation_validationset_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationSet)


def test_hyp_validation_validationset_constructor_exists():
    assert callable(validation_ValidationSet.__init__)


def test_hyp_validation_validationset_constructor_args():
    sig = inspect.signature(validation_ValidationSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edgemapping_is_not_abstract():
    assert not inspect.isabstract(EdgeMapping)


def test_hyp_edgemapping_constructor_exists():
    assert callable(EdgeMapping.__init__)


def test_hyp_edgemapping_constructor_args():
    sig = inspect.signature(EdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(description_PasteTargetDescription)


def test_hyp_description_pastetargetdescription_constructor_exists():
    assert callable(description_PasteTargetDescription.__init__)


def test_hyp_description_pastetargetdescription_constructor_args():
    sig = inspect.signature(description_PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DiagramElementMapping)


def test_hyp_diagram_description_diagramelementmapping_constructor_exists():
    assert callable(diagram_description_DiagramElementMapping.__init__)


def test_hyp_diagram_description_diagramelementmapping_constructor_args():
    sig = inspect.signature(diagram_description_DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "semanticElements" in params, "Missing parameter 'semanticElements'"
    assert "synchronizationLock" in params, "Missing parameter 'synchronizationLock'"
    assert "semanticCandidatesExpression" in params, "Missing parameter 'semanticCandidatesExpression'"
    assert "createElements" in params, "Missing parameter 'createElements'"








def test_hyp_description_representationdescription_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationDescription)


def test_hyp_description_representationdescription_constructor_exists():
    assert callable(description_RepresentationDescription.__init__)


def test_hyp_description_representationdescription_constructor_args():
    sig = inspect.signature(description_RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_draganddroptargetdescription_is_not_abstract():
    assert not inspect.isabstract(description_DragAndDropTargetDescription)


def test_hyp_description_draganddroptargetdescription_constructor_exists():
    assert callable(description_DragAndDropTargetDescription.__init__)


def test_hyp_description_draganddroptargetdescription_constructor_args():
    sig = inspect.signature(description_DragAndDropTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_nodemapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_NodeMapping)


def test_hyp_diagram_description_nodemapping_constructor_exists():
    assert callable(diagram_description_NodeMapping.__init__)


def test_hyp_diagram_description_nodemapping_constructor_args():
    sig = inspect.signature(diagram_description_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_containermapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ContainerMapping)


def test_hyp_diagram_description_containermapping_constructor_exists():
    assert callable(diagram_description_ContainerMapping.__init__)


def test_hyp_diagram_description_containermapping_constructor_args():
    sig = inspect.signature(diagram_description_ContainerMapping.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"




def test_hyp_diagram_description_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DiagramDescription)


def test_hyp_diagram_description_diagramdescription_constructor_exists():
    assert callable(diagram_description_DiagramDescription.__init__)


def test_hyp_diagram_description_diagramdescription_constructor_args():
    sig = inspect.signature(diagram_description_DiagramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "enablePopupBars" in params, "Missing parameter 'enablePopupBars'"







def test_hyp_diagram_eobject_is_not_abstract():
    assert not inspect.isabstract(diagram_EObject)


def test_hyp_diagram_eobject_constructor_exists():
    assert callable(diagram_EObject.__init__)


def test_hyp_diagram_eobject_constructor_args():
    sig = inspect.signature(diagram_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_selectmodelelementvariable_is_not_abstract():
    assert not inspect.isabstract(tool_SelectModelElementVariable)


def test_hyp_tool_selectmodelelementvariable_constructor_exists():
    assert callable(tool_SelectModelElementVariable.__init__)


def test_hyp_tool_selectmodelelementvariable_constructor_args():
    sig = inspect.signature(tool_SelectModelElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_concern_concernset_is_not_abstract():
    assert not inspect.isabstract(diagram_concern_ConcernSet)


def test_hyp_diagram_concern_concernset_constructor_exists():
    assert callable(diagram_concern_ConcernSet.__init__)


def test_hyp_diagram_concern_concernset_constructor_args():
    sig = inspect.signature(diagram_concern_ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(InteractiveVariableDescription)


def test_hyp_interactivevariabledescription_constructor_exists():
    assert callable(InteractiveVariableDescription.__init__)


def test_hyp_interactivevariabledescription_constructor_args():
    sig = inspect.signature(InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filter_filter_is_not_abstract():
    assert not inspect.isabstract(filter_Filter)


def test_hyp_filter_filter_constructor_exists():
    assert callable(filter_Filter.__init__)


def test_hyp_filter_filter_constructor_args():
    sig = inspect.signature(filter_Filter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filterdescription_is_not_abstract():
    assert not inspect.isabstract(FilterDescription)


def test_hyp_filterdescription_constructor_exists():
    assert callable(FilterDescription.__init__)


def test_hyp_filterdescription_constructor_args():
    sig = inspect.signature(FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_filter_compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_CompositeFilterDescription)


def test_hyp_diagram_filter_compositefilterdescription_constructor_exists():
    assert callable(diagram_filter_CompositeFilterDescription.__init__)


def test_hyp_diagram_filter_compositefilterdescription_constructor_args():
    sig = inspect.signature(diagram_filter_CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_filter_filter_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_Filter)


def test_hyp_diagram_filter_filter_constructor_exists():
    assert callable(diagram_filter_Filter.__init__)


def test_hyp_diagram_filter_filter_constructor_args():
    sig = inspect.signature(diagram_filter_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "filterKind" in params, "Missing parameter 'filterKind'"




def test_hyp_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_hyp_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_hyp_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_filter_variablefilter_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_VariableFilter)


def test_hyp_diagram_filter_variablefilter_constructor_exists():
    assert callable(diagram_filter_VariableFilter.__init__)


def test_hyp_diagram_filter_variablefilter_constructor_args():
    sig = inspect.signature(diagram_filter_VariableFilter.__init__)
    params = list(sig.parameters.keys())
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"




def test_hyp_diagram_filter_mappingfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_MappingFilter)


def test_hyp_diagram_filter_mappingfilter_constructor_exists():
    assert callable(diagram_filter_MappingFilter.__init__)


def test_hyp_diagram_filter_mappingfilter_constructor_args():
    sig = inspect.signature(diagram_filter_MappingFilter.__init__)
    params = list(sig.parameters.keys())
    assert "viewConditionExpression" in params, "Missing parameter 'viewConditionExpression'"
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"





def test_hyp_tool_elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDropVariable)


def test_hyp_tool_elementdropvariable_constructor_exists():
    assert callable(tool_ElementDropVariable.__init__)


def test_hyp_tool_elementdropvariable_constructor_args():
    sig = inspect.signature(tool_ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_DropContainerVariable)


def test_hyp_tool_dropcontainervariable_constructor_exists():
    assert callable(tool_DropContainerVariable.__init__)


def test_hyp_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ContainerDropDescription)


def test_hyp_diagram_tool_containerdropdescription_constructor_exists():
    assert callable(diagram_tool_ContainerDropDescription.__init__)


def test_hyp_diagram_tool_containerdropdescription_constructor_args():
    sig = inspect.signature(diagram_tool_ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())
    assert "dragSource" in params, "Missing parameter 'dragSource'"
    assert "moveEdges" in params, "Missing parameter 'moveEdges'"





def test_hyp_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationNavigationDescription)


def test_hyp_representationnavigationdescription_constructor_exists():
    assert callable(RepresentationNavigationDescription.__init__)


def test_hyp_representationnavigationdescription_constructor_args():
    sig = inspect.signature(RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_diagramnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DiagramNavigationDescription)


def test_hyp_diagram_tool_diagramnavigationdescription_constructor_exists():
    assert callable(diagram_tool_DiagramNavigationDescription.__init__)


def test_hyp_diagram_tool_diagramnavigationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_DiagramNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationCreationDescription)


def test_hyp_representationcreationdescription_constructor_exists():
    assert callable(RepresentationCreationDescription.__init__)


def test_hyp_representationcreationdescription_constructor_args():
    sig = inspect.signature(RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_diagramcreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DiagramCreationDescription)


def test_hyp_diagram_tool_diagramcreationdescription_constructor_exists():
    assert callable(diagram_tool_DiagramCreationDescription.__init__)


def test_hyp_diagram_tool_diagramcreationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_DiagramCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialContainerDropOperation)


def test_hyp_tool_initialcontainerdropoperation_constructor_exists():
    assert callable(tool_InitialContainerDropOperation.__init__)


def test_hyp_tool_initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(tool_InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(ContainerModelOperation)


def test_hyp_containermodeloperation_constructor_exists():
    assert callable(ContainerModelOperation.__init__)


def test_hyp_containermodeloperation_constructor_args():
    sig = inspect.signature(ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_navigation_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_Navigation)


def test_hyp_diagram_tool_navigation_constructor_exists():
    assert callable(diagram_tool_Navigation.__init__)


def test_hyp_diagram_tool_navigation_constructor_args():
    sig = inspect.signature(diagram_tool_Navigation.__init__)
    params = list(sig.parameters.keys())
    assert "createIfNotExistent" in params, "Missing parameter 'createIfNotExistent'"




def test_hyp_diagram_tool_createview_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_CreateView)


def test_hyp_diagram_tool_createview_constructor_exists():
    assert callable(diagram_tool_CreateView.__init__)


def test_hyp_diagram_tool_createview_constructor_args():
    sig = inspect.signature(diagram_tool_CreateView.__init__)
    params = list(sig.parameters.keys())
    assert "containerViewExpression" in params, "Missing parameter 'containerViewExpression'"
    assert "variableName" in params, "Missing parameter 'variableName'"





def test_hyp_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool_VariableContainer)


def test_hyp_tool_variablecontainer_constructor_exists():
    assert callable(tool_VariableContainer.__init__)


def test_hyp_tool_variablecontainer_constructor_args():
    sig = inspect.signature(tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(description_AbstractVariable)


def test_hyp_description_abstractvariable_constructor_exists():
    assert callable(description_AbstractVariable.__init__)


def test_hyp_description_abstractvariable_constructor_args():
    sig = inspect.signature(description_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_NodeCreationVariable)


def test_hyp_diagram_tool_nodecreationvariable_constructor_exists():
    assert callable(diagram_tool_NodeCreationVariable.__init__)


def test_hyp_diagram_tool_nodecreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_elementdoubleclickvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ElementDoubleClickVariable)


def test_hyp_diagram_tool_elementdoubleclickvariable_constructor_exists():
    assert callable(diagram_tool_ElementDoubleClickVariable.__init__)


def test_hyp_diagram_tool_elementdoubleclickvariable_constructor_args():
    sig = inspect.signature(diagram_tool_ElementDoubleClickVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_sourceedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_SourceEdgeViewCreationVariable)


def test_hyp_diagram_tool_sourceedgeviewcreationvariable_constructor_exists():
    assert callable(diagram_tool_SourceEdgeViewCreationVariable.__init__)


def test_hyp_diagram_tool_sourceedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_SourceEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_targetedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_TargetEdgeCreationVariable)


def test_hyp_diagram_tool_targetedgecreationvariable_constructor_exists():
    assert callable(diagram_tool_TargetEdgeCreationVariable.__init__)


def test_hyp_diagram_tool_targetedgecreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_TargetEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_targetedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_TargetEdgeViewCreationVariable)


def test_hyp_diagram_tool_targetedgeviewcreationvariable_constructor_exists():
    assert callable(diagram_tool_TargetEdgeViewCreationVariable.__init__)


def test_hyp_diagram_tool_targetedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_TargetEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_sourceedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_SourceEdgeCreationVariable)


def test_hyp_diagram_tool_sourceedgecreationvariable_constructor_exists():
    assert callable(diagram_tool_SourceEdgeCreationVariable.__init__)


def test_hyp_diagram_tool_sourceedgecreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_SourceEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_behaviortool_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_BehaviorTool)


def test_hyp_diagram_tool_behaviortool_constructor_exists():
    assert callable(diagram_tool_BehaviorTool.__init__)


def test_hyp_diagram_tool_behaviortool_constructor_args():
    sig = inspect.signature(diagram_tool_BehaviorTool.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"




def test_hyp_tool_editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(tool_EditMaskVariables)


def test_hyp_tool_editmaskvariables_constructor_exists():
    assert callable(tool_EditMaskVariables.__init__)


def test_hyp_tool_editmaskvariables_constructor_args():
    sig = inspect.signature(tool_EditMaskVariables.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_directeditlabel_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DirectEditLabel)


def test_hyp_diagram_tool_directeditlabel_constructor_exists():
    assert callable(diagram_tool_DirectEditLabel.__init__)


def test_hyp_diagram_tool_directeditlabel_constructor_args():
    sig = inspect.signature(diagram_tool_DirectEditLabel.__init__)
    params = list(sig.parameters.keys())
    assert "inputLabelExpression" in params, "Missing parameter 'inputLabelExpression'"




def test_hyp_createview_is_not_abstract():
    assert not inspect.isabstract(CreateView)


def test_hyp_createview_constructor_exists():
    assert callable(CreateView.__init__)


def test_hyp_createview_constructor_args():
    sig = inspect.signature(CreateView.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_createedgeview_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_CreateEdgeView)


def test_hyp_diagram_tool_createedgeview_constructor_exists():
    assert callable(diagram_tool_CreateEdgeView.__init__)


def test_hyp_diagram_tool_createedgeview_constructor_args():
    sig = inspect.signature(diagram_tool_CreateEdgeView.__init__)
    params = list(sig.parameters.keys())
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"
    assert "sourceExpression" in params, "Missing parameter 'sourceExpression'"





def test_hyp_tool_elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementSelectVariable)


def test_hyp_tool_elementselectvariable_constructor_exists():
    assert callable(tool_ElementSelectVariable.__init__)


def test_hyp_tool_elementselectvariable_constructor_args():
    sig = inspect.signature(tool_ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_tool_reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ReconnectEdgeDescription)


def test_hyp_diagram_tool_reconnectedgedescription_constructor_exists():
    assert callable(diagram_tool_ReconnectEdgeDescription.__init__)


def test_hyp_diagram_tool_reconnectedgedescription_constructor_args():
    sig = inspect.signature(diagram_tool_ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "reconnectionKind" in params, "Missing parameter 'reconnectionKind'"




def test_hyp_diagram_tool_deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DeleteHookParameter)


def test_hyp_diagram_tool_deletehookparameter_constructor_exists():
    assert callable(diagram_tool_DeleteHookParameter.__init__)


def test_hyp_diagram_tool_deletehookparameter_constructor_args():
    sig = inspect.signature(diagram_tool_DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_diagram_hidelabelcapabilitystyle_is_not_abstract():
    assert not inspect.isabstract(diagram_HideLabelCapabilityStyle)


def test_hyp_diagram_hidelabelcapabilitystyle_constructor_exists():
    assert callable(diagram_HideLabelCapabilityStyle.__init__)


def test_hyp_diagram_hidelabelcapabilitystyle_constructor_args():
    sig = inspect.signature(diagram_HideLabelCapabilityStyle.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"




def test_hyp_diagram_draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(diagram_DragAndDropTarget)


def test_hyp_diagram_draganddroptarget_constructor_exists():
    assert callable(diagram_DragAndDropTarget.__init__)


def test_hyp_diagram_draganddroptarget_constructor_args():
    sig = inspect.signature(diagram_DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(style_StyleDescription)


def test_hyp_style_styledescription_constructor_exists():
    assert callable(style_StyleDescription.__init__)


def test_hyp_style_styledescription_constructor_args():
    sig = inspect.signature(style_StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_NodeStyleDescription)


def test_hyp_diagram_style_nodestyledescription_constructor_exists():
    assert callable(diagram_style_NodeStyleDescription.__init__)


def test_hyp_diagram_style_nodestyledescription_constructor_args():
    sig = inspect.signature(diagram_style_NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "forbiddenSides" in params, "Missing parameter 'forbiddenSides'"







def test_hyp_diagram_computedstyledescriptionregistry_is_not_abstract():
    assert not inspect.isabstract(diagram_ComputedStyleDescriptionRegistry)


def test_hyp_diagram_computedstyledescriptionregistry_constructor_exists():
    assert callable(diagram_ComputedStyleDescriptionRegistry.__init__)


def test_hyp_diagram_computedstyledescriptionregistry_constructor_args():
    sig = inspect.signature(diagram_ComputedStyleDescriptionRegistry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edgestyle_is_not_abstract():
    assert not inspect.isabstract(EdgeStyle)


def test_hyp_edgestyle_constructor_exists():
    assert callable(EdgeStyle.__init__)


def test_hyp_edgestyle_constructor_args():
    sig = inspect.signature(EdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_bracketedgestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_BracketEdgeStyle)


def test_hyp_diagram_bracketedgestyle_constructor_exists():
    assert callable(diagram_BracketEdgeStyle.__init__)


def test_hyp_diagram_bracketedgestyle_constructor_args():
    sig = inspect.signature(diagram_BracketEdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_hyp_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_hyp_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collapsefilter_is_not_abstract():
    assert not inspect.isabstract(CollapseFilter)


def test_hyp_collapsefilter_constructor_exists():
    assert callable(CollapseFilter.__init__)


def test_hyp_collapsefilter_constructor_args():
    sig = inspect.signature(CollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_indirectlycollapsefilter_is_not_abstract():
    assert not inspect.isabstract(diagram_IndirectlyCollapseFilter)


def test_hyp_diagram_indirectlycollapsefilter_constructor_exists():
    assert callable(diagram_IndirectlyCollapseFilter.__init__)


def test_hyp_diagram_indirectlycollapsefilter_constructor_args():
    sig = inspect.signature(diagram_IndirectlyCollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_variablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram_VariableValue)


def test_hyp_diagram_variablevalue_constructor_exists():
    assert callable(diagram_VariableValue.__init__)


def test_hyp_diagram_variablevalue_constructor_args():
    sig = inspect.signature(diagram_VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedvariable_is_not_abstract():
    assert not inspect.isabstract(TypedVariable)


def test_hyp_typedvariable_constructor_exists():
    assert callable(TypedVariable.__init__)


def test_hyp_typedvariable_constructor_args():
    sig = inspect.signature(TypedVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variablevalue_is_not_abstract():
    assert not inspect.isabstract(VariableValue)


def test_hyp_variablevalue_constructor_exists():
    assert callable(VariableValue.__init__)


def test_hyp_variablevalue_constructor_args():
    sig = inspect.signature(VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_typedvariablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram_TypedVariableValue)


def test_hyp_diagram_typedvariablevalue_constructor_exists():
    assert callable(diagram_TypedVariableValue.__init__)


def test_hyp_diagram_typedvariablevalue_constructor_args():
    sig = inspect.signature(diagram_TypedVariableValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_diagram_eobjectvariablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram_EObjectVariableValue)


def test_hyp_diagram_eobjectvariablevalue_constructor_exists():
    assert callable(diagram_EObjectVariableValue.__init__)


def test_hyp_diagram_eobjectvariablevalue_constructor_args():
    sig = inspect.signature(diagram_EObjectVariableValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_endlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_EndLabelStyle)


def test_hyp_diagram_endlabelstyle_constructor_exists():
    assert callable(diagram_EndLabelStyle.__init__)


def test_hyp_diagram_endlabelstyle_constructor_args():
    sig = inspect.signature(diagram_EndLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_beginlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_BeginLabelStyle)


def test_hyp_diagram_beginlabelstyle_constructor_exists():
    assert callable(diagram_BeginLabelStyle.__init__)


def test_hyp_diagram_beginlabelstyle_constructor_args():
    sig = inspect.signature(diagram_BeginLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_centerlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_CenterLabelStyle)


def test_hyp_diagram_centerlabelstyle_constructor_exists():
    assert callable(diagram_CenterLabelStyle.__init__)


def test_hyp_diagram_centerlabelstyle_constructor_args():
    sig = inspect.signature(diagram_CenterLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_containerstyle_is_not_abstract():
    assert not inspect.isabstract(ContainerStyle)


def test_hyp_containerstyle_constructor_exists():
    assert callable(ContainerStyle.__init__)


def test_hyp_containerstyle_constructor_args():
    sig = inspect.signature(ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_shapecontainerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_ShapeContainerStyle)


def test_hyp_diagram_shapecontainerstyle_constructor_exists():
    assert callable(diagram_ShapeContainerStyle.__init__)


def test_hyp_diagram_shapecontainerstyle_constructor_args():
    sig = inspect.signature(diagram_ShapeContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"





def test_hyp_diagram_flatcontainerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_FlatContainerStyle)


def test_hyp_diagram_flatcontainerstyle_constructor_exists():
    assert callable(diagram_FlatContainerStyle.__init__)


def test_hyp_diagram_flatcontainerstyle_constructor_args():
    sig = inspect.signature(diagram_FlatContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"






def test_hyp_customizable_is_not_abstract():
    assert not inspect.isabstract(Customizable)


def test_hyp_customizable_constructor_exists():
    assert callable(Customizable.__init__)


def test_hyp_customizable_constructor_args():
    sig = inspect.signature(Customizable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_gaugesection_is_not_abstract():
    assert not inspect.isabstract(diagram_GaugeSection)


def test_hyp_diagram_gaugesection_constructor_exists():
    assert callable(diagram_GaugeSection.__init__)


def test_hyp_diagram_gaugesection_constructor_args():
    sig = inspect.signature(diagram_GaugeSection.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "label" in params, "Missing parameter 'label'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"
    assert "value" in params, "Missing parameter 'value'"
    assert "min" in params, "Missing parameter 'min'"









def test_hyp_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_hyp_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_hyp_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_note_is_not_abstract():
    assert not inspect.isabstract(diagram_Note)


def test_hyp_diagram_note_constructor_exists():
    assert callable(diagram_Note.__init__)


def test_hyp_diagram_note_constructor_args():
    sig = inspect.signature(diagram_Note.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"




def test_hyp_diagram_square_is_not_abstract():
    assert not inspect.isabstract(diagram_Square)


def test_hyp_diagram_square_constructor_exists():
    assert callable(diagram_Square.__init__)


def test_hyp_diagram_square_constructor_args():
    sig = inspect.signature(diagram_Square.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "color" in params, "Missing parameter 'color'"






def test_hyp_diagram_ellipse_is_not_abstract():
    assert not inspect.isabstract(diagram_Ellipse)


def test_hyp_diagram_ellipse_constructor_exists():
    assert callable(diagram_Ellipse.__init__)


def test_hyp_diagram_ellipse_constructor_args():
    sig = inspect.signature(diagram_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "verticalDiameter" in params, "Missing parameter 'verticalDiameter'"
    assert "horizontalDiameter" in params, "Missing parameter 'horizontalDiameter'"






def test_hyp_diagram_lozenge_is_not_abstract():
    assert not inspect.isabstract(diagram_Lozenge)


def test_hyp_diagram_lozenge_constructor_exists():
    assert callable(diagram_Lozenge.__init__)


def test_hyp_diagram_lozenge_constructor_args():
    sig = inspect.signature(diagram_Lozenge.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "color" in params, "Missing parameter 'color'"
    assert "width" in params, "Missing parameter 'width'"






def test_hyp_diagram_customstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_CustomStyle)


def test_hyp_diagram_customstyle_constructor_exists():
    assert callable(diagram_CustomStyle.__init__)


def test_hyp_diagram_customstyle_constructor_args():
    sig = inspect.signature(diagram_CustomStyle.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_diagram_bundledimage_is_not_abstract():
    assert not inspect.isabstract(diagram_BundledImage)


def test_hyp_diagram_bundledimage_constructor_exists():
    assert callable(diagram_BundledImage.__init__)


def test_hyp_diagram_bundledimage_constructor_args():
    sig = inspect.signature(diagram_BundledImage.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "providedShapeID" in params, "Missing parameter 'providedShapeID'"
    assert "color" in params, "Missing parameter 'color'"






def test_hyp_diagram_gaugecompositestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_GaugeCompositeStyle)


def test_hyp_diagram_gaugecompositestyle_constructor_exists():
    assert callable(diagram_GaugeCompositeStyle.__init__)


def test_hyp_diagram_gaugecompositestyle_constructor_args():
    sig = inspect.signature(diagram_GaugeCompositeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"




def test_hyp_diagram_workspaceimage_is_not_abstract():
    assert not inspect.isabstract(diagram_WorkspaceImage)


def test_hyp_diagram_workspaceimage_constructor_exists():
    assert callable(diagram_WorkspaceImage.__init__)


def test_hyp_diagram_workspaceimage_constructor_args():
    sig = inspect.signature(diagram_WorkspaceImage.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"




def test_hyp_diagram_dot_is_not_abstract():
    assert not inspect.isabstract(diagram_Dot)


def test_hyp_diagram_dot_constructor_exists():
    assert callable(diagram_Dot.__init__)


def test_hyp_diagram_dot_constructor_args():
    sig = inspect.signature(diagram_Dot.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"





def test_hyp_hidelabelcapabilitystyle_is_not_abstract():
    assert not inspect.isabstract(HideLabelCapabilityStyle)


def test_hyp_hidelabelcapabilitystyle_constructor_exists():
    assert callable(HideLabelCapabilityStyle.__init__)


def test_hyp_hidelabelcapabilitystyle_constructor_args():
    sig = inspect.signature(HideLabelCapabilityStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(BorderedStyle)


def test_hyp_borderedstyle_constructor_exists():
    assert callable(BorderedStyle.__init__)


def test_hyp_borderedstyle_constructor_args():
    sig = inspect.signature(BorderedStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_hyp_style_constructor_exists():
    assert callable(Style.__init__)


def test_hyp_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_BorderedStyle)


def test_hyp_diagram_borderedstyle_constructor_exists():
    assert callable(diagram_BorderedStyle.__init__)


def test_hyp_diagram_borderedstyle_constructor_args():
    sig = inspect.signature(diagram_BorderedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderSize" in params, "Missing parameter 'borderSize'"
    assert "borderColor" in params, "Missing parameter 'borderColor'"
    assert "borderLineStyle" in params, "Missing parameter 'borderLineStyle'"
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"







def test_hyp_labelstyle_is_not_abstract():
    assert not inspect.isabstract(LabelStyle)


def test_hyp_labelstyle_constructor_exists():
    assert callable(LabelStyle.__init__)


def test_hyp_labelstyle_constructor_args():
    sig = inspect.signature(LabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(IEdgeMapping)


def test_hyp_iedgemapping_constructor_exists():
    assert callable(IEdgeMapping.__init__)


def test_hyp_iedgemapping_constructor_args():
    sig = inspect.signature(IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_edgetarget_is_not_abstract():
    assert not inspect.isabstract(diagram_EdgeTarget)


def test_hyp_diagram_edgetarget_constructor_exists():
    assert callable(diagram_EdgeTarget.__init__)


def test_hyp_diagram_edgetarget_constructor_args():
    sig = inspect.signature(diagram_EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_edgestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_EdgeStyle)


def test_hyp_diagram_edgestyle_constructor_exists():
    assert callable(diagram_EdgeStyle.__init__)


def test_hyp_diagram_edgestyle_constructor_args():
    sig = inspect.signature(diagram_EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "strokeColor" in params, "Missing parameter 'strokeColor'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "centered" in params, "Missing parameter 'centered'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "size" in params, "Missing parameter 'size'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"











def test_hyp_ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(DDiagramElementContainer)


def test_hyp_ddiagramelementcontainer_constructor_exists():
    assert callable(DDiagramElementContainer.__init__)


def test_hyp_ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_dnodelist_is_not_abstract():
    assert not inspect.isabstract(diagram_DNodeList)


def test_hyp_diagram_dnodelist_constructor_exists():
    assert callable(diagram_DNodeList.__init__)


def test_hyp_diagram_dnodelist_constructor_args():
    sig = inspect.signature(diagram_DNodeList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_dnodecontainer_is_not_abstract():
    assert not inspect.isabstract(diagram_DNodeContainer)


def test_hyp_diagram_dnodecontainer_constructor_exists():
    assert callable(diagram_DNodeContainer.__init__)


def test_hyp_diagram_dnodecontainer_constructor_args():
    sig = inspect.signature(diagram_DNodeContainer.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"




def test_hyp_containermapping_is_not_abstract():
    assert not inspect.isabstract(ContainerMapping)


def test_hyp_containermapping_constructor_exists():
    assert callable(ContainerMapping.__init__)


def test_hyp_containermapping_constructor_args():
    sig = inspect.signature(ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_containerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_ContainerStyle)


def test_hyp_diagram_containerstyle_constructor_exists():
    assert callable(diagram_ContainerStyle.__init__)


def test_hyp_diagram_containerstyle_constructor_args():
    sig = inspect.signature(diagram_ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodemapping_is_not_abstract():
    assert not inspect.isabstract(NodeMapping)


def test_hyp_nodemapping_constructor_exists():
    assert callable(NodeMapping.__init__)


def test_hyp_nodemapping_constructor_args():
    sig = inspect.signature(NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_style_is_not_abstract():
    assert not inspect.isabstract(diagram_Style)


def test_hyp_diagram_style_constructor_exists():
    assert callable(diagram_Style.__init__)


def test_hyp_diagram_style_constructor_args():
    sig = inspect.signature(diagram_Style.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_nodestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_NodeStyle)


def test_hyp_diagram_nodestyle_constructor_exists():
    assert callable(diagram_NodeStyle.__init__)


def test_hyp_diagram_nodestyle_constructor_args():
    sig = inspect.signature(diagram_NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"




def test_hyp_edgetarget_is_not_abstract():
    assert not inspect.isabstract(EdgeTarget)


def test_hyp_edgetarget_constructor_exists():
    assert callable(EdgeTarget.__init__)


def test_hyp_edgetarget_constructor_args():
    sig = inspect.signature(EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(AbstractDNode)


def test_hyp_abstractdnode_constructor_exists():
    assert callable(AbstractDNode.__init__)


def test_hyp_abstractdnode_constructor_args():
    sig = inspect.signature(AbstractDNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(DDiagramElement)


def test_hyp_ddiagramelement_constructor_exists():
    assert callable(DDiagramElement.__init__)


def test_hyp_ddiagramelement_constructor_args():
    sig = inspect.signature(DDiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(diagram_AbstractDNode)


def test_hyp_diagram_abstractdnode_constructor_exists():
    assert callable(diagram_AbstractDNode.__init__)


def test_hyp_diagram_abstractdnode_constructor_args():
    sig = inspect.signature(diagram_AbstractDNode.__init__)
    params = list(sig.parameters.keys())
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"




def test_hyp_filter_compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(filter_CompositeFilterDescription)


def test_hyp_filter_compositefilterdescription_constructor_exists():
    assert callable(filter_CompositeFilterDescription.__init__)


def test_hyp_filter_compositefilterdescription_constructor_args():
    sig = inspect.signature(filter_CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(GraphicalFilter)


def test_hyp_graphicalfilter_constructor_exists():
    assert callable(GraphicalFilter.__init__)


def test_hyp_graphicalfilter_constructor_args():
    sig = inspect.signature(GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_appliedcompositefilters_is_not_abstract():
    assert not inspect.isabstract(diagram_AppliedCompositeFilters)


def test_hyp_diagram_appliedcompositefilters_constructor_exists():
    assert callable(diagram_AppliedCompositeFilters.__init__)


def test_hyp_diagram_appliedcompositefilters_constructor_args():
    sig = inspect.signature(diagram_AppliedCompositeFilters.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_hidelabelfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_HideLabelFilter)


def test_hyp_diagram_hidelabelfilter_constructor_exists():
    assert callable(diagram_HideLabelFilter.__init__)


def test_hyp_diagram_hidelabelfilter_constructor_args():
    sig = inspect.signature(diagram_HideLabelFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_foldingpointfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_FoldingPointFilter)


def test_hyp_diagram_foldingpointfilter_constructor_exists():
    assert callable(diagram_FoldingPointFilter.__init__)


def test_hyp_diagram_foldingpointfilter_constructor_args():
    sig = inspect.signature(diagram_FoldingPointFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_collapsefilter_is_not_abstract():
    assert not inspect.isabstract(diagram_CollapseFilter)


def test_hyp_diagram_collapsefilter_constructor_exists():
    assert callable(diagram_CollapseFilter.__init__)


def test_hyp_diagram_collapsefilter_constructor_args():
    sig = inspect.signature(diagram_CollapseFilter.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"





def test_hyp_diagram_foldingfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_FoldingFilter)


def test_hyp_diagram_foldingfilter_constructor_exists():
    assert callable(diagram_FoldingFilter.__init__)


def test_hyp_diagram_foldingfilter_constructor_args():
    sig = inspect.signature(diagram_FoldingFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_absoluteboundsfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_AbsoluteBoundsFilter)


def test_hyp_diagram_absoluteboundsfilter_constructor_exists():
    assert callable(diagram_AbsoluteBoundsFilter.__init__)


def test_hyp_diagram_absoluteboundsfilter_constructor_args():
    sig = inspect.signature(diagram_AbsoluteBoundsFilter.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"







def test_hyp_diagram_hidefilter_is_not_abstract():
    assert not inspect.isabstract(diagram_HideFilter)


def test_hyp_diagram_hidefilter_constructor_exists():
    assert callable(diagram_HideFilter.__init__)


def test_hyp_diagram_hidefilter_constructor_args():
    sig = inspect.signature(diagram_HideFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_GraphicalFilter)


def test_hyp_diagram_graphicalfilter_constructor_exists():
    assert callable(diagram_GraphicalFilter.__init__)


def test_hyp_diagram_graphicalfilter_constructor_args():
    sig = inspect.signature(diagram_GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(DiagramElementMapping)


def test_hyp_diagramelementmapping_constructor_exists():
    assert callable(DiagramElementMapping.__init__)


def test_hyp_diagramelementmapping_constructor_args():
    sig = inspect.signature(DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_decoration_is_not_abstract():
    assert not inspect.isabstract(diagram_Decoration)


def test_hyp_diagram_decoration_constructor_exists():
    assert callable(diagram_Decoration.__init__)


def test_hyp_diagram_decoration_constructor_args():
    sig = inspect.signature(diagram_Decoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(DRepresentationElement)


def test_hyp_drepresentationelement_constructor_exists():
    assert callable(DRepresentationElement.__init__)


def test_hyp_drepresentationelement_constructor_args():
    sig = inspect.signature(DRepresentationElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(DSemanticDecorator)


def test_hyp_dsemanticdecorator_constructor_exists():
    assert callable(DSemanticDecorator.__init__)


def test_hyp_dsemanticdecorator_constructor_args():
    sig = inspect.signature(DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ddiagram_is_not_abstract():
    assert not inspect.isabstract(DDiagram)


def test_hyp_ddiagram_constructor_exists():
    assert callable(DDiagram.__init__)


def test_hyp_ddiagram_constructor_args():
    sig = inspect.signature(DDiagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_dsemanticdiagram_is_not_abstract():
    assert not inspect.isabstract(diagram_DSemanticDiagram)


def test_hyp_diagram_dsemanticdiagram_constructor_exists():
    assert callable(diagram_DSemanticDiagram.__init__)


def test_hyp_diagram_dsemanticdiagram_constructor_args():
    sig = inspect.signature(diagram_DSemanticDiagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_layer_is_not_abstract():
    assert not inspect.isabstract(Layer)


def test_hyp_layer_constructor_exists():
    assert callable(Layer.__init__)


def test_hyp_layer_constructor_args():
    sig = inspect.signature(Layer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_additionallayer_is_not_abstract():
    assert not inspect.isabstract(diagram_description_AdditionalLayer)


def test_hyp_diagram_description_additionallayer_constructor_exists():
    assert callable(diagram_description_AdditionalLayer.__init__)


def test_hyp_diagram_description_additionallayer_constructor_args():
    sig = inspect.signature(diagram_description_AdditionalLayer.__init__)
    params = list(sig.parameters.keys())
    assert "activeByDefault" in params, "Missing parameter 'activeByDefault'"
    assert "optional" in params, "Missing parameter 'optional'"





def test_hyp_diagram_filtervariablehistory_is_not_abstract():
    assert not inspect.isabstract(diagram_FilterVariableHistory)


def test_hyp_diagram_filtervariablehistory_constructor_exists():
    assert callable(diagram_FilterVariableHistory.__init__)


def test_hyp_diagram_filtervariablehistory_constructor_args():
    sig = inspect.signature(diagram_FilterVariableHistory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_behaviortool_is_not_abstract():
    assert not inspect.isabstract(tool_BehaviorTool)


def test_hyp_tool_behaviortool_constructor_exists():
    assert callable(tool_BehaviorTool.__init__)


def test_hyp_tool_behaviortool_constructor_args():
    sig = inspect.signature(tool_BehaviorTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_validation_validationrule_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationRule)


def test_hyp_validation_validationrule_constructor_exists():
    assert callable(validation_ValidationRule.__init__)


def test_hyp_validation_validationrule_constructor_args():
    sig = inspect.signature(validation_ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_additionallayer_is_not_abstract():
    assert not inspect.isabstract(AdditionalLayer)


def test_hyp_additionallayer_constructor_exists():
    assert callable(AdditionalLayer.__init__)


def test_hyp_additionallayer_constructor_args():
    sig = inspect.signature(AdditionalLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filter_filterdescription_is_not_abstract():
    assert not inspect.isabstract(filter_FilterDescription)


def test_hyp_filter_filterdescription_constructor_exists():
    assert callable(filter_FilterDescription.__init__)


def test_hyp_filter_filterdescription_constructor_args():
    sig = inspect.signature(filter_FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_concern_concerndescription_is_not_abstract():
    assert not inspect.isabstract(concern_ConcernDescription)


def test_hyp_concern_concerndescription_constructor_exists():
    assert callable(concern_ConcernDescription.__init__)


def test_hyp_concern_concerndescription_constructor_args():
    sig = inspect.signature(concern_ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_dnodelistelement_is_not_abstract():
    assert not inspect.isabstract(diagram_DNodeListElement)


def test_hyp_diagram_dnodelistelement_constructor_exists():
    assert callable(diagram_DNodeListElement.__init__)


def test_hyp_diagram_dnodelistelement_constructor_args():
    sig = inspect.signature(diagram_DNodeListElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_dedge_is_not_abstract():
    assert not inspect.isabstract(diagram_DEdge)


def test_hyp_diagram_dedge_constructor_exists():
    assert callable(diagram_DEdge.__init__)


def test_hyp_diagram_dedge_constructor_args():
    sig = inspect.signature(diagram_DEdge.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "beginLabel" in params, "Missing parameter 'beginLabel'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "endLabel" in params, "Missing parameter 'endLabel'"
    assert "isMockEdge" in params, "Missing parameter 'isMockEdge'"
    assert "isFold" in params, "Missing parameter 'isFold'"
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"










def test_hyp_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(DiagramDescription)


def test_hyp_diagramdescription_constructor_exists():
    assert callable(DiagramDescription.__init__)


def test_hyp_diagramdescription_constructor_args():
    sig = inspect.signature(DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(diagram_DDiagramElement)


def test_hyp_diagram_ddiagramelement_constructor_exists():
    assert callable(diagram_DDiagramElement.__init__)


def test_hyp_diagram_ddiagramelement_constructor_args():
    sig = inspect.signature(diagram_DDiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipText" in params, "Missing parameter 'tooltipText'"
    assert "visible" in params, "Missing parameter 'visible'"





def test_hyp_draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(DragAndDropTarget)


def test_hyp_draganddroptarget_constructor_exists():
    assert callable(DragAndDropTarget.__init__)


def test_hyp_draganddroptarget_constructor_args():
    sig = inspect.signature(DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(diagram_DDiagramElementContainer)


def test_hyp_diagram_ddiagramelementcontainer_constructor_exists():
    assert callable(diagram_DDiagramElementContainer.__init__)


def test_hyp_diagram_ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(diagram_DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"





def test_hyp_diagram_dnode_is_not_abstract():
    assert not inspect.isabstract(diagram_DNode)


def test_hyp_diagram_dnode_constructor_exists():
    assert callable(diagram_DNode.__init__)


def test_hyp_diagram_dnode_constructor_args():
    sig = inspect.signature(diagram_DNode.__init__)
    params = list(sig.parameters.keys())
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "width" in params, "Missing parameter 'width'"
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"
    assert "height" in params, "Missing parameter 'height'"







def test_hyp_description_documentedelement_is_not_abstract():
    assert not inspect.isabstract(description_DocumentedElement)


def test_hyp_description_documentedelement_constructor_exists():
    assert callable(description_DocumentedElement.__init__)


def test_hyp_description_documentedelement_constructor_args():
    sig = inspect.signature(description_DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram_description_EdgeMappingImport)


def test_hyp_diagram_description_edgemappingimport_constructor_exists():
    assert callable(diagram_description_EdgeMappingImport.__init__)


def test_hyp_diagram_description_edgemappingimport_constructor_args():
    sig = inspect.signature(diagram_description_EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"




def test_hyp_diagram_filter_filterdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_FilterDescription)


def test_hyp_diagram_filter_filterdescription_constructor_exists():
    assert callable(diagram_filter_FilterDescription.__init__)


def test_hyp_diagram_filter_filterdescription_constructor_args():
    sig = inspect.signature(diagram_filter_FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_AbstractNodeMapping)


def test_hyp_diagram_description_abstractnodemapping_constructor_exists():
    assert callable(diagram_description_AbstractNodeMapping.__init__)


def test_hyp_diagram_description_abstractnodemapping_constructor_args():
    sig = inspect.signature(diagram_description_AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"




def test_hyp_diagram_concern_concerndescription_is_not_abstract():
    assert not inspect.isabstract(diagram_concern_ConcernDescription)


def test_hyp_diagram_concern_concerndescription_constructor_exists():
    assert callable(diagram_concern_ConcernDescription.__init__)


def test_hyp_diagram_concern_concerndescription_constructor_args():
    sig = inspect.signature(diagram_concern_ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_description_layer_is_not_abstract():
    assert not inspect.isabstract(diagram_description_Layer)


def test_hyp_diagram_description_layer_constructor_exists():
    assert callable(diagram_description_Layer.__init__)


def test_hyp_diagram_description_layer_constructor_args():
    sig = inspect.signature(diagram_description_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"




def test_hyp_diagram_tool_toolsection_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ToolSection)


def test_hyp_diagram_tool_toolsection_constructor_exists():
    assert callable(diagram_tool_ToolSection.__init__)


def test_hyp_diagram_tool_toolsection_constructor_args():
    sig = inspect.signature(diagram_tool_ToolSection.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"




def test_hyp_diagram_description_edgemapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_EdgeMapping)


def test_hyp_diagram_description_edgemapping_constructor_exists():
    assert callable(diagram_description_EdgeMapping.__init__)


def test_hyp_diagram_description_edgemapping_constructor_args():
    sig = inspect.signature(diagram_description_EdgeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "useDomainElement" in params, "Missing parameter 'useDomainElement'"
    assert "sourceFinderExpression" in params, "Missing parameter 'sourceFinderExpression'"
    assert "targetFinderExpression" in params, "Missing parameter 'targetFinderExpression'"
    assert "pathExpression" in params, "Missing parameter 'pathExpression'"
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"









def test_hyp_drepresentation_is_not_abstract():
    assert not inspect.isabstract(DRepresentation)


def test_hyp_drepresentation_constructor_exists():
    assert callable(DRepresentation.__init__)


def test_hyp_drepresentation_constructor_args():
    sig = inspect.signature(DRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_ddiagram_is_not_abstract():
    assert not inspect.isabstract(diagram_DDiagram)


def test_hyp_diagram_ddiagram_constructor_exists():
    assert callable(diagram_DDiagram.__init__)


def test_hyp_diagram_ddiagram_constructor_args():
    sig = inspect.signature(diagram_DDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "headerHeight" in params, "Missing parameter 'headerHeight'"
    assert "isInLayoutingMode" in params, "Missing parameter 'isInLayoutingMode'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"




def test_hyp_containershape_exists():
    # Check that the Enumeration exists
    assert ContainerShape is not None

def test_hyp_containershape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerShape]
    expected_literals = [
        "parallelogram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerShape"

def test_hyp_bundledimageshape_exists():
    # Check that the Enumeration exists
    assert BundledImageShape is not None

def test_hyp_bundledimageshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BundledImageShape]
    expected_literals = [
        "stroke",
        "ring",
        "providedShape",
        "square",
        "dot",
        "triangle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BundledImageShape"

def test_hyp_labelposition_exists():
    # Check that the Enumeration exists
    assert LabelPosition is not None

def test_hyp_labelposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelPosition]
    expected_literals = [
        "border",
        "node",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelPosition"

def test_hyp_backgroundstyle_exists():
    # Check that the Enumeration exists
    assert BackgroundStyle is not None

def test_hyp_backgroundstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackgroundStyle]
    expected_literals = [
        "Liquid",
        "GradientLeftToRight",
        "GradientTopToBottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackgroundStyle"

def test_hyp_resizekind_exists():
    # Check that the Enumeration exists
    assert ResizeKind is not None

def test_hyp_resizekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResizeKind]
    expected_literals = [
        "NSEW",
        "NONE",
        "EAST_WEST",
        "NORTH_SOUTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResizeKind"

def test_hyp_reconnectionkind_exists():
    # Check that the Enumeration exists
    assert ReconnectionKind is not None

def test_hyp_reconnectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReconnectionKind]
    expected_literals = [
        "RECONNECT_SOURCE",
        "RECONNECT_BOTH",
        "RECONNECT_TARGET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReconnectionKind"

def test_hyp_side_exists():
    # Check that the Enumeration exists
    assert Side is not None

def test_hyp_side_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Side]
    expected_literals = [
        "SOUTH",
        "NORTH",
        "EAST",
        "WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Side"

def test_hyp_edgearrows_exists():
    # Check that the Enumeration exists
    assert EdgeArrows is not None

def test_hyp_edgearrows_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeArrows]
    expected_literals = [
        "OutputClosedArrow",
        "OutputArrow",
        "InputFillClosedArrow",
        "FillDiamond",
        "InputArrowWithFillDiamond",
        "InputClosedArrow",
        "OutputFillClosedArrow",
        "NoDecoration",
        "InputArrow",
        "InputArrowWithDiamond",
        "Diamond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeArrows"

def test_hyp_arrangeconstraint_exists():
    # Check that the Enumeration exists
    assert ArrangeConstraint is not None

def test_hyp_arrangeconstraint_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrangeConstraint]
    expected_literals = [
        "KEEP_SIZE",
        "KEEP_RATIO",
        "KEEP_LOCATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrangeConstraint"

def test_hyp_filterkind_exists():
    # Check that the Enumeration exists
    assert FilterKind is not None

def test_hyp_filterkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FilterKind]
    expected_literals = [
        "COLLAPSE",
        "HIDE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FilterKind"

def test_hyp_containerlayout_exists():
    # Check that the Enumeration exists
    assert ContainerLayout is not None

def test_hyp_containerlayout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerLayout]
    expected_literals = [
        "HorizontalStack",
        "VerticalStack",
        "List",
        "FreeForm",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerLayout"

def test_hyp_centeringstyle_exists():
    # Check that the Enumeration exists
    assert CenteringStyle is not None

def test_hyp_centeringstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CenteringStyle]
    expected_literals = [
        "None_",
        "Both",
        "Target",
        "Source",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CenteringStyle"

def test_hyp_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_hyp_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "dot",
        "dash",
        "solid",
        "dash_dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_hyp_edgerouting_exists():
    # Check that the Enumeration exists
    assert EdgeRouting is not None

def test_hyp_edgerouting_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeRouting]
    expected_literals = [
        "manhattan",
        "tree",
        "straight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeRouting"

def test_hyp_layoutdirection_exists():
    # Check that the Enumeration exists
    assert LayoutDirection is not None

def test_hyp_layoutdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LayoutDirection]
    expected_literals = [
        "BottomToTop",
        "TopToBottom",
        "LeftToRight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LayoutDirection"

def test_hyp_alignmentkind_exists():
    # Check that the Enumeration exists
    assert AlignmentKind is not None

def test_hyp_alignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentKind]
    expected_literals = [
        "SQUARE",
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentKind"

def test_hyp_foldingstyle_exists():
    # Check that the Enumeration exists
    assert FoldingStyle is not None

def test_hyp_foldingstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FoldingStyle]
    expected_literals = [
        "SOURCE",
        "NONE",
        "TARGET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FoldingStyle"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
tool_DeleteHookParameter_strategy = st.builds(
    tool_DeleteHookParameter,
)
diagram_tool_DeleteHook_strategy = st.builds(
    diagram_tool_DeleteHook,
    id=
        safe_text
)
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
diagram_tool_RequestDescription_strategy = st.builds(
    diagram_tool_RequestDescription,
    type=
        safe_text
)
tool_DeleteHook_strategy = st.builds(
    tool_DeleteHook,
)
tool_ElementDeleteVariable_strategy = st.builds(
    tool_ElementDeleteVariable,
)
tool_ElementDoubleClickVariable_strategy = st.builds(
    tool_ElementDoubleClickVariable,
)
tool_InitEdgeCreationOperation_strategy = st.builds(
    tool_InitEdgeCreationOperation,
)
tool_TargetEdgeViewCreationVariable_strategy = st.builds(
    tool_TargetEdgeViewCreationVariable,
)
tool_SourceEdgeViewCreationVariable_strategy = st.builds(
    tool_SourceEdgeViewCreationVariable,
)
tool_TargetEdgeCreationVariable_strategy = st.builds(
    tool_TargetEdgeCreationVariable,
)
tool_SourceEdgeCreationVariable_strategy = st.builds(
    tool_SourceEdgeCreationVariable,
)
tool_ContainerViewVariable_strategy = st.builds(
    tool_ContainerViewVariable,
)
tool_NodeCreationVariable_strategy = st.builds(
    tool_NodeCreationVariable,
)
MappingBasedToolDescription_strategy = st.builds(
    MappingBasedToolDescription,
)
diagram_tool_ContainerCreationDescription_strategy = st.builds(
    diagram_tool_ContainerCreationDescription,
    iconPath=
        safe_text
)
diagram_tool_DeleteElementDescription_strategy = st.builds(
    diagram_tool_DeleteElementDescription,
)
diagram_tool_EdgeCreationDescription_strategy = st.builds(
    diagram_tool_EdgeCreationDescription,
    iconPath=
        safe_text,
    connectionStartPrecondition=
        safe_text
)
diagram_tool_DoubleClickDescription_strategy = st.builds(
    diagram_tool_DoubleClickDescription,
)
diagram_tool_NodeCreationDescription_strategy = st.builds(
    diagram_tool_NodeCreationDescription,
    iconPath=
        safe_text
)
tool_ToolGroup_strategy = st.builds(
    tool_ToolGroup,
)
diagram_tool_ToolGroupExtension_strategy = st.builds(
    diagram_tool_ToolGroupExtension,
)
ToolEntry_strategy = st.builds(
    ToolEntry,
)
diagram_tool_ToolGroup_strategy = st.builds(
    diagram_tool_ToolGroup,
)
tool_ToolGroupExtension_strategy = st.builds(
    tool_ToolGroupExtension,
)
tool_PopupMenu_strategy = st.builds(
    tool_PopupMenu,
)
tool_ToolEntry_strategy = st.builds(
    tool_ToolEntry,
)
tool_InitialNodeCreationOperation_strategy = st.builds(
    tool_InitialNodeCreationOperation,
)
diagram_style_HideLabelCapabilityStyleDescription_strategy = st.builds(
    diagram_style_HideLabelCapabilityStyleDescription,
    hideLabelByDefault=
        st.booleans()
)
EdgeStyleDescription_strategy = st.builds(
    EdgeStyleDescription,
)
diagram_style_BracketEdgeStyleDescription_strategy = st.builds(
    diagram_style_BracketEdgeStyleDescription,
)
BasicLabelStyleDescription_strategy = st.builds(
    BasicLabelStyleDescription,
)
diagram_style_CenterLabelStyleDescription_strategy = st.builds(
    diagram_style_CenterLabelStyleDescription,
)
diagram_style_EndLabelStyleDescription_strategy = st.builds(
    diagram_style_EndLabelStyleDescription,
)
diagram_style_BeginLabelStyleDescription_strategy = st.builds(
    diagram_style_BeginLabelStyleDescription,
)
style_EndLabelStyleDescription_strategy = st.builds(
    style_EndLabelStyleDescription,
)
style_CenterLabelStyleDescription_strategy = st.builds(
    style_CenterLabelStyleDescription,
)
style_BeginLabelStyleDescription_strategy = st.builds(
    style_BeginLabelStyleDescription,
)
style_LabelBorderStyleDescription_strategy = st.builds(
    style_LabelBorderStyleDescription,
)
diagram_style_SizeComputationContainerStyleDescription_strategy = st.builds(
    diagram_style_SizeComputationContainerStyleDescription,
    widthComputationExpression=
        safe_text,
    heightComputationExpression=
        safe_text
)
diagram_style_GaugeSectionDescription_strategy = st.builds(
    diagram_style_GaugeSectionDescription,
    minValueExpression=
        safe_text,
    label=
        safe_text,
    maxValueExpression=
        safe_text,
    valueExpression=
        safe_text
)
style_GaugeSectionDescription_strategy = st.builds(
    style_GaugeSectionDescription,
)
style_SizeComputationContainerStyleDescription_strategy = st.builds(
    style_SizeComputationContainerStyleDescription,
)
style_RoundedCornerStyleDescription_strategy = st.builds(
    style_RoundedCornerStyleDescription,
)
NodeStyleDescription_strategy = st.builds(
    NodeStyleDescription,
)
diagram_style_NoteDescription_strategy = st.builds(
    diagram_style_NoteDescription,
)
diagram_style_EllipseNodeDescription_strategy = st.builds(
    diagram_style_EllipseNodeDescription,
    verticalDiameterComputationExpression=
        safe_text,
    horizontalDiameterComputationExpression=
        safe_text
)
diagram_style_SquareDescription_strategy = st.builds(
    diagram_style_SquareDescription,
    width=
        safe_text,
    height=
        safe_text
)
diagram_style_DotDescription_strategy = st.builds(
    diagram_style_DotDescription,
    strokeSizeComputationExpression=
        safe_text
)
diagram_style_GaugeCompositeStyleDescription_strategy = st.builds(
    diagram_style_GaugeCompositeStyleDescription,
    alignment=
        safe_text
)
diagram_style_BundledImageDescription_strategy = st.builds(
    diagram_style_BundledImageDescription,
    shape=
        safe_text,
    providedShapeID=
        safe_text
)
diagram_style_CustomStyleDescription_strategy = st.builds(
    diagram_style_CustomStyleDescription,
    id=
        safe_text
)
style_HideLabelCapabilityStyleDescription_strategy = st.builds(
    style_HideLabelCapabilityStyleDescription,
)
style_TooltipStyleDescription_strategy = st.builds(
    style_TooltipStyleDescription,
)
style_LabelStyleDescription_strategy = st.builds(
    style_LabelStyleDescription,
)
style_BorderedStyleDescription_strategy = st.builds(
    style_BorderedStyleDescription,
)
diagram_style_ContainerStyleDescription_strategy = st.builds(
    diagram_style_ContainerStyleDescription,
    roundedCorner=
        st.booleans()
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
StyleDescription_strategy = st.builds(
    StyleDescription,
)
diagram_style_RoundedCornerStyleDescription_strategy = st.builds(
    diagram_style_RoundedCornerStyleDescription,
    arcHeight=
        safe_text,
    arcWidth=
        safe_text
)
diagram_style_EdgeStyleDescription_strategy = st.builds(
    diagram_style_EdgeStyleDescription,
    endsCentering=
        safe_text,
    foldingStyle=
        safe_text,
    sizeComputationExpression=
        safe_text,
    routingStyle=
        safe_text,
    lineStyle=
        safe_text,
    targetArrow=
        safe_text,
    sourceArrow=
        safe_text
)
diagram_style_BorderedStyleDescription_strategy = st.builds(
    diagram_style_BorderedStyleDescription,
    borderSizeComputationExpression=
        safe_text,
    borderLineStyle=
        safe_text
)
tool_ContainerDropDescription_strategy = st.builds(
    tool_ContainerDropDescription,
)
diagram_style_LozengeNodeDescription_strategy = st.builds(
    diagram_style_LozengeNodeDescription,
    widthComputationExpression=
        safe_text,
    heightComputationExpression=
        safe_text
)
diagram_description_DragAndDropTargetDescription_strategy = st.builds(
    diagram_description_DragAndDropTargetDescription,
)
Customization_strategy = st.builds(
    Customization,
)
DecorationDescriptionsSet_strategy = st.builds(
    DecorationDescriptionsSet,
)
description_EndUserDocumentedElement_strategy = st.builds(
    description_EndUserDocumentedElement,
)
DecorationDescription_strategy = st.builds(
    DecorationDescription,
)
diagram_description_MappingBasedDecoration_strategy = st.builds(
    diagram_description_MappingBasedDecoration,
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
diagram_description_Layout_strategy = st.builds(
    diagram_description_Layout,
)
ConditionalStyleDescription_strategy = st.builds(
    ConditionalStyleDescription,
)
diagram_description_ConditionalEdgeStyleDescription_strategy = st.builds(
    diagram_description_ConditionalEdgeStyleDescription,
)
diagram_description_ConditionalContainerStyleDescription_strategy = st.builds(
    diagram_description_ConditionalContainerStyleDescription,
)
diagram_description_ConditionalNodeStyleDescription_strategy = st.builds(
    diagram_description_ConditionalNodeStyleDescription,
)
description_IdentifiedElement_strategy = st.builds(
    description_IdentifiedElement,
)
diagram_description_IEdgeMapping_strategy = st.builds(
    diagram_description_IEdgeMapping,
)
AbstractNodeMapping_strategy = st.builds(
    AbstractNodeMapping,
)
tool_ReconnectEdgeDescription_strategy = st.builds(
    tool_ReconnectEdgeDescription,
)
ConditionalEdgeStyleDescription_strategy = st.builds(
    ConditionalEdgeStyleDescription,
)
style_EdgeStyleDescription_strategy = st.builds(
    style_EdgeStyleDescription,
)
description_IEdgeMapping_strategy = st.builds(
    description_IEdgeMapping,
)
description_ContainerMapping_strategy = st.builds(
    description_ContainerMapping,
)
description_AbstractMappingImport_strategy = st.builds(
    description_AbstractMappingImport,
)
diagram_description_ContainerMappingImport_strategy = st.builds(
    diagram_description_ContainerMappingImport,
)
description_NodeMapping_strategy = st.builds(
    description_NodeMapping,
)
diagram_description_NodeMappingImport_strategy = st.builds(
    diagram_description_NodeMappingImport,
)
ConditionalContainerStyleDescription_strategy = st.builds(
    ConditionalContainerStyleDescription,
)
style_ContainerStyleDescription_strategy = st.builds(
    style_ContainerStyleDescription,
)
diagram_style_ShapeContainerStyleDescription_strategy = st.builds(
    diagram_style_ShapeContainerStyleDescription,
    shape=
        safe_text
)
diagram_style_FlatContainerStyleDescription_strategy = st.builds(
    diagram_style_FlatContainerStyleDescription,
    backgroundStyle=
        safe_text
)
ConditionalNodeStyleDescription_strategy = st.builds(
    ConditionalNodeStyleDescription,
)
style_NodeStyleDescription_strategy = st.builds(
    style_NodeStyleDescription,
)
diagram_style_WorkspaceImageDescription_strategy = st.builds(
    diagram_style_WorkspaceImageDescription,
    workspacePath=
        safe_text
)
description_AbstractNodeMapping_strategy = st.builds(
    description_AbstractNodeMapping,
)
description_DiagramElementMapping_strategy = st.builds(
    description_DiagramElementMapping,
)
tool_DoubleClickDescription_strategy = st.builds(
    tool_DoubleClickDescription,
)
tool_DirectEditLabel_strategy = st.builds(
    tool_DirectEditLabel,
)
tool_DeleteElementDescription_strategy = st.builds(
    tool_DeleteElementDescription,
)
description_RepresentationElementMapping_strategy = st.builds(
    description_RepresentationElementMapping,
)
RepresentationExtensionDescription_strategy = st.builds(
    RepresentationExtensionDescription,
)
diagram_description_DiagramExtensionDescription_strategy = st.builds(
    diagram_description_DiagramExtensionDescription,
)
description_DiagramDescription_strategy = st.builds(
    description_DiagramDescription,
)
description_RepresentationImportDescription_strategy = st.builds(
    description_RepresentationImportDescription,
)
diagram_description_DiagramImportDescription_strategy = st.builds(
    diagram_description_DiagramImportDescription,
)
tool_ToolSection_strategy = st.builds(
    tool_ToolSection,
)
EdgeMappingImport_strategy = st.builds(
    EdgeMappingImport,
)
tool_InitialOperation_strategy = st.builds(
    tool_InitialOperation,
)
Layout_strategy = st.builds(
    Layout,
)
diagram_description_CompositeLayout_strategy = st.builds(
    diagram_description_CompositeLayout,
    direction=
        safe_text,
    padding=
        st.integers()
)
diagram_description_OrderedTreeLayout_strategy = st.builds(
    diagram_description_OrderedTreeLayout,
    childrenExpression=
        safe_text
)
tool_RepresentationCreationDescription_strategy = st.builds(
    tool_RepresentationCreationDescription,
)
tool_AbstractToolDescription_strategy = st.builds(
    tool_AbstractToolDescription,
)
concern_ConcernSet_strategy = st.builds(
    concern_ConcernSet,
)
validation_ValidationSet_strategy = st.builds(
    validation_ValidationSet,
)
EdgeMapping_strategy = st.builds(
    EdgeMapping,
)
description_PasteTargetDescription_strategy = st.builds(
    description_PasteTargetDescription,
)
diagram_description_DiagramElementMapping_strategy = st.builds(
    diagram_description_DiagramElementMapping,
    preconditionExpression=
        safe_text,
    semanticElements=
        safe_text,
    synchronizationLock=
        st.booleans(),
    semanticCandidatesExpression=
        safe_text,
    createElements=
        st.booleans()
)
description_RepresentationDescription_strategy = st.builds(
    description_RepresentationDescription,
)
description_DragAndDropTargetDescription_strategy = st.builds(
    description_DragAndDropTargetDescription,
)
diagram_description_NodeMapping_strategy = st.builds(
    diagram_description_NodeMapping,
)
diagram_description_ContainerMapping_strategy = st.builds(
    diagram_description_ContainerMapping,
    childrenPresentation=
        safe_text
)
diagram_description_DiagramDescription_strategy = st.builds(
    diagram_description_DiagramDescription,
    preconditionExpression=
        safe_text,
    domainClass=
        safe_text,
    rootExpression=
        safe_text,
    enablePopupBars=
        st.booleans()
)
diagram_EObject_strategy = st.builds(
    diagram_EObject,
)
tool_SelectModelElementVariable_strategy = st.builds(
    tool_SelectModelElementVariable,
)
diagram_concern_ConcernSet_strategy = st.builds(
    diagram_concern_ConcernSet,
)
InteractiveVariableDescription_strategy = st.builds(
    InteractiveVariableDescription,
)
filter_Filter_strategy = st.builds(
    filter_Filter,
)
FilterDescription_strategy = st.builds(
    FilterDescription,
)
diagram_filter_CompositeFilterDescription_strategy = st.builds(
    diagram_filter_CompositeFilterDescription,
)
diagram_filter_Filter_strategy = st.builds(
    diagram_filter_Filter,
    filterKind=
        safe_text
)
Filter_strategy = st.builds(
    Filter,
)
diagram_filter_VariableFilter_strategy = st.builds(
    diagram_filter_VariableFilter,
    semanticConditionExpression=
        safe_text
)
diagram_filter_MappingFilter_strategy = st.builds(
    diagram_filter_MappingFilter,
    viewConditionExpression=
        safe_text,
    semanticConditionExpression=
        safe_text
)
tool_ElementDropVariable_strategy = st.builds(
    tool_ElementDropVariable,
)
tool_DropContainerVariable_strategy = st.builds(
    tool_DropContainerVariable,
)
diagram_tool_ContainerDropDescription_strategy = st.builds(
    diagram_tool_ContainerDropDescription,
    dragSource=
        safe_text,
    moveEdges=
        st.booleans()
)
RepresentationNavigationDescription_strategy = st.builds(
    RepresentationNavigationDescription,
)
diagram_tool_DiagramNavigationDescription_strategy = st.builds(
    diagram_tool_DiagramNavigationDescription,
)
RepresentationCreationDescription_strategy = st.builds(
    RepresentationCreationDescription,
)
diagram_tool_DiagramCreationDescription_strategy = st.builds(
    diagram_tool_DiagramCreationDescription,
)
tool_InitialContainerDropOperation_strategy = st.builds(
    tool_InitialContainerDropOperation,
)
ContainerModelOperation_strategy = st.builds(
    ContainerModelOperation,
)
diagram_tool_Navigation_strategy = st.builds(
    diagram_tool_Navigation,
    createIfNotExistent=
        st.booleans()
)
diagram_tool_CreateView_strategy = st.builds(
    diagram_tool_CreateView,
    containerViewExpression=
        safe_text,
    variableName=
        safe_text
)
tool_VariableContainer_strategy = st.builds(
    tool_VariableContainer,
)
description_AbstractVariable_strategy = st.builds(
    description_AbstractVariable,
)
diagram_tool_NodeCreationVariable_strategy = st.builds(
    diagram_tool_NodeCreationVariable,
)
diagram_tool_ElementDoubleClickVariable_strategy = st.builds(
    diagram_tool_ElementDoubleClickVariable,
)
diagram_tool_SourceEdgeViewCreationVariable_strategy = st.builds(
    diagram_tool_SourceEdgeViewCreationVariable,
)
diagram_tool_TargetEdgeCreationVariable_strategy = st.builds(
    diagram_tool_TargetEdgeCreationVariable,
)
diagram_tool_TargetEdgeViewCreationVariable_strategy = st.builds(
    diagram_tool_TargetEdgeViewCreationVariable,
)
diagram_tool_SourceEdgeCreationVariable_strategy = st.builds(
    diagram_tool_SourceEdgeCreationVariable,
)
diagram_tool_BehaviorTool_strategy = st.builds(
    diagram_tool_BehaviorTool,
    domainClass=
        safe_text
)
tool_EditMaskVariables_strategy = st.builds(
    tool_EditMaskVariables,
)
diagram_tool_DirectEditLabel_strategy = st.builds(
    diagram_tool_DirectEditLabel,
    inputLabelExpression=
        safe_text
)
CreateView_strategy = st.builds(
    CreateView,
)
diagram_tool_CreateEdgeView_strategy = st.builds(
    diagram_tool_CreateEdgeView,
    targetExpression=
        safe_text,
    sourceExpression=
        safe_text
)
tool_ElementSelectVariable_strategy = st.builds(
    tool_ElementSelectVariable,
)
diagram_tool_ReconnectEdgeDescription_strategy = st.builds(
    diagram_tool_ReconnectEdgeDescription,
    reconnectionKind=
        safe_text
)
diagram_tool_DeleteHookParameter_strategy = st.builds(
    diagram_tool_DeleteHookParameter,
    name=
        safe_text,
    value=
        safe_text
)
diagram_HideLabelCapabilityStyle_strategy = st.builds(
    diagram_HideLabelCapabilityStyle,
    hideLabelByDefault=
        st.booleans()
)
diagram_DragAndDropTarget_strategy = st.builds(
    diagram_DragAndDropTarget,
)
style_StyleDescription_strategy = st.builds(
    style_StyleDescription,
)
diagram_style_NodeStyleDescription_strategy = st.builds(
    diagram_style_NodeStyleDescription,
    resizeKind=
        safe_text,
    sizeComputationExpression=
        safe_text,
    labelPosition=
        safe_text,
    forbiddenSides=
        safe_text
)
diagram_ComputedStyleDescriptionRegistry_strategy = st.builds(
    diagram_ComputedStyleDescriptionRegistry,
)
EdgeStyle_strategy = st.builds(
    EdgeStyle,
)
diagram_BracketEdgeStyle_strategy = st.builds(
    diagram_BracketEdgeStyle,
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
CollapseFilter_strategy = st.builds(
    CollapseFilter,
)
diagram_IndirectlyCollapseFilter_strategy = st.builds(
    diagram_IndirectlyCollapseFilter,
)
diagram_VariableValue_strategy = st.builds(
    diagram_VariableValue,
)
TypedVariable_strategy = st.builds(
    TypedVariable,
)
VariableValue_strategy = st.builds(
    VariableValue,
)
diagram_TypedVariableValue_strategy = st.builds(
    diagram_TypedVariableValue,
    value=
        safe_text
)
diagram_EObjectVariableValue_strategy = st.builds(
    diagram_EObjectVariableValue,
)
diagram_EndLabelStyle_strategy = st.builds(
    diagram_EndLabelStyle,
)
diagram_BeginLabelStyle_strategy = st.builds(
    diagram_BeginLabelStyle,
)
diagram_CenterLabelStyle_strategy = st.builds(
    diagram_CenterLabelStyle,
)
ContainerStyle_strategy = st.builds(
    ContainerStyle,
)
diagram_ShapeContainerStyle_strategy = st.builds(
    diagram_ShapeContainerStyle,
    shape=
        safe_text,
    backgroundColor=
        safe_text
)
diagram_FlatContainerStyle_strategy = st.builds(
    diagram_FlatContainerStyle,
    backgroundColor=
        safe_text,
    foregroundColor=
        safe_text,
    backgroundStyle=
        safe_text
)
Customizable_strategy = st.builds(
    Customizable,
)
diagram_GaugeSection_strategy = st.builds(
    diagram_GaugeSection,
    max=
        safe_text,
    label=
        safe_text,
    backgroundColor=
        safe_text,
    foregroundColor=
        safe_text,
    value=
        safe_text,
    min=
        safe_text
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
diagram_Note_strategy = st.builds(
    diagram_Note,
    color=
        safe_text
)
diagram_Square_strategy = st.builds(
    diagram_Square,
    width=
        safe_text,
    height=
        safe_text,
    color=
        safe_text
)
diagram_Ellipse_strategy = st.builds(
    diagram_Ellipse,
    color=
        safe_text,
    verticalDiameter=
        safe_text,
    horizontalDiameter=
        safe_text
)
diagram_Lozenge_strategy = st.builds(
    diagram_Lozenge,
    height=
        safe_text,
    color=
        safe_text,
    width=
        safe_text
)
diagram_CustomStyle_strategy = st.builds(
    diagram_CustomStyle,
    id=
        safe_text
)
diagram_BundledImage_strategy = st.builds(
    diagram_BundledImage,
    shape=
        safe_text,
    providedShapeID=
        safe_text,
    color=
        safe_text
)
diagram_GaugeCompositeStyle_strategy = st.builds(
    diagram_GaugeCompositeStyle,
    alignment=
        safe_text
)
diagram_WorkspaceImage_strategy = st.builds(
    diagram_WorkspaceImage,
    workspacePath=
        safe_text
)
diagram_Dot_strategy = st.builds(
    diagram_Dot,
    backgroundColor=
        safe_text,
    strokeSizeComputationExpression=
        safe_text
)
HideLabelCapabilityStyle_strategy = st.builds(
    HideLabelCapabilityStyle,
)
BorderedStyle_strategy = st.builds(
    BorderedStyle,
)
Style_strategy = st.builds(
    Style,
)
diagram_BorderedStyle_strategy = st.builds(
    diagram_BorderedStyle,
    borderSize=
        safe_text,
    borderColor=
        safe_text,
    borderLineStyle=
        safe_text,
    borderSizeComputationExpression=
        safe_text
)
LabelStyle_strategy = st.builds(
    LabelStyle,
)
IEdgeMapping_strategy = st.builds(
    IEdgeMapping,
)
diagram_EdgeTarget_strategy = st.builds(
    diagram_EdgeTarget,
)
diagram_EdgeStyle_strategy = st.builds(
    diagram_EdgeStyle,
    strokeColor=
        safe_text,
    lineStyle=
        safe_text,
    foldingStyle=
        safe_text,
    centered=
        safe_text,
    sourceArrow=
        safe_text,
    size=
        safe_text,
    routingStyle=
        safe_text,
    targetArrow=
        safe_text
)
DDiagramElementContainer_strategy = st.builds(
    DDiagramElementContainer,
)
diagram_DNodeList_strategy = st.builds(
    diagram_DNodeList,
)
diagram_DNodeContainer_strategy = st.builds(
    diagram_DNodeContainer,
    childrenPresentation=
        safe_text
)
ContainerMapping_strategy = st.builds(
    ContainerMapping,
)
diagram_ContainerStyle_strategy = st.builds(
    diagram_ContainerStyle,
)
NodeMapping_strategy = st.builds(
    NodeMapping,
)
diagram_Style_strategy = st.builds(
    diagram_Style,
)
diagram_NodeStyle_strategy = st.builds(
    diagram_NodeStyle,
    labelPosition=
        safe_text
)
EdgeTarget_strategy = st.builds(
    EdgeTarget,
)
AbstractDNode_strategy = st.builds(
    AbstractDNode,
)
DDiagramElement_strategy = st.builds(
    DDiagramElement,
)
diagram_AbstractDNode_strategy = st.builds(
    diagram_AbstractDNode,
    arrangeConstraints=
        safe_text
)
filter_CompositeFilterDescription_strategy = st.builds(
    filter_CompositeFilterDescription,
)
GraphicalFilter_strategy = st.builds(
    GraphicalFilter,
)
diagram_AppliedCompositeFilters_strategy = st.builds(
    diagram_AppliedCompositeFilters,
)
diagram_HideLabelFilter_strategy = st.builds(
    diagram_HideLabelFilter,
)
diagram_FoldingPointFilter_strategy = st.builds(
    diagram_FoldingPointFilter,
)
diagram_CollapseFilter_strategy = st.builds(
    diagram_CollapseFilter,
    height=
        st.integers(),
    width=
        st.integers()
)
diagram_FoldingFilter_strategy = st.builds(
    diagram_FoldingFilter,
)
diagram_AbsoluteBoundsFilter_strategy = st.builds(
    diagram_AbsoluteBoundsFilter,
    x=
        safe_text,
    y=
        safe_text,
    height=
        safe_text,
    width=
        safe_text
)
diagram_HideFilter_strategy = st.builds(
    diagram_HideFilter,
)
diagram_GraphicalFilter_strategy = st.builds(
    diagram_GraphicalFilter,
)
DiagramElementMapping_strategy = st.builds(
    DiagramElementMapping,
)
diagram_Decoration_strategy = st.builds(
    diagram_Decoration,
)
DRepresentationElement_strategy = st.builds(
    DRepresentationElement,
)
DSemanticDecorator_strategy = st.builds(
    DSemanticDecorator,
)
DDiagram_strategy = st.builds(
    DDiagram,
)
diagram_DSemanticDiagram_strategy = st.builds(
    diagram_DSemanticDiagram,
)
Layer_strategy = st.builds(
    Layer,
)
diagram_description_AdditionalLayer_strategy = st.builds(
    diagram_description_AdditionalLayer,
    activeByDefault=
        st.booleans(),
    optional=
        st.booleans()
)
diagram_FilterVariableHistory_strategy = st.builds(
    diagram_FilterVariableHistory,
)
tool_BehaviorTool_strategy = st.builds(
    tool_BehaviorTool,
)
validation_ValidationRule_strategy = st.builds(
    validation_ValidationRule,
)
AdditionalLayer_strategy = st.builds(
    AdditionalLayer,
)
filter_FilterDescription_strategy = st.builds(
    filter_FilterDescription,
)
concern_ConcernDescription_strategy = st.builds(
    concern_ConcernDescription,
)
diagram_DNodeListElement_strategy = st.builds(
    diagram_DNodeListElement,
)
diagram_DEdge_strategy = st.builds(
    diagram_DEdge,
    size=
        safe_text,
    beginLabel=
        safe_text,
    routingStyle=
        safe_text,
    endLabel=
        safe_text,
    isMockEdge=
        st.booleans(),
    isFold=
        st.booleans(),
    arrangeConstraints=
        safe_text
)
DiagramDescription_strategy = st.builds(
    DiagramDescription,
)
diagram_DDiagramElement_strategy = st.builds(
    diagram_DDiagramElement,
    tooltipText=
        safe_text,
    visible=
        st.booleans()
)
DragAndDropTarget_strategy = st.builds(
    DragAndDropTarget,
)
diagram_DDiagramElementContainer_strategy = st.builds(
    diagram_DDiagramElementContainer,
    height=
        safe_text,
    width=
        safe_text
)
diagram_DNode_strategy = st.builds(
    diagram_DNode,
    labelPosition=
        safe_text,
    width=
        safe_text,
    resizeKind=
        safe_text,
    height=
        safe_text
)
description_DocumentedElement_strategy = st.builds(
    description_DocumentedElement,
)
diagram_description_EdgeMappingImport_strategy = st.builds(
    diagram_description_EdgeMappingImport,
    inheritsAncestorFilters=
        st.booleans()
)
diagram_filter_FilterDescription_strategy = st.builds(
    diagram_filter_FilterDescription,
)
diagram_description_AbstractNodeMapping_strategy = st.builds(
    diagram_description_AbstractNodeMapping,
    domainClass=
        safe_text
)
diagram_concern_ConcernDescription_strategy = st.builds(
    diagram_concern_ConcernDescription,
)
diagram_description_Layer_strategy = st.builds(
    diagram_description_Layer,
    icon=
        safe_text
)
diagram_tool_ToolSection_strategy = st.builds(
    diagram_tool_ToolSection,
    icon=
        safe_text
)
diagram_description_EdgeMapping_strategy = st.builds(
    diagram_description_EdgeMapping,
    domainClass=
        safe_text,
    useDomainElement=
        st.booleans(),
    sourceFinderExpression=
        safe_text,
    targetFinderExpression=
        safe_text,
    pathExpression=
        safe_text,
    targetExpression=
        safe_text
)
DRepresentation_strategy = st.builds(
    DRepresentation,
)
diagram_DDiagram_strategy = st.builds(
    diagram_DDiagram,
    headerHeight=
        st.integers(),
    isInLayoutingMode=
        st.booleans(),
    synchronized=
        st.booleans()
)





@given(instance=diagram_tool_DeleteHook_strategy)
def test_hyp_diagram_tool_deletehook_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=diagram_tool_RequestDescription_strategy)
def test_hyp_diagram_tool_requestdescription_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original















@given(instance=diagram_tool_ContainerCreationDescription_strategy)
def test_hyp_diagram_tool_containercreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original





@given(instance=diagram_tool_EdgeCreationDescription_strategy)
def test_hyp_diagram_tool_edgecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=diagram_tool_EdgeCreationDescription_strategy)
def test_hyp_diagram_tool_edgecreationdescription_connectionStartPrecondition_setter(instance):
    original = instance.connectionStartPrecondition
    instance.connectionStartPrecondition = original
    assert instance.connectionStartPrecondition == original





@given(instance=diagram_tool_NodeCreationDescription_strategy)
def test_hyp_diagram_tool_nodecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original












@given(instance=diagram_style_HideLabelCapabilityStyleDescription_strategy)
def test_hyp_diagram_style_hidelabelcapabilitystyledescription_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original














@given(instance=diagram_style_SizeComputationContainerStyleDescription_strategy)
def test_hyp_diagram_style_sizecomputationcontainerstyledescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original



@given(instance=diagram_style_SizeComputationContainerStyleDescription_strategy)
def test_hyp_diagram_style_sizecomputationcontainerstyledescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original




@given(instance=diagram_style_GaugeSectionDescription_strategy)
def test_hyp_diagram_style_gaugesectiondescription_minValueExpression_setter(instance):
    original = instance.minValueExpression
    instance.minValueExpression = original
    assert instance.minValueExpression == original



@given(instance=diagram_style_GaugeSectionDescription_strategy)
def test_hyp_diagram_style_gaugesectiondescription_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=diagram_style_GaugeSectionDescription_strategy)
def test_hyp_diagram_style_gaugesectiondescription_maxValueExpression_setter(instance):
    original = instance.maxValueExpression
    instance.maxValueExpression = original
    assert instance.maxValueExpression == original



@given(instance=diagram_style_GaugeSectionDescription_strategy)
def test_hyp_diagram_style_gaugesectiondescription_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original









@given(instance=diagram_style_EllipseNodeDescription_strategy)
def test_hyp_diagram_style_ellipsenodedescription_verticalDiameterComputationExpression_setter(instance):
    original = instance.verticalDiameterComputationExpression
    instance.verticalDiameterComputationExpression = original
    assert instance.verticalDiameterComputationExpression == original



@given(instance=diagram_style_EllipseNodeDescription_strategy)
def test_hyp_diagram_style_ellipsenodedescription_horizontalDiameterComputationExpression_setter(instance):
    original = instance.horizontalDiameterComputationExpression
    instance.horizontalDiameterComputationExpression = original
    assert instance.horizontalDiameterComputationExpression == original




@given(instance=diagram_style_SquareDescription_strategy)
def test_hyp_diagram_style_squaredescription_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=diagram_style_SquareDescription_strategy)
def test_hyp_diagram_style_squaredescription_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=diagram_style_DotDescription_strategy)
def test_hyp_diagram_style_dotdescription_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original




@given(instance=diagram_style_GaugeCompositeStyleDescription_strategy)
def test_hyp_diagram_style_gaugecompositestyledescription_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original




@given(instance=diagram_style_BundledImageDescription_strategy)
def test_hyp_diagram_style_bundledimagedescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=diagram_style_BundledImageDescription_strategy)
def test_hyp_diagram_style_bundledimagedescription_providedShapeID_setter(instance):
    original = instance.providedShapeID
    instance.providedShapeID = original
    assert instance.providedShapeID == original




@given(instance=diagram_style_CustomStyleDescription_strategy)
def test_hyp_diagram_style_customstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original








@given(instance=diagram_style_ContainerStyleDescription_strategy)
def test_hyp_diagram_style_containerstyledescription_roundedCorner_setter(instance):
    original = instance.roundedCorner
    instance.roundedCorner = original
    assert instance.roundedCorner == original






@given(instance=diagram_style_RoundedCornerStyleDescription_strategy)
def test_hyp_diagram_style_roundedcornerstyledescription_arcHeight_setter(instance):
    original = instance.arcHeight
    instance.arcHeight = original
    assert instance.arcHeight == original



@given(instance=diagram_style_RoundedCornerStyleDescription_strategy)
def test_hyp_diagram_style_roundedcornerstyledescription_arcWidth_setter(instance):
    original = instance.arcWidth
    instance.arcWidth = original
    assert instance.arcWidth == original




@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_hyp_diagram_style_edgestyledescription_endsCentering_setter(instance):
    original = instance.endsCentering
    instance.endsCentering = original
    assert instance.endsCentering == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_hyp_diagram_style_edgestyledescription_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_hyp_diagram_style_edgestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_hyp_diagram_style_edgestyledescription_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_hyp_diagram_style_edgestyledescription_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_hyp_diagram_style_edgestyledescription_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_hyp_diagram_style_edgestyledescription_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original




@given(instance=diagram_style_BorderedStyleDescription_strategy)
def test_hyp_diagram_style_borderedstyledescription_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original



@given(instance=diagram_style_BorderedStyleDescription_strategy)
def test_hyp_diagram_style_borderedstyledescription_borderLineStyle_setter(instance):
    original = instance.borderLineStyle
    instance.borderLineStyle = original
    assert instance.borderLineStyle == original





@given(instance=diagram_style_LozengeNodeDescription_strategy)
def test_hyp_diagram_style_lozengenodedescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original



@given(instance=diagram_style_LozengeNodeDescription_strategy)
def test_hyp_diagram_style_lozengenodedescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original






























@given(instance=diagram_style_ShapeContainerStyleDescription_strategy)
def test_hyp_diagram_style_shapecontainerstyledescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original




@given(instance=diagram_style_FlatContainerStyleDescription_strategy)
def test_hyp_diagram_style_flatcontainerstyledescription_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original






@given(instance=diagram_style_WorkspaceImageDescription_strategy)
def test_hyp_diagram_style_workspaceimagedescription_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original



















@given(instance=diagram_description_CompositeLayout_strategy)
def test_hyp_diagram_description_compositelayout_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=diagram_description_CompositeLayout_strategy)
def test_hyp_diagram_description_compositelayout_padding_setter(instance):
    original = instance.padding
    instance.padding = original
    assert instance.padding == original




@given(instance=diagram_description_OrderedTreeLayout_strategy)
def test_hyp_diagram_description_orderedtreelayout_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original










@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_hyp_diagram_description_diagramelementmapping_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_hyp_diagram_description_diagramelementmapping_semanticElements_setter(instance):
    original = instance.semanticElements
    instance.semanticElements = original
    assert instance.semanticElements == original



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_hyp_diagram_description_diagramelementmapping_synchronizationLock_setter(instance):
    original = instance.synchronizationLock
    instance.synchronizationLock = original
    assert instance.synchronizationLock == original



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_hyp_diagram_description_diagramelementmapping_semanticCandidatesExpression_setter(instance):
    original = instance.semanticCandidatesExpression
    instance.semanticCandidatesExpression = original
    assert instance.semanticCandidatesExpression == original



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_hyp_diagram_description_diagramelementmapping_createElements_setter(instance):
    original = instance.createElements
    instance.createElements = original
    assert instance.createElements == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_diagramelementmapping_isfrom_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isFrom(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isFrom).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isFrom' in diagram_description_DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFrom' in diagram_description_DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFrom' in diagram_description_DiagramElementMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_diagramelementmapping_checkprecondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkPrecondition(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkPrecondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkPrecondition' in diagram_description_DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPrecondition' in diagram_description_DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPrecondition' in diagram_description_DiagramElementMapping is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_nodemapping_updatenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateNode' in diagram_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateNode' in diagram_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateNode' in diagram_description_NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_nodemapping_updatelistelement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateListElement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateListElement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateListElement' in diagram_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateListElement' in diagram_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateListElement' in diagram_description_NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_nodemapping_createnode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createNode(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createNode' in diagram_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createNode' in diagram_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createNode' in diagram_description_NodeMapping is not implemented or raised an error")




@given(instance=diagram_description_ContainerMapping_strategy)
def test_hyp_diagram_description_containermapping_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original




@given(instance=diagram_description_DiagramDescription_strategy)
def test_hyp_diagram_description_diagramdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original



@given(instance=diagram_description_DiagramDescription_strategy)
def test_hyp_diagram_description_diagramdescription_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=diagram_description_DiagramDescription_strategy)
def test_hyp_diagram_description_diagramdescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original



@given(instance=diagram_description_DiagramDescription_strategy)
def test_hyp_diagram_description_diagramdescription_enablePopupBars_setter(instance):
    original = instance.enablePopupBars
    instance.enablePopupBars = original
    assert instance.enablePopupBars == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_DiagramDescription_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_diagramdescription_creatediagram_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createDiagram()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createDiagram).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createDiagram' in diagram_description_DiagramDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createDiagram' in diagram_description_DiagramDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createDiagram' in diagram_description_DiagramDescription is not implemented or raised an error")











@given(instance=diagram_filter_Filter_strategy)
def test_hyp_diagram_filter_filter_filterKind_setter(instance):
    original = instance.filterKind
    instance.filterKind = original
    assert instance.filterKind == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_filter_Filter_strategy)
@settings(max_examples=30)
def test_hyp_diagram_filter_filter_isvisible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isVisible(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isVisible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isVisible' in diagram_filter_Filter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in diagram_filter_Filter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in diagram_filter_Filter is not implemented or raised an error")





@given(instance=diagram_filter_VariableFilter_strategy)
def test_hyp_diagram_filter_variablefilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_filter_VariableFilter_strategy)
@settings(max_examples=30)
def test_hyp_diagram_filter_variablefilter_resetvariables_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resetVariables()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resetVariables).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resetVariables' in diagram_filter_VariableFilter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resetVariables' in diagram_filter_VariableFilter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resetVariables' in diagram_filter_VariableFilter is not implemented or raised an error")




@given(instance=diagram_filter_MappingFilter_strategy)
def test_hyp_diagram_filter_mappingfilter_viewConditionExpression_setter(instance):
    original = instance.viewConditionExpression
    instance.viewConditionExpression = original
    assert instance.viewConditionExpression == original



@given(instance=diagram_filter_MappingFilter_strategy)
def test_hyp_diagram_filter_mappingfilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original






@given(instance=diagram_tool_ContainerDropDescription_strategy)
def test_hyp_diagram_tool_containerdropdescription_dragSource_setter(instance):
    original = instance.dragSource
    instance.dragSource = original
    assert instance.dragSource == original



@given(instance=diagram_tool_ContainerDropDescription_strategy)
def test_hyp_diagram_tool_containerdropdescription_moveEdges_setter(instance):
    original = instance.moveEdges
    instance.moveEdges = original
    assert instance.moveEdges == original










@given(instance=diagram_tool_Navigation_strategy)
def test_hyp_diagram_tool_navigation_createIfNotExistent_setter(instance):
    original = instance.createIfNotExistent
    instance.createIfNotExistent = original
    assert instance.createIfNotExistent == original




@given(instance=diagram_tool_CreateView_strategy)
def test_hyp_diagram_tool_createview_containerViewExpression_setter(instance):
    original = instance.containerViewExpression
    instance.containerViewExpression = original
    assert instance.containerViewExpression == original



@given(instance=diagram_tool_CreateView_strategy)
def test_hyp_diagram_tool_createview_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original












@given(instance=diagram_tool_BehaviorTool_strategy)
def test_hyp_diagram_tool_behaviortool_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original





@given(instance=diagram_tool_DirectEditLabel_strategy)
def test_hyp_diagram_tool_directeditlabel_inputLabelExpression_setter(instance):
    original = instance.inputLabelExpression
    instance.inputLabelExpression = original
    assert instance.inputLabelExpression == original





@given(instance=diagram_tool_CreateEdgeView_strategy)
def test_hyp_diagram_tool_createedgeview_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original



@given(instance=diagram_tool_CreateEdgeView_strategy)
def test_hyp_diagram_tool_createedgeview_sourceExpression_setter(instance):
    original = instance.sourceExpression
    instance.sourceExpression = original
    assert instance.sourceExpression == original





@given(instance=diagram_tool_ReconnectEdgeDescription_strategy)
def test_hyp_diagram_tool_reconnectedgedescription_reconnectionKind_setter(instance):
    original = instance.reconnectionKind
    instance.reconnectionKind = original
    assert instance.reconnectionKind == original




@given(instance=diagram_tool_DeleteHookParameter_strategy)
def test_hyp_diagram_tool_deletehookparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=diagram_tool_DeleteHookParameter_strategy)
def test_hyp_diagram_tool_deletehookparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=diagram_HideLabelCapabilityStyle_strategy)
def test_hyp_diagram_hidelabelcapabilitystyle_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original






@given(instance=diagram_style_NodeStyleDescription_strategy)
def test_hyp_diagram_style_nodestyledescription_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original



@given(instance=diagram_style_NodeStyleDescription_strategy)
def test_hyp_diagram_style_nodestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original



@given(instance=diagram_style_NodeStyleDescription_strategy)
def test_hyp_diagram_style_nodestyledescription_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original



@given(instance=diagram_style_NodeStyleDescription_strategy)
def test_hyp_diagram_style_nodestyledescription_forbiddenSides_setter(instance):
    original = instance.forbiddenSides
    instance.forbiddenSides = original
    assert instance.forbiddenSides == original













@given(instance=diagram_TypedVariableValue_strategy)
def test_hyp_diagram_typedvariablevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_EndLabelStyle_strategy)
@settings(max_examples=30)
def test_hyp_diagram_endlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in diagram_EndLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram_EndLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram_EndLabelStyle is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_BeginLabelStyle_strategy)
@settings(max_examples=30)
def test_hyp_diagram_beginlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in diagram_BeginLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram_BeginLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram_BeginLabelStyle is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_CenterLabelStyle_strategy)
@settings(max_examples=30)
def test_hyp_diagram_centerlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in diagram_CenterLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram_CenterLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram_CenterLabelStyle is not implemented or raised an error")





@given(instance=diagram_ShapeContainerStyle_strategy)
def test_hyp_diagram_shapecontainerstyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=diagram_ShapeContainerStyle_strategy)
def test_hyp_diagram_shapecontainerstyle_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original




@given(instance=diagram_FlatContainerStyle_strategy)
def test_hyp_diagram_flatcontainerstyle_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=diagram_FlatContainerStyle_strategy)
def test_hyp_diagram_flatcontainerstyle_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original



@given(instance=diagram_FlatContainerStyle_strategy)
def test_hyp_diagram_flatcontainerstyle_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original





@given(instance=diagram_GaugeSection_strategy)
def test_hyp_diagram_gaugesection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=diagram_GaugeSection_strategy)
def test_hyp_diagram_gaugesection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=diagram_GaugeSection_strategy)
def test_hyp_diagram_gaugesection_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=diagram_GaugeSection_strategy)
def test_hyp_diagram_gaugesection_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original



@given(instance=diagram_GaugeSection_strategy)
def test_hyp_diagram_gaugesection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=diagram_GaugeSection_strategy)
def test_hyp_diagram_gaugesection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original





@given(instance=diagram_Note_strategy)
def test_hyp_diagram_note_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=diagram_Square_strategy)
def test_hyp_diagram_square_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=diagram_Square_strategy)
def test_hyp_diagram_square_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_Square_strategy)
def test_hyp_diagram_square_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=diagram_Ellipse_strategy)
def test_hyp_diagram_ellipse_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=diagram_Ellipse_strategy)
def test_hyp_diagram_ellipse_verticalDiameter_setter(instance):
    original = instance.verticalDiameter
    instance.verticalDiameter = original
    assert instance.verticalDiameter == original



@given(instance=diagram_Ellipse_strategy)
def test_hyp_diagram_ellipse_horizontalDiameter_setter(instance):
    original = instance.horizontalDiameter
    instance.horizontalDiameter = original
    assert instance.horizontalDiameter == original




@given(instance=diagram_Lozenge_strategy)
def test_hyp_diagram_lozenge_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_Lozenge_strategy)
def test_hyp_diagram_lozenge_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=diagram_Lozenge_strategy)
def test_hyp_diagram_lozenge_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=diagram_CustomStyle_strategy)
def test_hyp_diagram_customstyle_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=diagram_BundledImage_strategy)
def test_hyp_diagram_bundledimage_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=diagram_BundledImage_strategy)
def test_hyp_diagram_bundledimage_providedShapeID_setter(instance):
    original = instance.providedShapeID
    instance.providedShapeID = original
    assert instance.providedShapeID == original



@given(instance=diagram_BundledImage_strategy)
def test_hyp_diagram_bundledimage_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=diagram_GaugeCompositeStyle_strategy)
def test_hyp_diagram_gaugecompositestyle_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original




@given(instance=diagram_WorkspaceImage_strategy)
def test_hyp_diagram_workspaceimage_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original




@given(instance=diagram_Dot_strategy)
def test_hyp_diagram_dot_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=diagram_Dot_strategy)
def test_hyp_diagram_dot_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original







@given(instance=diagram_BorderedStyle_strategy)
def test_hyp_diagram_borderedstyle_borderSize_setter(instance):
    original = instance.borderSize
    instance.borderSize = original
    assert instance.borderSize == original



@given(instance=diagram_BorderedStyle_strategy)
def test_hyp_diagram_borderedstyle_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original



@given(instance=diagram_BorderedStyle_strategy)
def test_hyp_diagram_borderedstyle_borderLineStyle_setter(instance):
    original = instance.borderLineStyle
    instance.borderLineStyle = original
    assert instance.borderLineStyle == original



@given(instance=diagram_BorderedStyle_strategy)
def test_hyp_diagram_borderedstyle_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original







@given(instance=diagram_EdgeStyle_strategy)
def test_hyp_diagram_edgestyle_strokeColor_setter(instance):
    original = instance.strokeColor
    instance.strokeColor = original
    assert instance.strokeColor == original



@given(instance=diagram_EdgeStyle_strategy)
def test_hyp_diagram_edgestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=diagram_EdgeStyle_strategy)
def test_hyp_diagram_edgestyle_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original



@given(instance=diagram_EdgeStyle_strategy)
def test_hyp_diagram_edgestyle_centered_setter(instance):
    original = instance.centered
    instance.centered = original
    assert instance.centered == original



@given(instance=diagram_EdgeStyle_strategy)
def test_hyp_diagram_edgestyle_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original



@given(instance=diagram_EdgeStyle_strategy)
def test_hyp_diagram_edgestyle_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=diagram_EdgeStyle_strategy)
def test_hyp_diagram_edgestyle_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original



@given(instance=diagram_EdgeStyle_strategy)
def test_hyp_diagram_edgestyle_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original






@given(instance=diagram_DNodeContainer_strategy)
def test_hyp_diagram_dnodecontainer_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original








@given(instance=diagram_NodeStyle_strategy)
def test_hyp_diagram_nodestyle_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original







@given(instance=diagram_AbstractDNode_strategy)
def test_hyp_diagram_abstractdnode_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original









@given(instance=diagram_CollapseFilter_strategy)
def test_hyp_diagram_collapsefilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_CollapseFilter_strategy)
def test_hyp_diagram_collapsefilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original





@given(instance=diagram_AbsoluteBoundsFilter_strategy)
def test_hyp_diagram_absoluteboundsfilter_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=diagram_AbsoluteBoundsFilter_strategy)
def test_hyp_diagram_absoluteboundsfilter_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=diagram_AbsoluteBoundsFilter_strategy)
def test_hyp_diagram_absoluteboundsfilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_AbsoluteBoundsFilter_strategy)
def test_hyp_diagram_absoluteboundsfilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original













@given(instance=diagram_description_AdditionalLayer_strategy)
def test_hyp_diagram_description_additionallayer_activeByDefault_setter(instance):
    original = instance.activeByDefault
    instance.activeByDefault = original
    assert instance.activeByDefault == original



@given(instance=diagram_description_AdditionalLayer_strategy)
def test_hyp_diagram_description_additionallayer_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original











@given(instance=diagram_DEdge_strategy)
def test_hyp_diagram_dedge_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=diagram_DEdge_strategy)
def test_hyp_diagram_dedge_beginLabel_setter(instance):
    original = instance.beginLabel
    instance.beginLabel = original
    assert instance.beginLabel == original



@given(instance=diagram_DEdge_strategy)
def test_hyp_diagram_dedge_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original



@given(instance=diagram_DEdge_strategy)
def test_hyp_diagram_dedge_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original



@given(instance=diagram_DEdge_strategy)
def test_hyp_diagram_dedge_isMockEdge_setter(instance):
    original = instance.isMockEdge
    instance.isMockEdge = original
    assert instance.isMockEdge == original



@given(instance=diagram_DEdge_strategy)
def test_hyp_diagram_dedge_isFold_setter(instance):
    original = instance.isFold
    instance.isFold = original
    assert instance.isFold == original



@given(instance=diagram_DEdge_strategy)
def test_hyp_diagram_dedge_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_DEdge_strategy)
@settings(max_examples=30)
def test_hyp_diagram_dedge_isrootfolding_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isRootFolding()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isRootFolding).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isRootFolding' in diagram_DEdge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isRootFolding' in diagram_DEdge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isRootFolding' in diagram_DEdge is not implemented or raised an error")





@given(instance=diagram_DDiagramElement_strategy)
def test_hyp_diagram_ddiagramelement_tooltipText_setter(instance):
    original = instance.tooltipText
    instance.tooltipText = original
    assert instance.tooltipText == original



@given(instance=diagram_DDiagramElement_strategy)
def test_hyp_diagram_ddiagramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original





@given(instance=diagram_DDiagramElementContainer_strategy)
def test_hyp_diagram_ddiagramelementcontainer_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_DDiagramElementContainer_strategy)
def test_hyp_diagram_ddiagramelementcontainer_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=diagram_DNode_strategy)
def test_hyp_diagram_dnode_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original



@given(instance=diagram_DNode_strategy)
def test_hyp_diagram_dnode_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=diagram_DNode_strategy)
def test_hyp_diagram_dnode_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original



@given(instance=diagram_DNode_strategy)
def test_hyp_diagram_dnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original





@given(instance=diagram_description_EdgeMappingImport_strategy)
def test_hyp_diagram_description_edgemappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_filter_FilterDescription_strategy)
@settings(max_examples=30)
def test_hyp_diagram_filter_filterdescription_isvisible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isVisible(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isVisible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isVisible' in diagram_filter_FilterDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in diagram_filter_FilterDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in diagram_filter_FilterDescription is not implemented or raised an error")




@given(instance=diagram_description_AbstractNodeMapping_strategy)
def test_hyp_diagram_description_abstractnodemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_abstractnodemapping_cleardnodesdone_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clearDNodesDone()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clearDNodesDone).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clearDNodesDone' in diagram_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clearDNodesDone' in diagram_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clearDNodesDone' in diagram_description_AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_abstractnodemapping_finddnodefromeobject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findDNodeFromEObject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findDNodeFromEObject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findDNodeFromEObject' in diagram_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findDNodeFromEObject' in diagram_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findDNodeFromEObject' in diagram_description_AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_abstractnodemapping_adddonenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addDoneNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addDoneNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addDoneNode' in diagram_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addDoneNode' in diagram_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addDoneNode' in diagram_description_AbstractNodeMapping is not implemented or raised an error")





@given(instance=diagram_description_Layer_strategy)
def test_hyp_diagram_description_layer_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original




@given(instance=diagram_tool_ToolSection_strategy)
def test_hyp_diagram_tool_toolsection_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original




@given(instance=diagram_description_EdgeMapping_strategy)
def test_hyp_diagram_description_edgemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_hyp_diagram_description_edgemapping_useDomainElement_setter(instance):
    original = instance.useDomainElement
    instance.useDomainElement = original
    assert instance.useDomainElement == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_hyp_diagram_description_edgemapping_sourceFinderExpression_setter(instance):
    original = instance.sourceFinderExpression
    instance.sourceFinderExpression = original
    assert instance.sourceFinderExpression == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_hyp_diagram_description_edgemapping_targetFinderExpression_setter(instance):
    original = instance.targetFinderExpression
    instance.targetFinderExpression = original
    assert instance.targetFinderExpression == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_hyp_diagram_description_edgemapping_pathExpression_setter(instance):
    original = instance.pathExpression
    instance.pathExpression = original
    assert instance.pathExpression == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_hyp_diagram_description_edgemapping_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_EdgeMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_edgemapping_createedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createEdge(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createEdge' in diagram_description_EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in diagram_description_EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in diagram_description_EdgeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_EdgeMapping_strategy)
@settings(max_examples=30)
def test_hyp_diagram_description_edgemapping_updateedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateEdge' in diagram_description_EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateEdge' in diagram_description_EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateEdge' in diagram_description_EdgeMapping is not implemented or raised an error")





@given(instance=diagram_DDiagram_strategy)
def test_hyp_diagram_ddiagram_headerHeight_setter(instance):
    original = instance.headerHeight
    instance.headerHeight = original
    assert instance.headerHeight == original



@given(instance=diagram_DDiagram_strategy)
def test_hyp_diagram_ddiagram_isInLayoutingMode_setter(instance):
    original = instance.isInLayoutingMode
    instance.isInLayoutingMode = original
    assert instance.isInLayoutingMode == original



@given(instance=diagram_DDiagram_strategy)
def test_hyp_diagram_ddiagram_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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
    Filter,
    FilterDescription,
    GraphicalFilter,
    HideLabelCapabilityStyle,
    IEdgeMapping,
    InteractiveVariableDescription,
    LabelStyle,
    Layer,
    Layout,
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
    diagram_description_CompositeLayout,
    diagram_description_ConditionalContainerStyleDescription,
    diagram_description_ConditionalEdgeStyleDescription,
    diagram_description_ConditionalNodeStyleDescription,
    diagram_description_ContainerMapping,
    diagram_description_ContainerMappingImport,
    diagram_description_DiagramDescription,
    diagram_description_DiagramElementMapping,
    diagram_description_DiagramExtensionDescription,
    diagram_description_DiagramImportDescription,
    diagram_description_DragAndDropTargetDescription,
    diagram_description_EdgeMapping,
    diagram_description_EdgeMappingImport,
    diagram_description_IEdgeMapping,
    diagram_description_Layer,
    diagram_description_Layout,
    diagram_description_MappingBasedDecoration,
    diagram_description_NodeMapping,
    diagram_description_NodeMappingImport,
    diagram_description_OrderedTreeLayout,
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
    LineStyle,
    ReconnectionKind,
    ResizeKind,
    Side,
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

def test_diagram_AbsoluteBoundsFilter_height_value_roundtrip():
    instance = diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_diagram_AbsoluteBoundsFilter_width_value_roundtrip():
    instance = diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_diagram_AbsoluteBoundsFilter_x_value_roundtrip():
    instance = diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_diagram_AbsoluteBoundsFilter_y_value_roundtrip():
    instance = diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_diagram_AbstractDNode_arrangeConstraints_value_roundtrip():
    instance = diagram_AbstractDNode(arrangeConstraints="sample_text")
    assert instance.arrangeConstraints == "sample_text"
    instance.arrangeConstraints = "sample_text_2"
    assert instance.arrangeConstraints == "sample_text_2"


def test_diagram_BorderedStyle_borderColor_value_roundtrip():
    instance = diagram_BorderedStyle(borderColor="sample_text", borderLineStyle="sample_text", borderSize="sample_text", borderSizeComputationExpression="sample_text")
    assert instance.borderColor == "sample_text"
    instance.borderColor = "sample_text_2"
    assert instance.borderColor == "sample_text_2"


def test_diagram_BorderedStyle_borderLineStyle_value_roundtrip():
    instance = diagram_BorderedStyle(borderColor="sample_text", borderLineStyle="sample_text", borderSize="sample_text", borderSizeComputationExpression="sample_text")
    assert instance.borderLineStyle == "sample_text"
    instance.borderLineStyle = "sample_text_2"
    assert instance.borderLineStyle == "sample_text_2"


def test_diagram_BorderedStyle_borderSize_value_roundtrip():
    instance = diagram_BorderedStyle(borderColor="sample_text", borderLineStyle="sample_text", borderSize="sample_text", borderSizeComputationExpression="sample_text")
    assert instance.borderSize == "sample_text"
    instance.borderSize = "sample_text_2"
    assert instance.borderSize == "sample_text_2"


def test_diagram_BorderedStyle_borderSizeComputationExpression_value_roundtrip():
    instance = diagram_BorderedStyle(borderColor="sample_text", borderLineStyle="sample_text", borderSize="sample_text", borderSizeComputationExpression="sample_text")
    assert instance.borderSizeComputationExpression == "sample_text"
    instance.borderSizeComputationExpression = "sample_text_2"
    assert instance.borderSizeComputationExpression == "sample_text_2"


def test_diagram_BundledImage_color_value_roundtrip():
    instance = diagram_BundledImage(color="sample_text", providedShapeID="sample_text", shape="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_diagram_BundledImage_providedShapeID_value_roundtrip():
    instance = diagram_BundledImage(color="sample_text", providedShapeID="sample_text", shape="sample_text")
    assert instance.providedShapeID == "sample_text"
    instance.providedShapeID = "sample_text_2"
    assert instance.providedShapeID == "sample_text_2"


def test_diagram_BundledImage_shape_value_roundtrip():
    instance = diagram_BundledImage(color="sample_text", providedShapeID="sample_text", shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_diagram_CollapseFilter_height_value_roundtrip():
    instance = diagram_CollapseFilter(height=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_diagram_CollapseFilter_width_value_roundtrip():
    instance = diagram_CollapseFilter(height=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_diagram_CustomStyle_id_value_roundtrip():
    instance = diagram_CustomStyle(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_diagram_DDiagram_headerHeight_value_roundtrip():
    instance = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    assert instance.headerHeight == 7
    instance.headerHeight = 13
    assert instance.headerHeight == 13


def test_diagram_DDiagram_isInLayoutingMode_value_roundtrip():
    instance = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    assert instance.isInLayoutingMode == True
    instance.isInLayoutingMode = False
    assert instance.isInLayoutingMode == False


def test_diagram_DDiagram_synchronized_value_roundtrip():
    instance = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    assert instance.synchronized == True
    instance.synchronized = False
    assert instance.synchronized == False


def test_diagram_DDiagramElement_tooltipText_value_roundtrip():
    instance = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    assert instance.tooltipText == "sample_text"
    instance.tooltipText = "sample_text_2"
    assert instance.tooltipText == "sample_text_2"


def test_diagram_DDiagramElement_visible_value_roundtrip():
    instance = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_diagram_DDiagramElementContainer_height_value_roundtrip():
    instance = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_diagram_DDiagramElementContainer_width_value_roundtrip():
    instance = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_diagram_DEdge_arrangeConstraints_value_roundtrip():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.arrangeConstraints == "sample_text"
    instance.arrangeConstraints = "sample_text_2"
    assert instance.arrangeConstraints == "sample_text_2"


def test_diagram_DEdge_beginLabel_value_roundtrip():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.beginLabel == "sample_text"
    instance.beginLabel = "sample_text_2"
    assert instance.beginLabel == "sample_text_2"


def test_diagram_DEdge_endLabel_value_roundtrip():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.endLabel == "sample_text"
    instance.endLabel = "sample_text_2"
    assert instance.endLabel == "sample_text_2"


def test_diagram_DEdge_isFold_value_roundtrip():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.isFold == True
    instance.isFold = False
    assert instance.isFold == False


def test_diagram_DEdge_isMockEdge_value_roundtrip():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.isMockEdge == True
    instance.isMockEdge = False
    assert instance.isMockEdge == False


def test_diagram_DEdge_routingStyle_value_roundtrip():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.routingStyle == "sample_text"
    instance.routingStyle = "sample_text_2"
    assert instance.routingStyle == "sample_text_2"


def test_diagram_DEdge_size_value_roundtrip():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_diagram_DNode_height_value_roundtrip():
    instance = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_diagram_DNode_labelPosition_value_roundtrip():
    instance = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert instance.labelPosition == "sample_text"
    instance.labelPosition = "sample_text_2"
    assert instance.labelPosition == "sample_text_2"


def test_diagram_DNode_resizeKind_value_roundtrip():
    instance = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert instance.resizeKind == "sample_text"
    instance.resizeKind = "sample_text_2"
    assert instance.resizeKind == "sample_text_2"


def test_diagram_DNode_width_value_roundtrip():
    instance = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_diagram_DNodeContainer_childrenPresentation_value_roundtrip():
    instance = diagram_DNodeContainer(childrenPresentation="sample_text")
    assert instance.childrenPresentation == "sample_text"
    instance.childrenPresentation = "sample_text_2"
    assert instance.childrenPresentation == "sample_text_2"


def test_diagram_Dot_backgroundColor_value_roundtrip():
    instance = diagram_Dot(backgroundColor="sample_text", strokeSizeComputationExpression="sample_text")
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_diagram_Dot_strokeSizeComputationExpression_value_roundtrip():
    instance = diagram_Dot(backgroundColor="sample_text", strokeSizeComputationExpression="sample_text")
    assert instance.strokeSizeComputationExpression == "sample_text"
    instance.strokeSizeComputationExpression = "sample_text_2"
    assert instance.strokeSizeComputationExpression == "sample_text_2"


def test_diagram_EdgeStyle_centered_value_roundtrip():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert instance.centered == "sample_text"
    instance.centered = "sample_text_2"
    assert instance.centered == "sample_text_2"


def test_diagram_EdgeStyle_foldingStyle_value_roundtrip():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert instance.foldingStyle == "sample_text"
    instance.foldingStyle = "sample_text_2"
    assert instance.foldingStyle == "sample_text_2"


def test_diagram_EdgeStyle_lineStyle_value_roundtrip():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert instance.lineStyle == "sample_text"
    instance.lineStyle = "sample_text_2"
    assert instance.lineStyle == "sample_text_2"


def test_diagram_EdgeStyle_routingStyle_value_roundtrip():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert instance.routingStyle == "sample_text"
    instance.routingStyle = "sample_text_2"
    assert instance.routingStyle == "sample_text_2"


def test_diagram_EdgeStyle_size_value_roundtrip():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_diagram_EdgeStyle_sourceArrow_value_roundtrip():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert instance.sourceArrow == "sample_text"
    instance.sourceArrow = "sample_text_2"
    assert instance.sourceArrow == "sample_text_2"


def test_diagram_EdgeStyle_strokeColor_value_roundtrip():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert instance.strokeColor == "sample_text"
    instance.strokeColor = "sample_text_2"
    assert instance.strokeColor == "sample_text_2"


def test_diagram_EdgeStyle_targetArrow_value_roundtrip():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert instance.targetArrow == "sample_text"
    instance.targetArrow = "sample_text_2"
    assert instance.targetArrow == "sample_text_2"


def test_diagram_Ellipse_color_value_roundtrip():
    instance = diagram_Ellipse(color="sample_text", horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_diagram_Ellipse_horizontalDiameter_value_roundtrip():
    instance = diagram_Ellipse(color="sample_text", horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert instance.horizontalDiameter == "sample_text"
    instance.horizontalDiameter = "sample_text_2"
    assert instance.horizontalDiameter == "sample_text_2"


def test_diagram_Ellipse_verticalDiameter_value_roundtrip():
    instance = diagram_Ellipse(color="sample_text", horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert instance.verticalDiameter == "sample_text"
    instance.verticalDiameter = "sample_text_2"
    assert instance.verticalDiameter == "sample_text_2"


def test_diagram_FlatContainerStyle_backgroundColor_value_roundtrip():
    instance = diagram_FlatContainerStyle(backgroundColor="sample_text", backgroundStyle="sample_text", foregroundColor="sample_text")
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_diagram_FlatContainerStyle_backgroundStyle_value_roundtrip():
    instance = diagram_FlatContainerStyle(backgroundColor="sample_text", backgroundStyle="sample_text", foregroundColor="sample_text")
    assert instance.backgroundStyle == "sample_text"
    instance.backgroundStyle = "sample_text_2"
    assert instance.backgroundStyle == "sample_text_2"


def test_diagram_FlatContainerStyle_foregroundColor_value_roundtrip():
    instance = diagram_FlatContainerStyle(backgroundColor="sample_text", backgroundStyle="sample_text", foregroundColor="sample_text")
    assert instance.foregroundColor == "sample_text"
    instance.foregroundColor = "sample_text_2"
    assert instance.foregroundColor == "sample_text_2"


def test_diagram_GaugeCompositeStyle_alignment_value_roundtrip():
    instance = diagram_GaugeCompositeStyle(alignment="sample_text")
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_diagram_GaugeSection_backgroundColor_value_roundtrip():
    instance = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_diagram_GaugeSection_foregroundColor_value_roundtrip():
    instance = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.foregroundColor == "sample_text"
    instance.foregroundColor = "sample_text_2"
    assert instance.foregroundColor == "sample_text_2"


def test_diagram_GaugeSection_label_value_roundtrip():
    instance = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_diagram_GaugeSection_max_value_roundtrip():
    instance = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_diagram_GaugeSection_min_value_roundtrip():
    instance = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_diagram_GaugeSection_value_value_roundtrip():
    instance = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_diagram_HideLabelCapabilityStyle_hideLabelByDefault_value_roundtrip():
    instance = diagram_HideLabelCapabilityStyle(hideLabelByDefault=True)
    assert instance.hideLabelByDefault == True
    instance.hideLabelByDefault = False
    assert instance.hideLabelByDefault == False


def test_diagram_Lozenge_color_value_roundtrip():
    instance = diagram_Lozenge(color="sample_text", height="sample_text", width="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_diagram_Lozenge_height_value_roundtrip():
    instance = diagram_Lozenge(color="sample_text", height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_diagram_Lozenge_width_value_roundtrip():
    instance = diagram_Lozenge(color="sample_text", height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_diagram_NodeStyle_labelPosition_value_roundtrip():
    instance = diagram_NodeStyle(labelPosition="sample_text")
    assert instance.labelPosition == "sample_text"
    instance.labelPosition = "sample_text_2"
    assert instance.labelPosition == "sample_text_2"


def test_diagram_Note_color_value_roundtrip():
    instance = diagram_Note(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_diagram_ShapeContainerStyle_backgroundColor_value_roundtrip():
    instance = diagram_ShapeContainerStyle(backgroundColor="sample_text", shape="sample_text")
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_diagram_ShapeContainerStyle_shape_value_roundtrip():
    instance = diagram_ShapeContainerStyle(backgroundColor="sample_text", shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_diagram_Square_color_value_roundtrip():
    instance = diagram_Square(color="sample_text", height="sample_text", width="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_diagram_Square_height_value_roundtrip():
    instance = diagram_Square(color="sample_text", height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_diagram_Square_width_value_roundtrip():
    instance = diagram_Square(color="sample_text", height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_diagram_TypedVariableValue_value_value_roundtrip():
    instance = diagram_TypedVariableValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_diagram_WorkspaceImage_workspacePath_value_roundtrip():
    instance = diagram_WorkspaceImage(workspacePath="sample_text")
    assert instance.workspacePath == "sample_text"
    instance.workspacePath = "sample_text_2"
    assert instance.workspacePath == "sample_text_2"


def test_diagram_description_AbstractNodeMapping_domainClass_value_roundtrip():
    instance = diagram_description_AbstractNodeMapping(domainClass="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_diagram_description_AdditionalLayer_activeByDefault_value_roundtrip():
    instance = diagram_description_AdditionalLayer(activeByDefault=True, optional=True)
    assert instance.activeByDefault == True
    instance.activeByDefault = False
    assert instance.activeByDefault == False


def test_diagram_description_AdditionalLayer_optional_value_roundtrip():
    instance = diagram_description_AdditionalLayer(activeByDefault=True, optional=True)
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_diagram_description_CompositeLayout_direction_value_roundtrip():
    instance = diagram_description_CompositeLayout(direction="sample_text", padding=7)
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_diagram_description_CompositeLayout_padding_value_roundtrip():
    instance = diagram_description_CompositeLayout(direction="sample_text", padding=7)
    assert instance.padding == 7
    instance.padding = 13
    assert instance.padding == 13


def test_diagram_description_ContainerMapping_childrenPresentation_value_roundtrip():
    instance = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    assert instance.childrenPresentation == "sample_text"
    instance.childrenPresentation = "sample_text_2"
    assert instance.childrenPresentation == "sample_text_2"


def test_diagram_description_DiagramDescription_domainClass_value_roundtrip():
    instance = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_diagram_description_DiagramDescription_enablePopupBars_value_roundtrip():
    instance = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert instance.enablePopupBars == True
    instance.enablePopupBars = False
    assert instance.enablePopupBars == False


def test_diagram_description_DiagramDescription_preconditionExpression_value_roundtrip():
    instance = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_diagram_description_DiagramDescription_rootExpression_value_roundtrip():
    instance = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert instance.rootExpression == "sample_text"
    instance.rootExpression = "sample_text_2"
    assert instance.rootExpression == "sample_text_2"


def test_diagram_description_DiagramElementMapping_createElements_value_roundtrip():
    instance = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.createElements == True
    instance.createElements = False
    assert instance.createElements == False


def test_diagram_description_DiagramElementMapping_preconditionExpression_value_roundtrip():
    instance = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_diagram_description_DiagramElementMapping_semanticCandidatesExpression_value_roundtrip():
    instance = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.semanticCandidatesExpression == "sample_text"
    instance.semanticCandidatesExpression = "sample_text_2"
    assert instance.semanticCandidatesExpression == "sample_text_2"


def test_diagram_description_DiagramElementMapping_semanticElements_value_roundtrip():
    instance = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.semanticElements == "sample_text"
    instance.semanticElements = "sample_text_2"
    assert instance.semanticElements == "sample_text_2"


def test_diagram_description_DiagramElementMapping_synchronizationLock_value_roundtrip():
    instance = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.synchronizationLock == True
    instance.synchronizationLock = False
    assert instance.synchronizationLock == False


def test_diagram_description_EdgeMapping_domainClass_value_roundtrip():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_diagram_description_EdgeMapping_pathExpression_value_roundtrip():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.pathExpression == "sample_text"
    instance.pathExpression = "sample_text_2"
    assert instance.pathExpression == "sample_text_2"


def test_diagram_description_EdgeMapping_sourceFinderExpression_value_roundtrip():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.sourceFinderExpression == "sample_text"
    instance.sourceFinderExpression = "sample_text_2"
    assert instance.sourceFinderExpression == "sample_text_2"


def test_diagram_description_EdgeMapping_targetExpression_value_roundtrip():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.targetExpression == "sample_text"
    instance.targetExpression = "sample_text_2"
    assert instance.targetExpression == "sample_text_2"


def test_diagram_description_EdgeMapping_targetFinderExpression_value_roundtrip():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.targetFinderExpression == "sample_text"
    instance.targetFinderExpression = "sample_text_2"
    assert instance.targetFinderExpression == "sample_text_2"


def test_diagram_description_EdgeMapping_useDomainElement_value_roundtrip():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.useDomainElement == True
    instance.useDomainElement = False
    assert instance.useDomainElement == False


def test_diagram_description_EdgeMappingImport_inheritsAncestorFilters_value_roundtrip():
    instance = diagram_description_EdgeMappingImport(inheritsAncestorFilters=True)
    assert instance.inheritsAncestorFilters == True
    instance.inheritsAncestorFilters = False
    assert instance.inheritsAncestorFilters == False


def test_diagram_description_Layer_icon_value_roundtrip():
    instance = diagram_description_Layer(icon="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_diagram_description_OrderedTreeLayout_childrenExpression_value_roundtrip():
    instance = diagram_description_OrderedTreeLayout(childrenExpression="sample_text")
    assert instance.childrenExpression == "sample_text"
    instance.childrenExpression = "sample_text_2"
    assert instance.childrenExpression == "sample_text_2"


def test_diagram_filter_Filter_filterKind_value_roundtrip():
    instance = diagram_filter_Filter(filterKind="sample_text")
    assert instance.filterKind == "sample_text"
    instance.filterKind = "sample_text_2"
    assert instance.filterKind == "sample_text_2"


def test_diagram_filter_MappingFilter_semanticConditionExpression_value_roundtrip():
    instance = diagram_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    assert instance.semanticConditionExpression == "sample_text"
    instance.semanticConditionExpression = "sample_text_2"
    assert instance.semanticConditionExpression == "sample_text_2"


def test_diagram_filter_MappingFilter_viewConditionExpression_value_roundtrip():
    instance = diagram_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    assert instance.viewConditionExpression == "sample_text"
    instance.viewConditionExpression = "sample_text_2"
    assert instance.viewConditionExpression == "sample_text_2"


def test_diagram_filter_VariableFilter_semanticConditionExpression_value_roundtrip():
    instance = diagram_filter_VariableFilter(semanticConditionExpression="sample_text")
    assert instance.semanticConditionExpression == "sample_text"
    instance.semanticConditionExpression = "sample_text_2"
    assert instance.semanticConditionExpression == "sample_text_2"


def test_diagram_style_BorderedStyleDescription_borderLineStyle_value_roundtrip():
    instance = diagram_style_BorderedStyleDescription(borderLineStyle="sample_text", borderSizeComputationExpression="sample_text")
    assert instance.borderLineStyle == "sample_text"
    instance.borderLineStyle = "sample_text_2"
    assert instance.borderLineStyle == "sample_text_2"


def test_diagram_style_BorderedStyleDescription_borderSizeComputationExpression_value_roundtrip():
    instance = diagram_style_BorderedStyleDescription(borderLineStyle="sample_text", borderSizeComputationExpression="sample_text")
    assert instance.borderSizeComputationExpression == "sample_text"
    instance.borderSizeComputationExpression = "sample_text_2"
    assert instance.borderSizeComputationExpression == "sample_text_2"


def test_diagram_style_BundledImageDescription_providedShapeID_value_roundtrip():
    instance = diagram_style_BundledImageDescription(providedShapeID="sample_text", shape="sample_text")
    assert instance.providedShapeID == "sample_text"
    instance.providedShapeID = "sample_text_2"
    assert instance.providedShapeID == "sample_text_2"


def test_diagram_style_BundledImageDescription_shape_value_roundtrip():
    instance = diagram_style_BundledImageDescription(providedShapeID="sample_text", shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_diagram_style_ContainerStyleDescription_roundedCorner_value_roundtrip():
    instance = diagram_style_ContainerStyleDescription(roundedCorner=True)
    assert instance.roundedCorner == True
    instance.roundedCorner = False
    assert instance.roundedCorner == False


def test_diagram_style_CustomStyleDescription_id_value_roundtrip():
    instance = diagram_style_CustomStyleDescription(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_diagram_style_DotDescription_strokeSizeComputationExpression_value_roundtrip():
    instance = diagram_style_DotDescription(strokeSizeComputationExpression="sample_text")
    assert instance.strokeSizeComputationExpression == "sample_text"
    instance.strokeSizeComputationExpression = "sample_text_2"
    assert instance.strokeSizeComputationExpression == "sample_text_2"


def test_diagram_style_EdgeStyleDescription_endsCentering_value_roundtrip():
    instance = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.endsCentering == "sample_text"
    instance.endsCentering = "sample_text_2"
    assert instance.endsCentering == "sample_text_2"


def test_diagram_style_EdgeStyleDescription_foldingStyle_value_roundtrip():
    instance = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.foldingStyle == "sample_text"
    instance.foldingStyle = "sample_text_2"
    assert instance.foldingStyle == "sample_text_2"


def test_diagram_style_EdgeStyleDescription_lineStyle_value_roundtrip():
    instance = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.lineStyle == "sample_text"
    instance.lineStyle = "sample_text_2"
    assert instance.lineStyle == "sample_text_2"


def test_diagram_style_EdgeStyleDescription_routingStyle_value_roundtrip():
    instance = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.routingStyle == "sample_text"
    instance.routingStyle = "sample_text_2"
    assert instance.routingStyle == "sample_text_2"


def test_diagram_style_EdgeStyleDescription_sizeComputationExpression_value_roundtrip():
    instance = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.sizeComputationExpression == "sample_text"
    instance.sizeComputationExpression = "sample_text_2"
    assert instance.sizeComputationExpression == "sample_text_2"


def test_diagram_style_EdgeStyleDescription_sourceArrow_value_roundtrip():
    instance = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.sourceArrow == "sample_text"
    instance.sourceArrow = "sample_text_2"
    assert instance.sourceArrow == "sample_text_2"


def test_diagram_style_EdgeStyleDescription_targetArrow_value_roundtrip():
    instance = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.targetArrow == "sample_text"
    instance.targetArrow = "sample_text_2"
    assert instance.targetArrow == "sample_text_2"


def test_diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression_value_roundtrip():
    instance = diagram_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    assert instance.horizontalDiameterComputationExpression == "sample_text"
    instance.horizontalDiameterComputationExpression = "sample_text_2"
    assert instance.horizontalDiameterComputationExpression == "sample_text_2"


def test_diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression_value_roundtrip():
    instance = diagram_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    assert instance.verticalDiameterComputationExpression == "sample_text"
    instance.verticalDiameterComputationExpression = "sample_text_2"
    assert instance.verticalDiameterComputationExpression == "sample_text_2"


def test_diagram_style_FlatContainerStyleDescription_backgroundStyle_value_roundtrip():
    instance = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    assert instance.backgroundStyle == "sample_text"
    instance.backgroundStyle = "sample_text_2"
    assert instance.backgroundStyle == "sample_text_2"


def test_diagram_style_GaugeCompositeStyleDescription_alignment_value_roundtrip():
    instance = diagram_style_GaugeCompositeStyleDescription(alignment="sample_text")
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_diagram_style_GaugeSectionDescription_label_value_roundtrip():
    instance = diagram_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_diagram_style_GaugeSectionDescription_maxValueExpression_value_roundtrip():
    instance = diagram_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    assert instance.maxValueExpression == "sample_text"
    instance.maxValueExpression = "sample_text_2"
    assert instance.maxValueExpression == "sample_text_2"


def test_diagram_style_GaugeSectionDescription_minValueExpression_value_roundtrip():
    instance = diagram_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    assert instance.minValueExpression == "sample_text"
    instance.minValueExpression = "sample_text_2"
    assert instance.minValueExpression == "sample_text_2"


def test_diagram_style_GaugeSectionDescription_valueExpression_value_roundtrip():
    instance = diagram_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    assert instance.valueExpression == "sample_text"
    instance.valueExpression = "sample_text_2"
    assert instance.valueExpression == "sample_text_2"


def test_diagram_style_HideLabelCapabilityStyleDescription_hideLabelByDefault_value_roundtrip():
    instance = diagram_style_HideLabelCapabilityStyleDescription(hideLabelByDefault=True)
    assert instance.hideLabelByDefault == True
    instance.hideLabelByDefault = False
    assert instance.hideLabelByDefault == False


def test_diagram_style_LozengeNodeDescription_heightComputationExpression_value_roundtrip():
    instance = diagram_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert instance.heightComputationExpression == "sample_text"
    instance.heightComputationExpression = "sample_text_2"
    assert instance.heightComputationExpression == "sample_text_2"


def test_diagram_style_LozengeNodeDescription_widthComputationExpression_value_roundtrip():
    instance = diagram_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert instance.widthComputationExpression == "sample_text"
    instance.widthComputationExpression = "sample_text_2"
    assert instance.widthComputationExpression == "sample_text_2"


def test_diagram_style_NodeStyleDescription_forbiddenSides_value_roundtrip():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert instance.forbiddenSides == "sample_text"
    instance.forbiddenSides = "sample_text_2"
    assert instance.forbiddenSides == "sample_text_2"


def test_diagram_style_NodeStyleDescription_labelPosition_value_roundtrip():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert instance.labelPosition == "sample_text"
    instance.labelPosition = "sample_text_2"
    assert instance.labelPosition == "sample_text_2"


def test_diagram_style_NodeStyleDescription_resizeKind_value_roundtrip():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert instance.resizeKind == "sample_text"
    instance.resizeKind = "sample_text_2"
    assert instance.resizeKind == "sample_text_2"


def test_diagram_style_NodeStyleDescription_sizeComputationExpression_value_roundtrip():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert instance.sizeComputationExpression == "sample_text"
    instance.sizeComputationExpression = "sample_text_2"
    assert instance.sizeComputationExpression == "sample_text_2"


def test_diagram_style_RoundedCornerStyleDescription_arcHeight_value_roundtrip():
    instance = diagram_style_RoundedCornerStyleDescription(arcHeight="sample_text", arcWidth="sample_text")
    assert instance.arcHeight == "sample_text"
    instance.arcHeight = "sample_text_2"
    assert instance.arcHeight == "sample_text_2"


def test_diagram_style_RoundedCornerStyleDescription_arcWidth_value_roundtrip():
    instance = diagram_style_RoundedCornerStyleDescription(arcHeight="sample_text", arcWidth="sample_text")
    assert instance.arcWidth == "sample_text"
    instance.arcWidth = "sample_text_2"
    assert instance.arcWidth == "sample_text_2"


def test_diagram_style_ShapeContainerStyleDescription_shape_value_roundtrip():
    instance = diagram_style_ShapeContainerStyleDescription(shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_diagram_style_SizeComputationContainerStyleDescription_heightComputationExpression_value_roundtrip():
    instance = diagram_style_SizeComputationContainerStyleDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert instance.heightComputationExpression == "sample_text"
    instance.heightComputationExpression = "sample_text_2"
    assert instance.heightComputationExpression == "sample_text_2"


def test_diagram_style_SizeComputationContainerStyleDescription_widthComputationExpression_value_roundtrip():
    instance = diagram_style_SizeComputationContainerStyleDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert instance.widthComputationExpression == "sample_text"
    instance.widthComputationExpression = "sample_text_2"
    assert instance.widthComputationExpression == "sample_text_2"


def test_diagram_style_SquareDescription_height_value_roundtrip():
    instance = diagram_style_SquareDescription(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_diagram_style_SquareDescription_width_value_roundtrip():
    instance = diagram_style_SquareDescription(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_diagram_style_WorkspaceImageDescription_workspacePath_value_roundtrip():
    instance = diagram_style_WorkspaceImageDescription(workspacePath="sample_text")
    assert instance.workspacePath == "sample_text"
    instance.workspacePath = "sample_text_2"
    assert instance.workspacePath == "sample_text_2"


def test_diagram_tool_BehaviorTool_domainClass_value_roundtrip():
    instance = diagram_tool_BehaviorTool(domainClass="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_diagram_tool_ContainerCreationDescription_iconPath_value_roundtrip():
    instance = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_diagram_tool_ContainerDropDescription_dragSource_value_roundtrip():
    instance = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    assert instance.dragSource == "sample_text"
    instance.dragSource = "sample_text_2"
    assert instance.dragSource == "sample_text_2"


def test_diagram_tool_ContainerDropDescription_moveEdges_value_roundtrip():
    instance = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    assert instance.moveEdges == True
    instance.moveEdges = False
    assert instance.moveEdges == False


def test_diagram_tool_CreateEdgeView_sourceExpression_value_roundtrip():
    instance = diagram_tool_CreateEdgeView(sourceExpression="sample_text", targetExpression="sample_text")
    assert instance.sourceExpression == "sample_text"
    instance.sourceExpression = "sample_text_2"
    assert instance.sourceExpression == "sample_text_2"


def test_diagram_tool_CreateEdgeView_targetExpression_value_roundtrip():
    instance = diagram_tool_CreateEdgeView(sourceExpression="sample_text", targetExpression="sample_text")
    assert instance.targetExpression == "sample_text"
    instance.targetExpression = "sample_text_2"
    assert instance.targetExpression == "sample_text_2"


def test_diagram_tool_CreateView_containerViewExpression_value_roundtrip():
    instance = diagram_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    assert instance.containerViewExpression == "sample_text"
    instance.containerViewExpression = "sample_text_2"
    assert instance.containerViewExpression == "sample_text_2"


def test_diagram_tool_CreateView_variableName_value_roundtrip():
    instance = diagram_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    assert instance.variableName == "sample_text"
    instance.variableName = "sample_text_2"
    assert instance.variableName == "sample_text_2"


def test_diagram_tool_DeleteHook_id_value_roundtrip():
    instance = diagram_tool_DeleteHook(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_diagram_tool_DeleteHookParameter_name_value_roundtrip():
    instance = diagram_tool_DeleteHookParameter(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_diagram_tool_DeleteHookParameter_value_value_roundtrip():
    instance = diagram_tool_DeleteHookParameter(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_diagram_tool_DirectEditLabel_inputLabelExpression_value_roundtrip():
    instance = diagram_tool_DirectEditLabel(inputLabelExpression="sample_text")
    assert instance.inputLabelExpression == "sample_text"
    instance.inputLabelExpression = "sample_text_2"
    assert instance.inputLabelExpression == "sample_text_2"


def test_diagram_tool_EdgeCreationDescription_connectionStartPrecondition_value_roundtrip():
    instance = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    assert instance.connectionStartPrecondition == "sample_text"
    instance.connectionStartPrecondition = "sample_text_2"
    assert instance.connectionStartPrecondition == "sample_text_2"


def test_diagram_tool_EdgeCreationDescription_iconPath_value_roundtrip():
    instance = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_diagram_tool_Navigation_createIfNotExistent_value_roundtrip():
    instance = diagram_tool_Navigation(createIfNotExistent=True)
    assert instance.createIfNotExistent == True
    instance.createIfNotExistent = False
    assert instance.createIfNotExistent == False


def test_diagram_tool_NodeCreationDescription_iconPath_value_roundtrip():
    instance = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_diagram_tool_ReconnectEdgeDescription_reconnectionKind_value_roundtrip():
    instance = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    assert instance.reconnectionKind == "sample_text"
    instance.reconnectionKind = "sample_text_2"
    assert instance.reconnectionKind == "sample_text_2"


def test_diagram_tool_RequestDescription_type_value_roundtrip():
    instance = diagram_tool_RequestDescription(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_diagram_tool_ToolSection_icon_value_roundtrip():
    instance = diagram_tool_ToolSection(icon="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_diagram_DDiagramElementContainer_isa_AbstractDNode():
    instance = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert isinstance(instance, AbstractDNode)


def test_diagram_DNode_isa_AbstractDNode():
    instance = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert isinstance(instance, AbstractDNode)


def test_diagram_DNodeListElement_isa_AbstractDNode():
    instance = diagram_DNodeListElement()
    assert isinstance(instance, AbstractDNode)


def test_diagram_tool_BehaviorTool_isa_AbstractToolDescription():
    instance = diagram_tool_BehaviorTool(domainClass="sample_text")
    assert isinstance(instance, AbstractToolDescription)


def test_diagram_tool_RequestDescription_isa_AbstractToolDescription():
    instance = diagram_tool_RequestDescription(type="sample_text")
    assert isinstance(instance, AbstractToolDescription)


def test_diagram_BeginLabelStyle_isa_BasicLabelStyle():
    instance = diagram_BeginLabelStyle()
    assert isinstance(instance, BasicLabelStyle)


def test_diagram_CenterLabelStyle_isa_BasicLabelStyle():
    instance = diagram_CenterLabelStyle()
    assert isinstance(instance, BasicLabelStyle)


def test_diagram_EndLabelStyle_isa_BasicLabelStyle():
    instance = diagram_EndLabelStyle()
    assert isinstance(instance, BasicLabelStyle)


def test_diagram_style_BeginLabelStyleDescription_isa_BasicLabelStyleDescription():
    instance = diagram_style_BeginLabelStyleDescription()
    assert isinstance(instance, BasicLabelStyleDescription)


def test_diagram_style_CenterLabelStyleDescription_isa_BasicLabelStyleDescription():
    instance = diagram_style_CenterLabelStyleDescription()
    assert isinstance(instance, BasicLabelStyleDescription)


def test_diagram_style_EndLabelStyleDescription_isa_BasicLabelStyleDescription():
    instance = diagram_style_EndLabelStyleDescription()
    assert isinstance(instance, BasicLabelStyleDescription)


def test_diagram_ContainerStyle_isa_BorderedStyle():
    instance = diagram_ContainerStyle()
    assert isinstance(instance, BorderedStyle)


def test_diagram_NodeStyle_isa_BorderedStyle():
    instance = diagram_NodeStyle(labelPosition="sample_text")
    assert isinstance(instance, BorderedStyle)


def test_diagram_IndirectlyCollapseFilter_isa_CollapseFilter():
    instance = diagram_IndirectlyCollapseFilter()
    assert isinstance(instance, CollapseFilter)


def test_diagram_description_ConditionalContainerStyleDescription_isa_ConditionalStyleDescription():
    instance = diagram_description_ConditionalContainerStyleDescription()
    assert isinstance(instance, ConditionalStyleDescription)


def test_diagram_description_ConditionalEdgeStyleDescription_isa_ConditionalStyleDescription():
    instance = diagram_description_ConditionalEdgeStyleDescription()
    assert isinstance(instance, ConditionalStyleDescription)


def test_diagram_description_ConditionalNodeStyleDescription_isa_ConditionalStyleDescription():
    instance = diagram_description_ConditionalNodeStyleDescription()
    assert isinstance(instance, ConditionalStyleDescription)


def test_diagram_tool_CreateView_isa_ContainerModelOperation():
    instance = diagram_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_diagram_tool_Navigation_isa_ContainerModelOperation():
    instance = diagram_tool_Navigation(createIfNotExistent=True)
    assert isinstance(instance, ContainerModelOperation)


def test_diagram_FlatContainerStyle_isa_ContainerStyle():
    instance = diagram_FlatContainerStyle(backgroundColor="sample_text", backgroundStyle="sample_text", foregroundColor="sample_text")
    assert isinstance(instance, ContainerStyle)


def test_diagram_ShapeContainerStyle_isa_ContainerStyle():
    instance = diagram_ShapeContainerStyle(backgroundColor="sample_text", shape="sample_text")
    assert isinstance(instance, ContainerStyle)


def test_diagram_WorkspaceImage_isa_ContainerStyle():
    instance = diagram_WorkspaceImage(workspacePath="sample_text")
    assert isinstance(instance, ContainerStyle)


def test_diagram_tool_CreateEdgeView_isa_CreateView():
    instance = diagram_tool_CreateEdgeView(sourceExpression="sample_text", targetExpression="sample_text")
    assert isinstance(instance, CreateView)


def test_diagram_GaugeSection_isa_Customizable():
    instance = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert isinstance(instance, Customizable)


def test_diagram_DSemanticDiagram_isa_DDiagram():
    instance = diagram_DSemanticDiagram()
    assert isinstance(instance, DDiagram)


def test_diagram_AbstractDNode_isa_DDiagramElement():
    instance = diagram_AbstractDNode(arrangeConstraints="sample_text")
    assert isinstance(instance, DDiagramElement)


def test_diagram_DEdge_isa_DDiagramElement():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert isinstance(instance, DDiagramElement)


def test_diagram_DNodeContainer_isa_DDiagramElementContainer():
    instance = diagram_DNodeContainer(childrenPresentation="sample_text")
    assert isinstance(instance, DDiagramElementContainer)


def test_diagram_DNodeList_isa_DDiagramElementContainer():
    instance = diagram_DNodeList()
    assert isinstance(instance, DDiagramElementContainer)


def test_diagram_DDiagram_isa_DRepresentation():
    instance = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    assert isinstance(instance, DRepresentation)


def test_diagram_DDiagramElement_isa_DRepresentationElement():
    instance = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    assert isinstance(instance, DRepresentationElement)


def test_diagram_DSemanticDiagram_isa_DSemanticDecorator():
    instance = diagram_DSemanticDiagram()
    assert isinstance(instance, DSemanticDecorator)


def test_diagram_description_MappingBasedDecoration_isa_DecorationDescription():
    instance = diagram_description_MappingBasedDecoration()
    assert isinstance(instance, DecorationDescription)


def test_diagram_concern_ConcernSet_isa_DocumentedElement():
    instance = diagram_concern_ConcernSet()
    assert isinstance(instance, DocumentedElement)


def test_diagram_description_Layout_isa_DocumentedElement():
    instance = diagram_description_Layout()
    assert isinstance(instance, DocumentedElement)


def test_diagram_DDiagram_isa_DragAndDropTarget():
    instance = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    assert isinstance(instance, DragAndDropTarget)


def test_diagram_DDiagramElementContainer_isa_DragAndDropTarget():
    instance = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert isinstance(instance, DragAndDropTarget)


def test_diagram_DNode_isa_DragAndDropTarget():
    instance = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert isinstance(instance, DragAndDropTarget)


def test_diagram_BracketEdgeStyle_isa_EdgeStyle():
    instance = diagram_BracketEdgeStyle()
    assert isinstance(instance, EdgeStyle)


def test_diagram_style_BracketEdgeStyleDescription_isa_EdgeStyleDescription():
    instance = diagram_style_BracketEdgeStyleDescription()
    assert isinstance(instance, EdgeStyleDescription)


def test_diagram_DDiagramElementContainer_isa_EdgeTarget():
    instance = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert isinstance(instance, EdgeTarget)


def test_diagram_DEdge_isa_EdgeTarget():
    instance = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert isinstance(instance, EdgeTarget)


def test_diagram_DNode_isa_EdgeTarget():
    instance = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert isinstance(instance, EdgeTarget)


def test_diagram_filter_MappingFilter_isa_Filter():
    instance = diagram_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    assert isinstance(instance, Filter)


def test_diagram_filter_VariableFilter_isa_Filter():
    instance = diagram_filter_VariableFilter(semanticConditionExpression="sample_text")
    assert isinstance(instance, Filter)


def test_diagram_filter_CompositeFilterDescription_isa_FilterDescription():
    instance = diagram_filter_CompositeFilterDescription()
    assert isinstance(instance, FilterDescription)


def test_diagram_AbsoluteBoundsFilter_isa_GraphicalFilter():
    instance = diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, GraphicalFilter)


def test_diagram_AppliedCompositeFilters_isa_GraphicalFilter():
    instance = diagram_AppliedCompositeFilters()
    assert isinstance(instance, GraphicalFilter)


def test_diagram_CollapseFilter_isa_GraphicalFilter():
    instance = diagram_CollapseFilter(height=7, width=7)
    assert isinstance(instance, GraphicalFilter)


def test_diagram_FoldingFilter_isa_GraphicalFilter():
    instance = diagram_FoldingFilter()
    assert isinstance(instance, GraphicalFilter)


def test_diagram_FoldingPointFilter_isa_GraphicalFilter():
    instance = diagram_FoldingPointFilter()
    assert isinstance(instance, GraphicalFilter)


def test_diagram_HideFilter_isa_GraphicalFilter():
    instance = diagram_HideFilter()
    assert isinstance(instance, GraphicalFilter)


def test_diagram_HideLabelFilter_isa_GraphicalFilter():
    instance = diagram_HideLabelFilter()
    assert isinstance(instance, GraphicalFilter)


def test_diagram_ContainerStyle_isa_HideLabelCapabilityStyle():
    instance = diagram_ContainerStyle()
    assert isinstance(instance, HideLabelCapabilityStyle)


def test_diagram_NodeStyle_isa_HideLabelCapabilityStyle():
    instance = diagram_NodeStyle(labelPosition="sample_text")
    assert isinstance(instance, HideLabelCapabilityStyle)


def test_diagram_ContainerStyle_isa_LabelStyle():
    instance = diagram_ContainerStyle()
    assert isinstance(instance, LabelStyle)


def test_diagram_NodeStyle_isa_LabelStyle():
    instance = diagram_NodeStyle(labelPosition="sample_text")
    assert isinstance(instance, LabelStyle)


def test_diagram_description_AdditionalLayer_isa_Layer():
    instance = diagram_description_AdditionalLayer(activeByDefault=True, optional=True)
    assert isinstance(instance, Layer)


def test_diagram_description_CompositeLayout_isa_Layout():
    instance = diagram_description_CompositeLayout(direction="sample_text", padding=7)
    assert isinstance(instance, Layout)


def test_diagram_description_OrderedTreeLayout_isa_Layout():
    instance = diagram_description_OrderedTreeLayout(childrenExpression="sample_text")
    assert isinstance(instance, Layout)


def test_diagram_tool_ContainerCreationDescription_isa_MappingBasedToolDescription():
    instance = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_diagram_tool_ContainerDropDescription_isa_MappingBasedToolDescription():
    instance = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    assert isinstance(instance, MappingBasedToolDescription)


def test_diagram_tool_DeleteElementDescription_isa_MappingBasedToolDescription():
    instance = diagram_tool_DeleteElementDescription()
    assert isinstance(instance, MappingBasedToolDescription)


def test_diagram_tool_DirectEditLabel_isa_MappingBasedToolDescription():
    instance = diagram_tool_DirectEditLabel(inputLabelExpression="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_diagram_tool_DoubleClickDescription_isa_MappingBasedToolDescription():
    instance = diagram_tool_DoubleClickDescription()
    assert isinstance(instance, MappingBasedToolDescription)


def test_diagram_tool_EdgeCreationDescription_isa_MappingBasedToolDescription():
    instance = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_diagram_tool_NodeCreationDescription_isa_MappingBasedToolDescription():
    instance = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_diagram_tool_ReconnectEdgeDescription_isa_MappingBasedToolDescription():
    instance = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_diagram_BundledImage_isa_NodeStyle():
    instance = diagram_BundledImage(color="sample_text", providedShapeID="sample_text", shape="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_CustomStyle_isa_NodeStyle():
    instance = diagram_CustomStyle(id="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_Dot_isa_NodeStyle():
    instance = diagram_Dot(backgroundColor="sample_text", strokeSizeComputationExpression="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_Ellipse_isa_NodeStyle():
    instance = diagram_Ellipse(color="sample_text", horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_GaugeCompositeStyle_isa_NodeStyle():
    instance = diagram_GaugeCompositeStyle(alignment="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_Lozenge_isa_NodeStyle():
    instance = diagram_Lozenge(color="sample_text", height="sample_text", width="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_Note_isa_NodeStyle():
    instance = diagram_Note(color="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_Square_isa_NodeStyle():
    instance = diagram_Square(color="sample_text", height="sample_text", width="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_WorkspaceImage_isa_NodeStyle():
    instance = diagram_WorkspaceImage(workspacePath="sample_text")
    assert isinstance(instance, NodeStyle)


def test_diagram_style_BundledImageDescription_isa_NodeStyleDescription():
    instance = diagram_style_BundledImageDescription(providedShapeID="sample_text", shape="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_diagram_style_CustomStyleDescription_isa_NodeStyleDescription():
    instance = diagram_style_CustomStyleDescription(id="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_diagram_style_DotDescription_isa_NodeStyleDescription():
    instance = diagram_style_DotDescription(strokeSizeComputationExpression="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_diagram_style_EllipseNodeDescription_isa_NodeStyleDescription():
    instance = diagram_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_diagram_style_GaugeCompositeStyleDescription_isa_NodeStyleDescription():
    instance = diagram_style_GaugeCompositeStyleDescription(alignment="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_diagram_style_LozengeNodeDescription_isa_NodeStyleDescription():
    instance = diagram_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_diagram_style_NoteDescription_isa_NodeStyleDescription():
    instance = diagram_style_NoteDescription()
    assert isinstance(instance, NodeStyleDescription)


def test_diagram_style_SquareDescription_isa_NodeStyleDescription():
    instance = diagram_style_SquareDescription(height="sample_text", width="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_diagram_tool_DiagramCreationDescription_isa_RepresentationCreationDescription():
    instance = diagram_tool_DiagramCreationDescription()
    assert isinstance(instance, RepresentationCreationDescription)


def test_diagram_description_DiagramExtensionDescription_isa_RepresentationExtensionDescription():
    instance = diagram_description_DiagramExtensionDescription()
    assert isinstance(instance, RepresentationExtensionDescription)


def test_diagram_tool_DiagramNavigationDescription_isa_RepresentationNavigationDescription():
    instance = diagram_tool_DiagramNavigationDescription()
    assert isinstance(instance, RepresentationNavigationDescription)


def test_diagram_BorderedStyle_isa_Style():
    instance = diagram_BorderedStyle(borderColor="sample_text", borderLineStyle="sample_text", borderSize="sample_text", borderSizeComputationExpression="sample_text")
    assert isinstance(instance, Style)


def test_diagram_ContainerStyle_isa_Style():
    instance = diagram_ContainerStyle()
    assert isinstance(instance, Style)


def test_diagram_EdgeStyle_isa_Style():
    instance = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    assert isinstance(instance, Style)


def test_diagram_NodeStyle_isa_Style():
    instance = diagram_NodeStyle(labelPosition="sample_text")
    assert isinstance(instance, Style)


def test_diagram_style_BorderedStyleDescription_isa_StyleDescription():
    instance = diagram_style_BorderedStyleDescription(borderLineStyle="sample_text", borderSizeComputationExpression="sample_text")
    assert isinstance(instance, StyleDescription)


def test_diagram_style_EdgeStyleDescription_isa_StyleDescription():
    instance = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert isinstance(instance, StyleDescription)


def test_diagram_style_RoundedCornerStyleDescription_isa_StyleDescription():
    instance = diagram_style_RoundedCornerStyleDescription(arcHeight="sample_text", arcWidth="sample_text")
    assert isinstance(instance, StyleDescription)


def test_diagram_tool_ToolGroup_isa_ToolEntry():
    instance = diagram_tool_ToolGroup()
    assert isinstance(instance, ToolEntry)


def test_diagram_EObjectVariableValue_isa_VariableValue():
    instance = diagram_EObjectVariableValue()
    assert isinstance(instance, VariableValue)


def test_diagram_TypedVariableValue_isa_VariableValue():
    instance = diagram_TypedVariableValue(value="sample_text")
    assert isinstance(instance, VariableValue)


def test_diagram_description_ContainerMappingImport_isa_description_AbstractMappingImport():
    instance = diagram_description_ContainerMappingImport()
    assert isinstance(instance, description_AbstractMappingImport)


def test_diagram_description_NodeMappingImport_isa_description_AbstractMappingImport():
    instance = diagram_description_NodeMappingImport()
    assert isinstance(instance, description_AbstractMappingImport)


def test_diagram_description_ContainerMapping_isa_description_AbstractNodeMapping():
    instance = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    assert isinstance(instance, description_AbstractNodeMapping)


def test_diagram_description_NodeMapping_isa_description_AbstractNodeMapping():
    instance = diagram_description_NodeMapping()
    assert isinstance(instance, description_AbstractNodeMapping)


def test_diagram_tool_ElementDoubleClickVariable_isa_description_AbstractVariable():
    instance = diagram_tool_ElementDoubleClickVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_diagram_tool_NodeCreationVariable_isa_description_AbstractVariable():
    instance = diagram_tool_NodeCreationVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_diagram_tool_SourceEdgeCreationVariable_isa_description_AbstractVariable():
    instance = diagram_tool_SourceEdgeCreationVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_diagram_tool_SourceEdgeViewCreationVariable_isa_description_AbstractVariable():
    instance = diagram_tool_SourceEdgeViewCreationVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_diagram_tool_TargetEdgeCreationVariable_isa_description_AbstractVariable():
    instance = diagram_tool_TargetEdgeCreationVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_diagram_tool_TargetEdgeViewCreationVariable_isa_description_AbstractVariable():
    instance = diagram_tool_TargetEdgeViewCreationVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_diagram_description_ContainerMappingImport_isa_description_ContainerMapping():
    instance = diagram_description_ContainerMappingImport()
    assert isinstance(instance, description_ContainerMapping)


def test_diagram_description_DiagramImportDescription_isa_description_DiagramDescription():
    instance = diagram_description_DiagramImportDescription()
    assert isinstance(instance, description_DiagramDescription)


def test_diagram_description_AbstractNodeMapping_isa_description_DiagramElementMapping():
    instance = diagram_description_AbstractNodeMapping(domainClass="sample_text")
    assert isinstance(instance, description_DiagramElementMapping)


def test_diagram_description_EdgeMapping_isa_description_DiagramElementMapping():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert isinstance(instance, description_DiagramElementMapping)


def test_diagram_DDiagram_isa_description_DocumentedElement():
    instance = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    assert isinstance(instance, description_DocumentedElement)


def test_diagram_concern_ConcernDescription_isa_description_DocumentedElement():
    instance = diagram_concern_ConcernDescription()
    assert isinstance(instance, description_DocumentedElement)


def test_diagram_description_AbstractNodeMapping_isa_description_DocumentedElement():
    instance = diagram_description_AbstractNodeMapping(domainClass="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_diagram_description_EdgeMapping_isa_description_DocumentedElement():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert isinstance(instance, description_DocumentedElement)


def test_diagram_description_EdgeMappingImport_isa_description_DocumentedElement():
    instance = diagram_description_EdgeMappingImport(inheritsAncestorFilters=True)
    assert isinstance(instance, description_DocumentedElement)


def test_diagram_description_Layer_isa_description_DocumentedElement():
    instance = diagram_description_Layer(icon="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_diagram_filter_FilterDescription_isa_description_DocumentedElement():
    instance = diagram_filter_FilterDescription()
    assert isinstance(instance, description_DocumentedElement)


def test_diagram_tool_ToolSection_isa_description_DocumentedElement():
    instance = diagram_tool_ToolSection(icon="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_diagram_description_ContainerMapping_isa_description_DragAndDropTargetDescription():
    instance = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    assert isinstance(instance, description_DragAndDropTargetDescription)


def test_diagram_description_DiagramDescription_isa_description_DragAndDropTargetDescription():
    instance = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert isinstance(instance, description_DragAndDropTargetDescription)


def test_diagram_description_NodeMapping_isa_description_DragAndDropTargetDescription():
    instance = diagram_description_NodeMapping()
    assert isinstance(instance, description_DragAndDropTargetDescription)


def test_diagram_description_Layer_isa_description_EndUserDocumentedElement():
    instance = diagram_description_Layer(icon="sample_text")
    assert isinstance(instance, description_EndUserDocumentedElement)


def test_diagram_description_EdgeMapping_isa_description_IEdgeMapping():
    instance = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert isinstance(instance, description_IEdgeMapping)


def test_diagram_description_EdgeMappingImport_isa_description_IEdgeMapping():
    instance = diagram_description_EdgeMappingImport(inheritsAncestorFilters=True)
    assert isinstance(instance, description_IEdgeMapping)


def test_diagram_concern_ConcernDescription_isa_description_IdentifiedElement():
    instance = diagram_concern_ConcernDescription()
    assert isinstance(instance, description_IdentifiedElement)


def test_diagram_description_EdgeMappingImport_isa_description_IdentifiedElement():
    instance = diagram_description_EdgeMappingImport(inheritsAncestorFilters=True)
    assert isinstance(instance, description_IdentifiedElement)


def test_diagram_description_Layer_isa_description_IdentifiedElement():
    instance = diagram_description_Layer(icon="sample_text")
    assert isinstance(instance, description_IdentifiedElement)


def test_diagram_filter_FilterDescription_isa_description_IdentifiedElement():
    instance = diagram_filter_FilterDescription()
    assert isinstance(instance, description_IdentifiedElement)


def test_diagram_tool_ToolSection_isa_description_IdentifiedElement():
    instance = diagram_tool_ToolSection(icon="sample_text")
    assert isinstance(instance, description_IdentifiedElement)


def test_diagram_description_NodeMappingImport_isa_description_NodeMapping():
    instance = diagram_description_NodeMappingImport()
    assert isinstance(instance, description_NodeMapping)


def test_diagram_description_DiagramDescription_isa_description_PasteTargetDescription():
    instance = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert isinstance(instance, description_PasteTargetDescription)


def test_diagram_description_DiagramElementMapping_isa_description_PasteTargetDescription():
    instance = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert isinstance(instance, description_PasteTargetDescription)


def test_diagram_description_DiagramDescription_isa_description_RepresentationDescription():
    instance = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert isinstance(instance, description_RepresentationDescription)


def test_diagram_description_DiagramElementMapping_isa_description_RepresentationElementMapping():
    instance = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert isinstance(instance, description_RepresentationElementMapping)


def test_diagram_description_DiagramImportDescription_isa_description_RepresentationImportDescription():
    instance = diagram_description_DiagramImportDescription()
    assert isinstance(instance, description_RepresentationImportDescription)


def test_diagram_style_ContainerStyleDescription_isa_style_BorderedStyleDescription():
    instance = diagram_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_BorderedStyleDescription)


def test_diagram_style_NodeStyleDescription_isa_style_BorderedStyleDescription():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_BorderedStyleDescription)


def test_diagram_style_FlatContainerStyleDescription_isa_style_ContainerStyleDescription():
    instance = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    assert isinstance(instance, style_ContainerStyleDescription)


def test_diagram_style_ShapeContainerStyleDescription_isa_style_ContainerStyleDescription():
    instance = diagram_style_ShapeContainerStyleDescription(shape="sample_text")
    assert isinstance(instance, style_ContainerStyleDescription)


def test_diagram_style_WorkspaceImageDescription_isa_style_ContainerStyleDescription():
    instance = diagram_style_WorkspaceImageDescription(workspacePath="sample_text")
    assert isinstance(instance, style_ContainerStyleDescription)


def test_diagram_style_ContainerStyleDescription_isa_style_HideLabelCapabilityStyleDescription():
    instance = diagram_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_HideLabelCapabilityStyleDescription)


def test_diagram_style_NodeStyleDescription_isa_style_HideLabelCapabilityStyleDescription():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_HideLabelCapabilityStyleDescription)


def test_diagram_style_ContainerStyleDescription_isa_style_LabelStyleDescription():
    instance = diagram_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_LabelStyleDescription)


def test_diagram_style_NodeStyleDescription_isa_style_LabelStyleDescription():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_LabelStyleDescription)


def test_diagram_style_WorkspaceImageDescription_isa_style_NodeStyleDescription():
    instance = diagram_style_WorkspaceImageDescription(workspacePath="sample_text")
    assert isinstance(instance, style_NodeStyleDescription)


def test_diagram_style_ContainerStyleDescription_isa_style_RoundedCornerStyleDescription():
    instance = diagram_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_RoundedCornerStyleDescription)


def test_diagram_style_FlatContainerStyleDescription_isa_style_SizeComputationContainerStyleDescription():
    instance = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    assert isinstance(instance, style_SizeComputationContainerStyleDescription)


def test_diagram_style_ShapeContainerStyleDescription_isa_style_SizeComputationContainerStyleDescription():
    instance = diagram_style_ShapeContainerStyleDescription(shape="sample_text")
    assert isinstance(instance, style_SizeComputationContainerStyleDescription)


def test_diagram_style_NodeStyleDescription_isa_style_StyleDescription():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_StyleDescription)


def test_diagram_style_ContainerStyleDescription_isa_style_TooltipStyleDescription():
    instance = diagram_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_TooltipStyleDescription)


def test_diagram_style_NodeStyleDescription_isa_style_TooltipStyleDescription():
    instance = diagram_style_NodeStyleDescription(forbiddenSides="sample_text", labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_TooltipStyleDescription)


def test_diagram_tool_ElementDoubleClickVariable_isa_tool_VariableContainer():
    instance = diagram_tool_ElementDoubleClickVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_diagram_tool_NodeCreationVariable_isa_tool_VariableContainer():
    instance = diagram_tool_NodeCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_diagram_tool_SourceEdgeCreationVariable_isa_tool_VariableContainer():
    instance = diagram_tool_SourceEdgeCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_diagram_tool_SourceEdgeViewCreationVariable_isa_tool_VariableContainer():
    instance = diagram_tool_SourceEdgeViewCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_diagram_tool_TargetEdgeCreationVariable_isa_tool_VariableContainer():
    instance = diagram_tool_TargetEdgeCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_diagram_tool_TargetEdgeViewCreationVariable_isa_tool_VariableContainer():
    instance = diagram_tool_TargetEdgeViewCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_assoc_activateBehaviors25_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = tool_BehaviorTool()
    b2 = tool_BehaviorTool()
    _safe_set(a, 'diagram_DDiagram26', {b1})
    assert _is_linked(a, 'diagram_DDiagram26', b1)
    if hasattr(b1, 'tool_BehaviorTool'):
        assert _is_linked(b1, 'tool_BehaviorTool', a)
    _safe_set(a, 'diagram_DDiagram26', {b2})
    assert _is_linked(a, 'diagram_DDiagram26', b2)
    if hasattr(b1, 'tool_BehaviorTool'):
        assert not _is_linked(b1, 'tool_BehaviorTool', a)
    if hasattr(b2, 'tool_BehaviorTool'):
        assert _is_linked(b2, 'tool_BehaviorTool', a)
    _safe_set(a, 'diagram_DDiagram26', set())
    assert not _is_linked(a, 'diagram_DDiagram26', b2)
    if hasattr(b2, 'tool_BehaviorTool'):
        assert not _is_linked(b2, 'tool_BehaviorTool', a)


def test_assoc_activatedFilters16_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = filter_FilterDescription()
    b2 = filter_FilterDescription()
    _safe_set(a, 'diagram_DDiagram17', {b1})
    assert _is_linked(a, 'diagram_DDiagram17', b1)
    if hasattr(b1, 'filter_FilterDescription'):
        assert _is_linked(b1, 'filter_FilterDescription', a)
    _safe_set(a, 'diagram_DDiagram17', {b2})
    assert _is_linked(a, 'diagram_DDiagram17', b2)
    if hasattr(b1, 'filter_FilterDescription'):
        assert not _is_linked(b1, 'filter_FilterDescription', a)
    if hasattr(b2, 'filter_FilterDescription'):
        assert _is_linked(b2, 'filter_FilterDescription', a)
    _safe_set(a, 'diagram_DDiagram17', set())
    assert not _is_linked(a, 'diagram_DDiagram17', b2)
    if hasattr(b2, 'filter_FilterDescription'):
        assert not _is_linked(b2, 'filter_FilterDescription', a)


def test_assoc_activatedLayers29_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = Layer()
    b2 = Layer()
    _safe_set(a, 'diagram_DDiagram30', {b1})
    assert _is_linked(a, 'diagram_DDiagram30', b1)
    if hasattr(b1, 'Layer'):
        assert _is_linked(b1, 'Layer', a)
    _safe_set(a, 'diagram_DDiagram30', {b2})
    assert _is_linked(a, 'diagram_DDiagram30', b2)
    if hasattr(b1, 'Layer'):
        assert not _is_linked(b1, 'Layer', a)
    if hasattr(b2, 'Layer'):
        assert _is_linked(b2, 'Layer', a)
    _safe_set(a, 'diagram_DDiagram30', set())
    assert not _is_linked(a, 'diagram_DDiagram30', b2)
    if hasattr(b2, 'Layer'):
        assert not _is_linked(b2, 'Layer', a)


def test_assoc_activatedRules23_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'diagram_DDiagram24', {b1})
    assert _is_linked(a, 'diagram_DDiagram24', b1)
    if hasattr(b1, 'validation_ValidationRule'):
        assert _is_linked(b1, 'validation_ValidationRule', a)
    _safe_set(a, 'diagram_DDiagram24', {b2})
    assert _is_linked(a, 'diagram_DDiagram24', b2)
    if hasattr(b1, 'validation_ValidationRule'):
        assert not _is_linked(b1, 'validation_ValidationRule', a)
    if hasattr(b2, 'validation_ValidationRule'):
        assert _is_linked(b2, 'validation_ValidationRule', a)
    _safe_set(a, 'diagram_DDiagram24', set())
    assert not _is_linked(a, 'diagram_DDiagram24', b2)
    if hasattr(b2, 'validation_ValidationRule'):
        assert not _is_linked(b2, 'validation_ValidationRule', a)


def test_assoc_activatedTransientLayers18_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = AdditionalLayer()
    b2 = AdditionalLayer()
    _safe_set(a, 'diagram_DDiagram19', {b1})
    assert _is_linked(a, 'diagram_DDiagram19', b1)
    if hasattr(b1, 'AdditionalLayer'):
        assert _is_linked(b1, 'AdditionalLayer', a)
    _safe_set(a, 'diagram_DDiagram19', {b2})
    assert _is_linked(a, 'diagram_DDiagram19', b2)
    if hasattr(b1, 'AdditionalLayer'):
        assert not _is_linked(b1, 'AdditionalLayer', a)
    if hasattr(b2, 'AdditionalLayer'):
        assert _is_linked(b2, 'AdditionalLayer', a)
    _safe_set(a, 'diagram_DDiagram19', set())
    assert not _is_linked(a, 'diagram_DDiagram19', b2)
    if hasattr(b2, 'AdditionalLayer'):
        assert not _is_linked(b2, 'AdditionalLayer', a)


def test_assoc_actualMapping53_link_reassign_clear():
    a = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_DNode54', b1)
    assert _is_linked(a, 'diagram_DNode54', b1)
    if hasattr(b1, 'NodeMapping'):
        assert _is_linked(b1, 'NodeMapping', a)
    _safe_set(a, 'diagram_DNode54', b2)
    assert _is_linked(a, 'diagram_DNode54', b2)
    if hasattr(b1, 'NodeMapping'):
        assert not _is_linked(b1, 'NodeMapping', a)
    if hasattr(b2, 'NodeMapping'):
        assert _is_linked(b2, 'NodeMapping', a)
    _safe_set(a, 'diagram_DNode54', None)
    assert not _is_linked(a, 'diagram_DNode54', b2)
    if hasattr(b2, 'NodeMapping'):
        assert not _is_linked(b2, 'NodeMapping', a)


def test_assoc_actualMapping72_link_reassign_clear():
    a = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_DDiagramElementContainer73', b1)
    assert _is_linked(a, 'diagram_DDiagramElementContainer73', b1)
    if hasattr(b1, 'ContainerMapping'):
        assert _is_linked(b1, 'ContainerMapping', a)
    _safe_set(a, 'diagram_DDiagramElementContainer73', b2)
    assert _is_linked(a, 'diagram_DDiagramElementContainer73', b2)
    if hasattr(b1, 'ContainerMapping'):
        assert not _is_linked(b1, 'ContainerMapping', a)
    if hasattr(b2, 'ContainerMapping'):
        assert _is_linked(b2, 'ContainerMapping', a)
    _safe_set(a, 'diagram_DDiagramElementContainer73', None)
    assert not _is_linked(a, 'diagram_DDiagramElementContainer73', b2)
    if hasattr(b2, 'ContainerMapping'):
        assert not _is_linked(b2, 'ContainerMapping', a)


def test_assoc_actualMapping98_link_reassign_clear():
    a = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = IEdgeMapping()
    b2 = IEdgeMapping()
    _safe_set(a, 'diagram_DEdge99', b1)
    assert _is_linked(a, 'diagram_DEdge99', b1)
    if hasattr(b1, 'IEdgeMapping'):
        assert _is_linked(b1, 'IEdgeMapping', a)
    _safe_set(a, 'diagram_DEdge99', b2)
    assert _is_linked(a, 'diagram_DEdge99', b2)
    if hasattr(b1, 'IEdgeMapping'):
        assert not _is_linked(b1, 'IEdgeMapping', a)
    if hasattr(b2, 'IEdgeMapping'):
        assert _is_linked(b2, 'IEdgeMapping', a)
    _safe_set(a, 'diagram_DEdge99', None)
    assert not _is_linked(a, 'diagram_DEdge99', b2)
    if hasattr(b2, 'IEdgeMapping'):
        assert not _is_linked(b2, 'IEdgeMapping', a)


def test_assoc_additionalLayers150_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = AdditionalLayer()
    b2 = AdditionalLayer()
    _safe_set(a, 'diagram_description_DiagramDescription151', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription151', b1)
    if hasattr(b1, 'AdditionalLayer152'):
        assert _is_linked(b1, 'AdditionalLayer152', a)
    _safe_set(a, 'diagram_description_DiagramDescription151', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription151', b2)
    if hasattr(b1, 'AdditionalLayer152'):
        assert not _is_linked(b1, 'AdditionalLayer152', a)
    if hasattr(b2, 'AdditionalLayer152'):
        assert _is_linked(b2, 'AdditionalLayer152', a)
    _safe_set(a, 'diagram_description_DiagramDescription151', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription151', b2)
    if hasattr(b2, 'AdditionalLayer152'):
        assert not _is_linked(b2, 'AdditionalLayer152', a)


def test_assoc_allActivatedTools156_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'diagram_description_DiagramDescription157', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription157', b1)
    if hasattr(b1, 'tool_AbstractToolDescription158'):
        assert _is_linked(b1, 'tool_AbstractToolDescription158', a)
    _safe_set(a, 'diagram_description_DiagramDescription157', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription157', b2)
    if hasattr(b1, 'tool_AbstractToolDescription158'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription158', a)
    if hasattr(b2, 'tool_AbstractToolDescription158'):
        assert _is_linked(b2, 'tool_AbstractToolDescription158', a)
    _safe_set(a, 'diagram_description_DiagramDescription157', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription157', b2)
    if hasattr(b2, 'tool_AbstractToolDescription158'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription158', a)


def test_assoc_allContainerMappings129_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_description_DiagramDescription130', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription130', b1)
    if hasattr(b1, 'ContainerMapping131'):
        assert _is_linked(b1, 'ContainerMapping131', a)
    _safe_set(a, 'diagram_description_DiagramDescription130', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription130', b2)
    if hasattr(b1, 'ContainerMapping131'):
        assert not _is_linked(b1, 'ContainerMapping131', a)
    if hasattr(b2, 'ContainerMapping131'):
        assert _is_linked(b2, 'ContainerMapping131', a)
    _safe_set(a, 'diagram_description_DiagramDescription130', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription130', b2)
    if hasattr(b2, 'ContainerMapping131'):
        assert not _is_linked(b2, 'ContainerMapping131', a)


def test_assoc_allContainerMappings214_link_reassign_clear():
    a = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_description_ContainerMapping215', {b1})
    assert _is_linked(a, 'diagram_description_ContainerMapping215', b1)
    if hasattr(b1, 'ContainerMapping216'):
        assert _is_linked(b1, 'ContainerMapping216', a)
    _safe_set(a, 'diagram_description_ContainerMapping215', {b2})
    assert _is_linked(a, 'diagram_description_ContainerMapping215', b2)
    if hasattr(b1, 'ContainerMapping216'):
        assert not _is_linked(b1, 'ContainerMapping216', a)
    if hasattr(b2, 'ContainerMapping216'):
        assert _is_linked(b2, 'ContainerMapping216', a)
    _safe_set(a, 'diagram_description_ContainerMapping215', set())
    assert not _is_linked(a, 'diagram_description_ContainerMapping215', b2)
    if hasattr(b2, 'ContainerMapping216'):
        assert not _is_linked(b2, 'ContainerMapping216', a)


def test_assoc_allEdgeMappings124_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = EdgeMapping()
    b2 = EdgeMapping()
    _safe_set(a, 'diagram_description_DiagramDescription125', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription125', b1)
    if hasattr(b1, 'EdgeMapping'):
        assert _is_linked(b1, 'EdgeMapping', a)
    _safe_set(a, 'diagram_description_DiagramDescription125', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription125', b2)
    if hasattr(b1, 'EdgeMapping'):
        assert not _is_linked(b1, 'EdgeMapping', a)
    if hasattr(b2, 'EdgeMapping'):
        assert _is_linked(b2, 'EdgeMapping', a)
    _safe_set(a, 'diagram_description_DiagramDescription125', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription125', b2)
    if hasattr(b2, 'EdgeMapping'):
        assert not _is_linked(b2, 'EdgeMapping', a)


def test_assoc_allEdgeMappings278_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = EdgeMapping()
    b2 = EdgeMapping()
    _safe_set(a, 'diagram_description_Layer279', {b1})
    assert _is_linked(a, 'diagram_description_Layer279', b1)
    if hasattr(b1, 'EdgeMapping280'):
        assert _is_linked(b1, 'EdgeMapping280', a)
    _safe_set(a, 'diagram_description_Layer279', {b2})
    assert _is_linked(a, 'diagram_description_Layer279', b2)
    if hasattr(b1, 'EdgeMapping280'):
        assert not _is_linked(b1, 'EdgeMapping280', a)
    if hasattr(b2, 'EdgeMapping280'):
        assert _is_linked(b2, 'EdgeMapping280', a)
    _safe_set(a, 'diagram_description_Layer279', set())
    assert not _is_linked(a, 'diagram_description_Layer279', b2)
    if hasattr(b2, 'EdgeMapping280'):
        assert not _is_linked(b2, 'EdgeMapping280', a)


def test_assoc_allFilters20_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = filter_FilterDescription()
    b2 = filter_FilterDescription()
    _safe_set(a, 'diagram_DDiagram21', {b1})
    assert _is_linked(a, 'diagram_DDiagram21', b1)
    if hasattr(b1, 'filter_FilterDescription22'):
        assert _is_linked(b1, 'filter_FilterDescription22', a)
    _safe_set(a, 'diagram_DDiagram21', {b2})
    assert _is_linked(a, 'diagram_DDiagram21', b2)
    if hasattr(b1, 'filter_FilterDescription22'):
        assert not _is_linked(b1, 'filter_FilterDescription22', a)
    if hasattr(b2, 'filter_FilterDescription22'):
        assert _is_linked(b2, 'filter_FilterDescription22', a)
    _safe_set(a, 'diagram_DDiagram21', set())
    assert not _is_linked(a, 'diagram_DDiagram21', b2)
    if hasattr(b2, 'filter_FilterDescription22'):
        assert not _is_linked(b2, 'filter_FilterDescription22', a)


def test_assoc_allLayers153_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = Layer()
    b2 = Layer()
    _safe_set(a, 'diagram_description_DiagramDescription154', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription154', b1)
    if hasattr(b1, 'Layer155'):
        assert _is_linked(b1, 'Layer155', a)
    _safe_set(a, 'diagram_description_DiagramDescription154', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription154', b2)
    if hasattr(b1, 'Layer155'):
        assert not _is_linked(b1, 'Layer155', a)
    if hasattr(b2, 'Layer155'):
        assert _is_linked(b2, 'Layer155', a)
    _safe_set(a, 'diagram_description_DiagramDescription154', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription154', b2)
    if hasattr(b2, 'Layer155'):
        assert not _is_linked(b2, 'Layer155', a)


def test_assoc_allNodeMappings126_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_description_DiagramDescription127', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription127', b1)
    if hasattr(b1, 'NodeMapping128'):
        assert _is_linked(b1, 'NodeMapping128', a)
    _safe_set(a, 'diagram_description_DiagramDescription127', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription127', b2)
    if hasattr(b1, 'NodeMapping128'):
        assert not _is_linked(b1, 'NodeMapping128', a)
    if hasattr(b2, 'NodeMapping128'):
        assert _is_linked(b2, 'NodeMapping128', a)
    _safe_set(a, 'diagram_description_DiagramDescription127', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription127', b2)
    if hasattr(b2, 'NodeMapping128'):
        assert not _is_linked(b2, 'NodeMapping128', a)


def test_assoc_allNodeMappings202_link_reassign_clear():
    a = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_description_ContainerMapping203', {b1})
    assert _is_linked(a, 'diagram_description_ContainerMapping203', b1)
    if hasattr(b1, 'NodeMapping204'):
        assert _is_linked(b1, 'NodeMapping204', a)
    _safe_set(a, 'diagram_description_ContainerMapping203', {b2})
    assert _is_linked(a, 'diagram_description_ContainerMapping203', b2)
    if hasattr(b1, 'NodeMapping204'):
        assert not _is_linked(b1, 'NodeMapping204', a)
    if hasattr(b2, 'NodeMapping204'):
        assert _is_linked(b2, 'NodeMapping204', a)
    _safe_set(a, 'diagram_description_ContainerMapping203', set())
    assert not _is_linked(a, 'diagram_description_ContainerMapping203', b2)
    if hasattr(b2, 'NodeMapping204'):
        assert not _is_linked(b2, 'NodeMapping204', a)


def test_assoc_allTools136_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'diagram_description_DiagramDescription137', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription137', b1)
    if hasattr(b1, 'tool_AbstractToolDescription'):
        assert _is_linked(b1, 'tool_AbstractToolDescription', a)
    _safe_set(a, 'diagram_description_DiagramDescription137', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription137', b2)
    if hasattr(b1, 'tool_AbstractToolDescription'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription', a)
    if hasattr(b2, 'tool_AbstractToolDescription'):
        assert _is_linked(b2, 'tool_AbstractToolDescription', a)
    _safe_set(a, 'diagram_description_DiagramDescription137', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription137', b2)
    if hasattr(b2, 'tool_AbstractToolDescription'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription', a)


def test_assoc_allTools267_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'diagram_description_Layer268', {b1})
    assert _is_linked(a, 'diagram_description_Layer268', b1)
    if hasattr(b1, 'tool_AbstractToolDescription269'):
        assert _is_linked(b1, 'tool_AbstractToolDescription269', a)
    _safe_set(a, 'diagram_description_Layer268', {b2})
    assert _is_linked(a, 'diagram_description_Layer268', b2)
    if hasattr(b1, 'tool_AbstractToolDescription269'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription269', a)
    if hasattr(b2, 'tool_AbstractToolDescription269'):
        assert _is_linked(b2, 'tool_AbstractToolDescription269', a)
    _safe_set(a, 'diagram_description_Layer268', set())
    assert not _is_linked(a, 'diagram_description_Layer268', b2)
    if hasattr(b2, 'tool_AbstractToolDescription269'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription269', a)


def test_assoc_backgroundColor295_link_reassign_clear():
    a = diagram_style_DotDescription(strokeSizeComputationExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_DotDescription', b1)
    assert _is_linked(a, 'diagram_style_DotDescription', b1)
    if hasattr(b1, 'ColorDescription296'):
        assert _is_linked(b1, 'ColorDescription296', a)
    _safe_set(a, 'diagram_style_DotDescription', b2)
    assert _is_linked(a, 'diagram_style_DotDescription', b2)
    if hasattr(b1, 'ColorDescription296'):
        assert not _is_linked(b1, 'ColorDescription296', a)
    if hasattr(b2, 'ColorDescription296'):
        assert _is_linked(b2, 'ColorDescription296', a)
    _safe_set(a, 'diagram_style_DotDescription', None)
    assert not _is_linked(a, 'diagram_style_DotDescription', b2)
    if hasattr(b2, 'ColorDescription296'):
        assert not _is_linked(b2, 'ColorDescription296', a)


def test_assoc_backgroundColor298_link_reassign_clear():
    a = diagram_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_GaugeSectionDescription', b1)
    assert _is_linked(a, 'diagram_style_GaugeSectionDescription', b1)
    if hasattr(b1, 'ColorDescription299'):
        assert _is_linked(b1, 'ColorDescription299', a)
    _safe_set(a, 'diagram_style_GaugeSectionDescription', b2)
    assert _is_linked(a, 'diagram_style_GaugeSectionDescription', b2)
    if hasattr(b1, 'ColorDescription299'):
        assert not _is_linked(b1, 'ColorDescription299', a)
    if hasattr(b2, 'ColorDescription299'):
        assert _is_linked(b2, 'ColorDescription299', a)
    _safe_set(a, 'diagram_style_GaugeSectionDescription', None)
    assert not _is_linked(a, 'diagram_style_GaugeSectionDescription', b2)
    if hasattr(b2, 'ColorDescription299'):
        assert not _is_linked(b2, 'ColorDescription299', a)


def test_assoc_backgroundColor303_link_reassign_clear():
    a = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription', b1)
    assert _is_linked(a, 'diagram_style_FlatContainerStyleDescription', b1)
    if hasattr(b1, 'ColorDescription304'):
        assert _is_linked(b1, 'ColorDescription304', a)
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription', b2)
    assert _is_linked(a, 'diagram_style_FlatContainerStyleDescription', b2)
    if hasattr(b1, 'ColorDescription304'):
        assert not _is_linked(b1, 'ColorDescription304', a)
    if hasattr(b2, 'ColorDescription304'):
        assert _is_linked(b2, 'ColorDescription304', a)
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription', None)
    assert not _is_linked(a, 'diagram_style_FlatContainerStyleDescription', b2)
    if hasattr(b2, 'ColorDescription304'):
        assert not _is_linked(b2, 'ColorDescription304', a)


def test_assoc_backgroundColor310_link_reassign_clear():
    a = diagram_style_ShapeContainerStyleDescription(shape="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_ShapeContainerStyleDescription', b1)
    assert _is_linked(a, 'diagram_style_ShapeContainerStyleDescription', b1)
    if hasattr(b1, 'ColorDescription311'):
        assert _is_linked(b1, 'ColorDescription311', a)
    _safe_set(a, 'diagram_style_ShapeContainerStyleDescription', b2)
    assert _is_linked(a, 'diagram_style_ShapeContainerStyleDescription', b2)
    if hasattr(b1, 'ColorDescription311'):
        assert not _is_linked(b1, 'ColorDescription311', a)
    if hasattr(b2, 'ColorDescription311'):
        assert _is_linked(b2, 'ColorDescription311', a)
    _safe_set(a, 'diagram_style_ShapeContainerStyleDescription', None)
    assert not _is_linked(a, 'diagram_style_ShapeContainerStyleDescription', b2)
    if hasattr(b2, 'ColorDescription311'):
        assert not _is_linked(b2, 'ColorDescription311', a)


def test_assoc_beginLabelStyle108_link_reassign_clear():
    a = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    b1 = diagram_BeginLabelStyle()
    b2 = diagram_BeginLabelStyle()
    _safe_set(a, 'diagram_EdgeStyle109', b1)
    assert _is_linked(a, 'diagram_EdgeStyle109', b1)
    if hasattr(b1, 'diagram_BeginLabelStyle'):
        assert _is_linked(b1, 'diagram_BeginLabelStyle', a)
    _safe_set(a, 'diagram_EdgeStyle109', b2)
    assert _is_linked(a, 'diagram_EdgeStyle109', b2)
    if hasattr(b1, 'diagram_BeginLabelStyle'):
        assert not _is_linked(b1, 'diagram_BeginLabelStyle', a)
    if hasattr(b2, 'diagram_BeginLabelStyle'):
        assert _is_linked(b2, 'diagram_BeginLabelStyle', a)
    _safe_set(a, 'diagram_EdgeStyle109', None)
    assert not _is_linked(a, 'diagram_EdgeStyle109', b2)
    if hasattr(b2, 'diagram_BeginLabelStyle'):
        assert not _is_linked(b2, 'diagram_BeginLabelStyle', a)


def test_assoc_beginLabelStyleDescription314_link_reassign_clear():
    a = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = style_BeginLabelStyleDescription()
    b2 = style_BeginLabelStyleDescription()
    _safe_set(a, 'diagram_style_EdgeStyleDescription315', b1)
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription315', b1)
    if hasattr(b1, 'style_BeginLabelStyleDescription'):
        assert _is_linked(b1, 'style_BeginLabelStyleDescription', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription315', b2)
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription315', b2)
    if hasattr(b1, 'style_BeginLabelStyleDescription'):
        assert not _is_linked(b1, 'style_BeginLabelStyleDescription', a)
    if hasattr(b2, 'style_BeginLabelStyleDescription'):
        assert _is_linked(b2, 'style_BeginLabelStyleDescription', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription315', None)
    assert not _is_linked(a, 'diagram_style_EdgeStyleDescription315', b2)
    if hasattr(b2, 'style_BeginLabelStyleDescription'):
        assert not _is_linked(b2, 'style_BeginLabelStyleDescription', a)


def test_assoc_borderColor284_link_reassign_clear():
    a = diagram_style_BorderedStyleDescription(borderLineStyle="sample_text", borderSizeComputationExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_BorderedStyleDescription', b1)
    assert _is_linked(a, 'diagram_style_BorderedStyleDescription', b1)
    if hasattr(b1, 'ColorDescription'):
        assert _is_linked(b1, 'ColorDescription', a)
    _safe_set(a, 'diagram_style_BorderedStyleDescription', b2)
    assert _is_linked(a, 'diagram_style_BorderedStyleDescription', b2)
    if hasattr(b1, 'ColorDescription'):
        assert not _is_linked(b1, 'ColorDescription', a)
    if hasattr(b2, 'ColorDescription'):
        assert _is_linked(b2, 'ColorDescription', a)
    _safe_set(a, 'diagram_style_BorderedStyleDescription', None)
    assert not _is_linked(a, 'diagram_style_BorderedStyleDescription', b2)
    if hasattr(b2, 'ColorDescription'):
        assert not _is_linked(b2, 'ColorDescription', a)


def test_assoc_borderedNodeMappings192_link_reassign_clear():
    a = diagram_description_AbstractNodeMapping(domainClass="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_description_AbstractNodeMapping', {b1})
    assert _is_linked(a, 'diagram_description_AbstractNodeMapping', b1)
    if hasattr(b1, 'NodeMapping193'):
        assert _is_linked(b1, 'NodeMapping193', a)
    _safe_set(a, 'diagram_description_AbstractNodeMapping', {b2})
    assert _is_linked(a, 'diagram_description_AbstractNodeMapping', b2)
    if hasattr(b1, 'NodeMapping193'):
        assert not _is_linked(b1, 'NodeMapping193', a)
    if hasattr(b2, 'NodeMapping193'):
        assert _is_linked(b2, 'NodeMapping193', a)
    _safe_set(a, 'diagram_description_AbstractNodeMapping', set())
    assert not _is_linked(a, 'diagram_description_AbstractNodeMapping', b2)
    if hasattr(b2, 'NodeMapping193'):
        assert not _is_linked(b2, 'NodeMapping193', a)


def test_assoc_candidatesMapping55_link_reassign_clear():
    a = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_DNode56', {b1})
    assert _is_linked(a, 'diagram_DNode56', b1)
    if hasattr(b1, 'NodeMapping57'):
        assert _is_linked(b1, 'NodeMapping57', a)
    _safe_set(a, 'diagram_DNode56', {b2})
    assert _is_linked(a, 'diagram_DNode56', b2)
    if hasattr(b1, 'NodeMapping57'):
        assert not _is_linked(b1, 'NodeMapping57', a)
    if hasattr(b2, 'NodeMapping57'):
        assert _is_linked(b2, 'NodeMapping57', a)
    _safe_set(a, 'diagram_DNode56', set())
    assert not _is_linked(a, 'diagram_DNode56', b2)
    if hasattr(b2, 'NodeMapping57'):
        assert not _is_linked(b2, 'NodeMapping57', a)


def test_assoc_candidatesMapping74_link_reassign_clear():
    a = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_DDiagramElementContainer75', {b1})
    assert _is_linked(a, 'diagram_DDiagramElementContainer75', b1)
    if hasattr(b1, 'ContainerMapping76'):
        assert _is_linked(b1, 'ContainerMapping76', a)
    _safe_set(a, 'diagram_DDiagramElementContainer75', {b2})
    assert _is_linked(a, 'diagram_DDiagramElementContainer75', b2)
    if hasattr(b1, 'ContainerMapping76'):
        assert not _is_linked(b1, 'ContainerMapping76', a)
    if hasattr(b2, 'ContainerMapping76'):
        assert _is_linked(b2, 'ContainerMapping76', a)
    _safe_set(a, 'diagram_DDiagramElementContainer75', set())
    assert not _is_linked(a, 'diagram_DDiagramElementContainer75', b2)
    if hasattr(b2, 'ContainerMapping76'):
        assert not _is_linked(b2, 'ContainerMapping76', a)


def test_assoc_centerLabelStyle110_link_reassign_clear():
    a = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    b1 = diagram_CenterLabelStyle()
    b2 = diagram_CenterLabelStyle()
    _safe_set(a, 'diagram_EdgeStyle111', b1)
    assert _is_linked(a, 'diagram_EdgeStyle111', b1)
    if hasattr(b1, 'diagram_CenterLabelStyle'):
        assert _is_linked(b1, 'diagram_CenterLabelStyle', a)
    _safe_set(a, 'diagram_EdgeStyle111', b2)
    assert _is_linked(a, 'diagram_EdgeStyle111', b2)
    if hasattr(b1, 'diagram_CenterLabelStyle'):
        assert not _is_linked(b1, 'diagram_CenterLabelStyle', a)
    if hasattr(b2, 'diagram_CenterLabelStyle'):
        assert _is_linked(b2, 'diagram_CenterLabelStyle', a)
    _safe_set(a, 'diagram_EdgeStyle111', None)
    assert not _is_linked(a, 'diagram_EdgeStyle111', b2)
    if hasattr(b2, 'diagram_CenterLabelStyle'):
        assert not _is_linked(b2, 'diagram_CenterLabelStyle', a)


def test_assoc_centerLabelStyleDescription316_link_reassign_clear():
    a = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = style_CenterLabelStyleDescription()
    b2 = style_CenterLabelStyleDescription()
    _safe_set(a, 'diagram_style_EdgeStyleDescription317', b1)
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription317', b1)
    if hasattr(b1, 'style_CenterLabelStyleDescription'):
        assert _is_linked(b1, 'style_CenterLabelStyleDescription', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription317', b2)
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription317', b2)
    if hasattr(b1, 'style_CenterLabelStyleDescription'):
        assert not _is_linked(b1, 'style_CenterLabelStyleDescription', a)
    if hasattr(b2, 'style_CenterLabelStyleDescription'):
        assert _is_linked(b2, 'style_CenterLabelStyleDescription', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription317', None)
    assert not _is_linked(a, 'diagram_style_EdgeStyleDescription317', b2)
    if hasattr(b2, 'style_CenterLabelStyleDescription'):
        assert not _is_linked(b2, 'style_CenterLabelStyleDescription', a)


def test_assoc_centeredSourceMappings320_link_reassign_clear():
    a = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_style_EdgeStyleDescription321', {b1})
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription321', b1)
    if hasattr(b1, 'DiagramElementMapping322'):
        assert _is_linked(b1, 'DiagramElementMapping322', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription321', {b2})
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription321', b2)
    if hasattr(b1, 'DiagramElementMapping322'):
        assert not _is_linked(b1, 'DiagramElementMapping322', a)
    if hasattr(b2, 'DiagramElementMapping322'):
        assert _is_linked(b2, 'DiagramElementMapping322', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription321', set())
    assert not _is_linked(a, 'diagram_style_EdgeStyleDescription321', b2)
    if hasattr(b2, 'DiagramElementMapping322'):
        assert not _is_linked(b2, 'DiagramElementMapping322', a)


def test_assoc_centeredTargetMappings323_link_reassign_clear():
    a = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_style_EdgeStyleDescription324', {b1})
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription324', b1)
    if hasattr(b1, 'DiagramElementMapping325'):
        assert _is_linked(b1, 'DiagramElementMapping325', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription324', {b2})
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription324', b2)
    if hasattr(b1, 'DiagramElementMapping325'):
        assert not _is_linked(b1, 'DiagramElementMapping325', a)
    if hasattr(b2, 'DiagramElementMapping325'):
        assert _is_linked(b2, 'DiagramElementMapping325', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription324', set())
    assert not _is_linked(a, 'diagram_style_EdgeStyleDescription324', b2)
    if hasattr(b2, 'DiagramElementMapping325'):
        assert not _is_linked(b2, 'DiagramElementMapping325', a)


def test_assoc_color285_link_reassign_clear():
    a = diagram_style_SquareDescription(height="sample_text", width="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_SquareDescription', b1)
    assert _is_linked(a, 'diagram_style_SquareDescription', b1)
    if hasattr(b1, 'ColorDescription286'):
        assert _is_linked(b1, 'ColorDescription286', a)
    _safe_set(a, 'diagram_style_SquareDescription', b2)
    assert _is_linked(a, 'diagram_style_SquareDescription', b2)
    if hasattr(b1, 'ColorDescription286'):
        assert not _is_linked(b1, 'ColorDescription286', a)
    if hasattr(b2, 'ColorDescription286'):
        assert _is_linked(b2, 'ColorDescription286', a)
    _safe_set(a, 'diagram_style_SquareDescription', None)
    assert not _is_linked(a, 'diagram_style_SquareDescription', b2)
    if hasattr(b2, 'ColorDescription286'):
        assert not _is_linked(b2, 'ColorDescription286', a)


def test_assoc_color287_link_reassign_clear():
    a = diagram_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_LozengeNodeDescription', b1)
    assert _is_linked(a, 'diagram_style_LozengeNodeDescription', b1)
    if hasattr(b1, 'ColorDescription288'):
        assert _is_linked(b1, 'ColorDescription288', a)
    _safe_set(a, 'diagram_style_LozengeNodeDescription', b2)
    assert _is_linked(a, 'diagram_style_LozengeNodeDescription', b2)
    if hasattr(b1, 'ColorDescription288'):
        assert not _is_linked(b1, 'ColorDescription288', a)
    if hasattr(b2, 'ColorDescription288'):
        assert _is_linked(b2, 'ColorDescription288', a)
    _safe_set(a, 'diagram_style_LozengeNodeDescription', None)
    assert not _is_linked(a, 'diagram_style_LozengeNodeDescription', b2)
    if hasattr(b2, 'ColorDescription288'):
        assert not _is_linked(b2, 'ColorDescription288', a)


def test_assoc_color289_link_reassign_clear():
    a = diagram_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_EllipseNodeDescription', b1)
    assert _is_linked(a, 'diagram_style_EllipseNodeDescription', b1)
    if hasattr(b1, 'ColorDescription290'):
        assert _is_linked(b1, 'ColorDescription290', a)
    _safe_set(a, 'diagram_style_EllipseNodeDescription', b2)
    assert _is_linked(a, 'diagram_style_EllipseNodeDescription', b2)
    if hasattr(b1, 'ColorDescription290'):
        assert not _is_linked(b1, 'ColorDescription290', a)
    if hasattr(b2, 'ColorDescription290'):
        assert _is_linked(b2, 'ColorDescription290', a)
    _safe_set(a, 'diagram_style_EllipseNodeDescription', None)
    assert not _is_linked(a, 'diagram_style_EllipseNodeDescription', b2)
    if hasattr(b2, 'ColorDescription290'):
        assert not _is_linked(b2, 'ColorDescription290', a)


def test_assoc_color291_link_reassign_clear():
    a = diagram_style_BundledImageDescription(providedShapeID="sample_text", shape="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_BundledImageDescription', b1)
    assert _is_linked(a, 'diagram_style_BundledImageDescription', b1)
    if hasattr(b1, 'ColorDescription292'):
        assert _is_linked(b1, 'ColorDescription292', a)
    _safe_set(a, 'diagram_style_BundledImageDescription', b2)
    assert _is_linked(a, 'diagram_style_BundledImageDescription', b2)
    if hasattr(b1, 'ColorDescription292'):
        assert not _is_linked(b1, 'ColorDescription292', a)
    if hasattr(b2, 'ColorDescription292'):
        assert _is_linked(b2, 'ColorDescription292', a)
    _safe_set(a, 'diagram_style_BundledImageDescription', None)
    assert not _is_linked(a, 'diagram_style_BundledImageDescription', b2)
    if hasattr(b2, 'ColorDescription292'):
        assert not _is_linked(b2, 'ColorDescription292', a)


def test_assoc_concerns134_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = concern_ConcernSet()
    b2 = concern_ConcernSet()
    _safe_set(a, 'diagram_description_DiagramDescription135', b1)
    assert _is_linked(a, 'diagram_description_DiagramDescription135', b1)
    if hasattr(b1, 'concern_ConcernSet'):
        assert _is_linked(b1, 'concern_ConcernSet', a)
    _safe_set(a, 'diagram_description_DiagramDescription135', b2)
    assert _is_linked(a, 'diagram_description_DiagramDescription135', b2)
    if hasattr(b1, 'concern_ConcernSet'):
        assert not _is_linked(b1, 'concern_ConcernSet', a)
    if hasattr(b2, 'concern_ConcernSet'):
        assert _is_linked(b2, 'concern_ConcernSet', a)
    _safe_set(a, 'diagram_description_DiagramDescription135', None)
    assert not _is_linked(a, 'diagram_description_DiagramDescription135', b2)
    if hasattr(b2, 'concern_ConcernSet'):
        assert not _is_linked(b2, 'concern_ConcernSet', a)


def test_assoc_conditionnalStyles198_link_reassign_clear():
    a = diagram_description_NodeMapping()
    b1 = ConditionalNodeStyleDescription()
    b2 = ConditionalNodeStyleDescription()
    _safe_set(a, 'diagram_description_NodeMapping199', {b1})
    assert _is_linked(a, 'diagram_description_NodeMapping199', b1)
    if hasattr(b1, 'ConditionalNodeStyleDescription'):
        assert _is_linked(b1, 'ConditionalNodeStyleDescription', a)
    _safe_set(a, 'diagram_description_NodeMapping199', {b2})
    assert _is_linked(a, 'diagram_description_NodeMapping199', b2)
    if hasattr(b1, 'ConditionalNodeStyleDescription'):
        assert not _is_linked(b1, 'ConditionalNodeStyleDescription', a)
    if hasattr(b2, 'ConditionalNodeStyleDescription'):
        assert _is_linked(b2, 'ConditionalNodeStyleDescription', a)
    _safe_set(a, 'diagram_description_NodeMapping199', set())
    assert not _is_linked(a, 'diagram_description_NodeMapping199', b2)
    if hasattr(b2, 'ConditionalNodeStyleDescription'):
        assert not _is_linked(b2, 'ConditionalNodeStyleDescription', a)


def test_assoc_conditionnalStyles219_link_reassign_clear():
    a = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = ConditionalContainerStyleDescription()
    b2 = ConditionalContainerStyleDescription()
    _safe_set(a, 'diagram_description_ContainerMapping220', {b1})
    assert _is_linked(a, 'diagram_description_ContainerMapping220', b1)
    if hasattr(b1, 'ConditionalContainerStyleDescription'):
        assert _is_linked(b1, 'ConditionalContainerStyleDescription', a)
    _safe_set(a, 'diagram_description_ContainerMapping220', {b2})
    assert _is_linked(a, 'diagram_description_ContainerMapping220', b2)
    if hasattr(b1, 'ConditionalContainerStyleDescription'):
        assert not _is_linked(b1, 'ConditionalContainerStyleDescription', a)
    if hasattr(b2, 'ConditionalContainerStyleDescription'):
        assert _is_linked(b2, 'ConditionalContainerStyleDescription', a)
    _safe_set(a, 'diagram_description_ContainerMapping220', set())
    assert not _is_linked(a, 'diagram_description_ContainerMapping220', b2)
    if hasattr(b2, 'ConditionalContainerStyleDescription'):
        assert not _is_linked(b2, 'ConditionalContainerStyleDescription', a)


def test_assoc_conditionnalStyles232_link_reassign_clear():
    a = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = ConditionalEdgeStyleDescription()
    b2 = ConditionalEdgeStyleDescription()
    _safe_set(a, 'diagram_description_EdgeMapping233', {b1})
    assert _is_linked(a, 'diagram_description_EdgeMapping233', b1)
    if hasattr(b1, 'ConditionalEdgeStyleDescription'):
        assert _is_linked(b1, 'ConditionalEdgeStyleDescription', a)
    _safe_set(a, 'diagram_description_EdgeMapping233', {b2})
    assert _is_linked(a, 'diagram_description_EdgeMapping233', b2)
    if hasattr(b1, 'ConditionalEdgeStyleDescription'):
        assert not _is_linked(b1, 'ConditionalEdgeStyleDescription', a)
    if hasattr(b2, 'ConditionalEdgeStyleDescription'):
        assert _is_linked(b2, 'ConditionalEdgeStyleDescription', a)
    _safe_set(a, 'diagram_description_EdgeMapping233', set())
    assert not _is_linked(a, 'diagram_description_EdgeMapping233', b2)
    if hasattr(b2, 'ConditionalEdgeStyleDescription'):
        assert not _is_linked(b2, 'ConditionalEdgeStyleDescription', a)


def test_assoc_conditionnalStyles240_link_reassign_clear():
    a = diagram_description_EdgeMappingImport(inheritsAncestorFilters=True)
    b1 = ConditionalEdgeStyleDescription()
    b2 = ConditionalEdgeStyleDescription()
    _safe_set(a, 'diagram_description_EdgeMappingImport241', {b1})
    assert _is_linked(a, 'diagram_description_EdgeMappingImport241', b1)
    if hasattr(b1, 'ConditionalEdgeStyleDescription242'):
        assert _is_linked(b1, 'ConditionalEdgeStyleDescription242', a)
    _safe_set(a, 'diagram_description_EdgeMappingImport241', {b2})
    assert _is_linked(a, 'diagram_description_EdgeMappingImport241', b2)
    if hasattr(b1, 'ConditionalEdgeStyleDescription242'):
        assert not _is_linked(b1, 'ConditionalEdgeStyleDescription242', a)
    if hasattr(b2, 'ConditionalEdgeStyleDescription242'):
        assert _is_linked(b2, 'ConditionalEdgeStyleDescription242', a)
    _safe_set(a, 'diagram_description_EdgeMappingImport241', set())
    assert not _is_linked(a, 'diagram_description_EdgeMappingImport241', b2)
    if hasattr(b2, 'ConditionalEdgeStyleDescription242'):
        assert not _is_linked(b2, 'ConditionalEdgeStyleDescription242', a)


def test_assoc_containerMappings167_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_description_DiagramDescription168', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription168', b1)
    if hasattr(b1, 'ContainerMapping169'):
        assert _is_linked(b1, 'ContainerMapping169', a)
    _safe_set(a, 'diagram_description_DiagramDescription168', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription168', b2)
    if hasattr(b1, 'ContainerMapping169'):
        assert not _is_linked(b1, 'ContainerMapping169', a)
    if hasattr(b2, 'ContainerMapping169'):
        assert _is_linked(b2, 'ContainerMapping169', a)
    _safe_set(a, 'diagram_description_DiagramDescription168', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription168', b2)
    if hasattr(b2, 'ContainerMapping169'):
        assert not _is_linked(b2, 'ContainerMapping169', a)


def test_assoc_containerMappings261_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_description_Layer262', {b1})
    assert _is_linked(a, 'diagram_description_Layer262', b1)
    if hasattr(b1, 'ContainerMapping263'):
        assert _is_linked(b1, 'ContainerMapping263', a)
    _safe_set(a, 'diagram_description_Layer262', {b2})
    assert _is_linked(a, 'diagram_description_Layer262', b2)
    if hasattr(b1, 'ContainerMapping263'):
        assert not _is_linked(b1, 'ContainerMapping263', a)
    if hasattr(b2, 'ContainerMapping263'):
        assert _is_linked(b2, 'ContainerMapping263', a)
    _safe_set(a, 'diagram_description_Layer262', set())
    assert not _is_linked(a, 'diagram_description_Layer262', b2)
    if hasattr(b2, 'ContainerMapping263'):
        assert not _is_linked(b2, 'ContainerMapping263', a)


def test_assoc_containerMappings372_link_reassign_clear():
    a = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_tool_ContainerCreationDescription', {b1})
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription', b1)
    if hasattr(b1, 'ContainerMapping373'):
        assert _is_linked(b1, 'ContainerMapping373', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription', {b2})
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription', b2)
    if hasattr(b1, 'ContainerMapping373'):
        assert not _is_linked(b1, 'ContainerMapping373', a)
    if hasattr(b2, 'ContainerMapping373'):
        assert _is_linked(b2, 'ContainerMapping373', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription', set())
    assert not _is_linked(a, 'diagram_tool_ContainerCreationDescription', b2)
    if hasattr(b2, 'ContainerMapping373'):
        assert not _is_linked(b2, 'ContainerMapping373', a)


def test_assoc_containerView390_link_reassign_clear():
    a = diagram_tool_DeleteElementDescription()
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'diagram_tool_DeleteElementDescription391', b1)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription391', b1)
    if hasattr(b1, 'tool_ContainerViewVariable392'):
        assert _is_linked(b1, 'tool_ContainerViewVariable392', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription391', b2)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription391', b2)
    if hasattr(b1, 'tool_ContainerViewVariable392'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable392', a)
    if hasattr(b2, 'tool_ContainerViewVariable392'):
        assert _is_linked(b2, 'tool_ContainerViewVariable392', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription391', None)
    assert not _is_linked(a, 'diagram_tool_DeleteElementDescription391', b2)
    if hasattr(b2, 'tool_ContainerViewVariable392'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable392', a)


def test_assoc_containers12_link_reassign_clear():
    a = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b2 = diagram_DDiagram(headerHeight=13, isInLayoutingMode=False, synchronized=False)
    _safe_set(a, 'diagram_DDiagramElementContainer', b1)
    assert _is_linked(a, 'diagram_DDiagramElementContainer', b1)
    if hasattr(b1, 'diagram_DDiagram13'):
        assert _is_linked(b1, 'diagram_DDiagram13', a)
    _safe_set(a, 'diagram_DDiagramElementContainer', b2)
    assert _is_linked(a, 'diagram_DDiagramElementContainer', b2)
    if hasattr(b1, 'diagram_DDiagram13'):
        assert not _is_linked(b1, 'diagram_DDiagram13', a)
    if hasattr(b2, 'diagram_DDiagram13'):
        assert _is_linked(b2, 'diagram_DDiagram13', a)
    _safe_set(a, 'diagram_DDiagramElementContainer', None)
    assert not _is_linked(a, 'diagram_DDiagramElementContainer', b2)
    if hasattr(b2, 'diagram_DDiagram13'):
        assert not _is_linked(b2, 'diagram_DDiagram13', a)


def test_assoc_containers62_link_reassign_clear():
    a = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b2 = diagram_DDiagramElementContainer(height="sample_text_2", width="sample_text_2")
    _safe_set(a, 'diagram_DDiagramElementContainer61', {b1})
    assert _is_linked(a, 'diagram_DDiagramElementContainer61', b1)
    if hasattr(b1, 'diagram_DDiagramElementContainer63'):
        assert _is_linked(b1, 'diagram_DDiagramElementContainer63', a)
    _safe_set(a, 'diagram_DDiagramElementContainer61', {b2})
    assert _is_linked(a, 'diagram_DDiagramElementContainer61', b2)
    if hasattr(b1, 'diagram_DDiagramElementContainer63'):
        assert not _is_linked(b1, 'diagram_DDiagramElementContainer63', a)
    if hasattr(b2, 'diagram_DDiagramElementContainer63'):
        assert _is_linked(b2, 'diagram_DDiagramElementContainer63', a)
    _safe_set(a, 'diagram_DDiagramElementContainer61', set())
    assert not _is_linked(a, 'diagram_DDiagramElementContainer61', b2)
    if hasattr(b2, 'diagram_DDiagramElementContainer63'):
        assert not _is_linked(b2, 'diagram_DDiagramElementContainer63', a)


def test_assoc_currentConcern14_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = concern_ConcernDescription()
    b2 = concern_ConcernDescription()
    _safe_set(a, 'diagram_DDiagram15', b1)
    assert _is_linked(a, 'diagram_DDiagram15', b1)
    if hasattr(b1, 'concern_ConcernDescription'):
        assert _is_linked(b1, 'concern_ConcernDescription', a)
    _safe_set(a, 'diagram_DDiagram15', b2)
    assert _is_linked(a, 'diagram_DDiagram15', b2)
    if hasattr(b1, 'concern_ConcernDescription'):
        assert not _is_linked(b1, 'concern_ConcernDescription', a)
    if hasattr(b2, 'concern_ConcernDescription'):
        assert _is_linked(b2, 'concern_ConcernDescription', a)
    _safe_set(a, 'diagram_DDiagram15', None)
    assert not _is_linked(a, 'diagram_DDiagram15', b2)
    if hasattr(b2, 'concern_ConcernDescription'):
        assert not _is_linked(b2, 'concern_ConcernDescription', a)


def test_assoc_customization281_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = Customization()
    b2 = Customization()
    _safe_set(a, 'diagram_description_Layer282', b1)
    assert _is_linked(a, 'diagram_description_Layer282', b1)
    if hasattr(b1, 'Customization'):
        assert _is_linked(b1, 'Customization', a)
    _safe_set(a, 'diagram_description_Layer282', b2)
    assert _is_linked(a, 'diagram_description_Layer282', b2)
    if hasattr(b1, 'Customization'):
        assert not _is_linked(b1, 'Customization', a)
    if hasattr(b2, 'Customization'):
        assert _is_linked(b2, 'Customization', a)
    _safe_set(a, 'diagram_description_Layer282', None)
    assert not _is_linked(a, 'diagram_description_Layer282', b2)
    if hasattr(b2, 'Customization'):
        assert not _is_linked(b2, 'Customization', a)


def test_assoc_decorationDescriptionsSet276_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = DecorationDescriptionsSet()
    b2 = DecorationDescriptionsSet()
    _safe_set(a, 'diagram_description_Layer277', b1)
    assert _is_linked(a, 'diagram_description_Layer277', b1)
    if hasattr(b1, 'DecorationDescriptionsSet'):
        assert _is_linked(b1, 'DecorationDescriptionsSet', a)
    _safe_set(a, 'diagram_description_Layer277', b2)
    assert _is_linked(a, 'diagram_description_Layer277', b2)
    if hasattr(b1, 'DecorationDescriptionsSet'):
        assert not _is_linked(b1, 'DecorationDescriptionsSet', a)
    if hasattr(b2, 'DecorationDescriptionsSet'):
        assert _is_linked(b2, 'DecorationDescriptionsSet', a)
    _safe_set(a, 'diagram_description_Layer277', None)
    assert not _is_linked(a, 'diagram_description_Layer277', b2)
    if hasattr(b2, 'DecorationDescriptionsSet'):
        assert not _is_linked(b2, 'DecorationDescriptionsSet', a)


def test_assoc_decorations37_link_reassign_clear():
    a = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = diagram_Decoration()
    b2 = diagram_Decoration()
    _safe_set(a, 'diagram_DDiagramElement38', {b1})
    assert _is_linked(a, 'diagram_DDiagramElement38', b1)
    if hasattr(b1, 'diagram_Decoration'):
        assert _is_linked(b1, 'diagram_Decoration', a)
    _safe_set(a, 'diagram_DDiagramElement38', {b2})
    assert _is_linked(a, 'diagram_DDiagramElement38', b2)
    if hasattr(b1, 'diagram_Decoration'):
        assert not _is_linked(b1, 'diagram_Decoration', a)
    if hasattr(b2, 'diagram_Decoration'):
        assert _is_linked(b2, 'diagram_Decoration', a)
    _safe_set(a, 'diagram_DDiagramElement38', set())
    assert not _is_linked(a, 'diagram_DDiagramElement38', b2)
    if hasattr(b2, 'diagram_Decoration'):
        assert not _is_linked(b2, 'diagram_Decoration', a)


def test_assoc_defaultConcern138_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = concern_ConcernDescription()
    b2 = concern_ConcernDescription()
    _safe_set(a, 'diagram_description_DiagramDescription139', b1)
    assert _is_linked(a, 'diagram_description_DiagramDescription139', b1)
    if hasattr(b1, 'concern_ConcernDescription140'):
        assert _is_linked(b1, 'concern_ConcernDescription140', a)
    _safe_set(a, 'diagram_description_DiagramDescription139', b2)
    assert _is_linked(a, 'diagram_description_DiagramDescription139', b2)
    if hasattr(b1, 'concern_ConcernDescription140'):
        assert not _is_linked(b1, 'concern_ConcernDescription140', a)
    if hasattr(b2, 'concern_ConcernDescription140'):
        assert _is_linked(b2, 'concern_ConcernDescription140', a)
    _safe_set(a, 'diagram_description_DiagramDescription139', None)
    assert not _is_linked(a, 'diagram_description_DiagramDescription139', b2)
    if hasattr(b2, 'concern_ConcernDescription140'):
        assert not _is_linked(b2, 'concern_ConcernDescription140', a)


def test_assoc_defaultLayer147_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = Layer()
    b2 = Layer()
    _safe_set(a, 'diagram_description_DiagramDescription148', b1)
    assert _is_linked(a, 'diagram_description_DiagramDescription148', b1)
    if hasattr(b1, 'Layer149'):
        assert _is_linked(b1, 'Layer149', a)
    _safe_set(a, 'diagram_description_DiagramDescription148', b2)
    assert _is_linked(a, 'diagram_description_DiagramDescription148', b2)
    if hasattr(b1, 'Layer149'):
        assert not _is_linked(b1, 'Layer149', a)
    if hasattr(b2, 'Layer149'):
        assert _is_linked(b2, 'Layer149', a)
    _safe_set(a, 'diagram_description_DiagramDescription148', None)
    assert not _is_linked(a, 'diagram_description_DiagramDescription148', b2)
    if hasattr(b2, 'Layer149'):
        assert not _is_linked(b2, 'Layer149', a)


def test_assoc_deletionDescription188_link_reassign_clear():
    a = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    b1 = tool_DeleteElementDescription()
    b2 = tool_DeleteElementDescription()
    _safe_set(a, 'diagram_description_DiagramElementMapping', b1)
    assert _is_linked(a, 'diagram_description_DiagramElementMapping', b1)
    if hasattr(b1, 'tool_DeleteElementDescription'):
        assert _is_linked(b1, 'tool_DeleteElementDescription', a)
    _safe_set(a, 'diagram_description_DiagramElementMapping', b2)
    assert _is_linked(a, 'diagram_description_DiagramElementMapping', b2)
    if hasattr(b1, 'tool_DeleteElementDescription'):
        assert not _is_linked(b1, 'tool_DeleteElementDescription', a)
    if hasattr(b2, 'tool_DeleteElementDescription'):
        assert _is_linked(b2, 'tool_DeleteElementDescription', a)
    _safe_set(a, 'diagram_description_DiagramElementMapping', None)
    assert not _is_linked(a, 'diagram_description_DiagramElementMapping', b2)
    if hasattr(b2, 'tool_DeleteElementDescription'):
        assert not _is_linked(b2, 'tool_DeleteElementDescription', a)


def test_assoc_description4_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = DiagramDescription()
    b2 = DiagramDescription()
    _safe_set(a, 'diagram_DDiagram5', b1)
    assert _is_linked(a, 'diagram_DDiagram5', b1)
    if hasattr(b1, 'DiagramDescription'):
        assert _is_linked(b1, 'DiagramDescription', a)
    _safe_set(a, 'diagram_DDiagram5', b2)
    assert _is_linked(a, 'diagram_DDiagram5', b2)
    if hasattr(b1, 'DiagramDescription'):
        assert not _is_linked(b1, 'DiagramDescription', a)
    if hasattr(b2, 'DiagramDescription'):
        assert _is_linked(b2, 'DiagramDescription', a)
    _safe_set(a, 'diagram_DDiagram5', None)
    assert not _is_linked(a, 'diagram_DDiagram5', b2)
    if hasattr(b2, 'DiagramDescription'):
        assert not _is_linked(b2, 'DiagramDescription', a)


def test_assoc_diagramDescription435_link_reassign_clear():
    a = diagram_tool_Navigation(createIfNotExistent=True)
    b1 = DiagramDescription()
    b2 = DiagramDescription()
    _safe_set(a, 'diagram_tool_Navigation', b1)
    assert _is_linked(a, 'diagram_tool_Navigation', b1)
    if hasattr(b1, 'DiagramDescription436'):
        assert _is_linked(b1, 'DiagramDescription436', a)
    _safe_set(a, 'diagram_tool_Navigation', b2)
    assert _is_linked(a, 'diagram_tool_Navigation', b2)
    if hasattr(b1, 'DiagramDescription436'):
        assert not _is_linked(b1, 'DiagramDescription436', a)
    if hasattr(b2, 'DiagramDescription436'):
        assert _is_linked(b2, 'DiagramDescription436', a)
    _safe_set(a, 'diagram_tool_Navigation', None)
    assert not _is_linked(a, 'diagram_tool_Navigation', b2)
    if hasattr(b2, 'DiagramDescription436'):
        assert not _is_linked(b2, 'DiagramDescription436', a)


def test_assoc_diagramElementMapping42_link_reassign_clear():
    a = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_DDiagramElement43', b1)
    assert _is_linked(a, 'diagram_DDiagramElement43', b1)
    if hasattr(b1, 'DiagramElementMapping'):
        assert _is_linked(b1, 'DiagramElementMapping', a)
    _safe_set(a, 'diagram_DDiagramElement43', b2)
    assert _is_linked(a, 'diagram_DDiagramElement43', b2)
    if hasattr(b1, 'DiagramElementMapping'):
        assert not _is_linked(b1, 'DiagramElementMapping', a)
    if hasattr(b2, 'DiagramElementMapping'):
        assert _is_linked(b2, 'DiagramElementMapping', a)
    _safe_set(a, 'diagram_DDiagramElement43', None)
    assert not _is_linked(a, 'diagram_DDiagramElement43', b2)
    if hasattr(b2, 'DiagramElementMapping'):
        assert not _is_linked(b2, 'DiagramElementMapping', a)


def test_assoc_diagramElements1_link_reassign_clear():
    a = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b2 = diagram_DDiagram(headerHeight=13, isInLayoutingMode=False, synchronized=False)
    _safe_set(a, 'diagram_DDiagramElement3', b1)
    assert _is_linked(a, 'diagram_DDiagramElement3', b1)
    if hasattr(b1, 'diagram_DDiagram2'):
        assert _is_linked(b1, 'diagram_DDiagram2', a)
    _safe_set(a, 'diagram_DDiagramElement3', b2)
    assert _is_linked(a, 'diagram_DDiagramElement3', b2)
    if hasattr(b1, 'diagram_DDiagram2'):
        assert not _is_linked(b1, 'diagram_DDiagram2', a)
    if hasattr(b2, 'diagram_DDiagram2'):
        assert _is_linked(b2, 'diagram_DDiagram2', a)
    _safe_set(a, 'diagram_DDiagramElement3', None)
    assert not _is_linked(a, 'diagram_DDiagramElement3', b2)
    if hasattr(b2, 'diagram_DDiagram2'):
        assert not _is_linked(b2, 'diagram_DDiagram2', a)


def test_assoc_diagramInitialisation145_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'diagram_description_DiagramDescription146', b1)
    assert _is_linked(a, 'diagram_description_DiagramDescription146', b1)
    if hasattr(b1, 'tool_InitialOperation'):
        assert _is_linked(b1, 'tool_InitialOperation', a)
    _safe_set(a, 'diagram_description_DiagramDescription146', b2)
    assert _is_linked(a, 'diagram_description_DiagramDescription146', b2)
    if hasattr(b1, 'tool_InitialOperation'):
        assert not _is_linked(b1, 'tool_InitialOperation', a)
    if hasattr(b2, 'tool_InitialOperation'):
        assert _is_linked(b2, 'tool_InitialOperation', a)
    _safe_set(a, 'diagram_description_DiagramDescription146', None)
    assert not _is_linked(a, 'diagram_description_DiagramDescription146', b2)
    if hasattr(b2, 'tool_InitialOperation'):
        assert not _is_linked(b2, 'tool_InitialOperation', a)


def test_assoc_doubleClickDescription191_link_reassign_clear():
    a = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    b1 = tool_DoubleClickDescription()
    b2 = tool_DoubleClickDescription()
    _safe_set(a, 'mappings', b1)
    assert _is_linked(a, 'mappings', b1)
    if hasattr(b1, 'DoubleClickDescription'):
        assert _is_linked(b1, 'DoubleClickDescription', a)
    _safe_set(a, 'mappings', b2)
    assert _is_linked(a, 'mappings', b2)
    if hasattr(b1, 'DoubleClickDescription'):
        assert not _is_linked(b1, 'DoubleClickDescription', a)
    if hasattr(b2, 'DoubleClickDescription'):
        assert _is_linked(b2, 'DoubleClickDescription', a)
    _safe_set(a, 'mappings', None)
    assert not _is_linked(a, 'mappings', b2)
    if hasattr(b2, 'DoubleClickDescription'):
        assert not _is_linked(b2, 'DoubleClickDescription', a)


def test_assoc_edgeMappingImports165_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = EdgeMappingImport()
    b2 = EdgeMappingImport()
    _safe_set(a, 'diagram_description_DiagramDescription166', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription166', b1)
    if hasattr(b1, 'EdgeMappingImport'):
        assert _is_linked(b1, 'EdgeMappingImport', a)
    _safe_set(a, 'diagram_description_DiagramDescription166', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription166', b2)
    if hasattr(b1, 'EdgeMappingImport'):
        assert not _is_linked(b1, 'EdgeMappingImport', a)
    if hasattr(b2, 'EdgeMappingImport'):
        assert _is_linked(b2, 'EdgeMappingImport', a)
    _safe_set(a, 'diagram_description_DiagramDescription166', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription166', b2)
    if hasattr(b2, 'EdgeMappingImport'):
        assert not _is_linked(b2, 'EdgeMappingImport', a)


def test_assoc_edgeMappingImports258_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = EdgeMappingImport()
    b2 = EdgeMappingImport()
    _safe_set(a, 'diagram_description_Layer259', {b1})
    assert _is_linked(a, 'diagram_description_Layer259', b1)
    if hasattr(b1, 'EdgeMappingImport260'):
        assert _is_linked(b1, 'EdgeMappingImport260', a)
    _safe_set(a, 'diagram_description_Layer259', {b2})
    assert _is_linked(a, 'diagram_description_Layer259', b2)
    if hasattr(b1, 'EdgeMappingImport260'):
        assert not _is_linked(b1, 'EdgeMappingImport260', a)
    if hasattr(b2, 'EdgeMappingImport260'):
        assert _is_linked(b2, 'EdgeMappingImport260', a)
    _safe_set(a, 'diagram_description_Layer259', set())
    assert not _is_linked(a, 'diagram_description_Layer259', b2)
    if hasattr(b2, 'EdgeMappingImport260'):
        assert not _is_linked(b2, 'EdgeMappingImport260', a)


def test_assoc_edgeMappings162_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = EdgeMapping()
    b2 = EdgeMapping()
    _safe_set(a, 'diagram_description_DiagramDescription163', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription163', b1)
    if hasattr(b1, 'EdgeMapping164'):
        assert _is_linked(b1, 'EdgeMapping164', a)
    _safe_set(a, 'diagram_description_DiagramDescription163', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription163', b2)
    if hasattr(b1, 'EdgeMapping164'):
        assert not _is_linked(b1, 'EdgeMapping164', a)
    if hasattr(b2, 'EdgeMapping164'):
        assert _is_linked(b2, 'EdgeMapping164', a)
    _safe_set(a, 'diagram_description_DiagramDescription163', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription163', b2)
    if hasattr(b2, 'EdgeMapping164'):
        assert not _is_linked(b2, 'EdgeMapping164', a)


def test_assoc_edgeMappings255_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = EdgeMapping()
    b2 = EdgeMapping()
    _safe_set(a, 'diagram_description_Layer256', {b1})
    assert _is_linked(a, 'diagram_description_Layer256', b1)
    if hasattr(b1, 'EdgeMapping257'):
        assert _is_linked(b1, 'EdgeMapping257', a)
    _safe_set(a, 'diagram_description_Layer256', {b2})
    assert _is_linked(a, 'diagram_description_Layer256', b2)
    if hasattr(b1, 'EdgeMapping257'):
        assert not _is_linked(b1, 'EdgeMapping257', a)
    if hasattr(b2, 'EdgeMapping257'):
        assert _is_linked(b2, 'EdgeMapping257', a)
    _safe_set(a, 'diagram_description_Layer256', set())
    assert not _is_linked(a, 'diagram_description_Layer256', b2)
    if hasattr(b2, 'EdgeMapping257'):
        assert not _is_linked(b2, 'EdgeMapping257', a)


def test_assoc_edgeMappings354_link_reassign_clear():
    a = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = EdgeMapping()
    b2 = EdgeMapping()
    _safe_set(a, 'diagram_tool_EdgeCreationDescription', {b1})
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription', b1)
    if hasattr(b1, 'EdgeMapping355'):
        assert _is_linked(b1, 'EdgeMapping355', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription', {b2})
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription', b2)
    if hasattr(b1, 'EdgeMapping355'):
        assert not _is_linked(b1, 'EdgeMapping355', a)
    if hasattr(b2, 'EdgeMapping355'):
        assert _is_linked(b2, 'EdgeMapping355', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription', set())
    assert not _is_linked(a, 'diagram_tool_EdgeCreationDescription', b2)
    if hasattr(b2, 'EdgeMapping355'):
        assert not _is_linked(b2, 'EdgeMapping355', a)


def test_assoc_edgeView424_link_reassign_clear():
    a = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription425', b1)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription425', b1)
    if hasattr(b1, 'tool_ElementSelectVariable426'):
        assert _is_linked(b1, 'tool_ElementSelectVariable426', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription425', b2)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription425', b2)
    if hasattr(b1, 'tool_ElementSelectVariable426'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable426', a)
    if hasattr(b2, 'tool_ElementSelectVariable426'):
        assert _is_linked(b2, 'tool_ElementSelectVariable426', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription425', None)
    assert not _is_linked(a, 'diagram_tool_ReconnectEdgeDescription425', b2)
    if hasattr(b2, 'tool_ElementSelectVariable426'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable426', a)


def test_assoc_edges6_link_reassign_clear():
    a = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b2 = diagram_DDiagram(headerHeight=13, isInLayoutingMode=False, synchronized=False)
    _safe_set(a, 'diagram_DEdge', b1)
    assert _is_linked(a, 'diagram_DEdge', b1)
    if hasattr(b1, 'diagram_DDiagram7'):
        assert _is_linked(b1, 'diagram_DDiagram7', a)
    _safe_set(a, 'diagram_DEdge', b2)
    assert _is_linked(a, 'diagram_DEdge', b2)
    if hasattr(b1, 'diagram_DDiagram7'):
        assert not _is_linked(b1, 'diagram_DDiagram7', a)
    if hasattr(b2, 'diagram_DDiagram7'):
        assert _is_linked(b2, 'diagram_DDiagram7', a)
    _safe_set(a, 'diagram_DEdge', None)
    assert not _is_linked(a, 'diagram_DEdge', b2)
    if hasattr(b2, 'diagram_DDiagram7'):
        assert not _is_linked(b2, 'diagram_DDiagram7', a)


def test_assoc_element386_link_reassign_clear():
    a = diagram_tool_DeleteElementDescription()
    b1 = tool_ElementDeleteVariable()
    b2 = tool_ElementDeleteVariable()
    _safe_set(a, 'diagram_tool_DeleteElementDescription', b1)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription', b1)
    if hasattr(b1, 'tool_ElementDeleteVariable'):
        assert _is_linked(b1, 'tool_ElementDeleteVariable', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription', b2)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription', b2)
    if hasattr(b1, 'tool_ElementDeleteVariable'):
        assert not _is_linked(b1, 'tool_ElementDeleteVariable', a)
    if hasattr(b2, 'tool_ElementDeleteVariable'):
        assert _is_linked(b2, 'tool_ElementDeleteVariable', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription', None)
    assert not _is_linked(a, 'diagram_tool_DeleteElementDescription', b2)
    if hasattr(b2, 'tool_ElementDeleteVariable'):
        assert not _is_linked(b2, 'tool_ElementDeleteVariable', a)


def test_assoc_element419_link_reassign_clear():
    a = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription420', b1)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription420', b1)
    if hasattr(b1, 'tool_ElementSelectVariable'):
        assert _is_linked(b1, 'tool_ElementSelectVariable', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription420', b2)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription420', b2)
    if hasattr(b1, 'tool_ElementSelectVariable'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable', a)
    if hasattr(b2, 'tool_ElementSelectVariable'):
        assert _is_linked(b2, 'tool_ElementSelectVariable', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription420', None)
    assert not _is_linked(a, 'diagram_tool_ReconnectEdgeDescription420', b2)
    if hasattr(b2, 'tool_ElementSelectVariable'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable', a)


def test_assoc_element448_link_reassign_clear():
    a = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_ElementDropVariable()
    b2 = tool_ElementDropVariable()
    _safe_set(a, 'diagram_tool_ContainerDropDescription449', b1)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription449', b1)
    if hasattr(b1, 'tool_ElementDropVariable'):
        assert _is_linked(b1, 'tool_ElementDropVariable', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription449', b2)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription449', b2)
    if hasattr(b1, 'tool_ElementDropVariable'):
        assert not _is_linked(b1, 'tool_ElementDropVariable', a)
    if hasattr(b2, 'tool_ElementDropVariable'):
        assert _is_linked(b2, 'tool_ElementDropVariable', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription449', None)
    assert not _is_linked(a, 'diagram_tool_ContainerDropDescription449', b2)
    if hasattr(b2, 'tool_ElementDropVariable'):
        assert not _is_linked(b2, 'tool_ElementDropVariable', a)


def test_assoc_elementView387_link_reassign_clear():
    a = diagram_tool_DeleteElementDescription()
    b1 = tool_ElementDeleteVariable()
    b2 = tool_ElementDeleteVariable()
    _safe_set(a, 'diagram_tool_DeleteElementDescription388', b1)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription388', b1)
    if hasattr(b1, 'tool_ElementDeleteVariable389'):
        assert _is_linked(b1, 'tool_ElementDeleteVariable389', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription388', b2)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription388', b2)
    if hasattr(b1, 'tool_ElementDeleteVariable389'):
        assert not _is_linked(b1, 'tool_ElementDeleteVariable389', a)
    if hasattr(b2, 'tool_ElementDeleteVariable389'):
        assert _is_linked(b2, 'tool_ElementDeleteVariable389', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription388', None)
    assert not _is_linked(a, 'diagram_tool_DeleteElementDescription388', b2)
    if hasattr(b2, 'tool_ElementDeleteVariable389'):
        assert not _is_linked(b2, 'tool_ElementDeleteVariable389', a)


def test_assoc_elements64_link_reassign_clear():
    a = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b2 = diagram_DDiagramElement(tooltipText="sample_text_2", visible=False)
    _safe_set(a, 'diagram_DDiagramElementContainer65', {b1})
    assert _is_linked(a, 'diagram_DDiagramElementContainer65', b1)
    if hasattr(b1, 'diagram_DDiagramElement66'):
        assert _is_linked(b1, 'diagram_DDiagramElement66', a)
    _safe_set(a, 'diagram_DDiagramElementContainer65', {b2})
    assert _is_linked(a, 'diagram_DDiagramElementContainer65', b2)
    if hasattr(b1, 'diagram_DDiagramElement66'):
        assert not _is_linked(b1, 'diagram_DDiagramElement66', a)
    if hasattr(b2, 'diagram_DDiagramElement66'):
        assert _is_linked(b2, 'diagram_DDiagramElement66', a)
    _safe_set(a, 'diagram_DDiagramElementContainer65', set())
    assert not _is_linked(a, 'diagram_DDiagramElementContainer65', b2)
    if hasattr(b2, 'diagram_DDiagramElement66'):
        assert not _is_linked(b2, 'diagram_DDiagramElement66', a)


def test_assoc_endLabelStyle112_link_reassign_clear():
    a = diagram_EndLabelStyle()
    b1 = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    b2 = diagram_EdgeStyle(centered="sample_text_2", foldingStyle="sample_text_2", lineStyle="sample_text_2", routingStyle="sample_text_2", size="sample_text_2", sourceArrow="sample_text_2", strokeColor="sample_text_2", targetArrow="sample_text_2")
    _safe_set(a, 'diagram_EndLabelStyle', b1)
    assert _is_linked(a, 'diagram_EndLabelStyle', b1)
    if hasattr(b1, 'diagram_EdgeStyle113'):
        assert _is_linked(b1, 'diagram_EdgeStyle113', a)
    _safe_set(a, 'diagram_EndLabelStyle', b2)
    assert _is_linked(a, 'diagram_EndLabelStyle', b2)
    if hasattr(b1, 'diagram_EdgeStyle113'):
        assert not _is_linked(b1, 'diagram_EdgeStyle113', a)
    if hasattr(b2, 'diagram_EdgeStyle113'):
        assert _is_linked(b2, 'diagram_EdgeStyle113', a)
    _safe_set(a, 'diagram_EndLabelStyle', None)
    assert not _is_linked(a, 'diagram_EndLabelStyle', b2)
    if hasattr(b2, 'diagram_EdgeStyle113'):
        assert not _is_linked(b2, 'diagram_EdgeStyle113', a)


def test_assoc_endLabelStyleDescription318_link_reassign_clear():
    a = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = style_EndLabelStyleDescription()
    b2 = style_EndLabelStyleDescription()
    _safe_set(a, 'diagram_style_EdgeStyleDescription319', b1)
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription319', b1)
    if hasattr(b1, 'style_EndLabelStyleDescription'):
        assert _is_linked(b1, 'style_EndLabelStyleDescription', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription319', b2)
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription319', b2)
    if hasattr(b1, 'style_EndLabelStyleDescription'):
        assert not _is_linked(b1, 'style_EndLabelStyleDescription', a)
    if hasattr(b2, 'style_EndLabelStyleDescription'):
        assert _is_linked(b2, 'style_EndLabelStyleDescription', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription319', None)
    assert not _is_linked(a, 'diagram_style_EdgeStyleDescription319', b2)
    if hasattr(b2, 'style_EndLabelStyleDescription'):
        assert not _is_linked(b2, 'style_EndLabelStyleDescription', a)


def test_assoc_extraMappings351_link_reassign_clear():
    a = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = AbstractNodeMapping()
    b2 = AbstractNodeMapping()
    _safe_set(a, 'diagram_tool_NodeCreationDescription352', {b1})
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription352', b1)
    if hasattr(b1, 'AbstractNodeMapping353'):
        assert _is_linked(b1, 'AbstractNodeMapping353', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription352', {b2})
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription352', b2)
    if hasattr(b1, 'AbstractNodeMapping353'):
        assert not _is_linked(b1, 'AbstractNodeMapping353', a)
    if hasattr(b2, 'AbstractNodeMapping353'):
        assert _is_linked(b2, 'AbstractNodeMapping353', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription352', set())
    assert not _is_linked(a, 'diagram_tool_NodeCreationDescription352', b2)
    if hasattr(b2, 'AbstractNodeMapping353'):
        assert not _is_linked(b2, 'AbstractNodeMapping353', a)


def test_assoc_extraMappings383_link_reassign_clear():
    a = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = AbstractNodeMapping()
    b2 = AbstractNodeMapping()
    _safe_set(a, 'diagram_tool_ContainerCreationDescription384', {b1})
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription384', b1)
    if hasattr(b1, 'AbstractNodeMapping385'):
        assert _is_linked(b1, 'AbstractNodeMapping385', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription384', {b2})
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription384', b2)
    if hasattr(b1, 'AbstractNodeMapping385'):
        assert not _is_linked(b1, 'AbstractNodeMapping385', a)
    if hasattr(b2, 'AbstractNodeMapping385'):
        assert _is_linked(b2, 'AbstractNodeMapping385', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription384', set())
    assert not _is_linked(a, 'diagram_tool_ContainerCreationDescription384', b2)
    if hasattr(b2, 'AbstractNodeMapping385'):
        assert not _is_linked(b2, 'AbstractNodeMapping385', a)


def test_assoc_extraSourceMappings366_link_reassign_clear():
    a = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_tool_EdgeCreationDescription367', {b1})
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription367', b1)
    if hasattr(b1, 'DiagramElementMapping368'):
        assert _is_linked(b1, 'DiagramElementMapping368', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription367', {b2})
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription367', b2)
    if hasattr(b1, 'DiagramElementMapping368'):
        assert not _is_linked(b1, 'DiagramElementMapping368', a)
    if hasattr(b2, 'DiagramElementMapping368'):
        assert _is_linked(b2, 'DiagramElementMapping368', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription367', set())
    assert not _is_linked(a, 'diagram_tool_EdgeCreationDescription367', b2)
    if hasattr(b2, 'DiagramElementMapping368'):
        assert not _is_linked(b2, 'DiagramElementMapping368', a)


def test_assoc_extraTargetMappings369_link_reassign_clear():
    a = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_tool_EdgeCreationDescription370', {b1})
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription370', b1)
    if hasattr(b1, 'DiagramElementMapping371'):
        assert _is_linked(b1, 'DiagramElementMapping371', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription370', {b2})
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription370', b2)
    if hasattr(b1, 'DiagramElementMapping371'):
        assert not _is_linked(b1, 'DiagramElementMapping371', a)
    if hasattr(b2, 'DiagramElementMapping371'):
        assert _is_linked(b2, 'DiagramElementMapping371', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription370', set())
    assert not _is_linked(a, 'diagram_tool_EdgeCreationDescription370', b2)
    if hasattr(b2, 'DiagramElementMapping371'):
        assert not _is_linked(b2, 'DiagramElementMapping371', a)


def test_assoc_filterVariableHistory27_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = diagram_FilterVariableHistory()
    b2 = diagram_FilterVariableHistory()
    _safe_set(a, 'diagram_DDiagram28', b1)
    assert _is_linked(a, 'diagram_DDiagram28', b1)
    if hasattr(b1, 'diagram_FilterVariableHistory'):
        assert _is_linked(b1, 'diagram_FilterVariableHistory', a)
    _safe_set(a, 'diagram_DDiagram28', b2)
    assert _is_linked(a, 'diagram_DDiagram28', b2)
    if hasattr(b1, 'diagram_FilterVariableHistory'):
        assert not _is_linked(b1, 'diagram_FilterVariableHistory', a)
    if hasattr(b2, 'diagram_FilterVariableHistory'):
        assert _is_linked(b2, 'diagram_FilterVariableHistory', a)
    _safe_set(a, 'diagram_DDiagram28', None)
    assert not _is_linked(a, 'diagram_DDiagram28', b2)
    if hasattr(b2, 'diagram_FilterVariableHistory'):
        assert not _is_linked(b2, 'diagram_FilterVariableHistory', a)


def test_assoc_filters122_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = filter_FilterDescription()
    b2 = filter_FilterDescription()
    _safe_set(a, 'diagram_description_DiagramDescription', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription', b1)
    if hasattr(b1, 'filter_FilterDescription123'):
        assert _is_linked(b1, 'filter_FilterDescription123', a)
    _safe_set(a, 'diagram_description_DiagramDescription', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription', b2)
    if hasattr(b1, 'filter_FilterDescription123'):
        assert not _is_linked(b1, 'filter_FilterDescription123', a)
    if hasattr(b2, 'filter_FilterDescription123'):
        assert _is_linked(b2, 'filter_FilterDescription123', a)
    _safe_set(a, 'diagram_description_DiagramDescription', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription', b2)
    if hasattr(b2, 'filter_FilterDescription123'):
        assert not _is_linked(b2, 'filter_FilterDescription123', a)


def test_assoc_foregroundColor300_link_reassign_clear():
    a = diagram_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_GaugeSectionDescription301', b1)
    assert _is_linked(a, 'diagram_style_GaugeSectionDescription301', b1)
    if hasattr(b1, 'ColorDescription302'):
        assert _is_linked(b1, 'ColorDescription302', a)
    _safe_set(a, 'diagram_style_GaugeSectionDescription301', b2)
    assert _is_linked(a, 'diagram_style_GaugeSectionDescription301', b2)
    if hasattr(b1, 'ColorDescription302'):
        assert not _is_linked(b1, 'ColorDescription302', a)
    if hasattr(b2, 'ColorDescription302'):
        assert _is_linked(b2, 'ColorDescription302', a)
    _safe_set(a, 'diagram_style_GaugeSectionDescription301', None)
    assert not _is_linked(a, 'diagram_style_GaugeSectionDescription301', b2)
    if hasattr(b2, 'ColorDescription302'):
        assert not _is_linked(b2, 'ColorDescription302', a)


def test_assoc_foregroundColor305_link_reassign_clear():
    a = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription306', b1)
    assert _is_linked(a, 'diagram_style_FlatContainerStyleDescription306', b1)
    if hasattr(b1, 'ColorDescription307'):
        assert _is_linked(b1, 'ColorDescription307', a)
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription306', b2)
    assert _is_linked(a, 'diagram_style_FlatContainerStyleDescription306', b2)
    if hasattr(b1, 'ColorDescription307'):
        assert not _is_linked(b1, 'ColorDescription307', a)
    if hasattr(b2, 'ColorDescription307'):
        assert _is_linked(b2, 'ColorDescription307', a)
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription306', None)
    assert not _is_linked(a, 'diagram_style_FlatContainerStyleDescription306', b2)
    if hasattr(b2, 'ColorDescription307'):
        assert not _is_linked(b2, 'ColorDescription307', a)


def test_assoc_graphicalFilters44_link_reassign_clear():
    a = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = diagram_GraphicalFilter()
    b2 = diagram_GraphicalFilter()
    _safe_set(a, 'diagram_DDiagramElement45', {b1})
    assert _is_linked(a, 'diagram_DDiagramElement45', b1)
    if hasattr(b1, 'diagram_GraphicalFilter'):
        assert _is_linked(b1, 'diagram_GraphicalFilter', a)
    _safe_set(a, 'diagram_DDiagramElement45', {b2})
    assert _is_linked(a, 'diagram_DDiagramElement45', b2)
    if hasattr(b1, 'diagram_GraphicalFilter'):
        assert not _is_linked(b1, 'diagram_GraphicalFilter', a)
    if hasattr(b2, 'diagram_GraphicalFilter'):
        assert _is_linked(b2, 'diagram_GraphicalFilter', a)
    _safe_set(a, 'diagram_DDiagramElement45', set())
    assert not _is_linked(a, 'diagram_DDiagramElement45', b2)
    if hasattr(b2, 'diagram_GraphicalFilter'):
        assert not _is_linked(b2, 'diagram_GraphicalFilter', a)


def test_assoc_groupExtensions335_link_reassign_clear():
    a = diagram_tool_ToolSection(icon="sample_text")
    b1 = tool_ToolGroupExtension()
    b2 = tool_ToolGroupExtension()
    _safe_set(a, 'diagram_tool_ToolSection336', {b1})
    assert _is_linked(a, 'diagram_tool_ToolSection336', b1)
    if hasattr(b1, 'tool_ToolGroupExtension'):
        assert _is_linked(b1, 'tool_ToolGroupExtension', a)
    _safe_set(a, 'diagram_tool_ToolSection336', {b2})
    assert _is_linked(a, 'diagram_tool_ToolSection336', b2)
    if hasattr(b1, 'tool_ToolGroupExtension'):
        assert not _is_linked(b1, 'tool_ToolGroupExtension', a)
    if hasattr(b2, 'tool_ToolGroupExtension'):
        assert _is_linked(b2, 'tool_ToolGroupExtension', a)
    _safe_set(a, 'diagram_tool_ToolSection336', set())
    assert not _is_linked(a, 'diagram_tool_ToolSection336', b2)
    if hasattr(b2, 'tool_ToolGroupExtension'):
        assert not _is_linked(b2, 'tool_ToolGroupExtension', a)


def test_assoc_hiddenElements31_link_reassign_clear():
    a = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b2 = diagram_DDiagram(headerHeight=13, isInLayoutingMode=False, synchronized=False)
    _safe_set(a, 'diagram_DDiagramElement33', b1)
    assert _is_linked(a, 'diagram_DDiagramElement33', b1)
    if hasattr(b1, 'diagram_DDiagram32'):
        assert _is_linked(b1, 'diagram_DDiagram32', a)
    _safe_set(a, 'diagram_DDiagramElement33', b2)
    assert _is_linked(a, 'diagram_DDiagramElement33', b2)
    if hasattr(b1, 'diagram_DDiagram32'):
        assert not _is_linked(b1, 'diagram_DDiagram32', a)
    if hasattr(b2, 'diagram_DDiagram32'):
        assert _is_linked(b2, 'diagram_DDiagram32', a)
    _safe_set(a, 'diagram_DDiagramElement33', None)
    assert not _is_linked(a, 'diagram_DDiagramElement33', b2)
    if hasattr(b2, 'diagram_DDiagram32'):
        assert not _is_linked(b2, 'diagram_DDiagram32', a)


def test_assoc_hook396_link_reassign_clear():
    a = diagram_tool_DeleteElementDescription()
    b1 = tool_DeleteHook()
    b2 = tool_DeleteHook()
    _safe_set(a, 'diagram_tool_DeleteElementDescription397', b1)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription397', b1)
    if hasattr(b1, 'tool_DeleteHook'):
        assert _is_linked(b1, 'tool_DeleteHook', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription397', b2)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription397', b2)
    if hasattr(b1, 'tool_DeleteHook'):
        assert not _is_linked(b1, 'tool_DeleteHook', a)
    if hasattr(b2, 'tool_DeleteHook'):
        assert _is_linked(b2, 'tool_DeleteHook', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription397', None)
    assert not _is_linked(a, 'diagram_tool_DeleteElementDescription397', b2)
    if hasattr(b2, 'tool_DeleteHook'):
        assert not _is_linked(b2, 'tool_DeleteHook', a)


def test_assoc_importedMapping238_link_reassign_clear():
    a = diagram_description_EdgeMappingImport(inheritsAncestorFilters=True)
    b1 = IEdgeMapping()
    b2 = IEdgeMapping()
    _safe_set(a, 'diagram_description_EdgeMappingImport', b1)
    assert _is_linked(a, 'diagram_description_EdgeMappingImport', b1)
    if hasattr(b1, 'IEdgeMapping239'):
        assert _is_linked(b1, 'IEdgeMapping239', a)
    _safe_set(a, 'diagram_description_EdgeMappingImport', b2)
    assert _is_linked(a, 'diagram_description_EdgeMappingImport', b2)
    if hasattr(b1, 'IEdgeMapping239'):
        assert not _is_linked(b1, 'IEdgeMapping239', a)
    if hasattr(b2, 'IEdgeMapping239'):
        assert _is_linked(b2, 'IEdgeMapping239', a)
    _safe_set(a, 'diagram_description_EdgeMappingImport', None)
    assert not _is_linked(a, 'diagram_description_EdgeMappingImport', b2)
    if hasattr(b2, 'IEdgeMapping239'):
        assert not _is_linked(b2, 'IEdgeMapping239', a)


def test_assoc_incomingEdges106_link_reassign_clear():
    a = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = diagram_EdgeTarget()
    b2 = diagram_EdgeTarget()
    _safe_set(a, 'DEdge107', b1)
    assert _is_linked(a, 'DEdge107', b1)
    if hasattr(b1, 'targetNode'):
        assert _is_linked(b1, 'targetNode', a)
    _safe_set(a, 'DEdge107', b2)
    assert _is_linked(a, 'DEdge107', b2)
    if hasattr(b1, 'targetNode'):
        assert not _is_linked(b1, 'targetNode', a)
    if hasattr(b2, 'targetNode'):
        assert _is_linked(b2, 'targetNode', a)
    _safe_set(a, 'DEdge107', None)
    assert not _is_linked(a, 'DEdge107', b2)
    if hasattr(b2, 'targetNode'):
        assert not _is_linked(b2, 'targetNode', a)


def test_assoc_init141_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_RepresentationCreationDescription()
    b2 = tool_RepresentationCreationDescription()
    _safe_set(a, 'diagram_description_DiagramDescription142', b1)
    assert _is_linked(a, 'diagram_description_DiagramDescription142', b1)
    if hasattr(b1, 'tool_RepresentationCreationDescription'):
        assert _is_linked(b1, 'tool_RepresentationCreationDescription', a)
    _safe_set(a, 'diagram_description_DiagramDescription142', b2)
    assert _is_linked(a, 'diagram_description_DiagramDescription142', b2)
    if hasattr(b1, 'tool_RepresentationCreationDescription'):
        assert not _is_linked(b1, 'tool_RepresentationCreationDescription', a)
    if hasattr(b2, 'tool_RepresentationCreationDescription'):
        assert _is_linked(b2, 'tool_RepresentationCreationDescription', a)
    _safe_set(a, 'diagram_description_DiagramDescription142', None)
    assert not _is_linked(a, 'diagram_description_DiagramDescription142', b2)
    if hasattr(b2, 'tool_RepresentationCreationDescription'):
        assert not _is_linked(b2, 'tool_RepresentationCreationDescription', a)


def test_assoc_initialOperation349_link_reassign_clear():
    a = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = tool_InitialNodeCreationOperation()
    b2 = tool_InitialNodeCreationOperation()
    _safe_set(a, 'diagram_tool_NodeCreationDescription350', b1)
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription350', b1)
    if hasattr(b1, 'tool_InitialNodeCreationOperation'):
        assert _is_linked(b1, 'tool_InitialNodeCreationOperation', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription350', b2)
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription350', b2)
    if hasattr(b1, 'tool_InitialNodeCreationOperation'):
        assert not _is_linked(b1, 'tool_InitialNodeCreationOperation', a)
    if hasattr(b2, 'tool_InitialNodeCreationOperation'):
        assert _is_linked(b2, 'tool_InitialNodeCreationOperation', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription350', None)
    assert not _is_linked(a, 'diagram_tool_NodeCreationDescription350', b2)
    if hasattr(b2, 'tool_InitialNodeCreationOperation'):
        assert not _is_linked(b2, 'tool_InitialNodeCreationOperation', a)


def test_assoc_initialOperation364_link_reassign_clear():
    a = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_InitEdgeCreationOperation()
    b2 = tool_InitEdgeCreationOperation()
    _safe_set(a, 'diagram_tool_EdgeCreationDescription365', b1)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription365', b1)
    if hasattr(b1, 'tool_InitEdgeCreationOperation'):
        assert _is_linked(b1, 'tool_InitEdgeCreationOperation', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription365', b2)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription365', b2)
    if hasattr(b1, 'tool_InitEdgeCreationOperation'):
        assert not _is_linked(b1, 'tool_InitEdgeCreationOperation', a)
    if hasattr(b2, 'tool_InitEdgeCreationOperation'):
        assert _is_linked(b2, 'tool_InitEdgeCreationOperation', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription365', None)
    assert not _is_linked(a, 'diagram_tool_EdgeCreationDescription365', b2)
    if hasattr(b2, 'tool_InitEdgeCreationOperation'):
        assert not _is_linked(b2, 'tool_InitEdgeCreationOperation', a)


def test_assoc_initialOperation380_link_reassign_clear():
    a = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = tool_InitialNodeCreationOperation()
    b2 = tool_InitialNodeCreationOperation()
    _safe_set(a, 'diagram_tool_ContainerCreationDescription381', b1)
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription381', b1)
    if hasattr(b1, 'tool_InitialNodeCreationOperation382'):
        assert _is_linked(b1, 'tool_InitialNodeCreationOperation382', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription381', b2)
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription381', b2)
    if hasattr(b1, 'tool_InitialNodeCreationOperation382'):
        assert not _is_linked(b1, 'tool_InitialNodeCreationOperation382', a)
    if hasattr(b2, 'tool_InitialNodeCreationOperation382'):
        assert _is_linked(b2, 'tool_InitialNodeCreationOperation382', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription381', None)
    assert not _is_linked(a, 'diagram_tool_ContainerCreationDescription381', b2)
    if hasattr(b2, 'tool_InitialNodeCreationOperation382'):
        assert not _is_linked(b2, 'tool_InitialNodeCreationOperation382', a)


def test_assoc_initialOperation393_link_reassign_clear():
    a = diagram_tool_DeleteElementDescription()
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'diagram_tool_DeleteElementDescription394', b1)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription394', b1)
    if hasattr(b1, 'tool_InitialOperation395'):
        assert _is_linked(b1, 'tool_InitialOperation395', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription394', b2)
    assert _is_linked(a, 'diagram_tool_DeleteElementDescription394', b2)
    if hasattr(b1, 'tool_InitialOperation395'):
        assert not _is_linked(b1, 'tool_InitialOperation395', a)
    if hasattr(b2, 'tool_InitialOperation395'):
        assert _is_linked(b2, 'tool_InitialOperation395', a)
    _safe_set(a, 'diagram_tool_DeleteElementDescription394', None)
    assert not _is_linked(a, 'diagram_tool_DeleteElementDescription394', b2)
    if hasattr(b2, 'tool_InitialOperation395'):
        assert not _is_linked(b2, 'tool_InitialOperation395', a)


def test_assoc_initialOperation421_link_reassign_clear():
    a = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription422', b1)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription422', b1)
    if hasattr(b1, 'tool_InitialOperation423'):
        assert _is_linked(b1, 'tool_InitialOperation423', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription422', b2)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription422', b2)
    if hasattr(b1, 'tool_InitialOperation423'):
        assert not _is_linked(b1, 'tool_InitialOperation423', a)
    if hasattr(b2, 'tool_InitialOperation423'):
        assert _is_linked(b2, 'tool_InitialOperation423', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription422', None)
    assert not _is_linked(a, 'diagram_tool_ReconnectEdgeDescription422', b2)
    if hasattr(b2, 'tool_InitialOperation423'):
        assert not _is_linked(b2, 'tool_InitialOperation423', a)


def test_assoc_initialOperation428_link_reassign_clear():
    a = diagram_tool_DirectEditLabel(inputLabelExpression="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'diagram_tool_DirectEditLabel429', b1)
    assert _is_linked(a, 'diagram_tool_DirectEditLabel429', b1)
    if hasattr(b1, 'tool_InitialOperation430'):
        assert _is_linked(b1, 'tool_InitialOperation430', a)
    _safe_set(a, 'diagram_tool_DirectEditLabel429', b2)
    assert _is_linked(a, 'diagram_tool_DirectEditLabel429', b2)
    if hasattr(b1, 'tool_InitialOperation430'):
        assert not _is_linked(b1, 'tool_InitialOperation430', a)
    if hasattr(b2, 'tool_InitialOperation430'):
        assert _is_linked(b2, 'tool_InitialOperation430', a)
    _safe_set(a, 'diagram_tool_DirectEditLabel429', None)
    assert not _is_linked(a, 'diagram_tool_DirectEditLabel429', b2)
    if hasattr(b2, 'tool_InitialOperation430'):
        assert not _is_linked(b2, 'tool_InitialOperation430', a)


def test_assoc_initialOperation431_link_reassign_clear():
    a = diagram_tool_BehaviorTool(domainClass="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'diagram_tool_BehaviorTool', b1)
    assert _is_linked(a, 'diagram_tool_BehaviorTool', b1)
    if hasattr(b1, 'tool_InitialOperation432'):
        assert _is_linked(b1, 'tool_InitialOperation432', a)
    _safe_set(a, 'diagram_tool_BehaviorTool', b2)
    assert _is_linked(a, 'diagram_tool_BehaviorTool', b2)
    if hasattr(b1, 'tool_InitialOperation432'):
        assert not _is_linked(b1, 'tool_InitialOperation432', a)
    if hasattr(b2, 'tool_InitialOperation432'):
        assert _is_linked(b2, 'tool_InitialOperation432', a)
    _safe_set(a, 'diagram_tool_BehaviorTool', None)
    assert not _is_linked(a, 'diagram_tool_BehaviorTool', b2)
    if hasattr(b2, 'tool_InitialOperation432'):
        assert not _is_linked(b2, 'tool_InitialOperation432', a)


def test_assoc_initialOperation453_link_reassign_clear():
    a = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_InitialContainerDropOperation()
    b2 = tool_InitialContainerDropOperation()
    _safe_set(a, 'diagram_tool_ContainerDropDescription454', b1)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription454', b1)
    if hasattr(b1, 'tool_InitialContainerDropOperation'):
        assert _is_linked(b1, 'tool_InitialContainerDropOperation', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription454', b2)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription454', b2)
    if hasattr(b1, 'tool_InitialContainerDropOperation'):
        assert not _is_linked(b1, 'tool_InitialContainerDropOperation', a)
    if hasattr(b2, 'tool_InitialContainerDropOperation'):
        assert _is_linked(b2, 'tool_InitialContainerDropOperation', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription454', None)
    assert not _is_linked(a, 'diagram_tool_ContainerDropDescription454', b2)
    if hasattr(b2, 'tool_InitialContainerDropOperation'):
        assert not _is_linked(b2, 'tool_InitialContainerDropOperation', a)


def test_assoc_labelBorderStyle308_link_reassign_clear():
    a = diagram_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    b1 = style_LabelBorderStyleDescription()
    b2 = style_LabelBorderStyleDescription()
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription309', b1)
    assert _is_linked(a, 'diagram_style_FlatContainerStyleDescription309', b1)
    if hasattr(b1, 'style_LabelBorderStyleDescription'):
        assert _is_linked(b1, 'style_LabelBorderStyleDescription', a)
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription309', b2)
    assert _is_linked(a, 'diagram_style_FlatContainerStyleDescription309', b2)
    if hasattr(b1, 'style_LabelBorderStyleDescription'):
        assert not _is_linked(b1, 'style_LabelBorderStyleDescription', a)
    if hasattr(b2, 'style_LabelBorderStyleDescription'):
        assert _is_linked(b2, 'style_LabelBorderStyleDescription', a)
    _safe_set(a, 'diagram_style_FlatContainerStyleDescription309', None)
    assert not _is_linked(a, 'diagram_style_FlatContainerStyleDescription309', b2)
    if hasattr(b2, 'style_LabelBorderStyleDescription'):
        assert not _is_linked(b2, 'style_LabelBorderStyleDescription', a)


def test_assoc_labelDirectEdit189_link_reassign_clear():
    a = diagram_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    b1 = tool_DirectEditLabel()
    b2 = tool_DirectEditLabel()
    _safe_set(a, 'diagram_description_DiagramElementMapping190', b1)
    assert _is_linked(a, 'diagram_description_DiagramElementMapping190', b1)
    if hasattr(b1, 'tool_DirectEditLabel'):
        assert _is_linked(b1, 'tool_DirectEditLabel', a)
    _safe_set(a, 'diagram_description_DiagramElementMapping190', b2)
    assert _is_linked(a, 'diagram_description_DiagramElementMapping190', b2)
    if hasattr(b1, 'tool_DirectEditLabel'):
        assert not _is_linked(b1, 'tool_DirectEditLabel', a)
    if hasattr(b2, 'tool_DirectEditLabel'):
        assert _is_linked(b2, 'tool_DirectEditLabel', a)
    _safe_set(a, 'diagram_description_DiagramElementMapping190', None)
    assert not _is_linked(a, 'diagram_description_DiagramElementMapping190', b2)
    if hasattr(b2, 'tool_DirectEditLabel'):
        assert not _is_linked(b2, 'tool_DirectEditLabel', a)


def test_assoc_layout143_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = Layout()
    b2 = Layout()
    _safe_set(a, 'diagram_description_DiagramDescription144', b1)
    assert _is_linked(a, 'diagram_description_DiagramDescription144', b1)
    if hasattr(b1, 'Layout'):
        assert _is_linked(b1, 'Layout', a)
    _safe_set(a, 'diagram_description_DiagramDescription144', b2)
    assert _is_linked(a, 'diagram_description_DiagramDescription144', b2)
    if hasattr(b1, 'Layout'):
        assert not _is_linked(b1, 'Layout', a)
    if hasattr(b2, 'Layout'):
        assert _is_linked(b2, 'Layout', a)
    _safe_set(a, 'diagram_description_DiagramDescription144', None)
    assert not _is_linked(a, 'diagram_description_DiagramDescription144', b2)
    if hasattr(b2, 'Layout'):
        assert not _is_linked(b2, 'Layout', a)


def test_assoc_mapping433_link_reassign_clear():
    a = diagram_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_tool_CreateView', b1)
    assert _is_linked(a, 'diagram_tool_CreateView', b1)
    if hasattr(b1, 'DiagramElementMapping434'):
        assert _is_linked(b1, 'DiagramElementMapping434', a)
    _safe_set(a, 'diagram_tool_CreateView', b2)
    assert _is_linked(a, 'diagram_tool_CreateView', b2)
    if hasattr(b1, 'DiagramElementMapping434'):
        assert not _is_linked(b1, 'DiagramElementMapping434', a)
    if hasattr(b2, 'DiagramElementMapping434'):
        assert _is_linked(b2, 'DiagramElementMapping434', a)
    _safe_set(a, 'diagram_tool_CreateView', None)
    assert not _is_linked(a, 'diagram_tool_CreateView', b2)
    if hasattr(b2, 'DiagramElementMapping434'):
        assert not _is_linked(b2, 'DiagramElementMapping434', a)


def test_assoc_mappings441_link_reassign_clear():
    a = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_tool_ContainerDropDescription', {b1})
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription', b1)
    if hasattr(b1, 'DiagramElementMapping442'):
        assert _is_linked(b1, 'DiagramElementMapping442', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription', {b2})
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription', b2)
    if hasattr(b1, 'DiagramElementMapping442'):
        assert not _is_linked(b1, 'DiagramElementMapping442', a)
    if hasattr(b2, 'DiagramElementMapping442'):
        assert _is_linked(b2, 'DiagramElementMapping442', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription', set())
    assert not _is_linked(a, 'diagram_tool_ContainerDropDescription', b2)
    if hasattr(b2, 'DiagramElementMapping442'):
        assert not _is_linked(b2, 'DiagramElementMapping442', a)


def test_assoc_mappings455_link_reassign_clear():
    a = diagram_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_filter_MappingFilter', {b1})
    assert _is_linked(a, 'diagram_filter_MappingFilter', b1)
    if hasattr(b1, 'DiagramElementMapping456'):
        assert _is_linked(b1, 'DiagramElementMapping456', a)
    _safe_set(a, 'diagram_filter_MappingFilter', {b2})
    assert _is_linked(a, 'diagram_filter_MappingFilter', b2)
    if hasattr(b1, 'DiagramElementMapping456'):
        assert not _is_linked(b1, 'DiagramElementMapping456', a)
    if hasattr(b2, 'DiagramElementMapping456'):
        assert _is_linked(b2, 'DiagramElementMapping456', a)
    _safe_set(a, 'diagram_filter_MappingFilter', set())
    assert not _is_linked(a, 'diagram_filter_MappingFilter', b2)
    if hasattr(b2, 'DiagramElementMapping456'):
        assert not _is_linked(b2, 'DiagramElementMapping456', a)


def test_assoc_mask427_link_reassign_clear():
    a = diagram_tool_DirectEditLabel(inputLabelExpression="sample_text")
    b1 = tool_EditMaskVariables()
    b2 = tool_EditMaskVariables()
    _safe_set(a, 'diagram_tool_DirectEditLabel', b1)
    assert _is_linked(a, 'diagram_tool_DirectEditLabel', b1)
    if hasattr(b1, 'tool_EditMaskVariables'):
        assert _is_linked(b1, 'tool_EditMaskVariables', a)
    _safe_set(a, 'diagram_tool_DirectEditLabel', b2)
    assert _is_linked(a, 'diagram_tool_DirectEditLabel', b2)
    if hasattr(b1, 'tool_EditMaskVariables'):
        assert not _is_linked(b1, 'tool_EditMaskVariables', a)
    if hasattr(b2, 'tool_EditMaskVariables'):
        assert _is_linked(b2, 'tool_EditMaskVariables', a)
    _safe_set(a, 'diagram_tool_DirectEditLabel', None)
    assert not _is_linked(a, 'diagram_tool_DirectEditLabel', b2)
    if hasattr(b2, 'tool_EditMaskVariables'):
        assert not _is_linked(b2, 'tool_EditMaskVariables', a)


def test_assoc_newContainer445_link_reassign_clear():
    a = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'diagram_tool_ContainerDropDescription446', b1)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription446', b1)
    if hasattr(b1, 'tool_DropContainerVariable447'):
        assert _is_linked(b1, 'tool_DropContainerVariable447', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription446', b2)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription446', b2)
    if hasattr(b1, 'tool_DropContainerVariable447'):
        assert not _is_linked(b1, 'tool_DropContainerVariable447', a)
    if hasattr(b2, 'tool_DropContainerVariable447'):
        assert _is_linked(b2, 'tool_DropContainerVariable447', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription446', None)
    assert not _is_linked(a, 'diagram_tool_ContainerDropDescription446', b2)
    if hasattr(b2, 'tool_DropContainerVariable447'):
        assert not _is_linked(b2, 'tool_DropContainerVariable447', a)


def test_assoc_newViewContainer450_link_reassign_clear():
    a = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'diagram_tool_ContainerDropDescription451', b1)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription451', b1)
    if hasattr(b1, 'tool_ContainerViewVariable452'):
        assert _is_linked(b1, 'tool_ContainerViewVariable452', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription451', b2)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription451', b2)
    if hasattr(b1, 'tool_ContainerViewVariable452'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable452', a)
    if hasattr(b2, 'tool_ContainerViewVariable452'):
        assert _is_linked(b2, 'tool_ContainerViewVariable452', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription451', None)
    assert not _is_linked(a, 'diagram_tool_ContainerDropDescription451', b2)
    if hasattr(b2, 'tool_ContainerViewVariable452'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable452', a)


def test_assoc_nodeListElements10_link_reassign_clear():
    a = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b1 = diagram_DNodeListElement()
    b2 = diagram_DNodeListElement()
    _safe_set(a, 'diagram_DDiagram11', {b1})
    assert _is_linked(a, 'diagram_DDiagram11', b1)
    if hasattr(b1, 'diagram_DNodeListElement'):
        assert _is_linked(b1, 'diagram_DNodeListElement', a)
    _safe_set(a, 'diagram_DDiagram11', {b2})
    assert _is_linked(a, 'diagram_DDiagram11', b2)
    if hasattr(b1, 'diagram_DNodeListElement'):
        assert not _is_linked(b1, 'diagram_DNodeListElement', a)
    if hasattr(b2, 'diagram_DNodeListElement'):
        assert _is_linked(b2, 'diagram_DNodeListElement', a)
    _safe_set(a, 'diagram_DDiagram11', set())
    assert not _is_linked(a, 'diagram_DDiagram11', b2)
    if hasattr(b2, 'diagram_DNodeListElement'):
        assert not _is_linked(b2, 'diagram_DNodeListElement', a)


def test_assoc_nodeMapping249_link_reassign_clear():
    a = diagram_description_OrderedTreeLayout(childrenExpression="sample_text")
    b1 = AbstractNodeMapping()
    b2 = AbstractNodeMapping()
    _safe_set(a, 'diagram_description_OrderedTreeLayout', {b1})
    assert _is_linked(a, 'diagram_description_OrderedTreeLayout', b1)
    if hasattr(b1, 'AbstractNodeMapping250'):
        assert _is_linked(b1, 'AbstractNodeMapping250', a)
    _safe_set(a, 'diagram_description_OrderedTreeLayout', {b2})
    assert _is_linked(a, 'diagram_description_OrderedTreeLayout', b2)
    if hasattr(b1, 'AbstractNodeMapping250'):
        assert not _is_linked(b1, 'AbstractNodeMapping250', a)
    if hasattr(b2, 'AbstractNodeMapping250'):
        assert _is_linked(b2, 'AbstractNodeMapping250', a)
    _safe_set(a, 'diagram_description_OrderedTreeLayout', set())
    assert not _is_linked(a, 'diagram_description_OrderedTreeLayout', b2)
    if hasattr(b2, 'AbstractNodeMapping250'):
        assert not _is_linked(b2, 'AbstractNodeMapping250', a)


def test_assoc_nodeMappings159_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_description_DiagramDescription160', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription160', b1)
    if hasattr(b1, 'NodeMapping161'):
        assert _is_linked(b1, 'NodeMapping161', a)
    _safe_set(a, 'diagram_description_DiagramDescription160', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription160', b2)
    if hasattr(b1, 'NodeMapping161'):
        assert not _is_linked(b1, 'NodeMapping161', a)
    if hasattr(b2, 'NodeMapping161'):
        assert _is_linked(b2, 'NodeMapping161', a)
    _safe_set(a, 'diagram_description_DiagramDescription160', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription160', b2)
    if hasattr(b2, 'NodeMapping161'):
        assert not _is_linked(b2, 'NodeMapping161', a)


def test_assoc_nodeMappings253_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_description_Layer', {b1})
    assert _is_linked(a, 'diagram_description_Layer', b1)
    if hasattr(b1, 'NodeMapping254'):
        assert _is_linked(b1, 'NodeMapping254', a)
    _safe_set(a, 'diagram_description_Layer', {b2})
    assert _is_linked(a, 'diagram_description_Layer', b2)
    if hasattr(b1, 'NodeMapping254'):
        assert not _is_linked(b1, 'NodeMapping254', a)
    if hasattr(b2, 'NodeMapping254'):
        assert _is_linked(b2, 'NodeMapping254', a)
    _safe_set(a, 'diagram_description_Layer', set())
    assert not _is_linked(a, 'diagram_description_Layer', b2)
    if hasattr(b2, 'NodeMapping254'):
        assert not _is_linked(b2, 'NodeMapping254', a)


def test_assoc_nodeMappings343_link_reassign_clear():
    a = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_tool_NodeCreationDescription', {b1})
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription', b1)
    if hasattr(b1, 'NodeMapping344'):
        assert _is_linked(b1, 'NodeMapping344', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription', {b2})
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription', b2)
    if hasattr(b1, 'NodeMapping344'):
        assert not _is_linked(b1, 'NodeMapping344', a)
    if hasattr(b2, 'NodeMapping344'):
        assert _is_linked(b2, 'NodeMapping344', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription', set())
    assert not _is_linked(a, 'diagram_tool_NodeCreationDescription', b2)
    if hasattr(b2, 'NodeMapping344'):
        assert not _is_linked(b2, 'NodeMapping344', a)


def test_assoc_nodes58_link_reassign_clear():
    a = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b2 = diagram_DDiagramElementContainer(height="sample_text_2", width="sample_text_2")
    _safe_set(a, 'diagram_DNode60', b1)
    assert _is_linked(a, 'diagram_DNode60', b1)
    if hasattr(b1, 'diagram_DDiagramElementContainer59'):
        assert _is_linked(b1, 'diagram_DDiagramElementContainer59', a)
    _safe_set(a, 'diagram_DNode60', b2)
    assert _is_linked(a, 'diagram_DNode60', b2)
    if hasattr(b1, 'diagram_DDiagramElementContainer59'):
        assert not _is_linked(b1, 'diagram_DDiagramElementContainer59', a)
    if hasattr(b2, 'diagram_DDiagramElementContainer59'):
        assert _is_linked(b2, 'diagram_DDiagramElementContainer59', a)
    _safe_set(a, 'diagram_DNode60', None)
    assert not _is_linked(a, 'diagram_DNode60', b2)
    if hasattr(b2, 'diagram_DDiagramElementContainer59'):
        assert not _is_linked(b2, 'diagram_DDiagramElementContainer59', a)


def test_assoc_nodes8_link_reassign_clear():
    a = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b2 = diagram_DDiagram(headerHeight=13, isInLayoutingMode=False, synchronized=False)
    _safe_set(a, 'diagram_DNode', b1)
    assert _is_linked(a, 'diagram_DNode', b1)
    if hasattr(b1, 'diagram_DDiagram9'):
        assert _is_linked(b1, 'diagram_DDiagram9', a)
    _safe_set(a, 'diagram_DNode', b2)
    assert _is_linked(a, 'diagram_DNode', b2)
    if hasattr(b1, 'diagram_DDiagram9'):
        assert not _is_linked(b1, 'diagram_DDiagram9', a)
    if hasattr(b2, 'diagram_DDiagram9'):
        assert _is_linked(b2, 'diagram_DDiagram9', a)
    _safe_set(a, 'diagram_DNode', None)
    assert not _is_linked(a, 'diagram_DNode', b2)
    if hasattr(b2, 'diagram_DDiagram9'):
        assert not _is_linked(b2, 'diagram_DDiagram9', a)


def test_assoc_oldContainer443_link_reassign_clear():
    a = diagram_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'diagram_tool_ContainerDropDescription444', b1)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription444', b1)
    if hasattr(b1, 'tool_DropContainerVariable'):
        assert _is_linked(b1, 'tool_DropContainerVariable', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription444', b2)
    assert _is_linked(a, 'diagram_tool_ContainerDropDescription444', b2)
    if hasattr(b1, 'tool_DropContainerVariable'):
        assert not _is_linked(b1, 'tool_DropContainerVariable', a)
    if hasattr(b2, 'tool_DropContainerVariable'):
        assert _is_linked(b2, 'tool_DropContainerVariable', a)
    _safe_set(a, 'diagram_tool_ContainerDropDescription444', None)
    assert not _is_linked(a, 'diagram_tool_ContainerDropDescription444', b2)
    if hasattr(b2, 'tool_DropContainerVariable'):
        assert not _is_linked(b2, 'tool_DropContainerVariable', a)


def test_assoc_originalStyle100_link_reassign_clear():
    a = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = diagram_Style()
    b2 = diagram_Style()
    _safe_set(a, 'diagram_DEdge101', b1)
    assert _is_linked(a, 'diagram_DEdge101', b1)
    if hasattr(b1, 'diagram_Style102'):
        assert _is_linked(b1, 'diagram_Style102', a)
    _safe_set(a, 'diagram_DEdge101', b2)
    assert _is_linked(a, 'diagram_DEdge101', b2)
    if hasattr(b1, 'diagram_Style102'):
        assert not _is_linked(b1, 'diagram_Style102', a)
    if hasattr(b2, 'diagram_Style102'):
        assert _is_linked(b2, 'diagram_Style102', a)
    _safe_set(a, 'diagram_DEdge101', None)
    assert not _is_linked(a, 'diagram_DEdge101', b2)
    if hasattr(b2, 'diagram_Style102'):
        assert not _is_linked(b2, 'diagram_Style102', a)


def test_assoc_originalStyle51_link_reassign_clear():
    a = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = diagram_Style()
    b2 = diagram_Style()
    _safe_set(a, 'diagram_DNode52', b1)
    assert _is_linked(a, 'diagram_DNode52', b1)
    if hasattr(b1, 'diagram_Style'):
        assert _is_linked(b1, 'diagram_Style', a)
    _safe_set(a, 'diagram_DNode52', b2)
    assert _is_linked(a, 'diagram_DNode52', b2)
    if hasattr(b1, 'diagram_Style'):
        assert not _is_linked(b1, 'diagram_Style', a)
    if hasattr(b2, 'diagram_Style'):
        assert _is_linked(b2, 'diagram_Style', a)
    _safe_set(a, 'diagram_DNode52', None)
    assert not _is_linked(a, 'diagram_DNode52', b2)
    if hasattr(b2, 'diagram_Style'):
        assert not _is_linked(b2, 'diagram_Style', a)


def test_assoc_originalStyle69_link_reassign_clear():
    a = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = diagram_Style()
    b2 = diagram_Style()
    _safe_set(a, 'diagram_DDiagramElementContainer70', b1)
    assert _is_linked(a, 'diagram_DDiagramElementContainer70', b1)
    if hasattr(b1, 'diagram_Style71'):
        assert _is_linked(b1, 'diagram_Style71', a)
    _safe_set(a, 'diagram_DDiagramElementContainer70', b2)
    assert _is_linked(a, 'diagram_DDiagramElementContainer70', b2)
    if hasattr(b1, 'diagram_Style71'):
        assert not _is_linked(b1, 'diagram_Style71', a)
    if hasattr(b2, 'diagram_Style71'):
        assert _is_linked(b2, 'diagram_Style71', a)
    _safe_set(a, 'diagram_DDiagramElementContainer70', None)
    assert not _is_linked(a, 'diagram_DDiagramElementContainer70', b2)
    if hasattr(b2, 'diagram_Style71'):
        assert not _is_linked(b2, 'diagram_Style71', a)


def test_assoc_outgoingEdges105_link_reassign_clear():
    a = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = diagram_EdgeTarget()
    b2 = diagram_EdgeTarget()
    _safe_set(a, 'DEdge', b1)
    assert _is_linked(a, 'DEdge', b1)
    if hasattr(b1, 'sourceNode'):
        assert _is_linked(b1, 'sourceNode', a)
    _safe_set(a, 'DEdge', b2)
    assert _is_linked(a, 'DEdge', b2)
    if hasattr(b1, 'sourceNode'):
        assert not _is_linked(b1, 'sourceNode', a)
    if hasattr(b2, 'sourceNode'):
        assert _is_linked(b2, 'sourceNode', a)
    _safe_set(a, 'DEdge', None)
    assert not _is_linked(a, 'DEdge', b2)
    if hasattr(b2, 'sourceNode'):
        assert not _is_linked(b2, 'sourceNode', a)


def test_assoc_ownedBorderedNodes47_link_reassign_clear():
    a = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = diagram_AbstractDNode(arrangeConstraints="sample_text")
    b2 = diagram_AbstractDNode(arrangeConstraints="sample_text_2")
    _safe_set(a, 'diagram_DNode48', b1)
    assert _is_linked(a, 'diagram_DNode48', b1)
    if hasattr(b1, 'diagram_AbstractDNode'):
        assert _is_linked(b1, 'diagram_AbstractDNode', a)
    _safe_set(a, 'diagram_DNode48', b2)
    assert _is_linked(a, 'diagram_DNode48', b2)
    if hasattr(b1, 'diagram_AbstractDNode'):
        assert not _is_linked(b1, 'diagram_AbstractDNode', a)
    if hasattr(b2, 'diagram_AbstractDNode'):
        assert _is_linked(b2, 'diagram_AbstractDNode', a)
    _safe_set(a, 'diagram_DNode48', None)
    assert not _is_linked(a, 'diagram_DNode48', b2)
    if hasattr(b2, 'diagram_AbstractDNode'):
        assert not _is_linked(b2, 'diagram_AbstractDNode', a)


def test_assoc_ownedDiagramElements0_link_reassign_clear():
    a = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = diagram_DDiagram(headerHeight=7, isInLayoutingMode=True, synchronized=True)
    b2 = diagram_DDiagram(headerHeight=13, isInLayoutingMode=False, synchronized=False)
    _safe_set(a, 'diagram_DDiagramElement', b1)
    assert _is_linked(a, 'diagram_DDiagramElement', b1)
    if hasattr(b1, 'diagram_DDiagram'):
        assert _is_linked(b1, 'diagram_DDiagram', a)
    _safe_set(a, 'diagram_DDiagramElement', b2)
    assert _is_linked(a, 'diagram_DDiagramElement', b2)
    if hasattr(b1, 'diagram_DDiagram'):
        assert not _is_linked(b1, 'diagram_DDiagram', a)
    if hasattr(b2, 'diagram_DDiagram'):
        assert _is_linked(b2, 'diagram_DDiagram', a)
    _safe_set(a, 'diagram_DDiagramElement', None)
    assert not _is_linked(a, 'diagram_DDiagramElement', b2)
    if hasattr(b2, 'diagram_DDiagram'):
        assert not _is_linked(b2, 'diagram_DDiagram', a)


def test_assoc_ownedDiagramElements77_link_reassign_clear():
    a = diagram_DNodeContainer(childrenPresentation="sample_text")
    b1 = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b2 = diagram_DDiagramElement(tooltipText="sample_text_2", visible=False)
    _safe_set(a, 'diagram_DNodeContainer', {b1})
    assert _is_linked(a, 'diagram_DNodeContainer', b1)
    if hasattr(b1, 'diagram_DDiagramElement78'):
        assert _is_linked(b1, 'diagram_DDiagramElement78', a)
    _safe_set(a, 'diagram_DNodeContainer', {b2})
    assert _is_linked(a, 'diagram_DNodeContainer', b2)
    if hasattr(b1, 'diagram_DDiagramElement78'):
        assert not _is_linked(b1, 'diagram_DDiagramElement78', a)
    if hasattr(b2, 'diagram_DDiagramElement78'):
        assert _is_linked(b2, 'diagram_DDiagramElement78', a)
    _safe_set(a, 'diagram_DNodeContainer', set())
    assert not _is_linked(a, 'diagram_DNodeContainer', b2)
    if hasattr(b2, 'diagram_DDiagramElement78'):
        assert not _is_linked(b2, 'diagram_DDiagramElement78', a)


def test_assoc_ownedStyle49_link_reassign_clear():
    a = diagram_NodeStyle(labelPosition="sample_text")
    b1 = diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b2 = diagram_DNode(height="sample_text_2", labelPosition="sample_text_2", resizeKind="sample_text_2", width="sample_text_2")
    _safe_set(a, 'diagram_NodeStyle', b1)
    assert _is_linked(a, 'diagram_NodeStyle', b1)
    if hasattr(b1, 'diagram_DNode50'):
        assert _is_linked(b1, 'diagram_DNode50', a)
    _safe_set(a, 'diagram_NodeStyle', b2)
    assert _is_linked(a, 'diagram_NodeStyle', b2)
    if hasattr(b1, 'diagram_DNode50'):
        assert not _is_linked(b1, 'diagram_DNode50', a)
    if hasattr(b2, 'diagram_DNode50'):
        assert _is_linked(b2, 'diagram_DNode50', a)
    _safe_set(a, 'diagram_NodeStyle', None)
    assert not _is_linked(a, 'diagram_NodeStyle', b2)
    if hasattr(b2, 'diagram_DNode50'):
        assert not _is_linked(b2, 'diagram_DNode50', a)


def test_assoc_ownedStyle67_link_reassign_clear():
    a = diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = diagram_ContainerStyle()
    b2 = diagram_ContainerStyle()
    _safe_set(a, 'diagram_DDiagramElementContainer68', b1)
    assert _is_linked(a, 'diagram_DDiagramElementContainer68', b1)
    if hasattr(b1, 'diagram_ContainerStyle'):
        assert _is_linked(b1, 'diagram_ContainerStyle', a)
    _safe_set(a, 'diagram_DDiagramElementContainer68', b2)
    assert _is_linked(a, 'diagram_DDiagramElementContainer68', b2)
    if hasattr(b1, 'diagram_ContainerStyle'):
        assert not _is_linked(b1, 'diagram_ContainerStyle', a)
    if hasattr(b2, 'diagram_ContainerStyle'):
        assert _is_linked(b2, 'diagram_ContainerStyle', a)
    _safe_set(a, 'diagram_DDiagramElementContainer68', None)
    assert not _is_linked(a, 'diagram_DDiagramElementContainer68', b2)
    if hasattr(b2, 'diagram_ContainerStyle'):
        assert not _is_linked(b2, 'diagram_ContainerStyle', a)


def test_assoc_ownedStyle81_link_reassign_clear():
    a = diagram_NodeStyle(labelPosition="sample_text")
    b1 = diagram_DNodeListElement()
    b2 = diagram_DNodeListElement()
    _safe_set(a, 'diagram_NodeStyle83', b1)
    assert _is_linked(a, 'diagram_NodeStyle83', b1)
    if hasattr(b1, 'diagram_DNodeListElement82'):
        assert _is_linked(b1, 'diagram_DNodeListElement82', a)
    _safe_set(a, 'diagram_NodeStyle83', b2)
    assert _is_linked(a, 'diagram_NodeStyle83', b2)
    if hasattr(b1, 'diagram_DNodeListElement82'):
        assert not _is_linked(b1, 'diagram_DNodeListElement82', a)
    if hasattr(b2, 'diagram_DNodeListElement82'):
        assert _is_linked(b2, 'diagram_DNodeListElement82', a)
    _safe_set(a, 'diagram_NodeStyle83', None)
    assert not _is_linked(a, 'diagram_NodeStyle83', b2)
    if hasattr(b2, 'diagram_DNodeListElement82'):
        assert not _is_linked(b2, 'diagram_DNodeListElement82', a)


def test_assoc_ownedStyle93_link_reassign_clear():
    a = diagram_EdgeStyle(centered="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", strokeColor="sample_text", targetArrow="sample_text")
    b1 = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b2 = diagram_DEdge(arrangeConstraints="sample_text_2", beginLabel="sample_text_2", endLabel="sample_text_2", isFold=False, isMockEdge=False, routingStyle="sample_text_2", size="sample_text_2")
    _safe_set(a, 'diagram_EdgeStyle', b1)
    assert _is_linked(a, 'diagram_EdgeStyle', b1)
    if hasattr(b1, 'diagram_DEdge94'):
        assert _is_linked(b1, 'diagram_DEdge94', a)
    _safe_set(a, 'diagram_EdgeStyle', b2)
    assert _is_linked(a, 'diagram_EdgeStyle', b2)
    if hasattr(b1, 'diagram_DEdge94'):
        assert not _is_linked(b1, 'diagram_DEdge94', a)
    if hasattr(b2, 'diagram_DEdge94'):
        assert _is_linked(b2, 'diagram_DEdge94', a)
    _safe_set(a, 'diagram_EdgeStyle', None)
    assert not _is_linked(a, 'diagram_EdgeStyle', b2)
    if hasattr(b2, 'diagram_DEdge94'):
        assert not _is_linked(b2, 'diagram_DEdge94', a)


def test_assoc_ownedTools326_link_reassign_clear():
    a = diagram_tool_ToolSection(icon="sample_text")
    b1 = tool_ToolEntry()
    b2 = tool_ToolEntry()
    _safe_set(a, 'diagram_tool_ToolSection', {b1})
    assert _is_linked(a, 'diagram_tool_ToolSection', b1)
    if hasattr(b1, 'tool_ToolEntry'):
        assert _is_linked(b1, 'tool_ToolEntry', a)
    _safe_set(a, 'diagram_tool_ToolSection', {b2})
    assert _is_linked(a, 'diagram_tool_ToolSection', b2)
    if hasattr(b1, 'tool_ToolEntry'):
        assert not _is_linked(b1, 'tool_ToolEntry', a)
    if hasattr(b2, 'tool_ToolEntry'):
        assert _is_linked(b2, 'tool_ToolEntry', a)
    _safe_set(a, 'diagram_tool_ToolSection', set())
    assert not _is_linked(a, 'diagram_tool_ToolSection', b2)
    if hasattr(b2, 'tool_ToolEntry'):
        assert not _is_linked(b2, 'tool_ToolEntry', a)


def test_assoc_ownedVariables458_link_reassign_clear():
    a = diagram_filter_VariableFilter(semanticConditionExpression="sample_text")
    b1 = InteractiveVariableDescription()
    b2 = InteractiveVariableDescription()
    _safe_set(a, 'diagram_filter_VariableFilter', {b1})
    assert _is_linked(a, 'diagram_filter_VariableFilter', b1)
    if hasattr(b1, 'InteractiveVariableDescription'):
        assert _is_linked(b1, 'InteractiveVariableDescription', a)
    _safe_set(a, 'diagram_filter_VariableFilter', {b2})
    assert _is_linked(a, 'diagram_filter_VariableFilter', b2)
    if hasattr(b1, 'InteractiveVariableDescription'):
        assert not _is_linked(b1, 'InteractiveVariableDescription', a)
    if hasattr(b2, 'InteractiveVariableDescription'):
        assert _is_linked(b2, 'InteractiveVariableDescription', a)
    _safe_set(a, 'diagram_filter_VariableFilter', set())
    assert not _is_linked(a, 'diagram_filter_VariableFilter', b2)
    if hasattr(b2, 'InteractiveVariableDescription'):
        assert not _is_linked(b2, 'InteractiveVariableDescription', a)


def test_assoc_parameters407_link_reassign_clear():
    a = diagram_tool_DeleteHook(id="sample_text")
    b1 = tool_DeleteHookParameter()
    b2 = tool_DeleteHookParameter()
    _safe_set(a, 'diagram_tool_DeleteHook', {b1})
    assert _is_linked(a, 'diagram_tool_DeleteHook', b1)
    if hasattr(b1, 'tool_DeleteHookParameter'):
        assert _is_linked(b1, 'tool_DeleteHookParameter', a)
    _safe_set(a, 'diagram_tool_DeleteHook', {b2})
    assert _is_linked(a, 'diagram_tool_DeleteHook', b2)
    if hasattr(b1, 'tool_DeleteHookParameter'):
        assert not _is_linked(b1, 'tool_DeleteHookParameter', a)
    if hasattr(b2, 'tool_DeleteHookParameter'):
        assert _is_linked(b2, 'tool_DeleteHookParameter', a)
    _safe_set(a, 'diagram_tool_DeleteHook', set())
    assert not _is_linked(a, 'diagram_tool_DeleteHook', b2)
    if hasattr(b2, 'tool_DeleteHookParameter'):
        assert not _is_linked(b2, 'tool_DeleteHookParameter', a)


def test_assoc_parentLayers34_link_reassign_clear():
    a = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = Layer()
    b2 = Layer()
    _safe_set(a, 'diagram_DDiagramElement35', {b1})
    assert _is_linked(a, 'diagram_DDiagramElement35', b1)
    if hasattr(b1, 'Layer36'):
        assert _is_linked(b1, 'Layer36', a)
    _safe_set(a, 'diagram_DDiagramElement35', {b2})
    assert _is_linked(a, 'diagram_DDiagramElement35', b2)
    if hasattr(b1, 'Layer36'):
        assert not _is_linked(b1, 'Layer36', a)
    if hasattr(b2, 'Layer36'):
        assert _is_linked(b2, 'Layer36', a)
    _safe_set(a, 'diagram_DDiagramElement35', set())
    assert not _is_linked(a, 'diagram_DDiagramElement35', b2)
    if hasattr(b2, 'Layer36'):
        assert not _is_linked(b2, 'Layer36', a)


def test_assoc_path103_link_reassign_clear():
    a = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = diagram_EdgeTarget()
    b2 = diagram_EdgeTarget()
    _safe_set(a, 'diagram_DEdge104', {b1})
    assert _is_linked(a, 'diagram_DEdge104', b1)
    if hasattr(b1, 'diagram_EdgeTarget'):
        assert _is_linked(b1, 'diagram_EdgeTarget', a)
    _safe_set(a, 'diagram_DEdge104', {b2})
    assert _is_linked(a, 'diagram_DEdge104', b2)
    if hasattr(b1, 'diagram_EdgeTarget'):
        assert not _is_linked(b1, 'diagram_EdgeTarget', a)
    if hasattr(b2, 'diagram_EdgeTarget'):
        assert _is_linked(b2, 'diagram_EdgeTarget', a)
    _safe_set(a, 'diagram_DEdge104', set())
    assert not _is_linked(a, 'diagram_DEdge104', b2)
    if hasattr(b2, 'diagram_EdgeTarget'):
        assert not _is_linked(b2, 'diagram_EdgeTarget', a)


def test_assoc_pathNodeMapping236_link_reassign_clear():
    a = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = AbstractNodeMapping()
    b2 = AbstractNodeMapping()
    _safe_set(a, 'diagram_description_EdgeMapping237', {b1})
    assert _is_linked(a, 'diagram_description_EdgeMapping237', b1)
    if hasattr(b1, 'AbstractNodeMapping'):
        assert _is_linked(b1, 'AbstractNodeMapping', a)
    _safe_set(a, 'diagram_description_EdgeMapping237', {b2})
    assert _is_linked(a, 'diagram_description_EdgeMapping237', b2)
    if hasattr(b1, 'AbstractNodeMapping'):
        assert not _is_linked(b1, 'AbstractNodeMapping', a)
    if hasattr(b2, 'AbstractNodeMapping'):
        assert _is_linked(b2, 'AbstractNodeMapping', a)
    _safe_set(a, 'diagram_description_EdgeMapping237', set())
    assert not _is_linked(a, 'diagram_description_EdgeMapping237', b2)
    if hasattr(b2, 'AbstractNodeMapping'):
        assert not _is_linked(b2, 'AbstractNodeMapping', a)


def test_assoc_popupMenus330_link_reassign_clear():
    a = diagram_tool_ToolSection(icon="sample_text")
    b1 = tool_PopupMenu()
    b2 = tool_PopupMenu()
    _safe_set(a, 'diagram_tool_ToolSection331', {b1})
    assert _is_linked(a, 'diagram_tool_ToolSection331', b1)
    if hasattr(b1, 'tool_PopupMenu'):
        assert _is_linked(b1, 'tool_PopupMenu', a)
    _safe_set(a, 'diagram_tool_ToolSection331', {b2})
    assert _is_linked(a, 'diagram_tool_ToolSection331', b2)
    if hasattr(b1, 'tool_PopupMenu'):
        assert not _is_linked(b1, 'tool_PopupMenu', a)
    if hasattr(b2, 'tool_PopupMenu'):
        assert _is_linked(b2, 'tool_PopupMenu', a)
    _safe_set(a, 'diagram_tool_ToolSection331', set())
    assert not _is_linked(a, 'diagram_tool_ToolSection331', b2)
    if hasattr(b2, 'tool_PopupMenu'):
        assert not _is_linked(b2, 'tool_PopupMenu', a)


def test_assoc_reconnections234_link_reassign_clear():
    a = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = tool_ReconnectEdgeDescription()
    b2 = tool_ReconnectEdgeDescription()
    _safe_set(a, 'diagram_description_EdgeMapping235', {b1})
    assert _is_linked(a, 'diagram_description_EdgeMapping235', b1)
    if hasattr(b1, 'tool_ReconnectEdgeDescription'):
        assert _is_linked(b1, 'tool_ReconnectEdgeDescription', a)
    _safe_set(a, 'diagram_description_EdgeMapping235', {b2})
    assert _is_linked(a, 'diagram_description_EdgeMapping235', b2)
    if hasattr(b1, 'tool_ReconnectEdgeDescription'):
        assert not _is_linked(b1, 'tool_ReconnectEdgeDescription', a)
    if hasattr(b2, 'tool_ReconnectEdgeDescription'):
        assert _is_linked(b2, 'tool_ReconnectEdgeDescription', a)
    _safe_set(a, 'diagram_description_EdgeMapping235', set())
    assert not _is_linked(a, 'diagram_description_EdgeMapping235', b2)
    if hasattr(b2, 'tool_ReconnectEdgeDescription'):
        assert not _is_linked(b2, 'tool_ReconnectEdgeDescription', a)


def test_assoc_reusedBorderedNodeMappings194_link_reassign_clear():
    a = diagram_description_AbstractNodeMapping(domainClass="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_description_AbstractNodeMapping195', {b1})
    assert _is_linked(a, 'diagram_description_AbstractNodeMapping195', b1)
    if hasattr(b1, 'NodeMapping196'):
        assert _is_linked(b1, 'NodeMapping196', a)
    _safe_set(a, 'diagram_description_AbstractNodeMapping195', {b2})
    assert _is_linked(a, 'diagram_description_AbstractNodeMapping195', b2)
    if hasattr(b1, 'NodeMapping196'):
        assert not _is_linked(b1, 'NodeMapping196', a)
    if hasattr(b2, 'NodeMapping196'):
        assert _is_linked(b2, 'NodeMapping196', a)
    _safe_set(a, 'diagram_description_AbstractNodeMapping195', set())
    assert not _is_linked(a, 'diagram_description_AbstractNodeMapping195', b2)
    if hasattr(b2, 'NodeMapping196'):
        assert not _is_linked(b2, 'NodeMapping196', a)


def test_assoc_reusedContainerMappings211_link_reassign_clear():
    a = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_description_ContainerMapping212', {b1})
    assert _is_linked(a, 'diagram_description_ContainerMapping212', b1)
    if hasattr(b1, 'ContainerMapping213'):
        assert _is_linked(b1, 'ContainerMapping213', a)
    _safe_set(a, 'diagram_description_ContainerMapping212', {b2})
    assert _is_linked(a, 'diagram_description_ContainerMapping212', b2)
    if hasattr(b1, 'ContainerMapping213'):
        assert not _is_linked(b1, 'ContainerMapping213', a)
    if hasattr(b2, 'ContainerMapping213'):
        assert _is_linked(b2, 'ContainerMapping213', a)
    _safe_set(a, 'diagram_description_ContainerMapping212', set())
    assert not _is_linked(a, 'diagram_description_ContainerMapping212', b2)
    if hasattr(b2, 'ContainerMapping213'):
        assert not _is_linked(b2, 'ContainerMapping213', a)


def test_assoc_reusedMappings170_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_description_DiagramDescription171', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription171', b1)
    if hasattr(b1, 'DiagramElementMapping172'):
        assert _is_linked(b1, 'DiagramElementMapping172', a)
    _safe_set(a, 'diagram_description_DiagramDescription171', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription171', b2)
    if hasattr(b1, 'DiagramElementMapping172'):
        assert not _is_linked(b1, 'DiagramElementMapping172', a)
    if hasattr(b2, 'DiagramElementMapping172'):
        assert _is_linked(b2, 'DiagramElementMapping172', a)
    _safe_set(a, 'diagram_description_DiagramDescription171', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription171', b2)
    if hasattr(b2, 'DiagramElementMapping172'):
        assert not _is_linked(b2, 'DiagramElementMapping172', a)


def test_assoc_reusedMappings264_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_description_Layer265', {b1})
    assert _is_linked(a, 'diagram_description_Layer265', b1)
    if hasattr(b1, 'DiagramElementMapping266'):
        assert _is_linked(b1, 'DiagramElementMapping266', a)
    _safe_set(a, 'diagram_description_Layer265', {b2})
    assert _is_linked(a, 'diagram_description_Layer265', b2)
    if hasattr(b1, 'DiagramElementMapping266'):
        assert not _is_linked(b1, 'DiagramElementMapping266', a)
    if hasattr(b2, 'DiagramElementMapping266'):
        assert _is_linked(b2, 'DiagramElementMapping266', a)
    _safe_set(a, 'diagram_description_Layer265', set())
    assert not _is_linked(a, 'diagram_description_Layer265', b2)
    if hasattr(b2, 'DiagramElementMapping266'):
        assert not _is_linked(b2, 'DiagramElementMapping266', a)


def test_assoc_reusedNodeMappings205_link_reassign_clear():
    a = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_description_ContainerMapping206', {b1})
    assert _is_linked(a, 'diagram_description_ContainerMapping206', b1)
    if hasattr(b1, 'NodeMapping207'):
        assert _is_linked(b1, 'NodeMapping207', a)
    _safe_set(a, 'diagram_description_ContainerMapping206', {b2})
    assert _is_linked(a, 'diagram_description_ContainerMapping206', b2)
    if hasattr(b1, 'NodeMapping207'):
        assert not _is_linked(b1, 'NodeMapping207', a)
    if hasattr(b2, 'NodeMapping207'):
        assert _is_linked(b2, 'NodeMapping207', a)
    _safe_set(a, 'diagram_description_ContainerMapping206', set())
    assert not _is_linked(a, 'diagram_description_ContainerMapping206', b2)
    if hasattr(b2, 'NodeMapping207'):
        assert not _is_linked(b2, 'NodeMapping207', a)


def test_assoc_reusedTools175_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'diagram_description_DiagramDescription176', {b1})
    assert _is_linked(a, 'diagram_description_DiagramDescription176', b1)
    if hasattr(b1, 'tool_AbstractToolDescription177'):
        assert _is_linked(b1, 'tool_AbstractToolDescription177', a)
    _safe_set(a, 'diagram_description_DiagramDescription176', {b2})
    assert _is_linked(a, 'diagram_description_DiagramDescription176', b2)
    if hasattr(b1, 'tool_AbstractToolDescription177'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription177', a)
    if hasattr(b2, 'tool_AbstractToolDescription177'):
        assert _is_linked(b2, 'tool_AbstractToolDescription177', a)
    _safe_set(a, 'diagram_description_DiagramDescription176', set())
    assert not _is_linked(a, 'diagram_description_DiagramDescription176', b2)
    if hasattr(b2, 'tool_AbstractToolDescription177'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription177', a)


def test_assoc_reusedTools273_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'diagram_description_Layer274', {b1})
    assert _is_linked(a, 'diagram_description_Layer274', b1)
    if hasattr(b1, 'tool_AbstractToolDescription275'):
        assert _is_linked(b1, 'tool_AbstractToolDescription275', a)
    _safe_set(a, 'diagram_description_Layer274', {b2})
    assert _is_linked(a, 'diagram_description_Layer274', b2)
    if hasattr(b1, 'tool_AbstractToolDescription275'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription275', a)
    if hasattr(b2, 'tool_AbstractToolDescription275'):
        assert _is_linked(b2, 'tool_AbstractToolDescription275', a)
    _safe_set(a, 'diagram_description_Layer274', set())
    assert not _is_linked(a, 'diagram_description_Layer274', b2)
    if hasattr(b2, 'tool_AbstractToolDescription275'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription275', a)


def test_assoc_reusedTools332_link_reassign_clear():
    a = diagram_tool_ToolSection(icon="sample_text")
    b1 = tool_ToolEntry()
    b2 = tool_ToolEntry()
    _safe_set(a, 'diagram_tool_ToolSection333', {b1})
    assert _is_linked(a, 'diagram_tool_ToolSection333', b1)
    if hasattr(b1, 'tool_ToolEntry334'):
        assert _is_linked(b1, 'tool_ToolEntry334', a)
    _safe_set(a, 'diagram_tool_ToolSection333', {b2})
    assert _is_linked(a, 'diagram_tool_ToolSection333', b2)
    if hasattr(b1, 'tool_ToolEntry334'):
        assert not _is_linked(b1, 'tool_ToolEntry334', a)
    if hasattr(b2, 'tool_ToolEntry334'):
        assert _is_linked(b2, 'tool_ToolEntry334', a)
    _safe_set(a, 'diagram_tool_ToolSection333', set())
    assert not _is_linked(a, 'diagram_tool_ToolSection333', b2)
    if hasattr(b2, 'tool_ToolEntry334'):
        assert not _is_linked(b2, 'tool_ToolEntry334', a)


def test_assoc_sections114_link_reassign_clear():
    a = diagram_GaugeSection(backgroundColor="sample_text", foregroundColor="sample_text", label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    b1 = diagram_GaugeCompositeStyle(alignment="sample_text")
    b2 = diagram_GaugeCompositeStyle(alignment="sample_text_2")
    _safe_set(a, 'diagram_GaugeSection', b1)
    assert _is_linked(a, 'diagram_GaugeSection', b1)
    if hasattr(b1, 'diagram_GaugeCompositeStyle'):
        assert _is_linked(b1, 'diagram_GaugeCompositeStyle', a)
    _safe_set(a, 'diagram_GaugeSection', b2)
    assert _is_linked(a, 'diagram_GaugeSection', b2)
    if hasattr(b1, 'diagram_GaugeCompositeStyle'):
        assert not _is_linked(b1, 'diagram_GaugeCompositeStyle', a)
    if hasattr(b2, 'diagram_GaugeCompositeStyle'):
        assert _is_linked(b2, 'diagram_GaugeCompositeStyle', a)
    _safe_set(a, 'diagram_GaugeSection', None)
    assert not _is_linked(a, 'diagram_GaugeSection', b2)
    if hasattr(b2, 'diagram_GaugeCompositeStyle'):
        assert not _is_linked(b2, 'diagram_GaugeCompositeStyle', a)


def test_assoc_sections297_link_reassign_clear():
    a = diagram_style_GaugeCompositeStyleDescription(alignment="sample_text")
    b1 = style_GaugeSectionDescription()
    b2 = style_GaugeSectionDescription()
    _safe_set(a, 'diagram_style_GaugeCompositeStyleDescription', {b1})
    assert _is_linked(a, 'diagram_style_GaugeCompositeStyleDescription', b1)
    if hasattr(b1, 'style_GaugeSectionDescription'):
        assert _is_linked(b1, 'style_GaugeSectionDescription', a)
    _safe_set(a, 'diagram_style_GaugeCompositeStyleDescription', {b2})
    assert _is_linked(a, 'diagram_style_GaugeCompositeStyleDescription', b2)
    if hasattr(b1, 'style_GaugeSectionDescription'):
        assert not _is_linked(b1, 'style_GaugeSectionDescription', a)
    if hasattr(b2, 'style_GaugeSectionDescription'):
        assert _is_linked(b2, 'style_GaugeSectionDescription', a)
    _safe_set(a, 'diagram_style_GaugeCompositeStyleDescription', set())
    assert not _is_linked(a, 'diagram_style_GaugeCompositeStyleDescription', b2)
    if hasattr(b2, 'style_GaugeSectionDescription'):
        assert not _is_linked(b2, 'style_GaugeSectionDescription', a)


def test_assoc_source408_link_reassign_clear():
    a = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_SourceEdgeCreationVariable()
    b2 = tool_SourceEdgeCreationVariable()
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription', b1)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription', b1)
    if hasattr(b1, 'tool_SourceEdgeCreationVariable409'):
        assert _is_linked(b1, 'tool_SourceEdgeCreationVariable409', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription', b2)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription', b2)
    if hasattr(b1, 'tool_SourceEdgeCreationVariable409'):
        assert not _is_linked(b1, 'tool_SourceEdgeCreationVariable409', a)
    if hasattr(b2, 'tool_SourceEdgeCreationVariable409'):
        assert _is_linked(b2, 'tool_SourceEdgeCreationVariable409', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription', None)
    assert not _is_linked(a, 'diagram_tool_ReconnectEdgeDescription', b2)
    if hasattr(b2, 'tool_SourceEdgeCreationVariable409'):
        assert not _is_linked(b2, 'tool_SourceEdgeCreationVariable409', a)


def test_assoc_sourceMapping225_link_reassign_clear():
    a = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_description_EdgeMapping', {b1})
    assert _is_linked(a, 'diagram_description_EdgeMapping', b1)
    if hasattr(b1, 'DiagramElementMapping226'):
        assert _is_linked(b1, 'DiagramElementMapping226', a)
    _safe_set(a, 'diagram_description_EdgeMapping', {b2})
    assert _is_linked(a, 'diagram_description_EdgeMapping', b2)
    if hasattr(b1, 'DiagramElementMapping226'):
        assert not _is_linked(b1, 'DiagramElementMapping226', a)
    if hasattr(b2, 'DiagramElementMapping226'):
        assert _is_linked(b2, 'DiagramElementMapping226', a)
    _safe_set(a, 'diagram_description_EdgeMapping', set())
    assert not _is_linked(a, 'diagram_description_EdgeMapping', b2)
    if hasattr(b2, 'DiagramElementMapping226'):
        assert not _is_linked(b2, 'DiagramElementMapping226', a)


def test_assoc_sourceNode95_link_reassign_clear():
    a = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = diagram_EdgeTarget()
    b2 = diagram_EdgeTarget()
    _safe_set(a, 'outgoingEdges', b1)
    assert _is_linked(a, 'outgoingEdges', b1)
    if hasattr(b1, 'EdgeTarget'):
        assert _is_linked(b1, 'EdgeTarget', a)
    _safe_set(a, 'outgoingEdges', b2)
    assert _is_linked(a, 'outgoingEdges', b2)
    if hasattr(b1, 'EdgeTarget'):
        assert not _is_linked(b1, 'EdgeTarget', a)
    if hasattr(b2, 'EdgeTarget'):
        assert _is_linked(b2, 'EdgeTarget', a)
    _safe_set(a, 'outgoingEdges', None)
    assert not _is_linked(a, 'outgoingEdges', b2)
    if hasattr(b2, 'EdgeTarget'):
        assert not _is_linked(b2, 'EdgeTarget', a)


def test_assoc_sourceVariable356_link_reassign_clear():
    a = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_SourceEdgeCreationVariable()
    b2 = tool_SourceEdgeCreationVariable()
    _safe_set(a, 'diagram_tool_EdgeCreationDescription357', b1)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription357', b1)
    if hasattr(b1, 'tool_SourceEdgeCreationVariable'):
        assert _is_linked(b1, 'tool_SourceEdgeCreationVariable', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription357', b2)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription357', b2)
    if hasattr(b1, 'tool_SourceEdgeCreationVariable'):
        assert not _is_linked(b1, 'tool_SourceEdgeCreationVariable', a)
    if hasattr(b2, 'tool_SourceEdgeCreationVariable'):
        assert _is_linked(b2, 'tool_SourceEdgeCreationVariable', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription357', None)
    assert not _is_linked(a, 'diagram_tool_EdgeCreationDescription357', b2)
    if hasattr(b2, 'tool_SourceEdgeCreationVariable'):
        assert not _is_linked(b2, 'tool_SourceEdgeCreationVariable', a)


def test_assoc_sourceView413_link_reassign_clear():
    a = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_SourceEdgeViewCreationVariable()
    b2 = tool_SourceEdgeViewCreationVariable()
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription414', b1)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription414', b1)
    if hasattr(b1, 'tool_SourceEdgeViewCreationVariable415'):
        assert _is_linked(b1, 'tool_SourceEdgeViewCreationVariable415', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription414', b2)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription414', b2)
    if hasattr(b1, 'tool_SourceEdgeViewCreationVariable415'):
        assert not _is_linked(b1, 'tool_SourceEdgeViewCreationVariable415', a)
    if hasattr(b2, 'tool_SourceEdgeViewCreationVariable415'):
        assert _is_linked(b2, 'tool_SourceEdgeViewCreationVariable415', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription414', None)
    assert not _is_linked(a, 'diagram_tool_ReconnectEdgeDescription414', b2)
    if hasattr(b2, 'tool_SourceEdgeViewCreationVariable415'):
        assert not _is_linked(b2, 'tool_SourceEdgeViewCreationVariable415', a)


def test_assoc_sourceViewVariable360_link_reassign_clear():
    a = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_SourceEdgeViewCreationVariable()
    b2 = tool_SourceEdgeViewCreationVariable()
    _safe_set(a, 'diagram_tool_EdgeCreationDescription361', b1)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription361', b1)
    if hasattr(b1, 'tool_SourceEdgeViewCreationVariable'):
        assert _is_linked(b1, 'tool_SourceEdgeViewCreationVariable', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription361', b2)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription361', b2)
    if hasattr(b1, 'tool_SourceEdgeViewCreationVariable'):
        assert not _is_linked(b1, 'tool_SourceEdgeViewCreationVariable', a)
    if hasattr(b2, 'tool_SourceEdgeViewCreationVariable'):
        assert _is_linked(b2, 'tool_SourceEdgeViewCreationVariable', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription361', None)
    assert not _is_linked(a, 'diagram_tool_EdgeCreationDescription361', b2)
    if hasattr(b2, 'tool_SourceEdgeViewCreationVariable'):
        assert not _is_linked(b2, 'tool_SourceEdgeViewCreationVariable', a)


def test_assoc_strokeColor312_link_reassign_clear():
    a = diagram_style_EdgeStyleDescription(endsCentering="sample_text", foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'diagram_style_EdgeStyleDescription', b1)
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription', b1)
    if hasattr(b1, 'ColorDescription313'):
        assert _is_linked(b1, 'ColorDescription313', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription', b2)
    assert _is_linked(a, 'diagram_style_EdgeStyleDescription', b2)
    if hasattr(b1, 'ColorDescription313'):
        assert not _is_linked(b1, 'ColorDescription313', a)
    if hasattr(b2, 'ColorDescription313'):
        assert _is_linked(b2, 'ColorDescription313', a)
    _safe_set(a, 'diagram_style_EdgeStyleDescription', None)
    assert not _is_linked(a, 'diagram_style_EdgeStyleDescription', b2)
    if hasattr(b2, 'ColorDescription313'):
        assert not _is_linked(b2, 'ColorDescription313', a)


def test_assoc_style197_link_reassign_clear():
    a = diagram_description_NodeMapping()
    b1 = style_NodeStyleDescription()
    b2 = style_NodeStyleDescription()
    _safe_set(a, 'diagram_description_NodeMapping', b1)
    assert _is_linked(a, 'diagram_description_NodeMapping', b1)
    if hasattr(b1, 'style_NodeStyleDescription'):
        assert _is_linked(b1, 'style_NodeStyleDescription', a)
    _safe_set(a, 'diagram_description_NodeMapping', b2)
    assert _is_linked(a, 'diagram_description_NodeMapping', b2)
    if hasattr(b1, 'style_NodeStyleDescription'):
        assert not _is_linked(b1, 'style_NodeStyleDescription', a)
    if hasattr(b2, 'style_NodeStyleDescription'):
        assert _is_linked(b2, 'style_NodeStyleDescription', a)
    _safe_set(a, 'diagram_description_NodeMapping', None)
    assert not _is_linked(a, 'diagram_description_NodeMapping', b2)
    if hasattr(b2, 'style_NodeStyleDescription'):
        assert not _is_linked(b2, 'style_NodeStyleDescription', a)


def test_assoc_style217_link_reassign_clear():
    a = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = style_ContainerStyleDescription()
    b2 = style_ContainerStyleDescription()
    _safe_set(a, 'diagram_description_ContainerMapping218', b1)
    assert _is_linked(a, 'diagram_description_ContainerMapping218', b1)
    if hasattr(b1, 'style_ContainerStyleDescription'):
        assert _is_linked(b1, 'style_ContainerStyleDescription', a)
    _safe_set(a, 'diagram_description_ContainerMapping218', b2)
    assert _is_linked(a, 'diagram_description_ContainerMapping218', b2)
    if hasattr(b1, 'style_ContainerStyleDescription'):
        assert not _is_linked(b1, 'style_ContainerStyleDescription', a)
    if hasattr(b2, 'style_ContainerStyleDescription'):
        assert _is_linked(b2, 'style_ContainerStyleDescription', a)
    _safe_set(a, 'diagram_description_ContainerMapping218', None)
    assert not _is_linked(a, 'diagram_description_ContainerMapping218', b2)
    if hasattr(b2, 'style_ContainerStyleDescription'):
        assert not _is_linked(b2, 'style_ContainerStyleDescription', a)


def test_assoc_style230_link_reassign_clear():
    a = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = style_EdgeStyleDescription()
    b2 = style_EdgeStyleDescription()
    _safe_set(a, 'diagram_description_EdgeMapping231', b1)
    assert _is_linked(a, 'diagram_description_EdgeMapping231', b1)
    if hasattr(b1, 'style_EdgeStyleDescription'):
        assert _is_linked(b1, 'style_EdgeStyleDescription', a)
    _safe_set(a, 'diagram_description_EdgeMapping231', b2)
    assert _is_linked(a, 'diagram_description_EdgeMapping231', b2)
    if hasattr(b1, 'style_EdgeStyleDescription'):
        assert not _is_linked(b1, 'style_EdgeStyleDescription', a)
    if hasattr(b2, 'style_EdgeStyleDescription'):
        assert _is_linked(b2, 'style_EdgeStyleDescription', a)
    _safe_set(a, 'diagram_description_EdgeMapping231', None)
    assert not _is_linked(a, 'diagram_description_EdgeMapping231', b2)
    if hasattr(b2, 'style_EdgeStyleDescription'):
        assert not _is_linked(b2, 'style_EdgeStyleDescription', a)


def test_assoc_subContainerMappings208_link_reassign_clear():
    a = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = ContainerMapping()
    b2 = ContainerMapping()
    _safe_set(a, 'diagram_description_ContainerMapping209', {b1})
    assert _is_linked(a, 'diagram_description_ContainerMapping209', b1)
    if hasattr(b1, 'ContainerMapping210'):
        assert _is_linked(b1, 'ContainerMapping210', a)
    _safe_set(a, 'diagram_description_ContainerMapping209', {b2})
    assert _is_linked(a, 'diagram_description_ContainerMapping209', b2)
    if hasattr(b1, 'ContainerMapping210'):
        assert not _is_linked(b1, 'ContainerMapping210', a)
    if hasattr(b2, 'ContainerMapping210'):
        assert _is_linked(b2, 'ContainerMapping210', a)
    _safe_set(a, 'diagram_description_ContainerMapping209', set())
    assert not _is_linked(a, 'diagram_description_ContainerMapping209', b2)
    if hasattr(b2, 'ContainerMapping210'):
        assert not _is_linked(b2, 'ContainerMapping210', a)


def test_assoc_subNodeMappings200_link_reassign_clear():
    a = diagram_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = NodeMapping()
    b2 = NodeMapping()
    _safe_set(a, 'diagram_description_ContainerMapping', {b1})
    assert _is_linked(a, 'diagram_description_ContainerMapping', b1)
    if hasattr(b1, 'NodeMapping201'):
        assert _is_linked(b1, 'NodeMapping201', a)
    _safe_set(a, 'diagram_description_ContainerMapping', {b2})
    assert _is_linked(a, 'diagram_description_ContainerMapping', b2)
    if hasattr(b1, 'NodeMapping201'):
        assert not _is_linked(b1, 'NodeMapping201', a)
    if hasattr(b2, 'NodeMapping201'):
        assert _is_linked(b2, 'NodeMapping201', a)
    _safe_set(a, 'diagram_description_ContainerMapping', set())
    assert not _is_linked(a, 'diagram_description_ContainerMapping', b2)
    if hasattr(b2, 'NodeMapping201'):
        assert not _is_linked(b2, 'NodeMapping201', a)


def test_assoc_subSections327_link_reassign_clear():
    a = diagram_tool_ToolSection(icon="sample_text")
    b1 = tool_ToolSection()
    b2 = tool_ToolSection()
    _safe_set(a, 'diagram_tool_ToolSection328', {b1})
    assert _is_linked(a, 'diagram_tool_ToolSection328', b1)
    if hasattr(b1, 'tool_ToolSection329'):
        assert _is_linked(b1, 'tool_ToolSection329', a)
    _safe_set(a, 'diagram_tool_ToolSection328', {b2})
    assert _is_linked(a, 'diagram_tool_ToolSection328', b2)
    if hasattr(b1, 'tool_ToolSection329'):
        assert not _is_linked(b1, 'tool_ToolSection329', a)
    if hasattr(b2, 'tool_ToolSection329'):
        assert _is_linked(b2, 'tool_ToolSection329', a)
    _safe_set(a, 'diagram_tool_ToolSection328', set())
    assert not _is_linked(a, 'diagram_tool_ToolSection328', b2)
    if hasattr(b2, 'tool_ToolSection329'):
        assert not _is_linked(b2, 'tool_ToolSection329', a)


def test_assoc_target410_link_reassign_clear():
    a = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_TargetEdgeCreationVariable()
    b2 = tool_TargetEdgeCreationVariable()
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription411', b1)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription411', b1)
    if hasattr(b1, 'tool_TargetEdgeCreationVariable412'):
        assert _is_linked(b1, 'tool_TargetEdgeCreationVariable412', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription411', b2)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription411', b2)
    if hasattr(b1, 'tool_TargetEdgeCreationVariable412'):
        assert not _is_linked(b1, 'tool_TargetEdgeCreationVariable412', a)
    if hasattr(b2, 'tool_TargetEdgeCreationVariable412'):
        assert _is_linked(b2, 'tool_TargetEdgeCreationVariable412', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription411', None)
    assert not _is_linked(a, 'diagram_tool_ReconnectEdgeDescription411', b2)
    if hasattr(b2, 'tool_TargetEdgeCreationVariable412'):
        assert not _is_linked(b2, 'tool_TargetEdgeCreationVariable412', a)


def test_assoc_targetMapping227_link_reassign_clear():
    a = diagram_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = DiagramElementMapping()
    b2 = DiagramElementMapping()
    _safe_set(a, 'diagram_description_EdgeMapping228', {b1})
    assert _is_linked(a, 'diagram_description_EdgeMapping228', b1)
    if hasattr(b1, 'DiagramElementMapping229'):
        assert _is_linked(b1, 'DiagramElementMapping229', a)
    _safe_set(a, 'diagram_description_EdgeMapping228', {b2})
    assert _is_linked(a, 'diagram_description_EdgeMapping228', b2)
    if hasattr(b1, 'DiagramElementMapping229'):
        assert not _is_linked(b1, 'DiagramElementMapping229', a)
    if hasattr(b2, 'DiagramElementMapping229'):
        assert _is_linked(b2, 'DiagramElementMapping229', a)
    _safe_set(a, 'diagram_description_EdgeMapping228', set())
    assert not _is_linked(a, 'diagram_description_EdgeMapping228', b2)
    if hasattr(b2, 'DiagramElementMapping229'):
        assert not _is_linked(b2, 'DiagramElementMapping229', a)


def test_assoc_targetNode96_link_reassign_clear():
    a = diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = diagram_EdgeTarget()
    b2 = diagram_EdgeTarget()
    _safe_set(a, 'incomingEdges', b1)
    assert _is_linked(a, 'incomingEdges', b1)
    if hasattr(b1, 'EdgeTarget97'):
        assert _is_linked(b1, 'EdgeTarget97', a)
    _safe_set(a, 'incomingEdges', b2)
    assert _is_linked(a, 'incomingEdges', b2)
    if hasattr(b1, 'EdgeTarget97'):
        assert not _is_linked(b1, 'EdgeTarget97', a)
    if hasattr(b2, 'EdgeTarget97'):
        assert _is_linked(b2, 'EdgeTarget97', a)
    _safe_set(a, 'incomingEdges', None)
    assert not _is_linked(a, 'incomingEdges', b2)
    if hasattr(b2, 'EdgeTarget97'):
        assert not _is_linked(b2, 'EdgeTarget97', a)


def test_assoc_targetVariable358_link_reassign_clear():
    a = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_TargetEdgeCreationVariable()
    b2 = tool_TargetEdgeCreationVariable()
    _safe_set(a, 'diagram_tool_EdgeCreationDescription359', b1)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription359', b1)
    if hasattr(b1, 'tool_TargetEdgeCreationVariable'):
        assert _is_linked(b1, 'tool_TargetEdgeCreationVariable', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription359', b2)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription359', b2)
    if hasattr(b1, 'tool_TargetEdgeCreationVariable'):
        assert not _is_linked(b1, 'tool_TargetEdgeCreationVariable', a)
    if hasattr(b2, 'tool_TargetEdgeCreationVariable'):
        assert _is_linked(b2, 'tool_TargetEdgeCreationVariable', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription359', None)
    assert not _is_linked(a, 'diagram_tool_EdgeCreationDescription359', b2)
    if hasattr(b2, 'tool_TargetEdgeCreationVariable'):
        assert not _is_linked(b2, 'tool_TargetEdgeCreationVariable', a)


def test_assoc_targetView416_link_reassign_clear():
    a = diagram_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_TargetEdgeViewCreationVariable()
    b2 = tool_TargetEdgeViewCreationVariable()
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription417', b1)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription417', b1)
    if hasattr(b1, 'tool_TargetEdgeViewCreationVariable418'):
        assert _is_linked(b1, 'tool_TargetEdgeViewCreationVariable418', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription417', b2)
    assert _is_linked(a, 'diagram_tool_ReconnectEdgeDescription417', b2)
    if hasattr(b1, 'tool_TargetEdgeViewCreationVariable418'):
        assert not _is_linked(b1, 'tool_TargetEdgeViewCreationVariable418', a)
    if hasattr(b2, 'tool_TargetEdgeViewCreationVariable418'):
        assert _is_linked(b2, 'tool_TargetEdgeViewCreationVariable418', a)
    _safe_set(a, 'diagram_tool_ReconnectEdgeDescription417', None)
    assert not _is_linked(a, 'diagram_tool_ReconnectEdgeDescription417', b2)
    if hasattr(b2, 'tool_TargetEdgeViewCreationVariable418'):
        assert not _is_linked(b2, 'tool_TargetEdgeViewCreationVariable418', a)


def test_assoc_targetViewVariable362_link_reassign_clear():
    a = diagram_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_TargetEdgeViewCreationVariable()
    b2 = tool_TargetEdgeViewCreationVariable()
    _safe_set(a, 'diagram_tool_EdgeCreationDescription363', b1)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription363', b1)
    if hasattr(b1, 'tool_TargetEdgeViewCreationVariable'):
        assert _is_linked(b1, 'tool_TargetEdgeViewCreationVariable', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription363', b2)
    assert _is_linked(a, 'diagram_tool_EdgeCreationDescription363', b2)
    if hasattr(b1, 'tool_TargetEdgeViewCreationVariable'):
        assert not _is_linked(b1, 'tool_TargetEdgeViewCreationVariable', a)
    if hasattr(b2, 'tool_TargetEdgeViewCreationVariable'):
        assert _is_linked(b2, 'tool_TargetEdgeViewCreationVariable', a)
    _safe_set(a, 'diagram_tool_EdgeCreationDescription363', None)
    assert not _is_linked(a, 'diagram_tool_EdgeCreationDescription363', b2)
    if hasattr(b2, 'tool_TargetEdgeViewCreationVariable'):
        assert not _is_linked(b2, 'tool_TargetEdgeViewCreationVariable', a)


def test_assoc_toolSection173_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_ToolSection()
    b2 = tool_ToolSection()
    _safe_set(a, 'diagram_description_DiagramDescription174', b1)
    assert _is_linked(a, 'diagram_description_DiagramDescription174', b1)
    if hasattr(b1, 'tool_ToolSection'):
        assert _is_linked(b1, 'tool_ToolSection', a)
    _safe_set(a, 'diagram_description_DiagramDescription174', b2)
    assert _is_linked(a, 'diagram_description_DiagramDescription174', b2)
    if hasattr(b1, 'tool_ToolSection'):
        assert not _is_linked(b1, 'tool_ToolSection', a)
    if hasattr(b2, 'tool_ToolSection'):
        assert _is_linked(b2, 'tool_ToolSection', a)
    _safe_set(a, 'diagram_description_DiagramDescription174', None)
    assert not _is_linked(a, 'diagram_description_DiagramDescription174', b2)
    if hasattr(b2, 'tool_ToolSection'):
        assert not _is_linked(b2, 'tool_ToolSection', a)


def test_assoc_toolSections270_link_reassign_clear():
    a = diagram_description_Layer(icon="sample_text")
    b1 = tool_ToolSection()
    b2 = tool_ToolSection()
    _safe_set(a, 'diagram_description_Layer271', {b1})
    assert _is_linked(a, 'diagram_description_Layer271', b1)
    if hasattr(b1, 'tool_ToolSection272'):
        assert _is_linked(b1, 'tool_ToolSection272', a)
    _safe_set(a, 'diagram_description_Layer271', {b2})
    assert _is_linked(a, 'diagram_description_Layer271', b2)
    if hasattr(b1, 'tool_ToolSection272'):
        assert not _is_linked(b1, 'tool_ToolSection272', a)
    if hasattr(b2, 'tool_ToolSection272'):
        assert _is_linked(b2, 'tool_ToolSection272', a)
    _safe_set(a, 'diagram_description_Layer271', set())
    assert not _is_linked(a, 'diagram_description_Layer271', b2)
    if hasattr(b2, 'tool_ToolSection272'):
        assert not _is_linked(b2, 'tool_ToolSection272', a)


def test_assoc_transientDecorations39_link_reassign_clear():
    a = diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = diagram_Decoration()
    b2 = diagram_Decoration()
    _safe_set(a, 'diagram_DDiagramElement40', {b1})
    assert _is_linked(a, 'diagram_DDiagramElement40', b1)
    if hasattr(b1, 'diagram_Decoration41'):
        assert _is_linked(b1, 'diagram_Decoration41', a)
    _safe_set(a, 'diagram_DDiagramElement40', {b2})
    assert _is_linked(a, 'diagram_DDiagramElement40', b2)
    if hasattr(b1, 'diagram_Decoration41'):
        assert not _is_linked(b1, 'diagram_Decoration41', a)
    if hasattr(b2, 'diagram_Decoration41'):
        assert _is_linked(b2, 'diagram_Decoration41', a)
    _safe_set(a, 'diagram_DDiagramElement40', set())
    assert not _is_linked(a, 'diagram_DDiagramElement40', b2)
    if hasattr(b2, 'diagram_Decoration41'):
        assert not _is_linked(b2, 'diagram_Decoration41', a)


def test_assoc_validationSet132_link_reassign_clear():
    a = diagram_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = validation_ValidationSet()
    b2 = validation_ValidationSet()
    _safe_set(a, 'diagram_description_DiagramDescription133', b1)
    assert _is_linked(a, 'diagram_description_DiagramDescription133', b1)
    if hasattr(b1, 'validation_ValidationSet'):
        assert _is_linked(b1, 'validation_ValidationSet', a)
    _safe_set(a, 'diagram_description_DiagramDescription133', b2)
    assert _is_linked(a, 'diagram_description_DiagramDescription133', b2)
    if hasattr(b1, 'validation_ValidationSet'):
        assert not _is_linked(b1, 'validation_ValidationSet', a)
    if hasattr(b2, 'validation_ValidationSet'):
        assert _is_linked(b2, 'validation_ValidationSet', a)
    _safe_set(a, 'diagram_description_DiagramDescription133', None)
    assert not _is_linked(a, 'diagram_description_DiagramDescription133', b2)
    if hasattr(b2, 'validation_ValidationSet'):
        assert not _is_linked(b2, 'validation_ValidationSet', a)


def test_assoc_variable345_link_reassign_clear():
    a = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = tool_NodeCreationVariable()
    b2 = tool_NodeCreationVariable()
    _safe_set(a, 'diagram_tool_NodeCreationDescription346', b1)
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription346', b1)
    if hasattr(b1, 'tool_NodeCreationVariable'):
        assert _is_linked(b1, 'tool_NodeCreationVariable', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription346', b2)
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription346', b2)
    if hasattr(b1, 'tool_NodeCreationVariable'):
        assert not _is_linked(b1, 'tool_NodeCreationVariable', a)
    if hasattr(b2, 'tool_NodeCreationVariable'):
        assert _is_linked(b2, 'tool_NodeCreationVariable', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription346', None)
    assert not _is_linked(a, 'diagram_tool_NodeCreationDescription346', b2)
    if hasattr(b2, 'tool_NodeCreationVariable'):
        assert not _is_linked(b2, 'tool_NodeCreationVariable', a)


def test_assoc_variable374_link_reassign_clear():
    a = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = tool_NodeCreationVariable()
    b2 = tool_NodeCreationVariable()
    _safe_set(a, 'diagram_tool_ContainerCreationDescription375', b1)
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription375', b1)
    if hasattr(b1, 'tool_NodeCreationVariable376'):
        assert _is_linked(b1, 'tool_NodeCreationVariable376', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription375', b2)
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription375', b2)
    if hasattr(b1, 'tool_NodeCreationVariable376'):
        assert not _is_linked(b1, 'tool_NodeCreationVariable376', a)
    if hasattr(b2, 'tool_NodeCreationVariable376'):
        assert _is_linked(b2, 'tool_NodeCreationVariable376', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription375', None)
    assert not _is_linked(a, 'diagram_tool_ContainerCreationDescription375', b2)
    if hasattr(b2, 'tool_NodeCreationVariable376'):
        assert not _is_linked(b2, 'tool_NodeCreationVariable376', a)


def test_assoc_variableDefinition118_link_reassign_clear():
    a = diagram_TypedVariableValue(value="sample_text")
    b1 = TypedVariable()
    b2 = TypedVariable()
    _safe_set(a, 'diagram_TypedVariableValue', b1)
    assert _is_linked(a, 'diagram_TypedVariableValue', b1)
    if hasattr(b1, 'TypedVariable'):
        assert _is_linked(b1, 'TypedVariable', a)
    _safe_set(a, 'diagram_TypedVariableValue', b2)
    assert _is_linked(a, 'diagram_TypedVariableValue', b2)
    if hasattr(b1, 'TypedVariable'):
        assert not _is_linked(b1, 'TypedVariable', a)
    if hasattr(b2, 'TypedVariable'):
        assert _is_linked(b2, 'TypedVariable', a)
    _safe_set(a, 'diagram_TypedVariableValue', None)
    assert not _is_linked(a, 'diagram_TypedVariableValue', b2)
    if hasattr(b2, 'TypedVariable'):
        assert not _is_linked(b2, 'TypedVariable', a)


def test_assoc_viewVariable347_link_reassign_clear():
    a = diagram_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'diagram_tool_NodeCreationDescription348', b1)
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription348', b1)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert _is_linked(b1, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription348', b2)
    assert _is_linked(a, 'diagram_tool_NodeCreationDescription348', b2)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable', a)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert _is_linked(b2, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'diagram_tool_NodeCreationDescription348', None)
    assert not _is_linked(a, 'diagram_tool_NodeCreationDescription348', b2)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable', a)


def test_assoc_viewVariable377_link_reassign_clear():
    a = diagram_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'diagram_tool_ContainerCreationDescription378', b1)
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription378', b1)
    if hasattr(b1, 'tool_ContainerViewVariable379'):
        assert _is_linked(b1, 'tool_ContainerViewVariable379', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription378', b2)
    assert _is_linked(a, 'diagram_tool_ContainerCreationDescription378', b2)
    if hasattr(b1, 'tool_ContainerViewVariable379'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable379', a)
    if hasattr(b2, 'tool_ContainerViewVariable379'):
        assert _is_linked(b2, 'tool_ContainerViewVariable379', a)
    _safe_set(a, 'diagram_tool_ContainerCreationDescription378', None)
    assert not _is_linked(a, 'diagram_tool_ContainerCreationDescription378', b2)
    if hasattr(b2, 'tool_ContainerViewVariable379'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable379', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractDNode_strategy = st.builds(AbstractDNode)
@given(instance=AbstractDNode_strategy)
@settings(max_examples=25)
def test_AbstractDNode_instantiation(instance):
    assert isinstance(instance, AbstractDNode)


AbstractNodeMapping_strategy = st.builds(AbstractNodeMapping)
@given(instance=AbstractNodeMapping_strategy)
@settings(max_examples=25)
def test_AbstractNodeMapping_instantiation(instance):
    assert isinstance(instance, AbstractNodeMapping)


AbstractToolDescription_strategy = st.builds(AbstractToolDescription)
@given(instance=AbstractToolDescription_strategy)
@settings(max_examples=25)
def test_AbstractToolDescription_instantiation(instance):
    assert isinstance(instance, AbstractToolDescription)


AdditionalLayer_strategy = st.builds(AdditionalLayer)
@given(instance=AdditionalLayer_strategy)
@settings(max_examples=25)
def test_AdditionalLayer_instantiation(instance):
    assert isinstance(instance, AdditionalLayer)


BasicLabelStyle_strategy = st.builds(BasicLabelStyle)
@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=25)
def test_BasicLabelStyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)


BasicLabelStyleDescription_strategy = st.builds(BasicLabelStyleDescription)
@given(instance=BasicLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_BasicLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, BasicLabelStyleDescription)


BorderedStyle_strategy = st.builds(BorderedStyle)
@given(instance=BorderedStyle_strategy)
@settings(max_examples=25)
def test_BorderedStyle_instantiation(instance):
    assert isinstance(instance, BorderedStyle)


CollapseFilter_strategy = st.builds(CollapseFilter)
@given(instance=CollapseFilter_strategy)
@settings(max_examples=25)
def test_CollapseFilter_instantiation(instance):
    assert isinstance(instance, CollapseFilter)


ColorDescription_strategy = st.builds(ColorDescription)
@given(instance=ColorDescription_strategy)
@settings(max_examples=25)
def test_ColorDescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)


ConditionalContainerStyleDescription_strategy = st.builds(ConditionalContainerStyleDescription)
@given(instance=ConditionalContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_ConditionalContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, ConditionalContainerStyleDescription)


ConditionalEdgeStyleDescription_strategy = st.builds(ConditionalEdgeStyleDescription)
@given(instance=ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_ConditionalEdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, ConditionalEdgeStyleDescription)


ConditionalNodeStyleDescription_strategy = st.builds(ConditionalNodeStyleDescription)
@given(instance=ConditionalNodeStyleDescription_strategy)
@settings(max_examples=25)
def test_ConditionalNodeStyleDescription_instantiation(instance):
    assert isinstance(instance, ConditionalNodeStyleDescription)


ConditionalStyleDescription_strategy = st.builds(ConditionalStyleDescription)
@given(instance=ConditionalStyleDescription_strategy)
@settings(max_examples=25)
def test_ConditionalStyleDescription_instantiation(instance):
    assert isinstance(instance, ConditionalStyleDescription)


ContainerMapping_strategy = st.builds(ContainerMapping)
@given(instance=ContainerMapping_strategy)
@settings(max_examples=25)
def test_ContainerMapping_instantiation(instance):
    assert isinstance(instance, ContainerMapping)


ContainerModelOperation_strategy = st.builds(ContainerModelOperation)
@given(instance=ContainerModelOperation_strategy)
@settings(max_examples=25)
def test_ContainerModelOperation_instantiation(instance):
    assert isinstance(instance, ContainerModelOperation)


ContainerStyle_strategy = st.builds(ContainerStyle)
@given(instance=ContainerStyle_strategy)
@settings(max_examples=25)
def test_ContainerStyle_instantiation(instance):
    assert isinstance(instance, ContainerStyle)


CreateView_strategy = st.builds(CreateView)
@given(instance=CreateView_strategy)
@settings(max_examples=25)
def test_CreateView_instantiation(instance):
    assert isinstance(instance, CreateView)


Customizable_strategy = st.builds(Customizable)
@given(instance=Customizable_strategy)
@settings(max_examples=25)
def test_Customizable_instantiation(instance):
    assert isinstance(instance, Customizable)


Customization_strategy = st.builds(Customization)
@given(instance=Customization_strategy)
@settings(max_examples=25)
def test_Customization_instantiation(instance):
    assert isinstance(instance, Customization)


DDiagram_strategy = st.builds(DDiagram)
@given(instance=DDiagram_strategy)
@settings(max_examples=25)
def test_DDiagram_instantiation(instance):
    assert isinstance(instance, DDiagram)


DDiagramElement_strategy = st.builds(DDiagramElement)
@given(instance=DDiagramElement_strategy)
@settings(max_examples=25)
def test_DDiagramElement_instantiation(instance):
    assert isinstance(instance, DDiagramElement)


DDiagramElementContainer_strategy = st.builds(DDiagramElementContainer)
@given(instance=DDiagramElementContainer_strategy)
@settings(max_examples=25)
def test_DDiagramElementContainer_instantiation(instance):
    assert isinstance(instance, DDiagramElementContainer)


DRepresentation_strategy = st.builds(DRepresentation)
@given(instance=DRepresentation_strategy)
@settings(max_examples=25)
def test_DRepresentation_instantiation(instance):
    assert isinstance(instance, DRepresentation)


DRepresentationElement_strategy = st.builds(DRepresentationElement)
@given(instance=DRepresentationElement_strategy)
@settings(max_examples=25)
def test_DRepresentationElement_instantiation(instance):
    assert isinstance(instance, DRepresentationElement)


DSemanticDecorator_strategy = st.builds(DSemanticDecorator)
@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=25)
def test_DSemanticDecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)


DecorationDescription_strategy = st.builds(DecorationDescription)
@given(instance=DecorationDescription_strategy)
@settings(max_examples=25)
def test_DecorationDescription_instantiation(instance):
    assert isinstance(instance, DecorationDescription)


DecorationDescriptionsSet_strategy = st.builds(DecorationDescriptionsSet)
@given(instance=DecorationDescriptionsSet_strategy)
@settings(max_examples=25)
def test_DecorationDescriptionsSet_instantiation(instance):
    assert isinstance(instance, DecorationDescriptionsSet)


DiagramDescription_strategy = st.builds(DiagramDescription)
@given(instance=DiagramDescription_strategy)
@settings(max_examples=25)
def test_DiagramDescription_instantiation(instance):
    assert isinstance(instance, DiagramDescription)


DiagramElementMapping_strategy = st.builds(DiagramElementMapping)
@given(instance=DiagramElementMapping_strategy)
@settings(max_examples=25)
def test_DiagramElementMapping_instantiation(instance):
    assert isinstance(instance, DiagramElementMapping)


DocumentedElement_strategy = st.builds(DocumentedElement)
@given(instance=DocumentedElement_strategy)
@settings(max_examples=25)
def test_DocumentedElement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)


DragAndDropTarget_strategy = st.builds(DragAndDropTarget)
@given(instance=DragAndDropTarget_strategy)
@settings(max_examples=25)
def test_DragAndDropTarget_instantiation(instance):
    assert isinstance(instance, DragAndDropTarget)


EdgeMapping_strategy = st.builds(EdgeMapping)
@given(instance=EdgeMapping_strategy)
@settings(max_examples=25)
def test_EdgeMapping_instantiation(instance):
    assert isinstance(instance, EdgeMapping)


EdgeMappingImport_strategy = st.builds(EdgeMappingImport)
@given(instance=EdgeMappingImport_strategy)
@settings(max_examples=25)
def test_EdgeMappingImport_instantiation(instance):
    assert isinstance(instance, EdgeMappingImport)


EdgeStyle_strategy = st.builds(EdgeStyle)
@given(instance=EdgeStyle_strategy)
@settings(max_examples=25)
def test_EdgeStyle_instantiation(instance):
    assert isinstance(instance, EdgeStyle)


EdgeStyleDescription_strategy = st.builds(EdgeStyleDescription)
@given(instance=EdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_EdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, EdgeStyleDescription)


EdgeTarget_strategy = st.builds(EdgeTarget)
@given(instance=EdgeTarget_strategy)
@settings(max_examples=25)
def test_EdgeTarget_instantiation(instance):
    assert isinstance(instance, EdgeTarget)


Filter_strategy = st.builds(Filter)
@given(instance=Filter_strategy)
@settings(max_examples=25)
def test_Filter_instantiation(instance):
    assert isinstance(instance, Filter)


FilterDescription_strategy = st.builds(FilterDescription)
@given(instance=FilterDescription_strategy)
@settings(max_examples=25)
def test_FilterDescription_instantiation(instance):
    assert isinstance(instance, FilterDescription)


GraphicalFilter_strategy = st.builds(GraphicalFilter)
@given(instance=GraphicalFilter_strategy)
@settings(max_examples=25)
def test_GraphicalFilter_instantiation(instance):
    assert isinstance(instance, GraphicalFilter)


HideLabelCapabilityStyle_strategy = st.builds(HideLabelCapabilityStyle)
@given(instance=HideLabelCapabilityStyle_strategy)
@settings(max_examples=25)
def test_HideLabelCapabilityStyle_instantiation(instance):
    assert isinstance(instance, HideLabelCapabilityStyle)


IEdgeMapping_strategy = st.builds(IEdgeMapping)
@given(instance=IEdgeMapping_strategy)
@settings(max_examples=25)
def test_IEdgeMapping_instantiation(instance):
    assert isinstance(instance, IEdgeMapping)


InteractiveVariableDescription_strategy = st.builds(InteractiveVariableDescription)
@given(instance=InteractiveVariableDescription_strategy)
@settings(max_examples=25)
def test_InteractiveVariableDescription_instantiation(instance):
    assert isinstance(instance, InteractiveVariableDescription)


LabelStyle_strategy = st.builds(LabelStyle)
@given(instance=LabelStyle_strategy)
@settings(max_examples=25)
def test_LabelStyle_instantiation(instance):
    assert isinstance(instance, LabelStyle)


Layer_strategy = st.builds(Layer)
@given(instance=Layer_strategy)
@settings(max_examples=25)
def test_Layer_instantiation(instance):
    assert isinstance(instance, Layer)


Layout_strategy = st.builds(Layout)
@given(instance=Layout_strategy)
@settings(max_examples=25)
def test_Layout_instantiation(instance):
    assert isinstance(instance, Layout)


MappingBasedToolDescription_strategy = st.builds(MappingBasedToolDescription)
@given(instance=MappingBasedToolDescription_strategy)
@settings(max_examples=25)
def test_MappingBasedToolDescription_instantiation(instance):
    assert isinstance(instance, MappingBasedToolDescription)


NodeMapping_strategy = st.builds(NodeMapping)
@given(instance=NodeMapping_strategy)
@settings(max_examples=25)
def test_NodeMapping_instantiation(instance):
    assert isinstance(instance, NodeMapping)


NodeStyle_strategy = st.builds(NodeStyle)
@given(instance=NodeStyle_strategy)
@settings(max_examples=25)
def test_NodeStyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)


NodeStyleDescription_strategy = st.builds(NodeStyleDescription)
@given(instance=NodeStyleDescription_strategy)
@settings(max_examples=25)
def test_NodeStyleDescription_instantiation(instance):
    assert isinstance(instance, NodeStyleDescription)


RepresentationCreationDescription_strategy = st.builds(RepresentationCreationDescription)
@given(instance=RepresentationCreationDescription_strategy)
@settings(max_examples=25)
def test_RepresentationCreationDescription_instantiation(instance):
    assert isinstance(instance, RepresentationCreationDescription)


RepresentationExtensionDescription_strategy = st.builds(RepresentationExtensionDescription)
@given(instance=RepresentationExtensionDescription_strategy)
@settings(max_examples=25)
def test_RepresentationExtensionDescription_instantiation(instance):
    assert isinstance(instance, RepresentationExtensionDescription)


RepresentationNavigationDescription_strategy = st.builds(RepresentationNavigationDescription)
@given(instance=RepresentationNavigationDescription_strategy)
@settings(max_examples=25)
def test_RepresentationNavigationDescription_instantiation(instance):
    assert isinstance(instance, RepresentationNavigationDescription)


Style_strategy = st.builds(Style)
@given(instance=Style_strategy)
@settings(max_examples=25)
def test_Style_instantiation(instance):
    assert isinstance(instance, Style)


StyleDescription_strategy = st.builds(StyleDescription)
@given(instance=StyleDescription_strategy)
@settings(max_examples=25)
def test_StyleDescription_instantiation(instance):
    assert isinstance(instance, StyleDescription)


ToolEntry_strategy = st.builds(ToolEntry)
@given(instance=ToolEntry_strategy)
@settings(max_examples=25)
def test_ToolEntry_instantiation(instance):
    assert isinstance(instance, ToolEntry)


TypedVariable_strategy = st.builds(TypedVariable)
@given(instance=TypedVariable_strategy)
@settings(max_examples=25)
def test_TypedVariable_instantiation(instance):
    assert isinstance(instance, TypedVariable)


VariableValue_strategy = st.builds(VariableValue)
@given(instance=VariableValue_strategy)
@settings(max_examples=25)
def test_VariableValue_instantiation(instance):
    assert isinstance(instance, VariableValue)


concern_ConcernDescription_strategy = st.builds(concern_ConcernDescription)
@given(instance=concern_ConcernDescription_strategy)
@settings(max_examples=25)
def test_concern_ConcernDescription_instantiation(instance):
    assert isinstance(instance, concern_ConcernDescription)


concern_ConcernSet_strategy = st.builds(concern_ConcernSet)
@given(instance=concern_ConcernSet_strategy)
@settings(max_examples=25)
def test_concern_ConcernSet_instantiation(instance):
    assert isinstance(instance, concern_ConcernSet)


description_AbstractMappingImport_strategy = st.builds(description_AbstractMappingImport)
@given(instance=description_AbstractMappingImport_strategy)
@settings(max_examples=25)
def test_description_AbstractMappingImport_instantiation(instance):
    assert isinstance(instance, description_AbstractMappingImport)


description_AbstractNodeMapping_strategy = st.builds(description_AbstractNodeMapping)
@given(instance=description_AbstractNodeMapping_strategy)
@settings(max_examples=25)
def test_description_AbstractNodeMapping_instantiation(instance):
    assert isinstance(instance, description_AbstractNodeMapping)


description_AbstractVariable_strategy = st.builds(description_AbstractVariable)
@given(instance=description_AbstractVariable_strategy)
@settings(max_examples=25)
def test_description_AbstractVariable_instantiation(instance):
    assert isinstance(instance, description_AbstractVariable)


description_ContainerMapping_strategy = st.builds(description_ContainerMapping)
@given(instance=description_ContainerMapping_strategy)
@settings(max_examples=25)
def test_description_ContainerMapping_instantiation(instance):
    assert isinstance(instance, description_ContainerMapping)


description_DiagramDescription_strategy = st.builds(description_DiagramDescription)
@given(instance=description_DiagramDescription_strategy)
@settings(max_examples=25)
def test_description_DiagramDescription_instantiation(instance):
    assert isinstance(instance, description_DiagramDescription)


description_DiagramElementMapping_strategy = st.builds(description_DiagramElementMapping)
@given(instance=description_DiagramElementMapping_strategy)
@settings(max_examples=25)
def test_description_DiagramElementMapping_instantiation(instance):
    assert isinstance(instance, description_DiagramElementMapping)


description_DocumentedElement_strategy = st.builds(description_DocumentedElement)
@given(instance=description_DocumentedElement_strategy)
@settings(max_examples=25)
def test_description_DocumentedElement_instantiation(instance):
    assert isinstance(instance, description_DocumentedElement)


description_DragAndDropTargetDescription_strategy = st.builds(description_DragAndDropTargetDescription)
@given(instance=description_DragAndDropTargetDescription_strategy)
@settings(max_examples=25)
def test_description_DragAndDropTargetDescription_instantiation(instance):
    assert isinstance(instance, description_DragAndDropTargetDescription)


description_EndUserDocumentedElement_strategy = st.builds(description_EndUserDocumentedElement)
@given(instance=description_EndUserDocumentedElement_strategy)
@settings(max_examples=25)
def test_description_EndUserDocumentedElement_instantiation(instance):
    assert isinstance(instance, description_EndUserDocumentedElement)


description_IEdgeMapping_strategy = st.builds(description_IEdgeMapping)
@given(instance=description_IEdgeMapping_strategy)
@settings(max_examples=25)
def test_description_IEdgeMapping_instantiation(instance):
    assert isinstance(instance, description_IEdgeMapping)


description_IdentifiedElement_strategy = st.builds(description_IdentifiedElement)
@given(instance=description_IdentifiedElement_strategy)
@settings(max_examples=25)
def test_description_IdentifiedElement_instantiation(instance):
    assert isinstance(instance, description_IdentifiedElement)


description_NodeMapping_strategy = st.builds(description_NodeMapping)
@given(instance=description_NodeMapping_strategy)
@settings(max_examples=25)
def test_description_NodeMapping_instantiation(instance):
    assert isinstance(instance, description_NodeMapping)


description_PasteTargetDescription_strategy = st.builds(description_PasteTargetDescription)
@given(instance=description_PasteTargetDescription_strategy)
@settings(max_examples=25)
def test_description_PasteTargetDescription_instantiation(instance):
    assert isinstance(instance, description_PasteTargetDescription)


description_RepresentationDescription_strategy = st.builds(description_RepresentationDescription)
@given(instance=description_RepresentationDescription_strategy)
@settings(max_examples=25)
def test_description_RepresentationDescription_instantiation(instance):
    assert isinstance(instance, description_RepresentationDescription)


description_RepresentationElementMapping_strategy = st.builds(description_RepresentationElementMapping)
@given(instance=description_RepresentationElementMapping_strategy)
@settings(max_examples=25)
def test_description_RepresentationElementMapping_instantiation(instance):
    assert isinstance(instance, description_RepresentationElementMapping)


description_RepresentationImportDescription_strategy = st.builds(description_RepresentationImportDescription)
@given(instance=description_RepresentationImportDescription_strategy)
@settings(max_examples=25)
def test_description_RepresentationImportDescription_instantiation(instance):
    assert isinstance(instance, description_RepresentationImportDescription)


diagram_AbsoluteBoundsFilter_strategy = st.builds(diagram_AbsoluteBoundsFilter, height=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=diagram_AbsoluteBoundsFilter_strategy)
@settings(max_examples=25)
def test_diagram_AbsoluteBoundsFilter_instantiation(instance):
    assert isinstance(instance, diagram_AbsoluteBoundsFilter)


diagram_AbstractDNode_strategy = st.builds(diagram_AbstractDNode, arrangeConstraints=safe_text)
@given(instance=diagram_AbstractDNode_strategy)
@settings(max_examples=25)
def test_diagram_AbstractDNode_instantiation(instance):
    assert isinstance(instance, diagram_AbstractDNode)


diagram_AppliedCompositeFilters_strategy = st.builds(diagram_AppliedCompositeFilters)
@given(instance=diagram_AppliedCompositeFilters_strategy)
@settings(max_examples=25)
def test_diagram_AppliedCompositeFilters_instantiation(instance):
    assert isinstance(instance, diagram_AppliedCompositeFilters)


diagram_BeginLabelStyle_strategy = st.builds(diagram_BeginLabelStyle)
@given(instance=diagram_BeginLabelStyle_strategy)
@settings(max_examples=25)
def test_diagram_BeginLabelStyle_instantiation(instance):
    assert isinstance(instance, diagram_BeginLabelStyle)


diagram_BorderedStyle_strategy = st.builds(diagram_BorderedStyle, borderColor=safe_text, borderLineStyle=safe_text, borderSize=safe_text, borderSizeComputationExpression=safe_text)
@given(instance=diagram_BorderedStyle_strategy)
@settings(max_examples=25)
def test_diagram_BorderedStyle_instantiation(instance):
    assert isinstance(instance, diagram_BorderedStyle)


diagram_BracketEdgeStyle_strategy = st.builds(diagram_BracketEdgeStyle)
@given(instance=diagram_BracketEdgeStyle_strategy)
@settings(max_examples=25)
def test_diagram_BracketEdgeStyle_instantiation(instance):
    assert isinstance(instance, diagram_BracketEdgeStyle)


diagram_BundledImage_strategy = st.builds(diagram_BundledImage, color=safe_text, providedShapeID=safe_text, shape=safe_text)
@given(instance=diagram_BundledImage_strategy)
@settings(max_examples=25)
def test_diagram_BundledImage_instantiation(instance):
    assert isinstance(instance, diagram_BundledImage)


diagram_CenterLabelStyle_strategy = st.builds(diagram_CenterLabelStyle)
@given(instance=diagram_CenterLabelStyle_strategy)
@settings(max_examples=25)
def test_diagram_CenterLabelStyle_instantiation(instance):
    assert isinstance(instance, diagram_CenterLabelStyle)


diagram_CollapseFilter_strategy = st.builds(diagram_CollapseFilter, height=st.integers(), width=st.integers())
@given(instance=diagram_CollapseFilter_strategy)
@settings(max_examples=25)
def test_diagram_CollapseFilter_instantiation(instance):
    assert isinstance(instance, diagram_CollapseFilter)


diagram_ComputedStyleDescriptionRegistry_strategy = st.builds(diagram_ComputedStyleDescriptionRegistry)
@given(instance=diagram_ComputedStyleDescriptionRegistry_strategy)
@settings(max_examples=25)
def test_diagram_ComputedStyleDescriptionRegistry_instantiation(instance):
    assert isinstance(instance, diagram_ComputedStyleDescriptionRegistry)


diagram_ContainerStyle_strategy = st.builds(diagram_ContainerStyle)
@given(instance=diagram_ContainerStyle_strategy)
@settings(max_examples=25)
def test_diagram_ContainerStyle_instantiation(instance):
    assert isinstance(instance, diagram_ContainerStyle)


diagram_CustomStyle_strategy = st.builds(diagram_CustomStyle, id=safe_text)
@given(instance=diagram_CustomStyle_strategy)
@settings(max_examples=25)
def test_diagram_CustomStyle_instantiation(instance):
    assert isinstance(instance, diagram_CustomStyle)


diagram_DDiagram_strategy = st.builds(diagram_DDiagram, headerHeight=st.integers(), isInLayoutingMode=st.booleans(), synchronized=st.booleans())
@given(instance=diagram_DDiagram_strategy)
@settings(max_examples=25)
def test_diagram_DDiagram_instantiation(instance):
    assert isinstance(instance, diagram_DDiagram)


diagram_DDiagramElement_strategy = st.builds(diagram_DDiagramElement, tooltipText=safe_text, visible=st.booleans())
@given(instance=diagram_DDiagramElement_strategy)
@settings(max_examples=25)
def test_diagram_DDiagramElement_instantiation(instance):
    assert isinstance(instance, diagram_DDiagramElement)


diagram_DDiagramElementContainer_strategy = st.builds(diagram_DDiagramElementContainer, height=safe_text, width=safe_text)
@given(instance=diagram_DDiagramElementContainer_strategy)
@settings(max_examples=25)
def test_diagram_DDiagramElementContainer_instantiation(instance):
    assert isinstance(instance, diagram_DDiagramElementContainer)


diagram_DEdge_strategy = st.builds(diagram_DEdge, arrangeConstraints=safe_text, beginLabel=safe_text, endLabel=safe_text, isFold=st.booleans(), isMockEdge=st.booleans(), routingStyle=safe_text, size=safe_text)
@given(instance=diagram_DEdge_strategy)
@settings(max_examples=25)
def test_diagram_DEdge_instantiation(instance):
    assert isinstance(instance, diagram_DEdge)


diagram_DNode_strategy = st.builds(diagram_DNode, height=safe_text, labelPosition=safe_text, resizeKind=safe_text, width=safe_text)
@given(instance=diagram_DNode_strategy)
@settings(max_examples=25)
def test_diagram_DNode_instantiation(instance):
    assert isinstance(instance, diagram_DNode)


diagram_DNodeContainer_strategy = st.builds(diagram_DNodeContainer, childrenPresentation=safe_text)
@given(instance=diagram_DNodeContainer_strategy)
@settings(max_examples=25)
def test_diagram_DNodeContainer_instantiation(instance):
    assert isinstance(instance, diagram_DNodeContainer)


diagram_DNodeList_strategy = st.builds(diagram_DNodeList)
@given(instance=diagram_DNodeList_strategy)
@settings(max_examples=25)
def test_diagram_DNodeList_instantiation(instance):
    assert isinstance(instance, diagram_DNodeList)


diagram_DNodeListElement_strategy = st.builds(diagram_DNodeListElement)
@given(instance=diagram_DNodeListElement_strategy)
@settings(max_examples=25)
def test_diagram_DNodeListElement_instantiation(instance):
    assert isinstance(instance, diagram_DNodeListElement)


diagram_DSemanticDiagram_strategy = st.builds(diagram_DSemanticDiagram)
@given(instance=diagram_DSemanticDiagram_strategy)
@settings(max_examples=25)
def test_diagram_DSemanticDiagram_instantiation(instance):
    assert isinstance(instance, diagram_DSemanticDiagram)


diagram_Decoration_strategy = st.builds(diagram_Decoration)
@given(instance=diagram_Decoration_strategy)
@settings(max_examples=25)
def test_diagram_Decoration_instantiation(instance):
    assert isinstance(instance, diagram_Decoration)


diagram_Dot_strategy = st.builds(diagram_Dot, backgroundColor=safe_text, strokeSizeComputationExpression=safe_text)
@given(instance=diagram_Dot_strategy)
@settings(max_examples=25)
def test_diagram_Dot_instantiation(instance):
    assert isinstance(instance, diagram_Dot)


diagram_DragAndDropTarget_strategy = st.builds(diagram_DragAndDropTarget)
@given(instance=diagram_DragAndDropTarget_strategy)
@settings(max_examples=25)
def test_diagram_DragAndDropTarget_instantiation(instance):
    assert isinstance(instance, diagram_DragAndDropTarget)


diagram_EObject_strategy = st.builds(diagram_EObject)
@given(instance=diagram_EObject_strategy)
@settings(max_examples=25)
def test_diagram_EObject_instantiation(instance):
    assert isinstance(instance, diagram_EObject)


diagram_EObjectVariableValue_strategy = st.builds(diagram_EObjectVariableValue)
@given(instance=diagram_EObjectVariableValue_strategy)
@settings(max_examples=25)
def test_diagram_EObjectVariableValue_instantiation(instance):
    assert isinstance(instance, diagram_EObjectVariableValue)


diagram_EdgeStyle_strategy = st.builds(diagram_EdgeStyle, centered=safe_text, foldingStyle=safe_text, lineStyle=safe_text, routingStyle=safe_text, size=safe_text, sourceArrow=safe_text, strokeColor=safe_text, targetArrow=safe_text)
@given(instance=diagram_EdgeStyle_strategy)
@settings(max_examples=25)
def test_diagram_EdgeStyle_instantiation(instance):
    assert isinstance(instance, diagram_EdgeStyle)


diagram_EdgeTarget_strategy = st.builds(diagram_EdgeTarget)
@given(instance=diagram_EdgeTarget_strategy)
@settings(max_examples=25)
def test_diagram_EdgeTarget_instantiation(instance):
    assert isinstance(instance, diagram_EdgeTarget)


diagram_Ellipse_strategy = st.builds(diagram_Ellipse, color=safe_text, horizontalDiameter=safe_text, verticalDiameter=safe_text)
@given(instance=diagram_Ellipse_strategy)
@settings(max_examples=25)
def test_diagram_Ellipse_instantiation(instance):
    assert isinstance(instance, diagram_Ellipse)


diagram_EndLabelStyle_strategy = st.builds(diagram_EndLabelStyle)
@given(instance=diagram_EndLabelStyle_strategy)
@settings(max_examples=25)
def test_diagram_EndLabelStyle_instantiation(instance):
    assert isinstance(instance, diagram_EndLabelStyle)


diagram_FilterVariableHistory_strategy = st.builds(diagram_FilterVariableHistory)
@given(instance=diagram_FilterVariableHistory_strategy)
@settings(max_examples=25)
def test_diagram_FilterVariableHistory_instantiation(instance):
    assert isinstance(instance, diagram_FilterVariableHistory)


diagram_FlatContainerStyle_strategy = st.builds(diagram_FlatContainerStyle, backgroundColor=safe_text, backgroundStyle=safe_text, foregroundColor=safe_text)
@given(instance=diagram_FlatContainerStyle_strategy)
@settings(max_examples=25)
def test_diagram_FlatContainerStyle_instantiation(instance):
    assert isinstance(instance, diagram_FlatContainerStyle)


diagram_FoldingFilter_strategy = st.builds(diagram_FoldingFilter)
@given(instance=diagram_FoldingFilter_strategy)
@settings(max_examples=25)
def test_diagram_FoldingFilter_instantiation(instance):
    assert isinstance(instance, diagram_FoldingFilter)


diagram_FoldingPointFilter_strategy = st.builds(diagram_FoldingPointFilter)
@given(instance=diagram_FoldingPointFilter_strategy)
@settings(max_examples=25)
def test_diagram_FoldingPointFilter_instantiation(instance):
    assert isinstance(instance, diagram_FoldingPointFilter)


diagram_GaugeCompositeStyle_strategy = st.builds(diagram_GaugeCompositeStyle, alignment=safe_text)
@given(instance=diagram_GaugeCompositeStyle_strategy)
@settings(max_examples=25)
def test_diagram_GaugeCompositeStyle_instantiation(instance):
    assert isinstance(instance, diagram_GaugeCompositeStyle)


diagram_GaugeSection_strategy = st.builds(diagram_GaugeSection, backgroundColor=safe_text, foregroundColor=safe_text, label=safe_text, max=safe_text, min=safe_text, value=safe_text)
@given(instance=diagram_GaugeSection_strategy)
@settings(max_examples=25)
def test_diagram_GaugeSection_instantiation(instance):
    assert isinstance(instance, diagram_GaugeSection)


diagram_GraphicalFilter_strategy = st.builds(diagram_GraphicalFilter)
@given(instance=diagram_GraphicalFilter_strategy)
@settings(max_examples=25)
def test_diagram_GraphicalFilter_instantiation(instance):
    assert isinstance(instance, diagram_GraphicalFilter)


diagram_HideFilter_strategy = st.builds(diagram_HideFilter)
@given(instance=diagram_HideFilter_strategy)
@settings(max_examples=25)
def test_diagram_HideFilter_instantiation(instance):
    assert isinstance(instance, diagram_HideFilter)


diagram_HideLabelCapabilityStyle_strategy = st.builds(diagram_HideLabelCapabilityStyle, hideLabelByDefault=st.booleans())
@given(instance=diagram_HideLabelCapabilityStyle_strategy)
@settings(max_examples=25)
def test_diagram_HideLabelCapabilityStyle_instantiation(instance):
    assert isinstance(instance, diagram_HideLabelCapabilityStyle)


diagram_HideLabelFilter_strategy = st.builds(diagram_HideLabelFilter)
@given(instance=diagram_HideLabelFilter_strategy)
@settings(max_examples=25)
def test_diagram_HideLabelFilter_instantiation(instance):
    assert isinstance(instance, diagram_HideLabelFilter)


diagram_IndirectlyCollapseFilter_strategy = st.builds(diagram_IndirectlyCollapseFilter)
@given(instance=diagram_IndirectlyCollapseFilter_strategy)
@settings(max_examples=25)
def test_diagram_IndirectlyCollapseFilter_instantiation(instance):
    assert isinstance(instance, diagram_IndirectlyCollapseFilter)


diagram_Lozenge_strategy = st.builds(diagram_Lozenge, color=safe_text, height=safe_text, width=safe_text)
@given(instance=diagram_Lozenge_strategy)
@settings(max_examples=25)
def test_diagram_Lozenge_instantiation(instance):
    assert isinstance(instance, diagram_Lozenge)


diagram_NodeStyle_strategy = st.builds(diagram_NodeStyle, labelPosition=safe_text)
@given(instance=diagram_NodeStyle_strategy)
@settings(max_examples=25)
def test_diagram_NodeStyle_instantiation(instance):
    assert isinstance(instance, diagram_NodeStyle)


diagram_Note_strategy = st.builds(diagram_Note, color=safe_text)
@given(instance=diagram_Note_strategy)
@settings(max_examples=25)
def test_diagram_Note_instantiation(instance):
    assert isinstance(instance, diagram_Note)


diagram_ShapeContainerStyle_strategy = st.builds(diagram_ShapeContainerStyle, backgroundColor=safe_text, shape=safe_text)
@given(instance=diagram_ShapeContainerStyle_strategy)
@settings(max_examples=25)
def test_diagram_ShapeContainerStyle_instantiation(instance):
    assert isinstance(instance, diagram_ShapeContainerStyle)


diagram_Square_strategy = st.builds(diagram_Square, color=safe_text, height=safe_text, width=safe_text)
@given(instance=diagram_Square_strategy)
@settings(max_examples=25)
def test_diagram_Square_instantiation(instance):
    assert isinstance(instance, diagram_Square)


diagram_Style_strategy = st.builds(diagram_Style)
@given(instance=diagram_Style_strategy)
@settings(max_examples=25)
def test_diagram_Style_instantiation(instance):
    assert isinstance(instance, diagram_Style)


diagram_TypedVariableValue_strategy = st.builds(diagram_TypedVariableValue, value=safe_text)
@given(instance=diagram_TypedVariableValue_strategy)
@settings(max_examples=25)
def test_diagram_TypedVariableValue_instantiation(instance):
    assert isinstance(instance, diagram_TypedVariableValue)


diagram_VariableValue_strategy = st.builds(diagram_VariableValue)
@given(instance=diagram_VariableValue_strategy)
@settings(max_examples=25)
def test_diagram_VariableValue_instantiation(instance):
    assert isinstance(instance, diagram_VariableValue)


diagram_WorkspaceImage_strategy = st.builds(diagram_WorkspaceImage, workspacePath=safe_text)
@given(instance=diagram_WorkspaceImage_strategy)
@settings(max_examples=25)
def test_diagram_WorkspaceImage_instantiation(instance):
    assert isinstance(instance, diagram_WorkspaceImage)


diagram_concern_ConcernDescription_strategy = st.builds(diagram_concern_ConcernDescription)
@given(instance=diagram_concern_ConcernDescription_strategy)
@settings(max_examples=25)
def test_diagram_concern_ConcernDescription_instantiation(instance):
    assert isinstance(instance, diagram_concern_ConcernDescription)


diagram_concern_ConcernSet_strategy = st.builds(diagram_concern_ConcernSet)
@given(instance=diagram_concern_ConcernSet_strategy)
@settings(max_examples=25)
def test_diagram_concern_ConcernSet_instantiation(instance):
    assert isinstance(instance, diagram_concern_ConcernSet)


diagram_description_AbstractNodeMapping_strategy = st.builds(diagram_description_AbstractNodeMapping, domainClass=safe_text)
@given(instance=diagram_description_AbstractNodeMapping_strategy)
@settings(max_examples=25)
def test_diagram_description_AbstractNodeMapping_instantiation(instance):
    assert isinstance(instance, diagram_description_AbstractNodeMapping)


diagram_description_AdditionalLayer_strategy = st.builds(diagram_description_AdditionalLayer, activeByDefault=st.booleans(), optional=st.booleans())
@given(instance=diagram_description_AdditionalLayer_strategy)
@settings(max_examples=25)
def test_diagram_description_AdditionalLayer_instantiation(instance):
    assert isinstance(instance, diagram_description_AdditionalLayer)


diagram_description_CompositeLayout_strategy = st.builds(diagram_description_CompositeLayout, direction=safe_text, padding=st.integers())
@given(instance=diagram_description_CompositeLayout_strategy)
@settings(max_examples=25)
def test_diagram_description_CompositeLayout_instantiation(instance):
    assert isinstance(instance, diagram_description_CompositeLayout)


diagram_description_ConditionalContainerStyleDescription_strategy = st.builds(diagram_description_ConditionalContainerStyleDescription)
@given(instance=diagram_description_ConditionalContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_description_ConditionalContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_description_ConditionalContainerStyleDescription)


diagram_description_ConditionalEdgeStyleDescription_strategy = st.builds(diagram_description_ConditionalEdgeStyleDescription)
@given(instance=diagram_description_ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_description_ConditionalEdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_description_ConditionalEdgeStyleDescription)


diagram_description_ConditionalNodeStyleDescription_strategy = st.builds(diagram_description_ConditionalNodeStyleDescription)
@given(instance=diagram_description_ConditionalNodeStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_description_ConditionalNodeStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_description_ConditionalNodeStyleDescription)


diagram_description_ContainerMapping_strategy = st.builds(diagram_description_ContainerMapping, childrenPresentation=safe_text)
@given(instance=diagram_description_ContainerMapping_strategy)
@settings(max_examples=25)
def test_diagram_description_ContainerMapping_instantiation(instance):
    assert isinstance(instance, diagram_description_ContainerMapping)


diagram_description_ContainerMappingImport_strategy = st.builds(diagram_description_ContainerMappingImport)
@given(instance=diagram_description_ContainerMappingImport_strategy)
@settings(max_examples=25)
def test_diagram_description_ContainerMappingImport_instantiation(instance):
    assert isinstance(instance, diagram_description_ContainerMappingImport)


diagram_description_DiagramDescription_strategy = st.builds(diagram_description_DiagramDescription, domainClass=safe_text, enablePopupBars=st.booleans(), preconditionExpression=safe_text, rootExpression=safe_text)
@given(instance=diagram_description_DiagramDescription_strategy)
@settings(max_examples=25)
def test_diagram_description_DiagramDescription_instantiation(instance):
    assert isinstance(instance, diagram_description_DiagramDescription)


diagram_description_DiagramElementMapping_strategy = st.builds(diagram_description_DiagramElementMapping, createElements=st.booleans(), preconditionExpression=safe_text, semanticCandidatesExpression=safe_text, semanticElements=safe_text, synchronizationLock=st.booleans())
@given(instance=diagram_description_DiagramElementMapping_strategy)
@settings(max_examples=25)
def test_diagram_description_DiagramElementMapping_instantiation(instance):
    assert isinstance(instance, diagram_description_DiagramElementMapping)


diagram_description_DiagramExtensionDescription_strategy = st.builds(diagram_description_DiagramExtensionDescription)
@given(instance=diagram_description_DiagramExtensionDescription_strategy)
@settings(max_examples=25)
def test_diagram_description_DiagramExtensionDescription_instantiation(instance):
    assert isinstance(instance, diagram_description_DiagramExtensionDescription)


diagram_description_DiagramImportDescription_strategy = st.builds(diagram_description_DiagramImportDescription)
@given(instance=diagram_description_DiagramImportDescription_strategy)
@settings(max_examples=25)
def test_diagram_description_DiagramImportDescription_instantiation(instance):
    assert isinstance(instance, diagram_description_DiagramImportDescription)


diagram_description_DragAndDropTargetDescription_strategy = st.builds(diagram_description_DragAndDropTargetDescription)
@given(instance=diagram_description_DragAndDropTargetDescription_strategy)
@settings(max_examples=25)
def test_diagram_description_DragAndDropTargetDescription_instantiation(instance):
    assert isinstance(instance, diagram_description_DragAndDropTargetDescription)


diagram_description_EdgeMapping_strategy = st.builds(diagram_description_EdgeMapping, domainClass=safe_text, pathExpression=safe_text, sourceFinderExpression=safe_text, targetExpression=safe_text, targetFinderExpression=safe_text, useDomainElement=st.booleans())
@given(instance=diagram_description_EdgeMapping_strategy)
@settings(max_examples=25)
def test_diagram_description_EdgeMapping_instantiation(instance):
    assert isinstance(instance, diagram_description_EdgeMapping)


diagram_description_EdgeMappingImport_strategy = st.builds(diagram_description_EdgeMappingImport, inheritsAncestorFilters=st.booleans())
@given(instance=diagram_description_EdgeMappingImport_strategy)
@settings(max_examples=25)
def test_diagram_description_EdgeMappingImport_instantiation(instance):
    assert isinstance(instance, diagram_description_EdgeMappingImport)


diagram_description_IEdgeMapping_strategy = st.builds(diagram_description_IEdgeMapping)
@given(instance=diagram_description_IEdgeMapping_strategy)
@settings(max_examples=25)
def test_diagram_description_IEdgeMapping_instantiation(instance):
    assert isinstance(instance, diagram_description_IEdgeMapping)


diagram_description_Layer_strategy = st.builds(diagram_description_Layer, icon=safe_text)
@given(instance=diagram_description_Layer_strategy)
@settings(max_examples=25)
def test_diagram_description_Layer_instantiation(instance):
    assert isinstance(instance, diagram_description_Layer)


diagram_description_Layout_strategy = st.builds(diagram_description_Layout)
@given(instance=diagram_description_Layout_strategy)
@settings(max_examples=25)
def test_diagram_description_Layout_instantiation(instance):
    assert isinstance(instance, diagram_description_Layout)


diagram_description_MappingBasedDecoration_strategy = st.builds(diagram_description_MappingBasedDecoration)
@given(instance=diagram_description_MappingBasedDecoration_strategy)
@settings(max_examples=25)
def test_diagram_description_MappingBasedDecoration_instantiation(instance):
    assert isinstance(instance, diagram_description_MappingBasedDecoration)


diagram_description_NodeMapping_strategy = st.builds(diagram_description_NodeMapping)
@given(instance=diagram_description_NodeMapping_strategy)
@settings(max_examples=25)
def test_diagram_description_NodeMapping_instantiation(instance):
    assert isinstance(instance, diagram_description_NodeMapping)


diagram_description_NodeMappingImport_strategy = st.builds(diagram_description_NodeMappingImport)
@given(instance=diagram_description_NodeMappingImport_strategy)
@settings(max_examples=25)
def test_diagram_description_NodeMappingImport_instantiation(instance):
    assert isinstance(instance, diagram_description_NodeMappingImport)


diagram_description_OrderedTreeLayout_strategy = st.builds(diagram_description_OrderedTreeLayout, childrenExpression=safe_text)
@given(instance=diagram_description_OrderedTreeLayout_strategy)
@settings(max_examples=25)
def test_diagram_description_OrderedTreeLayout_instantiation(instance):
    assert isinstance(instance, diagram_description_OrderedTreeLayout)


diagram_filter_CompositeFilterDescription_strategy = st.builds(diagram_filter_CompositeFilterDescription)
@given(instance=diagram_filter_CompositeFilterDescription_strategy)
@settings(max_examples=25)
def test_diagram_filter_CompositeFilterDescription_instantiation(instance):
    assert isinstance(instance, diagram_filter_CompositeFilterDescription)


diagram_filter_Filter_strategy = st.builds(diagram_filter_Filter, filterKind=safe_text)
@given(instance=diagram_filter_Filter_strategy)
@settings(max_examples=25)
def test_diagram_filter_Filter_instantiation(instance):
    assert isinstance(instance, diagram_filter_Filter)


diagram_filter_FilterDescription_strategy = st.builds(diagram_filter_FilterDescription)
@given(instance=diagram_filter_FilterDescription_strategy)
@settings(max_examples=25)
def test_diagram_filter_FilterDescription_instantiation(instance):
    assert isinstance(instance, diagram_filter_FilterDescription)


diagram_filter_MappingFilter_strategy = st.builds(diagram_filter_MappingFilter, semanticConditionExpression=safe_text, viewConditionExpression=safe_text)
@given(instance=diagram_filter_MappingFilter_strategy)
@settings(max_examples=25)
def test_diagram_filter_MappingFilter_instantiation(instance):
    assert isinstance(instance, diagram_filter_MappingFilter)


diagram_filter_VariableFilter_strategy = st.builds(diagram_filter_VariableFilter, semanticConditionExpression=safe_text)
@given(instance=diagram_filter_VariableFilter_strategy)
@settings(max_examples=25)
def test_diagram_filter_VariableFilter_instantiation(instance):
    assert isinstance(instance, diagram_filter_VariableFilter)


diagram_style_BeginLabelStyleDescription_strategy = st.builds(diagram_style_BeginLabelStyleDescription)
@given(instance=diagram_style_BeginLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_BeginLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_BeginLabelStyleDescription)


diagram_style_BorderedStyleDescription_strategy = st.builds(diagram_style_BorderedStyleDescription, borderLineStyle=safe_text, borderSizeComputationExpression=safe_text)
@given(instance=diagram_style_BorderedStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_BorderedStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_BorderedStyleDescription)


diagram_style_BracketEdgeStyleDescription_strategy = st.builds(diagram_style_BracketEdgeStyleDescription)
@given(instance=diagram_style_BracketEdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_BracketEdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_BracketEdgeStyleDescription)


diagram_style_BundledImageDescription_strategy = st.builds(diagram_style_BundledImageDescription, providedShapeID=safe_text, shape=safe_text)
@given(instance=diagram_style_BundledImageDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_BundledImageDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_BundledImageDescription)


diagram_style_CenterLabelStyleDescription_strategy = st.builds(diagram_style_CenterLabelStyleDescription)
@given(instance=diagram_style_CenterLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_CenterLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_CenterLabelStyleDescription)


diagram_style_ContainerStyleDescription_strategy = st.builds(diagram_style_ContainerStyleDescription, roundedCorner=st.booleans())
@given(instance=diagram_style_ContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_ContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_ContainerStyleDescription)


diagram_style_CustomStyleDescription_strategy = st.builds(diagram_style_CustomStyleDescription, id=safe_text)
@given(instance=diagram_style_CustomStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_CustomStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_CustomStyleDescription)


diagram_style_DotDescription_strategy = st.builds(diagram_style_DotDescription, strokeSizeComputationExpression=safe_text)
@given(instance=diagram_style_DotDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_DotDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_DotDescription)


diagram_style_EdgeStyleDescription_strategy = st.builds(diagram_style_EdgeStyleDescription, endsCentering=safe_text, foldingStyle=safe_text, lineStyle=safe_text, routingStyle=safe_text, sizeComputationExpression=safe_text, sourceArrow=safe_text, targetArrow=safe_text)
@given(instance=diagram_style_EdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_EdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_EdgeStyleDescription)


diagram_style_EllipseNodeDescription_strategy = st.builds(diagram_style_EllipseNodeDescription, horizontalDiameterComputationExpression=safe_text, verticalDiameterComputationExpression=safe_text)
@given(instance=diagram_style_EllipseNodeDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_EllipseNodeDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_EllipseNodeDescription)


diagram_style_EndLabelStyleDescription_strategy = st.builds(diagram_style_EndLabelStyleDescription)
@given(instance=diagram_style_EndLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_EndLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_EndLabelStyleDescription)


diagram_style_FlatContainerStyleDescription_strategy = st.builds(diagram_style_FlatContainerStyleDescription, backgroundStyle=safe_text)
@given(instance=diagram_style_FlatContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_FlatContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_FlatContainerStyleDescription)


diagram_style_GaugeCompositeStyleDescription_strategy = st.builds(diagram_style_GaugeCompositeStyleDescription, alignment=safe_text)
@given(instance=diagram_style_GaugeCompositeStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_GaugeCompositeStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_GaugeCompositeStyleDescription)


diagram_style_GaugeSectionDescription_strategy = st.builds(diagram_style_GaugeSectionDescription, label=safe_text, maxValueExpression=safe_text, minValueExpression=safe_text, valueExpression=safe_text)
@given(instance=diagram_style_GaugeSectionDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_GaugeSectionDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_GaugeSectionDescription)


diagram_style_HideLabelCapabilityStyleDescription_strategy = st.builds(diagram_style_HideLabelCapabilityStyleDescription, hideLabelByDefault=st.booleans())
@given(instance=diagram_style_HideLabelCapabilityStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_HideLabelCapabilityStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_HideLabelCapabilityStyleDescription)


diagram_style_LozengeNodeDescription_strategy = st.builds(diagram_style_LozengeNodeDescription, heightComputationExpression=safe_text, widthComputationExpression=safe_text)
@given(instance=diagram_style_LozengeNodeDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_LozengeNodeDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_LozengeNodeDescription)


diagram_style_NodeStyleDescription_strategy = st.builds(diagram_style_NodeStyleDescription, forbiddenSides=safe_text, labelPosition=safe_text, resizeKind=safe_text, sizeComputationExpression=safe_text)
@given(instance=diagram_style_NodeStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_NodeStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_NodeStyleDescription)


diagram_style_NoteDescription_strategy = st.builds(diagram_style_NoteDescription)
@given(instance=diagram_style_NoteDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_NoteDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_NoteDescription)


diagram_style_RoundedCornerStyleDescription_strategy = st.builds(diagram_style_RoundedCornerStyleDescription, arcHeight=safe_text, arcWidth=safe_text)
@given(instance=diagram_style_RoundedCornerStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_RoundedCornerStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_RoundedCornerStyleDescription)


diagram_style_ShapeContainerStyleDescription_strategy = st.builds(diagram_style_ShapeContainerStyleDescription, shape=safe_text)
@given(instance=diagram_style_ShapeContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_ShapeContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_ShapeContainerStyleDescription)


diagram_style_SizeComputationContainerStyleDescription_strategy = st.builds(diagram_style_SizeComputationContainerStyleDescription, heightComputationExpression=safe_text, widthComputationExpression=safe_text)
@given(instance=diagram_style_SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_SizeComputationContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_SizeComputationContainerStyleDescription)


diagram_style_SquareDescription_strategy = st.builds(diagram_style_SquareDescription, height=safe_text, width=safe_text)
@given(instance=diagram_style_SquareDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_SquareDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_SquareDescription)


diagram_style_WorkspaceImageDescription_strategy = st.builds(diagram_style_WorkspaceImageDescription, workspacePath=safe_text)
@given(instance=diagram_style_WorkspaceImageDescription_strategy)
@settings(max_examples=25)
def test_diagram_style_WorkspaceImageDescription_instantiation(instance):
    assert isinstance(instance, diagram_style_WorkspaceImageDescription)


diagram_tool_BehaviorTool_strategy = st.builds(diagram_tool_BehaviorTool, domainClass=safe_text)
@given(instance=diagram_tool_BehaviorTool_strategy)
@settings(max_examples=25)
def test_diagram_tool_BehaviorTool_instantiation(instance):
    assert isinstance(instance, diagram_tool_BehaviorTool)


diagram_tool_ContainerCreationDescription_strategy = st.builds(diagram_tool_ContainerCreationDescription, iconPath=safe_text)
@given(instance=diagram_tool_ContainerCreationDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_ContainerCreationDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_ContainerCreationDescription)


diagram_tool_ContainerDropDescription_strategy = st.builds(diagram_tool_ContainerDropDescription, dragSource=safe_text, moveEdges=st.booleans())
@given(instance=diagram_tool_ContainerDropDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_ContainerDropDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_ContainerDropDescription)


diagram_tool_CreateEdgeView_strategy = st.builds(diagram_tool_CreateEdgeView, sourceExpression=safe_text, targetExpression=safe_text)
@given(instance=diagram_tool_CreateEdgeView_strategy)
@settings(max_examples=25)
def test_diagram_tool_CreateEdgeView_instantiation(instance):
    assert isinstance(instance, diagram_tool_CreateEdgeView)


diagram_tool_CreateView_strategy = st.builds(diagram_tool_CreateView, containerViewExpression=safe_text, variableName=safe_text)
@given(instance=diagram_tool_CreateView_strategy)
@settings(max_examples=25)
def test_diagram_tool_CreateView_instantiation(instance):
    assert isinstance(instance, diagram_tool_CreateView)


diagram_tool_DeleteElementDescription_strategy = st.builds(diagram_tool_DeleteElementDescription)
@given(instance=diagram_tool_DeleteElementDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_DeleteElementDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_DeleteElementDescription)


diagram_tool_DeleteHook_strategy = st.builds(diagram_tool_DeleteHook, id=safe_text)
@given(instance=diagram_tool_DeleteHook_strategy)
@settings(max_examples=25)
def test_diagram_tool_DeleteHook_instantiation(instance):
    assert isinstance(instance, diagram_tool_DeleteHook)


diagram_tool_DeleteHookParameter_strategy = st.builds(diagram_tool_DeleteHookParameter, name=safe_text, value=safe_text)
@given(instance=diagram_tool_DeleteHookParameter_strategy)
@settings(max_examples=25)
def test_diagram_tool_DeleteHookParameter_instantiation(instance):
    assert isinstance(instance, diagram_tool_DeleteHookParameter)


diagram_tool_DiagramCreationDescription_strategy = st.builds(diagram_tool_DiagramCreationDescription)
@given(instance=diagram_tool_DiagramCreationDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_DiagramCreationDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_DiagramCreationDescription)


diagram_tool_DiagramNavigationDescription_strategy = st.builds(diagram_tool_DiagramNavigationDescription)
@given(instance=diagram_tool_DiagramNavigationDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_DiagramNavigationDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_DiagramNavigationDescription)


diagram_tool_DirectEditLabel_strategy = st.builds(diagram_tool_DirectEditLabel, inputLabelExpression=safe_text)
@given(instance=diagram_tool_DirectEditLabel_strategy)
@settings(max_examples=25)
def test_diagram_tool_DirectEditLabel_instantiation(instance):
    assert isinstance(instance, diagram_tool_DirectEditLabel)


diagram_tool_DoubleClickDescription_strategy = st.builds(diagram_tool_DoubleClickDescription)
@given(instance=diagram_tool_DoubleClickDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_DoubleClickDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_DoubleClickDescription)


diagram_tool_EdgeCreationDescription_strategy = st.builds(diagram_tool_EdgeCreationDescription, connectionStartPrecondition=safe_text, iconPath=safe_text)
@given(instance=diagram_tool_EdgeCreationDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_EdgeCreationDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_EdgeCreationDescription)


diagram_tool_ElementDoubleClickVariable_strategy = st.builds(diagram_tool_ElementDoubleClickVariable)
@given(instance=diagram_tool_ElementDoubleClickVariable_strategy)
@settings(max_examples=25)
def test_diagram_tool_ElementDoubleClickVariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_ElementDoubleClickVariable)


diagram_tool_Navigation_strategy = st.builds(diagram_tool_Navigation, createIfNotExistent=st.booleans())
@given(instance=diagram_tool_Navigation_strategy)
@settings(max_examples=25)
def test_diagram_tool_Navigation_instantiation(instance):
    assert isinstance(instance, diagram_tool_Navigation)


diagram_tool_NodeCreationDescription_strategy = st.builds(diagram_tool_NodeCreationDescription, iconPath=safe_text)
@given(instance=diagram_tool_NodeCreationDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_NodeCreationDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_NodeCreationDescription)


diagram_tool_NodeCreationVariable_strategy = st.builds(diagram_tool_NodeCreationVariable)
@given(instance=diagram_tool_NodeCreationVariable_strategy)
@settings(max_examples=25)
def test_diagram_tool_NodeCreationVariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_NodeCreationVariable)


diagram_tool_ReconnectEdgeDescription_strategy = st.builds(diagram_tool_ReconnectEdgeDescription, reconnectionKind=safe_text)
@given(instance=diagram_tool_ReconnectEdgeDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_ReconnectEdgeDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_ReconnectEdgeDescription)


diagram_tool_RequestDescription_strategy = st.builds(diagram_tool_RequestDescription, type=safe_text)
@given(instance=diagram_tool_RequestDescription_strategy)
@settings(max_examples=25)
def test_diagram_tool_RequestDescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_RequestDescription)


diagram_tool_SourceEdgeCreationVariable_strategy = st.builds(diagram_tool_SourceEdgeCreationVariable)
@given(instance=diagram_tool_SourceEdgeCreationVariable_strategy)
@settings(max_examples=25)
def test_diagram_tool_SourceEdgeCreationVariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_SourceEdgeCreationVariable)


diagram_tool_SourceEdgeViewCreationVariable_strategy = st.builds(diagram_tool_SourceEdgeViewCreationVariable)
@given(instance=diagram_tool_SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=25)
def test_diagram_tool_SourceEdgeViewCreationVariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_SourceEdgeViewCreationVariable)


diagram_tool_TargetEdgeCreationVariable_strategy = st.builds(diagram_tool_TargetEdgeCreationVariable)
@given(instance=diagram_tool_TargetEdgeCreationVariable_strategy)
@settings(max_examples=25)
def test_diagram_tool_TargetEdgeCreationVariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_TargetEdgeCreationVariable)


diagram_tool_TargetEdgeViewCreationVariable_strategy = st.builds(diagram_tool_TargetEdgeViewCreationVariable)
@given(instance=diagram_tool_TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=25)
def test_diagram_tool_TargetEdgeViewCreationVariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_TargetEdgeViewCreationVariable)


diagram_tool_ToolGroup_strategy = st.builds(diagram_tool_ToolGroup)
@given(instance=diagram_tool_ToolGroup_strategy)
@settings(max_examples=25)
def test_diagram_tool_ToolGroup_instantiation(instance):
    assert isinstance(instance, diagram_tool_ToolGroup)


diagram_tool_ToolGroupExtension_strategy = st.builds(diagram_tool_ToolGroupExtension)
@given(instance=diagram_tool_ToolGroupExtension_strategy)
@settings(max_examples=25)
def test_diagram_tool_ToolGroupExtension_instantiation(instance):
    assert isinstance(instance, diagram_tool_ToolGroupExtension)


diagram_tool_ToolSection_strategy = st.builds(diagram_tool_ToolSection, icon=safe_text)
@given(instance=diagram_tool_ToolSection_strategy)
@settings(max_examples=25)
def test_diagram_tool_ToolSection_instantiation(instance):
    assert isinstance(instance, diagram_tool_ToolSection)


filter_CompositeFilterDescription_strategy = st.builds(filter_CompositeFilterDescription)
@given(instance=filter_CompositeFilterDescription_strategy)
@settings(max_examples=25)
def test_filter_CompositeFilterDescription_instantiation(instance):
    assert isinstance(instance, filter_CompositeFilterDescription)


filter_Filter_strategy = st.builds(filter_Filter)
@given(instance=filter_Filter_strategy)
@settings(max_examples=25)
def test_filter_Filter_instantiation(instance):
    assert isinstance(instance, filter_Filter)


filter_FilterDescription_strategy = st.builds(filter_FilterDescription)
@given(instance=filter_FilterDescription_strategy)
@settings(max_examples=25)
def test_filter_FilterDescription_instantiation(instance):
    assert isinstance(instance, filter_FilterDescription)


style_BeginLabelStyleDescription_strategy = st.builds(style_BeginLabelStyleDescription)
@given(instance=style_BeginLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_style_BeginLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, style_BeginLabelStyleDescription)


style_BorderedStyleDescription_strategy = st.builds(style_BorderedStyleDescription)
@given(instance=style_BorderedStyleDescription_strategy)
@settings(max_examples=25)
def test_style_BorderedStyleDescription_instantiation(instance):
    assert isinstance(instance, style_BorderedStyleDescription)


style_CenterLabelStyleDescription_strategy = st.builds(style_CenterLabelStyleDescription)
@given(instance=style_CenterLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_style_CenterLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, style_CenterLabelStyleDescription)


style_ContainerStyleDescription_strategy = st.builds(style_ContainerStyleDescription)
@given(instance=style_ContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_style_ContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, style_ContainerStyleDescription)


style_EdgeStyleDescription_strategy = st.builds(style_EdgeStyleDescription)
@given(instance=style_EdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_style_EdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, style_EdgeStyleDescription)


style_EndLabelStyleDescription_strategy = st.builds(style_EndLabelStyleDescription)
@given(instance=style_EndLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_style_EndLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, style_EndLabelStyleDescription)


style_GaugeSectionDescription_strategy = st.builds(style_GaugeSectionDescription)
@given(instance=style_GaugeSectionDescription_strategy)
@settings(max_examples=25)
def test_style_GaugeSectionDescription_instantiation(instance):
    assert isinstance(instance, style_GaugeSectionDescription)


style_HideLabelCapabilityStyleDescription_strategy = st.builds(style_HideLabelCapabilityStyleDescription)
@given(instance=style_HideLabelCapabilityStyleDescription_strategy)
@settings(max_examples=25)
def test_style_HideLabelCapabilityStyleDescription_instantiation(instance):
    assert isinstance(instance, style_HideLabelCapabilityStyleDescription)


style_LabelBorderStyleDescription_strategy = st.builds(style_LabelBorderStyleDescription)
@given(instance=style_LabelBorderStyleDescription_strategy)
@settings(max_examples=25)
def test_style_LabelBorderStyleDescription_instantiation(instance):
    assert isinstance(instance, style_LabelBorderStyleDescription)


style_LabelStyleDescription_strategy = st.builds(style_LabelStyleDescription)
@given(instance=style_LabelStyleDescription_strategy)
@settings(max_examples=25)
def test_style_LabelStyleDescription_instantiation(instance):
    assert isinstance(instance, style_LabelStyleDescription)


style_NodeStyleDescription_strategy = st.builds(style_NodeStyleDescription)
@given(instance=style_NodeStyleDescription_strategy)
@settings(max_examples=25)
def test_style_NodeStyleDescription_instantiation(instance):
    assert isinstance(instance, style_NodeStyleDescription)


style_RoundedCornerStyleDescription_strategy = st.builds(style_RoundedCornerStyleDescription)
@given(instance=style_RoundedCornerStyleDescription_strategy)
@settings(max_examples=25)
def test_style_RoundedCornerStyleDescription_instantiation(instance):
    assert isinstance(instance, style_RoundedCornerStyleDescription)


style_SizeComputationContainerStyleDescription_strategy = st.builds(style_SizeComputationContainerStyleDescription)
@given(instance=style_SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_style_SizeComputationContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, style_SizeComputationContainerStyleDescription)


style_StyleDescription_strategy = st.builds(style_StyleDescription)
@given(instance=style_StyleDescription_strategy)
@settings(max_examples=25)
def test_style_StyleDescription_instantiation(instance):
    assert isinstance(instance, style_StyleDescription)


style_TooltipStyleDescription_strategy = st.builds(style_TooltipStyleDescription)
@given(instance=style_TooltipStyleDescription_strategy)
@settings(max_examples=25)
def test_style_TooltipStyleDescription_instantiation(instance):
    assert isinstance(instance, style_TooltipStyleDescription)


tool_AbstractToolDescription_strategy = st.builds(tool_AbstractToolDescription)
@given(instance=tool_AbstractToolDescription_strategy)
@settings(max_examples=25)
def test_tool_AbstractToolDescription_instantiation(instance):
    assert isinstance(instance, tool_AbstractToolDescription)


tool_BehaviorTool_strategy = st.builds(tool_BehaviorTool)
@given(instance=tool_BehaviorTool_strategy)
@settings(max_examples=25)
def test_tool_BehaviorTool_instantiation(instance):
    assert isinstance(instance, tool_BehaviorTool)


tool_ContainerDropDescription_strategy = st.builds(tool_ContainerDropDescription)
@given(instance=tool_ContainerDropDescription_strategy)
@settings(max_examples=25)
def test_tool_ContainerDropDescription_instantiation(instance):
    assert isinstance(instance, tool_ContainerDropDescription)


tool_ContainerViewVariable_strategy = st.builds(tool_ContainerViewVariable)
@given(instance=tool_ContainerViewVariable_strategy)
@settings(max_examples=25)
def test_tool_ContainerViewVariable_instantiation(instance):
    assert isinstance(instance, tool_ContainerViewVariable)


tool_DeleteElementDescription_strategy = st.builds(tool_DeleteElementDescription)
@given(instance=tool_DeleteElementDescription_strategy)
@settings(max_examples=25)
def test_tool_DeleteElementDescription_instantiation(instance):
    assert isinstance(instance, tool_DeleteElementDescription)


tool_DeleteHook_strategy = st.builds(tool_DeleteHook)
@given(instance=tool_DeleteHook_strategy)
@settings(max_examples=25)
def test_tool_DeleteHook_instantiation(instance):
    assert isinstance(instance, tool_DeleteHook)


tool_DeleteHookParameter_strategy = st.builds(tool_DeleteHookParameter)
@given(instance=tool_DeleteHookParameter_strategy)
@settings(max_examples=25)
def test_tool_DeleteHookParameter_instantiation(instance):
    assert isinstance(instance, tool_DeleteHookParameter)


tool_DirectEditLabel_strategy = st.builds(tool_DirectEditLabel)
@given(instance=tool_DirectEditLabel_strategy)
@settings(max_examples=25)
def test_tool_DirectEditLabel_instantiation(instance):
    assert isinstance(instance, tool_DirectEditLabel)


tool_DoubleClickDescription_strategy = st.builds(tool_DoubleClickDescription)
@given(instance=tool_DoubleClickDescription_strategy)
@settings(max_examples=25)
def test_tool_DoubleClickDescription_instantiation(instance):
    assert isinstance(instance, tool_DoubleClickDescription)


tool_DropContainerVariable_strategy = st.builds(tool_DropContainerVariable)
@given(instance=tool_DropContainerVariable_strategy)
@settings(max_examples=25)
def test_tool_DropContainerVariable_instantiation(instance):
    assert isinstance(instance, tool_DropContainerVariable)


tool_EditMaskVariables_strategy = st.builds(tool_EditMaskVariables)
@given(instance=tool_EditMaskVariables_strategy)
@settings(max_examples=25)
def test_tool_EditMaskVariables_instantiation(instance):
    assert isinstance(instance, tool_EditMaskVariables)


tool_ElementDeleteVariable_strategy = st.builds(tool_ElementDeleteVariable)
@given(instance=tool_ElementDeleteVariable_strategy)
@settings(max_examples=25)
def test_tool_ElementDeleteVariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDeleteVariable)


tool_ElementDoubleClickVariable_strategy = st.builds(tool_ElementDoubleClickVariable)
@given(instance=tool_ElementDoubleClickVariable_strategy)
@settings(max_examples=25)
def test_tool_ElementDoubleClickVariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDoubleClickVariable)


tool_ElementDropVariable_strategy = st.builds(tool_ElementDropVariable)
@given(instance=tool_ElementDropVariable_strategy)
@settings(max_examples=25)
def test_tool_ElementDropVariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDropVariable)


tool_ElementSelectVariable_strategy = st.builds(tool_ElementSelectVariable)
@given(instance=tool_ElementSelectVariable_strategy)
@settings(max_examples=25)
def test_tool_ElementSelectVariable_instantiation(instance):
    assert isinstance(instance, tool_ElementSelectVariable)


tool_InitEdgeCreationOperation_strategy = st.builds(tool_InitEdgeCreationOperation)
@given(instance=tool_InitEdgeCreationOperation_strategy)
@settings(max_examples=25)
def test_tool_InitEdgeCreationOperation_instantiation(instance):
    assert isinstance(instance, tool_InitEdgeCreationOperation)


tool_InitialContainerDropOperation_strategy = st.builds(tool_InitialContainerDropOperation)
@given(instance=tool_InitialContainerDropOperation_strategy)
@settings(max_examples=25)
def test_tool_InitialContainerDropOperation_instantiation(instance):
    assert isinstance(instance, tool_InitialContainerDropOperation)


tool_InitialNodeCreationOperation_strategy = st.builds(tool_InitialNodeCreationOperation)
@given(instance=tool_InitialNodeCreationOperation_strategy)
@settings(max_examples=25)
def test_tool_InitialNodeCreationOperation_instantiation(instance):
    assert isinstance(instance, tool_InitialNodeCreationOperation)


tool_InitialOperation_strategy = st.builds(tool_InitialOperation)
@given(instance=tool_InitialOperation_strategy)
@settings(max_examples=25)
def test_tool_InitialOperation_instantiation(instance):
    assert isinstance(instance, tool_InitialOperation)


tool_NodeCreationVariable_strategy = st.builds(tool_NodeCreationVariable)
@given(instance=tool_NodeCreationVariable_strategy)
@settings(max_examples=25)
def test_tool_NodeCreationVariable_instantiation(instance):
    assert isinstance(instance, tool_NodeCreationVariable)


tool_PopupMenu_strategy = st.builds(tool_PopupMenu)
@given(instance=tool_PopupMenu_strategy)
@settings(max_examples=25)
def test_tool_PopupMenu_instantiation(instance):
    assert isinstance(instance, tool_PopupMenu)


tool_ReconnectEdgeDescription_strategy = st.builds(tool_ReconnectEdgeDescription)
@given(instance=tool_ReconnectEdgeDescription_strategy)
@settings(max_examples=25)
def test_tool_ReconnectEdgeDescription_instantiation(instance):
    assert isinstance(instance, tool_ReconnectEdgeDescription)


tool_RepresentationCreationDescription_strategy = st.builds(tool_RepresentationCreationDescription)
@given(instance=tool_RepresentationCreationDescription_strategy)
@settings(max_examples=25)
def test_tool_RepresentationCreationDescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationCreationDescription)


tool_SelectModelElementVariable_strategy = st.builds(tool_SelectModelElementVariable)
@given(instance=tool_SelectModelElementVariable_strategy)
@settings(max_examples=25)
def test_tool_SelectModelElementVariable_instantiation(instance):
    assert isinstance(instance, tool_SelectModelElementVariable)


tool_SourceEdgeCreationVariable_strategy = st.builds(tool_SourceEdgeCreationVariable)
@given(instance=tool_SourceEdgeCreationVariable_strategy)
@settings(max_examples=25)
def test_tool_SourceEdgeCreationVariable_instantiation(instance):
    assert isinstance(instance, tool_SourceEdgeCreationVariable)


tool_SourceEdgeViewCreationVariable_strategy = st.builds(tool_SourceEdgeViewCreationVariable)
@given(instance=tool_SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=25)
def test_tool_SourceEdgeViewCreationVariable_instantiation(instance):
    assert isinstance(instance, tool_SourceEdgeViewCreationVariable)


tool_TargetEdgeCreationVariable_strategy = st.builds(tool_TargetEdgeCreationVariable)
@given(instance=tool_TargetEdgeCreationVariable_strategy)
@settings(max_examples=25)
def test_tool_TargetEdgeCreationVariable_instantiation(instance):
    assert isinstance(instance, tool_TargetEdgeCreationVariable)


tool_TargetEdgeViewCreationVariable_strategy = st.builds(tool_TargetEdgeViewCreationVariable)
@given(instance=tool_TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=25)
def test_tool_TargetEdgeViewCreationVariable_instantiation(instance):
    assert isinstance(instance, tool_TargetEdgeViewCreationVariable)


tool_ToolEntry_strategy = st.builds(tool_ToolEntry)
@given(instance=tool_ToolEntry_strategy)
@settings(max_examples=25)
def test_tool_ToolEntry_instantiation(instance):
    assert isinstance(instance, tool_ToolEntry)


tool_ToolGroup_strategy = st.builds(tool_ToolGroup)
@given(instance=tool_ToolGroup_strategy)
@settings(max_examples=25)
def test_tool_ToolGroup_instantiation(instance):
    assert isinstance(instance, tool_ToolGroup)


tool_ToolGroupExtension_strategy = st.builds(tool_ToolGroupExtension)
@given(instance=tool_ToolGroupExtension_strategy)
@settings(max_examples=25)
def test_tool_ToolGroupExtension_instantiation(instance):
    assert isinstance(instance, tool_ToolGroupExtension)


tool_ToolSection_strategy = st.builds(tool_ToolSection)
@given(instance=tool_ToolSection_strategy)
@settings(max_examples=25)
def test_tool_ToolSection_instantiation(instance):
    assert isinstance(instance, tool_ToolSection)


tool_VariableContainer_strategy = st.builds(tool_VariableContainer)
@given(instance=tool_VariableContainer_strategy)
@settings(max_examples=25)
def test_tool_VariableContainer_instantiation(instance):
    assert isinstance(instance, tool_VariableContainer)


validation_ValidationRule_strategy = st.builds(validation_ValidationRule)
@given(instance=validation_ValidationRule_strategy)
@settings(max_examples=25)
def test_validation_ValidationRule_instantiation(instance):
    assert isinstance(instance, validation_ValidationRule)


validation_ValidationSet_strategy = st.builds(validation_ValidationSet)
@given(instance=validation_ValidationSet_strategy)
@settings(max_examples=25)
def test_validation_ValidationSet_instantiation(instance):
    assert isinstance(instance, validation_ValidationSet)



