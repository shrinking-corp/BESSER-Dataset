from python_code import imp_Assign
from python_code import imp_Expr

def test_imp_Assign___init__():
    assert imp_Assign.__init__(imp_Assign('', imp_Assign=imp_Expr()), '', imp_Assign=imp_Expr()) == None


from python_code import imp_Binary
from python_code import imp_Expr

def test_imp_Binary___init__():
    assert imp_Binary.__init__(imp_Binary('', imp_Binary20=imp_Expr(), imp_Binary=imp_Expr()), '', imp_Binary20=imp_Expr(), imp_Binary=imp_Expr()) == None


from python_code import imp_BoolValue

def test_imp_BoolValue___init__():
    assert imp_BoolValue.__init__(imp_BoolValue(True), False) == None


from python_code import imp_IntConst

def test_imp_IntConst___init__():
    assert imp_IntConst.__init__(imp_IntConst(0), 0) == None


from python_code import imp_IntValue

def test_imp_IntValue___init__():
    assert imp_IntValue.__init__(imp_IntValue(0), 0) == None


from python_code import imp_Store
from python_code import imp_StringToValueMap
from python_code import imp_Value

def test_imp_StringToValueMap___init__():
    assert imp_StringToValueMap.__init__(imp_StringToValueMap('', imp_StringToValueMap=imp_Store(), imp_StringToValueMap24=imp_Value()), '', imp_StringToValueMap=imp_Store(), imp_StringToValueMap24=imp_Value()) == None


from python_code import imp_Expr
from python_code import imp_Unary

def test_imp_Unary___init__():
    assert imp_Unary.__init__(imp_Unary('', imp_Unary=imp_Expr()), '', imp_Unary=imp_Expr()) == None


from python_code import imp_Var

def test_imp_Var___init__():
    assert imp_Var.__init__(imp_Var(''), '') == None

