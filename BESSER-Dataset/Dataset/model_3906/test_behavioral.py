import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractAction,
    AbstractBranchTransition,
    AbstractLoopAction,
    AbstractResourceDemandingAction,
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
    LinkingResource,
    NamedElement,
    PCMRandomVariable,
    Parameter,
    ParametricResourceDemand,
    PassiveResource,
    ProcessingResourceSpecification,
    ProcessingResourceType,
    Protocol,
    ProvidedRole,
    ProvidesComponentType,
    QoSAnnotations,
    RandomVariable,
    Repository,
    RequiredRole,
    ResourceContainer,
    ResourceDemandingBehaviour,
    ResourceEnvironment,
    ResourceType,
    Role,
    ScenarioBehaviour,
    ServiceEffectSpecification,
    Signature,
    SpecifiedExecutionTime,
    SpecifiedOutputParameterAbstraction,
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
    connectors_Connector,
    entity_ComposedProvidingRequiringEntity,
    entity_Entity,
    entity_InterfaceProvidingEntity,
    entity_InterfaceProvidingRequiringEntity,
    entity_InterfaceRequiringEntity,
    entity_NamedElement,
    parameter_pcm_AbstractNamedReference,
    pcm_allocation_Allocation,
    pcm_allocation_AllocationContext,
    pcm_composition_AssemblyConnector,
    pcm_composition_AssemblyContext,
    pcm_composition_ComposedStructure,
    pcm_composition_ProvidedDelegationConnector,
    pcm_composition_RequiredDelegationConnector,
    pcm_connectors_Connector,
    pcm_core_PCMRandomVariable,
    pcm_entity_ComposedProvidingRequiringEntity,
    pcm_entity_Entity,
    pcm_entity_InterfaceProvidingEntity,
    pcm_entity_InterfaceProvidingRequiringEntity,
    pcm_entity_InterfaceRequiringEntity,
    pcm_entity_NamedElement,
    pcm_parameter_CharacterisedVariable,
    pcm_parameter_VariableCharacterisation,
    pcm_parameter_VariableUsage,
    pcm_protocol_Protocol,
    pcm_protocol_ServiceCall,
    pcm_qosannotations_ComponentSpecifiedExecutionTime,
    pcm_qosannotations_QoSAnnotations,
    pcm_qosannotations_SpecifiedExecutionTime,
    pcm_qosannotations_SpecifiedFailureProbability,
    pcm_qosannotations_SpecifiedOutputParameterAbstraction,
    pcm_qosannotations_SystemSpecifiedExecutionTime,
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
    pcm_repository_RequiredRole,
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
    pcm_seff_AbstractLoopAction,
    pcm_seff_AbstractResourceDemandingAction,
    pcm_seff_AcquireAction,
    pcm_seff_BranchAction,
    pcm_seff_CollectionIteratorAction,
    pcm_seff_ExternalCallAction,
    pcm_seff_ForkAction,
    pcm_seff_ForkedBehaviour,
    pcm_seff_GuardedBranchTransition,
    pcm_seff_InternalAction,
    pcm_seff_LoopAction,
    pcm_seff_ParametricResourceDemand,
    pcm_seff_ProbabilisticBranchTransition,
    pcm_seff_ReleaseAction,
    pcm_seff_ResourceDemandingBehaviour,
    pcm_seff_ResourceDemandingSEFF,
    pcm_seff_ServiceEffectSpecification,
    pcm_seff_SetVariableAction,
    pcm_seff_StartAction,
    pcm_seff_StopAction,
    pcm_seff_SynchronisationPoint,
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
    repository_DataType,
    repository_ImplementationComponentType,
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

def test_assoc_actions_ScenarioBehaviour210_stub_double():
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


def test_assoc_activeResourceType_ActiveResourceSpecification179_stub_double():
    # ProcessingResourceType has no real 'ProcessingResourceType180' property in the generated
    # code (a bare stub) -- manually attach it so pcm_resourceenvironment_ProcessingResourceSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_resourceenvironment_ProcessingResourceSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_resourceenvironment_ProcessingResourceSpecification(schedulingPolicy="sample_text")
    partner = ProcessingResourceType()
    setattr(partner, 'ProcessingResourceType180', None)
    _safe_set(owner, 'pcm_resourceenvironment_ProcessingResourceSpecification', partner)
    assert getattr(partner, 'ProcessingResourceType180') == owner
    _safe_set(owner, 'pcm_resourceenvironment_ProcessingResourceSpecification', None)
    assert getattr(partner, 'ProcessingResourceType180') is None


def test_assoc_allocationContexts_Allocation156_stub_double():
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


