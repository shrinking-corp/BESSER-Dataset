from python_code import fsmcore_NamedElement

def test_fsmcore_NamedElement___init__():
    assert fsmcore_NamedElement.__init__(fsmcore_NamedElement(''), '') == None


from python_code import fsmcore_Transition
from python_code import fsmcore_Trigger

def test_fsmcore_Trigger___init__():
    assert fsmcore_Trigger.__init__(fsmcore_Trigger('', fsmcore_Trigger=fsmcore_Transition()), '', fsmcore_Trigger=fsmcore_Transition()) == None

