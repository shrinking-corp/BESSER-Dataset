from python_code import euml_NamedElement
from python_code import euml_Relations

def test_euml_NamedElement___init__():
    assert euml_NamedElement.__init__(euml_NamedElement('', euml_NamedElement=euml_Relations()), '', euml_NamedElement=euml_Relations()) == None

