from python_code import arduinoml_Board
from python_code import arduinoml_Brick

def test_arduinoml_Brick___init__():
    assert arduinoml_Brick.__init__(arduinoml_Brick(0, arduinoml_Brick=arduinoml_Board()), 0, arduinoml_Brick=arduinoml_Board()) == None


from python_code import arduinoml_NamedElement

def test_arduinoml_NamedElement___init__():
    assert arduinoml_NamedElement.__init__(arduinoml_NamedElement(''), '') == None


from python_code import arduinoml_Transition
from python_code import arduinoml_Trigger

def test_arduinoml_Trigger___init__():
    assert arduinoml_Trigger.__init__(arduinoml_Trigger('', arduinoml_Trigger=arduinoml_Transition(), arduinoml_Trigger17=set()), '', arduinoml_Trigger=arduinoml_Transition(), arduinoml_Trigger17=set()) == None


from python_code import arduinoml_Wait

def test_arduinoml_Wait___init__():
    assert arduinoml_Wait.__init__(arduinoml_Wait(0), 0) == None

