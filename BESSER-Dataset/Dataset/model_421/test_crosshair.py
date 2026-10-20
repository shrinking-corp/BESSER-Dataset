from python_code import UML2_Class

def test_UML2_Class___init__():
    assert UML2_Class.__init__(UML2_Class(False, UML2_Class=set(), UML2_Class34=set()), False, UML2_Class=set(), UML2_Class34=set()) == None


from python_code import UML2_MultiplicityElement

def test_UML2_MultiplicityElement___init__():
    assert UML2_MultiplicityElement.__init__(UML2_MultiplicityElement(False, False, 0, ''), False, False, 0, '') == None


from python_code import UML2_Constraint
from python_code import UML2_Operation

def test_UML2_Operation___init__():
    assert UML2_Operation.__init__(UML2_Operation(False, UML2_Operation=set(), UML2_Operation18=UML2_Constraint()), False, UML2_Operation=set(), UML2_Operation18=UML2_Constraint()) == None


from python_code import UML2_Slot
from python_code import UML2_StructuralFeature
from python_code import UML2_StructuralFeatureAction

def test_UML2_StructuralFeature___init__():
    assert UML2_StructuralFeature.__init__(UML2_StructuralFeature(True, UML2_StructuralFeature68=UML2_StructuralFeatureAction(), UML2_StructuralFeature=UML2_Slot()), False, UML2_StructuralFeature68=UML2_StructuralFeatureAction(), UML2_StructuralFeature=UML2_Slot()) == None

