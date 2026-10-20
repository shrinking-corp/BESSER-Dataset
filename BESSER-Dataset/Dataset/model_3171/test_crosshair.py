from python_code import expressions_BoolConstant

def test_expressions_BoolConstant___init__():
    assert expressions_BoolConstant.__init__(expressions_BoolConstant(''), '') == None


from python_code import expressions_Comparison
from python_code import expressions_Expression

def test_expressions_Comparison___init__():
    assert expressions_Comparison.__init__(expressions_Comparison('', expressions_Comparison35=expressions_Expression(), expressions_Comparison=expressions_Expression()), '', expressions_Comparison35=expressions_Expression(), expressions_Comparison=expressions_Expression()) == None


from python_code import expressions_Equality
from python_code import expressions_Expression

def test_expressions_Equality___init__():
    assert expressions_Equality.__init__(expressions_Equality('', expressions_Equality=expressions_Expression(), expressions_Equality30=expressions_Expression()), '', expressions_Equality=expressions_Expression(), expressions_Equality30=expressions_Expression()) == None


from python_code import expressions_IntConstant

def test_expressions_IntConstant___init__():
    assert expressions_IntConstant.__init__(expressions_IntConstant(0), 0) == None


from python_code import expressions_Expression
from python_code import expressions_MulOrDiv

def test_expressions_MulOrDiv___init__():
    assert expressions_MulOrDiv.__init__(expressions_MulOrDiv('', expressions_MulOrDiv=expressions_Expression(), expressions_MulOrDiv15=expressions_Expression()), '', expressions_MulOrDiv=expressions_Expression(), expressions_MulOrDiv15=expressions_Expression()) == None


from python_code import expressions_StringConstant

def test_expressions_StringConstant___init__():
    assert expressions_StringConstant.__init__(expressions_StringConstant(''), '') == None


from python_code import expressions_Expression
from python_code import expressions_Variable
from python_code import expressions_VariableRef

def test_expressions_Variable___init__():
    assert expressions_Variable.__init__(expressions_Variable('', expressions_Variable=expressions_Expression(), expressions_Variable38=expressions_VariableRef()), '', expressions_Variable=expressions_Expression(), expressions_Variable38=expressions_VariableRef()) == None

