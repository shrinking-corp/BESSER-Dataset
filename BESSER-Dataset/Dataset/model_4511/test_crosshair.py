from python_code import arduinoml_AMLMachine
from python_code import arduinoml_AMLState

def test_arduinoml_AMLMachine___init__():
    assert arduinoml_AMLMachine.__init__(arduinoml_AMLMachine(0, arduinoml_AMLMachine=set(), arduinoml_AMLMachine2=set(), arduinoml_AMLMachine4=arduinoml_AMLState()), 0, arduinoml_AMLMachine=set(), arduinoml_AMLMachine2=set(), arduinoml_AMLMachine4=arduinoml_AMLState()) == None


from python_code import arduinoml_AnalogActionValue

def test_arduinoml_AnalogActionValue___init__():
    assert arduinoml_AnalogActionValue.__init__(arduinoml_AnalogActionValue(0), 0) == None


from python_code import arduinoml_AnalogCondition
from python_code import arduinoml_AnalogSensor

def test_arduinoml_AnalogCondition___init__():
    assert arduinoml_AnalogCondition.__init__(arduinoml_AnalogCondition('', 0, arduinoml_AnalogCondition=arduinoml_AnalogSensor()), '', 0, arduinoml_AnalogCondition=arduinoml_AnalogSensor()) == None


from python_code import arduinoml_DigitalAction
from python_code import arduinoml_DigitalActuator

def test_arduinoml_DigitalAction___init__():
    assert arduinoml_DigitalAction.__init__(arduinoml_DigitalAction('', arduinoml_DigitalAction=arduinoml_DigitalActuator()), '', arduinoml_DigitalAction=arduinoml_DigitalActuator()) == None


from python_code import arduinoml_DigitalCondition
from python_code import arduinoml_DigitalSensor

def test_arduinoml_DigitalCondition___init__():
    assert arduinoml_DigitalCondition.__init__(arduinoml_DigitalCondition('', arduinoml_DigitalCondition=arduinoml_DigitalSensor()), '', arduinoml_DigitalCondition=arduinoml_DigitalSensor()) == None


from python_code import arduinoml_NamedElement

def test_arduinoml_NamedElement___init__():
    assert arduinoml_NamedElement.__init__(arduinoml_NamedElement(''), '') == None


from python_code import arduinoml_TimeCondition

def test_arduinoml_TimeCondition___init__():
    assert arduinoml_TimeCondition.__init__(arduinoml_TimeCondition(0, '\x00'), 0, '\x00') == None

