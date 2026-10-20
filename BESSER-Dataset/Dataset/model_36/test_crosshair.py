from python_code import PetriNet_Arc
from python_code import PetriNet_PetriNet

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc('', 0, PetriNet_Arc=PetriNet_PetriNet()), '', 0, PetriNet_Arc=PetriNet_PetriNet()) == None


from python_code import PetriNet_Node
from python_code import PetriNet_PetriNet

def test_PetriNet_Node___init__():
    assert PetriNet_Node.__init__(PetriNet_Node('', PetriNet_Node=PetriNet_PetriNet()), '', PetriNet_Node=PetriNet_PetriNet()) == None


from python_code import PetriNet_PTArc
from python_code import PetriNet_Place
from python_code import PetriNet_TPArc

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place(0, PetriNet_Place=PetriNet_PTArc(), PetriNet_Place10=PetriNet_TPArc()), 0, PetriNet_Place=PetriNet_PTArc(), PetriNet_Place10=PetriNet_TPArc()) == None

