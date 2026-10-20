from python_code import HSM_State
from python_code import HSM_StateMachine

def test_HSM_State___init__():
    assert HSM_State.__init__(HSM_State('', HSM_State=HSM_StateMachine()), '', HSM_State=HSM_StateMachine()) == None

