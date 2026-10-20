from python_code import petrinet_Arc

def test_petrinet_Arc___init__():
    assert petrinet_Arc.__init__(petrinet_Arc(0), 0) == None


from python_code import petrinet_NamedElement

def test_petrinet_NamedElement___init__():
    assert petrinet_NamedElement.__init__(petrinet_NamedElement(''), '') == None

