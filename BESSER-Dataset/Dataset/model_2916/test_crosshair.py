from python_code import domainModel_Import

def test_domainModel_Import___init__():
    assert domainModel_Import.__init__(domainModel_Import(''), '') == None


from python_code import domainModel_PackageDeclaration

def test_domainModel_PackageDeclaration___init__():
    assert domainModel_PackageDeclaration.__init__(domainModel_PackageDeclaration('', domainModel_PackageDeclaration=set()), '', domainModel_PackageDeclaration=set()) == None

