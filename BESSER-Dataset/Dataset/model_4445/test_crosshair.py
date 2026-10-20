from python_code import arduinoML_Action
from python_code import arduinoML_Actuator
from python_code import arduinoML_State

def test_arduinoML_Action___init__():
    assert arduinoML_Action.__init__(arduinoML_Action('', arduinoML_Action=arduinoML_State(), arduinoML_Action9=arduinoML_Actuator()), '', arduinoML_Action=arduinoML_State(), arduinoML_Action9=arduinoML_Actuator()) == None


from python_code import arduinoML_App
from python_code import arduinoML_Mode

def test_arduinoML_App___init__():
    assert arduinoML_App.__init__(arduinoML_App(False, arduinoML_App=arduinoML_Mode(), arduinoML_App2=set(), arduinoML_App5=set()), False, arduinoML_App=arduinoML_Mode(), arduinoML_App2=set(), arduinoML_App5=set()) == None


from python_code import arduinoML_NamedElement

def test_arduinoML_NamedElement___init__():
    assert arduinoML_NamedElement.__init__(arduinoML_NamedElement(''), '') == None


from python_code import arduinoML_Transition

def test_arduinoML_Transition___init__():
    assert arduinoML_Transition.__init__(arduinoML_Transition('', 0, '', 0, '\x00', arduinoML_Transition=set(), arduinoML_Transition12=set()), '', 0, '', 0, '', arduinoML_Transition=set(), arduinoML_Transition12=set()) == None

