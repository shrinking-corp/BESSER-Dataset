from python_code import ube_Entity

def test_ube_Entity___init__():
    assert ube_Entity.__init__(ube_Entity(False, ube_Entity=set()), False, ube_Entity=set()) == None


from python_code import ube_NamedElement

def test_ube_NamedElement___init__():
    assert ube_NamedElement.__init__(ube_NamedElement(''), '') == None

