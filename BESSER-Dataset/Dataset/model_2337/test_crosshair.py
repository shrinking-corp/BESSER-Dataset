from python_code import persons_Person
from python_code import persons_PersonGroup

def test_persons_Person___init__():
    assert persons_Person.__init__(persons_Person('', persons_Person=persons_PersonGroup()), '', persons_Person=persons_PersonGroup()) == None

