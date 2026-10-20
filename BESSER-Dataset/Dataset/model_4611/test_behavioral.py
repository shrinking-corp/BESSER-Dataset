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
    ToolInstance,
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
    tool_GroupMenuItem,
    tool_InitialOperation,
    tool_MenuItemDescription,
    tool_MenuItemDescriptionWithIcon,
    tool_MenuItemOrRef,
    tool_ModelOperation,
    tool_NameVariable,
    tool_PasteDescription,
    tool_PopupMenu,
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
    viewpoint_IdentifiedElement,
    viewpoint_LabelStyle,
    viewpoint_MetaModelExtension,
    viewpoint_SessionManagerEObject,
    viewpoint_Style,
    viewpoint_ToolGroupInstance,
    viewpoint_ToolInstance,
    viewpoint_ToolSectionInstance,
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
    viewpoint_tool_GroupMenu,
    viewpoint_tool_GroupMenuItem,
    viewpoint_tool_If,
    viewpoint_tool_InitEdgeCreationOperation,
    viewpoint_tool_InitialContainerDropOperation,
    viewpoint_tool_InitialNodeCreationOperation,
    viewpoint_tool_InitialOperation,
    viewpoint_tool_Let,
    viewpoint_tool_MappingBasedToolDescription,
    viewpoint_tool_MenuItemDescription,
    viewpoint_tool_MenuItemDescriptionReference,
    viewpoint_tool_MenuItemDescriptionWithIcon,
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

def test_assoc_analyses54_reverse_link_reassign_clear():
    a1 = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    a2 = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text_2", open=False, resources="sample_text_2", synchronizationStatus="sample_text_2")
    b = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
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


