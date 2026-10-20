from python_code import wh_Affect

def test_wh_Affect___init__():
    assert wh_Affect.__init__(wh_Affect('', wh_Affect=set()), '', wh_Affect=set()) == None


from python_code import wh_ExprAnd
from python_code import wh_ExprEq
from python_code import wh_ExprOr
from python_code import wh_ExprSimple

def test_wh_ExprSimple___init__():
    assert wh_ExprSimple.__init__(wh_ExprSimple('', '', '\x00\x00', wh_ExprSimple42=wh_ExprOr(), wh_ExprSimple=wh_ExprAnd(), wh_ExprSimple59=wh_ExprEq(), wh_ExprSimple62=wh_ExprEq()), '', '', '', wh_ExprSimple42=wh_ExprOr(), wh_ExprSimple=wh_ExprAnd(), wh_ExprSimple59=wh_ExprEq(), wh_ExprSimple62=wh_ExprEq()) == None


from python_code import wh_ExprSym

def test_wh_ExprSym___init__():
    assert wh_ExprSym.__init__(wh_ExprSym('', wh_ExprSym=set()), '', wh_ExprSym=set()) == None


from python_code import wh_Definition
from python_code import wh_Function
from python_code import wh_Program

def test_wh_Function___init__():
    assert wh_Function.__init__(wh_Function('', wh_Function=wh_Program(), wh_Function4=wh_Definition()), '', wh_Function=wh_Program(), wh_Function4=wh_Definition()) == None


from python_code import wh_Definition
from python_code import wh_Input

def test_wh_Input___init__():
    assert wh_Input.__init__(wh_Input('', wh_Input=wh_Definition()), '', wh_Input=wh_Definition()) == None


from python_code import wh_Nop

def test_wh_Nop___init__():
    assert wh_Nop.__init__(wh_Nop(''), '') == None


from python_code import wh_Definition
from python_code import wh_Output

def test_wh_Output___init__():
    assert wh_Output.__init__(wh_Output('', wh_Output=wh_Definition()), '', wh_Output=wh_Definition()) == None

