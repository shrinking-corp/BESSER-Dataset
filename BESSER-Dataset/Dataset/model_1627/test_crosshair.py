from python_code import petri_NamedElement
from python_code import petri_PetriNet

def test_petri_NamedElement___init__():
    assert petri_NamedElement.__init__(petri_NamedElement('', petri_NamedElement=petri_PetriNet()), '', petri_NamedElement=petri_PetriNet()) == None


from python_code import petri_Place
from python_code import petri_Transition

def test_petri_Place___init__():
    assert petri_Place.__init__(petri_Place(0, petri_Place=petri_Transition(), petri_Place4=petri_Transition()), 0, petri_Place=petri_Transition(), petri_Place4=petri_Transition()) == None

