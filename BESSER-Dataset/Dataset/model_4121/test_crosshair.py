from python_code import myDsl_Expr
from python_code import myDsl_ExprSimple
from python_code import myDsl_Lexpr

def test_myDsl_ExprSimple___init__():
    assert myDsl_ExprSimple.__init__(myDsl_ExprSimple('', myDsl_ExprSimple=myDsl_Expr(), myDsl_ExprSimple62=myDsl_Lexpr(), myDsl_ExprSimple64=myDsl_Expr()), '', myDsl_ExprSimple=myDsl_Expr(), myDsl_ExprSimple62=myDsl_Lexpr(), myDsl_ExprSimple64=myDsl_Expr()) == None


from python_code import myDsl_Expr
from python_code import myDsl_ExprTerm

def test_myDsl_ExprTerm___init__():
    assert myDsl_ExprTerm.__init__(myDsl_ExprTerm('', '\x00', myDsl_ExprTerm=myDsl_Expr()), '\x00\x00', '', myDsl_ExprTerm=myDsl_Expr()) == None


from python_code import myDsl_Definiton
from python_code import myDsl_Function
from python_code import myDsl_Model

def test_myDsl_Function___init__():
    assert myDsl_Function.__init__(myDsl_Function('', myDsl_Function=myDsl_Model(), myDsl_Function2=myDsl_Definiton()), '', myDsl_Function=myDsl_Model(), myDsl_Function2=myDsl_Definiton()) == None


from python_code import myDsl_Definiton
from python_code import myDsl_Input

def test_myDsl_Input___init__():
    assert myDsl_Input.__init__(myDsl_Input('', '\x00', myDsl_Input=myDsl_Definiton()), '\x00\x00', '', myDsl_Input=myDsl_Definiton()) == None


from python_code import myDsl_Eq
from python_code import myDsl_Not
from python_code import myDsl_Or

def test_myDsl_Not___init__():
    assert myDsl_Not.__init__(myDsl_Not('', myDsl_Not=myDsl_Or(), myDsl_Not50=myDsl_Or(), myDsl_Not52=myDsl_Eq()), '', myDsl_Not=myDsl_Or(), myDsl_Not50=myDsl_Or(), myDsl_Not52=myDsl_Eq()) == None


from python_code import myDsl_Definiton
from python_code import myDsl_Output

def test_myDsl_Output___init__():
    assert myDsl_Output.__init__(myDsl_Output('', '\x00', myDsl_Output=myDsl_Definiton()), '\x00\x00', '', myDsl_Output=myDsl_Definiton()) == None

