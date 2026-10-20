from python_code import petrinet_metamodel_Arc
from python_code import petrinet_metamodel_PetriNet

def test_petrinet_metamodel_Arc___init__():
    assert petrinet_metamodel_Arc.__init__(petrinet_metamodel_Arc(0, petrinet_metamodel_Arc=petrinet_metamodel_PetriNet()), 0, petrinet_metamodel_Arc=petrinet_metamodel_PetriNet()) == None


from python_code import petrinet_metamodel_Element

def test_petrinet_metamodel_Element___init__():
    assert petrinet_metamodel_Element.__init__(petrinet_metamodel_Element('', '\x00'), '\x00\x00', '') == None


from python_code import petrinet_metamodel_PetriNet
from python_code import petrinet_metamodel_Place
from python_code import petrinet_metamodel_PlaceToTransArc
from python_code import petrinet_metamodel_TransToPlaceArc

def test_petrinet_metamodel_Place___init__():
    assert petrinet_metamodel_Place.__init__(petrinet_metamodel_Place(0, '', 0, Place17=petrinet_metamodel_PlaceToTransArc(), Place=petrinet_metamodel_PetriNet(), target=set(), source=set(), Place25=petrinet_metamodel_TransToPlaceArc(), places=petrinet_metamodel_PetriNet()), 0, '', 0, Place17=petrinet_metamodel_PlaceToTransArc(), Place=petrinet_metamodel_PetriNet(), target=set(), source=set(), Place25=petrinet_metamodel_TransToPlaceArc(), places=petrinet_metamodel_PetriNet()) == None


from python_code import petrinet_metamodel_Rectangle
from python_code import petrinet_metamodel_Transition

def test_petrinet_metamodel_Rectangle___init__():
    assert petrinet_metamodel_Rectangle.__init__(petrinet_metamodel_Rectangle(0, rectangle=petrinet_metamodel_Transition(), Rectangle=petrinet_metamodel_Transition()), 0, rectangle=petrinet_metamodel_Transition(), Rectangle=petrinet_metamodel_Transition()) == None

