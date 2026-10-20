from python_code import wh_ExprEq
from python_code import wh_ExprNot
from python_code import wh_ExprOr

def test_wh_ExprNot___init__():
    assert wh_ExprNot.__init__(wh_ExprNot('', wh_ExprNot72=wh_ExprEq(), wh_ExprNot=wh_ExprOr(), wh_ExprNot70=wh_ExprOr()), '', wh_ExprNot72=wh_ExprEq(), wh_ExprNot=wh_ExprOr(), wh_ExprNot70=wh_ExprOr()) == None


from python_code import wh_Cons
from python_code import wh_Expr
from python_code import wh_ExprEq
from python_code import wh_ExprSimple
from python_code import wh_ListExpr

def test_wh_ExprSimple___init__():
    assert wh_ExprSimple.__init__(wh_ExprSimple('', '\x00', wh_ExprSimple75=wh_ExprEq(), wh_ExprSimple78=wh_ExprEq(), wh_ExprSimple=wh_Cons(), wh_ExprSimple49=wh_ListExpr(), wh_ExprSimple51=wh_Expr(), wh_ExprSimple54=wh_Expr()), '\x00\x00', '', wh_ExprSimple75=wh_ExprEq(), wh_ExprSimple78=wh_ExprEq(), wh_ExprSimple=wh_Cons(), wh_ExprSimple49=wh_ListExpr(), wh_ExprSimple51=wh_Expr(), wh_ExprSimple54=wh_Expr()) == None


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


from python_code import wh_Definition
from python_code import wh_Program
from python_code import wh_Wh

def test_wh_Program___init__():
    assert wh_Program.__init__(wh_Program('', wh_Program=wh_Wh(), wh_Program2=wh_Definition()), '', wh_Program=wh_Wh(), wh_Program2=wh_Definition()) == None


from python_code import wh_Affect
from python_code import wh_Vars

def test_wh_Vars___init__():
    assert wh_Vars.__init__(wh_Vars('', wh_Vars=wh_Affect()), '', wh_Vars=wh_Affect()) == None

