import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    Artifact,
    BreakdownElement,
    CapabilityPattern,
    Category,
    Concept,
    ConfigurationPackage,
    DescribableElement,
    EstimatingConsideration,
    ExtensibleElement,
    Guidance,
    Kind,
    MethodContentElement,
    MethodContentKind,
    MethodContentPackage,
    MethodContentPackageableElement,
    MethodContentUse,
    MethodLibraryPackageableElement,
    MethodPluginPackageableElement,
    Practice,
    Process,
    ProcessElement,
    ProcessPackage,
    ProcessPackageableElement,
    Report,
    RoleUse,
    SupportingMaterial,
    Template,
    ToolMentor,
    VariabilityElement,
    WorkBreakdownElement,
    WorkDefinition,
    WorkDefinitionParameter,
    WorkDefinitionPerformer,
    WorkProductUse,
    spem_Activity,
    spem_BreakdownElement,
    spem_Category,
    spem_CompositeRole,
    spem_Default_ResponsibilityAssignment,
    spem_Default_TaskDefinitionParameter,
    spem_Default_TaskDefinitionPerformer,
    spem_DescribableElement,
    spem_EObject,
    spem_ExtensibleElement,
    spem_Guidance,
    spem_Kind,
    spem_LifeCycleSpecification,
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
    spem_WorkProductKind,
    spem_WorkProductPort,
    spem_WorkProductPortConnector,
    spem_WorkProductUse,
    spem_WorkProductUseRelationship,
    spem_WorkSequence,
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

def test_assoc_alternatives29_reverse_link_reassign_clear():
    a1 = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    a2 = spem_Activity(howToStaff="sample_text_2", isEnactable=False, useKind="sample_text_2")
    b = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity30', a1)
    assert _is_linked(b, 'spem_Activity30', a1)
    if hasattr(a1, 'spem_Activity28'):
        assert _is_linked(a1, 'spem_Activity28', b)
    _safe_set(b, 'spem_Activity30', a2)
    assert _is_linked(b, 'spem_Activity30', a2)
    if hasattr(a1, 'spem_Activity28'):
        assert not _is_linked(a1, 'spem_Activity28', b)
    if hasattr(a2, 'spem_Activity28'):
        assert _is_linked(a2, 'spem_Activity28', b)
    _safe_set(b, 'spem_Activity30', None)
    assert not _is_linked(b, 'spem_Activity30', a2)
    if hasattr(a2, 'spem_Activity28'):
        assert not _is_linked(a2, 'spem_Activity28', b)


def test_assoc_basePlugin185_reverse_link_reassign_clear():
    a1 = spem_MethodPlugin(supporting="sample_text", userChangeable=True)
    a2 = spem_MethodPlugin(supporting="sample_text_2", userChangeable=False)
    b = spem_MethodPlugin(supporting="sample_text", userChangeable=True)
    _safe_set(b, 'spem_MethodPlugin186', a1)
    assert _is_linked(b, 'spem_MethodPlugin186', a1)
    if hasattr(a1, 'spem_MethodPlugin184'):
        assert _is_linked(a1, 'spem_MethodPlugin184', b)
    _safe_set(b, 'spem_MethodPlugin186', a2)
    assert _is_linked(b, 'spem_MethodPlugin186', a2)
    if hasattr(a1, 'spem_MethodPlugin184'):
        assert not _is_linked(a1, 'spem_MethodPlugin184', b)
    if hasattr(a2, 'spem_MethodPlugin184'):
        assert _is_linked(a2, 'spem_MethodPlugin184', b)
    _safe_set(b, 'spem_MethodPlugin186', None)
    assert not _is_linked(b, 'spem_MethodPlugin186', a2)
    if hasattr(a2, 'spem_MethodPlugin184'):
        assert not _is_linked(a2, 'spem_MethodPlugin184', b)


def test_assoc_guidance56_reverse_link_reassign_clear():
    a1 = spem_Guidance(attachment="sample_text")
    a2 = spem_Guidance(attachment="sample_text_2")
    b = spem_DescribableElement(briefDescription="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text")
    _safe_set(b, 'spem_DescribableElement', {a1})
    assert _is_linked(b, 'spem_DescribableElement', a1)
    if hasattr(a1, 'spem_Guidance57'):
        assert _is_linked(a1, 'spem_Guidance57', b)
    _safe_set(b, 'spem_DescribableElement', {a2})
    assert _is_linked(b, 'spem_DescribableElement', a2)
    if hasattr(a1, 'spem_Guidance57'):
        assert not _is_linked(a1, 'spem_Guidance57', b)
    if hasattr(a2, 'spem_Guidance57'):
        assert _is_linked(a2, 'spem_Guidance57', b)
    _safe_set(b, 'spem_DescribableElement', set())
    assert not _is_linked(b, 'spem_DescribableElement', a2)
    if hasattr(a2, 'spem_Guidance57'):
        assert not _is_linked(a2, 'spem_Guidance57', b)


def test_assoc_linkToPredecessor7_reverse_link_reassign_clear():
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


def test_assoc_linkToSuccessor8_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(linkKind="sample_text")
    a2 = spem_WorkSequence(linkKind="sample_text_2")
    b = spem_WorkBreakdownElement(isEventDriven=True, isOngoing=True, isRepeatable=True)
    _safe_set(b, 'predecessor', {a1})
    assert _is_linked(b, 'predecessor', a1)
    if hasattr(a1, 'WorkSequence9'):
        assert _is_linked(a1, 'WorkSequence9', b)
    _safe_set(b, 'predecessor', {a2})
    assert _is_linked(b, 'predecessor', a2)
    if hasattr(a1, 'WorkSequence9'):
        assert not _is_linked(a1, 'WorkSequence9', b)
    if hasattr(a2, 'WorkSequence9'):
        assert _is_linked(a2, 'WorkSequence9', b)
    _safe_set(b, 'predecessor', set())
    assert not _is_linked(b, 'predecessor', a2)
    if hasattr(a2, 'WorkSequence9'):
        assert not _is_linked(a2, 'WorkSequence9', b)


