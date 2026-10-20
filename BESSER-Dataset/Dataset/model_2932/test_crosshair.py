from python_code import domainModel_Import

def test_domainModel_Import___init__():
    assert domainModel_Import.__init__(domainModel_Import(''), '') == None


from python_code import domainModel_PackageDecl

def test_domainModel_PackageDecl___init__():
    assert domainModel_PackageDecl.__init__(domainModel_PackageDecl('', domainModel_PackageDecl=set()), '', domainModel_PackageDecl=set()) == None

