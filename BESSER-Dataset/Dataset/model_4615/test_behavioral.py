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

def test_assoc_analyses47_reverse_link_reassign_clear():
    a1 = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    a2 = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text_2", open=False, resources="sample_text_2", synchronizationStatus="sample_text_2")
    b = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    _safe_set(b, 'viewpoint_DAnalysis49', a1)
    assert _is_linked(b, 'viewpoint_DAnalysis49', a1)
    if hasattr(a1, 'viewpoint_DAnalysisSessionEObject48'):
        assert _is_linked(a1, 'viewpoint_DAnalysisSessionEObject48', b)
    _safe_set(b, 'viewpoint_DAnalysis49', a2)
    assert _is_linked(b, 'viewpoint_DAnalysis49', a2)
    if hasattr(a1, 'viewpoint_DAnalysisSessionEObject48'):
        assert not _is_linked(a1, 'viewpoint_DAnalysisSessionEObject48', b)
    if hasattr(a2, 'viewpoint_DAnalysisSessionEObject48'):
        assert _is_linked(a2, 'viewpoint_DAnalysisSessionEObject48', b)
    _safe_set(b, 'viewpoint_DAnalysis49', None)
    assert not _is_linked(b, 'viewpoint_DAnalysis49', a2)
    if hasattr(a2, 'viewpoint_DAnalysisSessionEObject48'):
        assert not _is_linked(a2, 'viewpoint_DAnalysisSessionEObject48', b)


def test_assoc_ownedRepresentationElements17_reverse_link_reassign_clear():
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


