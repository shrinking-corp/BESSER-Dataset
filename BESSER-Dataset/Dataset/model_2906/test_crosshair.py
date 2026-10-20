from python_code import bombXML_Entity

def test_bombXML_Entity___init__():
    assert bombXML_Entity.__init__(bombXML_Entity(False, bombXML_Entity=set()), False, bombXML_Entity=set()) == None


from python_code import bombXML_NamedElement

def test_bombXML_NamedElement___init__():
    assert bombXML_NamedElement.__init__(bombXML_NamedElement(''), '') == None

