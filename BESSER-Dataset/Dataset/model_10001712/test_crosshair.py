from python_code import CargoTrain

def test_CargoTrain___init__():
    assert CargoTrain.__init__(CargoTrain('', '', '\x00\x00'), '', '', '') == None


from python_code import Coach

def test_Coach___init__():
    assert Coach.__init__(Coach(0, 0), 0, 0) == None


from python_code import FirstClass

def test_FirstClass___init__():
    assert FirstClass.__init__(FirstClass(0, 0), 0, 0) == None


from python_code import PassengerTrain

def test_PassengerTrain___init__():
    assert PassengerTrain.__init__(PassengerTrain('', '', 0), '\x00', '', 0) == None


from python_code import Train

def test_Train___init__():
    assert Train.__init__(Train('\x00\x00', '', '', ''), '', '', '', '') == None

