from python_code import UML2_MultiplicityElement

def test_UML2_MultiplicityElement___init__():
    assert UML2_MultiplicityElement.__init__(UML2_MultiplicityElement(True), False) == None


from python_code import UML2_Operation
from python_code import UML2_Parameter

def test_UML2_Parameter___init__():
    assert UML2_Parameter.__init__(UML2_Parameter('', UML2_Parameter=UML2_Operation()), '', UML2_Parameter=UML2_Operation()) == None

