from python_code import ResourceEnvironment
from python_code import System
from python_code import pcm_allocation_Allocation

def test_pcm_allocation_Allocation___init__():
    assert pcm_allocation_Allocation.__init__(pcm_allocation_Allocation(pcm_allocation_Allocation=set(), pcm_allocation_Allocation158=ResourceEnvironment(), pcm_allocation_Allocation160=System()), pcm_allocation_Allocation=set(), pcm_allocation_Allocation158=ResourceEnvironment(), pcm_allocation_Allocation160=System()) == None

def test_pcm_allocation_Allocation_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce():
    assert pcm_allocation_Allocation.EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(pcm_allocation_Allocation(pcm_allocation_Allocation=set(), pcm_allocation_Allocation158=ResourceEnvironment(), pcm_allocation_Allocation160=System()), 0, '\x00\x00') == None


from python_code import ProvidedRole
from python_code import composition_AssemblyContext
from python_code import composition_ComposedStructure
from python_code import pcm_composition_ProvidedDelegationConnector

def test_pcm_composition_ProvidedDelegationConnector___init__():
    assert pcm_composition_ProvidedDelegationConnector.__init__(pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector5=ProvidedRole(), pcm_composition_ProvidedDelegationConnector8=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector5=ProvidedRole(), pcm_composition_ProvidedDelegationConnector8=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()) == None

