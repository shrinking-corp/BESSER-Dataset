from python_code import Airplane

def test_Airplane___init__():
    assert Airplane.__init__(Airplane(0, 0), 0, 0) == None


from python_code import Boat

def test_Boat___init__():
    assert Boat.__init__(Boat(0), 0) == None


from python_code import Car

def test_Car___init__():
    assert Car.__init__(Car('', '', '', 0, 0, 0, 0), '', '\x00', '', 0, 0, 0, 0) == None


from python_code import Car1

def test_Car1___init__():
    assert Car1.__init__(Car1(0, '\x00'), 0, '\x00') == None


from python_code import Train

def test_Train___init__():
    assert Train.__init__(Train(0, '\x00'), 0, '\x00') == None


from python_code import Vehicle

def test_Vehicle___init__():
    assert Vehicle.__init__(Vehicle('', '', '\x00\x00'), '', '', '') == None

