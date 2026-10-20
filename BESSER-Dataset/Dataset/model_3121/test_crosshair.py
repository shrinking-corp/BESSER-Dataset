from python_code import Class
from python_code import ClassDiagram_Attribute
from python_code import Classifier

def test_ClassDiagram_Attribute___init__():
    assert ClassDiagram_Attribute.__init__(ClassDiagram_Attribute('', ClassDiagram_Attribute=Classifier(), attr=Class()), '\x00', ClassDiagram_Attribute=Classifier(), attr=Class()) == None


from python_code import Class
from python_code import ClassDiagram_Attribute
from python_code import ClassDiagram_Class
from python_code import Classifier
from python_code import Package

def test_ClassDiagram_Class___init__():
    assert ClassDiagram_Class.__init__(ClassDiagram_Class('', ClassDiagram_Class=set(), owner4=set(), ownedElements=Package(), Classifier=ClassDiagram_Attribute('', ClassDiagram_Attribute=Classifier(), attr=Class())), '', ClassDiagram_Class=set(), owner4=set(), ownedElements=Package(), Classifier=ClassDiagram_Attribute('', ClassDiagram_Attribute=Classifier(), attr=Class())) == None


from python_code import ClassDiagram_NamedElement

def test_ClassDiagram_NamedElement___init__():
    assert ClassDiagram_NamedElement.__init__(ClassDiagram_NamedElement(''), '') == None

