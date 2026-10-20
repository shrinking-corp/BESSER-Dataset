from python_code import petrinet_NamedElement

def test_petrinet_NamedElement___init__():
    assert petrinet_NamedElement.__init__(petrinet_NamedElement(''), '') == None


from python_code import petrinet_Edge
from python_code import petrinet_PetriNet
from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0, petrinet_Place=petrinet_PetriNet(), place=set(), Place=petrinet_Edge()), 0, petrinet_Place=petrinet_PetriNet(), place=set(), Place=petrinet_Edge()) == None

