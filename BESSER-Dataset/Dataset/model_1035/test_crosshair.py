from python_code import fsm_Block
from python_code import fsm_State

def test_fsm_Block___init__():
    assert fsm_Block.__init__(fsm_Block(fsm_Block15=fsm_State(), fsm_Block=fsm_State(), fsm_Block12=fsm_State()), fsm_Block15=fsm_State(), fsm_Block=fsm_State(), fsm_Block12=fsm_State()) == None

def test_fsm_Block_evalStatement():
    assert fsm_Block.evalStatement(fsm_Block(fsm_Block15=fsm_State(), fsm_Block=fsm_State(), fsm_Block12=fsm_State()), '') == None


from python_code import fsm_NamedElement

def test_fsm_NamedElement___init__():
    assert fsm_NamedElement.__init__(fsm_NamedElement(''), '') == None


from python_code import fsm_Transition
from python_code import fsm_Trigger

def test_fsm_Trigger___init__():
    assert fsm_Trigger.__init__(fsm_Trigger('', fsm_Trigger=fsm_Transition()), '', fsm_Trigger=fsm_Transition()) == None

