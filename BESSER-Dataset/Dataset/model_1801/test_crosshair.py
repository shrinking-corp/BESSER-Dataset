from enum import Enum
from python_code import LevelKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LevelKind.GREEN, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LevelKind.RED, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LevelKind.RED, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LevelKind.RED, 0)

def test_Enum___new___2():
    assert Enum.__new__(LevelKind.RED, 'RED') == LevelKind.RED

from enum import Enum
from python_code import RangeKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RangeKind.CAP, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RangeKind.CAP, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RangeKind.CAP, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RangeKind.CAP, 0)

def test_Enum___new___2():
    assert Enum.__new__(RangeKind.CAP, 'CAP') == RangeKind.CAP

from enum import Enum
from python_code import RedundancyType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RedundancyType.n, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RedundancyType.n, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RedundancyType.n, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RedundancyType.n, 0)

def test_Enum___new___2():
    assert Enum.__new__(RedundancyType.n, 'n') == RedundancyType.n

from enum import Enum
from python_code import StateType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(StateType.ACTIVE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(StateType.IDLE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(StateType.IDLE, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(StateType.IDLE, 0)

def test_Enum___new___2():
    assert Enum.__new__(StateType.IDLE, 'IDLE') == StateType.IDLE

from python_code import library_LastEvaluationExpressionResult

def test_library_LastEvaluationExpressionResult___init__():
    assert library_LastEvaluationExpressionResult.__init__(library_LastEvaluationExpressionResult(''), '') == None

from python_code import library_ProductInfo
from python_code import library_Vendor

def test_library_ProductInfo___init__():
    assert library_ProductInfo.__init__(library_ProductInfo('', '', '', '', '', '', library_ProductInfo=set(), library_ProductInfo121=set(), library_ProductInfo124=set(), library_ProductInfo133=library_Vendor()), '', '', '', '', '\x00', '', library_ProductInfo=set(), library_ProductInfo121=set(), library_ProductInfo124=set(), library_ProductInfo133=library_Vendor()) == None
