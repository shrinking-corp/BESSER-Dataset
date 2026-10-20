from python_code import UML2_ElementImport
from python_code import UML2_PackageableElement

def test_UML2_ElementImport___init__():
    assert UML2_ElementImport.__init__(UML2_ElementImport('', UML2_ElementImport=UML2_PackageableElement()), '', UML2_ElementImport=UML2_PackageableElement()) == None


from python_code import UML2_MultiplicityElement

def test_UML2_MultiplicityElement___init__():
    assert UML2_MultiplicityElement.__init__(UML2_MultiplicityElement(False, False, 0, ''), False, False, 0, '') == None


from python_code import UML2_Behavior
from python_code import UML2_OpaqueExpression

def test_UML2_OpaqueExpression___init__():
    assert UML2_OpaqueExpression.__init__(UML2_OpaqueExpression('', '\x00', UML2_OpaqueExpression=UML2_Behavior()), '\x00\x00', '', UML2_OpaqueExpression=UML2_Behavior()) == None


from python_code import UML2_Constraint
from python_code import UML2_Operation

def test_UML2_Operation___init__():
    assert UML2_Operation.__init__(UML2_Operation(False, UML2_Operation=set(), UML2_Operation25=UML2_Constraint()), False, UML2_Operation=set(), UML2_Operation25=UML2_Constraint()) == None


from python_code import UML2_PackageImport

def test_UML2_PackageImport___init__():
    assert UML2_PackageImport.__init__(UML2_PackageImport(''), '') == None


from python_code import UML2_Slot
from python_code import UML2_StructuralFeature
from python_code import UML2_StructuralFeatureAction

def test_UML2_StructuralFeature___init__():
    assert UML2_StructuralFeature.__init__(UML2_StructuralFeature(True, UML2_StructuralFeature39=UML2_Slot(), UML2_StructuralFeature=UML2_StructuralFeatureAction()), False, UML2_StructuralFeature39=UML2_Slot(), UML2_StructuralFeature=UML2_StructuralFeatureAction()) == None

