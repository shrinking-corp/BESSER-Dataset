from python_code import persons_NamedElement

def test_persons_NamedElement___init__():
    assert persons_NamedElement.__init__(persons_NamedElement(''), '') == None


from python_code import persons_Community
from python_code import persons_Facility
from python_code import persons_Person
from python_code import persons_TownHall

def test_persons_Person___init__():
    assert persons_Person.__init__(persons_Person('', persons_Person7=persons_TownHall(), persons_Person=persons_Community(), persons_Person19=persons_Facility()), '', persons_Person7=persons_TownHall(), persons_Person=persons_Community(), persons_Person19=persons_Facility()) == None

