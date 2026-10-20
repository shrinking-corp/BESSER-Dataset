from python_code import rell_BoolConstant

def test_rell_BoolConstant___init__():
    assert rell_BoolConstant.__init__(rell_BoolConstant(''), '') == None


from python_code import rell_Comparison
from python_code import rell_Expression

def test_rell_Comparison___init__():
    assert rell_Comparison.__init__(rell_Comparison('', rell_Comparison73=rell_Expression(), rell_Comparison=rell_Expression()), '', rell_Comparison73=rell_Expression(), rell_Comparison=rell_Expression()) == None


from python_code import rell_ConditionElement
from python_code import rell_Conditions
from python_code import rell_Expression

def test_rell_ConditionElement___init__():
    assert rell_ConditionElement.__init__(rell_ConditionElement('', rell_ConditionElement=rell_Conditions(), rell_ConditionElement26=rell_Expression()), '', rell_ConditionElement=rell_Conditions(), rell_ConditionElement26=rell_Expression()) == None


from python_code import rell_Equality
from python_code import rell_Expression

def test_rell_Equality___init__():
    assert rell_Equality.__init__(rell_Equality('', rell_Equality=rell_Expression(), rell_Equality68=rell_Expression()), '', rell_Equality=rell_Expression(), rell_Equality68=rell_Expression()) == None


from python_code import rell_IntConstant

def test_rell_IntConstant___init__():
    assert rell_IntConstant.__init__(rell_IntConstant(0), 0) == None


from python_code import rell_Expression
from python_code import rell_MulOrDiv

def test_rell_MulOrDiv___init__():
    assert rell_MulOrDiv.__init__(rell_MulOrDiv('', rell_MulOrDiv=rell_Expression(), rell_MulOrDiv90=rell_Expression()), '', rell_MulOrDiv=rell_Expression(), rell_MulOrDiv90=rell_Expression()) == None


from python_code import rell_Model
from python_code import rell_Operation
from python_code import rell_RelAttrubutesList

def test_rell_Operation___init__():
    assert rell_Operation.__init__(rell_Operation('', rell_Operation=rell_Model(), rell_Operation9=rell_RelAttrubutesList(), rell_Operation11=set()), '', rell_Operation=rell_Model(), rell_Operation9=rell_RelAttrubutesList(), rell_Operation11=set()) == None


from python_code import rell_PrimitiveType
from python_code import rell_TypeReference

def test_rell_PrimitiveType___init__():
    assert rell_PrimitiveType.__init__(rell_PrimitiveType('', rell_PrimitiveType=rell_TypeReference()), '', rell_PrimitiveType=rell_TypeReference()) == None


from python_code import rell_StringConstant

def test_rell_StringConstant___init__():
    assert rell_StringConstant.__init__(rell_StringConstant(''), '') == None

