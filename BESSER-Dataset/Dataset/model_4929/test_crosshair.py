from python_code import webapp_Attribute
from python_code import webapp_Model

def test_webapp_Attribute___init__():
    assert webapp_Attribute.__init__(webapp_Attribute('', webapp_Attribute=webapp_Model()), '', webapp_Attribute=webapp_Model()) == None


from python_code import webapp_CheckBox

def test_webapp_CheckBox___init__():
    assert webapp_CheckBox.__init__(webapp_CheckBox(''), '') == None


from python_code import webapp_Form
from python_code import webapp_FormWidget

def test_webapp_FormWidget___init__():
    assert webapp_FormWidget.__init__(webapp_FormWidget('', formWidgets=webapp_Form(), FormWidget=webapp_Form()), '', formWidgets=webapp_Form(), FormWidget=webapp_Form()) == None


from python_code import webapp_Gallery

def test_webapp_Gallery___init__():
    assert webapp_Gallery.__init__(webapp_Gallery(''), '') == None


from python_code import webapp_ImagesBlock

def test_webapp_ImagesBlock___init__():
    assert webapp_ImagesBlock.__init__(webapp_ImagesBlock(''), '') == None


from python_code import webapp_NamedElement

def test_webapp_NamedElement___init__():
    assert webapp_NamedElement.__init__(webapp_NamedElement(''), '') == None


from python_code import webapp_Spinner

def test_webapp_Spinner___init__():
    assert webapp_Spinner.__init__(webapp_Spinner(''), '') == None


from python_code import webapp_Table

def test_webapp_Table___init__():
    assert webapp_Table.__init__(webapp_Table('\x00\x00', '', False, True), '', '', False, False) == None


from python_code import webapp_Text

def test_webapp_Text___init__():
    assert webapp_Text.__init__(webapp_Text(0), 0) == None


from python_code import webapp_Video

def test_webapp_Video___init__():
    assert webapp_Video.__init__(webapp_Video(''), '') == None

