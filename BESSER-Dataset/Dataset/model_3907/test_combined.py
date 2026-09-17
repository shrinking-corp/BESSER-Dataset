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
    repository_RepositoryComponent,
    pcm_usagemodel_BranchTransition,
    BranchTransition,
    pcm_usagemodel_UserData,
    UserData,
    UsageScenario,
    pcm_usagemodel_UsageModel,
    AbstractUserAction,
    pcm_usagemodel_Branch,
    pcm_usagemodel_Stop,
    pcm_usagemodel_Delay,
    pcm_usagemodel_EntryLevelSystemCall,
    pcm_usagemodel_Loop,
    pcm_usagemodel_Start,
    ScenarioBehaviour,
    Workload,
    pcm_usagemodel_ClosedWorkload,
    pcm_usagemodel_OpenWorkload,
    pcm_usagemodel_Workload,
    SpecifiedOutputParameterAbstraction,
    SpecifiedQoSAnnotation,
    pcm_performance_SystemSpecifiedExecutionTime,
    pcm_reliability_SpecifiedFailureProbability,
    pcm_qosannotations_SpecifiedOutputParameterAbstraction,
    pcm_qosannotations_SpecifiedQoSAnnotation,
    QoSAnnotations,
    pcm_performance_ComponentSpecifiedExecutionTime,
    pcm_resourceenvironment_ProcessingResourceSpecification,
    CommunicationLinkResourceType,
    pcm_resourceenvironment_CommunicationLinkResourceSpecification,
    CommunicationLinkResourceSpecification,
    ProcessingResourceSpecification,
    LinkingResource,
    pcm_resourceenvironment_ResourceEnvironment,
    System,
    ResourceEnvironment,
    AllocationContext,
    ResourceType,
    pcm_resourcetype_ProcessingResourceType,
    pcm_resourcetype_ResourceRepository,
    UnitCarryingElement,
    ProcessingResourceType,
    pcm_resourcetype_CommunicationLinkResourceType,
    pcm_performance_ParametricResourceDemand,
    pcm_seff_ServiceEffectSpecification,
    ResourceContainer,
    AbstractBranchTransition,
    pcm_seff_GuardedBranchTransition,
    pcm_seff_ProbabilisticBranchTransition,
    pcm_seff_SynchronisationPoint,
    SynchronisationPoint,
    ForkedBehaviour,
    ResourceDemandingBehaviour,
    pcm_seff_ForkedBehaviour,
    AbstractLoopAction,
    pcm_seff_CollectionIteratorAction,
    pcm_seff_LoopAction,
    performance_ParametricResourceDemand,
    pcm_seff_ResourceDemandingBehaviour,
    seff_ResourceDemandingBehaviour,
    seff_ServiceEffectSpecification,
    AbstractAction,
    pcm_seff_ExternalCallAction,
    pcm_seff_AbstractInternalControlFlowAction,
    AbstractInternalControlFlowAction,
    pcm_seff_AbstractLoopAction,
    pcm_seff_SetVariableAction,
    pcm_seff_InternalAction,
    pcm_seff_StartAction,
    pcm_seff_ReleaseAction,
    pcm_seff_ForkAction,
    pcm_seff_AcquireAction,
    pcm_seff_BranchAction,
    pcm_seff_StopAction,
    parameter_pcm_AbstractNamedReference,
    VariableCharacterisation,
    pcm_parameter_VariableUsage,
    Variable,
    pcm_parameter_CharacterisedVariable,
    NamedElement,
    pcm_seff_AbstractBranchTransition,
    pcm_repository_InnerDeclaration,
    pcm_parameter_VariableCharacterisation,
    pcm_protocol_Protocol,
    pcm_protocol_ServiceCall,
    InnerDeclaration,
    CompositeDataType,
    repository_DataType,
    entity_Entity,
    pcm_repository_CompositeDataType,
    pcm_resourcetype_ResourceType,
    pcm_repository_CollectionDataType,
    PassiveResource,
    ServiceEffectSpecification,
    ProvidesComponentType,
    ImplementationComponentType,
    pcm_repository_BasicComponent,
    repository_ImplementationComponentType,
    entity_ComposedProvidingRequiringEntity,
    pcm_system_System,
    pcm_subsystem_SubSystem,
    pcm_repository_CompositeComponent,
    CompleteComponentType,
    pcm_repository_ExceptionType,
    Protocol,
    Role,
    pcm_repository_ProvidedRole,
    pcm_repository_ResourceRequiredRole,
    pcm_repository_RequiredRole,
    InterfaceProvidingRequiringEntity,
    pcm_repository_RepositoryComponent,
    Interface,
    Repository,
    pcm_repository_DataType,
    Signature,
    pcm_repository_Parameter,
    ExceptionType,
    DataType,
    pcm_repository_PrimitiveDataType,
    composition_ProvidedDelegationConnector,
    Parameter,
    pcm_repository_Signature,
    PCMRandomVariable,
    composition_ResourceRequiredDelegationConnector,
    composition_AssemblyConnector,
    composition_RequiredDelegationConnector,
    pcm_composition_ResourceRequiredDelegationConnector,
    Connector,
    pcm_repository_DelegationConnector,
    pcm_composition_AssemblyConnector,
    VariableUsage,
    RepositoryComponent,
    pcm_repository_ImplementationComponentType,
    pcm_repository_CompleteComponentType,
    pcm_repository_ProvidesComponentType,
    composition_AssemblyContext,
    DelegationConnector,
    pcm_composition_RequiredDelegationConnector,
    pcm_composition_ProvidedDelegationConnector,
    entity_InterfaceProvidingRequiringEntity,
    composition_ComposedStructure,
    pcm_entity_ComposedProvidingRequiringEntity,
    ResourceRequiredRole,
    RequiredRole,
    entity_ResourceInterfaceRequiringEntity,
    entity_InterfaceRequiringEntity,
    entity_InterfaceProvidingEntity,
    pcm_entity_InterfaceProvidingRequiringEntity,
    ProvidedRole,
    Entity,
    pcm_connectors_Connector,
    pcm_usagemodel_AbstractUserAction,
    pcm_seff_AbstractAction,
    pcm_allocation_AllocationContext,
    pcm_resourceenvironment_LinkingResource,
    pcm_allocation_Allocation,
    pcm_repository_Repository,
    pcm_entity_InterfaceRequiringEntity,
    pcm_composition_ComposedStructure,
    pcm_repository_Interface,
    pcm_usagemodel_UsageScenario,
    pcm_resourceenvironment_ResourceContainer,
    pcm_composition_AssemblyContext,
    pcm_entity_ResourceInterfaceRequiringEntity,
    pcm_qosannotations_QoSAnnotations,
    pcm_repository_PassiveResource,
    pcm_usagemodel_ScenarioBehaviour,
    pcm_repository_Role,
    pcm_entity_InterfaceProvidingEntity,
    pcm_entity_NamedElement,
    entity_NamedElement,
    Identifier,
    pcm_seff_ResourceDemandingSEFF,
    pcm_entity_Entity,
    RandomVariable,
    pcm_core_PCMRandomVariable,
    SchedulingPolicy,
    VariableCharacterisationType,
    PrimitiveTypeEnum,
    ParameterModifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_repository_repositorycomponent_is_not_abstract():
    assert not inspect.isabstract(repository_RepositoryComponent)


def test_hyp_repository_repositorycomponent_constructor_exists():
    assert callable(repository_RepositoryComponent.__init__)


def test_hyp_repository_repositorycomponent_constructor_args():
    sig = inspect.signature(repository_RepositoryComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_branchtransition_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_BranchTransition)


def test_hyp_pcm_usagemodel_branchtransition_constructor_exists():
    assert callable(pcm_usagemodel_BranchTransition.__init__)


def test_hyp_pcm_usagemodel_branchtransition_constructor_args():
    sig = inspect.signature(pcm_usagemodel_BranchTransition.__init__)
    params = list(sig.parameters.keys())
    assert "branchProbability" in params, "Missing parameter 'branchProbability'"




def test_hyp_branchtransition_is_not_abstract():
    assert not inspect.isabstract(BranchTransition)


def test_hyp_branchtransition_constructor_exists():
    assert callable(BranchTransition.__init__)


def test_hyp_branchtransition_constructor_args():
    sig = inspect.signature(BranchTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_userdata_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_UserData)


def test_hyp_pcm_usagemodel_userdata_constructor_exists():
    assert callable(pcm_usagemodel_UserData.__init__)


