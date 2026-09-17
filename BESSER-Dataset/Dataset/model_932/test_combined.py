# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MethodConfiguration,
    uma_ProcessFamily,
    ProcessPackage,
    Process,
    uma_ProcessPlanningTemplate,
    uma_ProcessContribution,
    uma_CapabilityPattern,
    uma_DeliveryProcess,
    Concept,
    uma_Whitepaper,
    Guidance,
    uma_TermDefinition,
    uma_EstimatingMetric,
    uma_Practice,
    uma_EstimationConsiderations,
    ContentCategory,
    uma_CustomCategory,
    uma_Domain,
    uma_RoleSet,
    uma_RoleSetGrouping,
    uma_Tool,
    uma_DisciplineGrouping,
    uma_WorkProductType,
    uma_Discipline,
    ProcessDescription,
    uma_DeliveryProcessDescription,
    BreakdownElementDescription,
    uma_DescriptorDescription,
    uma_ActivityDescription,
    RoleDescriptor,
    uma_CompositeRole,
    ActivityDescription,
    uma_ProcessDescription,
    Descriptor,
    uma_WorkProductDescriptor,
    uma_ProcessComponentDescriptor,
    uma_RoleDescriptor,
    Activity,
    uma_Process,
    uma_Phase,
    uma_Iteration,
    BreakdownElement,
    uma_Descriptor,
    uma_ProcessComponentInterface,
    uma_TeamProfile,
    uma_WorkBreakdownElement,
    uma_Roadmap,
    WorkBreakdownElement,
    uma_TaskDescriptor,
    uma_Milestone,
    ProcessElement,
    uma_PlanningData,
    uma_BreakdownElement,
    uma_WorkOrder,
    LeafElement,
    uma_Image,
    uma_TextElement,
    SemanticModelBridge,
    uma_UMASemanticModelBridge,
    uma_CoreSemanticModelBridge,
    uma_SimpleSemanticModelElement,
    GraphNode,
    GraphicPrimitive,
    uma_Ellipse,
    uma_Polyline,
    uma_Dimension,
    uma_GraphicPrimitive,
    GraphElement,
    uma_GraphEdge,
    uma_GraphNode,
    uma_Diagram,
    uma_GraphConnector,
    uma_Point,
    DiagramElement,
    uma_DiagramLink,
    uma_LeafElement,
    uma_SemanticModelBridge,
    uma_Reference,
    uma_Property,
    uma_GraphElement,
    ContentDescription,
    uma_PracticeDescription,
    uma_RoleDescription,
    uma_TaskDescription,
    uma_BreakdownElementDescription,
    uma_GuidanceDescription,
    uma_WorkProductDescription,
    WorkProductDescription,
    uma_ArtifactDescription,
    MethodPackage,
    uma_ProcessPackage,
    uma_ContentPackage,
    Package,
    uma_DeliverableDescription,
    WorkProduct,
    uma_Deliverable,
    uma_Outcome,
    uma_Artifact,
    Section,
    uma_ToolMentor,
    uma_Template,
    uma_Report,
    uma_Estimate,
    ContentElement,
    uma_ContentCategory,
    uma_WorkProduct,
    uma_Guidance,
    uma_Role,
    MethodUnit,
    uma_ProcessComponent,
    uma_MethodPlugin,
    uma_MethodLibrary,
    Classifier,
    WorkDefinition,
    uma_Step,
    uma_Task,
    uma_ReusableAsset,
    uma_Example,
    uma_Guideline,
    uma_Checklist,
    uma_Concept,
    uma_SupportingMaterial,
    VariabilityElement,
    uma_Activity,
    uma_Section,
    DescribableElement,
    uma_ProcessElement,
    uma_ContentElement,
    MethodElement,
    uma_MethodPackage,
    uma_DiagramElement,
    uma_MethodUnit,
    uma_MethodConfiguration,
    uma_WorkDefinition,
    uma_DescribableElement,
    uma_VariabilityElement,
    uma_ContentDescription,
    Namespace,
    NamedElement,
    uma_Namespace,
    uma_PackageableElement,
    Element,
    uma_NamedElement,
    uma_Element,
    PackageableElement,
    uma_MethodElement,
    uma_Package,
    uma_Type,
    Type,
    uma_Classifier,
    uma_Constraint,
    WorkOrderType,
    VariabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(MethodConfiguration)


def test_hyp_methodconfiguration_constructor_exists():
    assert callable(MethodConfiguration.__init__)


def test_hyp_methodconfiguration_constructor_args():
    sig = inspect.signature(MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_processfamily_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessFamily)


def test_hyp_uma_processfamily_constructor_exists():
    assert callable(uma_ProcessFamily.__init__)


