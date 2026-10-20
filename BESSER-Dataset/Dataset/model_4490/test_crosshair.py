from python_code import dSL_Behaviors
from python_code import dSL_Expression
from python_code import dSL_RobotBehavior

def test_dSL_Behaviors___init__():
    assert dSL_Behaviors.__init__(dSL_Behaviors('', dSL_Behaviors=dSL_RobotBehavior(), dSL_Behaviors2=dSL_Expression(), dSL_Behaviors4=set()), '', dSL_Behaviors=dSL_RobotBehavior(), dSL_Behaviors2=dSL_Expression(), dSL_Behaviors4=set()) == None


from python_code import dSL_ColorLiteral

def test_dSL_ColorLiteral___init__():
    assert dSL_ColorLiteral.__init__(dSL_ColorLiteral(''), '') == None


from python_code import dSL_DistanceLiteral

def test_dSL_DistanceLiteral___init__():
    assert dSL_DistanceLiteral.__init__(dSL_DistanceLiteral(0), 0) == None


from python_code import dSL_EdgeLiteral

def test_dSL_EdgeLiteral___init__():
    assert dSL_EdgeLiteral.__init__(dSL_EdgeLiteral(''), '') == None


from python_code import dSL_LeftRotatePoint

def test_dSL_LeftRotatePoint___init__():
    assert dSL_LeftRotatePoint.__init__(dSL_LeftRotatePoint(''), '') == None


from python_code import dSL_MiddleRotatePoint

def test_dSL_MiddleRotatePoint___init__():
    assert dSL_MiddleRotatePoint.__init__(dSL_MiddleRotatePoint(''), '') == None


from python_code import dSL_LeftMovementAction
from python_code import dSL_MovementAction
from python_code import dSL_RightMovementAction

def test_dSL_MovementAction___init__():
    assert dSL_MovementAction.__init__(dSL_MovementAction('', dSL_MovementAction=dSL_LeftMovementAction(), dSL_MovementAction7=dSL_RightMovementAction()), '', dSL_MovementAction=dSL_LeftMovementAction(), dSL_MovementAction7=dSL_RightMovementAction()) == None


from python_code import dSL_RightRotatePoint

def test_dSL_RightRotatePoint___init__():
    assert dSL_RightRotatePoint.__init__(dSL_RightRotatePoint(''), '') == None


from python_code import dSL_RotatePoints

def test_dSL_RotatePoints___init__():
    assert dSL_RotatePoints.__init__(dSL_RotatePoints(0), 0) == None


from python_code import dSL_TouchLiteral

def test_dSL_TouchLiteral___init__():
    assert dSL_TouchLiteral.__init__(dSL_TouchLiteral(''), '') == None

