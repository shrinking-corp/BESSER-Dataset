from python_code import iot_Actuator

def test_iot_Actuator___init__():
    assert iot_Actuator.__init__(iot_Actuator(True), False) == None

def test_iot_Actuator_toggle():
    assert iot_Actuator.toggle(iot_Actuator(False)) == None

def test_iot_Actuator_getStatus():
    assert iot_Actuator.getStatus(iot_Actuator(False)) == None

def test_iot_Actuator_switchOnOff():
    assert iot_Actuator.switchOnOff(iot_Actuator(False), 0) == None


from python_code import iot_CounterLoop

def test_iot_CounterLoop___init__():
    assert iot_CounterLoop.__init__(iot_CounterLoop(0), 0) == None


from python_code import iot_Hardware

def test_iot_Hardware___init__():
    assert iot_Hardware.__init__(iot_Hardware('\x00\x00', 0, False, 0), '', 0, False, 0) == None


from python_code import iot_Branching
from python_code import iot_IfPort

def test_iot_IfPort___init__():
    assert iot_IfPort.__init__(iot_IfPort(False, '', '\x00\x00', iot_IfPort=iot_Branching()), False, '', '', iot_IfPort=iot_Branching()) == None


from python_code import iot_ConditionPort
from python_code import iot_IterativeLoop

def test_iot_IterativeLoop___init__():
    assert iot_IterativeLoop.__init__(iot_IterativeLoop('', '\x00', iot_IterativeLoop=iot_ConditionPort()), '\x00\x00', '', iot_IterativeLoop=iot_ConditionPort()) == None


from python_code import iot_Sensor

def test_iot_Sensor___init__():
    assert iot_Sensor.__init__(iot_Sensor(''), '') == None

def test_iot_Sensor_getData():
    assert iot_Sensor.getData(iot_Sensor('')) == None


from python_code import iot_Snippet

def test_iot_Snippet___init__():
    assert iot_Snippet.__init__(iot_Snippet(''), '') == None

