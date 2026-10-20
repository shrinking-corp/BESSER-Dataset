from python_code import petriNet_Element
from python_code import petriNet_PetriNet

def test_petriNet_PetriNet___init__():
    assert petriNet_PetriNet.__init__(petriNet_PetriNet('', diagram=set(), PetriNet=petriNet_Element()), '', diagram=set(), PetriNet=petriNet_Element()) == None


from python_code import petriNet_Place
from python_code import petriNet_Transition

def test_petriNet_Place___init__():
    assert petriNet_Place.__init__(petriNet_Place(0, petriNet_Place=petriNet_Transition()), 0, petriNet_Place=petriNet_Transition()) == None

