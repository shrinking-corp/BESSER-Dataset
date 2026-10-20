from python_code import sadl_CardCondition
from python_code import sadl_Cardinality
from python_code import sadl_ResourceIdentifier

def test_sadl_CardCondition___init__():
    assert sadl_CardCondition.__init__(sadl_CardCondition('', sadl_CardCondition=sadl_Cardinality(), sadl_CardCondition176=sadl_ResourceIdentifier()), '', sadl_CardCondition=sadl_Cardinality(), sadl_CardCondition176=sadl_ResourceIdentifier()) == None


from python_code import sadl_Display

def test_sadl_Display___init__():
    assert sadl_Display.__init__(sadl_Display('', '\x00'), '\x00\x00', '') == None


from python_code import sadl_EObject
from python_code import sadl_Explanation

def test_sadl_Explanation___init__():
    assert sadl_Explanation.__init__(sadl_Explanation('', sadl_Explanation=sadl_EObject()), '', sadl_Explanation=sadl_EObject()) == None


from python_code import sadl_Import
from python_code import sadl_Model

def test_sadl_Import___init__():
    assert sadl_Import.__init__(sadl_Import('', '\x00', sadl_Import=sadl_Model()), '\x00\x00', '', sadl_Import=sadl_Model()) == None


from python_code import sadl_MaxCardCondition
from python_code import sadl_MaxCardinality
from python_code import sadl_ResourceIdentifier

def test_sadl_MaxCardCondition___init__():
    assert sadl_MaxCardCondition.__init__(sadl_MaxCardCondition('', sadl_MaxCardCondition=sadl_MaxCardinality(), sadl_MaxCardCondition173=sadl_ResourceIdentifier()), '', sadl_MaxCardCondition=sadl_MaxCardinality(), sadl_MaxCardCondition173=sadl_ResourceIdentifier()) == None


from python_code import sadl_MinCardCondition
from python_code import sadl_MinCardinality
from python_code import sadl_ResourceIdentifier

def test_sadl_MinCardCondition___init__():
    assert sadl_MinCardCondition.__init__(sadl_MinCardCondition('', sadl_MinCardCondition=sadl_MinCardinality(), sadl_MinCardCondition170=sadl_ResourceIdentifier()), '', sadl_MinCardCondition=sadl_MinCardinality(), sadl_MinCardCondition170=sadl_ResourceIdentifier()) == None


from python_code import sadl_Model
from python_code import sadl_ModelName

def test_sadl_ModelName___init__():
    assert sadl_ModelName.__init__(sadl_ModelName('', '', '', '', sadl_ModelName=sadl_Model(), sadl_ModelName6=set()), '', '', '', '', sadl_ModelName=sadl_Model(), sadl_ModelName6=set()) == None


from python_code import sadl_MergedTriples
from python_code import sadl_OfPatternReturningValues
from python_code import sadl_OfPhrase
from python_code import sadl_PropOfSubj
from python_code import sadl_ResourceByName

def test_sadl_OfPhrase___init__():
    assert sadl_OfPhrase.__init__(sadl_OfPhrase('', sadl_OfPhrase=sadl_OfPatternReturningValues(), sadl_OfPhrase293=sadl_MergedTriples(), sadl_OfPhrase301=sadl_ResourceByName(), sadl_OfPhrase355=sadl_PropOfSubj()), '', sadl_OfPhrase=sadl_OfPatternReturningValues(), sadl_OfPhrase293=sadl_MergedTriples(), sadl_OfPhrase301=sadl_ResourceByName(), sadl_OfPhrase355=sadl_PropOfSubj()) == None


from python_code import sadl_Condition
from python_code import sadl_ResourceByName
from python_code import sadl_ResourceByRestriction

def test_sadl_ResourceByRestriction___init__():
    assert sadl_ResourceByRestriction.__init__(sadl_ResourceByRestriction('', sadl_ResourceByRestriction=set(), sadl_ResourceByRestriction23=sadl_ResourceByName(), sadl_ResourceByRestriction26=sadl_Condition()), '', sadl_ResourceByRestriction=set(), sadl_ResourceByRestriction23=sadl_ResourceByName(), sadl_ResourceByRestriction26=sadl_Condition()) == None


from python_code import sadl_ResourceBySetOp

def test_sadl_ResourceBySetOp___init__():
    assert sadl_ResourceBySetOp.__init__(sadl_ResourceBySetOp('', '', sadl_ResourceBySetOp=set(), sadl_ResourceBySetOp18=set()), '', '', sadl_ResourceBySetOp=set(), sadl_ResourceBySetOp18=set()) == None


from python_code import sadl_ElementSet
from python_code import sadl_Rule

def test_sadl_Rule___init__():
    assert sadl_Rule.__init__(sadl_Rule('', sadl_Rule=sadl_ElementSet(), sadl_Rule307=sadl_ElementSet(), sadl_Rule310=sadl_ElementSet()), '', sadl_Rule=sadl_ElementSet(), sadl_Rule307=sadl_ElementSet(), sadl_Rule310=sadl_ElementSet()) == None


from python_code import sadl_OrderList
from python_code import sadl_SelectExpression
from python_code import sadl_VariableList

def test_sadl_SelectExpression___init__():
    assert sadl_SelectExpression.__init__(sadl_SelectExpression('', '', '\x00\x00', sadl_SelectExpression=sadl_VariableList(), sadl_SelectExpression325=sadl_OrderList()), '', '', '', sadl_SelectExpression=sadl_VariableList(), sadl_SelectExpression325=sadl_OrderList()) == None


from python_code import sadl_UnaryOpExpression

def test_sadl_UnaryOpExpression___init__():
    assert sadl_UnaryOpExpression.__init__(sadl_UnaryOpExpression(''), '') == None

