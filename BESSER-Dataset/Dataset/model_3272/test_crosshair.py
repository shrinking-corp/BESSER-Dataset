from python_code import sm_Event
from python_code import sm_sm_Transition

def test_sm_Event___init__():
    assert sm_Event.__init__(sm_Event('', sm_Event=sm_sm_Transition()), '', sm_Event=sm_sm_Transition()) == None

