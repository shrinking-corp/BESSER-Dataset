from python_code import myDsl_Assign
from python_code import myDsl_Expr

def test_myDsl_Assign___init__():
    assert myDsl_Assign.__init__(myDsl_Assign('', myDsl_Assign=myDsl_Expr(), myDsl_Assign37=myDsl_Expr()), '', myDsl_Assign=myDsl_Expr(), myDsl_Assign37=myDsl_Expr()) == None


from python_code import myDsl_Bool

def test_myDsl_Bool___init__():
    assert myDsl_Bool.__init__(myDsl_Bool(True), False) == None


from python_code import myDsl_Def
from python_code import myDsl_Expr

def test_myDsl_Def___init__():
    assert myDsl_Def.__init__(myDsl_Def('', myDsl_Def=myDsl_Expr()), '', myDsl_Def=myDsl_Expr()) == None


from python_code import myDsl_BObject
from python_code import myDsl_Expr
from python_code import myDsl_Field

def test_myDsl_Field___init__():
    assert myDsl_Field.__init__(myDsl_Field('', myDsl_Field=myDsl_BObject(), myDsl_Field95=myDsl_Expr()), '', myDsl_Field=myDsl_BObject(), myDsl_Field95=myDsl_Expr()) == None


from python_code import myDsl_Expr
from python_code import myDsl_Fun

def test_myDsl_Fun___init__():
    assert myDsl_Fun.__init__(myDsl_Fun('', myDsl_Fun=myDsl_Expr()), '', myDsl_Fun=myDsl_Expr()) == None


from python_code import myDsl_Int

def test_myDsl_Int___init__():
    assert myDsl_Int.__init__(myDsl_Int(0), 0) == None


from python_code import myDsl_Expr
from python_code import myDsl_Let

def test_myDsl_Let___init__():
    assert myDsl_Let.__init__(myDsl_Let('', myDsl_Let=myDsl_Expr(), myDsl_Let30=myDsl_Expr()), '', myDsl_Let=myDsl_Expr(), myDsl_Let30=myDsl_Expr()) == None


from python_code import myDsl_Expr
from python_code import myDsl_Project

def test_myDsl_Project___init__():
    assert myDsl_Project.__init__(myDsl_Project('', myDsl_Project=myDsl_Expr()), '', myDsl_Project=myDsl_Expr()) == None


from python_code import myDsl_Var

def test_myDsl_Var___init__():
    assert myDsl_Var.__init__(myDsl_Var(''), '') == None

