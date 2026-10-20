from python_code import EPackage
from python_code import ecore_EClassifier

def test_ecore_EClassifier___init__():
    assert ecore_EClassifier.__init__(ecore_EClassifier('', '', '', '', eClassifiers=EPackage(), ecore_EClassifier=set()), '', '', '', '', eClassifiers=EPackage(), ecore_EClassifier=set()) == None

def test_ecore_EClassifier_isInstance():
    assert ecore_EClassifier.isInstance(ecore_EClassifier('', '', '\x00\x00', '', eClassifiers=EPackage(), ecore_EClassifier=set()), '') == None

def test_ecore_EClassifier_getClassifierID():
    assert ecore_EClassifier.getClassifierID(ecore_EClassifier('', '', '\x00\x00', '', eClassifiers=EPackage(), ecore_EClassifier=set())) == None


from python_code import EEnum
from python_code import ecore_EEnumLiteral

def test_ecore_EEnumLiteral___init__():
    assert ecore_EEnumLiteral.__init__(ecore_EEnumLiteral('', '', '\x00\x00', eLiterals=EEnum()), '', '', '', eLiterals=EEnum()) == None


from python_code import ecore_EModelElement

def test_ecore_EModelElement___init__():
    assert ecore_EModelElement.__init__(ecore_EModelElement(eModelElement=set()), eModelElement=set()) == None

def test_ecore_EModelElement_getEAnnotation():
    assert ecore_EModelElement.getEAnnotation(ecore_EModelElement(eModelElement=set()), 0) == None


from python_code import ecore_EObject

def test_ecore_EObject___init__():
    assert ecore_EObject.__init__(ecore_EObject()) == None

def test_ecore_EObject_eContents():
    assert ecore_EObject.eContents(ecore_EObject()) == None

def test_ecore_EObject_eContainmentFeature():
    assert ecore_EObject.eContainmentFeature(ecore_EObject()) == None

def test_ecore_EObject_eSet():
    assert ecore_EObject.eSet(ecore_EObject(), '', '') == None

def test_ecore_EObject_eIsProxy():
    assert ecore_EObject.eIsProxy(ecore_EObject()) == None

def test_ecore_EObject_eContainer():
    assert ecore_EObject.eContainer(ecore_EObject()) == None

def test_ecore_EObject_eResource():
    assert ecore_EObject.eResource(ecore_EObject()) == None

def test_ecore_EObject_eContainingFeature():
    assert ecore_EObject.eContainingFeature(ecore_EObject()) == None

def test_ecore_EObject_eIsSet():
    assert ecore_EObject.eIsSet(ecore_EObject(), '') == None

def test_ecore_EObject_eUnset():
    assert ecore_EObject.eUnset(ecore_EObject(), '') == None

def test_ecore_EObject_eInvoke():
    assert ecore_EObject.eInvoke(ecore_EObject(), '', '') == None

def test_ecore_EObject_eCrossReferences():
    assert ecore_EObject.eCrossReferences(ecore_EObject()) == None

def test_ecore_EObject_eAllContents():
    assert ecore_EObject.eAllContents(ecore_EObject()) == None

def test_ecore_EObject_op_eGet():
    assert ecore_EObject.op_eGet(ecore_EObject(), '') == None

def test_ecore_EObject_eClass():
    assert ecore_EObject.eClass(ecore_EObject()) == None

def test_ecore_EObject_eGet():
    assert ecore_EObject.eGet(ecore_EObject(), '', '') == None

