from python_code import person_DocumentRoot

def test_person_DocumentRoot___init__():
    assert person_DocumentRoot.__init__(person_DocumentRoot('', person_DocumentRoot=set(), person_DocumentRoot3=set(), person_DocumentRoot6=set()), '', person_DocumentRoot=set(), person_DocumentRoot3=set(), person_DocumentRoot6=set()) == None


from python_code import person_CompanyType
from python_code import person_PersonType

def test_person_PersonType___init__():
    assert person_PersonType.__init__(person_PersonType('\x00\x00', '', '', '', person_PersonType=person_CompanyType()), '', '', '', '', person_PersonType=person_CompanyType()) == None

