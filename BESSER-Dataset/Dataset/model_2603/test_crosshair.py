from python_code import Persons_Person
from python_code import Persons_Persons

def test_Persons_Person___init__():
    assert Persons_Person.__init__(Persons_Person('', '', '\x00\x00', persons=Persons_Persons(), Person=Persons_Persons()), '', '', '', persons=Persons_Persons(), Person=Persons_Persons()) == None

