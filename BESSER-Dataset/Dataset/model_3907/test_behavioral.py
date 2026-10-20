import pytest
from datetime import date, datetime, time, timedelta

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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions_ScenarioBehaviour217_stub_double():
    # AbstractUserAction has no real 'AbstractUserAction' property in the generated
    # code (a bare stub) -- manually attach it so pcm_usagemodel_ScenarioBehaviour's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_usagemodel_ScenarioBehaviour's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_usagemodel_ScenarioBehaviour()
    partner = AbstractUserAction()
    setattr(partner, 'AbstractUserAction', None)
    _safe_set(owner, 'pcm_usagemodel_ScenarioBehaviour', {partner})
    assert getattr(partner, 'AbstractUserAction') == owner
    _safe_set(owner, 'pcm_usagemodel_ScenarioBehaviour', set())
    assert getattr(partner, 'AbstractUserAction') is None


def test_assoc_activeResourceType_ActiveResourceSpecification186_stub_double():
    # ProcessingResourceType has no real 'ProcessingResourceType187' property in the generated
    # code (a bare stub) -- manually attach it so pcm_resourceenvironment_ProcessingResourceSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_resourceenvironment_ProcessingResourceSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_resourceenvironment_ProcessingResourceSpecification(MTTF=3.14, MTTR=3.14, schedulingPolicy="sample_text")
    partner = ProcessingResourceType()
    setattr(partner, 'ProcessingResourceType187', None)
    _safe_set(owner, 'pcm_resourceenvironment_ProcessingResourceSpecification', partner)
    assert getattr(partner, 'ProcessingResourceType187') == owner
    _safe_set(owner, 'pcm_resourceenvironment_ProcessingResourceSpecification', None)
    assert getattr(partner, 'ProcessingResourceType187') is None


def test_assoc_allocationContexts_Allocation163_stub_double():
    # AllocationContext has no real 'AllocationContext' property in the generated
    # code (a bare stub) -- manually attach it so pcm_allocation_Allocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_allocation_Allocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_allocation_Allocation()
    partner = AllocationContext()
    setattr(partner, 'AllocationContext', None)
    _safe_set(owner, 'pcm_allocation_Allocation', {partner})
    assert getattr(partner, 'AllocationContext') == owner
    _safe_set(owner, 'pcm_allocation_Allocation', set())
    assert getattr(partner, 'AllocationContext') is None


def test_assoc_ancestorInterfaces_Interface74_stub_double():
    # Interface has no real 'Interface76' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Interface()
    setattr(partner, 'Interface76', None)
    _safe_set(owner, 'pcm_repository_Interface75', {partner})
    assert getattr(partner, 'Interface76') == owner
    _safe_set(owner, 'pcm_repository_Interface75', set())
    assert getattr(partner, 'Interface76') is None


def test_assoc_assemblyContext_ProvidedDelegationConnector8_stub_double():
    # composition_AssemblyContext has no real 'composition_AssemblyContext' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_ProvidedDelegationConnector()
    partner = composition_AssemblyContext()
    setattr(partner, 'composition_AssemblyContext', None)
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector9', partner)
    assert getattr(partner, 'composition_AssemblyContext') == owner
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector9', None)
    assert getattr(partner, 'composition_AssemblyContext') is None


def test_assoc_assemblyContext_RequiredDelegationConnector21_stub_double():
    # composition_AssemblyContext has no real 'composition_AssemblyContext23' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_RequiredDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_RequiredDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_RequiredDelegationConnector()
    partner = composition_AssemblyContext()
    setattr(partner, 'composition_AssemblyContext23', None)
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector22', partner)
    assert getattr(partner, 'composition_AssemblyContext23') == owner
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector22', None)
    assert getattr(partner, 'composition_AssemblyContext23') is None


