from python_code import cppmodel_CPPBasicType

def test_cppmodel_CPPBasicType___init__():
    assert cppmodel_CPPBasicType.__init__(cppmodel_CPPBasicType(''), '') == None


from python_code import cppmodel_CPPAttribute
from python_code import cppmodel_CPPClassRefAssocCollection

def test_cppmodel_CPPClassRefAssocCollection___init__():
    assert cppmodel_CPPClassRefAssocCollection.__init__(cppmodel_CPPClassRefAssocCollection('', cppmodel_CPPClassRefAssocCollection=cppmodel_CPPAttribute()), '', cppmodel_CPPClassRefAssocCollection=cppmodel_CPPAttribute()) == None


from python_code import cppmodel_CPPClassRefSimpleCollection

def test_cppmodel_CPPClassRefSimpleCollection___init__():
    assert cppmodel_CPPClassRefSimpleCollection.__init__(cppmodel_CPPClassRefSimpleCollection(''), '') == None


from python_code import cppmodel_CPPEnumerator

def test_cppmodel_CPPEnumerator___init__():
    assert cppmodel_CPPEnumerator.__init__(cppmodel_CPPEnumerator(''), '') == None


from python_code import cppmodel_CPPNamedElement
from python_code import cppmodel_OOPLNameProvider

def test_cppmodel_CPPNamedElement___init__():
    assert cppmodel_CPPNamedElement.__init__(cppmodel_CPPNamedElement('', cppmodel_CPPNamedElement=cppmodel_OOPLNameProvider()), '', cppmodel_CPPNamedElement=cppmodel_OOPLNameProvider()) == None

