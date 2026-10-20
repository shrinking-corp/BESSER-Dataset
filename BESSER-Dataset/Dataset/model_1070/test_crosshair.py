from python_code import PetriNet_Arc
from python_code import PetriNet_PetriNet

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc('', Arc=PetriNet_PetriNet(), arcs=PetriNet_PetriNet()), '', Arc=PetriNet_PetriNet(), arcs=PetriNet_PetriNet()) == None


from python_code import PetriNet_LocatedElement

def test_PetriNet_LocatedElement___init__():
    assert PetriNet_LocatedElement.__init__(PetriNet_LocatedElement(''), '') == None


from python_code import PetriNet_NamedElement

def test_PetriNet_NamedElement___init__():
    assert PetriNet_NamedElement.__init__(PetriNet_NamedElement(''), '') == None