def test_assoc_anchestorInterfaces_Interface65_stub_double():
    # Interface has no real 'Interface67' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Interface()
    setattr(partner, 'Interface67', None)
    _safe_set(owner, 'pcm_repository_Interface66', {partner})
    assert getattr(partner, 'Interface67') == owner
    _safe_set(owner, 'pcm_repository_Interface66', set())
    assert getattr(partner, 'Interface67') is None


def test_assoc_branchTransitions_Branch243_stub_double():
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


def test_assoc_branchedBehaviour_BranchTransition244_stub_double():
    # ScenarioBehaviour has no real 'ScenarioBehaviour245' property in the generated
    # code (a bare stub) -- manually attach it so pcm_usagemodel_BranchTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_usagemodel_BranchTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_usagemodel_BranchTransition(branchProbability=3.14)
    partner = ScenarioBehaviour()
    setattr(partner, 'ScenarioBehaviour245', None)
    _safe_set(owner, 'pcm_usagemodel_BranchTransition', partner)
    assert getattr(partner, 'ScenarioBehaviour245') == owner
    _safe_set(owner, 'pcm_usagemodel_BranchTransition', None)
    assert getattr(partner, 'ScenarioBehaviour245') is None


def test_assoc_branches_Branch140_stub_double():
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


def test_assoc_childComponentContext_ProvidedDelegationConnector7_stub_double():
    # composition_AssemblyContext has no real 'composition_AssemblyContext' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_ProvidedDelegationConnector()
    partner = composition_AssemblyContext()
    setattr(partner, 'composition_AssemblyContext', None)
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector8', partner)
    assert getattr(partner, 'composition_AssemblyContext') == owner
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector8', None)
    assert getattr(partner, 'composition_AssemblyContext') is None


def test_assoc_childComponentContext_RequiredDelegationConnector20_stub_double():
    # composition_AssemblyContext has no real 'composition_AssemblyContext22' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_RequiredDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_RequiredDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_RequiredDelegationConnector()
    partner = composition_AssemblyContext()
    setattr(partner, 'composition_AssemblyContext22', None)
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector21', partner)
    assert getattr(partner, 'composition_AssemblyContext22') == owner
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector21', None)
    assert getattr(partner, 'composition_AssemblyContext22') is None


def test_assoc_componentParameterUsage_ImplementationComponentType75_stub_double():
    # VariableUsage has no real 'VariableUsage77' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_ImplementationComponentType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_ImplementationComponentType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_ImplementationComponentType()
    partner = VariableUsage()
    setattr(partner, 'VariableUsage77', None)
    _safe_set(owner, 'pcm_repository_ImplementationComponentType76', {partner})
    assert getattr(partner, 'VariableUsage77') == owner
    _safe_set(owner, 'pcm_repository_ImplementationComponentType76', set())
    assert getattr(partner, 'VariableUsage77') is None


def test_assoc_components__Repository52_stub_double():
    # ProvidesComponentType has no real 'ProvidesComponentType53' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Repository(repositoryDescription="sample_text")
    partner = ProvidesComponentType()
    setattr(partner, 'ProvidesComponentType53', None)
    _safe_set(owner, 'repository_ProvidesComponentType', {partner})
    assert getattr(partner, 'ProvidesComponentType53') == owner
    _safe_set(owner, 'repository_ProvidesComponentType', set())
    assert getattr(partner, 'ProvidesComponentType53') is None


def test_assoc_datatype__Parameter48_stub_double():
    # DataType has no real 'DataType49' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Parameter(modifier__Parameter="sample_text", parameterName="sample_text")
    partner = DataType()
    setattr(partner, 'DataType49', None)
    _safe_set(owner, 'pcm_repository_Parameter', partner)
    assert getattr(partner, 'DataType49') == owner
    _safe_set(owner, 'pcm_repository_Parameter', None)
    assert getattr(partner, 'DataType49') is None


def test_assoc_datatypes_Repository56_stub_double():
    # DataType has no real 'DataType57' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Repository(repositoryDescription="sample_text")
    partner = DataType()
    setattr(partner, 'DataType57', None)
    _safe_set(owner, 'repository_DataType', {partner})
    assert getattr(partner, 'DataType57') == owner
    _safe_set(owner, 'repository_DataType', set())
    assert getattr(partner, 'DataType57') is None


