from python_code import RobotWork_Chrography

def test_RobotWork_Chrography___init__():
    assert RobotWork_Chrography.__init__(RobotWork_Chrography('', RobotWork_Chrography=set()), '', RobotWork_Chrography=set()) == None


from python_code import RobotWork_GoForward

def test_RobotWork_GoForward___init__():
    assert RobotWork_GoForward.__init__(RobotWork_GoForward(0), 0) == None


from python_code import RobotWork_Rotate

def test_RobotWork_Rotate___init__():
    assert RobotWork_Rotate.__init__(RobotWork_Rotate(0, False), 0, False) == None

