from python_code import fsm_tp_FSM
from python_code import fsm_tp_InitialState

def test_fsm_tp_FSM___init__():
    assert fsm_tp_FSM.__init__(fsm_tp_FSM('', fsm_tp_FSM=set(), fsm_tp_FSM2=set(), fsm_tp_FSM4=fsm_tp_InitialState()), '', fsm_tp_FSM=set(), fsm_tp_FSM2=set(), fsm_tp_FSM4=fsm_tp_InitialState()) == None

