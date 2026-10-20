from python_code import KM3_LocatedElement

def test_KM3_LocatedElement___init__():
    assert KM3_LocatedElement.__init__(KM3_LocatedElement(''), '') == None


from python_code import KM3_ModelElement
from python_code import KM3_Package

def test_KM3_ModelElement___init__():
    assert KM3_ModelElement.__init__(KM3_ModelElement('', contents=KM3_Package(), ModelElement=KM3_Package()), '', contents=KM3_Package(), ModelElement=KM3_Package()) == None