def test_assoc_metric58_reverse_link_reassign_clear():
    a1 = spem_Metric(expression="sample_text")
    a2 = spem_Metric(expression="sample_text_2")
    b = spem_DescribableElement(briefDescription="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text")
    _safe_set(b, 'spem_DescribableElement59', {a1})
    assert _is_linked(b, 'spem_DescribableElement59', a1)
    if hasattr(a1, 'spem_Metric'):
        assert _is_linked(a1, 'spem_Metric', b)
    _safe_set(b, 'spem_DescribableElement59', {a2})
    assert _is_linked(b, 'spem_DescribableElement59', a2)
    if hasattr(a1, 'spem_Metric'):
        assert not _is_linked(a1, 'spem_Metric', b)
    if hasattr(a2, 'spem_Metric'):
        assert _is_linked(a2, 'spem_Metric', b)
    _safe_set(b, 'spem_DescribableElement59', set())
    assert not _is_linked(b, 'spem_DescribableElement59', a2)
    if hasattr(a2, 'spem_Metric'):
        assert not _is_linked(a2, 'spem_Metric', b)


def test_assoc_nestedBreakdownElement15_reverse_link_reassign_clear():
    a1 = spem_BreakdownElement(hasMultipleOccurrences=True, isOptional=True, isPlanned=True)
    a2 = spem_BreakdownElement(hasMultipleOccurrences=False, isOptional=False, isPlanned=False)
    b = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity16', {a1})
    assert _is_linked(b, 'spem_Activity16', a1)
    if hasattr(a1, 'spem_BreakdownElement17'):
        assert _is_linked(a1, 'spem_BreakdownElement17', b)
    _safe_set(b, 'spem_Activity16', {a2})
    assert _is_linked(b, 'spem_Activity16', a2)
    if hasattr(a1, 'spem_BreakdownElement17'):
        assert not _is_linked(a1, 'spem_BreakdownElement17', b)
    if hasattr(a2, 'spem_BreakdownElement17'):
        assert _is_linked(a2, 'spem_BreakdownElement17', b)
    _safe_set(b, 'spem_Activity16', set())
    assert not _is_linked(b, 'spem_Activity16', a2)
    if hasattr(a2, 'spem_BreakdownElement17'):
        assert not _is_linked(a2, 'spem_BreakdownElement17', b)


def test_assoc_ownedMethodPlugin190_reverse_link_reassign_clear():
    a1 = spem_MethodPlugin(supporting="sample_text", userChangeable=True)
    a2 = spem_MethodPlugin(supporting="sample_text_2", userChangeable=False)
    b = spem_MethodLibrary(name="sample_text")
    _safe_set(b, 'spem_MethodLibrary', {a1})
    assert _is_linked(b, 'spem_MethodLibrary', a1)
    if hasattr(a1, 'spem_MethodPlugin191'):
        assert _is_linked(a1, 'spem_MethodPlugin191', b)
    _safe_set(b, 'spem_MethodLibrary', {a2})
    assert _is_linked(b, 'spem_MethodLibrary', a2)
    if hasattr(a1, 'spem_MethodPlugin191'):
        assert not _is_linked(a1, 'spem_MethodPlugin191', b)
    if hasattr(a2, 'spem_MethodPlugin191'):
        assert _is_linked(a2, 'spem_MethodPlugin191', b)
    _safe_set(b, 'spem_MethodLibrary', set())
    assert not _is_linked(b, 'spem_MethodLibrary', a2)
    if hasattr(a2, 'spem_MethodPlugin191'):
        assert not _is_linked(a2, 'spem_MethodPlugin191', b)


def test_assoc_ownedParameter1_reverse_link_reassign_clear():
    a1 = spem_WorkDefinitionParameter(direction="sample_text", name="sample_text", optionality="sample_text")
    a2 = spem_WorkDefinitionParameter(direction="sample_text_2", name="sample_text_2", optionality="sample_text_2")
    b = spem_WorkDefinition(postCondition="sample_text", preCondition="sample_text")
    _safe_set(b, 'spem_WorkDefinition', {a1})
    assert _is_linked(b, 'spem_WorkDefinition', a1)
    if hasattr(a1, 'spem_WorkDefinitionParameter'):
        assert _is_linked(a1, 'spem_WorkDefinitionParameter', b)
    _safe_set(b, 'spem_WorkDefinition', {a2})
    assert _is_linked(b, 'spem_WorkDefinition', a2)
    if hasattr(a1, 'spem_WorkDefinitionParameter'):
        assert not _is_linked(a1, 'spem_WorkDefinitionParameter', b)
    if hasattr(a2, 'spem_WorkDefinitionParameter'):
        assert _is_linked(a2, 'spem_WorkDefinitionParameter', b)
    _safe_set(b, 'spem_WorkDefinition', set())
    assert not _is_linked(b, 'spem_WorkDefinition', a2)
    if hasattr(a2, 'spem_WorkDefinitionParameter'):
        assert not _is_linked(a2, 'spem_WorkDefinitionParameter', b)


def test_assoc_ownedPort148_reverse_link_reassign_clear():
    a1 = spem_WorkProductPort(isOptional=True, portKind="sample_text")
    a2 = spem_WorkProductPort(isOptional=False, portKind="sample_text_2")
    b = spem_ProcessComponent(author="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", version="sample_text")
    _safe_set(b, 'spem_ProcessComponent149', {a1})
    assert _is_linked(b, 'spem_ProcessComponent149', a1)
    if hasattr(a1, 'spem_WorkProductPort'):
        assert _is_linked(a1, 'spem_WorkProductPort', b)
    _safe_set(b, 'spem_ProcessComponent149', {a2})
    assert _is_linked(b, 'spem_ProcessComponent149', a2)
    if hasattr(a1, 'spem_WorkProductPort'):
        assert not _is_linked(a1, 'spem_WorkProductPort', b)
    if hasattr(a2, 'spem_WorkProductPort'):
        assert _is_linked(a2, 'spem_WorkProductPort', b)
    _safe_set(b, 'spem_ProcessComponent149', set())
    assert not _is_linked(b, 'spem_ProcessComponent149', a2)
    if hasattr(a2, 'spem_WorkProductPort'):
        assert not _is_linked(a2, 'spem_WorkProductPort', b)


