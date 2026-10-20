from python_code import behaviour_AssignmentStatement
from python_code import behaviour_Expression

def test_behaviour_AssignmentStatement___init__():
    assert behaviour_AssignmentStatement.__init__(behaviour_AssignmentStatement('', behaviour_AssignmentStatement=behaviour_Expression()), '', behaviour_AssignmentStatement=behaviour_Expression()) == None


from python_code import behaviour_CallFunctionStatement

def test_behaviour_CallFunctionStatement___init__():
    assert behaviour_CallFunctionStatement.__init__(behaviour_CallFunctionStatement('', behaviour_CallFunctionStatement=set()), '', behaviour_CallFunctionStatement=set()) == None


from python_code import behaviour_DeclarationStatement
from python_code import behaviour_Expression

def test_behaviour_DeclarationStatement___init__():
    assert behaviour_DeclarationStatement.__init__(behaviour_DeclarationStatement('', '\x00', behaviour_DeclarationStatement=behaviour_Expression()), '\x00\x00', '', behaviour_DeclarationStatement=behaviour_Expression()) == None


from python_code import behaviour_Behaviour
from python_code import behaviour_Function

def test_behaviour_Function___init__():
    assert behaviour_Function.__init__(behaviour_Function('', behaviour_Function=behaviour_Behaviour(), behaviour_Function3=behaviour_Behaviour(), behaviour_Function5=set()), '', behaviour_Function=behaviour_Behaviour(), behaviour_Function3=behaviour_Behaviour(), behaviour_Function5=set()) == None


from python_code import behaviour_FunctionCall

def test_behaviour_FunctionCall___init__():
    assert behaviour_FunctionCall.__init__(behaviour_FunctionCall('', behaviour_FunctionCall=set()), '', behaviour_FunctionCall=set()) == None


from python_code import behaviour_Literal

def test_behaviour_Literal___init__():
    assert behaviour_Literal.__init__(behaviour_Literal(''), '') == None


from python_code import behaviour_Variable

def test_behaviour_Variable___init__():
    assert behaviour_Variable.__init__(behaviour_Variable(''), '') == None

