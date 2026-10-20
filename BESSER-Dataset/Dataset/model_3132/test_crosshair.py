from python_code import ClassM_Attribute

def test_ClassM_Attribute___init__():
    assert ClassM_Attribute.__init__(ClassM_Attribute(True), False) == None


from python_code import ClassM_Classifier
from python_code import ClassM_Model
from python_code import ClassM_TypedElement

def test_ClassM_Classifier___init__():
    assert ClassM_Classifier.__init__(ClassM_Classifier('', type=set(), Classifier=ClassM_TypedElement(), ClassM_Classifier=ClassM_Model()), '', type=set(), Classifier=ClassM_TypedElement(), ClassM_Classifier=ClassM_Model()) == None


from python_code import ClassM_Operation
from python_code import ClassM_Parameter

def test_ClassM_Parameter___init__():
    assert ClassM_Parameter.__init__(ClassM_Parameter('', Parameter=ClassM_Operation(), params=ClassM_Operation()), '', Parameter=ClassM_Operation(), params=ClassM_Operation()) == None


from python_code import ClassM_Class
from python_code import ClassM_StructuralFeature

def test_ClassM_StructuralFeature___init__():
    assert ClassM_StructuralFeature.__init__(ClassM_StructuralFeature('', '\x00', StructuralFeature=ClassM_Class(), features=ClassM_Class()), '\x00\x00', '', StructuralFeature=ClassM_Class(), features=ClassM_Class()) == None

