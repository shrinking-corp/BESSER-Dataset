from python_code import tfsm_Guard
from python_code import tfsm_Transition

def test_tfsm_Guard___init__():
    assert tfsm_Guard.__init__(tfsm_Guard(0, tfsm_Guard=tfsm_Transition()), 0, tfsm_Guard=tfsm_Transition()) == None


from python_code import tfsm_FSM
from python_code import tfsm_State

def test_tfsm_State___init__():
    assert tfsm_State.__init__(tfsm_State(0, tfsm_State=tfsm_FSM()), 0, tfsm_State=tfsm_FSM()) == None

