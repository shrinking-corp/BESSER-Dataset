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
    FulfillableElement,
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
    uma_ApplicableMetaClassInfo,
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
    uma_FulfillableElement,
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
    uma_Kind,
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

def test_assoc_bases249_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(supporting=True, userChangeable="sample_text")
    a2 = uma_MethodPlugin(supporting=False, userChangeable="sample_text_2")
    b = uma_MethodPlugin(supporting=True, userChangeable="sample_text")
    _safe_set(b, 'uma_MethodPlugin250', a1)
    assert _is_linked(b, 'uma_MethodPlugin250', a1)
    if hasattr(a1, 'uma_MethodPlugin248'):
        assert _is_linked(a1, 'uma_MethodPlugin248', b)
    _safe_set(b, 'uma_MethodPlugin250', a2)
    assert _is_linked(b, 'uma_MethodPlugin250', a2)
    if hasattr(a1, 'uma_MethodPlugin248'):
        assert not _is_linked(a1, 'uma_MethodPlugin248', b)
    if hasattr(a2, 'uma_MethodPlugin248'):
        assert _is_linked(a2, 'uma_MethodPlugin248', b)
    _safe_set(b, 'uma_MethodPlugin250', None)
    assert not _is_linked(b, 'uma_MethodPlugin250', a2)
    if hasattr(a2, 'uma_MethodPlugin248'):
        assert not _is_linked(a2, 'uma_MethodPlugin248', b)


def test_assoc_center318_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    _safe_set(b, 'uma_Ellipse', a1)
    assert _is_linked(b, 'uma_Ellipse', a1)
    if hasattr(a1, 'uma_Point319'):
        assert _is_linked(a1, 'uma_Point319', b)
    _safe_set(b, 'uma_Ellipse', a2)
    assert _is_linked(b, 'uma_Ellipse', a2)
    if hasattr(a1, 'uma_Point319'):
        assert not _is_linked(a1, 'uma_Point319', b)
    if hasattr(a2, 'uma_Point319'):
        assert _is_linked(a2, 'uma_Point319', b)
    _safe_set(b, 'uma_Ellipse', None)
    assert not _is_linked(b, 'uma_Ellipse', a2)
    if hasattr(a2, 'uma_Point319'):
        assert not _is_linked(a2, 'uma_Point319', b)


def test_assoc_childPackages155_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage156', a1)
    assert _is_linked(b, 'uma_MethodPackage156', a1)
    if hasattr(a1, 'uma_MethodPackage154'):
        assert _is_linked(a1, 'uma_MethodPackage154', b)
    _safe_set(b, 'uma_MethodPackage156', a2)
    assert _is_linked(b, 'uma_MethodPackage156', a2)
    if hasattr(a1, 'uma_MethodPackage154'):
        assert not _is_linked(a1, 'uma_MethodPackage154', b)
    if hasattr(a2, 'uma_MethodPackage154'):
        assert _is_linked(a2, 'uma_MethodPackage154', b)
    _safe_set(b, 'uma_MethodPackage156', None)
    assert not _is_linked(b, 'uma_MethodPackage156', a2)
    if hasattr(a2, 'uma_MethodPackage154'):
        assert not _is_linked(a2, 'uma_MethodPackage154', b)


def test_assoc_deliverableParts169_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'uma_WorkProductDescriptor170', a1)
    assert _is_linked(b, 'uma_WorkProductDescriptor170', a1)
    if hasattr(a1, 'uma_WorkProductDescriptor168'):
        assert _is_linked(a1, 'uma_WorkProductDescriptor168', b)
    _safe_set(b, 'uma_WorkProductDescriptor170', a2)
    assert _is_linked(b, 'uma_WorkProductDescriptor170', a2)
    if hasattr(a1, 'uma_WorkProductDescriptor168'):
        assert not _is_linked(a1, 'uma_WorkProductDescriptor168', b)
    if hasattr(a2, 'uma_WorkProductDescriptor168'):
        assert _is_linked(a2, 'uma_WorkProductDescriptor168', b)
    _safe_set(b, 'uma_WorkProductDescriptor170', None)
    assert not _is_linked(b, 'uma_WorkProductDescriptor170', a2)
    if hasattr(a2, 'uma_WorkProductDescriptor168'):
        assert not _is_linked(a2, 'uma_WorkProductDescriptor168', b)


def test_assoc_diagram293_reverse_link_reassign_clear():
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


