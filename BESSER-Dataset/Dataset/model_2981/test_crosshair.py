from python_code import automata_Automaton
from python_code import automata_State
from python_code import automata_Transition

def test_automata_State___init__():
    assert automata_State.__init__(automata_State('', False, automata_State=automata_Automaton(), automata_State7=automata_Transition(), automata_State10=automata_Transition()), '', False, automata_State=automata_Automaton(), automata_State7=automata_Transition(), automata_State10=automata_Transition()) == None


from python_code import automata_Automaton
from python_code import automata_Variable

def test_automata_Variable___init__():
    assert automata_Variable.__init__(automata_Variable('', automata_Variable=automata_Automaton()), '', automata_Variable=automata_Automaton()) == None

