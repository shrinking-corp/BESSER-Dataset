from enum import Enum
from python_code import Comparation
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Comparation.Less, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Comparation.Less, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Comparation.Less, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Comparation.Less, 0)

def test_Enum___new___2():
    assert Enum.__new__(Comparation.Less, 'Less') == Comparation.Less

from enum import Enum
from python_code import Protocol
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Protocol.Akka, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Protocol.Akka, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Protocol.Paho, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Protocol.Akka, 0)

def test_Enum___new___2():
    assert Enum.__new__(Protocol.Akka, 'Akka') == Protocol.Akka

from python_code import dataflownet_DataflowSystem

def test_dataflownet_DataflowSystem___init__():
    assert dataflownet_DataflowSystem.__init__(dataflownet_DataflowSystem('', dataflownet_DataflowSystem43=set(), dataflownet_DataflowSystem46=set(), dataflownet_DataflowSystem49=set(), dataflownet_DataflowSystem=set()), '', dataflownet_DataflowSystem43=set(), dataflownet_DataflowSystem46=set(), dataflownet_DataflowSystem49=set(), dataflownet_DataflowSystem=set()) == None

from python_code import dataflownet_NamedElement

def test_dataflownet_NamedElement___init__():
    assert dataflownet_NamedElement.__init__(dataflownet_NamedElement(''), '') == None

from python_code import dataflownet_StateMachineState
from python_code import dataflownet_StateMachineTransition

def test_dataflownet_StateMachineTransition___init__():
    assert dataflownet_StateMachineTransition.__init__(dataflownet_StateMachineTransition(0, StateMachineTransition=dataflownet_StateMachineState(), StateMachineTransition18=dataflownet_StateMachineState(), outputTransitions=dataflownet_StateMachineState(), inputTransitions=dataflownet_StateMachineState(), dataflownet_StateMachineTransition=set(), dataflownet_StateMachineTransition28=set()), 0, StateMachineTransition=dataflownet_StateMachineState(), StateMachineTransition18=dataflownet_StateMachineState(), outputTransitions=dataflownet_StateMachineState(), inputTransitions=dataflownet_StateMachineState(), dataflownet_StateMachineTransition=set(), dataflownet_StateMachineTransition28=set()) == None
