from python_code import tym_BoolConstant

def test_tym_BoolConstant___init__():
    assert tym_BoolConstant.__init__(tym_BoolConstant(''), '') == None


from python_code import tym_Comparison
from python_code import tym_Expression

def test_tym_Comparison___init__():
    assert tym_Comparison.__init__(tym_Comparison('', tym_Comparison=tym_Expression(), tym_Comparison53=tym_Expression()), '', tym_Comparison=tym_Expression(), tym_Comparison53=tym_Expression()) == None


from python_code import tym_Equality
from python_code import tym_Expression

def test_tym_Equality___init__():
    assert tym_Equality.__init__(tym_Equality('', tym_Equality=tym_Expression(), tym_Equality48=tym_Expression()), '', tym_Equality=tym_Expression(), tym_Equality48=tym_Expression()) == None


from python_code import tym_Function
from python_code import tym_FunctionBlock
from python_code import tym_FunctionCall

def test_tym_Function___init__():
    assert tym_Function.__init__(tym_Function('\x00\x00', '', tym_Function=set(), tym_Function32=tym_FunctionCall(), tym_Function9=tym_FunctionBlock()), '', '', tym_Function=set(), tym_Function32=tym_FunctionCall(), tym_Function9=tym_FunctionBlock()) == None


from python_code import tym_IntConstant

def test_tym_IntConstant___init__():
    assert tym_IntConstant.__init__(tym_IntConstant(0), 0) == None


from python_code import tym_Expression
from python_code import tym_MulOrDiv

def test_tym_MulOrDiv___init__():
    assert tym_MulOrDiv.__init__(tym_MulOrDiv('', tym_MulOrDiv=tym_Expression(), tym_MulOrDiv68=tym_Expression()), '', tym_MulOrDiv=tym_Expression(), tym_MulOrDiv68=tym_Expression()) == None


from python_code import tym_StringConstant

def test_tym_StringConstant___init__():
    assert tym_StringConstant.__init__(tym_StringConstant(''), '') == None

