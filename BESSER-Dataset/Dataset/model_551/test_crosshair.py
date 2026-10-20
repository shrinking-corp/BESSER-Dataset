from python_code import familyTree_FamilyTree
from python_code import familyTree_Female
from python_code import familyTree_Male
from python_code import familyTree_Person

def test_familyTree_Person___init__():
    assert familyTree_Person.__init__(familyTree_Person('', '\x00', children=familyTree_Male(), children3=familyTree_Female(), leaves=familyTree_FamilyTree(), Person8=familyTree_Male(), Person=familyTree_FamilyTree(), Person12=familyTree_Female()), '\x00\x00', '', children=familyTree_Male(), children3=familyTree_Female(), leaves=familyTree_FamilyTree(), Person8=familyTree_Male(), Person=familyTree_FamilyTree(), Person12=familyTree_Female()) == None

