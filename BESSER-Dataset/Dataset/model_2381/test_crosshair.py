from enum import Enum
from python_code import ActionGranularityType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ActionGranularityType.ROW, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ActionGranularityType.ROW, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ActionGranularityType.ROW, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ActionGranularityType.ROW, 0)

def test_Enum___new___2():
    assert Enum.__new__(ActionGranularityType.ROW, 'ROW') == ActionGranularityType.ROW

from enum import Enum
from python_code import ActionTimeType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ActionTimeType.AFTER, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ActionTimeType.AFTER, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ActionTimeType.AFTER, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ActionTimeType.AFTER, 0)

def test_Enum___new___2():
    assert Enum.__new__(ActionTimeType.AFTER, 'AFTER') == ActionTimeType.AFTER

from enum import Enum
from python_code import ReferentialActionType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ReferentialActionType.RESTRICT, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ReferentialActionType.CASCADE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ReferentialActionType.CASCADE, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ReferentialActionType.CASCADE, 0)

def test_Enum___new___2():
    assert Enum.__new__(ReferentialActionType.CASCADE, 'CASCADE') == ReferentialActionType.CASCADE

from python_code import relational_Assertion
from python_code import relational_Schema

def test_relational_Assertion___init__():
    assert relational_Assertion.__init__(relational_Assertion('', assertions=relational_Schema(), Assertion=relational_Schema()), '', assertions=relational_Schema(), Assertion=relational_Schema()) == None

from python_code import relational_ENamedElement

def test_relational_ENamedElement___init__():
    assert relational_ENamedElement.__init__(relational_ENamedElement(''), '') == None

from python_code import relational_Schema
from python_code import relational_Table
from python_code import relational_Trigger

def test_relational_Trigger___init__():
    assert relational_Trigger.__init__(relational_Trigger('', '', '', '', '', '', False, False, False, '', '', Trigger22=relational_Table(), Trigger=relational_Schema(), triggers=relational_Schema(), triggers13=relational_Table(), triggersConstrainted=set(), Trigger20=relational_Table()), '', '', '', '', '', '', True, False, False, '', '', Trigger22=relational_Table(), Trigger=relational_Schema(), triggers=relational_Schema(), triggers13=relational_Table(), triggersConstrainted=set(), Trigger20=relational_Table()) == None
