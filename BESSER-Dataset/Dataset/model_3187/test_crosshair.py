from python_code import myDsl_BoolConstant

def test_myDsl_BoolConstant___init__():
    assert myDsl_BoolConstant.__init__(myDsl_BoolConstant(''), '') == None


from python_code import myDsl_BoolType

def test_myDsl_BoolType___init__():
    assert myDsl_BoolType.__init__(myDsl_BoolType(''), '') == None


from python_code import myDsl_Comparison
from python_code import myDsl_Expression

def test_myDsl_Comparison___init__():
    assert myDsl_Comparison.__init__(myDsl_Comparison('', myDsl_Comparison=myDsl_Expression(), myDsl_Comparison39=myDsl_Expression()), '', myDsl_Comparison=myDsl_Expression(), myDsl_Comparison39=myDsl_Expression()) == None


from python_code import myDsl_Equality
from python_code import myDsl_Expression

def test_myDsl_Equality___init__():
    assert myDsl_Equality.__init__(myDsl_Equality('', myDsl_Equality=myDsl_Expression(), myDsl_Equality34=myDsl_Expression()), '', myDsl_Equality=myDsl_Expression(), myDsl_Equality34=myDsl_Expression()) == None


from python_code import myDsl_IntConstant

def test_myDsl_IntConstant___init__():
    assert myDsl_IntConstant.__init__(myDsl_IntConstant(0), 0) == None


from python_code import myDsl_IntType

def test_myDsl_IntType___init__():
    assert myDsl_IntType.__init__(myDsl_IntType(0), 0) == None


from python_code import myDsl_Expression
from python_code import myDsl_MulOrDiv

def test_myDsl_MulOrDiv___init__():
    assert myDsl_MulOrDiv.__init__(myDsl_MulOrDiv('', myDsl_MulOrDiv=myDsl_Expression(), myDsl_MulOrDiv54=myDsl_Expression()), '', myDsl_MulOrDiv=myDsl_Expression(), myDsl_MulOrDiv54=myDsl_Expression()) == None


from python_code import myDsl_StringConstant

def test_myDsl_StringConstant___init__():
    assert myDsl_StringConstant.__init__(myDsl_StringConstant(''), '') == None


from python_code import myDsl_StringType

def test_myDsl_StringType___init__():
    assert myDsl_StringType.__init__(myDsl_StringType(''), '') == None


from python_code import myDsl_Verb

def test_myDsl_Verb___init__():
    assert myDsl_Verb.__init__(myDsl_Verb('\x00\x00', '', myDsl_Verb=set()), '', '', myDsl_Verb=set()) == None

