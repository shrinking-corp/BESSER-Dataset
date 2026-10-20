from python_code import fsm_Buffer
from python_code import fsm_FSMSystem

def test_fsm_Buffer___init__():
    assert fsm_Buffer.__init__(fsm_Buffer('', fsm_Buffer=fsm_FSMSystem(), fsm_Buffer17=set(), fsm_Buffer20=set()), '', fsm_Buffer=fsm_FSMSystem(), fsm_Buffer17=set(), fsm_Buffer20=set()) == None


from python_code import fsm_NamedElement

def test_fsm_NamedElement___init__():
    assert fsm_NamedElement.__init__(fsm_NamedElement(''), '') == None


from python_code import fsm_State
from python_code import fsm_StateMachine
from python_code import fsm_Transition

def test_fsm_Transition___init__():
    assert fsm_Transition.__init__(fsm_Transition('', '\x00', fsm_Transition=fsm_StateMachine(), Transition=fsm_State(), Transition7=fsm_State(), outgoingTransitions=fsm_State(), incomingTransitions=fsm_State()), '\x00\x00', '', fsm_Transition=fsm_StateMachine(), Transition=fsm_State(), Transition7=fsm_State(), outgoingTransitions=fsm_State(), incomingTransitions=fsm_State()) == None

