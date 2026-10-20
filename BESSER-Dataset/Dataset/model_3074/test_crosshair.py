from python_code import oml_AnnotatedElement
from python_code import oml_Annotation

def test_oml_Annotation___init__():
    assert oml_Annotation.__init__(oml_Annotation('', '\x00', oml_Annotation=oml_AnnotatedElement()), '\x00\x00', '', oml_Annotation=oml_AnnotatedElement()) == None


from python_code import oml_NamedElement

def test_oml_NamedElement___init__():
    assert oml_NamedElement.__init__(oml_NamedElement(''), '') == None


from python_code import oml_StructuralFeature

def test_oml_StructuralFeature___init__():
    assert oml_StructuralFeature.__init__(oml_StructuralFeature(''), '') == None

