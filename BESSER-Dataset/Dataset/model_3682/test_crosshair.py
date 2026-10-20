from python_code import UML2_Association
from python_code import UML2_Property

def test_UML2_Property___init__():
    assert UML2_Property.__init__(UML2_Property('', UML2_Property=UML2_Association()), '', UML2_Property=UML2_Association()) == None

