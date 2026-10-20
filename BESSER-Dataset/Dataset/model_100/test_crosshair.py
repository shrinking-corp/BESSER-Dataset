from python_code import Core_IClassFile
from python_code import IType

def test_Core_IClassFile___init__():
    assert Core_IClassFile.__init__(Core_IClassFile('', '\x00', Core_IClassFile=IType()), '\x00\x00', '', Core_IClassFile=IType()) == None


from python_code import Core_IField

def test_Core_IField___init__():
    assert Core_IField.__init__(Core_IField('', '', '', '', ''), '', '', '', '', '') == None


from python_code import Core_IImportDeclaration

def test_Core_IImportDeclaration___init__():
    assert Core_IImportDeclaration.__init__(Core_IImportDeclaration('', '\x00'), '\x00\x00', '') == None


from python_code import Core_IJavaElement

def test_Core_IJavaElement___init__():
    assert Core_IJavaElement.__init__(Core_IJavaElement(''), '') == None


from python_code import Core_IMethod

def test_Core_IMethod___init__():
    assert Core_IMethod.__init__(Core_IMethod('', '', '', '', Core_IMethod=set()), '', '', '', '', Core_IMethod=set()) == None


from python_code import Core_IPackageFragment
from python_code import IPackageFragmentRoot

def test_Core_IPackageFragment___init__():
    assert Core_IPackageFragment.__init__(Core_IPackageFragment('', packageFragments=IPackageFragmentRoot(), Core_IPackageFragment=set(), Core_IPackageFragment16=set()), '', packageFragments=IPackageFragmentRoot(), Core_IPackageFragment=set(), Core_IPackageFragment16=set()) == None


from python_code import Core_ISourceRange

def test_Core_ISourceRange___init__():
    assert Core_ISourceRange.__init__(Core_ISourceRange('', '\x00'), '\x00\x00', '') == None


from python_code import Core_ISourceReference
from python_code import ISourceRange

def test_Core_ISourceReference___init__():
    assert Core_ISourceReference.__init__(Core_ISourceReference('', Core_ISourceReference=ISourceRange()), '', Core_ISourceReference=ISourceRange()) == None


from python_code import Core_IType

def test_Core_IType___init__():
    assert Core_IType.__init__(Core_IType('', '', Core_IType=set(), Core_IType38=set(), Core_IType40=set(), Core_IType42=set(), Core_IType45=set()), '', '', Core_IType=set(), Core_IType38=set(), Core_IType40=set(), Core_IType42=set(), Core_IType45=set()) == None


from python_code import Core_ITypeParameter

def test_Core_ITypeParameter___init__():
    assert Core_ITypeParameter.__init__(Core_ITypeParameter(''), '') == None


from python_code import Core_Parameter

def test_Core_Parameter___init__():
    assert Core_Parameter.__init__(Core_Parameter('', '\x00'), '\x00\x00', '') == None


from python_code import Core_PhysicalElement

def test_Core_PhysicalElement___init__():
    assert Core_PhysicalElement.__init__(Core_PhysicalElement('', '\x00'), '\x00\x00', '') == None

