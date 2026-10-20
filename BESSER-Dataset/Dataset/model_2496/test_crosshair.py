from python_code import y5fsm_Region
from python_code import y5fsm_State

def test_y5fsm_State___init__():
    assert y5fsm_State.__init__(y5fsm_State('', y5fsm_State=y5fsm_Region(), y5fsm_State2=set(), y5fsm_State4=set()), '', y5fsm_State=y5fsm_Region(), y5fsm_State2=set(), y5fsm_State4=set()) == None

