from python_code import petriNet_Place

def test_petriNet_Place___init__():
    assert petriNet_Place.__init__(petriNet_Place(0), 0) == None


from python_code import petriNet_Transition

def test_petriNet_Transition___init__():
    assert petriNet_Transition.__init__(petriNet_Transition(0, 0), 0, 0) == None

