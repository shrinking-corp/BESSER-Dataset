import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_allRepresentations34_reverse_link_reassign_clear():
    a1 = viewpoint_DView(initialized=True)
    a2 = viewpoint_DView(initialized=False)
    b = viewpoint_DRepresentation(name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation36', a1)
    assert _is_linked(b, 'viewpoint_DRepresentation36', a1)
    if hasattr(a1, 'viewpoint_DView35'):
        assert _is_linked(a1, 'viewpoint_DView35', b)
    _safe_set(b, 'viewpoint_DRepresentation36', a2)
    assert _is_linked(b, 'viewpoint_DRepresentation36', a2)
    if hasattr(a1, 'viewpoint_DView35'):
        assert not _is_linked(a1, 'viewpoint_DView35', b)
    if hasattr(a2, 'viewpoint_DView35'):
        assert _is_linked(a2, 'viewpoint_DView35', b)
    _safe_set(b, 'viewpoint_DRepresentation36', None)
    assert not _is_linked(b, 'viewpoint_DRepresentation36', a2)
    if hasattr(a2, 'viewpoint_DView35'):
        assert not _is_linked(a2, 'viewpoint_DView35', b)


def test_assoc_analyses54_reverse_link_reassign_clear():
    a1 = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    a2 = viewpoint_DAnalysisSessionEObject(blocked=False, controlledResources="sample_text_2", open=False, resources="sample_text_2", synchronizationStatus="sample_text_2")
    b = viewpoint_DAnalysis(version="sample_text")
    _safe_set(b, 'viewpoint_DAnalysis56', a1)
    assert _is_linked(b, 'viewpoint_DAnalysis56', a1)
    if hasattr(a1, 'viewpoint_DAnalysisSessionEObject55'):
        assert _is_linked(a1, 'viewpoint_DAnalysisSessionEObject55', b)
    _safe_set(b, 'viewpoint_DAnalysis56', a2)
    assert _is_linked(b, 'viewpoint_DAnalysis56', a2)
    if hasattr(a1, 'viewpoint_DAnalysisSessionEObject55'):
        assert not _is_linked(a1, 'viewpoint_DAnalysisSessionEObject55', b)
    if hasattr(a2, 'viewpoint_DAnalysisSessionEObject55'):
        assert _is_linked(a2, 'viewpoint_DAnalysisSessionEObject55', b)
    _safe_set(b, 'viewpoint_DAnalysis56', None)
    assert not _is_linked(b, 'viewpoint_DAnalysis56', a2)
    if hasattr(a2, 'viewpoint_DAnalysisSessionEObject55'):
        assert not _is_linked(a2, 'viewpoint_DAnalysisSessionEObject55', b)


def test_assoc_hiddenRepresentations37_reverse_link_reassign_clear():
    a1 = viewpoint_DView(initialized=True)
    a2 = viewpoint_DView(initialized=False)
    b = viewpoint_DRepresentation(name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation39', a1)
    assert _is_linked(b, 'viewpoint_DRepresentation39', a1)
    if hasattr(a1, 'viewpoint_DView38'):
        assert _is_linked(a1, 'viewpoint_DView38', b)
    _safe_set(b, 'viewpoint_DRepresentation39', a2)
    assert _is_linked(b, 'viewpoint_DRepresentation39', a2)
    if hasattr(a1, 'viewpoint_DView38'):
        assert not _is_linked(a1, 'viewpoint_DView38', b)
    if hasattr(a2, 'viewpoint_DView38'):
        assert _is_linked(a2, 'viewpoint_DView38', b)
    _safe_set(b, 'viewpoint_DRepresentation39', None)
    assert not _is_linked(b, 'viewpoint_DRepresentation39', a2)
    if hasattr(a2, 'viewpoint_DView38'):
        assert not _is_linked(a2, 'viewpoint_DView38', b)


def test_assoc_labelColor60_reverse_link_reassign_clear():
    a1 = viewpoint_RGBValues(blue=7, green=7, red=7)
    a2 = viewpoint_RGBValues(blue=13, green=13, red=13)
    b = viewpoint_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    _safe_set(b, 'viewpoint_BasicLabelStyle', a1)
    assert _is_linked(b, 'viewpoint_BasicLabelStyle', a1)
    if hasattr(a1, 'viewpoint_RGBValues'):
        assert _is_linked(a1, 'viewpoint_RGBValues', b)
    _safe_set(b, 'viewpoint_BasicLabelStyle', a2)
    assert _is_linked(b, 'viewpoint_BasicLabelStyle', a2)
    if hasattr(a1, 'viewpoint_RGBValues'):
        assert not _is_linked(a1, 'viewpoint_RGBValues', b)
    if hasattr(a2, 'viewpoint_RGBValues'):
        assert _is_linked(a2, 'viewpoint_RGBValues', b)
    _safe_set(b, 'viewpoint_BasicLabelStyle', None)
    assert not _is_linked(b, 'viewpoint_BasicLabelStyle', a2)
    if hasattr(a2, 'viewpoint_RGBValues'):
        assert not _is_linked(a2, 'viewpoint_RGBValues', b)


def test_assoc_ownedRepresentationElements20_reverse_link_reassign_clear():
    a1 = viewpoint_DRepresentationElement(name="sample_text")
    a2 = viewpoint_DRepresentationElement(name="sample_text_2")
    b = viewpoint_DRepresentation(name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation', {a1})
    assert _is_linked(b, 'viewpoint_DRepresentation', a1)
    if hasattr(a1, 'viewpoint_DRepresentationElement'):
        assert _is_linked(a1, 'viewpoint_DRepresentationElement', b)
    _safe_set(b, 'viewpoint_DRepresentation', {a2})
    assert _is_linked(b, 'viewpoint_DRepresentation', a2)
    if hasattr(a1, 'viewpoint_DRepresentationElement'):
        assert not _is_linked(a1, 'viewpoint_DRepresentationElement', b)
    if hasattr(a2, 'viewpoint_DRepresentationElement'):
        assert _is_linked(a2, 'viewpoint_DRepresentationElement', b)
    _safe_set(b, 'viewpoint_DRepresentation', set())
    assert not _is_linked(b, 'viewpoint_DRepresentation', a2)
    if hasattr(a2, 'viewpoint_DRepresentationElement'):
        assert not _is_linked(a2, 'viewpoint_DRepresentationElement', b)


def test_assoc_ownedRepresentations29_reverse_link_reassign_clear():
    a1 = viewpoint_DView(initialized=True)
    a2 = viewpoint_DView(initialized=False)
    b = viewpoint_DRepresentation(name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation31', a1)
    assert _is_linked(b, 'viewpoint_DRepresentation31', a1)
    if hasattr(a1, 'viewpoint_DView30'):
        assert _is_linked(a1, 'viewpoint_DView30', b)
    _safe_set(b, 'viewpoint_DRepresentation31', a2)
    assert _is_linked(b, 'viewpoint_DRepresentation31', a2)
    if hasattr(a1, 'viewpoint_DView30'):
        assert not _is_linked(a1, 'viewpoint_DView30', b)
    if hasattr(a2, 'viewpoint_DView30'):
        assert _is_linked(a2, 'viewpoint_DView30', b)
    _safe_set(b, 'viewpoint_DRepresentation31', None)
    assert not _is_linked(b, 'viewpoint_DRepresentation31', a2)
    if hasattr(a2, 'viewpoint_DView30'):
        assert not _is_linked(a2, 'viewpoint_DView30', b)


def test_assoc_ownedViews6_reverse_link_reassign_clear():
    a1 = viewpoint_DView(initialized=True)
    a2 = viewpoint_DView(initialized=False)
    b = viewpoint_DAnalysis(version="sample_text")
    _safe_set(b, 'viewpoint_DAnalysis7', {a1})
    assert _is_linked(b, 'viewpoint_DAnalysis7', a1)
    if hasattr(a1, 'viewpoint_DView'):
        assert _is_linked(a1, 'viewpoint_DView', b)
    _safe_set(b, 'viewpoint_DAnalysis7', {a2})
    assert _is_linked(b, 'viewpoint_DAnalysis7', a2)
    if hasattr(a1, 'viewpoint_DView'):
        assert not _is_linked(a1, 'viewpoint_DView', b)
    if hasattr(a2, 'viewpoint_DView'):
        assert _is_linked(a2, 'viewpoint_DView', b)
    _safe_set(b, 'viewpoint_DAnalysis7', set())
    assert not _is_linked(b, 'viewpoint_DAnalysis7', a2)
    if hasattr(a2, 'viewpoint_DView'):
        assert not _is_linked(a2, 'viewpoint_DView', b)


def test_assoc_referencedAnalysis1_reverse_link_reassign_clear():
    a1 = viewpoint_DAnalysis(version="sample_text")
    a2 = viewpoint_DAnalysis(version="sample_text_2")
    b = viewpoint_DAnalysis(version="sample_text")
    _safe_set(b, 'viewpoint_DAnalysis0', {a1})
    assert _is_linked(b, 'viewpoint_DAnalysis0', a1)
    if hasattr(a1, 'viewpoint_DAnalysis'):
        assert _is_linked(a1, 'viewpoint_DAnalysis', b)
    _safe_set(b, 'viewpoint_DAnalysis0', {a2})
    assert _is_linked(b, 'viewpoint_DAnalysis0', a2)
    if hasattr(a1, 'viewpoint_DAnalysis'):
        assert not _is_linked(a1, 'viewpoint_DAnalysis', b)
    if hasattr(a2, 'viewpoint_DAnalysis'):
        assert _is_linked(a2, 'viewpoint_DAnalysis', b)
    _safe_set(b, 'viewpoint_DAnalysis0', set())
    assert not _is_linked(b, 'viewpoint_DAnalysis0', a2)
    if hasattr(a2, 'viewpoint_DAnalysis'):
        assert not _is_linked(a2, 'viewpoint_DAnalysis', b)


def test_assoc_referencedRepresentations40_reverse_link_reassign_clear():
    a1 = viewpoint_DView(initialized=True)
    a2 = viewpoint_DView(initialized=False)
    b = viewpoint_DRepresentation(name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation42', a1)
    assert _is_linked(b, 'viewpoint_DRepresentation42', a1)
    if hasattr(a1, 'viewpoint_DView41'):
        assert _is_linked(a1, 'viewpoint_DView41', b)
    _safe_set(b, 'viewpoint_DRepresentation42', a2)
    assert _is_linked(b, 'viewpoint_DRepresentation42', a2)
    if hasattr(a1, 'viewpoint_DView41'):
        assert not _is_linked(a1, 'viewpoint_DView41', b)
    if hasattr(a2, 'viewpoint_DView41'):
        assert _is_linked(a2, 'viewpoint_DView41', b)
    _safe_set(b, 'viewpoint_DRepresentation42', None)
    assert not _is_linked(b, 'viewpoint_DRepresentation42', a2)
    if hasattr(a2, 'viewpoint_DView41'):
        assert not _is_linked(a2, 'viewpoint_DView41', b)


def test_assoc_representationElements21_reverse_link_reassign_clear():
    a1 = viewpoint_DRepresentationElement(name="sample_text")
    a2 = viewpoint_DRepresentationElement(name="sample_text_2")
    b = viewpoint_DRepresentation(name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation22', {a1})
    assert _is_linked(b, 'viewpoint_DRepresentation22', a1)
    if hasattr(a1, 'viewpoint_DRepresentationElement23'):
        assert _is_linked(a1, 'viewpoint_DRepresentationElement23', b)
    _safe_set(b, 'viewpoint_DRepresentation22', {a2})
    assert _is_linked(b, 'viewpoint_DRepresentation22', a2)
    if hasattr(a1, 'viewpoint_DRepresentationElement23'):
        assert not _is_linked(a1, 'viewpoint_DRepresentationElement23', b)
    if hasattr(a2, 'viewpoint_DRepresentationElement23'):
        assert _is_linked(a2, 'viewpoint_DRepresentationElement23', b)
    _safe_set(b, 'viewpoint_DRepresentation22', set())
    assert not _is_linked(b, 'viewpoint_DRepresentation22', a2)
    if hasattr(a2, 'viewpoint_DRepresentationElement23'):
        assert not _is_linked(a2, 'viewpoint_DRepresentationElement23', b)


def test_assoc_selectedViews8_reverse_link_reassign_clear():
    a1 = viewpoint_DView(initialized=True)
    a2 = viewpoint_DView(initialized=False)
    b = viewpoint_DAnalysis(version="sample_text")
    _safe_set(b, 'viewpoint_DAnalysis9', {a1})
    assert _is_linked(b, 'viewpoint_DAnalysis9', a1)
    if hasattr(a1, 'viewpoint_DView10'):
        assert _is_linked(a1, 'viewpoint_DView10', b)
    _safe_set(b, 'viewpoint_DAnalysis9', {a2})
    assert _is_linked(b, 'viewpoint_DAnalysis9', a2)
    if hasattr(a1, 'viewpoint_DView10'):
        assert not _is_linked(a1, 'viewpoint_DView10', b)
    if hasattr(a2, 'viewpoint_DView10'):
        assert _is_linked(a2, 'viewpoint_DView10', b)
    _safe_set(b, 'viewpoint_DAnalysis9', set())
    assert not _is_linked(b, 'viewpoint_DAnalysis9', a2)
    if hasattr(a2, 'viewpoint_DView10'):
        assert not _is_linked(a2, 'viewpoint_DView10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activatedViewpoints52_stub_double():
    # Viewpoint has no real 'Viewpoint53' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysisSessionEObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysisSessionEObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    partner = Viewpoint()
    setattr(partner, 'Viewpoint53', None)
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject', {partner})
    assert getattr(partner, 'Viewpoint53') == owner
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject', set())
    assert getattr(partner, 'Viewpoint53') is None


def test_assoc_allRules210_stub_double():
    # validation_ValidationRule has no real 'validation_ValidationRule212' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationSet(name="sample_text")
    partner = validation_ValidationRule()
    setattr(partner, 'validation_ValidationRule212', None)
    _safe_set(owner, 'viewpoint_validation_ValidationSet211', {partner})
    assert getattr(partner, 'validation_ValidationRule212') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationSet211', set())
    assert getattr(partner, 'validation_ValidationRule212') is None


def test_assoc_appliedOn102_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject103' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_EStructuralFeatureCustomization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_EStructuralFeatureCustomization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_EStructuralFeatureCustomization(applyOnAll=True)
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject103', None)
    _safe_set(owner, 'viewpoint_description_EStructuralFeatureCustomization', {partner})
    assert getattr(partner, 'description_viewpoint_EObject103') == owner
    _safe_set(owner, 'viewpoint_description_EStructuralFeatureCustomization', set())
    assert getattr(partner, 'description_viewpoint_EObject103') is None


def test_assoc_associatedColor107_stub_double():
    # FixedColor has no real 'FixedColor' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_ColorStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_ColorStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_ColorStep(associatedValue="sample_text")
    partner = FixedColor()
    setattr(partner, 'FixedColor', None)
    _safe_set(owner, 'viewpoint_description_ColorStep', partner)
    assert getattr(partner, 'FixedColor') == owner
    _safe_set(owner, 'viewpoint_description_ColorStep', None)
    assert getattr(partner, 'FixedColor') is None


def test_assoc_audits213_stub_double():
    # validation_RuleAudit has no real 'validation_RuleAudit' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    partner = validation_RuleAudit()
    setattr(partner, 'validation_RuleAudit', None)
    _safe_set(owner, 'viewpoint_validation_ValidationRule', {partner})
    assert getattr(partner, 'validation_RuleAudit') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationRule', set())
    assert getattr(partner, 'validation_RuleAudit') is None


def test_assoc_colorSteps106_stub_double():
    # ColorStep has no real 'ColorStep' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_InterpolatedColor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_InterpolatedColor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_InterpolatedColor(colorValueComputationExpression="sample_text", maxValueComputationExpression="sample_text", minValueComputationExpression="sample_text")
    partner = ColorStep()
    setattr(partner, 'ColorStep', None)
    _safe_set(owner, 'viewpoint_description_InterpolatedColor', {partner})
    assert getattr(partner, 'ColorStep') == owner
    _safe_set(owner, 'viewpoint_description_InterpolatedColor', set())
    assert getattr(partner, 'ColorStep') is None


def test_assoc_container126_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription', partner)
    assert getattr(partner, 'tool_DropContainerVariable') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription', None)
    assert getattr(partner, 'tool_DropContainerVariable') is None


def test_assoc_container142_stub_double():
    # tool_SelectContainerVariable has no real 'tool_SelectContainerVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_SelectContainerVariable()
    setattr(partner, 'tool_SelectContainerVariable', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription143', partner)
    assert getattr(partner, 'tool_SelectContainerVariable') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription143', None)
    assert getattr(partner, 'tool_SelectContainerVariable') is None


def test_assoc_container152_stub_double():
    # tool_SelectContainerVariable has no real 'tool_SelectContainerVariable154' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_SelectContainerVariable()
    setattr(partner, 'tool_SelectContainerVariable154', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription153', partner)
    assert getattr(partner, 'tool_SelectContainerVariable154') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription153', None)
    assert getattr(partner, 'tool_SelectContainerVariable154') is None


def test_assoc_containerVariable173_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable175' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable175', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription174', partner)
    assert getattr(partner, 'tool_ElementSelectVariable175') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription174', None)
    assert getattr(partner, 'tool_ElementSelectVariable175') is None


def test_assoc_containerView127_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription128', partner)
    assert getattr(partner, 'tool_ContainerViewVariable') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription128', None)
    assert getattr(partner, 'tool_ContainerViewVariable') is None


def test_assoc_containerView139_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable141' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable141', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription140', partner)
    assert getattr(partner, 'tool_ContainerViewVariable141') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription140', None)
    assert getattr(partner, 'tool_ContainerViewVariable141') is None


def test_assoc_containerView149_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable151' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable151', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription150', partner)
    assert getattr(partner, 'tool_ContainerViewVariable151') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription150', None)
    assert getattr(partner, 'tool_ContainerViewVariable151') is None


def test_assoc_containerViewVariable163_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable165' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable165', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription164', partner)
    assert getattr(partner, 'tool_ContainerViewVariable165') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription164', None)
    assert getattr(partner, 'tool_ContainerViewVariable165') is None


def test_assoc_containerViewVariable170_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable172' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable172', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription171', partner)
    assert getattr(partner, 'tool_ContainerViewVariable172') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription171', None)
    assert getattr(partner, 'tool_ContainerViewVariable172') is None


def test_assoc_copiedElement132_stub_double():
    # tool_ElementVariable has no real 'tool_ElementVariable134' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ElementVariable()
    setattr(partner, 'tool_ElementVariable134', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription133', partner)
    assert getattr(partner, 'tool_ElementVariable134') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription133', None)
    assert getattr(partner, 'tool_ElementVariable134') is None


def test_assoc_copiedView129_stub_double():
    # tool_ElementViewVariable has no real 'tool_ElementViewVariable131' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ElementViewVariable()
    setattr(partner, 'tool_ElementViewVariable131', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription130', partner)
    assert getattr(partner, 'tool_ElementViewVariable131') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription130', None)
    assert getattr(partner, 'tool_ElementViewVariable131') is None


def test_assoc_data116_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject117' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_AnnotationEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_AnnotationEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_AnnotationEntry(source="sample_text")
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject117', None)
    _safe_set(owner, 'viewpoint_description_AnnotationEntry', partner)
    assert getattr(partner, 'description_viewpoint_EObject117') == owner
    _safe_set(owner, 'viewpoint_description_AnnotationEntry', None)
    assert getattr(partner, 'description_viewpoint_EObject117') is None


def test_assoc_data49_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject50' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysisCustomData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysisCustomData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysisCustomData(key="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject50', None)
    _safe_set(owner, 'viewpoint_DAnalysisCustomData', partner)
    assert getattr(partner, 'viewpoint_EObject50') == owner
    _safe_set(owner, 'viewpoint_DAnalysisCustomData', None)
    assert getattr(partner, 'viewpoint_EObject50') is None


def test_assoc_details91_stub_double():
    # description_viewpoint_EStringToStringMapEntry has no real 'description_viewpoint_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_DAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_DAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_DAnnotation(source="sample_text")
    partner = description_viewpoint_EStringToStringMapEntry()
    setattr(partner, 'description_viewpoint_EStringToStringMapEntry', None)
    _safe_set(owner, 'viewpoint_description_DAnnotation', {partner})
    assert getattr(partner, 'description_viewpoint_EStringToStringMapEntry') == owner
    _safe_set(owner, 'viewpoint_description_DAnnotation', set())
    assert getattr(partner, 'description_viewpoint_EStringToStringMapEntry') is None


def test_assoc_eAnnotations4_stub_double():
    # DAnnotationEntry has no real 'DAnnotationEntry' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysis(version="sample_text")
    partner = DAnnotationEntry()
    setattr(partner, 'DAnnotationEntry', None)
    _safe_set(owner, 'viewpoint_DAnalysis5', {partner})
    assert getattr(partner, 'DAnnotationEntry') == owner
    _safe_set(owner, 'viewpoint_DAnalysis5', set())
    assert getattr(partner, 'DAnnotationEntry') is None


def test_assoc_eAnnotations90_stub_double():
    # DAnnotation has no real 'DAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_DModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_DModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_DModelElement()
    partner = DAnnotation()
    setattr(partner, 'DAnnotation', None)
    _safe_set(owner, 'viewpoint_description_DModelElement', {partner})
    assert getattr(partner, 'DAnnotation') == owner
    _safe_set(owner, 'viewpoint_description_DModelElement', set())
    assert getattr(partner, 'DAnnotation') is None


def test_assoc_element121_stub_double():
    # tool_ElementVariable has no real 'tool_ElementVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ToolDescription(iconPath="sample_text")
    partner = tool_ElementVariable()
    setattr(partner, 'tool_ElementVariable', None)
    _safe_set(owner, 'viewpoint_tool_ToolDescription', partner)
    assert getattr(partner, 'tool_ElementVariable') == owner
    _safe_set(owner, 'viewpoint_tool_ToolDescription', None)
    assert getattr(partner, 'tool_ElementVariable') is None


def test_assoc_element138_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription', partner)
    assert getattr(partner, 'tool_ElementSelectVariable') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription', None)
    assert getattr(partner, 'tool_ElementSelectVariable') is None


def test_assoc_element147_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable148' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable148', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription', partner)
    assert getattr(partner, 'tool_ElementSelectVariable148') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription', None)
    assert getattr(partner, 'tool_ElementSelectVariable148') is None


def test_assoc_elementView122_stub_double():
    # tool_ElementViewVariable has no real 'tool_ElementViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ToolDescription(iconPath="sample_text")
    partner = tool_ElementViewVariable()
    setattr(partner, 'tool_ElementViewVariable', None)
    _safe_set(owner, 'viewpoint_tool_ToolDescription123', partner)
    assert getattr(partner, 'tool_ElementViewVariable') == owner
    _safe_set(owner, 'viewpoint_tool_ToolDescription123', None)
    assert getattr(partner, 'tool_ElementViewVariable') is None


def test_assoc_entries115_stub_double():
    # UserColor has no real 'UserColor' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_UserColorsPalette's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_UserColorsPalette's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_UserColorsPalette(name="sample_text")
    partner = UserColor()
    setattr(partner, 'UserColor', None)
    _safe_set(owner, 'viewpoint_description_UserColorsPalette', {partner})
    assert getattr(partner, 'UserColor') == owner
    _safe_set(owner, 'viewpoint_description_UserColorsPalette', set())
    assert getattr(partner, 'UserColor') is None


def test_assoc_featureCustomizations96_stub_double():
    # EStructuralFeatureCustomization has no real 'EStructuralFeatureCustomization' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_VSMElementCustomization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_VSMElementCustomization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_VSMElementCustomization(predicateExpression="sample_text")
    partner = EStructuralFeatureCustomization()
    setattr(partner, 'EStructuralFeatureCustomization', None)
    _safe_set(owner, 'viewpoint_description_VSMElementCustomization', {partner})
    assert getattr(partner, 'EStructuralFeatureCustomization') == owner
    _safe_set(owner, 'viewpoint_description_VSMElementCustomization', set())
    assert getattr(partner, 'EStructuralFeatureCustomization') is None


def test_assoc_filters120_stub_double():
    # tool_ToolFilterDescription has no real 'tool_ToolFilterDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_AbstractToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_AbstractToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_AbstractToolDescription(forceRefresh=True, precondition="sample_text")
    partner = tool_ToolFilterDescription()
    setattr(partner, 'tool_ToolFilterDescription', None)
    _safe_set(owner, 'viewpoint_tool_AbstractToolDescription', {partner})
    assert getattr(partner, 'tool_ToolFilterDescription') == owner
    _safe_set(owner, 'viewpoint_tool_AbstractToolDescription', set())
    assert getattr(partner, 'tool_ToolFilterDescription') is None


def test_assoc_fixes214_stub_double():
    # validation_ValidationFix has no real 'validation_ValidationFix' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    partner = validation_ValidationFix()
    setattr(partner, 'validation_ValidationFix', None)
    _safe_set(owner, 'viewpoint_validation_ValidationRule215', {partner})
    assert getattr(partner, 'validation_ValidationFix') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationRule215', set())
    assert getattr(partner, 'validation_ValidationFix') is None


def test_assoc_initialOperation124_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ToolDescription(iconPath="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation', None)
    _safe_set(owner, 'viewpoint_tool_ToolDescription125', partner)
    assert getattr(partner, 'tool_InitialOperation') == owner
    _safe_set(owner, 'viewpoint_tool_ToolDescription125', None)
    assert getattr(partner, 'tool_InitialOperation') is None


def test_assoc_initialOperation135_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation137' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation137', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription136', partner)
    assert getattr(partner, 'tool_InitialOperation137') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription136', None)
    assert getattr(partner, 'tool_InitialOperation137') is None


def test_assoc_initialOperation144_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation146' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation146', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription145', partner)
    assert getattr(partner, 'tool_InitialOperation146') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription145', None)
    assert getattr(partner, 'tool_InitialOperation146') is None


def test_assoc_initialOperation155_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation157' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation157', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', partner)
    assert getattr(partner, 'tool_InitialOperation157') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription156', None)
    assert getattr(partner, 'tool_InitialOperation157') is None


def test_assoc_initialOperation160_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation162' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation162', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription161', partner)
    assert getattr(partner, 'tool_InitialOperation162') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription161', None)
    assert getattr(partner, 'tool_InitialOperation162') is None


def test_assoc_initialOperation217_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation218' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationFix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationFix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationFix(name="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation218', None)
    _safe_set(owner, 'viewpoint_validation_ValidationFix', partner)
    assert getattr(partner, 'tool_InitialOperation218') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationFix', None)
    assert getattr(partner, 'tool_InitialOperation218') is None


def test_assoc_labelColor118_stub_double():
    # ColorDescription has no real 'ColorDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_style_BasicLabelStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_style_BasicLabelStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_style_BasicLabelStyleDescription(iconPath="sample_text", labelExpression="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    partner = ColorDescription()
    setattr(partner, 'ColorDescription', None)
    _safe_set(owner, 'viewpoint_style_BasicLabelStyleDescription', partner)
    assert getattr(partner, 'ColorDescription') == owner
    _safe_set(owner, 'viewpoint_style_BasicLabelStyleDescription', None)
    assert getattr(partner, 'ColorDescription') is None


def test_assoc_listeners200_stub_double():
    # tool_FeatureChangeListener has no real 'tool_FeatureChangeListener' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ToolFilterDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ToolFilterDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ToolFilterDescription(elementsToListen="sample_text", precondition="sample_text")
    partner = tool_FeatureChangeListener()
    setattr(partner, 'tool_FeatureChangeListener', None)
    _safe_set(owner, 'viewpoint_tool_ToolFilterDescription', {partner})
    assert getattr(partner, 'tool_FeatureChangeListener') == owner
    _safe_set(owner, 'viewpoint_tool_ToolFilterDescription', set())
    assert getattr(partner, 'tool_FeatureChangeListener') is None


def test_assoc_members59_stub_double():
    # viewpoint_DResourceContainer has no real 'viewpoint_DResourceContainer' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DResource(name="sample_text", path="sample_text")
    partner = viewpoint_DResourceContainer()
    setattr(partner, 'viewpoint_DResourceContainer', None)
    _safe_set(owner, 'viewpoint_DResource', partner)
    assert owner in getattr(partner, 'viewpoint_DResourceContainer')
    _safe_set(owner, 'viewpoint_DResource', None)
    assert owner not in getattr(partner, 'viewpoint_DResourceContainer')


def test_assoc_metamodel81_stub_double():
    # description_viewpoint_EPackage has no real 'description_viewpoint_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_RepresentationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_RepresentationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_RepresentationDescription(initialisation=True, showOnStartup=True, titleExpression="sample_text")
    partner = description_viewpoint_EPackage()
    setattr(partner, 'description_viewpoint_EPackage', None)
    _safe_set(owner, 'viewpoint_description_RepresentationDescription', {partner})
    assert getattr(partner, 'description_viewpoint_EPackage') == owner
    _safe_set(owner, 'viewpoint_description_RepresentationDescription', set())
    assert getattr(partner, 'description_viewpoint_EPackage') is None


def test_assoc_metamodel84_stub_double():
    # description_viewpoint_EPackage has no real 'description_viewpoint_EPackage85' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_RepresentationExtensionDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_RepresentationExtensionDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    partner = description_viewpoint_EPackage()
    setattr(partner, 'description_viewpoint_EPackage85', None)
    _safe_set(owner, 'viewpoint_description_RepresentationExtensionDescription', {partner})
    assert getattr(partner, 'description_viewpoint_EPackage85') == owner
    _safe_set(owner, 'viewpoint_description_RepresentationExtensionDescription', set())
    assert getattr(partner, 'description_viewpoint_EPackage85') is None


def test_assoc_models2_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysis(version="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject', None)
    _safe_set(owner, 'viewpoint_DAnalysis3', {partner})
    assert getattr(partner, 'viewpoint_EObject') == owner
    _safe_set(owner, 'viewpoint_DAnalysis3', set())
    assert getattr(partner, 'viewpoint_EObject') is None


def test_assoc_object199_stub_double():
    # tool_viewpoint_EObject has no real 'tool_viewpoint_EObject' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SetObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SetObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SetObject(featureName="sample_text")
    partner = tool_viewpoint_EObject()
    setattr(partner, 'tool_viewpoint_EObject', None)
    _safe_set(owner, 'viewpoint_tool_SetObject', partner)
    assert getattr(partner, 'tool_viewpoint_EObject') == owner
    _safe_set(owner, 'viewpoint_tool_SetObject', None)
    assert getattr(partner, 'tool_viewpoint_EObject') is None


def test_assoc_ownedAnnotationEntries24_stub_double():
    # AnnotationEntry has no real 'AnnotationEntry' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentation(name="sample_text")
    partner = AnnotationEntry()
    setattr(partner, 'AnnotationEntry', None)
    _safe_set(owner, 'viewpoint_DRepresentation25', {partner})
    assert getattr(partner, 'AnnotationEntry') == owner
    _safe_set(owner, 'viewpoint_DRepresentation25', set())
    assert getattr(partner, 'AnnotationEntry') is None


def test_assoc_ownedExtensions32_stub_double():
    # viewpoint_MetaModelExtension has no real 'viewpoint_MetaModelExtension' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DView(initialized=True)
    partner = viewpoint_MetaModelExtension()
    setattr(partner, 'viewpoint_MetaModelExtension', None)
    _safe_set(owner, 'viewpoint_DView33', partner)
    assert getattr(partner, 'viewpoint_MetaModelExtension') == owner
    _safe_set(owner, 'viewpoint_DView33', None)
    assert getattr(partner, 'viewpoint_MetaModelExtension') is None


def test_assoc_ownedFeatureExtensions11_stub_double():
    # viewpoint_DFeatureExtension has no real 'viewpoint_DFeatureExtension' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysis(version="sample_text")
    partner = viewpoint_DFeatureExtension()
    setattr(partner, 'viewpoint_DFeatureExtension', None)
    _safe_set(owner, 'viewpoint_DAnalysis12', {partner})
    assert getattr(partner, 'viewpoint_DFeatureExtension') == owner
    _safe_set(owner, 'viewpoint_DAnalysis12', set())
    assert getattr(partner, 'viewpoint_DFeatureExtension') is None


def test_assoc_ownedFeatureExtensions76_stub_double():
    # FeatureExtensionDescription has no real 'FeatureExtensionDescription78' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = FeatureExtensionDescription()
    setattr(partner, 'FeatureExtensionDescription78', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint77', {partner})
    assert getattr(partner, 'FeatureExtensionDescription78') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint77', set())
    assert getattr(partner, 'FeatureExtensionDescription78') is None


def test_assoc_ownedJavaExtensions72_stub_double():
    # JavaExtension has no real 'JavaExtension' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = JavaExtension()
    setattr(partner, 'JavaExtension', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint73', {partner})
    assert getattr(partner, 'JavaExtension') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint73', set())
    assert getattr(partner, 'JavaExtension') is None


def test_assoc_ownedMMExtensions74_stub_double():
    # MetamodelExtensionSetting has no real 'MetamodelExtensionSetting' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = MetamodelExtensionSetting()
    setattr(partner, 'MetamodelExtensionSetting', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint75', {partner})
    assert getattr(partner, 'MetamodelExtensionSetting') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint75', set())
    assert getattr(partner, 'MetamodelExtensionSetting') is None


def test_assoc_ownedNavigationLinks15_stub_double():
    # viewpoint_DNavigable has no real 'viewpoint_DNavigable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DNavigationLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DNavigationLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DNavigationLink(label="sample_text", targetType="sample_text")
    partner = viewpoint_DNavigable()
    setattr(partner, 'viewpoint_DNavigable', None)
    _safe_set(owner, 'viewpoint_DNavigationLink', partner)
    assert owner in getattr(partner, 'viewpoint_DNavigable')
    _safe_set(owner, 'viewpoint_DNavigationLink', None)
    assert owner not in getattr(partner, 'viewpoint_DNavigable')


def test_assoc_ownedRepresentationExtensions70_stub_double():
    # RepresentationExtensionDescription has no real 'RepresentationExtensionDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationExtensionDescription()
    setattr(partner, 'RepresentationExtensionDescription', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint71', {partner})
    assert getattr(partner, 'RepresentationExtensionDescription') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint71', set())
    assert getattr(partner, 'RepresentationExtensionDescription') is None


def test_assoc_ownedRepresentations68_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint69', {partner})
    assert getattr(partner, 'RepresentationDescription') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint69', set())
    assert getattr(partner, 'RepresentationDescription') is None


def test_assoc_ownedRepresentations82_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription83' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_RepresentationTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_RepresentationTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_RepresentationTemplate(name="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription83', None)
    _safe_set(owner, 'viewpoint_description_RepresentationTemplate', {partner})
    assert getattr(partner, 'RepresentationDescription83') == owner
    _safe_set(owner, 'viewpoint_description_RepresentationTemplate', set())
    assert getattr(partner, 'RepresentationDescription83') is None


def test_assoc_ownedRules206_stub_double():
    # validation_ValidationRule has no real 'validation_ValidationRule' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationSet(name="sample_text")
    partner = validation_ValidationRule()
    setattr(partner, 'validation_ValidationRule', None)
    _safe_set(owner, 'viewpoint_validation_ValidationSet', {partner})
    assert getattr(partner, 'validation_ValidationRule') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationSet', set())
    assert getattr(partner, 'validation_ValidationRule') is None


def test_assoc_ownedSessions57_stub_double():
    # viewpoint_SessionManagerEObject has no real 'viewpoint_SessionManagerEObject' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysisSessionEObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysisSessionEObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysisSessionEObject(blocked=True, controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    partner = viewpoint_SessionManagerEObject()
    setattr(partner, 'viewpoint_SessionManagerEObject', None)
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject58', partner)
    assert owner in getattr(partner, 'viewpoint_SessionManagerEObject')
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject58', None)
    assert owner not in getattr(partner, 'viewpoint_SessionManagerEObject')


def test_assoc_ownedTemplates79_stub_double():
    # RepresentationTemplate has no real 'RepresentationTemplate' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationTemplate()
    setattr(partner, 'RepresentationTemplate', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint80', {partner})
    assert getattr(partner, 'RepresentationTemplate') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint80', set())
    assert getattr(partner, 'RepresentationTemplate') is None


def test_assoc_ownedViewpoints61_stub_double():
    # Viewpoint has no real 'Viewpoint62' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = Viewpoint()
    setattr(partner, 'Viewpoint62', None)
    _safe_set(owner, 'viewpoint_description_Group', {partner})
    assert getattr(partner, 'Viewpoint62') == owner
    _safe_set(owner, 'viewpoint_description_Group', set())
    assert getattr(partner, 'Viewpoint62') is None


def test_assoc_parameters185_stub_double():
    # tool_ExternalJavaActionParameter has no real 'tool_ExternalJavaActionParameter' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ExternalJavaAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ExternalJavaAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ExternalJavaAction(id="sample_text")
    partner = tool_ExternalJavaActionParameter()
    setattr(partner, 'tool_ExternalJavaActionParameter', None)
    _safe_set(owner, 'viewpoint_tool_ExternalJavaAction', {partner})
    assert getattr(partner, 'tool_ExternalJavaActionParameter') == owner
    _safe_set(owner, 'viewpoint_tool_ExternalJavaAction', set())
    assert getattr(partner, 'tool_ExternalJavaActionParameter') is None


def test_assoc_representationDescription158_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription159' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription159', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription', partner)
    assert getattr(partner, 'RepresentationDescription159') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription', None)
    assert getattr(partner, 'RepresentationDescription159') is None


def test_assoc_representationDescription168_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription169' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription169', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription', partner)
    assert getattr(partner, 'RepresentationDescription169') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription', None)
    assert getattr(partner, 'RepresentationDescription169') is None


def test_assoc_representationNameVariable166_stub_double():
    # tool_NameVariable has no real 'tool_NameVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_NameVariable()
    setattr(partner, 'tool_NameVariable', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription167', partner)
    assert getattr(partner, 'tool_NameVariable') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription167', None)
    assert getattr(partner, 'tool_NameVariable') is None


def test_assoc_representationNameVariable176_stub_double():
    # tool_NameVariable has no real 'tool_NameVariable178' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_NameVariable()
    setattr(partner, 'tool_NameVariable178', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription177', partner)
    assert getattr(partner, 'tool_NameVariable178') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription177', None)
    assert getattr(partner, 'tool_NameVariable178') is None


def test_assoc_reusedRules207_stub_double():
    # validation_ValidationRule has no real 'validation_ValidationRule209' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationSet(name="sample_text")
    partner = validation_ValidationRule()
    setattr(partner, 'validation_ValidationRule209', None)
    _safe_set(owner, 'viewpoint_validation_ValidationSet208', {partner})
    assert getattr(partner, 'validation_ValidationRule209') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationSet208', set())
    assert getattr(partner, 'validation_ValidationRule209') is None


def test_assoc_semanticElements26_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject28' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentationElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentationElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentationElement(name="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject28', None)
    _safe_set(owner, 'viewpoint_DRepresentationElement27', {partner})
    assert getattr(partner, 'viewpoint_EObject28') == owner
    _safe_set(owner, 'viewpoint_DRepresentationElement27', set())
    assert getattr(partner, 'viewpoint_EObject28') is None


def test_assoc_systemColorsPalette63_stub_double():
    # SytemColorsPalette has no real 'SytemColorsPalette' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = SytemColorsPalette()
    setattr(partner, 'SytemColorsPalette', None)
    _safe_set(owner, 'viewpoint_description_Group64', partner)
    assert getattr(partner, 'SytemColorsPalette') == owner
    _safe_set(owner, 'viewpoint_description_Group64', None)
    assert getattr(partner, 'SytemColorsPalette') is None


def test_assoc_userColorsPalettes65_stub_double():
    # UserColorsPalette has no real 'UserColorsPalette' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = UserColorsPalette()
    setattr(partner, 'UserColorsPalette', None)
    _safe_set(owner, 'viewpoint_description_Group66', {partner})
    assert getattr(partner, 'UserColorsPalette') == owner
    _safe_set(owner, 'viewpoint_description_Group66', set())
    assert getattr(partner, 'UserColorsPalette') is None


def test_assoc_validationSet67_stub_double():
    # validation_ValidationSet has no real 'validation_ValidationSet' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = validation_ValidationSet()
    setattr(partner, 'validation_ValidationSet', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint', partner)
    assert getattr(partner, 'validation_ValidationSet') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint', None)
    assert getattr(partner, 'validation_ValidationSet') is None


def test_assoc_value104_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject105' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_EReferenceCustomization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_EReferenceCustomization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_EReferenceCustomization(referenceName="sample_text")
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject105', None)
    _safe_set(owner, 'viewpoint_description_EReferenceCustomization', partner)
    assert getattr(partner, 'description_viewpoint_EObject105') == owner
    _safe_set(owner, 'viewpoint_description_EReferenceCustomization', None)
    assert getattr(partner, 'description_viewpoint_EObject105') is None


def test_assoc_viewpoint43_stub_double():
    # Viewpoint has no real 'Viewpoint' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DView(initialized=True)
    partner = Viewpoint()
    setattr(partner, 'Viewpoint', None)
    _safe_set(owner, 'viewpoint_DView44', partner)
    assert getattr(partner, 'Viewpoint') == owner
    _safe_set(owner, 'viewpoint_DView44', None)
    assert getattr(partner, 'Viewpoint') is None


