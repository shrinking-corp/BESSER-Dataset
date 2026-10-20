from python_code import iotdsl_BoolConstant

def test_iotdsl_BoolConstant___init__():
    assert iotdsl_BoolConstant.__init__(iotdsl_BoolConstant(''), '') == None


from python_code import iotdsl_Comparison
from python_code import iotdsl_Expression

def test_iotdsl_Comparison___init__():
    assert iotdsl_Comparison.__init__(iotdsl_Comparison('', iotdsl_Comparison49=iotdsl_Expression(), iotdsl_Comparison=iotdsl_Expression()), '', iotdsl_Comparison49=iotdsl_Expression(), iotdsl_Comparison=iotdsl_Expression()) == None


from python_code import iotdsl_Equality
from python_code import iotdsl_Expression

def test_iotdsl_Equality___init__():
    assert iotdsl_Equality.__init__(iotdsl_Equality('', iotdsl_Equality=iotdsl_Expression(), iotdsl_Equality44=iotdsl_Expression()), '', iotdsl_Equality=iotdsl_Expression(), iotdsl_Equality44=iotdsl_Expression()) == None


from python_code import iotdsl_IntConstant

def test_iotdsl_IntConstant___init__():
    assert iotdsl_IntConstant.__init__(iotdsl_IntConstant(0), 0) == None


from python_code import iotdsl_Expression
from python_code import iotdsl_MulOrDiv

def test_iotdsl_MulOrDiv___init__():
    assert iotdsl_MulOrDiv.__init__(iotdsl_MulOrDiv('', iotdsl_MulOrDiv=iotdsl_Expression(), iotdsl_MulOrDiv64=iotdsl_Expression()), '', iotdsl_MulOrDiv=iotdsl_Expression(), iotdsl_MulOrDiv64=iotdsl_Expression()) == None


from python_code import iotdsl_StringConstant

def test_iotdsl_StringConstant___init__():
    assert iotdsl_StringConstant.__init__(iotdsl_StringConstant(''), '') == None


from python_code import iotdsl_Expression
from python_code import iotdsl_Variable
from python_code import iotdsl_VariableRef

def test_iotdsl_Variable___init__():
    assert iotdsl_Variable.__init__(iotdsl_Variable('', iotdsl_Variable69=iotdsl_VariableRef(), iotdsl_Variable=iotdsl_Expression()), '', iotdsl_Variable69=iotdsl_VariableRef(), iotdsl_Variable=iotdsl_Expression()) == None

