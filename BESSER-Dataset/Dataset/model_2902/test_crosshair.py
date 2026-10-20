from python_code import myDSL_Entity

def test_myDSL_Entity___init__():
    assert myDSL_Entity.__init__(myDSL_Entity(False, myDSL_Entity=set()), False, myDSL_Entity=set()) == None


from python_code import myDSL_NamedElement

def test_myDSL_NamedElement___init__():
    assert myDSL_NamedElement.__init__(myDSL_NamedElement(''), '') == None

