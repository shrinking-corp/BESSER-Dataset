from python_code import ClassDiagram_Attribute

def test_ClassDiagram_Attribute___init__():
    assert ClassDiagram_Attribute.__init__(ClassDiagram_Attribute(True), False) == None


from python_code import ClassDiagram_Classifier
from python_code import ClassDiagram_Model
from python_code import ClassDiagram_TypedElement

def test_ClassDiagram_Classifier___init__():
    assert ClassDiagram_Classifier.__init__(ClassDiagram_Classifier('', ClassDiagram_Classifier10=ClassDiagram_TypedElement(), ClassDiagram_Classifier=ClassDiagram_Model()), '', ClassDiagram_Classifier10=ClassDiagram_TypedElement(), ClassDiagram_Classifier=ClassDiagram_Model()) == None


from python_code import ClassDiagram_Operation
from python_code import ClassDiagram_Parameter

def test_ClassDiagram_Parameter___init__():
    assert ClassDiagram_Parameter.__init__(ClassDiagram_Parameter('', Parameter=ClassDiagram_Operation(), params=ClassDiagram_Operation()), '', Parameter=ClassDiagram_Operation(), params=ClassDiagram_Operation()) == None


from python_code import ClassDiagram_Class
from python_code import ClassDiagram_StructuralFeature

def test_ClassDiagram_StructuralFeature___init__():
    assert ClassDiagram_StructuralFeature.__init__(ClassDiagram_StructuralFeature('', '\x00', StructuralFeature=ClassDiagram_Class(), features=ClassDiagram_Class()), '\x00\x00', '', StructuralFeature=ClassDiagram_Class(), features=ClassDiagram_Class()) == None

