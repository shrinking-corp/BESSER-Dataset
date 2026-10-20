from python_code import simpleuml_ModelElement
from python_code import simpleuml_UMLPackage

def test_simpleuml_ModelElement___init__():
    assert simpleuml_ModelElement.__init__(simpleuml_ModelElement('', simpleuml_ModelElement=simpleuml_UMLPackage()), '', simpleuml_ModelElement=simpleuml_UMLPackage()) == None

