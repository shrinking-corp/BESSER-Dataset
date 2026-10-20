from python_code import PetriNet_InputArc
from python_code import PetriNet_Net
from python_code import PetriNet_OutputArc
from python_code import PetriNet_Place

def test_PetriNet_Place___init__():
    assert PetriNet_Place.__init__(PetriNet_Place('', PetriNet_Place=set(), PetriNet_Place2=set(), PetriNet_Place4=set(), PetriNet_Place12=PetriNet_InputArc(), PetriNet_Place18=PetriNet_OutputArc(), PetriNet_Place23=PetriNet_Net()), '', PetriNet_Place=set(), PetriNet_Place2=set(), PetriNet_Place4=set(), PetriNet_Place12=PetriNet_InputArc(), PetriNet_Place18=PetriNet_OutputArc(), PetriNet_Place23=PetriNet_Net()) == None


from python_code import PetriNet_InputArc
from python_code import PetriNet_OutputArc
from python_code import PetriNet_Transition

def test_PetriNet_Transition___init__():
    assert PetriNet_Transition.__init__(PetriNet_Transition('', PetriNet_Transition=set(), PetriNet_Transition8=set(), PetriNet_Transition15=PetriNet_InputArc(), PetriNet_Transition21=PetriNet_OutputArc()), '', PetriNet_Transition=set(), PetriNet_Transition8=set(), PetriNet_Transition15=PetriNet_InputArc(), PetriNet_Transition21=PetriNet_OutputArc()) == None

