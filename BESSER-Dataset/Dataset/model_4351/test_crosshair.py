from python_code import ecoreDiff_ChangedEAnnotation
from python_code import ecoreDiff_EAnnotation
from python_code import ecoreDiff_EModelElement

def test_ecoreDiff_EAnnotation___init__():
    assert ecoreDiff_EAnnotation.__init__(ecoreDiff_EAnnotation('', ecoreDiff_EAnnotation=set(), eAnnotations=ecoreDiff_EModelElement(), ecoreDiff_EAnnotation3=set(), ecoreDiff_EAnnotation5=set(), EAnnotation=ecoreDiff_EModelElement(), ecoreDiff_EAnnotation107=ecoreDiff_ChangedEAnnotation()), '', ecoreDiff_EAnnotation=set(), eAnnotations=ecoreDiff_EModelElement(), ecoreDiff_EAnnotation3=set(), ecoreDiff_EAnnotation5=set(), EAnnotation=ecoreDiff_EModelElement(), ecoreDiff_EAnnotation107=ecoreDiff_ChangedEAnnotation()) == None


from python_code import ecoreDiff_ChangedEEnumLiteral
from python_code import ecoreDiff_EEnum
from python_code import ecoreDiff_EEnumLiteral

def test_ecoreDiff_EEnumLiteral___init__():
    assert ecoreDiff_EEnumLiteral.__init__(ecoreDiff_EEnumLiteral('', 0, '\x00\x00', ecoreDiff_EEnumLiteral=ecoreDiff_ChangedEEnumLiteral(), eLiterals=ecoreDiff_EEnum(), EEnumLiteral=ecoreDiff_EEnum()), '', 0, '', ecoreDiff_EEnumLiteral=ecoreDiff_ChangedEEnumLiteral(), eLiterals=ecoreDiff_EEnum(), EEnumLiteral=ecoreDiff_EEnum()) == None


from python_code import ecoreDiff_ChangedENamedElement
from python_code import ecoreDiff_ENamedElement

def test_ecoreDiff_ENamedElement___init__():
    assert ecoreDiff_ENamedElement.__init__(ecoreDiff_ENamedElement('', ecoreDiff_ENamedElement=ecoreDiff_ChangedENamedElement()), '', ecoreDiff_ENamedElement=ecoreDiff_ChangedENamedElement()) == None


from python_code import ecoreDiff_ChangedETypedElement
from python_code import ecoreDiff_EGenericType
from python_code import ecoreDiff_ETypedElement

def test_ecoreDiff_ETypedElement___init__():
    assert ecoreDiff_ETypedElement.__init__(ecoreDiff_ETypedElement(False, False, 0, 0, False, '', ecoreDiff_ETypedElement129=ecoreDiff_ChangedETypedElement(), ecoreDiff_ETypedElement=ecoreDiff_EGenericType()), False, False, 0, 0, False, '', ecoreDiff_ETypedElement129=ecoreDiff_ChangedETypedElement(), ecoreDiff_ETypedElement=ecoreDiff_EGenericType()) == None

