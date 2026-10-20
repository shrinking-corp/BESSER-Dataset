from python_code import petrinet_PetriNet

def test_petrinet_PetriNet___init__():
    assert petrinet_PetriNet.__init__(petrinet_PetriNet('', petrinet_PetriNet=set(), petrinet_PetriNet2=set()), '', petrinet_PetriNet=set(), petrinet_PetriNet2=set()) == None


from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0), 0) == None


from python_code import petrinet_Transition

def test_petrinet_Transition___init__():
    assert petrinet_Transition.__init__(petrinet_Transition(0, 0), 0, 0) == None

