from python_code import PetriNet_PetriNet

def test_PetriNet_PetriNet___init__():
    assert PetriNet_PetriNet.__init__(PetriNet_PetriNet('', PetriNet_PetriNet2=set(), PetriNet_PetriNet=set()), '', PetriNet_PetriNet2=set(), PetriNet_PetriNet=set()) == None


from python_code import PetriNet_Place

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place(0), 0) == None

