from python_code import Elements_IdentifiedElement

def test_Elements_IdentifiedElement___init__():
    assert Elements_IdentifiedElement.__init__(Elements_IdentifiedElement(''), '') == None


from python_code import Elements_Root

def test_Elements_Root___init__():
    assert Elements_Root.__init__(Elements_Root('\x00', Elements_Root=set()), '', Elements_Root=set()) == None

