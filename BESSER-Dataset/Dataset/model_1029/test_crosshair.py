from python_code import fsm_NamedElement

def test_fsm_NamedElement___init__():
    assert fsm_NamedElement.__init__(fsm_NamedElement(''), '') == None


from python_code import fsm_AndTrigger
from python_code import fsm_NotTrigger
from python_code import fsm_OrTrigger
from python_code import fsm_Transition
from python_code import fsm_Trigger

def test_fsm_Trigger___init__():
    assert fsm_Trigger.__init__(fsm_Trigger('', fsm_Trigger=fsm_Transition(), fsm_Trigger29=fsm_NotTrigger(), fsm_Trigger31=fsm_AndTrigger(), fsm_Trigger34=fsm_AndTrigger(), fsm_Trigger36=fsm_OrTrigger(), fsm_Trigger39=fsm_OrTrigger()), '', fsm_Trigger=fsm_Transition(), fsm_Trigger29=fsm_NotTrigger(), fsm_Trigger31=fsm_AndTrigger(), fsm_Trigger34=fsm_AndTrigger(), fsm_Trigger36=fsm_OrTrigger(), fsm_Trigger39=fsm_OrTrigger()) == None

