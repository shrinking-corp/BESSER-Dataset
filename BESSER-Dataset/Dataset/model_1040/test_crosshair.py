from python_code import fsm_AndTrigger
from python_code import fsm_NotTrigger
from python_code import fsm_OrTrigger
from python_code import fsm_Transition
from python_code import fsm_Trigger

def test_fsm_Trigger___init__():
    assert fsm_Trigger.__init__(fsm_Trigger('', fsm_Trigger23=fsm_NotTrigger(), fsm_Trigger25=fsm_AndTrigger(), fsm_Trigger28=fsm_AndTrigger(), fsm_Trigger30=fsm_OrTrigger(), fsm_Trigger33=fsm_OrTrigger(), fsm_Trigger=fsm_Transition()), '', fsm_Trigger23=fsm_NotTrigger(), fsm_Trigger25=fsm_AndTrigger(), fsm_Trigger28=fsm_AndTrigger(), fsm_Trigger30=fsm_OrTrigger(), fsm_Trigger33=fsm_OrTrigger(), fsm_Trigger=fsm_Transition()) == None


from python_code import fsm_VarRef

def test_fsm_VarRef___init__():
    assert fsm_VarRef.__init__(fsm_VarRef(''), '') == None

