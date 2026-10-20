from python_code import simpleUml_UMLModelElement

def test_simpleUml_UMLModelElement___init__():
    assert simpleUml_UMLModelElement.__init__(simpleUml_UMLModelElement('', '\x00'), '\x00\x00', '') == None

