from python_code import aGES_Import

def test_aGES_Import___init__():
    assert aGES_Import.__init__(aGES_Import(''), '') == None


from python_code import aGES_PackageDeclaration

def test_aGES_PackageDeclaration___init__():
    assert aGES_PackageDeclaration.__init__(aGES_PackageDeclaration('', aGES_PackageDeclaration=set()), '', aGES_PackageDeclaration=set()) == None

