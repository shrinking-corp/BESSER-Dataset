from python_code import PetriNets_PTArc
from python_code import PetriNets_Place
from python_code import PetriNets_TPArc
from python_code import PetriNets_Transition

def test_PetriNets_Place___init__():
    assert PetriNets_Place.__init__(PetriNets_Place(0, PetriNets_Place5=PetriNets_Transition(), PetriNets_Place=PetriNets_Transition(), PetriNets_Place11=PetriNets_TPArc(), PetriNets_Place16=PetriNets_PTArc()), 0, PetriNets_Place5=PetriNets_Transition(), PetriNets_Place=PetriNets_Transition(), PetriNets_Place11=PetriNets_TPArc(), PetriNets_Place16=PetriNets_PTArc()) == None

