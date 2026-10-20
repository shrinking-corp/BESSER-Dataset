from python_code import RefinementsEcore_EAnnotation
from python_code import RefinementsEcore_EModelElement

def test_RefinementsEcore_EAnnotation___init__():
    assert RefinementsEcore_EAnnotation.__init__(RefinementsEcore_EAnnotation('', eAnnotations=RefinementsEcore_EModelElement(), EAnnotation=RefinementsEcore_EModelElement()), '', eAnnotations=RefinementsEcore_EModelElement(), EAnnotation=RefinementsEcore_EModelElement()) == None


from python_code import RefinementsEcore_EEnum
from python_code import RefinementsEcore_EEnumLiteral

def test_RefinementsEcore_EEnumLiteral___init__():
    assert RefinementsEcore_EEnumLiteral.__init__(RefinementsEcore_EEnumLiteral(0, '\x00', EEnumLiteral=RefinementsEcore_EEnum(), eLiterals=RefinementsEcore_EEnum()), 0, '\x00', EEnumLiteral=RefinementsEcore_EEnum(), eLiterals=RefinementsEcore_EEnum()) == None


from python_code import RefinementsEcore_ENamedElement

def test_RefinementsEcore_ENamedElement___init__():
    assert RefinementsEcore_ENamedElement.__init__(RefinementsEcore_ENamedElement(''), '') == None

