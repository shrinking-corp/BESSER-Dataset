from python_code import behaviouralProgramMM_Assignment
from python_code import behaviouralProgramMM_Expression

def test_behaviouralProgramMM_Assignment___init__():
    assert behaviouralProgramMM_Assignment.__init__(behaviouralProgramMM_Assignment('', behaviouralProgramMM_Assignment=behaviouralProgramMM_Expression()), '', behaviouralProgramMM_Assignment=behaviouralProgramMM_Expression()) == None


from python_code import behaviouralProgramMM_Behaviour
from python_code import behaviouralProgramMM_Function

def test_behaviouralProgramMM_Function___init__():
    assert behaviouralProgramMM_Function.__init__(behaviouralProgramMM_Function('', behaviouralProgramMM_Function3=behaviouralProgramMM_Behaviour(), behaviouralProgramMM_Function5=set(), behaviouralProgramMM_Function=behaviouralProgramMM_Behaviour()), '', behaviouralProgramMM_Function3=behaviouralProgramMM_Behaviour(), behaviouralProgramMM_Function5=set(), behaviouralProgramMM_Function=behaviouralProgramMM_Behaviour()) == None


from python_code import behaviouralProgramMM_FunctionCall

def test_behaviouralProgramMM_FunctionCall___init__():
    assert behaviouralProgramMM_FunctionCall.__init__(behaviouralProgramMM_FunctionCall('', behaviouralProgramMM_FunctionCall=set()), '', behaviouralProgramMM_FunctionCall=set()) == None


from python_code import behaviouralProgramMM_FunctionCallStatement

def test_behaviouralProgramMM_FunctionCallStatement___init__():
    assert behaviouralProgramMM_FunctionCallStatement.__init__(behaviouralProgramMM_FunctionCallStatement('', behaviouralProgramMM_FunctionCallStatement=set()), '', behaviouralProgramMM_FunctionCallStatement=set()) == None


from python_code import behaviouralProgramMM_Expression
from python_code import behaviouralProgramMM_Instantiation

def test_behaviouralProgramMM_Instantiation___init__():
    assert behaviouralProgramMM_Instantiation.__init__(behaviouralProgramMM_Instantiation('', '\x00', behaviouralProgramMM_Instantiation=behaviouralProgramMM_Expression()), '\x00\x00', '', behaviouralProgramMM_Instantiation=behaviouralProgramMM_Expression()) == None


from python_code import behaviouralProgramMM_Literal

def test_behaviouralProgramMM_Literal___init__():
    assert behaviouralProgramMM_Literal.__init__(behaviouralProgramMM_Literal(''), '') == None


from python_code import behaviouralProgramMM_Variable

def test_behaviouralProgramMM_Variable___init__():
    assert behaviouralProgramMM_Variable.__init__(behaviouralProgramMM_Variable(''), '') == None

