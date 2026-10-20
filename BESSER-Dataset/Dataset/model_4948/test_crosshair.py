from python_code import form_Input

def test_form_Input___init__():
    assert form_Input.__init__(form_Input(False, '', '\x00\x00'), False, '', '') == None


from python_code import form_SelectionList

def test_form_SelectionList___init__():
    assert form_SelectionList.__init__(form_SelectionList(False, form_SelectionList=set()), False, form_SelectionList=set()) == None


from python_code import form_textArea

def test_form_textArea___init__():
    assert form_textArea.__init__(form_textArea(''), '') == None

