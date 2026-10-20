from python_code import imp_Binary
from python_code import imp_Expr

def test_imp_Binary___init__():
    assert imp_Binary.__init__(imp_Binary('', imp_Binary=imp_Expr(), imp_Binary23=imp_Expr()), '', imp_Binary=imp_Expr(), imp_Binary23=imp_Expr()) == None


from python_code import imp_BoolConst

def test_imp_BoolConst___init__():
    assert imp_BoolConst.__init__(imp_BoolConst(True), False) == None


from python_code import imp_BoolValue

def test_imp_BoolValue___init__():
    assert imp_BoolValue.__init__(imp_BoolValue(True), False) == None


from python_code import imp_Class
from python_code import imp_NewClass
from python_code import imp_Program

def test_imp_Class___init__():
    assert imp_Class.__init__(imp_Class('', imp_Class=imp_Program(), imp_Class45=set(), imp_Class47=set(), imp_Class50=imp_NewClass()), '', imp_Class=imp_Program(), imp_Class45=set(), imp_Class47=set(), imp_Class50=imp_NewClass()) == None


from python_code import imp_Declaration
from python_code import imp_Expr

def test_imp_Declaration___init__():
    assert imp_Declaration.__init__(imp_Declaration('', imp_Declaration=imp_Expr(), imp_Declaration2=imp_Expr()), '', imp_Declaration=imp_Expr(), imp_Declaration2=imp_Expr()) == None


from python_code import imp_IntConst

def test_imp_IntConst___init__():
    assert imp_IntConst.__init__(imp_IntConst(0), 0) == None


from python_code import imp_IntValue

def test_imp_IntValue___init__():
    assert imp_IntValue.__init__(imp_IntValue(0), 0) == None


from python_code import imp_Expr
from python_code import imp_Member
from python_code import imp_Project

def test_imp_Project___init__():
    assert imp_Project.__init__(imp_Project(False, imp_Project=imp_Expr(), imp_Project59=imp_Member(), imp_Project61=set()), False, imp_Project=imp_Expr(), imp_Project59=imp_Member(), imp_Project61=set()) == None


from python_code import imp_StringConst

def test_imp_StringConst___init__():
    assert imp_StringConst.__init__(imp_StringConst(''), '') == None


from python_code import imp_Store
from python_code import imp_StringToValueMap
from python_code import imp_Value

def test_imp_StringToValueMap___init__():
    assert imp_StringToValueMap.__init__(imp_StringToValueMap('', imp_StringToValueMap=imp_Store(), imp_StringToValueMap27=imp_Value()), '', imp_StringToValueMap=imp_Store(), imp_StringToValueMap27=imp_Value()) == None


from python_code import imp_StringValue

def test_imp_StringValue___init__():
    assert imp_StringValue.__init__(imp_StringValue(''), '') == None


from python_code import imp_Expr
from python_code import imp_Unary

def test_imp_Unary___init__():
    assert imp_Unary.__init__(imp_Unary('', imp_Unary=imp_Expr()), '', imp_Unary=imp_Expr()) == None

