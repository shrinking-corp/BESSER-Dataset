from python_code import codemodel_CMElement

def test_codemodel_CMElement___init__():
    assert codemodel_CMElement.__init__(codemodel_CMElement(''), '') == None


from python_code import codemodel_CodeModule
from python_code import codemodel_Function

def test_codemodel_Function___init__():
    assert codemodel_Function.__init__(codemodel_Function('', codemodel_Function=codemodel_CodeModule(), codemodel_Function12=set(), codemodel_Function8=set(), codemodel_Function10=set()), '', codemodel_Function=codemodel_CodeModule(), codemodel_Function12=set(), codemodel_Function8=set(), codemodel_Function10=set()) == None


from python_code import codemodel_MatrixType

def test_codemodel_MatrixType___init__():
    assert codemodel_MatrixType.__init__(codemodel_MatrixType('', '\x00'), '\x00\x00', '') == None


from python_code import codemodel_VectorType

def test_codemodel_VectorType___init__():
    assert codemodel_VectorType.__init__(codemodel_VectorType(''), '') == None

