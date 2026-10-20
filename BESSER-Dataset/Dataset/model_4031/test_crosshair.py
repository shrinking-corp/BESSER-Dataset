from python_code import uml_Class
from python_code import uml_Classifier
from python_code import uml_Generalization

def test_uml_Classifier___init__():
    assert uml_Classifier.__init__(uml_Classifier('', uml_Classifier=uml_Generalization(), Classifier=uml_Generalization(), uml_Classifier6=uml_Class(), specific=set()), '', uml_Classifier=uml_Generalization(), Classifier=uml_Generalization(), uml_Classifier6=uml_Class(), specific=set()) == None


from python_code import uml_Dependency
from python_code import uml_NamedElement

def test_uml_NamedElement___init__():
    assert uml_NamedElement.__init__(uml_NamedElement('', '\x00', uml_NamedElement=uml_Dependency()), '\x00\x00', '', uml_NamedElement=uml_Dependency()) == None

