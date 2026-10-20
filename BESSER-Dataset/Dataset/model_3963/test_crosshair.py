from python_code import umlClass_NamedElement

def test_umlClass_NamedElement___init__():
    assert umlClass_NamedElement.__init__(umlClass_NamedElement('', '\x00'), '\x00\x00', '') == None


from python_code import umlClass_StructuralFeature

def test_umlClass_StructuralFeature___init__():
    assert umlClass_StructuralFeature.__init__(umlClass_StructuralFeature(''), '') == None

