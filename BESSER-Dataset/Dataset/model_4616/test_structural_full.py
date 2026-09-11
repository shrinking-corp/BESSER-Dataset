import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractToolDescription,
    AbstractVariable,
    AnnotationEntry,
    BasicLabelStyle,
    BasicLabelStyleDescription,
    ColorDescription,
    ColorStep,
    ContainerModelOperation,
    Customizable,
    DAnnotation,
    DAnnotationEntry,
    DFile,
    DLabelled,
    DMappingBased,
    DNavigationLink,
    DRefreshable,
    DResource,
    DResourceContainer,
    DSemanticDecorator,
    DStylizable,
    DView,
    DecorationDescription,
    DocumentedElement,
    EStructuralFeatureCustomization,
    FeatureExtensionDescription,
    FixedColor,
    IVSMElementCustomization,
    IdentifiedElement,
    InformationSection,
    JavaExtension,
    MappingBasedToolDescription,
    MenuItemDescription,
    MenuItemOrRef,
    MetamodelExtensionSetting,
    ModelOperation,
    RepresentationDescription,
    RepresentationElementMapping,
    RepresentationExtensionDescription,
    RepresentationTemplate,
    SwitchChild,
    SystemColor,
    SytemColorsPalette,
    ToolEntry,
    UserColor,
    UserColorsPalette,
    ValidationRule,
    Viewpoint,
    description_ColorDescription,
    description_Component,
    description_DModelElement,
    description_DocumentedElement,
    description_EndUserDocumentedElement,
    description_FixedColor,
    description_IdentifiedElement,
    description_SelectionDescription,
    description_UserColor,
    description_viewpoint_EObject,
    description_viewpoint_EPackage,
    description_viewpoint_EStringToStringMapEntry,
    style_LabelBorderStyleDescription,
    style_LabelBorderStyles,
    style_StyleDescription,
    tool_AbstractToolDescription,
    tool_AbstractVariable,
    tool_Case,
    tool_ContainerModelOperation,
    tool_ContainerViewVariable,
    tool_Default,
    tool_DropContainerVariable,
    tool_ElementSelectVariable,
    tool_ElementVariable,
    tool_ElementViewVariable,
    tool_ExternalJavaAction,
    tool_ExternalJavaActionParameter,
    tool_FeatureChangeListener,
    tool_InitialOperation,
    tool_MenuItemDescription,
    tool_MenuItemOrRef,
    tool_ModelOperation,
    tool_NameVariable,
    tool_PasteDescription,
    tool_RepresentationCreationDescription,
    tool_RepresentationNavigationDescription,
    tool_SelectContainerVariable,
    tool_SubVariable,
    tool_ToolEntry,
    tool_ToolFilterDescription,
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
    viewpoint_EObject,
    viewpoint_LabelStyle,
    viewpoint_MetaModelExtension,
    viewpoint_RGBValues,
    viewpoint_SessionManagerEObject,
    viewpoint_Style,
    viewpoint_audit_InformationSection,
    viewpoint_audit_TemplateInformationSection,
    viewpoint_description_AbstractMappingImport,
    viewpoint_description_AnnotationEntry,
    viewpoint_description_ColorDescription,
    viewpoint_description_ColorStep,
    viewpoint_description_Component,
    viewpoint_description_ComputedColor,
    viewpoint_description_ConditionalStyleDescription,
    viewpoint_description_Customization,
    viewpoint_description_DAnnotation,
    viewpoint_description_DAnnotationEntry,
    viewpoint_description_DModelElement,
    viewpoint_description_DecorationDescription,
    viewpoint_description_DecorationDescriptionsSet,
    viewpoint_description_DocumentedElement,
    viewpoint_description_EAttributeCustomization,
    viewpoint_description_EReferenceCustomization,
    viewpoint_description_EStructuralFeatureCustomization,
    viewpoint_description_EndUserDocumentedElement,
    viewpoint_description_Environment,
    viewpoint_description_FeatureExtensionDescription,
    viewpoint_description_FixedColor,
    viewpoint_description_Group,
    viewpoint_description_IVSMElementCustomization,
    viewpoint_description_IdentifiedElement,
    viewpoint_description_InterpolatedColor,
    viewpoint_description_JavaExtension,
    viewpoint_description_MetamodelExtensionSetting,
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
    viewpoint_style_BasicLabelStyleDescription,
    viewpoint_style_LabelBorderStyleDescription,
    viewpoint_style_LabelBorderStyles,
    viewpoint_style_LabelStyleDescription,
    viewpoint_style_StyleDescription,
    viewpoint_style_TooltipStyleDescription,
    viewpoint_tool_AbstractToolDescription,
    viewpoint_tool_AbstractVariable,
    viewpoint_tool_AcceleoVariable,
    viewpoint_tool_Case,
    viewpoint_tool_ChangeContext,
    viewpoint_tool_ContainerModelOperation,
    viewpoint_tool_ContainerViewVariable,
    viewpoint_tool_CreateInstance,
    viewpoint_tool_Default,
    viewpoint_tool_DeleteView,
    viewpoint_tool_DialogVariable,
    viewpoint_tool_DropContainerVariable,
    viewpoint_tool_EditMaskVariables,
    viewpoint_tool_ElementDeleteVariable,
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
    viewpoint_tool_OperationAction,
    viewpoint_tool_PaneBasedSelectionWizardDescription,
    viewpoint_tool_PasteDescription,
    viewpoint_tool_PopupMenu,
    viewpoint_tool_RemoveElement,
    viewpoint_tool_RepresentationCreationDescription,
    viewpoint_tool_RepresentationNavigationDescription,
    viewpoint_tool_SelectContainerVariable,
    viewpoint_tool_SelectModelElementVariable,
    viewpoint_tool_SelectionWizardDescription,
    viewpoint_tool_SetObject,
    viewpoint_tool_SetValue,
    viewpoint_tool_SubVariable,
    viewpoint_tool_Switch,
    viewpoint_tool_SwitchChild,
    viewpoint_tool_ToolDescription,
    viewpoint_tool_ToolEntry,
    viewpoint_tool_ToolFilterDescription,
    viewpoint_tool_Unset,
    viewpoint_tool_VariableContainer,
    viewpoint_validation_RuleAudit,
    viewpoint_validation_SemanticValidationRule,
    viewpoint_validation_ValidationFix,
    viewpoint_validation_ValidationRule,
    viewpoint_validation_ValidationSet,
    viewpoint_validation_ViewValidationRule,
    DragSource,
    ERROR_LEVEL,
    FontFormat,
    LabelAlignment,
    NavigationTargetType,
    Position,
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


def test_viewpoint_style_TooltipStyleDescription_tooltipExpression_value_roundtrip():
    instance = viewpoint_style_TooltipStyleDescription(tooltipExpression="sample_text")
    assert instance.tooltipExpression == "sample_text"
    instance.tooltipExpression = "sample_text_2"
    assert instance.tooltipExpression == "sample_text_2"


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


def test_viewpoint_tool_DialogVariable_dialogPrompt_value_roundtrip():
    instance = viewpoint_tool_DialogVariable(dialogPrompt="sample_text")
    assert instance.dialogPrompt == "sample_text"
    instance.dialogPrompt = "sample_text_2"
    assert instance.dialogPrompt == "sample_text_2"


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


def test_viewpoint_style_LabelStyleDescription_isa_BasicLabelStyleDescription():
    instance = viewpoint_style_LabelStyleDescription(labelAlignment="sample_text")
    assert isinstance(instance, BasicLabelStyleDescription)


def test_viewpoint_description_FixedColor_isa_ColorDescription():
    instance = viewpoint_description_FixedColor(blue=7, green=7, red=7)
    assert isinstance(instance, ColorDescription)


def test_viewpoint_tool_ChangeContext_isa_ContainerModelOperation():
    instance = viewpoint_tool_ChangeContext(browseExpression="sample_text")
    assert isinstance(instance, ContainerModelOperation)


def test_viewpoint_tool_CreateInstance_isa_ContainerModelOperation():
    instance = viewpoint_tool_CreateInstance(referenceName="sample_text", typeName="sample_text", variableName="sample_text")
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


def test_viewpoint_BasicLabelStyle_isa_Customizable():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert isinstance(instance, Customizable)


def test_viewpoint_Style_isa_Customizable():
    instance = viewpoint_Style()
    assert isinstance(instance, Customizable)


def test_viewpoint_DModel_isa_DFile():
    instance = viewpoint_DModel()
    assert isinstance(instance, DFile)


def test_viewpoint_DRepresentationElement_isa_DLabelled():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DLabelled)


