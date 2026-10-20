from python_code import UML_14_Enumeration
from python_code import UML_14_EnumerationLiteral

def test_UML_14_EnumerationLiteral___init__():
    assert UML_14_EnumerationLiteral.__init__(UML_14_EnumerationLiteral('', EnumerationLiteral=UML_14_Enumeration(), literal=UML_14_Enumeration()), '', EnumerationLiteral=UML_14_Enumeration(), literal=UML_14_Enumeration()) == None


from python_code import UML_14_Generalization
from python_code import UML_14_Package

def test_UML_14_Generalization___init__():
    assert UML_14_Generalization.__init__(UML_14_Generalization('', UML_14_Generalization=set(), UML_14_Generalization9=set(), UML_14_Generalization41=UML_14_Package()), '', UML_14_Generalization=set(), UML_14_Generalization9=set(), UML_14_Generalization41=UML_14_Package()) == None


from python_code import UML_14_NamedElement

def test_UML_14_NamedElement___init__():
    assert UML_14_NamedElement.__init__(UML_14_NamedElement('', UML_14_NamedElement=set(), UML_14_NamedElement46=set()), '', UML_14_NamedElement=set(), UML_14_NamedElement46=set()) == None

