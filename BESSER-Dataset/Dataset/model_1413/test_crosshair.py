from python_code import NHSM_State
from python_code import NHSM_StateMachine
from python_code import NHSM_Transition

def test_NHSM_State___init__():
    assert NHSM_State.__init__(NHSM_State('', NHSM_State5=NHSM_Transition(), NHSM_State8=NHSM_Transition(), NHSM_State=NHSM_StateMachine()), '', NHSM_State5=NHSM_Transition(), NHSM_State8=NHSM_Transition(), NHSM_State=NHSM_StateMachine()) == None

