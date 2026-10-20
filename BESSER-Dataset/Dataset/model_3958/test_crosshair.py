from python_code import KM3_LocatedElement

def test_KM3_LocatedElement___init__():
    assert KM3_LocatedElement.__init__(KM3_LocatedElement(''), '') == None


from python_code import KM3_ModelElement
from python_code import KM3_Package

def test_KM3_ModelElement___init__():
    assert KM3_ModelElement.__init__(KM3_ModelElement('', KM3_ModelElement=KM3_Package()), '', KM3_ModelElement=KM3_Package()) == None


from python_code import KM3_Classifier
from python_code import KM3_TypedElement

def test_KM3_TypedElement___init__():
    assert KM3_TypedElement.__init__(KM3_TypedElement('\x00\x00', '', '', '', KM3_TypedElement=KM3_Classifier()), '', '', '', '', KM3_TypedElement=KM3_Classifier()) == None

