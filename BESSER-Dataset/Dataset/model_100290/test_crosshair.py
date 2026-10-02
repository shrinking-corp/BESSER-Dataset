from enum import Enum
from python_code import ArcKindType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ArcKindType.normal, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ArcKindType.normal, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ArcKindType.normal, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ArcKindType.normal, 0)

def test_Enum___new___2():
    assert Enum.__new__(ArcKindType.normal, 'normal') == ArcKindType.normal

from python_code import petrinet_PetriNet

def test_petrinet_PetriNet___init__():
    assert petrinet_PetriNet.__init__(petrinet_PetriNet('', petrinet_PetriNet2=set(), petrinet_PetriNet=set()), '', petrinet_PetriNet2=set(), petrinet_PetriNet=set()) == None

from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0), 0) == None

from python_code import petrinet_Transition

def test_petrinet_Transition___init__():
    assert petrinet_Transition.__init__(petrinet_Transition(0, 0), 0, 0) == None
