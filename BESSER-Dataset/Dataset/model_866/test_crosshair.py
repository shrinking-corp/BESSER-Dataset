from python_code import fsm_FSM
from python_code import fsm_InitialState

def test_fsm_InitialState___init__():
    assert fsm_InitialState.__init__(fsm_InitialState('', fsm_InitialState=fsm_FSM()), '', fsm_InitialState=fsm_FSM()) == None

