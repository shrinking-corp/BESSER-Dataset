from python_code import simpleuml_UMLModelElement

def test_simpleuml_UMLModelElement___init__():
    assert simpleuml_UMLModelElement.__init__(simpleuml_UMLModelElement('', '\x00'), '\x00\x00', '') == None

