from python_code import Ecore_ENamedElement

def test_Ecore_ENamedElement___init__():
    assert Ecore_ENamedElement.__init__(Ecore_ENamedElement(''), '') == None


from python_code import Ecore_EStringToStringMapEntry

def test_Ecore_EStringToStringMapEntry___init__():
    assert Ecore_EStringToStringMapEntry.__init__(Ecore_EStringToStringMapEntry('', '\x00'), '\x00\x00', '') == None

