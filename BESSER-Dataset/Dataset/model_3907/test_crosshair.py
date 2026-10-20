from python_code import ResourceEnvironment
from python_code import System
from python_code import pcm_allocation_Allocation

def test_pcm_allocation_Allocation___init__():
    assert pcm_allocation_Allocation.__init__(pcm_allocation_Allocation(pcm_allocation_Allocation=set(), pcm_allocation_Allocation165=ResourceEnvironment(), pcm_allocation_Allocation167=System()), pcm_allocation_Allocation=set(), pcm_allocation_Allocation165=ResourceEnvironment(), pcm_allocation_Allocation167=System()) == None

def test_pcm_allocation_Allocation_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce():
    assert pcm_allocation_Allocation.EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(pcm_allocation_Allocation(pcm_allocation_Allocation=set(), pcm_allocation_Allocation165=ResourceEnvironment(), pcm_allocation_Allocation167=System()), 0, '\x00\x00') == None


from python_code import ProvidedRole
from python_code import RequiredRole
from python_code import composition_AssemblyContext
from python_code import composition_ComposedStructure
from python_code import pcm_composition_AssemblyConnector

def test_pcm_composition_AssemblyConnector___init__():
    assert pcm_composition_AssemblyConnector.__init__(pcm_composition_AssemblyConnector(pcm_composition_AssemblyConnector=composition_AssemblyContext(), pcm_composition_AssemblyConnector29=composition_AssemblyContext(), pcm_composition_AssemblyConnector32=ProvidedRole(), pcm_composition_AssemblyConnector35=RequiredRole(), assemblyConnectors_ComposedStructure=composition_ComposedStructure()), pcm_composition_AssemblyConnector=composition_AssemblyContext(), pcm_composition_AssemblyConnector29=composition_AssemblyContext(), pcm_composition_AssemblyConnector32=ProvidedRole(), pcm_composition_AssemblyConnector35=RequiredRole(), assemblyConnectors_ComposedStructure=composition_ComposedStructure()) == None