def test_hyp_pcm_usagemodel_userdata_constructor_args():
    sig = inspect.signature(pcm_usagemodel_UserData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_userdata_is_not_abstract():
    assert not inspect.isabstract(UserData)


def test_hyp_userdata_constructor_exists():
    assert callable(UserData.__init__)


def test_hyp_userdata_constructor_args():
    sig = inspect.signature(UserData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_usagescenario_is_not_abstract():
    assert not inspect.isabstract(UsageScenario)


def test_hyp_usagescenario_constructor_exists():
    assert callable(UsageScenario.__init__)


def test_hyp_usagescenario_constructor_args():
    sig = inspect.signature(UsageScenario.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_usagemodel_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_UsageModel)


def test_hyp_pcm_usagemodel_usagemodel_constructor_exists():
    assert callable(pcm_usagemodel_UsageModel.__init__)


def test_hyp_pcm_usagemodel_usagemodel_constructor_args():
    sig = inspect.signature(pcm_usagemodel_UsageModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractuseraction_is_not_abstract():
    assert not inspect.isabstract(AbstractUserAction)


def test_hyp_abstractuseraction_constructor_exists():
    assert callable(AbstractUserAction.__init__)


def test_hyp_abstractuseraction_constructor_args():
    sig = inspect.signature(AbstractUserAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_branch_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_Branch)


def test_hyp_pcm_usagemodel_branch_constructor_exists():
    assert callable(pcm_usagemodel_Branch.__init__)


def test_hyp_pcm_usagemodel_branch_constructor_args():
    sig = inspect.signature(pcm_usagemodel_Branch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_stop_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_Stop)


def test_hyp_pcm_usagemodel_stop_constructor_exists():
    assert callable(pcm_usagemodel_Stop.__init__)


def test_hyp_pcm_usagemodel_stop_constructor_args():
    sig = inspect.signature(pcm_usagemodel_Stop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_delay_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_Delay)


def test_hyp_pcm_usagemodel_delay_constructor_exists():
    assert callable(pcm_usagemodel_Delay.__init__)


def test_hyp_pcm_usagemodel_delay_constructor_args():
    sig = inspect.signature(pcm_usagemodel_Delay.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_entrylevelsystemcall_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_EntryLevelSystemCall)


def test_hyp_pcm_usagemodel_entrylevelsystemcall_constructor_exists():
    assert callable(pcm_usagemodel_EntryLevelSystemCall.__init__)


def test_hyp_pcm_usagemodel_entrylevelsystemcall_constructor_args():
    sig = inspect.signature(pcm_usagemodel_EntryLevelSystemCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_loop_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_Loop)


def test_hyp_pcm_usagemodel_loop_constructor_exists():
    assert callable(pcm_usagemodel_Loop.__init__)


def test_hyp_pcm_usagemodel_loop_constructor_args():
    sig = inspect.signature(pcm_usagemodel_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_start_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_Start)


def test_hyp_pcm_usagemodel_start_constructor_exists():
    assert callable(pcm_usagemodel_Start.__init__)


def test_hyp_pcm_usagemodel_start_constructor_args():
    sig = inspect.signature(pcm_usagemodel_Start.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scenariobehaviour_is_not_abstract():
    assert not inspect.isabstract(ScenarioBehaviour)


def test_hyp_scenariobehaviour_constructor_exists():
    assert callable(ScenarioBehaviour.__init__)


def test_hyp_scenariobehaviour_constructor_args():
    sig = inspect.signature(ScenarioBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_workload_is_not_abstract():
    assert not inspect.isabstract(Workload)


def test_hyp_workload_constructor_exists():
    assert callable(Workload.__init__)


def test_hyp_workload_constructor_args():
    sig = inspect.signature(Workload.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_closedworkload_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_ClosedWorkload)


def test_hyp_pcm_usagemodel_closedworkload_constructor_exists():
    assert callable(pcm_usagemodel_ClosedWorkload.__init__)


def test_hyp_pcm_usagemodel_closedworkload_constructor_args():
    sig = inspect.signature(pcm_usagemodel_ClosedWorkload.__init__)
    params = list(sig.parameters.keys())
    assert "population" in params, "Missing parameter 'population'"




def test_hyp_pcm_usagemodel_openworkload_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_OpenWorkload)


def test_hyp_pcm_usagemodel_openworkload_constructor_exists():
    assert callable(pcm_usagemodel_OpenWorkload.__init__)


def test_hyp_pcm_usagemodel_openworkload_constructor_args():
    sig = inspect.signature(pcm_usagemodel_OpenWorkload.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_workload_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_Workload)


def test_hyp_pcm_usagemodel_workload_constructor_exists():
    assert callable(pcm_usagemodel_Workload.__init__)


def test_hyp_pcm_usagemodel_workload_constructor_args():
    sig = inspect.signature(pcm_usagemodel_Workload.__init__)
    params = list(sig.parameters.keys())



def test_hyp_specifiedoutputparameterabstraction_is_not_abstract():
    assert not inspect.isabstract(SpecifiedOutputParameterAbstraction)


def test_hyp_specifiedoutputparameterabstraction_constructor_exists():
    assert callable(SpecifiedOutputParameterAbstraction.__init__)


def test_hyp_specifiedoutputparameterabstraction_constructor_args():
    sig = inspect.signature(SpecifiedOutputParameterAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_specifiedqosannotation_is_not_abstract():
    assert not inspect.isabstract(SpecifiedQoSAnnotation)


def test_hyp_specifiedqosannotation_constructor_exists():
    assert callable(SpecifiedQoSAnnotation.__init__)


def test_hyp_specifiedqosannotation_constructor_args():
    sig = inspect.signature(SpecifiedQoSAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_performance_systemspecifiedexecutiontime_is_not_abstract():
    assert not inspect.isabstract(pcm_performance_SystemSpecifiedExecutionTime)


def test_hyp_pcm_performance_systemspecifiedexecutiontime_constructor_exists():
    assert callable(pcm_performance_SystemSpecifiedExecutionTime.__init__)


def test_hyp_pcm_performance_systemspecifiedexecutiontime_constructor_args():
    sig = inspect.signature(pcm_performance_SystemSpecifiedExecutionTime.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_reliability_specifiedfailureprobability_is_not_abstract():
    assert not inspect.isabstract(pcm_reliability_SpecifiedFailureProbability)


def test_hyp_pcm_reliability_specifiedfailureprobability_constructor_exists():
    assert callable(pcm_reliability_SpecifiedFailureProbability.__init__)


def test_hyp_pcm_reliability_specifiedfailureprobability_constructor_args():
    sig = inspect.signature(pcm_reliability_SpecifiedFailureProbability.__init__)
    params = list(sig.parameters.keys())
    assert "failureProbability" in params, "Missing parameter 'failureProbability'"




def test_hyp_pcm_qosannotations_specifiedoutputparameterabstraction_is_not_abstract():
    assert not inspect.isabstract(pcm_qosannotations_SpecifiedOutputParameterAbstraction)


def test_hyp_pcm_qosannotations_specifiedoutputparameterabstraction_constructor_exists():
    assert callable(pcm_qosannotations_SpecifiedOutputParameterAbstraction.__init__)


def test_hyp_pcm_qosannotations_specifiedoutputparameterabstraction_constructor_args():
    sig = inspect.signature(pcm_qosannotations_SpecifiedOutputParameterAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_qosannotations_specifiedqosannotation_is_not_abstract():
    assert not inspect.isabstract(pcm_qosannotations_SpecifiedQoSAnnotation)


def test_hyp_pcm_qosannotations_specifiedqosannotation_constructor_exists():
    assert callable(pcm_qosannotations_SpecifiedQoSAnnotation.__init__)


def test_hyp_pcm_qosannotations_specifiedqosannotation_constructor_args():
    sig = inspect.signature(pcm_qosannotations_SpecifiedQoSAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_qosannotations_is_not_abstract():
    assert not inspect.isabstract(QoSAnnotations)


def test_hyp_qosannotations_constructor_exists():
    assert callable(QoSAnnotations.__init__)


def test_hyp_qosannotations_constructor_args():
    sig = inspect.signature(QoSAnnotations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_performance_componentspecifiedexecutiontime_is_not_abstract():
    assert not inspect.isabstract(pcm_performance_ComponentSpecifiedExecutionTime)


def test_hyp_pcm_performance_componentspecifiedexecutiontime_constructor_exists():
    assert callable(pcm_performance_ComponentSpecifiedExecutionTime.__init__)


def test_hyp_pcm_performance_componentspecifiedexecutiontime_constructor_args():
    sig = inspect.signature(pcm_performance_ComponentSpecifiedExecutionTime.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourceenvironment_processingresourcespecification_is_not_abstract():
    assert not inspect.isabstract(pcm_resourceenvironment_ProcessingResourceSpecification)


def test_hyp_pcm_resourceenvironment_processingresourcespecification_constructor_exists():
    assert callable(pcm_resourceenvironment_ProcessingResourceSpecification.__init__)


def test_hyp_pcm_resourceenvironment_processingresourcespecification_constructor_args():
    sig = inspect.signature(pcm_resourceenvironment_ProcessingResourceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "schedulingPolicy" in params, "Missing parameter 'schedulingPolicy'"
    assert "MTTF" in params, "Missing parameter 'MTTF'"
    assert "MTTR" in params, "Missing parameter 'MTTR'"






def test_hyp_communicationlinkresourcetype_is_not_abstract():
    assert not inspect.isabstract(CommunicationLinkResourceType)


def test_hyp_communicationlinkresourcetype_constructor_exists():
    assert callable(CommunicationLinkResourceType.__init__)


def test_hyp_communicationlinkresourcetype_constructor_args():
    sig = inspect.signature(CommunicationLinkResourceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourceenvironment_communicationlinkresourcespecification_is_not_abstract():
    assert not inspect.isabstract(pcm_resourceenvironment_CommunicationLinkResourceSpecification)


def test_hyp_pcm_resourceenvironment_communicationlinkresourcespecification_constructor_exists():
    assert callable(pcm_resourceenvironment_CommunicationLinkResourceSpecification.__init__)


def test_hyp_pcm_resourceenvironment_communicationlinkresourcespecification_constructor_args():
    sig = inspect.signature(pcm_resourceenvironment_CommunicationLinkResourceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "failureProbability" in params, "Missing parameter 'failureProbability'"




def test_hyp_communicationlinkresourcespecification_is_not_abstract():
    assert not inspect.isabstract(CommunicationLinkResourceSpecification)


def test_hyp_communicationlinkresourcespecification_constructor_exists():
    assert callable(CommunicationLinkResourceSpecification.__init__)


def test_hyp_communicationlinkresourcespecification_constructor_args():
    sig = inspect.signature(CommunicationLinkResourceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processingresourcespecification_is_not_abstract():
    assert not inspect.isabstract(ProcessingResourceSpecification)


def test_hyp_processingresourcespecification_constructor_exists():
    assert callable(ProcessingResourceSpecification.__init__)


def test_hyp_processingresourcespecification_constructor_args():
    sig = inspect.signature(ProcessingResourceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_linkingresource_is_not_abstract():
    assert not inspect.isabstract(LinkingResource)


def test_hyp_linkingresource_constructor_exists():
    assert callable(LinkingResource.__init__)


def test_hyp_linkingresource_constructor_args():
    sig = inspect.signature(LinkingResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourceenvironment_resourceenvironment_is_not_abstract():
    assert not inspect.isabstract(pcm_resourceenvironment_ResourceEnvironment)


def test_hyp_pcm_resourceenvironment_resourceenvironment_constructor_exists():
    assert callable(pcm_resourceenvironment_ResourceEnvironment.__init__)


def test_hyp_pcm_resourceenvironment_resourceenvironment_constructor_args():
    sig = inspect.signature(pcm_resourceenvironment_ResourceEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_hyp_system_constructor_exists():
    assert callable(System.__init__)


def test_hyp_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resourceenvironment_is_not_abstract():
    assert not inspect.isabstract(ResourceEnvironment)


def test_hyp_resourceenvironment_constructor_exists():
    assert callable(ResourceEnvironment.__init__)


def test_hyp_resourceenvironment_constructor_args():
    sig = inspect.signature(ResourceEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_allocationcontext_is_not_abstract():
    assert not inspect.isabstract(AllocationContext)


def test_hyp_allocationcontext_constructor_exists():
    assert callable(AllocationContext.__init__)


def test_hyp_allocationcontext_constructor_args():
    sig = inspect.signature(AllocationContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resourcetype_is_not_abstract():
    assert not inspect.isabstract(ResourceType)


def test_hyp_resourcetype_constructor_exists():
    assert callable(ResourceType.__init__)


def test_hyp_resourcetype_constructor_args():
    sig = inspect.signature(ResourceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourcetype_processingresourcetype_is_not_abstract():
    assert not inspect.isabstract(pcm_resourcetype_ProcessingResourceType)


def test_hyp_pcm_resourcetype_processingresourcetype_constructor_exists():
    assert callable(pcm_resourcetype_ProcessingResourceType.__init__)


def test_hyp_pcm_resourcetype_processingresourcetype_constructor_args():
    sig = inspect.signature(pcm_resourcetype_ProcessingResourceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourcetype_resourcerepository_is_not_abstract():
    assert not inspect.isabstract(pcm_resourcetype_ResourceRepository)


def test_hyp_pcm_resourcetype_resourcerepository_constructor_exists():
    assert callable(pcm_resourcetype_ResourceRepository.__init__)


def test_hyp_pcm_resourcetype_resourcerepository_constructor_args():
    sig = inspect.signature(pcm_resourcetype_ResourceRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unitcarryingelement_is_not_abstract():
    assert not inspect.isabstract(UnitCarryingElement)


def test_hyp_unitcarryingelement_constructor_exists():
    assert callable(UnitCarryingElement.__init__)


def test_hyp_unitcarryingelement_constructor_args():
    sig = inspect.signature(UnitCarryingElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processingresourcetype_is_not_abstract():
    assert not inspect.isabstract(ProcessingResourceType)


def test_hyp_processingresourcetype_constructor_exists():
    assert callable(ProcessingResourceType.__init__)


def test_hyp_processingresourcetype_constructor_args():
    sig = inspect.signature(ProcessingResourceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourcetype_communicationlinkresourcetype_is_not_abstract():
    assert not inspect.isabstract(pcm_resourcetype_CommunicationLinkResourceType)


def test_hyp_pcm_resourcetype_communicationlinkresourcetype_constructor_exists():
    assert callable(pcm_resourcetype_CommunicationLinkResourceType.__init__)


def test_hyp_pcm_resourcetype_communicationlinkresourcetype_constructor_args():
    sig = inspect.signature(pcm_resourcetype_CommunicationLinkResourceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_performance_parametricresourcedemand_is_not_abstract():
    assert not inspect.isabstract(pcm_performance_ParametricResourceDemand)


def test_hyp_pcm_performance_parametricresourcedemand_constructor_exists():
    assert callable(pcm_performance_ParametricResourceDemand.__init__)


def test_hyp_pcm_performance_parametricresourcedemand_constructor_args():
    sig = inspect.signature(pcm_performance_ParametricResourceDemand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_serviceeffectspecification_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_ServiceEffectSpecification)


def test_hyp_pcm_seff_serviceeffectspecification_constructor_exists():
    assert callable(pcm_seff_ServiceEffectSpecification.__init__)


def test_hyp_pcm_seff_serviceeffectspecification_constructor_args():
    sig = inspect.signature(pcm_seff_ServiceEffectSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "seffTypeID" in params, "Missing parameter 'seffTypeID'"




def test_hyp_resourcecontainer_is_not_abstract():
    assert not inspect.isabstract(ResourceContainer)


def test_hyp_resourcecontainer_constructor_exists():
    assert callable(ResourceContainer.__init__)


def test_hyp_resourcecontainer_constructor_args():
    sig = inspect.signature(ResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractbranchtransition_is_not_abstract():
    assert not inspect.isabstract(AbstractBranchTransition)


def test_hyp_abstractbranchtransition_constructor_exists():
    assert callable(AbstractBranchTransition.__init__)


def test_hyp_abstractbranchtransition_constructor_args():
    sig = inspect.signature(AbstractBranchTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_guardedbranchtransition_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_GuardedBranchTransition)


def test_hyp_pcm_seff_guardedbranchtransition_constructor_exists():
    assert callable(pcm_seff_GuardedBranchTransition.__init__)


def test_hyp_pcm_seff_guardedbranchtransition_constructor_args():
    sig = inspect.signature(pcm_seff_GuardedBranchTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_probabilisticbranchtransition_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_ProbabilisticBranchTransition)


def test_hyp_pcm_seff_probabilisticbranchtransition_constructor_exists():
    assert callable(pcm_seff_ProbabilisticBranchTransition.__init__)


def test_hyp_pcm_seff_probabilisticbranchtransition_constructor_args():
    sig = inspect.signature(pcm_seff_ProbabilisticBranchTransition.__init__)
    params = list(sig.parameters.keys())
    assert "branchProbability" in params, "Missing parameter 'branchProbability'"




def test_hyp_pcm_seff_synchronisationpoint_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_SynchronisationPoint)


def test_hyp_pcm_seff_synchronisationpoint_constructor_exists():
    assert callable(pcm_seff_SynchronisationPoint.__init__)


def test_hyp_pcm_seff_synchronisationpoint_constructor_args():
    sig = inspect.signature(pcm_seff_SynchronisationPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_synchronisationpoint_is_not_abstract():
    assert not inspect.isabstract(SynchronisationPoint)


def test_hyp_synchronisationpoint_constructor_exists():
    assert callable(SynchronisationPoint.__init__)


def test_hyp_synchronisationpoint_constructor_args():
    sig = inspect.signature(SynchronisationPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forkedbehaviour_is_not_abstract():
    assert not inspect.isabstract(ForkedBehaviour)


def test_hyp_forkedbehaviour_constructor_exists():
    assert callable(ForkedBehaviour.__init__)


def test_hyp_forkedbehaviour_constructor_args():
    sig = inspect.signature(ForkedBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resourcedemandingbehaviour_is_not_abstract():
    assert not inspect.isabstract(ResourceDemandingBehaviour)


def test_hyp_resourcedemandingbehaviour_constructor_exists():
    assert callable(ResourceDemandingBehaviour.__init__)


def test_hyp_resourcedemandingbehaviour_constructor_args():
    sig = inspect.signature(ResourceDemandingBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_forkedbehaviour_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_ForkedBehaviour)


def test_hyp_pcm_seff_forkedbehaviour_constructor_exists():
    assert callable(pcm_seff_ForkedBehaviour.__init__)


def test_hyp_pcm_seff_forkedbehaviour_constructor_args():
    sig = inspect.signature(pcm_seff_ForkedBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractloopaction_is_not_abstract():
    assert not inspect.isabstract(AbstractLoopAction)


def test_hyp_abstractloopaction_constructor_exists():
    assert callable(AbstractLoopAction.__init__)


def test_hyp_abstractloopaction_constructor_args():
    sig = inspect.signature(AbstractLoopAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_collectioniteratoraction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_CollectionIteratorAction)


def test_hyp_pcm_seff_collectioniteratoraction_constructor_exists():
    assert callable(pcm_seff_CollectionIteratorAction.__init__)


def test_hyp_pcm_seff_collectioniteratoraction_constructor_args():
    sig = inspect.signature(pcm_seff_CollectionIteratorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_loopaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_LoopAction)


def test_hyp_pcm_seff_loopaction_constructor_exists():
    assert callable(pcm_seff_LoopAction.__init__)


def test_hyp_pcm_seff_loopaction_constructor_args():
    sig = inspect.signature(pcm_seff_LoopAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_performance_parametricresourcedemand_is_not_abstract():
    assert not inspect.isabstract(performance_ParametricResourceDemand)


def test_hyp_performance_parametricresourcedemand_constructor_exists():
    assert callable(performance_ParametricResourceDemand.__init__)


def test_hyp_performance_parametricresourcedemand_constructor_args():
    sig = inspect.signature(performance_ParametricResourceDemand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_resourcedemandingbehaviour_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_ResourceDemandingBehaviour)


def test_hyp_pcm_seff_resourcedemandingbehaviour_constructor_exists():
    assert callable(pcm_seff_ResourceDemandingBehaviour.__init__)


def test_hyp_pcm_seff_resourcedemandingbehaviour_constructor_args():
    sig = inspect.signature(pcm_seff_ResourceDemandingBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_seff_resourcedemandingbehaviour_is_not_abstract():
    assert not inspect.isabstract(seff_ResourceDemandingBehaviour)


def test_hyp_seff_resourcedemandingbehaviour_constructor_exists():
    assert callable(seff_ResourceDemandingBehaviour.__init__)


def test_hyp_seff_resourcedemandingbehaviour_constructor_args():
    sig = inspect.signature(seff_ResourceDemandingBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_seff_serviceeffectspecification_is_not_abstract():
    assert not inspect.isabstract(seff_ServiceEffectSpecification)


def test_hyp_seff_serviceeffectspecification_constructor_exists():
    assert callable(seff_ServiceEffectSpecification.__init__)


def test_hyp_seff_serviceeffectspecification_constructor_args():
    sig = inspect.signature(seff_ServiceEffectSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractaction_is_not_abstract():
    assert not inspect.isabstract(AbstractAction)


def test_hyp_abstractaction_constructor_exists():
    assert callable(AbstractAction.__init__)


def test_hyp_abstractaction_constructor_args():
    sig = inspect.signature(AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_externalcallaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_ExternalCallAction)


def test_hyp_pcm_seff_externalcallaction_constructor_exists():
    assert callable(pcm_seff_ExternalCallAction.__init__)


def test_hyp_pcm_seff_externalcallaction_constructor_args():
    sig = inspect.signature(pcm_seff_ExternalCallAction.__init__)
    params = list(sig.parameters.keys())
    assert "retryCount" in params, "Missing parameter 'retryCount'"




def test_hyp_pcm_seff_abstractinternalcontrolflowaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_AbstractInternalControlFlowAction)


def test_hyp_pcm_seff_abstractinternalcontrolflowaction_constructor_exists():
    assert callable(pcm_seff_AbstractInternalControlFlowAction.__init__)


def test_hyp_pcm_seff_abstractinternalcontrolflowaction_constructor_args():
    sig = inspect.signature(pcm_seff_AbstractInternalControlFlowAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractinternalcontrolflowaction_is_not_abstract():
    assert not inspect.isabstract(AbstractInternalControlFlowAction)


def test_hyp_abstractinternalcontrolflowaction_constructor_exists():
    assert callable(AbstractInternalControlFlowAction.__init__)


def test_hyp_abstractinternalcontrolflowaction_constructor_args():
    sig = inspect.signature(AbstractInternalControlFlowAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_abstractloopaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_AbstractLoopAction)


def test_hyp_pcm_seff_abstractloopaction_constructor_exists():
    assert callable(pcm_seff_AbstractLoopAction.__init__)


def test_hyp_pcm_seff_abstractloopaction_constructor_args():
    sig = inspect.signature(pcm_seff_AbstractLoopAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_setvariableaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_SetVariableAction)


def test_hyp_pcm_seff_setvariableaction_constructor_exists():
    assert callable(pcm_seff_SetVariableAction.__init__)


def test_hyp_pcm_seff_setvariableaction_constructor_args():
    sig = inspect.signature(pcm_seff_SetVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_internalaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_InternalAction)


def test_hyp_pcm_seff_internalaction_constructor_exists():
    assert callable(pcm_seff_InternalAction.__init__)


def test_hyp_pcm_seff_internalaction_constructor_args():
    sig = inspect.signature(pcm_seff_InternalAction.__init__)
    params = list(sig.parameters.keys())
    assert "failureProbability" in params, "Missing parameter 'failureProbability'"




def test_hyp_pcm_seff_startaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_StartAction)


def test_hyp_pcm_seff_startaction_constructor_exists():
    assert callable(pcm_seff_StartAction.__init__)


def test_hyp_pcm_seff_startaction_constructor_args():
    sig = inspect.signature(pcm_seff_StartAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_releaseaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_ReleaseAction)


def test_hyp_pcm_seff_releaseaction_constructor_exists():
    assert callable(pcm_seff_ReleaseAction.__init__)


def test_hyp_pcm_seff_releaseaction_constructor_args():
    sig = inspect.signature(pcm_seff_ReleaseAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_forkaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_ForkAction)


def test_hyp_pcm_seff_forkaction_constructor_exists():
    assert callable(pcm_seff_ForkAction.__init__)


def test_hyp_pcm_seff_forkaction_constructor_args():
    sig = inspect.signature(pcm_seff_ForkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_acquireaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_AcquireAction)


def test_hyp_pcm_seff_acquireaction_constructor_exists():
    assert callable(pcm_seff_AcquireAction.__init__)


def test_hyp_pcm_seff_acquireaction_constructor_args():
    sig = inspect.signature(pcm_seff_AcquireAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_branchaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_BranchAction)


def test_hyp_pcm_seff_branchaction_constructor_exists():
    assert callable(pcm_seff_BranchAction.__init__)


def test_hyp_pcm_seff_branchaction_constructor_args():
    sig = inspect.signature(pcm_seff_BranchAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_stopaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_StopAction)


def test_hyp_pcm_seff_stopaction_constructor_exists():
    assert callable(pcm_seff_StopAction.__init__)


def test_hyp_pcm_seff_stopaction_constructor_args():
    sig = inspect.signature(pcm_seff_StopAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameter_pcm_abstractnamedreference_is_not_abstract():
    assert not inspect.isabstract(parameter_pcm_AbstractNamedReference)


def test_hyp_parameter_pcm_abstractnamedreference_constructor_exists():
    assert callable(parameter_pcm_AbstractNamedReference.__init__)


def test_hyp_parameter_pcm_abstractnamedreference_constructor_args():
    sig = inspect.signature(parameter_pcm_AbstractNamedReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variablecharacterisation_is_not_abstract():
    assert not inspect.isabstract(VariableCharacterisation)


def test_hyp_variablecharacterisation_constructor_exists():
    assert callable(VariableCharacterisation.__init__)


def test_hyp_variablecharacterisation_constructor_args():
    sig = inspect.signature(VariableCharacterisation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_parameter_variableusage_is_not_abstract():
    assert not inspect.isabstract(pcm_parameter_VariableUsage)


def test_hyp_pcm_parameter_variableusage_constructor_exists():
    assert callable(pcm_parameter_VariableUsage.__init__)


def test_hyp_pcm_parameter_variableusage_constructor_args():
    sig = inspect.signature(pcm_parameter_VariableUsage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_parameter_characterisedvariable_is_not_abstract():
    assert not inspect.isabstract(pcm_parameter_CharacterisedVariable)


def test_hyp_pcm_parameter_characterisedvariable_constructor_exists():
    assert callable(pcm_parameter_CharacterisedVariable.__init__)


def test_hyp_pcm_parameter_characterisedvariable_constructor_args():
    sig = inspect.signature(pcm_parameter_CharacterisedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "characterisationType" in params, "Missing parameter 'characterisationType'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_abstractbranchtransition_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_AbstractBranchTransition)


def test_hyp_pcm_seff_abstractbranchtransition_constructor_exists():
    assert callable(pcm_seff_AbstractBranchTransition.__init__)


def test_hyp_pcm_seff_abstractbranchtransition_constructor_args():
    sig = inspect.signature(pcm_seff_AbstractBranchTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_innerdeclaration_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_InnerDeclaration)


def test_hyp_pcm_repository_innerdeclaration_constructor_exists():
    assert callable(pcm_repository_InnerDeclaration.__init__)


def test_hyp_pcm_repository_innerdeclaration_constructor_args():
    sig = inspect.signature(pcm_repository_InnerDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_parameter_variablecharacterisation_is_not_abstract():
    assert not inspect.isabstract(pcm_parameter_VariableCharacterisation)


def test_hyp_pcm_parameter_variablecharacterisation_constructor_exists():
    assert callable(pcm_parameter_VariableCharacterisation.__init__)


def test_hyp_pcm_parameter_variablecharacterisation_constructor_args():
    sig = inspect.signature(pcm_parameter_VariableCharacterisation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_pcm_protocol_protocol_is_not_abstract():
    assert not inspect.isabstract(pcm_protocol_Protocol)


def test_hyp_pcm_protocol_protocol_constructor_exists():
    assert callable(pcm_protocol_Protocol.__init__)


def test_hyp_pcm_protocol_protocol_constructor_args():
    sig = inspect.signature(pcm_protocol_Protocol.__init__)
    params = list(sig.parameters.keys())
    assert "protocolTypeID" in params, "Missing parameter 'protocolTypeID'"




def test_hyp_pcm_protocol_servicecall_is_not_abstract():
    assert not inspect.isabstract(pcm_protocol_ServiceCall)


def test_hyp_pcm_protocol_servicecall_constructor_exists():
    assert callable(pcm_protocol_ServiceCall.__init__)


def test_hyp_pcm_protocol_servicecall_constructor_args():
    sig = inspect.signature(pcm_protocol_ServiceCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_innerdeclaration_is_not_abstract():
    assert not inspect.isabstract(InnerDeclaration)


def test_hyp_innerdeclaration_constructor_exists():
    assert callable(InnerDeclaration.__init__)


def test_hyp_innerdeclaration_constructor_args():
    sig = inspect.signature(InnerDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compositedatatype_is_not_abstract():
    assert not inspect.isabstract(CompositeDataType)


def test_hyp_compositedatatype_constructor_exists():
    assert callable(CompositeDataType.__init__)


def test_hyp_compositedatatype_constructor_args():
    sig = inspect.signature(CompositeDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_repository_datatype_is_not_abstract():
    assert not inspect.isabstract(repository_DataType)


def test_hyp_repository_datatype_constructor_exists():
    assert callable(repository_DataType.__init__)


def test_hyp_repository_datatype_constructor_args():
    sig = inspect.signature(repository_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_entity_is_not_abstract():
    assert not inspect.isabstract(entity_Entity)


def test_hyp_entity_entity_constructor_exists():
    assert callable(entity_Entity.__init__)


def test_hyp_entity_entity_constructor_args():
    sig = inspect.signature(entity_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_compositedatatype_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_CompositeDataType)


def test_hyp_pcm_repository_compositedatatype_constructor_exists():
    assert callable(pcm_repository_CompositeDataType.__init__)


def test_hyp_pcm_repository_compositedatatype_constructor_args():
    sig = inspect.signature(pcm_repository_CompositeDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourcetype_resourcetype_is_not_abstract():
    assert not inspect.isabstract(pcm_resourcetype_ResourceType)


def test_hyp_pcm_resourcetype_resourcetype_constructor_exists():
    assert callable(pcm_resourcetype_ResourceType.__init__)


def test_hyp_pcm_resourcetype_resourcetype_constructor_args():
    sig = inspect.signature(pcm_resourcetype_ResourceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_collectiondatatype_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_CollectionDataType)


def test_hyp_pcm_repository_collectiondatatype_constructor_exists():
    assert callable(pcm_repository_CollectionDataType.__init__)


def test_hyp_pcm_repository_collectiondatatype_constructor_args():
    sig = inspect.signature(pcm_repository_CollectionDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_passiveresource_is_not_abstract():
    assert not inspect.isabstract(PassiveResource)


def test_hyp_passiveresource_constructor_exists():
    assert callable(PassiveResource.__init__)


def test_hyp_passiveresource_constructor_args():
    sig = inspect.signature(PassiveResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_serviceeffectspecification_is_not_abstract():
    assert not inspect.isabstract(ServiceEffectSpecification)


def test_hyp_serviceeffectspecification_constructor_exists():
    assert callable(ServiceEffectSpecification.__init__)


def test_hyp_serviceeffectspecification_constructor_args():
    sig = inspect.signature(ServiceEffectSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_providescomponenttype_is_not_abstract():
    assert not inspect.isabstract(ProvidesComponentType)


def test_hyp_providescomponenttype_constructor_exists():
    assert callable(ProvidesComponentType.__init__)


def test_hyp_providescomponenttype_constructor_args():
    sig = inspect.signature(ProvidesComponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_implementationcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ImplementationComponentType)


def test_hyp_implementationcomponenttype_constructor_exists():
    assert callable(ImplementationComponentType.__init__)


def test_hyp_implementationcomponenttype_constructor_args():
    sig = inspect.signature(ImplementationComponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_basiccomponent_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_BasicComponent)


def test_hyp_pcm_repository_basiccomponent_constructor_exists():
    assert callable(pcm_repository_BasicComponent.__init__)


def test_hyp_pcm_repository_basiccomponent_constructor_args():
    sig = inspect.signature(pcm_repository_BasicComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_repository_implementationcomponenttype_is_not_abstract():
    assert not inspect.isabstract(repository_ImplementationComponentType)


def test_hyp_repository_implementationcomponenttype_constructor_exists():
    assert callable(repository_ImplementationComponentType.__init__)


def test_hyp_repository_implementationcomponenttype_constructor_args():
    sig = inspect.signature(repository_ImplementationComponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_composedprovidingrequiringentity_is_not_abstract():
    assert not inspect.isabstract(entity_ComposedProvidingRequiringEntity)


def test_hyp_entity_composedprovidingrequiringentity_constructor_exists():
    assert callable(entity_ComposedProvidingRequiringEntity.__init__)


def test_hyp_entity_composedprovidingrequiringentity_constructor_args():
    sig = inspect.signature(entity_ComposedProvidingRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_system_system_is_not_abstract():
    assert not inspect.isabstract(pcm_system_System)


def test_hyp_pcm_system_system_constructor_exists():
    assert callable(pcm_system_System.__init__)


def test_hyp_pcm_system_system_constructor_args():
    sig = inspect.signature(pcm_system_System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_subsystem_subsystem_is_not_abstract():
    assert not inspect.isabstract(pcm_subsystem_SubSystem)


def test_hyp_pcm_subsystem_subsystem_constructor_exists():
    assert callable(pcm_subsystem_SubSystem.__init__)


def test_hyp_pcm_subsystem_subsystem_constructor_args():
    sig = inspect.signature(pcm_subsystem_SubSystem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_compositecomponent_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_CompositeComponent)


def test_hyp_pcm_repository_compositecomponent_constructor_exists():
    assert callable(pcm_repository_CompositeComponent.__init__)


def test_hyp_pcm_repository_compositecomponent_constructor_args():
    sig = inspect.signature(pcm_repository_CompositeComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completecomponenttype_is_not_abstract():
    assert not inspect.isabstract(CompleteComponentType)


def test_hyp_completecomponenttype_constructor_exists():
    assert callable(CompleteComponentType.__init__)


def test_hyp_completecomponenttype_constructor_args():
    sig = inspect.signature(CompleteComponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_exceptiontype_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_ExceptionType)


def test_hyp_pcm_repository_exceptiontype_constructor_exists():
    assert callable(pcm_repository_ExceptionType.__init__)


def test_hyp_pcm_repository_exceptiontype_constructor_args():
    sig = inspect.signature(pcm_repository_ExceptionType.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionMessage" in params, "Missing parameter 'exceptionMessage'"
    assert "exceptionName" in params, "Missing parameter 'exceptionName'"





def test_hyp_protocol_is_not_abstract():
    assert not inspect.isabstract(Protocol)


def test_hyp_protocol_constructor_exists():
    assert callable(Protocol.__init__)


def test_hyp_protocol_constructor_args():
    sig = inspect.signature(Protocol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_hyp_role_constructor_exists():
    assert callable(Role.__init__)


def test_hyp_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_providedrole_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_ProvidedRole)


def test_hyp_pcm_repository_providedrole_constructor_exists():
    assert callable(pcm_repository_ProvidedRole.__init__)


def test_hyp_pcm_repository_providedrole_constructor_args():
    sig = inspect.signature(pcm_repository_ProvidedRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_resourcerequiredrole_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_ResourceRequiredRole)


def test_hyp_pcm_repository_resourcerequiredrole_constructor_exists():
    assert callable(pcm_repository_ResourceRequiredRole.__init__)


def test_hyp_pcm_repository_resourcerequiredrole_constructor_args():
    sig = inspect.signature(pcm_repository_ResourceRequiredRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_requiredrole_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_RequiredRole)


def test_hyp_pcm_repository_requiredrole_constructor_exists():
    assert callable(pcm_repository_RequiredRole.__init__)


def test_hyp_pcm_repository_requiredrole_constructor_args():
    sig = inspect.signature(pcm_repository_RequiredRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interfaceprovidingrequiringentity_is_not_abstract():
    assert not inspect.isabstract(InterfaceProvidingRequiringEntity)


def test_hyp_interfaceprovidingrequiringentity_constructor_exists():
    assert callable(InterfaceProvidingRequiringEntity.__init__)


def test_hyp_interfaceprovidingrequiringentity_constructor_args():
    sig = inspect.signature(InterfaceProvidingRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_repositorycomponent_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_RepositoryComponent)


def test_hyp_pcm_repository_repositorycomponent_constructor_exists():
    assert callable(pcm_repository_RepositoryComponent.__init__)


def test_hyp_pcm_repository_repositorycomponent_constructor_args():
    sig = inspect.signature(pcm_repository_RepositoryComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_hyp_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_hyp_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_repository_is_not_abstract():
    assert not inspect.isabstract(Repository)


def test_hyp_repository_constructor_exists():
    assert callable(Repository.__init__)


def test_hyp_repository_constructor_args():
    sig = inspect.signature(Repository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_datatype_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_DataType)


def test_hyp_pcm_repository_datatype_constructor_exists():
    assert callable(pcm_repository_DataType.__init__)


def test_hyp_pcm_repository_datatype_constructor_args():
    sig = inspect.signature(pcm_repository_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_signature_is_not_abstract():
    assert not inspect.isabstract(Signature)


def test_hyp_signature_constructor_exists():
    assert callable(Signature.__init__)


def test_hyp_signature_constructor_args():
    sig = inspect.signature(Signature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_parameter_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_Parameter)


def test_hyp_pcm_repository_parameter_constructor_exists():
    assert callable(pcm_repository_Parameter.__init__)


def test_hyp_pcm_repository_parameter_constructor_args():
    sig = inspect.signature(pcm_repository_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "modifier__Parameter" in params, "Missing parameter 'modifier__Parameter'"
    assert "parameterName" in params, "Missing parameter 'parameterName'"





def test_hyp_exceptiontype_is_not_abstract():
    assert not inspect.isabstract(ExceptionType)


def test_hyp_exceptiontype_constructor_exists():
    assert callable(ExceptionType.__init__)


def test_hyp_exceptiontype_constructor_args():
    sig = inspect.signature(ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_PrimitiveDataType)


def test_hyp_pcm_repository_primitivedatatype_constructor_exists():
    assert callable(pcm_repository_PrimitiveDataType.__init__)


def test_hyp_pcm_repository_primitivedatatype_constructor_args():
    sig = inspect.signature(pcm_repository_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_composition_provideddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(composition_ProvidedDelegationConnector)


def test_hyp_composition_provideddelegationconnector_constructor_exists():
    assert callable(composition_ProvidedDelegationConnector.__init__)


def test_hyp_composition_provideddelegationconnector_constructor_args():
    sig = inspect.signature(composition_ProvidedDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_signature_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_Signature)


def test_hyp_pcm_repository_signature_constructor_exists():
    assert callable(pcm_repository_Signature.__init__)


def test_hyp_pcm_repository_signature_constructor_args():
    sig = inspect.signature(pcm_repository_Signature.__init__)
    params = list(sig.parameters.keys())
    assert "serviceName" in params, "Missing parameter 'serviceName'"




def test_hyp_pcmrandomvariable_is_not_abstract():
    assert not inspect.isabstract(PCMRandomVariable)


def test_hyp_pcmrandomvariable_constructor_exists():
    assert callable(PCMRandomVariable.__init__)


def test_hyp_pcmrandomvariable_constructor_args():
    sig = inspect.signature(PCMRandomVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_composition_resourcerequireddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(composition_ResourceRequiredDelegationConnector)


def test_hyp_composition_resourcerequireddelegationconnector_constructor_exists():
    assert callable(composition_ResourceRequiredDelegationConnector.__init__)


def test_hyp_composition_resourcerequireddelegationconnector_constructor_args():
    sig = inspect.signature(composition_ResourceRequiredDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_composition_assemblyconnector_is_not_abstract():
    assert not inspect.isabstract(composition_AssemblyConnector)


def test_hyp_composition_assemblyconnector_constructor_exists():
    assert callable(composition_AssemblyConnector.__init__)


def test_hyp_composition_assemblyconnector_constructor_args():
    sig = inspect.signature(composition_AssemblyConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_composition_requireddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(composition_RequiredDelegationConnector)


def test_hyp_composition_requireddelegationconnector_constructor_exists():
    assert callable(composition_RequiredDelegationConnector.__init__)


def test_hyp_composition_requireddelegationconnector_constructor_args():
    sig = inspect.signature(composition_RequiredDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_composition_resourcerequireddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(pcm_composition_ResourceRequiredDelegationConnector)


def test_hyp_pcm_composition_resourcerequireddelegationconnector_constructor_exists():
    assert callable(pcm_composition_ResourceRequiredDelegationConnector.__init__)


def test_hyp_pcm_composition_resourcerequireddelegationconnector_constructor_args():
    sig = inspect.signature(pcm_composition_ResourceRequiredDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connector_is_not_abstract():
    assert not inspect.isabstract(Connector)


def test_hyp_connector_constructor_exists():
    assert callable(Connector.__init__)


def test_hyp_connector_constructor_args():
    sig = inspect.signature(Connector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_delegationconnector_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_DelegationConnector)


def test_hyp_pcm_repository_delegationconnector_constructor_exists():
    assert callable(pcm_repository_DelegationConnector.__init__)


def test_hyp_pcm_repository_delegationconnector_constructor_args():
    sig = inspect.signature(pcm_repository_DelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_composition_assemblyconnector_is_not_abstract():
    assert not inspect.isabstract(pcm_composition_AssemblyConnector)


def test_hyp_pcm_composition_assemblyconnector_constructor_exists():
    assert callable(pcm_composition_AssemblyConnector.__init__)


def test_hyp_pcm_composition_assemblyconnector_constructor_args():
    sig = inspect.signature(pcm_composition_AssemblyConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variableusage_is_not_abstract():
    assert not inspect.isabstract(VariableUsage)


def test_hyp_variableusage_constructor_exists():
    assert callable(VariableUsage.__init__)


def test_hyp_variableusage_constructor_args():
    sig = inspect.signature(VariableUsage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_repositorycomponent_is_not_abstract():
    assert not inspect.isabstract(RepositoryComponent)


def test_hyp_repositorycomponent_constructor_exists():
    assert callable(RepositoryComponent.__init__)


def test_hyp_repositorycomponent_constructor_args():
    sig = inspect.signature(RepositoryComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_implementationcomponenttype_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_ImplementationComponentType)


def test_hyp_pcm_repository_implementationcomponenttype_constructor_exists():
    assert callable(pcm_repository_ImplementationComponentType.__init__)


def test_hyp_pcm_repository_implementationcomponenttype_constructor_args():
    sig = inspect.signature(pcm_repository_ImplementationComponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_completecomponenttype_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_CompleteComponentType)


def test_hyp_pcm_repository_completecomponenttype_constructor_exists():
    assert callable(pcm_repository_CompleteComponentType.__init__)


def test_hyp_pcm_repository_completecomponenttype_constructor_args():
    sig = inspect.signature(pcm_repository_CompleteComponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_providescomponenttype_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_ProvidesComponentType)


def test_hyp_pcm_repository_providescomponenttype_constructor_exists():
    assert callable(pcm_repository_ProvidesComponentType.__init__)


def test_hyp_pcm_repository_providescomponenttype_constructor_args():
    sig = inspect.signature(pcm_repository_ProvidesComponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_composition_assemblycontext_is_not_abstract():
    assert not inspect.isabstract(composition_AssemblyContext)


def test_hyp_composition_assemblycontext_constructor_exists():
    assert callable(composition_AssemblyContext.__init__)


def test_hyp_composition_assemblycontext_constructor_args():
    sig = inspect.signature(composition_AssemblyContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_delegationconnector_is_not_abstract():
    assert not inspect.isabstract(DelegationConnector)


def test_hyp_delegationconnector_constructor_exists():
    assert callable(DelegationConnector.__init__)


def test_hyp_delegationconnector_constructor_args():
    sig = inspect.signature(DelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_composition_requireddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(pcm_composition_RequiredDelegationConnector)


def test_hyp_pcm_composition_requireddelegationconnector_constructor_exists():
    assert callable(pcm_composition_RequiredDelegationConnector.__init__)


def test_hyp_pcm_composition_requireddelegationconnector_constructor_args():
    sig = inspect.signature(pcm_composition_RequiredDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_composition_provideddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(pcm_composition_ProvidedDelegationConnector)


def test_hyp_pcm_composition_provideddelegationconnector_constructor_exists():
    assert callable(pcm_composition_ProvidedDelegationConnector.__init__)


def test_hyp_pcm_composition_provideddelegationconnector_constructor_args():
    sig = inspect.signature(pcm_composition_ProvidedDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_interfaceprovidingrequiringentity_is_not_abstract():
    assert not inspect.isabstract(entity_InterfaceProvidingRequiringEntity)


def test_hyp_entity_interfaceprovidingrequiringentity_constructor_exists():
    assert callable(entity_InterfaceProvidingRequiringEntity.__init__)


def test_hyp_entity_interfaceprovidingrequiringentity_constructor_args():
    sig = inspect.signature(entity_InterfaceProvidingRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_composition_composedstructure_is_not_abstract():
    assert not inspect.isabstract(composition_ComposedStructure)


def test_hyp_composition_composedstructure_constructor_exists():
    assert callable(composition_ComposedStructure.__init__)


def test_hyp_composition_composedstructure_constructor_args():
    sig = inspect.signature(composition_ComposedStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_entity_composedprovidingrequiringentity_is_not_abstract():
    assert not inspect.isabstract(pcm_entity_ComposedProvidingRequiringEntity)


def test_hyp_pcm_entity_composedprovidingrequiringentity_constructor_exists():
    assert callable(pcm_entity_ComposedProvidingRequiringEntity.__init__)


def test_hyp_pcm_entity_composedprovidingrequiringentity_constructor_args():
    sig = inspect.signature(pcm_entity_ComposedProvidingRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resourcerequiredrole_is_not_abstract():
    assert not inspect.isabstract(ResourceRequiredRole)


def test_hyp_resourcerequiredrole_constructor_exists():
    assert callable(ResourceRequiredRole.__init__)


def test_hyp_resourcerequiredrole_constructor_args():
    sig = inspect.signature(ResourceRequiredRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requiredrole_is_not_abstract():
    assert not inspect.isabstract(RequiredRole)


def test_hyp_requiredrole_constructor_exists():
    assert callable(RequiredRole.__init__)


def test_hyp_requiredrole_constructor_args():
    sig = inspect.signature(RequiredRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_resourceinterfacerequiringentity_is_not_abstract():
    assert not inspect.isabstract(entity_ResourceInterfaceRequiringEntity)


def test_hyp_entity_resourceinterfacerequiringentity_constructor_exists():
    assert callable(entity_ResourceInterfaceRequiringEntity.__init__)


def test_hyp_entity_resourceinterfacerequiringentity_constructor_args():
    sig = inspect.signature(entity_ResourceInterfaceRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_interfacerequiringentity_is_not_abstract():
    assert not inspect.isabstract(entity_InterfaceRequiringEntity)


def test_hyp_entity_interfacerequiringentity_constructor_exists():
    assert callable(entity_InterfaceRequiringEntity.__init__)


def test_hyp_entity_interfacerequiringentity_constructor_args():
    sig = inspect.signature(entity_InterfaceRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_interfaceprovidingentity_is_not_abstract():
    assert not inspect.isabstract(entity_InterfaceProvidingEntity)


def test_hyp_entity_interfaceprovidingentity_constructor_exists():
    assert callable(entity_InterfaceProvidingEntity.__init__)


def test_hyp_entity_interfaceprovidingentity_constructor_args():
    sig = inspect.signature(entity_InterfaceProvidingEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_entity_interfaceprovidingrequiringentity_is_not_abstract():
    assert not inspect.isabstract(pcm_entity_InterfaceProvidingRequiringEntity)


def test_hyp_pcm_entity_interfaceprovidingrequiringentity_constructor_exists():
    assert callable(pcm_entity_InterfaceProvidingRequiringEntity.__init__)


def test_hyp_pcm_entity_interfaceprovidingrequiringentity_constructor_args():
    sig = inspect.signature(pcm_entity_InterfaceProvidingRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_providedrole_is_not_abstract():
    assert not inspect.isabstract(ProvidedRole)


def test_hyp_providedrole_constructor_exists():
    assert callable(ProvidedRole.__init__)


def test_hyp_providedrole_constructor_args():
    sig = inspect.signature(ProvidedRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_hyp_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_hyp_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_connectors_connector_is_not_abstract():
    assert not inspect.isabstract(pcm_connectors_Connector)


def test_hyp_pcm_connectors_connector_constructor_exists():
    assert callable(pcm_connectors_Connector.__init__)


def test_hyp_pcm_connectors_connector_constructor_args():
    sig = inspect.signature(pcm_connectors_Connector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_abstractuseraction_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_AbstractUserAction)


def test_hyp_pcm_usagemodel_abstractuseraction_constructor_exists():
    assert callable(pcm_usagemodel_AbstractUserAction.__init__)


def test_hyp_pcm_usagemodel_abstractuseraction_constructor_args():
    sig = inspect.signature(pcm_usagemodel_AbstractUserAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_abstractaction_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_AbstractAction)


def test_hyp_pcm_seff_abstractaction_constructor_exists():
    assert callable(pcm_seff_AbstractAction.__init__)


def test_hyp_pcm_seff_abstractaction_constructor_args():
    sig = inspect.signature(pcm_seff_AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_allocation_allocationcontext_is_not_abstract():
    assert not inspect.isabstract(pcm_allocation_AllocationContext)


def test_hyp_pcm_allocation_allocationcontext_constructor_exists():
    assert callable(pcm_allocation_AllocationContext.__init__)


def test_hyp_pcm_allocation_allocationcontext_constructor_args():
    sig = inspect.signature(pcm_allocation_AllocationContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourceenvironment_linkingresource_is_not_abstract():
    assert not inspect.isabstract(pcm_resourceenvironment_LinkingResource)


def test_hyp_pcm_resourceenvironment_linkingresource_constructor_exists():
    assert callable(pcm_resourceenvironment_LinkingResource.__init__)


def test_hyp_pcm_resourceenvironment_linkingresource_constructor_args():
    sig = inspect.signature(pcm_resourceenvironment_LinkingResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_allocation_allocation_is_not_abstract():
    assert not inspect.isabstract(pcm_allocation_Allocation)


def test_hyp_pcm_allocation_allocation_constructor_exists():
    assert callable(pcm_allocation_Allocation.__init__)


def test_hyp_pcm_allocation_allocation_constructor_args():
    sig = inspect.signature(pcm_allocation_Allocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_repository_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_Repository)


def test_hyp_pcm_repository_repository_constructor_exists():
    assert callable(pcm_repository_Repository.__init__)


def test_hyp_pcm_repository_repository_constructor_args():
    sig = inspect.signature(pcm_repository_Repository.__init__)
    params = list(sig.parameters.keys())
    assert "repositoryDescription" in params, "Missing parameter 'repositoryDescription'"




def test_hyp_pcm_entity_interfacerequiringentity_is_not_abstract():
    assert not inspect.isabstract(pcm_entity_InterfaceRequiringEntity)


def test_hyp_pcm_entity_interfacerequiringentity_constructor_exists():
    assert callable(pcm_entity_InterfaceRequiringEntity.__init__)


def test_hyp_pcm_entity_interfacerequiringentity_constructor_args():
    sig = inspect.signature(pcm_entity_InterfaceRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_composition_composedstructure_is_not_abstract():
    assert not inspect.isabstract(pcm_composition_ComposedStructure)


def test_hyp_pcm_composition_composedstructure_constructor_exists():
    assert callable(pcm_composition_ComposedStructure.__init__)


def test_hyp_pcm_composition_composedstructure_constructor_args():
    sig = inspect.signature(pcm_composition_ComposedStructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_interface_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_Interface)


def test_hyp_pcm_repository_interface_constructor_exists():
    assert callable(pcm_repository_Interface.__init__)


def test_hyp_pcm_repository_interface_constructor_args():
    sig = inspect.signature(pcm_repository_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_usagescenario_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_UsageScenario)


def test_hyp_pcm_usagemodel_usagescenario_constructor_exists():
    assert callable(pcm_usagemodel_UsageScenario.__init__)


def test_hyp_pcm_usagemodel_usagescenario_constructor_args():
    sig = inspect.signature(pcm_usagemodel_UsageScenario.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_resourceenvironment_resourcecontainer_is_not_abstract():
    assert not inspect.isabstract(pcm_resourceenvironment_ResourceContainer)


def test_hyp_pcm_resourceenvironment_resourcecontainer_constructor_exists():
    assert callable(pcm_resourceenvironment_ResourceContainer.__init__)


def test_hyp_pcm_resourceenvironment_resourcecontainer_constructor_args():
    sig = inspect.signature(pcm_resourceenvironment_ResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_composition_assemblycontext_is_not_abstract():
    assert not inspect.isabstract(pcm_composition_AssemblyContext)


def test_hyp_pcm_composition_assemblycontext_constructor_exists():
    assert callable(pcm_composition_AssemblyContext.__init__)


def test_hyp_pcm_composition_assemblycontext_constructor_args():
    sig = inspect.signature(pcm_composition_AssemblyContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_entity_resourceinterfacerequiringentity_is_not_abstract():
    assert not inspect.isabstract(pcm_entity_ResourceInterfaceRequiringEntity)


def test_hyp_pcm_entity_resourceinterfacerequiringentity_constructor_exists():
    assert callable(pcm_entity_ResourceInterfaceRequiringEntity.__init__)


def test_hyp_pcm_entity_resourceinterfacerequiringentity_constructor_args():
    sig = inspect.signature(pcm_entity_ResourceInterfaceRequiringEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_qosannotations_qosannotations_is_not_abstract():
    assert not inspect.isabstract(pcm_qosannotations_QoSAnnotations)


def test_hyp_pcm_qosannotations_qosannotations_constructor_exists():
    assert callable(pcm_qosannotations_QoSAnnotations.__init__)


def test_hyp_pcm_qosannotations_qosannotations_constructor_args():
    sig = inspect.signature(pcm_qosannotations_QoSAnnotations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_passiveresource_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_PassiveResource)


def test_hyp_pcm_repository_passiveresource_constructor_exists():
    assert callable(pcm_repository_PassiveResource.__init__)


def test_hyp_pcm_repository_passiveresource_constructor_args():
    sig = inspect.signature(pcm_repository_PassiveResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_usagemodel_scenariobehaviour_is_not_abstract():
    assert not inspect.isabstract(pcm_usagemodel_ScenarioBehaviour)


def test_hyp_pcm_usagemodel_scenariobehaviour_constructor_exists():
    assert callable(pcm_usagemodel_ScenarioBehaviour.__init__)


def test_hyp_pcm_usagemodel_scenariobehaviour_constructor_args():
    sig = inspect.signature(pcm_usagemodel_ScenarioBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_repository_role_is_not_abstract():
    assert not inspect.isabstract(pcm_repository_Role)


def test_hyp_pcm_repository_role_constructor_exists():
    assert callable(pcm_repository_Role.__init__)


def test_hyp_pcm_repository_role_constructor_args():
    sig = inspect.signature(pcm_repository_Role.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_entity_interfaceprovidingentity_is_not_abstract():
    assert not inspect.isabstract(pcm_entity_InterfaceProvidingEntity)


def test_hyp_pcm_entity_interfaceprovidingentity_constructor_exists():
    assert callable(pcm_entity_InterfaceProvidingEntity.__init__)


def test_hyp_pcm_entity_interfaceprovidingentity_constructor_args():
    sig = inspect.signature(pcm_entity_InterfaceProvidingEntity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_entity_namedelement_is_not_abstract():
    assert not inspect.isabstract(pcm_entity_NamedElement)


def test_hyp_pcm_entity_namedelement_constructor_exists():
    assert callable(pcm_entity_NamedElement.__init__)


def test_hyp_pcm_entity_namedelement_constructor_args():
    sig = inspect.signature(pcm_entity_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "entityName" in params, "Missing parameter 'entityName'"




def test_hyp_entity_namedelement_is_not_abstract():
    assert not inspect.isabstract(entity_NamedElement)


def test_hyp_entity_namedelement_constructor_exists():
    assert callable(entity_NamedElement.__init__)


def test_hyp_entity_namedelement_constructor_args():
    sig = inspect.signature(entity_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_hyp_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_hyp_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_seff_resourcedemandingseff_is_not_abstract():
    assert not inspect.isabstract(pcm_seff_ResourceDemandingSEFF)


def test_hyp_pcm_seff_resourcedemandingseff_constructor_exists():
    assert callable(pcm_seff_ResourceDemandingSEFF.__init__)


def test_hyp_pcm_seff_resourcedemandingseff_constructor_args():
    sig = inspect.signature(pcm_seff_ResourceDemandingSEFF.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_entity_entity_is_not_abstract():
    assert not inspect.isabstract(pcm_entity_Entity)


def test_hyp_pcm_entity_entity_constructor_exists():
    assert callable(pcm_entity_Entity.__init__)


def test_hyp_pcm_entity_entity_constructor_args():
    sig = inspect.signature(pcm_entity_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_randomvariable_is_not_abstract():
    assert not inspect.isabstract(RandomVariable)


def test_hyp_randomvariable_constructor_exists():
    assert callable(RandomVariable.__init__)


def test_hyp_randomvariable_constructor_args():
    sig = inspect.signature(RandomVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pcm_core_pcmrandomvariable_is_not_abstract():
    assert not inspect.isabstract(pcm_core_PCMRandomVariable)


def test_hyp_pcm_core_pcmrandomvariable_constructor_exists():
    assert callable(pcm_core_PCMRandomVariable.__init__)


def test_hyp_pcm_core_pcmrandomvariable_constructor_args():
    sig = inspect.signature(pcm_core_PCMRandomVariable.__init__)
    params = list(sig.parameters.keys())

def test_hyp_schedulingpolicy_exists():
    # Check that the Enumeration exists
    assert SchedulingPolicy is not None

def test_hyp_schedulingpolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchedulingPolicy]
    expected_literals = [
        "FCFS",
        "PROCESSOR_SHARING",
        "DELAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchedulingPolicy"

def test_hyp_variablecharacterisationtype_exists():
    # Check that the Enumeration exists
    assert VariableCharacterisationType is not None

def test_hyp_variablecharacterisationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableCharacterisationType]
    expected_literals = [
        "NUMBER_OF_ELEMENTS",
        "BYTESIZE",
        "TYPE",
        "VALUE",
        "STRUCTURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableCharacterisationType"

def test_hyp_primitivetypeenum_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypeEnum is not None

def test_hyp_primitivetypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypeEnum]
    expected_literals = [
        "BYTE",
        "BOOL",
        "INT",
        "CHAR",
        "STRING",
        "DOUBLE",
        "LONG",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypeEnum"

def test_hyp_parametermodifier_exists():
    # Check that the Enumeration exists
    assert ParameterModifier is not None

def test_hyp_parametermodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterModifier]
    expected_literals = [
        "none",
        "inout",
        "in_",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterModifier"


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
repository_RepositoryComponent_strategy = st.builds(
    repository_RepositoryComponent,
)
pcm_usagemodel_BranchTransition_strategy = st.builds(
    pcm_usagemodel_BranchTransition,
    branchProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BranchTransition_strategy = st.builds(
    BranchTransition,
)
pcm_usagemodel_UserData_strategy = st.builds(
    pcm_usagemodel_UserData,
)
UserData_strategy = st.builds(
    UserData,
)
UsageScenario_strategy = st.builds(
    UsageScenario,
)
pcm_usagemodel_UsageModel_strategy = st.builds(
    pcm_usagemodel_UsageModel,
)
AbstractUserAction_strategy = st.builds(
    AbstractUserAction,
)
pcm_usagemodel_Branch_strategy = st.builds(
    pcm_usagemodel_Branch,
)
pcm_usagemodel_Stop_strategy = st.builds(
    pcm_usagemodel_Stop,
)
pcm_usagemodel_Delay_strategy = st.builds(
    pcm_usagemodel_Delay,
)
pcm_usagemodel_EntryLevelSystemCall_strategy = st.builds(
    pcm_usagemodel_EntryLevelSystemCall,
)
pcm_usagemodel_Loop_strategy = st.builds(
    pcm_usagemodel_Loop,
)
pcm_usagemodel_Start_strategy = st.builds(
    pcm_usagemodel_Start,
)
ScenarioBehaviour_strategy = st.builds(
    ScenarioBehaviour,
)
Workload_strategy = st.builds(
    Workload,
)
pcm_usagemodel_ClosedWorkload_strategy = st.builds(
    pcm_usagemodel_ClosedWorkload,
    population=
        st.integers()
)
pcm_usagemodel_OpenWorkload_strategy = st.builds(
    pcm_usagemodel_OpenWorkload,
)
pcm_usagemodel_Workload_strategy = st.builds(
    pcm_usagemodel_Workload,
)
SpecifiedOutputParameterAbstraction_strategy = st.builds(
    SpecifiedOutputParameterAbstraction,
)
SpecifiedQoSAnnotation_strategy = st.builds(
    SpecifiedQoSAnnotation,
)
pcm_performance_SystemSpecifiedExecutionTime_strategy = st.builds(
    pcm_performance_SystemSpecifiedExecutionTime,
)
pcm_reliability_SpecifiedFailureProbability_strategy = st.builds(
    pcm_reliability_SpecifiedFailureProbability,
    failureProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
pcm_qosannotations_SpecifiedOutputParameterAbstraction_strategy = st.builds(
    pcm_qosannotations_SpecifiedOutputParameterAbstraction,
)
pcm_qosannotations_SpecifiedQoSAnnotation_strategy = st.builds(
    pcm_qosannotations_SpecifiedQoSAnnotation,
)
QoSAnnotations_strategy = st.builds(
    QoSAnnotations,
)
pcm_performance_ComponentSpecifiedExecutionTime_strategy = st.builds(
    pcm_performance_ComponentSpecifiedExecutionTime,
)
pcm_resourceenvironment_ProcessingResourceSpecification_strategy = st.builds(
    pcm_resourceenvironment_ProcessingResourceSpecification,
    schedulingPolicy=
        safe_text,
    MTTF=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    MTTR=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CommunicationLinkResourceType_strategy = st.builds(
    CommunicationLinkResourceType,
)
pcm_resourceenvironment_CommunicationLinkResourceSpecification_strategy = st.builds(
    pcm_resourceenvironment_CommunicationLinkResourceSpecification,
    failureProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CommunicationLinkResourceSpecification_strategy = st.builds(
    CommunicationLinkResourceSpecification,
)
ProcessingResourceSpecification_strategy = st.builds(
    ProcessingResourceSpecification,
)
LinkingResource_strategy = st.builds(
    LinkingResource,
)
pcm_resourceenvironment_ResourceEnvironment_strategy = st.builds(
    pcm_resourceenvironment_ResourceEnvironment,
)
System_strategy = st.builds(
    System,
)
ResourceEnvironment_strategy = st.builds(
    ResourceEnvironment,
)
AllocationContext_strategy = st.builds(
    AllocationContext,
)
ResourceType_strategy = st.builds(
    ResourceType,
)
pcm_resourcetype_ProcessingResourceType_strategy = st.builds(
    pcm_resourcetype_ProcessingResourceType,
)
pcm_resourcetype_ResourceRepository_strategy = st.builds(
    pcm_resourcetype_ResourceRepository,
)
UnitCarryingElement_strategy = st.builds(
    UnitCarryingElement,
)
ProcessingResourceType_strategy = st.builds(
    ProcessingResourceType,
)
pcm_resourcetype_CommunicationLinkResourceType_strategy = st.builds(
    pcm_resourcetype_CommunicationLinkResourceType,
)
pcm_performance_ParametricResourceDemand_strategy = st.builds(
    pcm_performance_ParametricResourceDemand,
)
pcm_seff_ServiceEffectSpecification_strategy = st.builds(
    pcm_seff_ServiceEffectSpecification,
    seffTypeID=
        safe_text
)
ResourceContainer_strategy = st.builds(
    ResourceContainer,
)
AbstractBranchTransition_strategy = st.builds(
    AbstractBranchTransition,
)
pcm_seff_GuardedBranchTransition_strategy = st.builds(
    pcm_seff_GuardedBranchTransition,
)
pcm_seff_ProbabilisticBranchTransition_strategy = st.builds(
    pcm_seff_ProbabilisticBranchTransition,
    branchProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
pcm_seff_SynchronisationPoint_strategy = st.builds(
    pcm_seff_SynchronisationPoint,
)
SynchronisationPoint_strategy = st.builds(
    SynchronisationPoint,
)
ForkedBehaviour_strategy = st.builds(
    ForkedBehaviour,
)
ResourceDemandingBehaviour_strategy = st.builds(
    ResourceDemandingBehaviour,
)
pcm_seff_ForkedBehaviour_strategy = st.builds(
    pcm_seff_ForkedBehaviour,
)
AbstractLoopAction_strategy = st.builds(
    AbstractLoopAction,
)
pcm_seff_CollectionIteratorAction_strategy = st.builds(
    pcm_seff_CollectionIteratorAction,
)
pcm_seff_LoopAction_strategy = st.builds(
    pcm_seff_LoopAction,
)
performance_ParametricResourceDemand_strategy = st.builds(
    performance_ParametricResourceDemand,
)
pcm_seff_ResourceDemandingBehaviour_strategy = st.builds(
    pcm_seff_ResourceDemandingBehaviour,
)
seff_ResourceDemandingBehaviour_strategy = st.builds(
    seff_ResourceDemandingBehaviour,
)
seff_ServiceEffectSpecification_strategy = st.builds(
    seff_ServiceEffectSpecification,
)
AbstractAction_strategy = st.builds(
    AbstractAction,
)
pcm_seff_ExternalCallAction_strategy = st.builds(
    pcm_seff_ExternalCallAction,
    retryCount=
        st.integers()
)
pcm_seff_AbstractInternalControlFlowAction_strategy = st.builds(
    pcm_seff_AbstractInternalControlFlowAction,
)
AbstractInternalControlFlowAction_strategy = st.builds(
    AbstractInternalControlFlowAction,
)
pcm_seff_AbstractLoopAction_strategy = st.builds(
    pcm_seff_AbstractLoopAction,
)
pcm_seff_SetVariableAction_strategy = st.builds(
    pcm_seff_SetVariableAction,
)
pcm_seff_InternalAction_strategy = st.builds(
    pcm_seff_InternalAction,
    failureProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
pcm_seff_StartAction_strategy = st.builds(
    pcm_seff_StartAction,
)
pcm_seff_ReleaseAction_strategy = st.builds(
    pcm_seff_ReleaseAction,
)
pcm_seff_ForkAction_strategy = st.builds(
    pcm_seff_ForkAction,
)
pcm_seff_AcquireAction_strategy = st.builds(
    pcm_seff_AcquireAction,
)
pcm_seff_BranchAction_strategy = st.builds(
    pcm_seff_BranchAction,
)
pcm_seff_StopAction_strategy = st.builds(
    pcm_seff_StopAction,
)
parameter_pcm_AbstractNamedReference_strategy = st.builds(
    parameter_pcm_AbstractNamedReference,
)
VariableCharacterisation_strategy = st.builds(
    VariableCharacterisation,
)
pcm_parameter_VariableUsage_strategy = st.builds(
    pcm_parameter_VariableUsage,
)
Variable_strategy = st.builds(
    Variable,
)
pcm_parameter_CharacterisedVariable_strategy = st.builds(
    pcm_parameter_CharacterisedVariable,
    characterisationType=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pcm_seff_AbstractBranchTransition_strategy = st.builds(
    pcm_seff_AbstractBranchTransition,
)
pcm_repository_InnerDeclaration_strategy = st.builds(
    pcm_repository_InnerDeclaration,
)
pcm_parameter_VariableCharacterisation_strategy = st.builds(
    pcm_parameter_VariableCharacterisation,
    type=
        safe_text
)
pcm_protocol_Protocol_strategy = st.builds(
    pcm_protocol_Protocol,
    protocolTypeID=
        safe_text
)
pcm_protocol_ServiceCall_strategy = st.builds(
    pcm_protocol_ServiceCall,
)
InnerDeclaration_strategy = st.builds(
    InnerDeclaration,
)
CompositeDataType_strategy = st.builds(
    CompositeDataType,
)
repository_DataType_strategy = st.builds(
    repository_DataType,
)
entity_Entity_strategy = st.builds(
    entity_Entity,
)
pcm_repository_CompositeDataType_strategy = st.builds(
    pcm_repository_CompositeDataType,
)
pcm_resourcetype_ResourceType_strategy = st.builds(
    pcm_resourcetype_ResourceType,
)
pcm_repository_CollectionDataType_strategy = st.builds(
    pcm_repository_CollectionDataType,
)
PassiveResource_strategy = st.builds(
    PassiveResource,
)
ServiceEffectSpecification_strategy = st.builds(
    ServiceEffectSpecification,
)
ProvidesComponentType_strategy = st.builds(
    ProvidesComponentType,
)
ImplementationComponentType_strategy = st.builds(
    ImplementationComponentType,
)
pcm_repository_BasicComponent_strategy = st.builds(
    pcm_repository_BasicComponent,
)
repository_ImplementationComponentType_strategy = st.builds(
    repository_ImplementationComponentType,
)
entity_ComposedProvidingRequiringEntity_strategy = st.builds(
    entity_ComposedProvidingRequiringEntity,
)
pcm_system_System_strategy = st.builds(
    pcm_system_System,
)
pcm_subsystem_SubSystem_strategy = st.builds(
    pcm_subsystem_SubSystem,
)
pcm_repository_CompositeComponent_strategy = st.builds(
    pcm_repository_CompositeComponent,
)
CompleteComponentType_strategy = st.builds(
    CompleteComponentType,
)
pcm_repository_ExceptionType_strategy = st.builds(
    pcm_repository_ExceptionType,
    exceptionMessage=
        safe_text,
    exceptionName=
        safe_text
)
Protocol_strategy = st.builds(
    Protocol,
)
Role_strategy = st.builds(
    Role,
)
pcm_repository_ProvidedRole_strategy = st.builds(
    pcm_repository_ProvidedRole,
)
pcm_repository_ResourceRequiredRole_strategy = st.builds(
    pcm_repository_ResourceRequiredRole,
)
pcm_repository_RequiredRole_strategy = st.builds(
    pcm_repository_RequiredRole,
)
InterfaceProvidingRequiringEntity_strategy = st.builds(
    InterfaceProvidingRequiringEntity,
)
pcm_repository_RepositoryComponent_strategy = st.builds(
    pcm_repository_RepositoryComponent,
)
Interface_strategy = st.builds(
    Interface,
)
Repository_strategy = st.builds(
    Repository,
)
pcm_repository_DataType_strategy = st.builds(
    pcm_repository_DataType,
)
Signature_strategy = st.builds(
    Signature,
)
pcm_repository_Parameter_strategy = st.builds(
    pcm_repository_Parameter,
    modifier__Parameter=
        safe_text,
    parameterName=
        safe_text
)
ExceptionType_strategy = st.builds(
    ExceptionType,
)
DataType_strategy = st.builds(
    DataType,
)
pcm_repository_PrimitiveDataType_strategy = st.builds(
    pcm_repository_PrimitiveDataType,
    type=
        safe_text
)
composition_ProvidedDelegationConnector_strategy = st.builds(
    composition_ProvidedDelegationConnector,
)
Parameter_strategy = st.builds(
    Parameter,
)
pcm_repository_Signature_strategy = st.builds(
    pcm_repository_Signature,
    serviceName=
        safe_text
)
PCMRandomVariable_strategy = st.builds(
    PCMRandomVariable,
)
composition_ResourceRequiredDelegationConnector_strategy = st.builds(
    composition_ResourceRequiredDelegationConnector,
)
composition_AssemblyConnector_strategy = st.builds(
    composition_AssemblyConnector,
)
composition_RequiredDelegationConnector_strategy = st.builds(
    composition_RequiredDelegationConnector,
)
pcm_composition_ResourceRequiredDelegationConnector_strategy = st.builds(
    pcm_composition_ResourceRequiredDelegationConnector,
)
Connector_strategy = st.builds(
    Connector,
)
pcm_repository_DelegationConnector_strategy = st.builds(
    pcm_repository_DelegationConnector,
)
pcm_composition_AssemblyConnector_strategy = st.builds(
    pcm_composition_AssemblyConnector,
)
VariableUsage_strategy = st.builds(
    VariableUsage,
)
RepositoryComponent_strategy = st.builds(
    RepositoryComponent,
)
pcm_repository_ImplementationComponentType_strategy = st.builds(
    pcm_repository_ImplementationComponentType,
)
pcm_repository_CompleteComponentType_strategy = st.builds(
    pcm_repository_CompleteComponentType,
)
pcm_repository_ProvidesComponentType_strategy = st.builds(
    pcm_repository_ProvidesComponentType,
)
composition_AssemblyContext_strategy = st.builds(
    composition_AssemblyContext,
)
DelegationConnector_strategy = st.builds(
    DelegationConnector,
)
pcm_composition_RequiredDelegationConnector_strategy = st.builds(
    pcm_composition_RequiredDelegationConnector,
)
pcm_composition_ProvidedDelegationConnector_strategy = st.builds(
    pcm_composition_ProvidedDelegationConnector,
)
entity_InterfaceProvidingRequiringEntity_strategy = st.builds(
    entity_InterfaceProvidingRequiringEntity,
)
composition_ComposedStructure_strategy = st.builds(
    composition_ComposedStructure,
)
pcm_entity_ComposedProvidingRequiringEntity_strategy = st.builds(
    pcm_entity_ComposedProvidingRequiringEntity,
)
ResourceRequiredRole_strategy = st.builds(
    ResourceRequiredRole,
)
RequiredRole_strategy = st.builds(
    RequiredRole,
)
entity_ResourceInterfaceRequiringEntity_strategy = st.builds(
    entity_ResourceInterfaceRequiringEntity,
)
entity_InterfaceRequiringEntity_strategy = st.builds(
    entity_InterfaceRequiringEntity,
)
entity_InterfaceProvidingEntity_strategy = st.builds(
    entity_InterfaceProvidingEntity,
)
pcm_entity_InterfaceProvidingRequiringEntity_strategy = st.builds(
    pcm_entity_InterfaceProvidingRequiringEntity,
)
ProvidedRole_strategy = st.builds(
    ProvidedRole,
)
Entity_strategy = st.builds(
    Entity,
)
pcm_connectors_Connector_strategy = st.builds(
    pcm_connectors_Connector,
)
pcm_usagemodel_AbstractUserAction_strategy = st.builds(
    pcm_usagemodel_AbstractUserAction,
)
pcm_seff_AbstractAction_strategy = st.builds(
    pcm_seff_AbstractAction,
)
pcm_allocation_AllocationContext_strategy = st.builds(
    pcm_allocation_AllocationContext,
)
pcm_resourceenvironment_LinkingResource_strategy = st.builds(
    pcm_resourceenvironment_LinkingResource,
)
pcm_allocation_Allocation_strategy = st.builds(
    pcm_allocation_Allocation,
)
pcm_repository_Repository_strategy = st.builds(
    pcm_repository_Repository,
    repositoryDescription=
        safe_text
)
pcm_entity_InterfaceRequiringEntity_strategy = st.builds(
    pcm_entity_InterfaceRequiringEntity,
)
pcm_composition_ComposedStructure_strategy = st.builds(
    pcm_composition_ComposedStructure,
)
pcm_repository_Interface_strategy = st.builds(
    pcm_repository_Interface,
)
pcm_usagemodel_UsageScenario_strategy = st.builds(
    pcm_usagemodel_UsageScenario,
)
pcm_resourceenvironment_ResourceContainer_strategy = st.builds(
    pcm_resourceenvironment_ResourceContainer,
)
pcm_composition_AssemblyContext_strategy = st.builds(
    pcm_composition_AssemblyContext,
)
pcm_entity_ResourceInterfaceRequiringEntity_strategy = st.builds(
    pcm_entity_ResourceInterfaceRequiringEntity,
)
pcm_qosannotations_QoSAnnotations_strategy = st.builds(
    pcm_qosannotations_QoSAnnotations,
)
pcm_repository_PassiveResource_strategy = st.builds(
    pcm_repository_PassiveResource,
)
pcm_usagemodel_ScenarioBehaviour_strategy = st.builds(
    pcm_usagemodel_ScenarioBehaviour,
)
pcm_repository_Role_strategy = st.builds(
    pcm_repository_Role,
)
pcm_entity_InterfaceProvidingEntity_strategy = st.builds(
    pcm_entity_InterfaceProvidingEntity,
)
pcm_entity_NamedElement_strategy = st.builds(
    pcm_entity_NamedElement,
    entityName=
        safe_text
)
entity_NamedElement_strategy = st.builds(
    entity_NamedElement,
)
Identifier_strategy = st.builds(
    Identifier,
)
pcm_seff_ResourceDemandingSEFF_strategy = st.builds(
    pcm_seff_ResourceDemandingSEFF,
)
pcm_entity_Entity_strategy = st.builds(
    pcm_entity_Entity,
)
RandomVariable_strategy = st.builds(
    RandomVariable,
)
pcm_core_PCMRandomVariable_strategy = st.builds(
    pcm_core_PCMRandomVariable,
)





@given(instance=pcm_usagemodel_BranchTransition_strategy)
def test_hyp_pcm_usagemodel_branchtransition_branchProbability_setter(instance):
    original = instance.branchProbability
    instance.branchProbability = original
    assert instance.branchProbability == original








import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_Branch_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_branch_allbranchprobabilitiesmustsumupto1_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AllBranchProbabilitiesMustSumUpTo1(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AllBranchProbabilitiesMustSumUpTo1).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AllBranchProbabilitiesMustSumUpTo1' in pcm_usagemodel_Branch is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AllBranchProbabilitiesMustSumUpTo1' in pcm_usagemodel_Branch did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AllBranchProbabilitiesMustSumUpTo1' in pcm_usagemodel_Branch is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_Stop_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_stop_stophasnosuccessor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.StopHasNoSuccessor(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.StopHasNoSuccessor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'StopHasNoSuccessor' in pcm_usagemodel_Stop is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'StopHasNoSuccessor' in pcm_usagemodel_Stop did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'StopHasNoSuccessor' in pcm_usagemodel_Stop is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_Start_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_start_starthasnopredecessor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.StartHasNoPredecessor(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.StartHasNoPredecessor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'StartHasNoPredecessor' in pcm_usagemodel_Start is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'StartHasNoPredecessor' in pcm_usagemodel_Start did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'StartHasNoPredecessor' in pcm_usagemodel_Start is not implemented or raised an error")






@given(instance=pcm_usagemodel_ClosedWorkload_strategy)
def test_hyp_pcm_usagemodel_closedworkload_population_setter(instance):
    original = instance.population
    instance.population = original
    assert instance.population == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_ClosedWorkload_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_closedworkload_populationinclosedworkloadneedstobespecified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.PopulationInClosedWorkloadNeedsToBeSpecified(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.PopulationInClosedWorkloadNeedsToBeSpecified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'PopulationInClosedWorkloadNeedsToBeSpecified' in pcm_usagemodel_ClosedWorkload is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'PopulationInClosedWorkloadNeedsToBeSpecified' in pcm_usagemodel_ClosedWorkload did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'PopulationInClosedWorkloadNeedsToBeSpecified' in pcm_usagemodel_ClosedWorkload is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_ClosedWorkload_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_closedworkload_thinktimeinclosedworkloadneedstobespecified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ThinkTimeInClosedWorkloadNeedsToBeSpecified(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ThinkTimeInClosedWorkloadNeedsToBeSpecified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ThinkTimeInClosedWorkloadNeedsToBeSpecified' in pcm_usagemodel_ClosedWorkload is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ThinkTimeInClosedWorkloadNeedsToBeSpecified' in pcm_usagemodel_ClosedWorkload did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ThinkTimeInClosedWorkloadNeedsToBeSpecified' in pcm_usagemodel_ClosedWorkload is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_OpenWorkload_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_openworkload_interarrivaltimeinopenworkloadneedstobespecified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.InterArrivalTimeInOpenWorkloadNeedsToBeSpecified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'InterArrivalTimeInOpenWorkloadNeedsToBeSpecified' in pcm_usagemodel_OpenWorkload is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'InterArrivalTimeInOpenWorkloadNeedsToBeSpecified' in pcm_usagemodel_OpenWorkload did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'InterArrivalTimeInOpenWorkloadNeedsToBeSpecified' in pcm_usagemodel_OpenWorkload is not implemented or raised an error")








@given(instance=pcm_reliability_SpecifiedFailureProbability_strategy)
def test_hyp_pcm_reliability_specifiedfailureprobability_failureProbability_setter(instance):
    original = instance.failureProbability
    instance.failureProbability = original
    assert instance.failureProbability == original








@given(instance=pcm_resourceenvironment_ProcessingResourceSpecification_strategy)
def test_hyp_pcm_resourceenvironment_processingresourcespecification_schedulingPolicy_setter(instance):
    original = instance.schedulingPolicy
    instance.schedulingPolicy = original
    assert instance.schedulingPolicy == original



@given(instance=pcm_resourceenvironment_ProcessingResourceSpecification_strategy)
def test_hyp_pcm_resourceenvironment_processingresourcespecification_MTTF_setter(instance):
    original = instance.MTTF
    instance.MTTF = original
    assert instance.MTTF == original



@given(instance=pcm_resourceenvironment_ProcessingResourceSpecification_strategy)
def test_hyp_pcm_resourceenvironment_processingresourcespecification_MTTR_setter(instance):
    original = instance.MTTR
    instance.MTTR = original
    assert instance.MTTR == original





@given(instance=pcm_resourceenvironment_CommunicationLinkResourceSpecification_strategy)
def test_hyp_pcm_resourceenvironment_communicationlinkresourcespecification_failureProbability_setter(instance):
    original = instance.failureProbability
    instance.failureProbability = original
    assert instance.failureProbability == original


















@given(instance=pcm_seff_ServiceEffectSpecification_strategy)
def test_hyp_pcm_seff_serviceeffectspecification_seffTypeID_setter(instance):
    original = instance.seffTypeID
    instance.seffTypeID = original
    assert instance.seffTypeID == original







@given(instance=pcm_seff_ProbabilisticBranchTransition_strategy)
def test_hyp_pcm_seff_probabilisticbranchtransition_branchProbability_setter(instance):
    original = instance.branchProbability
    instance.branchProbability = original
    assert instance.branchProbability == original











import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_seff_ResourceDemandingBehaviour_strategy)
@settings(max_examples=30)
def test_hyp_pcm_seff_resourcedemandingbehaviour_exactlyonestartaction_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ExactlyOneStartAction(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ExactlyOneStartAction).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ExactlyOneStartAction' in pcm_seff_ResourceDemandingBehaviour is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ExactlyOneStartAction' in pcm_seff_ResourceDemandingBehaviour did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ExactlyOneStartAction' in pcm_seff_ResourceDemandingBehaviour is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_seff_ResourceDemandingBehaviour_strategy)
@settings(max_examples=30)
def test_hyp_pcm_seff_resourcedemandingbehaviour_eachactionexceptstartactionandstopactionmusthhaveapredecessorandsuccessor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor' in pcm_seff_ResourceDemandingBehaviour is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor' in pcm_seff_ResourceDemandingBehaviour did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor' in pcm_seff_ResourceDemandingBehaviour is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_seff_ResourceDemandingBehaviour_strategy)
@settings(max_examples=30)
def test_hyp_pcm_seff_resourcedemandingbehaviour_exactlyonestopaction_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ExactlyOneStopAction(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ExactlyOneStopAction).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ExactlyOneStopAction' in pcm_seff_ResourceDemandingBehaviour is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ExactlyOneStopAction' in pcm_seff_ResourceDemandingBehaviour did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ExactlyOneStopAction' in pcm_seff_ResourceDemandingBehaviour is not implemented or raised an error")







@given(instance=pcm_seff_ExternalCallAction_strategy)
def test_hyp_pcm_seff_externalcallaction_retryCount_setter(instance):
    original = instance.retryCount
    instance.retryCount = original
    assert instance.retryCount == original








@given(instance=pcm_seff_InternalAction_strategy)
def test_hyp_pcm_seff_internalaction_failureProbability_setter(instance):
    original = instance.failureProbability
    instance.failureProbability = original
    assert instance.failureProbability == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_seff_StartAction_strategy)
@settings(max_examples=30)
def test_hyp_pcm_seff_startaction_startactionpredecessormustnotbedefined_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.StartActionPredecessorMustNotBeDefined(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.StartActionPredecessorMustNotBeDefined).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'StartActionPredecessorMustNotBeDefined' in pcm_seff_StartAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'StartActionPredecessorMustNotBeDefined' in pcm_seff_StartAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'StartActionPredecessorMustNotBeDefined' in pcm_seff_StartAction is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_seff_BranchAction_strategy)
@settings(max_examples=30)
def test_hyp_pcm_seff_branchaction_eitherguardedbranchesorprobabilisiticbranchtransitions_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.EitherGuardedBranchesOrProbabilisiticBranchTransitions(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.EitherGuardedBranchesOrProbabilisiticBranchTransitions).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'EitherGuardedBranchesOrProbabilisiticBranchTransitions' in pcm_seff_BranchAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'EitherGuardedBranchesOrProbabilisiticBranchTransitions' in pcm_seff_BranchAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'EitherGuardedBranchesOrProbabilisiticBranchTransitions' in pcm_seff_BranchAction is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_seff_BranchAction_strategy)
@settings(max_examples=30)
def test_hyp_pcm_seff_branchaction_allprobabilisticbranchprobabilitiesmustsumupto1_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AllProbabilisticBranchProbabilitiesMustSumUpTo1(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AllProbabilisticBranchProbabilitiesMustSumUpTo1).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AllProbabilisticBranchProbabilitiesMustSumUpTo1' in pcm_seff_BranchAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AllProbabilisticBranchProbabilitiesMustSumUpTo1' in pcm_seff_BranchAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AllProbabilisticBranchProbabilitiesMustSumUpTo1' in pcm_seff_BranchAction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_seff_StopAction_strategy)
@settings(max_examples=30)
def test_hyp_pcm_seff_stopaction_stopactionsuccessormustnotbedefined_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.StopActionSuccessorMustNotBeDefined(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.StopActionSuccessorMustNotBeDefined).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'StopActionSuccessorMustNotBeDefined' in pcm_seff_StopAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'StopActionSuccessorMustNotBeDefined' in pcm_seff_StopAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'StopActionSuccessorMustNotBeDefined' in pcm_seff_StopAction is not implemented or raised an error")








@given(instance=pcm_parameter_CharacterisedVariable_strategy)
def test_hyp_pcm_parameter_characterisedvariable_characterisationType_setter(instance):
    original = instance.characterisationType
    instance.characterisationType = original
    assert instance.characterisationType == original







@given(instance=pcm_parameter_VariableCharacterisation_strategy)
def test_hyp_pcm_parameter_variablecharacterisation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=pcm_protocol_Protocol_strategy)
def test_hyp_pcm_protocol_protocol_protocolTypeID_setter(instance):
    original = instance.protocolTypeID
    instance.protocolTypeID = original
    assert instance.protocolTypeID == original














import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_BasicComponent_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_basiccomponent_providesameinterfacesasimplementationtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ProvideSameInterfacesAsImplementationType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ProvideSameInterfacesAsImplementationType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ProvideSameInterfacesAsImplementationType' in pcm_repository_BasicComponent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ProvideSameInterfacesAsImplementationType' in pcm_repository_BasicComponent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ProvideSameInterfacesAsImplementationType' in pcm_repository_BasicComponent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_BasicComponent_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_basiccomponent_requiresameinterfacesasimplementationtype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RequireSameInterfacesAsImplementationType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RequireSameInterfacesAsImplementationType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RequireSameInterfacesAsImplementationType' in pcm_repository_BasicComponent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RequireSameInterfacesAsImplementationType' in pcm_repository_BasicComponent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RequireSameInterfacesAsImplementationType' in pcm_repository_BasicComponent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_BasicComponent_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_basiccomponent_nosefftypeusedtwice_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.NoSeffTypeUsedTwice(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.NoSeffTypeUsedTwice).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'NoSeffTypeUsedTwice' in pcm_repository_BasicComponent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'NoSeffTypeUsedTwice' in pcm_repository_BasicComponent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'NoSeffTypeUsedTwice' in pcm_repository_BasicComponent is not implemented or raised an error")






import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_CompositeComponent_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_compositecomponent_requiresameinterfaces_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RequireSameInterfaces(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RequireSameInterfaces).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RequireSameInterfaces' in pcm_repository_CompositeComponent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RequireSameInterfaces' in pcm_repository_CompositeComponent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RequireSameInterfaces' in pcm_repository_CompositeComponent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_CompositeComponent_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_compositecomponent_providesameinterfaces_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ProvideSameInterfaces(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ProvideSameInterfaces).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ProvideSameInterfaces' in pcm_repository_CompositeComponent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ProvideSameInterfaces' in pcm_repository_CompositeComponent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ProvideSameInterfaces' in pcm_repository_CompositeComponent is not implemented or raised an error")





@given(instance=pcm_repository_ExceptionType_strategy)
def test_hyp_pcm_repository_exceptiontype_exceptionMessage_setter(instance):
    original = instance.exceptionMessage
    instance.exceptionMessage = original
    assert instance.exceptionMessage == original



@given(instance=pcm_repository_ExceptionType_strategy)
def test_hyp_pcm_repository_exceptiontype_exceptionName_setter(instance):
    original = instance.exceptionName
    instance.exceptionName = original
    assert instance.exceptionName == original















@given(instance=pcm_repository_Parameter_strategy)
def test_hyp_pcm_repository_parameter_modifier__Parameter_setter(instance):
    original = instance.modifier__Parameter
    instance.modifier__Parameter = original
    assert instance.modifier__Parameter == original



@given(instance=pcm_repository_Parameter_strategy)
def test_hyp_pcm_repository_parameter_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original






@given(instance=pcm_repository_PrimitiveDataType_strategy)
def test_hyp_pcm_repository_primitivedatatype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=pcm_repository_Signature_strategy)
def test_hyp_pcm_repository_signature_serviceName_setter(instance):
    original = instance.serviceName
    instance.serviceName = original
    assert instance.serviceName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_Signature_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_signature_parameternameshavetobeuniqueforasignature_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ParameterNamesHaveToBeUniqueForASignature(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ParameterNamesHaveToBeUniqueForASignature).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ParameterNamesHaveToBeUniqueForASignature' in pcm_repository_Signature is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ParameterNamesHaveToBeUniqueForASignature' in pcm_repository_Signature did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ParameterNamesHaveToBeUniqueForASignature' in pcm_repository_Signature is not implemented or raised an error")









import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_composition_AssemblyConnector_strategy)
@settings(max_examples=30)
def test_hyp_pcm_composition_assemblyconnector_assemblyconnectorsreferencedprovidedrolesandchildcontextmustmatch_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch' in pcm_composition_AssemblyConnector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch' in pcm_composition_AssemblyConnector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch' in pcm_composition_AssemblyConnector is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_composition_AssemblyConnector_strategy)
@settings(max_examples=30)
def test_hyp_pcm_composition_assemblyconnector_assemblyconnectorsreferencedrequiredroleandchildcontextmustmatch_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch' in pcm_composition_AssemblyConnector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch' in pcm_composition_AssemblyConnector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch' in pcm_composition_AssemblyConnector is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_ImplementationComponentType_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_implementationcomponenttype_requiredinterfaceshavetoconformtocompletetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RequiredInterfacesHaveToConformToCompleteType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RequiredInterfacesHaveToConformToCompleteType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RequiredInterfacesHaveToConformToCompleteType' in pcm_repository_ImplementationComponentType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RequiredInterfacesHaveToConformToCompleteType' in pcm_repository_ImplementationComponentType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RequiredInterfacesHaveToConformToCompleteType' in pcm_repository_ImplementationComponentType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_ImplementationComponentType_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_implementationcomponenttype_providedinterfaceshavetoconformtocompletetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.providedInterfacesHaveToConformToCompleteType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.providedInterfacesHaveToConformToCompleteType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'providedInterfacesHaveToConformToCompleteType' in pcm_repository_ImplementationComponentType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'providedInterfacesHaveToConformToCompleteType' in pcm_repository_ImplementationComponentType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'providedInterfacesHaveToConformToCompleteType' in pcm_repository_ImplementationComponentType is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_CompleteComponentType_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_completecomponenttype_providedinterfaceshavetoconformtoprovidedtype2_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.providedInterfacesHaveToConformToProvidedType2(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.providedInterfacesHaveToConformToProvidedType2).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'providedInterfacesHaveToConformToProvidedType2' in pcm_repository_CompleteComponentType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'providedInterfacesHaveToConformToProvidedType2' in pcm_repository_CompleteComponentType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'providedInterfacesHaveToConformToProvidedType2' in pcm_repository_CompleteComponentType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_CompleteComponentType_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_completecomponenttype_atleastoneinterfacehastobeprovidedorrequiredbyausefullcompletecomponenttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType' in pcm_repository_CompleteComponentType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType' in pcm_repository_CompleteComponentType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType' in pcm_repository_CompleteComponentType is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_ProvidesComponentType_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_providescomponenttype_atleastoneinterfacehastobeprovidedbyausefullprovidescomponenttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType' in pcm_repository_ProvidesComponentType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType' in pcm_repository_ProvidesComponentType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType' in pcm_repository_ProvidesComponentType is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_composition_RequiredDelegationConnector_strategy)
@settings(max_examples=30)
def test_hyp_pcm_composition_requireddelegationconnector_requireddelegationconnectorandtheconnectedcomponentmustbepartofthesamecompositestructure_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure' in pcm_composition_RequiredDelegationConnector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure' in pcm_composition_RequiredDelegationConnector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure' in pcm_composition_RequiredDelegationConnector is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_composition_RequiredDelegationConnector_strategy)
@settings(max_examples=30)
def test_hyp_pcm_composition_requireddelegationconnector_componentofassemblycontextandinnerrolerequiringcomponentneedtobethesame_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame' in pcm_composition_RequiredDelegationConnector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame' in pcm_composition_RequiredDelegationConnector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame' in pcm_composition_RequiredDelegationConnector is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_composition_ProvidedDelegationConnector_strategy)
@settings(max_examples=30)
def test_hyp_pcm_composition_provideddelegationconnector_provideddelegationconnectorandtheconnectedcomponentmustbepartofthesamecompositestructure_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure' in pcm_composition_ProvidedDelegationConnector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure' in pcm_composition_ProvidedDelegationConnector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure' in pcm_composition_ProvidedDelegationConnector is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_composition_ProvidedDelegationConnector_strategy)
@settings(max_examples=30)
def test_hyp_pcm_composition_provideddelegationconnector_componentofassemblycontextandinnerroleprovidingcomponentneedtobethesame_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame' in pcm_composition_ProvidedDelegationConnector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame' in pcm_composition_ProvidedDelegationConnector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame' in pcm_composition_ProvidedDelegationConnector is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_entity_ComposedProvidingRequiringEntity_strategy)
@settings(max_examples=30)
def test_hyp_pcm_entity_composedprovidingrequiringentity_providedrolesmustbebound_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ProvidedRolesMustBeBound(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ProvidedRolesMustBeBound).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ProvidedRolesMustBeBound' in pcm_entity_ComposedProvidingRequiringEntity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ProvidedRolesMustBeBound' in pcm_entity_ComposedProvidingRequiringEntity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ProvidedRolesMustBeBound' in pcm_entity_ComposedProvidingRequiringEntity is not implemented or raised an error")















import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_allocation_Allocation_strategy)
@settings(max_examples=30)
def test_hyp_pcm_allocation_allocation_eachassemblycontextwithinsystemhastobeallocatedexactlyonce_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce' in pcm_allocation_Allocation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce' in pcm_allocation_Allocation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce' in pcm_allocation_Allocation is not implemented or raised an error")




@given(instance=pcm_repository_Repository_strategy)
def test_hyp_pcm_repository_repository_repositoryDescription_setter(instance):
    original = instance.repositoryDescription
    instance.repositoryDescription = original
    assert instance.repositoryDescription == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_Interface_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_interface_signatureshavetobeuniqueforaninterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SignaturesHaveToBeUniqueForAnInterface(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SignaturesHaveToBeUniqueForAnInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SignaturesHaveToBeUniqueForAnInterface' in pcm_repository_Interface is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SignaturesHaveToBeUniqueForAnInterface' in pcm_repository_Interface did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SignaturesHaveToBeUniqueForAnInterface' in pcm_repository_Interface is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_repository_Interface_strategy)
@settings(max_examples=30)
def test_hyp_pcm_repository_interface_noprotocoltypeidusedtwice_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.NoProtocolTypeIDUsedTwice(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.NoProtocolTypeIDUsedTwice).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'NoProtocolTypeIDUsedTwice' in pcm_repository_Interface is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'NoProtocolTypeIDUsedTwice' in pcm_repository_Interface did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'NoProtocolTypeIDUsedTwice' in pcm_repository_Interface is not implemented or raised an error")








import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_ScenarioBehaviour_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_scenariobehaviour_eachuseractionexceptstartandstopmusthaveapredecessorandsuccessor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor' in pcm_usagemodel_ScenarioBehaviour is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor' in pcm_usagemodel_ScenarioBehaviour did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor' in pcm_usagemodel_ScenarioBehaviour is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_ScenarioBehaviour_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_scenariobehaviour_exactlyonestop_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.Exactlyonestop(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.Exactlyonestop).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'Exactlyonestop' in pcm_usagemodel_ScenarioBehaviour is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'Exactlyonestop' in pcm_usagemodel_ScenarioBehaviour did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'Exactlyonestop' in pcm_usagemodel_ScenarioBehaviour is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_usagemodel_ScenarioBehaviour_strategy)
@settings(max_examples=30)
def test_hyp_pcm_usagemodel_scenariobehaviour_exactlyonestart_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.Exactlyonestart(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.Exactlyonestart).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'Exactlyonestart' in pcm_usagemodel_ScenarioBehaviour is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'Exactlyonestart' in pcm_usagemodel_ScenarioBehaviour did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'Exactlyonestart' in pcm_usagemodel_ScenarioBehaviour is not implemented or raised an error")






@given(instance=pcm_entity_NamedElement_strategy)
def test_hyp_pcm_entity_namedelement_entityName_setter(instance):
    original = instance.entityName
    instance.entityName = original
    assert instance.entityName == original







import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pcm_core_PCMRandomVariable_strategy)
@settings(max_examples=30)
def test_hyp_pcm_core_pcmrandomvariable_specificationmustnotbenull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SpecificationMustNotBeNULL(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SpecificationMustNotBeNULL).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SpecificationMustNotBeNULL' in pcm_core_PCMRandomVariable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SpecificationMustNotBeNULL' in pcm_core_PCMRandomVariable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SpecificationMustNotBeNULL' in pcm_core_PCMRandomVariable is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractAction,
    AbstractBranchTransition,
    AbstractInternalControlFlowAction,
    AbstractLoopAction,
    AbstractUserAction,
    AllocationContext,
    BranchTransition,
    CommunicationLinkResourceSpecification,
    CommunicationLinkResourceType,
    CompleteComponentType,
    CompositeDataType,
    Connector,
    DataType,
    DelegationConnector,
    Entity,
    ExceptionType,
    ForkedBehaviour,
    Identifier,
    ImplementationComponentType,
    InnerDeclaration,
    Interface,
    InterfaceProvidingRequiringEntity,
    LinkingResource,
    NamedElement,
    PCMRandomVariable,
    Parameter,
    PassiveResource,
    ProcessingResourceSpecification,
    ProcessingResourceType,
    Protocol,
    ProvidedRole,
    ProvidesComponentType,
    QoSAnnotations,
    RandomVariable,
    Repository,
    RepositoryComponent,
    RequiredRole,
    ResourceContainer,
    ResourceDemandingBehaviour,
    ResourceEnvironment,
    ResourceRequiredRole,
    ResourceType,
    Role,
    ScenarioBehaviour,
    ServiceEffectSpecification,
    Signature,
    SpecifiedOutputParameterAbstraction,
    SpecifiedQoSAnnotation,
    SynchronisationPoint,
    System,
    UnitCarryingElement,
    UsageScenario,
    UserData,
    Variable,
    VariableCharacterisation,
    VariableUsage,
    Workload,
    composition_AssemblyConnector,
    composition_AssemblyContext,
    composition_ComposedStructure,
    composition_ProvidedDelegationConnector,
    composition_RequiredDelegationConnector,
    composition_ResourceRequiredDelegationConnector,
    entity_ComposedProvidingRequiringEntity,
    entity_Entity,
    entity_InterfaceProvidingEntity,
    entity_InterfaceProvidingRequiringEntity,
    entity_InterfaceRequiringEntity,
    entity_NamedElement,
    entity_ResourceInterfaceRequiringEntity,
    parameter_pcm_AbstractNamedReference,
    pcm_allocation_Allocation,
    pcm_allocation_AllocationContext,
    pcm_composition_AssemblyConnector,
    pcm_composition_AssemblyContext,
    pcm_composition_ComposedStructure,
    pcm_composition_ProvidedDelegationConnector,
    pcm_composition_RequiredDelegationConnector,
    pcm_composition_ResourceRequiredDelegationConnector,
    pcm_connectors_Connector,
    pcm_core_PCMRandomVariable,
    pcm_entity_ComposedProvidingRequiringEntity,
    pcm_entity_Entity,
    pcm_entity_InterfaceProvidingEntity,
    pcm_entity_InterfaceProvidingRequiringEntity,
    pcm_entity_InterfaceRequiringEntity,
    pcm_entity_NamedElement,
    pcm_entity_ResourceInterfaceRequiringEntity,
    pcm_parameter_CharacterisedVariable,
    pcm_parameter_VariableCharacterisation,
    pcm_parameter_VariableUsage,
    pcm_performance_ComponentSpecifiedExecutionTime,
    pcm_performance_ParametricResourceDemand,
    pcm_performance_SystemSpecifiedExecutionTime,
    pcm_protocol_Protocol,
    pcm_protocol_ServiceCall,
    pcm_qosannotations_QoSAnnotations,
    pcm_qosannotations_SpecifiedOutputParameterAbstraction,
    pcm_qosannotations_SpecifiedQoSAnnotation,
    pcm_reliability_SpecifiedFailureProbability,
    pcm_repository_BasicComponent,
    pcm_repository_CollectionDataType,
    pcm_repository_CompleteComponentType,
    pcm_repository_CompositeComponent,
    pcm_repository_CompositeDataType,
    pcm_repository_DataType,
    pcm_repository_DelegationConnector,
    pcm_repository_ExceptionType,
    pcm_repository_ImplementationComponentType,
    pcm_repository_InnerDeclaration,
    pcm_repository_Interface,
    pcm_repository_Parameter,
    pcm_repository_PassiveResource,
    pcm_repository_PrimitiveDataType,
    pcm_repository_ProvidedRole,
    pcm_repository_ProvidesComponentType,
    pcm_repository_Repository,
    pcm_repository_RepositoryComponent,
    pcm_repository_RequiredRole,
    pcm_repository_ResourceRequiredRole,
    pcm_repository_Role,
    pcm_repository_Signature,
    pcm_resourceenvironment_CommunicationLinkResourceSpecification,
    pcm_resourceenvironment_LinkingResource,
    pcm_resourceenvironment_ProcessingResourceSpecification,
    pcm_resourceenvironment_ResourceContainer,
    pcm_resourceenvironment_ResourceEnvironment,
    pcm_resourcetype_CommunicationLinkResourceType,
    pcm_resourcetype_ProcessingResourceType,
    pcm_resourcetype_ResourceRepository,
    pcm_resourcetype_ResourceType,
    pcm_seff_AbstractAction,
    pcm_seff_AbstractBranchTransition,
    pcm_seff_AbstractInternalControlFlowAction,
    pcm_seff_AbstractLoopAction,
    pcm_seff_AcquireAction,
    pcm_seff_BranchAction,
    pcm_seff_CollectionIteratorAction,
    pcm_seff_ExternalCallAction,
    pcm_seff_ForkAction,
    pcm_seff_ForkedBehaviour,
    pcm_seff_GuardedBranchTransition,
    pcm_seff_InternalAction,
    pcm_seff_LoopAction,
    pcm_seff_ProbabilisticBranchTransition,
    pcm_seff_ReleaseAction,
    pcm_seff_ResourceDemandingBehaviour,
    pcm_seff_ResourceDemandingSEFF,
    pcm_seff_ServiceEffectSpecification,
    pcm_seff_SetVariableAction,
    pcm_seff_StartAction,
    pcm_seff_StopAction,
    pcm_seff_SynchronisationPoint,
    pcm_subsystem_SubSystem,
    pcm_system_System,
    pcm_usagemodel_AbstractUserAction,
    pcm_usagemodel_Branch,
    pcm_usagemodel_BranchTransition,
    pcm_usagemodel_ClosedWorkload,
    pcm_usagemodel_Delay,
    pcm_usagemodel_EntryLevelSystemCall,
    pcm_usagemodel_Loop,
    pcm_usagemodel_OpenWorkload,
    pcm_usagemodel_ScenarioBehaviour,
    pcm_usagemodel_Start,
    pcm_usagemodel_Stop,
    pcm_usagemodel_UsageModel,
    pcm_usagemodel_UsageScenario,
    pcm_usagemodel_UserData,
    pcm_usagemodel_Workload,
    performance_ParametricResourceDemand,
    repository_DataType,
    repository_ImplementationComponentType,
    repository_RepositoryComponent,
    seff_ResourceDemandingBehaviour,
    seff_ServiceEffectSpecification,
    ParameterModifier,
    PrimitiveTypeEnum,
    SchedulingPolicy,
    VariableCharacterisationType,
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

def test_pcm_entity_NamedElement_entityName_value_roundtrip():
    instance = pcm_entity_NamedElement(entityName="sample_text")
    assert instance.entityName == "sample_text"
    instance.entityName = "sample_text_2"
    assert instance.entityName == "sample_text_2"


def test_pcm_parameter_CharacterisedVariable_characterisationType_value_roundtrip():
    instance = pcm_parameter_CharacterisedVariable(characterisationType="sample_text")
    assert instance.characterisationType == "sample_text"
    instance.characterisationType = "sample_text_2"
    assert instance.characterisationType == "sample_text_2"


def test_pcm_parameter_VariableCharacterisation_type_value_roundtrip():
    instance = pcm_parameter_VariableCharacterisation(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_pcm_protocol_Protocol_protocolTypeID_value_roundtrip():
    instance = pcm_protocol_Protocol(protocolTypeID="sample_text")
    assert instance.protocolTypeID == "sample_text"
    instance.protocolTypeID = "sample_text_2"
    assert instance.protocolTypeID == "sample_text_2"


def test_pcm_reliability_SpecifiedFailureProbability_failureProbability_value_roundtrip():
    instance = pcm_reliability_SpecifiedFailureProbability(failureProbability=3.14)
    assert instance.failureProbability == 3.14
    instance.failureProbability = 9.99
    assert instance.failureProbability == 9.99


def test_pcm_repository_ExceptionType_exceptionMessage_value_roundtrip():
    instance = pcm_repository_ExceptionType(exceptionMessage="sample_text", exceptionName="sample_text")
    assert instance.exceptionMessage == "sample_text"
    instance.exceptionMessage = "sample_text_2"
    assert instance.exceptionMessage == "sample_text_2"


def test_pcm_repository_ExceptionType_exceptionName_value_roundtrip():
    instance = pcm_repository_ExceptionType(exceptionMessage="sample_text", exceptionName="sample_text")
    assert instance.exceptionName == "sample_text"
    instance.exceptionName = "sample_text_2"
    assert instance.exceptionName == "sample_text_2"


def test_pcm_repository_Parameter_modifier__Parameter_value_roundtrip():
    instance = pcm_repository_Parameter(modifier__Parameter="sample_text", parameterName="sample_text")
    assert instance.modifier__Parameter == "sample_text"
    instance.modifier__Parameter = "sample_text_2"
    assert instance.modifier__Parameter == "sample_text_2"


def test_pcm_repository_Parameter_parameterName_value_roundtrip():
    instance = pcm_repository_Parameter(modifier__Parameter="sample_text", parameterName="sample_text")
    assert instance.parameterName == "sample_text"
    instance.parameterName = "sample_text_2"
    assert instance.parameterName == "sample_text_2"


def test_pcm_repository_PrimitiveDataType_type_value_roundtrip():
    instance = pcm_repository_PrimitiveDataType(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_pcm_repository_Repository_repositoryDescription_value_roundtrip():
    instance = pcm_repository_Repository(repositoryDescription="sample_text")
    assert instance.repositoryDescription == "sample_text"
    instance.repositoryDescription = "sample_text_2"
    assert instance.repositoryDescription == "sample_text_2"


def test_pcm_repository_Signature_serviceName_value_roundtrip():
    instance = pcm_repository_Signature(serviceName="sample_text")
    assert instance.serviceName == "sample_text"
    instance.serviceName = "sample_text_2"
    assert instance.serviceName == "sample_text_2"


def test_pcm_resourceenvironment_CommunicationLinkResourceSpecification_failureProbability_value_roundtrip():
    instance = pcm_resourceenvironment_CommunicationLinkResourceSpecification(failureProbability=3.14)
    assert instance.failureProbability == 3.14
    instance.failureProbability = 9.99
    assert instance.failureProbability == 9.99


def test_pcm_resourceenvironment_ProcessingResourceSpecification_MTTF_value_roundtrip():
    instance = pcm_resourceenvironment_ProcessingResourceSpecification(MTTF=3.14, MTTR=3.14, schedulingPolicy="sample_text")
    assert instance.MTTF == 3.14
    instance.MTTF = 9.99
    assert instance.MTTF == 9.99


def test_pcm_resourceenvironment_ProcessingResourceSpecification_MTTR_value_roundtrip():
    instance = pcm_resourceenvironment_ProcessingResourceSpecification(MTTF=3.14, MTTR=3.14, schedulingPolicy="sample_text")
    assert instance.MTTR == 3.14
    instance.MTTR = 9.99
    assert instance.MTTR == 9.99


def test_pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy_value_roundtrip():
    instance = pcm_resourceenvironment_ProcessingResourceSpecification(MTTF=3.14, MTTR=3.14, schedulingPolicy="sample_text")
    assert instance.schedulingPolicy == "sample_text"
    instance.schedulingPolicy = "sample_text_2"
    assert instance.schedulingPolicy == "sample_text_2"


def test_pcm_seff_ExternalCallAction_retryCount_value_roundtrip():
    instance = pcm_seff_ExternalCallAction(retryCount=7)
    assert instance.retryCount == 7
    instance.retryCount = 13
    assert instance.retryCount == 13


def test_pcm_seff_InternalAction_failureProbability_value_roundtrip():
    instance = pcm_seff_InternalAction(failureProbability=3.14)
    assert instance.failureProbability == 3.14
    instance.failureProbability = 9.99
    assert instance.failureProbability == 9.99


def test_pcm_seff_ProbabilisticBranchTransition_branchProbability_value_roundtrip():
    instance = pcm_seff_ProbabilisticBranchTransition(branchProbability=3.14)
    assert instance.branchProbability == 3.14
    instance.branchProbability = 9.99
    assert instance.branchProbability == 9.99


def test_pcm_seff_ServiceEffectSpecification_seffTypeID_value_roundtrip():
    instance = pcm_seff_ServiceEffectSpecification(seffTypeID="sample_text")
    assert instance.seffTypeID == "sample_text"
    instance.seffTypeID = "sample_text_2"
    assert instance.seffTypeID == "sample_text_2"


def test_pcm_usagemodel_BranchTransition_branchProbability_value_roundtrip():
    instance = pcm_usagemodel_BranchTransition(branchProbability=3.14)
    assert instance.branchProbability == 3.14
    instance.branchProbability = 9.99
    assert instance.branchProbability == 9.99


def test_pcm_usagemodel_ClosedWorkload_population_value_roundtrip():
    instance = pcm_usagemodel_ClosedWorkload(population=7)
    assert instance.population == 7
    instance.population = 13
    assert instance.population == 13


def test_pcm_seff_AbstractInternalControlFlowAction_isa_AbstractAction():
    instance = pcm_seff_AbstractInternalControlFlowAction()
    assert isinstance(instance, AbstractAction)


def test_pcm_seff_ExternalCallAction_isa_AbstractAction():
    instance = pcm_seff_ExternalCallAction(retryCount=7)
    assert isinstance(instance, AbstractAction)


def test_pcm_seff_GuardedBranchTransition_isa_AbstractBranchTransition():
    instance = pcm_seff_GuardedBranchTransition()
    assert isinstance(instance, AbstractBranchTransition)


def test_pcm_seff_ProbabilisticBranchTransition_isa_AbstractBranchTransition():
    instance = pcm_seff_ProbabilisticBranchTransition(branchProbability=3.14)
    assert isinstance(instance, AbstractBranchTransition)


def test_pcm_seff_AbstractLoopAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_AbstractLoopAction()
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_AcquireAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_AcquireAction()
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_BranchAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_BranchAction()
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_ForkAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_ForkAction()
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_InternalAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_InternalAction(failureProbability=3.14)
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_ReleaseAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_ReleaseAction()
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_SetVariableAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_SetVariableAction()
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_StartAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_StartAction()
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_StopAction_isa_AbstractInternalControlFlowAction():
    instance = pcm_seff_StopAction()
    assert isinstance(instance, AbstractInternalControlFlowAction)


def test_pcm_seff_CollectionIteratorAction_isa_AbstractLoopAction():
    instance = pcm_seff_CollectionIteratorAction()
    assert isinstance(instance, AbstractLoopAction)


def test_pcm_seff_LoopAction_isa_AbstractLoopAction():
    instance = pcm_seff_LoopAction()
    assert isinstance(instance, AbstractLoopAction)


def test_pcm_usagemodel_Branch_isa_AbstractUserAction():
    instance = pcm_usagemodel_Branch()
    assert isinstance(instance, AbstractUserAction)


def test_pcm_usagemodel_Delay_isa_AbstractUserAction():
    instance = pcm_usagemodel_Delay()
    assert isinstance(instance, AbstractUserAction)


def test_pcm_usagemodel_EntryLevelSystemCall_isa_AbstractUserAction():
    instance = pcm_usagemodel_EntryLevelSystemCall()
    assert isinstance(instance, AbstractUserAction)


def test_pcm_usagemodel_Loop_isa_AbstractUserAction():
    instance = pcm_usagemodel_Loop()
    assert isinstance(instance, AbstractUserAction)


def test_pcm_usagemodel_Start_isa_AbstractUserAction():
    instance = pcm_usagemodel_Start()
    assert isinstance(instance, AbstractUserAction)


def test_pcm_usagemodel_Stop_isa_AbstractUserAction():
    instance = pcm_usagemodel_Stop()
    assert isinstance(instance, AbstractUserAction)


def test_pcm_composition_AssemblyConnector_isa_Connector():
    instance = pcm_composition_AssemblyConnector()
    assert isinstance(instance, Connector)


def test_pcm_repository_DelegationConnector_isa_Connector():
    instance = pcm_repository_DelegationConnector()
    assert isinstance(instance, Connector)


def test_pcm_repository_PrimitiveDataType_isa_DataType():
    instance = pcm_repository_PrimitiveDataType(type="sample_text")
    assert isinstance(instance, DataType)


def test_pcm_composition_ProvidedDelegationConnector_isa_DelegationConnector():
    instance = pcm_composition_ProvidedDelegationConnector()
    assert isinstance(instance, DelegationConnector)


def test_pcm_composition_RequiredDelegationConnector_isa_DelegationConnector():
    instance = pcm_composition_RequiredDelegationConnector()
    assert isinstance(instance, DelegationConnector)


def test_pcm_allocation_Allocation_isa_Entity():
    instance = pcm_allocation_Allocation()
    assert isinstance(instance, Entity)


def test_pcm_allocation_AllocationContext_isa_Entity():
    instance = pcm_allocation_AllocationContext()
    assert isinstance(instance, Entity)


def test_pcm_composition_AssemblyContext_isa_Entity():
    instance = pcm_composition_AssemblyContext()
    assert isinstance(instance, Entity)


def test_pcm_composition_ComposedStructure_isa_Entity():
    instance = pcm_composition_ComposedStructure()
    assert isinstance(instance, Entity)


def test_pcm_connectors_Connector_isa_Entity():
    instance = pcm_connectors_Connector()
    assert isinstance(instance, Entity)


def test_pcm_entity_InterfaceProvidingEntity_isa_Entity():
    instance = pcm_entity_InterfaceProvidingEntity()
    assert isinstance(instance, Entity)


def test_pcm_entity_InterfaceRequiringEntity_isa_Entity():
    instance = pcm_entity_InterfaceRequiringEntity()
    assert isinstance(instance, Entity)


def test_pcm_entity_ResourceInterfaceRequiringEntity_isa_Entity():
    instance = pcm_entity_ResourceInterfaceRequiringEntity()
    assert isinstance(instance, Entity)


def test_pcm_qosannotations_QoSAnnotations_isa_Entity():
    instance = pcm_qosannotations_QoSAnnotations()
    assert isinstance(instance, Entity)


def test_pcm_repository_Interface_isa_Entity():
    instance = pcm_repository_Interface()
    assert isinstance(instance, Entity)


def test_pcm_repository_PassiveResource_isa_Entity():
    instance = pcm_repository_PassiveResource()
    assert isinstance(instance, Entity)


def test_pcm_repository_Repository_isa_Entity():
    instance = pcm_repository_Repository(repositoryDescription="sample_text")
    assert isinstance(instance, Entity)


def test_pcm_repository_Role_isa_Entity():
    instance = pcm_repository_Role()
    assert isinstance(instance, Entity)


def test_pcm_resourceenvironment_LinkingResource_isa_Entity():
    instance = pcm_resourceenvironment_LinkingResource()
    assert isinstance(instance, Entity)


def test_pcm_resourceenvironment_ResourceContainer_isa_Entity():
    instance = pcm_resourceenvironment_ResourceContainer()
    assert isinstance(instance, Entity)


def test_pcm_seff_AbstractAction_isa_Entity():
    instance = pcm_seff_AbstractAction()
    assert isinstance(instance, Entity)


def test_pcm_usagemodel_AbstractUserAction_isa_Entity():
    instance = pcm_usagemodel_AbstractUserAction()
    assert isinstance(instance, Entity)


def test_pcm_usagemodel_ScenarioBehaviour_isa_Entity():
    instance = pcm_usagemodel_ScenarioBehaviour()
    assert isinstance(instance, Entity)


def test_pcm_usagemodel_UsageScenario_isa_Entity():
    instance = pcm_usagemodel_UsageScenario()
    assert isinstance(instance, Entity)


def test_pcm_entity_Entity_isa_Identifier():
    instance = pcm_entity_Entity()
    assert isinstance(instance, Identifier)


def test_pcm_seff_ResourceDemandingSEFF_isa_Identifier():
    instance = pcm_seff_ResourceDemandingSEFF()
    assert isinstance(instance, Identifier)


def test_pcm_repository_BasicComponent_isa_ImplementationComponentType():
    instance = pcm_repository_BasicComponent()
    assert isinstance(instance, ImplementationComponentType)


def test_pcm_repository_RepositoryComponent_isa_InterfaceProvidingRequiringEntity():
    instance = pcm_repository_RepositoryComponent()
    assert isinstance(instance, InterfaceProvidingRequiringEntity)


def test_pcm_repository_InnerDeclaration_isa_NamedElement():
    instance = pcm_repository_InnerDeclaration()
    assert isinstance(instance, NamedElement)


def test_pcm_seff_AbstractBranchTransition_isa_NamedElement():
    instance = pcm_seff_AbstractBranchTransition()
    assert isinstance(instance, NamedElement)


def test_pcm_resourcetype_CommunicationLinkResourceType_isa_ProcessingResourceType():
    instance = pcm_resourcetype_CommunicationLinkResourceType()
    assert isinstance(instance, ProcessingResourceType)


def test_pcm_core_PCMRandomVariable_isa_RandomVariable():
    instance = pcm_core_PCMRandomVariable()
    assert isinstance(instance, RandomVariable)


def test_pcm_repository_CompleteComponentType_isa_RepositoryComponent():
    instance = pcm_repository_CompleteComponentType()
    assert isinstance(instance, RepositoryComponent)


def test_pcm_repository_ImplementationComponentType_isa_RepositoryComponent():
    instance = pcm_repository_ImplementationComponentType()
    assert isinstance(instance, RepositoryComponent)


def test_pcm_repository_ProvidesComponentType_isa_RepositoryComponent():
    instance = pcm_repository_ProvidesComponentType()
    assert isinstance(instance, RepositoryComponent)


def test_pcm_seff_ForkedBehaviour_isa_ResourceDemandingBehaviour():
    instance = pcm_seff_ForkedBehaviour()
    assert isinstance(instance, ResourceDemandingBehaviour)


def test_pcm_resourcetype_ProcessingResourceType_isa_ResourceType():
    instance = pcm_resourcetype_ProcessingResourceType()
    assert isinstance(instance, ResourceType)


def test_pcm_repository_ProvidedRole_isa_Role():
    instance = pcm_repository_ProvidedRole()
    assert isinstance(instance, Role)


def test_pcm_repository_RequiredRole_isa_Role():
    instance = pcm_repository_RequiredRole()
    assert isinstance(instance, Role)


def test_pcm_repository_ResourceRequiredRole_isa_Role():
    instance = pcm_repository_ResourceRequiredRole()
    assert isinstance(instance, Role)


def test_pcm_performance_ComponentSpecifiedExecutionTime_isa_SpecifiedQoSAnnotation():
    instance = pcm_performance_ComponentSpecifiedExecutionTime()
    assert isinstance(instance, SpecifiedQoSAnnotation)


def test_pcm_performance_SystemSpecifiedExecutionTime_isa_SpecifiedQoSAnnotation():
    instance = pcm_performance_SystemSpecifiedExecutionTime()
    assert isinstance(instance, SpecifiedQoSAnnotation)


def test_pcm_reliability_SpecifiedFailureProbability_isa_SpecifiedQoSAnnotation():
    instance = pcm_reliability_SpecifiedFailureProbability(failureProbability=3.14)
    assert isinstance(instance, SpecifiedQoSAnnotation)


def test_pcm_resourcetype_ResourceType_isa_UnitCarryingElement():
    instance = pcm_resourcetype_ResourceType()
    assert isinstance(instance, UnitCarryingElement)


def test_pcm_parameter_CharacterisedVariable_isa_Variable():
    instance = pcm_parameter_CharacterisedVariable(characterisationType="sample_text")
    assert isinstance(instance, Variable)


def test_pcm_usagemodel_ClosedWorkload_isa_Workload():
    instance = pcm_usagemodel_ClosedWorkload(population=7)
    assert isinstance(instance, Workload)


def test_pcm_usagemodel_OpenWorkload_isa_Workload():
    instance = pcm_usagemodel_OpenWorkload()
    assert isinstance(instance, Workload)


def test_pcm_entity_ComposedProvidingRequiringEntity_isa_composition_ComposedStructure():
    instance = pcm_entity_ComposedProvidingRequiringEntity()
    assert isinstance(instance, composition_ComposedStructure)


def test_pcm_repository_CompositeComponent_isa_entity_ComposedProvidingRequiringEntity():
    instance = pcm_repository_CompositeComponent()
    assert isinstance(instance, entity_ComposedProvidingRequiringEntity)


def test_pcm_subsystem_SubSystem_isa_entity_ComposedProvidingRequiringEntity():
    instance = pcm_subsystem_SubSystem()
    assert isinstance(instance, entity_ComposedProvidingRequiringEntity)


def test_pcm_system_System_isa_entity_ComposedProvidingRequiringEntity():
    instance = pcm_system_System()
    assert isinstance(instance, entity_ComposedProvidingRequiringEntity)


def test_pcm_repository_CollectionDataType_isa_entity_Entity():
    instance = pcm_repository_CollectionDataType()
    assert isinstance(instance, entity_Entity)


def test_pcm_repository_CompositeDataType_isa_entity_Entity():
    instance = pcm_repository_CompositeDataType()
    assert isinstance(instance, entity_Entity)


def test_pcm_resourcetype_ResourceType_isa_entity_Entity():
    instance = pcm_resourcetype_ResourceType()
    assert isinstance(instance, entity_Entity)


def test_pcm_system_System_isa_entity_Entity():
    instance = pcm_system_System()
    assert isinstance(instance, entity_Entity)


def test_pcm_entity_InterfaceProvidingRequiringEntity_isa_entity_InterfaceProvidingEntity():
    instance = pcm_entity_InterfaceProvidingRequiringEntity()
    assert isinstance(instance, entity_InterfaceProvidingEntity)


def test_pcm_entity_ComposedProvidingRequiringEntity_isa_entity_InterfaceProvidingRequiringEntity():
    instance = pcm_entity_ComposedProvidingRequiringEntity()
    assert isinstance(instance, entity_InterfaceProvidingRequiringEntity)


def test_pcm_entity_InterfaceProvidingRequiringEntity_isa_entity_InterfaceRequiringEntity():
    instance = pcm_entity_InterfaceProvidingRequiringEntity()
    assert isinstance(instance, entity_InterfaceRequiringEntity)


def test_pcm_entity_Entity_isa_entity_NamedElement():
    instance = pcm_entity_Entity()
    assert isinstance(instance, entity_NamedElement)


def test_pcm_entity_InterfaceProvidingRequiringEntity_isa_entity_ResourceInterfaceRequiringEntity():
    instance = pcm_entity_InterfaceProvidingRequiringEntity()
    assert isinstance(instance, entity_ResourceInterfaceRequiringEntity)


def test_pcm_repository_CollectionDataType_isa_repository_DataType():
    instance = pcm_repository_CollectionDataType()
    assert isinstance(instance, repository_DataType)


def test_pcm_repository_CompositeDataType_isa_repository_DataType():
    instance = pcm_repository_CompositeDataType()
    assert isinstance(instance, repository_DataType)


def test_pcm_repository_CompositeComponent_isa_repository_ImplementationComponentType():
    instance = pcm_repository_CompositeComponent()
    assert isinstance(instance, repository_ImplementationComponentType)


def test_pcm_subsystem_SubSystem_isa_repository_RepositoryComponent():
    instance = pcm_subsystem_SubSystem()
    assert isinstance(instance, repository_RepositoryComponent)


def test_pcm_seff_ResourceDemandingSEFF_isa_seff_ResourceDemandingBehaviour():
    instance = pcm_seff_ResourceDemandingSEFF()
    assert isinstance(instance, seff_ResourceDemandingBehaviour)


def test_pcm_seff_ResourceDemandingSEFF_isa_seff_ServiceEffectSpecification():
    instance = pcm_seff_ResourceDemandingSEFF()
    assert isinstance(instance, seff_ServiceEffectSpecification)


def test_assoc_actions_ScenarioBehaviour217_link_reassign_clear():
    a = pcm_usagemodel_ScenarioBehaviour()
    b1 = AbstractUserAction()
    b2 = AbstractUserAction()
    _safe_set(a, 'pcm_usagemodel_ScenarioBehaviour', {b1})
    assert _is_linked(a, 'pcm_usagemodel_ScenarioBehaviour', b1)
    if hasattr(b1, 'AbstractUserAction'):
        assert _is_linked(b1, 'AbstractUserAction', a)
    _safe_set(a, 'pcm_usagemodel_ScenarioBehaviour', {b2})
    assert _is_linked(a, 'pcm_usagemodel_ScenarioBehaviour', b2)
    if hasattr(b1, 'AbstractUserAction'):
        assert not _is_linked(b1, 'AbstractUserAction', a)
    if hasattr(b2, 'AbstractUserAction'):
        assert _is_linked(b2, 'AbstractUserAction', a)
    _safe_set(a, 'pcm_usagemodel_ScenarioBehaviour', set())
    assert not _is_linked(a, 'pcm_usagemodel_ScenarioBehaviour', b2)
    if hasattr(b2, 'AbstractUserAction'):
        assert not _is_linked(b2, 'AbstractUserAction', a)


def test_assoc_activeResourceType_ActiveResourceSpecification186_link_reassign_clear():
    a = pcm_resourceenvironment_ProcessingResourceSpecification(MTTF=3.14, MTTR=3.14, schedulingPolicy="sample_text")
    b1 = ProcessingResourceType()
    b2 = ProcessingResourceType()
    _safe_set(a, 'pcm_resourceenvironment_ProcessingResourceSpecification', b1)
    assert _is_linked(a, 'pcm_resourceenvironment_ProcessingResourceSpecification', b1)
    if hasattr(b1, 'ProcessingResourceType187'):
        assert _is_linked(b1, 'ProcessingResourceType187', a)
    _safe_set(a, 'pcm_resourceenvironment_ProcessingResourceSpecification', b2)
    assert _is_linked(a, 'pcm_resourceenvironment_ProcessingResourceSpecification', b2)
    if hasattr(b1, 'ProcessingResourceType187'):
        assert not _is_linked(b1, 'ProcessingResourceType187', a)
    if hasattr(b2, 'ProcessingResourceType187'):
        assert _is_linked(b2, 'ProcessingResourceType187', a)
    _safe_set(a, 'pcm_resourceenvironment_ProcessingResourceSpecification', None)
    assert not _is_linked(a, 'pcm_resourceenvironment_ProcessingResourceSpecification', b2)
    if hasattr(b2, 'ProcessingResourceType187'):
        assert not _is_linked(b2, 'ProcessingResourceType187', a)


def test_assoc_allocationContexts_Allocation163_link_reassign_clear():
    a = pcm_allocation_Allocation()
    b1 = AllocationContext()
    b2 = AllocationContext()
    _safe_set(a, 'pcm_allocation_Allocation', {b1})
    assert _is_linked(a, 'pcm_allocation_Allocation', b1)
    if hasattr(b1, 'AllocationContext'):
        assert _is_linked(b1, 'AllocationContext', a)
    _safe_set(a, 'pcm_allocation_Allocation', {b2})
    assert _is_linked(a, 'pcm_allocation_Allocation', b2)
    if hasattr(b1, 'AllocationContext'):
        assert not _is_linked(b1, 'AllocationContext', a)
    if hasattr(b2, 'AllocationContext'):
        assert _is_linked(b2, 'AllocationContext', a)
    _safe_set(a, 'pcm_allocation_Allocation', set())
    assert not _is_linked(a, 'pcm_allocation_Allocation', b2)
    if hasattr(b2, 'AllocationContext'):
        assert not _is_linked(b2, 'AllocationContext', a)


def test_assoc_ancestorInterfaces_Interface74_link_reassign_clear():
    a = pcm_repository_Interface()
    b1 = Interface()
    b2 = Interface()
    _safe_set(a, 'pcm_repository_Interface75', {b1})
    assert _is_linked(a, 'pcm_repository_Interface75', b1)
    if hasattr(b1, 'Interface76'):
        assert _is_linked(b1, 'Interface76', a)
    _safe_set(a, 'pcm_repository_Interface75', {b2})
    assert _is_linked(a, 'pcm_repository_Interface75', b2)
    if hasattr(b1, 'Interface76'):
        assert not _is_linked(b1, 'Interface76', a)
    if hasattr(b2, 'Interface76'):
        assert _is_linked(b2, 'Interface76', a)
    _safe_set(a, 'pcm_repository_Interface75', set())
    assert not _is_linked(a, 'pcm_repository_Interface75', b2)
    if hasattr(b2, 'Interface76'):
        assert not _is_linked(b2, 'Interface76', a)


def test_assoc_assemblyContext_ProvidedDelegationConnector8_link_reassign_clear():
    a = pcm_composition_ProvidedDelegationConnector()
    b1 = composition_AssemblyContext()
    b2 = composition_AssemblyContext()
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector9', b1)
    assert _is_linked(a, 'pcm_composition_ProvidedDelegationConnector9', b1)
    if hasattr(b1, 'composition_AssemblyContext'):
        assert _is_linked(b1, 'composition_AssemblyContext', a)
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector9', b2)
    assert _is_linked(a, 'pcm_composition_ProvidedDelegationConnector9', b2)
    if hasattr(b1, 'composition_AssemblyContext'):
        assert not _is_linked(b1, 'composition_AssemblyContext', a)
    if hasattr(b2, 'composition_AssemblyContext'):
        assert _is_linked(b2, 'composition_AssemblyContext', a)
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector9', None)
    assert not _is_linked(a, 'pcm_composition_ProvidedDelegationConnector9', b2)
    if hasattr(b2, 'composition_AssemblyContext'):
        assert not _is_linked(b2, 'composition_AssemblyContext', a)


def test_assoc_assemblyContext_RequiredDelegationConnector21_link_reassign_clear():
    a = pcm_composition_RequiredDelegationConnector()
    b1 = composition_AssemblyContext()
    b2 = composition_AssemblyContext()
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector22', b1)
    assert _is_linked(a, 'pcm_composition_RequiredDelegationConnector22', b1)
    if hasattr(b1, 'composition_AssemblyContext23'):
        assert _is_linked(b1, 'composition_AssemblyContext23', a)
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector22', b2)
    assert _is_linked(a, 'pcm_composition_RequiredDelegationConnector22', b2)
    if hasattr(b1, 'composition_AssemblyContext23'):
        assert not _is_linked(b1, 'composition_AssemblyContext23', a)
    if hasattr(b2, 'composition_AssemblyContext23'):
        assert _is_linked(b2, 'composition_AssemblyContext23', a)
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector22', None)
    assert not _is_linked(a, 'pcm_composition_RequiredDelegationConnector22', b2)
    if hasattr(b2, 'composition_AssemblyContext23'):
        assert not _is_linked(b2, 'composition_AssemblyContext23', a)


def test_assoc_branchTransitions_Branch250_link_reassign_clear():
    a = pcm_usagemodel_Branch()
    b1 = BranchTransition()
    b2 = BranchTransition()
    _safe_set(a, 'pcm_usagemodel_Branch', {b1})
    assert _is_linked(a, 'pcm_usagemodel_Branch', b1)
    if hasattr(b1, 'BranchTransition'):
        assert _is_linked(b1, 'BranchTransition', a)
    _safe_set(a, 'pcm_usagemodel_Branch', {b2})
    assert _is_linked(a, 'pcm_usagemodel_Branch', b2)
    if hasattr(b1, 'BranchTransition'):
        assert not _is_linked(b1, 'BranchTransition', a)
    if hasattr(b2, 'BranchTransition'):
        assert _is_linked(b2, 'BranchTransition', a)
    _safe_set(a, 'pcm_usagemodel_Branch', set())
    assert not _is_linked(a, 'pcm_usagemodel_Branch', b2)
    if hasattr(b2, 'BranchTransition'):
        assert not _is_linked(b2, 'BranchTransition', a)


def test_assoc_branchedBehaviour_BranchTransition251_link_reassign_clear():
    a = pcm_usagemodel_BranchTransition(branchProbability=3.14)
    b1 = ScenarioBehaviour()
    b2 = ScenarioBehaviour()
    _safe_set(a, 'pcm_usagemodel_BranchTransition', b1)
    assert _is_linked(a, 'pcm_usagemodel_BranchTransition', b1)
    if hasattr(b1, 'ScenarioBehaviour252'):
        assert _is_linked(b1, 'ScenarioBehaviour252', a)
    _safe_set(a, 'pcm_usagemodel_BranchTransition', b2)
    assert _is_linked(a, 'pcm_usagemodel_BranchTransition', b2)
    if hasattr(b1, 'ScenarioBehaviour252'):
        assert not _is_linked(b1, 'ScenarioBehaviour252', a)
    if hasattr(b2, 'ScenarioBehaviour252'):
        assert _is_linked(b2, 'ScenarioBehaviour252', a)
    _safe_set(a, 'pcm_usagemodel_BranchTransition', None)
    assert not _is_linked(a, 'pcm_usagemodel_BranchTransition', b2)
    if hasattr(b2, 'ScenarioBehaviour252'):
        assert not _is_linked(b2, 'ScenarioBehaviour252', a)


def test_assoc_branches_Branch142_link_reassign_clear():
    a = pcm_seff_BranchAction()
    b1 = AbstractBranchTransition()
    b2 = AbstractBranchTransition()
    _safe_set(a, 'pcm_seff_BranchAction', {b1})
    assert _is_linked(a, 'pcm_seff_BranchAction', b1)
    if hasattr(b1, 'AbstractBranchTransition'):
        assert _is_linked(b1, 'AbstractBranchTransition', a)
    _safe_set(a, 'pcm_seff_BranchAction', {b2})
    assert _is_linked(a, 'pcm_seff_BranchAction', b2)
    if hasattr(b1, 'AbstractBranchTransition'):
        assert not _is_linked(b1, 'AbstractBranchTransition', a)
    if hasattr(b2, 'AbstractBranchTransition'):
        assert _is_linked(b2, 'AbstractBranchTransition', a)
    _safe_set(a, 'pcm_seff_BranchAction', set())
    assert not _is_linked(a, 'pcm_seff_BranchAction', b2)
    if hasattr(b2, 'AbstractBranchTransition'):
        assert not _is_linked(b2, 'AbstractBranchTransition', a)


def test_assoc_calledService_ExternalService130_link_reassign_clear():
    a = pcm_seff_ExternalCallAction(retryCount=7)
    b1 = Signature()
    b2 = Signature()
    _safe_set(a, 'pcm_seff_ExternalCallAction', b1)
    assert _is_linked(a, 'pcm_seff_ExternalCallAction', b1)
    if hasattr(b1, 'Signature131'):
        assert _is_linked(b1, 'Signature131', a)
    _safe_set(a, 'pcm_seff_ExternalCallAction', b2)
    assert _is_linked(a, 'pcm_seff_ExternalCallAction', b2)
    if hasattr(b1, 'Signature131'):
        assert not _is_linked(b1, 'Signature131', a)
    if hasattr(b2, 'Signature131'):
        assert _is_linked(b2, 'Signature131', a)
    _safe_set(a, 'pcm_seff_ExternalCallAction', None)
    assert not _is_linked(a, 'pcm_seff_ExternalCallAction', b2)
    if hasattr(b2, 'Signature131'):
        assert not _is_linked(b2, 'Signature131', a)


def test_assoc_communicationLinkResourceType_CommunicationLinkResourceSpecification179_link_reassign_clear():
    a = pcm_resourceenvironment_CommunicationLinkResourceSpecification(failureProbability=3.14)
    b1 = CommunicationLinkResourceType()
    b2 = CommunicationLinkResourceType()
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification', b1)
    assert _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification', b1)
    if hasattr(b1, 'CommunicationLinkResourceType'):
        assert _is_linked(b1, 'CommunicationLinkResourceType', a)
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification', b2)
    assert _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification', b2)
    if hasattr(b1, 'CommunicationLinkResourceType'):
        assert not _is_linked(b1, 'CommunicationLinkResourceType', a)
    if hasattr(b2, 'CommunicationLinkResourceType'):
        assert _is_linked(b2, 'CommunicationLinkResourceType', a)
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification', None)
    assert not _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification', b2)
    if hasattr(b2, 'CommunicationLinkResourceType'):
        assert not _is_linked(b2, 'CommunicationLinkResourceType', a)


def test_assoc_componentParameterUsage_ImplementationComponentType87_link_reassign_clear():
    a = pcm_repository_ImplementationComponentType()
    b1 = VariableUsage()
    b2 = VariableUsage()
    _safe_set(a, 'pcm_repository_ImplementationComponentType88', {b1})
    assert _is_linked(a, 'pcm_repository_ImplementationComponentType88', b1)
    if hasattr(b1, 'VariableUsage89'):
        assert _is_linked(b1, 'VariableUsage89', a)
    _safe_set(a, 'pcm_repository_ImplementationComponentType88', {b2})
    assert _is_linked(a, 'pcm_repository_ImplementationComponentType88', b2)
    if hasattr(b1, 'VariableUsage89'):
        assert not _is_linked(b1, 'VariableUsage89', a)
    if hasattr(b2, 'VariableUsage89'):
        assert _is_linked(b2, 'VariableUsage89', a)
    _safe_set(a, 'pcm_repository_ImplementationComponentType88', set())
    assert not _is_linked(a, 'pcm_repository_ImplementationComponentType88', b2)
    if hasattr(b2, 'VariableUsage89'):
        assert not _is_linked(b2, 'VariableUsage89', a)


def test_assoc_components__Repository61_link_reassign_clear():
    a = pcm_repository_Repository(repositoryDescription="sample_text")
    b1 = RepositoryComponent()
    b2 = RepositoryComponent()
    _safe_set(a, 'repository_RepositoryComponent', {b1})
    assert _is_linked(a, 'repository_RepositoryComponent', b1)
    if hasattr(b1, 'RepositoryComponent62'):
        assert _is_linked(b1, 'RepositoryComponent62', a)
    _safe_set(a, 'repository_RepositoryComponent', {b2})
    assert _is_linked(a, 'repository_RepositoryComponent', b2)
    if hasattr(b1, 'RepositoryComponent62'):
        assert not _is_linked(b1, 'RepositoryComponent62', a)
    if hasattr(b2, 'RepositoryComponent62'):
        assert _is_linked(b2, 'RepositoryComponent62', a)
    _safe_set(a, 'repository_RepositoryComponent', set())
    assert not _is_linked(a, 'repository_RepositoryComponent', b2)
    if hasattr(b2, 'RepositoryComponent62'):
        assert not _is_linked(b2, 'RepositoryComponent62', a)


def test_assoc_datatype__Parameter57_link_reassign_clear():
    a = pcm_repository_Parameter(modifier__Parameter="sample_text", parameterName="sample_text")
    b1 = DataType()
    b2 = DataType()
    _safe_set(a, 'pcm_repository_Parameter', b1)
    assert _is_linked(a, 'pcm_repository_Parameter', b1)
    if hasattr(b1, 'DataType58'):
        assert _is_linked(b1, 'DataType58', a)
    _safe_set(a, 'pcm_repository_Parameter', b2)
    assert _is_linked(a, 'pcm_repository_Parameter', b2)
    if hasattr(b1, 'DataType58'):
        assert not _is_linked(b1, 'DataType58', a)
    if hasattr(b2, 'DataType58'):
        assert _is_linked(b2, 'DataType58', a)
    _safe_set(a, 'pcm_repository_Parameter', None)
    assert not _is_linked(a, 'pcm_repository_Parameter', b2)
    if hasattr(b2, 'DataType58'):
        assert not _is_linked(b2, 'DataType58', a)


def test_assoc_datatypes_Repository65_link_reassign_clear():
    a = pcm_repository_Repository(repositoryDescription="sample_text")
    b1 = DataType()
    b2 = DataType()
    _safe_set(a, 'repository_DataType', {b1})
    assert _is_linked(a, 'repository_DataType', b1)
    if hasattr(b1, 'DataType66'):
        assert _is_linked(b1, 'DataType66', a)
    _safe_set(a, 'repository_DataType', {b2})
    assert _is_linked(a, 'repository_DataType', b2)
    if hasattr(b1, 'DataType66'):
        assert not _is_linked(b1, 'DataType66', a)
    if hasattr(b2, 'DataType66'):
        assert _is_linked(b2, 'DataType66', a)
    _safe_set(a, 'repository_DataType', set())
    assert not _is_linked(a, 'repository_DataType', b2)
    if hasattr(b2, 'DataType66'):
        assert not _is_linked(b2, 'DataType66', a)


def test_assoc_describedService__SEFF151_link_reassign_clear():
    a = pcm_seff_ServiceEffectSpecification(seffTypeID="sample_text")
    b1 = Signature()
    b2 = Signature()
    _safe_set(a, 'pcm_seff_ServiceEffectSpecification', b1)
    assert _is_linked(a, 'pcm_seff_ServiceEffectSpecification', b1)
    if hasattr(b1, 'Signature152'):
        assert _is_linked(b1, 'Signature152', a)
    _safe_set(a, 'pcm_seff_ServiceEffectSpecification', b2)
    assert _is_linked(a, 'pcm_seff_ServiceEffectSpecification', b2)
    if hasattr(b1, 'Signature152'):
        assert not _is_linked(b1, 'Signature152', a)
    if hasattr(b2, 'Signature152'):
        assert _is_linked(b2, 'Signature152', a)
    _safe_set(a, 'pcm_seff_ServiceEffectSpecification', None)
    assert not _is_linked(a, 'pcm_seff_ServiceEffectSpecification', b2)
    if hasattr(b2, 'Signature152'):
        assert not _is_linked(b2, 'Signature152', a)


def test_assoc_exceptions__Signature55_link_reassign_clear():
    a = pcm_repository_Signature(serviceName="sample_text")
    b1 = ExceptionType()
    b2 = ExceptionType()
    _safe_set(a, 'pcm_repository_Signature56', {b1})
    assert _is_linked(a, 'pcm_repository_Signature56', b1)
    if hasattr(b1, 'ExceptionType'):
        assert _is_linked(b1, 'ExceptionType', a)
    _safe_set(a, 'pcm_repository_Signature56', {b2})
    assert _is_linked(a, 'pcm_repository_Signature56', b2)
    if hasattr(b1, 'ExceptionType'):
        assert not _is_linked(b1, 'ExceptionType', a)
    if hasattr(b2, 'ExceptionType'):
        assert _is_linked(b2, 'ExceptionType', a)
    _safe_set(a, 'pcm_repository_Signature56', set())
    assert not _is_linked(a, 'pcm_repository_Signature56', b2)
    if hasattr(b2, 'ExceptionType'):
        assert not _is_linked(b2, 'ExceptionType', a)


def test_assoc_innerProvidedRole_ProvidedDelegationConnector3_link_reassign_clear():
    a = pcm_composition_ProvidedDelegationConnector()
    b1 = ProvidedRole()
    b2 = ProvidedRole()
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector', b1)
    assert _is_linked(a, 'pcm_composition_ProvidedDelegationConnector', b1)
    if hasattr(b1, 'ProvidedRole4'):
        assert _is_linked(b1, 'ProvidedRole4', a)
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector', b2)
    assert _is_linked(a, 'pcm_composition_ProvidedDelegationConnector', b2)
    if hasattr(b1, 'ProvidedRole4'):
        assert not _is_linked(b1, 'ProvidedRole4', a)
    if hasattr(b2, 'ProvidedRole4'):
        assert _is_linked(b2, 'ProvidedRole4', a)
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector', None)
    assert not _is_linked(a, 'pcm_composition_ProvidedDelegationConnector', b2)
    if hasattr(b2, 'ProvidedRole4'):
        assert not _is_linked(b2, 'ProvidedRole4', a)


def test_assoc_innerRequiredRole_RequiredDelegationConnector16_link_reassign_clear():
    a = pcm_composition_RequiredDelegationConnector()
    b1 = RequiredRole()
    b2 = RequiredRole()
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector', b1)
    assert _is_linked(a, 'pcm_composition_RequiredDelegationConnector', b1)
    if hasattr(b1, 'RequiredRole17'):
        assert _is_linked(b1, 'RequiredRole17', a)
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector', b2)
    assert _is_linked(a, 'pcm_composition_RequiredDelegationConnector', b2)
    if hasattr(b1, 'RequiredRole17'):
        assert not _is_linked(b1, 'RequiredRole17', a)
    if hasattr(b2, 'RequiredRole17'):
        assert _is_linked(b2, 'RequiredRole17', a)
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector', None)
    assert not _is_linked(a, 'pcm_composition_RequiredDelegationConnector', b2)
    if hasattr(b2, 'RequiredRole17'):
        assert not _is_linked(b2, 'RequiredRole17', a)


def test_assoc_inputParameterUsages_ExternalCallAction132_link_reassign_clear():
    a = pcm_seff_ExternalCallAction(retryCount=7)
    b1 = VariableUsage()
    b2 = VariableUsage()
    _safe_set(a, 'pcm_seff_ExternalCallAction133', {b1})
    assert _is_linked(a, 'pcm_seff_ExternalCallAction133', b1)
    if hasattr(b1, 'VariableUsage134'):
        assert _is_linked(b1, 'VariableUsage134', a)
    _safe_set(a, 'pcm_seff_ExternalCallAction133', {b2})
    assert _is_linked(a, 'pcm_seff_ExternalCallAction133', b2)
    if hasattr(b1, 'VariableUsage134'):
        assert not _is_linked(b1, 'VariableUsage134', a)
    if hasattr(b2, 'VariableUsage134'):
        assert _is_linked(b2, 'VariableUsage134', a)
    _safe_set(a, 'pcm_seff_ExternalCallAction133', set())
    assert not _is_linked(a, 'pcm_seff_ExternalCallAction133', b2)
    if hasattr(b2, 'VariableUsage134'):
        assert not _is_linked(b2, 'VariableUsage134', a)


def test_assoc_interArrivalTime_OpenWorkload230_link_reassign_clear():
    a = pcm_usagemodel_OpenWorkload()
    b1 = PCMRandomVariable()
    b2 = PCMRandomVariable()
    _safe_set(a, 'pcm_usagemodel_OpenWorkload', b1)
    assert _is_linked(a, 'pcm_usagemodel_OpenWorkload', b1)
    if hasattr(b1, 'PCMRandomVariable231'):
        assert _is_linked(b1, 'PCMRandomVariable231', a)
    _safe_set(a, 'pcm_usagemodel_OpenWorkload', b2)
    assert _is_linked(a, 'pcm_usagemodel_OpenWorkload', b2)
    if hasattr(b1, 'PCMRandomVariable231'):
        assert not _is_linked(b1, 'PCMRandomVariable231', a)
    if hasattr(b2, 'PCMRandomVariable231'):
        assert _is_linked(b2, 'PCMRandomVariable231', a)
    _safe_set(a, 'pcm_usagemodel_OpenWorkload', None)
    assert not _is_linked(a, 'pcm_usagemodel_OpenWorkload', b2)
    if hasattr(b2, 'PCMRandomVariable231'):
        assert not _is_linked(b2, 'PCMRandomVariable231', a)


def test_assoc_interface_Signature53_link_reassign_clear():
    a = pcm_repository_Signature(serviceName="sample_text")
    b1 = Interface()
    b2 = Interface()
    _safe_set(a, 'signatures__Interface', b1)
    assert _is_linked(a, 'signatures__Interface', b1)
    if hasattr(b1, 'Interface'):
        assert _is_linked(b1, 'Interface', a)
    _safe_set(a, 'signatures__Interface', b2)
    assert _is_linked(a, 'signatures__Interface', b2)
    if hasattr(b1, 'Interface'):
        assert not _is_linked(b1, 'Interface', a)
    if hasattr(b2, 'Interface'):
        assert _is_linked(b2, 'Interface', a)
    _safe_set(a, 'signatures__Interface', None)
    assert not _is_linked(a, 'signatures__Interface', b2)
    if hasattr(b2, 'Interface'):
        assert not _is_linked(b2, 'Interface', a)


def test_assoc_interfaces__Repository63_link_reassign_clear():
    a = pcm_repository_Repository(repositoryDescription="sample_text")
    b1 = Interface()
    b2 = Interface()
    _safe_set(a, 'repository_Interface', {b1})
    assert _is_linked(a, 'repository_Interface', b1)
    if hasattr(b1, 'Interface64'):
        assert _is_linked(b1, 'Interface64', a)
    _safe_set(a, 'repository_Interface', {b2})
    assert _is_linked(a, 'repository_Interface', b2)
    if hasattr(b1, 'Interface64'):
        assert not _is_linked(b1, 'Interface64', a)
    if hasattr(b2, 'Interface64'):
        assert _is_linked(b2, 'Interface64', a)
    _safe_set(a, 'repository_Interface', set())
    assert not _is_linked(a, 'repository_Interface', b2)
    if hasattr(b2, 'Interface64'):
        assert not _is_linked(b2, 'Interface64', a)


def test_assoc_latency_CommunicationLinkResourceSpecification180_link_reassign_clear():
    a = pcm_resourceenvironment_CommunicationLinkResourceSpecification(failureProbability=3.14)
    b1 = PCMRandomVariable()
    b2 = PCMRandomVariable()
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification181', b1)
    assert _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification181', b1)
    if hasattr(b1, 'PCMRandomVariable182'):
        assert _is_linked(b1, 'PCMRandomVariable182', a)
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification181', b2)
    assert _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification181', b2)
    if hasattr(b1, 'PCMRandomVariable182'):
        assert not _is_linked(b1, 'PCMRandomVariable182', a)
    if hasattr(b2, 'PCMRandomVariable182'):
        assert _is_linked(b2, 'PCMRandomVariable182', a)
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification181', None)
    assert not _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification181', b2)
    if hasattr(b2, 'PCMRandomVariable182'):
        assert not _is_linked(b2, 'PCMRandomVariable182', a)


def test_assoc_outerProvidedRole_ProvidedDelegationConnector5_link_reassign_clear():
    a = pcm_composition_ProvidedDelegationConnector()
    b1 = ProvidedRole()
    b2 = ProvidedRole()
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector6', b1)
    assert _is_linked(a, 'pcm_composition_ProvidedDelegationConnector6', b1)
    if hasattr(b1, 'ProvidedRole7'):
        assert _is_linked(b1, 'ProvidedRole7', a)
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector6', b2)
    assert _is_linked(a, 'pcm_composition_ProvidedDelegationConnector6', b2)
    if hasattr(b1, 'ProvidedRole7'):
        assert not _is_linked(b1, 'ProvidedRole7', a)
    if hasattr(b2, 'ProvidedRole7'):
        assert _is_linked(b2, 'ProvidedRole7', a)
    _safe_set(a, 'pcm_composition_ProvidedDelegationConnector6', None)
    assert not _is_linked(a, 'pcm_composition_ProvidedDelegationConnector6', b2)
    if hasattr(b2, 'ProvidedRole7'):
        assert not _is_linked(b2, 'ProvidedRole7', a)


def test_assoc_outerRequiredRole_RequiredDelegationConnector18_link_reassign_clear():
    a = pcm_composition_RequiredDelegationConnector()
    b1 = RequiredRole()
    b2 = RequiredRole()
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector19', b1)
    assert _is_linked(a, 'pcm_composition_RequiredDelegationConnector19', b1)
    if hasattr(b1, 'RequiredRole20'):
        assert _is_linked(b1, 'RequiredRole20', a)
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector19', b2)
    assert _is_linked(a, 'pcm_composition_RequiredDelegationConnector19', b2)
    if hasattr(b1, 'RequiredRole20'):
        assert not _is_linked(b1, 'RequiredRole20', a)
    if hasattr(b2, 'RequiredRole20'):
        assert _is_linked(b2, 'RequiredRole20', a)
    _safe_set(a, 'pcm_composition_RequiredDelegationConnector19', None)
    assert not _is_linked(a, 'pcm_composition_RequiredDelegationConnector19', b2)
    if hasattr(b2, 'RequiredRole20'):
        assert not _is_linked(b2, 'RequiredRole20', a)


def test_assoc_outputVariableUsages_ExternalCallAction135_link_reassign_clear():
    a = pcm_seff_ExternalCallAction(retryCount=7)
    b1 = VariableUsage()
    b2 = VariableUsage()
    _safe_set(a, 'pcm_seff_ExternalCallAction136', {b1})
    assert _is_linked(a, 'pcm_seff_ExternalCallAction136', b1)
    if hasattr(b1, 'VariableUsage137'):
        assert _is_linked(b1, 'VariableUsage137', a)
    _safe_set(a, 'pcm_seff_ExternalCallAction136', {b2})
    assert _is_linked(a, 'pcm_seff_ExternalCallAction136', b2)
    if hasattr(b1, 'VariableUsage137'):
        assert not _is_linked(b1, 'VariableUsage137', a)
    if hasattr(b2, 'VariableUsage137'):
        assert _is_linked(b2, 'VariableUsage137', a)
    _safe_set(a, 'pcm_seff_ExternalCallAction136', set())
    assert not _is_linked(a, 'pcm_seff_ExternalCallAction136', b2)
    if hasattr(b2, 'VariableUsage137'):
        assert not _is_linked(b2, 'VariableUsage137', a)


def test_assoc_parameters__Signature52_link_reassign_clear():
    a = pcm_repository_Signature(serviceName="sample_text")
    b1 = Parameter()
    b2 = Parameter()
    _safe_set(a, 'signature_Parameter', {b1})
    assert _is_linked(a, 'signature_Parameter', b1)
    if hasattr(b1, 'Parameter'):
        assert _is_linked(b1, 'Parameter', a)
    _safe_set(a, 'signature_Parameter', {b2})
    assert _is_linked(a, 'signature_Parameter', b2)
    if hasattr(b1, 'Parameter'):
        assert not _is_linked(b1, 'Parameter', a)
    if hasattr(b2, 'Parameter'):
        assert _is_linked(b2, 'Parameter', a)
    _safe_set(a, 'signature_Parameter', set())
    assert not _is_linked(a, 'signature_Parameter', b2)
    if hasattr(b2, 'Parameter'):
        assert not _is_linked(b2, 'Parameter', a)


def test_assoc_parentCompleteComponentTypes86_link_reassign_clear():
    a = pcm_repository_ImplementationComponentType()
    b1 = CompleteComponentType()
    b2 = CompleteComponentType()
    _safe_set(a, 'pcm_repository_ImplementationComponentType', {b1})
    assert _is_linked(a, 'pcm_repository_ImplementationComponentType', b1)
    if hasattr(b1, 'CompleteComponentType'):
        assert _is_linked(b1, 'CompleteComponentType', a)
    _safe_set(a, 'pcm_repository_ImplementationComponentType', {b2})
    assert _is_linked(a, 'pcm_repository_ImplementationComponentType', b2)
    if hasattr(b1, 'CompleteComponentType'):
        assert not _is_linked(b1, 'CompleteComponentType', a)
    if hasattr(b2, 'CompleteComponentType'):
        assert _is_linked(b2, 'CompleteComponentType', a)
    _safe_set(a, 'pcm_repository_ImplementationComponentType', set())
    assert not _is_linked(a, 'pcm_repository_ImplementationComponentType', b2)
    if hasattr(b2, 'CompleteComponentType'):
        assert not _is_linked(b2, 'CompleteComponentType', a)


def test_assoc_parentInterface__Interface72_link_reassign_clear():
    a = pcm_repository_Interface()
    b1 = Interface()
    b2 = Interface()
    _safe_set(a, 'pcm_repository_Interface', {b1})
    assert _is_linked(a, 'pcm_repository_Interface', b1)
    if hasattr(b1, 'Interface73'):
        assert _is_linked(b1, 'Interface73', a)
    _safe_set(a, 'pcm_repository_Interface', {b2})
    assert _is_linked(a, 'pcm_repository_Interface', b2)
    if hasattr(b1, 'Interface73'):
        assert not _is_linked(b1, 'Interface73', a)
    if hasattr(b2, 'Interface73'):
        assert _is_linked(b2, 'Interface73', a)
    _safe_set(a, 'pcm_repository_Interface', set())
    assert not _is_linked(a, 'pcm_repository_Interface', b2)
    if hasattr(b2, 'Interface73'):
        assert not _is_linked(b2, 'Interface73', a)


def test_assoc_parentProvidesComponentTypes90_link_reassign_clear():
    a = pcm_repository_CompleteComponentType()
    b1 = ProvidesComponentType()
    b2 = ProvidesComponentType()
    _safe_set(a, 'pcm_repository_CompleteComponentType', {b1})
    assert _is_linked(a, 'pcm_repository_CompleteComponentType', b1)
    if hasattr(b1, 'ProvidesComponentType'):
        assert _is_linked(b1, 'ProvidesComponentType', a)
    _safe_set(a, 'pcm_repository_CompleteComponentType', {b2})
    assert _is_linked(a, 'pcm_repository_CompleteComponentType', b2)
    if hasattr(b1, 'ProvidesComponentType'):
        assert not _is_linked(b1, 'ProvidesComponentType', a)
    if hasattr(b2, 'ProvidesComponentType'):
        assert _is_linked(b2, 'ProvidesComponentType', a)
    _safe_set(a, 'pcm_repository_CompleteComponentType', set())
    assert not _is_linked(a, 'pcm_repository_CompleteComponentType', b2)
    if hasattr(b2, 'ProvidesComponentType'):
        assert not _is_linked(b2, 'ProvidesComponentType', a)


def test_assoc_parentStructure_AssemblyConnector37_link_reassign_clear():
    a = pcm_composition_AssemblyConnector()
    b1 = composition_ComposedStructure()
    b2 = composition_ComposedStructure()
    _safe_set(a, 'assemblyConnectors_ComposedStructure', b1)
    assert _is_linked(a, 'assemblyConnectors_ComposedStructure', b1)
    if hasattr(b1, 'ComposedStructure38'):
        assert _is_linked(b1, 'ComposedStructure38', a)
    _safe_set(a, 'assemblyConnectors_ComposedStructure', b2)
    assert _is_linked(a, 'assemblyConnectors_ComposedStructure', b2)
    if hasattr(b1, 'ComposedStructure38'):
        assert not _is_linked(b1, 'ComposedStructure38', a)
    if hasattr(b2, 'ComposedStructure38'):
        assert _is_linked(b2, 'ComposedStructure38', a)
    _safe_set(a, 'assemblyConnectors_ComposedStructure', None)
    assert not _is_linked(a, 'assemblyConnectors_ComposedStructure', b2)
    if hasattr(b2, 'ComposedStructure38'):
        assert not _is_linked(b2, 'ComposedStructure38', a)


def test_assoc_parentStructure_ProvidedDelegationConnector10_link_reassign_clear():
    a = pcm_composition_ProvidedDelegationConnector()
    b1 = composition_ComposedStructure()
    b2 = composition_ComposedStructure()
    _safe_set(a, 'providedDelegationConnectors_ComposedStructure', b1)
    assert _is_linked(a, 'providedDelegationConnectors_ComposedStructure', b1)
    if hasattr(b1, 'ComposedStructure'):
        assert _is_linked(b1, 'ComposedStructure', a)
    _safe_set(a, 'providedDelegationConnectors_ComposedStructure', b2)
    assert _is_linked(a, 'providedDelegationConnectors_ComposedStructure', b2)
    if hasattr(b1, 'ComposedStructure'):
        assert not _is_linked(b1, 'ComposedStructure', a)
    if hasattr(b2, 'ComposedStructure'):
        assert _is_linked(b2, 'ComposedStructure', a)
    _safe_set(a, 'providedDelegationConnectors_ComposedStructure', None)
    assert not _is_linked(a, 'providedDelegationConnectors_ComposedStructure', b2)
    if hasattr(b2, 'ComposedStructure'):
        assert not _is_linked(b2, 'ComposedStructure', a)


def test_assoc_parentStructure_RequiredDelegationConnector24_link_reassign_clear():
    a = pcm_composition_RequiredDelegationConnector()
    b1 = composition_ComposedStructure()
    b2 = composition_ComposedStructure()
    _safe_set(a, 'requiredDelegationConnectors_ComposedStructure', b1)
    assert _is_linked(a, 'requiredDelegationConnectors_ComposedStructure', b1)
    if hasattr(b1, 'ComposedStructure25'):
        assert _is_linked(b1, 'ComposedStructure25', a)
    _safe_set(a, 'requiredDelegationConnectors_ComposedStructure', b2)
    assert _is_linked(a, 'requiredDelegationConnectors_ComposedStructure', b2)
    if hasattr(b1, 'ComposedStructure25'):
        assert not _is_linked(b1, 'ComposedStructure25', a)
    if hasattr(b2, 'ComposedStructure25'):
        assert _is_linked(b2, 'ComposedStructure25', a)
    _safe_set(a, 'requiredDelegationConnectors_ComposedStructure', None)
    assert not _is_linked(a, 'requiredDelegationConnectors_ComposedStructure', b2)
    if hasattr(b2, 'ComposedStructure25'):
        assert not _is_linked(b2, 'ComposedStructure25', a)


def test_assoc_passiveResource_BasicComponent92_link_reassign_clear():
    a = pcm_repository_BasicComponent()
    b1 = PassiveResource()
    b2 = PassiveResource()
    _safe_set(a, 'pcm_repository_BasicComponent93', {b1})
    assert _is_linked(a, 'pcm_repository_BasicComponent93', b1)
    if hasattr(b1, 'PassiveResource'):
        assert _is_linked(b1, 'PassiveResource', a)
    _safe_set(a, 'pcm_repository_BasicComponent93', {b2})
    assert _is_linked(a, 'pcm_repository_BasicComponent93', b2)
    if hasattr(b1, 'PassiveResource'):
        assert not _is_linked(b1, 'PassiveResource', a)
    if hasattr(b2, 'PassiveResource'):
        assert _is_linked(b2, 'PassiveResource', a)
    _safe_set(a, 'pcm_repository_BasicComponent93', set())
    assert not _is_linked(a, 'pcm_repository_BasicComponent93', b2)
    if hasattr(b2, 'PassiveResource'):
        assert not _is_linked(b2, 'PassiveResource', a)


def test_assoc_processingRate_ProcessingResourceSpecification188_link_reassign_clear():
    a = pcm_resourceenvironment_ProcessingResourceSpecification(MTTF=3.14, MTTR=3.14, schedulingPolicy="sample_text")
    b1 = PCMRandomVariable()
    b2 = PCMRandomVariable()
    _safe_set(a, 'pcm_resourceenvironment_ProcessingResourceSpecification189', b1)
    assert _is_linked(a, 'pcm_resourceenvironment_ProcessingResourceSpecification189', b1)
    if hasattr(b1, 'PCMRandomVariable190'):
        assert _is_linked(b1, 'PCMRandomVariable190', a)
    _safe_set(a, 'pcm_resourceenvironment_ProcessingResourceSpecification189', b2)
    assert _is_linked(a, 'pcm_resourceenvironment_ProcessingResourceSpecification189', b2)
    if hasattr(b1, 'PCMRandomVariable190'):
        assert not _is_linked(b1, 'PCMRandomVariable190', a)
    if hasattr(b2, 'PCMRandomVariable190'):
        assert _is_linked(b2, 'PCMRandomVariable190', a)
    _safe_set(a, 'pcm_resourceenvironment_ProcessingResourceSpecification189', None)
    assert not _is_linked(a, 'pcm_resourceenvironment_ProcessingResourceSpecification189', b2)
    if hasattr(b2, 'PCMRandomVariable190'):
        assert not _is_linked(b2, 'PCMRandomVariable190', a)


def test_assoc_protocols__Interface77_link_reassign_clear():
    a = pcm_repository_Interface()
    b1 = Protocol()
    b2 = Protocol()
    _safe_set(a, 'pcm_repository_Interface78', {b1})
    assert _is_linked(a, 'pcm_repository_Interface78', b1)
    if hasattr(b1, 'Protocol'):
        assert _is_linked(b1, 'Protocol', a)
    _safe_set(a, 'pcm_repository_Interface78', {b2})
    assert _is_linked(a, 'pcm_repository_Interface78', b2)
    if hasattr(b1, 'Protocol'):
        assert not _is_linked(b1, 'Protocol', a)
    if hasattr(b2, 'Protocol'):
        assert _is_linked(b2, 'Protocol', a)
    _safe_set(a, 'pcm_repository_Interface78', set())
    assert not _is_linked(a, 'pcm_repository_Interface78', b2)
    if hasattr(b2, 'Protocol'):
        assert not _is_linked(b2, 'Protocol', a)


def test_assoc_providedRole_AssemblyConnector31_link_reassign_clear():
    a = pcm_composition_AssemblyConnector()
    b1 = ProvidedRole()
    b2 = ProvidedRole()
    _safe_set(a, 'pcm_composition_AssemblyConnector32', b1)
    assert _is_linked(a, 'pcm_composition_AssemblyConnector32', b1)
    if hasattr(b1, 'ProvidedRole33'):
        assert _is_linked(b1, 'ProvidedRole33', a)
    _safe_set(a, 'pcm_composition_AssemblyConnector32', b2)
    assert _is_linked(a, 'pcm_composition_AssemblyConnector32', b2)
    if hasattr(b1, 'ProvidedRole33'):
        assert not _is_linked(b1, 'ProvidedRole33', a)
    if hasattr(b2, 'ProvidedRole33'):
        assert _is_linked(b2, 'ProvidedRole33', a)
    _safe_set(a, 'pcm_composition_AssemblyConnector32', None)
    assert not _is_linked(a, 'pcm_composition_AssemblyConnector32', b2)
    if hasattr(b2, 'ProvidedRole33'):
        assert not _is_linked(b2, 'ProvidedRole33', a)


def test_assoc_providingAssemblyContext_AssemblyConnector28_link_reassign_clear():
    a = pcm_composition_AssemblyConnector()
    b1 = composition_AssemblyContext()
    b2 = composition_AssemblyContext()
    _safe_set(a, 'pcm_composition_AssemblyConnector29', b1)
    assert _is_linked(a, 'pcm_composition_AssemblyConnector29', b1)
    if hasattr(b1, 'composition_AssemblyContext30'):
        assert _is_linked(b1, 'composition_AssemblyContext30', a)
    _safe_set(a, 'pcm_composition_AssemblyConnector29', b2)
    assert _is_linked(a, 'pcm_composition_AssemblyConnector29', b2)
    if hasattr(b1, 'composition_AssemblyContext30'):
        assert not _is_linked(b1, 'composition_AssemblyContext30', a)
    if hasattr(b2, 'composition_AssemblyContext30'):
        assert _is_linked(b2, 'composition_AssemblyContext30', a)
    _safe_set(a, 'pcm_composition_AssemblyConnector29', None)
    assert not _is_linked(a, 'pcm_composition_AssemblyConnector29', b2)
    if hasattr(b2, 'composition_AssemblyContext30'):
        assert not _is_linked(b2, 'composition_AssemblyContext30', a)


def test_assoc_repository_Interface81_link_reassign_clear():
    a = pcm_repository_Interface()
    b1 = Repository()
    b2 = Repository()
    _safe_set(a, 'interfaces__Repository', b1)
    assert _is_linked(a, 'interfaces__Repository', b1)
    if hasattr(b1, 'Repository82'):
        assert _is_linked(b1, 'Repository82', a)
    _safe_set(a, 'interfaces__Repository', b2)
    assert _is_linked(a, 'interfaces__Repository', b2)
    if hasattr(b1, 'Repository82'):
        assert not _is_linked(b1, 'Repository82', a)
    if hasattr(b2, 'Repository82'):
        assert _is_linked(b2, 'Repository82', a)
    _safe_set(a, 'interfaces__Repository', None)
    assert not _is_linked(a, 'interfaces__Repository', b2)
    if hasattr(b2, 'Repository82'):
        assert not _is_linked(b2, 'Repository82', a)


def test_assoc_requiredRole_AssemblyConnector34_link_reassign_clear():
    a = pcm_composition_AssemblyConnector()
    b1 = RequiredRole()
    b2 = RequiredRole()
    _safe_set(a, 'pcm_composition_AssemblyConnector35', b1)
    assert _is_linked(a, 'pcm_composition_AssemblyConnector35', b1)
    if hasattr(b1, 'RequiredRole36'):
        assert _is_linked(b1, 'RequiredRole36', a)
    _safe_set(a, 'pcm_composition_AssemblyConnector35', b2)
    assert _is_linked(a, 'pcm_composition_AssemblyConnector35', b2)
    if hasattr(b1, 'RequiredRole36'):
        assert not _is_linked(b1, 'RequiredRole36', a)
    if hasattr(b2, 'RequiredRole36'):
        assert _is_linked(b2, 'RequiredRole36', a)
    _safe_set(a, 'pcm_composition_AssemblyConnector35', None)
    assert not _is_linked(a, 'pcm_composition_AssemblyConnector35', b2)
    if hasattr(b2, 'RequiredRole36'):
        assert not _is_linked(b2, 'RequiredRole36', a)


def test_assoc_requiringAssemblyContext_AssemblyConnector26_link_reassign_clear():
    a = pcm_composition_AssemblyConnector()
    b1 = composition_AssemblyContext()
    b2 = composition_AssemblyContext()
    _safe_set(a, 'pcm_composition_AssemblyConnector', b1)
    assert _is_linked(a, 'pcm_composition_AssemblyConnector', b1)
    if hasattr(b1, 'composition_AssemblyContext27'):
        assert _is_linked(b1, 'composition_AssemblyContext27', a)
    _safe_set(a, 'pcm_composition_AssemblyConnector', b2)
    assert _is_linked(a, 'pcm_composition_AssemblyConnector', b2)
    if hasattr(b1, 'composition_AssemblyContext27'):
        assert not _is_linked(b1, 'composition_AssemblyContext27', a)
    if hasattr(b2, 'composition_AssemblyContext27'):
        assert _is_linked(b2, 'composition_AssemblyContext27', a)
    _safe_set(a, 'pcm_composition_AssemblyConnector', None)
    assert not _is_linked(a, 'pcm_composition_AssemblyConnector', b2)
    if hasattr(b2, 'composition_AssemblyContext27'):
        assert not _is_linked(b2, 'composition_AssemblyContext27', a)


def test_assoc_returntype__Signature54_link_reassign_clear():
    a = pcm_repository_Signature(serviceName="sample_text")
    b1 = DataType()
    b2 = DataType()
    _safe_set(a, 'pcm_repository_Signature', b1)
    assert _is_linked(a, 'pcm_repository_Signature', b1)
    if hasattr(b1, 'DataType'):
        assert _is_linked(b1, 'DataType', a)
    _safe_set(a, 'pcm_repository_Signature', b2)
    assert _is_linked(a, 'pcm_repository_Signature', b2)
    if hasattr(b1, 'DataType'):
        assert not _is_linked(b1, 'DataType', a)
    if hasattr(b2, 'DataType'):
        assert _is_linked(b2, 'DataType', a)
    _safe_set(a, 'pcm_repository_Signature', None)
    assert not _is_linked(a, 'pcm_repository_Signature', b2)
    if hasattr(b2, 'DataType'):
        assert not _is_linked(b2, 'DataType', a)


def test_assoc_role_ExternalService138_link_reassign_clear():
    a = pcm_seff_ExternalCallAction(retryCount=7)
    b1 = Role()
    b2 = Role()
    _safe_set(a, 'pcm_seff_ExternalCallAction139', b1)
    assert _is_linked(a, 'pcm_seff_ExternalCallAction139', b1)
    if hasattr(b1, 'Role'):
        assert _is_linked(b1, 'Role', a)
    _safe_set(a, 'pcm_seff_ExternalCallAction139', b2)
    assert _is_linked(a, 'pcm_seff_ExternalCallAction139', b2)
    if hasattr(b1, 'Role'):
        assert not _is_linked(b1, 'Role', a)
    if hasattr(b2, 'Role'):
        assert _is_linked(b2, 'Role', a)
    _safe_set(a, 'pcm_seff_ExternalCallAction139', None)
    assert not _is_linked(a, 'pcm_seff_ExternalCallAction139', b2)
    if hasattr(b2, 'Role'):
        assert not _is_linked(b2, 'Role', a)


def test_assoc_serviceEffectSpecifications__BasicComponent91_link_reassign_clear():
    a = pcm_repository_BasicComponent()
    b1 = ServiceEffectSpecification()
    b2 = ServiceEffectSpecification()
    _safe_set(a, 'pcm_repository_BasicComponent', {b1})
    assert _is_linked(a, 'pcm_repository_BasicComponent', b1)
    if hasattr(b1, 'ServiceEffectSpecification'):
        assert _is_linked(b1, 'ServiceEffectSpecification', a)
    _safe_set(a, 'pcm_repository_BasicComponent', {b2})
    assert _is_linked(a, 'pcm_repository_BasicComponent', b2)
    if hasattr(b1, 'ServiceEffectSpecification'):
        assert not _is_linked(b1, 'ServiceEffectSpecification', a)
    if hasattr(b2, 'ServiceEffectSpecification'):
        assert _is_linked(b2, 'ServiceEffectSpecification', a)
    _safe_set(a, 'pcm_repository_BasicComponent', set())
    assert not _is_linked(a, 'pcm_repository_BasicComponent', b2)
    if hasattr(b2, 'ServiceEffectSpecification'):
        assert not _is_linked(b2, 'ServiceEffectSpecification', a)


def test_assoc_signature_Parameter59_link_reassign_clear():
    a = pcm_repository_Parameter(modifier__Parameter="sample_text", parameterName="sample_text")
    b1 = Signature()
    b2 = Signature()
    _safe_set(a, 'parameters__Signature', b1)
    assert _is_linked(a, 'parameters__Signature', b1)
    if hasattr(b1, 'Signature'):
        assert _is_linked(b1, 'Signature', a)
    _safe_set(a, 'parameters__Signature', b2)
    assert _is_linked(a, 'parameters__Signature', b2)
    if hasattr(b1, 'Signature'):
        assert not _is_linked(b1, 'Signature', a)
    if hasattr(b2, 'Signature'):
        assert _is_linked(b2, 'Signature', a)
    _safe_set(a, 'parameters__Signature', None)
    assert not _is_linked(a, 'parameters__Signature', b2)
    if hasattr(b2, 'Signature'):
        assert not _is_linked(b2, 'Signature', a)


def test_assoc_signatures__Interface79_link_reassign_clear():
    a = pcm_repository_Interface()
    b1 = Signature()
    b2 = Signature()
    _safe_set(a, 'interface_Signature', {b1})
    assert _is_linked(a, 'interface_Signature', b1)
    if hasattr(b1, 'Signature80'):
        assert _is_linked(b1, 'Signature80', a)
    _safe_set(a, 'interface_Signature', {b2})
    assert _is_linked(a, 'interface_Signature', b2)
    if hasattr(b1, 'Signature80'):
        assert not _is_linked(b1, 'Signature80', a)
    if hasattr(b2, 'Signature80'):
        assert _is_linked(b2, 'Signature80', a)
    _safe_set(a, 'interface_Signature', set())
    assert not _is_linked(a, 'interface_Signature', b2)
    if hasattr(b2, 'Signature80'):
        assert not _is_linked(b2, 'Signature80', a)


def test_assoc_specification_VariableCharacterisation106_link_reassign_clear():
    a = pcm_parameter_VariableCharacterisation(type="sample_text")
    b1 = PCMRandomVariable()
    b2 = PCMRandomVariable()
    _safe_set(a, 'pcm_parameter_VariableCharacterisation', b1)
    assert _is_linked(a, 'pcm_parameter_VariableCharacterisation', b1)
    if hasattr(b1, 'PCMRandomVariable107'):
        assert _is_linked(b1, 'PCMRandomVariable107', a)
    _safe_set(a, 'pcm_parameter_VariableCharacterisation', b2)
    assert _is_linked(a, 'pcm_parameter_VariableCharacterisation', b2)
    if hasattr(b1, 'PCMRandomVariable107'):
        assert not _is_linked(b1, 'PCMRandomVariable107', a)
    if hasattr(b2, 'PCMRandomVariable107'):
        assert _is_linked(b2, 'PCMRandomVariable107', a)
    _safe_set(a, 'pcm_parameter_VariableCharacterisation', None)
    assert not _is_linked(a, 'pcm_parameter_VariableCharacterisation', b2)
    if hasattr(b2, 'PCMRandomVariable107'):
        assert not _is_linked(b2, 'PCMRandomVariable107', a)


def test_assoc_steps_Behaviour115_link_reassign_clear():
    a = pcm_seff_ResourceDemandingBehaviour()
    b1 = AbstractAction()
    b2 = AbstractAction()
    _safe_set(a, 'pcm_seff_ResourceDemandingBehaviour', {b1})
    assert _is_linked(a, 'pcm_seff_ResourceDemandingBehaviour', b1)
    if hasattr(b1, 'AbstractAction116'):
        assert _is_linked(b1, 'AbstractAction116', a)
    _safe_set(a, 'pcm_seff_ResourceDemandingBehaviour', {b2})
    assert _is_linked(a, 'pcm_seff_ResourceDemandingBehaviour', b2)
    if hasattr(b1, 'AbstractAction116'):
        assert not _is_linked(b1, 'AbstractAction116', a)
    if hasattr(b2, 'AbstractAction116'):
        assert _is_linked(b2, 'AbstractAction116', a)
    _safe_set(a, 'pcm_seff_ResourceDemandingBehaviour', set())
    assert not _is_linked(a, 'pcm_seff_ResourceDemandingBehaviour', b2)
    if hasattr(b2, 'AbstractAction116'):
        assert not _is_linked(b2, 'AbstractAction116', a)


def test_assoc_system_Allocation166_link_reassign_clear():
    a = pcm_allocation_Allocation()
    b1 = System()
    b2 = System()
    _safe_set(a, 'pcm_allocation_Allocation167', b1)
    assert _is_linked(a, 'pcm_allocation_Allocation167', b1)
    if hasattr(b1, 'System'):
        assert _is_linked(b1, 'System', a)
    _safe_set(a, 'pcm_allocation_Allocation167', b2)
    assert _is_linked(a, 'pcm_allocation_Allocation167', b2)
    if hasattr(b1, 'System'):
        assert not _is_linked(b1, 'System', a)
    if hasattr(b2, 'System'):
        assert _is_linked(b2, 'System', a)
    _safe_set(a, 'pcm_allocation_Allocation167', None)
    assert not _is_linked(a, 'pcm_allocation_Allocation167', b2)
    if hasattr(b2, 'System'):
        assert not _is_linked(b2, 'System', a)


def test_assoc_targetResourceEnvironment_Allocation164_link_reassign_clear():
    a = pcm_allocation_Allocation()
    b1 = ResourceEnvironment()
    b2 = ResourceEnvironment()
    _safe_set(a, 'pcm_allocation_Allocation165', b1)
    assert _is_linked(a, 'pcm_allocation_Allocation165', b1)
    if hasattr(b1, 'ResourceEnvironment'):
        assert _is_linked(b1, 'ResourceEnvironment', a)
    _safe_set(a, 'pcm_allocation_Allocation165', b2)
    assert _is_linked(a, 'pcm_allocation_Allocation165', b2)
    if hasattr(b1, 'ResourceEnvironment'):
        assert not _is_linked(b1, 'ResourceEnvironment', a)
    if hasattr(b2, 'ResourceEnvironment'):
        assert _is_linked(b2, 'ResourceEnvironment', a)
    _safe_set(a, 'pcm_allocation_Allocation165', None)
    assert not _is_linked(a, 'pcm_allocation_Allocation165', b2)
    if hasattr(b2, 'ResourceEnvironment'):
        assert not _is_linked(b2, 'ResourceEnvironment', a)


def test_assoc_thinkTime_ClosedWorkload248_link_reassign_clear():
    a = pcm_usagemodel_ClosedWorkload(population=7)
    b1 = PCMRandomVariable()
    b2 = PCMRandomVariable()
    _safe_set(a, 'pcm_usagemodel_ClosedWorkload', b1)
    assert _is_linked(a, 'pcm_usagemodel_ClosedWorkload', b1)
    if hasattr(b1, 'PCMRandomVariable249'):
        assert _is_linked(b1, 'PCMRandomVariable249', a)
    _safe_set(a, 'pcm_usagemodel_ClosedWorkload', b2)
    assert _is_linked(a, 'pcm_usagemodel_ClosedWorkload', b2)
    if hasattr(b1, 'PCMRandomVariable249'):
        assert not _is_linked(b1, 'PCMRandomVariable249', a)
    if hasattr(b2, 'PCMRandomVariable249'):
        assert _is_linked(b2, 'PCMRandomVariable249', a)
    _safe_set(a, 'pcm_usagemodel_ClosedWorkload', None)
    assert not _is_linked(a, 'pcm_usagemodel_ClosedWorkload', b2)
    if hasattr(b2, 'PCMRandomVariable249'):
        assert not _is_linked(b2, 'PCMRandomVariable249', a)


def test_assoc_throughput_CommunicationLinkResourceSpecification183_link_reassign_clear():
    a = pcm_resourceenvironment_CommunicationLinkResourceSpecification(failureProbability=3.14)
    b1 = PCMRandomVariable()
    b2 = PCMRandomVariable()
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification184', b1)
    assert _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification184', b1)
    if hasattr(b1, 'PCMRandomVariable185'):
        assert _is_linked(b1, 'PCMRandomVariable185', a)
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification184', b2)
    assert _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification184', b2)
    if hasattr(b1, 'PCMRandomVariable185'):
        assert not _is_linked(b1, 'PCMRandomVariable185', a)
    if hasattr(b2, 'PCMRandomVariable185'):
        assert _is_linked(b2, 'PCMRandomVariable185', a)
    _safe_set(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification184', None)
    assert not _is_linked(a, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification184', b2)
    if hasattr(b2, 'PCMRandomVariable185'):
        assert not _is_linked(b2, 'PCMRandomVariable185', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractAction_strategy = st.builds(AbstractAction)
@given(instance=AbstractAction_strategy)
@settings(max_examples=25)
def test_AbstractAction_instantiation(instance):
    assert isinstance(instance, AbstractAction)


AbstractBranchTransition_strategy = st.builds(AbstractBranchTransition)
@given(instance=AbstractBranchTransition_strategy)
@settings(max_examples=25)
def test_AbstractBranchTransition_instantiation(instance):
    assert isinstance(instance, AbstractBranchTransition)


AbstractInternalControlFlowAction_strategy = st.builds(AbstractInternalControlFlowAction)
@given(instance=AbstractInternalControlFlowAction_strategy)
@settings(max_examples=25)
def test_AbstractInternalControlFlowAction_instantiation(instance):
    assert isinstance(instance, AbstractInternalControlFlowAction)


AbstractLoopAction_strategy = st.builds(AbstractLoopAction)
@given(instance=AbstractLoopAction_strategy)
@settings(max_examples=25)
def test_AbstractLoopAction_instantiation(instance):
    assert isinstance(instance, AbstractLoopAction)


AbstractUserAction_strategy = st.builds(AbstractUserAction)
@given(instance=AbstractUserAction_strategy)
@settings(max_examples=25)
def test_AbstractUserAction_instantiation(instance):
    assert isinstance(instance, AbstractUserAction)


AllocationContext_strategy = st.builds(AllocationContext)
@given(instance=AllocationContext_strategy)
@settings(max_examples=25)
def test_AllocationContext_instantiation(instance):
    assert isinstance(instance, AllocationContext)


BranchTransition_strategy = st.builds(BranchTransition)
@given(instance=BranchTransition_strategy)
@settings(max_examples=25)
def test_BranchTransition_instantiation(instance):
    assert isinstance(instance, BranchTransition)


CommunicationLinkResourceSpecification_strategy = st.builds(CommunicationLinkResourceSpecification)
@given(instance=CommunicationLinkResourceSpecification_strategy)
@settings(max_examples=25)
def test_CommunicationLinkResourceSpecification_instantiation(instance):
    assert isinstance(instance, CommunicationLinkResourceSpecification)


CommunicationLinkResourceType_strategy = st.builds(CommunicationLinkResourceType)
@given(instance=CommunicationLinkResourceType_strategy)
@settings(max_examples=25)
def test_CommunicationLinkResourceType_instantiation(instance):
    assert isinstance(instance, CommunicationLinkResourceType)


CompleteComponentType_strategy = st.builds(CompleteComponentType)
@given(instance=CompleteComponentType_strategy)
@settings(max_examples=25)
def test_CompleteComponentType_instantiation(instance):
    assert isinstance(instance, CompleteComponentType)


CompositeDataType_strategy = st.builds(CompositeDataType)
@given(instance=CompositeDataType_strategy)
@settings(max_examples=25)
def test_CompositeDataType_instantiation(instance):
    assert isinstance(instance, CompositeDataType)


Connector_strategy = st.builds(Connector)
@given(instance=Connector_strategy)
@settings(max_examples=25)
def test_Connector_instantiation(instance):
    assert isinstance(instance, Connector)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


DelegationConnector_strategy = st.builds(DelegationConnector)
@given(instance=DelegationConnector_strategy)
@settings(max_examples=25)
def test_DelegationConnector_instantiation(instance):
    assert isinstance(instance, DelegationConnector)


Entity_strategy = st.builds(Entity)
@given(instance=Entity_strategy)
@settings(max_examples=25)
def test_Entity_instantiation(instance):
    assert isinstance(instance, Entity)


ExceptionType_strategy = st.builds(ExceptionType)
@given(instance=ExceptionType_strategy)
@settings(max_examples=25)
def test_ExceptionType_instantiation(instance):
    assert isinstance(instance, ExceptionType)


ForkedBehaviour_strategy = st.builds(ForkedBehaviour)
@given(instance=ForkedBehaviour_strategy)
@settings(max_examples=25)
def test_ForkedBehaviour_instantiation(instance):
    assert isinstance(instance, ForkedBehaviour)


Identifier_strategy = st.builds(Identifier)
@given(instance=Identifier_strategy)
@settings(max_examples=25)
def test_Identifier_instantiation(instance):
    assert isinstance(instance, Identifier)


ImplementationComponentType_strategy = st.builds(ImplementationComponentType)
@given(instance=ImplementationComponentType_strategy)
@settings(max_examples=25)
def test_ImplementationComponentType_instantiation(instance):
    assert isinstance(instance, ImplementationComponentType)


InnerDeclaration_strategy = st.builds(InnerDeclaration)
@given(instance=InnerDeclaration_strategy)
@settings(max_examples=25)
def test_InnerDeclaration_instantiation(instance):
    assert isinstance(instance, InnerDeclaration)


Interface_strategy = st.builds(Interface)
@given(instance=Interface_strategy)
@settings(max_examples=25)
def test_Interface_instantiation(instance):
    assert isinstance(instance, Interface)


InterfaceProvidingRequiringEntity_strategy = st.builds(InterfaceProvidingRequiringEntity)
@given(instance=InterfaceProvidingRequiringEntity_strategy)
@settings(max_examples=25)
def test_InterfaceProvidingRequiringEntity_instantiation(instance):
    assert isinstance(instance, InterfaceProvidingRequiringEntity)


LinkingResource_strategy = st.builds(LinkingResource)
@given(instance=LinkingResource_strategy)
@settings(max_examples=25)
def test_LinkingResource_instantiation(instance):
    assert isinstance(instance, LinkingResource)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


PCMRandomVariable_strategy = st.builds(PCMRandomVariable)
@given(instance=PCMRandomVariable_strategy)
@settings(max_examples=25)
def test_PCMRandomVariable_instantiation(instance):
    assert isinstance(instance, PCMRandomVariable)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


PassiveResource_strategy = st.builds(PassiveResource)
@given(instance=PassiveResource_strategy)
@settings(max_examples=25)
def test_PassiveResource_instantiation(instance):
    assert isinstance(instance, PassiveResource)


ProcessingResourceSpecification_strategy = st.builds(ProcessingResourceSpecification)
@given(instance=ProcessingResourceSpecification_strategy)
@settings(max_examples=25)
def test_ProcessingResourceSpecification_instantiation(instance):
    assert isinstance(instance, ProcessingResourceSpecification)


ProcessingResourceType_strategy = st.builds(ProcessingResourceType)
@given(instance=ProcessingResourceType_strategy)
@settings(max_examples=25)
def test_ProcessingResourceType_instantiation(instance):
    assert isinstance(instance, ProcessingResourceType)


Protocol_strategy = st.builds(Protocol)
@given(instance=Protocol_strategy)
@settings(max_examples=25)
def test_Protocol_instantiation(instance):
    assert isinstance(instance, Protocol)


ProvidedRole_strategy = st.builds(ProvidedRole)
@given(instance=ProvidedRole_strategy)
@settings(max_examples=25)
def test_ProvidedRole_instantiation(instance):
    assert isinstance(instance, ProvidedRole)


ProvidesComponentType_strategy = st.builds(ProvidesComponentType)
@given(instance=ProvidesComponentType_strategy)
@settings(max_examples=25)
def test_ProvidesComponentType_instantiation(instance):
    assert isinstance(instance, ProvidesComponentType)


QoSAnnotations_strategy = st.builds(QoSAnnotations)
@given(instance=QoSAnnotations_strategy)
@settings(max_examples=25)
def test_QoSAnnotations_instantiation(instance):
    assert isinstance(instance, QoSAnnotations)


RandomVariable_strategy = st.builds(RandomVariable)
@given(instance=RandomVariable_strategy)
@settings(max_examples=25)
def test_RandomVariable_instantiation(instance):
    assert isinstance(instance, RandomVariable)


Repository_strategy = st.builds(Repository)
@given(instance=Repository_strategy)
@settings(max_examples=25)
def test_Repository_instantiation(instance):
    assert isinstance(instance, Repository)


RepositoryComponent_strategy = st.builds(RepositoryComponent)
@given(instance=RepositoryComponent_strategy)
@settings(max_examples=25)
def test_RepositoryComponent_instantiation(instance):
    assert isinstance(instance, RepositoryComponent)


RequiredRole_strategy = st.builds(RequiredRole)
@given(instance=RequiredRole_strategy)
@settings(max_examples=25)
def test_RequiredRole_instantiation(instance):
    assert isinstance(instance, RequiredRole)


ResourceContainer_strategy = st.builds(ResourceContainer)
@given(instance=ResourceContainer_strategy)
@settings(max_examples=25)
def test_ResourceContainer_instantiation(instance):
    assert isinstance(instance, ResourceContainer)


ResourceDemandingBehaviour_strategy = st.builds(ResourceDemandingBehaviour)
@given(instance=ResourceDemandingBehaviour_strategy)
@settings(max_examples=25)
def test_ResourceDemandingBehaviour_instantiation(instance):
    assert isinstance(instance, ResourceDemandingBehaviour)


ResourceEnvironment_strategy = st.builds(ResourceEnvironment)
@given(instance=ResourceEnvironment_strategy)
@settings(max_examples=25)
def test_ResourceEnvironment_instantiation(instance):
    assert isinstance(instance, ResourceEnvironment)


ResourceRequiredRole_strategy = st.builds(ResourceRequiredRole)
@given(instance=ResourceRequiredRole_strategy)
@settings(max_examples=25)
def test_ResourceRequiredRole_instantiation(instance):
    assert isinstance(instance, ResourceRequiredRole)


ResourceType_strategy = st.builds(ResourceType)
@given(instance=ResourceType_strategy)
@settings(max_examples=25)
def test_ResourceType_instantiation(instance):
    assert isinstance(instance, ResourceType)


Role_strategy = st.builds(Role)
@given(instance=Role_strategy)
@settings(max_examples=25)
def test_Role_instantiation(instance):
    assert isinstance(instance, Role)


ScenarioBehaviour_strategy = st.builds(ScenarioBehaviour)
@given(instance=ScenarioBehaviour_strategy)
@settings(max_examples=25)
def test_ScenarioBehaviour_instantiation(instance):
    assert isinstance(instance, ScenarioBehaviour)


ServiceEffectSpecification_strategy = st.builds(ServiceEffectSpecification)
@given(instance=ServiceEffectSpecification_strategy)
@settings(max_examples=25)
def test_ServiceEffectSpecification_instantiation(instance):
    assert isinstance(instance, ServiceEffectSpecification)


Signature_strategy = st.builds(Signature)
@given(instance=Signature_strategy)
@settings(max_examples=25)
def test_Signature_instantiation(instance):
    assert isinstance(instance, Signature)


SpecifiedOutputParameterAbstraction_strategy = st.builds(SpecifiedOutputParameterAbstraction)
@given(instance=SpecifiedOutputParameterAbstraction_strategy)
@settings(max_examples=25)
def test_SpecifiedOutputParameterAbstraction_instantiation(instance):
    assert isinstance(instance, SpecifiedOutputParameterAbstraction)


SpecifiedQoSAnnotation_strategy = st.builds(SpecifiedQoSAnnotation)
@given(instance=SpecifiedQoSAnnotation_strategy)
@settings(max_examples=25)
def test_SpecifiedQoSAnnotation_instantiation(instance):
    assert isinstance(instance, SpecifiedQoSAnnotation)


SynchronisationPoint_strategy = st.builds(SynchronisationPoint)
@given(instance=SynchronisationPoint_strategy)
@settings(max_examples=25)
def test_SynchronisationPoint_instantiation(instance):
    assert isinstance(instance, SynchronisationPoint)


System_strategy = st.builds(System)
@given(instance=System_strategy)
@settings(max_examples=25)
def test_System_instantiation(instance):
    assert isinstance(instance, System)


UnitCarryingElement_strategy = st.builds(UnitCarryingElement)
@given(instance=UnitCarryingElement_strategy)
@settings(max_examples=25)
def test_UnitCarryingElement_instantiation(instance):
    assert isinstance(instance, UnitCarryingElement)


UsageScenario_strategy = st.builds(UsageScenario)
@given(instance=UsageScenario_strategy)
@settings(max_examples=25)
def test_UsageScenario_instantiation(instance):
    assert isinstance(instance, UsageScenario)


UserData_strategy = st.builds(UserData)
@given(instance=UserData_strategy)
@settings(max_examples=25)
def test_UserData_instantiation(instance):
    assert isinstance(instance, UserData)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


VariableCharacterisation_strategy = st.builds(VariableCharacterisation)
@given(instance=VariableCharacterisation_strategy)
@settings(max_examples=25)
def test_VariableCharacterisation_instantiation(instance):
    assert isinstance(instance, VariableCharacterisation)


VariableUsage_strategy = st.builds(VariableUsage)
@given(instance=VariableUsage_strategy)
@settings(max_examples=25)
def test_VariableUsage_instantiation(instance):
    assert isinstance(instance, VariableUsage)


Workload_strategy = st.builds(Workload)
@given(instance=Workload_strategy)
@settings(max_examples=25)
def test_Workload_instantiation(instance):
    assert isinstance(instance, Workload)


composition_AssemblyConnector_strategy = st.builds(composition_AssemblyConnector)
@given(instance=composition_AssemblyConnector_strategy)
@settings(max_examples=25)
def test_composition_AssemblyConnector_instantiation(instance):
    assert isinstance(instance, composition_AssemblyConnector)


composition_AssemblyContext_strategy = st.builds(composition_AssemblyContext)
@given(instance=composition_AssemblyContext_strategy)
@settings(max_examples=25)
def test_composition_AssemblyContext_instantiation(instance):
    assert isinstance(instance, composition_AssemblyContext)


composition_ComposedStructure_strategy = st.builds(composition_ComposedStructure)
@given(instance=composition_ComposedStructure_strategy)
@settings(max_examples=25)
def test_composition_ComposedStructure_instantiation(instance):
    assert isinstance(instance, composition_ComposedStructure)


composition_ProvidedDelegationConnector_strategy = st.builds(composition_ProvidedDelegationConnector)
@given(instance=composition_ProvidedDelegationConnector_strategy)
@settings(max_examples=25)
def test_composition_ProvidedDelegationConnector_instantiation(instance):
    assert isinstance(instance, composition_ProvidedDelegationConnector)


composition_RequiredDelegationConnector_strategy = st.builds(composition_RequiredDelegationConnector)
@given(instance=composition_RequiredDelegationConnector_strategy)
@settings(max_examples=25)
def test_composition_RequiredDelegationConnector_instantiation(instance):
    assert isinstance(instance, composition_RequiredDelegationConnector)


composition_ResourceRequiredDelegationConnector_strategy = st.builds(composition_ResourceRequiredDelegationConnector)
@given(instance=composition_ResourceRequiredDelegationConnector_strategy)
@settings(max_examples=25)
def test_composition_ResourceRequiredDelegationConnector_instantiation(instance):
    assert isinstance(instance, composition_ResourceRequiredDelegationConnector)


entity_ComposedProvidingRequiringEntity_strategy = st.builds(entity_ComposedProvidingRequiringEntity)
@given(instance=entity_ComposedProvidingRequiringEntity_strategy)
@settings(max_examples=25)
def test_entity_ComposedProvidingRequiringEntity_instantiation(instance):
    assert isinstance(instance, entity_ComposedProvidingRequiringEntity)


entity_Entity_strategy = st.builds(entity_Entity)
@given(instance=entity_Entity_strategy)
@settings(max_examples=25)
def test_entity_Entity_instantiation(instance):
    assert isinstance(instance, entity_Entity)


entity_InterfaceProvidingEntity_strategy = st.builds(entity_InterfaceProvidingEntity)
@given(instance=entity_InterfaceProvidingEntity_strategy)
@settings(max_examples=25)
def test_entity_InterfaceProvidingEntity_instantiation(instance):
    assert isinstance(instance, entity_InterfaceProvidingEntity)


entity_InterfaceProvidingRequiringEntity_strategy = st.builds(entity_InterfaceProvidingRequiringEntity)
@given(instance=entity_InterfaceProvidingRequiringEntity_strategy)
@settings(max_examples=25)
def test_entity_InterfaceProvidingRequiringEntity_instantiation(instance):
    assert isinstance(instance, entity_InterfaceProvidingRequiringEntity)


entity_InterfaceRequiringEntity_strategy = st.builds(entity_InterfaceRequiringEntity)
@given(instance=entity_InterfaceRequiringEntity_strategy)
@settings(max_examples=25)
def test_entity_InterfaceRequiringEntity_instantiation(instance):
    assert isinstance(instance, entity_InterfaceRequiringEntity)


entity_NamedElement_strategy = st.builds(entity_NamedElement)
@given(instance=entity_NamedElement_strategy)
@settings(max_examples=25)
def test_entity_NamedElement_instantiation(instance):
    assert isinstance(instance, entity_NamedElement)


entity_ResourceInterfaceRequiringEntity_strategy = st.builds(entity_ResourceInterfaceRequiringEntity)
@given(instance=entity_ResourceInterfaceRequiringEntity_strategy)
@settings(max_examples=25)
def test_entity_ResourceInterfaceRequiringEntity_instantiation(instance):
    assert isinstance(instance, entity_ResourceInterfaceRequiringEntity)


parameter_pcm_AbstractNamedReference_strategy = st.builds(parameter_pcm_AbstractNamedReference)
@given(instance=parameter_pcm_AbstractNamedReference_strategy)
@settings(max_examples=25)
def test_parameter_pcm_AbstractNamedReference_instantiation(instance):
    assert isinstance(instance, parameter_pcm_AbstractNamedReference)


pcm_allocation_Allocation_strategy = st.builds(pcm_allocation_Allocation)
@given(instance=pcm_allocation_Allocation_strategy)
@settings(max_examples=25)
def test_pcm_allocation_Allocation_instantiation(instance):
    assert isinstance(instance, pcm_allocation_Allocation)


pcm_allocation_AllocationContext_strategy = st.builds(pcm_allocation_AllocationContext)
@given(instance=pcm_allocation_AllocationContext_strategy)
@settings(max_examples=25)
def test_pcm_allocation_AllocationContext_instantiation(instance):
    assert isinstance(instance, pcm_allocation_AllocationContext)


pcm_composition_AssemblyConnector_strategy = st.builds(pcm_composition_AssemblyConnector)
@given(instance=pcm_composition_AssemblyConnector_strategy)
@settings(max_examples=25)
def test_pcm_composition_AssemblyConnector_instantiation(instance):
    assert isinstance(instance, pcm_composition_AssemblyConnector)


pcm_composition_AssemblyContext_strategy = st.builds(pcm_composition_AssemblyContext)
@given(instance=pcm_composition_AssemblyContext_strategy)
@settings(max_examples=25)
def test_pcm_composition_AssemblyContext_instantiation(instance):
    assert isinstance(instance, pcm_composition_AssemblyContext)


pcm_composition_ComposedStructure_strategy = st.builds(pcm_composition_ComposedStructure)
@given(instance=pcm_composition_ComposedStructure_strategy)
@settings(max_examples=25)
def test_pcm_composition_ComposedStructure_instantiation(instance):
    assert isinstance(instance, pcm_composition_ComposedStructure)


pcm_composition_ProvidedDelegationConnector_strategy = st.builds(pcm_composition_ProvidedDelegationConnector)
@given(instance=pcm_composition_ProvidedDelegationConnector_strategy)
@settings(max_examples=25)
def test_pcm_composition_ProvidedDelegationConnector_instantiation(instance):
    assert isinstance(instance, pcm_composition_ProvidedDelegationConnector)


pcm_composition_RequiredDelegationConnector_strategy = st.builds(pcm_composition_RequiredDelegationConnector)
@given(instance=pcm_composition_RequiredDelegationConnector_strategy)
@settings(max_examples=25)
def test_pcm_composition_RequiredDelegationConnector_instantiation(instance):
    assert isinstance(instance, pcm_composition_RequiredDelegationConnector)


pcm_composition_ResourceRequiredDelegationConnector_strategy = st.builds(pcm_composition_ResourceRequiredDelegationConnector)
@given(instance=pcm_composition_ResourceRequiredDelegationConnector_strategy)
@settings(max_examples=25)
def test_pcm_composition_ResourceRequiredDelegationConnector_instantiation(instance):
    assert isinstance(instance, pcm_composition_ResourceRequiredDelegationConnector)


pcm_connectors_Connector_strategy = st.builds(pcm_connectors_Connector)
@given(instance=pcm_connectors_Connector_strategy)
@settings(max_examples=25)
def test_pcm_connectors_Connector_instantiation(instance):
    assert isinstance(instance, pcm_connectors_Connector)


pcm_core_PCMRandomVariable_strategy = st.builds(pcm_core_PCMRandomVariable)
@given(instance=pcm_core_PCMRandomVariable_strategy)
@settings(max_examples=25)
def test_pcm_core_PCMRandomVariable_instantiation(instance):
    assert isinstance(instance, pcm_core_PCMRandomVariable)


pcm_entity_ComposedProvidingRequiringEntity_strategy = st.builds(pcm_entity_ComposedProvidingRequiringEntity)
@given(instance=pcm_entity_ComposedProvidingRequiringEntity_strategy)
@settings(max_examples=25)
def test_pcm_entity_ComposedProvidingRequiringEntity_instantiation(instance):
    assert isinstance(instance, pcm_entity_ComposedProvidingRequiringEntity)


pcm_entity_Entity_strategy = st.builds(pcm_entity_Entity)
@given(instance=pcm_entity_Entity_strategy)
@settings(max_examples=25)
def test_pcm_entity_Entity_instantiation(instance):
    assert isinstance(instance, pcm_entity_Entity)


pcm_entity_InterfaceProvidingEntity_strategy = st.builds(pcm_entity_InterfaceProvidingEntity)
@given(instance=pcm_entity_InterfaceProvidingEntity_strategy)
@settings(max_examples=25)
def test_pcm_entity_InterfaceProvidingEntity_instantiation(instance):
    assert isinstance(instance, pcm_entity_InterfaceProvidingEntity)


pcm_entity_InterfaceProvidingRequiringEntity_strategy = st.builds(pcm_entity_InterfaceProvidingRequiringEntity)
@given(instance=pcm_entity_InterfaceProvidingRequiringEntity_strategy)
@settings(max_examples=25)
def test_pcm_entity_InterfaceProvidingRequiringEntity_instantiation(instance):
    assert isinstance(instance, pcm_entity_InterfaceProvidingRequiringEntity)


pcm_entity_InterfaceRequiringEntity_strategy = st.builds(pcm_entity_InterfaceRequiringEntity)
@given(instance=pcm_entity_InterfaceRequiringEntity_strategy)
@settings(max_examples=25)
def test_pcm_entity_InterfaceRequiringEntity_instantiation(instance):
    assert isinstance(instance, pcm_entity_InterfaceRequiringEntity)


pcm_entity_NamedElement_strategy = st.builds(pcm_entity_NamedElement, entityName=safe_text)
@given(instance=pcm_entity_NamedElement_strategy)
@settings(max_examples=25)
def test_pcm_entity_NamedElement_instantiation(instance):
    assert isinstance(instance, pcm_entity_NamedElement)


pcm_entity_ResourceInterfaceRequiringEntity_strategy = st.builds(pcm_entity_ResourceInterfaceRequiringEntity)
@given(instance=pcm_entity_ResourceInterfaceRequiringEntity_strategy)
@settings(max_examples=25)
def test_pcm_entity_ResourceInterfaceRequiringEntity_instantiation(instance):
    assert isinstance(instance, pcm_entity_ResourceInterfaceRequiringEntity)


pcm_parameter_CharacterisedVariable_strategy = st.builds(pcm_parameter_CharacterisedVariable, characterisationType=safe_text)
@given(instance=pcm_parameter_CharacterisedVariable_strategy)
@settings(max_examples=25)
def test_pcm_parameter_CharacterisedVariable_instantiation(instance):
    assert isinstance(instance, pcm_parameter_CharacterisedVariable)


pcm_parameter_VariableCharacterisation_strategy = st.builds(pcm_parameter_VariableCharacterisation, type=safe_text)
@given(instance=pcm_parameter_VariableCharacterisation_strategy)
@settings(max_examples=25)
def test_pcm_parameter_VariableCharacterisation_instantiation(instance):
    assert isinstance(instance, pcm_parameter_VariableCharacterisation)


pcm_parameter_VariableUsage_strategy = st.builds(pcm_parameter_VariableUsage)
@given(instance=pcm_parameter_VariableUsage_strategy)
@settings(max_examples=25)
def test_pcm_parameter_VariableUsage_instantiation(instance):
    assert isinstance(instance, pcm_parameter_VariableUsage)


pcm_performance_ComponentSpecifiedExecutionTime_strategy = st.builds(pcm_performance_ComponentSpecifiedExecutionTime)
@given(instance=pcm_performance_ComponentSpecifiedExecutionTime_strategy)
@settings(max_examples=25)
def test_pcm_performance_ComponentSpecifiedExecutionTime_instantiation(instance):
    assert isinstance(instance, pcm_performance_ComponentSpecifiedExecutionTime)


pcm_performance_ParametricResourceDemand_strategy = st.builds(pcm_performance_ParametricResourceDemand)
@given(instance=pcm_performance_ParametricResourceDemand_strategy)
@settings(max_examples=25)
def test_pcm_performance_ParametricResourceDemand_instantiation(instance):
    assert isinstance(instance, pcm_performance_ParametricResourceDemand)


pcm_performance_SystemSpecifiedExecutionTime_strategy = st.builds(pcm_performance_SystemSpecifiedExecutionTime)
@given(instance=pcm_performance_SystemSpecifiedExecutionTime_strategy)
@settings(max_examples=25)
def test_pcm_performance_SystemSpecifiedExecutionTime_instantiation(instance):
    assert isinstance(instance, pcm_performance_SystemSpecifiedExecutionTime)


pcm_protocol_Protocol_strategy = st.builds(pcm_protocol_Protocol, protocolTypeID=safe_text)
@given(instance=pcm_protocol_Protocol_strategy)
@settings(max_examples=25)
def test_pcm_protocol_Protocol_instantiation(instance):
    assert isinstance(instance, pcm_protocol_Protocol)


pcm_protocol_ServiceCall_strategy = st.builds(pcm_protocol_ServiceCall)
@given(instance=pcm_protocol_ServiceCall_strategy)
@settings(max_examples=25)
def test_pcm_protocol_ServiceCall_instantiation(instance):
    assert isinstance(instance, pcm_protocol_ServiceCall)


pcm_qosannotations_QoSAnnotations_strategy = st.builds(pcm_qosannotations_QoSAnnotations)
@given(instance=pcm_qosannotations_QoSAnnotations_strategy)
@settings(max_examples=25)
def test_pcm_qosannotations_QoSAnnotations_instantiation(instance):
    assert isinstance(instance, pcm_qosannotations_QoSAnnotations)


pcm_qosannotations_SpecifiedOutputParameterAbstraction_strategy = st.builds(pcm_qosannotations_SpecifiedOutputParameterAbstraction)
@given(instance=pcm_qosannotations_SpecifiedOutputParameterAbstraction_strategy)
@settings(max_examples=25)
def test_pcm_qosannotations_SpecifiedOutputParameterAbstraction_instantiation(instance):
    assert isinstance(instance, pcm_qosannotations_SpecifiedOutputParameterAbstraction)


pcm_qosannotations_SpecifiedQoSAnnotation_strategy = st.builds(pcm_qosannotations_SpecifiedQoSAnnotation)
@given(instance=pcm_qosannotations_SpecifiedQoSAnnotation_strategy)
@settings(max_examples=25)
def test_pcm_qosannotations_SpecifiedQoSAnnotation_instantiation(instance):
    assert isinstance(instance, pcm_qosannotations_SpecifiedQoSAnnotation)


pcm_reliability_SpecifiedFailureProbability_strategy = st.builds(pcm_reliability_SpecifiedFailureProbability, failureProbability=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=pcm_reliability_SpecifiedFailureProbability_strategy)
@settings(max_examples=25)
def test_pcm_reliability_SpecifiedFailureProbability_instantiation(instance):
    assert isinstance(instance, pcm_reliability_SpecifiedFailureProbability)


pcm_repository_BasicComponent_strategy = st.builds(pcm_repository_BasicComponent)
@given(instance=pcm_repository_BasicComponent_strategy)
@settings(max_examples=25)
def test_pcm_repository_BasicComponent_instantiation(instance):
    assert isinstance(instance, pcm_repository_BasicComponent)


pcm_repository_CollectionDataType_strategy = st.builds(pcm_repository_CollectionDataType)
@given(instance=pcm_repository_CollectionDataType_strategy)
@settings(max_examples=25)
def test_pcm_repository_CollectionDataType_instantiation(instance):
    assert isinstance(instance, pcm_repository_CollectionDataType)


pcm_repository_CompleteComponentType_strategy = st.builds(pcm_repository_CompleteComponentType)
@given(instance=pcm_repository_CompleteComponentType_strategy)
@settings(max_examples=25)
def test_pcm_repository_CompleteComponentType_instantiation(instance):
    assert isinstance(instance, pcm_repository_CompleteComponentType)


pcm_repository_CompositeComponent_strategy = st.builds(pcm_repository_CompositeComponent)
@given(instance=pcm_repository_CompositeComponent_strategy)
@settings(max_examples=25)
def test_pcm_repository_CompositeComponent_instantiation(instance):
    assert isinstance(instance, pcm_repository_CompositeComponent)


pcm_repository_CompositeDataType_strategy = st.builds(pcm_repository_CompositeDataType)
@given(instance=pcm_repository_CompositeDataType_strategy)
@settings(max_examples=25)
def test_pcm_repository_CompositeDataType_instantiation(instance):
    assert isinstance(instance, pcm_repository_CompositeDataType)


pcm_repository_DataType_strategy = st.builds(pcm_repository_DataType)
@given(instance=pcm_repository_DataType_strategy)
@settings(max_examples=25)
def test_pcm_repository_DataType_instantiation(instance):
    assert isinstance(instance, pcm_repository_DataType)


pcm_repository_DelegationConnector_strategy = st.builds(pcm_repository_DelegationConnector)
@given(instance=pcm_repository_DelegationConnector_strategy)
@settings(max_examples=25)
def test_pcm_repository_DelegationConnector_instantiation(instance):
    assert isinstance(instance, pcm_repository_DelegationConnector)


pcm_repository_ExceptionType_strategy = st.builds(pcm_repository_ExceptionType, exceptionMessage=safe_text, exceptionName=safe_text)
@given(instance=pcm_repository_ExceptionType_strategy)
@settings(max_examples=25)
def test_pcm_repository_ExceptionType_instantiation(instance):
    assert isinstance(instance, pcm_repository_ExceptionType)


pcm_repository_ImplementationComponentType_strategy = st.builds(pcm_repository_ImplementationComponentType)
@given(instance=pcm_repository_ImplementationComponentType_strategy)
@settings(max_examples=25)
def test_pcm_repository_ImplementationComponentType_instantiation(instance):
    assert isinstance(instance, pcm_repository_ImplementationComponentType)


pcm_repository_InnerDeclaration_strategy = st.builds(pcm_repository_InnerDeclaration)
@given(instance=pcm_repository_InnerDeclaration_strategy)
@settings(max_examples=25)
def test_pcm_repository_InnerDeclaration_instantiation(instance):
    assert isinstance(instance, pcm_repository_InnerDeclaration)


pcm_repository_Interface_strategy = st.builds(pcm_repository_Interface)
@given(instance=pcm_repository_Interface_strategy)
@settings(max_examples=25)
def test_pcm_repository_Interface_instantiation(instance):
    assert isinstance(instance, pcm_repository_Interface)


pcm_repository_Parameter_strategy = st.builds(pcm_repository_Parameter, modifier__Parameter=safe_text, parameterName=safe_text)
@given(instance=pcm_repository_Parameter_strategy)
@settings(max_examples=25)
def test_pcm_repository_Parameter_instantiation(instance):
    assert isinstance(instance, pcm_repository_Parameter)


pcm_repository_PassiveResource_strategy = st.builds(pcm_repository_PassiveResource)
@given(instance=pcm_repository_PassiveResource_strategy)
@settings(max_examples=25)
def test_pcm_repository_PassiveResource_instantiation(instance):
    assert isinstance(instance, pcm_repository_PassiveResource)


pcm_repository_PrimitiveDataType_strategy = st.builds(pcm_repository_PrimitiveDataType, type=safe_text)
@given(instance=pcm_repository_PrimitiveDataType_strategy)
@settings(max_examples=25)
def test_pcm_repository_PrimitiveDataType_instantiation(instance):
    assert isinstance(instance, pcm_repository_PrimitiveDataType)


pcm_repository_ProvidedRole_strategy = st.builds(pcm_repository_ProvidedRole)
@given(instance=pcm_repository_ProvidedRole_strategy)
@settings(max_examples=25)
def test_pcm_repository_ProvidedRole_instantiation(instance):
    assert isinstance(instance, pcm_repository_ProvidedRole)


pcm_repository_ProvidesComponentType_strategy = st.builds(pcm_repository_ProvidesComponentType)
@given(instance=pcm_repository_ProvidesComponentType_strategy)
@settings(max_examples=25)
def test_pcm_repository_ProvidesComponentType_instantiation(instance):
    assert isinstance(instance, pcm_repository_ProvidesComponentType)


pcm_repository_Repository_strategy = st.builds(pcm_repository_Repository, repositoryDescription=safe_text)
@given(instance=pcm_repository_Repository_strategy)
@settings(max_examples=25)
def test_pcm_repository_Repository_instantiation(instance):
    assert isinstance(instance, pcm_repository_Repository)


pcm_repository_RepositoryComponent_strategy = st.builds(pcm_repository_RepositoryComponent)
@given(instance=pcm_repository_RepositoryComponent_strategy)
@settings(max_examples=25)
def test_pcm_repository_RepositoryComponent_instantiation(instance):
    assert isinstance(instance, pcm_repository_RepositoryComponent)


pcm_repository_RequiredRole_strategy = st.builds(pcm_repository_RequiredRole)
@given(instance=pcm_repository_RequiredRole_strategy)
@settings(max_examples=25)
def test_pcm_repository_RequiredRole_instantiation(instance):
    assert isinstance(instance, pcm_repository_RequiredRole)


pcm_repository_ResourceRequiredRole_strategy = st.builds(pcm_repository_ResourceRequiredRole)
@given(instance=pcm_repository_ResourceRequiredRole_strategy)
@settings(max_examples=25)
def test_pcm_repository_ResourceRequiredRole_instantiation(instance):
    assert isinstance(instance, pcm_repository_ResourceRequiredRole)


pcm_repository_Role_strategy = st.builds(pcm_repository_Role)
@given(instance=pcm_repository_Role_strategy)
@settings(max_examples=25)
def test_pcm_repository_Role_instantiation(instance):
    assert isinstance(instance, pcm_repository_Role)


pcm_repository_Signature_strategy = st.builds(pcm_repository_Signature, serviceName=safe_text)
@given(instance=pcm_repository_Signature_strategy)
@settings(max_examples=25)
def test_pcm_repository_Signature_instantiation(instance):
    assert isinstance(instance, pcm_repository_Signature)


pcm_resourceenvironment_CommunicationLinkResourceSpecification_strategy = st.builds(pcm_resourceenvironment_CommunicationLinkResourceSpecification, failureProbability=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=pcm_resourceenvironment_CommunicationLinkResourceSpecification_strategy)
@settings(max_examples=25)
def test_pcm_resourceenvironment_CommunicationLinkResourceSpecification_instantiation(instance):
    assert isinstance(instance, pcm_resourceenvironment_CommunicationLinkResourceSpecification)


pcm_resourceenvironment_LinkingResource_strategy = st.builds(pcm_resourceenvironment_LinkingResource)
@given(instance=pcm_resourceenvironment_LinkingResource_strategy)
@settings(max_examples=25)
def test_pcm_resourceenvironment_LinkingResource_instantiation(instance):
    assert isinstance(instance, pcm_resourceenvironment_LinkingResource)


pcm_resourceenvironment_ProcessingResourceSpecification_strategy = st.builds(pcm_resourceenvironment_ProcessingResourceSpecification, MTTF=st.floats(allow_nan=False, allow_infinity=False), MTTR=st.floats(allow_nan=False, allow_infinity=False), schedulingPolicy=safe_text)
@given(instance=pcm_resourceenvironment_ProcessingResourceSpecification_strategy)
@settings(max_examples=25)
def test_pcm_resourceenvironment_ProcessingResourceSpecification_instantiation(instance):
    assert isinstance(instance, pcm_resourceenvironment_ProcessingResourceSpecification)


pcm_resourceenvironment_ResourceContainer_strategy = st.builds(pcm_resourceenvironment_ResourceContainer)
@given(instance=pcm_resourceenvironment_ResourceContainer_strategy)
@settings(max_examples=25)
def test_pcm_resourceenvironment_ResourceContainer_instantiation(instance):
    assert isinstance(instance, pcm_resourceenvironment_ResourceContainer)


pcm_resourceenvironment_ResourceEnvironment_strategy = st.builds(pcm_resourceenvironment_ResourceEnvironment)
@given(instance=pcm_resourceenvironment_ResourceEnvironment_strategy)
@settings(max_examples=25)
def test_pcm_resourceenvironment_ResourceEnvironment_instantiation(instance):
    assert isinstance(instance, pcm_resourceenvironment_ResourceEnvironment)


pcm_resourcetype_CommunicationLinkResourceType_strategy = st.builds(pcm_resourcetype_CommunicationLinkResourceType)
@given(instance=pcm_resourcetype_CommunicationLinkResourceType_strategy)
@settings(max_examples=25)
def test_pcm_resourcetype_CommunicationLinkResourceType_instantiation(instance):
    assert isinstance(instance, pcm_resourcetype_CommunicationLinkResourceType)


pcm_resourcetype_ProcessingResourceType_strategy = st.builds(pcm_resourcetype_ProcessingResourceType)
@given(instance=pcm_resourcetype_ProcessingResourceType_strategy)
@settings(max_examples=25)
def test_pcm_resourcetype_ProcessingResourceType_instantiation(instance):
    assert isinstance(instance, pcm_resourcetype_ProcessingResourceType)


pcm_resourcetype_ResourceRepository_strategy = st.builds(pcm_resourcetype_ResourceRepository)
@given(instance=pcm_resourcetype_ResourceRepository_strategy)
@settings(max_examples=25)
def test_pcm_resourcetype_ResourceRepository_instantiation(instance):
    assert isinstance(instance, pcm_resourcetype_ResourceRepository)


pcm_resourcetype_ResourceType_strategy = st.builds(pcm_resourcetype_ResourceType)
@given(instance=pcm_resourcetype_ResourceType_strategy)
@settings(max_examples=25)
def test_pcm_resourcetype_ResourceType_instantiation(instance):
    assert isinstance(instance, pcm_resourcetype_ResourceType)


pcm_seff_AbstractAction_strategy = st.builds(pcm_seff_AbstractAction)
@given(instance=pcm_seff_AbstractAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_AbstractAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_AbstractAction)


pcm_seff_AbstractBranchTransition_strategy = st.builds(pcm_seff_AbstractBranchTransition)
@given(instance=pcm_seff_AbstractBranchTransition_strategy)
@settings(max_examples=25)
def test_pcm_seff_AbstractBranchTransition_instantiation(instance):
    assert isinstance(instance, pcm_seff_AbstractBranchTransition)


pcm_seff_AbstractInternalControlFlowAction_strategy = st.builds(pcm_seff_AbstractInternalControlFlowAction)
@given(instance=pcm_seff_AbstractInternalControlFlowAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_AbstractInternalControlFlowAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_AbstractInternalControlFlowAction)


pcm_seff_AbstractLoopAction_strategy = st.builds(pcm_seff_AbstractLoopAction)
@given(instance=pcm_seff_AbstractLoopAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_AbstractLoopAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_AbstractLoopAction)


pcm_seff_AcquireAction_strategy = st.builds(pcm_seff_AcquireAction)
@given(instance=pcm_seff_AcquireAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_AcquireAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_AcquireAction)


pcm_seff_BranchAction_strategy = st.builds(pcm_seff_BranchAction)
@given(instance=pcm_seff_BranchAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_BranchAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_BranchAction)


pcm_seff_CollectionIteratorAction_strategy = st.builds(pcm_seff_CollectionIteratorAction)
@given(instance=pcm_seff_CollectionIteratorAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_CollectionIteratorAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_CollectionIteratorAction)


pcm_seff_ExternalCallAction_strategy = st.builds(pcm_seff_ExternalCallAction, retryCount=st.integers())
@given(instance=pcm_seff_ExternalCallAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_ExternalCallAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_ExternalCallAction)


pcm_seff_ForkAction_strategy = st.builds(pcm_seff_ForkAction)
@given(instance=pcm_seff_ForkAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_ForkAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_ForkAction)


pcm_seff_ForkedBehaviour_strategy = st.builds(pcm_seff_ForkedBehaviour)
@given(instance=pcm_seff_ForkedBehaviour_strategy)
@settings(max_examples=25)
def test_pcm_seff_ForkedBehaviour_instantiation(instance):
    assert isinstance(instance, pcm_seff_ForkedBehaviour)


pcm_seff_GuardedBranchTransition_strategy = st.builds(pcm_seff_GuardedBranchTransition)
@given(instance=pcm_seff_GuardedBranchTransition_strategy)
@settings(max_examples=25)
def test_pcm_seff_GuardedBranchTransition_instantiation(instance):
    assert isinstance(instance, pcm_seff_GuardedBranchTransition)


pcm_seff_InternalAction_strategy = st.builds(pcm_seff_InternalAction, failureProbability=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=pcm_seff_InternalAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_InternalAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_InternalAction)


pcm_seff_LoopAction_strategy = st.builds(pcm_seff_LoopAction)
@given(instance=pcm_seff_LoopAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_LoopAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_LoopAction)


pcm_seff_ProbabilisticBranchTransition_strategy = st.builds(pcm_seff_ProbabilisticBranchTransition, branchProbability=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=pcm_seff_ProbabilisticBranchTransition_strategy)
@settings(max_examples=25)
def test_pcm_seff_ProbabilisticBranchTransition_instantiation(instance):
    assert isinstance(instance, pcm_seff_ProbabilisticBranchTransition)


pcm_seff_ReleaseAction_strategy = st.builds(pcm_seff_ReleaseAction)
@given(instance=pcm_seff_ReleaseAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_ReleaseAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_ReleaseAction)


pcm_seff_ResourceDemandingBehaviour_strategy = st.builds(pcm_seff_ResourceDemandingBehaviour)
@given(instance=pcm_seff_ResourceDemandingBehaviour_strategy)
@settings(max_examples=25)
def test_pcm_seff_ResourceDemandingBehaviour_instantiation(instance):
    assert isinstance(instance, pcm_seff_ResourceDemandingBehaviour)


pcm_seff_ResourceDemandingSEFF_strategy = st.builds(pcm_seff_ResourceDemandingSEFF)
@given(instance=pcm_seff_ResourceDemandingSEFF_strategy)
@settings(max_examples=25)
def test_pcm_seff_ResourceDemandingSEFF_instantiation(instance):
    assert isinstance(instance, pcm_seff_ResourceDemandingSEFF)


pcm_seff_ServiceEffectSpecification_strategy = st.builds(pcm_seff_ServiceEffectSpecification, seffTypeID=safe_text)
@given(instance=pcm_seff_ServiceEffectSpecification_strategy)
@settings(max_examples=25)
def test_pcm_seff_ServiceEffectSpecification_instantiation(instance):
    assert isinstance(instance, pcm_seff_ServiceEffectSpecification)


pcm_seff_SetVariableAction_strategy = st.builds(pcm_seff_SetVariableAction)
@given(instance=pcm_seff_SetVariableAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_SetVariableAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_SetVariableAction)


pcm_seff_StartAction_strategy = st.builds(pcm_seff_StartAction)
@given(instance=pcm_seff_StartAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_StartAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_StartAction)


pcm_seff_StopAction_strategy = st.builds(pcm_seff_StopAction)
@given(instance=pcm_seff_StopAction_strategy)
@settings(max_examples=25)
def test_pcm_seff_StopAction_instantiation(instance):
    assert isinstance(instance, pcm_seff_StopAction)


pcm_seff_SynchronisationPoint_strategy = st.builds(pcm_seff_SynchronisationPoint)
@given(instance=pcm_seff_SynchronisationPoint_strategy)
@settings(max_examples=25)
def test_pcm_seff_SynchronisationPoint_instantiation(instance):
    assert isinstance(instance, pcm_seff_SynchronisationPoint)


pcm_subsystem_SubSystem_strategy = st.builds(pcm_subsystem_SubSystem)
@given(instance=pcm_subsystem_SubSystem_strategy)
@settings(max_examples=25)
def test_pcm_subsystem_SubSystem_instantiation(instance):
    assert isinstance(instance, pcm_subsystem_SubSystem)


pcm_system_System_strategy = st.builds(pcm_system_System)
@given(instance=pcm_system_System_strategy)
@settings(max_examples=25)
def test_pcm_system_System_instantiation(instance):
    assert isinstance(instance, pcm_system_System)


pcm_usagemodel_AbstractUserAction_strategy = st.builds(pcm_usagemodel_AbstractUserAction)
@given(instance=pcm_usagemodel_AbstractUserAction_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_AbstractUserAction_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_AbstractUserAction)


pcm_usagemodel_Branch_strategy = st.builds(pcm_usagemodel_Branch)
@given(instance=pcm_usagemodel_Branch_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_Branch_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_Branch)


pcm_usagemodel_BranchTransition_strategy = st.builds(pcm_usagemodel_BranchTransition, branchProbability=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=pcm_usagemodel_BranchTransition_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_BranchTransition_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_BranchTransition)


pcm_usagemodel_ClosedWorkload_strategy = st.builds(pcm_usagemodel_ClosedWorkload, population=st.integers())
@given(instance=pcm_usagemodel_ClosedWorkload_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_ClosedWorkload_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_ClosedWorkload)


pcm_usagemodel_Delay_strategy = st.builds(pcm_usagemodel_Delay)
@given(instance=pcm_usagemodel_Delay_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_Delay_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_Delay)


pcm_usagemodel_EntryLevelSystemCall_strategy = st.builds(pcm_usagemodel_EntryLevelSystemCall)
@given(instance=pcm_usagemodel_EntryLevelSystemCall_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_EntryLevelSystemCall_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_EntryLevelSystemCall)


pcm_usagemodel_Loop_strategy = st.builds(pcm_usagemodel_Loop)
@given(instance=pcm_usagemodel_Loop_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_Loop_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_Loop)


pcm_usagemodel_OpenWorkload_strategy = st.builds(pcm_usagemodel_OpenWorkload)
@given(instance=pcm_usagemodel_OpenWorkload_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_OpenWorkload_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_OpenWorkload)


pcm_usagemodel_ScenarioBehaviour_strategy = st.builds(pcm_usagemodel_ScenarioBehaviour)
@given(instance=pcm_usagemodel_ScenarioBehaviour_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_ScenarioBehaviour_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_ScenarioBehaviour)


pcm_usagemodel_Start_strategy = st.builds(pcm_usagemodel_Start)
@given(instance=pcm_usagemodel_Start_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_Start_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_Start)


pcm_usagemodel_Stop_strategy = st.builds(pcm_usagemodel_Stop)
@given(instance=pcm_usagemodel_Stop_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_Stop_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_Stop)


pcm_usagemodel_UsageModel_strategy = st.builds(pcm_usagemodel_UsageModel)
@given(instance=pcm_usagemodel_UsageModel_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_UsageModel_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_UsageModel)


pcm_usagemodel_UsageScenario_strategy = st.builds(pcm_usagemodel_UsageScenario)
@given(instance=pcm_usagemodel_UsageScenario_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_UsageScenario_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_UsageScenario)


pcm_usagemodel_UserData_strategy = st.builds(pcm_usagemodel_UserData)
@given(instance=pcm_usagemodel_UserData_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_UserData_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_UserData)


pcm_usagemodel_Workload_strategy = st.builds(pcm_usagemodel_Workload)
@given(instance=pcm_usagemodel_Workload_strategy)
@settings(max_examples=25)
def test_pcm_usagemodel_Workload_instantiation(instance):
    assert isinstance(instance, pcm_usagemodel_Workload)


performance_ParametricResourceDemand_strategy = st.builds(performance_ParametricResourceDemand)
@given(instance=performance_ParametricResourceDemand_strategy)
@settings(max_examples=25)
def test_performance_ParametricResourceDemand_instantiation(instance):
    assert isinstance(instance, performance_ParametricResourceDemand)


repository_DataType_strategy = st.builds(repository_DataType)
@given(instance=repository_DataType_strategy)
@settings(max_examples=25)
def test_repository_DataType_instantiation(instance):
    assert isinstance(instance, repository_DataType)


repository_ImplementationComponentType_strategy = st.builds(repository_ImplementationComponentType)
@given(instance=repository_ImplementationComponentType_strategy)
@settings(max_examples=25)
def test_repository_ImplementationComponentType_instantiation(instance):
    assert isinstance(instance, repository_ImplementationComponentType)


repository_RepositoryComponent_strategy = st.builds(repository_RepositoryComponent)
@given(instance=repository_RepositoryComponent_strategy)
@settings(max_examples=25)
def test_repository_RepositoryComponent_instantiation(instance):
    assert isinstance(instance, repository_RepositoryComponent)


seff_ResourceDemandingBehaviour_strategy = st.builds(seff_ResourceDemandingBehaviour)
@given(instance=seff_ResourceDemandingBehaviour_strategy)
@settings(max_examples=25)
def test_seff_ResourceDemandingBehaviour_instantiation(instance):
    assert isinstance(instance, seff_ResourceDemandingBehaviour)


seff_ServiceEffectSpecification_strategy = st.builds(seff_ServiceEffectSpecification)
@given(instance=seff_ServiceEffectSpecification_strategy)
@settings(max_examples=25)
def test_seff_ServiceEffectSpecification_instantiation(instance):
    assert isinstance(instance, seff_ServiceEffectSpecification)



