from python_code import SM_State
from python_code import SM_StateMachine

def test_SM_State___init__():
    assert SM_State.__init__(SM_State('', SM_State=SM_StateMachine()), '', SM_State=SM_StateMachine()) == None

