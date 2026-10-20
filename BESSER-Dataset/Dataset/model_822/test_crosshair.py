from python_code import fsm_AssignValueAction

def test_fsm_AssignValueAction___init__():
    assert fsm_AssignValueAction.__init__(fsm_AssignValueAction(0), 0) == None


from python_code import fsm_DecreaseValueAction

def test_fsm_DecreaseValueAction___init__():
    assert fsm_DecreaseValueAction.__init__(fsm_DecreaseValueAction(0), 0) == None


from python_code import fsm_Guard
from python_code import fsm_Transition

def test_fsm_Guard___init__():
    assert fsm_Guard.__init__(fsm_Guard(True, fsm_Guard=fsm_Transition()), False, fsm_Guard=fsm_Transition()) == None


from python_code import fsm_IncreaseValueAction

def test_fsm_IncreaseValueAction___init__():
    assert fsm_IncreaseValueAction.__init__(fsm_IncreaseValueAction(0), 0) == None


from python_code import fsm_NamedElement

def test_fsm_NamedElement___init__():
    assert fsm_NamedElement.__init__(fsm_NamedElement(''), '') == None


from python_code import fsm_StateMachine
from python_code import fsm_Variable

def test_fsm_Variable___init__():
    assert fsm_Variable.__init__(fsm_Variable('', fsm_Variable=fsm_StateMachine()), '', fsm_Variable=fsm_StateMachine()) == None

