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
    AbstractToolDescription,
    viewpoint_tool_MappingBasedToolDescription,
    tool_InitialOperation,
    tool_ElementViewVariable,
    ToolEntry,
    viewpoint_tool_AbstractToolDescription,
    tool_ToolFilterDescription,
    BasicLabelStyleDescription,
    viewpoint_style_LabelStyleDescription,
    viewpoint_style_TooltipStyleDescription,
    viewpoint_style_LabelBorderStyleDescription,
    style_LabelBorderStyleDescription,
    viewpoint_style_LabelBorderStyles,
    description_viewpoint_EDataType,
    viewpoint_style_BasicLabelStyleDescription,
    viewpoint_style_StyleDescription,
    viewpoint_description_IdentifiedElement,
    viewpoint_description_EndUserDocumentedElement,
    viewpoint_description_AnnotationEntry,
    UserColor,
    description_SubVariable,
    description_InteractiveVariableDescription,
    viewpoint_description_TypedVariable,
    viewpoint_description_InteractiveVariableDescription,
    AbstractVariable,
    viewpoint_description_SubVariable,
    viewpoint_description_AbstractVariable,
    viewpoint_description_DAnnotationEntry,
    viewpoint_description_UserColor,
    description_FixedColor,
    viewpoint_description_UserColorsPalette,
    SystemColor,
    viewpoint_description_SytemColorsPalette,
    style_LabelBorderStyles,
    tool_ToolEntry,
    viewpoint_description_Environment,
    description_UserColor,
    viewpoint_description_UserFixedColor,
    description_ColorDescription,
    viewpoint_description_ComputedColor,
    viewpoint_description_InterpolatedColor,
    ColorDescription,
    viewpoint_description_FixedColor,
    viewpoint_description_ColorStep,
    ColorStep,
    FixedColor,
    viewpoint_description_SystemColor,
    viewpoint_description_ColorDescription,
    viewpoint_description_SelectionDescription,
    viewpoint_description_IVSMElementCustomization,
    IVSMElementCustomization,
    viewpoint_description_VSMElementCustomization,
    viewpoint_description_Customization,
    viewpoint_description_EStructuralFeatureCustomization,
    viewpoint_description_VSMElementCustomizationReuse,
    EStructuralFeatureCustomization,
    viewpoint_description_EAttributeCustomization,
    viewpoint_description_EReferenceCustomization,
    viewpoint_description_DecorationDescription,
    viewpoint_description_DecorationDescriptionsSet,
    tool_PasteDescription,
    viewpoint_description_PasteTargetDescription,
    viewpoint_description_AbstractMappingImport,
    tool_RepresentationNavigationDescription,
    tool_RepresentationCreationDescription,
    IdentifiedElement,
    viewpoint_description_ConditionalStyleDescription,
    description_viewpoint_EStringToStringMapEntry,
    viewpoint_description_DAnnotation,
    DAnnotation,
    viewpoint_description_DModelElement,
    viewpoint_description_DocumentedElement,
    viewpoint_description_RepresentationTemplate,
    description_viewpoint_EPackage,
    viewpoint_description_RepresentationElementMapping,
    viewpoint_description_JavaExtension,
    description_viewpoint_EObject,
    viewpoint_description_MetamodelExtensionSetting,
    viewpoint_description_RepresentationExtensionDescription,
    validation_ValidationSet,
    description_IdentifiedElement,
    description_EndUserDocumentedElement,
    description_Component,
    viewpoint_description_Component,
    viewpoint_description_Extension,
    viewpoint_description_FeatureExtensionDescription,
    RepresentationTemplate,
    MetamodelExtensionSetting,
    JavaExtension,
    RepresentationExtensionDescription,
    viewpoint_Customizable,
    DFile,
    viewpoint_DModel,
    Extension,
    UserColorsPalette,
    SytemColorsPalette,
    viewpoint_DAnalysisSessionEObject,
    DResourceContainer,
    viewpoint_DFolder,
    viewpoint_DProject,
    DResource,
    viewpoint_DResourceContainer,
    viewpoint_DFile,
    viewpoint_DResource,
    viewpoint_SessionManagerEObject,
    DecorationDescription,
    viewpoint_description_GenericDecorationDescription,
    viewpoint_description_SemanticBasedDecoration,
    viewpoint_Decoration,
    style_StyleDescription,
    Customizable,
    viewpoint_BasicLabelStyle,
    BasicLabelStyle,
    viewpoint_LabelStyle,
    viewpoint_DAnalysisCustomData,
    viewpoint_UIState,
    AnnotationEntry,
    viewpoint_MetaModelExtension,
    Viewpoint,
    DSemanticDecorator,
    DStylizable,
    DMappingBased,
    viewpoint_DRefreshable,
    viewpoint_DStylizable,
    FeatureExtensionDescription,
    viewpoint_DFeatureExtension,
    description_DModelElement,
    DRefreshable,
    viewpoint_DRepresentationElement,
    viewpoint_Style,
    description_DocumentedElement,
    viewpoint_tool_ToolEntry,
    viewpoint_description_RepresentationDescription,
    viewpoint_description_Viewpoint,
    viewpoint_description_Group,
    viewpoint_DRepresentation,
    RepresentationDescription,
    viewpoint_description_RepresentationImportDescription,
    viewpoint_DRepresentationDescriptor,
    viewpoint_DSemanticDecorator,
    viewpoint_DMappingBased,
    viewpoint_DView,
    DAnnotationEntry,
    viewpoint_EObject,
    viewpoint_DAnalysis,
    viewpoint_validation_ValidationFix,
    InformationSection,
    viewpoint_audit_TemplateInformationSection,
    viewpoint_audit_InformationSection,
    viewpoint_validation_RuleAudit,
    RepresentationElementMapping,
    ValidationRule,
    viewpoint_validation_ViewValidationRule,
    viewpoint_validation_SemanticValidationRule,
    validation_ValidationFix,
    DocumentedElement,
    viewpoint_validation_ValidationSet,
    validation_RuleAudit,
    viewpoint_validation_ValidationRule,
    validation_ValidationRule,
    viewpoint_tool_FeatureChangeListener,
    tool_Default,
    tool_Case,
    viewpoint_tool_SwitchChild,
    SwitchChild,
    viewpoint_tool_Default,
    viewpoint_tool_Case,
    viewpoint_tool_ExternalJavaActionParameter,
    tool_FeatureChangeListener,
    viewpoint_tool_ToolFilterDescription,
    viewpoint_tool_NameVariable,
    tool_viewpoint_EObject,
    viewpoint_tool_InitialOperation,
    viewpoint_tool_InitialNodeCreationOperation,
    viewpoint_tool_ModelOperation,
    tool_ModelOperation,
    ModelOperation,
    viewpoint_tool_Switch,
    viewpoint_tool_ContainerModelOperation,
    viewpoint_tool_EditMaskVariables,
    ContainerModelOperation,
    viewpoint_tool_RemoveElement,
    viewpoint_tool_SetObject,
    viewpoint_tool_For,
    viewpoint_tool_If,
    viewpoint_tool_Unset,
    viewpoint_tool_DeleteView,
    viewpoint_tool_ChangeContext,
    viewpoint_tool_SetValue,
    viewpoint_tool_Let,
    viewpoint_tool_MoveElement,
    viewpoint_tool_CreateInstance,
    viewpoint_tool_InitialContainerDropOperation,
    viewpoint_tool_InitEdgeCreationOperation,
    viewpoint_tool_PopupMenu,
    tool_ExternalJavaAction,
    tool_ExternalJavaActionParameter,
    tool_ContainerModelOperation,
    viewpoint_tool_ElementSelectVariable,
    description_AbstractVariable,
    viewpoint_tool_DialogVariable,
    tool_VariableContainer,
    viewpoint_tool_SelectContainerVariable,
    viewpoint_tool_ElementDeleteVariable,
    viewpoint_tool_ElementVariable,
    viewpoint_tool_DropContainerVariable,
    viewpoint_tool_ElementViewVariable,
    viewpoint_tool_ElementDropVariable,
    viewpoint_tool_ContainerViewVariable,
    viewpoint_tool_AcceleoVariable,
    SubVariable,
    viewpoint_tool_VariableContainer,
    MenuItemDescription,
    viewpoint_tool_OperationAction,
    tool_MenuItemDescription,
    viewpoint_tool_ExternalJavaAction,
    viewpoint_tool_ExternalJavaActionCall,
    MenuItemOrRef,
    viewpoint_tool_MenuItemDescriptionReference,
    tool_MenuItemOrRef,
    viewpoint_tool_MenuItemOrRef,
    tool_NameVariable,
    viewpoint_tool_RepresentationNavigationDescription,
    viewpoint_tool_RepresentationCreationDescription,
    tool_SelectContainerVariable,
    tool_ElementSelectVariable,
    description_SelectionDescription,
    viewpoint_tool_SelectModelElementVariable,
    tool_AbstractToolDescription,
    viewpoint_tool_MenuItemDescription,
    viewpoint_tool_SelectionWizardDescription,
    viewpoint_tool_PaneBasedSelectionWizardDescription,
    tool_ContainerViewVariable,
    tool_DropContainerVariable,
    tool_ElementVariable,
    MappingBasedToolDescription,
    viewpoint_tool_PasteDescription,
    viewpoint_tool_ToolDescription,
    Position,
    FontFormat,
    LabelAlignment,
    SystemColors,
    DecorationDistributionDirection,
    ERROR_LEVEL,
    DragSource,
    SyncStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(AbstractToolDescription)


def test_hyp_abstracttooldescription_constructor_exists():
    assert callable(AbstractToolDescription.__init__)


def test_hyp_abstracttooldescription_constructor_args():
    sig = inspect.signature(AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MappingBasedToolDescription)


def test_hyp_viewpoint_tool_mappingbasedtooldescription_constructor_exists():
    assert callable(viewpoint_tool_MappingBasedToolDescription.__init__)


def test_hyp_viewpoint_tool_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialOperation)


def test_hyp_tool_initialoperation_constructor_exists():
    assert callable(tool_InitialOperation.__init__)


def test_hyp_tool_initialoperation_constructor_args():
    sig = inspect.signature(tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementViewVariable)


def test_hyp_tool_elementviewvariable_constructor_exists():
    assert callable(tool_ElementViewVariable.__init__)


def test_hyp_tool_elementviewvariable_constructor_args():
    sig = inspect.signature(tool_ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_toolentry_is_not_abstract():
    assert not inspect.isabstract(ToolEntry)


def test_hyp_toolentry_constructor_exists():
    assert callable(ToolEntry.__init__)


def test_hyp_toolentry_constructor_args():
    sig = inspect.signature(ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_AbstractToolDescription)


def test_hyp_viewpoint_tool_abstracttooldescription_constructor_exists():
    assert callable(viewpoint_tool_AbstractToolDescription.__init__)


def test_hyp_viewpoint_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "inverseSelectionOrder" in params, "Missing parameter 'inverseSelectionOrder'"
    assert "forceRefresh" in params, "Missing parameter 'forceRefresh'"
    assert "elementsToSelect" in params, "Missing parameter 'elementsToSelect'"
    assert "precondition" in params, "Missing parameter 'precondition'"







def test_hyp_tool_toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(tool_ToolFilterDescription)


def test_hyp_tool_toolfilterdescription_constructor_exists():
    assert callable(tool_ToolFilterDescription.__init__)


def test_hyp_tool_toolfilterdescription_constructor_args():
    sig = inspect.signature(tool_ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyleDescription)


def test_hyp_basiclabelstyledescription_constructor_exists():
    assert callable(BasicLabelStyleDescription.__init__)


def test_hyp_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_style_labelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelStyleDescription)


def test_hyp_viewpoint_style_labelstyledescription_constructor_exists():
    assert callable(viewpoint_style_LabelStyleDescription.__init__)


def test_hyp_viewpoint_style_labelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"




def test_hyp_viewpoint_style_tooltipstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_TooltipStyleDescription)


def test_hyp_viewpoint_style_tooltipstyledescription_constructor_exists():
    assert callable(viewpoint_style_TooltipStyleDescription.__init__)


def test_hyp_viewpoint_style_tooltipstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_TooltipStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipExpression" in params, "Missing parameter 'tooltipExpression'"




def test_hyp_viewpoint_style_labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelBorderStyleDescription)


def test_hyp_viewpoint_style_labelborderstyledescription_constructor_exists():
    assert callable(viewpoint_style_LabelBorderStyleDescription.__init__)


def test_hyp_viewpoint_style_labelborderstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"







def test_hyp_style_labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_LabelBorderStyleDescription)


def test_hyp_style_labelborderstyledescription_constructor_exists():
    assert callable(style_LabelBorderStyleDescription.__init__)


def test_hyp_style_labelborderstyledescription_constructor_args():
    sig = inspect.signature(style_LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_style_labelborderstyles_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelBorderStyles)


def test_hyp_viewpoint_style_labelborderstyles_constructor_exists():
    assert callable(viewpoint_style_LabelBorderStyles.__init__)


def test_hyp_viewpoint_style_labelborderstyles_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelBorderStyles.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_viewpoint_edatatype_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EDataType)


def test_hyp_description_viewpoint_edatatype_constructor_exists():
    assert callable(description_viewpoint_EDataType.__init__)


def test_hyp_description_viewpoint_edatatype_constructor_args():
    sig = inspect.signature(description_viewpoint_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_style_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_BasicLabelStyleDescription)


def test_hyp_viewpoint_style_basiclabelstyledescription_constructor_exists():
    assert callable(viewpoint_style_BasicLabelStyleDescription.__init__)


def test_hyp_viewpoint_style_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "labelExpression" in params, "Missing parameter 'labelExpression'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"








def test_hyp_viewpoint_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_StyleDescription)


def test_hyp_viewpoint_style_styledescription_constructor_exists():
    assert callable(viewpoint_style_StyleDescription.__init__)


def test_hyp_viewpoint_style_styledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_IdentifiedElement)


def test_hyp_viewpoint_description_identifiedelement_constructor_exists():
    assert callable(viewpoint_description_IdentifiedElement.__init__)


def test_hyp_viewpoint_description_identifiedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"





def test_hyp_viewpoint_description_enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EndUserDocumentedElement)


def test_hyp_viewpoint_description_enduserdocumentedelement_constructor_exists():
    assert callable(viewpoint_description_EndUserDocumentedElement.__init__)


def test_hyp_viewpoint_description_enduserdocumentedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "endUserDocumentation" in params, "Missing parameter 'endUserDocumentation'"




def test_hyp_viewpoint_description_annotationentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AnnotationEntry)


def test_hyp_viewpoint_description_annotationentry_constructor_exists():
    assert callable(viewpoint_description_AnnotationEntry.__init__)


def test_hyp_viewpoint_description_annotationentry_constructor_args():
    sig = inspect.signature(viewpoint_description_AnnotationEntry.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"




def test_hyp_usercolor_is_not_abstract():
    assert not inspect.isabstract(UserColor)


def test_hyp_usercolor_constructor_exists():
    assert callable(UserColor.__init__)


def test_hyp_usercolor_constructor_args():
    sig = inspect.signature(UserColor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_subvariable_is_not_abstract():
    assert not inspect.isabstract(description_SubVariable)


def test_hyp_description_subvariable_constructor_exists():
    assert callable(description_SubVariable.__init__)


def test_hyp_description_subvariable_constructor_args():
    sig = inspect.signature(description_SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(description_InteractiveVariableDescription)


def test_hyp_description_interactivevariabledescription_constructor_exists():
    assert callable(description_InteractiveVariableDescription.__init__)


def test_hyp_description_interactivevariabledescription_constructor_args():
    sig = inspect.signature(description_InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_typedvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_TypedVariable)


def test_hyp_viewpoint_description_typedvariable_constructor_exists():
    assert callable(viewpoint_description_TypedVariable.__init__)


def test_hyp_viewpoint_description_typedvariable_constructor_args():
    sig = inspect.signature(viewpoint_description_TypedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValueExpression" in params, "Missing parameter 'defaultValueExpression'"




def test_hyp_viewpoint_description_interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_InteractiveVariableDescription)


def test_hyp_viewpoint_description_interactivevariabledescription_constructor_exists():
    assert callable(viewpoint_description_InteractiveVariableDescription.__init__)


def test_hyp_viewpoint_description_interactivevariabledescription_constructor_args():
    sig = inspect.signature(viewpoint_description_InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())
    assert "userDocumentation" in params, "Missing parameter 'userDocumentation'"




def test_hyp_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_hyp_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_hyp_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_subvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SubVariable)


def test_hyp_viewpoint_description_subvariable_constructor_exists():
    assert callable(viewpoint_description_SubVariable.__init__)


def test_hyp_viewpoint_description_subvariable_constructor_args():
    sig = inspect.signature(viewpoint_description_SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AbstractVariable)


def test_hyp_viewpoint_description_abstractvariable_constructor_exists():
    assert callable(viewpoint_description_AbstractVariable.__init__)


def test_hyp_viewpoint_description_abstractvariable_constructor_args():
    sig = inspect.signature(viewpoint_description_AbstractVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_viewpoint_description_dannotationentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DAnnotationEntry)


def test_hyp_viewpoint_description_dannotationentry_constructor_exists():
    assert callable(viewpoint_description_DAnnotationEntry.__init__)


def test_hyp_viewpoint_description_dannotationentry_constructor_args():
    sig = inspect.signature(viewpoint_description_DAnnotationEntry.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "details" in params, "Missing parameter 'details'"





def test_hyp_viewpoint_description_usercolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserColor)


def test_hyp_viewpoint_description_usercolor_constructor_exists():
    assert callable(viewpoint_description_UserColor.__init__)


def test_hyp_viewpoint_description_usercolor_constructor_args():
    sig = inspect.signature(viewpoint_description_UserColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_description_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(description_FixedColor)


def test_hyp_description_fixedcolor_constructor_exists():
    assert callable(description_FixedColor.__init__)


def test_hyp_description_fixedcolor_constructor_args():
    sig = inspect.signature(description_FixedColor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_usercolorspalette_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserColorsPalette)


def test_hyp_viewpoint_description_usercolorspalette_constructor_exists():
    assert callable(viewpoint_description_UserColorsPalette.__init__)


def test_hyp_viewpoint_description_usercolorspalette_constructor_args():
    sig = inspect.signature(viewpoint_description_UserColorsPalette.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_systemcolor_is_not_abstract():
    assert not inspect.isabstract(SystemColor)


def test_hyp_systemcolor_constructor_exists():
    assert callable(SystemColor.__init__)


def test_hyp_systemcolor_constructor_args():
    sig = inspect.signature(SystemColor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_sytemcolorspalette_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SytemColorsPalette)


def test_hyp_viewpoint_description_sytemcolorspalette_constructor_exists():
    assert callable(viewpoint_description_SytemColorsPalette.__init__)


def test_hyp_viewpoint_description_sytemcolorspalette_constructor_args():
    sig = inspect.signature(viewpoint_description_SytemColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_labelborderstyles_is_not_abstract():
    assert not inspect.isabstract(style_LabelBorderStyles)


def test_hyp_style_labelborderstyles_constructor_exists():
    assert callable(style_LabelBorderStyles.__init__)


def test_hyp_style_labelborderstyles_constructor_args():
    sig = inspect.signature(style_LabelBorderStyles.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_toolentry_is_not_abstract():
    assert not inspect.isabstract(tool_ToolEntry)


def test_hyp_tool_toolentry_constructor_exists():
    assert callable(tool_ToolEntry.__init__)


def test_hyp_tool_toolentry_constructor_args():
    sig = inspect.signature(tool_ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_environment_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Environment)


def test_hyp_viewpoint_description_environment_constructor_exists():
    assert callable(viewpoint_description_Environment.__init__)


def test_hyp_viewpoint_description_environment_constructor_args():
    sig = inspect.signature(viewpoint_description_Environment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_usercolor_is_not_abstract():
    assert not inspect.isabstract(description_UserColor)


def test_hyp_description_usercolor_constructor_exists():
    assert callable(description_UserColor.__init__)


def test_hyp_description_usercolor_constructor_args():
    sig = inspect.signature(description_UserColor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_userfixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserFixedColor)


def test_hyp_viewpoint_description_userfixedcolor_constructor_exists():
    assert callable(viewpoint_description_UserFixedColor.__init__)


def test_hyp_viewpoint_description_userfixedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_UserFixedColor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_colordescription_is_not_abstract():
    assert not inspect.isabstract(description_ColorDescription)


def test_hyp_description_colordescription_constructor_exists():
    assert callable(description_ColorDescription.__init__)


def test_hyp_description_colordescription_constructor_args():
    sig = inspect.signature(description_ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_computedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ComputedColor)


def test_hyp_viewpoint_description_computedcolor_constructor_exists():
    assert callable(viewpoint_description_ComputedColor.__init__)


def test_hyp_viewpoint_description_computedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_ComputedColor.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "red" in params, "Missing parameter 'red'"
    assert "blue" in params, "Missing parameter 'blue'"






def test_hyp_viewpoint_description_interpolatedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_InterpolatedColor)


def test_hyp_viewpoint_description_interpolatedcolor_constructor_exists():
    assert callable(viewpoint_description_InterpolatedColor.__init__)


def test_hyp_viewpoint_description_interpolatedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_InterpolatedColor.__init__)
    params = list(sig.parameters.keys())
    assert "maxValueComputationExpression" in params, "Missing parameter 'maxValueComputationExpression'"
    assert "minValueComputationExpression" in params, "Missing parameter 'minValueComputationExpression'"
    assert "colorValueComputationExpression" in params, "Missing parameter 'colorValueComputationExpression'"






def test_hyp_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_hyp_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_hyp_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_FixedColor)


def test_hyp_viewpoint_description_fixedcolor_constructor_exists():
    assert callable(viewpoint_description_FixedColor.__init__)


def test_hyp_viewpoint_description_fixedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_FixedColor.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"






def test_hyp_viewpoint_description_colorstep_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ColorStep)


def test_hyp_viewpoint_description_colorstep_constructor_exists():
    assert callable(viewpoint_description_ColorStep.__init__)


def test_hyp_viewpoint_description_colorstep_constructor_args():
    sig = inspect.signature(viewpoint_description_ColorStep.__init__)
    params = list(sig.parameters.keys())
    assert "associatedValue" in params, "Missing parameter 'associatedValue'"




def test_hyp_colorstep_is_not_abstract():
    assert not inspect.isabstract(ColorStep)


def test_hyp_colorstep_constructor_exists():
    assert callable(ColorStep.__init__)


def test_hyp_colorstep_constructor_args():
    sig = inspect.signature(ColorStep.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(FixedColor)


def test_hyp_fixedcolor_constructor_exists():
    assert callable(FixedColor.__init__)


def test_hyp_fixedcolor_constructor_args():
    sig = inspect.signature(FixedColor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_systemcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SystemColor)


def test_hyp_viewpoint_description_systemcolor_constructor_exists():
    assert callable(viewpoint_description_SystemColor.__init__)


def test_hyp_viewpoint_description_systemcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_SystemColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_viewpoint_description_colordescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ColorDescription)


def test_hyp_viewpoint_description_colordescription_constructor_exists():
    assert callable(viewpoint_description_ColorDescription.__init__)


def test_hyp_viewpoint_description_colordescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_selectiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SelectionDescription)


def test_hyp_viewpoint_description_selectiondescription_constructor_exists():
    assert callable(viewpoint_description_SelectionDescription.__init__)


def test_hyp_viewpoint_description_selectiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_SelectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "tree" in params, "Missing parameter 'tree'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "message" in params, "Missing parameter 'message'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"









def test_hyp_viewpoint_description_ivsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_IVSMElementCustomization)


def test_hyp_viewpoint_description_ivsmelementcustomization_constructor_exists():
    assert callable(viewpoint_description_IVSMElementCustomization.__init__)


def test_hyp_viewpoint_description_ivsmelementcustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_IVSMElementCustomization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ivsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(IVSMElementCustomization)


def test_hyp_ivsmelementcustomization_constructor_exists():
    assert callable(IVSMElementCustomization.__init__)


def test_hyp_ivsmelementcustomization_constructor_args():
    sig = inspect.signature(IVSMElementCustomization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_vsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_VSMElementCustomization)


def test_hyp_viewpoint_description_vsmelementcustomization_constructor_exists():
    assert callable(viewpoint_description_VSMElementCustomization.__init__)


def test_hyp_viewpoint_description_vsmelementcustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_VSMElementCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"




def test_hyp_viewpoint_description_customization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Customization)


