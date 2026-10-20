from python_code import statemachines_Event
from python_code import statemachines_StateMachine
from python_code import statemachines_Transition

def test_statemachines_Event___init__():
    assert statemachines_Event.__init__(statemachines_Event('', '\x00', statemachines_Event13=statemachines_Transition(), statemachines_Event=statemachines_StateMachine(), statemachines_Event5=statemachines_StateMachine()), '\x00\x00', '', statemachines_Event13=statemachines_Transition(), statemachines_Event=statemachines_StateMachine(), statemachines_Event5=statemachines_StateMachine()) == None


from python_code import statemachines_State
from python_code import statemachines_StateMachine
from python_code import statemachines_Transition

def test_statemachines_State___init__():
    assert statemachines_State.__init__(statemachines_State('', statemachines_State=statemachines_StateMachine(), statemachines_State7=set(), statemachines_State10=statemachines_Transition()), '', statemachines_State=statemachines_StateMachine(), statemachines_State7=set(), statemachines_State10=statemachines_Transition()) == None