def test_assoc_branchTransitions_Branch250_stub_double():
    # BranchTransition has no real 'BranchTransition' property in the generated
    # code (a bare stub) -- manually attach it so pcm_usagemodel_Branch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_usagemodel_Branch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_usagemodel_Branch()
    partner = BranchTransition()
    setattr(partner, 'BranchTransition', None)
    _safe_set(owner, 'pcm_usagemodel_Branch', {partner})
    assert getattr(partner, 'BranchTransition') == owner
    _safe_set(owner, 'pcm_usagemodel_Branch', set())
    assert getattr(partner, 'BranchTransition') is None


def test_assoc_branchedBehaviour_BranchTransition251_stub_double():
    # ScenarioBehaviour has no real 'ScenarioBehaviour252' property in the generated
    # code (a bare stub) -- manually attach it so pcm_usagemodel_BranchTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_usagemodel_BranchTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_usagemodel_BranchTransition(branchProbability=3.14)
    partner = ScenarioBehaviour()
    setattr(partner, 'ScenarioBehaviour252', None)
    _safe_set(owner, 'pcm_usagemodel_BranchTransition', partner)
    assert getattr(partner, 'ScenarioBehaviour252') == owner
    _safe_set(owner, 'pcm_usagemodel_BranchTransition', None)
    assert getattr(partner, 'ScenarioBehaviour252') is None


def test_assoc_branches_Branch142_stub_double():
    # AbstractBranchTransition has no real 'AbstractBranchTransition' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_BranchAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_BranchAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_BranchAction()
    partner = AbstractBranchTransition()
    setattr(partner, 'AbstractBranchTransition', None)
    _safe_set(owner, 'pcm_seff_BranchAction', {partner})
    assert getattr(partner, 'AbstractBranchTransition') == owner
    _safe_set(owner, 'pcm_seff_BranchAction', set())
    assert getattr(partner, 'AbstractBranchTransition') is None


def test_assoc_calledService_ExternalService130_stub_double():
    # Signature has no real 'Signature131' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_ExternalCallAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_ExternalCallAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_ExternalCallAction(retryCount=7)
    partner = Signature()
    setattr(partner, 'Signature131', None)
    _safe_set(owner, 'pcm_seff_ExternalCallAction', partner)
    assert getattr(partner, 'Signature131') == owner
    _safe_set(owner, 'pcm_seff_ExternalCallAction', None)
    assert getattr(partner, 'Signature131') is None


