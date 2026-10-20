from python_code import cal_AstActor
from python_code import cal_AstEntity
from python_code import cal_AstUnit

def test_cal_AstEntity___init__():
    assert cal_AstEntity.__init__(cal_AstEntity('', '', cal_AstEntity=set(), cal_AstEntity2=set(), cal_AstEntity4=cal_AstActor(), cal_AstEntity6=cal_AstUnit()), '', '', cal_AstEntity=set(), cal_AstEntity2=set(), cal_AstEntity4=cal_AstActor(), cal_AstEntity6=cal_AstUnit()) == None


from python_code import cal_AstState
from python_code import cal_AstTransition
from python_code import cal_ExternalTarget
from python_code import cal_Fsm
from python_code import cal_ScheduleFsm

def test_cal_AstState___init__():
    assert cal_AstState.__init__(cal_AstState('', '\x00', cal_AstState=cal_ScheduleFsm(), cal_AstState97=cal_Fsm(), cal_AstState100=cal_AstTransition(), cal_AstState106=cal_AstTransition(), cal_AstState114=cal_ExternalTarget(), cal_AstState117=cal_ExternalTarget(), cal_AstState120=cal_ExternalTarget()), '\x00\x00', '', cal_AstState=cal_ScheduleFsm(), cal_AstState97=cal_Fsm(), cal_AstState100=cal_AstTransition(), cal_AstState106=cal_AstTransition(), cal_AstState114=cal_ExternalTarget(), cal_AstState117=cal_ExternalTarget(), cal_AstState120=cal_ExternalTarget()) == None


from python_code import cal_AstAction
from python_code import cal_AstTag
from python_code import cal_AstTransition
from python_code import cal_Inequality
from python_code import cal_RegExpTag

def test_cal_AstTag___init__():
    assert cal_AstTag.__init__(cal_AstTag('', cal_AstTag=cal_Inequality(), cal_AstTag103=cal_AstTransition(), cal_AstTag132=cal_AstAction(), cal_AstTag279=cal_RegExpTag()), '', cal_AstTag=cal_Inequality(), cal_AstTag103=cal_AstTransition(), cal_AstTag132=cal_AstAction(), cal_AstTag279=cal_RegExpTag()) == None


from python_code import cal_AstExpression
from python_code import cal_ExpressionBinary

def test_cal_ExpressionBinary___init__():
    assert cal_ExpressionBinary.__init__(cal_ExpressionBinary('', cal_ExpressionBinary=cal_AstExpression(), cal_ExpressionBinary283=cal_AstExpression()), '', cal_ExpressionBinary=cal_AstExpression(), cal_ExpressionBinary283=cal_AstExpression()) == None


from python_code import cal_ExpressionBoolean

def test_cal_ExpressionBoolean___init__():
    assert cal_ExpressionBoolean.__init__(cal_ExpressionBoolean(True), False) == None


from python_code import cal_ExpressionFloat

def test_cal_ExpressionFloat___init__():
    assert cal_ExpressionFloat.__init__(cal_ExpressionFloat(0.0), 0.0) == None


from python_code import cal_ExpressionInteger

def test_cal_ExpressionInteger___init__():
    assert cal_ExpressionInteger.__init__(cal_ExpressionInteger(''), '') == None


from python_code import cal_ExpressionString

def test_cal_ExpressionString___init__():
    assert cal_ExpressionString.__init__(cal_ExpressionString(''), '') == None


from python_code import cal_AstExpression
from python_code import cal_ExpressionUnary

def test_cal_ExpressionUnary___init__():
    assert cal_ExpressionUnary.__init__(cal_ExpressionUnary('', cal_ExpressionUnary=cal_AstExpression()), '', cal_ExpressionUnary=cal_AstExpression()) == None


from python_code import cal_AstActor
from python_code import cal_AstExpression
from python_code import cal_AstType
from python_code import cal_AstUnit
from python_code import cal_ExpressionCall
from python_code import cal_Function

def test_cal_Function___init__():
    assert cal_Function.__init__(cal_Function('', cal_Function=cal_AstUnit(), cal_Function72=cal_AstExpression(), cal_Function33=cal_AstActor(), cal_Function60=set(), cal_Function63=set(), cal_Function66=cal_AstType(), cal_Function69=set(), cal_Function217=cal_ExpressionCall()), '', cal_Function=cal_AstUnit(), cal_Function72=cal_AstExpression(), cal_Function33=cal_AstActor(), cal_Function60=set(), cal_Function63=set(), cal_Function66=cal_AstType(), cal_Function69=set(), cal_Function217=cal_ExpressionCall()) == None


from python_code import cal_AstActor
from python_code import cal_ExternalTarget
from python_code import cal_Fsm
from python_code import cal_LocalFsm

def test_cal_LocalFsm___init__():
    assert cal_LocalFsm.__init__(cal_LocalFsm('', cal_LocalFsm=cal_AstActor(), cal_LocalFsm111=cal_ExternalTarget(), cal_LocalFsm125=cal_Fsm()), '', cal_LocalFsm=cal_AstActor(), cal_LocalFsm111=cal_ExternalTarget(), cal_LocalFsm125=cal_Fsm()) == None


from python_code import cal_RegExp
from python_code import cal_RegExpBinary

def test_cal_RegExpBinary___init__():
    assert cal_RegExpBinary.__init__(cal_RegExpBinary('', cal_RegExpBinary=cal_RegExp(), cal_RegExpBinary274=cal_RegExp()), '', cal_RegExpBinary=cal_RegExp(), cal_RegExpBinary274=cal_RegExp()) == None


from python_code import cal_RegExp
from python_code import cal_RegExpUnary

def test_cal_RegExpUnary___init__():
    assert cal_RegExpUnary.__init__(cal_RegExpUnary('', cal_RegExpUnary=cal_RegExp()), '', cal_RegExpUnary=cal_RegExp()) == None

