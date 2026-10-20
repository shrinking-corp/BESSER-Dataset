from python_code import AssemblyContext
from python_code import ProvidedRole
from python_code import RequiredRole
from python_code import cm_composition_AssemblyConnector
from python_code import cm_composition_ComposedStructure

def test_cm_composition_AssemblyConnector___init__():
    assert cm_composition_AssemblyConnector.__init__(cm_composition_AssemblyConnector(cm_composition_AssemblyConnector=AssemblyContext(), cm_composition_AssemblyConnector61=AssemblyContext(), cm_composition_AssemblyConnector64=ProvidedRole(), cm_composition_AssemblyConnector67=RequiredRole(), Connector=cm_composition_ComposedStructure(parentStructure=set(), parentStructure43=set())), cm_composition_AssemblyConnector=AssemblyContext(), cm_composition_AssemblyConnector61=AssemblyContext(), cm_composition_AssemblyConnector64=ProvidedRole(), cm_composition_AssemblyConnector67=RequiredRole(), Connector=cm_composition_ComposedStructure(parentStructure=set(), parentStructure43=set())) == None

def test_cm_composition_AssemblyConnector_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch():
    assert cm_composition_AssemblyConnector.AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(cm_composition_AssemblyConnector(cm_composition_AssemblyConnector=AssemblyContext(), cm_composition_AssemblyConnector61=AssemblyContext(), cm_composition_AssemblyConnector64=ProvidedRole(), cm_composition_AssemblyConnector67=RequiredRole(), Connector=cm_composition_ComposedStructure(parentStructure=set(), parentStructure43=set())), '\x00', '') == None

def test_cm_composition_AssemblyConnector_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch():
    assert cm_composition_AssemblyConnector.AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(cm_composition_AssemblyConnector(cm_composition_AssemblyConnector=AssemblyContext(), cm_composition_AssemblyConnector61=AssemblyContext(), cm_composition_AssemblyConnector64=ProvidedRole(), cm_composition_AssemblyConnector67=RequiredRole(), Connector=cm_composition_ComposedStructure(parentStructure=set(), parentStructure43=set())), '\x00', '') == None

def test_cm_composition_AssemblyConnector_AssemblyConnectorsReferencedInterfacesMustMatch():
    assert cm_composition_AssemblyConnector.AssemblyConnectorsReferencedInterfacesMustMatch(cm_composition_AssemblyConnector(cm_composition_AssemblyConnector=AssemblyContext(), cm_composition_AssemblyConnector61=AssemblyContext(), cm_composition_AssemblyConnector64=ProvidedRole(), cm_composition_AssemblyConnector67=RequiredRole(), Connector=cm_composition_ComposedStructure(parentStructure=set(), parentStructure43=set())), '\x00', '') == None


from python_code import cm_composition_ComposedStructure

def test_cm_composition_ComposedStructure___init__():
    assert cm_composition_ComposedStructure.__init__(cm_composition_ComposedStructure(parentStructure=set(), parentStructure43=set()), parentStructure=set(), parentStructure43=set()) == None

def test_cm_composition_ComposedStructure_MultipleConnectorsConstraint():
    assert cm_composition_ComposedStructure.MultipleConnectorsConstraint(cm_composition_ComposedStructure(parentStructure=set(), parentStructure43=set()), '\x00', '') == None

def test_cm_composition_ComposedStructure_MultipleConnectorsConstraintForAssemblyConnectors():
    assert cm_composition_ComposedStructure.MultipleConnectorsConstraintForAssemblyConnectors(cm_composition_ComposedStructure(parentStructure=set(), parentStructure43=set()), '\x00', '') == None


from python_code import cm_composition_Identifier

def test_cm_composition_Identifier___init__():
    assert cm_composition_Identifier.__init__(cm_composition_Identifier(''), '') == None

def test_cm_composition_Identifier_idHasToBeUnique():
    assert cm_composition_Identifier.idHasToBeUnique(cm_composition_Identifier(''), 0, '\x00\x00') == None


from python_code import cm_composition_NamedElement

def test_cm_composition_NamedElement___init__():
    assert cm_composition_NamedElement.__init__(cm_composition_NamedElement(''), '') == None


from python_code import AssemblyContext
from python_code import ProvidedRole
from python_code import cm_composition_ProvidedDelegationConnector

