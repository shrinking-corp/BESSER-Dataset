from enum import Enum
from python_code import EventContext
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EventContext.RECENT, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EventContext.RECENT, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EventContext.RECENT, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EventContext.RECENT, 0)

def test_Enum___new___2():
    assert Enum.__new__(EventContext.RECENT, 'RECENT') == EventContext.RECENT

from python_code import automaton_Event
from python_code import automaton_InternalModel

def test_automaton_InternalModel___init__():
    assert automaton_InternalModel.__init__(automaton_InternalModel('', automaton_InternalModel=set(), automaton_InternalModel2=automaton_Event()), '', automaton_InternalModel=set(), automaton_InternalModel2=automaton_Event()) == None
