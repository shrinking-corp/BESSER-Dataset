from python_code import yya_NamedElement

def test_yya_NamedElement___init__():
    assert yya_NamedElement.__init__(yya_NamedElement('\x00', yya_NamedElement=set()), '', yya_NamedElement=set()) == None

