from python_code import petri_Node
from python_code import petri_PetriNet

def test_petri_Node___init__():
    assert petri_Node.__init__(petri_Node('', petri_Node=petri_PetriNet()), '', petri_Node=petri_PetriNet()) == None


from python_code import petri_PTArc
from python_code import petri_Place
from python_code import petri_TPArc

def test_petri_Place___init__():
    assert petri_Place.__init__(petri_Place(0, petri_Place=petri_TPArc(), petri_Place7=petri_PTArc()), 0, petri_Place=petri_TPArc(), petri_Place7=petri_PTArc()) == None

