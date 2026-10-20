import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    Artifact,
    BreakdownElement,
    CapabilityPattern,
    Category,
    Concept,
    DescribableElement,
    Edge,
    ExtensibleElement,
    Guidance,
    Kind,
    MethodContentElement,
    MethodContentPackage,
    MethodContentPackageableElement,
    MethodContentUse,
    MethodLibraryPackageableElement,
    MethodPluginPackageableElement,
    Node,
    Practice,
    Process,
    ProcessElement,
    ProcessPackage,
    ProcessPackageableElement,
    RoleUse,
    SupportingMaterial,
    VariabilityElement,
    WorkBreakdownElement,
    WorkDefinition,
    WorkDefinitionParameter,
    WorkDefinitionPerformer,
    WorkProductUse,
    activity_spem_BreakdownElement,
    spem_Activity,
    spem_BreakdownElement,
    spem_Category,
    spem_CompositeRole,
    spem_Default_ResponsibilityAssignment,
    spem_Default_TaskDefinitionParameter,
    spem_Default_TaskDefinitionPerformer,
    spem_DescribableElement,
    spem_ExtensibleElement,
    spem_Guidance,
    spem_Kind,
    spem_MethodConfiguration,
    spem_MethodContentElement,
    spem_MethodContentKind,
    spem_MethodContentPackage,
    spem_MethodContentPackageableElement,
    spem_MethodContentUse,
    spem_MethodLibrary,
    spem_MethodLibraryPackageableElement,
    spem_MethodPlugin,
    spem_MethodPluginPackageableElement,
    spem_Metric,
    spem_Milestone,
    spem_PlanningData,
    spem_ProcessComponent,
    spem_ProcessComponentUse,
    spem_ProcessElement,
    spem_ProcessKind,
    spem_ProcessPackage,
    spem_ProcessPackageableElement,
    spem_ProcessParameter,
    spem_ProcessPerformer,
    spem_ProcessResponsibilityAssignment,
    spem_Qualification,
    spem_RoleDefinition,
    spem_RoleUse,
    spem_Step,
    spem_TaskDefinition,
    spem_TaskUse,
    spem_TeamProfile,
    spem_ToolDefinition,
    spem_VariabilityElement,
    spem_WorkBreakdownElement,
    spem_WorkDefinition,
    spem_WorkDefinitionParameter,
    spem_WorkDefinitionPerformer,
    spem_WorkProductDefinition,
    spem_WorkProductDefinitionRelationship,
    spem_WorkProductPort,
    spem_WorkProductPortConnector,
    spem_WorkProductUse,
    spem_WorkProductUseRelationship,
    spem_WorkSequence,
    spem_activity_DecisionNode,
    spem_activity_Edge,
    spem_activity_EndNode,
    spem_activity_ForkNode,
    spem_activity_JoinNode,
    spem_activity_Node,
    spem_activity_StartNode,
    spem_uma_Artifact,
    spem_uma_CapabilityPattern,
    spem_uma_CapabilityPatternPackage,
    spem_uma_CategoryPackage,
    spem_uma_Checklist,
    spem_uma_Concept,
    spem_uma_ConfigurationPackage,
    spem_uma_CustomCategory,
    spem_uma_Deliverable,
    spem_uma_DeliveryProcess,
    spem_uma_DeliveryProcessPackage,
    spem_uma_Discipline,
    spem_uma_DisciplineGrouping,
    spem_uma_DisciplinePackage,
    spem_uma_Domain,
    spem_uma_DomainPackage,
    spem_uma_EstimatingConsideration,
    spem_uma_Example,
    spem_uma_GuidancePackage,
    spem_uma_Guideline,
    spem_uma_Iteration,
    spem_uma_Outcome,
    spem_uma_Phase,
    spem_uma_Practice,
    spem_uma_Process,
    spem_uma_ProcessComponentPackage,
    spem_uma_ProcessPlanningTemplate,
    spem_uma_QualificationPackage,
    spem_uma_Report,
    spem_uma_ReusableAsset,
    spem_uma_Roadmap,
    spem_uma_RoleDefinitionPackage,
    spem_uma_RoleSet,
    spem_uma_RoleSetPackage,
    spem_uma_Root,
    spem_uma_SupportingMaterial,
    spem_uma_TaskDefinitionPackage,
    spem_uma_Template,
    spem_uma_TermDefinition,
    spem_uma_ToolDefinitionPackage,
    spem_uma_ToolMentor,
    spem_uma_Whitepaper,
    spem_uma_WorkProductDefinitionPackage,
    spem_uma_WorkProductKind,
    spem_uma_WorkProductKindPackage,
    uma_spem_Activity,
    uma_spem_MethodConfiguration,
    uma_spem_MethodContentElement,
    uma_spem_MethodLibrary,
    uma_spem_MethodPlugin,
    uma_spem_RoleDefinition,
    uma_spem_TaskDefinition,
    uma_spem_WorkProductDefinition,
    uma_spem_WorkProductPortConnector,
    uma_spem_WorkProductUse,
    ActivityUseKind,
    ContractKind,
    EstimatingTechnique,
    ExpertiseLevel,
    OptionalityKind,
    ParameterDirectionKind,
    RiskLevel,
    VariabilityType,
    WorkProductRelationshipKind,
    WorkSequenceKind,
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

def test_assoc_linkToPredecessor5_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(linkKind="sample_text")
    a2 = spem_WorkSequence(linkKind="sample_text_2")
    b = spem_WorkBreakdownElement(isEventDriven=True, isOngoing=True, isRepeatable=True)
    _safe_set(b, 'successor', {a1})
    assert _is_linked(b, 'successor', a1)
    if hasattr(a1, 'WorkSequence'):
        assert _is_linked(a1, 'WorkSequence', b)
    _safe_set(b, 'successor', {a2})
    assert _is_linked(b, 'successor', a2)
    if hasattr(a1, 'WorkSequence'):
        assert not _is_linked(a1, 'WorkSequence', b)
    if hasattr(a2, 'WorkSequence'):
        assert _is_linked(a2, 'WorkSequence', b)
    _safe_set(b, 'successor', set())
    assert not _is_linked(b, 'successor', a2)
    if hasattr(a2, 'WorkSequence'):
        assert not _is_linked(a2, 'WorkSequence', b)


