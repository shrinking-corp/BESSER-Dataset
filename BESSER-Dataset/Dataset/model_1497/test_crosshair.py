from python_code import PetriNet_Arc
from python_code import PetriNet_Element
from python_code import PetriNet_PetriNetRoot

def test_PetriNet_Element___init__():
    assert PetriNet_Element.__init__(PetriNet_Element('', PetriNet_Element=PetriNet_PetriNetRoot(), PetriNet_Element5=PetriNet_Arc(), PetriNet_Element8=PetriNet_Arc()), '', PetriNet_Element=PetriNet_PetriNetRoot(), PetriNet_Element5=PetriNet_Arc(), PetriNet_Element8=PetriNet_Arc()) == None


from python_code import PetriNet_Place

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place(0), 0) == None


from python_code import PetriNet_Transition

def test_PetriNet_Transition___init__():
    assert PetriNet_Transition.__init__(PetriNet_Transition(0, 0), 0, 0) == None

