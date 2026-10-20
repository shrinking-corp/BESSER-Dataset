from python_code import Alarm_Signaler

def test_Alarm_Signaler___init__():
    assert Alarm_Signaler.__init__(Alarm_Signaler(0), 0) == None


from python_code import Camera

def test_Camera___init__():
    assert Camera.__init__(Camera(0, 0), 0, 0) == None


from python_code import Device_Configuration

def test_Device_Configuration___init__():
    assert Device_Configuration.__init__(Device_Configuration(0, False, False, False), 0, False, False, True) == None


from python_code import FloorCoordinates

def test_FloorCoordinates___init__():
    assert FloorCoordinates.__init__(FloorCoordinates(0, 0), 0, 0) == None


from python_code import HeatAirConditioning

def test_HeatAirConditioning___init__():
    assert HeatAirConditioning.__init__(HeatAirConditioning(0), 0) == None


from python_code import Home_Theatre

def test_Home_Theatre___init__():
    assert Home_Theatre.__init__(Home_Theatre(''), '') == None


from python_code import Lights

def test_Lights___init__():
    assert Lights.__init__(Lights(0), 0) == None


from python_code import SAFE_HOME_SYSTEM

def test_SAFE_HOME_SYSTEM___init__():
    assert SAFE_HOME_SYSTEM.__init__(SAFE_HOME_SYSTEM('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Sensor

def test_Sensor___init__():
    assert Sensor.__init__(Sensor(True), False) == None


from python_code import Telephone_Answering_machine

def test_Telephone_Answering_machine___init__():
    assert Telephone_Answering_machine.__init__(Telephone_Answering_machine(0), 0) == None


from python_code import Television

def test_Television___init__():
    assert Television.__init__(Television(''), '') == None

