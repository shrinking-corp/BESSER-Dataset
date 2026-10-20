from python_code import forms_AttributePageElement
from python_code import forms_AttributeValueCondition

def test_forms_AttributeValueCondition___init__():
    assert forms_AttributeValueCondition.__init__(forms_AttributeValueCondition('', forms_AttributeValueCondition=forms_AttributePageElement()), '', forms_AttributeValueCondition=forms_AttributePageElement()) == None


from python_code import forms_TextFieldAttributePageElement

def test_forms_TextFieldAttributePageElement___init__():
    assert forms_TextFieldAttributePageElement.__init__(forms_TextFieldAttributePageElement(''), '') == None

