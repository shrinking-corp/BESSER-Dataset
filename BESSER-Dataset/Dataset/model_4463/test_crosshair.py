from python_code import arduinoML_App
from python_code import arduinoML_State

def test_arduinoML_App___init__():
    assert arduinoML_App.__init__(arduinoML_App('', arduinoML_App=set(), arduinoML_App2=set(), arduinoML_App4=arduinoML_State()), '', arduinoML_App=set(), arduinoML_App2=set(), arduinoML_App4=arduinoML_State()) == None


from python_code import arduinoML_Condition
from python_code import arduinoML_Sensor
from python_code import arduinoML_Signal
from python_code import arduinoML_Transition

def test_arduinoML_Condition___init__():
    assert arduinoML_Condition.__init__(arduinoML_Condition('', arduinoML_Condition=arduinoML_Transition(), arduinoML_Condition20=arduinoML_Sensor(), arduinoML_Condition22=arduinoML_Signal()), '', arduinoML_Condition=arduinoML_Transition(), arduinoML_Condition20=arduinoML_Sensor(), arduinoML_Condition22=arduinoML_Signal()) == None


from python_code import arduinoML_DigitalSignal

def test_arduinoML_DigitalSignal___init__():
    assert arduinoML_DigitalSignal.__init__(arduinoML_DigitalSignal(''), '') == None


from python_code import arduinoML_NamedElement

def test_arduinoML_NamedElement___init__():
    assert arduinoML_NamedElement.__init__(arduinoML_NamedElement(''), '') == None


from python_code import arduinoML_StringSignal

def test_arduinoML_StringSignal___init__():
    assert arduinoML_StringSignal.__init__(arduinoML_StringSignal(''), '') == None