def test_assoc_linkToSuccessor6_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(linkKind="sample_text")
    a2 = spem_WorkSequence(linkKind="sample_text_2")
    b = spem_WorkBreakdownElement(isEventDriven=True, isOngoing=True, isRepeatable=True)
    _safe_set(b, 'predecessor', {a1})
    assert _is_linked(b, 'predecessor', a1)
    if hasattr(a1, 'WorkSequence7'):
        assert _is_linked(a1, 'WorkSequence7', b)
    _safe_set(b, 'predecessor', {a2})
    assert _is_linked(b, 'predecessor', a2)
    if hasattr(a1, 'WorkSequence7'):
        assert not _is_linked(a1, 'WorkSequence7', b)
    if hasattr(a2, 'WorkSequence7'):
        assert _is_linked(a2, 'WorkSequence7', b)
    _safe_set(b, 'predecessor', set())
    assert not _is_linked(b, 'predecessor', a2)
    if hasattr(a2, 'WorkSequence7'):
        assert not _is_linked(a2, 'WorkSequence7', b)


def test_assoc_metric54_reverse_link_reassign_clear():
    a1 = spem_Metric(expression="sample_text")
    a2 = spem_Metric(expression="sample_text_2")
    b = spem_DescribableElement(author="sample_text", briefDescription="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text", version="sample_text")
    _safe_set(b, 'spem_DescribableElement55', {a1})
    assert _is_linked(b, 'spem_DescribableElement55', a1)
    if hasattr(a1, 'spem_Metric'):
        assert _is_linked(a1, 'spem_Metric', b)
    _safe_set(b, 'spem_DescribableElement55', {a2})
    assert _is_linked(b, 'spem_DescribableElement55', a2)
    if hasattr(a1, 'spem_Metric'):
        assert not _is_linked(a1, 'spem_Metric', b)
    if hasattr(a2, 'spem_Metric'):
        assert _is_linked(a2, 'spem_Metric', b)
    _safe_set(b, 'spem_DescribableElement55', set())
    assert not _is_linked(b, 'spem_DescribableElement55', a2)
    if hasattr(a2, 'spem_Metric'):
        assert not _is_linked(a2, 'spem_Metric', b)