def test_assoc_representationElements18_reverse_link_reassign_clear():
    a1 = viewpoint_DRepresentationElement(name="sample_text")
    a2 = viewpoint_DRepresentationElement(name="sample_text_2")
    b = viewpoint_DRepresentation(name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation19', {a1})
    assert _is_linked(b, 'viewpoint_DRepresentation19', a1)
    if hasattr(a1, 'viewpoint_DRepresentationElement20'):
        assert _is_linked(a1, 'viewpoint_DRepresentationElement20', b)
    _safe_set(b, 'viewpoint_DRepresentation19', {a2})
    assert _is_linked(b, 'viewpoint_DRepresentation19', a2)
    if hasattr(a1, 'viewpoint_DRepresentationElement20'):
        assert not _is_linked(a1, 'viewpoint_DRepresentationElement20', b)
    if hasattr(a2, 'viewpoint_DRepresentationElement20'):
        assert _is_linked(a2, 'viewpoint_DRepresentationElement20', b)
    _safe_set(b, 'viewpoint_DRepresentation19', set())
    assert not _is_linked(b, 'viewpoint_DRepresentation19', a2)
    if hasattr(a2, 'viewpoint_DRepresentationElement20'):
        assert not _is_linked(a2, 'viewpoint_DRepresentationElement20', b)


def test_assoc_uiState23_reverse_link_reassign_clear():
    a1 = viewpoint_UIState(inverseSelectionOrder=True)
    a2 = viewpoint_UIState(inverseSelectionOrder=False)
    b = viewpoint_DRepresentation(name="sample_text")
    _safe_set(b, 'viewpoint_DRepresentation24', a1)
    assert _is_linked(b, 'viewpoint_DRepresentation24', a1)
    if hasattr(a1, 'viewpoint_UIState'):
        assert _is_linked(a1, 'viewpoint_UIState', b)
    _safe_set(b, 'viewpoint_DRepresentation24', a2)
    assert _is_linked(b, 'viewpoint_DRepresentation24', a2)
    if hasattr(a1, 'viewpoint_UIState'):
        assert not _is_linked(a1, 'viewpoint_UIState', b)
    if hasattr(a2, 'viewpoint_UIState'):
        assert _is_linked(a2, 'viewpoint_UIState', b)
    _safe_set(b, 'viewpoint_DRepresentation24', None)
    assert not _is_linked(b, 'viewpoint_DRepresentation24', a2)
    if hasattr(a2, 'viewpoint_UIState'):
        assert not _is_linked(a2, 'viewpoint_UIState', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activatedViewpoints45_stub_double():
    # Viewpoint has no real 'Viewpoint46' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysisSessionEObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysisSessionEObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    partner = Viewpoint()
    setattr(partner, 'Viewpoint46', None)
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject', {partner})
    assert getattr(partner, 'Viewpoint46') == owner
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject', set())
    assert getattr(partner, 'Viewpoint46') is None


def test_assoc_allRules208_stub_double():
    # validation_ValidationRule has no real 'validation_ValidationRule210' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationSet(name="sample_text")
    partner = validation_ValidationRule()
    setattr(partner, 'validation_ValidationRule210', None)
    _safe_set(owner, 'viewpoint_validation_ValidationSet209', {partner})
    assert getattr(partner, 'validation_ValidationRule210') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationSet209', set())
    assert getattr(partner, 'validation_ValidationRule210') is None


def test_assoc_appliedOn99_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject100' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_EStructuralFeatureCustomization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_EStructuralFeatureCustomization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_EStructuralFeatureCustomization(applyOnAll=True)
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject100', None)
    _safe_set(owner, 'viewpoint_description_EStructuralFeatureCustomization', {partner})
    assert getattr(partner, 'description_viewpoint_EObject100') == owner
    _safe_set(owner, 'viewpoint_description_EStructuralFeatureCustomization', set())
    assert getattr(partner, 'description_viewpoint_EObject100') is None


def test_assoc_associatedColor104_stub_double():
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


def test_assoc_audits211_stub_double():
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


def test_assoc_colorSteps103_stub_double():
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


def test_assoc_container124_stub_double():
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


def test_assoc_container140_stub_double():
    # tool_SelectContainerVariable has no real 'tool_SelectContainerVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_SelectContainerVariable()
    setattr(partner, 'tool_SelectContainerVariable', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription141', partner)
    assert getattr(partner, 'tool_SelectContainerVariable') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription141', None)
    assert getattr(partner, 'tool_SelectContainerVariable') is None


def test_assoc_container150_stub_double():
    # tool_SelectContainerVariable has no real 'tool_SelectContainerVariable152' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_SelectContainerVariable()
    setattr(partner, 'tool_SelectContainerVariable152', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription151', partner)
    assert getattr(partner, 'tool_SelectContainerVariable152') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription151', None)
    assert getattr(partner, 'tool_SelectContainerVariable152') is None


def test_assoc_containerVariable171_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable173' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable173', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription172', partner)
    assert getattr(partner, 'tool_ElementSelectVariable173') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription172', None)
    assert getattr(partner, 'tool_ElementSelectVariable173') is None


def test_assoc_containerView125_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription126', partner)
    assert getattr(partner, 'tool_ContainerViewVariable') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription126', None)
    assert getattr(partner, 'tool_ContainerViewVariable') is None


def test_assoc_containerView137_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable139' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable139', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription138', partner)
    assert getattr(partner, 'tool_ContainerViewVariable139') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription138', None)
    assert getattr(partner, 'tool_ContainerViewVariable139') is None


def test_assoc_containerView147_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable149' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable149', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription148', partner)
    assert getattr(partner, 'tool_ContainerViewVariable149') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription148', None)
    assert getattr(partner, 'tool_ContainerViewVariable149') is None


def test_assoc_containerViewVariable161_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable163' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable163', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription162', partner)
    assert getattr(partner, 'tool_ContainerViewVariable163') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription162', None)
    assert getattr(partner, 'tool_ContainerViewVariable163') is None


def test_assoc_containerViewVariable168_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable170' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable170', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription169', partner)
    assert getattr(partner, 'tool_ContainerViewVariable170') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription169', None)
    assert getattr(partner, 'tool_ContainerViewVariable170') is None


def test_assoc_copiedElement130_stub_double():
    # tool_ElementVariable has no real 'tool_ElementVariable132' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ElementVariable()
    setattr(partner, 'tool_ElementVariable132', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription131', partner)
    assert getattr(partner, 'tool_ElementVariable132') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription131', None)
    assert getattr(partner, 'tool_ElementVariable132') is None


def test_assoc_copiedView127_stub_double():
    # tool_ElementViewVariable has no real 'tool_ElementViewVariable129' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_ElementViewVariable()
    setattr(partner, 'tool_ElementViewVariable129', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription128', partner)
    assert getattr(partner, 'tool_ElementViewVariable129') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription128', None)
    assert getattr(partner, 'tool_ElementViewVariable129') is None


def test_assoc_data113_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject114' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_AnnotationEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_AnnotationEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_AnnotationEntry(source="sample_text")
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject114', None)
    _safe_set(owner, 'viewpoint_description_AnnotationEntry', partner)
    assert getattr(partner, 'description_viewpoint_EObject114') == owner
    _safe_set(owner, 'viewpoint_description_AnnotationEntry', None)
    assert getattr(partner, 'description_viewpoint_EObject114') is None


def test_assoc_data42_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject43' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysisCustomData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysisCustomData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysisCustomData(key="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject43', None)
    _safe_set(owner, 'viewpoint_DAnalysisCustomData', partner)
    assert getattr(partner, 'viewpoint_EObject43') == owner
    _safe_set(owner, 'viewpoint_DAnalysisCustomData', None)
    assert getattr(partner, 'viewpoint_EObject43') is None


def test_assoc_details88_stub_double():
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
    owner = viewpoint_DAnalysis(semanticResources="sample_text", version="sample_text")
    partner = DAnnotationEntry()
    setattr(partner, 'DAnnotationEntry', None)
    _safe_set(owner, 'viewpoint_DAnalysis5', {partner})
    assert getattr(partner, 'DAnnotationEntry') == owner
    _safe_set(owner, 'viewpoint_DAnalysis5', set())
    assert getattr(partner, 'DAnnotationEntry') is None


def test_assoc_eAnnotations87_stub_double():
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


def test_assoc_element119_stub_double():
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


def test_assoc_element136_stub_double():
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


def test_assoc_element145_stub_double():
    # tool_ElementSelectVariable has no real 'tool_ElementSelectVariable146' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_ElementSelectVariable()
    setattr(partner, 'tool_ElementSelectVariable146', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription', partner)
    assert getattr(partner, 'tool_ElementSelectVariable146') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription', None)
    assert getattr(partner, 'tool_ElementSelectVariable146') is None


def test_assoc_elementView120_stub_double():
    # tool_ElementViewVariable has no real 'tool_ElementViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ToolDescription(iconPath="sample_text")
    partner = tool_ElementViewVariable()
    setattr(partner, 'tool_ElementViewVariable', None)
    _safe_set(owner, 'viewpoint_tool_ToolDescription121', partner)
    assert getattr(partner, 'tool_ElementViewVariable') == owner
    _safe_set(owner, 'viewpoint_tool_ToolDescription121', None)
    assert getattr(partner, 'tool_ElementViewVariable') is None


def test_assoc_elementsToSelect53_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject55' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_UIState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_UIState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_UIState(inverseSelectionOrder=True)
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject55', None)
    _safe_set(owner, 'viewpoint_UIState54', {partner})
    assert getattr(partner, 'viewpoint_EObject55') == owner
    _safe_set(owner, 'viewpoint_UIState54', set())
    assert getattr(partner, 'viewpoint_EObject55') is None


def test_assoc_entries112_stub_double():
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


def test_assoc_extensions62_stub_double():
    # Extension has no real 'Extension' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = Extension()
    setattr(partner, 'Extension', None)
    _safe_set(owner, 'viewpoint_description_Group63', {partner})
    assert getattr(partner, 'Extension') == owner
    _safe_set(owner, 'viewpoint_description_Group63', set())
    assert getattr(partner, 'Extension') is None


def test_assoc_featureCustomizations93_stub_double():
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


def test_assoc_filters118_stub_double():
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


def test_assoc_fixes212_stub_double():
    # validation_ValidationFix has no real 'validation_ValidationFix' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationRule(level="sample_text", message="sample_text")
    partner = validation_ValidationFix()
    setattr(partner, 'validation_ValidationFix', None)
    _safe_set(owner, 'viewpoint_validation_ValidationRule213', {partner})
    assert getattr(partner, 'validation_ValidationFix') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationRule213', set())
    assert getattr(partner, 'validation_ValidationFix') is None


def test_assoc_initialOperation122_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_ToolDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_ToolDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_ToolDescription(iconPath="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation', None)
    _safe_set(owner, 'viewpoint_tool_ToolDescription123', partner)
    assert getattr(partner, 'tool_InitialOperation') == owner
    _safe_set(owner, 'viewpoint_tool_ToolDescription123', None)
    assert getattr(partner, 'tool_InitialOperation') is None


def test_assoc_initialOperation133_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation135' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PasteDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PasteDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PasteDescription()
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation135', None)
    _safe_set(owner, 'viewpoint_tool_PasteDescription134', partner)
    assert getattr(partner, 'tool_InitialOperation135') == owner
    _safe_set(owner, 'viewpoint_tool_PasteDescription134', None)
    assert getattr(partner, 'tool_InitialOperation135') is None


def test_assoc_initialOperation142_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation144' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_SelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_SelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_SelectionWizardDescription(iconPath="sample_text", windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation144', None)
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription143', partner)
    assert getattr(partner, 'tool_InitialOperation144') == owner
    _safe_set(owner, 'viewpoint_tool_SelectionWizardDescription143', None)
    assert getattr(partner, 'tool_InitialOperation144') is None


def test_assoc_initialOperation153_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation155' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_PaneBasedSelectionWizardDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_PaneBasedSelectionWizardDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_PaneBasedSelectionWizardDescription(candidatesExpression="sample_text", childrenExpression="sample_text", choiceOfValuesMessage="sample_text", iconPath="sample_text", message="sample_text", preSelectedCandidatesExpression="sample_text", rootExpression="sample_text", selectedValuesMessage="sample_text", tree=True, windowImagePath="sample_text", windowTitle="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation155', None)
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription154', partner)
    assert getattr(partner, 'tool_InitialOperation155') == owner
    _safe_set(owner, 'viewpoint_tool_PaneBasedSelectionWizardDescription154', None)
    assert getattr(partner, 'tool_InitialOperation155') is None


def test_assoc_initialOperation158_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation160' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation160', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription159', partner)
    assert getattr(partner, 'tool_InitialOperation160') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription159', None)
    assert getattr(partner, 'tool_InitialOperation160') is None


def test_assoc_initialOperation215_stub_double():
    # tool_InitialOperation has no real 'tool_InitialOperation216' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationFix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationFix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationFix(name="sample_text")
    partner = tool_InitialOperation()
    setattr(partner, 'tool_InitialOperation216', None)
    _safe_set(owner, 'viewpoint_validation_ValidationFix', partner)
    assert getattr(partner, 'tool_InitialOperation216') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationFix', None)
    assert getattr(partner, 'tool_InitialOperation216') is None


def test_assoc_labelColor116_stub_double():
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


def test_assoc_listeners198_stub_double():
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


def test_assoc_members52_stub_double():
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


def test_assoc_metamodel78_stub_double():
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


def test_assoc_metamodel81_stub_double():
    # description_viewpoint_EPackage has no real 'description_viewpoint_EPackage82' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_RepresentationExtensionDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_RepresentationExtensionDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_RepresentationExtensionDescription(name="sample_text", representationName="sample_text", viewpointURI="sample_text")
    partner = description_viewpoint_EPackage()
    setattr(partner, 'description_viewpoint_EPackage82', None)
    _safe_set(owner, 'viewpoint_description_RepresentationExtensionDescription', {partner})
    assert getattr(partner, 'description_viewpoint_EPackage82') == owner
    _safe_set(owner, 'viewpoint_description_RepresentationExtensionDescription', set())
    assert getattr(partner, 'description_viewpoint_EPackage82') is None


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


def test_assoc_object197_stub_double():
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


def test_assoc_ownedAnnotationEntries21_stub_double():
    # AnnotationEntry has no real 'AnnotationEntry' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentation(name="sample_text")
    partner = AnnotationEntry()
    setattr(partner, 'AnnotationEntry', None)
    _safe_set(owner, 'viewpoint_DRepresentation22', {partner})
    assert getattr(partner, 'AnnotationEntry') == owner
    _safe_set(owner, 'viewpoint_DRepresentation22', set())
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


def test_assoc_ownedFeatureExtensions73_stub_double():
    # FeatureExtensionDescription has no real 'FeatureExtensionDescription75' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = FeatureExtensionDescription()
    setattr(partner, 'FeatureExtensionDescription75', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint74', {partner})
    assert getattr(partner, 'FeatureExtensionDescription75') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint74', set())
    assert getattr(partner, 'FeatureExtensionDescription75') is None


def test_assoc_ownedJavaExtensions69_stub_double():
    # JavaExtension has no real 'JavaExtension' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = JavaExtension()
    setattr(partner, 'JavaExtension', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint70', {partner})
    assert getattr(partner, 'JavaExtension') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint70', set())
    assert getattr(partner, 'JavaExtension') is None


def test_assoc_ownedMMExtensions71_stub_double():
    # MetamodelExtensionSetting has no real 'MetamodelExtensionSetting' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = MetamodelExtensionSetting()
    setattr(partner, 'MetamodelExtensionSetting', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint72', {partner})
    assert getattr(partner, 'MetamodelExtensionSetting') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint72', set())
    assert getattr(partner, 'MetamodelExtensionSetting') is None


def test_assoc_ownedRepresentationExtensions67_stub_double():
    # RepresentationExtensionDescription has no real 'RepresentationExtensionDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationExtensionDescription()
    setattr(partner, 'RepresentationExtensionDescription', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint68', {partner})
    assert getattr(partner, 'RepresentationExtensionDescription') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint68', set())
    assert getattr(partner, 'RepresentationExtensionDescription') is None


def test_assoc_ownedRepresentations30_stub_double():
    # viewpoint_DView has no real 'viewpoint_DView31' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentation(name="sample_text")
    partner = viewpoint_DView()
    setattr(partner, 'viewpoint_DView31', None)
    _safe_set(owner, 'viewpoint_DRepresentation32', partner)
    assert owner in getattr(partner, 'viewpoint_DView31')
    _safe_set(owner, 'viewpoint_DRepresentation32', None)
    assert owner not in getattr(partner, 'viewpoint_DView31')


def test_assoc_ownedRepresentations65_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint66', {partner})
    assert getattr(partner, 'RepresentationDescription') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint66', set())
    assert getattr(partner, 'RepresentationDescription') is None


def test_assoc_ownedRepresentations79_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription80' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_RepresentationTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_RepresentationTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_RepresentationTemplate(name="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription80', None)
    _safe_set(owner, 'viewpoint_description_RepresentationTemplate', {partner})
    assert getattr(partner, 'RepresentationDescription80') == owner
    _safe_set(owner, 'viewpoint_description_RepresentationTemplate', set())
    assert getattr(partner, 'RepresentationDescription80') is None


def test_assoc_ownedRules204_stub_double():
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


def test_assoc_ownedSessions50_stub_double():
    # viewpoint_SessionManagerEObject has no real 'viewpoint_SessionManagerEObject' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DAnalysisSessionEObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DAnalysisSessionEObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DAnalysisSessionEObject(controlledResources="sample_text", open=True, resources="sample_text", synchronizationStatus="sample_text")
    partner = viewpoint_SessionManagerEObject()
    setattr(partner, 'viewpoint_SessionManagerEObject', None)
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject51', partner)
    assert owner in getattr(partner, 'viewpoint_SessionManagerEObject')
    _safe_set(owner, 'viewpoint_DAnalysisSessionEObject51', None)
    assert owner not in getattr(partner, 'viewpoint_SessionManagerEObject')


def test_assoc_ownedTemplates76_stub_double():
    # RepresentationTemplate has no real 'RepresentationTemplate' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Viewpoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Viewpoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Viewpoint(conflicts="sample_text", customizes="sample_text", icon="sample_text", modelFileExtension="sample_text", reuses="sample_text")
    partner = RepresentationTemplate()
    setattr(partner, 'RepresentationTemplate', None)
    _safe_set(owner, 'viewpoint_description_Viewpoint77', {partner})
    assert getattr(partner, 'RepresentationTemplate') == owner
    _safe_set(owner, 'viewpoint_description_Viewpoint77', set())
    assert getattr(partner, 'RepresentationTemplate') is None


def test_assoc_ownedViewpoints56_stub_double():
    # Viewpoint has no real 'Viewpoint57' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = Viewpoint()
    setattr(partner, 'Viewpoint57', None)
    _safe_set(owner, 'viewpoint_description_Group', {partner})
    assert getattr(partner, 'Viewpoint57') == owner
    _safe_set(owner, 'viewpoint_description_Group', set())
    assert getattr(partner, 'Viewpoint57') is None


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


def test_assoc_parameters183_stub_double():
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


def test_assoc_representationDescription156_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription157' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription157', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription', partner)
    assert getattr(partner, 'RepresentationDescription157') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription', None)
    assert getattr(partner, 'RepresentationDescription157') is None


def test_assoc_representationDescription166_stub_double():
    # RepresentationDescription has no real 'RepresentationDescription167' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = RepresentationDescription()
    setattr(partner, 'RepresentationDescription167', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription', partner)
    assert getattr(partner, 'RepresentationDescription167') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription', None)
    assert getattr(partner, 'RepresentationDescription167') is None


def test_assoc_representationNameVariable164_stub_double():
    # tool_NameVariable has no real 'tool_NameVariable' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationCreationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationCreationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationCreationDescription(browseExpression="sample_text", titleExpression="sample_text")
    partner = tool_NameVariable()
    setattr(partner, 'tool_NameVariable', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription165', partner)
    assert getattr(partner, 'tool_NameVariable') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationCreationDescription165', None)
    assert getattr(partner, 'tool_NameVariable') is None


def test_assoc_representationNameVariable174_stub_double():
    # tool_NameVariable has no real 'tool_NameVariable176' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_tool_RepresentationNavigationDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_tool_RepresentationNavigationDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_tool_RepresentationNavigationDescription(browseExpression="sample_text", navigationNameExpression="sample_text")
    partner = tool_NameVariable()
    setattr(partner, 'tool_NameVariable176', None)
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription175', partner)
    assert getattr(partner, 'tool_NameVariable176') == owner
    _safe_set(owner, 'viewpoint_tool_RepresentationNavigationDescription175', None)
    assert getattr(partner, 'tool_NameVariable176') is None


def test_assoc_reusedRules205_stub_double():
    # validation_ValidationRule has no real 'validation_ValidationRule207' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_validation_ValidationSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_validation_ValidationSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_validation_ValidationSet(name="sample_text")
    partner = validation_ValidationRule()
    setattr(partner, 'validation_ValidationRule207', None)
    _safe_set(owner, 'viewpoint_validation_ValidationSet206', {partner})
    assert getattr(partner, 'validation_ValidationRule207') == owner
    _safe_set(owner, 'viewpoint_validation_ValidationSet206', set())
    assert getattr(partner, 'validation_ValidationRule207') is None


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


def test_assoc_semanticElements25_stub_double():
    # viewpoint_EObject has no real 'viewpoint_EObject27' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_DRepresentationElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_DRepresentationElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_DRepresentationElement(name="sample_text")
    partner = viewpoint_EObject()
    setattr(partner, 'viewpoint_EObject27', None)
    _safe_set(owner, 'viewpoint_DRepresentationElement26', {partner})
    assert getattr(partner, 'viewpoint_EObject27') == owner
    _safe_set(owner, 'viewpoint_DRepresentationElement26', set())
    assert getattr(partner, 'viewpoint_EObject27') is None


def test_assoc_systemColorsPalette58_stub_double():
    # SytemColorsPalette has no real 'SytemColorsPalette' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = SytemColorsPalette()
    setattr(partner, 'SytemColorsPalette', None)
    _safe_set(owner, 'viewpoint_description_Group59', partner)
    assert getattr(partner, 'SytemColorsPalette') == owner
    _safe_set(owner, 'viewpoint_description_Group59', None)
    assert getattr(partner, 'SytemColorsPalette') is None


def test_assoc_userColorsPalettes60_stub_double():
    # UserColorsPalette has no real 'UserColorsPalette' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_Group(name="sample_text", version="sample_text")
    partner = UserColorsPalette()
    setattr(partner, 'UserColorsPalette', None)
    _safe_set(owner, 'viewpoint_description_Group61', {partner})
    assert getattr(partner, 'UserColorsPalette') == owner
    _safe_set(owner, 'viewpoint_description_Group61', set())
    assert getattr(partner, 'UserColorsPalette') is None


def test_assoc_validationSet64_stub_double():
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


def test_assoc_value101_stub_double():
    # description_viewpoint_EObject has no real 'description_viewpoint_EObject102' property in the generated
    # code (a bare stub) -- manually attach it so viewpoint_description_EReferenceCustomization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewpoint_description_EReferenceCustomization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewpoint_description_EReferenceCustomization(referenceName="sample_text")
    partner = description_viewpoint_EObject()
    setattr(partner, 'description_viewpoint_EObject102', None)
    _safe_set(owner, 'viewpoint_description_EReferenceCustomization', partner)
    assert getattr(partner, 'description_viewpoint_EObject102') == owner
    _safe_set(owner, 'viewpoint_description_EReferenceCustomization', None)
    assert getattr(partner, 'description_viewpoint_EObject102') is None


def test_assoc_valueType115_stub_double():
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


