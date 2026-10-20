from python_code import docbook_Identifiable

def test_docbook_Identifiable___init__():
    assert docbook_Identifiable.__init__(docbook_Identifiable(''), '') == None


from python_code import docbook_Para
from python_code import docbook_Section

def test_docbook_Para___init__():
    assert docbook_Para.__init__(docbook_Para('', docbook_Para=docbook_Section()), '', docbook_Para=docbook_Section()) == None


from python_code import docbook_TitledElement

def test_docbook_TitledElement___init__():
    assert docbook_TitledElement.__init__(docbook_TitledElement(''), '') == None

