from python_code import state_State

def test_state_State___init__():
    assert state_State.__init__(state_State('', '\x00'), '\x00\x00', '') == None


from python_code import state_Module
from python_code import state_StateMachine

def test_state_StateMachine___init__():
    assert state_StateMachine.__init__(state_StateMachine('', state_StateMachine=set(), state_StateMachine17=set(), state_StateMachine20=state_Module()), '', state_StateMachine=set(), state_StateMachine17=set(), state_StateMachine20=state_Module()) == None

