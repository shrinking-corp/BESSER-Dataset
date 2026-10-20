from python_code import petriNet_PetriNet
from python_code import petriNet_PetriNetElt

def test_petriNet_PetriNet___init__():
    assert petriNet_PetriNet.__init__(petriNet_PetriNet('', petriNet_PetriNet=petriNet_PetriNetElt(), petriNet_PetriNet8=set()), '', petriNet_PetriNet=petriNet_PetriNetElt(), petriNet_PetriNet8=set()) == None


from python_code import petriNet_Place

def test_petriNet_Place___init__():
    assert petriNet_Place.__init__(petriNet_Place(0), 0) == None

