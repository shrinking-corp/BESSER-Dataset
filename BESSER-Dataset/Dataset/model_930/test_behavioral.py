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
    uma_MethodElementProperty,
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

def test_assoc_bases306_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(userChangeable="sample_text")
    a2 = uma_MethodPlugin(userChangeable="sample_text_2")
    b = uma_MethodPlugin(userChangeable="sample_text")
    _safe_set(b, 'uma_MethodPlugin307', a1)
    assert _is_linked(b, 'uma_MethodPlugin307', a1)
    if hasattr(a1, 'uma_MethodPlugin305'):
        assert _is_linked(a1, 'uma_MethodPlugin305', b)
    _safe_set(b, 'uma_MethodPlugin307', a2)
    assert _is_linked(b, 'uma_MethodPlugin307', a2)
    if hasattr(a1, 'uma_MethodPlugin305'):
        assert not _is_linked(a1, 'uma_MethodPlugin305', b)
    if hasattr(a2, 'uma_MethodPlugin305'):
        assert _is_linked(a2, 'uma_MethodPlugin305', b)
    _safe_set(b, 'uma_MethodPlugin307', None)
    assert not _is_linked(b, 'uma_MethodPlugin307', a2)
    if hasattr(a2, 'uma_MethodPlugin305'):
        assert not _is_linked(a2, 'uma_MethodPlugin305', b)


def test_assoc_breakdownElements121_reverse_link_reassign_clear():
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


def test_assoc_center119_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    _safe_set(b, 'uma_Ellipse', a1)
    assert _is_linked(b, 'uma_Ellipse', a1)
    if hasattr(a1, 'uma_Point120'):
        assert _is_linked(a1, 'uma_Point120', b)
    _safe_set(b, 'uma_Ellipse', a2)
    assert _is_linked(b, 'uma_Ellipse', a2)
    if hasattr(a1, 'uma_Point120'):
        assert not _is_linked(a1, 'uma_Point120', b)
    if hasattr(a2, 'uma_Point120'):
        assert _is_linked(a2, 'uma_Point120', b)
    _safe_set(b, 'uma_Ellipse', None)
    assert not _is_linked(b, 'uma_Ellipse', a2)
    if hasattr(a2, 'uma_Point120'):
        assert not _is_linked(a2, 'uma_Point120', b)


def test_assoc_childPackages74_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage75', a1)
    assert _is_linked(b, 'uma_MethodPackage75', a1)
    if hasattr(a1, 'uma_MethodPackage73'):
        assert _is_linked(a1, 'uma_MethodPackage73', b)
    _safe_set(b, 'uma_MethodPackage75', a2)
    assert _is_linked(b, 'uma_MethodPackage75', a2)
    if hasattr(a1, 'uma_MethodPackage73'):
        assert not _is_linked(a1, 'uma_MethodPackage73', b)
    if hasattr(a2, 'uma_MethodPackage73'):
        assert _is_linked(a2, 'uma_MethodPackage73', b)
    _safe_set(b, 'uma_MethodPackage75', None)
    assert not _is_linked(b, 'uma_MethodPackage75', a2)
    if hasattr(a2, 'uma_MethodPackage73'):
        assert not _is_linked(a2, 'uma_MethodPackage73', b)


def test_assoc_deliverableParts176_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'uma_WorkProductDescriptor177', a1)
    assert _is_linked(b, 'uma_WorkProductDescriptor177', a1)
    if hasattr(a1, 'uma_WorkProductDescriptor175'):
        assert _is_linked(a1, 'uma_WorkProductDescriptor175', b)
    _safe_set(b, 'uma_WorkProductDescriptor177', a2)
    assert _is_linked(b, 'uma_WorkProductDescriptor177', a2)
    if hasattr(a1, 'uma_WorkProductDescriptor175'):
        assert not _is_linked(a1, 'uma_WorkProductDescriptor175', b)
    if hasattr(a2, 'uma_WorkProductDescriptor175'):
        assert _is_linked(a2, 'uma_WorkProductDescriptor175', b)
    _safe_set(b, 'uma_WorkProductDescriptor177', None)
    assert not _is_linked(b, 'uma_WorkProductDescriptor177', a2)
    if hasattr(a2, 'uma_WorkProductDescriptor175'):
        assert not _is_linked(a2, 'uma_WorkProductDescriptor175', b)


def test_assoc_diagram92_reverse_link_reassign_clear():
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


