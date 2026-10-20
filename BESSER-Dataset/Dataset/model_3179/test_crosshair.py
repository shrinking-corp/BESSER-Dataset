from python_code import iot_BoolConstant

def test_iot_BoolConstant___init__():
    assert iot_BoolConstant.__init__(iot_BoolConstant(''), '') == None


from python_code import iot_Comparison
from python_code import iot_Expression

def test_iot_Comparison___init__():
    assert iot_Comparison.__init__(iot_Comparison('', iot_Comparison=iot_Expression(), iot_Comparison49=iot_Expression()), '', iot_Comparison=iot_Expression(), iot_Comparison49=iot_Expression()) == None


from python_code import iot_Equality
from python_code import iot_Expression

def test_iot_Equality___init__():
    assert iot_Equality.__init__(iot_Equality('', iot_Equality=iot_Expression(), iot_Equality44=iot_Expression()), '', iot_Equality=iot_Expression(), iot_Equality44=iot_Expression()) == None


from python_code import iot_IntConstant

def test_iot_IntConstant___init__():
    assert iot_IntConstant.__init__(iot_IntConstant(0), 0) == None


from python_code import iot_Expression
from python_code import iot_MulOrDiv

def test_iot_MulOrDiv___init__():
    assert iot_MulOrDiv.__init__(iot_MulOrDiv('', iot_MulOrDiv=iot_Expression(), iot_MulOrDiv64=iot_Expression()), '', iot_MulOrDiv=iot_Expression(), iot_MulOrDiv64=iot_Expression()) == None


from python_code import iot_StringConstant

def test_iot_StringConstant___init__():
    assert iot_StringConstant.__init__(iot_StringConstant(''), '') == None


from python_code import iot_Expression
from python_code import iot_Variable
from python_code import iot_VariableRef

def test_iot_Variable___init__():
    assert iot_Variable.__init__(iot_Variable('', iot_Variable=iot_Expression(), iot_Variable69=iot_VariableRef()), '', iot_Variable=iot_Expression(), iot_Variable69=iot_VariableRef()) == None

