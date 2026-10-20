from python_code import fml_Heading

def test_fml_Heading___init__():
    assert fml_Heading.__init__(fml_Heading('', '\x00'), '\x00\x00', '') == None


from python_code import fml_InputElement

def test_fml_InputElement___init__():
    assert fml_InputElement.__init__(fml_InputElement(True), False) == None


from python_code import fml_List

def test_fml_List___init__():
    assert fml_List.__init__(fml_List(False, fml_List=set()), False, fml_List=set()) == None


from python_code import fml_TextInput

def test_fml_TextInput___init__():
    assert fml_TextInput.__init__(fml_TextInput('', '', '\x00\x00'), '', '', '') == None


from python_code import fml_TextParagraph

def test_fml_TextParagraph___init__():
    assert fml_TextParagraph.__init__(fml_TextParagraph(''), '') == None

