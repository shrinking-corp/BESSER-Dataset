from python_code import hbmxml_Entity

def test_hbmxml_Entity___init__():
    assert hbmxml_Entity.__init__(hbmxml_Entity(False, hbmxml_Entity=set()), False, hbmxml_Entity=set()) == None


from python_code import hbmxml_NamedElement

def test_hbmxml_NamedElement___init__():
    assert hbmxml_NamedElement.__init__(hbmxml_NamedElement(''), '') == None

