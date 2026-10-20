from python_code import statemachine_Event
from python_code import statemachine_SM
from python_code import statemachine_Transition

def test_statemachine_Event___init__():
    assert statemachine_Event.__init__(statemachine_Event('', statemachine_Event19=statemachine_Transition(), statemachine_Event=statemachine_SM()), '', statemachine_Event19=statemachine_Transition(), statemachine_Event=statemachine_SM()) == None


from python_code import statemachine_SM
from python_code import statemachine_State
from python_code import statemachine_Transition

def test_statemachine_State___init__():
    assert statemachine_State.__init__(statemachine_State('', statemachine_State=statemachine_SM(), statemachine_State3=statemachine_SM(), statemachine_State16=statemachine_Transition(), statemachine_State6=statemachine_SM(), statemachine_State13=statemachine_Transition()), '', statemachine_State=statemachine_SM(), statemachine_State3=statemachine_SM(), statemachine_State16=statemachine_Transition(), statemachine_State6=statemachine_SM(), statemachine_State13=statemachine_Transition()) == None

