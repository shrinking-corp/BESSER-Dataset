from python_code import ecoreDiff_ChangedEAnnotation
from python_code import ecoreDiff_EAnnotation
from python_code import ecoreDiff_EModelElement

def test_ecoreDiff_EAnnotation___init__():
    assert ecoreDiff_EAnnotation.__init__(ecoreDiff_EAnnotation('', ecoreDiff_EAnnotation5=set(), eAnnotations=ecoreDiff_EModelElement(), EAnnotation=ecoreDiff_EModelElement(), ecoreDiff_EAnnotation=set(), ecoreDiff_EAnnotation3=set(), ecoreDiff_EAnnotation112=ecoreDiff_ChangedEAnnotation()), '', ecoreDiff_EAnnotation5=set(), eAnnotations=ecoreDiff_EModelElement(), EAnnotation=ecoreDiff_EModelElement(), ecoreDiff_EAnnotation=set(), ecoreDiff_EAnnotation3=set(), ecoreDiff_EAnnotation112=ecoreDiff_ChangedEAnnotation()) == None

from python_code import ecoreDiff_ChangedEEnumLiteral
from python_code import ecoreDiff_EEnum
from python_code import ecoreDiff_EEnumLiteral

def test_ecoreDiff_EEnumLiteral___init__():
    assert ecoreDiff_EEnumLiteral.__init__(ecoreDiff_EEnumLiteral(0, '', '\x00\x00', eLiterals=ecoreDiff_EEnum(), EEnumLiteral=ecoreDiff_EEnum(), ecoreDiff_EEnumLiteral=ecoreDiff_ChangedEEnumLiteral()), 0, '', '', eLiterals=ecoreDiff_EEnum(), EEnumLiteral=ecoreDiff_EEnum(), ecoreDiff_EEnumLiteral=ecoreDiff_ChangedEEnumLiteral()) == None

from python_code import ecoreDiff_ChangedENamedElement
from python_code import ecoreDiff_ENamedElement

def test_ecoreDiff_ENamedElement___init__():
    assert ecoreDiff_ENamedElement.__init__(ecoreDiff_ENamedElement('', ecoreDiff_ENamedElement=ecoreDiff_ChangedENamedElement()), '', ecoreDiff_ENamedElement=ecoreDiff_ChangedENamedElement()) == None

from python_code import ecoreDiff_ChangedETypedElement
from python_code import ecoreDiff_EGenericType
from python_code import ecoreDiff_EObject
from python_code import ecoreDiff_ETypedElement

def test_ecoreDiff_ETypedElement___init__():
    assert ecoreDiff_ETypedElement.__init__(ecoreDiff_ETypedElement(False, False, 0, 0, False, False, ecoreDiff_ETypedElement=ecoreDiff_EObject(), ecoreDiff_ETypedElement88=ecoreDiff_EGenericType(), ecoreDiff_ETypedElement199=ecoreDiff_ChangedETypedElement()), False, False, 0, 0, False, False, ecoreDiff_ETypedElement=ecoreDiff_EObject(), ecoreDiff_ETypedElement88=ecoreDiff_EGenericType(), ecoreDiff_ETypedElement199=ecoreDiff_ChangedETypedElement()) == None
