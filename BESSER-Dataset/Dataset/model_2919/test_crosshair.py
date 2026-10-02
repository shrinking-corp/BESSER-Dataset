from enum import Enum
from python_code import Cardinality
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Cardinality.Many, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Cardinality.Many, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Cardinality.Many, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Cardinality.Many, 0)

def test_Enum___new___2():
    assert Enum.__new__(Cardinality.Many, 'Many') == Cardinality.Many

from enum import Enum
from python_code import DatabaseTechnologies
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DatabaseTechnologies.Oracle, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DatabaseTechnologies.Oracle, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DatabaseTechnologies.MySql, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DatabaseTechnologies.MySql, 0)

def test_Enum___new___2():
    assert Enum.__new__(DatabaseTechnologies.MySql, 'MySql') == DatabaseTechnologies.MySql

from enum import Enum
from python_code import DateDetails
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DateDetails.DateOnly, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DateDetails.DateOnly, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DateDetails.DateOnly, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DateDetails.TimeOnly, 0)

def test_Enum___new___2():
    assert Enum.__new__(DateDetails.TimeOnly, 'DateOnly') == DateDetails.DateOnly

from enum import Enum
from python_code import OrmTechnologies
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(OrmTechnologies.JPA, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(OrmTechnologies.Idiorm, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(OrmTechnologies.JPA, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(OrmTechnologies.JPA, 0)

def test_Enum___new___2():
    assert Enum.__new__(OrmTechnologies.JPA, 'JPA') == OrmTechnologies.JPA

from enum import Enum
from python_code import isHasChoices
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(isHasChoices.hasA, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(isHasChoices.hasA, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(isHasChoices.isA, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(isHasChoices.isA, 0)

def test_Enum___new___2():
    assert Enum.__new__(isHasChoices.isA, 'isA') == isHasChoices.isA

from python_code import persistence_AssociationWithContainment

def test_persistence_AssociationWithContainment___init__():
    assert persistence_AssociationWithContainment.__init__(persistence_AssociationWithContainment(True), False) == None

from python_code import persistence_AssociationWithoutContainment

def test_persistence_AssociationWithoutContainment___init__():
    assert persistence_AssociationWithoutContainment.__init__(persistence_AssociationWithoutContainment('', False), '', False) == None

from python_code import persistence_DataType
from python_code import persistence_DataTypeAttribute

def test_persistence_DataTypeAttribute___init__():
    assert persistence_DataTypeAttribute.__init__(persistence_DataTypeAttribute(False, False, False, persistence_DataTypeAttribute=persistence_DataType()), False, False, False, persistence_DataTypeAttribute=persistence_DataType()) == None

from python_code import persistence_DateAttribute

def test_persistence_DateAttribute___init__():
    assert persistence_DateAttribute.__init__(persistence_DateAttribute('', '\x00'), '\x00\x00', '') == None

from python_code import persistence_DatePathElement

def test_persistence_DatePathElement___init__():
    assert persistence_DatePathElement.__init__(persistence_DatePathElement(''), '') == None

from python_code import persistence_ResourceAttribute

def test_persistence_ResourceAttribute___init__():
    assert persistence_ResourceAttribute.__init__(persistence_ResourceAttribute('', False, 0, '', persistence_ResourceAttribute=set()), '', False, 0, '', persistence_ResourceAttribute=set()) == None

from python_code import persistence_StaticPathElement

def test_persistence_StaticPathElement___init__():
    assert persistence_StaticPathElement.__init__(persistence_StaticPathElement(''), '') == None

from python_code import persistence_UrlAttribute

def test_persistence_UrlAttribute___init__():
    assert persistence_UrlAttribute.__init__(persistence_UrlAttribute(''), '') == None
