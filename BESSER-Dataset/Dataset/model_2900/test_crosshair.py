from python_code import forms_Entity

def test_forms_Entity___init__():
    assert forms_Entity.__init__(forms_Entity(False, forms_Entity=set()), False, forms_Entity=set()) == None


from python_code import forms_NamedElement

def test_forms_NamedElement___init__():
    assert forms_NamedElement.__init__(forms_NamedElement(''), '') == None

