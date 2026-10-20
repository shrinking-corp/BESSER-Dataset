from python_code import Camera_sensor
from python_code import Door_Security

def test_Camera_sensor___init__():
    assert Camera_sensor.__init__(Camera_sensor(0, 0, home_Security1=Door_Security()), 0, 0, home_Security1=Door_Security()) == None


from python_code import Door_Security
from python_code import Event_Log

def test_Event_Log___init__():
    assert Event_Log.__init__(Event_Log('', home_Security3=Door_Security()), '', home_Security3=Door_Security()) == None


from python_code import Door_Security
from python_code import Light_PIR_Sensor

def test_Light_PIR_Sensor___init__():
    assert Light_PIR_Sensor.__init__(Light_PIR_Sensor('', home_Security5=Door_Security()), '', home_Security5=Door_Security()) == None


from python_code import Door_Security
from python_code import Lock_doors_sensors

def test_Lock_doors_sensors___init__():
    assert Lock_doors_sensors.__init__(Lock_doors_sensors('', home_Security7=Door_Security()), '', home_Security7=Door_Security()) == None

