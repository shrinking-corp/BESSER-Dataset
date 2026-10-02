from enum import Enum
from python_code import SWMLTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SWMLTypes.Email, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SWMLTypes.Email, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SWMLTypes.Float, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SWMLTypes.Email, 0)

def test_Enum___new___2():
    assert Enum.__new__(SWMLTypes.Float, 'Email') == SWMLTypes.Email

from python_code import swml_IndexPage

def test_swml_IndexPage___init__():
    assert swml_IndexPage.__init__(swml_IndexPage(0), 0) == None

from python_code import swml_HypertextLayer
from python_code import swml_Link
from python_code import swml_Page

def test_swml_Page___init__():
    assert swml_Page.__init__(swml_Page('', swml_Page=swml_HypertextLayer(), swml_Page16=set(), swml_Page21=swml_Link(), swml_Page7=swml_HypertextLayer()), '', swml_Page=swml_HypertextLayer(), swml_Page16=set(), swml_Page21=swml_Link(), swml_Page7=swml_HypertextLayer()) == None

from python_code import swml_ContentLayer
from python_code import swml_HypertextLayer
from python_code import swml_WebModel

def test_swml_WebModel___init__():
    assert swml_WebModel.__init__(swml_WebModel('', swml_WebModel=swml_HypertextLayer(), swml_WebModel2=swml_ContentLayer()), '', swml_WebModel=swml_HypertextLayer(), swml_WebModel2=swml_ContentLayer()) == None