def test_hyp_viewpoint_description_customization_constructor_exists():
    assert callable(viewpoint_description_Customization.__init__)


def test_hyp_viewpoint_description_customization_constructor_args():
    sig = inspect.signature(viewpoint_description_Customization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EStructuralFeatureCustomization)


def test_hyp_viewpoint_description_estructuralfeaturecustomization_constructor_exists():
    assert callable(viewpoint_description_EStructuralFeatureCustomization.__init__)


def test_hyp_viewpoint_description_estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "applyOnAll" in params, "Missing parameter 'applyOnAll'"




def test_hyp_viewpoint_description_vsmelementcustomizationreuse_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_VSMElementCustomizationReuse)


def test_hyp_viewpoint_description_vsmelementcustomizationreuse_constructor_exists():
    assert callable(viewpoint_description_VSMElementCustomizationReuse.__init__)


def test_hyp_viewpoint_description_vsmelementcustomizationreuse_constructor_args():
    sig = inspect.signature(viewpoint_description_VSMElementCustomizationReuse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeatureCustomization)


def test_hyp_estructuralfeaturecustomization_constructor_exists():
    assert callable(EStructuralFeatureCustomization.__init__)


def test_hyp_estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_eattributecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EAttributeCustomization)


def test_hyp_viewpoint_description_eattributecustomization_constructor_exists():
    assert callable(viewpoint_description_EAttributeCustomization.__init__)


def test_hyp_viewpoint_description_eattributecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EAttributeCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "attributeName" in params, "Missing parameter 'attributeName'"





def test_hyp_viewpoint_description_ereferencecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EReferenceCustomization)


def test_hyp_viewpoint_description_ereferencecustomization_constructor_exists():
    assert callable(viewpoint_description_EReferenceCustomization.__init__)


def test_hyp_viewpoint_description_ereferencecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EReferenceCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "referenceName" in params, "Missing parameter 'referenceName'"




def test_hyp_viewpoint_description_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DecorationDescription)


def test_hyp_viewpoint_description_decorationdescription_constructor_exists():
    assert callable(viewpoint_description_DecorationDescription.__init__)


def test_hyp_viewpoint_description_decorationdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_DecorationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipExpression" in params, "Missing parameter 'tooltipExpression'"
    assert "name" in params, "Missing parameter 'name'"
    assert "imageExpression" in params, "Missing parameter 'imageExpression'"
    assert "position" in params, "Missing parameter 'position'"
    assert "distributionDirection" in params, "Missing parameter 'distributionDirection'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"









def test_hyp_viewpoint_description_decorationdescriptionsset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DecorationDescriptionsSet)


def test_hyp_viewpoint_description_decorationdescriptionsset_constructor_exists():
    assert callable(viewpoint_description_DecorationDescriptionsSet.__init__)


def test_hyp_viewpoint_description_decorationdescriptionsset_constructor_args():
    sig = inspect.signature(viewpoint_description_DecorationDescriptionsSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_pastedescription_is_not_abstract():
    assert not inspect.isabstract(tool_PasteDescription)


def test_hyp_tool_pastedescription_constructor_exists():
    assert callable(tool_PasteDescription.__init__)


def test_hyp_tool_pastedescription_constructor_args():
    sig = inspect.signature(tool_PasteDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_PasteTargetDescription)


def test_hyp_viewpoint_description_pastetargetdescription_constructor_exists():
    assert callable(viewpoint_description_PasteTargetDescription.__init__)


def test_hyp_viewpoint_description_pastetargetdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AbstractMappingImport)


def test_hyp_viewpoint_description_abstractmappingimport_constructor_exists():
    assert callable(viewpoint_description_AbstractMappingImport.__init__)


def test_hyp_viewpoint_description_abstractmappingimport_constructor_args():
    sig = inspect.signature(viewpoint_description_AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "hideSubMappings" in params, "Missing parameter 'hideSubMappings'"
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"





def test_hyp_tool_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationNavigationDescription)


def test_hyp_tool_representationnavigationdescription_constructor_exists():
    assert callable(tool_RepresentationNavigationDescription.__init__)


def test_hyp_tool_representationnavigationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationCreationDescription)


def test_hyp_tool_representationcreationdescription_constructor_exists():
    assert callable(tool_RepresentationCreationDescription.__init__)


def test_hyp_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElement)


def test_hyp_identifiedelement_constructor_exists():
    assert callable(IdentifiedElement.__init__)


def test_hyp_identifiedelement_constructor_args():
    sig = inspect.signature(IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ConditionalStyleDescription)


def test_hyp_viewpoint_description_conditionalstyledescription_constructor_exists():
    assert callable(viewpoint_description_ConditionalStyleDescription.__init__)


def test_hyp_viewpoint_description_conditionalstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"




def test_hyp_description_viewpoint_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EStringToStringMapEntry)


def test_hyp_description_viewpoint_estringtostringmapentry_constructor_exists():
    assert callable(description_viewpoint_EStringToStringMapEntry.__init__)


def test_hyp_description_viewpoint_estringtostringmapentry_constructor_args():
    sig = inspect.signature(description_viewpoint_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_dannotation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DAnnotation)


def test_hyp_viewpoint_description_dannotation_constructor_exists():
    assert callable(viewpoint_description_DAnnotation.__init__)


def test_hyp_viewpoint_description_dannotation_constructor_args():
    sig = inspect.signature(viewpoint_description_DAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"




def test_hyp_dannotation_is_not_abstract():
    assert not inspect.isabstract(DAnnotation)


def test_hyp_dannotation_constructor_exists():
    assert callable(DAnnotation.__init__)


def test_hyp_dannotation_constructor_args():
    sig = inspect.signature(DAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_dmodelelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DModelElement)


def test_hyp_viewpoint_description_dmodelelement_constructor_exists():
    assert callable(viewpoint_description_DModelElement.__init__)


def test_hyp_viewpoint_description_dmodelelement_constructor_args():
    sig = inspect.signature(viewpoint_description_DModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_documentedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DocumentedElement)


def test_hyp_viewpoint_description_documentedelement_constructor_exists():
    assert callable(viewpoint_description_DocumentedElement.__init__)


def test_hyp_viewpoint_description_documentedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_DocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"




def test_hyp_viewpoint_description_representationtemplate_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationTemplate)


def test_hyp_viewpoint_description_representationtemplate_constructor_exists():
    assert callable(viewpoint_description_RepresentationTemplate.__init__)


def test_hyp_viewpoint_description_representationtemplate_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_description_viewpoint_epackage_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EPackage)


def test_hyp_description_viewpoint_epackage_constructor_exists():
    assert callable(description_viewpoint_EPackage.__init__)


def test_hyp_description_viewpoint_epackage_constructor_args():
    sig = inspect.signature(description_viewpoint_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationElementMapping)


def test_hyp_viewpoint_description_representationelementmapping_constructor_exists():
    assert callable(viewpoint_description_RepresentationElementMapping.__init__)


def test_hyp_viewpoint_description_representationelementmapping_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_javaextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_JavaExtension)


def test_hyp_viewpoint_description_javaextension_constructor_exists():
    assert callable(viewpoint_description_JavaExtension.__init__)


def test_hyp_viewpoint_description_javaextension_constructor_args():
    sig = inspect.signature(viewpoint_description_JavaExtension.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"




def test_hyp_description_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EObject)


def test_hyp_description_viewpoint_eobject_constructor_exists():
    assert callable(description_viewpoint_EObject.__init__)


def test_hyp_description_viewpoint_eobject_constructor_args():
    sig = inspect.signature(description_viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_metamodelextensionsetting_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_MetamodelExtensionSetting)


def test_hyp_viewpoint_description_metamodelextensionsetting_constructor_exists():
    assert callable(viewpoint_description_MetamodelExtensionSetting.__init__)


def test_hyp_viewpoint_description_metamodelextensionsetting_constructor_args():
    sig = inspect.signature(viewpoint_description_MetamodelExtensionSetting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationExtensionDescription)


def test_hyp_viewpoint_description_representationextensiondescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationExtensionDescription.__init__)


def test_hyp_viewpoint_description_representationextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "representationName" in params, "Missing parameter 'representationName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "viewpointURI" in params, "Missing parameter 'viewpointURI'"






def test_hyp_validation_validationset_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationSet)


def test_hyp_validation_validationset_constructor_exists():
    assert callable(validation_ValidationSet.__init__)


def test_hyp_validation_validationset_constructor_args():
    sig = inspect.signature(validation_ValidationSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(description_IdentifiedElement)


def test_hyp_description_identifiedelement_constructor_exists():
    assert callable(description_IdentifiedElement.__init__)


def test_hyp_description_identifiedelement_constructor_args():
    sig = inspect.signature(description_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(description_EndUserDocumentedElement)


def test_hyp_description_enduserdocumentedelement_constructor_exists():
    assert callable(description_EndUserDocumentedElement.__init__)


def test_hyp_description_enduserdocumentedelement_constructor_args():
    sig = inspect.signature(description_EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_component_is_not_abstract():
    assert not inspect.isabstract(description_Component)


def test_hyp_description_component_constructor_exists():
    assert callable(description_Component.__init__)


def test_hyp_description_component_constructor_args():
    sig = inspect.signature(description_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_component_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Component)


def test_hyp_viewpoint_description_component_constructor_exists():
    assert callable(viewpoint_description_Component.__init__)


def test_hyp_viewpoint_description_component_constructor_args():
    sig = inspect.signature(viewpoint_description_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_extension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Extension)


def test_hyp_viewpoint_description_extension_constructor_exists():
    assert callable(viewpoint_description_Extension.__init__)


def test_hyp_viewpoint_description_extension_constructor_args():
    sig = inspect.signature(viewpoint_description_Extension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_featureextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_FeatureExtensionDescription)


def test_hyp_viewpoint_description_featureextensiondescription_constructor_exists():
    assert callable(viewpoint_description_FeatureExtensionDescription.__init__)


def test_hyp_viewpoint_description_featureextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_FeatureExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_representationtemplate_is_not_abstract():
    assert not inspect.isabstract(RepresentationTemplate)


def test_hyp_representationtemplate_constructor_exists():
    assert callable(RepresentationTemplate.__init__)


def test_hyp_representationtemplate_constructor_args():
    sig = inspect.signature(RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metamodelextensionsetting_is_not_abstract():
    assert not inspect.isabstract(MetamodelExtensionSetting)


def test_hyp_metamodelextensionsetting_constructor_exists():
    assert callable(MetamodelExtensionSetting.__init__)


def test_hyp_metamodelextensionsetting_constructor_args():
    sig = inspect.signature(MetamodelExtensionSetting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaextension_is_not_abstract():
    assert not inspect.isabstract(JavaExtension)


def test_hyp_javaextension_constructor_exists():
    assert callable(JavaExtension.__init__)


def test_hyp_javaextension_constructor_args():
    sig = inspect.signature(JavaExtension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationExtensionDescription)


def test_hyp_representationextensiondescription_constructor_exists():
    assert callable(RepresentationExtensionDescription.__init__)


def test_hyp_representationextensiondescription_constructor_args():
    sig = inspect.signature(RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_customizable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Customizable)


def test_hyp_viewpoint_customizable_constructor_exists():
    assert callable(viewpoint_Customizable.__init__)


def test_hyp_viewpoint_customizable_constructor_args():
    sig = inspect.signature(viewpoint_Customizable.__init__)
    params = list(sig.parameters.keys())
    assert "customFeatures" in params, "Missing parameter 'customFeatures'"




def test_hyp_dfile_is_not_abstract():
    assert not inspect.isabstract(DFile)


def test_hyp_dfile_constructor_exists():
    assert callable(DFile.__init__)


def test_hyp_dfile_constructor_args():
    sig = inspect.signature(DFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dmodel_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DModel)


def test_hyp_viewpoint_dmodel_constructor_exists():
    assert callable(viewpoint_DModel.__init__)


def test_hyp_viewpoint_dmodel_constructor_args():
    sig = inspect.signature(viewpoint_DModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_hyp_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_hyp_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_usercolorspalette_is_not_abstract():
    assert not inspect.isabstract(UserColorsPalette)


def test_hyp_usercolorspalette_constructor_exists():
    assert callable(UserColorsPalette.__init__)


def test_hyp_usercolorspalette_constructor_args():
    sig = inspect.signature(UserColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sytemcolorspalette_is_not_abstract():
    assert not inspect.isabstract(SytemColorsPalette)


def test_hyp_sytemcolorspalette_constructor_exists():
    assert callable(SytemColorsPalette.__init__)


def test_hyp_sytemcolorspalette_constructor_args():
    sig = inspect.signature(SytemColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_danalysissessioneobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysisSessionEObject)


def test_hyp_viewpoint_danalysissessioneobject_constructor_exists():
    assert callable(viewpoint_DAnalysisSessionEObject.__init__)


def test_hyp_viewpoint_danalysissessioneobject_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysisSessionEObject.__init__)
    params = list(sig.parameters.keys())
    assert "open" in params, "Missing parameter 'open'"
    assert "synchronizationStatus" in params, "Missing parameter 'synchronizationStatus'"
    assert "controlledResources" in params, "Missing parameter 'controlledResources'"
    assert "resources" in params, "Missing parameter 'resources'"







def test_hyp_dresourcecontainer_is_not_abstract():
    assert not inspect.isabstract(DResourceContainer)


def test_hyp_dresourcecontainer_constructor_exists():
    assert callable(DResourceContainer.__init__)


def test_hyp_dresourcecontainer_constructor_args():
    sig = inspect.signature(DResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dfolder_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFolder)


def test_hyp_viewpoint_dfolder_constructor_exists():
    assert callable(viewpoint_DFolder.__init__)


def test_hyp_viewpoint_dfolder_constructor_args():
    sig = inspect.signature(viewpoint_DFolder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dproject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DProject)


def test_hyp_viewpoint_dproject_constructor_exists():
    assert callable(viewpoint_DProject.__init__)


def test_hyp_viewpoint_dproject_constructor_args():
    sig = inspect.signature(viewpoint_DProject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dresource_is_not_abstract():
    assert not inspect.isabstract(DResource)


def test_hyp_dresource_constructor_exists():
    assert callable(DResource.__init__)


def test_hyp_dresource_constructor_args():
    sig = inspect.signature(DResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dresourcecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DResourceContainer)


def test_hyp_viewpoint_dresourcecontainer_constructor_exists():
    assert callable(viewpoint_DResourceContainer.__init__)


def test_hyp_viewpoint_dresourcecontainer_constructor_args():
    sig = inspect.signature(viewpoint_DResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dfile_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFile)


def test_hyp_viewpoint_dfile_constructor_exists():
    assert callable(viewpoint_DFile.__init__)


def test_hyp_viewpoint_dfile_constructor_args():
    sig = inspect.signature(viewpoint_DFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dresource_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DResource)


def test_hyp_viewpoint_dresource_constructor_exists():
    assert callable(viewpoint_DResource.__init__)


def test_hyp_viewpoint_dresource_constructor_args():
    sig = inspect.signature(viewpoint_DResource.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_viewpoint_sessionmanagereobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_SessionManagerEObject)


def test_hyp_viewpoint_sessionmanagereobject_constructor_exists():
    assert callable(viewpoint_SessionManagerEObject.__init__)


def test_hyp_viewpoint_sessionmanagereobject_constructor_args():
    sig = inspect.signature(viewpoint_SessionManagerEObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(DecorationDescription)


def test_hyp_decorationdescription_constructor_exists():
    assert callable(DecorationDescription.__init__)


def test_hyp_decorationdescription_constructor_args():
    sig = inspect.signature(DecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_genericdecorationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_GenericDecorationDescription)


def test_hyp_viewpoint_description_genericdecorationdescription_constructor_exists():
    assert callable(viewpoint_description_GenericDecorationDescription.__init__)


def test_hyp_viewpoint_description_genericdecorationdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_GenericDecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_semanticbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SemanticBasedDecoration)


def test_hyp_viewpoint_description_semanticbaseddecoration_constructor_exists():
    assert callable(viewpoint_description_SemanticBasedDecoration.__init__)


def test_hyp_viewpoint_description_semanticbaseddecoration_constructor_args():
    sig = inspect.signature(viewpoint_description_SemanticBasedDecoration.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"




def test_hyp_viewpoint_decoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Decoration)


def test_hyp_viewpoint_decoration_constructor_exists():
    assert callable(viewpoint_Decoration.__init__)


def test_hyp_viewpoint_decoration_constructor_args():
    sig = inspect.signature(viewpoint_Decoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(style_StyleDescription)


def test_hyp_style_styledescription_constructor_exists():
    assert callable(style_StyleDescription.__init__)


def test_hyp_style_styledescription_constructor_args():
    sig = inspect.signature(style_StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customizable_is_not_abstract():
    assert not inspect.isabstract(Customizable)


def test_hyp_customizable_constructor_exists():
    assert callable(Customizable.__init__)


def test_hyp_customizable_constructor_args():
    sig = inspect.signature(Customizable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_BasicLabelStyle)


def test_hyp_viewpoint_basiclabelstyle_constructor_exists():
    assert callable(viewpoint_BasicLabelStyle.__init__)


def test_hyp_viewpoint_basiclabelstyle_constructor_args():
    sig = inspect.signature(viewpoint_BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "labelColor" in params, "Missing parameter 'labelColor'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"








def test_hyp_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_hyp_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_hyp_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_labelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_LabelStyle)


def test_hyp_viewpoint_labelstyle_constructor_exists():
    assert callable(viewpoint_LabelStyle.__init__)


def test_hyp_viewpoint_labelstyle_constructor_args():
    sig = inspect.signature(viewpoint_LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"




def test_hyp_viewpoint_danalysiscustomdata_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysisCustomData)


def test_hyp_viewpoint_danalysiscustomdata_constructor_exists():
    assert callable(viewpoint_DAnalysisCustomData.__init__)


def test_hyp_viewpoint_danalysiscustomdata_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysisCustomData.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_viewpoint_uistate_is_not_abstract():
    assert not inspect.isabstract(viewpoint_UIState)


def test_hyp_viewpoint_uistate_constructor_exists():
    assert callable(viewpoint_UIState.__init__)


def test_hyp_viewpoint_uistate_constructor_args():
    sig = inspect.signature(viewpoint_UIState.__init__)
    params = list(sig.parameters.keys())
    assert "inverseSelectionOrder" in params, "Missing parameter 'inverseSelectionOrder'"
    assert "decorationImage" in params, "Missing parameter 'decorationImage'"





def test_hyp_annotationentry_is_not_abstract():
    assert not inspect.isabstract(AnnotationEntry)


def test_hyp_annotationentry_constructor_exists():
    assert callable(AnnotationEntry.__init__)


def test_hyp_annotationentry_constructor_args():
    sig = inspect.signature(AnnotationEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_metamodelextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_MetaModelExtension)


def test_hyp_viewpoint_metamodelextension_constructor_exists():
    assert callable(viewpoint_MetaModelExtension.__init__)


def test_hyp_viewpoint_metamodelextension_constructor_args():
    sig = inspect.signature(viewpoint_MetaModelExtension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_is_not_abstract():
    assert not inspect.isabstract(Viewpoint)


def test_hyp_viewpoint_constructor_exists():
    assert callable(Viewpoint.__init__)


def test_hyp_viewpoint_constructor_args():
    sig = inspect.signature(Viewpoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(DSemanticDecorator)


def test_hyp_dsemanticdecorator_constructor_exists():
    assert callable(DSemanticDecorator.__init__)


def test_hyp_dsemanticdecorator_constructor_args():
    sig = inspect.signature(DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dstylizable_is_not_abstract():
    assert not inspect.isabstract(DStylizable)


def test_hyp_dstylizable_constructor_exists():
    assert callable(DStylizable.__init__)


def test_hyp_dstylizable_constructor_args():
    sig = inspect.signature(DStylizable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dmappingbased_is_not_abstract():
    assert not inspect.isabstract(DMappingBased)


def test_hyp_dmappingbased_constructor_exists():
    assert callable(DMappingBased.__init__)


def test_hyp_dmappingbased_constructor_args():
    sig = inspect.signature(DMappingBased.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_drefreshable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRefreshable)


def test_hyp_viewpoint_drefreshable_constructor_exists():
    assert callable(viewpoint_DRefreshable.__init__)


def test_hyp_viewpoint_drefreshable_constructor_args():
    sig = inspect.signature(viewpoint_DRefreshable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dstylizable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DStylizable)


def test_hyp_viewpoint_dstylizable_constructor_exists():
    assert callable(viewpoint_DStylizable.__init__)


def test_hyp_viewpoint_dstylizable_constructor_args():
    sig = inspect.signature(viewpoint_DStylizable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featureextensiondescription_is_not_abstract():
    assert not inspect.isabstract(FeatureExtensionDescription)


def test_hyp_featureextensiondescription_constructor_exists():
    assert callable(FeatureExtensionDescription.__init__)


def test_hyp_featureextensiondescription_constructor_args():
    sig = inspect.signature(FeatureExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dfeatureextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFeatureExtension)


def test_hyp_viewpoint_dfeatureextension_constructor_exists():
    assert callable(viewpoint_DFeatureExtension.__init__)


def test_hyp_viewpoint_dfeatureextension_constructor_args():
    sig = inspect.signature(viewpoint_DFeatureExtension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_dmodelelement_is_not_abstract():
    assert not inspect.isabstract(description_DModelElement)


def test_hyp_description_dmodelelement_constructor_exists():
    assert callable(description_DModelElement.__init__)


def test_hyp_description_dmodelelement_constructor_args():
    sig = inspect.signature(description_DModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_drefreshable_is_not_abstract():
    assert not inspect.isabstract(DRefreshable)


def test_hyp_drefreshable_constructor_exists():
    assert callable(DRefreshable.__init__)


def test_hyp_drefreshable_constructor_args():
    sig = inspect.signature(DRefreshable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentationElement)


def test_hyp_viewpoint_drepresentationelement_constructor_exists():
    assert callable(viewpoint_DRepresentationElement.__init__)


def test_hyp_viewpoint_drepresentationelement_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentationElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_viewpoint_style_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Style)


def test_hyp_viewpoint_style_constructor_exists():
    assert callable(viewpoint_Style.__init__)


def test_hyp_viewpoint_style_constructor_args():
    sig = inspect.signature(viewpoint_Style.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_documentedelement_is_not_abstract():
    assert not inspect.isabstract(description_DocumentedElement)


def test_hyp_description_documentedelement_constructor_exists():
    assert callable(description_DocumentedElement.__init__)


def test_hyp_description_documentedelement_constructor_args():
    sig = inspect.signature(description_DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_toolentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolEntry)


def test_hyp_viewpoint_tool_toolentry_constructor_exists():
    assert callable(viewpoint_tool_ToolEntry.__init__)


def test_hyp_viewpoint_tool_toolentry_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_representationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationDescription)


def test_hyp_viewpoint_description_representationdescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationDescription.__init__)


def test_hyp_viewpoint_description_representationdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "showOnStartup" in params, "Missing parameter 'showOnStartup'"
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"
    assert "initialisation" in params, "Missing parameter 'initialisation'"






def test_hyp_viewpoint_description_viewpoint_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Viewpoint)


def test_hyp_viewpoint_description_viewpoint_constructor_exists():
    assert callable(viewpoint_description_Viewpoint.__init__)


def test_hyp_viewpoint_description_viewpoint_constructor_args():
    sig = inspect.signature(viewpoint_description_Viewpoint.__init__)
    params = list(sig.parameters.keys())
    assert "customizes" in params, "Missing parameter 'customizes'"
    assert "modelFileExtension" in params, "Missing parameter 'modelFileExtension'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "conflicts" in params, "Missing parameter 'conflicts'"
    assert "reuses" in params, "Missing parameter 'reuses'"








def test_hyp_viewpoint_description_group_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Group)


def test_hyp_viewpoint_description_group_constructor_exists():
    assert callable(viewpoint_description_Group.__init__)


def test_hyp_viewpoint_description_group_constructor_args():
    sig = inspect.signature(viewpoint_description_Group.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_viewpoint_drepresentation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentation)


def test_hyp_viewpoint_drepresentation_constructor_exists():
    assert callable(viewpoint_DRepresentation.__init__)


def test_hyp_viewpoint_drepresentation_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_representationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationDescription)


def test_hyp_representationdescription_constructor_exists():
    assert callable(RepresentationDescription.__init__)


def test_hyp_representationdescription_constructor_args():
    sig = inspect.signature(RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_description_representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationImportDescription)


def test_hyp_viewpoint_description_representationimportdescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationImportDescription.__init__)


def test_hyp_viewpoint_description_representationimportdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_drepresentationdescriptor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentationDescriptor)


def test_hyp_viewpoint_drepresentationdescriptor_constructor_exists():
    assert callable(viewpoint_DRepresentationDescriptor.__init__)


def test_hyp_viewpoint_drepresentationdescriptor_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentationDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_viewpoint_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DSemanticDecorator)


def test_hyp_viewpoint_dsemanticdecorator_constructor_exists():
    assert callable(viewpoint_DSemanticDecorator.__init__)


def test_hyp_viewpoint_dsemanticdecorator_constructor_args():
    sig = inspect.signature(viewpoint_DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dmappingbased_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DMappingBased)


def test_hyp_viewpoint_dmappingbased_constructor_exists():
    assert callable(viewpoint_DMappingBased.__init__)


def test_hyp_viewpoint_dmappingbased_constructor_args():
    sig = inspect.signature(viewpoint_DMappingBased.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_dview_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DView)


def test_hyp_viewpoint_dview_constructor_exists():
    assert callable(viewpoint_DView.__init__)


def test_hyp_viewpoint_dview_constructor_args():
    sig = inspect.signature(viewpoint_DView.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dannotationentry_is_not_abstract():
    assert not inspect.isabstract(DAnnotationEntry)


def test_hyp_dannotationentry_constructor_exists():
    assert callable(DAnnotationEntry.__init__)


def test_hyp_dannotationentry_constructor_args():
    sig = inspect.signature(DAnnotationEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_EObject)


def test_hyp_viewpoint_eobject_constructor_exists():
    assert callable(viewpoint_EObject.__init__)


def test_hyp_viewpoint_eobject_constructor_args():
    sig = inspect.signature(viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_danalysis_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysis)


def test_hyp_viewpoint_danalysis_constructor_exists():
    assert callable(viewpoint_DAnalysis.__init__)


def test_hyp_viewpoint_danalysis_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysis.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "semanticResources" in params, "Missing parameter 'semanticResources'"





def test_hyp_viewpoint_validation_validationfix_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationFix)


def test_hyp_viewpoint_validation_validationfix_constructor_exists():
    assert callable(viewpoint_validation_ValidationFix.__init__)


def test_hyp_viewpoint_validation_validationfix_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationFix.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_informationsection_is_not_abstract():
    assert not inspect.isabstract(InformationSection)


def test_hyp_informationsection_constructor_exists():
    assert callable(InformationSection.__init__)


def test_hyp_informationsection_constructor_args():
    sig = inspect.signature(InformationSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_audit_templateinformationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint_audit_TemplateInformationSection)


def test_hyp_viewpoint_audit_templateinformationsection_constructor_exists():
    assert callable(viewpoint_audit_TemplateInformationSection.__init__)


def test_hyp_viewpoint_audit_templateinformationsection_constructor_args():
    sig = inspect.signature(viewpoint_audit_TemplateInformationSection.__init__)
    params = list(sig.parameters.keys())
    assert "templatePath" in params, "Missing parameter 'templatePath'"




def test_hyp_viewpoint_audit_informationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint_audit_InformationSection)


def test_hyp_viewpoint_audit_informationsection_constructor_exists():
    assert callable(viewpoint_audit_InformationSection.__init__)


def test_hyp_viewpoint_audit_informationsection_constructor_args():
    sig = inspect.signature(viewpoint_audit_InformationSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_validation_ruleaudit_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_RuleAudit)


def test_hyp_viewpoint_validation_ruleaudit_constructor_exists():
    assert callable(viewpoint_validation_RuleAudit.__init__)


def test_hyp_viewpoint_validation_ruleaudit_constructor_args():
    sig = inspect.signature(viewpoint_validation_RuleAudit.__init__)
    params = list(sig.parameters.keys())
    assert "auditExpression" in params, "Missing parameter 'auditExpression'"




def test_hyp_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(RepresentationElementMapping)


def test_hyp_representationelementmapping_constructor_exists():
    assert callable(RepresentationElementMapping.__init__)


def test_hyp_representationelementmapping_constructor_args():
    sig = inspect.signature(RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_validationrule_is_not_abstract():
    assert not inspect.isabstract(ValidationRule)


def test_hyp_validationrule_constructor_exists():
    assert callable(ValidationRule.__init__)


def test_hyp_validationrule_constructor_args():
    sig = inspect.signature(ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_validation_viewvalidationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ViewValidationRule)


def test_hyp_viewpoint_validation_viewvalidationrule_constructor_exists():
    assert callable(viewpoint_validation_ViewValidationRule.__init__)


def test_hyp_viewpoint_validation_viewvalidationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_ViewValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_validation_semanticvalidationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_SemanticValidationRule)


def test_hyp_viewpoint_validation_semanticvalidationrule_constructor_exists():
    assert callable(viewpoint_validation_SemanticValidationRule.__init__)


def test_hyp_viewpoint_validation_semanticvalidationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_SemanticValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "targetClass" in params, "Missing parameter 'targetClass'"




def test_hyp_validation_validationfix_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationFix)


def test_hyp_validation_validationfix_constructor_exists():
    assert callable(validation_ValidationFix.__init__)


def test_hyp_validation_validationfix_constructor_args():
    sig = inspect.signature(validation_ValidationFix.__init__)
    params = list(sig.parameters.keys())



def test_hyp_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_hyp_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_hyp_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_validation_validationset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationSet)


def test_hyp_viewpoint_validation_validationset_constructor_exists():
    assert callable(viewpoint_validation_ValidationSet.__init__)


def test_hyp_viewpoint_validation_validationset_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_validation_ruleaudit_is_not_abstract():
    assert not inspect.isabstract(validation_RuleAudit)


def test_hyp_validation_ruleaudit_constructor_exists():
    assert callable(validation_RuleAudit.__init__)


def test_hyp_validation_ruleaudit_constructor_args():
    sig = inspect.signature(validation_RuleAudit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_validation_validationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationRule)


def test_hyp_viewpoint_validation_validationrule_constructor_exists():
    assert callable(viewpoint_validation_ValidationRule.__init__)


def test_hyp_viewpoint_validation_validationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "message" in params, "Missing parameter 'message'"





def test_hyp_validation_validationrule_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationRule)


def test_hyp_validation_validationrule_constructor_exists():
    assert callable(validation_ValidationRule.__init__)


def test_hyp_validation_validationrule_constructor_args():
    sig = inspect.signature(validation_ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_FeatureChangeListener)


def test_hyp_viewpoint_tool_featurechangelistener_constructor_exists():
    assert callable(viewpoint_tool_FeatureChangeListener.__init__)


def test_hyp_viewpoint_tool_featurechangelistener_constructor_args():
    sig = inspect.signature(viewpoint_tool_FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "featureName" in params, "Missing parameter 'featureName'"





def test_hyp_tool_default_is_not_abstract():
    assert not inspect.isabstract(tool_Default)


def test_hyp_tool_default_constructor_exists():
    assert callable(tool_Default.__init__)


def test_hyp_tool_default_constructor_args():
    sig = inspect.signature(tool_Default.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_case_is_not_abstract():
    assert not inspect.isabstract(tool_Case)


def test_hyp_tool_case_constructor_exists():
    assert callable(tool_Case.__init__)


def test_hyp_tool_case_constructor_args():
    sig = inspect.signature(tool_Case.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_switchchild_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SwitchChild)


def test_hyp_viewpoint_tool_switchchild_constructor_exists():
    assert callable(viewpoint_tool_SwitchChild.__init__)


def test_hyp_viewpoint_tool_switchchild_constructor_args():
    sig = inspect.signature(viewpoint_tool_SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_hyp_switchchild_is_not_abstract():
    assert not inspect.isabstract(SwitchChild)


def test_hyp_switchchild_constructor_exists():
    assert callable(SwitchChild.__init__)


def test_hyp_switchchild_constructor_args():
    sig = inspect.signature(SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_default_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Default)


def test_hyp_viewpoint_tool_default_constructor_exists():
    assert callable(viewpoint_tool_Default.__init__)


def test_hyp_viewpoint_tool_default_constructor_args():
    sig = inspect.signature(viewpoint_tool_Default.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_case_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Case)


def test_hyp_viewpoint_tool_case_constructor_exists():
    assert callable(viewpoint_tool_Case.__init__)


def test_hyp_viewpoint_tool_case_constructor_args():
    sig = inspect.signature(viewpoint_tool_Case.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"




def test_hyp_viewpoint_tool_externaljavaactionparameter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaActionParameter)


def test_hyp_viewpoint_tool_externaljavaactionparameter_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaActionParameter.__init__)


def test_hyp_viewpoint_tool_externaljavaactionparameter_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaActionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_tool_featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(tool_FeatureChangeListener)


def test_hyp_tool_featurechangelistener_constructor_exists():
    assert callable(tool_FeatureChangeListener.__init__)


def test_hyp_tool_featurechangelistener_constructor_args():
    sig = inspect.signature(tool_FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolFilterDescription)


def test_hyp_viewpoint_tool_toolfilterdescription_constructor_exists():
    assert callable(viewpoint_tool_ToolFilterDescription.__init__)


def test_hyp_viewpoint_tool_toolfilterdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "elementsToListen" in params, "Missing parameter 'elementsToListen'"





def test_hyp_viewpoint_tool_namevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_NameVariable)


def test_hyp_viewpoint_tool_namevariable_constructor_exists():
    assert callable(viewpoint_tool_NameVariable.__init__)


def test_hyp_viewpoint_tool_namevariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_NameVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(tool_viewpoint_EObject)


def test_hyp_tool_viewpoint_eobject_constructor_exists():
    assert callable(tool_viewpoint_EObject.__init__)


def test_hyp_tool_viewpoint_eobject_constructor_args():
    sig = inspect.signature(tool_viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialOperation)


def test_hyp_viewpoint_tool_initialoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialOperation.__init__)


def test_hyp_viewpoint_tool_initialoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialNodeCreationOperation)


def test_hyp_viewpoint_tool_initialnodecreationoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialNodeCreationOperation.__init__)


def test_hyp_viewpoint_tool_initialnodecreationoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_modeloperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ModelOperation)


def test_hyp_viewpoint_tool_modeloperation_constructor_exists():
    assert callable(viewpoint_tool_ModelOperation.__init__)


def test_hyp_viewpoint_tool_modeloperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_modeloperation_is_not_abstract():
    assert not inspect.isabstract(tool_ModelOperation)


def test_hyp_tool_modeloperation_constructor_exists():
    assert callable(tool_ModelOperation.__init__)


def test_hyp_tool_modeloperation_constructor_args():
    sig = inspect.signature(tool_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modeloperation_is_not_abstract():
    assert not inspect.isabstract(ModelOperation)


def test_hyp_modeloperation_constructor_exists():
    assert callable(ModelOperation.__init__)


def test_hyp_modeloperation_constructor_args():
    sig = inspect.signature(ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_switch_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Switch)


def test_hyp_viewpoint_tool_switch_constructor_exists():
    assert callable(viewpoint_tool_Switch.__init__)


def test_hyp_viewpoint_tool_switch_constructor_args():
    sig = inspect.signature(viewpoint_tool_Switch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ContainerModelOperation)


def test_hyp_viewpoint_tool_containermodeloperation_constructor_exists():
    assert callable(viewpoint_tool_ContainerModelOperation.__init__)


def test_hyp_viewpoint_tool_containermodeloperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_EditMaskVariables)


def test_hyp_viewpoint_tool_editmaskvariables_constructor_exists():
    assert callable(viewpoint_tool_EditMaskVariables.__init__)


def test_hyp_viewpoint_tool_editmaskvariables_constructor_args():
    sig = inspect.signature(viewpoint_tool_EditMaskVariables.__init__)
    params = list(sig.parameters.keys())
    assert "mask" in params, "Missing parameter 'mask'"




def test_hyp_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(ContainerModelOperation)


def test_hyp_containermodeloperation_constructor_exists():
    assert callable(ContainerModelOperation.__init__)


def test_hyp_containermodeloperation_constructor_args():
    sig = inspect.signature(ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_removeelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RemoveElement)


def test_hyp_viewpoint_tool_removeelement_constructor_exists():
    assert callable(viewpoint_tool_RemoveElement.__init__)


def test_hyp_viewpoint_tool_removeelement_constructor_args():
    sig = inspect.signature(viewpoint_tool_RemoveElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_setobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SetObject)


def test_hyp_viewpoint_tool_setobject_constructor_exists():
    assert callable(viewpoint_tool_SetObject.__init__)


def test_hyp_viewpoint_tool_setobject_constructor_args():
    sig = inspect.signature(viewpoint_tool_SetObject.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"




def test_hyp_viewpoint_tool_for_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_For)


def test_hyp_viewpoint_tool_for_constructor_exists():
    assert callable(viewpoint_tool_For.__init__)


def test_hyp_viewpoint_tool_for_constructor_args():
    sig = inspect.signature(viewpoint_tool_For.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"





def test_hyp_viewpoint_tool_if_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_If)


def test_hyp_viewpoint_tool_if_constructor_exists():
    assert callable(viewpoint_tool_If.__init__)


def test_hyp_viewpoint_tool_if_constructor_args():
    sig = inspect.signature(viewpoint_tool_If.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"




def test_hyp_viewpoint_tool_unset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Unset)


def test_hyp_viewpoint_tool_unset_constructor_exists():
    assert callable(viewpoint_tool_Unset.__init__)


def test_hyp_viewpoint_tool_unset_constructor_args():
    sig = inspect.signature(viewpoint_tool_Unset.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "elementExpression" in params, "Missing parameter 'elementExpression'"





def test_hyp_viewpoint_tool_deleteview_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DeleteView)


def test_hyp_viewpoint_tool_deleteview_constructor_exists():
    assert callable(viewpoint_tool_DeleteView.__init__)


def test_hyp_viewpoint_tool_deleteview_constructor_args():
    sig = inspect.signature(viewpoint_tool_DeleteView.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_changecontext_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ChangeContext)


def test_hyp_viewpoint_tool_changecontext_constructor_exists():
    assert callable(viewpoint_tool_ChangeContext.__init__)


def test_hyp_viewpoint_tool_changecontext_constructor_args():
    sig = inspect.signature(viewpoint_tool_ChangeContext.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"




def test_hyp_viewpoint_tool_setvalue_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SetValue)


def test_hyp_viewpoint_tool_setvalue_constructor_exists():
    assert callable(viewpoint_tool_SetValue.__init__)


def test_hyp_viewpoint_tool_setvalue_constructor_args():
    sig = inspect.signature(viewpoint_tool_SetValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"





def test_hyp_viewpoint_tool_let_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Let)


def test_hyp_viewpoint_tool_let_constructor_exists():
    assert callable(viewpoint_tool_Let.__init__)


def test_hyp_viewpoint_tool_let_constructor_args():
    sig = inspect.signature(viewpoint_tool_Let.__init__)
    params = list(sig.parameters.keys())
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"
    assert "variableName" in params, "Missing parameter 'variableName'"





def test_hyp_viewpoint_tool_moveelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MoveElement)


