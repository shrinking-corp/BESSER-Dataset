from python_code import UML2WithID_Element

def test_UML2WithID_Element___init__():
    assert UML2WithID_Element.__init__(UML2WithID_Element(''), '') == None


from python_code import UML2WithID_NamedElement
from python_code import UML2WithID_Namespace

def test_UML2WithID_NamedElement___init__():
    assert UML2WithID_NamedElement.__init__(UML2WithID_NamedElement('', UML2WithID_NamedElement=UML2WithID_Namespace()), '', UML2WithID_NamedElement=UML2WithID_Namespace()) == None

