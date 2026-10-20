from python_code import PetriNet_Arc

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc(''), '') == None


from python_code import PetriNet
from python_code import PetriNet_Place

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place('', target=set(), source=set(), places=PetriNet()), '', target=set(), source=set(), places=PetriNet()) == None

