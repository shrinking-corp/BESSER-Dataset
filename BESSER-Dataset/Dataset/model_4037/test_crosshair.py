from python_code import uml_Class

def test_uml_Class___init__():
    assert uml_Class.__init__(uml_Class('', '', uml_Class=set(), uml_Class5=set(), uml_Class8=set(), uml_Class10=set()), '\x00', '', uml_Class=set(), uml_Class5=set(), uml_Class8=set(), uml_Class10=set()) == None


from python_code import uml_Dependency
from python_code import uml_NamedElement

def test_uml_NamedElement___init__():
    assert uml_NamedElement.__init__(uml_NamedElement('', '\x00', uml_NamedElement=uml_Dependency(), uml_NamedElement16=uml_Dependency()), '\x00\x00', '', uml_NamedElement=uml_Dependency(), uml_NamedElement16=uml_Dependency()) == None

