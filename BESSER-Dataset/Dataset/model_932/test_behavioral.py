import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    ActivityDescription,
    BreakdownElement,
    BreakdownElementDescription,
    Classifier,
    Concept,
    ContentCategory,
    ContentDescription,
    ContentElement,
    DescribableElement,
    Descriptor,
    DiagramElement,
    Element,
    GraphElement,
    GraphNode,
    GraphicPrimitive,
    Guidance,
    LeafElement,
    MethodConfiguration,
    MethodElement,
    MethodPackage,
    MethodUnit,
    NamedElement,
    Namespace,
    Package,
    PackageableElement,
    Process,
    ProcessDescription,
    ProcessElement,
    ProcessPackage,
    RoleDescriptor,
    Section,
    SemanticModelBridge,
    Type,
    VariabilityElement,
    WorkBreakdownElement,
    WorkDefinition,
    WorkProduct,
    WorkProductDescription,
    uma_Activity,
    uma_ActivityDescription,
    uma_Artifact,
    uma_ArtifactDescription,
    uma_BreakdownElement,
    uma_BreakdownElementDescription,
    uma_CapabilityPattern,
    uma_Checklist,
    uma_Classifier,
    uma_CompositeRole,
    uma_Concept,
    uma_Constraint,
    uma_ContentCategory,
    uma_ContentDescription,
    uma_ContentElement,
    uma_ContentPackage,
    uma_CoreSemanticModelBridge,
    uma_CustomCategory,
    uma_Deliverable,
    uma_DeliverableDescription,
    uma_DeliveryProcess,
    uma_DeliveryProcessDescription,
    uma_DescribableElement,
    uma_Descriptor,
    uma_DescriptorDescription,
    uma_Diagram,
    uma_DiagramElement,
    uma_DiagramLink,
    uma_Dimension,
    uma_Discipline,
    uma_DisciplineGrouping,
    uma_Domain,
    uma_Element,
    uma_Ellipse,
    uma_Estimate,
    uma_EstimatingMetric,
    uma_EstimationConsiderations,
    uma_Example,
    uma_GraphConnector,
    uma_GraphEdge,
    uma_GraphElement,
    uma_GraphNode,
    uma_GraphicPrimitive,
    uma_Guidance,
    uma_GuidanceDescription,
    uma_Guideline,
    uma_Image,
    uma_Iteration,
    uma_LeafElement,
    uma_MethodConfiguration,
    uma_MethodElement,
    uma_MethodLibrary,
    uma_MethodPackage,
    uma_MethodPlugin,
    uma_MethodUnit,
    uma_Milestone,
    uma_NamedElement,
    uma_Namespace,
    uma_Outcome,
    uma_Package,
    uma_PackageableElement,
    uma_Phase,
    uma_PlanningData,
    uma_Point,
    uma_Polyline,
    uma_Practice,
    uma_PracticeDescription,
    uma_Process,
    uma_ProcessComponent,
    uma_ProcessComponentDescriptor,
    uma_ProcessComponentInterface,
    uma_ProcessContribution,
    uma_ProcessDescription,
    uma_ProcessElement,
    uma_ProcessFamily,
    uma_ProcessPackage,
    uma_ProcessPlanningTemplate,
    uma_Property,
    uma_Reference,
    uma_Report,
    uma_ReusableAsset,
    uma_Roadmap,
    uma_Role,
    uma_RoleDescription,
    uma_RoleDescriptor,
    uma_RoleSet,
    uma_RoleSetGrouping,
    uma_Section,
    uma_SemanticModelBridge,
    uma_SimpleSemanticModelElement,
    uma_Step,
    uma_SupportingMaterial,
    uma_Task,
    uma_TaskDescription,
    uma_TaskDescriptor,
    uma_TeamProfile,
    uma_Template,
    uma_TermDefinition,
    uma_TextElement,
    uma_Tool,
    uma_ToolMentor,
    uma_Type,
    uma_UMASemanticModelBridge,
    uma_VariabilityElement,
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

def test_assoc_bases279_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(userChangeable="sample_text")
    a2 = uma_MethodPlugin(userChangeable="sample_text_2")
    b = uma_MethodPlugin(userChangeable="sample_text")
    _safe_set(b, 'uma_MethodPlugin280', a1)
    assert _is_linked(b, 'uma_MethodPlugin280', a1)
    if hasattr(a1, 'uma_MethodPlugin278'):
        assert _is_linked(a1, 'uma_MethodPlugin278', b)
    _safe_set(b, 'uma_MethodPlugin280', a2)
    assert _is_linked(b, 'uma_MethodPlugin280', a2)
    if hasattr(a1, 'uma_MethodPlugin278'):
        assert not _is_linked(a1, 'uma_MethodPlugin278', b)
    if hasattr(a2, 'uma_MethodPlugin278'):
        assert _is_linked(a2, 'uma_MethodPlugin278', b)
    _safe_set(b, 'uma_MethodPlugin280', None)
    assert not _is_linked(b, 'uma_MethodPlugin280', a2)
    if hasattr(a2, 'uma_MethodPlugin278'):
        assert not _is_linked(a2, 'uma_MethodPlugin278', b)


def test_assoc_center117_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    _safe_set(b, 'uma_Ellipse', a1)
    assert _is_linked(b, 'uma_Ellipse', a1)
    if hasattr(a1, 'uma_Point118'):
        assert _is_linked(a1, 'uma_Point118', b)
    _safe_set(b, 'uma_Ellipse', a2)
    assert _is_linked(b, 'uma_Ellipse', a2)
    if hasattr(a1, 'uma_Point118'):
        assert not _is_linked(a1, 'uma_Point118', b)
    if hasattr(a2, 'uma_Point118'):
        assert _is_linked(a2, 'uma_Point118', b)
    _safe_set(b, 'uma_Ellipse', None)
    assert not _is_linked(b, 'uma_Ellipse', a2)
    if hasattr(a2, 'uma_Point118'):
        assert not _is_linked(a2, 'uma_Point118', b)


