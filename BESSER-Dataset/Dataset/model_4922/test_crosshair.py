from python_code import dsml_visitor_Visitor

def test_dsml_visitor_Visitor___init__():
    assert dsml_visitor_Visitor.__init__(dsml_visitor_Visitor(''), '') == None


from python_code import dsml_web_BetweenValidator
from python_code import dsml_web_Field

def test_dsml_web_BetweenValidator___init__():
    assert dsml_web_BetweenValidator.__init__(dsml_web_BetweenValidator(0, 0, Validator=dsml_web_Field()), 0, 0, Validator=dsml_web_Field()) == None


from python_code import Error
from python_code import Success
from python_code import dsml_web_Form

def test_dsml_web_Form___init__():
    assert dsml_web_Form.__init__(dsml_web_Form('', dsml_web_Form=set(), dsml_web_Form12=Success(), dsml_web_Form14=Error()), '', dsml_web_Form=set(), dsml_web_Form12=Success(), dsml_web_Form14=Error()) == None

def test_dsml_web_Form_accept():
    assert dsml_web_Form.accept(dsml_web_Form('', dsml_web_Form=set(), dsml_web_Form12=Success(), dsml_web_Form14=Error()), '') == None


from python_code import dsml_web_FormElement

def test_dsml_web_FormElement___init__():
    assert dsml_web_FormElement.__init__(dsml_web_FormElement('', '\x00'), '\x00\x00', '') == None

def test_dsml_web_FormElement_accept():
    assert dsml_web_FormElement.accept(dsml_web_FormElement('', ''), '') == None


from python_code import dsml_web_Field
from python_code import dsml_web_GreaterThanValidator

def test_dsml_web_GreaterThanValidator___init__():
    assert dsml_web_GreaterThanValidator.__init__(dsml_web_GreaterThanValidator(0, Validator=dsml_web_Field()), 0, Validator=dsml_web_Field()) == None


from python_code import dsml_web_Item

def test_dsml_web_Item___init__():
    assert dsml_web_Item.__init__(dsml_web_Item(''), '') == None


from python_code import dsml_web_Field
from python_code import dsml_web_LessThanValidator

def test_dsml_web_LessThanValidator___init__():
    assert dsml_web_LessThanValidator.__init__(dsml_web_LessThanValidator(0, Validator=dsml_web_Field()), 0, Validator=dsml_web_Field()) == None


from python_code import Page
from python_code import dsml_web_Link

def test_dsml_web_Link___init__():
    assert dsml_web_Link.__init__(dsml_web_Link('', dsml_web_Link=Page()), '', dsml_web_Link=Page()) == None

def test_dsml_web_Link_accept():
    assert dsml_web_Link.accept(dsml_web_Link('', dsml_web_Link=Page()), 0) == None


from python_code import Form
from python_code import dsml_web_Page

def test_dsml_web_Page___init__():
    assert dsml_web_Page.__init__(dsml_web_Page('', '', dsml_web_Page=Form(), dsml_web_Page3=set(), dsml_web_Page5=set()), '', '', dsml_web_Page=Form(), dsml_web_Page3=set(), dsml_web_Page5=set()) == None


from python_code import dsml_web_PasswordField

def test_dsml_web_PasswordField___init__():
    assert dsml_web_PasswordField.__init__(dsml_web_PasswordField(0, 0), 0, 0) == None


from python_code import dsml_web_Field
from python_code import dsml_web_RegexValidator

def test_dsml_web_RegexValidator___init__():
    assert dsml_web_RegexValidator.__init__(dsml_web_RegexValidator('', Validator=dsml_web_Field()), '', Validator=dsml_web_Field()) == None


from python_code import dsml_web_Select

def test_dsml_web_Select___init__():
    assert dsml_web_Select.__init__(dsml_web_Select(0), 0) == None


from python_code import dsml_web_Field
from python_code import dsml_web_StringLengthValidator

def test_dsml_web_StringLengthValidator___init__():
    assert dsml_web_StringLengthValidator.__init__(dsml_web_StringLengthValidator(0, 0, Validator=dsml_web_Field()), 0, 0, Validator=dsml_web_Field()) == None


from python_code import dsml_web_Text

def test_dsml_web_Text___init__():
    assert dsml_web_Text.__init__(dsml_web_Text(''), '') == None

def test_dsml_web_Text_accept():
    assert dsml_web_Text.accept(dsml_web_Text(''), 0) == None


from python_code import dsml_web_TextArea

def test_dsml_web_TextArea___init__():
    assert dsml_web_TextArea.__init__(dsml_web_TextArea(0, 0), 0, 0) == None


from python_code import dsml_web_TextField

def test_dsml_web_TextField___init__():
    assert dsml_web_TextField.__init__(dsml_web_TextField(0, 0), 0, 0) == None


from python_code import dsml_web_Field
from python_code import dsml_web_TypeValidator

def test_dsml_web_TypeValidator___init__():
    assert dsml_web_TypeValidator.__init__(dsml_web_TypeValidator('', Validator=dsml_web_Field()), '', Validator=dsml_web_Field()) == None


from python_code import dsml_web_Validator

def test_dsml_web_Validator___init__():
    assert dsml_web_Validator.__init__(dsml_web_Validator()) == None

def test_dsml_web_Validator_accept():
    assert dsml_web_Validator.accept(dsml_web_Validator(), '') == None


from python_code import dsml_web_Website

def test_dsml_web_Website___init__():
    assert dsml_web_Website.__init__(dsml_web_Website('', dsml_web_Website=set()), '', dsml_web_Website=set()) == None

