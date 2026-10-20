from python_code import sgraph_Choice

def test_sgraph_Choice___init__():
    assert sgraph_Choice.__init__(sgraph_Choice(''), '') == None


from python_code import sgraph_Entry

def test_sgraph_Entry___init__():
    assert sgraph_Entry.__init__(sgraph_Entry(''), '') == None


from python_code import sgraph_ScopedElement

def test_sgraph_ScopedElement___init__():
    assert sgraph_ScopedElement.__init__(sgraph_ScopedElement('', sgraph_ScopedElement=set()), '', sgraph_ScopedElement=set()) == None


from python_code import sgraph_SpecificationElement

def test_sgraph_SpecificationElement___init__():
    assert sgraph_SpecificationElement.__init__(sgraph_SpecificationElement(''), '') == None

