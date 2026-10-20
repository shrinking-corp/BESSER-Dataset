from python_code import smalluml_Enumeration

def test_smalluml_Enumeration___init__():
    assert smalluml_Enumeration.__init__(smalluml_Enumeration(''), '') == None


from python_code import smalluml_NamedElement
from python_code import smalluml_Package

def test_smalluml_NamedElement___init__():
    assert smalluml_NamedElement.__init__(smalluml_NamedElement('', smalluml_NamedElement=smalluml_Package()), '', smalluml_NamedElement=smalluml_Package()) == None


from python_code import smalluml_Class
from python_code import smalluml_Relation
from python_code import smalluml_Role

def test_smalluml_Role___init__():
    assert smalluml_Role.__init__(smalluml_Role(0, 0, smalluml_Role=smalluml_Relation(), smalluml_Role19=smalluml_Relation(), smalluml_Role21=smalluml_Class()), 0, 0, smalluml_Role=smalluml_Relation(), smalluml_Role19=smalluml_Relation(), smalluml_Role21=smalluml_Class()) == None

