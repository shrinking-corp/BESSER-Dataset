from python_code import statechart_AbstractState
from python_code import statechart_Action

def test_statechart_Action___init__():
    assert statechart_Action.__init__(statechart_Action('', statechart_Action=statechart_AbstractState()), '', statechart_Action=statechart_AbstractState()) == None


from python_code import statechart_ModelElement

def test_statechart_ModelElement___init__():
    assert statechart_ModelElement.__init__(statechart_ModelElement(''), '') == None


from python_code import statechart_AbstractState
from python_code import statechart_CompositeState
from python_code import statechart_Transition

def test_statechart_Transition___init__():
    assert statechart_Transition.__init__(statechart_Transition('', '\x00', statechart_Transition=statechart_CompositeState(), outgoing=statechart_AbstractState(), incoming=statechart_AbstractState(), Transition=statechart_AbstractState(), Transition5=statechart_AbstractState()), '\x00\x00', '', statechart_Transition=statechart_CompositeState(), outgoing=statechart_AbstractState(), incoming=statechart_AbstractState(), Transition=statechart_AbstractState(), Transition5=statechart_AbstractState()) == None

