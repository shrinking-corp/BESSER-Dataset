from python_code import PN_PetriNet

def test_PN_PetriNet___init__():
    assert PN_PetriNet.__init__(PN_PetriNet('\x00', PN_PetriNet=set()), '', PN_PetriNet=set()) == None


from python_code import PN_InputArc
from python_code import PN_OutputArc
from python_code import PN_Transition

def test_PN_Transition___init__():
    assert PN_Transition.__init__(PN_Transition(0.0, 0.0, PN_Transition=PN_OutputArc(), PN_Transition8=PN_InputArc()), 0.0, 0.0, PN_Transition=PN_OutputArc(), PN_Transition8=PN_InputArc()) == None

