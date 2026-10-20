from python_code import UML2WithID_Element

def test_UML2WithID_Element___init__():
    assert UML2WithID_Element.__init__(UML2WithID_Element(''), '') == None


from python_code import UML2WithID_Association
from python_code import UML2WithID_Property

def test_UML2WithID_Property___init__():
    assert UML2WithID_Property.__init__(UML2WithID_Property('', UML2WithID_Property=UML2WithID_Association()), '', UML2WithID_Property=UML2WithID_Association()) == None

