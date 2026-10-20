from python_code import a_Model
from python_code import a_PackageDeclaration

def test_a_PackageDeclaration___init__():
    assert a_PackageDeclaration.__init__(a_PackageDeclaration('\x00', a_PackageDeclaration=a_Model(), a_PackageDeclaration2=set()), '', a_PackageDeclaration=a_Model(), a_PackageDeclaration2=set()) == None

