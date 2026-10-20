from python_code import PetriNet_Place

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place(0), 0) == None


from python_code import PetriNet_Transition

def test_PetriNet_Transition___init__():
    assert PetriNet_Transition.__init__(PetriNet_Transition(0, 0), 0, 0) == None

