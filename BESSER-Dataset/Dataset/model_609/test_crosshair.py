from enum import Enum
from python_code import Behavior
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Behavior.RESTRICT, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Behavior.RESTRICT, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Behavior.CASCADE, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Behavior.CASCADE, 0)

def test_Enum___new___2():
    assert Enum.__new__(Behavior.CASCADE, 'CASCADE') == Behavior.CASCADE

from enum import Enum
from python_code import Charset
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Charset.CP852, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Charset.BIG5, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Charset.ASCII, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Charset.BIG5, 0)

def test_Enum___new___2():
    assert Enum.__new__(Charset.BIG5, 'DEC8') == Charset.DEC8

from enum import Enum
from python_code import ColumnType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ColumnType.CHAR, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ColumnType.REAL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ColumnType.REAL, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ColumnType.REAL, 0)

def test_Enum___new___2():
    assert Enum.__new__(ColumnType.BIT, 'BIT') == ColumnType.BIT

from enum import Enum
from python_code import FormMethod
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FormMethod.POST, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FormMethod.POST, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FormMethod.GET, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FormMethod.GET, 0)

def test_Enum___new___2():
    assert Enum.__new__(FormMethod.GET, 'GET') == FormMethod.GET

from enum import Enum
from python_code import InputType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InputType.TEXT, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InputType.TEXT, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InputType.TEXT, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InputType.TEXT, 0)

def test_Enum___new___2():
    assert Enum.__new__(InputType.TEXT, 'TEXT') == InputType.TEXT

from python_code import webapp_Check
from python_code import webapp_Constraint

def test_webapp_Check___init__():
    assert webapp_Check.__init__(webapp_Check('', webapp_Check=webapp_Constraint()), '', webapp_Check=webapp_Constraint()) == None

from python_code import webapp_Form

def test_webapp_Form___init__():
    assert webapp_Form.__init__(webapp_Form('', webapp_Form=set()), '', webapp_Form=set()) == None

from python_code import webapp_ForeignKey
from python_code import webapp_OnDelete

def test_webapp_OnDelete___init__():
    assert webapp_OnDelete.__init__(webapp_OnDelete('', webapp_OnDelete=webapp_ForeignKey()), '', webapp_OnDelete=webapp_ForeignKey()) == None

from python_code import webapp_ForeignKey
from python_code import webapp_OnUpdate

def test_webapp_OnUpdate___init__():
    assert webapp_OnUpdate.__init__(webapp_OnUpdate('', webapp_OnUpdate=webapp_ForeignKey()), '', webapp_OnUpdate=webapp_ForeignKey()) == None

from python_code import webapp_Text

def test_webapp_Text___init__():
    assert webapp_Text.__init__(webapp_Text(''), '') == None