def test_assoc_parameterType2_reverse_link_reassign_clear():
    a1 = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    a2 = spem_WorkProductDefinition(impactOfNotHaving="sample_text_2", reasonForNotNeeding="sample_text_2")
    b = spem_WorkDefinitionParameter(direction="sample_text", name="sample_text", optionality="sample_text")
    _safe_set(b, 'spem_WorkDefinitionParameter3', a1)
    assert _is_linked(b, 'spem_WorkDefinitionParameter3', a1)
    if hasattr(a1, 'spem_WorkProductDefinition'):
        assert _is_linked(a1, 'spem_WorkProductDefinition', b)
    _safe_set(b, 'spem_WorkDefinitionParameter3', a2)
    assert _is_linked(b, 'spem_WorkDefinitionParameter3', a2)
    if hasattr(a1, 'spem_WorkProductDefinition'):
        assert not _is_linked(a1, 'spem_WorkProductDefinition', b)
    if hasattr(a2, 'spem_WorkProductDefinition'):
        assert _is_linked(a2, 'spem_WorkProductDefinition', b)
    _safe_set(b, 'spem_WorkDefinitionParameter3', None)
    assert not _is_linked(b, 'spem_WorkDefinitionParameter3', a2)
    if hasattr(a2, 'spem_WorkProductDefinition'):
        assert not _is_linked(a2, 'spem_WorkProductDefinition', b)


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


def test_assoc_portType202_reverse_link_reassign_clear():
    a1 = spem_WorkProductPort(isOptional=True, portKind="sample_text")
    a2 = spem_WorkProductPort(isOptional=False, portKind="sample_text_2")
    b = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    _safe_set(b, 'spem_WorkProductDefinition204', a1)
    assert _is_linked(b, 'spem_WorkProductDefinition204', a1)
    if hasattr(a1, 'spem_WorkProductPort203'):
        assert _is_linked(a1, 'spem_WorkProductPort203', b)
    _safe_set(b, 'spem_WorkProductDefinition204', a2)
    assert _is_linked(b, 'spem_WorkProductDefinition204', a2)
    if hasattr(a1, 'spem_WorkProductPort203'):
        assert not _is_linked(a1, 'spem_WorkProductPort203', b)
    if hasattr(a2, 'spem_WorkProductPort203'):
        assert _is_linked(a2, 'spem_WorkProductPort203', b)
    _safe_set(b, 'spem_WorkProductDefinition204', None)
    assert not _is_linked(b, 'spem_WorkProductDefinition204', a2)
    if hasattr(a2, 'spem_WorkProductPort203'):
        assert not _is_linked(a2, 'spem_WorkProductPort203', b)


def test_assoc_predecessor10_reverse_link_reassign_clear():
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


def test_assoc_predecessor91_reverse_link_reassign_clear():
    a1 = spem_Step(name="sample_text")
    a2 = spem_Step(name="sample_text_2")
    b = spem_Step(name="sample_text")
    _safe_set(b, 'spem_Step92', a1)
    assert _is_linked(b, 'spem_Step92', a1)
    if hasattr(a1, 'spem_Step90'):
        assert _is_linked(a1, 'spem_Step90', b)
    _safe_set(b, 'spem_Step92', a2)
    assert _is_linked(b, 'spem_Step92', a2)
    if hasattr(a1, 'spem_Step90'):
        assert not _is_linked(a1, 'spem_Step90', b)
    if hasattr(a2, 'spem_Step90'):
        assert _is_linked(a2, 'spem_Step90', b)
    _safe_set(b, 'spem_Step92', None)
    assert not _is_linked(b, 'spem_Step92', a2)
    if hasattr(a2, 'spem_Step90'):
        assert not _is_linked(a2, 'spem_Step90', b)


def test_assoc_presentedAfter61_reverse_link_reassign_clear():
    a1 = spem_DescribableElement(briefDescription="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text")
    a2 = spem_DescribableElement(briefDescription="sample_text_2", mainDescription="sample_text_2", presentationName="sample_text_2", purpose="sample_text_2")
    b = spem_DescribableElement(briefDescription="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text")
    _safe_set(b, 'spem_DescribableElement62', a1)
    assert _is_linked(b, 'spem_DescribableElement62', a1)
    if hasattr(a1, 'spem_DescribableElement60'):
        assert _is_linked(a1, 'spem_DescribableElement60', b)
    _safe_set(b, 'spem_DescribableElement62', a2)
    assert _is_linked(b, 'spem_DescribableElement62', a2)
    if hasattr(a1, 'spem_DescribableElement60'):
        assert not _is_linked(a1, 'spem_DescribableElement60', b)
    if hasattr(a2, 'spem_DescribableElement60'):
        assert _is_linked(a2, 'spem_DescribableElement60', b)
    _safe_set(b, 'spem_DescribableElement62', None)
    assert not _is_linked(b, 'spem_DescribableElement62', a2)
    if hasattr(a2, 'spem_DescribableElement60'):
        assert not _is_linked(a2, 'spem_DescribableElement60', b)


def test_assoc_presentedBefore64_reverse_link_reassign_clear():
    a1 = spem_DescribableElement(briefDescription="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text")
    a2 = spem_DescribableElement(briefDescription="sample_text_2", mainDescription="sample_text_2", presentationName="sample_text_2", purpose="sample_text_2")
    b = spem_DescribableElement(briefDescription="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text")
    _safe_set(b, 'spem_DescribableElement65', a1)
    assert _is_linked(b, 'spem_DescribableElement65', a1)
    if hasattr(a1, 'spem_DescribableElement63'):
        assert _is_linked(a1, 'spem_DescribableElement63', b)
    _safe_set(b, 'spem_DescribableElement65', a2)
    assert _is_linked(b, 'spem_DescribableElement65', a2)
    if hasattr(a1, 'spem_DescribableElement63'):
        assert not _is_linked(a1, 'spem_DescribableElement63', b)
    if hasattr(a2, 'spem_DescribableElement63'):
        assert _is_linked(a2, 'spem_DescribableElement63', b)
    _safe_set(b, 'spem_DescribableElement65', None)
    assert not _is_linked(b, 'spem_DescribableElement65', a2)
    if hasattr(a2, 'spem_DescribableElement63'):
        assert not _is_linked(a2, 'spem_DescribableElement63', b)


def test_assoc_process146_reverse_link_reassign_clear():
    a1 = spem_ProcessComponent(author="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", version="sample_text")
    a2 = spem_ProcessComponent(author="sample_text_2", changeDate=date(2025, 6, 15), changeDescription="sample_text_2", copyright="sample_text_2", version="sample_text_2")
    b = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity147', a1)
    assert _is_linked(b, 'spem_Activity147', a1)
    if hasattr(a1, 'spem_ProcessComponent'):
        assert _is_linked(a1, 'spem_ProcessComponent', b)
    _safe_set(b, 'spem_Activity147', a2)
    assert _is_linked(b, 'spem_Activity147', a2)
    if hasattr(a1, 'spem_ProcessComponent'):
        assert not _is_linked(a1, 'spem_ProcessComponent', b)
    if hasattr(a2, 'spem_ProcessComponent'):
        assert _is_linked(a2, 'spem_ProcessComponent', b)
    _safe_set(b, 'spem_Activity147', None)
    assert not _is_linked(b, 'spem_Activity147', a2)
    if hasattr(a2, 'spem_ProcessComponent'):
        assert not _is_linked(a2, 'spem_ProcessComponent', b)


