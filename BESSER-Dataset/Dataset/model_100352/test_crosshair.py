from python_code import dfa_NamedElement

def test_dfa_NamedElement___init__():
    assert dfa_NamedElement.__init__(dfa_NamedElement(''), '') == None


from python_code import dfa_State
from python_code import dfa_Transition

def test_dfa_State___init__():
    assert dfa_State.__init__(dfa_State('', dfa_State=dfa_Transition()), '', dfa_State=dfa_Transition()) == None


from python_code import dfa_Language
from python_code import dfa_Symbol
from python_code import dfa_Transition

def test_dfa_Symbol___init__():
    assert dfa_Symbol.__init__(dfa_Symbol('', '', '\x00\x00', dfa_Symbol=dfa_Transition(), dfa_Symbol12=dfa_Language()), '', '', '', dfa_Symbol=dfa_Transition(), dfa_Symbol12=dfa_Language()) == None

