from python_code import gfsm_ConstExpr

def test_gfsm_ConstExpr___init__():
    assert gfsm_ConstExpr.__init__(gfsm_ConstExpr(0), 0) == None


from python_code import gfsm_IntBlock
from python_code import gfsm_IntExpression
from python_code import gfsm_IntVarAssign

def test_gfsm_IntVarAssign___init__():
    assert gfsm_IntVarAssign.__init__(gfsm_IntVarAssign('', gfsm_IntVarAssign=gfsm_IntExpression(), gfsm_IntVarAssign32=gfsm_IntBlock()), '', gfsm_IntVarAssign=gfsm_IntExpression(), gfsm_IntVarAssign32=gfsm_IntBlock()) == None


from python_code import gfsm_IntVarRef

def test_gfsm_IntVarRef___init__():
    assert gfsm_IntVarRef.__init__(gfsm_IntVarRef(''), '') == None