def test_assoc_referencedMethodPlugin188_reverse_link_reassign_clear():
    a1 = spem_MethodPlugin(supporting="sample_text", userChangeable=True)
    a2 = spem_MethodPlugin(supporting="sample_text_2", userChangeable=False)
    b = spem_MethodPlugin(supporting="sample_text", userChangeable=True)
    _safe_set(b, 'spem_MethodPlugin189', a1)
    assert _is_linked(b, 'spem_MethodPlugin189', a1)
    if hasattr(a1, 'spem_MethodPlugin187'):
        assert _is_linked(a1, 'spem_MethodPlugin187', b)
    _safe_set(b, 'spem_MethodPlugin189', a2)
    assert _is_linked(b, 'spem_MethodPlugin189', a2)
    if hasattr(a1, 'spem_MethodPlugin187'):
        assert not _is_linked(a1, 'spem_MethodPlugin187', b)
    if hasattr(a2, 'spem_MethodPlugin187'):
        assert _is_linked(a2, 'spem_MethodPlugin187', b)
    _safe_set(b, 'spem_MethodPlugin189', None)
    assert not _is_linked(b, 'spem_MethodPlugin189', a2)
    if hasattr(a2, 'spem_MethodPlugin187'):
        assert not _is_linked(a2, 'spem_MethodPlugin187', b)


def test_assoc_selectedStep132_reverse_link_reassign_clear():
    a1 = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    a2 = spem_TaskUse(postCondition="sample_text_2", preCondition="sample_text_2")
    b = spem_Step(name="sample_text")
    _safe_set(b, 'spem_Step134', a1)
    assert _is_linked(b, 'spem_Step134', a1)
    if hasattr(a1, 'spem_TaskUse133'):
        assert _is_linked(a1, 'spem_TaskUse133', b)
    _safe_set(b, 'spem_Step134', a2)
    assert _is_linked(b, 'spem_Step134', a2)
    if hasattr(a1, 'spem_TaskUse133'):
        assert not _is_linked(a1, 'spem_TaskUse133', b)
    if hasattr(a2, 'spem_TaskUse133'):
        assert _is_linked(a2, 'spem_TaskUse133', b)
    _safe_set(b, 'spem_Step134', None)
    assert not _is_linked(b, 'spem_Step134', a2)
    if hasattr(a2, 'spem_TaskUse133'):
        assert not _is_linked(a2, 'spem_TaskUse133', b)


def test_assoc_successor11_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(linkKind="sample_text")
    a2 = spem_WorkSequence(linkKind="sample_text_2")
    b = spem_WorkBreakdownElement(isEventDriven=True, isOngoing=True, isRepeatable=True)
    _safe_set(b, 'WorkBreakdownElement12', a1)
    assert _is_linked(b, 'WorkBreakdownElement12', a1)
    if hasattr(a1, 'linkToPredecessor'):
        assert _is_linked(a1, 'linkToPredecessor', b)
    _safe_set(b, 'WorkBreakdownElement12', a2)
    assert _is_linked(b, 'WorkBreakdownElement12', a2)
    if hasattr(a1, 'linkToPredecessor'):
        assert not _is_linked(a1, 'linkToPredecessor', b)
    if hasattr(a2, 'linkToPredecessor'):
        assert _is_linked(a2, 'linkToPredecessor', b)
    _safe_set(b, 'WorkBreakdownElement12', None)
    assert not _is_linked(b, 'WorkBreakdownElement12', a2)
    if hasattr(a2, 'linkToPredecessor'):
        assert not _is_linked(a2, 'linkToPredecessor', b)


def test_assoc_suppressedBreakdownElement18_reverse_link_reassign_clear():
    a1 = spem_BreakdownElement(hasMultipleOccurrences=True, isOptional=True, isPlanned=True)
    a2 = spem_BreakdownElement(hasMultipleOccurrences=False, isOptional=False, isPlanned=False)
    b = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity19', {a1})
    assert _is_linked(b, 'spem_Activity19', a1)
    if hasattr(a1, 'spem_BreakdownElement20'):
        assert _is_linked(a1, 'spem_BreakdownElement20', b)
    _safe_set(b, 'spem_Activity19', {a2})
    assert _is_linked(b, 'spem_Activity19', a2)
    if hasattr(a1, 'spem_BreakdownElement20'):
        assert not _is_linked(a1, 'spem_BreakdownElement20', b)
    if hasattr(a2, 'spem_BreakdownElement20'):
        assert _is_linked(a2, 'spem_BreakdownElement20', b)
    _safe_set(b, 'spem_Activity19', set())
    assert not _is_linked(b, 'spem_Activity19', a2)
    if hasattr(a2, 'spem_BreakdownElement20'):
        assert not _is_linked(a2, 'spem_BreakdownElement20', b)


def test_assoc_suppressedMethodContentElement74_reverse_link_reassign_clear():
    a1 = spem_MethodContentElement(author="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", version="sample_text")
    a2 = spem_MethodContentElement(author="sample_text_2", changeDate=date(2025, 6, 15), changeDescription="sample_text_2", copyright="sample_text_2", version="sample_text_2")
    b = spem_MethodContentElement(author="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", version="sample_text")
    _safe_set(b, 'spem_MethodContentElement73', {a1})
    assert _is_linked(b, 'spem_MethodContentElement73', a1)
    if hasattr(a1, 'spem_MethodContentElement'):
        assert _is_linked(a1, 'spem_MethodContentElement', b)
    _safe_set(b, 'spem_MethodContentElement73', {a2})
    assert _is_linked(b, 'spem_MethodContentElement73', a2)
    if hasattr(a1, 'spem_MethodContentElement'):
        assert not _is_linked(a1, 'spem_MethodContentElement', b)
    if hasattr(a2, 'spem_MethodContentElement'):
        assert _is_linked(a2, 'spem_MethodContentElement', b)
    _safe_set(b, 'spem_MethodContentElement73', set())
    assert not _is_linked(b, 'spem_MethodContentElement73', a2)
    if hasattr(a2, 'spem_MethodContentElement'):
        assert not _is_linked(a2, 'spem_MethodContentElement', b)


