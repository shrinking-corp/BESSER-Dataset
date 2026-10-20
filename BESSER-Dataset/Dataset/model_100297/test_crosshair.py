from python_code import PetriNet_Arc

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc('', '\x00'), '\x00\x00', '') == None


from python_code import PetriNet_Element

def test_PetriNet_Element___init__():
    assert PetriNet_Element.__init__(PetriNet_Element(''), '') == None

