from python_code import ecore_ENamedElement

def test_ecore_ENamedElement___init__():
    assert ecore_ENamedElement.__init__(ecore_ENamedElement(''), '') == None


from python_code import ecore_EStringToStringMapEntry

def test_ecore_EStringToStringMapEntry___init__():
    assert ecore_EStringToStringMapEntry.__init__(ecore_EStringToStringMapEntry('', '\x00'), '\x00\x00', '') == None

