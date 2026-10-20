from python_code import robotG_robot_Bip

def test_robotG_robot_Bip___init__():
    assert robotG_robot_Bip.__init__(robotG_robot_Bip(0, 0, False), 0, 0, False) == None


from python_code import robotG_robot_Display

def test_robotG_robot_Display___init__():
    assert robotG_robot_Display.__init__(robotG_robot_Display('\x00\x00', 0, 0, 0), '', 0, 0, 0) == None


from python_code import robotG_robot_HasTurned

def test_robotG_robot_HasTurned___init__():
    assert robotG_robot_HasTurned.__init__(robotG_robot_HasTurned(0), 0) == None


from python_code import robotG_robot_Move

def test_robotG_robot_Move___init__():
    assert robotG_robot_Move.__init__(robotG_robot_Move(0), 0) == None


from python_code import robotG_robot_Obstacle

def test_robotG_robot_Obstacle___init__():
    assert robotG_robot_Obstacle.__init__(robotG_robot_Obstacle(0), 0) == None


from python_code import robotG_robot_SetTurnAngle

def test_robotG_robot_SetTurnAngle___init__():
    assert robotG_robot_SetTurnAngle.__init__(robotG_robot_SetTurnAngle(0), 0) == None


from python_code import robotG_robot_Turn

def test_robotG_robot_Turn___init__():
    assert robotG_robot_Turn.__init__(robotG_robot_Turn(0, 0), 0, 0) == None