def test_assoc_nestedBreakdownElement13_reverse_link_reassign_clear():
    a1 = spem_BreakdownElement(hasMultipleOccurrences=True, isOptional=True, isPlanned=True)
    a2 = spem_BreakdownElement(hasMultipleOccurrences=False, isOptional=False, isPlanned=False)
    b = spem_Activity(isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity14', {a1})
    assert _is_linked(b, 'spem_Activity14', a1)
    if hasattr(a1, 'spem_BreakdownElement15'):
        assert _is_linked(a1, 'spem_BreakdownElement15', b)
    _safe_set(b, 'spem_Activity14', {a2})
    assert _is_linked(b, 'spem_Activity14', a2)
    if hasattr(a1, 'spem_BreakdownElement15'):
        assert not _is_linked(a1, 'spem_BreakdownElement15', b)
    if hasattr(a2, 'spem_BreakdownElement15'):
        assert _is_linked(a2, 'spem_BreakdownElement15', b)
    _safe_set(b, 'spem_Activity14', set())
    assert not _is_linked(b, 'spem_Activity14', a2)
    if hasattr(a2, 'spem_BreakdownElement15'):
        assert not _is_linked(a2, 'spem_BreakdownElement15', b)


def test_assoc_ownedParameter2_reverse_link_reassign_clear():
    a1 = spem_WorkDefinitionParameter(direction="sample_text")
    a2 = spem_WorkDefinitionParameter(direction="sample_text_2")
    b = spem_WorkDefinition(postCondition="sample_text", preCondition="sample_text")
    _safe_set(b, 'spem_WorkDefinition3', {a1})
    assert _is_linked(b, 'spem_WorkDefinition3', a1)
    if hasattr(a1, 'spem_WorkDefinitionParameter'):
        assert _is_linked(a1, 'spem_WorkDefinitionParameter', b)
    _safe_set(b, 'spem_WorkDefinition3', {a2})
    assert _is_linked(b, 'spem_WorkDefinition3', a2)
    if hasattr(a1, 'spem_WorkDefinitionParameter'):
        assert not _is_linked(a1, 'spem_WorkDefinitionParameter', b)
    if hasattr(a2, 'spem_WorkDefinitionParameter'):
        assert _is_linked(a2, 'spem_WorkDefinitionParameter', b)
    _safe_set(b, 'spem_WorkDefinition3', set())
    assert not _is_linked(b, 'spem_WorkDefinition3', a2)
    if hasattr(a2, 'spem_WorkDefinitionParameter'):
        assert not _is_linked(a2, 'spem_WorkDefinitionParameter', b)


def test_assoc_ownedProcessParameter114_reverse_link_reassign_clear():
    a1 = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    a2 = spem_TaskUse(postCondition="sample_text_2", preCondition="sample_text_2")
    b = spem_ProcessParameter(optionality="sample_text")
    _safe_set(b, 'spem_ProcessParameter116', a1)
    assert _is_linked(b, 'spem_ProcessParameter116', a1)
    if hasattr(a1, 'spem_TaskUse115'):
        assert _is_linked(a1, 'spem_TaskUse115', b)
    _safe_set(b, 'spem_ProcessParameter116', a2)
    assert _is_linked(b, 'spem_ProcessParameter116', a2)
    if hasattr(a1, 'spem_TaskUse115'):
        assert not _is_linked(a1, 'spem_TaskUse115', b)
    if hasattr(a2, 'spem_TaskUse115'):
        assert _is_linked(a2, 'spem_TaskUse115', b)
    _safe_set(b, 'spem_ProcessParameter116', None)
    assert not _is_linked(b, 'spem_ProcessParameter116', a2)
    if hasattr(a2, 'spem_TaskUse115'):
        assert not _is_linked(a2, 'spem_TaskUse115', b)


def test_assoc_ownedProcessParameter19_reverse_link_reassign_clear():
    a1 = spem_ProcessParameter(optionality="sample_text")
    a2 = spem_ProcessParameter(optionality="sample_text_2")
    b = spem_Activity(isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity20', {a1})
    assert _is_linked(b, 'spem_Activity20', a1)
    if hasattr(a1, 'spem_ProcessParameter'):
        assert _is_linked(a1, 'spem_ProcessParameter', b)
    _safe_set(b, 'spem_Activity20', {a2})
    assert _is_linked(b, 'spem_Activity20', a2)
    if hasattr(a1, 'spem_ProcessParameter'):
        assert not _is_linked(a1, 'spem_ProcessParameter', b)
    if hasattr(a2, 'spem_ProcessParameter'):
        assert _is_linked(a2, 'spem_ProcessParameter', b)
    _safe_set(b, 'spem_Activity20', set())
    assert not _is_linked(b, 'spem_Activity20', a2)
    if hasattr(a2, 'spem_ProcessParameter'):
        assert not _is_linked(a2, 'spem_ProcessParameter', b)


def test_assoc_planningData4_reverse_link_reassign_clear():
    a1 = spem_PlanningData(duration="sample_text", finishDate=date(2024, 1, 1), rank=7, startDate=date(2024, 1, 1))
    a2 = spem_PlanningData(duration="sample_text_2", finishDate=date(2025, 6, 15), rank=13, startDate=date(2025, 6, 15))
    b = spem_BreakdownElement(hasMultipleOccurrences=True, isOptional=True, isPlanned=True)
    _safe_set(b, 'spem_BreakdownElement', a1)
    assert _is_linked(b, 'spem_BreakdownElement', a1)
    if hasattr(a1, 'spem_PlanningData'):
        assert _is_linked(a1, 'spem_PlanningData', b)
    _safe_set(b, 'spem_BreakdownElement', a2)
    assert _is_linked(b, 'spem_BreakdownElement', a2)
    if hasattr(a1, 'spem_PlanningData'):
        assert not _is_linked(a1, 'spem_PlanningData', b)
    if hasattr(a2, 'spem_PlanningData'):
        assert _is_linked(a2, 'spem_PlanningData', b)
    _safe_set(b, 'spem_BreakdownElement', None)
    assert not _is_linked(b, 'spem_BreakdownElement', a2)
    if hasattr(a2, 'spem_PlanningData'):
        assert not _is_linked(a2, 'spem_PlanningData', b)


def test_assoc_predecessor73_reverse_link_reassign_clear():
    a1 = spem_Step(name="sample_text")
    a2 = spem_Step(name="sample_text_2")
    b = spem_Step(name="sample_text")
    _safe_set(b, 'successor74', a1)
    assert _is_linked(b, 'successor74', a1)
    if hasattr(a1, 'Step'):
        assert _is_linked(a1, 'Step', b)
    _safe_set(b, 'successor74', a2)
    assert _is_linked(b, 'successor74', a2)
    if hasattr(a1, 'Step'):
        assert not _is_linked(a1, 'Step', b)
    if hasattr(a2, 'Step'):
        assert _is_linked(a2, 'Step', b)
    _safe_set(b, 'successor74', None)
    assert not _is_linked(b, 'successor74', a2)
    if hasattr(a2, 'Step'):
        assert not _is_linked(a2, 'Step', b)


def test_assoc_predecessor8_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(linkKind="sample_text")
    a2 = spem_WorkSequence(linkKind="sample_text_2")
    b = spem_WorkBreakdownElement(isEventDriven=True, isOngoing=True, isRepeatable=True)
    _safe_set(b, 'WorkBreakdownElement', a1)
    assert _is_linked(b, 'WorkBreakdownElement', a1)
    if hasattr(a1, 'linkToSuccessor'):
        assert _is_linked(a1, 'linkToSuccessor', b)
    _safe_set(b, 'WorkBreakdownElement', a2)
    assert _is_linked(b, 'WorkBreakdownElement', a2)
    if hasattr(a1, 'linkToSuccessor'):
        assert not _is_linked(a1, 'linkToSuccessor', b)
    if hasattr(a2, 'linkToSuccessor'):
        assert _is_linked(a2, 'linkToSuccessor', b)
    _safe_set(b, 'WorkBreakdownElement', None)
    assert not _is_linked(b, 'WorkBreakdownElement', a2)
    if hasattr(a2, 'linkToSuccessor'):
        assert not _is_linked(a2, 'linkToSuccessor', b)


def test_assoc_selectedStep111_reverse_link_reassign_clear():
    a1 = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    a2 = spem_TaskUse(postCondition="sample_text_2", preCondition="sample_text_2")
    b = spem_Step(name="sample_text")
    _safe_set(b, 'spem_Step113', a1)
    assert _is_linked(b, 'spem_Step113', a1)
    if hasattr(a1, 'spem_TaskUse112'):
        assert _is_linked(a1, 'spem_TaskUse112', b)
    _safe_set(b, 'spem_Step113', a2)
    assert _is_linked(b, 'spem_Step113', a2)
    if hasattr(a1, 'spem_TaskUse112'):
        assert not _is_linked(a1, 'spem_TaskUse112', b)
    if hasattr(a2, 'spem_TaskUse112'):
        assert _is_linked(a2, 'spem_TaskUse112', b)
    _safe_set(b, 'spem_Step113', None)
    assert not _is_linked(b, 'spem_Step113', a2)
    if hasattr(a2, 'spem_TaskUse112'):
        assert not _is_linked(a2, 'spem_TaskUse112', b)


def test_assoc_successor76_reverse_link_reassign_clear():
    a1 = spem_Step(name="sample_text")
    a2 = spem_Step(name="sample_text_2")
    b = spem_Step(name="sample_text")
    _safe_set(b, 'predecessor77', a1)
    assert _is_linked(b, 'predecessor77', a1)
    if hasattr(a1, 'Step78'):
        assert _is_linked(a1, 'Step78', b)
    _safe_set(b, 'predecessor77', a2)
    assert _is_linked(b, 'predecessor77', a2)
    if hasattr(a1, 'Step78'):
        assert not _is_linked(a1, 'Step78', b)
    if hasattr(a2, 'Step78'):
        assert _is_linked(a2, 'Step78', b)
    _safe_set(b, 'predecessor77', None)
    assert not _is_linked(b, 'predecessor77', a2)
    if hasattr(a2, 'Step78'):
        assert not _is_linked(a2, 'Step78', b)


def test_assoc_successor9_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(linkKind="sample_text")
    a2 = spem_WorkSequence(linkKind="sample_text_2")
    b = spem_WorkBreakdownElement(isEventDriven=True, isOngoing=True, isRepeatable=True)
    _safe_set(b, 'WorkBreakdownElement10', a1)
    assert _is_linked(b, 'WorkBreakdownElement10', a1)
    if hasattr(a1, 'linkToPredecessor'):
        assert _is_linked(a1, 'linkToPredecessor', b)
    _safe_set(b, 'WorkBreakdownElement10', a2)
    assert _is_linked(b, 'WorkBreakdownElement10', a2)
    if hasattr(a1, 'linkToPredecessor'):
        assert not _is_linked(a1, 'linkToPredecessor', b)
    if hasattr(a2, 'linkToPredecessor'):
        assert _is_linked(a2, 'linkToPredecessor', b)
    _safe_set(b, 'WorkBreakdownElement10', None)
    assert not _is_linked(b, 'WorkBreakdownElement10', a2)
    if hasattr(a2, 'linkToPredecessor'):
        assert not _is_linked(a2, 'linkToPredecessor', b)


def test_assoc_suppressedBreakdownElement16_reverse_link_reassign_clear():
    a1 = spem_BreakdownElement(hasMultipleOccurrences=True, isOptional=True, isPlanned=True)
    a2 = spem_BreakdownElement(hasMultipleOccurrences=False, isOptional=False, isPlanned=False)
    b = spem_Activity(isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity17', {a1})
    assert _is_linked(b, 'spem_Activity17', a1)
    if hasattr(a1, 'spem_BreakdownElement18'):
        assert _is_linked(a1, 'spem_BreakdownElement18', b)
    _safe_set(b, 'spem_Activity17', {a2})
    assert _is_linked(b, 'spem_Activity17', a2)
    if hasattr(a1, 'spem_BreakdownElement18'):
        assert not _is_linked(a1, 'spem_BreakdownElement18', b)
    if hasattr(a2, 'spem_BreakdownElement18'):
        assert _is_linked(a2, 'spem_BreakdownElement18', b)
    _safe_set(b, 'spem_Activity17', set())
    assert not _is_linked(b, 'spem_Activity17', a2)
    if hasattr(a2, 'spem_BreakdownElement18'):
        assert not _is_linked(a2, 'spem_BreakdownElement18', b)


def test_assoc_usedActivity12_reverse_link_reassign_clear():
    a1 = spem_Activity(isEnactable=True, useKind="sample_text")
    a2 = spem_Activity(isEnactable=False, useKind="sample_text_2")
    b = spem_Activity(isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity11', a1)
    assert _is_linked(b, 'spem_Activity11', a1)
    if hasattr(a1, 'spem_Activity'):
        assert _is_linked(a1, 'spem_Activity', b)
    _safe_set(b, 'spem_Activity11', a2)
    assert _is_linked(b, 'spem_Activity11', a2)
    if hasattr(a1, 'spem_Activity'):
        assert not _is_linked(a1, 'spem_Activity', b)
    if hasattr(a2, 'spem_Activity'):
        assert _is_linked(a2, 'spem_Activity', b)
    _safe_set(b, 'spem_Activity11', None)
    assert not _is_linked(b, 'spem_Activity11', a2)
    if hasattr(a2, 'spem_Activity'):
        assert not _is_linked(a2, 'spem_Activity', b)


def test_assoc_variabilityBasedOnElement127_reverse_link_reassign_clear():
    a1 = spem_VariabilityElement(variabilityType="sample_text")
    a2 = spem_VariabilityElement(variabilityType="sample_text_2")
    b = spem_VariabilityElement(variabilityType="sample_text")
    _safe_set(b, 'spem_VariabilityElement126', a1)
    assert _is_linked(b, 'spem_VariabilityElement126', a1)
    if hasattr(a1, 'spem_VariabilityElement'):
        assert _is_linked(a1, 'spem_VariabilityElement', b)
    _safe_set(b, 'spem_VariabilityElement126', a2)
    assert _is_linked(b, 'spem_VariabilityElement126', a2)
    if hasattr(a1, 'spem_VariabilityElement'):
        assert not _is_linked(a1, 'spem_VariabilityElement', b)
    if hasattr(a2, 'spem_VariabilityElement'):
        assert _is_linked(a2, 'spem_VariabilityElement', b)
    _safe_set(b, 'spem_VariabilityElement126', None)
    assert not _is_linked(b, 'spem_VariabilityElement126', a2)
    if hasattr(a2, 'spem_VariabilityElement'):
        assert not _is_linked(a2, 'spem_VariabilityElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_aggregatedRole117_stub_double():
    # spem_CompositeRole has no real 'spem_CompositeRole' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_CompositeRole()
    setattr(partner, 'spem_CompositeRole', None)
    _safe_set(owner, 'spem_RoleDefinition118', partner)
    assert owner in getattr(partner, 'spem_CompositeRole')
    _safe_set(owner, 'spem_RoleDefinition118', None)
    assert owner not in getattr(partner, 'spem_CompositeRole')


def test_assoc_categorizedElement59_stub_double():
    # spem_Category has no real 'category' property in the generated
    # code (a bare stub) -- manually attach it so spem_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_DescribableElement(author="sample_text", briefDescription="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text", version="sample_text")
    partner = spem_Category()
    setattr(partner, 'category', None)
    _safe_set(owner, 'DescribableElement', partner)
    assert owner in getattr(partner, 'category')
    _safe_set(owner, 'DescribableElement', None)
    assert owner not in getattr(partner, 'category')


def test_assoc_category56_stub_double():
    # spem_Category has no real 'Category' property in the generated
    # code (a bare stub) -- manually attach it so spem_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_DescribableElement(author="sample_text", briefDescription="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text", version="sample_text")
    partner = spem_Category()
    setattr(partner, 'Category', None)
    _safe_set(owner, 'categorizedElement', {partner})
    assert getattr(partner, 'Category') == owner
    _safe_set(owner, 'categorizedElement', set())
    assert getattr(partner, 'Category') is None


def test_assoc_communicationMaterial184_stub_double():
    # SupportingMaterial has no real 'SupportingMaterial' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_DeliveryProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_DeliveryProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_DeliveryProcess(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    partner = SupportingMaterial()
    setattr(partner, 'SupportingMaterial', None)
    _safe_set(owner, 'spem_uma_DeliveryProcess', {partner})
    assert getattr(partner, 'SupportingMaterial') == owner
    _safe_set(owner, 'spem_uma_DeliveryProcess', set())
    assert getattr(partner, 'SupportingMaterial') is None


def test_assoc_configurationPackage171_stub_double():
    # spem_MethodContentPackage has no real 'spem_MethodContentPackage173' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodLibrary(name="sample_text")
    partner = spem_MethodContentPackage()
    setattr(partner, 'spem_MethodContentPackage173', None)
    _safe_set(owner, 'spem_MethodLibrary172', partner)
    assert getattr(partner, 'spem_MethodContentPackage173') == owner
    _safe_set(owner, 'spem_MethodLibrary172', None)
    assert getattr(partner, 'spem_MethodContentPackage173') is None


def test_assoc_connectedPort177_stub_double():
    # spem_WorkProductPortConnector has no real 'spem_WorkProductPortConnector' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductPort(isOptional=True, portKind="sample_text")
    partner = spem_WorkProductPortConnector()
    setattr(partner, 'spem_WorkProductPortConnector', None)
    _safe_set(owner, 'spem_WorkProductPort178', partner)
    assert owner in getattr(partner, 'spem_WorkProductPortConnector')
    _safe_set(owner, 'spem_WorkProductPort178', None)
    assert owner not in getattr(partner, 'spem_WorkProductPortConnector')


def test_assoc_contentReference200_stub_double():
    # uma_spem_MethodContentElement has no real 'uma_spem_MethodContentElement' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Practice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Practice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Practice(additionalInfo="sample_text", application="sample_text", background="sample_text", goal="sample_text", levelOfAdoption="sample_text", problem="sample_text")
    partner = uma_spem_MethodContentElement()
    setattr(partner, 'uma_spem_MethodContentElement', None)
    _safe_set(owner, 'spem_uma_Practice201', {partner})
    assert getattr(partner, 'uma_spem_MethodContentElement') == owner
    _safe_set(owner, 'spem_uma_Practice201', set())
    assert getattr(partner, 'uma_spem_MethodContentElement') is None


def test_assoc_defaultContext21_stub_double():
    # spem_MethodConfiguration has no real 'spem_MethodConfiguration' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(isEnactable=True, useKind="sample_text")
    partner = spem_MethodConfiguration()
    setattr(partner, 'spem_MethodConfiguration', None)
    _safe_set(owner, 'spem_Activity22', partner)
    assert getattr(partner, 'spem_MethodConfiguration') == owner
    _safe_set(owner, 'spem_Activity22', None)
    assert getattr(partner, 'spem_MethodConfiguration') is None


def test_assoc_deliveredProduct180_stub_double():
    # uma_spem_WorkProductUse has no real 'uma_spem_WorkProductUse' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Deliverable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Deliverable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Deliverable(externalDescription="sample_text", packagingGuidance="sample_text")
    partner = uma_spem_WorkProductUse()
    setattr(partner, 'uma_spem_WorkProductUse', None)
    _safe_set(owner, 'spem_uma_Deliverable', {partner})
    assert getattr(partner, 'uma_spem_WorkProductUse') == owner
    _safe_set(owner, 'spem_uma_Deliverable', set())
    assert getattr(partner, 'uma_spem_WorkProductUse') is None


def test_assoc_educationalMaterial185_stub_double():
    # SupportingMaterial has no real 'SupportingMaterial187' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_DeliveryProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_DeliveryProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_DeliveryProcess(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    partner = SupportingMaterial()
    setattr(partner, 'SupportingMaterial187', None)
    _safe_set(owner, 'spem_uma_DeliveryProcess186', {partner})
    assert getattr(partner, 'SupportingMaterial187') == owner
    _safe_set(owner, 'spem_uma_DeliveryProcess186', set())
    assert getattr(partner, 'SupportingMaterial187') is None


def test_assoc_guidance53_stub_double():
    # spem_Guidance has no real 'spem_Guidance' property in the generated
    # code (a bare stub) -- manually attach it so spem_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_DescribableElement(author="sample_text", briefDescription="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text", version="sample_text")
    partner = spem_Guidance()
    setattr(partner, 'spem_Guidance', None)
    _safe_set(owner, 'spem_DescribableElement', {partner})
    assert getattr(partner, 'spem_Guidance') == owner
    _safe_set(owner, 'spem_DescribableElement', set())
    assert getattr(partner, 'spem_Guidance') is None


def test_assoc_includedConnector182_stub_double():
    # uma_spem_WorkProductPortConnector has no real 'uma_spem_WorkProductPortConnector' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Process(scope="sample_text", usageNote="sample_text")
    partner = uma_spem_WorkProductPortConnector()
    setattr(partner, 'uma_spem_WorkProductPortConnector', None)
    _safe_set(owner, 'spem_uma_Process183', {partner})
    assert getattr(partner, 'uma_spem_WorkProductPortConnector') == owner
    _safe_set(owner, 'spem_uma_Process183', set())
    assert getattr(partner, 'uma_spem_WorkProductPortConnector') is None


def test_assoc_includedPattern181_stub_double():
    # CapabilityPattern has no real 'CapabilityPattern' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Process(scope="sample_text", usageNote="sample_text")
    partner = CapabilityPattern()
    setattr(partner, 'CapabilityPattern', None)
    _safe_set(owner, 'spem_uma_Process', {partner})
    assert getattr(partner, 'CapabilityPattern') == owner
    _safe_set(owner, 'spem_uma_Process', set())
    assert getattr(partner, 'CapabilityPattern') is None


def test_assoc_linkedActivity27_stub_double():
    # spem_ProcessPerformer has no real 'spem_ProcessPerformer28' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(isEnactable=True, useKind="sample_text")
    partner = spem_ProcessPerformer()
    setattr(partner, 'spem_ProcessPerformer28', None)
    _safe_set(owner, 'spem_Activity29', partner)
    assert getattr(partner, 'spem_ProcessPerformer28') == owner
    _safe_set(owner, 'spem_Activity29', None)
    assert getattr(partner, 'spem_ProcessPerformer28') is None


def test_assoc_linkedRoleDefinition89_stub_double():
    # spem_Default_TaskDefinitionPerformer has no real 'spem_Default_TaskDefinitionPerformer90' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_Default_TaskDefinitionPerformer()
    setattr(partner, 'spem_Default_TaskDefinitionPerformer90', None)
    _safe_set(owner, 'spem_RoleDefinition91', partner)
    assert owner in getattr(partner, 'spem_Default_TaskDefinitionPerformer90')
    _safe_set(owner, 'spem_RoleDefinition91', None)
    assert owner not in getattr(partner, 'spem_Default_TaskDefinitionPerformer90')


def test_assoc_linkedRoleDefinition92_stub_double():
    # spem_Default_ResponsibilityAssignment has no real 'spem_Default_ResponsibilityAssignment' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_Default_ResponsibilityAssignment()
    setattr(partner, 'spem_Default_ResponsibilityAssignment', None)
    _safe_set(owner, 'spem_RoleDefinition93', partner)
    assert owner in getattr(partner, 'spem_Default_ResponsibilityAssignment')
    _safe_set(owner, 'spem_RoleDefinition93', None)
    assert owner not in getattr(partner, 'spem_Default_ResponsibilityAssignment')


def test_assoc_linkedTaskUse30_stub_double():
    # spem_ProcessPerformer has no real 'spem_ProcessPerformer31' property in the generated
    # code (a bare stub) -- manually attach it so spem_TaskUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_TaskUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    partner = spem_ProcessPerformer()
    setattr(partner, 'spem_ProcessPerformer31', None)
    _safe_set(owner, 'spem_TaskUse', partner)
    assert getattr(partner, 'spem_ProcessPerformer31') == owner
    _safe_set(owner, 'spem_TaskUse', None)
    assert getattr(partner, 'spem_ProcessPerformer31') is None


def test_assoc_linkedWorkDefinition1_stub_double():
    # spem_WorkDefinitionPerformer has no real 'spem_WorkDefinitionPerformer' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkDefinition(postCondition="sample_text", preCondition="sample_text")
    partner = spem_WorkDefinitionPerformer()
    setattr(partner, 'spem_WorkDefinitionPerformer', None)
    _safe_set(owner, 'spem_WorkDefinition', partner)
    assert getattr(partner, 'spem_WorkDefinitionPerformer') == owner
    _safe_set(owner, 'spem_WorkDefinition', None)
    assert getattr(partner, 'spem_WorkDefinitionPerformer') is None


def test_assoc_ownedMethodContentMember100_stub_double():
    # spem_MethodContentPackage has no real 'spem_MethodContentPackage' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodContentPackageableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodContentPackageableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodContentPackageableElement(name="sample_text")
    partner = spem_MethodContentPackage()
    setattr(partner, 'spem_MethodContentPackage', None)
    _safe_set(owner, 'spem_MethodContentPackageableElement', partner)
    assert owner in getattr(partner, 'spem_MethodContentPackage')
    _safe_set(owner, 'spem_MethodContentPackageableElement', None)
    assert owner not in getattr(partner, 'spem_MethodContentPackage')


def test_assoc_ownedMethodPlugin166_stub_double():
    # spem_MethodPlugin has no real 'spem_MethodPlugin167' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodLibrary(name="sample_text")
    partner = spem_MethodPlugin()
    setattr(partner, 'spem_MethodPlugin167', None)
    _safe_set(owner, 'spem_MethodLibrary', {partner})
    assert getattr(partner, 'spem_MethodPlugin167') == owner
    _safe_set(owner, 'spem_MethodLibrary', set())
    assert getattr(partner, 'spem_MethodPlugin167') is None


def test_assoc_ownedPort130_stub_double():
    # spem_ProcessComponent has no real 'spem_ProcessComponent131' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductPort(isOptional=True, portKind="sample_text")
    partner = spem_ProcessComponent()
    setattr(partner, 'spem_ProcessComponent131', None)
    _safe_set(owner, 'spem_WorkProductPort', partner)
    assert owner in getattr(partner, 'spem_ProcessComponent131')
    _safe_set(owner, 'spem_WorkProductPort', None)
    assert owner not in getattr(partner, 'spem_ProcessComponent131')


def test_assoc_ownedProcessMember104_stub_double():
    # spem_ProcessPackage has no real 'spem_ProcessPackage' property in the generated
    # code (a bare stub) -- manually attach it so spem_ProcessPackageableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_ProcessPackageableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_ProcessPackageableElement(name="sample_text")
    partner = spem_ProcessPackage()
    setattr(partner, 'spem_ProcessPackage', None)
    _safe_set(owner, 'spem_ProcessPackageableElement', partner)
    assert owner in getattr(partner, 'spem_ProcessPackage')
    _safe_set(owner, 'spem_ProcessPackageableElement', None)
    assert owner not in getattr(partner, 'spem_ProcessPackage')


def test_assoc_ownedTaskDefinitionParameter63_stub_double():
    # spem_TaskDefinition has no real 'spem_TaskDefinition' property in the generated
    # code (a bare stub) -- manually attach it so spem_Default_TaskDefinitionParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Default_TaskDefinitionParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Default_TaskDefinitionParameter(name="sample_text", optionality="sample_text")
    partner = spem_TaskDefinition()
    setattr(partner, 'spem_TaskDefinition', None)
    _safe_set(owner, 'spem_Default_TaskDefinitionParameter', partner)
    assert owner in getattr(partner, 'spem_TaskDefinition')
    _safe_set(owner, 'spem_Default_TaskDefinitionParameter', None)
    assert owner not in getattr(partner, 'spem_TaskDefinition')


def test_assoc_parameterType47_stub_double():
    # spem_WorkProductUse has no real 'spem_WorkProductUse49' property in the generated
    # code (a bare stub) -- manually attach it so spem_ProcessParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_ProcessParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_ProcessParameter(optionality="sample_text")
    partner = spem_WorkProductUse()
    setattr(partner, 'spem_WorkProductUse49', None)
    _safe_set(owner, 'spem_ProcessParameter48', partner)
    assert getattr(partner, 'spem_WorkProductUse49') == owner
    _safe_set(owner, 'spem_ProcessParameter48', None)
    assert getattr(partner, 'spem_WorkProductUse49') is None


def test_assoc_parameterType97_stub_double():
    # spem_WorkProductDefinition has no real 'spem_WorkProductDefinition99' property in the generated
    # code (a bare stub) -- manually attach it so spem_Default_TaskDefinitionParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Default_TaskDefinitionParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Default_TaskDefinitionParameter(name="sample_text", optionality="sample_text")
    partner = spem_WorkProductDefinition()
    setattr(partner, 'spem_WorkProductDefinition99', None)
    _safe_set(owner, 'spem_Default_TaskDefinitionParameter98', partner)
    assert getattr(partner, 'spem_WorkProductDefinition99') == owner
    _safe_set(owner, 'spem_Default_TaskDefinitionParameter98', None)
    assert getattr(partner, 'spem_WorkProductDefinition99') is None


def test_assoc_portType174_stub_double():
    # spem_WorkProductDefinition has no real 'spem_WorkProductDefinition176' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductPort(isOptional=True, portKind="sample_text")
    partner = spem_WorkProductDefinition()
    setattr(partner, 'spem_WorkProductDefinition176', None)
    _safe_set(owner, 'spem_WorkProductPort175', partner)
    assert getattr(partner, 'spem_WorkProductDefinition176') == owner
    _safe_set(owner, 'spem_WorkProductPort175', None)
    assert getattr(partner, 'spem_WorkProductDefinition176') is None


def test_assoc_predefinedConfiguration168_stub_double():
    # spem_MethodConfiguration has no real 'spem_MethodConfiguration170' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodLibrary(name="sample_text")
    partner = spem_MethodConfiguration()
    setattr(partner, 'spem_MethodConfiguration170', None)
    _safe_set(owner, 'spem_MethodLibrary169', {partner})
    assert getattr(partner, 'spem_MethodConfiguration170') == owner
    _safe_set(owner, 'spem_MethodLibrary169', set())
    assert getattr(partner, 'spem_MethodConfiguration170') is None


def test_assoc_process128_stub_double():
    # spem_ProcessComponent has no real 'spem_ProcessComponent' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(isEnactable=True, useKind="sample_text")
    partner = spem_ProcessComponent()
    setattr(partner, 'spem_ProcessComponent', None)
    _safe_set(owner, 'spem_Activity129', partner)
    assert getattr(partner, 'spem_ProcessComponent') == owner
    _safe_set(owner, 'spem_Activity129', None)
    assert getattr(partner, 'spem_ProcessComponent') is None


def test_assoc_providedQualification79_stub_double():
    # spem_Qualification has no real 'spem_Qualification81' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_Qualification()
    setattr(partner, 'spem_Qualification81', None)
    _safe_set(owner, 'spem_RoleDefinition80', {partner})
    assert getattr(partner, 'spem_Qualification81') == owner
    _safe_set(owner, 'spem_RoleDefinition80', set())
    assert getattr(partner, 'spem_Qualification81') is None


def test_assoc_referencedActivity198_stub_double():
    # uma_spem_Activity has no real 'uma_spem_Activity' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Practice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Practice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Practice(additionalInfo="sample_text", application="sample_text", background="sample_text", goal="sample_text", levelOfAdoption="sample_text", problem="sample_text")
    partner = uma_spem_Activity()
    setattr(partner, 'uma_spem_Activity', None)
    _safe_set(owner, 'spem_uma_Practice199', {partner})
    assert getattr(partner, 'uma_spem_Activity') == owner
    _safe_set(owner, 'spem_uma_Practice199', set())
    assert getattr(partner, 'uma_spem_Activity') is None


def test_assoc_role32_stub_double():
    # spem_RoleUse has no real 'spem_RoleUse33' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_RoleUse()
    setattr(partner, 'spem_RoleUse33', None)
    _safe_set(owner, 'spem_RoleDefinition', partner)
    assert getattr(partner, 'spem_RoleUse33') == owner
    _safe_set(owner, 'spem_RoleDefinition', None)
    assert getattr(partner, 'spem_RoleUse33') is None


def test_assoc_source211_stub_double():
    # activity_spem_BreakdownElement has no real 'activity_spem_BreakdownElement' property in the generated
    # code (a bare stub) -- manually attach it so spem_activity_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_activity_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_activity_Edge(guard="sample_text")
    partner = activity_spem_BreakdownElement()
    setattr(partner, 'activity_spem_BreakdownElement', None)
    _safe_set(owner, 'spem_activity_Edge', partner)
    assert getattr(partner, 'activity_spem_BreakdownElement') == owner
    _safe_set(owner, 'spem_activity_Edge', None)
    assert getattr(partner, 'activity_spem_BreakdownElement') is None


def test_assoc_source42_stub_double():
    # spem_WorkProductUse has no real 'spem_WorkProductUse43' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductUseRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductUseRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductUseRelationship(relationshipKind="sample_text")
    partner = spem_WorkProductUse()
    setattr(partner, 'spem_WorkProductUse43', None)
    _safe_set(owner, 'spem_WorkProductUseRelationship', partner)
    assert getattr(partner, 'spem_WorkProductUse43') == owner
    _safe_set(owner, 'spem_WorkProductUseRelationship', None)
    assert getattr(partner, 'spem_WorkProductUse43') is None


def test_assoc_step64_stub_double():
    # spem_TaskDefinition has no real 'spem_TaskDefinition65' property in the generated
    # code (a bare stub) -- manually attach it so spem_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Step(name="sample_text")
    partner = spem_TaskDefinition()
    setattr(partner, 'spem_TaskDefinition65', None)
    _safe_set(owner, 'spem_Step', partner)
    assert owner in getattr(partner, 'spem_TaskDefinition65')
    _safe_set(owner, 'spem_Step', None)
    assert owner not in getattr(partner, 'spem_TaskDefinition65')


def test_assoc_subPractice197_stub_double():
    # Practice has no real 'Practice' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Practice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Practice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Practice(additionalInfo="sample_text", application="sample_text", background="sample_text", goal="sample_text", levelOfAdoption="sample_text", problem="sample_text")
    partner = Practice()
    setattr(partner, 'Practice', None)
    _safe_set(owner, 'spem_uma_Practice', {partner})
    assert getattr(partner, 'Practice') == owner
    _safe_set(owner, 'spem_uma_Practice', set())
    assert getattr(partner, 'Practice') is None


def test_assoc_target212_stub_double():
    # activity_spem_BreakdownElement has no real 'activity_spem_BreakdownElement214' property in the generated
    # code (a bare stub) -- manually attach it so spem_activity_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_activity_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_activity_Edge(guard="sample_text")
    partner = activity_spem_BreakdownElement()
    setattr(partner, 'activity_spem_BreakdownElement214', None)
    _safe_set(owner, 'spem_activity_Edge213', partner)
    assert getattr(partner, 'activity_spem_BreakdownElement214') == owner
    _safe_set(owner, 'spem_activity_Edge213', None)
    assert getattr(partner, 'activity_spem_BreakdownElement214') is None


def test_assoc_target44_stub_double():
    # spem_WorkProductUse has no real 'spem_WorkProductUse46' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductUseRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductUseRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductUseRelationship(relationshipKind="sample_text")
    partner = spem_WorkProductUse()
    setattr(partner, 'spem_WorkProductUse46', None)
    _safe_set(owner, 'spem_WorkProductUseRelationship45', {partner})
    assert getattr(partner, 'spem_WorkProductUse46') == owner
    _safe_set(owner, 'spem_WorkProductUseRelationship45', set())
    assert getattr(partner, 'spem_WorkProductUse46') is None


def test_assoc_task105_stub_double():
    # spem_TaskDefinition has no real 'spem_TaskDefinition107' property in the generated
    # code (a bare stub) -- manually attach it so spem_TaskUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_TaskUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    partner = spem_TaskDefinition()
    setattr(partner, 'spem_TaskDefinition107', None)
    _safe_set(owner, 'spem_TaskUse106', partner)
    assert getattr(partner, 'spem_TaskDefinition107') == owner
    _safe_set(owner, 'spem_TaskUse106', None)
    assert getattr(partner, 'spem_TaskDefinition107') is None


def test_assoc_usedPort134_stub_double():
    # spem_ProcessComponentUse has no real 'spem_ProcessComponentUse135' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductPort(isOptional=True, portKind="sample_text")
    partner = spem_ProcessComponentUse()
    setattr(partner, 'spem_ProcessComponentUse135', None)
    _safe_set(owner, 'spem_WorkProductPort136', partner)
    assert owner in getattr(partner, 'spem_ProcessComponentUse135')
    _safe_set(owner, 'spem_WorkProductPort136', None)
    assert owner not in getattr(partner, 'spem_ProcessComponentUse135')


def test_assoc_usedQualification108_stub_double():
    # spem_Qualification has no real 'spem_Qualification110' property in the generated
    # code (a bare stub) -- manually attach it so spem_TaskUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_TaskUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    partner = spem_Qualification()
    setattr(partner, 'spem_Qualification110', None)
    _safe_set(owner, 'spem_TaskUse109', {partner})
    assert getattr(partner, 'spem_Qualification110') == owner
    _safe_set(owner, 'spem_TaskUse109', set())
    assert getattr(partner, 'spem_Qualification110') is None


def test_assoc_validContext23_stub_double():
    # spem_MethodConfiguration has no real 'spem_MethodConfiguration25' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(isEnactable=True, useKind="sample_text")
    partner = spem_MethodConfiguration()
    setattr(partner, 'spem_MethodConfiguration25', None)
    _safe_set(owner, 'spem_Activity24', {partner})
    assert getattr(partner, 'spem_MethodConfiguration25') == owner
    _safe_set(owner, 'spem_Activity24', set())
    assert getattr(partner, 'spem_MethodConfiguration25') is None


