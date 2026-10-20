from python_code import arduinoml_Action
from python_code import arduinoml_Actuator
from python_code import arduinoml_State

def test_arduinoml_Action___init__():
    assert arduinoml_Action.__init__(arduinoml_Action('', arduinoml_Action=arduinoml_State(), arduinoml_Action22=arduinoml_Actuator()), '', arduinoml_Action=arduinoml_State(), arduinoml_Action22=arduinoml_Actuator()) == None


from python_code import arduinoml_App
from python_code import arduinoml_Brick

def test_arduinoml_Brick___init__():
    assert arduinoml_Brick.__init__(arduinoml_Brick(0, '\x00', arduinoml_Brick=arduinoml_App()), 0, '\x00', arduinoml_Brick=arduinoml_App()) == None


from python_code import arduinoml_MultipleCondition

def test_arduinoml_MultipleCondition___init__():
    assert arduinoml_MultipleCondition.__init__(arduinoml_MultipleCondition('', arduinoml_MultipleCondition=set()), '', arduinoml_MultipleCondition=set()) == None


from python_code import arduinoml_NamedElement

def test_arduinoml_NamedElement___init__():
    assert arduinoml_NamedElement.__init__(arduinoml_NamedElement(''), '') == None

