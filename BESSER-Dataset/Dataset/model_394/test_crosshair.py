from python_code import UML2_Classifier
from python_code import UML2_NamedElement
from python_code import UML2_Namespace

def test_UML2_NamedElement___init__():
    assert UML2_NamedElement.__init__(UML2_NamedElement('', UML2_NamedElement=UML2_Namespace(), UML2_NamedElement2=UML2_Classifier()), '', UML2_NamedElement=UML2_Namespace(), UML2_NamedElement2=UML2_Classifier()) == None

