from python_code import cal_AstActorVariable
from python_code import cal_AstActorVariableReference
from python_code import cal_AstEntity
from python_code import cal_AstNetwork

def test_cal_AstActorVariable___init__():
    assert cal_AstActorVariable.__init__(cal_AstActorVariable('\x00', cal_AstActorVariable38=cal_AstEntity(), cal_AstActorVariable41=set(), cal_AstActorVariable=cal_AstNetwork(), cal_AstActorVariable55=cal_AstActorVariableReference()), '', cal_AstActorVariable38=cal_AstEntity(), cal_AstActorVariable41=set(), cal_AstActorVariable=cal_AstNetwork(), cal_AstActorVariable55=cal_AstActorVariableReference()) == None


from python_code import cal_AstActorVariableReference
from python_code import cal_AstConnection
from python_code import cal_AstStructure

def test_cal_AstConnection___init__():
    assert cal_AstConnection.__init__(cal_AstConnection('\x00\x00', '', cal_AstConnection=cal_AstStructure(), cal_AstConnection47=cal_AstActorVariableReference(), cal_AstConnection49=cal_AstActorVariableReference(), cal_AstConnection52=set()), '', '', cal_AstConnection=cal_AstStructure(), cal_AstConnection47=cal_AstActorVariableReference(), cal_AstConnection49=cal_AstActorVariableReference(), cal_AstConnection52=set()) == None


from python_code import cal_AstExpression
from python_code import cal_AstExpressionBinary

def test_cal_AstExpressionBinary___init__():
    assert cal_AstExpressionBinary.__init__(cal_AstExpressionBinary('', cal_AstExpressionBinary=cal_AstExpression(), cal_AstExpressionBinary301=cal_AstExpression()), '', cal_AstExpressionBinary=cal_AstExpression(), cal_AstExpressionBinary301=cal_AstExpression()) == None


from python_code import cal_AstExpressionBoolean

def test_cal_AstExpressionBoolean___init__():
    assert cal_AstExpressionBoolean.__init__(cal_AstExpressionBoolean(True), False) == None


from python_code import cal_AstExpressionFloat

def test_cal_AstExpressionFloat___init__():
    assert cal_AstExpressionFloat.__init__(cal_AstExpressionFloat(0.0), 0.0) == None


from python_code import cal_AstExpressionInteger

def test_cal_AstExpressionInteger___init__():
    assert cal_AstExpressionInteger.__init__(cal_AstExpressionInteger(''), '') == None


from python_code import cal_AstExpressionString

def test_cal_AstExpressionString___init__():
    assert cal_AstExpressionString.__init__(cal_AstExpressionString(''), '') == None


from python_code import cal_AstExpression
from python_code import cal_AstExpressionUnary

def test_cal_AstExpressionUnary___init__():
    assert cal_AstExpressionUnary.__init__(cal_AstExpressionUnary('', cal_AstExpressionUnary=cal_AstExpression()), '', cal_AstExpressionUnary=cal_AstExpression()) == None


from python_code import cal_AstExpressionVariable
from python_code import cal_AstMemberAccess
from python_code import cal_AstStatementAssign

def test_cal_AstMemberAccess___init__():
    assert cal_AstMemberAccess.__init__(cal_AstMemberAccess('', cal_AstMemberAccess264=cal_AstExpressionVariable(), cal_AstMemberAccess=cal_AstStatementAssign(), cal_AstMemberAccess294=set()), '', cal_AstMemberAccess264=cal_AstExpressionVariable(), cal_AstMemberAccess=cal_AstStatementAssign(), cal_AstMemberAccess294=set()) == None


from python_code import cal_AstSchedule
from python_code import cal_AstState
from python_code import cal_AstTransition

def test_cal_AstState___init__():
    assert cal_AstState.__init__(cal_AstState('', cal_AstState=cal_AstSchedule(), cal_AstState145=cal_AstTransition(), cal_AstState151=cal_AstTransition()), '', cal_AstState=cal_AstSchedule(), cal_AstState145=cal_AstTransition(), cal_AstState151=cal_AstTransition()) == None


from python_code import cal_AstAction
from python_code import cal_AstInequality
from python_code import cal_AstTag
from python_code import cal_AstTransition

def test_cal_AstTag___init__():
    assert cal_AstTag.__init__(cal_AstTag('', cal_AstTag148=cal_AstTransition(), cal_AstTag157=cal_AstAction(), cal_AstTag=cal_AstInequality()), '', cal_AstTag148=cal_AstTransition(), cal_AstTag157=cal_AstAction(), cal_AstTag=cal_AstInequality()) == None

