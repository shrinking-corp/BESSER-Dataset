from python_code import fsm_Transition

def test_fsm_Transition___init__():
    assert fsm_Transition.__init__(fsm_Transition('', '', '\x00\x00'), '', '', '') == None

def test_fsm_Transition_foo():
    assert fsm_Transition.foo(fsm_Transition('', '', '\x00'), '', '') == None

