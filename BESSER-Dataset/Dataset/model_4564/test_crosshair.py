from python_code import robot_robot_Bip

def test_robot_robot_Bip___init__():
    assert robot_robot_Bip.__init__(robot_robot_Bip('', '', '\x00\x00'), '', '', '') == None


from python_code import robot_robot_HasTurnedCmd

def test_robot_robot_HasTurnedCmd___init__():
    assert robot_robot_HasTurnedCmd.__init__(robot_robot_HasTurnedCmd(''), '') == None


from python_code import robot_robot_MoveCmd

def test_robot_robot_MoveCmd___init__():
    assert robot_robot_MoveCmd.__init__(robot_robot_MoveCmd(''), '') == None


from python_code import robot_robot_ObstacleCmd

def test_robot_robot_ObstacleCmd___init__():
    assert robot_robot_ObstacleCmd.__init__(robot_robot_ObstacleCmd(''), '') == None


from python_code import robot_robot_PrintCmd

def test_robot_robot_PrintCmd___init__():
    assert robot_robot_PrintCmd.__init__(robot_robot_PrintCmd('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import robot_robot_SetTurnAngleCmd

def test_robot_robot_SetTurnAngleCmd___init__():
    assert robot_robot_SetTurnAngleCmd.__init__(robot_robot_SetTurnAngleCmd(''), '') == None


from python_code import robot_robot_TurnCmd

def test_robot_robot_TurnCmd___init__():
    assert robot_robot_TurnCmd.__init__(robot_robot_TurnCmd('', '\x00'), '\x00\x00', '') == None

