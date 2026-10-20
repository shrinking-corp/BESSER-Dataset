from python_code import classm1_Attribute
from python_code import classm1_Class

def test_classm1_Attribute___init__():
    assert classm1_Attribute.__init__(classm1_Attribute(False, '\x00', classm1_Attribute=classm1_Class(), classm1_Attribute2=classm1_Class()), False, '\x00', classm1_Attribute=classm1_Class(), classm1_Attribute2=classm1_Class()) == None


from python_code import classm1_CNamedElement

def test_classm1_CNamedElement___init__():
    assert classm1_CNamedElement.__init__(classm1_CNamedElement(''), '') == None

