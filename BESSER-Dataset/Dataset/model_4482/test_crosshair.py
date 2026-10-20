from python_code import Logo_ArithmeticExpr

def test_Logo_ArithmeticExpr___init__():
    assert Logo_ArithmeticExpr.__init__(Logo_ArithmeticExpr(''), '') == None


from python_code import Logo_Boolean

def test_Logo_Boolean___init__():
    assert Logo_Boolean.__init__(Logo_Boolean(True), False) == None


from python_code import Logo_BooleanExpr

def test_Logo_BooleanExpr___init__():
    assert Logo_BooleanExpr.__init__(Logo_BooleanExpr(''), '') == None


from python_code import Logo_Double

def test_Logo_Double___init__():
    assert Logo_Double.__init__(Logo_Double(0.0), 0.0) == None


from python_code import Logo_Integer

def test_Logo_Integer___init__():
    assert Logo_Integer.__init__(Logo_Integer(0), 0) == None


from python_code import Logo_Block
from python_code import Logo_Literal
from python_code import Logo_Procedure
from python_code import Logo_ProcedureCall

def test_Logo_Procedure___init__():
    assert Logo_Procedure.__init__(Logo_Procedure('', Logo_Procedure=Logo_Block(), Logo_Procedure32=Logo_Literal(), Logo_Procedure34=Logo_ProcedureCall()), '', Logo_Procedure=Logo_Block(), Logo_Procedure32=Logo_Literal(), Logo_Procedure34=Logo_ProcedureCall()) == None


from python_code import Logo_String

def test_Logo_String___init__():
    assert Logo_String.__init__(Logo_String(''), '') == None


from python_code import Logo_Assignation
from python_code import Logo_Expression
from python_code import Logo_VarDecl
from python_code import Logo_VarReference

def test_Logo_VarDecl___init__():
    assert Logo_VarDecl.__init__(Logo_VarDecl('', Logo_VarDecl=Logo_Expression(), Logo_VarDecl11=Logo_VarReference(), Logo_VarDecl36=Logo_Assignation()), '', Logo_VarDecl=Logo_Expression(), Logo_VarDecl11=Logo_VarReference(), Logo_VarDecl36=Logo_Assignation()) == None

