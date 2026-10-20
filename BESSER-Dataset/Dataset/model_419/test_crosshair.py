from python_code import UML2_MultiplicityElement

def test_UML2_MultiplicityElement___init__():
    assert UML2_MultiplicityElement.__init__(UML2_MultiplicityElement(False, False, 0, ''), False, False, 0, '') == None


from python_code import UML2_Operation
from python_code import UML2_Parameter

def test_UML2_Parameter___init__():
    assert UML2_Parameter.__init__(UML2_Parameter('', UML2_Parameter=UML2_Operation()), '', UML2_Parameter=UML2_Operation()) == None


from python_code import UML2_Slot
from python_code import UML2_StructuralFeature
from python_code import UML2_StructuralFeatureAction

def test_UML2_StructuralFeature___init__():
    assert UML2_StructuralFeature.__init__(UML2_StructuralFeature(True, UML2_StructuralFeature=UML2_StructuralFeatureAction(), UML2_StructuralFeature47=UML2_Slot()), False, UML2_StructuralFeature=UML2_StructuralFeatureAction(), UML2_StructuralFeature47=UML2_Slot()) == None

