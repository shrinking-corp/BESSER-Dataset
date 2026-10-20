from python_code import arduinoML_Action
from python_code import arduinoML_Actuator
from python_code import arduinoML_State

def test_arduinoML_Action___init__():
    assert arduinoML_Action.__init__(arduinoML_Action('', arduinoML_Action=arduinoML_State(), arduinoML_Action10=arduinoML_Actuator()), '', arduinoML_Action=arduinoML_State(), arduinoML_Action10=arduinoML_Actuator()) == None


from python_code import arduinoML_App
from python_code import arduinoML_Brick

def test_arduinoML_Brick___init__():
    assert arduinoML_Brick.__init__(arduinoML_Brick(0, arduinoML_Brick=arduinoML_App()), 0, arduinoML_Brick=arduinoML_App()) == None


from python_code import arduinoML_NamedElement

def test_arduinoML_NamedElement___init__():
    assert arduinoML_NamedElement.__init__(arduinoML_NamedElement(''), '') == None


from python_code import arduinoML_Sensor
from python_code import arduinoML_State
from python_code import arduinoML_Transition

def test_arduinoML_Transition___init__():
    assert arduinoML_Transition.__init__(arduinoML_Transition('', Transition=arduinoML_State(), arduinoML_Transition=arduinoML_State(), arduinoML_Transition14=arduinoML_Sensor(), transition=arduinoML_State()), '', Transition=arduinoML_State(), arduinoML_Transition=arduinoML_State(), arduinoML_Transition14=arduinoML_Sensor(), transition=arduinoML_State()) == None