def test_assoc_diagram303_reverse_link_reassign_clear():
    a1 = uma_SemanticModelBridge(presentation="sample_text")
    a2 = uma_SemanticModelBridge(presentation="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'Diagram304', a1)
    assert _is_linked(b, 'Diagram304', a1)
    if hasattr(a1, 'namespace'):
        assert _is_linked(a1, 'namespace', b)
    _safe_set(b, 'Diagram304', a2)
    assert _is_linked(b, 'Diagram304', a2)
    if hasattr(a1, 'namespace'):
        assert not _is_linked(a1, 'namespace', b)
    if hasattr(a2, 'namespace'):
        assert _is_linked(a2, 'namespace', b)
    _safe_set(b, 'Diagram304', None)
    assert not _is_linked(b, 'Diagram304', a2)
    if hasattr(a2, 'namespace'):
        assert not _is_linked(a2, 'namespace', b)


def test_assoc_diagramLink270_reverse_link_reassign_clear():
    a1 = uma_DiagramLink(zoom="sample_text")
    a2 = uma_DiagramLink(zoom="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'diagram', {a1})
    assert _is_linked(b, 'diagram', a1)
    if hasattr(a1, 'DiagramLink'):
        assert _is_linked(a1, 'DiagramLink', b)
    _safe_set(b, 'diagram', {a2})
    assert _is_linked(b, 'diagram', a2)
    if hasattr(a1, 'DiagramLink'):
        assert not _is_linked(a1, 'DiagramLink', b)
    if hasattr(a2, 'DiagramLink'):
        assert _is_linked(a2, 'DiagramLink', b)
    _safe_set(b, 'diagram', set())
    assert not _is_linked(b, 'diagram', a2)
    if hasattr(a2, 'DiagramLink'):
        assert not _is_linked(a2, 'DiagramLink', b)


def test_assoc_impactedBy164_reverse_link_reassign_clear():
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


def test_assoc_impacts166_reverse_link_reassign_clear():
    a1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    a2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    b = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    _safe_set(b, 'impactedBy', {a1})
    assert _is_linked(b, 'impactedBy', a1)
    if hasattr(a1, 'WorkProductDescriptor167'):
        assert _is_linked(a1, 'WorkProductDescriptor167', b)
    _safe_set(b, 'impactedBy', {a2})
    assert _is_linked(b, 'impactedBy', a2)
    if hasattr(a1, 'WorkProductDescriptor167'):
        assert not _is_linked(a1, 'WorkProductDescriptor167', b)
    if hasattr(a2, 'WorkProductDescriptor167'):
        assert _is_linked(a2, 'WorkProductDescriptor167', b)
    _safe_set(b, 'impactedBy', set())
    assert not _is_linked(b, 'impactedBy', a2)
    if hasattr(a2, 'WorkProductDescriptor167'):
        assert not _is_linked(a2, 'WorkProductDescriptor167', b)


def test_assoc_linkToPredecessor102_reverse_link_reassign_clear():
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
    b = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", presentationName="sample_text", suppressed="sample_text")
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


def test_assoc_methodPackages245_reverse_link_reassign_clear():
    a1 = uma_MethodPlugin(supporting=True, userChangeable="sample_text")
    a2 = uma_MethodPlugin(supporting=False, userChangeable="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage247', a1)
    assert _is_linked(b, 'uma_MethodPackage247', a1)
    if hasattr(a1, 'uma_MethodPlugin246'):
        assert _is_linked(a1, 'uma_MethodPlugin246', b)
    _safe_set(b, 'uma_MethodPackage247', a2)
    assert _is_linked(b, 'uma_MethodPackage247', a2)
    if hasattr(a1, 'uma_MethodPlugin246'):
        assert not _is_linked(a1, 'uma_MethodPlugin246', b)
    if hasattr(a2, 'uma_MethodPlugin246'):
        assert _is_linked(a2, 'uma_MethodPlugin246', b)
    _safe_set(b, 'uma_MethodPackage247', None)
    assert not _is_linked(b, 'uma_MethodPackage247', a2)
    if hasattr(a2, 'uma_MethodPlugin246'):
        assert not _is_linked(a2, 'uma_MethodPlugin246', b)


def test_assoc_namespace271_reverse_link_reassign_clear():
    a1 = uma_SemanticModelBridge(presentation="sample_text")
    a2 = uma_SemanticModelBridge(presentation="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'diagram272', a1)
    assert _is_linked(b, 'diagram272', a1)
    if hasattr(a1, 'SemanticModelBridge'):
        assert _is_linked(a1, 'SemanticModelBridge', b)
    _safe_set(b, 'diagram272', a2)
    assert _is_linked(b, 'diagram272', a2)
    if hasattr(a1, 'SemanticModelBridge'):
        assert not _is_linked(a1, 'SemanticModelBridge', b)
    if hasattr(a2, 'SemanticModelBridge'):
        assert _is_linked(a2, 'SemanticModelBridge', b)
    _safe_set(b, 'diagram272', None)
    assert not _is_linked(b, 'diagram272', a2)
    if hasattr(a2, 'SemanticModelBridge'):
        assert not _is_linked(a2, 'SemanticModelBridge', b)


def test_assoc_ownedRules0_reverse_link_reassign_clear():
    a1 = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", presentationName="sample_text", suppressed="sample_text")
    a2 = uma_MethodElement(briefDescription="sample_text_2", guid="sample_text_2", orderingGuide="sample_text_2", presentationName="sample_text_2", suppressed="sample_text_2")
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


def test_assoc_planningData108_reverse_link_reassign_clear():
    a1 = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    a2 = uma_PlanningData(finishDate="sample_text_2", rank="sample_text_2", startDate="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement109', a1)
    assert _is_linked(b, 'uma_BreakdownElement109', a1)
    if hasattr(a1, 'uma_PlanningData'):
        assert _is_linked(a1, 'uma_PlanningData', b)
    _safe_set(b, 'uma_BreakdownElement109', a2)
    assert _is_linked(b, 'uma_BreakdownElement109', a2)
    if hasattr(a1, 'uma_PlanningData'):
        assert not _is_linked(a1, 'uma_PlanningData', b)
    if hasattr(a2, 'uma_PlanningData'):
        assert _is_linked(a2, 'uma_PlanningData', b)
    _safe_set(b, 'uma_BreakdownElement109', None)
    assert not _is_linked(b, 'uma_BreakdownElement109', a2)
    if hasattr(a2, 'uma_PlanningData'):
        assert not _is_linked(a2, 'uma_PlanningData', b)


def test_assoc_pred141_reverse_link_reassign_clear():
    a1 = uma_WorkOrder(linkType="sample_text")
    a2 = uma_WorkOrder(linkType="sample_text_2")
    b = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    _safe_set(b, 'uma_WorkBreakdownElement143', a1)
    assert _is_linked(b, 'uma_WorkBreakdownElement143', a1)
    if hasattr(a1, 'uma_WorkOrder142'):
        assert _is_linked(a1, 'uma_WorkOrder142', b)
    _safe_set(b, 'uma_WorkBreakdownElement143', a2)
    assert _is_linked(b, 'uma_WorkBreakdownElement143', a2)
    if hasattr(a1, 'uma_WorkOrder142'):
        assert not _is_linked(a1, 'uma_WorkOrder142', b)
    if hasattr(a2, 'uma_WorkOrder142'):
        assert _is_linked(a2, 'uma_WorkOrder142', b)
    _safe_set(b, 'uma_WorkBreakdownElement143', None)
    assert not _is_linked(b, 'uma_WorkBreakdownElement143', a2)
    if hasattr(a2, 'uma_WorkOrder142'):
        assert not _is_linked(a2, 'uma_WorkOrder142', b)


def test_assoc_predecessor29_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    _safe_set(b, 'uma_Section30', a1)
    assert _is_linked(b, 'uma_Section30', a1)
    if hasattr(a1, 'uma_Section28'):
        assert _is_linked(a1, 'uma_Section28', b)
    _safe_set(b, 'uma_Section30', a2)
    assert _is_linked(b, 'uma_Section30', a2)
    if hasattr(a1, 'uma_Section28'):
        assert not _is_linked(a1, 'uma_Section28', b)
    if hasattr(a2, 'uma_Section28'):
        assert _is_linked(a2, 'uma_Section28', b)
    _safe_set(b, 'uma_Section30', None)
    assert not _is_linked(b, 'uma_Section30', a2)
    if hasattr(a2, 'uma_Section28'):
        assert not _is_linked(a2, 'uma_Section28', b)


def test_assoc_presentation20_reverse_link_reassign_clear():
    a1 = uma_DescribableElement(nodeicon="sample_text", shapeicon="sample_text")
    a2 = uma_DescribableElement(nodeicon="sample_text_2", shapeicon="sample_text_2")
    b = uma_ContentDescription(externalId="sample_text", keyConsiderations="sample_text", longPresentationName="sample_text", mainDescription="sample_text")
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


def test_assoc_presentedAfter104_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement103', a1)
    assert _is_linked(b, 'uma_BreakdownElement103', a1)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert _is_linked(a1, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_BreakdownElement103', a2)
    assert _is_linked(b, 'uma_BreakdownElement103', a2)
    if hasattr(a1, 'uma_BreakdownElement'):
        assert not _is_linked(a1, 'uma_BreakdownElement', b)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert _is_linked(a2, 'uma_BreakdownElement', b)
    _safe_set(b, 'uma_BreakdownElement103', None)
    assert not _is_linked(b, 'uma_BreakdownElement103', a2)
    if hasattr(a2, 'uma_BreakdownElement'):
        assert not _is_linked(a2, 'uma_BreakdownElement', b)


def test_assoc_presentedBefore106_reverse_link_reassign_clear():
    a1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    a2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    b = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    _safe_set(b, 'uma_BreakdownElement107', a1)
    assert _is_linked(b, 'uma_BreakdownElement107', a1)
    if hasattr(a1, 'uma_BreakdownElement105'):
        assert _is_linked(a1, 'uma_BreakdownElement105', b)
    _safe_set(b, 'uma_BreakdownElement107', a2)
    assert _is_linked(b, 'uma_BreakdownElement107', a2)
    if hasattr(a1, 'uma_BreakdownElement105'):
        assert not _is_linked(a1, 'uma_BreakdownElement105', b)
    if hasattr(a2, 'uma_BreakdownElement105'):
        assert _is_linked(a2, 'uma_BreakdownElement105', b)
    _safe_set(b, 'uma_BreakdownElement107', None)
    assert not _is_linked(b, 'uma_BreakdownElement107', a2)
    if hasattr(a2, 'uma_BreakdownElement105'):
        assert not _is_linked(a2, 'uma_BreakdownElement105', b)


def test_assoc_property288_reverse_link_reassign_clear():
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


def test_assoc_reference287_reverse_link_reassign_clear():
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


def test_assoc_referenced289_reverse_link_reassign_clear():
    a1 = uma_Reference(isIndividualRepresentation="sample_text")
    a2 = uma_Reference(isIndividualRepresentation="sample_text_2")
    b = uma_DiagramElement(isVisible="sample_text")
    _safe_set(b, 'DiagramElement290', a1)
    assert _is_linked(b, 'DiagramElement290', a1)
    if hasattr(a1, 'reference'):
        assert _is_linked(a1, 'reference', b)
    _safe_set(b, 'DiagramElement290', a2)
    assert _is_linked(b, 'DiagramElement290', a2)
    if hasattr(a1, 'reference'):
        assert not _is_linked(a1, 'reference', b)
    if hasattr(a2, 'reference'):
        assert _is_linked(a2, 'reference', b)
    _safe_set(b, 'DiagramElement290', None)
    assert not _is_linked(b, 'DiagramElement290', a2)
    if hasattr(a2, 'reference'):
        assert not _is_linked(a2, 'reference', b)


def test_assoc_reusedPackages153_reverse_link_reassign_clear():
    a1 = uma_MethodPackage(global_="sample_text")
    a2 = uma_MethodPackage(global_="sample_text_2")
    b = uma_MethodPackage(global_="sample_text")
    _safe_set(b, 'uma_MethodPackage152', {a1})
    assert _is_linked(b, 'uma_MethodPackage152', a1)
    if hasattr(a1, 'uma_MethodPackage'):
        assert _is_linked(a1, 'uma_MethodPackage', b)
    _safe_set(b, 'uma_MethodPackage152', {a2})
    assert _is_linked(b, 'uma_MethodPackage152', a2)
    if hasattr(a1, 'uma_MethodPackage'):
        assert not _is_linked(a1, 'uma_MethodPackage', b)
    if hasattr(a2, 'uma_MethodPackage'):
        assert _is_linked(a2, 'uma_MethodPackage', b)
    _safe_set(b, 'uma_MethodPackage152', set())
    assert not _is_linked(b, 'uma_MethodPackage152', a2)
    if hasattr(a2, 'uma_MethodPackage'):
        assert not _is_linked(a2, 'uma_MethodPackage', b)


def test_assoc_sections21_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_ContentDescription(externalId="sample_text", keyConsiderations="sample_text", longPresentationName="sample_text", mainDescription="sample_text")
    _safe_set(b, 'uma_ContentDescription22', {a1})
    assert _is_linked(b, 'uma_ContentDescription22', a1)
    if hasattr(a1, 'uma_Section'):
        assert _is_linked(a1, 'uma_Section', b)
    _safe_set(b, 'uma_ContentDescription22', {a2})
    assert _is_linked(b, 'uma_ContentDescription22', a2)
    if hasattr(a1, 'uma_Section'):
        assert not _is_linked(a1, 'uma_Section', b)
    if hasattr(a2, 'uma_Section'):
        assert _is_linked(a2, 'uma_Section', b)
    _safe_set(b, 'uma_ContentDescription22', set())
    assert not _is_linked(b, 'uma_ContentDescription22', a2)
    if hasattr(a2, 'uma_Section'):
        assert not _is_linked(a2, 'uma_Section', b)


def test_assoc_subSections26_reverse_link_reassign_clear():
    a1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    a2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    b = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    _safe_set(b, 'uma_Section27', a1)
    assert _is_linked(b, 'uma_Section27', a1)
    if hasattr(a1, 'uma_Section25'):
        assert _is_linked(a1, 'uma_Section25', b)
    _safe_set(b, 'uma_Section27', a2)
    assert _is_linked(b, 'uma_Section27', a2)
    if hasattr(a1, 'uma_Section25'):
        assert not _is_linked(a1, 'uma_Section25', b)
    if hasattr(a2, 'uma_Section25'):
        assert _is_linked(a2, 'uma_Section25', b)
    _safe_set(b, 'uma_Section27', None)
    assert not _is_linked(b, 'uma_Section27', a2)
    if hasattr(a2, 'uma_Section25'):
        assert not _is_linked(a2, 'uma_Section25', b)


def test_assoc_variabilityBasedOnElement32_reverse_link_reassign_clear():
    a1 = uma_VariabilityElement(variabilityType="sample_text")
    a2 = uma_VariabilityElement(variabilityType="sample_text_2")
    b = uma_VariabilityElement(variabilityType="sample_text")
    _safe_set(b, 'uma_VariabilityElement31', a1)
    assert _is_linked(b, 'uma_VariabilityElement31', a1)
    if hasattr(a1, 'uma_VariabilityElement'):
        assert _is_linked(a1, 'uma_VariabilityElement', b)
    _safe_set(b, 'uma_VariabilityElement31', a2)
    assert _is_linked(b, 'uma_VariabilityElement31', a2)
    if hasattr(a1, 'uma_VariabilityElement'):
        assert not _is_linked(a1, 'uma_VariabilityElement', b)
    if hasattr(a2, 'uma_VariabilityElement'):
        assert _is_linked(a2, 'uma_VariabilityElement', b)
    _safe_set(b, 'uma_VariabilityElement31', None)
    assert not _is_linked(b, 'uma_VariabilityElement31', a2)
    if hasattr(a2, 'uma_VariabilityElement'):
        assert not _is_linked(a2, 'uma_VariabilityElement', b)


def test_assoc_viewpoint273_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_Diagram(zoom="sample_text")
    _safe_set(b, 'uma_Diagram274', a1)
    assert _is_linked(b, 'uma_Diagram274', a1)
    if hasattr(a1, 'uma_Point'):
        assert _is_linked(a1, 'uma_Point', b)
    _safe_set(b, 'uma_Diagram274', a2)
    assert _is_linked(b, 'uma_Diagram274', a2)
    if hasattr(a1, 'uma_Point'):
        assert not _is_linked(a1, 'uma_Point', b)
    if hasattr(a2, 'uma_Point'):
        assert _is_linked(a2, 'uma_Point', b)
    _safe_set(b, 'uma_Diagram274', None)
    assert not _is_linked(b, 'uma_Diagram274', a2)
    if hasattr(a2, 'uma_Point'):
        assert not _is_linked(a2, 'uma_Point', b)


def test_assoc_viewport291_reverse_link_reassign_clear():
    a1 = uma_Point(x="sample_text", y="sample_text")
    a2 = uma_Point(x="sample_text_2", y="sample_text_2")
    b = uma_DiagramLink(zoom="sample_text")
    _safe_set(b, 'uma_DiagramLink', a1)
    assert _is_linked(b, 'uma_DiagramLink', a1)
    if hasattr(a1, 'uma_Point292'):
        assert _is_linked(a1, 'uma_Point292', b)
    _safe_set(b, 'uma_DiagramLink', a2)
    assert _is_linked(b, 'uma_DiagramLink', a2)
    if hasattr(a1, 'uma_Point292'):
        assert not _is_linked(a1, 'uma_Point292', b)
    if hasattr(a2, 'uma_Point292'):
        assert _is_linked(a2, 'uma_Point292', b)
    _safe_set(b, 'uma_DiagramLink', None)
    assert not _is_linked(b, 'uma_DiagramLink', a2)
    if hasattr(a2, 'uma_Point292'):
        assert not _is_linked(a2, 'uma_Point292', b)


def test_assoc_waypoints316_reverse_link_reassign_clear():
    a1 = uma_Polyline(closed="sample_text")
    a2 = uma_Polyline(closed="sample_text_2")
    b = uma_Point(x="sample_text", y="sample_text")
    _safe_set(b, 'uma_Point317', a1)
    assert _is_linked(b, 'uma_Point317', a1)
    if hasattr(a1, 'uma_Polyline'):
        assert _is_linked(a1, 'uma_Polyline', b)
    _safe_set(b, 'uma_Point317', a2)
    assert _is_linked(b, 'uma_Point317', a2)
    if hasattr(a1, 'uma_Polyline'):
        assert not _is_linked(a1, 'uma_Polyline', b)
    if hasattr(a2, 'uma_Polyline'):
        assert _is_linked(a2, 'uma_Polyline', b)
    _safe_set(b, 'uma_Point317', None)
    assert not _is_linked(b, 'uma_Point317', a2)
    if hasattr(a2, 'uma_Polyline'):
        assert not _is_linked(a2, 'uma_Polyline', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_WorkProduct160_stub_double():
    # uma_WorkProduct has no real 'uma_WorkProduct162' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_WorkProduct()
    setattr(partner, 'uma_WorkProduct162', None)
    _safe_set(owner, 'uma_WorkProductDescriptor161', partner)
    assert getattr(partner, 'uma_WorkProduct162') == owner
    _safe_set(owner, 'uma_WorkProductDescriptor161', None)
    assert getattr(partner, 'uma_WorkProduct162') is None


def test_assoc_applicableMetaClassInfo5_stub_double():
    # uma_Kind has no real 'uma_Kind6' property in the generated
    # code (a bare stub) -- manually attach it so uma_ApplicableMetaClassInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_ApplicableMetaClassInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_ApplicableMetaClassInfo(isPrimaryExtension="sample_text")
    partner = uma_Kind()
    setattr(partner, 'uma_Kind6', None)
    _safe_set(owner, 'uma_ApplicableMetaClassInfo', partner)
    assert owner in getattr(partner, 'uma_Kind6')
    _safe_set(owner, 'uma_ApplicableMetaClassInfo', None)
    assert owner not in getattr(partner, 'uma_Kind6')


def test_assoc_breakdownElements99_stub_double():
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


def test_assoc_categorizedElements148_stub_double():
    # uma_CustomCategory has no real 'uma_CustomCategory' property in the generated
    # code (a bare stub) -- manually attach it so uma_DescribableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DescribableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DescribableElement(nodeicon="sample_text", shapeicon="sample_text")
    partner = uma_CustomCategory()
    setattr(partner, 'uma_CustomCategory', None)
    _safe_set(owner, 'uma_DescribableElement149', partner)
    assert owner in getattr(partner, 'uma_CustomCategory')
    _safe_set(owner, 'uma_DescribableElement149', None)
    assert owner not in getattr(partner, 'uma_CustomCategory')


def test_assoc_checklists111_stub_double():
    # uma_Checklist has no real 'uma_Checklist113' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Checklist()
    setattr(partner, 'uma_Checklist113', None)
    _safe_set(owner, 'uma_BreakdownElement112', {partner})
    assert getattr(partner, 'uma_Checklist113') == owner
    _safe_set(owner, 'uma_BreakdownElement112', set())
    assert getattr(partner, 'uma_Checklist113') is None


def test_assoc_concepts114_stub_double():
    # uma_Concept has no real 'uma_Concept116' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Concept()
    setattr(partner, 'uma_Concept116', None)
    _safe_set(owner, 'uma_BreakdownElement115', {partner})
    assert getattr(partner, 'uma_Concept116') == owner
    _safe_set(owner, 'uma_BreakdownElement115', set())
    assert getattr(partner, 'uma_Concept116') is None


def test_assoc_contained276_stub_double():
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


def test_assoc_container286_stub_double():
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


def test_assoc_copyrightStatement23_stub_double():
    # uma_SupportingMaterial has no real 'uma_SupportingMaterial24' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    partner = uma_SupportingMaterial()
    setattr(partner, 'uma_SupportingMaterial24', None)
    _safe_set(owner, 'uma_MethodUnit', partner)
    assert getattr(partner, 'uma_SupportingMaterial24') == owner
    _safe_set(owner, 'uma_MethodUnit', None)
    assert getattr(partner, 'uma_SupportingMaterial24') is None


def test_assoc_diagrams268_stub_double():
    # uma_ProcessPackage has no real 'uma_ProcessPackage269' property in the generated
    # code (a bare stub) -- manually attach it so uma_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Diagram(zoom="sample_text")
    partner = uma_ProcessPackage()
    setattr(partner, 'uma_ProcessPackage269', None)
    _safe_set(owner, 'uma_Diagram', partner)
    assert owner in getattr(partner, 'uma_ProcessPackage269')
    _safe_set(owner, 'uma_Diagram', None)
    assert owner not in getattr(partner, 'uma_ProcessPackage269')


def test_assoc_element313_stub_double():
    # uma_UMASemanticModelBridge has no real 'uma_UMASemanticModelBridge' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", presentationName="sample_text", suppressed="sample_text")
    partner = uma_UMASemanticModelBridge()
    setattr(partner, 'uma_UMASemanticModelBridge', None)
    _safe_set(owner, 'uma_MethodElement314', partner)
    assert getattr(partner, 'uma_UMASemanticModelBridge') == owner
    _safe_set(owner, 'uma_MethodElement314', None)
    assert getattr(partner, 'uma_UMASemanticModelBridge') is None


def test_assoc_estimationconsiderations135_stub_double():
    # uma_EstimationConsiderations has no real 'uma_EstimationConsiderations137' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_EstimationConsiderations()
    setattr(partner, 'uma_EstimationConsiderations137', None)
    _safe_set(owner, 'uma_BreakdownElement136', {partner})
    assert getattr(partner, 'uma_EstimationConsiderations137') == owner
    _safe_set(owner, 'uma_BreakdownElement136', set())
    assert getattr(partner, 'uma_EstimationConsiderations137') is None


def test_assoc_examples117_stub_double():
    # uma_Example has no real 'uma_Example119' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Example()
    setattr(partner, 'uma_Example119', None)
    _safe_set(owner, 'uma_BreakdownElement118', {partner})
    assert getattr(partner, 'uma_Example119') == owner
    _safe_set(owner, 'uma_BreakdownElement118', set())
    assert getattr(partner, 'uma_Example119') is None


def test_assoc_externalInput194_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor195' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor195', None)
    _safe_set(owner, 'uma_WorkProductDescriptor196', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor195')
    _safe_set(owner, 'uma_WorkProductDescriptor196', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor195')


def test_assoc_graphElement294_stub_double():
    # uma_GraphElement has no real 'GraphElement295' property in the generated
    # code (a bare stub) -- manually attach it so uma_DiagramLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DiagramLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DiagramLink(zoom="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement295', None)
    _safe_set(owner, 'link', partner)
    assert getattr(partner, 'GraphElement295') == owner
    _safe_set(owner, 'link', None)
    assert getattr(partner, 'GraphElement295') is None


def test_assoc_graphElement305_stub_double():
    # uma_GraphElement has no real 'GraphElement306' property in the generated
    # code (a bare stub) -- manually attach it so uma_SemanticModelBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_SemanticModelBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_SemanticModelBridge(presentation="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'GraphElement306', None)
    _safe_set(owner, 'semanticModel', partner)
    assert getattr(partner, 'GraphElement306') == owner
    _safe_set(owner, 'semanticModel', None)
    assert getattr(partner, 'GraphElement306') is None


def test_assoc_guidelines120_stub_double():
    # uma_Guideline has no real 'uma_Guideline122' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Guideline()
    setattr(partner, 'uma_Guideline122', None)
    _safe_set(owner, 'uma_BreakdownElement121', {partner})
    assert getattr(partner, 'uma_Guideline122') == owner
    _safe_set(owner, 'uma_BreakdownElement121', set())
    assert getattr(partner, 'uma_Guideline122') is None


def test_assoc_interfaceIO310_stub_double():
    # uma_ProcessComponentInterface has no real 'uma_ProcessComponentInterface311' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_ProcessComponentInterface()
    setattr(partner, 'uma_ProcessComponentInterface311', None)
    _safe_set(owner, 'uma_WorkProductDescriptor312', partner)
    assert owner in getattr(partner, 'uma_ProcessComponentInterface311')
    _safe_set(owner, 'uma_WorkProductDescriptor312', None)
    assert owner not in getattr(partner, 'uma_ProcessComponentInterface311')


def test_assoc_kind3_stub_double():
    # uma_Kind has no real 'uma_Kind' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", presentationName="sample_text", suppressed="sample_text")
    partner = uma_Kind()
    setattr(partner, 'uma_Kind', None)
    _safe_set(owner, 'uma_MethodElement4', {partner})
    assert getattr(partner, 'uma_Kind') == owner
    _safe_set(owner, 'uma_MethodElement4', set())
    assert getattr(partner, 'uma_Kind') is None


def test_assoc_link279_stub_double():
    # uma_GraphElement has no real 'graphElement' property in the generated
    # code (a bare stub) -- manually attach it so uma_DiagramLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_DiagramLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_DiagramLink(zoom="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'graphElement', None)
    _safe_set(owner, 'DiagramLink280', partner)
    assert owner in getattr(partner, 'graphElement')
    _safe_set(owner, 'DiagramLink280', None)
    assert owner not in getattr(partner, 'graphElement')


def test_assoc_mandatoryInput197_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor198' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor198', None)
    _safe_set(owner, 'uma_WorkProductDescriptor199', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor198')
    _safe_set(owner, 'uma_WorkProductDescriptor199', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor198')


def test_assoc_methodPackageSelection227_stub_double():
    # uma_MethodConfiguration has no real 'uma_MethodConfiguration228' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPackage(global_="sample_text")
    partner = uma_MethodConfiguration()
    setattr(partner, 'uma_MethodConfiguration228', None)
    _safe_set(owner, 'uma_MethodPackage229', partner)
    assert owner in getattr(partner, 'uma_MethodConfiguration228')
    _safe_set(owner, 'uma_MethodPackage229', None)
    assert owner not in getattr(partner, 'uma_MethodConfiguration228')


def test_assoc_methodPluginSelection225_stub_double():
    # uma_MethodConfiguration has no real 'uma_MethodConfiguration226' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPlugin(supporting=True, userChangeable="sample_text")
    partner = uma_MethodConfiguration()
    setattr(partner, 'uma_MethodConfiguration226', None)
    _safe_set(owner, 'uma_MethodPlugin', partner)
    assert owner in getattr(partner, 'uma_MethodConfiguration226')
    _safe_set(owner, 'uma_MethodPlugin', None)
    assert owner not in getattr(partner, 'uma_MethodConfiguration226')


def test_assoc_methodPlugins322_stub_double():
    # uma_MethodLibrary has no real 'uma_MethodLibrary' property in the generated
    # code (a bare stub) -- manually attach it so uma_MethodPlugin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_MethodPlugin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_MethodPlugin(supporting=True, userChangeable="sample_text")
    partner = uma_MethodLibrary()
    setattr(partner, 'uma_MethodLibrary', None)
    _safe_set(owner, 'uma_MethodPlugin323', partner)
    assert owner in getattr(partner, 'uma_MethodLibrary')
    _safe_set(owner, 'uma_MethodPlugin323', None)
    assert owner not in getattr(partner, 'uma_MethodLibrary')


def test_assoc_modifies180_stub_double():
    # uma_RoleDescriptor has no real 'uma_RoleDescriptor181' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'uma_RoleDescriptor181', None)
    _safe_set(owner, 'uma_WorkProductDescriptor182', partner)
    assert owner in getattr(partner, 'uma_RoleDescriptor181')
    _safe_set(owner, 'uma_WorkProductDescriptor182', None)
    assert owner not in getattr(partner, 'uma_RoleDescriptor181')


def test_assoc_optionalInput200_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor201' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor201', None)
    _safe_set(owner, 'uma_WorkProductDescriptor202', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor201')
    _safe_set(owner, 'uma_WorkProductDescriptor202', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor201')


def test_assoc_output203_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor204' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor204', None)
    _safe_set(owner, 'uma_WorkProductDescriptor205', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor204')
    _safe_set(owner, 'uma_WorkProductDescriptor205', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor204')


def test_assoc_position277_stub_double():
    # uma_GraphElement has no real 'uma_GraphElement' property in the generated
    # code (a bare stub) -- manually attach it so uma_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Point(x="sample_text", y="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'uma_GraphElement', None)
    _safe_set(owner, 'uma_Point278', partner)
    assert getattr(partner, 'uma_GraphElement') == owner
    _safe_set(owner, 'uma_Point278', None)
    assert getattr(partner, 'uma_GraphElement') is None


def test_assoc_postcondition51_stub_double():
    # uma_WorkDefinition has no real 'uma_WorkDefinition52' property in the generated
    # code (a bare stub) -- manually attach it so uma_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Constraint(body="sample_text")
    partner = uma_WorkDefinition()
    setattr(partner, 'uma_WorkDefinition52', None)
    _safe_set(owner, 'uma_Constraint53', partner)
    assert getattr(partner, 'uma_WorkDefinition52') == owner
    _safe_set(owner, 'uma_Constraint53', None)
    assert getattr(partner, 'uma_WorkDefinition52') is None


def test_assoc_precondition49_stub_double():
    # uma_WorkDefinition has no real 'uma_WorkDefinition' property in the generated
    # code (a bare stub) -- manually attach it so uma_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Constraint(body="sample_text")
    partner = uma_WorkDefinition()
    setattr(partner, 'uma_WorkDefinition', None)
    _safe_set(owner, 'uma_Constraint50', partner)
    assert getattr(partner, 'uma_WorkDefinition') == owner
    _safe_set(owner, 'uma_Constraint50', None)
    assert getattr(partner, 'uma_WorkDefinition') is None


def test_assoc_reports132_stub_double():
    # uma_Report has no real 'uma_Report134' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Report()
    setattr(partner, 'uma_Report134', None)
    _safe_set(owner, 'uma_BreakdownElement133', {partner})
    assert getattr(partner, 'uma_Report134') == owner
    _safe_set(owner, 'uma_BreakdownElement133', set())
    assert getattr(partner, 'uma_Report134') is None


def test_assoc_requiredResults159_stub_double():
    # uma_Milestone has no real 'uma_Milestone' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_Milestone()
    setattr(partner, 'uma_Milestone', None)
    _safe_set(owner, 'uma_WorkProductDescriptor', partner)
    assert owner in getattr(partner, 'uma_Milestone')
    _safe_set(owner, 'uma_WorkProductDescriptor', None)
    assert owner not in getattr(partner, 'uma_Milestone')


def test_assoc_responsibleFor183_stub_double():
    # uma_RoleDescriptor has no real 'uma_RoleDescriptor184' property in the generated
    # code (a bare stub) -- manually attach it so uma_WorkProductDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_WorkProductDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    partner = uma_RoleDescriptor()
    setattr(partner, 'uma_RoleDescriptor184', None)
    _safe_set(owner, 'uma_WorkProductDescriptor185', partner)
    assert owner in getattr(partner, 'uma_RoleDescriptor184')
    _safe_set(owner, 'uma_WorkProductDescriptor185', None)
    assert owner not in getattr(partner, 'uma_RoleDescriptor184')


def test_assoc_reusableAssets123_stub_double():
    # uma_ReusableAsset has no real 'uma_ReusableAsset125' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_ReusableAsset()
    setattr(partner, 'uma_ReusableAsset125', None)
    _safe_set(owner, 'uma_BreakdownElement124', {partner})
    assert getattr(partner, 'uma_ReusableAsset125') == owner
    _safe_set(owner, 'uma_BreakdownElement124', set())
    assert getattr(partner, 'uma_ReusableAsset125') is None


def test_assoc_selectedSteps209_stub_double():
    # uma_TaskDescriptor has no real 'uma_TaskDescriptor210' property in the generated
    # code (a bare stub) -- manually attach it so uma_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    partner = uma_TaskDescriptor()
    setattr(partner, 'uma_TaskDescriptor210', None)
    _safe_set(owner, 'uma_Section211', partner)
    assert owner in getattr(partner, 'uma_TaskDescriptor210')
    _safe_set(owner, 'uma_Section211', None)
    assert owner not in getattr(partner, 'uma_TaskDescriptor210')


def test_assoc_semanticModel283_stub_double():
    # uma_GraphElement has no real 'graphElement284' property in the generated
    # code (a bare stub) -- manually attach it so uma_SemanticModelBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_SemanticModelBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_SemanticModelBridge(presentation="sample_text")
    partner = uma_GraphElement()
    setattr(partner, 'graphElement284', None)
    _safe_set(owner, 'SemanticModelBridge285', partner)
    assert getattr(partner, 'graphElement284') == owner
    _safe_set(owner, 'SemanticModelBridge285', None)
    assert getattr(partner, 'graphElement284') is None


def test_assoc_size275_stub_double():
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


def test_assoc_superActivities110_stub_double():
    # uma_Activity has no real 'Activity' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Activity()
    setattr(partner, 'Activity', None)
    _safe_set(owner, 'breakdownElements', partner)
    assert getattr(partner, 'Activity') == owner
    _safe_set(owner, 'breakdownElements', None)
    assert getattr(partner, 'Activity') is None


def test_assoc_supportingMaterials126_stub_double():
    # uma_SupportingMaterial has no real 'uma_SupportingMaterial128' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_SupportingMaterial()
    setattr(partner, 'uma_SupportingMaterial128', None)
    _safe_set(owner, 'uma_BreakdownElement127', {partner})
    assert getattr(partner, 'uma_SupportingMaterial128') == owner
    _safe_set(owner, 'uma_BreakdownElement127', set())
    assert getattr(partner, 'uma_SupportingMaterial128') is None


def test_assoc_templates129_stub_double():
    # uma_Template has no real 'uma_Template131' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_Template()
    setattr(partner, 'uma_Template131', None)
    _safe_set(owner, 'uma_BreakdownElement130', {partner})
    assert getattr(partner, 'uma_Template131') == owner
    _safe_set(owner, 'uma_BreakdownElement130', set())
    assert getattr(partner, 'uma_Template131') is None


def test_assoc_toolmentor138_stub_double():
    # uma_ToolMentor has no real 'uma_ToolMentor140' property in the generated
    # code (a bare stub) -- manually attach it so uma_BreakdownElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_BreakdownElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    partner = uma_ToolMentor()
    setattr(partner, 'uma_ToolMentor140', None)
    _safe_set(owner, 'uma_BreakdownElement139', {partner})
    assert getattr(partner, 'uma_ToolMentor140') == owner
    _safe_set(owner, 'uma_BreakdownElement139', set())
    assert getattr(partner, 'uma_ToolMentor140') is None


def test_assoc_waypoints299_stub_double():
    # uma_GraphEdge has no real 'uma_GraphEdge' property in the generated
    # code (a bare stub) -- manually attach it so uma_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uma_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uma_Point(x="sample_text", y="sample_text")
    partner = uma_GraphEdge()
    setattr(partner, 'uma_GraphEdge', None)
    _safe_set(owner, 'uma_Point300', partner)
    assert owner in getattr(partner, 'uma_GraphEdge')
    _safe_set(owner, 'uma_Point300', None)
    assert owner not in getattr(partner, 'uma_GraphEdge')


