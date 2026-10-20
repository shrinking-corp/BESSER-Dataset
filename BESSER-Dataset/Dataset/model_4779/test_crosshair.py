from python_code import types_ArrayTypeSpecifier

def test_types_ArrayTypeSpecifier___init__():
    assert types_ArrayTypeSpecifier.__init__(types_ArrayTypeSpecifier(0), 0) == None

def test_types_ArrayTypeSpecifier_getElementType():
    assert types_ArrayTypeSpecifier.getElementType(types_ArrayTypeSpecifier(0)) == None


from python_code import types_ComplexType

def test_types_ComplexType___init__():
    assert types_ComplexType.__init__(types_ComplexType(types_ComplexType=set()), types_ComplexType=set()) == None

def test_types_ComplexType_getAllFeatures():
    assert types_ComplexType.getAllFeatures(types_ComplexType(types_ComplexType=set())) == None


from python_code import types_Domain

def test_types_Domain___init__():
    assert types_Domain.__init__(types_Domain(''), '') == None


from python_code import types_EnumerationType
from python_code import types_Enumerator

def test_types_Enumerator___init__():
    assert types_Enumerator.__init__(types_Enumerator(0, Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()), 0, Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()) == None


from python_code import types_Event

def test_types_Event___init__():
    assert types_Event.__init__(types_Event(''), '') == None


from python_code import types_AnnotationType
from python_code import types_Expression
from python_code import types_Property

def test_types_Property___init__():
    assert types_Property.__init__(types_Property(False, False, types_Property=types_Expression(), types_Property38=types_AnnotationType()), False, False, types_Property=types_Expression(), types_Property38=types_AnnotationType()) == None


from python_code import types_Type
from python_code import types_TypeParameter
from python_code import types_TypeSpecifier
from python_code import types_TypedElement

def test_types_Type___init__():
    assert types_Type.__init__(types_Type(False, False, types_Type9=types_TypedElement(), types_Type=set(), types_Type15=types_TypeSpecifier(), types_Type24=types_TypeParameter()), False, False, types_Type9=types_TypedElement(), types_Type=set(), types_Type15=types_TypeSpecifier(), types_Type24=types_TypeParameter()) == None

def test_types_Type_getOriginType():
    assert types_Type.getOriginType(types_Type(False, False, types_Type9=types_TypedElement(), types_Type=set(), types_Type15=types_TypeSpecifier(), types_Type24=types_TypeParameter())) == None

