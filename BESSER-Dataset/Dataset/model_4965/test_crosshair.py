from python_code import Classifier
from python_code import km3_Class
from python_code import km3_Package
from python_code import km3_TypedElement

def test_km3_Class___init__():
    assert km3_Class.__init__(km3_Class('', owner8=set(), owner=set(), km3_Class=set(), km3_Class5=set(), Classifier=km3_TypedElement('', '', '\x00', '', km3_TypedElement=Classifier(), ModelElement=km3_Package())), '', owner8=set(), owner=set(), km3_Class=set(), km3_Class5=set(), Classifier=km3_TypedElement('', '', '', '', km3_TypedElement=Classifier(), ModelElement=km3_Package())) == None


from python_code import km3_LocatedElement

def test_km3_LocatedElement___init__():
    assert km3_LocatedElement.__init__(km3_LocatedElement(''), '') == None


from python_code import Package
from python_code import km3_ModelElement

def test_km3_ModelElement___init__():
    assert km3_ModelElement.__init__(km3_ModelElement('', contents=Package()), '', contents=Package()) == None


from python_code import Classifier
from python_code import Reference
from python_code import km3_Class
from python_code import km3_Package
from python_code import km3_Reference
from python_code import km3_StructuralFeature
from python_code import km3_TypedElement

def test_km3_Reference___init__():
    assert km3_Reference.__init__(km3_Reference('', km3_Reference=Reference(), StructuralFeature=km3_Class('', owner8=set(), owner=set(), km3_Class=set(), km3_Class5=set(), Classifier=km3_TypedElement('\x00', '', '', '', km3_TypedElement=Classifier(), ModelElement=km3_Package())), StructuralFeature13=km3_StructuralFeature(), StructuralFeature15=km3_StructuralFeature()), '', km3_Reference=Reference(), StructuralFeature=km3_Class('', owner8=set(), owner=set(), km3_Class=set(), km3_Class5=set(), Classifier=km3_TypedElement('', '', '', '', km3_TypedElement=Classifier(), ModelElement=km3_Package())), StructuralFeature13=km3_StructuralFeature(), StructuralFeature15=km3_StructuralFeature()) == None


from python_code import Classifier
from python_code import km3_Package
from python_code import km3_TypedElement

def test_km3_TypedElement___init__():
    assert km3_TypedElement.__init__(km3_TypedElement('', '', '', '', km3_TypedElement=Classifier(), ModelElement=km3_Package()), '', '', '', '', km3_TypedElement=Classifier(), ModelElement=km3_Package()) == None

