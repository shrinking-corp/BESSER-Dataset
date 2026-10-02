from enum import Enum
from python_code import Color
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Color.BLUE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Color.BLUE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Color.RED, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Color.RED, 0)

def test_Enum___new___2():
    assert Enum.__new__(Color.RED, 'RED') == Color.RED

from python_code import genericsGoCrazy_MyClass

def test_genericsGoCrazy_MyClass___init__():
    assert genericsGoCrazy_MyClass.__init__(genericsGoCrazy_MyClass('', '', '', '', ''), '', '', '', '', '') == None

def test_genericsGoCrazy_MyClass_bar():
    assert genericsGoCrazy_MyClass.bar(genericsGoCrazy_MyClass('\x00', '\x00\x00', '', '', ''), '', '', '') == None
