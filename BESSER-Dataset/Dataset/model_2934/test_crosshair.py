from python_code import domainmodel_Import

def test_domainmodel_Import___init__():
    assert domainmodel_Import.__init__(domainmodel_Import(''), '') == None


from python_code import domainmodel_PackageDeclaration

def test_domainmodel_PackageDeclaration___init__():
    assert domainmodel_PackageDeclaration.__init__(domainmodel_PackageDeclaration('', domainmodel_PackageDeclaration=set()), '', domainmodel_PackageDeclaration=set()) == None

