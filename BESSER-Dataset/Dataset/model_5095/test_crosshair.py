from python_code import adl301_AbstractComponent
from python_code import adl301_Attributes

def test_adl301_Attributes___init__():
    assert adl301_Attributes.__init__(adl301_Attributes('', adl301_Attributes=adl301_AbstractComponent(), adl301_Attributes15=set()), '', adl301_Attributes=adl301_AbstractComponent(), adl301_Attributes15=set()) == None


from python_code import adl301_AbstractComponent
from python_code import adl301_Content

def test_adl301_Content___init__():
    assert adl301_Content.__init__(adl301_Content('', '\x00', adl301_Content=adl301_AbstractComponent()), '\x00\x00', '', adl301_Content=adl301_AbstractComponent()) == None


from python_code import adl301_NamedElement

def test_adl301_NamedElement___init__():
    assert adl301_NamedElement.__init__(adl301_NamedElement(''), '') == None


from python_code import adl301_Type

def test_adl301_Type___init__():
    assert adl301_Type.__init__(adl301_Type('', adl301_Type=set()), '', adl301_Type=set()) == None