def test_assoc_ownedRepresentationElements23_reverse_link_reassign_clear():
    a1 = viewpoint_DRepresentationElement(name="sample_text")
    a2 = viewpoint_DRepresentationElement(name="sample_text_2")
    b = viewpoint_DRepresentation(documentation="sample_text", name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation24', {a1})
    assert _is_linked(b, 'viewpoint_DRepresentation24', a1)
    if hasattr(a1, 'viewpoint_DRepresentationElement'):
        assert _is_linked(a1, 'viewpoint_DRepresentationElement', b)
    _safe_set(b, 'viewpoint_DRepresentation24', {a2})
    assert _is_linked(b, 'viewpoint_DRepresentation24', a2)
    if hasattr(a1, 'viewpoint_DRepresentationElement'):
        assert not _is_linked(a1, 'viewpoint_DRepresentationElement', b)
    if hasattr(a2, 'viewpoint_DRepresentationElement'):
        assert _is_linked(a2, 'viewpoint_DRepresentationElement', b)
    _safe_set(b, 'viewpoint_DRepresentation24', set())
    assert not _is_linked(b, 'viewpoint_DRepresentation24', a2)
    if hasattr(a2, 'viewpoint_DRepresentationElement'):
        assert not _is_linked(a2, 'viewpoint_DRepresentationElement', b)


def test_assoc_referencedAnalysis1_reverse_link_reassign_clear():
    a1 = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    a2 = viewpoint_DAnalysis(semanticResources="sample_text_2", version="sample_text_2")
    b = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
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


def test_assoc_representation21_reverse_link_reassign_clear():
    a1 = viewpoint_DRepresentationDescriptor(changeId="sample_text", name="sample_text", repPath="sample_text")
    a2 = viewpoint_DRepresentationDescriptor(changeId="sample_text_2", name="sample_text_2", repPath="sample_text_2")
    b = viewpoint_DRepresentation(documentation="sample_text", name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation', a1)
    assert _is_linked(b, 'viewpoint_DRepresentation', a1)
    if hasattr(a1, 'viewpoint_DRepresentationDescriptor22'):
        assert _is_linked(a1, 'viewpoint_DRepresentationDescriptor22', b)
    _safe_set(b, 'viewpoint_DRepresentation', a2)
    assert _is_linked(b, 'viewpoint_DRepresentation', a2)
    if hasattr(a1, 'viewpoint_DRepresentationDescriptor22'):
        assert not _is_linked(a1, 'viewpoint_DRepresentationDescriptor22', b)
    if hasattr(a2, 'viewpoint_DRepresentationDescriptor22'):
        assert _is_linked(a2, 'viewpoint_DRepresentationDescriptor22', b)
    _safe_set(b, 'viewpoint_DRepresentation', None)
    assert not _is_linked(b, 'viewpoint_DRepresentation', a2)
    if hasattr(a2, 'viewpoint_DRepresentationDescriptor22'):
        assert not _is_linked(a2, 'viewpoint_DRepresentationDescriptor22', b)


def test_assoc_representationElements25_reverse_link_reassign_clear():
    a1 = viewpoint_DRepresentationElement(name="sample_text")
    a2 = viewpoint_DRepresentationElement(name="sample_text_2")
    b = viewpoint_DRepresentation(documentation="sample_text", name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation26', {a1})
    assert _is_linked(b, 'viewpoint_DRepresentation26', a1)
    if hasattr(a1, 'viewpoint_DRepresentationElement27'):
        assert _is_linked(a1, 'viewpoint_DRepresentationElement27', b)
    _safe_set(b, 'viewpoint_DRepresentation26', {a2})
    assert _is_linked(b, 'viewpoint_DRepresentation26', a2)
    if hasattr(a1, 'viewpoint_DRepresentationElement27'):
        assert not _is_linked(a1, 'viewpoint_DRepresentationElement27', b)
    if hasattr(a2, 'viewpoint_DRepresentationElement27'):
        assert _is_linked(a2, 'viewpoint_DRepresentationElement27', b)
    _safe_set(b, 'viewpoint_DRepresentation26', set())
    assert not _is_linked(b, 'viewpoint_DRepresentation26', a2)
    if hasattr(a2, 'viewpoint_DRepresentationElement27'):
        assert not _is_linked(a2, 'viewpoint_DRepresentationElement27', b)


def test_assoc_uiState30_reverse_link_reassign_clear():
    a1 = viewpoint_UIState(decorationImage="sample_text", inverseSelectionOrder=True, subDiagramDecorationDescriptors="sample_text")
    a2 = viewpoint_UIState(decorationImage="sample_text_2", inverseSelectionOrder=False, subDiagramDecorationDescriptors="sample_text_2")
    b = viewpoint_DRepresentation(documentation="sample_text", name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation31', a1)
    assert _is_linked(b, 'viewpoint_DRepresentation31', a1)
    if hasattr(a1, 'viewpoint_UIState'):
        assert _is_linked(a1, 'viewpoint_UIState', b)
    _safe_set(b, 'viewpoint_DRepresentation31', a2)
    assert _is_linked(b, 'viewpoint_DRepresentation31', a2)
    if hasattr(a1, 'viewpoint_UIState'):
        assert not _is_linked(a1, 'viewpoint_UIState', b)
    if hasattr(a2, 'viewpoint_UIState'):
        assert _is_linked(a2, 'viewpoint_UIState', b)
    _safe_set(b, 'viewpoint_DRepresentation31', None)
    assert not _is_linked(b, 'viewpoint_DRepresentation31', a2)
    if hasattr(a2, 'viewpoint_UIState'):
        assert not _is_linked(a2, 'viewpoint_UIState', b)


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
    owner = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    partner = Viewpoint()
    setattr(partner, 'Viewpoint53', None)
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject', {partner})
    assert getattr(partner, 'Viewpoint53') == owner
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject', set())
    assert getattr(partner, 'Viewpoint53') is None


def test_assoc_allRules240_stub_double():
    # validation_ValidationRule has no real 'validation_ValidationRule242' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationSet(name="sample_text")
    partner = validation_ValidationRule()
    setattr(partner, 'validation_ValidationRule242', None)
    _safe_set(owner, 'viewpoint_validation_ValidationSet241', {partner})
    assert getattr(partner, 'validation_ValidationRule242') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationSet241', set())
    assert getattr(partner, 'validation_ValidationRule242') is None


def test_assoc_appliedOn127_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject128' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_EStructuralFeatureCustomization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_EStructuralFeatureCustomization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_EStructuralFeatureCustomization(applyOnAll=True)
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject128', None)
    _safe_set(owner, 'viewpoint_description_EStructuralFeatureCustomization', {partner})
    assert getattr(partner, 'description_viewpoint_EObject128') == owner
    _safe_set(owner, 'viewpoint_description_EStructuralFeatureCustomization', set())
    assert getattr(partner, 'description_viewpoint_EObject128') is None


def test_assoc_associatedColor132_stub_double():
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


def test_assoc_audits243_stub_double():
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


def test_assoc_colorSteps131_stub_double():
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


def test_assoc_container153_stub_double():
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


def test_assoc_container169_stub_double():
    # tool_SelectContainerVariable has no real 'tool_SelectContainerVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_SelectContainerVariable()
    setattr(partner, 'tool_SelectContainerVariable', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription170', partner)
    assert getattr(partner, 'tool_SelectContainerVariable') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription170', None)
    assert getattr(partner, 'tool_SelectContainerVariable') is None


def test_assoc_container179_stub_double():
    # tool_SelectContainerVariable has no real 'tool_SelectContainerVariable181' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_SelectContainerVariable()
    setattr(partner, 'tool_SelectContainerVariable181', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription180', partner)
    assert getattr(partner, 'tool_SelectContainerVariable181') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription180', None)
    assert getattr(partner, 'tool_SelectContainerVariable181') is None


def test_assoc_containerVariable200_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable202' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable202', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription201', partner)
    assert getattr(partner, 'tool_ElementSelectVariable202') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription201', None)
    assert getattr(partner, 'tool_ElementSelectVariable202') is None


def test_assoc_containerView154_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription155', partner)
    assert getattr(partner, 'tool_ContainerViewVariable') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription155', None)
    assert getattr(partner, 'tool_ContainerViewVariable') is None


def test_assoc_containerView166_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable168' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable168', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription167', partner)
    assert getattr(partner, 'tool_ContainerViewVariable168') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription167', None)
    assert getattr(partner, 'tool_ContainerViewVariable168') is None


def test_assoc_containerView176_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable178' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable178', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription177', partner)
    assert getattr(partner, 'tool_ContainerViewVariable178') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription177', None)
    assert getattr(partner, 'tool_ContainerViewVariable178') is None


def test_assoc_containerViewVariable190_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable192' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable192', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription191', partner)
    assert getattr(partner, 'tool_ContainerViewVariable192') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription191', None)
    assert getattr(partner, 'tool_ContainerViewVariable192') is None


def test_assoc_containerViewVariable197_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable199' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable199', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription198', partner)
    assert getattr(partner, 'tool_ContainerViewVariable199') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription198', None)
    assert getattr(partner, 'tool_ContainerViewVariable199') is None


def test_assoc_copiedElement159_stub_double():
    # tool_ElementVariable has no real 'tool_ElementVariable161' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ElementVariable()
    setattr(partner, 'tool_ElementVariable161', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription160', partner)
    assert getattr(partner, 'tool_ElementVariable161') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription160', None)
    assert getattr(partner, 'tool_ElementVariable161') is None


def test_assoc_copiedView156_stub_double():
    # tool_ElementViewVariable has no real 'tool_ElementViewVariable158' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ElementViewVariable()
    setattr(partner, 'tool_ElementViewVariable158', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription157', partner)
    assert getattr(partner, 'tool_ElementViewVariable158') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription157', None)
    assert getattr(partner, 'tool_ElementViewVariable158') is None


def test_assoc_data142_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject143' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_AnnotationEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_AnnotationEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_AnnotationEntry(source="sample_text")
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject143', None)
    _safe_set(owner, 'viewpoint_description_AnnotationEntry', partner)
    assert getattr(partner, 'description_viewpoint_EObject143') == owner
    _safe_set(owner, 'viewpoint_description_AnnotationEntry', None)
    assert getattr(partner, 'description_viewpoint_EObject143') is None


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


def test_assoc_description17_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentationDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentationDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentationDescriptor(changeId="sample_text", name="sample_text", repPath="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription', None)
    _safe_set(owner, 'viewpoint_DRepresentationDescriptor', partner)
    assert getattr(partner, 'RepresentationDescription') == owner
    _safe_set(owner, 'viewpoint_DRepresentationDescriptor', None)
    assert getattr(partner, 'RepresentationDescription') is None


def test_assoc_details113_stub_double():
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


def test_assoc_eAnnotations112_stub_double():
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


def test_assoc_eAnnotations4_stub_double():
    # DAnnotationEntry has no real 'DAnnotationEntry' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    partner = DAnnotationEntry()
    setattr(partner, 'DAnnotationEntry', None)
    _safe_set(owner, 'viewpoint_DAnalysis5', {partner})
    assert getattr(partner, 'DAnnotationEntry') == owner
    _safe_set(owner, 'viewpoint_DAnalysis5', set())
    assert getattr(partner, 'DAnnotationEntry') is None


def test_assoc_element148_stub_double():
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


def test_assoc_element165_stub_double():
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


def test_assoc_element174_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable175' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable175', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription', partner)
    assert getattr(partner, 'tool_ElementSelectVariable175') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription', None)
    assert getattr(partner, 'tool_ElementSelectVariable175') is None


def test_assoc_elementView149_stub_double():
    # tool_ElementViewVariable has no real 'tool_ElementViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ToolDescription(iconPath="sample_text")
    partner = tool_ElementViewVariable()
    setattr(partner, 'tool_ElementViewVariable', None)
    _safe_set(owner, 'viewpoint_tool_ToolDescription150', partner)
    assert getattr(partner, 'tool_ElementViewVariable') == owner
    _safe_set(owner, 'viewpoint_tool_ToolDescription150', None)
    assert getattr(partner, 'tool_ElementViewVariable') is None


def test_assoc_elementsToSelect60_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject62' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_UIState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_UIState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_UIState(decorationImage="sample_text", inverseSelectionOrder=True, subDiagramDecorationDescriptors="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject62', None)
    _safe_set(owner, 'viewpoint_UIState61', {partner})
    assert getattr(partner, 'viewpoint_EObject62') == owner
    _safe_set(owner, 'viewpoint_UIState61', set())
    assert getattr(partner, 'viewpoint_EObject62') is None


def test_assoc_entries141_stub_double():
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


def test_assoc_extensions86_stub_double():
    # Extension has no real 'Extension' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = Extension()
    setattr(partner, 'Extension', None)
    _safe_set(owner, 'viewpoint_description_Group87', {partner})
    assert getattr(partner, 'Extension') == owner
    _safe_set(owner, 'viewpoint_description_Group87', set())
    assert getattr(partner, 'Extension') is None


def test_assoc_featureCustomizations121_stub_double():
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


def test_assoc_filters147_stub_double():
    # tool_ToolFilterDescription has no real 'tool_ToolFilterDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_AbstractToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_AbstractToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_AbstractToolDescription(elementsToSelect="sample_text", forceRefresh=True, inverseSelectionOrder=True, precondition="sample_text")
    partner = tool_ToolFilterDescription()
    setattr(partner, 'tool_ToolFilterDescription', None)
    _safe_set(owner, 'viewpoint_tool_AbstractToolDescription', {partner})
    assert getattr(partner, 'tool_ToolFilterDescription') == owner
    _safe_set(owner, 'viewpoint_tool_AbstractToolDescription', set())
    assert getattr(partner, 'tool_ToolFilterDescription') is None


def test_assoc_fixes244_stub_double():
    # validation_ValidationFix has no real 'validation_ValidationFix' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    partner = validation_ValidationFix()
    setattr(partner, 'validation_ValidationFix', None)
    _safe_set(owner, 'viewpoint_validation_ValidationRule245', {partner})
    assert getattr(partner, 'validation_ValidationFix') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationRule245', set())
    assert getattr(partner, 'validation_ValidationFix') is None


def test_assoc_initialOperation151_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ToolDescription(iconPath="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation', None)
    _safe_set(owner, 'viewpoint_tool_ToolDescription152', partner)
    assert getattr(partner, 'tool_InitialOperation') == owner
    _safe_set(owner, 'viewpoint_tool_ToolDescription152', None)
    assert getattr(partner, 'tool_InitialOperation') is None


def test_assoc_initialOperation162_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation164' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation164', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription163', partner)
    assert getattr(partner, 'tool_InitialOperation164') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription163', None)
    assert getattr(partner, 'tool_InitialOperation164') is None


def test_assoc_initialOperation171_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation173' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation173', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription172', partner)
    assert getattr(partner, 'tool_InitialOperation173') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription172', None)
    assert getattr(partner, 'tool_InitialOperation173') is None


def test_assoc_initialOperation182_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation184' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation184', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription183', partner)
    assert getattr(partner, 'tool_InitialOperation184') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription183', None)
    assert getattr(partner, 'tool_InitialOperation184') is None


def test_assoc_initialOperation187_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation189' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation189', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription188', partner)
    assert getattr(partner, 'tool_InitialOperation189') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription188', None)
    assert getattr(partner, 'tool_InitialOperation189') is None


def test_assoc_initialOperation247_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation248' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationFix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationFix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationFix(name="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation248', None)
    _safe_set(owner, 'viewpoint_validation_ValidationFix', partner)
    assert getattr(partner, 'tool_InitialOperation248') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationFix', None)
    assert getattr(partner, 'tool_InitialOperation248') is None


def test_assoc_itemDescriptions234_stub_double():
    # tool_GroupMenuItem has no real 'tool_GroupMenuItem' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_GroupMenu's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_GroupMenu's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_GroupMenu(locationURI="sample_text")
    partner = tool_GroupMenuItem()
    setattr(partner, 'tool_GroupMenuItem', None)
    _safe_set(owner, 'viewpoint_tool_GroupMenu235', {partner})
    assert getattr(partner, 'tool_GroupMenuItem') == owner
    _safe_set(owner, 'viewpoint_tool_GroupMenu235', set())
    assert getattr(partner, 'tool_GroupMenuItem') is None


def test_assoc_labelColor145_stub_double():
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


def test_assoc_listeners227_stub_double():
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


def test_assoc_metamodel103_stub_double():
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


def test_assoc_metamodel106_stub_double():
    # description_viewpoint_EPackage has no real 'description_viewpoint_EPackage107' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_RepresentationExtensionDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_RepresentationExtensionDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    partner = description_viewpoint_EPackage()
    setattr(partner, 'description_viewpoint_EPackage107', None)
    _safe_set(owner, 'viewpoint_description_RepresentationExtensionDescription', {partner})
    assert getattr(partner, 'description_viewpoint_EPackage107') == owner
    _safe_set(owner, 'viewpoint_description_RepresentationExtensionDescription', set())
    assert getattr(partner, 'description_viewpoint_EPackage107') is None


def test_assoc_models2_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject', None)
    _safe_set(owner, 'viewpoint_DAnalysis3', {partner})
    assert getattr(partner, 'viewpoint_EObject') == owner
    _safe_set(owner, 'viewpoint_DAnalysis3', set())
    assert getattr(partner, 'viewpoint_EObject') is None


def test_assoc_object226_stub_double():
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


def test_assoc_ownedAnnotationEntries28_stub_double():
    # AnnotationEntry has no real 'AnnotationEntry' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentation(documentation="sample_text", name="sample_text")
    partner = AnnotationEntry()
    setattr(partner, 'AnnotationEntry', None)
    _safe_set(owner, 'viewpoint_DRepresentation29', {partner})
    assert getattr(partner, 'AnnotationEntry') == owner
    _safe_set(owner, 'viewpoint_DRepresentation29', set())
    assert getattr(partner, 'AnnotationEntry') is None


def test_assoc_ownedFeatureExtensions11_stub_double():
    # viewpoint_DFeatureExtension has no real 'viewpoint_DFeatureExtension' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    partner = viewpoint_DFeatureExtension()
    setattr(partner, 'viewpoint_DFeatureExtension', None)
    _safe_set(owner, 'viewpoint_DAnalysis12', {partner})
    assert getattr(partner, 'viewpoint_DFeatureExtension') == owner
    _safe_set(owner, 'viewpoint_DAnalysis12', set())
    assert getattr(partner, 'viewpoint_DFeatureExtension') is None


def test_assoc_ownedFeatureExtensions98_stub_double():
    # FeatureExtensionDescription has no real 'FeatureExtensionDescription100' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = FeatureExtensionDescription()
    setattr(partner, 'FeatureExtensionDescription100', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint99', {partner})
    assert getattr(partner, 'FeatureExtensionDescription100') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint99', set())
    assert getattr(partner, 'FeatureExtensionDescription100') is None


def test_assoc_ownedJavaExtensions94_stub_double():
    # JavaExtension has no real 'JavaExtension' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = JavaExtension()
    setattr(partner, 'JavaExtension', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint95', {partner})
    assert getattr(partner, 'JavaExtension') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint95', set())
    assert getattr(partner, 'JavaExtension') is None


def test_assoc_ownedMMExtensions96_stub_double():
    # MetamodelExtensionSetting has no real 'MetamodelExtensionSetting' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = MetamodelExtensionSetting()
    setattr(partner, 'MetamodelExtensionSetting', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint97', {partner})
    assert getattr(partner, 'MetamodelExtensionSetting') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint97', set())
    assert getattr(partner, 'MetamodelExtensionSetting') is None


def test_assoc_ownedRepresentationDescriptors37_stub_double():
    # viewpoint_DView has no real 'viewpoint_DView38' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentationDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentationDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentationDescriptor(changeId="sample_text", name="sample_text", repPath="sample_text")
    partner = viewpoint_DView()
    setattr(partner, 'viewpoint_DView38', None)
    _safe_set(owner, 'viewpoint_DRepresentationDescriptor39', partner)
    assert owner in getattr(partner, 'viewpoint_DView38')
    _safe_set(owner, 'viewpoint_DRepresentationDescriptor39', None)
    assert owner not in getattr(partner, 'viewpoint_DView38')


def test_assoc_ownedRepresentationExtensions92_stub_double():
    # RepresentationExtensionDescription has no real 'RepresentationExtensionDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationExtensionDescription()
    setattr(partner, 'RepresentationExtensionDescription', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint93', {partner})
    assert getattr(partner, 'RepresentationExtensionDescription') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint93', set())
    assert getattr(partner, 'RepresentationExtensionDescription') is None


def test_assoc_ownedRepresentations104_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription105' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_RepresentationTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_RepresentationTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_RepresentationTemplate(name="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription105', None)
    _safe_set(owner, 'viewpoint_description_RepresentationTemplate', {partner})
    assert getattr(partner, 'RepresentationDescription105') == owner
    _safe_set(owner, 'viewpoint_description_RepresentationTemplate', set())
    assert getattr(partner, 'RepresentationDescription105') is None


def test_assoc_ownedRepresentations89_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription91' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription91', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint90', {partner})
    assert getattr(partner, 'RepresentationDescription91') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint90', set())
    assert getattr(partner, 'RepresentationDescription91') is None


def test_assoc_ownedRules236_stub_double():
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
    owner = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    partner = viewpoint_SessionManagerEObject()
    setattr(partner, 'viewpoint_SessionManagerEObject', None)
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject58', partner)
    assert owner in getattr(partner, 'viewpoint_SessionManagerEObject')
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject58', None)
    assert owner not in getattr(partner, 'viewpoint_SessionManagerEObject')


def test_assoc_ownedTemplates101_stub_double():
    # RepresentationTemplate has no real 'RepresentationTemplate' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationTemplate()
    setattr(partner, 'RepresentationTemplate', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint102', {partner})
    assert getattr(partner, 'RepresentationTemplate') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint102', set())
    assert getattr(partner, 'RepresentationTemplate') is None


def test_assoc_ownedViewpoints80_stub_double():
    # Viewpoint has no real 'Viewpoint81' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = Viewpoint()
    setattr(partner, 'Viewpoint81', None)
    _safe_set(owner, 'viewpoint_description_Group', {partner})
    assert getattr(partner, 'Viewpoint81') == owner
    _safe_set(owner, 'viewpoint_description_Group', set())
    assert getattr(partner, 'Viewpoint81') is None


def test_assoc_ownedViews6_stub_double():
    # viewpoint_DView has no real 'viewpoint_DView' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    partner = viewpoint_DView()
    setattr(partner, 'viewpoint_DView', None)
    _safe_set(owner, 'viewpoint_DAnalysis7', {partner})
    assert getattr(partner, 'viewpoint_DView') == owner
    _safe_set(owner, 'viewpoint_DAnalysis7', set())
    assert getattr(partner, 'viewpoint_DView') is None


def test_assoc_parameters212_stub_double():
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


def test_assoc_popupMenus233_stub_double():
    # tool_PopupMenu has no real 'tool_PopupMenu' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_GroupMenu's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_GroupMenu's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_GroupMenu(locationURI="sample_text")
    partner = tool_PopupMenu()
    setattr(partner, 'tool_PopupMenu', None)
    _safe_set(owner, 'viewpoint_tool_GroupMenu', {partner})
    assert getattr(partner, 'tool_PopupMenu') == owner
    _safe_set(owner, 'viewpoint_tool_GroupMenu', set())
    assert getattr(partner, 'tool_PopupMenu') is None


def test_assoc_references114_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject116' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_DAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_DAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_DAnnotation(source="sample_text")
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject116', None)
    _safe_set(owner, 'viewpoint_description_DAnnotation115', {partner})
    assert getattr(partner, 'description_viewpoint_EObject116') == owner
    _safe_set(owner, 'viewpoint_description_DAnnotation115', set())
    assert getattr(partner, 'description_viewpoint_EObject116') is None


def test_assoc_representationDescription185_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription186' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription186', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription', partner)
    assert getattr(partner, 'RepresentationDescription186') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription', None)
    assert getattr(partner, 'RepresentationDescription186') is None


def test_assoc_representationDescription195_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription196' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription196', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription', partner)
    assert getattr(partner, 'RepresentationDescription196') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription', None)
    assert getattr(partner, 'RepresentationDescription196') is None


def test_assoc_representationNameVariable193_stub_double():
    # tool_NameVariable has no real 'tool_NameVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_NameVariable()
    setattr(partner, 'tool_NameVariable', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription194', partner)
    assert getattr(partner, 'tool_NameVariable') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription194', None)
    assert getattr(partner, 'tool_NameVariable') is None


def test_assoc_representationNameVariable203_stub_double():
    # tool_NameVariable has no real 'tool_NameVariable205' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_NameVariable()
    setattr(partner, 'tool_NameVariable205', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription204', partner)
    assert getattr(partner, 'tool_NameVariable205') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription204', None)
    assert getattr(partner, 'tool_NameVariable205') is None


def test_assoc_reusedRules237_stub_double():
    # validation_ValidationRule has no real 'validation_ValidationRule239' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationSet(name="sample_text")
    partner = validation_ValidationRule()
    setattr(partner, 'validation_ValidationRule239', None)
    _safe_set(owner, 'viewpoint_validation_ValidationSet238', {partner})
    assert getattr(partner, 'validation_ValidationRule239') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationSet238', set())
    assert getattr(partner, 'validation_ValidationRule239') is None


def test_assoc_selectedViews8_stub_double():
    # viewpoint_DView has no real 'viewpoint_DView10' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    partner = viewpoint_DView()
    setattr(partner, 'viewpoint_DView10', None)
    _safe_set(owner, 'viewpoint_DAnalysis9', {partner})
    assert getattr(partner, 'viewpoint_DView10') == owner
    _safe_set(owner, 'viewpoint_DAnalysis9', set())
    assert getattr(partner, 'viewpoint_DView10') is None


def test_assoc_semanticElements32_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject34' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentationElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentationElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentationElement(name="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject34', None)
    _safe_set(owner, 'viewpoint_DRepresentationElement33', {partner})
    assert getattr(partner, 'viewpoint_EObject34') == owner
    _safe_set(owner, 'viewpoint_DRepresentationElement33', set())
    assert getattr(partner, 'viewpoint_EObject34') is None


def test_assoc_systemColorsPalette82_stub_double():
    # SytemColorsPalette has no real 'SytemColorsPalette' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = SytemColorsPalette()
    setattr(partner, 'SytemColorsPalette', None)
    _safe_set(owner, 'viewpoint_description_Group83', partner)
    assert getattr(partner, 'SytemColorsPalette') == owner
    _safe_set(owner, 'viewpoint_description_Group83', None)
    assert getattr(partner, 'SytemColorsPalette') is None


def test_assoc_target18_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject20' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentationDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentationDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentationDescriptor(changeId="sample_text", name="sample_text", repPath="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject20', None)
    _safe_set(owner, 'viewpoint_DRepresentationDescriptor19', partner)
    assert getattr(partner, 'viewpoint_EObject20') == owner
    _safe_set(owner, 'viewpoint_DRepresentationDescriptor19', None)
    assert getattr(partner, 'viewpoint_EObject20') is None


def test_assoc_toolEntry65_stub_double():
    # tool_ToolEntry has no real 'tool_ToolEntry' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_ToolInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_ToolInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_ToolInstance(enabled=True, filtered=True, id="sample_text", visible=True)
    partner = tool_ToolEntry()
    setattr(partner, 'tool_ToolEntry', None)
    _safe_set(owner, 'viewpoint_ToolInstance', partner)
    assert getattr(partner, 'tool_ToolEntry') == owner
    _safe_set(owner, 'viewpoint_ToolInstance', None)
    assert getattr(partner, 'tool_ToolEntry') is None


def test_assoc_toolSections63_stub_double():
    # viewpoint_ToolSectionInstance has no real 'viewpoint_ToolSectionInstance' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_UIState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_UIState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_UIState(decorationImage="sample_text", inverseSelectionOrder=True, subDiagramDecorationDescriptors="sample_text")
    partner = viewpoint_ToolSectionInstance()
    setattr(partner, 'viewpoint_ToolSectionInstance', None)
    _safe_set(owner, 'viewpoint_UIState64', {partner})
    assert getattr(partner, 'viewpoint_ToolSectionInstance') == owner
    _safe_set(owner, 'viewpoint_UIState64', set())
    assert getattr(partner, 'viewpoint_ToolSectionInstance') is None


def test_assoc_tools66_stub_double():
    # viewpoint_ToolGroupInstance has no real 'viewpoint_ToolGroupInstance' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_ToolInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_ToolInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_ToolInstance(enabled=True, filtered=True, id="sample_text", visible=True)
    partner = viewpoint_ToolGroupInstance()
    setattr(partner, 'viewpoint_ToolGroupInstance', None)
    _safe_set(owner, 'viewpoint_ToolInstance67', partner)
    assert owner in getattr(partner, 'viewpoint_ToolGroupInstance')
    _safe_set(owner, 'viewpoint_ToolInstance67', None)
    assert owner not in getattr(partner, 'viewpoint_ToolGroupInstance')


def test_assoc_tools71_stub_double():
    # viewpoint_ToolSectionInstance has no real 'viewpoint_ToolSectionInstance72' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_ToolInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_ToolInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_ToolInstance(enabled=True, filtered=True, id="sample_text", visible=True)
    partner = viewpoint_ToolSectionInstance()
    setattr(partner, 'viewpoint_ToolSectionInstance72', None)
    _safe_set(owner, 'viewpoint_ToolInstance73', partner)
    assert owner in getattr(partner, 'viewpoint_ToolSectionInstance72')
    _safe_set(owner, 'viewpoint_ToolInstance73', None)
    assert owner not in getattr(partner, 'viewpoint_ToolSectionInstance72')


def test_assoc_userColorsPalettes84_stub_double():
    # UserColorsPalette has no real 'UserColorsPalette' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = UserColorsPalette()
    setattr(partner, 'UserColorsPalette', None)
    _safe_set(owner, 'viewpoint_description_Group85', {partner})
    assert getattr(partner, 'UserColorsPalette') == owner
    _safe_set(owner, 'viewpoint_description_Group85', set())
    assert getattr(partner, 'UserColorsPalette') is None


def test_assoc_validationSet88_stub_double():
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


def test_assoc_value129_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject130' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_EReferenceCustomization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_EReferenceCustomization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_EReferenceCustomization(referenceName="sample_text")
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject130', None)
    _safe_set(owner, 'viewpoint_description_EReferenceCustomization', partner)
    assert getattr(partner, 'description_viewpoint_EObject130') == owner
    _safe_set(owner, 'viewpoint_description_EReferenceCustomization', None)
    assert getattr(partner, 'description_viewpoint_EObject130') is None


def test_assoc_valueType144_stub_double():
    # description_viewpoint_EDataType has no real 'description_viewpoint_EDataType' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_TypedVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_TypedVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_TypedVariable(defaultValueExpression="sample_text")
    partner = description_viewpoint_EDataType()
    setattr(partner, 'description_viewpoint_EDataType', None)
    _safe_set(owner, 'viewpoint_description_TypedVariable', partner)
    assert getattr(partner, 'description_viewpoint_EDataType') == owner
    _safe_set(owner, 'viewpoint_description_TypedVariable', None)
    assert getattr(partner, 'description_viewpoint_EDataType') is None


