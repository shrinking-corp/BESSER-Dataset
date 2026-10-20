from python_code import domainmodel_Import

def test_domainmodel_Import___init__():
    assert domainmodel_Import.__init__(domainmodel_Import(''), '') == None


from python_code import domainmodel_Entity
from python_code import domainmodel_Method

def test_domainmodel_Method___init__():
    assert domainmodel_Method.__init__(domainmodel_Method('', '\x00', domainmodel_Method=domainmodel_Entity()), '\x00\x00', '', domainmodel_Method=domainmodel_Entity()) == None


from python_code import domainmodel_PackageDeclaration

def test_domainmodel_PackageDeclaration___init__():
    assert domainmodel_PackageDeclaration.__init__(domainmodel_PackageDeclaration('', domainmodel_PackageDeclaration=set()), '', domainmodel_PackageDeclaration=set()) == None

