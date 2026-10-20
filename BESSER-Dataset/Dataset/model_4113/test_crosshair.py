from python_code import while_l_Affect

def test_while_l_Affect___init__():
    assert while_l_Affect.__init__(while_l_Affect('', while_l_Affect=set()), '', while_l_Affect=set()) == None


from python_code import while_l_ExprSym

def test_while_l_ExprSym___init__():
    assert while_l_ExprSym.__init__(while_l_ExprSym('', while_l_ExprSym=set()), '', while_l_ExprSym=set()) == None


from python_code import while_l_Definition
from python_code import while_l_Function
from python_code import while_l_Program

def test_while_l_Function___init__():
    assert while_l_Function.__init__(while_l_Function('', while_l_Function=while_l_Program(), while_l_Function4=while_l_Definition()), '', while_l_Function=while_l_Program(), while_l_Function4=while_l_Definition()) == None


from python_code import while_l_Nop

def test_while_l_Nop___init__():
    assert while_l_Nop.__init__(while_l_Nop(''), '') == None


from python_code import while_l_Definition
from python_code import while_l_Output

def test_while_l_Output___init__():
    assert while_l_Output.__init__(while_l_Output('', while_l_Output=while_l_Definition()), '', while_l_Output=while_l_Definition()) == None

