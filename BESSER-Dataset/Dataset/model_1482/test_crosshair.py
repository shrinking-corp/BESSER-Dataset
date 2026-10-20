from python_code import transformr_Expression

def test_transformr_Expression___init__():
    assert transformr_Expression.__init__(transformr_Expression('', transformr_Expression=set()), '', transformr_Expression=set()) == None


from python_code import transformr_NamedElement

def test_transformr_NamedElement___init__():
    assert transformr_NamedElement.__init__(transformr_NamedElement(''), '') == None


from python_code import transformr_TypedElement

def test_transformr_TypedElement___init__():
    assert transformr_TypedElement.__init__(transformr_TypedElement(''), '') == None

