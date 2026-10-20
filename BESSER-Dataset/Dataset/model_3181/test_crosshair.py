from python_code import expressionDSL_BooleanConstant

def test_expressionDSL_BooleanConstant___init__():
    assert expressionDSL_BooleanConstant.__init__(expressionDSL_BooleanConstant(''), '') == None


from python_code import expressionDSL_Comparison
from python_code import expressionDSL_Expression

def test_expressionDSL_Comparison___init__():
    assert expressionDSL_Comparison.__init__(expressionDSL_Comparison('', expressionDSL_Comparison=expressionDSL_Expression(), expressionDSL_Comparison37=expressionDSL_Expression()), '', expressionDSL_Comparison=expressionDSL_Expression(), expressionDSL_Comparison37=expressionDSL_Expression()) == None


from python_code import expressionDSL_FunctionCall
from python_code import expressionDSL_FunctionDef

def test_expressionDSL_FunctionDef___init__():
    assert expressionDSL_FunctionDef.__init__(expressionDSL_FunctionDef('', expressionDSL_FunctionDef=expressionDSL_FunctionCall()), '', expressionDSL_FunctionDef=expressionDSL_FunctionCall()) == None


from python_code import expressionDSL_IntConstant

def test_expressionDSL_IntConstant___init__():
    assert expressionDSL_IntConstant.__init__(expressionDSL_IntConstant(0), 0) == None


from python_code import expressionDSL_Expression
from python_code import expressionDSL_MulOrDiv

def test_expressionDSL_MulOrDiv___init__():
    assert expressionDSL_MulOrDiv.__init__(expressionDSL_MulOrDiv('', expressionDSL_MulOrDiv=expressionDSL_Expression(), expressionDSL_MulOrDiv52=expressionDSL_Expression()), '', expressionDSL_MulOrDiv=expressionDSL_Expression(), expressionDSL_MulOrDiv52=expressionDSL_Expression()) == None


from python_code import expressionDSL_Named
from python_code import expressionDSL_VariableArrayOrFunctionRef

def test_expressionDSL_Named___init__():
    assert expressionDSL_Named.__init__(expressionDSL_Named('', expressionDSL_Named=expressionDSL_VariableArrayOrFunctionRef()), '', expressionDSL_Named=expressionDSL_VariableArrayOrFunctionRef()) == None


from python_code import expressionDSL_StringConstant

def test_expressionDSL_StringConstant___init__():
    assert expressionDSL_StringConstant.__init__(expressionDSL_StringConstant(''), '') == None