def test_pcm_composition_AssemblyConnector_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch():
    assert pcm_composition_AssemblyConnector.AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(pcm_composition_AssemblyConnector(pcm_composition_AssemblyConnector=composition_AssemblyContext(), pcm_composition_AssemblyConnector29=composition_AssemblyContext(), pcm_composition_AssemblyConnector32=ProvidedRole(), pcm_composition_AssemblyConnector35=RequiredRole(), assemblyConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None

def test_pcm_composition_AssemblyConnector_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch():
    assert pcm_composition_AssemblyConnector.AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(pcm_composition_AssemblyConnector(pcm_composition_AssemblyConnector=composition_AssemblyContext(), pcm_composition_AssemblyConnector29=composition_AssemblyContext(), pcm_composition_AssemblyConnector32=ProvidedRole(), pcm_composition_AssemblyConnector35=RequiredRole(), assemblyConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None


from python_code import ProvidedRole
from python_code import composition_AssemblyContext
from python_code import composition_ComposedStructure
from python_code import pcm_composition_ProvidedDelegationConnector

def test_pcm_composition_ProvidedDelegationConnector___init__():
    assert pcm_composition_ProvidedDelegationConnector.__init__(pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector6=ProvidedRole(), pcm_composition_ProvidedDelegationConnector9=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector6=ProvidedRole(), pcm_composition_ProvidedDelegationConnector9=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()) == None

def test_pcm_composition_ProvidedDelegationConnector_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame():
    assert pcm_composition_ProvidedDelegationConnector.ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector6=ProvidedRole(), pcm_composition_ProvidedDelegationConnector9=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None

def test_pcm_composition_ProvidedDelegationConnector_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure():
    assert pcm_composition_ProvidedDelegationConnector.ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector6=ProvidedRole(), pcm_composition_ProvidedDelegationConnector9=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None


from python_code import RequiredRole
from python_code import composition_AssemblyContext
from python_code import composition_ComposedStructure
from python_code import pcm_composition_RequiredDelegationConnector

def test_pcm_composition_RequiredDelegationConnector___init__():
    assert pcm_composition_RequiredDelegationConnector.__init__(pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector19=RequiredRole(), pcm_composition_RequiredDelegationConnector22=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector19=RequiredRole(), pcm_composition_RequiredDelegationConnector22=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()) == None

def test_pcm_composition_RequiredDelegationConnector_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure():
    assert pcm_composition_RequiredDelegationConnector.RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector19=RequiredRole(), pcm_composition_RequiredDelegationConnector22=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None

def test_pcm_composition_RequiredDelegationConnector_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame():
    assert pcm_composition_RequiredDelegationConnector.ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector19=RequiredRole(), pcm_composition_RequiredDelegationConnector22=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None


from python_code import pcm_core_PCMRandomVariable

def test_pcm_core_PCMRandomVariable___init__():
    assert pcm_core_PCMRandomVariable.__init__(pcm_core_PCMRandomVariable()) == None

def test_pcm_core_PCMRandomVariable_SpecificationMustNotBeNULL():
    assert pcm_core_PCMRandomVariable.SpecificationMustNotBeNULL(pcm_core_PCMRandomVariable(), '', '') == None


from python_code import ProvidedRole
from python_code import RequiredRole
from python_code import composition_AssemblyContext
from python_code import composition_ComposedStructure
from python_code import pcm_composition_AssemblyConnector
from python_code import pcm_composition_AssemblyContext
from python_code import pcm_composition_ProvidedDelegationConnector
from python_code import pcm_composition_RequiredDelegationConnector
from python_code import pcm_composition_ResourceRequiredDelegationConnector
from python_code import pcm_entity_ComposedProvidingRequiringEntity

def test_pcm_entity_ComposedProvidingRequiringEntity___init__():
    assert pcm_entity_ComposedProvidingRequiringEntity.__init__(pcm_entity_ComposedProvidingRequiringEntity(ComposedStructure=pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector6=ProvidedRole(), pcm_composition_ProvidedDelegationConnector9=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), ComposedStructure25=pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector19=RequiredRole(), pcm_composition_RequiredDelegationConnector22=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), ComposedStructure13=pcm_composition_AssemblyContext(), ComposedStructure40=pcm_composition_ResourceRequiredDelegationConnector(), ComposedStructure38=pcm_composition_AssemblyConnector(pcm_composition_AssemblyConnector=composition_AssemblyContext(), pcm_composition_AssemblyConnector29=composition_AssemblyContext(), pcm_composition_AssemblyConnector32=ProvidedRole(), pcm_composition_AssemblyConnector35=RequiredRole(), assemblyConnectors_ComposedStructure=composition_ComposedStructure())), ComposedStructure=pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector6=ProvidedRole(), pcm_composition_ProvidedDelegationConnector9=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), ComposedStructure25=pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector19=RequiredRole(), pcm_composition_RequiredDelegationConnector22=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), ComposedStructure13=pcm_composition_AssemblyContext(), ComposedStructure40=pcm_composition_ResourceRequiredDelegationConnector(), ComposedStructure38=pcm_composition_AssemblyConnector(pcm_composition_AssemblyConnector=composition_AssemblyContext(), pcm_composition_AssemblyConnector29=composition_AssemblyContext(), pcm_composition_AssemblyConnector32=ProvidedRole(), pcm_composition_AssemblyConnector35=RequiredRole(), assemblyConnectors_ComposedStructure=composition_ComposedStructure())) == None

def test_pcm_entity_ComposedProvidingRequiringEntity_ProvidedRolesMustBeBound():
    assert pcm_entity_ComposedProvidingRequiringEntity.ProvidedRolesMustBeBound(pcm_entity_ComposedProvidingRequiringEntity(ComposedStructure=pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector6=ProvidedRole(), pcm_composition_ProvidedDelegationConnector9=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), ComposedStructure25=pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector19=RequiredRole(), pcm_composition_RequiredDelegationConnector22=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), ComposedStructure13=pcm_composition_AssemblyContext(), ComposedStructure40=pcm_composition_ResourceRequiredDelegationConnector(), ComposedStructure38=pcm_composition_AssemblyConnector(pcm_composition_AssemblyConnector=composition_AssemblyContext(), pcm_composition_AssemblyConnector29=composition_AssemblyContext(), pcm_composition_AssemblyConnector32=ProvidedRole(), pcm_composition_AssemblyConnector35=RequiredRole(), assemblyConnectors_ComposedStructure=composition_ComposedStructure())), 0, 0) == None