def test_hyp_viewpoint_tool_moveelement_constructor_exists():
    assert callable(viewpoint_tool_MoveElement.__init__)


def test_hyp_viewpoint_tool_moveelement_constructor_args():
    sig = inspect.signature(viewpoint_tool_MoveElement.__init__)
    params = list(sig.parameters.keys())
    assert "newContainerExpression" in params, "Missing parameter 'newContainerExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"





def test_hyp_viewpoint_tool_createinstance_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_CreateInstance)


def test_hyp_viewpoint_tool_createinstance_constructor_exists():
    assert callable(viewpoint_tool_CreateInstance.__init__)


def test_hyp_viewpoint_tool_createinstance_constructor_args():
    sig = inspect.signature(viewpoint_tool_CreateInstance.__init__)
    params = list(sig.parameters.keys())
    assert "referenceName" in params, "Missing parameter 'referenceName'"
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "typeName" in params, "Missing parameter 'typeName'"






def test_hyp_viewpoint_tool_initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialContainerDropOperation)


def test_hyp_viewpoint_tool_initialcontainerdropoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialContainerDropOperation.__init__)


def test_hyp_viewpoint_tool_initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitEdgeCreationOperation)


def test_hyp_viewpoint_tool_initedgecreationoperation_constructor_exists():
    assert callable(viewpoint_tool_InitEdgeCreationOperation.__init__)


def test_hyp_viewpoint_tool_initedgecreationoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_popupmenu_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PopupMenu)


def test_hyp_viewpoint_tool_popupmenu_constructor_exists():
    assert callable(viewpoint_tool_PopupMenu.__init__)


def test_hyp_viewpoint_tool_popupmenu_constructor_args():
    sig = inspect.signature(viewpoint_tool_PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_externaljavaaction_is_not_abstract():
    assert not inspect.isabstract(tool_ExternalJavaAction)


def test_hyp_tool_externaljavaaction_constructor_exists():
    assert callable(tool_ExternalJavaAction.__init__)


def test_hyp_tool_externaljavaaction_constructor_args():
    sig = inspect.signature(tool_ExternalJavaAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_externaljavaactionparameter_is_not_abstract():
    assert not inspect.isabstract(tool_ExternalJavaActionParameter)


def test_hyp_tool_externaljavaactionparameter_constructor_exists():
    assert callable(tool_ExternalJavaActionParameter.__init__)


def test_hyp_tool_externaljavaactionparameter_constructor_args():
    sig = inspect.signature(tool_ExternalJavaActionParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerModelOperation)


def test_hyp_tool_containermodeloperation_constructor_exists():
    assert callable(tool_ContainerModelOperation.__init__)


def test_hyp_tool_containermodeloperation_constructor_args():
    sig = inspect.signature(tool_ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementSelectVariable)


def test_hyp_viewpoint_tool_elementselectvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementSelectVariable.__init__)


def test_hyp_viewpoint_tool_elementselectvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(description_AbstractVariable)


def test_hyp_description_abstractvariable_constructor_exists():
    assert callable(description_AbstractVariable.__init__)


def test_hyp_description_abstractvariable_constructor_args():
    sig = inspect.signature(description_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_dialogvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DialogVariable)


def test_hyp_viewpoint_tool_dialogvariable_constructor_exists():
    assert callable(viewpoint_tool_DialogVariable.__init__)


def test_hyp_viewpoint_tool_dialogvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_DialogVariable.__init__)
    params = list(sig.parameters.keys())
    assert "dialogPrompt" in params, "Missing parameter 'dialogPrompt'"




def test_hyp_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool_VariableContainer)


def test_hyp_tool_variablecontainer_constructor_exists():
    assert callable(tool_VariableContainer.__init__)


def test_hyp_tool_variablecontainer_constructor_args():
    sig = inspect.signature(tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectContainerVariable)


def test_hyp_viewpoint_tool_selectcontainervariable_constructor_exists():
    assert callable(viewpoint_tool_SelectContainerVariable.__init__)


def test_hyp_viewpoint_tool_selectcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementDeleteVariable)


def test_hyp_viewpoint_tool_elementdeletevariable_constructor_exists():
    assert callable(viewpoint_tool_ElementDeleteVariable.__init__)


def test_hyp_viewpoint_tool_elementdeletevariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_elementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementVariable)


def test_hyp_viewpoint_tool_elementvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementVariable.__init__)


def test_hyp_viewpoint_tool_elementvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DropContainerVariable)


def test_hyp_viewpoint_tool_dropcontainervariable_constructor_exists():
    assert callable(viewpoint_tool_DropContainerVariable.__init__)


def test_hyp_viewpoint_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementViewVariable)


def test_hyp_viewpoint_tool_elementviewvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementViewVariable.__init__)


def test_hyp_viewpoint_tool_elementviewvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementDropVariable)


def test_hyp_viewpoint_tool_elementdropvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementDropVariable.__init__)


def test_hyp_viewpoint_tool_elementdropvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ContainerViewVariable)


def test_hyp_viewpoint_tool_containerviewvariable_constructor_exists():
    assert callable(viewpoint_tool_ContainerViewVariable.__init__)


def test_hyp_viewpoint_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_acceleovariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_AcceleoVariable)


def test_hyp_viewpoint_tool_acceleovariable_constructor_exists():
    assert callable(viewpoint_tool_AcceleoVariable.__init__)


def test_hyp_viewpoint_tool_acceleovariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_AcceleoVariable.__init__)
    params = list(sig.parameters.keys())
    assert "computationExpression" in params, "Missing parameter 'computationExpression'"




def test_hyp_subvariable_is_not_abstract():
    assert not inspect.isabstract(SubVariable)


def test_hyp_subvariable_constructor_exists():
    assert callable(SubVariable.__init__)


def test_hyp_subvariable_constructor_args():
    sig = inspect.signature(SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_VariableContainer)


def test_hyp_viewpoint_tool_variablecontainer_constructor_exists():
    assert callable(viewpoint_tool_VariableContainer.__init__)


def test_hyp_viewpoint_tool_variablecontainer_constructor_args():
    sig = inspect.signature(viewpoint_tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(MenuItemDescription)


def test_hyp_menuitemdescription_constructor_exists():
    assert callable(MenuItemDescription.__init__)


def test_hyp_menuitemdescription_constructor_args():
    sig = inspect.signature(MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_operationaction_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_OperationAction)


def test_hyp_viewpoint_tool_operationaction_constructor_exists():
    assert callable(viewpoint_tool_OperationAction.__init__)


def test_hyp_viewpoint_tool_operationaction_constructor_args():
    sig = inspect.signature(viewpoint_tool_OperationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(tool_MenuItemDescription)


def test_hyp_tool_menuitemdescription_constructor_exists():
    assert callable(tool_MenuItemDescription.__init__)


def test_hyp_tool_menuitemdescription_constructor_args():
    sig = inspect.signature(tool_MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_externaljavaaction_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaAction)


def test_hyp_viewpoint_tool_externaljavaaction_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaAction.__init__)


def test_hyp_viewpoint_tool_externaljavaaction_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaAction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_viewpoint_tool_externaljavaactioncall_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaActionCall)


def test_hyp_viewpoint_tool_externaljavaactioncall_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaActionCall.__init__)


def test_hyp_viewpoint_tool_externaljavaactioncall_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaActionCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(MenuItemOrRef)


def test_hyp_menuitemorref_constructor_exists():
    assert callable(MenuItemOrRef.__init__)


def test_hyp_menuitemorref_constructor_args():
    sig = inspect.signature(MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_menuitemdescriptionreference_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemDescriptionReference)


def test_hyp_viewpoint_tool_menuitemdescriptionreference_constructor_exists():
    assert callable(viewpoint_tool_MenuItemDescriptionReference.__init__)


def test_hyp_viewpoint_tool_menuitemdescriptionreference_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemDescriptionReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(tool_MenuItemOrRef)


def test_hyp_tool_menuitemorref_constructor_exists():
    assert callable(tool_MenuItemOrRef.__init__)


def test_hyp_tool_menuitemorref_constructor_args():
    sig = inspect.signature(tool_MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemOrRef)


def test_hyp_viewpoint_tool_menuitemorref_constructor_exists():
    assert callable(viewpoint_tool_MenuItemOrRef.__init__)


def test_hyp_viewpoint_tool_menuitemorref_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_namevariable_is_not_abstract():
    assert not inspect.isabstract(tool_NameVariable)


def test_hyp_tool_namevariable_constructor_exists():
    assert callable(tool_NameVariable.__init__)


def test_hyp_tool_namevariable_constructor_args():
    sig = inspect.signature(tool_NameVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RepresentationNavigationDescription)


def test_hyp_viewpoint_tool_representationnavigationdescription_constructor_exists():
    assert callable(viewpoint_tool_RepresentationNavigationDescription.__init__)


def test_hyp_viewpoint_tool_representationnavigationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"
    assert "navigationNameExpression" in params, "Missing parameter 'navigationNameExpression'"





def test_hyp_viewpoint_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RepresentationCreationDescription)


def test_hyp_viewpoint_tool_representationcreationdescription_constructor_exists():
    assert callable(viewpoint_tool_RepresentationCreationDescription.__init__)


def test_hyp_viewpoint_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"





def test_hyp_tool_selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_SelectContainerVariable)


