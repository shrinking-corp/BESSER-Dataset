from enum import Enum
from python_code import COREFeatureRelationshipType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(COREFeatureRelationshipType.XOR, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(COREFeatureRelationshipType.OR, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(COREFeatureRelationshipType.OR, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(COREFeatureRelationshipType.OR, 0)

def test_Enum___new___2():
    assert Enum.__new__(COREFeatureRelationshipType.OR, 'OR') == COREFeatureRelationshipType.OR

from python_code import core_COREFeatureModel

def test_core_COREFeatureModel___init__():
    assert core_COREFeatureModel.__init__(core_COREFeatureModel()) == None

def test_core_COREFeatureModel_getLocalRoot():
    assert core_COREFeatureModel.getLocalRoot(core_COREFeatureModel()) == None

def test_core_COREFeatureModel_getGlobalRoot():
    assert core_COREFeatureModel.getGlobalRoot(core_COREFeatureModel()) == None

from python_code import core_CORENamedElement

def test_core_CORENamedElement___init__():
    assert core_CORENamedElement.__init__(core_CORENamedElement(''), '') == None
