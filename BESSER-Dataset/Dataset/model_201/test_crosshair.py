from python_code import ecore_ENamedElement

def test_ecore_ENamedElement___init__():
    assert ecore_ENamedElement.__init__(ecore_ENamedElement(''), '') == None


from python_code import ecore_hello
from python_code import ecore_prueba

def test_ecore_prueba___init__():
    assert ecore_prueba.__init__(ecore_prueba(0.0, '', 0, '', 0.0, '', 0, '', ref2=set(), prueba=ecore_hello()), 0.0, '\x00', 0, '', 0.0, '', 0, '', ref2=set(), prueba=ecore_hello()) == None

