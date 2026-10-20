from python_code import org_behavior_BooleanLiteral

def test_org_behavior_BooleanLiteral___init__():
    assert org_behavior_BooleanLiteral.__init__(org_behavior_BooleanLiteral(''), '') == None


from python_code import behavior_Expression
from python_code import org_behavior_CallFeature

def test_org_behavior_CallFeature___init__():
    assert org_behavior_CallFeature.__init__(org_behavior_CallFeature('', org_behavior_CallFeature=behavior_Expression()), '', org_behavior_CallFeature=behavior_Expression()) == None


from python_code import org_behavior_CallVariable

def test_org_behavior_CallVariable___init__():
    assert org_behavior_CallVariable.__init__(org_behavior_CallVariable(''), '') == None


from python_code import org_behavior_IntegerLiteral

def test_org_behavior_IntegerLiteral___init__():
    assert org_behavior_IntegerLiteral.__init__(org_behavior_IntegerLiteral(''), '') == None


from python_code import org_behavior_JavaStaticCall

def test_org_behavior_JavaStaticCall___init__():
    assert org_behavior_JavaStaticCall.__init__(org_behavior_JavaStaticCall('\x00\x00', '', org_behavior_JavaStaticCall=set()), '', '', org_behavior_JavaStaticCall=set()) == None


from python_code import behavior_TypeReference
from python_code import org_behavior_LambdaParameter

def test_org_behavior_LambdaParameter___init__():
    assert org_behavior_LambdaParameter.__init__(org_behavior_LambdaParameter('', org_behavior_LambdaParameter=behavior_TypeReference()), '', org_behavior_LambdaParameter=behavior_TypeReference()) == None


from python_code import behavior_TypeReference
from python_code import org_behavior_Rescue

def test_org_behavior_Rescue___init__():
    assert org_behavior_Rescue.__init__(org_behavior_Rescue('', org_behavior_Rescue=set(), org_behavior_Rescue30=behavior_TypeReference()), '', org_behavior_Rescue=set(), org_behavior_Rescue30=behavior_TypeReference()) == None


from python_code import org_behavior_StringLiteral

def test_org_behavior_StringLiteral___init__():
    assert org_behavior_StringLiteral.__init__(org_behavior_StringLiteral(''), '') == None


from python_code import behavior_Expression
from python_code import behavior_TypeReference
from python_code import org_behavior_VariableDecl

def test_org_behavior_VariableDecl___init__():
    assert org_behavior_VariableDecl.__init__(org_behavior_VariableDecl('', org_behavior_VariableDecl=behavior_Expression(), org_behavior_VariableDecl52=behavior_TypeReference()), '', org_behavior_VariableDecl=behavior_Expression(), org_behavior_VariableDecl52=behavior_TypeReference()) == None


from python_code import org_structure_Class

def test_org_structure_Class___init__():
    assert org_structure_Class.__init__(org_structure_Class('', '', org_structure_Class=set(), org_structure_Class108=set(), org_structure_Class111=set()), '', '', org_structure_Class=set(), org_structure_Class108=set(), org_structure_Class111=set()) == None


from python_code import org_structure_ClassDefinition

def test_org_structure_ClassDefinition___init__():
    assert org_structure_ClassDefinition.__init__(org_structure_ClassDefinition('', '', '', invOwner=set(), owningClass=set(), owningClass135=set()), '', '\x00', '', invOwner=set(), owningClass=set(), owningClass135=set()) == None


from python_code import behavior_Expression
from python_code import org_structure_Constraint
from python_code import structure_ClassDefinition
from python_code import structure_Operation

def test_org_structure_Constraint___init__():
    assert org_structure_Constraint.__init__(org_structure_Constraint('', '\x00', org_structure_Constraint=behavior_Expression(), inv=structure_ClassDefinition(), pre=structure_Operation(), post=structure_Operation()), '\x00\x00', '', org_structure_Constraint=behavior_Expression(), inv=structure_ClassDefinition(), pre=structure_Operation(), post=structure_Operation()) == None


