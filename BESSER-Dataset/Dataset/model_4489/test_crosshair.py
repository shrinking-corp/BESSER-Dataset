from python_code import dSL_Behavior
from python_code import dSL_Expression
from python_code import dSL_MarsRoverExpedition

def test_dSL_Behavior___init__():
    assert dSL_Behavior.__init__(dSL_Behavior('', dSL_Behavior=dSL_MarsRoverExpedition(), dSL_Behavior10=dSL_Expression(), dSL_Behavior12=set()), '', dSL_Behavior=dSL_MarsRoverExpedition(), dSL_Behavior10=dSL_Expression(), dSL_Behavior12=set()) == None


from python_code import dSL_ColorLiteral

def test_dSL_ColorLiteral___init__():
    assert dSL_ColorLiteral.__init__(dSL_ColorLiteral(''), '') == None


from python_code import dSL_DepthLiteral

def test_dSL_DepthLiteral___init__():
    assert dSL_DepthLiteral.__init__(dSL_DepthLiteral(''), '') == None


from python_code import dSL_DistanceLiteral

def test_dSL_DistanceLiteral___init__():
    assert dSL_DistanceLiteral.__init__(dSL_DistanceLiteral(0), 0) == None


from python_code import dSL_EdgeLiteral

def test_dSL_EdgeLiteral___init__():
    assert dSL_EdgeLiteral.__init__(dSL_EdgeLiteral(''), '') == None


from python_code import dSL_EndAfter

def test_dSL_EndAfter___init__():
    assert dSL_EndAfter.__init__(dSL_EndAfter(0), 0) == None


from python_code import dSL_EndCondition
from python_code import dSL_EndWhen

def test_dSL_EndWhen___init__():
    assert dSL_EndWhen.__init__(dSL_EndWhen('', 0, dSL_EndWhen=dSL_EndCondition()), '', 0, dSL_EndWhen=dSL_EndCondition()) == None


from python_code import dSL_LeftRotatePoint

def test_dSL_LeftRotatePoint___init__():
    assert dSL_LeftRotatePoint.__init__(dSL_LeftRotatePoint(''), '') == None


from python_code import dSL_MeasurementAction

def test_dSL_MeasurementAction___init__():
    assert dSL_MeasurementAction.__init__(dSL_MeasurementAction(''), '') == None


from python_code import dSL_MiddleRotatePoint

def test_dSL_MiddleRotatePoint___init__():
    assert dSL_MiddleRotatePoint.__init__(dSL_MiddleRotatePoint(''), '') == None


from python_code import dSL_EndCondition
from python_code import dSL_MarsRoverExpedition
from python_code import dSL_Mission

def test_dSL_Mission___init__():
    assert dSL_Mission.__init__(dSL_Mission('\x00', dSL_Mission4=set(), dSL_Mission6=dSL_EndCondition(), dSL_Mission=dSL_MarsRoverExpedition()), '', dSL_Mission4=set(), dSL_Mission6=dSL_EndCondition(), dSL_Mission=dSL_MarsRoverExpedition()) == None


from python_code import dSL_MoveAction

def test_dSL_MoveAction___init__():
    assert dSL_MoveAction.__init__(dSL_MoveAction(''), '') == None


from python_code import dSL_LeftMovementAction
from python_code import dSL_MovementAction
from python_code import dSL_RightMovementAction

def test_dSL_MovementAction___init__():
    assert dSL_MovementAction.__init__(dSL_MovementAction('', dSL_MovementAction15=dSL_RightMovementAction(), dSL_MovementAction=dSL_LeftMovementAction()), '', dSL_MovementAction15=dSL_RightMovementAction(), dSL_MovementAction=dSL_LeftMovementAction()) == None


from python_code import dSL_RightRotatePoint

def test_dSL_RightRotatePoint___init__():
    assert dSL_RightRotatePoint.__init__(dSL_RightRotatePoint(''), '') == None


from python_code import dSL_RotatePoints

def test_dSL_RotatePoints___init__():
    assert dSL_RotatePoints.__init__(dSL_RotatePoints(0), 0) == None


from python_code import dSL_TouchLiteral

def test_dSL_TouchLiteral___init__():
    assert dSL_TouchLiteral.__init__(dSL_TouchLiteral(''), '') == None


from python_code import dSL_TrueLiteral

def test_dSL_TrueLiteral___init__():
    assert dSL_TrueLiteral.__init__(dSL_TrueLiteral(''), '') == None

