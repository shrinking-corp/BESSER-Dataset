from python_code import expressions_BoolConstant

def test_expressions_BoolConstant___init__():
    assert expressions_BoolConstant.__init__(expressions_BoolConstant(''), '') == None


from python_code import expressions_IntConstant

def test_expressions_IntConstant___init__():
    assert expressions_IntConstant.__init__(expressions_IntConstant(0), 0) == None


from python_code import expressions_StringConstant

def test_expressions_StringConstant___init__():
    assert expressions_StringConstant.__init__(expressions_StringConstant(''), '') == None


from python_code import expressions_Expression
from python_code import expressions_Variable
from python_code import expressions_VariableRef

def test_expressions_Variable___init__():
    assert expressions_Variable.__init__(expressions_Variable('', expressions_Variable=expressions_Expression(), expressions_Variable8=expressions_VariableRef()), '', expressions_Variable=expressions_Expression(), expressions_Variable8=expressions_VariableRef()) == None

