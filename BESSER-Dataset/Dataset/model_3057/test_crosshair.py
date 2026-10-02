from enum import Enum
from python_code import DataTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DataTypes.Long, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DataTypes.Long, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DataTypes.Long, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DataTypes.Long, 0)

def test_Enum___new___2():
    assert Enum.__new__(DataTypes.Long, 'Long') == DataTypes.Long

from enum import Enum
from python_code import InternalDSLType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InternalDSLType.NestedFunctions, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InternalDSLType.NestedFunctions, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InternalDSLType.NestedFunctions, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InternalDSLType.NestedFunctions, 0)

def test_Enum___new___2():
    assert Enum.__new__(InternalDSLType.NestedFunctions, 'NestedFunctions') == InternalDSLType.NestedFunctions