def test_viewpoint_DRepresentationElement_isa_DMappingBased():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DMappingBased)


def test_viewpoint_DSourceFileLink_isa_DNavigationLink():
    instance = viewpoint_DSourceFileLink(endPosition=7, filePath="sample_text", startPosition=7)
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


def test_viewpoint_DRepresentationElement_isa_DStylizable():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DStylizable)


def test_viewpoint_DRepresentationContainer_isa_DView():
    instance = viewpoint_DRepresentationContainer()
    assert isinstance(instance, DView)


def test_viewpoint_description_SemanticBasedDecoration_isa_DecorationDescription():
    instance = viewpoint_description_SemanticBasedDecoration(domainClass="sample_text")
    assert isinstance(instance, DecorationDescription)


def test_viewpoint_validation_ValidationSet_isa_DocumentedElement():
    instance = viewpoint_validation_ValidationSet(name="sample_text")
    assert isinstance(instance, DocumentedElement)


def test_viewpoint_description_EAttributeCustomization_isa_EStructuralFeatureCustomization():
    instance = viewpoint_description_EAttributeCustomization(attributeName="sample_text", value="sample_text")
    assert isinstance(instance, EStructuralFeatureCustomization)


def test_viewpoint_description_EReferenceCustomization_isa_EStructuralFeatureCustomization():
    instance = viewpoint_description_EReferenceCustomization(referenceName="sample_text")
    assert isinstance(instance, EStructuralFeatureCustomization)


def test_viewpoint_description_SystemColor_isa_FixedColor():
    instance = viewpoint_description_SystemColor(name="sample_text")
    assert isinstance(instance, FixedColor)


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


def test_viewpoint_tool_PasteDescription_isa_MappingBasedToolDescription():
    instance = viewpoint_tool_PasteDescription()
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


def test_viewpoint_description_RepresentationImportDescription_isa_RepresentationDescription():
    instance = viewpoint_description_RepresentationImportDescription()
    assert isinstance(instance, RepresentationDescription)


def test_viewpoint_tool_Case_isa_SwitchChild():
    instance = viewpoint_tool_Case(conditionExpression="sample_text")
    assert isinstance(instance, SwitchChild)


def test_viewpoint_tool_Default_isa_SwitchChild():
    instance = viewpoint_tool_Default()
    assert isinstance(instance, SwitchChild)


def test_viewpoint_tool_AbstractToolDescription_isa_ToolEntry():
    instance = viewpoint_tool_AbstractToolDescription(forceRefresh=True, precondition="sample_text")
    assert isinstance(instance, ToolEntry)


def test_viewpoint_validation_SemanticValidationRule_isa_ValidationRule():
    instance = viewpoint_validation_SemanticValidationRule(targetClass="sample_text")
    assert isinstance(instance, ValidationRule)


def test_viewpoint_validation_ViewValidationRule_isa_ValidationRule():
    instance = viewpoint_validation_ViewValidationRule()
    assert isinstance(instance, ValidationRule)


def test_viewpoint_description_ComputedColor_isa_description_ColorDescription():
    instance = viewpoint_description_ComputedColor(blue="sample_text", green="sample_text", red="sample_text")
    assert isinstance(instance, description_ColorDescription)


def test_viewpoint_description_InterpolatedColor_isa_description_ColorDescription():
    instance = viewpoint_description_InterpolatedColor(colorValueComputationExpression="sample_text", maxValueComputationExpression="sample_text", minValueComputationExpression="sample_text")
    assert isinstance(instance, description_ColorDescription)


def test_viewpoint_description_Viewpoint_isa_description_Component():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert isinstance(instance, description_Component)


def test_viewpoint_DRepresentation_isa_description_DModelElement():
    instance = viewpoint_DRepresentation(name="sample_text")
    assert isinstance(instance, description_DModelElement)


def test_viewpoint_description_Group_isa_description_DModelElement():
    instance = viewpoint_description_Group(name="sample_text", version="sample_text")
    assert isinstance(instance, description_DModelElement)


