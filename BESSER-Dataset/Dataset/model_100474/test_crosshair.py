from python_code import stm_Event
from python_code import stm_SelfEvent
from python_code import stm_Statemachine
from python_code import stm_Transition

def test_stm_Event___init__():
    assert stm_Event.__init__(stm_Event('', stm_Event=stm_Statemachine(), stm_Event28=stm_Transition(), stm_Event39=stm_SelfEvent()), '', stm_Event=stm_Statemachine(), stm_Event28=stm_Transition(), stm_Event39=stm_SelfEvent()) == None

