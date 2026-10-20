from python_code import arduinoml_AnalogAction

def test_arduinoml_AnalogAction___init__():
    assert arduinoml_AnalogAction.__init__(arduinoml_AnalogAction(0), 0) == None


from python_code import arduinoml_BinaryAction

def test_arduinoml_BinaryAction___init__():
    assert arduinoml_BinaryAction.__init__(arduinoml_BinaryAction(''), '') == None


from python_code import arduinoml_App
from python_code import arduinoml_Brick

def test_arduinoml_Brick___init__():
    assert arduinoml_Brick.__init__(arduinoml_Brick('', arduinoml_Brick=arduinoml_App()), '', arduinoml_Brick=arduinoml_App()) == None


from python_code import arduinoml_MultipleElementCondition
from python_code import arduinoml_Transition

def test_arduinoml_MultipleElementCondition___init__():
    assert arduinoml_MultipleElementCondition.__init__(arduinoml_MultipleElementCondition('', arduinoml_MultipleElementCondition=arduinoml_Transition(), arduinoml_MultipleElementCondition19=set()), '', arduinoml_MultipleElementCondition=arduinoml_Transition(), arduinoml_MultipleElementCondition19=set()) == None


from python_code import arduinoml_NamedElement

def test_arduinoml_NamedElement___init__():
    assert arduinoml_NamedElement.__init__(arduinoml_NamedElement(''), '') == None


from python_code import arduinoml_BinarySensor
from python_code import arduinoml_SingleElementCondition

def test_arduinoml_SingleElementCondition___init__():
    assert arduinoml_SingleElementCondition.__init__(arduinoml_SingleElementCondition('', arduinoml_SingleElementCondition=arduinoml_BinarySensor()), '', arduinoml_SingleElementCondition=arduinoml_BinarySensor()) == None


from python_code import arduinoml_AnalogSensor
from python_code import arduinoml_ValueElementCondition

def test_arduinoml_ValueElementCondition___init__():
    assert arduinoml_ValueElementCondition.__init__(arduinoml_ValueElementCondition(0.0, '\x00\x00', arduinoml_ValueElementCondition=arduinoml_AnalogSensor()), 0.0, '', arduinoml_ValueElementCondition=arduinoml_AnalogSensor()) == None