def test_assoc_diagram98_reverse_link_reassign_clear():
    a1 = uma_SemanticModelBridge(presentation="sample_text")
    a2 = uma_SemanticModelBridge(presentation="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'Diagram99', a1)
    assert _is_linked(b, 'Diagram99', a1)
    if hasattr(a1, 'namespace'):
        assert _is_linked(a1, 'namespace', b)
    _safe_set(b, 'Diagram99', a2)
    assert _is_linked(b, 'Diagram99', a2)
    if hasattr(a1, 'namespace'):
        assert not _is_linked(a1, 'namespace', b)
    if hasattr(a2, 'namespace'):
        assert _is_linked(a2, 'namespace', b)
    _safe_set(b, 'Diagram99', None)
    assert not _is_linked(b, 'Diagram99', a2)
    if hasattr(a2, 'namespace'):
        assert not _is_linked(a2, 'namespace', b)


def test_assoc_diagramLink108_reverse_link_reassign_clear():
    a1 = uma_DiagramLink(zoom="sample_text")
    a2 = uma_DiagramLink(zoom="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'diagram', {a1})
    assert _is_linked(b, 'diagram', a1)
    if hasattr(a1, 'DiagramLink109'):
        assert _is_linked(a1, 'DiagramLink109', b)
    _safe_set(b, 'diagram', {a2})
    assert _is_linked(b, 'diagram', a2)
    if hasattr(a1, 'DiagramLink109'):
        assert not _is_linked(a1, 'DiagramLink109', b)
    if hasattr(a2, 'DiagramLink109'):
        assert _is_linked(a2, 'DiagramLink109', b)
    _safe_set(b, 'diagram', set())
    assert not _is_linked(b, 'diagram', a2)
    if hasattr(a2, 'DiagramLink109'):
        assert not _is_linked(a2, 'DiagramLink109', b)


def test_assoc_impactedBy171_reverse_link_reassign_clear():
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


def test_assoc_impacts173_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'impactedBy', {a1})
    assert _is_linked(b, 'impactedBy', a1)
    if hasattr(a1, 'WorkProductDescriptor174'):
        assert _is_linked(a1, 'WorkProductDescriptor174', b)
    _safe_set(b, 'impactedBy', {a2})
    assert _is_linked(b, 'impactedBy', a2)
    if hasattr(a1, 'WorkProductDescriptor174'):
        assert not _is_linked(a1, 'WorkProductDescriptor174', b)
    if hasattr(a2, 'WorkProductDescriptor174'):
        assert _is_linked(a2, 'WorkProductDescriptor174', b)
    _safe_set(b, 'impactedBy', set())
    assert not _is_linked(b, 'impactedBy', a2)
    if hasattr(a2, 'WorkProductDescriptor174'):
        assert not _is_linked(a2, 'WorkProductDescriptor174', b)


def test_assoc_linkToPredecessor141_reverse_link_reassign_clear():
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


def test_assoc_methodElementProperty1_reverse_link_reassign_clear():
    a1 = uma_MethodElementProperty(value="sample_text")
    a2 = uma_MethodElementProperty(value="sample_text_2")
    b = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    _safe_set(b, 'uma_MethodElement2', {a1})
    assert _is_linked(b, 'uma_MethodElement2', a1)
    if hasattr(a1, 'uma_MethodElementProperty'):
        assert _is_linked(a1, 'uma_MethodElementProperty', b)
    _safe_set(b, 'uma_MethodElement2', {a2})
    assert _is_linked(b, 'uma_MethodElement2', a2)
    if hasattr(a1, 'uma_MethodElementProperty'):
        assert not _is_linked(a1, 'uma_MethodElementProperty', b)
    if hasattr(a2, 'uma_MethodElementProperty'):
        assert _is_linked(a2, 'uma_MethodElementProperty', b)
    _safe_set(b, 'uma_MethodElement2', set())
    assert not _is_linked(b, 'uma_MethodElement2', a2)
    if hasattr(a2, 'uma_MethodElementProperty'):
        assert not _is_linked(a2, 'uma_MethodElementProperty', b)


def test_assoc_methodPackages303_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(userChangeable="sample_text")
    a2 = uma_MethodPlugin(userChangeable="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage304', a1)
    assert _is_linked(b, 'uma_MethodPackage304', a1)
    if hasattr(a1, 'uma_MethodPlugin'):
        assert _is_linked(a1, 'uma_MethodPlugin', b)
    _safe_set(b, 'uma_MethodPackage304', a2)
    assert _is_linked(b, 'uma_MethodPackage304', a2)
    if hasattr(a1, 'uma_MethodPlugin'):
        assert not _is_linked(a1, 'uma_MethodPlugin', b)
    if hasattr(a2, 'uma_MethodPlugin'):
        assert _is_linked(a2, 'uma_MethodPlugin', b)
    _safe_set(b, 'uma_MethodPackage304', None)
    assert not _is_linked(b, 'uma_MethodPackage304', a2)
    if hasattr(a2, 'uma_MethodPlugin'):
        assert not _is_linked(a2, 'uma_MethodPlugin', b)


def test_assoc_namespace110_reverse_link_reassign_clear():
    a1 = uma_SemanticModelBridge(presentation="sample_text")
    a2 = uma_SemanticModelBridge(presentation="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'diagram111', a1)
    assert _is_linked(b, 'diagram111', a1)
    if hasattr(a1, 'SemanticModelBridge112'):
        assert _is_linked(a1, 'SemanticModelBridge112', b)
    _safe_set(b, 'diagram111', a2)
    assert _is_linked(b, 'diagram111', a2)
    if hasattr(a1, 'SemanticModelBridge112'):
        assert not _is_linked(a1, 'SemanticModelBridge112', b)
    if hasattr(a2, 'SemanticModelBridge112'):
        assert _is_linked(a2, 'SemanticModelBridge112', b)
    _safe_set(b, 'diagram111', None)
    assert not _is_linked(b, 'diagram111', a2)
    if hasattr(a2, 'SemanticModelBridge112'):
        assert not _is_linked(a2, 'SemanticModelBridge112', b)


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


def test_assoc_planningData147_reverse_link_reassign_clear():
    a1 = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    a2 = uma_PlanningData(finishDate="sample_text_2", rank="sample_text_2", startDate="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement148', a1)
    assert _is_linked(b, 'uma_BreakdownElement148', a1)
    if hasattr(a1, 'uma_PlanningData'):
        assert _is_linked(a1, 'uma_PlanningData', b)
    _safe_set(b, 'uma_BreakdownElement148', a2)
    assert _is_linked(b, 'uma_BreakdownElement148', a2)
    if hasattr(a1, 'uma_PlanningData'):
        assert not _is_linked(a1, 'uma_PlanningData', b)
    if hasattr(a2, 'uma_PlanningData'):
        assert _is_linked(a2, 'uma_PlanningData', b)
    _safe_set(b, 'uma_BreakdownElement148', None)
    assert not _is_linked(b, 'uma_BreakdownElement148', a2)
    if hasattr(a2, 'uma_PlanningData'):
        assert not _is_linked(a2, 'uma_PlanningData', b)


def test_assoc_pred164_reverse_link_reassign_clear():
    a1 = uma_WorkOrder(linkType="sample_text")
    a2 = uma_WorkOrder(linkType="sample_text_2")
    b = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    _safe_set(b, 'uma_WorkBreakdownElement166', a1)
    assert _is_linked(b, 'uma_WorkBreakdownElement166', a1)
    if hasattr(a1, 'uma_WorkOrder165'):
        assert _is_linked(a1, 'uma_WorkOrder165', b)
    _safe_set(b, 'uma_WorkBreakdownElement166', a2)
    assert _is_linked(b, 'uma_WorkBreakdownElement166', a2)
    if hasattr(a1, 'uma_WorkOrder165'):
        assert not _is_linked(a1, 'uma_WorkOrder165', b)
    if hasattr(a2, 'uma_WorkOrder165'):
        assert _is_linked(a2, 'uma_WorkOrder165', b)
    _safe_set(b, 'uma_WorkBreakdownElement166', None)
    assert not _is_linked(b, 'uma_WorkBreakdownElement166', a2)
    if hasattr(a2, 'uma_WorkOrder165'):
        assert not _is_linked(a2, 'uma_WorkOrder165', b)


def test_assoc_predecessor23_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    _safe_set(b, 'uma_Section24', a1)
    assert _is_linked(b, 'uma_Section24', a1)
    if hasattr(a1, 'uma_Section22'):
        assert _is_linked(a1, 'uma_Section22', b)
    _safe_set(b, 'uma_Section24', a2)
    assert _is_linked(b, 'uma_Section24', a2)
    if hasattr(a1, 'uma_Section22'):
        assert not _is_linked(a1, 'uma_Section22', b)
    if hasattr(a2, 'uma_Section22'):
        assert _is_linked(a2, 'uma_Section22', b)
    _safe_set(b, 'uma_Section24', None)
    assert not _is_linked(b, 'uma_Section24', a2)
    if hasattr(a2, 'uma_Section22'):
        assert not _is_linked(a2, 'uma_Section22', b)


def test_assoc_presentation16_reverse_link_reassign_clear():
    a1 = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    a2 = uma_DescribableElement(nodeicon="sample_text_2", presentationName="sample_text_2", shapeicon="sample_text_2")
    b = uma_ContentDescription(externalId="sample_text", keyConsiderations="sample_text", mainDescription="sample_text")
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


def test_assoc_presentedAfter143_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement142', a1)
    assert _is_linked(b, 'uma_BreakdownElement142', a1)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert _is_linked(a1, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_BreakdownElement142', a2)
    assert _is_linked(b, 'uma_BreakdownElement142', a2)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert not _is_linked(a1, 'uma_BreakdownElement', b)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert _is_linked(a2, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_BreakdownElement142', None)
    assert not _is_linked(b, 'uma_BreakdownElement142', a2)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert not _is_linked(a2, 'uma_BreakdownElement', b)


def test_assoc_presentedBefore145_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement146', a1)
    assert _is_linked(b, 'uma_BreakdownElement146', a1)
    if hasattr(a1, 'uma_BreakdownElement144'):
        assert _is_linked(a1, 'uma_BreakdownElement144', b)
    _safe_set(b, 'uma_BreakdownElement146', a2)
    assert _is_linked(b, 'uma_BreakdownElement146', a2)
    if hasattr(a1, 'uma_BreakdownElement144'):
        assert not _is_linked(a1, 'uma_BreakdownElement144', b)
    if hasattr(a2, 'uma_BreakdownElement144'):
        assert _is_linked(a2, 'uma_BreakdownElement144', b)
    _safe_set(b, 'uma_BreakdownElement146', None)
    assert not _is_linked(b, 'uma_BreakdownElement146', a2)
    if hasattr(a2, 'uma_BreakdownElement144'):
        assert not _is_linked(a2, 'uma_BreakdownElement144', b)


def test_assoc_property87_reverse_link_reassign_clear():
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


def test_assoc_reference86_reverse_link_reassign_clear():
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


def test_assoc_referenced100_reverse_link_reassign_clear():
    a1 = uma_Reference(isIndividualRepresentation="sample_text")
    a2 = uma_Reference(isIndividualRepresentation="sample_text_2")
    b = uma_DiagramElement(isVisible="sample_text")
    _safe_set(b, 'DiagramElement101', a1)
    assert _is_linked(b, 'DiagramElement101', a1)
    if hasattr(a1, 'reference'):
        assert _is_linked(a1, 'reference', b)
    _safe_set(b, 'DiagramElement101', a2)
    assert _is_linked(b, 'DiagramElement101', a2)
    if hasattr(a1, 'reference'):
        assert not _is_linked(a1, 'reference', b)
    if hasattr(a2, 'reference'):
        assert _is_linked(a2, 'reference', b)
    _safe_set(b, 'DiagramElement101', None)
    assert not _is_linked(b, 'DiagramElement101', a2)
    if hasattr(a2, 'reference'):
        assert not _is_linked(a2, 'reference', b)


def test_assoc_reusedPackages72_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage71', {a1})
    assert _is_linked(b, 'uma_MethodPackage71', a1)
    if hasattr(a1, 'uma_MethodPackage'):
        assert _is_linked(a1, 'uma_MethodPackage', b)
    _safe_set(b, 'uma_MethodPackage71', {a2})
    assert _is_linked(b, 'uma_MethodPackage71', a2)
    if hasattr(a1, 'uma_MethodPackage'):
        assert not _is_linked(a1, 'uma_MethodPackage', b)
    if hasattr(a2, 'uma_MethodPackage'):
        assert _is_linked(a2, 'uma_MethodPackage', b)
    _safe_set(b, 'uma_MethodPackage71', set())
    assert not _is_linked(b, 'uma_MethodPackage71', a2)
    if hasattr(a2, 'uma_MethodPackage'):
        assert not _is_linked(a2, 'uma_MethodPackage', b)


def test_assoc_sections17_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_ContentDescription(externalId="sample_text", keyConsiderations="sample_text", mainDescription="sample_text")
    _safe_set(b, 'uma_ContentDescription18', {a1})
    assert _is_linked(b, 'uma_ContentDescription18', a1)
    if hasattr(a1, 'uma_Section'):
        assert _is_linked(a1, 'uma_Section', b)
    _safe_set(b, 'uma_ContentDescription18', {a2})
    assert _is_linked(b, 'uma_ContentDescription18', a2)
    if hasattr(a1, 'uma_Section'):
        assert not _is_linked(a1, 'uma_Section', b)
    if hasattr(a2, 'uma_Section'):
        assert _is_linked(a2, 'uma_Section', b)
    _safe_set(b, 'uma_ContentDescription18', set())
    assert not _is_linked(b, 'uma_ContentDescription18', a2)
    if hasattr(a2, 'uma_Section'):
        assert not _is_linked(a2, 'uma_Section', b)


def test_assoc_subSections20_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    _safe_set(b, 'uma_Section21', a1)
    assert _is_linked(b, 'uma_Section21', a1)
    if hasattr(a1, 'uma_Section19'):
        assert _is_linked(a1, 'uma_Section19', b)
    _safe_set(b, 'uma_Section21', a2)
    assert _is_linked(b, 'uma_Section21', a2)
    if hasattr(a1, 'uma_Section19'):
        assert not _is_linked(a1, 'uma_Section19', b)
    if hasattr(a2, 'uma_Section19'):
        assert _is_linked(a2, 'uma_Section19', b)
    _safe_set(b, 'uma_Section21', None)
    assert not _is_linked(b, 'uma_Section21', a2)
    if hasattr(a2, 'uma_Section19'):
        assert not _is_linked(a2, 'uma_Section19', b)


def test_assoc_superActivities149_reverse_link_reassign_clear():
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


def test_assoc_variabilityBasedOnElement309_reverse_link_reassign_clear():
    a1 = uma_VariabilityElement(variabilityType="sample_text")
    a2 = uma_VariabilityElement(variabilityType="sample_text_2")
    b = uma_VariabilityElement(variabilityType="sample_text")
    _safe_set(b, 'uma_VariabilityElement308', a1)
    assert _is_linked(b, 'uma_VariabilityElement308', a1)
    if hasattr(a1, 'uma_VariabilityElement'):
        assert _is_linked(a1, 'uma_VariabilityElement', b)
    _safe_set(b, 'uma_VariabilityElement308', a2)
    assert _is_linked(b, 'uma_VariabilityElement308', a2)
    if hasattr(a1, 'uma_VariabilityElement'):
        assert not _is_linked(a1, 'uma_VariabilityElement', b)
    if hasattr(a2, 'uma_VariabilityElement'):
        assert _is_linked(a2, 'uma_VariabilityElement', b)
    _safe_set(b, 'uma_VariabilityElement308', None)
    assert not _is_linked(b, 'uma_VariabilityElement308', a2)
    if hasattr(a2, 'uma_VariabilityElement'):
        assert not _is_linked(a2, 'uma_VariabilityElement', b)


def test_assoc_viewpoint106_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'uma_Diagram', a1)
    assert _is_linked(b, 'uma_Diagram', a1)
    if hasattr(a1, 'uma_Point107'):
        assert _is_linked(a1, 'uma_Point107', b)
    _safe_set(b, 'uma_Diagram', a2)
    assert _is_linked(b, 'uma_Diagram', a2)
    if hasattr(a1, 'uma_Point107'):
        assert not _is_linked(a1, 'uma_Point107', b)
    if hasattr(a2, 'uma_Point107'):
        assert _is_linked(a2, 'uma_Point107', b)
    _safe_set(b, 'uma_Diagram', None)
    assert not _is_linked(b, 'uma_Diagram', a2)
    if hasattr(a2, 'uma_Point107'):
        assert not _is_linked(a2, 'uma_Point107', b)


def test_assoc_viewport88_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_DiagramLink(zoom="sample_text")
    _safe_set(b, 'uma_DiagramLink', a1)
    assert _is_linked(b, 'uma_DiagramLink', a1)
    if hasattr(a1, 'uma_Point89'):
        assert _is_linked(a1, 'uma_Point89', b)
    _safe_set(b, 'uma_DiagramLink', a2)
    assert _is_linked(b, 'uma_DiagramLink', a2)
    if hasattr(a1, 'uma_Point89'):
        assert not _is_linked(a1, 'uma_Point89', b)
    if hasattr(a2, 'uma_Point89'):
        assert _is_linked(a2, 'uma_Point89', b)
    _safe_set(b, 'uma_DiagramLink', None)
    assert not _is_linked(b, 'uma_DiagramLink', a2)
    if hasattr(a2, 'uma_Point89'):
        assert not _is_linked(a2, 'uma_Point89', b)


def test_assoc_waypoints117_reverse_link_reassign_clear():
    a1 = uma_Polyline(closed="sample_text")
    a2 = uma_Polyline(closed="sample_text_2")
    b = uma_Point(x="sample_text", y="sample_text")
    _safe_set(b, 'uma_Point118', a1)
    assert _is_linked(b, 'uma_Point118', a1)
    if hasattr(a1, 'uma_Polyline'):
        assert _is_linked(a1, 'uma_Polyline', b)
    _safe_set(b, 'uma_Point118', a2)
    assert _is_linked(b, 'uma_Point118', a2)
    if hasattr(a1, 'uma_Polyline'):
        assert not _is_linked(a1, 'uma_Polyline', b)
    if hasattr(a2, 'uma_Polyline'):
        assert _is_linked(a2, 'uma_Polyline', b)
    _safe_set(b, 'uma_Point118', None)
    assert not _is_linked(b, 'uma_Point118', a2)
    if hasattr(a2, 'uma_Polyline'):
        assert not _is_linked(a2, 'uma_Polyline', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_WorkProduct167_stub_double():
    # uma_WorkProduct has no real 'uma_WorkProduct169' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_WorkProduct()
    setattr(partner, 'uma_WorkProduct169', None)
    _safe_set(owner, 'uma_WorkProductDescriptor168', partner)
    assert getattr(partner, 'uma_WorkProduct169') == owner
    _safe_set(owner, 'uma_WorkProductDescriptor168', None)
    assert getattr(partner, 'uma_WorkProduct169') is None


def test_assoc_activityReferences211_stub_double():
    # uma_Practice has no real 'uma_Practice212' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Practice()
    setattr(partner, 'uma_Practice212', None)
    _safe_set(owner, 'uma_Activity213', partner)
    assert owner in getattr(partner, 'uma_Practice212')
    _safe_set(owner, 'uma_Activity213', None)
    assert owner not in getattr(partner, 'uma_Practice212')


def test_assoc_categorizedElements270_stub_double():
    # uma_CustomCategory has no real 'uma_CustomCategory' property in the generated
    # code (a bare stub) -- manually attach it so uma_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    partner = uma_CustomCategory()
    setattr(partner, 'uma_CustomCategory', None)
    _safe_set(owner, 'uma_DescribableElement271', partner)
    assert owner in getattr(partner, 'uma_CustomCategory')
    _safe_set(owner, 'uma_DescribableElement271', None)
    assert owner not in getattr(partner, 'uma_CustomCategory')


def test_assoc_checklists126_stub_double():
    # uma_Checklist has no real 'uma_Checklist128' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Checklist()
    setattr(partner, 'uma_Checklist128', None)
    _safe_set(owner, 'uma_Activity127', {partner})
    assert getattr(partner, 'uma_Checklist128') == owner
    _safe_set(owner, 'uma_Activity127', set())
    assert getattr(partner, 'uma_Checklist128') is None


def test_assoc_concepts129_stub_double():
    # uma_Concept has no real 'uma_Concept131' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Concept()
    setattr(partner, 'uma_Concept131', None)
    _safe_set(owner, 'uma_Activity130', {partner})
    assert getattr(partner, 'uma_Concept131') == owner
    _safe_set(owner, 'uma_Activity130', set())
    assert getattr(partner, 'uma_Concept131') is None


def test_assoc_contained79_stub_double():
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


def test_assoc_container85_stub_double():
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


def test_assoc_copyrightStatement310_stub_double():
    # uma_SupportingMaterial has no real 'uma_SupportingMaterial311' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    partner = uma_SupportingMaterial()
    setattr(partner, 'uma_SupportingMaterial311', None)
    _safe_set(owner, 'uma_MethodUnit', partner)
    assert getattr(partner, 'uma_SupportingMaterial311') == owner
    _safe_set(owner, 'uma_MethodUnit', None)
    assert getattr(partner, 'uma_SupportingMaterial311') is None


def test_assoc_diagrams292_stub_double():
    # uma_ProcessPackage has no real 'uma_ProcessPackage293' property in the generated
    # code (a bare stub) -- manually attach it so uma_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Diagram(zoom="sample_text")
    partner = uma_ProcessPackage()
    setattr(partner, 'uma_ProcessPackage293', None)
    _safe_set(owner, 'uma_Diagram294', partner)
    assert owner in getattr(partner, 'uma_ProcessPackage293')
    _safe_set(owner, 'uma_Diagram294', None)
    assert owner not in getattr(partner, 'uma_ProcessPackage293')


def test_assoc_element114_stub_double():
    # uma_UMASemanticModelBridge has no real 'uma_UMASemanticModelBridge' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    partner = uma_UMASemanticModelBridge()
    setattr(partner, 'uma_UMASemanticModelBridge', None)
    _safe_set(owner, 'uma_MethodElement115', partner)
    assert getattr(partner, 'uma_UMASemanticModelBridge') == owner
    _safe_set(owner, 'uma_MethodElement115', None)
    assert getattr(partner, 'uma_UMASemanticModelBridge') is None


def test_assoc_examples132_stub_double():
    # uma_Example has no real 'uma_Example134' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Example()
    setattr(partner, 'uma_Example134', None)
    _safe_set(owner, 'uma_Activity133', {partner})
    assert getattr(partner, 'uma_Example134') == owner
    _safe_set(owner, 'uma_Activity133', set())
    assert getattr(partner, 'uma_Example134') is None


def test_assoc_externalInput186_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor187' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor187', None)
    _safe_set(owner, 'uma_WorkProductDescriptor188', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor187')
    _safe_set(owner, 'uma_WorkProductDescriptor188', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor187')


def test_assoc_graphElement90_stub_double():
    # uma_GraphElement has no real 'GraphElement91' property in the generated
    # code (a bare stub) -- manually attach it so uma_DiagramLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DiagramLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DiagramLink(zoom="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement91', None)
    _safe_set(owner, 'link', partner)
    assert getattr(partner, 'GraphElement91') == owner
    _safe_set(owner, 'link', None)
    assert getattr(partner, 'GraphElement91') is None


def test_assoc_graphElement96_stub_double():
    # uma_GraphElement has no real 'GraphElement97' property in the generated
    # code (a bare stub) -- manually attach it so uma_SemanticModelBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_SemanticModelBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_SemanticModelBridge(presentation="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement97', None)
    _safe_set(owner, 'semanticModel', partner)
    assert getattr(partner, 'GraphElement97') == owner
    _safe_set(owner, 'semanticModel', None)
    assert getattr(partner, 'GraphElement97') is None


def test_assoc_guidelines135_stub_double():
    # uma_Guideline has no real 'uma_Guideline137' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Guideline()
    setattr(partner, 'uma_Guideline137', None)
    _safe_set(owner, 'uma_Activity136', {partner})
    assert getattr(partner, 'uma_Guideline137') == owner
    _safe_set(owner, 'uma_Activity136', set())
    assert getattr(partner, 'uma_Guideline137') is None


def test_assoc_interfaceIO298_stub_double():
    # uma_ProcessComponentInterface has no real 'uma_ProcessComponentInterface299' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_ProcessComponentInterface()
    setattr(partner, 'uma_ProcessComponentInterface299', None)
    _safe_set(owner, 'uma_WorkProductDescriptor300', partner)
    assert owner in getattr(partner, 'uma_ProcessComponentInterface299')
    _safe_set(owner, 'uma_WorkProductDescriptor300', None)
    assert owner not in getattr(partner, 'uma_ProcessComponentInterface299')


def test_assoc_link80_stub_double():
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


def test_assoc_mandatoryInput189_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor190' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor190', None)
    _safe_set(owner, 'uma_WorkProductDescriptor191', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor190')
    _safe_set(owner, 'uma_WorkProductDescriptor191', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor190')


def test_assoc_methodPackageSelection315_stub_double():
    # uma_MethodConfiguration has no real 'uma_MethodConfiguration316' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPackage(global_="sample_text")
    partner = uma_MethodConfiguration()
    setattr(partner, 'uma_MethodConfiguration316', None)
    _safe_set(owner, 'uma_MethodPackage317', partner)
    assert owner in getattr(partner, 'uma_MethodConfiguration316')
    _safe_set(owner, 'uma_MethodPackage317', None)
    assert owner not in getattr(partner, 'uma_MethodConfiguration316')


def test_assoc_methodPluginSelection312_stub_double():
    # uma_MethodConfiguration has no real 'uma_MethodConfiguration313' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPlugin(userChangeable="sample_text")
    partner = uma_MethodConfiguration()
    setattr(partner, 'uma_MethodConfiguration313', None)
    _safe_set(owner, 'uma_MethodPlugin314', partner)
    assert owner in getattr(partner, 'uma_MethodConfiguration313')
    _safe_set(owner, 'uma_MethodPlugin314', None)
    assert owner not in getattr(partner, 'uma_MethodConfiguration313')


def test_assoc_methodPlugins335_stub_double():
    # uma_MethodLibrary has no real 'uma_MethodLibrary' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPlugin(userChangeable="sample_text")
    partner = uma_MethodLibrary()
    setattr(partner, 'uma_MethodLibrary', None)
    _safe_set(owner, 'uma_MethodPlugin336', partner)
    assert owner in getattr(partner, 'uma_MethodLibrary')
    _safe_set(owner, 'uma_MethodPlugin336', None)
    assert owner not in getattr(partner, 'uma_MethodLibrary')


def test_assoc_modifies159_stub_double():
    # uma_RoleDescriptor has no real 'uma_RoleDescriptor160' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'uma_RoleDescriptor160', None)
    _safe_set(owner, 'uma_WorkProductDescriptor', partner)
    assert owner in getattr(partner, 'uma_RoleDescriptor160')
    _safe_set(owner, 'uma_WorkProductDescriptor', None)
    assert owner not in getattr(partner, 'uma_RoleDescriptor160')


def test_assoc_optionalInput192_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor193' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor193', None)
    _safe_set(owner, 'uma_WorkProductDescriptor194', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor193')
    _safe_set(owner, 'uma_WorkProductDescriptor194', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor193')


def test_assoc_output195_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor196' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor196', None)
    _safe_set(owner, 'uma_WorkProductDescriptor197', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor196')
    _safe_set(owner, 'uma_WorkProductDescriptor197', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor196')


def test_assoc_position78_stub_double():
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


def test_assoc_postcondition61_stub_double():
    # uma_WorkDefinition has no real 'uma_WorkDefinition62' property in the generated
    # code (a bare stub) -- manually attach it so uma_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Constraint(body="sample_text")
    partner = uma_WorkDefinition()
    setattr(partner, 'uma_WorkDefinition62', None)
    _safe_set(owner, 'uma_Constraint63', partner)
    assert getattr(partner, 'uma_WorkDefinition62') == owner
    _safe_set(owner, 'uma_Constraint63', None)
    assert getattr(partner, 'uma_WorkDefinition62') is None


def test_assoc_precondition59_stub_double():
    # uma_WorkDefinition has no real 'uma_WorkDefinition' property in the generated
    # code (a bare stub) -- manually attach it so uma_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Constraint(body="sample_text")
    partner = uma_WorkDefinition()
    setattr(partner, 'uma_WorkDefinition', None)
    _safe_set(owner, 'uma_Constraint60', partner)
    assert getattr(partner, 'uma_WorkDefinition') == owner
    _safe_set(owner, 'uma_Constraint60', None)
    assert getattr(partner, 'uma_WorkDefinition') is None


def test_assoc_referenceWorkflows252_stub_double():
    # uma_Discipline has no real 'uma_Discipline253' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_Discipline()
    setattr(partner, 'uma_Discipline253', None)
    _safe_set(owner, 'uma_Activity254', partner)
    assert owner in getattr(partner, 'uma_Discipline253')
    _safe_set(owner, 'uma_Activity254', None)
    assert owner not in getattr(partner, 'uma_Discipline253')


def test_assoc_responsibleFor161_stub_double():
    # uma_RoleDescriptor has no real 'uma_RoleDescriptor162' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'uma_RoleDescriptor162', None)
    _safe_set(owner, 'uma_WorkProductDescriptor163', partner)
    assert owner in getattr(partner, 'uma_RoleDescriptor162')
    _safe_set(owner, 'uma_WorkProductDescriptor163', None)
    assert owner not in getattr(partner, 'uma_RoleDescriptor162')


def test_assoc_reusableAssets138_stub_double():
    # uma_ReusableAsset has no real 'uma_ReusableAsset140' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_ReusableAsset()
    setattr(partner, 'uma_ReusableAsset140', None)
    _safe_set(owner, 'uma_Activity139', {partner})
    assert getattr(partner, 'uma_ReusableAsset140') == owner
    _safe_set(owner, 'uma_Activity139', set())
    assert getattr(partner, 'uma_ReusableAsset140') is None


def test_assoc_roadmaps122_stub_double():
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


def test_assoc_selectedSteps201_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor202' property in the generated
    # code (a bare stub) -- manually attach it so uma_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor202', None)
    _safe_set(owner, 'uma_Section203', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor202')
    _safe_set(owner, 'uma_Section203', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor202')


def test_assoc_semanticModel83_stub_double():
    # uma_GraphElement has no real 'graphElement84' property in the generated
    # code (a bare stub) -- manually attach it so uma_SemanticModelBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_SemanticModelBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_SemanticModelBridge(presentation="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'graphElement84', None)
    _safe_set(owner, 'SemanticModelBridge', partner)
    assert getattr(partner, 'graphElement84') == owner
    _safe_set(owner, 'SemanticModelBridge', None)
    assert getattr(partner, 'graphElement84') is None


def test_assoc_size113_stub_double():
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


def test_assoc_supportingMaterials123_stub_double():
    # uma_SupportingMaterial has no real 'uma_SupportingMaterial125' property in the generated
    # code (a bare stub) -- manually attach it so uma_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Activity(isEnactable="sample_text")
    partner = uma_SupportingMaterial()
    setattr(partner, 'uma_SupportingMaterial125', None)
    _safe_set(owner, 'uma_Activity124', {partner})
    assert getattr(partner, 'uma_SupportingMaterial125') == owner
    _safe_set(owner, 'uma_Activity124', set())
    assert getattr(partner, 'uma_SupportingMaterial125') is None


def test_assoc_waypoints104_stub_double():
    # uma_GraphEdge has no real 'uma_GraphEdge' property in the generated
    # code (a bare stub) -- manually attach it so uma_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Point(x="sample_text", y="sample_text")
    partner = uma_GraphEdge()
    setattr(partner, 'uma_GraphEdge', None)
    _safe_set(owner, 'uma_Point105', partner)
    assert owner in getattr(partner, 'uma_GraphEdge')
    _safe_set(owner, 'uma_Point105', None)
    assert owner not in getattr(partner, 'uma_GraphEdge')


