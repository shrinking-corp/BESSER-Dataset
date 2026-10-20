from python_code import PetriNet
from python_code import PetriNet_Arc

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc(0, arcs=PetriNet()), 0, arcs=PetriNet()) == None


from python_code import PetriNet_LocatedElement

def test_PetriNet_LocatedElement___init__():
    assert PetriNet_LocatedElement.__init__(PetriNet_LocatedElement(''), '') == None


from python_code import PetriNet_NamedElement

def test_PetriNet_NamedElement___init__():
    assert PetriNet_NamedElement.__init__(PetriNet_NamedElement(''), '') == None

