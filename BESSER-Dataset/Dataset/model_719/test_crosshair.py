from python_code import behavior_CallExpression
from python_code import behavior_Expression
from python_code import kermeta_behavior_Assignment

def test_kermeta_behavior_Assignment___init__():
    assert kermeta_behavior_Assignment.__init__(kermeta_behavior_Assignment('', kermeta_behavior_Assignment=behavior_CallExpression(), kermeta_behavior_Assignment2=behavior_Expression()), '', kermeta_behavior_Assignment=behavior_CallExpression(), kermeta_behavior_Assignment2=behavior_Expression()) == None


from python_code import kermeta_behavior_BooleanLiteral

def test_kermeta_behavior_BooleanLiteral___init__():
    assert kermeta_behavior_BooleanLiteral.__init__(kermeta_behavior_BooleanLiteral(''), '') == None


from python_code import behavior_Expression
from python_code import kermeta_behavior_CallFeature
from python_code import structure_EnumerationLiteral
from python_code import structure_Operation
from python_code import structure_Property

def test_kermeta_behavior_CallFeature___init__():
    assert kermeta_behavior_CallFeature.__init__(kermeta_behavior_CallFeature('', kermeta_behavior_CallFeature=behavior_Expression(), kermeta_behavior_CallFeature16=structure_Property(), kermeta_behavior_CallFeature18=structure_Operation(), kermeta_behavior_CallFeature20=structure_EnumerationLiteral()), '', kermeta_behavior_CallFeature=behavior_Expression(), kermeta_behavior_CallFeature16=structure_Property(), kermeta_behavior_CallFeature18=structure_Operation(), kermeta_behavior_CallFeature20=structure_EnumerationLiteral()) == None


from python_code import kermeta_behavior_CallVariable

def test_kermeta_behavior_CallVariable___init__():
    assert kermeta_behavior_CallVariable.__init__(kermeta_behavior_CallVariable(''), '') == None


from python_code import kermeta_behavior_IntegerLiteral

def test_kermeta_behavior_IntegerLiteral___init__():
    assert kermeta_behavior_IntegerLiteral.__init__(kermeta_behavior_IntegerLiteral(''), '') == None


from python_code import kermeta_behavior_JavaStaticCall

def test_kermeta_behavior_JavaStaticCall___init__():
    assert kermeta_behavior_JavaStaticCall.__init__(kermeta_behavior_JavaStaticCall('\x00\x00', '', kermeta_behavior_JavaStaticCall=set()), '', '', kermeta_behavior_JavaStaticCall=set()) == None


from python_code import behavior_TypeReference
from python_code import kermeta_behavior_LambdaParameter

def test_kermeta_behavior_LambdaParameter___init__():
    assert kermeta_behavior_LambdaParameter.__init__(kermeta_behavior_LambdaParameter('', kermeta_behavior_LambdaParameter=behavior_TypeReference()), '', kermeta_behavior_LambdaParameter=behavior_TypeReference()) == None


from python_code import behavior_TypeReference
from python_code import kermeta_behavior_Rescue

def test_kermeta_behavior_Rescue___init__():
    assert kermeta_behavior_Rescue.__init__(kermeta_behavior_Rescue('', kermeta_behavior_Rescue=set(), kermeta_behavior_Rescue34=behavior_TypeReference()), '', kermeta_behavior_Rescue=set(), kermeta_behavior_Rescue34=behavior_TypeReference()) == None


from python_code import kermeta_behavior_StringLiteral

def test_kermeta_behavior_StringLiteral___init__():
    assert kermeta_behavior_StringLiteral.__init__(kermeta_behavior_StringLiteral(''), '') == None


from python_code import behavior_Expression
from python_code import behavior_TypeReference
from python_code import kermeta_behavior_VariableDecl

def test_kermeta_behavior_VariableDecl___init__():
    assert kermeta_behavior_VariableDecl.__init__(kermeta_behavior_VariableDecl('', kermeta_behavior_VariableDecl=behavior_Expression(), kermeta_behavior_VariableDecl56=behavior_TypeReference()), '', kermeta_behavior_VariableDecl=behavior_Expression(), kermeta_behavior_VariableDecl56=behavior_TypeReference()) == None


from python_code import kermeta_structure_Class

