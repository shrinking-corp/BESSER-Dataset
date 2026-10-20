from python_code import uml_UML_NamedElement

def test_uml_UML_NamedElement___init__():
    assert uml_UML_NamedElement.__init__(uml_UML_NamedElement(''), '') == None


from python_code import uml_UML_Constraint
from python_code import uml_UML_OpaqueExpression

def test_uml_UML_OpaqueExpression___init__():
    assert uml_UML_OpaqueExpression.__init__(uml_UML_OpaqueExpression('', '\x00', uml_UML_OpaqueExpression=uml_UML_Constraint()), '\x00\x00', '', uml_UML_OpaqueExpression=uml_UML_Constraint()) == None

