from enum import Enum
from python_code import FIELD_FORMAT
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FIELD_FORMAT.XSD, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FIELD_FORMAT.XSD, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FIELD_FORMAT.AU, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FIELD_FORMAT.XSD, 0)

def test_Enum___new___2():
    assert Enum.__new__(FIELD_FORMAT.AU, 'AU') == FIELD_FORMAT.AU

from enum import Enum
from python_code import UNIT
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(UNIT.AMP, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(UNIT.KG, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(UNIT.KG, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(UNIT.KG, 0)

def test_Enum___new___2():
    assert Enum.__new__(UNIT.KG, 'KG') == UNIT.KG

from python_code import cjsidl_EObject
from python_code import cjsidl_arrayDef
from python_code import cjsidl_recordDef
from python_code import cjsidl_scopedType
from python_code import cjsidl_typeDef

def test_cjsidl_arrayDef___init__():
    assert cjsidl_arrayDef.__init__(cjsidl_arrayDef('\x00\x00', '', '', '', cjsidl_arrayDef=cjsidl_typeDef(), cjsidl_arrayDef425=cjsidl_recordDef(), cjsidl_arrayDef460=cjsidl_EObject(), cjsidl_arrayDef463=cjsidl_scopedType()), '', '', '', '', cjsidl_arrayDef=cjsidl_typeDef(), cjsidl_arrayDef425=cjsidl_recordDef(), cjsidl_arrayDef460=cjsidl_EObject(), cjsidl_arrayDef463=cjsidl_scopedType()) == None

from python_code import cjsidl_bitfieldDef
from python_code import cjsidl_recordDef
from python_code import cjsidl_typeDef

def test_cjsidl_bitfieldDef___init__():
    assert cjsidl_bitfieldDef.__init__(cjsidl_bitfieldDef('', '', '', '', cjsidl_bitfieldDef=cjsidl_typeDef(), cjsidl_bitfieldDef434=cjsidl_recordDef(), cjsidl_bitfieldDef354=set()), '', '', '', '', cjsidl_bitfieldDef=cjsidl_typeDef(), cjsidl_bitfieldDef434=cjsidl_recordDef(), cjsidl_bitfieldDef354=set()) == None

from python_code import cjsidl_internalTransition

def test_cjsidl_internalTransition___init__():
    assert cjsidl_internalTransition.__init__(cjsidl_internalTransition(''), '') == None

from python_code import cjsidl_valueSpec

def test_cjsidl_valueSpec___init__():
    assert cjsidl_valueSpec.__init__(cjsidl_valueSpec('', '', '\x00\x00'), '', '', '') == None