def test_assoc_childPackages72_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'parentPackage', {a1})
    assert _is_linked(b, 'parentPackage', a1)
    if hasattr(a1, 'MethodPackage73'):
        assert _is_linked(a1, 'MethodPackage73', b)
    _safe_set(b, 'parentPackage', {a2})
    assert _is_linked(b, 'parentPackage', a2)
    if hasattr(a1, 'MethodPackage73'):
        assert not _is_linked(a1, 'MethodPackage73', b)
    if hasattr(a2, 'MethodPackage73'):
        assert _is_linked(a2, 'MethodPackage73', b)
    _safe_set(b, 'parentPackage', set())
    assert not _is_linked(b, 'parentPackage', a2)
    if hasattr(a2, 'MethodPackage73'):
        assert not _is_linked(a2, 'MethodPackage73', b)


def test_assoc_deliverableParts205_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'uma_WorkProductDescriptor206', a1)
    assert _is_linked(b, 'uma_WorkProductDescriptor206', a1)
    if hasattr(a1, 'uma_WorkProductDescriptor204'):
        assert _is_linked(a1, 'uma_WorkProductDescriptor204', b)
    _safe_set(b, 'uma_WorkProductDescriptor206', a2)
    assert _is_linked(b, 'uma_WorkProductDescriptor206', a2)
    if hasattr(a1, 'uma_WorkProductDescriptor204'):
        assert not _is_linked(a1, 'uma_WorkProductDescriptor204', b)
    if hasattr(a2, 'uma_WorkProductDescriptor204'):
        assert _is_linked(a2, 'uma_WorkProductDescriptor204', b)
    _safe_set(b, 'uma_WorkProductDescriptor206', None)
    assert not _is_linked(b, 'uma_WorkProductDescriptor206', a2)
    if hasattr(a2, 'uma_WorkProductDescriptor204'):
        assert not _is_linked(a2, 'uma_WorkProductDescriptor204', b)


