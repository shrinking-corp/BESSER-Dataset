from python_code import PetriNetMM2_Arc
from python_code import PetriNetMM2_PetriNetModel

def test_PetriNetMM2_Arc___init__():
    assert PetriNetMM2_Arc.__init__(PetriNetMM2_Arc(0, PetriNetModelElement=PetriNetMM2_PetriNetModel()), 0, PetriNetModelElement=PetriNetMM2_PetriNetModel()) == None


from python_code import PetriNetMM2_GenericPT
from python_code import PetriNetMM2_PetriNetModel

def test_PetriNetMM2_GenericPT___init__():
    assert PetriNetMM2_GenericPT.__init__(PetriNetMM2_GenericPT('', PetriNetModelElement=PetriNetMM2_PetriNetModel()), '', PetriNetModelElement=PetriNetMM2_PetriNetModel()) == None


from python_code import PetriNetMM2_PetriNet
from python_code import PetriNetMM2_PetriNetModel

def test_PetriNetMM2_PetriNet___init__():
    assert PetriNetMM2_PetriNet.__init__(PetriNetMM2_PetriNet('', net=set(), net4=set(), PetriNetMM2_PetriNet=set(), PetriNetModelElement=PetriNetMM2_PetriNetModel()), '', net=set(), net4=set(), PetriNetMM2_PetriNet=set(), PetriNetModelElement=PetriNetMM2_PetriNetModel()) == None


from python_code import PetriNet
from python_code import PetriNetMM2_Place

def test_PetriNetMM2_Place___init__():
    assert PetriNetMM2_Place.__init__(PetriNetMM2_Place('', 0, places=PetriNet(), src=set(), dst=set()), '', 0, places=PetriNet(), src=set(), dst=set()) == None


from python_code import PetriNet
from python_code import PetriNetMM2_Transition

def test_PetriNetMM2_Transition___init__():
    assert PetriNetMM2_Transition.__init__(PetriNetMM2_Transition('', 0, transitions=PetriNet(), dst12=set(), src15=set()), '', 0, transitions=PetriNet(), dst12=set(), src15=set()) == None

