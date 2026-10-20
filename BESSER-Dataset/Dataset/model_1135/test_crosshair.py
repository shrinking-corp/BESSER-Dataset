from python_code import gpfl_Field
from python_code import gpfl_GExpression
from python_code import gpfl_SendCmd

def test_gpfl_Field___init__():
    assert gpfl_Field.__init__(gpfl_Field('', gpfl_Field=gpfl_GExpression(), gpfl_Field40=gpfl_SendCmd()), '', gpfl_Field=gpfl_GExpression(), gpfl_Field40=gpfl_SendCmd()) == None


from python_code import gpfl_IntLitCmd

def test_gpfl_IntLitCmd___init__():
    assert gpfl_IntLitCmd.__init__(gpfl_IntLitCmd(0), 0) == None


from python_code import gpfl_GExpression
from python_code import gpfl_InterruptStmt

def test_gpfl_InterruptStmt___init__():
    assert gpfl_InterruptStmt.__init__(gpfl_InterruptStmt(0, gpfl_InterruptStmt=gpfl_GExpression(), gpfl_InterruptStmt34=set()), 0, gpfl_InterruptStmt=gpfl_GExpression(), gpfl_InterruptStmt34=set()) == None


from python_code import gpfl_PortLit

def test_gpfl_PortLit___init__():
    assert gpfl_PortLit.__init__(gpfl_PortLit(True), False) == None


from python_code import gpfl_GExpression
from python_code import gpfl_SetCmd

def test_gpfl_SetCmd___init__():
    assert gpfl_SetCmd.__init__(gpfl_SetCmd('', gpfl_SetCmd=gpfl_GExpression()), '', gpfl_SetCmd=gpfl_GExpression()) == None


from python_code import gpfl_StringLit

def test_gpfl_StringLit___init__():
    assert gpfl_StringLit.__init__(gpfl_StringLit(''), '') == None


from python_code import gpfl_Variable

def test_gpfl_Variable___init__():
    assert gpfl_Variable.__init__(gpfl_Variable(''), '') == None