def test_kermeta_structure_Class___init__():
    assert kermeta_structure_Class.__init__(kermeta_structure_Class('', '', kermeta_structure_Class=set(), kermeta_structure_Class61=set(), kermeta_structure_Class64=set()), '', '', kermeta_structure_Class=set(), kermeta_structure_Class61=set(), kermeta_structure_Class64=set()) == None

def test_kermeta_structure_Class__new():
    assert kermeta_structure_Class._new(kermeta_structure_Class('\x00\x00', '', kermeta_structure_Class=set(), kermeta_structure_Class61=set(), kermeta_structure_Class64=set())) == None


from python_code import kermeta_structure_ClassDefinition
from python_code import kermeta_structure_ParameterizedType
from python_code import kermeta_structure_Type

def test_kermeta_structure_ClassDefinition___init__():
    assert kermeta_structure_ClassDefinition.__init__(kermeta_structure_ClassDefinition('', invOwner=set(), owningClass=set(), owningClass124=set(), kermeta_structure_ClassDefinition=set(), TypeContainer=kermeta_structure_Type(), structure_GenericTypeDefinition=kermeta_structure_ParameterizedType()), '', invOwner=set(), owningClass=set(), owningClass124=set(), kermeta_structure_ClassDefinition=set(), TypeContainer=kermeta_structure_Type(), structure_GenericTypeDefinition=kermeta_structure_ParameterizedType()) == None


from python_code import behavior_Expression
from python_code import kermeta_structure_Constraint
from python_code import structure_ClassDefinition
from python_code import structure_Operation

def test_kermeta_structure_Constraint___init__():
    assert kermeta_structure_Constraint.__init__(kermeta_structure_Constraint('', '\x00', kermeta_structure_Constraint=behavior_Expression(), inv=structure_ClassDefinition(), pre=structure_Operation(), post=structure_Operation()), '\x00\x00', '', kermeta_structure_Constraint=behavior_Expression(), inv=structure_ClassDefinition(), pre=structure_Operation(), post=structure_Operation()) == None


from python_code import kermeta_structure_Filter

def test_kermeta_structure_Filter___init__():
    assert kermeta_structure_Filter.__init__(kermeta_structure_Filter(''), '') == None


from python_code import kermeta_structure_MultiplicityElement

def test_kermeta_structure_MultiplicityElement___init__():
    assert kermeta_structure_MultiplicityElement.__init__(kermeta_structure_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import kermeta_structure_NamedElement

def test_kermeta_structure_NamedElement___init__():
    assert kermeta_structure_NamedElement.__init__(kermeta_structure_NamedElement(''), '') == None


from python_code import kermeta_structure_Package
from python_code import structure_Package

def test_kermeta_structure_Package___init__():
    assert kermeta_structure_Package.__init__(kermeta_structure_Package('', nestingPackage=set(), nestedPackage=structure_Package()), '', nestingPackage=set(), nestedPackage=structure_Package()) == None


from python_code import behavior_Expression
from python_code import kermeta_structure_Property
from python_code import structure_ClassDefinition
from python_code import structure_Property

def test_kermeta_structure_Property___init__():
    assert kermeta_structure_Property.__init__(kermeta_structure_Property('', '', '', '', '', '', '', kermeta_structure_Property=structure_Property(), kermeta_structure_Property87=behavior_Expression(), kermeta_structure_Property90=behavior_Expression(), ownedAttribute=structure_ClassDefinition()), '', '\x00', '', '', '', '', '', kermeta_structure_Property=structure_Property(), kermeta_structure_Property87=behavior_Expression(), kermeta_structure_Property90=behavior_Expression(), ownedAttribute=structure_ClassDefinition()) == None


from python_code import kermeta_structure_Require

def test_kermeta_structure_Require___init__():
    assert kermeta_structure_Require.__init__(kermeta_structure_Require(''), '') == None


from python_code import kermeta_structure_Tag

def test_kermeta_structure_Tag___init__():
    assert kermeta_structure_Tag.__init__(kermeta_structure_Tag('\x00\x00', '', tag=set()), '', '', tag=set()) == None


from python_code import kermeta_structure_TypeDefinition

def test_kermeta_structure_TypeDefinition___init__():
    assert kermeta_structure_TypeDefinition.__init__(kermeta_structure_TypeDefinition(''), '') == None


from python_code import kermeta_structure_Using

def test_kermeta_structure_Using___init__():
    assert kermeta_structure_Using.__init__(kermeta_structure_Using(''), '') == None

