from python_code import iot_Arduino
from python_code import iot_Board

def test_iot_Arduino___init__():
    assert iot_Arduino.__init__(iot_Arduino('\x00\x00', 0, iot_Arduino4=set(), iot_Arduino=iot_Board()), '', 0, iot_Arduino4=set(), iot_Arduino=iot_Board()) == None

def test_iot_Arduino_setup():
    assert iot_Arduino.setup(iot_Arduino('', 0, iot_Arduino4=set(), iot_Arduino=iot_Board())) == None

def test_iot_Arduino_loop():
    assert iot_Arduino.loop(iot_Arduino('', 0, iot_Arduino4=set(), iot_Arduino=iot_Board())) == None