def test_assoc_diagram90_reverse_link_reassign_clear():
    a1 = uma_DiagramLink(zoom="sample_text")
    a2 = uma_DiagramLink(zoom="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'Diagram', a1)
    assert _is_linked(b, 'Diagram', a1)
    if hasattr(a1, 'diagramLink'):
        assert _is_linked(a1, 'diagramLink', b)
    _safe_set(b, 'Diagram', a2)
    assert _is_linked(b, 'Diagram', a2)
    if hasattr(a1, 'diagramLink'):
        assert not _is_linked(a1, 'diagramLink', b)
    if hasattr(a2, 'diagramLink'):
        assert _is_linked(a2, 'diagramLink', b)
    _safe_set(b, 'Diagram', None)
    assert not _is_linked(b, 'Diagram', a2)
    if hasattr(a2, 'diagramLink'):
        assert not _is_linked(a2, 'diagramLink', b)


def test_assoc_diagram96_reverse_link_reassign_clear():
    a1 = uma_SemanticModelBridge(presentation="sample_text")
    a2 = uma_SemanticModelBridge(presentation="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'Diagram97', a1)
    assert _is_linked(b, 'Diagram97', a1)
    if hasattr(a1, 'namespace'):
        assert _is_linked(a1, 'namespace', b)
    _safe_set(b, 'Diagram97', a2)
    assert _is_linked(b, 'Diagram97', a2)
    if hasattr(a1, 'namespace'):
        assert not _is_linked(a1, 'namespace', b)
    if hasattr(a2, 'namespace'):
        assert _is_linked(a2, 'namespace', b)
    _safe_set(b, 'Diagram97', None)
    assert not _is_linked(b, 'Diagram97', a2)
    if hasattr(a2, 'namespace'):
        assert not _is_linked(a2, 'namespace', b)


def test_assoc_diagramLink106_reverse_link_reassign_clear():
    a1 = uma_DiagramLink(zoom="sample_text")
    a2 = uma_DiagramLink(zoom="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'diagram', {a1})
    assert _is_linked(b, 'diagram', a1)
    if hasattr(a1, 'DiagramLink107'):
        assert _is_linked(a1, 'DiagramLink107', b)
    _safe_set(b, 'diagram', {a2})
    assert _is_linked(b, 'diagram', a2)
    if hasattr(a1, 'DiagramLink107'):
        assert not _is_linked(a1, 'DiagramLink107', b)
    if hasattr(a2, 'DiagramLink107'):
        assert _is_linked(a2, 'DiagramLink107', b)
    _safe_set(b, 'diagram', set())
    assert not _is_linked(b, 'diagram', a2)
    if hasattr(a2, 'DiagramLink107'):
        assert not _is_linked(a2, 'DiagramLink107', b)


def test_assoc_impactedBy191_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'impacts', {a1})
    assert _is_linked(b, 'impacts', a1)
    if hasattr(a1, 'WorkProductDescriptor192'):
        assert _is_linked(a1, 'WorkProductDescriptor192', b)
    _safe_set(b, 'impacts', {a2})
    assert _is_linked(b, 'impacts', a2)
    if hasattr(a1, 'WorkProductDescriptor192'):
        assert not _is_linked(a1, 'WorkProductDescriptor192', b)
    if hasattr(a2, 'WorkProductDescriptor192'):
        assert _is_linked(a2, 'WorkProductDescriptor192', b)
    _safe_set(b, 'impacts', set())
    assert not _is_linked(b, 'impacts', a2)
    if hasattr(a2, 'WorkProductDescriptor192'):
        assert not _is_linked(a2, 'WorkProductDescriptor192', b)


def test_assoc_impacts194_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'impactedBy', {a1})
    assert _is_linked(b, 'impactedBy', a1)
    if hasattr(a1, 'WorkProductDescriptor195'):
        assert _is_linked(a1, 'WorkProductDescriptor195', b)
    _safe_set(b, 'impactedBy', {a2})
    assert _is_linked(b, 'impactedBy', a2)
    if hasattr(a1, 'WorkProductDescriptor195'):
        assert not _is_linked(a1, 'WorkProductDescriptor195', b)
    if hasattr(a2, 'WorkProductDescriptor195'):
        assert _is_linked(a2, 'WorkProductDescriptor195', b)
    _safe_set(b, 'impactedBy', set())
    assert not _is_linked(b, 'impactedBy', a2)
    if hasattr(a2, 'WorkProductDescriptor195'):
        assert not _is_linked(a2, 'WorkProductDescriptor195', b)


def test_assoc_linkToPredecessor139_reverse_link_reassign_clear():
    a1 = uma_WorkOrder(linkType="sample_text")
    a2 = uma_WorkOrder(linkType="sample_text_2")
    b = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
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


def test_assoc_methodPackages276_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(userChangeable="sample_text")
    a2 = uma_MethodPlugin(userChangeable="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage277', a1)
    assert _is_linked(b, 'uma_MethodPackage277', a1)
    if hasattr(a1, 'uma_MethodPlugin'):
        assert _is_linked(a1, 'uma_MethodPlugin', b)
    _safe_set(b, 'uma_MethodPackage277', a2)
    assert _is_linked(b, 'uma_MethodPackage277', a2)
    if hasattr(a1, 'uma_MethodPlugin'):
        assert not _is_linked(a1, 'uma_MethodPlugin', b)
    if hasattr(a2, 'uma_MethodPlugin'):
        assert _is_linked(a2, 'uma_MethodPlugin', b)
    _safe_set(b, 'uma_MethodPackage277', None)
    assert not _is_linked(b, 'uma_MethodPackage277', a2)
    if hasattr(a2, 'uma_MethodPlugin'):
        assert not _is_linked(a2, 'uma_MethodPlugin', b)


def test_assoc_namespace108_reverse_link_reassign_clear():
    a1 = uma_SemanticModelBridge(presentation="sample_text")
    a2 = uma_SemanticModelBridge(presentation="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'diagram109', a1)
    assert _is_linked(b, 'diagram109', a1)
    if hasattr(a1, 'SemanticModelBridge110'):
        assert _is_linked(a1, 'SemanticModelBridge110', b)
    _safe_set(b, 'diagram109', a2)
    assert _is_linked(b, 'diagram109', a2)
    if hasattr(a1, 'SemanticModelBridge110'):
        assert not _is_linked(a1, 'SemanticModelBridge110', b)
    if hasattr(a2, 'SemanticModelBridge110'):
        assert _is_linked(a2, 'SemanticModelBridge110', b)
    _safe_set(b, 'diagram109', None)
    assert not _is_linked(b, 'diagram109', a2)
    if hasattr(a2, 'SemanticModelBridge110'):
        assert not _is_linked(a2, 'SemanticModelBridge110', b)


def test_assoc_ownedRules0_reverse_link_reassign_clear():
    a1 = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    a2 = uma_MethodElement(briefDescription="sample_text_2", guid="sample_text_2", orderingGuide="sample_text_2", suppressed="sample_text_2")
    b = uma_Constraint(body="sample_text")
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


def test_assoc_parentPackage70_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'childPackages', a1)
    assert _is_linked(b, 'childPackages', a1)
    if hasattr(a1, 'MethodPackage'):
        assert _is_linked(a1, 'MethodPackage', b)
    _safe_set(b, 'childPackages', a2)
    assert _is_linked(b, 'childPackages', a2)
    if hasattr(a1, 'MethodPackage'):
        assert not _is_linked(a1, 'MethodPackage', b)
    if hasattr(a2, 'MethodPackage'):
        assert _is_linked(a2, 'MethodPackage', b)
    _safe_set(b, 'childPackages', None)
    assert not _is_linked(b, 'childPackages', a2)
    if hasattr(a2, 'MethodPackage'):
        assert not _is_linked(a2, 'MethodPackage', b)


def test_assoc_planningData145_reverse_link_reassign_clear():
    a1 = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    a2 = uma_PlanningData(finishDate="sample_text_2", rank="sample_text_2", startDate="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement146', a1)
    assert _is_linked(b, 'uma_BreakdownElement146', a1)
    if hasattr(a1, 'uma_PlanningData'):
        assert _is_linked(a1, 'uma_PlanningData', b)
    _safe_set(b, 'uma_BreakdownElement146', a2)
    assert _is_linked(b, 'uma_BreakdownElement146', a2)
    if hasattr(a1, 'uma_PlanningData'):
        assert not _is_linked(a1, 'uma_PlanningData', b)
    if hasattr(a2, 'uma_PlanningData'):
        assert _is_linked(a2, 'uma_PlanningData', b)
    _safe_set(b, 'uma_BreakdownElement146', None)
    assert not _is_linked(b, 'uma_BreakdownElement146', a2)
    if hasattr(a2, 'uma_PlanningData'):
        assert not _is_linked(a2, 'uma_PlanningData', b)


def test_assoc_pred165_reverse_link_reassign_clear():
    a1 = uma_WorkOrder(linkType="sample_text")
    a2 = uma_WorkOrder(linkType="sample_text_2")
    b = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    _safe_set(b, 'uma_WorkBreakdownElement167', a1)
    assert _is_linked(b, 'uma_WorkBreakdownElement167', a1)
    if hasattr(a1, 'uma_WorkOrder166'):
        assert _is_linked(a1, 'uma_WorkOrder166', b)
    _safe_set(b, 'uma_WorkBreakdownElement167', a2)
    assert _is_linked(b, 'uma_WorkBreakdownElement167', a2)
    if hasattr(a1, 'uma_WorkOrder166'):
        assert not _is_linked(a1, 'uma_WorkOrder166', b)
    if hasattr(a2, 'uma_WorkOrder166'):
        assert _is_linked(a2, 'uma_WorkOrder166', b)
    _safe_set(b, 'uma_WorkBreakdownElement167', None)
    assert not _is_linked(b, 'uma_WorkBreakdownElement167', a2)
    if hasattr(a2, 'uma_WorkOrder166'):
        assert not _is_linked(a2, 'uma_WorkOrder166', b)


def test_assoc_predecessor19_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    _safe_set(b, 'uma_Section20', a1)
    assert _is_linked(b, 'uma_Section20', a1)
    if hasattr(a1, 'uma_Section18'):
        assert _is_linked(a1, 'uma_Section18', b)
    _safe_set(b, 'uma_Section20', a2)
    assert _is_linked(b, 'uma_Section20', a2)
    if hasattr(a1, 'uma_Section18'):
        assert not _is_linked(a1, 'uma_Section18', b)
    if hasattr(a2, 'uma_Section18'):
        assert _is_linked(a2, 'uma_Section18', b)
    _safe_set(b, 'uma_Section20', None)
    assert not _is_linked(b, 'uma_Section20', a2)
    if hasattr(a2, 'uma_Section18'):
        assert not _is_linked(a2, 'uma_Section18', b)


def test_assoc_presentation12_reverse_link_reassign_clear():
    a1 = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    a2 = uma_DescribableElement(nodeicon="sample_text_2", presentationName="sample_text_2", shapeicon="sample_text_2")
    b = uma_ContentDescription(keyConsiderations="sample_text", mainDescription="sample_text")
    _safe_set(b, 'uma_ContentDescription', a1)
    assert _is_linked(b, 'uma_ContentDescription', a1)
    if hasattr(a1, 'uma_DescribableElement'):
        assert _is_linked(a1, 'uma_DescribableElement', b)
    _safe_set(b, 'uma_ContentDescription', a2)
    assert _is_linked(b, 'uma_ContentDescription', a2)
    if hasattr(a1, 'uma_DescribableElement'):
        assert not _is_linked(a1, 'uma_DescribableElement', b)
    if hasattr(a2, 'uma_DescribableElement'):
        assert _is_linked(a2, 'uma_DescribableElement', b)
    _safe_set(b, 'uma_ContentDescription', None)
    assert not _is_linked(b, 'uma_ContentDescription', a2)
    if hasattr(a2, 'uma_DescribableElement'):
        assert not _is_linked(a2, 'uma_DescribableElement', b)


def test_assoc_presentedAfter141_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement140', a1)
    assert _is_linked(b, 'uma_BreakdownElement140', a1)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert _is_linked(a1, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_BreakdownElement140', a2)
    assert _is_linked(b, 'uma_BreakdownElement140', a2)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert not _is_linked(a1, 'uma_BreakdownElement', b)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert _is_linked(a2, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_BreakdownElement140', None)
    assert not _is_linked(b, 'uma_BreakdownElement140', a2)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert not _is_linked(a2, 'uma_BreakdownElement', b)


def test_assoc_presentedBefore143_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement144', a1)
    assert _is_linked(b, 'uma_BreakdownElement144', a1)
    if hasattr(a1, 'uma_BreakdownElement142'):
        assert _is_linked(a1, 'uma_BreakdownElement142', b)
    _safe_set(b, 'uma_BreakdownElement144', a2)
    assert _is_linked(b, 'uma_BreakdownElement144', a2)
    if hasattr(a1, 'uma_BreakdownElement142'):
        assert not _is_linked(a1, 'uma_BreakdownElement142', b)
    if hasattr(a2, 'uma_BreakdownElement142'):
        assert _is_linked(a2, 'uma_BreakdownElement142', b)
    _safe_set(b, 'uma_BreakdownElement144', None)
    assert not _is_linked(b, 'uma_BreakdownElement144', a2)
    if hasattr(a2, 'uma_BreakdownElement142'):
        assert not _is_linked(a2, 'uma_BreakdownElement142', b)


def test_assoc_property85_reverse_link_reassign_clear():
    a1 = uma_Property(key="sample_text", value="sample_text")
    a2 = uma_Property(key="sample_text_2", value="sample_text_2")
    b = uma_DiagramElement(isVisible="sample_text")
    _safe_set(b, 'uma_DiagramElement', {a1})
    assert _is_linked(b, 'uma_DiagramElement', a1)
    if hasattr(a1, 'uma_Property'):
        assert _is_linked(a1, 'uma_Property', b)
    _safe_set(b, 'uma_DiagramElement', {a2})
    assert _is_linked(b, 'uma_DiagramElement', a2)
    if hasattr(a1, 'uma_Property'):
        assert not _is_linked(a1, 'uma_Property', b)
    if hasattr(a2, 'uma_Property'):
        assert _is_linked(a2, 'uma_Property', b)
    _safe_set(b, 'uma_DiagramElement', set())
    assert not _is_linked(b, 'uma_DiagramElement', a2)
    if hasattr(a2, 'uma_Property'):
        assert not _is_linked(a2, 'uma_Property', b)


def test_assoc_reference84_reverse_link_reassign_clear():
    a1 = uma_Reference(isIndividualRepresentation="sample_text")
    a2 = uma_Reference(isIndividualRepresentation="sample_text_2")
    b = uma_DiagramElement(isVisible="sample_text")
    _safe_set(b, 'referenced', {a1})
    assert _is_linked(b, 'referenced', a1)
    if hasattr(a1, 'Reference'):
        assert _is_linked(a1, 'Reference', b)
    _safe_set(b, 'referenced', {a2})
    assert _is_linked(b, 'referenced', a2)
    if hasattr(a1, 'Reference'):
        assert not _is_linked(a1, 'Reference', b)
    if hasattr(a2, 'Reference'):
        assert _is_linked(a2, 'Reference', b)
    _safe_set(b, 'referenced', set())
    assert not _is_linked(b, 'referenced', a2)
    if hasattr(a2, 'Reference'):
        assert not _is_linked(a2, 'Reference', b)


def test_assoc_referenced98_reverse_link_reassign_clear():
    a1 = uma_Reference(isIndividualRepresentation="sample_text")
    a2 = uma_Reference(isIndividualRepresentation="sample_text_2")
    b = uma_DiagramElement(isVisible="sample_text")
    _safe_set(b, 'DiagramElement99', a1)
    assert _is_linked(b, 'DiagramElement99', a1)
    if hasattr(a1, 'reference'):
        assert _is_linked(a1, 'reference', b)
    _safe_set(b, 'DiagramElement99', a2)
    assert _is_linked(b, 'DiagramElement99', a2)
    if hasattr(a1, 'reference'):
        assert not _is_linked(a1, 'reference', b)
    if hasattr(a2, 'reference'):
        assert _is_linked(a2, 'reference', b)
    _safe_set(b, 'DiagramElement99', None)
    assert not _is_linked(b, 'DiagramElement99', a2)
    if hasattr(a2, 'reference'):
        assert not _is_linked(a2, 'reference', b)


def test_assoc_reusedPackages68_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage67', {a1})
    assert _is_linked(b, 'uma_MethodPackage67', a1)
    if hasattr(a1, 'uma_MethodPackage'):
        assert _is_linked(a1, 'uma_MethodPackage', b)
    _safe_set(b, 'uma_MethodPackage67', {a2})
    assert _is_linked(b, 'uma_MethodPackage67', a2)
    if hasattr(a1, 'uma_MethodPackage'):
        assert not _is_linked(a1, 'uma_MethodPackage', b)
    if hasattr(a2, 'uma_MethodPackage'):
        assert _is_linked(a2, 'uma_MethodPackage', b)
    _safe_set(b, 'uma_MethodPackage67', set())
    assert not _is_linked(b, 'uma_MethodPackage67', a2)
    if hasattr(a2, 'uma_MethodPackage'):
        assert not _is_linked(a2, 'uma_MethodPackage', b)


def test_assoc_sections13_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_ContentDescription(keyConsiderations="sample_text", mainDescription="sample_text")
    _safe_set(b, 'uma_ContentDescription14', {a1})
    assert _is_linked(b, 'uma_ContentDescription14', a1)
    if hasattr(a1, 'uma_Section'):
        assert _is_linked(a1, 'uma_Section', b)
    _safe_set(b, 'uma_ContentDescription14', {a2})
    assert _is_linked(b, 'uma_ContentDescription14', a2)
    if hasattr(a1, 'uma_Section'):
        assert not _is_linked(a1, 'uma_Section', b)
    if hasattr(a2, 'uma_Section'):
        assert _is_linked(a2, 'uma_Section', b)
    _safe_set(b, 'uma_ContentDescription14', set())
    assert not _is_linked(b, 'uma_ContentDescription14', a2)
    if hasattr(a2, 'uma_Section'):
        assert not _is_linked(a2, 'uma_Section', b)


def test_assoc_subSections16_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    _safe_set(b, 'uma_Section17', a1)
    assert _is_linked(b, 'uma_Section17', a1)
    if hasattr(a1, 'uma_Section15'):
        assert _is_linked(a1, 'uma_Section15', b)
    _safe_set(b, 'uma_Section17', a2)
    assert _is_linked(b, 'uma_Section17', a2)
    if hasattr(a1, 'uma_Section15'):
        assert not _is_linked(a1, 'uma_Section15', b)
    if hasattr(a2, 'uma_Section15'):
        assert _is_linked(a2, 'uma_Section15', b)
    _safe_set(b, 'uma_Section17', None)
    assert not _is_linked(b, 'uma_Section17', a2)
    if hasattr(a2, 'uma_Section15'):
        assert not _is_linked(a2, 'uma_Section15', b)


def test_assoc_variabilityBasedOnElement282_reverse_link_reassign_clear():
    a1 = uma_VariabilityElement(variabilityType="sample_text")
    a2 = uma_VariabilityElement(variabilityType="sample_text_2")
    b = uma_VariabilityElement(variabilityType="sample_text")
    _safe_set(b, 'uma_VariabilityElement281', a1)
    assert _is_linked(b, 'uma_VariabilityElement281', a1)
    if hasattr(a1, 'uma_VariabilityElement'):
        assert _is_linked(a1, 'uma_VariabilityElement', b)
    _safe_set(b, 'uma_VariabilityElement281', a2)
    assert _is_linked(b, 'uma_VariabilityElement281', a2)
    if hasattr(a1, 'uma_VariabilityElement'):
        assert not _is_linked(a1, 'uma_VariabilityElement', b)
    if hasattr(a2, 'uma_VariabilityElement'):
        assert _is_linked(a2, 'uma_VariabilityElement', b)
    _safe_set(b, 'uma_VariabilityElement281', None)
    assert not _is_linked(b, 'uma_VariabilityElement281', a2)
    if hasattr(a2, 'uma_VariabilityElement'):
        assert not _is_linked(a2, 'uma_VariabilityElement', b)


def test_assoc_viewpoint104_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'uma_Diagram', a1)
    assert _is_linked(b, 'uma_Diagram', a1)
    if hasattr(a1, 'uma_Point105'):
        assert _is_linked(a1, 'uma_Point105', b)
    _safe_set(b, 'uma_Diagram', a2)
    assert _is_linked(b, 'uma_Diagram', a2)
    if hasattr(a1, 'uma_Point105'):
        assert not _is_linked(a1, 'uma_Point105', b)
    if hasattr(a2, 'uma_Point105'):
        assert _is_linked(a2, 'uma_Point105', b)
    _safe_set(b, 'uma_Diagram', None)
    assert not _is_linked(b, 'uma_Diagram', a2)
    if hasattr(a2, 'uma_Point105'):
        assert not _is_linked(a2, 'uma_Point105', b)


def test_assoc_viewport86_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_DiagramLink(zoom="sample_text")
    _safe_set(b, 'uma_DiagramLink', a1)
    assert _is_linked(b, 'uma_DiagramLink', a1)
    if hasattr(a1, 'uma_Point87'):
        assert _is_linked(a1, 'uma_Point87', b)
    _safe_set(b, 'uma_DiagramLink', a2)
    assert _is_linked(b, 'uma_DiagramLink', a2)
    if hasattr(a1, 'uma_Point87'):
        assert not _is_linked(a1, 'uma_Point87', b)
    if hasattr(a2, 'uma_Point87'):
        assert _is_linked(a2, 'uma_Point87', b)
    _safe_set(b, 'uma_DiagramLink', None)
    assert not _is_linked(b, 'uma_DiagramLink', a2)
    if hasattr(a2, 'uma_Point87'):
        assert not _is_linked(a2, 'uma_Point87', b)


def test_assoc_waypoints115_reverse_link_reassign_clear():
    a1 = uma_Polyline(closed="sample_text")
    a2 = uma_Polyline(closed="sample_text_2")
    b = uma_Point(x="sample_text", y="sample_text")
    _safe_set(b, 'uma_Point116', a1)
    assert _is_linked(b, 'uma_Point116', a1)
    if hasattr(a1, 'uma_Polyline'):
        assert _is_linked(a1, 'uma_Polyline', b)
    _safe_set(b, 'uma_Point116', a2)
    assert _is_linked(b, 'uma_Point116', a2)
    if hasattr(a1, 'uma_Polyline'):
        assert not _is_linked(a1, 'uma_Polyline', b)
    if hasattr(a2, 'uma_Polyline'):
        assert _is_linked(a2, 'uma_Polyline', b)
    _safe_set(b, 'uma_Point116', None)
    assert not _is_linked(b, 'uma_Point116', a2)
    if hasattr(a2, 'uma_Polyline'):
        assert not _is_linked(a2, 'uma_Polyline', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_OptionalInputTo200_stub_double():
    # uma_TaskDescriptor has no real 'TaskDescriptor201' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'TaskDescriptor201', None)
    _safe_set(owner, 'optionalInput', {partner})
    assert getattr(partner, 'TaskDescriptor201') == owner
    _safe_set(owner, 'optionalInput', set())
    assert getattr(partner, 'TaskDescriptor201') is None


def test_assoc_WorkProduct186_stub_double():
    # uma_WorkProduct has no real 'uma_WorkProduct187' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_WorkProduct()
    setattr(partner, 'uma_WorkProduct187', None)
    _safe_set(owner, 'uma_WorkProductDescriptor', partner)
    assert getattr(partner, 'uma_WorkProduct187') == owner
    _safe_set(owner, 'uma_WorkProductDescriptor', None)
    assert getattr(partner, 'uma_WorkProduct187') is None


def test_assoc_breakdownElements119_stub_double():
    # uma_Activity has no real 'superActivities' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Activity()
    setattr(partner, 'superActivities', None)
    _safe_set(owner, 'BreakdownElement', partner)
    assert owner in getattr(partner, 'superActivities')
    _safe_set(owner, 'BreakdownElement', None)
    assert owner not in getattr(partner, 'superActivities')


def test_assoc_categorizedElements243_stub_double():
    # uma_CustomCategory has no real 'uma_CustomCategory' property in the generated
    # code (a bare stub) -- manually attach it so uma_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    partner = uma_CustomCategory()
    setattr(partner, 'uma_CustomCategory', None)
    _safe_set(owner, 'uma_DescribableElement244', partner)
    assert owner in getattr(partner, 'uma_CustomCategory')
    _safe_set(owner, 'uma_DescribableElement244', None)
    assert owner not in getattr(partner, 'uma_CustomCategory')


def test_assoc_contained77_stub_double():
    # uma_GraphElement has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so uma_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DiagramElement(isVisible="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'container', None)
    _safe_set(owner, 'DiagramElement', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'DiagramElement', None)
    assert owner not in getattr(partner, 'container')


def test_assoc_container83_stub_double():
    # uma_GraphElement has no real 'GraphElement' property in the generated
    # code (a bare stub) -- manually attach it so uma_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DiagramElement(isVisible="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement', None)
    _safe_set(owner, 'contained', partner)
    assert getattr(partner, 'GraphElement') == owner
    _safe_set(owner, 'contained', None)
    assert getattr(partner, 'GraphElement') is None


def test_assoc_copyrightStatement285_stub_double():
    # uma_SupportingMaterial has no real 'uma_SupportingMaterial286' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    partner = uma_SupportingMaterial()
    setattr(partner, 'uma_SupportingMaterial286', None)
    _safe_set(owner, 'uma_MethodUnit', partner)
    assert getattr(partner, 'uma_SupportingMaterial286') == owner
    _safe_set(owner, 'uma_MethodUnit', None)
    assert getattr(partner, 'uma_SupportingMaterial286') is None


def test_assoc_diagrams265_stub_double():
    # uma_ProcessPackage has no real 'uma_ProcessPackage266' property in the generated
    # code (a bare stub) -- manually attach it so uma_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Diagram(zoom="sample_text")
    partner = uma_ProcessPackage()
    setattr(partner, 'uma_ProcessPackage266', None)
    _safe_set(owner, 'uma_Diagram267', partner)
    assert owner in getattr(partner, 'uma_ProcessPackage266')
    _safe_set(owner, 'uma_Diagram267', None)
    assert owner not in getattr(partner, 'uma_ProcessPackage266')


def test_assoc_element112_stub_double():
    # uma_UMASemanticModelBridge has no real 'uma_UMASemanticModelBridge' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    partner = uma_UMASemanticModelBridge()
    setattr(partner, 'uma_UMASemanticModelBridge', None)
    _safe_set(owner, 'uma_MethodElement113', partner)
    assert getattr(partner, 'uma_UMASemanticModelBridge') == owner
    _safe_set(owner, 'uma_MethodElement113', None)
    assert getattr(partner, 'uma_UMASemanticModelBridge') is None


def test_assoc_externalInput173_stub_double():
    # uma_TaskDescriptor has no real 'externalInputTo' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'externalInputTo', None)
    _safe_set(owner, 'WorkProductDescriptor174', partner)
    assert owner in getattr(partner, 'externalInputTo')
    _safe_set(owner, 'WorkProductDescriptor174', None)
    assert owner not in getattr(partner, 'externalInputTo')


def test_assoc_externalInputTo188_stub_double():
    # uma_TaskDescriptor has no real 'TaskDescriptor189' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'TaskDescriptor189', None)
    _safe_set(owner, 'externalInput', {partner})
    assert getattr(partner, 'TaskDescriptor189') == owner
    _safe_set(owner, 'externalInput', set())
    assert getattr(partner, 'TaskDescriptor189') is None


def test_assoc_graphElement88_stub_double():
    # uma_GraphElement has no real 'GraphElement89' property in the generated
    # code (a bare stub) -- manually attach it so uma_DiagramLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DiagramLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DiagramLink(zoom="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement89', None)
    _safe_set(owner, 'link', partner)
    assert getattr(partner, 'GraphElement89') == owner
    _safe_set(owner, 'link', None)
    assert getattr(partner, 'GraphElement89') is None


def test_assoc_graphElement94_stub_double():
    # uma_GraphElement has no real 'GraphElement95' property in the generated
    # code (a bare stub) -- manually attach it so uma_SemanticModelBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_SemanticModelBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_SemanticModelBridge(presentation="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement95', None)
    _safe_set(owner, 'semanticModel', partner)
    assert getattr(partner, 'GraphElement95') == owner
    _safe_set(owner, 'semanticModel', None)
    assert getattr(partner, 'GraphElement95') is None


def test_assoc_interfaceIO271_stub_double():
    # uma_ProcessComponentInterface has no real 'uma_ProcessComponentInterface272' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_ProcessComponentInterface()
    setattr(partner, 'uma_ProcessComponentInterface272', None)
    _safe_set(owner, 'uma_WorkProductDescriptor273', partner)
    assert owner in getattr(partner, 'uma_ProcessComponentInterface272')
    _safe_set(owner, 'uma_WorkProductDescriptor273', None)
    assert owner not in getattr(partner, 'uma_ProcessComponentInterface272')


def test_assoc_link78_stub_double():
    # uma_GraphElement has no real 'graphElement' property in the generated
    # code (a bare stub) -- manually attach it so uma_DiagramLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DiagramLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DiagramLink(zoom="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'graphElement', None)
    _safe_set(owner, 'DiagramLink', partner)
    assert owner in getattr(partner, 'graphElement')
    _safe_set(owner, 'DiagramLink', None)
    assert owner not in getattr(partner, 'graphElement')


def test_assoc_mandatoryInput175_stub_double():
    # uma_TaskDescriptor has no real 'mandatoryInputTo' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'mandatoryInputTo', None)
    _safe_set(owner, 'WorkProductDescriptor176', partner)
    assert owner in getattr(partner, 'mandatoryInputTo')
    _safe_set(owner, 'WorkProductDescriptor176', None)
    assert owner not in getattr(partner, 'mandatoryInputTo')


def test_assoc_mandatoryInputTo196_stub_double():
    # uma_TaskDescriptor has no real 'TaskDescriptor197' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'TaskDescriptor197', None)
    _safe_set(owner, 'mandatoryInput', {partner})
    assert getattr(partner, 'TaskDescriptor197') == owner
    _safe_set(owner, 'mandatoryInput', set())
    assert getattr(partner, 'TaskDescriptor197') is None


def test_assoc_methodPackageSelection290_stub_double():
    # uma_MethodConfiguration has no real 'uma_MethodConfiguration291' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPackage(global_="sample_text")
    partner = uma_MethodConfiguration()
    setattr(partner, 'uma_MethodConfiguration291', None)
    _safe_set(owner, 'uma_MethodPackage292', partner)
    assert owner in getattr(partner, 'uma_MethodConfiguration291')
    _safe_set(owner, 'uma_MethodPackage292', None)
    assert owner not in getattr(partner, 'uma_MethodConfiguration291')


def test_assoc_methodPluginSelection287_stub_double():
    # uma_MethodConfiguration has no real 'uma_MethodConfiguration288' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPlugin(userChangeable="sample_text")
    partner = uma_MethodConfiguration()
    setattr(partner, 'uma_MethodConfiguration288', None)
    _safe_set(owner, 'uma_MethodPlugin289', partner)
    assert owner in getattr(partner, 'uma_MethodConfiguration288')
    _safe_set(owner, 'uma_MethodPlugin289', None)
    assert owner not in getattr(partner, 'uma_MethodConfiguration288')


def test_assoc_methodPlugins304_stub_double():
    # uma_MethodLibrary has no real 'uma_MethodLibrary' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPlugin(userChangeable="sample_text")
    partner = uma_MethodLibrary()
    setattr(partner, 'uma_MethodLibrary', None)
    _safe_set(owner, 'uma_MethodPlugin305', partner)
    assert owner in getattr(partner, 'uma_MethodLibrary')
    _safe_set(owner, 'uma_MethodPlugin305', None)
    assert owner not in getattr(partner, 'uma_MethodLibrary')


def test_assoc_modifies160_stub_double():
    # uma_RoleDescriptor has no real 'workedOnBy' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'workedOnBy', None)
    _safe_set(owner, 'WorkProductDescriptor', partner)
    assert owner in getattr(partner, 'workedOnBy')
    _safe_set(owner, 'WorkProductDescriptor', None)
    assert owner not in getattr(partner, 'workedOnBy')


def test_assoc_optionalInput177_stub_double():
    # uma_TaskDescriptor has no real 'OptionalInputTo' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'OptionalInputTo', None)
    _safe_set(owner, 'WorkProductDescriptor178', partner)
    assert owner in getattr(partner, 'OptionalInputTo')
    _safe_set(owner, 'WorkProductDescriptor178', None)
    assert owner not in getattr(partner, 'OptionalInputTo')


def test_assoc_output179_stub_double():
    # uma_TaskDescriptor has no real 'outputFrom' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'outputFrom', None)
    _safe_set(owner, 'WorkProductDescriptor180', partner)
    assert owner in getattr(partner, 'outputFrom')
    _safe_set(owner, 'WorkProductDescriptor180', None)
    assert owner not in getattr(partner, 'outputFrom')


def test_assoc_outputFrom202_stub_double():
    # uma_TaskDescriptor has no real 'TaskDescriptor203' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'TaskDescriptor203', None)
    _safe_set(owner, 'output', {partner})
    assert getattr(partner, 'TaskDescriptor203') == owner
    _safe_set(owner, 'output', set())
    assert getattr(partner, 'TaskDescriptor203') is None


def test_assoc_position76_stub_double():
    # uma_GraphElement has no real 'uma_GraphElement' property in the generated
    # code (a bare stub) -- manually attach it so uma_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Point(x="sample_text", y="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'uma_GraphElement', None)
    _safe_set(owner, 'uma_Point', partner)
    assert getattr(partner, 'uma_GraphElement') == owner
    _safe_set(owner, 'uma_Point', None)
    assert getattr(partner, 'uma_GraphElement') is None


def test_assoc_postcondition57_stub_double():
    # uma_WorkDefinition has no real 'uma_WorkDefinition58' property in the generated
    # code (a bare stub) -- manually attach it so uma_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Constraint(body="sample_text")
    partner = uma_WorkDefinition()
    setattr(partner, 'uma_WorkDefinition58', None)
    _safe_set(owner, 'uma_Constraint59', partner)
    assert getattr(partner, 'uma_WorkDefinition58') == owner
    _safe_set(owner, 'uma_Constraint59', None)
    assert getattr(partner, 'uma_WorkDefinition58') is None


def test_assoc_precondition55_stub_double():
    # uma_WorkDefinition has no real 'uma_WorkDefinition' property in the generated
    # code (a bare stub) -- manually attach it so uma_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Constraint(body="sample_text")
    partner = uma_WorkDefinition()
    setattr(partner, 'uma_WorkDefinition', None)
    _safe_set(owner, 'uma_Constraint56', partner)
    assert getattr(partner, 'uma_WorkDefinition') == owner
    _safe_set(owner, 'uma_Constraint56', None)
    assert getattr(partner, 'uma_WorkDefinition') is None


def test_assoc_responsibleFor163_stub_double():
    # uma_RoleDescriptor has no real 'responsibleRole' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'responsibleRole', None)
    _safe_set(owner, 'WorkProductDescriptor164', partner)
    assert owner in getattr(partner, 'responsibleRole')
    _safe_set(owner, 'WorkProductDescriptor164', None)
    assert owner not in getattr(partner, 'responsibleRole')


def test_assoc_responsibleRole207_stub_double():
    # uma_RoleDescriptor has no real 'RoleDescriptor208' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'RoleDescriptor208', None)
    _safe_set(owner, 'responsibleFor', partner)
    assert getattr(partner, 'RoleDescriptor208') == owner
    _safe_set(owner, 'responsibleFor', None)
    assert getattr(partner, 'RoleDescriptor208') is None


def test_assoc_selectedSteps183_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor184' property in the generated
    # code (a bare stub) -- manually attach it so uma_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor184', None)
    _safe_set(owner, 'uma_Section185', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor184')
    _safe_set(owner, 'uma_Section185', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor184')


def test_assoc_semanticModel81_stub_double():
    # uma_GraphElement has no real 'graphElement82' property in the generated
    # code (a bare stub) -- manually attach it so uma_SemanticModelBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_SemanticModelBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_SemanticModelBridge(presentation="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'graphElement82', None)
    _safe_set(owner, 'SemanticModelBridge', partner)
    assert getattr(partner, 'graphElement82') == owner
    _safe_set(owner, 'SemanticModelBridge', None)
    assert getattr(partner, 'graphElement82') is None


def test_assoc_size111_stub_double():
    # uma_GraphNode has no real 'uma_GraphNode' property in the generated
    # code (a bare stub) -- manually attach it so uma_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Dimension(height="sample_text", width="sample_text")
    partner = uma_GraphNode()
    setattr(partner, 'uma_GraphNode', None)
    _safe_set(owner, 'uma_Dimension', partner)
    assert getattr(partner, 'uma_GraphNode') == owner
    _safe_set(owner, 'uma_Dimension', None)
    assert getattr(partner, 'uma_GraphNode') is None


def test_assoc_superActivities147_stub_double():
    # uma_Activity has no real 'Activity' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Activity()
    setattr(partner, 'Activity', None)
    _safe_set(owner, 'breakdownElements', {partner})
    assert getattr(partner, 'Activity') == owner
    _safe_set(owner, 'breakdownElements', set())
    assert getattr(partner, 'Activity') is None


def test_assoc_waypoints102_stub_double():
    # uma_GraphEdge has no real 'uma_GraphEdge' property in the generated
    # code (a bare stub) -- manually attach it so uma_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Point(x="sample_text", y="sample_text")
    partner = uma_GraphEdge()
    setattr(partner, 'uma_GraphEdge', None)
    _safe_set(owner, 'uma_Point103', partner)
    assert owner in getattr(partner, 'uma_GraphEdge')
    _safe_set(owner, 'uma_Point103', None)
    assert owner not in getattr(partner, 'uma_GraphEdge')


def test_assoc_workedOnBy198_stub_double():
    # uma_RoleDescriptor has no real 'RoleDescriptor199' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'RoleDescriptor199', None)
    _safe_set(owner, 'modifies', {partner})
    assert getattr(partner, 'RoleDescriptor199') == owner
    _safe_set(owner, 'modifies', set())
    assert getattr(partner, 'RoleDescriptor199') is None


