from python_code import while_Program
from python_code import while_Val

def test_while_Val___init__():
    assert while_Val.__init__(while_Val('', while_Val=while_Program()), '', while_Val=while_Program()) == None


from python_code import while_Assignment
from python_code import while_Program
from python_code import while_Var
from python_code import while_VarExp

def test_while_Var___init__():
    assert while_Var.__init__(while_Var('', while_Var=while_Program(), while_Var25=while_VarExp(), while_Var27=while_Assignment()), '', while_Var=while_Program(), while_Var25=while_VarExp(), while_Var27=while_Assignment()) == None

