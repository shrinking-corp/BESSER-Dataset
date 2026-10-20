from python_code import library_AbstractPerson

def test_library_AbstractPerson___init__():
    assert library_AbstractPerson.__init__(library_AbstractPerson(''), '') == None

def test_library_AbstractPerson_getLastName():
    assert library_AbstractPerson.getLastName(library_AbstractPerson('')) == None

def test_library_AbstractPerson_getFirstName():
    assert library_AbstractPerson.getFirstName(library_AbstractPerson('')) == None


from python_code import library_Library
from python_code import library_UoD

def test_library_Library___init__():
    assert library_Library.__init__(library_Library('', library_Library8=set(), library_Library11=set(), library_Library=library_UoD()), '', library_Library8=set(), library_Library11=set(), library_Library=library_UoD()) == None

