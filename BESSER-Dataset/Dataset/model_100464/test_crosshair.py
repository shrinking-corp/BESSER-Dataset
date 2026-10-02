from enum import Enum
from python_code import AdditiveOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AdditiveOperator.minus, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AdditiveOperator.minus, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AdditiveOperator.plus, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AdditiveOperator.plus, 0)

def test_Enum___new___2():
    assert Enum.__new__(AdditiveOperator.plus, 'plus') == AdditiveOperator.plus

from enum import Enum
from python_code import AssignmentOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AssignmentOperator.assign, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AssignmentOperator.assign, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AssignmentOperator.assign, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AssignmentOperator.assign, '')

def test_Enum___new___2():
    assert Enum.__new__(AssignmentOperator.assign, 'assign') == AssignmentOperator.assign

from enum import Enum
from python_code import Direction
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Direction.OUT, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Direction.OUT, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Direction.OUT, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Direction.IN, 0)

def test_Enum___new___2():
    assert Enum.__new__(Direction.IN, 'IN') == Direction.IN

from enum import Enum
from python_code import MultiplicativeOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(MultiplicativeOperator.mod, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MultiplicativeOperator.mul, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MultiplicativeOperator.mul, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MultiplicativeOperator.mod, 0)

def test_Enum___new___2():
    assert Enum.__new__(MultiplicativeOperator.mod, 'mod') == MultiplicativeOperator.mod

from enum import Enum
from python_code import RelationalOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RelationalOperator.smaller, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RelationalOperator.equals, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RelationalOperator.smaller, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RelationalOperator.equals, 0)

def test_Enum___new___2():
    assert Enum.__new__(RelationalOperator.equals, 'smaller') == RelationalOperator.smaller

from enum import Enum
from python_code import ShiftOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ShiftOperator.right, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ShiftOperator.right, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ShiftOperator.left, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ShiftOperator.left, 0)

def test_Enum___new___2():
    assert Enum.__new__(ShiftOperator.left, 'left') == ShiftOperator.left

from enum import Enum
from python_code import TimeEventType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TimeEventType.every, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TimeEventType.every, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TimeEventType.after, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TimeEventType.every, 0)

def test_Enum___new___2():
    assert Enum.__new__(TimeEventType.every, 'every') == TimeEventType.every

from enum import Enum
from python_code import TimeUnit
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TimeUnit.second, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TimeUnit.second, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TimeUnit.second, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TimeUnit.second, 0)

def test_Enum___new___2():
    assert Enum.__new__(TimeUnit.second, 'second') == TimeUnit.second

from enum import Enum
from python_code import Type
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Type.void, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Type.real, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Type.real, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Type.real, 0)

def test_Enum___new___2():
    assert Enum.__new__(Type.real, 'void') == Type.void

