from enum import Enum
from python_code import ActorCommunicationType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ActorCommunicationType.DATA_DRIVEN, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ActorCommunicationType.SYNCHRONOUS, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ActorCommunicationType.SYNCHRONOUS, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ActorCommunicationType.SYNCHRONOUS, 0)

def test_Enum___new___2():
    assert Enum.__new__(ActorCommunicationType.DATA_DRIVEN, 'DATA_DRIVEN') == ActorCommunicationType.DATA_DRIVEN

from enum import Enum
from python_code import CommunicationType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CommunicationType.SYNCHRONOUS, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CommunicationType.SYNCHRONOUS, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CommunicationType.EVENT_DRIVEN, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CommunicationType.SYNCHRONOUS, 0)

def test_Enum___new___2():
    assert Enum.__new__(CommunicationType.SYNCHRONOUS, 'SYNCHRONOUS') == CommunicationType.SYNCHRONOUS

from python_code import room_BaseState
from python_code import room_RefinedState
from python_code import room_StateTerminal
from python_code import room_SubStateTrPointTerminal

def test_room_BaseState___init__():
    assert room_BaseState.__init__(room_BaseState('', room_BaseState252=room_StateTerminal(), room_BaseState259=room_SubStateTrPointTerminal(), room_BaseState=room_RefinedState()), '', room_BaseState252=room_StateTerminal(), room_BaseState259=room_SubStateTrPointTerminal(), room_BaseState=room_RefinedState()) == None

from python_code import room_LogicalThread
from python_code import room_SubSystemClass

def test_room_LogicalThread___init__():
    assert room_LogicalThread.__init__(room_LogicalThread('\x00\x00', 0, room_LogicalThread180=set(), room_LogicalThread=room_SubSystemClass()), '', 0, room_LogicalThread180=set(), room_LogicalThread=room_SubSystemClass()) == None

from python_code import room_StateGraphItem

def test_room_StateGraphItem___init__():
    assert room_StateGraphItem.__init__(room_StateGraphItem()) == None

def test_room_StateGraphItem_getName():
    assert room_StateGraphItem.getName(room_StateGraphItem()) == None

from python_code import room_StateGraph
from python_code import room_SubStateTrPointTerminal
from python_code import room_TrPoint
from python_code import room_TrPointTerminal

def test_room_TrPoint___init__():
    assert room_TrPoint.__init__(room_TrPoint('', room_TrPoint254=room_TrPointTerminal(), room_TrPoint256=room_SubStateTrPointTerminal(), room_TrPoint=room_StateGraph()), '', room_TrPoint254=room_TrPointTerminal(), room_TrPoint256=room_SubStateTrPointTerminal(), room_TrPoint=room_StateGraph()) == None

from python_code import room_TransitionPoint

def test_room_TransitionPoint___init__():
    assert room_TransitionPoint.__init__(room_TransitionPoint(True), False) == None
