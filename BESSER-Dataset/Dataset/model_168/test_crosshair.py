from python_code import PetriNet_Arc

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc('', '\x00'), '\x00\x00', '') == None


from python_code import PetriNet_PetriNet

def test_PetriNet_PetriNet___init__():
    assert PetriNet_PetriNet.__init__(PetriNet_PetriNet('', PetriNet_PetriNet=set(), PetriNet_PetriNet2=set(), PetriNet_PetriNet4=set()), '', PetriNet_PetriNet=set(), PetriNet_PetriNet2=set(), PetriNet_PetriNet4=set()) == None


from python_code import PetriNet
from python_code import PetriNet_Place

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place('', target=set(), source=set(), PetriNet_Place=PetriNet()), '', target=set(), source=set(), PetriNet_Place=PetriNet()) == None


from python_code import PetriNet_Transition

def test_PetriNet_Transition___init__():
    assert PetriNet_Transition.__init__(PetriNet_Transition('', target9=set(), source12=set()), '', target9=set(), source12=set()) == None

