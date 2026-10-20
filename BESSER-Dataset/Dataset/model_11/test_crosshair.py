from python_code import petrinet_Arc
from python_code import petrinet_RefNodes

def test_petrinet_Arc___init__():
    assert petrinet_Arc.__init__(petrinet_Arc('', petrinet_Arc=petrinet_RefNodes(), petrinet_Arc6=petrinet_RefNodes()), '', petrinet_Arc=petrinet_RefNodes(), petrinet_Arc6=petrinet_RefNodes()) == None


from python_code import petrinet_Node

def test_petrinet_Node___init__():
    assert petrinet_Node.__init__(petrinet_Node(''), '') == None


from python_code import petrinet_PetriNet

def test_petrinet_PetriNet___init__():
    assert petrinet_PetriNet.__init__(petrinet_PetriNet('', petrinet_PetriNet=set(), petrinet_PetriNet2=set()), '', petrinet_PetriNet=set(), petrinet_PetriNet2=set()) == None


from python_code import petrinet_Token

def test_petrinet_Token___init__():
    assert petrinet_Token.__init__(petrinet_Token(''), '') == None

