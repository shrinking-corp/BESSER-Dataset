from python_code import forms_AttributeValueCondition

def test_forms_AttributeValueCondition___init__():
    assert forms_AttributeValueCondition.__init__(forms_AttributeValueCondition(''), '') == None


from python_code import forms_CompositeCondition

def test_forms_CompositeCondition___init__():
    assert forms_CompositeCondition.__init__(forms_CompositeCondition('', forms_CompositeCondition=set()), '', forms_CompositeCondition=set()) == None


from python_code import forms_TextField

def test_forms_TextField___init__():
    assert forms_TextField.__init__(forms_TextField(''), '') == None

