from python_code import petrinet_Node

def test_petrinet_Node___init__():
    assert petrinet_Node.__init__(petrinet_Node(0.0, 0.0, ''), 0.0, 0.0, '') == None


from python_code import petrinet_PetriNet
from python_code import petrinet_PetriNetRelationship
from python_code import petrinet_System

def test_petrinet_PetriNet___init__():
    assert petrinet_PetriNet.__init__(petrinet_PetriNet('', petrinet_PetriNet=petrinet_System(), petrinet_PetriNet4=set(), petrinet_PetriNet7=petrinet_PetriNetRelationship(), petrinet_PetriNet10=petrinet_PetriNetRelationship()), '', petrinet_PetriNet=petrinet_System(), petrinet_PetriNet4=set(), petrinet_PetriNet7=petrinet_PetriNetRelationship(), petrinet_PetriNet10=petrinet_PetriNetRelationship()) == None

