from python_code import Persons_Person
from python_code import Persons_PersonContainer

def test_Persons_Person___init__():
    assert Persons_Person.__init__(Persons_Person('', 0, Persons_Person=Persons_PersonContainer()), '', 0, Persons_Person=Persons_PersonContainer()) == None

