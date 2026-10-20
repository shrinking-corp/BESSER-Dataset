from python_code import myDsl_Import

def test_myDsl_Import___init__():
    assert myDsl_Import.__init__(myDsl_Import(''), '') == None


from python_code import myDsl_PackageDeclaration

def test_myDsl_PackageDeclaration___init__():
    assert myDsl_PackageDeclaration.__init__(myDsl_PackageDeclaration('', myDsl_PackageDeclaration=set()), '', myDsl_PackageDeclaration=set()) == None

