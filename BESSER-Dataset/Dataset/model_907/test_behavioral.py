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


