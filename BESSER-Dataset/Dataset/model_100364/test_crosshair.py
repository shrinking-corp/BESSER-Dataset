from python_code import fsm_NamedElement

def test_fsm_NamedElement___init__():
    assert fsm_NamedElement.__init__(fsm_NamedElement(''), '') == None


from python_code import fsm_TimedTransition

def test_fsm_TimedTransition___init__():
    assert fsm_TimedTransition.__init__(fsm_TimedTransition(0), 0) == None


from python_code import fsm_StateMachine
from python_code import fsm_Variable

def test_fsm_Variable___init__():
    assert fsm_Variable.__init__(fsm_Variable('', False, fsm_Variable=fsm_StateMachine()), '', False, fsm_Variable=fsm_StateMachine()) == None

