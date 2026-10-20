from python_code import logo_Move

def test_logo_Move___init__():
    assert logo_Move.__init__(logo_Move(0.0), 0.0) == None


from python_code import logo_Turn

def test_logo_Turn___init__():
    assert logo_Turn.__init__(logo_Turn(0.0), 0.0) == None


from python_code import logo_WhileNoObstacle

def test_logo_WhileNoObstacle___init__():
    assert logo_WhileNoObstacle.__init__(logo_WhileNoObstacle(0.0, logo_WhileNoObstacle=set()), 0.0, logo_WhileNoObstacle=set()) == None

