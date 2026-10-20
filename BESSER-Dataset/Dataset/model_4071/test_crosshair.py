from python_code import uml_UMLModelElement

def test_uml_UMLModelElement___init__():
    assert uml_UMLModelElement.__init__(uml_UMLModelElement('', '\x00'), '\x00\x00', '') == None