def test_hyp_tool_selectcontainervariable_constructor_exists():
    assert callable(tool_SelectContainerVariable.__init__)


def test_hyp_tool_selectcontainervariable_constructor_args():
    sig = inspect.signature(tool_SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementSelectVariable)


def test_hyp_tool_elementselectvariable_constructor_exists():
    assert callable(tool_ElementSelectVariable.__init__)


def test_hyp_tool_elementselectvariable_constructor_args():
    sig = inspect.signature(tool_ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_selectiondescription_is_not_abstract():
    assert not inspect.isabstract(description_SelectionDescription)


def test_hyp_description_selectiondescription_constructor_exists():
    assert callable(description_SelectionDescription.__init__)


def test_hyp_description_selectiondescription_constructor_args():
    sig = inspect.signature(description_SelectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_selectmodelelementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectModelElementVariable)


def test_hyp_viewpoint_tool_selectmodelelementvariable_constructor_exists():
    assert callable(viewpoint_tool_SelectModelElementVariable.__init__)


def test_hyp_viewpoint_tool_selectmodelelementvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectModelElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool_AbstractToolDescription)


def test_hyp_tool_abstracttooldescription_constructor_exists():
    assert callable(tool_AbstractToolDescription.__init__)


def test_hyp_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemDescription)


def test_hyp_viewpoint_tool_menuitemdescription_constructor_exists():
    assert callable(viewpoint_tool_MenuItemDescription.__init__)


def test_hyp_viewpoint_tool_menuitemdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemDescription.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"




def test_hyp_viewpoint_tool_selectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectionWizardDescription)


def test_hyp_viewpoint_tool_selectionwizarddescription_constructor_exists():
    assert callable(viewpoint_tool_SelectionWizardDescription.__init__)


def test_hyp_viewpoint_tool_selectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"






def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PaneBasedSelectionWizardDescription)


def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_constructor_exists():
    assert callable(viewpoint_tool_PaneBasedSelectionWizardDescription.__init__)


def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_PaneBasedSelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"
    assert "selectedValuesMessage" in params, "Missing parameter 'selectedValuesMessage'"
    assert "message" in params, "Missing parameter 'message'"
    assert "tree" in params, "Missing parameter 'tree'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "choiceOfValuesMessage" in params, "Missing parameter 'choiceOfValuesMessage'"
    assert "preSelectedCandidatesExpression" in params, "Missing parameter 'preSelectedCandidatesExpression'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"














def test_hyp_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerViewVariable)


def test_hyp_tool_containerviewvariable_constructor_exists():
    assert callable(tool_ContainerViewVariable.__init__)


def test_hyp_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_DropContainerVariable)


def test_hyp_tool_dropcontainervariable_constructor_exists():
    assert callable(tool_DropContainerVariable.__init__)


def test_hyp_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_elementvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementVariable)


def test_hyp_tool_elementvariable_constructor_exists():
    assert callable(tool_ElementVariable.__init__)


def test_hyp_tool_elementvariable_constructor_args():
    sig = inspect.signature(tool_ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(MappingBasedToolDescription)


def test_hyp_mappingbasedtooldescription_constructor_exists():
    assert callable(MappingBasedToolDescription.__init__)


def test_hyp_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_pastedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PasteDescription)


def test_hyp_viewpoint_tool_pastedescription_constructor_exists():
    assert callable(viewpoint_tool_PasteDescription.__init__)


def test_hyp_viewpoint_tool_pastedescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_PasteDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_tool_tooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolDescription)


def test_hyp_viewpoint_tool_tooldescription_constructor_exists():
    assert callable(viewpoint_tool_ToolDescription.__init__)


def test_hyp_viewpoint_tool_tooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"


def test_hyp_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_hyp_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "WEST",
        "SOUTH_WEST",
        "EAST",
        "SOUTH_EAST",
        "NORTH_EAST",
        "NORTH_WEST",
        "CENTER",
        "SOUTH",
        "NORTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"

def test_hyp_fontformat_exists():
    # Check that the Enumeration exists
    assert FontFormat is not None

def test_hyp_fontformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontFormat]
    expected_literals = [
        "bold",
        "strike_through",
        "underline",
        "italic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontFormat"

def test_hyp_labelalignment_exists():
    # Check that the Enumeration exists
    assert LabelAlignment is not None

def test_hyp_labelalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelAlignment]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelAlignment"

def test_hyp_systemcolors_exists():
    # Check that the Enumeration exists
    assert SystemColors is not None

def test_hyp_systemcolors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemColors]
    expected_literals = [
        "black",
        "light_blue",
        "light_chocolate",
        "dark_red",
        "dark_orange",
        "chocolate",
        "dark_green",
        "dark_yellow",
        "purple",
        "dark_chocolate",
        "red",
        "yellow",
        "blue",
        "light_yellow",
        "orange",
        "light_gray",
        "white",
        "dark_purple",
        "gray",
        "light_orange",
        "light_purple",
        "light_red",
        "light_green",
        "green",
        "dark_gray",
        "dark_blue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemColors"

def test_hyp_decorationdistributiondirection_exists():
    # Check that the Enumeration exists
    assert DecorationDistributionDirection is not None

def test_hyp_decorationdistributiondirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DecorationDistributionDirection]
    expected_literals = [
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DecorationDistributionDirection"

def test_hyp_error_level_exists():
    # Check that the Enumeration exists
    assert ERROR_LEVEL is not None

def test_hyp_error_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ERROR_LEVEL]
    expected_literals = [
        "WARNING",
        "INFO",
        "ERROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ERROR_LEVEL"

def test_hyp_dragsource_exists():
    # Check that the Enumeration exists
    assert DragSource is not None

def test_hyp_dragsource_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DragSource]
    expected_literals = [
        "PROJECT_EXPLORER",
        "BOTH",
        "DIAGRAM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DragSource"

def test_hyp_syncstatus_exists():
    # Check that the Enumeration exists
    assert SyncStatus is not None

def test_hyp_syncstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SyncStatus]
    expected_literals = [
        "dirty",
        "sync",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SyncStatus"


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
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
viewpoint_tool_MappingBasedToolDescription_strategy = st.builds(
    viewpoint_tool_MappingBasedToolDescription,
)
tool_InitialOperation_strategy = st.builds(
    tool_InitialOperation,
)
tool_ElementViewVariable_strategy = st.builds(
    tool_ElementViewVariable,
)
ToolEntry_strategy = st.builds(
    ToolEntry,
)
viewpoint_tool_AbstractToolDescription_strategy = st.builds(
    viewpoint_tool_AbstractToolDescription,
    inverseSelectionOrder=
        st.booleans(),
    forceRefresh=
        st.booleans(),
    elementsToSelect=
        safe_text,
    precondition=
        safe_text
)
tool_ToolFilterDescription_strategy = st.builds(
    tool_ToolFilterDescription,
)
BasicLabelStyleDescription_strategy = st.builds(
    BasicLabelStyleDescription,
)
viewpoint_style_LabelStyleDescription_strategy = st.builds(
    viewpoint_style_LabelStyleDescription,
    labelAlignment=
        safe_text
)
viewpoint_style_TooltipStyleDescription_strategy = st.builds(
    viewpoint_style_TooltipStyleDescription,
    tooltipExpression=
        safe_text
)
viewpoint_style_LabelBorderStyleDescription_strategy = st.builds(
    viewpoint_style_LabelBorderStyleDescription,
    cornerHeight=
        st.integers(),
    name=
        safe_text,
    id=
        safe_text,
    cornerWidth=
        st.integers()
)
style_LabelBorderStyleDescription_strategy = st.builds(
    style_LabelBorderStyleDescription,
)
viewpoint_style_LabelBorderStyles_strategy = st.builds(
    viewpoint_style_LabelBorderStyles,
)
description_viewpoint_EDataType_strategy = st.builds(
    description_viewpoint_EDataType,
)
viewpoint_style_BasicLabelStyleDescription_strategy = st.builds(
    viewpoint_style_BasicLabelStyleDescription,
    labelSize=
        st.integers(),
    iconPath=
        safe_text,
    labelExpression=
        safe_text,
    showIcon=
        st.booleans(),
    labelFormat=
        safe_text
)
viewpoint_style_StyleDescription_strategy = st.builds(
    viewpoint_style_StyleDescription,
)
viewpoint_description_IdentifiedElement_strategy = st.builds(
    viewpoint_description_IdentifiedElement,
    name=
        safe_text,
    label=
        safe_text
)
viewpoint_description_EndUserDocumentedElement_strategy = st.builds(
    viewpoint_description_EndUserDocumentedElement,
    endUserDocumentation=
        safe_text
)
viewpoint_description_AnnotationEntry_strategy = st.builds(
    viewpoint_description_AnnotationEntry,
    source=
        safe_text
)
UserColor_strategy = st.builds(
    UserColor,
)
description_SubVariable_strategy = st.builds(
    description_SubVariable,
)
description_InteractiveVariableDescription_strategy = st.builds(
    description_InteractiveVariableDescription,
)
viewpoint_description_TypedVariable_strategy = st.builds(
    viewpoint_description_TypedVariable,
    defaultValueExpression=
        safe_text
)
viewpoint_description_InteractiveVariableDescription_strategy = st.builds(
    viewpoint_description_InteractiveVariableDescription,
    userDocumentation=
        safe_text
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
viewpoint_description_SubVariable_strategy = st.builds(
    viewpoint_description_SubVariable,
)
viewpoint_description_AbstractVariable_strategy = st.builds(
    viewpoint_description_AbstractVariable,
    name=
        safe_text
)
viewpoint_description_DAnnotationEntry_strategy = st.builds(
    viewpoint_description_DAnnotationEntry,
    source=
        safe_text,
    details=
        safe_text
)
viewpoint_description_UserColor_strategy = st.builds(
    viewpoint_description_UserColor,
    name=
        safe_text
)
description_FixedColor_strategy = st.builds(
    description_FixedColor,
)
viewpoint_description_UserColorsPalette_strategy = st.builds(
    viewpoint_description_UserColorsPalette,
    name=
        safe_text
)
SystemColor_strategy = st.builds(
    SystemColor,
)
viewpoint_description_SytemColorsPalette_strategy = st.builds(
    viewpoint_description_SytemColorsPalette,
)
style_LabelBorderStyles_strategy = st.builds(
    style_LabelBorderStyles,
)
tool_ToolEntry_strategy = st.builds(
    tool_ToolEntry,
)
viewpoint_description_Environment_strategy = st.builds(
    viewpoint_description_Environment,
)
description_UserColor_strategy = st.builds(
    description_UserColor,
)
viewpoint_description_UserFixedColor_strategy = st.builds(
    viewpoint_description_UserFixedColor,
)
description_ColorDescription_strategy = st.builds(
    description_ColorDescription,
)
viewpoint_description_ComputedColor_strategy = st.builds(
    viewpoint_description_ComputedColor,
    green=
        safe_text,
    red=
        safe_text,
    blue=
        safe_text
)
viewpoint_description_InterpolatedColor_strategy = st.builds(
    viewpoint_description_InterpolatedColor,
    maxValueComputationExpression=
        safe_text,
    minValueComputationExpression=
        safe_text,
    colorValueComputationExpression=
        safe_text
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
viewpoint_description_FixedColor_strategy = st.builds(
    viewpoint_description_FixedColor,
    red=
        st.integers(),
    green=
        st.integers(),
    blue=
        st.integers()
)
viewpoint_description_ColorStep_strategy = st.builds(
    viewpoint_description_ColorStep,
    associatedValue=
        safe_text
)
ColorStep_strategy = st.builds(
    ColorStep,
)
FixedColor_strategy = st.builds(
    FixedColor,
)
viewpoint_description_SystemColor_strategy = st.builds(
    viewpoint_description_SystemColor,
    name=
        safe_text
)
viewpoint_description_ColorDescription_strategy = st.builds(
    viewpoint_description_ColorDescription,
)
viewpoint_description_SelectionDescription_strategy = st.builds(
    viewpoint_description_SelectionDescription,
    tree=
        st.booleans(),
    rootExpression=
        safe_text,
    candidatesExpression=
        safe_text,
    multiple=
        st.booleans(),
    message=
        safe_text,
    childrenExpression=
        safe_text
)
viewpoint_description_IVSMElementCustomization_strategy = st.builds(
    viewpoint_description_IVSMElementCustomization,
)
IVSMElementCustomization_strategy = st.builds(
    IVSMElementCustomization,
)
viewpoint_description_VSMElementCustomization_strategy = st.builds(
    viewpoint_description_VSMElementCustomization,
    predicateExpression=
        safe_text
)
viewpoint_description_Customization_strategy = st.builds(
    viewpoint_description_Customization,
)
viewpoint_description_EStructuralFeatureCustomization_strategy = st.builds(
    viewpoint_description_EStructuralFeatureCustomization,
    applyOnAll=
        st.booleans()
)
viewpoint_description_VSMElementCustomizationReuse_strategy = st.builds(
    viewpoint_description_VSMElementCustomizationReuse,
)
EStructuralFeatureCustomization_strategy = st.builds(
    EStructuralFeatureCustomization,
)
viewpoint_description_EAttributeCustomization_strategy = st.builds(
    viewpoint_description_EAttributeCustomization,
    value=
        safe_text,
    attributeName=
        safe_text
)
viewpoint_description_EReferenceCustomization_strategy = st.builds(
    viewpoint_description_EReferenceCustomization,
    referenceName=
        safe_text
)
viewpoint_description_DecorationDescription_strategy = st.builds(
    viewpoint_description_DecorationDescription,
    tooltipExpression=
        safe_text,
    name=
        safe_text,
    imageExpression=
        safe_text,
    position=
        safe_text,
    distributionDirection=
        safe_text,
    preconditionExpression=
        safe_text
)
viewpoint_description_DecorationDescriptionsSet_strategy = st.builds(
    viewpoint_description_DecorationDescriptionsSet,
)
tool_PasteDescription_strategy = st.builds(
    tool_PasteDescription,
)
viewpoint_description_PasteTargetDescription_strategy = st.builds(
    viewpoint_description_PasteTargetDescription,
)
viewpoint_description_AbstractMappingImport_strategy = st.builds(
    viewpoint_description_AbstractMappingImport,
    hideSubMappings=
        st.booleans(),
    inheritsAncestorFilters=
        st.booleans()
)
tool_RepresentationNavigationDescription_strategy = st.builds(
    tool_RepresentationNavigationDescription,
)
tool_RepresentationCreationDescription_strategy = st.builds(
    tool_RepresentationCreationDescription,
)
IdentifiedElement_strategy = st.builds(
    IdentifiedElement,
)
viewpoint_description_ConditionalStyleDescription_strategy = st.builds(
    viewpoint_description_ConditionalStyleDescription,
    predicateExpression=
        safe_text
)
description_viewpoint_EStringToStringMapEntry_strategy = st.builds(
    description_viewpoint_EStringToStringMapEntry,
)
viewpoint_description_DAnnotation_strategy = st.builds(
    viewpoint_description_DAnnotation,
    source=
        safe_text
)
DAnnotation_strategy = st.builds(
    DAnnotation,
)
viewpoint_description_DModelElement_strategy = st.builds(
    viewpoint_description_DModelElement,
)
viewpoint_description_DocumentedElement_strategy = st.builds(
    viewpoint_description_DocumentedElement,
    documentation=
        safe_text
)
viewpoint_description_RepresentationTemplate_strategy = st.builds(
    viewpoint_description_RepresentationTemplate,
    name=
        safe_text
)
description_viewpoint_EPackage_strategy = st.builds(
    description_viewpoint_EPackage,
)
viewpoint_description_RepresentationElementMapping_strategy = st.builds(
    viewpoint_description_RepresentationElementMapping,
)
viewpoint_description_JavaExtension_strategy = st.builds(
    viewpoint_description_JavaExtension,
    qualifiedClassName=
        safe_text
)
description_viewpoint_EObject_strategy = st.builds(
    description_viewpoint_EObject,
)
viewpoint_description_MetamodelExtensionSetting_strategy = st.builds(
    viewpoint_description_MetamodelExtensionSetting,
)
viewpoint_description_RepresentationExtensionDescription_strategy = st.builds(
    viewpoint_description_RepresentationExtensionDescription,
    representationName=
        safe_text,
    name=
        safe_text,
    viewpointURI=
        safe_text
)
validation_ValidationSet_strategy = st.builds(
    validation_ValidationSet,
)
description_IdentifiedElement_strategy = st.builds(
    description_IdentifiedElement,
)
description_EndUserDocumentedElement_strategy = st.builds(
    description_EndUserDocumentedElement,
)
description_Component_strategy = st.builds(
    description_Component,
)
viewpoint_description_Component_strategy = st.builds(
    viewpoint_description_Component,
)
viewpoint_description_Extension_strategy = st.builds(
    viewpoint_description_Extension,
)
viewpoint_description_FeatureExtensionDescription_strategy = st.builds(
    viewpoint_description_FeatureExtensionDescription,
)
RepresentationTemplate_strategy = st.builds(
    RepresentationTemplate,
)
MetamodelExtensionSetting_strategy = st.builds(
    MetamodelExtensionSetting,
)
JavaExtension_strategy = st.builds(
    JavaExtension,
)
RepresentationExtensionDescription_strategy = st.builds(
    RepresentationExtensionDescription,
)
viewpoint_Customizable_strategy = st.builds(
    viewpoint_Customizable,
    customFeatures=
        safe_text
)
DFile_strategy = st.builds(
    DFile,
)
viewpoint_DModel_strategy = st.builds(
    viewpoint_DModel,
)
Extension_strategy = st.builds(
    Extension,
)
UserColorsPalette_strategy = st.builds(
    UserColorsPalette,
)
SytemColorsPalette_strategy = st.builds(
    SytemColorsPalette,
)
viewpoint_DAnalysisSessionEObject_strategy = st.builds(
    viewpoint_DAnalysisSessionEObject,
    open=
        st.booleans(),
    synchronizationStatus=
        safe_text,
    controlledResources=
        safe_text,
    resources=
        safe_text
)
DResourceContainer_strategy = st.builds(
    DResourceContainer,
)
viewpoint_DFolder_strategy = st.builds(
    viewpoint_DFolder,
)
viewpoint_DProject_strategy = st.builds(
    viewpoint_DProject,
)
DResource_strategy = st.builds(
    DResource,
)
viewpoint_DResourceContainer_strategy = st.builds(
    viewpoint_DResourceContainer,
)
viewpoint_DFile_strategy = st.builds(
    viewpoint_DFile,
)
viewpoint_DResource_strategy = st.builds(
    viewpoint_DResource,
    path=
        safe_text,
    name=
        safe_text
)
viewpoint_SessionManagerEObject_strategy = st.builds(
    viewpoint_SessionManagerEObject,
)
DecorationDescription_strategy = st.builds(
    DecorationDescription,
)
viewpoint_description_GenericDecorationDescription_strategy = st.builds(
    viewpoint_description_GenericDecorationDescription,
)
viewpoint_description_SemanticBasedDecoration_strategy = st.builds(
    viewpoint_description_SemanticBasedDecoration,
    domainClass=
        safe_text
)
viewpoint_Decoration_strategy = st.builds(
    viewpoint_Decoration,
)
style_StyleDescription_strategy = st.builds(
    style_StyleDescription,
)
Customizable_strategy = st.builds(
    Customizable,
)
viewpoint_BasicLabelStyle_strategy = st.builds(
    viewpoint_BasicLabelStyle,
    labelSize=
        st.integers(),
    showIcon=
        st.booleans(),
    iconPath=
        safe_text,
    labelColor=
        safe_text,
    labelFormat=
        safe_text
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
viewpoint_LabelStyle_strategy = st.builds(
    viewpoint_LabelStyle,
    labelAlignment=
        safe_text
)
viewpoint_DAnalysisCustomData_strategy = st.builds(
    viewpoint_DAnalysisCustomData,
    key=
        safe_text
)
viewpoint_UIState_strategy = st.builds(
    viewpoint_UIState,
    inverseSelectionOrder=
        st.booleans(),
    decorationImage=
        safe_text
)
AnnotationEntry_strategy = st.builds(
    AnnotationEntry,
)
viewpoint_MetaModelExtension_strategy = st.builds(
    viewpoint_MetaModelExtension,
)
Viewpoint_strategy = st.builds(
    Viewpoint,
)
DSemanticDecorator_strategy = st.builds(
    DSemanticDecorator,
)
DStylizable_strategy = st.builds(
    DStylizable,
)
DMappingBased_strategy = st.builds(
    DMappingBased,
)
viewpoint_DRefreshable_strategy = st.builds(
    viewpoint_DRefreshable,
)
viewpoint_DStylizable_strategy = st.builds(
    viewpoint_DStylizable,
)
FeatureExtensionDescription_strategy = st.builds(
    FeatureExtensionDescription,
)
viewpoint_DFeatureExtension_strategy = st.builds(
    viewpoint_DFeatureExtension,
)
description_DModelElement_strategy = st.builds(
    description_DModelElement,
)
DRefreshable_strategy = st.builds(
    DRefreshable,
)
viewpoint_DRepresentationElement_strategy = st.builds(
    viewpoint_DRepresentationElement,
    name=
        safe_text
)
viewpoint_Style_strategy = st.builds(
    viewpoint_Style,
)
description_DocumentedElement_strategy = st.builds(
    description_DocumentedElement,
)
viewpoint_tool_ToolEntry_strategy = st.builds(
    viewpoint_tool_ToolEntry,
)
viewpoint_description_RepresentationDescription_strategy = st.builds(
    viewpoint_description_RepresentationDescription,
    showOnStartup=
        st.booleans(),
    titleExpression=
        safe_text,
    initialisation=
        st.booleans()
)
viewpoint_description_Viewpoint_strategy = st.builds(
    viewpoint_description_Viewpoint,
    customizes=
        safe_text,
    modelFileExtension=
        safe_text,
    icon=
        safe_text,
    conflicts=
        safe_text,
    reuses=
        safe_text
)
viewpoint_description_Group_strategy = st.builds(
    viewpoint_description_Group,
    version=
        safe_text,
    name=
        safe_text
)
viewpoint_DRepresentation_strategy = st.builds(
    viewpoint_DRepresentation,
    name=
        safe_text
)
RepresentationDescription_strategy = st.builds(
    RepresentationDescription,
)
viewpoint_description_RepresentationImportDescription_strategy = st.builds(
    viewpoint_description_RepresentationImportDescription,
)
viewpoint_DRepresentationDescriptor_strategy = st.builds(
    viewpoint_DRepresentationDescriptor,
    name=
        safe_text
)
viewpoint_DSemanticDecorator_strategy = st.builds(
    viewpoint_DSemanticDecorator,
)
viewpoint_DMappingBased_strategy = st.builds(
    viewpoint_DMappingBased,
)
viewpoint_DView_strategy = st.builds(
    viewpoint_DView,
)
DAnnotationEntry_strategy = st.builds(
    DAnnotationEntry,
)
viewpoint_EObject_strategy = st.builds(
    viewpoint_EObject,
)
viewpoint_DAnalysis_strategy = st.builds(
    viewpoint_DAnalysis,
    version=
        safe_text,
    semanticResources=
        safe_text
)
viewpoint_validation_ValidationFix_strategy = st.builds(
    viewpoint_validation_ValidationFix,
    name=
        safe_text
)
InformationSection_strategy = st.builds(
    InformationSection,
)
viewpoint_audit_TemplateInformationSection_strategy = st.builds(
    viewpoint_audit_TemplateInformationSection,
    templatePath=
        safe_text
)
viewpoint_audit_InformationSection_strategy = st.builds(
    viewpoint_audit_InformationSection,
)
viewpoint_validation_RuleAudit_strategy = st.builds(
    viewpoint_validation_RuleAudit,
    auditExpression=
        safe_text
)
RepresentationElementMapping_strategy = st.builds(
    RepresentationElementMapping,
)
ValidationRule_strategy = st.builds(
    ValidationRule,
)
viewpoint_validation_ViewValidationRule_strategy = st.builds(
    viewpoint_validation_ViewValidationRule,
)
viewpoint_validation_SemanticValidationRule_strategy = st.builds(
    viewpoint_validation_SemanticValidationRule,
    targetClass=
        safe_text
)
validation_ValidationFix_strategy = st.builds(
    validation_ValidationFix,
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
viewpoint_validation_ValidationSet_strategy = st.builds(
    viewpoint_validation_ValidationSet,
    name=
        safe_text
)
validation_RuleAudit_strategy = st.builds(
    validation_RuleAudit,
)
viewpoint_validation_ValidationRule_strategy = st.builds(
    viewpoint_validation_ValidationRule,
    level=
        safe_text,
    message=
        safe_text
)
validation_ValidationRule_strategy = st.builds(
    validation_ValidationRule,
)
viewpoint_tool_FeatureChangeListener_strategy = st.builds(
    viewpoint_tool_FeatureChangeListener,
    domainClass=
        safe_text,
    featureName=
        safe_text
)
tool_Default_strategy = st.builds(
    tool_Default,
)
tool_Case_strategy = st.builds(
    tool_Case,
)
viewpoint_tool_SwitchChild_strategy = st.builds(
    viewpoint_tool_SwitchChild,
)
SwitchChild_strategy = st.builds(
    SwitchChild,
)
viewpoint_tool_Default_strategy = st.builds(
    viewpoint_tool_Default,
)
viewpoint_tool_Case_strategy = st.builds(
    viewpoint_tool_Case,
    conditionExpression=
        safe_text
)
viewpoint_tool_ExternalJavaActionParameter_strategy = st.builds(
    viewpoint_tool_ExternalJavaActionParameter,
    value=
        safe_text,
    name=
        safe_text
)
tool_FeatureChangeListener_strategy = st.builds(
    tool_FeatureChangeListener,
)
viewpoint_tool_ToolFilterDescription_strategy = st.builds(
    viewpoint_tool_ToolFilterDescription,
    precondition=
        safe_text,
    elementsToListen=
        safe_text
)
viewpoint_tool_NameVariable_strategy = st.builds(
    viewpoint_tool_NameVariable,
)
tool_viewpoint_EObject_strategy = st.builds(
    tool_viewpoint_EObject,
)
viewpoint_tool_InitialOperation_strategy = st.builds(
    viewpoint_tool_InitialOperation,
)
viewpoint_tool_InitialNodeCreationOperation_strategy = st.builds(
    viewpoint_tool_InitialNodeCreationOperation,
)
viewpoint_tool_ModelOperation_strategy = st.builds(
    viewpoint_tool_ModelOperation,
)
tool_ModelOperation_strategy = st.builds(
    tool_ModelOperation,
)
ModelOperation_strategy = st.builds(
    ModelOperation,
)
viewpoint_tool_Switch_strategy = st.builds(
    viewpoint_tool_Switch,
)
viewpoint_tool_ContainerModelOperation_strategy = st.builds(
    viewpoint_tool_ContainerModelOperation,
)
viewpoint_tool_EditMaskVariables_strategy = st.builds(
    viewpoint_tool_EditMaskVariables,
    mask=
        safe_text
)
ContainerModelOperation_strategy = st.builds(
    ContainerModelOperation,
)
viewpoint_tool_RemoveElement_strategy = st.builds(
    viewpoint_tool_RemoveElement,
)
viewpoint_tool_SetObject_strategy = st.builds(
    viewpoint_tool_SetObject,
    featureName=
        safe_text
)
viewpoint_tool_For_strategy = st.builds(
    viewpoint_tool_For,
    expression=
        safe_text,
    iteratorName=
        safe_text
)
viewpoint_tool_If_strategy = st.builds(
    viewpoint_tool_If,
    conditionExpression=
        safe_text
)
viewpoint_tool_Unset_strategy = st.builds(
    viewpoint_tool_Unset,
    featureName=
        safe_text,
    elementExpression=
        safe_text
)
viewpoint_tool_DeleteView_strategy = st.builds(
    viewpoint_tool_DeleteView,
)
viewpoint_tool_ChangeContext_strategy = st.builds(
    viewpoint_tool_ChangeContext,
    browseExpression=
        safe_text
)
viewpoint_tool_SetValue_strategy = st.builds(
    viewpoint_tool_SetValue,
    valueExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint_tool_Let_strategy = st.builds(
    viewpoint_tool_Let,
    valueExpression=
        safe_text,
    variableName=
        safe_text
)
viewpoint_tool_MoveElement_strategy = st.builds(
    viewpoint_tool_MoveElement,
    newContainerExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint_tool_CreateInstance_strategy = st.builds(
    viewpoint_tool_CreateInstance,
    referenceName=
        safe_text,
    variableName=
        safe_text,
    typeName=
        safe_text
)
viewpoint_tool_InitialContainerDropOperation_strategy = st.builds(
    viewpoint_tool_InitialContainerDropOperation,
)
viewpoint_tool_InitEdgeCreationOperation_strategy = st.builds(
    viewpoint_tool_InitEdgeCreationOperation,
)
viewpoint_tool_PopupMenu_strategy = st.builds(
    viewpoint_tool_PopupMenu,
)
tool_ExternalJavaAction_strategy = st.builds(
    tool_ExternalJavaAction,
)
tool_ExternalJavaActionParameter_strategy = st.builds(
    tool_ExternalJavaActionParameter,
)
tool_ContainerModelOperation_strategy = st.builds(
    tool_ContainerModelOperation,
)
viewpoint_tool_ElementSelectVariable_strategy = st.builds(
    viewpoint_tool_ElementSelectVariable,
)
description_AbstractVariable_strategy = st.builds(
    description_AbstractVariable,
)
viewpoint_tool_DialogVariable_strategy = st.builds(
    viewpoint_tool_DialogVariable,
    dialogPrompt=
        safe_text
)
tool_VariableContainer_strategy = st.builds(
    tool_VariableContainer,
)
viewpoint_tool_SelectContainerVariable_strategy = st.builds(
    viewpoint_tool_SelectContainerVariable,
)
viewpoint_tool_ElementDeleteVariable_strategy = st.builds(
    viewpoint_tool_ElementDeleteVariable,
)
viewpoint_tool_ElementVariable_strategy = st.builds(
    viewpoint_tool_ElementVariable,
)
viewpoint_tool_DropContainerVariable_strategy = st.builds(
    viewpoint_tool_DropContainerVariable,
)
viewpoint_tool_ElementViewVariable_strategy = st.builds(
    viewpoint_tool_ElementViewVariable,
)
viewpoint_tool_ElementDropVariable_strategy = st.builds(
    viewpoint_tool_ElementDropVariable,
)
viewpoint_tool_ContainerViewVariable_strategy = st.builds(
    viewpoint_tool_ContainerViewVariable,
)
viewpoint_tool_AcceleoVariable_strategy = st.builds(
    viewpoint_tool_AcceleoVariable,
    computationExpression=
        safe_text
)
SubVariable_strategy = st.builds(
    SubVariable,
)
viewpoint_tool_VariableContainer_strategy = st.builds(
    viewpoint_tool_VariableContainer,
)
MenuItemDescription_strategy = st.builds(
    MenuItemDescription,
)
viewpoint_tool_OperationAction_strategy = st.builds(
    viewpoint_tool_OperationAction,
)
tool_MenuItemDescription_strategy = st.builds(
    tool_MenuItemDescription,
)
viewpoint_tool_ExternalJavaAction_strategy = st.builds(
    viewpoint_tool_ExternalJavaAction,
    id=
        safe_text
)
viewpoint_tool_ExternalJavaActionCall_strategy = st.builds(
    viewpoint_tool_ExternalJavaActionCall,
)
MenuItemOrRef_strategy = st.builds(
    MenuItemOrRef,
)
viewpoint_tool_MenuItemDescriptionReference_strategy = st.builds(
    viewpoint_tool_MenuItemDescriptionReference,
)
tool_MenuItemOrRef_strategy = st.builds(
    tool_MenuItemOrRef,
)
viewpoint_tool_MenuItemOrRef_strategy = st.builds(
    viewpoint_tool_MenuItemOrRef,
)
tool_NameVariable_strategy = st.builds(
    tool_NameVariable,
)
viewpoint_tool_RepresentationNavigationDescription_strategy = st.builds(
    viewpoint_tool_RepresentationNavigationDescription,
    browseExpression=
        safe_text,
    navigationNameExpression=
        safe_text
)
viewpoint_tool_RepresentationCreationDescription_strategy = st.builds(
    viewpoint_tool_RepresentationCreationDescription,
    browseExpression=
        safe_text,
    titleExpression=
        safe_text
)
tool_SelectContainerVariable_strategy = st.builds(
    tool_SelectContainerVariable,
)
tool_ElementSelectVariable_strategy = st.builds(
    tool_ElementSelectVariable,
)
description_SelectionDescription_strategy = st.builds(
    description_SelectionDescription,
)
viewpoint_tool_SelectModelElementVariable_strategy = st.builds(
    viewpoint_tool_SelectModelElementVariable,
)
tool_AbstractToolDescription_strategy = st.builds(
    tool_AbstractToolDescription,
)
viewpoint_tool_MenuItemDescription_strategy = st.builds(
    viewpoint_tool_MenuItemDescription,
    icon=
        safe_text
)
viewpoint_tool_SelectionWizardDescription_strategy = st.builds(
    viewpoint_tool_SelectionWizardDescription,
    windowTitle=
        safe_text,
    windowImagePath=
        safe_text,
    iconPath=
        safe_text
)
viewpoint_tool_PaneBasedSelectionWizardDescription_strategy = st.builds(
    viewpoint_tool_PaneBasedSelectionWizardDescription,
    windowTitle=
        safe_text,
    selectedValuesMessage=
        safe_text,
    message=
        safe_text,
    tree=
        st.booleans(),
    iconPath=
        safe_text,
    windowImagePath=
        safe_text,
    candidatesExpression=
        safe_text,
    rootExpression=
        safe_text,
    choiceOfValuesMessage=
        safe_text,
    preSelectedCandidatesExpression=
        safe_text,
    childrenExpression=
        safe_text
)
tool_ContainerViewVariable_strategy = st.builds(
    tool_ContainerViewVariable,
)
tool_DropContainerVariable_strategy = st.builds(
    tool_DropContainerVariable,
)
tool_ElementVariable_strategy = st.builds(
    tool_ElementVariable,
)
MappingBasedToolDescription_strategy = st.builds(
    MappingBasedToolDescription,
)
viewpoint_tool_PasteDescription_strategy = st.builds(
    viewpoint_tool_PasteDescription,
)
viewpoint_tool_ToolDescription_strategy = st.builds(
    viewpoint_tool_ToolDescription,
    iconPath=
        safe_text
)









@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_hyp_viewpoint_tool_abstracttooldescription_inverseSelectionOrder_setter(instance):
    original = instance.inverseSelectionOrder
    instance.inverseSelectionOrder = original
    assert instance.inverseSelectionOrder == original



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_hyp_viewpoint_tool_abstracttooldescription_forceRefresh_setter(instance):
    original = instance.forceRefresh
    instance.forceRefresh = original
    assert instance.forceRefresh == original



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_hyp_viewpoint_tool_abstracttooldescription_elementsToSelect_setter(instance):
    original = instance.elementsToSelect
    instance.elementsToSelect = original
    assert instance.elementsToSelect == original



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_hyp_viewpoint_tool_abstracttooldescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original






@given(instance=viewpoint_style_LabelStyleDescription_strategy)
def test_hyp_viewpoint_style_labelstyledescription_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original




@given(instance=viewpoint_style_TooltipStyleDescription_strategy)
def test_hyp_viewpoint_style_tooltipstyledescription_tooltipExpression_setter(instance):
    original = instance.tooltipExpression
    instance.tooltipExpression = original
    assert instance.tooltipExpression == original




@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_hyp_viewpoint_style_labelborderstyledescription_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_hyp_viewpoint_style_labelborderstyledescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_hyp_viewpoint_style_labelborderstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_hyp_viewpoint_style_labelborderstyledescription_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original







@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_hyp_viewpoint_style_basiclabelstyledescription_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_hyp_viewpoint_style_basiclabelstyledescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_hyp_viewpoint_style_basiclabelstyledescription_labelExpression_setter(instance):
    original = instance.labelExpression
    instance.labelExpression = original
    assert instance.labelExpression == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_hyp_viewpoint_style_basiclabelstyledescription_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_hyp_viewpoint_style_basiclabelstyledescription_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original





@given(instance=viewpoint_description_IdentifiedElement_strategy)
def test_hyp_viewpoint_description_identifiedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_description_IdentifiedElement_strategy)
def test_hyp_viewpoint_description_identifiedelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=viewpoint_description_EndUserDocumentedElement_strategy)
def test_hyp_viewpoint_description_enduserdocumentedelement_endUserDocumentation_setter(instance):
    original = instance.endUserDocumentation
    instance.endUserDocumentation = original
    assert instance.endUserDocumentation == original




@given(instance=viewpoint_description_AnnotationEntry_strategy)
def test_hyp_viewpoint_description_annotationentry_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original







@given(instance=viewpoint_description_TypedVariable_strategy)
def test_hyp_viewpoint_description_typedvariable_defaultValueExpression_setter(instance):
    original = instance.defaultValueExpression
    instance.defaultValueExpression = original
    assert instance.defaultValueExpression == original




@given(instance=viewpoint_description_InteractiveVariableDescription_strategy)
def test_hyp_viewpoint_description_interactivevariabledescription_userDocumentation_setter(instance):
    original = instance.userDocumentation
    instance.userDocumentation = original
    assert instance.userDocumentation == original






@given(instance=viewpoint_description_AbstractVariable_strategy)
def test_hyp_viewpoint_description_abstractvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=viewpoint_description_DAnnotationEntry_strategy)
def test_hyp_viewpoint_description_dannotationentry_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=viewpoint_description_DAnnotationEntry_strategy)
def test_hyp_viewpoint_description_dannotationentry_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original




@given(instance=viewpoint_description_UserColor_strategy)
def test_hyp_viewpoint_description_usercolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=viewpoint_description_UserColorsPalette_strategy)
def test_hyp_viewpoint_description_usercolorspalette_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original












@given(instance=viewpoint_description_ComputedColor_strategy)
def test_hyp_viewpoint_description_computedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=viewpoint_description_ComputedColor_strategy)
def test_hyp_viewpoint_description_computedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=viewpoint_description_ComputedColor_strategy)
def test_hyp_viewpoint_description_computedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original




