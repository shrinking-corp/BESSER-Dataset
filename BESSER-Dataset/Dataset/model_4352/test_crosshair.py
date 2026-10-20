from python_code import ecoreDiff_ChangedEAnnotation
from python_code import ecoreDiff_EAnnotation
from python_code import ecoreDiff_EModelElement

def test_ecoreDiff_EAnnotation___init__():
    assert ecoreDiff_EAnnotation.__init__(ecoreDiff_EAnnotation('', ecoreDiff_EAnnotation=set(), ecoreDiff_EAnnotation2=ecoreDiff_EModelElement(), ecoreDiff_EAnnotation4=set(), ecoreDiff_EAnnotation6=set(), ecoreDiff_EAnnotation93=ecoreDiff_ChangedEAnnotation(), ecoreDiff_EAnnotation86=ecoreDiff_EModelElement()), '', ecoreDiff_EAnnotation=set(), ecoreDiff_EAnnotation2=ecoreDiff_EModelElement(), ecoreDiff_EAnnotation4=set(), ecoreDiff_EAnnotation6=set(), ecoreDiff_EAnnotation93=ecoreDiff_ChangedEAnnotation(), ecoreDiff_EAnnotation86=ecoreDiff_EModelElement()) == None


from python_code import ecoreDiff_ChangedEDataType
from python_code import ecoreDiff_EDataType

def test_ecoreDiff_EDataType___init__():
    assert ecoreDiff_EDataType.__init__(ecoreDiff_EDataType(True, ecoreDiff_EDataType=ecoreDiff_ChangedEDataType()), False, ecoreDiff_EDataType=ecoreDiff_ChangedEDataType()) == None


from python_code import ecoreDiff_ChangedEEnumLiteral
from python_code import ecoreDiff_EEnum
from python_code import ecoreDiff_EEnumLiteral

def test_ecoreDiff_EEnumLiteral___init__():
    assert ecoreDiff_EEnumLiteral.__init__(ecoreDiff_EEnumLiteral(0, '', '\x00\x00', ecoreDiff_EEnumLiteral=ecoreDiff_EEnum(), ecoreDiff_EEnumLiteral82=ecoreDiff_EEnum(), ecoreDiff_EEnumLiteral269=ecoreDiff_ChangedEEnumLiteral()), 0, '', '', ecoreDiff_EEnumLiteral=ecoreDiff_EEnum(), ecoreDiff_EEnumLiteral82=ecoreDiff_EEnum(), ecoreDiff_EEnumLiteral269=ecoreDiff_ChangedEEnumLiteral()) == None


from python_code import ecoreDiff_ChangedENamedElement
from python_code import ecoreDiff_ENamedElement

def test_ecoreDiff_ENamedElement___init__():
    assert ecoreDiff_ENamedElement.__init__(ecoreDiff_ENamedElement('', ecoreDiff_ENamedElement=ecoreDiff_ChangedENamedElement()), '', ecoreDiff_ENamedElement=ecoreDiff_ChangedENamedElement()) == None


from python_code import ecoreDiff_ChangedETypedElement
from python_code import ecoreDiff_EGenericType
from python_code import ecoreDiff_EObject
from python_code import ecoreDiff_ETypedElement

def test_ecoreDiff_ETypedElement___init__():
    assert ecoreDiff_ETypedElement.__init__(ecoreDiff_ETypedElement(False, False, 0, 0, ecoreDiff_ETypedElement=ecoreDiff_EObject(), ecoreDiff_ETypedElement68=ecoreDiff_EGenericType(), ecoreDiff_ETypedElement207=ecoreDiff_ChangedETypedElement()), False, False, 0, 0, ecoreDiff_ETypedElement=ecoreDiff_EObject(), ecoreDiff_ETypedElement68=ecoreDiff_EGenericType(), ecoreDiff_ETypedElement207=ecoreDiff_ChangedETypedElement()) == None