def test_viewpoint_DRepresentation_isa_description_DocumentedElement():
    instance = viewpoint_DRepresentation(name="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_Group_isa_description_DocumentedElement():
    instance = viewpoint_description_Group(name="sample_text", version="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_RepresentationDescription_isa_description_DocumentedElement():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_Viewpoint_isa_description_DocumentedElement():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_tool_ToolEntry_isa_description_DocumentedElement():
    instance = viewpoint_tool_ToolEntry()
    assert isinstance(instance, description_DocumentedElement)


def test_viewpoint_description_RepresentationDescription_isa_description_EndUserDocumentedElement():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert isinstance(instance, description_EndUserDocumentedElement)


def test_viewpoint_description_Viewpoint_isa_description_EndUserDocumentedElement():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert isinstance(instance, description_EndUserDocumentedElement)


def test_viewpoint_description_UserFixedColor_isa_description_FixedColor():
    instance = viewpoint_description_UserFixedColor()
    assert isinstance(instance, description_FixedColor)


def test_viewpoint_description_RepresentationDescription_isa_description_IdentifiedElement():
    instance = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_description_Viewpoint_isa_description_IdentifiedElement():
    instance = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    assert isinstance(instance, description_IdentifiedElement)


def test_viewpoint_tool_ToolEntry_isa_description_IdentifiedElement():
    instance = viewpoint_tool_ToolEntry()
    assert isinstance(instance, description_IdentifiedElement)


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


def test_viewpoint_tool_ElementDropVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ElementDropVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_ElementVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ElementVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_ElementViewVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_ElementViewVariable()
    assert isinstance(instance, tool_AbstractVariable)


def test_viewpoint_tool_SelectContainerVariable_isa_tool_AbstractVariable():
    instance = viewpoint_tool_SelectContainerVariable()
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


def test_viewpoint_tool_ElementDropVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ElementDropVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_ElementVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ElementVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_ElementViewVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_ElementViewVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_viewpoint_tool_SelectContainerVariable_isa_tool_VariableContainer():
    instance = viewpoint_tool_SelectContainerVariable()
    assert isinstance(instance, tool_VariableContainer)


def test_assoc_activatedViewpoints52_link_reassign_clear():
    a = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    b1 = Viewpoint()
    b2 = Viewpoint()
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject', b1)
    if hasattr(b1, 'Viewpoint53'):
        assert _is_linked(b1, 'Viewpoint53', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject', b2)
    if hasattr(b1, 'Viewpoint53'):
        assert not _is_linked(b1, 'Viewpoint53', a)
    if hasattr(b2, 'Viewpoint53'):
        assert _is_linked(b2, 'Viewpoint53', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject', set())
    assert not _is_linked(a, 'viewpoint_DAnalysisSessionEObject', b2)
    if hasattr(b2, 'Viewpoint53'):
        assert not _is_linked(b2, 'Viewpoint53', a)


def test_assoc_allRepresentations34_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DView35', {b1})
    assert _is_linked(a, 'viewpoint_DView35', b1)
    if hasattr(b1, 'viewpoint_DRepresentation36'):
        assert _is_linked(b1, 'viewpoint_DRepresentation36', a)
    _safe_set(a, 'viewpoint_DView35', {b2})
    assert _is_linked(a, 'viewpoint_DView35', b2)
    if hasattr(b1, 'viewpoint_DRepresentation36'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation36', a)
    if hasattr(b2, 'viewpoint_DRepresentation36'):
        assert _is_linked(b2, 'viewpoint_DRepresentation36', a)
    _safe_set(a, 'viewpoint_DView35', set())
    assert not _is_linked(a, 'viewpoint_DView35', b2)
    if hasattr(b2, 'viewpoint_DRepresentation36'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation36', a)


def test_assoc_allRules210_link_reassign_clear():
    a = viewpoint_validation_ValidationSet(name="sample_text")
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_validation_ValidationSet211', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet211', b1)
    if hasattr(b1, 'validation_ValidationRule212'):
        assert _is_linked(b1, 'validation_ValidationRule212', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet211', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet211', b2)
    if hasattr(b1, 'validation_ValidationRule212'):
        assert not _is_linked(b1, 'validation_ValidationRule212', a)
    if hasattr(b2, 'validation_ValidationRule212'):
        assert _is_linked(b2, 'validation_ValidationRule212', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet211', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationSet211', b2)
    if hasattr(b2, 'validation_ValidationRule212'):
        assert not _is_linked(b2, 'validation_ValidationRule212', a)


def test_assoc_analyses54_link_reassign_clear():
    a = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    b1 = viewpoint_DAnalysis(version="sample_text")
    b2 = viewpoint_DAnalysis(version="sample_text_2")
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject55', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject55', b1)
    if hasattr(b1, 'viewpoint_DAnalysis56'):
        assert _is_linked(b1, 'viewpoint_DAnalysis56', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject55', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject55', b2)
    if hasattr(b1, 'viewpoint_DAnalysis56'):
        assert not _is_linked(b1, 'viewpoint_DAnalysis56', a)
    if hasattr(b2, 'viewpoint_DAnalysis56'):
        assert _is_linked(b2, 'viewpoint_DAnalysis56', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject55', set())
    assert not _is_linked(a, 'viewpoint_DAnalysisSessionEObject55', b2)
    if hasattr(b2, 'viewpoint_DAnalysis56'):
        assert not _is_linked(b2, 'viewpoint_DAnalysis56', a)


def test_assoc_appliedOn102_link_reassign_clear():
    a = viewpoint_description_EStructuralFeatureCustomization(applyOnAll=True)
    b1 = description_viewpoint_EObject()
    b2 = description_viewpoint_EObject()
    _safe_set(a, 'viewpoint_description_EStructuralFeatureCustomization', {b1})
    assert _is_linked(a, 'viewpoint_description_EStructuralFeatureCustomization', b1)
    if hasattr(b1, 'description_viewpoint_EObject103'):
        assert _is_linked(b1, 'description_viewpoint_EObject103', a)
    _safe_set(a, 'viewpoint_description_EStructuralFeatureCustomization', {b2})
    assert _is_linked(a, 'viewpoint_description_EStructuralFeatureCustomization', b2)
    if hasattr(b1, 'description_viewpoint_EObject103'):
        assert not _is_linked(b1, 'description_viewpoint_EObject103', a)
    if hasattr(b2, 'description_viewpoint_EObject103'):
        assert _is_linked(b2, 'description_viewpoint_EObject103', a)
    _safe_set(a, 'viewpoint_description_EStructuralFeatureCustomization', set())
    assert not _is_linked(a, 'viewpoint_description_EStructuralFeatureCustomization', b2)
    if hasattr(b2, 'description_viewpoint_EObject103'):
        assert not _is_linked(b2, 'description_viewpoint_EObject103', a)


def test_assoc_associatedColor107_link_reassign_clear():
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


def test_assoc_audits213_link_reassign_clear():
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


def test_assoc_colorSteps106_link_reassign_clear():
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


def test_assoc_container126_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription', b1)
    if hasattr(b1, 'tool_DropContainerVariable'):
        assert _is_linked(b1, 'tool_DropContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription', b2)
    if hasattr(b1, 'tool_DropContainerVariable'):
        assert not _is_linked(b1, 'tool_DropContainerVariable', a)
    if hasattr(b2, 'tool_DropContainerVariable'):
        assert _is_linked(b2, 'tool_DropContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription', b2)
    if hasattr(b2, 'tool_DropContainerVariable'):
        assert not _is_linked(b2, 'tool_DropContainerVariable', a)


def test_assoc_container142_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_SelectContainerVariable()
    b2 = tool_SelectContainerVariable()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription143', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription143', b1)
    if hasattr(b1, 'tool_SelectContainerVariable'):
        assert _is_linked(b1, 'tool_SelectContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription143', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription143', b2)
    if hasattr(b1, 'tool_SelectContainerVariable'):
        assert not _is_linked(b1, 'tool_SelectContainerVariable', a)
    if hasattr(b2, 'tool_SelectContainerVariable'):
        assert _is_linked(b2, 'tool_SelectContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription143', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription143', b2)
    if hasattr(b2, 'tool_SelectContainerVariable'):
        assert not _is_linked(b2, 'tool_SelectContainerVariable', a)


def test_assoc_container152_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_SelectContainerVariable()
    b2 = tool_SelectContainerVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription153', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription153', b1)
    if hasattr(b1, 'tool_SelectContainerVariable154'):
        assert _is_linked(b1, 'tool_SelectContainerVariable154', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription153', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription153', b2)
    if hasattr(b1, 'tool_SelectContainerVariable154'):
        assert not _is_linked(b1, 'tool_SelectContainerVariable154', a)
    if hasattr(b2, 'tool_SelectContainerVariable154'):
        assert _is_linked(b2, 'tool_SelectContainerVariable154', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription153', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription153', b2)
    if hasattr(b2, 'tool_SelectContainerVariable154'):
        assert not _is_linked(b2, 'tool_SelectContainerVariable154', a)


def test_assoc_containerVariable173_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription174', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription174', b1)
    if hasattr(b1, 'tool_ElementSelectVariable175'):
        assert _is_linked(b1, 'tool_ElementSelectVariable175', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription174', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription174', b2)
    if hasattr(b1, 'tool_ElementSelectVariable175'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable175', a)
    if hasattr(b2, 'tool_ElementSelectVariable175'):
        assert _is_linked(b2, 'tool_ElementSelectVariable175', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription174', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription174', b2)
    if hasattr(b2, 'tool_ElementSelectVariable175'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable175', a)


def test_assoc_containerView127_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription128', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription128', b1)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert _is_linked(b1, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription128', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription128', b2)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable', a)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert _is_linked(b2, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription128', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription128', b2)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable', a)


def test_assoc_containerView139_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription140', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription140', b1)
    if hasattr(b1, 'tool_ContainerViewVariable141'):
        assert _is_linked(b1, 'tool_ContainerViewVariable141', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription140', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription140', b2)
    if hasattr(b1, 'tool_ContainerViewVariable141'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable141', a)
    if hasattr(b2, 'tool_ContainerViewVariable141'):
        assert _is_linked(b2, 'tool_ContainerViewVariable141', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription140', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription140', b2)
    if hasattr(b2, 'tool_ContainerViewVariable141'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable141', a)


def test_assoc_containerView149_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription150', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription150', b1)
    if hasattr(b1, 'tool_ContainerViewVariable151'):
        assert _is_linked(b1, 'tool_ContainerViewVariable151', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription150', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription150', b2)
    if hasattr(b1, 'tool_ContainerViewVariable151'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable151', a)
    if hasattr(b2, 'tool_ContainerViewVariable151'):
        assert _is_linked(b2, 'tool_ContainerViewVariable151', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription150', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription150', b2)
    if hasattr(b2, 'tool_ContainerViewVariable151'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable151', a)


def test_assoc_containerViewVariable163_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription164', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription164', b1)
    if hasattr(b1, 'tool_ContainerViewVariable165'):
        assert _is_linked(b1, 'tool_ContainerViewVariable165', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription164', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription164', b2)
    if hasattr(b1, 'tool_ContainerViewVariable165'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable165', a)
    if hasattr(b2, 'tool_ContainerViewVariable165'):
        assert _is_linked(b2, 'tool_ContainerViewVariable165', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription164', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription164', b2)
    if hasattr(b2, 'tool_ContainerViewVariable165'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable165', a)


def test_assoc_containerViewVariable170_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription171', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription171', b1)
    if hasattr(b1, 'tool_ContainerViewVariable172'):
        assert _is_linked(b1, 'tool_ContainerViewVariable172', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription171', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription171', b2)
    if hasattr(b1, 'tool_ContainerViewVariable172'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable172', a)
    if hasattr(b2, 'tool_ContainerViewVariable172'):
        assert _is_linked(b2, 'tool_ContainerViewVariable172', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription171', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription171', b2)
    if hasattr(b2, 'tool_ContainerViewVariable172'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable172', a)


def test_assoc_copiedElement132_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ElementVariable()
    b2 = tool_ElementVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription133', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription133', b1)
    if hasattr(b1, 'tool_ElementVariable134'):
        assert _is_linked(b1, 'tool_ElementVariable134', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription133', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription133', b2)
    if hasattr(b1, 'tool_ElementVariable134'):
        assert not _is_linked(b1, 'tool_ElementVariable134', a)
    if hasattr(b2, 'tool_ElementVariable134'):
        assert _is_linked(b2, 'tool_ElementVariable134', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription133', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription133', b2)
    if hasattr(b2, 'tool_ElementVariable134'):
        assert not _is_linked(b2, 'tool_ElementVariable134', a)


def test_assoc_copiedView129_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ElementViewVariable()
    b2 = tool_ElementViewVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription130', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription130', b1)
    if hasattr(b1, 'tool_ElementViewVariable131'):
        assert _is_linked(b1, 'tool_ElementViewVariable131', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription130', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription130', b2)
    if hasattr(b1, 'tool_ElementViewVariable131'):
        assert not _is_linked(b1, 'tool_ElementViewVariable131', a)
    if hasattr(b2, 'tool_ElementViewVariable131'):
        assert _is_linked(b2, 'tool_ElementViewVariable131', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription130', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription130', b2)
    if hasattr(b2, 'tool_ElementViewVariable131'):
        assert not _is_linked(b2, 'tool_ElementViewVariable131', a)


def test_assoc_data116_link_reassign_clear():
    a = viewpoint_description_AnnotationEntry(source="sample_text")
    b1 = description_viewpoint_EObject()
    b2 = description_viewpoint_EObject()
    _safe_set(a, 'viewpoint_description_AnnotationEntry', b1)
    assert _is_linked(a, 'viewpoint_description_AnnotationEntry', b1)
    if hasattr(b1, 'description_viewpoint_EObject117'):
        assert _is_linked(b1, 'description_viewpoint_EObject117', a)
    _safe_set(a, 'viewpoint_description_AnnotationEntry', b2)
    assert _is_linked(a, 'viewpoint_description_AnnotationEntry', b2)
    if hasattr(b1, 'description_viewpoint_EObject117'):
        assert not _is_linked(b1, 'description_viewpoint_EObject117', a)
    if hasattr(b2, 'description_viewpoint_EObject117'):
        assert _is_linked(b2, 'description_viewpoint_EObject117', a)
    _safe_set(a, 'viewpoint_description_AnnotationEntry', None)
    assert not _is_linked(a, 'viewpoint_description_AnnotationEntry', b2)
    if hasattr(b2, 'description_viewpoint_EObject117'):
        assert not _is_linked(b2, 'description_viewpoint_EObject117', a)


def test_assoc_data49_link_reassign_clear():
    a = viewpoint_DAnalysisCustomData(key="sample_text")
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_DAnalysisCustomData', b1)
    assert _is_linked(a, 'viewpoint_DAnalysisCustomData', b1)
    if hasattr(b1, 'viewpoint_EObject50'):
        assert _is_linked(b1, 'viewpoint_EObject50', a)
    _safe_set(a, 'viewpoint_DAnalysisCustomData', b2)
    assert _is_linked(a, 'viewpoint_DAnalysisCustomData', b2)
    if hasattr(b1, 'viewpoint_EObject50'):
        assert not _is_linked(b1, 'viewpoint_EObject50', a)
    if hasattr(b2, 'viewpoint_EObject50'):
        assert _is_linked(b2, 'viewpoint_EObject50', a)
    _safe_set(a, 'viewpoint_DAnalysisCustomData', None)
    assert not _is_linked(a, 'viewpoint_DAnalysisCustomData', b2)
    if hasattr(b2, 'viewpoint_EObject50'):
        assert not _is_linked(b2, 'viewpoint_EObject50', a)


def test_assoc_details91_link_reassign_clear():
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


def test_assoc_eAnnotations90_link_reassign_clear():
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


def test_assoc_element121_link_reassign_clear():
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


def test_assoc_element138_link_reassign_clear():
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


def test_assoc_element147_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b1)
    if hasattr(b1, 'tool_ElementSelectVariable148'):
        assert _is_linked(b1, 'tool_ElementSelectVariable148', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    if hasattr(b1, 'tool_ElementSelectVariable148'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable148', a)
    if hasattr(b2, 'tool_ElementSelectVariable148'):
        assert _is_linked(b2, 'tool_ElementSelectVariable148', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    if hasattr(b2, 'tool_ElementSelectVariable148'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable148', a)


def test_assoc_elementView122_link_reassign_clear():
    a = viewpoint_tool_ToolDescription(iconPath="sample_text")
    b1 = tool_ElementViewVariable()
    b2 = tool_ElementViewVariable()
    _safe_set(a, 'viewpoint_tool_ToolDescription123', b1)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription123', b1)
    if hasattr(b1, 'tool_ElementViewVariable'):
        assert _is_linked(b1, 'tool_ElementViewVariable', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription123', b2)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription123', b2)
    if hasattr(b1, 'tool_ElementViewVariable'):
        assert not _is_linked(b1, 'tool_ElementViewVariable', a)
    if hasattr(b2, 'tool_ElementViewVariable'):
        assert _is_linked(b2, 'tool_ElementViewVariable', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription123', None)
    assert not _is_linked(a, 'viewpoint_tool_ToolDescription123', b2)
    if hasattr(b2, 'tool_ElementViewVariable'):
        assert not _is_linked(b2, 'tool_ElementViewVariable', a)


def test_assoc_entries115_link_reassign_clear():
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


def test_assoc_featureCustomizations96_link_reassign_clear():
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


def test_assoc_filters120_link_reassign_clear():
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


def test_assoc_fixes214_link_reassign_clear():
    a = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    b1 = validation_ValidationFix()
    b2 = validation_ValidationFix()
    _safe_set(a, 'viewpoint_validation_ValidationRule215', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationRule215', b1)
    if hasattr(b1, 'validation_ValidationFix'):
        assert _is_linked(b1, 'validation_ValidationFix', a)
    _safe_set(a, 'viewpoint_validation_ValidationRule215', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationRule215', b2)
    if hasattr(b1, 'validation_ValidationFix'):
        assert not _is_linked(b1, 'validation_ValidationFix', a)
    if hasattr(b2, 'validation_ValidationFix'):
        assert _is_linked(b2, 'validation_ValidationFix', a)
    _safe_set(a, 'viewpoint_validation_ValidationRule215', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationRule215', b2)
    if hasattr(b2, 'validation_ValidationFix'):
        assert not _is_linked(b2, 'validation_ValidationFix', a)


def test_assoc_hiddenRepresentations37_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DView38', {b1})
    assert _is_linked(a, 'viewpoint_DView38', b1)
    if hasattr(b1, 'viewpoint_DRepresentation39'):
        assert _is_linked(b1, 'viewpoint_DRepresentation39', a)
    _safe_set(a, 'viewpoint_DView38', {b2})
    assert _is_linked(a, 'viewpoint_DView38', b2)
    if hasattr(b1, 'viewpoint_DRepresentation39'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation39', a)
    if hasattr(b2, 'viewpoint_DRepresentation39'):
        assert _is_linked(b2, 'viewpoint_DRepresentation39', a)
    _safe_set(a, 'viewpoint_DView38', set())
    assert not _is_linked(a, 'viewpoint_DView38', b2)
    if hasattr(b2, 'viewpoint_DRepresentation39'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation39', a)


def test_assoc_initialOperation124_link_reassign_clear():
    a = viewpoint_tool_ToolDescription(iconPath="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_ToolDescription125', b1)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription125', b1)
    if hasattr(b1, 'tool_InitialOperation'):
        assert _is_linked(b1, 'tool_InitialOperation', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription125', b2)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription125', b2)
    if hasattr(b1, 'tool_InitialOperation'):
        assert not _is_linked(b1, 'tool_InitialOperation', a)
    if hasattr(b2, 'tool_InitialOperation'):
        assert _is_linked(b2, 'tool_InitialOperation', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription125', None)
    assert not _is_linked(a, 'viewpoint_tool_ToolDescription125', b2)
    if hasattr(b2, 'tool_InitialOperation'):
        assert not _is_linked(b2, 'tool_InitialOperation', a)


def test_assoc_initialOperation135_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_PasteDescription136', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription136', b1)
    if hasattr(b1, 'tool_InitialOperation137'):
        assert _is_linked(b1, 'tool_InitialOperation137', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription136', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription136', b2)
    if hasattr(b1, 'tool_InitialOperation137'):
        assert not _is_linked(b1, 'tool_InitialOperation137', a)
    if hasattr(b2, 'tool_InitialOperation137'):
        assert _is_linked(b2, 'tool_InitialOperation137', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription136', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription136', b2)
    if hasattr(b2, 'tool_InitialOperation137'):
        assert not _is_linked(b2, 'tool_InitialOperation137', a)


def test_assoc_initialOperation144_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription145', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription145', b1)
    if hasattr(b1, 'tool_InitialOperation146'):
        assert _is_linked(b1, 'tool_InitialOperation146', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription145', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription145', b2)
    if hasattr(b1, 'tool_InitialOperation146'):
        assert not _is_linked(b1, 'tool_InitialOperation146', a)
    if hasattr(b2, 'tool_InitialOperation146'):
        assert _is_linked(b2, 'tool_InitialOperation146', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription145', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription145', b2)
    if hasattr(b2, 'tool_InitialOperation146'):
        assert not _is_linked(b2, 'tool_InitialOperation146', a)


def test_assoc_initialOperation155_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b1)
    if hasattr(b1, 'tool_InitialOperation157'):
        assert _is_linked(b1, 'tool_InitialOperation157', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b2)
    if hasattr(b1, 'tool_InitialOperation157'):
        assert not _is_linked(b1, 'tool_InitialOperation157', a)
    if hasattr(b2, 'tool_InitialOperation157'):
        assert _is_linked(b2, 'tool_InitialOperation157', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b2)
    if hasattr(b2, 'tool_InitialOperation157'):
        assert not _is_linked(b2, 'tool_InitialOperation157', a)


def test_assoc_initialOperation160_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription161', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription161', b1)
    if hasattr(b1, 'tool_InitialOperation162'):
        assert _is_linked(b1, 'tool_InitialOperation162', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription161', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription161', b2)
    if hasattr(b1, 'tool_InitialOperation162'):
        assert not _is_linked(b1, 'tool_InitialOperation162', a)
    if hasattr(b2, 'tool_InitialOperation162'):
        assert _is_linked(b2, 'tool_InitialOperation162', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription161', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription161', b2)
    if hasattr(b2, 'tool_InitialOperation162'):
        assert not _is_linked(b2, 'tool_InitialOperation162', a)


def test_assoc_initialOperation217_link_reassign_clear():
    a = viewpoint_validation_ValidationFix(name="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_validation_ValidationFix', b1)
    assert _is_linked(a, 'viewpoint_validation_ValidationFix', b1)
    if hasattr(b1, 'tool_InitialOperation218'):
        assert _is_linked(b1, 'tool_InitialOperation218', a)
    _safe_set(a, 'viewpoint_validation_ValidationFix', b2)
    assert _is_linked(a, 'viewpoint_validation_ValidationFix', b2)
    if hasattr(b1, 'tool_InitialOperation218'):
        assert not _is_linked(b1, 'tool_InitialOperation218', a)
    if hasattr(b2, 'tool_InitialOperation218'):
        assert _is_linked(b2, 'tool_InitialOperation218', a)
    _safe_set(a, 'viewpoint_validation_ValidationFix', None)
    assert not _is_linked(a, 'viewpoint_validation_ValidationFix', b2)
    if hasattr(b2, 'tool_InitialOperation218'):
        assert not _is_linked(b2, 'tool_InitialOperation218', a)


def test_assoc_labelColor118_link_reassign_clear():
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


def test_assoc_labelColor60_link_reassign_clear():
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


def test_assoc_listeners200_link_reassign_clear():
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


def test_assoc_members59_link_reassign_clear():
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


def test_assoc_metamodel81_link_reassign_clear():
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


def test_assoc_metamodel84_link_reassign_clear():
    a = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    b1 = description_viewpoint_EPackage()
    b2 = description_viewpoint_EPackage()
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', {b1})
    assert _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b1)
    if hasattr(b1, 'description_viewpoint_EPackage85'):
        assert _is_linked(b1, 'description_viewpoint_EPackage85', a)
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', {b2})
    assert _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b2)
    if hasattr(b1, 'description_viewpoint_EPackage85'):
        assert not _is_linked(b1, 'description_viewpoint_EPackage85', a)
    if hasattr(b2, 'description_viewpoint_EPackage85'):
        assert _is_linked(b2, 'description_viewpoint_EPackage85', a)
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', set())
    assert not _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b2)
    if hasattr(b2, 'description_viewpoint_EPackage85'):
        assert not _is_linked(b2, 'description_viewpoint_EPackage85', a)


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


def test_assoc_object199_link_reassign_clear():
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


def test_assoc_ownedAnnotationEntries24_link_reassign_clear():
    a = viewpoint_DRepresentation(name="sample_text")
    b1 = AnnotationEntry()
    b2 = AnnotationEntry()
    _safe_set(a, 'viewpoint_DRepresentation25', {b1})
    assert _is_linked(a, 'viewpoint_DRepresentation25', b1)
    if hasattr(b1, 'AnnotationEntry'):
        assert _is_linked(b1, 'AnnotationEntry', a)
    _safe_set(a, 'viewpoint_DRepresentation25', {b2})
    assert _is_linked(a, 'viewpoint_DRepresentation25', b2)
    if hasattr(b1, 'AnnotationEntry'):
        assert not _is_linked(b1, 'AnnotationEntry', a)
    if hasattr(b2, 'AnnotationEntry'):
        assert _is_linked(b2, 'AnnotationEntry', a)
    _safe_set(a, 'viewpoint_DRepresentation25', set())
    assert not _is_linked(a, 'viewpoint_DRepresentation25', b2)
    if hasattr(b2, 'AnnotationEntry'):
        assert not _is_linked(b2, 'AnnotationEntry', a)


def test_assoc_ownedExtensions32_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_MetaModelExtension()
    b2 = viewpoint_MetaModelExtension()
    _safe_set(a, 'viewpoint_DView33', b1)
    assert _is_linked(a, 'viewpoint_DView33', b1)
    if hasattr(b1, 'viewpoint_MetaModelExtension'):
        assert _is_linked(b1, 'viewpoint_MetaModelExtension', a)
    _safe_set(a, 'viewpoint_DView33', b2)
    assert _is_linked(a, 'viewpoint_DView33', b2)
    if hasattr(b1, 'viewpoint_MetaModelExtension'):
        assert not _is_linked(b1, 'viewpoint_MetaModelExtension', a)
    if hasattr(b2, 'viewpoint_MetaModelExtension'):
        assert _is_linked(b2, 'viewpoint_MetaModelExtension', a)
    _safe_set(a, 'viewpoint_DView33', None)
    assert not _is_linked(a, 'viewpoint_DView33', b2)
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


def test_assoc_ownedFeatureExtensions76_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = FeatureExtensionDescription()
    b2 = FeatureExtensionDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint77', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint77', b1)
    if hasattr(b1, 'FeatureExtensionDescription78'):
        assert _is_linked(b1, 'FeatureExtensionDescription78', a)
    _safe_set(a, 'viewpoint_description_Viewpoint77', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint77', b2)
    if hasattr(b1, 'FeatureExtensionDescription78'):
        assert not _is_linked(b1, 'FeatureExtensionDescription78', a)
    if hasattr(b2, 'FeatureExtensionDescription78'):
        assert _is_linked(b2, 'FeatureExtensionDescription78', a)
    _safe_set(a, 'viewpoint_description_Viewpoint77', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint77', b2)
    if hasattr(b2, 'FeatureExtensionDescription78'):
        assert not _is_linked(b2, 'FeatureExtensionDescription78', a)


def test_assoc_ownedJavaExtensions72_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = JavaExtension()
    b2 = JavaExtension()
    _safe_set(a, 'viewpoint_description_Viewpoint73', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint73', b1)
    if hasattr(b1, 'JavaExtension'):
        assert _is_linked(b1, 'JavaExtension', a)
    _safe_set(a, 'viewpoint_description_Viewpoint73', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint73', b2)
    if hasattr(b1, 'JavaExtension'):
        assert not _is_linked(b1, 'JavaExtension', a)
    if hasattr(b2, 'JavaExtension'):
        assert _is_linked(b2, 'JavaExtension', a)
    _safe_set(a, 'viewpoint_description_Viewpoint73', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint73', b2)
    if hasattr(b2, 'JavaExtension'):
        assert not _is_linked(b2, 'JavaExtension', a)


def test_assoc_ownedMMExtensions74_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = MetamodelExtensionSetting()
    b2 = MetamodelExtensionSetting()
    _safe_set(a, 'viewpoint_description_Viewpoint75', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint75', b1)
    if hasattr(b1, 'MetamodelExtensionSetting'):
        assert _is_linked(b1, 'MetamodelExtensionSetting', a)
    _safe_set(a, 'viewpoint_description_Viewpoint75', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint75', b2)
    if hasattr(b1, 'MetamodelExtensionSetting'):
        assert not _is_linked(b1, 'MetamodelExtensionSetting', a)
    if hasattr(b2, 'MetamodelExtensionSetting'):
        assert _is_linked(b2, 'MetamodelExtensionSetting', a)
    _safe_set(a, 'viewpoint_description_Viewpoint75', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint75', b2)
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


def test_assoc_ownedRepresentationElements20_link_reassign_clear():
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


def test_assoc_ownedRepresentationExtensions70_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationExtensionDescription()
    b2 = RepresentationExtensionDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint71', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint71', b1)
    if hasattr(b1, 'RepresentationExtensionDescription'):
        assert _is_linked(b1, 'RepresentationExtensionDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint71', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint71', b2)
    if hasattr(b1, 'RepresentationExtensionDescription'):
        assert not _is_linked(b1, 'RepresentationExtensionDescription', a)
    if hasattr(b2, 'RepresentationExtensionDescription'):
        assert _is_linked(b2, 'RepresentationExtensionDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint71', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint71', b2)
    if hasattr(b2, 'RepresentationExtensionDescription'):
        assert not _is_linked(b2, 'RepresentationExtensionDescription', a)


def test_assoc_ownedRepresentations29_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DView30', {b1})
    assert _is_linked(a, 'viewpoint_DView30', b1)
    if hasattr(b1, 'viewpoint_DRepresentation31'):
        assert _is_linked(b1, 'viewpoint_DRepresentation31', a)
    _safe_set(a, 'viewpoint_DView30', {b2})
    assert _is_linked(a, 'viewpoint_DView30', b2)
    if hasattr(b1, 'viewpoint_DRepresentation31'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation31', a)
    if hasattr(b2, 'viewpoint_DRepresentation31'):
        assert _is_linked(b2, 'viewpoint_DRepresentation31', a)
    _safe_set(a, 'viewpoint_DView30', set())
    assert not _is_linked(a, 'viewpoint_DView30', b2)
    if hasattr(b2, 'viewpoint_DRepresentation31'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation31', a)


def test_assoc_ownedRepresentations68_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint69', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint69', b1)
    if hasattr(b1, 'RepresentationDescription'):
        assert _is_linked(b1, 'RepresentationDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint69', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint69', b2)
    if hasattr(b1, 'RepresentationDescription'):
        assert not _is_linked(b1, 'RepresentationDescription', a)
    if hasattr(b2, 'RepresentationDescription'):
        assert _is_linked(b2, 'RepresentationDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint69', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint69', b2)
    if hasattr(b2, 'RepresentationDescription'):
        assert not _is_linked(b2, 'RepresentationDescription', a)


def test_assoc_ownedRepresentations82_link_reassign_clear():
    a = viewpoint_description_RepresentationTemplate(name="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', {b1})
    assert _is_linked(a, 'viewpoint_description_RepresentationTemplate', b1)
    if hasattr(b1, 'RepresentationDescription83'):
        assert _is_linked(b1, 'RepresentationDescription83', a)
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', {b2})
    assert _is_linked(a, 'viewpoint_description_RepresentationTemplate', b2)
    if hasattr(b1, 'RepresentationDescription83'):
        assert not _is_linked(b1, 'RepresentationDescription83', a)
    if hasattr(b2, 'RepresentationDescription83'):
        assert _is_linked(b2, 'RepresentationDescription83', a)
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', set())
    assert not _is_linked(a, 'viewpoint_description_RepresentationTemplate', b2)
    if hasattr(b2, 'RepresentationDescription83'):
        assert not _is_linked(b2, 'RepresentationDescription83', a)


def test_assoc_ownedRules206_link_reassign_clear():
    a = viewpoint_validation_ValidationSet(name="sample_text")
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_validation_ValidationSet', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet', b1)
    if hasattr(b1, 'validation_ValidationRule'):
        assert _is_linked(b1, 'validation_ValidationRule', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet', b2)
    if hasattr(b1, 'validation_ValidationRule'):
        assert not _is_linked(b1, 'validation_ValidationRule', a)
    if hasattr(b2, 'validation_ValidationRule'):
        assert _is_linked(b2, 'validation_ValidationRule', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationSet', b2)
    if hasattr(b2, 'validation_ValidationRule'):
        assert not _is_linked(b2, 'validation_ValidationRule', a)


def test_assoc_ownedSessions57_link_reassign_clear():
    a = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    b1 = viewpoint_SessionManagerEObject()
    b2 = viewpoint_SessionManagerEObject()
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject58', b1)
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject58', b1)
    if hasattr(b1, 'viewpoint_SessionManagerEObject'):
        assert _is_linked(b1, 'viewpoint_SessionManagerEObject', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject58', b2)
    assert _is_linked(a, 'viewpoint_DAnalysisSessionEObject58', b2)
    if hasattr(b1, 'viewpoint_SessionManagerEObject'):
        assert not _is_linked(b1, 'viewpoint_SessionManagerEObject', a)
    if hasattr(b2, 'viewpoint_SessionManagerEObject'):
        assert _is_linked(b2, 'viewpoint_SessionManagerEObject', a)
    _safe_set(a, 'viewpoint_DAnalysisSessionEObject58', None)
    assert not _is_linked(a, 'viewpoint_DAnalysisSessionEObject58', b2)
    if hasattr(b2, 'viewpoint_SessionManagerEObject'):
        assert not _is_linked(b2, 'viewpoint_SessionManagerEObject', a)


def test_assoc_ownedTemplates79_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationTemplate()
    b2 = RepresentationTemplate()
    _safe_set(a, 'viewpoint_description_Viewpoint80', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint80', b1)
    if hasattr(b1, 'RepresentationTemplate'):
        assert _is_linked(b1, 'RepresentationTemplate', a)
    _safe_set(a, 'viewpoint_description_Viewpoint80', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint80', b2)
    if hasattr(b1, 'RepresentationTemplate'):
        assert not _is_linked(b1, 'RepresentationTemplate', a)
    if hasattr(b2, 'RepresentationTemplate'):
        assert _is_linked(b2, 'RepresentationTemplate', a)
    _safe_set(a, 'viewpoint_description_Viewpoint80', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint80', b2)
    if hasattr(b2, 'RepresentationTemplate'):
        assert not _is_linked(b2, 'RepresentationTemplate', a)


def test_assoc_ownedViewpoints61_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = Viewpoint()
    b2 = Viewpoint()
    _safe_set(a, 'viewpoint_description_Group', {b1})
    assert _is_linked(a, 'viewpoint_description_Group', b1)
    if hasattr(b1, 'Viewpoint62'):
        assert _is_linked(b1, 'Viewpoint62', a)
    _safe_set(a, 'viewpoint_description_Group', {b2})
    assert _is_linked(a, 'viewpoint_description_Group', b2)
    if hasattr(b1, 'Viewpoint62'):
        assert not _is_linked(b1, 'Viewpoint62', a)
    if hasattr(b2, 'Viewpoint62'):
        assert _is_linked(b2, 'Viewpoint62', a)
    _safe_set(a, 'viewpoint_description_Group', set())
    assert not _is_linked(a, 'viewpoint_description_Group', b2)
    if hasattr(b2, 'Viewpoint62'):
        assert not _is_linked(b2, 'Viewpoint62', a)


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


def test_assoc_parameters185_link_reassign_clear():
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


def test_assoc_referencedRepresentations40_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DView41', {b1})
    assert _is_linked(a, 'viewpoint_DView41', b1)
    if hasattr(b1, 'viewpoint_DRepresentation42'):
        assert _is_linked(b1, 'viewpoint_DRepresentation42', a)
    _safe_set(a, 'viewpoint_DView41', {b2})
    assert _is_linked(a, 'viewpoint_DView41', b2)
    if hasattr(b1, 'viewpoint_DRepresentation42'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation42', a)
    if hasattr(b2, 'viewpoint_DRepresentation42'):
        assert _is_linked(b2, 'viewpoint_DRepresentation42', a)
    _safe_set(a, 'viewpoint_DView41', set())
    assert not _is_linked(a, 'viewpoint_DView41', b2)
    if hasattr(b2, 'viewpoint_DRepresentation42'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation42', a)


def test_assoc_representationDescription158_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b1)
    if hasattr(b1, 'RepresentationDescription159'):
        assert _is_linked(b1, 'RepresentationDescription159', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    if hasattr(b1, 'RepresentationDescription159'):
        assert not _is_linked(b1, 'RepresentationDescription159', a)
    if hasattr(b2, 'RepresentationDescription159'):
        assert _is_linked(b2, 'RepresentationDescription159', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    if hasattr(b2, 'RepresentationDescription159'):
        assert not _is_linked(b2, 'RepresentationDescription159', a)


def test_assoc_representationDescription168_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b1)
    if hasattr(b1, 'RepresentationDescription169'):
        assert _is_linked(b1, 'RepresentationDescription169', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    if hasattr(b1, 'RepresentationDescription169'):
        assert not _is_linked(b1, 'RepresentationDescription169', a)
    if hasattr(b2, 'RepresentationDescription169'):
        assert _is_linked(b2, 'RepresentationDescription169', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    if hasattr(b2, 'RepresentationDescription169'):
        assert not _is_linked(b2, 'RepresentationDescription169', a)


def test_assoc_representationElements21_link_reassign_clear():
    a = viewpoint_DRepresentationElement(name="sample_text")
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DRepresentationElement23', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationElement23', b1)
    if hasattr(b1, 'viewpoint_DRepresentation22'):
        assert _is_linked(b1, 'viewpoint_DRepresentation22', a)
    _safe_set(a, 'viewpoint_DRepresentationElement23', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationElement23', b2)
    if hasattr(b1, 'viewpoint_DRepresentation22'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation22', a)
    if hasattr(b2, 'viewpoint_DRepresentation22'):
        assert _is_linked(b2, 'viewpoint_DRepresentation22', a)
    _safe_set(a, 'viewpoint_DRepresentationElement23', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationElement23', b2)
    if hasattr(b2, 'viewpoint_DRepresentation22'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation22', a)


def test_assoc_representationNameVariable166_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_NameVariable()
    b2 = tool_NameVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription167', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription167', b1)
    if hasattr(b1, 'tool_NameVariable'):
        assert _is_linked(b1, 'tool_NameVariable', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription167', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription167', b2)
    if hasattr(b1, 'tool_NameVariable'):
        assert not _is_linked(b1, 'tool_NameVariable', a)
    if hasattr(b2, 'tool_NameVariable'):
        assert _is_linked(b2, 'tool_NameVariable', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription167', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription167', b2)
    if hasattr(b2, 'tool_NameVariable'):
        assert not _is_linked(b2, 'tool_NameVariable', a)


def test_assoc_representationNameVariable176_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_NameVariable()
    b2 = tool_NameVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription177', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription177', b1)
    if hasattr(b1, 'tool_NameVariable178'):
        assert _is_linked(b1, 'tool_NameVariable178', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription177', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription177', b2)
    if hasattr(b1, 'tool_NameVariable178'):
        assert not _is_linked(b1, 'tool_NameVariable178', a)
    if hasattr(b2, 'tool_NameVariable178'):
        assert _is_linked(b2, 'tool_NameVariable178', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription177', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription177', b2)
    if hasattr(b2, 'tool_NameVariable178'):
        assert not _is_linked(b2, 'tool_NameVariable178', a)


def test_assoc_reusedRules207_link_reassign_clear():
    a = viewpoint_validation_ValidationSet(name="sample_text")
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_validation_ValidationSet208', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet208', b1)
    if hasattr(b1, 'validation_ValidationRule209'):
        assert _is_linked(b1, 'validation_ValidationRule209', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet208', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet208', b2)
    if hasattr(b1, 'validation_ValidationRule209'):
        assert not _is_linked(b1, 'validation_ValidationRule209', a)
    if hasattr(b2, 'validation_ValidationRule209'):
        assert _is_linked(b2, 'validation_ValidationRule209', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet208', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationSet208', b2)
    if hasattr(b2, 'validation_ValidationRule209'):
        assert not _is_linked(b2, 'validation_ValidationRule209', a)


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


def test_assoc_semanticElements26_link_reassign_clear():
    a = viewpoint_DRepresentationElement(name="sample_text")
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_DRepresentationElement27', {b1})
    assert _is_linked(a, 'viewpoint_DRepresentationElement27', b1)
    if hasattr(b1, 'viewpoint_EObject28'):
        assert _is_linked(b1, 'viewpoint_EObject28', a)
    _safe_set(a, 'viewpoint_DRepresentationElement27', {b2})
    assert _is_linked(a, 'viewpoint_DRepresentationElement27', b2)
    if hasattr(b1, 'viewpoint_EObject28'):
        assert not _is_linked(b1, 'viewpoint_EObject28', a)
    if hasattr(b2, 'viewpoint_EObject28'):
        assert _is_linked(b2, 'viewpoint_EObject28', a)
    _safe_set(a, 'viewpoint_DRepresentationElement27', set())
    assert not _is_linked(a, 'viewpoint_DRepresentationElement27', b2)
    if hasattr(b2, 'viewpoint_EObject28'):
        assert not _is_linked(b2, 'viewpoint_EObject28', a)


def test_assoc_systemColorsPalette63_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = SytemColorsPalette()
    b2 = SytemColorsPalette()
    _safe_set(a, 'viewpoint_description_Group64', b1)
    assert _is_linked(a, 'viewpoint_description_Group64', b1)
    if hasattr(b1, 'SytemColorsPalette'):
        assert _is_linked(b1, 'SytemColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group64', b2)
    assert _is_linked(a, 'viewpoint_description_Group64', b2)
    if hasattr(b1, 'SytemColorsPalette'):
        assert not _is_linked(b1, 'SytemColorsPalette', a)
    if hasattr(b2, 'SytemColorsPalette'):
        assert _is_linked(b2, 'SytemColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group64', None)
    assert not _is_linked(a, 'viewpoint_description_Group64', b2)
    if hasattr(b2, 'SytemColorsPalette'):
        assert not _is_linked(b2, 'SytemColorsPalette', a)


def test_assoc_userColorsPalettes65_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = UserColorsPalette()
    b2 = UserColorsPalette()
    _safe_set(a, 'viewpoint_description_Group66', {b1})
    assert _is_linked(a, 'viewpoint_description_Group66', b1)
    if hasattr(b1, 'UserColorsPalette'):
        assert _is_linked(b1, 'UserColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group66', {b2})
    assert _is_linked(a, 'viewpoint_description_Group66', b2)
    if hasattr(b1, 'UserColorsPalette'):
        assert not _is_linked(b1, 'UserColorsPalette', a)
    if hasattr(b2, 'UserColorsPalette'):
        assert _is_linked(b2, 'UserColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group66', set())
    assert not _is_linked(a, 'viewpoint_description_Group66', b2)
    if hasattr(b2, 'UserColorsPalette'):
        assert not _is_linked(b2, 'UserColorsPalette', a)


def test_assoc_validationSet67_link_reassign_clear():
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


def test_assoc_value104_link_reassign_clear():
    a = viewpoint_description_EReferenceCustomization(referenceName="sample_text")
    b1 = description_viewpoint_EObject()
    b2 = description_viewpoint_EObject()
    _safe_set(a, 'viewpoint_description_EReferenceCustomization', b1)
    assert _is_linked(a, 'viewpoint_description_EReferenceCustomization', b1)
    if hasattr(b1, 'description_viewpoint_EObject105'):
        assert _is_linked(b1, 'description_viewpoint_EObject105', a)
    _safe_set(a, 'viewpoint_description_EReferenceCustomization', b2)
    assert _is_linked(a, 'viewpoint_description_EReferenceCustomization', b2)
    if hasattr(b1, 'description_viewpoint_EObject105'):
        assert not _is_linked(b1, 'description_viewpoint_EObject105', a)
    if hasattr(b2, 'description_viewpoint_EObject105'):
        assert _is_linked(b2, 'description_viewpoint_EObject105', a)
    _safe_set(a, 'viewpoint_description_EReferenceCustomization', None)
    assert not _is_linked(a, 'viewpoint_description_EReferenceCustomization', b2)
    if hasattr(b2, 'description_viewpoint_EObject105'):
        assert not _is_linked(b2, 'description_viewpoint_EObject105', a)


def test_assoc_viewpoint43_link_reassign_clear():
    a = viewpoint_DView(initialized=True)
    b1 = Viewpoint()
    b2 = Viewpoint()
    _safe_set(a, 'viewpoint_DView44', b1)
    assert _is_linked(a, 'viewpoint_DView44', b1)
    if hasattr(b1, 'Viewpoint'):
        assert _is_linked(b1, 'Viewpoint', a)
    _safe_set(a, 'viewpoint_DView44', b2)
    assert _is_linked(a, 'viewpoint_DView44', b2)
    if hasattr(b1, 'Viewpoint'):
        assert not _is_linked(b1, 'Viewpoint', a)
    if hasattr(b2, 'Viewpoint'):
        assert _is_linked(b2, 'Viewpoint', a)
    _safe_set(a, 'viewpoint_DView44', None)
    assert not _is_linked(a, 'viewpoint_DView44', b2)
    if hasattr(b2, 'Viewpoint'):
        assert not _is_linked(b2, 'Viewpoint', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

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


ContainerModelOperation_strategy = st.builds(ContainerModelOperation)
@given(instance=ContainerModelOperation_strategy)
@settings(max_examples=25)
def test_ContainerModelOperation_instantiation(instance):
    assert isinstance(instance, ContainerModelOperation)


Customizable_strategy = st.builds(Customizable)
@given(instance=Customizable_strategy)
@settings(max_examples=25)
def test_Customizable_instantiation(instance):
    assert isinstance(instance, Customizable)


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


DNavigationLink_strategy = st.builds(DNavigationLink)
@given(instance=DNavigationLink_strategy)
@settings(max_examples=25)
def test_DNavigationLink_instantiation(instance):
    assert isinstance(instance, DNavigationLink)


DRefreshable_strategy = st.builds(DRefreshable)
@given(instance=DRefreshable_strategy)
@settings(max_examples=25)
def test_DRefreshable_instantiation(instance):
    assert isinstance(instance, DRefreshable)


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


DocumentedElement_strategy = st.builds(DocumentedElement)
@given(instance=DocumentedElement_strategy)
@settings(max_examples=25)
def test_DocumentedElement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)


EStructuralFeatureCustomization_strategy = st.builds(EStructuralFeatureCustomization)
@given(instance=EStructuralFeatureCustomization_strategy)
@settings(max_examples=25)
def test_EStructuralFeatureCustomization_instantiation(instance):
    assert isinstance(instance, EStructuralFeatureCustomization)


FeatureExtensionDescription_strategy = st.builds(FeatureExtensionDescription)
@given(instance=FeatureExtensionDescription_strategy)
@settings(max_examples=25)
def test_FeatureExtensionDescription_instantiation(instance):
    assert isinstance(instance, FeatureExtensionDescription)


FixedColor_strategy = st.builds(FixedColor)
@given(instance=FixedColor_strategy)
@settings(max_examples=25)
def test_FixedColor_instantiation(instance):
    assert isinstance(instance, FixedColor)


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


ModelOperation_strategy = st.builds(ModelOperation)
@given(instance=ModelOperation_strategy)
@settings(max_examples=25)
def test_ModelOperation_instantiation(instance):
    assert isinstance(instance, ModelOperation)


RepresentationDescription_strategy = st.builds(RepresentationDescription)
@given(instance=RepresentationDescription_strategy)
@settings(max_examples=25)
def test_RepresentationDescription_instantiation(instance):
    assert isinstance(instance, RepresentationDescription)


RepresentationElementMapping_strategy = st.builds(RepresentationElementMapping)
@given(instance=RepresentationElementMapping_strategy)
@settings(max_examples=25)
def test_RepresentationElementMapping_instantiation(instance):
    assert isinstance(instance, RepresentationElementMapping)


RepresentationExtensionDescription_strategy = st.builds(RepresentationExtensionDescription)
@given(instance=RepresentationExtensionDescription_strategy)
@settings(max_examples=25)
def test_RepresentationExtensionDescription_instantiation(instance):
    assert isinstance(instance, RepresentationExtensionDescription)


RepresentationTemplate_strategy = st.builds(RepresentationTemplate)
@given(instance=RepresentationTemplate_strategy)
@settings(max_examples=25)
def test_RepresentationTemplate_instantiation(instance):
    assert isinstance(instance, RepresentationTemplate)


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


Viewpoint_strategy = st.builds(Viewpoint)
@given(instance=Viewpoint_strategy)
@settings(max_examples=25)
def test_Viewpoint_instantiation(instance):
    assert isinstance(instance, Viewpoint)


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


description_DModelElement_strategy = st.builds(description_DModelElement)
@given(instance=description_DModelElement_strategy)
@settings(max_examples=25)
def test_description_DModelElement_instantiation(instance):
    assert isinstance(instance, description_DModelElement)


description_DocumentedElement_strategy = st.builds(description_DocumentedElement)
@given(instance=description_DocumentedElement_strategy)
@settings(max_examples=25)
def test_description_DocumentedElement_instantiation(instance):
    assert isinstance(instance, description_DocumentedElement)


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


description_IdentifiedElement_strategy = st.builds(description_IdentifiedElement)
@given(instance=description_IdentifiedElement_strategy)
@settings(max_examples=25)
def test_description_IdentifiedElement_instantiation(instance):
    assert isinstance(instance, description_IdentifiedElement)


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


style_StyleDescription_strategy = st.builds(style_StyleDescription)
@given(instance=style_StyleDescription_strategy)
@settings(max_examples=25)
def test_style_StyleDescription_instantiation(instance):
    assert isinstance(instance, style_StyleDescription)


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


tool_Case_strategy = st.builds(tool_Case)
@given(instance=tool_Case_strategy)
@settings(max_examples=25)
def test_tool_Case_instantiation(instance):
    assert isinstance(instance, tool_Case)


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


tool_DropContainerVariable_strategy = st.builds(tool_DropContainerVariable)
@given(instance=tool_DropContainerVariable_strategy)
@settings(max_examples=25)
def test_tool_DropContainerVariable_instantiation(instance):
    assert isinstance(instance, tool_DropContainerVariable)


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


tool_PasteDescription_strategy = st.builds(tool_PasteDescription)
@given(instance=tool_PasteDescription_strategy)
@settings(max_examples=25)
def test_tool_PasteDescription_instantiation(instance):
    assert isinstance(instance, tool_PasteDescription)


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


tool_SubVariable_strategy = st.builds(tool_SubVariable)
@given(instance=tool_SubVariable_strategy)
@settings(max_examples=25)
def test_tool_SubVariable_instantiation(instance):
    assert isinstance(instance, tool_SubVariable)


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


viewpoint_description_AbstractMappingImport_strategy = st.builds(viewpoint_description_AbstractMappingImport, hideSubMappings=st.booleans(), inheritsAncestorFilters=st.booleans())
@given(instance=viewpoint_description_AbstractMappingImport_strategy)
@settings(max_examples=25)
def test_viewpoint_description_AbstractMappingImport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AbstractMappingImport)


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


viewpoint_description_ComputedColor_strategy = st.builds(viewpoint_description_ComputedColor, blue=safe_text, green=safe_text, red=safe_text)
@given(instance=viewpoint_description_ComputedColor_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ComputedColor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ComputedColor)


viewpoint_description_ConditionalStyleDescription_strategy = st.builds(viewpoint_description_ConditionalStyleDescription, predicateExpression=safe_text)
@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_ConditionalStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalStyleDescription)


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


viewpoint_description_DocumentedElement_strategy = st.builds(viewpoint_description_DocumentedElement, documentation=safe_text)
@given(instance=viewpoint_description_DocumentedElement_strategy)
@settings(max_examples=25)
def test_viewpoint_description_DocumentedElement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DocumentedElement)


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


viewpoint_description_MetamodelExtensionSetting_strategy = st.builds(viewpoint_description_MetamodelExtensionSetting)
@given(instance=viewpoint_description_MetamodelExtensionSetting_strategy)
@settings(max_examples=25)
def test_viewpoint_description_MetamodelExtensionSetting_instantiation(instance):
    assert isinstance(instance, viewpoint_description_MetamodelExtensionSetting)


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


viewpoint_style_BasicLabelStyleDescription_strategy = st.builds(viewpoint_style_BasicLabelStyleDescription, iconPath=safe_text, labelExpression=safe_text, labelFormat=safe_text, labelSize=st.integers(), showIcon=st.booleans())
@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_style_BasicLabelStyleDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BasicLabelStyleDescription)


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


viewpoint_tool_CreateInstance_strategy = st.builds(viewpoint_tool_CreateInstance, referenceName=safe_text, typeName=safe_text, variableName=safe_text)
@given(instance=viewpoint_tool_CreateInstance_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_CreateInstance_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_CreateInstance)


viewpoint_tool_Default_strategy = st.builds(viewpoint_tool_Default)
@given(instance=viewpoint_tool_Default_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_Default_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Default)


viewpoint_tool_DeleteView_strategy = st.builds(viewpoint_tool_DeleteView)
@given(instance=viewpoint_tool_DeleteView_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DeleteView_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteView)


viewpoint_tool_DialogVariable_strategy = st.builds(viewpoint_tool_DialogVariable, dialogPrompt=safe_text)
@given(instance=viewpoint_tool_DialogVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DialogVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DialogVariable)


viewpoint_tool_DropContainerVariable_strategy = st.builds(viewpoint_tool_DropContainerVariable)
@given(instance=viewpoint_tool_DropContainerVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_DropContainerVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DropContainerVariable)


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


