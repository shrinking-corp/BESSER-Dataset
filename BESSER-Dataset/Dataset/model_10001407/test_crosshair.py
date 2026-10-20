from python_code import Control_Box

def test_Control_Box___init__():
    assert Control_Box.__init__(Control_Box(False, 0.0), False, 0.0) == None


from python_code import FAN

def test_FAN___init__():
    assert FAN.__init__(FAN(''), '') == None


from python_code import Fan_Regulator_Box

def test_Fan_Regulator_Box___init__():
    assert Fan_Regulator_Box.__init__(Fan_Regulator_Box(''), '') == None


from python_code import FireAlarm_Sensor

def test_FireAlarm_Sensor___init__():
    assert FireAlarm_Sensor.__init__(FireAlarm_Sensor(False, False), False, False) == None


from python_code import Light

def test_Light___init__():
    assert Light.__init__(Light(''), '') == None


from python_code import Sensor

def test_Sensor___init__():
    assert Sensor.__init__(Sensor(0, 0), 0, 0) == None

