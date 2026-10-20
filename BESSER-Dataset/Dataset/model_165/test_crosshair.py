from python_code import PetriNets_Arc
from python_code import PetriNets_PetriNet

def test_PetriNets_Arc___init__():
    assert PetriNets_Arc.__init__(PetriNets_Arc(0, PetriNets_Arc=PetriNets_PetriNet()), 0, PetriNets_Arc=PetriNets_PetriNet()) == None

