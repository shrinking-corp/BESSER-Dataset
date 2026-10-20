from python_code import domainmodel_Import

def test_domainmodel_Import___init__():
    assert domainmodel_Import.__init__(domainmodel_Import(''), '') == None


from python_code import domainmodel_PackageDec

def test_domainmodel_PackageDec___init__():
    assert domainmodel_PackageDec.__init__(domainmodel_PackageDec('', domainmodel_PackageDec=set()), '', domainmodel_PackageDec=set()) == None

