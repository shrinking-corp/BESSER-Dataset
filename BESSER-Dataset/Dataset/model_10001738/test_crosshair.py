from python_code import Arduino
from python_code import Firebase

def test_Arduino___init__():
    assert Arduino.__init__(Arduino('', sensor1=set(), Arduino__Firebase_04=Firebase()), '', sensor1=set(), Arduino__Firebase_04=Firebase()) == None


from python_code import Count_Sensor

def test_Count_Sensor___init__():
    assert Count_Sensor.__init__(Count_Sensor(0), 0) == None


from python_code import Gas_Smoke_Sensor

def test_Gas_Smoke_Sensor___init__():
    assert Gas_Smoke_Sensor.__init__(Gas_Smoke_Sensor(False, False), False, False) == None


from python_code import Firebase
from python_code import Mobile_App

def test_Mobile_App___init__():
    assert Mobile_App.__init__(Mobile_App(0, 0, Home_Security_System_System_02=Firebase()), 0, 0, Home_Security_System_System_02=Firebase()) == None


from python_code import Firebase
from python_code import Web

def test_Web___init__():
    assert Web.__init__(Web(0, '', 0.0, 0.0, '', Firebase_Web_17=Firebase()), 0, '', 0.0, 0.0, '', Firebase_Web_17=Firebase()) == None

