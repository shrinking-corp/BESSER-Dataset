from python_code import adlrecurs_AbstractComponent
from python_code import adlrecurs_Attributes

def test_adlrecurs_Attributes___init__():
    assert adlrecurs_Attributes.__init__(adlrecurs_Attributes('', adlrecurs_Attributes15=set(), adlrecurs_Attributes=adlrecurs_AbstractComponent()), '', adlrecurs_Attributes15=set(), adlrecurs_Attributes=adlrecurs_AbstractComponent()) == None


from python_code import adlrecurs_AbstractComponent
from python_code import adlrecurs_Content

def test_adlrecurs_Content___init__():
    assert adlrecurs_Content.__init__(adlrecurs_Content('', '\x00', adlrecurs_Content=adlrecurs_AbstractComponent()), '\x00\x00', '', adlrecurs_Content=adlrecurs_AbstractComponent()) == None


from python_code import adlrecurs_NamedElement

def test_adlrecurs_NamedElement___init__():
    assert adlrecurs_NamedElement.__init__(adlrecurs_NamedElement(''), '') == None


from python_code import adlrecurs_Type

def test_adlrecurs_Type___init__():
    assert adlrecurs_Type.__init__(adlrecurs_Type('', adlrecurs_Type=set()), '', adlrecurs_Type=set()) == None

