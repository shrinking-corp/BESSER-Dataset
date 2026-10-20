from python_code import form_Heading

def test_form_Heading___init__():
    assert form_Heading.__init__(form_Heading(0), 0) == None


from python_code import form_InputField

def test_form_InputField___init__():
    assert form_InputField.__init__(form_InputField('', False), '', False) == None


from python_code import form_List

def test_form_List___init__():
    assert form_List.__init__(form_List(False, form_List=set()), False, form_List=set()) == None


from python_code import form_Text

def test_form_Text___init__():
    assert form_Text.__init__(form_Text(''), '') == None


from python_code import form_TextField

def test_form_TextField___init__():
    assert form_TextField.__init__(form_TextField(True), False) == None

