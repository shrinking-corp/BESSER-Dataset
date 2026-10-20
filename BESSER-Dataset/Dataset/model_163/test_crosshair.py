from python_code import petrinet_Arc

def test_petrinet_Arc___init__():
    assert petrinet_Arc.__init__(petrinet_Arc(0), 0) == None


from python_code import petrinet_PTArc
from python_code import petrinet_PetriNet
from python_code import petrinet_Place
from python_code import petrinet_TPArc

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place('\x00\x00', 0, petrinet_Place=petrinet_PetriNet(), source5=set(), Place=petrinet_PTArc(), petrinet_Place10=petrinet_TPArc()), '', 0, petrinet_Place=petrinet_PetriNet(), source5=set(), Place=petrinet_PTArc(), petrinet_Place10=petrinet_TPArc()) == None


from python_code import petrinet_PTArc
from python_code import petrinet_PetriNet
from python_code import petrinet_TPArc
from python_code import petrinet_Transition

def test_petrinet_Transition___init__():
    assert petrinet_Transition.__init__(petrinet_Transition('', petrinet_Transition=petrinet_PetriNet(), source=set(), petrinet_Transition7=petrinet_PTArc(), Transition=petrinet_TPArc()), '', petrinet_Transition=petrinet_PetriNet(), source=set(), petrinet_Transition7=petrinet_PTArc(), Transition=petrinet_TPArc()) == None

