from python_code import statemachine_State
from python_code import statemachine_Statemachine
from python_code import statemachine_Transition

def test_statemachine_State___init__():
    assert statemachine_State.__init__(statemachine_State('', statemachine_State=statemachine_Statemachine(), statemachine_State4=set(), statemachine_State6=set(), statemachine_State11=statemachine_Transition()), '', statemachine_State=statemachine_Statemachine(), statemachine_State4=set(), statemachine_State6=set(), statemachine_State11=statemachine_Transition()) == None

