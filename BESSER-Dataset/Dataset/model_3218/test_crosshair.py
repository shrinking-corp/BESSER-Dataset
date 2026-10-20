from python_code import Core_ICompilationUnit
from python_code import Core_IImportDeclaration

def test_Core_IImportDeclaration___init__():
    assert Core_IImportDeclaration.__init__(Core_IImportDeclaration('', '\x00', Core_IImportDeclaration=Core_ICompilationUnit()), '\x00\x00', '', Core_IImportDeclaration=Core_ICompilationUnit()) == None


from python_code import Core_IJavaElement

def test_Core_IJavaElement___init__():
    assert Core_IJavaElement.__init__(Core_IJavaElement(''), '') == None


from python_code import Core_IPackageFragment
from python_code import Core_IPackageFragmentRoot

def test_Core_IPackageFragment___init__():
    assert Core_IPackageFragment.__init__(Core_IPackageFragment('', IPackageFragment=Core_IPackageFragmentRoot(), packageFragments=Core_IPackageFragmentRoot(), Core_IPackageFragment=set(), Core_IPackageFragment16=set()), '', IPackageFragment=Core_IPackageFragmentRoot(), packageFragments=Core_IPackageFragmentRoot(), Core_IPackageFragment=set(), Core_IPackageFragment16=set()) == None


from python_code import Core_PhysicalElement

def test_Core_PhysicalElement___init__():
    assert Core_PhysicalElement.__init__(Core_PhysicalElement('', '\x00'), '\x00\x00', '') == None

