from python_code import UML2_Constraint
from python_code import UML2_Operation

def test_UML2_Operation___init__():
    assert UML2_Operation.__init__(UML2_Operation(True, UML2_Operation=UML2_Constraint()), False, UML2_Operation=UML2_Constraint()) == None

