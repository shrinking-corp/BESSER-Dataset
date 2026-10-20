from python_code import forms_Condition
from python_code import forms_EMFL_FormModel

def test_forms_Condition___init__():
    assert forms_Condition.__init__(forms_Condition(0, forms_Condition=forms_EMFL_FormModel()), 0, forms_Condition=forms_EMFL_FormModel()) == None


from python_code import forms_TextField

def test_forms_TextField___init__():
    assert forms_TextField.__init__(forms_TextField(''), '') == None

