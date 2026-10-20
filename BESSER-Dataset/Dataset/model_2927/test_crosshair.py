from python_code import ling_Import

def test_ling_Import___init__():
    assert ling_Import.__init__(ling_Import(''), '') == None


from python_code import ling_PackageDeclaration

def test_ling_PackageDeclaration___init__():
    assert ling_PackageDeclaration.__init__(ling_PackageDeclaration('', ling_PackageDeclaration=set()), '', ling_PackageDeclaration=set()) == None

