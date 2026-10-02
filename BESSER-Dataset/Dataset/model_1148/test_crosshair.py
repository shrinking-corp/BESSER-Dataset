from enum import Enum
from python_code import AssignTypeDatatype
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AssignTypeDatatype.replace, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AssignTypeDatatype.delete, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AssignTypeDatatype.delete, 0, 0, '') == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AssignTypeDatatype.replace, '')

def test_Enum___new___2():
    assert Enum.__new__(AssignTypeDatatype.replace, 'delete') == AssignTypeDatatype.delete

from enum import Enum
from python_code import BindingDatatype
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(BindingDatatype.late, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(BindingDatatype.late, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(BindingDatatype.early, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(BindingDatatype.late, 0)

def test_Enum___new___2():
    assert Enum.__new__(BindingDatatype.late, 'late') == BindingDatatype.late

from enum import Enum
from python_code import BooleanDatatype
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(BooleanDatatype.false, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(BooleanDatatype.false, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(BooleanDatatype.true, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(BooleanDatatype.true, 0)

def test_Enum___new___2():
    assert Enum.__new__(BooleanDatatype.true, 'true') == BooleanDatatype.true

from enum import Enum
from python_code import ExmodeDatatype
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ExmodeDatatype.lax, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ExmodeDatatype.lax, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ExmodeDatatype.lax, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ExmodeDatatype.lax, 0)

def test_Enum___new___2():
    assert Enum.__new__(ExmodeDatatype.lax, 'lax') == ExmodeDatatype.lax

from enum import Enum
from python_code import HistoryTypeDatatype
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(HistoryTypeDatatype.deep, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(HistoryTypeDatatype.deep, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(HistoryTypeDatatype.deep, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(HistoryTypeDatatype.deep, 0)

def test_Enum___new___2():
    assert Enum.__new__(HistoryTypeDatatype.deep, 'deep') == HistoryTypeDatatype.deep

from enum import Enum
from python_code import TransitionTypeDatatype
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TransitionTypeDatatype.external, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TransitionTypeDatatype.external, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TransitionTypeDatatype.internal, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TransitionTypeDatatype.external, 0)

def test_Enum___new___2():
    assert Enum.__new__(TransitionTypeDatatype.external, 'external') == TransitionTypeDatatype.external
