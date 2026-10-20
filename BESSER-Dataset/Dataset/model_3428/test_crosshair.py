from python_code import people_Model
from python_code import people_Person

def test_people_Person___init__():
    assert people_Person.__init__(people_Person('', people_Person=people_Model()), '', people_Person=people_Model()) == None

