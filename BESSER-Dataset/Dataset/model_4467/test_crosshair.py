from python_code import RobotProjectModel_Amount

def test_RobotProjectModel_Amount___init__():
    assert RobotProjectModel_Amount.__init__(RobotProjectModel_Amount(0), 0) == None


from python_code import RobotProjectModel_Angle
from python_code import RobotProjectModel_Turn

def test_RobotProjectModel_Angle___init__():
    assert RobotProjectModel_Angle.__init__(RobotProjectModel_Angle('', RobotProjectModel_Angle=RobotProjectModel_Turn()), '', RobotProjectModel_Angle=RobotProjectModel_Turn()) == None


from python_code import RobotProjectModel_DetectedObjectIs

def test_RobotProjectModel_DetectedObjectIs___init__():
    assert RobotProjectModel_DetectedObjectIs.__init__(RobotProjectModel_DetectedObjectIs(''), '') == None


from python_code import RobotProjectModel_Distance
from python_code import RobotProjectModel_MoveStraight

def test_RobotProjectModel_Distance___init__():
    assert RobotProjectModel_Distance.__init__(RobotProjectModel_Distance('', RobotProjectModel_Distance=RobotProjectModel_MoveStraight()), '', RobotProjectModel_Distance=RobotProjectModel_MoveStraight()) == None


from python_code import RobotProjectModel_Duration
from python_code import RobotProjectModel_TimedInstruction

def test_RobotProjectModel_Duration___init__():
    assert RobotProjectModel_Duration.__init__(RobotProjectModel_Duration('', RobotProjectModel_Duration=RobotProjectModel_TimedInstruction()), '', RobotProjectModel_Duration=RobotProjectModel_TimedInstruction()) == None


from python_code import RobotProjectModel_Call
from python_code import RobotProjectModel_Function
from python_code import RobotProjectModel_InstructionBlock

def test_RobotProjectModel_Function___init__():
    assert RobotProjectModel_Function.__init__(RobotProjectModel_Function('', RobotProjectModel_Function=RobotProjectModel_InstructionBlock(), RobotProjectModel_Function6=RobotProjectModel_Call()), '', RobotProjectModel_Function=RobotProjectModel_InstructionBlock(), RobotProjectModel_Function6=RobotProjectModel_Call()) == None


from python_code import RobotProjectModel_Print

def test_RobotProjectModel_Print___init__():
    assert RobotProjectModel_Print.__init__(RobotProjectModel_Print(''), '') == None

