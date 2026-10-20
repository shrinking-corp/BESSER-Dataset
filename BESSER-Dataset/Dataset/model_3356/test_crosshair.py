from python_code import uispecDsl_ComboWidget

def test_uispecDsl_ComboWidget___init__():
    assert uispecDsl_ComboWidget.__init__(uispecDsl_ComboWidget(''), '') == None


from python_code import uispecDsl_Form

def test_uispecDsl_Form___init__():
    assert uispecDsl_Form.__init__(uispecDsl_Form('', uispecDsl_Form2=set(), uispecDsl_Form=set()), '', uispecDsl_Form2=set(), uispecDsl_Form=set()) == None


from python_code import uispecDsl_TextFieldWidget

def test_uispecDsl_TextFieldWidget___init__():
    assert uispecDsl_TextFieldWidget.__init__(uispecDsl_TextFieldWidget(0), 0) == None

