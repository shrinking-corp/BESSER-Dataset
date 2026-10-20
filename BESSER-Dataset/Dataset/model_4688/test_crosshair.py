from python_code import simpleALEnv_ALVarRef

def test_simpleALEnv_ALVarRef___init__():
    assert simpleALEnv_ALVarRef.__init__(simpleALEnv_ALVarRef(''), '') == None


from python_code import simpleALEnv_ArithLit

def test_simpleALEnv_ArithLit___init__():
    assert simpleALEnv_ArithLit.__init__(simpleALEnv_ArithLit(0), 0) == None


from python_code import simpleALEnv_Arith
from python_code import simpleALEnv_Assign
from python_code import simpleALEnv_IfStmt

def test_simpleALEnv_Assign___init__():
    assert simpleALEnv_Assign.__init__(simpleALEnv_Assign('', simpleALEnv_Assign=simpleALEnv_Arith(), simpleALEnv_Assign8=simpleALEnv_IfStmt(), simpleALEnv_Assign11=simpleALEnv_IfStmt()), '', simpleALEnv_Assign=simpleALEnv_Arith(), simpleALEnv_Assign8=simpleALEnv_IfStmt(), simpleALEnv_Assign11=simpleALEnv_IfStmt()) == None


from python_code import simpleALEnv_Print

def test_simpleALEnv_Print___init__():
    assert simpleALEnv_Print.__init__(simpleALEnv_Print(''), '') == None


from python_code import simpleALEnv_RandRange

def test_simpleALEnv_RandRange___init__():
    assert simpleALEnv_RandRange.__init__(simpleALEnv_RandRange(0, 0), 0, 0) == None