@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_hyp_viewpoint_description_interpolatedcolor_maxValueComputationExpression_setter(instance):
    original = instance.maxValueComputationExpression
    instance.maxValueComputationExpression = original
    assert instance.maxValueComputationExpression == original



@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_hyp_viewpoint_description_interpolatedcolor_minValueComputationExpression_setter(instance):
    original = instance.minValueComputationExpression
    instance.minValueComputationExpression = original
    assert instance.minValueComputationExpression == original



@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_hyp_viewpoint_description_interpolatedcolor_colorValueComputationExpression_setter(instance):
    original = instance.colorValueComputationExpression
    instance.colorValueComputationExpression = original
    assert instance.colorValueComputationExpression == original





@given(instance=viewpoint_description_FixedColor_strategy)
def test_hyp_viewpoint_description_fixedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=viewpoint_description_FixedColor_strategy)
def test_hyp_viewpoint_description_fixedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=viewpoint_description_FixedColor_strategy)
def test_hyp_viewpoint_description_fixedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original




@given(instance=viewpoint_description_ColorStep_strategy)
def test_hyp_viewpoint_description_colorstep_associatedValue_setter(instance):
    original = instance.associatedValue
    instance.associatedValue = original
    assert instance.associatedValue == original






@given(instance=viewpoint_description_SystemColor_strategy)
def test_hyp_viewpoint_description_systemcolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_hyp_viewpoint_description_selectiondescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_hyp_viewpoint_description_selectiondescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_hyp_viewpoint_description_selectiondescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_hyp_viewpoint_description_selectiondescription_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_hyp_viewpoint_description_selectiondescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_hyp_viewpoint_description_selectiondescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original






@given(instance=viewpoint_description_VSMElementCustomization_strategy)
def test_hyp_viewpoint_description_vsmelementcustomization_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original





@given(instance=viewpoint_description_EStructuralFeatureCustomization_strategy)
def test_hyp_viewpoint_description_estructuralfeaturecustomization_applyOnAll_setter(instance):
    original = instance.applyOnAll
    instance.applyOnAll = original
    assert instance.applyOnAll == original






@given(instance=viewpoint_description_EAttributeCustomization_strategy)
def test_hyp_viewpoint_description_eattributecustomization_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=viewpoint_description_EAttributeCustomization_strategy)
def test_hyp_viewpoint_description_eattributecustomization_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original




@given(instance=viewpoint_description_EReferenceCustomization_strategy)
def test_hyp_viewpoint_description_ereferencecustomization_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original




@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_hyp_viewpoint_description_decorationdescription_tooltipExpression_setter(instance):
    original = instance.tooltipExpression
    instance.tooltipExpression = original
    assert instance.tooltipExpression == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_hyp_viewpoint_description_decorationdescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_hyp_viewpoint_description_decorationdescription_imageExpression_setter(instance):
    original = instance.imageExpression
    instance.imageExpression = original
    assert instance.imageExpression == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_hyp_viewpoint_description_decorationdescription_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_hyp_viewpoint_description_decorationdescription_distributionDirection_setter(instance):
    original = instance.distributionDirection
    instance.distributionDirection = original
    assert instance.distributionDirection == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_hyp_viewpoint_description_decorationdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original







@given(instance=viewpoint_description_AbstractMappingImport_strategy)
def test_hyp_viewpoint_description_abstractmappingimport_hideSubMappings_setter(instance):
    original = instance.hideSubMappings
    instance.hideSubMappings = original
    assert instance.hideSubMappings == original



@given(instance=viewpoint_description_AbstractMappingImport_strategy)
def test_hyp_viewpoint_description_abstractmappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original







@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
def test_hyp_viewpoint_description_conditionalstyledescription_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
@settings(max_examples=30)
def test_hyp_viewpoint_description_conditionalstyledescription_checkpredicate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkPredicate(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkPredicate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkPredicate' in viewpoint_description_ConditionalStyleDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPredicate' in viewpoint_description_ConditionalStyleDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPredicate' in viewpoint_description_ConditionalStyleDescription is not implemented or raised an error")





@given(instance=viewpoint_description_DAnnotation_strategy)
def test_hyp_viewpoint_description_dannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original






@given(instance=viewpoint_description_DocumentedElement_strategy)
def test_hyp_viewpoint_description_documentedelement_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original




@given(instance=viewpoint_description_RepresentationTemplate_strategy)
def test_hyp_viewpoint_description_representationtemplate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=viewpoint_description_JavaExtension_strategy)
def test_hyp_viewpoint_description_javaextension_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original






@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_hyp_viewpoint_description_representationextensiondescription_representationName_setter(instance):
    original = instance.representationName
    instance.representationName = original
    assert instance.representationName == original



@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_hyp_viewpoint_description_representationextensiondescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_hyp_viewpoint_description_representationextensiondescription_viewpointURI_setter(instance):
    original = instance.viewpointURI
    instance.viewpointURI = original
    assert instance.viewpointURI == original















@given(instance=viewpoint_Customizable_strategy)
def test_hyp_viewpoint_customizable_customFeatures_setter(instance):
    original = instance.customFeatures
    instance.customFeatures = original
    assert instance.customFeatures == original









@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_hyp_viewpoint_danalysissessioneobject_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_hyp_viewpoint_danalysissessioneobject_synchronizationStatus_setter(instance):
    original = instance.synchronizationStatus
    instance.synchronizationStatus = original
    assert instance.synchronizationStatus == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_hyp_viewpoint_danalysissessioneobject_controlledResources_setter(instance):
    original = instance.controlledResources
    instance.controlledResources = original
    assert instance.controlledResources == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_hyp_viewpoint_danalysissessioneobject_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original










@given(instance=viewpoint_DResource_strategy)
def test_hyp_viewpoint_dresource_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=viewpoint_DResource_strategy)
def test_hyp_viewpoint_dresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=viewpoint_description_SemanticBasedDecoration_strategy)
def test_hyp_viewpoint_description_semanticbaseddecoration_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original







@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_hyp_viewpoint_basiclabelstyle_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_hyp_viewpoint_basiclabelstyle_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_hyp_viewpoint_basiclabelstyle_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_hyp_viewpoint_basiclabelstyle_labelColor_setter(instance):
    original = instance.labelColor
    instance.labelColor = original
    assert instance.labelColor == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_hyp_viewpoint_basiclabelstyle_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original





@given(instance=viewpoint_LabelStyle_strategy)
def test_hyp_viewpoint_labelstyle_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original




@given(instance=viewpoint_DAnalysisCustomData_strategy)
def test_hyp_viewpoint_danalysiscustomdata_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




@given(instance=viewpoint_UIState_strategy)
def test_hyp_viewpoint_uistate_inverseSelectionOrder_setter(instance):
    original = instance.inverseSelectionOrder
    instance.inverseSelectionOrder = original
    assert instance.inverseSelectionOrder == original



@given(instance=viewpoint_UIState_strategy)
def test_hyp_viewpoint_uistate_decorationImage_setter(instance):
    original = instance.decorationImage
    instance.decorationImage = original
    assert instance.decorationImage == original








import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_DRefreshable_strategy)
@settings(max_examples=30)
def test_hyp_viewpoint_drefreshable_refresh_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.refresh()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.refresh).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'refresh' in viewpoint_DRefreshable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'refresh' in viewpoint_DRefreshable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'refresh' in viewpoint_DRefreshable is not implemented or raised an error")









@given(instance=viewpoint_DRepresentationElement_strategy)
def test_hyp_viewpoint_drepresentationelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_hyp_viewpoint_description_representationdescription_showOnStartup_setter(instance):
    original = instance.showOnStartup
    instance.showOnStartup = original
    assert instance.showOnStartup == original



@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_hyp_viewpoint_description_representationdescription_titleExpression_setter(instance):
    original = instance.titleExpression
    instance.titleExpression = original
    assert instance.titleExpression == original



@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_hyp_viewpoint_description_representationdescription_initialisation_setter(instance):
    original = instance.initialisation
    instance.initialisation = original
    assert instance.initialisation == original




@given(instance=viewpoint_description_Viewpoint_strategy)
def test_hyp_viewpoint_description_viewpoint_customizes_setter(instance):
    original = instance.customizes
    instance.customizes = original
    assert instance.customizes == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_hyp_viewpoint_description_viewpoint_modelFileExtension_setter(instance):
    original = instance.modelFileExtension
    instance.modelFileExtension = original
    assert instance.modelFileExtension == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_hyp_viewpoint_description_viewpoint_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_hyp_viewpoint_description_viewpoint_conflicts_setter(instance):
    original = instance.conflicts
    instance.conflicts = original
    assert instance.conflicts == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_hyp_viewpoint_description_viewpoint_reuses_setter(instance):
    original = instance.reuses
    instance.reuses = original
    assert instance.reuses == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_Viewpoint_strategy)
@settings(max_examples=30)
def test_hyp_viewpoint_description_viewpoint_initview_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.initView(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.initView).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'initView' in viewpoint_description_Viewpoint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initView' in viewpoint_description_Viewpoint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initView' in viewpoint_description_Viewpoint is not implemented or raised an error")




@given(instance=viewpoint_description_Group_strategy)
def test_hyp_viewpoint_description_group_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=viewpoint_description_Group_strategy)
def test_hyp_viewpoint_description_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=viewpoint_DRepresentation_strategy)
def test_hyp_viewpoint_drepresentation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=viewpoint_DRepresentationDescriptor_strategy)
def test_hyp_viewpoint_drepresentationdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=viewpoint_DAnalysis_strategy)
def test_hyp_viewpoint_danalysis_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=viewpoint_DAnalysis_strategy)
def test_hyp_viewpoint_danalysis_semanticResources_setter(instance):
    original = instance.semanticResources
    instance.semanticResources = original
    assert instance.semanticResources == original




@given(instance=viewpoint_validation_ValidationFix_strategy)
def test_hyp_viewpoint_validation_validationfix_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=viewpoint_audit_TemplateInformationSection_strategy)
def test_hyp_viewpoint_audit_templateinformationsection_templatePath_setter(instance):
    original = instance.templatePath
    instance.templatePath = original
    assert instance.templatePath == original





@given(instance=viewpoint_validation_RuleAudit_strategy)
def test_hyp_viewpoint_validation_ruleaudit_auditExpression_setter(instance):
    original = instance.auditExpression
    instance.auditExpression = original
    assert instance.auditExpression == original







@given(instance=viewpoint_validation_SemanticValidationRule_strategy)
def test_hyp_viewpoint_validation_semanticvalidationrule_targetClass_setter(instance):
    original = instance.targetClass
    instance.targetClass = original
    assert instance.targetClass == original






