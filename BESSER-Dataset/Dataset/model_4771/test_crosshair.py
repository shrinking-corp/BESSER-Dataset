from python_code import eol_types_AnyType
from python_code import eol_types_MapType

def test_eol_types_AnyType___init__():
    assert eol_types_AnyType.__init__(eol_types_AnyType(False, eol_types_AnyType=set(), eol_types_AnyType2=eol_types_MapType(), eol_types_AnyType5=eol_types_MapType()), False, eol_types_AnyType=set(), eol_types_AnyType2=eol_types_MapType(), eol_types_AnyType5=eol_types_MapType()) == None


from python_code import eol_types_ModelElementType

def test_eol_types_ModelElementType___init__():
    assert eol_types_ModelElementType.__init__(eol_types_ModelElementType('', '\x00'), '\x00\x00', '') == None


from python_code import eol_types_ModelType

def test_eol_types_ModelType___init__():
    assert eol_types_ModelType.__init__(eol_types_ModelType(''), '') == None


from python_code import eol_types_NativeType

def test_eol_types_NativeType___init__():
    assert eol_types_NativeType.__init__(eol_types_NativeType(''), '') == None

