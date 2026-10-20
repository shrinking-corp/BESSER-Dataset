from python_code import PetriNets_Arc
from python_code import PetriNets_Node

def test_PetriNets_Node___init__():
    assert PetriNets_Node.__init__(PetriNets_Node('', source=set(), target=set(), Node=PetriNets_Arc(), Node6=PetriNets_Arc()), '', source=set(), target=set(), Node=PetriNets_Arc(), Node6=PetriNets_Arc()) == None


from python_code import PetriNets_Place

def test_PetriNets_Place___init__():
    assert PetriNets_Place.__init__(PetriNets_Place(0, PetriNets_Place=set()), 0, PetriNets_Place=set()) == None

