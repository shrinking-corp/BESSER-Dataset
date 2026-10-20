from python_code import petrinet_PetriNet
from python_code import petrinet_PetriNetElement

def test_petrinet_PetriNet___init__():
    assert petrinet_PetriNet.__init__(petrinet_PetriNet('', petriNet=set(), PetriNet=petrinet_PetriNetElement()), '', petriNet=set(), PetriNet=petrinet_PetriNetElement()) == None


from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0), 0) == None

