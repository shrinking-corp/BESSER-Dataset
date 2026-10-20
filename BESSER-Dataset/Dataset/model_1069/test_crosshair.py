from python_code import petriNet_Arc
from python_code import petriNet_PetriNet

def test_petriNet_Arc___init__():
    assert petriNet_Arc.__init__(petriNet_Arc(0, arcs=petriNet_PetriNet(), Arc=petriNet_PetriNet()), 0, arcs=petriNet_PetriNet(), Arc=petriNet_PetriNet()) == None


from python_code import petriNet_LocatedElement

def test_petriNet_LocatedElement___init__():
    assert petriNet_LocatedElement.__init__(petriNet_LocatedElement(''), '') == None


from python_code import petriNet_NamedElement

def test_petriNet_NamedElement___init__():
    assert petriNet_NamedElement.__init__(petriNet_NamedElement(''), '') == None

