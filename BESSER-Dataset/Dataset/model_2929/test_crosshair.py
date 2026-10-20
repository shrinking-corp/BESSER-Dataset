from python_code import myTuto_Import

def test_myTuto_Import___init__():
    assert myTuto_Import.__init__(myTuto_Import(''), '') == None


from python_code import myTuto_PackageDeclaration

def test_myTuto_PackageDeclaration___init__():
    assert myTuto_PackageDeclaration.__init__(myTuto_PackageDeclaration('', myTuto_PackageDeclaration=set()), '', myTuto_PackageDeclaration=set()) == None

