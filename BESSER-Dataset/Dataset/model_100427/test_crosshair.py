from enum import Enum
from python_code import Operator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Operator.sub, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Operator.add, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Operator.eq, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Operator.eq, 0)

def test_Enum___new___2():
    assert Enum.__new__(Operator.eq, 'lt') == Operator.lt

from python_code import SimplStateMachine_BooleanData

def test_SimplStateMachine_BooleanData___init__():
    assert SimplStateMachine_BooleanData.__init__(SimplStateMachine_BooleanData(True), False) == None

from python_code import SimplStateMachine_Event
from python_code import SimplStateMachine_StateMachine
from python_code import SimplStateMachine_Transition

def test_SimplStateMachine_Event___init__():
    assert SimplStateMachine_Event.__init__(SimplStateMachine_Event('', SimplStateMachine_Event=SimplStateMachine_StateMachine(), SimplStateMachine_Event20=SimplStateMachine_Transition()), '', SimplStateMachine_Event=SimplStateMachine_StateMachine(), SimplStateMachine_Event20=SimplStateMachine_Transition()) == None

from python_code import SimplStateMachine_Expression
from python_code import SimplStateMachine_ExpressionElement
from python_code import SimplStateMachine_Transition

def test_SimplStateMachine_Expression___init__():
    assert SimplStateMachine_Expression.__init__(SimplStateMachine_Expression('', '\x00', SimplStateMachine_Expression=SimplStateMachine_Transition(), SimplStateMachine_Expression24=SimplStateMachine_ExpressionElement(), SimplStateMachine_Expression26=SimplStateMachine_ExpressionElement()), '\x00\x00', '', SimplStateMachine_Expression=SimplStateMachine_Transition(), SimplStateMachine_Expression24=SimplStateMachine_ExpressionElement(), SimplStateMachine_Expression26=SimplStateMachine_ExpressionElement()) == None

from python_code import SimplStateMachine_IntegerData

def test_SimplStateMachine_IntegerData___init__():
    assert SimplStateMachine_IntegerData.__init__(SimplStateMachine_IntegerData(0), 0) == None
