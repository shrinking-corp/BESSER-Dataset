from python_code import petrinet_PetriNet

def test_petrinet_PetriNet___init__():
    assert petrinet_PetriNet.__init__(petrinet_PetriNet('', petrinet_PetriNet=set(), petrinet_PetriNet2=set()), '', petrinet_PetriNet=set(), petrinet_PetriNet2=set()) == None


from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0, petrinet_Place=set()), 0, petrinet_Place=set()) == None

def test_petrinet_Place_hasCapacity():
    assert petrinet_Place.hasCapacity(petrinet_Place(0, petrinet_Place=set()), '') == None


from python_code import petrinet_Transition

def test_petrinet_Transition___init__():
    assert petrinet_Transition.__init__(petrinet_Transition()) == None

def test_petrinet_Transition_isEnabled():
    assert petrinet_Transition.isEnabled(petrinet_Transition()) == None

def test_petrinet_Transition_fire():
    assert petrinet_Transition.fire(petrinet_Transition()) == None