def test_cm_composition_ProvidedDelegationConnector___init__():
    assert cm_composition_ProvidedDelegationConnector.__init__(cm_composition_ProvidedDelegationConnector(cm_composition_ProvidedDelegationConnector=ProvidedRole(), cm_composition_ProvidedDelegationConnector46=ProvidedRole(), cm_composition_ProvidedDelegationConnector49=AssemblyContext()), cm_composition_ProvidedDelegationConnector=ProvidedRole(), cm_composition_ProvidedDelegationConnector46=ProvidedRole(), cm_composition_ProvidedDelegationConnector49=AssemblyContext()) == None

def test_cm_composition_ProvidedDelegationConnector_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure():
    assert cm_composition_ProvidedDelegationConnector.ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(cm_composition_ProvidedDelegationConnector(cm_composition_ProvidedDelegationConnector=ProvidedRole(), cm_composition_ProvidedDelegationConnector46=ProvidedRole(), cm_composition_ProvidedDelegationConnector49=AssemblyContext()), '', '') == None

def test_cm_composition_ProvidedDelegationConnector_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame():
    assert cm_composition_ProvidedDelegationConnector.ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(cm_composition_ProvidedDelegationConnector(cm_composition_ProvidedDelegationConnector=ProvidedRole(), cm_composition_ProvidedDelegationConnector46=ProvidedRole(), cm_composition_ProvidedDelegationConnector49=AssemblyContext()), '', '') == None


from python_code import cm_composition_System

def test_cm_composition_System___init__():
    assert cm_composition_System.__init__(cm_composition_System()) == None

def test_cm_composition_System_SystemMustHaveAtLeastOneProvidedRole():
    assert cm_composition_System.SystemMustHaveAtLeastOneProvidedRole(cm_composition_System(), '', '') == None


from python_code import cm_repository_CompositeComponent

def test_cm_repository_CompositeComponent___init__():
    assert cm_repository_CompositeComponent.__init__(cm_repository_CompositeComponent()) == None

def test_cm_repository_CompositeComponent_ProvideSameInterfaces():
    assert cm_repository_CompositeComponent.ProvideSameInterfaces(cm_repository_CompositeComponent(), '', '') == None

def test_cm_repository_CompositeComponent_RequireSameInterfaces():
    assert cm_repository_CompositeComponent.RequireSameInterfaces(cm_repository_CompositeComponent(), '', '') == None


from python_code import cm_repository_ExceptionType

def test_cm_repository_ExceptionType___init__():
    assert cm_repository_ExceptionType.__init__(cm_repository_ExceptionType('', '\x00'), '\x00\x00', '') == None


from python_code import DataType
from python_code import Signature
from python_code import cm_repository_Parameter

def test_cm_repository_Parameter___init__():
    assert cm_repository_Parameter.__init__(cm_repository_Parameter('', cm_repository_Parameter=DataType(), parameters=Signature()), '\x00', cm_repository_Parameter=DataType(), parameters=Signature()) == None


from python_code import DataType
from python_code import Signature
from python_code import cm_repository_CollectionDataType
from python_code import cm_repository_InnerDeclaration
from python_code import cm_repository_Parameter
from python_code import cm_repository_PrimitiveDataType
from python_code import cm_repository_Repository
from python_code import cm_repository_Signature

def test_cm_repository_PrimitiveDataType___init__():
    assert cm_repository_PrimitiveDataType.__init__(cm_repository_PrimitiveDataType('\x00', DataType15=cm_repository_Repository('', repository=set(), repository11=set(), repository14=set()), DataType=cm_repository_Parameter('', cm_repository_Parameter=DataType(), parameters=Signature()), DataType37=cm_repository_InnerDeclaration(), DataType26=cm_repository_Signature(), DataType33=cm_repository_CollectionDataType()), '', DataType15=cm_repository_Repository('', repository=set(), repository11=set(), repository14=set()), DataType=cm_repository_Parameter('', cm_repository_Parameter=DataType(), parameters=Signature()), DataType37=cm_repository_InnerDeclaration(), DataType26=cm_repository_Signature(), DataType33=cm_repository_CollectionDataType()) == None


from python_code import cm_repository_Repository

def test_cm_repository_Repository___init__():
    assert cm_repository_Repository.__init__(cm_repository_Repository('', repository=set(), repository11=set(), repository14=set()), '', repository=set(), repository11=set(), repository14=set()) == None


from python_code import BranchAction
from python_code import cm_seff_ProbabilisticBranchTransition

def test_cm_seff_ProbabilisticBranchTransition___init__():
    assert cm_seff_ProbabilisticBranchTransition.__init__(cm_seff_ProbabilisticBranchTransition(0.0, branchTransitions=BranchAction()), 0.0, branchTransitions=BranchAction()) == None