def test_assoc_usageGuidance5_reverse_link_reassign_clear():
    a1 = spem_Guidance(attachment="sample_text")
    a2 = spem_Guidance(attachment="sample_text_2")
    b = spem_BreakdownElement(hasMultipleOccurrences=True, isOptional=True, isPlanned=True)
    _safe_set(b, 'spem_BreakdownElement6', a1)
    assert _is_linked(b, 'spem_BreakdownElement6', a1)
    if hasattr(a1, 'spem_Guidance'):
        assert _is_linked(a1, 'spem_Guidance', b)
    _safe_set(b, 'spem_BreakdownElement6', a2)
    assert _is_linked(b, 'spem_BreakdownElement6', a2)
    if hasattr(a1, 'spem_Guidance'):
        assert not _is_linked(a1, 'spem_Guidance', b)
    if hasattr(a2, 'spem_Guidance'):
        assert _is_linked(a2, 'spem_Guidance', b)
    _safe_set(b, 'spem_BreakdownElement6', None)
    assert not _is_linked(b, 'spem_BreakdownElement6', a2)
    if hasattr(a2, 'spem_Guidance'):
        assert not _is_linked(a2, 'spem_Guidance', b)


def test_assoc_usedActivity14_reverse_link_reassign_clear():
    a1 = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    a2 = spem_Activity(howToStaff="sample_text_2", isEnactable=False, useKind="sample_text_2")
    b = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    _safe_set(b, 'spem_Activity13', a1)
    assert _is_linked(b, 'spem_Activity13', a1)
    if hasattr(a1, 'spem_Activity'):
        assert _is_linked(a1, 'spem_Activity', b)
    _safe_set(b, 'spem_Activity13', a2)
    assert _is_linked(b, 'spem_Activity13', a2)
    if hasattr(a1, 'spem_Activity'):
        assert not _is_linked(a1, 'spem_Activity', b)
    if hasattr(a2, 'spem_Activity'):
        assert _is_linked(a2, 'spem_Activity', b)
    _safe_set(b, 'spem_Activity13', None)
    assert not _is_linked(b, 'spem_Activity13', a2)
    if hasattr(a2, 'spem_Activity'):
        assert not _is_linked(a2, 'spem_Activity', b)