from python_code import pcm_entity_NamedElement

def test_pcm_entity_NamedElement___init__():
    assert pcm_entity_NamedElement.__init__(pcm_entity_NamedElement(''), '') == None


from python_code import pcm_parameter_CharacterisedVariable

def test_pcm_parameter_CharacterisedVariable___init__():
    assert pcm_parameter_CharacterisedVariable.__init__(pcm_parameter_CharacterisedVariable(''), '') == None


from python_code import PCMRandomVariable
from python_code import pcm_parameter_VariableCharacterisation

def test_pcm_parameter_VariableCharacterisation___init__():
    assert pcm_parameter_VariableCharacterisation.__init__(pcm_parameter_VariableCharacterisation('', pcm_parameter_VariableCharacterisation=PCMRandomVariable()), '', pcm_parameter_VariableCharacterisation=PCMRandomVariable()) == None


from python_code import pcm_protocol_Protocol

def test_pcm_protocol_Protocol___init__():
    assert pcm_protocol_Protocol.__init__(pcm_protocol_Protocol(''), '') == None


from python_code import pcm_qosannotations_QoSAnnotations
from python_code import pcm_reliability_SpecifiedFailureProbability

def test_pcm_reliability_SpecifiedFailureProbability___init__():
    assert pcm_reliability_SpecifiedFailureProbability.__init__(pcm_reliability_SpecifiedFailureProbability(0.0, SpecifiedQoSAnnotation=pcm_qosannotations_QoSAnnotations()), 0.0, SpecifiedQoSAnnotation=pcm_qosannotations_QoSAnnotations()) == None


from python_code import pcm_repository_BasicComponent

def test_pcm_repository_BasicComponent___init__():
    assert pcm_repository_BasicComponent.__init__(pcm_repository_BasicComponent(pcm_repository_BasicComponent=set(), pcm_repository_BasicComponent93=set()), pcm_repository_BasicComponent=set(), pcm_repository_BasicComponent93=set()) == None

def test_pcm_repository_BasicComponent_RequireSameInterfacesAsImplementationType():
    assert pcm_repository_BasicComponent.RequireSameInterfacesAsImplementationType(pcm_repository_BasicComponent(pcm_repository_BasicComponent=set(), pcm_repository_BasicComponent93=set()), '\x00', '') == None

def test_pcm_repository_BasicComponent_NoSeffTypeUsedTwice():
    assert pcm_repository_BasicComponent.NoSeffTypeUsedTwice(pcm_repository_BasicComponent(pcm_repository_BasicComponent=set(), pcm_repository_BasicComponent93=set()), '\x00', '') == None

def test_pcm_repository_BasicComponent_ProvideSameInterfacesAsImplementationType():
    assert pcm_repository_BasicComponent.ProvideSameInterfacesAsImplementationType(pcm_repository_BasicComponent(pcm_repository_BasicComponent=set(), pcm_repository_BasicComponent93=set()), '\x00', '') == None


from python_code import pcm_composition_AssemblyContext
from python_code import pcm_repository_CompleteComponentType
from python_code import pcm_repository_Repository

