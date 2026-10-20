from python_code import OO_AnnotatedElement
from python_code import OO_Annotation

def test_OO_Annotation___init__():
    assert OO_Annotation.__init__(OO_Annotation('', '\x00', OO_Annotation=OO_AnnotatedElement()), '\x00\x00', '', OO_Annotation=OO_AnnotatedElement()) == None


from python_code import OO_NamedElement

def test_OO_NamedElement___init__():
    assert OO_NamedElement.__init__(OO_NamedElement(''), '') == None


from python_code import OO_StructuralFeature

def test_OO_StructuralFeature___init__():
    assert OO_StructuralFeature.__init__(OO_StructuralFeature(''), '') == None