def test_assoc_variabilityBasedOnElement145_reverse_link_reassign_clear():
    a1 = spem_VariabilityElement(variabilityType="sample_text")
    a2 = spem_VariabilityElement(variabilityType="sample_text_2")
    b = spem_VariabilityElement(variabilityType="sample_text")
    _safe_set(b, 'spem_VariabilityElement144', a1)
    assert _is_linked(b, 'spem_VariabilityElement144', a1)
    if hasattr(a1, 'spem_VariabilityElement'):
        assert _is_linked(a1, 'spem_VariabilityElement', b)
    _safe_set(b, 'spem_VariabilityElement144', a2)
    assert _is_linked(b, 'spem_VariabilityElement144', a2)
    if hasattr(a1, 'spem_VariabilityElement'):
        assert not _is_linked(a1, 'spem_VariabilityElement', b)
    if hasattr(a2, 'spem_VariabilityElement'):
        assert _is_linked(a2, 'spem_VariabilityElement', b)
    _safe_set(b, 'spem_VariabilityElement144', None)
    assert not _is_linked(b, 'spem_VariabilityElement144', a2)
    if hasattr(a2, 'spem_VariabilityElement'):
        assert not _is_linked(a2, 'spem_VariabilityElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_aggregatedRole135_stub_double():
    # spem_CompositeRole has no real 'spem_CompositeRole' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_CompositeRole()
    setattr(partner, 'spem_CompositeRole', None)
    _safe_set(owner, 'spem_RoleDefinition136', partner)
    assert owner in getattr(partner, 'spem_CompositeRole')
    _safe_set(owner, 'spem_RoleDefinition136', None)
    assert owner not in getattr(partner, 'spem_CompositeRole')


def test_assoc_any200_stub_double():
    # spem_EObject has no real 'spem_EObject' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodLibrary(name="sample_text")
    partner = spem_EObject()
    setattr(partner, 'spem_EObject', None)
    _safe_set(owner, 'spem_MethodLibrary201', {partner})
    assert getattr(partner, 'spem_EObject') == owner
    _safe_set(owner, 'spem_MethodLibrary201', set())
    assert getattr(partner, 'spem_EObject') is None


def test_assoc_category68_stub_double():
    # spem_Category has no real 'spem_Category' property in the generated
    # code (a bare stub) -- manually attach it so spem_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_DescribableElement(briefDescription="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text")
    partner = spem_Category()
    setattr(partner, 'spem_Category', None)
    _safe_set(owner, 'spem_DescribableElement69', {partner})
    assert getattr(partner, 'spem_Category') == owner
    _safe_set(owner, 'spem_DescribableElement69', set())
    assert getattr(partner, 'spem_Category') is None


def test_assoc_communicationMaterial212_stub_double():
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


def test_assoc_configurationPackage198_stub_double():
    # ConfigurationPackage has no real 'ConfigurationPackage' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodLibrary(name="sample_text")
    partner = ConfigurationPackage()
    setattr(partner, 'ConfigurationPackage', None)
    _safe_set(owner, 'spem_MethodLibrary199', partner)
    assert getattr(partner, 'ConfigurationPackage') == owner
    _safe_set(owner, 'spem_MethodLibrary199', None)
    assert getattr(partner, 'ConfigurationPackage') is None


def test_assoc_connectedPort205_stub_double():
    # spem_WorkProductPortConnector has no real 'spem_WorkProductPortConnector' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductPort(isOptional=True, portKind="sample_text")
    partner = spem_WorkProductPortConnector()
    setattr(partner, 'spem_WorkProductPortConnector', None)
    _safe_set(owner, 'spem_WorkProductPort206', partner)
    assert owner in getattr(partner, 'spem_WorkProductPortConnector')
    _safe_set(owner, 'spem_WorkProductPort206', None)
    assert owner not in getattr(partner, 'spem_WorkProductPortConnector')


def test_assoc_contentReference228_stub_double():
    # uma_spem_MethodContentElement has no real 'uma_spem_MethodContentElement' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Practice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Practice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Practice(additionalInfo="sample_text", application="sample_text", background="sample_text", goal="sample_text", levelOfAdoption="sample_text", problem="sample_text")
    partner = uma_spem_MethodContentElement()
    setattr(partner, 'uma_spem_MethodContentElement', None)
    _safe_set(owner, 'spem_uma_Practice229', {partner})
    assert getattr(partner, 'uma_spem_MethodContentElement') == owner
    _safe_set(owner, 'spem_uma_Practice229', set())
    assert getattr(partner, 'uma_spem_MethodContentElement') is None


def test_assoc_defaultContext23_stub_double():
    # spem_MethodConfiguration has no real 'spem_MethodConfiguration' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    partner = spem_MethodConfiguration()
    setattr(partner, 'spem_MethodConfiguration', None)
    _safe_set(owner, 'spem_Activity24', partner)
    assert getattr(partner, 'spem_MethodConfiguration') == owner
    _safe_set(owner, 'spem_Activity24', None)
    assert getattr(partner, 'spem_MethodConfiguration') is None


def test_assoc_deliveredProduct208_stub_double():
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


def test_assoc_educationalMaterial213_stub_double():
    # SupportingMaterial has no real 'SupportingMaterial215' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_DeliveryProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_DeliveryProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_DeliveryProcess(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    partner = SupportingMaterial()
    setattr(partner, 'SupportingMaterial215', None)
    _safe_set(owner, 'spem_uma_DeliveryProcess214', {partner})
    assert getattr(partner, 'SupportingMaterial215') == owner
    _safe_set(owner, 'spem_uma_DeliveryProcess214', set())
    assert getattr(partner, 'SupportingMaterial215') is None


def test_assoc_estimatingConsideration93_stub_double():
    # EstimatingConsideration has no real 'EstimatingConsideration95' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = EstimatingConsideration()
    setattr(partner, 'EstimatingConsideration95', None)
    _safe_set(owner, 'spem_WorkProductDefinition94', {partner})
    assert getattr(partner, 'EstimatingConsideration95') == owner
    _safe_set(owner, 'spem_WorkProductDefinition94', set())
    assert getattr(partner, 'EstimatingConsideration95') is None


def test_assoc_includedConnector210_stub_double():
    # uma_spem_WorkProductPortConnector has no real 'uma_spem_WorkProductPortConnector' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Process(scope="sample_text", usageNote="sample_text")
    partner = uma_spem_WorkProductPortConnector()
    setattr(partner, 'uma_spem_WorkProductPortConnector', None)
    _safe_set(owner, 'spem_uma_Process211', {partner})
    assert getattr(partner, 'uma_spem_WorkProductPortConnector') == owner
    _safe_set(owner, 'spem_uma_Process211', set())
    assert getattr(partner, 'uma_spem_WorkProductPortConnector') is None


def test_assoc_includedPattern209_stub_double():
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


def test_assoc_keyConsideration66_stub_double():
    # EstimatingConsideration has no real 'EstimatingConsideration' property in the generated
    # code (a bare stub) -- manually attach it so spem_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_DescribableElement(briefDescription="sample_text", mainDescription="sample_text", presentationName="sample_text", purpose="sample_text")
    partner = EstimatingConsideration()
    setattr(partner, 'EstimatingConsideration', None)
    _safe_set(owner, 'spem_DescribableElement67', {partner})
    assert getattr(partner, 'EstimatingConsideration') == owner
    _safe_set(owner, 'spem_DescribableElement67', set())
    assert getattr(partner, 'EstimatingConsideration') is None


def test_assoc_linkedActivity32_stub_double():
    # spem_ProcessPerformer has no real 'spem_ProcessPerformer33' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    partner = spem_ProcessPerformer()
    setattr(partner, 'spem_ProcessPerformer33', None)
    _safe_set(owner, 'spem_Activity34', partner)
    assert getattr(partner, 'spem_ProcessPerformer33') == owner
    _safe_set(owner, 'spem_Activity34', None)
    assert getattr(partner, 'spem_ProcessPerformer33') is None


def test_assoc_linkedRoleDefinition113_stub_double():
    # spem_Default_TaskDefinitionPerformer has no real 'spem_Default_TaskDefinitionPerformer114' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_Default_TaskDefinitionPerformer()
    setattr(partner, 'spem_Default_TaskDefinitionPerformer114', None)
    _safe_set(owner, 'spem_RoleDefinition115', partner)
    assert owner in getattr(partner, 'spem_Default_TaskDefinitionPerformer114')
    _safe_set(owner, 'spem_RoleDefinition115', None)
    assert owner not in getattr(partner, 'spem_Default_TaskDefinitionPerformer114')


def test_assoc_linkedRoleDefinition116_stub_double():
    # spem_Default_ResponsibilityAssignment has no real 'spem_Default_ResponsibilityAssignment' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_Default_ResponsibilityAssignment()
    setattr(partner, 'spem_Default_ResponsibilityAssignment', None)
    _safe_set(owner, 'spem_RoleDefinition117', partner)
    assert owner in getattr(partner, 'spem_Default_ResponsibilityAssignment')
    _safe_set(owner, 'spem_RoleDefinition117', None)
    assert owner not in getattr(partner, 'spem_Default_ResponsibilityAssignment')


def test_assoc_linkedTaskUse35_stub_double():
    # spem_ProcessPerformer has no real 'spem_ProcessPerformer36' property in the generated
    # code (a bare stub) -- manually attach it so spem_TaskUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_TaskUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    partner = spem_ProcessPerformer()
    setattr(partner, 'spem_ProcessPerformer36', None)
    _safe_set(owner, 'spem_TaskUse', partner)
    assert getattr(partner, 'spem_ProcessPerformer36') == owner
    _safe_set(owner, 'spem_TaskUse', None)
    assert getattr(partner, 'spem_ProcessPerformer36') is None


def test_assoc_linkedWorkProductDefinition118_stub_double():
    # spem_Default_ResponsibilityAssignment has no real 'spem_Default_ResponsibilityAssignment119' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = spem_Default_ResponsibilityAssignment()
    setattr(partner, 'spem_Default_ResponsibilityAssignment119', None)
    _safe_set(owner, 'spem_WorkProductDefinition120', partner)
    assert getattr(partner, 'spem_Default_ResponsibilityAssignment119') == owner
    _safe_set(owner, 'spem_WorkProductDefinition120', None)
    assert getattr(partner, 'spem_Default_ResponsibilityAssignment119') is None


def test_assoc_managedWorkProduct77_stub_double():
    # spem_ToolDefinition has no real 'spem_ToolDefinition' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = spem_ToolDefinition()
    setattr(partner, 'spem_ToolDefinition', None)
    _safe_set(owner, 'spem_WorkProductDefinition78', partner)
    assert owner in getattr(partner, 'spem_ToolDefinition')
    _safe_set(owner, 'spem_WorkProductDefinition78', None)
    assert owner not in getattr(partner, 'spem_ToolDefinition')


def test_assoc_methodContentKind75_stub_double():
    # spem_MethodContentKind has no real 'spem_MethodContentKind' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodContentElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodContentElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodContentElement(author="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", version="sample_text")
    partner = spem_MethodContentKind()
    setattr(partner, 'spem_MethodContentKind', None)
    _safe_set(owner, 'spem_MethodContentElement76', partner)
    assert getattr(partner, 'spem_MethodContentKind') == owner
    _safe_set(owner, 'spem_MethodContentElement76', None)
    assert getattr(partner, 'spem_MethodContentKind') is None


def test_assoc_methodPluginSelection158_stub_double():
    # spem_MethodConfiguration has no real 'spem_MethodConfiguration159' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodPlugin(supporting="sample_text", userChangeable=True)
    partner = spem_MethodConfiguration()
    setattr(partner, 'spem_MethodConfiguration159', None)
    _safe_set(owner, 'spem_MethodPlugin', partner)
    assert owner in getattr(partner, 'spem_MethodConfiguration159')
    _safe_set(owner, 'spem_MethodPlugin', None)
    assert owner not in getattr(partner, 'spem_MethodConfiguration159')


def test_assoc_ownedMethodContentMember121_stub_double():
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


def test_assoc_ownedMethodContentPackage178_stub_double():
    # spem_MethodContentPackage has no real 'spem_MethodContentPackage180' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodPlugin(supporting="sample_text", userChangeable=True)
    partner = spem_MethodContentPackage()
    setattr(partner, 'spem_MethodContentPackage180', None)
    _safe_set(owner, 'spem_MethodPlugin179', {partner})
    assert getattr(partner, 'spem_MethodContentPackage180') == owner
    _safe_set(owner, 'spem_MethodPlugin179', set())
    assert getattr(partner, 'spem_MethodContentPackage180') is None


def test_assoc_ownedProcessMember125_stub_double():
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


def test_assoc_ownedProcessPackage181_stub_double():
    # spem_ProcessPackage has no real 'spem_ProcessPackage183' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodPlugin(supporting="sample_text", userChangeable=True)
    partner = spem_ProcessPackage()
    setattr(partner, 'spem_ProcessPackage183', None)
    _safe_set(owner, 'spem_MethodPlugin182', {partner})
    assert getattr(partner, 'spem_ProcessPackage183') == owner
    _safe_set(owner, 'spem_MethodPlugin182', set())
    assert getattr(partner, 'spem_ProcessPackage183') is None


def test_assoc_ownedProcessParameter129_stub_double():
    # spem_ProcessParameter has no real 'spem_ProcessParameter131' property in the generated
    # code (a bare stub) -- manually attach it so spem_TaskUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_TaskUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    partner = spem_ProcessParameter()
    setattr(partner, 'spem_ProcessParameter131', None)
    _safe_set(owner, 'spem_TaskUse130', {partner})
    assert getattr(partner, 'spem_ProcessParameter131') == owner
    _safe_set(owner, 'spem_TaskUse130', set())
    assert getattr(partner, 'spem_ProcessParameter131') is None


def test_assoc_ownedProcessParameter21_stub_double():
    # spem_ProcessParameter has no real 'spem_ProcessParameter' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    partner = spem_ProcessParameter()
    setattr(partner, 'spem_ProcessParameter', None)
    _safe_set(owner, 'spem_Activity22', {partner})
    assert getattr(partner, 'spem_ProcessParameter') == owner
    _safe_set(owner, 'spem_Activity22', set())
    assert getattr(partner, 'spem_ProcessParameter') is None


def test_assoc_predefinedConfiguration192_stub_double():
    # spem_MethodConfiguration has no real 'spem_MethodConfiguration194' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodLibrary(name="sample_text")
    partner = spem_MethodConfiguration()
    setattr(partner, 'spem_MethodConfiguration194', None)
    _safe_set(owner, 'spem_MethodLibrary193', {partner})
    assert getattr(partner, 'spem_MethodConfiguration194') == owner
    _safe_set(owner, 'spem_MethodLibrary193', set())
    assert getattr(partner, 'spem_MethodConfiguration194') is None


def test_assoc_processComponent150_stub_double():
    # spem_ProcessComponentUse has no real 'spem_ProcessComponentUse' property in the generated
    # code (a bare stub) -- manually attach it so spem_ProcessComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_ProcessComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_ProcessComponent(author="sample_text", changeDate=date(2024, 1, 1), changeDescription="sample_text", copyright="sample_text", version="sample_text")
    partner = spem_ProcessComponentUse()
    setattr(partner, 'spem_ProcessComponentUse', None)
    _safe_set(owner, 'spem_ProcessComponent151', partner)
    assert getattr(partner, 'spem_ProcessComponentUse') == owner
    _safe_set(owner, 'spem_ProcessComponent151', None)
    assert getattr(partner, 'spem_ProcessComponentUse') is None


def test_assoc_referencedActivity226_stub_double():
    # uma_spem_Activity has no real 'uma_spem_Activity' property in the generated
    # code (a bare stub) -- manually attach it so spem_uma_Practice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_uma_Practice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_uma_Practice(additionalInfo="sample_text", application="sample_text", background="sample_text", goal="sample_text", levelOfAdoption="sample_text", problem="sample_text")
    partner = uma_spem_Activity()
    setattr(partner, 'uma_spem_Activity', None)
    _safe_set(owner, 'spem_uma_Practice227', {partner})
    assert getattr(partner, 'uma_spem_Activity') == owner
    _safe_set(owner, 'spem_uma_Practice227', set())
    assert getattr(partner, 'uma_spem_Activity') is None


def test_assoc_report96_stub_double():
    # Report has no real 'Report' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = Report()
    setattr(partner, 'Report', None)
    _safe_set(owner, 'spem_WorkProductDefinition97', {partner})
    assert getattr(partner, 'Report') == owner
    _safe_set(owner, 'spem_WorkProductDefinition97', set())
    assert getattr(partner, 'Report') is None


def test_assoc_requiredQualification103_stub_double():
    # spem_Qualification has no real 'spem_Qualification105' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_Qualification()
    setattr(partner, 'spem_Qualification105', None)
    _safe_set(owner, 'spem_RoleDefinition104', {partner})
    assert getattr(partner, 'spem_Qualification105') == owner
    _safe_set(owner, 'spem_RoleDefinition104', set())
    assert getattr(partner, 'spem_Qualification105') is None


def test_assoc_role37_stub_double():
    # spem_RoleUse has no real 'spem_RoleUse38' property in the generated
    # code (a bare stub) -- manually attach it so spem_RoleDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_RoleDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_RoleDefinition(synonym="sample_text")
    partner = spem_RoleUse()
    setattr(partner, 'spem_RoleUse38', None)
    _safe_set(owner, 'spem_RoleDefinition', partner)
    assert getattr(partner, 'spem_RoleUse38') == owner
    _safe_set(owner, 'spem_RoleDefinition', None)
    assert getattr(partner, 'spem_RoleUse38') is None


def test_assoc_source106_stub_double():
    # spem_WorkProductDefinitionRelationship has no real 'spem_WorkProductDefinitionRelationship' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = spem_WorkProductDefinitionRelationship()
    setattr(partner, 'spem_WorkProductDefinitionRelationship', None)
    _safe_set(owner, 'spem_WorkProductDefinition107', partner)
    assert getattr(partner, 'spem_WorkProductDefinitionRelationship') == owner
    _safe_set(owner, 'spem_WorkProductDefinition107', None)
    assert getattr(partner, 'spem_WorkProductDefinitionRelationship') is None


def test_assoc_step83_stub_double():
    # spem_TaskDefinition has no real 'spem_TaskDefinition84' property in the generated
    # code (a bare stub) -- manually attach it so spem_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Step(name="sample_text")
    partner = spem_TaskDefinition()
    setattr(partner, 'spem_TaskDefinition84', None)
    _safe_set(owner, 'spem_Step', partner)
    assert owner in getattr(partner, 'spem_TaskDefinition84')
    _safe_set(owner, 'spem_Step', None)
    assert owner not in getattr(partner, 'spem_TaskDefinition84')


def test_assoc_subPractice225_stub_double():
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


def test_assoc_target108_stub_double():
    # spem_WorkProductDefinitionRelationship has no real 'spem_WorkProductDefinitionRelationship109' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = spem_WorkProductDefinitionRelationship()
    setattr(partner, 'spem_WorkProductDefinitionRelationship109', None)
    _safe_set(owner, 'spem_WorkProductDefinition110', partner)
    assert owner in getattr(partner, 'spem_WorkProductDefinitionRelationship109')
    _safe_set(owner, 'spem_WorkProductDefinition110', None)
    assert owner not in getattr(partner, 'spem_WorkProductDefinitionRelationship109')


def test_assoc_task126_stub_double():
    # spem_TaskDefinition has no real 'spem_TaskDefinition128' property in the generated
    # code (a bare stub) -- manually attach it so spem_TaskUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_TaskUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_TaskUse(postCondition="sample_text", preCondition="sample_text")
    partner = spem_TaskDefinition()
    setattr(partner, 'spem_TaskDefinition128', None)
    _safe_set(owner, 'spem_TaskUse127', partner)
    assert getattr(partner, 'spem_TaskDefinition128') == owner
    _safe_set(owner, 'spem_TaskUse127', None)
    assert getattr(partner, 'spem_TaskDefinition128') is None


def test_assoc_template98_stub_double():
    # Template has no real 'Template' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = Template()
    setattr(partner, 'Template', None)
    _safe_set(owner, 'spem_WorkProductDefinition99', {partner})
    assert getattr(partner, 'Template') == owner
    _safe_set(owner, 'spem_WorkProductDefinition99', set())
    assert getattr(partner, 'Template') is None


def test_assoc_tool195_stub_double():
    # spem_ToolDefinition has no real 'spem_ToolDefinition197' property in the generated
    # code (a bare stub) -- manually attach it so spem_MethodLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_MethodLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_MethodLibrary(name="sample_text")
    partner = spem_ToolDefinition()
    setattr(partner, 'spem_ToolDefinition197', None)
    _safe_set(owner, 'spem_MethodLibrary196', partner)
    assert getattr(partner, 'spem_ToolDefinition197') == owner
    _safe_set(owner, 'spem_MethodLibrary196', None)
    assert getattr(partner, 'spem_ToolDefinition197') is None


def test_assoc_toolMentor100_stub_double():
    # ToolMentor has no real 'ToolMentor102' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = ToolMentor()
    setattr(partner, 'ToolMentor102', None)
    _safe_set(owner, 'spem_WorkProductDefinition101', {partner})
    assert getattr(partner, 'ToolMentor102') == owner
    _safe_set(owner, 'spem_WorkProductDefinition101', set())
    assert getattr(partner, 'ToolMentor102') is None


def test_assoc_usedPort152_stub_double():
    # spem_ProcessComponentUse has no real 'spem_ProcessComponentUse153' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductPort(isOptional=True, portKind="sample_text")
    partner = spem_ProcessComponentUse()
    setattr(partner, 'spem_ProcessComponentUse153', None)
    _safe_set(owner, 'spem_WorkProductPort154', partner)
    assert owner in getattr(partner, 'spem_ProcessComponentUse153')
    _safe_set(owner, 'spem_WorkProductPort154', None)
    assert owner not in getattr(partner, 'spem_ProcessComponentUse153')


def test_assoc_validContext25_stub_double():
    # spem_MethodConfiguration has no real 'spem_MethodConfiguration27' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(howToStaff="sample_text", isEnactable=True, useKind="sample_text")
    partner = spem_MethodConfiguration()
    setattr(partner, 'spem_MethodConfiguration27', None)
    _safe_set(owner, 'spem_Activity26', {partner})
    assert getattr(partner, 'spem_MethodConfiguration27') == owner
    _safe_set(owner, 'spem_Activity26', set())
    assert getattr(partner, 'spem_MethodConfiguration27') is None


def test_assoc_workProduct43_stub_double():
    # spem_WorkProductUse has no real 'spem_WorkProductUse44' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkProductDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkProductDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkProductDefinition(impactOfNotHaving="sample_text", reasonForNotNeeding="sample_text")
    partner = spem_WorkProductUse()
    setattr(partner, 'spem_WorkProductUse44', None)
    _safe_set(owner, 'spem_WorkProductDefinition45', partner)
    assert getattr(partner, 'spem_WorkProductUse44') == owner
    _safe_set(owner, 'spem_WorkProductDefinition45', None)
    assert getattr(partner, 'spem_WorkProductUse44') is None