def test_pcm_repository_CompleteComponentType___init__():
    assert pcm_repository_CompleteComponentType.__init__(pcm_repository_CompleteComponentType(pcm_repository_CompleteComponentType=set(), RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()), pcm_repository_CompleteComponentType=set(), RepositoryComponent62=pcm_repository_Repository('\x00', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()) == None

def test_pcm_repository_CompleteComponentType_providedInterfacesHaveToConformToProvidedType2():
    assert pcm_repository_CompleteComponentType.providedInterfacesHaveToConformToProvidedType2(pcm_repository_CompleteComponentType(pcm_repository_CompleteComponentType=set(), RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()), '', '') == None

def test_pcm_repository_CompleteComponentType_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType():
    assert pcm_repository_CompleteComponentType.AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(pcm_repository_CompleteComponentType(pcm_repository_CompleteComponentType=set(), RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()), '', '') == None


from python_code import pcm_repository_CompositeComponent

def test_pcm_repository_CompositeComponent___init__():
    assert pcm_repository_CompositeComponent.__init__(pcm_repository_CompositeComponent()) == None

def test_pcm_repository_CompositeComponent_RequireSameInterfaces():
    assert pcm_repository_CompositeComponent.RequireSameInterfaces(pcm_repository_CompositeComponent(), '', '') == None

def test_pcm_repository_CompositeComponent_ProvideSameInterfaces():
    assert pcm_repository_CompositeComponent.ProvideSameInterfaces(pcm_repository_CompositeComponent(), '', '') == None


from python_code import pcm_repository_ExceptionType

def test_pcm_repository_ExceptionType___init__():
    assert pcm_repository_ExceptionType.__init__(pcm_repository_ExceptionType('', '\x00'), '\x00\x00', '') == None


from python_code import pcm_composition_AssemblyContext
from python_code import pcm_repository_ImplementationComponentType
from python_code import pcm_repository_Repository

def test_pcm_repository_ImplementationComponentType___init__():
    assert pcm_repository_ImplementationComponentType.__init__(pcm_repository_ImplementationComponentType(pcm_repository_ImplementationComponentType=set(), pcm_repository_ImplementationComponentType88=set(), RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()), pcm_repository_ImplementationComponentType=set(), pcm_repository_ImplementationComponentType88=set(), RepositoryComponent62=pcm_repository_Repository('\x00', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()) == None

def test_pcm_repository_ImplementationComponentType_providedInterfacesHaveToConformToCompleteType():
    assert pcm_repository_ImplementationComponentType.providedInterfacesHaveToConformToCompleteType(pcm_repository_ImplementationComponentType(pcm_repository_ImplementationComponentType=set(), pcm_repository_ImplementationComponentType88=set(), RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()), 0, '') == None

def test_pcm_repository_ImplementationComponentType_RequiredInterfacesHaveToConformToCompleteType():
    assert pcm_repository_ImplementationComponentType.RequiredInterfacesHaveToConformToCompleteType(pcm_repository_ImplementationComponentType(pcm_repository_ImplementationComponentType=set(), pcm_repository_ImplementationComponentType88=set(), RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()), 0, '') == None


from python_code import Repository
from python_code import pcm_repository_Interface

def test_pcm_repository_Interface___init__():
    assert pcm_repository_Interface.__init__(pcm_repository_Interface(pcm_repository_Interface=set(), pcm_repository_Interface78=set(), interface_Signature=set(), interfaces__Repository=Repository(), pcm_repository_Interface75=set()), pcm_repository_Interface=set(), pcm_repository_Interface78=set(), interface_Signature=set(), interfaces__Repository=Repository(), pcm_repository_Interface75=set()) == None

def test_pcm_repository_Interface_NoProtocolTypeIDUsedTwice():
    assert pcm_repository_Interface.NoProtocolTypeIDUsedTwice(pcm_repository_Interface(pcm_repository_Interface=set(), pcm_repository_Interface78=set(), interface_Signature=set(), interfaces__Repository=Repository(), pcm_repository_Interface75=set()), '', '') == None

def test_pcm_repository_Interface_SignaturesHaveToBeUniqueForAnInterface():
    assert pcm_repository_Interface.SignaturesHaveToBeUniqueForAnInterface(pcm_repository_Interface(pcm_repository_Interface=set(), pcm_repository_Interface78=set(), interface_Signature=set(), interfaces__Repository=Repository(), pcm_repository_Interface75=set()), '', '') == None


from python_code import DataType
from python_code import Signature
from python_code import pcm_repository_Parameter

def test_pcm_repository_Parameter___init__():
    assert pcm_repository_Parameter.__init__(pcm_repository_Parameter('', '', pcm_repository_Parameter=DataType(), parameters__Signature=Signature()), '', '', pcm_repository_Parameter=DataType(), parameters__Signature=Signature()) == None


from python_code import pcm_composition_AssemblyContext
from python_code import pcm_repository_ProvidesComponentType
from python_code import pcm_repository_Repository

def test_pcm_repository_ProvidesComponentType___init__():
    assert pcm_repository_ProvidesComponentType.__init__(pcm_repository_ProvidesComponentType(RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()), RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()) == None

def test_pcm_repository_ProvidesComponentType_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType():
    assert pcm_repository_ProvidesComponentType.AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(pcm_repository_ProvidesComponentType(RepositoryComponent62=pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), RepositoryComponent=pcm_composition_AssemblyContext()), '', 0) == None


from python_code import pcm_repository_Repository

def test_pcm_repository_Repository___init__():
    assert pcm_repository_Repository.__init__(pcm_repository_Repository('', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()), '', repository_Interface=set(), repository_DataType=set(), repository_RepositoryComponent=set()) == None


from python_code import DataType
from python_code import Interface
from python_code import pcm_repository_Signature

def test_pcm_repository_Signature___init__():
    assert pcm_repository_Signature.__init__(pcm_repository_Signature('', signature_Parameter=set(), signatures__Interface=Interface(), pcm_repository_Signature=DataType(), pcm_repository_Signature56=set()), '', signature_Parameter=set(), signatures__Interface=Interface(), pcm_repository_Signature=DataType(), pcm_repository_Signature56=set()) == None

def test_pcm_repository_Signature_ParameterNamesHaveToBeUniqueForASignature():
    assert pcm_repository_Signature.ParameterNamesHaveToBeUniqueForASignature(pcm_repository_Signature('', signature_Parameter=set(), signatures__Interface=Interface(), pcm_repository_Signature=DataType(), pcm_repository_Signature56=set()), '', 0) == None


from python_code import CommunicationLinkResourceType
from python_code import PCMRandomVariable
from python_code import pcm_resourceenvironment_CommunicationLinkResourceSpecification

def test_pcm_resourceenvironment_CommunicationLinkResourceSpecification___init__():
    assert pcm_resourceenvironment_CommunicationLinkResourceSpecification.__init__(pcm_resourceenvironment_CommunicationLinkResourceSpecification(0.0, pcm_resourceenvironment_CommunicationLinkResourceSpecification=CommunicationLinkResourceType(), pcm_resourceenvironment_CommunicationLinkResourceSpecification181=PCMRandomVariable(), pcm_resourceenvironment_CommunicationLinkResourceSpecification184=PCMRandomVariable()), 0.0, pcm_resourceenvironment_CommunicationLinkResourceSpecification=CommunicationLinkResourceType(), pcm_resourceenvironment_CommunicationLinkResourceSpecification181=PCMRandomVariable(), pcm_resourceenvironment_CommunicationLinkResourceSpecification184=PCMRandomVariable()) == None


from python_code import PCMRandomVariable
from python_code import ProcessingResourceType
from python_code import pcm_resourceenvironment_ProcessingResourceSpecification

def test_pcm_resourceenvironment_ProcessingResourceSpecification___init__():
    assert pcm_resourceenvironment_ProcessingResourceSpecification.__init__(pcm_resourceenvironment_ProcessingResourceSpecification(0.0, 0.0, '', pcm_resourceenvironment_ProcessingResourceSpecification=ProcessingResourceType(), pcm_resourceenvironment_ProcessingResourceSpecification189=PCMRandomVariable()), 0.0, 0.0, '', pcm_resourceenvironment_ProcessingResourceSpecification=ProcessingResourceType(), pcm_resourceenvironment_ProcessingResourceSpecification189=PCMRandomVariable()) == None


from python_code import pcm_performance_ParametricResourceDemand
from python_code import pcm_seff_BranchAction

def test_pcm_seff_BranchAction___init__():
    assert pcm_seff_BranchAction.__init__(pcm_seff_BranchAction(pcm_seff_BranchAction=set(), AbstractInternalControlFlowAction=pcm_performance_ParametricResourceDemand()), pcm_seff_BranchAction=set(), AbstractInternalControlFlowAction=pcm_performance_ParametricResourceDemand()) == None

def test_pcm_seff_BranchAction_EitherGuardedBranchesOrProbabilisiticBranchTransitions():
    assert pcm_seff_BranchAction.EitherGuardedBranchesOrProbabilisiticBranchTransitions(pcm_seff_BranchAction(pcm_seff_BranchAction=set(), AbstractInternalControlFlowAction=pcm_performance_ParametricResourceDemand()), 0, '\x00\x00') == None

def test_pcm_seff_BranchAction_AllProbabilisticBranchProbabilitiesMustSumUpTo1():
    assert pcm_seff_BranchAction.AllProbabilisticBranchProbabilitiesMustSumUpTo1(pcm_seff_BranchAction(pcm_seff_BranchAction=set(), AbstractInternalControlFlowAction=pcm_performance_ParametricResourceDemand()), 0, '\x00\x00') == None

