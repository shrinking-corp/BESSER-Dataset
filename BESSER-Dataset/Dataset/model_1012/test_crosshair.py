from python_code import fsm_FSM
from python_code import fsm_InitialState

def test_fsm_FSM___init__():
    assert fsm_FSM.__init__(fsm_FSM('', fsm_FSM=set(), fsm_FSM2=set(), fsm_FSM4=fsm_InitialState()), '', fsm_FSM=set(), fsm_FSM2=set(), fsm_FSM4=fsm_InitialState()) == None

