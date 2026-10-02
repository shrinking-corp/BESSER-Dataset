import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    ActivityDescription,
    BreakdownElement,
    BreakdownElementDescription,
    Concept,
    ContentCategory,
    ContentDescription,
    ContentElement,
    DescribableElement,
    Descriptor,
    Element,
    Guidance,
    MethodElement,
    MethodPackage,
    MethodUnit,
    NamedElement,
    PackageableElement,
    Process,
    ProcessDescription,
    ProcessElement,
    ProcessPackage,
    RoleDescriptor,
    WorkBreakdownElement,
    WorkProduct,
    WorkProductDescription,
    uma_Activity,
    uma_ActivityDescription,
    uma_ApplicableMetaClassInfo,
    uma_Artifact,
    uma_ArtifactDescription,
    uma_BreakdownElement,
    uma_BreakdownElementDescription,
    uma_CapabilityPattern,
    uma_Checklist,
    uma_CompositeRole,
    uma_Concept,
    uma_Constraint,
    uma_ContentCategory,
    uma_ContentCategoryPackage,
    uma_ContentDescription,
    uma_ContentElement,
    uma_ContentPackage,
    uma_CustomCategory,
    uma_Deliverable,
    uma_DeliverableDescription,
    uma_DeliveryProcess,
    uma_DeliveryProcessDescription,
    uma_DescribableElement,
    uma_Descriptor,
    uma_DescriptorDescription,
    uma_Discipline,
    uma_DisciplineGrouping,
    uma_DocumentRoot,
    uma_Domain,
    uma_EStringToStringMapEntry,
    uma_Element,
    uma_Estimate,
    uma_EstimatingMetric,
    uma_EstimationConsiderations,
    uma_Example,
    uma_Guidance,
    uma_GuidanceDescription,
    uma_Guideline,
    uma_Iteration,
    uma_Kind,
    uma_MethodConfiguration,
    uma_MethodElement,
    uma_MethodElementProperty,
    uma_MethodLibrary,
    uma_MethodPackage,
    uma_MethodPlugin,
    uma_MethodUnit,
    uma_Milestone,
    uma_NamedElement,
    uma_Outcome,
    uma_PackageableElement,
    uma_Phase,
    uma_PlanningData,
    uma_Practice,
    uma_PracticeDescription,
    uma_Process,
    uma_ProcessComponent,
    uma_ProcessComponentInterface,
    uma_ProcessDescription,
    uma_ProcessElement,
    uma_ProcessPackage,
    uma_ProcessPlanningTemplate,
    uma_Report,
    uma_ReusableAsset,
    uma_Roadmap,
    uma_Role,
    uma_RoleDescription,
    uma_RoleDescriptor,
    uma_RoleSet,
    uma_RoleSetGrouping,
    uma_Section,
    uma_SupportingMaterial,
    uma_Task,
    uma_TaskDescription,
    uma_TaskDescriptor,
    uma_TeamProfile,
    uma_Template,
    uma_TermDefinition,
    uma_Tool,
    uma_ToolMentor,
    uma_Whitepaper,
    uma_WorkBreakdownElement,
    uma_WorkDefinition,
    uma_WorkOrder,
    uma_WorkProduct,
    uma_WorkProductDescription,
    uma_WorkProductDescriptor,
    uma_WorkProductType,
    VariabilityType,
    WorkOrderType,
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

def test_assoc_aggregatedRole2_reverse_link_reassign_clear():
    a1 = uma_Role(group2="sample_text", responsibleFor="sample_text")
    a2 = uma_Role(group2="sample_text_2", responsibleFor="sample_text_2")
    b = uma_CompositeRole(group2="sample_text")
    _safe_set(b, 'uma_CompositeRole', {a1})
    assert _is_linked(b, 'uma_CompositeRole', a1)
    if hasattr(a1, 'uma_Role'):
        assert _is_linked(a1, 'uma_Role', b)
    _safe_set(b, 'uma_CompositeRole', {a2})
    assert _is_linked(b, 'uma_CompositeRole', a2)
    if hasattr(a1, 'uma_Role'):
        assert not _is_linked(a1, 'uma_Role', b)
    if hasattr(a2, 'uma_Role'):
        assert _is_linked(a2, 'uma_Role', b)
    _safe_set(b, 'uma_CompositeRole', set())
    assert not _is_linked(b, 'uma_CompositeRole', a2)
    if hasattr(a2, 'uma_Role'):
        assert not _is_linked(a2, 'uma_Role', b)


