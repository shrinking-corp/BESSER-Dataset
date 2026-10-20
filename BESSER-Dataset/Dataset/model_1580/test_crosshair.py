from python_code import petrinet_Arc
from python_code import petrinet_NetworkSystem
from python_code import petrinet_PetriNet

def test_petrinet_PetriNet___init__():
    assert petrinet_PetriNet.__init__(petrinet_PetriNet('\x00', petrinet_PetriNet15=petrinet_NetworkSystem(), petrinet_PetriNet=set(), petrinet_PetriNet2=petrinet_Arc(), petrinet_PetriNet5=petrinet_Arc()), '', petrinet_PetriNet15=petrinet_NetworkSystem(), petrinet_PetriNet=set(), petrinet_PetriNet2=petrinet_Arc(), petrinet_PetriNet5=petrinet_Arc()) == None


from python_code import petrinet_InputArc
from python_code import petrinet_OutputArc
from python_code import petrinet_Transition

def test_petrinet_Transition___init__():
    assert petrinet_Transition.__init__(petrinet_Transition(0.0, 0.0, petrinet_Transition10=petrinet_InputArc(), petrinet_Transition=petrinet_OutputArc()), 0.0, 0.0, petrinet_Transition10=petrinet_InputArc(), petrinet_Transition=petrinet_OutputArc()) == None

