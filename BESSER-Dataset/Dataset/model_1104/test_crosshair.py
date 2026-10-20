from python_code import evoPetrinet_Arc
from python_code import evoPetrinet_PetriNet

def test_evoPetrinet_Arc___init__():
    assert evoPetrinet_Arc.__init__(evoPetrinet_Arc('', Element=evoPetrinet_PetriNet()), '', Element=evoPetrinet_PetriNet()) == None


from python_code import evoPetrinet_LocatedElement

def test_evoPetrinet_LocatedElement___init__():
    assert evoPetrinet_LocatedElement.__init__(evoPetrinet_LocatedElement(''), '') == None


from python_code import evoPetrinet_NamedElement

def test_evoPetrinet_NamedElement___init__():
    assert evoPetrinet_NamedElement.__init__(evoPetrinet_NamedElement(''), '') == None

