from python_code import petrinet_Element
from python_code import petrinet_PetriNet

def test_petrinet_Element___init__():
    assert petrinet_Element.__init__(petrinet_Element('', petrinet_Element=petrinet_PetriNet()), '', petrinet_Element=petrinet_PetriNet()) == None


from python_code import petrinet_InputArc
from python_code import petrinet_OutputArc
from python_code import petrinet_Transition

def test_petrinet_Transition___init__():
    assert petrinet_Transition.__init__(petrinet_Transition(0.0, 0.0, petrinet_Transition=petrinet_OutputArc(), petrinet_Transition5=petrinet_InputArc()), 0.0, 0.0, petrinet_Transition=petrinet_OutputArc(), petrinet_Transition5=petrinet_InputArc()) == None

