from python_code import StateMachine_NamedState

def test_StateMachine_NamedState___init__():
    assert StateMachine_NamedState.__init__(StateMachine_NamedState(''), '') == None


from python_code import StateMachine_State
from python_code import StateMachine_Transition
from python_code import StateMachine_WashingMachine

def test_StateMachine_Transition___init__():
    assert StateMachine_Transition.__init__(StateMachine_Transition('\x00\x00', '', 0, '', StateMachine_Transition2=StateMachine_State(), StateMachine_Transition5=StateMachine_State(), StateMachine_Transition=StateMachine_State(), StateMachine_Transition11=StateMachine_WashingMachine()), '', '', 0, '', StateMachine_Transition2=StateMachine_State(), StateMachine_Transition5=StateMachine_State(), StateMachine_Transition=StateMachine_State(), StateMachine_Transition11=StateMachine_WashingMachine()) == None


from python_code import StateMachine_UnNamedState

def test_StateMachine_UnNamedState___init__():
    assert StateMachine_UnNamedState.__init__(StateMachine_UnNamedState(''), '') == None

