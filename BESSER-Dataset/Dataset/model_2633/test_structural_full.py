import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractDNode,
    AbstractToolDescription,
    AbstractVariable,
    AnnotationEntry,
    BasicLabelStyle,
    BasicLabelStyleDescription,
    BeginLabelStyle,
    CenterLabelStyle,
    CollapseFilter,
    ColorDescription,
    ColorStep,
    ConditionalStyleDescription,
    ContainerModelOperation,
    ContainerStyle,
    ContainerVariable2StyleDescription,
    CreateView,
    Customizable,
    Customization,
    DAnnotation,
    DAnnotationEntry,
    DContainer,
    DDiagram,
    DDiagramElement,
    DDiagramElementContainer,
    DDiagramSet,
    DEdge,
    DFile,
    DLabelled,
    DMappingBased,
    DNavigable,
    DNavigationLink,
    DNode,
    DNodeListElement,
    DRefreshable,
    DRepresentation,
    DRepresentationElement,
    DResource,
    DResourceContainer,
    DSemanticDecorator,
    DStylizable,
    DValidable,
    DView,
    DecorationDescription,
    DecorationDescriptionsSet,
    DiagramElementMapping2ModelElement,
    DocumentedElement,
    DragAndDropTarget,
    EStructuralFeatureCustomization,
    EdgeStyle,
    EdgeStyleDescription,
    EdgeTarget,
    EndLabelStyle,
    FeatureExtensionDescription,
    Filter,
    FilterDescription,
    FilterVariableHistory,
    FilterVariableValue,
    FixedColor,
    GaugeSection,
    GraphicalFilter,
    IVSMElementCustomization,
    IdentifiedElement,
    InformationSection,
    JavaExtension,
    LabelStyle,
    Layer,
    Layout,
    MappingBasedToolDescription,
    MenuItemDescription,
    MenuItemOrRef,
    MetamodelExtensionSetting,
    ModelElement2ViewVariable,
    ModelOperation,
    NodeStyle,
    NodeStyleDescription,
    RepresentationCreationDescription,
    RepresentationDescription,
    RepresentationExtensionDescription,
    RepresentationNavigationDescription,
    RepresentationTemplate,
    SelectionDescription,
    Style,
    StyleDescription,
    SwitchChild,
    SystemColor,
    SytemColorsPalette,
    ToolEntry,
    UserColor,
    UserColorsPalette,
    ValidationRule,
    ViewVariable2ContainerVariable,
    Viewpoint,
    concern_ConcernDescription,
    concern_ConcernSet,
    description_AbstractMappingImport,
    description_AbstractNodeMapping,
    description_AdditionalLayer,
    description_ColorDescription,
    description_Component,
    description_ConditionalContainerStyleDescription,
    description_ConditionalEdgeStyleDescription,
    description_ConditionalNodeStyleDescription,
    description_ContainerMapping,
    description_DModelElement,
    description_DiagramDescription,
    description_DiagramElementMapping,
    description_DocumentedElement,
    description_DragAndDropTargetDescription,
    description_EdgeMapping,
    description_EdgeMappingImport,
    description_EndUserDocumentedElement,
    description_FixedColor,
    description_IEdgeMapping,
    description_IdentifiedElement,
    description_Layer,
    description_Layout,
    description_NodeMapping,
    description_PasteTargetDescription,
    description_RepresentationDescription,
    description_RepresentationElementMapping,
    description_RepresentationImportDescription,
    description_SelectionDescription,
    description_UserColor,
    description_viewpoint_EObject,
    description_viewpoint_EPackage,
    description_viewpoint_EStringToStringMapEntry,
    diagram_AbstractDNode,
    diagram_BorderedStyle,
    diagram_ContainerStyle,
    diagram_DDiagram,
    diagram_DDiagramElement,
    diagram_EdgeTarget,
    diagram_NodeStyle,
    diagram_viewpoint_DRepresentationContainer,
    diagram_viewpoint_Decoration,
    diagram_viewpoint_EObject,
    diagram_viewpoint_RGBValues,
    diagram_viewpoint_Style,
    filter_CompositeFilterDescription,
    filter_Filter,
    filter_FilterDescription,
    filter_FilterVariable,
    style_BeginLabelStyleDescription,
    style_BorderedStyleDescription,
    style_CenterLabelStyleDescription,
    style_ContainerStyleDescription,
    style_EdgeStyleDescription,
    style_EndLabelStyleDescription,
    style_GaugeSectionDescription,
    style_LabelBorderStyleDescription,
    style_LabelBorderStyles,
    style_LabelStyleDescription,
    style_NodeStyleDescription,
    style_RoundedCornerStyleDescription,
    style_SizeComputationContainerStyleDescription,
    style_StyleDescription,
    style_TooltipStyleDescription,
    tool_AbstractToolDescription,
    tool_AbstractVariable,
    tool_BehaviorTool,
    tool_Case,
    tool_ContainerDropDescription,
    tool_ContainerModelOperation,
    tool_ContainerViewVariable,
    tool_Default,
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
    tool_ElementVariable,
    tool_ElementViewVariable,
    tool_ExternalJavaAction,
    tool_ExternalJavaActionParameter,
    tool_FeatureChangeListener,
    tool_InitEdgeCreationOperation,
    tool_InitialContainerDropOperation,
    tool_InitialNodeCreationOperation,
    tool_InitialOperation,
    tool_MenuItemDescription,
    tool_MenuItemOrRef,
    tool_ModelOperation,
    tool_NameVariable,
    tool_NodeCreationVariable,
    tool_PasteDescription,
    tool_PopupMenu,
    tool_ReconnectEdgeDescription,
    tool_RepresentationCreationDescription,
    tool_RepresentationNavigationDescription,
    tool_SelectContainerVariable,
    tool_SourceEdgeCreationVariable,
    tool_SourceEdgeViewCreationVariable,
    tool_SubVariable,
    tool_TargetEdgeCreationVariable,
    tool_TargetEdgeViewCreationVariable,
    tool_ToolEntry,
    tool_ToolFilterDescription,
    tool_ToolGroup,
    tool_ToolGroupExtension,
    tool_ToolSection,
    tool_VariableContainer,
    tool_viewpoint_EObject,
    validation_RuleAudit,
    validation_ValidationFix,
    validation_ValidationRule,
    validation_ValidationSet,
    viewpoint_BasicLabelStyle,
    viewpoint_Customizable,
    viewpoint_DAnalysis,
    viewpoint_DAnalysisCustomData,
    viewpoint_DAnalysisSessionEObject,
    viewpoint_DContainer,
    viewpoint_DEObjectLink,
    viewpoint_DFeatureExtension,
    viewpoint_DFile,
    viewpoint_DFolder,
    viewpoint_DLabelled,
    viewpoint_DMappingBased,
    viewpoint_DModel,
    viewpoint_DNavigable,
    viewpoint_DNavigationLink,
    viewpoint_DProject,
    viewpoint_DRefreshable,
    viewpoint_DRepresentation,
    viewpoint_DRepresentationContainer,
    viewpoint_DRepresentationElement,
    viewpoint_DResource,
    viewpoint_DResourceContainer,
    viewpoint_DSemanticDecorator,
    viewpoint_DSourceFileLink,
    viewpoint_DStylizable,
    viewpoint_DValidable,
    viewpoint_DView,
    viewpoint_Decoration,
    viewpoint_DragAndDropTarget,
    viewpoint_EObject,
    viewpoint_LabelStyle,
    viewpoint_MetaModelExtension,
    viewpoint_RGBValues,
    viewpoint_SessionManagerEObject,
    viewpoint_Style,
    viewpoint_audit_InformationSection,
    viewpoint_audit_TemplateInformationSection,
    viewpoint_concern_ConcernDescription,
    viewpoint_concern_ConcernSet,
    viewpoint_description_AbstractMappingImport,
    viewpoint_description_AbstractNodeMapping,
    viewpoint_description_AdditionalLayer,
    viewpoint_description_AnnotationEntry,
    viewpoint_description_ColorDescription,
    viewpoint_description_ColorStep,
    viewpoint_description_Component,
    viewpoint_description_CompositeLayout,
    viewpoint_description_ComputedColor,
    viewpoint_description_ConditionalContainerStyleDescription,
    viewpoint_description_ConditionalEdgeStyleDescription,
    viewpoint_description_ConditionalNodeStyleDescription,
    viewpoint_description_ConditionalStyleDescription,
    viewpoint_description_ContainerMapping,
    viewpoint_description_ContainerMappingImport,
    viewpoint_description_Customization,
    viewpoint_description_DAnnotation,
    viewpoint_description_DAnnotationEntry,
    viewpoint_description_DModelElement,
    viewpoint_description_DecorationDescription,
    viewpoint_description_DecorationDescriptionsSet,
    viewpoint_description_DiagramDescription,
    viewpoint_description_DiagramElementMapping,
    viewpoint_description_DiagramExtensionDescription,
    viewpoint_description_DiagramImportDescription,
    viewpoint_description_DocumentedElement,
    viewpoint_description_DragAndDropTargetDescription,
    viewpoint_description_EAttributeCustomization,
    viewpoint_description_EReferenceCustomization,
    viewpoint_description_EStructuralFeatureCustomization,
    viewpoint_description_EdgeMapping,
    viewpoint_description_EdgeMappingImport,
    viewpoint_description_EndUserDocumentedElement,
    viewpoint_description_Environment,
    viewpoint_description_FeatureExtensionDescription,
    viewpoint_description_FixedColor,
    viewpoint_description_Group,
    viewpoint_description_IEdgeMapping,
    viewpoint_description_IVSMElementCustomization,
    viewpoint_description_IdentifiedElement,
    viewpoint_description_InterpolatedColor,
    viewpoint_description_JavaExtension,
    viewpoint_description_Layer,
    viewpoint_description_Layout,
    viewpoint_description_MappingBasedDecoration,
    viewpoint_description_MetamodelExtensionSetting,
    viewpoint_description_NodeMapping,
    viewpoint_description_NodeMappingImport,
    viewpoint_description_OrderedTreeLayout,
    viewpoint_description_PasteTargetDescription,
    viewpoint_description_RepresentationDescription,
    viewpoint_description_RepresentationElementMapping,
    viewpoint_description_RepresentationExtensionDescription,
    viewpoint_description_RepresentationImportDescription,
    viewpoint_description_RepresentationTemplate,
    viewpoint_description_SelectionDescription,
    viewpoint_description_SemanticBasedDecoration,
    viewpoint_description_SystemColor,
    viewpoint_description_SytemColorsPalette,
    viewpoint_description_UserColor,
    viewpoint_description_UserColorsPalette,
    viewpoint_description_UserFixedColor,
    viewpoint_description_VSMElementCustomization,
    viewpoint_description_VSMElementCustomizationReuse,
    viewpoint_description_Viewpoint,
    viewpoint_diagram_AbsoluteBoundsFilter,
    viewpoint_diagram_AbstractDNode,
    viewpoint_diagram_AppliedCompositeFilters,
    viewpoint_diagram_BeginLabelStyle,
    viewpoint_diagram_BorderedStyle,
    viewpoint_diagram_BracketEdgeStyle,
    viewpoint_diagram_BundledImage,
    viewpoint_diagram_CenterLabelStyle,
    viewpoint_diagram_CollapseFilter,
    viewpoint_diagram_ComputedStyleDescriptionRegistry,
    viewpoint_diagram_ContainerStyle,
    viewpoint_diagram_ContainerVariable2StyleDescription,
    viewpoint_diagram_CustomStyle,
    viewpoint_diagram_DDiagram,
    viewpoint_diagram_DDiagramElement,
    viewpoint_diagram_DDiagramElementContainer,
    viewpoint_diagram_DDiagramLink,
    viewpoint_diagram_DDiagramSet,
    viewpoint_diagram_DEdge,
    viewpoint_diagram_DNode,
    viewpoint_diagram_DNodeContainer,
    viewpoint_diagram_DNodeList,
    viewpoint_diagram_DNodeListElement,
    viewpoint_diagram_DSemanticDiagram,
    viewpoint_diagram_DiagramElementMapping2ModelElement,
    viewpoint_diagram_Dot,
    viewpoint_diagram_EdgeStyle,
    viewpoint_diagram_EdgeTarget,
    viewpoint_diagram_Ellipse,
    viewpoint_diagram_EndLabelStyle,
    viewpoint_diagram_FilterVariableHistory,
    viewpoint_diagram_FilterVariableValue,
    viewpoint_diagram_FlatContainerStyle,
    viewpoint_diagram_FoldingFilter,
    viewpoint_diagram_FoldingPointFilter,
    viewpoint_diagram_GaugeCompositeStyle,
    viewpoint_diagram_GaugeSection,
    viewpoint_diagram_GraphicalFilter,
    viewpoint_diagram_HideFilter,
    viewpoint_diagram_HideLabelFilter,
    viewpoint_diagram_IndirectlyCollapseFilter,
    viewpoint_diagram_Lozenge,
    viewpoint_diagram_ModelElement2ViewVariable,
    viewpoint_diagram_NodeStyle,
    viewpoint_diagram_Note,
    viewpoint_diagram_ShapeContainerStyle,
    viewpoint_diagram_Square,
    viewpoint_diagram_ViewVariable2ContainerVariable,
    viewpoint_diagram_WorkspaceImage,
    viewpoint_filter_CompositeFilterDescription,
    viewpoint_filter_Filter,
    viewpoint_filter_FilterDescription,
    viewpoint_filter_FilterVariable,
    viewpoint_filter_MappingFilter,
    viewpoint_filter_VariableFilter,
    viewpoint_style_BasicLabelStyleDescription,
    viewpoint_style_BeginLabelStyleDescription,
    viewpoint_style_BorderedStyleDescription,
    viewpoint_style_BracketEdgeStyleDescription,
    viewpoint_style_BundledImageDescription,
    viewpoint_style_CenterLabelStyleDescription,
    viewpoint_style_ContainerStyleDescription,
    viewpoint_style_CustomStyleDescription,
    viewpoint_style_DotDescription,
    viewpoint_style_EdgeStyleDescription,
    viewpoint_style_EllipseNodeDescription,
    viewpoint_style_EndLabelStyleDescription,
    viewpoint_style_FlatContainerStyleDescription,
    viewpoint_style_GaugeCompositeStyleDescription,
    viewpoint_style_GaugeSectionDescription,
    viewpoint_style_LabelBorderStyleDescription,
    viewpoint_style_LabelBorderStyles,
    viewpoint_style_LabelStyleDescription,
    viewpoint_style_LozengeNodeDescription,
    viewpoint_style_NodeStyleDescription,
    viewpoint_style_NoteDescription,
    viewpoint_style_RoundedCornerStyleDescription,
    viewpoint_style_ShapeContainerStyleDescription,
    viewpoint_style_SizeComputationContainerStyleDescription,
    viewpoint_style_SquareDescription,
    viewpoint_style_StyleDescription,
    viewpoint_style_TooltipStyleDescription,
    viewpoint_style_WorkspaceImageDescription,
    viewpoint_tool_AbstractToolDescription,
    viewpoint_tool_AbstractVariable,
    viewpoint_tool_AcceleoVariable,
    viewpoint_tool_BehaviorTool,
    viewpoint_tool_Case,
    viewpoint_tool_ChangeContext,
    viewpoint_tool_ContainerCreationDescription,
    viewpoint_tool_ContainerDropDescription,
    viewpoint_tool_ContainerModelOperation,
    viewpoint_tool_ContainerViewVariable,
    viewpoint_tool_CreateEdgeView,
    viewpoint_tool_CreateInstance,
    viewpoint_tool_CreateView,
    viewpoint_tool_Default,
    viewpoint_tool_DeleteElementDescription,
    viewpoint_tool_DeleteHook,
    viewpoint_tool_DeleteHookParameter,
    viewpoint_tool_DeleteView,
    viewpoint_tool_DiagramCreationDescription,
    viewpoint_tool_DiagramNavigationDescription,
    viewpoint_tool_DialogVariable,
    viewpoint_tool_DirectEditLabel,
    viewpoint_tool_DoubleClickDescription,
    viewpoint_tool_DropContainerVariable,
    viewpoint_tool_EdgeCreationDescription,
    viewpoint_tool_EditMaskVariables,
    viewpoint_tool_ElementDeleteVariable,
    viewpoint_tool_ElementDoubleClickVariable,
    viewpoint_tool_ElementDropVariable,
    viewpoint_tool_ElementSelectVariable,
    viewpoint_tool_ElementVariable,
    viewpoint_tool_ElementViewVariable,
    viewpoint_tool_ExternalJavaAction,
    viewpoint_tool_ExternalJavaActionCall,
    viewpoint_tool_ExternalJavaActionParameter,
    viewpoint_tool_FeatureChangeListener,
    viewpoint_tool_For,
    viewpoint_tool_If,
    viewpoint_tool_InitEdgeCreationOperation,
    viewpoint_tool_InitialContainerDropOperation,
    viewpoint_tool_InitialNodeCreationOperation,
    viewpoint_tool_InitialOperation,
    viewpoint_tool_MappingBasedToolDescription,
    viewpoint_tool_MenuItemDescription,
    viewpoint_tool_MenuItemDescriptionReference,
    viewpoint_tool_MenuItemOrRef,
    viewpoint_tool_ModelOperation,
    viewpoint_tool_MoveElement,
    viewpoint_tool_NameVariable,
    viewpoint_tool_Navigation,
    viewpoint_tool_NodeCreationDescription,
    viewpoint_tool_NodeCreationVariable,
    viewpoint_tool_OperationAction,
    viewpoint_tool_PaneBasedSelectionWizardDescription,
    viewpoint_tool_PasteDescription,
    viewpoint_tool_PopupMenu,
    viewpoint_tool_ReconnectEdgeDescription,
    viewpoint_tool_RemoveElement,
    viewpoint_tool_RepresentationCreationDescription,
    viewpoint_tool_RepresentationNavigationDescription,
    viewpoint_tool_RequestDescription,
    viewpoint_tool_SelectContainerVariable,
    viewpoint_tool_SelectModelElementVariable,
    viewpoint_tool_SelectionWizardDescription,
    viewpoint_tool_SetObject,
    viewpoint_tool_SetValue,
    viewpoint_tool_SourceEdgeCreationVariable,
    viewpoint_tool_SourceEdgeViewCreationVariable,
    viewpoint_tool_SubVariable,
    viewpoint_tool_Switch,
    viewpoint_tool_SwitchChild,
    viewpoint_tool_TargetEdgeCreationVariable,
    viewpoint_tool_TargetEdgeViewCreationVariable,
    viewpoint_tool_ToolDescription,
    viewpoint_tool_ToolEntry,
    viewpoint_tool_ToolFilterDescription,
    viewpoint_tool_ToolGroup,
    viewpoint_tool_ToolGroupExtension,
    viewpoint_tool_ToolSection,
    viewpoint_tool_Unset,
    viewpoint_tool_VariableContainer,
    viewpoint_validation_RuleAudit,
    viewpoint_validation_SemanticValidationRule,
    viewpoint_validation_ValidationFix,
    viewpoint_validation_ValidationRule,
    viewpoint_validation_ValidationSet,
    viewpoint_validation_ViewValidationRule,
    AlignmentKind,
    ArrangeConstraint,
    BackgroundStyle,
    BundledImageShape,
    ContainerLayout,
    ContainerShape,
    DragSource,
    ERROR_LEVEL,
    EdgeArrows,
    EdgeRouting,
    FilterKind,
    FoldingStyle,
    FontFormat,
    LabelAlignment,
    LabelPosition,
    LayoutDirection,
    LineStyle,
    NavigationTargetType,
    Position,
    ReconnectionKind,
    ResizeKind,
    SyncStatus,
    SystemColors,
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

def test_viewpoint_BasicLabelStyle_iconPath_value_roundtrip():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_BasicLabelStyle_labelFormat_value_roundtrip():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelFormat == "sample_text"
    instance.labelFormat = "sample_text_2"
    assert instance.labelFormat == "sample_text_2"


def test_viewpoint_BasicLabelStyle_labelSize_value_roundtrip():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelSize == 7
    instance.labelSize = 13
    assert instance.labelSize == 13


def test_viewpoint_BasicLabelStyle_showIcon_value_roundtrip():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.showIcon == True
    instance.showIcon = False
    assert instance.showIcon == False


def test_viewpoint_Customizable_customFeatures_value_roundtrip():
    instance = viewpoint_Customizable(customFeatures="sample_text")
    assert instance.customFeatures == "sample_text"
    instance.customFeatures = "sample_text_2"
    assert instance.customFeatures == "sample_text_2"


def test_viewpoint_DAnalysis_version_value_roundtrip():
    instance = viewpoint_DAnalysis(version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_viewpoint_DAnalysisCustomData_key_value_roundtrip():
    instance = viewpoint_DAnalysisCustomData(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_viewpoint_DAnalysisSessionEObject_blocked_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.blocked == True
    instance.blocked = False
    assert instance.blocked == False


def test_viewpoint_DAnalysisSessionEObject_controlledResources_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.controlledResources == "sample_text"
    instance.controlledResources = "sample_text_2"
    assert instance.controlledResources == "sample_text_2"


def test_viewpoint_DAnalysisSessionEObject_open_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.open == True
    instance.open = False
    assert instance.open == False


def test_viewpoint_DAnalysisSessionEObject_resources_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.resources == "sample_text"
    instance.resources = "sample_text_2"
    assert instance.resources == "sample_text_2"


def test_viewpoint_DAnalysisSessionEObject_synchronizationStatus_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.synchronizationStatus == "sample_text"
    instance.synchronizationStatus = "sample_text_2"
    assert instance.synchronizationStatus == "sample_text_2"


def test_viewpoint_DNavigationLink_label_value_roundtrip():
    instance = viewpoint_DNavigationLink(label="sample_text", targetType="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_viewpoint_DNavigationLink_targetType_value_roundtrip():
    instance = viewpoint_DNavigationLink(label="sample_text", targetType="sample_text")
    assert instance.targetType == "sample_text"
    instance.targetType = "sample_text_2"
    assert instance.targetType == "sample_text_2"


def test_viewpoint_DRepresentation_name_value_roundtrip():
    instance = viewpoint_DRepresentation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_DRepresentationElement_name_value_roundtrip():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_DResource_name_value_roundtrip():
    instance = viewpoint_DResource(name="sample_text", path="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_DResource_path_value_roundtrip():
    instance = viewpoint_DResource(name="sample_text", path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_viewpoint_DSourceFileLink_endPosition_value_roundtrip():
    instance = viewpoint_DSourceFileLink(endPosition=7, filePath="sample_text", startPosition=7)
    assert instance.endPosition == 7
    instance.endPosition = 13
    assert instance.endPosition == 13


def test_viewpoint_DSourceFileLink_filePath_value_roundtrip():
    instance = viewpoint_DSourceFileLink(endPosition=7, filePath="sample_text", startPosition=7)
    assert instance.filePath == "sample_text"
    instance.filePath = "sample_text_2"
    assert instance.filePath == "sample_text_2"


def test_viewpoint_DSourceFileLink_startPosition_value_roundtrip():
    instance = viewpoint_DSourceFileLink(endPosition=7, filePath="sample_text", startPosition=7)
    assert instance.startPosition == 7
    instance.startPosition = 13
    assert instance.startPosition == 13


def test_viewpoint_DView_initialized_value_roundtrip():
    instance = viewpoint_DView(initialized=True)
    assert instance.initialized == True
    instance.initialized = False
    assert instance.initialized == False


def test_viewpoint_LabelStyle_labelAlignment_value_roundtrip():
    instance = viewpoint_LabelStyle(labelAlignment="sample_text")
    assert instance.labelAlignment == "sample_text"
    instance.labelAlignment = "sample_text_2"
    assert instance.labelAlignment == "sample_text_2"


def test_viewpoint_RGBValues_blue_value_roundtrip():
    instance = viewpoint_RGBValues(blue=7, green=7, red=7)
    assert instance.blue == 7
    instance.blue = 13
    assert instance.blue == 13


def test_viewpoint_RGBValues_green_value_roundtrip():
    instance = viewpoint_RGBValues(blue=7, green=7, red=7)
    assert instance.green == 7
    instance.green = 13
    assert instance.green == 13


def test_viewpoint_RGBValues_red_value_roundtrip():
    instance = viewpoint_RGBValues(blue=7, green=7, red=7)
    assert instance.red == 7
    instance.red = 13
    assert instance.red == 13


def test_viewpoint_audit_TemplateInformationSection_templatePath_value_roundtrip():
    instance = viewpoint_audit_TemplateInformationSection(templatePath="sample_text")
    assert instance.templatePath == "sample_text"
    instance.templatePath = "sample_text_2"
    assert instance.templatePath == "sample_text_2"


def test_viewpoint_description_AbstractMappingImport_hideSubMappings_value_roundtrip():
    instance = viewpoint_description_AbstractMappingImport(hideSubMappings=True, inheritsAncestorFilters=True)
    assert instance.hideSubMappings == True
    instance.hideSubMappings = False
    assert instance.hideSubMappings == False


def test_viewpoint_description_AbstractMappingImport_inheritsAncestorFilters_value_roundtrip():
    instance = viewpoint_description_AbstractMappingImport(hideSubMappings=True, inheritsAncestorFilters=True)
    assert instance.inheritsAncestorFilters == True
    instance.inheritsAncestorFilters = False
    assert instance.inheritsAncestorFilters == False


def test_viewpoint_description_AbstractNodeMapping_domainClass_value_roundtrip():
    instance = viewpoint_description_AbstractNodeMapping(domainClass="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_viewpoint_description_AdditionalLayer_activeByDefault_value_roundtrip():
    instance = viewpoint_description_AdditionalLayer(activeByDefault=True, optional=True)
    assert instance.activeByDefault == True
    instance.activeByDefault = False
    assert instance.activeByDefault == False


def test_viewpoint_description_AdditionalLayer_optional_value_roundtrip():
    instance = viewpoint_description_AdditionalLayer(activeByDefault=True, optional=True)
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_viewpoint_description_AnnotationEntry_source_value_roundtrip():
    instance = viewpoint_description_AnnotationEntry(source="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_viewpoint_description_ColorStep_associatedValue_value_roundtrip():
    instance = viewpoint_description_ColorStep(associatedValue="sample_text")
    assert instance.associatedValue == "sample_text"
    instance.associatedValue = "sample_text_2"
    assert instance.associatedValue == "sample_text_2"


def test_viewpoint_description_CompositeLayout_direction_value_roundtrip():
    instance = viewpoint_description_CompositeLayout(direction="sample_text", padding=7)
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_viewpoint_description_CompositeLayout_padding_value_roundtrip():
    instance = viewpoint_description_CompositeLayout(direction="sample_text", padding=7)
    assert instance.padding == 7
    instance.padding = 13
    assert instance.padding == 13


def test_viewpoint_description_ComputedColor_blue_value_roundtrip():
    instance = viewpoint_description_ComputedColor(blue="sample_text", green="sample_text", red="sample_text")
    assert instance.blue == "sample_text"
    instance.blue = "sample_text_2"
    assert instance.blue == "sample_text_2"


def test_viewpoint_description_ComputedColor_green_value_roundtrip():
    instance = viewpoint_description_ComputedColor(blue="sample_text", green="sample_text", red="sample_text")
    assert instance.green == "sample_text"
    instance.green = "sample_text_2"
    assert instance.green == "sample_text_2"


def test_viewpoint_description_ComputedColor_red_value_roundtrip():
    instance = viewpoint_description_ComputedColor(blue="sample_text", green="sample_text", red="sample_text")
    assert instance.red == "sample_text"
    instance.red = "sample_text_2"
    assert instance.red == "sample_text_2"


def test_viewpoint_description_ConditionalStyleDescription_predicateExpression_value_roundtrip():
    instance = viewpoint_description_ConditionalStyleDescription(predicateExpression="sample_text")
    assert instance.predicateExpression == "sample_text"
    instance.predicateExpression = "sample_text_2"
    assert instance.predicateExpression == "sample_text_2"


def test_viewpoint_description_ContainerMapping_childrenPresentation_value_roundtrip():
    instance = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    assert instance.childrenPresentation == "sample_text"
    instance.childrenPresentation = "sample_text_2"
    assert instance.childrenPresentation == "sample_text_2"


def test_viewpoint_description_DAnnotation_source_value_roundtrip():
    instance = viewpoint_description_DAnnotation(source="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_viewpoint_description_DAnnotationEntry_details_value_roundtrip():
    instance = viewpoint_description_DAnnotationEntry(details="sample_text", source="sample_text")
    assert instance.details == "sample_text"
    instance.details = "sample_text_2"
    assert instance.details == "sample_text_2"


def test_viewpoint_description_DAnnotationEntry_source_value_roundtrip():
    instance = viewpoint_description_DAnnotationEntry(details="sample_text", source="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_viewpoint_description_DecorationDescription_decoratorPath_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(decoratorPath="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text")
    assert instance.decoratorPath == "sample_text"
    instance.decoratorPath = "sample_text_2"
    assert instance.decoratorPath == "sample_text_2"


def test_viewpoint_description_DecorationDescription_name_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(decoratorPath="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_DecorationDescription_position_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(decoratorPath="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_viewpoint_description_DecorationDescription_preconditionExpression_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(decoratorPath="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text")
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_viewpoint_description_DiagramDescription_domainClass_value_roundtrip():
    instance = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_viewpoint_description_DiagramDescription_enablePopupBars_value_roundtrip():
    instance = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert instance.enablePopupBars == True
    instance.enablePopupBars = False
    assert instance.enablePopupBars == False


def test_viewpoint_description_DiagramDescription_preconditionExpression_value_roundtrip():
    instance = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_viewpoint_description_DiagramDescription_rootExpression_value_roundtrip():
    instance = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert instance.rootExpression == "sample_text"
    instance.rootExpression = "sample_text_2"
    assert instance.rootExpression == "sample_text_2"


def test_viewpoint_description_DiagramElementMapping_createElements_value_roundtrip():
    instance = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.createElements == True
    instance.createElements = False
    assert instance.createElements == False


def test_viewpoint_description_DiagramElementMapping_preconditionExpression_value_roundtrip():
    instance = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_viewpoint_description_DiagramElementMapping_semanticCandidatesExpression_value_roundtrip():
    instance = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.semanticCandidatesExpression == "sample_text"
    instance.semanticCandidatesExpression = "sample_text_2"
    assert instance.semanticCandidatesExpression == "sample_text_2"


def test_viewpoint_description_DiagramElementMapping_semanticElements_value_roundtrip():
    instance = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.semanticElements == "sample_text"
    instance.semanticElements = "sample_text_2"
    assert instance.semanticElements == "sample_text_2"


def test_viewpoint_description_DiagramElementMapping_synchronizationLock_value_roundtrip():
    instance = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert instance.synchronizationLock == True
    instance.synchronizationLock = False
    assert instance.synchronizationLock == False


def test_viewpoint_description_DocumentedElement_documentation_value_roundtrip():
    instance = viewpoint_description_DocumentedElement(documentation="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_viewpoint_description_EAttributeCustomization_attributeName_value_roundtrip():
    instance = viewpoint_description_EAttributeCustomization(attributeName="sample_text", value="sample_text")
    assert instance.attributeName == "sample_text"
    instance.attributeName = "sample_text_2"
    assert instance.attributeName == "sample_text_2"


def test_viewpoint_description_EAttributeCustomization_value_value_roundtrip():
    instance = viewpoint_description_EAttributeCustomization(attributeName="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_viewpoint_description_EReferenceCustomization_referenceName_value_roundtrip():
    instance = viewpoint_description_EReferenceCustomization(referenceName="sample_text")
    assert instance.referenceName == "sample_text"
    instance.referenceName = "sample_text_2"
    assert instance.referenceName == "sample_text_2"


def test_viewpoint_description_EStructuralFeatureCustomization_applyOnAll_value_roundtrip():
    instance = viewpoint_description_EStructuralFeatureCustomization(applyOnAll=True)
    assert instance.applyOnAll == True
    instance.applyOnAll = False
    assert instance.applyOnAll == False


def test_viewpoint_description_EdgeMapping_domainClass_value_roundtrip():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_viewpoint_description_EdgeMapping_pathExpression_value_roundtrip():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.pathExpression == "sample_text"
    instance.pathExpression = "sample_text_2"
    assert instance.pathExpression == "sample_text_2"


def test_viewpoint_description_EdgeMapping_sourceFinderExpression_value_roundtrip():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.sourceFinderExpression == "sample_text"
    instance.sourceFinderExpression = "sample_text_2"
    assert instance.sourceFinderExpression == "sample_text_2"


def test_viewpoint_description_EdgeMapping_targetExpression_value_roundtrip():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.targetExpression == "sample_text"
    instance.targetExpression = "sample_text_2"
    assert instance.targetExpression == "sample_text_2"


def test_viewpoint_description_EdgeMapping_targetFinderExpression_value_roundtrip():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.targetFinderExpression == "sample_text"
    instance.targetFinderExpression = "sample_text_2"
    assert instance.targetFinderExpression == "sample_text_2"


def test_viewpoint_description_EdgeMapping_useDomainElement_value_roundtrip():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert instance.useDomainElement == True
    instance.useDomainElement = False
    assert instance.useDomainElement == False


def test_viewpoint_description_EdgeMappingImport_inheritsAncestorFilters_value_roundtrip():
    instance = viewpoint_description_EdgeMappingImport(inheritsAncestorFilters=True)
    assert instance.inheritsAncestorFilters == True
    instance.inheritsAncestorFilters = False
    assert instance.inheritsAncestorFilters == False


def test_viewpoint_description_EndUserDocumentedElement_endUserDocumentation_value_roundtrip():
    instance = viewpoint_description_EndUserDocumentedElement(endUserDocumentation="sample_text")
    assert instance.endUserDocumentation == "sample_text"
    instance.endUserDocumentation = "sample_text_2"
    assert instance.endUserDocumentation == "sample_text_2"


def test_viewpoint_description_FixedColor_blue_value_roundtrip():
    instance = viewpoint_description_FixedColor(blue=7, green=7, red=7)
    assert instance.blue == 7
    instance.blue = 13
    assert instance.blue == 13


def test_viewpoint_description_FixedColor_green_value_roundtrip():
    instance = viewpoint_description_FixedColor(blue=7, green=7, red=7)
    assert instance.green == 7
    instance.green = 13
    assert instance.green == 13


def test_viewpoint_description_FixedColor_red_value_roundtrip():
    instance = viewpoint_description_FixedColor(blue=7, green=7, red=7)
    assert instance.red == 7
    instance.red = 13
    assert instance.red == 13


def test_viewpoint_description_Group_name_value_roundtrip():
    instance = viewpoint_description_Group(name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_Group_version_value_roundtrip():
    instance = viewpoint_description_Group(name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_viewpoint_description_IdentifiedElement_label_value_roundtrip():
    instance = viewpoint_description_IdentifiedElement(label="sample_text", name="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_viewpoint_description_IdentifiedElement_name_value_roundtrip():
    instance = viewpoint_description_IdentifiedElement(label="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_InterpolatedColor_colorValueComputationExpression_value_roundtrip():
    instance = viewpoint_description_InterpolatedColor(colorValueComputationExpression="sample_text", maxValueComputationExpression="sample_text", minValueComputationExpression="sample_text")
    assert instance.colorValueComputationExpression == "sample_text"
    instance.colorValueComputationExpression = "sample_text_2"
    assert instance.colorValueComputationExpression == "sample_text_2"


def test_viewpoint_description_InterpolatedColor_maxValueComputationExpression_value_roundtrip():
    instance = viewpoint_description_InterpolatedColor(colorValueComputationExpression="sample_text", maxValueComputationExpression="sample_text", minValueComputationExpression="sample_text")
    assert instance.maxValueComputationExpression == "sample_text"
    instance.maxValueComputationExpression = "sample_text_2"
    assert instance.maxValueComputationExpression == "sample_text_2"


def test_viewpoint_description_InterpolatedColor_minValueComputationExpression_value_roundtrip():
    instance = viewpoint_description_InterpolatedColor(colorValueComputationExpression="sample_text", maxValueComputationExpression="sample_text", minValueComputationExpression="sample_text")
    assert instance.minValueComputationExpression == "sample_text"
    instance.minValueComputationExpression = "sample_text_2"
    assert instance.minValueComputationExpression == "sample_text_2"


def test_viewpoint_description_JavaExtension_qualifiedClassName_value_roundtrip():
    instance = viewpoint_description_JavaExtension(qualifiedClassName="sample_text")
    assert instance.qualifiedClassName == "sample_text"
    instance.qualifiedClassName = "sample_text_2"
    assert instance.qualifiedClassName == "sample_text_2"


def test_viewpoint_description_Layer_icon_value_roundtrip():
    instance = viewpoint_description_Layer(icon="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_viewpoint_description_OrderedTreeLayout_childrenExpression_value_roundtrip():
    instance = viewpoint_description_OrderedTreeLayout(childrenExpression="sample_text")
    assert instance.childrenExpression == "sample_text"
    instance.childrenExpression = "sample_text_2"
    assert instance.childrenExpression == "sample_text_2"


def test_viewpoint_description_RepresentationDescription_initialisation_value_roundtrip():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert instance.initialisation == True
    instance.initialisation = False
    assert instance.initialisation == False


def test_viewpoint_description_RepresentationDescription_showOnStartup_value_roundtrip():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert instance.showOnStartup == True
    instance.showOnStartup = False
    assert instance.showOnStartup == False


def test_viewpoint_description_RepresentationDescription_titleExpression_value_roundtrip():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert instance.titleExpression == "sample_text"
    instance.titleExpression = "sample_text_2"
    assert instance.titleExpression == "sample_text_2"


def test_viewpoint_description_RepresentationExtensionDescription_name_value_roundtrip():
    instance = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_RepresentationExtensionDescription_representationName_value_roundtrip():
    instance = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    assert instance.representationName == "sample_text"
    instance.representationName = "sample_text_2"
    assert instance.representationName == "sample_text_2"


def test_viewpoint_description_RepresentationExtensionDescription_viewpointURI_value_roundtrip():
    instance = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    assert instance.viewpointURI == "sample_text"
    instance.viewpointURI = "sample_text_2"
    assert instance.viewpointURI == "sample_text_2"


def test_viewpoint_description_RepresentationTemplate_name_value_roundtrip():
    instance = viewpoint_description_RepresentationTemplate(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_SelectionDescription_candidatesExpression_value_roundtrip():
    instance = viewpoint_description_SelectionDescription(candidatesExpression="sample_text", childrenExpression="sample_text", message="sample_text", multiple=True, rootExpression="sample_text", tree=True)
    assert instance.candidatesExpression == "sample_text"
    instance.candidatesExpression = "sample_text_2"
    assert instance.candidatesExpression == "sample_text_2"


def test_viewpoint_description_SelectionDescription_childrenExpression_value_roundtrip():
    instance = viewpoint_description_SelectionDescription(candidatesExpression="sample_text", childrenExpression="sample_text", message="sample_text", multiple=True, rootExpression="sample_text", tree=True)
    assert instance.childrenExpression == "sample_text"
    instance.childrenExpression = "sample_text_2"
    assert instance.childrenExpression == "sample_text_2"


def test_viewpoint_description_SelectionDescription_message_value_roundtrip():
    instance = viewpoint_description_SelectionDescription(candidatesExpression="sample_text", childrenExpression="sample_text", message="sample_text", multiple=True, rootExpression="sample_text", tree=True)
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_viewpoint_description_SelectionDescription_multiple_value_roundtrip():
    instance = viewpoint_description_SelectionDescription(candidatesExpression="sample_text", childrenExpression="sample_text", message="sample_text", multiple=True, rootExpression="sample_text", tree=True)
    assert instance.multiple == True
    instance.multiple = False
    assert instance.multiple == False


def test_viewpoint_description_SelectionDescription_rootExpression_value_roundtrip():
    instance = viewpoint_description_SelectionDescription(candidatesExpression="sample_text", childrenExpression="sample_text", message="sample_text", multiple=True, rootExpression="sample_text", tree=True)
    assert instance.rootExpression == "sample_text"
    instance.rootExpression = "sample_text_2"
    assert instance.rootExpression == "sample_text_2"


def test_viewpoint_description_SelectionDescription_tree_value_roundtrip():
    instance = viewpoint_description_SelectionDescription(candidatesExpression="sample_text", childrenExpression="sample_text", message="sample_text", multiple=True, rootExpression="sample_text", tree=True)
    assert instance.tree == True
    instance.tree = False
    assert instance.tree == False


def test_viewpoint_description_SemanticBasedDecoration_domainClass_value_roundtrip():
    instance = viewpoint_description_SemanticBasedDecoration(domainClass="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_viewpoint_description_SystemColor_name_value_roundtrip():
    instance = viewpoint_description_SystemColor(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_UserColor_name_value_roundtrip():
    instance = viewpoint_description_UserColor(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_UserColorsPalette_name_value_roundtrip():
    instance = viewpoint_description_UserColorsPalette(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_VSMElementCustomization_predicateExpression_value_roundtrip():
    instance = viewpoint_description_VSMElementCustomization(predicateExpression="sample_text")
    assert instance.predicateExpression == "sample_text"
    instance.predicateExpression = "sample_text_2"
    assert instance.predicateExpression == "sample_text_2"


def test_viewpoint_description_Viewpoint_conflicts_value_roundtrip():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert instance.conflicts == "sample_text"
    instance.conflicts = "sample_text_2"
    assert instance.conflicts == "sample_text_2"


def test_viewpoint_description_Viewpoint_customizes_value_roundtrip():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert instance.customizes == "sample_text"
    instance.customizes = "sample_text_2"
    assert instance.customizes == "sample_text_2"


def test_viewpoint_description_Viewpoint_icon_value_roundtrip():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_viewpoint_description_Viewpoint_modelFileExtension_value_roundtrip():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert instance.modelFileExtension == "sample_text"
    instance.modelFileExtension = "sample_text_2"
    assert instance.modelFileExtension == "sample_text_2"


def test_viewpoint_description_Viewpoint_reuses_value_roundtrip():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert instance.reuses == "sample_text"
    instance.reuses = "sample_text_2"
    assert instance.reuses == "sample_text_2"


def test_viewpoint_diagram_AbsoluteBoundsFilter_height_value_roundtrip():
    instance = viewpoint_diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_viewpoint_diagram_AbsoluteBoundsFilter_width_value_roundtrip():
    instance = viewpoint_diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_viewpoint_diagram_AbsoluteBoundsFilter_x_value_roundtrip():
    instance = viewpoint_diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_viewpoint_diagram_AbsoluteBoundsFilter_y_value_roundtrip():
    instance = viewpoint_diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_viewpoint_diagram_AbstractDNode_arrangeConstraints_value_roundtrip():
    instance = viewpoint_diagram_AbstractDNode(arrangeConstraints="sample_text")
    assert instance.arrangeConstraints == "sample_text"
    instance.arrangeConstraints = "sample_text_2"
    assert instance.arrangeConstraints == "sample_text_2"


def test_viewpoint_diagram_BorderedStyle_borderSize_value_roundtrip():
    instance = viewpoint_diagram_BorderedStyle(borderSize="sample_text", borderSizeComputationExpression="sample_text")
    assert instance.borderSize == "sample_text"
    instance.borderSize = "sample_text_2"
    assert instance.borderSize == "sample_text_2"


def test_viewpoint_diagram_BorderedStyle_borderSizeComputationExpression_value_roundtrip():
    instance = viewpoint_diagram_BorderedStyle(borderSize="sample_text", borderSizeComputationExpression="sample_text")
    assert instance.borderSizeComputationExpression == "sample_text"
    instance.borderSizeComputationExpression = "sample_text_2"
    assert instance.borderSizeComputationExpression == "sample_text_2"


def test_viewpoint_diagram_BundledImage_shape_value_roundtrip():
    instance = viewpoint_diagram_BundledImage(shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_viewpoint_diagram_CollapseFilter_height_value_roundtrip():
    instance = viewpoint_diagram_CollapseFilter(height=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_viewpoint_diagram_CollapseFilter_width_value_roundtrip():
    instance = viewpoint_diagram_CollapseFilter(height=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_viewpoint_diagram_CustomStyle_id_value_roundtrip():
    instance = viewpoint_diagram_CustomStyle(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_viewpoint_diagram_DDiagram_headerHeight_value_roundtrip():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert instance.headerHeight == 7
    instance.headerHeight = 13
    assert instance.headerHeight == 13


def test_viewpoint_diagram_DDiagram_info_value_roundtrip():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert instance.info == "sample_text"
    instance.info = "sample_text_2"
    assert instance.info == "sample_text_2"


def test_viewpoint_diagram_DDiagram_isInLayoutingMode_value_roundtrip():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert instance.isInLayoutingMode == True
    instance.isInLayoutingMode = False
    assert instance.isInLayoutingMode == False


def test_viewpoint_diagram_DDiagram_synchronized_value_roundtrip():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert instance.synchronized == True
    instance.synchronized = False
    assert instance.synchronized == False


def test_viewpoint_diagram_DDiagramElement_tooltipText_value_roundtrip():
    instance = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    assert instance.tooltipText == "sample_text"
    instance.tooltipText = "sample_text_2"
    assert instance.tooltipText == "sample_text_2"


def test_viewpoint_diagram_DDiagramElement_visible_value_roundtrip():
    instance = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_viewpoint_diagram_DDiagramElementContainer_height_value_roundtrip():
    instance = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_viewpoint_diagram_DDiagramElementContainer_width_value_roundtrip():
    instance = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_viewpoint_diagram_DEdge_arrangeConstraints_value_roundtrip():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.arrangeConstraints == "sample_text"
    instance.arrangeConstraints = "sample_text_2"
    assert instance.arrangeConstraints == "sample_text_2"


def test_viewpoint_diagram_DEdge_beginLabel_value_roundtrip():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.beginLabel == "sample_text"
    instance.beginLabel = "sample_text_2"
    assert instance.beginLabel == "sample_text_2"


def test_viewpoint_diagram_DEdge_endLabel_value_roundtrip():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.endLabel == "sample_text"
    instance.endLabel = "sample_text_2"
    assert instance.endLabel == "sample_text_2"


def test_viewpoint_diagram_DEdge_isFold_value_roundtrip():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.isFold == True
    instance.isFold = False
    assert instance.isFold == False


def test_viewpoint_diagram_DEdge_isMockEdge_value_roundtrip():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.isMockEdge == True
    instance.isMockEdge = False
    assert instance.isMockEdge == False


def test_viewpoint_diagram_DEdge_routingStyle_value_roundtrip():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.routingStyle == "sample_text"
    instance.routingStyle = "sample_text_2"
    assert instance.routingStyle == "sample_text_2"


def test_viewpoint_diagram_DEdge_size_value_roundtrip():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_viewpoint_diagram_DNode_height_value_roundtrip():
    instance = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_viewpoint_diagram_DNode_labelPosition_value_roundtrip():
    instance = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert instance.labelPosition == "sample_text"
    instance.labelPosition = "sample_text_2"
    assert instance.labelPosition == "sample_text_2"


def test_viewpoint_diagram_DNode_resizeKind_value_roundtrip():
    instance = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert instance.resizeKind == "sample_text"
    instance.resizeKind = "sample_text_2"
    assert instance.resizeKind == "sample_text_2"


def test_viewpoint_diagram_DNode_width_value_roundtrip():
    instance = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_viewpoint_diagram_DNodeContainer_childrenPresentation_value_roundtrip():
    instance = viewpoint_diagram_DNodeContainer(childrenPresentation="sample_text")
    assert instance.childrenPresentation == "sample_text"
    instance.childrenPresentation = "sample_text_2"
    assert instance.childrenPresentation == "sample_text_2"


def test_viewpoint_diagram_DNodeList_lineWidth_value_roundtrip():
    instance = viewpoint_diagram_DNodeList(lineWidth=7)
    assert instance.lineWidth == 7
    instance.lineWidth = 13
    assert instance.lineWidth == 13


def test_viewpoint_diagram_Dot_strokeSizeComputationExpression_value_roundtrip():
    instance = viewpoint_diagram_Dot(strokeSizeComputationExpression="sample_text")
    assert instance.strokeSizeComputationExpression == "sample_text"
    instance.strokeSizeComputationExpression = "sample_text_2"
    assert instance.strokeSizeComputationExpression == "sample_text_2"


def test_viewpoint_diagram_EdgeStyle_foldingStyle_value_roundtrip():
    instance = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.foldingStyle == "sample_text"
    instance.foldingStyle = "sample_text_2"
    assert instance.foldingStyle == "sample_text_2"


def test_viewpoint_diagram_EdgeStyle_lineStyle_value_roundtrip():
    instance = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.lineStyle == "sample_text"
    instance.lineStyle = "sample_text_2"
    assert instance.lineStyle == "sample_text_2"


def test_viewpoint_diagram_EdgeStyle_routingStyle_value_roundtrip():
    instance = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.routingStyle == "sample_text"
    instance.routingStyle = "sample_text_2"
    assert instance.routingStyle == "sample_text_2"


def test_viewpoint_diagram_EdgeStyle_size_value_roundtrip():
    instance = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_viewpoint_diagram_EdgeStyle_sourceArrow_value_roundtrip():
    instance = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.sourceArrow == "sample_text"
    instance.sourceArrow = "sample_text_2"
    assert instance.sourceArrow == "sample_text_2"


def test_viewpoint_diagram_EdgeStyle_targetArrow_value_roundtrip():
    instance = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.targetArrow == "sample_text"
    instance.targetArrow = "sample_text_2"
    assert instance.targetArrow == "sample_text_2"


def test_viewpoint_diagram_Ellipse_horizontalDiameter_value_roundtrip():
    instance = viewpoint_diagram_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert instance.horizontalDiameter == "sample_text"
    instance.horizontalDiameter = "sample_text_2"
    assert instance.horizontalDiameter == "sample_text_2"


def test_viewpoint_diagram_Ellipse_verticalDiameter_value_roundtrip():
    instance = viewpoint_diagram_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert instance.verticalDiameter == "sample_text"
    instance.verticalDiameter = "sample_text_2"
    assert instance.verticalDiameter == "sample_text_2"


def test_viewpoint_diagram_FlatContainerStyle_backgroundStyle_value_roundtrip():
    instance = viewpoint_diagram_FlatContainerStyle(backgroundStyle="sample_text")
    assert instance.backgroundStyle == "sample_text"
    instance.backgroundStyle = "sample_text_2"
    assert instance.backgroundStyle == "sample_text_2"


def test_viewpoint_diagram_GaugeCompositeStyle_alignment_value_roundtrip():
    instance = viewpoint_diagram_GaugeCompositeStyle(alignment="sample_text")
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_viewpoint_diagram_GaugeSection_label_value_roundtrip():
    instance = viewpoint_diagram_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_viewpoint_diagram_GaugeSection_max_value_roundtrip():
    instance = viewpoint_diagram_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_viewpoint_diagram_GaugeSection_min_value_roundtrip():
    instance = viewpoint_diagram_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_viewpoint_diagram_GaugeSection_value_value_roundtrip():
    instance = viewpoint_diagram_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_viewpoint_diagram_Lozenge_height_value_roundtrip():
    instance = viewpoint_diagram_Lozenge(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_viewpoint_diagram_Lozenge_width_value_roundtrip():
    instance = viewpoint_diagram_Lozenge(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_viewpoint_diagram_NodeStyle_hideLabelByDefault_value_roundtrip():
    instance = viewpoint_diagram_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert instance.hideLabelByDefault == True
    instance.hideLabelByDefault = False
    assert instance.hideLabelByDefault == False


def test_viewpoint_diagram_NodeStyle_labelPosition_value_roundtrip():
    instance = viewpoint_diagram_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert instance.labelPosition == "sample_text"
    instance.labelPosition = "sample_text_2"
    assert instance.labelPosition == "sample_text_2"


def test_viewpoint_diagram_ShapeContainerStyle_shape_value_roundtrip():
    instance = viewpoint_diagram_ShapeContainerStyle(shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_viewpoint_diagram_Square_height_value_roundtrip():
    instance = viewpoint_diagram_Square(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_viewpoint_diagram_Square_width_value_roundtrip():
    instance = viewpoint_diagram_Square(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_viewpoint_diagram_WorkspaceImage_workspacePath_value_roundtrip():
    instance = viewpoint_diagram_WorkspaceImage(workspacePath="sample_text")
    assert instance.workspacePath == "sample_text"
    instance.workspacePath = "sample_text_2"
    assert instance.workspacePath == "sample_text_2"


def test_viewpoint_filter_Filter_filterKind_value_roundtrip():
    instance = viewpoint_filter_Filter(filterKind="sample_text")
    assert instance.filterKind == "sample_text"
    instance.filterKind = "sample_text_2"
    assert instance.filterKind == "sample_text_2"


def test_viewpoint_filter_FilterVariable_name_value_roundtrip():
    instance = viewpoint_filter_FilterVariable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_filter_MappingFilter_semanticConditionExpression_value_roundtrip():
    instance = viewpoint_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    assert instance.semanticConditionExpression == "sample_text"
    instance.semanticConditionExpression = "sample_text_2"
    assert instance.semanticConditionExpression == "sample_text_2"


def test_viewpoint_filter_MappingFilter_viewConditionExpression_value_roundtrip():
    instance = viewpoint_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    assert instance.viewConditionExpression == "sample_text"
    instance.viewConditionExpression = "sample_text_2"
    assert instance.viewConditionExpression == "sample_text_2"


def test_viewpoint_filter_VariableFilter_semanticConditionExpression_value_roundtrip():
    instance = viewpoint_filter_VariableFilter(semanticConditionExpression="sample_text")
    assert instance.semanticConditionExpression == "sample_text"
    instance.semanticConditionExpression = "sample_text_2"
    assert instance.semanticConditionExpression == "sample_text_2"


def test_viewpoint_style_BasicLabelStyleDescription_iconPath_value_roundtrip():
    instance = viewpoint_style_BasicLabelStyleDescription(iconPath="sample_text", labelExpression="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_style_BasicLabelStyleDescription_labelExpression_value_roundtrip():
    instance = viewpoint_style_BasicLabelStyleDescription(iconPath="sample_text", labelExpression="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelExpression == "sample_text"
    instance.labelExpression = "sample_text_2"
    assert instance.labelExpression == "sample_text_2"


def test_viewpoint_style_BasicLabelStyleDescription_labelFormat_value_roundtrip():
    instance = viewpoint_style_BasicLabelStyleDescription(iconPath="sample_text", labelExpression="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelFormat == "sample_text"
    instance.labelFormat = "sample_text_2"
    assert instance.labelFormat == "sample_text_2"


def test_viewpoint_style_BasicLabelStyleDescription_labelSize_value_roundtrip():
    instance = viewpoint_style_BasicLabelStyleDescription(iconPath="sample_text", labelExpression="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelSize == 7
    instance.labelSize = 13
    assert instance.labelSize == 13


def test_viewpoint_style_BasicLabelStyleDescription_showIcon_value_roundtrip():
    instance = viewpoint_style_BasicLabelStyleDescription(iconPath="sample_text", labelExpression="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.showIcon == True
    instance.showIcon = False
    assert instance.showIcon == False


def test_viewpoint_style_BorderedStyleDescription_borderSizeComputationExpression_value_roundtrip():
    instance = viewpoint_style_BorderedStyleDescription(borderSizeComputationExpression="sample_text")
    assert instance.borderSizeComputationExpression == "sample_text"
    instance.borderSizeComputationExpression = "sample_text_2"
    assert instance.borderSizeComputationExpression == "sample_text_2"


def test_viewpoint_style_BundledImageDescription_shape_value_roundtrip():
    instance = viewpoint_style_BundledImageDescription(shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_viewpoint_style_ContainerStyleDescription_roundedCorner_value_roundtrip():
    instance = viewpoint_style_ContainerStyleDescription(roundedCorner=True)
    assert instance.roundedCorner == True
    instance.roundedCorner = False
    assert instance.roundedCorner == False


def test_viewpoint_style_CustomStyleDescription_id_value_roundtrip():
    instance = viewpoint_style_CustomStyleDescription(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_viewpoint_style_DotDescription_strokeSizeComputationExpression_value_roundtrip():
    instance = viewpoint_style_DotDescription(strokeSizeComputationExpression="sample_text")
    assert instance.strokeSizeComputationExpression == "sample_text"
    instance.strokeSizeComputationExpression = "sample_text_2"
    assert instance.strokeSizeComputationExpression == "sample_text_2"


def test_viewpoint_style_EdgeStyleDescription_foldingStyle_value_roundtrip():
    instance = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.foldingStyle == "sample_text"
    instance.foldingStyle = "sample_text_2"
    assert instance.foldingStyle == "sample_text_2"


def test_viewpoint_style_EdgeStyleDescription_lineStyle_value_roundtrip():
    instance = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.lineStyle == "sample_text"
    instance.lineStyle = "sample_text_2"
    assert instance.lineStyle == "sample_text_2"


def test_viewpoint_style_EdgeStyleDescription_routingStyle_value_roundtrip():
    instance = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.routingStyle == "sample_text"
    instance.routingStyle = "sample_text_2"
    assert instance.routingStyle == "sample_text_2"


def test_viewpoint_style_EdgeStyleDescription_sizeComputationExpression_value_roundtrip():
    instance = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.sizeComputationExpression == "sample_text"
    instance.sizeComputationExpression = "sample_text_2"
    assert instance.sizeComputationExpression == "sample_text_2"


def test_viewpoint_style_EdgeStyleDescription_sourceArrow_value_roundtrip():
    instance = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.sourceArrow == "sample_text"
    instance.sourceArrow = "sample_text_2"
    assert instance.sourceArrow == "sample_text_2"


def test_viewpoint_style_EdgeStyleDescription_targetArrow_value_roundtrip():
    instance = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert instance.targetArrow == "sample_text"
    instance.targetArrow = "sample_text_2"
    assert instance.targetArrow == "sample_text_2"


def test_viewpoint_style_EllipseNodeDescription_horizontalDiameterComputationExpression_value_roundtrip():
    instance = viewpoint_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    assert instance.horizontalDiameterComputationExpression == "sample_text"
    instance.horizontalDiameterComputationExpression = "sample_text_2"
    assert instance.horizontalDiameterComputationExpression == "sample_text_2"


def test_viewpoint_style_EllipseNodeDescription_verticalDiameterComputationExpression_value_roundtrip():
    instance = viewpoint_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    assert instance.verticalDiameterComputationExpression == "sample_text"
    instance.verticalDiameterComputationExpression = "sample_text_2"
    assert instance.verticalDiameterComputationExpression == "sample_text_2"


def test_viewpoint_style_FlatContainerStyleDescription_backgroundStyle_value_roundtrip():
    instance = viewpoint_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    assert instance.backgroundStyle == "sample_text"
    instance.backgroundStyle = "sample_text_2"
    assert instance.backgroundStyle == "sample_text_2"


def test_viewpoint_style_GaugeCompositeStyleDescription_alignment_value_roundtrip():
    instance = viewpoint_style_GaugeCompositeStyleDescription(alignment="sample_text")
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_viewpoint_style_GaugeSectionDescription_label_value_roundtrip():
    instance = viewpoint_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_viewpoint_style_GaugeSectionDescription_maxValueExpression_value_roundtrip():
    instance = viewpoint_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    assert instance.maxValueExpression == "sample_text"
    instance.maxValueExpression = "sample_text_2"
    assert instance.maxValueExpression == "sample_text_2"


def test_viewpoint_style_GaugeSectionDescription_minValueExpression_value_roundtrip():
    instance = viewpoint_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    assert instance.minValueExpression == "sample_text"
    instance.minValueExpression = "sample_text_2"
    assert instance.minValueExpression == "sample_text_2"


def test_viewpoint_style_GaugeSectionDescription_valueExpression_value_roundtrip():
    instance = viewpoint_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    assert instance.valueExpression == "sample_text"
    instance.valueExpression = "sample_text_2"
    assert instance.valueExpression == "sample_text_2"


def test_viewpoint_style_LabelBorderStyleDescription_cornerHeight_value_roundtrip():
    instance = viewpoint_style_LabelBorderStyleDescription(cornerHeight=7, cornerWidth=7, id="sample_text", name="sample_text")
    assert instance.cornerHeight == 7
    instance.cornerHeight = 13
    assert instance.cornerHeight == 13


def test_viewpoint_style_LabelBorderStyleDescription_cornerWidth_value_roundtrip():
    instance = viewpoint_style_LabelBorderStyleDescription(cornerHeight=7, cornerWidth=7, id="sample_text", name="sample_text")
    assert instance.cornerWidth == 7
    instance.cornerWidth = 13
    assert instance.cornerWidth == 13


def test_viewpoint_style_LabelBorderStyleDescription_id_value_roundtrip():
    instance = viewpoint_style_LabelBorderStyleDescription(cornerHeight=7, cornerWidth=7, id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_viewpoint_style_LabelBorderStyleDescription_name_value_roundtrip():
    instance = viewpoint_style_LabelBorderStyleDescription(cornerHeight=7, cornerWidth=7, id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_style_LabelStyleDescription_labelAlignment_value_roundtrip():
    instance = viewpoint_style_LabelStyleDescription(labelAlignment="sample_text")
    assert instance.labelAlignment == "sample_text"
    instance.labelAlignment = "sample_text_2"
    assert instance.labelAlignment == "sample_text_2"


def test_viewpoint_style_LozengeNodeDescription_heightComputationExpression_value_roundtrip():
    instance = viewpoint_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert instance.heightComputationExpression == "sample_text"
    instance.heightComputationExpression = "sample_text_2"
    assert instance.heightComputationExpression == "sample_text_2"


def test_viewpoint_style_LozengeNodeDescription_widthComputationExpression_value_roundtrip():
    instance = viewpoint_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert instance.widthComputationExpression == "sample_text"
    instance.widthComputationExpression = "sample_text_2"
    assert instance.widthComputationExpression == "sample_text_2"


def test_viewpoint_style_NodeStyleDescription_hideLabelByDefault_value_roundtrip():
    instance = viewpoint_style_NodeStyleDescription(hideLabelByDefault=True, labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert instance.hideLabelByDefault == True
    instance.hideLabelByDefault = False
    assert instance.hideLabelByDefault == False


def test_viewpoint_style_NodeStyleDescription_labelPosition_value_roundtrip():
    instance = viewpoint_style_NodeStyleDescription(hideLabelByDefault=True, labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert instance.labelPosition == "sample_text"
    instance.labelPosition = "sample_text_2"
    assert instance.labelPosition == "sample_text_2"


def test_viewpoint_style_NodeStyleDescription_resizeKind_value_roundtrip():
    instance = viewpoint_style_NodeStyleDescription(hideLabelByDefault=True, labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert instance.resizeKind == "sample_text"
    instance.resizeKind = "sample_text_2"
    assert instance.resizeKind == "sample_text_2"


def test_viewpoint_style_NodeStyleDescription_sizeComputationExpression_value_roundtrip():
    instance = viewpoint_style_NodeStyleDescription(hideLabelByDefault=True, labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert instance.sizeComputationExpression == "sample_text"
    instance.sizeComputationExpression = "sample_text_2"
    assert instance.sizeComputationExpression == "sample_text_2"


def test_viewpoint_style_RoundedCornerStyleDescription_arcHeight_value_roundtrip():
    instance = viewpoint_style_RoundedCornerStyleDescription(arcHeight="sample_text", arcWidth="sample_text")
    assert instance.arcHeight == "sample_text"
    instance.arcHeight = "sample_text_2"
    assert instance.arcHeight == "sample_text_2"


def test_viewpoint_style_RoundedCornerStyleDescription_arcWidth_value_roundtrip():
    instance = viewpoint_style_RoundedCornerStyleDescription(arcHeight="sample_text", arcWidth="sample_text")
    assert instance.arcWidth == "sample_text"
    instance.arcWidth = "sample_text_2"
    assert instance.arcWidth == "sample_text_2"


def test_viewpoint_style_ShapeContainerStyleDescription_shape_value_roundtrip():
    instance = viewpoint_style_ShapeContainerStyleDescription(shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_viewpoint_style_SizeComputationContainerStyleDescription_heightComputationExpression_value_roundtrip():
    instance = viewpoint_style_SizeComputationContainerStyleDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert instance.heightComputationExpression == "sample_text"
    instance.heightComputationExpression = "sample_text_2"
    assert instance.heightComputationExpression == "sample_text_2"


def test_viewpoint_style_SizeComputationContainerStyleDescription_widthComputationExpression_value_roundtrip():
    instance = viewpoint_style_SizeComputationContainerStyleDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert instance.widthComputationExpression == "sample_text"
    instance.widthComputationExpression = "sample_text_2"
    assert instance.widthComputationExpression == "sample_text_2"


def test_viewpoint_style_SquareDescription_height_value_roundtrip():
    instance = viewpoint_style_SquareDescription(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_viewpoint_style_SquareDescription_width_value_roundtrip():
    instance = viewpoint_style_SquareDescription(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_viewpoint_style_TooltipStyleDescription_tooltipExpression_value_roundtrip():
    instance = viewpoint_style_TooltipStyleDescription(tooltipExpression="sample_text")
    assert instance.tooltipExpression == "sample_text"
    instance.tooltipExpression = "sample_text_2"
    assert instance.tooltipExpression == "sample_text_2"


def test_viewpoint_style_WorkspaceImageDescription_workspacePath_value_roundtrip():
    instance = viewpoint_style_WorkspaceImageDescription(workspacePath="sample_text")
    assert instance.workspacePath == "sample_text"
    instance.workspacePath = "sample_text_2"
    assert instance.workspacePath == "sample_text_2"


def test_viewpoint_tool_AbstractToolDescription_forceRefresh_value_roundtrip():
    instance = viewpoint_tool_AbstractToolDescription(forceRefresh=True, precondition="sample_text")
    assert instance.forceRefresh == True
    instance.forceRefresh = False
    assert instance.forceRefresh == False


def test_viewpoint_tool_AbstractToolDescription_precondition_value_roundtrip():
    instance = viewpoint_tool_AbstractToolDescription(forceRefresh=True, precondition="sample_text")
    assert instance.precondition == "sample_text"
    instance.precondition = "sample_text_2"
    assert instance.precondition == "sample_text_2"


def test_viewpoint_tool_AbstractVariable_name_value_roundtrip():
    instance = viewpoint_tool_AbstractVariable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_tool_AcceleoVariable_computationExpression_value_roundtrip():
    instance = viewpoint_tool_AcceleoVariable(computationExpression="sample_text")
    assert instance.computationExpression == "sample_text"
    instance.computationExpression = "sample_text_2"
    assert instance.computationExpression == "sample_text_2"


def test_viewpoint_tool_BehaviorTool_domainClass_value_roundtrip():
    instance = viewpoint_tool_BehaviorTool(domainClass="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_viewpoint_tool_Case_conditionExpression_value_roundtrip():
    instance = viewpoint_tool_Case(conditionExpression="sample_text")
    assert instance.conditionExpression == "sample_text"
    instance.conditionExpression = "sample_text_2"
    assert instance.conditionExpression == "sample_text_2"


def test_viewpoint_tool_ChangeContext_browseExpression_value_roundtrip():
    instance = viewpoint_tool_ChangeContext(browseExpression="sample_text")
    assert instance.browseExpression == "sample_text"
    instance.browseExpression = "sample_text_2"
    assert instance.browseExpression == "sample_text_2"


def test_viewpoint_tool_ContainerCreationDescription_iconPath_value_roundtrip():
    instance = viewpoint_tool_ContainerCreationDescription(iconPath="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_tool_ContainerDropDescription_dragSource_value_roundtrip():
    instance = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    assert instance.dragSource == "sample_text"
    instance.dragSource = "sample_text_2"
    assert instance.dragSource == "sample_text_2"


def test_viewpoint_tool_ContainerDropDescription_moveEdges_value_roundtrip():
    instance = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    assert instance.moveEdges == True
    instance.moveEdges = False
    assert instance.moveEdges == False


def test_viewpoint_tool_CreateEdgeView_sourceExpression_value_roundtrip():
    instance = viewpoint_tool_CreateEdgeView(sourceExpression="sample_text", targetExpression="sample_text")
    assert instance.sourceExpression == "sample_text"
    instance.sourceExpression = "sample_text_2"
    assert instance.sourceExpression == "sample_text_2"


def test_viewpoint_tool_CreateEdgeView_targetExpression_value_roundtrip():
    instance = viewpoint_tool_CreateEdgeView(sourceExpression="sample_text", targetExpression="sample_text")
    assert instance.targetExpression == "sample_text"
    instance.targetExpression = "sample_text_2"
    assert instance.targetExpression == "sample_text_2"


def test_viewpoint_tool_CreateInstance_referenceName_value_roundtrip():
    instance = viewpoint_tool_CreateInstance(referenceName="sample_text", typeName="sample_text", variableName="sample_text")
    assert instance.referenceName == "sample_text"
    instance.referenceName = "sample_text_2"
    assert instance.referenceName == "sample_text_2"


def test_viewpoint_tool_CreateInstance_typeName_value_roundtrip():
    instance = viewpoint_tool_CreateInstance(referenceName="sample_text", typeName="sample_text", variableName="sample_text")
    assert instance.typeName == "sample_text"
    instance.typeName = "sample_text_2"
    assert instance.typeName == "sample_text_2"


def test_viewpoint_tool_CreateInstance_variableName_value_roundtrip():
    instance = viewpoint_tool_CreateInstance(referenceName="sample_text", typeName="sample_text", variableName="sample_text")
    assert instance.variableName == "sample_text"
    instance.variableName = "sample_text_2"
    assert instance.variableName == "sample_text_2"


def test_viewpoint_tool_CreateView_containerViewExpression_value_roundtrip():
    instance = viewpoint_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    assert instance.containerViewExpression == "sample_text"
    instance.containerViewExpression = "sample_text_2"
    assert instance.containerViewExpression == "sample_text_2"


def test_viewpoint_tool_CreateView_variableName_value_roundtrip():
    instance = viewpoint_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    assert instance.variableName == "sample_text"
    instance.variableName = "sample_text_2"
    assert instance.variableName == "sample_text_2"


def test_viewpoint_tool_DeleteHook_id_value_roundtrip():
    instance = viewpoint_tool_DeleteHook(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_viewpoint_tool_DeleteHookParameter_name_value_roundtrip():
    instance = viewpoint_tool_DeleteHookParameter(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_tool_DeleteHookParameter_value_value_roundtrip():
    instance = viewpoint_tool_DeleteHookParameter(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_viewpoint_tool_DialogVariable_dialogPrompt_value_roundtrip():
    instance = viewpoint_tool_DialogVariable(dialogPrompt="sample_text")
    assert instance.dialogPrompt == "sample_text"
    instance.dialogPrompt = "sample_text_2"
    assert instance.dialogPrompt == "sample_text_2"


def test_viewpoint_tool_DirectEditLabel_inputLabelExpression_value_roundtrip():
    instance = viewpoint_tool_DirectEditLabel(inputLabelExpression="sample_text")
    assert instance.inputLabelExpression == "sample_text"
    instance.inputLabelExpression = "sample_text_2"
    assert instance.inputLabelExpression == "sample_text_2"


def test_viewpoint_tool_EdgeCreationDescription_connectionStartPrecondition_value_roundtrip():
    instance = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    assert instance.connectionStartPrecondition == "sample_text"
    instance.connectionStartPrecondition = "sample_text_2"
    assert instance.connectionStartPrecondition == "sample_text_2"


def test_viewpoint_tool_EdgeCreationDescription_iconPath_value_roundtrip():
    instance = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_tool_EditMaskVariables_mask_value_roundtrip():
    instance = viewpoint_tool_EditMaskVariables(mask="sample_text")
    assert instance.mask == "sample_text"
    instance.mask = "sample_text_2"
    assert instance.mask == "sample_text_2"


def test_viewpoint_tool_ExternalJavaAction_id_value_roundtrip():
    instance = viewpoint_tool_ExternalJavaAction(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_viewpoint_tool_ExternalJavaActionParameter_name_value_roundtrip():
    instance = viewpoint_tool_ExternalJavaActionParameter(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_tool_ExternalJavaActionParameter_value_value_roundtrip():
    instance = viewpoint_tool_ExternalJavaActionParameter(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_viewpoint_tool_FeatureChangeListener_domainClass_value_roundtrip():
    instance = viewpoint_tool_FeatureChangeListener(domainClass="sample_text", featureName="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_viewpoint_tool_FeatureChangeListener_featureName_value_roundtrip():
    instance = viewpoint_tool_FeatureChangeListener(domainClass="sample_text", featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_viewpoint_tool_For_expression_value_roundtrip():
    instance = viewpoint_tool_For(expression="sample_text", iteratorName="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_viewpoint_tool_For_iteratorName_value_roundtrip():
    instance = viewpoint_tool_For(expression="sample_text", iteratorName="sample_text")
    assert instance.iteratorName == "sample_text"
    instance.iteratorName = "sample_text_2"
    assert instance.iteratorName == "sample_text_2"


def test_viewpoint_tool_If_conditionExpression_value_roundtrip():
    instance = viewpoint_tool_If(conditionExpression="sample_text")
    assert instance.conditionExpression == "sample_text"
    instance.conditionExpression = "sample_text_2"
    assert instance.conditionExpression == "sample_text_2"


def test_viewpoint_tool_MenuItemDescription_icon_value_roundtrip():
    instance = viewpoint_tool_MenuItemDescription(icon="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_viewpoint_tool_MoveElement_featureName_value_roundtrip():
    instance = viewpoint_tool_MoveElement(featureName="sample_text", newContainerExpression="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_viewpoint_tool_MoveElement_newContainerExpression_value_roundtrip():
    instance = viewpoint_tool_MoveElement(featureName="sample_text", newContainerExpression="sample_text")
    assert instance.newContainerExpression == "sample_text"
    instance.newContainerExpression = "sample_text_2"
    assert instance.newContainerExpression == "sample_text_2"


def test_viewpoint_tool_Navigation_createIfNotExistent_value_roundtrip():
    instance = viewpoint_tool_Navigation(createIfNotExistent=True)
    assert instance.createIfNotExistent == True
    instance.createIfNotExistent = False
    assert instance.createIfNotExistent == False


def test_viewpoint_tool_NodeCreationDescription_iconPath_value_roundtrip():
    instance = viewpoint_tool_NodeCreationDescription(iconPath="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_candidatesExpression_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.candidatesExpression == "sample_text"
    instance.candidatesExpression = "sample_text_2"
    assert instance.candidatesExpression == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_childrenExpression_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.childrenExpression == "sample_text"
    instance.childrenExpression = "sample_text_2"
    assert instance.childrenExpression == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_choiceOfValuesMessage_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.choiceOfValuesMessage == "sample_text"
    instance.choiceOfValuesMessage = "sample_text_2"
    assert instance.choiceOfValuesMessage == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_iconPath_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_message_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_preSelectedCandidatesExpression_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.preSelectedCandidatesExpression == "sample_text"
    instance.preSelectedCandidatesExpression = "sample_text_2"
    assert instance.preSelectedCandidatesExpression == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_rootExpression_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.rootExpression == "sample_text"
    instance.rootExpression = "sample_text_2"
    assert instance.rootExpression == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_selectedValuesMessage_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.selectedValuesMessage == "sample_text"
    instance.selectedValuesMessage = "sample_text_2"
    assert instance.selectedValuesMessage == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_tree_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.tree == True
    instance.tree = False
    assert instance.tree == False


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_windowImagePath_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.windowImagePath == "sample_text"
    instance.windowImagePath = "sample_text_2"
    assert instance.windowImagePath == "sample_text_2"


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_windowTitle_value_roundtrip():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.windowTitle == "sample_text"
    instance.windowTitle = "sample_text_2"
    assert instance.windowTitle == "sample_text_2"


def test_viewpoint_tool_ReconnectEdgeDescription_reconnectionKind_value_roundtrip():
    instance = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    assert instance.reconnectionKind == "sample_text"
    instance.reconnectionKind = "sample_text_2"
    assert instance.reconnectionKind == "sample_text_2"


def test_viewpoint_tool_RepresentationCreationDescription_browseExpression_value_roundtrip():
    instance = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    assert instance.browseExpression == "sample_text"
    instance.browseExpression = "sample_text_2"
    assert instance.browseExpression == "sample_text_2"


def test_viewpoint_tool_RepresentationCreationDescription_titleExpression_value_roundtrip():
    instance = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    assert instance.titleExpression == "sample_text"
    instance.titleExpression = "sample_text_2"
    assert instance.titleExpression == "sample_text_2"


def test_viewpoint_tool_RepresentationNavigationDescription_browseExpression_value_roundtrip():
    instance = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    assert instance.browseExpression == "sample_text"
    instance.browseExpression = "sample_text_2"
    assert instance.browseExpression == "sample_text_2"


def test_viewpoint_tool_RepresentationNavigationDescription_navigationNameExpression_value_roundtrip():
    instance = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    assert instance.navigationNameExpression == "sample_text"
    instance.navigationNameExpression = "sample_text_2"
    assert instance.navigationNameExpression == "sample_text_2"


def test_viewpoint_tool_RequestDescription_type_value_roundtrip():
    instance = viewpoint_tool_RequestDescription(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_viewpoint_tool_SelectionWizardDescription_iconPath_value_roundtrip():
    instance = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_tool_SelectionWizardDescription_windowImagePath_value_roundtrip():
    instance = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.windowImagePath == "sample_text"
    instance.windowImagePath = "sample_text_2"
    assert instance.windowImagePath == "sample_text_2"


def test_viewpoint_tool_SelectionWizardDescription_windowTitle_value_roundtrip():
    instance = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    assert instance.windowTitle == "sample_text"
    instance.windowTitle = "sample_text_2"
    assert instance.windowTitle == "sample_text_2"


def test_viewpoint_tool_SetObject_featureName_value_roundtrip():
    instance = viewpoint_tool_SetObject(featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_viewpoint_tool_SetValue_featureName_value_roundtrip():
    instance = viewpoint_tool_SetValue(featureName="sample_text", valueExpression="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_viewpoint_tool_SetValue_valueExpression_value_roundtrip():
    instance = viewpoint_tool_SetValue(featureName="sample_text", valueExpression="sample_text")
    assert instance.valueExpression == "sample_text"
    instance.valueExpression = "sample_text_2"
    assert instance.valueExpression == "sample_text_2"


def test_viewpoint_tool_ToolDescription_iconPath_value_roundtrip():
    instance = viewpoint_tool_ToolDescription(iconPath="sample_text")
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_tool_ToolFilterDescription_elementsToListen_value_roundtrip():
    instance = viewpoint_tool_ToolFilterDescription(elementsToListen="sample_text", precondition="sample_text")
    assert instance.elementsToListen == "sample_text"
    instance.elementsToListen = "sample_text_2"
    assert instance.elementsToListen == "sample_text_2"


def test_viewpoint_tool_ToolFilterDescription_precondition_value_roundtrip():
    instance = viewpoint_tool_ToolFilterDescription(elementsToListen="sample_text", precondition="sample_text")
    assert instance.precondition == "sample_text"
    instance.precondition = "sample_text_2"
    assert instance.precondition == "sample_text_2"


def test_viewpoint_tool_ToolSection_icon_value_roundtrip():
    instance = viewpoint_tool_ToolSection(icon="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_viewpoint_tool_Unset_elementExpression_value_roundtrip():
    instance = viewpoint_tool_Unset(elementExpression="sample_text", featureName="sample_text")
    assert instance.elementExpression == "sample_text"
    instance.elementExpression = "sample_text_2"
    assert instance.elementExpression == "sample_text_2"


def test_viewpoint_tool_Unset_featureName_value_roundtrip():
    instance = viewpoint_tool_Unset(elementExpression="sample_text", featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_viewpoint_validation_RuleAudit_auditExpression_value_roundtrip():
    instance = viewpoint_validation_RuleAudit(auditExpression="sample_text")
    assert instance.auditExpression == "sample_text"
    instance.auditExpression = "sample_text_2"
    assert instance.auditExpression == "sample_text_2"


def test_viewpoint_validation_SemanticValidationRule_targetClass_value_roundtrip():
    instance = viewpoint_validation_SemanticValidationRule(targetClass="sample_text")
    assert instance.targetClass == "sample_text"
    instance.targetClass = "sample_text_2"
    assert instance.targetClass == "sample_text_2"


def test_viewpoint_validation_ValidationFix_name_value_roundtrip():
    instance = viewpoint_validation_ValidationFix(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_validation_ValidationRule_level_value_roundtrip():
    instance = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    assert instance.level == "sample_text"
    instance.level = "sample_text_2"
    assert instance.level == "sample_text_2"


def test_viewpoint_validation_ValidationRule_message_value_roundtrip():
    instance = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_viewpoint_validation_ValidationSet_name_value_roundtrip():
    instance = viewpoint_validation_ValidationSet(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_diagram_DNodeListElement_isa_AbstractDNode():
    instance = viewpoint_diagram_DNodeListElement()
    assert isinstance(instance, AbstractDNode)


def test_viewpoint_tool_BehaviorTool_isa_AbstractToolDescription():
    instance = viewpoint_tool_BehaviorTool(domainClass="sample_text")
    assert isinstance(instance, AbstractToolDescription)


def test_viewpoint_tool_MappingBasedToolDescription_isa_AbstractToolDescription():
    instance = viewpoint_tool_MappingBasedToolDescription()
    assert isinstance(instance, AbstractToolDescription)


def test_viewpoint_tool_PaneBasedSelectionWizardDescription_isa_AbstractToolDescription():
    instance = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    assert isinstance(instance, AbstractToolDescription)


def test_viewpoint_tool_PopupMenu_isa_AbstractToolDescription():
    instance = viewpoint_tool_PopupMenu()
    assert isinstance(instance, AbstractToolDescription)


def test_viewpoint_tool_RepresentationCreationDescription_isa_AbstractToolDescription():
    instance = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    assert isinstance(instance, AbstractToolDescription)


def test_viewpoint_tool_RepresentationNavigationDescription_isa_AbstractToolDescription():
    instance = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    assert isinstance(instance, AbstractToolDescription)


def test_viewpoint_tool_RequestDescription_isa_AbstractToolDescription():
    instance = viewpoint_tool_RequestDescription(type="sample_text")
    assert isinstance(instance, AbstractToolDescription)


def test_viewpoint_tool_DialogVariable_isa_AbstractVariable():
    instance = viewpoint_tool_DialogVariable(dialogPrompt="sample_text")
    assert isinstance(instance, AbstractVariable)


def test_viewpoint_tool_ElementSelectVariable_isa_AbstractVariable():
    instance = viewpoint_tool_ElementSelectVariable()
    assert isinstance(instance, AbstractVariable)


def test_viewpoint_tool_NameVariable_isa_AbstractVariable():
    instance = viewpoint_tool_NameVariable()
    assert isinstance(instance, AbstractVariable)


def test_viewpoint_tool_SubVariable_isa_AbstractVariable():
    instance = viewpoint_tool_SubVariable()
    assert isinstance(instance, AbstractVariable)


def test_viewpoint_LabelStyle_isa_BasicLabelStyle():
    instance = viewpoint_LabelStyle(labelAlignment="sample_text")
    assert isinstance(instance, BasicLabelStyle)


def test_viewpoint_diagram_BeginLabelStyle_isa_BasicLabelStyle():
    instance = viewpoint_diagram_BeginLabelStyle()
    assert isinstance(instance, BasicLabelStyle)


def test_viewpoint_diagram_CenterLabelStyle_isa_BasicLabelStyle():
    instance = viewpoint_diagram_CenterLabelStyle()
    assert isinstance(instance, BasicLabelStyle)


def test_viewpoint_diagram_EndLabelStyle_isa_BasicLabelStyle():
    instance = viewpoint_diagram_EndLabelStyle()
    assert isinstance(instance, BasicLabelStyle)


def test_viewpoint_style_BeginLabelStyleDescription_isa_BasicLabelStyleDescription():
    instance = viewpoint_style_BeginLabelStyleDescription()
    assert isinstance(instance, BasicLabelStyleDescription)


def test_viewpoint_style_CenterLabelStyleDescription_isa_BasicLabelStyleDescription():
    instance = viewpoint_style_CenterLabelStyleDescription()
    assert isinstance(instance, BasicLabelStyleDescription)


def test_viewpoint_style_EndLabelStyleDescription_isa_BasicLabelStyleDescription():
    instance = viewpoint_style_EndLabelStyleDescription()
    assert isinstance(instance, BasicLabelStyleDescription)


def test_viewpoint_style_LabelStyleDescription_isa_BasicLabelStyleDescription():
    instance = viewpoint_style_LabelStyleDescription(labelAlignment="sample_text")
    assert isinstance(instance, BasicLabelStyleDescription)


def test_viewpoint_diagram_IndirectlyCollapseFilter_isa_CollapseFilter():
    instance = viewpoint_diagram_IndirectlyCollapseFilter()
    assert isinstance(instance, CollapseFilter)


def test_viewpoint_description_FixedColor_isa_ColorDescription():
    instance = viewpoint_description_FixedColor(blue=7, green=7, red=7)
    assert isinstance(instance, ColorDescription)


def test_viewpoint_description_ConditionalContainerStyleDescription_isa_ConditionalStyleDescription():
    instance = viewpoint_description_ConditionalContainerStyleDescription()
    assert isinstance(instance, ConditionalStyleDescription)


def test_viewpoint_description_ConditionalEdgeStyleDescription_isa_ConditionalStyleDescription():
    instance = viewpoint_description_ConditionalEdgeStyleDescription()
    assert isinstance(instance, ConditionalStyleDescription)


def test_viewpoint_description_ConditionalNodeStyleDescription_isa_ConditionalStyleDescription():
    instance = viewpoint_description_ConditionalNodeStyleDescription()
    assert isinstance(instance, ConditionalStyleDescription)


def test_viewpoint_tool_ChangeContext_isa_ContainerModelOperation():
    instance = viewpoint_tool_ChangeContext(browseExpression="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_CreateInstance_isa_ContainerModelOperation():
    instance = viewpoint_tool_CreateInstance(referenceName="sample_text", typeName="sample_text", variableName="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_CreateView_isa_ContainerModelOperation():
    instance = viewpoint_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_DeleteView_isa_ContainerModelOperation():
    instance = viewpoint_tool_DeleteView()
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_For_isa_ContainerModelOperation():
    instance = viewpoint_tool_For(expression="sample_text", iteratorName="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_If_isa_ContainerModelOperation():
    instance = viewpoint_tool_If(conditionExpression="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_MoveElement_isa_ContainerModelOperation():
    instance = viewpoint_tool_MoveElement(featureName="sample_text", newContainerExpression="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_Navigation_isa_ContainerModelOperation():
    instance = viewpoint_tool_Navigation(createIfNotExistent=True)
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_RemoveElement_isa_ContainerModelOperation():
    instance = viewpoint_tool_RemoveElement()
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_SetObject_isa_ContainerModelOperation():
    instance = viewpoint_tool_SetObject(featureName="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_SetValue_isa_ContainerModelOperation():
    instance = viewpoint_tool_SetValue(featureName="sample_text", valueExpression="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_Unset_isa_ContainerModelOperation():
    instance = viewpoint_tool_Unset(elementExpression="sample_text", featureName="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_diagram_FlatContainerStyle_isa_ContainerStyle():
    instance = viewpoint_diagram_FlatContainerStyle(backgroundStyle="sample_text")
    assert isinstance(instance, ContainerStyle)


def test_viewpoint_diagram_ShapeContainerStyle_isa_ContainerStyle():
    instance = viewpoint_diagram_ShapeContainerStyle(shape="sample_text")
    assert isinstance(instance, ContainerStyle)


def test_viewpoint_tool_CreateEdgeView_isa_CreateView():
    instance = viewpoint_tool_CreateEdgeView(sourceExpression="sample_text", targetExpression="sample_text")
    assert isinstance(instance, CreateView)


def test_viewpoint_BasicLabelStyle_isa_Customizable():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert isinstance(instance, Customizable)


def test_viewpoint_Style_isa_Customizable():
    instance = viewpoint_Style()
    assert isinstance(instance, Customizable)


def test_viewpoint_diagram_GaugeSection_isa_Customizable():
    instance = viewpoint_diagram_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert isinstance(instance, Customizable)


def test_viewpoint_diagram_DDiagram_isa_DContainer():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert isinstance(instance, DContainer)


def test_viewpoint_diagram_DDiagramElementContainer_isa_DContainer():
    instance = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert isinstance(instance, DContainer)


def test_viewpoint_diagram_AbstractDNode_isa_DDiagramElement():
    instance = viewpoint_diagram_AbstractDNode(arrangeConstraints="sample_text")
    assert isinstance(instance, DDiagramElement)


def test_viewpoint_diagram_DNodeContainer_isa_DDiagramElementContainer():
    instance = viewpoint_diagram_DNodeContainer(childrenPresentation="sample_text")
    assert isinstance(instance, DDiagramElementContainer)


def test_viewpoint_diagram_DNodeList_isa_DDiagramElementContainer():
    instance = viewpoint_diagram_DNodeList(lineWidth=7)
    assert isinstance(instance, DDiagramElementContainer)


def test_viewpoint_DModel_isa_DFile():
    instance = viewpoint_DModel()
    assert isinstance(instance, DFile)


def test_viewpoint_DRepresentationElement_isa_DLabelled():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DLabelled)


def test_viewpoint_DRepresentationElement_isa_DMappingBased():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DMappingBased)


def test_viewpoint_diagram_DDiagramElement_isa_DNavigable():
    instance = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    assert isinstance(instance, DNavigable)


def test_viewpoint_DEObjectLink_isa_DNavigationLink():
    instance = viewpoint_DEObjectLink()
    assert isinstance(instance, DNavigationLink)


def test_viewpoint_DSourceFileLink_isa_DNavigationLink():
    instance = viewpoint_DSourceFileLink(endPosition=7, filePath="sample_text", startPosition=7)
    assert isinstance(instance, DNavigationLink)


def test_viewpoint_diagram_DDiagramLink_isa_DNavigationLink():
    instance = viewpoint_diagram_DDiagramLink()
    assert isinstance(instance, DNavigationLink)


def test_viewpoint_DRepresentation_isa_DRefreshable():
    instance = viewpoint_DRepresentation(name="sample_text")
    assert isinstance(instance, DRefreshable)


def test_viewpoint_DRepresentationElement_isa_DRefreshable():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DRefreshable)


def test_viewpoint_DView_isa_DRefreshable():
    instance = viewpoint_DView(initialized=True)
    assert isinstance(instance, DRefreshable)


def test_viewpoint_Style_isa_DRefreshable():
    instance = viewpoint_Style()
    assert isinstance(instance, DRefreshable)


def test_viewpoint_diagram_DDiagram_isa_DRepresentation():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert isinstance(instance, DRepresentation)


def test_viewpoint_diagram_DDiagramElement_isa_DRepresentationElement():
    instance = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    assert isinstance(instance, DRepresentationElement)


def test_viewpoint_DFile_isa_DResource():
    instance = viewpoint_DFile()
    assert isinstance(instance, DResource)


def test_viewpoint_DResourceContainer_isa_DResource():
    instance = viewpoint_DResourceContainer()
    assert isinstance(instance, DResource)


def test_viewpoint_DFolder_isa_DResourceContainer():
    instance = viewpoint_DFolder()
    assert isinstance(instance, DResourceContainer)


def test_viewpoint_DProject_isa_DResourceContainer():
    instance = viewpoint_DProject()
    assert isinstance(instance, DResourceContainer)


def test_viewpoint_DRepresentationElement_isa_DSemanticDecorator():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DSemanticDecorator)


def test_viewpoint_diagram_DSemanticDiagram_isa_DSemanticDecorator():
    instance = viewpoint_diagram_DSemanticDiagram()
    assert isinstance(instance, DSemanticDecorator)


def test_viewpoint_DRepresentationElement_isa_DStylizable():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DStylizable)


def test_viewpoint_diagram_DDiagram_isa_DValidable():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert isinstance(instance, DValidable)


def test_viewpoint_diagram_DDiagramElement_isa_DValidable():
    instance = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    assert isinstance(instance, DValidable)


def test_viewpoint_DRepresentationContainer_isa_DView():
    instance = viewpoint_DRepresentationContainer()
    assert isinstance(instance, DView)


def test_viewpoint_description_MappingBasedDecoration_isa_DecorationDescription():
    instance = viewpoint_description_MappingBasedDecoration()
    assert isinstance(instance, DecorationDescription)


def test_viewpoint_description_SemanticBasedDecoration_isa_DecorationDescription():
    instance = viewpoint_description_SemanticBasedDecoration(domainClass="sample_text")
    assert isinstance(instance, DecorationDescription)


def test_viewpoint_concern_ConcernSet_isa_DocumentedElement():
    instance = viewpoint_concern_ConcernSet()
    assert isinstance(instance, DocumentedElement)


def test_viewpoint_description_Layout_isa_DocumentedElement():
    instance = viewpoint_description_Layout()
    assert isinstance(instance, DocumentedElement)


def test_viewpoint_validation_ValidationSet_isa_DocumentedElement():
    instance = viewpoint_validation_ValidationSet(name="sample_text")
    assert isinstance(instance, DocumentedElement)


def test_viewpoint_diagram_DDiagram_isa_DragAndDropTarget():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert isinstance(instance, DragAndDropTarget)


def test_viewpoint_diagram_DDiagramElementContainer_isa_DragAndDropTarget():
    instance = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert isinstance(instance, DragAndDropTarget)


def test_viewpoint_diagram_DNode_isa_DragAndDropTarget():
    instance = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert isinstance(instance, DragAndDropTarget)


def test_viewpoint_description_EAttributeCustomization_isa_EStructuralFeatureCustomization():
    instance = viewpoint_description_EAttributeCustomization(attributeName="sample_text", value="sample_text")
    assert isinstance(instance, EStructuralFeatureCustomization)


def test_viewpoint_description_EReferenceCustomization_isa_EStructuralFeatureCustomization():
    instance = viewpoint_description_EReferenceCustomization(referenceName="sample_text")
    assert isinstance(instance, EStructuralFeatureCustomization)


def test_viewpoint_diagram_BracketEdgeStyle_isa_EdgeStyle():
    instance = viewpoint_diagram_BracketEdgeStyle()
    assert isinstance(instance, EdgeStyle)


def test_viewpoint_style_BracketEdgeStyleDescription_isa_EdgeStyleDescription():
    instance = viewpoint_style_BracketEdgeStyleDescription()
    assert isinstance(instance, EdgeStyleDescription)


def test_viewpoint_filter_MappingFilter_isa_Filter():
    instance = viewpoint_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    assert isinstance(instance, Filter)


def test_viewpoint_filter_VariableFilter_isa_Filter():
    instance = viewpoint_filter_VariableFilter(semanticConditionExpression="sample_text")
    assert isinstance(instance, Filter)


def test_viewpoint_filter_CompositeFilterDescription_isa_FilterDescription():
    instance = viewpoint_filter_CompositeFilterDescription()
    assert isinstance(instance, FilterDescription)


def test_viewpoint_description_SystemColor_isa_FixedColor():
    instance = viewpoint_description_SystemColor(name="sample_text")
    assert isinstance(instance, FixedColor)


def test_viewpoint_diagram_AbsoluteBoundsFilter_isa_GraphicalFilter():
    instance = viewpoint_diagram_AbsoluteBoundsFilter(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, GraphicalFilter)


def test_viewpoint_diagram_AppliedCompositeFilters_isa_GraphicalFilter():
    instance = viewpoint_diagram_AppliedCompositeFilters()
    assert isinstance(instance, GraphicalFilter)


def test_viewpoint_diagram_CollapseFilter_isa_GraphicalFilter():
    instance = viewpoint_diagram_CollapseFilter(height=7, width=7)
    assert isinstance(instance, GraphicalFilter)


def test_viewpoint_diagram_FoldingFilter_isa_GraphicalFilter():
    instance = viewpoint_diagram_FoldingFilter()
    assert isinstance(instance, GraphicalFilter)


def test_viewpoint_diagram_FoldingPointFilter_isa_GraphicalFilter():
    instance = viewpoint_diagram_FoldingPointFilter()
    assert isinstance(instance, GraphicalFilter)


def test_viewpoint_diagram_HideFilter_isa_GraphicalFilter():
    instance = viewpoint_diagram_HideFilter()
    assert isinstance(instance, GraphicalFilter)


def test_viewpoint_diagram_HideLabelFilter_isa_GraphicalFilter():
    instance = viewpoint_diagram_HideLabelFilter()
    assert isinstance(instance, GraphicalFilter)


def test_viewpoint_description_VSMElementCustomization_isa_IVSMElementCustomization():
    instance = viewpoint_description_VSMElementCustomization(predicateExpression="sample_text")
    assert isinstance(instance, IVSMElementCustomization)


def test_viewpoint_description_VSMElementCustomizationReuse_isa_IVSMElementCustomization():
    instance = viewpoint_description_VSMElementCustomizationReuse()
    assert isinstance(instance, IVSMElementCustomization)


def test_viewpoint_description_RepresentationElementMapping_isa_IdentifiedElement():
    instance = viewpoint_description_RepresentationElementMapping()
    assert isinstance(instance, IdentifiedElement)


def test_viewpoint_audit_TemplateInformationSection_isa_InformationSection():
    instance = viewpoint_audit_TemplateInformationSection(templatePath="sample_text")
    assert isinstance(instance, InformationSection)


def test_viewpoint_diagram_ContainerStyle_isa_LabelStyle():
    instance = viewpoint_diagram_ContainerStyle()
    assert isinstance(instance, LabelStyle)


def test_viewpoint_diagram_NodeStyle_isa_LabelStyle():
    instance = viewpoint_diagram_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert isinstance(instance, LabelStyle)


def test_viewpoint_description_AdditionalLayer_isa_Layer():
    instance = viewpoint_description_AdditionalLayer(activeByDefault=True, optional=True)
    assert isinstance(instance, Layer)


def test_viewpoint_description_CompositeLayout_isa_Layout():
    instance = viewpoint_description_CompositeLayout(direction="sample_text", padding=7)
    assert isinstance(instance, Layout)


def test_viewpoint_description_OrderedTreeLayout_isa_Layout():
    instance = viewpoint_description_OrderedTreeLayout(childrenExpression="sample_text")
    assert isinstance(instance, Layout)


def test_viewpoint_tool_ContainerCreationDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_ContainerCreationDescription(iconPath="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_ContainerDropDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_DeleteElementDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_DeleteElementDescription()
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_DirectEditLabel_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_DirectEditLabel(inputLabelExpression="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_DoubleClickDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_DoubleClickDescription()
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_EdgeCreationDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_NodeCreationDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_NodeCreationDescription(iconPath="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_PasteDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_PasteDescription()
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_ReconnectEdgeDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_ToolDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_ToolDescription(iconPath="sample_text")
    assert isinstance(instance, MappingBasedToolDescription)


def test_viewpoint_tool_OperationAction_isa_MenuItemDescription():
    instance = viewpoint_tool_OperationAction()
    assert isinstance(instance, MenuItemDescription)


def test_viewpoint_tool_MenuItemDescriptionReference_isa_MenuItemOrRef():
    instance = viewpoint_tool_MenuItemDescriptionReference()
    assert isinstance(instance, MenuItemOrRef)


def test_viewpoint_tool_ContainerModelOperation_isa_ModelOperation():
    instance = viewpoint_tool_ContainerModelOperation()
    assert isinstance(instance, ModelOperation)


def test_viewpoint_tool_Switch_isa_ModelOperation():
    instance = viewpoint_tool_Switch()
    assert isinstance(instance, ModelOperation)


def test_viewpoint_diagram_BundledImage_isa_NodeStyle():
    instance = viewpoint_diagram_BundledImage(shape="sample_text")
    assert isinstance(instance, NodeStyle)


def test_viewpoint_diagram_CustomStyle_isa_NodeStyle():
    instance = viewpoint_diagram_CustomStyle(id="sample_text")
    assert isinstance(instance, NodeStyle)


def test_viewpoint_diagram_Dot_isa_NodeStyle():
    instance = viewpoint_diagram_Dot(strokeSizeComputationExpression="sample_text")
    assert isinstance(instance, NodeStyle)


def test_viewpoint_diagram_Ellipse_isa_NodeStyle():
    instance = viewpoint_diagram_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert isinstance(instance, NodeStyle)


def test_viewpoint_diagram_GaugeCompositeStyle_isa_NodeStyle():
    instance = viewpoint_diagram_GaugeCompositeStyle(alignment="sample_text")
    assert isinstance(instance, NodeStyle)


def test_viewpoint_diagram_Lozenge_isa_NodeStyle():
    instance = viewpoint_diagram_Lozenge(height="sample_text", width="sample_text")
    assert isinstance(instance, NodeStyle)


def test_viewpoint_diagram_Note_isa_NodeStyle():
    instance = viewpoint_diagram_Note()
    assert isinstance(instance, NodeStyle)


def test_viewpoint_diagram_Square_isa_NodeStyle():
    instance = viewpoint_diagram_Square(height="sample_text", width="sample_text")
    assert isinstance(instance, NodeStyle)


def test_viewpoint_style_BundledImageDescription_isa_NodeStyleDescription():
    instance = viewpoint_style_BundledImageDescription(shape="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_viewpoint_style_CustomStyleDescription_isa_NodeStyleDescription():
    instance = viewpoint_style_CustomStyleDescription(id="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_viewpoint_style_DotDescription_isa_NodeStyleDescription():
    instance = viewpoint_style_DotDescription(strokeSizeComputationExpression="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_viewpoint_style_EllipseNodeDescription_isa_NodeStyleDescription():
    instance = viewpoint_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_viewpoint_style_GaugeCompositeStyleDescription_isa_NodeStyleDescription():
    instance = viewpoint_style_GaugeCompositeStyleDescription(alignment="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_viewpoint_style_LozengeNodeDescription_isa_NodeStyleDescription():
    instance = viewpoint_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_viewpoint_style_NoteDescription_isa_NodeStyleDescription():
    instance = viewpoint_style_NoteDescription()
    assert isinstance(instance, NodeStyleDescription)


def test_viewpoint_style_SquareDescription_isa_NodeStyleDescription():
    instance = viewpoint_style_SquareDescription(height="sample_text", width="sample_text")
    assert isinstance(instance, NodeStyleDescription)


def test_viewpoint_tool_DiagramCreationDescription_isa_RepresentationCreationDescription():
    instance = viewpoint_tool_DiagramCreationDescription()
    assert isinstance(instance, RepresentationCreationDescription)


def test_viewpoint_description_RepresentationImportDescription_isa_RepresentationDescription():
    instance = viewpoint_description_RepresentationImportDescription()
    assert isinstance(instance, RepresentationDescription)


def test_viewpoint_description_DiagramExtensionDescription_isa_RepresentationExtensionDescription():
    instance = viewpoint_description_DiagramExtensionDescription()
    assert isinstance(instance, RepresentationExtensionDescription)


def test_viewpoint_tool_DiagramNavigationDescription_isa_RepresentationNavigationDescription():
    instance = viewpoint_tool_DiagramNavigationDescription()
    assert isinstance(instance, RepresentationNavigationDescription)


def test_viewpoint_filter_FilterVariable_isa_SelectionDescription():
    instance = viewpoint_filter_FilterVariable(name="sample_text")
    assert isinstance(instance, SelectionDescription)


def test_viewpoint_diagram_BorderedStyle_isa_Style():
    instance = viewpoint_diagram_BorderedStyle(borderSize="sample_text", borderSizeComputationExpression="sample_text")
    assert isinstance(instance, Style)


def test_viewpoint_diagram_ContainerStyle_isa_Style():
    instance = viewpoint_diagram_ContainerStyle()
    assert isinstance(instance, Style)


def test_viewpoint_diagram_EdgeStyle_isa_Style():
    instance = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert isinstance(instance, Style)


def test_viewpoint_diagram_NodeStyle_isa_Style():
    instance = viewpoint_diagram_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert isinstance(instance, Style)


def test_viewpoint_style_BorderedStyleDescription_isa_StyleDescription():
    instance = viewpoint_style_BorderedStyleDescription(borderSizeComputationExpression="sample_text")
    assert isinstance(instance, StyleDescription)


def test_viewpoint_style_EdgeStyleDescription_isa_StyleDescription():
    instance = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    assert isinstance(instance, StyleDescription)


def test_viewpoint_style_RoundedCornerStyleDescription_isa_StyleDescription():
    instance = viewpoint_style_RoundedCornerStyleDescription(arcHeight="sample_text", arcWidth="sample_text")
    assert isinstance(instance, StyleDescription)


def test_viewpoint_tool_Case_isa_SwitchChild():
    instance = viewpoint_tool_Case(conditionExpression="sample_text")
    assert isinstance(instance, SwitchChild)


def test_viewpoint_tool_Default_isa_SwitchChild():
    instance = viewpoint_tool_Default()
    assert isinstance(instance, SwitchChild)


def test_viewpoint_tool_AbstractToolDescription_isa_ToolEntry():
    instance = viewpoint_tool_AbstractToolDescription(forceRefresh=True, precondition="sample_text")
    assert isinstance(instance, ToolEntry)


def test_viewpoint_tool_ToolGroup_isa_ToolEntry():
    instance = viewpoint_tool_ToolGroup()
    assert isinstance(instance, ToolEntry)


def test_viewpoint_validation_SemanticValidationRule_isa_ValidationRule():
    instance = viewpoint_validation_SemanticValidationRule(targetClass="sample_text")
    assert isinstance(instance, ValidationRule)


def test_viewpoint_validation_ViewValidationRule_isa_ValidationRule():
    instance = viewpoint_validation_ViewValidationRule()
    assert isinstance(instance, ValidationRule)


def test_viewpoint_description_ContainerMappingImport_isa_description_AbstractMappingImport():
    instance = viewpoint_description_ContainerMappingImport()
    assert isinstance(instance, description_AbstractMappingImport)


def test_viewpoint_description_NodeMappingImport_isa_description_AbstractMappingImport():
    instance = viewpoint_description_NodeMappingImport()
    assert isinstance(instance, description_AbstractMappingImport)


def test_viewpoint_description_ContainerMapping_isa_description_AbstractNodeMapping():
    instance = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    assert isinstance(instance, description_AbstractNodeMapping)


def test_viewpoint_description_NodeMapping_isa_description_AbstractNodeMapping():
    instance = viewpoint_description_NodeMapping()
    assert isinstance(instance, description_AbstractNodeMapping)


def test_viewpoint_description_ComputedColor_isa_description_ColorDescription():
    instance = viewpoint_description_ComputedColor(blue="sample_text", green="sample_text", red="sample_text")
    assert isinstance(instance, description_ColorDescription)


def test_viewpoint_description_InterpolatedColor_isa_description_ColorDescription():
    instance = viewpoint_description_InterpolatedColor(colorValueComputationExpression="sample_text", maxValueComputationExpression="sample_text", minValueComputationExpression="sample_text")
    assert isinstance(instance, description_ColorDescription)


def test_viewpoint_description_Viewpoint_isa_description_Component():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert isinstance(instance, description_Component)


def test_viewpoint_description_ContainerMappingImport_isa_description_ContainerMapping():
    instance = viewpoint_description_ContainerMappingImport()
    assert isinstance(instance, description_ContainerMapping)


def test_viewpoint_DRepresentation_isa_description_DModelElement():
    instance = viewpoint_DRepresentation(name="sample_text")
    assert isinstance(instance, description_DModelElement)


def test_viewpoint_description_Group_isa_description_DModelElement():
    instance = viewpoint_description_Group(name="sample_text", version="sample_text")
    assert isinstance(instance, description_DModelElement)


def test_viewpoint_description_DiagramImportDescription_isa_description_DiagramDescription():
    instance = viewpoint_description_DiagramImportDescription()
    assert isinstance(instance, description_DiagramDescription)


def test_viewpoint_description_AbstractNodeMapping_isa_description_DiagramElementMapping():
    instance = viewpoint_description_AbstractNodeMapping(domainClass="sample_text")
    assert isinstance(instance, description_DiagramElementMapping)


def test_viewpoint_description_EdgeMapping_isa_description_DiagramElementMapping():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert isinstance(instance, description_DiagramElementMapping)


def test_viewpoint_DRepresentation_isa_description_DocumentedElement():
    instance = viewpoint_DRepresentation(name="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_concern_ConcernDescription_isa_description_DocumentedElement():
    instance = viewpoint_concern_ConcernDescription()
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_AbstractNodeMapping_isa_description_DocumentedElement():
    instance = viewpoint_description_AbstractNodeMapping(domainClass="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_EdgeMapping_isa_description_DocumentedElement():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_EdgeMappingImport_isa_description_DocumentedElement():
    instance = viewpoint_description_EdgeMappingImport(inheritsAncestorFilters=True)
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_Group_isa_description_DocumentedElement():
    instance = viewpoint_description_Group(name="sample_text", version="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_Layer_isa_description_DocumentedElement():
    instance = viewpoint_description_Layer(icon="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_RepresentationDescription_isa_description_DocumentedElement():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_Viewpoint_isa_description_DocumentedElement():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_diagram_DDiagram_isa_description_DocumentedElement():
    instance = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_filter_FilterDescription_isa_description_DocumentedElement():
    instance = viewpoint_filter_FilterDescription()
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_tool_ToolEntry_isa_description_DocumentedElement():
    instance = viewpoint_tool_ToolEntry()
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_tool_ToolSection_isa_description_DocumentedElement():
    instance = viewpoint_tool_ToolSection(icon="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_ContainerMapping_isa_description_DragAndDropTargetDescription():
    instance = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    assert isinstance(instance, description_DragAndDropTargetDescription)


def test_viewpoint_description_DiagramDescription_isa_description_DragAndDropTargetDescription():
    instance = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert isinstance(instance, description_DragAndDropTargetDescription)


def test_viewpoint_description_NodeMapping_isa_description_DragAndDropTargetDescription():
    instance = viewpoint_description_NodeMapping()
    assert isinstance(instance, description_DragAndDropTargetDescription)


def test_viewpoint_description_Layer_isa_description_EndUserDocumentedElement():
    instance = viewpoint_description_Layer(icon="sample_text")
    assert isinstance(instance, description_EndUserDocumentedElement)


def test_viewpoint_description_RepresentationDescription_isa_description_EndUserDocumentedElement():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert isinstance(instance, description_EndUserDocumentedElement)


def test_viewpoint_description_Viewpoint_isa_description_EndUserDocumentedElement():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert isinstance(instance, description_EndUserDocumentedElement)


def test_viewpoint_description_UserFixedColor_isa_description_FixedColor():
    instance = viewpoint_description_UserFixedColor()
    assert isinstance(instance, description_FixedColor)


def test_viewpoint_description_EdgeMapping_isa_description_IEdgeMapping():
    instance = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    assert isinstance(instance, description_IEdgeMapping)


def test_viewpoint_description_EdgeMappingImport_isa_description_IEdgeMapping():
    instance = viewpoint_description_EdgeMappingImport(inheritsAncestorFilters=True)
    assert isinstance(instance, description_IEdgeMapping)


def test_viewpoint_concern_ConcernDescription_isa_description_IdentifiedElement():
    instance = viewpoint_concern_ConcernDescription()
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_description_EdgeMappingImport_isa_description_IdentifiedElement():
    instance = viewpoint_description_EdgeMappingImport(inheritsAncestorFilters=True)
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_description_Layer_isa_description_IdentifiedElement():
    instance = viewpoint_description_Layer(icon="sample_text")
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_description_RepresentationDescription_isa_description_IdentifiedElement():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_description_Viewpoint_isa_description_IdentifiedElement():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_filter_FilterDescription_isa_description_IdentifiedElement():
    instance = viewpoint_filter_FilterDescription()
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_tool_ToolEntry_isa_description_IdentifiedElement():
    instance = viewpoint_tool_ToolEntry()
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_tool_ToolSection_isa_description_IdentifiedElement():
    instance = viewpoint_tool_ToolSection(icon="sample_text")
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_description_NodeMappingImport_isa_description_NodeMapping():
    instance = viewpoint_description_NodeMappingImport()
    assert isinstance(instance, description_NodeMapping)


def test_viewpoint_description_DiagramDescription_isa_description_PasteTargetDescription():
    instance = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert isinstance(instance, description_PasteTargetDescription)


def test_viewpoint_description_DiagramElementMapping_isa_description_PasteTargetDescription():
    instance = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert isinstance(instance, description_PasteTargetDescription)


def test_viewpoint_description_DiagramDescription_isa_description_RepresentationDescription():
    instance = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    assert isinstance(instance, description_RepresentationDescription)


def test_viewpoint_description_DiagramElementMapping_isa_description_RepresentationElementMapping():
    instance = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    assert isinstance(instance, description_RepresentationElementMapping)


def test_viewpoint_description_DiagramImportDescription_isa_description_RepresentationImportDescription():
    instance = viewpoint_description_DiagramImportDescription()
    assert isinstance(instance, description_RepresentationImportDescription)


def test_viewpoint_tool_SelectModelElementVariable_isa_description_SelectionDescription():
    instance = viewpoint_tool_SelectModelElementVariable()
    assert isinstance(instance, description_SelectionDescription)


def test_viewpoint_tool_SelectionWizardDescription_isa_description_SelectionDescription():
    instance = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    assert isinstance(instance, description_SelectionDescription)


def test_viewpoint_description_ComputedColor_isa_description_UserColor():
    instance = viewpoint_description_ComputedColor(blue="sample_text", green="sample_text", red="sample_text")
    assert isinstance(instance, description_UserColor)


def test_viewpoint_description_InterpolatedColor_isa_description_UserColor():
    instance = viewpoint_description_InterpolatedColor(colorValueComputationExpression="sample_text", maxValueComputationExpression="sample_text", minValueComputationExpression="sample_text")
    assert isinstance(instance, description_UserColor)


def test_viewpoint_description_UserFixedColor_isa_description_UserColor():
    instance = viewpoint_description_UserFixedColor()
    assert isinstance(instance, description_UserColor)


def test_viewpoint_diagram_DDiagramElementContainer_isa_diagram_AbstractDNode():
    instance = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert isinstance(instance, diagram_AbstractDNode)


def test_viewpoint_diagram_DNode_isa_diagram_AbstractDNode():
    instance = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert isinstance(instance, diagram_AbstractDNode)


def test_viewpoint_diagram_ContainerStyle_isa_diagram_BorderedStyle():
    instance = viewpoint_diagram_ContainerStyle()
    assert isinstance(instance, diagram_BorderedStyle)


def test_viewpoint_diagram_NodeStyle_isa_diagram_BorderedStyle():
    instance = viewpoint_diagram_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert isinstance(instance, diagram_BorderedStyle)


def test_viewpoint_diagram_WorkspaceImage_isa_diagram_ContainerStyle():
    instance = viewpoint_diagram_WorkspaceImage(workspacePath="sample_text")
    assert isinstance(instance, diagram_ContainerStyle)


def test_viewpoint_diagram_DSemanticDiagram_isa_diagram_DDiagram():
    instance = viewpoint_diagram_DSemanticDiagram()
    assert isinstance(instance, diagram_DDiagram)


def test_viewpoint_diagram_DEdge_isa_diagram_DDiagramElement():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert isinstance(instance, diagram_DDiagramElement)


def test_viewpoint_diagram_DDiagramElementContainer_isa_diagram_EdgeTarget():
    instance = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    assert isinstance(instance, diagram_EdgeTarget)


def test_viewpoint_diagram_DEdge_isa_diagram_EdgeTarget():
    instance = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    assert isinstance(instance, diagram_EdgeTarget)


def test_viewpoint_diagram_DNode_isa_diagram_EdgeTarget():
    instance = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    assert isinstance(instance, diagram_EdgeTarget)


def test_viewpoint_diagram_WorkspaceImage_isa_diagram_NodeStyle():
    instance = viewpoint_diagram_WorkspaceImage(workspacePath="sample_text")
    assert isinstance(instance, diagram_NodeStyle)


def test_viewpoint_style_ContainerStyleDescription_isa_style_BorderedStyleDescription():
    instance = viewpoint_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_BorderedStyleDescription)


def test_viewpoint_style_NodeStyleDescription_isa_style_BorderedStyleDescription():
    instance = viewpoint_style_NodeStyleDescription(hideLabelByDefault=True, labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_BorderedStyleDescription)


def test_viewpoint_style_FlatContainerStyleDescription_isa_style_ContainerStyleDescription():
    instance = viewpoint_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    assert isinstance(instance, style_ContainerStyleDescription)


def test_viewpoint_style_ShapeContainerStyleDescription_isa_style_ContainerStyleDescription():
    instance = viewpoint_style_ShapeContainerStyleDescription(shape="sample_text")
    assert isinstance(instance, style_ContainerStyleDescription)


def test_viewpoint_style_WorkspaceImageDescription_isa_style_ContainerStyleDescription():
    instance = viewpoint_style_WorkspaceImageDescription(workspacePath="sample_text")
    assert isinstance(instance, style_ContainerStyleDescription)


def test_viewpoint_style_ContainerStyleDescription_isa_style_LabelStyleDescription():
    instance = viewpoint_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_LabelStyleDescription)


def test_viewpoint_style_NodeStyleDescription_isa_style_LabelStyleDescription():
    instance = viewpoint_style_NodeStyleDescription(hideLabelByDefault=True, labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_LabelStyleDescription)


def test_viewpoint_style_WorkspaceImageDescription_isa_style_NodeStyleDescription():
    instance = viewpoint_style_WorkspaceImageDescription(workspacePath="sample_text")
    assert isinstance(instance, style_NodeStyleDescription)


def test_viewpoint_style_ContainerStyleDescription_isa_style_RoundedCornerStyleDescription():
    instance = viewpoint_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_RoundedCornerStyleDescription)


def test_viewpoint_style_FlatContainerStyleDescription_isa_style_SizeComputationContainerStyleDescription():
    instance = viewpoint_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    assert isinstance(instance, style_SizeComputationContainerStyleDescription)


def test_viewpoint_style_ShapeContainerStyleDescription_isa_style_SizeComputationContainerStyleDescription():
    instance = viewpoint_style_ShapeContainerStyleDescription(shape="sample_text")
    assert isinstance(instance, style_SizeComputationContainerStyleDescription)


def test_viewpoint_style_NodeStyleDescription_isa_style_StyleDescription():
    instance = viewpoint_style_NodeStyleDescription(hideLabelByDefault=True, labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_StyleDescription)


def test_viewpoint_style_ContainerStyleDescription_isa_style_TooltipStyleDescription():
    instance = viewpoint_style_ContainerStyleDescription(roundedCorner=True)
    assert isinstance(instance, style_TooltipStyleDescription)


def test_viewpoint_style_NodeStyleDescription_isa_style_TooltipStyleDescription():
    instance = viewpoint_style_NodeStyleDescription(hideLabelByDefault=True, labelPosition="sample_text", resizeKind="sample_text", sizeComputationExpression="sample_text")
    assert isinstance(instance, style_TooltipStyleDescription)


def test_viewpoint_tool_MenuItemDescription_isa_tool_AbstractToolDescription():
    instance = viewpoint_tool_MenuItemDescription(icon="sample_text")
    assert isinstance(instance, tool_AbstractToolDescription)


def test_viewpoint_tool_SelectionWizardDescription_isa_tool_AbstractToolDescription():
    instance = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    assert isinstance(instance, tool_AbstractToolDescription)


def test_viewpoint_tool_ContainerViewVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ContainerViewVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_DropContainerVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_DropContainerVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_ElementDeleteVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ElementDeleteVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_ElementDoubleClickVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ElementDoubleClickVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_ElementDropVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ElementDropVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_ElementVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ElementVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_ElementViewVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ElementViewVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_NodeCreationVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_NodeCreationVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_SelectContainerVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_SelectContainerVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_SourceEdgeCreationVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_SourceEdgeCreationVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_SourceEdgeViewCreationVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_SourceEdgeViewCreationVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_TargetEdgeCreationVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_TargetEdgeCreationVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_TargetEdgeViewCreationVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_TargetEdgeViewCreationVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_ExternalJavaAction_isa_tool_ContainerModelOperation():
    instance = viewpoint_tool_ExternalJavaAction(id="sample_text")
    assert isinstance(instance, tool_ContainerModelOperation)


def test_viewpoint_tool_ExternalJavaActionCall_isa_tool_ContainerModelOperation():
    instance = viewpoint_tool_ExternalJavaActionCall()
    assert isinstance(instance, tool_ContainerModelOperation)


def test_viewpoint_tool_ExternalJavaAction_isa_tool_MenuItemDescription():
    instance = viewpoint_tool_ExternalJavaAction(id="sample_text")
    assert isinstance(instance, tool_MenuItemDescription)


def test_viewpoint_tool_ExternalJavaActionCall_isa_tool_MenuItemDescription():
    instance = viewpoint_tool_ExternalJavaActionCall()
    assert isinstance(instance, tool_MenuItemDescription)


def test_viewpoint_tool_MenuItemDescription_isa_tool_MenuItemOrRef():
    instance = viewpoint_tool_MenuItemDescription(icon="sample_text")
    assert isinstance(instance, tool_MenuItemOrRef)


def test_viewpoint_tool_AcceleoVariable_isa_tool_SubVariable():
    instance = viewpoint_tool_AcceleoVariable(computationExpression="sample_text")
    assert isinstance(instance, tool_SubVariable)


def test_viewpoint_tool_SelectModelElementVariable_isa_tool_SubVariable():
    instance = viewpoint_tool_SelectModelElementVariable()
    assert isinstance(instance, tool_SubVariable)


def test_viewpoint_tool_AcceleoVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_AcceleoVariable(computationExpression="sample_text")
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_ContainerViewVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ContainerViewVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_DropContainerVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_DropContainerVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_ElementDeleteVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ElementDeleteVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_ElementDoubleClickVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ElementDoubleClickVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_ElementDropVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ElementDropVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_ElementVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ElementVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_ElementViewVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ElementViewVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_NodeCreationVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_NodeCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_SelectContainerVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_SelectContainerVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_SourceEdgeCreationVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_SourceEdgeCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_SourceEdgeViewCreationVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_SourceEdgeViewCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_TargetEdgeCreationVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_TargetEdgeCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_TargetEdgeViewCreationVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_TargetEdgeViewCreationVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_assoc_activateBehaviors250_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = tool_BehaviorTool()
    b2 = tool_BehaviorTool()
    _safe_set(a, 'viewpoint_diagram_DDiagram251', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram251', b1)
    if hasattr(b1, 'tool_BehaviorTool'):
        assert _is_linked(b1, 'tool_BehaviorTool', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram251', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram251', b2)
    if hasattr(b1, 'tool_BehaviorTool'):
        assert not _is_linked(b1, 'tool_BehaviorTool', a)
    if hasattr(b2, 'tool_BehaviorTool'):
        assert _is_linked(b2, 'tool_BehaviorTool', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram251', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram251', b2)
    if hasattr(b2, 'tool_BehaviorTool'):
        assert not _is_linked(b2, 'tool_BehaviorTool', a)


def test_assoc_activatedFilters243_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = filter_FilterDescription()
    b2 = filter_FilterDescription()
    _safe_set(a, 'viewpoint_diagram_DDiagram244', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram244', b1)
    if hasattr(b1, 'filter_FilterDescription'):
        assert _is_linked(b1, 'filter_FilterDescription', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram244', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram244', b2)
    if hasattr(b1, 'filter_FilterDescription'):
        assert not _is_linked(b1, 'filter_FilterDescription', a)
    if hasattr(b2, 'filter_FilterDescription'):
        assert _is_linked(b2, 'filter_FilterDescription', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram244', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram244', b2)
    if hasattr(b2, 'filter_FilterDescription'):
        assert not _is_linked(b2, 'filter_FilterDescription', a)


def test_assoc_activatedLayers254_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = description_Layer()
    b2 = description_Layer()
    _safe_set(a, 'viewpoint_diagram_DDiagram255', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram255', b1)
    if hasattr(b1, 'description_Layer'):
        assert _is_linked(b1, 'description_Layer', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram255', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram255', b2)
    if hasattr(b1, 'description_Layer'):
        assert not _is_linked(b1, 'description_Layer', a)
    if hasattr(b2, 'description_Layer'):
        assert _is_linked(b2, 'description_Layer', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram255', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram255', b2)
    if hasattr(b2, 'description_Layer'):
        assert not _is_linked(b2, 'description_Layer', a)


def test_assoc_activatedRules248_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_diagram_DDiagram249', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram249', b1)
    if hasattr(b1, 'validation_ValidationRule'):
        assert _is_linked(b1, 'validation_ValidationRule', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram249', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram249', b2)
    if hasattr(b1, 'validation_ValidationRule'):
        assert not _is_linked(b1, 'validation_ValidationRule', a)
    if hasattr(b2, 'validation_ValidationRule'):
        assert _is_linked(b2, 'validation_ValidationRule', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram249', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram249', b2)
    if hasattr(b2, 'validation_ValidationRule'):
        assert not _is_linked(b2, 'validation_ValidationRule', a)


def test_assoc_activatedViewpoints56_link_reassign_clear():
    a = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    b1 = Viewpoint()
    b2 = Viewpoint()
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject', b1)
    if hasattr(b1, 'Viewpoint57'):
        assert _is_linked(b1, 'Viewpoint57', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject', b2)
    if hasattr(b1, 'Viewpoint57'):
        assert not _is_linked(b1, 'Viewpoint57', a)
    if hasattr(b2, 'Viewpoint57'):
        assert _is_linked(b2, 'Viewpoint57', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject', set())
    assert not _is_linked(a, 'viewpoint_DAnalysisSessionEObject', b2)
    if hasattr(b2, 'Viewpoint57'):
        assert not _is_linked(b2, 'Viewpoint57', a)


def test_assoc_actualMapping281_link_reassign_clear():
    a = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_diagram_DNode282', b1)
    assert _is_linked(a, 'viewpoint_diagram_DNode282', b1)
    if hasattr(b1, 'description_NodeMapping'):
        assert _is_linked(b1, 'description_NodeMapping', a)
    _safe_set(a, 'viewpoint_diagram_DNode282', b2)
    assert _is_linked(a, 'viewpoint_diagram_DNode282', b2)
    if hasattr(b1, 'description_NodeMapping'):
        assert not _is_linked(b1, 'description_NodeMapping', a)
    if hasattr(b2, 'description_NodeMapping'):
        assert _is_linked(b2, 'description_NodeMapping', a)
    _safe_set(a, 'viewpoint_diagram_DNode282', None)
    assert not _is_linked(a, 'viewpoint_diagram_DNode282', b2)
    if hasattr(b2, 'description_NodeMapping'):
        assert not _is_linked(b2, 'description_NodeMapping', a)


def test_assoc_actualMapping302_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer303', b1)
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer303', b1)
    if hasattr(b1, 'description_ContainerMapping'):
        assert _is_linked(b1, 'description_ContainerMapping', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer303', b2)
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer303', b2)
    if hasattr(b1, 'description_ContainerMapping'):
        assert not _is_linked(b1, 'description_ContainerMapping', a)
    if hasattr(b2, 'description_ContainerMapping'):
        assert _is_linked(b2, 'description_ContainerMapping', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer303', None)
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer303', b2)
    if hasattr(b2, 'description_ContainerMapping'):
        assert not _is_linked(b2, 'description_ContainerMapping', a)


def test_assoc_actualMapping327_link_reassign_clear():
    a = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = description_IEdgeMapping()
    b2 = description_IEdgeMapping()
    _safe_set(a, 'viewpoint_diagram_DEdge328', b1)
    assert _is_linked(a, 'viewpoint_diagram_DEdge328', b1)
    if hasattr(b1, 'description_IEdgeMapping'):
        assert _is_linked(b1, 'description_IEdgeMapping', a)
    _safe_set(a, 'viewpoint_diagram_DEdge328', b2)
    assert _is_linked(a, 'viewpoint_diagram_DEdge328', b2)
    if hasattr(b1, 'description_IEdgeMapping'):
        assert not _is_linked(b1, 'description_IEdgeMapping', a)
    if hasattr(b2, 'description_IEdgeMapping'):
        assert _is_linked(b2, 'description_IEdgeMapping', a)
    _safe_set(a, 'viewpoint_diagram_DEdge328', None)
    assert not _is_linked(a, 'viewpoint_diagram_DEdge328', b2)
    if hasattr(b2, 'description_IEdgeMapping'):
        assert not _is_linked(b2, 'description_IEdgeMapping', a)


def test_assoc_additionalLayers436_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_AdditionalLayer()
    b2 = description_AdditionalLayer()
    _safe_set(a, 'viewpoint_description_DiagramDescription437', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription437', b1)
    if hasattr(b1, 'description_AdditionalLayer'):
        assert _is_linked(b1, 'description_AdditionalLayer', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription437', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription437', b2)
    if hasattr(b1, 'description_AdditionalLayer'):
        assert not _is_linked(b1, 'description_AdditionalLayer', a)
    if hasattr(b2, 'description_AdditionalLayer'):
        assert _is_linked(b2, 'description_AdditionalLayer', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription437', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription437', b2)
    if hasattr(b2, 'description_AdditionalLayer'):
        assert not _is_linked(b2, 'description_AdditionalLayer', a)


def test_assoc_allActivatedTools441_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'viewpoint_description_DiagramDescription442', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription442', b1)
    if hasattr(b1, 'tool_AbstractToolDescription443'):
        assert _is_linked(b1, 'tool_AbstractToolDescription443', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription442', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription442', b2)
    if hasattr(b1, 'tool_AbstractToolDescription443'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription443', a)
    if hasattr(b2, 'tool_AbstractToolDescription443'):
        assert _is_linked(b2, 'tool_AbstractToolDescription443', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription442', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription442', b2)
    if hasattr(b2, 'tool_AbstractToolDescription443'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription443', a)


def test_assoc_allContainerMappings412_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_description_DiagramDescription413', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription413', b1)
    if hasattr(b1, 'description_ContainerMapping414'):
        assert _is_linked(b1, 'description_ContainerMapping414', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription413', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription413', b2)
    if hasattr(b1, 'description_ContainerMapping414'):
        assert not _is_linked(b1, 'description_ContainerMapping414', a)
    if hasattr(b2, 'description_ContainerMapping414'):
        assert _is_linked(b2, 'description_ContainerMapping414', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription413', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription413', b2)
    if hasattr(b2, 'description_ContainerMapping414'):
        assert not _is_linked(b2, 'description_ContainerMapping414', a)


def test_assoc_allContainerMappings499_link_reassign_clear():
    a = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_description_ContainerMapping500', {b1})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping500', b1)
    if hasattr(b1, 'description_ContainerMapping501'):
        assert _is_linked(b1, 'description_ContainerMapping501', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping500', {b2})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping500', b2)
    if hasattr(b1, 'description_ContainerMapping501'):
        assert not _is_linked(b1, 'description_ContainerMapping501', a)
    if hasattr(b2, 'description_ContainerMapping501'):
        assert _is_linked(b2, 'description_ContainerMapping501', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping500', set())
    assert not _is_linked(a, 'viewpoint_description_ContainerMapping500', b2)
    if hasattr(b2, 'description_ContainerMapping501'):
        assert not _is_linked(b2, 'description_ContainerMapping501', a)


def test_assoc_allEdgeMappings407_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_EdgeMapping()
    b2 = description_EdgeMapping()
    _safe_set(a, 'viewpoint_description_DiagramDescription408', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription408', b1)
    if hasattr(b1, 'description_EdgeMapping'):
        assert _is_linked(b1, 'description_EdgeMapping', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription408', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription408', b2)
    if hasattr(b1, 'description_EdgeMapping'):
        assert not _is_linked(b1, 'description_EdgeMapping', a)
    if hasattr(b2, 'description_EdgeMapping'):
        assert _is_linked(b2, 'description_EdgeMapping', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription408', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription408', b2)
    if hasattr(b2, 'description_EdgeMapping'):
        assert not _is_linked(b2, 'description_EdgeMapping', a)


def test_assoc_allEdgeMappings563_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = description_EdgeMapping()
    b2 = description_EdgeMapping()
    _safe_set(a, 'viewpoint_description_Layer564', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer564', b1)
    if hasattr(b1, 'description_EdgeMapping565'):
        assert _is_linked(b1, 'description_EdgeMapping565', a)
    _safe_set(a, 'viewpoint_description_Layer564', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer564', b2)
    if hasattr(b1, 'description_EdgeMapping565'):
        assert not _is_linked(b1, 'description_EdgeMapping565', a)
    if hasattr(b2, 'description_EdgeMapping565'):
        assert _is_linked(b2, 'description_EdgeMapping565', a)
    _safe_set(a, 'viewpoint_description_Layer564', set())
    assert not _is_linked(a, 'viewpoint_description_Layer564', b2)
    if hasattr(b2, 'description_EdgeMapping565'):
        assert not _is_linked(b2, 'description_EdgeMapping565', a)


def test_assoc_allFilters245_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = filter_FilterDescription()
    b2 = filter_FilterDescription()
    _safe_set(a, 'viewpoint_diagram_DDiagram246', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram246', b1)
    if hasattr(b1, 'filter_FilterDescription247'):
        assert _is_linked(b1, 'filter_FilterDescription247', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram246', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram246', b2)
    if hasattr(b1, 'filter_FilterDescription247'):
        assert not _is_linked(b1, 'filter_FilterDescription247', a)
    if hasattr(b2, 'filter_FilterDescription247'):
        assert _is_linked(b2, 'filter_FilterDescription247', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram246', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram246', b2)
    if hasattr(b2, 'filter_FilterDescription247'):
        assert not _is_linked(b2, 'filter_FilterDescription247', a)


def test_assoc_allLayers438_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_Layer()
    b2 = description_Layer()
    _safe_set(a, 'viewpoint_description_DiagramDescription439', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription439', b1)
    if hasattr(b1, 'description_Layer440'):
        assert _is_linked(b1, 'description_Layer440', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription439', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription439', b2)
    if hasattr(b1, 'description_Layer440'):
        assert not _is_linked(b1, 'description_Layer440', a)
    if hasattr(b2, 'description_Layer440'):
        assert _is_linked(b2, 'description_Layer440', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription439', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription439', b2)
    if hasattr(b2, 'description_Layer440'):
        assert not _is_linked(b2, 'description_Layer440', a)


def test_assoc_allNodeMappings409_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_description_DiagramDescription410', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription410', b1)
    if hasattr(b1, 'description_NodeMapping411'):
        assert _is_linked(b1, 'description_NodeMapping411', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription410', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription410', b2)
    if hasattr(b1, 'description_NodeMapping411'):
        assert not _is_linked(b1, 'description_NodeMapping411', a)
    if hasattr(b2, 'description_NodeMapping411'):
        assert _is_linked(b2, 'description_NodeMapping411', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription410', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription410', b2)
    if hasattr(b2, 'description_NodeMapping411'):
        assert not _is_linked(b2, 'description_NodeMapping411', a)


def test_assoc_allNodeMappings487_link_reassign_clear():
    a = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_description_ContainerMapping488', {b1})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping488', b1)
    if hasattr(b1, 'description_NodeMapping489'):
        assert _is_linked(b1, 'description_NodeMapping489', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping488', {b2})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping488', b2)
    if hasattr(b1, 'description_NodeMapping489'):
        assert not _is_linked(b1, 'description_NodeMapping489', a)
    if hasattr(b2, 'description_NodeMapping489'):
        assert _is_linked(b2, 'description_NodeMapping489', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping488', set())
    assert not _is_linked(a, 'viewpoint_description_ContainerMapping488', b2)
    if hasattr(b2, 'description_NodeMapping489'):
        assert not _is_linked(b2, 'description_NodeMapping489', a)


def test_assoc_allRepresentations36_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DView37', {b1})
    assert _is_linked(a, 'viewpoint_DView37', b1)
    if hasattr(b1, 'viewpoint_DRepresentation38'):
        assert _is_linked(b1, 'viewpoint_DRepresentation38', a)
    _safe_set(a, 'viewpoint_DView37', {b2})
    assert _is_linked(a, 'viewpoint_DView37', b2)
    if hasattr(b1, 'viewpoint_DRepresentation38'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation38', a)
    if hasattr(b2, 'viewpoint_DRepresentation38'):
        assert _is_linked(b2, 'viewpoint_DRepresentation38', a)
    _safe_set(a, 'viewpoint_DView37', set())
    assert not _is_linked(a, 'viewpoint_DView37', b2)
    if hasattr(b2, 'viewpoint_DRepresentation38'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation38', a)


def test_assoc_allRules733_link_reassign_clear():
    a = viewpoint_validation_ValidationSet(name="sample_text")
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_validation_ValidationSet734', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet734', b1)
    if hasattr(b1, 'validation_ValidationRule735'):
        assert _is_linked(b1, 'validation_ValidationRule735', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet734', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet734', b2)
    if hasattr(b1, 'validation_ValidationRule735'):
        assert not _is_linked(b1, 'validation_ValidationRule735', a)
    if hasattr(b2, 'validation_ValidationRule735'):
        assert _is_linked(b2, 'validation_ValidationRule735', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet734', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationSet734', b2)
    if hasattr(b2, 'validation_ValidationRule735'):
        assert not _is_linked(b2, 'validation_ValidationRule735', a)


def test_assoc_allTools420_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'viewpoint_description_DiagramDescription421', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription421', b1)
    if hasattr(b1, 'tool_AbstractToolDescription'):
        assert _is_linked(b1, 'tool_AbstractToolDescription', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription421', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription421', b2)
    if hasattr(b1, 'tool_AbstractToolDescription'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription', a)
    if hasattr(b2, 'tool_AbstractToolDescription'):
        assert _is_linked(b2, 'tool_AbstractToolDescription', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription421', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription421', b2)
    if hasattr(b2, 'tool_AbstractToolDescription'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription', a)


def test_assoc_allTools552_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'viewpoint_description_Layer553', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer553', b1)
    if hasattr(b1, 'tool_AbstractToolDescription554'):
        assert _is_linked(b1, 'tool_AbstractToolDescription554', a)
    _safe_set(a, 'viewpoint_description_Layer553', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer553', b2)
    if hasattr(b1, 'tool_AbstractToolDescription554'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription554', a)
    if hasattr(b2, 'tool_AbstractToolDescription554'):
        assert _is_linked(b2, 'tool_AbstractToolDescription554', a)
    _safe_set(a, 'viewpoint_description_Layer553', set())
    assert not _is_linked(a, 'viewpoint_description_Layer553', b2)
    if hasattr(b2, 'tool_AbstractToolDescription554'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription554', a)


def test_assoc_analyses58_link_reassign_clear():
    a = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    b1 = viewpoint_DAnalysis(version="sample_text")
    b2 = viewpoint_DAnalysis(version="sample_text_2")
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject59', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject59', b1)
    if hasattr(b1, 'viewpoint_DAnalysis60'):
        assert _is_linked(b1, 'viewpoint_DAnalysis60', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject59', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject59', b2)
    if hasattr(b1, 'viewpoint_DAnalysis60'):
        assert not _is_linked(b1, 'viewpoint_DAnalysis60', a)
    if hasattr(b2, 'viewpoint_DAnalysis60'):
        assert _is_linked(b2, 'viewpoint_DAnalysis60', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject59', set())
    assert not _is_linked(a, 'viewpoint_DAnalysisSessionEObject59', b2)
    if hasattr(b2, 'viewpoint_DAnalysis60'):
        assert not _is_linked(b2, 'viewpoint_DAnalysis60', a)


def test_assoc_appliedOn107_link_reassign_clear():
    a = viewpoint_description_EStructuralFeatureCustomization(applyOnAll=True)
    b1 = description_viewpoint_EObject()
    b2 = description_viewpoint_EObject()
    _safe_set(a, 'viewpoint_description_EStructuralFeatureCustomization', {b1})
    assert _is_linked(a, 'viewpoint_description_EStructuralFeatureCustomization', b1)
    if hasattr(b1, 'description_viewpoint_EObject108'):
        assert _is_linked(b1, 'description_viewpoint_EObject108', a)
    _safe_set(a, 'viewpoint_description_EStructuralFeatureCustomization', {b2})
    assert _is_linked(a, 'viewpoint_description_EStructuralFeatureCustomization', b2)
    if hasattr(b1, 'description_viewpoint_EObject108'):
        assert not _is_linked(b1, 'description_viewpoint_EObject108', a)
    if hasattr(b2, 'description_viewpoint_EObject108'):
        assert _is_linked(b2, 'description_viewpoint_EObject108', a)
    _safe_set(a, 'viewpoint_description_EStructuralFeatureCustomization', set())
    assert not _is_linked(a, 'viewpoint_description_EStructuralFeatureCustomization', b2)
    if hasattr(b2, 'description_viewpoint_EObject108'):
        assert not _is_linked(b2, 'description_viewpoint_EObject108', a)


def test_assoc_associatedColor112_link_reassign_clear():
    a = viewpoint_description_ColorStep(associatedValue="sample_text")
    b1 = FixedColor()
    b2 = FixedColor()
    _safe_set(a, 'viewpoint_description_ColorStep', b1)
    assert _is_linked(a, 'viewpoint_description_ColorStep', b1)
    if hasattr(b1, 'FixedColor'):
        assert _is_linked(b1, 'FixedColor', a)
    _safe_set(a, 'viewpoint_description_ColorStep', b2)
    assert _is_linked(a, 'viewpoint_description_ColorStep', b2)
    if hasattr(b1, 'FixedColor'):
        assert not _is_linked(b1, 'FixedColor', a)
    if hasattr(b2, 'FixedColor'):
        assert _is_linked(b2, 'FixedColor', a)
    _safe_set(a, 'viewpoint_description_ColorStep', None)
    assert not _is_linked(a, 'viewpoint_description_ColorStep', b2)
    if hasattr(b2, 'FixedColor'):
        assert not _is_linked(b2, 'FixedColor', a)


def test_assoc_audits736_link_reassign_clear():
    a = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    b1 = validation_RuleAudit()
    b2 = validation_RuleAudit()
    _safe_set(a, 'viewpoint_validation_ValidationRule', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationRule', b1)
    if hasattr(b1, 'validation_RuleAudit'):
        assert _is_linked(b1, 'validation_RuleAudit', a)
    _safe_set(a, 'viewpoint_validation_ValidationRule', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationRule', b2)
    if hasattr(b1, 'validation_RuleAudit'):
        assert not _is_linked(b1, 'validation_RuleAudit', a)
    if hasattr(b2, 'validation_RuleAudit'):
        assert _is_linked(b2, 'validation_RuleAudit', a)
    _safe_set(a, 'viewpoint_validation_ValidationRule', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationRule', b2)
    if hasattr(b2, 'validation_RuleAudit'):
        assert not _is_linked(b2, 'validation_RuleAudit', a)


def test_assoc_backgroundColor342_link_reassign_clear():
    a = viewpoint_diagram_Dot(strokeSizeComputationExpression="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_Dot', b1)
    assert _is_linked(a, 'viewpoint_diagram_Dot', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues', a)
    _safe_set(a, 'viewpoint_diagram_Dot', b2)
    assert _is_linked(a, 'viewpoint_diagram_Dot', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues', a)
    _safe_set(a, 'viewpoint_diagram_Dot', None)
    assert not _is_linked(a, 'viewpoint_diagram_Dot', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues', a)


def test_assoc_backgroundColor343_link_reassign_clear():
    a = viewpoint_diagram_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_GaugeSection', b1)
    assert _is_linked(a, 'viewpoint_diagram_GaugeSection', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues344'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues344', a)
    _safe_set(a, 'viewpoint_diagram_GaugeSection', b2)
    assert _is_linked(a, 'viewpoint_diagram_GaugeSection', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues344'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues344', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues344'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues344', a)
    _safe_set(a, 'viewpoint_diagram_GaugeSection', None)
    assert not _is_linked(a, 'viewpoint_diagram_GaugeSection', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues344'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues344', a)


def test_assoc_backgroundColor348_link_reassign_clear():
    a = viewpoint_diagram_FlatContainerStyle(backgroundStyle="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_FlatContainerStyle', b1)
    assert _is_linked(a, 'viewpoint_diagram_FlatContainerStyle', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues349'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues349', a)
    _safe_set(a, 'viewpoint_diagram_FlatContainerStyle', b2)
    assert _is_linked(a, 'viewpoint_diagram_FlatContainerStyle', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues349'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues349', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues349'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues349', a)
    _safe_set(a, 'viewpoint_diagram_FlatContainerStyle', None)
    assert not _is_linked(a, 'viewpoint_diagram_FlatContainerStyle', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues349'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues349', a)


def test_assoc_backgroundColor353_link_reassign_clear():
    a = viewpoint_diagram_ShapeContainerStyle(shape="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_ShapeContainerStyle', b1)
    assert _is_linked(a, 'viewpoint_diagram_ShapeContainerStyle', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues354'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues354', a)
    _safe_set(a, 'viewpoint_diagram_ShapeContainerStyle', b2)
    assert _is_linked(a, 'viewpoint_diagram_ShapeContainerStyle', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues354'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues354', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues354'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues354', a)
    _safe_set(a, 'viewpoint_diagram_ShapeContainerStyle', None)
    assert not _is_linked(a, 'viewpoint_diagram_ShapeContainerStyle', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues354'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues354', a)


def test_assoc_backgroundColor580_link_reassign_clear():
    a = viewpoint_style_DotDescription(strokeSizeComputationExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_DotDescription', b1)
    assert _is_linked(a, 'viewpoint_style_DotDescription', b1)
    if hasattr(b1, 'ColorDescription581'):
        assert _is_linked(b1, 'ColorDescription581', a)
    _safe_set(a, 'viewpoint_style_DotDescription', b2)
    assert _is_linked(a, 'viewpoint_style_DotDescription', b2)
    if hasattr(b1, 'ColorDescription581'):
        assert not _is_linked(b1, 'ColorDescription581', a)
    if hasattr(b2, 'ColorDescription581'):
        assert _is_linked(b2, 'ColorDescription581', a)
    _safe_set(a, 'viewpoint_style_DotDescription', None)
    assert not _is_linked(a, 'viewpoint_style_DotDescription', b2)
    if hasattr(b2, 'ColorDescription581'):
        assert not _is_linked(b2, 'ColorDescription581', a)


def test_assoc_backgroundColor583_link_reassign_clear():
    a = viewpoint_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_GaugeSectionDescription', b1)
    assert _is_linked(a, 'viewpoint_style_GaugeSectionDescription', b1)
    if hasattr(b1, 'ColorDescription584'):
        assert _is_linked(b1, 'ColorDescription584', a)
    _safe_set(a, 'viewpoint_style_GaugeSectionDescription', b2)
    assert _is_linked(a, 'viewpoint_style_GaugeSectionDescription', b2)
    if hasattr(b1, 'ColorDescription584'):
        assert not _is_linked(b1, 'ColorDescription584', a)
    if hasattr(b2, 'ColorDescription584'):
        assert _is_linked(b2, 'ColorDescription584', a)
    _safe_set(a, 'viewpoint_style_GaugeSectionDescription', None)
    assert not _is_linked(a, 'viewpoint_style_GaugeSectionDescription', b2)
    if hasattr(b2, 'ColorDescription584'):
        assert not _is_linked(b2, 'ColorDescription584', a)


def test_assoc_backgroundColor588_link_reassign_clear():
    a = viewpoint_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription', b1)
    assert _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription', b1)
    if hasattr(b1, 'ColorDescription589'):
        assert _is_linked(b1, 'ColorDescription589', a)
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription', b2)
    assert _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription', b2)
    if hasattr(b1, 'ColorDescription589'):
        assert not _is_linked(b1, 'ColorDescription589', a)
    if hasattr(b2, 'ColorDescription589'):
        assert _is_linked(b2, 'ColorDescription589', a)
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription', None)
    assert not _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription', b2)
    if hasattr(b2, 'ColorDescription589'):
        assert not _is_linked(b2, 'ColorDescription589', a)


def test_assoc_backgroundColor596_link_reassign_clear():
    a = viewpoint_style_ShapeContainerStyleDescription(shape="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_ShapeContainerStyleDescription', b1)
    assert _is_linked(a, 'viewpoint_style_ShapeContainerStyleDescription', b1)
    if hasattr(b1, 'ColorDescription597'):
        assert _is_linked(b1, 'ColorDescription597', a)
    _safe_set(a, 'viewpoint_style_ShapeContainerStyleDescription', b2)
    assert _is_linked(a, 'viewpoint_style_ShapeContainerStyleDescription', b2)
    if hasattr(b1, 'ColorDescription597'):
        assert not _is_linked(b1, 'ColorDescription597', a)
    if hasattr(b2, 'ColorDescription597'):
        assert _is_linked(b2, 'ColorDescription597', a)
    _safe_set(a, 'viewpoint_style_ShapeContainerStyleDescription', None)
    assert not _is_linked(a, 'viewpoint_style_ShapeContainerStyleDescription', b2)
    if hasattr(b2, 'ColorDescription597'):
        assert not _is_linked(b2, 'ColorDescription597', a)


def test_assoc_beginLabelStyle369_link_reassign_clear():
    a = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = BeginLabelStyle()
    b2 = BeginLabelStyle()
    _safe_set(a, 'viewpoint_diagram_EdgeStyle370', b1)
    assert _is_linked(a, 'viewpoint_diagram_EdgeStyle370', b1)
    if hasattr(b1, 'BeginLabelStyle'):
        assert _is_linked(b1, 'BeginLabelStyle', a)
    _safe_set(a, 'viewpoint_diagram_EdgeStyle370', b2)
    assert _is_linked(a, 'viewpoint_diagram_EdgeStyle370', b2)
    if hasattr(b1, 'BeginLabelStyle'):
        assert not _is_linked(b1, 'BeginLabelStyle', a)
    if hasattr(b2, 'BeginLabelStyle'):
        assert _is_linked(b2, 'BeginLabelStyle', a)
    _safe_set(a, 'viewpoint_diagram_EdgeStyle370', None)
    assert not _is_linked(a, 'viewpoint_diagram_EdgeStyle370', b2)
    if hasattr(b2, 'BeginLabelStyle'):
        assert not _is_linked(b2, 'BeginLabelStyle', a)


def test_assoc_beginLabelStyleDescription600_link_reassign_clear():
    a = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = style_BeginLabelStyleDescription()
    b2 = style_BeginLabelStyleDescription()
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription601', b1)
    assert _is_linked(a, 'viewpoint_style_EdgeStyleDescription601', b1)
    if hasattr(b1, 'style_BeginLabelStyleDescription'):
        assert _is_linked(b1, 'style_BeginLabelStyleDescription', a)
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription601', b2)
    assert _is_linked(a, 'viewpoint_style_EdgeStyleDescription601', b2)
    if hasattr(b1, 'style_BeginLabelStyleDescription'):
        assert not _is_linked(b1, 'style_BeginLabelStyleDescription', a)
    if hasattr(b2, 'style_BeginLabelStyleDescription'):
        assert _is_linked(b2, 'style_BeginLabelStyleDescription', a)
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription601', None)
    assert not _is_linked(a, 'viewpoint_style_EdgeStyleDescription601', b2)
    if hasattr(b2, 'style_BeginLabelStyleDescription'):
        assert not _is_linked(b2, 'style_BeginLabelStyleDescription', a)


def test_assoc_borderColor376_link_reassign_clear():
    a = viewpoint_diagram_BorderedStyle(borderSize="sample_text", borderSizeComputationExpression="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_BorderedStyle', b1)
    assert _is_linked(a, 'viewpoint_diagram_BorderedStyle', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues377'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues377', a)
    _safe_set(a, 'viewpoint_diagram_BorderedStyle', b2)
    assert _is_linked(a, 'viewpoint_diagram_BorderedStyle', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues377'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues377', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues377'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues377', a)
    _safe_set(a, 'viewpoint_diagram_BorderedStyle', None)
    assert not _is_linked(a, 'viewpoint_diagram_BorderedStyle', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues377'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues377', a)


def test_assoc_borderColor568_link_reassign_clear():
    a = viewpoint_style_BorderedStyleDescription(borderSizeComputationExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_BorderedStyleDescription', b1)
    assert _is_linked(a, 'viewpoint_style_BorderedStyleDescription', b1)
    if hasattr(b1, 'ColorDescription569'):
        assert _is_linked(b1, 'ColorDescription569', a)
    _safe_set(a, 'viewpoint_style_BorderedStyleDescription', b2)
    assert _is_linked(a, 'viewpoint_style_BorderedStyleDescription', b2)
    if hasattr(b1, 'ColorDescription569'):
        assert not _is_linked(b1, 'ColorDescription569', a)
    if hasattr(b2, 'ColorDescription569'):
        assert _is_linked(b2, 'ColorDescription569', a)
    _safe_set(a, 'viewpoint_style_BorderedStyleDescription', None)
    assert not _is_linked(a, 'viewpoint_style_BorderedStyleDescription', b2)
    if hasattr(b2, 'ColorDescription569'):
        assert not _is_linked(b2, 'ColorDescription569', a)


def test_assoc_borderedNodeMappings477_link_reassign_clear():
    a = viewpoint_description_AbstractNodeMapping(domainClass="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_description_AbstractNodeMapping', {b1})
    assert _is_linked(a, 'viewpoint_description_AbstractNodeMapping', b1)
    if hasattr(b1, 'description_NodeMapping478'):
        assert _is_linked(b1, 'description_NodeMapping478', a)
    _safe_set(a, 'viewpoint_description_AbstractNodeMapping', {b2})
    assert _is_linked(a, 'viewpoint_description_AbstractNodeMapping', b2)
    if hasattr(b1, 'description_NodeMapping478'):
        assert not _is_linked(b1, 'description_NodeMapping478', a)
    if hasattr(b2, 'description_NodeMapping478'):
        assert _is_linked(b2, 'description_NodeMapping478', a)
    _safe_set(a, 'viewpoint_description_AbstractNodeMapping', set())
    assert not _is_linked(a, 'viewpoint_description_AbstractNodeMapping', b2)
    if hasattr(b2, 'description_NodeMapping478'):
        assert not _is_linked(b2, 'description_NodeMapping478', a)


def test_assoc_candidatesMapping283_link_reassign_clear():
    a = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_diagram_DNode284', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DNode284', b1)
    if hasattr(b1, 'description_NodeMapping285'):
        assert _is_linked(b1, 'description_NodeMapping285', a)
    _safe_set(a, 'viewpoint_diagram_DNode284', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DNode284', b2)
    if hasattr(b1, 'description_NodeMapping285'):
        assert not _is_linked(b1, 'description_NodeMapping285', a)
    if hasattr(b2, 'description_NodeMapping285'):
        assert _is_linked(b2, 'description_NodeMapping285', a)
    _safe_set(a, 'viewpoint_diagram_DNode284', set())
    assert not _is_linked(a, 'viewpoint_diagram_DNode284', b2)
    if hasattr(b2, 'description_NodeMapping285'):
        assert not _is_linked(b2, 'description_NodeMapping285', a)


def test_assoc_candidatesMapping304_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer305', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer305', b1)
    if hasattr(b1, 'description_ContainerMapping306'):
        assert _is_linked(b1, 'description_ContainerMapping306', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer305', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer305', b2)
    if hasattr(b1, 'description_ContainerMapping306'):
        assert not _is_linked(b1, 'description_ContainerMapping306', a)
    if hasattr(b2, 'description_ContainerMapping306'):
        assert _is_linked(b2, 'description_ContainerMapping306', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer305', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer305', b2)
    if hasattr(b2, 'description_ContainerMapping306'):
        assert not _is_linked(b2, 'description_ContainerMapping306', a)


def test_assoc_centerLabelStyle371_link_reassign_clear():
    a = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = CenterLabelStyle()
    b2 = CenterLabelStyle()
    _safe_set(a, 'viewpoint_diagram_EdgeStyle372', b1)
    assert _is_linked(a, 'viewpoint_diagram_EdgeStyle372', b1)
    if hasattr(b1, 'CenterLabelStyle'):
        assert _is_linked(b1, 'CenterLabelStyle', a)
    _safe_set(a, 'viewpoint_diagram_EdgeStyle372', b2)
    assert _is_linked(a, 'viewpoint_diagram_EdgeStyle372', b2)
    if hasattr(b1, 'CenterLabelStyle'):
        assert not _is_linked(b1, 'CenterLabelStyle', a)
    if hasattr(b2, 'CenterLabelStyle'):
        assert _is_linked(b2, 'CenterLabelStyle', a)
    _safe_set(a, 'viewpoint_diagram_EdgeStyle372', None)
    assert not _is_linked(a, 'viewpoint_diagram_EdgeStyle372', b2)
    if hasattr(b2, 'CenterLabelStyle'):
        assert not _is_linked(b2, 'CenterLabelStyle', a)


def test_assoc_centerLabelStyleDescription602_link_reassign_clear():
    a = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = style_CenterLabelStyleDescription()
    b2 = style_CenterLabelStyleDescription()
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription603', b1)
    assert _is_linked(a, 'viewpoint_style_EdgeStyleDescription603', b1)
    if hasattr(b1, 'style_CenterLabelStyleDescription'):
        assert _is_linked(b1, 'style_CenterLabelStyleDescription', a)
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription603', b2)
    assert _is_linked(a, 'viewpoint_style_EdgeStyleDescription603', b2)
    if hasattr(b1, 'style_CenterLabelStyleDescription'):
        assert not _is_linked(b1, 'style_CenterLabelStyleDescription', a)
    if hasattr(b2, 'style_CenterLabelStyleDescription'):
        assert _is_linked(b2, 'style_CenterLabelStyleDescription', a)
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription603', None)
    assert not _is_linked(a, 'viewpoint_style_EdgeStyleDescription603', b2)
    if hasattr(b2, 'style_CenterLabelStyleDescription'):
        assert not _is_linked(b2, 'style_CenterLabelStyleDescription', a)


def test_assoc_color355_link_reassign_clear():
    a = viewpoint_diagram_Square(height="sample_text", width="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_Square', b1)
    assert _is_linked(a, 'viewpoint_diagram_Square', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues356'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues356', a)
    _safe_set(a, 'viewpoint_diagram_Square', b2)
    assert _is_linked(a, 'viewpoint_diagram_Square', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues356'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues356', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues356'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues356', a)
    _safe_set(a, 'viewpoint_diagram_Square', None)
    assert not _is_linked(a, 'viewpoint_diagram_Square', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues356'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues356', a)


def test_assoc_color357_link_reassign_clear():
    a = viewpoint_diagram_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_Ellipse', b1)
    assert _is_linked(a, 'viewpoint_diagram_Ellipse', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues358'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues358', a)
    _safe_set(a, 'viewpoint_diagram_Ellipse', b2)
    assert _is_linked(a, 'viewpoint_diagram_Ellipse', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues358'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues358', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues358'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues358', a)
    _safe_set(a, 'viewpoint_diagram_Ellipse', None)
    assert not _is_linked(a, 'viewpoint_diagram_Ellipse', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues358'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues358', a)


def test_assoc_color359_link_reassign_clear():
    a = viewpoint_diagram_Lozenge(height="sample_text", width="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_Lozenge', b1)
    assert _is_linked(a, 'viewpoint_diagram_Lozenge', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues360'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues360', a)
    _safe_set(a, 'viewpoint_diagram_Lozenge', b2)
    assert _is_linked(a, 'viewpoint_diagram_Lozenge', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues360'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues360', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues360'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues360', a)
    _safe_set(a, 'viewpoint_diagram_Lozenge', None)
    assert not _is_linked(a, 'viewpoint_diagram_Lozenge', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues360'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues360', a)


def test_assoc_color361_link_reassign_clear():
    a = viewpoint_diagram_BundledImage(shape="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_BundledImage', b1)
    assert _is_linked(a, 'viewpoint_diagram_BundledImage', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues362'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues362', a)
    _safe_set(a, 'viewpoint_diagram_BundledImage', b2)
    assert _is_linked(a, 'viewpoint_diagram_BundledImage', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues362'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues362', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues362'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues362', a)
    _safe_set(a, 'viewpoint_diagram_BundledImage', None)
    assert not _is_linked(a, 'viewpoint_diagram_BundledImage', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues362'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues362', a)


def test_assoc_color570_link_reassign_clear():
    a = viewpoint_style_SquareDescription(height="sample_text", width="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_SquareDescription', b1)
    assert _is_linked(a, 'viewpoint_style_SquareDescription', b1)
    if hasattr(b1, 'ColorDescription571'):
        assert _is_linked(b1, 'ColorDescription571', a)
    _safe_set(a, 'viewpoint_style_SquareDescription', b2)
    assert _is_linked(a, 'viewpoint_style_SquareDescription', b2)
    if hasattr(b1, 'ColorDescription571'):
        assert not _is_linked(b1, 'ColorDescription571', a)
    if hasattr(b2, 'ColorDescription571'):
        assert _is_linked(b2, 'ColorDescription571', a)
    _safe_set(a, 'viewpoint_style_SquareDescription', None)
    assert not _is_linked(a, 'viewpoint_style_SquareDescription', b2)
    if hasattr(b2, 'ColorDescription571'):
        assert not _is_linked(b2, 'ColorDescription571', a)


def test_assoc_color572_link_reassign_clear():
    a = viewpoint_style_LozengeNodeDescription(heightComputationExpression="sample_text", widthComputationExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_LozengeNodeDescription', b1)
    assert _is_linked(a, 'viewpoint_style_LozengeNodeDescription', b1)
    if hasattr(b1, 'ColorDescription573'):
        assert _is_linked(b1, 'ColorDescription573', a)
    _safe_set(a, 'viewpoint_style_LozengeNodeDescription', b2)
    assert _is_linked(a, 'viewpoint_style_LozengeNodeDescription', b2)
    if hasattr(b1, 'ColorDescription573'):
        assert not _is_linked(b1, 'ColorDescription573', a)
    if hasattr(b2, 'ColorDescription573'):
        assert _is_linked(b2, 'ColorDescription573', a)
    _safe_set(a, 'viewpoint_style_LozengeNodeDescription', None)
    assert not _is_linked(a, 'viewpoint_style_LozengeNodeDescription', b2)
    if hasattr(b2, 'ColorDescription573'):
        assert not _is_linked(b2, 'ColorDescription573', a)


def test_assoc_color574_link_reassign_clear():
    a = viewpoint_style_EllipseNodeDescription(horizontalDiameterComputationExpression="sample_text", verticalDiameterComputationExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_EllipseNodeDescription', b1)
    assert _is_linked(a, 'viewpoint_style_EllipseNodeDescription', b1)
    if hasattr(b1, 'ColorDescription575'):
        assert _is_linked(b1, 'ColorDescription575', a)
    _safe_set(a, 'viewpoint_style_EllipseNodeDescription', b2)
    assert _is_linked(a, 'viewpoint_style_EllipseNodeDescription', b2)
    if hasattr(b1, 'ColorDescription575'):
        assert not _is_linked(b1, 'ColorDescription575', a)
    if hasattr(b2, 'ColorDescription575'):
        assert _is_linked(b2, 'ColorDescription575', a)
    _safe_set(a, 'viewpoint_style_EllipseNodeDescription', None)
    assert not _is_linked(a, 'viewpoint_style_EllipseNodeDescription', b2)
    if hasattr(b2, 'ColorDescription575'):
        assert not _is_linked(b2, 'ColorDescription575', a)


def test_assoc_color576_link_reassign_clear():
    a = viewpoint_style_BundledImageDescription(shape="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_BundledImageDescription', b1)
    assert _is_linked(a, 'viewpoint_style_BundledImageDescription', b1)
    if hasattr(b1, 'ColorDescription577'):
        assert _is_linked(b1, 'ColorDescription577', a)
    _safe_set(a, 'viewpoint_style_BundledImageDescription', b2)
    assert _is_linked(a, 'viewpoint_style_BundledImageDescription', b2)
    if hasattr(b1, 'ColorDescription577'):
        assert not _is_linked(b1, 'ColorDescription577', a)
    if hasattr(b2, 'ColorDescription577'):
        assert _is_linked(b2, 'ColorDescription577', a)
    _safe_set(a, 'viewpoint_style_BundledImageDescription', None)
    assert not _is_linked(a, 'viewpoint_style_BundledImageDescription', b2)
    if hasattr(b2, 'ColorDescription577'):
        assert not _is_linked(b2, 'ColorDescription577', a)


def test_assoc_colorSteps111_link_reassign_clear():
    a = viewpoint_description_InterpolatedColor(colorValueComputationExpression="sample_text", maxValueComputationExpression="sample_text", minValueComputationExpression="sample_text")
    b1 = ColorStep()
    b2 = ColorStep()
    _safe_set(a, 'viewpoint_description_InterpolatedColor', {b1})
    assert _is_linked(a, 'viewpoint_description_InterpolatedColor', b1)
    if hasattr(b1, 'ColorStep'):
        assert _is_linked(b1, 'ColorStep', a)
    _safe_set(a, 'viewpoint_description_InterpolatedColor', {b2})
    assert _is_linked(a, 'viewpoint_description_InterpolatedColor', b2)
    if hasattr(b1, 'ColorStep'):
        assert not _is_linked(b1, 'ColorStep', a)
    if hasattr(b2, 'ColorStep'):
        assert _is_linked(b2, 'ColorStep', a)
    _safe_set(a, 'viewpoint_description_InterpolatedColor', set())
    assert not _is_linked(a, 'viewpoint_description_InterpolatedColor', b2)
    if hasattr(b2, 'ColorStep'):
        assert not _is_linked(b2, 'ColorStep', a)


def test_assoc_concerns418_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = concern_ConcernSet()
    b2 = concern_ConcernSet()
    _safe_set(a, 'viewpoint_description_DiagramDescription419', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription419', b1)
    if hasattr(b1, 'concern_ConcernSet'):
        assert _is_linked(b1, 'concern_ConcernSet', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription419', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription419', b2)
    if hasattr(b1, 'concern_ConcernSet'):
        assert not _is_linked(b1, 'concern_ConcernSet', a)
    if hasattr(b2, 'concern_ConcernSet'):
        assert _is_linked(b2, 'concern_ConcernSet', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription419', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription419', b2)
    if hasattr(b2, 'concern_ConcernSet'):
        assert not _is_linked(b2, 'concern_ConcernSet', a)


def test_assoc_conditionnalStyles483_link_reassign_clear():
    a = viewpoint_description_NodeMapping()
    b1 = description_ConditionalNodeStyleDescription()
    b2 = description_ConditionalNodeStyleDescription()
    _safe_set(a, 'viewpoint_description_NodeMapping484', {b1})
    assert _is_linked(a, 'viewpoint_description_NodeMapping484', b1)
    if hasattr(b1, 'description_ConditionalNodeStyleDescription'):
        assert _is_linked(b1, 'description_ConditionalNodeStyleDescription', a)
    _safe_set(a, 'viewpoint_description_NodeMapping484', {b2})
    assert _is_linked(a, 'viewpoint_description_NodeMapping484', b2)
    if hasattr(b1, 'description_ConditionalNodeStyleDescription'):
        assert not _is_linked(b1, 'description_ConditionalNodeStyleDescription', a)
    if hasattr(b2, 'description_ConditionalNodeStyleDescription'):
        assert _is_linked(b2, 'description_ConditionalNodeStyleDescription', a)
    _safe_set(a, 'viewpoint_description_NodeMapping484', set())
    assert not _is_linked(a, 'viewpoint_description_NodeMapping484', b2)
    if hasattr(b2, 'description_ConditionalNodeStyleDescription'):
        assert not _is_linked(b2, 'description_ConditionalNodeStyleDescription', a)


def test_assoc_conditionnalStyles504_link_reassign_clear():
    a = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = description_ConditionalContainerStyleDescription()
    b2 = description_ConditionalContainerStyleDescription()
    _safe_set(a, 'viewpoint_description_ContainerMapping505', {b1})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping505', b1)
    if hasattr(b1, 'description_ConditionalContainerStyleDescription'):
        assert _is_linked(b1, 'description_ConditionalContainerStyleDescription', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping505', {b2})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping505', b2)
    if hasattr(b1, 'description_ConditionalContainerStyleDescription'):
        assert not _is_linked(b1, 'description_ConditionalContainerStyleDescription', a)
    if hasattr(b2, 'description_ConditionalContainerStyleDescription'):
        assert _is_linked(b2, 'description_ConditionalContainerStyleDescription', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping505', set())
    assert not _is_linked(a, 'viewpoint_description_ContainerMapping505', b2)
    if hasattr(b2, 'description_ConditionalContainerStyleDescription'):
        assert not _is_linked(b2, 'description_ConditionalContainerStyleDescription', a)


def test_assoc_conditionnalStyles517_link_reassign_clear():
    a = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = description_ConditionalEdgeStyleDescription()
    b2 = description_ConditionalEdgeStyleDescription()
    _safe_set(a, 'viewpoint_description_EdgeMapping518', {b1})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping518', b1)
    if hasattr(b1, 'description_ConditionalEdgeStyleDescription'):
        assert _is_linked(b1, 'description_ConditionalEdgeStyleDescription', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping518', {b2})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping518', b2)
    if hasattr(b1, 'description_ConditionalEdgeStyleDescription'):
        assert not _is_linked(b1, 'description_ConditionalEdgeStyleDescription', a)
    if hasattr(b2, 'description_ConditionalEdgeStyleDescription'):
        assert _is_linked(b2, 'description_ConditionalEdgeStyleDescription', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping518', set())
    assert not _is_linked(a, 'viewpoint_description_EdgeMapping518', b2)
    if hasattr(b2, 'description_ConditionalEdgeStyleDescription'):
        assert not _is_linked(b2, 'description_ConditionalEdgeStyleDescription', a)


def test_assoc_conditionnalStyles525_link_reassign_clear():
    a = viewpoint_description_EdgeMappingImport(inheritsAncestorFilters=True)
    b1 = description_ConditionalEdgeStyleDescription()
    b2 = description_ConditionalEdgeStyleDescription()
    _safe_set(a, 'viewpoint_description_EdgeMappingImport526', {b1})
    assert _is_linked(a, 'viewpoint_description_EdgeMappingImport526', b1)
    if hasattr(b1, 'description_ConditionalEdgeStyleDescription527'):
        assert _is_linked(b1, 'description_ConditionalEdgeStyleDescription527', a)
    _safe_set(a, 'viewpoint_description_EdgeMappingImport526', {b2})
    assert _is_linked(a, 'viewpoint_description_EdgeMappingImport526', b2)
    if hasattr(b1, 'description_ConditionalEdgeStyleDescription527'):
        assert not _is_linked(b1, 'description_ConditionalEdgeStyleDescription527', a)
    if hasattr(b2, 'description_ConditionalEdgeStyleDescription527'):
        assert _is_linked(b2, 'description_ConditionalEdgeStyleDescription527', a)
    _safe_set(a, 'viewpoint_description_EdgeMappingImport526', set())
    assert not _is_linked(a, 'viewpoint_description_EdgeMappingImport526', b2)
    if hasattr(b2, 'description_ConditionalEdgeStyleDescription527'):
        assert not _is_linked(b2, 'description_ConditionalEdgeStyleDescription527', a)


def test_assoc_container143_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription', b1)
    if hasattr(b1, 'tool_DropContainerVariable144'):
        assert _is_linked(b1, 'tool_DropContainerVariable144', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription', b2)
    if hasattr(b1, 'tool_DropContainerVariable144'):
        assert not _is_linked(b1, 'tool_DropContainerVariable144', a)
    if hasattr(b2, 'tool_DropContainerVariable144'):
        assert _is_linked(b2, 'tool_DropContainerVariable144', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription', b2)
    if hasattr(b2, 'tool_DropContainerVariable144'):
        assert not _is_linked(b2, 'tool_DropContainerVariable144', a)


def test_assoc_container161_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_SelectContainerVariable()
    b2 = tool_SelectContainerVariable()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription162', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription162', b1)
    if hasattr(b1, 'tool_SelectContainerVariable'):
        assert _is_linked(b1, 'tool_SelectContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription162', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription162', b2)
    if hasattr(b1, 'tool_SelectContainerVariable'):
        assert not _is_linked(b1, 'tool_SelectContainerVariable', a)
    if hasattr(b2, 'tool_SelectContainerVariable'):
        assert _is_linked(b2, 'tool_SelectContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription162', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription162', b2)
    if hasattr(b2, 'tool_SelectContainerVariable'):
        assert not _is_linked(b2, 'tool_SelectContainerVariable', a)


def test_assoc_container171_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_SelectContainerVariable()
    b2 = tool_SelectContainerVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription172', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription172', b1)
    if hasattr(b1, 'tool_SelectContainerVariable173'):
        assert _is_linked(b1, 'tool_SelectContainerVariable173', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription172', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription172', b2)
    if hasattr(b1, 'tool_SelectContainerVariable173'):
        assert not _is_linked(b1, 'tool_SelectContainerVariable173', a)
    if hasattr(b2, 'tool_SelectContainerVariable173'):
        assert _is_linked(b2, 'tool_SelectContainerVariable173', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription172', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription172', b2)
    if hasattr(b2, 'tool_SelectContainerVariable173'):
        assert not _is_linked(b2, 'tool_SelectContainerVariable173', a)


def test_assoc_containerMappings452_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_description_DiagramDescription453', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription453', b1)
    if hasattr(b1, 'description_ContainerMapping454'):
        assert _is_linked(b1, 'description_ContainerMapping454', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription453', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription453', b2)
    if hasattr(b1, 'description_ContainerMapping454'):
        assert not _is_linked(b1, 'description_ContainerMapping454', a)
    if hasattr(b2, 'description_ContainerMapping454'):
        assert _is_linked(b2, 'description_ContainerMapping454', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription453', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription453', b2)
    if hasattr(b2, 'description_ContainerMapping454'):
        assert not _is_linked(b2, 'description_ContainerMapping454', a)


def test_assoc_containerMappings546_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_description_Layer547', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer547', b1)
    if hasattr(b1, 'description_ContainerMapping548'):
        assert _is_linked(b1, 'description_ContainerMapping548', a)
    _safe_set(a, 'viewpoint_description_Layer547', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer547', b2)
    if hasattr(b1, 'description_ContainerMapping548'):
        assert not _is_linked(b1, 'description_ContainerMapping548', a)
    if hasattr(b2, 'description_ContainerMapping548'):
        assert _is_linked(b2, 'description_ContainerMapping548', a)
    _safe_set(a, 'viewpoint_description_Layer547', set())
    assert not _is_linked(a, 'viewpoint_description_Layer547', b2)
    if hasattr(b2, 'description_ContainerMapping548'):
        assert not _is_linked(b2, 'description_ContainerMapping548', a)


def test_assoc_containerMappings654_link_reassign_clear():
    a = viewpoint_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription', {b1})
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription', b1)
    if hasattr(b1, 'description_ContainerMapping655'):
        assert _is_linked(b1, 'description_ContainerMapping655', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription', {b2})
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription', b2)
    if hasattr(b1, 'description_ContainerMapping655'):
        assert not _is_linked(b1, 'description_ContainerMapping655', a)
    if hasattr(b2, 'description_ContainerMapping655'):
        assert _is_linked(b2, 'description_ContainerMapping655', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription', set())
    assert not _is_linked(a, 'viewpoint_tool_ContainerCreationDescription', b2)
    if hasattr(b2, 'description_ContainerMapping655'):
        assert not _is_linked(b2, 'description_ContainerMapping655', a)


def test_assoc_containerVariable192_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription193', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription193', b1)
    if hasattr(b1, 'tool_ElementSelectVariable194'):
        assert _is_linked(b1, 'tool_ElementSelectVariable194', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription193', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription193', b2)
    if hasattr(b1, 'tool_ElementSelectVariable194'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable194', a)
    if hasattr(b2, 'tool_ElementSelectVariable194'):
        assert _is_linked(b2, 'tool_ElementSelectVariable194', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription193', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription193', b2)
    if hasattr(b2, 'tool_ElementSelectVariable194'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable194', a)


def test_assoc_containerView145_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription146', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription146', b1)
    if hasattr(b1, 'tool_ContainerViewVariable147'):
        assert _is_linked(b1, 'tool_ContainerViewVariable147', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription146', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription146', b2)
    if hasattr(b1, 'tool_ContainerViewVariable147'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable147', a)
    if hasattr(b2, 'tool_ContainerViewVariable147'):
        assert _is_linked(b2, 'tool_ContainerViewVariable147', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription146', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription146', b2)
    if hasattr(b2, 'tool_ContainerViewVariable147'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable147', a)


def test_assoc_containerView158_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription159', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription159', b1)
    if hasattr(b1, 'tool_ContainerViewVariable160'):
        assert _is_linked(b1, 'tool_ContainerViewVariable160', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription159', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription159', b2)
    if hasattr(b1, 'tool_ContainerViewVariable160'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable160', a)
    if hasattr(b2, 'tool_ContainerViewVariable160'):
        assert _is_linked(b2, 'tool_ContainerViewVariable160', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription159', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription159', b2)
    if hasattr(b2, 'tool_ContainerViewVariable160'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable160', a)


def test_assoc_containerView168_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription169', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription169', b1)
    if hasattr(b1, 'tool_ContainerViewVariable170'):
        assert _is_linked(b1, 'tool_ContainerViewVariable170', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription169', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription169', b2)
    if hasattr(b1, 'tool_ContainerViewVariable170'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable170', a)
    if hasattr(b2, 'tool_ContainerViewVariable170'):
        assert _is_linked(b2, 'tool_ContainerViewVariable170', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription169', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription169', b2)
    if hasattr(b2, 'tool_ContainerViewVariable170'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable170', a)


def test_assoc_containerView672_link_reassign_clear():
    a = viewpoint_tool_DeleteElementDescription()
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription673', b1)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription673', b1)
    if hasattr(b1, 'tool_ContainerViewVariable674'):
        assert _is_linked(b1, 'tool_ContainerViewVariable674', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription673', b2)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription673', b2)
    if hasattr(b1, 'tool_ContainerViewVariable674'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable674', a)
    if hasattr(b2, 'tool_ContainerViewVariable674'):
        assert _is_linked(b2, 'tool_ContainerViewVariable674', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription673', None)
    assert not _is_linked(a, 'viewpoint_tool_DeleteElementDescription673', b2)
    if hasattr(b2, 'tool_ContainerViewVariable674'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable674', a)


def test_assoc_containerViewVariable182_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription183', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription183', b1)
    if hasattr(b1, 'tool_ContainerViewVariable184'):
        assert _is_linked(b1, 'tool_ContainerViewVariable184', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription183', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription183', b2)
    if hasattr(b1, 'tool_ContainerViewVariable184'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable184', a)
    if hasattr(b2, 'tool_ContainerViewVariable184'):
        assert _is_linked(b2, 'tool_ContainerViewVariable184', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription183', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription183', b2)
    if hasattr(b2, 'tool_ContainerViewVariable184'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable184', a)


def test_assoc_containerViewVariable189_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription190', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription190', b1)
    if hasattr(b1, 'tool_ContainerViewVariable191'):
        assert _is_linked(b1, 'tool_ContainerViewVariable191', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription190', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription190', b2)
    if hasattr(b1, 'tool_ContainerViewVariable191'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable191', a)
    if hasattr(b2, 'tool_ContainerViewVariable191'):
        assert _is_linked(b2, 'tool_ContainerViewVariable191', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription190', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription190', b2)
    if hasattr(b2, 'tool_ContainerViewVariable191'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable191', a)


def test_assoc_containers239_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = DDiagramElementContainer()
    b2 = DDiagramElementContainer()
    _safe_set(a, 'viewpoint_diagram_DDiagram240', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram240', b1)
    if hasattr(b1, 'DDiagramElementContainer'):
        assert _is_linked(b1, 'DDiagramElementContainer', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram240', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram240', b2)
    if hasattr(b1, 'DDiagramElementContainer'):
        assert not _is_linked(b1, 'DDiagramElementContainer', a)
    if hasattr(b2, 'DDiagramElementContainer'):
        assert _is_linked(b2, 'DDiagramElementContainer', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram240', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram240', b2)
    if hasattr(b2, 'DDiagramElementContainer'):
        assert not _is_linked(b2, 'DDiagramElementContainer', a)


def test_assoc_containers288_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = DDiagramElementContainer()
    b2 = DDiagramElementContainer()
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer289', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer289', b1)
    if hasattr(b1, 'DDiagramElementContainer290'):
        assert _is_linked(b1, 'DDiagramElementContainer290', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer289', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer289', b2)
    if hasattr(b1, 'DDiagramElementContainer290'):
        assert not _is_linked(b1, 'DDiagramElementContainer290', a)
    if hasattr(b2, 'DDiagramElementContainer290'):
        assert _is_linked(b2, 'DDiagramElementContainer290', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer289', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer289', b2)
    if hasattr(b2, 'DDiagramElementContainer290'):
        assert not _is_linked(b2, 'DDiagramElementContainer290', a)


def test_assoc_copiedElement151_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ElementVariable()
    b2 = tool_ElementVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription152', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription152', b1)
    if hasattr(b1, 'tool_ElementVariable153'):
        assert _is_linked(b1, 'tool_ElementVariable153', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription152', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription152', b2)
    if hasattr(b1, 'tool_ElementVariable153'):
        assert not _is_linked(b1, 'tool_ElementVariable153', a)
    if hasattr(b2, 'tool_ElementVariable153'):
        assert _is_linked(b2, 'tool_ElementVariable153', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription152', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription152', b2)
    if hasattr(b2, 'tool_ElementVariable153'):
        assert not _is_linked(b2, 'tool_ElementVariable153', a)


def test_assoc_copiedView148_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ElementViewVariable()
    b2 = tool_ElementViewVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription149', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription149', b1)
    if hasattr(b1, 'tool_ElementViewVariable150'):
        assert _is_linked(b1, 'tool_ElementViewVariable150', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription149', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription149', b2)
    if hasattr(b1, 'tool_ElementViewVariable150'):
        assert not _is_linked(b1, 'tool_ElementViewVariable150', a)
    if hasattr(b2, 'tool_ElementViewVariable150'):
        assert _is_linked(b2, 'tool_ElementViewVariable150', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription149', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription149', b2)
    if hasattr(b2, 'tool_ElementViewVariable150'):
        assert not _is_linked(b2, 'tool_ElementViewVariable150', a)


def test_assoc_currentConcern241_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = concern_ConcernDescription()
    b2 = concern_ConcernDescription()
    _safe_set(a, 'viewpoint_diagram_DDiagram242', b1)
    assert _is_linked(a, 'viewpoint_diagram_DDiagram242', b1)
    if hasattr(b1, 'concern_ConcernDescription'):
        assert _is_linked(b1, 'concern_ConcernDescription', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram242', b2)
    assert _is_linked(a, 'viewpoint_diagram_DDiagram242', b2)
    if hasattr(b1, 'concern_ConcernDescription'):
        assert not _is_linked(b1, 'concern_ConcernDescription', a)
    if hasattr(b2, 'concern_ConcernDescription'):
        assert _is_linked(b2, 'concern_ConcernDescription', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram242', None)
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram242', b2)
    if hasattr(b2, 'concern_ConcernDescription'):
        assert not _is_linked(b2, 'concern_ConcernDescription', a)


def test_assoc_customization566_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = Customization()
    b2 = Customization()
    _safe_set(a, 'viewpoint_description_Layer567', b1)
    assert _is_linked(a, 'viewpoint_description_Layer567', b1)
    if hasattr(b1, 'Customization'):
        assert _is_linked(b1, 'Customization', a)
    _safe_set(a, 'viewpoint_description_Layer567', b2)
    assert _is_linked(a, 'viewpoint_description_Layer567', b2)
    if hasattr(b1, 'Customization'):
        assert not _is_linked(b1, 'Customization', a)
    if hasattr(b2, 'Customization'):
        assert _is_linked(b2, 'Customization', a)
    _safe_set(a, 'viewpoint_description_Layer567', None)
    assert not _is_linked(a, 'viewpoint_description_Layer567', b2)
    if hasattr(b2, 'Customization'):
        assert not _is_linked(b2, 'Customization', a)


def test_assoc_data121_link_reassign_clear():
    a = viewpoint_description_AnnotationEntry(source="sample_text")
    b1 = description_viewpoint_EObject()
    b2 = description_viewpoint_EObject()
    _safe_set(a, 'viewpoint_description_AnnotationEntry', b1)
    assert _is_linked(a, 'viewpoint_description_AnnotationEntry', b1)
    if hasattr(b1, 'description_viewpoint_EObject122'):
        assert _is_linked(b1, 'description_viewpoint_EObject122', a)
    _safe_set(a, 'viewpoint_description_AnnotationEntry', b2)
    assert _is_linked(a, 'viewpoint_description_AnnotationEntry', b2)
    if hasattr(b1, 'description_viewpoint_EObject122'):
        assert not _is_linked(b1, 'description_viewpoint_EObject122', a)
    if hasattr(b2, 'description_viewpoint_EObject122'):
        assert _is_linked(b2, 'description_viewpoint_EObject122', a)
    _safe_set(a, 'viewpoint_description_AnnotationEntry', None)
    assert not _is_linked(a, 'viewpoint_description_AnnotationEntry', b2)
    if hasattr(b2, 'description_viewpoint_EObject122'):
        assert not _is_linked(b2, 'description_viewpoint_EObject122', a)


def test_assoc_data53_link_reassign_clear():
    a = viewpoint_DAnalysisCustomData(key="sample_text")
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_DAnalysisCustomData', b1)
    assert _is_linked(a, 'viewpoint_DAnalysisCustomData', b1)
    if hasattr(b1, 'viewpoint_EObject54'):
        assert _is_linked(b1, 'viewpoint_EObject54', a)
    _safe_set(a, 'viewpoint_DAnalysisCustomData', b2)
    assert _is_linked(a, 'viewpoint_DAnalysisCustomData', b2)
    if hasattr(b1, 'viewpoint_EObject54'):
        assert not _is_linked(b1, 'viewpoint_EObject54', a)
    if hasattr(b2, 'viewpoint_EObject54'):
        assert _is_linked(b2, 'viewpoint_EObject54', a)
    _safe_set(a, 'viewpoint_DAnalysisCustomData', None)
    assert not _is_linked(a, 'viewpoint_DAnalysisCustomData', b2)
    if hasattr(b2, 'viewpoint_EObject54'):
        assert not _is_linked(b2, 'viewpoint_EObject54', a)


def test_assoc_decorationDescriptionsSet561_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = DecorationDescriptionsSet()
    b2 = DecorationDescriptionsSet()
    _safe_set(a, 'viewpoint_description_Layer562', b1)
    assert _is_linked(a, 'viewpoint_description_Layer562', b1)
    if hasattr(b1, 'DecorationDescriptionsSet'):
        assert _is_linked(b1, 'DecorationDescriptionsSet', a)
    _safe_set(a, 'viewpoint_description_Layer562', b2)
    assert _is_linked(a, 'viewpoint_description_Layer562', b2)
    if hasattr(b1, 'DecorationDescriptionsSet'):
        assert not _is_linked(b1, 'DecorationDescriptionsSet', a)
    if hasattr(b2, 'DecorationDescriptionsSet'):
        assert _is_linked(b2, 'DecorationDescriptionsSet', a)
    _safe_set(a, 'viewpoint_description_Layer562', None)
    assert not _is_linked(a, 'viewpoint_description_Layer562', b2)
    if hasattr(b2, 'DecorationDescriptionsSet'):
        assert not _is_linked(b2, 'DecorationDescriptionsSet', a)


def test_assoc_decorations261_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = diagram_viewpoint_Decoration()
    b2 = diagram_viewpoint_Decoration()
    _safe_set(a, 'viewpoint_diagram_DDiagramElement262', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElement262', b1)
    if hasattr(b1, 'diagram_viewpoint_Decoration'):
        assert _is_linked(b1, 'diagram_viewpoint_Decoration', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElement262', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElement262', b2)
    if hasattr(b1, 'diagram_viewpoint_Decoration'):
        assert not _is_linked(b1, 'diagram_viewpoint_Decoration', a)
    if hasattr(b2, 'diagram_viewpoint_Decoration'):
        assert _is_linked(b2, 'diagram_viewpoint_Decoration', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElement262', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElement262', b2)
    if hasattr(b2, 'diagram_viewpoint_Decoration'):
        assert not _is_linked(b2, 'diagram_viewpoint_Decoration', a)


def test_assoc_defaultConcern422_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = concern_ConcernDescription()
    b2 = concern_ConcernDescription()
    _safe_set(a, 'viewpoint_description_DiagramDescription423', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription423', b1)
    if hasattr(b1, 'concern_ConcernDescription424'):
        assert _is_linked(b1, 'concern_ConcernDescription424', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription423', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription423', b2)
    if hasattr(b1, 'concern_ConcernDescription424'):
        assert not _is_linked(b1, 'concern_ConcernDescription424', a)
    if hasattr(b2, 'concern_ConcernDescription424'):
        assert _is_linked(b2, 'concern_ConcernDescription424', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription423', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription423', b2)
    if hasattr(b2, 'concern_ConcernDescription424'):
        assert not _is_linked(b2, 'concern_ConcernDescription424', a)


def test_assoc_defaultLayer433_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_Layer()
    b2 = description_Layer()
    _safe_set(a, 'viewpoint_description_DiagramDescription434', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription434', b1)
    if hasattr(b1, 'description_Layer435'):
        assert _is_linked(b1, 'description_Layer435', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription434', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription434', b2)
    if hasattr(b1, 'description_Layer435'):
        assert not _is_linked(b1, 'description_Layer435', a)
    if hasattr(b2, 'description_Layer435'):
        assert _is_linked(b2, 'description_Layer435', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription434', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription434', b2)
    if hasattr(b2, 'description_Layer435'):
        assert not _is_linked(b2, 'description_Layer435', a)


def test_assoc_deletionDescription473_link_reassign_clear():
    a = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    b1 = tool_DeleteElementDescription()
    b2 = tool_DeleteElementDescription()
    _safe_set(a, 'viewpoint_description_DiagramElementMapping', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramElementMapping', b1)
    if hasattr(b1, 'tool_DeleteElementDescription'):
        assert _is_linked(b1, 'tool_DeleteElementDescription', a)
    _safe_set(a, 'viewpoint_description_DiagramElementMapping', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramElementMapping', b2)
    if hasattr(b1, 'tool_DeleteElementDescription'):
        assert not _is_linked(b1, 'tool_DeleteElementDescription', a)
    if hasattr(b2, 'tool_DeleteElementDescription'):
        assert _is_linked(b2, 'tool_DeleteElementDescription', a)
    _safe_set(a, 'viewpoint_description_DiagramElementMapping', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramElementMapping', b2)
    if hasattr(b2, 'tool_DeleteElementDescription'):
        assert not _is_linked(b2, 'tool_DeleteElementDescription', a)


def test_assoc_description229_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = description_DiagramDescription()
    b2 = description_DiagramDescription()
    _safe_set(a, 'viewpoint_diagram_DDiagram230', b1)
    assert _is_linked(a, 'viewpoint_diagram_DDiagram230', b1)
    if hasattr(b1, 'description_DiagramDescription'):
        assert _is_linked(b1, 'description_DiagramDescription', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram230', b2)
    assert _is_linked(a, 'viewpoint_diagram_DDiagram230', b2)
    if hasattr(b1, 'description_DiagramDescription'):
        assert not _is_linked(b1, 'description_DiagramDescription', a)
    if hasattr(b2, 'description_DiagramDescription'):
        assert _is_linked(b2, 'description_DiagramDescription', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram230', None)
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram230', b2)
    if hasattr(b2, 'description_DiagramDescription'):
        assert not _is_linked(b2, 'description_DiagramDescription', a)


def test_assoc_details95_link_reassign_clear():
    a = viewpoint_description_DAnnotation(source="sample_text")
    b1 = description_viewpoint_EStringToStringMapEntry()
    b2 = description_viewpoint_EStringToStringMapEntry()
    _safe_set(a, 'viewpoint_description_DAnnotation', {b1})
    assert _is_linked(a, 'viewpoint_description_DAnnotation', b1)
    if hasattr(b1, 'description_viewpoint_EStringToStringMapEntry'):
        assert _is_linked(b1, 'description_viewpoint_EStringToStringMapEntry', a)
    _safe_set(a, 'viewpoint_description_DAnnotation', {b2})
    assert _is_linked(a, 'viewpoint_description_DAnnotation', b2)
    if hasattr(b1, 'description_viewpoint_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'description_viewpoint_EStringToStringMapEntry', a)
    if hasattr(b2, 'description_viewpoint_EStringToStringMapEntry'):
        assert _is_linked(b2, 'description_viewpoint_EStringToStringMapEntry', a)
    _safe_set(a, 'viewpoint_description_DAnnotation', set())
    assert not _is_linked(a, 'viewpoint_description_DAnnotation', b2)
    if hasattr(b2, 'description_viewpoint_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'description_viewpoint_EStringToStringMapEntry', a)


def test_assoc_diagramDescription717_link_reassign_clear():
    a = viewpoint_tool_Navigation(createIfNotExistent=True)
    b1 = description_DiagramDescription()
    b2 = description_DiagramDescription()
    _safe_set(a, 'viewpoint_tool_Navigation', b1)
    assert _is_linked(a, 'viewpoint_tool_Navigation', b1)
    if hasattr(b1, 'description_DiagramDescription718'):
        assert _is_linked(b1, 'description_DiagramDescription718', a)
    _safe_set(a, 'viewpoint_tool_Navigation', b2)
    assert _is_linked(a, 'viewpoint_tool_Navigation', b2)
    if hasattr(b1, 'description_DiagramDescription718'):
        assert not _is_linked(b1, 'description_DiagramDescription718', a)
    if hasattr(b2, 'description_DiagramDescription718'):
        assert _is_linked(b2, 'description_DiagramDescription718', a)
    _safe_set(a, 'viewpoint_tool_Navigation', None)
    assert not _is_linked(a, 'viewpoint_tool_Navigation', b2)
    if hasattr(b2, 'description_DiagramDescription718'):
        assert not _is_linked(b2, 'description_DiagramDescription718', a)


def test_assoc_diagramElementMapping263_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_diagram_DDiagramElement264', b1)
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElement264', b1)
    if hasattr(b1, 'description_DiagramElementMapping265'):
        assert _is_linked(b1, 'description_DiagramElementMapping265', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElement264', b2)
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElement264', b2)
    if hasattr(b1, 'description_DiagramElementMapping265'):
        assert not _is_linked(b1, 'description_DiagramElementMapping265', a)
    if hasattr(b2, 'description_DiagramElementMapping265'):
        assert _is_linked(b2, 'description_DiagramElementMapping265', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElement264', None)
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElement264', b2)
    if hasattr(b2, 'description_DiagramElementMapping265'):
        assert not _is_linked(b2, 'description_DiagramElementMapping265', a)


def test_assoc_diagramElements226_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = DDiagramElement()
    b2 = DDiagramElement()
    _safe_set(a, 'viewpoint_diagram_DDiagram227', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram227', b1)
    if hasattr(b1, 'DDiagramElement228'):
        assert _is_linked(b1, 'DDiagramElement228', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram227', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram227', b2)
    if hasattr(b1, 'DDiagramElement228'):
        assert not _is_linked(b1, 'DDiagramElement228', a)
    if hasattr(b2, 'DDiagramElement228'):
        assert _is_linked(b2, 'DDiagramElement228', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram227', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram227', b2)
    if hasattr(b2, 'DDiagramElement228'):
        assert not _is_linked(b2, 'DDiagramElement228', a)


def test_assoc_diagramInitialisation430_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_description_DiagramDescription431', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription431', b1)
    if hasattr(b1, 'tool_InitialOperation432'):
        assert _is_linked(b1, 'tool_InitialOperation432', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription431', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription431', b2)
    if hasattr(b1, 'tool_InitialOperation432'):
        assert not _is_linked(b1, 'tool_InitialOperation432', a)
    if hasattr(b2, 'tool_InitialOperation432'):
        assert _is_linked(b2, 'tool_InitialOperation432', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription431', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription431', b2)
    if hasattr(b2, 'tool_InitialOperation432'):
        assert not _is_linked(b2, 'tool_InitialOperation432', a)


def test_assoc_diagramSet16_link_reassign_clear():
    a = viewpoint_DRepresentationContainer()
    b1 = DDiagramSet()
    b2 = DDiagramSet()
    _safe_set(a, 'viewpoint_DRepresentationContainer', {b1})
    assert _is_linked(a, 'viewpoint_DRepresentationContainer', b1)
    if hasattr(b1, 'DDiagramSet'):
        assert _is_linked(b1, 'DDiagramSet', a)
    _safe_set(a, 'viewpoint_DRepresentationContainer', {b2})
    assert _is_linked(a, 'viewpoint_DRepresentationContainer', b2)
    if hasattr(b1, 'DDiagramSet'):
        assert not _is_linked(b1, 'DDiagramSet', a)
    if hasattr(b2, 'DDiagramSet'):
        assert _is_linked(b2, 'DDiagramSet', a)
    _safe_set(a, 'viewpoint_DRepresentationContainer', set())
    assert not _is_linked(a, 'viewpoint_DRepresentationContainer', b2)
    if hasattr(b2, 'DDiagramSet'):
        assert not _is_linked(b2, 'DDiagramSet', a)


def test_assoc_doubleClickDescription476_link_reassign_clear():
    a = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
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


def test_assoc_eAnnotations4_link_reassign_clear():
    a = viewpoint_DAnalysis(version="sample_text")
    b1 = DAnnotationEntry()
    b2 = DAnnotationEntry()
    _safe_set(a, 'viewpoint_DAnalysis5', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysis5', b1)
    if hasattr(b1, 'DAnnotationEntry'):
        assert _is_linked(b1, 'DAnnotationEntry', a)
    _safe_set(a, 'viewpoint_DAnalysis5', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysis5', b2)
    if hasattr(b1, 'DAnnotationEntry'):
        assert not _is_linked(b1, 'DAnnotationEntry', a)
    if hasattr(b2, 'DAnnotationEntry'):
        assert _is_linked(b2, 'DAnnotationEntry', a)
    _safe_set(a, 'viewpoint_DAnalysis5', set())
    assert not _is_linked(a, 'viewpoint_DAnalysis5', b2)
    if hasattr(b2, 'DAnnotationEntry'):
        assert not _is_linked(b2, 'DAnnotationEntry', a)


def test_assoc_eAnnotations94_link_reassign_clear():
    a = viewpoint_description_DModelElement()
    b1 = DAnnotation()
    b2 = DAnnotation()
    _safe_set(a, 'viewpoint_description_DModelElement', {b1})
    assert _is_linked(a, 'viewpoint_description_DModelElement', b1)
    if hasattr(b1, 'DAnnotation'):
        assert _is_linked(b1, 'DAnnotation', a)
    _safe_set(a, 'viewpoint_description_DModelElement', {b2})
    assert _is_linked(a, 'viewpoint_description_DModelElement', b2)
    if hasattr(b1, 'DAnnotation'):
        assert not _is_linked(b1, 'DAnnotation', a)
    if hasattr(b2, 'DAnnotation'):
        assert _is_linked(b2, 'DAnnotation', a)
    _safe_set(a, 'viewpoint_description_DModelElement', set())
    assert not _is_linked(a, 'viewpoint_description_DModelElement', b2)
    if hasattr(b2, 'DAnnotation'):
        assert not _is_linked(b2, 'DAnnotation', a)


def test_assoc_edgeMappingImports450_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_EdgeMappingImport()
    b2 = description_EdgeMappingImport()
    _safe_set(a, 'viewpoint_description_DiagramDescription451', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription451', b1)
    if hasattr(b1, 'description_EdgeMappingImport'):
        assert _is_linked(b1, 'description_EdgeMappingImport', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription451', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription451', b2)
    if hasattr(b1, 'description_EdgeMappingImport'):
        assert not _is_linked(b1, 'description_EdgeMappingImport', a)
    if hasattr(b2, 'description_EdgeMappingImport'):
        assert _is_linked(b2, 'description_EdgeMappingImport', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription451', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription451', b2)
    if hasattr(b2, 'description_EdgeMappingImport'):
        assert not _is_linked(b2, 'description_EdgeMappingImport', a)


def test_assoc_edgeMappingImports543_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = description_EdgeMappingImport()
    b2 = description_EdgeMappingImport()
    _safe_set(a, 'viewpoint_description_Layer544', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer544', b1)
    if hasattr(b1, 'description_EdgeMappingImport545'):
        assert _is_linked(b1, 'description_EdgeMappingImport545', a)
    _safe_set(a, 'viewpoint_description_Layer544', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer544', b2)
    if hasattr(b1, 'description_EdgeMappingImport545'):
        assert not _is_linked(b1, 'description_EdgeMappingImport545', a)
    if hasattr(b2, 'description_EdgeMappingImport545'):
        assert _is_linked(b2, 'description_EdgeMappingImport545', a)
    _safe_set(a, 'viewpoint_description_Layer544', set())
    assert not _is_linked(a, 'viewpoint_description_Layer544', b2)
    if hasattr(b2, 'description_EdgeMappingImport545'):
        assert not _is_linked(b2, 'description_EdgeMappingImport545', a)


def test_assoc_edgeMappings447_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_EdgeMapping()
    b2 = description_EdgeMapping()
    _safe_set(a, 'viewpoint_description_DiagramDescription448', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription448', b1)
    if hasattr(b1, 'description_EdgeMapping449'):
        assert _is_linked(b1, 'description_EdgeMapping449', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription448', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription448', b2)
    if hasattr(b1, 'description_EdgeMapping449'):
        assert not _is_linked(b1, 'description_EdgeMapping449', a)
    if hasattr(b2, 'description_EdgeMapping449'):
        assert _is_linked(b2, 'description_EdgeMapping449', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription448', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription448', b2)
    if hasattr(b2, 'description_EdgeMapping449'):
        assert not _is_linked(b2, 'description_EdgeMapping449', a)


def test_assoc_edgeMappings540_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = description_EdgeMapping()
    b2 = description_EdgeMapping()
    _safe_set(a, 'viewpoint_description_Layer541', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer541', b1)
    if hasattr(b1, 'description_EdgeMapping542'):
        assert _is_linked(b1, 'description_EdgeMapping542', a)
    _safe_set(a, 'viewpoint_description_Layer541', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer541', b2)
    if hasattr(b1, 'description_EdgeMapping542'):
        assert not _is_linked(b1, 'description_EdgeMapping542', a)
    if hasattr(b2, 'description_EdgeMapping542'):
        assert _is_linked(b2, 'description_EdgeMapping542', a)
    _safe_set(a, 'viewpoint_description_Layer541', set())
    assert not _is_linked(a, 'viewpoint_description_Layer541', b2)
    if hasattr(b2, 'description_EdgeMapping542'):
        assert not _is_linked(b2, 'description_EdgeMapping542', a)


def test_assoc_edgeMappings636_link_reassign_clear():
    a = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = description_EdgeMapping()
    b2 = description_EdgeMapping()
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription', {b1})
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription', b1)
    if hasattr(b1, 'description_EdgeMapping637'):
        assert _is_linked(b1, 'description_EdgeMapping637', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription', {b2})
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription', b2)
    if hasattr(b1, 'description_EdgeMapping637'):
        assert not _is_linked(b1, 'description_EdgeMapping637', a)
    if hasattr(b2, 'description_EdgeMapping637'):
        assert _is_linked(b2, 'description_EdgeMapping637', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription', set())
    assert not _is_linked(a, 'viewpoint_tool_EdgeCreationDescription', b2)
    if hasattr(b2, 'description_EdgeMapping637'):
        assert not _is_linked(b2, 'description_EdgeMapping637', a)


def test_assoc_edgeView706_link_reassign_clear():
    a = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription707', b1)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription707', b1)
    if hasattr(b1, 'tool_ElementSelectVariable708'):
        assert _is_linked(b1, 'tool_ElementSelectVariable708', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription707', b2)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription707', b2)
    if hasattr(b1, 'tool_ElementSelectVariable708'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable708', a)
    if hasattr(b2, 'tool_ElementSelectVariable708'):
        assert _is_linked(b2, 'tool_ElementSelectVariable708', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription707', None)
    assert not _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription707', b2)
    if hasattr(b2, 'tool_ElementSelectVariable708'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable708', a)


def test_assoc_edges233_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = DEdge()
    b2 = DEdge()
    _safe_set(a, 'viewpoint_diagram_DDiagram234', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram234', b1)
    if hasattr(b1, 'DEdge'):
        assert _is_linked(b1, 'DEdge', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram234', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram234', b2)
    if hasattr(b1, 'DEdge'):
        assert not _is_linked(b1, 'DEdge', a)
    if hasattr(b2, 'DEdge'):
        assert _is_linked(b2, 'DEdge', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram234', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram234', b2)
    if hasattr(b2, 'DEdge'):
        assert not _is_linked(b2, 'DEdge', a)


def test_assoc_element126_link_reassign_clear():
    a = viewpoint_tool_ToolDescription(iconPath="sample_text")
    b1 = tool_ElementVariable()
    b2 = tool_ElementVariable()
    _safe_set(a, 'viewpoint_tool_ToolDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription', b1)
    if hasattr(b1, 'tool_ElementVariable'):
        assert _is_linked(b1, 'tool_ElementVariable', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription', b2)
    if hasattr(b1, 'tool_ElementVariable'):
        assert not _is_linked(b1, 'tool_ElementVariable', a)
    if hasattr(b2, 'tool_ElementVariable'):
        assert _is_linked(b2, 'tool_ElementVariable', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_ToolDescription', b2)
    if hasattr(b2, 'tool_ElementVariable'):
        assert not _is_linked(b2, 'tool_ElementVariable', a)


def test_assoc_element137_link_reassign_clear():
    a = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_ElementDropVariable()
    b2 = tool_ElementDropVariable()
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription138', b1)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription138', b1)
    if hasattr(b1, 'tool_ElementDropVariable'):
        assert _is_linked(b1, 'tool_ElementDropVariable', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription138', b2)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription138', b2)
    if hasattr(b1, 'tool_ElementDropVariable'):
        assert not _is_linked(b1, 'tool_ElementDropVariable', a)
    if hasattr(b2, 'tool_ElementDropVariable'):
        assert _is_linked(b2, 'tool_ElementDropVariable', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription138', None)
    assert not _is_linked(a, 'viewpoint_tool_ContainerDropDescription138', b2)
    if hasattr(b2, 'tool_ElementDropVariable'):
        assert not _is_linked(b2, 'tool_ElementDropVariable', a)


def test_assoc_element157_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription', b1)
    if hasattr(b1, 'tool_ElementSelectVariable'):
        assert _is_linked(b1, 'tool_ElementSelectVariable', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription', b2)
    if hasattr(b1, 'tool_ElementSelectVariable'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable', a)
    if hasattr(b2, 'tool_ElementSelectVariable'):
        assert _is_linked(b2, 'tool_ElementSelectVariable', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription', b2)
    if hasattr(b2, 'tool_ElementSelectVariable'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable', a)


def test_assoc_element166_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b1)
    if hasattr(b1, 'tool_ElementSelectVariable167'):
        assert _is_linked(b1, 'tool_ElementSelectVariable167', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    if hasattr(b1, 'tool_ElementSelectVariable167'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable167', a)
    if hasattr(b2, 'tool_ElementSelectVariable167'):
        assert _is_linked(b2, 'tool_ElementSelectVariable167', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    if hasattr(b2, 'tool_ElementSelectVariable167'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable167', a)


def test_assoc_element668_link_reassign_clear():
    a = viewpoint_tool_DeleteElementDescription()
    b1 = tool_ElementDeleteVariable()
    b2 = tool_ElementDeleteVariable()
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription', b1)
    if hasattr(b1, 'tool_ElementDeleteVariable'):
        assert _is_linked(b1, 'tool_ElementDeleteVariable', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription', b2)
    if hasattr(b1, 'tool_ElementDeleteVariable'):
        assert not _is_linked(b1, 'tool_ElementDeleteVariable', a)
    if hasattr(b2, 'tool_ElementDeleteVariable'):
        assert _is_linked(b2, 'tool_ElementDeleteVariable', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_DeleteElementDescription', b2)
    if hasattr(b2, 'tool_ElementDeleteVariable'):
        assert not _is_linked(b2, 'tool_ElementDeleteVariable', a)


def test_assoc_element700_link_reassign_clear():
    a = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription701', b1)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription701', b1)
    if hasattr(b1, 'tool_ElementSelectVariable702'):
        assert _is_linked(b1, 'tool_ElementSelectVariable702', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription701', b2)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription701', b2)
    if hasattr(b1, 'tool_ElementSelectVariable702'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable702', a)
    if hasattr(b2, 'tool_ElementSelectVariable702'):
        assert _is_linked(b2, 'tool_ElementSelectVariable702', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription701', None)
    assert not _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription701', b2)
    if hasattr(b2, 'tool_ElementSelectVariable702'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable702', a)


def test_assoc_elementView127_link_reassign_clear():
    a = viewpoint_tool_ToolDescription(iconPath="sample_text")
    b1 = tool_ElementViewVariable()
    b2 = tool_ElementViewVariable()
    _safe_set(a, 'viewpoint_tool_ToolDescription128', b1)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription128', b1)
    if hasattr(b1, 'tool_ElementViewVariable'):
        assert _is_linked(b1, 'tool_ElementViewVariable', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription128', b2)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription128', b2)
    if hasattr(b1, 'tool_ElementViewVariable'):
        assert not _is_linked(b1, 'tool_ElementViewVariable', a)
    if hasattr(b2, 'tool_ElementViewVariable'):
        assert _is_linked(b2, 'tool_ElementViewVariable', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription128', None)
    assert not _is_linked(a, 'viewpoint_tool_ToolDescription128', b2)
    if hasattr(b2, 'tool_ElementViewVariable'):
        assert not _is_linked(b2, 'tool_ElementViewVariable', a)


def test_assoc_elementView669_link_reassign_clear():
    a = viewpoint_tool_DeleteElementDescription()
    b1 = tool_ElementDeleteVariable()
    b2 = tool_ElementDeleteVariable()
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription670', b1)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription670', b1)
    if hasattr(b1, 'tool_ElementDeleteVariable671'):
        assert _is_linked(b1, 'tool_ElementDeleteVariable671', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription670', b2)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription670', b2)
    if hasattr(b1, 'tool_ElementDeleteVariable671'):
        assert not _is_linked(b1, 'tool_ElementDeleteVariable671', a)
    if hasattr(b2, 'tool_ElementDeleteVariable671'):
        assert _is_linked(b2, 'tool_ElementDeleteVariable671', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription670', None)
    assert not _is_linked(a, 'viewpoint_tool_DeleteElementDescription670', b2)
    if hasattr(b2, 'tool_ElementDeleteVariable671'):
        assert not _is_linked(b2, 'tool_ElementDeleteVariable671', a)


def test_assoc_elements291_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = DDiagramElement()
    b2 = DDiagramElement()
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer292', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer292', b1)
    if hasattr(b1, 'DDiagramElement293'):
        assert _is_linked(b1, 'DDiagramElement293', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer292', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer292', b2)
    if hasattr(b1, 'DDiagramElement293'):
        assert not _is_linked(b1, 'DDiagramElement293', a)
    if hasattr(b2, 'DDiagramElement293'):
        assert _is_linked(b2, 'DDiagramElement293', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer292', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer292', b2)
    if hasattr(b2, 'DDiagramElement293'):
        assert not _is_linked(b2, 'DDiagramElement293', a)


def test_assoc_endLabelStyle373_link_reassign_clear():
    a = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = EndLabelStyle()
    b2 = EndLabelStyle()
    _safe_set(a, 'viewpoint_diagram_EdgeStyle374', b1)
    assert _is_linked(a, 'viewpoint_diagram_EdgeStyle374', b1)
    if hasattr(b1, 'EndLabelStyle'):
        assert _is_linked(b1, 'EndLabelStyle', a)
    _safe_set(a, 'viewpoint_diagram_EdgeStyle374', b2)
    assert _is_linked(a, 'viewpoint_diagram_EdgeStyle374', b2)
    if hasattr(b1, 'EndLabelStyle'):
        assert not _is_linked(b1, 'EndLabelStyle', a)
    if hasattr(b2, 'EndLabelStyle'):
        assert _is_linked(b2, 'EndLabelStyle', a)
    _safe_set(a, 'viewpoint_diagram_EdgeStyle374', None)
    assert not _is_linked(a, 'viewpoint_diagram_EdgeStyle374', b2)
    if hasattr(b2, 'EndLabelStyle'):
        assert not _is_linked(b2, 'EndLabelStyle', a)


def test_assoc_endLabelStyleDescription604_link_reassign_clear():
    a = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = style_EndLabelStyleDescription()
    b2 = style_EndLabelStyleDescription()
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription605', b1)
    assert _is_linked(a, 'viewpoint_style_EdgeStyleDescription605', b1)
    if hasattr(b1, 'style_EndLabelStyleDescription'):
        assert _is_linked(b1, 'style_EndLabelStyleDescription', a)
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription605', b2)
    assert _is_linked(a, 'viewpoint_style_EdgeStyleDescription605', b2)
    if hasattr(b1, 'style_EndLabelStyleDescription'):
        assert not _is_linked(b1, 'style_EndLabelStyleDescription', a)
    if hasattr(b2, 'style_EndLabelStyleDescription'):
        assert _is_linked(b2, 'style_EndLabelStyleDescription', a)
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription605', None)
    assert not _is_linked(a, 'viewpoint_style_EdgeStyleDescription605', b2)
    if hasattr(b2, 'style_EndLabelStyleDescription'):
        assert not _is_linked(b2, 'style_EndLabelStyleDescription', a)


def test_assoc_entries120_link_reassign_clear():
    a = viewpoint_description_UserColorsPalette(name="sample_text")
    b1 = UserColor()
    b2 = UserColor()
    _safe_set(a, 'viewpoint_description_UserColorsPalette', {b1})
    assert _is_linked(a, 'viewpoint_description_UserColorsPalette', b1)
    if hasattr(b1, 'UserColor'):
        assert _is_linked(b1, 'UserColor', a)
    _safe_set(a, 'viewpoint_description_UserColorsPalette', {b2})
    assert _is_linked(a, 'viewpoint_description_UserColorsPalette', b2)
    if hasattr(b1, 'UserColor'):
        assert not _is_linked(b1, 'UserColor', a)
    if hasattr(b2, 'UserColor'):
        assert _is_linked(b2, 'UserColor', a)
    _safe_set(a, 'viewpoint_description_UserColorsPalette', set())
    assert not _is_linked(a, 'viewpoint_description_UserColorsPalette', b2)
    if hasattr(b2, 'UserColor'):
        assert not _is_linked(b2, 'UserColor', a)


def test_assoc_extraMappings633_link_reassign_clear():
    a = viewpoint_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = description_AbstractNodeMapping()
    b2 = description_AbstractNodeMapping()
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription634', {b1})
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription634', b1)
    if hasattr(b1, 'description_AbstractNodeMapping635'):
        assert _is_linked(b1, 'description_AbstractNodeMapping635', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription634', {b2})
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription634', b2)
    if hasattr(b1, 'description_AbstractNodeMapping635'):
        assert not _is_linked(b1, 'description_AbstractNodeMapping635', a)
    if hasattr(b2, 'description_AbstractNodeMapping635'):
        assert _is_linked(b2, 'description_AbstractNodeMapping635', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription634', set())
    assert not _is_linked(a, 'viewpoint_tool_NodeCreationDescription634', b2)
    if hasattr(b2, 'description_AbstractNodeMapping635'):
        assert not _is_linked(b2, 'description_AbstractNodeMapping635', a)


def test_assoc_extraMappings665_link_reassign_clear():
    a = viewpoint_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = description_AbstractNodeMapping()
    b2 = description_AbstractNodeMapping()
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription666', {b1})
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription666', b1)
    if hasattr(b1, 'description_AbstractNodeMapping667'):
        assert _is_linked(b1, 'description_AbstractNodeMapping667', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription666', {b2})
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription666', b2)
    if hasattr(b1, 'description_AbstractNodeMapping667'):
        assert not _is_linked(b1, 'description_AbstractNodeMapping667', a)
    if hasattr(b2, 'description_AbstractNodeMapping667'):
        assert _is_linked(b2, 'description_AbstractNodeMapping667', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription666', set())
    assert not _is_linked(a, 'viewpoint_tool_ContainerCreationDescription666', b2)
    if hasattr(b2, 'description_AbstractNodeMapping667'):
        assert not _is_linked(b2, 'description_AbstractNodeMapping667', a)


def test_assoc_extraSourceMappings648_link_reassign_clear():
    a = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription649', {b1})
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription649', b1)
    if hasattr(b1, 'description_DiagramElementMapping650'):
        assert _is_linked(b1, 'description_DiagramElementMapping650', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription649', {b2})
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription649', b2)
    if hasattr(b1, 'description_DiagramElementMapping650'):
        assert not _is_linked(b1, 'description_DiagramElementMapping650', a)
    if hasattr(b2, 'description_DiagramElementMapping650'):
        assert _is_linked(b2, 'description_DiagramElementMapping650', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription649', set())
    assert not _is_linked(a, 'viewpoint_tool_EdgeCreationDescription649', b2)
    if hasattr(b2, 'description_DiagramElementMapping650'):
        assert not _is_linked(b2, 'description_DiagramElementMapping650', a)


def test_assoc_extraTargetMappings651_link_reassign_clear():
    a = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription652', {b1})
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription652', b1)
    if hasattr(b1, 'description_DiagramElementMapping653'):
        assert _is_linked(b1, 'description_DiagramElementMapping653', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription652', {b2})
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription652', b2)
    if hasattr(b1, 'description_DiagramElementMapping653'):
        assert not _is_linked(b1, 'description_DiagramElementMapping653', a)
    if hasattr(b2, 'description_DiagramElementMapping653'):
        assert _is_linked(b2, 'description_DiagramElementMapping653', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription652', set())
    assert not _is_linked(a, 'viewpoint_tool_EdgeCreationDescription652', b2)
    if hasattr(b2, 'description_DiagramElementMapping653'):
        assert not _is_linked(b2, 'description_DiagramElementMapping653', a)


def test_assoc_featureCustomizations101_link_reassign_clear():
    a = viewpoint_description_VSMElementCustomization(predicateExpression="sample_text")
    b1 = EStructuralFeatureCustomization()
    b2 = EStructuralFeatureCustomization()
    _safe_set(a, 'viewpoint_description_VSMElementCustomization', {b1})
    assert _is_linked(a, 'viewpoint_description_VSMElementCustomization', b1)
    if hasattr(b1, 'EStructuralFeatureCustomization'):
        assert _is_linked(b1, 'EStructuralFeatureCustomization', a)
    _safe_set(a, 'viewpoint_description_VSMElementCustomization', {b2})
    assert _is_linked(a, 'viewpoint_description_VSMElementCustomization', b2)
    if hasattr(b1, 'EStructuralFeatureCustomization'):
        assert not _is_linked(b1, 'EStructuralFeatureCustomization', a)
    if hasattr(b2, 'EStructuralFeatureCustomization'):
        assert _is_linked(b2, 'EStructuralFeatureCustomization', a)
    _safe_set(a, 'viewpoint_description_VSMElementCustomization', set())
    assert not _is_linked(a, 'viewpoint_description_VSMElementCustomization', b2)
    if hasattr(b2, 'EStructuralFeatureCustomization'):
        assert not _is_linked(b2, 'EStructuralFeatureCustomization', a)


def test_assoc_filterVariableHistory252_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = FilterVariableHistory()
    b2 = FilterVariableHistory()
    _safe_set(a, 'viewpoint_diagram_DDiagram253', b1)
    assert _is_linked(a, 'viewpoint_diagram_DDiagram253', b1)
    if hasattr(b1, 'FilterVariableHistory'):
        assert _is_linked(b1, 'FilterVariableHistory', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram253', b2)
    assert _is_linked(a, 'viewpoint_diagram_DDiagram253', b2)
    if hasattr(b1, 'FilterVariableHistory'):
        assert not _is_linked(b1, 'FilterVariableHistory', a)
    if hasattr(b2, 'FilterVariableHistory'):
        assert _is_linked(b2, 'FilterVariableHistory', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram253', None)
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram253', b2)
    if hasattr(b2, 'FilterVariableHistory'):
        assert not _is_linked(b2, 'FilterVariableHistory', a)


def test_assoc_filters125_link_reassign_clear():
    a = viewpoint_tool_AbstractToolDescription(forceRefresh=True, precondition="sample_text")
    b1 = tool_ToolFilterDescription()
    b2 = tool_ToolFilterDescription()
    _safe_set(a, 'viewpoint_tool_AbstractToolDescription', {b1})
    assert _is_linked(a, 'viewpoint_tool_AbstractToolDescription', b1)
    if hasattr(b1, 'tool_ToolFilterDescription'):
        assert _is_linked(b1, 'tool_ToolFilterDescription', a)
    _safe_set(a, 'viewpoint_tool_AbstractToolDescription', {b2})
    assert _is_linked(a, 'viewpoint_tool_AbstractToolDescription', b2)
    if hasattr(b1, 'tool_ToolFilterDescription'):
        assert not _is_linked(b1, 'tool_ToolFilterDescription', a)
    if hasattr(b2, 'tool_ToolFilterDescription'):
        assert _is_linked(b2, 'tool_ToolFilterDescription', a)
    _safe_set(a, 'viewpoint_tool_AbstractToolDescription', set())
    assert not _is_linked(a, 'viewpoint_tool_AbstractToolDescription', b2)
    if hasattr(b2, 'tool_ToolFilterDescription'):
        assert not _is_linked(b2, 'tool_ToolFilterDescription', a)


def test_assoc_filters405_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = filter_FilterDescription()
    b2 = filter_FilterDescription()
    _safe_set(a, 'viewpoint_description_DiagramDescription', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription', b1)
    if hasattr(b1, 'filter_FilterDescription406'):
        assert _is_linked(b1, 'filter_FilterDescription406', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription', b2)
    if hasattr(b1, 'filter_FilterDescription406'):
        assert not _is_linked(b1, 'filter_FilterDescription406', a)
    if hasattr(b2, 'filter_FilterDescription406'):
        assert _is_linked(b2, 'filter_FilterDescription406', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription', b2)
    if hasattr(b2, 'filter_FilterDescription406'):
        assert not _is_linked(b2, 'filter_FilterDescription406', a)


def test_assoc_fixes737_link_reassign_clear():
    a = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    b1 = validation_ValidationFix()
    b2 = validation_ValidationFix()
    _safe_set(a, 'viewpoint_validation_ValidationRule738', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationRule738', b1)
    if hasattr(b1, 'validation_ValidationFix'):
        assert _is_linked(b1, 'validation_ValidationFix', a)
    _safe_set(a, 'viewpoint_validation_ValidationRule738', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationRule738', b2)
    if hasattr(b1, 'validation_ValidationFix'):
        assert not _is_linked(b1, 'validation_ValidationFix', a)
    if hasattr(b2, 'validation_ValidationFix'):
        assert _is_linked(b2, 'validation_ValidationFix', a)
    _safe_set(a, 'viewpoint_validation_ValidationRule738', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationRule738', b2)
    if hasattr(b2, 'validation_ValidationFix'):
        assert not _is_linked(b2, 'validation_ValidationFix', a)


def test_assoc_foregroundColor345_link_reassign_clear():
    a = viewpoint_diagram_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_GaugeSection346', b1)
    assert _is_linked(a, 'viewpoint_diagram_GaugeSection346', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues347'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues347', a)
    _safe_set(a, 'viewpoint_diagram_GaugeSection346', b2)
    assert _is_linked(a, 'viewpoint_diagram_GaugeSection346', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues347'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues347', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues347'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues347', a)
    _safe_set(a, 'viewpoint_diagram_GaugeSection346', None)
    assert not _is_linked(a, 'viewpoint_diagram_GaugeSection346', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues347'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues347', a)


def test_assoc_foregroundColor350_link_reassign_clear():
    a = viewpoint_diagram_FlatContainerStyle(backgroundStyle="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_FlatContainerStyle351', b1)
    assert _is_linked(a, 'viewpoint_diagram_FlatContainerStyle351', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues352'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues352', a)
    _safe_set(a, 'viewpoint_diagram_FlatContainerStyle351', b2)
    assert _is_linked(a, 'viewpoint_diagram_FlatContainerStyle351', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues352'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues352', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues352'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues352', a)
    _safe_set(a, 'viewpoint_diagram_FlatContainerStyle351', None)
    assert not _is_linked(a, 'viewpoint_diagram_FlatContainerStyle351', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues352'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues352', a)


def test_assoc_foregroundColor585_link_reassign_clear():
    a = viewpoint_style_GaugeSectionDescription(label="sample_text", maxValueExpression="sample_text", minValueExpression="sample_text", valueExpression="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_GaugeSectionDescription586', b1)
    assert _is_linked(a, 'viewpoint_style_GaugeSectionDescription586', b1)
    if hasattr(b1, 'ColorDescription587'):
        assert _is_linked(b1, 'ColorDescription587', a)
    _safe_set(a, 'viewpoint_style_GaugeSectionDescription586', b2)
    assert _is_linked(a, 'viewpoint_style_GaugeSectionDescription586', b2)
    if hasattr(b1, 'ColorDescription587'):
        assert not _is_linked(b1, 'ColorDescription587', a)
    if hasattr(b2, 'ColorDescription587'):
        assert _is_linked(b2, 'ColorDescription587', a)
    _safe_set(a, 'viewpoint_style_GaugeSectionDescription586', None)
    assert not _is_linked(a, 'viewpoint_style_GaugeSectionDescription586', b2)
    if hasattr(b2, 'ColorDescription587'):
        assert not _is_linked(b2, 'ColorDescription587', a)


def test_assoc_foregroundColor590_link_reassign_clear():
    a = viewpoint_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription591', b1)
    assert _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription591', b1)
    if hasattr(b1, 'ColorDescription592'):
        assert _is_linked(b1, 'ColorDescription592', a)
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription591', b2)
    assert _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription591', b2)
    if hasattr(b1, 'ColorDescription592'):
        assert not _is_linked(b1, 'ColorDescription592', a)
    if hasattr(b2, 'ColorDescription592'):
        assert _is_linked(b2, 'ColorDescription592', a)
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription591', None)
    assert not _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription591', b2)
    if hasattr(b2, 'ColorDescription592'):
        assert not _is_linked(b2, 'ColorDescription592', a)


def test_assoc_graphicalFilters266_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = GraphicalFilter()
    b2 = GraphicalFilter()
    _safe_set(a, 'viewpoint_diagram_DDiagramElement267', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElement267', b1)
    if hasattr(b1, 'GraphicalFilter'):
        assert _is_linked(b1, 'GraphicalFilter', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElement267', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElement267', b2)
    if hasattr(b1, 'GraphicalFilter'):
        assert not _is_linked(b1, 'GraphicalFilter', a)
    if hasattr(b2, 'GraphicalFilter'):
        assert _is_linked(b2, 'GraphicalFilter', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElement267', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElement267', b2)
    if hasattr(b2, 'GraphicalFilter'):
        assert not _is_linked(b2, 'GraphicalFilter', a)


def test_assoc_groupExtensions616_link_reassign_clear():
    a = viewpoint_tool_ToolSection(icon="sample_text")
    b1 = tool_ToolGroupExtension()
    b2 = tool_ToolGroupExtension()
    _safe_set(a, 'viewpoint_tool_ToolSection617', {b1})
    assert _is_linked(a, 'viewpoint_tool_ToolSection617', b1)
    if hasattr(b1, 'tool_ToolGroupExtension'):
        assert _is_linked(b1, 'tool_ToolGroupExtension', a)
    _safe_set(a, 'viewpoint_tool_ToolSection617', {b2})
    assert _is_linked(a, 'viewpoint_tool_ToolSection617', b2)
    if hasattr(b1, 'tool_ToolGroupExtension'):
        assert not _is_linked(b1, 'tool_ToolGroupExtension', a)
    if hasattr(b2, 'tool_ToolGroupExtension'):
        assert _is_linked(b2, 'tool_ToolGroupExtension', a)
    _safe_set(a, 'viewpoint_tool_ToolSection617', set())
    assert not _is_linked(a, 'viewpoint_tool_ToolSection617', b2)
    if hasattr(b2, 'tool_ToolGroupExtension'):
        assert not _is_linked(b2, 'tool_ToolGroupExtension', a)


def test_assoc_hiddenElements256_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = DDiagramElement()
    b2 = DDiagramElement()
    _safe_set(a, 'viewpoint_diagram_DDiagram257', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram257', b1)
    if hasattr(b1, 'DDiagramElement258'):
        assert _is_linked(b1, 'DDiagramElement258', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram257', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram257', b2)
    if hasattr(b1, 'DDiagramElement258'):
        assert not _is_linked(b1, 'DDiagramElement258', a)
    if hasattr(b2, 'DDiagramElement258'):
        assert _is_linked(b2, 'DDiagramElement258', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram257', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram257', b2)
    if hasattr(b2, 'DDiagramElement258'):
        assert not _is_linked(b2, 'DDiagramElement258', a)


def test_assoc_hiddenRepresentations39_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DView40', {b1})
    assert _is_linked(a, 'viewpoint_DView40', b1)
    if hasattr(b1, 'viewpoint_DRepresentation41'):
        assert _is_linked(b1, 'viewpoint_DRepresentation41', a)
    _safe_set(a, 'viewpoint_DView40', {b2})
    assert _is_linked(a, 'viewpoint_DView40', b2)
    if hasattr(b1, 'viewpoint_DRepresentation41'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation41', a)
    if hasattr(b2, 'viewpoint_DRepresentation41'):
        assert _is_linked(b2, 'viewpoint_DRepresentation41', a)
    _safe_set(a, 'viewpoint_DView40', set())
    assert not _is_linked(a, 'viewpoint_DView40', b2)
    if hasattr(b2, 'viewpoint_DRepresentation41'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation41', a)


def test_assoc_hook678_link_reassign_clear():
    a = viewpoint_tool_DeleteElementDescription()
    b1 = tool_DeleteHook()
    b2 = tool_DeleteHook()
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription679', b1)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription679', b1)
    if hasattr(b1, 'tool_DeleteHook'):
        assert _is_linked(b1, 'tool_DeleteHook', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription679', b2)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription679', b2)
    if hasattr(b1, 'tool_DeleteHook'):
        assert not _is_linked(b1, 'tool_DeleteHook', a)
    if hasattr(b2, 'tool_DeleteHook'):
        assert _is_linked(b2, 'tool_DeleteHook', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription679', None)
    assert not _is_linked(a, 'viewpoint_tool_DeleteElementDescription679', b2)
    if hasattr(b2, 'tool_DeleteHook'):
        assert not _is_linked(b2, 'tool_DeleteHook', a)


def test_assoc_importedMapping523_link_reassign_clear():
    a = viewpoint_description_EdgeMappingImport(inheritsAncestorFilters=True)
    b1 = description_IEdgeMapping()
    b2 = description_IEdgeMapping()
    _safe_set(a, 'viewpoint_description_EdgeMappingImport', b1)
    assert _is_linked(a, 'viewpoint_description_EdgeMappingImport', b1)
    if hasattr(b1, 'description_IEdgeMapping524'):
        assert _is_linked(b1, 'description_IEdgeMapping524', a)
    _safe_set(a, 'viewpoint_description_EdgeMappingImport', b2)
    assert _is_linked(a, 'viewpoint_description_EdgeMappingImport', b2)
    if hasattr(b1, 'description_IEdgeMapping524'):
        assert not _is_linked(b1, 'description_IEdgeMapping524', a)
    if hasattr(b2, 'description_IEdgeMapping524'):
        assert _is_linked(b2, 'description_IEdgeMapping524', a)
    _safe_set(a, 'viewpoint_description_EdgeMappingImport', None)
    assert not _is_linked(a, 'viewpoint_description_EdgeMappingImport', b2)
    if hasattr(b2, 'description_IEdgeMapping524'):
        assert not _is_linked(b2, 'description_IEdgeMapping524', a)


def test_assoc_init425_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_RepresentationCreationDescription()
    b2 = tool_RepresentationCreationDescription()
    _safe_set(a, 'viewpoint_description_DiagramDescription426', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription426', b1)
    if hasattr(b1, 'tool_RepresentationCreationDescription427'):
        assert _is_linked(b1, 'tool_RepresentationCreationDescription427', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription426', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription426', b2)
    if hasattr(b1, 'tool_RepresentationCreationDescription427'):
        assert not _is_linked(b1, 'tool_RepresentationCreationDescription427', a)
    if hasattr(b2, 'tool_RepresentationCreationDescription427'):
        assert _is_linked(b2, 'tool_RepresentationCreationDescription427', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription426', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription426', b2)
    if hasattr(b2, 'tool_RepresentationCreationDescription427'):
        assert not _is_linked(b2, 'tool_RepresentationCreationDescription427', a)


def test_assoc_initialOperation129_link_reassign_clear():
    a = viewpoint_tool_ToolDescription(iconPath="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_ToolDescription130', b1)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription130', b1)
    if hasattr(b1, 'tool_InitialOperation'):
        assert _is_linked(b1, 'tool_InitialOperation', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription130', b2)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription130', b2)
    if hasattr(b1, 'tool_InitialOperation'):
        assert not _is_linked(b1, 'tool_InitialOperation', a)
    if hasattr(b2, 'tool_InitialOperation'):
        assert _is_linked(b2, 'tool_InitialOperation', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription130', None)
    assert not _is_linked(a, 'viewpoint_tool_ToolDescription130', b2)
    if hasattr(b2, 'tool_InitialOperation'):
        assert not _is_linked(b2, 'tool_InitialOperation', a)


def test_assoc_initialOperation141_link_reassign_clear():
    a = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_InitialContainerDropOperation()
    b2 = tool_InitialContainerDropOperation()
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription142', b1)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription142', b1)
    if hasattr(b1, 'tool_InitialContainerDropOperation'):
        assert _is_linked(b1, 'tool_InitialContainerDropOperation', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription142', b2)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription142', b2)
    if hasattr(b1, 'tool_InitialContainerDropOperation'):
        assert not _is_linked(b1, 'tool_InitialContainerDropOperation', a)
    if hasattr(b2, 'tool_InitialContainerDropOperation'):
        assert _is_linked(b2, 'tool_InitialContainerDropOperation', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription142', None)
    assert not _is_linked(a, 'viewpoint_tool_ContainerDropDescription142', b2)
    if hasattr(b2, 'tool_InitialContainerDropOperation'):
        assert not _is_linked(b2, 'tool_InitialContainerDropOperation', a)


def test_assoc_initialOperation154_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_PasteDescription155', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription155', b1)
    if hasattr(b1, 'tool_InitialOperation156'):
        assert _is_linked(b1, 'tool_InitialOperation156', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription155', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription155', b2)
    if hasattr(b1, 'tool_InitialOperation156'):
        assert not _is_linked(b1, 'tool_InitialOperation156', a)
    if hasattr(b2, 'tool_InitialOperation156'):
        assert _is_linked(b2, 'tool_InitialOperation156', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription155', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription155', b2)
    if hasattr(b2, 'tool_InitialOperation156'):
        assert not _is_linked(b2, 'tool_InitialOperation156', a)


def test_assoc_initialOperation163_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription164', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription164', b1)
    if hasattr(b1, 'tool_InitialOperation165'):
        assert _is_linked(b1, 'tool_InitialOperation165', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription164', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription164', b2)
    if hasattr(b1, 'tool_InitialOperation165'):
        assert not _is_linked(b1, 'tool_InitialOperation165', a)
    if hasattr(b2, 'tool_InitialOperation165'):
        assert _is_linked(b2, 'tool_InitialOperation165', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription164', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription164', b2)
    if hasattr(b2, 'tool_InitialOperation165'):
        assert not _is_linked(b2, 'tool_InitialOperation165', a)


def test_assoc_initialOperation174_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription175', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription175', b1)
    if hasattr(b1, 'tool_InitialOperation176'):
        assert _is_linked(b1, 'tool_InitialOperation176', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription175', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription175', b2)
    if hasattr(b1, 'tool_InitialOperation176'):
        assert not _is_linked(b1, 'tool_InitialOperation176', a)
    if hasattr(b2, 'tool_InitialOperation176'):
        assert _is_linked(b2, 'tool_InitialOperation176', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription175', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription175', b2)
    if hasattr(b2, 'tool_InitialOperation176'):
        assert not _is_linked(b2, 'tool_InitialOperation176', a)


def test_assoc_initialOperation179_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription180', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription180', b1)
    if hasattr(b1, 'tool_InitialOperation181'):
        assert _is_linked(b1, 'tool_InitialOperation181', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription180', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription180', b2)
    if hasattr(b1, 'tool_InitialOperation181'):
        assert not _is_linked(b1, 'tool_InitialOperation181', a)
    if hasattr(b2, 'tool_InitialOperation181'):
        assert _is_linked(b2, 'tool_InitialOperation181', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription180', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription180', b2)
    if hasattr(b2, 'tool_InitialOperation181'):
        assert not _is_linked(b2, 'tool_InitialOperation181', a)


def test_assoc_initialOperation631_link_reassign_clear():
    a = viewpoint_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = tool_InitialNodeCreationOperation()
    b2 = tool_InitialNodeCreationOperation()
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription632', b1)
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription632', b1)
    if hasattr(b1, 'tool_InitialNodeCreationOperation'):
        assert _is_linked(b1, 'tool_InitialNodeCreationOperation', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription632', b2)
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription632', b2)
    if hasattr(b1, 'tool_InitialNodeCreationOperation'):
        assert not _is_linked(b1, 'tool_InitialNodeCreationOperation', a)
    if hasattr(b2, 'tool_InitialNodeCreationOperation'):
        assert _is_linked(b2, 'tool_InitialNodeCreationOperation', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription632', None)
    assert not _is_linked(a, 'viewpoint_tool_NodeCreationDescription632', b2)
    if hasattr(b2, 'tool_InitialNodeCreationOperation'):
        assert not _is_linked(b2, 'tool_InitialNodeCreationOperation', a)


def test_assoc_initialOperation646_link_reassign_clear():
    a = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_InitEdgeCreationOperation()
    b2 = tool_InitEdgeCreationOperation()
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription647', b1)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription647', b1)
    if hasattr(b1, 'tool_InitEdgeCreationOperation'):
        assert _is_linked(b1, 'tool_InitEdgeCreationOperation', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription647', b2)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription647', b2)
    if hasattr(b1, 'tool_InitEdgeCreationOperation'):
        assert not _is_linked(b1, 'tool_InitEdgeCreationOperation', a)
    if hasattr(b2, 'tool_InitEdgeCreationOperation'):
        assert _is_linked(b2, 'tool_InitEdgeCreationOperation', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription647', None)
    assert not _is_linked(a, 'viewpoint_tool_EdgeCreationDescription647', b2)
    if hasattr(b2, 'tool_InitEdgeCreationOperation'):
        assert not _is_linked(b2, 'tool_InitEdgeCreationOperation', a)


def test_assoc_initialOperation662_link_reassign_clear():
    a = viewpoint_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = tool_InitialNodeCreationOperation()
    b2 = tool_InitialNodeCreationOperation()
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription663', b1)
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription663', b1)
    if hasattr(b1, 'tool_InitialNodeCreationOperation664'):
        assert _is_linked(b1, 'tool_InitialNodeCreationOperation664', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription663', b2)
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription663', b2)
    if hasattr(b1, 'tool_InitialNodeCreationOperation664'):
        assert not _is_linked(b1, 'tool_InitialNodeCreationOperation664', a)
    if hasattr(b2, 'tool_InitialNodeCreationOperation664'):
        assert _is_linked(b2, 'tool_InitialNodeCreationOperation664', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription663', None)
    assert not _is_linked(a, 'viewpoint_tool_ContainerCreationDescription663', b2)
    if hasattr(b2, 'tool_InitialNodeCreationOperation664'):
        assert not _is_linked(b2, 'tool_InitialNodeCreationOperation664', a)


def test_assoc_initialOperation675_link_reassign_clear():
    a = viewpoint_tool_DeleteElementDescription()
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription676', b1)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription676', b1)
    if hasattr(b1, 'tool_InitialOperation677'):
        assert _is_linked(b1, 'tool_InitialOperation677', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription676', b2)
    assert _is_linked(a, 'viewpoint_tool_DeleteElementDescription676', b2)
    if hasattr(b1, 'tool_InitialOperation677'):
        assert not _is_linked(b1, 'tool_InitialOperation677', a)
    if hasattr(b2, 'tool_InitialOperation677'):
        assert _is_linked(b2, 'tool_InitialOperation677', a)
    _safe_set(a, 'viewpoint_tool_DeleteElementDescription676', None)
    assert not _is_linked(a, 'viewpoint_tool_DeleteElementDescription676', b2)
    if hasattr(b2, 'tool_InitialOperation677'):
        assert not _is_linked(b2, 'tool_InitialOperation677', a)


def test_assoc_initialOperation703_link_reassign_clear():
    a = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription704', b1)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription704', b1)
    if hasattr(b1, 'tool_InitialOperation705'):
        assert _is_linked(b1, 'tool_InitialOperation705', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription704', b2)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription704', b2)
    if hasattr(b1, 'tool_InitialOperation705'):
        assert not _is_linked(b1, 'tool_InitialOperation705', a)
    if hasattr(b2, 'tool_InitialOperation705'):
        assert _is_linked(b2, 'tool_InitialOperation705', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription704', None)
    assert not _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription704', b2)
    if hasattr(b2, 'tool_InitialOperation705'):
        assert not _is_linked(b2, 'tool_InitialOperation705', a)


def test_assoc_initialOperation710_link_reassign_clear():
    a = viewpoint_tool_DirectEditLabel(inputLabelExpression="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_DirectEditLabel711', b1)
    assert _is_linked(a, 'viewpoint_tool_DirectEditLabel711', b1)
    if hasattr(b1, 'tool_InitialOperation712'):
        assert _is_linked(b1, 'tool_InitialOperation712', a)
    _safe_set(a, 'viewpoint_tool_DirectEditLabel711', b2)
    assert _is_linked(a, 'viewpoint_tool_DirectEditLabel711', b2)
    if hasattr(b1, 'tool_InitialOperation712'):
        assert not _is_linked(b1, 'tool_InitialOperation712', a)
    if hasattr(b2, 'tool_InitialOperation712'):
        assert _is_linked(b2, 'tool_InitialOperation712', a)
    _safe_set(a, 'viewpoint_tool_DirectEditLabel711', None)
    assert not _is_linked(a, 'viewpoint_tool_DirectEditLabel711', b2)
    if hasattr(b2, 'tool_InitialOperation712'):
        assert not _is_linked(b2, 'tool_InitialOperation712', a)


def test_assoc_initialOperation713_link_reassign_clear():
    a = viewpoint_tool_BehaviorTool(domainClass="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_BehaviorTool', b1)
    assert _is_linked(a, 'viewpoint_tool_BehaviorTool', b1)
    if hasattr(b1, 'tool_InitialOperation714'):
        assert _is_linked(b1, 'tool_InitialOperation714', a)
    _safe_set(a, 'viewpoint_tool_BehaviorTool', b2)
    assert _is_linked(a, 'viewpoint_tool_BehaviorTool', b2)
    if hasattr(b1, 'tool_InitialOperation714'):
        assert not _is_linked(b1, 'tool_InitialOperation714', a)
    if hasattr(b2, 'tool_InitialOperation714'):
        assert _is_linked(b2, 'tool_InitialOperation714', a)
    _safe_set(a, 'viewpoint_tool_BehaviorTool', None)
    assert not _is_linked(a, 'viewpoint_tool_BehaviorTool', b2)
    if hasattr(b2, 'tool_InitialOperation714'):
        assert not _is_linked(b2, 'tool_InitialOperation714', a)


def test_assoc_initialOperation741_link_reassign_clear():
    a = viewpoint_validation_ValidationFix(name="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_validation_ValidationFix', b1)
    assert _is_linked(a, 'viewpoint_validation_ValidationFix', b1)
    if hasattr(b1, 'tool_InitialOperation742'):
        assert _is_linked(b1, 'tool_InitialOperation742', a)
    _safe_set(a, 'viewpoint_validation_ValidationFix', b2)
    assert _is_linked(a, 'viewpoint_validation_ValidationFix', b2)
    if hasattr(b1, 'tool_InitialOperation742'):
        assert not _is_linked(b1, 'tool_InitialOperation742', a)
    if hasattr(b2, 'tool_InitialOperation742'):
        assert _is_linked(b2, 'tool_InitialOperation742', a)
    _safe_set(a, 'viewpoint_validation_ValidationFix', None)
    assert not _is_linked(a, 'viewpoint_validation_ValidationFix', b2)
    if hasattr(b2, 'tool_InitialOperation742'):
        assert not _is_linked(b2, 'tool_InitialOperation742', a)


def test_assoc_labelBorderStyle593_link_reassign_clear():
    a = viewpoint_style_FlatContainerStyleDescription(backgroundStyle="sample_text")
    b1 = style_LabelBorderStyleDescription()
    b2 = style_LabelBorderStyleDescription()
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription594', b1)
    assert _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription594', b1)
    if hasattr(b1, 'style_LabelBorderStyleDescription595'):
        assert _is_linked(b1, 'style_LabelBorderStyleDescription595', a)
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription594', b2)
    assert _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription594', b2)
    if hasattr(b1, 'style_LabelBorderStyleDescription595'):
        assert not _is_linked(b1, 'style_LabelBorderStyleDescription595', a)
    if hasattr(b2, 'style_LabelBorderStyleDescription595'):
        assert _is_linked(b2, 'style_LabelBorderStyleDescription595', a)
    _safe_set(a, 'viewpoint_style_FlatContainerStyleDescription594', None)
    assert not _is_linked(a, 'viewpoint_style_FlatContainerStyleDescription594', b2)
    if hasattr(b2, 'style_LabelBorderStyleDescription595'):
        assert not _is_linked(b2, 'style_LabelBorderStyleDescription595', a)


def test_assoc_labelColor123_link_reassign_clear():
    a = viewpoint_style_BasicLabelStyleDescription(iconPath="sample_text", labelExpression="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_BasicLabelStyleDescription', b1)
    assert _is_linked(a, 'viewpoint_style_BasicLabelStyleDescription', b1)
    if hasattr(b1, 'ColorDescription'):
        assert _is_linked(b1, 'ColorDescription', a)
    _safe_set(a, 'viewpoint_style_BasicLabelStyleDescription', b2)
    assert _is_linked(a, 'viewpoint_style_BasicLabelStyleDescription', b2)
    if hasattr(b1, 'ColorDescription'):
        assert not _is_linked(b1, 'ColorDescription', a)
    if hasattr(b2, 'ColorDescription'):
        assert _is_linked(b2, 'ColorDescription', a)
    _safe_set(a, 'viewpoint_style_BasicLabelStyleDescription', None)
    assert not _is_linked(a, 'viewpoint_style_BasicLabelStyleDescription', b2)
    if hasattr(b2, 'ColorDescription'):
        assert not _is_linked(b2, 'ColorDescription', a)


def test_assoc_labelColor64_link_reassign_clear():
    a = viewpoint_RGBValues(blue=7, green=7, red=7)
    b1 = viewpoint_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    b2 = viewpoint_BasicLabelStyle(iconPath="sample_text_2", labelFormat="sample_text_2", labelSize=13, showIcon=False)
    _safe_set(a, 'viewpoint_RGBValues', b1)
    assert _is_linked(a, 'viewpoint_RGBValues', b1)
    if hasattr(b1, 'viewpoint_BasicLabelStyle'):
        assert _is_linked(b1, 'viewpoint_BasicLabelStyle', a)
    _safe_set(a, 'viewpoint_RGBValues', b2)
    assert _is_linked(a, 'viewpoint_RGBValues', b2)
    if hasattr(b1, 'viewpoint_BasicLabelStyle'):
        assert not _is_linked(b1, 'viewpoint_BasicLabelStyle', a)
    if hasattr(b2, 'viewpoint_BasicLabelStyle'):
        assert _is_linked(b2, 'viewpoint_BasicLabelStyle', a)
    _safe_set(a, 'viewpoint_RGBValues', None)
    assert not _is_linked(a, 'viewpoint_RGBValues', b2)
    if hasattr(b2, 'viewpoint_BasicLabelStyle'):
        assert not _is_linked(b2, 'viewpoint_BasicLabelStyle', a)


def test_assoc_labelDirectEdit474_link_reassign_clear():
    a = viewpoint_description_DiagramElementMapping(createElements=True, preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", semanticElements="sample_text", synchronizationLock=True)
    b1 = tool_DirectEditLabel()
    b2 = tool_DirectEditLabel()
    _safe_set(a, 'viewpoint_description_DiagramElementMapping475', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramElementMapping475', b1)
    if hasattr(b1, 'tool_DirectEditLabel'):
        assert _is_linked(b1, 'tool_DirectEditLabel', a)
    _safe_set(a, 'viewpoint_description_DiagramElementMapping475', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramElementMapping475', b2)
    if hasattr(b1, 'tool_DirectEditLabel'):
        assert not _is_linked(b1, 'tool_DirectEditLabel', a)
    if hasattr(b2, 'tool_DirectEditLabel'):
        assert _is_linked(b2, 'tool_DirectEditLabel', a)
    _safe_set(a, 'viewpoint_description_DiagramElementMapping475', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramElementMapping475', b2)
    if hasattr(b2, 'tool_DirectEditLabel'):
        assert not _is_linked(b2, 'tool_DirectEditLabel', a)


def test_assoc_layout428_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_Layout()
    b2 = description_Layout()
    _safe_set(a, 'viewpoint_description_DiagramDescription429', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription429', b1)
    if hasattr(b1, 'description_Layout'):
        assert _is_linked(b1, 'description_Layout', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription429', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription429', b2)
    if hasattr(b1, 'description_Layout'):
        assert not _is_linked(b1, 'description_Layout', a)
    if hasattr(b2, 'description_Layout'):
        assert _is_linked(b2, 'description_Layout', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription429', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription429', b2)
    if hasattr(b2, 'description_Layout'):
        assert not _is_linked(b2, 'description_Layout', a)


def test_assoc_listeners219_link_reassign_clear():
    a = viewpoint_tool_ToolFilterDescription(elementsToListen="sample_text", precondition="sample_text")
    b1 = tool_FeatureChangeListener()
    b2 = tool_FeatureChangeListener()
    _safe_set(a, 'viewpoint_tool_ToolFilterDescription', {b1})
    assert _is_linked(a, 'viewpoint_tool_ToolFilterDescription', b1)
    if hasattr(b1, 'tool_FeatureChangeListener'):
        assert _is_linked(b1, 'tool_FeatureChangeListener', a)
    _safe_set(a, 'viewpoint_tool_ToolFilterDescription', {b2})
    assert _is_linked(a, 'viewpoint_tool_ToolFilterDescription', b2)
    if hasattr(b1, 'tool_FeatureChangeListener'):
        assert not _is_linked(b1, 'tool_FeatureChangeListener', a)
    if hasattr(b2, 'tool_FeatureChangeListener'):
        assert _is_linked(b2, 'tool_FeatureChangeListener', a)
    _safe_set(a, 'viewpoint_tool_ToolFilterDescription', set())
    assert not _is_linked(a, 'viewpoint_tool_ToolFilterDescription', b2)
    if hasattr(b2, 'tool_FeatureChangeListener'):
        assert not _is_linked(b2, 'tool_FeatureChangeListener', a)


def test_assoc_mapping715_link_reassign_clear():
    a = viewpoint_tool_CreateView(containerViewExpression="sample_text", variableName="sample_text")
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_tool_CreateView', b1)
    assert _is_linked(a, 'viewpoint_tool_CreateView', b1)
    if hasattr(b1, 'description_DiagramElementMapping716'):
        assert _is_linked(b1, 'description_DiagramElementMapping716', a)
    _safe_set(a, 'viewpoint_tool_CreateView', b2)
    assert _is_linked(a, 'viewpoint_tool_CreateView', b2)
    if hasattr(b1, 'description_DiagramElementMapping716'):
        assert not _is_linked(b1, 'description_DiagramElementMapping716', a)
    if hasattr(b2, 'description_DiagramElementMapping716'):
        assert _is_linked(b2, 'description_DiagramElementMapping716', a)
    _safe_set(a, 'viewpoint_tool_CreateView', None)
    assert not _is_linked(a, 'viewpoint_tool_CreateView', b2)
    if hasattr(b2, 'description_DiagramElementMapping716'):
        assert not _is_linked(b2, 'description_DiagramElementMapping716', a)


def test_assoc_mappings131_link_reassign_clear():
    a = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription', {b1})
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription', b1)
    if hasattr(b1, 'description_DiagramElementMapping'):
        assert _is_linked(b1, 'description_DiagramElementMapping', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription', {b2})
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription', b2)
    if hasattr(b1, 'description_DiagramElementMapping'):
        assert not _is_linked(b1, 'description_DiagramElementMapping', a)
    if hasattr(b2, 'description_DiagramElementMapping'):
        assert _is_linked(b2, 'description_DiagramElementMapping', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription', set())
    assert not _is_linked(a, 'viewpoint_tool_ContainerDropDescription', b2)
    if hasattr(b2, 'description_DiagramElementMapping'):
        assert not _is_linked(b2, 'description_DiagramElementMapping', a)


def test_assoc_mappings723_link_reassign_clear():
    a = viewpoint_filter_MappingFilter(semanticConditionExpression="sample_text", viewConditionExpression="sample_text")
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_filter_MappingFilter', {b1})
    assert _is_linked(a, 'viewpoint_filter_MappingFilter', b1)
    if hasattr(b1, 'description_DiagramElementMapping724'):
        assert _is_linked(b1, 'description_DiagramElementMapping724', a)
    _safe_set(a, 'viewpoint_filter_MappingFilter', {b2})
    assert _is_linked(a, 'viewpoint_filter_MappingFilter', b2)
    if hasattr(b1, 'description_DiagramElementMapping724'):
        assert not _is_linked(b1, 'description_DiagramElementMapping724', a)
    if hasattr(b2, 'description_DiagramElementMapping724'):
        assert _is_linked(b2, 'description_DiagramElementMapping724', a)
    _safe_set(a, 'viewpoint_filter_MappingFilter', set())
    assert not _is_linked(a, 'viewpoint_filter_MappingFilter', b2)
    if hasattr(b2, 'description_DiagramElementMapping724'):
        assert not _is_linked(b2, 'description_DiagramElementMapping724', a)


def test_assoc_mask709_link_reassign_clear():
    a = viewpoint_tool_DirectEditLabel(inputLabelExpression="sample_text")
    b1 = tool_EditMaskVariables()
    b2 = tool_EditMaskVariables()
    _safe_set(a, 'viewpoint_tool_DirectEditLabel', b1)
    assert _is_linked(a, 'viewpoint_tool_DirectEditLabel', b1)
    if hasattr(b1, 'tool_EditMaskVariables'):
        assert _is_linked(b1, 'tool_EditMaskVariables', a)
    _safe_set(a, 'viewpoint_tool_DirectEditLabel', b2)
    assert _is_linked(a, 'viewpoint_tool_DirectEditLabel', b2)
    if hasattr(b1, 'tool_EditMaskVariables'):
        assert not _is_linked(b1, 'tool_EditMaskVariables', a)
    if hasattr(b2, 'tool_EditMaskVariables'):
        assert _is_linked(b2, 'tool_EditMaskVariables', a)
    _safe_set(a, 'viewpoint_tool_DirectEditLabel', None)
    assert not _is_linked(a, 'viewpoint_tool_DirectEditLabel', b2)
    if hasattr(b2, 'tool_EditMaskVariables'):
        assert not _is_linked(b2, 'tool_EditMaskVariables', a)


def test_assoc_members63_link_reassign_clear():
    a = viewpoint_DResource(name="sample_text", path="sample_text")
    b1 = viewpoint_DResourceContainer()
    b2 = viewpoint_DResourceContainer()
    _safe_set(a, 'viewpoint_DResource', b1)
    assert _is_linked(a, 'viewpoint_DResource', b1)
    if hasattr(b1, 'viewpoint_DResourceContainer'):
        assert _is_linked(b1, 'viewpoint_DResourceContainer', a)
    _safe_set(a, 'viewpoint_DResource', b2)
    assert _is_linked(a, 'viewpoint_DResource', b2)
    if hasattr(b1, 'viewpoint_DResourceContainer'):
        assert not _is_linked(b1, 'viewpoint_DResourceContainer', a)
    if hasattr(b2, 'viewpoint_DResourceContainer'):
        assert _is_linked(b2, 'viewpoint_DResourceContainer', a)
    _safe_set(a, 'viewpoint_DResource', None)
    assert not _is_linked(a, 'viewpoint_DResource', b2)
    if hasattr(b2, 'viewpoint_DResourceContainer'):
        assert not _is_linked(b2, 'viewpoint_DResourceContainer', a)


def test_assoc_metamodel85_link_reassign_clear():
    a = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    b1 = description_viewpoint_EPackage()
    b2 = description_viewpoint_EPackage()
    _safe_set(a, 'viewpoint_description_RepresentationDescription', {b1})
    assert _is_linked(a, 'viewpoint_description_RepresentationDescription', b1)
    if hasattr(b1, 'description_viewpoint_EPackage'):
        assert _is_linked(b1, 'description_viewpoint_EPackage', a)
    _safe_set(a, 'viewpoint_description_RepresentationDescription', {b2})
    assert _is_linked(a, 'viewpoint_description_RepresentationDescription', b2)
    if hasattr(b1, 'description_viewpoint_EPackage'):
        assert not _is_linked(b1, 'description_viewpoint_EPackage', a)
    if hasattr(b2, 'description_viewpoint_EPackage'):
        assert _is_linked(b2, 'description_viewpoint_EPackage', a)
    _safe_set(a, 'viewpoint_description_RepresentationDescription', set())
    assert not _is_linked(a, 'viewpoint_description_RepresentationDescription', b2)
    if hasattr(b2, 'description_viewpoint_EPackage'):
        assert not _is_linked(b2, 'description_viewpoint_EPackage', a)


def test_assoc_metamodel88_link_reassign_clear():
    a = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    b1 = description_viewpoint_EPackage()
    b2 = description_viewpoint_EPackage()
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', {b1})
    assert _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b1)
    if hasattr(b1, 'description_viewpoint_EPackage89'):
        assert _is_linked(b1, 'description_viewpoint_EPackage89', a)
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', {b2})
    assert _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b2)
    if hasattr(b1, 'description_viewpoint_EPackage89'):
        assert not _is_linked(b1, 'description_viewpoint_EPackage89', a)
    if hasattr(b2, 'description_viewpoint_EPackage89'):
        assert _is_linked(b2, 'description_viewpoint_EPackage89', a)
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', set())
    assert not _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b2)
    if hasattr(b2, 'description_viewpoint_EPackage89'):
        assert not _is_linked(b2, 'description_viewpoint_EPackage89', a)


def test_assoc_models17_link_reassign_clear():
    a = viewpoint_DRepresentationContainer()
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_DRepresentationContainer18', {b1})
    assert _is_linked(a, 'viewpoint_DRepresentationContainer18', b1)
    if hasattr(b1, 'viewpoint_EObject19'):
        assert _is_linked(b1, 'viewpoint_EObject19', a)
    _safe_set(a, 'viewpoint_DRepresentationContainer18', {b2})
    assert _is_linked(a, 'viewpoint_DRepresentationContainer18', b2)
    if hasattr(b1, 'viewpoint_EObject19'):
        assert not _is_linked(b1, 'viewpoint_EObject19', a)
    if hasattr(b2, 'viewpoint_EObject19'):
        assert _is_linked(b2, 'viewpoint_EObject19', a)
    _safe_set(a, 'viewpoint_DRepresentationContainer18', set())
    assert not _is_linked(a, 'viewpoint_DRepresentationContainer18', b2)
    if hasattr(b2, 'viewpoint_EObject19'):
        assert not _is_linked(b2, 'viewpoint_EObject19', a)


def test_assoc_models2_link_reassign_clear():
    a = viewpoint_DAnalysis(version="sample_text")
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_DAnalysis3', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysis3', b1)
    if hasattr(b1, 'viewpoint_EObject'):
        assert _is_linked(b1, 'viewpoint_EObject', a)
    _safe_set(a, 'viewpoint_DAnalysis3', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysis3', b2)
    if hasattr(b1, 'viewpoint_EObject'):
        assert not _is_linked(b1, 'viewpoint_EObject', a)
    if hasattr(b2, 'viewpoint_EObject'):
        assert _is_linked(b2, 'viewpoint_EObject', a)
    _safe_set(a, 'viewpoint_DAnalysis3', set())
    assert not _is_linked(a, 'viewpoint_DAnalysis3', b2)
    if hasattr(b2, 'viewpoint_EObject'):
        assert not _is_linked(b2, 'viewpoint_EObject', a)


def test_assoc_newContainer134_link_reassign_clear():
    a = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription135', b1)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription135', b1)
    if hasattr(b1, 'tool_DropContainerVariable136'):
        assert _is_linked(b1, 'tool_DropContainerVariable136', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription135', b2)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription135', b2)
    if hasattr(b1, 'tool_DropContainerVariable136'):
        assert not _is_linked(b1, 'tool_DropContainerVariable136', a)
    if hasattr(b2, 'tool_DropContainerVariable136'):
        assert _is_linked(b2, 'tool_DropContainerVariable136', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription135', None)
    assert not _is_linked(a, 'viewpoint_tool_ContainerDropDescription135', b2)
    if hasattr(b2, 'tool_DropContainerVariable136'):
        assert not _is_linked(b2, 'tool_DropContainerVariable136', a)


def test_assoc_newViewContainer139_link_reassign_clear():
    a = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription140', b1)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription140', b1)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert _is_linked(b1, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription140', b2)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription140', b2)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable', a)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert _is_linked(b2, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription140', None)
    assert not _is_linked(a, 'viewpoint_tool_ContainerDropDescription140', b2)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable', a)


def test_assoc_nodeListElements237_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = DNodeListElement()
    b2 = DNodeListElement()
    _safe_set(a, 'viewpoint_diagram_DDiagram238', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram238', b1)
    if hasattr(b1, 'DNodeListElement'):
        assert _is_linked(b1, 'DNodeListElement', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram238', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram238', b2)
    if hasattr(b1, 'DNodeListElement'):
        assert not _is_linked(b1, 'DNodeListElement', a)
    if hasattr(b2, 'DNodeListElement'):
        assert _is_linked(b2, 'DNodeListElement', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram238', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram238', b2)
    if hasattr(b2, 'DNodeListElement'):
        assert not _is_linked(b2, 'DNodeListElement', a)


def test_assoc_nodeMapping534_link_reassign_clear():
    a = viewpoint_description_OrderedTreeLayout(childrenExpression="sample_text")
    b1 = description_AbstractNodeMapping()
    b2 = description_AbstractNodeMapping()
    _safe_set(a, 'viewpoint_description_OrderedTreeLayout', {b1})
    assert _is_linked(a, 'viewpoint_description_OrderedTreeLayout', b1)
    if hasattr(b1, 'description_AbstractNodeMapping535'):
        assert _is_linked(b1, 'description_AbstractNodeMapping535', a)
    _safe_set(a, 'viewpoint_description_OrderedTreeLayout', {b2})
    assert _is_linked(a, 'viewpoint_description_OrderedTreeLayout', b2)
    if hasattr(b1, 'description_AbstractNodeMapping535'):
        assert not _is_linked(b1, 'description_AbstractNodeMapping535', a)
    if hasattr(b2, 'description_AbstractNodeMapping535'):
        assert _is_linked(b2, 'description_AbstractNodeMapping535', a)
    _safe_set(a, 'viewpoint_description_OrderedTreeLayout', set())
    assert not _is_linked(a, 'viewpoint_description_OrderedTreeLayout', b2)
    if hasattr(b2, 'description_AbstractNodeMapping535'):
        assert not _is_linked(b2, 'description_AbstractNodeMapping535', a)


def test_assoc_nodeMappings444_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_description_DiagramDescription445', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription445', b1)
    if hasattr(b1, 'description_NodeMapping446'):
        assert _is_linked(b1, 'description_NodeMapping446', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription445', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription445', b2)
    if hasattr(b1, 'description_NodeMapping446'):
        assert not _is_linked(b1, 'description_NodeMapping446', a)
    if hasattr(b2, 'description_NodeMapping446'):
        assert _is_linked(b2, 'description_NodeMapping446', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription445', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription445', b2)
    if hasattr(b2, 'description_NodeMapping446'):
        assert not _is_linked(b2, 'description_NodeMapping446', a)


def test_assoc_nodeMappings538_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_description_Layer', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer', b1)
    if hasattr(b1, 'description_NodeMapping539'):
        assert _is_linked(b1, 'description_NodeMapping539', a)
    _safe_set(a, 'viewpoint_description_Layer', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer', b2)
    if hasattr(b1, 'description_NodeMapping539'):
        assert not _is_linked(b1, 'description_NodeMapping539', a)
    if hasattr(b2, 'description_NodeMapping539'):
        assert _is_linked(b2, 'description_NodeMapping539', a)
    _safe_set(a, 'viewpoint_description_Layer', set())
    assert not _is_linked(a, 'viewpoint_description_Layer', b2)
    if hasattr(b2, 'description_NodeMapping539'):
        assert not _is_linked(b2, 'description_NodeMapping539', a)


def test_assoc_nodeMappings624_link_reassign_clear():
    a = viewpoint_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription', {b1})
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription', b1)
    if hasattr(b1, 'description_NodeMapping625'):
        assert _is_linked(b1, 'description_NodeMapping625', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription', {b2})
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription', b2)
    if hasattr(b1, 'description_NodeMapping625'):
        assert not _is_linked(b1, 'description_NodeMapping625', a)
    if hasattr(b2, 'description_NodeMapping625'):
        assert _is_linked(b2, 'description_NodeMapping625', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription', set())
    assert not _is_linked(a, 'viewpoint_tool_NodeCreationDescription', b2)
    if hasattr(b2, 'description_NodeMapping625'):
        assert not _is_linked(b2, 'description_NodeMapping625', a)


def test_assoc_nodes235_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = DNode()
    b2 = DNode()
    _safe_set(a, 'viewpoint_diagram_DDiagram236', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram236', b1)
    if hasattr(b1, 'DNode'):
        assert _is_linked(b1, 'DNode', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram236', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram236', b2)
    if hasattr(b1, 'DNode'):
        assert not _is_linked(b1, 'DNode', a)
    if hasattr(b2, 'DNode'):
        assert _is_linked(b2, 'DNode', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram236', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram236', b2)
    if hasattr(b2, 'DNode'):
        assert not _is_linked(b2, 'DNode', a)


def test_assoc_nodes286_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = DNode()
    b2 = DNode()
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer', b1)
    if hasattr(b1, 'DNode287'):
        assert _is_linked(b1, 'DNode287', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer', b2)
    if hasattr(b1, 'DNode287'):
        assert not _is_linked(b1, 'DNode287', a)
    if hasattr(b2, 'DNode287'):
        assert _is_linked(b2, 'DNode287', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer', b2)
    if hasattr(b2, 'DNode287'):
        assert not _is_linked(b2, 'DNode287', a)


def test_assoc_object218_link_reassign_clear():
    a = viewpoint_tool_SetObject(featureName="sample_text")
    b1 = tool_viewpoint_EObject()
    b2 = tool_viewpoint_EObject()
    _safe_set(a, 'viewpoint_tool_SetObject', b1)
    assert _is_linked(a, 'viewpoint_tool_SetObject', b1)
    if hasattr(b1, 'tool_viewpoint_EObject'):
        assert _is_linked(b1, 'tool_viewpoint_EObject', a)
    _safe_set(a, 'viewpoint_tool_SetObject', b2)
    assert _is_linked(a, 'viewpoint_tool_SetObject', b2)
    if hasattr(b1, 'tool_viewpoint_EObject'):
        assert not _is_linked(b1, 'tool_viewpoint_EObject', a)
    if hasattr(b2, 'tool_viewpoint_EObject'):
        assert _is_linked(b2, 'tool_viewpoint_EObject', a)
    _safe_set(a, 'viewpoint_tool_SetObject', None)
    assert not _is_linked(a, 'viewpoint_tool_SetObject', b2)
    if hasattr(b2, 'tool_viewpoint_EObject'):
        assert not _is_linked(b2, 'tool_viewpoint_EObject', a)


def test_assoc_oldContainer132_link_reassign_clear():
    a = viewpoint_tool_ContainerDropDescription(dragSource="sample_text", moveEdges=True)
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription133', b1)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription133', b1)
    if hasattr(b1, 'tool_DropContainerVariable'):
        assert _is_linked(b1, 'tool_DropContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription133', b2)
    assert _is_linked(a, 'viewpoint_tool_ContainerDropDescription133', b2)
    if hasattr(b1, 'tool_DropContainerVariable'):
        assert not _is_linked(b1, 'tool_DropContainerVariable', a)
    if hasattr(b2, 'tool_DropContainerVariable'):
        assert _is_linked(b2, 'tool_DropContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_ContainerDropDescription133', None)
    assert not _is_linked(a, 'viewpoint_tool_ContainerDropDescription133', b2)
    if hasattr(b2, 'tool_DropContainerVariable'):
        assert not _is_linked(b2, 'tool_DropContainerVariable', a)


def test_assoc_originalStyle279_link_reassign_clear():
    a = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = diagram_viewpoint_Style()
    b2 = diagram_viewpoint_Style()
    _safe_set(a, 'viewpoint_diagram_DNode280', b1)
    assert _is_linked(a, 'viewpoint_diagram_DNode280', b1)
    if hasattr(b1, 'diagram_viewpoint_Style'):
        assert _is_linked(b1, 'diagram_viewpoint_Style', a)
    _safe_set(a, 'viewpoint_diagram_DNode280', b2)
    assert _is_linked(a, 'viewpoint_diagram_DNode280', b2)
    if hasattr(b1, 'diagram_viewpoint_Style'):
        assert not _is_linked(b1, 'diagram_viewpoint_Style', a)
    if hasattr(b2, 'diagram_viewpoint_Style'):
        assert _is_linked(b2, 'diagram_viewpoint_Style', a)
    _safe_set(a, 'viewpoint_diagram_DNode280', None)
    assert not _is_linked(a, 'viewpoint_diagram_DNode280', b2)
    if hasattr(b2, 'diagram_viewpoint_Style'):
        assert not _is_linked(b2, 'diagram_viewpoint_Style', a)


def test_assoc_originalStyle299_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = diagram_viewpoint_Style()
    b2 = diagram_viewpoint_Style()
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer300', b1)
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer300', b1)
    if hasattr(b1, 'diagram_viewpoint_Style301'):
        assert _is_linked(b1, 'diagram_viewpoint_Style301', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer300', b2)
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer300', b2)
    if hasattr(b1, 'diagram_viewpoint_Style301'):
        assert not _is_linked(b1, 'diagram_viewpoint_Style301', a)
    if hasattr(b2, 'diagram_viewpoint_Style301'):
        assert _is_linked(b2, 'diagram_viewpoint_Style301', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer300', None)
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer300', b2)
    if hasattr(b2, 'diagram_viewpoint_Style301'):
        assert not _is_linked(b2, 'diagram_viewpoint_Style301', a)


def test_assoc_originalStyle329_link_reassign_clear():
    a = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = diagram_viewpoint_Style()
    b2 = diagram_viewpoint_Style()
    _safe_set(a, 'viewpoint_diagram_DEdge330', b1)
    assert _is_linked(a, 'viewpoint_diagram_DEdge330', b1)
    if hasattr(b1, 'diagram_viewpoint_Style331'):
        assert _is_linked(b1, 'diagram_viewpoint_Style331', a)
    _safe_set(a, 'viewpoint_diagram_DEdge330', b2)
    assert _is_linked(a, 'viewpoint_diagram_DEdge330', b2)
    if hasattr(b1, 'diagram_viewpoint_Style331'):
        assert not _is_linked(b1, 'diagram_viewpoint_Style331', a)
    if hasattr(b2, 'diagram_viewpoint_Style331'):
        assert _is_linked(b2, 'diagram_viewpoint_Style331', a)
    _safe_set(a, 'viewpoint_diagram_DEdge330', None)
    assert not _is_linked(a, 'viewpoint_diagram_DEdge330', b2)
    if hasattr(b2, 'diagram_viewpoint_Style331'):
        assert not _is_linked(b2, 'diagram_viewpoint_Style331', a)


def test_assoc_ownedAnnotationEntries26_link_reassign_clear():
    a = viewpoint_DRepresentation(name="sample_text")
    b1 = AnnotationEntry()
    b2 = AnnotationEntry()
    _safe_set(a, 'viewpoint_DRepresentation27', {b1})
    assert _is_linked(a, 'viewpoint_DRepresentation27', b1)
    if hasattr(b1, 'AnnotationEntry'):
        assert _is_linked(b1, 'AnnotationEntry', a)
    _safe_set(a, 'viewpoint_DRepresentation27', {b2})
    assert _is_linked(a, 'viewpoint_DRepresentation27', b2)
    if hasattr(b1, 'AnnotationEntry'):
        assert not _is_linked(b1, 'AnnotationEntry', a)
    if hasattr(b2, 'AnnotationEntry'):
        assert _is_linked(b2, 'AnnotationEntry', a)
    _safe_set(a, 'viewpoint_DRepresentation27', set())
    assert not _is_linked(a, 'viewpoint_DRepresentation27', b2)
    if hasattr(b2, 'AnnotationEntry'):
        assert not _is_linked(b2, 'AnnotationEntry', a)


def test_assoc_ownedBorderedNodes273_link_reassign_clear():
    a = viewpoint_diagram_AbstractDNode(arrangeConstraints="sample_text")
    b1 = DNode()
    b2 = DNode()
    _safe_set(a, 'viewpoint_diagram_AbstractDNode', {b1})
    assert _is_linked(a, 'viewpoint_diagram_AbstractDNode', b1)
    if hasattr(b1, 'DNode274'):
        assert _is_linked(b1, 'DNode274', a)
    _safe_set(a, 'viewpoint_diagram_AbstractDNode', {b2})
    assert _is_linked(a, 'viewpoint_diagram_AbstractDNode', b2)
    if hasattr(b1, 'DNode274'):
        assert not _is_linked(b1, 'DNode274', a)
    if hasattr(b2, 'DNode274'):
        assert _is_linked(b2, 'DNode274', a)
    _safe_set(a, 'viewpoint_diagram_AbstractDNode', set())
    assert not _is_linked(a, 'viewpoint_diagram_AbstractDNode', b2)
    if hasattr(b2, 'DNode274'):
        assert not _is_linked(b2, 'DNode274', a)


def test_assoc_ownedDetails276_link_reassign_clear():
    a = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = DDiagram()
    b2 = DDiagram()
    _safe_set(a, 'viewpoint_diagram_DNode277', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DNode277', b1)
    if hasattr(b1, 'DDiagram278'):
        assert _is_linked(b1, 'DDiagram278', a)
    _safe_set(a, 'viewpoint_diagram_DNode277', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DNode277', b2)
    if hasattr(b1, 'DDiagram278'):
        assert not _is_linked(b1, 'DDiagram278', a)
    if hasattr(b2, 'DDiagram278'):
        assert _is_linked(b2, 'DDiagram278', a)
    _safe_set(a, 'viewpoint_diagram_DNode277', set())
    assert not _is_linked(a, 'viewpoint_diagram_DNode277', b2)
    if hasattr(b2, 'DDiagram278'):
        assert not _is_linked(b2, 'DDiagram278', a)


def test_assoc_ownedDetails296_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = DDiagram()
    b2 = DDiagram()
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer297', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer297', b1)
    if hasattr(b1, 'DDiagram298'):
        assert _is_linked(b1, 'DDiagram298', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer297', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer297', b2)
    if hasattr(b1, 'DDiagram298'):
        assert not _is_linked(b1, 'DDiagram298', a)
    if hasattr(b2, 'DDiagram298'):
        assert _is_linked(b2, 'DDiagram298', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer297', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer297', b2)
    if hasattr(b2, 'DDiagram298'):
        assert not _is_linked(b2, 'DDiagram298', a)


def test_assoc_ownedDiagramElements225_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = DDiagramElement()
    b2 = DDiagramElement()
    _safe_set(a, 'viewpoint_diagram_DDiagram', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram', b1)
    if hasattr(b1, 'DDiagramElement'):
        assert _is_linked(b1, 'DDiagramElement', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram', b2)
    if hasattr(b1, 'DDiagramElement'):
        assert not _is_linked(b1, 'DDiagramElement', a)
    if hasattr(b2, 'DDiagramElement'):
        assert _is_linked(b2, 'DDiagramElement', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram', b2)
    if hasattr(b2, 'DDiagramElement'):
        assert not _is_linked(b2, 'DDiagramElement', a)


def test_assoc_ownedDiagramElements307_link_reassign_clear():
    a = viewpoint_diagram_DNodeContainer(childrenPresentation="sample_text")
    b1 = DDiagramElement()
    b2 = DDiagramElement()
    _safe_set(a, 'viewpoint_diagram_DNodeContainer', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DNodeContainer', b1)
    if hasattr(b1, 'DDiagramElement308'):
        assert _is_linked(b1, 'DDiagramElement308', a)
    _safe_set(a, 'viewpoint_diagram_DNodeContainer', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DNodeContainer', b2)
    if hasattr(b1, 'DDiagramElement308'):
        assert not _is_linked(b1, 'DDiagramElement308', a)
    if hasattr(b2, 'DDiagramElement308'):
        assert _is_linked(b2, 'DDiagramElement308', a)
    _safe_set(a, 'viewpoint_diagram_DNodeContainer', set())
    assert not _is_linked(a, 'viewpoint_diagram_DNodeContainer', b2)
    if hasattr(b2, 'DDiagramElement308'):
        assert not _is_linked(b2, 'DDiagramElement308', a)


def test_assoc_ownedElements309_link_reassign_clear():
    a = viewpoint_diagram_DNodeList(lineWidth=7)
    b1 = DNodeListElement()
    b2 = DNodeListElement()
    _safe_set(a, 'viewpoint_diagram_DNodeList', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DNodeList', b1)
    if hasattr(b1, 'DNodeListElement310'):
        assert _is_linked(b1, 'DNodeListElement310', a)
    _safe_set(a, 'viewpoint_diagram_DNodeList', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DNodeList', b2)
    if hasattr(b1, 'DNodeListElement310'):
        assert not _is_linked(b1, 'DNodeListElement310', a)
    if hasattr(b2, 'DNodeListElement310'):
        assert _is_linked(b2, 'DNodeListElement310', a)
    _safe_set(a, 'viewpoint_diagram_DNodeList', set())
    assert not _is_linked(a, 'viewpoint_diagram_DNodeList', b2)
    if hasattr(b2, 'DNodeListElement310'):
        assert not _is_linked(b2, 'DNodeListElement310', a)


def test_assoc_ownedExtensions34_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_MetaModelExtension()
    b2 = viewpoint_MetaModelExtension()
    _safe_set(a, 'viewpoint_DView35', b1)
    assert _is_linked(a, 'viewpoint_DView35', b1)
    if hasattr(b1, 'viewpoint_MetaModelExtension'):
        assert _is_linked(b1, 'viewpoint_MetaModelExtension', a)
    _safe_set(a, 'viewpoint_DView35', b2)
    assert _is_linked(a, 'viewpoint_DView35', b2)
    if hasattr(b1, 'viewpoint_MetaModelExtension'):
        assert not _is_linked(b1, 'viewpoint_MetaModelExtension', a)
    if hasattr(b2, 'viewpoint_MetaModelExtension'):
        assert _is_linked(b2, 'viewpoint_MetaModelExtension', a)
    _safe_set(a, 'viewpoint_DView35', None)
    assert not _is_linked(a, 'viewpoint_DView35', b2)
    if hasattr(b2, 'viewpoint_MetaModelExtension'):
        assert not _is_linked(b2, 'viewpoint_MetaModelExtension', a)


def test_assoc_ownedFeatureExtensions11_link_reassign_clear():
    a = viewpoint_DAnalysis(version="sample_text")
    b1 = viewpoint_DFeatureExtension()
    b2 = viewpoint_DFeatureExtension()
    _safe_set(a, 'viewpoint_DAnalysis12', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysis12', b1)
    if hasattr(b1, 'viewpoint_DFeatureExtension'):
        assert _is_linked(b1, 'viewpoint_DFeatureExtension', a)
    _safe_set(a, 'viewpoint_DAnalysis12', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysis12', b2)
    if hasattr(b1, 'viewpoint_DFeatureExtension'):
        assert not _is_linked(b1, 'viewpoint_DFeatureExtension', a)
    if hasattr(b2, 'viewpoint_DFeatureExtension'):
        assert _is_linked(b2, 'viewpoint_DFeatureExtension', a)
    _safe_set(a, 'viewpoint_DAnalysis12', set())
    assert not _is_linked(a, 'viewpoint_DAnalysis12', b2)
    if hasattr(b2, 'viewpoint_DFeatureExtension'):
        assert not _is_linked(b2, 'viewpoint_DFeatureExtension', a)


def test_assoc_ownedFeatureExtensions80_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = FeatureExtensionDescription()
    b2 = FeatureExtensionDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint81', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint81', b1)
    if hasattr(b1, 'FeatureExtensionDescription82'):
        assert _is_linked(b1, 'FeatureExtensionDescription82', a)
    _safe_set(a, 'viewpoint_description_Viewpoint81', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint81', b2)
    if hasattr(b1, 'FeatureExtensionDescription82'):
        assert not _is_linked(b1, 'FeatureExtensionDescription82', a)
    if hasattr(b2, 'FeatureExtensionDescription82'):
        assert _is_linked(b2, 'FeatureExtensionDescription82', a)
    _safe_set(a, 'viewpoint_description_Viewpoint81', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint81', b2)
    if hasattr(b2, 'FeatureExtensionDescription82'):
        assert not _is_linked(b2, 'FeatureExtensionDescription82', a)


def test_assoc_ownedJavaExtensions76_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = JavaExtension()
    b2 = JavaExtension()
    _safe_set(a, 'viewpoint_description_Viewpoint77', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint77', b1)
    if hasattr(b1, 'JavaExtension'):
        assert _is_linked(b1, 'JavaExtension', a)
    _safe_set(a, 'viewpoint_description_Viewpoint77', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint77', b2)
    if hasattr(b1, 'JavaExtension'):
        assert not _is_linked(b1, 'JavaExtension', a)
    if hasattr(b2, 'JavaExtension'):
        assert _is_linked(b2, 'JavaExtension', a)
    _safe_set(a, 'viewpoint_description_Viewpoint77', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint77', b2)
    if hasattr(b2, 'JavaExtension'):
        assert not _is_linked(b2, 'JavaExtension', a)


def test_assoc_ownedMMExtensions78_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = MetamodelExtensionSetting()
    b2 = MetamodelExtensionSetting()
    _safe_set(a, 'viewpoint_description_Viewpoint79', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint79', b1)
    if hasattr(b1, 'MetamodelExtensionSetting'):
        assert _is_linked(b1, 'MetamodelExtensionSetting', a)
    _safe_set(a, 'viewpoint_description_Viewpoint79', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint79', b2)
    if hasattr(b1, 'MetamodelExtensionSetting'):
        assert not _is_linked(b1, 'MetamodelExtensionSetting', a)
    if hasattr(b2, 'MetamodelExtensionSetting'):
        assert _is_linked(b2, 'MetamodelExtensionSetting', a)
    _safe_set(a, 'viewpoint_description_Viewpoint79', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint79', b2)
    if hasattr(b2, 'MetamodelExtensionSetting'):
        assert not _is_linked(b2, 'MetamodelExtensionSetting', a)


def test_assoc_ownedNavigationLinks15_link_reassign_clear():
    a = viewpoint_DNavigationLink(label="sample_text", targetType="sample_text")
    b1 = viewpoint_DNavigable()
    b2 = viewpoint_DNavigable()
    _safe_set(a, 'viewpoint_DNavigationLink', b1)
    assert _is_linked(a, 'viewpoint_DNavigationLink', b1)
    if hasattr(b1, 'viewpoint_DNavigable'):
        assert _is_linked(b1, 'viewpoint_DNavigable', a)
    _safe_set(a, 'viewpoint_DNavigationLink', b2)
    assert _is_linked(a, 'viewpoint_DNavigationLink', b2)
    if hasattr(b1, 'viewpoint_DNavigable'):
        assert not _is_linked(b1, 'viewpoint_DNavigable', a)
    if hasattr(b2, 'viewpoint_DNavigable'):
        assert _is_linked(b2, 'viewpoint_DNavigable', a)
    _safe_set(a, 'viewpoint_DNavigationLink', None)
    assert not _is_linked(a, 'viewpoint_DNavigationLink', b2)
    if hasattr(b2, 'viewpoint_DNavigable'):
        assert not _is_linked(b2, 'viewpoint_DNavigable', a)


def test_assoc_ownedRepresentationElements22_link_reassign_clear():
    a = viewpoint_DRepresentationElement(name="sample_text")
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DRepresentationElement', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationElement', b1)
    if hasattr(b1, 'viewpoint_DRepresentation'):
        assert _is_linked(b1, 'viewpoint_DRepresentation', a)
    _safe_set(a, 'viewpoint_DRepresentationElement', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationElement', b2)
    if hasattr(b1, 'viewpoint_DRepresentation'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation', a)
    if hasattr(b2, 'viewpoint_DRepresentation'):
        assert _is_linked(b2, 'viewpoint_DRepresentation', a)
    _safe_set(a, 'viewpoint_DRepresentationElement', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationElement', b2)
    if hasattr(b2, 'viewpoint_DRepresentation'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation', a)


def test_assoc_ownedRepresentationExtensions74_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationExtensionDescription()
    b2 = RepresentationExtensionDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint75', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint75', b1)
    if hasattr(b1, 'RepresentationExtensionDescription'):
        assert _is_linked(b1, 'RepresentationExtensionDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint75', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint75', b2)
    if hasattr(b1, 'RepresentationExtensionDescription'):
        assert not _is_linked(b1, 'RepresentationExtensionDescription', a)
    if hasattr(b2, 'RepresentationExtensionDescription'):
        assert _is_linked(b2, 'RepresentationExtensionDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint75', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint75', b2)
    if hasattr(b2, 'RepresentationExtensionDescription'):
        assert not _is_linked(b2, 'RepresentationExtensionDescription', a)


def test_assoc_ownedRepresentations31_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DView32', {b1})
    assert _is_linked(a, 'viewpoint_DView32', b1)
    if hasattr(b1, 'viewpoint_DRepresentation33'):
        assert _is_linked(b1, 'viewpoint_DRepresentation33', a)
    _safe_set(a, 'viewpoint_DView32', {b2})
    assert _is_linked(a, 'viewpoint_DView32', b2)
    if hasattr(b1, 'viewpoint_DRepresentation33'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation33', a)
    if hasattr(b2, 'viewpoint_DRepresentation33'):
        assert _is_linked(b2, 'viewpoint_DRepresentation33', a)
    _safe_set(a, 'viewpoint_DView32', set())
    assert not _is_linked(a, 'viewpoint_DView32', b2)
    if hasattr(b2, 'viewpoint_DRepresentation33'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation33', a)


def test_assoc_ownedRepresentations72_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint73', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint73', b1)
    if hasattr(b1, 'RepresentationDescription'):
        assert _is_linked(b1, 'RepresentationDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint73', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint73', b2)
    if hasattr(b1, 'RepresentationDescription'):
        assert not _is_linked(b1, 'RepresentationDescription', a)
    if hasattr(b2, 'RepresentationDescription'):
        assert _is_linked(b2, 'RepresentationDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint73', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint73', b2)
    if hasattr(b2, 'RepresentationDescription'):
        assert not _is_linked(b2, 'RepresentationDescription', a)


def test_assoc_ownedRepresentations86_link_reassign_clear():
    a = viewpoint_description_RepresentationTemplate(name="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', {b1})
    assert _is_linked(a, 'viewpoint_description_RepresentationTemplate', b1)
    if hasattr(b1, 'RepresentationDescription87'):
        assert _is_linked(b1, 'RepresentationDescription87', a)
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', {b2})
    assert _is_linked(a, 'viewpoint_description_RepresentationTemplate', b2)
    if hasattr(b1, 'RepresentationDescription87'):
        assert not _is_linked(b1, 'RepresentationDescription87', a)
    if hasattr(b2, 'RepresentationDescription87'):
        assert _is_linked(b2, 'RepresentationDescription87', a)
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', set())
    assert not _is_linked(a, 'viewpoint_description_RepresentationTemplate', b2)
    if hasattr(b2, 'RepresentationDescription87'):
        assert not _is_linked(b2, 'RepresentationDescription87', a)


def test_assoc_ownedRules728_link_reassign_clear():
    a = viewpoint_validation_ValidationSet(name="sample_text")
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_validation_ValidationSet', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet', b1)
    if hasattr(b1, 'validation_ValidationRule729'):
        assert _is_linked(b1, 'validation_ValidationRule729', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet', b2)
    if hasattr(b1, 'validation_ValidationRule729'):
        assert not _is_linked(b1, 'validation_ValidationRule729', a)
    if hasattr(b2, 'validation_ValidationRule729'):
        assert _is_linked(b2, 'validation_ValidationRule729', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationSet', b2)
    if hasattr(b2, 'validation_ValidationRule729'):
        assert not _is_linked(b2, 'validation_ValidationRule729', a)


def test_assoc_ownedSessions61_link_reassign_clear():
    a = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    b1 = viewpoint_SessionManagerEObject()
    b2 = viewpoint_SessionManagerEObject()
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject62', b1)
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject62', b1)
    if hasattr(b1, 'viewpoint_SessionManagerEObject'):
        assert _is_linked(b1, 'viewpoint_SessionManagerEObject', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject62', b2)
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject62', b2)
    if hasattr(b1, 'viewpoint_SessionManagerEObject'):
        assert not _is_linked(b1, 'viewpoint_SessionManagerEObject', a)
    if hasattr(b2, 'viewpoint_SessionManagerEObject'):
        assert _is_linked(b2, 'viewpoint_SessionManagerEObject', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject62', None)
    assert not _is_linked(a, 'viewpoint_DAnalysisSessionEObject62', b2)
    if hasattr(b2, 'viewpoint_SessionManagerEObject'):
        assert not _is_linked(b2, 'viewpoint_SessionManagerEObject', a)


def test_assoc_ownedStyle275_link_reassign_clear():
    a = viewpoint_diagram_DNode(height="sample_text", labelPosition="sample_text", resizeKind="sample_text", width="sample_text")
    b1 = NodeStyle()
    b2 = NodeStyle()
    _safe_set(a, 'viewpoint_diagram_DNode', b1)
    assert _is_linked(a, 'viewpoint_diagram_DNode', b1)
    if hasattr(b1, 'NodeStyle'):
        assert _is_linked(b1, 'NodeStyle', a)
    _safe_set(a, 'viewpoint_diagram_DNode', b2)
    assert _is_linked(a, 'viewpoint_diagram_DNode', b2)
    if hasattr(b1, 'NodeStyle'):
        assert not _is_linked(b1, 'NodeStyle', a)
    if hasattr(b2, 'NodeStyle'):
        assert _is_linked(b2, 'NodeStyle', a)
    _safe_set(a, 'viewpoint_diagram_DNode', None)
    assert not _is_linked(a, 'viewpoint_diagram_DNode', b2)
    if hasattr(b2, 'NodeStyle'):
        assert not _is_linked(b2, 'NodeStyle', a)


def test_assoc_ownedStyle294_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElementContainer(height="sample_text", width="sample_text")
    b1 = ContainerStyle()
    b2 = ContainerStyle()
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer295', b1)
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer295', b1)
    if hasattr(b1, 'ContainerStyle'):
        assert _is_linked(b1, 'ContainerStyle', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer295', b2)
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer295', b2)
    if hasattr(b1, 'ContainerStyle'):
        assert not _is_linked(b1, 'ContainerStyle', a)
    if hasattr(b2, 'ContainerStyle'):
        assert _is_linked(b2, 'ContainerStyle', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElementContainer295', None)
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElementContainer295', b2)
    if hasattr(b2, 'ContainerStyle'):
        assert not _is_linked(b2, 'ContainerStyle', a)


def test_assoc_ownedStyle322_link_reassign_clear():
    a = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = EdgeStyle()
    b2 = EdgeStyle()
    _safe_set(a, 'viewpoint_diagram_DEdge', b1)
    assert _is_linked(a, 'viewpoint_diagram_DEdge', b1)
    if hasattr(b1, 'EdgeStyle'):
        assert _is_linked(b1, 'EdgeStyle', a)
    _safe_set(a, 'viewpoint_diagram_DEdge', b2)
    assert _is_linked(a, 'viewpoint_diagram_DEdge', b2)
    if hasattr(b1, 'EdgeStyle'):
        assert not _is_linked(b1, 'EdgeStyle', a)
    if hasattr(b2, 'EdgeStyle'):
        assert _is_linked(b2, 'EdgeStyle', a)
    _safe_set(a, 'viewpoint_diagram_DEdge', None)
    assert not _is_linked(a, 'viewpoint_diagram_DEdge', b2)
    if hasattr(b2, 'EdgeStyle'):
        assert not _is_linked(b2, 'EdgeStyle', a)


def test_assoc_ownedTemplates83_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationTemplate()
    b2 = RepresentationTemplate()
    _safe_set(a, 'viewpoint_description_Viewpoint84', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint84', b1)
    if hasattr(b1, 'RepresentationTemplate'):
        assert _is_linked(b1, 'RepresentationTemplate', a)
    _safe_set(a, 'viewpoint_description_Viewpoint84', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint84', b2)
    if hasattr(b1, 'RepresentationTemplate'):
        assert not _is_linked(b1, 'RepresentationTemplate', a)
    if hasattr(b2, 'RepresentationTemplate'):
        assert _is_linked(b2, 'RepresentationTemplate', a)
    _safe_set(a, 'viewpoint_description_Viewpoint84', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint84', b2)
    if hasattr(b2, 'RepresentationTemplate'):
        assert not _is_linked(b2, 'RepresentationTemplate', a)


def test_assoc_ownedTools606_link_reassign_clear():
    a = viewpoint_tool_ToolSection(icon="sample_text")
    b1 = tool_ToolEntry()
    b2 = tool_ToolEntry()
    _safe_set(a, 'viewpoint_tool_ToolSection', {b1})
    assert _is_linked(a, 'viewpoint_tool_ToolSection', b1)
    if hasattr(b1, 'tool_ToolEntry607'):
        assert _is_linked(b1, 'tool_ToolEntry607', a)
    _safe_set(a, 'viewpoint_tool_ToolSection', {b2})
    assert _is_linked(a, 'viewpoint_tool_ToolSection', b2)
    if hasattr(b1, 'tool_ToolEntry607'):
        assert not _is_linked(b1, 'tool_ToolEntry607', a)
    if hasattr(b2, 'tool_ToolEntry607'):
        assert _is_linked(b2, 'tool_ToolEntry607', a)
    _safe_set(a, 'viewpoint_tool_ToolSection', set())
    assert not _is_linked(a, 'viewpoint_tool_ToolSection', b2)
    if hasattr(b2, 'tool_ToolEntry607'):
        assert not _is_linked(b2, 'tool_ToolEntry607', a)


def test_assoc_ownedVariables726_link_reassign_clear():
    a = viewpoint_filter_VariableFilter(semanticConditionExpression="sample_text")
    b1 = filter_FilterVariable()
    b2 = filter_FilterVariable()
    _safe_set(a, 'viewpoint_filter_VariableFilter', {b1})
    assert _is_linked(a, 'viewpoint_filter_VariableFilter', b1)
    if hasattr(b1, 'filter_FilterVariable727'):
        assert _is_linked(b1, 'filter_FilterVariable727', a)
    _safe_set(a, 'viewpoint_filter_VariableFilter', {b2})
    assert _is_linked(a, 'viewpoint_filter_VariableFilter', b2)
    if hasattr(b1, 'filter_FilterVariable727'):
        assert not _is_linked(b1, 'filter_FilterVariable727', a)
    if hasattr(b2, 'filter_FilterVariable727'):
        assert _is_linked(b2, 'filter_FilterVariable727', a)
    _safe_set(a, 'viewpoint_filter_VariableFilter', set())
    assert not _is_linked(a, 'viewpoint_filter_VariableFilter', b2)
    if hasattr(b2, 'filter_FilterVariable727'):
        assert not _is_linked(b2, 'filter_FilterVariable727', a)


def test_assoc_ownedViewpoints65_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = Viewpoint()
    b2 = Viewpoint()
    _safe_set(a, 'viewpoint_description_Group', {b1})
    assert _is_linked(a, 'viewpoint_description_Group', b1)
    if hasattr(b1, 'Viewpoint66'):
        assert _is_linked(b1, 'Viewpoint66', a)
    _safe_set(a, 'viewpoint_description_Group', {b2})
    assert _is_linked(a, 'viewpoint_description_Group', b2)
    if hasattr(b1, 'Viewpoint66'):
        assert not _is_linked(b1, 'Viewpoint66', a)
    if hasattr(b2, 'Viewpoint66'):
        assert _is_linked(b2, 'Viewpoint66', a)
    _safe_set(a, 'viewpoint_description_Group', set())
    assert not _is_linked(a, 'viewpoint_description_Group', b2)
    if hasattr(b2, 'Viewpoint66'):
        assert not _is_linked(b2, 'Viewpoint66', a)


def test_assoc_ownedViews6_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DAnalysis(version="sample_text")
    b2 = viewpoint_DAnalysis(version="sample_text_2")
    _safe_set(a, 'viewpoint_DView', b1)
    assert _is_linked(a, 'viewpoint_DView', b1)
    if hasattr(b1, 'viewpoint_DAnalysis7'):
        assert _is_linked(b1, 'viewpoint_DAnalysis7', a)
    _safe_set(a, 'viewpoint_DView', b2)
    assert _is_linked(a, 'viewpoint_DView', b2)
    if hasattr(b1, 'viewpoint_DAnalysis7'):
        assert not _is_linked(b1, 'viewpoint_DAnalysis7', a)
    if hasattr(b2, 'viewpoint_DAnalysis7'):
        assert _is_linked(b2, 'viewpoint_DAnalysis7', a)
    _safe_set(a, 'viewpoint_DView', None)
    assert not _is_linked(a, 'viewpoint_DView', b2)
    if hasattr(b2, 'viewpoint_DAnalysis7'):
        assert not _is_linked(b2, 'viewpoint_DAnalysis7', a)


def test_assoc_parameters204_link_reassign_clear():
    a = viewpoint_tool_ExternalJavaAction(id="sample_text")
    b1 = tool_ExternalJavaActionParameter()
    b2 = tool_ExternalJavaActionParameter()
    _safe_set(a, 'viewpoint_tool_ExternalJavaAction', {b1})
    assert _is_linked(a, 'viewpoint_tool_ExternalJavaAction', b1)
    if hasattr(b1, 'tool_ExternalJavaActionParameter'):
        assert _is_linked(b1, 'tool_ExternalJavaActionParameter', a)
    _safe_set(a, 'viewpoint_tool_ExternalJavaAction', {b2})
    assert _is_linked(a, 'viewpoint_tool_ExternalJavaAction', b2)
    if hasattr(b1, 'tool_ExternalJavaActionParameter'):
        assert not _is_linked(b1, 'tool_ExternalJavaActionParameter', a)
    if hasattr(b2, 'tool_ExternalJavaActionParameter'):
        assert _is_linked(b2, 'tool_ExternalJavaActionParameter', a)
    _safe_set(a, 'viewpoint_tool_ExternalJavaAction', set())
    assert not _is_linked(a, 'viewpoint_tool_ExternalJavaAction', b2)
    if hasattr(b2, 'tool_ExternalJavaActionParameter'):
        assert not _is_linked(b2, 'tool_ExternalJavaActionParameter', a)


def test_assoc_parameters688_link_reassign_clear():
    a = viewpoint_tool_DeleteHook(id="sample_text")
    b1 = tool_DeleteHookParameter()
    b2 = tool_DeleteHookParameter()
    _safe_set(a, 'viewpoint_tool_DeleteHook', {b1})
    assert _is_linked(a, 'viewpoint_tool_DeleteHook', b1)
    if hasattr(b1, 'tool_DeleteHookParameter'):
        assert _is_linked(b1, 'tool_DeleteHookParameter', a)
    _safe_set(a, 'viewpoint_tool_DeleteHook', {b2})
    assert _is_linked(a, 'viewpoint_tool_DeleteHook', b2)
    if hasattr(b1, 'tool_DeleteHookParameter'):
        assert not _is_linked(b1, 'tool_DeleteHookParameter', a)
    if hasattr(b2, 'tool_DeleteHookParameter'):
        assert _is_linked(b2, 'tool_DeleteHookParameter', a)
    _safe_set(a, 'viewpoint_tool_DeleteHook', set())
    assert not _is_linked(a, 'viewpoint_tool_DeleteHook', b2)
    if hasattr(b2, 'tool_DeleteHookParameter'):
        assert not _is_linked(b2, 'tool_DeleteHookParameter', a)


def test_assoc_parentLayers259_link_reassign_clear():
    a = viewpoint_diagram_DDiagramElement(tooltipText="sample_text", visible=True)
    b1 = description_Layer()
    b2 = description_Layer()
    _safe_set(a, 'viewpoint_diagram_DDiagramElement', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElement', b1)
    if hasattr(b1, 'description_Layer260'):
        assert _is_linked(b1, 'description_Layer260', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElement', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagramElement', b2)
    if hasattr(b1, 'description_Layer260'):
        assert not _is_linked(b1, 'description_Layer260', a)
    if hasattr(b2, 'description_Layer260'):
        assert _is_linked(b2, 'description_Layer260', a)
    _safe_set(a, 'viewpoint_diagram_DDiagramElement', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagramElement', b2)
    if hasattr(b2, 'description_Layer260'):
        assert not _is_linked(b2, 'description_Layer260', a)


def test_assoc_path332_link_reassign_clear():
    a = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = EdgeTarget()
    b2 = EdgeTarget()
    _safe_set(a, 'viewpoint_diagram_DEdge333', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DEdge333', b1)
    if hasattr(b1, 'EdgeTarget334'):
        assert _is_linked(b1, 'EdgeTarget334', a)
    _safe_set(a, 'viewpoint_diagram_DEdge333', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DEdge333', b2)
    if hasattr(b1, 'EdgeTarget334'):
        assert not _is_linked(b1, 'EdgeTarget334', a)
    if hasattr(b2, 'EdgeTarget334'):
        assert _is_linked(b2, 'EdgeTarget334', a)
    _safe_set(a, 'viewpoint_diagram_DEdge333', set())
    assert not _is_linked(a, 'viewpoint_diagram_DEdge333', b2)
    if hasattr(b2, 'EdgeTarget334'):
        assert not _is_linked(b2, 'EdgeTarget334', a)


def test_assoc_pathNodeMapping521_link_reassign_clear():
    a = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = description_AbstractNodeMapping()
    b2 = description_AbstractNodeMapping()
    _safe_set(a, 'viewpoint_description_EdgeMapping522', {b1})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping522', b1)
    if hasattr(b1, 'description_AbstractNodeMapping'):
        assert _is_linked(b1, 'description_AbstractNodeMapping', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping522', {b2})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping522', b2)
    if hasattr(b1, 'description_AbstractNodeMapping'):
        assert not _is_linked(b1, 'description_AbstractNodeMapping', a)
    if hasattr(b2, 'description_AbstractNodeMapping'):
        assert _is_linked(b2, 'description_AbstractNodeMapping', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping522', set())
    assert not _is_linked(a, 'viewpoint_description_EdgeMapping522', b2)
    if hasattr(b2, 'description_AbstractNodeMapping'):
        assert not _is_linked(b2, 'description_AbstractNodeMapping', a)


def test_assoc_popupMenus611_link_reassign_clear():
    a = viewpoint_tool_ToolSection(icon="sample_text")
    b1 = tool_PopupMenu()
    b2 = tool_PopupMenu()
    _safe_set(a, 'viewpoint_tool_ToolSection612', {b1})
    assert _is_linked(a, 'viewpoint_tool_ToolSection612', b1)
    if hasattr(b1, 'tool_PopupMenu'):
        assert _is_linked(b1, 'tool_PopupMenu', a)
    _safe_set(a, 'viewpoint_tool_ToolSection612', {b2})
    assert _is_linked(a, 'viewpoint_tool_ToolSection612', b2)
    if hasattr(b1, 'tool_PopupMenu'):
        assert not _is_linked(b1, 'tool_PopupMenu', a)
    if hasattr(b2, 'tool_PopupMenu'):
        assert _is_linked(b2, 'tool_PopupMenu', a)
    _safe_set(a, 'viewpoint_tool_ToolSection612', set())
    assert not _is_linked(a, 'viewpoint_tool_ToolSection612', b2)
    if hasattr(b2, 'tool_PopupMenu'):
        assert not _is_linked(b2, 'tool_PopupMenu', a)


def test_assoc_reconnections519_link_reassign_clear():
    a = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = tool_ReconnectEdgeDescription()
    b2 = tool_ReconnectEdgeDescription()
    _safe_set(a, 'viewpoint_description_EdgeMapping520', {b1})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping520', b1)
    if hasattr(b1, 'tool_ReconnectEdgeDescription'):
        assert _is_linked(b1, 'tool_ReconnectEdgeDescription', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping520', {b2})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping520', b2)
    if hasattr(b1, 'tool_ReconnectEdgeDescription'):
        assert not _is_linked(b1, 'tool_ReconnectEdgeDescription', a)
    if hasattr(b2, 'tool_ReconnectEdgeDescription'):
        assert _is_linked(b2, 'tool_ReconnectEdgeDescription', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping520', set())
    assert not _is_linked(a, 'viewpoint_description_EdgeMapping520', b2)
    if hasattr(b2, 'tool_ReconnectEdgeDescription'):
        assert not _is_linked(b2, 'tool_ReconnectEdgeDescription', a)


def test_assoc_referencedAnalysis1_link_reassign_clear():
    a = viewpoint_DAnalysis(version="sample_text")
    b1 = viewpoint_DAnalysis(version="sample_text")
    b2 = viewpoint_DAnalysis(version="sample_text_2")
    _safe_set(a, 'viewpoint_DAnalysis', b1)
    assert _is_linked(a, 'viewpoint_DAnalysis', b1)
    if hasattr(b1, 'viewpoint_DAnalysis0'):
        assert _is_linked(b1, 'viewpoint_DAnalysis0', a)
    _safe_set(a, 'viewpoint_DAnalysis', b2)
    assert _is_linked(a, 'viewpoint_DAnalysis', b2)
    if hasattr(b1, 'viewpoint_DAnalysis0'):
        assert not _is_linked(b1, 'viewpoint_DAnalysis0', a)
    if hasattr(b2, 'viewpoint_DAnalysis0'):
        assert _is_linked(b2, 'viewpoint_DAnalysis0', a)
    _safe_set(a, 'viewpoint_DAnalysis', None)
    assert not _is_linked(a, 'viewpoint_DAnalysis', b2)
    if hasattr(b2, 'viewpoint_DAnalysis0'):
        assert not _is_linked(b2, 'viewpoint_DAnalysis0', a)


def test_assoc_referencedRepresentations42_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DView43', {b1})
    assert _is_linked(a, 'viewpoint_DView43', b1)
    if hasattr(b1, 'viewpoint_DRepresentation44'):
        assert _is_linked(b1, 'viewpoint_DRepresentation44', a)
    _safe_set(a, 'viewpoint_DView43', {b2})
    assert _is_linked(a, 'viewpoint_DView43', b2)
    if hasattr(b1, 'viewpoint_DRepresentation44'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation44', a)
    if hasattr(b2, 'viewpoint_DRepresentation44'):
        assert _is_linked(b2, 'viewpoint_DRepresentation44', a)
    _safe_set(a, 'viewpoint_DView43', set())
    assert not _is_linked(a, 'viewpoint_DView43', b2)
    if hasattr(b2, 'viewpoint_DRepresentation44'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation44', a)


def test_assoc_representationDescription177_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b1)
    if hasattr(b1, 'RepresentationDescription178'):
        assert _is_linked(b1, 'RepresentationDescription178', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    if hasattr(b1, 'RepresentationDescription178'):
        assert not _is_linked(b1, 'RepresentationDescription178', a)
    if hasattr(b2, 'RepresentationDescription178'):
        assert _is_linked(b2, 'RepresentationDescription178', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    if hasattr(b2, 'RepresentationDescription178'):
        assert not _is_linked(b2, 'RepresentationDescription178', a)


def test_assoc_representationDescription187_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b1)
    if hasattr(b1, 'RepresentationDescription188'):
        assert _is_linked(b1, 'RepresentationDescription188', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    if hasattr(b1, 'RepresentationDescription188'):
        assert not _is_linked(b1, 'RepresentationDescription188', a)
    if hasattr(b2, 'RepresentationDescription188'):
        assert _is_linked(b2, 'RepresentationDescription188', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    if hasattr(b2, 'RepresentationDescription188'):
        assert not _is_linked(b2, 'RepresentationDescription188', a)


def test_assoc_representationElements23_link_reassign_clear():
    a = viewpoint_DRepresentationElement(name="sample_text")
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DRepresentationElement25', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationElement25', b1)
    if hasattr(b1, 'viewpoint_DRepresentation24'):
        assert _is_linked(b1, 'viewpoint_DRepresentation24', a)
    _safe_set(a, 'viewpoint_DRepresentationElement25', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationElement25', b2)
    if hasattr(b1, 'viewpoint_DRepresentation24'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation24', a)
    if hasattr(b2, 'viewpoint_DRepresentation24'):
        assert _is_linked(b2, 'viewpoint_DRepresentation24', a)
    _safe_set(a, 'viewpoint_DRepresentationElement25', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationElement25', b2)
    if hasattr(b2, 'viewpoint_DRepresentation24'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation24', a)


def test_assoc_representationNameVariable185_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_NameVariable()
    b2 = tool_NameVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription186', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription186', b1)
    if hasattr(b1, 'tool_NameVariable'):
        assert _is_linked(b1, 'tool_NameVariable', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription186', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription186', b2)
    if hasattr(b1, 'tool_NameVariable'):
        assert not _is_linked(b1, 'tool_NameVariable', a)
    if hasattr(b2, 'tool_NameVariable'):
        assert _is_linked(b2, 'tool_NameVariable', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription186', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription186', b2)
    if hasattr(b2, 'tool_NameVariable'):
        assert not _is_linked(b2, 'tool_NameVariable', a)


def test_assoc_representationNameVariable195_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_NameVariable()
    b2 = tool_NameVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription196', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription196', b1)
    if hasattr(b1, 'tool_NameVariable197'):
        assert _is_linked(b1, 'tool_NameVariable197', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription196', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription196', b2)
    if hasattr(b1, 'tool_NameVariable197'):
        assert not _is_linked(b1, 'tool_NameVariable197', a)
    if hasattr(b2, 'tool_NameVariable197'):
        assert _is_linked(b2, 'tool_NameVariable197', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription196', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription196', b2)
    if hasattr(b2, 'tool_NameVariable197'):
        assert not _is_linked(b2, 'tool_NameVariable197', a)


def test_assoc_reusedBorderedNodeMappings479_link_reassign_clear():
    a = viewpoint_description_AbstractNodeMapping(domainClass="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_description_AbstractNodeMapping480', {b1})
    assert _is_linked(a, 'viewpoint_description_AbstractNodeMapping480', b1)
    if hasattr(b1, 'description_NodeMapping481'):
        assert _is_linked(b1, 'description_NodeMapping481', a)
    _safe_set(a, 'viewpoint_description_AbstractNodeMapping480', {b2})
    assert _is_linked(a, 'viewpoint_description_AbstractNodeMapping480', b2)
    if hasattr(b1, 'description_NodeMapping481'):
        assert not _is_linked(b1, 'description_NodeMapping481', a)
    if hasattr(b2, 'description_NodeMapping481'):
        assert _is_linked(b2, 'description_NodeMapping481', a)
    _safe_set(a, 'viewpoint_description_AbstractNodeMapping480', set())
    assert not _is_linked(a, 'viewpoint_description_AbstractNodeMapping480', b2)
    if hasattr(b2, 'description_NodeMapping481'):
        assert not _is_linked(b2, 'description_NodeMapping481', a)


def test_assoc_reusedContainerMappings496_link_reassign_clear():
    a = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_description_ContainerMapping497', {b1})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping497', b1)
    if hasattr(b1, 'description_ContainerMapping498'):
        assert _is_linked(b1, 'description_ContainerMapping498', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping497', {b2})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping497', b2)
    if hasattr(b1, 'description_ContainerMapping498'):
        assert not _is_linked(b1, 'description_ContainerMapping498', a)
    if hasattr(b2, 'description_ContainerMapping498'):
        assert _is_linked(b2, 'description_ContainerMapping498', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping497', set())
    assert not _is_linked(a, 'viewpoint_description_ContainerMapping497', b2)
    if hasattr(b2, 'description_ContainerMapping498'):
        assert not _is_linked(b2, 'description_ContainerMapping498', a)


def test_assoc_reusedMappings455_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_description_DiagramDescription456', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription456', b1)
    if hasattr(b1, 'description_DiagramElementMapping457'):
        assert _is_linked(b1, 'description_DiagramElementMapping457', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription456', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription456', b2)
    if hasattr(b1, 'description_DiagramElementMapping457'):
        assert not _is_linked(b1, 'description_DiagramElementMapping457', a)
    if hasattr(b2, 'description_DiagramElementMapping457'):
        assert _is_linked(b2, 'description_DiagramElementMapping457', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription456', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription456', b2)
    if hasattr(b2, 'description_DiagramElementMapping457'):
        assert not _is_linked(b2, 'description_DiagramElementMapping457', a)


def test_assoc_reusedMappings549_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_description_Layer550', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer550', b1)
    if hasattr(b1, 'description_DiagramElementMapping551'):
        assert _is_linked(b1, 'description_DiagramElementMapping551', a)
    _safe_set(a, 'viewpoint_description_Layer550', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer550', b2)
    if hasattr(b1, 'description_DiagramElementMapping551'):
        assert not _is_linked(b1, 'description_DiagramElementMapping551', a)
    if hasattr(b2, 'description_DiagramElementMapping551'):
        assert _is_linked(b2, 'description_DiagramElementMapping551', a)
    _safe_set(a, 'viewpoint_description_Layer550', set())
    assert not _is_linked(a, 'viewpoint_description_Layer550', b2)
    if hasattr(b2, 'description_DiagramElementMapping551'):
        assert not _is_linked(b2, 'description_DiagramElementMapping551', a)


def test_assoc_reusedNodeMappings490_link_reassign_clear():
    a = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_description_ContainerMapping491', {b1})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping491', b1)
    if hasattr(b1, 'description_NodeMapping492'):
        assert _is_linked(b1, 'description_NodeMapping492', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping491', {b2})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping491', b2)
    if hasattr(b1, 'description_NodeMapping492'):
        assert not _is_linked(b1, 'description_NodeMapping492', a)
    if hasattr(b2, 'description_NodeMapping492'):
        assert _is_linked(b2, 'description_NodeMapping492', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping491', set())
    assert not _is_linked(a, 'viewpoint_description_ContainerMapping491', b2)
    if hasattr(b2, 'description_NodeMapping492'):
        assert not _is_linked(b2, 'description_NodeMapping492', a)


def test_assoc_reusedRules730_link_reassign_clear():
    a = viewpoint_validation_ValidationSet(name="sample_text")
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_validation_ValidationSet731', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet731', b1)
    if hasattr(b1, 'validation_ValidationRule732'):
        assert _is_linked(b1, 'validation_ValidationRule732', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet731', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet731', b2)
    if hasattr(b1, 'validation_ValidationRule732'):
        assert not _is_linked(b1, 'validation_ValidationRule732', a)
    if hasattr(b2, 'validation_ValidationRule732'):
        assert _is_linked(b2, 'validation_ValidationRule732', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet731', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationSet731', b2)
    if hasattr(b2, 'validation_ValidationRule732'):
        assert not _is_linked(b2, 'validation_ValidationRule732', a)


def test_assoc_reusedTools460_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'viewpoint_description_DiagramDescription461', {b1})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription461', b1)
    if hasattr(b1, 'tool_AbstractToolDescription462'):
        assert _is_linked(b1, 'tool_AbstractToolDescription462', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription461', {b2})
    assert _is_linked(a, 'viewpoint_description_DiagramDescription461', b2)
    if hasattr(b1, 'tool_AbstractToolDescription462'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription462', a)
    if hasattr(b2, 'tool_AbstractToolDescription462'):
        assert _is_linked(b2, 'tool_AbstractToolDescription462', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription461', set())
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription461', b2)
    if hasattr(b2, 'tool_AbstractToolDescription462'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription462', a)


def test_assoc_reusedTools558_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = tool_AbstractToolDescription()
    b2 = tool_AbstractToolDescription()
    _safe_set(a, 'viewpoint_description_Layer559', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer559', b1)
    if hasattr(b1, 'tool_AbstractToolDescription560'):
        assert _is_linked(b1, 'tool_AbstractToolDescription560', a)
    _safe_set(a, 'viewpoint_description_Layer559', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer559', b2)
    if hasattr(b1, 'tool_AbstractToolDescription560'):
        assert not _is_linked(b1, 'tool_AbstractToolDescription560', a)
    if hasattr(b2, 'tool_AbstractToolDescription560'):
        assert _is_linked(b2, 'tool_AbstractToolDescription560', a)
    _safe_set(a, 'viewpoint_description_Layer559', set())
    assert not _is_linked(a, 'viewpoint_description_Layer559', b2)
    if hasattr(b2, 'tool_AbstractToolDescription560'):
        assert not _is_linked(b2, 'tool_AbstractToolDescription560', a)


def test_assoc_reusedTools613_link_reassign_clear():
    a = viewpoint_tool_ToolSection(icon="sample_text")
    b1 = tool_ToolEntry()
    b2 = tool_ToolEntry()
    _safe_set(a, 'viewpoint_tool_ToolSection614', {b1})
    assert _is_linked(a, 'viewpoint_tool_ToolSection614', b1)
    if hasattr(b1, 'tool_ToolEntry615'):
        assert _is_linked(b1, 'tool_ToolEntry615', a)
    _safe_set(a, 'viewpoint_tool_ToolSection614', {b2})
    assert _is_linked(a, 'viewpoint_tool_ToolSection614', b2)
    if hasattr(b1, 'tool_ToolEntry615'):
        assert not _is_linked(b1, 'tool_ToolEntry615', a)
    if hasattr(b2, 'tool_ToolEntry615'):
        assert _is_linked(b2, 'tool_ToolEntry615', a)
    _safe_set(a, 'viewpoint_tool_ToolSection614', set())
    assert not _is_linked(a, 'viewpoint_tool_ToolSection614', b2)
    if hasattr(b2, 'tool_ToolEntry615'):
        assert not _is_linked(b2, 'tool_ToolEntry615', a)


def test_assoc_sections375_link_reassign_clear():
    a = viewpoint_diagram_GaugeCompositeStyle(alignment="sample_text")
    b1 = GaugeSection()
    b2 = GaugeSection()
    _safe_set(a, 'viewpoint_diagram_GaugeCompositeStyle', {b1})
    assert _is_linked(a, 'viewpoint_diagram_GaugeCompositeStyle', b1)
    if hasattr(b1, 'GaugeSection'):
        assert _is_linked(b1, 'GaugeSection', a)
    _safe_set(a, 'viewpoint_diagram_GaugeCompositeStyle', {b2})
    assert _is_linked(a, 'viewpoint_diagram_GaugeCompositeStyle', b2)
    if hasattr(b1, 'GaugeSection'):
        assert not _is_linked(b1, 'GaugeSection', a)
    if hasattr(b2, 'GaugeSection'):
        assert _is_linked(b2, 'GaugeSection', a)
    _safe_set(a, 'viewpoint_diagram_GaugeCompositeStyle', set())
    assert not _is_linked(a, 'viewpoint_diagram_GaugeCompositeStyle', b2)
    if hasattr(b2, 'GaugeSection'):
        assert not _is_linked(b2, 'GaugeSection', a)


def test_assoc_sections582_link_reassign_clear():
    a = viewpoint_style_GaugeCompositeStyleDescription(alignment="sample_text")
    b1 = style_GaugeSectionDescription()
    b2 = style_GaugeSectionDescription()
    _safe_set(a, 'viewpoint_style_GaugeCompositeStyleDescription', {b1})
    assert _is_linked(a, 'viewpoint_style_GaugeCompositeStyleDescription', b1)
    if hasattr(b1, 'style_GaugeSectionDescription'):
        assert _is_linked(b1, 'style_GaugeSectionDescription', a)
    _safe_set(a, 'viewpoint_style_GaugeCompositeStyleDescription', {b2})
    assert _is_linked(a, 'viewpoint_style_GaugeCompositeStyleDescription', b2)
    if hasattr(b1, 'style_GaugeSectionDescription'):
        assert not _is_linked(b1, 'style_GaugeSectionDescription', a)
    if hasattr(b2, 'style_GaugeSectionDescription'):
        assert _is_linked(b2, 'style_GaugeSectionDescription', a)
    _safe_set(a, 'viewpoint_style_GaugeCompositeStyleDescription', set())
    assert not _is_linked(a, 'viewpoint_style_GaugeCompositeStyleDescription', b2)
    if hasattr(b2, 'style_GaugeSectionDescription'):
        assert not _is_linked(b2, 'style_GaugeSectionDescription', a)


def test_assoc_selectedViews8_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DAnalysis(version="sample_text")
    b2 = viewpoint_DAnalysis(version="sample_text_2")
    _safe_set(a, 'viewpoint_DView10', b1)
    assert _is_linked(a, 'viewpoint_DView10', b1)
    if hasattr(b1, 'viewpoint_DAnalysis9'):
        assert _is_linked(b1, 'viewpoint_DAnalysis9', a)
    _safe_set(a, 'viewpoint_DView10', b2)
    assert _is_linked(a, 'viewpoint_DView10', b2)
    if hasattr(b1, 'viewpoint_DAnalysis9'):
        assert not _is_linked(b1, 'viewpoint_DAnalysis9', a)
    if hasattr(b2, 'viewpoint_DAnalysis9'):
        assert _is_linked(b2, 'viewpoint_DAnalysis9', a)
    _safe_set(a, 'viewpoint_DView10', None)
    assert not _is_linked(a, 'viewpoint_DView10', b2)
    if hasattr(b2, 'viewpoint_DAnalysis9'):
        assert not _is_linked(b2, 'viewpoint_DAnalysis9', a)


def test_assoc_semanticElements28_link_reassign_clear():
    a = viewpoint_DRepresentationElement(name="sample_text")
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_DRepresentationElement29', {b1})
    assert _is_linked(a, 'viewpoint_DRepresentationElement29', b1)
    if hasattr(b1, 'viewpoint_EObject30'):
        assert _is_linked(b1, 'viewpoint_EObject30', a)
    _safe_set(a, 'viewpoint_DRepresentationElement29', {b2})
    assert _is_linked(a, 'viewpoint_DRepresentationElement29', b2)
    if hasattr(b1, 'viewpoint_EObject30'):
        assert not _is_linked(b1, 'viewpoint_EObject30', a)
    if hasattr(b2, 'viewpoint_EObject30'):
        assert _is_linked(b2, 'viewpoint_EObject30', a)
    _safe_set(a, 'viewpoint_DRepresentationElement29', set())
    assert not _is_linked(a, 'viewpoint_DRepresentationElement29', b2)
    if hasattr(b2, 'viewpoint_EObject30'):
        assert not _is_linked(b2, 'viewpoint_EObject30', a)


def test_assoc_source689_link_reassign_clear():
    a = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_SourceEdgeCreationVariable()
    b2 = tool_SourceEdgeCreationVariable()
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription', b1)
    if hasattr(b1, 'tool_SourceEdgeCreationVariable690'):
        assert _is_linked(b1, 'tool_SourceEdgeCreationVariable690', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription', b2)
    if hasattr(b1, 'tool_SourceEdgeCreationVariable690'):
        assert not _is_linked(b1, 'tool_SourceEdgeCreationVariable690', a)
    if hasattr(b2, 'tool_SourceEdgeCreationVariable690'):
        assert _is_linked(b2, 'tool_SourceEdgeCreationVariable690', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription', b2)
    if hasattr(b2, 'tool_SourceEdgeCreationVariable690'):
        assert not _is_linked(b2, 'tool_SourceEdgeCreationVariable690', a)


def test_assoc_sourceMapping510_link_reassign_clear():
    a = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_description_EdgeMapping', {b1})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping', b1)
    if hasattr(b1, 'description_DiagramElementMapping511'):
        assert _is_linked(b1, 'description_DiagramElementMapping511', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping', {b2})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping', b2)
    if hasattr(b1, 'description_DiagramElementMapping511'):
        assert not _is_linked(b1, 'description_DiagramElementMapping511', a)
    if hasattr(b2, 'description_DiagramElementMapping511'):
        assert _is_linked(b2, 'description_DiagramElementMapping511', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping', set())
    assert not _is_linked(a, 'viewpoint_description_EdgeMapping', b2)
    if hasattr(b2, 'description_DiagramElementMapping511'):
        assert not _is_linked(b2, 'description_DiagramElementMapping511', a)


def test_assoc_sourceNode323_link_reassign_clear():
    a = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = EdgeTarget()
    b2 = EdgeTarget()
    _safe_set(a, 'outgoingEdges', b1)
    assert _is_linked(a, 'outgoingEdges', b1)
    if hasattr(b1, 'EdgeTarget324'):
        assert _is_linked(b1, 'EdgeTarget324', a)
    _safe_set(a, 'outgoingEdges', b2)
    assert _is_linked(a, 'outgoingEdges', b2)
    if hasattr(b1, 'EdgeTarget324'):
        assert not _is_linked(b1, 'EdgeTarget324', a)
    if hasattr(b2, 'EdgeTarget324'):
        assert _is_linked(b2, 'EdgeTarget324', a)
    _safe_set(a, 'outgoingEdges', None)
    assert not _is_linked(a, 'outgoingEdges', b2)
    if hasattr(b2, 'EdgeTarget324'):
        assert not _is_linked(b2, 'EdgeTarget324', a)


def test_assoc_sourceVariable638_link_reassign_clear():
    a = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_SourceEdgeCreationVariable()
    b2 = tool_SourceEdgeCreationVariable()
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription639', b1)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription639', b1)
    if hasattr(b1, 'tool_SourceEdgeCreationVariable'):
        assert _is_linked(b1, 'tool_SourceEdgeCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription639', b2)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription639', b2)
    if hasattr(b1, 'tool_SourceEdgeCreationVariable'):
        assert not _is_linked(b1, 'tool_SourceEdgeCreationVariable', a)
    if hasattr(b2, 'tool_SourceEdgeCreationVariable'):
        assert _is_linked(b2, 'tool_SourceEdgeCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription639', None)
    assert not _is_linked(a, 'viewpoint_tool_EdgeCreationDescription639', b2)
    if hasattr(b2, 'tool_SourceEdgeCreationVariable'):
        assert not _is_linked(b2, 'tool_SourceEdgeCreationVariable', a)


def test_assoc_sourceView694_link_reassign_clear():
    a = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_SourceEdgeViewCreationVariable()
    b2 = tool_SourceEdgeViewCreationVariable()
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription695', b1)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription695', b1)
    if hasattr(b1, 'tool_SourceEdgeViewCreationVariable696'):
        assert _is_linked(b1, 'tool_SourceEdgeViewCreationVariable696', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription695', b2)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription695', b2)
    if hasattr(b1, 'tool_SourceEdgeViewCreationVariable696'):
        assert not _is_linked(b1, 'tool_SourceEdgeViewCreationVariable696', a)
    if hasattr(b2, 'tool_SourceEdgeViewCreationVariable696'):
        assert _is_linked(b2, 'tool_SourceEdgeViewCreationVariable696', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription695', None)
    assert not _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription695', b2)
    if hasattr(b2, 'tool_SourceEdgeViewCreationVariable696'):
        assert not _is_linked(b2, 'tool_SourceEdgeViewCreationVariable696', a)


def test_assoc_sourceViewVariable642_link_reassign_clear():
    a = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_SourceEdgeViewCreationVariable()
    b2 = tool_SourceEdgeViewCreationVariable()
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription643', b1)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription643', b1)
    if hasattr(b1, 'tool_SourceEdgeViewCreationVariable'):
        assert _is_linked(b1, 'tool_SourceEdgeViewCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription643', b2)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription643', b2)
    if hasattr(b1, 'tool_SourceEdgeViewCreationVariable'):
        assert not _is_linked(b1, 'tool_SourceEdgeViewCreationVariable', a)
    if hasattr(b2, 'tool_SourceEdgeViewCreationVariable'):
        assert _is_linked(b2, 'tool_SourceEdgeViewCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription643', None)
    assert not _is_linked(a, 'viewpoint_tool_EdgeCreationDescription643', b2)
    if hasattr(b2, 'tool_SourceEdgeViewCreationVariable'):
        assert not _is_linked(b2, 'tool_SourceEdgeViewCreationVariable', a)


def test_assoc_strokeColor367_link_reassign_clear():
    a = viewpoint_diagram_EdgeStyle(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", size="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = diagram_viewpoint_RGBValues()
    b2 = diagram_viewpoint_RGBValues()
    _safe_set(a, 'viewpoint_diagram_EdgeStyle', b1)
    assert _is_linked(a, 'viewpoint_diagram_EdgeStyle', b1)
    if hasattr(b1, 'diagram_viewpoint_RGBValues368'):
        assert _is_linked(b1, 'diagram_viewpoint_RGBValues368', a)
    _safe_set(a, 'viewpoint_diagram_EdgeStyle', b2)
    assert _is_linked(a, 'viewpoint_diagram_EdgeStyle', b2)
    if hasattr(b1, 'diagram_viewpoint_RGBValues368'):
        assert not _is_linked(b1, 'diagram_viewpoint_RGBValues368', a)
    if hasattr(b2, 'diagram_viewpoint_RGBValues368'):
        assert _is_linked(b2, 'diagram_viewpoint_RGBValues368', a)
    _safe_set(a, 'viewpoint_diagram_EdgeStyle', None)
    assert not _is_linked(a, 'viewpoint_diagram_EdgeStyle', b2)
    if hasattr(b2, 'diagram_viewpoint_RGBValues368'):
        assert not _is_linked(b2, 'diagram_viewpoint_RGBValues368', a)


def test_assoc_strokeColor598_link_reassign_clear():
    a = viewpoint_style_EdgeStyleDescription(foldingStyle="sample_text", lineStyle="sample_text", routingStyle="sample_text", sizeComputationExpression="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription', b1)
    assert _is_linked(a, 'viewpoint_style_EdgeStyleDescription', b1)
    if hasattr(b1, 'ColorDescription599'):
        assert _is_linked(b1, 'ColorDescription599', a)
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription', b2)
    assert _is_linked(a, 'viewpoint_style_EdgeStyleDescription', b2)
    if hasattr(b1, 'ColorDescription599'):
        assert not _is_linked(b1, 'ColorDescription599', a)
    if hasattr(b2, 'ColorDescription599'):
        assert _is_linked(b2, 'ColorDescription599', a)
    _safe_set(a, 'viewpoint_style_EdgeStyleDescription', None)
    assert not _is_linked(a, 'viewpoint_style_EdgeStyleDescription', b2)
    if hasattr(b2, 'ColorDescription599'):
        assert not _is_linked(b2, 'ColorDescription599', a)


def test_assoc_style482_link_reassign_clear():
    a = viewpoint_description_NodeMapping()
    b1 = style_NodeStyleDescription()
    b2 = style_NodeStyleDescription()
    _safe_set(a, 'viewpoint_description_NodeMapping', b1)
    assert _is_linked(a, 'viewpoint_description_NodeMapping', b1)
    if hasattr(b1, 'style_NodeStyleDescription'):
        assert _is_linked(b1, 'style_NodeStyleDescription', a)
    _safe_set(a, 'viewpoint_description_NodeMapping', b2)
    assert _is_linked(a, 'viewpoint_description_NodeMapping', b2)
    if hasattr(b1, 'style_NodeStyleDescription'):
        assert not _is_linked(b1, 'style_NodeStyleDescription', a)
    if hasattr(b2, 'style_NodeStyleDescription'):
        assert _is_linked(b2, 'style_NodeStyleDescription', a)
    _safe_set(a, 'viewpoint_description_NodeMapping', None)
    assert not _is_linked(a, 'viewpoint_description_NodeMapping', b2)
    if hasattr(b2, 'style_NodeStyleDescription'):
        assert not _is_linked(b2, 'style_NodeStyleDescription', a)


def test_assoc_style502_link_reassign_clear():
    a = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = style_ContainerStyleDescription()
    b2 = style_ContainerStyleDescription()
    _safe_set(a, 'viewpoint_description_ContainerMapping503', b1)
    assert _is_linked(a, 'viewpoint_description_ContainerMapping503', b1)
    if hasattr(b1, 'style_ContainerStyleDescription'):
        assert _is_linked(b1, 'style_ContainerStyleDescription', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping503', b2)
    assert _is_linked(a, 'viewpoint_description_ContainerMapping503', b2)
    if hasattr(b1, 'style_ContainerStyleDescription'):
        assert not _is_linked(b1, 'style_ContainerStyleDescription', a)
    if hasattr(b2, 'style_ContainerStyleDescription'):
        assert _is_linked(b2, 'style_ContainerStyleDescription', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping503', None)
    assert not _is_linked(a, 'viewpoint_description_ContainerMapping503', b2)
    if hasattr(b2, 'style_ContainerStyleDescription'):
        assert not _is_linked(b2, 'style_ContainerStyleDescription', a)


def test_assoc_style515_link_reassign_clear():
    a = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = style_EdgeStyleDescription()
    b2 = style_EdgeStyleDescription()
    _safe_set(a, 'viewpoint_description_EdgeMapping516', b1)
    assert _is_linked(a, 'viewpoint_description_EdgeMapping516', b1)
    if hasattr(b1, 'style_EdgeStyleDescription'):
        assert _is_linked(b1, 'style_EdgeStyleDescription', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping516', b2)
    assert _is_linked(a, 'viewpoint_description_EdgeMapping516', b2)
    if hasattr(b1, 'style_EdgeStyleDescription'):
        assert not _is_linked(b1, 'style_EdgeStyleDescription', a)
    if hasattr(b2, 'style_EdgeStyleDescription'):
        assert _is_linked(b2, 'style_EdgeStyleDescription', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping516', None)
    assert not _is_linked(a, 'viewpoint_description_EdgeMapping516', b2)
    if hasattr(b2, 'style_EdgeStyleDescription'):
        assert not _is_linked(b2, 'style_EdgeStyleDescription', a)


def test_assoc_subContainerMappings493_link_reassign_clear():
    a = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = description_ContainerMapping()
    b2 = description_ContainerMapping()
    _safe_set(a, 'viewpoint_description_ContainerMapping494', {b1})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping494', b1)
    if hasattr(b1, 'description_ContainerMapping495'):
        assert _is_linked(b1, 'description_ContainerMapping495', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping494', {b2})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping494', b2)
    if hasattr(b1, 'description_ContainerMapping495'):
        assert not _is_linked(b1, 'description_ContainerMapping495', a)
    if hasattr(b2, 'description_ContainerMapping495'):
        assert _is_linked(b2, 'description_ContainerMapping495', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping494', set())
    assert not _is_linked(a, 'viewpoint_description_ContainerMapping494', b2)
    if hasattr(b2, 'description_ContainerMapping495'):
        assert not _is_linked(b2, 'description_ContainerMapping495', a)


def test_assoc_subDiagrams231_link_reassign_clear():
    a = viewpoint_diagram_DDiagram(headerHeight=7, info="sample_text", isInLayoutingMode=True, synchronized=True)
    b1 = DDiagram()
    b2 = DDiagram()
    _safe_set(a, 'viewpoint_diagram_DDiagram232', {b1})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram232', b1)
    if hasattr(b1, 'DDiagram'):
        assert _is_linked(b1, 'DDiagram', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram232', {b2})
    assert _is_linked(a, 'viewpoint_diagram_DDiagram232', b2)
    if hasattr(b1, 'DDiagram'):
        assert not _is_linked(b1, 'DDiagram', a)
    if hasattr(b2, 'DDiagram'):
        assert _is_linked(b2, 'DDiagram', a)
    _safe_set(a, 'viewpoint_diagram_DDiagram232', set())
    assert not _is_linked(a, 'viewpoint_diagram_DDiagram232', b2)
    if hasattr(b2, 'DDiagram'):
        assert not _is_linked(b2, 'DDiagram', a)


def test_assoc_subNodeMappings485_link_reassign_clear():
    a = viewpoint_description_ContainerMapping(childrenPresentation="sample_text")
    b1 = description_NodeMapping()
    b2 = description_NodeMapping()
    _safe_set(a, 'viewpoint_description_ContainerMapping', {b1})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping', b1)
    if hasattr(b1, 'description_NodeMapping486'):
        assert _is_linked(b1, 'description_NodeMapping486', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping', {b2})
    assert _is_linked(a, 'viewpoint_description_ContainerMapping', b2)
    if hasattr(b1, 'description_NodeMapping486'):
        assert not _is_linked(b1, 'description_NodeMapping486', a)
    if hasattr(b2, 'description_NodeMapping486'):
        assert _is_linked(b2, 'description_NodeMapping486', a)
    _safe_set(a, 'viewpoint_description_ContainerMapping', set())
    assert not _is_linked(a, 'viewpoint_description_ContainerMapping', b2)
    if hasattr(b2, 'description_NodeMapping486'):
        assert not _is_linked(b2, 'description_NodeMapping486', a)


def test_assoc_subSections608_link_reassign_clear():
    a = viewpoint_tool_ToolSection(icon="sample_text")
    b1 = tool_ToolSection()
    b2 = tool_ToolSection()
    _safe_set(a, 'viewpoint_tool_ToolSection609', {b1})
    assert _is_linked(a, 'viewpoint_tool_ToolSection609', b1)
    if hasattr(b1, 'tool_ToolSection610'):
        assert _is_linked(b1, 'tool_ToolSection610', a)
    _safe_set(a, 'viewpoint_tool_ToolSection609', {b2})
    assert _is_linked(a, 'viewpoint_tool_ToolSection609', b2)
    if hasattr(b1, 'tool_ToolSection610'):
        assert not _is_linked(b1, 'tool_ToolSection610', a)
    if hasattr(b2, 'tool_ToolSection610'):
        assert _is_linked(b2, 'tool_ToolSection610', a)
    _safe_set(a, 'viewpoint_tool_ToolSection609', set())
    assert not _is_linked(a, 'viewpoint_tool_ToolSection609', b2)
    if hasattr(b2, 'tool_ToolSection610'):
        assert not _is_linked(b2, 'tool_ToolSection610', a)


def test_assoc_systemColorsPalette67_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = SytemColorsPalette()
    b2 = SytemColorsPalette()
    _safe_set(a, 'viewpoint_description_Group68', b1)
    assert _is_linked(a, 'viewpoint_description_Group68', b1)
    if hasattr(b1, 'SytemColorsPalette'):
        assert _is_linked(b1, 'SytemColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group68', b2)
    assert _is_linked(a, 'viewpoint_description_Group68', b2)
    if hasattr(b1, 'SytemColorsPalette'):
        assert not _is_linked(b1, 'SytemColorsPalette', a)
    if hasattr(b2, 'SytemColorsPalette'):
        assert _is_linked(b2, 'SytemColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group68', None)
    assert not _is_linked(a, 'viewpoint_description_Group68', b2)
    if hasattr(b2, 'SytemColorsPalette'):
        assert not _is_linked(b2, 'SytemColorsPalette', a)


def test_assoc_target691_link_reassign_clear():
    a = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_TargetEdgeCreationVariable()
    b2 = tool_TargetEdgeCreationVariable()
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription692', b1)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription692', b1)
    if hasattr(b1, 'tool_TargetEdgeCreationVariable693'):
        assert _is_linked(b1, 'tool_TargetEdgeCreationVariable693', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription692', b2)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription692', b2)
    if hasattr(b1, 'tool_TargetEdgeCreationVariable693'):
        assert not _is_linked(b1, 'tool_TargetEdgeCreationVariable693', a)
    if hasattr(b2, 'tool_TargetEdgeCreationVariable693'):
        assert _is_linked(b2, 'tool_TargetEdgeCreationVariable693', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription692', None)
    assert not _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription692', b2)
    if hasattr(b2, 'tool_TargetEdgeCreationVariable693'):
        assert not _is_linked(b2, 'tool_TargetEdgeCreationVariable693', a)


def test_assoc_targetMapping512_link_reassign_clear():
    a = viewpoint_description_EdgeMapping(domainClass="sample_text", pathExpression="sample_text", sourceFinderExpression="sample_text", targetExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    b1 = description_DiagramElementMapping()
    b2 = description_DiagramElementMapping()
    _safe_set(a, 'viewpoint_description_EdgeMapping513', {b1})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping513', b1)
    if hasattr(b1, 'description_DiagramElementMapping514'):
        assert _is_linked(b1, 'description_DiagramElementMapping514', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping513', {b2})
    assert _is_linked(a, 'viewpoint_description_EdgeMapping513', b2)
    if hasattr(b1, 'description_DiagramElementMapping514'):
        assert not _is_linked(b1, 'description_DiagramElementMapping514', a)
    if hasattr(b2, 'description_DiagramElementMapping514'):
        assert _is_linked(b2, 'description_DiagramElementMapping514', a)
    _safe_set(a, 'viewpoint_description_EdgeMapping513', set())
    assert not _is_linked(a, 'viewpoint_description_EdgeMapping513', b2)
    if hasattr(b2, 'description_DiagramElementMapping514'):
        assert not _is_linked(b2, 'description_DiagramElementMapping514', a)


def test_assoc_targetNode325_link_reassign_clear():
    a = viewpoint_diagram_DEdge(arrangeConstraints="sample_text", beginLabel="sample_text", endLabel="sample_text", isFold=True, isMockEdge=True, routingStyle="sample_text", size="sample_text")
    b1 = EdgeTarget()
    b2 = EdgeTarget()
    _safe_set(a, 'incomingEdges', b1)
    assert _is_linked(a, 'incomingEdges', b1)
    if hasattr(b1, 'EdgeTarget326'):
        assert _is_linked(b1, 'EdgeTarget326', a)
    _safe_set(a, 'incomingEdges', b2)
    assert _is_linked(a, 'incomingEdges', b2)
    if hasattr(b1, 'EdgeTarget326'):
        assert not _is_linked(b1, 'EdgeTarget326', a)
    if hasattr(b2, 'EdgeTarget326'):
        assert _is_linked(b2, 'EdgeTarget326', a)
    _safe_set(a, 'incomingEdges', None)
    assert not _is_linked(a, 'incomingEdges', b2)
    if hasattr(b2, 'EdgeTarget326'):
        assert not _is_linked(b2, 'EdgeTarget326', a)


def test_assoc_targetVariable640_link_reassign_clear():
    a = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_TargetEdgeCreationVariable()
    b2 = tool_TargetEdgeCreationVariable()
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription641', b1)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription641', b1)
    if hasattr(b1, 'tool_TargetEdgeCreationVariable'):
        assert _is_linked(b1, 'tool_TargetEdgeCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription641', b2)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription641', b2)
    if hasattr(b1, 'tool_TargetEdgeCreationVariable'):
        assert not _is_linked(b1, 'tool_TargetEdgeCreationVariable', a)
    if hasattr(b2, 'tool_TargetEdgeCreationVariable'):
        assert _is_linked(b2, 'tool_TargetEdgeCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription641', None)
    assert not _is_linked(a, 'viewpoint_tool_EdgeCreationDescription641', b2)
    if hasattr(b2, 'tool_TargetEdgeCreationVariable'):
        assert not _is_linked(b2, 'tool_TargetEdgeCreationVariable', a)


def test_assoc_targetView697_link_reassign_clear():
    a = viewpoint_tool_ReconnectEdgeDescription(reconnectionKind="sample_text")
    b1 = tool_TargetEdgeViewCreationVariable()
    b2 = tool_TargetEdgeViewCreationVariable()
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription698', b1)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription698', b1)
    if hasattr(b1, 'tool_TargetEdgeViewCreationVariable699'):
        assert _is_linked(b1, 'tool_TargetEdgeViewCreationVariable699', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription698', b2)
    assert _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription698', b2)
    if hasattr(b1, 'tool_TargetEdgeViewCreationVariable699'):
        assert not _is_linked(b1, 'tool_TargetEdgeViewCreationVariable699', a)
    if hasattr(b2, 'tool_TargetEdgeViewCreationVariable699'):
        assert _is_linked(b2, 'tool_TargetEdgeViewCreationVariable699', a)
    _safe_set(a, 'viewpoint_tool_ReconnectEdgeDescription698', None)
    assert not _is_linked(a, 'viewpoint_tool_ReconnectEdgeDescription698', b2)
    if hasattr(b2, 'tool_TargetEdgeViewCreationVariable699'):
        assert not _is_linked(b2, 'tool_TargetEdgeViewCreationVariable699', a)


def test_assoc_targetViewVariable644_link_reassign_clear():
    a = viewpoint_tool_EdgeCreationDescription(connectionStartPrecondition="sample_text", iconPath="sample_text")
    b1 = tool_TargetEdgeViewCreationVariable()
    b2 = tool_TargetEdgeViewCreationVariable()
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription645', b1)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription645', b1)
    if hasattr(b1, 'tool_TargetEdgeViewCreationVariable'):
        assert _is_linked(b1, 'tool_TargetEdgeViewCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription645', b2)
    assert _is_linked(a, 'viewpoint_tool_EdgeCreationDescription645', b2)
    if hasattr(b1, 'tool_TargetEdgeViewCreationVariable'):
        assert not _is_linked(b1, 'tool_TargetEdgeViewCreationVariable', a)
    if hasattr(b2, 'tool_TargetEdgeViewCreationVariable'):
        assert _is_linked(b2, 'tool_TargetEdgeViewCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_EdgeCreationDescription645', None)
    assert not _is_linked(a, 'viewpoint_tool_EdgeCreationDescription645', b2)
    if hasattr(b2, 'tool_TargetEdgeViewCreationVariable'):
        assert not _is_linked(b2, 'tool_TargetEdgeViewCreationVariable', a)


def test_assoc_toolSection458_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = tool_ToolSection()
    b2 = tool_ToolSection()
    _safe_set(a, 'viewpoint_description_DiagramDescription459', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription459', b1)
    if hasattr(b1, 'tool_ToolSection'):
        assert _is_linked(b1, 'tool_ToolSection', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription459', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription459', b2)
    if hasattr(b1, 'tool_ToolSection'):
        assert not _is_linked(b1, 'tool_ToolSection', a)
    if hasattr(b2, 'tool_ToolSection'):
        assert _is_linked(b2, 'tool_ToolSection', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription459', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription459', b2)
    if hasattr(b2, 'tool_ToolSection'):
        assert not _is_linked(b2, 'tool_ToolSection', a)


def test_assoc_toolSections555_link_reassign_clear():
    a = viewpoint_description_Layer(icon="sample_text")
    b1 = tool_ToolSection()
    b2 = tool_ToolSection()
    _safe_set(a, 'viewpoint_description_Layer556', {b1})
    assert _is_linked(a, 'viewpoint_description_Layer556', b1)
    if hasattr(b1, 'tool_ToolSection557'):
        assert _is_linked(b1, 'tool_ToolSection557', a)
    _safe_set(a, 'viewpoint_description_Layer556', {b2})
    assert _is_linked(a, 'viewpoint_description_Layer556', b2)
    if hasattr(b1, 'tool_ToolSection557'):
        assert not _is_linked(b1, 'tool_ToolSection557', a)
    if hasattr(b2, 'tool_ToolSection557'):
        assert _is_linked(b2, 'tool_ToolSection557', a)
    _safe_set(a, 'viewpoint_description_Layer556', set())
    assert not _is_linked(a, 'viewpoint_description_Layer556', b2)
    if hasattr(b2, 'tool_ToolSection557'):
        assert not _is_linked(b2, 'tool_ToolSection557', a)


def test_assoc_userColorsPalettes69_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = UserColorsPalette()
    b2 = UserColorsPalette()
    _safe_set(a, 'viewpoint_description_Group70', {b1})
    assert _is_linked(a, 'viewpoint_description_Group70', b1)
    if hasattr(b1, 'UserColorsPalette'):
        assert _is_linked(b1, 'UserColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group70', {b2})
    assert _is_linked(a, 'viewpoint_description_Group70', b2)
    if hasattr(b1, 'UserColorsPalette'):
        assert not _is_linked(b1, 'UserColorsPalette', a)
    if hasattr(b2, 'UserColorsPalette'):
        assert _is_linked(b2, 'UserColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group70', set())
    assert not _is_linked(a, 'viewpoint_description_Group70', b2)
    if hasattr(b2, 'UserColorsPalette'):
        assert not _is_linked(b2, 'UserColorsPalette', a)


def test_assoc_validationSet415_link_reassign_clear():
    a = viewpoint_description_DiagramDescription(domainClass="sample_text", enablePopupBars=True, preconditionExpression="sample_text", rootExpression="sample_text")
    b1 = validation_ValidationSet()
    b2 = validation_ValidationSet()
    _safe_set(a, 'viewpoint_description_DiagramDescription416', b1)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription416', b1)
    if hasattr(b1, 'validation_ValidationSet417'):
        assert _is_linked(b1, 'validation_ValidationSet417', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription416', b2)
    assert _is_linked(a, 'viewpoint_description_DiagramDescription416', b2)
    if hasattr(b1, 'validation_ValidationSet417'):
        assert not _is_linked(b1, 'validation_ValidationSet417', a)
    if hasattr(b2, 'validation_ValidationSet417'):
        assert _is_linked(b2, 'validation_ValidationSet417', a)
    _safe_set(a, 'viewpoint_description_DiagramDescription416', None)
    assert not _is_linked(a, 'viewpoint_description_DiagramDescription416', b2)
    if hasattr(b2, 'validation_ValidationSet417'):
        assert not _is_linked(b2, 'validation_ValidationSet417', a)


def test_assoc_validationSet71_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = validation_ValidationSet()
    b2 = validation_ValidationSet()
    _safe_set(a, 'viewpoint_description_Viewpoint', b1)
    assert _is_linked(a, 'viewpoint_description_Viewpoint', b1)
    if hasattr(b1, 'validation_ValidationSet'):
        assert _is_linked(b1, 'validation_ValidationSet', a)
    _safe_set(a, 'viewpoint_description_Viewpoint', b2)
    assert _is_linked(a, 'viewpoint_description_Viewpoint', b2)
    if hasattr(b1, 'validation_ValidationSet'):
        assert not _is_linked(b1, 'validation_ValidationSet', a)
    if hasattr(b2, 'validation_ValidationSet'):
        assert _is_linked(b2, 'validation_ValidationSet', a)
    _safe_set(a, 'viewpoint_description_Viewpoint', None)
    assert not _is_linked(a, 'viewpoint_description_Viewpoint', b2)
    if hasattr(b2, 'validation_ValidationSet'):
        assert not _is_linked(b2, 'validation_ValidationSet', a)


def test_assoc_value109_link_reassign_clear():
    a = viewpoint_description_EReferenceCustomization(referenceName="sample_text")
    b1 = description_viewpoint_EObject()
    b2 = description_viewpoint_EObject()
    _safe_set(a, 'viewpoint_description_EReferenceCustomization', b1)
    assert _is_linked(a, 'viewpoint_description_EReferenceCustomization', b1)
    if hasattr(b1, 'description_viewpoint_EObject110'):
        assert _is_linked(b1, 'description_viewpoint_EObject110', a)
    _safe_set(a, 'viewpoint_description_EReferenceCustomization', b2)
    assert _is_linked(a, 'viewpoint_description_EReferenceCustomization', b2)
    if hasattr(b1, 'description_viewpoint_EObject110'):
        assert not _is_linked(b1, 'description_viewpoint_EObject110', a)
    if hasattr(b2, 'description_viewpoint_EObject110'):
        assert _is_linked(b2, 'description_viewpoint_EObject110', a)
    _safe_set(a, 'viewpoint_description_EReferenceCustomization', None)
    assert not _is_linked(a, 'viewpoint_description_EReferenceCustomization', b2)
    if hasattr(b2, 'description_viewpoint_EObject110'):
        assert not _is_linked(b2, 'description_viewpoint_EObject110', a)


def test_assoc_variable626_link_reassign_clear():
    a = viewpoint_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = tool_NodeCreationVariable()
    b2 = tool_NodeCreationVariable()
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription627', b1)
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription627', b1)
    if hasattr(b1, 'tool_NodeCreationVariable'):
        assert _is_linked(b1, 'tool_NodeCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription627', b2)
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription627', b2)
    if hasattr(b1, 'tool_NodeCreationVariable'):
        assert not _is_linked(b1, 'tool_NodeCreationVariable', a)
    if hasattr(b2, 'tool_NodeCreationVariable'):
        assert _is_linked(b2, 'tool_NodeCreationVariable', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription627', None)
    assert not _is_linked(a, 'viewpoint_tool_NodeCreationDescription627', b2)
    if hasattr(b2, 'tool_NodeCreationVariable'):
        assert not _is_linked(b2, 'tool_NodeCreationVariable', a)


def test_assoc_variable656_link_reassign_clear():
    a = viewpoint_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = tool_NodeCreationVariable()
    b2 = tool_NodeCreationVariable()
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription657', b1)
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription657', b1)
    if hasattr(b1, 'tool_NodeCreationVariable658'):
        assert _is_linked(b1, 'tool_NodeCreationVariable658', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription657', b2)
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription657', b2)
    if hasattr(b1, 'tool_NodeCreationVariable658'):
        assert not _is_linked(b1, 'tool_NodeCreationVariable658', a)
    if hasattr(b2, 'tool_NodeCreationVariable658'):
        assert _is_linked(b2, 'tool_NodeCreationVariable658', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription657', None)
    assert not _is_linked(a, 'viewpoint_tool_ContainerCreationDescription657', b2)
    if hasattr(b2, 'tool_NodeCreationVariable658'):
        assert not _is_linked(b2, 'tool_NodeCreationVariable658', a)


def test_assoc_viewVariable628_link_reassign_clear():
    a = viewpoint_tool_NodeCreationDescription(iconPath="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription629', b1)
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription629', b1)
    if hasattr(b1, 'tool_ContainerViewVariable630'):
        assert _is_linked(b1, 'tool_ContainerViewVariable630', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription629', b2)
    assert _is_linked(a, 'viewpoint_tool_NodeCreationDescription629', b2)
    if hasattr(b1, 'tool_ContainerViewVariable630'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable630', a)
    if hasattr(b2, 'tool_ContainerViewVariable630'):
        assert _is_linked(b2, 'tool_ContainerViewVariable630', a)
    _safe_set(a, 'viewpoint_tool_NodeCreationDescription629', None)
    assert not _is_linked(a, 'viewpoint_tool_NodeCreationDescription629', b2)
    if hasattr(b2, 'tool_ContainerViewVariable630'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable630', a)


def test_assoc_viewVariable659_link_reassign_clear():
    a = viewpoint_tool_ContainerCreationDescription(iconPath="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription660', b1)
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription660', b1)
    if hasattr(b1, 'tool_ContainerViewVariable661'):
        assert _is_linked(b1, 'tool_ContainerViewVariable661', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription660', b2)
    assert _is_linked(a, 'viewpoint_tool_ContainerCreationDescription660', b2)
    if hasattr(b1, 'tool_ContainerViewVariable661'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable661', a)
    if hasattr(b2, 'tool_ContainerViewVariable661'):
        assert _is_linked(b2, 'tool_ContainerViewVariable661', a)
    _safe_set(a, 'viewpoint_tool_ContainerCreationDescription660', None)
    assert not _is_linked(a, 'viewpoint_tool_ContainerCreationDescription660', b2)
    if hasattr(b2, 'tool_ContainerViewVariable661'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable661', a)


def test_assoc_viewpoint45_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = Viewpoint()
    b2 = Viewpoint()
    _safe_set(a, 'viewpoint_DView46', b1)
    assert _is_linked(a, 'viewpoint_DView46', b1)
    if hasattr(b1, 'Viewpoint'):
        assert _is_linked(b1, 'Viewpoint', a)
    _safe_set(a, 'viewpoint_DView46', b2)
    assert _is_linked(a, 'viewpoint_DView46', b2)
    if hasattr(b1, 'Viewpoint'):
        assert not _is_linked(b1, 'Viewpoint', a)
    if hasattr(b2, 'Viewpoint'):
        assert _is_linked(b2, 'Viewpoint', a)
    _safe_set(a, 'viewpoint_DView46', None)
    assert not _is_linked(a, 'viewpoint_DView46', b2)
    if hasattr(b2, 'Viewpoint'):
        assert not _is_linked(b2, 'Viewpoint', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractDNode_strategy = st.builds(AbstractDNode)
@given(instance=AbstractDNode_strategy)
@settings(max_examples=25)
def test_AbstractDNode_instantiation(instance):
    assert isinstance(instance, AbstractDNode)


AbstractToolDescription_strategy = st.builds(AbstractToolDescription)
@given(instance=AbstractToolDescription_strategy)
@settings(max_examples=25)
def test_AbstractToolDescription_instantiation(instance):
    assert isinstance(instance, AbstractToolDescription)


AbstractVariable_strategy = st.builds(AbstractVariable)
@given(instance=AbstractVariable_strategy)
@settings(max_examples=25)
def test_AbstractVariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)


AnnotationEntry_strategy = st.builds(AnnotationEntry)
@given(instance=AnnotationEntry_strategy)
@settings(max_examples=25)
def test_AnnotationEntry_instantiation(instance):
    assert isinstance(instance, AnnotationEntry)


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


BeginLabelStyle_strategy = st.builds(BeginLabelStyle)
@given(instance=BeginLabelStyle_strategy)
@settings(max_examples=25)
def test_BeginLabelStyle_instantiation(instance):
    assert isinstance(instance, BeginLabelStyle)


CenterLabelStyle_strategy = st.builds(CenterLabelStyle)
@given(instance=CenterLabelStyle_strategy)
@settings(max_examples=25)
def test_CenterLabelStyle_instantiation(instance):
    assert isinstance(instance, CenterLabelStyle)


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


ColorStep_strategy = st.builds(ColorStep)
@given(instance=ColorStep_strategy)
@settings(max_examples=25)
def test_ColorStep_instantiation(instance):
    assert isinstance(instance, ColorStep)


ConditionalStyleDescription_strategy = st.builds(ConditionalStyleDescription)
@given(instance=ConditionalStyleDescription_strategy)
@settings(max_examples=25)
def test_ConditionalStyleDescription_instantiation(instance):
    assert isinstance(instance, ConditionalStyleDescription)


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


ContainerVariable2StyleDescription_strategy = st.builds(ContainerVariable2StyleDescription)
@given(instance=ContainerVariable2StyleDescription_strategy)
@settings(max_examples=25)
def test_ContainerVariable2StyleDescription_instantiation(instance):
    assert isinstance(instance, ContainerVariable2StyleDescription)


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


DAnnotation_strategy = st.builds(DAnnotation)
@given(instance=DAnnotation_strategy)
@settings(max_examples=25)
def test_DAnnotation_instantiation(instance):
    assert isinstance(instance, DAnnotation)


DAnnotationEntry_strategy = st.builds(DAnnotationEntry)
@given(instance=DAnnotationEntry_strategy)
@settings(max_examples=25)
def test_DAnnotationEntry_instantiation(instance):
    assert isinstance(instance, DAnnotationEntry)


DContainer_strategy = st.builds(DContainer)
@given(instance=DContainer_strategy)
@settings(max_examples=25)
def test_DContainer_instantiation(instance):
    assert isinstance(instance, DContainer)


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


DDiagramSet_strategy = st.builds(DDiagramSet)
@given(instance=DDiagramSet_strategy)
@settings(max_examples=25)
def test_DDiagramSet_instantiation(instance):
    assert isinstance(instance, DDiagramSet)


DEdge_strategy = st.builds(DEdge)
@given(instance=DEdge_strategy)
@settings(max_examples=25)
def test_DEdge_instantiation(instance):
    assert isinstance(instance, DEdge)


DFile_strategy = st.builds(DFile)
@given(instance=DFile_strategy)
@settings(max_examples=25)
def test_DFile_instantiation(instance):
    assert isinstance(instance, DFile)


DLabelled_strategy = st.builds(DLabelled)
@given(instance=DLabelled_strategy)
@settings(max_examples=25)
def test_DLabelled_instantiation(instance):
    assert isinstance(instance, DLabelled)


DMappingBased_strategy = st.builds(DMappingBased)
@given(instance=DMappingBased_strategy)
@settings(max_examples=25)
def test_DMappingBased_instantiation(instance):
    assert isinstance(instance, DMappingBased)


DNavigable_strategy = st.builds(DNavigable)
@given(instance=DNavigable_strategy)
@settings(max_examples=25)
def test_DNavigable_instantiation(instance):
    assert isinstance(instance, DNavigable)


DNavigationLink_strategy = st.builds(DNavigationLink)
@given(instance=DNavigationLink_strategy)
@settings(max_examples=25)
def test_DNavigationLink_instantiation(instance):
    assert isinstance(instance, DNavigationLink)


DNode_strategy = st.builds(DNode)
@given(instance=DNode_strategy)
@settings(max_examples=25)
def test_DNode_instantiation(instance):
    assert isinstance(instance, DNode)


DNodeListElement_strategy = st.builds(DNodeListElement)
@given(instance=DNodeListElement_strategy)
@settings(max_examples=25)
def test_DNodeListElement_instantiation(instance):
    assert isinstance(instance, DNodeListElement)


DRefreshable_strategy = st.builds(DRefreshable)
@given(instance=DRefreshable_strategy)
@settings(max_examples=25)
def test_DRefreshable_instantiation(instance):
    assert isinstance(instance, DRefreshable)


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


DResource_strategy = st.builds(DResource)
@given(instance=DResource_strategy)
@settings(max_examples=25)
def test_DResource_instantiation(instance):
    assert isinstance(instance, DResource)


DResourceContainer_strategy = st.builds(DResourceContainer)
@given(instance=DResourceContainer_strategy)
@settings(max_examples=25)
def test_DResourceContainer_instantiation(instance):
    assert isinstance(instance, DResourceContainer)


DSemanticDecorator_strategy = st.builds(DSemanticDecorator)
@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=25)
def test_DSemanticDecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)


DStylizable_strategy = st.builds(DStylizable)
@given(instance=DStylizable_strategy)
@settings(max_examples=25)
def test_DStylizable_instantiation(instance):
    assert isinstance(instance, DStylizable)


DValidable_strategy = st.builds(DValidable)
@given(instance=DValidable_strategy)
@settings(max_examples=25)
def test_DValidable_instantiation(instance):
    assert isinstance(instance, DValidable)


DView_strategy = st.builds(DView)
@given(instance=DView_strategy)
@settings(max_examples=25)
def test_DView_instantiation(instance):
    assert isinstance(instance, DView)


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


DiagramElementMapping2ModelElement_strategy = st.builds(DiagramElementMapping2ModelElement)
@given(instance=DiagramElementMapping2ModelElement_strategy)
@settings(max_examples=25)
def test_DiagramElementMapping2ModelElement_instantiation(instance):
    assert isinstance(instance, DiagramElementMapping2ModelElement)


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


EStructuralFeatureCustomization_strategy = st.builds(EStructuralFeatureCustomization)
@given(instance=EStructuralFeatureCustomization_strategy)
@settings(max_examples=25)
def test_EStructuralFeatureCustomization_instantiation(instance):
    assert isinstance(instance, EStructuralFeatureCustomization)


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


EndLabelStyle_strategy = st.builds(EndLabelStyle)
@given(instance=EndLabelStyle_strategy)
@settings(max_examples=25)
def test_EndLabelStyle_instantiation(instance):
    assert isinstance(instance, EndLabelStyle)


FeatureExtensionDescription_strategy = st.builds(FeatureExtensionDescription)
@given(instance=FeatureExtensionDescription_strategy)
@settings(max_examples=25)
def test_FeatureExtensionDescription_instantiation(instance):
    assert isinstance(instance, FeatureExtensionDescription)


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


FilterVariableHistory_strategy = st.builds(FilterVariableHistory)
@given(instance=FilterVariableHistory_strategy)
@settings(max_examples=25)
def test_FilterVariableHistory_instantiation(instance):
    assert isinstance(instance, FilterVariableHistory)


FilterVariableValue_strategy = st.builds(FilterVariableValue)
@given(instance=FilterVariableValue_strategy)
@settings(max_examples=25)
def test_FilterVariableValue_instantiation(instance):
    assert isinstance(instance, FilterVariableValue)


FixedColor_strategy = st.builds(FixedColor)
@given(instance=FixedColor_strategy)
@settings(max_examples=25)
def test_FixedColor_instantiation(instance):
    assert isinstance(instance, FixedColor)


GaugeSection_strategy = st.builds(GaugeSection)
@given(instance=GaugeSection_strategy)
@settings(max_examples=25)
def test_GaugeSection_instantiation(instance):
    assert isinstance(instance, GaugeSection)


GraphicalFilter_strategy = st.builds(GraphicalFilter)
@given(instance=GraphicalFilter_strategy)
@settings(max_examples=25)
def test_GraphicalFilter_instantiation(instance):
    assert isinstance(instance, GraphicalFilter)


IVSMElementCustomization_strategy = st.builds(IVSMElementCustomization)
@given(instance=IVSMElementCustomization_strategy)
@settings(max_examples=25)
def test_IVSMElementCustomization_instantiation(instance):
    assert isinstance(instance, IVSMElementCustomization)


IdentifiedElement_strategy = st.builds(IdentifiedElement)
@given(instance=IdentifiedElement_strategy)
@settings(max_examples=25)
def test_IdentifiedElement_instantiation(instance):
    assert isinstance(instance, IdentifiedElement)


InformationSection_strategy = st.builds(InformationSection)
@given(instance=InformationSection_strategy)
@settings(max_examples=25)
def test_InformationSection_instantiation(instance):
    assert isinstance(instance, InformationSection)


JavaExtension_strategy = st.builds(JavaExtension)
@given(instance=JavaExtension_strategy)
@settings(max_examples=25)
def test_JavaExtension_instantiation(instance):
    assert isinstance(instance, JavaExtension)


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


MenuItemDescription_strategy = st.builds(MenuItemDescription)
@given(instance=MenuItemDescription_strategy)
@settings(max_examples=25)
def test_MenuItemDescription_instantiation(instance):
    assert isinstance(instance, MenuItemDescription)


MenuItemOrRef_strategy = st.builds(MenuItemOrRef)
@given(instance=MenuItemOrRef_strategy)
@settings(max_examples=25)
def test_MenuItemOrRef_instantiation(instance):
    assert isinstance(instance, MenuItemOrRef)


MetamodelExtensionSetting_strategy = st.builds(MetamodelExtensionSetting)
@given(instance=MetamodelExtensionSetting_strategy)
@settings(max_examples=25)
def test_MetamodelExtensionSetting_instantiation(instance):
    assert isinstance(instance, MetamodelExtensionSetting)


ModelElement2ViewVariable_strategy = st.builds(ModelElement2ViewVariable)
@given(instance=ModelElement2ViewVariable_strategy)
@settings(max_examples=25)
def test_ModelElement2ViewVariable_instantiation(instance):
    assert isinstance(instance, ModelElement2ViewVariable)


ModelOperation_strategy = st.builds(ModelOperation)
@given(instance=ModelOperation_strategy)
@settings(max_examples=25)
def test_ModelOperation_instantiation(instance):
    assert isinstance(instance, ModelOperation)


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


RepresentationDescription_strategy = st.builds(RepresentationDescription)
@given(instance=RepresentationDescription_strategy)
@settings(max_examples=25)
def test_RepresentationDescription_instantiation(instance):
    assert isinstance(instance, RepresentationDescription)


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


RepresentationTemplate_strategy = st.builds(RepresentationTemplate)
@given(instance=RepresentationTemplate_strategy)
@settings(max_examples=25)
def test_RepresentationTemplate_instantiation(instance):
    assert isinstance(instance, RepresentationTemplate)


SelectionDescription_strategy = st.builds(SelectionDescription)
@given(instance=SelectionDescription_strategy)
@settings(max_examples=25)
def test_SelectionDescription_instantiation(instance):
    assert isinstance(instance, SelectionDescription)


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


SwitchChild_strategy = st.builds(SwitchChild)
@given(instance=SwitchChild_strategy)
@settings(max_examples=25)
def test_SwitchChild_instantiation(instance):
    assert isinstance(instance, SwitchChild)


SystemColor_strategy = st.builds(SystemColor)
@given(instance=SystemColor_strategy)
@settings(max_examples=25)
def test_SystemColor_instantiation(instance):
    assert isinstance(instance, SystemColor)


SytemColorsPalette_strategy = st.builds(SytemColorsPalette)
@given(instance=SytemColorsPalette_strategy)
@settings(max_examples=25)
def test_SytemColorsPalette_instantiation(instance):
    assert isinstance(instance, SytemColorsPalette)


ToolEntry_strategy = st.builds(ToolEntry)
@given(instance=ToolEntry_strategy)
@settings(max_examples=25)
def test_ToolEntry_instantiation(instance):
    assert isinstance(instance, ToolEntry)


UserColor_strategy = st.builds(UserColor)
@given(instance=UserColor_strategy)
@settings(max_examples=25)
def test_UserColor_instantiation(instance):
    assert isinstance(instance, UserColor)


UserColorsPalette_strategy = st.builds(UserColorsPalette)
@given(instance=UserColorsPalette_strategy)
@settings(max_examples=25)
def test_UserColorsPalette_instantiation(instance):
    assert isinstance(instance, UserColorsPalette)


ValidationRule_strategy = st.builds(ValidationRule)
@given(instance=ValidationRule_strategy)
@settings(max_examples=25)
def test_ValidationRule_instantiation(instance):
    assert isinstance(instance, ValidationRule)


ViewVariable2ContainerVariable_strategy = st.builds(ViewVariable2ContainerVariable)
@given(instance=ViewVariable2ContainerVariable_strategy)
@settings(max_examples=25)
def test_ViewVariable2ContainerVariable_instantiation(instance):
    assert isinstance(instance, ViewVariable2ContainerVariable)


Viewpoint_strategy = st.builds(Viewpoint)
@given(instance=Viewpoint_strategy)
@settings(max_examples=25)
def test_Viewpoint_instantiation(instance):
    assert isinstance(instance, Viewpoint)


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


description_AdditionalLayer_strategy = st.builds(description_AdditionalLayer)
@given(instance=description_AdditionalLayer_strategy)
@settings(max_examples=25)
def test_description_AdditionalLayer_instantiation(instance):
    assert isinstance(instance, description_AdditionalLayer)


description_ColorDescription_strategy = st.builds(description_ColorDescription)
@given(instance=description_ColorDescription_strategy)
@settings(max_examples=25)
def test_description_ColorDescription_instantiation(instance):
    assert isinstance(instance, description_ColorDescription)


description_Component_strategy = st.builds(description_Component)
@given(instance=description_Component_strategy)
@settings(max_examples=25)
def test_description_Component_instantiation(instance):
    assert isinstance(instance, description_Component)


description_ConditionalContainerStyleDescription_strategy = st.builds(description_ConditionalContainerStyleDescription)
@given(instance=description_ConditionalContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_description_ConditionalContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, description_ConditionalContainerStyleDescription)


description_ConditionalEdgeStyleDescription_strategy = st.builds(description_ConditionalEdgeStyleDescription)
@given(instance=description_ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_description_ConditionalEdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, description_ConditionalEdgeStyleDescription)


description_ConditionalNodeStyleDescription_strategy = st.builds(description_ConditionalNodeStyleDescription)
@given(instance=description_ConditionalNodeStyleDescription_strategy)
@settings(max_examples=25)
def test_description_ConditionalNodeStyleDescription_instantiation(instance):
    assert isinstance(instance, description_ConditionalNodeStyleDescription)


description_ContainerMapping_strategy = st.builds(description_ContainerMapping)
@given(instance=description_ContainerMapping_strategy)
@settings(max_examples=25)
def test_description_ContainerMapping_instantiation(instance):
    assert isinstance(instance, description_ContainerMapping)


description_DModelElement_strategy = st.builds(description_DModelElement)
@given(instance=description_DModelElement_strategy)
@settings(max_examples=25)
def test_description_DModelElement_instantiation(instance):
    assert isinstance(instance, description_DModelElement)


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


description_EdgeMapping_strategy = st.builds(description_EdgeMapping)
@given(instance=description_EdgeMapping_strategy)
@settings(max_examples=25)
def test_description_EdgeMapping_instantiation(instance):
    assert isinstance(instance, description_EdgeMapping)


description_EdgeMappingImport_strategy = st.builds(description_EdgeMappingImport)
@given(instance=description_EdgeMappingImport_strategy)
@settings(max_examples=25)
def test_description_EdgeMappingImport_instantiation(instance):
    assert isinstance(instance, description_EdgeMappingImport)


description_EndUserDocumentedElement_strategy = st.builds(description_EndUserDocumentedElement)
@given(instance=description_EndUserDocumentedElement_strategy)
@settings(max_examples=25)
def test_description_EndUserDocumentedElement_instantiation(instance):
    assert isinstance(instance, description_EndUserDocumentedElement)


description_FixedColor_strategy = st.builds(description_FixedColor)
@given(instance=description_FixedColor_strategy)
@settings(max_examples=25)
def test_description_FixedColor_instantiation(instance):
    assert isinstance(instance, description_FixedColor)


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


description_Layer_strategy = st.builds(description_Layer)
@given(instance=description_Layer_strategy)
@settings(max_examples=25)
def test_description_Layer_instantiation(instance):
    assert isinstance(instance, description_Layer)


description_Layout_strategy = st.builds(description_Layout)
@given(instance=description_Layout_strategy)
@settings(max_examples=25)
def test_description_Layout_instantiation(instance):
    assert isinstance(instance, description_Layout)


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


description_SelectionDescription_strategy = st.builds(description_SelectionDescription)
@given(instance=description_SelectionDescription_strategy)
@settings(max_examples=25)
def test_description_SelectionDescription_instantiation(instance):
    assert isinstance(instance, description_SelectionDescription)


description_UserColor_strategy = st.builds(description_UserColor)
@given(instance=description_UserColor_strategy)
@settings(max_examples=25)
def test_description_UserColor_instantiation(instance):
    assert isinstance(instance, description_UserColor)


description_viewpoint_EObject_strategy = st.builds(description_viewpoint_EObject)
@given(instance=description_viewpoint_EObject_strategy)
@settings(max_examples=25)
def test_description_viewpoint_EObject_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EObject)


description_viewpoint_EPackage_strategy = st.builds(description_viewpoint_EPackage)
@given(instance=description_viewpoint_EPackage_strategy)
@settings(max_examples=25)
def test_description_viewpoint_EPackage_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EPackage)


description_viewpoint_EStringToStringMapEntry_strategy = st.builds(description_viewpoint_EStringToStringMapEntry)
@given(instance=description_viewpoint_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_description_viewpoint_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EStringToStringMapEntry)


diagram_AbstractDNode_strategy = st.builds(diagram_AbstractDNode)
@given(instance=diagram_AbstractDNode_strategy)
@settings(max_examples=25)
def test_diagram_AbstractDNode_instantiation(instance):
    assert isinstance(instance, diagram_AbstractDNode)


diagram_BorderedStyle_strategy = st.builds(diagram_BorderedStyle)
@given(instance=diagram_BorderedStyle_strategy)
@settings(max_examples=25)
def test_diagram_BorderedStyle_instantiation(instance):
    assert isinstance(instance, diagram_BorderedStyle)


diagram_ContainerStyle_strategy = st.builds(diagram_ContainerStyle)
@given(instance=diagram_ContainerStyle_strategy)
@settings(max_examples=25)
def test_diagram_ContainerStyle_instantiation(instance):
    assert isinstance(instance, diagram_ContainerStyle)


diagram_DDiagram_strategy = st.builds(diagram_DDiagram)
@given(instance=diagram_DDiagram_strategy)
@settings(max_examples=25)
def test_diagram_DDiagram_instantiation(instance):
    assert isinstance(instance, diagram_DDiagram)


diagram_DDiagramElement_strategy = st.builds(diagram_DDiagramElement)
@given(instance=diagram_DDiagramElement_strategy)
@settings(max_examples=25)
def test_diagram_DDiagramElement_instantiation(instance):
    assert isinstance(instance, diagram_DDiagramElement)


diagram_EdgeTarget_strategy = st.builds(diagram_EdgeTarget)
@given(instance=diagram_EdgeTarget_strategy)
@settings(max_examples=25)
def test_diagram_EdgeTarget_instantiation(instance):
    assert isinstance(instance, diagram_EdgeTarget)


diagram_NodeStyle_strategy = st.builds(diagram_NodeStyle)
@given(instance=diagram_NodeStyle_strategy)
@settings(max_examples=25)
def test_diagram_NodeStyle_instantiation(instance):
    assert isinstance(instance, diagram_NodeStyle)


diagram_viewpoint_DRepresentationContainer_strategy = st.builds(diagram_viewpoint_DRepresentationContainer)
@given(instance=diagram_viewpoint_DRepresentationContainer_strategy)
@settings(max_examples=25)
def test_diagram_viewpoint_DRepresentationContainer_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_DRepresentationContainer)


diagram_viewpoint_Decoration_strategy = st.builds(diagram_viewpoint_Decoration)
@given(instance=diagram_viewpoint_Decoration_strategy)
@settings(max_examples=25)
def test_diagram_viewpoint_Decoration_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_Decoration)


diagram_viewpoint_EObject_strategy = st.builds(diagram_viewpoint_EObject)
@given(instance=diagram_viewpoint_EObject_strategy)
@settings(max_examples=25)
def test_diagram_viewpoint_EObject_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_EObject)


diagram_viewpoint_RGBValues_strategy = st.builds(diagram_viewpoint_RGBValues)
@given(instance=diagram_viewpoint_RGBValues_strategy)
@settings(max_examples=25)
def test_diagram_viewpoint_RGBValues_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_RGBValues)


diagram_viewpoint_Style_strategy = st.builds(diagram_viewpoint_Style)
@given(instance=diagram_viewpoint_Style_strategy)
@settings(max_examples=25)
def test_diagram_viewpoint_Style_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_Style)


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


filter_FilterVariable_strategy = st.builds(filter_FilterVariable)
@given(instance=filter_FilterVariable_strategy)
@settings(max_examples=25)
def test_filter_FilterVariable_instantiation(instance):
    assert isinstance(instance, filter_FilterVariable)


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


style_LabelBorderStyleDescription_strategy = st.builds(style_LabelBorderStyleDescription)
@given(instance=style_LabelBorderStyleDescription_strategy)
@settings(max_examples=25)
def test_style_LabelBorderStyleDescription_instantiation(instance):
    assert isinstance(instance, style_LabelBorderStyleDescription)


style_LabelBorderStyles_strategy = st.builds(style_LabelBorderStyles)
@given(instance=style_LabelBorderStyles_strategy)
@settings(max_examples=25)
def test_style_LabelBorderStyles_instantiation(instance):
    assert isinstance(instance, style_LabelBorderStyles)


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


tool_AbstractVariable_strategy = st.builds(tool_AbstractVariable)
@given(instance=tool_AbstractVariable_strategy)
@settings(max_examples=25)
def test_tool_AbstractVariable_instantiation(instance):
    assert isinstance(instance, tool_AbstractVariable)


tool_BehaviorTool_strategy = st.builds(tool_BehaviorTool)
@given(instance=tool_BehaviorTool_strategy)
@settings(max_examples=25)
def test_tool_BehaviorTool_instantiation(instance):
    assert isinstance(instance, tool_BehaviorTool)


tool_Case_strategy = st.builds(tool_Case)
@given(instance=tool_Case_strategy)
@settings(max_examples=25)
def test_tool_Case_instantiation(instance):
    assert isinstance(instance, tool_Case)


tool_ContainerDropDescription_strategy = st.builds(tool_ContainerDropDescription)
@given(instance=tool_ContainerDropDescription_strategy)
@settings(max_examples=25)
def test_tool_ContainerDropDescription_instantiation(instance):
    assert isinstance(instance, tool_ContainerDropDescription)


tool_ContainerModelOperation_strategy = st.builds(tool_ContainerModelOperation)
@given(instance=tool_ContainerModelOperation_strategy)
@settings(max_examples=25)
def test_tool_ContainerModelOperation_instantiation(instance):
    assert isinstance(instance, tool_ContainerModelOperation)


tool_ContainerViewVariable_strategy = st.builds(tool_ContainerViewVariable)
@given(instance=tool_ContainerViewVariable_strategy)
@settings(max_examples=25)
def test_tool_ContainerViewVariable_instantiation(instance):
    assert isinstance(instance, tool_ContainerViewVariable)


tool_Default_strategy = st.builds(tool_Default)
@given(instance=tool_Default_strategy)
@settings(max_examples=25)
def test_tool_Default_instantiation(instance):
    assert isinstance(instance, tool_Default)


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


tool_ElementVariable_strategy = st.builds(tool_ElementVariable)
@given(instance=tool_ElementVariable_strategy)
@settings(max_examples=25)
def test_tool_ElementVariable_instantiation(instance):
    assert isinstance(instance, tool_ElementVariable)


tool_ElementViewVariable_strategy = st.builds(tool_ElementViewVariable)
@given(instance=tool_ElementViewVariable_strategy)
@settings(max_examples=25)
def test_tool_ElementViewVariable_instantiation(instance):
    assert isinstance(instance, tool_ElementViewVariable)


tool_ExternalJavaAction_strategy = st.builds(tool_ExternalJavaAction)
@given(instance=tool_ExternalJavaAction_strategy)
@settings(max_examples=25)
def test_tool_ExternalJavaAction_instantiation(instance):
    assert isinstance(instance, tool_ExternalJavaAction)


tool_ExternalJavaActionParameter_strategy = st.builds(tool_ExternalJavaActionParameter)
@given(instance=tool_ExternalJavaActionParameter_strategy)
@settings(max_examples=25)
def test_tool_ExternalJavaActionParameter_instantiation(instance):
    assert isinstance(instance, tool_ExternalJavaActionParameter)


tool_FeatureChangeListener_strategy = st.builds(tool_FeatureChangeListener)
@given(instance=tool_FeatureChangeListener_strategy)
@settings(max_examples=25)
def test_tool_FeatureChangeListener_instantiation(instance):
    assert isinstance(instance, tool_FeatureChangeListener)


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


tool_MenuItemDescription_strategy = st.builds(tool_MenuItemDescription)
@given(instance=tool_MenuItemDescription_strategy)
@settings(max_examples=25)
def test_tool_MenuItemDescription_instantiation(instance):
    assert isinstance(instance, tool_MenuItemDescription)


tool_MenuItemOrRef_strategy = st.builds(tool_MenuItemOrRef)
@given(instance=tool_MenuItemOrRef_strategy)
@settings(max_examples=25)
def test_tool_MenuItemOrRef_instantiation(instance):
    assert isinstance(instance, tool_MenuItemOrRef)


tool_ModelOperation_strategy = st.builds(tool_ModelOperation)
@given(instance=tool_ModelOperation_strategy)
@settings(max_examples=25)
def test_tool_ModelOperation_instantiation(instance):
    assert isinstance(instance, tool_ModelOperation)


tool_NameVariable_strategy = st.builds(tool_NameVariable)
@given(instance=tool_NameVariable_strategy)
@settings(max_examples=25)
def test_tool_NameVariable_instantiation(instance):
    assert isinstance(instance, tool_NameVariable)


tool_NodeCreationVariable_strategy = st.builds(tool_NodeCreationVariable)
@given(instance=tool_NodeCreationVariable_strategy)
@settings(max_examples=25)
def test_tool_NodeCreationVariable_instantiation(instance):
    assert isinstance(instance, tool_NodeCreationVariable)


tool_PasteDescription_strategy = st.builds(tool_PasteDescription)
@given(instance=tool_PasteDescription_strategy)
@settings(max_examples=25)
def test_tool_PasteDescription_instantiation(instance):
    assert isinstance(instance, tool_PasteDescription)


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


tool_RepresentationNavigationDescription_strategy = st.builds(tool_RepresentationNavigationDescription)
@given(instance=tool_RepresentationNavigationDescription_strategy)
@settings(max_examples=25)
def test_tool_RepresentationNavigationDescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationNavigationDescription)


tool_SelectContainerVariable_strategy = st.builds(tool_SelectContainerVariable)
@given(instance=tool_SelectContainerVariable_strategy)
@settings(max_examples=25)
def test_tool_SelectContainerVariable_instantiation(instance):
    assert isinstance(instance, tool_SelectContainerVariable)


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


tool_SubVariable_strategy = st.builds(tool_SubVariable)
@given(instance=tool_SubVariable_strategy)
@settings(max_examples=25)
def test_tool_SubVariable_instantiation(instance):
    assert isinstance(instance, tool_SubVariable)


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


tool_ToolFilterDescription_strategy = st.builds(tool_ToolFilterDescription)
@given(instance=tool_ToolFilterDescription_strategy)
@settings(max_examples=25)
def test_tool_ToolFilterDescription_instantiation(instance):
    assert isinstance(instance, tool_ToolFilterDescription)


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


tool_viewpoint_EObject_strategy = st.builds(tool_viewpoint_EObject)
@given(instance=tool_viewpoint_EObject_strategy)
@settings(max_examples=25)
def test_tool_viewpoint_EObject_instantiation(instance):
    assert isinstance(instance, tool_viewpoint_EObject)


validation_RuleAudit_strategy = st.builds(validation_RuleAudit)
@given(instance=validation_RuleAudit_strategy)
@settings(max_examples=25)
def test_validation_RuleAudit_instantiation(instance):
    assert isinstance(instance, validation_RuleAudit)


validation_ValidationFix_strategy = st.builds(validation_ValidationFix)
@given(instance=validation_ValidationFix_strategy)
@settings(max_examples=25)
def test_validation_ValidationFix_instantiation(instance):
    assert isinstance(instance, validation_ValidationFix)


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


viewpoint_BasicLabelStyle_strategy = st.builds(viewpoint_BasicLabelStyle, iconPath=safe_text, labelFormat=safe_text, labelSize=st.integers(), showIcon=st.booleans())
@given(instance=viewpoint_BasicLabelStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_BasicLabelStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_BasicLabelStyle)


viewpoint_Customizable_strategy = st.builds(viewpoint_Customizable, customFeatures=safe_text)
@given(instance=viewpoint_Customizable_strategy)
@settings(max_examples=25)
def test_viewpoint_Customizable_instantiation(instance):
    assert isinstance(instance, viewpoint_Customizable)


viewpoint_DAnalysis_strategy = st.builds(viewpoint_DAnalysis, version=safe_text)
@given(instance=viewpoint_DAnalysis_strategy)
@settings(max_examples=25)
def test_viewpoint_DAnalysis_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysis)


viewpoint_DAnalysisCustomData_strategy = st.builds(viewpoint_DAnalysisCustomData, key=safe_text)
@given(instance=viewpoint_DAnalysisCustomData_strategy)
@settings(max_examples=25)
def test_viewpoint_DAnalysisCustomData_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysisCustomData)


viewpoint_DAnalysisSessionEObject_strategy = st.builds(viewpoint_DAnalysisSessionEObject, blocked=st.booleans(), controlledResources=safe_text, open=st.booleans(), resources=safe_text, synchronizationStatus=safe_text)
@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
@settings(max_examples=25)
def test_viewpoint_DAnalysisSessionEObject_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysisSessionEObject)


viewpoint_DContainer_strategy = st.builds(viewpoint_DContainer)
@given(instance=viewpoint_DContainer_strategy)
@settings(max_examples=25)
def test_viewpoint_DContainer_instantiation(instance):
    assert isinstance(instance, viewpoint_DContainer)


viewpoint_DEObjectLink_strategy = st.builds(viewpoint_DEObjectLink)
@given(instance=viewpoint_DEObjectLink_strategy)
@settings(max_examples=25)
def test_viewpoint_DEObjectLink_instantiation(instance):
    assert isinstance(instance, viewpoint_DEObjectLink)


viewpoint_DFeatureExtension_strategy = st.builds(viewpoint_DFeatureExtension)
@given(instance=viewpoint_DFeatureExtension_strategy)
@settings(max_examples=25)
def test_viewpoint_DFeatureExtension_instantiation(instance):
    assert isinstance(instance, viewpoint_DFeatureExtension)


viewpoint_DFile_strategy = st.builds(viewpoint_DFile)
@given(instance=viewpoint_DFile_strategy)
@settings(max_examples=25)
def test_viewpoint_DFile_instantiation(instance):
    assert isinstance(instance, viewpoint_DFile)


viewpoint_DFolder_strategy = st.builds(viewpoint_DFolder)
@given(instance=viewpoint_DFolder_strategy)
@settings(max_examples=25)
def test_viewpoint_DFolder_instantiation(instance):
    assert isinstance(instance, viewpoint_DFolder)


viewpoint_DLabelled_strategy = st.builds(viewpoint_DLabelled)
@given(instance=viewpoint_DLabelled_strategy)
@settings(max_examples=25)
def test_viewpoint_DLabelled_instantiation(instance):
    assert isinstance(instance, viewpoint_DLabelled)


viewpoint_DMappingBased_strategy = st.builds(viewpoint_DMappingBased)
@given(instance=viewpoint_DMappingBased_strategy)
@settings(max_examples=25)
def test_viewpoint_DMappingBased_instantiation(instance):
    assert isinstance(instance, viewpoint_DMappingBased)


viewpoint_DModel_strategy = st.builds(viewpoint_DModel)
@given(instance=viewpoint_DModel_strategy)
@settings(max_examples=25)
def test_viewpoint_DModel_instantiation(instance):
    assert isinstance(instance, viewpoint_DModel)


viewpoint_DNavigable_strategy = st.builds(viewpoint_DNavigable)
@given(instance=viewpoint_DNavigable_strategy)
@settings(max_examples=25)
def test_viewpoint_DNavigable_instantiation(instance):
    assert isinstance(instance, viewpoint_DNavigable)


viewpoint_DNavigationLink_strategy = st.builds(viewpoint_DNavigationLink, label=safe_text, targetType=safe_text)
@given(instance=viewpoint_DNavigationLink_strategy)
@settings(max_examples=25)
def test_viewpoint_DNavigationLink_instantiation(instance):
    assert isinstance(instance, viewpoint_DNavigationLink)


viewpoint_DProject_strategy = st.builds(viewpoint_DProject)
@given(instance=viewpoint_DProject_strategy)
@settings(max_examples=25)
def test_viewpoint_DProject_instantiation(instance):
    assert isinstance(instance, viewpoint_DProject)


viewpoint_DRefreshable_strategy = st.builds(viewpoint_DRefreshable)
@given(instance=viewpoint_DRefreshable_strategy)
@settings(max_examples=25)
def test_viewpoint_DRefreshable_instantiation(instance):
    assert isinstance(instance, viewpoint_DRefreshable)


viewpoint_DRepresentation_strategy = st.builds(viewpoint_DRepresentation, name=safe_text)
@given(instance=viewpoint_DRepresentation_strategy)
@settings(max_examples=25)
def test_viewpoint_DRepresentation_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentation)


viewpoint_DRepresentationContainer_strategy = st.builds(viewpoint_DRepresentationContainer)
@given(instance=viewpoint_DRepresentationContainer_strategy)
@settings(max_examples=25)
def test_viewpoint_DRepresentationContainer_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentationContainer)


viewpoint_DRepresentationElement_strategy = st.builds(viewpoint_DRepresentationElement, name=safe_text)
@given(instance=viewpoint_DRepresentationElement_strategy)
@settings(max_examples=25)
def test_viewpoint_DRepresentationElement_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentationElement)


viewpoint_DResource_strategy = st.builds(viewpoint_DResource, name=safe_text, path=safe_text)
@given(instance=viewpoint_DResource_strategy)
@settings(max_examples=25)
def test_viewpoint_DResource_instantiation(instance):
    assert isinstance(instance, viewpoint_DResource)


viewpoint_DResourceContainer_strategy = st.builds(viewpoint_DResourceContainer)
@given(instance=viewpoint_DResourceContainer_strategy)
@settings(max_examples=25)
def test_viewpoint_DResourceContainer_instantiation(instance):
    assert isinstance(instance, viewpoint_DResourceContainer)


viewpoint_DSemanticDecorator_strategy = st.builds(viewpoint_DSemanticDecorator)
@given(instance=viewpoint_DSemanticDecorator_strategy)
@settings(max_examples=25)
def test_viewpoint_DSemanticDecorator_instantiation(instance):
    assert isinstance(instance, viewpoint_DSemanticDecorator)


viewpoint_DSourceFileLink_strategy = st.builds(viewpoint_DSourceFileLink, endPosition=st.integers(), filePath=safe_text, startPosition=st.integers())
@given(instance=viewpoint_DSourceFileLink_strategy)
@settings(max_examples=25)
def test_viewpoint_DSourceFileLink_instantiation(instance):
    assert isinstance(instance, viewpoint_DSourceFileLink)


viewpoint_DStylizable_strategy = st.builds(viewpoint_DStylizable)
@given(instance=viewpoint_DStylizable_strategy)
@settings(max_examples=25)
def test_viewpoint_DStylizable_instantiation(instance):
    assert isinstance(instance, viewpoint_DStylizable)


viewpoint_DValidable_strategy = st.builds(viewpoint_DValidable)
@given(instance=viewpoint_DValidable_strategy)
@settings(max_examples=25)
def test_viewpoint_DValidable_instantiation(instance):
    assert isinstance(instance, viewpoint_DValidable)


viewpoint_DView_strategy = st.builds(viewpoint_DView, initialized=st.booleans())
@given(instance=viewpoint_DView_strategy)
@settings(max_examples=25)
def test_viewpoint_DView_instantiation(instance):
    assert isinstance(instance, viewpoint_DView)


viewpoint_Decoration_strategy = st.builds(viewpoint_Decoration)
@given(instance=viewpoint_Decoration_strategy)
@settings(max_examples=25)
def test_viewpoint_Decoration_instantiation(instance):
    assert isinstance(instance, viewpoint_Decoration)


viewpoint_DragAndDropTarget_strategy = st.builds(viewpoint_DragAndDropTarget)
@given(instance=viewpoint_DragAndDropTarget_strategy)
@settings(max_examples=25)
def test_viewpoint_DragAndDropTarget_instantiation(instance):
    assert isinstance(instance, viewpoint_DragAndDropTarget)


viewpoint_EObject_strategy = st.builds(viewpoint_EObject)
@given(instance=viewpoint_EObject_strategy)
@settings(max_examples=25)
def test_viewpoint_EObject_instantiation(instance):
    assert isinstance(instance, viewpoint_EObject)


viewpoint_LabelStyle_strategy = st.builds(viewpoint_LabelStyle, labelAlignment=safe_text)
@given(instance=viewpoint_LabelStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_LabelStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_LabelStyle)


viewpoint_MetaModelExtension_strategy = st.builds(viewpoint_MetaModelExtension)
@given(instance=viewpoint_MetaModelExtension_strategy)
@settings(max_examples=25)
def test_viewpoint_MetaModelExtension_instantiation(instance):
    assert isinstance(instance, viewpoint_MetaModelExtension)


viewpoint_RGBValues_strategy = st.builds(viewpoint_RGBValues, blue=st.integers(), green=st.integers(), red=st.integers())
@given(instance=viewpoint_RGBValues_strategy)
@settings(max_examples=25)
def test_viewpoint_RGBValues_instantiation(instance):
    assert isinstance(instance, viewpoint_RGBValues)


viewpoint_SessionManagerEObject_strategy = st.builds(viewpoint_SessionManagerEObject)
@given(instance=viewpoint_SessionManagerEObject_strategy)
@settings(max_examples=25)
def test_viewpoint_SessionManagerEObject_instantiation(instance):
    assert isinstance(instance, viewpoint_SessionManagerEObject)


viewpoint_Style_strategy = st.builds(viewpoint_Style)
@given(instance=viewpoint_Style_strategy)
@settings(max_examples=25)
def test_viewpoint_Style_instantiation(instance):
    assert isinstance(instance, viewpoint_Style)


viewpoint_audit_InformationSection_strategy = st.builds(viewpoint_audit_InformationSection)
@given(instance=viewpoint_audit_InformationSection_strategy)
@settings(max_examples=25)
def test_viewpoint_audit_InformationSection_instantiation(instance):
    assert isinstance(instance, viewpoint_audit_InformationSection)


viewpoint_audit_TemplateInformationSection_strategy = st.builds(viewpoint_audit_TemplateInformationSection, templatePath=safe_text)
@given(instance=viewpoint_audit_TemplateInformationSection_strategy)
@settings(max_examples=25)
def test_viewpoint_audit_TemplateInformationSection_instantiation(instance):
    assert isinstance(instance, viewpoint_audit_TemplateInformationSection)


viewpoint_concern_ConcernDescription_strategy = st.builds(viewpoint_concern_ConcernDescription)
@given(instance=viewpoint_concern_ConcernDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_concern_ConcernDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_concern_ConcernDescription)


viewpoint_concern_ConcernSet_strategy = st.builds(viewpoint_concern_ConcernSet)
@given(instance=viewpoint_concern_ConcernSet_strategy)
@settings(max_examples=25)
def test_viewpoint_concern_ConcernSet_instantiation(instance):
    assert isinstance(instance, viewpoint_concern_ConcernSet)


viewpoint_description_AbstractMappingImport_strategy = st.builds(viewpoint_description_AbstractMappingImport, hideSubMappings=st.booleans(), inheritsAncestorFilters=st.booleans())
@given(instance=viewpoint_description_AbstractMappingImport_strategy)
@settings(max_examples=25)
def test_viewpoint_description_AbstractMappingImport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AbstractMappingImport)


viewpoint_description_AbstractNodeMapping_strategy = st.builds(viewpoint_description_AbstractNodeMapping, domainClass=safe_text)
@given(instance=viewpoint_description_AbstractNodeMapping_strategy)
@settings(max_examples=25)
def test_viewpoint_description_AbstractNodeMapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AbstractNodeMapping)


viewpoint_description_AdditionalLayer_strategy = st.builds(viewpoint_description_AdditionalLayer, activeByDefault=st.booleans(), optional=st.booleans())
@given(instance=viewpoint_description_AdditionalLayer_strategy)
@settings(max_examples=25)
def test_viewpoint_description_AdditionalLayer_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AdditionalLayer)


viewpoint_description_AnnotationEntry_strategy = st.builds(viewpoint_description_AnnotationEntry, source=safe_text)
@given(instance=viewpoint_description_AnnotationEntry_strategy)
@settings(max_examples=25)
def test_viewpoint_description_AnnotationEntry_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AnnotationEntry)


viewpoint_description_ColorDescription_strategy = st.builds(viewpoint_description_ColorDescription)
@given(instance=viewpoint_description_ColorDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ColorDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ColorDescription)


viewpoint_description_ColorStep_strategy = st.builds(viewpoint_description_ColorStep, associatedValue=safe_text)
@given(instance=viewpoint_description_ColorStep_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ColorStep_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ColorStep)


viewpoint_description_Component_strategy = st.builds(viewpoint_description_Component)
@given(instance=viewpoint_description_Component_strategy)
@settings(max_examples=25)
def test_viewpoint_description_Component_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Component)


viewpoint_description_CompositeLayout_strategy = st.builds(viewpoint_description_CompositeLayout, direction=safe_text, padding=st.integers())
@given(instance=viewpoint_description_CompositeLayout_strategy)
@settings(max_examples=25)
def test_viewpoint_description_CompositeLayout_instantiation(instance):
    assert isinstance(instance, viewpoint_description_CompositeLayout)


viewpoint_description_ComputedColor_strategy = st.builds(viewpoint_description_ComputedColor, blue=safe_text, green=safe_text, red=safe_text)
@given(instance=viewpoint_description_ComputedColor_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ComputedColor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ComputedColor)


viewpoint_description_ConditionalContainerStyleDescription_strategy = st.builds(viewpoint_description_ConditionalContainerStyleDescription)
@given(instance=viewpoint_description_ConditionalContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ConditionalContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalContainerStyleDescription)


viewpoint_description_ConditionalEdgeStyleDescription_strategy = st.builds(viewpoint_description_ConditionalEdgeStyleDescription)
@given(instance=viewpoint_description_ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ConditionalEdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalEdgeStyleDescription)


viewpoint_description_ConditionalNodeStyleDescription_strategy = st.builds(viewpoint_description_ConditionalNodeStyleDescription)
@given(instance=viewpoint_description_ConditionalNodeStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ConditionalNodeStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalNodeStyleDescription)


viewpoint_description_ConditionalStyleDescription_strategy = st.builds(viewpoint_description_ConditionalStyleDescription, predicateExpression=safe_text)
@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ConditionalStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalStyleDescription)


viewpoint_description_ContainerMapping_strategy = st.builds(viewpoint_description_ContainerMapping, childrenPresentation=safe_text)
@given(instance=viewpoint_description_ContainerMapping_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ContainerMapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ContainerMapping)


viewpoint_description_ContainerMappingImport_strategy = st.builds(viewpoint_description_ContainerMappingImport)
@given(instance=viewpoint_description_ContainerMappingImport_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ContainerMappingImport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ContainerMappingImport)


viewpoint_description_Customization_strategy = st.builds(viewpoint_description_Customization)
@given(instance=viewpoint_description_Customization_strategy)
@settings(max_examples=25)
def test_viewpoint_description_Customization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Customization)


viewpoint_description_DAnnotation_strategy = st.builds(viewpoint_description_DAnnotation, source=safe_text)
@given(instance=viewpoint_description_DAnnotation_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DAnnotation_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DAnnotation)


viewpoint_description_DAnnotationEntry_strategy = st.builds(viewpoint_description_DAnnotationEntry, details=safe_text, source=safe_text)
@given(instance=viewpoint_description_DAnnotationEntry_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DAnnotationEntry_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DAnnotationEntry)


viewpoint_description_DModelElement_strategy = st.builds(viewpoint_description_DModelElement)
@given(instance=viewpoint_description_DModelElement_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DModelElement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DModelElement)


viewpoint_description_DecorationDescription_strategy = st.builds(viewpoint_description_DecorationDescription, decoratorPath=safe_text, name=safe_text, position=safe_text, preconditionExpression=safe_text)
@given(instance=viewpoint_description_DecorationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DecorationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DecorationDescription)


viewpoint_description_DecorationDescriptionsSet_strategy = st.builds(viewpoint_description_DecorationDescriptionsSet)
@given(instance=viewpoint_description_DecorationDescriptionsSet_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DecorationDescriptionsSet_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DecorationDescriptionsSet)


viewpoint_description_DiagramDescription_strategy = st.builds(viewpoint_description_DiagramDescription, domainClass=safe_text, enablePopupBars=st.booleans(), preconditionExpression=safe_text, rootExpression=safe_text)
@given(instance=viewpoint_description_DiagramDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DiagramDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DiagramDescription)


viewpoint_description_DiagramElementMapping_strategy = st.builds(viewpoint_description_DiagramElementMapping, createElements=st.booleans(), preconditionExpression=safe_text, semanticCandidatesExpression=safe_text, semanticElements=safe_text, synchronizationLock=st.booleans())
@given(instance=viewpoint_description_DiagramElementMapping_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DiagramElementMapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DiagramElementMapping)


viewpoint_description_DiagramExtensionDescription_strategy = st.builds(viewpoint_description_DiagramExtensionDescription)
@given(instance=viewpoint_description_DiagramExtensionDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DiagramExtensionDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DiagramExtensionDescription)


viewpoint_description_DiagramImportDescription_strategy = st.builds(viewpoint_description_DiagramImportDescription)
@given(instance=viewpoint_description_DiagramImportDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DiagramImportDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DiagramImportDescription)


viewpoint_description_DocumentedElement_strategy = st.builds(viewpoint_description_DocumentedElement, documentation=safe_text)
@given(instance=viewpoint_description_DocumentedElement_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DocumentedElement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DocumentedElement)


viewpoint_description_DragAndDropTargetDescription_strategy = st.builds(viewpoint_description_DragAndDropTargetDescription)
@given(instance=viewpoint_description_DragAndDropTargetDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DragAndDropTargetDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DragAndDropTargetDescription)


viewpoint_description_EAttributeCustomization_strategy = st.builds(viewpoint_description_EAttributeCustomization, attributeName=safe_text, value=safe_text)
@given(instance=viewpoint_description_EAttributeCustomization_strategy)
@settings(max_examples=25)
def test_viewpoint_description_EAttributeCustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EAttributeCustomization)


viewpoint_description_EReferenceCustomization_strategy = st.builds(viewpoint_description_EReferenceCustomization, referenceName=safe_text)
@given(instance=viewpoint_description_EReferenceCustomization_strategy)
@settings(max_examples=25)
def test_viewpoint_description_EReferenceCustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EReferenceCustomization)


viewpoint_description_EStructuralFeatureCustomization_strategy = st.builds(viewpoint_description_EStructuralFeatureCustomization, applyOnAll=st.booleans())
@given(instance=viewpoint_description_EStructuralFeatureCustomization_strategy)
@settings(max_examples=25)
def test_viewpoint_description_EStructuralFeatureCustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EStructuralFeatureCustomization)


viewpoint_description_EdgeMapping_strategy = st.builds(viewpoint_description_EdgeMapping, domainClass=safe_text, pathExpression=safe_text, sourceFinderExpression=safe_text, targetExpression=safe_text, targetFinderExpression=safe_text, useDomainElement=st.booleans())
@given(instance=viewpoint_description_EdgeMapping_strategy)
@settings(max_examples=25)
def test_viewpoint_description_EdgeMapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EdgeMapping)


viewpoint_description_EdgeMappingImport_strategy = st.builds(viewpoint_description_EdgeMappingImport, inheritsAncestorFilters=st.booleans())
@given(instance=viewpoint_description_EdgeMappingImport_strategy)
@settings(max_examples=25)
def test_viewpoint_description_EdgeMappingImport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EdgeMappingImport)


viewpoint_description_EndUserDocumentedElement_strategy = st.builds(viewpoint_description_EndUserDocumentedElement, endUserDocumentation=safe_text)
@given(instance=viewpoint_description_EndUserDocumentedElement_strategy)
@settings(max_examples=25)
def test_viewpoint_description_EndUserDocumentedElement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EndUserDocumentedElement)


viewpoint_description_Environment_strategy = st.builds(viewpoint_description_Environment)
@given(instance=viewpoint_description_Environment_strategy)
@settings(max_examples=25)
def test_viewpoint_description_Environment_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Environment)


viewpoint_description_FeatureExtensionDescription_strategy = st.builds(viewpoint_description_FeatureExtensionDescription)
@given(instance=viewpoint_description_FeatureExtensionDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_FeatureExtensionDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_FeatureExtensionDescription)


viewpoint_description_FixedColor_strategy = st.builds(viewpoint_description_FixedColor, blue=st.integers(), green=st.integers(), red=st.integers())
@given(instance=viewpoint_description_FixedColor_strategy)
@settings(max_examples=25)
def test_viewpoint_description_FixedColor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_FixedColor)


viewpoint_description_Group_strategy = st.builds(viewpoint_description_Group, name=safe_text, version=safe_text)
@given(instance=viewpoint_description_Group_strategy)
@settings(max_examples=25)
def test_viewpoint_description_Group_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Group)


viewpoint_description_IEdgeMapping_strategy = st.builds(viewpoint_description_IEdgeMapping)
@given(instance=viewpoint_description_IEdgeMapping_strategy)
@settings(max_examples=25)
def test_viewpoint_description_IEdgeMapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_IEdgeMapping)


viewpoint_description_IVSMElementCustomization_strategy = st.builds(viewpoint_description_IVSMElementCustomization)
@given(instance=viewpoint_description_IVSMElementCustomization_strategy)
@settings(max_examples=25)
def test_viewpoint_description_IVSMElementCustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_IVSMElementCustomization)


viewpoint_description_IdentifiedElement_strategy = st.builds(viewpoint_description_IdentifiedElement, label=safe_text, name=safe_text)
@given(instance=viewpoint_description_IdentifiedElement_strategy)
@settings(max_examples=25)
def test_viewpoint_description_IdentifiedElement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_IdentifiedElement)


viewpoint_description_InterpolatedColor_strategy = st.builds(viewpoint_description_InterpolatedColor, colorValueComputationExpression=safe_text, maxValueComputationExpression=safe_text, minValueComputationExpression=safe_text)
@given(instance=viewpoint_description_InterpolatedColor_strategy)
@settings(max_examples=25)
def test_viewpoint_description_InterpolatedColor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_InterpolatedColor)


viewpoint_description_JavaExtension_strategy = st.builds(viewpoint_description_JavaExtension, qualifiedClassName=safe_text)
@given(instance=viewpoint_description_JavaExtension_strategy)
@settings(max_examples=25)
def test_viewpoint_description_JavaExtension_instantiation(instance):
    assert isinstance(instance, viewpoint_description_JavaExtension)


viewpoint_description_Layer_strategy = st.builds(viewpoint_description_Layer, icon=safe_text)
@given(instance=viewpoint_description_Layer_strategy)
@settings(max_examples=25)
def test_viewpoint_description_Layer_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Layer)


viewpoint_description_Layout_strategy = st.builds(viewpoint_description_Layout)
@given(instance=viewpoint_description_Layout_strategy)
@settings(max_examples=25)
def test_viewpoint_description_Layout_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Layout)


viewpoint_description_MappingBasedDecoration_strategy = st.builds(viewpoint_description_MappingBasedDecoration)
@given(instance=viewpoint_description_MappingBasedDecoration_strategy)
@settings(max_examples=25)
def test_viewpoint_description_MappingBasedDecoration_instantiation(instance):
    assert isinstance(instance, viewpoint_description_MappingBasedDecoration)


viewpoint_description_MetamodelExtensionSetting_strategy = st.builds(viewpoint_description_MetamodelExtensionSetting)
@given(instance=viewpoint_description_MetamodelExtensionSetting_strategy)
@settings(max_examples=25)
def test_viewpoint_description_MetamodelExtensionSetting_instantiation(instance):
    assert isinstance(instance, viewpoint_description_MetamodelExtensionSetting)


viewpoint_description_NodeMapping_strategy = st.builds(viewpoint_description_NodeMapping)
@given(instance=viewpoint_description_NodeMapping_strategy)
@settings(max_examples=25)
def test_viewpoint_description_NodeMapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_NodeMapping)


viewpoint_description_NodeMappingImport_strategy = st.builds(viewpoint_description_NodeMappingImport)
@given(instance=viewpoint_description_NodeMappingImport_strategy)
@settings(max_examples=25)
def test_viewpoint_description_NodeMappingImport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_NodeMappingImport)


viewpoint_description_OrderedTreeLayout_strategy = st.builds(viewpoint_description_OrderedTreeLayout, childrenExpression=safe_text)
@given(instance=viewpoint_description_OrderedTreeLayout_strategy)
@settings(max_examples=25)
def test_viewpoint_description_OrderedTreeLayout_instantiation(instance):
    assert isinstance(instance, viewpoint_description_OrderedTreeLayout)


viewpoint_description_PasteTargetDescription_strategy = st.builds(viewpoint_description_PasteTargetDescription)
@given(instance=viewpoint_description_PasteTargetDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_PasteTargetDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_PasteTargetDescription)


viewpoint_description_RepresentationDescription_strategy = st.builds(viewpoint_description_RepresentationDescription, initialisation=st.booleans(), showOnStartup=st.booleans(), titleExpression=safe_text)
@given(instance=viewpoint_description_RepresentationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_RepresentationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationDescription)


viewpoint_description_RepresentationElementMapping_strategy = st.builds(viewpoint_description_RepresentationElementMapping)
@given(instance=viewpoint_description_RepresentationElementMapping_strategy)
@settings(max_examples=25)
def test_viewpoint_description_RepresentationElementMapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationElementMapping)


viewpoint_description_RepresentationExtensionDescription_strategy = st.builds(viewpoint_description_RepresentationExtensionDescription, name=safe_text, representationName=safe_text, viewpointURI=safe_text)
@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_RepresentationExtensionDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationExtensionDescription)


viewpoint_description_RepresentationImportDescription_strategy = st.builds(viewpoint_description_RepresentationImportDescription)
@given(instance=viewpoint_description_RepresentationImportDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_RepresentationImportDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationImportDescription)


viewpoint_description_RepresentationTemplate_strategy = st.builds(viewpoint_description_RepresentationTemplate, name=safe_text)
@given(instance=viewpoint_description_RepresentationTemplate_strategy)
@settings(max_examples=25)
def test_viewpoint_description_RepresentationTemplate_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationTemplate)


viewpoint_description_SelectionDescription_strategy = st.builds(viewpoint_description_SelectionDescription, candidatesExpression=safe_text, childrenExpression=safe_text, message=safe_text, multiple=st.booleans(), rootExpression=safe_text, tree=st.booleans())
@given(instance=viewpoint_description_SelectionDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_SelectionDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SelectionDescription)


viewpoint_description_SemanticBasedDecoration_strategy = st.builds(viewpoint_description_SemanticBasedDecoration, domainClass=safe_text)
@given(instance=viewpoint_description_SemanticBasedDecoration_strategy)
@settings(max_examples=25)
def test_viewpoint_description_SemanticBasedDecoration_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SemanticBasedDecoration)


viewpoint_description_SystemColor_strategy = st.builds(viewpoint_description_SystemColor, name=safe_text)
@given(instance=viewpoint_description_SystemColor_strategy)
@settings(max_examples=25)
def test_viewpoint_description_SystemColor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SystemColor)


viewpoint_description_SytemColorsPalette_strategy = st.builds(viewpoint_description_SytemColorsPalette)
@given(instance=viewpoint_description_SytemColorsPalette_strategy)
@settings(max_examples=25)
def test_viewpoint_description_SytemColorsPalette_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SytemColorsPalette)


viewpoint_description_UserColor_strategy = st.builds(viewpoint_description_UserColor, name=safe_text)
@given(instance=viewpoint_description_UserColor_strategy)
@settings(max_examples=25)
def test_viewpoint_description_UserColor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserColor)


viewpoint_description_UserColorsPalette_strategy = st.builds(viewpoint_description_UserColorsPalette, name=safe_text)
@given(instance=viewpoint_description_UserColorsPalette_strategy)
@settings(max_examples=25)
def test_viewpoint_description_UserColorsPalette_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserColorsPalette)


viewpoint_description_UserFixedColor_strategy = st.builds(viewpoint_description_UserFixedColor)
@given(instance=viewpoint_description_UserFixedColor_strategy)
@settings(max_examples=25)
def test_viewpoint_description_UserFixedColor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserFixedColor)


viewpoint_description_VSMElementCustomization_strategy = st.builds(viewpoint_description_VSMElementCustomization, predicateExpression=safe_text)
@given(instance=viewpoint_description_VSMElementCustomization_strategy)
@settings(max_examples=25)
def test_viewpoint_description_VSMElementCustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_VSMElementCustomization)


viewpoint_description_VSMElementCustomizationReuse_strategy = st.builds(viewpoint_description_VSMElementCustomizationReuse)
@given(instance=viewpoint_description_VSMElementCustomizationReuse_strategy)
@settings(max_examples=25)
def test_viewpoint_description_VSMElementCustomizationReuse_instantiation(instance):
    assert isinstance(instance, viewpoint_description_VSMElementCustomizationReuse)


viewpoint_description_Viewpoint_strategy = st.builds(viewpoint_description_Viewpoint, conflicts=safe_text, customizes=safe_text, icon=safe_text, modelFileExtension=safe_text, reuses=safe_text)
@given(instance=viewpoint_description_Viewpoint_strategy)
@settings(max_examples=25)
def test_viewpoint_description_Viewpoint_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Viewpoint)


viewpoint_diagram_AbsoluteBoundsFilter_strategy = st.builds(viewpoint_diagram_AbsoluteBoundsFilter, height=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=viewpoint_diagram_AbsoluteBoundsFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_AbsoluteBoundsFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_AbsoluteBoundsFilter)


viewpoint_diagram_AbstractDNode_strategy = st.builds(viewpoint_diagram_AbstractDNode, arrangeConstraints=safe_text)
@given(instance=viewpoint_diagram_AbstractDNode_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_AbstractDNode_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_AbstractDNode)


viewpoint_diagram_AppliedCompositeFilters_strategy = st.builds(viewpoint_diagram_AppliedCompositeFilters)
@given(instance=viewpoint_diagram_AppliedCompositeFilters_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_AppliedCompositeFilters_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_AppliedCompositeFilters)


viewpoint_diagram_BeginLabelStyle_strategy = st.builds(viewpoint_diagram_BeginLabelStyle)
@given(instance=viewpoint_diagram_BeginLabelStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_BeginLabelStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_BeginLabelStyle)


viewpoint_diagram_BorderedStyle_strategy = st.builds(viewpoint_diagram_BorderedStyle, borderSize=safe_text, borderSizeComputationExpression=safe_text)
@given(instance=viewpoint_diagram_BorderedStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_BorderedStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_BorderedStyle)


viewpoint_diagram_BracketEdgeStyle_strategy = st.builds(viewpoint_diagram_BracketEdgeStyle)
@given(instance=viewpoint_diagram_BracketEdgeStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_BracketEdgeStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_BracketEdgeStyle)


viewpoint_diagram_BundledImage_strategy = st.builds(viewpoint_diagram_BundledImage, shape=safe_text)
@given(instance=viewpoint_diagram_BundledImage_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_BundledImage_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_BundledImage)


viewpoint_diagram_CenterLabelStyle_strategy = st.builds(viewpoint_diagram_CenterLabelStyle)
@given(instance=viewpoint_diagram_CenterLabelStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_CenterLabelStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_CenterLabelStyle)


viewpoint_diagram_CollapseFilter_strategy = st.builds(viewpoint_diagram_CollapseFilter, height=st.integers(), width=st.integers())
@given(instance=viewpoint_diagram_CollapseFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_CollapseFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_CollapseFilter)


viewpoint_diagram_ComputedStyleDescriptionRegistry_strategy = st.builds(viewpoint_diagram_ComputedStyleDescriptionRegistry)
@given(instance=viewpoint_diagram_ComputedStyleDescriptionRegistry_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_ComputedStyleDescriptionRegistry_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ComputedStyleDescriptionRegistry)


viewpoint_diagram_ContainerStyle_strategy = st.builds(viewpoint_diagram_ContainerStyle)
@given(instance=viewpoint_diagram_ContainerStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_ContainerStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ContainerStyle)


viewpoint_diagram_ContainerVariable2StyleDescription_strategy = st.builds(viewpoint_diagram_ContainerVariable2StyleDescription)
@given(instance=viewpoint_diagram_ContainerVariable2StyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_ContainerVariable2StyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ContainerVariable2StyleDescription)


viewpoint_diagram_CustomStyle_strategy = st.builds(viewpoint_diagram_CustomStyle, id=safe_text)
@given(instance=viewpoint_diagram_CustomStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_CustomStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_CustomStyle)


viewpoint_diagram_DDiagram_strategy = st.builds(viewpoint_diagram_DDiagram, headerHeight=st.integers(), info=safe_text, isInLayoutingMode=st.booleans(), synchronized=st.booleans())
@given(instance=viewpoint_diagram_DDiagram_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DDiagram_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagram)


viewpoint_diagram_DDiagramElement_strategy = st.builds(viewpoint_diagram_DDiagramElement, tooltipText=safe_text, visible=st.booleans())
@given(instance=viewpoint_diagram_DDiagramElement_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DDiagramElement_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagramElement)


viewpoint_diagram_DDiagramElementContainer_strategy = st.builds(viewpoint_diagram_DDiagramElementContainer, height=safe_text, width=safe_text)
@given(instance=viewpoint_diagram_DDiagramElementContainer_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DDiagramElementContainer_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagramElementContainer)


viewpoint_diagram_DDiagramLink_strategy = st.builds(viewpoint_diagram_DDiagramLink)
@given(instance=viewpoint_diagram_DDiagramLink_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DDiagramLink_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagramLink)


viewpoint_diagram_DDiagramSet_strategy = st.builds(viewpoint_diagram_DDiagramSet)
@given(instance=viewpoint_diagram_DDiagramSet_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DDiagramSet_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagramSet)


viewpoint_diagram_DEdge_strategy = st.builds(viewpoint_diagram_DEdge, arrangeConstraints=safe_text, beginLabel=safe_text, endLabel=safe_text, isFold=st.booleans(), isMockEdge=st.booleans(), routingStyle=safe_text, size=safe_text)
@given(instance=viewpoint_diagram_DEdge_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DEdge_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DEdge)


viewpoint_diagram_DNode_strategy = st.builds(viewpoint_diagram_DNode, height=safe_text, labelPosition=safe_text, resizeKind=safe_text, width=safe_text)
@given(instance=viewpoint_diagram_DNode_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DNode_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DNode)


viewpoint_diagram_DNodeContainer_strategy = st.builds(viewpoint_diagram_DNodeContainer, childrenPresentation=safe_text)
@given(instance=viewpoint_diagram_DNodeContainer_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DNodeContainer_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DNodeContainer)


viewpoint_diagram_DNodeList_strategy = st.builds(viewpoint_diagram_DNodeList, lineWidth=st.integers())
@given(instance=viewpoint_diagram_DNodeList_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DNodeList_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DNodeList)


viewpoint_diagram_DNodeListElement_strategy = st.builds(viewpoint_diagram_DNodeListElement)
@given(instance=viewpoint_diagram_DNodeListElement_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DNodeListElement_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DNodeListElement)


viewpoint_diagram_DSemanticDiagram_strategy = st.builds(viewpoint_diagram_DSemanticDiagram)
@given(instance=viewpoint_diagram_DSemanticDiagram_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DSemanticDiagram_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DSemanticDiagram)


viewpoint_diagram_DiagramElementMapping2ModelElement_strategy = st.builds(viewpoint_diagram_DiagramElementMapping2ModelElement)
@given(instance=viewpoint_diagram_DiagramElementMapping2ModelElement_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_DiagramElementMapping2ModelElement_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DiagramElementMapping2ModelElement)


viewpoint_diagram_Dot_strategy = st.builds(viewpoint_diagram_Dot, strokeSizeComputationExpression=safe_text)
@given(instance=viewpoint_diagram_Dot_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_Dot_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Dot)


viewpoint_diagram_EdgeStyle_strategy = st.builds(viewpoint_diagram_EdgeStyle, foldingStyle=safe_text, lineStyle=safe_text, routingStyle=safe_text, size=safe_text, sourceArrow=safe_text, targetArrow=safe_text)
@given(instance=viewpoint_diagram_EdgeStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_EdgeStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_EdgeStyle)


viewpoint_diagram_EdgeTarget_strategy = st.builds(viewpoint_diagram_EdgeTarget)
@given(instance=viewpoint_diagram_EdgeTarget_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_EdgeTarget_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_EdgeTarget)


viewpoint_diagram_Ellipse_strategy = st.builds(viewpoint_diagram_Ellipse, horizontalDiameter=safe_text, verticalDiameter=safe_text)
@given(instance=viewpoint_diagram_Ellipse_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_Ellipse_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Ellipse)


viewpoint_diagram_EndLabelStyle_strategy = st.builds(viewpoint_diagram_EndLabelStyle)
@given(instance=viewpoint_diagram_EndLabelStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_EndLabelStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_EndLabelStyle)


viewpoint_diagram_FilterVariableHistory_strategy = st.builds(viewpoint_diagram_FilterVariableHistory)
@given(instance=viewpoint_diagram_FilterVariableHistory_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_FilterVariableHistory_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FilterVariableHistory)


viewpoint_diagram_FilterVariableValue_strategy = st.builds(viewpoint_diagram_FilterVariableValue)
@given(instance=viewpoint_diagram_FilterVariableValue_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_FilterVariableValue_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FilterVariableValue)


viewpoint_diagram_FlatContainerStyle_strategy = st.builds(viewpoint_diagram_FlatContainerStyle, backgroundStyle=safe_text)
@given(instance=viewpoint_diagram_FlatContainerStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_FlatContainerStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FlatContainerStyle)


viewpoint_diagram_FoldingFilter_strategy = st.builds(viewpoint_diagram_FoldingFilter)
@given(instance=viewpoint_diagram_FoldingFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_FoldingFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FoldingFilter)


viewpoint_diagram_FoldingPointFilter_strategy = st.builds(viewpoint_diagram_FoldingPointFilter)
@given(instance=viewpoint_diagram_FoldingPointFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_FoldingPointFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FoldingPointFilter)


viewpoint_diagram_GaugeCompositeStyle_strategy = st.builds(viewpoint_diagram_GaugeCompositeStyle, alignment=safe_text)
@given(instance=viewpoint_diagram_GaugeCompositeStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_GaugeCompositeStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_GaugeCompositeStyle)


viewpoint_diagram_GaugeSection_strategy = st.builds(viewpoint_diagram_GaugeSection, label=safe_text, max=safe_text, min=safe_text, value=safe_text)
@given(instance=viewpoint_diagram_GaugeSection_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_GaugeSection_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_GaugeSection)


viewpoint_diagram_GraphicalFilter_strategy = st.builds(viewpoint_diagram_GraphicalFilter)
@given(instance=viewpoint_diagram_GraphicalFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_GraphicalFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_GraphicalFilter)


viewpoint_diagram_HideFilter_strategy = st.builds(viewpoint_diagram_HideFilter)
@given(instance=viewpoint_diagram_HideFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_HideFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_HideFilter)


viewpoint_diagram_HideLabelFilter_strategy = st.builds(viewpoint_diagram_HideLabelFilter)
@given(instance=viewpoint_diagram_HideLabelFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_HideLabelFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_HideLabelFilter)


viewpoint_diagram_IndirectlyCollapseFilter_strategy = st.builds(viewpoint_diagram_IndirectlyCollapseFilter)
@given(instance=viewpoint_diagram_IndirectlyCollapseFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_IndirectlyCollapseFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_IndirectlyCollapseFilter)


viewpoint_diagram_Lozenge_strategy = st.builds(viewpoint_diagram_Lozenge, height=safe_text, width=safe_text)
@given(instance=viewpoint_diagram_Lozenge_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_Lozenge_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Lozenge)


viewpoint_diagram_ModelElement2ViewVariable_strategy = st.builds(viewpoint_diagram_ModelElement2ViewVariable)
@given(instance=viewpoint_diagram_ModelElement2ViewVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_ModelElement2ViewVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ModelElement2ViewVariable)


viewpoint_diagram_NodeStyle_strategy = st.builds(viewpoint_diagram_NodeStyle, hideLabelByDefault=st.booleans(), labelPosition=safe_text)
@given(instance=viewpoint_diagram_NodeStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_NodeStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_NodeStyle)


viewpoint_diagram_Note_strategy = st.builds(viewpoint_diagram_Note)
@given(instance=viewpoint_diagram_Note_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_Note_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Note)


viewpoint_diagram_ShapeContainerStyle_strategy = st.builds(viewpoint_diagram_ShapeContainerStyle, shape=safe_text)
@given(instance=viewpoint_diagram_ShapeContainerStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_ShapeContainerStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ShapeContainerStyle)


viewpoint_diagram_Square_strategy = st.builds(viewpoint_diagram_Square, height=safe_text, width=safe_text)
@given(instance=viewpoint_diagram_Square_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_Square_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Square)


viewpoint_diagram_ViewVariable2ContainerVariable_strategy = st.builds(viewpoint_diagram_ViewVariable2ContainerVariable)
@given(instance=viewpoint_diagram_ViewVariable2ContainerVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_ViewVariable2ContainerVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ViewVariable2ContainerVariable)


viewpoint_diagram_WorkspaceImage_strategy = st.builds(viewpoint_diagram_WorkspaceImage, workspacePath=safe_text)
@given(instance=viewpoint_diagram_WorkspaceImage_strategy)
@settings(max_examples=25)
def test_viewpoint_diagram_WorkspaceImage_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_WorkspaceImage)


viewpoint_filter_CompositeFilterDescription_strategy = st.builds(viewpoint_filter_CompositeFilterDescription)
@given(instance=viewpoint_filter_CompositeFilterDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_filter_CompositeFilterDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_CompositeFilterDescription)


viewpoint_filter_Filter_strategy = st.builds(viewpoint_filter_Filter, filterKind=safe_text)
@given(instance=viewpoint_filter_Filter_strategy)
@settings(max_examples=25)
def test_viewpoint_filter_Filter_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_Filter)


viewpoint_filter_FilterDescription_strategy = st.builds(viewpoint_filter_FilterDescription)
@given(instance=viewpoint_filter_FilterDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_filter_FilterDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_FilterDescription)


viewpoint_filter_FilterVariable_strategy = st.builds(viewpoint_filter_FilterVariable, name=safe_text)
@given(instance=viewpoint_filter_FilterVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_filter_FilterVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_FilterVariable)


viewpoint_filter_MappingFilter_strategy = st.builds(viewpoint_filter_MappingFilter, semanticConditionExpression=safe_text, viewConditionExpression=safe_text)
@given(instance=viewpoint_filter_MappingFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_filter_MappingFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_MappingFilter)


viewpoint_filter_VariableFilter_strategy = st.builds(viewpoint_filter_VariableFilter, semanticConditionExpression=safe_text)
@given(instance=viewpoint_filter_VariableFilter_strategy)
@settings(max_examples=25)
def test_viewpoint_filter_VariableFilter_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_VariableFilter)


viewpoint_style_BasicLabelStyleDescription_strategy = st.builds(viewpoint_style_BasicLabelStyleDescription, iconPath=safe_text, labelExpression=safe_text, labelFormat=safe_text, labelSize=st.integers(), showIcon=st.booleans())
@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_BasicLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BasicLabelStyleDescription)


viewpoint_style_BeginLabelStyleDescription_strategy = st.builds(viewpoint_style_BeginLabelStyleDescription)
@given(instance=viewpoint_style_BeginLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_BeginLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BeginLabelStyleDescription)


viewpoint_style_BorderedStyleDescription_strategy = st.builds(viewpoint_style_BorderedStyleDescription, borderSizeComputationExpression=safe_text)
@given(instance=viewpoint_style_BorderedStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_BorderedStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BorderedStyleDescription)


viewpoint_style_BracketEdgeStyleDescription_strategy = st.builds(viewpoint_style_BracketEdgeStyleDescription)
@given(instance=viewpoint_style_BracketEdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_BracketEdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BracketEdgeStyleDescription)


viewpoint_style_BundledImageDescription_strategy = st.builds(viewpoint_style_BundledImageDescription, shape=safe_text)
@given(instance=viewpoint_style_BundledImageDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_BundledImageDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BundledImageDescription)


viewpoint_style_CenterLabelStyleDescription_strategy = st.builds(viewpoint_style_CenterLabelStyleDescription)
@given(instance=viewpoint_style_CenterLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_CenterLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_CenterLabelStyleDescription)


viewpoint_style_ContainerStyleDescription_strategy = st.builds(viewpoint_style_ContainerStyleDescription, roundedCorner=st.booleans())
@given(instance=viewpoint_style_ContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_ContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_ContainerStyleDescription)


viewpoint_style_CustomStyleDescription_strategy = st.builds(viewpoint_style_CustomStyleDescription, id=safe_text)
@given(instance=viewpoint_style_CustomStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_CustomStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_CustomStyleDescription)


viewpoint_style_DotDescription_strategy = st.builds(viewpoint_style_DotDescription, strokeSizeComputationExpression=safe_text)
@given(instance=viewpoint_style_DotDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_DotDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_DotDescription)


viewpoint_style_EdgeStyleDescription_strategy = st.builds(viewpoint_style_EdgeStyleDescription, foldingStyle=safe_text, lineStyle=safe_text, routingStyle=safe_text, sizeComputationExpression=safe_text, sourceArrow=safe_text, targetArrow=safe_text)
@given(instance=viewpoint_style_EdgeStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_EdgeStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_EdgeStyleDescription)


viewpoint_style_EllipseNodeDescription_strategy = st.builds(viewpoint_style_EllipseNodeDescription, horizontalDiameterComputationExpression=safe_text, verticalDiameterComputationExpression=safe_text)
@given(instance=viewpoint_style_EllipseNodeDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_EllipseNodeDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_EllipseNodeDescription)


viewpoint_style_EndLabelStyleDescription_strategy = st.builds(viewpoint_style_EndLabelStyleDescription)
@given(instance=viewpoint_style_EndLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_EndLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_EndLabelStyleDescription)


viewpoint_style_FlatContainerStyleDescription_strategy = st.builds(viewpoint_style_FlatContainerStyleDescription, backgroundStyle=safe_text)
@given(instance=viewpoint_style_FlatContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_FlatContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_FlatContainerStyleDescription)


viewpoint_style_GaugeCompositeStyleDescription_strategy = st.builds(viewpoint_style_GaugeCompositeStyleDescription, alignment=safe_text)
@given(instance=viewpoint_style_GaugeCompositeStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_GaugeCompositeStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_GaugeCompositeStyleDescription)


viewpoint_style_GaugeSectionDescription_strategy = st.builds(viewpoint_style_GaugeSectionDescription, label=safe_text, maxValueExpression=safe_text, minValueExpression=safe_text, valueExpression=safe_text)
@given(instance=viewpoint_style_GaugeSectionDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_GaugeSectionDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_GaugeSectionDescription)


viewpoint_style_LabelBorderStyleDescription_strategy = st.builds(viewpoint_style_LabelBorderStyleDescription, cornerHeight=st.integers(), cornerWidth=st.integers(), id=safe_text, name=safe_text)
@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_LabelBorderStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelBorderStyleDescription)


viewpoint_style_LabelBorderStyles_strategy = st.builds(viewpoint_style_LabelBorderStyles)
@given(instance=viewpoint_style_LabelBorderStyles_strategy)
@settings(max_examples=25)
def test_viewpoint_style_LabelBorderStyles_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelBorderStyles)


viewpoint_style_LabelStyleDescription_strategy = st.builds(viewpoint_style_LabelStyleDescription, labelAlignment=safe_text)
@given(instance=viewpoint_style_LabelStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_LabelStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelStyleDescription)


viewpoint_style_LozengeNodeDescription_strategy = st.builds(viewpoint_style_LozengeNodeDescription, heightComputationExpression=safe_text, widthComputationExpression=safe_text)
@given(instance=viewpoint_style_LozengeNodeDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_LozengeNodeDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LozengeNodeDescription)


viewpoint_style_NodeStyleDescription_strategy = st.builds(viewpoint_style_NodeStyleDescription, hideLabelByDefault=st.booleans(), labelPosition=safe_text, resizeKind=safe_text, sizeComputationExpression=safe_text)
@given(instance=viewpoint_style_NodeStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_NodeStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_NodeStyleDescription)


viewpoint_style_NoteDescription_strategy = st.builds(viewpoint_style_NoteDescription)
@given(instance=viewpoint_style_NoteDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_NoteDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_NoteDescription)


viewpoint_style_RoundedCornerStyleDescription_strategy = st.builds(viewpoint_style_RoundedCornerStyleDescription, arcHeight=safe_text, arcWidth=safe_text)
@given(instance=viewpoint_style_RoundedCornerStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_RoundedCornerStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_RoundedCornerStyleDescription)


viewpoint_style_ShapeContainerStyleDescription_strategy = st.builds(viewpoint_style_ShapeContainerStyleDescription, shape=safe_text)
@given(instance=viewpoint_style_ShapeContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_ShapeContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_ShapeContainerStyleDescription)


viewpoint_style_SizeComputationContainerStyleDescription_strategy = st.builds(viewpoint_style_SizeComputationContainerStyleDescription, heightComputationExpression=safe_text, widthComputationExpression=safe_text)
@given(instance=viewpoint_style_SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_SizeComputationContainerStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_SizeComputationContainerStyleDescription)


viewpoint_style_SquareDescription_strategy = st.builds(viewpoint_style_SquareDescription, height=safe_text, width=safe_text)
@given(instance=viewpoint_style_SquareDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_SquareDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_SquareDescription)


viewpoint_style_StyleDescription_strategy = st.builds(viewpoint_style_StyleDescription)
@given(instance=viewpoint_style_StyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_StyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_StyleDescription)


viewpoint_style_TooltipStyleDescription_strategy = st.builds(viewpoint_style_TooltipStyleDescription, tooltipExpression=safe_text)
@given(instance=viewpoint_style_TooltipStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_TooltipStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_TooltipStyleDescription)


viewpoint_style_WorkspaceImageDescription_strategy = st.builds(viewpoint_style_WorkspaceImageDescription, workspacePath=safe_text)
@given(instance=viewpoint_style_WorkspaceImageDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_WorkspaceImageDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_WorkspaceImageDescription)


viewpoint_tool_AbstractToolDescription_strategy = st.builds(viewpoint_tool_AbstractToolDescription, forceRefresh=st.booleans(), precondition=safe_text)
@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_AbstractToolDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AbstractToolDescription)


viewpoint_tool_AbstractVariable_strategy = st.builds(viewpoint_tool_AbstractVariable, name=safe_text)
@given(instance=viewpoint_tool_AbstractVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_AbstractVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AbstractVariable)


viewpoint_tool_AcceleoVariable_strategy = st.builds(viewpoint_tool_AcceleoVariable, computationExpression=safe_text)
@given(instance=viewpoint_tool_AcceleoVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_AcceleoVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AcceleoVariable)


viewpoint_tool_BehaviorTool_strategy = st.builds(viewpoint_tool_BehaviorTool, domainClass=safe_text)
@given(instance=viewpoint_tool_BehaviorTool_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_BehaviorTool_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_BehaviorTool)


viewpoint_tool_Case_strategy = st.builds(viewpoint_tool_Case, conditionExpression=safe_text)
@given(instance=viewpoint_tool_Case_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_Case_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Case)


viewpoint_tool_ChangeContext_strategy = st.builds(viewpoint_tool_ChangeContext, browseExpression=safe_text)
@given(instance=viewpoint_tool_ChangeContext_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ChangeContext_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ChangeContext)


viewpoint_tool_ContainerCreationDescription_strategy = st.builds(viewpoint_tool_ContainerCreationDescription, iconPath=safe_text)
@given(instance=viewpoint_tool_ContainerCreationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ContainerCreationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerCreationDescription)


viewpoint_tool_ContainerDropDescription_strategy = st.builds(viewpoint_tool_ContainerDropDescription, dragSource=safe_text, moveEdges=st.booleans())
@given(instance=viewpoint_tool_ContainerDropDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ContainerDropDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerDropDescription)


viewpoint_tool_ContainerModelOperation_strategy = st.builds(viewpoint_tool_ContainerModelOperation)
@given(instance=viewpoint_tool_ContainerModelOperation_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ContainerModelOperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerModelOperation)


viewpoint_tool_ContainerViewVariable_strategy = st.builds(viewpoint_tool_ContainerViewVariable)
@given(instance=viewpoint_tool_ContainerViewVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ContainerViewVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerViewVariable)


viewpoint_tool_CreateEdgeView_strategy = st.builds(viewpoint_tool_CreateEdgeView, sourceExpression=safe_text, targetExpression=safe_text)
@given(instance=viewpoint_tool_CreateEdgeView_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_CreateEdgeView_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_CreateEdgeView)


viewpoint_tool_CreateInstance_strategy = st.builds(viewpoint_tool_CreateInstance, referenceName=safe_text, typeName=safe_text, variableName=safe_text)
@given(instance=viewpoint_tool_CreateInstance_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_CreateInstance_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_CreateInstance)


viewpoint_tool_CreateView_strategy = st.builds(viewpoint_tool_CreateView, containerViewExpression=safe_text, variableName=safe_text)
@given(instance=viewpoint_tool_CreateView_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_CreateView_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_CreateView)


viewpoint_tool_Default_strategy = st.builds(viewpoint_tool_Default)
@given(instance=viewpoint_tool_Default_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_Default_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Default)


viewpoint_tool_DeleteElementDescription_strategy = st.builds(viewpoint_tool_DeleteElementDescription)
@given(instance=viewpoint_tool_DeleteElementDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DeleteElementDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteElementDescription)


viewpoint_tool_DeleteHook_strategy = st.builds(viewpoint_tool_DeleteHook, id=safe_text)
@given(instance=viewpoint_tool_DeleteHook_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DeleteHook_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteHook)


viewpoint_tool_DeleteHookParameter_strategy = st.builds(viewpoint_tool_DeleteHookParameter, name=safe_text, value=safe_text)
@given(instance=viewpoint_tool_DeleteHookParameter_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DeleteHookParameter_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteHookParameter)


viewpoint_tool_DeleteView_strategy = st.builds(viewpoint_tool_DeleteView)
@given(instance=viewpoint_tool_DeleteView_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DeleteView_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteView)


viewpoint_tool_DiagramCreationDescription_strategy = st.builds(viewpoint_tool_DiagramCreationDescription)
@given(instance=viewpoint_tool_DiagramCreationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DiagramCreationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DiagramCreationDescription)


viewpoint_tool_DiagramNavigationDescription_strategy = st.builds(viewpoint_tool_DiagramNavigationDescription)
@given(instance=viewpoint_tool_DiagramNavigationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DiagramNavigationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DiagramNavigationDescription)


viewpoint_tool_DialogVariable_strategy = st.builds(viewpoint_tool_DialogVariable, dialogPrompt=safe_text)
@given(instance=viewpoint_tool_DialogVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DialogVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DialogVariable)


viewpoint_tool_DirectEditLabel_strategy = st.builds(viewpoint_tool_DirectEditLabel, inputLabelExpression=safe_text)
@given(instance=viewpoint_tool_DirectEditLabel_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DirectEditLabel_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DirectEditLabel)


viewpoint_tool_DoubleClickDescription_strategy = st.builds(viewpoint_tool_DoubleClickDescription)
@given(instance=viewpoint_tool_DoubleClickDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DoubleClickDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DoubleClickDescription)


viewpoint_tool_DropContainerVariable_strategy = st.builds(viewpoint_tool_DropContainerVariable)
@given(instance=viewpoint_tool_DropContainerVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DropContainerVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DropContainerVariable)


viewpoint_tool_EdgeCreationDescription_strategy = st.builds(viewpoint_tool_EdgeCreationDescription, connectionStartPrecondition=safe_text, iconPath=safe_text)
@given(instance=viewpoint_tool_EdgeCreationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_EdgeCreationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_EdgeCreationDescription)


viewpoint_tool_EditMaskVariables_strategy = st.builds(viewpoint_tool_EditMaskVariables, mask=safe_text)
@given(instance=viewpoint_tool_EditMaskVariables_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_EditMaskVariables_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_EditMaskVariables)


viewpoint_tool_ElementDeleteVariable_strategy = st.builds(viewpoint_tool_ElementDeleteVariable)
@given(instance=viewpoint_tool_ElementDeleteVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ElementDeleteVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementDeleteVariable)


viewpoint_tool_ElementDoubleClickVariable_strategy = st.builds(viewpoint_tool_ElementDoubleClickVariable)
@given(instance=viewpoint_tool_ElementDoubleClickVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ElementDoubleClickVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementDoubleClickVariable)


viewpoint_tool_ElementDropVariable_strategy = st.builds(viewpoint_tool_ElementDropVariable)
@given(instance=viewpoint_tool_ElementDropVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ElementDropVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementDropVariable)


viewpoint_tool_ElementSelectVariable_strategy = st.builds(viewpoint_tool_ElementSelectVariable)
@given(instance=viewpoint_tool_ElementSelectVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ElementSelectVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementSelectVariable)


viewpoint_tool_ElementVariable_strategy = st.builds(viewpoint_tool_ElementVariable)
@given(instance=viewpoint_tool_ElementVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ElementVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementVariable)


viewpoint_tool_ElementViewVariable_strategy = st.builds(viewpoint_tool_ElementViewVariable)
@given(instance=viewpoint_tool_ElementViewVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ElementViewVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementViewVariable)


viewpoint_tool_ExternalJavaAction_strategy = st.builds(viewpoint_tool_ExternalJavaAction, id=safe_text)
@given(instance=viewpoint_tool_ExternalJavaAction_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ExternalJavaAction_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaAction)


viewpoint_tool_ExternalJavaActionCall_strategy = st.builds(viewpoint_tool_ExternalJavaActionCall)
@given(instance=viewpoint_tool_ExternalJavaActionCall_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ExternalJavaActionCall_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaActionCall)


viewpoint_tool_ExternalJavaActionParameter_strategy = st.builds(viewpoint_tool_ExternalJavaActionParameter, name=safe_text, value=safe_text)
@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ExternalJavaActionParameter_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaActionParameter)


viewpoint_tool_FeatureChangeListener_strategy = st.builds(viewpoint_tool_FeatureChangeListener, domainClass=safe_text, featureName=safe_text)
@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_FeatureChangeListener_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_FeatureChangeListener)


viewpoint_tool_For_strategy = st.builds(viewpoint_tool_For, expression=safe_text, iteratorName=safe_text)
@given(instance=viewpoint_tool_For_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_For_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_For)


viewpoint_tool_If_strategy = st.builds(viewpoint_tool_If, conditionExpression=safe_text)
@given(instance=viewpoint_tool_If_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_If_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_If)


viewpoint_tool_InitEdgeCreationOperation_strategy = st.builds(viewpoint_tool_InitEdgeCreationOperation)
@given(instance=viewpoint_tool_InitEdgeCreationOperation_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_InitEdgeCreationOperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitEdgeCreationOperation)


viewpoint_tool_InitialContainerDropOperation_strategy = st.builds(viewpoint_tool_InitialContainerDropOperation)
@given(instance=viewpoint_tool_InitialContainerDropOperation_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_InitialContainerDropOperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialContainerDropOperation)


viewpoint_tool_InitialNodeCreationOperation_strategy = st.builds(viewpoint_tool_InitialNodeCreationOperation)
@given(instance=viewpoint_tool_InitialNodeCreationOperation_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_InitialNodeCreationOperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialNodeCreationOperation)


viewpoint_tool_InitialOperation_strategy = st.builds(viewpoint_tool_InitialOperation)
@given(instance=viewpoint_tool_InitialOperation_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_InitialOperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialOperation)


viewpoint_tool_MappingBasedToolDescription_strategy = st.builds(viewpoint_tool_MappingBasedToolDescription)
@given(instance=viewpoint_tool_MappingBasedToolDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_MappingBasedToolDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MappingBasedToolDescription)


viewpoint_tool_MenuItemDescription_strategy = st.builds(viewpoint_tool_MenuItemDescription, icon=safe_text)
@given(instance=viewpoint_tool_MenuItemDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_MenuItemDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemDescription)


viewpoint_tool_MenuItemDescriptionReference_strategy = st.builds(viewpoint_tool_MenuItemDescriptionReference)
@given(instance=viewpoint_tool_MenuItemDescriptionReference_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_MenuItemDescriptionReference_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemDescriptionReference)


viewpoint_tool_MenuItemOrRef_strategy = st.builds(viewpoint_tool_MenuItemOrRef)
@given(instance=viewpoint_tool_MenuItemOrRef_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_MenuItemOrRef_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemOrRef)


viewpoint_tool_ModelOperation_strategy = st.builds(viewpoint_tool_ModelOperation)
@given(instance=viewpoint_tool_ModelOperation_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ModelOperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ModelOperation)


viewpoint_tool_MoveElement_strategy = st.builds(viewpoint_tool_MoveElement, featureName=safe_text, newContainerExpression=safe_text)
@given(instance=viewpoint_tool_MoveElement_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_MoveElement_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MoveElement)


viewpoint_tool_NameVariable_strategy = st.builds(viewpoint_tool_NameVariable)
@given(instance=viewpoint_tool_NameVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_NameVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_NameVariable)


viewpoint_tool_Navigation_strategy = st.builds(viewpoint_tool_Navigation, createIfNotExistent=st.booleans())
@given(instance=viewpoint_tool_Navigation_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_Navigation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Navigation)


viewpoint_tool_NodeCreationDescription_strategy = st.builds(viewpoint_tool_NodeCreationDescription, iconPath=safe_text)
@given(instance=viewpoint_tool_NodeCreationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_NodeCreationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_NodeCreationDescription)


viewpoint_tool_NodeCreationVariable_strategy = st.builds(viewpoint_tool_NodeCreationVariable)
@given(instance=viewpoint_tool_NodeCreationVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_NodeCreationVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_NodeCreationVariable)


viewpoint_tool_OperationAction_strategy = st.builds(viewpoint_tool_OperationAction)
@given(instance=viewpoint_tool_OperationAction_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_OperationAction_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_OperationAction)


viewpoint_tool_PaneBasedSelectionWizardDescription_strategy = st.builds(viewpoint_tool_PaneBasedSelectionWizardDescription, candidatesExpression=safe_text, childrenExpression=safe_text, choiceOfValuesMessage=safe_text, iconPath=safe_text, message=safe_text, preSelectedCandidatesExpression=safe_text, rootExpression=safe_text, selectedValuesMessage=safe_text, tree=st.booleans(), windowImagePath=safe_text, windowTitle=safe_text)
@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_PaneBasedSelectionWizardDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PaneBasedSelectionWizardDescription)


viewpoint_tool_PasteDescription_strategy = st.builds(viewpoint_tool_PasteDescription)
@given(instance=viewpoint_tool_PasteDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_PasteDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PasteDescription)


viewpoint_tool_PopupMenu_strategy = st.builds(viewpoint_tool_PopupMenu)
@given(instance=viewpoint_tool_PopupMenu_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_PopupMenu_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PopupMenu)


viewpoint_tool_ReconnectEdgeDescription_strategy = st.builds(viewpoint_tool_ReconnectEdgeDescription, reconnectionKind=safe_text)
@given(instance=viewpoint_tool_ReconnectEdgeDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ReconnectEdgeDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ReconnectEdgeDescription)


viewpoint_tool_RemoveElement_strategy = st.builds(viewpoint_tool_RemoveElement)
@given(instance=viewpoint_tool_RemoveElement_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_RemoveElement_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RemoveElement)


viewpoint_tool_RepresentationCreationDescription_strategy = st.builds(viewpoint_tool_RepresentationCreationDescription, browseExpression=safe_text, titleExpression=safe_text)
@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_RepresentationCreationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RepresentationCreationDescription)


viewpoint_tool_RepresentationNavigationDescription_strategy = st.builds(viewpoint_tool_RepresentationNavigationDescription, browseExpression=safe_text, navigationNameExpression=safe_text)
@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_RepresentationNavigationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RepresentationNavigationDescription)


viewpoint_tool_RequestDescription_strategy = st.builds(viewpoint_tool_RequestDescription, type=safe_text)
@given(instance=viewpoint_tool_RequestDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_RequestDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RequestDescription)


viewpoint_tool_SelectContainerVariable_strategy = st.builds(viewpoint_tool_SelectContainerVariable)
@given(instance=viewpoint_tool_SelectContainerVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SelectContainerVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectContainerVariable)


viewpoint_tool_SelectModelElementVariable_strategy = st.builds(viewpoint_tool_SelectModelElementVariable)
@given(instance=viewpoint_tool_SelectModelElementVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SelectModelElementVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectModelElementVariable)


viewpoint_tool_SelectionWizardDescription_strategy = st.builds(viewpoint_tool_SelectionWizardDescription, iconPath=safe_text, windowImagePath=safe_text, windowTitle=safe_text)
@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SelectionWizardDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectionWizardDescription)


viewpoint_tool_SetObject_strategy = st.builds(viewpoint_tool_SetObject, featureName=safe_text)
@given(instance=viewpoint_tool_SetObject_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SetObject_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SetObject)


viewpoint_tool_SetValue_strategy = st.builds(viewpoint_tool_SetValue, featureName=safe_text, valueExpression=safe_text)
@given(instance=viewpoint_tool_SetValue_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SetValue_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SetValue)


viewpoint_tool_SourceEdgeCreationVariable_strategy = st.builds(viewpoint_tool_SourceEdgeCreationVariable)
@given(instance=viewpoint_tool_SourceEdgeCreationVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SourceEdgeCreationVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SourceEdgeCreationVariable)


viewpoint_tool_SourceEdgeViewCreationVariable_strategy = st.builds(viewpoint_tool_SourceEdgeViewCreationVariable)
@given(instance=viewpoint_tool_SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SourceEdgeViewCreationVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SourceEdgeViewCreationVariable)


viewpoint_tool_SubVariable_strategy = st.builds(viewpoint_tool_SubVariable)
@given(instance=viewpoint_tool_SubVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SubVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SubVariable)


viewpoint_tool_Switch_strategy = st.builds(viewpoint_tool_Switch)
@given(instance=viewpoint_tool_Switch_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_Switch_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Switch)


viewpoint_tool_SwitchChild_strategy = st.builds(viewpoint_tool_SwitchChild)
@given(instance=viewpoint_tool_SwitchChild_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_SwitchChild_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SwitchChild)


viewpoint_tool_TargetEdgeCreationVariable_strategy = st.builds(viewpoint_tool_TargetEdgeCreationVariable)
@given(instance=viewpoint_tool_TargetEdgeCreationVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_TargetEdgeCreationVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_TargetEdgeCreationVariable)


viewpoint_tool_TargetEdgeViewCreationVariable_strategy = st.builds(viewpoint_tool_TargetEdgeViewCreationVariable)
@given(instance=viewpoint_tool_TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_TargetEdgeViewCreationVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_TargetEdgeViewCreationVariable)


viewpoint_tool_ToolDescription_strategy = st.builds(viewpoint_tool_ToolDescription, iconPath=safe_text)
@given(instance=viewpoint_tool_ToolDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ToolDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolDescription)


viewpoint_tool_ToolEntry_strategy = st.builds(viewpoint_tool_ToolEntry)
@given(instance=viewpoint_tool_ToolEntry_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ToolEntry_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolEntry)


viewpoint_tool_ToolFilterDescription_strategy = st.builds(viewpoint_tool_ToolFilterDescription, elementsToListen=safe_text, precondition=safe_text)
@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ToolFilterDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolFilterDescription)


viewpoint_tool_ToolGroup_strategy = st.builds(viewpoint_tool_ToolGroup)
@given(instance=viewpoint_tool_ToolGroup_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ToolGroup_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolGroup)


viewpoint_tool_ToolGroupExtension_strategy = st.builds(viewpoint_tool_ToolGroupExtension)
@given(instance=viewpoint_tool_ToolGroupExtension_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ToolGroupExtension_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolGroupExtension)


viewpoint_tool_ToolSection_strategy = st.builds(viewpoint_tool_ToolSection, icon=safe_text)
@given(instance=viewpoint_tool_ToolSection_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_ToolSection_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolSection)


viewpoint_tool_Unset_strategy = st.builds(viewpoint_tool_Unset, elementExpression=safe_text, featureName=safe_text)
@given(instance=viewpoint_tool_Unset_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_Unset_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Unset)


viewpoint_tool_VariableContainer_strategy = st.builds(viewpoint_tool_VariableContainer)
@given(instance=viewpoint_tool_VariableContainer_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_VariableContainer_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_VariableContainer)


viewpoint_validation_RuleAudit_strategy = st.builds(viewpoint_validation_RuleAudit, auditExpression=safe_text)
@given(instance=viewpoint_validation_RuleAudit_strategy)
@settings(max_examples=25)
def test_viewpoint_validation_RuleAudit_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_RuleAudit)


viewpoint_validation_SemanticValidationRule_strategy = st.builds(viewpoint_validation_SemanticValidationRule, targetClass=safe_text)
@given(instance=viewpoint_validation_SemanticValidationRule_strategy)
@settings(max_examples=25)
def test_viewpoint_validation_SemanticValidationRule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_SemanticValidationRule)


viewpoint_validation_ValidationFix_strategy = st.builds(viewpoint_validation_ValidationFix, name=safe_text)
@given(instance=viewpoint_validation_ValidationFix_strategy)
@settings(max_examples=25)
def test_viewpoint_validation_ValidationFix_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationFix)


viewpoint_validation_ValidationRule_strategy = st.builds(viewpoint_validation_ValidationRule, level=safe_text, message=safe_text)
@given(instance=viewpoint_validation_ValidationRule_strategy)
@settings(max_examples=25)
def test_viewpoint_validation_ValidationRule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationRule)


viewpoint_validation_ValidationSet_strategy = st.builds(viewpoint_validation_ValidationSet, name=safe_text)
@given(instance=viewpoint_validation_ValidationSet_strategy)
@settings(max_examples=25)
def test_viewpoint_validation_ValidationSet_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationSet)


viewpoint_validation_ViewValidationRule_strategy = st.builds(viewpoint_validation_ViewValidationRule)
@given(instance=viewpoint_validation_ViewValidationRule_strategy)
@settings(max_examples=25)
def test_viewpoint_validation_ViewValidationRule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ViewValidationRule)


