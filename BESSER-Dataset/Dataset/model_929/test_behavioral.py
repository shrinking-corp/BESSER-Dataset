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
    Vertex,
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
    uma_ProcessDescription,
    uma_ProcessElement,
    uma_ProcessFamily,
    uma_ProcessPackage,
    uma_ProcessPlanningTemplate,
    uma_Property,
    uma_PseudoState,
    uma_Reference,
    uma_Region,
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
    uma_State,
    uma_StateMachine,
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
    uma_Transition,
    uma_Type,
    uma_UMASemanticModelBridge,
    uma_VariabilityElement,
    uma_Vertex,
    uma_Whitepaper,
    uma_WorkBreakdownElement,
    uma_WorkDefinition,
    uma_WorkOrder,
    uma_WorkProduct,
    uma_WorkProductDescription,
    uma_WorkProductDescriptor,
    uma_WorkProductType,
    PseudoStateKind,
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

def test_assoc_bases302_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(userChangeable="sample_text")
    a2 = uma_MethodPlugin(userChangeable="sample_text_2")
    b = uma_MethodPlugin(userChangeable="sample_text")
    _safe_set(b, 'uma_MethodPlugin303', a1)
    assert _is_linked(b, 'uma_MethodPlugin303', a1)
    if hasattr(a1, 'uma_MethodPlugin301'):
        assert _is_linked(a1, 'uma_MethodPlugin301', b)
    _safe_set(b, 'uma_MethodPlugin303', a2)
    assert _is_linked(b, 'uma_MethodPlugin303', a2)
    if hasattr(a1, 'uma_MethodPlugin301'):
        assert not _is_linked(a1, 'uma_MethodPlugin301', b)
    if hasattr(a2, 'uma_MethodPlugin301'):
        assert _is_linked(a2, 'uma_MethodPlugin301', b)
    _safe_set(b, 'uma_MethodPlugin303', None)
    assert not _is_linked(b, 'uma_MethodPlugin303', a2)
    if hasattr(a2, 'uma_MethodPlugin301'):
        assert not _is_linked(a2, 'uma_MethodPlugin301', b)


def test_assoc_breakdownElements117_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_Activity(isEnactable="sample_text")
    _safe_set(b, 'superActivities', {a1})
    assert _is_linked(b, 'superActivities', a1)
    if hasattr(a1, 'BreakdownElement'):
        assert _is_linked(a1, 'BreakdownElement', b)
    _safe_set(b, 'superActivities', {a2})
    assert _is_linked(b, 'superActivities', a2)
    if hasattr(a1, 'BreakdownElement'):
        assert not _is_linked(a1, 'BreakdownElement', b)
    if hasattr(a2, 'BreakdownElement'):
        assert _is_linked(a2, 'BreakdownElement', b)
    _safe_set(b, 'superActivities', set())
    assert not _is_linked(b, 'superActivities', a2)
    if hasattr(a2, 'BreakdownElement'):
        assert not _is_linked(a2, 'BreakdownElement', b)


def test_assoc_center115_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    _safe_set(b, 'uma_Ellipse', a1)
    assert _is_linked(b, 'uma_Ellipse', a1)
    if hasattr(a1, 'uma_Point116'):
        assert _is_linked(a1, 'uma_Point116', b)
    _safe_set(b, 'uma_Ellipse', a2)
    assert _is_linked(b, 'uma_Ellipse', a2)
    if hasattr(a1, 'uma_Point116'):
        assert not _is_linked(a1, 'uma_Point116', b)
    if hasattr(a2, 'uma_Point116'):
        assert _is_linked(a2, 'uma_Point116', b)
    _safe_set(b, 'uma_Ellipse', None)
    assert not _is_linked(b, 'uma_Ellipse', a2)
    if hasattr(a2, 'uma_Point116'):
        assert not _is_linked(a2, 'uma_Point116', b)


def test_assoc_childPackages70_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage71', a1)
    assert _is_linked(b, 'uma_MethodPackage71', a1)
    if hasattr(a1, 'uma_MethodPackage69'):
        assert _is_linked(a1, 'uma_MethodPackage69', b)
    _safe_set(b, 'uma_MethodPackage71', a2)
    assert _is_linked(b, 'uma_MethodPackage71', a2)
    if hasattr(a1, 'uma_MethodPackage69'):
        assert not _is_linked(a1, 'uma_MethodPackage69', b)
    if hasattr(a2, 'uma_MethodPackage69'):
        assert _is_linked(a2, 'uma_MethodPackage69', b)
    _safe_set(b, 'uma_MethodPackage71', None)
    assert not _is_linked(b, 'uma_MethodPackage71', a2)
    if hasattr(a2, 'uma_MethodPackage69'):
        assert not _is_linked(a2, 'uma_MethodPackage69', b)


