from python_code import classdiagram_Association
from python_code import classdiagram_Class
from python_code import classdiagram_ClassDiagram

def test_classdiagram_Association___init__():
    assert classdiagram_Association.__init__(classdiagram_Association('', classdiagram_Association=classdiagram_ClassDiagram(), Association=classdiagram_Class(), Association28=classdiagram_Class(), associationsAsSource=classdiagram_Class(), associationsAsTarget=classdiagram_Class()), '', classdiagram_Association=classdiagram_ClassDiagram(), Association=classdiagram_Class(), Association28=classdiagram_Class(), associationsAsSource=classdiagram_Class(), associationsAsTarget=classdiagram_Class()) == None


from python_code import classdiagram_Class
from python_code import classdiagram_ClassDiagram
from python_code import classdiagram_Composition

def test_classdiagram_Composition___init__():
    assert classdiagram_Composition.__init__(classdiagram_Composition('', classdiagram_Composition=classdiagram_ClassDiagram(), Composition=classdiagram_Class(), Composition31=classdiagram_Class(), compositionsAsConstituent=classdiagram_Class(), compositionsAsComposite=classdiagram_Class()), '', classdiagram_Composition=classdiagram_ClassDiagram(), Composition=classdiagram_Class(), Composition31=classdiagram_Class(), compositionsAsConstituent=classdiagram_Class(), compositionsAsComposite=classdiagram_Class()) == None


from python_code import classdiagram_Class
from python_code import classdiagram_ClassDiagram
from python_code import classdiagram_Dependency

def test_classdiagram_Dependency___init__():
    assert classdiagram_Dependency.__init__(classdiagram_Dependency('', Dependency=classdiagram_Class(), Dependency14=classdiagram_Class(), classdiagram_Dependency=classdiagram_ClassDiagram(), dependenciesAsDependee=classdiagram_Class(), dependenciesAsDepender=classdiagram_Class()), '', Dependency=classdiagram_Class(), Dependency14=classdiagram_Class(), classdiagram_Dependency=classdiagram_ClassDiagram(), dependenciesAsDependee=classdiagram_Class(), dependenciesAsDepender=classdiagram_Class()) == None


from python_code import classdiagram_NamedElement

def test_classdiagram_NamedElement___init__():
    assert classdiagram_NamedElement.__init__(classdiagram_NamedElement(''), '') == None


from python_code import classdiagram_Typeable
from python_code import classdiagram_TypedElement

def test_classdiagram_TypedElement___init__():
    assert classdiagram_TypedElement.__init__(classdiagram_TypedElement(True, classdiagram_TypedElement=classdiagram_Typeable()), False, classdiagram_TypedElement=classdiagram_Typeable()) == None