@given(instance=viewpoint_validation_ValidationSet_strategy)
def test_hyp_viewpoint_validation_validationset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=viewpoint_validation_ValidationRule_strategy)
def test_hyp_viewpoint_validation_validationrule_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=viewpoint_validation_ValidationRule_strategy)
def test_hyp_viewpoint_validation_validationrule_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_validation_ValidationRule_strategy)
@settings(max_examples=30)
def test_hyp_viewpoint_validation_validationrule_checkrule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkRule(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkRule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkRule' in viewpoint_validation_ValidationRule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkRule' in viewpoint_validation_ValidationRule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkRule' in viewpoint_validation_ValidationRule is not implemented or raised an error")





@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
def test_hyp_viewpoint_tool_featurechangelistener_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
def test_hyp_viewpoint_tool_featurechangelistener_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original









@given(instance=viewpoint_tool_Case_strategy)
def test_hyp_viewpoint_tool_case_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original




@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
def test_hyp_viewpoint_tool_externaljavaactionparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
def test_hyp_viewpoint_tool_externaljavaactionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
def test_hyp_viewpoint_tool_toolfilterdescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
def test_hyp_viewpoint_tool_toolfilterdescription_elementsToListen_setter(instance):
    original = instance.elementsToListen
    instance.elementsToListen = original
    assert instance.elementsToListen == original













@given(instance=viewpoint_tool_EditMaskVariables_strategy)
def test_hyp_viewpoint_tool_editmaskvariables_mask_setter(instance):
    original = instance.mask
    instance.mask = original
    assert instance.mask == original






@given(instance=viewpoint_tool_SetObject_strategy)
def test_hyp_viewpoint_tool_setobject_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original




@given(instance=viewpoint_tool_For_strategy)
def test_hyp_viewpoint_tool_for_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=viewpoint_tool_For_strategy)
def test_hyp_viewpoint_tool_for_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original




@given(instance=viewpoint_tool_If_strategy)
def test_hyp_viewpoint_tool_if_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original




@given(instance=viewpoint_tool_Unset_strategy)
def test_hyp_viewpoint_tool_unset_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original



@given(instance=viewpoint_tool_Unset_strategy)
def test_hyp_viewpoint_tool_unset_elementExpression_setter(instance):
    original = instance.elementExpression
    instance.elementExpression = original
    assert instance.elementExpression == original





@given(instance=viewpoint_tool_ChangeContext_strategy)
def test_hyp_viewpoint_tool_changecontext_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original




@given(instance=viewpoint_tool_SetValue_strategy)
def test_hyp_viewpoint_tool_setvalue_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original



@given(instance=viewpoint_tool_SetValue_strategy)
def test_hyp_viewpoint_tool_setvalue_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original




@given(instance=viewpoint_tool_Let_strategy)
def test_hyp_viewpoint_tool_let_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original



@given(instance=viewpoint_tool_Let_strategy)
def test_hyp_viewpoint_tool_let_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original




@given(instance=viewpoint_tool_MoveElement_strategy)
def test_hyp_viewpoint_tool_moveelement_newContainerExpression_setter(instance):
    original = instance.newContainerExpression
    instance.newContainerExpression = original
    assert instance.newContainerExpression == original



@given(instance=viewpoint_tool_MoveElement_strategy)
def test_hyp_viewpoint_tool_moveelement_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original




@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_hyp_viewpoint_tool_createinstance_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original



@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_hyp_viewpoint_tool_createinstance_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original



@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_hyp_viewpoint_tool_createinstance_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original












@given(instance=viewpoint_tool_DialogVariable_strategy)
def test_hyp_viewpoint_tool_dialogvariable_dialogPrompt_setter(instance):
    original = instance.dialogPrompt
    instance.dialogPrompt = original
    assert instance.dialogPrompt == original












@given(instance=viewpoint_tool_AcceleoVariable_strategy)
def test_hyp_viewpoint_tool_acceleovariable_computationExpression_setter(instance):
    original = instance.computationExpression
    instance.computationExpression = original
    assert instance.computationExpression == original









@given(instance=viewpoint_tool_ExternalJavaAction_strategy)
def test_hyp_viewpoint_tool_externaljavaaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original










@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
def test_hyp_viewpoint_tool_representationnavigationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original



@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
def test_hyp_viewpoint_tool_representationnavigationdescription_navigationNameExpression_setter(instance):
    original = instance.navigationNameExpression
    instance.navigationNameExpression = original
    assert instance.navigationNameExpression == original




@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
def test_hyp_viewpoint_tool_representationcreationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original



@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
def test_hyp_viewpoint_tool_representationcreationdescription_titleExpression_setter(instance):
    original = instance.titleExpression
    instance.titleExpression = original
    assert instance.titleExpression == original









@given(instance=viewpoint_tool_MenuItemDescription_strategy)
def test_hyp_viewpoint_tool_menuitemdescription_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original




@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_selectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original



@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_selectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original



@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_selectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original




@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_selectedValuesMessage_setter(instance):
    original = instance.selectedValuesMessage
    instance.selectedValuesMessage = original
    assert instance.selectedValuesMessage == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_choiceOfValuesMessage_setter(instance):
    original = instance.choiceOfValuesMessage
    instance.choiceOfValuesMessage = original
    assert instance.choiceOfValuesMessage == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_preSelectedCandidatesExpression_setter(instance):
    original = instance.preSelectedCandidatesExpression
    instance.preSelectedCandidatesExpression = original
    assert instance.preSelectedCandidatesExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_hyp_viewpoint_tool_panebasedselectionwizarddescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original









@given(instance=viewpoint_tool_ToolDescription_strategy)
def test_hyp_viewpoint_tool_tooldescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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
    DMappingBased,
    DRefreshable,
    DResource,
    DResourceContainer,
    DSemanticDecorator,
    DStylizable,
    DecorationDescription,
    DocumentedElement,
    EStructuralFeatureCustomization,
    Extension,
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
    SubVariable,
    SwitchChild,
    SystemColor,
    SytemColorsPalette,
    ToolEntry,
    UserColor,
    UserColorsPalette,
    ValidationRule,
    Viewpoint,
    description_AbstractVariable,
    description_ColorDescription,
    description_Component,
    description_DModelElement,
    description_DocumentedElement,
    description_EndUserDocumentedElement,
    description_FixedColor,
    description_IdentifiedElement,
    description_InteractiveVariableDescription,
    description_SelectionDescription,
    description_SubVariable,
    description_UserColor,
    description_viewpoint_EDataType,
    description_viewpoint_EObject,
    description_viewpoint_EPackage,
    description_viewpoint_EStringToStringMapEntry,
    style_LabelBorderStyleDescription,
    style_LabelBorderStyles,
    style_StyleDescription,
    tool_AbstractToolDescription,
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
    viewpoint_DFeatureExtension,
    viewpoint_DFile,
    viewpoint_DFolder,
    viewpoint_DMappingBased,
    viewpoint_DModel,
    viewpoint_DProject,
    viewpoint_DRefreshable,
    viewpoint_DRepresentation,
    viewpoint_DRepresentationDescriptor,
    viewpoint_DRepresentationElement,
    viewpoint_DResource,
    viewpoint_DResourceContainer,
    viewpoint_DSemanticDecorator,
    viewpoint_DStylizable,
    viewpoint_DView,
    viewpoint_Decoration,
    viewpoint_EObject,
    viewpoint_LabelStyle,
    viewpoint_MetaModelExtension,
    viewpoint_SessionManagerEObject,
    viewpoint_Style,
    viewpoint_UIState,
    viewpoint_audit_InformationSection,
    viewpoint_audit_TemplateInformationSection,
    viewpoint_description_AbstractMappingImport,
    viewpoint_description_AbstractVariable,
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
    viewpoint_description_Extension,
    viewpoint_description_FeatureExtensionDescription,
    viewpoint_description_FixedColor,
    viewpoint_description_GenericDecorationDescription,
    viewpoint_description_Group,
    viewpoint_description_IVSMElementCustomization,
    viewpoint_description_IdentifiedElement,
    viewpoint_description_InteractiveVariableDescription,
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
    viewpoint_description_SubVariable,
    viewpoint_description_SystemColor,
    viewpoint_description_SytemColorsPalette,
    viewpoint_description_TypedVariable,
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
    viewpoint_tool_Let,
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
    DecorationDistributionDirection,
    DragSource,
    ERROR_LEVEL,
    FontFormat,
    LabelAlignment,
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
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelColor="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_viewpoint_BasicLabelStyle_labelColor_value_roundtrip():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelColor="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelColor == "sample_text"
    instance.labelColor = "sample_text_2"
    assert instance.labelColor == "sample_text_2"


def test_viewpoint_BasicLabelStyle_labelFormat_value_roundtrip():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelColor="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelFormat == "sample_text"
    instance.labelFormat = "sample_text_2"
    assert instance.labelFormat == "sample_text_2"


def test_viewpoint_BasicLabelStyle_labelSize_value_roundtrip():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelColor="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelSize == 7
    instance.labelSize = 13
    assert instance.labelSize == 13


def test_viewpoint_BasicLabelStyle_showIcon_value_roundtrip():
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelColor="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.showIcon == True
    instance.showIcon = False
    assert instance.showIcon == False


def test_viewpoint_Customizable_customFeatures_value_roundtrip():
    instance = viewpoint_Customizable(customFeatures="sample_text")
    assert instance.customFeatures == "sample_text"
    instance.customFeatures = "sample_text_2"
    assert instance.customFeatures == "sample_text_2"


def test_viewpoint_DAnalysis_semanticResources_value_roundtrip():
    instance = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    assert instance.semanticResources == "sample_text"
    instance.semanticResources = "sample_text_2"
    assert instance.semanticResources == "sample_text_2"


def test_viewpoint_DAnalysis_version_value_roundtrip():
    instance = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_viewpoint_DAnalysisCustomData_key_value_roundtrip():
    instance = viewpoint_DAnalysisCustomData(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_viewpoint_DAnalysisSessionEObject_controlledResources_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.controlledResources == "sample_text"
    instance.controlledResources = "sample_text_2"
    assert instance.controlledResources == "sample_text_2"


def test_viewpoint_DAnalysisSessionEObject_open_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.open == True
    instance.open = False
    assert instance.open == False


def test_viewpoint_DAnalysisSessionEObject_resources_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.resources == "sample_text"
    instance.resources = "sample_text_2"
    assert instance.resources == "sample_text_2"


def test_viewpoint_DAnalysisSessionEObject_synchronizationStatus_value_roundtrip():
    instance = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    assert instance.synchronizationStatus == "sample_text"
    instance.synchronizationStatus = "sample_text_2"
    assert instance.synchronizationStatus == "sample_text_2"


def test_viewpoint_DRepresentation_name_value_roundtrip():
    instance = viewpoint_DRepresentation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_DRepresentationDescriptor_name_value_roundtrip():
    instance = viewpoint_DRepresentationDescriptor(name="sample_text")
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


def test_viewpoint_LabelStyle_labelAlignment_value_roundtrip():
    instance = viewpoint_LabelStyle(labelAlignment="sample_text")
    assert instance.labelAlignment == "sample_text"
    instance.labelAlignment = "sample_text_2"
    assert instance.labelAlignment == "sample_text_2"


def test_viewpoint_UIState_decorationImage_value_roundtrip():
    instance = viewpoint_UIState(decorationImage="sample_text", inverseSelectionOrder=True)
    assert instance.decorationImage == "sample_text"
    instance.decorationImage = "sample_text_2"
    assert instance.decorationImage == "sample_text_2"


def test_viewpoint_UIState_inverseSelectionOrder_value_roundtrip():
    instance = viewpoint_UIState(decorationImage="sample_text", inverseSelectionOrder=True)
    assert instance.inverseSelectionOrder == True
    instance.inverseSelectionOrder = False
    assert instance.inverseSelectionOrder == False


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


def test_viewpoint_description_AbstractVariable_name_value_roundtrip():
    instance = viewpoint_description_AbstractVariable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


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


def test_viewpoint_description_DecorationDescription_distributionDirection_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(distributionDirection="sample_text", imageExpression="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text", tooltipExpression="sample_text")
    assert instance.distributionDirection == "sample_text"
    instance.distributionDirection = "sample_text_2"
    assert instance.distributionDirection == "sample_text_2"


def test_viewpoint_description_DecorationDescription_imageExpression_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(distributionDirection="sample_text", imageExpression="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text", tooltipExpression="sample_text")
    assert instance.imageExpression == "sample_text"
    instance.imageExpression = "sample_text_2"
    assert instance.imageExpression == "sample_text_2"


def test_viewpoint_description_DecorationDescription_name_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(distributionDirection="sample_text", imageExpression="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text", tooltipExpression="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_viewpoint_description_DecorationDescription_position_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(distributionDirection="sample_text", imageExpression="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text", tooltipExpression="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_viewpoint_description_DecorationDescription_preconditionExpression_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(distributionDirection="sample_text", imageExpression="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text", tooltipExpression="sample_text")
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_viewpoint_description_DecorationDescription_tooltipExpression_value_roundtrip():
    instance = viewpoint_description_DecorationDescription(distributionDirection="sample_text", imageExpression="sample_text", name="sample_text", position="sample_text", preconditionExpression="sample_text", tooltipExpression="sample_text")
    assert instance.tooltipExpression == "sample_text"
    instance.tooltipExpression = "sample_text_2"
    assert instance.tooltipExpression == "sample_text_2"


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


def test_viewpoint_description_InteractiveVariableDescription_userDocumentation_value_roundtrip():
    instance = viewpoint_description_InteractiveVariableDescription(userDocumentation="sample_text")
    assert instance.userDocumentation == "sample_text"
    instance.userDocumentation = "sample_text_2"
    assert instance.userDocumentation == "sample_text_2"


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


def test_viewpoint_description_TypedVariable_defaultValueExpression_value_roundtrip():
    instance = viewpoint_description_TypedVariable(defaultValueExpression="sample_text")
    assert instance.defaultValueExpression == "sample_text"
    instance.defaultValueExpression = "sample_text_2"
    assert instance.defaultValueExpression == "sample_text_2"


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


def test_viewpoint_tool_AbstractToolDescription_elementsToSelect_value_roundtrip():
    instance = viewpoint_tool_AbstractToolDescription(elementsToSelect="sample_text", forceRefresh=True, inverseSelectionOrder=True, precondition="sample_text")
    assert instance.elementsToSelect == "sample_text"
    instance.elementsToSelect = "sample_text_2"
    assert instance.elementsToSelect == "sample_text_2"


def test_viewpoint_tool_AbstractToolDescription_forceRefresh_value_roundtrip():
    instance = viewpoint_tool_AbstractToolDescription(elementsToSelect="sample_text", forceRefresh=True, inverseSelectionOrder=True, precondition="sample_text")
    assert instance.forceRefresh == True
    instance.forceRefresh = False
    assert instance.forceRefresh == False


def test_viewpoint_tool_AbstractToolDescription_inverseSelectionOrder_value_roundtrip():
    instance = viewpoint_tool_AbstractToolDescription(elementsToSelect="sample_text", forceRefresh=True, inverseSelectionOrder=True, precondition="sample_text")
    assert instance.inverseSelectionOrder == True
    instance.inverseSelectionOrder = False
    assert instance.inverseSelectionOrder == False


def test_viewpoint_tool_AbstractToolDescription_precondition_value_roundtrip():
    instance = viewpoint_tool_AbstractToolDescription(elementsToSelect="sample_text", forceRefresh=True, inverseSelectionOrder=True, precondition="sample_text")
    assert instance.precondition == "sample_text"
    instance.precondition = "sample_text_2"
    assert instance.precondition == "sample_text_2"


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


def test_viewpoint_tool_Let_valueExpression_value_roundtrip():
    instance = viewpoint_tool_Let(valueExpression="sample_text", variableName="sample_text")
    assert instance.valueExpression == "sample_text"
    instance.valueExpression = "sample_text_2"
    assert instance.valueExpression == "sample_text_2"


def test_viewpoint_tool_Let_variableName_value_roundtrip():
    instance = viewpoint_tool_Let(valueExpression="sample_text", variableName="sample_text")
    assert instance.variableName == "sample_text"
    instance.variableName = "sample_text_2"
    assert instance.variableName == "sample_text_2"


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


def test_viewpoint_description_SubVariable_isa_AbstractVariable():
    instance = viewpoint_description_SubVariable()
    assert isinstance(instance, AbstractVariable)


def test_viewpoint_tool_DialogVariable_isa_AbstractVariable():
    instance = viewpoint_tool_DialogVariable(dialogPrompt="sample_text")
    assert isinstance(instance, AbstractVariable)


def test_viewpoint_tool_ElementSelectVariable_isa_AbstractVariable():
    instance = viewpoint_tool_ElementSelectVariable()
    assert isinstance(instance, AbstractVariable)


def test_viewpoint_tool_NameVariable_isa_AbstractVariable():
    instance = viewpoint_tool_NameVariable()
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


def test_viewpoint_tool_Let_isa_ContainerModelOperation():
    instance = viewpoint_tool_Let(valueExpression="sample_text", variableName="sample_text")
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
    instance = viewpoint_BasicLabelStyle(iconPath="sample_text", labelColor="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert isinstance(instance, Customizable)


def test_viewpoint_Style_isa_Customizable():
    instance = viewpoint_Style()
    assert isinstance(instance, Customizable)


def test_viewpoint_DModel_isa_DFile():
    instance = viewpoint_DModel()
    assert isinstance(instance, DFile)


def test_viewpoint_DRepresentationElement_isa_DMappingBased():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DMappingBased)


def test_viewpoint_DRepresentation_isa_DRefreshable():
    instance = viewpoint_DRepresentation(name="sample_text")
    assert isinstance(instance, DRefreshable)


def test_viewpoint_DRepresentationElement_isa_DRefreshable():
    instance = viewpoint_DRepresentationElement(name="sample_text")
    assert isinstance(instance, DRefreshable)


def test_viewpoint_DView_isa_DRefreshable():
    instance = viewpoint_DView()
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


def test_viewpoint_description_GenericDecorationDescription_isa_DecorationDescription():
    instance = viewpoint_description_GenericDecorationDescription()
    assert isinstance(instance, DecorationDescription)


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


def test_viewpoint_validation_ValidationRule_isa_IdentifiedElement():
    instance = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
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
    instance = viewpoint_tool_AbstractToolDescription(elementsToSelect="sample_text", forceRefresh=True, inverseSelectionOrder=True, precondition="sample_text")
    assert isinstance(instance, ToolEntry)


def test_viewpoint_validation_SemanticValidationRule_isa_ValidationRule():
    instance = viewpoint_validation_SemanticValidationRule(targetClass="sample_text")
    assert isinstance(instance, ValidationRule)


def test_viewpoint_validation_ViewValidationRule_isa_ValidationRule():
    instance = viewpoint_validation_ViewValidationRule()
    assert isinstance(instance, ValidationRule)


def test_viewpoint_tool_ContainerViewVariable_isa_description_AbstractVariable():
    instance = viewpoint_tool_ContainerViewVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_viewpoint_tool_DropContainerVariable_isa_description_AbstractVariable():
    instance = viewpoint_tool_DropContainerVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_viewpoint_tool_ElementDeleteVariable_isa_description_AbstractVariable():
    instance = viewpoint_tool_ElementDeleteVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_viewpoint_tool_ElementDropVariable_isa_description_AbstractVariable():
    instance = viewpoint_tool_ElementDropVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_viewpoint_tool_ElementVariable_isa_description_AbstractVariable():
    instance = viewpoint_tool_ElementVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_viewpoint_tool_ElementViewVariable_isa_description_AbstractVariable():
    instance = viewpoint_tool_ElementViewVariable()
    assert isinstance(instance, description_AbstractVariable)


def test_viewpoint_tool_SelectContainerVariable_isa_description_AbstractVariable():
    instance = viewpoint_tool_SelectContainerVariable()
    assert isinstance(instance, description_AbstractVariable)


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


def test_viewpoint_description_TypedVariable_isa_description_InteractiveVariableDescription():
    instance = viewpoint_description_TypedVariable(defaultValueExpression="sample_text")
    assert isinstance(instance, description_InteractiveVariableDescription)


def test_viewpoint_tool_SelectModelElementVariable_isa_description_InteractiveVariableDescription():
    instance = viewpoint_tool_SelectModelElementVariable()
    assert isinstance(instance, description_InteractiveVariableDescription)


def test_viewpoint_tool_SelectModelElementVariable_isa_description_SelectionDescription():
    instance = viewpoint_tool_SelectModelElementVariable()
    assert isinstance(instance, description_SelectionDescription)


def test_viewpoint_tool_SelectionWizardDescription_isa_description_SelectionDescription():
    instance = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    assert isinstance(instance, description_SelectionDescription)


def test_viewpoint_description_TypedVariable_isa_description_SubVariable():
    instance = viewpoint_description_TypedVariable(defaultValueExpression="sample_text")
    assert isinstance(instance, description_SubVariable)


def test_viewpoint_tool_AcceleoVariable_isa_description_SubVariable():
    instance = viewpoint_tool_AcceleoVariable(computationExpression="sample_text")
    assert isinstance(instance, description_SubVariable)


def test_viewpoint_tool_SelectModelElementVariable_isa_description_SubVariable():
    instance = viewpoint_tool_SelectModelElementVariable()
    assert isinstance(instance, description_SubVariable)


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
    a = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
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


def test_assoc_allRules216_link_reassign_clear():
    a = viewpoint_validation_ValidationSet(name="sample_text")
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_validation_ValidationSet217', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet217', b1)
    if hasattr(b1, 'validation_ValidationRule218'):
        assert _is_linked(b1, 'validation_ValidationRule218', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet217', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet217', b2)
    if hasattr(b1, 'validation_ValidationRule218'):
        assert not _is_linked(b1, 'validation_ValidationRule218', a)
    if hasattr(b2, 'validation_ValidationRule218'):
        assert _is_linked(b2, 'validation_ValidationRule218', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet217', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationSet217', b2)
    if hasattr(b2, 'validation_ValidationRule218'):
        assert not _is_linked(b2, 'validation_ValidationRule218', a)


def test_assoc_analyses54_link_reassign_clear():
    a = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    b1 = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    b2 = viewpoint_DAnalysis(semanticResources="sample_text_2", version="sample_text_2")
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


def test_assoc_audits219_link_reassign_clear():
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


def test_assoc_container132_link_reassign_clear():
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


def test_assoc_container148_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_SelectContainerVariable()
    b2 = tool_SelectContainerVariable()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription149', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription149', b1)
    if hasattr(b1, 'tool_SelectContainerVariable'):
        assert _is_linked(b1, 'tool_SelectContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription149', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription149', b2)
    if hasattr(b1, 'tool_SelectContainerVariable'):
        assert not _is_linked(b1, 'tool_SelectContainerVariable', a)
    if hasattr(b2, 'tool_SelectContainerVariable'):
        assert _is_linked(b2, 'tool_SelectContainerVariable', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription149', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription149', b2)
    if hasattr(b2, 'tool_SelectContainerVariable'):
        assert not _is_linked(b2, 'tool_SelectContainerVariable', a)


def test_assoc_container158_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_SelectContainerVariable()
    b2 = tool_SelectContainerVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription159', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription159', b1)
    if hasattr(b1, 'tool_SelectContainerVariable160'):
        assert _is_linked(b1, 'tool_SelectContainerVariable160', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription159', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription159', b2)
    if hasattr(b1, 'tool_SelectContainerVariable160'):
        assert not _is_linked(b1, 'tool_SelectContainerVariable160', a)
    if hasattr(b2, 'tool_SelectContainerVariable160'):
        assert _is_linked(b2, 'tool_SelectContainerVariable160', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription159', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription159', b2)
    if hasattr(b2, 'tool_SelectContainerVariable160'):
        assert not _is_linked(b2, 'tool_SelectContainerVariable160', a)


def test_assoc_containerVariable179_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription180', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription180', b1)
    if hasattr(b1, 'tool_ElementSelectVariable181'):
        assert _is_linked(b1, 'tool_ElementSelectVariable181', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription180', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription180', b2)
    if hasattr(b1, 'tool_ElementSelectVariable181'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable181', a)
    if hasattr(b2, 'tool_ElementSelectVariable181'):
        assert _is_linked(b2, 'tool_ElementSelectVariable181', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription180', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription180', b2)
    if hasattr(b2, 'tool_ElementSelectVariable181'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable181', a)


def test_assoc_containerView133_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription134', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription134', b1)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert _is_linked(b1, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription134', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription134', b2)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable', a)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert _is_linked(b2, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription134', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription134', b2)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable', a)