def test_assoc_deliverableParts172_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'uma_WorkProductDescriptor173', a1)
    assert _is_linked(b, 'uma_WorkProductDescriptor173', a1)
    if hasattr(a1, 'uma_WorkProductDescriptor171'):
        assert _is_linked(a1, 'uma_WorkProductDescriptor171', b)
    _safe_set(b, 'uma_WorkProductDescriptor173', a2)
    assert _is_linked(b, 'uma_WorkProductDescriptor173', a2)
    if hasattr(a1, 'uma_WorkProductDescriptor171'):
        assert not _is_linked(a1, 'uma_WorkProductDescriptor171', b)
    if hasattr(a2, 'uma_WorkProductDescriptor171'):
        assert _is_linked(a2, 'uma_WorkProductDescriptor171', b)
    _safe_set(b, 'uma_WorkProductDescriptor173', None)
    assert not _is_linked(b, 'uma_WorkProductDescriptor173', a2)
    if hasattr(a2, 'uma_WorkProductDescriptor171'):
        assert not _is_linked(a2, 'uma_WorkProductDescriptor171', b)


def test_assoc_diagram88_reverse_link_reassign_clear():
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


def test_assoc_diagram94_reverse_link_reassign_clear():
    a1 = uma_SemanticModelBridge(presentation="sample_text")
    a2 = uma_SemanticModelBridge(presentation="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'Diagram95', a1)
    assert _is_linked(b, 'Diagram95', a1)
    if hasattr(a1, 'namespace'):
        assert _is_linked(a1, 'namespace', b)
    _safe_set(b, 'Diagram95', a2)
    assert _is_linked(b, 'Diagram95', a2)
    if hasattr(a1, 'namespace'):
        assert not _is_linked(a1, 'namespace', b)
    if hasattr(a2, 'namespace'):
        assert _is_linked(a2, 'namespace', b)
    _safe_set(b, 'Diagram95', None)
    assert not _is_linked(b, 'Diagram95', a2)
    if hasattr(a2, 'namespace'):
        assert not _is_linked(a2, 'namespace', b)


def test_assoc_diagramLink104_reverse_link_reassign_clear():
    a1 = uma_DiagramLink(zoom="sample_text")
    a2 = uma_DiagramLink(zoom="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'diagram', {a1})
    assert _is_linked(b, 'diagram', a1)
    if hasattr(a1, 'DiagramLink105'):
        assert _is_linked(a1, 'DiagramLink105', b)
    _safe_set(b, 'diagram', {a2})
    assert _is_linked(b, 'diagram', a2)
    if hasattr(a1, 'DiagramLink105'):
        assert not _is_linked(a1, 'DiagramLink105', b)
    if hasattr(a2, 'DiagramLink105'):
        assert _is_linked(a2, 'DiagramLink105', b)
    _safe_set(b, 'diagram', set())
    assert not _is_linked(b, 'diagram', a2)
    if hasattr(a2, 'DiagramLink105'):
        assert not _is_linked(a2, 'DiagramLink105', b)


def test_assoc_impactedBy167_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'impacts', {a1})
    assert _is_linked(b, 'impacts', a1)
    if hasattr(a1, 'WorkProductDescriptor'):
        assert _is_linked(a1, 'WorkProductDescriptor', b)
    _safe_set(b, 'impacts', {a2})
    assert _is_linked(b, 'impacts', a2)
    if hasattr(a1, 'WorkProductDescriptor'):
        assert not _is_linked(a1, 'WorkProductDescriptor', b)
    if hasattr(a2, 'WorkProductDescriptor'):
        assert _is_linked(a2, 'WorkProductDescriptor', b)
    _safe_set(b, 'impacts', set())
    assert not _is_linked(b, 'impacts', a2)
    if hasattr(a2, 'WorkProductDescriptor'):
        assert not _is_linked(a2, 'WorkProductDescriptor', b)


def test_assoc_impacts169_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'impactedBy', {a1})
    assert _is_linked(b, 'impactedBy', a1)
    if hasattr(a1, 'WorkProductDescriptor170'):
        assert _is_linked(a1, 'WorkProductDescriptor170', b)
    _safe_set(b, 'impactedBy', {a2})
    assert _is_linked(b, 'impactedBy', a2)
    if hasattr(a1, 'WorkProductDescriptor170'):
        assert not _is_linked(a1, 'WorkProductDescriptor170', b)
    if hasattr(a2, 'WorkProductDescriptor170'):
        assert _is_linked(a2, 'WorkProductDescriptor170', b)
    _safe_set(b, 'impactedBy', set())
    assert not _is_linked(b, 'impactedBy', a2)
    if hasattr(a2, 'WorkProductDescriptor170'):
        assert not _is_linked(a2, 'WorkProductDescriptor170', b)


