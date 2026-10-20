from python_code import boa_Assign
from python_code import boa_Expr

def test_boa_Assign___init__():
    assert boa_Assign.__init__(boa_Assign('', boa_Assign=boa_Expr(), boa_Assign50=boa_Expr()), '', boa_Assign=boa_Expr(), boa_Assign50=boa_Expr()) == None


from python_code import boa_Bool

def test_boa_Bool___init__():
    assert boa_Bool.__init__(boa_Bool(True), False) == None


from python_code import boa_Def
from python_code import boa_Expr

def test_boa_Def___init__():
    assert boa_Def.__init__(boa_Def('', boa_Def=boa_Expr()), '', boa_Def=boa_Expr()) == None


from python_code import boa_EvalBoolRes

def test_boa_EvalBoolRes___init__():
    assert boa_EvalBoolRes.__init__(boa_EvalBoolRes(True), False) == None


from python_code import boa_Ctx
from python_code import boa_EvalFunRes
from python_code import boa_Expr

def test_boa_EvalFunRes___init__():
    assert boa_EvalFunRes.__init__(boa_EvalFunRes('', boa_EvalFunRes78=boa_Ctx(), boa_EvalFunRes=boa_Expr()), '', boa_EvalFunRes78=boa_Ctx(), boa_EvalFunRes=boa_Expr()) == None


from python_code import boa_EvalIntRes

def test_boa_EvalIntRes___init__():
    assert boa_EvalIntRes.__init__(boa_EvalIntRes(0), 0) == None


from python_code import boa_BObject
from python_code import boa_Expr
from python_code import boa_Field

def test_boa_Field___init__():
    assert boa_Field.__init__(boa_Field('', boa_Field=boa_BObject(), boa_Field11=boa_Expr()), '', boa_Field=boa_BObject(), boa_Field11=boa_Expr()) == None


from python_code import boa_Expr
from python_code import boa_Fun

def test_boa_Fun___init__():
    assert boa_Fun.__init__(boa_Fun('', boa_Fun=boa_Expr()), '', boa_Fun=boa_Expr()) == None


from python_code import boa_Int

def test_boa_Int___init__():
    assert boa_Int.__init__(boa_Int(0), 0) == None


from python_code import boa_Expr
from python_code import boa_Let

def test_boa_Let___init__():
    assert boa_Let.__init__(boa_Let('', boa_Let=boa_Expr(), boa_Let43=boa_Expr()), '', boa_Let=boa_Expr(), boa_Let43=boa_Expr()) == None


from python_code import boa_Expr
from python_code import boa_Project

def test_boa_Project___init__():
    assert boa_Project.__init__(boa_Project('', boa_Project=boa_Expr()), '', boa_Project=boa_Expr()) == None


from python_code import boa_Ctx
from python_code import boa_EvalBoundFunRes
from python_code import boa_EvalMapRes
from python_code import boa_EvalRes
from python_code import boa_StringToEvalResMap

def test_boa_StringToEvalResMap___init__():
    assert boa_StringToEvalResMap.__init__(boa_StringToEvalResMap('', boa_StringToEvalResMap81=boa_EvalBoundFunRes(), boa_StringToEvalResMap=boa_Ctx(), boa_StringToEvalResMap70=boa_Ctx(), boa_StringToEvalResMap72=boa_EvalRes(), boa_StringToEvalResMap74=boa_EvalMapRes()), '', boa_StringToEvalResMap81=boa_EvalBoundFunRes(), boa_StringToEvalResMap=boa_Ctx(), boa_StringToEvalResMap70=boa_Ctx(), boa_StringToEvalResMap72=boa_EvalRes(), boa_StringToEvalResMap74=boa_EvalMapRes()) == None


from python_code import boa_Var

def test_boa_Var___init__():
    assert boa_Var.__init__(boa_Var(''), '') == None

