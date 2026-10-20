from python_code import arduinoML_Action
from python_code import arduinoML_Actuator
from python_code import arduinoML_State

def test_arduinoML_Action___init__():
    assert arduinoML_Action.__init__(arduinoML_Action('', 0, arduinoML_Action=arduinoML_State(), arduinoML_Action12=arduinoML_Actuator()), '', 0, arduinoML_Action=arduinoML_State(), arduinoML_Action12=arduinoML_Actuator()) == None


from python_code import arduinoML_App
from python_code import arduinoML_Brick

def test_arduinoML_Brick___init__():
    assert arduinoML_Brick.__init__(arduinoML_Brick(0, '\x00', arduinoML_Brick=arduinoML_App()), 0, '\x00', arduinoML_Brick=arduinoML_App()) == None


from python_code import arduinoML_Condition
from python_code import arduinoML_Sensor

def test_arduinoML_Condition___init__():
    assert arduinoML_Condition.__init__(arduinoML_Condition('', 0, '\x00\x00', arduinoML_Condition=arduinoML_Sensor()), '', 0, '', arduinoML_Condition=arduinoML_Sensor()) == None


from python_code import arduinoML_NamedElement

def test_arduinoML_NamedElement___init__():
    assert arduinoML_NamedElement.__init__(arduinoML_NamedElement(''), '') == None


from python_code import arduinoML_BaseCondition
from python_code import arduinoML_SinkError
from python_code import arduinoML_State

def test_arduinoML_SinkError___init__():
    assert arduinoML_SinkError.__init__(arduinoML_SinkError(0, SinkError=arduinoML_State(), arduinoML_SinkError=arduinoML_BaseCondition(), arduinoML_SinkError24=set(), errors=arduinoML_State()), 0, SinkError=arduinoML_State(), arduinoML_SinkError=arduinoML_BaseCondition(), arduinoML_SinkError24=set(), errors=arduinoML_State()) == None

