from python_code import automata_BooleanGuard

def test_automata_BooleanGuard___init__():
    assert automata_BooleanGuard.__init__(automata_BooleanGuard(False, '\x00'), False, '\x00') == None


from python_code import automata_NumberGuard

def test_automata_NumberGuard___init__():
    assert automata_NumberGuard.__init__(automata_NumberGuard('', '\x00'), '\x00\x00', '') == None


from python_code import automata_Automaton
from python_code import automata_State
from python_code import automata_Transition

def test_automata_State___init__():
    assert automata_State.__init__(automata_State('', False, automata_State7=automata_Transition(), automata_State10=automata_Transition(), automata_State=automata_Automaton()), '', False, automata_State7=automata_Transition(), automata_State10=automata_Transition(), automata_State=automata_Automaton()) == None


from python_code import automata_StringGuard

def test_automata_StringGuard___init__():
    assert automata_StringGuard.__init__(automata_StringGuard('', '\x00'), '\x00\x00', '') == None


from python_code import automata_Action
from python_code import automata_Automaton
from python_code import automata_Guard
from python_code import automata_Variable

def test_automata_Variable___init__():
    assert automata_Variable.__init__(automata_Variable('', '\x00', automata_Variable=automata_Automaton(), automata_Variable17=automata_Action(), automata_Variable15=automata_Guard()), '\x00\x00', '', automata_Variable=automata_Automaton(), automata_Variable17=automata_Action(), automata_Variable15=automata_Guard()) == None