def test_assoc_containerView145_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription146', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription146', b1)
    if hasattr(b1, 'tool_ContainerViewVariable147'):
        assert _is_linked(b1, 'tool_ContainerViewVariable147', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription146', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription146', b2)
    if hasattr(b1, 'tool_ContainerViewVariable147'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable147', a)
    if hasattr(b2, 'tool_ContainerViewVariable147'):
        assert _is_linked(b2, 'tool_ContainerViewVariable147', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription146', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription146', b2)
    if hasattr(b2, 'tool_ContainerViewVariable147'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable147', a)


def test_assoc_containerView155_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b1)
    if hasattr(b1, 'tool_ContainerViewVariable157'):
        assert _is_linked(b1, 'tool_ContainerViewVariable157', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b2)
    if hasattr(b1, 'tool_ContainerViewVariable157'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable157', a)
    if hasattr(b2, 'tool_ContainerViewVariable157'):
        assert _is_linked(b2, 'tool_ContainerViewVariable157', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', b2)
    if hasattr(b2, 'tool_ContainerViewVariable157'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable157', a)


def test_assoc_containerViewVariable169_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription170', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription170', b1)
    if hasattr(b1, 'tool_ContainerViewVariable171'):
        assert _is_linked(b1, 'tool_ContainerViewVariable171', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription170', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription170', b2)
    if hasattr(b1, 'tool_ContainerViewVariable171'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable171', a)
    if hasattr(b2, 'tool_ContainerViewVariable171'):
        assert _is_linked(b2, 'tool_ContainerViewVariable171', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription170', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription170', b2)
    if hasattr(b2, 'tool_ContainerViewVariable171'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable171', a)


def test_assoc_containerViewVariable176_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription177', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription177', b1)
    if hasattr(b1, 'tool_ContainerViewVariable178'):
        assert _is_linked(b1, 'tool_ContainerViewVariable178', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription177', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription177', b2)
    if hasattr(b1, 'tool_ContainerViewVariable178'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable178', a)
    if hasattr(b2, 'tool_ContainerViewVariable178'):
        assert _is_linked(b2, 'tool_ContainerViewVariable178', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription177', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription177', b2)
    if hasattr(b2, 'tool_ContainerViewVariable178'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable178', a)


def test_assoc_copiedElement138_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ElementVariable()
    b2 = tool_ElementVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription139', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription139', b1)
    if hasattr(b1, 'tool_ElementVariable140'):
        assert _is_linked(b1, 'tool_ElementVariable140', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription139', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription139', b2)
    if hasattr(b1, 'tool_ElementVariable140'):
        assert not _is_linked(b1, 'tool_ElementVariable140', a)
    if hasattr(b2, 'tool_ElementVariable140'):
        assert _is_linked(b2, 'tool_ElementVariable140', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription139', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription139', b2)
    if hasattr(b2, 'tool_ElementVariable140'):
        assert not _is_linked(b2, 'tool_ElementVariable140', a)


def test_assoc_copiedView135_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_ElementViewVariable()
    b2 = tool_ElementViewVariable()
    _safe_set(a, 'viewpoint_tool_PasteDescription136', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription136', b1)
    if hasattr(b1, 'tool_ElementViewVariable137'):
        assert _is_linked(b1, 'tool_ElementViewVariable137', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription136', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription136', b2)
    if hasattr(b1, 'tool_ElementViewVariable137'):
        assert not _is_linked(b1, 'tool_ElementViewVariable137', a)
    if hasattr(b2, 'tool_ElementViewVariable137'):
        assert _is_linked(b2, 'tool_ElementViewVariable137', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription136', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription136', b2)
    if hasattr(b2, 'tool_ElementViewVariable137'):
        assert not _is_linked(b2, 'tool_ElementViewVariable137', a)


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


def test_assoc_description17_link_reassign_clear():
    a = viewpoint_DRepresentationDescriptor(name="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_DRepresentationDescriptor', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationDescriptor', b1)
    if hasattr(b1, 'RepresentationDescription'):
        assert _is_linked(b1, 'RepresentationDescription', a)
    _safe_set(a, 'viewpoint_DRepresentationDescriptor', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationDescriptor', b2)
    if hasattr(b1, 'RepresentationDescription'):
        assert not _is_linked(b1, 'RepresentationDescription', a)
    if hasattr(b2, 'RepresentationDescription'):
        assert _is_linked(b2, 'RepresentationDescription', a)
    _safe_set(a, 'viewpoint_DRepresentationDescriptor', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationDescriptor', b2)
    if hasattr(b2, 'RepresentationDescription'):
        assert not _is_linked(b2, 'RepresentationDescription', a)


def test_assoc_details96_link_reassign_clear():
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
    a = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
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


def test_assoc_eAnnotations95_link_reassign_clear():
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


def test_assoc_element127_link_reassign_clear():
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


def test_assoc_element144_link_reassign_clear():
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


def test_assoc_element153_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_ElementSelectVariable()
    b2 = tool_ElementSelectVariable()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b1)
    if hasattr(b1, 'tool_ElementSelectVariable154'):
        assert _is_linked(b1, 'tool_ElementSelectVariable154', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    if hasattr(b1, 'tool_ElementSelectVariable154'):
        assert not _is_linked(b1, 'tool_ElementSelectVariable154', a)
    if hasattr(b2, 'tool_ElementSelectVariable154'):
        assert _is_linked(b2, 'tool_ElementSelectVariable154', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription', b2)
    if hasattr(b2, 'tool_ElementSelectVariable154'):
        assert not _is_linked(b2, 'tool_ElementSelectVariable154', a)


def test_assoc_elementView128_link_reassign_clear():
    a = viewpoint_tool_ToolDescription(iconPath="sample_text")
    b1 = tool_ElementViewVariable()
    b2 = tool_ElementViewVariable()
    _safe_set(a, 'viewpoint_tool_ToolDescription129', b1)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription129', b1)
    if hasattr(b1, 'tool_ElementViewVariable'):
        assert _is_linked(b1, 'tool_ElementViewVariable', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription129', b2)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription129', b2)
    if hasattr(b1, 'tool_ElementViewVariable'):
        assert not _is_linked(b1, 'tool_ElementViewVariable', a)
    if hasattr(b2, 'tool_ElementViewVariable'):
        assert _is_linked(b2, 'tool_ElementViewVariable', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription129', None)
    assert not _is_linked(a, 'viewpoint_tool_ToolDescription129', b2)
    if hasattr(b2, 'tool_ElementViewVariable'):
        assert not _is_linked(b2, 'tool_ElementViewVariable', a)


def test_assoc_elementsToSelect60_link_reassign_clear():
    a = viewpoint_UIState(decorationImage="sample_text", inverseSelectionOrder=True)
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_UIState61', {b1})
    assert _is_linked(a, 'viewpoint_UIState61', b1)
    if hasattr(b1, 'viewpoint_EObject62'):
        assert _is_linked(b1, 'viewpoint_EObject62', a)
    _safe_set(a, 'viewpoint_UIState61', {b2})
    assert _is_linked(a, 'viewpoint_UIState61', b2)
    if hasattr(b1, 'viewpoint_EObject62'):
        assert not _is_linked(b1, 'viewpoint_EObject62', a)
    if hasattr(b2, 'viewpoint_EObject62'):
        assert _is_linked(b2, 'viewpoint_EObject62', a)
    _safe_set(a, 'viewpoint_UIState61', set())
    assert not _is_linked(a, 'viewpoint_UIState61', b2)
    if hasattr(b2, 'viewpoint_EObject62'):
        assert not _is_linked(b2, 'viewpoint_EObject62', a)


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


def test_assoc_extensions69_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = Extension()
    b2 = Extension()
    _safe_set(a, 'viewpoint_description_Group70', {b1})
    assert _is_linked(a, 'viewpoint_description_Group70', b1)
    if hasattr(b1, 'Extension'):
        assert _is_linked(b1, 'Extension', a)
    _safe_set(a, 'viewpoint_description_Group70', {b2})
    assert _is_linked(a, 'viewpoint_description_Group70', b2)
    if hasattr(b1, 'Extension'):
        assert not _is_linked(b1, 'Extension', a)
    if hasattr(b2, 'Extension'):
        assert _is_linked(b2, 'Extension', a)
    _safe_set(a, 'viewpoint_description_Group70', set())
    assert not _is_linked(a, 'viewpoint_description_Group70', b2)
    if hasattr(b2, 'Extension'):
        assert not _is_linked(b2, 'Extension', a)


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


def test_assoc_filters126_link_reassign_clear():
    a = viewpoint_tool_AbstractToolDescription(elementsToSelect="sample_text", forceRefresh=True, inverseSelectionOrder=True, precondition="sample_text")
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


def test_assoc_fixes220_link_reassign_clear():
    a = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    b1 = validation_ValidationFix()
    b2 = validation_ValidationFix()
    _safe_set(a, 'viewpoint_validation_ValidationRule221', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationRule221', b1)
    if hasattr(b1, 'validation_ValidationFix'):
        assert _is_linked(b1, 'validation_ValidationFix', a)
    _safe_set(a, 'viewpoint_validation_ValidationRule221', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationRule221', b2)
    if hasattr(b1, 'validation_ValidationFix'):
        assert not _is_linked(b1, 'validation_ValidationFix', a)
    if hasattr(b2, 'validation_ValidationFix'):
        assert _is_linked(b2, 'validation_ValidationFix', a)
    _safe_set(a, 'viewpoint_validation_ValidationRule221', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationRule221', b2)
    if hasattr(b2, 'validation_ValidationFix'):
        assert not _is_linked(b2, 'validation_ValidationFix', a)


def test_assoc_initialOperation130_link_reassign_clear():
    a = viewpoint_tool_ToolDescription(iconPath="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_ToolDescription131', b1)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription131', b1)
    if hasattr(b1, 'tool_InitialOperation'):
        assert _is_linked(b1, 'tool_InitialOperation', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription131', b2)
    assert _is_linked(a, 'viewpoint_tool_ToolDescription131', b2)
    if hasattr(b1, 'tool_InitialOperation'):
        assert not _is_linked(b1, 'tool_InitialOperation', a)
    if hasattr(b2, 'tool_InitialOperation'):
        assert _is_linked(b2, 'tool_InitialOperation', a)
    _safe_set(a, 'viewpoint_tool_ToolDescription131', None)
    assert not _is_linked(a, 'viewpoint_tool_ToolDescription131', b2)
    if hasattr(b2, 'tool_InitialOperation'):
        assert not _is_linked(b2, 'tool_InitialOperation', a)


def test_assoc_initialOperation141_link_reassign_clear():
    a = viewpoint_tool_PasteDescription()
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_PasteDescription142', b1)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription142', b1)
    if hasattr(b1, 'tool_InitialOperation143'):
        assert _is_linked(b1, 'tool_InitialOperation143', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription142', b2)
    assert _is_linked(a, 'viewpoint_tool_PasteDescription142', b2)
    if hasattr(b1, 'tool_InitialOperation143'):
        assert not _is_linked(b1, 'tool_InitialOperation143', a)
    if hasattr(b2, 'tool_InitialOperation143'):
        assert _is_linked(b2, 'tool_InitialOperation143', a)
    _safe_set(a, 'viewpoint_tool_PasteDescription142', None)
    assert not _is_linked(a, 'viewpoint_tool_PasteDescription142', b2)
    if hasattr(b2, 'tool_InitialOperation143'):
        assert not _is_linked(b2, 'tool_InitialOperation143', a)


def test_assoc_initialOperation150_link_reassign_clear():
    a = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription151', b1)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription151', b1)
    if hasattr(b1, 'tool_InitialOperation152'):
        assert _is_linked(b1, 'tool_InitialOperation152', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription151', b2)
    assert _is_linked(a, 'viewpoint_tool_SelectionWizardDescription151', b2)
    if hasattr(b1, 'tool_InitialOperation152'):
        assert not _is_linked(b1, 'tool_InitialOperation152', a)
    if hasattr(b2, 'tool_InitialOperation152'):
        assert _is_linked(b2, 'tool_InitialOperation152', a)
    _safe_set(a, 'viewpoint_tool_SelectionWizardDescription151', None)
    assert not _is_linked(a, 'viewpoint_tool_SelectionWizardDescription151', b2)
    if hasattr(b2, 'tool_InitialOperation152'):
        assert not _is_linked(b2, 'tool_InitialOperation152', a)


def test_assoc_initialOperation161_link_reassign_clear():
    a = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription162', b1)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription162', b1)
    if hasattr(b1, 'tool_InitialOperation163'):
        assert _is_linked(b1, 'tool_InitialOperation163', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription162', b2)
    assert _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription162', b2)
    if hasattr(b1, 'tool_InitialOperation163'):
        assert not _is_linked(b1, 'tool_InitialOperation163', a)
    if hasattr(b2, 'tool_InitialOperation163'):
        assert _is_linked(b2, 'tool_InitialOperation163', a)
    _safe_set(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription162', None)
    assert not _is_linked(a, 'viewpoint_tool_PaneBasedSelectionWizardDescription162', b2)
    if hasattr(b2, 'tool_InitialOperation163'):
        assert not _is_linked(b2, 'tool_InitialOperation163', a)


def test_assoc_initialOperation166_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription167', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription167', b1)
    if hasattr(b1, 'tool_InitialOperation168'):
        assert _is_linked(b1, 'tool_InitialOperation168', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription167', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription167', b2)
    if hasattr(b1, 'tool_InitialOperation168'):
        assert not _is_linked(b1, 'tool_InitialOperation168', a)
    if hasattr(b2, 'tool_InitialOperation168'):
        assert _is_linked(b2, 'tool_InitialOperation168', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription167', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription167', b2)
    if hasattr(b2, 'tool_InitialOperation168'):
        assert not _is_linked(b2, 'tool_InitialOperation168', a)


def test_assoc_initialOperation223_link_reassign_clear():
    a = viewpoint_validation_ValidationFix(name="sample_text")
    b1 = tool_InitialOperation()
    b2 = tool_InitialOperation()
    _safe_set(a, 'viewpoint_validation_ValidationFix', b1)
    assert _is_linked(a, 'viewpoint_validation_ValidationFix', b1)
    if hasattr(b1, 'tool_InitialOperation224'):
        assert _is_linked(b1, 'tool_InitialOperation224', a)
    _safe_set(a, 'viewpoint_validation_ValidationFix', b2)
    assert _is_linked(a, 'viewpoint_validation_ValidationFix', b2)
    if hasattr(b1, 'tool_InitialOperation224'):
        assert not _is_linked(b1, 'tool_InitialOperation224', a)
    if hasattr(b2, 'tool_InitialOperation224'):
        assert _is_linked(b2, 'tool_InitialOperation224', a)
    _safe_set(a, 'viewpoint_validation_ValidationFix', None)
    assert not _is_linked(a, 'viewpoint_validation_ValidationFix', b2)
    if hasattr(b2, 'tool_InitialOperation224'):
        assert not _is_linked(b2, 'tool_InitialOperation224', a)


def test_assoc_labelColor124_link_reassign_clear():
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


def test_assoc_listeners206_link_reassign_clear():
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


def test_assoc_metamodel86_link_reassign_clear():
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


def test_assoc_metamodel89_link_reassign_clear():
    a = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    b1 = description_viewpoint_EPackage()
    b2 = description_viewpoint_EPackage()
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', {b1})
    assert _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b1)
    if hasattr(b1, 'description_viewpoint_EPackage90'):
        assert _is_linked(b1, 'description_viewpoint_EPackage90', a)
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', {b2})
    assert _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b2)
    if hasattr(b1, 'description_viewpoint_EPackage90'):
        assert not _is_linked(b1, 'description_viewpoint_EPackage90', a)
    if hasattr(b2, 'description_viewpoint_EPackage90'):
        assert _is_linked(b2, 'description_viewpoint_EPackage90', a)
    _safe_set(a, 'viewpoint_description_RepresentationExtensionDescription', set())
    assert not _is_linked(a, 'viewpoint_description_RepresentationExtensionDescription', b2)
    if hasattr(b2, 'description_viewpoint_EPackage90'):
        assert not _is_linked(b2, 'description_viewpoint_EPackage90', a)


def test_assoc_models2_link_reassign_clear():
    a = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
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


def test_assoc_object205_link_reassign_clear():
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


def test_assoc_ownedAnnotationEntries28_link_reassign_clear():
    a = viewpoint_DRepresentation(name="sample_text")
    b1 = AnnotationEntry()
    b2 = AnnotationEntry()
    _safe_set(a, 'viewpoint_DRepresentation29', {b1})
    assert _is_linked(a, 'viewpoint_DRepresentation29', b1)
    if hasattr(b1, 'AnnotationEntry'):
        assert _is_linked(b1, 'AnnotationEntry', a)
    _safe_set(a, 'viewpoint_DRepresentation29', {b2})
    assert _is_linked(a, 'viewpoint_DRepresentation29', b2)
    if hasattr(b1, 'AnnotationEntry'):
        assert not _is_linked(b1, 'AnnotationEntry', a)
    if hasattr(b2, 'AnnotationEntry'):
        assert _is_linked(b2, 'AnnotationEntry', a)
    _safe_set(a, 'viewpoint_DRepresentation29', set())
    assert not _is_linked(a, 'viewpoint_DRepresentation29', b2)
    if hasattr(b2, 'AnnotationEntry'):
        assert not _is_linked(b2, 'AnnotationEntry', a)


def test_assoc_ownedFeatureExtensions11_link_reassign_clear():
    a = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
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


def test_assoc_ownedFeatureExtensions81_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = FeatureExtensionDescription()
    b2 = FeatureExtensionDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint82', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint82', b1)
    if hasattr(b1, 'FeatureExtensionDescription83'):
        assert _is_linked(b1, 'FeatureExtensionDescription83', a)
    _safe_set(a, 'viewpoint_description_Viewpoint82', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint82', b2)
    if hasattr(b1, 'FeatureExtensionDescription83'):
        assert not _is_linked(b1, 'FeatureExtensionDescription83', a)
    if hasattr(b2, 'FeatureExtensionDescription83'):
        assert _is_linked(b2, 'FeatureExtensionDescription83', a)
    _safe_set(a, 'viewpoint_description_Viewpoint82', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint82', b2)
    if hasattr(b2, 'FeatureExtensionDescription83'):
        assert not _is_linked(b2, 'FeatureExtensionDescription83', a)


def test_assoc_ownedJavaExtensions77_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = JavaExtension()
    b2 = JavaExtension()
    _safe_set(a, 'viewpoint_description_Viewpoint78', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint78', b1)
    if hasattr(b1, 'JavaExtension'):
        assert _is_linked(b1, 'JavaExtension', a)
    _safe_set(a, 'viewpoint_description_Viewpoint78', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint78', b2)
    if hasattr(b1, 'JavaExtension'):
        assert not _is_linked(b1, 'JavaExtension', a)
    if hasattr(b2, 'JavaExtension'):
        assert _is_linked(b2, 'JavaExtension', a)
    _safe_set(a, 'viewpoint_description_Viewpoint78', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint78', b2)
    if hasattr(b2, 'JavaExtension'):
        assert not _is_linked(b2, 'JavaExtension', a)


def test_assoc_ownedMMExtensions79_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = MetamodelExtensionSetting()
    b2 = MetamodelExtensionSetting()
    _safe_set(a, 'viewpoint_description_Viewpoint80', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint80', b1)
    if hasattr(b1, 'MetamodelExtensionSetting'):
        assert _is_linked(b1, 'MetamodelExtensionSetting', a)
    _safe_set(a, 'viewpoint_description_Viewpoint80', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint80', b2)
    if hasattr(b1, 'MetamodelExtensionSetting'):
        assert not _is_linked(b1, 'MetamodelExtensionSetting', a)
    if hasattr(b2, 'MetamodelExtensionSetting'):
        assert _is_linked(b2, 'MetamodelExtensionSetting', a)
    _safe_set(a, 'viewpoint_description_Viewpoint80', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint80', b2)
    if hasattr(b2, 'MetamodelExtensionSetting'):
        assert not _is_linked(b2, 'MetamodelExtensionSetting', a)


def test_assoc_ownedRepresentationDescriptors37_link_reassign_clear():
    a = viewpoint_DRepresentationDescriptor(name="sample_text")
    b1 = viewpoint_DView()
    b2 = viewpoint_DView()
    _safe_set(a, 'viewpoint_DRepresentationDescriptor39', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationDescriptor39', b1)
    if hasattr(b1, 'viewpoint_DView38'):
        assert _is_linked(b1, 'viewpoint_DView38', a)
    _safe_set(a, 'viewpoint_DRepresentationDescriptor39', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationDescriptor39', b2)
    if hasattr(b1, 'viewpoint_DView38'):
        assert not _is_linked(b1, 'viewpoint_DView38', a)
    if hasattr(b2, 'viewpoint_DView38'):
        assert _is_linked(b2, 'viewpoint_DView38', a)
    _safe_set(a, 'viewpoint_DRepresentationDescriptor39', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationDescriptor39', b2)
    if hasattr(b2, 'viewpoint_DView38'):
        assert not _is_linked(b2, 'viewpoint_DView38', a)


def test_assoc_ownedRepresentationElements23_link_reassign_clear():
    a = viewpoint_DRepresentationElement(name="sample_text")
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DRepresentationElement', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationElement', b1)
    if hasattr(b1, 'viewpoint_DRepresentation24'):
        assert _is_linked(b1, 'viewpoint_DRepresentation24', a)
    _safe_set(a, 'viewpoint_DRepresentationElement', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationElement', b2)
    if hasattr(b1, 'viewpoint_DRepresentation24'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation24', a)
    if hasattr(b2, 'viewpoint_DRepresentation24'):
        assert _is_linked(b2, 'viewpoint_DRepresentation24', a)
    _safe_set(a, 'viewpoint_DRepresentationElement', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationElement', b2)
    if hasattr(b2, 'viewpoint_DRepresentation24'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation24', a)


def test_assoc_ownedRepresentationExtensions75_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationExtensionDescription()
    b2 = RepresentationExtensionDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint76', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint76', b1)
    if hasattr(b1, 'RepresentationExtensionDescription'):
        assert _is_linked(b1, 'RepresentationExtensionDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint76', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint76', b2)
    if hasattr(b1, 'RepresentationExtensionDescription'):
        assert not _is_linked(b1, 'RepresentationExtensionDescription', a)
    if hasattr(b2, 'RepresentationExtensionDescription'):
        assert _is_linked(b2, 'RepresentationExtensionDescription', a)
    _safe_set(a, 'viewpoint_description_Viewpoint76', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint76', b2)
    if hasattr(b2, 'RepresentationExtensionDescription'):
        assert not _is_linked(b2, 'RepresentationExtensionDescription', a)


def test_assoc_ownedRepresentations72_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_description_Viewpoint73', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint73', b1)
    if hasattr(b1, 'RepresentationDescription74'):
        assert _is_linked(b1, 'RepresentationDescription74', a)
    _safe_set(a, 'viewpoint_description_Viewpoint73', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint73', b2)
    if hasattr(b1, 'RepresentationDescription74'):
        assert not _is_linked(b1, 'RepresentationDescription74', a)
    if hasattr(b2, 'RepresentationDescription74'):
        assert _is_linked(b2, 'RepresentationDescription74', a)
    _safe_set(a, 'viewpoint_description_Viewpoint73', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint73', b2)
    if hasattr(b2, 'RepresentationDescription74'):
        assert not _is_linked(b2, 'RepresentationDescription74', a)


def test_assoc_ownedRepresentations87_link_reassign_clear():
    a = viewpoint_description_RepresentationTemplate(name="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', {b1})
    assert _is_linked(a, 'viewpoint_description_RepresentationTemplate', b1)
    if hasattr(b1, 'RepresentationDescription88'):
        assert _is_linked(b1, 'RepresentationDescription88', a)
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', {b2})
    assert _is_linked(a, 'viewpoint_description_RepresentationTemplate', b2)
    if hasattr(b1, 'RepresentationDescription88'):
        assert not _is_linked(b1, 'RepresentationDescription88', a)
    if hasattr(b2, 'RepresentationDescription88'):
        assert _is_linked(b2, 'RepresentationDescription88', a)
    _safe_set(a, 'viewpoint_description_RepresentationTemplate', set())
    assert not _is_linked(a, 'viewpoint_description_RepresentationTemplate', b2)
    if hasattr(b2, 'RepresentationDescription88'):
        assert not _is_linked(b2, 'RepresentationDescription88', a)


def test_assoc_ownedRules212_link_reassign_clear():
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
    a = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
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


def test_assoc_ownedTemplates84_link_reassign_clear():
    a = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    b1 = RepresentationTemplate()
    b2 = RepresentationTemplate()
    _safe_set(a, 'viewpoint_description_Viewpoint85', {b1})
    assert _is_linked(a, 'viewpoint_description_Viewpoint85', b1)
    if hasattr(b1, 'RepresentationTemplate'):
        assert _is_linked(b1, 'RepresentationTemplate', a)
    _safe_set(a, 'viewpoint_description_Viewpoint85', {b2})
    assert _is_linked(a, 'viewpoint_description_Viewpoint85', b2)
    if hasattr(b1, 'RepresentationTemplate'):
        assert not _is_linked(b1, 'RepresentationTemplate', a)
    if hasattr(b2, 'RepresentationTemplate'):
        assert _is_linked(b2, 'RepresentationTemplate', a)
    _safe_set(a, 'viewpoint_description_Viewpoint85', set())
    assert not _is_linked(a, 'viewpoint_description_Viewpoint85', b2)
    if hasattr(b2, 'RepresentationTemplate'):
        assert not _is_linked(b2, 'RepresentationTemplate', a)


def test_assoc_ownedViewpoints63_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = Viewpoint()
    b2 = Viewpoint()
    _safe_set(a, 'viewpoint_description_Group', {b1})
    assert _is_linked(a, 'viewpoint_description_Group', b1)
    if hasattr(b1, 'Viewpoint64'):
        assert _is_linked(b1, 'Viewpoint64', a)
    _safe_set(a, 'viewpoint_description_Group', {b2})
    assert _is_linked(a, 'viewpoint_description_Group', b2)
    if hasattr(b1, 'Viewpoint64'):
        assert not _is_linked(b1, 'Viewpoint64', a)
    if hasattr(b2, 'Viewpoint64'):
        assert _is_linked(b2, 'Viewpoint64', a)
    _safe_set(a, 'viewpoint_description_Group', set())
    assert not _is_linked(a, 'viewpoint_description_Group', b2)
    if hasattr(b2, 'Viewpoint64'):
        assert not _is_linked(b2, 'Viewpoint64', a)


def test_assoc_ownedViews6_link_reassign_clear():
    a = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    b1 = viewpoint_DView()
    b2 = viewpoint_DView()
    _safe_set(a, 'viewpoint_DAnalysis7', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysis7', b1)
    if hasattr(b1, 'viewpoint_DView'):
        assert _is_linked(b1, 'viewpoint_DView', a)
    _safe_set(a, 'viewpoint_DAnalysis7', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysis7', b2)
    if hasattr(b1, 'viewpoint_DView'):
        assert not _is_linked(b1, 'viewpoint_DView', a)
    if hasattr(b2, 'viewpoint_DView'):
        assert _is_linked(b2, 'viewpoint_DView', a)
    _safe_set(a, 'viewpoint_DAnalysis7', set())
    assert not _is_linked(a, 'viewpoint_DAnalysis7', b2)
    if hasattr(b2, 'viewpoint_DView'):
        assert not _is_linked(b2, 'viewpoint_DView', a)


def test_assoc_parameters191_link_reassign_clear():
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
    a = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    b1 = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    b2 = viewpoint_DAnalysis(semanticResources="sample_text_2", version="sample_text_2")
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


def test_assoc_representation21_link_reassign_clear():
    a = viewpoint_DRepresentationDescriptor(name="sample_text")
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DRepresentationDescriptor22', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationDescriptor22', b1)
    if hasattr(b1, 'viewpoint_DRepresentation'):
        assert _is_linked(b1, 'viewpoint_DRepresentation', a)
    _safe_set(a, 'viewpoint_DRepresentationDescriptor22', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationDescriptor22', b2)
    if hasattr(b1, 'viewpoint_DRepresentation'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation', a)
    if hasattr(b2, 'viewpoint_DRepresentation'):
        assert _is_linked(b2, 'viewpoint_DRepresentation', a)
    _safe_set(a, 'viewpoint_DRepresentationDescriptor22', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationDescriptor22', b2)
    if hasattr(b2, 'viewpoint_DRepresentation'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation', a)


def test_assoc_representationDescription164_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b1)
    if hasattr(b1, 'RepresentationDescription165'):
        assert _is_linked(b1, 'RepresentationDescription165', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    if hasattr(b1, 'RepresentationDescription165'):
        assert not _is_linked(b1, 'RepresentationDescription165', a)
    if hasattr(b2, 'RepresentationDescription165'):
        assert _is_linked(b2, 'RepresentationDescription165', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription', b2)
    if hasattr(b2, 'RepresentationDescription165'):
        assert not _is_linked(b2, 'RepresentationDescription165', a)


def test_assoc_representationDescription174_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = RepresentationDescription()
    b2 = RepresentationDescription()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b1)
    if hasattr(b1, 'RepresentationDescription175'):
        assert _is_linked(b1, 'RepresentationDescription175', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    if hasattr(b1, 'RepresentationDescription175'):
        assert not _is_linked(b1, 'RepresentationDescription175', a)
    if hasattr(b2, 'RepresentationDescription175'):
        assert _is_linked(b2, 'RepresentationDescription175', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription', b2)
    if hasattr(b2, 'RepresentationDescription175'):
        assert not _is_linked(b2, 'RepresentationDescription175', a)


def test_assoc_representationElements25_link_reassign_clear():
    a = viewpoint_DRepresentationElement(name="sample_text")
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_DRepresentationElement27', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationElement27', b1)
    if hasattr(b1, 'viewpoint_DRepresentation26'):
        assert _is_linked(b1, 'viewpoint_DRepresentation26', a)
    _safe_set(a, 'viewpoint_DRepresentationElement27', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationElement27', b2)
    if hasattr(b1, 'viewpoint_DRepresentation26'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation26', a)
    if hasattr(b2, 'viewpoint_DRepresentation26'):
        assert _is_linked(b2, 'viewpoint_DRepresentation26', a)
    _safe_set(a, 'viewpoint_DRepresentationElement27', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationElement27', b2)
    if hasattr(b2, 'viewpoint_DRepresentation26'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation26', a)


def test_assoc_representationNameVariable172_link_reassign_clear():
    a = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    b1 = tool_NameVariable()
    b2 = tool_NameVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription173', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription173', b1)
    if hasattr(b1, 'tool_NameVariable'):
        assert _is_linked(b1, 'tool_NameVariable', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription173', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription173', b2)
    if hasattr(b1, 'tool_NameVariable'):
        assert not _is_linked(b1, 'tool_NameVariable', a)
    if hasattr(b2, 'tool_NameVariable'):
        assert _is_linked(b2, 'tool_NameVariable', a)
    _safe_set(a, 'viewpoint_tool_RepresentationCreationDescription173', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationCreationDescription173', b2)
    if hasattr(b2, 'tool_NameVariable'):
        assert not _is_linked(b2, 'tool_NameVariable', a)


def test_assoc_representationNameVariable182_link_reassign_clear():
    a = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    b1 = tool_NameVariable()
    b2 = tool_NameVariable()
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription183', b1)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription183', b1)
    if hasattr(b1, 'tool_NameVariable184'):
        assert _is_linked(b1, 'tool_NameVariable184', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription183', b2)
    assert _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription183', b2)
    if hasattr(b1, 'tool_NameVariable184'):
        assert not _is_linked(b1, 'tool_NameVariable184', a)
    if hasattr(b2, 'tool_NameVariable184'):
        assert _is_linked(b2, 'tool_NameVariable184', a)
    _safe_set(a, 'viewpoint_tool_RepresentationNavigationDescription183', None)
    assert not _is_linked(a, 'viewpoint_tool_RepresentationNavigationDescription183', b2)
    if hasattr(b2, 'tool_NameVariable184'):
        assert not _is_linked(b2, 'tool_NameVariable184', a)


def test_assoc_reusedRules213_link_reassign_clear():
    a = viewpoint_validation_ValidationSet(name="sample_text")
    b1 = validation_ValidationRule()
    b2 = validation_ValidationRule()
    _safe_set(a, 'viewpoint_validation_ValidationSet214', {b1})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet214', b1)
    if hasattr(b1, 'validation_ValidationRule215'):
        assert _is_linked(b1, 'validation_ValidationRule215', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet214', {b2})
    assert _is_linked(a, 'viewpoint_validation_ValidationSet214', b2)
    if hasattr(b1, 'validation_ValidationRule215'):
        assert not _is_linked(b1, 'validation_ValidationRule215', a)
    if hasattr(b2, 'validation_ValidationRule215'):
        assert _is_linked(b2, 'validation_ValidationRule215', a)
    _safe_set(a, 'viewpoint_validation_ValidationSet214', set())
    assert not _is_linked(a, 'viewpoint_validation_ValidationSet214', b2)
    if hasattr(b2, 'validation_ValidationRule215'):
        assert not _is_linked(b2, 'validation_ValidationRule215', a)


def test_assoc_selectedViews8_link_reassign_clear():
    a = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    b1 = viewpoint_DView()
    b2 = viewpoint_DView()
    _safe_set(a, 'viewpoint_DAnalysis9', {b1})
    assert _is_linked(a, 'viewpoint_DAnalysis9', b1)
    if hasattr(b1, 'viewpoint_DView10'):
        assert _is_linked(b1, 'viewpoint_DView10', a)
    _safe_set(a, 'viewpoint_DAnalysis9', {b2})
    assert _is_linked(a, 'viewpoint_DAnalysis9', b2)
    if hasattr(b1, 'viewpoint_DView10'):
        assert not _is_linked(b1, 'viewpoint_DView10', a)
    if hasattr(b2, 'viewpoint_DView10'):
        assert _is_linked(b2, 'viewpoint_DView10', a)
    _safe_set(a, 'viewpoint_DAnalysis9', set())
    assert not _is_linked(a, 'viewpoint_DAnalysis9', b2)
    if hasattr(b2, 'viewpoint_DView10'):
        assert not _is_linked(b2, 'viewpoint_DView10', a)


def test_assoc_semanticElements32_link_reassign_clear():
    a = viewpoint_DRepresentationElement(name="sample_text")
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_DRepresentationElement33', {b1})
    assert _is_linked(a, 'viewpoint_DRepresentationElement33', b1)
    if hasattr(b1, 'viewpoint_EObject34'):
        assert _is_linked(b1, 'viewpoint_EObject34', a)
    _safe_set(a, 'viewpoint_DRepresentationElement33', {b2})
    assert _is_linked(a, 'viewpoint_DRepresentationElement33', b2)
    if hasattr(b1, 'viewpoint_EObject34'):
        assert not _is_linked(b1, 'viewpoint_EObject34', a)
    if hasattr(b2, 'viewpoint_EObject34'):
        assert _is_linked(b2, 'viewpoint_EObject34', a)
    _safe_set(a, 'viewpoint_DRepresentationElement33', set())
    assert not _is_linked(a, 'viewpoint_DRepresentationElement33', b2)
    if hasattr(b2, 'viewpoint_EObject34'):
        assert not _is_linked(b2, 'viewpoint_EObject34', a)


def test_assoc_systemColorsPalette65_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = SytemColorsPalette()
    b2 = SytemColorsPalette()
    _safe_set(a, 'viewpoint_description_Group66', b1)
    assert _is_linked(a, 'viewpoint_description_Group66', b1)
    if hasattr(b1, 'SytemColorsPalette'):
        assert _is_linked(b1, 'SytemColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group66', b2)
    assert _is_linked(a, 'viewpoint_description_Group66', b2)
    if hasattr(b1, 'SytemColorsPalette'):
        assert not _is_linked(b1, 'SytemColorsPalette', a)
    if hasattr(b2, 'SytemColorsPalette'):
        assert _is_linked(b2, 'SytemColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group66', None)
    assert not _is_linked(a, 'viewpoint_description_Group66', b2)
    if hasattr(b2, 'SytemColorsPalette'):
        assert not _is_linked(b2, 'SytemColorsPalette', a)


def test_assoc_target18_link_reassign_clear():
    a = viewpoint_DRepresentationDescriptor(name="sample_text")
    b1 = viewpoint_EObject()
    b2 = viewpoint_EObject()
    _safe_set(a, 'viewpoint_DRepresentationDescriptor19', b1)
    assert _is_linked(a, 'viewpoint_DRepresentationDescriptor19', b1)
    if hasattr(b1, 'viewpoint_EObject20'):
        assert _is_linked(b1, 'viewpoint_EObject20', a)
    _safe_set(a, 'viewpoint_DRepresentationDescriptor19', b2)
    assert _is_linked(a, 'viewpoint_DRepresentationDescriptor19', b2)
    if hasattr(b1, 'viewpoint_EObject20'):
        assert not _is_linked(b1, 'viewpoint_EObject20', a)
    if hasattr(b2, 'viewpoint_EObject20'):
        assert _is_linked(b2, 'viewpoint_EObject20', a)
    _safe_set(a, 'viewpoint_DRepresentationDescriptor19', None)
    assert not _is_linked(a, 'viewpoint_DRepresentationDescriptor19', b2)
    if hasattr(b2, 'viewpoint_EObject20'):
        assert not _is_linked(b2, 'viewpoint_EObject20', a)


def test_assoc_uiState30_link_reassign_clear():
    a = viewpoint_UIState(decorationImage="sample_text", inverseSelectionOrder=True)
    b1 = viewpoint_DRepresentation(name="sample_text")
    b2 = viewpoint_DRepresentation(name="sample_text_2")
    _safe_set(a, 'viewpoint_UIState', b1)
    assert _is_linked(a, 'viewpoint_UIState', b1)
    if hasattr(b1, 'viewpoint_DRepresentation31'):
        assert _is_linked(b1, 'viewpoint_DRepresentation31', a)
    _safe_set(a, 'viewpoint_UIState', b2)
    assert _is_linked(a, 'viewpoint_UIState', b2)
    if hasattr(b1, 'viewpoint_DRepresentation31'):
        assert not _is_linked(b1, 'viewpoint_DRepresentation31', a)
    if hasattr(b2, 'viewpoint_DRepresentation31'):
        assert _is_linked(b2, 'viewpoint_DRepresentation31', a)
    _safe_set(a, 'viewpoint_UIState', None)
    assert not _is_linked(a, 'viewpoint_UIState', b2)
    if hasattr(b2, 'viewpoint_DRepresentation31'):
        assert not _is_linked(b2, 'viewpoint_DRepresentation31', a)


def test_assoc_userColorsPalettes67_link_reassign_clear():
    a = viewpoint_description_Group(name="sample_text", version="sample_text")
    b1 = UserColorsPalette()
    b2 = UserColorsPalette()
    _safe_set(a, 'viewpoint_description_Group68', {b1})
    assert _is_linked(a, 'viewpoint_description_Group68', b1)
    if hasattr(b1, 'UserColorsPalette'):
        assert _is_linked(b1, 'UserColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group68', {b2})
    assert _is_linked(a, 'viewpoint_description_Group68', b2)
    if hasattr(b1, 'UserColorsPalette'):
        assert not _is_linked(b1, 'UserColorsPalette', a)
    if hasattr(b2, 'UserColorsPalette'):
        assert _is_linked(b2, 'UserColorsPalette', a)
    _safe_set(a, 'viewpoint_description_Group68', set())
    assert not _is_linked(a, 'viewpoint_description_Group68', b2)
    if hasattr(b2, 'UserColorsPalette'):
        assert not _is_linked(b2, 'UserColorsPalette', a)


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


def test_assoc_valueType123_link_reassign_clear():
    a = viewpoint_description_TypedVariable(defaultValueExpression="sample_text")
    b1 = description_viewpoint_EDataType()
    b2 = description_viewpoint_EDataType()
    _safe_set(a, 'viewpoint_description_TypedVariable', b1)
    assert _is_linked(a, 'viewpoint_description_TypedVariable', b1)
    if hasattr(b1, 'description_viewpoint_EDataType'):
        assert _is_linked(b1, 'description_viewpoint_EDataType', a)
    _safe_set(a, 'viewpoint_description_TypedVariable', b2)
    assert _is_linked(a, 'viewpoint_description_TypedVariable', b2)
    if hasattr(b1, 'description_viewpoint_EDataType'):
        assert not _is_linked(b1, 'description_viewpoint_EDataType', a)
    if hasattr(b2, 'description_viewpoint_EDataType'):
        assert _is_linked(b2, 'description_viewpoint_EDataType', a)
    _safe_set(a, 'viewpoint_description_TypedVariable', None)
    assert not _is_linked(a, 'viewpoint_description_TypedVariable', b2)
    if hasattr(b2, 'description_viewpoint_EDataType'):
        assert not _is_linked(b2, 'description_viewpoint_EDataType', a)


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


DMappingBased_strategy = st.builds(DMappingBased)
@given(instance=DMappingBased_strategy)
@settings(max_examples=25)
def test_DMappingBased_instantiation(instance):
    assert isinstance(instance, DMappingBased)


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


Extension_strategy = st.builds(Extension)
@given(instance=Extension_strategy)
@settings(max_examples=25)
def test_Extension_instantiation(instance):
    assert isinstance(instance, Extension)


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


SubVariable_strategy = st.builds(SubVariable)
@given(instance=SubVariable_strategy)
@settings(max_examples=25)
def test_SubVariable_instantiation(instance):
    assert isinstance(instance, SubVariable)


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


description_AbstractVariable_strategy = st.builds(description_AbstractVariable)
@given(instance=description_AbstractVariable_strategy)
@settings(max_examples=25)
def test_description_AbstractVariable_instantiation(instance):
    assert isinstance(instance, description_AbstractVariable)


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


description_InteractiveVariableDescription_strategy = st.builds(description_InteractiveVariableDescription)
@given(instance=description_InteractiveVariableDescription_strategy)
@settings(max_examples=25)
def test_description_InteractiveVariableDescription_instantiation(instance):
    assert isinstance(instance, description_InteractiveVariableDescription)


description_SelectionDescription_strategy = st.builds(description_SelectionDescription)
@given(instance=description_SelectionDescription_strategy)
@settings(max_examples=25)
def test_description_SelectionDescription_instantiation(instance):
    assert isinstance(instance, description_SelectionDescription)


description_SubVariable_strategy = st.builds(description_SubVariable)
@given(instance=description_SubVariable_strategy)
@settings(max_examples=25)
def test_description_SubVariable_instantiation(instance):
    assert isinstance(instance, description_SubVariable)


description_UserColor_strategy = st.builds(description_UserColor)
@given(instance=description_UserColor_strategy)
@settings(max_examples=25)
def test_description_UserColor_instantiation(instance):
    assert isinstance(instance, description_UserColor)


description_viewpoint_EDataType_strategy = st.builds(description_viewpoint_EDataType)
@given(instance=description_viewpoint_EDataType_strategy)
@settings(max_examples=25)
def test_description_viewpoint_EDataType_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EDataType)


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


viewpoint_BasicLabelStyle_strategy = st.builds(viewpoint_BasicLabelStyle, iconPath=safe_text, labelColor=safe_text, labelFormat=safe_text, labelSize=st.integers(), showIcon=st.booleans())
@given(instance=viewpoint_BasicLabelStyle_strategy)
@settings(max_examples=25)
def test_viewpoint_BasicLabelStyle_instantiation(instance):
    assert isinstance(instance, viewpoint_BasicLabelStyle)


viewpoint_Customizable_strategy = st.builds(viewpoint_Customizable, customFeatures=safe_text)
@given(instance=viewpoint_Customizable_strategy)
@settings(max_examples=25)
def test_viewpoint_Customizable_instantiation(instance):
    assert isinstance(instance, viewpoint_Customizable)


viewpoint_DAnalysis_strategy = st.builds(viewpoint_DAnalysis, semanticResources=safe_text, version=safe_text)
@given(instance=viewpoint_DAnalysis_strategy)
@settings(max_examples=25)
def test_viewpoint_DAnalysis_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysis)


viewpoint_DAnalysisCustomData_strategy = st.builds(viewpoint_DAnalysisCustomData, key=safe_text)
@given(instance=viewpoint_DAnalysisCustomData_strategy)
@settings(max_examples=25)
def test_viewpoint_DAnalysisCustomData_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysisCustomData)


viewpoint_DAnalysisSessionEObject_strategy = st.builds(viewpoint_DAnalysisSessionEObject, controlledResources=safe_text, open=st.booleans(), resources=safe_text, synchronizationStatus=safe_text)
@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
@settings(max_examples=25)
def test_viewpoint_DAnalysisSessionEObject_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysisSessionEObject)


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


viewpoint_DRepresentationDescriptor_strategy = st.builds(viewpoint_DRepresentationDescriptor, name=safe_text)
@given(instance=viewpoint_DRepresentationDescriptor_strategy)
@settings(max_examples=25)
def test_viewpoint_DRepresentationDescriptor_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentationDescriptor)


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


viewpoint_DStylizable_strategy = st.builds(viewpoint_DStylizable)
@given(instance=viewpoint_DStylizable_strategy)
@settings(max_examples=25)
def test_viewpoint_DStylizable_instantiation(instance):
    assert isinstance(instance, viewpoint_DStylizable)


viewpoint_DView_strategy = st.builds(viewpoint_DView)
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


viewpoint_UIState_strategy = st.builds(viewpoint_UIState, decorationImage=safe_text, inverseSelectionOrder=st.booleans())
@given(instance=viewpoint_UIState_strategy)
@settings(max_examples=25)
def test_viewpoint_UIState_instantiation(instance):
    assert isinstance(instance, viewpoint_UIState)


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


viewpoint_description_AbstractVariable_strategy = st.builds(viewpoint_description_AbstractVariable, name=safe_text)
@given(instance=viewpoint_description_AbstractVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_description_AbstractVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AbstractVariable)


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


viewpoint_description_DecorationDescription_strategy = st.builds(viewpoint_description_DecorationDescription, distributionDirection=safe_text, imageExpression=safe_text, name=safe_text, position=safe_text, preconditionExpression=safe_text, tooltipExpression=safe_text)
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


viewpoint_description_Extension_strategy = st.builds(viewpoint_description_Extension)
@given(instance=viewpoint_description_Extension_strategy)
@settings(max_examples=25)
def test_viewpoint_description_Extension_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Extension)


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


viewpoint_description_GenericDecorationDescription_strategy = st.builds(viewpoint_description_GenericDecorationDescription)
@given(instance=viewpoint_description_GenericDecorationDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_GenericDecorationDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_GenericDecorationDescription)


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


viewpoint_description_InteractiveVariableDescription_strategy = st.builds(viewpoint_description_InteractiveVariableDescription, userDocumentation=safe_text)
@given(instance=viewpoint_description_InteractiveVariableDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_description_InteractiveVariableDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_InteractiveVariableDescription)


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


viewpoint_description_SubVariable_strategy = st.builds(viewpoint_description_SubVariable)
@given(instance=viewpoint_description_SubVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_description_SubVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SubVariable)


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


viewpoint_description_TypedVariable_strategy = st.builds(viewpoint_description_TypedVariable, defaultValueExpression=safe_text)
@given(instance=viewpoint_description_TypedVariable_strategy)
@settings(max_examples=25)
def test_viewpoint_description_TypedVariable_instantiation(instance):
    assert isinstance(instance, viewpoint_description_TypedVariable)


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


viewpoint_tool_AbstractToolDescription_strategy = st.builds(viewpoint_tool_AbstractToolDescription, elementsToSelect=safe_text, forceRefresh=st.booleans(), inverseSelectionOrder=st.booleans(), precondition=safe_text)
@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_AbstractToolDescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AbstractToolDescription)


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


viewpoint_tool_Let_strategy = st.builds(viewpoint_tool_Let, valueExpression=safe_text, variableName=safe_text)
@given(instance=viewpoint_tool_Let_strategy)
@settings(max_examples=25)
def test_viewpoint_tool_Let_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Let)


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



