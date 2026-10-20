from python_code import PetriNet_Arc
from python_code import PetriNet_PetriNet

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc(0, PetriNet_Arc=PetriNet_PetriNet()), 0, PetriNet_Arc=PetriNet_PetriNet()) == None


from python_code import PetriNet_PetriNet
from python_code import PetriNet_Place
from python_code import PetriNet_PlaceToTransArc
from python_code import PetriNet_TransToPlaceArc

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place(0, PetriNet_Place=PetriNet_PetriNet(), PetriNet_Place6=PetriNet_PlaceToTransArc(), PetriNet_Place14=PetriNet_TransToPlaceArc()), 0, PetriNet_Place=PetriNet_PetriNet(), PetriNet_Place6=PetriNet_PlaceToTransArc(), PetriNet_Place14=PetriNet_TransToPlaceArc()) == None

