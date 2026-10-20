from python_code import typeslibrary_TypesLibrary
from python_code import typeslibrary_TypesLibraryUser

def test_typeslibrary_TypesLibrary___init__():
    assert typeslibrary_TypesLibrary.__init__(typeslibrary_TypesLibrary('', typeslibrary_TypesLibrary=typeslibrary_TypesLibraryUser()), '', typeslibrary_TypesLibrary=typeslibrary_TypesLibraryUser()) == None


from python_code import typeslibrary_UserDefinedTypesLibrary

def test_typeslibrary_UserDefinedTypesLibrary___init__():
    assert typeslibrary_UserDefinedTypesLibrary.__init__(typeslibrary_UserDefinedTypesLibrary('\x00', typeslibrary_UserDefinedTypesLibrary=set()), '', typeslibrary_UserDefinedTypesLibrary=set()) == None

