from python_code import ktest301_AbstractComponent
from python_code import ktest301_Attributes

def test_ktest301_Attributes___init__():
    assert ktest301_Attributes.__init__(ktest301_Attributes('', ktest301_Attributes=ktest301_AbstractComponent(), ktest301_Attributes15=set()), '', ktest301_Attributes=ktest301_AbstractComponent(), ktest301_Attributes15=set()) == None


from python_code import ktest301_AbstractComponent
from python_code import ktest301_Content

def test_ktest301_Content___init__():
    assert ktest301_Content.__init__(ktest301_Content('', '\x00', ktest301_Content=ktest301_AbstractComponent()), '\x00\x00', '', ktest301_Content=ktest301_AbstractComponent()) == None


from python_code import ktest301_NamedElement

def test_ktest301_NamedElement___init__():
    assert ktest301_NamedElement.__init__(ktest301_NamedElement(''), '') == None


from python_code import ktest301_Type

def test_ktest301_Type___init__():
    assert ktest301_Type.__init__(ktest301_Type('', ktest301_Type=set()), '', ktest301_Type=set()) == None

