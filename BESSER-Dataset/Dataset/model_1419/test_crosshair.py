from python_code import statemachine_Event
from python_code import statemachine_Statemachine
from python_code import statemachine_Transition

def test_statemachine_Event___init__():
    assert statemachine_Event.__init__(statemachine_Event('', '\x00', statemachine_Event=statemachine_Statemachine(), statemachine_Event3=statemachine_Statemachine(), statemachine_Event15=statemachine_Transition()), '\x00\x00', '', statemachine_Event=statemachine_Statemachine(), statemachine_Event3=statemachine_Statemachine(), statemachine_Event15=statemachine_Transition()) == None


from python_code import statemachine_State
from python_code import statemachine_Statemachine
from python_code import statemachine_Transition

def test_statemachine_State___init__():
    assert statemachine_State.__init__(statemachine_State('', statemachine_State=statemachine_Statemachine(), statemachine_State9=set(), statemachine_State12=set(), statemachine_State18=statemachine_Transition()), '', statemachine_State=statemachine_Statemachine(), statemachine_State9=set(), statemachine_State12=set(), statemachine_State18=statemachine_Transition()) == None

