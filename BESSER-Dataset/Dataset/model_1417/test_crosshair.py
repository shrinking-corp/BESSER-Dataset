from python_code import sam_DataFlow
from python_code import sam_DataPort

def test_sam_DataFlow___init__():
    assert sam_DataFlow.__init__(sam_DataFlow('', sam_DataFlow=sam_DataPort(), sam_DataFlow47=set()), '', sam_DataFlow=sam_DataPort(), sam_DataFlow47=set()) == None


from python_code import sam_IdentifiedItem

def test_sam_IdentifiedItem___init__():
    assert sam_IdentifiedItem.__init__(sam_IdentifiedItem('', '\x00'), '\x00\x00', '') == None


from python_code import sam_NamedItem

def test_sam_NamedItem___init__():
    assert sam_NamedItem.__init__(sam_NamedItem(''), '') == None


from python_code import sam_AbstractState
from python_code import sam_Automaton
from python_code import sam_State
from python_code import sam_Transition

def test_sam_Transition___init__():
    assert sam_Transition.__init__(sam_Transition('', '', '\x00\x00', Transition=sam_AbstractState(), Transition4=sam_Automaton(), Transition14=sam_State(), inlink=sam_State(), listTransitions=sam_Automaton(), outlink=sam_AbstractState()), '', '', '', Transition=sam_AbstractState(), Transition4=sam_Automaton(), Transition14=sam_State(), inlink=sam_State(), listTransitions=sam_Automaton(), outlink=sam_AbstractState()) == None