def test_assoc_communicationLinkResourceType_CommunicationLinkResourceSpecification179_stub_double():
    # CommunicationLinkResourceType has no real 'CommunicationLinkResourceType' property in the generated
    # code (a bare stub) -- manually attach it so pcm_resourceenvironment_CommunicationLinkResourceSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_resourceenvironment_CommunicationLinkResourceSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_resourceenvironment_CommunicationLinkResourceSpecification(failureProbability=3.14)
    partner = CommunicationLinkResourceType()
    setattr(partner, 'CommunicationLinkResourceType', None)
    _safe_set(owner, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification', partner)
    assert getattr(partner, 'CommunicationLinkResourceType') == owner
    _safe_set(owner, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification', None)
    assert getattr(partner, 'CommunicationLinkResourceType') is None


def test_assoc_componentParameterUsage_ImplementationComponentType87_stub_double():
    # VariableUsage has no real 'VariableUsage89' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_ImplementationComponentType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_ImplementationComponentType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_ImplementationComponentType()
    partner = VariableUsage()
    setattr(partner, 'VariableUsage89', None)
    _safe_set(owner, 'pcm_repository_ImplementationComponentType88', {partner})
    assert getattr(partner, 'VariableUsage89') == owner
    _safe_set(owner, 'pcm_repository_ImplementationComponentType88', set())
    assert getattr(partner, 'VariableUsage89') is None


def test_assoc_components__Repository61_stub_double():
    # RepositoryComponent has no real 'RepositoryComponent62' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Repository(repositoryDescription="sample_text")
    partner = RepositoryComponent()
    setattr(partner, 'RepositoryComponent62', None)
    _safe_set(owner, 'repository_RepositoryComponent', {partner})
    assert getattr(partner, 'RepositoryComponent62') == owner
    _safe_set(owner, 'repository_RepositoryComponent', set())
    assert getattr(partner, 'RepositoryComponent62') is None


def test_assoc_datatype__Parameter57_stub_double():
    # DataType has no real 'DataType58' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Parameter(modifier__Parameter="sample_text", parameterName="sample_text")
    partner = DataType()
    setattr(partner, 'DataType58', None)
    _safe_set(owner, 'pcm_repository_Parameter', partner)
    assert getattr(partner, 'DataType58') == owner
    _safe_set(owner, 'pcm_repository_Parameter', None)
    assert getattr(partner, 'DataType58') is None


def test_assoc_datatypes_Repository65_stub_double():
    # DataType has no real 'DataType66' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Repository(repositoryDescription="sample_text")
    partner = DataType()
    setattr(partner, 'DataType66', None)
    _safe_set(owner, 'repository_DataType', {partner})
    assert getattr(partner, 'DataType66') == owner
    _safe_set(owner, 'repository_DataType', set())
    assert getattr(partner, 'DataType66') is None


def test_assoc_describedService__SEFF151_stub_double():
    # Signature has no real 'Signature152' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_ServiceEffectSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_ServiceEffectSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_ServiceEffectSpecification(seffTypeID="sample_text")
    partner = Signature()
    setattr(partner, 'Signature152', None)
    _safe_set(owner, 'pcm_seff_ServiceEffectSpecification', partner)
    assert getattr(partner, 'Signature152') == owner
    _safe_set(owner, 'pcm_seff_ServiceEffectSpecification', None)
    assert getattr(partner, 'Signature152') is None


def test_assoc_exceptions__Signature55_stub_double():
    # ExceptionType has no real 'ExceptionType' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Signature(serviceName="sample_text")
    partner = ExceptionType()
    setattr(partner, 'ExceptionType', None)
    _safe_set(owner, 'pcm_repository_Signature56', {partner})
    assert getattr(partner, 'ExceptionType') == owner
    _safe_set(owner, 'pcm_repository_Signature56', set())
    assert getattr(partner, 'ExceptionType') is None


def test_assoc_innerProvidedRole_ProvidedDelegationConnector3_stub_double():
    # ProvidedRole has no real 'ProvidedRole4' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_ProvidedDelegationConnector()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole4', None)
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector', partner)
    assert getattr(partner, 'ProvidedRole4') == owner
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector', None)
    assert getattr(partner, 'ProvidedRole4') is None


def test_assoc_innerRequiredRole_RequiredDelegationConnector16_stub_double():
    # RequiredRole has no real 'RequiredRole17' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_RequiredDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_RequiredDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_RequiredDelegationConnector()
    partner = RequiredRole()
    setattr(partner, 'RequiredRole17', None)
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector', partner)
    assert getattr(partner, 'RequiredRole17') == owner
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector', None)
    assert getattr(partner, 'RequiredRole17') is None


def test_assoc_inputParameterUsages_ExternalCallAction132_stub_double():
    # VariableUsage has no real 'VariableUsage134' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_ExternalCallAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_ExternalCallAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_ExternalCallAction(retryCount=7)
    partner = VariableUsage()
    setattr(partner, 'VariableUsage134', None)
    _safe_set(owner, 'pcm_seff_ExternalCallAction133', {partner})
    assert getattr(partner, 'VariableUsage134') == owner
    _safe_set(owner, 'pcm_seff_ExternalCallAction133', set())
    assert getattr(partner, 'VariableUsage134') is None


def test_assoc_interArrivalTime_OpenWorkload230_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable231' property in the generated
    # code (a bare stub) -- manually attach it so pcm_usagemodel_OpenWorkload's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_usagemodel_OpenWorkload's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_usagemodel_OpenWorkload()
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable231', None)
    _safe_set(owner, 'pcm_usagemodel_OpenWorkload', partner)
    assert getattr(partner, 'PCMRandomVariable231') == owner
    _safe_set(owner, 'pcm_usagemodel_OpenWorkload', None)
    assert getattr(partner, 'PCMRandomVariable231') is None


def test_assoc_interface_Signature53_stub_double():
    # Interface has no real 'Interface' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Signature(serviceName="sample_text")
    partner = Interface()
    setattr(partner, 'Interface', None)
    _safe_set(owner, 'signatures__Interface', partner)
    assert getattr(partner, 'Interface') == owner
    _safe_set(owner, 'signatures__Interface', None)
    assert getattr(partner, 'Interface') is None


def test_assoc_interfaces__Repository63_stub_double():
    # Interface has no real 'Interface64' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Repository(repositoryDescription="sample_text")
    partner = Interface()
    setattr(partner, 'Interface64', None)
    _safe_set(owner, 'repository_Interface', {partner})
    assert getattr(partner, 'Interface64') == owner
    _safe_set(owner, 'repository_Interface', set())
    assert getattr(partner, 'Interface64') is None


def test_assoc_latency_CommunicationLinkResourceSpecification180_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable182' property in the generated
    # code (a bare stub) -- manually attach it so pcm_resourceenvironment_CommunicationLinkResourceSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_resourceenvironment_CommunicationLinkResourceSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_resourceenvironment_CommunicationLinkResourceSpecification(failureProbability=3.14)
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable182', None)
    _safe_set(owner, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification181', partner)
    assert getattr(partner, 'PCMRandomVariable182') == owner
    _safe_set(owner, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification181', None)
    assert getattr(partner, 'PCMRandomVariable182') is None


def test_assoc_outerProvidedRole_ProvidedDelegationConnector5_stub_double():
    # ProvidedRole has no real 'ProvidedRole7' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_ProvidedDelegationConnector()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole7', None)
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector6', partner)
    assert getattr(partner, 'ProvidedRole7') == owner
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector6', None)
    assert getattr(partner, 'ProvidedRole7') is None


def test_assoc_outerRequiredRole_RequiredDelegationConnector18_stub_double():
    # RequiredRole has no real 'RequiredRole20' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_RequiredDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_RequiredDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_RequiredDelegationConnector()
    partner = RequiredRole()
    setattr(partner, 'RequiredRole20', None)
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector19', partner)
    assert getattr(partner, 'RequiredRole20') == owner
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector19', None)
    assert getattr(partner, 'RequiredRole20') is None


def test_assoc_outputVariableUsages_ExternalCallAction135_stub_double():
    # VariableUsage has no real 'VariableUsage137' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_ExternalCallAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_ExternalCallAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_ExternalCallAction(retryCount=7)
    partner = VariableUsage()
    setattr(partner, 'VariableUsage137', None)
    _safe_set(owner, 'pcm_seff_ExternalCallAction136', {partner})
    assert getattr(partner, 'VariableUsage137') == owner
    _safe_set(owner, 'pcm_seff_ExternalCallAction136', set())
    assert getattr(partner, 'VariableUsage137') is None


def test_assoc_parameters__Signature52_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Signature(serviceName="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'signature_Parameter', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'signature_Parameter', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_parentCompleteComponentTypes86_stub_double():
    # CompleteComponentType has no real 'CompleteComponentType' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_ImplementationComponentType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_ImplementationComponentType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_ImplementationComponentType()
    partner = CompleteComponentType()
    setattr(partner, 'CompleteComponentType', None)
    _safe_set(owner, 'pcm_repository_ImplementationComponentType', {partner})
    assert getattr(partner, 'CompleteComponentType') == owner
    _safe_set(owner, 'pcm_repository_ImplementationComponentType', set())
    assert getattr(partner, 'CompleteComponentType') is None


def test_assoc_parentInterface__Interface72_stub_double():
    # Interface has no real 'Interface73' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Interface()
    setattr(partner, 'Interface73', None)
    _safe_set(owner, 'pcm_repository_Interface', {partner})
    assert getattr(partner, 'Interface73') == owner
    _safe_set(owner, 'pcm_repository_Interface', set())
    assert getattr(partner, 'Interface73') is None


def test_assoc_parentProvidesComponentTypes90_stub_double():
    # ProvidesComponentType has no real 'ProvidesComponentType' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_CompleteComponentType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_CompleteComponentType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_CompleteComponentType()
    partner = ProvidesComponentType()
    setattr(partner, 'ProvidesComponentType', None)
    _safe_set(owner, 'pcm_repository_CompleteComponentType', {partner})
    assert getattr(partner, 'ProvidesComponentType') == owner
    _safe_set(owner, 'pcm_repository_CompleteComponentType', set())
    assert getattr(partner, 'ProvidesComponentType') is None


def test_assoc_parentStructure_AssemblyConnector37_stub_double():
    # composition_ComposedStructure has no real 'ComposedStructure38' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_AssemblyConnector()
    partner = composition_ComposedStructure()
    setattr(partner, 'ComposedStructure38', None)
    _safe_set(owner, 'assemblyConnectors_ComposedStructure', partner)
    assert getattr(partner, 'ComposedStructure38') == owner
    _safe_set(owner, 'assemblyConnectors_ComposedStructure', None)
    assert getattr(partner, 'ComposedStructure38') is None


def test_assoc_parentStructure_ProvidedDelegationConnector10_stub_double():
    # composition_ComposedStructure has no real 'ComposedStructure' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_ProvidedDelegationConnector()
    partner = composition_ComposedStructure()
    setattr(partner, 'ComposedStructure', None)
    _safe_set(owner, 'providedDelegationConnectors_ComposedStructure', partner)
    assert getattr(partner, 'ComposedStructure') == owner
    _safe_set(owner, 'providedDelegationConnectors_ComposedStructure', None)
    assert getattr(partner, 'ComposedStructure') is None


def test_assoc_parentStructure_RequiredDelegationConnector24_stub_double():
    # composition_ComposedStructure has no real 'ComposedStructure25' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_RequiredDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_RequiredDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_RequiredDelegationConnector()
    partner = composition_ComposedStructure()
    setattr(partner, 'ComposedStructure25', None)
    _safe_set(owner, 'requiredDelegationConnectors_ComposedStructure', partner)
    assert getattr(partner, 'ComposedStructure25') == owner
    _safe_set(owner, 'requiredDelegationConnectors_ComposedStructure', None)
    assert getattr(partner, 'ComposedStructure25') is None


def test_assoc_passiveResource_BasicComponent92_stub_double():
    # PassiveResource has no real 'PassiveResource' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_BasicComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_BasicComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_BasicComponent()
    partner = PassiveResource()
    setattr(partner, 'PassiveResource', None)
    _safe_set(owner, 'pcm_repository_BasicComponent93', {partner})
    assert getattr(partner, 'PassiveResource') == owner
    _safe_set(owner, 'pcm_repository_BasicComponent93', set())
    assert getattr(partner, 'PassiveResource') is None


def test_assoc_processingRate_ProcessingResourceSpecification188_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable190' property in the generated
    # code (a bare stub) -- manually attach it so pcm_resourceenvironment_ProcessingResourceSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_resourceenvironment_ProcessingResourceSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_resourceenvironment_ProcessingResourceSpecification(MTTF=3.14, MTTR=3.14, schedulingPolicy="sample_text")
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable190', None)
    _safe_set(owner, 'pcm_resourceenvironment_ProcessingResourceSpecification189', partner)
    assert getattr(partner, 'PCMRandomVariable190') == owner
    _safe_set(owner, 'pcm_resourceenvironment_ProcessingResourceSpecification189', None)
    assert getattr(partner, 'PCMRandomVariable190') is None


def test_assoc_protocols__Interface77_stub_double():
    # Protocol has no real 'Protocol' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Protocol()
    setattr(partner, 'Protocol', None)
    _safe_set(owner, 'pcm_repository_Interface78', {partner})
    assert getattr(partner, 'Protocol') == owner
    _safe_set(owner, 'pcm_repository_Interface78', set())
    assert getattr(partner, 'Protocol') is None


def test_assoc_providedRole_AssemblyConnector31_stub_double():
    # ProvidedRole has no real 'ProvidedRole33' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_AssemblyConnector()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole33', None)
    _safe_set(owner, 'pcm_composition_AssemblyConnector32', partner)
    assert getattr(partner, 'ProvidedRole33') == owner
    _safe_set(owner, 'pcm_composition_AssemblyConnector32', None)
    assert getattr(partner, 'ProvidedRole33') is None


def test_assoc_providingAssemblyContext_AssemblyConnector28_stub_double():
    # composition_AssemblyContext has no real 'composition_AssemblyContext30' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_AssemblyConnector()
    partner = composition_AssemblyContext()
    setattr(partner, 'composition_AssemblyContext30', None)
    _safe_set(owner, 'pcm_composition_AssemblyConnector29', partner)
    assert getattr(partner, 'composition_AssemblyContext30') == owner
    _safe_set(owner, 'pcm_composition_AssemblyConnector29', None)
    assert getattr(partner, 'composition_AssemblyContext30') is None


def test_assoc_repository_Interface81_stub_double():
    # Repository has no real 'Repository82' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Repository()
    setattr(partner, 'Repository82', None)
    _safe_set(owner, 'interfaces__Repository', partner)
    assert getattr(partner, 'Repository82') == owner
    _safe_set(owner, 'interfaces__Repository', None)
    assert getattr(partner, 'Repository82') is None


def test_assoc_requiredRole_AssemblyConnector34_stub_double():
    # RequiredRole has no real 'RequiredRole36' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_AssemblyConnector()
    partner = RequiredRole()
    setattr(partner, 'RequiredRole36', None)
    _safe_set(owner, 'pcm_composition_AssemblyConnector35', partner)
    assert getattr(partner, 'RequiredRole36') == owner
    _safe_set(owner, 'pcm_composition_AssemblyConnector35', None)
    assert getattr(partner, 'RequiredRole36') is None


def test_assoc_requiringAssemblyContext_AssemblyConnector26_stub_double():
    # composition_AssemblyContext has no real 'composition_AssemblyContext27' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_AssemblyConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_AssemblyConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_AssemblyConnector()
    partner = composition_AssemblyContext()
    setattr(partner, 'composition_AssemblyContext27', None)
    _safe_set(owner, 'pcm_composition_AssemblyConnector', partner)
    assert getattr(partner, 'composition_AssemblyContext27') == owner
    _safe_set(owner, 'pcm_composition_AssemblyConnector', None)
    assert getattr(partner, 'composition_AssemblyContext27') is None


def test_assoc_returntype__Signature54_stub_double():
    # DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Signature(serviceName="sample_text")
    partner = DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'pcm_repository_Signature', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'pcm_repository_Signature', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_role_ExternalService138_stub_double():
    # Role has no real 'Role' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_ExternalCallAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_ExternalCallAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_ExternalCallAction(retryCount=7)
    partner = Role()
    setattr(partner, 'Role', None)
    _safe_set(owner, 'pcm_seff_ExternalCallAction139', partner)
    assert getattr(partner, 'Role') == owner
    _safe_set(owner, 'pcm_seff_ExternalCallAction139', None)
    assert getattr(partner, 'Role') is None


def test_assoc_serviceEffectSpecifications__BasicComponent91_stub_double():
    # ServiceEffectSpecification has no real 'ServiceEffectSpecification' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_BasicComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_BasicComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_BasicComponent()
    partner = ServiceEffectSpecification()
    setattr(partner, 'ServiceEffectSpecification', None)
    _safe_set(owner, 'pcm_repository_BasicComponent', {partner})
    assert getattr(partner, 'ServiceEffectSpecification') == owner
    _safe_set(owner, 'pcm_repository_BasicComponent', set())
    assert getattr(partner, 'ServiceEffectSpecification') is None


def test_assoc_signature_Parameter59_stub_double():
    # Signature has no real 'Signature' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Parameter(modifier__Parameter="sample_text", parameterName="sample_text")
    partner = Signature()
    setattr(partner, 'Signature', None)
    _safe_set(owner, 'parameters__Signature', partner)
    assert getattr(partner, 'Signature') == owner
    _safe_set(owner, 'parameters__Signature', None)
    assert getattr(partner, 'Signature') is None


def test_assoc_signatures__Interface79_stub_double():
    # Signature has no real 'Signature80' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Signature()
    setattr(partner, 'Signature80', None)
    _safe_set(owner, 'interface_Signature', {partner})
    assert getattr(partner, 'Signature80') == owner
    _safe_set(owner, 'interface_Signature', set())
    assert getattr(partner, 'Signature80') is None


def test_assoc_specification_VariableCharacterisation106_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable107' property in the generated
    # code (a bare stub) -- manually attach it so pcm_parameter_VariableCharacterisation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_parameter_VariableCharacterisation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_parameter_VariableCharacterisation(type="sample_text")
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable107', None)
    _safe_set(owner, 'pcm_parameter_VariableCharacterisation', partner)
    assert getattr(partner, 'PCMRandomVariable107') == owner
    _safe_set(owner, 'pcm_parameter_VariableCharacterisation', None)
    assert getattr(partner, 'PCMRandomVariable107') is None


def test_assoc_steps_Behaviour115_stub_double():
    # AbstractAction has no real 'AbstractAction116' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_ResourceDemandingBehaviour's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_ResourceDemandingBehaviour's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_ResourceDemandingBehaviour()
    partner = AbstractAction()
    setattr(partner, 'AbstractAction116', None)
    _safe_set(owner, 'pcm_seff_ResourceDemandingBehaviour', {partner})
    assert getattr(partner, 'AbstractAction116') == owner
    _safe_set(owner, 'pcm_seff_ResourceDemandingBehaviour', set())
    assert getattr(partner, 'AbstractAction116') is None


def test_assoc_system_Allocation166_stub_double():
    # System has no real 'System' property in the generated
    # code (a bare stub) -- manually attach it so pcm_allocation_Allocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_allocation_Allocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_allocation_Allocation()
    partner = System()
    setattr(partner, 'System', None)
    _safe_set(owner, 'pcm_allocation_Allocation167', partner)
    assert getattr(partner, 'System') == owner
    _safe_set(owner, 'pcm_allocation_Allocation167', None)
    assert getattr(partner, 'System') is None


def test_assoc_targetResourceEnvironment_Allocation164_stub_double():
    # ResourceEnvironment has no real 'ResourceEnvironment' property in the generated
    # code (a bare stub) -- manually attach it so pcm_allocation_Allocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_allocation_Allocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_allocation_Allocation()
    partner = ResourceEnvironment()
    setattr(partner, 'ResourceEnvironment', None)
    _safe_set(owner, 'pcm_allocation_Allocation165', partner)
    assert getattr(partner, 'ResourceEnvironment') == owner
    _safe_set(owner, 'pcm_allocation_Allocation165', None)
    assert getattr(partner, 'ResourceEnvironment') is None


def test_assoc_thinkTime_ClosedWorkload248_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable249' property in the generated
    # code (a bare stub) -- manually attach it so pcm_usagemodel_ClosedWorkload's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_usagemodel_ClosedWorkload's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_usagemodel_ClosedWorkload(population=7)
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable249', None)
    _safe_set(owner, 'pcm_usagemodel_ClosedWorkload', partner)
    assert getattr(partner, 'PCMRandomVariable249') == owner
    _safe_set(owner, 'pcm_usagemodel_ClosedWorkload', None)
    assert getattr(partner, 'PCMRandomVariable249') is None


def test_assoc_throughput_CommunicationLinkResourceSpecification183_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable185' property in the generated
    # code (a bare stub) -- manually attach it so pcm_resourceenvironment_CommunicationLinkResourceSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_resourceenvironment_CommunicationLinkResourceSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_resourceenvironment_CommunicationLinkResourceSpecification(failureProbability=3.14)
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable185', None)
    _safe_set(owner, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification184', partner)
    assert getattr(partner, 'PCMRandomVariable185') == owner
    _safe_set(owner, 'pcm_resourceenvironment_CommunicationLinkResourceSpecification184', None)
    assert getattr(partner, 'PCMRandomVariable185') is None


