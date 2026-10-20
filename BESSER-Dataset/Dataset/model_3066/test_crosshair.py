from python_code import forms_CompositeCondition

def test_forms_CompositeCondition___init__():
    assert forms_CompositeCondition.__init__(forms_CompositeCondition('', forms_CompositeCondition=set()), '', forms_CompositeCondition=set()) == None


from python_code import forms_Entity
from python_code import forms_Form
from python_code import forms_FormModel
from python_code import forms_RelationshipPageElement

def test_forms_Form___init__():
    assert forms_Form.__init__(forms_Form('', '', False, forms_Form=forms_FormModel(), forms_Form18=forms_Entity(), forms_Form21=set(), forms_Form40=forms_RelationshipPageElement()), '', '', True, forms_Form=forms_FormModel(), forms_Form18=forms_Entity(), forms_Form21=set(), forms_Form40=forms_RelationshipPageElement()) == None


from python_code import forms_Enumeration
from python_code import forms_Literal

def test_forms_Literal___init__():
    assert forms_Literal.__init__(forms_Literal('', forms_Literal=forms_Enumeration()), '', forms_Literal=forms_Enumeration()) == None


from python_code import forms_NamedElement

def test_forms_NamedElement___init__():
    assert forms_NamedElement.__init__(forms_NamedElement(''), '') == None


from python_code import forms_TextField

def test_forms_TextField___init__():
    assert forms_TextField.__init__(forms_TextField(''), '') == None

