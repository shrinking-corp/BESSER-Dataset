from python_code import whileDsl_ExprEq
from python_code import whileDsl_ExprNot
from python_code import whileDsl_ExprOr

def test_whileDsl_ExprNot___init__():
    assert whileDsl_ExprNot.__init__(whileDsl_ExprNot(True, whileDsl_ExprNot=whileDsl_ExprOr(), whileDsl_ExprNot55=whileDsl_ExprEq()), False, whileDsl_ExprNot=whileDsl_ExprOr(), whileDsl_ExprNot55=whileDsl_ExprEq()) == None


from python_code import whileDsl_EObject
from python_code import whileDsl_ExprEq
from python_code import whileDsl_ExprSimple

def test_whileDsl_ExprSimple___init__():
    assert whileDsl_ExprSimple.__init__(whileDsl_ExprSimple('', whileDsl_ExprSimple58=whileDsl_ExprEq(), whileDsl_ExprSimple61=whileDsl_ExprEq(), whileDsl_ExprSimple=whileDsl_EObject()), '', whileDsl_ExprSimple58=whileDsl_ExprEq(), whileDsl_ExprSimple61=whileDsl_ExprEq(), whileDsl_ExprSimple=whileDsl_EObject()) == None


from python_code import whileDsl_Expr
from python_code import whileDsl_ExprSimpleWithExpr

def test_whileDsl_ExprSimpleWithExpr___init__():
    assert whileDsl_ExprSimpleWithExpr.__init__(whileDsl_ExprSimpleWithExpr('', whileDsl_ExprSimpleWithExpr=whileDsl_Expr()), '', whileDsl_ExprSimpleWithExpr=whileDsl_Expr()) == None


from python_code import whileDsl_ExprSimpleWithLExpr
from python_code import whileDsl_LExpr

def test_whileDsl_ExprSimpleWithLExpr___init__():
    assert whileDsl_ExprSimpleWithLExpr.__init__(whileDsl_ExprSimpleWithLExpr('', whileDsl_ExprSimpleWithLExpr=whileDsl_LExpr()), '', whileDsl_ExprSimpleWithLExpr=whileDsl_LExpr()) == None


from python_code import whileDsl_ExprSimpleWithSymbolLExpr
from python_code import whileDsl_LExpr

def test_whileDsl_ExprSimpleWithSymbolLExpr___init__():
    assert whileDsl_ExprSimpleWithSymbolLExpr.__init__(whileDsl_ExprSimpleWithSymbolLExpr('', whileDsl_ExprSimpleWithSymbolLExpr=whileDsl_LExpr()), '', whileDsl_ExprSimpleWithSymbolLExpr=whileDsl_LExpr()) == None


from python_code import whileDsl_Commands
from python_code import whileDsl_Expr
from python_code import whileDsl_ForeachCommand

def test_whileDsl_ForeachCommand___init__():
    assert whileDsl_ForeachCommand.__init__(whileDsl_ForeachCommand('', whileDsl_ForeachCommand=whileDsl_Expr(), whileDsl_ForeachCommand31=whileDsl_Commands()), '', whileDsl_ForeachCommand=whileDsl_Expr(), whileDsl_ForeachCommand31=whileDsl_Commands()) == None


from python_code import whileDsl_Definition
from python_code import whileDsl_Function
from python_code import whileDsl_Model

def test_whileDsl_Function___init__():
    assert whileDsl_Function.__init__(whileDsl_Function('', whileDsl_Function=whileDsl_Model(), whileDsl_Function2=whileDsl_Definition()), '', whileDsl_Function=whileDsl_Model(), whileDsl_Function2=whileDsl_Definition()) == None


from python_code import whileDsl_Definition
from python_code import whileDsl_Input

def test_whileDsl_Input___init__():
    assert whileDsl_Input.__init__(whileDsl_Input('', whileDsl_Input=whileDsl_Definition()), '', whileDsl_Input=whileDsl_Definition()) == None


from python_code import whileDsl_Definition
from python_code import whileDsl_Output

def test_whileDsl_Output___init__():
    assert whileDsl_Output.__init__(whileDsl_Output('', whileDsl_Output=whileDsl_Definition()), '', whileDsl_Output=whileDsl_Definition()) == None


from python_code import whileDsl_Vars
from python_code import whileDsl_VarsCommand

def test_whileDsl_Vars___init__():
    assert whileDsl_Vars.__init__(whileDsl_Vars('', whileDsl_Vars=whileDsl_VarsCommand()), '', whileDsl_Vars=whileDsl_VarsCommand()) == None

