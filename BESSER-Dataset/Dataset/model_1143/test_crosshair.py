from python_code import myStateMachines_Event
from python_code import myStateMachines_Statemachine
from python_code import myStateMachines_Transition

def test_myStateMachines_Event___init__():
    assert myStateMachines_Event.__init__(myStateMachines_Event('', myStateMachines_Event=myStateMachines_Statemachine(), myStateMachines_Event10=myStateMachines_Transition()), '', myStateMachines_Event=myStateMachines_Statemachine(), myStateMachines_Event10=myStateMachines_Transition()) == None


from python_code import myStateMachines_State
from python_code import myStateMachines_Statemachine
from python_code import myStateMachines_Transition

def test_myStateMachines_State___init__():
    assert myStateMachines_State.__init__(myStateMachines_State('\x00\x00', '', myStateMachines_State4=myStateMachines_Statemachine(), myStateMachines_State7=set(), myStateMachines_State13=myStateMachines_Transition(), myStateMachines_State=myStateMachines_Statemachine()), '', '', myStateMachines_State4=myStateMachines_Statemachine(), myStateMachines_State7=set(), myStateMachines_State13=myStateMachines_Transition(), myStateMachines_State=myStateMachines_Statemachine()) == None

