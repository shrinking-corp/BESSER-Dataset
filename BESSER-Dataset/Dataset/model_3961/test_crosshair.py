from python_code import uml2CD_Association
from python_code import uml2CD_Property

def test_uml2CD_Association___init__():
    assert uml2CD_Association.__init__(uml2CD_Association(False, Association=uml2CD_Property(), Association96=uml2CD_Property(), association=set(), owningAssociation=set()), False, Association=uml2CD_Property(), Association96=uml2CD_Property(), association=set(), owningAssociation=set()) == None


from python_code import uml2CD_ElementImport
from python_code import uml2CD_Namespace
from python_code import uml2CD_PackageableElement

def test_uml2CD_ElementImport___init__():
    assert uml2CD_ElementImport.__init__(uml2CD_ElementImport('', ElementImport=uml2CD_Namespace(), uml2CD_ElementImport=uml2CD_PackageableElement(), elementImport=uml2CD_Namespace()), '', ElementImport=uml2CD_Namespace(), uml2CD_ElementImport=uml2CD_PackageableElement(), elementImport=uml2CD_Namespace()) == None


from python_code import uml2CD_Dependency
from python_code import uml2CD_NamedElement
from python_code import uml2CD_Namespace

def test_uml2CD_NamedElement___init__():
    assert uml2CD_NamedElement.__init__(uml2CD_NamedElement('', client=set(), uml2CD_NamedElement=uml2CD_Namespace(), supplier=set(), NamedElement=uml2CD_Dependency(), NamedElement115=uml2CD_Dependency()), '', client=set(), uml2CD_NamedElement=uml2CD_Namespace(), supplier=set(), NamedElement=uml2CD_Dependency(), NamedElement115=uml2CD_Dependency()) == None


from python_code import uml2CD_Namespace
from python_code import uml2CD_Package
from python_code import uml2CD_PackageImport

def test_uml2CD_PackageImport___init__():
    assert uml2CD_PackageImport.__init__(uml2CD_PackageImport('', PackageImport=uml2CD_Namespace(), uml2CD_PackageImport=uml2CD_Package(), packageImport=uml2CD_Namespace()), '', PackageImport=uml2CD_Namespace(), uml2CD_PackageImport=uml2CD_Package(), packageImport=uml2CD_Namespace()) == None


from python_code import uml2CD_BehavioralFeature
from python_code import uml2CD_Parameter
from python_code import uml2CD_ValueSpecification

def test_uml2CD_Parameter___init__():
    assert uml2CD_Parameter.__init__(uml2CD_Parameter('', Parameter=uml2CD_ValueSpecification(), Parameter70=uml2CD_BehavioralFeature(), ownedParameter=uml2CD_BehavioralFeature(), owningParameter=uml2CD_ValueSpecification()), '', Parameter=uml2CD_ValueSpecification(), Parameter70=uml2CD_BehavioralFeature(), ownedParameter=uml2CD_BehavioralFeature(), owningParameter=uml2CD_ValueSpecification()) == None

