from python_code import Camera_sensor
from python_code import Home_Security

def test_Camera_sensor___init__():
    assert Camera_sensor.__init__(Camera_sensor(0, 0, home_Security3=Home_Security()), 0, 0, home_Security3=Home_Security()) == None

from python_code import Event_Log
from python_code import Home_Security

def test_Event_Log___init__():
    assert Event_Log.__init__(Event_Log('', home_Security5=Home_Security()), '', home_Security5=Home_Security()) == None

from python_code import Home_Security
from python_code import Light_Sensor

def test_Light_Sensor___init__():
    assert Light_Sensor.__init__(Light_Sensor('', home_Security7=Home_Security()), '', home_Security7=Home_Security()) == None

from python_code import Home_Security
from python_code import Lock_doors_sensors

def test_Lock_doors_sensors___init__():
    assert Lock_doors_sensors.__init__(Lock_doors_sensors('', home_Security9=Home_Security()), '', home_Security9=Home_Security()) == None

from python_code import Home_Security
from python_code import Server

def test_Server___init__():
    assert Server.__init__(Server('', home_Security1=Home_Security()), '', home_Security1=Home_Security()) == None

from python_code import Home_Security
from python_code import Temperature_sensor

def test_Temperature_sensor___init__():
    assert Temperature_sensor.__init__(Temperature_sensor('', home_Security11=Home_Security()), '', home_Security11=Home_Security()) == None
