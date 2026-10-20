from python_code import fmpl_ArithmeticExpression
from python_code import fmpl_Expression

def test_fmpl_ArithmeticExpression___init__():
    assert fmpl_ArithmeticExpression.__init__(fmpl_ArithmeticExpression('', fmpl_ArithmeticExpression=fmpl_Expression(), fmpl_ArithmeticExpression34=fmpl_Expression()), '', fmpl_ArithmeticExpression=fmpl_Expression(), fmpl_ArithmeticExpression34=fmpl_Expression()) == None


from python_code import fmpl_IntegerLit

def test_fmpl_IntegerLit___init__():
    assert fmpl_IntegerLit.__init__(fmpl_IntegerLit(0), 0) == None


from python_code import fmpl_Read

def test_fmpl_Read___init__():
    assert fmpl_Read.__init__(fmpl_Read(0, 0), 0, 0) == None


from python_code import fmpl_Cond
from python_code import fmpl_Expression
from python_code import fmpl_Relational

def test_fmpl_Relational___init__():
    assert fmpl_Relational.__init__(fmpl_Relational('', fmpl_Relational=fmpl_Cond(), fmpl_Relational26=fmpl_Expression(), fmpl_Relational29=fmpl_Expression()), '', fmpl_Relational=fmpl_Cond(), fmpl_Relational26=fmpl_Expression(), fmpl_Relational29=fmpl_Expression()) == None


from python_code import fmpl_StringLit

def test_fmpl_StringLit___init__():
    assert fmpl_StringLit.__init__(fmpl_StringLit(''), '') == None


from python_code import fmpl_Expression
from python_code import fmpl_VarDeclaration
from python_code import fmpl_VarReference

def test_fmpl_VarDeclaration___init__():
    assert fmpl_VarDeclaration.__init__(fmpl_VarDeclaration('', fmpl_VarDeclaration=fmpl_Expression(), fmpl_VarDeclaration40=fmpl_VarReference()), '', fmpl_VarDeclaration=fmpl_Expression(), fmpl_VarDeclaration40=fmpl_VarReference()) == None


from python_code import fmpl_VarReference
from python_code import fmpl_Write

def test_fmpl_Write___init__():
    assert fmpl_Write.__init__(fmpl_Write(0, 0, fmpl_Write=fmpl_VarReference()), 0, 0, fmpl_Write=fmpl_VarReference()) == None