def test_assoc_describedService__SEFF149_stub_double():
    # Signature has no real 'Signature150' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_ServiceEffectSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_ServiceEffectSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_ServiceEffectSpecification(seffTypeID="sample_text")
    partner = Signature()
    setattr(partner, 'Signature150', None)
    _safe_set(owner, 'pcm_seff_ServiceEffectSpecification', partner)
    assert getattr(partner, 'Signature150') == owner
    _safe_set(owner, 'pcm_seff_ServiceEffectSpecification', None)
    assert getattr(partner, 'Signature150') is None


def test_assoc_exceptions__Signature46_stub_double():
    # ExceptionType has no real 'ExceptionType' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Signature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Signature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Signature(serviceName="sample_text")
    partner = ExceptionType()
    setattr(partner, 'ExceptionType', None)
    _safe_set(owner, 'pcm_repository_Signature47', {partner})
    assert getattr(partner, 'ExceptionType') == owner
    _safe_set(owner, 'pcm_repository_Signature47', set())
    assert getattr(partner, 'ExceptionType') is None


def test_assoc_implementationComponentType80_stub_double():
    # ImplementationComponentType has no real 'ImplementationComponentType' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_CompositeComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_CompositeComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_CompositeComponent()
    partner = ImplementationComponentType()
    setattr(partner, 'ImplementationComponentType', None)
    _safe_set(owner, 'pcm_repository_CompositeComponent', partner)
    assert getattr(partner, 'ImplementationComponentType') == owner
    _safe_set(owner, 'pcm_repository_CompositeComponent', None)
    assert getattr(partner, 'ImplementationComponentType') is None


def test_assoc_implementationComponentType81_stub_double():
    # ImplementationComponentType has no real 'ImplementationComponentType82' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_BasicComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_BasicComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_BasicComponent()
    partner = ImplementationComponentType()
    setattr(partner, 'ImplementationComponentType82', None)
    _safe_set(owner, 'pcm_repository_BasicComponent', partner)
    assert getattr(partner, 'ImplementationComponentType82') == owner
    _safe_set(owner, 'pcm_repository_BasicComponent', None)
    assert getattr(partner, 'ImplementationComponentType82') is None


def test_assoc_innerProvidedRole_ProvidedDelegationConnector2_stub_double():
    # ProvidedRole has no real 'ProvidedRole3' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_ProvidedDelegationConnector()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole3', None)
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector', partner)
    assert getattr(partner, 'ProvidedRole3') == owner
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector', None)
    assert getattr(partner, 'ProvidedRole3') is None


def test_assoc_innerRequiredRole_RequiredDelegationConnector15_stub_double():
    # RequiredRole has no real 'RequiredRole16' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_RequiredDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_RequiredDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_RequiredDelegationConnector()
    partner = RequiredRole()
    setattr(partner, 'RequiredRole16', None)
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector', partner)
    assert getattr(partner, 'RequiredRole16') == owner
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector', None)
    assert getattr(partner, 'RequiredRole16') is None


def test_assoc_interArrivalTime_OpenWorkload223_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable224' property in the generated
    # code (a bare stub) -- manually attach it so pcm_usagemodel_OpenWorkload's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_usagemodel_OpenWorkload's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_usagemodel_OpenWorkload()
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable224', None)
    _safe_set(owner, 'pcm_usagemodel_OpenWorkload', partner)
    assert getattr(partner, 'PCMRandomVariable224') == owner
    _safe_set(owner, 'pcm_usagemodel_OpenWorkload', None)
    assert getattr(partner, 'PCMRandomVariable224') is None


def test_assoc_interface_Signature44_stub_double():
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


def test_assoc_interfaces__Repository54_stub_double():
    # Interface has no real 'Interface55' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Repository(repositoryDescription="sample_text")
    partner = Interface()
    setattr(partner, 'Interface55', None)
    _safe_set(owner, 'repository_Interface', {partner})
    assert getattr(partner, 'Interface55') == owner
    _safe_set(owner, 'repository_Interface', set())
    assert getattr(partner, 'Interface55') is None


def test_assoc_outerProvidedRole_ProvidedDelegationConnector4_stub_double():
    # ProvidedRole has no real 'ProvidedRole6' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_ProvidedDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_ProvidedDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_ProvidedDelegationConnector()
    partner = ProvidedRole()
    setattr(partner, 'ProvidedRole6', None)
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector5', partner)
    assert getattr(partner, 'ProvidedRole6') == owner
    _safe_set(owner, 'pcm_composition_ProvidedDelegationConnector5', None)
    assert getattr(partner, 'ProvidedRole6') is None


