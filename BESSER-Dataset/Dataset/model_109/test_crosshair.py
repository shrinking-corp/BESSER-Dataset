from enum import Enum
from python_code import AssignmentOperatorKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AssignmentOperatorKind.plus_assign, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AssignmentOperatorKind.assign, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AssignmentOperatorKind.assign, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AssignmentOperatorKind.times_assign, 0)

def test_Enum___new___2():
    assert Enum.__new__(AssignmentOperatorKind.times_assign, 'assign') == AssignmentOperatorKind.assign

from enum import Enum
from python_code import InfixExpressionOperatorKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InfixExpressionOperatorKind.times, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InfixExpressionOperatorKind.plus, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InfixExpressionOperatorKind.less, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InfixExpressionOperatorKind.plus, '')

def test_Enum___new___2():
    assert Enum.__new__(InfixExpressionOperatorKind.or_, 'plus') == InfixExpressionOperatorKind.plus

from python_code import JDTAST_ArrayCreation
from python_code import JDTAST_ArrayType
from python_code import JDTAST_Type

def test_JDTAST_ArrayType___init__():
    assert JDTAST_ArrayType.__init__(JDTAST_ArrayType('', JDTAST_ArrayType=JDTAST_ArrayCreation(), JDTAST_ArrayType401=JDTAST_Type(), JDTAST_ArrayType404=JDTAST_Type()), '', JDTAST_ArrayType=JDTAST_ArrayCreation(), JDTAST_ArrayType401=JDTAST_Type(), JDTAST_ArrayType404=JDTAST_Type()) == None

from python_code import JDTAST_BooleanLiteral

def test_JDTAST_BooleanLiteral___init__():
    assert JDTAST_BooleanLiteral.__init__(JDTAST_BooleanLiteral(''), '') == None

from python_code import JDTAST_CharacterLiteral

def test_JDTAST_CharacterLiteral___init__():
    assert JDTAST_CharacterLiteral.__init__(JDTAST_CharacterLiteral('', '\x00'), '\x00\x00', '') == None

from python_code import JDTAST_ICompilationUnit
from python_code import JDTAST_IImportDeclaration

def test_JDTAST_IImportDeclaration___init__():
    assert JDTAST_IImportDeclaration.__init__(JDTAST_IImportDeclaration('', '\x00', JDTAST_IImportDeclaration=JDTAST_ICompilationUnit()), '\x00\x00', '', JDTAST_IImportDeclaration=JDTAST_ICompilationUnit()) == None

from python_code import JDTAST_IJavaElement

def test_JDTAST_IJavaElement___init__():
    assert JDTAST_IJavaElement.__init__(JDTAST_IJavaElement(''), '') == None

from python_code import JDTAST_IPackageFragment
from python_code import JDTAST_IPackageFragmentRoot
from python_code import JDTAST_PackageDeclaration

def test_JDTAST_IPackageFragment___init__():
    assert JDTAST_IPackageFragment.__init__(JDTAST_IPackageFragment('', JDTAST_IPackageFragment=set(), JDTAST_IPackageFragment16=set(), IPackageFragment=JDTAST_IPackageFragmentRoot(), packageFragments=JDTAST_IPackageFragmentRoot(), JDTAST_IPackageFragment106=JDTAST_PackageDeclaration()), '', JDTAST_IPackageFragment=set(), JDTAST_IPackageFragment16=set(), IPackageFragment=JDTAST_IPackageFragmentRoot(), packageFragments=JDTAST_IPackageFragmentRoot(), JDTAST_IPackageFragment106=JDTAST_PackageDeclaration()) == None

from python_code import JDTAST_Modifier

def test_JDTAST_Modifier___init__():
    assert JDTAST_Modifier.__init__(JDTAST_Modifier('', '', '', '', '', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '', '', '', '', '') == None

from python_code import JDTAST_NumberLiteral

def test_JDTAST_NumberLiteral___init__():
    assert JDTAST_NumberLiteral.__init__(JDTAST_NumberLiteral(''), '') == None

from python_code import JDTAST_PhysicalElement

def test_JDTAST_PhysicalElement___init__():
    assert JDTAST_PhysicalElement.__init__(JDTAST_PhysicalElement('', '\x00'), '\x00\x00', '') == None

from python_code import JDTAST_PrimitiveType

def test_JDTAST_PrimitiveType___init__():
    assert JDTAST_PrimitiveType.__init__(JDTAST_PrimitiveType(''), '') == None

from python_code import JDTAST_StringLiteral

def test_JDTAST_StringLiteral___init__():
    assert JDTAST_StringLiteral.__init__(JDTAST_StringLiteral('', '\x00'), '\x00\x00', '') == None

from python_code import JDTAST_Javadoc
from python_code import JDTAST_TagElement

def test_JDTAST_TagElement___init__():
    assert JDTAST_TagElement.__init__(JDTAST_TagElement('\x00\x00', '', JDTAST_TagElement=set(), JDTAST_TagElement182=JDTAST_Javadoc()), '', '', JDTAST_TagElement=set(), JDTAST_TagElement182=JDTAST_Javadoc()) == None

from python_code import JDTAST_TextElement

def test_JDTAST_TextElement___init__():
    assert JDTAST_TextElement.__init__(JDTAST_TextElement(''), '') == None

from python_code import JDTAST_Type
from python_code import JDTAST_TypeDeclaration

def test_JDTAST_TypeDeclaration___init__():
    assert JDTAST_TypeDeclaration.__init__(JDTAST_TypeDeclaration('', JDTAST_TypeDeclaration=JDTAST_Type(), JDTAST_TypeDeclaration175=set(), JDTAST_TypeDeclaration178=set()), '', JDTAST_TypeDeclaration=JDTAST_Type(), JDTAST_TypeDeclaration175=set(), JDTAST_TypeDeclaration178=set()) == None

from python_code import JDTAST_Type
from python_code import JDTAST_WildcardType

def test_JDTAST_WildcardType___init__():
    assert JDTAST_WildcardType.__init__(JDTAST_WildcardType('', JDTAST_WildcardType=JDTAST_Type()), '', JDTAST_WildcardType=JDTAST_Type()) == None

from enum import Enum
from python_code import Modifiers
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Modifiers.default, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Modifiers.enum, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Modifiers.enum, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Modifiers.bridge, 0)

def test_Enum___new___2():
    assert Enum.__new__(Modifiers.bridge, 'enum') == Modifiers.enum

from enum import Enum
from python_code import PostfixExpressionOperatorKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PostfixExpressionOperatorKind.decrement, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PostfixExpressionOperatorKind.decrement, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PostfixExpressionOperatorKind.increment, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PostfixExpressionOperatorKind.decrement, 0)

def test_Enum___new___2():
    assert Enum.__new__(PostfixExpressionOperatorKind.decrement, 'decrement') == PostfixExpressionOperatorKind.decrement

from enum import Enum
from python_code import PrefixExpressionOperatorKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PrefixExpressionOperatorKind.minus, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PrefixExpressionOperatorKind.plus, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PrefixExpressionOperatorKind.not_, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PrefixExpressionOperatorKind.plus, 0)

def test_Enum___new___2():
    assert Enum.__new__(PrefixExpressionOperatorKind.plus, 'not_') == PrefixExpressionOperatorKind.not_
