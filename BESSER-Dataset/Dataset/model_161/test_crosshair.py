from python_code import PetriNetModel_Arc
from python_code import PetriNetModel_Node

def test_PetriNetModel_Node___init__():
    assert PetriNetModel_Node.__init__(PetriNetModel_Node('', source=set(), Node=PetriNetModel_Arc(), Node7=PetriNetModel_Arc(), target=set()), '', source=set(), Node=PetriNetModel_Arc(), Node7=PetriNetModel_Arc(), target=set()) == None


from python_code import PetriNetModel_PObject
from python_code import PetriNetModel_PetriNet

def test_PetriNetModel_PObject___init__():
    assert PetriNetModel_PObject.__init__(PetriNetModel_PObject(0, PetriNetModel_PObject=PetriNetModel_PetriNet()), 0, PetriNetModel_PObject=PetriNetModel_PetriNet()) == None

