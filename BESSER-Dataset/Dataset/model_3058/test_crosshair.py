from python_code import classLayout2Frontend_Autocomplete

def test_classLayout2Frontend_Autocomplete___init__():
    assert classLayout2Frontend_Autocomplete.__init__(classLayout2Frontend_Autocomplete(True), False) == None


from python_code import classLayout2Frontend_Image

def test_classLayout2Frontend_Image___init__():
    assert classLayout2Frontend_Image.__init__(classLayout2Frontend_Image(0.0, 0.0), 0.0, 0.0) == None


from python_code import classLayout2Frontend_Input
from python_code import classLayout2Frontend_IterationFilter

def test_classLayout2Frontend_Input___init__():
    assert classLayout2Frontend_Input.__init__(classLayout2Frontend_Input('', classLayout2Frontend_Input=classLayout2Frontend_IterationFilter()), '', classLayout2Frontend_Input=classLayout2Frontend_IterationFilter()) == None


from python_code import classLayout2Frontend_InputText

def test_classLayout2Frontend_InputText___init__():
    assert classLayout2Frontend_InputText.__init__(classLayout2Frontend_InputText(True), False) == None


from python_code import classLayout2Frontend_List

def test_classLayout2Frontend_List___init__():
    assert classLayout2Frontend_List.__init__(classLayout2Frontend_List(True), False) == None


from python_code import classLayout2Frontend_Enumeration
from python_code import classLayout2Frontend_Literal

def test_classLayout2Frontend_Literal___init__():
    assert classLayout2Frontend_Literal.__init__(classLayout2Frontend_Literal(0, classLayout2Frontend_Literal=classLayout2Frontend_Enumeration()), 0, classLayout2Frontend_Literal=classLayout2Frontend_Enumeration()) == None


from python_code import classLayout2Frontend_Property
from python_code import classLayout2Frontend_PropertyType

def test_classLayout2Frontend_Property___init__():
    assert classLayout2Frontend_Property.__init__(classLayout2Frontend_Property('', classLayout2Frontend_Property=classLayout2Frontend_PropertyType()), '', classLayout2Frontend_Property=classLayout2Frontend_PropertyType()) == None


from python_code import classLayout2Frontend_TextArea

def test_classLayout2Frontend_TextArea___init__():
    assert classLayout2Frontend_TextArea.__init__(classLayout2Frontend_TextArea('', False), '', False) == None