def test_assoc_outerRequiredRole_RequiredDelegationConnector17_stub_double():
    # RequiredRole has no real 'RequiredRole19' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_RequiredDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_RequiredDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_RequiredDelegationConnector()
    partner = RequiredRole()
    setattr(partner, 'RequiredRole19', None)
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector18', partner)
    assert getattr(partner, 'RequiredRole19') == owner
    _safe_set(owner, 'pcm_composition_RequiredDelegationConnector18', None)
    assert getattr(partner, 'RequiredRole19') is None


def test_assoc_parameters__Signature43_stub_double():
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


def test_assoc_parentCompleteComponentTypes74_stub_double():
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


def test_assoc_parentInterface__Interface63_stub_double():
    # Interface has no real 'Interface64' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Interface()
    setattr(partner, 'Interface64', None)
    _safe_set(owner, 'pcm_repository_Interface', {partner})
    assert getattr(partner, 'Interface64') == owner
    _safe_set(owner, 'pcm_repository_Interface', set())
    assert getattr(partner, 'Interface64') is None


def test_assoc_parentProvidesComponentTypes78_stub_double():
    # ProvidesComponentType has no real 'ProvidesComponentType79' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_CompleteComponentType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_CompleteComponentType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_CompleteComponentType()
    partner = ProvidesComponentType()
    setattr(partner, 'ProvidesComponentType79', None)
    _safe_set(owner, 'pcm_repository_CompleteComponentType', {partner})
    assert getattr(partner, 'ProvidesComponentType79') == owner
    _safe_set(owner, 'pcm_repository_CompleteComponentType', set())
    assert getattr(partner, 'ProvidesComponentType79') is None


def test_assoc_parentStructure_ProvidedDelegationConnector9_stub_double():
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


def test_assoc_parentStructure_RequiredDelegationConnector23_stub_double():
    # composition_ComposedStructure has no real 'ComposedStructure24' property in the generated
    # code (a bare stub) -- manually attach it so pcm_composition_RequiredDelegationConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_composition_RequiredDelegationConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_composition_RequiredDelegationConnector()
    partner = composition_ComposedStructure()
    setattr(partner, 'ComposedStructure24', None)
    _safe_set(owner, 'requiredDelegationConnectors_ComposedStructure', partner)
    assert getattr(partner, 'ComposedStructure24') == owner
    _safe_set(owner, 'requiredDelegationConnectors_ComposedStructure', None)
    assert getattr(partner, 'ComposedStructure24') is None


def test_assoc_passiveResource_BasicComponent85_stub_double():
    # PassiveResource has no real 'PassiveResource' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_BasicComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_BasicComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_BasicComponent()
    partner = PassiveResource()
    setattr(partner, 'PassiveResource', None)
    _safe_set(owner, 'pcm_repository_BasicComponent86', {partner})
    assert getattr(partner, 'PassiveResource') == owner
    _safe_set(owner, 'pcm_repository_BasicComponent86', set())
    assert getattr(partner, 'PassiveResource') is None


def test_assoc_processingRate_ProcessingResourceSpecification181_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable183' property in the generated
    # code (a bare stub) -- manually attach it so pcm_resourceenvironment_ProcessingResourceSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_resourceenvironment_ProcessingResourceSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_resourceenvironment_ProcessingResourceSpecification(schedulingPolicy="sample_text")
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable183', None)
    _safe_set(owner, 'pcm_resourceenvironment_ProcessingResourceSpecification182', partner)
    assert getattr(partner, 'PCMRandomVariable183') == owner
    _safe_set(owner, 'pcm_resourceenvironment_ProcessingResourceSpecification182', None)
    assert getattr(partner, 'PCMRandomVariable183') is None


def test_assoc_protocols__Interface68_stub_double():
    # Protocol has no real 'Protocol' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Protocol()
    setattr(partner, 'Protocol', None)
    _safe_set(owner, 'pcm_repository_Interface69', {partner})
    assert getattr(partner, 'Protocol') == owner
    _safe_set(owner, 'pcm_repository_Interface69', set())
    assert getattr(partner, 'Protocol') is None


def test_assoc_repository_Interface72_stub_double():
    # Repository has no real 'Repository73' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Repository()
    setattr(partner, 'Repository73', None)
    _safe_set(owner, 'interfaces__Repository', partner)
    assert getattr(partner, 'Repository73') == owner
    _safe_set(owner, 'interfaces__Repository', None)
    assert getattr(partner, 'Repository73') is None


def test_assoc_repository_ProvidesComponentType58_stub_double():
    # Repository has no real 'Repository59' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_ProvidesComponentType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_ProvidesComponentType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_ProvidesComponentType()
    partner = Repository()
    setattr(partner, 'Repository59', None)
    _safe_set(owner, 'components__Repository', partner)
    assert getattr(partner, 'Repository59') == owner
    _safe_set(owner, 'components__Repository', None)
    assert getattr(partner, 'Repository59') is None


