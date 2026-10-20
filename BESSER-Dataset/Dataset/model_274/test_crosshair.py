from python_code import ecore_EAttribute

def test_ecore_EAttribute___init__():
    assert ecore_EAttribute.__init__(ecore_EAttribute(True), False) == None


from python_code import ecore_EEnum
from python_code import ecore_EEnumLiteral

def test_ecore_EEnumLiteral___init__():
    assert ecore_EEnumLiteral.__init__(ecore_EEnumLiteral('', EEnumLiteral=ecore_EEnum(), eLiterals=ecore_EEnum()), '', EEnumLiteral=ecore_EEnum(), eLiterals=ecore_EEnum()) == None


from python_code import ecore_ENamedElement

def test_ecore_ENamedElement___init__():
    assert ecore_ENamedElement.__init__(ecore_ENamedElement(''), '') == None

