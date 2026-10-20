from python_code import domainDsl_EType

def test_domainDsl_EType___init__():
    assert domainDsl_EType.__init__(domainDsl_EType(''), '') == None


from python_code import domainDsl_Import

def test_domainDsl_Import___init__():
    assert domainDsl_Import.__init__(domainDsl_Import(''), '') == None


from python_code import domainDsl_PackageDeclaration

def test_domainDsl_PackageDeclaration___init__():
    assert domainDsl_PackageDeclaration.__init__(domainDsl_PackageDeclaration('', domainDsl_PackageDeclaration=set()), '', domainDsl_PackageDeclaration=set()) == None