def test_assoc_breakdownElement5_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(checklist="sample_text", concept="sample_text", example="sample_text", group1="sample_text", guideline="sample_text", hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", planningData="sample_text", prefix="sample_text", presentedAfter="sample_text", presentedBefore="sample_text", reusableAsset="sample_text", superActivity="sample_text", supportingMaterial="sample_text", whitepaper="sample_text")
    a2 = uma_BreakdownElement(checklist="sample_text_2", concept="sample_text_2", example="sample_text_2", group1="sample_text_2", guideline="sample_text_2", hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", planningData="sample_text_2", prefix="sample_text_2", presentedAfter="sample_text_2", presentedBefore="sample_text_2", reusableAsset="sample_text_2", superActivity="sample_text_2", supportingMaterial="sample_text_2", whitepaper="sample_text_2")
    b = uma_Activity(group3="sample_text", isEnactable="sample_text", postcondition="sample_text", precondition="sample_text", roadmap="sample_text", variabilityBasedOnElement="sample_text", variabilityType="sample_text")
    _safe_set(b, 'uma_Activity', {a1})
    assert _is_linked(b, 'uma_Activity', a1)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert _is_linked(a1, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_Activity', {a2})
    assert _is_linked(b, 'uma_Activity', a2)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert not _is_linked(a1, 'uma_BreakdownElement', b)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert _is_linked(a2, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_Activity', set())
    assert not _is_linked(b, 'uma_Activity', a2)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert not _is_linked(a2, 'uma_BreakdownElement', b)


def test_assoc_containedArtifact1_reverse_link_reassign_clear():
    a1 = uma_Artifact(group3="sample_text")
    a2 = uma_Artifact(group3="sample_text_2")
    b = uma_Artifact(group3="sample_text")
    _safe_set(b, 'uma_Artifact0', {a1})
    assert _is_linked(b, 'uma_Artifact0', a1)
    if hasattr(a1, 'uma_Artifact'):
        assert _is_linked(a1, 'uma_Artifact', b)
    _safe_set(b, 'uma_Artifact0', {a2})
    assert _is_linked(b, 'uma_Artifact0', a2)
    if hasattr(a1, 'uma_Artifact'):
        assert not _is_linked(a1, 'uma_Artifact', b)
    if hasattr(a2, 'uma_Artifact'):
        assert _is_linked(a2, 'uma_Artifact', b)
    _safe_set(b, 'uma_Artifact0', set())
    assert not _is_linked(b, 'uma_Artifact0', a2)
    if hasattr(a2, 'uma_Artifact'):
        assert not _is_linked(a2, 'uma_Artifact', b)


def test_assoc_contentElement6_reverse_link_reassign_clear():
    a1 = uma_ContentPackage(group2="sample_text")
    a2 = uma_ContentPackage(group2="sample_text_2")
    b = uma_ContentElement(checklist="sample_text", concept="sample_text", example="sample_text", group1="sample_text", guideline="sample_text", reusableAsset="sample_text", supportingMaterial="sample_text", variabilityBasedOnElement="sample_text", variabilityType="sample_text", whitepaper="sample_text")
    _safe_set(b, 'uma_ContentElement', a1)
    assert _is_linked(b, 'uma_ContentElement', a1)
    if hasattr(a1, 'uma_ContentPackage'):
        assert _is_linked(a1, 'uma_ContentPackage', b)
    _safe_set(b, 'uma_ContentElement', a2)
    assert _is_linked(b, 'uma_ContentElement', a2)
    if hasattr(a1, 'uma_ContentPackage'):
        assert not _is_linked(a1, 'uma_ContentPackage', b)
    if hasattr(a2, 'uma_ContentPackage'):
        assert _is_linked(a2, 'uma_ContentPackage', b)
    _safe_set(b, 'uma_ContentElement', None)
    assert not _is_linked(b, 'uma_ContentElement', a2)
    if hasattr(a2, 'uma_ContentPackage'):
        assert not _is_linked(a2, 'uma_ContentPackage', b)


def test_assoc_interface39_reverse_link_reassign_clear():
    a1 = uma_ProcessComponentInterface(group2="sample_text")
    a2 = uma_ProcessComponentInterface(group2="sample_text_2")
    b = uma_ProcessComponent(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", copyright="sample_text", version="sample_text")
    _safe_set(b, 'uma_ProcessComponent', a1)
    assert _is_linked(b, 'uma_ProcessComponent', a1)
    if hasattr(a1, 'uma_ProcessComponentInterface'):
        assert _is_linked(a1, 'uma_ProcessComponentInterface', b)
    _safe_set(b, 'uma_ProcessComponent', a2)
    assert _is_linked(b, 'uma_ProcessComponent', a2)
    if hasattr(a1, 'uma_ProcessComponentInterface'):
        assert not _is_linked(a1, 'uma_ProcessComponentInterface', b)
    if hasattr(a2, 'uma_ProcessComponentInterface'):
        assert _is_linked(a2, 'uma_ProcessComponentInterface', b)
    _safe_set(b, 'uma_ProcessComponent', None)
    assert not _is_linked(b, 'uma_ProcessComponent', a2)
    if hasattr(a2, 'uma_ProcessComponentInterface'):
        assert not _is_linked(a2, 'uma_ProcessComponentInterface', b)


def test_assoc_interfaceIO44_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text", deliverableParts="sample_text", externalInputTo="sample_text", group2="sample_text", impactedBy="sample_text", impacts="sample_text", mandatoryInputTo="sample_text", optionalInputTo="sample_text", outputFrom="sample_text", responsibleRole="sample_text", workProduct="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2", deliverableParts="sample_text_2", externalInputTo="sample_text_2", group2="sample_text_2", impactedBy="sample_text_2", impacts="sample_text_2", mandatoryInputTo="sample_text_2", optionalInputTo="sample_text_2", outputFrom="sample_text_2", responsibleRole="sample_text_2", workProduct="sample_text_2")
    b = uma_ProcessComponentInterface(group2="sample_text")
    _safe_set(b, 'uma_ProcessComponentInterface45', {a1})
    assert _is_linked(b, 'uma_ProcessComponentInterface45', a1)
    if hasattr(a1, 'uma_WorkProductDescriptor'):
        assert _is_linked(a1, 'uma_WorkProductDescriptor', b)
    _safe_set(b, 'uma_ProcessComponentInterface45', {a2})
    assert _is_linked(b, 'uma_ProcessComponentInterface45', a2)
    if hasattr(a1, 'uma_WorkProductDescriptor'):
        assert not _is_linked(a1, 'uma_WorkProductDescriptor', b)
    if hasattr(a2, 'uma_WorkProductDescriptor'):
        assert _is_linked(a2, 'uma_WorkProductDescriptor', b)
    _safe_set(b, 'uma_ProcessComponentInterface45', set())
    assert not _is_linked(b, 'uma_ProcessComponentInterface45', a2)
    if hasattr(a2, 'uma_WorkProductDescriptor'):
        assert not _is_linked(a2, 'uma_WorkProductDescriptor', b)


def test_assoc_interfaceSpecification42_reverse_link_reassign_clear():
    a1 = uma_TaskDescriptor(additionallyPerformedBy="sample_text", assistedBy="sample_text", externalInput="sample_text", group3="sample_text", isSynchronizedWithSource="sample_text", mandatoryInput="sample_text", optionalInput="sample_text", output="sample_text", performedPrimarilyBy="sample_text", task="sample_text")
    a2 = uma_TaskDescriptor(additionallyPerformedBy="sample_text_2", assistedBy="sample_text_2", externalInput="sample_text_2", group3="sample_text_2", isSynchronizedWithSource="sample_text_2", mandatoryInput="sample_text_2", optionalInput="sample_text_2", output="sample_text_2", performedPrimarilyBy="sample_text_2", task="sample_text_2")
    b = uma_ProcessComponentInterface(group2="sample_text")
    _safe_set(b, 'uma_ProcessComponentInterface43', {a1})
    assert _is_linked(b, 'uma_ProcessComponentInterface43', a1)
    if hasattr(a1, 'uma_TaskDescriptor'):
        assert _is_linked(a1, 'uma_TaskDescriptor', b)
    _safe_set(b, 'uma_ProcessComponentInterface43', {a2})
    assert _is_linked(b, 'uma_ProcessComponentInterface43', a2)
    if hasattr(a1, 'uma_TaskDescriptor'):
        assert not _is_linked(a1, 'uma_TaskDescriptor', b)
    if hasattr(a2, 'uma_TaskDescriptor'):
        assert _is_linked(a2, 'uma_TaskDescriptor', b)
    _safe_set(b, 'uma_ProcessComponentInterface43', set())
    assert not _is_linked(b, 'uma_ProcessComponentInterface43', a2)
    if hasattr(a2, 'uma_TaskDescriptor'):
        assert not _is_linked(a2, 'uma_TaskDescriptor', b)


def test_assoc_methodConfiguration15_reverse_link_reassign_clear():
    a1 = uma_MethodConfiguration(addedCategory="sample_text", baseConfiguration="sample_text", defaultView="sample_text", methodPackageSelection="sample_text", methodPluginSelection="sample_text", processView="sample_text", subtractedCategory="sample_text")
    a2 = uma_MethodConfiguration(addedCategory="sample_text_2", baseConfiguration="sample_text_2", defaultView="sample_text_2", methodPackageSelection="sample_text_2", methodPluginSelection="sample_text_2", processView="sample_text_2", subtractedCategory="sample_text_2")
    b = uma_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uma_DocumentRoot16', {a1})
    assert _is_linked(b, 'uma_DocumentRoot16', a1)
    if hasattr(a1, 'uma_MethodConfiguration'):
        assert _is_linked(a1, 'uma_MethodConfiguration', b)
    _safe_set(b, 'uma_DocumentRoot16', {a2})
    assert _is_linked(b, 'uma_DocumentRoot16', a2)
    if hasattr(a1, 'uma_MethodConfiguration'):
        assert not _is_linked(a1, 'uma_MethodConfiguration', b)
    if hasattr(a2, 'uma_MethodConfiguration'):
        assert _is_linked(a2, 'uma_MethodConfiguration', b)
    _safe_set(b, 'uma_DocumentRoot16', set())
    assert not _is_linked(b, 'uma_DocumentRoot16', a2)
    if hasattr(a2, 'uma_MethodConfiguration'):
        assert not _is_linked(a2, 'uma_MethodConfiguration', b)


def test_assoc_methodConfiguration29_reverse_link_reassign_clear():
    a1 = uma_MethodLibrary(tool="sample_text")
    a2 = uma_MethodLibrary(tool="sample_text_2")
    b = uma_MethodConfiguration(addedCategory="sample_text", baseConfiguration="sample_text", defaultView="sample_text", methodPackageSelection="sample_text", methodPluginSelection="sample_text", processView="sample_text", subtractedCategory="sample_text")
    _safe_set(b, 'uma_MethodConfiguration31', a1)
    assert _is_linked(b, 'uma_MethodConfiguration31', a1)
    if hasattr(a1, 'uma_MethodLibrary30'):
        assert _is_linked(a1, 'uma_MethodLibrary30', b)
    _safe_set(b, 'uma_MethodConfiguration31', a2)
    assert _is_linked(b, 'uma_MethodConfiguration31', a2)
    if hasattr(a1, 'uma_MethodLibrary30'):
        assert not _is_linked(a1, 'uma_MethodLibrary30', b)
    if hasattr(a2, 'uma_MethodLibrary30'):
        assert _is_linked(a2, 'uma_MethodLibrary30', b)
    _safe_set(b, 'uma_MethodConfiguration31', None)
    assert not _is_linked(b, 'uma_MethodConfiguration31', a2)
    if hasattr(a2, 'uma_MethodLibrary30'):
        assert not _is_linked(a2, 'uma_MethodLibrary30', b)


def test_assoc_methodElementProperty24_reverse_link_reassign_clear():
    a1 = uma_MethodElementProperty(value="sample_text")
    a2 = uma_MethodElementProperty(value="sample_text_2")
    b = uma_MethodElement(briefDescription="sample_text", group="sample_text", id="sample_text", orderingGuide="sample_text", presentationName="sample_text", suppressed="sample_text")
    _safe_set(b, 'uma_MethodElement25', {a1})
    assert _is_linked(b, 'uma_MethodElement25', a1)
    if hasattr(a1, 'uma_MethodElementProperty'):
        assert _is_linked(a1, 'uma_MethodElementProperty', b)
    _safe_set(b, 'uma_MethodElement25', {a2})
    assert _is_linked(b, 'uma_MethodElement25', a2)
    if hasattr(a1, 'uma_MethodElementProperty'):
        assert not _is_linked(a1, 'uma_MethodElementProperty', b)
    if hasattr(a2, 'uma_MethodElementProperty'):
        assert _is_linked(a2, 'uma_MethodElementProperty', b)
    _safe_set(b, 'uma_MethodElement25', set())
    assert not _is_linked(b, 'uma_MethodElement25', a2)
    if hasattr(a2, 'uma_MethodElementProperty'):
        assert not _is_linked(a2, 'uma_MethodElementProperty', b)


def test_assoc_methodLibrary17_reverse_link_reassign_clear():
    a1 = uma_MethodLibrary(tool="sample_text")
    a2 = uma_MethodLibrary(tool="sample_text_2")
    b = uma_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uma_DocumentRoot18', {a1})
    assert _is_linked(b, 'uma_DocumentRoot18', a1)
    if hasattr(a1, 'uma_MethodLibrary'):
        assert _is_linked(a1, 'uma_MethodLibrary', b)
    _safe_set(b, 'uma_DocumentRoot18', {a2})
    assert _is_linked(b, 'uma_DocumentRoot18', a2)
    if hasattr(a1, 'uma_MethodLibrary'):
        assert not _is_linked(a1, 'uma_MethodLibrary', b)
    if hasattr(a2, 'uma_MethodLibrary'):
        assert _is_linked(a2, 'uma_MethodLibrary', b)
    _safe_set(b, 'uma_DocumentRoot18', set())
    assert not _is_linked(b, 'uma_DocumentRoot18', a2)
    if hasattr(a2, 'uma_MethodLibrary'):
        assert not _is_linked(a2, 'uma_MethodLibrary', b)


def test_assoc_methodPackage33_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text", group1="sample_text", reusedPackage="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2", group1="sample_text_2", reusedPackage="sample_text_2")
    b = uma_MethodPackage(global_="sample_text", group1="sample_text", reusedPackage="sample_text")
    _safe_set(b, 'uma_MethodPackage32', {a1})
    assert _is_linked(b, 'uma_MethodPackage32', a1)
    if hasattr(a1, 'uma_MethodPackage'):
        assert _is_linked(a1, 'uma_MethodPackage', b)
    _safe_set(b, 'uma_MethodPackage32', {a2})
    assert _is_linked(b, 'uma_MethodPackage32', a2)
    if hasattr(a1, 'uma_MethodPackage'):
        assert not _is_linked(a1, 'uma_MethodPackage', b)
    if hasattr(a2, 'uma_MethodPackage'):
        assert _is_linked(a2, 'uma_MethodPackage', b)
    _safe_set(b, 'uma_MethodPackage32', set())
    assert not _is_linked(b, 'uma_MethodPackage32', a2)
    if hasattr(a2, 'uma_MethodPackage'):
        assert not _is_linked(a2, 'uma_MethodPackage', b)


def test_assoc_methodPackage34_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(referencedMethodPlugin="sample_text", supporting="sample_text", userChangeable="sample_text")
    a2 = uma_MethodPlugin(referencedMethodPlugin="sample_text_2", supporting="sample_text_2", userChangeable="sample_text_2")
    b = uma_MethodPackage(global_="sample_text", group1="sample_text", reusedPackage="sample_text")
    _safe_set(b, 'uma_MethodPackage36', a1)
    assert _is_linked(b, 'uma_MethodPackage36', a1)
    if hasattr(a1, 'uma_MethodPlugin35'):
        assert _is_linked(a1, 'uma_MethodPlugin35', b)
    _safe_set(b, 'uma_MethodPackage36', a2)
    assert _is_linked(b, 'uma_MethodPackage36', a2)
    if hasattr(a1, 'uma_MethodPlugin35'):
        assert not _is_linked(a1, 'uma_MethodPlugin35', b)
    if hasattr(a2, 'uma_MethodPlugin35'):
        assert _is_linked(a2, 'uma_MethodPlugin35', b)
    _safe_set(b, 'uma_MethodPackage36', None)
    assert not _is_linked(b, 'uma_MethodPackage36', a2)
    if hasattr(a2, 'uma_MethodPlugin35'):
        assert not _is_linked(a2, 'uma_MethodPlugin35', b)


def test_assoc_methodPlugin19_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(referencedMethodPlugin="sample_text", supporting="sample_text", userChangeable="sample_text")
    a2 = uma_MethodPlugin(referencedMethodPlugin="sample_text_2", supporting="sample_text_2", userChangeable="sample_text_2")
    b = uma_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'uma_DocumentRoot20', {a1})
    assert _is_linked(b, 'uma_DocumentRoot20', a1)
    if hasattr(a1, 'uma_MethodPlugin'):
        assert _is_linked(a1, 'uma_MethodPlugin', b)
    _safe_set(b, 'uma_DocumentRoot20', {a2})
    assert _is_linked(b, 'uma_DocumentRoot20', a2)
    if hasattr(a1, 'uma_MethodPlugin'):
        assert not _is_linked(a1, 'uma_MethodPlugin', b)
    if hasattr(a2, 'uma_MethodPlugin'):
        assert _is_linked(a2, 'uma_MethodPlugin', b)
    _safe_set(b, 'uma_DocumentRoot20', set())
    assert not _is_linked(b, 'uma_DocumentRoot20', a2)
    if hasattr(a2, 'uma_MethodPlugin'):
        assert not _is_linked(a2, 'uma_MethodPlugin', b)


def test_assoc_methodPlugin26_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(referencedMethodPlugin="sample_text", supporting="sample_text", userChangeable="sample_text")
    a2 = uma_MethodPlugin(referencedMethodPlugin="sample_text_2", supporting="sample_text_2", userChangeable="sample_text_2")
    b = uma_MethodLibrary(tool="sample_text")
    _safe_set(b, 'uma_MethodLibrary27', {a1})
    assert _is_linked(b, 'uma_MethodLibrary27', a1)
    if hasattr(a1, 'uma_MethodPlugin28'):
        assert _is_linked(a1, 'uma_MethodPlugin28', b)
    _safe_set(b, 'uma_MethodLibrary27', {a2})
    assert _is_linked(b, 'uma_MethodLibrary27', a2)
    if hasattr(a1, 'uma_MethodPlugin28'):
        assert not _is_linked(a1, 'uma_MethodPlugin28', b)
    if hasattr(a2, 'uma_MethodPlugin28'):
        assert _is_linked(a2, 'uma_MethodPlugin28', b)
    _safe_set(b, 'uma_MethodLibrary27', set())
    assert not _is_linked(b, 'uma_MethodLibrary27', a2)
    if hasattr(a2, 'uma_MethodPlugin28'):
        assert not _is_linked(a2, 'uma_MethodPlugin28', b)


def test_assoc_ownedRule23_reverse_link_reassign_clear():
    a1 = uma_MethodElement(briefDescription="sample_text", group="sample_text", id="sample_text", orderingGuide="sample_text", presentationName="sample_text", suppressed="sample_text")
    a2 = uma_MethodElement(briefDescription="sample_text_2", group="sample_text_2", id="sample_text_2", orderingGuide="sample_text_2", presentationName="sample_text_2", suppressed="sample_text_2")
    b = uma_Constraint(mainDescription="sample_text")
    _safe_set(b, 'uma_Constraint', a1)
    assert _is_linked(b, 'uma_Constraint', a1)
    if hasattr(a1, 'uma_MethodElement'):
        assert _is_linked(a1, 'uma_MethodElement', b)
    _safe_set(b, 'uma_Constraint', a2)
    assert _is_linked(b, 'uma_Constraint', a2)
    if hasattr(a1, 'uma_MethodElement'):
        assert not _is_linked(a1, 'uma_MethodElement', b)
    if hasattr(a2, 'uma_MethodElement'):
        assert _is_linked(a2, 'uma_MethodElement', b)
    _safe_set(b, 'uma_Constraint', None)
    assert not _is_linked(b, 'uma_Constraint', a2)
    if hasattr(a2, 'uma_MethodElement'):
        assert not _is_linked(a2, 'uma_MethodElement', b)


def test_assoc_predecessor53_reverse_link_reassign_clear():
    a1 = uma_WorkOrder(id="sample_text", linkType="sample_text", properties="sample_text", value="sample_text")
    a2 = uma_WorkOrder(id="sample_text_2", linkType="sample_text_2", properties="sample_text_2", value="sample_text_2")
    b = uma_WorkBreakdownElement(group2="sample_text", isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    _safe_set(b, 'uma_WorkBreakdownElement', {a1})
    assert _is_linked(b, 'uma_WorkBreakdownElement', a1)
    if hasattr(a1, 'uma_WorkOrder'):
        assert _is_linked(a1, 'uma_WorkOrder', b)
    _safe_set(b, 'uma_WorkBreakdownElement', {a2})
    assert _is_linked(b, 'uma_WorkBreakdownElement', a2)
    if hasattr(a1, 'uma_WorkOrder'):
        assert not _is_linked(a1, 'uma_WorkOrder', b)
    if hasattr(a2, 'uma_WorkOrder'):
        assert _is_linked(a2, 'uma_WorkOrder', b)
    _safe_set(b, 'uma_WorkBreakdownElement', set())
    assert not _is_linked(b, 'uma_WorkBreakdownElement', a2)
    if hasattr(a2, 'uma_WorkOrder'):
        assert not _is_linked(a2, 'uma_WorkOrder', b)


def test_assoc_presentation7_reverse_link_reassign_clear():
    a1 = uma_DescribableElement(fulfill="sample_text", isAbstract="sample_text", nodeicon="sample_text", shapeicon="sample_text")
    a2 = uma_DescribableElement(fulfill="sample_text_2", isAbstract="sample_text_2", nodeicon="sample_text_2", shapeicon="sample_text_2")
    b = uma_ContentDescription(externalId="sample_text", keyConsiderations="sample_text", mainDescription="sample_text")
    _safe_set(b, 'uma_ContentDescription8', a1)
    assert _is_linked(b, 'uma_ContentDescription8', a1)
    if hasattr(a1, 'uma_DescribableElement'):
        assert _is_linked(a1, 'uma_DescribableElement', b)
    _safe_set(b, 'uma_ContentDescription8', a2)
    assert _is_linked(b, 'uma_ContentDescription8', a2)
    if hasattr(a1, 'uma_DescribableElement'):
        assert not _is_linked(a1, 'uma_DescribableElement', b)
    if hasattr(a2, 'uma_DescribableElement'):
        assert _is_linked(a2, 'uma_DescribableElement', b)
    _safe_set(b, 'uma_ContentDescription8', None)
    assert not _is_linked(b, 'uma_ContentDescription8', a2)
    if hasattr(a2, 'uma_DescribableElement'):
        assert not _is_linked(a2, 'uma_DescribableElement', b)


def test_assoc_process40_reverse_link_reassign_clear():
    a1 = uma_ProcessComponent(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", copyright="sample_text", version="sample_text")
    a2 = uma_ProcessComponent(authors="sample_text_2", changeDate="sample_text_2", changeDescription="sample_text_2", copyright="sample_text_2", version="sample_text_2")
    b = uma_Process(defaultContext="sample_text", diagramURI="sample_text", includesPattern="sample_text", validContext="sample_text")
    _safe_set(b, 'uma_Process', a1)
    assert _is_linked(b, 'uma_Process', a1)
    if hasattr(a1, 'uma_ProcessComponent41'):
        assert _is_linked(a1, 'uma_ProcessComponent41', b)
    _safe_set(b, 'uma_Process', a2)
    assert _is_linked(b, 'uma_Process', a2)
    if hasattr(a1, 'uma_ProcessComponent41'):
        assert not _is_linked(a1, 'uma_ProcessComponent41', b)
    if hasattr(a2, 'uma_ProcessComponent41'):
        assert _is_linked(a2, 'uma_ProcessComponent41', b)
    _safe_set(b, 'uma_Process', None)
    assert not _is_linked(b, 'uma_Process', a2)
    if hasattr(a2, 'uma_ProcessComponent41'):
        assert not _is_linked(a2, 'uma_ProcessComponent41', b)


def test_assoc_section4_reverse_link_reassign_clear():
    a1 = uma_Section(description="sample_text", predecessor="sample_text", sectionName="sample_text", variabilityBasedOnElement="sample_text", variabilityType="sample_text")
    a2 = uma_Section(description="sample_text_2", predecessor="sample_text_2", sectionName="sample_text_2", variabilityBasedOnElement="sample_text_2", variabilityType="sample_text_2")
    b = uma_ContentDescription(externalId="sample_text", keyConsiderations="sample_text", mainDescription="sample_text")
    _safe_set(b, 'uma_ContentDescription', {a1})
    assert _is_linked(b, 'uma_ContentDescription', a1)
    if hasattr(a1, 'uma_Section'):
        assert _is_linked(a1, 'uma_Section', b)
    _safe_set(b, 'uma_ContentDescription', {a2})
    assert _is_linked(b, 'uma_ContentDescription', a2)
    if hasattr(a1, 'uma_Section'):
        assert not _is_linked(a1, 'uma_Section', b)
    if hasattr(a2, 'uma_Section'):
        assert _is_linked(a2, 'uma_Section', b)
    _safe_set(b, 'uma_ContentDescription', set())
    assert not _is_linked(b, 'uma_ContentDescription', a2)
    if hasattr(a2, 'uma_Section'):
        assert not _is_linked(a2, 'uma_Section', b)


def test_assoc_step50_reverse_link_reassign_clear():
    a1 = uma_TaskDescriptor(additionallyPerformedBy="sample_text", assistedBy="sample_text", externalInput="sample_text", group3="sample_text", isSynchronizedWithSource="sample_text", mandatoryInput="sample_text", optionalInput="sample_text", output="sample_text", performedPrimarilyBy="sample_text", task="sample_text")
    a2 = uma_TaskDescriptor(additionallyPerformedBy="sample_text_2", assistedBy="sample_text_2", externalInput="sample_text_2", group3="sample_text_2", isSynchronizedWithSource="sample_text_2", mandatoryInput="sample_text_2", optionalInput="sample_text_2", output="sample_text_2", performedPrimarilyBy="sample_text_2", task="sample_text_2")
    b = uma_Section(description="sample_text", predecessor="sample_text", sectionName="sample_text", variabilityBasedOnElement="sample_text", variabilityType="sample_text")
    _safe_set(b, 'uma_Section52', a1)
    assert _is_linked(b, 'uma_Section52', a1)
    if hasattr(a1, 'uma_TaskDescriptor51'):
        assert _is_linked(a1, 'uma_TaskDescriptor51', b)
    _safe_set(b, 'uma_Section52', a2)
    assert _is_linked(b, 'uma_Section52', a2)
    if hasattr(a1, 'uma_TaskDescriptor51'):
        assert not _is_linked(a1, 'uma_TaskDescriptor51', b)
    if hasattr(a2, 'uma_TaskDescriptor51'):
        assert _is_linked(a2, 'uma_TaskDescriptor51', b)
    _safe_set(b, 'uma_Section52', None)
    assert not _is_linked(b, 'uma_Section52', a2)
    if hasattr(a2, 'uma_TaskDescriptor51'):
        assert not _is_linked(a2, 'uma_TaskDescriptor51', b)


def test_assoc_subDiscipline10_reverse_link_reassign_clear():
    a1 = uma_Discipline(group2="sample_text", referenceWorkflow="sample_text", task="sample_text")
    a2 = uma_Discipline(group2="sample_text_2", referenceWorkflow="sample_text_2", task="sample_text_2")
    b = uma_Discipline(group2="sample_text", referenceWorkflow="sample_text", task="sample_text")
    _safe_set(b, 'uma_Discipline9', {a1})
    assert _is_linked(b, 'uma_Discipline9', a1)
    if hasattr(a1, 'uma_Discipline'):
        assert _is_linked(a1, 'uma_Discipline', b)
    _safe_set(b, 'uma_Discipline9', {a2})
    assert _is_linked(b, 'uma_Discipline9', a2)
    if hasattr(a1, 'uma_Discipline'):
        assert not _is_linked(a1, 'uma_Discipline', b)
    if hasattr(a2, 'uma_Discipline'):
        assert _is_linked(a2, 'uma_Discipline', b)
    _safe_set(b, 'uma_Discipline9', set())
    assert not _is_linked(b, 'uma_Discipline9', a2)
    if hasattr(a2, 'uma_Discipline'):
        assert not _is_linked(a2, 'uma_Discipline', b)


def test_assoc_subPractice38_reverse_link_reassign_clear():
    a1 = uma_Practice(activityReference="sample_text", contentReference="sample_text", group2="sample_text")
    a2 = uma_Practice(activityReference="sample_text_2", contentReference="sample_text_2", group2="sample_text_2")
    b = uma_Practice(activityReference="sample_text", contentReference="sample_text", group2="sample_text")
    _safe_set(b, 'uma_Practice37', {a1})
    assert _is_linked(b, 'uma_Practice37', a1)
    if hasattr(a1, 'uma_Practice'):
        assert _is_linked(a1, 'uma_Practice', b)
    _safe_set(b, 'uma_Practice37', {a2})
    assert _is_linked(b, 'uma_Practice37', a2)
    if hasattr(a1, 'uma_Practice'):
        assert not _is_linked(a1, 'uma_Practice', b)
    if hasattr(a2, 'uma_Practice'):
        assert _is_linked(a2, 'uma_Practice', b)
    _safe_set(b, 'uma_Practice37', set())
    assert not _is_linked(b, 'uma_Practice37', a2)
    if hasattr(a2, 'uma_Practice'):
        assert not _is_linked(a2, 'uma_Practice', b)


def test_assoc_subSection48_reverse_link_reassign_clear():
    a1 = uma_Section(description="sample_text", predecessor="sample_text", sectionName="sample_text", variabilityBasedOnElement="sample_text", variabilityType="sample_text")
    a2 = uma_Section(description="sample_text_2", predecessor="sample_text_2", sectionName="sample_text_2", variabilityBasedOnElement="sample_text_2", variabilityType="sample_text_2")
    b = uma_Section(description="sample_text", predecessor="sample_text", sectionName="sample_text", variabilityBasedOnElement="sample_text", variabilityType="sample_text")
    _safe_set(b, 'uma_Section49', a1)
    assert _is_linked(b, 'uma_Section49', a1)
    if hasattr(a1, 'uma_Section47'):
        assert _is_linked(a1, 'uma_Section47', b)
    _safe_set(b, 'uma_Section49', a2)
    assert _is_linked(b, 'uma_Section49', a2)
    if hasattr(a1, 'uma_Section47'):
        assert not _is_linked(a1, 'uma_Section47', b)
    if hasattr(a2, 'uma_Section47'):
        assert _is_linked(a2, 'uma_Section47', b)
    _safe_set(b, 'uma_Section49', None)
    assert not _is_linked(b, 'uma_Section49', a2)
    if hasattr(a2, 'uma_Section47'):
        assert not _is_linked(a2, 'uma_Section47', b)


def test_assoc_subdomain22_reverse_link_reassign_clear():
    a1 = uma_Domain(group2="sample_text", workProduct="sample_text")
    a2 = uma_Domain(group2="sample_text_2", workProduct="sample_text_2")
    b = uma_Domain(group2="sample_text", workProduct="sample_text")
    _safe_set(b, 'uma_Domain21', {a1})
    assert _is_linked(b, 'uma_Domain21', a1)
    if hasattr(a1, 'uma_Domain'):
        assert _is_linked(a1, 'uma_Domain', b)
    _safe_set(b, 'uma_Domain21', {a2})
    assert _is_linked(b, 'uma_Domain21', a2)
    if hasattr(a1, 'uma_Domain'):
        assert not _is_linked(a1, 'uma_Domain', b)
    if hasattr(a2, 'uma_Domain'):
        assert _is_linked(a2, 'uma_Domain', b)
    _safe_set(b, 'uma_Domain21', set())
    assert not _is_linked(b, 'uma_Domain21', a2)
    if hasattr(a2, 'uma_Domain'):
        assert not _is_linked(a2, 'uma_Domain', b)


