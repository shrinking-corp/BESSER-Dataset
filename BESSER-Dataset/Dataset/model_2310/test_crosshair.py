from python_code import Persons_Female
from python_code import Persons_PersonsModel

def test_Persons_Female___init__():
    assert Persons_Female.__init__(Persons_Female(0, Person=Persons_PersonsModel()), 0, Person=Persons_PersonsModel()) == None


from python_code import Persons_Male
from python_code import Persons_PersonsModel

def test_Persons_Male___init__():
    assert Persons_Male.__init__(Persons_Male(0, Person=Persons_PersonsModel()), 0, Person=Persons_PersonsModel()) == None


from python_code import PersonsModel
from python_code import Persons_Person

def test_Persons_Person___init__():
    assert Persons_Person.__init__(Persons_Person('', Persons_Person=PersonsModel()), '', Persons_Person=PersonsModel()) == None

