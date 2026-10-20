from python_code import family_Family

def test_family_Family___init__():
    assert family_Family.__init__(family_Family('', '', '\x00\x00'), '', '', '') == None


from python_code import family_NamedElement

def test_family_NamedElement___init__():
    assert family_NamedElement.__init__(family_NamedElement(''), '') == None

