from python_code import UML2WithID_Element

def test_UML2WithID_Element___init__():
    assert UML2WithID_Element.__init__(UML2WithID_Element(''), '') == None


from python_code import UML2WithID_Operation
from python_code import UML2WithID_Parameter

def test_UML2WithID_Parameter___init__():
    assert UML2WithID_Parameter.__init__(UML2WithID_Parameter('', UML2WithID_Parameter=UML2WithID_Operation()), '', UML2WithID_Parameter=UML2WithID_Operation()) == None

