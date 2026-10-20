from python_code import PetriNet_Place

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place(0), 0) == None


from python_code import PetriNet_PetriElement
from python_code import PetriNet_ReseauPetri

def test_PetriNet_ReseauPetri___init__():
    assert PetriNet_ReseauPetri.__init__(PetriNet_ReseauPetri('', PetriNet_ReseauPetri=set(), PetriNet_ReseauPetri6=PetriNet_PetriElement()), '', PetriNet_ReseauPetri=set(), PetriNet_ReseauPetri6=PetriNet_PetriElement()) == None

