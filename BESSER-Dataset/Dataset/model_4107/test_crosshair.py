from enum import Enum
from python_code import PseudostateKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PseudostateKind.initial, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PseudostateKind.initial, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PseudostateKind.initial, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PseudostateKind.initial, 0)

def test_Enum___new___2():
    assert Enum.__new__(PseudostateKind.initial, 'initial') == PseudostateKind.initial

from python_code import compositestates_NamedElement

def test_compositestates_NamedElement___init__():
    assert compositestates_NamedElement.__init__(compositestates_NamedElement(''), '') == None

from python_code import compositestates_Pseudostate

def test_compositestates_Pseudostate___init__():
    assert compositestates_Pseudostate.__init__(compositestates_Pseudostate(''), '') == None
