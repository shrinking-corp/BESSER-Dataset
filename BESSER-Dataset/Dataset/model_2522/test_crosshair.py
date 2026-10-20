from python_code import codemodel_CMElement
from python_code import codemodel_Root

def test_codemodel_CMElement___init__():
    assert codemodel_CMElement.__init__(codemodel_CMElement('', codemodel_CMElement=codemodel_Root()), '', codemodel_CMElement=codemodel_Root()) == None

