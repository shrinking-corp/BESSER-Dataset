from python_code import dsl_FSM
from python_code import dsl_InitialState

def test_dsl_FSM___init__():
    assert dsl_FSM.__init__(dsl_FSM('', dsl_FSM2=set(), dsl_FSM4=dsl_InitialState(), dsl_FSM=set()), '', dsl_FSM2=set(), dsl_FSM4=dsl_InitialState(), dsl_FSM=set()) == None