def test_pcm_composition_ProvidedDelegationConnector_ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame():
    assert pcm_composition_ProvidedDelegationConnector.ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame(pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector5=ProvidedRole(), pcm_composition_ProvidedDelegationConnector8=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None

def test_pcm_composition_ProvidedDelegationConnector_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure():
    assert pcm_composition_ProvidedDelegationConnector.ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(pcm_composition_ProvidedDelegationConnector(pcm_composition_ProvidedDelegationConnector=ProvidedRole(), pcm_composition_ProvidedDelegationConnector5=ProvidedRole(), pcm_composition_ProvidedDelegationConnector8=composition_AssemblyContext(), providedDelegationConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None


from python_code import RequiredRole
from python_code import composition_AssemblyContext
from python_code import composition_ComposedStructure
from python_code import pcm_composition_RequiredDelegationConnector

def test_pcm_composition_RequiredDelegationConnector___init__():
    assert pcm_composition_RequiredDelegationConnector.__init__(pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector18=RequiredRole(), pcm_composition_RequiredDelegationConnector21=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector18=RequiredRole(), pcm_composition_RequiredDelegationConnector21=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()) == None

def test_pcm_composition_RequiredDelegationConnector_ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame():
    assert pcm_composition_RequiredDelegationConnector.ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame(pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector18=RequiredRole(), pcm_composition_RequiredDelegationConnector21=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None

def test_pcm_composition_RequiredDelegationConnector_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure():
    assert pcm_composition_RequiredDelegationConnector.RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(pcm_composition_RequiredDelegationConnector(pcm_composition_RequiredDelegationConnector=RequiredRole(), pcm_composition_RequiredDelegationConnector18=RequiredRole(), pcm_composition_RequiredDelegationConnector21=composition_AssemblyContext(), requiredDelegationConnectors_ComposedStructure=composition_ComposedStructure()), '', 0) == None


from python_code import pcm_core_PCMRandomVariable

def test_pcm_core_PCMRandomVariable___init__():
    assert pcm_core_PCMRandomVariable.__init__(pcm_core_PCMRandomVariable()) == None

def test_pcm_core_PCMRandomVariable_SpecificationMustNotBeNULL():
    assert pcm_core_PCMRandomVariable.SpecificationMustNotBeNULL(pcm_core_PCMRandomVariable(), '', '') == None


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


from python_code import pcm_repository_ExceptionType

def test_pcm_repository_ExceptionType___init__():
    assert pcm_repository_ExceptionType.__init__(pcm_repository_ExceptionType('', '\x00'), '\x00\x00', '') == None


from python_code import Repository
from python_code import pcm_repository_Interface

def test_pcm_repository_Interface___init__():
    assert pcm_repository_Interface.__init__(pcm_repository_Interface(pcm_repository_Interface66=set(), pcm_repository_Interface69=set(), interface_Signature=set(), interfaces__Repository=Repository(), pcm_repository_Interface=set()), pcm_repository_Interface66=set(), pcm_repository_Interface69=set(), interface_Signature=set(), interfaces__Repository=Repository(), pcm_repository_Interface=set()) == None

def test_pcm_repository_Interface_NoProtocolTypeIDUsedTwice():
    assert pcm_repository_Interface.NoProtocolTypeIDUsedTwice(pcm_repository_Interface(pcm_repository_Interface66=set(), pcm_repository_Interface69=set(), interface_Signature=set(), interfaces__Repository=Repository(), pcm_repository_Interface=set()), '', '') == None

def test_pcm_repository_Interface_SignaturesHaveToBeUniqueForAnInterface():
    assert pcm_repository_Interface.SignaturesHaveToBeUniqueForAnInterface(pcm_repository_Interface(pcm_repository_Interface66=set(), pcm_repository_Interface69=set(), interface_Signature=set(), interfaces__Repository=Repository(), pcm_repository_Interface=set()), '', '') == None


from python_code import DataType
from python_code import Signature
from python_code import pcm_repository_Parameter

def test_pcm_repository_Parameter___init__():
    assert pcm_repository_Parameter.__init__(pcm_repository_Parameter('', '', pcm_repository_Parameter=DataType(), parameters__Signature=Signature()), '', '', pcm_repository_Parameter=DataType(), parameters__Signature=Signature()) == None


from python_code import Repository
from python_code import pcm_repository_ProvidesComponentType

def test_pcm_repository_ProvidesComponentType___init__():
    assert pcm_repository_ProvidesComponentType.__init__(pcm_repository_ProvidesComponentType(components__Repository=Repository()), components__Repository=Repository()) == None

def test_pcm_repository_ProvidesComponentType_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType():
    assert pcm_repository_ProvidesComponentType.AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(pcm_repository_ProvidesComponentType(components__Repository=Repository()), '', '') == None


from python_code import PCMRandomVariable
from python_code import ProcessingResourceType
from python_code import pcm_resourceenvironment_ProcessingResourceSpecification

def test_pcm_resourceenvironment_ProcessingResourceSpecification___init__():
    assert pcm_resourceenvironment_ProcessingResourceSpecification.__init__(pcm_resourceenvironment_ProcessingResourceSpecification('', pcm_resourceenvironment_ProcessingResourceSpecification=ProcessingResourceType(), pcm_resourceenvironment_ProcessingResourceSpecification182=PCMRandomVariable()), '\x00', pcm_resourceenvironment_ProcessingResourceSpecification=ProcessingResourceType(), pcm_resourceenvironment_ProcessingResourceSpecification182=PCMRandomVariable()) == None


from python_code import pcm_seff_BranchAction
from python_code import pcm_seff_ParametricResourceDemand

def test_pcm_seff_BranchAction___init__():
    assert pcm_seff_BranchAction.__init__(pcm_seff_BranchAction(pcm_seff_BranchAction=set(), AbstractResourceDemandingAction=pcm_seff_ParametricResourceDemand()), pcm_seff_BranchAction=set(), AbstractResourceDemandingAction=pcm_seff_ParametricResourceDemand()) == None

def test_pcm_seff_BranchAction_EitherGuardedBranchesOrProbabilisiticBranchTransitions():
    assert pcm_seff_BranchAction.EitherGuardedBranchesOrProbabilisiticBranchTransitions(pcm_seff_BranchAction(pcm_seff_BranchAction=set(), AbstractResourceDemandingAction=pcm_seff_ParametricResourceDemand()), 0, '\x00\x00') == None

def test_pcm_seff_BranchAction_AllProbabilisticBranchProbabilitiesMustSumUpTo1():
    assert pcm_seff_BranchAction.AllProbabilisticBranchProbabilitiesMustSumUpTo1(pcm_seff_BranchAction(pcm_seff_BranchAction=set(), AbstractResourceDemandingAction=pcm_seff_ParametricResourceDemand()), 0, '\x00\x00') == None

