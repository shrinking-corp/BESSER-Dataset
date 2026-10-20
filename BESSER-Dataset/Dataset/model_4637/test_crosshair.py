from python_code import notation_GraphicalElement

def test_notation_GraphicalElement___init__():
    assert notation_GraphicalElement.__init__(notation_GraphicalElement(0, 0, 0, 0, '', ''), 0, 0, 0, 0, '\x00', '') == None


from python_code import notation_IdElement

def test_notation_IdElement___init__():
    assert notation_IdElement.__init__(notation_IdElement(''), '') == None


from python_code import notation_Image

def test_notation_Image___init__():
    assert notation_Image.__init__(notation_Image(''), '') == None


from python_code import notation_Label
from python_code import notation_TextualElement

def test_notation_TextualElement___init__():
    assert notation_TextualElement.__init__(notation_TextualElement('', notation_TextualElement=notation_Label()), '', notation_TextualElement=notation_Label()) == None


from python_code import notation_EAttribute
from python_code import notation_Value

def test_notation_Value___init__():
    assert notation_Value.__init__(notation_Value('', notation_Value=notation_EAttribute()), '', notation_Value=notation_EAttribute()) == None

