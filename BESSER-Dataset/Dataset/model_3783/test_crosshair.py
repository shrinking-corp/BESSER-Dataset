from python_code import test_NamedElement

def test_test_NamedElement___init__():
    assert test_NamedElement.__init__(test_NamedElement(''), '') == None


from python_code import test_Root

def test_test_Root___init__():
    assert test_Root.__init__(test_Root('\x00', test_Root=set()), '', test_Root=set()) == None

