from enum import Enum
from python_code import FontOption
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FontOption.BOLD, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FontOption.BOLD, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FontOption.BOLD, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FontOption.BOLD, 0)

def test_Enum___new___2():
    assert Enum.__new__(FontOption.BOLD, 'BOLD') == FontOption.BOLD

from python_code import Styling_BooleanParameter

def test_Styling_BooleanParameter___init__():
    assert Styling_BooleanParameter.__init__(Styling_BooleanParameter(True), False) == None

from python_code import Styling_ConstantPattern

def test_Styling_ConstantPattern___init__():
    assert Styling_ConstantPattern.__init__(Styling_ConstantPattern(''), '') == None

from python_code import Styling_IntParameter

def test_Styling_IntParameter___init__():
    assert Styling_IntParameter.__init__(Styling_IntParameter(0), 0) == None

from python_code import Styling_ModelPattern

def test_Styling_ModelPattern___init__():
    assert Styling_ModelPattern.__init__(Styling_ModelPattern(''), '') == None

from python_code import Styling_OperationPattern

def test_Styling_OperationPattern___init__():
    assert Styling_OperationPattern.__init__(Styling_OperationPattern('\x00', Styling_OperationPattern=set()), '', Styling_OperationPattern=set()) == None

from python_code import Styling_StringParameter

def test_Styling_StringParameter___init__():
    assert Styling_StringParameter.__init__(Styling_StringParameter(''), '') == None
