from python_code import PetriNet_Arc
from python_code import PetriNet_PetriNet

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc(0, PetriNet_Arc=PetriNet_PetriNet()), 0, PetriNet_Arc=PetriNet_PetriNet()) == None


from python_code import PetriNet_Element

def test_PetriNet_Element___init__():
    assert PetriNet_Element.__init__(PetriNet_Element(''), '') == None

