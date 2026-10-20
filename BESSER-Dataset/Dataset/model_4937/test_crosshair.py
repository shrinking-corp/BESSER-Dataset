from python_code import webapp_CheckBox

def test_webapp_CheckBox___init__():
    assert webapp_CheckBox.__init__(webapp_CheckBox(''), '') == None


from python_code import webapp_DateBox

def test_webapp_DateBox___init__():
    assert webapp_DateBox.__init__(webapp_DateBox(''), '') == None


from python_code import webapp_FormButton

def test_webapp_FormButton___init__():
    assert webapp_FormButton.__init__(webapp_FormButton(''), '') == None


from python_code import webapp_DropDownList
from python_code import webapp_ListElement
from python_code import webapp_RadioButton

def test_webapp_ListElement___init__():
    assert webapp_ListElement.__init__(webapp_ListElement('', webapp_ListElement11=webapp_RadioButton(), webapp_ListElement=webapp_DropDownList()), '', webapp_ListElement11=webapp_RadioButton(), webapp_ListElement=webapp_DropDownList()) == None


from python_code import webapp_NormalControl
from python_code import webapp_NormalPage

def test_webapp_NormalControl___init__():
    assert webapp_NormalControl.__init__(webapp_NormalControl('', webapp_NormalControl=webapp_NormalPage()), '', webapp_NormalControl=webapp_NormalPage()) == None


from python_code import webapp_TextBox

def test_webapp_TextBox___init__():
    assert webapp_TextBox.__init__(webapp_TextBox('\x00\x00', 0, 0, True), '', 0, 0, False) == None