from python_code import org_structure_Metamodel
from python_code import org_structure_Model
from python_code import org_structure_Tag
from python_code import org_structure_UseAdaptationOperator

def test_org_structure_Metamodel___init__():
    assert org_structure_Metamodel.__init__(org_structure_Metamodel('', False, org_structure_Metamodel=set(), org_structure_Metamodel139=set(), structure_KermetaModelElement205=org_structure_UseAdaptationOperator(), KermetaModelElement=org_structure_Tag('', '', kTag=set()), structure_KermetaModelElement=org_structure_Model()), '\x00', False, org_structure_Metamodel=set(), org_structure_Metamodel139=set(), structure_KermetaModelElement205=org_structure_UseAdaptationOperator(), KermetaModelElement=org_structure_Tag('', '', kTag=set()), structure_KermetaModelElement=org_structure_Model()) == None


from python_code import behavior_Expression
from python_code import org_structure_ModelTransformation
from python_code import structure_ModelTypeDefinition

def test_org_structure_ModelTransformation___init__():
    assert org_structure_ModelTransformation.__init__(org_structure_ModelTransformation('', org_structure_ModelTransformation=set(), org_structure_ModelTransformation228=behavior_Expression(), org_structure_ModelTransformation231=set(), ownedTransformations=structure_ModelTypeDefinition(), org_structure_ModelTransformation235=set()), '', org_structure_ModelTransformation=set(), org_structure_ModelTransformation228=behavior_Expression(), org_structure_ModelTransformation231=set(), ownedTransformations=structure_ModelTypeDefinition(), org_structure_ModelTransformation235=set()) == None


from python_code import org_structure_MultiplicityElement

def test_org_structure_MultiplicityElement___init__():
    assert org_structure_MultiplicityElement.__init__(org_structure_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import org_structure_NamedElement

def test_org_structure_NamedElement___init__():
    assert org_structure_NamedElement.__init__(org_structure_NamedElement(''), '') == None


from python_code import org_structure_OperationAdaptationOperator
from python_code import structure_Operation

def test_org_structure_OperationAdaptationOperator___init__():
    assert org_structure_OperationAdaptationOperator.__init__(org_structure_OperationAdaptationOperator('', org_structure_OperationAdaptationOperator=structure_Operation()), '', org_structure_OperationAdaptationOperator=structure_Operation()) == None


from python_code import org_structure_Package
from python_code import structure_Package

def test_org_structure_Package___init__():
    assert org_structure_Package.__init__(org_structure_Package('', nestingPackage=set(), nestedPackage=structure_Package(), org_structure_Package=set()), '', nestingPackage=set(), nestedPackage=structure_Package(), org_structure_Package=set()) == None


from python_code import org_structure_PropertyAdaptationOperator
from python_code import structure_Property

def test_org_structure_PropertyAdaptationOperator___init__():
    assert org_structure_PropertyAdaptationOperator.__init__(org_structure_PropertyAdaptationOperator('\x00\x00', '', '', '', org_structure_PropertyAdaptationOperator=structure_Property()), '', '', '', '', org_structure_PropertyAdaptationOperator=structure_Property()) == None


from python_code import org_structure_Tag

def test_org_structure_Tag___init__():
    assert org_structure_Tag.__init__(org_structure_Tag('\x00\x00', '', kTag=set()), '', '', kTag=set()) == None


from python_code import org_structure_Type
from python_code import org_structure_UnresolvedOperation
from python_code import org_structure_UseAdaptationOperator

def test_org_structure_UnresolvedOperation___init__():
    assert org_structure_UnresolvedOperation.__init__(org_structure_UnresolvedOperation('', TypeContainer=org_structure_Type(), structure_UnresolvedReference=org_structure_UseAdaptationOperator()), '', TypeContainer=org_structure_Type(), structure_UnresolvedReference=org_structure_UseAdaptationOperator()) == None

