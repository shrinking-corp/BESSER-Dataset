from python_code import Module
from python_code import ea_automata_Automaton

def test_ea_automata_Automaton___init__():
    assert ea_automata_Automaton.__init__(ea_automata_Automaton('', '', '', automaton=set(), automaton2=set(), automata=Module()), '', '', '', automaton=set(), automaton2=set(), automata=Module()) == None


from python_code import Automaton
from python_code import ea_automata_State

def test_ea_automata_State___init__():
    assert ea_automata_State.__init__(ea_automata_State('', '', states=Automaton(), target=set(), source=set()), '', '', states=Automaton(), target=set(), source=set()) == None


from python_code import Automaton
from python_code import State
from python_code import ea_automata_Transition

def test_ea_automata_Transition___init__():
    assert ea_automata_Transition.__init__(ea_automata_Transition('', transitions=Automaton(), outgoing=State(), incoming=State()), '', transitions=Automaton(), outgoing=State(), incoming=State()) == None


from python_code import ea_extensions_BooleanExtension

def test_ea_extensions_BooleanExtension___init__():
    assert ea_extensions_BooleanExtension.__init__(ea_extensions_BooleanExtension(True), False) == None


from python_code import ea_extensions_IExtendible

def test_ea_extensions_IExtendible___init__():
    assert ea_extensions_IExtendible.__init__(ea_extensions_IExtendible(owner=set()), owner=set()) == None

def test_ea_extensions_IExtendible_updateExtension():
    assert ea_extensions_IExtendible.updateExtension(ea_extensions_IExtendible(owner=set()), 0) == None

def test_ea_extensions_IExtendible_findExtension():
    assert ea_extensions_IExtendible.findExtension(ea_extensions_IExtendible(owner=set()), 0) == None


from python_code import IExtendible
from python_code import ea_extensions_IExtension

def test_ea_extensions_IExtension___init__():
    assert ea_extensions_IExtension.__init__(ea_extensions_IExtension('', extensions=IExtendible()), '\x00', extensions=IExtendible()) == None


from python_code import ea_extensions_IntegerExtension

def test_ea_extensions_IntegerExtension___init__():
    assert ea_extensions_IntegerExtension.__init__(ea_extensions_IntegerExtension(0), 0) == None


from python_code import ea_extensions_StringExtension

def test_ea_extensions_StringExtension___init__():
    assert ea_extensions_StringExtension.__init__(ea_extensions_StringExtension(''), '') == None


from python_code import ea_extensions_StringListExtension

def test_ea_extensions_StringListExtension___init__():
    assert ea_extensions_StringListExtension.__init__(ea_extensions_StringListExtension(''), '') == None