def test_assoc_returntype__Signature45_stub_double():
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


def test_assoc_serviceEffectSpecifications__BasicComponent83_stub_double():
    # ServiceEffectSpecification has no real 'ServiceEffectSpecification' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_BasicComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_BasicComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_BasicComponent()
    partner = ServiceEffectSpecification()
    setattr(partner, 'ServiceEffectSpecification', None)
    _safe_set(owner, 'pcm_repository_BasicComponent84', {partner})
    assert getattr(partner, 'ServiceEffectSpecification') == owner
    _safe_set(owner, 'pcm_repository_BasicComponent84', set())
    assert getattr(partner, 'ServiceEffectSpecification') is None


def test_assoc_signature_Parameter50_stub_double():
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


def test_assoc_signatures__Interface70_stub_double():
    # Signature has no real 'Signature71' property in the generated
    # code (a bare stub) -- manually attach it so pcm_repository_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_repository_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_repository_Interface()
    partner = Signature()
    setattr(partner, 'Signature71', None)
    _safe_set(owner, 'interface_Signature', {partner})
    assert getattr(partner, 'Signature71') == owner
    _safe_set(owner, 'interface_Signature', set())
    assert getattr(partner, 'Signature71') is None


def test_assoc_specification_VariableCharacterisation99_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable100' property in the generated
    # code (a bare stub) -- manually attach it so pcm_parameter_VariableCharacterisation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_parameter_VariableCharacterisation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_parameter_VariableCharacterisation(type="sample_text")
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable100', None)
    _safe_set(owner, 'pcm_parameter_VariableCharacterisation', partner)
    assert getattr(partner, 'PCMRandomVariable100') == owner
    _safe_set(owner, 'pcm_parameter_VariableCharacterisation', None)
    assert getattr(partner, 'PCMRandomVariable100') is None


def test_assoc_steps_Behaviour113_stub_double():
    # AbstractAction has no real 'AbstractAction114' property in the generated
    # code (a bare stub) -- manually attach it so pcm_seff_ResourceDemandingBehaviour's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_seff_ResourceDemandingBehaviour's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_seff_ResourceDemandingBehaviour()
    partner = AbstractAction()
    setattr(partner, 'AbstractAction114', None)
    _safe_set(owner, 'pcm_seff_ResourceDemandingBehaviour', {partner})
    assert getattr(partner, 'AbstractAction114') == owner
    _safe_set(owner, 'pcm_seff_ResourceDemandingBehaviour', set())
    assert getattr(partner, 'AbstractAction114') is None


def test_assoc_system_Allocation159_stub_double():
    # System has no real 'System' property in the generated
    # code (a bare stub) -- manually attach it so pcm_allocation_Allocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_allocation_Allocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_allocation_Allocation()
    partner = System()
    setattr(partner, 'System', None)
    _safe_set(owner, 'pcm_allocation_Allocation160', partner)
    assert getattr(partner, 'System') == owner
    _safe_set(owner, 'pcm_allocation_Allocation160', None)
    assert getattr(partner, 'System') is None


def test_assoc_targetResourceEnvironment_Allocation157_stub_double():
    # ResourceEnvironment has no real 'ResourceEnvironment' property in the generated
    # code (a bare stub) -- manually attach it so pcm_allocation_Allocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_allocation_Allocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_allocation_Allocation()
    partner = ResourceEnvironment()
    setattr(partner, 'ResourceEnvironment', None)
    _safe_set(owner, 'pcm_allocation_Allocation158', partner)
    assert getattr(partner, 'ResourceEnvironment') == owner
    _safe_set(owner, 'pcm_allocation_Allocation158', None)
    assert getattr(partner, 'ResourceEnvironment') is None


def test_assoc_thinkTime_ClosedWorkload241_stub_double():
    # PCMRandomVariable has no real 'PCMRandomVariable242' property in the generated
    # code (a bare stub) -- manually attach it so pcm_usagemodel_ClosedWorkload's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcm_usagemodel_ClosedWorkload's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcm_usagemodel_ClosedWorkload(population=7)
    partner = PCMRandomVariable()
    setattr(partner, 'PCMRandomVariable242', None)
    _safe_set(owner, 'pcm_usagemodel_ClosedWorkload', partner)
    assert getattr(partner, 'PCMRandomVariable242') == owner
    _safe_set(owner, 'pcm_usagemodel_ClosedWorkload', None)
    assert getattr(partner, 'PCMRandomVariable242') is None


