from python_code import taskDSL_Avoid
from python_code import taskDSL_Detector

def test_taskDSL_Avoid___init__():
    assert taskDSL_Avoid.__init__(taskDSL_Avoid('\x00\x00', '', taskDSL_Avoid=taskDSL_Detector(), taskDSL_Avoid13=set()), '', '', taskDSL_Avoid=taskDSL_Detector(), taskDSL_Avoid13=set()) == None


from python_code import taskDSL_DriveUntil

def test_taskDSL_DriveUntil___init__():
    assert taskDSL_DriveUntil.__init__(taskDSL_DriveUntil('', '', '\x00\x00'), '', '', '') == None


from python_code import taskDSL_FollowLine

def test_taskDSL_FollowLine___init__():
    assert taskDSL_FollowLine.__init__(taskDSL_FollowLine(0), 0) == None


from python_code import taskDSL_Investigate

def test_taskDSL_Investigate___init__():
    assert taskDSL_Investigate.__init__(taskDSL_Investigate(''), '') == None


from python_code import taskDSL_DSL
from python_code import taskDSL_Mission

def test_taskDSL_Mission___init__():
    assert taskDSL_Mission.__init__(taskDSL_Mission('\x00', taskDSL_Mission4=set(), taskDSL_Mission=taskDSL_DSL()), '', taskDSL_Mission4=set(), taskDSL_Mission=taskDSL_DSL()) == None


from python_code import taskDSL_MoveBack

def test_taskDSL_MoveBack___init__():
    assert taskDSL_MoveBack.__init__(taskDSL_MoveBack(0), 0) == None


from python_code import taskDSL_Speak

def test_taskDSL_Speak___init__():
    assert taskDSL_Speak.__init__(taskDSL_Speak(''), '') == None


from python_code import taskDSL_TurnLeft

def test_taskDSL_TurnLeft___init__():
    assert taskDSL_TurnLeft.__init__(taskDSL_TurnLeft(0), 0) == None


from python_code import taskDSL_TurnRight

def test_taskDSL_TurnRight___init__():
    assert taskDSL_TurnRight.__init__(taskDSL_TurnRight(0), 0) == None