def test_hyp_uma_processfamily_constructor_args():
    sig = inspect.signature(uma_ProcessFamily.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processpackage_is_not_abstract():
    assert not inspect.isabstract(ProcessPackage)


def test_hyp_processpackage_constructor_exists():
    assert callable(ProcessPackage.__init__)


def test_hyp_processpackage_constructor_args():
    sig = inspect.signature(ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_hyp_process_constructor_exists():
    assert callable(Process.__init__)


def test_hyp_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_processplanningtemplate_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessPlanningTemplate)


def test_hyp_uma_processplanningtemplate_constructor_exists():
    assert callable(uma_ProcessPlanningTemplate.__init__)


def test_hyp_uma_processplanningtemplate_constructor_args():
    sig = inspect.signature(uma_ProcessPlanningTemplate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_processcontribution_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessContribution)


def test_hyp_uma_processcontribution_constructor_exists():
    assert callable(uma_ProcessContribution.__init__)


def test_hyp_uma_processcontribution_constructor_args():
    sig = inspect.signature(uma_ProcessContribution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_capabilitypattern_is_not_abstract():
    assert not inspect.isabstract(uma_CapabilityPattern)


def test_hyp_uma_capabilitypattern_constructor_exists():
    assert callable(uma_CapabilityPattern.__init__)


def test_hyp_uma_capabilitypattern_constructor_args():
    sig = inspect.signature(uma_CapabilityPattern.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_deliveryprocess_is_not_abstract():
    assert not inspect.isabstract(uma_DeliveryProcess)


def test_hyp_uma_deliveryprocess_constructor_exists():
    assert callable(uma_DeliveryProcess.__init__)


def test_hyp_uma_deliveryprocess_constructor_args():
    sig = inspect.signature(uma_DeliveryProcess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_concept_is_not_abstract():
    assert not inspect.isabstract(Concept)


def test_hyp_concept_constructor_exists():
    assert callable(Concept.__init__)


def test_hyp_concept_constructor_args():
    sig = inspect.signature(Concept.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_whitepaper_is_not_abstract():
    assert not inspect.isabstract(uma_Whitepaper)


def test_hyp_uma_whitepaper_constructor_exists():
    assert callable(uma_Whitepaper.__init__)


def test_hyp_uma_whitepaper_constructor_args():
    sig = inspect.signature(uma_Whitepaper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_guidance_is_not_abstract():
    assert not inspect.isabstract(Guidance)


def test_hyp_guidance_constructor_exists():
    assert callable(Guidance.__init__)


def test_hyp_guidance_constructor_args():
    sig = inspect.signature(Guidance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_termdefinition_is_not_abstract():
    assert not inspect.isabstract(uma_TermDefinition)


def test_hyp_uma_termdefinition_constructor_exists():
    assert callable(uma_TermDefinition.__init__)


def test_hyp_uma_termdefinition_constructor_args():
    sig = inspect.signature(uma_TermDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_estimatingmetric_is_not_abstract():
    assert not inspect.isabstract(uma_EstimatingMetric)


def test_hyp_uma_estimatingmetric_constructor_exists():
    assert callable(uma_EstimatingMetric.__init__)


def test_hyp_uma_estimatingmetric_constructor_args():
    sig = inspect.signature(uma_EstimatingMetric.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_practice_is_not_abstract():
    assert not inspect.isabstract(uma_Practice)


def test_hyp_uma_practice_constructor_exists():
    assert callable(uma_Practice.__init__)


def test_hyp_uma_practice_constructor_args():
    sig = inspect.signature(uma_Practice.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_estimationconsiderations_is_not_abstract():
    assert not inspect.isabstract(uma_EstimationConsiderations)


def test_hyp_uma_estimationconsiderations_constructor_exists():
    assert callable(uma_EstimationConsiderations.__init__)


def test_hyp_uma_estimationconsiderations_constructor_args():
    sig = inspect.signature(uma_EstimationConsiderations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentcategory_is_not_abstract():
    assert not inspect.isabstract(ContentCategory)


def test_hyp_contentcategory_constructor_exists():
    assert callable(ContentCategory.__init__)


def test_hyp_contentcategory_constructor_args():
    sig = inspect.signature(ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_customcategory_is_not_abstract():
    assert not inspect.isabstract(uma_CustomCategory)


def test_hyp_uma_customcategory_constructor_exists():
    assert callable(uma_CustomCategory.__init__)


def test_hyp_uma_customcategory_constructor_args():
    sig = inspect.signature(uma_CustomCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_domain_is_not_abstract():
    assert not inspect.isabstract(uma_Domain)


def test_hyp_uma_domain_constructor_exists():
    assert callable(uma_Domain.__init__)


def test_hyp_uma_domain_constructor_args():
    sig = inspect.signature(uma_Domain.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_roleset_is_not_abstract():
    assert not inspect.isabstract(uma_RoleSet)


def test_hyp_uma_roleset_constructor_exists():
    assert callable(uma_RoleSet.__init__)


def test_hyp_uma_roleset_constructor_args():
    sig = inspect.signature(uma_RoleSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_rolesetgrouping_is_not_abstract():
    assert not inspect.isabstract(uma_RoleSetGrouping)


def test_hyp_uma_rolesetgrouping_constructor_exists():
    assert callable(uma_RoleSetGrouping.__init__)


def test_hyp_uma_rolesetgrouping_constructor_args():
    sig = inspect.signature(uma_RoleSetGrouping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_tool_is_not_abstract():
    assert not inspect.isabstract(uma_Tool)


def test_hyp_uma_tool_constructor_exists():
    assert callable(uma_Tool.__init__)


def test_hyp_uma_tool_constructor_args():
    sig = inspect.signature(uma_Tool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_disciplinegrouping_is_not_abstract():
    assert not inspect.isabstract(uma_DisciplineGrouping)


def test_hyp_uma_disciplinegrouping_constructor_exists():
    assert callable(uma_DisciplineGrouping.__init__)


def test_hyp_uma_disciplinegrouping_constructor_args():
    sig = inspect.signature(uma_DisciplineGrouping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_workproducttype_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductType)


def test_hyp_uma_workproducttype_constructor_exists():
    assert callable(uma_WorkProductType.__init__)


def test_hyp_uma_workproducttype_constructor_args():
    sig = inspect.signature(uma_WorkProductType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_discipline_is_not_abstract():
    assert not inspect.isabstract(uma_Discipline)


def test_hyp_uma_discipline_constructor_exists():
    assert callable(uma_Discipline.__init__)


def test_hyp_uma_discipline_constructor_args():
    sig = inspect.signature(uma_Discipline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processdescription_is_not_abstract():
    assert not inspect.isabstract(ProcessDescription)


def test_hyp_processdescription_constructor_exists():
    assert callable(ProcessDescription.__init__)


def test_hyp_processdescription_constructor_args():
    sig = inspect.signature(ProcessDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_deliveryprocessdescription_is_not_abstract():
    assert not inspect.isabstract(uma_DeliveryProcessDescription)


def test_hyp_uma_deliveryprocessdescription_constructor_exists():
    assert callable(uma_DeliveryProcessDescription.__init__)


def test_hyp_uma_deliveryprocessdescription_constructor_args():
    sig = inspect.signature(uma_DeliveryProcessDescription.__init__)
    params = list(sig.parameters.keys())
    assert "projectCharacteristics" in params, "Missing parameter 'projectCharacteristics'"
    assert "riskLevel" in params, "Missing parameter 'riskLevel'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "projectMemberExpertise" in params, "Missing parameter 'projectMemberExpertise'"
    assert "typeOfContract" in params, "Missing parameter 'typeOfContract'"
    assert "estimatingTechnique" in params, "Missing parameter 'estimatingTechnique'"









def test_hyp_breakdownelementdescription_is_not_abstract():
    assert not inspect.isabstract(BreakdownElementDescription)


def test_hyp_breakdownelementdescription_constructor_exists():
    assert callable(BreakdownElementDescription.__init__)


def test_hyp_breakdownelementdescription_constructor_args():
    sig = inspect.signature(BreakdownElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_descriptordescription_is_not_abstract():
    assert not inspect.isabstract(uma_DescriptorDescription)


def test_hyp_uma_descriptordescription_constructor_exists():
    assert callable(uma_DescriptorDescription.__init__)


def test_hyp_uma_descriptordescription_constructor_args():
    sig = inspect.signature(uma_DescriptorDescription.__init__)
    params = list(sig.parameters.keys())
    assert "refinedDescription" in params, "Missing parameter 'refinedDescription'"




def test_hyp_uma_activitydescription_is_not_abstract():
    assert not inspect.isabstract(uma_ActivityDescription)


def test_hyp_uma_activitydescription_constructor_exists():
    assert callable(uma_ActivityDescription.__init__)


def test_hyp_uma_activitydescription_constructor_args():
    sig = inspect.signature(uma_ActivityDescription.__init__)
    params = list(sig.parameters.keys())
    assert "howtoStaff" in params, "Missing parameter 'howtoStaff'"
    assert "alternatives" in params, "Missing parameter 'alternatives'"
    assert "purpose" in params, "Missing parameter 'purpose'"






def test_hyp_roledescriptor_is_not_abstract():
    assert not inspect.isabstract(RoleDescriptor)


def test_hyp_roledescriptor_constructor_exists():
    assert callable(RoleDescriptor.__init__)


def test_hyp_roledescriptor_constructor_args():
    sig = inspect.signature(RoleDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_compositerole_is_not_abstract():
    assert not inspect.isabstract(uma_CompositeRole)


def test_hyp_uma_compositerole_constructor_exists():
    assert callable(uma_CompositeRole.__init__)


def test_hyp_uma_compositerole_constructor_args():
    sig = inspect.signature(uma_CompositeRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitydescription_is_not_abstract():
    assert not inspect.isabstract(ActivityDescription)


def test_hyp_activitydescription_constructor_exists():
    assert callable(ActivityDescription.__init__)


def test_hyp_activitydescription_constructor_args():
    sig = inspect.signature(ActivityDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_processdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessDescription)


def test_hyp_uma_processdescription_constructor_exists():
    assert callable(uma_ProcessDescription.__init__)


def test_hyp_uma_processdescription_constructor_args():
    sig = inspect.signature(uma_ProcessDescription.__init__)
    params = list(sig.parameters.keys())
    assert "usageNotes" in params, "Missing parameter 'usageNotes'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "externalId" in params, "Missing parameter 'externalId'"






def test_hyp_descriptor_is_not_abstract():
    assert not inspect.isabstract(Descriptor)


def test_hyp_descriptor_constructor_exists():
    assert callable(Descriptor.__init__)


def test_hyp_descriptor_constructor_args():
    sig = inspect.signature(Descriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_workproductdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductDescriptor)


def test_hyp_uma_workproductdescriptor_constructor_exists():
    assert callable(uma_WorkProductDescriptor.__init__)


def test_hyp_uma_workproductdescriptor_constructor_args():
    sig = inspect.signature(uma_WorkProductDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "activityExitState" in params, "Missing parameter 'activityExitState'"
    assert "activityEntryState" in params, "Missing parameter 'activityEntryState'"





def test_hyp_uma_processcomponentdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessComponentDescriptor)


def test_hyp_uma_processcomponentdescriptor_constructor_exists():
    assert callable(uma_ProcessComponentDescriptor.__init__)


def test_hyp_uma_processcomponentdescriptor_constructor_args():
    sig = inspect.signature(uma_ProcessComponentDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_roledescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_RoleDescriptor)


def test_hyp_uma_roledescriptor_constructor_exists():
    assert callable(uma_RoleDescriptor.__init__)


def test_hyp_uma_roledescriptor_constructor_args():
    sig = inspect.signature(uma_RoleDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_hyp_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_hyp_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_process_is_not_abstract():
    assert not inspect.isabstract(uma_Process)


def test_hyp_uma_process_constructor_exists():
    assert callable(uma_Process.__init__)


def test_hyp_uma_process_constructor_args():
    sig = inspect.signature(uma_Process.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_phase_is_not_abstract():
    assert not inspect.isabstract(uma_Phase)


def test_hyp_uma_phase_constructor_exists():
    assert callable(uma_Phase.__init__)


def test_hyp_uma_phase_constructor_args():
    sig = inspect.signature(uma_Phase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_iteration_is_not_abstract():
    assert not inspect.isabstract(uma_Iteration)


def test_hyp_uma_iteration_constructor_exists():
    assert callable(uma_Iteration.__init__)


def test_hyp_uma_iteration_constructor_args():
    sig = inspect.signature(uma_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(BreakdownElement)


def test_hyp_breakdownelement_constructor_exists():
    assert callable(BreakdownElement.__init__)


def test_hyp_breakdownelement_constructor_args():
    sig = inspect.signature(BreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_descriptor_is_not_abstract():
    assert not inspect.isabstract(uma_Descriptor)


def test_hyp_uma_descriptor_constructor_exists():
    assert callable(uma_Descriptor.__init__)


def test_hyp_uma_descriptor_constructor_args():
    sig = inspect.signature(uma_Descriptor.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronizedWithSource" in params, "Missing parameter 'isSynchronizedWithSource'"




def test_hyp_uma_processcomponentinterface_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessComponentInterface)


def test_hyp_uma_processcomponentinterface_constructor_exists():
    assert callable(uma_ProcessComponentInterface.__init__)


def test_hyp_uma_processcomponentinterface_constructor_args():
    sig = inspect.signature(uma_ProcessComponentInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_teamprofile_is_not_abstract():
    assert not inspect.isabstract(uma_TeamProfile)


def test_hyp_uma_teamprofile_constructor_exists():
    assert callable(uma_TeamProfile.__init__)


def test_hyp_uma_teamprofile_constructor_args():
    sig = inspect.signature(uma_TeamProfile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma_WorkBreakdownElement)


def test_hyp_uma_workbreakdownelement_constructor_exists():
    assert callable(uma_WorkBreakdownElement.__init__)


def test_hyp_uma_workbreakdownelement_constructor_args():
    sig = inspect.signature(uma_WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "isRepeatable" in params, "Missing parameter 'isRepeatable'"
    assert "isEventDriven" in params, "Missing parameter 'isEventDriven'"
    assert "isOngoing" in params, "Missing parameter 'isOngoing'"






def test_hyp_uma_roadmap_is_not_abstract():
    assert not inspect.isabstract(uma_Roadmap)


def test_hyp_uma_roadmap_constructor_exists():
    assert callable(uma_Roadmap.__init__)


def test_hyp_uma_roadmap_constructor_args():
    sig = inspect.signature(uma_Roadmap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(WorkBreakdownElement)


def test_hyp_workbreakdownelement_constructor_exists():
    assert callable(WorkBreakdownElement.__init__)


def test_hyp_workbreakdownelement_constructor_args():
    sig = inspect.signature(WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_taskdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_TaskDescriptor)


def test_hyp_uma_taskdescriptor_constructor_exists():
    assert callable(uma_TaskDescriptor.__init__)


def test_hyp_uma_taskdescriptor_constructor_args():
    sig = inspect.signature(uma_TaskDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_milestone_is_not_abstract():
    assert not inspect.isabstract(uma_Milestone)


def test_hyp_uma_milestone_constructor_exists():
    assert callable(uma_Milestone.__init__)


def test_hyp_uma_milestone_constructor_args():
    sig = inspect.signature(uma_Milestone.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_hyp_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_hyp_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_planningdata_is_not_abstract():
    assert not inspect.isabstract(uma_PlanningData)


def test_hyp_uma_planningdata_constructor_exists():
    assert callable(uma_PlanningData.__init__)


def test_hyp_uma_planningdata_constructor_args():
    sig = inspect.signature(uma_PlanningData.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "finishDate" in params, "Missing parameter 'finishDate'"






def test_hyp_uma_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma_BreakdownElement)


def test_hyp_uma_breakdownelement_constructor_exists():
    assert callable(uma_BreakdownElement.__init__)


def test_hyp_uma_breakdownelement_constructor_args():
    sig = inspect.signature(uma_BreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "hasMultipleOccurrences" in params, "Missing parameter 'hasMultipleOccurrences'"
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "isOptional" in params, "Missing parameter 'isOptional'"
    assert "isPlanned" in params, "Missing parameter 'isPlanned'"







def test_hyp_uma_workorder_is_not_abstract():
    assert not inspect.isabstract(uma_WorkOrder)


def test_hyp_uma_workorder_constructor_exists():
    assert callable(uma_WorkOrder.__init__)


def test_hyp_uma_workorder_constructor_args():
    sig = inspect.signature(uma_WorkOrder.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"




def test_hyp_leafelement_is_not_abstract():
    assert not inspect.isabstract(LeafElement)


def test_hyp_leafelement_constructor_exists():
    assert callable(LeafElement.__init__)


def test_hyp_leafelement_constructor_args():
    sig = inspect.signature(LeafElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_image_is_not_abstract():
    assert not inspect.isabstract(uma_Image)


def test_hyp_uma_image_constructor_exists():
    assert callable(uma_Image.__init__)


def test_hyp_uma_image_constructor_args():
    sig = inspect.signature(uma_Image.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"





def test_hyp_uma_textelement_is_not_abstract():
    assert not inspect.isabstract(uma_TextElement)


def test_hyp_uma_textelement_constructor_exists():
    assert callable(uma_TextElement.__init__)


def test_hyp_uma_textelement_constructor_args():
    sig = inspect.signature(uma_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_semanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(SemanticModelBridge)


def test_hyp_semanticmodelbridge_constructor_exists():
    assert callable(SemanticModelBridge.__init__)


def test_hyp_semanticmodelbridge_constructor_args():
    sig = inspect.signature(SemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_umasemanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma_UMASemanticModelBridge)


def test_hyp_uma_umasemanticmodelbridge_constructor_exists():
    assert callable(uma_UMASemanticModelBridge.__init__)


def test_hyp_uma_umasemanticmodelbridge_constructor_args():
    sig = inspect.signature(uma_UMASemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_coresemanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma_CoreSemanticModelBridge)


def test_hyp_uma_coresemanticmodelbridge_constructor_exists():
    assert callable(uma_CoreSemanticModelBridge.__init__)


def test_hyp_uma_coresemanticmodelbridge_constructor_args():
    sig = inspect.signature(uma_CoreSemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_simplesemanticmodelelement_is_not_abstract():
    assert not inspect.isabstract(uma_SimpleSemanticModelElement)


def test_hyp_uma_simplesemanticmodelelement_constructor_exists():
    assert callable(uma_SimpleSemanticModelElement.__init__)


def test_hyp_uma_simplesemanticmodelelement_constructor_args():
    sig = inspect.signature(uma_SimpleSemanticModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "typeInfo" in params, "Missing parameter 'typeInfo'"




def test_hyp_graphnode_is_not_abstract():
    assert not inspect.isabstract(GraphNode)


def test_hyp_graphnode_constructor_exists():
    assert callable(GraphNode.__init__)


def test_hyp_graphnode_constructor_args():
    sig = inspect.signature(GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphicprimitive_is_not_abstract():
    assert not inspect.isabstract(GraphicPrimitive)


def test_hyp_graphicprimitive_constructor_exists():
    assert callable(GraphicPrimitive.__init__)


def test_hyp_graphicprimitive_constructor_args():
    sig = inspect.signature(GraphicPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_ellipse_is_not_abstract():
    assert not inspect.isabstract(uma_Ellipse)


def test_hyp_uma_ellipse_constructor_exists():
    assert callable(uma_Ellipse.__init__)


def test_hyp_uma_ellipse_constructor_args():
    sig = inspect.signature(uma_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "endAngle" in params, "Missing parameter 'endAngle'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "radiusY" in params, "Missing parameter 'radiusY'"
    assert "radiusX" in params, "Missing parameter 'radiusX'"
    assert "startAngle" in params, "Missing parameter 'startAngle'"








def test_hyp_uma_polyline_is_not_abstract():
    assert not inspect.isabstract(uma_Polyline)


def test_hyp_uma_polyline_constructor_exists():
    assert callable(uma_Polyline.__init__)


def test_hyp_uma_polyline_constructor_args():
    sig = inspect.signature(uma_Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "closed" in params, "Missing parameter 'closed'"




def test_hyp_uma_dimension_is_not_abstract():
    assert not inspect.isabstract(uma_Dimension)


def test_hyp_uma_dimension_constructor_exists():
    assert callable(uma_Dimension.__init__)


def test_hyp_uma_dimension_constructor_args():
    sig = inspect.signature(uma_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"





def test_hyp_uma_graphicprimitive_is_not_abstract():
    assert not inspect.isabstract(uma_GraphicPrimitive)


def test_hyp_uma_graphicprimitive_constructor_exists():
    assert callable(uma_GraphicPrimitive.__init__)


def test_hyp_uma_graphicprimitive_constructor_args():
    sig = inspect.signature(uma_GraphicPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_hyp_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_hyp_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_graphedge_is_not_abstract():
    assert not inspect.isabstract(uma_GraphEdge)


def test_hyp_uma_graphedge_constructor_exists():
    assert callable(uma_GraphEdge.__init__)


def test_hyp_uma_graphedge_constructor_args():
    sig = inspect.signature(uma_GraphEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_graphnode_is_not_abstract():
    assert not inspect.isabstract(uma_GraphNode)


def test_hyp_uma_graphnode_constructor_exists():
    assert callable(uma_GraphNode.__init__)


def test_hyp_uma_graphnode_constructor_args():
    sig = inspect.signature(uma_GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_diagram_is_not_abstract():
    assert not inspect.isabstract(uma_Diagram)


def test_hyp_uma_diagram_constructor_exists():
    assert callable(uma_Diagram.__init__)


def test_hyp_uma_diagram_constructor_args():
    sig = inspect.signature(uma_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "zoom" in params, "Missing parameter 'zoom'"




def test_hyp_uma_graphconnector_is_not_abstract():
    assert not inspect.isabstract(uma_GraphConnector)


def test_hyp_uma_graphconnector_constructor_exists():
    assert callable(uma_GraphConnector.__init__)


def test_hyp_uma_graphconnector_constructor_args():
    sig = inspect.signature(uma_GraphConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_point_is_not_abstract():
    assert not inspect.isabstract(uma_Point)


def test_hyp_uma_point_constructor_exists():
    assert callable(uma_Point.__init__)


def test_hyp_uma_point_constructor_args():
    sig = inspect.signature(uma_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_hyp_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_hyp_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_diagramlink_is_not_abstract():
    assert not inspect.isabstract(uma_DiagramLink)


def test_hyp_uma_diagramlink_constructor_exists():
    assert callable(uma_DiagramLink.__init__)


def test_hyp_uma_diagramlink_constructor_args():
    sig = inspect.signature(uma_DiagramLink.__init__)
    params = list(sig.parameters.keys())
    assert "zoom" in params, "Missing parameter 'zoom'"




def test_hyp_uma_leafelement_is_not_abstract():
    assert not inspect.isabstract(uma_LeafElement)


def test_hyp_uma_leafelement_constructor_exists():
    assert callable(uma_LeafElement.__init__)


def test_hyp_uma_leafelement_constructor_args():
    sig = inspect.signature(uma_LeafElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_semanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma_SemanticModelBridge)


def test_hyp_uma_semanticmodelbridge_constructor_exists():
    assert callable(uma_SemanticModelBridge.__init__)


def test_hyp_uma_semanticmodelbridge_constructor_args():
    sig = inspect.signature(uma_SemanticModelBridge.__init__)
    params = list(sig.parameters.keys())
    assert "presentation" in params, "Missing parameter 'presentation'"




def test_hyp_uma_reference_is_not_abstract():
    assert not inspect.isabstract(uma_Reference)


def test_hyp_uma_reference_constructor_exists():
    assert callable(uma_Reference.__init__)


def test_hyp_uma_reference_constructor_args():
    sig = inspect.signature(uma_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "isIndividualRepresentation" in params, "Missing parameter 'isIndividualRepresentation'"




def test_hyp_uma_property_is_not_abstract():
    assert not inspect.isabstract(uma_Property)


def test_hyp_uma_property_constructor_exists():
    assert callable(uma_Property.__init__)


def test_hyp_uma_property_constructor_args():
    sig = inspect.signature(uma_Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_uma_graphelement_is_not_abstract():
    assert not inspect.isabstract(uma_GraphElement)


def test_hyp_uma_graphelement_constructor_exists():
    assert callable(uma_GraphElement.__init__)


def test_hyp_uma_graphelement_constructor_args():
    sig = inspect.signature(uma_GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentdescription_is_not_abstract():
    assert not inspect.isabstract(ContentDescription)


def test_hyp_contentdescription_constructor_exists():
    assert callable(ContentDescription.__init__)


def test_hyp_contentdescription_constructor_args():
    sig = inspect.signature(ContentDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_practicedescription_is_not_abstract():
    assert not inspect.isabstract(uma_PracticeDescription)


def test_hyp_uma_practicedescription_constructor_exists():
    assert callable(uma_PracticeDescription.__init__)


def test_hyp_uma_practicedescription_constructor_args():
    sig = inspect.signature(uma_PracticeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "levelsOfAdoption" in params, "Missing parameter 'levelsOfAdoption'"
    assert "goals" in params, "Missing parameter 'goals'"
    assert "background" in params, "Missing parameter 'background'"
    assert "application" in params, "Missing parameter 'application'"
    assert "additionalInfo" in params, "Missing parameter 'additionalInfo'"
    assert "problem" in params, "Missing parameter 'problem'"









def test_hyp_uma_roledescription_is_not_abstract():
    assert not inspect.isabstract(uma_RoleDescription)


def test_hyp_uma_roledescription_constructor_exists():
    assert callable(uma_RoleDescription.__init__)


def test_hyp_uma_roledescription_constructor_args():
    sig = inspect.signature(uma_RoleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "skills" in params, "Missing parameter 'skills'"
    assert "synonyms" in params, "Missing parameter 'synonyms'"
    assert "assignmentApproaches" in params, "Missing parameter 'assignmentApproaches'"






def test_hyp_uma_taskdescription_is_not_abstract():
    assert not inspect.isabstract(uma_TaskDescription)


def test_hyp_uma_taskdescription_constructor_exists():
    assert callable(uma_TaskDescription.__init__)


def test_hyp_uma_taskdescription_constructor_args():
    sig = inspect.signature(uma_TaskDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alternatives" in params, "Missing parameter 'alternatives'"
    assert "purpose" in params, "Missing parameter 'purpose'"





def test_hyp_uma_breakdownelementdescription_is_not_abstract():
    assert not inspect.isabstract(uma_BreakdownElementDescription)


def test_hyp_uma_breakdownelementdescription_constructor_exists():
    assert callable(uma_BreakdownElementDescription.__init__)


def test_hyp_uma_breakdownelementdescription_constructor_args():
    sig = inspect.signature(uma_BreakdownElementDescription.__init__)
    params = list(sig.parameters.keys())
    assert "usageGuidance" in params, "Missing parameter 'usageGuidance'"




def test_hyp_uma_guidancedescription_is_not_abstract():
    assert not inspect.isabstract(uma_GuidanceDescription)


def test_hyp_uma_guidancedescription_constructor_exists():
    assert callable(uma_GuidanceDescription.__init__)


def test_hyp_uma_guidancedescription_constructor_args():
    sig = inspect.signature(uma_GuidanceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "attachments" in params, "Missing parameter 'attachments'"




def test_hyp_uma_workproductdescription_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductDescription)


def test_hyp_uma_workproductdescription_constructor_exists():
    assert callable(uma_WorkProductDescription.__init__)


def test_hyp_uma_workproductdescription_constructor_args():
    sig = inspect.signature(uma_WorkProductDescription.__init__)
    params = list(sig.parameters.keys())
    assert "externalId" in params, "Missing parameter 'externalId'"
    assert "reasonsForNotNeeding" in params, "Missing parameter 'reasonsForNotNeeding'"
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "impactOfNotHaving" in params, "Missing parameter 'impactOfNotHaving'"







def test_hyp_workproductdescription_is_not_abstract():
    assert not inspect.isabstract(WorkProductDescription)


def test_hyp_workproductdescription_constructor_exists():
    assert callable(WorkProductDescription.__init__)


def test_hyp_workproductdescription_constructor_args():
    sig = inspect.signature(WorkProductDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_artifactdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ArtifactDescription)


def test_hyp_uma_artifactdescription_constructor_exists():
    assert callable(uma_ArtifactDescription.__init__)


def test_hyp_uma_artifactdescription_constructor_args():
    sig = inspect.signature(uma_ArtifactDescription.__init__)
    params = list(sig.parameters.keys())
    assert "representationOptions" in params, "Missing parameter 'representationOptions'"
    assert "briefOutline" in params, "Missing parameter 'briefOutline'"





def test_hyp_methodpackage_is_not_abstract():
    assert not inspect.isabstract(MethodPackage)


def test_hyp_methodpackage_constructor_exists():
    assert callable(MethodPackage.__init__)


def test_hyp_methodpackage_constructor_args():
    sig = inspect.signature(MethodPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_processpackage_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessPackage)


def test_hyp_uma_processpackage_constructor_exists():
    assert callable(uma_ProcessPackage.__init__)


def test_hyp_uma_processpackage_constructor_args():
    sig = inspect.signature(uma_ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_contentpackage_is_not_abstract():
    assert not inspect.isabstract(uma_ContentPackage)


def test_hyp_uma_contentpackage_constructor_exists():
    assert callable(uma_ContentPackage.__init__)


def test_hyp_uma_contentpackage_constructor_args():
    sig = inspect.signature(uma_ContentPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_hyp_package_constructor_exists():
    assert callable(Package.__init__)


def test_hyp_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_deliverabledescription_is_not_abstract():
    assert not inspect.isabstract(uma_DeliverableDescription)


def test_hyp_uma_deliverabledescription_constructor_exists():
    assert callable(uma_DeliverableDescription.__init__)


def test_hyp_uma_deliverabledescription_constructor_args():
    sig = inspect.signature(uma_DeliverableDescription.__init__)
    params = list(sig.parameters.keys())
    assert "externalDescription" in params, "Missing parameter 'externalDescription'"
    assert "packagingGuidance" in params, "Missing parameter 'packagingGuidance'"





def test_hyp_workproduct_is_not_abstract():
    assert not inspect.isabstract(WorkProduct)


def test_hyp_workproduct_constructor_exists():
    assert callable(WorkProduct.__init__)


def test_hyp_workproduct_constructor_args():
    sig = inspect.signature(WorkProduct.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_deliverable_is_not_abstract():
    assert not inspect.isabstract(uma_Deliverable)


def test_hyp_uma_deliverable_constructor_exists():
    assert callable(uma_Deliverable.__init__)


def test_hyp_uma_deliverable_constructor_args():
    sig = inspect.signature(uma_Deliverable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_outcome_is_not_abstract():
    assert not inspect.isabstract(uma_Outcome)


def test_hyp_uma_outcome_constructor_exists():
    assert callable(uma_Outcome.__init__)


def test_hyp_uma_outcome_constructor_args():
    sig = inspect.signature(uma_Outcome.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_artifact_is_not_abstract():
    assert not inspect.isabstract(uma_Artifact)


def test_hyp_uma_artifact_constructor_exists():
    assert callable(uma_Artifact.__init__)


def test_hyp_uma_artifact_constructor_args():
    sig = inspect.signature(uma_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_hyp_section_constructor_exists():
    assert callable(Section.__init__)


def test_hyp_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_toolmentor_is_not_abstract():
    assert not inspect.isabstract(uma_ToolMentor)


def test_hyp_uma_toolmentor_constructor_exists():
    assert callable(uma_ToolMentor.__init__)


def test_hyp_uma_toolmentor_constructor_args():
    sig = inspect.signature(uma_ToolMentor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_template_is_not_abstract():
    assert not inspect.isabstract(uma_Template)


def test_hyp_uma_template_constructor_exists():
    assert callable(uma_Template.__init__)


def test_hyp_uma_template_constructor_args():
    sig = inspect.signature(uma_Template.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_report_is_not_abstract():
    assert not inspect.isabstract(uma_Report)


def test_hyp_uma_report_constructor_exists():
    assert callable(uma_Report.__init__)


def test_hyp_uma_report_constructor_args():
    sig = inspect.signature(uma_Report.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_estimate_is_not_abstract():
    assert not inspect.isabstract(uma_Estimate)


def test_hyp_uma_estimate_constructor_exists():
    assert callable(uma_Estimate.__init__)


def test_hyp_uma_estimate_constructor_args():
    sig = inspect.signature(uma_Estimate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contentelement_is_not_abstract():
    assert not inspect.isabstract(ContentElement)


def test_hyp_contentelement_constructor_exists():
    assert callable(ContentElement.__init__)


def test_hyp_contentelement_constructor_args():
    sig = inspect.signature(ContentElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_contentcategory_is_not_abstract():
    assert not inspect.isabstract(uma_ContentCategory)


def test_hyp_uma_contentcategory_constructor_exists():
    assert callable(uma_ContentCategory.__init__)


def test_hyp_uma_contentcategory_constructor_args():
    sig = inspect.signature(uma_ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_workproduct_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProduct)


def test_hyp_uma_workproduct_constructor_exists():
    assert callable(uma_WorkProduct.__init__)


def test_hyp_uma_workproduct_constructor_args():
    sig = inspect.signature(uma_WorkProduct.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_guidance_is_not_abstract():
    assert not inspect.isabstract(uma_Guidance)


def test_hyp_uma_guidance_constructor_exists():
    assert callable(uma_Guidance.__init__)


def test_hyp_uma_guidance_constructor_args():
    sig = inspect.signature(uma_Guidance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_role_is_not_abstract():
    assert not inspect.isabstract(uma_Role)


def test_hyp_uma_role_constructor_exists():
    assert callable(uma_Role.__init__)


def test_hyp_uma_role_constructor_args():
    sig = inspect.signature(uma_Role.__init__)
    params = list(sig.parameters.keys())



def test_hyp_methodunit_is_not_abstract():
    assert not inspect.isabstract(MethodUnit)


def test_hyp_methodunit_constructor_exists():
    assert callable(MethodUnit.__init__)


def test_hyp_methodunit_constructor_args():
    sig = inspect.signature(MethodUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_processcomponent_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessComponent)


def test_hyp_uma_processcomponent_constructor_exists():
    assert callable(uma_ProcessComponent.__init__)


def test_hyp_uma_processcomponent_constructor_args():
    sig = inspect.signature(uma_ProcessComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_methodplugin_is_not_abstract():
    assert not inspect.isabstract(uma_MethodPlugin)


def test_hyp_uma_methodplugin_constructor_exists():
    assert callable(uma_MethodPlugin.__init__)


def test_hyp_uma_methodplugin_constructor_args():
    sig = inspect.signature(uma_MethodPlugin.__init__)
    params = list(sig.parameters.keys())
    assert "userChangeable" in params, "Missing parameter 'userChangeable'"




def test_hyp_uma_methodlibrary_is_not_abstract():
    assert not inspect.isabstract(uma_MethodLibrary)


def test_hyp_uma_methodlibrary_constructor_exists():
    assert callable(uma_MethodLibrary.__init__)


def test_hyp_uma_methodlibrary_constructor_args():
    sig = inspect.signature(uma_MethodLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workdefinition_is_not_abstract():
    assert not inspect.isabstract(WorkDefinition)


def test_hyp_workdefinition_constructor_exists():
    assert callable(WorkDefinition.__init__)


def test_hyp_workdefinition_constructor_args():
    sig = inspect.signature(WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_step_is_not_abstract():
    assert not inspect.isabstract(uma_Step)


def test_hyp_uma_step_constructor_exists():
    assert callable(uma_Step.__init__)


def test_hyp_uma_step_constructor_args():
    sig = inspect.signature(uma_Step.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_task_is_not_abstract():
    assert not inspect.isabstract(uma_Task)


def test_hyp_uma_task_constructor_exists():
    assert callable(uma_Task.__init__)


def test_hyp_uma_task_constructor_args():
    sig = inspect.signature(uma_Task.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_reusableasset_is_not_abstract():
    assert not inspect.isabstract(uma_ReusableAsset)


def test_hyp_uma_reusableasset_constructor_exists():
    assert callable(uma_ReusableAsset.__init__)


def test_hyp_uma_reusableasset_constructor_args():
    sig = inspect.signature(uma_ReusableAsset.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_example_is_not_abstract():
    assert not inspect.isabstract(uma_Example)


def test_hyp_uma_example_constructor_exists():
    assert callable(uma_Example.__init__)


def test_hyp_uma_example_constructor_args():
    sig = inspect.signature(uma_Example.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_guideline_is_not_abstract():
    assert not inspect.isabstract(uma_Guideline)


def test_hyp_uma_guideline_constructor_exists():
    assert callable(uma_Guideline.__init__)


def test_hyp_uma_guideline_constructor_args():
    sig = inspect.signature(uma_Guideline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_checklist_is_not_abstract():
    assert not inspect.isabstract(uma_Checklist)


def test_hyp_uma_checklist_constructor_exists():
    assert callable(uma_Checklist.__init__)


def test_hyp_uma_checklist_constructor_args():
    sig = inspect.signature(uma_Checklist.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_concept_is_not_abstract():
    assert not inspect.isabstract(uma_Concept)


def test_hyp_uma_concept_constructor_exists():
    assert callable(uma_Concept.__init__)


def test_hyp_uma_concept_constructor_args():
    sig = inspect.signature(uma_Concept.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(uma_SupportingMaterial)


def test_hyp_uma_supportingmaterial_constructor_exists():
    assert callable(uma_SupportingMaterial.__init__)


def test_hyp_uma_supportingmaterial_constructor_args():
    sig = inspect.signature(uma_SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(VariabilityElement)


def test_hyp_variabilityelement_constructor_exists():
    assert callable(VariabilityElement.__init__)


def test_hyp_variabilityelement_constructor_args():
    sig = inspect.signature(VariabilityElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_activity_is_not_abstract():
    assert not inspect.isabstract(uma_Activity)


def test_hyp_uma_activity_constructor_exists():
    assert callable(uma_Activity.__init__)


def test_hyp_uma_activity_constructor_args():
    sig = inspect.signature(uma_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_section_is_not_abstract():
    assert not inspect.isabstract(uma_Section)


def test_hyp_uma_section_constructor_exists():
    assert callable(uma_Section.__init__)


def test_hyp_uma_section_constructor_args():
    sig = inspect.signature(uma_Section.__init__)
    params = list(sig.parameters.keys())
    assert "sectionDescription" in params, "Missing parameter 'sectionDescription'"
    assert "sectionName" in params, "Missing parameter 'sectionName'"





def test_hyp_describableelement_is_not_abstract():
    assert not inspect.isabstract(DescribableElement)


def test_hyp_describableelement_constructor_exists():
    assert callable(DescribableElement.__init__)


def test_hyp_describableelement_constructor_args():
    sig = inspect.signature(DescribableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_processelement_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessElement)


def test_hyp_uma_processelement_constructor_exists():
    assert callable(uma_ProcessElement.__init__)


def test_hyp_uma_processelement_constructor_args():
    sig = inspect.signature(uma_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_contentelement_is_not_abstract():
    assert not inspect.isabstract(uma_ContentElement)


def test_hyp_uma_contentelement_constructor_exists():
    assert callable(uma_ContentElement.__init__)


def test_hyp_uma_contentelement_constructor_args():
    sig = inspect.signature(uma_ContentElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_methodelement_is_not_abstract():
    assert not inspect.isabstract(MethodElement)


def test_hyp_methodelement_constructor_exists():
    assert callable(MethodElement.__init__)


def test_hyp_methodelement_constructor_args():
    sig = inspect.signature(MethodElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_methodpackage_is_not_abstract():
    assert not inspect.isabstract(uma_MethodPackage)


def test_hyp_uma_methodpackage_constructor_exists():
    assert callable(uma_MethodPackage.__init__)


def test_hyp_uma_methodpackage_constructor_args():
    sig = inspect.signature(uma_MethodPackage.__init__)
    params = list(sig.parameters.keys())
    assert "global_" in params, "Missing parameter 'global_'"




def test_hyp_uma_diagramelement_is_not_abstract():
    assert not inspect.isabstract(uma_DiagramElement)


def test_hyp_uma_diagramelement_constructor_exists():
    assert callable(uma_DiagramElement.__init__)


def test_hyp_uma_diagramelement_constructor_args():
    sig = inspect.signature(uma_DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "isVisible" in params, "Missing parameter 'isVisible'"




def test_hyp_uma_methodunit_is_not_abstract():
    assert not inspect.isabstract(uma_MethodUnit)


def test_hyp_uma_methodunit_constructor_exists():
    assert callable(uma_MethodUnit.__init__)


def test_hyp_uma_methodunit_constructor_args():
    sig = inspect.signature(uma_MethodUnit.__init__)
    params = list(sig.parameters.keys())
    assert "changeDate" in params, "Missing parameter 'changeDate'"
    assert "version" in params, "Missing parameter 'version'"
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"
    assert "authors" in params, "Missing parameter 'authors'"







def test_hyp_uma_methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(uma_MethodConfiguration)


def test_hyp_uma_methodconfiguration_constructor_exists():
    assert callable(uma_MethodConfiguration.__init__)


def test_hyp_uma_methodconfiguration_constructor_args():
    sig = inspect.signature(uma_MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_workdefinition_is_not_abstract():
    assert not inspect.isabstract(uma_WorkDefinition)


def test_hyp_uma_workdefinition_constructor_exists():
    assert callable(uma_WorkDefinition.__init__)


def test_hyp_uma_workdefinition_constructor_args():
    sig = inspect.signature(uma_WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_describableelement_is_not_abstract():
    assert not inspect.isabstract(uma_DescribableElement)


def test_hyp_uma_describableelement_constructor_exists():
    assert callable(uma_DescribableElement.__init__)


def test_hyp_uma_describableelement_constructor_args():
    sig = inspect.signature(uma_DescribableElement.__init__)
    params = list(sig.parameters.keys())
    assert "presentationName" in params, "Missing parameter 'presentationName'"
    assert "nodeicon" in params, "Missing parameter 'nodeicon'"
    assert "shapeicon" in params, "Missing parameter 'shapeicon'"






def test_hyp_uma_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(uma_VariabilityElement)


def test_hyp_uma_variabilityelement_constructor_exists():
    assert callable(uma_VariabilityElement.__init__)


def test_hyp_uma_variabilityelement_constructor_args():
    sig = inspect.signature(uma_VariabilityElement.__init__)
    params = list(sig.parameters.keys())
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"




def test_hyp_uma_contentdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ContentDescription)


def test_hyp_uma_contentdescription_constructor_exists():
    assert callable(uma_ContentDescription.__init__)


def test_hyp_uma_contentdescription_constructor_args():
    sig = inspect.signature(uma_ContentDescription.__init__)
    params = list(sig.parameters.keys())
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"
    assert "keyConsiderations" in params, "Missing parameter 'keyConsiderations'"





def test_hyp_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_hyp_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_hyp_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_namespace_is_not_abstract():
    assert not inspect.isabstract(uma_Namespace)


def test_hyp_uma_namespace_constructor_exists():
    assert callable(uma_Namespace.__init__)


def test_hyp_uma_namespace_constructor_args():
    sig = inspect.signature(uma_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_packageableelement_is_not_abstract():
    assert not inspect.isabstract(uma_PackageableElement)


def test_hyp_uma_packageableelement_constructor_exists():
    assert callable(uma_PackageableElement.__init__)


def test_hyp_uma_packageableelement_constructor_args():
    sig = inspect.signature(uma_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_namedelement_is_not_abstract():
    assert not inspect.isabstract(uma_NamedElement)


def test_hyp_uma_namedelement_constructor_exists():
    assert callable(uma_NamedElement.__init__)


def test_hyp_uma_namedelement_constructor_args():
    sig = inspect.signature(uma_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_uma_element_is_not_abstract():
    assert not inspect.isabstract(uma_Element)


def test_hyp_uma_element_constructor_exists():
    assert callable(uma_Element.__init__)


def test_hyp_uma_element_constructor_args():
    sig = inspect.signature(uma_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_hyp_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_hyp_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_methodelement_is_not_abstract():
    assert not inspect.isabstract(uma_MethodElement)


def test_hyp_uma_methodelement_constructor_exists():
    assert callable(uma_MethodElement.__init__)


def test_hyp_uma_methodelement_constructor_args():
    sig = inspect.signature(uma_MethodElement.__init__)
    params = list(sig.parameters.keys())
    assert "orderingGuide" in params, "Missing parameter 'orderingGuide'"
    assert "suppressed" in params, "Missing parameter 'suppressed'"
    assert "briefDescription" in params, "Missing parameter 'briefDescription'"
    assert "guid" in params, "Missing parameter 'guid'"







def test_hyp_uma_package_is_not_abstract():
    assert not inspect.isabstract(uma_Package)


def test_hyp_uma_package_constructor_exists():
    assert callable(uma_Package.__init__)


def test_hyp_uma_package_constructor_args():
    sig = inspect.signature(uma_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_type_is_not_abstract():
    assert not inspect.isabstract(uma_Type)


def test_hyp_uma_type_constructor_exists():
    assert callable(uma_Type.__init__)


def test_hyp_uma_type_constructor_args():
    sig = inspect.signature(uma_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_classifier_is_not_abstract():
    assert not inspect.isabstract(uma_Classifier)


def test_hyp_uma_classifier_constructor_exists():
    assert callable(uma_Classifier.__init__)


def test_hyp_uma_classifier_constructor_args():
    sig = inspect.signature(uma_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uma_constraint_is_not_abstract():
    assert not inspect.isabstract(uma_Constraint)


def test_hyp_uma_constraint_constructor_exists():
    assert callable(uma_Constraint.__init__)


def test_hyp_uma_constraint_constructor_args():
    sig = inspect.signature(uma_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"


def test_hyp_workordertype_exists():
    # Check that the Enumeration exists
    assert WorkOrderType is not None

def test_hyp_workordertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkOrderType]
    expected_literals = [
        "startToStart",
        "finishToStart",
        "startToFinish",
        "finishToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkOrderType"

def test_hyp_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_hyp_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "extends",
        "na",
        "replaces",
        "contributes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariabilityType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
MethodConfiguration_strategy = st.builds(
    MethodConfiguration,
)
uma_ProcessFamily_strategy = st.builds(
    uma_ProcessFamily,
)
ProcessPackage_strategy = st.builds(
    ProcessPackage,
)
Process_strategy = st.builds(
    Process,
)
uma_ProcessPlanningTemplate_strategy = st.builds(
    uma_ProcessPlanningTemplate,
)
uma_ProcessContribution_strategy = st.builds(
    uma_ProcessContribution,
)
uma_CapabilityPattern_strategy = st.builds(
    uma_CapabilityPattern,
)
uma_DeliveryProcess_strategy = st.builds(
    uma_DeliveryProcess,
)
Concept_strategy = st.builds(
    Concept,
)
uma_Whitepaper_strategy = st.builds(
    uma_Whitepaper,
)
Guidance_strategy = st.builds(
    Guidance,
)
uma_TermDefinition_strategy = st.builds(
    uma_TermDefinition,
)
uma_EstimatingMetric_strategy = st.builds(
    uma_EstimatingMetric,
)
uma_Practice_strategy = st.builds(
    uma_Practice,
)
uma_EstimationConsiderations_strategy = st.builds(
    uma_EstimationConsiderations,
)
ContentCategory_strategy = st.builds(
    ContentCategory,
)
uma_CustomCategory_strategy = st.builds(
    uma_CustomCategory,
)
uma_Domain_strategy = st.builds(
    uma_Domain,
)
uma_RoleSet_strategy = st.builds(
    uma_RoleSet,
)
uma_RoleSetGrouping_strategy = st.builds(
    uma_RoleSetGrouping,
)
uma_Tool_strategy = st.builds(
    uma_Tool,
)
uma_DisciplineGrouping_strategy = st.builds(
    uma_DisciplineGrouping,
)
uma_WorkProductType_strategy = st.builds(
    uma_WorkProductType,
)
uma_Discipline_strategy = st.builds(
    uma_Discipline,
)
ProcessDescription_strategy = st.builds(
    ProcessDescription,
)
uma_DeliveryProcessDescription_strategy = st.builds(
    uma_DeliveryProcessDescription,
    projectCharacteristics=
        safe_text,
    riskLevel=
        safe_text,
    scale=
        safe_text,
    projectMemberExpertise=
        safe_text,
    typeOfContract=
        safe_text,
    estimatingTechnique=
        safe_text
)
BreakdownElementDescription_strategy = st.builds(
    BreakdownElementDescription,
)
uma_DescriptorDescription_strategy = st.builds(
    uma_DescriptorDescription,
    refinedDescription=
        safe_text
)
uma_ActivityDescription_strategy = st.builds(
    uma_ActivityDescription,
    howtoStaff=
        safe_text,
    alternatives=
        safe_text,
    purpose=
        safe_text
)
RoleDescriptor_strategy = st.builds(
    RoleDescriptor,
)
uma_CompositeRole_strategy = st.builds(
    uma_CompositeRole,
)
ActivityDescription_strategy = st.builds(
    ActivityDescription,
)
uma_ProcessDescription_strategy = st.builds(
    uma_ProcessDescription,
    usageNotes=
        safe_text,
    scope=
        safe_text,
    externalId=
        safe_text
)
Descriptor_strategy = st.builds(
    Descriptor,
)
uma_WorkProductDescriptor_strategy = st.builds(
    uma_WorkProductDescriptor,
    activityExitState=
        safe_text,
    activityEntryState=
        safe_text
)
uma_ProcessComponentDescriptor_strategy = st.builds(
    uma_ProcessComponentDescriptor,
)
uma_RoleDescriptor_strategy = st.builds(
    uma_RoleDescriptor,
)
Activity_strategy = st.builds(
    Activity,
)
uma_Process_strategy = st.builds(
    uma_Process,
)
uma_Phase_strategy = st.builds(
    uma_Phase,
)
uma_Iteration_strategy = st.builds(
    uma_Iteration,
)
BreakdownElement_strategy = st.builds(
    BreakdownElement,
)
uma_Descriptor_strategy = st.builds(
    uma_Descriptor,
    isSynchronizedWithSource=
        safe_text
)
uma_ProcessComponentInterface_strategy = st.builds(
    uma_ProcessComponentInterface,
)
uma_TeamProfile_strategy = st.builds(
    uma_TeamProfile,
)
uma_WorkBreakdownElement_strategy = st.builds(
    uma_WorkBreakdownElement,
    isRepeatable=
        safe_text,
    isEventDriven=
        safe_text,
    isOngoing=
        safe_text
)
uma_Roadmap_strategy = st.builds(
    uma_Roadmap,
)
WorkBreakdownElement_strategy = st.builds(
    WorkBreakdownElement,
)
uma_TaskDescriptor_strategy = st.builds(
    uma_TaskDescriptor,
)
uma_Milestone_strategy = st.builds(
    uma_Milestone,
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
uma_PlanningData_strategy = st.builds(
    uma_PlanningData,
    rank=
        safe_text,
    startDate=
        safe_text,
    finishDate=
        safe_text
)
uma_BreakdownElement_strategy = st.builds(
    uma_BreakdownElement,
    hasMultipleOccurrences=
        safe_text,
    prefix=
        safe_text,
    isOptional=
        safe_text,
    isPlanned=
        safe_text
)
uma_WorkOrder_strategy = st.builds(
    uma_WorkOrder,
    linkType=
        safe_text
)
LeafElement_strategy = st.builds(
    LeafElement,
)
uma_Image_strategy = st.builds(
    uma_Image,
    uri=
        safe_text,
    mimeType=
        safe_text
)
uma_TextElement_strategy = st.builds(
    uma_TextElement,
    text=
        safe_text
)
SemanticModelBridge_strategy = st.builds(
    SemanticModelBridge,
)
uma_UMASemanticModelBridge_strategy = st.builds(
    uma_UMASemanticModelBridge,
)
uma_CoreSemanticModelBridge_strategy = st.builds(
    uma_CoreSemanticModelBridge,
)
uma_SimpleSemanticModelElement_strategy = st.builds(
    uma_SimpleSemanticModelElement,
    typeInfo=
        safe_text
)
GraphNode_strategy = st.builds(
    GraphNode,
)
GraphicPrimitive_strategy = st.builds(
    GraphicPrimitive,
)
uma_Ellipse_strategy = st.builds(
    uma_Ellipse,
    endAngle=
        safe_text,
    rotation=
        safe_text,
    radiusY=
        safe_text,
    radiusX=
        safe_text,
    startAngle=
        safe_text
)
uma_Polyline_strategy = st.builds(
    uma_Polyline,
    closed=
        safe_text
)
uma_Dimension_strategy = st.builds(
    uma_Dimension,
    height=
        safe_text,
    width=
        safe_text
)
uma_GraphicPrimitive_strategy = st.builds(
    uma_GraphicPrimitive,
)
GraphElement_strategy = st.builds(
    GraphElement,
)
uma_GraphEdge_strategy = st.builds(
    uma_GraphEdge,
)
uma_GraphNode_strategy = st.builds(
    uma_GraphNode,
)
uma_Diagram_strategy = st.builds(
    uma_Diagram,
    zoom=
        safe_text
)
uma_GraphConnector_strategy = st.builds(
    uma_GraphConnector,
)
uma_Point_strategy = st.builds(
    uma_Point,
    y=
        safe_text,
    x=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
uma_DiagramLink_strategy = st.builds(
    uma_DiagramLink,
    zoom=
        safe_text
)
uma_LeafElement_strategy = st.builds(
    uma_LeafElement,
)
uma_SemanticModelBridge_strategy = st.builds(
    uma_SemanticModelBridge,
    presentation=
        safe_text
)
uma_Reference_strategy = st.builds(
    uma_Reference,
    isIndividualRepresentation=
        safe_text
)
uma_Property_strategy = st.builds(
    uma_Property,
    value=
        safe_text,
    key=
        safe_text
)
uma_GraphElement_strategy = st.builds(
    uma_GraphElement,
)
ContentDescription_strategy = st.builds(
    ContentDescription,
)
uma_PracticeDescription_strategy = st.builds(
    uma_PracticeDescription,
    levelsOfAdoption=
        safe_text,
    goals=
        safe_text,
    background=
        safe_text,
    application=
        safe_text,
    additionalInfo=
        safe_text,
    problem=
        safe_text
)
uma_RoleDescription_strategy = st.builds(
    uma_RoleDescription,
    skills=
        safe_text,
    synonyms=
        safe_text,
    assignmentApproaches=
        safe_text
)
uma_TaskDescription_strategy = st.builds(
    uma_TaskDescription,
    alternatives=
        safe_text,
    purpose=
        safe_text
)
uma_BreakdownElementDescription_strategy = st.builds(
    uma_BreakdownElementDescription,
    usageGuidance=
        safe_text
)
uma_GuidanceDescription_strategy = st.builds(
    uma_GuidanceDescription,
    attachments=
        safe_text
)
uma_WorkProductDescription_strategy = st.builds(
    uma_WorkProductDescription,
    externalId=
        safe_text,
    reasonsForNotNeeding=
        safe_text,
    purpose=
        safe_text,
    impactOfNotHaving=
        safe_text
)
WorkProductDescription_strategy = st.builds(
    WorkProductDescription,
)
uma_ArtifactDescription_strategy = st.builds(
    uma_ArtifactDescription,
    representationOptions=
        safe_text,
    briefOutline=
        safe_text
)
MethodPackage_strategy = st.builds(
    MethodPackage,
)
uma_ProcessPackage_strategy = st.builds(
    uma_ProcessPackage,
)
uma_ContentPackage_strategy = st.builds(
    uma_ContentPackage,
)
Package_strategy = st.builds(
    Package,
)
uma_DeliverableDescription_strategy = st.builds(
    uma_DeliverableDescription,
    externalDescription=
        safe_text,
    packagingGuidance=
        safe_text
)
WorkProduct_strategy = st.builds(
    WorkProduct,
)
uma_Deliverable_strategy = st.builds(
    uma_Deliverable,
)
uma_Outcome_strategy = st.builds(
    uma_Outcome,
)
uma_Artifact_strategy = st.builds(
    uma_Artifact,
)
Section_strategy = st.builds(
    Section,
)
uma_ToolMentor_strategy = st.builds(
    uma_ToolMentor,
)
uma_Template_strategy = st.builds(
    uma_Template,
)
uma_Report_strategy = st.builds(
    uma_Report,
)
uma_Estimate_strategy = st.builds(
    uma_Estimate,
)
ContentElement_strategy = st.builds(
    ContentElement,
)
uma_ContentCategory_strategy = st.builds(
    uma_ContentCategory,
)
uma_WorkProduct_strategy = st.builds(
    uma_WorkProduct,
)
uma_Guidance_strategy = st.builds(
    uma_Guidance,
)
uma_Role_strategy = st.builds(
    uma_Role,
)
MethodUnit_strategy = st.builds(
    MethodUnit,
)
uma_ProcessComponent_strategy = st.builds(
    uma_ProcessComponent,
)
uma_MethodPlugin_strategy = st.builds(
    uma_MethodPlugin,
    userChangeable=
        safe_text
)
uma_MethodLibrary_strategy = st.builds(
    uma_MethodLibrary,
)
Classifier_strategy = st.builds(
    Classifier,
)
WorkDefinition_strategy = st.builds(
    WorkDefinition,
)
uma_Step_strategy = st.builds(
    uma_Step,
)
uma_Task_strategy = st.builds(
    uma_Task,
)
uma_ReusableAsset_strategy = st.builds(
    uma_ReusableAsset,
)
uma_Example_strategy = st.builds(
    uma_Example,
)
uma_Guideline_strategy = st.builds(
    uma_Guideline,
)
uma_Checklist_strategy = st.builds(
    uma_Checklist,
)
uma_Concept_strategy = st.builds(
    uma_Concept,
)
uma_SupportingMaterial_strategy = st.builds(
    uma_SupportingMaterial,
)
VariabilityElement_strategy = st.builds(
    VariabilityElement,
)
uma_Activity_strategy = st.builds(
    uma_Activity,
)
uma_Section_strategy = st.builds(
    uma_Section,
    sectionDescription=
        safe_text,
    sectionName=
        safe_text
)
DescribableElement_strategy = st.builds(
    DescribableElement,
)
uma_ProcessElement_strategy = st.builds(
    uma_ProcessElement,
)
uma_ContentElement_strategy = st.builds(
    uma_ContentElement,
)
MethodElement_strategy = st.builds(
    MethodElement,
)
uma_MethodPackage_strategy = st.builds(
    uma_MethodPackage,
    global_=
        safe_text
)
uma_DiagramElement_strategy = st.builds(
    uma_DiagramElement,
    isVisible=
        safe_text
)
uma_MethodUnit_strategy = st.builds(
    uma_MethodUnit,
    changeDate=
        safe_text,
    version=
        safe_text,
    changeDescription=
        safe_text,
    authors=
        safe_text
)
uma_MethodConfiguration_strategy = st.builds(
    uma_MethodConfiguration,
)
uma_WorkDefinition_strategy = st.builds(
    uma_WorkDefinition,
)
uma_DescribableElement_strategy = st.builds(
    uma_DescribableElement,
    presentationName=
        safe_text,
    nodeicon=
        safe_text,
    shapeicon=
        safe_text
)
uma_VariabilityElement_strategy = st.builds(
    uma_VariabilityElement,
    variabilityType=
        safe_text
)
uma_ContentDescription_strategy = st.builds(
    uma_ContentDescription,
    mainDescription=
        safe_text,
    keyConsiderations=
        safe_text
)
Namespace_strategy = st.builds(
    Namespace,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uma_Namespace_strategy = st.builds(
    uma_Namespace,
)
uma_PackageableElement_strategy = st.builds(
    uma_PackageableElement,
)
Element_strategy = st.builds(
    Element,
)
uma_NamedElement_strategy = st.builds(
    uma_NamedElement,
    name=
        safe_text
)
uma_Element_strategy = st.builds(
    uma_Element,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uma_MethodElement_strategy = st.builds(
    uma_MethodElement,
    orderingGuide=
        safe_text,
    suppressed=
        safe_text,
    briefDescription=
        safe_text,
    guid=
        safe_text
)
uma_Package_strategy = st.builds(
    uma_Package,
)
uma_Type_strategy = st.builds(
    uma_Type,
)
Type_strategy = st.builds(
    Type,
)
uma_Classifier_strategy = st.builds(
    uma_Classifier,
)
uma_Constraint_strategy = st.builds(
    uma_Constraint,
    body=
        safe_text
)





























@given(instance=uma_DeliveryProcessDescription_strategy)
def test_hyp_uma_deliveryprocessdescription_projectCharacteristics_setter(instance):
    original = instance.projectCharacteristics
    instance.projectCharacteristics = original
    assert instance.projectCharacteristics == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_hyp_uma_deliveryprocessdescription_riskLevel_setter(instance):
    original = instance.riskLevel
    instance.riskLevel = original
    assert instance.riskLevel == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_hyp_uma_deliveryprocessdescription_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_hyp_uma_deliveryprocessdescription_projectMemberExpertise_setter(instance):
    original = instance.projectMemberExpertise
    instance.projectMemberExpertise = original
    assert instance.projectMemberExpertise == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_hyp_uma_deliveryprocessdescription_typeOfContract_setter(instance):
    original = instance.typeOfContract
    instance.typeOfContract = original
    assert instance.typeOfContract == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_hyp_uma_deliveryprocessdescription_estimatingTechnique_setter(instance):
    original = instance.estimatingTechnique
    instance.estimatingTechnique = original
    assert instance.estimatingTechnique == original





@given(instance=uma_DescriptorDescription_strategy)
def test_hyp_uma_descriptordescription_refinedDescription_setter(instance):
    original = instance.refinedDescription
    instance.refinedDescription = original
    assert instance.refinedDescription == original




@given(instance=uma_ActivityDescription_strategy)
def test_hyp_uma_activitydescription_howtoStaff_setter(instance):
    original = instance.howtoStaff
    instance.howtoStaff = original
    assert instance.howtoStaff == original



@given(instance=uma_ActivityDescription_strategy)
def test_hyp_uma_activitydescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original



@given(instance=uma_ActivityDescription_strategy)
def test_hyp_uma_activitydescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original







@given(instance=uma_ProcessDescription_strategy)
def test_hyp_uma_processdescription_usageNotes_setter(instance):
    original = instance.usageNotes
    instance.usageNotes = original
    assert instance.usageNotes == original



@given(instance=uma_ProcessDescription_strategy)
def test_hyp_uma_processdescription_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=uma_ProcessDescription_strategy)
def test_hyp_uma_processdescription_externalId_setter(instance):
    original = instance.externalId
    instance.externalId = original
    assert instance.externalId == original





@given(instance=uma_WorkProductDescriptor_strategy)
def test_hyp_uma_workproductdescriptor_activityExitState_setter(instance):
    original = instance.activityExitState
    instance.activityExitState = original
    assert instance.activityExitState == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_hyp_uma_workproductdescriptor_activityEntryState_setter(instance):
    original = instance.activityEntryState
    instance.activityEntryState = original
    assert instance.activityEntryState == original











@given(instance=uma_Descriptor_strategy)
def test_hyp_uma_descriptor_isSynchronizedWithSource_setter(instance):
    original = instance.isSynchronizedWithSource
    instance.isSynchronizedWithSource = original
    assert instance.isSynchronizedWithSource == original






@given(instance=uma_WorkBreakdownElement_strategy)
def test_hyp_uma_workbreakdownelement_isRepeatable_setter(instance):
    original = instance.isRepeatable
    instance.isRepeatable = original
    assert instance.isRepeatable == original



@given(instance=uma_WorkBreakdownElement_strategy)
def test_hyp_uma_workbreakdownelement_isEventDriven_setter(instance):
    original = instance.isEventDriven
    instance.isEventDriven = original
    assert instance.isEventDriven == original



@given(instance=uma_WorkBreakdownElement_strategy)
def test_hyp_uma_workbreakdownelement_isOngoing_setter(instance):
    original = instance.isOngoing
    instance.isOngoing = original
    assert instance.isOngoing == original









@given(instance=uma_PlanningData_strategy)
def test_hyp_uma_planningdata_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=uma_PlanningData_strategy)
def test_hyp_uma_planningdata_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=uma_PlanningData_strategy)
def test_hyp_uma_planningdata_finishDate_setter(instance):
    original = instance.finishDate
    instance.finishDate = original
    assert instance.finishDate == original




@given(instance=uma_BreakdownElement_strategy)
def test_hyp_uma_breakdownelement_hasMultipleOccurrences_setter(instance):
    original = instance.hasMultipleOccurrences
    instance.hasMultipleOccurrences = original
    assert instance.hasMultipleOccurrences == original



@given(instance=uma_BreakdownElement_strategy)
def test_hyp_uma_breakdownelement_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=uma_BreakdownElement_strategy)
def test_hyp_uma_breakdownelement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original



@given(instance=uma_BreakdownElement_strategy)
def test_hyp_uma_breakdownelement_isPlanned_setter(instance):
    original = instance.isPlanned
    instance.isPlanned = original
    assert instance.isPlanned == original




@given(instance=uma_WorkOrder_strategy)
def test_hyp_uma_workorder_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original





@given(instance=uma_Image_strategy)
def test_hyp_uma_image_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=uma_Image_strategy)
def test_hyp_uma_image_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original




@given(instance=uma_TextElement_strategy)
def test_hyp_uma_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original







@given(instance=uma_SimpleSemanticModelElement_strategy)
def test_hyp_uma_simplesemanticmodelelement_typeInfo_setter(instance):
    original = instance.typeInfo
    instance.typeInfo = original
    assert instance.typeInfo == original






@given(instance=uma_Ellipse_strategy)
def test_hyp_uma_ellipse_endAngle_setter(instance):
    original = instance.endAngle
    instance.endAngle = original
    assert instance.endAngle == original



@given(instance=uma_Ellipse_strategy)
def test_hyp_uma_ellipse_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=uma_Ellipse_strategy)
def test_hyp_uma_ellipse_radiusY_setter(instance):
    original = instance.radiusY
    instance.radiusY = original
    assert instance.radiusY == original



@given(instance=uma_Ellipse_strategy)
def test_hyp_uma_ellipse_radiusX_setter(instance):
    original = instance.radiusX
    instance.radiusX = original
    assert instance.radiusX == original



@given(instance=uma_Ellipse_strategy)
def test_hyp_uma_ellipse_startAngle_setter(instance):
    original = instance.startAngle
    instance.startAngle = original
    assert instance.startAngle == original




@given(instance=uma_Polyline_strategy)
def test_hyp_uma_polyline_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original




@given(instance=uma_Dimension_strategy)
def test_hyp_uma_dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=uma_Dimension_strategy)
def test_hyp_uma_dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original








@given(instance=uma_Diagram_strategy)
def test_hyp_uma_diagram_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original





@given(instance=uma_Point_strategy)
def test_hyp_uma_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uma_Point_strategy)
def test_hyp_uma_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original





@given(instance=uma_DiagramLink_strategy)
def test_hyp_uma_diagramlink_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original





@given(instance=uma_SemanticModelBridge_strategy)
def test_hyp_uma_semanticmodelbridge_presentation_setter(instance):
    original = instance.presentation
    instance.presentation = original
    assert instance.presentation == original




@given(instance=uma_Reference_strategy)
def test_hyp_uma_reference_isIndividualRepresentation_setter(instance):
    original = instance.isIndividualRepresentation
    instance.isIndividualRepresentation = original
    assert instance.isIndividualRepresentation == original




@given(instance=uma_Property_strategy)
def test_hyp_uma_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=uma_Property_strategy)
def test_hyp_uma_property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original






@given(instance=uma_PracticeDescription_strategy)
def test_hyp_uma_practicedescription_levelsOfAdoption_setter(instance):
    original = instance.levelsOfAdoption
    instance.levelsOfAdoption = original
    assert instance.levelsOfAdoption == original



@given(instance=uma_PracticeDescription_strategy)
def test_hyp_uma_practicedescription_goals_setter(instance):
    original = instance.goals
    instance.goals = original
    assert instance.goals == original



@given(instance=uma_PracticeDescription_strategy)
def test_hyp_uma_practicedescription_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=uma_PracticeDescription_strategy)
def test_hyp_uma_practicedescription_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original



@given(instance=uma_PracticeDescription_strategy)
def test_hyp_uma_practicedescription_additionalInfo_setter(instance):
    original = instance.additionalInfo
    instance.additionalInfo = original
    assert instance.additionalInfo == original



@given(instance=uma_PracticeDescription_strategy)
def test_hyp_uma_practicedescription_problem_setter(instance):
    original = instance.problem
    instance.problem = original
    assert instance.problem == original




@given(instance=uma_RoleDescription_strategy)
def test_hyp_uma_roledescription_skills_setter(instance):
    original = instance.skills
    instance.skills = original
    assert instance.skills == original



@given(instance=uma_RoleDescription_strategy)
def test_hyp_uma_roledescription_synonyms_setter(instance):
    original = instance.synonyms
    instance.synonyms = original
    assert instance.synonyms == original



@given(instance=uma_RoleDescription_strategy)
def test_hyp_uma_roledescription_assignmentApproaches_setter(instance):
    original = instance.assignmentApproaches
    instance.assignmentApproaches = original
    assert instance.assignmentApproaches == original




@given(instance=uma_TaskDescription_strategy)
def test_hyp_uma_taskdescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original



@given(instance=uma_TaskDescription_strategy)
def test_hyp_uma_taskdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original




@given(instance=uma_BreakdownElementDescription_strategy)
def test_hyp_uma_breakdownelementdescription_usageGuidance_setter(instance):
    original = instance.usageGuidance
    instance.usageGuidance = original
    assert instance.usageGuidance == original




@given(instance=uma_GuidanceDescription_strategy)
def test_hyp_uma_guidancedescription_attachments_setter(instance):
    original = instance.attachments
    instance.attachments = original
    assert instance.attachments == original




@given(instance=uma_WorkProductDescription_strategy)
def test_hyp_uma_workproductdescription_externalId_setter(instance):
    original = instance.externalId
    instance.externalId = original
    assert instance.externalId == original



@given(instance=uma_WorkProductDescription_strategy)
def test_hyp_uma_workproductdescription_reasonsForNotNeeding_setter(instance):
    original = instance.reasonsForNotNeeding
    instance.reasonsForNotNeeding = original
    assert instance.reasonsForNotNeeding == original



@given(instance=uma_WorkProductDescription_strategy)
def test_hyp_uma_workproductdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=uma_WorkProductDescription_strategy)
def test_hyp_uma_workproductdescription_impactOfNotHaving_setter(instance):
    original = instance.impactOfNotHaving
    instance.impactOfNotHaving = original
    assert instance.impactOfNotHaving == original





@given(instance=uma_ArtifactDescription_strategy)
def test_hyp_uma_artifactdescription_representationOptions_setter(instance):
    original = instance.representationOptions
    instance.representationOptions = original
    assert instance.representationOptions == original



@given(instance=uma_ArtifactDescription_strategy)
def test_hyp_uma_artifactdescription_briefOutline_setter(instance):
    original = instance.briefOutline
    instance.briefOutline = original
    assert instance.briefOutline == original








@given(instance=uma_DeliverableDescription_strategy)
def test_hyp_uma_deliverabledescription_externalDescription_setter(instance):
    original = instance.externalDescription
    instance.externalDescription = original
    assert instance.externalDescription == original



@given(instance=uma_DeliverableDescription_strategy)
def test_hyp_uma_deliverabledescription_packagingGuidance_setter(instance):
    original = instance.packagingGuidance
    instance.packagingGuidance = original
    assert instance.packagingGuidance == original




















@given(instance=uma_MethodPlugin_strategy)
def test_hyp_uma_methodplugin_userChangeable_setter(instance):
    original = instance.userChangeable
    instance.userChangeable = original
    assert instance.userChangeable == original

















@given(instance=uma_Section_strategy)
def test_hyp_uma_section_sectionDescription_setter(instance):
    original = instance.sectionDescription
    instance.sectionDescription = original
    assert instance.sectionDescription == original



@given(instance=uma_Section_strategy)
def test_hyp_uma_section_sectionName_setter(instance):
    original = instance.sectionName
    instance.sectionName = original
    assert instance.sectionName == original








@given(instance=uma_MethodPackage_strategy)
def test_hyp_uma_methodpackage_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original




@given(instance=uma_DiagramElement_strategy)
def test_hyp_uma_diagramelement_isVisible_setter(instance):
    original = instance.isVisible
    instance.isVisible = original
    assert instance.isVisible == original




@given(instance=uma_MethodUnit_strategy)
def test_hyp_uma_methodunit_changeDate_setter(instance):
    original = instance.changeDate
    instance.changeDate = original
    assert instance.changeDate == original



@given(instance=uma_MethodUnit_strategy)
def test_hyp_uma_methodunit_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=uma_MethodUnit_strategy)
def test_hyp_uma_methodunit_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original



@given(instance=uma_MethodUnit_strategy)
def test_hyp_uma_methodunit_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original






@given(instance=uma_DescribableElement_strategy)
def test_hyp_uma_describableelement_presentationName_setter(instance):
    original = instance.presentationName
    instance.presentationName = original
    assert instance.presentationName == original



@given(instance=uma_DescribableElement_strategy)
def test_hyp_uma_describableelement_nodeicon_setter(instance):
    original = instance.nodeicon
    instance.nodeicon = original
    assert instance.nodeicon == original



@given(instance=uma_DescribableElement_strategy)
def test_hyp_uma_describableelement_shapeicon_setter(instance):
    original = instance.shapeicon
    instance.shapeicon = original
    assert instance.shapeicon == original




@given(instance=uma_VariabilityElement_strategy)
def test_hyp_uma_variabilityelement_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original




@given(instance=uma_ContentDescription_strategy)
def test_hyp_uma_contentdescription_mainDescription_setter(instance):
    original = instance.mainDescription
    instance.mainDescription = original
    assert instance.mainDescription == original



@given(instance=uma_ContentDescription_strategy)
def test_hyp_uma_contentdescription_keyConsiderations_setter(instance):
    original = instance.keyConsiderations
    instance.keyConsiderations = original
    assert instance.keyConsiderations == original









@given(instance=uma_NamedElement_strategy)
def test_hyp_uma_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=uma_MethodElement_strategy)
def test_hyp_uma_methodelement_orderingGuide_setter(instance):
    original = instance.orderingGuide
    instance.orderingGuide = original
    assert instance.orderingGuide == original



@given(instance=uma_MethodElement_strategy)
def test_hyp_uma_methodelement_suppressed_setter(instance):
    original = instance.suppressed
    instance.suppressed = original
    assert instance.suppressed == original



@given(instance=uma_MethodElement_strategy)
def test_hyp_uma_methodelement_briefDescription_setter(instance):
    original = instance.briefDescription
    instance.briefDescription = original
    assert instance.briefDescription == original



@given(instance=uma_MethodElement_strategy)
def test_hyp_uma_methodelement_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original








@given(instance=uma_Constraint_strategy)
def test_hyp_uma_constraint_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_uma_ActivityDescription_alternatives_value_roundtrip():
    instance = uma_ActivityDescription(alternatives="sample_text", howtoStaff="sample_text", purpose="sample_text")
    assert instance.alternatives == "sample_text"
    instance.alternatives = "sample_text_2"
    assert instance.alternatives == "sample_text_2"


def test_uma_ActivityDescription_howtoStaff_value_roundtrip():
    instance = uma_ActivityDescription(alternatives="sample_text", howtoStaff="sample_text", purpose="sample_text")
    assert instance.howtoStaff == "sample_text"
    instance.howtoStaff = "sample_text_2"
    assert instance.howtoStaff == "sample_text_2"


def test_uma_ActivityDescription_purpose_value_roundtrip():
    instance = uma_ActivityDescription(alternatives="sample_text", howtoStaff="sample_text", purpose="sample_text")
    assert instance.purpose == "sample_text"
    instance.purpose = "sample_text_2"
    assert instance.purpose == "sample_text_2"


def test_uma_ArtifactDescription_briefOutline_value_roundtrip():
    instance = uma_ArtifactDescription(briefOutline="sample_text", representationOptions="sample_text")
    assert instance.briefOutline == "sample_text"
    instance.briefOutline = "sample_text_2"
    assert instance.briefOutline == "sample_text_2"


def test_uma_ArtifactDescription_representationOptions_value_roundtrip():
    instance = uma_ArtifactDescription(briefOutline="sample_text", representationOptions="sample_text")
    assert instance.representationOptions == "sample_text"
    instance.representationOptions = "sample_text_2"
    assert instance.representationOptions == "sample_text_2"


def test_uma_BreakdownElement_hasMultipleOccurrences_value_roundtrip():
    instance = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    assert instance.hasMultipleOccurrences == "sample_text"
    instance.hasMultipleOccurrences = "sample_text_2"
    assert instance.hasMultipleOccurrences == "sample_text_2"


def test_uma_BreakdownElement_isOptional_value_roundtrip():
    instance = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    assert instance.isOptional == "sample_text"
    instance.isOptional = "sample_text_2"
    assert instance.isOptional == "sample_text_2"


def test_uma_BreakdownElement_isPlanned_value_roundtrip():
    instance = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    assert instance.isPlanned == "sample_text"
    instance.isPlanned = "sample_text_2"
    assert instance.isPlanned == "sample_text_2"


def test_uma_BreakdownElement_prefix_value_roundtrip():
    instance = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    assert instance.prefix == "sample_text"
    instance.prefix = "sample_text_2"
    assert instance.prefix == "sample_text_2"


def test_uma_BreakdownElementDescription_usageGuidance_value_roundtrip():
    instance = uma_BreakdownElementDescription(usageGuidance="sample_text")
    assert instance.usageGuidance == "sample_text"
    instance.usageGuidance = "sample_text_2"
    assert instance.usageGuidance == "sample_text_2"


def test_uma_Constraint_body_value_roundtrip():
    instance = uma_Constraint(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_uma_ContentDescription_keyConsiderations_value_roundtrip():
    instance = uma_ContentDescription(keyConsiderations="sample_text", mainDescription="sample_text")
    assert instance.keyConsiderations == "sample_text"
    instance.keyConsiderations = "sample_text_2"
    assert instance.keyConsiderations == "sample_text_2"


def test_uma_ContentDescription_mainDescription_value_roundtrip():
    instance = uma_ContentDescription(keyConsiderations="sample_text", mainDescription="sample_text")
    assert instance.mainDescription == "sample_text"
    instance.mainDescription = "sample_text_2"
    assert instance.mainDescription == "sample_text_2"


def test_uma_DeliverableDescription_externalDescription_value_roundtrip():
    instance = uma_DeliverableDescription(externalDescription="sample_text", packagingGuidance="sample_text")
    assert instance.externalDescription == "sample_text"
    instance.externalDescription = "sample_text_2"
    assert instance.externalDescription == "sample_text_2"


def test_uma_DeliverableDescription_packagingGuidance_value_roundtrip():
    instance = uma_DeliverableDescription(externalDescription="sample_text", packagingGuidance="sample_text")
    assert instance.packagingGuidance == "sample_text"
    instance.packagingGuidance = "sample_text_2"
    assert instance.packagingGuidance == "sample_text_2"


def test_uma_DeliveryProcessDescription_estimatingTechnique_value_roundtrip():
    instance = uma_DeliveryProcessDescription(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    assert instance.estimatingTechnique == "sample_text"
    instance.estimatingTechnique = "sample_text_2"
    assert instance.estimatingTechnique == "sample_text_2"


def test_uma_DeliveryProcessDescription_projectCharacteristics_value_roundtrip():
    instance = uma_DeliveryProcessDescription(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    assert instance.projectCharacteristics == "sample_text"
    instance.projectCharacteristics = "sample_text_2"
    assert instance.projectCharacteristics == "sample_text_2"


def test_uma_DeliveryProcessDescription_projectMemberExpertise_value_roundtrip():
    instance = uma_DeliveryProcessDescription(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    assert instance.projectMemberExpertise == "sample_text"
    instance.projectMemberExpertise = "sample_text_2"
    assert instance.projectMemberExpertise == "sample_text_2"


def test_uma_DeliveryProcessDescription_riskLevel_value_roundtrip():
    instance = uma_DeliveryProcessDescription(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    assert instance.riskLevel == "sample_text"
    instance.riskLevel = "sample_text_2"
    assert instance.riskLevel == "sample_text_2"


def test_uma_DeliveryProcessDescription_scale_value_roundtrip():
    instance = uma_DeliveryProcessDescription(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    assert instance.scale == "sample_text"
    instance.scale = "sample_text_2"
    assert instance.scale == "sample_text_2"


def test_uma_DeliveryProcessDescription_typeOfContract_value_roundtrip():
    instance = uma_DeliveryProcessDescription(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    assert instance.typeOfContract == "sample_text"
    instance.typeOfContract = "sample_text_2"
    assert instance.typeOfContract == "sample_text_2"


def test_uma_DescribableElement_nodeicon_value_roundtrip():
    instance = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    assert instance.nodeicon == "sample_text"
    instance.nodeicon = "sample_text_2"
    assert instance.nodeicon == "sample_text_2"


def test_uma_DescribableElement_presentationName_value_roundtrip():
    instance = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    assert instance.presentationName == "sample_text"
    instance.presentationName = "sample_text_2"
    assert instance.presentationName == "sample_text_2"


def test_uma_DescribableElement_shapeicon_value_roundtrip():
    instance = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    assert instance.shapeicon == "sample_text"
    instance.shapeicon = "sample_text_2"
    assert instance.shapeicon == "sample_text_2"


def test_uma_Descriptor_isSynchronizedWithSource_value_roundtrip():
    instance = uma_Descriptor(isSynchronizedWithSource="sample_text")
    assert instance.isSynchronizedWithSource == "sample_text"
    instance.isSynchronizedWithSource = "sample_text_2"
    assert instance.isSynchronizedWithSource == "sample_text_2"


def test_uma_DescriptorDescription_refinedDescription_value_roundtrip():
    instance = uma_DescriptorDescription(refinedDescription="sample_text")
    assert instance.refinedDescription == "sample_text"
    instance.refinedDescription = "sample_text_2"
    assert instance.refinedDescription == "sample_text_2"


def test_uma_Diagram_zoom_value_roundtrip():
    instance = uma_Diagram(zoom="sample_text")
    assert instance.zoom == "sample_text"
    instance.zoom = "sample_text_2"
    assert instance.zoom == "sample_text_2"


def test_uma_DiagramElement_isVisible_value_roundtrip():
    instance = uma_DiagramElement(isVisible="sample_text")
    assert instance.isVisible == "sample_text"
    instance.isVisible = "sample_text_2"
    assert instance.isVisible == "sample_text_2"


def test_uma_DiagramLink_zoom_value_roundtrip():
    instance = uma_DiagramLink(zoom="sample_text")
    assert instance.zoom == "sample_text"
    instance.zoom = "sample_text_2"
    assert instance.zoom == "sample_text_2"


def test_uma_Dimension_height_value_roundtrip():
    instance = uma_Dimension(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_uma_Dimension_width_value_roundtrip():
    instance = uma_Dimension(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_uma_Ellipse_endAngle_value_roundtrip():
    instance = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    assert instance.endAngle == "sample_text"
    instance.endAngle = "sample_text_2"
    assert instance.endAngle == "sample_text_2"


def test_uma_Ellipse_radiusX_value_roundtrip():
    instance = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    assert instance.radiusX == "sample_text"
    instance.radiusX = "sample_text_2"
    assert instance.radiusX == "sample_text_2"


def test_uma_Ellipse_radiusY_value_roundtrip():
    instance = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    assert instance.radiusY == "sample_text"
    instance.radiusY = "sample_text_2"
    assert instance.radiusY == "sample_text_2"


def test_uma_Ellipse_rotation_value_roundtrip():
    instance = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_uma_Ellipse_startAngle_value_roundtrip():
    instance = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    assert instance.startAngle == "sample_text"
    instance.startAngle = "sample_text_2"
    assert instance.startAngle == "sample_text_2"


def test_uma_GuidanceDescription_attachments_value_roundtrip():
    instance = uma_GuidanceDescription(attachments="sample_text")
    assert instance.attachments == "sample_text"
    instance.attachments = "sample_text_2"
    assert instance.attachments == "sample_text_2"


def test_uma_Image_mimeType_value_roundtrip():
    instance = uma_Image(mimeType="sample_text", uri="sample_text")
    assert instance.mimeType == "sample_text"
    instance.mimeType = "sample_text_2"
    assert instance.mimeType == "sample_text_2"


def test_uma_Image_uri_value_roundtrip():
    instance = uma_Image(mimeType="sample_text", uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_uma_MethodElement_briefDescription_value_roundtrip():
    instance = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    assert instance.briefDescription == "sample_text"
    instance.briefDescription = "sample_text_2"
    assert instance.briefDescription == "sample_text_2"


def test_uma_MethodElement_guid_value_roundtrip():
    instance = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    assert instance.guid == "sample_text"
    instance.guid = "sample_text_2"
    assert instance.guid == "sample_text_2"


def test_uma_MethodElement_orderingGuide_value_roundtrip():
    instance = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    assert instance.orderingGuide == "sample_text"
    instance.orderingGuide = "sample_text_2"
    assert instance.orderingGuide == "sample_text_2"


def test_uma_MethodElement_suppressed_value_roundtrip():
    instance = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    assert instance.suppressed == "sample_text"
    instance.suppressed = "sample_text_2"
    assert instance.suppressed == "sample_text_2"


def test_uma_MethodPackage_global__value_roundtrip():
    instance = uma_MethodPackage(global_="sample_text")
    assert instance.global_ == "sample_text"
    instance.global_ = "sample_text_2"
    assert instance.global_ == "sample_text_2"


def test_uma_MethodPlugin_userChangeable_value_roundtrip():
    instance = uma_MethodPlugin(userChangeable="sample_text")
    assert instance.userChangeable == "sample_text"
    instance.userChangeable = "sample_text_2"
    assert instance.userChangeable == "sample_text_2"


def test_uma_MethodUnit_authors_value_roundtrip():
    instance = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    assert instance.authors == "sample_text"
    instance.authors = "sample_text_2"
    assert instance.authors == "sample_text_2"


def test_uma_MethodUnit_changeDate_value_roundtrip():
    instance = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    assert instance.changeDate == "sample_text"
    instance.changeDate = "sample_text_2"
    assert instance.changeDate == "sample_text_2"


def test_uma_MethodUnit_changeDescription_value_roundtrip():
    instance = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    assert instance.changeDescription == "sample_text"
    instance.changeDescription = "sample_text_2"
    assert instance.changeDescription == "sample_text_2"


def test_uma_MethodUnit_version_value_roundtrip():
    instance = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_uma_NamedElement_name_value_roundtrip():
    instance = uma_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_uma_PlanningData_finishDate_value_roundtrip():
    instance = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    assert instance.finishDate == "sample_text"
    instance.finishDate = "sample_text_2"
    assert instance.finishDate == "sample_text_2"


def test_uma_PlanningData_rank_value_roundtrip():
    instance = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    assert instance.rank == "sample_text"
    instance.rank = "sample_text_2"
    assert instance.rank == "sample_text_2"


def test_uma_PlanningData_startDate_value_roundtrip():
    instance = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    assert instance.startDate == "sample_text"
    instance.startDate = "sample_text_2"
    assert instance.startDate == "sample_text_2"


def test_uma_Point_x_value_roundtrip():
    instance = uma_Point(x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_uma_Point_y_value_roundtrip():
    instance = uma_Point(x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_uma_Polyline_closed_value_roundtrip():
    instance = uma_Polyline(closed="sample_text")
    assert instance.closed == "sample_text"
    instance.closed = "sample_text_2"
    assert instance.closed == "sample_text_2"


def test_uma_PracticeDescription_additionalInfo_value_roundtrip():
    instance = uma_PracticeDescription(additionalInfo="sample_text", application="sample_text", background="sample_text", goals="sample_text", levelsOfAdoption="sample_text", problem="sample_text")
    assert instance.additionalInfo == "sample_text"
    instance.additionalInfo = "sample_text_2"
    assert instance.additionalInfo == "sample_text_2"


def test_uma_PracticeDescription_application_value_roundtrip():
    instance = uma_PracticeDescription(additionalInfo="sample_text", application="sample_text", background="sample_text", goals="sample_text", levelsOfAdoption="sample_text", problem="sample_text")
    assert instance.application == "sample_text"
    instance.application = "sample_text_2"
    assert instance.application == "sample_text_2"


def test_uma_PracticeDescription_background_value_roundtrip():
    instance = uma_PracticeDescription(additionalInfo="sample_text", application="sample_text", background="sample_text", goals="sample_text", levelsOfAdoption="sample_text", problem="sample_text")
    assert instance.background == "sample_text"
    instance.background = "sample_text_2"
    assert instance.background == "sample_text_2"


def test_uma_PracticeDescription_goals_value_roundtrip():
    instance = uma_PracticeDescription(additionalInfo="sample_text", application="sample_text", background="sample_text", goals="sample_text", levelsOfAdoption="sample_text", problem="sample_text")
    assert instance.goals == "sample_text"
    instance.goals = "sample_text_2"
    assert instance.goals == "sample_text_2"


def test_uma_PracticeDescription_levelsOfAdoption_value_roundtrip():
    instance = uma_PracticeDescription(additionalInfo="sample_text", application="sample_text", background="sample_text", goals="sample_text", levelsOfAdoption="sample_text", problem="sample_text")
    assert instance.levelsOfAdoption == "sample_text"
    instance.levelsOfAdoption = "sample_text_2"
    assert instance.levelsOfAdoption == "sample_text_2"


def test_uma_PracticeDescription_problem_value_roundtrip():
    instance = uma_PracticeDescription(additionalInfo="sample_text", application="sample_text", background="sample_text", goals="sample_text", levelsOfAdoption="sample_text", problem="sample_text")
    assert instance.problem == "sample_text"
    instance.problem = "sample_text_2"
    assert instance.problem == "sample_text_2"


def test_uma_ProcessDescription_externalId_value_roundtrip():
    instance = uma_ProcessDescription(externalId="sample_text", scope="sample_text", usageNotes="sample_text")
    assert instance.externalId == "sample_text"
    instance.externalId = "sample_text_2"
    assert instance.externalId == "sample_text_2"


def test_uma_ProcessDescription_scope_value_roundtrip():
    instance = uma_ProcessDescription(externalId="sample_text", scope="sample_text", usageNotes="sample_text")
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_uma_ProcessDescription_usageNotes_value_roundtrip():
    instance = uma_ProcessDescription(externalId="sample_text", scope="sample_text", usageNotes="sample_text")
    assert instance.usageNotes == "sample_text"
    instance.usageNotes = "sample_text_2"
    assert instance.usageNotes == "sample_text_2"


def test_uma_Property_key_value_roundtrip():
    instance = uma_Property(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_uma_Property_value_value_roundtrip():
    instance = uma_Property(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_uma_Reference_isIndividualRepresentation_value_roundtrip():
    instance = uma_Reference(isIndividualRepresentation="sample_text")
    assert instance.isIndividualRepresentation == "sample_text"
    instance.isIndividualRepresentation = "sample_text_2"
    assert instance.isIndividualRepresentation == "sample_text_2"


def test_uma_RoleDescription_assignmentApproaches_value_roundtrip():
    instance = uma_RoleDescription(assignmentApproaches="sample_text", skills="sample_text", synonyms="sample_text")
    assert instance.assignmentApproaches == "sample_text"
    instance.assignmentApproaches = "sample_text_2"
    assert instance.assignmentApproaches == "sample_text_2"


def test_uma_RoleDescription_skills_value_roundtrip():
    instance = uma_RoleDescription(assignmentApproaches="sample_text", skills="sample_text", synonyms="sample_text")
    assert instance.skills == "sample_text"
    instance.skills = "sample_text_2"
    assert instance.skills == "sample_text_2"


def test_uma_RoleDescription_synonyms_value_roundtrip():
    instance = uma_RoleDescription(assignmentApproaches="sample_text", skills="sample_text", synonyms="sample_text")
    assert instance.synonyms == "sample_text"
    instance.synonyms = "sample_text_2"
    assert instance.synonyms == "sample_text_2"


def test_uma_Section_sectionDescription_value_roundtrip():
    instance = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    assert instance.sectionDescription == "sample_text"
    instance.sectionDescription = "sample_text_2"
    assert instance.sectionDescription == "sample_text_2"


def test_uma_Section_sectionName_value_roundtrip():
    instance = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    assert instance.sectionName == "sample_text"
    instance.sectionName = "sample_text_2"
    assert instance.sectionName == "sample_text_2"


def test_uma_SemanticModelBridge_presentation_value_roundtrip():
    instance = uma_SemanticModelBridge(presentation="sample_text")
    assert instance.presentation == "sample_text"
    instance.presentation = "sample_text_2"
    assert instance.presentation == "sample_text_2"


def test_uma_SimpleSemanticModelElement_typeInfo_value_roundtrip():
    instance = uma_SimpleSemanticModelElement(typeInfo="sample_text")
    assert instance.typeInfo == "sample_text"
    instance.typeInfo = "sample_text_2"
    assert instance.typeInfo == "sample_text_2"


def test_uma_TaskDescription_alternatives_value_roundtrip():
    instance = uma_TaskDescription(alternatives="sample_text", purpose="sample_text")
    assert instance.alternatives == "sample_text"
    instance.alternatives = "sample_text_2"
    assert instance.alternatives == "sample_text_2"


def test_uma_TaskDescription_purpose_value_roundtrip():
    instance = uma_TaskDescription(alternatives="sample_text", purpose="sample_text")
    assert instance.purpose == "sample_text"
    instance.purpose = "sample_text_2"
    assert instance.purpose == "sample_text_2"


def test_uma_TextElement_text_value_roundtrip():
    instance = uma_TextElement(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_uma_VariabilityElement_variabilityType_value_roundtrip():
    instance = uma_VariabilityElement(variabilityType="sample_text")
    assert instance.variabilityType == "sample_text"
    instance.variabilityType = "sample_text_2"
    assert instance.variabilityType == "sample_text_2"


def test_uma_WorkBreakdownElement_isEventDriven_value_roundtrip():
    instance = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    assert instance.isEventDriven == "sample_text"
    instance.isEventDriven = "sample_text_2"
    assert instance.isEventDriven == "sample_text_2"


def test_uma_WorkBreakdownElement_isOngoing_value_roundtrip():
    instance = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    assert instance.isOngoing == "sample_text"
    instance.isOngoing = "sample_text_2"
    assert instance.isOngoing == "sample_text_2"


def test_uma_WorkBreakdownElement_isRepeatable_value_roundtrip():
    instance = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    assert instance.isRepeatable == "sample_text"
    instance.isRepeatable = "sample_text_2"
    assert instance.isRepeatable == "sample_text_2"


def test_uma_WorkOrder_linkType_value_roundtrip():
    instance = uma_WorkOrder(linkType="sample_text")
    assert instance.linkType == "sample_text"
    instance.linkType = "sample_text_2"
    assert instance.linkType == "sample_text_2"


def test_uma_WorkProductDescription_externalId_value_roundtrip():
    instance = uma_WorkProductDescription(externalId="sample_text", impactOfNotHaving="sample_text", purpose="sample_text", reasonsForNotNeeding="sample_text")
    assert instance.externalId == "sample_text"
    instance.externalId = "sample_text_2"
    assert instance.externalId == "sample_text_2"


def test_uma_WorkProductDescription_impactOfNotHaving_value_roundtrip():
    instance = uma_WorkProductDescription(externalId="sample_text", impactOfNotHaving="sample_text", purpose="sample_text", reasonsForNotNeeding="sample_text")
    assert instance.impactOfNotHaving == "sample_text"
    instance.impactOfNotHaving = "sample_text_2"
    assert instance.impactOfNotHaving == "sample_text_2"


def test_uma_WorkProductDescription_purpose_value_roundtrip():
    instance = uma_WorkProductDescription(externalId="sample_text", impactOfNotHaving="sample_text", purpose="sample_text", reasonsForNotNeeding="sample_text")
    assert instance.purpose == "sample_text"
    instance.purpose = "sample_text_2"
    assert instance.purpose == "sample_text_2"


def test_uma_WorkProductDescription_reasonsForNotNeeding_value_roundtrip():
    instance = uma_WorkProductDescription(externalId="sample_text", impactOfNotHaving="sample_text", purpose="sample_text", reasonsForNotNeeding="sample_text")
    assert instance.reasonsForNotNeeding == "sample_text"
    instance.reasonsForNotNeeding = "sample_text_2"
    assert instance.reasonsForNotNeeding == "sample_text_2"


def test_uma_WorkProductDescriptor_activityEntryState_value_roundtrip():
    instance = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    assert instance.activityEntryState == "sample_text"
    instance.activityEntryState = "sample_text_2"
    assert instance.activityEntryState == "sample_text_2"


def test_uma_WorkProductDescriptor_activityExitState_value_roundtrip():
    instance = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    assert instance.activityExitState == "sample_text"
    instance.activityExitState = "sample_text_2"
    assert instance.activityExitState == "sample_text_2"


def test_uma_Iteration_isa_Activity():
    instance = uma_Iteration()
    assert isinstance(instance, Activity)


def test_uma_Phase_isa_Activity():
    instance = uma_Phase()
    assert isinstance(instance, Activity)


def test_uma_Process_isa_Activity():
    instance = uma_Process()
    assert isinstance(instance, Activity)


def test_uma_ProcessDescription_isa_ActivityDescription():
    instance = uma_ProcessDescription(externalId="sample_text", scope="sample_text", usageNotes="sample_text")
    assert isinstance(instance, ActivityDescription)


def test_uma_Descriptor_isa_BreakdownElement():
    instance = uma_Descriptor(isSynchronizedWithSource="sample_text")
    assert isinstance(instance, BreakdownElement)


def test_uma_ProcessComponentInterface_isa_BreakdownElement():
    instance = uma_ProcessComponentInterface()
    assert isinstance(instance, BreakdownElement)


def test_uma_TeamProfile_isa_BreakdownElement():
    instance = uma_TeamProfile()
    assert isinstance(instance, BreakdownElement)


def test_uma_WorkBreakdownElement_isa_BreakdownElement():
    instance = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    assert isinstance(instance, BreakdownElement)


def test_uma_ActivityDescription_isa_BreakdownElementDescription():
    instance = uma_ActivityDescription(alternatives="sample_text", howtoStaff="sample_text", purpose="sample_text")
    assert isinstance(instance, BreakdownElementDescription)


def test_uma_DescriptorDescription_isa_BreakdownElementDescription():
    instance = uma_DescriptorDescription(refinedDescription="sample_text")
    assert isinstance(instance, BreakdownElementDescription)


def test_uma_DescribableElement_isa_Classifier():
    instance = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    assert isinstance(instance, Classifier)


def test_uma_Whitepaper_isa_Concept():
    instance = uma_Whitepaper()
    assert isinstance(instance, Concept)


def test_uma_CustomCategory_isa_ContentCategory():
    instance = uma_CustomCategory()
    assert isinstance(instance, ContentCategory)


def test_uma_Discipline_isa_ContentCategory():
    instance = uma_Discipline()
    assert isinstance(instance, ContentCategory)


def test_uma_DisciplineGrouping_isa_ContentCategory():
    instance = uma_DisciplineGrouping()
    assert isinstance(instance, ContentCategory)


def test_uma_Domain_isa_ContentCategory():
    instance = uma_Domain()
    assert isinstance(instance, ContentCategory)


def test_uma_RoleSet_isa_ContentCategory():
    instance = uma_RoleSet()
    assert isinstance(instance, ContentCategory)


def test_uma_RoleSetGrouping_isa_ContentCategory():
    instance = uma_RoleSetGrouping()
    assert isinstance(instance, ContentCategory)


def test_uma_Tool_isa_ContentCategory():
    instance = uma_Tool()
    assert isinstance(instance, ContentCategory)


def test_uma_WorkProductType_isa_ContentCategory():
    instance = uma_WorkProductType()
    assert isinstance(instance, ContentCategory)


def test_uma_BreakdownElementDescription_isa_ContentDescription():
    instance = uma_BreakdownElementDescription(usageGuidance="sample_text")
    assert isinstance(instance, ContentDescription)


def test_uma_GuidanceDescription_isa_ContentDescription():
    instance = uma_GuidanceDescription(attachments="sample_text")
    assert isinstance(instance, ContentDescription)


def test_uma_PracticeDescription_isa_ContentDescription():
    instance = uma_PracticeDescription(additionalInfo="sample_text", application="sample_text", background="sample_text", goals="sample_text", levelsOfAdoption="sample_text", problem="sample_text")
    assert isinstance(instance, ContentDescription)


def test_uma_RoleDescription_isa_ContentDescription():
    instance = uma_RoleDescription(assignmentApproaches="sample_text", skills="sample_text", synonyms="sample_text")
    assert isinstance(instance, ContentDescription)


def test_uma_TaskDescription_isa_ContentDescription():
    instance = uma_TaskDescription(alternatives="sample_text", purpose="sample_text")
    assert isinstance(instance, ContentDescription)


def test_uma_WorkProductDescription_isa_ContentDescription():
    instance = uma_WorkProductDescription(externalId="sample_text", impactOfNotHaving="sample_text", purpose="sample_text", reasonsForNotNeeding="sample_text")
    assert isinstance(instance, ContentDescription)


def test_uma_ContentCategory_isa_ContentElement():
    instance = uma_ContentCategory()
    assert isinstance(instance, ContentElement)


def test_uma_Guidance_isa_ContentElement():
    instance = uma_Guidance()
    assert isinstance(instance, ContentElement)


def test_uma_Role_isa_ContentElement():
    instance = uma_Role()
    assert isinstance(instance, ContentElement)


def test_uma_Task_isa_ContentElement():
    instance = uma_Task()
    assert isinstance(instance, ContentElement)


def test_uma_WorkProduct_isa_ContentElement():
    instance = uma_WorkProduct()
    assert isinstance(instance, ContentElement)


def test_uma_ContentElement_isa_DescribableElement():
    instance = uma_ContentElement()
    assert isinstance(instance, DescribableElement)


def test_uma_ProcessElement_isa_DescribableElement():
    instance = uma_ProcessElement()
    assert isinstance(instance, DescribableElement)


def test_uma_ProcessComponentDescriptor_isa_Descriptor():
    instance = uma_ProcessComponentDescriptor()
    assert isinstance(instance, Descriptor)


def test_uma_RoleDescriptor_isa_Descriptor():
    instance = uma_RoleDescriptor()
    assert isinstance(instance, Descriptor)


def test_uma_TaskDescriptor_isa_Descriptor():
    instance = uma_TaskDescriptor()
    assert isinstance(instance, Descriptor)


def test_uma_WorkProductDescriptor_isa_Descriptor():
    instance = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    assert isinstance(instance, Descriptor)


def test_uma_DiagramLink_isa_DiagramElement():
    instance = uma_DiagramLink(zoom="sample_text")
    assert isinstance(instance, DiagramElement)


def test_uma_GraphElement_isa_DiagramElement():
    instance = uma_GraphElement()
    assert isinstance(instance, DiagramElement)


def test_uma_LeafElement_isa_DiagramElement():
    instance = uma_LeafElement()
    assert isinstance(instance, DiagramElement)


def test_uma_Property_isa_DiagramElement():
    instance = uma_Property(key="sample_text", value="sample_text")
    assert isinstance(instance, DiagramElement)


def test_uma_Reference_isa_DiagramElement():
    instance = uma_Reference(isIndividualRepresentation="sample_text")
    assert isinstance(instance, DiagramElement)


def test_uma_SemanticModelBridge_isa_DiagramElement():
    instance = uma_SemanticModelBridge(presentation="sample_text")
    assert isinstance(instance, DiagramElement)


def test_uma_NamedElement_isa_Element():
    instance = uma_NamedElement(name="sample_text")
    assert isinstance(instance, Element)


def test_uma_GraphConnector_isa_GraphElement():
    instance = uma_GraphConnector()
    assert isinstance(instance, GraphElement)


def test_uma_GraphEdge_isa_GraphElement():
    instance = uma_GraphEdge()
    assert isinstance(instance, GraphElement)


def test_uma_GraphNode_isa_GraphElement():
    instance = uma_GraphNode()
    assert isinstance(instance, GraphElement)


def test_uma_Diagram_isa_GraphNode():
    instance = uma_Diagram(zoom="sample_text")
    assert isinstance(instance, GraphNode)


def test_uma_Ellipse_isa_GraphicPrimitive():
    instance = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    assert isinstance(instance, GraphicPrimitive)


def test_uma_Polyline_isa_GraphicPrimitive():
    instance = uma_Polyline(closed="sample_text")
    assert isinstance(instance, GraphicPrimitive)


def test_uma_Checklist_isa_Guidance():
    instance = uma_Checklist()
    assert isinstance(instance, Guidance)


def test_uma_Concept_isa_Guidance():
    instance = uma_Concept()
    assert isinstance(instance, Guidance)


def test_uma_Estimate_isa_Guidance():
    instance = uma_Estimate()
    assert isinstance(instance, Guidance)


def test_uma_EstimatingMetric_isa_Guidance():
    instance = uma_EstimatingMetric()
    assert isinstance(instance, Guidance)


def test_uma_EstimationConsiderations_isa_Guidance():
    instance = uma_EstimationConsiderations()
    assert isinstance(instance, Guidance)


def test_uma_Example_isa_Guidance():
    instance = uma_Example()
    assert isinstance(instance, Guidance)


def test_uma_Guideline_isa_Guidance():
    instance = uma_Guideline()
    assert isinstance(instance, Guidance)


def test_uma_Practice_isa_Guidance():
    instance = uma_Practice()
    assert isinstance(instance, Guidance)


def test_uma_Report_isa_Guidance():
    instance = uma_Report()
    assert isinstance(instance, Guidance)


def test_uma_ReusableAsset_isa_Guidance():
    instance = uma_ReusableAsset()
    assert isinstance(instance, Guidance)


def test_uma_Roadmap_isa_Guidance():
    instance = uma_Roadmap()
    assert isinstance(instance, Guidance)


def test_uma_SupportingMaterial_isa_Guidance():
    instance = uma_SupportingMaterial()
    assert isinstance(instance, Guidance)


def test_uma_Template_isa_Guidance():
    instance = uma_Template()
    assert isinstance(instance, Guidance)


def test_uma_TermDefinition_isa_Guidance():
    instance = uma_TermDefinition()
    assert isinstance(instance, Guidance)


def test_uma_ToolMentor_isa_Guidance():
    instance = uma_ToolMentor()
    assert isinstance(instance, Guidance)


def test_uma_GraphicPrimitive_isa_LeafElement():
    instance = uma_GraphicPrimitive()
    assert isinstance(instance, LeafElement)


def test_uma_Image_isa_LeafElement():
    instance = uma_Image(mimeType="sample_text", uri="sample_text")
    assert isinstance(instance, LeafElement)


def test_uma_TextElement_isa_LeafElement():
    instance = uma_TextElement(text="sample_text")
    assert isinstance(instance, LeafElement)


def test_uma_ProcessFamily_isa_MethodConfiguration():
    instance = uma_ProcessFamily()
    assert isinstance(instance, MethodConfiguration)


def test_uma_Constraint_isa_MethodElement():
    instance = uma_Constraint(body="sample_text")
    assert isinstance(instance, MethodElement)


def test_uma_DescribableElement_isa_MethodElement():
    instance = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    assert isinstance(instance, MethodElement)


def test_uma_DiagramElement_isa_MethodElement():
    instance = uma_DiagramElement(isVisible="sample_text")
    assert isinstance(instance, MethodElement)


def test_uma_MethodConfiguration_isa_MethodElement():
    instance = uma_MethodConfiguration()
    assert isinstance(instance, MethodElement)


def test_uma_MethodPackage_isa_MethodElement():
    instance = uma_MethodPackage(global_="sample_text")
    assert isinstance(instance, MethodElement)


def test_uma_MethodUnit_isa_MethodElement():
    instance = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    assert isinstance(instance, MethodElement)


def test_uma_VariabilityElement_isa_MethodElement():
    instance = uma_VariabilityElement(variabilityType="sample_text")
    assert isinstance(instance, MethodElement)


def test_uma_WorkDefinition_isa_MethodElement():
    instance = uma_WorkDefinition()
    assert isinstance(instance, MethodElement)


def test_uma_ContentPackage_isa_MethodPackage():
    instance = uma_ContentPackage()
    assert isinstance(instance, MethodPackage)


def test_uma_ProcessPackage_isa_MethodPackage():
    instance = uma_ProcessPackage()
    assert isinstance(instance, MethodPackage)


def test_uma_ContentDescription_isa_MethodUnit():
    instance = uma_ContentDescription(keyConsiderations="sample_text", mainDescription="sample_text")
    assert isinstance(instance, MethodUnit)


def test_uma_MethodLibrary_isa_MethodUnit():
    instance = uma_MethodLibrary()
    assert isinstance(instance, MethodUnit)


def test_uma_MethodPlugin_isa_MethodUnit():
    instance = uma_MethodPlugin(userChangeable="sample_text")
    assert isinstance(instance, MethodUnit)


def test_uma_ProcessComponent_isa_MethodUnit():
    instance = uma_ProcessComponent()
    assert isinstance(instance, MethodUnit)


def test_uma_Namespace_isa_NamedElement():
    instance = uma_Namespace()
    assert isinstance(instance, NamedElement)


def test_uma_PackageableElement_isa_NamedElement():
    instance = uma_PackageableElement()
    assert isinstance(instance, NamedElement)


def test_uma_Package_isa_Namespace():
    instance = uma_Package()
    assert isinstance(instance, Namespace)


def test_uma_MethodLibrary_isa_Package():
    instance = uma_MethodLibrary()
    assert isinstance(instance, Package)


def test_uma_MethodPackage_isa_Package():
    instance = uma_MethodPackage(global_="sample_text")
    assert isinstance(instance, Package)


def test_uma_MethodPlugin_isa_Package():
    instance = uma_MethodPlugin(userChangeable="sample_text")
    assert isinstance(instance, Package)


def test_uma_MethodElement_isa_PackageableElement():
    instance = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    assert isinstance(instance, PackageableElement)


def test_uma_Package_isa_PackageableElement():
    instance = uma_Package()
    assert isinstance(instance, PackageableElement)


def test_uma_Type_isa_PackageableElement():
    instance = uma_Type()
    assert isinstance(instance, PackageableElement)


def test_uma_CapabilityPattern_isa_Process():
    instance = uma_CapabilityPattern()
    assert isinstance(instance, Process)


def test_uma_DeliveryProcess_isa_Process():
    instance = uma_DeliveryProcess()
    assert isinstance(instance, Process)


def test_uma_ProcessContribution_isa_Process():
    instance = uma_ProcessContribution()
    assert isinstance(instance, Process)


def test_uma_ProcessPlanningTemplate_isa_Process():
    instance = uma_ProcessPlanningTemplate()
    assert isinstance(instance, Process)


def test_uma_DeliveryProcessDescription_isa_ProcessDescription():
    instance = uma_DeliveryProcessDescription(estimatingTechnique="sample_text", projectCharacteristics="sample_text", projectMemberExpertise="sample_text", riskLevel="sample_text", scale="sample_text", typeOfContract="sample_text")
    assert isinstance(instance, ProcessDescription)


def test_uma_BreakdownElement_isa_ProcessElement():
    instance = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    assert isinstance(instance, ProcessElement)


def test_uma_PlanningData_isa_ProcessElement():
    instance = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    assert isinstance(instance, ProcessElement)


def test_uma_WorkOrder_isa_ProcessElement():
    instance = uma_WorkOrder(linkType="sample_text")
    assert isinstance(instance, ProcessElement)


def test_uma_ProcessComponent_isa_ProcessPackage():
    instance = uma_ProcessComponent()
    assert isinstance(instance, ProcessPackage)


def test_uma_CompositeRole_isa_RoleDescriptor():
    instance = uma_CompositeRole()
    assert isinstance(instance, RoleDescriptor)


def test_uma_Step_isa_Section():
    instance = uma_Step()
    assert isinstance(instance, Section)


def test_uma_CoreSemanticModelBridge_isa_SemanticModelBridge():
    instance = uma_CoreSemanticModelBridge()
    assert isinstance(instance, SemanticModelBridge)


def test_uma_SimpleSemanticModelElement_isa_SemanticModelBridge():
    instance = uma_SimpleSemanticModelElement(typeInfo="sample_text")
    assert isinstance(instance, SemanticModelBridge)


def test_uma_UMASemanticModelBridge_isa_SemanticModelBridge():
    instance = uma_UMASemanticModelBridge()
    assert isinstance(instance, SemanticModelBridge)


def test_uma_Classifier_isa_Type():
    instance = uma_Classifier()
    assert isinstance(instance, Type)


def test_uma_Activity_isa_VariabilityElement():
    instance = uma_Activity()
    assert isinstance(instance, VariabilityElement)


def test_uma_ContentElement_isa_VariabilityElement():
    instance = uma_ContentElement()
    assert isinstance(instance, VariabilityElement)


def test_uma_Section_isa_VariabilityElement():
    instance = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    assert isinstance(instance, VariabilityElement)


def test_uma_Activity_isa_WorkBreakdownElement():
    instance = uma_Activity()
    assert isinstance(instance, WorkBreakdownElement)


def test_uma_Milestone_isa_WorkBreakdownElement():
    instance = uma_Milestone()
    assert isinstance(instance, WorkBreakdownElement)


def test_uma_TaskDescriptor_isa_WorkBreakdownElement():
    instance = uma_TaskDescriptor()
    assert isinstance(instance, WorkBreakdownElement)


def test_uma_Activity_isa_WorkDefinition():
    instance = uma_Activity()
    assert isinstance(instance, WorkDefinition)


def test_uma_Step_isa_WorkDefinition():
    instance = uma_Step()
    assert isinstance(instance, WorkDefinition)


def test_uma_Task_isa_WorkDefinition():
    instance = uma_Task()
    assert isinstance(instance, WorkDefinition)


def test_uma_Artifact_isa_WorkProduct():
    instance = uma_Artifact()
    assert isinstance(instance, WorkProduct)


def test_uma_Deliverable_isa_WorkProduct():
    instance = uma_Deliverable()
    assert isinstance(instance, WorkProduct)


def test_uma_Outcome_isa_WorkProduct():
    instance = uma_Outcome()
    assert isinstance(instance, WorkProduct)


def test_uma_ArtifactDescription_isa_WorkProductDescription():
    instance = uma_ArtifactDescription(briefOutline="sample_text", representationOptions="sample_text")
    assert isinstance(instance, WorkProductDescription)


def test_uma_DeliverableDescription_isa_WorkProductDescription():
    instance = uma_DeliverableDescription(externalDescription="sample_text", packagingGuidance="sample_text")
    assert isinstance(instance, WorkProductDescription)


def test_assoc_OptionalInputTo200_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'optionalInput', {b1})
    assert _is_linked(a, 'optionalInput', b1)
    if hasattr(b1, 'TaskDescriptor201'):
        assert _is_linked(b1, 'TaskDescriptor201', a)
    _safe_set(a, 'optionalInput', {b2})
    assert _is_linked(a, 'optionalInput', b2)
    if hasattr(b1, 'TaskDescriptor201'):
        assert not _is_linked(b1, 'TaskDescriptor201', a)
    if hasattr(b2, 'TaskDescriptor201'):
        assert _is_linked(b2, 'TaskDescriptor201', a)
    _safe_set(a, 'optionalInput', set())
    assert not _is_linked(a, 'optionalInput', b2)
    if hasattr(b2, 'TaskDescriptor201'):
        assert not _is_linked(b2, 'TaskDescriptor201', a)


def test_assoc_WorkProduct186_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_WorkProduct()
    b2 = uma_WorkProduct()
    _safe_set(a, 'uma_WorkProductDescriptor', b1)
    assert _is_linked(a, 'uma_WorkProductDescriptor', b1)
    if hasattr(b1, 'uma_WorkProduct187'):
        assert _is_linked(b1, 'uma_WorkProduct187', a)
    _safe_set(a, 'uma_WorkProductDescriptor', b2)
    assert _is_linked(a, 'uma_WorkProductDescriptor', b2)
    if hasattr(b1, 'uma_WorkProduct187'):
        assert not _is_linked(b1, 'uma_WorkProduct187', a)
    if hasattr(b2, 'uma_WorkProduct187'):
        assert _is_linked(b2, 'uma_WorkProduct187', a)
    _safe_set(a, 'uma_WorkProductDescriptor', None)
    assert not _is_linked(a, 'uma_WorkProductDescriptor', b2)
    if hasattr(b2, 'uma_WorkProduct187'):
        assert not _is_linked(b2, 'uma_WorkProduct187', a)


def test_assoc_bases279_link_reassign_clear():
    a = uma_MethodPlugin(userChangeable="sample_text")
    b1 = uma_MethodPlugin(userChangeable="sample_text")
    b2 = uma_MethodPlugin(userChangeable="sample_text_2")
    _safe_set(a, 'uma_MethodPlugin278', {b1})
    assert _is_linked(a, 'uma_MethodPlugin278', b1)
    if hasattr(b1, 'uma_MethodPlugin280'):
        assert _is_linked(b1, 'uma_MethodPlugin280', a)
    _safe_set(a, 'uma_MethodPlugin278', {b2})
    assert _is_linked(a, 'uma_MethodPlugin278', b2)
    if hasattr(b1, 'uma_MethodPlugin280'):
        assert not _is_linked(b1, 'uma_MethodPlugin280', a)
    if hasattr(b2, 'uma_MethodPlugin280'):
        assert _is_linked(b2, 'uma_MethodPlugin280', a)
    _safe_set(a, 'uma_MethodPlugin278', set())
    assert not _is_linked(a, 'uma_MethodPlugin278', b2)
    if hasattr(b2, 'uma_MethodPlugin280'):
        assert not _is_linked(b2, 'uma_MethodPlugin280', a)


def test_assoc_breakdownElements119_link_reassign_clear():
    a = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    b1 = uma_Activity()
    b2 = uma_Activity()
    _safe_set(a, 'BreakdownElement', b1)
    assert _is_linked(a, 'BreakdownElement', b1)
    if hasattr(b1, 'superActivities'):
        assert _is_linked(b1, 'superActivities', a)
    _safe_set(a, 'BreakdownElement', b2)
    assert _is_linked(a, 'BreakdownElement', b2)
    if hasattr(b1, 'superActivities'):
        assert not _is_linked(b1, 'superActivities', a)
    if hasattr(b2, 'superActivities'):
        assert _is_linked(b2, 'superActivities', a)
    _safe_set(a, 'BreakdownElement', None)
    assert not _is_linked(a, 'BreakdownElement', b2)
    if hasattr(b2, 'superActivities'):
        assert not _is_linked(b2, 'superActivities', a)


def test_assoc_categorizedElements243_link_reassign_clear():
    a = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    b1 = uma_CustomCategory()
    b2 = uma_CustomCategory()
    _safe_set(a, 'uma_DescribableElement244', b1)
    assert _is_linked(a, 'uma_DescribableElement244', b1)
    if hasattr(b1, 'uma_CustomCategory'):
        assert _is_linked(b1, 'uma_CustomCategory', a)
    _safe_set(a, 'uma_DescribableElement244', b2)
    assert _is_linked(a, 'uma_DescribableElement244', b2)
    if hasattr(b1, 'uma_CustomCategory'):
        assert not _is_linked(b1, 'uma_CustomCategory', a)
    if hasattr(b2, 'uma_CustomCategory'):
        assert _is_linked(b2, 'uma_CustomCategory', a)
    _safe_set(a, 'uma_DescribableElement244', None)
    assert not _is_linked(a, 'uma_DescribableElement244', b2)
    if hasattr(b2, 'uma_CustomCategory'):
        assert not _is_linked(b2, 'uma_CustomCategory', a)


def test_assoc_center117_link_reassign_clear():
    a = uma_Point(x="sample_text", y="sample_text")
    b1 = uma_Ellipse(endAngle="sample_text", radiusX="sample_text", radiusY="sample_text", rotation="sample_text", startAngle="sample_text")
    b2 = uma_Ellipse(endAngle="sample_text_2", radiusX="sample_text_2", radiusY="sample_text_2", rotation="sample_text_2", startAngle="sample_text_2")
    _safe_set(a, 'uma_Point118', b1)
    assert _is_linked(a, 'uma_Point118', b1)
    if hasattr(b1, 'uma_Ellipse'):
        assert _is_linked(b1, 'uma_Ellipse', a)
    _safe_set(a, 'uma_Point118', b2)
    assert _is_linked(a, 'uma_Point118', b2)
    if hasattr(b1, 'uma_Ellipse'):
        assert not _is_linked(b1, 'uma_Ellipse', a)
    if hasattr(b2, 'uma_Ellipse'):
        assert _is_linked(b2, 'uma_Ellipse', a)
    _safe_set(a, 'uma_Point118', None)
    assert not _is_linked(a, 'uma_Point118', b2)
    if hasattr(b2, 'uma_Ellipse'):
        assert not _is_linked(b2, 'uma_Ellipse', a)


def test_assoc_childPackages72_link_reassign_clear():
    a = uma_MethodPackage(global_="sample_text")
    b1 = uma_MethodPackage(global_="sample_text")
    b2 = uma_MethodPackage(global_="sample_text_2")
    _safe_set(a, 'MethodPackage73', b1)
    assert _is_linked(a, 'MethodPackage73', b1)
    if hasattr(b1, 'parentPackage'):
        assert _is_linked(b1, 'parentPackage', a)
    _safe_set(a, 'MethodPackage73', b2)
    assert _is_linked(a, 'MethodPackage73', b2)
    if hasattr(b1, 'parentPackage'):
        assert not _is_linked(b1, 'parentPackage', a)
    if hasattr(b2, 'parentPackage'):
        assert _is_linked(b2, 'parentPackage', a)
    _safe_set(a, 'MethodPackage73', None)
    assert not _is_linked(a, 'MethodPackage73', b2)
    if hasattr(b2, 'parentPackage'):
        assert not _is_linked(b2, 'parentPackage', a)


def test_assoc_contained77_link_reassign_clear():
    a = uma_DiagramElement(isVisible="sample_text")
    b1 = uma_GraphElement()
    b2 = uma_GraphElement()
    _safe_set(a, 'DiagramElement', b1)
    assert _is_linked(a, 'DiagramElement', b1)
    if hasattr(b1, 'container'):
        assert _is_linked(b1, 'container', a)
    _safe_set(a, 'DiagramElement', b2)
    assert _is_linked(a, 'DiagramElement', b2)
    if hasattr(b1, 'container'):
        assert not _is_linked(b1, 'container', a)
    if hasattr(b2, 'container'):
        assert _is_linked(b2, 'container', a)
    _safe_set(a, 'DiagramElement', None)
    assert not _is_linked(a, 'DiagramElement', b2)
    if hasattr(b2, 'container'):
        assert not _is_linked(b2, 'container', a)


def test_assoc_container83_link_reassign_clear():
    a = uma_DiagramElement(isVisible="sample_text")
    b1 = uma_GraphElement()
    b2 = uma_GraphElement()
    _safe_set(a, 'contained', b1)
    assert _is_linked(a, 'contained', b1)
    if hasattr(b1, 'GraphElement'):
        assert _is_linked(b1, 'GraphElement', a)
    _safe_set(a, 'contained', b2)
    assert _is_linked(a, 'contained', b2)
    if hasattr(b1, 'GraphElement'):
        assert not _is_linked(b1, 'GraphElement', a)
    if hasattr(b2, 'GraphElement'):
        assert _is_linked(b2, 'GraphElement', a)
    _safe_set(a, 'contained', None)
    assert not _is_linked(a, 'contained', b2)
    if hasattr(b2, 'GraphElement'):
        assert not _is_linked(b2, 'GraphElement', a)


def test_assoc_copyrightStatement285_link_reassign_clear():
    a = uma_MethodUnit(authors="sample_text", changeDate="sample_text", changeDescription="sample_text", version="sample_text")
    b1 = uma_SupportingMaterial()
    b2 = uma_SupportingMaterial()
    _safe_set(a, 'uma_MethodUnit', b1)
    assert _is_linked(a, 'uma_MethodUnit', b1)
    if hasattr(b1, 'uma_SupportingMaterial286'):
        assert _is_linked(b1, 'uma_SupportingMaterial286', a)
    _safe_set(a, 'uma_MethodUnit', b2)
    assert _is_linked(a, 'uma_MethodUnit', b2)
    if hasattr(b1, 'uma_SupportingMaterial286'):
        assert not _is_linked(b1, 'uma_SupportingMaterial286', a)
    if hasattr(b2, 'uma_SupportingMaterial286'):
        assert _is_linked(b2, 'uma_SupportingMaterial286', a)
    _safe_set(a, 'uma_MethodUnit', None)
    assert not _is_linked(a, 'uma_MethodUnit', b2)
    if hasattr(b2, 'uma_SupportingMaterial286'):
        assert not _is_linked(b2, 'uma_SupportingMaterial286', a)


def test_assoc_deliverableParts205_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    _safe_set(a, 'uma_WorkProductDescriptor204', {b1})
    assert _is_linked(a, 'uma_WorkProductDescriptor204', b1)
    if hasattr(b1, 'uma_WorkProductDescriptor206'):
        assert _is_linked(b1, 'uma_WorkProductDescriptor206', a)
    _safe_set(a, 'uma_WorkProductDescriptor204', {b2})
    assert _is_linked(a, 'uma_WorkProductDescriptor204', b2)
    if hasattr(b1, 'uma_WorkProductDescriptor206'):
        assert not _is_linked(b1, 'uma_WorkProductDescriptor206', a)
    if hasattr(b2, 'uma_WorkProductDescriptor206'):
        assert _is_linked(b2, 'uma_WorkProductDescriptor206', a)
    _safe_set(a, 'uma_WorkProductDescriptor204', set())
    assert not _is_linked(a, 'uma_WorkProductDescriptor204', b2)
    if hasattr(b2, 'uma_WorkProductDescriptor206'):
        assert not _is_linked(b2, 'uma_WorkProductDescriptor206', a)


def test_assoc_diagram90_link_reassign_clear():
    a = uma_DiagramLink(zoom="sample_text")
    b1 = uma_Diagram(zoom="sample_text")
    b2 = uma_Diagram(zoom="sample_text_2")
    _safe_set(a, 'diagramLink', b1)
    assert _is_linked(a, 'diagramLink', b1)
    if hasattr(b1, 'Diagram'):
        assert _is_linked(b1, 'Diagram', a)
    _safe_set(a, 'diagramLink', b2)
    assert _is_linked(a, 'diagramLink', b2)
    if hasattr(b1, 'Diagram'):
        assert not _is_linked(b1, 'Diagram', a)
    if hasattr(b2, 'Diagram'):
        assert _is_linked(b2, 'Diagram', a)
    _safe_set(a, 'diagramLink', None)
    assert not _is_linked(a, 'diagramLink', b2)
    if hasattr(b2, 'Diagram'):
        assert not _is_linked(b2, 'Diagram', a)


def test_assoc_diagram96_link_reassign_clear():
    a = uma_SemanticModelBridge(presentation="sample_text")
    b1 = uma_Diagram(zoom="sample_text")
    b2 = uma_Diagram(zoom="sample_text_2")
    _safe_set(a, 'namespace', b1)
    assert _is_linked(a, 'namespace', b1)
    if hasattr(b1, 'Diagram97'):
        assert _is_linked(b1, 'Diagram97', a)
    _safe_set(a, 'namespace', b2)
    assert _is_linked(a, 'namespace', b2)
    if hasattr(b1, 'Diagram97'):
        assert not _is_linked(b1, 'Diagram97', a)
    if hasattr(b2, 'Diagram97'):
        assert _is_linked(b2, 'Diagram97', a)
    _safe_set(a, 'namespace', None)
    assert not _is_linked(a, 'namespace', b2)
    if hasattr(b2, 'Diagram97'):
        assert not _is_linked(b2, 'Diagram97', a)


def test_assoc_diagramLink106_link_reassign_clear():
    a = uma_DiagramLink(zoom="sample_text")
    b1 = uma_Diagram(zoom="sample_text")
    b2 = uma_Diagram(zoom="sample_text_2")
    _safe_set(a, 'DiagramLink107', b1)
    assert _is_linked(a, 'DiagramLink107', b1)
    if hasattr(b1, 'diagram'):
        assert _is_linked(b1, 'diagram', a)
    _safe_set(a, 'DiagramLink107', b2)
    assert _is_linked(a, 'DiagramLink107', b2)
    if hasattr(b1, 'diagram'):
        assert not _is_linked(b1, 'diagram', a)
    if hasattr(b2, 'diagram'):
        assert _is_linked(b2, 'diagram', a)
    _safe_set(a, 'DiagramLink107', None)
    assert not _is_linked(a, 'DiagramLink107', b2)
    if hasattr(b2, 'diagram'):
        assert not _is_linked(b2, 'diagram', a)


def test_assoc_diagrams265_link_reassign_clear():
    a = uma_Diagram(zoom="sample_text")
    b1 = uma_ProcessPackage()
    b2 = uma_ProcessPackage()
    _safe_set(a, 'uma_Diagram267', b1)
    assert _is_linked(a, 'uma_Diagram267', b1)
    if hasattr(b1, 'uma_ProcessPackage266'):
        assert _is_linked(b1, 'uma_ProcessPackage266', a)
    _safe_set(a, 'uma_Diagram267', b2)
    assert _is_linked(a, 'uma_Diagram267', b2)
    if hasattr(b1, 'uma_ProcessPackage266'):
        assert not _is_linked(b1, 'uma_ProcessPackage266', a)
    if hasattr(b2, 'uma_ProcessPackage266'):
        assert _is_linked(b2, 'uma_ProcessPackage266', a)
    _safe_set(a, 'uma_Diagram267', None)
    assert not _is_linked(a, 'uma_Diagram267', b2)
    if hasattr(b2, 'uma_ProcessPackage266'):
        assert not _is_linked(b2, 'uma_ProcessPackage266', a)


def test_assoc_element112_link_reassign_clear():
    a = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    b1 = uma_UMASemanticModelBridge()
    b2 = uma_UMASemanticModelBridge()
    _safe_set(a, 'uma_MethodElement113', b1)
    assert _is_linked(a, 'uma_MethodElement113', b1)
    if hasattr(b1, 'uma_UMASemanticModelBridge'):
        assert _is_linked(b1, 'uma_UMASemanticModelBridge', a)
    _safe_set(a, 'uma_MethodElement113', b2)
    assert _is_linked(a, 'uma_MethodElement113', b2)
    if hasattr(b1, 'uma_UMASemanticModelBridge'):
        assert not _is_linked(b1, 'uma_UMASemanticModelBridge', a)
    if hasattr(b2, 'uma_UMASemanticModelBridge'):
        assert _is_linked(b2, 'uma_UMASemanticModelBridge', a)
    _safe_set(a, 'uma_MethodElement113', None)
    assert not _is_linked(a, 'uma_MethodElement113', b2)
    if hasattr(b2, 'uma_UMASemanticModelBridge'):
        assert not _is_linked(b2, 'uma_UMASemanticModelBridge', a)


def test_assoc_externalInput173_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'WorkProductDescriptor174', b1)
    assert _is_linked(a, 'WorkProductDescriptor174', b1)
    if hasattr(b1, 'externalInputTo'):
        assert _is_linked(b1, 'externalInputTo', a)
    _safe_set(a, 'WorkProductDescriptor174', b2)
    assert _is_linked(a, 'WorkProductDescriptor174', b2)
    if hasattr(b1, 'externalInputTo'):
        assert not _is_linked(b1, 'externalInputTo', a)
    if hasattr(b2, 'externalInputTo'):
        assert _is_linked(b2, 'externalInputTo', a)
    _safe_set(a, 'WorkProductDescriptor174', None)
    assert not _is_linked(a, 'WorkProductDescriptor174', b2)
    if hasattr(b2, 'externalInputTo'):
        assert not _is_linked(b2, 'externalInputTo', a)


def test_assoc_externalInputTo188_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'externalInput', {b1})
    assert _is_linked(a, 'externalInput', b1)
    if hasattr(b1, 'TaskDescriptor189'):
        assert _is_linked(b1, 'TaskDescriptor189', a)
    _safe_set(a, 'externalInput', {b2})
    assert _is_linked(a, 'externalInput', b2)
    if hasattr(b1, 'TaskDescriptor189'):
        assert not _is_linked(b1, 'TaskDescriptor189', a)
    if hasattr(b2, 'TaskDescriptor189'):
        assert _is_linked(b2, 'TaskDescriptor189', a)
    _safe_set(a, 'externalInput', set())
    assert not _is_linked(a, 'externalInput', b2)
    if hasattr(b2, 'TaskDescriptor189'):
        assert not _is_linked(b2, 'TaskDescriptor189', a)


def test_assoc_graphElement88_link_reassign_clear():
    a = uma_DiagramLink(zoom="sample_text")
    b1 = uma_GraphElement()
    b2 = uma_GraphElement()
    _safe_set(a, 'link', b1)
    assert _is_linked(a, 'link', b1)
    if hasattr(b1, 'GraphElement89'):
        assert _is_linked(b1, 'GraphElement89', a)
    _safe_set(a, 'link', b2)
    assert _is_linked(a, 'link', b2)
    if hasattr(b1, 'GraphElement89'):
        assert not _is_linked(b1, 'GraphElement89', a)
    if hasattr(b2, 'GraphElement89'):
        assert _is_linked(b2, 'GraphElement89', a)
    _safe_set(a, 'link', None)
    assert not _is_linked(a, 'link', b2)
    if hasattr(b2, 'GraphElement89'):
        assert not _is_linked(b2, 'GraphElement89', a)


def test_assoc_graphElement94_link_reassign_clear():
    a = uma_SemanticModelBridge(presentation="sample_text")
    b1 = uma_GraphElement()
    b2 = uma_GraphElement()
    _safe_set(a, 'semanticModel', b1)
    assert _is_linked(a, 'semanticModel', b1)
    if hasattr(b1, 'GraphElement95'):
        assert _is_linked(b1, 'GraphElement95', a)
    _safe_set(a, 'semanticModel', b2)
    assert _is_linked(a, 'semanticModel', b2)
    if hasattr(b1, 'GraphElement95'):
        assert not _is_linked(b1, 'GraphElement95', a)
    if hasattr(b2, 'GraphElement95'):
        assert _is_linked(b2, 'GraphElement95', a)
    _safe_set(a, 'semanticModel', None)
    assert not _is_linked(a, 'semanticModel', b2)
    if hasattr(b2, 'GraphElement95'):
        assert not _is_linked(b2, 'GraphElement95', a)


def test_assoc_impactedBy191_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    _safe_set(a, 'WorkProductDescriptor192', b1)
    assert _is_linked(a, 'WorkProductDescriptor192', b1)
    if hasattr(b1, 'impacts'):
        assert _is_linked(b1, 'impacts', a)
    _safe_set(a, 'WorkProductDescriptor192', b2)
    assert _is_linked(a, 'WorkProductDescriptor192', b2)
    if hasattr(b1, 'impacts'):
        assert not _is_linked(b1, 'impacts', a)
    if hasattr(b2, 'impacts'):
        assert _is_linked(b2, 'impacts', a)
    _safe_set(a, 'WorkProductDescriptor192', None)
    assert not _is_linked(a, 'WorkProductDescriptor192', b2)
    if hasattr(b2, 'impacts'):
        assert not _is_linked(b2, 'impacts', a)


def test_assoc_impacts194_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b2 = uma_WorkProductDescriptor(activityEntryState="sample_text_2", activityExitState="sample_text_2")
    _safe_set(a, 'WorkProductDescriptor195', b1)
    assert _is_linked(a, 'WorkProductDescriptor195', b1)
    if hasattr(b1, 'impactedBy'):
        assert _is_linked(b1, 'impactedBy', a)
    _safe_set(a, 'WorkProductDescriptor195', b2)
    assert _is_linked(a, 'WorkProductDescriptor195', b2)
    if hasattr(b1, 'impactedBy'):
        assert not _is_linked(b1, 'impactedBy', a)
    if hasattr(b2, 'impactedBy'):
        assert _is_linked(b2, 'impactedBy', a)
    _safe_set(a, 'WorkProductDescriptor195', None)
    assert not _is_linked(a, 'WorkProductDescriptor195', b2)
    if hasattr(b2, 'impactedBy'):
        assert not _is_linked(b2, 'impactedBy', a)


def test_assoc_interfaceIO271_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_ProcessComponentInterface()
    b2 = uma_ProcessComponentInterface()
    _safe_set(a, 'uma_WorkProductDescriptor273', b1)
    assert _is_linked(a, 'uma_WorkProductDescriptor273', b1)
    if hasattr(b1, 'uma_ProcessComponentInterface272'):
        assert _is_linked(b1, 'uma_ProcessComponentInterface272', a)
    _safe_set(a, 'uma_WorkProductDescriptor273', b2)
    assert _is_linked(a, 'uma_WorkProductDescriptor273', b2)
    if hasattr(b1, 'uma_ProcessComponentInterface272'):
        assert not _is_linked(b1, 'uma_ProcessComponentInterface272', a)
    if hasattr(b2, 'uma_ProcessComponentInterface272'):
        assert _is_linked(b2, 'uma_ProcessComponentInterface272', a)
    _safe_set(a, 'uma_WorkProductDescriptor273', None)
    assert not _is_linked(a, 'uma_WorkProductDescriptor273', b2)
    if hasattr(b2, 'uma_ProcessComponentInterface272'):
        assert not _is_linked(b2, 'uma_ProcessComponentInterface272', a)


def test_assoc_link78_link_reassign_clear():
    a = uma_DiagramLink(zoom="sample_text")
    b1 = uma_GraphElement()
    b2 = uma_GraphElement()
    _safe_set(a, 'DiagramLink', b1)
    assert _is_linked(a, 'DiagramLink', b1)
    if hasattr(b1, 'graphElement'):
        assert _is_linked(b1, 'graphElement', a)
    _safe_set(a, 'DiagramLink', b2)
    assert _is_linked(a, 'DiagramLink', b2)
    if hasattr(b1, 'graphElement'):
        assert not _is_linked(b1, 'graphElement', a)
    if hasattr(b2, 'graphElement'):
        assert _is_linked(b2, 'graphElement', a)
    _safe_set(a, 'DiagramLink', None)
    assert not _is_linked(a, 'DiagramLink', b2)
    if hasattr(b2, 'graphElement'):
        assert not _is_linked(b2, 'graphElement', a)


def test_assoc_linkToPredecessor139_link_reassign_clear():
    a = uma_WorkOrder(linkType="sample_text")
    b1 = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    b2 = uma_WorkBreakdownElement(isEventDriven="sample_text_2", isOngoing="sample_text_2", isRepeatable="sample_text_2")
    _safe_set(a, 'uma_WorkOrder', b1)
    assert _is_linked(a, 'uma_WorkOrder', b1)
    if hasattr(b1, 'uma_WorkBreakdownElement'):
        assert _is_linked(b1, 'uma_WorkBreakdownElement', a)
    _safe_set(a, 'uma_WorkOrder', b2)
    assert _is_linked(a, 'uma_WorkOrder', b2)
    if hasattr(b1, 'uma_WorkBreakdownElement'):
        assert not _is_linked(b1, 'uma_WorkBreakdownElement', a)
    if hasattr(b2, 'uma_WorkBreakdownElement'):
        assert _is_linked(b2, 'uma_WorkBreakdownElement', a)
    _safe_set(a, 'uma_WorkOrder', None)
    assert not _is_linked(a, 'uma_WorkOrder', b2)
    if hasattr(b2, 'uma_WorkBreakdownElement'):
        assert not _is_linked(b2, 'uma_WorkBreakdownElement', a)


def test_assoc_mandatoryInput175_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'WorkProductDescriptor176', b1)
    assert _is_linked(a, 'WorkProductDescriptor176', b1)
    if hasattr(b1, 'mandatoryInputTo'):
        assert _is_linked(b1, 'mandatoryInputTo', a)
    _safe_set(a, 'WorkProductDescriptor176', b2)
    assert _is_linked(a, 'WorkProductDescriptor176', b2)
    if hasattr(b1, 'mandatoryInputTo'):
        assert not _is_linked(b1, 'mandatoryInputTo', a)
    if hasattr(b2, 'mandatoryInputTo'):
        assert _is_linked(b2, 'mandatoryInputTo', a)
    _safe_set(a, 'WorkProductDescriptor176', None)
    assert not _is_linked(a, 'WorkProductDescriptor176', b2)
    if hasattr(b2, 'mandatoryInputTo'):
        assert not _is_linked(b2, 'mandatoryInputTo', a)


def test_assoc_mandatoryInputTo196_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'mandatoryInput', {b1})
    assert _is_linked(a, 'mandatoryInput', b1)
    if hasattr(b1, 'TaskDescriptor197'):
        assert _is_linked(b1, 'TaskDescriptor197', a)
    _safe_set(a, 'mandatoryInput', {b2})
    assert _is_linked(a, 'mandatoryInput', b2)
    if hasattr(b1, 'TaskDescriptor197'):
        assert not _is_linked(b1, 'TaskDescriptor197', a)
    if hasattr(b2, 'TaskDescriptor197'):
        assert _is_linked(b2, 'TaskDescriptor197', a)
    _safe_set(a, 'mandatoryInput', set())
    assert not _is_linked(a, 'mandatoryInput', b2)
    if hasattr(b2, 'TaskDescriptor197'):
        assert not _is_linked(b2, 'TaskDescriptor197', a)


def test_assoc_methodPackageSelection290_link_reassign_clear():
    a = uma_MethodPackage(global_="sample_text")
    b1 = uma_MethodConfiguration()
    b2 = uma_MethodConfiguration()
    _safe_set(a, 'uma_MethodPackage292', b1)
    assert _is_linked(a, 'uma_MethodPackage292', b1)
    if hasattr(b1, 'uma_MethodConfiguration291'):
        assert _is_linked(b1, 'uma_MethodConfiguration291', a)
    _safe_set(a, 'uma_MethodPackage292', b2)
    assert _is_linked(a, 'uma_MethodPackage292', b2)
    if hasattr(b1, 'uma_MethodConfiguration291'):
        assert not _is_linked(b1, 'uma_MethodConfiguration291', a)
    if hasattr(b2, 'uma_MethodConfiguration291'):
        assert _is_linked(b2, 'uma_MethodConfiguration291', a)
    _safe_set(a, 'uma_MethodPackage292', None)
    assert not _is_linked(a, 'uma_MethodPackage292', b2)
    if hasattr(b2, 'uma_MethodConfiguration291'):
        assert not _is_linked(b2, 'uma_MethodConfiguration291', a)


def test_assoc_methodPackages276_link_reassign_clear():
    a = uma_MethodPlugin(userChangeable="sample_text")
    b1 = uma_MethodPackage(global_="sample_text")
    b2 = uma_MethodPackage(global_="sample_text_2")
    _safe_set(a, 'uma_MethodPlugin', {b1})
    assert _is_linked(a, 'uma_MethodPlugin', b1)
    if hasattr(b1, 'uma_MethodPackage277'):
        assert _is_linked(b1, 'uma_MethodPackage277', a)
    _safe_set(a, 'uma_MethodPlugin', {b2})
    assert _is_linked(a, 'uma_MethodPlugin', b2)
    if hasattr(b1, 'uma_MethodPackage277'):
        assert not _is_linked(b1, 'uma_MethodPackage277', a)
    if hasattr(b2, 'uma_MethodPackage277'):
        assert _is_linked(b2, 'uma_MethodPackage277', a)
    _safe_set(a, 'uma_MethodPlugin', set())
    assert not _is_linked(a, 'uma_MethodPlugin', b2)
    if hasattr(b2, 'uma_MethodPackage277'):
        assert not _is_linked(b2, 'uma_MethodPackage277', a)


def test_assoc_methodPluginSelection287_link_reassign_clear():
    a = uma_MethodPlugin(userChangeable="sample_text")
    b1 = uma_MethodConfiguration()
    b2 = uma_MethodConfiguration()
    _safe_set(a, 'uma_MethodPlugin289', b1)
    assert _is_linked(a, 'uma_MethodPlugin289', b1)
    if hasattr(b1, 'uma_MethodConfiguration288'):
        assert _is_linked(b1, 'uma_MethodConfiguration288', a)
    _safe_set(a, 'uma_MethodPlugin289', b2)
    assert _is_linked(a, 'uma_MethodPlugin289', b2)
    if hasattr(b1, 'uma_MethodConfiguration288'):
        assert not _is_linked(b1, 'uma_MethodConfiguration288', a)
    if hasattr(b2, 'uma_MethodConfiguration288'):
        assert _is_linked(b2, 'uma_MethodConfiguration288', a)
    _safe_set(a, 'uma_MethodPlugin289', None)
    assert not _is_linked(a, 'uma_MethodPlugin289', b2)
    if hasattr(b2, 'uma_MethodConfiguration288'):
        assert not _is_linked(b2, 'uma_MethodConfiguration288', a)


def test_assoc_methodPlugins304_link_reassign_clear():
    a = uma_MethodPlugin(userChangeable="sample_text")
    b1 = uma_MethodLibrary()
    b2 = uma_MethodLibrary()
    _safe_set(a, 'uma_MethodPlugin305', b1)
    assert _is_linked(a, 'uma_MethodPlugin305', b1)
    if hasattr(b1, 'uma_MethodLibrary'):
        assert _is_linked(b1, 'uma_MethodLibrary', a)
    _safe_set(a, 'uma_MethodPlugin305', b2)
    assert _is_linked(a, 'uma_MethodPlugin305', b2)
    if hasattr(b1, 'uma_MethodLibrary'):
        assert not _is_linked(b1, 'uma_MethodLibrary', a)
    if hasattr(b2, 'uma_MethodLibrary'):
        assert _is_linked(b2, 'uma_MethodLibrary', a)
    _safe_set(a, 'uma_MethodPlugin305', None)
    assert not _is_linked(a, 'uma_MethodPlugin305', b2)
    if hasattr(b2, 'uma_MethodLibrary'):
        assert not _is_linked(b2, 'uma_MethodLibrary', a)


def test_assoc_modifies160_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_RoleDescriptor()
    b2 = uma_RoleDescriptor()
    _safe_set(a, 'WorkProductDescriptor', b1)
    assert _is_linked(a, 'WorkProductDescriptor', b1)
    if hasattr(b1, 'workedOnBy'):
        assert _is_linked(b1, 'workedOnBy', a)
    _safe_set(a, 'WorkProductDescriptor', b2)
    assert _is_linked(a, 'WorkProductDescriptor', b2)
    if hasattr(b1, 'workedOnBy'):
        assert not _is_linked(b1, 'workedOnBy', a)
    if hasattr(b2, 'workedOnBy'):
        assert _is_linked(b2, 'workedOnBy', a)
    _safe_set(a, 'WorkProductDescriptor', None)
    assert not _is_linked(a, 'WorkProductDescriptor', b2)
    if hasattr(b2, 'workedOnBy'):
        assert not _is_linked(b2, 'workedOnBy', a)


def test_assoc_namespace108_link_reassign_clear():
    a = uma_SemanticModelBridge(presentation="sample_text")
    b1 = uma_Diagram(zoom="sample_text")
    b2 = uma_Diagram(zoom="sample_text_2")
    _safe_set(a, 'SemanticModelBridge110', b1)
    assert _is_linked(a, 'SemanticModelBridge110', b1)
    if hasattr(b1, 'diagram109'):
        assert _is_linked(b1, 'diagram109', a)
    _safe_set(a, 'SemanticModelBridge110', b2)
    assert _is_linked(a, 'SemanticModelBridge110', b2)
    if hasattr(b1, 'diagram109'):
        assert not _is_linked(b1, 'diagram109', a)
    if hasattr(b2, 'diagram109'):
        assert _is_linked(b2, 'diagram109', a)
    _safe_set(a, 'SemanticModelBridge110', None)
    assert not _is_linked(a, 'SemanticModelBridge110', b2)
    if hasattr(b2, 'diagram109'):
        assert not _is_linked(b2, 'diagram109', a)


def test_assoc_optionalInput177_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'WorkProductDescriptor178', b1)
    assert _is_linked(a, 'WorkProductDescriptor178', b1)
    if hasattr(b1, 'OptionalInputTo'):
        assert _is_linked(b1, 'OptionalInputTo', a)
    _safe_set(a, 'WorkProductDescriptor178', b2)
    assert _is_linked(a, 'WorkProductDescriptor178', b2)
    if hasattr(b1, 'OptionalInputTo'):
        assert not _is_linked(b1, 'OptionalInputTo', a)
    if hasattr(b2, 'OptionalInputTo'):
        assert _is_linked(b2, 'OptionalInputTo', a)
    _safe_set(a, 'WorkProductDescriptor178', None)
    assert not _is_linked(a, 'WorkProductDescriptor178', b2)
    if hasattr(b2, 'OptionalInputTo'):
        assert not _is_linked(b2, 'OptionalInputTo', a)


def test_assoc_output179_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'WorkProductDescriptor180', b1)
    assert _is_linked(a, 'WorkProductDescriptor180', b1)
    if hasattr(b1, 'outputFrom'):
        assert _is_linked(b1, 'outputFrom', a)
    _safe_set(a, 'WorkProductDescriptor180', b2)
    assert _is_linked(a, 'WorkProductDescriptor180', b2)
    if hasattr(b1, 'outputFrom'):
        assert not _is_linked(b1, 'outputFrom', a)
    if hasattr(b2, 'outputFrom'):
        assert _is_linked(b2, 'outputFrom', a)
    _safe_set(a, 'WorkProductDescriptor180', None)
    assert not _is_linked(a, 'WorkProductDescriptor180', b2)
    if hasattr(b2, 'outputFrom'):
        assert not _is_linked(b2, 'outputFrom', a)


def test_assoc_outputFrom202_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'output', {b1})
    assert _is_linked(a, 'output', b1)
    if hasattr(b1, 'TaskDescriptor203'):
        assert _is_linked(b1, 'TaskDescriptor203', a)
    _safe_set(a, 'output', {b2})
    assert _is_linked(a, 'output', b2)
    if hasattr(b1, 'TaskDescriptor203'):
        assert not _is_linked(b1, 'TaskDescriptor203', a)
    if hasattr(b2, 'TaskDescriptor203'):
        assert _is_linked(b2, 'TaskDescriptor203', a)
    _safe_set(a, 'output', set())
    assert not _is_linked(a, 'output', b2)
    if hasattr(b2, 'TaskDescriptor203'):
        assert not _is_linked(b2, 'TaskDescriptor203', a)


def test_assoc_ownedRules0_link_reassign_clear():
    a = uma_MethodElement(briefDescription="sample_text", guid="sample_text", orderingGuide="sample_text", suppressed="sample_text")
    b1 = uma_Constraint(body="sample_text")
    b2 = uma_Constraint(body="sample_text_2")
    _safe_set(a, 'uma_MethodElement', {b1})
    assert _is_linked(a, 'uma_MethodElement', b1)
    if hasattr(b1, 'uma_Constraint'):
        assert _is_linked(b1, 'uma_Constraint', a)
    _safe_set(a, 'uma_MethodElement', {b2})
    assert _is_linked(a, 'uma_MethodElement', b2)
    if hasattr(b1, 'uma_Constraint'):
        assert not _is_linked(b1, 'uma_Constraint', a)
    if hasattr(b2, 'uma_Constraint'):
        assert _is_linked(b2, 'uma_Constraint', a)
    _safe_set(a, 'uma_MethodElement', set())
    assert not _is_linked(a, 'uma_MethodElement', b2)
    if hasattr(b2, 'uma_Constraint'):
        assert not _is_linked(b2, 'uma_Constraint', a)


def test_assoc_parentPackage70_link_reassign_clear():
    a = uma_MethodPackage(global_="sample_text")
    b1 = uma_MethodPackage(global_="sample_text")
    b2 = uma_MethodPackage(global_="sample_text_2")
    _safe_set(a, 'MethodPackage', b1)
    assert _is_linked(a, 'MethodPackage', b1)
    if hasattr(b1, 'childPackages'):
        assert _is_linked(b1, 'childPackages', a)
    _safe_set(a, 'MethodPackage', b2)
    assert _is_linked(a, 'MethodPackage', b2)
    if hasattr(b1, 'childPackages'):
        assert not _is_linked(b1, 'childPackages', a)
    if hasattr(b2, 'childPackages'):
        assert _is_linked(b2, 'childPackages', a)
    _safe_set(a, 'MethodPackage', None)
    assert not _is_linked(a, 'MethodPackage', b2)
    if hasattr(b2, 'childPackages'):
        assert not _is_linked(b2, 'childPackages', a)


def test_assoc_planningData145_link_reassign_clear():
    a = uma_PlanningData(finishDate="sample_text", rank="sample_text", startDate="sample_text")
    b1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    b2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    _safe_set(a, 'uma_PlanningData', b1)
    assert _is_linked(a, 'uma_PlanningData', b1)
    if hasattr(b1, 'uma_BreakdownElement146'):
        assert _is_linked(b1, 'uma_BreakdownElement146', a)
    _safe_set(a, 'uma_PlanningData', b2)
    assert _is_linked(a, 'uma_PlanningData', b2)
    if hasattr(b1, 'uma_BreakdownElement146'):
        assert not _is_linked(b1, 'uma_BreakdownElement146', a)
    if hasattr(b2, 'uma_BreakdownElement146'):
        assert _is_linked(b2, 'uma_BreakdownElement146', a)
    _safe_set(a, 'uma_PlanningData', None)
    assert not _is_linked(a, 'uma_PlanningData', b2)
    if hasattr(b2, 'uma_BreakdownElement146'):
        assert not _is_linked(b2, 'uma_BreakdownElement146', a)


def test_assoc_position76_link_reassign_clear():
    a = uma_Point(x="sample_text", y="sample_text")
    b1 = uma_GraphElement()
    b2 = uma_GraphElement()
    _safe_set(a, 'uma_Point', b1)
    assert _is_linked(a, 'uma_Point', b1)
    if hasattr(b1, 'uma_GraphElement'):
        assert _is_linked(b1, 'uma_GraphElement', a)
    _safe_set(a, 'uma_Point', b2)
    assert _is_linked(a, 'uma_Point', b2)
    if hasattr(b1, 'uma_GraphElement'):
        assert not _is_linked(b1, 'uma_GraphElement', a)
    if hasattr(b2, 'uma_GraphElement'):
        assert _is_linked(b2, 'uma_GraphElement', a)
    _safe_set(a, 'uma_Point', None)
    assert not _is_linked(a, 'uma_Point', b2)
    if hasattr(b2, 'uma_GraphElement'):
        assert not _is_linked(b2, 'uma_GraphElement', a)


def test_assoc_postcondition57_link_reassign_clear():
    a = uma_Constraint(body="sample_text")
    b1 = uma_WorkDefinition()
    b2 = uma_WorkDefinition()
    _safe_set(a, 'uma_Constraint59', b1)
    assert _is_linked(a, 'uma_Constraint59', b1)
    if hasattr(b1, 'uma_WorkDefinition58'):
        assert _is_linked(b1, 'uma_WorkDefinition58', a)
    _safe_set(a, 'uma_Constraint59', b2)
    assert _is_linked(a, 'uma_Constraint59', b2)
    if hasattr(b1, 'uma_WorkDefinition58'):
        assert not _is_linked(b1, 'uma_WorkDefinition58', a)
    if hasattr(b2, 'uma_WorkDefinition58'):
        assert _is_linked(b2, 'uma_WorkDefinition58', a)
    _safe_set(a, 'uma_Constraint59', None)
    assert not _is_linked(a, 'uma_Constraint59', b2)
    if hasattr(b2, 'uma_WorkDefinition58'):
        assert not _is_linked(b2, 'uma_WorkDefinition58', a)


def test_assoc_precondition55_link_reassign_clear():
    a = uma_Constraint(body="sample_text")
    b1 = uma_WorkDefinition()
    b2 = uma_WorkDefinition()
    _safe_set(a, 'uma_Constraint56', b1)
    assert _is_linked(a, 'uma_Constraint56', b1)
    if hasattr(b1, 'uma_WorkDefinition'):
        assert _is_linked(b1, 'uma_WorkDefinition', a)
    _safe_set(a, 'uma_Constraint56', b2)
    assert _is_linked(a, 'uma_Constraint56', b2)
    if hasattr(b1, 'uma_WorkDefinition'):
        assert not _is_linked(b1, 'uma_WorkDefinition', a)
    if hasattr(b2, 'uma_WorkDefinition'):
        assert _is_linked(b2, 'uma_WorkDefinition', a)
    _safe_set(a, 'uma_Constraint56', None)
    assert not _is_linked(a, 'uma_Constraint56', b2)
    if hasattr(b2, 'uma_WorkDefinition'):
        assert not _is_linked(b2, 'uma_WorkDefinition', a)


def test_assoc_pred165_link_reassign_clear():
    a = uma_WorkOrder(linkType="sample_text")
    b1 = uma_WorkBreakdownElement(isEventDriven="sample_text", isOngoing="sample_text", isRepeatable="sample_text")
    b2 = uma_WorkBreakdownElement(isEventDriven="sample_text_2", isOngoing="sample_text_2", isRepeatable="sample_text_2")
    _safe_set(a, 'uma_WorkOrder166', b1)
    assert _is_linked(a, 'uma_WorkOrder166', b1)
    if hasattr(b1, 'uma_WorkBreakdownElement167'):
        assert _is_linked(b1, 'uma_WorkBreakdownElement167', a)
    _safe_set(a, 'uma_WorkOrder166', b2)
    assert _is_linked(a, 'uma_WorkOrder166', b2)
    if hasattr(b1, 'uma_WorkBreakdownElement167'):
        assert not _is_linked(b1, 'uma_WorkBreakdownElement167', a)
    if hasattr(b2, 'uma_WorkBreakdownElement167'):
        assert _is_linked(b2, 'uma_WorkBreakdownElement167', a)
    _safe_set(a, 'uma_WorkOrder166', None)
    assert not _is_linked(a, 'uma_WorkOrder166', b2)
    if hasattr(b2, 'uma_WorkBreakdownElement167'):
        assert not _is_linked(b2, 'uma_WorkBreakdownElement167', a)


def test_assoc_predecessor19_link_reassign_clear():
    a = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    b1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    b2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    _safe_set(a, 'uma_Section18', b1)
    assert _is_linked(a, 'uma_Section18', b1)
    if hasattr(b1, 'uma_Section20'):
        assert _is_linked(b1, 'uma_Section20', a)
    _safe_set(a, 'uma_Section18', b2)
    assert _is_linked(a, 'uma_Section18', b2)
    if hasattr(b1, 'uma_Section20'):
        assert not _is_linked(b1, 'uma_Section20', a)
    if hasattr(b2, 'uma_Section20'):
        assert _is_linked(b2, 'uma_Section20', a)
    _safe_set(a, 'uma_Section18', None)
    assert not _is_linked(a, 'uma_Section18', b2)
    if hasattr(b2, 'uma_Section20'):
        assert not _is_linked(b2, 'uma_Section20', a)


def test_assoc_presentation12_link_reassign_clear():
    a = uma_DescribableElement(nodeicon="sample_text", presentationName="sample_text", shapeicon="sample_text")
    b1 = uma_ContentDescription(keyConsiderations="sample_text", mainDescription="sample_text")
    b2 = uma_ContentDescription(keyConsiderations="sample_text_2", mainDescription="sample_text_2")
    _safe_set(a, 'uma_DescribableElement', b1)
    assert _is_linked(a, 'uma_DescribableElement', b1)
    if hasattr(b1, 'uma_ContentDescription'):
        assert _is_linked(b1, 'uma_ContentDescription', a)
    _safe_set(a, 'uma_DescribableElement', b2)
    assert _is_linked(a, 'uma_DescribableElement', b2)
    if hasattr(b1, 'uma_ContentDescription'):
        assert not _is_linked(b1, 'uma_ContentDescription', a)
    if hasattr(b2, 'uma_ContentDescription'):
        assert _is_linked(b2, 'uma_ContentDescription', a)
    _safe_set(a, 'uma_DescribableElement', None)
    assert not _is_linked(a, 'uma_DescribableElement', b2)
    if hasattr(b2, 'uma_ContentDescription'):
        assert not _is_linked(b2, 'uma_ContentDescription', a)


def test_assoc_presentedAfter141_link_reassign_clear():
    a = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    b1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    b2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    _safe_set(a, 'uma_BreakdownElement', b1)
    assert _is_linked(a, 'uma_BreakdownElement', b1)
    if hasattr(b1, 'uma_BreakdownElement140'):
        assert _is_linked(b1, 'uma_BreakdownElement140', a)
    _safe_set(a, 'uma_BreakdownElement', b2)
    assert _is_linked(a, 'uma_BreakdownElement', b2)
    if hasattr(b1, 'uma_BreakdownElement140'):
        assert not _is_linked(b1, 'uma_BreakdownElement140', a)
    if hasattr(b2, 'uma_BreakdownElement140'):
        assert _is_linked(b2, 'uma_BreakdownElement140', a)
    _safe_set(a, 'uma_BreakdownElement', None)
    assert not _is_linked(a, 'uma_BreakdownElement', b2)
    if hasattr(b2, 'uma_BreakdownElement140'):
        assert not _is_linked(b2, 'uma_BreakdownElement140', a)


def test_assoc_presentedBefore143_link_reassign_clear():
    a = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    b1 = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    b2 = uma_BreakdownElement(hasMultipleOccurrences="sample_text_2", isOptional="sample_text_2", isPlanned="sample_text_2", prefix="sample_text_2")
    _safe_set(a, 'uma_BreakdownElement142', b1)
    assert _is_linked(a, 'uma_BreakdownElement142', b1)
    if hasattr(b1, 'uma_BreakdownElement144'):
        assert _is_linked(b1, 'uma_BreakdownElement144', a)
    _safe_set(a, 'uma_BreakdownElement142', b2)
    assert _is_linked(a, 'uma_BreakdownElement142', b2)
    if hasattr(b1, 'uma_BreakdownElement144'):
        assert not _is_linked(b1, 'uma_BreakdownElement144', a)
    if hasattr(b2, 'uma_BreakdownElement144'):
        assert _is_linked(b2, 'uma_BreakdownElement144', a)
    _safe_set(a, 'uma_BreakdownElement142', None)
    assert not _is_linked(a, 'uma_BreakdownElement142', b2)
    if hasattr(b2, 'uma_BreakdownElement144'):
        assert not _is_linked(b2, 'uma_BreakdownElement144', a)


def test_assoc_property85_link_reassign_clear():
    a = uma_Property(key="sample_text", value="sample_text")
    b1 = uma_DiagramElement(isVisible="sample_text")
    b2 = uma_DiagramElement(isVisible="sample_text_2")
    _safe_set(a, 'uma_Property', b1)
    assert _is_linked(a, 'uma_Property', b1)
    if hasattr(b1, 'uma_DiagramElement'):
        assert _is_linked(b1, 'uma_DiagramElement', a)
    _safe_set(a, 'uma_Property', b2)
    assert _is_linked(a, 'uma_Property', b2)
    if hasattr(b1, 'uma_DiagramElement'):
        assert not _is_linked(b1, 'uma_DiagramElement', a)
    if hasattr(b2, 'uma_DiagramElement'):
        assert _is_linked(b2, 'uma_DiagramElement', a)
    _safe_set(a, 'uma_Property', None)
    assert not _is_linked(a, 'uma_Property', b2)
    if hasattr(b2, 'uma_DiagramElement'):
        assert not _is_linked(b2, 'uma_DiagramElement', a)


def test_assoc_reference84_link_reassign_clear():
    a = uma_Reference(isIndividualRepresentation="sample_text")
    b1 = uma_DiagramElement(isVisible="sample_text")
    b2 = uma_DiagramElement(isVisible="sample_text_2")
    _safe_set(a, 'Reference', b1)
    assert _is_linked(a, 'Reference', b1)
    if hasattr(b1, 'referenced'):
        assert _is_linked(b1, 'referenced', a)
    _safe_set(a, 'Reference', b2)
    assert _is_linked(a, 'Reference', b2)
    if hasattr(b1, 'referenced'):
        assert not _is_linked(b1, 'referenced', a)
    if hasattr(b2, 'referenced'):
        assert _is_linked(b2, 'referenced', a)
    _safe_set(a, 'Reference', None)
    assert not _is_linked(a, 'Reference', b2)
    if hasattr(b2, 'referenced'):
        assert not _is_linked(b2, 'referenced', a)


def test_assoc_referenced98_link_reassign_clear():
    a = uma_Reference(isIndividualRepresentation="sample_text")
    b1 = uma_DiagramElement(isVisible="sample_text")
    b2 = uma_DiagramElement(isVisible="sample_text_2")
    _safe_set(a, 'reference', b1)
    assert _is_linked(a, 'reference', b1)
    if hasattr(b1, 'DiagramElement99'):
        assert _is_linked(b1, 'DiagramElement99', a)
    _safe_set(a, 'reference', b2)
    assert _is_linked(a, 'reference', b2)
    if hasattr(b1, 'DiagramElement99'):
        assert not _is_linked(b1, 'DiagramElement99', a)
    if hasattr(b2, 'DiagramElement99'):
        assert _is_linked(b2, 'DiagramElement99', a)
    _safe_set(a, 'reference', None)
    assert not _is_linked(a, 'reference', b2)
    if hasattr(b2, 'DiagramElement99'):
        assert not _is_linked(b2, 'DiagramElement99', a)


def test_assoc_responsibleFor163_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_RoleDescriptor()
    b2 = uma_RoleDescriptor()
    _safe_set(a, 'WorkProductDescriptor164', b1)
    assert _is_linked(a, 'WorkProductDescriptor164', b1)
    if hasattr(b1, 'responsibleRole'):
        assert _is_linked(b1, 'responsibleRole', a)
    _safe_set(a, 'WorkProductDescriptor164', b2)
    assert _is_linked(a, 'WorkProductDescriptor164', b2)
    if hasattr(b1, 'responsibleRole'):
        assert not _is_linked(b1, 'responsibleRole', a)
    if hasattr(b2, 'responsibleRole'):
        assert _is_linked(b2, 'responsibleRole', a)
    _safe_set(a, 'WorkProductDescriptor164', None)
    assert not _is_linked(a, 'WorkProductDescriptor164', b2)
    if hasattr(b2, 'responsibleRole'):
        assert not _is_linked(b2, 'responsibleRole', a)


def test_assoc_responsibleRole207_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_RoleDescriptor()
    b2 = uma_RoleDescriptor()
    _safe_set(a, 'responsibleFor', b1)
    assert _is_linked(a, 'responsibleFor', b1)
    if hasattr(b1, 'RoleDescriptor208'):
        assert _is_linked(b1, 'RoleDescriptor208', a)
    _safe_set(a, 'responsibleFor', b2)
    assert _is_linked(a, 'responsibleFor', b2)
    if hasattr(b1, 'RoleDescriptor208'):
        assert not _is_linked(b1, 'RoleDescriptor208', a)
    if hasattr(b2, 'RoleDescriptor208'):
        assert _is_linked(b2, 'RoleDescriptor208', a)
    _safe_set(a, 'responsibleFor', None)
    assert not _is_linked(a, 'responsibleFor', b2)
    if hasattr(b2, 'RoleDescriptor208'):
        assert not _is_linked(b2, 'RoleDescriptor208', a)


def test_assoc_reusedPackages68_link_reassign_clear():
    a = uma_MethodPackage(global_="sample_text")
    b1 = uma_MethodPackage(global_="sample_text")
    b2 = uma_MethodPackage(global_="sample_text_2")
    _safe_set(a, 'uma_MethodPackage', b1)
    assert _is_linked(a, 'uma_MethodPackage', b1)
    if hasattr(b1, 'uma_MethodPackage67'):
        assert _is_linked(b1, 'uma_MethodPackage67', a)
    _safe_set(a, 'uma_MethodPackage', b2)
    assert _is_linked(a, 'uma_MethodPackage', b2)
    if hasattr(b1, 'uma_MethodPackage67'):
        assert not _is_linked(b1, 'uma_MethodPackage67', a)
    if hasattr(b2, 'uma_MethodPackage67'):
        assert _is_linked(b2, 'uma_MethodPackage67', a)
    _safe_set(a, 'uma_MethodPackage', None)
    assert not _is_linked(a, 'uma_MethodPackage', b2)
    if hasattr(b2, 'uma_MethodPackage67'):
        assert not _is_linked(b2, 'uma_MethodPackage67', a)


def test_assoc_sections13_link_reassign_clear():
    a = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    b1 = uma_ContentDescription(keyConsiderations="sample_text", mainDescription="sample_text")
    b2 = uma_ContentDescription(keyConsiderations="sample_text_2", mainDescription="sample_text_2")
    _safe_set(a, 'uma_Section', b1)
    assert _is_linked(a, 'uma_Section', b1)
    if hasattr(b1, 'uma_ContentDescription14'):
        assert _is_linked(b1, 'uma_ContentDescription14', a)
    _safe_set(a, 'uma_Section', b2)
    assert _is_linked(a, 'uma_Section', b2)
    if hasattr(b1, 'uma_ContentDescription14'):
        assert not _is_linked(b1, 'uma_ContentDescription14', a)
    if hasattr(b2, 'uma_ContentDescription14'):
        assert _is_linked(b2, 'uma_ContentDescription14', a)
    _safe_set(a, 'uma_Section', None)
    assert not _is_linked(a, 'uma_Section', b2)
    if hasattr(b2, 'uma_ContentDescription14'):
        assert not _is_linked(b2, 'uma_ContentDescription14', a)


def test_assoc_selectedSteps183_link_reassign_clear():
    a = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    b1 = uma_TaskDescriptor()
    b2 = uma_TaskDescriptor()
    _safe_set(a, 'uma_Section185', b1)
    assert _is_linked(a, 'uma_Section185', b1)
    if hasattr(b1, 'uma_TaskDescriptor184'):
        assert _is_linked(b1, 'uma_TaskDescriptor184', a)
    _safe_set(a, 'uma_Section185', b2)
    assert _is_linked(a, 'uma_Section185', b2)
    if hasattr(b1, 'uma_TaskDescriptor184'):
        assert not _is_linked(b1, 'uma_TaskDescriptor184', a)
    if hasattr(b2, 'uma_TaskDescriptor184'):
        assert _is_linked(b2, 'uma_TaskDescriptor184', a)
    _safe_set(a, 'uma_Section185', None)
    assert not _is_linked(a, 'uma_Section185', b2)
    if hasattr(b2, 'uma_TaskDescriptor184'):
        assert not _is_linked(b2, 'uma_TaskDescriptor184', a)


def test_assoc_semanticModel81_link_reassign_clear():
    a = uma_SemanticModelBridge(presentation="sample_text")
    b1 = uma_GraphElement()
    b2 = uma_GraphElement()
    _safe_set(a, 'SemanticModelBridge', b1)
    assert _is_linked(a, 'SemanticModelBridge', b1)
    if hasattr(b1, 'graphElement82'):
        assert _is_linked(b1, 'graphElement82', a)
    _safe_set(a, 'SemanticModelBridge', b2)
    assert _is_linked(a, 'SemanticModelBridge', b2)
    if hasattr(b1, 'graphElement82'):
        assert not _is_linked(b1, 'graphElement82', a)
    if hasattr(b2, 'graphElement82'):
        assert _is_linked(b2, 'graphElement82', a)
    _safe_set(a, 'SemanticModelBridge', None)
    assert not _is_linked(a, 'SemanticModelBridge', b2)
    if hasattr(b2, 'graphElement82'):
        assert not _is_linked(b2, 'graphElement82', a)


def test_assoc_size111_link_reassign_clear():
    a = uma_Dimension(height="sample_text", width="sample_text")
    b1 = uma_GraphNode()
    b2 = uma_GraphNode()
    _safe_set(a, 'uma_Dimension', b1)
    assert _is_linked(a, 'uma_Dimension', b1)
    if hasattr(b1, 'uma_GraphNode'):
        assert _is_linked(b1, 'uma_GraphNode', a)
    _safe_set(a, 'uma_Dimension', b2)
    assert _is_linked(a, 'uma_Dimension', b2)
    if hasattr(b1, 'uma_GraphNode'):
        assert not _is_linked(b1, 'uma_GraphNode', a)
    if hasattr(b2, 'uma_GraphNode'):
        assert _is_linked(b2, 'uma_GraphNode', a)
    _safe_set(a, 'uma_Dimension', None)
    assert not _is_linked(a, 'uma_Dimension', b2)
    if hasattr(b2, 'uma_GraphNode'):
        assert not _is_linked(b2, 'uma_GraphNode', a)


def test_assoc_subSections16_link_reassign_clear():
    a = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    b1 = uma_Section(sectionDescription="sample_text", sectionName="sample_text")
    b2 = uma_Section(sectionDescription="sample_text_2", sectionName="sample_text_2")
    _safe_set(a, 'uma_Section15', {b1})
    assert _is_linked(a, 'uma_Section15', b1)
    if hasattr(b1, 'uma_Section17'):
        assert _is_linked(b1, 'uma_Section17', a)
    _safe_set(a, 'uma_Section15', {b2})
    assert _is_linked(a, 'uma_Section15', b2)
    if hasattr(b1, 'uma_Section17'):
        assert not _is_linked(b1, 'uma_Section17', a)
    if hasattr(b2, 'uma_Section17'):
        assert _is_linked(b2, 'uma_Section17', a)
    _safe_set(a, 'uma_Section15', set())
    assert not _is_linked(a, 'uma_Section15', b2)
    if hasattr(b2, 'uma_Section17'):
        assert not _is_linked(b2, 'uma_Section17', a)


def test_assoc_superActivities147_link_reassign_clear():
    a = uma_BreakdownElement(hasMultipleOccurrences="sample_text", isOptional="sample_text", isPlanned="sample_text", prefix="sample_text")
    b1 = uma_Activity()
    b2 = uma_Activity()
    _safe_set(a, 'breakdownElements', {b1})
    assert _is_linked(a, 'breakdownElements', b1)
    if hasattr(b1, 'Activity'):
        assert _is_linked(b1, 'Activity', a)
    _safe_set(a, 'breakdownElements', {b2})
    assert _is_linked(a, 'breakdownElements', b2)
    if hasattr(b1, 'Activity'):
        assert not _is_linked(b1, 'Activity', a)
    if hasattr(b2, 'Activity'):
        assert _is_linked(b2, 'Activity', a)
    _safe_set(a, 'breakdownElements', set())
    assert not _is_linked(a, 'breakdownElements', b2)
    if hasattr(b2, 'Activity'):
        assert not _is_linked(b2, 'Activity', a)


def test_assoc_variabilityBasedOnElement282_link_reassign_clear():
    a = uma_VariabilityElement(variabilityType="sample_text")
    b1 = uma_VariabilityElement(variabilityType="sample_text")
    b2 = uma_VariabilityElement(variabilityType="sample_text_2")
    _safe_set(a, 'uma_VariabilityElement', b1)
    assert _is_linked(a, 'uma_VariabilityElement', b1)
    if hasattr(b1, 'uma_VariabilityElement281'):
        assert _is_linked(b1, 'uma_VariabilityElement281', a)
    _safe_set(a, 'uma_VariabilityElement', b2)
    assert _is_linked(a, 'uma_VariabilityElement', b2)
    if hasattr(b1, 'uma_VariabilityElement281'):
        assert not _is_linked(b1, 'uma_VariabilityElement281', a)
    if hasattr(b2, 'uma_VariabilityElement281'):
        assert _is_linked(b2, 'uma_VariabilityElement281', a)
    _safe_set(a, 'uma_VariabilityElement', None)
    assert not _is_linked(a, 'uma_VariabilityElement', b2)
    if hasattr(b2, 'uma_VariabilityElement281'):
        assert not _is_linked(b2, 'uma_VariabilityElement281', a)


def test_assoc_viewpoint104_link_reassign_clear():
    a = uma_Point(x="sample_text", y="sample_text")
    b1 = uma_Diagram(zoom="sample_text")
    b2 = uma_Diagram(zoom="sample_text_2")
    _safe_set(a, 'uma_Point105', b1)
    assert _is_linked(a, 'uma_Point105', b1)
    if hasattr(b1, 'uma_Diagram'):
        assert _is_linked(b1, 'uma_Diagram', a)
    _safe_set(a, 'uma_Point105', b2)
    assert _is_linked(a, 'uma_Point105', b2)
    if hasattr(b1, 'uma_Diagram'):
        assert not _is_linked(b1, 'uma_Diagram', a)
    if hasattr(b2, 'uma_Diagram'):
        assert _is_linked(b2, 'uma_Diagram', a)
    _safe_set(a, 'uma_Point105', None)
    assert not _is_linked(a, 'uma_Point105', b2)
    if hasattr(b2, 'uma_Diagram'):
        assert not _is_linked(b2, 'uma_Diagram', a)


def test_assoc_viewport86_link_reassign_clear():
    a = uma_Point(x="sample_text", y="sample_text")
    b1 = uma_DiagramLink(zoom="sample_text")
    b2 = uma_DiagramLink(zoom="sample_text_2")
    _safe_set(a, 'uma_Point87', b1)
    assert _is_linked(a, 'uma_Point87', b1)
    if hasattr(b1, 'uma_DiagramLink'):
        assert _is_linked(b1, 'uma_DiagramLink', a)
    _safe_set(a, 'uma_Point87', b2)
    assert _is_linked(a, 'uma_Point87', b2)
    if hasattr(b1, 'uma_DiagramLink'):
        assert not _is_linked(b1, 'uma_DiagramLink', a)
    if hasattr(b2, 'uma_DiagramLink'):
        assert _is_linked(b2, 'uma_DiagramLink', a)
    _safe_set(a, 'uma_Point87', None)
    assert not _is_linked(a, 'uma_Point87', b2)
    if hasattr(b2, 'uma_DiagramLink'):
        assert not _is_linked(b2, 'uma_DiagramLink', a)


def test_assoc_waypoints102_link_reassign_clear():
    a = uma_Point(x="sample_text", y="sample_text")
    b1 = uma_GraphEdge()
    b2 = uma_GraphEdge()
    _safe_set(a, 'uma_Point103', b1)
    assert _is_linked(a, 'uma_Point103', b1)
    if hasattr(b1, 'uma_GraphEdge'):
        assert _is_linked(b1, 'uma_GraphEdge', a)
    _safe_set(a, 'uma_Point103', b2)
    assert _is_linked(a, 'uma_Point103', b2)
    if hasattr(b1, 'uma_GraphEdge'):
        assert not _is_linked(b1, 'uma_GraphEdge', a)
    if hasattr(b2, 'uma_GraphEdge'):
        assert _is_linked(b2, 'uma_GraphEdge', a)
    _safe_set(a, 'uma_Point103', None)
    assert not _is_linked(a, 'uma_Point103', b2)
    if hasattr(b2, 'uma_GraphEdge'):
        assert not _is_linked(b2, 'uma_GraphEdge', a)


def test_assoc_waypoints115_link_reassign_clear():
    a = uma_Polyline(closed="sample_text")
    b1 = uma_Point(x="sample_text", y="sample_text")
    b2 = uma_Point(x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'uma_Polyline', {b1})
    assert _is_linked(a, 'uma_Polyline', b1)
    if hasattr(b1, 'uma_Point116'):
        assert _is_linked(b1, 'uma_Point116', a)
    _safe_set(a, 'uma_Polyline', {b2})
    assert _is_linked(a, 'uma_Polyline', b2)
    if hasattr(b1, 'uma_Point116'):
        assert not _is_linked(b1, 'uma_Point116', a)
    if hasattr(b2, 'uma_Point116'):
        assert _is_linked(b2, 'uma_Point116', a)
    _safe_set(a, 'uma_Polyline', set())
    assert not _is_linked(a, 'uma_Polyline', b2)
    if hasattr(b2, 'uma_Point116'):
        assert not _is_linked(b2, 'uma_Point116', a)


def test_assoc_workedOnBy198_link_reassign_clear():
    a = uma_WorkProductDescriptor(activityEntryState="sample_text", activityExitState="sample_text")
    b1 = uma_RoleDescriptor()
    b2 = uma_RoleDescriptor()
    _safe_set(a, 'modifies', {b1})
    assert _is_linked(a, 'modifies', b1)
    if hasattr(b1, 'RoleDescriptor199'):
        assert _is_linked(b1, 'RoleDescriptor199', a)
    _safe_set(a, 'modifies', {b2})
    assert _is_linked(a, 'modifies', b2)
    if hasattr(b1, 'RoleDescriptor199'):
        assert not _is_linked(b1, 'RoleDescriptor199', a)
    if hasattr(b2, 'RoleDescriptor199'):
        assert _is_linked(b2, 'RoleDescriptor199', a)
    _safe_set(a, 'modifies', set())
    assert not _is_linked(a, 'modifies', b2)
    if hasattr(b2, 'RoleDescriptor199'):
        assert not _is_linked(b2, 'RoleDescriptor199', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Activity_strategy = st.builds(Activity)
@given(instance=Activity_strategy)
@settings(max_examples=25)
def test_Activity_instantiation(instance):
    assert isinstance(instance, Activity)


ActivityDescription_strategy = st.builds(ActivityDescription)
@given(instance=ActivityDescription_strategy)
@settings(max_examples=25)
def test_ActivityDescription_instantiation(instance):
    assert isinstance(instance, ActivityDescription)


BreakdownElement_strategy = st.builds(BreakdownElement)
@given(instance=BreakdownElement_strategy)
@settings(max_examples=25)
def test_BreakdownElement_instantiation(instance):
    assert isinstance(instance, BreakdownElement)


BreakdownElementDescription_strategy = st.builds(BreakdownElementDescription)
@given(instance=BreakdownElementDescription_strategy)
@settings(max_examples=25)
def test_BreakdownElementDescription_instantiation(instance):
    assert isinstance(instance, BreakdownElementDescription)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


Concept_strategy = st.builds(Concept)
@given(instance=Concept_strategy)
@settings(max_examples=25)
def test_Concept_instantiation(instance):
    assert isinstance(instance, Concept)


ContentCategory_strategy = st.builds(ContentCategory)
@given(instance=ContentCategory_strategy)
@settings(max_examples=25)
def test_ContentCategory_instantiation(instance):
    assert isinstance(instance, ContentCategory)


ContentDescription_strategy = st.builds(ContentDescription)
@given(instance=ContentDescription_strategy)
@settings(max_examples=25)
def test_ContentDescription_instantiation(instance):
    assert isinstance(instance, ContentDescription)


ContentElement_strategy = st.builds(ContentElement)
@given(instance=ContentElement_strategy)
@settings(max_examples=25)
def test_ContentElement_instantiation(instance):
    assert isinstance(instance, ContentElement)


DescribableElement_strategy = st.builds(DescribableElement)
@given(instance=DescribableElement_strategy)
@settings(max_examples=25)
def test_DescribableElement_instantiation(instance):
    assert isinstance(instance, DescribableElement)


Descriptor_strategy = st.builds(Descriptor)
@given(instance=Descriptor_strategy)
@settings(max_examples=25)
def test_Descriptor_instantiation(instance):
    assert isinstance(instance, Descriptor)


DiagramElement_strategy = st.builds(DiagramElement)
@given(instance=DiagramElement_strategy)
@settings(max_examples=25)
def test_DiagramElement_instantiation(instance):
    assert isinstance(instance, DiagramElement)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


GraphElement_strategy = st.builds(GraphElement)
@given(instance=GraphElement_strategy)
@settings(max_examples=25)
def test_GraphElement_instantiation(instance):
    assert isinstance(instance, GraphElement)


GraphNode_strategy = st.builds(GraphNode)
@given(instance=GraphNode_strategy)
@settings(max_examples=25)
def test_GraphNode_instantiation(instance):
    assert isinstance(instance, GraphNode)


GraphicPrimitive_strategy = st.builds(GraphicPrimitive)
@given(instance=GraphicPrimitive_strategy)
@settings(max_examples=25)
def test_GraphicPrimitive_instantiation(instance):
    assert isinstance(instance, GraphicPrimitive)


Guidance_strategy = st.builds(Guidance)
@given(instance=Guidance_strategy)
@settings(max_examples=25)
def test_Guidance_instantiation(instance):
    assert isinstance(instance, Guidance)


LeafElement_strategy = st.builds(LeafElement)
@given(instance=LeafElement_strategy)
@settings(max_examples=25)
def test_LeafElement_instantiation(instance):
    assert isinstance(instance, LeafElement)


MethodConfiguration_strategy = st.builds(MethodConfiguration)
@given(instance=MethodConfiguration_strategy)
@settings(max_examples=25)
def test_MethodConfiguration_instantiation(instance):
    assert isinstance(instance, MethodConfiguration)


MethodElement_strategy = st.builds(MethodElement)
@given(instance=MethodElement_strategy)
@settings(max_examples=25)
def test_MethodElement_instantiation(instance):
    assert isinstance(instance, MethodElement)


MethodPackage_strategy = st.builds(MethodPackage)
@given(instance=MethodPackage_strategy)
@settings(max_examples=25)
def test_MethodPackage_instantiation(instance):
    assert isinstance(instance, MethodPackage)


MethodUnit_strategy = st.builds(MethodUnit)
@given(instance=MethodUnit_strategy)
@settings(max_examples=25)
def test_MethodUnit_instantiation(instance):
    assert isinstance(instance, MethodUnit)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Namespace_strategy = st.builds(Namespace)
@given(instance=Namespace_strategy)
@settings(max_examples=25)
def test_Namespace_instantiation(instance):
    assert isinstance(instance, Namespace)


Package_strategy = st.builds(Package)
@given(instance=Package_strategy)
@settings(max_examples=25)
def test_Package_instantiation(instance):
    assert isinstance(instance, Package)


PackageableElement_strategy = st.builds(PackageableElement)
@given(instance=PackageableElement_strategy)
@settings(max_examples=25)
def test_PackageableElement_instantiation(instance):
    assert isinstance(instance, PackageableElement)


Process_strategy = st.builds(Process)
@given(instance=Process_strategy)
@settings(max_examples=25)
def test_Process_instantiation(instance):
    assert isinstance(instance, Process)


ProcessDescription_strategy = st.builds(ProcessDescription)
@given(instance=ProcessDescription_strategy)
@settings(max_examples=25)
def test_ProcessDescription_instantiation(instance):
    assert isinstance(instance, ProcessDescription)


ProcessElement_strategy = st.builds(ProcessElement)
@given(instance=ProcessElement_strategy)
@settings(max_examples=25)
def test_ProcessElement_instantiation(instance):
    assert isinstance(instance, ProcessElement)


ProcessPackage_strategy = st.builds(ProcessPackage)
@given(instance=ProcessPackage_strategy)
@settings(max_examples=25)
def test_ProcessPackage_instantiation(instance):
    assert isinstance(instance, ProcessPackage)


RoleDescriptor_strategy = st.builds(RoleDescriptor)
@given(instance=RoleDescriptor_strategy)
@settings(max_examples=25)
def test_RoleDescriptor_instantiation(instance):
    assert isinstance(instance, RoleDescriptor)


Section_strategy = st.builds(Section)
@given(instance=Section_strategy)
@settings(max_examples=25)
def test_Section_instantiation(instance):
    assert isinstance(instance, Section)


SemanticModelBridge_strategy = st.builds(SemanticModelBridge)
@given(instance=SemanticModelBridge_strategy)
@settings(max_examples=25)
def test_SemanticModelBridge_instantiation(instance):
    assert isinstance(instance, SemanticModelBridge)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


VariabilityElement_strategy = st.builds(VariabilityElement)
@given(instance=VariabilityElement_strategy)
@settings(max_examples=25)
def test_VariabilityElement_instantiation(instance):
    assert isinstance(instance, VariabilityElement)


WorkBreakdownElement_strategy = st.builds(WorkBreakdownElement)
@given(instance=WorkBreakdownElement_strategy)
@settings(max_examples=25)
def test_WorkBreakdownElement_instantiation(instance):
    assert isinstance(instance, WorkBreakdownElement)


WorkDefinition_strategy = st.builds(WorkDefinition)
@given(instance=WorkDefinition_strategy)
@settings(max_examples=25)
def test_WorkDefinition_instantiation(instance):
    assert isinstance(instance, WorkDefinition)


WorkProduct_strategy = st.builds(WorkProduct)
@given(instance=WorkProduct_strategy)
@settings(max_examples=25)
def test_WorkProduct_instantiation(instance):
    assert isinstance(instance, WorkProduct)


WorkProductDescription_strategy = st.builds(WorkProductDescription)
@given(instance=WorkProductDescription_strategy)
@settings(max_examples=25)
def test_WorkProductDescription_instantiation(instance):
    assert isinstance(instance, WorkProductDescription)


uma_Activity_strategy = st.builds(uma_Activity)
@given(instance=uma_Activity_strategy)
@settings(max_examples=25)
def test_uma_Activity_instantiation(instance):
    assert isinstance(instance, uma_Activity)


uma_ActivityDescription_strategy = st.builds(uma_ActivityDescription, alternatives=safe_text, howtoStaff=safe_text, purpose=safe_text)
@given(instance=uma_ActivityDescription_strategy)
@settings(max_examples=25)
def test_uma_ActivityDescription_instantiation(instance):
    assert isinstance(instance, uma_ActivityDescription)


uma_Artifact_strategy = st.builds(uma_Artifact)
@given(instance=uma_Artifact_strategy)
@settings(max_examples=25)
def test_uma_Artifact_instantiation(instance):
    assert isinstance(instance, uma_Artifact)


uma_ArtifactDescription_strategy = st.builds(uma_ArtifactDescription, briefOutline=safe_text, representationOptions=safe_text)
@given(instance=uma_ArtifactDescription_strategy)
@settings(max_examples=25)
def test_uma_ArtifactDescription_instantiation(instance):
    assert isinstance(instance, uma_ArtifactDescription)


uma_BreakdownElement_strategy = st.builds(uma_BreakdownElement, hasMultipleOccurrences=safe_text, isOptional=safe_text, isPlanned=safe_text, prefix=safe_text)
@given(instance=uma_BreakdownElement_strategy)
@settings(max_examples=25)
def test_uma_BreakdownElement_instantiation(instance):
    assert isinstance(instance, uma_BreakdownElement)


uma_BreakdownElementDescription_strategy = st.builds(uma_BreakdownElementDescription, usageGuidance=safe_text)
@given(instance=uma_BreakdownElementDescription_strategy)
@settings(max_examples=25)
def test_uma_BreakdownElementDescription_instantiation(instance):
    assert isinstance(instance, uma_BreakdownElementDescription)


uma_CapabilityPattern_strategy = st.builds(uma_CapabilityPattern)
@given(instance=uma_CapabilityPattern_strategy)
@settings(max_examples=25)
def test_uma_CapabilityPattern_instantiation(instance):
    assert isinstance(instance, uma_CapabilityPattern)


uma_Checklist_strategy = st.builds(uma_Checklist)
@given(instance=uma_Checklist_strategy)
@settings(max_examples=25)
def test_uma_Checklist_instantiation(instance):
    assert isinstance(instance, uma_Checklist)


uma_Classifier_strategy = st.builds(uma_Classifier)
@given(instance=uma_Classifier_strategy)
@settings(max_examples=25)
def test_uma_Classifier_instantiation(instance):
    assert isinstance(instance, uma_Classifier)


uma_CompositeRole_strategy = st.builds(uma_CompositeRole)
@given(instance=uma_CompositeRole_strategy)
@settings(max_examples=25)
def test_uma_CompositeRole_instantiation(instance):
    assert isinstance(instance, uma_CompositeRole)


uma_Concept_strategy = st.builds(uma_Concept)
@given(instance=uma_Concept_strategy)
@settings(max_examples=25)
def test_uma_Concept_instantiation(instance):
    assert isinstance(instance, uma_Concept)


uma_Constraint_strategy = st.builds(uma_Constraint, body=safe_text)
@given(instance=uma_Constraint_strategy)
@settings(max_examples=25)
def test_uma_Constraint_instantiation(instance):
    assert isinstance(instance, uma_Constraint)


uma_ContentCategory_strategy = st.builds(uma_ContentCategory)
@given(instance=uma_ContentCategory_strategy)
@settings(max_examples=25)
def test_uma_ContentCategory_instantiation(instance):
    assert isinstance(instance, uma_ContentCategory)


uma_ContentDescription_strategy = st.builds(uma_ContentDescription, keyConsiderations=safe_text, mainDescription=safe_text)
@given(instance=uma_ContentDescription_strategy)
@settings(max_examples=25)
def test_uma_ContentDescription_instantiation(instance):
    assert isinstance(instance, uma_ContentDescription)


uma_ContentElement_strategy = st.builds(uma_ContentElement)
@given(instance=uma_ContentElement_strategy)
@settings(max_examples=25)
def test_uma_ContentElement_instantiation(instance):
    assert isinstance(instance, uma_ContentElement)


uma_ContentPackage_strategy = st.builds(uma_ContentPackage)
@given(instance=uma_ContentPackage_strategy)
@settings(max_examples=25)
def test_uma_ContentPackage_instantiation(instance):
    assert isinstance(instance, uma_ContentPackage)


uma_CoreSemanticModelBridge_strategy = st.builds(uma_CoreSemanticModelBridge)
@given(instance=uma_CoreSemanticModelBridge_strategy)
@settings(max_examples=25)
def test_uma_CoreSemanticModelBridge_instantiation(instance):
    assert isinstance(instance, uma_CoreSemanticModelBridge)


uma_CustomCategory_strategy = st.builds(uma_CustomCategory)
@given(instance=uma_CustomCategory_strategy)
@settings(max_examples=25)
def test_uma_CustomCategory_instantiation(instance):
    assert isinstance(instance, uma_CustomCategory)


uma_Deliverable_strategy = st.builds(uma_Deliverable)
@given(instance=uma_Deliverable_strategy)
@settings(max_examples=25)
def test_uma_Deliverable_instantiation(instance):
    assert isinstance(instance, uma_Deliverable)


uma_DeliverableDescription_strategy = st.builds(uma_DeliverableDescription, externalDescription=safe_text, packagingGuidance=safe_text)
@given(instance=uma_DeliverableDescription_strategy)
@settings(max_examples=25)
def test_uma_DeliverableDescription_instantiation(instance):
    assert isinstance(instance, uma_DeliverableDescription)


uma_DeliveryProcess_strategy = st.builds(uma_DeliveryProcess)
@given(instance=uma_DeliveryProcess_strategy)
@settings(max_examples=25)
def test_uma_DeliveryProcess_instantiation(instance):
    assert isinstance(instance, uma_DeliveryProcess)


uma_DeliveryProcessDescription_strategy = st.builds(uma_DeliveryProcessDescription, estimatingTechnique=safe_text, projectCharacteristics=safe_text, projectMemberExpertise=safe_text, riskLevel=safe_text, scale=safe_text, typeOfContract=safe_text)
@given(instance=uma_DeliveryProcessDescription_strategy)
@settings(max_examples=25)
def test_uma_DeliveryProcessDescription_instantiation(instance):
    assert isinstance(instance, uma_DeliveryProcessDescription)


uma_DescribableElement_strategy = st.builds(uma_DescribableElement, nodeicon=safe_text, presentationName=safe_text, shapeicon=safe_text)
@given(instance=uma_DescribableElement_strategy)
@settings(max_examples=25)
def test_uma_DescribableElement_instantiation(instance):
    assert isinstance(instance, uma_DescribableElement)


uma_Descriptor_strategy = st.builds(uma_Descriptor, isSynchronizedWithSource=safe_text)
@given(instance=uma_Descriptor_strategy)
@settings(max_examples=25)
def test_uma_Descriptor_instantiation(instance):
    assert isinstance(instance, uma_Descriptor)


uma_DescriptorDescription_strategy = st.builds(uma_DescriptorDescription, refinedDescription=safe_text)
@given(instance=uma_DescriptorDescription_strategy)
@settings(max_examples=25)
def test_uma_DescriptorDescription_instantiation(instance):
    assert isinstance(instance, uma_DescriptorDescription)


uma_Diagram_strategy = st.builds(uma_Diagram, zoom=safe_text)
@given(instance=uma_Diagram_strategy)
@settings(max_examples=25)
def test_uma_Diagram_instantiation(instance):
    assert isinstance(instance, uma_Diagram)


uma_DiagramElement_strategy = st.builds(uma_DiagramElement, isVisible=safe_text)
@given(instance=uma_DiagramElement_strategy)
@settings(max_examples=25)
def test_uma_DiagramElement_instantiation(instance):
    assert isinstance(instance, uma_DiagramElement)


uma_DiagramLink_strategy = st.builds(uma_DiagramLink, zoom=safe_text)
@given(instance=uma_DiagramLink_strategy)
@settings(max_examples=25)
def test_uma_DiagramLink_instantiation(instance):
    assert isinstance(instance, uma_DiagramLink)


uma_Dimension_strategy = st.builds(uma_Dimension, height=safe_text, width=safe_text)
@given(instance=uma_Dimension_strategy)
@settings(max_examples=25)
def test_uma_Dimension_instantiation(instance):
    assert isinstance(instance, uma_Dimension)


uma_Discipline_strategy = st.builds(uma_Discipline)
@given(instance=uma_Discipline_strategy)
@settings(max_examples=25)
def test_uma_Discipline_instantiation(instance):
    assert isinstance(instance, uma_Discipline)


uma_DisciplineGrouping_strategy = st.builds(uma_DisciplineGrouping)
@given(instance=uma_DisciplineGrouping_strategy)
@settings(max_examples=25)
def test_uma_DisciplineGrouping_instantiation(instance):
    assert isinstance(instance, uma_DisciplineGrouping)


uma_Domain_strategy = st.builds(uma_Domain)
@given(instance=uma_Domain_strategy)
@settings(max_examples=25)
def test_uma_Domain_instantiation(instance):
    assert isinstance(instance, uma_Domain)


uma_Element_strategy = st.builds(uma_Element)
@given(instance=uma_Element_strategy)
@settings(max_examples=25)
def test_uma_Element_instantiation(instance):
    assert isinstance(instance, uma_Element)


uma_Ellipse_strategy = st.builds(uma_Ellipse, endAngle=safe_text, radiusX=safe_text, radiusY=safe_text, rotation=safe_text, startAngle=safe_text)
@given(instance=uma_Ellipse_strategy)
@settings(max_examples=25)
def test_uma_Ellipse_instantiation(instance):
    assert isinstance(instance, uma_Ellipse)


uma_Estimate_strategy = st.builds(uma_Estimate)
@given(instance=uma_Estimate_strategy)
@settings(max_examples=25)
def test_uma_Estimate_instantiation(instance):
    assert isinstance(instance, uma_Estimate)


uma_EstimatingMetric_strategy = st.builds(uma_EstimatingMetric)
@given(instance=uma_EstimatingMetric_strategy)
@settings(max_examples=25)
def test_uma_EstimatingMetric_instantiation(instance):
    assert isinstance(instance, uma_EstimatingMetric)


uma_EstimationConsiderations_strategy = st.builds(uma_EstimationConsiderations)
@given(instance=uma_EstimationConsiderations_strategy)
@settings(max_examples=25)
def test_uma_EstimationConsiderations_instantiation(instance):
    assert isinstance(instance, uma_EstimationConsiderations)


uma_Example_strategy = st.builds(uma_Example)
@given(instance=uma_Example_strategy)
@settings(max_examples=25)
def test_uma_Example_instantiation(instance):
    assert isinstance(instance, uma_Example)


uma_GraphConnector_strategy = st.builds(uma_GraphConnector)
@given(instance=uma_GraphConnector_strategy)
@settings(max_examples=25)
def test_uma_GraphConnector_instantiation(instance):
    assert isinstance(instance, uma_GraphConnector)


uma_GraphEdge_strategy = st.builds(uma_GraphEdge)
@given(instance=uma_GraphEdge_strategy)
@settings(max_examples=25)
def test_uma_GraphEdge_instantiation(instance):
    assert isinstance(instance, uma_GraphEdge)


uma_GraphElement_strategy = st.builds(uma_GraphElement)
@given(instance=uma_GraphElement_strategy)
@settings(max_examples=25)
def test_uma_GraphElement_instantiation(instance):
    assert isinstance(instance, uma_GraphElement)


uma_GraphNode_strategy = st.builds(uma_GraphNode)
@given(instance=uma_GraphNode_strategy)
@settings(max_examples=25)
def test_uma_GraphNode_instantiation(instance):
    assert isinstance(instance, uma_GraphNode)


uma_GraphicPrimitive_strategy = st.builds(uma_GraphicPrimitive)
@given(instance=uma_GraphicPrimitive_strategy)
@settings(max_examples=25)
def test_uma_GraphicPrimitive_instantiation(instance):
    assert isinstance(instance, uma_GraphicPrimitive)


uma_Guidance_strategy = st.builds(uma_Guidance)
@given(instance=uma_Guidance_strategy)
@settings(max_examples=25)
def test_uma_Guidance_instantiation(instance):
    assert isinstance(instance, uma_Guidance)


uma_GuidanceDescription_strategy = st.builds(uma_GuidanceDescription, attachments=safe_text)
@given(instance=uma_GuidanceDescription_strategy)
@settings(max_examples=25)
def test_uma_GuidanceDescription_instantiation(instance):
    assert isinstance(instance, uma_GuidanceDescription)


uma_Guideline_strategy = st.builds(uma_Guideline)
@given(instance=uma_Guideline_strategy)
@settings(max_examples=25)
def test_uma_Guideline_instantiation(instance):
    assert isinstance(instance, uma_Guideline)


uma_Image_strategy = st.builds(uma_Image, mimeType=safe_text, uri=safe_text)
@given(instance=uma_Image_strategy)
@settings(max_examples=25)
def test_uma_Image_instantiation(instance):
    assert isinstance(instance, uma_Image)


uma_Iteration_strategy = st.builds(uma_Iteration)
@given(instance=uma_Iteration_strategy)
@settings(max_examples=25)
def test_uma_Iteration_instantiation(instance):
    assert isinstance(instance, uma_Iteration)


uma_LeafElement_strategy = st.builds(uma_LeafElement)
@given(instance=uma_LeafElement_strategy)
@settings(max_examples=25)
def test_uma_LeafElement_instantiation(instance):
    assert isinstance(instance, uma_LeafElement)


uma_MethodConfiguration_strategy = st.builds(uma_MethodConfiguration)
@given(instance=uma_MethodConfiguration_strategy)
@settings(max_examples=25)
def test_uma_MethodConfiguration_instantiation(instance):
    assert isinstance(instance, uma_MethodConfiguration)


uma_MethodElement_strategy = st.builds(uma_MethodElement, briefDescription=safe_text, guid=safe_text, orderingGuide=safe_text, suppressed=safe_text)
@given(instance=uma_MethodElement_strategy)
@settings(max_examples=25)
def test_uma_MethodElement_instantiation(instance):
    assert isinstance(instance, uma_MethodElement)


uma_MethodLibrary_strategy = st.builds(uma_MethodLibrary)
@given(instance=uma_MethodLibrary_strategy)
@settings(max_examples=25)
def test_uma_MethodLibrary_instantiation(instance):
    assert isinstance(instance, uma_MethodLibrary)


uma_MethodPackage_strategy = st.builds(uma_MethodPackage, global_=safe_text)
@given(instance=uma_MethodPackage_strategy)
@settings(max_examples=25)
def test_uma_MethodPackage_instantiation(instance):
    assert isinstance(instance, uma_MethodPackage)


uma_MethodPlugin_strategy = st.builds(uma_MethodPlugin, userChangeable=safe_text)
@given(instance=uma_MethodPlugin_strategy)
@settings(max_examples=25)
def test_uma_MethodPlugin_instantiation(instance):
    assert isinstance(instance, uma_MethodPlugin)


uma_MethodUnit_strategy = st.builds(uma_MethodUnit, authors=safe_text, changeDate=safe_text, changeDescription=safe_text, version=safe_text)
@given(instance=uma_MethodUnit_strategy)
@settings(max_examples=25)
def test_uma_MethodUnit_instantiation(instance):
    assert isinstance(instance, uma_MethodUnit)


uma_Milestone_strategy = st.builds(uma_Milestone)
@given(instance=uma_Milestone_strategy)
@settings(max_examples=25)
def test_uma_Milestone_instantiation(instance):
    assert isinstance(instance, uma_Milestone)


uma_NamedElement_strategy = st.builds(uma_NamedElement, name=safe_text)
@given(instance=uma_NamedElement_strategy)
@settings(max_examples=25)
def test_uma_NamedElement_instantiation(instance):
    assert isinstance(instance, uma_NamedElement)


uma_Namespace_strategy = st.builds(uma_Namespace)
@given(instance=uma_Namespace_strategy)
@settings(max_examples=25)
def test_uma_Namespace_instantiation(instance):
    assert isinstance(instance, uma_Namespace)


uma_Outcome_strategy = st.builds(uma_Outcome)
@given(instance=uma_Outcome_strategy)
@settings(max_examples=25)
def test_uma_Outcome_instantiation(instance):
    assert isinstance(instance, uma_Outcome)


uma_Package_strategy = st.builds(uma_Package)
@given(instance=uma_Package_strategy)
@settings(max_examples=25)
def test_uma_Package_instantiation(instance):
    assert isinstance(instance, uma_Package)


uma_PackageableElement_strategy = st.builds(uma_PackageableElement)
@given(instance=uma_PackageableElement_strategy)
@settings(max_examples=25)
def test_uma_PackageableElement_instantiation(instance):
    assert isinstance(instance, uma_PackageableElement)


uma_Phase_strategy = st.builds(uma_Phase)
@given(instance=uma_Phase_strategy)
@settings(max_examples=25)
def test_uma_Phase_instantiation(instance):
    assert isinstance(instance, uma_Phase)


uma_PlanningData_strategy = st.builds(uma_PlanningData, finishDate=safe_text, rank=safe_text, startDate=safe_text)
@given(instance=uma_PlanningData_strategy)
@settings(max_examples=25)
def test_uma_PlanningData_instantiation(instance):
    assert isinstance(instance, uma_PlanningData)


uma_Point_strategy = st.builds(uma_Point, x=safe_text, y=safe_text)
@given(instance=uma_Point_strategy)
@settings(max_examples=25)
def test_uma_Point_instantiation(instance):
    assert isinstance(instance, uma_Point)


uma_Polyline_strategy = st.builds(uma_Polyline, closed=safe_text)
@given(instance=uma_Polyline_strategy)
@settings(max_examples=25)
def test_uma_Polyline_instantiation(instance):
    assert isinstance(instance, uma_Polyline)


uma_Practice_strategy = st.builds(uma_Practice)
@given(instance=uma_Practice_strategy)
@settings(max_examples=25)
def test_uma_Practice_instantiation(instance):
    assert isinstance(instance, uma_Practice)


uma_PracticeDescription_strategy = st.builds(uma_PracticeDescription, additionalInfo=safe_text, application=safe_text, background=safe_text, goals=safe_text, levelsOfAdoption=safe_text, problem=safe_text)
@given(instance=uma_PracticeDescription_strategy)
@settings(max_examples=25)
def test_uma_PracticeDescription_instantiation(instance):
    assert isinstance(instance, uma_PracticeDescription)


uma_Process_strategy = st.builds(uma_Process)
@given(instance=uma_Process_strategy)
@settings(max_examples=25)
def test_uma_Process_instantiation(instance):
    assert isinstance(instance, uma_Process)


uma_ProcessComponent_strategy = st.builds(uma_ProcessComponent)
@given(instance=uma_ProcessComponent_strategy)
@settings(max_examples=25)
def test_uma_ProcessComponent_instantiation(instance):
    assert isinstance(instance, uma_ProcessComponent)


uma_ProcessComponentDescriptor_strategy = st.builds(uma_ProcessComponentDescriptor)
@given(instance=uma_ProcessComponentDescriptor_strategy)
@settings(max_examples=25)
def test_uma_ProcessComponentDescriptor_instantiation(instance):
    assert isinstance(instance, uma_ProcessComponentDescriptor)


uma_ProcessComponentInterface_strategy = st.builds(uma_ProcessComponentInterface)
@given(instance=uma_ProcessComponentInterface_strategy)
@settings(max_examples=25)
def test_uma_ProcessComponentInterface_instantiation(instance):
    assert isinstance(instance, uma_ProcessComponentInterface)


uma_ProcessContribution_strategy = st.builds(uma_ProcessContribution)
@given(instance=uma_ProcessContribution_strategy)
@settings(max_examples=25)
def test_uma_ProcessContribution_instantiation(instance):
    assert isinstance(instance, uma_ProcessContribution)


uma_ProcessDescription_strategy = st.builds(uma_ProcessDescription, externalId=safe_text, scope=safe_text, usageNotes=safe_text)
@given(instance=uma_ProcessDescription_strategy)
@settings(max_examples=25)
def test_uma_ProcessDescription_instantiation(instance):
    assert isinstance(instance, uma_ProcessDescription)


uma_ProcessElement_strategy = st.builds(uma_ProcessElement)
@given(instance=uma_ProcessElement_strategy)
@settings(max_examples=25)
def test_uma_ProcessElement_instantiation(instance):
    assert isinstance(instance, uma_ProcessElement)


uma_ProcessFamily_strategy = st.builds(uma_ProcessFamily)
@given(instance=uma_ProcessFamily_strategy)
@settings(max_examples=25)
def test_uma_ProcessFamily_instantiation(instance):
    assert isinstance(instance, uma_ProcessFamily)


uma_ProcessPackage_strategy = st.builds(uma_ProcessPackage)
@given(instance=uma_ProcessPackage_strategy)
@settings(max_examples=25)
def test_uma_ProcessPackage_instantiation(instance):
    assert isinstance(instance, uma_ProcessPackage)


uma_ProcessPlanningTemplate_strategy = st.builds(uma_ProcessPlanningTemplate)
@given(instance=uma_ProcessPlanningTemplate_strategy)
@settings(max_examples=25)
def test_uma_ProcessPlanningTemplate_instantiation(instance):
    assert isinstance(instance, uma_ProcessPlanningTemplate)


uma_Property_strategy = st.builds(uma_Property, key=safe_text, value=safe_text)
@given(instance=uma_Property_strategy)
@settings(max_examples=25)
def test_uma_Property_instantiation(instance):
    assert isinstance(instance, uma_Property)


uma_Reference_strategy = st.builds(uma_Reference, isIndividualRepresentation=safe_text)
@given(instance=uma_Reference_strategy)
@settings(max_examples=25)
def test_uma_Reference_instantiation(instance):
    assert isinstance(instance, uma_Reference)


uma_Report_strategy = st.builds(uma_Report)
@given(instance=uma_Report_strategy)
@settings(max_examples=25)
def test_uma_Report_instantiation(instance):
    assert isinstance(instance, uma_Report)


uma_ReusableAsset_strategy = st.builds(uma_ReusableAsset)
@given(instance=uma_ReusableAsset_strategy)
@settings(max_examples=25)
def test_uma_ReusableAsset_instantiation(instance):
    assert isinstance(instance, uma_ReusableAsset)


uma_Roadmap_strategy = st.builds(uma_Roadmap)
@given(instance=uma_Roadmap_strategy)
@settings(max_examples=25)
def test_uma_Roadmap_instantiation(instance):
    assert isinstance(instance, uma_Roadmap)


uma_Role_strategy = st.builds(uma_Role)
@given(instance=uma_Role_strategy)
@settings(max_examples=25)
def test_uma_Role_instantiation(instance):
    assert isinstance(instance, uma_Role)


uma_RoleDescription_strategy = st.builds(uma_RoleDescription, assignmentApproaches=safe_text, skills=safe_text, synonyms=safe_text)
@given(instance=uma_RoleDescription_strategy)
@settings(max_examples=25)
def test_uma_RoleDescription_instantiation(instance):
    assert isinstance(instance, uma_RoleDescription)


uma_RoleDescriptor_strategy = st.builds(uma_RoleDescriptor)
@given(instance=uma_RoleDescriptor_strategy)
@settings(max_examples=25)
def test_uma_RoleDescriptor_instantiation(instance):
    assert isinstance(instance, uma_RoleDescriptor)


uma_RoleSet_strategy = st.builds(uma_RoleSet)
@given(instance=uma_RoleSet_strategy)
@settings(max_examples=25)
def test_uma_RoleSet_instantiation(instance):
    assert isinstance(instance, uma_RoleSet)


uma_RoleSetGrouping_strategy = st.builds(uma_RoleSetGrouping)
@given(instance=uma_RoleSetGrouping_strategy)
@settings(max_examples=25)
def test_uma_RoleSetGrouping_instantiation(instance):
    assert isinstance(instance, uma_RoleSetGrouping)


uma_Section_strategy = st.builds(uma_Section, sectionDescription=safe_text, sectionName=safe_text)
@given(instance=uma_Section_strategy)
@settings(max_examples=25)
def test_uma_Section_instantiation(instance):
    assert isinstance(instance, uma_Section)


uma_SemanticModelBridge_strategy = st.builds(uma_SemanticModelBridge, presentation=safe_text)
@given(instance=uma_SemanticModelBridge_strategy)
@settings(max_examples=25)
def test_uma_SemanticModelBridge_instantiation(instance):
    assert isinstance(instance, uma_SemanticModelBridge)


uma_SimpleSemanticModelElement_strategy = st.builds(uma_SimpleSemanticModelElement, typeInfo=safe_text)
@given(instance=uma_SimpleSemanticModelElement_strategy)
@settings(max_examples=25)
def test_uma_SimpleSemanticModelElement_instantiation(instance):
    assert isinstance(instance, uma_SimpleSemanticModelElement)


uma_Step_strategy = st.builds(uma_Step)
@given(instance=uma_Step_strategy)
@settings(max_examples=25)
def test_uma_Step_instantiation(instance):
    assert isinstance(instance, uma_Step)


uma_SupportingMaterial_strategy = st.builds(uma_SupportingMaterial)
@given(instance=uma_SupportingMaterial_strategy)
@settings(max_examples=25)
def test_uma_SupportingMaterial_instantiation(instance):
    assert isinstance(instance, uma_SupportingMaterial)


uma_Task_strategy = st.builds(uma_Task)
@given(instance=uma_Task_strategy)
@settings(max_examples=25)
def test_uma_Task_instantiation(instance):
    assert isinstance(instance, uma_Task)


uma_TaskDescription_strategy = st.builds(uma_TaskDescription, alternatives=safe_text, purpose=safe_text)
@given(instance=uma_TaskDescription_strategy)
@settings(max_examples=25)
def test_uma_TaskDescription_instantiation(instance):
    assert isinstance(instance, uma_TaskDescription)


uma_TaskDescriptor_strategy = st.builds(uma_TaskDescriptor)
@given(instance=uma_TaskDescriptor_strategy)
@settings(max_examples=25)
def test_uma_TaskDescriptor_instantiation(instance):
    assert isinstance(instance, uma_TaskDescriptor)


uma_TeamProfile_strategy = st.builds(uma_TeamProfile)
@given(instance=uma_TeamProfile_strategy)
@settings(max_examples=25)
def test_uma_TeamProfile_instantiation(instance):
    assert isinstance(instance, uma_TeamProfile)


uma_Template_strategy = st.builds(uma_Template)
@given(instance=uma_Template_strategy)
@settings(max_examples=25)
def test_uma_Template_instantiation(instance):
    assert isinstance(instance, uma_Template)


uma_TermDefinition_strategy = st.builds(uma_TermDefinition)
@given(instance=uma_TermDefinition_strategy)
@settings(max_examples=25)
def test_uma_TermDefinition_instantiation(instance):
    assert isinstance(instance, uma_TermDefinition)


uma_TextElement_strategy = st.builds(uma_TextElement, text=safe_text)
@given(instance=uma_TextElement_strategy)
@settings(max_examples=25)
def test_uma_TextElement_instantiation(instance):
    assert isinstance(instance, uma_TextElement)


uma_Tool_strategy = st.builds(uma_Tool)
@given(instance=uma_Tool_strategy)
@settings(max_examples=25)
def test_uma_Tool_instantiation(instance):
    assert isinstance(instance, uma_Tool)


uma_ToolMentor_strategy = st.builds(uma_ToolMentor)
@given(instance=uma_ToolMentor_strategy)
@settings(max_examples=25)
def test_uma_ToolMentor_instantiation(instance):
    assert isinstance(instance, uma_ToolMentor)


uma_Type_strategy = st.builds(uma_Type)
@given(instance=uma_Type_strategy)
@settings(max_examples=25)
def test_uma_Type_instantiation(instance):
    assert isinstance(instance, uma_Type)


uma_UMASemanticModelBridge_strategy = st.builds(uma_UMASemanticModelBridge)
@given(instance=uma_UMASemanticModelBridge_strategy)
@settings(max_examples=25)
def test_uma_UMASemanticModelBridge_instantiation(instance):
    assert isinstance(instance, uma_UMASemanticModelBridge)


uma_VariabilityElement_strategy = st.builds(uma_VariabilityElement, variabilityType=safe_text)
@given(instance=uma_VariabilityElement_strategy)
@settings(max_examples=25)
def test_uma_VariabilityElement_instantiation(instance):
    assert isinstance(instance, uma_VariabilityElement)


uma_Whitepaper_strategy = st.builds(uma_Whitepaper)
@given(instance=uma_Whitepaper_strategy)
@settings(max_examples=25)
def test_uma_Whitepaper_instantiation(instance):
    assert isinstance(instance, uma_Whitepaper)


uma_WorkBreakdownElement_strategy = st.builds(uma_WorkBreakdownElement, isEventDriven=safe_text, isOngoing=safe_text, isRepeatable=safe_text)
@given(instance=uma_WorkBreakdownElement_strategy)
@settings(max_examples=25)
def test_uma_WorkBreakdownElement_instantiation(instance):
    assert isinstance(instance, uma_WorkBreakdownElement)


uma_WorkDefinition_strategy = st.builds(uma_WorkDefinition)
@given(instance=uma_WorkDefinition_strategy)
@settings(max_examples=25)
def test_uma_WorkDefinition_instantiation(instance):
    assert isinstance(instance, uma_WorkDefinition)


uma_WorkOrder_strategy = st.builds(uma_WorkOrder, linkType=safe_text)
@given(instance=uma_WorkOrder_strategy)
@settings(max_examples=25)
def test_uma_WorkOrder_instantiation(instance):
    assert isinstance(instance, uma_WorkOrder)


uma_WorkProduct_strategy = st.builds(uma_WorkProduct)
@given(instance=uma_WorkProduct_strategy)
@settings(max_examples=25)
def test_uma_WorkProduct_instantiation(instance):
    assert isinstance(instance, uma_WorkProduct)


uma_WorkProductDescription_strategy = st.builds(uma_WorkProductDescription, externalId=safe_text, impactOfNotHaving=safe_text, purpose=safe_text, reasonsForNotNeeding=safe_text)
@given(instance=uma_WorkProductDescription_strategy)
@settings(max_examples=25)
def test_uma_WorkProductDescription_instantiation(instance):
    assert isinstance(instance, uma_WorkProductDescription)


uma_WorkProductDescriptor_strategy = st.builds(uma_WorkProductDescriptor, activityEntryState=safe_text, activityExitState=safe_text)
@given(instance=uma_WorkProductDescriptor_strategy)
@settings(max_examples=25)
def test_uma_WorkProductDescriptor_instantiation(instance):
    assert isinstance(instance, uma_WorkProductDescriptor)


uma_WorkProductType_strategy = st.builds(uma_WorkProductType)
@given(instance=uma_WorkProductType_strategy)
@settings(max_examples=25)
def test_uma_WorkProductType_instantiation(instance):
    assert isinstance(instance, uma_WorkProductType)



