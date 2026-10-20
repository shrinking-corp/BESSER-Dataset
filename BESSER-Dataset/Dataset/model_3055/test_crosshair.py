from python_code import entityDsl_ComboBox
from python_code import entityDsl_ComboBoxItem

def test_entityDsl_ComboBoxItem___init__():
    assert entityDsl_ComboBoxItem.__init__(entityDsl_ComboBoxItem('', entityDsl_ComboBoxItem=entityDsl_ComboBox()), '', entityDsl_ComboBoxItem=entityDsl_ComboBox()) == None


from python_code import entityDsl_Domainmodel

def test_entityDsl_Domainmodel___init__():
    assert entityDsl_Domainmodel.__init__(entityDsl_Domainmodel('', entityDsl_Domainmodel=set()), '', entityDsl_Domainmodel=set()) == None


from python_code import entityDsl_RadioButton
from python_code import entityDsl_RadioButtonGroup

def test_entityDsl_RadioButton___init__():
    assert entityDsl_RadioButton.__init__(entityDsl_RadioButton('', entityDsl_RadioButton=entityDsl_RadioButtonGroup()), '', entityDsl_RadioButton=entityDsl_RadioButtonGroup()) == None


from python_code import entityDsl_Spinner

def test_entityDsl_Spinner___init__():
    assert entityDsl_Spinner.__init__(entityDsl_Spinner(0, 0, 0), 0, 0, 0) == None

