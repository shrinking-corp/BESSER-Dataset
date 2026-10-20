from python_code import types_EnumerationType
from python_code import types_Enumerator

def test_types_Enumerator___init__():
    assert types_Enumerator.__init__(types_Enumerator('', Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()), '', Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()) == None


from python_code import types_RangeConstraint

def test_types_RangeConstraint___init__():
    assert types_RangeConstraint.__init__(types_RangeConstraint('', '\x00'), '\x00\x00', '') == None


from python_code import types_Type
from python_code import types_TypeParameter
from python_code import types_TypedElement

def test_types_Type___init__():
    assert types_Type.__init__(types_Type('\x00', types_Type=set(), types_Type6=types_TypedElement(), types_Type9=types_TypedElement(), types_Type18=types_TypeParameter()), '', types_Type=set(), types_Type6=types_TypedElement(), types_Type9=types_TypedElement(), types_Type18=types_TypeParameter()) == None

