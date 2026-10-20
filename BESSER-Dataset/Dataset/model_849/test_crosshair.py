from python_code import fsm_NamedElement

def test_fsm_NamedElement___init__():
    assert fsm_NamedElement.__init__(fsm_NamedElement(''), '') == None


from python_code import fsm_State
from python_code import fsm_Transition

def test_fsm_Transition___init__():
    assert fsm_Transition.__init__(fsm_Transition('', '\x00', Transition=fsm_State(), fsm_Transition=fsm_State(), leavingTransitions=fsm_State()), '\x00\x00', '', Transition=fsm_State(), fsm_Transition=fsm_State(), leavingTransitions=fsm_State()) == None

