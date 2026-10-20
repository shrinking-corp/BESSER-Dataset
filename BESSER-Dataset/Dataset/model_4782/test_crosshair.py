from python_code import types_Domain
from python_code import types_Package

def test_types_Domain___init__():
    assert types_Domain.__init__(types_Domain('', types_Domain=types_Package()), '', types_Domain=types_Package()) == None


from python_code import types_EnumerationType
from python_code import types_Enumerator

def test_types_Enumerator___init__():
    assert types_Enumerator.__init__(types_Enumerator('', Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()), '', Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()) == None


from python_code import types_Event

def test_types_Event___init__():
    assert types_Event.__init__(types_Event(''), '') == None


from python_code import types_Property

def test_types_Property___init__():
    assert types_Property.__init__(types_Property(False, False, False), False, False, False) == None


from python_code import types_RangeConstraint

def test_types_RangeConstraint___init__():
    assert types_RangeConstraint.__init__(types_RangeConstraint('', '\x00'), '\x00\x00', '') == None


from python_code import types_Type
from python_code import types_TypeParameter
from python_code import types_TypedElement

def test_types_Type___init__():
    assert types_Type.__init__(types_Type(False, types_Type=set(), types_Type7=types_TypedElement(), types_Type10=types_TypedElement(), types_Type20=types_TypeParameter()), False, types_Type=set(), types_Type7=types_TypedElement(), types_Type10=types_TypedElement(), types_Type20=types_TypeParameter()) == None

def test_types_Type_getOriginType():
    assert types_Type.getOriginType(types_Type(False, types_Type=set(), types_Type7=types_TypedElement(), types_Type10=types_TypedElement(), types_Type20=types_TypeParameter())) == None

