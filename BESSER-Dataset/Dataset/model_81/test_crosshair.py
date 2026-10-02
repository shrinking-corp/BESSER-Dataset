from enum import Enum
from python_code import AssignmentKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AssignmentKind.ASSIGN, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AssignmentKind.ASSIGN, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AssignmentKind.ASSIGN, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AssignmentKind.ASSIGN, '')

def test_Enum___new___2():
    assert Enum.__new__(AssignmentKind.ASSIGN, 'ASSIGN') == AssignmentKind.ASSIGN

from enum import Enum
from python_code import InfixExpressionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InfixExpressionKind.PLUS, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InfixExpressionKind.PLUS, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InfixExpressionKind.PLUS, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InfixExpressionKind.PLUS, 0)

def test_Enum___new___2():
    assert Enum.__new__(InfixExpressionKind.TIMES, 'OR') == InfixExpressionKind.OR

from enum import Enum
from python_code import InheritanceKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InheritanceKind.none, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InheritanceKind.none, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InheritanceKind.none, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InheritanceKind.none, 0)

def test_Enum___new___2():
    assert Enum.__new__(InheritanceKind.none, 'none') == InheritanceKind.none

from enum import Enum
from python_code import PostfixExpressionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PostfixExpressionKind.DECREMENT, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PostfixExpressionKind.DECREMENT, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PostfixExpressionKind.INCREMENT, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PostfixExpressionKind.DECREMENT, 0)

def test_Enum___new___2():
    assert Enum.__new__(PostfixExpressionKind.DECREMENT, 'DECREMENT') == PostfixExpressionKind.DECREMENT

from enum import Enum
from python_code import PrefixExpressionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PrefixExpressionKind.PLUS, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PrefixExpressionKind.NOT, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PrefixExpressionKind.NOT, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PrefixExpressionKind.NOT, 0)

def test_Enum___new___2():
    assert Enum.__new__(PrefixExpressionKind.NOT, 'NOT') == PrefixExpressionKind.NOT

from enum import Enum
from python_code import VisibilityKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(VisibilityKind.public, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(VisibilityKind.none, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(VisibilityKind.none, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(VisibilityKind.none, 0)

def test_Enum___new___2():
    assert Enum.__new__(VisibilityKind.none, 'none') == VisibilityKind.none

from python_code import java__ArrayType
from python_code import java__TypeAccess

def test_java__ArrayType___init__():
    assert java__ArrayType.__init__(java__ArrayType(0, java__ArrayType=java__TypeAccess()), 0, java__ArrayType=java__TypeAccess()) == None

from python_code import java__Assignment
from python_code import java__Expression

def test_java__Assignment___init__():
    assert java__Assignment.__init__(java__Assignment('', java__Assignment=java__Expression(), java__Assignment83=java__Expression()), '', java__Assignment=java__Expression(), java__Assignment83=java__Expression()) == None

from python_code import java__BooleanLiteral

def test_java__BooleanLiteral___init__():
    assert java__BooleanLiteral.__init__(java__BooleanLiteral(True), False) == None

from python_code import java__CharacterLiteral

def test_java__CharacterLiteral___init__():
    assert java__CharacterLiteral.__init__(java__CharacterLiteral(''), '') == None

from python_code import java__Expression
from python_code import java__InfixExpression

def test_java__InfixExpression___init__():
    assert java__InfixExpression.__init__(java__InfixExpression('', java__InfixExpression=java__Expression(), java__InfixExpression188=java__Expression(), java__InfixExpression191=set()), '', java__InfixExpression=java__Expression(), java__InfixExpression188=java__Expression(), java__InfixExpression191=set()) == None

from python_code import java__Manifest
from python_code import java__ManifestEntry

def test_java__ManifestEntry___init__():
    assert java__ManifestEntry.__init__(java__ManifestEntry('', java__ManifestEntry=java__Manifest(), java__ManifestEntry211=set()), '', java__ManifestEntry=java__Manifest(), java__ManifestEntry211=set()) == None

from python_code import java__MethodRef
from python_code import java__MethodRefParameter
from python_code import java__TypeAccess

def test_java__MethodRefParameter___init__():
    assert java__MethodRefParameter.__init__(java__MethodRefParameter('', False, java__MethodRefParameter=java__MethodRef(), java__MethodRefParameter233=java__TypeAccess()), '', False, java__MethodRefParameter=java__MethodRef(), java__MethodRefParameter233=java__TypeAccess()) == None
