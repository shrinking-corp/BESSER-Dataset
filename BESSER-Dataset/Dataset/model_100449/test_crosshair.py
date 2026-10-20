from python_code import states_ActionExecution
from python_code import states_Event
from python_code import states_Transition

def test_states_Event___init__():
    assert states_Event.__init__(states_Event('', states_Event=states_Transition(), states_Event16=states_ActionExecution()), '', states_Event=states_Transition(), states_Event16=states_ActionExecution()) == None

