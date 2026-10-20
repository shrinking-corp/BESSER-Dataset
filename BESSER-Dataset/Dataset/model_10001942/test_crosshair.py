from python_code import Count_Sensor

def test_Count_Sensor___init__():
    assert Count_Sensor.__init__(Count_Sensor(0), 0) == None


from python_code import Gas_Smoke_Sensor

def test_Gas_Smoke_Sensor___init__():
    assert Gas_Smoke_Sensor.__init__(Gas_Smoke_Sensor(False, False), False, False) == None


from python_code import Firebase
from python_code import MobileApp

def test_MobileApp___init__():
    assert MobileApp.__init__(MobileApp(0, 0, Home_Security_System_System_02=Firebase(), Alarm_Mobile_App_129=set()), 0, 0, Home_Security_System_System_02=Firebase(), Alarm_Mobile_App_129=set()) == None


from python_code import Arduino
from python_code import Sensor

def test_Sensor___init__():
    assert Sensor.__init__(Sensor(0, 0, system0=Arduino()), 0, 0, system0=Arduino()) == None


from python_code import Firebase
from python_code import WebPage

def test_WebPage___init__():
    assert WebPage.__init__(WebPage(0.0, '', 0, '', 0.0, Firebase_Web_17=Firebase()), 0.0, '', 0, '\x00', 0.0, Firebase_Web_17=Firebase()) == None

