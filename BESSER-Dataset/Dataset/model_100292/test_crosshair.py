from python_code import petrinet_Arc

def test_petrinet_Arc___init__():
    assert petrinet_Arc.__init__(petrinet_Arc(0), 0) == None


from python_code import petrinet_Named

def test_petrinet_Named___init__():
    assert petrinet_Named.__init__(petrinet_Named(''), '') == None


from python_code import petrinet_InArc
from python_code import petrinet_OutArc
from python_code import petrinet_PetriNet
from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0, petrinet_Place=petrinet_PetriNet(), petrinet_Place12=petrinet_OutArc(), petrinet_Place9=petrinet_InArc()), 0, petrinet_Place=petrinet_PetriNet(), petrinet_Place12=petrinet_OutArc(), petrinet_Place9=petrinet_InArc()) == None

