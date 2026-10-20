from python_code import fsm_Transition

def test_fsm_Transition___init__():
    assert fsm_Transition.__init__(fsm_Transition(0), 0) == None

def test_fsm_Transition_f1():
    assert fsm_Transition.f1(fsm_Transition(0)) == None

def test_fsm_Transition_f2():
    assert fsm_Transition.f2(fsm_Transition(0)) == None

