from python_code import PetriNets_PetriNet
from python_code import PetriNets_Place
from python_code import PetriNets_Token
from python_code import PetriNets_Transition

def test_PetriNets_Place___init__():
    assert PetriNets_Place.__init__(PetriNets_Place(0, 0, Place=PetriNets_PetriNet(), places=PetriNets_PetriNet(), place=set(), PetriNets_Place12=PetriNets_Transition(), Place6=PetriNets_Token(), PetriNets_Place=PetriNets_Transition()), 0, 0, Place=PetriNets_PetriNet(), places=PetriNets_PetriNet(), place=set(), PetriNets_Place12=PetriNets_Transition(), Place6=PetriNets_Token(), PetriNets_Place=PetriNets_Transition()) == None

def test_PetriNets_Place_tokens():
    assert PetriNets_Place.tokens(PetriNets_Place(0, 0, Place=PetriNets_PetriNet(), places=PetriNets_PetriNet(), place=set(), PetriNets_Place12=PetriNets_Transition(), Place6=PetriNets_Token(), PetriNets_Place=PetriNets_Transition())) == None

