from python_code import Persons_NamedElement

def test_Persons_NamedElement___init__():
    assert Persons_NamedElement.__init__(Persons_NamedElement(''), '') == None


from python_code import Persons_Community
from python_code import Persons_Facility
from python_code import Persons_Person
from python_code import Persons_TownHall

def test_Persons_Person___init__():
    assert Persons_Person.__init__(Persons_Person('', Persons_Person=Persons_Community(), Persons_Person7=Persons_TownHall(), Persons_Person19=Persons_Facility()), '', Persons_Person=Persons_Community(), Persons_Person7=Persons_TownHall(), Persons_Person19=Persons_Facility()) == None

