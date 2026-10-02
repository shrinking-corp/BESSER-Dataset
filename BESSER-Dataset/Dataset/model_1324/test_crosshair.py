from enum import Enum
from python_code import VisibilityType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(VisibilityType.PRIVATE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(VisibilityType.PRIVATE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(VisibilityType.PUBLIC, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(VisibilityType.PUBLIC, 0)

def test_Enum___new___2():
    assert Enum.__new__(VisibilityType.PUBLIC, 'PUBLIC') == VisibilityType.PUBLIC

from python_code import stateMachine_StateMachine

def test_stateMachine_StateMachine___init__():
    assert stateMachine_StateMachine.__init__(stateMachine_StateMachine('', stateMachine_StateMachine=set()), '', stateMachine_StateMachine=set()) == None
