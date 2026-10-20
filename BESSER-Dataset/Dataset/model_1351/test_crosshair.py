from python_code import statemachine_AbstractState
from python_code import statemachine_StateMachine
from python_code import statemachine_Transition

def test_statemachine_AbstractState___init__():
    assert statemachine_AbstractState.__init__(statemachine_AbstractState('', statemachine_AbstractState=statemachine_StateMachine(), AbstractState=statemachine_Transition(), AbstractState9=statemachine_Transition(), source=set(), target=set()), '', statemachine_AbstractState=statemachine_StateMachine(), AbstractState=statemachine_Transition(), AbstractState9=statemachine_Transition(), source=set(), target=set()) == None


from python_code import statemachine_FiringElement

def test_statemachine_FiringElement___init__():
    assert statemachine_FiringElement.__init__(statemachine_FiringElement('', '\x00'), '\x00\x00', '') == None

