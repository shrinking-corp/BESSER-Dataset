from enum import Enum
from python_code import COREFeatureRelationshipType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(COREFeatureRelationshipType.OR, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(COREFeatureRelationshipType.OR, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(COREFeatureRelationshipType.OR, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(COREFeatureRelationshipType.OR, 0)

def test_Enum___new___2():
    assert Enum.__new__(COREFeatureRelationshipType.OR, 'OR') == COREFeatureRelationshipType.OR

from enum import Enum
from python_code import COREPartialityType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(COREPartialityType.none, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(COREPartialityType.none, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(COREPartialityType.none, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(COREPartialityType.none, 0)

def test_Enum___new___2():
    assert Enum.__new__(COREPartialityType.none, 'none') == COREPartialityType.none

from enum import Enum
from python_code import COREVisibilityType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(COREVisibilityType.concern, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(COREVisibilityType.concern, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(COREVisibilityType.public, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(COREVisibilityType.public, 0)

def test_Enum___new___2():
    assert Enum.__new__(COREVisibilityType.public, 'public') == COREVisibilityType.public

from python_code import core_COREInterface
from python_code import core_COREModel
from python_code import core_COREModelElement

def test_core_COREModelElement___init__():
    assert core_COREModelElement.__init__(core_COREModelElement('', '\x00', core_COREModelElement=core_COREModel(), core_COREModelElement42=core_COREInterface(), core_COREModelElement45=core_COREInterface()), '\x00\x00', '', core_COREModelElement=core_COREModel(), core_COREModelElement42=core_COREInterface(), core_COREModelElement45=core_COREInterface()) == None

from python_code import core_CORENamedElement

def test_core_CORENamedElement___init__():
    assert core_CORENamedElement.__init__(core_CORENamedElement(''), '') == None

from python_code import core_LayoutElement
from python_code import core_LayoutMap

def test_core_LayoutElement___init__():
    assert core_LayoutElement.__init__(core_LayoutElement(0.0, 0.0, core_LayoutElement=core_LayoutMap()), 0.0, 0.0, core_LayoutElement=core_LayoutMap()) == None
