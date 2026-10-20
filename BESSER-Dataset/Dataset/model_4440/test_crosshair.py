from python_code import roverDSL_BBLiteral

def test_roverDSL_BBLiteral___init__():
    assert roverDSL_BBLiteral.__init__(roverDSL_BBLiteral(True), False) == None


from python_code import roverDSL_BSensorLiteral

def test_roverDSL_BSensorLiteral___init__():
    assert roverDSL_BSensorLiteral.__init__(roverDSL_BSensorLiteral(''), '') == None


from python_code import roverDSL_BVLiteral

def test_roverDSL_BVLiteral___init__():
    assert roverDSL_BVLiteral.__init__(roverDSL_BVLiteral(False, 0), False, 0) == None


from python_code import roverDSL_BVarLiteral

def test_roverDSL_BVarLiteral___init__():
    assert roverDSL_BVarLiteral.__init__(roverDSL_BVarLiteral(''), '') == None


from python_code import roverDSL_BehaviorName
from python_code import roverDSL_Implementation
from python_code import roverDSL_Robot

def test_roverDSL_BehaviorName___init__():
    assert roverDSL_BehaviorName.__init__(roverDSL_BehaviorName('', roverDSL_BehaviorName16=roverDSL_Implementation(), roverDSL_BehaviorName=roverDSL_Robot()), '', roverDSL_BehaviorName16=roverDSL_Implementation(), roverDSL_BehaviorName=roverDSL_Robot()) == None


from python_code import roverDSL_ColorLiteral

def test_roverDSL_ColorLiteral___init__():
    assert roverDSL_ColorLiteral.__init__(roverDSL_ColorLiteral(''), '') == None


from python_code import roverDSL_ExpressionBinComp
from python_code import roverDSL_ValueExpression

def test_roverDSL_ExpressionBinComp___init__():
    assert roverDSL_ExpressionBinComp.__init__(roverDSL_ExpressionBinComp('', roverDSL_ExpressionBinComp=roverDSL_ValueExpression(), roverDSL_ExpressionBinComp79=roverDSL_ValueExpression()), '', roverDSL_ExpressionBinComp=roverDSL_ValueExpression(), roverDSL_ExpressionBinComp79=roverDSL_ValueExpression()) == None


from python_code import roverDSL_ExpressionBinOp
from python_code import roverDSL_ValueExpression

def test_roverDSL_ExpressionBinOp___init__():
    assert roverDSL_ExpressionBinOp.__init__(roverDSL_ExpressionBinOp('', roverDSL_ExpressionBinOp=roverDSL_ValueExpression(), roverDSL_ExpressionBinOp74=roverDSL_ValueExpression()), '', roverDSL_ExpressionBinOp=roverDSL_ValueExpression(), roverDSL_ExpressionBinOp74=roverDSL_ValueExpression()) == None


from python_code import roverDSL_AssignExpression
from python_code import roverDSL_Global
from python_code import roverDSL_Robot

def test_roverDSL_Global___init__():
    assert roverDSL_Global.__init__(roverDSL_Global('', roverDSL_Global=roverDSL_Robot(), roverDSL_Global41=roverDSL_AssignExpression()), '', roverDSL_Global=roverDSL_Robot(), roverDSL_Global41=roverDSL_AssignExpression()) == None


from python_code import roverDSL_ShowAction

def test_roverDSL_ShowAction___init__():
    assert roverDSL_ShowAction.__init__(roverDSL_ShowAction('', '\x00'), '\x00\x00', '') == None


from python_code import roverDSL_SoundAction

def test_roverDSL_SoundAction___init__():
    assert roverDSL_SoundAction.__init__(roverDSL_SoundAction(''), '') == None


from python_code import roverDSL_Robot
from python_code import roverDSL_Static
from python_code import roverDSL_ValueExpression

def test_roverDSL_Static___init__():
    assert roverDSL_Static.__init__(roverDSL_Static('', roverDSL_Static12=roverDSL_ValueExpression(), roverDSL_Static=roverDSL_Robot()), '', roverDSL_Static12=roverDSL_ValueExpression(), roverDSL_Static=roverDSL_Robot()) == None


from python_code import roverDSL_Robot
from python_code import roverDSL_SubRoutine
from python_code import roverDSL_SubRoutineAction

def test_roverDSL_SubRoutine___init__():
    assert roverDSL_SubRoutine.__init__(roverDSL_SubRoutine('', roverDSL_SubRoutine=roverDSL_Robot(), roverDSL_SubRoutine23=set(), roverDSL_SubRoutine64=roverDSL_SubRoutineAction()), '', roverDSL_SubRoutine=roverDSL_Robot(), roverDSL_SubRoutine23=set(), roverDSL_SubRoutine64=roverDSL_SubRoutineAction()) == None

