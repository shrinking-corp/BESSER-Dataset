from python_code import classdiagram_Class
from python_code import classdiagram_ClassDiagram
from python_code import classdiagram_Dependency

def test_classdiagram_Dependency___init__():
    assert classdiagram_Dependency.__init__(classdiagram_Dependency('', classdiagram_Dependency=classdiagram_ClassDiagram(), Dependency=classdiagram_Class(), Dependency10=classdiagram_Class(), dependenciesAsDependee=classdiagram_Class(), dependenciesAsDepender=classdiagram_Class()), '', classdiagram_Dependency=classdiagram_ClassDiagram(), Dependency=classdiagram_Class(), Dependency10=classdiagram_Class(), dependenciesAsDependee=classdiagram_Class(), dependenciesAsDepender=classdiagram_Class()) == None


from python_code import classdiagram_NamedElement

def test_classdiagram_NamedElement___init__():
    assert classdiagram_NamedElement.__init__(classdiagram_NamedElement(''), '') == None


from python_code import classdiagram_Class
from python_code import classdiagram_TypedElement

def test_classdiagram_TypedElement___init__():
    assert classdiagram_TypedElement.__init__(classdiagram_TypedElement(True, classdiagram_TypedElement=classdiagram_Class()), False, classdiagram_TypedElement=classdiagram_Class()) == None

