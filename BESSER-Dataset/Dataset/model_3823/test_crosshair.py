from python_code import types_ArrayTypeSpecifier

def test_types_ArrayTypeSpecifier___init__():
    assert types_ArrayTypeSpecifier.__init__(types_ArrayTypeSpecifier(0), 0) == None

def test_types_ArrayTypeSpecifier_getElementType():
    assert types_ArrayTypeSpecifier.getElementType(types_ArrayTypeSpecifier(0)) == None


from python_code import types_Domain
from python_code import types_Package

def test_types_Domain___init__():
    assert types_Domain.__init__(types_Domain('', types_Domain=types_Package()), '', types_Domain=types_Package()) == None


from python_code import types_EnumerationType
from python_code import types_Enumerator

def test_types_Enumerator___init__():
    assert types_Enumerator.__init__(types_Enumerator(0, Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()), 0, Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()) == None


from python_code import types_Event

def test_types_Event___init__():
    assert types_Event.__init__(types_Event(''), '') == None


from python_code import types_Package
from python_code import types_PackageMember

def test_types_PackageMember___init__():
    assert types_PackageMember.__init__(types_PackageMember('', types_PackageMember=types_Package()), '', types_PackageMember=types_Package()) == None


from python_code import types_Annotation
from python_code import types_Property

def test_types_Property___init__():
    assert types_Property.__init__(types_Property(False, False, False, types_Property=types_Annotation()), False, False, False, types_Property=types_Annotation()) == None


from python_code import types_RangeConstraint

def test_types_RangeConstraint___init__():
    assert types_RangeConstraint.__init__(types_RangeConstraint('', '\x00'), '\x00\x00', '') == None


from python_code import types_Type
from python_code import types_TypeParameter
from python_code import types_TypeSpecifier
from python_code import types_TypedElement

def test_types_Type___init__():
    assert types_Type.__init__(types_Type(False, False, types_Type10=types_TypedElement(), types_Type15=types_TypeSpecifier(), types_Type=set(), types_Type28=types_TypeParameter()), False, False, types_Type10=types_TypedElement(), types_Type15=types_TypeSpecifier(), types_Type=set(), types_Type28=types_TypeParameter()) == None

def test_types_Type_getOriginType():
    assert types_Type.getOriginType(types_Type(False, False, types_Type10=types_TypedElement(), types_Type15=types_TypeSpecifier(), types_Type=set(), types_Type28=types_TypeParameter())) == None

