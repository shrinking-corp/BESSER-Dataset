from python_code import wh_Import

def test_wh_Import___init__():
    assert wh_Import.__init__(wh_Import(''), '') == None


from python_code import wh_PackageDeclaration

def test_wh_PackageDeclaration___init__():
    assert wh_PackageDeclaration.__init__(wh_PackageDeclaration('', wh_PackageDeclaration=set()), '', wh_PackageDeclaration=set()) == None

