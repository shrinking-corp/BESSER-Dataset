from python_code import bootstrap_CheckBox

def test_bootstrap_CheckBox___init__():
    assert bootstrap_CheckBox.__init__(bootstrap_CheckBox(''), '') == None


from python_code import bootstrap_Form
from python_code import bootstrap_FormWidget

def test_bootstrap_FormWidget___init__():
    assert bootstrap_FormWidget.__init__(bootstrap_FormWidget('', formWidgets=bootstrap_Form(), FormWidget=bootstrap_Form()), '', formWidgets=bootstrap_Form(), FormWidget=bootstrap_Form()) == None


from python_code import bootstrap_Gallery

def test_bootstrap_Gallery___init__():
    assert bootstrap_Gallery.__init__(bootstrap_Gallery(''), '') == None


from python_code import bootstrap_ImagesBlock

def test_bootstrap_ImagesBlock___init__():
    assert bootstrap_ImagesBlock.__init__(bootstrap_ImagesBlock(''), '') == None


from python_code import bootstrap_Spinner

def test_bootstrap_Spinner___init__():
    assert bootstrap_Spinner.__init__(bootstrap_Spinner(''), '') == None


from python_code import bootstrap_Table

def test_bootstrap_Table___init__():
    assert bootstrap_Table.__init__(bootstrap_Table('\x00\x00', '', False, True), '', '', False, False) == None


from python_code import bootstrap_Text

def test_bootstrap_Text___init__():
    assert bootstrap_Text.__init__(bootstrap_Text(0), 0) == None


from python_code import bootstrap_Video

def test_bootstrap_Video___init__():
    assert bootstrap_Video.__init__(bootstrap_Video(''), '') == None

