from enum import Enum
from python_code import ActionVerb
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ActionVerb.add, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ActionVerb.add, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ActionVerb.edit, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ActionVerb.add, 0)

def test_Enum___new___2():
    assert Enum.__new__(ActionVerb.add, 'add') == ActionVerb.add

from enum import Enum
from python_code import GestureKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GestureKind.tap, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GestureKind.tap, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GestureKind.tap, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GestureKind.tap, 0)

def test_Enum___new___2():
    assert Enum.__new__(GestureKind.tap, 'tap') == GestureKind.tap

from enum import Enum
from python_code import RESTVerb
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RESTVerb.PUT, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RESTVerb.PUT, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RESTVerb.PUT, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RESTVerb.PUT, 0)

def test_Enum___new___2():
    assert Enum.__new__(RESTVerb.GET, 'PUT') == RESTVerb.PUT

from enum import Enum
from python_code import ScreenKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ScreenKind.DefaultList, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ScreenKind.DefaultList, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ScreenKind.DefaultList, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ScreenKind.DefaultList, 0)

def test_Enum___new___2():
    assert Enum.__new__(ScreenKind.DefaultList, 'DefaultList') == ScreenKind.DefaultList

from enum import Enum
from python_code import UIActionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(UIActionKind.navigate, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(UIActionKind.navigate, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(UIActionKind.navigate, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(UIActionKind.delete, 0)

def test_Enum___new___2():
    assert Enum.__new__(UIActionKind.delete, 'delete') == UIActionKind.delete

from python_code import applauseDsl_AbsoluteRESTURL
from python_code import applauseDsl_DataSource
from python_code import applauseDsl_UrlFragment

def test_applauseDsl_AbsoluteRESTURL___init__():
    assert applauseDsl_AbsoluteRESTURL.__init__(applauseDsl_AbsoluteRESTURL(0, applauseDsl_AbsoluteRESTURL=applauseDsl_DataSource(), applauseDsl_AbsoluteRESTURL32=applauseDsl_UrlFragment()), 0, applauseDsl_AbsoluteRESTURL=applauseDsl_DataSource(), applauseDsl_AbsoluteRESTURL32=applauseDsl_UrlFragment()) == None

from python_code import applauseDsl_Model
from python_code import applauseDsl_NamedElement

def test_applauseDsl_NamedElement___init__():
    assert applauseDsl_NamedElement.__init__(applauseDsl_NamedElement('', applauseDsl_NamedElement=applauseDsl_Model()), '', applauseDsl_NamedElement=applauseDsl_Model()) == None

from python_code import applauseDsl_StringLiteral

def test_applauseDsl_StringLiteral___init__():
    assert applauseDsl_StringLiteral.__init__(applauseDsl_StringLiteral(''), '') == None

from python_code import applauseDsl_DataType
from python_code import applauseDsl_TypeMapping

def test_applauseDsl_TypeMapping___init__():
    assert applauseDsl_TypeMapping.__init__(applauseDsl_TypeMapping('', applauseDsl_TypeMapping=applauseDsl_DataType()), '', applauseDsl_TypeMapping=applauseDsl_DataType()) == None

from python_code import applauseDsl_ListItemCellDeclaration
from python_code import applauseDsl_UIComponentDeclaration
from python_code import applauseDsl_UIComponentMemberCall
from python_code import applauseDsl_UIComponentMemberDeclaration
from python_code import applauseDsl_UIComponentOrDataType

def test_applauseDsl_UIComponentMemberDeclaration___init__():
    assert applauseDsl_UIComponentMemberDeclaration.__init__(applauseDsl_UIComponentMemberDeclaration('', applauseDsl_UIComponentMemberDeclaration89=applauseDsl_UIComponentMemberCall(), applauseDsl_UIComponentMemberDeclaration92=applauseDsl_UIComponentMemberCall(), applauseDsl_UIComponentMemberDeclaration=applauseDsl_ListItemCellDeclaration(), applauseDsl_UIComponentMemberDeclaration71=applauseDsl_UIComponentDeclaration(), applauseDsl_UIComponentMemberDeclaration73=applauseDsl_UIComponentOrDataType()), '', applauseDsl_UIComponentMemberDeclaration89=applauseDsl_UIComponentMemberCall(), applauseDsl_UIComponentMemberDeclaration92=applauseDsl_UIComponentMemberCall(), applauseDsl_UIComponentMemberDeclaration=applauseDsl_ListItemCellDeclaration(), applauseDsl_UIComponentMemberDeclaration71=applauseDsl_UIComponentDeclaration(), applauseDsl_UIComponentMemberDeclaration73=applauseDsl_UIComponentOrDataType()) == None

from python_code import applauseDsl_UrlPathFragment

def test_applauseDsl_UrlPathFragment___init__():
    assert applauseDsl_UrlPathFragment.__init__(applauseDsl_UrlPathFragment(''), '') == None
