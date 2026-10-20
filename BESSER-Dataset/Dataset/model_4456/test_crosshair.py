from python_code import arduinoml_Actuator
from python_code import arduinoml_ActuatorState
from python_code import arduinoml_Transition

def test_arduinoml_ActuatorState___init__():
    assert arduinoml_ActuatorState.__init__(arduinoml_ActuatorState(True, arduinoml_ActuatorState=arduinoml_Actuator(), arduinoml_ActuatorState20=arduinoml_Transition()), False, arduinoml_ActuatorState=arduinoml_Actuator(), arduinoml_ActuatorState20=arduinoml_Transition()) == None


from python_code import arduinoml_Board
from python_code import arduinoml_Brick

def test_arduinoml_Brick___init__():
    assert arduinoml_Brick.__init__(arduinoml_Brick('', 0, arduinoml_Brick=arduinoml_Board()), '', 0, arduinoml_Brick=arduinoml_Board()) == None


from python_code import arduinoml_Off

def test_arduinoml_Off___init__():
    assert arduinoml_Off.__init__(arduinoml_Off()) == None

def test_arduinoml_Off_turnOff():
    assert arduinoml_Off.turnOff(arduinoml_Off()) == None


from python_code import arduinoml_On

def test_arduinoml_On___init__():
    assert arduinoml_On.__init__(arduinoml_On()) == None

def test_arduinoml_On_turnOn():
    assert arduinoml_On.turnOn(arduinoml_On()) == None


from python_code import arduinoml_Board
from python_code import arduinoml_State
from python_code import arduinoml_Transition

def test_arduinoml_State___init__():
    assert arduinoml_State.__init__(arduinoml_State('', arduinoml_State9=set(), arduinoml_State=arduinoml_Board(), arduinoml_State3=arduinoml_Board(), arduinoml_State7=set(), arduinoml_State13=arduinoml_Transition(), arduinoml_State16=arduinoml_Transition()), '', arduinoml_State9=set(), arduinoml_State=arduinoml_Board(), arduinoml_State3=arduinoml_Board(), arduinoml_State7=set(), arduinoml_State13=arduinoml_Transition(), arduinoml_State16=arduinoml_Transition()) == None

