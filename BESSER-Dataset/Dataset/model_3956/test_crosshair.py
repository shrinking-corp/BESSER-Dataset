from python_code import Classes_Kernel_Association

def test_Classes_Kernel_Association___init__():
    assert Classes_Kernel_Association.__init__(Classes_Kernel_Association(False, association=set(), owningAssociation=set(), Classes_Kernel_Association=set()), True, association=set(), owningAssociation=set(), Classes_Kernel_Association=set()) == None


from python_code import Classes_Kernel_ElementImport
from python_code import Classes_Kernel_Type
from python_code import Namespace
from python_code import PackageableElement

def test_Classes_Kernel_ElementImport___init__():
    assert Classes_Kernel_ElementImport.__init__(Classes_Kernel_ElementImport('', '', Classes_Kernel_ElementImport=PackageableElement(), elementImport=Namespace()), '', '', Classes_Kernel_ElementImport=Classes_Kernel_Type(), elementImport=Namespace()) == None


from python_code import Classes_Kernel_Generalization_
from python_code import Classifier

def test_Classes_Kernel_Generalization____init__():
    assert Classes_Kernel_Generalization_.__init__(Classes_Kernel_Generalization_(False, Classes_Kernel_Generalization=Classifier(), generalization=Classifier(), generalization124=set()), False, Classes_Kernel_Generalization=Classifier(), generalization=Classifier(), generalization124=set()) == None


from python_code import Classes_Kernel_Package
from python_code import Package

def test_Classes_Kernel_Package___init__():
    assert Classes_Kernel_Package.__init__(Classes_Kernel_Package('', nestingPackage=set(), receivingPackage=set(), nestedPackage=Package(), Classes_Kernel_Package=set(), package=set()), '', nestingPackage=set(), receivingPackage=set(), nestedPackage=Package(), Classes_Kernel_Package=set(), package=set()) == None


from python_code import Classes_Kernel_PackageImport
from python_code import Namespace
from python_code import Package

def test_Classes_Kernel_PackageImport___init__():
    assert Classes_Kernel_PackageImport.__init__(Classes_Kernel_PackageImport('', Classes_Kernel_PackageImport=Package(), packageImport=Namespace()), '', Classes_Kernel_PackageImport=Package(), packageImport=Namespace()) == None


from python_code import Classes_Kernel_StructuralFeature

def test_Classes_Kernel_StructuralFeature___init__():
    assert Classes_Kernel_StructuralFeature.__init__(Classes_Kernel_StructuralFeature(True), False) == None


from python_code import Classes_Kernel_ElementImport
from python_code import Classes_Kernel_Namespace
from python_code import Classes_Kernel_Package
from python_code import Classes_Kernel_Type
from python_code import Classes_PowerTypes_GeneralizationSet
from python_code import Classifier
from python_code import Namespace
from python_code import Package
from python_code import PackageableElement

def test_Classes_PowerTypes_GeneralizationSet___init__():
    assert Classes_PowerTypes_GeneralizationSet.__init__(Classes_PowerTypes_GeneralizationSet(False, True, generalizationSet=set(), powertypeExtent=Classifier(), PackageableElement=Classes_Kernel_Namespace(), PackageableElement16=Classes_Kernel_ElementImport('', '', Classes_Kernel_ElementImport=Classes_Kernel_Type(), elementImport=Namespace()), PackageableElement27=Classes_Kernel_Package('', nestingPackage=set(), receivingPackage=set(), nestedPackage=Package(), Classes_Kernel_Package=set(), package=set())), False, False, generalizationSet=set(), powertypeExtent=Classifier(), PackageableElement=Classes_Kernel_Namespace(), PackageableElement16=Classes_Kernel_ElementImport('', '\x00', Classes_Kernel_ElementImport=PackageableElement(), elementImport=Namespace()), PackageableElement27=Classes_Kernel_Package('', nestingPackage=set(), receivingPackage=set(), nestedPackage=Package(), Classes_Kernel_Package=set(), package=set())) == None