from enum import Enum
from python_code import UnaryOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(UnaryOperator.positive, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(UnaryOperator.positive, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(UnaryOperator.positive, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(UnaryOperator.positive, 0)

def test_Enum___new___2():
    assert Enum.__new__(UnaryOperator.positive, 'positive') == UnaryOperator.positive

from python_code import stext_Assignment
from python_code import stext_Expression
from python_code import stext_Variable

def test_stext_Assignment___init__():
    assert stext_Assignment.__init__(stext_Assignment('', stext_Assignment=stext_Variable(), stext_Assignment23=stext_Expression()), '', stext_Assignment=stext_Variable(), stext_Assignment23=stext_Expression()) == None

from python_code import stext_EventDefinition
from python_code import stext_EventDerivation

def test_stext_EventDefinition___init__():
    assert stext_EventDefinition.__init__(stext_EventDefinition('', '\x00', stext_EventDefinition=stext_EventDerivation()), '\x00\x00', '', stext_EventDefinition=stext_EventDerivation()) == None

from python_code import stext_InterfaceScope

def test_stext_InterfaceScope___init__():
    assert stext_InterfaceScope.__init__(stext_InterfaceScope(''), '') == None

from python_code import stext_Expression
from python_code import stext_LogicalRelationExpression

def test_stext_LogicalRelationExpression___init__():
    assert stext_LogicalRelationExpression.__init__(stext_LogicalRelationExpression('', stext_LogicalRelationExpression=stext_Expression(), stext_LogicalRelationExpression75=stext_Expression()), '', stext_LogicalRelationExpression=stext_Expression(), stext_LogicalRelationExpression75=stext_Expression()) == None

from python_code import stext_Expression
from python_code import stext_NumericalAddSubtractExpression

def test_stext_NumericalAddSubtractExpression___init__():
    assert stext_NumericalAddSubtractExpression.__init__(stext_NumericalAddSubtractExpression('', stext_NumericalAddSubtractExpression85=stext_Expression(), stext_NumericalAddSubtractExpression=stext_Expression()), '', stext_NumericalAddSubtractExpression85=stext_Expression(), stext_NumericalAddSubtractExpression=stext_Expression()) == None

from python_code import stext_Expression
from python_code import stext_NumericalMultiplyDivideExpression

def test_stext_NumericalMultiplyDivideExpression___init__():
    assert stext_NumericalMultiplyDivideExpression.__init__(stext_NumericalMultiplyDivideExpression('', stext_NumericalMultiplyDivideExpression=stext_Expression(), stext_NumericalMultiplyDivideExpression90=stext_Expression()), '', stext_NumericalMultiplyDivideExpression=stext_Expression(), stext_NumericalMultiplyDivideExpression90=stext_Expression()) == None

from python_code import stext_Expression
from python_code import stext_NumericalUnaryExpression

def test_stext_NumericalUnaryExpression___init__():
    assert stext_NumericalUnaryExpression.__init__(stext_NumericalUnaryExpression('', stext_NumericalUnaryExpression=stext_Expression()), '', stext_NumericalUnaryExpression=stext_Expression()) == None

from python_code import stext_Operation
from python_code import stext_OperationCall

def test_stext_Operation___init__():
    assert stext_Operation.__init__(stext_Operation('', '\x00', stext_Operation=stext_OperationCall()), '\x00\x00', '', stext_Operation=stext_OperationCall()) == None

from python_code import stext_PrimitiveValueExpression

def test_stext_PrimitiveValueExpression___init__():
    assert stext_PrimitiveValueExpression.__init__(stext_PrimitiveValueExpression(''), '') == None

from python_code import stext_ReactionPriority

def test_stext_ReactionPriority___init__():
    assert stext_ReactionPriority.__init__(stext_ReactionPriority(0), 0) == None

from python_code import stext_Expression
from python_code import stext_ShiftExpression

def test_stext_ShiftExpression___init__():
    assert stext_ShiftExpression.__init__(stext_ShiftExpression('', stext_ShiftExpression=stext_Expression(), stext_ShiftExpression80=stext_Expression()), '', stext_ShiftExpression=stext_Expression(), stext_ShiftExpression80=stext_Expression()) == None

from python_code import stext_StatechartDefinition
from python_code import stext_StatechartRoot

def test_stext_StatechartDefinition___init__():
    assert stext_StatechartDefinition.__init__(stext_StatechartDefinition('', stext_StatechartDefinition=stext_StatechartRoot(), stext_StatechartDefinition5=set()), '', stext_StatechartDefinition=stext_StatechartRoot(), stext_StatechartDefinition5=set()) == None

from python_code import stext_TimeEventSpec

def test_stext_TimeEventSpec___init__():
    assert stext_TimeEventSpec.__init__(stext_TimeEventSpec('', 0, '\x00\x00'), '', 0, '') == None

from python_code import stext_VariableDefinition

def test_stext_VariableDefinition___init__():
    assert stext_VariableDefinition.__init__(stext_VariableDefinition(False, False, '', ''), False, False, '', '') == None