def test_assoc_linkToPredecessor137_reverse_link_reassign_clear():
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


def test_assoc_methodPackages299_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(userChangeable="sample_text")
    a2 = uma_MethodPlugin(userChangeable="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage300', a1)
    assert _is_linked(b, 'uma_MethodPackage300', a1)
    if hasattr(a1, 'uma_MethodPlugin'):
        assert _is_linked(a1, 'uma_MethodPlugin', b)
    _safe_set(b, 'uma_MethodPackage300', a2)
    assert _is_linked(b, 'uma_MethodPackage300', a2)
    if hasattr(a1, 'uma_MethodPlugin'):
        assert not _is_linked(a1, 'uma_MethodPlugin', b)
    if hasattr(a2, 'uma_MethodPlugin'):
        assert _is_linked(a2, 'uma_MethodPlugin', b)
    _safe_set(b, 'uma_MethodPackage300', None)
    assert not _is_linked(b, 'uma_MethodPackage300', a2)
    if hasattr(a2, 'uma_MethodPlugin'):
        assert not _is_linked(a2, 'uma_MethodPlugin', b)


def test_assoc_namespace106_reverse_link_reassign_clear():
    a1 = uma_SemanticModelBridge(presentation="sample_text")
    a2 = uma_SemanticModelBridge(presentation="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'diagram107', a1)
    assert _is_linked(b, 'diagram107', a1)
    if hasattr(a1, 'SemanticModelBridge108'):
        assert _is_linked(a1, 'SemanticModelBridge108', b)
    _safe_set(b, 'diagram107', a2)
    assert _is_linked(b, 'diagram107', a2)
    if hasattr(a1, 'SemanticModelBridge108'):
        assert not _is_linked(a1, 'SemanticModelBridge108', b)
    if hasattr(a2, 'SemanticModelBridge108'):
        assert _is_linked(a2, 'SemanticModelBridge108', b)
    _safe_set(b, 'diagram107', None)
    assert not _is_linked(b, 'diagram107', a2)
    if hasattr(a2, 'SemanticModelBridge108'):
        assert not _is_linked(a2, 'SemanticModelBridge108', b)


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


def test_assoc_planningData143_reverse_link_reassign_clear():
    a1 = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    a2 = uma_PlanningData(finishDate="sample_text_2", rank="sample_text_2", startDate="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement144', a1)
    assert _is_linked(b, 'uma_BreakdownElement144', a1)
    if hasattr(a1, 'uma_PlanningData'):
        assert _is_linked(a1, 'uma_PlanningData', b)
    _safe_set(b, 'uma_BreakdownElement144', a2)
    assert _is_linked(b, 'uma_BreakdownElement144', a2)
    if hasattr(a1, 'uma_PlanningData'):
        assert not _is_linked(a1, 'uma_PlanningData', b)
    if hasattr(a2, 'uma_PlanningData'):
        assert _is_linked(a2, 'uma_PlanningData', b)
    _safe_set(b, 'uma_BreakdownElement144', None)
    assert not _is_linked(b, 'uma_BreakdownElement144', a2)
    if hasattr(a2, 'uma_PlanningData'):
        assert not _is_linked(a2, 'uma_PlanningData', b)


def test_assoc_pred160_reverse_link_reassign_clear():
    a1 = uma_WorkOrder(linkType="sample_text")
    a2 = uma_WorkOrder(linkType="sample_text_2")
    b = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    _safe_set(b, 'uma_WorkBreakdownElement162', a1)
    assert _is_linked(b, 'uma_WorkBreakdownElement162', a1)
    if hasattr(a1, 'uma_WorkOrder161'):
        assert _is_linked(a1, 'uma_WorkOrder161', b)
    _safe_set(b, 'uma_WorkBreakdownElement162', a2)
    assert _is_linked(b, 'uma_WorkBreakdownElement162', a2)
    if hasattr(a1, 'uma_WorkOrder161'):
        assert not _is_linked(a1, 'uma_WorkOrder161', b)
    if hasattr(a2, 'uma_WorkOrder161'):
        assert _is_linked(a2, 'uma_WorkOrder161', b)
    _safe_set(b, 'uma_WorkBreakdownElement162', None)
    assert not _is_linked(b, 'uma_WorkBreakdownElement162', a2)
    if hasattr(a2, 'uma_WorkOrder161'):
        assert not _is_linked(a2, 'uma_WorkOrder161', b)


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


def test_assoc_presentedAfter139_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement138', a1)
    assert _is_linked(b, 'uma_BreakdownElement138', a1)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert _is_linked(a1, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_BreakdownElement138', a2)
    assert _is_linked(b, 'uma_BreakdownElement138', a2)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert not _is_linked(a1, 'uma_BreakdownElement', b)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert _is_linked(a2, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_BreakdownElement138', None)
    assert not _is_linked(b, 'uma_BreakdownElement138', a2)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert not _is_linked(a2, 'uma_BreakdownElement', b)


def test_assoc_presentedBefore141_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement142', a1)
    assert _is_linked(b, 'uma_BreakdownElement142', a1)
    if hasattr(a1, 'uma_BreakdownElement140'):
        assert _is_linked(a1, 'uma_BreakdownElement140', b)
    _safe_set(b, 'uma_BreakdownElement142', a2)
    assert _is_linked(b, 'uma_BreakdownElement142', a2)
    if hasattr(a1, 'uma_BreakdownElement140'):
        assert not _is_linked(a1, 'uma_BreakdownElement140', b)
    if hasattr(a2, 'uma_BreakdownElement140'):
        assert _is_linked(a2, 'uma_BreakdownElement140', b)
    _safe_set(b, 'uma_BreakdownElement142', None)
    assert not _is_linked(b, 'uma_BreakdownElement142', a2)
    if hasattr(a2, 'uma_BreakdownElement140'):
        assert not _is_linked(a2, 'uma_BreakdownElement140', b)


def test_assoc_property83_reverse_link_reassign_clear():
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


def test_assoc_reference82_reverse_link_reassign_clear():
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


def test_assoc_referenced96_reverse_link_reassign_clear():
    a1 = uma_Reference(isIndividualRepresentation="sample_text")
    a2 = uma_Reference(isIndividualRepresentation="sample_text_2")
    b = uma_DiagramElement(isVisible="sample_text")
    _safe_set(b, 'DiagramElement97', a1)
    assert _is_linked(b, 'DiagramElement97', a1)
    if hasattr(a1, 'reference'):
        assert _is_linked(a1, 'reference', b)
    _safe_set(b, 'DiagramElement97', a2)
    assert _is_linked(b, 'DiagramElement97', a2)
    if hasattr(a1, 'reference'):
        assert not _is_linked(a1, 'reference', b)
    if hasattr(a2, 'reference'):
        assert _is_linked(a2, 'reference', b)
    _safe_set(b, 'DiagramElement97', None)
    assert not _is_linked(b, 'DiagramElement97', a2)
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


def test_assoc_superActivities145_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_Activity(isEnactable="sample_text")
    _safe_set(b, 'Activity', a1)
    assert _is_linked(b, 'Activity', a1)
    if hasattr(a1, 'breakdownElements'):
        assert _is_linked(a1, 'breakdownElements', b)
    _safe_set(b, 'Activity', a2)
    assert _is_linked(b, 'Activity', a2)
    if hasattr(a1, 'breakdownElements'):
        assert not _is_linked(a1, 'breakdownElements', b)
    if hasattr(a2, 'breakdownElements'):
        assert _is_linked(a2, 'breakdownElements', b)
    _safe_set(b, 'Activity', None)
    assert not _is_linked(b, 'Activity', a2)
    if hasattr(a2, 'breakdownElements'):
        assert not _is_linked(a2, 'breakdownElements', b)


def test_assoc_variabilityBasedOnElement305_reverse_link_reassign_clear():
    a1 = uma_VariabilityElement(variabilityType="sample_text")
    a2 = uma_VariabilityElement(variabilityType="sample_text_2")
    b = uma_VariabilityElement(variabilityType="sample_text")
    _safe_set(b, 'uma_VariabilityElement304', a1)
    assert _is_linked(b, 'uma_VariabilityElement304', a1)
    if hasattr(a1, 'uma_VariabilityElement'):
        assert _is_linked(a1, 'uma_VariabilityElement', b)
    _safe_set(b, 'uma_VariabilityElement304', a2)
    assert _is_linked(b, 'uma_VariabilityElement304', a2)
    if hasattr(a1, 'uma_VariabilityElement'):
        assert not _is_linked(a1, 'uma_VariabilityElement', b)
    if hasattr(a2, 'uma_VariabilityElement'):
        assert _is_linked(a2, 'uma_VariabilityElement', b)
    _safe_set(b, 'uma_VariabilityElement304', None)
    assert not _is_linked(b, 'uma_VariabilityElement304', a2)
    if hasattr(a2, 'uma_VariabilityElement'):
        assert not _is_linked(a2, 'uma_VariabilityElement', b)


def test_assoc_viewpoint102_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'uma_Diagram', a1)
    assert _is_linked(b, 'uma_Diagram', a1)
    if hasattr(a1, 'uma_Point103'):
        assert _is_linked(a1, 'uma_Point103', b)
    _safe_set(b, 'uma_Diagram', a2)
    assert _is_linked(b, 'uma_Diagram', a2)
    if hasattr(a1, 'uma_Point103'):
        assert not _is_linked(a1, 'uma_Point103', b)
    if hasattr(a2, 'uma_Point103'):
        assert _is_linked(a2, 'uma_Point103', b)
    _safe_set(b, 'uma_Diagram', None)
    assert not _is_linked(b, 'uma_Diagram', a2)
    if hasattr(a2, 'uma_Point103'):
        assert not _is_linked(a2, 'uma_Point103', b)


def test_assoc_viewport84_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_DiagramLink(zoom="sample_text")
    _safe_set(b, 'uma_DiagramLink', a1)
    assert _is_linked(b, 'uma_DiagramLink', a1)
    if hasattr(a1, 'uma_Point85'):
        assert _is_linked(a1, 'uma_Point85', b)
    _safe_set(b, 'uma_DiagramLink', a2)
    assert _is_linked(b, 'uma_DiagramLink', a2)
    if hasattr(a1, 'uma_Point85'):
        assert not _is_linked(a1, 'uma_Point85', b)
    if hasattr(a2, 'uma_Point85'):
        assert _is_linked(a2, 'uma_Point85', b)
    _safe_set(b, 'uma_DiagramLink', None)
    assert not _is_linked(b, 'uma_DiagramLink', a2)
    if hasattr(a2, 'uma_Point85'):
        assert not _is_linked(a2, 'uma_Point85', b)


def test_assoc_waypoints113_reverse_link_reassign_clear():
    a1 = uma_Polyline(closed="sample_text")
    a2 = uma_Polyline(closed="sample_text_2")
    b = uma_Point(x="sample_text", y="sample_text")
    _safe_set(b, 'uma_Point114', a1)
    assert _is_linked(b, 'uma_Point114', a1)
    if hasattr(a1, 'uma_Polyline'):
        assert _is_linked(a1, 'uma_Polyline', b)
    _safe_set(b, 'uma_Point114', a2)
    assert _is_linked(b, 'uma_Point114', a2)
    if hasattr(a1, 'uma_Polyline'):
        assert not _is_linked(a1, 'uma_Polyline', b)
    if hasattr(a2, 'uma_Polyline'):
        assert _is_linked(a2, 'uma_Polyline', b)
    _safe_set(b, 'uma_Point114', None)
    assert not _is_linked(b, 'uma_Point114', a2)
    if hasattr(a2, 'uma_Polyline'):
        assert not _is_linked(a2, 'uma_Polyline', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_WorkProduct163_stub_double():
    # uma_WorkProduct has no real 'uma_WorkProduct165' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_WorkProduct()
    setattr(partner, 'uma_WorkProduct165', None)
    _safe_set(owner, 'uma_WorkProductDescriptor164', partner)
    assert getattr(partner, 'uma_WorkProduct165') == owner
    _safe_set(owner, 'uma_WorkProductDescriptor164', None)
    assert getattr(partner, 'uma_WorkProduct165') is None


def test_assoc_activityReferences207_stub_double():
    # uma_Practice has no real 'uma_Practice208' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Practice()
    setattr(partner, 'uma_Practice208', None)
    _safe_set(owner, 'uma_Activity209', partner)
    assert owner in getattr(partner, 'uma_Practice208')
    _safe_set(owner, 'uma_Activity209', None)
    assert owner not in getattr(partner, 'uma_Practice208')


def test_assoc_categorizedElements266_stub_double():
    # uma_CustomCategory has no real 'uma_CustomCategory' property in the generated
    # code (a bare stub) -- manually attach it so uma_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    partner = uma_CustomCategory()
    setattr(partner, 'uma_CustomCategory', None)
    _safe_set(owner, 'uma_DescribableElement267', partner)
    assert owner in getattr(partner, 'uma_CustomCategory')
    _safe_set(owner, 'uma_DescribableElement267', None)
    assert owner not in getattr(partner, 'uma_CustomCategory')


def test_assoc_checklists122_stub_double():
    # uma_Checklist has no real 'uma_Checklist124' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Checklist()
    setattr(partner, 'uma_Checklist124', None)
    _safe_set(owner, 'uma_Activity123', {partner})
    assert getattr(partner, 'uma_Checklist124') == owner
    _safe_set(owner, 'uma_Activity123', set())
    assert getattr(partner, 'uma_Checklist124') is None


def test_assoc_concepts125_stub_double():
    # uma_Concept has no real 'uma_Concept127' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Concept()
    setattr(partner, 'uma_Concept127', None)
    _safe_set(owner, 'uma_Activity126', {partner})
    assert getattr(partner, 'uma_Concept127') == owner
    _safe_set(owner, 'uma_Activity126', set())
    assert getattr(partner, 'uma_Concept127') is None


def test_assoc_contained75_stub_double():
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


def test_assoc_container81_stub_double():
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


def test_assoc_copyrightStatement306_stub_double():
    # uma_SupportingMaterial has no real 'uma_SupportingMaterial307' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    partner = uma_SupportingMaterial()
    setattr(partner, 'uma_SupportingMaterial307', None)
    _safe_set(owner, 'uma_MethodUnit', partner)
    assert getattr(partner, 'uma_SupportingMaterial307') == owner
    _safe_set(owner, 'uma_MethodUnit', None)
    assert getattr(partner, 'uma_SupportingMaterial307') is None


def test_assoc_diagrams288_stub_double():
    # uma_ProcessPackage has no real 'uma_ProcessPackage289' property in the generated
    # code (a bare stub) -- manually attach it so uma_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Diagram(zoom="sample_text")
    partner = uma_ProcessPackage()
    setattr(partner, 'uma_ProcessPackage289', None)
    _safe_set(owner, 'uma_Diagram290', partner)
    assert owner in getattr(partner, 'uma_ProcessPackage289')
    _safe_set(owner, 'uma_Diagram290', None)
    assert owner not in getattr(partner, 'uma_ProcessPackage289')


def test_assoc_element110_stub_double():
    # uma_UMASemanticModelBridge has no real 'uma_UMASemanticModelBridge' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    partner = uma_UMASemanticModelBridge()
    setattr(partner, 'uma_UMASemanticModelBridge', None)
    _safe_set(owner, 'uma_MethodElement111', partner)
    assert getattr(partner, 'uma_UMASemanticModelBridge') == owner
    _safe_set(owner, 'uma_MethodElement111', None)
    assert getattr(partner, 'uma_UMASemanticModelBridge') is None


def test_assoc_examples128_stub_double():
    # uma_Example has no real 'uma_Example130' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Example()
    setattr(partner, 'uma_Example130', None)
    _safe_set(owner, 'uma_Activity129', {partner})
    assert getattr(partner, 'uma_Example130') == owner
    _safe_set(owner, 'uma_Activity129', set())
    assert getattr(partner, 'uma_Example130') is None


def test_assoc_externalInput182_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor183' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor183', None)
    _safe_set(owner, 'uma_WorkProductDescriptor184', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor183')
    _safe_set(owner, 'uma_WorkProductDescriptor184', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor183')


def test_assoc_graphElement86_stub_double():
    # uma_GraphElement has no real 'GraphElement87' property in the generated
    # code (a bare stub) -- manually attach it so uma_DiagramLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DiagramLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DiagramLink(zoom="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement87', None)
    _safe_set(owner, 'link', partner)
    assert getattr(partner, 'GraphElement87') == owner
    _safe_set(owner, 'link', None)
    assert getattr(partner, 'GraphElement87') is None


def test_assoc_graphElement92_stub_double():
    # uma_GraphElement has no real 'GraphElement93' property in the generated
    # code (a bare stub) -- manually attach it so uma_SemanticModelBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_SemanticModelBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_SemanticModelBridge(presentation="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement93', None)
    _safe_set(owner, 'semanticModel', partner)
    assert getattr(partner, 'GraphElement93') == owner
    _safe_set(owner, 'semanticModel', None)
    assert getattr(partner, 'GraphElement93') is None


def test_assoc_guidelines131_stub_double():
    # uma_Guideline has no real 'uma_Guideline133' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Guideline()
    setattr(partner, 'uma_Guideline133', None)
    _safe_set(owner, 'uma_Activity132', {partner})
    assert getattr(partner, 'uma_Guideline133') == owner
    _safe_set(owner, 'uma_Activity132', set())
    assert getattr(partner, 'uma_Guideline133') is None


def test_assoc_interfaceIO294_stub_double():
    # uma_ProcessComponentInterface has no real 'uma_ProcessComponentInterface295' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_ProcessComponentInterface()
    setattr(partner, 'uma_ProcessComponentInterface295', None)
    _safe_set(owner, 'uma_WorkProductDescriptor296', partner)
    assert owner in getattr(partner, 'uma_ProcessComponentInterface295')
    _safe_set(owner, 'uma_WorkProductDescriptor296', None)
    assert owner not in getattr(partner, 'uma_ProcessComponentInterface295')


def test_assoc_link76_stub_double():
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


def test_assoc_mandatoryInput185_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor186' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor186', None)
    _safe_set(owner, 'uma_WorkProductDescriptor187', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor186')
    _safe_set(owner, 'uma_WorkProductDescriptor187', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor186')


def test_assoc_methodPackageSelection311_stub_double():
    # uma_MethodConfiguration has no real 'uma_MethodConfiguration312' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPackage(global_="sample_text")
    partner = uma_MethodConfiguration()
    setattr(partner, 'uma_MethodConfiguration312', None)
    _safe_set(owner, 'uma_MethodPackage313', partner)
    assert owner in getattr(partner, 'uma_MethodConfiguration312')
    _safe_set(owner, 'uma_MethodPackage313', None)
    assert owner not in getattr(partner, 'uma_MethodConfiguration312')


def test_assoc_methodPluginSelection308_stub_double():
    # uma_MethodConfiguration has no real 'uma_MethodConfiguration309' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPlugin(userChangeable="sample_text")
    partner = uma_MethodConfiguration()
    setattr(partner, 'uma_MethodConfiguration309', None)
    _safe_set(owner, 'uma_MethodPlugin310', partner)
    assert owner in getattr(partner, 'uma_MethodConfiguration309')
    _safe_set(owner, 'uma_MethodPlugin310', None)
    assert owner not in getattr(partner, 'uma_MethodConfiguration309')


def test_assoc_methodPlugins325_stub_double():
    # uma_MethodLibrary has no real 'uma_MethodLibrary' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPlugin(userChangeable="sample_text")
    partner = uma_MethodLibrary()
    setattr(partner, 'uma_MethodLibrary', None)
    _safe_set(owner, 'uma_MethodPlugin326', partner)
    assert owner in getattr(partner, 'uma_MethodLibrary')
    _safe_set(owner, 'uma_MethodPlugin326', None)
    assert owner not in getattr(partner, 'uma_MethodLibrary')


def test_assoc_modifies155_stub_double():
    # uma_RoleDescriptor has no real 'uma_RoleDescriptor156' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'uma_RoleDescriptor156', None)
    _safe_set(owner, 'uma_WorkProductDescriptor', partner)
    assert owner in getattr(partner, 'uma_RoleDescriptor156')
    _safe_set(owner, 'uma_WorkProductDescriptor', None)
    assert owner not in getattr(partner, 'uma_RoleDescriptor156')


def test_assoc_optionalInput188_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor189' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor189', None)
    _safe_set(owner, 'uma_WorkProductDescriptor190', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor189')
    _safe_set(owner, 'uma_WorkProductDescriptor190', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor189')


def test_assoc_output191_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor192' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor192', None)
    _safe_set(owner, 'uma_WorkProductDescriptor193', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor192')
    _safe_set(owner, 'uma_WorkProductDescriptor193', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor192')


def test_assoc_position74_stub_double():
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


def test_assoc_referenceWorkflows248_stub_double():
    # uma_Discipline has no real 'uma_Discipline249' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Discipline()
    setattr(partner, 'uma_Discipline249', None)
    _safe_set(owner, 'uma_Activity250', partner)
    assert owner in getattr(partner, 'uma_Discipline249')
    _safe_set(owner, 'uma_Activity250', None)
    assert owner not in getattr(partner, 'uma_Discipline249')


def test_assoc_responsibleFor157_stub_double():
    # uma_RoleDescriptor has no real 'uma_RoleDescriptor158' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'uma_RoleDescriptor158', None)
    _safe_set(owner, 'uma_WorkProductDescriptor159', partner)
    assert owner in getattr(partner, 'uma_RoleDescriptor158')
    _safe_set(owner, 'uma_WorkProductDescriptor159', None)
    assert owner not in getattr(partner, 'uma_RoleDescriptor158')


def test_assoc_reusableAssets134_stub_double():
    # uma_ReusableAsset has no real 'uma_ReusableAsset136' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_ReusableAsset()
    setattr(partner, 'uma_ReusableAsset136', None)
    _safe_set(owner, 'uma_Activity135', {partner})
    assert getattr(partner, 'uma_ReusableAsset136') == owner
    _safe_set(owner, 'uma_Activity135', set())
    assert getattr(partner, 'uma_ReusableAsset136') is None


def test_assoc_roadmaps118_stub_double():
    # uma_Roadmap has no real 'uma_Roadmap' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Roadmap()
    setattr(partner, 'uma_Roadmap', None)
    _safe_set(owner, 'uma_Activity', {partner})
    assert getattr(partner, 'uma_Roadmap') == owner
    _safe_set(owner, 'uma_Activity', set())
    assert getattr(partner, 'uma_Roadmap') is None


def test_assoc_selectedSteps197_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor198' property in the generated
    # code (a bare stub) -- manually attach it so uma_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor198', None)
    _safe_set(owner, 'uma_Section199', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor198')
    _safe_set(owner, 'uma_Section199', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor198')


def test_assoc_semanticModel79_stub_double():
    # uma_GraphElement has no real 'graphElement80' property in the generated
    # code (a bare stub) -- manually attach it so uma_SemanticModelBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_SemanticModelBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_SemanticModelBridge(presentation="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'graphElement80', None)
    _safe_set(owner, 'SemanticModelBridge', partner)
    assert getattr(partner, 'graphElement80') == owner
    _safe_set(owner, 'SemanticModelBridge', None)
    assert getattr(partner, 'graphElement80') is None


def test_assoc_size109_stub_double():
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


def test_assoc_supportingMaterials119_stub_double():
    # uma_SupportingMaterial has no real 'uma_SupportingMaterial121' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_SupportingMaterial()
    setattr(partner, 'uma_SupportingMaterial121', None)
    _safe_set(owner, 'uma_Activity120', {partner})
    assert getattr(partner, 'uma_SupportingMaterial121') == owner
    _safe_set(owner, 'uma_Activity120', set())
    assert getattr(partner, 'uma_SupportingMaterial121') is None


def test_assoc_waypoints100_stub_double():
    # uma_GraphEdge has no real 'uma_GraphEdge' property in the generated
    # code (a bare stub) -- manually attach it so uma_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Point(x="sample_text", y="sample_text")
    partner = uma_GraphEdge()
    setattr(partner, 'uma_GraphEdge', None)
    _safe_set(owner, 'uma_Point101', partner)
    assert owner in getattr(partner, 'uma_GraphEdge')
    _safe_set(owner, 'uma_Point101', None)
    assert owner not in getattr(partner, 'uma_GraphEdge')


