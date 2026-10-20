from python_code import FireAlarm_Sensor

def test_FireAlarm_Sensor___init__():
    assert FireAlarm_Sensor.__init__(FireAlarm_Sensor(True), False) == None


from python_code import Light

def test_Light___init__():
    assert Light.__init__(Light(''), '') == None

