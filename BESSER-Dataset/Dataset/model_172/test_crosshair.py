from python_code import petri_Edge

def test_petri_Edge___init__():
    assert petri_Edge.__init__(petri_Edge(0), 0) == None


from python_code import petri_EdgeToPlace
from python_code import petri_PetriNet
from python_code import petri_Place

def test_petri_Place___init__():
    assert petri_Place.__init__(petri_Place(0, petri_Place=petri_PetriNet(), petri_Place4=set(), petri_Place9=petri_EdgeToPlace()), 0, petri_Place=petri_PetriNet(), petri_Place4=set(), petri_Place9=petri_EdgeToPlace()) == None


from python_code import petri_EdgeToTransition
from python_code import petri_PetriNet
from python_code import petri_Transition

def test_petri_Transition___init__():
    assert petri_Transition.__init__(petri_Transition(0, petri_Transition=petri_PetriNet(), petri_Transition6=set(), petri_Transition12=petri_EdgeToTransition()), 0, petri_Transition=petri_PetriNet(), petri_Transition6=set(), petri_Transition12=petri_EdgeToTransition()) == None

