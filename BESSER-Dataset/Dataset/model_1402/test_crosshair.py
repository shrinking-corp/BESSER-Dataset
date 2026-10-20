from python_code import HSM_StateMachine

def test_HSM_StateMachine___init__():
    assert HSM_StateMachine.__init__(HSM_StateMachine(HSM_StateMachine=set(), HSM_StateMachine2=set()), HSM_StateMachine=set(), HSM_StateMachine2=set()) == None

def test_HSM_StateMachine_addTransition():
    assert HSM_StateMachine.addTransition(HSM_StateMachine(HSM_StateMachine=set(), HSM_StateMachine2=set()), 0, '') == None

