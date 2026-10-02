from enum import Enum
from python_code import ArcKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ArcKind.normal, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ArcKind.normal, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ArcKind.normal, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ArcKind.normal, 0)

def test_Enum___new___2():
    assert Enum.__new__(ArcKind.normal, 'normal') == ArcKind.normal

from python_code import Node
from python_code import PetriNet
from python_code import petrinetsemantics_DDMMPetriNet_Arc

def test_petrinetsemantics_DDMMPetriNet_Arc___init__():
    assert petrinetsemantics_DDMMPetriNet_Arc.__init__(petrinetsemantics_DDMMPetriNet_Arc('\x00\x00', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), '', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()) == None

from python_code import PetriNet
from python_code import petrinetsemantics_DDMMPetriNet_Node

def test_petrinetsemantics_DDMMPetriNet_Node___init__():
    assert petrinetsemantics_DDMMPetriNet_Node.__init__(petrinetsemantics_DDMMPetriNet_Node('', nodes=PetriNet(), source=set(), target=set()), '', nodes=PetriNet(), source=set(), target=set()) == None

from python_code import petrinetsemantics_DDMMPetriNet_PetriNet

def test_petrinetsemantics_DDMMPetriNet_PetriNet___init__():
    assert petrinetsemantics_DDMMPetriNet_PetriNet.__init__(petrinetsemantics_DDMMPetriNet_PetriNet('', net=set(), net2=set()), '', net=set(), net2=set()) == None

from python_code import Node
from python_code import PetriNet
from python_code import petrinetsemantics_DDMMPetriNet_Arc
from python_code import petrinetsemantics_DDMMPetriNet_PetriNet
from python_code import petrinetsemantics_DDMMPetriNet_Place
from python_code import petrinetsemantics_SDMMPetriNet_Node_dynamic

def test_petrinetsemantics_DDMMPetriNet_Place___init__():
    assert petrinetsemantics_DDMMPetriNet_Place.__init__(petrinetsemantics_DDMMPetriNet_Place(0, Node9=petrinetsemantics_DDMMPetriNet_Arc('', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), Node11=petrinetsemantics_DDMMPetriNet_Arc('', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), Node=petrinetsemantics_DDMMPetriNet_PetriNet('', net=set(), net2=set()), Node15=petrinetsemantics_SDMMPetriNet_Node_dynamic()), 0, Node9=petrinetsemantics_DDMMPetriNet_Arc('', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), Node11=petrinetsemantics_DDMMPetriNet_Arc('\x00', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), Node=petrinetsemantics_DDMMPetriNet_PetriNet('', net=set(), net2=set()), Node15=petrinetsemantics_SDMMPetriNet_Node_dynamic()) == None

from python_code import Node
from python_code import PetriNet
from python_code import petrinetsemantics_DDMMPetriNet_Arc
from python_code import petrinetsemantics_DDMMPetriNet_PetriNet
from python_code import petrinetsemantics_DDMMPetriNet_Transition
from python_code import petrinetsemantics_SDMMPetriNet_Node_dynamic

def test_petrinetsemantics_DDMMPetriNet_Transition___init__():
    assert petrinetsemantics_DDMMPetriNet_Transition.__init__(petrinetsemantics_DDMMPetriNet_Transition(0, 0, Node9=petrinetsemantics_DDMMPetriNet_Arc('', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), Node11=petrinetsemantics_DDMMPetriNet_Arc('', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), Node=petrinetsemantics_DDMMPetriNet_PetriNet('', net=set(), net2=set()), Node15=petrinetsemantics_SDMMPetriNet_Node_dynamic()), 0, 0, Node9=petrinetsemantics_DDMMPetriNet_Arc('', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), Node11=petrinetsemantics_DDMMPetriNet_Arc('', 0, incomings=Node(), outgoings=Node(), arcs=PetriNet()), Node=petrinetsemantics_DDMMPetriNet_PetriNet('', net=set(), net2=set()), Node15=petrinetsemantics_SDMMPetriNet_Node_dynamic()) == None

from python_code import Transition
from python_code import petrinetsemantics_EDMMPetriNet_FireTransitionEvent

def test_petrinetsemantics_EDMMPetriNet_FireTransitionEvent___init__():
    assert petrinetsemantics_EDMMPetriNet_FireTransitionEvent.__init__(petrinetsemantics_EDMMPetriNet_FireTransitionEvent(0.0, petrinetsemantics_EDMMPetriNet_FireTransitionEvent=Transition()), 0.0, petrinetsemantics_EDMMPetriNet_FireTransitionEvent=Transition()) == None

from python_code import Place
from python_code import petrinetsemantics_SDMMPetriNet_PetriNet_dynamic
from python_code import petrinetsemantics_SDMMPetriNet_Place_dynamic

def test_petrinetsemantics_SDMMPetriNet_Place_dynamic___init__():
    assert petrinetsemantics_SDMMPetriNet_Place_dynamic.__init__(petrinetsemantics_SDMMPetriNet_Place_dynamic(0, petrinetsemantics_SDMMPetriNet_Place_dynamic=Place(), Node_dynamic=petrinetsemantics_SDMMPetriNet_PetriNet_dynamic()), 0, petrinetsemantics_SDMMPetriNet_Place_dynamic=Place(), Node_dynamic=petrinetsemantics_SDMMPetriNet_PetriNet_dynamic()) == None

from python_code import petrinetsemantics_TM3PetriNet_PNSimEvent

def test_petrinetsemantics_TM3PetriNet_PNSimEvent___init__():
    assert petrinetsemantics_TM3PetriNet_PNSimEvent.__init__(petrinetsemantics_TM3PetriNet_PNSimEvent(False, 0, '\x00\x00'), False, 0, '') == None
